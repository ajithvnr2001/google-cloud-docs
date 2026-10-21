---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/onepassword-audit-events/
title: Collect 1Password Audit Events logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:01:46.469347+00:00
---

# Collect 1Password Audit Events logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/onepassword-audit-events/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect 1Password Audit Events logs

**Parser Version:** 2.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest 1Password Audit Events logs to Google Security Operations using Cloud Storage V2.

1Password is a password management platform that helps teams securely store, share, and manage credentials, secrets, and sensitive information. The 1Password Events API provides access to audit event data that captures administrative and policy actions performed in your 1Password Business account.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A Google Cloud project with Cloud Storage API enabled
  * Permissions to create and manage Cloud Storage buckets
  * Permissions to manage Identity and Access Management (IAM) policies on Cloud Storage buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * A [1Password Business](https://1password.com/pricing/password-manager) account
  * An owner or administrator role in your 1Password account



## Create a Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `onepassword-audit-secops-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Collect 1Password credentials

### Set up Events Reporting integration

  1. Sign in to your account on [1Password.com](https://1password.com).
  2. Select **Integrations** in the sidebar.
  3. If you have previously set up other integrations, select **Directory** on the **Integrations** page.
  4. In the **Events Reporting** section, select **Other**.
  5. In the **Name** field, enter a name for the integration (for example, `Google SecOps Audit Events`).
  6. Click **Add Integration**.



### Create a bearer token

  1. 1Password continues straight to the bearer token setup.

**Note:** To issue an additional token later, open the integration on the **Integrations** page and click **Add a token**.
  2. Provide the following configuration details:

     * **Token Name** : Enter a descriptive name (for example, `SecOps GCS Collector - Audit Events`)
     * **Expires After** : Choose when the token expires: **30 days** , **90 days** , or **180 days**. The default is **Never**.
     * **Events to Report** : Choose which events the token can access. All event types are selected by default. Keep **Audit events** selected and clear **Sign-in attempts** and **Item usages** so the token is scoped to audit events only.
  3. Click **Issue Token**.

  4. On the **Save your token** page, click **Save in 1Password** , choose the vault where you want to store the token, and then click **Save**. The token is saved as an API Credential item.

**Note:** The bearer token is a JWT credential. Copy its credential field from the saved item when you configure the collector. To replace a token, issue the new one first and revoke the old one afterwards, because ingestion stops as soon as a token is revoked.
  5. Click **View Integration Details** to confirm the integration is active.




### Determine your Events API base URL

The base URL depends on the server that hosts your 1Password account:

If your account is hosted on | Your Events API base URL is  
---|---  
`1password.com` | `https://events.1password.com`  
`ent.1password.com` | `https://events.ent.1password.com`  
`1password.ca` | `https://events.1password.ca`  
`1password.eu` | `https://events.1password.eu`  
**Note:** To determine which server hosts your account, sign in to 1Password.com and check the domain in your browser address bar.

### Test API access

  * Test your credentials before proceeding with the integration:
        
        # Replace with your actual bearer token and base URL
        BEARER_TOKEN="<your-bearer-token>"
        API_BASE="https://events.1password.com"
        
        # Test API access using the introspect endpoint
        curl -v \
            -H "Authorization: Bearer $BEARER_TOKEN" \
            "$API_BASE/api/v2/auth/introspect"
        




A successful response returns a JSON object with the `features` field listing the event types your token can access (for example, `["auditevents"]`).

**Note:** The Events API returns data from the last 120 days only. For older activity, use the audit log in your 1Password account.

## Create a service account for the Cloud Run function

The Cloud Run function needs a service account with permissions to write to Cloud Storage bucket and be invoked by Pub/Sub.

### Create the service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `onepassword-audit-collector-sa`
     * **Service account description** : Enter `Service account for Cloud Run function to collect 1Password Audit Events logs`
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

  * **Storage Object Admin** : Writes logs to Cloud Storage bucket and manage state files
  * **Cloud Run Invoker** : Allows Pub/Sub to invoke the function
  * **Cloud Functions Invoker** : Allows function invocation



### Grant IAM permissions on the Cloud Storage bucket

Grant the service account write permissions on the Cloud Storage bucket:

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket (`onepassword-audit-secops-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter `onepassword-audit-collector-sa@PROJECT_ID.iam.gserviceaccount.com`
     * **Assign roles** : Select **Storage Object Admin**
  6. Click **Save**.



## Create a Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `onepassword-audit-trigger`
     * Leave other settings as default
  4. Click **Create**.



## Create a Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch audit event logs from the 1Password Events API and write them to Cloud Storage.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `onepassword-audit-collector`  
**Region** | Select region matching your Cloud Storage bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose `onepassword-audit-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll to and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select `onepassword-audit-collector-sa`
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `onepassword-audit-secops-logs` | Cloud Storage bucket name  
`GCS_PREFIX` | `onepassword-audit` | Prefix for log files  
`STATE_KEY` | `onepassword-audit-state.json` | State file path, outside the log prefix  
`OP_API_BASE` | `https://events.1password.com` | 1Password Events API base URL  
`OP_BEARER_TOKEN` | `<your-bearer-token>` | 1Password Events API bearer token  
`MAX_RECORDS` | `10000` | Max records per run  
`PAGE_SIZE` | `1000` | Records per page (max 1000)  
`LOOKBACK_HOURS` | `24` | Initial lookback period in hours  
**Note:** `STATE_KEY` points outside the log prefix on purpose. The feed ingests every object under its bucket URI and, when a deletion option is selected, deletes what it transferred. Keeping the state file out of that prefix stops it from being ingested as log data and from being deleted, which would reset collection and re-ingest duplicate events.
  10. In the **Variables & Secrets** section, go to to **Requests** :

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




### Add the function code

  1. Enter **main** in the **Entry point** field.
  2. In the inline code editor, create two files:

     * First file - **main.py:**
           
           import functions_framework
           from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
           from google.cloud.exceptions import NotFound
           import json
           import os
           import re
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
           GCS_PREFIX = os.environ.get('GCS_PREFIX', 'onepassword-audit')
           # STATE_KEY must stay OUTSIDE GCS_PREFIX. The feed ingests every object under
           # its bucket URI and, with a deletion option selected, deletes what it
           # transferred. A state file inside the prefix is ingested as log data and then
           # deleted, which drops the cursor and replays the whole lookback window.
           STATE_KEY = os.environ.get('STATE_KEY', 'onepassword-audit-state.json')
           API_BASE = os.environ.get('OP_API_BASE')
           BEARER_TOKEN = os.environ.get('OP_BEARER_TOKEN')
           MAX_RECORDS = int(os.environ.get('MAX_RECORDS', '10000'))
           # The Events API accepts a limit from 1 to 1000.
           PAGE_SIZE = int(os.environ.get('PAGE_SIZE', '1000'))
           LOOKBACK_HOURS = int(os.environ.get('LOOKBACK_HOURS', '24'))
           
           # 1Password Events API v2 audit events endpoint
           AUDIT_EVENTS_PATH = '/api/v2/auditevents'
           
           class FetchError(Exception):
               """Raised when the 1Password Events API call fails.
           
               State must never be written on a failed fetch. Saving a rejected cursor back
               would wedge the collector: every later run would fail on page 1, ingest
               nothing, and still report success.
               """
           
           def parse_datetime(value: str) -> datetime:
               """Parse a 1Password `timestamp` into an aware datetime.
           
               The API returns RFC 3339 with either a numeric offset and whole seconds
               (2023-03-15T16:33:50-03:00) or Z with nanosecond precision
               (2025-10-31T13:45:49.203617068Z). Fractional digits are trimmed to
               microseconds because fromisoformat accepts at most six.
               """
               text = str(value).strip()
               if text.endswith('Z'):
                   text = text[:-1] + '+00:00'
               text = re.sub(r'\.(\d{6})\d+', r'.\1', text)
               dt = datetime.fromisoformat(text)
               if dt.tzinfo is None:
                   dt = dt.replace(tzinfo=timezone.utc)
               return dt.astimezone(timezone.utc)
           
           @functions_framework.cloud_event
           def main(cloud_event):
               """Fetch 1Password audit events and write them to Cloud Storage as NDJSON."""
               if not all([GCS_BUCKET, API_BASE, BEARER_TOKEN]):
                   # Raise rather than return: a bare return acks the Pub/Sub message and
                   # reports the run as successful, silently discarding the schedule tick.
                   raise RuntimeError('Missing required environment variables '
                                   '(GCS_BUCKET, OP_API_BASE, OP_BEARER_TOKEN)')
           
               bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(GCS_BUCKET)
               state = load_state(bucket, STATE_KEY)
           
               now = datetime.now(timezone.utc)
           
               print('--- Processing endpoint: auditevents ---')
           
               saved_cursor = [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get('cursor_auditevents')
               seen_uuids = set([state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get('seen_uuids', []))
           
               # If the cursor is gone, resume from the last event actually written instead
               # of replaying a blind 24 hours. LOOKBACK_HOURS applies only on a cold start.
               if saved_cursor:
                   start_time = None
               elif [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get('last_event_time'):
                   start_time = parse_datetime(state['last_event_time'])
                   print(f'No cursor found. Resuming from the last recorded event at {start_time.isoformat()}')
               else:
                   start_time = now - timedelta(hours=LOOKBACK_HOURS)
                   print(f'Cold start. Fetching from {start_time.isoformat()}')
           
               records, last_cursor = fetch_endpoint(
                   api_base=API_BASE,
                   path=AUDIT_EVENTS_PATH,
                   bearer_token=BEARER_TOKEN,
                   saved_cursor=saved_cursor,
                   start_time=start_time,
                   page_size=PAGE_SIZE,
                   max_records=MAX_RECORDS,
               )
           
               # The cursor path can re-deliver events, so filter by uuid before writing.
               fresh = [r for r in records if str(r.get('uuid', '')) not in seen_uuids]
               print(f'Fetched {len(records)} records, {len(fresh)} new after deduplication')
           
               if fresh:
                   timestamp = now.strftime('%Y%m%dT%H%M%SZ')
                   object_key = f'{GCS_PREFIX}/auditevents_{timestamp}.ndjson'
                   blob = bucket.blob(object_key)
           
                   ndjson = '\n'.join(
                       json.dumps(r, ensure_ascii=False) for r in fresh
                   ) + '\n'
                   blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
                       ndjson, content_type='application/x-ndjson'
                   )
           
                   print(f'Wrote {len(fresh)} auditevents records '
                       f'to gs://{GCS_BUCKET}/{object_key}')
           
               # State is written only after any data is durably uploaded.
               new_state = dict(state)
               if last_cursor:
                   new_state['cursor_auditevents'] = last_cursor
           
               newest = None
               for record in records:
                   stamp = record.get('timestamp')
                   if not stamp:
                       continue
                   try:
                       parsed = parse_datetime(stamp)
                   except ValueError:
                       continue
                   if newest is None or parsed > newest:
                       newest = parsed
               if newest:
                   new_state['last_event_time'] = newest.isoformat()
                   # Retain the uuids of the newest batch so a cursor reset does not
                   # re-ingest the events that straddle the resume point.
                   new_state['seen_uuids'] = sorted(
                       {str(r.get('uuid', '')) for r in records if r.get('uuid')}
                   )
           
               new_state['last_run'] = now.isoformat()
               save_state(bucket, STATE_KEY, new_state)
           
               print(f'Successfully processed {len(fresh)} records')
           
           def load_state(bucket, key):
               """Read the collector state from Cloud Storage.
           
               Only a missing object is treated as a cold start. Any other error is raised:
               swallowing it would drop the cursor and replay the lookback window.
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
               uploaded, the next run resumes from the stale cursor and duplicates it.
               """
               blob = bucket.blob(key)
               blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
                   json.dumps(state, indent=2),
                   content_type='application/json',
               )
               print(f"Saved state: cursor={[state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get('cursor_auditevents')!r} "
                   f"last_event_time={[state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get('last_event_time')}")
           
           def fetch_endpoint(api_base, path, bearer_token, saved_cursor,
                           start_time, page_size, max_records):
               """Fetch events from the 1Password Events API v2 audit events endpoint.
           
               The API uses cursor-based pagination with POST requests. The first request
               sends a ResetCursor object with an optional start_time and limit. Subsequent
               requests send the cursor returned by the previous response. The cursor is a
               persistent checkpoint and stays valid across runs.
           
               Args:
                   api_base: Events API base URL
                   path: Endpoint path
                   bearer_token: JWT bearer token
                   saved_cursor: Cursor from the previous run, or None
                   start_time: Lower bound used only when there is no cursor
                   page_size: Max events per page (1 to 1000)
                   max_records: Max total events per run
           
               Returns:
                   Tuple of (records list, cursor to persist).
           
               Raises:
                   FetchError: on any API or transport failure, so that a rejected cursor is
                       never written back to the state file.
               """
               url = f'{api_base.rstrip("/")}{path}'
           
               headers = {
                   'Authorization': f'Bearer {bearer_token}',
                   'Content-Type': 'application/json',
                   'Accept': 'application/json',
               }
           
               records = []
               cursor = saved_cursor
               page_num = 0
               backoff = 1.0
               rate_limit_retries = 0
               MAX_RATE_LIMIT_RETRIES = 5
           
               while True:
                   page_num += 1
           
                   if len(records) >= max_records:
                       print(f'Reached max_records limit ({max_records})')
                       break
           
                   if cursor:
                       # Continuing cursor: resume from the last position.
                       body = json.dumps({'cursor': cursor})
                   else:
                       # ResetCursor: first request, or the cursor was lost.
                       reset = {'limit': page_size}
                       if start_time:
                           reset['start_time'] = start_time.strftime('%Y-%m-%dT%H:%M:%SZ')
                       body = json.dumps(reset)
           
                   try:
                       response = http.request(
                           'POST', url, body=body, headers=headers,
                       )
                   except Exception as e:
                       raise FetchError(f'Request to {url} failed: {e}') from e
           
                   # Documented limits are 600 requests per minute and 30,000 per hour.
                   if response.status == 429:
                       rate_limit_retries += 1
                       if rate_limit_retries > MAX_RATE_LIMIT_RETRIES:
                           raise FetchError('Rate limited repeatedly; giving up without saving state')
                       raw_retry_after = response.headers.get('Retry-After')
                       try:
                           retry_after = int(raw_retry_after) if raw_retry_after else int(backoff)
                       except (TypeError, ValueError):
                           retry_after = int(backoff)
                       print(f'Rate limited (429). Retrying after {retry_after}s...')
                       time.sleep(retry_after)
                       backoff = min(backoff * 2, 60.0)
                       continue
           
                   backoff = 1.0
                   rate_limit_retries = 0
           
                   if response.status != 200:
                       body_text = response.data.decode('utf-8')
                       # A 400 or 401 here may mean the saved cursor was rejected. Raising
                       # leaves the previous state intact so the run can be retried, rather
                       # than persisting a cursor that stalls every future run.
                       raise FetchError(f'HTTP {response.status} from the Events API: {body_text}')
           
                   try:
                       data = json.loads(response.data.decode('utf-8'))
                   except json.JSONDecodeError as e:
                       raise FetchError(f'Malformed JSON response from the Events API: {e}') from e
           
                   page_items = data.get('items', [])
                   cursor = data.get('cursor')
                   has_more = data.get('has_more', False)
           
                   if page_items:
                       print(f'Page {page_num}: Retrieved '
                           f'{len(page_items)} events')
                       records.extend(page_items)
           
                   if not has_more:
                       print('No more pages (has_more=false)')
                       break
           
                   if not cursor:
                       print('No cursor returned, stopping')
                       break
           
                   if not page_items:
                       # has_more can be true while a page is empty. Stop rather than spin.
                       print('Empty page with has_more=true; resuming on the next run')
                       break
           
               print(f'Retrieved {len(records)} total records '
                   f'from {page_num} pages')
               return records, cursor
           

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
**Name** | `onepassword-audit-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select `onepassword-audit-trigger`  
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

  1. In the **Cloud Scheduler** console, find `onepassword-audit-collector-hourly`.
  2. Click **Force run** to trigger the job manually.
  3. Wait a few seconds.
  4. Go to **Cloud Run > Services**.
  5. Click `onepassword-audit-collector`.
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         --- Processing endpoint: auditevents ---
         Page 1: Retrieved X events
         Fetched X records, Y new after deduplication
         Wrote Y auditevents records to gs://onepassword-audit-secops-logs/onepassword-audit/auditevents_YYYYMMDDTHHMMSSZ.ndjson
         Saved state: cursor='...' last_event_time=YYYY-MM-DDTHH:MM:SS+00:00
         Successfully processed Y records
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click `onepassword-audit-secops-logs`.

  10. Navigate to the `onepassword-audit/` folder.

  11. Verify that a new `.ndjson` file was created with the current timestamp.




If you see errors in the logs:

  * **HTTP 401** : Check the bearer token in the `OP_BEARER_TOKEN` environment variable. The token may have expired.
  * **HTTP 429** : Rate limiting. The function automatically retries with backoff. The 1Password Events API allows 600 requests per minute and 30,000 requests per hour.
  * **Missing environment variables** : Check all required variables are set in the Cloud Run function configuration.
  * **No records returned** : Verify your bearer token has access to audit events using the introspect endpoint.
  * **The same events arrive repeatedly** : Confirm that `STATE_KEY` is not inside the prefix the feed reads. If the state file is deleted by the feed, the cursor is lost and the collector re-reads from its last recorded event.



## Retrieve the Google SecOps service account

Google SecOps uses a unique service account to read data from your Cloud Storage bucket. You must grant this service account access to your bucket.

### Get the service account email

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `1Password Audit Events Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **1Password Audit Events** as the **Log type**.
  7. Click **Get Service Account**.
  8. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  9. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Don't use service accounts from other documentation or examples.
  10. Click **Next**.

  11. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the Cloud Storage bucket URI with the prefix path:
           
           gs://onepassword-audit-secops-logs/onepassword-audit/
           

**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never delete files** : Never delete files from the source (recommended for testing).
       * **Delete transferred files and empty directories** : Delete files and empty directories from the source after a successful fetch completes.

**Note:** Grant both roles. **Storage Object Viewer** does not grant the bucket-level permission the feed needs, and the **Storage Legacy Bucket** roles do not grant permission to read object contents.
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days)

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)

     * **Ingestion labels** : The label to be applied to the events from this feed

  12. Click **Next**.

  13. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## Grant IAM permissions to the Google SecOps service account

The Google SecOps service account needs two roles on your Cloud Storage bucket: **Storage Object Viewer** to read the log objects, and a bucket-level role to read the bucket metadata.

  1. Go to **Cloud Storage > Buckets**.
  2. Click `onepassword-audit-secops-logs`.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Paste the Google SecOps service account email
     * **Assign roles** : Select both of the following: 
       * **Storage Object Viewer** : reads the log objects.
       * **Storage Legacy Bucket Reader** : reads the bucket metadata. If you selected the **Delete transferred files and empty directories** deletion option, select **Storage Legacy Bucket Writer** instead, which also grants the delete permission.
  6. Click **Save**.

**Note:** Grant both roles. **Storage Object Viewer** does not grant the bucket-level permission the feed needs, and the **Storage Legacy Bucket** roles do not grant permission to read object contents.



## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
`additional_action` | `additional.fields` | Merged  
`aux_id_label` | `additional.fields` | Merged  
`aux_info_list` | `additional.fields` | Merged  
`object_type_label` | `additional.fields` | Merged  
`EventTime` | `metadata.event_timestamp` | Parsed as `yyyy-MM-dd HH:mm:ss`  
`expiry` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ssZZZZZZZZZZ`  
`item.session.login_time` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ssZZZZZZZZZZ`  
`item.timestamp` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`has_principal` | `metadata.event_type` | Mapped: `true` → `USER_UNCATEGORIZED`, `true` → `STATUS_UPDATE`  
`item.session.uuid` | `network.session_id` | Directly mapped  
`deviceUuid` | `principal.asset.asset_id` | Directly mapped  
`session_ip` | `principal.asset.ip` | Merged  
`item.actor_details.email` | `principal.email` | Directly mapped  
`session_ip` | `principal.ip` | Merged  
`item.location.city` | `principal.location.city` | Directly mapped  
`item.location.country` | `principal.location.country_or_region` | Directly mapped  
`item.location.region` | `principal.location.name` | Directly mapped  
`item.location.latitude` | `principal.location.region_latitude` | Directly mapped  
`item.location.longitude` | `principal.location.region_longitude` | Directly mapped  
`uuid_label` | `principal.resource.attribute.labels` | Merged  
`item.actor_details.name` | `principal.user.user_display_name` | Directly mapped  
`item.actor_details.uuid` | `principal.user.userid` | Directly mapped  
`actor_uuid_label` | `security_result.about.resource.attribute.labels` | Merged  
`aux_uid_label` | `security_result.about.resource.attribute.labels` | Merged  
`object_id_label` | `security_result.about.resource.attribute.labels` | Merged  
`item.session.device_uuid` | `target.resource.product_object_id` | Directly mapped  
N/A | `metadata.event_type` | Constant: `USER_UNCATEGORIZED`  
N/A | `metadata.product_name` | Constant: `ONEPASSWORD_AUDIT_EVENTS`  
N/A | `metadata.vendor_name` | Constant: `ONEPASSWORD`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/onepassword-audit-events-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
