---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vectra-xdr/
title: Collect Vectra XDR logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T12:27:20.653062+00:00
---

# Collect Vectra XDR logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vectra-xdr/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Vectra XDR logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Vectra XDR logs to Google Security Operations using Google Cloud Storage V2.

Vectra XDR is an extended detection and response platform that correlates threats across network, identity, cloud, and SaaS environments. The Vectra AI Platform REST API v3 provides programmatic access to detection, scoring, lockdown, audit, and health logs.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * Privileged access to the Vectra AI Platform with administrator permissions
  * An API client with Client ID and Client Secret configured in the Vectra AI Platform



## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `vectra-xdr-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Collect Vectra XDR API credentials

### Create API client

  1. Sign in to your Vectra AI Platform instance (for example, `https://your-tenant.vectra.ai`).
  2. Go to **Manage > API Clients**.
  3. Click **Add API Client**.
  4. Enter a name for the API client (for example, `Google SecOps Integration`).
  5. Select the required role (for example, **Read-Only** or a custom role with detection and audit access).
  6. Click **Generate Credentials**.
  7. Copy and save the following details in a secure location:

     * **Client ID** : The API client ID
     * **Client Secret** : The API client secret
**Note:** The client secret is displayed only once. Store it securely. If lost, you will need to regenerate the credentials.



### Determine API base URL

The Vectra API base URL is your tenant URL:

Format | Example  
---|---  
Tenant URL | `https://your-tenant.vectra.ai`  
**Note:** Replace `your-tenant` with your actual Vectra AI Platform tenant name.

### Test API access

  * Test your credentials before proceeding with the integration:
        
        # Replace with your actual credentials
        VECTRA_CLIENT_ID="your-client-id"
        VECTRA_CLIENT_SECRET="your-client-secret"
        VECTRA_BASE_URL="https://your-tenant.vectra.ai"
        
        # Get access token using HTTP Basic Auth
        TOKEN=$(curl -s -X POST "${VECTRA_BASE_URL}/oauth2/token" \
          -u "${VECTRA_CLIENT_ID}:${VECTRA_CLIENT_SECRET}" \
          -H "Content-Type: application/x-www-form-urlencoded" \
          -d "grant_type=client_credentials" \
          | jq -r '.access_token')
        
        # Test API access - list detection events
        curl -s -X GET "${VECTRA_BASE_URL}/api/v3.4/events/detections/?limit=1" \
          -H "Authorization: Bearer ${TOKEN}"
        




## Create service account for Cloud Run function

The Cloud Run function needs a service account with permissions to write to GCS bucket and be invoked by Pub/Sub.

### Create service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `vectra-xdr-logs-collector-sa`
     * **Service account description** : Enter `Service account for Cloud Run function to collect Vectra XDR logs`
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
  2. Click your bucket name (for example, `vectra-xdr-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `vectra-xdr-logs-collector-sa@PROJECT_ID.iam.gserviceaccount.com`)
     * **Assign roles** : Select **Storage Object Admin**
  6. Click **Save**.



## Create Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `vectra-xdr-logs-trigger`
     * Leave other settings as default
  4. Click **Create**.



## Create Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from the Vectra AI Platform REST API and write them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `vectra-xdr-logs-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose the topic `vectra-xdr-logs-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll to and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select the service account `vectra-xdr-logs-collector-sa`.
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:

Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `vectra-xdr-logs` | GCS bucket name  
`GCS_PREFIX` | `vectra` | Prefix for log files  
`STATE_KEY` | `vectra/state.json` | State file path  
`VECTRA_CLIENT_ID` | `your-client-id` | Vectra API client ID  
`VECTRA_CLIENT_SECRET` | `your-client-secret` | Vectra API client secret  
`VECTRA_BASE_URL` | `https://your-tenant.vectra.ai` | Vectra tenant URL  
`MAX_RECORDS` | `5000` | Max records per run  
`BATCH_SIZE` | `500` | Events per API request (max 1000)  
`LOOKBACK_HOURS` | `24` | Initial lookback period  
  10. In the **Variables & Secrets** section, scroll to **Requests** :

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

  15. After the service is created, the **inline code editor** opens automatically.




### Add function code

  1. Enter **main** in the **Entry point** field.
  2. In the inline code editor, create two files:

     * First file: **main.py:**
           
           import functions_framework
           from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
           import base64
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
           GCS_PREFIX = os.environ.get('GCS_PREFIX', 'vectra')
           STATE_KEY = os.environ.get('STATE_KEY', 'vectra/state.json')
           VECTRA_CLIENT_ID = os.environ.get('VECTRA_CLIENT_ID')
           VECTRA_CLIENT_SECRET = os.environ.get('VECTRA_CLIENT_SECRET')
           VECTRA_BASE_URL = os.environ.get('VECTRA_BASE_URL')
           MAX_RECORDS = int(os.environ.get('MAX_RECORDS', '5000'))
           BATCH_SIZE = int(os.environ.get('BATCH_SIZE', '500'))
           LOOKBACK_HOURS = int(os.environ.get('LOOKBACK_HOURS', '24'))
           
           def get_access_token():
             """
             Obtain OAuth2 access token using HTTP Basic Auth
             with client credentials grant per Vectra API docs.
             """
             base_url = VECTRA_BASE_URL.rstrip('/')
             token_url = f"{base_url}/oauth2/token"
           
             credentials = base64.b64encode(
               f"{VECTRA_CLIENT_ID}:{VECTRA_CLIENT_SECRET}".encode()
             ).decode()
           
             headers = {
               'Content-Type': 'application/x-www-form-urlencoded',
               'Authorization': f'Basic {credentials}',
               'Accept': 'application/json'
             }
           
             body = 'grant_type=client_credentials'
           
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
                 raise RuntimeError(f"Failed to get access token: {response.status} - {response.data.decode('utf-8')}")
           
               data = json.loads(response.data.decode('utf-8'))
               return data['access_token']
           
             raise RuntimeError("Failed to get access token after 3 retries")
           
           @functions_framework.cloud_event
           def main(cloud_event):
             """
             Cloud Run function triggered by Pub/Sub to fetch Vectra XDR
             detection and audit event logs and write to GCS.
             Uses the Vectra REST API v3.4 Events endpoints with
             checkpoint-based pagination.
             """
           
             if not all([GCS_BUCKET, VECTRA_CLIENT_ID, VECTRA_CLIENT_SECRET, VECTRA_BASE_URL]):
               print('Error: Missing required environment variables')
               return
           
             try:
               bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(GCS_BUCKET)
           
               # Load state (stores per-endpoint checkpoints)
               state = load_state(bucket, STATE_KEY)
           
               now = datetime.now(timezone.utc)
               token = get_access_token()
           
               # Fetch detection events and audit events
               all_records = []
               new_state = dict(state)
           
               for event_type in ['detections', 'audits']:
                 checkpoint = [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get(f'{event_type}_checkpoint')
                 last_time = [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get(f'{event_type}_last_time')
           
                 # On first run, use lookback window
                 start_time = None
                 if not checkpoint and not last_time:
                   start_time = now - timedelta(hours=LOOKBACK_HOURS)
           
                 records, next_checkpoint = fetch_events(
                   token=token,
                   event_type=event_type,
                   checkpoint=checkpoint,
                   start_time=start_time,
                   batch_size=BATCH_SIZE,
                   max_records=MAX_RECORDS,
                 )
                 all_records.extend(records)
           
                 # Save checkpoint for next run
                 if next_checkpoint is not None:
                   new_state[f'{event_type}_checkpoint'] = next_checkpoint
                 new_state[f'{event_type}_last_time'] = now.isoformat()
           
               if not all_records:
                 print("No new event records found.")
                 save_state(bucket, STATE_KEY, new_state)
                 return
           
               # Write to GCS as NDJSON
               timestamp = now.strftime('%Y%m%d_%H%M%S')
               object_key = f"{GCS_PREFIX}/logs_{timestamp}.ndjson"
               blob = bucket.blob(object_key)
           
               ndjson = '\n'.join(
                 json.dumps(record, ensure_ascii=False) for record in all_records
               ) + '\n'
               blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(ndjson, content_type='application/x-ndjson')
           
               print(f"Wrote {len(all_records)} records to gs://{GCS_BUCKET}/{object_key}")
           
               save_state(bucket, STATE_KEY, new_state)
               print(f"Successfully processed {len(all_records)} records")
           
             except Exception as e:
               print(f'Error processing logs: {str(e)}')
               raise
           
           def load_state(bucket, key):
             """Load state from GCS."""
             try:
               blob = bucket.blob(key)
               if blob.exists():
                 return json.loads(blob.[download_as_text](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_download_as_text)())
             except Exception as e:
               print(f"Warning: Could not load state: {e}")
             return {}
           
           def save_state(bucket, key, state: dict):
             """Save state to GCS."""
             try:
               blob = bucket.blob(key)
               blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
                 json.dumps(state, indent=2),
                 content_type='application/json'
               )
               print(f"Saved state: {[state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state)}")
             except Exception as e:
               print(f"Warning: Could not save state: {e}")
           
           def fetch_events(token: str, event_type: str, checkpoint: int = None,
                   start_time: datetime = None, batch_size: int = 500,
                   max_records: int = 5000):
             """
             Fetch events from Vectra AI Platform REST API v3.4
             using checkpoint-based pagination.
           
             Endpoints:
               - /api/v3.4/events/detections/
               - /api/v3.4/events/audits/
           
             Args:
               token: OAuth2 access token
               event_type: 'detections' or 'audits'
               checkpoint: Resume from this event ID (from previous run)
               start_time: Only used on first run when no checkpoint exists
               batch_size: Number of events per request (max 1000)
               max_records: Maximum total events to fetch per run
           
             Returns:
               Tuple of (events list, next_checkpoint int or None)
             """
             base_url = VECTRA_BASE_URL.rstrip('/')
             endpoint = f"{base_url}/api/v3.4/events/{event_type}/"
           
             headers = {
               'Authorization': f'Bearer {token}',
               'Accept': 'application/json',
               'User-Agent': 'GoogleSecOps-VectraXDRCollector/1.0'
             }
           
             records = []
             batch_num = 0
             backoff = 1.0
             next_checkpoint = checkpoint
           
             while True:
               batch_num += 1
           
               if len(records) >= max_records:
                 print(f"Reached max_records limit ({max_records}) for {event_type}")
                 break
           
               # Build query parameters
               params = {
                 'limit': min(batch_size, max_records - len(records)),
                 'ordering': 'event_timestamp',
               }
           
               if next_checkpoint is not None:
                 params['from'] = next_checkpoint
               elif start_time is not None:
                 params['event_timestamp_gte'] = start_time.strftime('%Y-%m-%dT%H:%M:%SZ')
           
               # Include INFO detections (excluded by default in v3.4)
               if event_type == 'detections':
                 params['include_info_category'] = 'true'
           
               query_string = '&'.join(f'{k}={v}' for k, v in params.items())
               url = f"{endpoint}?{query_string}"
           
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
                   print(f"HTTP {response.status}: {response.data.decode('utf-8')}")
                   break
           
                 data = json.loads(response.data.decode('utf-8'))
           
                 events = data.get('events', [])
                 remaining = data.get('remaining_count', 0)
                 batch_checkpoint = data.get('next_checkpoint')
           
                 if not events:
                   print(f"No more events for {event_type}")
                   break
           
                 print(f"{event_type} batch {batch_num}: {len(events)} events, {remaining} remaining")
           
                 # Tag events with source type
                 for event in events:
                   event['_vectra_event_type'] = event_type
           
                 records.extend(events)
           
                 # Update checkpoint for next batch/run
                 if batch_checkpoint is not None:
                   next_checkpoint = batch_checkpoint
           
                 # No more events remaining
                 if remaining == 0:
                   print(f"All events fetched for {event_type}")
                   break
           
               except Exception as e:
                 print(f"Error fetching {event_type} events: {e}")
                 break
           
             print(f"Retrieved {len(records)} total {event_type} events from {batch_num} batches")
             return records, next_checkpoint
           

     * Second file: **requirements.txt:**
           
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
**Name** | `vectra-xdr-logs-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the topic `vectra-xdr-logs-trigger`  
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
  5. Click `vectra-xdr-logs-collector`.
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         detections batch 1: X events, Y remaining
         All events fetched for detections
         audits batch 1: X events, Y remaining
         All events fetched for audits
         Wrote X records to gs://vectra-xdr-logs/vectra/logs_YYYYMMDD_HHMMSS.ndjson
         Successfully processed X records
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click your bucket name (`vectra-xdr-logs`).

  10. Navigate to the `vectra/` folder.

  11. Verify that a new `.ndjson` file was created with the current timestamp.




If you see errors in the logs:

  * **HTTP 401** : Check client credentials in environment variables
  * **HTTP 403** : Verify API client has required permissions in Vectra AI Platform
  * **HTTP 429** : Rate limiting - function will automatically retry with backoff
  * **Missing environment variables** : Check all required variables are set



## Configure a feed in Google SecOps to ingest Vectra XDR logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Vectra XDR Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Vectra XDR** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address.

**Note:** Each Google SecOps instance has a unique service account. Do not use service accounts from other documentation or examples.
  9. Click **Next**.

  10. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://vectra-xdr-logs/vectra/
           

       * Replace: 
         * `vectra-xdr-logs`: Your GCS bucket name.
         * `vectra`: Optional prefix/folder path where logs are stored (leave empty for root).
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
log_type_lable, id_label, triaged_label, detail_label, properties_label, event_object_label | additional.fields | Merged with various labels based on log type  
msg, d_type_vname | extensions.auth.auth_details | Set to msg for USER_LOGIN, d_type_vname for other user logins  
d_type_vname, category, type, msg | metadata.event_type | Set to GENERIC_EVENT initially; overridden to specific types based on log type and conditions  
d_type_vname, category, type, event_action | metadata.product_event_type | Set to d_type_vname in Detection, category in Scoring, type in Lockdown, event_action in Audit  
detection_id, id | metadata.product_log_id | Set to detection_id in Detection, id in Lockdown and Audit  
version, system.version.vectra_version | metadata.product_version | Set to version in Audit, system.version.vectra_version in Health  
_sensor.serial_number | observer.asset_id | Value copied directly  
_sensor.name | observer.hostname | Value copied directly  
_sensor.ip_address | observer.ip | Value copied directly  
_sensor.location | observer.location.name | Value copied directly  
entity_id | principal.asset_id | Value copied directly, prefixed with "Vectra:" if not colon-separated  
entity_uid | principal.hostname | Value copied directly if matches pattern  
src_ip, source_ip | principal.ip | Set from src_ip in Detection if valid IP, source_ip in Audit if valid IP  
var_entity_uid, var_username, var_api_client_id, var_user_type, var_entity_name | principal.user.attribute.labels | Merged with various var_ based on log type  
user_role | principal.user.attribute.roles | Value copied directly  
entity_uid, name, entity_name, username | principal.user.email_addresses | Set from entity_uid in Detection if email pattern, name in Scoring if email pattern, entity_name in Lockdown if email pattern, username in Audit if email pattern  
locked_by | principal.user.user_display_name | Value copied directly  
entity_id, user_id | principal.user.userid | Set from entity_id in Detection/Scoring/Lockdown, user_id in Audit  
result_status | security_result.action | Set to ALLOW if success, FAIL if failure  
result_status | security_result.action_details | Value copied directly  
mitre | security_result.attack_details.techniques | Merged from mitre array  
category | security_result.category | Mapped to category_temp based on regex matches for COMMAND & CONTROL, BOTNET ACTIVITY, etc.  
category | security_result.category_details | Value copied directly  
certainty | security_result.confidence_score | Converted to float  
urgency_reason, msg | security_result.description | Set to urgency_reason in Scoring, msg in Audit  
var_type, var_detection_type, var_triaged, var_id, var_active_detection_types, var_breadth_contrib, var_attack_rating, var_importance, var_last_detection_id, var_last_detection_type, var_last_detection_url, var_urgency_score, var_velocity_contrib, unlock_event_timestamp_label, var_detection_updated_at, var_sensor_connectivity_sensors_error, var_connectivity_sensors_affected_metadata_hours, var_connectivity_sensors_status, var_connectivity_updated_at, var_cpu_idle_percent, var_cpu_nice_percent, var_cpu_system_percent, var_cpu_updated_at, var_cpu_user_percent, var_disk_disk_utilization_free_bytes, var_disk_raid_disks_missing_output_label, var_disk_raid_disks_missing_error, var_disk_raid_disks_missing_status, var_disk_degraded_raid_volume_output, var_disk_degraded_raid_volume_error, var_disk_degraded_raid_volume_status, var_disk_disk_raid_error, var_disk_disk_raid_status, var_disk_disk_raid_output, var_disk_disk_utilization_total_bytes, var_disk_disk_utilization_usage_percent, var_disk_disk_utilization_used_bytes, var_disk_updated_at, var_hostid_artifact_counts_arsenic, var_hostid_artifact_counts_carbon_black, var_hostid_artifact_counts_cb_cloud, var_hostid_artifact_counts_clear_state, var_hostid_artifact_counts_cookie, var_hostid_artifact_counts_crowdstrike, var_hostid_artifact_counts_cybereason, var_hostid_artifact_counts_dhcp, var_hostid_artifact_counts_dns, var_hostid_artifact_counts_end_time, var_hostid_artifact_counts_fireeye, var_hostid_artifact_counts_generic_edr, var_hostid_artifact_counts_idle_end, var_hostid_artifact_counts_idle_start, var_hostid_artifact_counts_invalid, var_hostid_artifact_counts_kerberos_user, var_hostid_artifact_counts_kerberos, var_hostid_artifact_counts_mdns, var_hostid_artifact_counts_netbios, var_hostid_artifact_counts_proxy_ip, var_hostid_artifact_counts_rdns, var_hostid_artifact_counts_sentinelone, var_hostid_artifact_counts_split, var_hostid_artifact_counts_src_port, var_hostid_artifact_counts_static_ip, var_hostid_artifact_counts_TestEDR, var_hostid_artifact_counts_total, var_hostid_artifact_counts_uagent, var_hostid_artifact_counts_vmachine_info, var_hostid_artifact_counts_windows_defender, var_hostid_artifact_counts_zpa_user, var_hostid_ip_always_percent, var_hostid_ip_never_percent, var_hostid_ip_sometimes_percent, var_hostid_updated_at, var_dimm_stat_dimm, var_dimm_stat_status, var_memory_free_bytes, var_memory_total_bytes, var_memory_updated_at, var_memory_usage_percent, var_memory_used_bytes, network_interfaces_brain_label, var_network_interfaces_sensors_w4ftj0a8_eth0_link, var_network_traffic_brain_aggregated_peak_traffic_mbps, var_network_traffic_brain_interface_peak_traffic_label, var_network_traffic_sensors_edr_sensor_aggregated_peak_traffic_mbps, var_sensor_interface_peak_traffic_eth0_peak_traffic_mbps, var_network_updated_at, var_network_vlans_count, var_network_vlans_vlan_ids, var_power_error, var_power_status, var_power_updated_at, var_power_power_supply, var_sensors_headend_uri, var_sensors_id, var_sensors_last_seen, var_sensors_luid, var_sensors_mode, var_sensors_original_version, var_sensors_product_name, var_sensors_public_key, var_sensors_ssh_tunnel_port, var_sensors_status, var_sensors_update_count, var_sensors_version, var_trafficdrop_sensors_error, var_trafficdrop_sensors_ip_address, var_trafficdrop_sensors_luid, var_trafficdrop_sensors_name, var_trafficdrop_sensors_output_end, var_trafficdrop_sensors_output_interface_cutoff, var_trafficdrop_sensors_output_start, var_trafficdrop_sensors_output_interface_baseline, var_trafficdrop_sensors_output_interface_name, var_trafficdrop_sensors_output_interface_traffic, var_trafficdrop_sensors_serial_number, var_trafficdrop_sensors_status, var_trafficdrop_updated_at | security_result.detection_fields | Merged with various var_ and labels based on log type  
is_prioritized | security_result.priority | Set to HIGH if true, LOW if false  
is_prioritized | security_result.priority_details | Value copied directly  
threat | security_result.risk_score | Converted to float  
severity | security_result.severity | Set to HIGH if matches (?i)high, MEDIUM if matches (?i)medium, LOW if matches (?i)low  
severity | security_result.severity_details | Value copied directly  
detection_href, url | security_result.url_back_to_product | Set to detection_href in Detection, url in Scoring  
entity_id | target.asset_id | Value copied directly, prefixed with "Vectra:" if not colon-separated  
entity_name, name | target.hostname | Set from entity_name in Lockdown, name in Scoring if not IP  
target_ip_temp | target.ip | Value copied directly  
lock_event_timestamp | target.user.account_lockout_time | Converted from string to timestamp  
var_entity_name | target.user.attribute.labels | Merged with var_entity_name  
name, entity_name | target.user.email_addresses | Set from name in Scoring if email pattern, entity_name in Lockdown if email pattern  
entity_id | target.user.userid | Value copied directly  
| metadata.product_name | Set to "XDR"  
| metadata.vendor_name | Set to "Vectra"  
`entity_uid` | `principal.mac` or `principal.ip` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/vectra-xdr-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
