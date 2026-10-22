---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sap-btp/
title: Collect SAP BTP logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:34:34.386304+00:00
---

# Collect SAP BTP logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sap-btp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect SAP BTP logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest SAP Business Technology Platform (BTP) logs to Google Security Operations using Cloud Storage V2.

SAP Business Technology Platform (BTP) is a cloud platform that provides application development, integration, data management, and analytics capabilities. It generates security audit logs, access logs, and service event logs that are critical for monitoring platform activity and detecting security threats. A Cloud Run function polls the audit log retrieval API of the SAP **Audit Log Management Service** on a schedule, writes logs to a Cloud Storage bucket in NDJSON format, and Google SecOps ingests them through a Cloud Storage V2 feed.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A Google Cloud project with Cloud Storage API enabled
  * Permissions to create and manage Cloud Storage buckets
  * Permissions to manage Identity and Access Management (IAM) policies on Cloud Storage buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * Administrator access to SAP BTP with permissions to configure audit log retrieval (**Space Developer** in the target Cloud Foundry space, and the ability to add entitlements at the global account level)
  * The **Audit Log Management Service** (technical name: `auditlog-management`) entitled to your SAP BTP subaccount

**Note:** The Audit Log Management Service replaced the earlier Audit Log Retrieval service (technical name: `auditlog-api`), which is no longer available. If an existing integration uses a service instance of `auditlog-api`, recreate it with `auditlog-management`.



## Create a Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `sap-btp-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Collect SAP BTP API credentials

### Create an Audit Log Management Service instance

  1. Sign in to the [SAP BTP Cockpit](https://cockpit.btp.cloud.sap/).
  2. Ensure the **Audit Log Management Service** entitlement is assigned to the subaccount: in the subaccount view, go to **Entitlements > Edit > Add Service Plans** (entitlements are allocated from the global account).
  3. Navigate to your subaccount.
  4. Go to **Services > Instances and Subscriptions**.
  5. Click **Create**.
  6. Provide the following configuration details: 
     * **Service** : Select **Audit Log Management Service** (technical name: `auditlog-management`).
     * **Plan** : Select **default**.
     * **Runtime Environment** : Select **Cloud Foundry**.
     * **Space** : Select the target space.
     * **Instance Name** : Enter a name (for example, `auditlog-management-secops`).
  7. Click **Create**.



### Create a service key

  1. In the SAP BTP Cockpit, go to **Services > Instances and Subscriptions** and select the `auditlog-management` service instance.
  2. Choose **Create Service Key**.
  3. Enter a name (for example, `google-secops-integration`).
  4. Click **Create**.
  5. Copy and save the following details from the service key in a secure location:

     * **url** : The base URL for audit log retrieval requests.
     * **uaa.url** : The OAuth server base URL. The token endpoint is `<uaa.url>/oauth/token`.
     * **uaa.clientid** : The OAuth client ID.
     * **uaa.clientsecret** : The OAuth client secret.
**Note:** The OAuth access token obtained with these credentials is valid for 1 hour. The audit log service retains subaccount audit data for 90 days by default, which bounds any backfill. The retrieval API is rate limited (4 requests per second with bursts up to 20 on most landscapes) and returns HTTP 429 beyond that.



### Test API access

  * Test your credentials before proceeding with the integration:
        
        # Replace with your actual credentials from the service key
        UAA_URL="https://your-subdomain.authentication.region.hana.ondemand.com"
        CLIENT_ID="your-client-id"
        CLIENT_SECRET="your-client-secret"
        API_URL="https://auditlog-management.cfapps.us10.hana.ondemand.com"
        
        # Get OAuth token
        TOKEN=$(curl -s -X POST "${UAA_URL}/oauth/token" \
          -u "${CLIENT_ID}:${CLIENT_SECRET}" \
          -d "grant_type=client_credentials" \
          -H "Content-Type: application/x-www-form-urlencoded" | jq -r '.access_token')
        
        # Test API access: the API takes time_from/time_to in UTC without a
        # timezone suffix and returns a JSON array at the root. When the result
        # set is chunked, the next chunk's handle arrives in the "Paging"
        # response header.
        curl -v -H "Authorization: Bearer ${TOKEN}" \
          "${API_URL}/auditlog/v2/auditlogrecords?time_from=2026-08-07T00:00:00&time_to=2026-08-07T01:00:00"
        




## Create a service account for the Cloud Run function

The Cloud Run function needs a service account with permissions to write to Cloud Storage bucket and be invoked by Pub/Sub.

### Create the service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `sap-btp-collector-sa`.
     * **Service account description** : Enter `Service account for Cloud Run function to collect SAP BTP logs`.
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

  * **Storage Object Admin** : Write logs to Cloud Storage bucket and manage state files
  * **Cloud Run Invoker** : Allow Pub/Sub to invoke the function
  * **Cloud Functions Invoker** : Allow function invocation



### Grant IAM permissions on a Cloud Storage bucket

Grant the service account write permissions on the Cloud Storage bucket:

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name (for example, `sap-btp-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `sap-btp-collector-sa@your-project.iam.gserviceaccount.com`).
     * **Assign roles** : Select **Storage Object Admin**.
  6. Click **Save**.



## Create a Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `sap-btp-trigger`.
     * Leave other settings as default.
  4. Click **Create**.



## Create the Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch audit logs from the Audit Log Management Service retrieval API and write them to Cloud Storage.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `sap-btp-collector`  
**Region** | Select region matching your Cloud Storage bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose the topic `sap-btp-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select the service account `sap-btp-collector-sa`.
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `sap-btp-logs` | Cloud Storage bucket name  
`GCS_PREFIX` | `sap-btp` | Prefix for log files  
`STATE_KEY` | `sap-btp-state.json` | State file path, outside the log prefix  
`SAP_API_URL` | `https://auditlog-management.cfapps.us10.hana.ondemand.com` | The `url` value from the service key  
`SAP_UAA_URL` | `https://your-subdomain.authentication.region.hana.ondemand.com` | OAuth token endpoint URL  
`SAP_CLIENT_ID` | `your-client-id` | OAuth client ID  
`SAP_CLIENT_SECRET` | `your-client-secret` | OAuth client secret  
`LOOKBACK_HOURS` | `24` | Initial lookback period  
**Note:** `STATE_KEY` points outside the log prefix on purpose. The feed ingests every object under its bucket URI and, when a deletion option is selected, deletes what it transferred. Keeping the state file out of that prefix stops it from being ingested as log data and from being deleted, which would reset collection and re-ingest duplicate events.
  10. In the **Variables & Secrets** tab navigate to **Requests** :

     * **Request timeout** : Enter `600` seconds (10 minutes).
  11. Go to the **Settings** tab in **Containers** :

     * In the **Resources** section: 
       * **Memory** : Select **512 MiB** or higher.
       * **CPU** : Select **1**.
     * Click **Done**.
  12. Go to the **Execution environment** :

     * Select **Default** (recommended).
  13. In the **Revision scaling** section:

     * **Minimum number of instances** : Enter `0`.
     * **Maximum number of instances** : Enter `100` (or adjust based on expected load).
  14. Click **Create**.

  15. Wait for the service to be created (1-2 minutes).

  16. After the service is created, the **inline code editor** will open automatically.




### Add the function code

  1. Enter **main** in **Function entry point**.
  2. In the inline code editor, create two files:

     * First file - **main.py** :
           
           import functions_framework
           from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
           import hashlib
           import json
           import os
           import urllib3
           from datetime import datetime, timezone, timedelta
           import time
           import base64
           import uuid
           
           # Initialize HTTP client with timeouts
           http = urllib3.PoolManager(
               timeout=urllib3.Timeout(connect=5.0, read=30.0),
               retries=False,
           )
           
           # Initialize Storage client
           storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
           
           # Environment variables
           GCS_BUCKET = os.environ.get('GCS_BUCKET')
           GCS_PREFIX = os.environ.get('GCS_PREFIX', 'sap-btp')
           STATE_KEY = os.environ.get('STATE_KEY', 'sap-btp-state.json')
           SEEN_KEY = STATE_KEY + '.seen'
           API_URL = os.environ.get('SAP_API_URL')
           UAA_URL = os.environ.get('SAP_UAA_URL')
           CLIENT_ID = os.environ.get('SAP_CLIENT_ID')
           CLIENT_SECRET = os.environ.get('SAP_CLIENT_SECRET')
           LOOKBACK_HOURS = int(os.environ.get('LOOKBACK_HOURS', '24'))
           
           def parse_datetime(value: str) -> datetime:
               """Parse ISO datetime string to datetime object."""
               if [value](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.ObjectCustomContextPayload.html#google_cloud_storage_blob_ObjectCustomContextPayload_value).endswith("Z"):
                   value = value[:-1] + "+00:00"
               return datetime.fromisoformat(value)
           
           # message_uuid is the identifier of an audit log record; the parser maps it to
           # metadata.product_log_id.
           ID_FIELDS = ('message_uuid',)
           
           def event_keys(event):
               """Return every identity this event can be recognised by."""
               keys = {'sha256:' + hashlib.sha256(
                   json.dumps(event, sort_keys=True, ensure_ascii=False).encode('utf-8')
               ).hexdigest()}
               for field in ID_FIELDS:
                   value = event.get(field)
                   if value:
                       keys.add(f'{field}:{[value](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.ObjectCustomContextPayload.html#google_cloud_storage_blob_ObjectCustomContextPayload_value)}')
               return keys
           
           def get_oauth_token():
               """Get OAuth 2.0 access token using client credentials flow."""
               token_url = f"{UAA_URL.rstrip('/')}/oauth/token"
           
               credentials = f"{CLIENT_ID}:{CLIENT_SECRET}"
               encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
           
               headers = {
                   'Authorization': f'Basic {encoded_credentials}',
                   'Content-Type': 'application/x-www-form-urlencoded',
                   'Accept': 'application/json'
               }
           
               body = 'grant_type=client_credentials'
           
               backoff = 1.0
               max_retries = 3
           
               for attempt in range(max_retries):
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
           
               raise RuntimeError(f"Failed to get token after {max_retries} retries due to rate limiting")
           
           @functions_framework.cloud_event
           def main(cloud_event):
               """
               Cloud Run function triggered by Pub/Sub to fetch SAP BTP
               audit logs and write to GCS.
           
               Args:
                   cloud_event: CloudEvent object containing Pub/Sub message
               """
           
               if not all([GCS_BUCKET, API_URL, UAA_URL, CLIENT_ID, CLIENT_SECRET]):
                   # Raise rather than return: a bare return acks the Pub/Sub message and
                   # reports the run as successful, silently discarding the schedule tick.
                   raise RuntimeError('Missing required environment variables')
           
               try:
                   bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(GCS_BUCKET)
           
                   # Load state
                   state = load_state(bucket, STATE_KEY)
                   seen_keys = load_seen(bucket, SEEN_KEY)
           
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
           
                   print(f"Fetching audit logs from {last_time.isoformat()} to {now.isoformat()}")
           
                   # Get OAuth token
                   token = get_oauth_token()
           
                   # Fetch audit logs
                   records, newest_event_time = fetch_audit_logs(
                       token=token,
                       start_time=last_time,
                       end_time=now,
                   )
           
                   # Drop the events already written by a previous run (overlap window)
                   fresh = [r for r in records if not (event_keys(r) & seen_keys)]
           
                   if not fresh:
                       print("No new audit log records found.")
                       return
           
                   # Write to GCS as NDJSON
                   timestamp = now.strftime('%Y%m%d_%H%M%S')
                   # The random suffix keeps concurrent executions (Pub/Sub delivers at
                   # least once) from overwriting each other's object within one second.
                   object_key = f"{GCS_PREFIX}/audit_{timestamp}_{uuid.uuid4().hex[:8]}.ndjson"
                   blob = bucket.blob(object_key)
           
                   ndjson = '\n'.join([json.dumps(record, ensure_ascii=False) for record in fresh]) + '\n'
                   blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(ndjson, content_type='application/x-ndjson')
           
                   print(f"Wrote {len(fresh)} records to gs://{GCS_BUCKET}/{object_key}")
           
                   # Remember every fetched record so the next overlap window is deduplicated
                   save_seen(bucket, SEEN_KEY, records)
           
                   # Update state with newest event time. The watermark must be an event
                   # timestamp, never wall clock: a wall-clock watermark skips every event
                   # the vendor indexes late.
                   if not newest_event_time:
                       raise RuntimeError('Records were returned but no event timestamp could be parsed')
                   save_state(bucket, STATE_KEY, newest_event_time)
           
                   print(f"Successfully processed {len(fresh)} records")
           
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
                   raise
           
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
                   raise
           
           def load_seen(bucket, key):
               """Load the event keys written by the previous run."""
               try:
                   blob = bucket.blob(key)
                   if blob.exists():
                       return set(json.loads(blob.[download_as_text](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_download_as_text)()))
               except Exception as e:
                   print(f"Warning: Could not load seen keys: {e}")
                   raise
           
               return set()
           
           def save_seen(bucket, key, records):
               """Save the keys of every fetched record for the next overlap window."""
               try:
                   keys = set()
                   for record in records:
                       keys |= event_keys(record)
                   blob = bucket.blob(key)
                   blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
                       json.dumps(sorted(keys)),
                       content_type='application/json'
                   )
                   print(f"Saved {len(keys)} seen keys")
               except Exception as e:
                   print(f"Warning: Could not save seen keys: {e}")
                   raise
           
           def fetch_audit_logs(token: str, start_time: datetime, end_time: datetime):
               """
               Fetch audit logs from the Audit Log Management Service retrieval API.
           
               The API takes time_from/time_to in UTC without a timezone designator and
               returns a JSON array at the root (HTTP 204 when the window is empty).
               When the result set is chunked, the next chunk's handle arrives in the
               "Paging" response header as handle=<value> and is passed back as the
               handle query parameter; the server chunk size is fixed at 500 records.
           
               Args:
                   token: OAuth 2.0 access token
                   start_time: Start time for log query
                   end_time: End time for log query
           
               Returns:
                   Tuple of (records list, newest_event_time ISO string)
           
               Raises:
                   RuntimeError: on any API failure, so a failed fetch can never be
                       mistaken for an empty result.
               """
               base_url = API_URL.rstrip('/')
               endpoint = f"{base_url}/auditlog/v2/auditlogrecords"
           
               headers = {
                   'Authorization': f'Bearer {token}',
                   'Accept': 'application/json',
                   'User-Agent': 'GoogleSecOps-SAPBTPCollector/1.0'
               }
           
               records = []
               newest_time = None
               page_num = 0
               backoff = 1.0
               rate_limit_retries = 0
               token_refreshed = False
           
               # The API expects UTC timestamps with no timezone suffix.
               time_from = start_time.strftime('%Y-%m-%dT%H:%M:%S')
               time_to = end_time.strftime('%Y-%m-%dT%H:%M:%S')
               handle = None
           
               from urllib.parse import urlencode
           
               while True:
                   page_num += 1
           
                   # Rebuild the full parameter set on every request.
                   params = {'time_from': time_from, 'time_to': time_to}
                   if handle:
                       params['handle'] = handle
                   url = f"{endpoint}?{urlencode(params)}"
           
                   response = http.request('GET', url, headers=headers)
           
                   # The documented rate limit is 4 requests per second (burst 20).
                   if response.status == 429:
                       rate_limit_retries += 1
                       if rate_limit_retries > 5:
                           raise RuntimeError('Rate limited repeatedly; giving up without advancing the watermark')
                       retry_after = response.headers.get('Retry-After')
                       try:
                           delay = float(retry_after) if retry_after else backoff
                       except (TypeError, ValueError):
                           delay = backoff
                       delay = min(max(delay, 1.0), 60.0)
                       print(f"Rate limited (429). Retrying after {delay}s...")
                       time.sleep(delay)
                       backoff = min(backoff * 2, 30.0)
                       continue
           
                   backoff = 1.0
                   rate_limit_retries = 0
           
                   if response.status == 401:
                       # One refresh per run: a second consecutive 401 means the audit
                       # service rejects tokens UAA still issues, and retrying forever
                       # would hammer both services until the platform kills the run.
                       if token_refreshed:
                           raise RuntimeError('Audit log request still unauthorized after a token refresh')
                       print("Token expired, refreshing...")
                       token = get_oauth_token()
                       headers['Authorization'] = f'Bearer {token}'
                       token_refreshed = True
                       continue
           
                   token_refreshed = False
           
                   if response.status == 204:
                       # Documented empty result for the requested window.
                       break
           
                   if response.status != 200:
                       raise RuntimeError(
                           f"Audit log request failed: {response.status} - "
                           f"{response.data.decode('utf-8')}"
                       )
           
                   data = json.loads(response.data.decode('utf-8'))
           
                   # The records arrive as a JSON array at the root. Tolerate wrapped
                   # shapes defensively, but never call .get on a list: doing so
                   # crashed previous revisions of this function.
                   if isinstance(data, list):
                       page_results = data
                   elif isinstance(data, dict):
                       page_results = data.get('value', data.get('results', []))
                   else:
                       page_results = []
           
                   print(f"Page {page_num}: Retrieved {len(page_results)} audit records")
                   records.extend(page_results)
           
                   # Track newest event time. Parse before assigning: an unparseable
                   # stamp must never become the persisted watermark.
                   for record in page_results:
                       event_time = record.get('time') or record.get('timestamp')
                       if not event_time:
                           continue
                       try:
                           parsed = parse_datetime(event_time)
                       except Exception as e:
                           print(f"Warning: Could not parse event time: {e}")
                           continue
                       if newest_time is None or parsed > parse_datetime(newest_time):
                           newest_time = event_time
           
                   # More chunks are signaled only by the Paging response header.
                   paging = response.headers.get('Paging') or response.headers.get('paging') or ''
                   handle = paging.split('=', 1)[1] if '=' in paging else None
                   if not handle:
                       break
           
               print(f"Retrieved {len(records)} total audit records from {page_num} pages")
               return records, newest_time
           

**Note:** This script is provided as an example and is not officially supported. We welcome feedback about how we can improve it. To submit feedback, click **Send Feedback > Google SecOps Security Product Feedback** on this page.

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
**Name** | `sap-btp-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the topic `sap-btp-trigger`  
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

  1. In the **Cloud Scheduler** console, find your job (`sap-btp-collector-hourly`).
  2. Click **Force run** to trigger manually.
  3. Wait a few seconds and go to **Cloud Run > Services > sap-btp-collector > Logs**.
  4. Verify the function executed successfully. Look for:
         
         Fetching audit logs from YYYY-MM-DDTHH:MM:SS+00:00 to YYYY-MM-DDTHH:MM:SS+00:00
         Page 1: Retrieved X audit records
         Wrote X records to gs://sap-btp-logs/sap-btp/audit_YYYYMMDD_HHMMSS.ndjson
         Successfully processed X records
         

  5. Check the Cloud Storage bucket (`sap-btp-logs`) to confirm audit logs were written.




If you see errors in the logs:

  * **HTTP 401** : Check OAuth credentials in environment variables or token may have expired (function handles refresh automatically)
  * **HTTP 403** : Verify the service key belongs to an `auditlog-management` instance in the same subaccount whose logs you expect; user role collections do not apply to client-credentials tokens
  * **HTTP 429** : Rate limiting - function will automatically retry with backoff
  * **Failed to get access token** : Verify `SAP_UAA_URL`, `SAP_CLIENT_ID`, and `SAP_CLIENT_SECRET` are correct



## Configure a feed in Google SecOps to ingest SAP BTP logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `SAP BTP Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Sap Business Technology Platform** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address. You will use it in the next step.

**Note:** Each Google SecOps instance has a unique service account. Do not use service accounts from other documentation or examples.
  9. Click **Next**.

  10. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the Cloud Storage bucket URI with the prefix path:
           
           gs://sap-btp-logs/sap-btp/
           

       * Replace: 
         * `sap-btp-logs`: Your Cloud Storage bucket name.
         * `sap-btp/`: Path where logs are stored.
**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never delete files** : Never delete files from the source (recommended for testing).
       * **Delete transferred files and empty directories** : Delete files and empty directories from the source after a successful fetch completes.
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days).

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).

     * **Ingestion labels** : The label to be applied to the events from this feed.

  11. Click **Next**.

  12. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## Grant IAM permissions to the Google SecOps service account

The Google SecOps service account needs two roles on your Cloud Storage bucket: **Storage Object Viewer** to read the log objects, and a bucket-level role to read the bucket metadata.

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name (`sap-btp-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Paste the Google SecOps service account email.
     * **Assign roles** : Select both of the following: 
       * **Storage Object Viewer** : reads the log objects.
       * **Storage Legacy Bucket Reader** : reads the bucket metadata. If you selected the **Delete transferred files and empty directories** deletion option, select **Storage Legacy Bucket Writer** instead, which also grants the delete permission.
  6. Click **Save**.

**Note:** Grant both roles. **Storage Object Viewer** does not grant the bucket-level permission the feed needs, and the **Storage Legacy Bucket** roles do not grant permission to read object contents.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`time` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`principal_present` | `metadata.event_type` | Mapped: `true` → `STATUS_UPDATE`  
`user_present` | `metadata.event_type` | Mapped: `true` → `USER_RESOURCE_ACCESS`, `true` → `USER_UNCATEGORIZED`  
`json_message_uuid` | `metadata.product_log_id` | Directly mapped  
`host` | `principal.asset.hostname` | Directly mapped  
`key` | `principal.asset.ip` | Mapped: `ip` → `value`  
`principal_ip` | `principal.asset.ip` | Merged  
`value` | `principal.asset.ip` | Merged  
`host` | `principal.hostname` | Directly mapped  
`key` | `principal.ip` | Mapped: `ip` → `value`  
`principal_ip` | `principal.ip` | Merged  
`value` | `principal.ip` | Merged  
`principal_user_role` | `principal.user.attribute.roles` | Merged  
`key` | `principal.user.email_addresses` | Mapped: `"new","old"` → `value2`, `"new","old"` → `value1`  
`key1` | `principal.user.email_addresses` | Mapped: `emails` → `value2`, `userName` → `value1`  
`key2` | `principal.user.email_addresses` | Mapped: `value` → `value2`  
`value1` | `principal.user.email_addresses` | Mapped: `^.+@.+$` → `value1`  
`value2` | `principal.user.email_addresses` | Merged  
`user` | `principal.user.user_display_name` | Directly mapped  
`json_message.data_subject.id.userid` | `principal.user.userid` | Directly mapped  
`value1` | `principal.user.userid` | Directly mapped  
`category` | `security_result.category_details` | Merged  
`als_service_id_label` | `security_result.detection_fields` | Merged  
`app_or_service_id_label` | `security_result.detection_fields` | Merged  
`attri_label` | `security_result.detection_fields` | Merged  
`attribute_label` | `security_result.detection_fields` | Merged  
`attribute_label1` | `security_result.detection_fields` | Merged  
`custom_status_label` | `security_result.detection_fields` | Merged  
`custom_success_label` | `security_result.detection_fields` | Merged  
`custom_type_label` | `security_result.detection_fields` | Merged  
`desc_label` | `security_result.detection_fields` | Merged  
`format_version_label` | `security_result.detection_fields` | Merged  
`key` | `security_result.detection_fields` | Mapped: `json_message` → `message_label`, `id` → `attribute_label`, `"new","old"` → `attribu...  
`message_id_label` | `security_result.detection_fields` | Merged  
`message_label` | `security_result.detection_fields` | Merged  
`message_label_json_message` | `security_result.detection_fields` | Merged  
`message_label_msgId` | `security_result.detection_fields` | Merged  
`message_label_msgNo` | `security_result.detection_fields` | Merged  
`message_label_uuid` | `security_result.detection_fields` | Merged  
`message_label_version` | `security_result.detection_fields` | Merged  
`org_id_label` | `security_result.detection_fields` | Merged  
`space_id_label` | `security_result.detection_fields` | Merged  
`tenant_label` | `security_result.detection_fields` | Merged  
`key` | `security_result.severity` | Mapped: `level` → `INFORMATIONAL`, `level` → `MEDIUM`, `level` → `UNKNOWN_SEVERITY`  
`level` | `security_result.severity` | Mapped: `INFO` → `INFORMATIONAL`  
`value` | `security_result.severity` | Mapped: `INFO` → `INFORMATIONAL`, `WARN` → `MEDIUM`  
`level` | `security_result.severity_details` | Directly mapped  
`value1` | `target.resource.product_object_id` | Directly mapped  
`key1` | `target.resource.resource_type` | Mapped: `clusterID` → `CLUSTER`  
N/A | `metadata.event_type` | Constant: `GENERIC_EVENT`  
N/A | `metadata.product_name` | Constant: `SAP_BTP`  
N/A | `metadata.vendor_name` | Constant: `SAP_BTP`  
N/A | `security_result.severity` | Constant: `INFORMATIONAL`  
N/A | `target.resource.resource_type` | Constant: `CLUSTER`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sap-btp-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
