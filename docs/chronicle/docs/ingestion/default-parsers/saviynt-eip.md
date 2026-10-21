---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/saviynt-eip/
title: Collect Saviynt Enterprise Identity Cloud logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T14:32:45.796894+00:00
---

# Collect Saviynt Enterprise Identity Cloud logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/saviynt-eip/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Saviynt Enterprise Identity Cloud logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Saviynt Enterprise Identity Cloud (EIP) logs to Google Security Operations using Google Cloud Storage V2.

Saviynt Enterprise Identity Cloud (EIP) is an identity governance and cloud security platform used for access management, identity lifecycle management, and compliance. It generates audit log data for all security activities performed within the Identity Repository.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * Privileged access to Saviynt EIP with administrator permissions



## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `saviynt-eip-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Collect Saviynt EIP API credentials

### Obtain API credentials

  1. Sign in to the **Saviynt EIP** admin console.
  2. Go to **Admin > Settings > Connections**.
  3. Create or identify an API user with the following permissions: 
     * **webservice_api_authenticateUser**
     * **api_v5_fetchRuntimeControlsData**
  4. Note the following details: 
     * **Username** : The API user account username.
     * **Password** : The API user account password.
     * **Saviynt Host URL** : Your Saviynt tenant URL (for example, `https://YOUR_SAVIYNT_HOST`).



### Determine analytics name

  1. In the Saviynt admin console, go to **Admin > Runtime Controls**.
  2. Note the **Analytics Name** for the audit data you want to export (for example, `AuditTrailAnalytics`).



### Verify permissions

To verify the API user has the required permissions:

  1. Sign in to the **Saviynt EIP** admin console.
  2. Go to **Admin > User Management**.
  3. Click on the API user account.
  4. Verify the user has **webservice_api_authenticateUser** and **api_v5_fetchRuntimeControlsData** access permissions.
  5. If permissions are missing, contact your Saviynt administrator.



### Test API access

  * Test your credentials before proceeding with the integration:
        
        # Replace with your actual credentials
        SAVIYNT_HOST="https://YOUR_SAVIYNT_HOST"
        USERNAME="your-username"
        PASSWORD="your-password"
        
        # Get authentication token
        TOKEN=$(curl -s -X POST "${SAVIYNT_HOST}/ECM/api/login" \
          -H "Content-Type: application/json" \
          -d "{\"username\": \"${USERNAME}\", \"password\": \"${PASSWORD}\"}" \
          | jq -r '.access_token')
        
        # Test API access
        curl -v -H "Authorization: Bearer ${TOKEN}" \
          -H "Content-Type: application/json" \
          -X POST "${SAVIYNT_HOST}/ECM/api/v5/fetchRuntimeControlsDataV2" \
          -d '{"analyticsname": "YOUR_ANALYTICS_NAME", "timeFrame": 5}'
        




## Create service account for Cloud Run function

The Cloud Run function needs a service account with permissions to write to GCS bucket and be invoked by Pub/Sub.

### Create service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `saviynt-eip-collector-sa`.
     * **Service account description** : Enter `Service account for Cloud Run function to collect Saviynt EIP logs`.
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
  2. Click your bucket name (for example, `saviynt-eip-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `saviynt-eip-collector-sa@your-project.iam.gserviceaccount.com`).
     * **Assign roles** : Select **Storage Object Admin**.
  6. Click **Save**.



## Create Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `saviynt-eip-trigger`.
     * Leave other settings as default.
  4. Click **Create**.



## Create Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from Saviynt EIP API and write them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `saviynt-eip-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose the topic `saviynt-eip-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select the service account `saviynt-eip-collector-sa`.
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `saviynt-eip-logs` | GCS bucket name  
`GCS_PREFIX` | `saviynt` | Prefix for log files  
`STATE_KEY` | `saviynt/state.json` | State file path  
`SAVIYNT_HOST` | `https://YOUR_SAVIYNT_HOST` | Saviynt tenant URL  
`SAVIYNT_USER` | `your-api-username` | API user username  
`SAVIYNT_PASS` | `your-api-password` | API user password  
`ANALYTICS_NAME` | `AuditTrailAnalytics` | Analytics record name  
`TIMEFRAME_MINUTES` | `60` | Timeframe in minutes for each query  
`MAX_RECORDS` | `10000` | Max records per run  
`LOOKBACK_HOURS` | `24` | Initial lookback period  
  10. In the **Variables & Secrets** tab, navigate to the **Requests** section:

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

     * First file **main.py:**
           
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
           GCS_PREFIX = os.environ.get('GCS_PREFIX', 'saviynt')
           STATE_KEY = os.environ.get('STATE_KEY', 'saviynt/state.json')
           SAVIYNT_HOST = os.environ.get('SAVIYNT_HOST', '').rstrip('/')
           SAVIYNT_USER = os.environ.get('SAVIYNT_USER', '')
           SAVIYNT_PASS = os.environ.get('SAVIYNT_PASS', '')
           ANALYTICS_NAME = os.environ.get('ANALYTICS_NAME', '')
           TIMEFRAME_MINUTES = int(os.environ.get('TIMEFRAME_MINUTES', '60'))
           MAX_RECORDS = int(os.environ.get('MAX_RECORDS', '10000'))
           LOOKBACK_HOURS = int(os.environ.get('LOOKBACK_HOURS', '24'))
           
           def parse_datetime(value: str) -> datetime:
             """Parse ISO datetime string to datetime object."""
             if [value](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.ObjectCustomContextPayload.html#google_cloud_storage_blob_ObjectCustomContextPayload_value).endswith("Z"):
               value = value[:-1] + "+00:00"
             return datetime.fromisoformat(value)
           
           def get_token():
             """Get authentication token from Saviynt login API."""
             login_url = f"{SAVIYNT_HOST}/ECM/api/login"
           
             body = json.dumps({
               "username": SAVIYNT_USER,
               "password": SAVIYNT_PASS
             })
           
             headers = {
               'Content-Type': 'application/json',
               'Accept': 'application/json'
             }
           
             backoff = 1.0
             max_retries = 3
           
             for attempt in range(max_retries):
               response = http.request('POST', login_url, body=body.encode('utf-8'), headers=headers)
           
               if response.status == 429:
                 retry_after = int(response.headers.get('Retry-After', str(int(backoff))))
                 print(f"Rate limited (429) on login request. Retrying after {retry_after}s...")
                 time.sleep(retry_after)
                 backoff = min(backoff * 2, 30.0)
                 continue
           
               if response.status != 200:
                 raise RuntimeError(f"Failed to authenticate: {response.status} - {response.data.decode('utf-8')}")
           
               data = json.loads(response.data.decode('utf-8'))
               return data['access_token']
           
             raise RuntimeError(f"Failed to get token after {max_retries} retries due to rate limiting")
           
           @functions_framework.cloud_event
           def main(cloud_event):
             """
             Cloud Run function triggered by Pub/Sub to fetch Saviynt EIP logs and write to GCS.
           
             Args:
               cloud_event: CloudEvent object containing Pub/Sub message
             """
           
             if not all([GCS_BUCKET, SAVIYNT_HOST, SAVIYNT_USER, SAVIYNT_PASS, ANALYTICS_NAME]):
               print('Error: Missing required environment variables')
               return
           
             try:
               bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(GCS_BUCKET)
           
               # Load state
               state = load_state(bucket, STATE_KEY)
           
               now = datetime.now(timezone.utc)
           
               print(f"Fetching audit logs with analytics={ANALYTICS_NAME}, timeFrame={TIMEFRAME_MINUTES}")
           
               # Get access token
               token = get_token()
           
               # Fetch logs
               records = fetch_logs(
                 token=token,
                 analytics_name=ANALYTICS_NAME,
                 timeframe_minutes=TIMEFRAME_MINUTES,
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
           
           def fetch_logs(token: str, analytics_name: str, timeframe_minutes: int, max_records: int):
             """
             Fetch audit logs from Saviynt fetchRuntimeControlsDataV2 API with rate limiting.
           
             Args:
               token: Authentication token
               analytics_name: Name of the analytics record
               timeframe_minutes: Timeframe in minutes for the query
               max_records: Maximum total records to fetch
           
             Returns:
               List of records
             """
             endpoint = f"{SAVIYNT_HOST}/ECM/api/v5/fetchRuntimeControlsDataV2"
           
             headers = {
               'Authorization': f'Bearer {token}',
               'Content-Type': 'application/json',
               'Accept': 'application/json',
               'User-Agent': 'GoogleSecOps-SaviyntCollector/1.0'
             }
           
             body = json.dumps({
               "analyticsname": analytics_name,
               "timeFrame": timeframe_minutes
             })
           
             backoff = 1.0
             max_retries = 3
           
             for attempt in range(max_retries):
               try:
                 response = http.request('POST', endpoint, body=body.encode('utf-8'), headers=headers)
           
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
                   return []
           
                 data = json.loads(response.data.decode('utf-8'))
           
                 # Saviynt returns results in a 'result' or 'results' key
                 records = data.get('result', data.get('results', []))
           
                 if isinstance(records, list):
                   if len(records) > max_records:
                     records = records[:max_records]
                   print(f"Retrieved {len(records)} audit records")
                   return records
                 else:
                   # If the response is a single object, wrap it
                   print(f"Retrieved 1 audit record")
                   return [records]
           
               except Exception as e:
                 print(f"Error fetching logs: {e}")
                 if attempt < max_retries - 1:
                   time.sleep(backoff)
                   backoff = min(backoff * 2, 30.0)
                   continue
                 return []
           
             return []
           

     * Second file **requirements.txt:**
           
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
**Name** | `saviynt-eip-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the topic `saviynt-eip-trigger`  
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

  1. In the **Cloud Scheduler** console, find your job (`saviynt-eip-collector-hourly`).
  2. Click **Force run** to trigger manually.
  3. Wait a few seconds and go to **Cloud Run > Services > saviynt-eip-collector > Logs**.
  4. Verify the function executed successfully. Look for:
         
         Fetching audit logs with analytics=AuditTrailAnalytics, timeFrame=60
         Retrieved X audit records
         Wrote X records to gs://saviynt-eip-logs/saviynt/logs_YYYYMMDD_HHMMSS.ndjson
         Successfully processed X records
         

  5. Check the GCS bucket (`saviynt-eip-logs`) to confirm logs were written.




If you see errors in the logs:

  * **HTTP 401** : Check API credentials in environment variables
  * **HTTP 403** : Verify API user has required permissions in Saviynt admin console
  * **HTTP 429** : Rate limiting - function will automatically retry with backoff
  * **Failed to authenticate** : Verify `SAVIYNT_HOST`, `SAVIYNT_USER`, and `SAVIYNT_PASS` are correct



## Configure a feed in Google SecOps to ingest Saviynt EIP logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Saviynt EIP Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Saviynt Enterprise Identity Cloud** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address. You will use it in the next step.

**Note:** Each Google SecOps instance has a unique service account. Do not use service accounts from other documentation or examples.
  9. Click **Next**.

  10. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://saviynt-eip-logs/saviynt/
           

       * Replace: 
         * `saviynt-eip-logs`: Your GCS bucket name.
         * `saviynt`: Optional prefix/folder path where logs are stored (leave empty for root).
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
  2. Click your bucket name (`saviynt-eip-logs`).
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
action_taken | sr.action_details | Action details  
category | sr.category_details | Category details  
Message,message | metadata.description | Description of the event  
| metadata.event_type | Type of event  
Object Type | metadata.product_event_type | Product-specific event type  
eventId | metadata.product_log_id | Product log ID  
IP Address | principal.ip | IP address  
query | principal.process.command_line | Command line of the process  
actionUri | principal.url | URL  
accessed_by | principal.user.email_addresses | Email addresses of the user  
accessed_by | principal.user.userid | User ID  
sr | security_result | Security result  
| metadata.product_name | Product name  
| metadata.vendor_name | Vendor name  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/saviynt-eip-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
