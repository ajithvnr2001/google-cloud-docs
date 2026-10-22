---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/group-ib/
title: Collect Group-IB Threat Intelligence logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:37:27.418518+00:00
---

# Collect Group-IB Threat Intelligence logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/group-ib/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Group-IB Threat Intelligence logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Group-IB Threat Intelligence logs to Google Security Operations using Google Cloud Storage.

Group-IB Threat Intelligence & Attribution (TI&A) is a cyber threat intelligence platform that provides real-time data on threat actors, indicators of compromise (IOCs), malware, command-and-control (C2) infrastructure, compromised credentials, phishing campaigns, and vulnerabilities. It aggregates intelligence from open, deep, and dark web sources, enabling security teams to proactively detect and respond to threats.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A Group-IB TI&A account with API access enabled
  * Access to the Group-IB TI&A portal (`tap.group-ib.com`)
  * A Google Cloud project with the following APIs enabled: 
    * Cloud Storage API
    * Cloud Functions API
    * Cloud Scheduler API
    * Cloud Build API



## Generate Group-IB API key

  1. Sign in to the **Group-IB TI &A** portal at `https://tap.group-ib.com`.
  2. Click your **name** in the top-right corner and select **Profile**.
  3. Click **Go to my settings**.
  4. Go to the **Security and Access** tab.
  5. In the **Personal token** section, click **Generate new token**.
  6. Copy and save the **API key** securely.

**Note:** The API key is used as a password together with your email address for HTTP Basic authentication. Store it securely. If you lose the key, you must generate a new one.

**Important:** Contact Group-IB support to allowlist the IP address of your Cloud Function (or NAT Gateway) so that API requests are not blocked.

## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `groupib-ti-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
  6. Click **Create**.




## Deploy Cloud Function to pull Group-IB data

Create a Cloud Function that pulls threat intelligence data from the Group-IB TI&A API and writes it to the GCS bucket as NDJSON files for Google SecOps to ingest.

### Create the Cloud Function

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Go to **Cloud Functions**.
  3. Click **Create Function**.
  4. Provide the following configuration details:

Setting | Value  
---|---  
**Environment** | 2nd gen  
**Function name** | `groupib-to-gcs`  
**Region** | Select the region closest to your GCS bucket  
**Trigger type** | HTTPS  
**Authentication** | Require authentication  
**Memory allocated** | 512 MB (increase if fetching large collections)  
**Timeout** | 540 seconds  
  5. Click **Next**.

  6. Set the **Runtime** to `Python 3.11` (or later).

  7. Set the **Entry point** to `main`.

  8. Replace the contents of `main.py` with the following code:
         
         import json
         import os
         import requests
         import functions_framework
         from datetime import datetime, timedelta, timezone
         from urllib.parse import urljoin
         from requests.auth import HTTPBasicAuth
         from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
         
         GIB_API_URL = os.environ.get('GIB_API_URL', 'https://tap.group-ib.com/api/v2/')
         GIB_USERNAME = os.environ.get('GIB_USERNAME')
         GIB_API_KEY = os.environ.get('GIB_API_KEY')
         GCS_BUCKET = os.environ.get('GCS_BUCKET')
         GCS_PREFIX = os.environ.get('GCS_PREFIX', 'groupib-ti')
         COLLECTIONS = os.environ.get('GIB_COLLECTIONS', 'compromised/account,malware/cnc,apt/threat,hi/threat').split(',')
         DEFAULT_DAYS_BACK = int(os.environ.get('DEFAULT_DAYS_BACK', '3'))
         
         # Max items per request: 100 for most collections, 20 for apt/threat and hi/threat
         BIG_DATA_COLLECTIONS = ['apt/threat', 'hi/threat']
         
         # File to persist seqUpdate values between runs (use GCS for durability)
         STATE_BLOB = '_state/seq_updates.json'
         
         def load_state():
             """Load seqUpdate state from GCS."""
             client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
             bucket = client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(GCS_BUCKET)
             blob = bucket.blob(f"{GCS_PREFIX}/{STATE_BLOB}")
             if blob.exists():
                 return json.loads(blob.[download_as_text](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_download_as_text)())
             return {}
         
         def save_state(state):
             """Save seqUpdate state to GCS."""
             client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
             bucket = client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(GCS_BUCKET)
             blob = bucket.blob(f"{GCS_PREFIX}/{STATE_BLOB}")
             blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(json.dumps(state), content_type='application/json')
         
         def gib_request(session, url, params=None):
             """Send authenticated GET request to Group-IB API."""
             resp = session.get(url, params=params)
             if resp.status_code == 301:
                 raise Exception('IP not whitelisted by Group-IB. Contact Group-IB support.')
             resp.raise_for_status()
             return resp.json()
         
         def get_seq_update_by_date(session, collection, date_str):
             """Get seqUpdate value for a collection starting from a given date."""
             url = urljoin(GIB_API_URL, 'sequence_list')
             data = gib_request(session, url, {'date': date_str, 'collection': collection})
             return data.get('list', {}).get(collection)
         
         def fetch_collection(session, collection, seq_update):
             """Fetch all new items from a collection starting after the given seqUpdate."""
             limit = 20 if collection in BIG_DATA_COLLECTIONS else 100
             url = urljoin(GIB_API_URL, f"{collection}/updated")
             all_items = []
             last_seq = seq_update
         
             while True:
                 data = gib_request(session, url, {'seqUpdate': str(last_seq), 'limit': limit})
                 items = data.get('items', [])
                 if not items:
                     break
                 all_items.extend(items)
                 last_seq = items[-1].get('seqUpdate')
         
             return all_items, last_seq
         
         def write_to_gcs(items, collection_name):
             """Write items to GCS as NDJSON."""
             if not items:
                 return 0
             client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
             bucket = client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(GCS_BUCKET)
             timestamp = datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')
             safe_name = collection_name.replace('/', '_')
             blob_path = f"{GCS_PREFIX}/{safe_name}_{timestamp}.ndjson"
             blob = bucket.blob(blob_path)
             ndjson = '\n'.join(json.dumps(item, ensure_ascii=False) for item in items) + '\n'
             blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(ndjson, content_type='application/x-ndjson')
             return len(items)
         
         @functions_framework.http
         def main(request):
             """Cloud Function entry point."""
             session = requests.Session()
             session.auth = HTTPBasicAuth(GIB_USERNAME, GIB_API_KEY)
             session.headers.update({'Accept': '*/*'})
         
             state = load_state()
             total = 0
         
             for collection in COLLECTIONS:
                 collection = collection.strip()
                 seq_update = [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get(collection)
         
                 if seq_update is None:
                     default_date = (datetime.now(timezone.utc) - timedelta(days=DEFAULT_DAYS_BACK)).strftime('%Y-%m-%d')
                     seq_update = get_seq_update_by_date(session, collection, default_date)
                     if seq_update is None:
                         continue
         
                 items, last_seq = fetch_collection(session, collection, seq_update)
                 if items:
                     write_to_gcs(items, collection)
                     total += len(items)
                 state[collection] = last_seq
         
             save_state(state)
             return json.dumps({'status': 'success', 'total_items': total}), 200
         

  9. Replace the contents of `requirements.txt` with the following dependencies:
         
         functions-framework==3.*
         requests>=2.28.0
         google-cloud-storage>=2.0.0
         

  10. Click **Deploy**.




### Configure environment variables

  1. After deployment, go to your function details page.
  2. Click **Edit**.
  3. Expand the **Runtime, build, connections and security settings** section.
  4. Under **Runtime environment variables** , add the following variables:

Variable | Value  
---|---  
`GIB_API_URL` | `https://tap.group-ib.com/api/v2/` (or `https://bt.group-ib.com/api/v2/` depending on your region)  
`GIB_USERNAME` | Your Group-IB account email address  
`GIB_API_KEY` | Your Group-IB API key (personal token)  
`GCS_BUCKET` | Your GCS bucket name (for example, `groupib-ti-logs`)  
`GCS_PREFIX` | Prefix for log files (for example, `groupib-ti`)  
`GIB_COLLECTIONS` | Comma-separated list of collections to fetch (see below)  
`DEFAULT_DAYS_BACK` | Number of days to look back on first run (default: `3`)  
  5. Click **Deploy**.

**Note:** For production environments, store sensitive values (`GIB_API_KEY`) in **Secret Manager** instead of plain environment variables. Reference them using the **Reference a secret** option in the function configuration.



### Available Group-IB collections

Configure the `GIB_COLLECTIONS` variable with the collections relevant to your use case:

Collection | Description | Max limit  
---|---|---  
`compromised/account` | Compromised account credentials (login, password, domain) | 100  
`compromised/card` | Compromised bank cards | 100  
`compromised/mule` | Money mule accounts | 100  
`compromised/imei` | Compromised mobile device IMEIs | 100  
`compromised/file` | Compromised files with malware attribution | 100  
`attacks/ddos` | DDoS attack data (target IPs, domains) | 100  
`attacks/deface` | Website defacement incidents | 100  
`attacks/phishing` | Phishing URLs and domains | 100  
`attacks/phishing_kit` | Phishing kit hashes and target brands | 100  
`bp/phishing` | Brand protection — phishing incidents | 100  
`bp/phishing_kit` | Brand protection — phishing kits | 100  
`hi/threat` | Cybercriminal (HI) threat reports with IOCs and MITRE ATT&CK mapping | 20  
`hi/threat_actor` | Cybercriminal threat actor profiles | 100  
`apt/threat` | APT (nation-state) threat reports with IOCs and MITRE ATT&CK mapping | 20  
`apt/threat_actor` | APT threat actor profiles | 100  
`malware/cnc` | Command-and-Control server indicators (IPs, domains) | 100  
`malware/malware` | Malware descriptions and threat levels | 100  
`malware/targeted_malware` | Targeted malware samples (hashes, filenames) | 100  
`osi/git_leak` | Git repository data leaks | 100  
`osi/public_leak` | Public data leaks (pastes, dumps) | 100  
`osi/vulnerability` | Vulnerability data with CVSS scores | 100  
`suspicious_ip/tor_node` | Tor exit node IP addresses | 100  
`suspicious_ip/open_proxy` | Open proxy IP addresses | 100  
`suspicious_ip/socks_proxy` | SOCKS proxy IP addresses | 100  
  
  * **Example** : To collect compromised credentials, C2 infrastructure, and APT data:
        
        compromised/account,malware/cnc,apt/threat,hi/threat
        

**Note:** The `apt/threat` and `hi/threat` collections have a maximum limit of 20 items per API request due to large response sizes. The Cloud Function handles this automatically. If using a POC or partner license, access to data may be limited to 30 days. Do not use IP addresses from `attacks/phishing` for detection — this may cause many false positives. Focus only on URLs.



## Schedule the Cloud Function

Use Cloud Scheduler to trigger the function at regular intervals.

  1. Go to **Cloud Scheduler** in the Google Cloud Console.
  2. Click **Create Job**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | `groupib-to-gcs-schedule`  
**Region** | Same region as your Cloud Function  
**Frequency** | `0 */1 * * *` (every hour) or `0 0 * * *` (daily)  
**Timezone** | Select your timezone  
  4. Under **Configure the execution** :

     * **Target type** : Select **HTTP**.
     * **URL** : Enter the Cloud Function trigger URL.
     * **HTTP method** : Select **POST**.
     * **Auth header** : Select **Add OIDC token**.
     * **Service account** : Select a service account with `roles/cloudfunctions.invoker` permission.
  5. Click **Create**.

**Note:** The Cloud Function tracks its position using `seqUpdate` values stored in GCS. On the first run, it looks back `DEFAULT_DAYS_BACK` days (default: 3). Subsequent runs pick up where the previous run left off, regardless of the scheduler frequency.



## Test the data export

  1. In the Cloud Scheduler console, click **Force Run** next to your job to trigger the function manually.
  2. Check the Cloud Function logs in **Cloud Logging** to verify that data was fetched from Group-IB.
  3. Go to **Cloud Storage > Buckets** in the Google Cloud Console.
  4. Click your bucket name (for example, `groupib-ti-logs`).
  5. Navigate to the prefix folder (for example, `groupib-ti/`).
  6. Verify that new `.ndjson` files are appearing in the bucket.

**Note:** Each log file is named with a timestamp in the format `{collection}_{YYYYMMDD_HHMMSS}.ndjson` (for example, `ioc_common_20260318_120000.ndjson`).



## Retrieve the Google SecOps service account

Google SecOps uses a unique service account to read data from your GCS bucket. You must grant this service account access to your bucket.

### Get the service account email

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Group-IB Threat Intelligence`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Group-IB Threat Intelligence** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email is displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Don't use service accounts from other documentation or examples.



## Grant IAM permissions to the Google SecOps service account

The Google SecOps service account needs **Storage Object Viewer** role on your GCS bucket.

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name (for example, `groupib-ti-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Paste the Google SecOps service account email.
     * **Assign roles** : Select **Storage Object Viewer**.
  6. Click **Save**.

**Note:** If you plan to use the deletion option "Delete transferred files" or "Delete transferred files and empty directories," grant **Storage Object Admin** role instead of **Storage Object Viewer**.



## Configure a feed in Google SecOps to ingest Group-IB Threat Intelligence logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Group-IB Threat Intelligence`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Group-IB Threat Intelligence** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://groupib-ti-logs/groupib-ti/
           

Replace:

       * `groupib-ti-logs`: Your GCS bucket name.
       * `groupib-ti`: The prefix/folder path where logs are stored.
**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never** : Never deletes any files after transfers (recommended for testing).
       * **Delete transferred files** : Deletes files after successful transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.
**Note:** If you select a deletion option, the service account must have **Storage Object Admin** role instead of **Storage Object Viewer**. Update IAM permissions accordingly.
     * **Maximum File Age** : Include files modified in the last number of days. Default is 180 days.

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).

     * **Ingestion labels** : The label to be applied to the events from this feed.

  9. Click **Next**.

  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
