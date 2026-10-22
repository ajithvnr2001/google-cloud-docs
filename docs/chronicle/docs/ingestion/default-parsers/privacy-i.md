---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/privacy-i/
title: Collect Privacy-i logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:10:39.006715+00:00
---

# Collect Privacy-i logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/privacy-i/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Privacy-i logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Privacy-i logs to Google Security Operations using Google Cloud Storage V2.

Privacy-i is an endpoint data privacy and compliance monitoring platform developed by Somansa (now acquired by Mitsui Bussan Secure Directions). The platform provides sensitive data discovery, classification, and policy enforcement across endpoints. The Privacy-i REST API provides programmatic access to inspection logs, incident reports, and agent activity data.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * Administrative access to the Privacy-i management console
  * API credentials (API key or OAuth2 credentials) for the Privacy-i REST API



## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `privacy-i-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Collect Privacy-i API credentials

### Obtain API key

  1. Sign in to the **Privacy-i management console** with administrator credentials.
  2. Go to **Settings > API Management** (or **System > API Configuration**).
  3. Click **Generate API Key**.
  4. Enter a name for the API key (for example, `Google SecOps Integration`).
  5. Copy and save the following details in a secure location:

     * **API Key** : The generated API key value
     * **Server URL** : The Privacy-i management server URL (for example, `https://privacy-i.your-domain.com`)
**Note:** The API key is displayed only once. Store it securely. If lost, you will need to regenerate it.



### Determine API base URL

The Privacy-i API base URL is your management server URL:

Format | Example  
---|---  
Server URL | `https://privacy-i.your-domain.com/api`  
**Note:** Replace `privacy-i.your-domain.com` with your actual Privacy-i management server hostname.

### Test API access

  * Test your credentials before proceeding with the integration:
        
        # Replace with your actual credentials
        PRIVACY_I_API_KEY="your-api-key"
        PRIVACY_I_BASE_URL="https://privacy-i.your-domain.com/api"
        
        # Test API access - list recent events
        curl -s -X GET "${PRIVACY_I_BASE_URL}/v1/events?limit=1" \
          -H "Authorization: Bearer ${PRIVACY_I_API_KEY}" \
          -H "Accept: application/json"
        




## Create service account for Cloud Run function

The Cloud Run function needs a service account with permissions to write to GCS bucket and be invoked by Pub/Sub.

### Create service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `privacy-i-logs-collector-sa`
     * **Service account description** : Enter `Service account for Cloud Run function to collect Privacy-i logs`
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
  2. Click on your bucket name (for example, `privacy-i-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `privacy-i-logs-collector-sa@PROJECT_ID.iam.gserviceaccount.com`)
     * **Assign roles** : Select **Storage Object Admin**
  6. Click **Save**.



## Create Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `privacy-i-logs-trigger`
     * Leave other settings as default
  4. Click **Create**.



## Create Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from the Privacy-i REST API and write them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `privacy-i-logs-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose the topic `privacy-i-logs-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select the service account `privacy-i-logs-collector-sa`.
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `privacy-i-logs` | GCS bucket name  
`GCS_PREFIX` | `privacy-i` | Prefix for log files  
`STATE_KEY` | `privacy-i/state.json` | State file path  
`PRIVACY_I_API_KEY` | `your-api-key` | Privacy-i API key  
`PRIVACY_I_BASE_URL` | `https://privacy-i.your-domain.com/api` | Privacy-i API base URL  
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
           
           # Initialize HTTP client with timeouts
           http = urllib3.PoolManager(
             timeout=urllib3.Timeout(connect=5.0, read=30.0),
             retries=False,
           )
           
           # Initialize Storage client
           storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
           
           # Environment variables
           GCS_BUCKET = os.environ.get('GCS_BUCKET')
           GCS_PREFIX = os.environ.get('GCS_PREFIX', 'privacy-i')
           STATE_KEY = os.environ.get('STATE_KEY', 'privacy-i/state.json')
           PRIVACY_I_API_KEY = os.environ.get('PRIVACY_I_API_KEY')
           PRIVACY_I_BASE_URL = os.environ.get('PRIVACY_I_BASE_URL')
           MAX_RECORDS = int(os.environ.get('MAX_RECORDS', '5000'))
           PAGE_SIZE = int(os.environ.get('PAGE_SIZE', '1000'))
           LOOKBACK_HOURS = int(os.environ.get('LOOKBACK_HOURS', '24'))
           
           def parse_datetime(value: str) -> datetime:
             """Parse ISO datetime string to datetime object."""
             if [value](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.ObjectCustomContextPayload.html#google_cloud_storage_blob_ObjectCustomContextPayload_value).endswith("Z"):
               value = value[:-1] + "+00:00"
             return datetime.fromisoformat(value)
           
           @functions_framework.cloud_event
           def main(cloud_event):
             """
             Cloud Run function triggered by Pub/Sub to fetch Privacy-i
             inspection and incident logs and write to GCS.
           
             Args:
               cloud_event: CloudEvent object containing Pub/Sub message
             """
           
             if not all([GCS_BUCKET, PRIVACY_I_API_KEY, PRIVACY_I_BASE_URL]):
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
           
               # Fetch logs from multiple endpoints
               all_records = []
               newest_event_time = None
           
               for endpoint_type in ['events', 'incidents']:
                 records, newest_time = fetch_logs(
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
           
           def fetch_logs(endpoint_type: str, start_time: datetime, end_time: datetime, page_size: int, max_records: int):
             """
             Fetch logs from Privacy-i REST API
             with offset-based pagination and rate limiting.
           
             Args:
               endpoint_type: API endpoint type (events, incidents)
               start_time: Start time for log query
               end_time: End time for log query
               page_size: Number of records per page
               max_records: Maximum total records to fetch
           
             Returns:
               Tuple of (records list, newest_event_time ISO string)
             """
             api_base = PRIVACY_I_BASE_URL.rstrip('/')
             endpoint = f"{api_base}/v1/{endpoint_type}"
           
             headers = {
               'Authorization': f'Bearer {PRIVACY_I_API_KEY}',
               'Accept': 'application/json',
               'User-Agent': 'GoogleSecOps-PrivacyICollector/1.0'
             }
           
             records = []
             newest_time = None
             page_num = 0
             offset = 0
             backoff = 1.0
           
             start_iso = start_time.strftime('%Y-%m-%dT%H:%M:%SZ')
             end_iso = end_time.strftime('%Y-%m-%dT%H:%M:%SZ')
           
             while True:
               page_num += 1
           
               if len(records) >= max_records:
                 print(f"Reached max_records limit ({max_records}) for {endpoint_type}")
                 break
           
               url = f"{endpoint}?startDate={start_iso}&endDate={end_iso}&limit={min(page_size, max_records - len(records))}&offset={offset}"
           
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
           
                 page_results = data.get('data', data.get('results', data.get('items', [])))
           
                 if not page_results:
                   print(f"No more results (empty page) for {endpoint_type}")
                   break
           
                 print(f"{endpoint_type} page {page_num}: Retrieved {len(page_results)} events")
           
                 # Add endpoint type for identification
                 for event in page_results:
                   event['_privacy_i_log_type'] = endpoint_type
           
                 records.extend(page_results)
           
                 # Track newest event time
                 for event in page_results:
                   try:
                     event_ts = event.get('timestamp') or event.get('eventTime') or event.get('createdAt')
                     if event_ts:
                       event_time = str(event_ts)
                       if newest_time is None or parse_datetime(event_time) > parse_datetime(newest_time):
                         newest_time = event_time
                   except Exception as e:
                     print(f"Warning: Could not parse event time: {e}")
           
                 # Check for more results
                 total = data.get('total', data.get('totalCount', 0))
                 if total and (offset + len(page_results)) >= total:
                   print(f"No more pages for {endpoint_type} (reached total)")
                   break
           
                 if len(page_results) < page_size:
                   print(f"No more pages for {endpoint_type} (last page not full)")
                   break
           
                 offset += len(page_results)
           
               except Exception as e:
                 print(f"Error fetching {endpoint_type} logs: {e}")
                 return records, newest_time
           
             print(f"Retrieved {len(records)} total {endpoint_type} records from {page_num} pages")
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
**Name** | `privacy-i-logs-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the topic `privacy-i-logs-trigger`  
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
  5. Click on `privacy-i-logs-collector`.
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         Fetching logs from YYYY-MM-DDTHH:MM:SS+00:00 to YYYY-MM-DDTHH:MM:SS+00:00
         events page 1: Retrieved X events
         incidents page 1: Retrieved X events
         Wrote X records to gs://privacy-i-logs/privacy-i/logs_YYYYMMDD_HHMMSS.ndjson
         Successfully processed X records
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click on your bucket name (`privacy-i-logs`).

  10. Navigate to the `privacy-i/` folder.

  11. Verify that a new `.ndjson` file was created with the current timestamp.




If you see errors in the logs:

  * **HTTP 401** : Check API key in environment variables
  * **HTTP 403** : Verify API key has required permissions in Privacy-i management console
  * **HTTP 429** : Rate limiting - function will automatically retry with backoff
  * **Missing environment variables** : Check all required variables are set



## Configure a feed in Google SecOps to ingest Privacy-i logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Privacy-i Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Privacy-i** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address.

**Note:** Each Google SecOps instance has a unique service account. Do not use service accounts from other documentation or examples.
  9. Click **Next**.

  10. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://privacy-i-logs/privacy-i/
           

       * Replace: 
         * `privacy-i-logs`: Your GCS bucket name.
         * `privacy-i`: Optional prefix/folder path where logs are stored (leave empty for root).
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

  * The Google SecOps service account needs **Storage Object Viewer** role on your GCS bucket.


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
has_principal, has_target_file, has_user | metadata.event_type | Set to SCAN_FILE if has_principal and has_target_file, else USER_UNCATEGORIZED if has_user, else STATUS_UPDATE if has_principal, else GENERIC_EVENT  
elog_incidentlogguid, efile_incidentlogguid, guid | metadata.product_log_id | Value from elog_incidentlogguid if not empty, else efile_incidentlogguid if not empty, else guid  
datatype | metadata.product_event_type | Value copied directly  
productversion | metadata.product_version | Value copied directly  
| metadata.product_name | Set to "PRIVACY_I"  
| metadata.vendor_name | Set to "PRIVACY_I"  
dfile_agentip, ip | principal.asset.ip | Merged from dfile_agentip if not empty, then ip if not empty  
dfile_agentip, ip | principal.ip | Merged from dfile_agentip if not empty, then ip if not empty  
dfile_computername | principal.asset.asset_id | Concatenated as "Computer:%{dfile_computername}"  
computername | principal.asset.hostname | Concatenated as "Computer:%{computername}"  
osserial_label, computerguid_label | principal.asset.attribute.labels | Merged from osserial_label and computerguid_label  
productid | principal.asset.product_object_id | Value copied directly  
dlog_ostype, osname | principal.platform | Set based on dlog_ostype enum (0=WINDOWS,1=LINUX,2=MAC), then overwritten based on osname regex  
macaddr | principal.mac | Merged from macaddr  
dfile_userid, userid, admin_id | principal.user.userid | Set to dfile_userid, then overwritten by userid if not empty, then by admin_id if not empty  
dfile_username, empname, admin_name | principal.user.user_display_name | Set to dfile_username, then overwritten by empname if not empty, then by admin_name if not empty  
dfile_deptname | principal.user.department | Value copied directly  
logintime | principal.user.last_login_time | Converted using date format yyyy-MM-dd HH:mm:ss  
job | principal.user.title | Value copied directly  
dfile_patterninfo | security_result | Extracted from JSON and structured into detection fields  
category | security_result.category_details | Value copied directly  
logtype | security_result.action | Value copied directly  
elog_detectedapplicationname | target.application | Value copied directly  
dfile_filecreatedtime | target.file.create_time | Converted using date format ISO8601  
dfile_fileextension | target.file.mime_type | Value copied directly  
dfile_filename | target.file.names | Merged from dfile_filename  
dfile_filesize | target.file.size | Converted to integer  
dfile_firstscannedpath | target.file.full_path | Value copied directly  
dfile_firstscannedtime | target.file.first_seen_time | Converted using date format ISO8601  
dfile_filemodifiedtime | target.file.last_modification_time | Converted using date format ISO8601  
efile_fileaccessedtime | target.file.last_access_time | Converted using date format yyyy-MM-dd HH:mm:ss  
efile_resulttime | target.file.last_analysis_time | Converted using date format ISO8601  
efile_patternguid_label, dfile_dataformatname_label, dfile_filerelationguid_label, dfile_inspectcount_label, dfile_inspectendtime_label, dfile_inspectstarttime_label, dfile_inspectfilecount_label, dfile_inspectpropertycount_label, dfile_inspectpropertyfilecount_label, dfile_inspectlogtime_label, dfile_filetype_label, dlog_inspectinfo_label, dlog_inspectexaminationtype_label, dlog_inspecttype_label, dfile_encryptfiletype_label, dfile_scanlogtype_label, dfile_policyname_label, elog_mediaguid_label, elog_mediaid_label, loggroup_label, agent_id_label, logouttime_label, packageinstalledtime_label, registeredtime_label, detail_label | additional.fields | Merged from multiple label fields  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/privacy-i-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
