---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sailpoint-iam/
title: Collect SailPoint IAM logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T03:30:50.292573+00:00
---

# Collect SailPoint IAM logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sailpoint-iam/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect SailPoint IAM logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest SailPoint IAM logs to Google Security Operations using Google Cloud Storage. SailPoint Identity Security Cloud provides identity governance and administration capabilities for managing user access, compliance, and security across enterprise applications.

## Before you begin

Ensure that you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * Privileged access to SailPoint Identity Security Cloud tenant or API



## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `sailpoint-iam-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Collect SailPoint Identity Security Cloud API credentials

  1. Sign in to the **SailPoint Identity Security Cloud Admin Console** as an administrator.
  2. Go to **Admin > Global > Security Settings > API Management**.
  3. Click **Create API Client**.
  4. Choose **Client Credentials** as the grant type.
  5. Provide the following configuration details: 
     * **Name** : Enter a descriptive name (for example, `Chronicle Export API`).
     * **Description** : Enter description for the API client.
     * **Scopes** : Select **sp:scopes:all** (or appropriate read scopes for audit events).
  6. Click **Create** and copy the generated API credentials securely.
  7. Record your SailPoint tenant base URL (for example, `https://tenant.api.identitynow.com`).
  8. Copy and save in a secure location the following details:

     * `IDN_CLIENT_ID`
     * `IDN_CLIENT_SECRET`
     * `IDN_BASE`
**Note:** The OAuth client must be configured with the CLIENT_CREDENTIALS grant type. Some SailPoint APIs remain user-context-only even with scope sp:scopes:all. For more information, see [SailPoint authentication documentation](https://developer.sailpoint.com/docs/api/authentication/).



### Test API access

  * Test your credentials before proceeding with the integration:
        
        # Replace with your actual credentials
        IDN_CLIENT_ID="your-client-id"
        IDN_CLIENT_SECRET="your-client-secret"
        IDN_BASE="https://tenant.api.identitynow.com"
        
        # Get OAuth token
        TOKEN=$(curl -s -X POST "${IDN_BASE}/oauth/token" \
          -H "Content-Type: application/x-www-form-urlencoded" \
          -d "grant_type=client_credentials&client_id=${IDN_CLIENT_ID}&client_secret=${IDN_CLIENT_SECRET}&scope=sp:scopes:all" | jq -r '.access_token')
        
        # Test API access
        curl -v -H "Authorization: Bearer ${TOKEN}" "${IDN_BASE}/v3/search" \
          -H "Content-Type: application/json" \
          -d '{"indices":["events"],"query":{"query":"*"},"limit":1}'
        




## Create service account for Cloud Run function

The Cloud Run function needs a service account with permissions to write to GCS bucket.

### Create service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `sailpoint-iam-collector-sa`.
     * **Service account description** : Enter `Service account for Cloud Run function to collect SailPoint IAM logs`.
  4. Click **Create and Continue**.
  5. In the **Grant this service account access to project** section: 
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



#### Grant IAM permissions on GCS bucket

Grant the service account write permissions on the GCS bucket:

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email.
     * **Assign roles** : Select **Storage Object Admin**.
  6. Click **Save**.



## Create Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `sailpoint-iam-trigger`.
     * Leave other settings as default.
  4. Click **Create**.



## Create Cloud Run function to collect logs

The Cloud Run function is triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from SailPoint Identity Security Cloud API and writes them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `sailpoint-iam-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose the Pub/Sub topic (`sailpoint-iam-trigger`).
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub automatically handles authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select the service account (`sailpoint-iam-collector-sa`).
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value  
---|---  
`GCS_BUCKET` | `sailpoint-iam-logs`  
`GCS_PREFIX` | `sailpoint/iam/`  
`STATE_KEY` | `sailpoint/iam/state.json`  
`WINDOW_SECONDS` | `3600`  
`HTTP_TIMEOUT` | `60`  
`MAX_RETRIES` | `3`  
`USER_AGENT` | `sailpoint-iam-to-gcs/1.0`  
`IDN_BASE` | `https://tenant.api.identitynow.com`  
`IDN_CLIENT_ID` | `your-client-id`  
`IDN_CLIENT_SECRET` | `your-client-secret`  
`IDN_SCOPE` | `sp:scopes:all`  
`PAGE_SIZE` | `250`  
`MAX_PAGES` | `20`  
  10. Scroll down in the **Variables & Secrets** tab to **Requests** :

     * **Request timeout** : Enter `600` seconds (10 minutes).
  11. Go to the **Settings** tab in **Containers** :

     * In the **Resources** section: 
       * **Memory** : Select **512 MiB** or higher.
       * **CPU** : Select **1**.
     * Click **Done**.
  12. Scroll down to **Execution environment** :

     * Select **Default** (recommended).
  13. In the **Revision scaling** section:

     * **Minimum number of instances** : Enter `0`.
     * **Maximum number of instances** : Enter `100` (or adjust based on expected load).
  14. Click **Create**.

  15. Wait for the service to be created (1-2 minutes).

  16. After the service is created, the **inline code editor** opens automatically.




### Add function code

  1. Enter **main** in **Function entry point**
  2. In the inline code editor, create two files:

     * First file: **main.py:**
    
    import functions_framework
     from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
     import json
     import os
     import urllib3
     from datetime import datetime, timezone
     import time
     import uuid
    
     # Initialize HTTP client
     http = urllib3.PoolManager()
    
     # Initialize Storage client
     storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    
     # Get environment variables
     GCS_BUCKET = os.environ.get('GCS_BUCKET')
     GCS_PREFIX = os.environ.get('GCS_PREFIX', 'sailpoint/iam/')
     STATE_KEY = os.environ.get('STATE_KEY', 'sailpoint/iam/state.json')
     WINDOW_SEC = int(os.environ.get('WINDOW_SECONDS', '3600'))
     HTTP_TIMEOUT = int(os.environ.get('HTTP_TIMEOUT', '60'))
     IDN_BASE = os.environ.get('IDN_BASE')
     CLIENT_ID = os.environ.get('IDN_CLIENT_ID')
     CLIENT_SECRET = os.environ.get('IDN_CLIENT_SECRET')
     SCOPE = os.environ.get('IDN_SCOPE', 'sp:scopes:all')
     PAGE_SIZE = int(os.environ.get('PAGE_SIZE', '250'))
     MAX_PAGES = int(os.environ.get('MAX_PAGES', '20'))
     MAX_RETRIES = int(os.environ.get('MAX_RETRIES', '3'))
     USER_AGENT = os.environ.get('USER_AGENT', 'sailpoint-iam-to-gcs/1.0')
    
     def _load_state(bucket):
         """Load state from GCS."""
         try:
             blob = bucket.blob(STATE_KEY)
             if blob.exists():
                 state_data = blob.[download_as_text](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_download_as_text)()
                 return json.loads(state_data)
         except Exception as e:
             print(f'Warning: Could not load state: {str(e)}')
         return {}
    
     def _save_state(bucket, st):
         """Save state to GCS."""
         try:
             blob = bucket.blob(STATE_KEY)
             blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
                 json.dumps(st, separators=(',', ':')),
                 content_type='application/json'
             )
         except Exception as e:
             print(f'Warning: Could not save state: {str(e)}')
    
     def _iso(ts):
         """Convert timestamp to ISO format."""
         return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(ts))
    
     def _get_oauth_token():
         """Get OAuth2 access token using Client Credentials flow."""
         token_url = f"{IDN_BASE.rstrip('/')}/oauth/token"
    
         fields = {
             'grant_type': 'client_credentials',
             'client_id': CLIENT_ID,
             'client_secret': CLIENT_SECRET,
             'scope': SCOPE
         }
    
         headers = {
             'Content-Type': 'application/x-www-form-urlencoded',
             'User-Agent': USER_AGENT
         }
    
         response = http.request(
             'POST',
             token_url,
             fields=fields,
             headers=headers,
             timeout=HTTP_TIMEOUT
         )
    
         token_data = json.loads(response.data.decode('utf-8'))
         return token_data['access_token']
    
     def _search_events(access_token, created_from, search_after=None):
         """Search for audit events using SailPoint's /v3/search API.
    
         IMPORTANT: SailPoint requires colons in ISO8601 timestamps to be escaped with backslashes.
         Example: 2024-01-15T10:30:00Z must be sent as 2024-01-15T10\\:30\\:00Z
    
         For more information, see:
         - https://developer.sailpoint.com/docs/api/standard-collection-parameters/
         - https://developer.sailpoint.com/docs/api/v3/search-post/
         """
         search_url = f"{IDN_BASE.rstrip('/')}/v3/search"
    
         # Escape colons in timestamp for SailPoint search query
         escaped_timestamp = created_from.replace(':', '\\:')
         query_str = f'created:>={escaped_timestamp}'
    
         payload = {
             'indices': ['events'],
             'query': {
                 'query': query_str
             },
             'sort': ['created', '+id'],
             'limit': PAGE_SIZE
         }
    
         if search_after:
             payload['searchAfter'] = search_after
    
         attempt = 0
         while True:
             headers = {
                 'Content-Type': 'application/json',
                 'Accept': 'application/json',
                 'Authorization': f'Bearer {access_token}',
                 'User-Agent': USER_AGENT
             }
    
             try:
                 response = http.request(
                     'POST',
                     search_url,
                     body=json.dumps(payload).encode('utf-8'),
                     headers=headers,
                     timeout=HTTP_TIMEOUT
                 )
    
                 response_data = json.loads(response.data.decode('utf-8'))
    
                 # Handle different response formats
                 if isinstance(response_data, list):
                     return response_data
                 return response_data.get('results', response_data.get('data', []))
    
             except Exception as e:
                 attempt += 1
                 print(f'HTTP error on attempt {attempt}: {e}')
                 if attempt > MAX_RETRIES:
                     raise
                 # Exponential backoff with jitter
                 time.sleep(min(60, 2 ** attempt) + (time.time() % 1))
    
     def _put_events_data(bucket, events, from_ts, to_ts, page_num):
         """Write events to GCS in JSONL format (one JSON object per line)."""
         # Create unique GCS key for events data
         ts_path = time.strftime('%Y/%m/%d', time.gmtime(to_ts))
         uniq = f"{int(time.time() * 1e6)}_{uuid.uuid4().hex[:8]}"
         key = f"{GCS_PREFIX}{ts_path}/sailpoint_iam_{int(from_ts)}_{int(to_ts)}_p{page_num:03d}_{uniq}.jsonl"
    
         # Convert events list to JSONL format (one JSON object per line)
         jsonl_lines = [json.dumps(event, separators=(',', ':')) for event in events]
         jsonl_content = '\n'.join(jsonl_lines)
    
         blob = bucket.blob(key)
         blob.[metadata](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_metadata) = {
             'source': 'sailpoint-iam',
             'from_timestamp': str(int(from_ts)),
             'to_timestamp': str(int(to_ts)),
             'page_number': str(page_num),
             'events_count': str(len(events)),
             'format': 'jsonl'
         }
         blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
             jsonl_content,
             content_type='application/x-ndjson'
         )
    
         return key
    
     def _get_item_id(item):
         """Extract ID from event item, trying multiple possible fields."""
         for field in ('id', 'uuid', 'eventId', '_id'):
             if field in item and item[field]:
                 return str(item[field])
         return ''
    
     @functions_framework.cloud_event
     def main(cloud_event):
         """
         Cloud Run function triggered by Pub/Sub to fetch SailPoint IAM logs and write to GCS.
    
         Args:
             cloud_event: CloudEvent object containing Pub/Sub message
         """
    
         if not all([GCS_BUCKET, IDN_BASE, CLIENT_ID, CLIENT_SECRET]):
             print('Error: Missing required environment variables')
             return
    
         try:
             bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(GCS_BUCKET)
    
             st = _load_state(bucket)
             now = time.time()
             from_ts = float(st.get('last_to_ts') or (now - WINDOW_SEC))
             to_ts = now
    
             # Get OAuth token
             access_token = _get_oauth_token()
    
             created_from = _iso(from_ts)
             print(f'Fetching SailPoint IAM events from: {created_from}')
    
             # Handle pagination state
             last_created = st.get('last_created')
             last_id = st.get('last_id')
             search_after = [last_created, last_id] if (last_created and last_id) else None
    
             pages = 0
             total_events = 0
             written_keys = []
             newest_created = last_created or created_from
             newest_id = last_id or ''
    
             while pages < MAX_PAGES:
                 events = _search_events(access_token, created_from, search_after)
                 if not events:
                     break
    
                 # Write page to GCS in JSONL format
                 key = _put_events_data(bucket, events, from_ts, to_ts, pages + 1)
                 written_keys.append(key)
                 total_events += len(events)
    
                 # Update pagination state from last item
                 last_event = events[-1]
                 last_event_created = last_event.get('created') or last_event.get('metadata', {}).get('created')
                 last_event_id = _get_item_id(last_event)
    
                 if last_event_created:
                     newest_created = last_event_created
                 if last_event_id:
                     newest_id = last_event_id
    
                 search_after = [newest_created, newest_id]
                 pages += 1
    
                 # If we got less than page size, we're done
                 if len(events) < PAGE_SIZE:
                     break
    
             print(f'Successfully retrieved {total_events} events across {pages} pages')
    
             # Save state for next run
             st['last_to_ts'] = to_ts
             st['last_created'] = newest_created
             st['last_id'] = newest_id
             st['last_successful_run'] = now
             _save_state(bucket, st)
    
             print(f'Wrote {len(written_keys)} files to GCS')
    
         except Exception as e:
             print(f'Error processing logs: {str(e)}')
             raise
    

     * Second file: **requirements.txt:**
    
    functions-framework==3.*
     google-cloud-storage==2.*
     urllib3>=2.0.0
     ```
    

  3. Click **Deploy** to save and deploy the function.

  4. Wait for deployment to complete (2-3 minutes).

**Note:** The Pub/Sub trigger configuration automatically creates the necessary subscriptions and permissions.



## Create Cloud Scheduler job

Cloud scheduler publishes messages to the Pub/Sub topic at regular intervals, triggering the Cloud Run function.

  1. In the **GCP Console** , go to **Cloud Scheduler**.
  2. Click **Create Job**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | `sailpoint-iam-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the Pub/Sub topic (`sailpoint-iam-trigger`)  
**Message body** | `{}` (empty JSON object)  
  4. Click **Create**.




### Schedule frequency options

  * Choose frequency based on log volume and latency requirements:

Frequency | Cron Expression | Use Case  
---|---|---  
Every 5 minutes | `*/5 * * * *` | High-volume, low-latency  
Every 15 minutes | `*/15 * * * *` | Medium volume  
Every hour | `0 * * * *` | Standard (recommended)  
Every 6 hours | `0 */6 * * *` | Low volume, batch processing  
Daily | `0 0 * * *` | Historical data collection  



### Test the scheduler job

  1. In the **Cloud Scheduler** console, find your job.
  2. Click **Force run** to trigger manually.
  3. Wait a few seconds and go to **Cloud Run > Services > sailpoint-iam-collector > Logs**.
  4. Verify the function executed successfully.
  5. Check the GCS bucket to confirm logs were written.



## Retrieve the Google SecOps service account

Google SecOps uses a unique service account to read data from your GCS bucket. You must grant this service account access to your bucket.

### Get the service account email

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `SailPoint IAM logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **SailPoint IAM** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email is displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Don't use service accounts from other documentation or examples.



## Grant IAM permissions to the Google SecOps service account

The Google SecOps service account needs **Storage Object Viewer** role on your GCS bucket.

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Paste the Google SecOps service account email.
     * **Assign roles** : Select **Storage Object Viewer**.
  6. Click **Save**.

**Note:** If you plan to use the deletion option "Delete transferred files" or "Delete transferred files and empty directories," grant **Storage Object Admin** role instead of Storage Object Viewer.



## Configure a feed in Google SecOps to ingest SailPoint IAM logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `SailPoint IAM logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **SailPoint IAM** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://sailpoint-iam-logs/sailpoint/iam/
           

       * Replace:

         * `sailpoint-iam-logs`: Your GCS bucket name.
         * `sailpoint/iam/`: Optional prefix/folder path where logs are stored (leave empty for root).
       * **Examples:**

         * Root bucket: `gs://company-logs/`
         * With prefix: `gs://company-logs/sailpoint-logs/`
         * With subfolder: `gs://company-logs/sailpoint/iam/`
**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never** : Never deletes any files after transfers (recommended for testing).
       * **Delete transferred files** : Deletes files after successful transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.

**Note:** If you select a deletion option, the service account must have **Storage Object Admin** role instead of Storage Object Viewer. Update IAM permissions accordingly.
     * **Maximum File Age** : Include files modified in the last number of days. Default is 180 days.

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).

     * **Ingestion labels** : The label to be applied to the events from this feed.

  9. Click **Next**.

  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
action | metadata.description | The value of the action field from the raw log.  
actor.name | principal.user.user_display_name | The value of the actor.name field from the raw log.  
attributes.accountName | principal.user.group_identifiers | The value of the attributes.accountName field from the raw log.  
attributes.appId | target.asset_id | "App ID: " concatenated with the value of the attributes.appId field from the raw log.  
attributes.attributeName | additional.fields[0].value.string_value | The value of the attributes.attributeName field from the raw log, placed within an additional.fields object. The key is set to "Attribute Name".  
attributes.attributeValue | additional.fields[1].value.string_value | The value of the attributes.attributeValue field from the raw log, placed within an additional.fields object. The key is set to "Attribute Value".  
attributes.cloudAppName | target.application | The value of the attributes.cloudAppName field from the raw log.  
attributes.hostName | target.hostname, target.asset.hostname | The value of the attributes.hostName field from the raw log.  
attributes.interface | additional.fields[2].value.string_value | The value of the attributes.interface field from the raw log, placed within an additional.fields object. The key is set to "Interface".  
attributes.operation | security_result.action_details | The value of the attributes.operation field from the raw log.  
attributes.previousValue | additional.fields[3].value.string_value | The value of the attributes.previousValue field from the raw log, placed within an additional.fields object. The key is set to "Previous Value".  
attributes.provisioningResult | security_result.detection_fields.value | The value of the attributes.provisioningResult field from the raw log, placed within a security_result.detection_fields object. The key is set to "Provisioning Result".  
attributes.sourceId | principal.labels[0].value | The value of the attributes.sourceId field from the raw log, placed within a principal.labels object. The key is set to "Source Id".  
attributes.sourceName | principal.labels[1].value | The value of the attributes.sourceName field from the raw log, placed within a principal.labels object. The key is set to "Source Name".  
auditClassName | metadata.product_event_type | The value of the auditClassName field from the raw log.  
created | metadata.event_timestamp.seconds, metadata.event_timestamp.nanos | The value of the created field from the raw log, converted to timestamp if instant.epochSecond is not present.  
id | metadata.product_log_id | The value of the id field from the raw log.  
instant.epochSecond | metadata.event_timestamp.seconds | The value of the instant.epochSecond field from the raw log, used for timestamp.  
ipAddress | principal.asset.ip, principal.ip | The value of the ipAddress field from the raw log.  
interface | additional.fields[0].value.string_value | The value of the interface field from the raw log, placed within an additional.fields object. The key is set to "interface".  
loggerName | intermediary.application | The value of the loggerName field from the raw log.  
message | metadata.description, security_result.description | Used for various purposes, including setting the description in metadata and security_result, and extracting XML content.  
name | security_result.description | The value of the name field from the raw log.  
operation | target.resource.attribute.labels[0].value, metadata.product_event_type | The value of the operation field from the raw log, placed within a target.resource.attribute.labels object. The key is set to "operation". Also used for metadata.product_event_type.  
org | principal.administrative_domain | The value of the org field from the raw log.  
pod | principal.location.name | The value of the pod field from the raw log.  
referenceClass | additional.fields[1].value.string_value | The value of the referenceClass field from the raw log, placed within an additional.fields object. The key is set to "referenceClass".  
referenceId | additional.fields[2].value.string_value | The value of the referenceId field from the raw log, placed within an additional.fields object. The key is set to "referenceId".  
sailPointObjectName | additional.fields[3].value.string_value | The value of the sailPointObjectName field from the raw log, placed within an additional.fields object. The key is set to "sailPointObjectName".  
serverHost | principal.hostname, principal.asset.hostname | The value of the serverHost field from the raw log.  
stack | additional.fields[4].value.string_value | The value of the stack field from the raw log, placed within an additional.fields object. The key is set to "Stack".  
status | security_result.severity_details | The value of the status field from the raw log.  
target | additional.fields[4].value.string_value | The value of the target field from the raw log, placed within an additional.fields object. The key is set to "target".  
target.name | principal.user.userid | The value of the target.name field from the raw log.  
technicalName | security_result.summary | The value of the technicalName field from the raw log.  
thrown.cause.message | xml_body, detailed_message | The value of the thrown.cause.message field from the raw log, used to extract XML content.  
thrown.message | xml_body, detailed_message | The value of the thrown.message field from the raw log, used to extract XML content.  
trackingNumber | additional.fields[5].value.string_value | The value of the trackingNumber field from the raw log, placed within an additional.fields object. The key is set to "Tracking Number".  
type | metadata.product_event_type | The value of the type field from the raw log.  
_version | metadata.product_version | The value of the _version field from the raw log.  
N/A | metadata.event_timestamp | Derived from instant.epochSecond or created fields.  
N/A | metadata.event_type | Determined by parser logic based on various fields, including has_principal_user, has_target_application, technicalName, and action. Default value is "GENERIC_EVENT".  
N/A | metadata.log_type | Set to "SAILPOINT_IAM".  
N/A | metadata.product_name | Set to "IAM".  
N/A | metadata.vendor_name | Set to "SAILPOINT".  
N/A | extensions.auth.type | Set to "AUTHTYPE_UNSPECIFIED" in certain conditions.  
N/A | target.resource.attribute.labels[0].key | Set to "operation".  
`actor.name` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`target.name` | `event.idm.read_only_udm.target.user.userid` | Mapped from changelog  
`attributes.hostName` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`attributes.info` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`synced` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`objects` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`details` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`attributes.attributeValue` | `target.group.attribute.labels` | Mapped from changelog  
`attributes.accountName` | `principal.user.attribute.labels` | Mapped from changelog  
`interface", "referenceClass", "referenceId", "sailPointObjectName", and "target` | `additional.fields` | Mapped from changelog  
`serverHost" and "server` | `principal.hostname` | Mapped from changelog  
`operation` | `target.attribute.labels` | Mapped from changelog  
`metadata.event_type` | `USER_CHANGE_PASSWORD` | Mapped from changelog  
`metadata.event_type` | `USER_DELETION` | Mapped from changelog  
`metadata.event_type` | `USER_RESOURCE_ACCESS` | Mapped from changelog  
`metadata.event_type` | `USER_LOGIN` | Mapped from changelog  
`metadata.event_type` | `USER_RESOURCE_UPDATE_PERMISSIONS` | Mapped from changelog  
`metadata.event_type` | `USER_RESOURCE_UPDATE_CONTENT` | Mapped from changelog  
`metadata.event_type` | `USER_LOGOUT` | Mapped from changelog  
`metadata.event_type` | `USER_CREATION` | Mapped from changelog  
`metadata.event_type` | `USER_CHANGE_PERMISSIONS` | Mapped from changelog  
`metadata.event_type` | `USER_RESOURCE_CREATION` | Mapped from changelog  
`metadata.event_type` | `EMAIL_TRANSACTION` | Mapped from changelog  
`stack", "attributes.interface", "trackingNumber", "attributes.accountUuid", "attributes.previousValue", "attributes.attributeName", and "attributes.attributeValue` | `additional.fields` | Mapped from changelog  
`attributes.sourceId" and "attributes.sourceName` | `principal.labels` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sailpoint-iam-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
