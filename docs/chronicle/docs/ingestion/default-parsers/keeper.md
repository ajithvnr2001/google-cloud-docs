---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/keeper/
title: Collect Keeper Enterprise Security logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:45:03.859038+00:00
---

# Collect Keeper Enterprise Security logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/keeper/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Keeper Enterprise Security logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Keeper Enterprise Security logs to Google Security Operations using Google Cloud Storage V2.

Keeper Enterprise Security is an enterprise password manager and privileged access management platform that protects credentials, secrets, and sensitive data. It generates audit logs for vault access, password changes, sharing events, and administrative actions through the Reporting and Alerts API.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * Privileged access to the Keeper Admin Console with administrator permissions
  * A Keeper Enterprise or Business plan with the Advanced Reporting and Alerts Module (ARAM) enabled



## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `keeper-audit-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Collect Keeper Enterprise Security API credentials

### Create API key

  1. Sign in to the [Keeper Admin Console](https://keepersecurity.com/console).
  2. Go to **Admin > Reporting & Alerts**.
  3. Click **API Keys** or navigate to the API key management section.
  4. Click **Create API Key**.
  5. Enter a name for the API key (for example, `Google Security Operations Integration`).
  6. Copy and save the following details in a secure location: 
     * **API Key** : The generated API key value
     * **Private Key** : Download the private key file (used for token generation)
  7. Note your Keeper Enterprise **Enterprise ID** from the Admin Console.

**Note:** The API key must have access to the Reporting and Alerts Module (ARAM) endpoints. Contact Keeper support if the ARAM module is not enabled for your enterprise.



### Determine API base URL

  * The Keeper API base URL depends on your data center region:

Region | API Base URL  
---|---  
US | `https://keepersecurity.com`  
EU | `https://keepersecurity.eu`  
AU | `https://keepersecurity.com.au`  
CA | `https://keepersecurity.ca`  
JP | `https://keepersecurity.jp`  
US GovCloud | `https://govcloud.keepersecurity.us`  
**Note:** Confirm your region from the Keeper Admin Console URL or your account documentation.



### Verify permissions

To verify the account has the required permissions:

  1. Sign in to the [Keeper Admin Console](https://keepersecurity.com/console).
  2. Go to **Admin > Reporting & Alerts**.
  3. If you can see the **Reporting & Alerts** dashboard and **API Keys** section, you have the required permissions.
  4. If you cannot see this option, contact your Keeper administrator to enable the ARAM module and grant administrator access.



### Test API access

  * Test your credentials before proceeding with the integration:
        
        # Replace with your actual credentials
        KEEPER_API_KEY="your-api-key"
        KEEPER_BASE="https://keepersecurity.com"
        
        # Test API access - get audit events (requires signed token)
        # Note: Keeper uses a signed JWT for authentication.
        # Refer to Keeper Commander CLI for testing:
        keeper audit-report --format json --limit 1
        




## Create a service account for the Cloud Run function

The Cloud Run function needs a service account with permissions to write to GCS bucket and be invoked by Pub/Sub.

### Create service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `keeper-logs-collector-sa`
     * **Service account description** : Enter `Service account for Cloud Run function to collect Keeper Enterprise Security logs`
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
  2. Click on your bucket name (for example, `keeper-audit-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `keeper-logs-collector-sa@PROJECT_ID.iam.gserviceaccount.com`)
     * **Assign roles** : Select **Storage Object Admin**
  6. Click **Save**.



## Create Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `keeper-logs-trigger`
     * Leave other settings as default
  4. Click **Create**.



## Create Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from Keeper Reporting and Alerts API and write them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `keeper-logs-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose the topic `keeper-logs-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select the service account `keeper-logs-collector-sa`.
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `keeper-audit-logs` | GCS bucket name  
`GCS_PREFIX` | `keeper` | Prefix for log files  
`STATE_KEY` | `keeper/state.json` | State file path  
`KEEPER_API_BASE` | `https://keepersecurity.com` | Keeper API base URL  
`KEEPER_API_KEY` | `your-api-key` | Keeper API key  
`KEEPER_PRIVATE_KEY` | `base64-encoded-private-key` | Base64-encoded private key  
`KEEPER_ENTERPRISE_ID` | `12345` | Enterprise ID  
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

     * First file - **main.py:**
           
           import functions_framework
             from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
             import json
             import os
             import urllib3
             from datetime import datetime, timezone, timedelta
             import time
             import base64
             import hashlib
             import hmac
           
             # Initialize HTTP client with timeouts
             http = urllib3.PoolManager(
               timeout=urllib3.Timeout(connect=5.0, read=30.0),
               retries=False,
             )
           
             # Initialize Storage client
             storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
           
             # Environment variables
             GCS_BUCKET = os.environ.get('GCS_BUCKET')
             GCS_PREFIX = os.environ.get('GCS_PREFIX', 'keeper')
             STATE_KEY = os.environ.get('STATE_KEY', 'keeper/state.json')
             KEEPER_API_BASE = os.environ.get('KEEPER_API_BASE', 'https://keepersecurity.com')
             KEEPER_API_KEY = os.environ.get('KEEPER_API_KEY')
             KEEPER_PRIVATE_KEY = os.environ.get('KEEPER_PRIVATE_KEY')
             KEEPER_ENTERPRISE_ID = os.environ.get('KEEPER_ENTERPRISE_ID')
             MAX_RECORDS = int(os.environ.get('MAX_RECORDS', '5000'))
             PAGE_SIZE = int(os.environ.get('PAGE_SIZE', '1000'))
             LOOKBACK_HOURS = int(os.environ.get('LOOKBACK_HOURS', '24'))
           
             def to_unix_millis(dt: datetime) -> int:
               """Convert datetime to Unix epoch milliseconds."""
               if dt.tzinfo is None:
                 dt = dt.replace(tzinfo=timezone.utc)
               dt = dt.astimezone(timezone.utc)
               return int(dt.timestamp() * 1000)
           
             def parse_datetime(value: str) -> datetime:
               """Parse ISO datetime string to datetime object."""
               if [value](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.ObjectCustomContextPayload.html#google_cloud_storage_blob_ObjectCustomContextPayload_value).endswith("Z"):
                 value = value[:-1] + "+00:00"
               return datetime.fromisoformat(value)
           
             def get_auth_token():
               """
               Generate authentication token for Keeper Reporting API.
               Uses HMAC-SHA512 signing with the private key.
               """
               api_base = KEEPER_API_BASE.rstrip('/')
               token_url = f"{api_base}/api/rest/enterprise/auth/token"
           
               # Build token request
               timestamp = str(int(time.time()))
               message = f"{KEEPER_API_KEY}:{timestamp}"
           
               # Decode private key from base64
               private_key_bytes = base64.b64decode(KEEPER_PRIVATE_KEY)
           
               # Sign with HMAC-SHA512
               signature = hmac.new(
                 private_key_bytes,
                 message.encode('utf-8'),
                 hashlib.sha512
               ).digest()
               signature_b64 = base64.b64encode(signature).decode('utf-8')
           
               body = json.dumps({
                 'api_key': KEEPER_API_KEY,
                 'timestamp': timestamp,
                 'signature': signature_b64,
                 'enterprise_id': KEEPER_ENTERPRISE_ID
               })
           
               headers = {
                 'Content-Type': 'application/json',
                 'Accept': 'application/json'
               }
           
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
                   raise RuntimeError(f"Failed to get auth token: {response.status} - {response.data.decode('utf-8')}")
           
                 data = json.loads(response.data.decode('utf-8'))
                 return data.get('token', data.get('access_token'))
           
               raise RuntimeError("Failed to get auth token after 3 retries")
           
             @functions_framework.cloud_event
             def main(cloud_event):
               """
               Cloud Run function triggered by Pub/Sub to fetch Keeper Enterprise
               Security audit logs and write to GCS.
           
               Args:
                 cloud_event: CloudEvent object containing Pub/Sub message
               """
           
               if not all([GCS_BUCKET, KEEPER_API_KEY, KEEPER_PRIVATE_KEY, KEEPER_ENTERPRISE_ID]):
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
           
                 # Get auth token
                 token = get_auth_token()
           
                 # Fetch logs
                 records, newest_event_time = fetch_logs(
                   token=token,
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
           
             def fetch_logs(token: str, start_time: datetime, end_time: datetime, page_size: int, max_records: int):
               """
               Fetch audit event logs from Keeper Reporting and Alerts API
               with pagination and rate limiting.
           
               Args:
                 token: Authentication token
                 start_time: Start time for log query
                 end_time: End time for log query
                 page_size: Number of records per page
                 max_records: Maximum total records to fetch
           
               Returns:
                 Tuple of (records list, newest_event_time ISO string)
               """
               api_base = KEEPER_API_BASE.rstrip('/')
               endpoint = f"{api_base}/api/rest/enterprise/audit-events"
           
               headers = {
                 'Authorization': f'Bearer {token}',
                 'Accept': 'application/json',
                 'Content-Type': 'application/json',
                 'User-Agent': 'GoogleSecOps-KeeperCollector/1.0'
               }
           
               records = []
               newest_time = None
               page_num = 0
               backoff = 1.0
           
               # Convert to Unix epoch seconds for Keeper API
               start_epoch = int(start_time.timestamp())
               end_epoch = int(end_time.timestamp())
               cursor = None
           
               while True:
                 page_num += 1
           
                 if len(records) >= max_records:
                   print(f"Reached max_records limit ({max_records})")
                   break
           
                 # Build request body
                 body = {
                   'start_time': start_epoch,
                   'end_time': end_epoch,
                   'limit': min(page_size, max_records - len(records)),
                   'enterprise_id': KEEPER_ENTERPRISE_ID
                 }
                 if cursor:
                   body['cursor'] = cursor
           
                 try:
                   response = http.request(
                     'POST',
                     endpoint,
                     body=json.dumps(body),
                     headers=headers
                   )
           
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
           
                   page_results = data.get('audit_events', data.get('events', []))
           
                   if not page_results:
                     print(f"No more results (empty page)")
                     break
           
                   print(f"Page {page_num}: Retrieved {len(page_results)} events")
                   records.extend(page_results)
           
                   # Track newest event time
                   for event in page_results:
                     try:
                       event_ts = event.get('timestamp') or event.get('created')
                       if event_ts:
                         if isinstance(event_ts, (int, float)):
                           event_dt = datetime.fromtimestamp(event_ts, tz=timezone.utc)
                           event_time = event_dt.isoformat()
                         else:
                           event_time = str(event_ts)
                         if newest_time is None or parse_datetime(event_time) > parse_datetime(newest_time):
                           newest_time = event_time
                     except Exception as e:
                       print(f"Warning: Could not parse event time: {e}")
           
                   # Check for more results
                   cursor = data.get('cursor') or data.get('next_cursor')
                   if not cursor:
                     print("No more pages (no next cursor)")
                     break
           
                 except Exception as e:
                   print(f"Error fetching logs: {e}")
                   return [], None
           
               print(f"Retrieved {len(records)} total records from {page_num} pages")
               return records, newest_time
           

     * Second file - **requirements.txt:**
           
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
**Name** | `keeper-logs-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the topic `keeper-logs-trigger`  
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
  5. Click on `keeper-logs-collector`.
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         Fetching logs from YYYY-MM-DDTHH:MM:SS+00:00 to YYYY-MM-DDTHH:MM:SS+00:00
         Page 1: Retrieved X events
         Wrote X records to gs://keeper-audit-logs/keeper/logs_YYYYMMDD_HHMMSS.ndjson
         Successfully processed X records
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click on your bucket name (`keeper-audit-logs`).

  10. Navigate to the `keeper/` folder.

  11. Verify that a new `.ndjson` file was created with the current timestamp.




If you see errors in the logs:

  * **HTTP 401** : Check API credentials in environment variables
  * **HTTP 403** : Verify account has required ARAM permissions in Keeper Admin Console
  * **HTTP 429** : Rate limiting - function will automatically retry with backoff
  * **Missing environment variables** : Check all required variables are set



## Configure a feed in Google SecOps to ingest Keeper Enterprise Security logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Keeper Enterprise Security Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Keeper Enterprise Security** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy the email address.

**Note:** Each Google SecOps instance has a unique service account. Do not use service accounts from other documentation or examples.
  9. Click **Next**.

  10. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://keeper-audit-logs/keeper/
           

       * Replace: 
         * `keeper-audit-logs`: Your GCS bucket name.
         * `keeper`: Optional prefix/folder path where logs are stored (leave empty for root).
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

The Google SecOps service account needs the **Storage Object Viewer** role on your GCS bucket.

  1. Go to **Cloud Storage > Buckets**.
  2. Click on your bucket name.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Paste the Google SecOps service account email
     * **Assign roles** : Select **Storage Object Viewer**
  6. Click **Save**.

**Note:** If you plan to use the deletion option "Delete transferred files" or "Delete transferred files and empty directories," grant **Storage Object Admin** role instead of Storage Object Viewer.

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
logData.channel | extensions.auth.type | Set to uppercase value if in ["SSO", "MACHINE", "VPN", "PHYSICAL", "TACACS"], else "AUTHTYPE_UNSPECIFIED"  
logData.timestamp | metadata.event_timestamp | Converted using ISO8601 format  
logData.audit_event, logData.remote_address | metadata.event_type | Set to "USER_LOGIN" if audit_event matches "login" and remote_address is not empty, else "STATUS_UPDATE" if remote_address not empty, else "GENERIC_EVENT"  
logData.audit_event | metadata.product_event_type | Value copied directly  
logData.enterprise_id | metadata.product_log_id | Converted to string  
| metadata.product_name | Set to "KEEPER"  
| metadata.vendor_name | Set to "KEEPER"  
logData.client_version | network.http.parsed_user_agent | Value copied directly, then converted to parseduseragent  
logData.client_version | network.http.user_agent | Value copied directly  
logData.remote_address | principal.asset.ip | Value copied directly  
logData.remote_address | principal.ip | Value copied directly  
logData.category | security_result.category_details | Merged from source  
logData.shared_folder_uid, logData.folder_uid | security_result.detection_fields | Merged as labels with keys "shared_folder_uid" and "folder_uid"  
logData.email | target.user.email_addresses | Merged from source  
logData.username | target.user.userid | Value copied directly  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/keeper-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
