---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/citrix-analytics/
title: Collect Citrix Analytics logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:42:59.063727+00:00
---

# Collect Citrix Analytics logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/citrix-analytics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Citrix Analytics logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Citrix Analytics logs to Google Security Operations using Google Cloud Storage. Citrix Analytics for Performance (Cloud Software Group) provides aggregated performance data from Citrix Virtual Apps and Desktops environments, enabling you to fetch session, machine, and user data through the OData API. Citrix Analytics for Security provides risk insights and data source events that can be exported through Kafka-based SIEM integration.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * Privileged access to a Citrix Analytics for Performance tenant
  * Citrix Cloud API credentials (Client ID, Client Secret, Customer ID)



## Collect Citrix Analytics API credentials

### Get Citrix Cloud API credentials

  1. Sign in to the [Citrix Cloud Console](https://citrix.cloud.com/).
  2. Click the menu icon in the upper left corner of the screen.
  3. Select **Identity and Access Management** from the menu.
  4. Select the **API Access** tab.
  5. Click **Create Client**.
  6. Copy and save the following details in a secure location: 
     * **Client ID**
     * **Client Secret**
     * **Customer ID** (located in the Citrix Cloud URL or the IAM page)



### Determine API base URL

The OData API base URL depends on your Citrix Cloud region:

Region | API Base URL  
---|---  
United States | `https://api.cloud.com/casodata`  
European Union | `https://api.eu.cloud.com/casodata`  
Asia Pacific South | `https://api.ap-s.cloud.com/casodata`  
**Note:** The implementation uses a Citrix Cloud bearer token for authentication. The token is obtained by calling the Citrix Cloud OAuth2 endpoint with your Client ID and Client Secret.

### Verify permissions

To verify the account has the required permissions:

  1. Sign in to [Citrix Cloud](https://citrix.cloud.com/).
  2. Go to **Identity and Access Management > Administrators**.
  3. Verify that the account used to create API credentials has **Full access** or **Custom access** with Citrix Analytics for Performance permissions enabled.
  4. If you cannot see the required permissions, contact your Citrix Cloud administrator to grant access.



### Test API access

  * Test your credentials before proceeding with the integration:
        
        CITRIX_CUSTOMER_ID="your-customer-id"
        CITRIX_CLIENT_ID="your-client-id"
        CITRIX_CLIENT_SECRET="your-client-secret"
        
        # Get bearer token
        TOKEN=$(curl -s -X POST \
          "https://api.cloud.com/cctrustoauth2/${CITRIX_CUSTOMER_ID}/tokens/clients" \
          -H "Content-Type: application/x-www-form-urlencoded" \
          -d "grant_type=client_credentials&client_id=${CITRIX_CLIENT_ID}&client_secret=${CITRIX_CLIENT_SECRET}" \
          | python3 -c "import sys,json; print(json.load(sys.stdin)['access_token'])")
        
        # Test OData API access
        curl -v -H "Authorization: CwsAuth bearer=${TOKEN}" \
          -H "Citrix-CustomerId: ${CITRIX_CUSTOMER_ID}" \
          -H "Accept: application/json" \
          "https://api.cloud.com/casodata/sessions?\$top=1"
        




## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `citrix-analytics-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Create service account for Cloud Run function

The Cloud Run function needs a service account with permissions to write to GCS bucket and be invoked by Pub/Sub.

### Create service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `citrix-analytics-collector-sa`
     * **Service account description** : Enter `Service account for Cloud Run function to collect Citrix Analytics logs`
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
  2. Click your bucket name.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `citrix-analytics-collector-sa@PROJECT_ID.iam.gserviceaccount.com`)
     * **Assign roles** : Select **Storage Object Admin**
  6. Click **Save**.



## Create Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `citrix-analytics-trigger`
     * Leave other settings as default
  4. Click **Create**.



## Create Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from the Citrix Analytics OData API and write them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `citrix-analytics-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose the topic `citrix-analytics-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select the service account `citrix-analytics-collector-sa`
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `citrix-analytics-logs` | GCS bucket name  
`GCS_PREFIX` | `citrix_analytics` | Prefix for log files  
`STATE_KEY` | `citrix_analytics/state.json` | State file path  
`CITRIX_CLIENT_ID` | `your-client-id` | Citrix Cloud Client ID  
`CITRIX_CLIENT_SECRET` | `your-client-secret` | Citrix Cloud Client Secret  
`CITRIX_CUSTOMER_ID` | `your-customer-id` | Citrix Cloud Customer ID  
`API_BASE` | `https://api.cloud.com/casodata` | OData API base URL  
`ENTITIES` | `sessions,machines,users` | Entity types to collect  
`TOP_N` | `1000` | Records per page  
`LOOKBACK_MINUTES` | `75` | Initial lookback period  
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

     * **main.py:**
           
           import functions_framework
           from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
           import json
           import os
           import urllib3
           from datetime import datetime, timedelta, timezone
           import urllib.parse
           import time
           
           # Initialize HTTP client with timeouts
           http = urllib3.PoolManager(
               timeout=urllib3.Timeout(connect=5.0, read=30.0),
               retries=False,
           )
           
           # Initialize Storage client
           storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
           
           CITRIX_TOKEN_URL_TMPL = "https://api.cloud.com/cctrustoauth2/{customerid}/tokens/clients"
           DEFAULT_API_BASE = "https://api.cloud.com/casodata"
           
           @functions_framework.cloud_event
           def main(cloud_event):
               """
               Cloud Run function triggered by Pub/Sub to fetch logs
               from Citrix Analytics OData API and write to GCS.
           
               Args:
                   cloud_event: CloudEvent object containing Pub/Sub message
               """
           
               # Get environment variables
               bucket_name = os.environ.get('GCS_BUCKET')
               prefix = os.environ.get('GCS_PREFIX', 'citrix_analytics').strip('/')
               state_key = os.environ.get('STATE_KEY') or f"{prefix}/state.json"
               customer_id = os.environ.get('CITRIX_CUSTOMER_ID')
               client_id = os.environ.get('CITRIX_CLIENT_ID')
               client_secret = os.environ.get('CITRIX_CLIENT_SECRET')
               api_base = os.environ.get('API_BASE', DEFAULT_API_BASE)
               entities = [e.strip() for e in os.environ.get('ENTITIES', 'sessions,machines,users').split(',') if e.strip()]
               top_n = int(os.environ.get('TOP_N', '1000'))
               lookback_minutes = int(os.environ.get('LOOKBACK_MINUTES', '75'))
           
               if not all([bucket_name, customer_id, client_id, client_secret]):
                   print('Error: Missing required environment variables')
                   return
           
               try:
                   # Get GCS bucket
                   bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
           
                   # Determine target hour to collect
                   now = datetime.now(timezone.utc)
                   fallback_target = (now - timedelta(minutes=lookback_minutes)).replace(minute=0, second=0, microsecond=0)
           
                   # Load state (last processed timestamp)
                   state = load_state(bucket, state_key)
                   last_processed_str = [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get('last_hour_utc')
           
                   if last_processed_str:
                       last_processed = datetime.fromisoformat(last_processed_str.replace('Z', '+00:00')).replace(tzinfo=None)
                       target_hour = last_processed + timedelta(hours=1)
                   else:
                       target_hour = fallback_target
           
                   print(f'Processing logs for hour: {target_hour.isoformat()}Z')
           
                   # Get authentication token
                   token = get_citrix_token(customer_id, client_id, client_secret)
                   headers = {
                       'Authorization': f'CwsAuth bearer={token}',
                       'Citrix-CustomerId': customer_id,
                       'Accept': 'application/json',
                       'Content-Type': 'application/json',
                   }
           
                   total_records = 0
           
                   # Process each entity type
                   for entity in entities:
                       records = []
                       for row in fetch_odata_entity(entity, target_hour, top_n, headers, api_base):
                           enriched_record = {
                               'citrix_entity': entity,
                               'citrix_hour_utc': target_hour.isoformat() + 'Z',
                               'collection_timestamp': datetime.now(timezone.utc).isoformat() + 'Z',
                               'raw': row
                           }
                           records.append(enriched_record)
           
                           # Write in batches to avoid memory issues
                           if len(records) >= 1000:
                               blob_name = f"{prefix}/{[entity](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.acl.ACL.html#google_cloud_storage_acl_ACL_entity)}/year={target_hour.year:04d}/month={target_hour.month:02d}/day={target_hour.day:02d}/hour={target_hour.hour:02d}/part-{datetime.now(timezone.utc).strftime('%Y%m%d%H%M%S%f')}.ndjson"
                               write_ndjson_to_gcs(bucket, blob_name, records)
                               total_records += len(records)
                               records = []
           
                       # Write remaining records
                       if records:
                           blob_name = f"{prefix}/{[entity](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.acl.ACL.html#google_cloud_storage_acl_ACL_entity)}/year={target_hour.year:04d}/month={target_hour.month:02d}/day={target_hour.day:02d}/hour={target_hour.hour:02d}/part-{datetime.now(timezone.utc).strftime('%Y%m%d%H%M%S%f')}.ndjson"
                           write_ndjson_to_gcs(bucket, blob_name, records)
                           total_records += len(records)
           
                   # Update state file
                   save_state(bucket, state_key, {'last_hour_utc': target_hour.isoformat() + 'Z'})
           
                   print(f'Successfully processed {total_records} records for hour {target_hour.isoformat()}Z')
           
               except Exception as e:
                   print(f'Error processing logs: {str(e)}')
                   raise
           
           def get_citrix_token(customer_id, client_id, client_secret):
               """Get Citrix Cloud authentication token."""
               url = CITRIX_TOKEN_URL_TMPL.format(customerid=customer_id)
               payload = {
                   'grant_type': 'client_credentials',
                   'client_id': client_id,
                   'client_secret': client_secret,
               }
               data = urllib.parse.urlencode(payload).encode('utf-8')
           
               response = http.request(
                   'POST',
                   url,
                   body=data,
                   headers={
                       'Accept': 'application/json',
                       'Content-Type': 'application/x-www-form-urlencoded',
                   }
               )
           
               if response.status != 200:
                   print(f'Token request failed with status {response.status}')
                   print(f'Response: {response.data.decode("utf-8")}')
                   raise Exception(f'Failed to get Citrix token: HTTP {response.status}')
           
               token_response = json.loads(response.data.decode('utf-8'))
               return token_response['access_token']
           
           def fetch_odata_entity(entity, when_utc, top, headers, api_base):
               """Fetch data from Citrix Analytics OData API with pagination and rate limiting."""
               year = when_utc.year
               month = when_utc.month
               day = when_utc.day
               hour = when_utc.hour
           
               base_url = f"{api_base.rstrip('/')}/{[entity](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.acl.ACL.html#google_cloud_storage_acl_ACL_entity)}?year={year:04d}&month={month:02d}&day={day:02d}&hour={hour:02d}"
               skip = 0
               backoff = 1.0
           
               while True:
                   url = f"{base_url}&$top={top}&$skip={skip}"
           
                   response = http.request('GET', url, headers=headers)
           
                   # Handle rate limiting with exponential backoff
                   if response.status == 429:
                       retry_after = int(response.headers.get('Retry-After', str(int(backoff))))
                       print(f'Rate limited (429). Retrying after {retry_after}s...')
                       time.sleep(retry_after)
                       backoff = min(backoff * 2, 30.0)
                       continue
           
                   backoff = 1.0
           
                   if response.status != 200:
                       print(f'HTTP Error: {response.status}')
                       response_text = response.data.decode('utf-8')
                       print(f'Response body: {response_text}')
                       return
           
                   data = json.loads(response.data.decode('utf-8'))
                   items = data.get('value', [])
           
                   if not items:
                       break
           
                   for item in items:
                       yield item
           
                   if len(items) < top:
                       break
           
                   skip += top
           
           def load_state(bucket, key):
               """Load state from GCS."""
               try:
                   blob = bucket.blob(key)
                   if blob.exists():
                       state_data = blob.[download_as_text](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_download_as_text)()
                       return json.loads(state_data)
               except Exception as e:
                   print(f'Warning: Could not load state: {str(e)}')
               return {}
           
           def save_state(bucket, key, state):
               """Save state to GCS."""
               try:
                   blob = bucket.blob(key)
                   blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
                       json.dumps(state, separators=(',', ':')),
                       content_type='application/json'
                   )
               except Exception as e:
                   print(f'Warning: Could not save state: {str(e)}')
           
           def write_ndjson_to_gcs(bucket, key, records):
               """Write records as NDJSON to GCS."""
               body_lines = []
               for record in records:
                   json_line = json.dumps(record, separators=(',', ':'), ensure_ascii=False)
                   body_lines.append(json_line)
           
               body = ('\n'.join(body_lines) + '\n').encode('utf-8')
           
               blob = bucket.blob(key)
               blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(body, content_type='application/x-ndjson')
           

     * **requirements.txt:**
           
           functions-framework==3.*
           google-cloud-storage==2.*
           urllib3>=2.0.0
           

  3. Click **Deploy** to save and deploy the function.

  4. Wait for deployment to complete (2-3 minutes).

**Note:** This script is provided as an example and is not officially supported. We welcome feedback about how we can improve it. To submit feedback, click **Send Feedback** > **Google SecOps Security Product Feedback** on this page.



## Create Cloud Scheduler job

Cloud Scheduler will publish messages to the Pub/Sub topic at regular intervals, triggering the Cloud Run function.

  1. In the **GCP Console** , go to **Cloud Scheduler**.
  2. Click **Create Job**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | `citrix-analytics-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the topic `citrix-analytics-trigger`  
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
  5. Click on the function name `citrix-analytics-collector`.
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         Processing logs for hour: YYYY-MM-DDTHH:00:00Z
         Successfully processed X records for hour YYYY-MM-DDTHH:00:00Z
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click your bucket name.

  10. Navigate to the prefix folder `citrix_analytics/`.

  11. Verify that new `.ndjson` files were created with the current timestamp.




If you see errors in the logs:

  * **HTTP 401** : Check API credentials in environment variables
  * **HTTP 403** : Verify account has required permissions in Citrix Cloud
  * **HTTP 429** : Rate limiting - function will automatically retry with backoff
  * **Missing environment variables** : Check all required variables are set



## Configure a feed in Google SecOps to ingest Citrix Analytics logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Citrix Analytics logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Citrix Analytics** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Don't use service accounts from other documentation or examples.
  9. Click **Next**.

  10. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://citrix-analytics-logs/citrix_analytics/
           

       * Replace: 
         * `citrix-analytics-logs`: Your GCS bucket name.
         * `citrix_analytics`: Optional prefix/folder path where logs are stored (leave empty for root).
**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never** : Never deletes any files after transfers (recommended for testing).
       * **Delete transferred files** : Deletes files after successful transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.
**Note:** If you select a deletion option, the service account must have **Storage Object Admin** role instead of **Storage Object Viewer**. Update IAM permissions accordingly.
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

**Note:** If you plan to use the deletion option "Delete transferred files" or "Delete transferred files and empty directories," grant **Storage Object Admin** role instead of **Storage Object Viewer**.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`occurrence_event_type` | `extensions.auth.type` | Mapped: `Session.Logon` → `AUTHTYPE_UNSPECIFIED`, `Session.End` → `AUTHTYPE_UNSPECIFIED`  
`server_name` | `intermediary.asset.hostname` | Directly mapped  
`server_name` | `intermediary.hostname` | Directly mapped  
`event_type` | `metadata.description` | Directly mapped  
`timestamp` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`udm_event_type` | `metadata.event_type` | Mapped: `"USER_LOGIN", "USER_LOGOUT"` → `GENERIC_EVENT`  
`tenant_id` | `metadata.product_deployment_id` | Directly mapped  
`occurrence_event_type` | `metadata.product_event_type` | Directly mapped  
`event_id` | `metadata.product_log_id` | Directly mapped  
`product` | `metadata.product_name` | Directly mapped  
`product_version` | `metadata.product_version` | Directly mapped  
`ui_link` | `metadata.url_back_to_product` | Directly mapped  
`session_key` | `network.session_id` | Directly mapped  
`domain` | `principal.administrative_domain` | Directly mapped  
`device_id` | `principal.asset.hostname` | Directly mapped  
`client_ip` | `principal.asset.ip` | Merged  
`vulnerability` | `principal.asset.vulnerabilities` | Merged  
`device_id` | `principal.hostname` | Directly mapped  
`client_ip` | `principal.ip` | Merged  
`os_name` | `principal.platform` | Mapped values (6 total, e.g. `(?i)windows` → `WINDOWS`, `(?i)windows` → `MAC`, `(?i)windows`...  
`os_extra_info` | `principal.platform_patch_level` | Directly mapped  
`os_version` | `principal.platform_version` | Directly mapped  
`entity_id` | `principal.user.email_addresses` | Mapped: `^.+@.+$` → `entity_id`  
`entity_type` | `principal.user.email_addresses` | Mapped: `user` → `entity_id`  
`session_user_name` | `principal.user.user_display_name` | Directly mapped  
`entity_id` | `principal.user.userid` | Directly mapped  
`session_user_name` | `principal.user.userid` | Directly mapped  
`alert_message` | `security_result.action_details` | Directly mapped  
`analytic` | `security_result.analytics_metadata` | Merged  
`category` | `security_result.category` | Merged  
`indicator_category` | `security_result.category` | Mapped: `Data exfiltration` → `category`  
`indicator_name` | `security_result.description` | Directly mapped  
`label` | `security_result.detection_fields` | Merged  
`label` | `security_result.outcomes` | Merged  
`severity` | `security_result.severity` | Directly mapped  
`app_name` | `target.application` | Directly mapped  
`app_name` | `target.process.file.names` | Merged  
`printer_name` | `target.resource.name` | Directly mapped  
`entity_id` | `target.user.email_addresses` | Mapped: `^.+@.+$` → `entity_id`  
`entity_type` | `target.user.email_addresses` | Mapped: `user` → `entity_id`  
`session_user_name` | `target.user.user_display_name` | Directly mapped  
`entity_id` | `target.user.userid` | Directly mapped  
`session_user_name` | `target.user.userid` | Directly mapped  
N/A | `extensions.auth.type` | Constant: `AUTHTYPE_UNSPECIFIED`  
N/A | `metadata.event_type` | Constant: `GENERIC_EVENT`  
N/A | `metadata.vendor_name` | Constant: `CITRIX_ANALYTICS`  
N/A | `principal.platform` | Constant: `WINDOWS`  
N/A | `security_result.confidence_score` | Constant: `risk_probability`  
N/A | `security_result.risk_score` | Constant: `cur_riskscore`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/citrix-analytics-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
