---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/qualys-asset-context/
title: Collect Qualys asset context logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T22:22:26.399535+00:00
---

# Collect Qualys asset context logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/qualys-asset-context/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Qualys asset context logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Qualys asset context logs to Google Security Operations using Google Cloud Storage.

Qualys asset context provides host asset inventory data (IP addresses, DNS names, operating system, cloud provider metadata, and tags) from the Qualys platform. Because this data is pulled from the Qualys API, a Cloud Run function periodically queries the Qualys Host List API, converts the XML response to JSON, and writes it to a Cloud Storage bucket, where Google SecOps ingests it.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A Google Cloud project with the Cloud Storage, Cloud Run, Pub/Sub, and Cloud Scheduler APIs enabled
  * Permissions to create and manage Cloud Storage buckets, service accounts, Cloud Run functions, Pub/Sub topics, and Cloud Scheduler jobs
  * A Qualys account with API access (a user with the **Manager** role, or a role that has API access and visibility of the assets you want to collect)



## Create a Cloud Storage bucket

  1. Go to the [Google Cloud console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. Go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details: 
     * **Name your bucket** : Enter a globally unique name (for example, `qualys-asset-context-logs`).
     * **Location type** : Choose based on your needs (Region, Dual-region, or Multi-region).
     * **Location** : Select the location (for example, `us-central1`).
     * **Storage class** : Select **Standard**.
     * **Access control** : Select **Uniform**.
  6. Click **Create**.



## Collect Qualys API credentials

  1. Sign in to the **Qualys** web application.
  2. Identify or create an API user: 
     * Go to **Users > User Management**.
     * Use an existing user, or click **New > User** and assign the **Manager** role (or a role with API access).
  3. Record the user's **username** and **password**.
  4. Identify your Qualys API server URL (it is specific to your Qualys platform, for example, `https://qualysapi.qg3.apps.qualys.com`). To find it, see [Identify your Qualys platform](https://www.qualys.com/platform-identification/).

**Note:** The Qualys FO API requires the `X-Requested-With` header on every request. The Cloud Run function sets this header automatically.



## Create a service account for the Cloud Run function

  1. Go to **IAM & Admin > Service Accounts**.
  2. Click **Create service account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `qualys-asset-context-sa`.
     * **Service account description** : Enter `Service account for Cloud Run function to collect Qualys asset context logs`.
  4. Click **Create and continue**.
  5. Grant the following roles: 
     * **Storage Object Admin** : write host records to the bucket.
     * **Cloud Run Invoker** : allow Pub/Sub to invoke the function.
  6. Click **Continue** , and then click **Done**.



### Grant the service account access to the Cloud Storage bucket

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (`qualys-asset-context-sa@<PROJECT_ID>.iam.gserviceaccount.com`).
     * **Assign roles** : Select **Storage Object Admin**.
  6. Click **Save**.



## Create a Pub/Sub topic

  1. Go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. In the **Topic ID** field, enter `qualys-asset-context-trigger`.
  4. Click **Create**.



## Create the Cloud Run function to collect logs

The Cloud Run function is triggered by Pub/Sub messages from Cloud Scheduler. It calls the Qualys FO Host List API, converts the XML response to JSON, and writes the host records to the bucket.

  1. Go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** to use the inline code editor.
  4. Provide the following configuration details: 
     * **Service name** : Enter `qualys-asset-context-collector`.
     * **Region** : Select the region matching your bucket (for example, `us-central1`).
     * **Runtime** : Select **Python 3.12** or later.
  5. In the **Trigger** section: 
     1. Click **Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , select `qualys-asset-context-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section, select **Require authentication**.
  7. Expand **Containers, Networking, Security** , and on the **Security** tab set **Service account** to `qualys-asset-context-sa`.
  8. On the **Containers > Variables & Secrets** tab, add the following environment variables:

Variable name | Example value  
---|---  
`GCS_BUCKET` | `qualys-asset-context-logs`  
`GCS_PREFIX` | `qualys-asset-context/`  
`QUALYS_BASE_URL` | `https://qualysapi.qg3.apps.qualys.com`  
`QUALYS_USERNAME` | `your-qualys-username`  
`QUALYS_PASSWORD` | `your-qualys-password`  
`TRUNCATION_LIMIT` | `1000`  
`HTTP_TIMEOUT` | `300`  
`MAX_PAGES` | `50`  
  9. Set the **Request timeout** to `600` seconds and **Memory** to **512 MiB** or higher.

  10. Click **Create**. After the service is created, the inline code editor opens.




### Add the function code

  1. In the **Function entry point** field, enter `main`.
  2. In the inline code editor, replace the contents of `main.py` with the following code:
         
         import functions_framework
         from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
         import os
         import time
         import uuid
         import json
         import base64
         import requests
         import xmltodict
         
         storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
         
         GCS_BUCKET = os.environ.get('GCS_BUCKET')
         GCS_PREFIX = os.environ.get('GCS_PREFIX', 'qualys-asset-context/')
         QUALYS_BASE_URL = os.environ.get('QUALYS_BASE_URL')
         QUALYS_USERNAME = os.environ.get('QUALYS_USERNAME')
         QUALYS_PASSWORD = os.environ.get('QUALYS_PASSWORD')
         TRUNCATION_LIMIT = int(os.environ.get('TRUNCATION_LIMIT', '1000'))
         HTTP_TIMEOUT = int(os.environ.get('HTTP_TIMEOUT', '300'))
         MAX_PAGES = int(os.environ.get('MAX_PAGES', '50'))
         
         def _headers():
             """Qualys FO API requires Basic auth and the X-Requested-With header."""
             token = base64.b64encode(f'{QUALYS_USERNAME}:{QUALYS_PASSWORD}'.encode()).decode()
             return {'Authorization': f'Basic {token}', 'X-Requested-With': 'Cloud Run function'}
         
         def _extract_hosts(xml_text):
             """Parse the FO Host List XML into (list_of_host_dicts, next_page_url)."""
             doc = xmltodict.parse(xml_text)
             response = (doc.get('HOST_LIST_OUTPUT') or {}).get('RESPONSE') or {}
             host_list = (response.get('HOST_LIST') or {}).get('HOST')
             if host_list is None:
                 hosts = []
             elif isinstance(host_list, list):
                 hosts = host_list
             else:
                 hosts = [host_list]
             # When the result is truncated, RESPONSE contains <WARNING><URL>...</URL></WARNING>.
             warning = response.get('WARNING')
             next_url = warning.get('URL') if isinstance(warning, dict) else None
             return hosts, next_url
         
         def _write_hosts(bucket, hosts, page_num):
             """Write one batch of hosts to GCS as JSON, one host per line."""
             ts_path = time.strftime('%Y/%m/%d', time.gmtime())
             uniq = f'{int(time.time() * 1e6)}_{uuid.uuid4().hex[:8]}'
             key = f'{GCS_PREFIX}{ts_path}/qualys_asset_context_p{page_num:03d}_{uniq}.json'
             lines = [json.dumps(host, separators=(',', ':')) for host in hosts]
             bucket.blob(key).[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)('\n'.join(lines), content_type='application/x-ndjson')
             return key
         
         @functions_framework.cloud_event
         def main(cloud_event):
             """Triggered by Pub/Sub to pull the Qualys host asset inventory and write it to GCS."""
             if not all([GCS_BUCKET, QUALYS_BASE_URL, QUALYS_USERNAME, QUALYS_PASSWORD]):
                 print('Error: missing required environment variables')
                 return
         
             bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(GCS_BUCKET)
             session = requests.Session()
             session.headers.update(_headers())
         
             url = f"{QUALYS_BASE_URL.rstrip('/')}/api/2.0/fo/asset/host/"
             params = {
                 'action': 'list',
                 'details': 'All',
                 'truncation_limit': TRUNCATION_LIMIT,
                 # show_cloud_tags, host_metadata, and show_tags add the cloud provider
                 # tags, cloud instance metadata, and asset tags that the parser maps.
                 'show_cloud_tags': 1,
                 'host_metadata': 'all',
                 'show_tags': 1,
             }
         
             pages = 0
             total = 0
             try:
                 while pages < MAX_PAGES:
                     resp = session.get(url, params=params, timeout=HTTP_TIMEOUT)
                     resp.raise_for_status()
                     hosts, next_url = _extract_hosts(resp.text)
                     if hosts:
                         _write_hosts(bucket, hosts, pages + 1)
                         total += len(hosts)
                     pages += 1
                     if not next_url:
                         break
                     # The pagination URL already includes every query parameter.
                     url, params = next_url, None
         
                 print(f'Wrote {total} hosts across {pages} pages')
             except Exception as e:
                 print(f'Error collecting Qualys asset context: {e}')
                 raise
         

  3. Create a `requirements.txt` file with the following contents:
         
         functions-framework==3.*
         google-cloud-storage==2.*
         requests>=2.31.0
         xmltodict>=0.13.0
         

  4. Click **Deploy** and wait for the deployment to complete.




## Create a Cloud Scheduler job

  1. Go to **Cloud Scheduler**.
  2. Click **Create job**.
  3. Provide the following configuration details: 
     * **Name** : Enter `qualys-asset-context-collector-daily`.
     * **Region** : Select the same region as the Cloud Run function.
     * **Frequency** : Enter `0 */6 * * *` (every six hours).
     * **Timezone** : Select **UTC**.
     * **Target type** : Select **Pub/Sub**.
     * **Topic** : Select `qualys-asset-context-trigger`.
     * **Message body** : Enter `{}`.
  4. Click **Create**.
  5. To verify the setup, click **Force run** on the job, and then check the Cloud Run logs and the bucket to confirm that host records were written.



## Configure a feed in Google SecOps to ingest Qualys asset context logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Qualys asset context logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Qualys asset context** as the **Log type**.
  7. Click **Get Service Account** next to the **Chronicle Service Account** field, and copy the service account email.
  8. Click **Next**.
  9. Specify values for the following input parameters: 
     * **Storage Bucket URI** : Enter `gs://qualys-asset-context-logs/qualys-asset-context/`. This URL must end with a trailing forward slash (/).
     * **Source deletion options** : Select the deletion option according to your preference.
     * **Maximum File Age** : Include files modified in the last number of days. Default is 180 days.
  10. Click **Next**.
  11. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.



## Grant the Google SecOps service account access to the bucket

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Paste the Google SecOps service account email from the feed setup.
     * **Assign roles** : Select **Storage Object Viewer** (or **Storage Object Admin** if you chose a deletion option).
  6. Click **Save**.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`ASSET_ID` | `entity.asset.asset_id` | Directly mapped  
`DNS_DATA.HOSTNAME` | `entity.asset.hostname` | Directly mapped  
`IP` | `entity.asset.ip` | Merged  
`OS` | `entity.asset.platform_software.platform` | Mapped: `(?i)windows` → `WINDOWS`  
`ID` | `entity.asset.product_object_id` | Directly mapped  
`dataset` | `relations` | Merged  
N/A | `entity.asset.platform_software.platform` | Constant: `WINDOWS`  
N/A | `metadata.entity_type` | Constant: `ASSET`  
N/A | `metadata.product_name` | Constant: `QUALYS ASSET CONTEXT`  
N/A | `metadata.vendor_name` | Constant: `QUALYS ASSET CONTEXT`  
`DNS_DATA.HOSTNAME` | `entity.entity.asset.hostname` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/qualys-asset-context-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
