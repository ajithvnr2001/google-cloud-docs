---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/workday-user-activity/
title: Collect Workday User Activity logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:18:12.475806+00:00
---

# Collect Workday User Activity logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/workday-user-activity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Workday User Activity logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Workday User Activity logs to Google Security Operations using Cloud Storage V2.

Workday is a cloud-based human capital management (HCM) and finance platform that generates user activity, authentication, and security audit logs. The User Activity Logging REST API provides programmatic access to these logs.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A Google Cloud project with {storage_api} enabled
  * Permissions to create and manage Cloud Storage buckets
  * Permissions to manage Identity and Access Management (IAM) policies on Cloud Storage buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * Privileged access to Workday with Security Administrator or equivalent permissions
  * User Activity Logging enabled in your Workday tenant



## Create a Cloud Storage bucket

  1. Go to the [Google Cloud console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `workday-activity-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Collect Workday API credentials

### Enable user activity logging

  1. Sign in to your Workday tenant as a Security Administrator.
  2. In the Workday search bar, search for and open the **Edit Tenant Setup - System** task.
  3. In the **Security** section, select the **Enable User Activity Logging** checkbox.
  4. Click **OK** to save the changes.

**Note:** Once enabled, Workday records all user activity in a secure tenant database. Activity logging must be enabled before any logs are available for export.

### Create an Integration System User (ISU)

  1. In the Workday search bar, search for **Create Integration System User**.
  2. Enter a **User Name** (for example, `ISU_SIEM_Export`) and a strong **Password**.
  3. Clear the **Require New Password at Next Sign In** checkbox.
  4. Click **OK**.
  5. Search for **Create Security Group** and create an **Integration System Security Group (Unconstrained)**.
  6. Add the ISU (`ISU_SIEM_Export`) to this security group.
  7. Search for **View Domain** and locate the **User Activity Logging** domain. Grant **Get** access to the ISU security group for this domain.
  8. Search for **Activate Pending Security Policy Changes** and activate the changes.



### Register an API client for OAuth

  1. In the Workday search bar, search for **Register API Client for Integrations**.
  2. Enter a **Client Name** (for example, `SIEM_OAuth_Client`).
  3. Select the **Non-Expiring Refresh Tokens** option.
  4. Add the scope: **System** (or the scope required for User Activity Logging API).
  5. Click **OK**.
  6. Copy and save the following details in a secure location: 
     * **Client ID** : The API client identifier.
     * **Client Secret** : The API client secret.
  7. Search for **Manage Refresh Tokens for Integrations**.
  8. Select the ISU account (`ISU_SIEM_Export`).
  9. Generate a new refresh token for the API client.
  10. Copy and save the **Refresh Token**.



### Determine the tenant URL

The API endpoint is based on your Workday tenant. The format is:

Component | Value  
---|---  
**Token endpoint** | `https://HOST/ccx/oauth2/TENANT/token`  
**Activity Logging API** | `https://HOST/ccx/api/privacy/v1/TENANT/activityLogging`  
**Note:** Replace `HOST` with your Workday hostname and `TENANT` with your tenant name.

### Verify permissions

To verify the ISU has the required permissions:

  1. Sign in to Workday as a Security Administrator.
  2. Search for **View Integration System User** and select the ISU (`ISU_SIEM_Export`).
  3. Verify the user is a member of the security group with **Get** access to the **User Activity Logging** domain.
  4. If access is missing, update the security group and activate pending security policy changes.



### Test API access

  * Test your credentials before proceeding with the integration:
        
        ```bash
        # Replace with your actual credentials
        CLIENT_ID="your-client-id"
        CLIENT_SECRET="your-client-secret"
        REFRESH_TOKEN="your-refresh-token"
        HOST="your-workday-host"
        TENANT="your-tenant"
        
        # Get OAuth access token
        TOKEN=$(curl -s -X POST "https://${HOST}/ccx/oauth2/${TENANT}/token" \
            -H "Content-Type: application/x-www-form-urlencoded" \
            -d "grant_type=refresh_token&client_id=${CLIENT_ID}&client_secret=${CLIENT_SECRET}&refresh_token=${REFRESH_TOKEN}" \
            | jq -r '.access_token')
        
        # Test API access
        curl -v -H "Authorization: Bearer ${TOKEN}" \
            "https://${HOST}/ccx/api/privacy/v1/${TENANT}/activityLogging?from=2024-01-01T00:00:00Z&to=2024-01-01T01:00:00Z"
        ```
        




## Create a service account for the Cloud Run function

The Cloud Run function needs a service account with permissions to write to a Cloud Storage bucket and be invoked by Pub/Sub.

### Create the service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `workday-activity-collector-sa`.
     * **Service account description** : Enter `Service account for Cloud Run function to collect Workday User Activity logs`.
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

  * **Storage Object Admin** : Write logs to Cloud Storage bucket and manage state files
  * **Cloud Run Invoker** : Allow Pub/Sub to invoke the function
  * **Cloud Functions Invoker** : Allow function invocation



### Grant IAM permissions on the Cloud Storage bucket

Grant the service account write permissions on the Cloud Storage bucket as follows:

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name (for example, `workday-activity-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `workday-activity-collector-sa@your-project.iam.gserviceaccount.com`).
     * **Assign roles** : Select **Storage Object Admin**.
  6. Click **Save**.



## Create a Pub/Sub topic

Create the Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `workday-activity-trigger`.
     * Leave other settings as default.
  4. Click **Create**.



## Create a Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from Workday User Activity Logging API and write them to Cloud Storage.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Write a function**.
  3. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `workday-activity-collector`  
**Region** | Select region matching your Cloud Storage bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  4. In the **Trigger** section, click **Add trigger** and select **Pub/Sub trigger**.

  5. In the **Eventarc trigger** pane, provide the following configuration details:

     * **Trigger name** : Keep the generated name or enter a name for the trigger.
     * **Trigger type** : Select **Google Sources**.
     * **Event provider** : Select **Pub/Sub**.
     * **Event type** : Select **google.cloud.pubsub.topic.v1.messagePublished**.
     * **Select a Cloud Pub/Sub topic** : Choose the topic `workday-activity-trigger`.
     * **Region** : Select the same region as the function.
     * **Service account** : Select the service account `workday-activity-collector-sa`.
  6. Click **Save trigger**.

**Note:** The trigger options come from Eventarc. If **Pub/Sub trigger** is not listed, enable the **Eventarc API** for the project and reload the page. If the pane reports that the service account is missing the **Eventarc Event Receiver** or **Cloud Run Invoker** role, click **Grant**.
  7. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Select **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  8. Navigate to and expand **Containers, Networking, Security**.

  9. Go to the **Security** tab:

     * **Service account** : Select the service account `workday-activity-collector-sa`.
  10. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `workday-activity-logs` | Cloud Storage bucket name  
`GCS_PREFIX` | `workday` | Prefix for log files  
`STATE_KEY` | `workday-state.json` | State path, outside the log prefix  
`WORKDAY_HOST` | `your-workday-host` | Workday hostname  
`WORKDAY_TENANT` | `your-tenant` | Workday tenant name  
`CLIENT_ID` | `your-client-id` | OAuth client ID  
`CLIENT_SECRET` | `your-client-secret` | OAuth client secret  
`REFRESH_TOKEN` | `your-refresh-token` | OAuth refresh token  
`MAX_RECORDS` | `10000` | Max records per run  
`PAGE_SIZE` | `100` | Records per page  
`LOOKBACK_HOURS` | `24` | Initial lookback period  
**Note:** `STATE_KEY` points outside the log prefix on purpose. The feed ingests every object under its bucket URI and, when a deletion option is selected, deletes what it transferred. Keeping the state file out of that prefix stops it from being ingested as log data and from being deleted, which would reset collection and re-ingest duplicate events.
  11. In the **Variables & Secrets** tab go to **Requests** :

     * **Request timeout** : Enter `600` seconds (10 minutes).
  12. Go to the **Settings** tab in **Containers** :

     * In the **Resources** section: 
       * **Memory** : Select **512 MiB** or higher.
       * **CPU** : Select **1**.
  13. In the **Revision scaling** section:

     * **Minimum number of instances** : Enter `0`.
     * **Maximum number of instances** : Enter `100` (or adjust based on expected load).
  14. Click **Create**.

  15. Wait for the service to be created (1-2 minutes).

  16. After the service is created, the **inline code editor** will open automatically.




### Add the function code

  1. Enter **main** in **Function entry point**.
  2. In the inline code editor, create two files:

     * First file - **main.py:**
           
           import functions_framework
           from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
           import json
           import os
           import urllib3
           from datetime import datetime, timezone, timedelta
           import time
           import hashlib
           
           # Initialize HTTP client with timeouts
           http = urllib3.PoolManager(
               timeout=urllib3.Timeout(connect=5.0, read=30.0),
               retries=False,
           )
           
           # Initialize Storage client
           storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
           
           # Environment variables
           GCS_BUCKET = os.environ.get('GCS_BUCKET')
           GCS_PREFIX = os.environ.get('GCS_PREFIX', 'workday')
           STATE_KEY = os.environ.get('STATE_KEY', 'workday-state.json')
           WORKDAY_HOST = os.environ.get('WORKDAY_HOST', '')
           WORKDAY_TENANT = os.environ.get('WORKDAY_TENANT', '')
           CLIENT_ID = os.environ.get('CLIENT_ID', '')
           CLIENT_SECRET = os.environ.get('CLIENT_SECRET', '')
           REFRESH_TOKEN = os.environ.get('REFRESH_TOKEN', '')
           MAX_RECORDS = int(os.environ.get('MAX_RECORDS', '10000'))
           PAGE_SIZE = int(os.environ.get('PAGE_SIZE', '100'))
           LOOKBACK_HOURS = int(os.environ.get('LOOKBACK_HOURS', '24'))
           
           def parse_datetime(value: str) -> datetime:
               """Parse ISO datetime string to datetime object."""
               if [value](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.ObjectCustomContextPayload.html#google_cloud_storage_blob_ObjectCustomContextPayload_value).endswith("Z"):
                   value = value[:-1] + "+00:00"
               return datetime.fromisoformat(value)
           
           # Activity Logging entries carry no per-event identifier (taskId and
           # sessionId are reused), so the content hash is the identity.
           ID_FIELDS = ()
           
           def event_keys(event):
               """Return every identity this event can be recognised by."""
               keys = {'sha256:' + hashlib.sha256(
                   json.dumps(event, sort_keys=True, ensure_ascii=False).encode('utf-8')
               ).hexdigest()}
               for field in ID_FIELDS:
                   value = event.get(field)
                   if value:
                       keys.add(f'{field}:{[value](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.ObjectCustomContextPayload.html#google_cloud_storage_blob_ObjectCustomContextPayload_value)}')
               return keys
           
           def get_token():
               """Get OAuth 2.0 access token using refresh token flow."""
               token_url = f"https://{WORKDAY_HOST}/ccx/oauth2/{WORKDAY_TENANT}/token"
           
               body = f"grant_type=refresh_token&client_id={CLIENT_ID}&client_secret={CLIENT_SECRET}&refresh_token={REFRESH_TOKEN}"
           
               headers = {
                   'Content-Type': 'application/x-www-form-urlencoded',
                   'Accept': 'application/json'
               }
           
               backoff = 1.0
               max_retries = 3
           
               for attempt in range(max_retries):
                   response = http.request('POST', token_url, body=body.encode('utf-8'), headers=headers)
           
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
           
               raise RuntimeError(f"Failed to get token after {max_retries} retries due to rate limiting")
           
           @functions_framework.cloud_event
           def main(cloud_event):
               """
               Cloud Run function triggered by Pub/Sub to fetch Workday User Activity logs and write to GCS.
           
               Args:
                   cloud_event: CloudEvent object containing Pub/Sub message
               """
           
               if not all([GCS_BUCKET, WORKDAY_HOST, WORKDAY_TENANT, CLIENT_ID, CLIENT_SECRET, REFRESH_TOKEN]):
                   print('Error: Missing required environment variables')
                   return
           
               try:
                   bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(GCS_BUCKET)
           
                   # Load state
                   state = load_state(bucket, STATE_KEY)
                   seen_keys = load_seen(bucket, STATE_KEY)
           
                   # Determine time window
                   now = datetime.now(timezone.utc)
                   last_time = None
           
                   if isinstance(state, dict) and [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get("last_event_time"):
                       try:
                           last_time = parse_datetime(state["last_event_time"])
                           last_time = last_time - timedelta(minutes=2)
                       except Exception as e:
                           print(f"Warning: Could not parse last_event_time: {e}")
           
                   if last_time is None:
                       last_time = now - timedelta(hours=LOOKBACK_HOURS)
           
                   print(f"Fetching logs from {last_time.isoformat()} to {now.isoformat()}")
           
                   # Get access token
                   token = get_token()
           
                   # Fetch logs
                   records, newest_event_time = fetch_logs(
                       token=token,
                       start_time=last_time,
                       end_time=now,
                       page_size=PAGE_SIZE,
                       max_records=MAX_RECORDS,
                   )
           
                   # Drop the events the overlap window re-read from the previous run
                   fresh = [r for r in records if not (event_keys(r) & seen_keys)]
                   all_keys = set()
                   for record in records:
                       all_keys |= event_keys(record)
           
                   if not fresh:
                       print("No new log records found.")
                       return
           
                   # Write to GCS as NDJSON
                   timestamp = now.strftime('%Y%m%d_%H%M%S')
                   object_key = f"{GCS_PREFIX}/logs_{timestamp}.ndjson"
                   blob = bucket.blob(object_key)
           
                   ndjson = '\n'.join([json.dumps(record, ensure_ascii=False) for record in fresh]) + '\n'
                   blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(ndjson, content_type='application/x-ndjson')
           
                   print(f"Wrote {len(fresh)} records to gs://{GCS_BUCKET}/{object_key}")
           
                   # Remember every fetched record so the next overlap window skips it
                   save_seen(bucket, STATE_KEY, all_keys)
           
                   if newest_event_time:
                       save_state(bucket, STATE_KEY, newest_event_time)
                   else:
                       save_state(bucket, STATE_KEY, now.isoformat())
           
                   print(f"Successfully processed {len(fresh)} records")
           
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
                   raise
           
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
                   raise
           
           def load_seen(bucket, key):
               """Load the event keys written by the previous run (sidecar object)."""
               try:
                   blob = bucket.blob(key + '.seen')
                   if blob.exists():
                       return set(json.loads(blob.[download_as_text](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_download_as_text)()))
               except Exception as e:
                   print(f"Warning: Could not load seen keys: {e}")
                   raise
           
               return set()
           
           def save_seen(bucket, key, keys):
               """Save the event keys of this run to the sidecar object."""
               try:
                   blob = bucket.blob(key + '.seen')
                   blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
                       json.dumps(sorted(keys)),
                       content_type='application/json'
                   )
                   print(f"Saved {len(keys)} event keys for deduplication")
               except Exception as e:
                   print(f"Warning: Could not save seen keys: {e}")
                   raise
           
           def fetch_logs(token: str, start_time: datetime, end_time: datetime, page_size: int, max_records: int):
               """
               Fetch user activity logs from Workday Activity Logging API with pagination and rate limiting.
           
               Args:
                   token: OAuth 2.0 access token
                   start_time: Start time for log query
                   end_time: End time for log query
                   page_size: Number of records per page
                   max_records: Maximum total records to fetch
           
               Returns:
                   Tuple of (records list, newest_event_time ISO string)
               """
               base_url = f"https://{WORKDAY_HOST}/ccx/api/privacy/v1/{WORKDAY_TENANT}/activityLogging"
           
               headers = {
                   'Authorization': f'Bearer {token}',
                   'Accept': 'application/json',
                   'User-Agent': 'GoogleSecOps-WorkdayCollector/1.0'
               }
           
               records = []
               newest_time = None
               page_num = 0
               backoff = 1.0
               offset = 0
           
               from_iso = start_time.strftime('%Y-%m-%dT%H:%M:%SZ')
               to_iso = end_time.strftime('%Y-%m-%dT%H:%M:%SZ')
           
               while True:
                   page_num += 1
           
                   if len(records) >= max_records:
                       print(f"Reached max_records limit ({max_records})")
                       break
           
                   current_limit = min(page_size, max_records - len(records))
                   url = f"{base_url}?from={from_iso}&to={to_iso}&limit={current_limit}&offset={offset}"
           
                   try:
                       response = http.request('GET', url, headers=headers)
           
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
                               event_time = event.get('requestTime') or event.get('systemAccount', {}).get('signOnDateTime')
                               if event_time:
                                   if newest_time is None or parse_datetime(event_time) > parse_datetime(newest_time):
                                       newest_time = event_time
                           except Exception as e:
                               print(f"Warning: Could not parse event time: {e}")
           
                       # Check pagination
                       total = data.get('total', 0)
                       if offset + len(page_results) >= total:
                           print(f"Reached end of results (offset={offset + len(page_results)}, total={total})")
                           break
           
                       offset += len(page_results)
           
                   except Exception as e:
                       print(f"Error fetching logs: {e}")
                       return [], None
           
               print(f"Retrieved {len(records)} total records from {page_num} pages")
               return records, newest_time
           

**Note:** This script is provided as an example and is not officially supported. We welcome feedback about how we can improve it. To submit feedback, click **Send Feedback > Google SecOps Security Product Feedback** on this page.

     * Second file: **requirements.txt:**
           
           functions-framework==3.*
           google-cloud-storage==2.*
           urllib3>=2.0.0
           

  3. Click **Deploy** to save and deploy the function.

  4. Wait for deployment to complete (2-3 minutes).

**Note:** The Pub/Sub trigger configuration automatically creates the necessary subscriptions and permissions.



## Create a Cloud Scheduler job

Cloud Scheduler publishes messages to the Pub/Sub topic at regular intervals, triggering the Cloud Run function.

  1. In the **GCP Console** , go to **Cloud Scheduler**.
  2. Click **Create Job**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | `workday-activity-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the topic `workday-activity-trigger`  
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

  1. In the **Cloud Scheduler** console, find your job (`workday-activity-collector-hourly`).
  2. Click **Force run** to trigger manually.
  3. Wait a few seconds and go to **Cloud Run > Services > workday-activity-collector > Logs**.
  4. Verify the function executed successfully. Look for:
         
         Fetching logs from YYYY-MM-DDTHH:MM:SS+00:00 to YYYY-MM-DDTHH:MM:SS+00:00
         Page 1: Retrieved X events
         Wrote X records to gs://workday-activity-logs/workday/logs_YYYYMMDD_HHMMSS.ndjson
         Successfully processed X records
         

  5. Check the Cloud Storage bucket (`workday-activity-logs`) to confirm logs were written.




If you see errors in the logs:

  * **HTTP 401** : Check OAuth credentials in environment variables
  * **HTTP 403** : Verify ISU has required permissions for User Activity Logging domain
  * **HTTP 429** : Rate limiting - function will automatically retry with backoff
  * **Failed to get access token** : Verify `WORKDAY_HOST`, `WORKDAY_TENANT`, `CLIENT_ID`, `CLIENT_SECRET`, and `REFRESH_TOKEN` are correct



## Configure a feed in Google SecOps to ingest Workday User Activity logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Workday User Activity Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Workday User Activity** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address. You'll use it in the next step.

**Note:** Each Google SecOps instance has a unique service account. Do not use service accounts from other documentation or examples.
  9. Click **Next**.

  10. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the Cloud Storage bucket URI with the prefix path:
           
           gs://workday-activity-logs/workday/
           

       * Replace: 
         * `workday-activity-logs`: Your Cloud Storage bucket name.
         * `workday`: Optional prefix or path where logs are stored (leave empty for root).
**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never delete files** : Never delete files from the source (recommended for testing).
       * **Delete transferred files and empty directories** : Delete files and empty directories from the source after a successful fetch completes.
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days).

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).

     * **Ingestion labels** : The label to be applied to the events from this feed.

  11. Click **Next**.

  12. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## Grant IAM permissions to the Google SecOps service account

The Google SecOps service account needs two roles on your Cloud Storage bucket: **Storage Object Viewer** to read the log objects, and a bucket-level role to read the bucket metadata.

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name (`workday-activity-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Paste the Google SecOps service account email.
     * **Assign roles** : Select both of the following: 
       * **Storage Object Viewer** : reads the log objects.
       * **Storage Legacy Bucket Reader** : reads the bucket metadata. If you selected the **Delete transferred files and empty directories** deletion option, select **Storage Legacy Bucket Writer** instead, which also grants the delete permission.
  6. Click **Save**.

**Note:** Grant both roles. **Storage Object Viewer** does not grant the bucket-level permission the feed needs, and the **Storage Legacy Bucket** roles do not grant permission to read object contents.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`Account_Locked__Disabled_or_Expired_label` | `additional.fields` | Merged  
`Authentication_Type_label` | `additional.fields` | Merged  
`Created_Moment_label` | `additional.fields` | Merged  
`Current_OMS_Version_label` | `additional.fields` | Merged  
`Device_is_Trusted_label` | `additional.fields` | Merged  
`Elapsed_Time__Minutes_label` | `additional.fields` | Merged  
`Failed_Sign_On_label` | `additional.fields` | Merged  
`Hire_Date_for_Signon_Worker_label` | `additional.fields` | Merged  
`Job_Family_for_Signon_Worker_label` | `additional.fields` | Merged  
`Operating_System_label` | `additional.fields` | Merged  
`Pay_Rate_type_label` | `additional.fields` | Merged  
`Request_Originator_label` | `additional.fields` | Merged  
`SAML_Identity_Provider_label` | `additional.fields` | Merged  
`Sign-on_Time_label` | `additional.fields` | Merged  
`Signoff_Time_label` | `additional.fields` | Merged  
`Signon_Day_of_the_Week_label` | `additional.fields` | Merged  
`Signon_Hour_of_Day_label` | `additional.fields` | Merged  
`Tenant_Access_Read_Only_label` | `additional.fields` | Merged  
`UI_Client_Type_label` | `additional.fields` | Merged  
`Worker_Active_for_Signon_Worker_label` | `additional.fields` | Merged  
`Worker_Type_for_Signon_Worker_label` | `additional.fields` | Merged  
`awaiting_details_label` | `additional.fields` | Merged  
`data_label` | `additional.fields` | Merged  
`evp_nme_label` | `additional.fields` | Merged  
`evpminus_label` | `additional.fields` | Merged  
`signon_ip_address_label` | `additional.fields` | Merged  
`@requestTime` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`Sign-on_Time` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ssZZ`  
`event_type` | `metadata.event_type` | Directly mapped  
`status_code` | `metadata.product_event_type` | Directly mapped  
`tenant` | `metadata.product_event_type` | Directly mapped  
`taskId` | `metadata.product_log_id` | Directly mapped  
`User_Agent` | `network.http.parsed_user_agent` | Renamed/mapped  
`Browser_Type` | `network.http.user_agent` | Directly mapped  
`User_Agent` | `network.http.user_agent` | Directly mapped  
`userAgent` | `network.http.user_agent` | Directly mapped  
`Session_ID` | `network.session_id` | Directly mapped  
`sessionId` | `network.session_id` | Directly mapped  
`Client_TLS_Version` | `network.tls.version` | Renamed/mapped  
`Worker` | `principal.asset.hostname` | Directly mapped  
`ip` | `principal.asset.ip` | Merged  
`ipaddress` | `principal.asset.ip` | Merged  
`Worker` | `principal.hostname` | Directly mapped  
`manager_name` | `principal.hostname` | Directly mapped  
`ip` | `principal.ip` | Merged  
`ipaddress` | `principal.ip` | Merged  
`Signon_Worker_label` | `principal.user.attribute.labels` | Merged  
`Supervisory_Organization_of_Signon_Worker_label` | `principal.user.attribute.labels` | Merged  
`System_Account_label` | `principal.user.attribute.labels` | Merged  
`Workday_Account_Sign_On_label` | `principal.user.attribute.labels` | Merged  
`user_credentials_label` | `principal.user.attribute.labels` | Merged  
`User_Name` | `principal.user.email_addresses` | Merged  
`Role` | `principal.user.user_display_name` | Directly mapped  
`manager_id` | `principal.user.userid` | Directly mapped  
`Active_Session_label` | `security_result.detection_fields` | Merged  
`Authentication_Failure_Message_label` | `security_result.detection_fields` | Merged  
`Forgotten_Password_Reset_Request_label` | `security_result.detection_fields` | Merged  
`Invalid_Credentials_label` | `security_result.detection_fields` | Merged  
`Is_Device_Managed_label` | `security_result.detection_fields` | Merged  
`MFA_Exempt_label` | `security_result.detection_fields` | Merged  
`Password_Changed_label` | `security_result.detection_fields` | Merged  
`Position_label` | `security_result.detection_fields` | Merged  
`taskDisplayName` | `security_result.summary` | Directly mapped  
`hostname` | `target.hostname` | Directly mapped  
`CITY_NME` | `target.location.city` | Directly mapped  
`Location` | `target.location.city` | Directly mapped  
`COUNTRY_NME` | `target.location.country_or_region` | Directly mapped  
`Location_Country_for_Signon_Worker` | `target.location.country_or_region` | Directly mapped  
`Location_State` | `target.location.state` | Directly mapped  
`STATE_NME` | `target.location.state` | Directly mapped  
`Exempt_labels` | `target.resource.attribute.labels` | Merged  
`browser_type_label` | `target.resource.attribute.labels` | Merged  
`class_of_instance_label` | `target.resource.attribute.labels` | Merged  
`device` | `target.resource.resource_subtype` | Directly mapped  
`device1` | `target.resource.resource_subtype` | Directly mapped  
`device` | `target.resource.type` | Mapped: `(?i)(Desktop/Laptop/Mobile/Phone)` → `DEVICE`  
`device1` | `target.resource.type` | Mapped: `(?i)(Desktop/Laptop/Mobile/Phone)` → `DEVICE`  
`BUSINESSGROUP_NME` | `target.user.department` | Merged  
`email_name` | `target.user.email_addresses` | Merged  
`EMPLOYEE_ID` | `target.user.employee_id` | Directly mapped  
`Employee_ID` | `target.user.employee_id` | Directly mapped  
`FIRST_NME` | `target.user.first_name` | Directly mapped  
`EMPLOYEE_TYPE` | `target.user.group_identifiers` | Merged  
`LAST_NME` | `target.user.last_name` | Directly mapped  
`JOBTITLE_NME` | `target.user.title` | Directly mapped  
`title` | `target.user.title` | Directly mapped  
`target.id` | `target.user.userid` | Directly mapped  
N/A | `metadata.product_name` | Constant: `WORKDAY_USER_ACTIVITY`  
N/A | `metadata.vendor_name` | Constant: `WORKDAY_USER_ACTIVITY`  
N/A | `target.resource.type` | Constant: `DEVICE`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/workday-user-activity-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
