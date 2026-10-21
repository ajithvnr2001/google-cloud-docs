---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/citrix-ms/
title: Collect Citrix Monitor Service logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T07:28:28.496959+00:00
---

# Collect Citrix Monitor Service logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/citrix-ms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Citrix Monitor Service logs

**Parser Version:** 2.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Citrix Monitor Service logs to Google Security Operations using Google Cloud Storage. Citrix Monitor Service is part of Citrix DaaS (formerly Citrix Virtual Apps and Desktops Service) and provides an OData v4 API for monitoring data about machines, sessions, connections, applications, and users across your Citrix environment. A Cloud Run function polls the Citrix Monitor Service OData API on a schedule and writes the collected logs to a GCS bucket, from which Google SecOps ingests them.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run functions, Pub/Sub topics, and Cloud Scheduler jobs
  * Permissions to create service accounts and manage IAM roles
  * Privileged access to Citrix Cloud tenant with administrator role
  * Citrix Cloud API credentials (Client ID, Client Secret, Customer ID)



## Collect Citrix Monitor Service API credentials

  1. Sign in to the [Citrix Cloud Console](https://citrix.cloud.com/).
  2. Go to **Identity and Access Management > API Access**.
  3. Click **Create Client**.
  4. Copy and save in a secure location the following details:

     * **Client ID**
     * **Client Secret**
     * **Customer ID** (visible at the top of the Citrix Cloud console)
     * **API Base URL** (based on your region): 
       * **US/EU/AP-S** : `https://api.cloud.com`
       * **Japan** : `https://api.citrixcloud.jp`
       * **US Gov** : `https://api.cloud.us`
**Note:** Use the endpoint based on the geographical region you selected while accessing the Citrix Monitor Service data for DaaS. For example, US/EU/AP-S region uses `https://api.cloud.com/monitorodata`, Japan region uses `https://api.citrixcloud.jp/monitorodata`, and US Gov region uses `https://api.cloud.us/monitorodata`.



### Test API access

  * Test your credentials before proceeding with the integration:
        
        # Replace with your actual credentials
        CITRIX_CUSTOMER_ID="your-customer-id"
        CITRIX_CLIENT_ID="your-client-id"
        CITRIX_CLIENT_SECRET="your-client-secret"
        API_BASE="https://api.cloud.com"
        
        # Get bearer token
        TOKEN=$(curl -s -X POST "${API_BASE}/cctrustoauth2/${CITRIX_CUSTOMER_ID}/tokens/clients" \
          -H "Content-Type: application/x-www-form-urlencoded" \
          -d "grant_type=client_credentials&client_id=${CITRIX_CLIENT_ID}&client_secret=${CITRIX_CLIENT_SECRET}" \
          | python3 -c "import sys,json; print(json.load(sys.stdin)['access_token'])")
        
        # Test Monitor OData API access
        curl -v "${API_BASE}/monitorodata/Machines?\$top=1" \
          -H "Authorization: CWSAuth bearer=${TOKEN}" \
          -H "Citrix-CustomerId: ${CITRIX_CUSTOMER_ID}" \
          -H "Accept: application/json"
        




If you receive an HTTP 200 response with JSON data, your credentials are working correctly.

## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `citrix-monitor-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Create service account for Cloud Run function

The Cloud Run function needs a service account with permissions to write to GCS bucket.

### Create service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `citrix-monitor-collector-sa`.
     * **Service account description** : Enter `Service account for Cloud Run function to collect Citrix Monitor Service logs`.
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



### Grant IAM permissions on GCS bucket

Grant the service account write permissions on the GCS bucket:

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (`citrix-monitor-collector-sa@PROJECT_ID.iam.gserviceaccount.com`).
     * **Assign roles** : Select **Storage Object Admin**.
  6. Click **Save**.



## Create Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `citrix-monitor-trigger`.
     * Leave other settings as default.
  4. Click **Create**.



## Create Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from [Citrix Monitor Service OData API](https://developer-docs.citrix.com/en-us/monitor-service-odata-api/) and write them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `citrix-monitor-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose the topic (`citrix-monitor-trigger`).
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select the service account (`citrix-monitor-collector-sa`).
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value  
---|---  
`GCS_BUCKET` | `citrix-monitor-logs`  
`GCS_PREFIX` | `citrix_monitor`  
`STATE_KEY` | `citrix_monitor/state.json`  
`CITRIX_CLIENT_ID` | `your-client-id`  
`CITRIX_CLIENT_SECRET` | `your-client-secret`  
`CITRIX_CUSTOMER_ID` | `your-customer-id`  
`API_BASE` | `https://api.cloud.com`  
`ENTITIES` | `Machines,Sessions,Connections,Applications,Users`  
`PAGE_SIZE` | `1000`  
`LOOKBACK_MINUTES` | `75`  
`USE_TIME_FILTER` | `true`  
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

  16. After the service is created, the **inline code editor** will open automatically.




### Add function code

  1. Enter **main** in the **Function entry point** field.
  2. In the inline code editor, create two files:

     * **main.py:**
           
           import functions_framework
           from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
           import json
           import os
           import urllib3
           from datetime import datetime, timedelta, timezone
           import uuid
           import time
           
           # Citrix Cloud OAuth2 endpoint template
           TOKEN_URL_TMPL = "{api_base}/cctrustoauth2/{customerid}/tokens/clients"
           DEFAULT_API_BASE = "https://api.cloud.com"
           MONITOR_BASE_PATH = "/monitorodata"
           
           # Initialize HTTP client with timeouts
           http = urllib3.PoolManager(
                   timeout=urllib3.Timeout(connect=5.0, read=30.0),
                   retries=False,
           )
           
           # Initialize Storage client
           storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
           
           def http_post_form(url, data_dict):
                   """POST form data to get authentication token."""
                   encoded_data = urllib3.request.urlencode(data_dict)
                   response = http.request(
                           'POST',
                           url,
                           body=encoded_data,
                           headers={
                                   'Accept': 'application/json',
                                   'Content-Type': 'application/x-www-form-urlencoded'
                           }
                   )
                   return json.loads(response.data.decode('utf-8'))
           
           def http_get_json(url, headers):
                   """GET JSON data from API endpoint."""
                   response = http.request('GET', url, headers=headers)
                   if response.status == 429:
                           retry_after = int(response.headers.get('Retry-After', '10'))
                           print(f"Rate limited (429). Retrying after {retry_after}s...")
                           time.sleep(retry_after)
                           response = http.request('GET', url, headers=headers)
                   if response.status != 200:
                           raise Exception(f"HTTP {response.status}: {response.data.decode('utf-8')[:500]}")
                   return json.loads(response.data.decode('utf-8'))
           
           def get_citrix_token(api_base, customer_id, client_id, client_secret):
                   """Get Citrix Cloud authentication token."""
                   url = TOKEN_URL_TMPL.format(
                           api_base=api_base.rstrip('/'),
                           customerid=customer_id
                   )
                   payload = {
                           'grant_type': 'client_credentials',
                           'client_id': client_id,
                           'client_secret': client_secret
                   }
                   response = http_post_form(url, payload)
                   return response['access_token']
           
           def build_entity_url(api_base, entity, filter_query=None, top=None):
                   """Build OData URL with optional filter and pagination."""
                   base = api_base.rstrip('/') + MONITOR_BASE_PATH + '/' + entity
                   params = []
                   if filter_query:
                           encoded_filter = urllib3.request.urlencode({'$filter': filter_query})[9:]
                           params.append('$filter=' + encoded_filter)
                   if top:
                           params.append('$top=' + str(top))
                   return base + ('?' + '&'.join(params) if params else '')
           
           def fetch_entity_rows(entity, start_iso=None, end_iso=None, page_size=1000, headers=None, api_base=DEFAULT_API_BASE):
                   """Fetch entity data with optional time filtering and OData pagination."""
                   first_url = None
                   if start_iso and end_iso:
                           filter_query = f"(ModifiedDate ge {start_iso} and ModifiedDate lt {end_iso})"
                           first_url = build_entity_url(api_base, entity, filter_query, page_size)
                   else:
                           first_url = build_entity_url(api_base, entity, None, page_size)
           
                   url = first_url
                   while url:
                           try:
                                   data = http_get_json(url, headers)
                                   items = data.get('value', [])
                                   for item in items:
                                           yield item
                                   url = data.get('@odata.nextLink')
                           except Exception as e:
                                   if 'Bad Request' in str(e) and start_iso and end_iso:
                                           print(f"ModifiedDate filter not supported for {[entity](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.acl.ACL.html#google_cloud_storage_acl_ACL_entity)}, falling back to unfiltered query")
                                           url = build_entity_url(api_base, entity, None, page_size)
                                           start_iso = None
                                           end_iso = None
                                           continue
                                   else:
                                           raise
           
           def load_state(bucket, key):
                   """Read the last processed timestamp from GCS state file."""
                   try:
                           blob = bucket.blob(key)
                           if blob.exists():
                                   content = blob.[download_as_text](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_download_as_text)()
                                   state = json.loads(content)
                                   timestamp_str = [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get('last_hour_utc')
                                   if timestamp_str:
                                           return datetime.fromisoformat(timestamp_str.replace('Z', '+00:00')).replace(tzinfo=None)
                   except Exception as e:
                           print(f"Warning: Could not load state: {str(e)}")
                   return None
           
           def save_state(bucket, key, dt_utc):
                   """Write the current processed timestamp to GCS state file."""
                   state = {'last_hour_utc': dt_utc.isoformat() + 'Z'}
                   blob = bucket.blob(key)
                   blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
                           json.dumps(state, separators=(',', ':')),
                           content_type='application/json'
                   )
           
           def write_ndjson_to_gcs(bucket, key, rows):
                   """Write rows as NDJSON to GCS."""
                   body_lines = []
                   for row in rows:
                           json_line = json.dumps(row, separators=(',', ':'), ensure_ascii=False)
                           body_lines.append(json_line)
                   body = '\n'.join(body_lines) + '\n'
                   blob = bucket.blob(key)
                   blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(body, content_type='application/x-ndjson')
           
           @functions_framework.cloud_event
           def main(cloud_event):
                   """
                   Cloud Run function triggered by Pub/Sub to fetch Citrix Monitor Service logs and write to GCS.
           
                   Args:
                           cloud_event: CloudEvent object containing Pub/Sub message
                   """
           
                   # Get environment variables
                   bucket_name = os.environ.get('GCS_BUCKET')
                   prefix = os.environ.get('GCS_PREFIX', 'citrix_monitor').strip('/')
                   state_key = os.environ.get('STATE_KEY') or f"{prefix}/state.json"
                   customer_id = os.environ.get('CITRIX_CUSTOMER_ID')
                   client_id = os.environ.get('CITRIX_CLIENT_ID')
                   client_secret = os.environ.get('CITRIX_CLIENT_SECRET')
                   api_base = os.environ.get('API_BASE', DEFAULT_API_BASE)
                   entities = [e.strip() for e in os.environ.get('ENTITIES', 'Machines,Sessions,Connections,Applications,Users').split(',') if e.strip()]
                   page_size = int(os.environ.get('PAGE_SIZE', '1000'))
                   lookback_minutes = int(os.environ.get('LOOKBACK_MINUTES', '75'))
                   use_time_filter = os.environ.get('USE_TIME_FILTER', 'true').lower() == 'true'
           
                   if not all([bucket_name, customer_id, client_id, client_secret]):
                           print('Error: Missing required environment variables')
                           return
           
                   try:
                           # Get GCS bucket
                           bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
           
                           # Time window calculation
                           now = datetime.utcnow()
                           fallback_hour = (now - timedelta(minutes=lookback_minutes)).replace(minute=0, second=0, microsecond=0)
                           last_processed = load_state(bucket, state_key)
                           target_hour = (last_processed + timedelta(hours=1)) if last_processed else fallback_hour
                           start_iso = target_hour.isoformat() + 'Z'
                           end_iso = (target_hour + timedelta(hours=1)).isoformat() + 'Z'
           
                           # Authentication
                           token = get_citrix_token(api_base, customer_id, client_id, client_secret)
                           headers = {
                                   'Authorization': f'CWSAuth bearer={token}',
                                   'Citrix-CustomerId': customer_id,
                                   'Accept': 'application/json',
                                   'Accept-Encoding': 'gzip, deflate, br',
                                   'User-Agent': 'citrix-monitor-gcs-collector/1.0'
                           }
           
                           total_records = 0
           
                           # Process each entity type
                           for entity in entities:
                                   rows_batch = []
                                   try:
                                           entity_generator = fetch_entity_rows(
                                                   entity=entity,
                                                   start_iso=start_iso if use_time_filter else None,
                                                   end_iso=end_iso if use_time_filter else None,
                                                   page_size=page_size,
                                                   headers=headers,
                                                   api_base=api_base
                                           )
           
                                           for row in entity_generator:
                                                   rows_batch.append(row)
           
                                                   # Write in batches to avoid memory issues
                                                   if len(rows_batch) >= 1000:
                                                           gcs_key = f"{prefix}/{[entity](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.acl.ACL.html#google_cloud_storage_acl_ACL_entity)}/year={target_hour.year:04d}/month={target_hour.month:02d}/day={target_hour.day:02d}/hour={target_hour.hour:02d}/part-{uuid.uuid4().hex}.ndjson"
                                                           write_ndjson_to_gcs(bucket, gcs_key, rows_batch)
                                                           total_records += len(rows_batch)
                                                           rows_batch = []
           
                                   except Exception as ex:
                                           print(f"Error processing entity {[entity](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.acl.ACL.html#google_cloud_storage_acl_ACL_entity)}: {str(ex)}")
                                           continue
           
                                   # Write remaining records
                                   if rows_batch:
                                           gcs_key = f"{prefix}/{[entity](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.acl.ACL.html#google_cloud_storage_acl_ACL_entity)}/year={target_hour.year:04d}/month={target_hour.month:02d}/day={target_hour.day:02d}/hour={target_hour.hour:02d}/part-{uuid.uuid4().hex}.ndjson"
                                           write_ndjson_to_gcs(bucket, gcs_key, rows_batch)
                                           total_records += len(rows_batch)
           
                           # Update state file
                           save_state(bucket, state_key, target_hour)
           
                           print(f"Successfully processed {total_records} records for hour {start_iso}")
                           print(f"Entities processed: {', '.join(entities)}")
           
                   except Exception as e:
                           print(f'Error processing Citrix Monitor logs: {str(e)}')
                           raise
           

**Note:** This script is provided as an example and is not officially supported. We welcome feedback about how we can improve it. To submit feedback, click **Send Feedback > Google SecOps Security Product Feedback** on this page.

     * **requirements.txt:**
           
           functions-framework==3.*
           google-cloud-storage==2.*
           urllib3>=2.0.0
           

  3. Click **Deploy** to save and deploy the function.

  4. Wait for deployment to complete (2-3 minutes).

**Note:** This script is provided as an example and is not officially supported. We welcome feedback about how we can improve it. To submit feedback, click Send Feedback > Google SecOps Security Product Feedback on this page.



## Create Cloud Scheduler job

Cloud Scheduler will publish messages to the Pub/Sub topic at regular intervals, triggering the Cloud Run function.

  1. In the **GCP Console** , go to **Cloud Scheduler**.
  2. Click **Create Job**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | `citrix-monitor-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the topic (`citrix-monitor-trigger`)  
**Message body** | `{}` (empty JSON object)  
  4. Click **Create**.




### Test the integration

  1. In the **Cloud Scheduler** console, find your job.
  2. Click **Force run** to trigger the job manually.
  3. Wait a few seconds.
  4. Go to **Cloud Run > Services**.
  5. Click on the function name (`citrix-monitor-collector`).
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         Successfully processed X records for hour YYYY-MM-DDTHH:MM:SSZ
         Entities processed: Machines, Sessions, Connections, Applications, Users
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click on your bucket name.

  10. Navigate to the prefix folder (`citrix_monitor/`).

  11. Verify that new `.ndjson` files were created.




If you see errors in the logs:

  * **HTTP 401** : Check API credentials in environment variables
  * **HTTP 403** : Verify the Citrix Cloud account has administrator permissions
  * **HTTP 429** : Rate limiting - the function will automatically retry with backoff
  * **Missing environment variables** : Check all required variables are set



## Configure a feed in Google SecOps to ingest Citrix Monitor Service logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Citrix Monitor Service logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Citrix Monitor** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address. You will use it in the next step.

**Note:** Each Google SecOps instance has a unique service account. Do not use service accounts from other documentation or examples.
  9. Click **Next**.

  10. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://citrix-monitor-logs/citrix_monitor/
           

       * Replace: 
         * `citrix-monitor-logs`: Your GCS bucket name.
         * `citrix_monitor`: Optional prefix/folder path where logs are stored (leave empty for root).
**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never** : Never deletes any files after transfers (recommended for testing).
       * **Delete transferred files** : Deletes files after successful transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.
**Note:** If you select a deletion option, the service account must have **Storage Object Admin** role instead of **Storage Object Viewer**. Update IAM permissions accordingly.
     * **Maximum File Age** : Include files modified in the last number of days. Default is 180 days.

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).

     * **Ingestion labels** : The label to be applied to the events from this feed.

  11. Click **Next**.

  12. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




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

**Note:** If you plan to use the deletion option "Delete transferred files" or "Delete transferred files and empty directories," grant **Storage Object Admin** role instead of **Storage Object Viewer**.



## UDM Mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`additional_user_id_label` | `additional.fields` | Merged  
`CreatedDate` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`event_type` | `metadata.event_type` | Directly mapped  
`label_Connection_State` | `metadata.ingestion_labels` | Merged  
`label_Log_On_Duration` | `metadata.ingestion_labels` | Merged  
`label_Session_Key` | `metadata.ingestion_labels` | Merged  
`Machine.AgentVersion` | `metadata.product_version` | Directly mapped  
`Machine.DnsName` | `network.dns_domain` | Directly mapped  
`applicationInstance.Application.BrowserName` | `network.http.user_agent` | Directly mapped  
`CurrentConnectionId` | `network.session_id` | Directly mapped  
`Machine.HostedMachineName` | `principal.administrative_domain` | Directly mapped  
`Machine.Id` | `principal.asset.asset_id` | Directly mapped  
`MachineId` | `principal.asset.asset_id` | Directly mapped  
`Machine.HostingServerName` | `principal.hostname` | Directly mapped  
`Machine.IPAddress` | `principal.ip` | Merged  
`connection.ClientAddress` | `principal.ip` | Merged  
`connection.ConnectedViaIPAddress` | `principal.ip` | Merged  
`user` | `principal.user.email_addresses` | Mapped: `^.+@.+$` → `user`  
`Machine.AssociatedUserFullNames` | `principal.user.user_display_name` | Directly mapped  
`Machine.Sid` | `principal.user.windows_sid` | Directly mapped  
`User.Domain` | `target.administrative_domain` | Directly mapped  
`applicationInstance.Application.Name` | `target.application` | Directly mapped  
`connection.LaunchedViaIPAddress` | `target.ip` | Merged  
`applicationInstance.Application.Path` | `target.process.file.full_path` | Directly mapped  
`Machine.Hash` | `target.process.file.md5` | Directly mapped  
`applicationInstance.Application.AdminFolder` | `target.process.parent_process.file.full_path` | Directly mapped  
`User.Upn` | `target.user.email_addresses` | Merged  
`User.FullName` | `target.user.user_display_name` | Directly mapped  
`User.UserName` | `target.user.userid` | Directly mapped  
`User.Sid` | `target.user.windows_sid` | Directly mapped  
N/A | `metadata.event_type` | Constant: `GENERIC_EVENT`  
N/A | `metadata.product_name` | Constant: `CITRIX_MONITOR`  
N/A | `metadata.vendor_name` | Constant: `CITRIX_MONITOR`  
N/A | `target.platform` | Constant: `WINDOWS`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/citrix-monitor-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
