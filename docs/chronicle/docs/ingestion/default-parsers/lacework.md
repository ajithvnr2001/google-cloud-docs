---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/lacework/
title: Collect FortiCNAPP (formerly Lacework) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:39:13.825572+00:00
---

# Collect FortiCNAPP (formerly Lacework) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/lacework/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect FortiCNAPP (formerly Lacework) logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest FortiCNAPP (formerly known as Lacework) logs to Google Security Operations using Google Cloud Storage V2.

FortiCNAPP is a cloud-native application protection platform (CNAPP) that provides cloud security posture management, workload protection, and threat detection across multi-cloud environments. It generates alerts, compliance findings, and audit logs that can be collected via the Lacework REST API.

## Before you begin

Make sure that you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * Privileged access to the FortiCNAPP (formerly Lacework) console with admin permissions
  * A Lacework account with API key access enabled



## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.

  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `lacework-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Collect FortiCNAPP (formerly Lacework) API credentials

### Generate API key

  1. Sign in to your [Lacework console](https://lacework.net/).
  2. Go to **Settings > Configuration > API Keys**.
  3. Click **\+ Add New**.
  4. Enter a name for the API key (for example, `Google SecOps Integration`).
  5. Optionally enter a description.
  6. Click **Save**.

  7. Copy and save the following details in a secure location:

     * **Key ID** : The generated API key ID
     * **Secret** : The generated API secret (shown only once)
**Note:** The API secret is displayed only once at the time of creation. If you lose it, you must generate a new API key.
  8. Note your Lacework account URL from the browser address bar.

     * Format: `https://<ACCOUNT>.lacework.net`
     * Example: If your Lacework console URL is `https://acme.lacework.net`, your account name is `acme`



### Verify permissions

To verify the account has the required permissions:

  1. Sign in to the Lacework console.
  2. Go to **Settings > Configuration > API Keys**.
  3. If you can see the API Keys page and create keys, you have the required permissions.
  4. If you cannot see this option, contact your administrator to grant admin-level access.



### Test API access

  * Test your credentials before proceeding with the integration:
        
        # Replace with your actual credentials
        LW_ACCOUNT="your-account-name"
        LW_KEY_ID="your-api-key-id"
        LW_SECRET="your-api-secret"
        
        # Get a temporary access token
        TOKEN=$(curl -s -X POST "https://${LW_ACCOUNT}.lacework.net/api/v2/access/tokens" \
            -H "X-LW-UAKS: ${LW_SECRET}" \
            -H "Content-Type: application/json" \
            -d "{\"keyId\": \"${LW_KEY_ID}\", \"expiryTime\": 3600}" | python3 -c "import sys,json; print(json.load(sys.stdin).get('token',''))")
        
        # Test API access - list alerts
        curl -v -H "Authorization: Bearer ${TOKEN}" \
            "https://${LW_ACCOUNT}.lacework.net/api/v2/Alerts?startTime=$(date -u -v-1d +%Y-%m-%dT%H:%M:%SZ)&endTime=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
        




## Create service account for Cloud Run function

The Cloud Run function needs a service account with permissions to write to GCS bucket and be invoked by Pub/Sub.

### Create service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.

  3. Provide the following configuration details:

     * **Service account name** : Enter `lacework-logs-collector-sa`
     * **Service account description** : Enter `Service account for Cloud Run function to collect FortiCNAPP (formerly Lacework) logs`
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
  2. Click on your bucket name (for example, `lacework-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.

  5. Provide the following configuration details:

     * **Add principals** : Enter the service account email (for example, `lacework-logs-collector-sa@PROJECT_ID.iam.gserviceaccount.com`)
     * **Assign roles** : Select **Storage Object Admin**
  6. Click **Save**.




## Create Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.

  3. Provide the following configuration details:

     * **Topic ID** : Enter `lacework-logs-trigger`
     * Leave other settings as default
  4. Click **Create**.




## Create Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from the FortiCNAPP (formerly Lacework) API and write them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).

  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `lacework-logs-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose the topic `lacework-logs-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select the service account `lacework-logs-collector-sa`.
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `lacework-logs` | GCS bucket name  
`GCS_PREFIX` | `lacework` | Prefix for log files  
`STATE_KEY` | `lacework/state.json` | State file path  
`LW_ACCOUNT` | `acme` | Lacework account name  
`LW_KEY_ID` | `your-api-key-id` | Lacework API key ID  
`LW_SECRET` | `your-api-secret` | Lacework API secret  
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
           GCS_PREFIX = os.environ.get('GCS_PREFIX', 'lacework')
           STATE_KEY = os.environ.get('STATE_KEY', 'lacework/state.json')
           LW_ACCOUNT = os.environ.get('LW_ACCOUNT')
           LW_KEY_ID = os.environ.get('LW_KEY_ID')
           LW_SECRET = os.environ.get('LW_SECRET')
           MAX_RECORDS = int(os.environ.get('MAX_RECORDS', '5000'))
           PAGE_SIZE = int(os.environ.get('PAGE_SIZE', '500'))
           LOOKBACK_HOURS = int(os.environ.get('LOOKBACK_HOURS', '24'))
           
           # Lacework API base URL
           API_BASE_TEMPLATE = 'https://{account}.lacework.net/api/v2'
           
           # Log endpoints to fetch
           ENDPOINTS = [
               {'name': 'alerts', 'path': '/Alerts', 'time_field': 'startTime', 'results_key': 'data'},
               {'name': 'audit_logs', 'path': '/AuditLogs', 'time_field': 'createdTime', 'results_key': 'data'},
           ]
           
           def get_access_token(api_base: str, key_id: str, secret: str) -> str:
               """Get a temporary access token from Lacework API."""
               token_url = f"{api_base}/access/tokens"
               body = json.dumps({
                   'keyId': key_id,
                   'expiryTime': 3600
               }).encode('utf-8')
               headers = {
                   'X-LW-UAKS': secret,
                   'Content-Type': 'application/json',
               }
               response = http.request('POST', token_url, body=body, headers=headers)
               if response.status != 201:
                   raise Exception(f"Failed to get access token: HTTP {response.status} - {response.data.decode('utf-8')}")
               token_data = json.loads(response.data.decode('utf-8'))
               return token_data['token']
           
           @functions_framework.cloud_event
           def main(cloud_event):
               """
               Cloud Run function triggered by Pub/Sub to fetch FortiCNAPP
               (formerly Lacework) logs and write to GCS.
           
               Args:
                   cloud_event: CloudEvent object containing Pub/Sub message
               """
           
               if not all([GCS_BUCKET, LW_ACCOUNT, LW_KEY_ID, LW_SECRET]):
                   print('Error: Missing required environment variables')
                   return
           
               try:
                   bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(GCS_BUCKET)
                   api_base = API_BASE_TEMPLATE.format(account=LW_ACCOUNT)
           
                   # Get access token
                   token = get_access_token(api_base, LW_KEY_ID, LW_SECRET)
                   print("Successfully obtained access token")
           
                   # Load state
                   state = load_state(bucket, STATE_KEY)
           
                   # Determine time window
                   now = datetime.now(timezone.utc)
                   all_records = []
           
                   for endpoint in ENDPOINTS:
                       ep_name = endpoint['name']
                       last_time_str = None
           
                       if isinstance(state, dict) and [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get(f"last_{ep_name}_time"):
                           try:
                               last_time = parse_datetime(state[f"last_{ep_name}_time"])
                               # Overlap by 2 minutes to catch any delayed events
                               last_time = last_time - timedelta(minutes=2)
                               last_time_str = last_time.strftime('%Y-%m-%dT%H:%M:%SZ')
                           except Exception as e:
                               print(f"Warning: Could not parse last_{ep_name}_time: {e}")
           
                       if last_time_str is None:
                           last_time = now - timedelta(hours=LOOKBACK_HOURS)
                           last_time_str = last_time.strftime('%Y-%m-%dT%H:%M:%SZ')
           
                       end_time_str = now.strftime('%Y-%m-%dT%H:%M:%SZ')
           
                       print(f"Fetching {ep_name} from {last_time_str} to {end_time_str}")
           
                       records, newest_event_time = fetch_logs(
                           api_base=api_base,
                           token=token,
                           endpoint=endpoint,
                           start_time=last_time_str,
                           end_time=end_time_str,
                           page_size=PAGE_SIZE,
                           max_records=MAX_RECORDS,
                       )
           
                       # Tag records with endpoint type
                       for record in records:
                           record['_lw_log_type'] = ep_name
           
                       all_records.extend(records)
           
                       # Update state for this endpoint
                       if newest_event_time:
                           state[f"last_{ep_name}_time"] = newest_event_time
                       else:
                           state[f"last_{ep_name}_time"] = end_time_str
           
                       print(f"Fetched {len(records)} {ep_name} records")
           
                   if not all_records:
                       print("No new log records found.")
                       save_state(bucket, STATE_KEY, state)
                       return
           
                   # Write to GCS as NDJSON
                   timestamp = now.strftime('%Y%m%d_%H%M%S')
                   object_key = f"{GCS_PREFIX}/logs_{timestamp}.ndjson"
                   blob = bucket.blob(object_key)
           
                   ndjson = '\n'.join([json.dumps(record, ensure_ascii=False) for record in all_records]) + '\n'
                   blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(ndjson, content_type='application/x-ndjson')
           
                   print(f"Wrote {len(all_records)} records to gs://{GCS_BUCKET}/{object_key}")
           
                   # Save state
                   save_state(bucket, STATE_KEY, state)
           
                   print(f"Successfully processed {len(all_records)} records")
           
               except Exception as e:
                   print(f'Error processing logs: {str(e)}')
                   raise
           
           def parse_datetime(value: str) -> datetime:
               """Parse ISO datetime string to datetime object."""
               if [value](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.ObjectCustomContextPayload.html#google_cloud_storage_blob_ObjectCustomContextPayload_value).endswith("Z"):
                   value = value[:-1] + "+00:00"
               return datetime.fromisoformat(value)
           
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
           
           def save_state(bucket, key, state: dict):
               """Save the state to GCS state file."""
               try:
                   blob = bucket.blob(key)
                   blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
                       json.dumps(state, indent=2),
                       content_type='application/json'
                   )
                   print(f"Saved state: {json.dumps(state)}")
               except Exception as e:
                   print(f"Warning: Could not save state: {e}")
           
           def fetch_logs(api_base: str, token: str, endpoint: dict, start_time: str, end_time: str, page_size: int, max_records: int):
               """
               Fetch logs from Lacework API with pagination and rate limiting.
           
               Args:
                   api_base: API base URL
                   token: Bearer access token
                   endpoint: Endpoint configuration dict
                   start_time: Start time in ISO format
                   end_time: End time in ISO format
                   page_size: Number of records per page
                   max_records: Maximum total records to fetch
           
               Returns:
                   Tuple of (records list, newest_event_time ISO string)
               """
               headers = {
                   'Authorization': f'Bearer {token}',
                   'Accept': 'application/json',
                   'Content-Type': 'application/json',
                   'User-Agent': 'GoogleSecOps-LaceworkCollector/1.0'
               }
           
               ep_path = endpoint['path']
               time_field = endpoint['time_field']
               results_key = endpoint['results_key']
           
               records = []
               newest_time = None
               page_num = 0
               backoff = 1.0
               next_page = None
           
               while True:
                   page_num += 1
           
                   if len(records) >= max_records:
                       print(f"Reached max_records limit ({max_records}) for {endpoint['name']}")
                       break
           
                   # Build request URL
                   if next_page:
                       url = next_page
                   else:
                       url = f"{api_base}{ep_path}?startTime={start_time}&endTime={end_time}"
           
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
           
                       page_results = data.get(results_key, [])
           
                       if not page_results:
                           print(f"No more results (empty page) for {endpoint['name']}")
                           break
           
                       print(f"Page {page_num}: Retrieved {len(page_results)} {endpoint['name']} events")
                       records.extend(page_results)
           
                       # Track newest event time
                       for event in page_results:
                           try:
                               event_time = event.get(time_field)
                               if event_time:
                                   if newest_time is None or parse_datetime(event_time) > parse_datetime(newest_time):
                                       newest_time = event_time
                           except Exception as e:
                               print(f"Warning: Could not parse event time: {e}")
           
                       # Check for next page via paging object
                       paging = data.get('paging', {})
                       next_page_url = paging.get('urls', {}).get('nextPage')
                       if not next_page_url:
                           print(f"No more pages for {endpoint['name']}")
                           break
                       next_page = next_page_url
           
                   except Exception as e:
                       print(f"Error fetching {endpoint['name']} logs: {e}")
                       return [], None
           
               print(f"Retrieved {len(records)} total {endpoint['name']} records from {page_num} pages")
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
**Name** | `lacework-logs-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the topic `lacework-logs-trigger`  
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
  5. Click on `lacework-logs-collector`.
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         Successfully obtained access token
         Fetching alerts from YYYY-MM-DDTHH:MM:SSZ to YYYY-MM-DDTHH:MM:SSZ
         Page 1: Retrieved X alerts events
         Fetched X alerts records
         Fetching audit_logs from YYYY-MM-DDTHH:MM:SSZ to YYYY-MM-DDTHH:MM:SSZ
         Page 1: Retrieved X audit_logs events
         Fetched X audit_logs records
         Wrote X records to gs://lacework-logs/lacework/logs_YYYYMMDD_HHMMSS.ndjson
         Successfully processed X records
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click on your bucket name (`lacework-logs`).

  10. Navigate to the `lacework/` folder.

  11. Verify that a new `.ndjson` file was created with the current timestamp.




If you see errors in the logs:

  * **HTTP 401** : Check API credentials in environment variables or token may be expired
  * **HTTP 403** : Verify the API key has required permissions in the Lacework console
  * **HTTP 429** : Rate limiting - function will automatically retry with backoff
  * **Missing environment variables** : Check all required variables are set



## Configure a feed in Google SecOps to ingest FortiCNAPP (formerly Lacework) logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Lacework Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Lacework Cloud Security** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address.

**Note:** Each Google SecOps instance has a unique service account. Do not use service accounts from other documentation or examples.
  9. Click **Next**.

  10. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://lacework-logs/lacework/
           

       * Replace: 
         * `lacework-logs`: Your GCS bucket name.
         * `lacework`: Optional prefix/folder path where logs are stored (leave empty for root).
**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never** : Never deletes any files after transfers (recommended for testing).
       * **Delete transferred files** : Deletes files after successful transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.

**Note:** If you select a deletion option, the service account must have **Storage Object Admin** role instead of Storage Object Viewer. Update IAM permissions accordingly.
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


**Note:** If you plan to use the deletion option "Delete transferred files" or "Delete transferred files and empty directories," grant **Storage Object Admin** role instead of Storage Object Viewer.

### Supported Lacework Cloud Security Sample Logs

  * Agent or Machine Information (Host Inventory)
        
        {
          "AGENT_VERSION": "6.7.6-4ce73a7b",
          "CREATED_TIME": "Thu, 03 Nov 2022 02:09:36 -0700",
          "HOSTNAME": "host-agent-1",
          "IP_ADDR": "10.0.0.1",
          "LAST_UPDATE": "Wed, 18 Oct 2023 17:59:09 -0700",
          "MID": 6516601498285932156,
          "MODE": "ebpf",
          "OS": "Linux",
          "STATUS": "ACTIVE",
          "TAGS": {
            "Account": "999999999999",
            "AmiId": "ami-00000000000000000",
            "ExternalIp": "203.0.113.10",
            "Hostname": "internal-host-1.zone.compute.internal",
            "InstanceId": "i-00000000000000000",
            "InternalIp": "172.16.1.10",
            "LwTokenShort": "DUMMYTOKENABCD123456",
            "Name": "proxy-DMZ-app-1",
            "ResourceType": "proxy-machines",
            "SubnetId": "subnet-00000000000000000",
            "VmInstanceType": "t3.small",
            "VmProvider": "AWS",
            "VpcId": "vpc-00000000000000000",
            "Zone": "us-west-2a",
            "arch": "amd64",
            "falconx.io/application": "proxy-machines",
            "falconx.io/environment": "prod",
            "falconx.io/project": "edge",
            "falconx.io/team": "edge",
            "os": "linux"
          }
        }
        

  * File Metadata or Integrity
        
        {
        "CREATED_TIME": "Wed, 18 Oct 2023 17:02:01 -0700",
        "FILEDATA_HASH": "DUMMYHASH582C741AD91CA817B4718DEAA4E8A83C0B9D92E2",
        "FILE_PATH": "/usr/local/bin/secure_config",
        "MID": 7371220731851617371,
        "MTIME": "Fri, 25 Aug 2023 13:03:09 -0700",
        "SIZE": 8078
        }
        

  * Host Vulnerability Assessment
        
        {
        "CVE_PROPS": {
          "description": "DOCUMENTATION: The MITRE CVE dictionary describes this issue as: "
                         "This CVE ID has been rejected or withdrawn by its CVE Numbering "
                         "Authority for the following reason: This CVE ID has been rejected "
                         "or withdrawn by its CVE Numbering Authority.",
          "link": "https://vendor.example.com/security/cve/CVE-2021-47472",
          "metadata": null
        },
        "CVE_RISK_INFO": {
          "HOST_COUNT": 1249,
          "IMAGE_COUNT": 0,
          "PKG_COUNT": 0,
          "SEVERITY_LEVEL": 2,
          "score": 0.5154245281584533
        },
        "CVE_RISK_SCORE": 3.77,
        "END_TIME": "2024-09-04 07:00:00.000",
        "EVAL_CTX": {
          "collector_type": "Agent",
          "exception_props": [],
          "hostname": "vuln-host-1.example.net"
        },
        "EVAL_GUID": "3dc61df780e3b722aa59b0ffcac85683",
        "FEATURE_KEY": {
          "name": "kernel-headers",
          "namespace": "centos:7",
          "package_active": 1,
          "package_path": "",
          "version_installed": "0:3.10.0-1160.119.1.el7.tuxcare.els2"
        },
        "MACHINE_TAGS": {
          "Account": "999999999999",
          "AmiId": "ami-00000000000000000",
          "ExternalIp": "203.0.113.10",
          "Hostname": "ip-172-16-1-10.example-prod.aws.featurespace.net",
          "InternalIp": "10.0.0.1",
          "LwTokenShort": "DUMMYTOKENABCD123456",
          "VmProvider": "AWS",
          "VpcId": "vpc-00000000000000000",
          "os": "linux"
        },
        "MID": 5746003737030963813,
        "PACKAGE_STATUS": "ACTIVE",
        "REGION": "eu-west-2",
        "RISK_SCORE": 10,
        "SEVERITY": "Low",
        "START_TIME": "2024-09-04 06:00:00.000",
        "STATUS": "Exception",
        "VULN_ID": "CVE-2021-47472"
        }
        

  * Cloud Configuration Compliance (Audit)
        
        {
        "ACCOUNT": {
          "AccountId": "999999999999",
          "Account_Alias": ""
        },
        "EVAL_TYPE": "LW_SA",
        "ID": "lacework-global-87",
        "REASON": "Default security group does not restrict traffic",
        "RECOMMENDATION": "Ensure the default security group of every Virtual Private Cloud (VPC) restricts all traffic",
        "REGION": "eu-north-1",
        "REPORT_TIME": "2024-11-10 18:00:00.000",
        "RESOURCE_ID": "arn:aws:ec2:eu-west-1:999999999999:security-group/sg-00000000000000000",
        "SECTION": "",
        "SEVERITY": "High",
        "STATUS": "NonCompliant"
        }
        

  * DNS Query or Resolution
        
        {
        "CREATED_TIME": "2024-11-06 05:14:44.329",
        "DNS_SERVER_IP": "10.0.0.53",
        "FQDN": "data-service-prod-1234567890.s3.eu-west-2.amazonaws.com",
        "HOST_IP_ADDR": "172.16.1.20",
        "MID": 8843985456817096491,
        "TTL": 5
        }
        

  * Image Vulnerability Assessment
        
        {
        "CVE_PROPS": null,
        "EVAL_CTX": {
          "collector_type": "Agentless",
          "image_info": {
            "digest": "sha256:52d5cb782dad7a8a03c8bd1b285bbd32bdbfa8fcc435614bb1e6ceefcf26ae1d",
            "id": "sha256:31427c44cac7ab632d541181073bbd46a964e4ed38d087d8a47f60bb66eef4df",
            "registry": "999999999999.dkr.ecr.eu-west-1.amazonaws.com",
            "repo": "amazon/aws-network-policy-agent"
          }
        },
        "EVAL_GUID": "3a17a74f0a65eed2bddd2d37bb02e6af",
        "FEATURE_KEY": {
          "name": "perl-threads",
          "namespace": "amzn:2",
          "version": "1.87-4.amzn2.0.2"
        },
        "FIX_INFO": {
          "fix_available": 0,
          "fixed_version": ""
        },
        "IMAGE_ID": "sha256:31427c44cac7ab632d541181073bbd46a964e4ed38d087d8a47f60bb66eef4df",
        "IMAGE_RISK_INFO": {
          "factors": [
            "cve",
            "reachability"
          ],
          "factors_breakdown": {
            "cve_counts": {
              "Critical": 0,
              "High": 21,
              "Medium": 73
            },
            "internet_reachability": "Unknown"
          }
        },
        "IMAGE_RISK_SCORE": 6.4,
        "PACKAGE_STATUS": "NO_AGENT_AVAILABLE",
        "RISK_SCORE": 6.4,
        "START_TIME": "2024-11-05 19:05:03.553",
        "STATUS": "GOOD"
        }
        

  * Network Traffic or Connection Summary
        
        {
        "DST_ENTITY_ID": {
          "hostname": "service-A.region.amazonaws.com",
          "ip_internal": 0,
          "port": 443,
          "protocol": "TCP"
        },
        "DST_ENTITY_TYPE": "DnsSep",
        "DST_IN_BYTES": 0,
        "DST_OUT_BYTES": 0,
        "ENDPOINT_DETAILS": [
          {
            "dst_ip_addr": "203.0.113.10",
            "dst_port": 443,
            "protocol": "TCP",
            "src_ip_addr": "192.168.1.10"
          },
          {
            "dst_ip_addr": "198.51.100.5",
            "dst_port": 443,
            "protocol": "TCP",
            "src_ip_addr": "192.168.1.10"
          }
        ],
        "END_TIME": "2024-11-05 21:00:00.000",
        "NUM_CONNS": 4,
        "SRC_ENTITY_ID": {
          "mid": 2080882850610892909,
          "pid_hash": 744766973756676842
        },
        "SRC_ENTITY_TYPE": "Process",
        "SRC_IN_BYTES": 25028,
        "SRC_OUT_BYTES": 11962,
        "START_TIME": "2024-11-05 20:00:00.000"
        }
        

  * Package Information or Update
        
        {
        "ARCH": "x86_64",
        "CREATED_TIME": "2024-11-08 01:28:30.566",
        "MID": 4172267319977985370,
        "PACKAGE_NAME": "grub2",
        "VERSION": "2:2.02-0.87.0.2.el7.el7.centos.14.tuxcare.els2"
        }
        

  * Container Process Activity
        
        {
        "CONTAINER_ID": "4853339865add970f72213ec5d76ff51d1308c61a7680cc23c8de20c38c0a8e1",
        "END_TIME": "2024-11-08 02:00:00.000",
        "FILE_PATH": "/app/grpc-health-probe",
        "MID": 3708952045169222383,
        "PID": 177267,
        "POD_NAME": "kubernetes-pod-abc",
        "PPID": 177257,
        "PROCESS_START_TIME": "2024-11-08 01:43:29.960",
        "START_TIME": "2024-11-08 01:00:00.000",
        "UID": 0,
        "USERNAME": "serviceuser"
        }
        

  * General Alert or Event (CloudTrail)
        
        {
        "EVENT_ID": "413328",
        "EVENT_NAME": "Unauthorized API Call",
        "EVENT_TYPE": "CloudTrailDefaultAlert",
        "SUMMARY": " For account: 999999999999 (and 22 more) : event Unauthorized API Call from a username other "
                   "than whitelisted ones. Replaces lacework-global-29 occurred 3772 times by user "
                   "UDM-PRINCIPAL-ID:UDM-SERVICE-ROLE (and 167 more) ",
        "START_TIME": "07 Feb 2025 12:00 GMT",
        "EVENT_CATEGORY": "Aws",
        "LINK": "https://security.example.net/ui/alert/12345/details",
        "ACCOUNT": "UDM_ACCOUNT",
        "SOURCE": "CloudTrail",
        "subject": {
          "srcEvent": {
            "event": {
              "errorCode": "AccessDenied",
              "errorMessage": "User: arn:aws:sts::999999999999:assumed-role/UDM-SERVICE-ROLE-IngestionApiRole/UDM-SERVICE-PRINCIPAL "
                              "is not authorized to perform: kinesis:ListShards on resource: "
                              "arn:aws:kinesis:us-east-1:999999999999:stream/ingestion-qa-rel-fraud-review-Stream "
                              "because no identity-based policy allows the kinesis:ListShards action",
              "eventName": "ListShards",
              "eventSource": "kinesis.amazonaws.com",
              "eventTime": "2025-02-07T12:00:24Z",
              "recipientAccountId": "999999999999",
              "sourceIPAddress": "firehose.amazonaws.com",
              "userIdentity": {
                "accessKeyId": "ACCESSKEYIDDUMMY",
                "accountId": "999999999999",
                "arn": "arn:aws:sts::999999999999:assumed-role/UDM-SERVICE-ROLE-IngestionApiRole/UDM-SERVICE-PRINCIPAL",
                "sessionContext": {
                  "sessionIssuer": {
                    "accountId": "999999999999",
                    "arn": "arn:aws:iam::999999999999:role/UDM-SERVICE-ROLE-IngestionApiRole",
                    "principalId": "PRINCIPALIDDUMMY",
                    "userName": "UDM-SERVICE-ROLE-IngestionApiRole"
                  }
                }
              },
              "vpcEndpointId": "vpce-00000000000000000"
            },
            "principalId": "PRINCIPALIDDUMMY:UDM-SERVICE-PRINCIPAL",
            "recipientAccountId": "999999999999",
            "sourceIPAddress": "firehose.amazonaws.com",
            "userIdentityName": "UDM-SERVICE-ROLE-IngestionApiRole"
          }
        }
        }
        




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
alertId | metadata.product_log_id | Value copied directly  
alertName | security_result.rule_name | Value copied directly  
severity | security_result.severity | Mapped to UDM severity  
status | security_result.summary | Value copied directly  
alertType | security_result.category_details | Value copied directly  
startTime | metadata.event_timestamp | Parsed as ISO 8601 timestamp  
endTime | additional.fields | Stored as end_time label  
alertInfo.description | security_result.description | Value copied directly  
alertInfo.subject | metadata.description | Value copied directly  
entityMap.Machine.hostname | principal.hostname | Value copied directly  
entityMap.Machine.externalIp | principal.ip | Value copied directly  
entityMap.User.username | principal.user.userid | Value copied directly  
entityMap.Region.region | principal.location.name | Value copied directly  
entityMap.CT_User.accountId | principal.user.product_object_id | Value copied directly  
`event_title` | `event.idm.read_only_udm.security_result.summary` | Mapped from changelog  
`event_description` | `event.idm.read_only_udm.security_result.description` | Mapped from changelog  
`summary_details` | `event.idm.read_only_udm.security_result.confidence_details` | Mapped from changelog  
`target_user_id` | `event.idm.read_only_udm.target.user.userid` | Mapped from changelog  
`resource_product_id` | `event.idm.read_only_udm.target.resource.product_object_id` | Mapped from changelog  
`user_role` | `event.idm.read_only_udm.target.user.role_name` | Mapped from changelog  
`account_name` | `event.idm.read_only_udm.target.resource.name` | Mapped from changelog  
`application` | `event.idm.read_only_udm.target.application` | Mapped from changelog  
`event_id` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`event_type` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`event_severity` | `event.idm.read_only_udm.security_result.severity_details` | Mapped from changelog  
`lacework_account` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`event_link` | `event.idm.read_only_udm.metadata.url_back_to_product` | Mapped from changelog  
`starttimevalue` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`endtimevalue` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`intgGuid` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`rec_id` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`event_source` | `event.idm.read_only_udm.metadata.product_name` | Mapped from changelog  
`event_timestamp` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`ACCOUNT", "EVENT_CATEGORY", "subject.srcEvent.recipientAccountAlias", "DERIVED_FIELDS.SOURCE", "subject.srcEvent.event.userIdentity.accessKeyId", "subject.srcEvent.event.userIdentity.arn", "subject.srcEvent.event.errorCode", "subject.srcEvent.event.errorMessage", "subject.srcEvent.event.eventID", "subject.srcEvent.event.eventSource", "subject.srcEvent.event.userIdentity.sessionContext.attributes.mfaAuthenticated", "subject.srcEvent.username", "subject.startTime", "subject.srcEvent.eventName", "DERIVED_FIELDS.CATEGORY", "DERIVED_FIELDS.SUBCATEGORY", "subject.dstEvent.gbm_version", "subject.dstEvent.is_visible", "subject.dstEvent.severity", "subject.dstEvent.recipientAccountAlias", "subject.srcEvent.api", "subject.srcEvent.calltype", "subject.srcEvent.gbm_version", "subject.srcEvent.is_visible", and "subject.srcEvent.severity` | `additional.fields` | Mapped from changelog  
`SUMMARY` | `metadata.description` | Mapped from changelog  
`EVENT_TYPE` | `metadata.product_event_type` | Mapped from changelog  
`EVENT_ID` | `metadata.product_log_id` | Mapped from changelog  
`LINK` | `metadata.url_back_to_product` | Mapped from changelog  
`subject.srcEvent.event.userAgent", "subject.srcEvent.source` | `network.http.user_agent` | Mapped from changelog  
`subject.srcEvent.recipientAccountId` | `principal.user.groupid` | Mapped from changelog  
`subject.srcEvent.principalId` | `principal.user.userid` | Mapped from changelog  
`subject.srcEvent.event.awsRegion` | `security_result.about.asset.attribute.cloud.availability_zone` | Mapped from changelog  
`subject.srcEvent.event.eventCategory` | `security_result.about.asset.category` | Mapped from changelog  
`EVENT_NAME` | `security_result.category` | Mapped from changelog  
`EVENT_NAME` | `security_result.summary` | Mapped from changelog  
`subject.srcType` | `src.resource.resource_subtype` | Mapped from changelog  
`subject.srcEvent.event.userIdentity.sessionContext.attributes.creationDate` | `metadata.event_timestamp` | Mapped from changelog  
`subject.srcEvent.accountcaller` | `principal.resource.product_object_id` | Mapped from changelog  
`subject.dstEvent.region` | `target.asset.location.name` | Mapped from changelog  
`subject.dstEvent.accountcaller` | `target.resource.product_object_id` | Mapped from changelog  
`subject.dstType` | `target.resource.resource_subtype` | Mapped from changelog  
`subject.dstEvent.service` | `target.url` | Mapped from changelog  
`subject.dstEvent.username` | `target.user.userid` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/lacework-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
