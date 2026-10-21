---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ibm-security-verify-saas/
title: Collect IBM Security Verify SaaS logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:30:49.157520+00:00
---

# Collect IBM Security Verify SaaS logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ibm-security-verify-saas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect IBM Security Verify SaaS logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest IBM Security Verify SaaS logs to Google Security Operations using Google Cloud Storage V2.

IBM Security Verify SaaS is a cloud-based identity and access management platform that provides SSO, MFA, and adaptive access controls. It generates audit logs for authentication events, policy decisions, and user lifecycle management.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * Privileged access to IBM Security Verify SaaS (administrator role)



## Create a Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `ibm-verify-saas-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Collect IBM Security Verify SaaS API credentials

### Create API client

  1. Sign in to the **IBM Security Verify** admin console.
  2. Go to **Security > API Access**.
  3. Click **Add API Client**.
  4. Enter a name for the API client (for example, `Google Security Operations Integration`).
  5. Assign the following permissions: 
     * **Read event logs**
     * **Read reports**
  6. Click **Save**.
  7. Copy and save the following details in a secure location: 
     * **Client ID** : The API client identifier.
     * **Client Secret** : The API client secret key.



### Determine tenant URL

The API base URL is derived from your IBM Security Verify tenant. The format is:

Console URL | API Base URL  
---|---  
`https://YOUR_TENANT.verify.ibm.com` | `https://YOUR_TENANT.verify.ibm.com`  
  
  * Replace `YOUR_TENANT` with your actual IBM Security Verify tenant name.



### Verify permissions

To verify the API client has the required permissions:

  1. Sign in to the **IBM Security Verify** admin console.
  2. Go to **Security > API Access**.
  3. Click on the API client name.
  4. Verify that **Read event logs** and **Read reports** permissions are enabled.
  5. If permissions are missing, contact your IBM Security Verify administrator.



### Test API access

  * Test your credentials before proceeding with the integration:
        
        # Replace with your actual credentials
        CLIENT_ID="your-client-id"
        CLIENT_SECRET="your-client-secret"
        TENANT_URL="https://YOUR_TENANT.verify.ibm.com"
        
        # Get OAuth token
        TOKEN=$(curl -s -X POST "${TENANT_URL}/v1.0/endpoint/default/token" \
          -H "Content-Type: application/x-www-form-urlencoded" \
          -d "grant_type=client_credentials&client_id=${CLIENT_ID}&client_secret=${CLIENT_SECRET}" \
          | jq -r '.access_token')
        
        # Test API access
        curl -v -H "Authorization: Bearer ${TOKEN}" "${TENANT_URL}/v1.0/events?size=1"
        




## Create a service account for Cloud Run function

The Cloud Run function needs a service account with permissions to write to GCS bucket and be invoked by Pub/Sub.

### Create the service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `ibm-verify-collector-sa`.
     * **Service account description** : Enter `Service account for Cloud Run function to collect IBM Security Verify SaaS logs`.
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
  2. Click your bucket name (for example, `ibm-verify-saas-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `ibm-verify-collector-sa@your-project.iam.gserviceaccount.com`).
     * **Assign roles** : Select **Storage Object Admin**.
  6. Click **Save**.



## Create a Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `ibm-verify-trigger`.
     * Leave other settings as default.
  4. Click **Create**.



## Create a Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from IBM Security Verify SaaS API and write them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `ibm-verify-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose the topic `ibm-verify-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select the service account `ibm-verify-collector-sa`.
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `ibm-verify-saas-logs` | GCS bucket name  
`GCS_PREFIX` | `ibm-verify` | Prefix for log files  
`STATE_KEY` | `ibm-verify/state.json` | State file path  
`TENANT_URL` | `https://YOUR_TENANT.verify.ibm.com` | IBM Security Verify tenant URL  
`CLIENT_ID` | `your-client-id` | API client ID  
`CLIENT_SECRET` | `your-client-secret` | API client secret  
`MAX_RECORDS` | `10000` | Max records per run  
`PAGE_SIZE` | `1000` | Records per page  
`LOOKBACK_HOURS` | `24` | Initial lookback period  
  10. Scroll down in the **Variables & Secrets** tab to **Requests** :

     * **Request timeout** : Enter `600` seconds (10 minutes).
  11. Go to the **Settings** tab in **Containers** :

     * In the **Resources** section: 
       * **Memory** : Select **512 MiB** or higher.
       * **CPU** : Select **1**.
  12. In the **Revision scaling** section:

     * **Minimum number of instances** : Enter `0`.
     * **Maximum number of instances** : Enter `100` (or adjust based on expected load).
  13. Click **Create**.

  14. Wait for the service to be created (1-2 minutes).

  15. After the service is created, the **inline code editor** will open automatically.




### Add function code

  1. Enter **main** in **Function entry point**.
  2. In the inline code editor, create two files:

     * First file - **main.py:**
           
           import functions_framework
           from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
           import json
           import os
           import urllib3
           from datetime import datetime, timezone, timedelta
           import time
           import base64
           
           # Initialize HTTP client with timeouts
           http = urllib3.PoolManager(
             timeout=urllib3.Timeout(connect=5.0, read=30.0),
             retries=False,
           )
           
           # Initialize Storage client
           storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
           
           # Environment variables
           GCS_BUCKET = os.environ.get('GCS_BUCKET')
           GCS_PREFIX = os.environ.get('GCS_PREFIX', 'ibm-verify')
           STATE_KEY = os.environ.get('STATE_KEY', 'ibm-verify/state.json')
           TENANT_URL = os.environ.get('TENANT_URL', '').rstrip('/')
           CLIENT_ID = os.environ.get('CLIENT_ID', '')
           CLIENT_SECRET = os.environ.get('CLIENT_SECRET', '')
           MAX_RECORDS = int(os.environ.get('MAX_RECORDS', '10000'))
           PAGE_SIZE = int(os.environ.get('PAGE_SIZE', '1000'))
           LOOKBACK_HOURS = int(os.environ.get('LOOKBACK_HOURS', '24'))
           
           def parse_datetime(value: str) -> datetime:
             """Parse ISO datetime string to datetime object."""
             if [value](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.ObjectCustomContextPayload.html#google_cloud_storage_blob_ObjectCustomContextPayload_value).endswith("Z"):
               value = value[:-1] + "+00:00"
             return datetime.fromisoformat(value)
           
           def get_token():
             """Get OAuth 2.0 access token using client credentials flow."""
             token_url = f"{TENANT_URL}/v1.0/endpoint/default/token"
           
             body = f"grant_type=client_credentials&client_id={CLIENT_ID}&client_secret={CLIENT_SECRET}"
           
             headers = {
               'Content-Type': 'application/x-www-form-urlencoded',
               'Accept': 'application/json'
             }
           
             backoff = 1.0
             max_retries = 3
           
             for attempt in range(max_retries):
               response = http.request('POST', token_url, body=body.encode('utf-8'), headers=headers)
           
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
           
             raise RuntimeError(f"Failed to get token after {max_retries} retries due to rate limiting")
           
           @functions_framework.cloud_event
           def main(cloud_event):
             """
             Cloud Run function triggered by Pub/Sub to fetch IBM Security Verify SaaS logs and write to GCS.
           
             Args:
               cloud_event: CloudEvent object containing Pub/Sub message
             """
           
             if not all([GCS_BUCKET, TENANT_URL, CLIENT_ID, CLIENT_SECRET]):
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
                   last_time = last_time - timedelta(minutes=2)
                 except Exception as e:
                   print(f"Warning: Could not parse last_event_time: {e}")
           
               if last_time is None:
                 last_time = now - timedelta(hours=LOOKBACK_HOURS)
           
               print(f"Fetching logs from {last_time.isoformat()} to {now.isoformat()}")
           
               # Get access token
               token = get_token()
           
               # Fetch logs
               records, newest_event_time = fetch_logs(
                 token=token,
                 start_time=last_time,
                 end_time=now,
                 page_size=PAGE_SIZE,
                 max_records=MAX_RECORDS,
               )
           
               if not records:
                 print("No new log records found.")
                 save_state(bucket, STATE_KEY, now.isoformat())
                 return
           
               # Write to GCS as NDJSON
               timestamp = now.strftime('%Y%m%d_%H%M%S')
               object_key = f"{GCS_PREFIX}/logs_{timestamp}.ndjson"
               blob = bucket.blob(object_key)
           
               ndjson = '\n'.join([json.dumps(record, ensure_ascii=False) for record in records]) + '\n'
               blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(ndjson, content_type='application/x-ndjson')
           
               print(f"Wrote {len(records)} records to gs://{GCS_BUCKET}/{object_key}")
           
               if newest_event_time:
                 save_state(bucket, STATE_KEY, newest_event_time)
               else:
                 save_state(bucket, STATE_KEY, now.isoformat())
           
               print(f"Successfully processed {len(records)} records")
           
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
           
           def fetch_logs(token: str, start_time: datetime, end_time: datetime, page_size: int, max_records: int):
             """
             Fetch logs from IBM Security Verify SaaS Events API with pagination and rate limiting.
           
             Args:
               token: OAuth 2.0 access token
               start_time: Start time for log query
               end_time: End time for log query
               page_size: Number of records per page
               max_records: Maximum total records to fetch
           
             Returns:
               Tuple of (records list, newest_event_time ISO string)
             """
             endpoint = f"{TENANT_URL}/v1.0/events"
           
             headers = {
               'Authorization': f'Bearer {token}',
               'Accept': 'application/json',
               'User-Agent': 'GoogleSecOps-IBMVerifyCollector/1.0'
             }
           
             records = []
             newest_time = None
             page_num = 0
             backoff = 1.0
           
             start_iso = start_time.strftime('%Y-%m-%dT%H:%M:%S.000Z')
             end_iso = end_time.strftime('%Y-%m-%dT%H:%M:%S.000Z')
           
             # IBM Verify Events API uses filter and sort_order with pagination
             search_after = None
           
             while True:
               page_num += 1
           
               if len(records) >= max_records:
                 print(f"Reached max_records limit ({max_records})")
                 break
           
               params = []
               params.append(f"size={min(page_size, max_records - len(records))}")
               params.append(f"filter=time+ge+\"{start_iso}\"+and+time+le+\"{end_iso}\"")
               params.append("sort_order=asc")
               if search_after:
                 params.append(f"search_after={search_after}")
           
               url = f"{endpoint}?{'&'.join(params)}"
           
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
                   print(f"HTTP Error: {response.status}")
                   response_text = response.data.decode('utf-8')
                   print(f"Response body: {response_text}")
                   return [], None
           
                 data = json.loads(response.data.decode('utf-8'))
           
                 page_results = data.get('events', [])
           
                 if not page_results:
                   print(f"No more results (empty page)")
                   break
           
                 print(f"Page {page_num}: Retrieved {len(page_results)} events")
                 records.extend(page_results)
           
                 # Track newest event time
                 for event in page_results:
                   try:
                     event_time = event.get('time')
                     if event_time:
                       if newest_time is None or parse_datetime(event_time) > parse_datetime(newest_time):
                         newest_time = event_time
                   except Exception as e:
                     print(f"Warning: Could not parse event time: {e}")
           
                 # Check for more results using search_after pagination
                 if len(page_results) < page_size:
                   print(f"Reached last page (size={len(page_results)} < limit={page_size})")
                   break
           
                 # Use the last event's sort value for pagination
                 last_event = page_results[-1]
                 search_after = last_event.get('time', '')
           
               except Exception as e:
                 print(f"Error fetching logs: {e}")
                 return [], None
           
             print(f"Retrieved {len(records)} total records from {page_num} pages")
             return records, newest_time
           

     * Second file - **requirements.txt:**
           
           functions-framework==3.*
           google-cloud-storage==2.*
           urllib3>=2.0.0
           

  3. Click **Deploy** to save and deploy the function.

  4. Wait for deployment to complete (2-3 minutes).

**Note:** The Pub/Sub trigger configuration automatically creates the necessary subscriptions and permissions.



## Create a Cloud Scheduler job

Cloud Scheduler will publish messages to the Pub/Sub topic at regular intervals, triggering the Cloud Run function.

  1. In the **GCP Console** , go to **Cloud Scheduler**.
  2. Click **Create Job**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | `ibm-verify-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the topic `ibm-verify-trigger`  
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

  1. In the **Cloud Scheduler** console, find your job (`ibm-verify-collector-hourly`).
  2. Click **Force run** to trigger manually.
  3. Wait a few seconds and go to **Cloud Run > Services > ibm-verify-collector > Logs**.
  4. Verify the function executed successfully. Look for:
         
         Fetching logs from YYYY-MM-DDTHH:MM:SS+00:00 to YYYY-MM-DDTHH:MM:SS+00:00
         Page 1: Retrieved X events
         Wrote X records to gs://ibm-verify-saas-logs/ibm-verify/logs_YYYYMMDD_HHMMSS.ndjson
         Successfully processed X records
         

  5. Check the GCS bucket (`ibm-verify-saas-logs`) to confirm logs were written.




If you see errors in the logs:

  * **HTTP 401** : Check API credentials in environment variables
  * **HTTP 403** : Verify API client has required permissions in IBM Security Verify admin console
  * **HTTP 429** : Rate limiting - function will automatically retry with backoff
  * **Failed to get access token** : Verify `TENANT_URL`, `CLIENT_ID`, and `CLIENT_SECRET` are correct



## Configure a feed in Google SecOps to ingest IBM Security Verify SaaS logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `IBM Security Verify SaaS Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **IBM Security Verify SaaS** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address. You will use it in the next step.

**Note:** Each Google SecOps instance has a unique service account. Do not use service accounts from other documentation or examples.
  9. Click **Next**.

  10. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://ibm-verify-saas-logs/ibm-verify/
           

       * Replace: 
         * `ibm-verify-saas-logs`: Your GCS bucket name.
         * `ibm-verify`: Optional prefix/folder path where logs are stored (leave empty for root).
**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never** : Never deletes any files after transfers (recommended for testing).
       * **Delete transferred files** : Deletes files after successful transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.

**Note:** If you select a deletion option, the service account must have **Storage Object Admin** role instead of Storage Object Viewer. Update IAM permissions accordingly.
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days).

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).

     * **Ingestion labels** : The label to be applied to the events from this feed.

  11. Click **Next**.

  12. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## Grant IAM permissions to the Google SecOps service account

The Google SecOps service account needs **Storage Object Viewer** role on your GCS bucket.

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name (`ibm-verify-saas-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Paste the Google SecOps service account email.
     * **Assign roles** : Select **Storage Object Viewer**.
  6. Click **Save**.

**Note:** If you plan to use the deletion option "Delete transferred files" or "Delete transferred files and empty directories," grant **Storage Object Admin** role instead of Storage Object Viewer.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
data.realm, geoip.continent_name, data.applicationtype, data.id_token, data.grant_id, data.grant_type, data.at_hash, data.rt_hash, id, data.scope, data.uasessionid, data.performedby_type, data.subject_type, data.target_type, data.templateid, data.subjectid, data.performedby, data.action, data.performedby_clientname, geoip.as_org, geoip.country_iso_code, operation.op, operation.path, operation.value, operation.value.name, operation.value.values | additional.fields | Additional metadata fields not covered by standard UDM fields  
auth_type | extensions.auth.type | Type of authentication used  
meta_event_type | metadata.event_type | Type of event (e.g., USER_LOGIN, NETWORK_CONNECTION)  
tenantid | metadata.product_deployment_id | Identifier for the product deployment  
event_type | metadata.product_event_type | Product-specific event type  
data.ib_request_id | metadata.product_log_id | Product-specific log identifier  
data.devicetype | network.http.parsed_user_agent | Parsed user agent string  
data.devicetype | network.http.user_agent | User agent string  
data.sessionid | network.session_id | Session identifier  
tenantname | observer.hostname | Hostname of the observer  
data.applicationname | principal.application | Application associated with the principal  
data.origin, geoip.ip | principal.ip | IP address of the principal  
geoip.city_name | principal.location.city | City of the principal's location  
geoip.country_name | principal.location.country_or_region | Country or region of the principal's location  
geoip.location.lat | principal.location.region_latitude | Latitude of the principal's location  
geoip.location.lon | principal.location.region_longitude | Longitude of the principal's location  
geoip.region_name | principal.location.state | State of the principal's location  
data.applicationid | principal.resource.product_object_id | Product object identifier for the resource  
data.subtype | principal.resource.resource_subtype | Subtype of the resource  
data.redirecturl | principal.url | URL associated with the principal  
data.username | principal.user.user_display_name | Display name of the user  
data.userid | principal.user.userid | User identifier  
security_result | security_result | Security result information  
data.client_id, data.client_name, data.client_type | security_result.about.resource.attribute.labels | Labels for resource attributes  
action1 | security_result.action | Action taken by the security system  
data.result | security_result.action_details | Details of the security action  
data.status_code, correlationid | security_result.detection_fields | Fields related to detection  
servicename | target.application | Application targeted  
data.targetid | target.resource.id | Identifier of the target resource  
data.account_name | target.user.user_display_name | Display name of the target user  
data.target | target.user.userid | User identifier of the target  
| metadata.product_name | Product name  
| metadata.vendor_name | Vendor/company name  
`data.status_code", "data.performedby_type", "data.subject_type", "data.target_type", "data.templateid", "data.subjectid", "data.performedby", "data.action", and "data.performedby_clientname` | `additional.fields` | Mapped from changelog  
`data.cause` | `security_result.summary` | Mapped from changelog  
`data.json.Operations.path", "data.json.Operations.op", and "data.json.Operations.value` | `additional.fields` | Mapped from changelog  
`geoip.as_org", "geoip.country_iso_code` | `additional.fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ibm-security-verify-saas-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
