---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/watchguard-edr/
title: Collect WatchGuard EDR logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:07:38.145441+00:00
---

# Collect WatchGuard EDR logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/watchguard-edr/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect WatchGuard EDR logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

**Note:** This feature is covered by [Pre-GA Offerings Terms](https://chronicle.security/legal/service-terms/) of the Google Security Operations Service Specific Terms. Pre-GA features might have limited support, and changes to pre-GA features might not be compatible with other pre-GA versions. For more information, see the [Google SecOps Technical Support Service guidelines](https://chronicle.security/legal/technical-support-services-guidelines/) and the [Google SecOps Service Specific Terms](https://chronicle.security/legal/service-terms/).  
If this feature isn't visible in your environment, see [Manage preview features](https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage) or contact your system administrator.

This document explains how to ingest WatchGuard EDR logs to Google Security Operations using Google Cloud Storage V2.

WatchGuard EDR (formerly Panda Adaptive Defense) is a cloud-managed endpoint detection and response platform providing advanced threat protection, behavioral analysis, and threat hunting. The WatchGuard Cloud API provides programmatic access to security event data including detections, indicators of attack, and threat intelligence logs.

## Before you begin

Make sure that you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * Privileged access to the WatchGuard Cloud console with administrator permissions
  * A WatchGuard Cloud API key or OAuth2 credentials



## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `watchguard-edr-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Collect WatchGuard EDR API credentials

### Obtain API credentials

  1. Sign in to the [WatchGuard Cloud](https://cloud.watchguard.com/) console as an administrator.
  2. Go to **Administration > Managed Access**.
  3. Click **API Access** or navigate to the API key management section.
  4. Click **Generate API Key**.
  5. Enter a name for the API key (for example, `Google SecOps Integration`).
  6. Copy and save the following details in a secure location:

     * **API Key ID** : The API access key
     * **API Secret** : The API secret key
     * **Account ID** : Your WatchGuard Cloud account ID
**Note:** The API credentials are displayed only once. Store them securely. If lost, you will need to regenerate them.



### Determine API base URL

The WatchGuard Cloud API base URL depends on your data center region:

Region | API Base URL  
---|---  
US | `https://api.usa.cloud.watchguard.com`  
EU | `https://api.eu.cloud.watchguard.com`  
**Note:** Confirm your region from the WatchGuard Cloud console URL or your account documentation.

### Test API access

  * Test your credentials before proceeding with the integration:
        
        # Replace with your actual credentials
        WG_API_KEY="your-api-key-id"
        WG_API_SECRET="your-api-secret"
        WG_ACCOUNT_ID="your-account-id"
        WG_BASE_URL="https://api.usa.cloud.watchguard.com"
        
        # Get access token
        TOKEN=$(curl -s -X POST "${WG_BASE_URL}/oauth/token" \
          -H "Content-Type: application/x-www-form-urlencoded" \
          -d "grant_type=client_credentials&client_id=${WG_API_KEY}&client_secret=${WG_API_SECRET}&scope=api-access" \
          | jq -r '.access_token')
        
        # Test API access - list indicators
        curl -s -X GET "${WG_BASE_URL}/rest/aether/v1/accounts/${WG_ACCOUNT_ID}/indicators?$top=1" \
          -H "Authorization: Bearer ${TOKEN}"
        




## Create service account for Cloud Run function

The Cloud Run function needs a service account with permissions to write to GCS bucket and be invoked by Pub/Sub.

### Create service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `watchguard-edr-logs-collector-sa`
     * **Service account description** : Enter `Service account for Cloud Run function to collect WatchGuard EDR logs`
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
  2. Click on your bucket name (for example, `watchguard-edr-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `watchguard-edr-logs-collector-sa@PROJECT_ID.iam.gserviceaccount.com`)
     * **Assign roles** : Select **Storage Object Admin**
  6. Click **Save**.



## Create Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `watchguard-edr-logs-trigger`
     * Leave other settings as default
  4. Click **Create**.



## Create Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from the WatchGuard Cloud API and write them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `watchguard-edr-logs-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose the topic `watchguard-edr-logs-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select the service account `watchguard-edr-logs-collector-sa`.
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `watchguard-edr-logs` | GCS bucket name  
`GCS_PREFIX` | `watchguard` | Prefix for log files  
`STATE_KEY` | `watchguard/state.json` | State file path  
`WG_API_KEY` | `your-api-key-id` | WatchGuard Cloud API key ID  
`WG_API_SECRET` | `your-api-secret` | WatchGuard Cloud API secret  
`WG_ACCOUNT_ID` | `your-account-id` | WatchGuard Cloud account ID  
`WG_API_BASE` | `https://api.usa.cloud.watchguard.com` | WatchGuard Cloud API base URL  
`MAX_RECORDS` | `5000` | Max records per run  
`PAGE_SIZE` | `1000` | Records per page  
`LOOKBACK_HOURS` | `24` | Initial lookback period  
  10. In the **Variables & Secrets** section, scroll down to **Requests** :

     * **Request timeout** : Enter `600` seconds (10 minutes)
  11. Go to the **Settings** tab:

     * In the **Resources** section: 
       * **Memory** : Select **512 MiB** or higher
       * **CPU** : Select **1**
  12. In the **Revision scaling** section:

     * **Minimum number of instances** : Enter `0`
     * **Maximum number of instances** : Enter `100` (or adjust based on expected load)
  13. Click **Create**.

  14. Wait for the service to be created (1-2 minutes).

  15. After the service is created, the **inline code editor** will open automatically.




### Add function code

  1. Enter **main** in the **Entry point** field.
  2. In the inline code editor, create two files:

     * **main.py:**
           
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
           GCS_PREFIX = os.environ.get('GCS_PREFIX', 'watchguard')
           STATE_KEY = os.environ.get('STATE_KEY', 'watchguard/state.json')
           WG_API_KEY = os.environ.get('WG_API_KEY')
           WG_API_SECRET = os.environ.get('WG_API_SECRET')
           WG_ACCOUNT_ID = os.environ.get('WG_ACCOUNT_ID')
           WG_API_BASE = os.environ.get('WG_API_BASE', 'https://api.usa.cloud.watchguard.com')
           MAX_RECORDS = int(os.environ.get('MAX_RECORDS', '5000'))
           PAGE_SIZE = int(os.environ.get('PAGE_SIZE', '1000'))
           LOOKBACK_HOURS = int(os.environ.get('LOOKBACK_HOURS', '24'))
           
           def parse_datetime(value: str) -> datetime:
             """Parse ISO datetime string to datetime object."""
             if [value](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.ObjectCustomContextPayload.html#google_cloud_storage_blob_ObjectCustomContextPayload_value).endswith("Z"):
               value = value[:-1] + "+00:00"
             return datetime.fromisoformat(value)
           
           def get_access_token():
             """
             Obtain OAuth2 access token using client credentials grant.
             """
             api_base = WG_API_BASE.rstrip('/')
             token_url = f"{api_base}/oauth/token"
           
             headers = {
               'Content-Type': 'application/x-www-form-urlencoded',
               'Accept': 'application/json'
             }
           
             body = (
               f"grant_type=client_credentials"
               f"&client_id={WG_API_KEY}"
               f"&client_secret={WG_API_SECRET}"
               f"&scope=api-access"
             )
           
             backoff = 1.0
             for attempt in range(3):
               response = http.request('POST', token_url, body=body, headers=headers)
           
               if response.status == 429:
                 retry_after = int(response.headers.get('Retry-After', str(int(backoff))))
                 print(f"Rate limited (429) on token request. Retrying after {retry_after}s...")
                 time.sleep(retry_after)
                 backoff = min(backoff * 2, 30.0)
                 continue
           
               if response.status != 200:
                 raise RuntimeError(f"Failed to get access token: {response.status} - {response.data.decode('utf-8')}")
           
               data = json.loads(response.data.decode('utf-8'))
               return data['access_token']
           
             raise RuntimeError("Failed to get access token after 3 retries")
           
           @functions_framework.cloud_event
           def main(cloud_event):
             """
             Cloud Run function triggered by Pub/Sub to fetch WatchGuard EDR
             security event logs and write to GCS.
           
             Args:
               cloud_event: CloudEvent object containing Pub/Sub message
             """
           
             if not all([GCS_BUCKET, WG_API_KEY, WG_API_SECRET, WG_ACCOUNT_ID]):
               print('Error: Missing required environment variables')
               return
           
             try:
               bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(GCS_BUCKET)
           
               # Load state
               state = load_state(bucket, STATE_KEY)
           
               # Determine time window
               now = datetime.now(timezone.utc)
               last_time = None
           
               if isinstance(state, dict) and [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get("last_event_time"):
                 try:
                   last_time = parse_datetime(state["last_event_time"])
                   # Overlap by 2 minutes to catch any delayed events
                   last_time = last_time - timedelta(minutes=2)
                 except Exception as e:
                   print(f"Warning: Could not parse last_event_time: {e}")
           
               if last_time is None:
                 last_time = now - timedelta(hours=LOOKBACK_HOURS)
           
               print(f"Fetching logs from {last_time.isoformat()} to {now.isoformat()}")
           
               # Get access token
               token = get_access_token()
           
               # Fetch logs from multiple endpoints
               all_records = []
               newest_event_time = None
           
               for endpoint_type in ['indicators', 'threats']:
                 records, newest_time = fetch_logs(
                   token=token,
                   endpoint_type=endpoint_type,
                   start_time=last_time,
                   end_time=now,
                   page_size=PAGE_SIZE,
                   max_records=MAX_RECORDS,
                 )
                 all_records.extend(records)
                 if newest_time:
                   if newest_event_time is None or parse_datetime(newest_time) > parse_datetime(newest_event_time):
                     newest_event_time = newest_time
           
               if not all_records:
                 print("No new log records found.")
                 save_state(bucket, STATE_KEY, now.isoformat())
                 return
           
               # Write to GCS as NDJSON
               timestamp = now.strftime('%Y%m%d_%H%M%S')
               object_key = f"{GCS_PREFIX}/logs_{timestamp}.ndjson"
               blob = bucket.blob(object_key)
           
               ndjson = '\n'.join([json.dumps(record, ensure_ascii=False) for record in all_records]) + '\n'
               blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(ndjson, content_type='application/x-ndjson')
           
               print(f"Wrote {len(all_records)} records to gs://{GCS_BUCKET}/{object_key}")
           
               # Update state with newest event time
               if newest_event_time:
                 save_state(bucket, STATE_KEY, newest_event_time)
               else:
                 save_state(bucket, STATE_KEY, now.isoformat())
           
               print(f"Successfully processed {len(all_records)} records")
           
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
           
           def save_state(bucket, key, last_event_time_iso: str):
             """Save the last event timestamp to GCS state file."""
             try:
               state = {'last_event_time': last_event_time_iso}
               blob = bucket.blob(key)
               blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
                 json.dumps(state, indent=2),
                 content_type='application/json'
               )
               print(f"Saved state: last_event_time={last_event_time_iso}")
             except Exception as e:
               print(f"Warning: Could not save state: {e}")
           
           def fetch_logs(token: str, endpoint_type: str, start_time: datetime, end_time: datetime, page_size: int, max_records: int):
             """
             Fetch security event logs from WatchGuard Cloud API
             with OData-style pagination and rate limiting.
           
             Args:
               token: OAuth2 access token
               endpoint_type: API endpoint type (indicators, threats)
               start_time: Start time for log query
               end_time: End time for log query
               page_size: Number of records per page
               max_records: Maximum total records to fetch
           
             Returns:
               Tuple of (records list, newest_event_time ISO string)
             """
             api_base = WG_API_BASE.rstrip('/')
             endpoint = f"{api_base}/rest/aether/v1/accounts/{WG_ACCOUNT_ID}/{endpoint_type}"
           
             headers = {
               'Authorization': f'Bearer {token}',
               'Accept': 'application/json',
               'User-Agent': 'GoogleSecOps-WatchGuardEDRCollector/1.0'
             }
           
             records = []
             newest_time = None
             page_num = 0
             skip = 0
             backoff = 1.0
           
             start_iso = start_time.strftime('%Y-%m-%dT%H:%M:%SZ')
             end_iso = end_time.strftime('%Y-%m-%dT%H:%M:%SZ')
           
             while True:
               page_num += 1
           
               if len(records) >= max_records:
                 print(f"Reached max_records limit ({max_records}) for {endpoint_type}")
                 break
           
               url = f"{endpoint}?$top={min(page_size, max_records - len(records))}&$skip={skip}&$filter=date ge {start_iso} and date le {end_iso}&$orderby=date asc"
           
               try:
                 response = http.request('GET', url, headers=headers)
           
                 # Handle rate limiting with exponential backoff
                 if response.status == 429:
                   retry_after = int(response.headers.get('Retry-After', str(int(backoff))))
                   print(f"Rate limited (429). Retrying after {retry_after}s...")
                   time.sleep(retry_after)
                   backoff = min(backoff * 2, 30.0)
                   continue
           
                 backoff = 1.0
           
                 if response.status != 200:
                   print(f"HTTP Error: {response.status}")
                   response_text = response.data.decode('utf-8')
                   print(f"Response body: {response_text}")
                   return records, newest_time
           
                 data = json.loads(response.data.decode('utf-8'))
           
                 page_results = data.get('value', data.get('data', []))
           
                 if not page_results:
                   print(f"No more results (empty page) for {endpoint_type}")
                   break
           
                 print(f"{endpoint_type} page {page_num}: Retrieved {len(page_results)} events")
           
                 # Add endpoint type for identification
                 for event in page_results:
                   event['_wg_log_type'] = endpoint_type
           
                 records.extend(page_results)
           
                 # Track newest event time
                 for event in page_results:
                   try:
                     event_ts = event.get('date') or event.get('timestamp') or event.get('createdAt')
                     if event_ts:
                       event_time = str(event_ts)
                       if newest_time is None or parse_datetime(event_time) > parse_datetime(newest_time):
                         newest_time = event_time
                   except Exception as e:
                     print(f"Warning: Could not parse event time: {e}")
           
                 # Check for more results
                 if len(page_results) < page_size:
                   print(f"No more pages for {endpoint_type} (last page not full)")
                   break
           
                 skip += len(page_results)
           
               except Exception as e:
                 print(f"Error fetching {endpoint_type} logs: {e}")
                 return records, newest_time
           
             print(f"Retrieved {len(records)} total {endpoint_type} records from {page_num} pages")
             return records, newest_time
           

     * **requirements.txt:**
           
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
**Name** | `watchguard-edr-logs-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the topic `watchguard-edr-logs-trigger`  
**Message body** | `{}` (empty JSON object)  
  4. Click **Create**.




### Schedule frequency options

Choose frequency based on log volume and latency requirements:

Frequency | Cron Expression | Use Case  
---|---|---  
Every 5 minutes | `*/5 * * * *` | High-volume, low-latency  
Every 15 minutes | `*/15 * * * *` | Medium volume  
Every hour | `0 * * * *` | Standard (recommended)  
Every 6 hours | `0 */6 * * *` | Low volume, batch processing  
Daily | `0 0 * * *` | Historical data collection  
  
### Test the integration

  1. In the **Cloud Scheduler** console, find your job.
  2. Click **Force run** to trigger the job manually.
  3. Wait a few seconds.
  4. Go to **Cloud Run > Services**.
  5. Click on `watchguard-edr-logs-collector`.
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         Fetching logs from YYYY-MM-DDTHH:MM:SS+00:00 to YYYY-MM-DDTHH:MM:SS+00:00
         indicators page 1: Retrieved X events
         threats page 1: Retrieved X events
         Wrote X records to gs://watchguard-edr-logs/watchguard/logs_YYYYMMDD_HHMMSS.ndjson
         Successfully processed X records
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click on your bucket name (`watchguard-edr-logs`).

  10. Navigate to the `watchguard/` folder.

  11. Verify that a new `.ndjson` file was created with the current timestamp.




If you see errors in the logs:

  * **HTTP 401** : Check API credentials in environment variables
  * **HTTP 403** : Verify API key has required permissions in WatchGuard Cloud console
  * **HTTP 429** : Rate limiting - function will automatically retry with backoff
  * **Missing environment variables** : Check all required variables are set



## Configure a feed in Google SecOps to ingest WatchGuard EDR logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `WatchGuard EDR Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **WatchGuard EDR** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address.

**Note:** Each Google SecOps instance has a unique service account. Do not use service accounts from other documentation or examples.
  9. Click **Next**.

  10. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://watchguard-edr-logs/watchguard/
           

       * Replace: 
         * `watchguard-edr-logs`: Your GCS bucket name.
         * `watchguard`: Optional prefix/folder path where logs are stored (leave empty for root).
**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never** : Never deletes any files after transfers (recommended for testing).
       * **Delete transferred files** : Deletes files after successful transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.

**Note:** If you select a deletion option, the service account must have **Storage Object Admin** role instead of **Storage Object Viewer**. Update IAM permissions accordingly.
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days)

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)

     * **Ingestion labels** : The label to be applied to the events from this feed

  11. Click **Next**.

  12. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## Grant IAM permissions to the Google SecOps service account

The Google SecOps service account needs **Storage Object Viewer** role on your GCS bucket.

  1. Go to **Cloud Storage > Buckets**.
  2. Click on your bucket name.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Paste the Google SecOps service account email
     * **Assign roles** : Select **Storage Object Viewer**
  6. Click **Save**.

**Note:** If you plan to use the deletion option "Delete transferred files" or "Delete transferred files and empty directories," grant **Storage Object Admin** role instead of **Storage Object Viewer**.

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
| about.asset.asset_id | Set to device_vendor.device_product:deviceExternalId  
| about.file.full_path | Value from filePath if not empty, else from _hash if file_is_not_hash, else from fileHash if file_is_not_hash  
| about.file.size | Value from fsize if > 0  
| about.hostname | Value from dvchost  
| about.ip | Merged from dvc array after IP validation  
| about.mac | Value from dvcmac if valid MAC, else from dvc_mac if slot not present  
| about.nat_ip | Value from deviceTranslatedAddress  
| about.process.command_line | Value from Subject if not present, else Emne, else Path  
| about.process.pid | Value from dvcpid  
| about.resource.attribute.permissions | Value from filePermission  
| about.resource.attribute.labels | Value from resource_Type_label  
| additional.fields | Merged from various additional_* labels like additional_eventId, additional_devicePayloadId, etc.  
| metadata.collected_timestamp | Value from alertDateTime if ISO format, else from AlertDate if ISO format, else from Received if ISO format, else from Generated if ISO format  
| metadata.description | Value from msg  
| metadata.event_timestamp | Value from Date if ISO format  
| metadata.event_type | Set to "PROCESS_UNCATEGORIZED" if file_full_path not empty, else "SCAN_UNCATEGORIZED" if event_name in LogSpyware or LogPredictiveMachineLearning, else "STATUS_UPDATE" if has_principal true, else "GENERIC_EVENT"  
| metadata.product_event_type | Value from huntingRule if not empty, else from ThreatType, else from device_event_class_id - event_name, else from device_event_class_id, else from event_name  
| metadata.product_log_id | Value from pandaAlertId if not empty, else from externalId  
| metadata.product_name | Set to "ALERTS" for JSON, else from device_product  
| metadata.product_version | Value from device_version  
| metadata.url_back_to_product | Value from directLink  
| metadata.vendor_name | Set to "WATCHGUARD" for JSON, else from device_vendor  
| network.application_protocol | Value from app_protocol_output if not empty  
| network.direction | Set to "INBOUND" if deviceDirection == 0, else "OUTBOUND" if == 1  
| network.http.method | Value from requestMethod  
| network.http.user_agent | Value from requestClientApplication  
| network.ip_protocol | Value from ip_protocol_out if not empty  
| network.received_bytes | Value from in if > 0 and integer  
| network.sent_bytes | Value from out if > 0 and integer  
| principal.administrative_domain | Value from sntdom if not empty, else from Domain, else from Domene  
| principal.application | Value from sourceServiceName  
| principal.asset.asset_id | Value from MUID if not empty  
| principal.asset.hostname | Value from machineName if not empty, else from HostName, else from SourceMachineName, else from MachineName  
| principal.asset.ip | Merged from HostIp if not empty, else SourceIP, else MachineIP  
| principal.asset.product_object_id | Value from ClientId  
| principal.group.group_display_name | Value from Group_name if not empty, else Gruppenavn  
| principal.hostname | Value from machineName if not empty, else from temp_dhost if not empty, else from shost if IP validation fails, else from Device_name, else Enhetsnavn  
| principal.ip | Value from principal_ip if valid IP, else from src if valid IP  
| principal.mac | Value from smac if valid MAC  
| principal.nat_ip | Value from sourceTranslatedAddress if valid IP  
| principal.nat_port | Value from sourceTranslatedPort if > 0  
| principal.port | Value from spt if integer and not 0  
| principal.process.command_line | Value from sproc  
| principal.process.pid | Value from spid  
| principal.user.attribute.roles | Value from spriv  
| principal.user.user_display_name | Value from suser if not starts with {, else from SourceUserName, else from CustomerName if not empty  
| principal.user.userid | Value from contents.0.LoggedUser if not empty and sets event_type to USER_UNCATEGORIZED, else from temp_duid, else from User, else Bruker  
| security_result.action | Set to "ALLOW" if act in accept/notified or outcome REDIRECTED_USER_MAY_PROCEED or categoryOutcome Success or cs2 Allow, else "BLOCK" if act deny/blocked or outcome BLOCKED or categoryOutcome Failure or cs2 Denied, else "FAIL" if outcome Failure  
| security_result.action_details | Value from act, else from Action_Taken  
| security_result.attack_details.tactics | Merged from tactics_data if not empty  
| security_result.attack_details.techniques | Merged from technique_data if not empty  
| security_result.category_details | Value from cat  
| security_result.description | Value from msg_data_2 if not empty, else from THRuleName, else from Type, else Scan_Type  
| security_result.detection_fields | Merged from operation_label, operasjon_label, permission_label, tillatelse_label, infection_channel_label, spyware_Grayware_Type_label, threat_probability_label  
| security_result.rule_name | Value from mwProfile  
| security_result.severity | Set to "INFORMATIONAL" if severity == 1, "LOW" if 2, "MEDIUM" if 3, "HIGH" if 4, "CRITICAL" if 5; else LOW if severity in 0/1/2, MEDIUM if 3/4/5/INFO, HIGH if 6/7/SEVERE, CRITICAL if 8/9/10/VERY-HIGH  
| security_result.summary | Value from appcategory, else Result  
| security_result.threat_name | Value from Spyware if not empty, else Virus_Malware_Name, else Unknown_Threat  
| src.file.full_path | Value from oldFilePath  
| src.file.size | Value from oldFileSize if > 0  
| target.administrative_domain | Value from dntdom  
| target.application | Value from destinationServiceName  
| target.file.full_path | Value from ItemPath  
| target.file.md5 | Value from ItemHash if lowercase succeeds  
| target.hostname | Value from temp_dhost if not empty  
| target.ip | Value from dst_ip if valid IP  
| target.mac | Value from dmac if valid MAC  
| target.nat_ip | Value from destination_translated_address if valid IP  
| target.nat_port | Value from destinationTranslatedPort if integer  
| target.port | Value from dpt if integer and in range  
| target.process.command_line | Value from dproc  
| target.process.file.full_path | Value from contents.0.ChildPath if not empty, else from file_full_path  
| target.process.file.md5 | Value from contents.0.ChildMd5 if lowercase succeeds  
| target.process.file.names | Merged from file_name if not empty  
| target.process.parent_process.file.full_path | Value from contents.0.ParentPath  
| target.process.parent_process.file.md5 | Value from contents.0.ParentMd5 if lowercase succeeds  
| target.process.parent_process.file.names | Merged from parent_file_name if not empty  
| target.process.parent_process.pid | Value from contents.0.ParentPID  
| target.process.pid | Value from dpid  
| target.resource.attribute.labels | Value from DriveType_label, ServiceLevel_label  
| target.url | Value from request  
| target.user.user_display_name | Value from temp_duser  
| target.user.userid | Value from temp_duid if not empty  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/watchguard-edr-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
