---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/asset-panda/
title: Collect Asset Panda logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:29:30.828867+00:00
---

# Collect Asset Panda logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/asset-panda/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Asset Panda logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Asset Panda logs to Google Security Operations using Google Cloud Storage V2.

Asset Panda is a cloud-based asset management platform that enables organizations to track, manage, and report on physical and digital assets throughout their lifecycle. The Asset Panda REST API provides access to change logs that record field-level modifications, asset transfers, action history, and user activity across all asset groups. These change logs can be collected through the API and written to a GCS bucket for ingestion by Google SecOps.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * An Asset Panda account with administrator access (required for API configuration)
  * An Asset Panda API key and secret with read permissions



## Generate Asset Panda API credentials

### Navigate to API Configuration

  1. Sign in to your **Asset Panda** account as an administrator.
  2. Click the **Settings** (gear) icon in the top-right corner.
  3. Select **API Configuration**.



### Create an API key

  1. On the **API Configuration** page, click **Create New API Key**.
  2. Provide the following configuration details:

     * **Name** : Enter a descriptive name for the key (for example, `SIEM Change Log Collector`)
     * **Permissions** : Select **Read**
**Note:** For security, grant only read permissions. Write and delete permissions are not required for log collection.
  3. Click **Save**.

  4. Record the following credentials displayed at the bottom of the page:

     * **API Key** (also called Client ID)
     * **API Secret** (also called Client Secret)
**Note:** The API secret is displayed only once. Store both values securely. If you lose the secret, you must generate a new API key.



### Identify group IDs

The Cloud Run function needs group IDs to query objects and their change logs. To find your group IDs:

  1. In **Asset Panda** , go to **Settings > Group Settings**.
  2. Click the **Edit** link next to a group name.
  3. Note the numeric value near the end of the browser URL. This is the group ID (for example, `12345`).
  4. Repeat for each group whose change logs you want to collect.



### Test API access

  * Test your credentials before proceeding with the integration:
        
        API_KEY="your-api-key"
        API_SECRET="your-api-secret"
        
        # Test authentication by retrieving account settings
        curl -s "https://api.assetpanda.com/v3/settings" \
          -H "Accept: application/json" \
          -H "Access-Key-Id: ${API_KEY}" \
          -H "Access-Key-Secret: ${API_SECRET}"
        

**Note:** Asset Panda enforces a rate limit of 400 API calls per 3-minute window per IP address. The Cloud Run function handles this with built-in rate limiting.



## Create a Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `asset-panda-change-logs`)  
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
     * **Service account name** : Enter `asset-panda-logs-collector-sa`
     * **Service account description** : Enter `Service account for Cloud Run function to collect Asset Panda change logs`
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
     * **Add principals** : Enter the service account email (for example, `asset-panda-logs-collector-sa@PROJECT_ID.iam.gserviceaccount.com`)
     * **Assign roles** : Select **Storage Object Admin**
  6. Click **Save**.



## Create a Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `asset-panda-logs-trigger`
     * Leave other settings as default
  4. Click **Create**.



## Create a Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch change logs from the Asset Panda REST API and write them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `asset-panda-logs-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose the topic `asset-panda-logs-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select the service account `asset-panda-logs-collector-sa`
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `asset-panda-change-logs` | GCS bucket name  
`GCS_PREFIX` | `asset-panda` | Prefix for log files  
`STATE_KEY` | `asset-panda/state.json` | State file path  
`AP_API_KEY` | `your-api-key` | Asset Panda API key  
`AP_API_SECRET` | `your-api-secret` | Asset Panda API secret  
`AP_GROUP_IDS` | `12345,67890` | Comma-separated group IDs to monitor  
`PAGE_SIZE` | `50` | Records per API page (max 50)  
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
           GCS_PREFIX = os.environ.get('GCS_PREFIX', 'asset-panda').strip('/')
           STATE_KEY = os.environ.get('STATE_KEY') or f"{GCS_PREFIX}/state.json"
           AP_API_KEY = os.environ.get('AP_API_KEY')
           AP_API_SECRET = os.environ.get('AP_API_SECRET')
           AP_GROUP_IDS = os.environ.get('AP_GROUP_IDS', '')
           PAGE_SIZE = int(os.environ.get('PAGE_SIZE', '50'))
           MAX_RECORDS = int(os.environ.get('MAX_RECORDS', '10000'))
           LOOKBACK_HOURS = int(os.environ.get('LOOKBACK_HOURS', '2'))
           
           BASE_URL = 'https://api.assetpanda.com'
           
           # Rate limiting: 400 calls per 3 minutes
           RATE_LIMIT_CALLS = 400
           RATE_LIMIT_WINDOW = 180  # seconds
           call_timestamps = []
           
           def rate_limit_wait():
             """Enforce rate limiting of 400 calls per 3-minute window."""
             global call_timestamps
             now = time.time()
             call_timestamps = [t for t in call_timestamps if now - t < RATE_LIMIT_WINDOW]
             if len(call_timestamps) >= RATE_LIMIT_CALLS:
               sleep_time = RATE_LIMIT_WINDOW - (now - call_timestamps[0]) + 1
               print(f"Rate limit approaching. Sleeping {sleep_time:.1f}s...")
               time.sleep(sleep_time)
               call_timestamps = [t for t in call_timestamps if time.time() - t < RATE_LIMIT_WINDOW]
             call_timestamps.append(time.time())
           
           def api_request(method, path, params=None):
             """Make an authenticated request to the Asset Panda API."""
             rate_limit_wait()
           
             url = f"{BASE_URL}{path}"
             headers = {
               'Accept': 'application/json',
               'Content-Type': 'application/json',
               'Access-Key-Id': AP_API_KEY,
               'Access-Key-Secret': AP_API_SECRET,
             }
           
             backoff = 1.0
             for attempt in range(3):
               try:
                 if method == 'GET':
                   response = http.request(method, url, headers=headers, fields=params)
                 else:
                   body = json.dumps(params or {}).encode('utf-8')
                   response = http.request(method, url, headers=headers, body=body)
           
                 if response.status == 429:
                   retry_after = int(response.headers.get('Retry-After', str(int(backoff))))
                   print(f"Rate limited (429). Retrying after {retry_after}s...")
                   time.sleep(retry_after)
                   backoff = min(backoff * 2, 60.0)
                   continue
           
                 if response.status == 200:
                   return json.loads(response.data.decode('utf-8'))
           
                 print(f"HTTP {response.status}: {response.data.decode('utf-8')[:500]}")
                 return None
           
               except Exception as e:
                 print(f"Request error (attempt {attempt + 1}): {e}")
                 if attempt < 2:
                   time.sleep(backoff)
                   backoff *= 2
           
             return None
           
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
             Asset Panda change logs and write to GCS.
           
             Args:
               cloud_event: CloudEvent object containing Pub/Sub message
             """
             if not all([GCS_BUCKET, AP_API_KEY, AP_API_SECRET, AP_GROUP_IDS]):
               print('Error: Missing required environment variables')
               return
           
             group_ids = [gid.strip() for gid in AP_GROUP_IDS.split(',') if gid.strip()]
             if not group_ids:
               print('Error: No group IDs configured')
               return
           
             try:
               bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(GCS_BUCKET)
           
               # Load state
               state = load_state(bucket, STATE_KEY)
           
               # Determine time window
               now = datetime.now(timezone.utc)
               last_time = None
           
               if isinstance(state, dict) and [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get("last_run_time"):
                 try:
                   last_time = parse_datetime(state["last_run_time"])
                   if last_time:
                     last_time = last_time - timedelta(minutes=2)
                 except Exception as e:
                   print(f"Warning: Could not parse last_run_time: {e}")
           
               if last_time is None:
                 last_time = now - timedelta(hours=LOOKBACK_HOURS)
           
               print(f"Collecting change logs from {last_time.isoformat()} to {now.isoformat()}")
           
               all_records = []
           
               for group_id in group_ids:
                 if len(all_records) >= MAX_RECORDS:
                   print(f"Reached max_records limit ({MAX_RECORDS})")
                   break
           
                 records = fetch_group_change_logs(group_id, last_time, now)
                 all_records.extend(records)
                 print(f"Group {group_id}: collected {len(records)} change log entries")
           
               if not all_records:
                 print("No new change log records found.")
                 save_state(bucket, STATE_KEY, now.isoformat())
                 return
           
               # Write to GCS as NDJSON
               timestamp = now.strftime('%Y%m%d_%H%M%S')
               object_key = f"{GCS_PREFIX}/logs_{timestamp}.ndjson"
               blob = bucket.blob(object_key)
           
               ndjson = '\n'.join(
                 [json.dumps(record, ensure_ascii=False) for record in all_records]
               ) + '\n'
               blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(ndjson, content_type='application/x-ndjson')
           
               print(f"Wrote {len(all_records)} records to gs://{GCS_BUCKET}/{object_key}")
           
               # Update state
               save_state(bucket, STATE_KEY, now.isoformat())
               print(f"Successfully processed {len(all_records)} records")
           
             except Exception as e:
               print(f'Error processing change logs: {str(e)}')
               raise
           
           def fetch_group_change_logs(group_id, start_time, end_time):
             """
             Fetch change logs for all objects in a group.
           
             Args:
               group_id: Asset Panda group ID
               start_time: Start time for log query
               end_time: End time for log query
           
             Returns:
               List of change log records
             """
             records = []
             offset = 0
           
             # Iterate through objects in the group
             while True:
               if len(records) >= MAX_RECORDS:
                 break
           
               search_data = api_request(
                 'POST',
                 f'/v3/groups/{group_id}/search_objects',
                 {'offset': offset, 'limit': PAGE_SIZE}
               )
           
               if not search_data:
                 break
           
               objects = search_data.get('objects', [])
               if not objects:
                 break
           
               for obj in objects:
                 object_id = obj.get('id')
                 if not object_id:
                   continue
           
                 change_logs = fetch_object_change_logs(
                   object_id, group_id, start_time, end_time
                 )
                 records.extend(change_logs)
           
                 if len(records) >= MAX_RECORDS:
                   break
           
               total = search_data.get('totals', {}).get('objects', 0)
               offset += len(objects)
               if offset >= total:
                 break
           
             return records
           
           def fetch_object_change_logs(object_id, group_id, start_time, end_time):
             """
             Fetch change logs for a specific object.
           
             Args:
               object_id: Asset Panda object ID
               group_id: Asset Panda group ID
               start_time: Start time filter
               end_time: End time filter
           
             Returns:
               List of change log records with metadata
             """
             records = []
             offset = 0
           
             while True:
               data = api_request(
                 'GET',
                 f'/v3/entity_objects/{object_id}/change_logs',
                 {'limit': PAGE_SIZE, 'offset': offset}
               )
           
               if not data:
                 break
           
               logs = data.get('change_logs', data.get('data', []))
               if isinstance(logs, dict):
                 logs = [logs]
           
               if not logs:
                 break
           
               for log_entry in logs:
                 log_time = parse_datetime(
                   log_entry.get('created_at') or log_entry.get('updated_at', '')
                 )
           
                 if log_time and log_time < start_time:
                   return records
                 if log_time and log_time > end_time:
                   continue
           
                 log_entry['_group_id'] = group_id
                 log_entry['_object_id'] = object_id
                 records.append(log_entry)
           
               if len(logs) < PAGE_SIZE:
                 break
           
               offset += len(logs)
           
             return records
           
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
           
           def save_state(bucket, key, last_run_time_iso):
             """Save the last run timestamp to GCS state file."""
             try:
               state = {'last_run_time': last_run_time_iso}
               blob = bucket.blob(key)
               blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
                 json.dumps(state, indent=2),
                 content_type='application/json'
               )
               print(f"Saved state: last_run_time={last_run_time_iso}")
             except Exception as e:
               print(f"Warning: Could not save state: {e}")
           

     * Second file - **requirements.txt:**
           
           functions-framework==3.*
           google-cloud-storage==2.*
           urllib3>=2.0.0
           

  3. Click **Deploy** to save and deploy the function.

  4. Wait for deployment to complete (2-3 minutes).

**Note:** The Pub/Sub trigger configuration automatically creates the necessary subscriptions and permissions. Asset Panda enforces a rate limit of 400 calls per 3-minute window per IP address. The function includes built-in rate limiting to respect this constraint.



## Create a Cloud Scheduler job

Cloud Scheduler will publish messages to the Pub/Sub topic at regular intervals, triggering the Cloud Run function.

  1. In the **GCP Console** , go to **Cloud Scheduler**.
  2. Click **Create Job**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | `asset-panda-logs-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the topic `asset-panda-logs-trigger`  
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
  5. Click on the function name `asset-panda-logs-collector`.
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         Collecting change logs from YYYY-MM-DDTHH:MM:SS+00:00 to YYYY-MM-DDTHH:MM:SS+00:00
         Group 12345: collected X change log entries
         Wrote X records to gs://asset-panda-change-logs/asset-panda/logs_YYYYMMDD_HHMMSS.ndjson
         Successfully processed X records
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click your bucket name.

  10. Navigate to the prefix folder `asset-panda/`.

  11. Verify that a new `.ndjson` file was created with the current timestamp.




If you see errors in the logs:

  * **HTTP 401** : Check API credentials in environment variables. Verify the API key and secret are correct.
  * **HTTP 403** : Verify the API key has read permissions enabled.
  * **HTTP 429** : Rate limiting - function will automatically retry with backoff.
  * **Empty results** : Verify that the configured group IDs exist and contain objects with change history.
  * **Missing environment variables** : Check all required variables are set.



## Configure a feed in Google SecOps to ingest Asset Panda logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Asset Panda Change Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Asset Panda** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Don't use service accounts from other documentation or examples.
  9. Click **Next**.

  10. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://asset-panda-change-logs/asset-panda/
           

       * Replace: 
         * `asset-panda-change-logs`: Your GCS bucket name.
         * `asset-panda`: Optional prefix/folder path where logs are stored (leave empty for root).
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
`array_values_label` | `additional.fields` | Merged  
`data_label` | `additional.fields` | Merged  
`field_values_label` | `additional.fields` | Merged  
`low_values_label` | `additional.fields` | Merged  
`value_ids_label` | `additional.fields` | Merged  
`values_label` | `additional.fields` | Merged  
`display_with_secondary` | `intermediary.user.user_display_name` | Directly mapped  
`secondary_name` | `intermediary.user.userid` | Directly mapped  
`created_at` | `metadata.event_timestamp` | Parsed as `RFC 3339`  
`has_user` | `metadata.event_type` | Mapped: `true` → `USER_UNCATEGORIZED`  
`object_version_ids` | `metadata.product_version` | Directly mapped  
`share_url` | `metadata.url_back_to_product` | Directly mapped  
`display_name` | `principal.user.user_display_name` | Directly mapped  
`id` | `principal.user.userid` | Directly mapped  
`account_id_label` | `security_result.detection_fields` | Merged  
`change_source_label` | `security_result.detection_fields` | Merged  
`change_trigger_label` | `security_result.detection_fields` | Merged  
`created_at_label` | `security_result.detection_fields` | Merged  
`date_format_label` | `security_result.detection_fields` | Merged  
`docusign_envelope_id_label` | `security_result.detection_fields` | Merged  
`embedded_into_object_id_label` | `security_result.detection_fields` | Merged  
`entity_action_id_label` | `security_result.detection_fields` | Merged  
`entity_id_label` | `security_result.detection_fields` | Merged  
`entity_id_label1` | `security_result.detection_fields` | Merged  
`entity_key_label` | `security_result.detection_fields` | Merged  
`google_calendar_sync_label` | `security_result.detection_fields` | Merged  
`gps_coordinates_label` | `security_result.detection_fields` | Merged  
`has_audit_history_label` | `security_result.detection_fields` | Merged  
`id_label` | `security_result.detection_fields` | Merged  
`is_archived_label` | `security_result.detection_fields` | Merged  
`is_deletable_label` | `security_result.detection_fields` | Merged  
`is_editable_label` | `security_result.detection_fields` | Merged  
`is_locked_label` | `security_result.detection_fields` | Merged  
`linked_action_object_id_label` | `security_result.detection_fields` | Merged  
`modifier_id_label` | `security_result.detection_fields` | Merged  
`next_step_reservation_uid_label` | `security_result.detection_fields` | Merged  
`object_appreciation_label` | `security_result.detection_fields` | Merged  
`object_depreciation_label` | `security_result.detection_fields` | Merged  
`oid_label` | `security_result.detection_fields` | Merged  
`old_id_label` | `security_result.detection_fields` | Merged  
`parent_action_object_id_label` | `security_result.detection_fields` | Merged  
`predefined_forms_label` | `security_result.detection_fields` | Merged  
`reservation_notification_label` | `security_result.detection_fields` | Merged  
`reservation_uid_label` | `security_result.detection_fields` | Merged  
`returned_label` | `security_result.detection_fields` | Merged  
`state_label` | `security_result.detection_fields` | Merged  
`status_label` | `security_result.detection_fields` | Merged  
`updated_at_label` | `security_result.detection_fields` | Merged  
`user_id_label` | `security_result.detection_fields` | Merged  
`version_label` | `security_result.detection_fields` | Merged  
N/A | `metadata.event_type` | Constant: `USER_UNCATEGORIZED`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/asset-panda-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
