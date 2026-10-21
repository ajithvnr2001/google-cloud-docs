---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/agiloft/
title: Collect Agiloft logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:29:29.464307+00:00
---

# Collect Agiloft logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/agiloft/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Agiloft logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Agiloft logs to Google Security Operations using Google Cloud Storage V2.

Agiloft is a no-code contract lifecycle management (CLM) platform that automates contract creation, approval workflows, and compliance tracking. The Agiloft Activity Log table records system usage events such as user logins, logouts, record modifications, rule changes, and administrative actions. These activity logs can be exported through the Agiloft REST API and written to a GCS bucket for ingestion by Google SecOps.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * An Agiloft instance with Advanced, Premium, or Platform edition (REST API access requires one of these editions)
  * An Agiloft user account in a REST-enabled group with access to the Activity Log table
  * Activity logging enabled in the Agiloft knowledgebase (KB)



## Configure Agiloft activity logging

  1. Sign in to your **Agiloft** KB with an administrator account.
  2. Click the **Setup** gear in the upper right corner.
  3. Go to **System > Configure Activity Log**.
  4. Click **New** to open the **Audit Rules** wizard.
  5. Provide the following configuration details: 
     * **Name** : Enter a name for the rule (for example, `All Activity for SIEM`)
     * **Language** : Select your KB language
  6. Create or select a saved search that determines which users' actions are logged.
  7. Select the events to track. For comprehensive security monitoring, select: 
     * Login
     * Logout
     * Login Failure
     * Record Create
     * Record Edit
     * Record Delete
     * File Download
     * Rule Edit
     * Workflow Edit
     * Group Edit
     * Team Edit
     * Table Edit
     * Column Edit
  8. Define the retention period for the audit records (for example, `1 year`).
  9. Click **Finish**.

**Note:** By default, Agiloft includes audit rules for system events, all logins, admin actions, and deletions. Review existing rules before creating a new one to avoid duplicates.



### Unhide the Activity Log table

  1. In the **Agiloft** KB, go to **Setup > Tables**.
  2. Select **Activity Log** from the table list.
  3. Click **Unhide** to make the Activity Log table accessible for API queries.

**Note:** The Activity Log table must be visible (unhidden) before you can query it through the REST API.



## Collect Agiloft API credentials

### Get Agiloft instance details

  1. Sign in to your **Agiloft** instance.
  2. Note the following values from the browser address bar:

     * **Hostname** : The server address (for example, `yourcompany.agiloft.com`)
     * **KB Name** : The knowledgebase name, displayed in the upper right corner of the KB next to the Help icon (for example, `Production`)
**Note:** KB names are case sensitive. Use the exact name as displayed in the Agiloft interface.



### Create a dedicated API user

  1. In the **Agiloft** KB, go to **Setup > Access > People**.
  2. Create a new user account dedicated to API access: 
     * **Login** : Enter a descriptive login (for example, `siem_api_user`)
     * **Password** : Set a strong password
  3. Add the user to a group that has REST API access enabled and read access to the **Activity Log** table.

**Note:** The API user must be a native Agiloft account. LDAP accounts are not compatible with REST API authentication.



### Verify permissions

To verify the account has the required permissions:

  1. Sign in to **Agiloft** with the API user credentials.
  2. Go to **Setup > Tables**.
  3. Verify that the **Activity Log** table is visible and accessible.
  4. If you cannot see the Activity Log table, contact your Agiloft administrator to grant the necessary group permissions.



### Test API access

  * Test your credentials before proceeding with the integration:
        
        AGILOFT_HOST="https://yourcompany.agiloft.com"
        AGILOFT_KB="YourKBName"
        AGILOFT_LOGIN="siem_api_user"
        AGILOFT_PASSWORD="your-password"
        
        # Test login and get JWT token
        TOKEN=$(curl -s "${AGILOFT_HOST}/ewws/EWLogin?$KB=${AGILOFT_KB}&\$login=${AGILOFT_LOGIN}&\$password=${AGILOFT_PASSWORD}&\$lang=en" \
          | python3 -c "import sys,json; data=json.load(sys.stdin); print(data.get('token',''))")
        
        echo "Token: ${TOKEN}"
        
        # Test Activity Log table access with JSON format
        curl -v "${AGILOFT_HOST}/ewws/EWSearch/.json?\$KB=${AGILOFT_KB}&\$table=activity_log&\$login=${AGILOFT_LOGIN}&\$password=${AGILOFT_PASSWORD}&\$lang=en&limit=1&page=0&field=id&field=action&field=description&field=login&field=date" \
          -H "Accept: application/json"
        

**Note:** The default JWT token expiration time is 15 minutes. For the Cloud Run function, the credential-based authentication method (login and password in URL parameters) is used instead to avoid token refresh complexity.



## Create a Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `agiloft-activity-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Create a service account for the Cloud Run function

The Cloud Run function needs a service account with permissions to write to GCS bucket and be invoked by Pub/Sub.

### Create the service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `agiloft-logs-collector-sa`
     * **Service account description** : Enter `Service account for Cloud Run function to collect Agiloft activity logs`
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
  2. Click your bucket name.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `agiloft-logs-collector-sa@PROJECT_ID.iam.gserviceaccount.com`)
     * **Assign roles** : Select **Storage Object Admin**
  6. Click **Save**.



## Create a Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `agiloft-logs-trigger`
     * Leave other settings as default
  4. Click **Create**.



## Create a Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch activity logs from the Agiloft REST API and write them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `agiloft-logs-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose the topic `agiloft-logs-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select the service account `agiloft-logs-collector-sa`
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `agiloft-activity-logs` | GCS bucket name  
`GCS_PREFIX` | `agiloft` | Prefix for log files  
`STATE_KEY` | `agiloft/state.json` | State file path  
`AGILOFT_HOST` | `https://yourcompany.agiloft.com` | Agiloft instance URL  
`AGILOFT_KB` | `YourKBName` | Agiloft KB name (case sensitive)  
`AGILOFT_LOGIN` | `siem_api_user` | API user login  
`AGILOFT_PASSWORD` | `your-password` | API user password  
`PAGE_SIZE` | `100` | Records per API page  
`MAX_RECORDS` | `10000` | Max records per run  
`LOOKBACK_HOURS` | `2` | Initial lookback period  
  10. Scroll down in the **Variables & Secrets** section to **Requests** :

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
           import urllib.parse
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
           GCS_PREFIX = os.environ.get('GCS_PREFIX', 'agiloft').strip('/')
           STATE_KEY = os.environ.get('STATE_KEY') or f"{GCS_PREFIX}/state.json"
           AGILOFT_HOST = os.environ.get('AGILOFT_HOST', '').rstrip('/')
           AGILOFT_KB = os.environ.get('AGILOFT_KB')
           AGILOFT_LOGIN = os.environ.get('AGILOFT_LOGIN')
           AGILOFT_PASSWORD = os.environ.get('AGILOFT_PASSWORD')
           PAGE_SIZE = int(os.environ.get('PAGE_SIZE', '100'))
           MAX_RECORDS = int(os.environ.get('MAX_RECORDS', '10000'))
           LOOKBACK_HOURS = int(os.environ.get('LOOKBACK_HOURS', '2'))
           
           ACTIVITY_LOG_FIELDS = [
             'id', 'action', 'action_duration', 'login', 'user_name',
             'user_primary_team', 'company', 'cookie', 'date',
             'description', 'groups', 'interface', 'ip',
             'record_id', 'rule_id', 'session_duration',
             'session_id', 'table_label'
           ]
           
           def parse_datetime(value):
             """Parse ISO datetime string to datetime object."""
             if not value:
               return None
             if [value](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.ObjectCustomContextPayload.html#google_cloud_storage_blob_ObjectCustomContextPayload_value).endswith("Z"):
               value = value[:-1] + "+00:00"
             try:
               return datetime.fromisoformat(value)
             except Exception:
               return None
           
           @functions_framework.cloud_event
           def main(cloud_event):
             """
             Cloud Run function triggered by Pub/Sub to fetch
             Agiloft Activity Log records and write to GCS.
           
             Args:
               cloud_event: CloudEvent object containing Pub/Sub message
             """
           
             if not all([GCS_BUCKET, AGILOFT_HOST, AGILOFT_KB, AGILOFT_LOGIN, AGILOFT_PASSWORD]):
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
                   # Overlap by 2 minutes to catch delayed events
                   if last_time:
                     last_time = last_time - timedelta(minutes=2)
                 except Exception as e:
                   print(f"Warning: Could not parse last_event_time: {e}")
           
               if last_time is None:
                 last_time = now - timedelta(hours=LOOKBACK_HOURS)
           
               print(f"Fetching activity logs from {last_time.isoformat()} to {now.isoformat()}")
           
               # Fetch activity logs
               records, newest_event_time = fetch_activity_logs(
                 start_time=last_time,
                 end_time=now,
               )
           
               if not records:
                 print("No new activity log records found.")
                 save_state(bucket, STATE_KEY, now.isoformat())
                 return
           
               # Write to GCS as NDJSON
               timestamp = now.strftime('%Y%m%d_%H%M%S')
               object_key = f"{GCS_PREFIX}/logs_{timestamp}.ndjson"
               blob = bucket.blob(object_key)
           
               ndjson = '\n'.join(
                 [json.dumps(record, ensure_ascii=False) for record in records]
               ) + '\n'
               blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(ndjson, content_type='application/x-ndjson')
           
               print(f"Wrote {len(records)} records to gs://{GCS_BUCKET}/{object_key}")
           
               # Update state
               if newest_event_time:
                 save_state(bucket, STATE_KEY, newest_event_time)
               else:
                 save_state(bucket, STATE_KEY, now.isoformat())
           
               print(f"Successfully processed {len(records)} records")
           
             except Exception as e:
               print(f'Error processing activity logs: {str(e)}')
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
           
           def save_state(bucket, key, last_event_time_iso):
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
           
           def fetch_activity_logs(start_time, end_time):
             """
             Fetch activity logs from Agiloft REST API with pagination.
           
             Args:
               start_time: Start time for log query
               end_time: End time for log query
           
             Returns:
               Tuple of (records list, newest_event_time ISO string)
             """
             base_url = f"{AGILOFT_HOST}/ewws/EWSearch/.json"
           
             # Build field parameters
             field_params = '&'.join(
               [f"field={urllib.parse.quote(f)}" for f in ACTIVITY_LOG_FIELDS]
             )
           
             # Build date filter query
             start_str = start_time.strftime('%d %m %y %H:%M:%S')
             end_str = end_time.strftime('%d %m %y %H:%M:%S')
             query_filter = urllib.parse.quote(
               f"date >= '{start_str}' AND date <= '{end_str}'"
             )
           
             records = []
             newest_time = None
             page_num = 0
             backoff = 1.0
           
             while True:
               if len(records) >= MAX_RECORDS:
                 print(f"Reached max_records limit ({MAX_RECORDS})")
                 break
           
               url = (
                 f"{base_url}"
                 f"?$KB={urllib.parse.quote(AGILOFT_KB)}"
                 f"&$table=activity_log"
                 f"&$login={urllib.parse.quote(AGILOFT_LOGIN)}"
                 f"&$password={urllib.parse.quote(AGILOFT_PASSWORD)}"
                 f"&$lang=en"
                 f"&query={query_filter}"
                 f"&limit={PAGE_SIZE}"
                 f"&page={page_num}"
                 f"&{field_params}"
               )
           
               try:
                 response = http.request('GET', url)
           
                 # Handle rate limiting with exponential backoff
                 if response.status == 429:
                   retry_after = int(
                     response.headers.get('Retry-After', str(int(backoff)))
                   )
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
           
                 if not data.get('success', False):
                   print(f"API error: {data.get('message', 'Unknown error')}")
                   return [], None
           
                 result = data.get('result', [])
           
                 # Handle single record vs list
                 if isinstance(result, dict):
                   result = [result]
           
                 if not result:
                   print(f"No more results (empty page {page_num})")
                   break
           
                 print(f"Page {page_num}: Retrieved {len(result)} events")
                 records.extend(result)
           
                 # Track newest event time
                 for event in result:
                   try:
                     event_time = event.get('date')
                     if event_time:
                       if newest_time is None:
                         newest_time = event_time
                       else:
                         current_dt = parse_datetime(event_time)
                         newest_dt = parse_datetime(newest_time)
                         if current_dt and newest_dt and current_dt > newest_dt:
                           newest_time = event_time
                   except Exception as e:
                     print(f"Warning: Could not parse event time: {e}")
           
                 # Check pagination
                 if len(result) < PAGE_SIZE:
                   print(
                     f"Reached last page (size={len(result)} < limit={PAGE_SIZE})"
                   )
                   break
           
                 page_num += 1
           
               except Exception as e:
                 print(f"Error fetching activity logs: {e}")
                 return [], None
           
             print(f"Retrieved {len(records)} total records from {page_num + 1} pages")
             return records, newest_time
           

     * Second file - **requirements.txt:**
           
           functions-framework==3.*
           google-cloud-storage==2.*
           urllib3>=2.0.0
           

  3. Click **Deploy** to save and deploy the function.

  4. Wait for deployment to complete (2-3 minutes).

**Note:** The Pub/Sub trigger configuration automatically creates the necessary subscriptions and permissions. The Agiloft REST API introduces a one-second delay between calls by default (configurable via the WSDelay global variable). The function handles this natively through sequential pagination.



## Create a Cloud Scheduler job

Cloud Scheduler will publish messages to the Pub/Sub topic at regular intervals, triggering the Cloud Run function.

  1. In the **GCP Console** , go to **Cloud Scheduler**.
  2. Click **Create Job**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | `agiloft-logs-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the topic `agiloft-logs-trigger`  
**Message body** | `{}` (empty JSON object)  
  4. Click **Create**.




### Schedule frequency options

Choose frequency based on log volume and latency requirements:

Frequency | Cron Expression | Use Case  
---|---|---  
Every hour | `0 * * * *` | Standard (recommended)  
Every 2 hours | `0 */2 * * *` | Lower volume  
Every 6 hours | `0 */6 * * *` | Low volume, batch processing  
  
### Test the integration

  1. In the **Cloud Scheduler** console, find your job.
  2. Click **Force run** to trigger the job manually.
  3. Wait a few seconds.
  4. Go to **Cloud Run > Services**.
  5. Click on the function name `agiloft-logs-collector`.
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         Fetching activity logs from YYYY-MM-DDTHH:MM:SS+00:00 to YYYY-MM-DDTHH:MM:SS+00:00
         Page 0: Retrieved X events
         Wrote X records to gs://agiloft-activity-logs/agiloft/logs_YYYYMMDD_HHMMSS.ndjson
         Successfully processed X records
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click your bucket name.

  10. Navigate to the prefix folder `agiloft/`.

  11. Verify that a new `.ndjson` file was created with the current timestamp.




If you see errors in the logs:

  * **HTTP 401** : Check API credentials in environment variables. Verify login and password are correct.
  * **HTTP 403** : Verify the API user has read access to the Activity Log table and belongs to a REST-enabled group.
  * **HTTP 429** : Rate limiting - function will automatically retry with backoff.
  * **"success": false** : Check the error message. Common causes include incorrect KB name (case sensitive) or table name.
  * **Missing environment variables** : Check all required variables are set.



## Configure a feed in Google SecOps to ingest Agiloft logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Agiloft Activity Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Agiloft** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Don't use service accounts from other documentation or examples.
  9. Click **Next**.

  10. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://agiloft-activity-logs/agiloft/
           

       * Replace: 
         * `agiloft-activity-logs`: Your GCS bucket name.
         * `agiloft`: Optional prefix/folder path where logs are stored (leave empty for root).
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
  2. Click your bucket name.
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
`_1880_full_name_label` | `additional.fields` | Merged  
`_1888_full_name_label` | `additional.fields` | Merged  
`action_duration_label` | `additional.fields` | Merged  
`cookie_label` | `additional.fields` | Merged  
`creator_login_label` | `additional.fields` | Merged  
`creator_team_label` | `additional.fields` | Merged  
`deleteable_label` | `additional.fields` | Merged  
`demo_data_label` | `additional.fields` | Merged  
`interface_label` | `additional.fields` | Merged  
`login_label` | `additional.fields` | Merged  
`record_id_label` | `additional.fields` | Merged  
`table_label_label` | `additional.fields` | Merged  
`type_label` | `additional.fields` | Merged  
`description` | `metadata.description` | Directly mapped  
`date` | `metadata.event_timestamp` | Parsed as `MMM dd yyyy HH:mm:ss`  
`date_created` | `metadata.event_timestamp` | Parsed as `MMM dd yyyy HH:mm:ss`  
`date_updated` | `metadata.event_timestamp` | Parsed as `MMM dd yyyy HH:mm:ss`  
`timestamp` | `metadata.event_timestamp` | Parsed as `dd/MMM/yyyy:HH:mm:ss Z`  
`has_principal` | `metadata.event_type` | Mapped: `true` → `STATUS_UPDATE`  
`has_principal_user` | `metadata.event_type` | Mapped: `true` → `USER_UNCATEGORIZED`  
`activity_log_id` | `metadata.product_deployment_id` | Directly mapped  
`id` | `metadata.product_log_id` | Directly mapped  
`method` | `network.http.method` | Directly mapped  
`url` | `network.http.referral_url` | Directly mapped  
`response_code` | `network.http.response_code` | Directly mapped  
`byte_transferred` | `network.received_bytes` | Directly mapped  
`session_duration` | `network.session_duration.seconds` | Directly mapped  
`client_ip` | `principal.asset.ip` | Merged  
`ip` | `principal.asset.ip` | Merged  
`client_ip` | `principal.ip` | Merged  
`ip` | `principal.ip` | Merged  
`user_primary_team_label` | `principal.user.attribute.labels` | Merged  
`company` | `principal.user.company_name` | Directly mapped  
`groups` | `principal.user.group_identifiers` | Merged  
`user_name` | `principal.user.user_display_name` | Directly mapped  
`user` | `principal.user.userid` | Directly mapped  
`user_login` | `principal.user.userid` | Directly mapped  
N/A | `metadata.event_type` | Constant: `USER_UNCATEGORIZED`  
N/A | `metadata.product_name` | Constant: `Agiloft`  
N/A | `metadata.vendor_name` | Constant: `Agiloft`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/agiloft-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
