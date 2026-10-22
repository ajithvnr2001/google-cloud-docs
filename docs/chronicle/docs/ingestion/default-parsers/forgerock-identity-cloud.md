---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/forgerock-identity-cloud/
title: Collect PingOne Advanced Identity Cloud logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:33:25.085220+00:00
---

# Collect PingOne Advanced Identity Cloud logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/forgerock-identity-cloud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect PingOne Advanced Identity Cloud logs

**Parser Version:** 4.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest PingOne Advanced Identity Cloud (formerly ForgeRock Identity Cloud) logs to Google Security Operations using Google Cloud Storage V2.

PingOne Advanced Identity Cloud is a cloud-native identity-as-a-service (IDaaS) platform that provides identity management, access management, and identity governance capabilities. It enables organizations to manage user identities, enforce authentication policies including multi-factor authentication, and provide single sign-on across applications while maintaining compliance and security.

For more information, see [ForgeRock Identity Cloud documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/forgerock-identity-cloud).

## Before you begin

Ensure that you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * Privileged access to the PingOne Advanced Identity Cloud admin console (tenant administrator)
  * A PingOne Advanced Identity Cloud Log API key and secret with access to the monitoring endpoints



## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `forgerock-identity-cloud-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Create a Log API key in PingOne Advanced Identity Cloud

PingOne Advanced Identity Cloud uses Log API keys to authenticate requests to the `/monitoring/logs` endpoint. This is separate from service accounts, which are used for AM/IDM operations.

### Create the API key

  1. Sign in to the **PingOne Advanced Identity Cloud** admin console at `https://<tenant-env-fqdn>/platform/admin` (for example, `https://openam-mycompany-ew2.id.forgerock.io/platform/admin`).
  2. Click the **Tenant menu** (upper right).
  3. Click **Tenant settings**.
  4. Click the **Global Settings** tab.
  5. Click **Log API Keys**.
  6. Click **New Log API Key**.
  7. Enter a descriptive name (for example, `chronicle-log-collector`).
  8. Click **Create**.
  9. Copy and save the following values securely:

     * **api_key_id** : The API key identifier.
     * **api_key_secret** : The API key secret.
**Note:** The API key secret is displayed only once during creation. If lost, you must create a new Log API key.



### Get your tenant environment FQDN

  1. Sign in to the PingOne Advanced Identity Cloud admin console.
  2. Click the **Tenant menu** (upper right).
  3. Click **Tenant settings**.
  4. Under **Details** , note the **Tenant Name** value. 
     * Production format: `openam-<base-name>-<data-region>.id.forgerock.io`
     * Development format: `openam-<base-name>-<data-region>-dev.id.forgerock.io`
     * Sandbox format: `openam-<sandbox-name>.forgeblocks.com`



### Test API access

  * Test your credentials before proceeding with the integration:
        
        # Replace with your actual tenant FQDN and credentials
        TENANT_FQDN="openam-mycompany-ew2.id.forgerock.io"
        API_KEY="<your-api-key-id>"
        API_SECRET="<your-api-key-secret>"
        
        # List available log sources
        curl -v \
            -H "x-api-key: ${API_KEY}" \
            -H "x-api-secret: ${API_SECRET}" \
            "https://${TENANT_FQDN}/monitoring/logs/sources?_prettyPrint=true"
        
        # Retrieve recent audit logs
        curl -v \
            -H "x-api-key: ${API_KEY}" \
            -H "x-api-secret: ${API_SECRET}" \
            "https://${TENANT_FQDN}/monitoring/logs?source=am-authentication&_pageSize=5"
        




A successful response returns HTTP 200 with a JSON object containing log entries. If you receive HTTP 401, verify the API key and secret. If you receive HTTP 429, you have exceeded the rate limit of 60 requests per minute.

## Create service account for Cloud Run function

The Cloud Run function needs a service account with permissions to write to the GCS bucket and be invoked by Pub/Sub.

### Create service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `forgerock-logs-collector-sa`
     * **Service account description** : Enter `Service account for Cloud Run function to collect PingOne Advanced Identity Cloud logs`
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

  * **Storage Object Admin** : Write logs to the GCS bucket and manage state files.
  * **Cloud Run Invoker** : Allow Pub/Sub to invoke the function.
  * **Cloud Functions Invoker** : Allow function invocation.



### Grant IAM permissions on GCS bucket

Grant the service account write permissions on the GCS bucket:

  1. Go to **Cloud Storage > Buckets**.
  2. Click on your bucket name (for example, `forgerock-identity-cloud-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `forgerock-logs-collector-sa@PROJECT_ID.iam.gserviceaccount.com`)
     * **Assign roles** : Select **Storage Object Admin**
  6. Click **Save**.



## Create Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `forgerock-logs-trigger`
     * Leave other settings as default
  4. Click **Create**.



## Create Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from the PingOne Advanced Identity Cloud monitoring API and write them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `forgerock-logs-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose `forgerock-logs-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select `forgerock-logs-collector-sa`
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `forgerock-identity-cloud-logs` | GCS bucket name  
`GCS_PREFIX` | `forgerock-logs` | Prefix for log files  
`STATE_KEY` | `forgerock-logs/state.json` | State file path  
`TENANT_FQDN` | `openam-mycompany-ew2.id.forgerock.io` | PingOne AIC tenant environment FQDN  
`API_KEY` | `<your-api-key-id>` | PingOne AIC Log API key ID  
`API_SECRET` | `<your-api-key-secret>` | PingOne AIC Log API key secret  
`LOG_SOURCES` | `am-authentication,am-access,am-activity,am-config,idm-access,idm-activity,idm-authentication,idm-sync` | Comma-separated log sources  
`MAX_RECORDS` | `5000` | Max records per source per run  
`PAGE_SIZE` | `1000` | Records per page (max 1000)  
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

     * **main.py:**
           
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
           GCS_PREFIX = os.environ.get('GCS_PREFIX', 'forgerock-logs')
           STATE_KEY = os.environ.get('STATE_KEY', 'forgerock-logs/state.json')
           TENANT_FQDN = os.environ.get('TENANT_FQDN')
           API_KEY = os.environ.get('API_KEY')
           API_SECRET = os.environ.get('API_SECRET')
           LOG_SOURCES = os.environ.get('LOG_SOURCES', 'am-authentication,am-access,am-activity,idm-access,idm-activity,idm-authentication')
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
               Cloud Run function triggered by Pub/Sub to fetch PingOne Advanced Identity Cloud
               logs and write to GCS.
           
               Args:
                   cloud_event: CloudEvent object containing Pub/Sub message
               """
           
               if not all([GCS_BUCKET, TENANT_FQDN, API_KEY, API_SECRET]):
                   print('Error: Missing required environment variables')
                   return
           
               try:
                   # Get GCS bucket
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
           
                   # Fetch logs for configured sources
                   all_records = []
                   newest_event_time = None
                   sources = [s.strip() for s in LOG_SOURCES.split(',') if s.strip()]
           
                   for source in sources:
                       records, source_newest_time = fetch_logs(
                           tenant_fqdn=TENANT_FQDN,
                           api_key=API_KEY,
                           api_secret=API_SECRET,
                           source=source,
                           start_time=last_time,
                           end_time=now,
                           page_size=PAGE_SIZE,
                           max_records=MAX_RECORDS,
                       )
                       all_records.extend(records)
           
                       if source_newest_time:
                           if newest_event_time is None or parse_datetime(source_newest_time) > parse_datetime(newest_event_time):
                               newest_event_time = source_newest_time
           
                       print(f"Source '{source}': {len(records)} records")
           
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
           
           def fetch_logs(tenant_fqdn: str, api_key: str, api_secret: str, source: str, start_time: datetime, end_time: datetime, page_size: int, max_records: int):
               """
               Fetch logs from PingOne Advanced Identity Cloud Monitoring API with pagination.
           
               Args:
                   tenant_fqdn: Tenant environment FQDN
                   api_key: Log API key ID
                   api_secret: Log API key secret
                   source: Log source (am-authentication, am-access, idm-access, etc.)
                   start_time: Start time for log query
                   end_time: End time for log query
                   page_size: Number of records per page (max 1000)
                   max_records: Maximum total records to fetch
           
               Returns:
                   Tuple of (records list, newest_event_time ISO string)
               """
               endpoint = f"https://{tenant_fqdn}/monitoring/logs"
           
               headers = {
                   'x-api-key': api_key,
                   'x-api-secret': api_secret,
                   'Accept': 'application/json',
                   'User-Agent': 'GoogleSecOps-ForgeRockCollector/1.0'
               }
           
               records = []
               newest_time = None
               page_num = 0
               backoff = 1.0
           
               begin_time = start_time.strftime('%Y-%m-%dT%H:%M:%SZ')
               end_time_str = end_time.strftime('%Y-%m-%dT%H:%M:%SZ')
               paged_results_cookie = None
           
               while True:
                   page_num += 1
           
                   if len(records) >= max_records:
                       print(f"Reached max_records limit ({max_records})")
                       break
           
                   current_limit = min(page_size, max_records - len(records))
                   url = f"{endpoint}?source={source}&beginTime={begin_time}&endTime={end_time_str}&_pageSize={current_limit}"
           
                   if paged_results_cookie:
                       url += f"&_pagedResultsCookie={paged_results_cookie}"
           
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
                           return [], None
           
                       data = json.loads(response.data.decode('utf-8'))
           
                       page_results = data.get('result', [])
           
                       if not page_results:
                           print(f"No more results (empty page)")
                           break
           
                       print(f"Page {page_num}: Retrieved {len(page_results)} events")
                       records.extend(page_results)
           
                       # Track newest event time
                       for event in page_results:
                           try:
                               event_time = event.get('timestamp')
                               if event_time:
                                   if newest_time is None or parse_datetime(event_time) > parse_datetime(newest_time):
                                       newest_time = event_time
                           except Exception as e:
                               print(f"Warning: Could not parse event time: {e}")
           
                       # Check for more results
                       paged_results_cookie = data.get('pagedResultsCookie')
                       if not paged_results_cookie or paged_results_cookie == "-1":
                           print(f"Reached last page (no more results)")
                           break
           
                   except Exception as e:
                       print(f"Error fetching logs: {e}")
                       return [], None
           
               print(f"Retrieved {len(records)} total records from {page_num} pages")
               return records, newest_time
           

     * **requirements.txt:**
           
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
**Name** | `forgerock-logs-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select `forgerock-logs-trigger`  
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

  1. In the **Cloud Scheduler** console, find your job (`forgerock-logs-collector-hourly`).
  2. Click **Force run** to trigger the job manually.
  3. Wait a few seconds.
  4. Go to **Cloud Run > Services**.
  5. Click on **forgerock-logs-collector**.
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         Fetching logs from YYYY-MM-DDTHH:MM:SS+00:00 to YYYY-MM-DDTHH:MM:SS+00:00
         Source 'am-authentication': X records
         Source 'am-access': X records
         Wrote X records to gs://forgerock-identity-cloud-logs/forgerock-logs/logs_YYYYMMDD_HHMMSS.ndjson
         Successfully processed X records
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click on your bucket name (`forgerock-identity-cloud-logs`).

  10. Navigate to the `forgerock-logs/` folder.

  11. Verify that a new `.ndjson` file was created with the current timestamp.




If you see errors in the logs:

  * **HTTP 401** : Check the Log API key and secret in environment variables.
  * **HTTP 403** : Verify the API key has not been revoked in PingOne Advanced Identity Cloud.
  * **HTTP 429** : Rate limiting (60 requests per minute per environment) - the function will automatically retry with backoff.
  * **Missing environment variables** : Check all required variables are set.



## Retrieve the Google SecOps service account

Google SecOps uses a unique service account to read data from your GCS bucket. You must grant this service account access to your bucket.

### Get the service account email

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `ForgeRock Identity Cloud Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **ForgeRock Identity Cloud** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Do not use service accounts from other documentation or examples.
  9. Click **Next**.

  10. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://forgerock-identity-cloud-logs/forgerock-logs/
           

**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never** : Never deletes any files after transfers (recommended for testing).
       * **Delete transferred files** : Deletes files after successful transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.
**Note:** If you select a deletion option, the service account must have **Storage Object Admin** role instead of **Storage Object Viewer**. Update IAM permissions accordingly.
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days).

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).

     * **Ingestion labels** : The label to be applied to the events from this feed.

  11. Click **Next**.

  12. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## Grant IAM permissions to the Google SecOps service account

The Google SecOps service account needs **Storage Object Viewer** role on your GCS bucket.

  1. Go to **Cloud Storage > Buckets**.
  2. Click on your bucket name (`forgerock-identity-cloud-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Paste the Google SecOps service account email.
     * **Assign roles** : Select **Storage Object Viewer**.
  6. Click **Save**.

**Note:** If you plan to use the deletion option "Delete transferred files" or "Delete transferred files and empty directories," grant **Storage Object Admin** role instead of **Storage Object Viewer**.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`aav_label` | `additional.fields` | Merged  
`detail_label` | `additional.fields` | Merged  
`id_label` | `additional.fields` | Merged  
`objectId_label` | `additional.fields` | Merged  
`secure_label` | `additional.fields` | Merged  
`source_label` | `additional.fields` | Merged  
`topic_label` | `additional.fields` | Merged  
`trackingId_list` | `additional.fields` | Merged  
`transactionId_label` | `additional.fields` | Merged  
`extensions` | `extensions` | Renamed/mapped  
`metadata` | `metadata` | Renamed/mapped  
`payload.eventName` | `metadata.product_event_type` | Directly mapped  
`network` | `network` | Renamed/mapped  
`x-forwarded-proto` | `network.application_protocol` | Directly mapped  
`payload.http.request.method` | `network.http.method` | Directly mapped  
`value` | `network.http.response_code` | Renamed/mapped  
`user-agent` | `network.http.user_agent` | Directly mapped  
`principal` | `principal` | Renamed/mapped  
`host` | `principal.asset.hostname` | Directly mapped  
`payload.client.ip` | `principal.asset.ip` | Merged  
`xip` | `principal.asset.ip` | Merged  
`host` | `principal.hostname` | Directly mapped  
`entry.info.ipAddress` | `principal.ip` | Merged  
`payload.client.ip` | `principal.ip` | Merged  
`xip` | `principal.ip` | Merged  
`payload.client.port` | `principal.port` | Renamed/mapped  
`user_distinguished_name` | `principal.user.attribute.labels` | Merged  
`payload.userId` | `principal.user.userid` | Directly mapped  
`userId` | `principal.user.userid` | Directly mapped  
`Security_Result` | `security_result` | Merged  
`target` | `target` | Renamed/mapped  
`payload.applicationPrincipal.0` | `target.application` | Directly mapped  
`app_label` | `target.resource.attribute.labels` | Merged  
`realm_label` | `target.resource.attribute.labels` | Merged  
`payload.component` | `target.resource.name` | Directly mapped  
`payload.http.request.path` | `target.url` | Directly mapped  
N/A | `additional.fields` | Constant: `topic_label`  
N/A | `extensions.auth.type` | Constant: `AUTHTYPE_UNSPECIFIED`  
N/A | `metadata.event_type` | Constant: `USER_LOGIN`  
N/A | `principal.asset.ip` | Constant: `payload.client.ip`  
N/A | `principal.ip` | Constant: `payload.client.ip`  
N/A | `principal.user.attribute.labels` | Constant: `user_distinguished_name`  
N/A | `security_result` | Constant: `Security_Result`  
N/A | `target.resource.attribute.labels` | Constant: `app_label`  
`source_cloud` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`entry_info_nodeExtraLogging_auditInfo_Timestamp` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`entry_info_nodeOutcome` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`entry_info_authLevel` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`entry_info_nodeExtraLogging_auditInfo_clientId` | `event.idm.read_only_udm.principal.application` | Mapped from changelog  
`entry_info_nodeExtraLogging_auditInfo_EventName` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`entry_info_nodeExtraLogging_auditInfo_FlowType` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`entry_info_displayName` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`entry_info_nodeType` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`entry_info_nodeExtraLogging_auditInfo_Status` | `event.idm.read_only_udm.security_result.action` | Mapped from changelog  
`entry_info_nodeExtraLogging_auditInfo_TransactionId` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`entry_info_nodeId` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`entry_info_treeName` | `event.idm.read_only_udm.security_result.description` | Mapped from changelog  
`tenant_url` | `event.idm.read_only_udm.principal.url` | Mapped from changelog  
`payload.client.ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`payload.http.request.headers.x-forwarded-for` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`payload.client.port` | `event.idm.read_only_udm.principal.port` | Mapped from changelog  
`payload.http.request.method` | `event.idm.read_only_udm.network.http.request.method` | Mapped from changelog  
`payload.http.request.path` | `event.idm.read_only_udm.target.url` | Mapped from changelog  
`payload.topic` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`payload.http.request.headers.accept-api-version` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`payload.http.request.secure` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`payload.request.detail` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`payload.response` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`payload.request` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`payload.trackingIds` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`payload.objectId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`payload.http.request.headers.user-agent` | `event.idm.read_only_udm.network.http.user_agent` | Mapped from changelog  
`payload.http.request.headers.host` | `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` | Mapped from changelog  
`payload.http.request.headers.x-forwarded-proto` | `event.idm.read_only_udm.network.application_protocol` | Mapped from changelog  
`payload.response.statusCode` | `event.idm.read_only_udm.network.http.response_code` | Mapped from changelog  
`payload.operation` | `event.idm.read_only_udm.security_result.action_details` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/forgerock-identity-cloud-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
