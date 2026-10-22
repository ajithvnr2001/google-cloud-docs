---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/spycloud/
title: Collect SpyCloud logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:35:59.942947+00:00
---

# Collect SpyCloud logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/spycloud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect SpyCloud logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest SpyCloud logs to Google Security Operations using Google Cloud Storage V2.

SpyCloud is an account takeover prevention platform that provides breach and stolen credential intelligence. It delivers breach records, watchlist alerts, and compromised credential reports through a REST API.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * A SpyCloud account with API access and a valid API key



## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `spycloud-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Collect SpyCloud API credentials

### Obtain API key

  1. Sign in to the [SpyCloud portal](https://portal.spycloud.com/) as an administrator.
  2. Go to **Settings > API**.
  3. Copy and save the **API key** in a secure location.



### Verify permissions

To verify your API key has the required access:

  1. Sign in to the [SpyCloud portal](https://portal.spycloud.com/).
  2. Go to **Settings > API**.
  3. Verify the API key is active and has access to the required endpoints (breach data, watchlist, compass).
  4. If access is restricted, contact your SpyCloud administrator.



### Test API access

  * Test your credentials before proceeding with the integration:
        
        # Replace with your actual API key
        API_KEY="your-api-key"
        
        # Test API access - fetch watchlist data
        curl -v -H "X-API-Key: ${API_KEY}" \
          "https://api.spycloud.io/enterprise-v2/breach/data/watchlist?since=2024-01-01&until=2024-01-02"
        




## Create service account for Cloud Run function

The Cloud Run function needs a service account with permissions to write to GCS bucket and be invoked by Pub/Sub.

### Create service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `spycloud-collector-sa`.
     * **Service account description** : Enter `Service account for Cloud Run function to collect SpyCloud logs`.
  4. Click **Create and Continue**.
  5. In the **Grant this service account access to project** section, add the following roles: 
     1. Click **Select a role**.
     2. Search for and select **Storage Object Admin**.
     3. Click **\+ Add another role**.
     4. Search for and select **Cloud Run Invoker**.
     5. Click **\+ Add another role**.
     6. Search for and select **Cloud Functions Invoker**.
  6. Click **Continue**.
  7. Click **Done**.



These roles are required for:

  * **Storage Object Admin** : Write logs to GCS bucket and manage state files
  * **Cloud Run Invoker** : Allow Pub/Sub to invoke the function
  * **Cloud Functions Invoker** : Allow function invocation



### Grant IAM permissions on GCS bucket

Grant the service account write permissions on the GCS bucket:

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name (for example, `spycloud-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `spycloud-collector-sa@your-project.iam.gserviceaccount.com`).
     * **Assign roles** : Select **Storage Object Admin**.
  6. Click **Save**.



## Create Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `spycloud-trigger`.
     * Leave other settings as default.
  4. Click **Create**.



## Create Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from SpyCloud API and write them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `spycloud-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose the topic `spycloud-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select the service account `spycloud-collector-sa`.
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `spycloud-logs` | GCS bucket name  
`GCS_PREFIX` | `spycloud` | Prefix for log files  
`STATE_KEY` | `spycloud/state.json` | State file path  
`API_KEY` | `your-api-key` | SpyCloud API key  
`API_BASE` | `https://api.spycloud.io` | API base URL  
`MAX_RECORDS` | `10000` | Max records per run  
`LOOKBACK_DAYS` | `7` | Initial lookback period in days  
`STREAMS` | `watchlist,catalog` | Comma-separated data streams  
  10. Scroll down in the **Variables & Secrets** tab to **Requests** :

     * **Request timeout** : Enter `600` seconds (10 minutes).
  11. Go to the **Settings** tab in **Containers** :

     * In the **Resources** section: 
       * **Memory** : Select **512 MiB** or higher.
       * **CPU** : Select **1**.
  12. In the **Revision scaling** section:

     * **Minimum number of instances** : Enter `0`.
     * **Maximum number of instances** : Enter `100` (or adjust based on expected load).
  13. Click **Create**.

  14. Wait for the service to be created (1-2 minutes).

  15. After the service is created, the **inline code editor** will open automatically.




### Add function code

  1. Enter **main** in **Function entry point**.
  2. In the inline code editor, create two files:

     * First file: **main.py:**
           
           import functions_framework
           from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
           import json
           import os
           import urllib3
           from datetime import datetime, timezone, timedelta
           import time
           
           # Initialize HTTP client with timeouts
           http = urllib3.PoolManager(
             timeout=urllib3.Timeout(connect=5.0, read=30.0),
             retries=False,
           )
           
           # Initialize Storage client
           storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
           
           # Environment variables
           GCS_BUCKET = os.environ.get('GCS_BUCKET')
           GCS_PREFIX = os.environ.get('GCS_PREFIX', 'spycloud')
           STATE_KEY = os.environ.get('STATE_KEY', 'spycloud/state.json')
           API_KEY = os.environ.get('API_KEY', '')
           API_BASE = os.environ.get('API_BASE', 'https://api.spycloud.io').rstrip('/')
           MAX_RECORDS = int(os.environ.get('MAX_RECORDS', '10000'))
           LOOKBACK_DAYS = int(os.environ.get('LOOKBACK_DAYS', '7'))
           STREAMS = [s.strip() for s in os.environ.get('STREAMS', 'watchlist').split(',') if s.strip()]
           
           def parse_datetime(value: str) -> datetime:
             """Parse ISO datetime string to datetime object."""
             if [value](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.ObjectCustomContextPayload.html#google_cloud_storage_blob_ObjectCustomContextPayload_value).endswith("Z"):
               value = value[:-1] + "+00:00"
             return datetime.fromisoformat(value)
           
           @functions_framework.cloud_event
           def main(cloud_event):
             """
             Cloud Run function triggered by Pub/Sub to fetch SpyCloud logs and write to GCS.
           
             Args:
               cloud_event: CloudEvent object containing Pub/Sub message
             """
           
             if not all([GCS_BUCKET, API_KEY]):
               print('Error: Missing required environment variables')
               return
           
             try:
               bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(GCS_BUCKET)
           
               # Load state
               state = load_state(bucket, STATE_KEY)
           
               now = datetime.now(timezone.utc)
           
               # Determine date range
               if isinstance(state, dict) and [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get("last_date"):
                 since_date = state["last_date"]
               else:
                 since_date = (now - timedelta(days=LOOKBACK_DAYS)).strftime('%Y-%m-%d')
           
               until_date = now.strftime('%Y-%m-%d')
           
               print(f"Fetching data from {since_date} to {until_date}")
           
               report = {}
           
               if 'watchlist' in STREAMS:
                 print("Fetching watchlist breach data...")
                 count = pull_watchlist(bucket, since_date, until_date)
                 report['watchlist_records'] = count
           
               if 'catalog' in STREAMS:
                 print("Fetching breach catalog...")
                 count = pull_catalog(bucket, since_date, until_date)
                 report['catalog_records'] = count
           
               if 'compass' in STREAMS:
                 print("Fetching compass data...")
                 count = pull_compass(bucket, since_date, until_date)
                 report['compass_records'] = count
           
               # Update state
               save_state(bucket, STATE_KEY, until_date)
               print(f"Successfully processed: {json.dumps(report)}")
           
             except Exception as e:
               print(f'Error processing logs: {str(e)}')
               raise
           
           def load_state(bucket, key):
             """Load state from GCS."""
             try:
               blob = bucket.blob(key)
               if blob.exists():
                 state_data = blob.[download_as_text](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_download_as_text)()
                 return json.loads(state_data)
             except Exception as e:
               print(f"Warning: Could not load state: {e}")
           
             return {}
           
           def save_state(bucket, key, last_date: str):
             """Save the last query date to GCS state file."""
             try:
               state = {'last_date': last_date, 'last_event_time': datetime.now(timezone.utc).isoformat()}
               blob = bucket.blob(key)
               blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
                 json.dumps(state, indent=2),
                 content_type='application/json'
               )
               print(f"Saved state: last_date={last_date}")
             except Exception as e:
               print(f"Warning: Could not save state: {e}")
           
           def api_get(endpoint: str, params: dict = None):
             """Make authenticated GET request to SpyCloud API with rate limiting."""
             url = f"{API_BASE}{endpoint}"
             if params:
               query = '&'.join([f"{k}={v}" for k, v in params.items()])
               url = f"{url}?{query}"
           
             headers = {
               'X-API-Key': API_KEY,
               'Accept': 'application/json',
               'User-Agent': 'GoogleSecOps-SpyCloudCollector/1.0'
             }
           
             backoff = 1.0
             max_retries = 3
           
             for attempt in range(max_retries):
               response = http.request('GET', url, headers=headers)
           
               if response.status == 429:
                 retry_after = int(response.headers.get('Retry-After', str(int(backoff))))
                 print(f"Rate limited (429). Retrying after {retry_after}s...")
                 time.sleep(retry_after)
                 backoff = min(backoff * 2, 30.0)
                 continue
           
               if response.status != 200:
                 print(f"HTTP Error: {response.status} - {response.data.decode('utf-8')}")
                 return None
           
               return json.loads(response.data.decode('utf-8'))
           
             print(f"Failed after {max_retries} retries due to rate limiting")
             return None
           
           def write_ndjson(bucket, prefix: str, stream_name: str, records: list):
             """Write records to GCS as NDJSON."""
             if not records:
               return 0
           
             now = datetime.now(timezone.utc)
             timestamp = now.strftime('%Y%m%d_%H%M%S')
             object_key = f"{GCS_PREFIX}/{stream_name}/logs_{timestamp}.ndjson"
             blob = bucket.blob(object_key)
           
             ndjson = '\n'.join([json.dumps(record, ensure_ascii=False) for record in records]) + '\n'
             blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(ndjson, content_type='application/x-ndjson')
           
             print(f"Wrote {len(records)} records to gs://{GCS_BUCKET}/{object_key}")
             return len(records)
           
           def pull_watchlist(bucket, since_date: str, until_date: str):
             """Fetch watchlist breach data."""
             cursor = None
             all_records = []
           
             while True:
               params = {'since': since_date, 'until': until_date}
               if cursor:
                 params['cursor'] = cursor
           
               data = api_get('/enterprise-v2/breach/data/watchlist', params)
               if not data:
                 break
           
               results = data.get('results', [])
               if not results:
                 break
           
               all_records.extend(results)
           
               if len(all_records) >= MAX_RECORDS:
                 print(f"Reached max_records limit ({MAX_RECORDS})")
                 break
           
               cursor = data.get('cursor')
               if not cursor:
                 break
           
             return write_ndjson(bucket, GCS_PREFIX, 'watchlist', all_records)
           
           def pull_catalog(bucket, since_date: str, until_date: str):
             """Fetch breach catalog."""
             params = {'since': since_date, 'until': until_date}
             data = api_get('/enterprise-v2/breach/catalog', params)
             if not data:
               return 0
           
             results = data.get('results', [])
             return write_ndjson(bucket, GCS_PREFIX, 'catalog', results)
           
           def pull_compass(bucket, since_date: str, until_date: str):
             """Fetch compass findings."""
             cursor = None
             all_records = []
           
             while True:
               params = {'since': since_date, 'until': until_date}
               if cursor:
                 params['cursor'] = cursor
           
               data = api_get('/enterprise-v2/compass/data', params)
               if not data:
                 break
           
               results = data.get('results', [])
               if not results:
                 break
           
               all_records.extend(results)
           
               if len(all_records) >= MAX_RECORDS:
                 print(f"Reached max_records limit ({MAX_RECORDS})")
                 break
           
               cursor = data.get('cursor')
               if not cursor:
                 break
           
             return write_ndjson(bucket, GCS_PREFIX, 'compass', all_records)
           

     * Second file: **requirements.txt:**
           
           functions-framework==3.*
           google-cloud-storage==2.*
           urllib3>=2.0.0
           

  3. Click **Deploy** to save and deploy the function.

  4. Wait for deployment to complete (2-3 minutes).

**Note:** The Pub/Sub trigger configuration automatically creates the necessary subscriptions and permissions.



## Create Cloud Scheduler job

Cloud Scheduler will publish messages to the Pub/Sub topic at regular intervals, triggering the Cloud Run function.

  1. In the **GCP Console** , go to **Cloud Scheduler**.
  2. Click **Create Job**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | `spycloud-collector-daily`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 0 * * *` (daily at midnight)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the topic `spycloud-trigger`  
**Message body** | `{}` (empty JSON object)  
  4. Click **Create**.




### Schedule frequency options

Choose frequency based on log volume and latency requirements:

Frequency | Cron Expression | Use Case  
---|---|---  
Every 5 minutes | `*/5 * * * *` | High-volume, low-latency  
Every 15 minutes | `*/15 * * * *` | Medium volume  
Every hour | `0 * * * *` | Standard  
Every 6 hours | `0 */6 * * *` | Low volume, batch processing  
Daily | `0 0 * * *` | Historical data collection (recommended for breach data)  
  
### Test the integration

  1. In the **Cloud Scheduler** console, find your job (`spycloud-collector-daily`).
  2. Click **Force run** to trigger manually.
  3. Wait a few seconds and go to **Cloud Run > Services > spycloud-collector > Logs**.
  4. Verify the function executed successfully. Look for:
         
         Fetching data from YYYY-MM-DD to YYYY-MM-DD
         Fetching watchlist breach data...
         Wrote X records to gs://spycloud-logs/spycloud/watchlist/logs_YYYYMMDD_HHMMSS.ndjson
         Successfully processed: {"watchlist_records": X, "catalog_records": Y}
         

  5. Check the GCS bucket (`spycloud-logs`) to confirm logs were written.




If you see errors in the logs:

  * **HTTP 401** : Check API key in environment variables
  * **HTTP 403** : Verify API key has access to required endpoints
  * **HTTP 429** : Rate limiting - function will automatically retry with backoff
  * **Missing environment variables** : Check all required variables are set



## Configure a feed in Google SecOps to ingest SpyCloud logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `SpyCloud Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **SpyCloud** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address. You will use it in the next step.

**Note:** Each Google SecOps instance has a unique service account. Do not use service accounts from other documentation or examples.
  9. Click **Next**.

  10. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://spycloud-logs/spycloud/
           

       * Replace: 
         * `spycloud-logs`: Your GCS bucket name.
         * `spycloud`: Optional prefix/folder path where logs are stored (leave empty for root).
**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never** : Never deletes any files after transfers (recommended for testing).
       * **Delete transferred files** : Deletes files after successful transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.

**Note:** If you select a deletion option, the service account must have **Storage Object Admin** role instead of Storage Object Viewer. Update IAM permissions accordingly.
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days).

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).

     * **Ingestion labels** : The label to be applied to the events from this feed.

  11. Click **Next**.

  12. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## Grant IAM permissions to the Google SecOps service account

The Google SecOps service account needs **Storage Object Viewer** role on your GCS bucket.

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name (`spycloud-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Paste the Google SecOps service account email.
     * **Assign roles** : Select **Storage Object Viewer**.
  6. Click **Save**.

**Note:** If you plan to use the deletion option "Delete transferred files" or "Delete transferred files and empty directories," grant **Storage Object Admin** role instead of Storage Object Viewer.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
av_softwares, assets.av_softwares, assets.country, assets.country_code, assets.display_resolution, assets.email, assets.full_name, assets.infected_machine_id, assets.infected_path, assets.infected_time, assets.ip_addresses, assets.keyboard_languages, assets.password, assets.target_url, assets.username, assets.user_browser, assets.user_hostname, assets.user_os, assets.user_sys_registered_owner | additional.fields | Merged from labels created from these fields and av_software_list  
password | extensions.auth.auth_details | Value copied directly  
when | metadata.event_timestamp | Parsed as ISO8601 timestamp  
| metadata.event_type | Set based on conditions: NETWORK_CONNECTION if has_principal, has_target, has_network; USER_UNCATEGORIZED if has_principal and has_principal_userid; STATUS_UPDATE if has_principal and not has_principal_ip; else GENERIC_EVENT; or USER_UNCATEGORIZED if user_hostname, ip, or infected_machine_id present  
infected_time | metadata.ingested_timestamp | Parsed as timestamp with formats yyyy-MM-ddTHH:mm:ssZ, RFC 3339, ISO8601  
log_id, assets.log_id, uuid | metadata.product_log_id | Value from log_id if not empty, else assets.log_id, else uuid  
user_os | network.http.parsed_user_agent | Converted to parsed user agent  
user_os | network.http.user_agent | Value copied directly  
cookie_domain | principal.administrative_domain | Value copied directly  
country | principal.asset.location.country_or_region | Value copied directly  
infected_machine_id | principal.asset_id | Concatenated as "id: " + infected_machine_id  
infected_path | principal.file.full_path | Value copied directly  
user_hostname, domain | principal.hostname | Set to user_hostname if not empty, then to domain if not empty  
ip, ip_addresses | principal.ip | Merged from ip and ip_addresses array  
country_code | principal.resource.attribute.labels | Merged from country_code_label created from country_code  
id | principal.resource.id | Value copied directly (converted to string)  
homepage | principal.url | Value copied directly  
email | principal.user.email_addresses | Value copied directly  
full_name | principal.user.user_display_name | Value copied directly  
user_sys_registered_owner, email_username | principal.user.userid | Set to user_sys_registered_owner, then to email_username if not empty  
confidence | security_result.confidence_details | Converted to string  
description | security_result.description | Value copied directly  
cookie_expiration, cookie_name, cookie_subdomain, cookie_value, day, document_id, locality_zone, source_id, spycloud_publishdate, spycloud_publish_date, user_browser, infected_time, timezone, password_type, password_plaintext, email_domain, api_token, account_status, breach_category, breach_main_category, consumer_category, malware_family, num_records, premium_flag, sensitive_source, short_title, site_description, title, tlp, type, display_resolution, keyboard_languages | security_result.detection_fields | Merged from labels created from these fields  
severity | security_result.severity | Set to LOW if "2", INFORMATIONAL if "5", HIGH if "20", CRITICAL if "25" or "26"  
severity | security_result.severity_details | Value copied directly  
target_subdomain | target.administrative_domain | Value copied directly  
target_domain | target.asset.hostname | Value copied directly  
target_domain | target.hostname | Value copied directly  
target_url | target.url | Value copied directly  
username | target.user.userid | Value copied directly  
| metadata.product_name | Set to "SPYCLOUD"  
| metadata.vendor_name | Set to "SpyCloud"  
`spycloud_publish_date", "infected_time", and "timezone` | `security_result.detection_fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/spycloud-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
