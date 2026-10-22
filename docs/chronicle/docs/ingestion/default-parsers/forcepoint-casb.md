---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/forcepoint-casb/
title: Collect Forcepoint ONE CASB logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:11:35.150668+00:00
---

# Collect Forcepoint ONE CASB logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/forcepoint-casb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Forcepoint ONE CASB logs

**Parser Version:** 2.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Forcepoint ONE CASB (formerly Forcepoint/Bitglass CASB) logs to Google Security Operations using Google Cloud Storage V2.

Forcepoint ONE CASB is a cloud access security broker that provides visibility, compliance, and threat protection for cloud applications. It monitors and controls access to SaaS applications, enforces data loss prevention policies, and detects anomalous user behavior across sanctioned and unsanctioned cloud services.

For more information, see [Forcepoint CASB documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/forcepoint-casb).

## Before you begin

Ensure that you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * Privileged access to the Forcepoint ONE portal (administrator role)
  * Forcepoint ONE API credentials (API access token or OAuth client credentials)



## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `forcepoint-casb-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Collect Forcepoint ONE CASB API credentials

### Get API access token

  1. Sign in to the **Forcepoint ONE** portal at `https://portal.bitglass.com` (or your regional portal URL) with an administrator account.
  2. Go to **Settings > API Integration**.
  3. Click **Generate API Token** (or **Create New Token** if generating for the first time).
  4. Provide the following configuration details: 
     * **Token Name** : Enter a descriptive name (for example, `SecOps-GCS-Integration`).
     * **Permissions** : Select **Read** access for the following scopes: 
       * **Access Logs** : User activity and access events.
       * **Admin Audit Logs** : Administrative changes and configuration events.
       * **DLP Incidents** : Data loss prevention events.
       * **Threat Protection Logs** : Malware and threat detection events.
  5. Click **Generate**.
  6. Copy and save the following values securely:

     * **API Access Token** : The generated token value.
     * **API Base URL** : Your Forcepoint ONE API endpoint (for example, `https://portal.bitglass.com/api`).
**Note:** The API token is displayed only once. If lost, you must generate a new token.



### Verify permissions

To verify the account has the required permissions:

  1. Sign in to the **Forcepoint ONE** portal.
  2. Go to **Settings > Administrators**.
  3. Verify that your account has the **Administrator** or **Security Administrator** role.
  4. If you cannot see the **API Integration** option, contact your Forcepoint ONE administrator to grant the required role.



### Test API access

  * Test your credentials before proceeding with the integration:
        
        API_TOKEN="<your-api-token>"
        API_BASE="https://portal.bitglass.com"
        
        # Test API access - retrieve recent access logs
        curl -v -H "Authorization: Bearer ${API_TOKEN}" \
            -H "Accept: application/json" \
            "${API_BASE}/api/v1/logs/access?limit=1"
        




A successful response returns HTTP 200 with a JSON object containing log entries. If you receive HTTP 401, verify the API token. If you receive HTTP 403, verify account permissions.

## Create service account for Cloud Run function

The Cloud Run function needs a service account with permissions to write to the GCS bucket and be invoked by Pub/Sub.

### Create service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `forcepoint-casb-collector-sa`
     * **Service account description** : Enter `Service account for Cloud Run function to collect Forcepoint ONE CASB logs`
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

  * **Storage Object Admin** : Write logs to the GCS bucket and manage state files.
  * **Cloud Run Invoker** : Allow Pub/Sub to invoke the function.
  * **Cloud Functions Invoker** : Allow function invocation.



### Grant IAM permissions on GCS bucket

Grant the service account write permissions on the GCS bucket:

  1. Go to **Cloud Storage > Buckets**.
  2. Click on your bucket name (for example, `forcepoint-casb-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `forcepoint-casb-collector-sa@PROJECT_ID.iam.gserviceaccount.com`)
     * **Assign roles** : Select **Storage Object Admin**
  6. Click **Save**.



## Create Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `forcepoint-casb-trigger`
     * Leave other settings as default
  4. Click **Create**.



## Create Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from the Forcepoint ONE CASB API and write them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `forcepoint-casb-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose `forcepoint-casb-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select `forcepoint-casb-collector-sa`
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `forcepoint-casb-logs` | GCS bucket name  
`GCS_PREFIX` | `forcepoint-casb` | Prefix for log files  
`STATE_KEY` | `forcepoint-casb/state.json` | State file path  
`API_BASE` | `https://portal.bitglass.com` | Forcepoint ONE API base URL  
`API_TOKEN` | `your-api-token` | Forcepoint ONE API token  
`MAX_RECORDS` | `5000` | Max records per run  
`PAGE_SIZE` | `500` | Records per page  
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
           GCS_PREFIX = os.environ.get('GCS_PREFIX', 'forcepoint-casb')
           STATE_KEY = os.environ.get('STATE_KEY', 'forcepoint-casb/state.json')
           API_BASE = os.environ.get('API_BASE')
           API_TOKEN = os.environ.get('API_TOKEN')
           MAX_RECORDS = int(os.environ.get('MAX_RECORDS', '5000'))
           PAGE_SIZE = int(os.environ.get('PAGE_SIZE', '500'))
           LOOKBACK_HOURS = int(os.environ.get('LOOKBACK_HOURS', '24'))
           
           def parse_datetime(value: str) -> datetime:
               """Parse ISO datetime string to datetime object."""
               if [value](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.ObjectCustomContextPayload.html#google_cloud_storage_blob_ObjectCustomContextPayload_value).endswith("Z"):
                   value = value[:-1] + "+00:00"
               return datetime.fromisoformat(value)
           
           @functions_framework.cloud_event
           def main(cloud_event):
               """
               Cloud Run function triggered by Pub/Sub to fetch Forcepoint ONE CASB logs
               and write to GCS.
           
               Args:
                   cloud_event: CloudEvent object containing Pub/Sub message
               """
           
               if not all([GCS_BUCKET, API_BASE, API_TOKEN]):
                   print('Error: Missing required environment variables')
                   return
           
               try:
                   # Get GCS bucket
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
           
                   # Fetch logs
                   records, newest_event_time = fetch_logs(
                       api_base=API_BASE,
                       api_token=API_TOKEN,
                       start_time=last_time,
                       end_time=now,
                       page_size=PAGE_SIZE,
                       max_records=MAX_RECORDS,
                   )
           
                   if not records:
                       print("No new log records found.")
                       save_state(bucket, STATE_KEY, now.isoformat())
                       return
           
                   # Write to GCS as NDJSON
                   timestamp = now.strftime('%Y%m%d_%H%M%S')
                   object_key = f"{GCS_PREFIX}/logs_{timestamp}.ndjson"
                   blob = bucket.blob(object_key)
           
                   ndjson = '\n'.join([json.dumps(record, ensure_ascii=False) for record in records]) + '\n'
                   blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(ndjson, content_type='application/x-ndjson')
           
                   print(f"Wrote {len(records)} records to gs://{GCS_BUCKET}/{object_key}")
           
                   # Update state with newest event time
                   if newest_event_time:
                       save_state(bucket, STATE_KEY, newest_event_time)
                   else:
                       save_state(bucket, STATE_KEY, now.isoformat())
           
                   print(f"Successfully processed {len(records)} records")
           
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
           
           def fetch_logs(api_base: str, api_token: str, start_time: datetime, end_time: datetime, page_size: int, max_records: int):
               """
               Fetch logs from Forcepoint ONE CASB API with pagination and rate limiting.
           
               Args:
                   api_base: Forcepoint ONE API base URL
                   api_token: API access token
                   start_time: Start time for log query
                   end_time: End time for log query
                   page_size: Number of records per page
                   max_records: Maximum total records to fetch
           
               Returns:
                   Tuple of (records list, newest_event_time ISO string)
               """
               base_url = api_base.rstrip('/')
               endpoint = f"{base_url}/api/v1/logs/access"
           
               headers = {
                   'Authorization': f'Bearer {api_token}',
                   'Accept': 'application/json',
                   'Content-Type': 'application/json',
                   'User-Agent': 'GoogleSecOps-ForcepointCASBCollector/1.0'
               }
           
               records = []
               newest_time = None
               page_num = 0
               backoff = 1.0
               start_index = 0
           
               start_iso = start_time.strftime('%Y-%m-%dT%H:%M:%SZ')
               end_iso = end_time.strftime('%Y-%m-%dT%H:%M:%SZ')
           
               while True:
                   page_num += 1
           
                   if len(records) >= max_records:
                       print(f"Reached max_records limit ({max_records})")
                       break
           
                   current_limit = min(page_size, max_records - len(records))
                   url = f"{endpoint}?startDate={start_iso}&endDate={end_iso}&offset={start_index}&limit={current_limit}"
           
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
                           return [], None
           
                       data = json.loads(response.data.decode('utf-8'))
           
                       page_results = data.get('data', [])
           
                       if not page_results:
                           print(f"No more results (empty page)")
                           break
           
                       print(f"Page {page_num}: Retrieved {len(page_results)} events")
                       records.extend(page_results)
           
                       # Track newest event time
                       for event in page_results:
                           try:
                               event_time = event.get('timestamp') or event.get('created_at')
                               if event_time:
                                   if newest_time is None or parse_datetime(event_time) > parse_datetime(newest_time):
                                       newest_time = event_time
                           except Exception as e:
                               print(f"Warning: Could not parse event time: {e}")
           
                       # Check for more results
                       if len(page_results) < current_limit:
                           print(f"Reached last page (size={len(page_results)} < limit={current_limit})")
                           break
           
                       start_index += len(page_results)
           
                   except Exception as e:
                       print(f"Error fetching logs: {e}")
                       return [], None
           
               print(f"Retrieved {len(records)} total records from {page_num} pages")
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
**Name** | `forcepoint-casb-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select `forcepoint-casb-trigger`  
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

  1. In the **Cloud Scheduler** console, find your job (`forcepoint-casb-collector-hourly`).
  2. Click **Force run** to trigger the job manually.
  3. Wait a few seconds.
  4. Go to **Cloud Run > Services**.
  5. Click on **forcepoint-casb-collector**.
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         Fetching logs from YYYY-MM-DDTHH:MM:SS+00:00 to YYYY-MM-DDTHH:MM:SS+00:00
         Page 1: Retrieved X events
         Wrote X records to gs://forcepoint-casb-logs/forcepoint-casb/logs_YYYYMMDD_HHMMSS.ndjson
         Successfully processed X records
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click on your bucket name (`forcepoint-casb-logs`).

  10. Navigate to the `forcepoint-casb/` folder.

  11. Verify that a new `.ndjson` file was created with the current timestamp.




If you see errors in the logs:

  * **HTTP 401** : Check the API token in environment variables.
  * **HTTP 403** : Verify the account has required permissions in the Forcepoint ONE portal.
  * **HTTP 429** : Rate limiting - the function will automatically retry with backoff.
  * **Missing environment variables** : Check all required variables are set.



## Retrieve the Google SecOps service account

Google SecOps uses a unique service account to read data from your GCS bucket. You must grant this service account access to your bucket.

### Get the service account email

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Forcepoint CASB Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Forcepoint CASB** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Do not use service accounts from other documentation or examples.
  9. Click **Next**.

  10. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://forcepoint-casb-logs/forcepoint-casb/
           

**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never** : Never deletes any files after transfers (recommended for testing).
       * **Delete transferred files** : Deletes files after successful transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.
**Note:** If you select a deletion option, the service account must have **Storage Object Admin** role instead of **Storage Object Viewer**. Update IAM permissions accordingly.
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days).

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).

     * **Ingestion labels** : The label to be applied to the events from this feed.

  11. Click **Next**.

  12. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## Grant IAM permissions to the Google SecOps service account

The Google SecOps service account needs **Storage Object Viewer** role on your GCS bucket.

  1. Go to **Cloud Storage > Buckets**.
  2. Click on your bucket name (`forcepoint-casb-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Paste the Google SecOps service account email.
     * **Assign roles** : Select **Storage Object Viewer**.
  6. Click **Save**.

**Note:** If you plan to use the deletion option "Delete transferred files" or "Delete transferred files and empty directories," grant **Storage Object Admin** role instead of **Storage Object Viewer**.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`extensions` | `extensions` | Renamed/mapped  
`request` | `extensions.auth.auth_details` | Directly mapped  
`intermediary` | `intermediary` | Merged  
`smb_host` | `intermediary.hostname` | Directly mapped  
`smb_uid` | `intermediary.user.userid` | Directly mapped  
`metadata` | `metadata` | Renamed/mapped  
`msg` | `metadata.description` | Directly mapped  
`event_name` | `metadata.product_event_type` | Directly mapped  
`event_type` | `metadata.product_event_type` | Directly mapped  
`value` | `metadata.product_name` | Directly mapped  
`product` | `metadata.vendor_name` | Directly mapped  
`network` | `network` | Renamed/mapped  
`requestClientApplication` | `network.http.user_agent` | Directly mapped  
`principal` | `principal` | Renamed/mapped  
`ahost` | `principal.hostname` | Directly mapped  
`agt` | `principal.ip` | Merged  
`atz` | `principal.location.country_or_region` | Directly mapped  
`amac` | `principal.mac` | Merged  
`sourceServiceName` | `principal.platform_version` | Directly mapped  
`av_label` | `principal.resource.attribute.labels` | Merged  
`aid` | `principal.resource.id` | Directly mapped  
`at` | `principal.resource.name` | Directly mapped  
`agentZoneURI` | `principal.url` | Directly mapped  
`cs1` | `principal.user.email_addresses` | Merged  
`suid` | `principal.user.userid` | Directly mapped  
`security_result` | `security_result` | Merged  
`action` | `security_result.action` | Merged  
`msg` | `security_result.summary` | Directly mapped  
`src_label` | `src` | Renamed/mapped  
`target` | `target` | Renamed/mapped  
`dvchost` | `target.hostname` | Directly mapped  
`dvc` | `target.ip` | Merged  
`deviceProcessName` | `target.resource.name` | Directly mapped  
`deviceZoneURI` | `target.url` | Directly mapped  
N/A | `extensions.auth.type` | Constant: `SSO`  
N/A | `intermediary` | Constant: `intermediary`  
N/A | `metadata.event_type` | Constant: `USER_RESOURCE_ACCESS`  
N/A | `principal.ip` | Constant: `agt`  
N/A | `principal.mac` | Constant: `amac`  
N/A | `principal.platform` | Constant: `WINDOWS`  
N/A | `principal.resource.attribute.labels` | Constant: `av_label`  
N/A | `principal.user.email_addresses` | Constant: `cs1`  
N/A | `security_result` | Constant: `security_result`  
N/A | `security_result.action` | Constant: `action`  
N/A | `target.ip` | Constant: `dvc`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/forcepoint-casb-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
