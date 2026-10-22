---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/mulesoft-anypoint/
title: Collect MuleSoft Anypoint platform logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:55:11.918100+00:00
---

# Collect MuleSoft Anypoint platform logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/mulesoft-anypoint/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect MuleSoft Anypoint platform logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest audit-trail events from MuleSoft Anypoint platform logs to Google Security Operations using Cloud Storage.

**Note:** MuleSoft is a log type without a prebuilt parser, therefore this guide only covers log ingestion. You must configure a custom parser to convert MuleSoft logs to UDM.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A Google Cloud project with Cloud Storage API enabled
  * Permissions to create and manage Cloud Storage buckets
  * Permissions to manage Identity and Access Management (IAM) policies on Cloud Storage buckets
  * Permissions to create Cloud Run functions, Pub/Sub topics, and Cloud Scheduler jobs
  * Permissions to create service accounts
  * Privileged access to the MuleSoft Anypoint Platform



## Get the MuleSoft Organization ID

  1. Sign in to the [Anypoint Platform](https://anypoint.mulesoft.com/).
  2. Go to **Access Management > Organizations**.
  3. In the **Business Groups** table, click your organization's name.
  4. Copy the **Organization ID** (for example, `0a12b3c4-d5e6-789f-1021-1a2b34cd5e6f`).



Alternatively, go to [MuleSoft Business Groups](https://anypoint.mulesoft.com/accounts/#/cs/profile/businessgroups) and copy the ID from the URL.

## Create the MuleSoft Connected App

  1. Sign in to the [Anypoint Platform](https://anypoint.mulesoft.com/).
  2. Go to **Access Management > Connected Apps > Create App**.
  3. Provide the following configuration details: 
     * **App name** : Enter a unique name (for example, `Google SecOps export`).
     * Select **App acts on its own behalf (client credentials)**.
  4. Click **Add scopes > Audit Log Viewer > Next**.
  5. Select every Business Group whose logs you need.
  6. Click **Next > Add scopes**.
  7. Click **Save** and copy the **Client ID** and **Client Secret**.

**Note:** Additional scopes may be required based on organization permissions. If you encounter permission errors, verify that the Connected App has been granted access to all required Business Groups.



## Create a Cloud Storage bucket

  1. Go to the [Google Cloud console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `mulesoft-audit-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Create a service account for the Cloud Run function

The Cloud Run function requires a service account with permissions to write to the Cloud Storage bucket.

### Create the service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `mulesoft-logs-collector-sa`.
     * **Service account description** : Enter `Service account for Cloud Run function to collect MuleSoft Anypoint logs`.
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

  * **Storage Object Admin** : Write logs to the Cloud Storage bucket and manage state files
  * **Cloud Run Invoker** : Allow Pub/Sub to invoke the function
  * **Cloud Functions Invoker** : Allow function invocation



#### Grant IAM permissions on the Cloud Storage bucket

Grant the service account `write` permissions on the Cloud Storage bucket as follows:

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `mulesoft-logs-collector-sa@PROJECT_ID.iam.gserviceaccount.com`).
     * **Assign roles** : Select **Storage Object Admin**.
  6. Click **Save**.



## Create a Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to as follows:

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `mulesoft-audit-trigger`.
     * Leave other settings as default.
  4. Click **Create**.



## Create a Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from the MuleSoft Anypoint API and write them to Cloud Storage.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Write a function**.
  3. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `mulesoft-audit-collector`  
**Region** | Select the region matching your Cloud Storage bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  4. In the **Trigger** section, click **Add trigger** and select **Pub/Sub trigger**.

  5. In the **Eventarc trigger** pane, provide the following configuration details:

     * **Trigger name** : Keep the generated name or enter a name for the trigger.
     * **Trigger type** : Select **Google Sources**.
     * **Event provider** : Select **Pub/Sub**.
     * **Event type** : Select **google.cloud.pubsub.topic.v1.messagePublished**.
     * **Select a Cloud Pub/Sub topic** : Choose the topic `mulesoft-audit-trigger`.
     * **Region** : Select the same region as the function.
     * **Service account** : Select the service account `mulesoft-logs-collector-sa`.
  6. Click **Save trigger**.

**Note:** The trigger options come from Eventarc. If **Pub/Sub trigger** is not listed, enable the **Eventarc API** for the project and reload the page. If the pane reports that the service account is missing the **Eventarc Event Receiver** or **Cloud Run Invoker** role, click **Grant**.
  7. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check**Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  8. Navigate to and expand **Containers, Networking, Security**.

  9. Go to the **Security** tab:

     * **Service account** : Select the `mulesoft-logs-collector-sa` service account.
  10. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `mulesoft-audit-logs` | Cloud Storage bucket name  
`GCS_PREFIX` | `mulesoft-audit` | Prefix for log files  
`STATE_KEY` | `mulesoft-audit-state.json` | State path, outside the log prefix  
`MULE_ORG_ID` | `your_org_id` | MuleSoft Organization ID  
`CLIENT_ID` | `your_client_id` | Connected App client ID  
`CLIENT_SECRET` | `your_client_secret` | Connected App client secret  
`MAX_RECORDS` | `10000` | Max records per run  
`PAGE_SIZE` | `200` | Entries per page (API maximum is 200)  
`LOOKBACK_HOURS` | `24` | Initial lookback period on first run  
**Note:** `STATE_KEY` points outside the log prefix on purpose. The feed ingests every object under its bucket URI and, when a deletion option is selected, deletes what it transferred. Keeping the state file out of that prefix stops it from being ingested as log data and from being deleted, which would reset collection and re-ingest duplicate events.
  11. Navigate to **Variables & Secrets** tab to **Requests** :

     * **Request timeout** : Enter `600` seconds (10 minutes).
  12. Go to the **Settings** tab in **Containers** :

     * In the **Resources** section: 
       * **Memory** : Select **512 MiB** or higher.
       * **CPU** : Select **1**.
     * Click **Done**.
  13. Navigate to **Execution environment** :

     * Select **Default** (recommended).
  14. In the **Revision scaling** section:

     * **Minimum number of instances** : Enter `0`.
     * **Maximum number of instances** : Enter `100` (or adjust based on expected load).
  15. Click **Create**.

  16. Wait for the service to be created (1-2 minutes).

  17. After the service is created, the inline code editor opens automatically.




### Add the function code

  1. Enter **main** in the **Function entry point**
  2. In the inline code editor, create two files:

     * First file - **main.py:**
           
           import functions_framework
           from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
           from google.cloud.exceptions import NotFound
           import hashlib
           import json
           import os
           import urllib3
           from urllib.parse import urlencode
           from datetime import datetime, timezone, timedelta
           import time
           
           # Initialize HTTP client with timeouts
           http = urllib3.PoolManager(
               timeout=urllib3.Timeout(connect=5.0, read=30.0),
               retries=False,
           )
           
           # Initialize Storage client
           storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
           
           # MuleSoft API endpoints
           TOKEN_URL = "https://anypoint.mulesoft.com/accounts/api/v2/oauth2/token"
           AUDIT_URL = "https://anypoint.mulesoft.com/audit/v2/organizations/{org_id}/query?cursorPagination=true"
           
           # Environment variables
           GCS_BUCKET = os.environ.get('GCS_BUCKET')
           GCS_PREFIX = os.environ.get('GCS_PREFIX', 'mulesoft-audit')
           # STATE_KEY must stay OUTSIDE GCS_PREFIX. The feed ingests every object under
           # its bucket URI and, with a deletion option selected, deletes what it
           # transferred. A state file inside the prefix would be ingested as log data and
           # then deleted, resetting collection and re-ingesting duplicates.
           STATE_KEY = os.environ.get('STATE_KEY', 'mulesoft-audit-state.json')
           MULE_ORG_ID = os.environ.get('MULE_ORG_ID')
           CLIENT_ID = os.environ.get('CLIENT_ID')
           CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
           MAX_RECORDS = int(os.environ.get('MAX_RECORDS', '10000'))
           # The Audit Log Query API returns at most 200 entries per JSON query.
           PAGE_SIZE = min(int(os.environ.get('PAGE_SIZE', '200')), 200)
           LOOKBACK_HOURS = int(os.environ.get('LOOKBACK_HOURS', '24'))
           # The query re-reads this many minutes before the watermark so that events the
           # platform records late are still collected. Re-read events are removed by hash.
           OVERLAP_MINUTES = int(os.environ.get('OVERLAP_MINUTES', '2'))
           
           class FetchError(Exception):
               """Raised when the MuleSoft API call fails.
           
               The watermark must never advance on a failed fetch, otherwise the events in
               the failed window are skipped permanently.
               """
           
           def to_unix_millis(dt: datetime) -> int:
               """Convert datetime to Unix epoch milliseconds."""
               if dt.tzinfo is None:
                   dt = dt.replace(tzinfo=timezone.utc)
               return int(dt.astimezone(timezone.utc).timestamp() * 1000)
           
           def parse_datetime(value: str) -> datetime:
               """Parse an ISO 8601 datetime string into an aware datetime."""
               if [value](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.ObjectCustomContextPayload.html#google_cloud_storage_blob_ObjectCustomContextPayload_value).endswith("Z"):
                   value = value[:-1] + "+00:00"
               dt = datetime.fromisoformat(value)
               if dt.tzinfo is None:
                   dt = dt.replace(tzinfo=timezone.utc)
               return dt
           
           def event_keys(event: dict) -> set:
               """Return the identity this event can be recognised by.
           
               Audit log entries carry no unique event ID, so a record counts as already
               collected when its full JSON content was seen before. The overlap window
               returns the same JSON again, which this catches without any knowledge of
               the payload schema.
               """
               return {'sha256:' + hashlib.sha256(
                   json.dumps(event, sort_keys=True, ensure_ascii=False).encode('utf-8')
               ).hexdigest()}
           
           def event_time(event: dict) -> str:
               """Return the event timestamp as an ISO 8601 string, or an empty string.
           
               Audit log entries carry the event time in `timestamp` as Unix milliseconds.
               """
               raw = event.get('timestamp')
               if raw is None or raw == '':
                   return ''
               try:
                   return datetime.fromtimestamp(int(raw) / 1000, tz=timezone.utc).isoformat()
               except (TypeError, ValueError):
                   return ''
           
           @functions_framework.cloud_event
           def main(cloud_event):
               """Fetch MuleSoft Anypoint audit logs and write them to Cloud Storage.
           
               Args:
                   cloud_event: CloudEvent object containing the Pub/Sub message.
               """
               if not all([GCS_BUCKET, MULE_ORG_ID, CLIENT_ID, CLIENT_SECRET]):
                   # Raise rather than return: a bare return acks the Pub/Sub message and
                   # reports the run as successful, silently discarding the schedule tick.
                   raise RuntimeError('Missing required environment variables')
           
               bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(GCS_BUCKET)
               state = load_state(bucket, STATE_KEY)
           
               now = datetime.now(timezone.utc)
               watermark = None
               if [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get('last_event_time'):
                   watermark = parse_datetime(state['last_event_time'])
               seen_keys = set([state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get('seen_keys', []))
           
               if watermark is None:
                   start_time = now - timedelta(hours=LOOKBACK_HOURS)
               else:
                   start_time = watermark - timedelta(minutes=OVERLAP_MINUTES)
           
               print(f"Fetching audit logs from {start_time.isoformat()} to {now.isoformat()}")
           
               token = get_token(CLIENT_ID, CLIENT_SECRET)
           
               # A FetchError here propagates: the run fails, the watermark is untouched,
               # and the next invocation retries the same window.
               records, newest_event_time = fetch_audit(
                   org_id=MULE_ORG_ID,
                   token=token,
                   start_time=start_time,
                   end_time=now,
                   page_size=PAGE_SIZE,
                   max_records=MAX_RECORDS,
               )
           
               # Remove events already written by an earlier run. Without this, the overlap
               # window re-emits its events on every invocation.
               fresh = [r for r in records if not (event_keys(r) & seen_keys)]
               print(f"Fetched {len(records)} records, {len(fresh)} new after deduplication")
           
               if not fresh:
                   print("No new audit log records found. Watermark left unchanged.")
                   return
           
               if not newest_event_time:
                   # A watermark that cannot be derived from the data is not a watermark.
                   # Advancing on wall-clock here would skip every late-recorded event.
                   raise FetchError('Records were returned but no event timestamp could be parsed')
           
               timestamp = now.strftime('%Y%m%dT%H%M%SZ')
               object_key = f"{GCS_PREFIX}/audit_{timestamp}.ndjson"
               blob = bucket.blob(object_key)
           
               ndjson = '\n'.join(json.dumps(record, ensure_ascii=False) for record in fresh) + '\n'
               blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(ndjson, content_type='application/x-ndjson')
           
               print(f"Wrote {len(fresh)} records to gs://{GCS_BUCKET}/{object_key}")
           
               # Advance the watermark only after the data is durably written.
               new_watermark = parse_datetime(newest_event_time)
               if watermark and new_watermark < watermark:
                   new_watermark = watermark
           
               # Retain only the hashes still inside the overlap window, so the state file
               # stays small while covering every event the next query can re-read.
               cutoff = new_watermark - timedelta(minutes=OVERLAP_MINUTES)
               retained = set()
               for record in records:
                   stamp = event_time(record)
                   if not stamp:
                       continue
                   if parse_datetime(stamp) >= cutoff:
                       retained.update(event_keys(record))
           
               save_state(bucket, STATE_KEY, {
                   'last_event_time': new_watermark.isoformat(),
                   'seen_keys': sorted(retained),
               })
           
               print(f"Successfully processed {len(fresh)} records")
           
           def load_state(bucket, key):
               """Read the collector state from Cloud Storage.
           
               Only a missing object is treated as a cold start. Any other error is raised:
               swallowing it would silently reset collection to the full lookback window
               and re-ingest that entire period.
               """
               blob = bucket.blob(key)
               try:
                   return json.loads(blob.[download_as_text](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_download_as_text)())
               except NotFound:
                   print('No state file found. Starting from the lookback window.')
                   return {}
           
           def save_state(bucket, key, state: dict):
               """Write the collector state to Cloud Storage.
           
               Failures are raised, not logged. If the state write fails after the data was
               uploaded, the next run repeats the same window and duplicates it.
               """
               blob = bucket.blob(key)
               blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
                   json.dumps(state, indent=2),
                   content_type='application/json',
               )
               print(f"Saved state: last_event_time={[state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get('last_event_time')}")
           
           def retry_after_seconds(response, backoff: float) -> int:
               """Parse Retry-After defensively; it may be an HTTP date, which int() cannot parse."""
               raw = response.headers.get('Retry-After')
               try:
                   return int(raw) if raw else int(backoff)
               except (TypeError, ValueError):
                   return int(backoff)
           
           def get_token(client_id: str, client_secret: str) -> str:
               """Get an OAuth 2.0 access token from MuleSoft using client credentials."""
               body = urlencode({
                   'grant_type': 'client_credentials',
                   'client_id': client_id,
                   'client_secret': client_secret,
               }).encode('utf-8')
           
               backoff = 1.0
               for attempt in range(5):
                   try:
                       response = http.request(
                           'POST',
                           TOKEN_URL,
                           body=body,
                           headers={'Content-Type': 'application/x-www-form-urlencoded'},
                       )
                   except Exception as e:
                       raise FetchError(f'Token request failed: {e}') from e
           
                   if response.status == 429:
                       wait = retry_after_seconds(response, backoff)
                       print(f"Rate limited (429) on token request. Retrying after {wait}s...")
                       time.sleep(wait)
                       backoff = min(backoff * 2, 30.0)
                       continue
           
                   if response.status != 200:
                       raise FetchError(f'Failed to get token: HTTP {response.status} {response.data.decode("utf-8", "replace")}')
           
                   try:
                       return json.loads(response.data.decode('utf-8'))['access_token']
                   except (json.JSONDecodeError, KeyError) as e:
                       raise FetchError(f'Malformed token response: {e}') from e
           
               raise FetchError('Rate limited repeatedly on token request; giving up without advancing the watermark')
           
           def fetch_audit(org_id: str, token: str, start_time: datetime, end_time: datetime, page_size: int, max_records: int):
               """Fetch audit log entries from the MuleSoft Audit Log Query API.
           
               Uses cursor pagination. The API returns entries in ascending timestamp order,
               which a time watermark requires: with newest-first ordering a truncated run
               would advance the watermark past unread events.
           
               Returns:
                   Tuple of (records list, newest_event_time ISO string).
           
               Raises:
                   FetchError: on any API or transport failure, so that the caller does not
                       mistake a failed fetch for an empty result and advance the watermark.
               """
               endpoint = AUDIT_URL.format(org_id=org_id)
               headers = {
                   'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/json',
                   'Accept': 'application/json',
               }
           
               records = []
               newest_time = None
               cursor = None
               page_num = 0
               backoff = 1.0
               rate_limit_retries = 0
               MAX_RATE_LIMIT_RETRIES = 5
           
               while True:
                   page_num += 1
           
                   if len(records) >= max_records:
                       # Stop cleanly. The remaining events stay ahead of the watermark and
                       # are collected by the next run.
                       print(f"Reached max_records limit ({max_records})")
                       break
           
                   # Rebuild the full query on every page; the time window must never be dropped.
                   body = {
                       'startDate': to_unix_millis(start_time),
                       'endDate': to_unix_millis(end_time),
                       'limit': page_size,
                       'ascending': True,
                   }
                   if cursor:
                       body['cursor'] = cursor
           
                   try:
                       response = http.request(
                           'POST',
                           endpoint,
                           body=json.dumps(body).encode('utf-8'),
                           headers=headers,
                       )
                   except Exception as e:
                       raise FetchError(f'Request to {endpoint} failed: {e}') from e
           
                   if response.status == 429:
                       rate_limit_retries += 1
                       if rate_limit_retries > MAX_RATE_LIMIT_RETRIES:
                           raise FetchError('Rate limited repeatedly; giving up without advancing the watermark')
                       wait = retry_after_seconds(response, backoff)
                       print(f"Rate limited (429). Retrying after {wait}s...")
                       time.sleep(wait)
                       backoff = min(backoff * 2, 30.0)
                       continue
           
                   backoff = 1.0
                   rate_limit_retries = 0
           
                   if response.status != 200:
                       raise FetchError(f'HTTP {response.status} from {endpoint}: {response.data.decode("utf-8", "replace")}')
           
                   try:
                       data = json.loads(response.data.decode('utf-8'))
                   except json.JSONDecodeError as e:
                       raise FetchError(f'Malformed JSON response from {endpoint}: {e}') from e
           
                   page_results = data.get('data') or []
                   if not page_results:
                       print("No more results (empty page)")
                       break
           
                   print(f"Page {page_num}: Retrieved {len(page_results)} entries")
                   records.extend(page_results)
           
                   for event in page_results:
                       stamp = event_time(event)
                       if not stamp:
                           continue
                       if newest_time is None or parse_datetime(stamp) > parse_datetime(newest_time):
                           newest_time = stamp
           
                   cursor = data.get('cursor')
                   if not cursor:
                       break
           
               print(f"Retrieved {len(records)} total entries from {page_num} pages")
               return records, newest_time
           

**Note:** This script is provided as an example and is not officially supported. We welcome feedback about how we can improve it. To submit feedback, click **Send Feedback > Google SecOps Security Product Feedback** on this page.

     * Second file - **requirements.txt:**
           
           functions-framework==3.*
           google-cloud-storage==2.*
           urllib3>=2.0.0
           

  3. Click **Deploy** to save and deploy the function.

  4. Wait for deployment to complete (2-3 minutes).




### Important considerations

  * **Rate limiting:** The Audit Log Query endpoint applies rate limits per IP in the three control planes. The US control plane allows 700 requests per minute per IP, while EU and Gov control planes allow 40 requests per minute per IP. The function implements exponential backoff to handle rate limiting automatically.

  * **Token expiration:** Access tokens usually expire about 30 to 60 minutes after being issued. The function requests a new token for each execution, which is well within that window.

  * **Deduplication and state:** The function keeps a watermark of the newest event time and the hashes of events inside the overlap window in the state file. Each run re-reads two minutes before the watermark to catch late-recorded entries and drops the ones it already wrote, so a retry, a manual run, or a scheduler delay does not produce duplicate events. A failed API call fails the run and leaves the watermark unchanged, so the next run retries the same window.

  * **Audit log retention:** Audit logs have a default retention period of one year. If your organization was created before July 10, 2023 and you didn't manually change the retention period, the retention period is six years. Download logs periodically if you need to retain them beyond the configured retention period.




## Create a Cloud Scheduler job

Cloud Scheduler will publish messages to the Pub/Sub topic at regular intervals, triggering the Cloud Run function.

  1. In the **GCP Console** , go to **Cloud Scheduler**.
  2. Click **Create Job**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | `mulesoft-audit-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the topic `mulesoft-audit-trigger`  
**Message body** | `{}` (empty JSON object)  
  4. Click **Create**.




### Test the scheduler job

  1. In the **Cloud Scheduler** console, find your job.
  2. Click **Force run** to trigger manually.
  3. Wait a few seconds and go to **Cloud Run > Services > mulesoft-audit-collector > Logs**.
  4. Verify the function executed successfully.
  5. Check the Cloud Storage bucket to confirm logs were written.



## Configure a feed in Google SecOps to ingest the MuleSoft logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `MuleSoft Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Mulesoft** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address. You will use it in the next step.

**Note:** Each Google SecOps instance has a unique service account. Do not use service accounts from other documentation or examples.
  9. Click **Next**.

  10. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the Cloud Storage bucket URI:
           
           gs://mulesoft-audit-logs/
           

       * Replace `mulesoft-audit-logs` with the actual name of the bucket.
**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never delete files** : Never delete files from the source (recommended for testing).
       * **Delete transferred files and empty directories** : Delete files and empty directories from the source after a successful fetch completes.
     * **Maximum File Age** : Include files modified in the last number of days. Default is 180 days.

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).

     * **Ingestion labels** : The label to be applied to the events from this feed.

  11. Click **Next**.

  12. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## Grant IAM permissions to the Google SecOps service account

The Google SecOps service account needs two roles on your Cloud Storage bucket: **Storage Object Viewer** to read the log objects, and a bucket-level role to read the bucket metadata.

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Paste the Google SecOps service account email.
     * **Assign roles** : Select both of the following:
     * **Storage Object Viewer** : reads the log objects.
     * **Storage Legacy Bucket Reader** : reads the bucket metadata. If you selected the **Delete transferred files and empty directories** deletion option, select **Storage Legacy Bucket Writer** instead, which also grants the delete permission.
  6. Click **Save**.

**Note:** Grant both roles. **Storage Object Viewer** does not grant the bucket-level permission the feed needs, and the **Storage Legacy Bucket** roles do not grant permission to read object contents.



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
