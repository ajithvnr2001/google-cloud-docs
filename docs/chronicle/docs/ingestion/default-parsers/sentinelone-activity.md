---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sentinelone-activity/
title: Collect SentinelOne Activity logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:54:45.540881+00:00
---

# Collect SentinelOne Activity logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sentinelone-activity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect SentinelOne Activity logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest SentinelOne Activity logs to Google Security Operations using Google Cloud Storage V2.

SentinelOne Singularity is an autonomous endpoint protection platform that provides real-time prevention, detection, and response capabilities across endpoints, cloud workloads, and IoT devices. The Activity log captures administrative and operational events in your SentinelOne environment, including user logins, policy changes, threat management actions, agent installations, and system configuration changes. These activity logs can be exported through the SentinelOne REST API and written to a GCS bucket for ingestion by Google SecOps.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * A SentinelOne Singularity management console with API access
  * A SentinelOne service user account with Viewer role or higher



## Generate a SentinelOne API token

  1. Sign in to your **SentinelOne** management console at `https://<your-management-url>.sentinelone.net`.
  2. Go to **Settings > Users > Service Users**.
  3. Click **Actions > Create New Service User**.
  4. Provide the following configuration details: 
     * **Name** : Enter a descriptive name (for example, `SIEM Activity Log Integration`)
     * **Expiration date** : Set an expiration date or leave as default
     * **Scope level** : Select the appropriate scope (Account or Site)
     * **Role** : Select **Viewer** (minimum required for reading activity logs)
  5. Click **Create User**.
  6. A dialog displays the API token.
  7. **Copy and save** the API token securely.

**Important:** The API token is displayed only once during creation. Store it in a secure location. If you lose the token, you must create a new service user to generate a new one.

### Verify API access

  * Test your credentials before proceeding with the integration:
        
        S1_BASE_URL="https://your-management-url.sentinelone.net"
        S1_API_TOKEN="your-api-token"
        
        curl -s -X GET "${S1_BASE_URL}/web/api/v2.1/activities?limit=2" \
            -H "Authorization: ApiToken ${S1_API_TOKEN}" \
            | python3 -m json.tool
        

  * A successful response returns a JSON object with `data` array containing activity records and a `pagination` object:
        
        {
            "data": [
                {
                    "id": "123456789",
                    "activityType": 27,
                    "activityUuid": "a2c8037c-e6df-436d-b92b-bc09a418717e",
                    "createdAt": "2026-03-29T10:30:00.000000Z",
                    "primaryDescription": "User logged in",
                    "accountId": "123456",
                    "accountName": "My Account",
                    "siteId": "789012",
                    "data": {}
                }
            ],
            "pagination": {
                "nextCursor": "eyJpZCI6...",
                "totalItems": 1500
            }
        }
        




If you see these errors:

  * **HTTP 401 (Unauthorized)** : Verify the API token is correct and has not expired.
  * **HTTP 403 (Forbidden)** : Verify the service user has the appropriate scope and role.



## Create a Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `sentinelone-activity-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Create a service account for the Cloud Run function

The Cloud Run function needs a service account with permissions to write to GCS bucket and be invoked by Pub/Sub.

### Create service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `s1-activity-collector-sa`
     * **Service account description** : Enter `Service account for Cloud Run function to collect SentinelOne Activity logs`
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
     * **Add principals** : Enter the service account email (for example, `s1-activity-collector-sa@PROJECT_ID.iam.gserviceaccount.com`)
     * **Assign roles** : Select **Storage Object Admin**
  6. Click **Save**.



## Create a Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `s1-activity-trigger`
     * Leave other settings as default
  4. Click **Create**.



## Create a Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch activity logs from the SentinelOne REST API and write them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `s1-activity-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose the topic `s1-activity-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select the service account `s1-activity-collector-sa`
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `sentinelone-activity-logs` | GCS bucket name  
`GCS_PREFIX` | `sentinelone-activities` | Prefix for log files  
`STATE_KEY` | `sentinelone-activities/state.json` | State file path  
`S1_BASE_URL` | `https://your-mgmt-url.sentinelone.net` | SentinelOne management console URL  
`S1_API_TOKEN` | `your-api-token` | SentinelOne API token  
`PAGE_SIZE` | `1000` | Records per API page (max 1000)  
`MAX_RECORDS` | `50000` | Max records per run  
`LOOKBACK_HOURS` | `2` | Initial lookback period  
  10. Scroll down in the **Variables & Secrets** section to **Requests** :

     * **Request timeout** : Enter `540` seconds (9 minutes)
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
             timeout=urllib3.Timeout(connect=5.0, read=60.0),
             retries=False,
           )
           
           # Initialize Storage client
           storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
           
           # Environment variables
           GCS_BUCKET = os.environ.get('GCS_BUCKET')
           GCS_PREFIX = os.environ.get('GCS_PREFIX', 'sentinelone-activities').strip('/')
           STATE_KEY = os.environ.get('STATE_KEY') or f"{GCS_PREFIX}/state.json"
           S1_BASE_URL = os.environ.get('S1_BASE_URL', '').rstrip('/')
           S1_API_TOKEN = os.environ.get('S1_API_TOKEN')
           PAGE_SIZE = int(os.environ.get('PAGE_SIZE', '1000'))
           MAX_RECORDS = int(os.environ.get('MAX_RECORDS', '50000'))
           LOOKBACK_HOURS = int(os.environ.get('LOOKBACK_HOURS', '2'))
           
           ACTIVITIES_ENDPOINT = '/web/api/v2.1/activities'
           
           def parse_datetime(value):
             """Parse ISO datetime string to datetime object."""
             if not value:
               return None
             if [value](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.ObjectCustomContextPayload.html#google_cloud_storage_blob_ObjectCustomContextPayload_value).endswith("Z"):
               value = value[:-1] + "+00:00"
             try:
               return datetime.fromisoformat(value)
             except Exception:
               try:
                 return datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
               except Exception:
                 return None
           
           @functions_framework.cloud_event
           def main(cloud_event):
             """
             Cloud Run function triggered by Pub/Sub to fetch
             SentinelOne Activity records and write to GCS.
           
             Args:
               cloud_event: CloudEvent object containing Pub/Sub message
             """
           
             if not all([GCS_BUCKET, S1_BASE_URL, S1_API_TOKEN]):
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
           
               print(
                 f"Fetching activity logs from "
                 f"{last_time.isoformat()} to {now.isoformat()}"
               )
           
               # Fetch activity logs
               records, newest_event_time = fetch_activity_logs(
                 start_time=last_time,
                 end_time=now,
               )
           
               if not records:
                 print("No new activity records found.")
                 save_state(bucket, STATE_KEY, now.isoformat())
                 return
           
               # Write to GCS as NDJSON
               timestamp = now.strftime('%Y%m%d_%H%M%S')
               object_key = f"{GCS_PREFIX}/logs_{timestamp}.ndjson"
               blob = bucket.blob(object_key)
           
               ndjson = '\n'.join(
                 [json.dumps(record, ensure_ascii=False) for record in records]
               ) + '\n'
               blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
                 ndjson, content_type='application/x-ndjson'
               )
           
               print(
                 f"Wrote {len(records)} records to "
                 f"gs://{GCS_BUCKET}/{object_key}"
               )
           
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
             Fetch activity logs from SentinelOne REST API with
             cursor-based pagination.
           
             Args:
               start_time: Start time for log query
               end_time: End time for log query
           
             Returns:
               Tuple of (records list, newest_event_time ISO string)
             """
             url = f"{S1_BASE_URL}{ACTIVITIES_ENDPOINT}"
             headers = {
               'Authorization': f'ApiToken {S1_API_TOKEN}',
               'Content-Type': 'application/json',
             }
           
             # Format timestamps for SentinelOne API
             start_str = start_time.strftime('%Y-%m-%dT%H:%M:%S.000000Z')
           
             records = []
             newest_time = None
             cursor = None
             backoff = 1.0
           
             while True:
               if len(records) >= MAX_RECORDS:
                 print(f"Reached max_records limit ({MAX_RECORDS})")
                 break
           
               params = {
                 'createdAt__gt': start_str,
                 'limit': str(PAGE_SIZE),
                 'sortBy': 'createdAt',
                 'sortOrder': 'asc',
               }
           
               if cursor:
                 params['cursor'] = cursor
           
               try:
                 response = http.request(
                   'GET', url,
                   fields=params,
                   headers=headers
                 )
           
                 # Handle rate limiting with exponential backoff
                 if response.status == 429:
                   retry_after = int(
                     response.headers.get(
                       'Retry-After', str(int(backoff))
                     )
                   )
                   print(
                     f"Rate limited (429). "
                     f"Retrying after {retry_after}s..."
                   )
                   time.sleep(retry_after)
                   backoff = min(backoff * 2, 30.0)
                   continue
           
                 # Handle token expiry
                 if response.status == 401:
                   print(
                     "API token is invalid or expired. "
                     "Generate a new token in SentinelOne console."
                   )
                   return records, newest_time
           
                 backoff = 1.0
           
                 if response.status != 200:
                   print(f"HTTP Error: {response.status}")
                   response_text = response.data.decode('utf-8')
                   print(f"Response body: {response_text}")
                   return records, newest_time
           
                 data = json.loads(response.data.decode('utf-8'))
                 result = data.get('data', [])
                 pagination = data.get('pagination', {})
                 total_items = pagination.get('totalItems', 0)
                 next_cursor = pagination.get('nextCursor')
           
                 if not result:
                   print("No more results (empty page)")
                   break
           
                 print(
                   f"Retrieved {len(result)} events "
                   f"(total: {total_items})"
                 )
                 records.extend(result)
           
                 # Track newest event time
                 for event in result:
                   try:
                     event_time = event.get('createdAt')
                     if event_time:
                       if newest_time is None:
                         newest_time = event_time
                       else:
                         current_dt = parse_datetime(event_time)
                         newest_dt = parse_datetime(newest_time)
                         if (
                           current_dt and newest_dt
                           and current_dt > newest_dt
                         ):
                           newest_time = event_time
                   except Exception as e:
                     print(
                       f"Warning: Could not parse "
                       f"event time: {e}"
                     )
           
                 # Check pagination
                 if not next_cursor:
                   print("Reached last page")
                   break
           
                 cursor = next_cursor
           
               except Exception as e:
                 print(f"Error fetching activity logs: {e}")
                 return records, newest_time
           
             print(f"Retrieved {len(records)} total activity records")
             return records, newest_time
           

     * Second file - **requirements.txt:**
           
           functions-framework==3.*
           google-cloud-storage==2.*
           urllib3>=2.0.0
           

  3. Click **Deploy** to save and deploy the function.

  4. Wait for deployment to complete (2-3 minutes).

**Note:** The SentinelOne API uses cursor-based pagination. The `createdAt__gt` parameter filters activities created after the specified timestamp. The API returns a maximum of 1000 records per page (controlled by the `limit` parameter). The `pagination.nextCursor` value from each response is passed as the `cursor` parameter in the next request to retrieve subsequent pages.



## Create a Cloud Scheduler job

Cloud Scheduler will publish messages to the Pub/Sub topic at regular intervals, triggering the Cloud Run function.

  1. In the **GCP Console** , go to **Cloud Scheduler**.
  2. Click **Create Job**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | `s1-activity-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the topic `s1-activity-trigger`  
**Message body** | `{}` (empty JSON object)  
  4. Click **Create**.




### Schedule frequency options

Choose frequency based on log volume and latency requirements:

Frequency | Cron Expression | Use Case  
---|---|---  
Every 10 minutes | `*/10 * * * *` | High volume, near real-time  
Every hour | `0 * * * *` | Standard (recommended)  
Every 2 hours | `0 */2 * * *` | Lower volume  
**Note:** The poll interval and scheduler frequency should match. If the poll interval is greater than the scheduler time, data loss may occur. If the poll interval is less than the scheduler time, data duplication may occur. The function uses a 2-minute overlap window to prevent missed events.

### Test the integration

  1. In the **Cloud Scheduler** console, find your job.
  2. Click **Force run** to trigger the job manually.
  3. Wait a few seconds.
  4. Go to **Cloud Run > Services**.
  5. Click on the function name `s1-activity-collector`.
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         Fetching activity logs from YYYY-MM-DDTHH:MM:SS+00:00 to YYYY-MM-DDTHH:MM:SS+00:00
         Retrieved X events (total: Y)
         Wrote X records to gs://sentinelone-activity-logs/sentinelone-activities/logs_YYYYMMDD_HHMMSS.ndjson
         Successfully processed X records
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click your bucket name.

  10. Navigate to the prefix folder `sentinelone-activities/`.

  11. Verify that a new `.ndjson` file was created with the current timestamp.




If you see errors in the logs:

  * **HTTP 400** : Check the SentinelOne management console URL does not have a trailing slash. Verify query parameters are correct.
  * **HTTP 401** : The API token is invalid or expired. Generate a new token in the SentinelOne console under **Settings > Users > Service Users**.
  * **HTTP 403** : The service user does not have sufficient permissions. Verify the role and scope level.
  * **HTTP 429** : Rate limiting - the function will automatically retry with exponential backoff.
  * **Missing environment variables** : Check all required variables are set in the Cloud Run function configuration.



## Configure a feed in Google SecOps to ingest SentinelOne Activity logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `SentinelOne Activity Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Sentinelone Activity** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Don't use service accounts from other documentation or examples.
  9. Click **Next**.

  10. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://sentinelone-activity-logs/sentinelone-activities/
           

       * Replace: 
         * `sentinelone-activity-logs`: Your GCS bucket name.
         * `sentinelone-activities`: Optional prefix/folder path where logs are stored (leave empty for root).
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
`deviceNtDomain` | `about.administrative_domain` | Renamed/mapped  
`deviceExternalId` | `about.asset.asset_id` | Directly mapped  
`device_product` | `about.asset.asset_id` | Directly mapped  
`device_vendor` | `about.asset.asset_id` | Directly mapped  
`fileHash` | `about.file.full_path` | Directly mapped  
`filePath` | `about.file.full_path` | Renamed/mapped  
`_hash` | `about.file.sha256` | Renamed/mapped  
`fileHash` | `about.file.sha256` | Renamed/mapped  
`fsize` | `about.file.size` | Renamed/mapped  
`dvchost` | `about.hostname` | Renamed/mapped  
`ips` | `about.ip` | Merged  
`dvc_mac` | `about.mac` | Mapped: `slot` → `mac_address`  
`dvcmac` | `about.mac` | Merged  
`mac_address` | `about.mac` | Merged  
`deviceTranslatedAddress` | `about.nat_ip` | Merged  
`Emne` | `about.process.command_line` | Directly mapped  
`Path` | `about.process.command_line` | Directly mapped  
`Subject` | `about.process.command_line` | Directly mapped  
`deviceProcessName` | `about.process.command_line` | Renamed/mapped  
`dvcpid` | `about.process.pid` | Renamed/mapped  
`permissions` | `about.resource.attribute.permissions` | Merged  
`additional_cfp1` | `additional.fields` | Merged  
`additional_cfp2` | `additional.fields` | Merged  
`additional_cfp3` | `additional.fields` | Merged  
`additional_cfp4` | `additional.fields` | Merged  
`additional_cn1` | `additional.fields` | Merged  
`additional_cn2` | `additional.fields` | Merged  
`additional_cn3` | `additional.fields` | Merged  
`additional_cs1` | `additional.fields` | Merged  
`additional_cs2` | `additional.fields` | Merged  
`additional_cs3` | `additional.fields` | Merged  
`additional_cs4` | `additional.fields` | Merged  
`additional_cs5` | `additional.fields` | Merged  
`additional_cs6` | `additional.fields` | Merged  
`additional_cs7` | `additional.fields` | Merged  
`additional_devicePayloadId` | `additional.fields` | Merged  
`additional_eventId` | `additional.fields` | Merged  
`additional_flexString1` | `additional.fields` | Merged  
`additional_fname` | `additional.fields` | Merged  
`cs2` | `additional.fields` | Mapped: `arc_test` → `additional_cs2`  
`cs5_label` | `additional.fields` | Merged  
`source_type_label` | `additional.fields` | Merged  
`has_user` | `extensions.auth.type` | Mapped: `true` → `AUTHTYPE_UNSPECIFIED`  
`event_name` | `metadata.description` | Directly mapped  
`msg` | `metadata.description` | Renamed/mapped  
`primaryDescription` | `metadata.description` | Directly mapped  
`Generated` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ss`  
`Received` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ss`  
`createdAt` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`rt` | `metadata.event_timestamp` | Parsed as `(EEE,ddMMMyyyy,HH:mm:ss)`  
`updatedAt` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`event_name` | `metadata.event_type` | Mapped: `"LogSpyware","LogPredictiveMachineLearning"` → `SCAN_UNCATEGORIZED`  
`has_principal` | `metadata.event_type` | Mapped: `true` → `NETWORK_CONNECTION`, `true` → `STATUS_UPDATE`  
`has_user` | `metadata.event_type` | Mapped: `true` → `USER_LOGIN`  
`activityType` | `metadata.product_event_type` | Directly mapped  
`device_event_class_id` | `metadata.product_event_type` | Directly mapped  
`event_name` | `metadata.product_event_type` | Directly mapped  
`activityID` | `metadata.product_log_id` | Directly mapped  
`activityUuid` | `metadata.product_log_id` | Directly mapped  
`externalId` | `metadata.product_log_id` | Directly mapped  
`device_product` | `metadata.product_name` | Directly mapped  
`device_version` | `metadata.product_version` | Directly mapped  
`device_vendor` | `metadata.vendor_name` | Renamed/mapped  
`app_protocol_output` | `network.application_protocol` | Directly mapped  
`deviceDirection` | `network.direction` | Mapped: `0` → `INBOUND`, `1` → `OUTBOUND`  
`requestMethod` | `network.http.method` | Renamed/mapped  
`requestClientApplication` | `network.http.user_agent` | Renamed/mapped  
`ip_protocol_out` | `network.ip_protocol` | Directly mapped  
`in` | `network.received_bytes` | Renamed/mapped  
`out` | `network.sent_bytes` | Renamed/mapped  
`sntdom` | `principal.administrative_domain` | Renamed/mapped  
`sourceServiceName` | `principal.application` | Renamed/mapped  
`data.ipAddress` | `principal.asset.ip` | Merged  
`Group_name` | `principal.group.group_display_name` | Directly mapped  
`Gruppenavn` | `principal.group.group_display_name` | Directly mapped  
`Device_name` | `principal.hostname` | Directly mapped  
`Enhetsnavn` | `principal.hostname` | Directly mapped  
`shost` | `principal.hostname` | Renamed/mapped  
`data.ipAddress` | `principal.ip` | Merged  
`principal_ip` | `principal.ip` | Merged  
`shost` | `principal.ip` | Merged  
`mac` | `principal.mac` | Merged  
`sourceTranslatedAddress` | `principal.nat_ip` | Merged  
`sourceTranslatedPort` | `principal.nat_port` | Renamed/mapped  
`spt` | `principal.port` | Renamed/mapped  
`data.sourceprocesscommandline` | `principal.process.command_line` | Directly mapped  
`sproc` | `principal.process.command_line` | Renamed/mapped  
`data.sourceprocessname` | `principal.process.file.names` | Merged  
`spid` | `principal.process.pid` | Renamed/mapped  
`principal_role` | `principal.user.attribute.roles` | Merged  
`suser` | `principal.user.user_display_name` | Directly mapped  
`suid` | `principal.user.userid` | Renamed/mapped  
`sec_result` | `security_result` | Merged  
`_action` | `security_result.action` | Merged  
`act` | `security_result.action` | Mapped: `accept` → `_action`, `deny` → `_action`  
`Action_Taken` | `security_result.action_details` | Directly mapped  
`act` | `security_result.action_details` | Directly mapped  
`cat` | `security_result.category_details` | Merged  
`Scan_Type` | `security_result.description` | Directly mapped  
`Type` | `security_result.description` | Directly mapped  
`msg_data_2` | `security_result.description` | Directly mapped  
`infection_channel_label` | `security_result.detection_fields` | Merged  
`operasjon_label` | `security_result.detection_fields` | Merged  
`operation_label` | `security_result.detection_fields` | Merged  
`permission_label` | `security_result.detection_fields` | Merged  
`spyware_Grayware_Type_label` | `security_result.detection_fields` | Merged  
`threat_probability_label` | `security_result.detection_fields` | Merged  
`tillatelse_label` | `security_result.detection_fields` | Merged  
`mwProfile` | `security_result.rule_name` | Directly mapped  
`severity` | `security_result.severity` | Mapped: `"0", "1", "2", "3", "LOW"` → `LOW`, `"4", "5", "6", "MEDIUM", "SUBSTANTIAL", "INFO"...  
`Result` | `security_result.summary` | Directly mapped  
`appcategory` | `security_result.summary` | Directly mapped  
`reason` | `security_result.summary` | Renamed/mapped  
`Spyware` | `security_result.threat_name` | Directly mapped  
`Unknown_Threat` | `security_result.threat_name` | Directly mapped  
`Virus_Malware_Name` | `security_result.threat_name` | Directly mapped  
`oldFilePath` | `src.file.full_path` | Renamed/mapped  
`oldFileSize` | `src.file.size` | Renamed/mapped  
`old_permissions` | `src.resource.attribute.permissions` | Merged  
`dntdom` | `target.administrative_domain` | Renamed/mapped  
`destinationServiceName` | `target.application` | Renamed/mapped  
`agentId` | `target.asset.asset_id` | Directly mapped  
`data.computerName` | `target.asset.hostname` | Directly mapped  
`data.newGroupName` | `target.group.group_display_name` | Directly mapped  
`data.newGroupId` | `target.group.product_object_id` | Directly mapped  
`data.computerName` | `target.hostname` | Directly mapped  
`temp_dhost` | `target.hostname` | Directly mapped  
`IPv6_Address` | `target.ip` | Merged  
`dst_ip` | `target.ip` | Merged  
`ipv6` | `target.ip` | Mapped: `-` → `IPv6_Address`  
`data.siteName` | `target.location.name` | Directly mapped  
`siteName` | `target.location.name` | Directly mapped  
`mac_address` | `target.mac` | Merged  
`accountName` | `target.namespace` | Directly mapped  
`destination_translated_address` | `target.nat_ip` | Merged  
`destinationTranslatedPort` | `target.nat_port` | Renamed/mapped  
`dpt` | `target.port` | Renamed/mapped  
`dproc` | `target.process.command_line` | Renamed/mapped  
`File_name` | `target.process.file.full_path` | Directly mapped  
`Infected_Resource` | `target.process.file.full_path` | Directly mapped  
`Object` | `target.process.file.full_path` | Directly mapped  
`Objekt` | `target.process.file.full_path` | Directly mapped  
`dpid` | `target.process.pid` | Renamed/mapped  
`full_scope_details_label` | `target.resource.attribute.labels` | Merged  
`notification_scope_label` | `target.resource.attribute.labels` | Merged  
`resource_Type_label` | `target.resource.attribute.labels` | Merged  
`scope_level_label` | `target.resource.attribute.labels` | Merged  
`site_id_label` | `target.resource.attribute.labels` | Merged  
`vendor_activity_id_label` | `target.resource.attribute.labels` | Merged  
`request` | `target.url` | Directly mapped  
`target_role` | `target.user.attribute.roles` | Merged  
`CustomerName` | `target.user.user_display_name` | Directly mapped  
`data.accountName` | `target.user.user_display_name` | Directly mapped  
`temp_duser` | `target.user.user_display_name` | Directly mapped  
`Bruker` | `target.user.userid` | Directly mapped  
`User_value` | `target.user.userid` | Directly mapped  
`accountId` | `target.user.userid` | Directly mapped  
`temp_duid` | `target.user.userid` | Directly mapped  
N/A | `extensions.auth.type` | Constant: `AUTHTYPE_UNSPECIFIED`  
N/A | `metadata.event_type` | Constant: `PROCESS_UNCATEGORIZED`  
N/A | `metadata.vendor_name` | Constant: `SentinelOne`  
N/A | `network.direction` | Constant: `INBOUND`  
N/A | `security_result.severity` | Constant: `LOW`  
`createdAt` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`updatedAt` | `event.idm.read_only_udm.security_result.last_updated_time` | Mapped from changelog  
`activityUuid` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`activityID` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`primaryDescription` | `event.idm.read_only_udm.metadata.description` | Mapped from changelog  
`rt` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`activityType` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`device_product` | `event.idm.read_only_udm.metadata.product_name` | Mapped from changelog  
`data.ipAddress` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`data.ipAddress` | `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`data.sourceprocesscommandline` | `event.idm.read_only_udm.principal.process.command_line` | Mapped from changelog  
`data.sourceprocessname` | `event.idm.read_only_udm.principal.process.file.names` | Mapped from changelog  
`agentId` | `event.idm.read_only_udm.target.asset.asset_id` | Mapped from changelog  
`data.computerName` | `event.idm.read_only_udm.target.hostname` | Mapped from changelog  
`data.computerName` | `event.idm.read_only_udm.target.asset.hostname` | Mapped from changelog  
`accountName` | `event.idm.read_only_udm.target.namespace` | Mapped from changelog  
`siteName,` | `event.idm.read_only_udm.target.location.name` | Mapped from changelog  
`accountId` | `event.idm.read_only_udm.target.user.userid` | Mapped from changelog  
`data.accountName` | `event.idm.read_only_udm.target.user.user_display_name` | Mapped from changelog  
`data.newGroupId` | `event.idm.read_only_udm.target.group.product_object_id` | Mapped from changelog  
`data.newGroupName` | `event.idm.read_only_udm.target.group.group_display_name` | Mapped from changelog  
`data.sourceType` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`data.alertid` | `event.idm.read_only_udm.security_result.rule_id` | Mapped from changelog  
`data.ruledescription` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`data.oldGroupName` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`data.oldGroupId` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`data.newGroupId` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`data.newGroupName` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`data.fullScopeDetails` | `event.idm.read_only_udm.security_result.description` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sentinelone-activity-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
