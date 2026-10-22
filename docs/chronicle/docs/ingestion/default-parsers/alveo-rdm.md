---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/alveo-rdm/
title: Collect Alveo Risk Data Management logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:25:46.693085+00:00
---

# Collect Alveo Risk Data Management logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/alveo-rdm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Alveo Risk Data Management logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Alveo Risk Data Management (RDM) logs to Google Security Operations using Google Cloud Storage V2.

Alveo RDM, part of the Prime EDM platform by Gresham Technologies, is a cloud-based financial data management solution that helps banks, asset managers, insurers, and other financial institutions manage market data, risk factors, and reference data across multiple asset classes. The platform provides a RESTful API through its Ops360 interface for programmatic access to data operations, audit trail records, and data lineage information. These audit and operational logs can be exported through the REST API and written to a GCS bucket for ingestion by Google SecOps.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * An Alveo RDM (Prime EDM) instance with REST API access enabled
  * An Alveo user account with API credentials and permissions to access audit trail data
  * API client credentials (Client ID and Client Secret) generated from the Alveo administration console



## Collect Alveo RDM API credentials

### Get the Alveo instance details

  1. Sign in to your **Alveo RDM** (Prime EDM) instance.
  2. Note the following values from the browser address bar:

     * **Base URL** : The API server address (for example, `https://yourcompany.alveotech.com`)
     * **Tenant ID** : Your organization's tenant identifier, displayed in the administration console
**Note:** The base URL and tenant ID are specific to your Alveo deployment. Contact your Alveo administrator if these values are not available in the console.



### Create API credentials

  1. Sign in to the **Alveo RDM** administration console.
  2. Go to **Administration > API Access > Client Credentials**.
  3. Click **Create New Client**.
  4. Provide the following configuration details: 
     * **Client Name** : Enter a descriptive name (for example, `Google SecOps Integration`)
     * **Scopes** : Select **audit:read** and **data:read**
  5. Click **Create**.
  6. Copy and securely store the generated credentials:

     * **Client ID** : Copy this value
     * **Client Secret** : Copy this value
**Note:** The Client Secret is displayed only once during creation. Store it securely before closing the dialog.



### Verify permissions

To verify the account has the required permissions:

  1. Sign in to the **Alveo RDM** console with API user credentials.
  2. Go to **Administration > Audit Trail**.
  3. Verify that audit trail records are visible and accessible.
  4. If you cannot see the Audit Trail section, contact your Alveo administrator to grant the necessary permissions.



### Test API access

  * Test your credentials before proceeding with the integration:
        
        ALVEO_BASE_URL="https://yourcompany.alveotech.com"
        ALVEO_CLIENT_ID="your-client-id"
        ALVEO_CLIENT_SECRET="your-client-secret"
        
        # Get OAuth2 access token
        TOKEN=$(curl -s -X POST "${ALVEO_BASE_URL}/oauth/token" \
          -H "Content-Type: application/x-www-form-urlencoded" \
          -d "grant_type=client_credentials&client_id=${ALVEO_CLIENT_ID}&client_secret=${ALVEO_CLIENT_SECRET}" \
          | python3 -c "import sys,json; print(json.load(sys.stdin).get('access_token',''))")
        
        echo "Token: ${TOKEN}"
        
        # Test audit trail API access
        curl -v "${ALVEO_BASE_URL}/api/v1/audit/events?limit=1" \
          -H "Authorization: Bearer ${TOKEN}" \
          -H "Accept: application/json"
        

**Note:** OAuth2 access tokens have a limited lifespan (typically 3600 seconds). The Cloud Run function handles token refresh automatically before each collection run.



## Create a Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `alveo-rdm-audit-logs`)  
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
     * **Service account name** : Enter `alveo-rdm-logs-collector-sa`
     * **Service account description** : Enter `Service account for Cloud Run function to collect Alveo RDM audit logs`
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
     * **Add principals** : Enter the service account email (for example, `alveo-rdm-logs-collector-sa@PROJECT_ID.iam.gserviceaccount.com`)
     * **Assign roles** : Select **Storage Object Admin**
  6. Click **Save**.



## Create a Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `alveo-rdm-logs-trigger`
     * Leave other settings as default
  4. Click **Create**.



## Create a Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch audit trail logs from the Alveo RDM REST API and write them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `alveo-rdm-logs-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose the topic `alveo-rdm-logs-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select the service account `alveo-rdm-logs-collector-sa`
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `alveo-rdm-audit-logs` | GCS bucket name  
`GCS_PREFIX` | `alveo-rdm` | Prefix for log files  
`STATE_KEY` | `alveo-rdm/state.json` | State file path  
`ALVEO_BASE_URL` | `https://yourcompany.alveotech.com` | Alveo RDM API base URL  
`ALVEO_CLIENT_ID` | `your-client-id` | OAuth2 Client ID  
`ALVEO_CLIENT_SECRET` | `your-client-secret` | OAuth2 Client Secret  
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
           GCS_PREFIX = os.environ.get('GCS_PREFIX', 'alveo-rdm').strip('/')
           STATE_KEY = os.environ.get('STATE_KEY') or f"{GCS_PREFIX}/state.json"
           ALVEO_BASE_URL = os.environ.get('ALVEO_BASE_URL', '').rstrip('/')
           ALVEO_CLIENT_ID = os.environ.get('ALVEO_CLIENT_ID')
           ALVEO_CLIENT_SECRET = os.environ.get('ALVEO_CLIENT_SECRET')
           PAGE_SIZE = int(os.environ.get('PAGE_SIZE', '100'))
           MAX_RECORDS = int(os.environ.get('MAX_RECORDS', '10000'))
           LOOKBACK_HOURS = int(os.environ.get('LOOKBACK_HOURS', '2'))
           
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
           
           def get_access_token():
             """Get OAuth2 access token using client credentials."""
             token_url = f"{ALVEO_BASE_URL}/oauth/token"
             body = urllib.parse.urlencode({
               'grant_type': 'client_credentials',
               'client_id': ALVEO_CLIENT_ID,
               'client_secret': ALVEO_CLIENT_SECRET,
             }).encode('utf-8')
           
             response = http.request(
               'POST',
               token_url,
               body=body,
               headers={'Content-Type': 'application/x-www-form-urlencoded'},
             )
           
             if response.status != 200:
               raise Exception(
                 f"Failed to get access token: HTTP {response.status} "
                 f"{response.data.decode('utf-8')}"
               )
           
             data = json.loads(response.data.decode('utf-8'))
             return data['access_token']
           
           @functions_framework.cloud_event
           def main(cloud_event):
             """
             Cloud Run function triggered by Pub/Sub to fetch
             Alveo RDM audit trail records and write to GCS.
           
             Args:
               cloud_event: CloudEvent object containing Pub/Sub message
             """
           
             if not all([GCS_BUCKET, ALVEO_BASE_URL, ALVEO_CLIENT_ID,
                   ALVEO_CLIENT_SECRET]):
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
                 f"Fetching audit logs from {last_time.isoformat()} "
                 f"to {now.isoformat()}"
               )
           
               # Get OAuth2 token
               token = get_access_token()
               print("Successfully obtained OAuth2 access token")
           
               # Fetch audit logs
               records, newest_event_time = fetch_audit_logs(
                 token=token,
                 start_time=last_time,
                 end_time=now,
               )
           
               if not records:
                 print("No new audit log records found.")
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
               print(f'Error processing audit logs: {str(e)}')
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
           
           def fetch_audit_logs(token, start_time, end_time):
             """
             Fetch audit trail logs from Alveo RDM REST API with pagination.
           
             Args:
               token: OAuth2 access token
               start_time: Start time for log query
               end_time: End time for log query
           
             Returns:
               Tuple of (records list, newest_event_time ISO string)
             """
             endpoint = f"{ALVEO_BASE_URL}/api/v1/audit/events"
           
             headers = {
               'Authorization': f'Bearer {token}',
               'Accept': 'application/json',
               'Content-Type': 'application/json',
               'User-Agent': 'GoogleSecOps-AlveoRDMCollector/1.0'
             }
           
             start_iso = start_time.isoformat()
             end_iso = end_time.isoformat()
           
             records = []
             newest_time = None
             offset = 0
             page_num = 0
             backoff = 1.0
           
             while True:
               if len(records) >= MAX_RECORDS:
                 print(f"Reached max_records limit ({MAX_RECORDS})")
                 break
           
               params = (
                 f"?startTime={urllib.parse.quote(start_iso)}"
                 f"&endTime={urllib.parse.quote(end_iso)}"
                 f"&offset={offset}"
                 f"&limit={min(PAGE_SIZE, MAX_RECORDS - len(records))}"
               )
               url = f"{endpoint}{params}"
           
               try:
                 response = http.request('GET', url, headers=headers)
           
                 # Handle rate limiting with exponential backoff
                 if response.status == 429:
                   retry_after = int(
                     response.headers.get('Retry-After', str(int(backoff)))
                   )
                   print(
                     f"Rate limited (429). Retrying after {retry_after}s..."
                   )
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
           
                 page_results = data.get('events', [])
           
                 if not page_results:
                   print(f"No more results (empty page {page_num})")
                   break
           
                 print(
                   f"Page {page_num}: Retrieved {len(page_results)} events"
                 )
                 records.extend(page_results)
           
                 # Track newest event time
                 for event in page_results:
                   try:
                     event_time = event.get('timestamp')
                     if event_time:
                       if newest_time is None:
                         newest_time = event_time
                       else:
                         current_dt = parse_datetime(event_time)
                         newest_dt = parse_datetime(newest_time)
                         if (current_dt and newest_dt
                             and current_dt > newest_dt):
                           newest_time = event_time
                   except Exception as e:
                     print(
                       f"Warning: Could not parse event time: {e}"
                     )
           
                 # Check pagination
                 if len(page_results) < PAGE_SIZE:
                   print(
                     f"Reached last page "
                     f"(size={len(page_results)} < limit={PAGE_SIZE})"
                   )
                   break
           
                 offset += len(page_results)
                 page_num += 1
           
               except Exception as e:
                 print(f"Error fetching audit logs: {e}")
                 return [], None
           
             print(
               f"Retrieved {len(records)} total records "
               f"from {page_num + 1} pages"
             )
             return records, newest_time
           

     * Second file - **requirements.txt:**
           
           functions-framework==3.*
           google-cloud-storage==2.*
           urllib3>=2.0.0
           

  3. Click **Deploy** to save and deploy the function.

  4. Wait for deployment to complete (2-3 minutes).

**Note:** The Pub/Sub trigger configuration automatically creates the necessary subscriptions and permissions. The function obtains a fresh OAuth2 access token at the start of each execution to avoid token expiration issues.



## Create a Cloud Scheduler job

Cloud Scheduler will publish messages to the Pub/Sub topic at regular intervals, triggering the Cloud Run function.

  1. In the **GCP Console** , go to **Cloud Scheduler**.
  2. Click **Create Job**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | `alveo-rdm-logs-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the topic `alveo-rdm-logs-trigger`  
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
  5. Click on the function name `alveo-rdm-logs-collector`.
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         Successfully obtained OAuth2 access token
         Fetching audit logs from YYYY-MM-DDTHH:MM:SS+00:00 to YYYY-MM-DDTHH:MM:SS+00:00
         Page 0: Retrieved X events
         Wrote X records to gs://alveo-rdm-audit-logs/alveo-rdm/logs_YYYYMMDD_HHMMSS.ndjson
         Successfully processed X records
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click your bucket name.

  10. Navigate to the prefix folder `alveo-rdm/`.

  11. Verify that a new `.ndjson` file was created with the current timestamp.




If you see errors in the logs:

  * **HTTP 401** : Check OAuth2 credentials in environment variables. Verify Client ID and Client Secret are correct.
  * **HTTP 403** : Verify the API client has the required scopes (audit:read, data:read).
  * **HTTP 429** : Rate limiting - function will automatically retry with backoff.
  * **Token error** : Check that the ALVEO_BASE_URL is correct and the OAuth2 token endpoint is reachable.
  * **Missing environment variables** : Check all required variables are set.



## Configure a feed in Google SecOps to ingest Alveo RDM logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Alveo RDM Audit Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Alveo Risk Data Management** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Don't use service accounts from other documentation or examples.
  9. Click **Next**.

  10. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://alveo-rdm-audit-logs/alveo-rdm/
           

       * Replace: 
         * `alveo-rdm-audit-logs`: Your GCS bucket name.
         * `alveo-rdm`: Optional prefix/folder path where logs are stored (leave empty for root).
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
`function_label` | `additional.fields` | Merged  
`interface_attribute_label` | `additional.fields` | Merged  
`interface_datafile_label` | `additional.fields` | Merged  
`log_level_label` | `additional.fields` | Merged  
`new_value_label` | `additional.fields` | Merged  
`object_label` | `additional.fields` | Merged  
`old_value_label` | `additional.fields` | Merged  
`operation_type_label` | `additional.fields` | Merged  
`register_type_label` | `additional.fields` | Merged  
`status_process_label` | `additional.fields` | Merged  
`msg` | `extensions.auth.type` | Mapped: `logon` → `MACHINE`  
`date` | `metadata.event_timestamp` | Parsed as `MMM dd yyyy HH:mm:ss`  
`date_hours` | `metadata.event_timestamp` | Parsed as `yyyyMMdd HHmmss`  
`has_principal` | `metadata.event_type` | Mapped: `true` → `NETWORK_CONNECTION`, `true` → `STATUS_UPDATE`  
`has_user` | `metadata.event_type` | Mapped: `true` → `USER_UNCATEGORIZED`  
`msg` | `metadata.event_type` | Mapped: `logon` → `USER_LOGIN`  
`host_name` | `principal.asset.hostname` | Directly mapped  
`src_ip` | `principal.asset.ip` | Merged  
`host_name` | `principal.hostname` | Directly mapped  
`src_ip` | `principal.ip` | Merged  
`country` | `principal.location.country_or_region` | Directly mapped  
`object_type` | `principal.user.role_name` | Directly mapped  
`modified_user` | `principal.user.userid` | Directly mapped  
`act` | `security_result.action` | Merged  
`msg` | `security_result.action` | Mapped: `failed` → `act`  
`msg` | `security_result.description` | Directly mapped  
`process_id` | `target.process.pid` | Directly mapped  
`affected_user` | `target.user.userid` | Directly mapped  
`user_id` | `target.user.userid` | Directly mapped  
N/A | `extensions.auth.type` | Constant: `MACHINE`  
N/A | `metadata.event_type` | Constant: `USER_LOGIN`  
N/A | `metadata.product_name` | Constant: `ALVEO RDM`  
N/A | `metadata.vendor_name` | Constant: `ALVEO RDM`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/alveo-rdm-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
