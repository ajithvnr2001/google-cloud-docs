---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/kyriba/
title: Collect Kyriba Treasury Management logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:54:31.055077+00:00
---

# Collect Kyriba Treasury Management logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/kyriba/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Kyriba Treasury Management logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Kyriba Treasury Management logs to Google Security Operations using Google Cloud Storage V2.

Kyriba is a cloud-based treasury and finance management platform. It generates audit logs for payment operations, user access, approval workflows, and financial transactions. The parser extracts fields from Kyriba audit data and maps them to the Unified Data Model (UDM), capturing user identity, transaction details, approval status, and security results.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * Privileged access to the Kyriba platform with authority to configure API access and generate OAuth2 credentials



## Create a Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `kyriba-treasury-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Collect Kyriba API credentials

### Get your Kyriba instance URL

  1. Sign in to your Kyriba platform.
  2. Note your instance URL from the browser address bar. 
     * Format: `https://<your-instance>.kyriba.com`
     * Example: If you access Kyriba at `https://acme.kyriba.com/gateway`, your instance URL is `https://acme.kyriba.com`



### Create OAuth2 API credentials

  1. Sign in to the Kyriba platform as an administrator.
  2. Navigate to **Administration > API Access**.
  3. Click **Create** or **Add Application**.
  4. Provide the following configuration details: 
     * **Application name** : Enter `Google Security Operations Integration`
     * **Grant type** : Select **Client Credentials**
  5. Click **Save**.
  6. Copy and save the credentials securely:

     * **Client ID** : Copy this value
     * **Client Secret** : Copy this value
**Note:** The account used to create the credentials must have administrator permissions to access the Kyriba API.



### Verify permissions

To verify the credentials have the required permissions:

  1. Sign in to the Kyriba platform.
  2. Navigate to **Administration > API Access**.
  3. Confirm the application you created is listed and has an **Active** status.
  4. Verify the application has access to the **Audit Trail** API scope.



### Test API access

  * Test your credentials before proceeding with the integration:
        
        # Replace with your actual credentials
        CLIENT_ID="<your-client-id>"
        CLIENT_SECRET="<your-client-secret>"
        KYRIBA_HOST="https://<your-instance>.kyriba.com"
        
        # Get OAuth2 token
        TOKEN=$(curl -s -X POST "${KYRIBA_HOST}/gateway/oauth/token" \
          -H "Content-Type: application/x-www-form-urlencoded" \
          -d "grant_type=client_credentials&client_id=${CLIENT_ID}&client_secret=${CLIENT_SECRET}" \
          | python3 -c "import sys,json; print(json.load(sys.stdin)['access_token'])")
        
        # Test API access
        curl -v -H "Authorization: Bearer ${TOKEN}" \
          "${KYRIBA_HOST}/gateway/api/v1/audit-trails?startDate=2024-01-01&endDate=2024-01-02"
        




## Create a service account for the Cloud Run function

The Cloud Run function needs a service account with permissions to write to GCS bucket and be invoked by Pub/Sub.

### Create a service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `kyriba-logs-collector-sa`
     * **Service account description** : Enter `Service account for Cloud Run function to collect Kyriba Treasury Management logs`
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



### Grant IAM permissions on the GCS bucket

Grant the service account write permissions on the GCS bucket:

  1. Go to **Cloud Storage > Buckets**.
  2. Click on your bucket name (for example, `kyriba-treasury-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `kyriba-logs-collector-sa@PROJECT_ID.iam.gserviceaccount.com`)
     * **Assign roles** : Select **Storage Object Admin**
  6. Click **Save**.



## Create a Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `kyriba-logs-trigger`
     * Leave other settings as default
  4. Click **Create**.



## Create a Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from the Kyriba API and write them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `kyriba-logs-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose the Pub/Sub topic (`kyriba-logs-trigger`).
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select the service account (`kyriba-logs-collector-sa`)
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `kyriba-treasury-logs` | GCS bucket name  
`GCS_PREFIX` | `kyriba` | Prefix for log files  
`STATE_KEY` | `kyriba/state.json` | State file path  
`KYRIBA_HOST` | `https://<your-instance>.kyriba.com` | Kyriba instance URL  
`CLIENT_ID` | `your-client-id` | OAuth2 Client ID  
`CLIENT_SECRET` | `your-client-secret` | OAuth2 Client Secret  
`MAX_RECORDS` | `1000` | Max records per run  
`PAGE_SIZE` | `100` | Records per page  
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
             import urllib.parse
           
             # Initialize HTTP client with timeouts
             http = urllib3.PoolManager(
               timeout=urllib3.Timeout(connect=5.0, read=30.0),
               retries=False,
             )
           
             # Initialize Storage client
             storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
           
             # Environment variables
             GCS_BUCKET = os.environ.get('GCS_BUCKET')
             GCS_PREFIX = os.environ.get('GCS_PREFIX', 'kyriba')
             STATE_KEY = os.environ.get('STATE_KEY', 'kyriba/state.json')
             KYRIBA_HOST = os.environ.get('KYRIBA_HOST')
             CLIENT_ID = os.environ.get('CLIENT_ID')
             CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
             MAX_RECORDS = int(os.environ.get('MAX_RECORDS', '1000'))
             PAGE_SIZE = int(os.environ.get('PAGE_SIZE', '100'))
             LOOKBACK_HOURS = int(os.environ.get('LOOKBACK_HOURS', '24'))
           
             def parse_datetime(value: str) -> datetime:
               """Parse ISO datetime string to datetime object."""
               if [value](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.ObjectCustomContextPayload.html#google_cloud_storage_blob_ObjectCustomContextPayload_value).endswith("Z"):
                 value = value[:-1] + "+00:00"
               return datetime.fromisoformat(value)
           
             def get_oauth_token(host: str, client_id: str, client_secret: str) -> str:
               """Get OAuth 2.0 access token from Kyriba."""
               token_url = f"{host.rstrip('/')}/gateway/oauth/token"
               data = urllib.parse.urlencode({
                 'grant_type': 'client_credentials',
                 'client_id': client_id,
                 'client_secret': client_secret,
               }).encode('utf-8')
               response = http.request(
                 'POST', token_url,
                 body=data,
                 headers={'Content-Type': 'application/x-www-form-urlencoded'},
               )
               if response.status != 200:
                 raise Exception(f"OAuth token request failed: {response.status} {response.data.decode('utf-8')}")
               token_data = json.loads(response.data.decode('utf-8'))
               return token_data['access_token']
           
             @functions_framework.cloud_event
             def main(cloud_event):
               """
               Cloud Run function triggered by Pub/Sub to fetch Kyriba Treasury Management
               audit logs and write them to GCS.
           
               Args:
                 cloud_event: CloudEvent object containing Pub/Sub message
               """
           
               if not all([GCS_BUCKET, KYRIBA_HOST, CLIENT_ID, CLIENT_SECRET]):
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
           
                 # Get OAuth token
                 token = get_oauth_token(KYRIBA_HOST, CLIENT_ID, CLIENT_SECRET)
                 print("Successfully obtained OAuth2 token")
           
                 # Fetch logs
                 records, newest_event_time = fetch_logs(
                   host=KYRIBA_HOST,
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
           
             def fetch_logs(host: str, token: str, start_time: datetime, end_time: datetime, page_size: int, max_records: int):
               """
               Fetch audit trail logs from Kyriba API with pagination and rate limiting.
           
               Args:
                 host: Kyriba instance URL
                 token: OAuth2 access token
                 start_time: Start time for log query
                 end_time: End time for log query
                 page_size: Number of records per page
                 max_records: Maximum total records to fetch
           
               Returns:
                 Tuple of (records list, newest_event_time ISO string)
               """
               base_url = host.rstrip('/')
               endpoint = f"{base_url}/gateway/api/v1/audit-trails"
           
               headers = {
                 'Authorization': f'Bearer {token}',
                 'Accept': 'application/json',
                 'Content-Type': 'application/json',
                 'User-Agent': 'GoogleSecOps-KyribaCollector/1.0',
               }
           
               records = []
               newest_time = None
               page_num = 0
               backoff = 1.0
               offset = 0
           
               start_date = start_time.strftime('%Y-%m-%d')
               end_date = end_time.strftime('%Y-%m-%d')
           
               while True:
                 page_num += 1
           
                 if len(records) >= max_records:
                   print(f"Reached max_records limit ({max_records})")
                   break
           
                 params = []
                 params.append(f"startDate={start_date}")
                 params.append(f"endDate={end_date}")
                 params.append(f"offset={offset}")
                 params.append(f"limit={min(page_size, max_records - len(records))}")
                 url = f"{endpoint}?{'&'.join(params)}"
           
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
           
                   page_results = data.get('results', [])
           
                   if not page_results:
                     print(f"No more results (empty page)")
                     break
           
                   print(f"Page {page_num}: Retrieved {len(page_results)} events")
                   records.extend(page_results)
           
                   # Track newest event time
                   for event in page_results:
                     try:
                       event_time = event.get('dateTime') or event.get('date')
                       if event_time:
                         if newest_time is None or parse_datetime(event_time) > parse_datetime(newest_time):
                           newest_time = event_time
                     except Exception as e:
                       print(f"Warning: Could not parse event time: {e}")
           
                   # Check for more results
                   if len(page_results) < page_size:
                     print(f"Reached last page (size={len(page_results)} < limit={page_size})")
                     break
           
                   offset += len(page_results)
           
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
**Name** | `kyriba-logs-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the Pub/Sub topic (`kyriba-logs-trigger`)  
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
  5. Click on your function name (`kyriba-logs-collector`).
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         Fetching logs from YYYY-MM-DDTHH:MM:SS+00:00 to YYYY-MM-DDTHH:MM:SS+00:00
         Successfully obtained OAuth2 token
         Page 1: Retrieved X events
         Wrote X records to gs://kyriba-treasury-logs/kyriba/logs_YYYYMMDD_HHMMSS.ndjson
         Successfully processed X records
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click on your bucket name (`kyriba-treasury-logs`).

  10. Navigate to the prefix folder (`kyriba/`).

  11. Verify that a new `.ndjson` file was created with the current timestamp.




If you see errors in the logs:

  * **HTTP 401** : Check OAuth2 credentials (Client ID and Client Secret) in environment variables
  * **HTTP 403** : Verify the API application has access to the Audit Trail scope
  * **HTTP 429** : Rate limiting - function will automatically retry with backoff
  * **Missing environment variables** : Check all required variables are set



## Retrieve the Google SecOps service account

Google SecOps uses a unique service account to read data from your GCS bucket. You must grant this service account access to your bucket.

### Get the service account email

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Kyriba Treasury Management Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Kyriba Treasury Management** as the **Log type**.
  7. Click **Get Service Account**.
  8. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  9. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Don't use service accounts from other documentation or examples.
  10. Click **Next**.

  11. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://kyriba-treasury-logs/kyriba/
           

       * Replace: 
         * `kyriba-treasury-logs`: Your GCS bucket name.
         * `kyriba`: Optional prefix/folder path where logs are stored (leave empty for root).
**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never** : Never deletes any files after transfers (recommended for testing).
       * **Delete transferred files** : Deletes files after successful transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.

**Note:** If you select a deletion option, the service account must have **Storage Object Admin** role instead of Storage Object Viewer. Update IAM permissions accordingly.
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days)

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)

     * **Ingestion labels** : The label to be applied to the events from this feed

  12. Click **Next**.

  13. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## Grant IAM permissions to the Google SecOps service account

The Google SecOps service account needs **Storage Object Viewer** role on your GCS bucket.

  1. Go to **Cloud Storage > Buckets**.
  2. Click on your bucket name (for example, `kyriba-treasury-logs`).
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
column11 | metadata.description | Value copied directly  
column16, column17 | metadata.event_timestamp | Parsed from date and time fields using date filter with formats "MM/dd/yyyy hh:mm A" and "MM/dd/yyyy h:m A"  
principal_userid | metadata.event_type | Set to "USER_RESOURCE_CREATION" if principal_userid is not empty, else "GENERIC_EVENT"  
column3 | principal.user.company_name | Value copied directly  
column15 | principal.user.userid | Value copied directly  
status | sec_result.action | Set to "ALLOW" if status is "Remitted", else "BLOCK"  
column6 | sec_result.description | Value copied directly  
sec_result | security_result | Value copied directly  
column4 | target.location.name | Value copied directly  
column1 | target.resource.id | Value copied directly  
| target.resource.name | Set to "TRANSACTION"  
| target.resource.resource_type |   
column13 | target.user.company_name | Value copied directly  
| metadata.product_name | Set to "KYRIBA TREASURY"  
| metadata.vendor_name | Set to "KYRIBA"  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
