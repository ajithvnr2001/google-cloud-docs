---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cyberark-epm/
title: Collect CyberArk Endpoint Privilege Manager logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T12:57:25.398306+00:00
---

# Collect CyberArk Endpoint Privilege Manager logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cyberark-epm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect CyberArk Endpoint Privilege Manager logs

**Parser Version:** 2.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest CyberArk Endpoint Privilege Manager (EPM) logs to Google Security Operations using Cloud Storage V2.

CyberArk Endpoint Privilege Manager enforces least privilege on Windows, macOS, and Linux endpoints by removing local administrator rights, controlling which applications can run or elevate, and protecting credentials against theft. EPM SaaS exposes its event data through the EPM REST API. A Cloud Run function polls the raw events of each EPM set and writes them to a Cloud Storage bucket, from which Google SecOps ingests them.

**Note:** EPM SaaS has no SIEM or syslog forwarding option in the management console. Event export from EPM SaaS is available only through the EPM REST API, which is the method this document describes.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A Google Cloud project with Cloud Storage API enabled
  * Permissions to create and manage Cloud Storage buckets
  * Permissions to manage Identity and Access Management (IAM) policies on Cloud Storage buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * A CyberArk EPM SaaS tenant
  * An EPM account administrator to create the API user and role



## Create a Cloud Storage bucket

  1. Go to the [Google Cloud console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `cyberark-epm-secops-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Collect CyberArk EPM credentials

The Cloud Run function signs in to the EPM REST API with an EPM user. Create a dedicated user with view-only access to the sets whose events you want to collect.

### Create the API user

  1. Sign in to the EPM management console as an account administrator.
  2. Click the **Administration** tile.
  3. Go to the **Users** page and click **Add user**.
  4. Provide the following configuration details: 
     * **Email address** : Enter the sign-in name for the integration user (for example, `secops-collector@example.com`).
     * **Password** : Enter a password of 12 to 128 characters.
  5. Click **Add**.
  6. Save the sign-in name and password securely. You will use them as the `EPM_USERNAME` and `EPM_PASSWORD` values of the Cloud Run function.



### Create a view-only role and assign it

  1. In **Administration** , go to the **Roles** page and click **Create role**.
  2. Provide the following configuration details: 
     * **Name** : Enter a name for the role (for example, `SecOps view only`).
     * **Permission group** : Select **View only**.
     * **Sets** : Select every set whose events you want to collect.
  3. Click **Create**.
  4. Go to the **Role assignment** page.
  5. On the row of the role you created, click **More actions (...) > Assign or unassign users**.
  6. Click **Assign users** , search for the integration user, select it, and click **Assign**.
  7. Click **Save**.

**Note:** A set administrator cannot sign in until a role is assigned. The function lists the sets the user can view and collects events from all of them, or only from the sets listed in `EPM_SET_IDS`.



### Determine the EPM login URL

The EPM authentication API is served by the dispatcher server of your region. The function uses this URL only to sign in; every other call goes to the manager URL that the sign-in response returns.

Region | Login URL  
---|---  
USA | `https://login.epm.cyberark.com`  
Germany | `https://eu.epm.cyberark.com`  
Switzerland | `https://ch.epm.cyberark.com`  
UK | `https://uk.epm.cyberark.com`  
Australia | `https://au.epm.cyberark.com`  
Canada | `https://ca.epm.cyberark.com`  
India | `https://in.epm.cyberark.com`  
Japan | `https://jp.epm.cyberark.com`  
Singapore | `https://sg.epm.cyberark.com`  
Italy | `https://it.epm.cyberark.com`  
UAE | `https://ae.epm.cyberark.com`  
Federal | `https://login.epm.cyberarkgov.cloud`  
**Note:** The region is the one shown in the address bar when you sign in to the EPM management console.

### Test API access

  * Test the credentials before proceeding with the integration as follows:
        
        # Replace with your actual values
        EPM_LOGIN_URL="https://login.epm.cyberark.com"
        EPM_USERNAME="<your-username>"
        EPM_PASSWORD="<your-password>"
        
        # Sign in and get a session token and the manager URL
        curl -s -X POST "$EPM_LOGIN_URL/EPM/API/Auth/EPM/Logon" \
            -H "Content-Type: application/json" \
            -d "{\"Username\":\"$EPM_USERNAME\",\"Password\":\"$EPM_PASSWORD\",\"ApplicationID\":\"GoogleSecOps\"}"
        

  * A successful response returns `EPMAuthenticationResult` (the session token) and `ManagerURL`. To confirm the role, list the sets with the token as follows:
        
        # Replace with the values from the sign-in response
        MANAGER_URL="<ManagerURL>"
        TOKEN="<EPMAuthenticationResult>"
        
        curl -s "$MANAGER_URL/EPM/API/Sets?Limit=1000" \
            -H "Authorization: basic $TOKEN"
        




The response lists every set the user can view. If `Sets` is empty, the role is not assigned or does not include the sets.

**Note:** EPM allows one API sign-in per minute per user. Wait a minute between the test and the first run of the function, and do not use the integration user for anything else.

## Create a service account for the Cloud Run function

The Cloud Run function needs a service account with permissions to write to Cloud Storage bucket and be invoked by Pub/Sub.

### Create a service account

  1. In the **Google Cloud console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `cyberark-epm-collector-sa`
     * **Service account description** : Enter `Service account for Cloud Run function to collect CyberArk EPM logs`
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



### Grant IAM permissions on the Cloud Storage bucket

Grant the service account write permissions on the Cloud Storage bucket:

  1. In the **Google Cloud console** , Go to **Cloud Storage > Buckets**.
  2. Click your bucket name.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `cyberark-epm-collector-sa@PROJECT_ID.iam.gserviceaccount.com`)
     * **Assign roles** : Select **Storage Object Admin**
  6. Click **Save**.



## Create a Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **Google Cloud console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `cyberark-epm-trigger`
     * Leave other settings as default
  4. Click **Create**.



## Create a Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch raw events from the CyberArk EPM REST API and write them to Cloud Storage.

  1. In the **Google Cloud console** , go to **Cloud Run**.
  2. Click **Write a function**.
  3. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `cyberark-epm-collector`  
**Region** | Select region matching your Cloud Storage bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  4. In the **Trigger** section, click **Add trigger** and select **Pub/Sub trigger**.

  5. In the **Eventarc trigger** pane, provide the following configuration details:

     * **Trigger name** : Keep the generated name or enter a name for the trigger.
     * **Trigger type** : Select **Google Sources**.
     * **Event provider** : Select **Pub/Sub**.
     * **Event type** : Select **google.cloud.pubsub.topic.v1.messagePublished**.
     * **Select a Cloud Pub/Sub topic** : Choose the topic `cyberark-epm-trigger`.
     * **Region** : Select the same region as the function.
     * **Service account** : Select the service account `cyberark-epm-collector-sa`.
  6. Click **Save trigger**.

**Note:** The trigger options come from Eventarc. If **Pub/Sub trigger** is not listed, enable the **Eventarc API** for the project and reload the page. If the pane reports that the service account is missing the **Eventarc Event Receiver** or **Cloud Run Invoker** role, click **Grant**.
  7. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Select **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  8. Navigate to and expand **Containers, Networking, Security**.

  9. Go to the **Security** tab:

     * **Service account** : Select the service account `cyberark-epm-collector-sa`
  10. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `cyberark-epm-secops-logs` | Cloud Storage bucket name  
`GCS_PREFIX` | `cyberark-epm` | Prefix for log files  
`STATE_KEY` | `cyberark-epm-state.json` | State path, outside the log prefix  
`EPM_LOGIN_URL` | `https://login.epm.cyberark.com` | EPM login URL for your region  
`EPM_USERNAME` | `secops-collector@example.com` | Sign-in name of the EPM API user  
`EPM_PASSWORD` | `<your-password>` | Password of the EPM API user  
`EPM_APPLICATION_ID` | `GoogleSecOps` | Application name reported at sign-in  
`EPM_SET_IDS` | (empty) | Optional comma-separated set IDs; empty collects every set the user can view  
`EPM_API_VERSION` | (empty) | Optional API version (for example, `24.12.0.1`); empty uses the latest  
`MAX_RECORDS` | `10000` | Max records per run  
`PAGE_SIZE` | `1000` | Records per page (API maximum is 1000)  
`LOOKBACK_HOURS` | `24` | Initial lookback period on first run  
`OVERLAP_MINUTES` | `15` | Re-read window before the watermark, to catch events that agents report late  
**Note:** `STATE_KEY` points outside the log prefix on purpose. The feed ingests every object under its bucket URI and, when a deletion option is selected, deletes what it transferred. Keeping the state file out of that prefix stops it from being ingested as log data and from being deleted, which would reset collection and re-ingest duplicate events.
  11. In the **Variables & Secrets** section, navigate to **Requests** :

     * **Request timeout** : Enter `600` seconds (10 minutes)
  12. Go to the **Settings** tab:

     * In the **Resources** section: 
       * **Memory** : Select **512 MiB** or higher
       * **CPU** : Select **1**
  13. In the **Revision scaling** section:

     * **Minimum number of instances** : Enter `0`
     * **Maximum number of instances** : Enter `1`
**Note:** Keep the maximum at `1`. EPM allows one API sign-in per minute per user, and two overlapping runs would also write overlapping event batches.
  14. Click **Create**.

  15. Wait for the service to be created (1-2 minutes).

  16. After the service is created, the **inline code editor** will open automatically.




### Add the function code

  1. Enter **main** in the **Entry point** field.
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
                   timeout=urllib3.Timeout(connect=5.0, read=60.0),
                   retries=False,
           )
           
           # Initialize Storage client
           storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
           
           # Environment variables
           GCS_BUCKET = os.environ.get('GCS_BUCKET')
           GCS_PREFIX = os.environ.get('GCS_PREFIX', 'cyberark-epm')
           # STATE_KEY must stay OUTSIDE GCS_PREFIX. The feed ingests every object under
           # its bucket URI and, with a deletion option selected, deletes what it
           # transferred. A state file inside the prefix would be ingested as log data and
           # then deleted, resetting collection and re-ingesting duplicates.
           STATE_KEY = os.environ.get('STATE_KEY', 'cyberark-epm-state.json')
           EPM_LOGIN_URL = os.environ.get('EPM_LOGIN_URL', 'https://login.epm.cyberark.com')
           EPM_USERNAME = os.environ.get('EPM_USERNAME')
           EPM_PASSWORD = os.environ.get('EPM_PASSWORD')
           EPM_APPLICATION_ID = os.environ.get('EPM_APPLICATION_ID', 'GoogleSecOps')
           # Comma-separated set IDs to collect. Empty collects every set the user can view.
           EPM_SET_IDS = [s.strip() for s in os.environ.get('EPM_SET_IDS', '').split(',') if s.strip()]
           # API version segment. Empty uses the latest version, which CyberArk recommends.
           EPM_API_VERSION = os.environ.get('EPM_API_VERSION', '').strip()
           MAX_RECORDS = int(os.environ.get('MAX_RECORDS', '10000'))
           # The Events/Search API returns at most 1,000 records per page.
           PAGE_SIZE = min(int(os.environ.get('PAGE_SIZE', '1000')), 1000)
           LOOKBACK_HOURS = int(os.environ.get('LOOKBACK_HOURS', '24'))
           # The query re-reads this many minutes before the watermark. EPM agents report
           # in batches, so an event can reach the service well after its event date.
           # Re-read events are removed by content hash.
           OVERLAP_MINUTES = int(os.environ.get('OVERLAP_MINUTES', '15'))
           # The events APIs allow 5 calls per second; keep a small gap between calls.
           CALL_INTERVAL_SECONDS = 0.25
           
           class FetchError(Exception):
                   """Raised when the EPM API call fails.
           
                   The watermark must never advance on a failed fetch, otherwise the events in
                   the failed window are skipped permanently.
                   """
           
           def parse_datetime(value: str) -> datetime:
                   """Parse an ISO 8601 datetime string into an aware datetime."""
                   if [value](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.ObjectCustomContextPayload.html#google_cloud_storage_blob_ObjectCustomContextPayload_value).endswith('Z'):
                           value = value[:-1] + '+00:00'
                   dt = datetime.fromisoformat(value)
                   if dt.tzinfo is None:
                           dt = dt.replace(tzinfo=timezone.utc)
                   return dt
           
           def epm_time(dt: datetime) -> str:
                   """Render a datetime in the YYYY-MM-DDThh:mm:ssZ form the EPM filter accepts."""
                   return dt.astimezone(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
           
           def api_path(*parts: str) -> str:
                   """Build an /EPM/API path, inserting the version segment when one is set."""
                   segments = ['EPM', 'API']
                   if EPM_API_VERSION:
                           segments.append(EPM_API_VERSION)
                   segments.extend(parts)
                   return '/' + '/'.join(segments)
           
           def event_keys(event: dict) -> set:
                   """Return the identity this event can be recognised by.
           
                   Raw events carry no unique event ID, so a record counts as already
                   collected when its full JSON content was seen before. The overlap window
                   returns the same JSON again, which this catches without any knowledge of
                   the payload schema.
                   """
                   return {'sha256:' + hashlib.sha256(
                           json.dumps(event, sort_keys=True, ensure_ascii=False).encode('utf-8')
                   ).hexdigest()}
           
           def event_time(event: dict) -> str:
                   """Return the event timestamp as an ISO 8601 string, or an empty string.
           
                   Raw events carry the time of the most recent occurrence in `lastEventDate`.
                   """
                   value = event.get('lastEventDate')
                   return str(value) if value else ''
           
           @functions_framework.cloud_event
           def main(cloud_event):
                   """Fetch CyberArk EPM raw events and write them to Cloud Storage.
           
                   Args:
                           cloud_event: CloudEvent object containing the Pub/Sub message.
                   """
                   if not all([GCS_BUCKET, EPM_LOGIN_URL, EPM_USERNAME, EPM_PASSWORD]):
                           # Raise rather than return: a bare return acks the Pub/Sub message and
                           # reports the run as successful, silently discarding the schedule tick.
                           raise RuntimeError('Missing required environment variables')
           
                   bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(GCS_BUCKET)
                   state = load_state(bucket, STATE_KEY)
                   set_states = [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get('sets', {})
           
                   now = datetime.now(timezone.utc)
           
                   manager_url, token = login()
                   headers = {
                           'Authorization': f'basic {token}',
                           'Content-Type': 'application/json',
                           'Accept': 'application/json',
                   }
           
                   sets = list_sets(manager_url, headers)
                   if EPM_SET_IDS:
                           sets = [s for s in sets if s['Id'] in EPM_SET_IDS]
                           missing = set(EPM_SET_IDS) - {s['Id'] for s in sets}
                           if missing:
                                   raise FetchError(f'Configured set IDs not visible to this user: {sorted(missing)}')
                   if not sets:
                           raise FetchError('No EPM sets are visible to this user; check the assigned role')
           
                   fresh_all = []
                   new_set_states = {}
                   budget = MAX_RECORDS
           
                   for epm_set in sets:
                           set_id = epm_set['Id']
                           set_state = set_states.get(set_id, {})
                           watermark = None
                           if set_state.get('last_event_time'):
                                   watermark = parse_datetime(set_state['last_event_time'])
                           seen_keys = set(set_state.get('seen_keys', []))
           
                           if watermark is None:
                                   start_time = now - timedelta(hours=LOOKBACK_HOURS)
                           else:
                                   start_time = watermark - timedelta(minutes=OVERLAP_MINUTES)
           
                           print(f"Set {set_id} ({epm_set.get('Name', '')}): fetching events from {start_time.isoformat()} to {now.isoformat()}")
           
                           # A FetchError here propagates: the run fails, the watermark is untouched,
                           # and the next invocation retries the same window.
                           records, newest_event_time = fetch_events(
                                   manager_url=manager_url,
                                   headers=headers,
                                   set_id=set_id,
                                   start_time=start_time,
                                   end_time=now,
                                   page_size=PAGE_SIZE,
                                   max_records=budget,
                           )
                           budget -= len(records)
           
                           # Remove events already written by an earlier run. Without this, the overlap
                           # window re-emits its events on every invocation.
                           fresh = [r for r in records if not (event_keys(r) & seen_keys)]
                           print(f"Set {set_id}: fetched {len(records)} records, {len(fresh)} new after deduplication")
           
                           if not fresh:
                                   new_set_states[set_id] = set_state
                                   continue
           
                           if not newest_event_time:
                                   # A watermark that cannot be derived from the data is not a watermark.
                                   # Advancing on wall-clock here would skip every late-reported event.
                                   raise FetchError(f'Set {set_id}: records were returned but no event timestamp could be parsed')
           
                           # The parser reads the set from the event itself. Annotate copies so the
                           # deduplication hashes keep matching what the API returns next time.
                           fresh_all.extend({**record, 'setID': set_id} for record in fresh)
           
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
                                   try:
                                           if parse_datetime(stamp) >= cutoff:
                                                   retained.update(event_keys(record))
                                   except ValueError:
                                           continue
           
                           new_set_states[set_id] = {
                                   'last_event_time': new_watermark.isoformat(),
                                   'seen_keys': sorted(retained),
                           }
           
                           if budget <= 0:
                                   print(f"Reached max_records limit ({MAX_RECORDS}); remaining sets are collected by the next run")
                                   break
           
                   # Keep the state of sets not visited in this run.
                   for set_id, set_state in set_states.items():
                           new_set_states.setdefault(set_id, set_state)
           
                   if not fresh_all:
                           print("No new events found. Watermarks left unchanged.")
                           return
           
                   timestamp = now.strftime('%Y%m%dT%H%M%SZ')
                   object_key = f"{GCS_PREFIX}/events_{timestamp}.ndjson"
                   blob = bucket.blob(object_key)
           
                   ndjson = '\n'.join(json.dumps(record, ensure_ascii=False) for record in fresh_all) + '\n'
                   blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(ndjson, content_type='application/x-ndjson')
           
                   print(f"Wrote {len(fresh_all)} records to gs://{GCS_BUCKET}/{object_key}")
           
                   # Advance the watermarks only after the data is durably written.
                   save_state(bucket, STATE_KEY, {'sets': new_set_states})
           
                   print(f"Successfully processed {len(fresh_all)} records")
           
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
                   print(f"Saved state for {len([state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get('sets', {}))} sets")
           
           def request_json(method: str, url: str, headers: dict, body: dict = None):
                   """Call the EPM API and return the decoded JSON body.
           
                   Raises FetchError on any transport or HTTP failure, so that the caller does
                   not mistake a failed call for an empty result and advance the watermark.
                   """
                   backoff = 1.0
                   for attempt in range(5):
                           time.sleep(CALL_INTERVAL_SECONDS)
                           try:
                                   response = http.request(
                                           method,
                                           url,
                                           body=json.dumps(body).encode('utf-8') if body is not None else None,
                                           headers=headers,
                                   )
                           except Exception as e:
                                   raise FetchError(f'Request to {url} failed: {e}') from e
           
                           if response.status == 429:
                                   raw_retry_after = response.headers.get('Retry-After')
                                   try:
                                           # Retry-After may also be an HTTP date, which int() cannot parse.
                                           wait = int(raw_retry_after) if raw_retry_after else int(backoff)
                                   except (TypeError, ValueError):
                                           wait = int(backoff)
                                   print(f"Rate limited (429). Retrying after {wait}s...")
                                   time.sleep(wait)
                                   backoff = min(backoff * 2, 30.0)
                                   continue
           
                           if response.status != 200:
                                   raise FetchError(f'HTTP {response.status} from {url}: {response.data.decode("utf-8", "replace")}')
           
                           try:
                                   return json.loads(response.data.decode('utf-8'))
                           except json.JSONDecodeError as e:
                                   raise FetchError(f'Malformed JSON response from {url}: {e}') from e
           
                   raise FetchError('Rate limited repeatedly; giving up without advancing the watermark')
           
           def login():
                   """Authenticate to EPM and return the manager URL and session token.
           
                   EPM allows one API login per minute per user, so the function signs in once
                   per run and reuses the token for every call in that run.
                   """
                   url = f"{EPM_LOGIN_URL.rstrip('/')}{api_path('Auth', 'EPM', 'Logon')}"
                   body = {
                           'Username': EPM_USERNAME,
                           'Password': EPM_PASSWORD,
                           'ApplicationID': EPM_APPLICATION_ID,
                   }
                   data = request_json('POST', url, {'Content-Type': 'application/json'}, body)
                   token = data.get('EPMAuthenticationResult')
                   manager_url = data.get('ManagerURL')
                   if not token or not manager_url:
                           raise FetchError(f'Login response did not contain a token and manager URL: {data}')
                   if data.get('IsPasswordExpired'):
                           raise FetchError('The EPM user password has expired; set a new password and update EPM_PASSWORD')
                   return manager_url.rstrip('/'), token
           
           def list_sets(manager_url: str, headers: dict):
                   """Return the sets visible to the API user."""
                   url = f"{manager_url}{api_path('Sets')}?{urlencode({'Offset': 0, 'Limit': 1000})}"
                   data = request_json('GET', url, headers)
                   sets = data.get('Sets') or []
                   print(f"Found {len(sets)} sets")
                   return sets
           
           def fetch_events(manager_url: str, headers: dict, set_id: str, start_time: datetime, end_time: datetime, page_size: int, max_records: int):
                   """Fetch raw events for one set from the EPM Events/Search API.
           
                   Pages with nextCursor, which returns events in chronological order. A time
                   watermark is only correct over an ascending scan: with newest-first ordering
                   a truncated run would advance the watermark past unread events.
           
                   Returns:
                           Tuple of (records list, newest_event_time ISO string).
                   """
                   endpoint = f"{manager_url}{api_path('Sets', set_id, 'Events', 'Search')}"
                   body = {
                           'filter': f'eventDate GE {epm_time(start_time)} AND eventDate LE {epm_time(end_time)}',
                   }
           
                   records = []
                   newest_time = None
                   cursor = 'start'
                   page_num = 0
           
                   while True:
                           page_num += 1
           
                           if len(records) >= max_records:
                                   # Stop cleanly. The remaining events stay ahead of the watermark and
                                   # are collected by the next run.
                                   print(f"Set {set_id}: reached max_records limit ({max_records})")
                                   break
           
                           # Rebuild the full query on every page; the time window must never be dropped.
                           url = f"{endpoint}?{urlencode({'nextCursor': cursor, 'limit': page_size})}"
                           data = request_json('POST', url, headers, body)
           
                           page_results = data.get('events') or []
                           if not page_results:
                                   print(f"Set {set_id}: no more results (empty page)")
                                   break
           
                           print(f"Set {set_id}: page {page_num} retrieved {len(page_results)} events")
                           records.extend(page_results)
           
                           for event in page_results:
                                   stamp = event_time(event)
                                   if not stamp:
                                           continue
                                   try:
                                           if newest_time is None or parse_datetime(stamp) > parse_datetime(newest_time):
                                                   newest_time = stamp
                                   except ValueError as e:
                                           print(f"Warning: Could not parse event time {stamp!r}: {e}")
           
                           cursor = data.get('nextCursor')
                           if not cursor:
                                   break
           
                   print(f"Set {set_id}: retrieved {len(records)} total events from {page_num} pages")
                   return records, newest_time
           

**Note:** This script is provided as an example and is not officially supported. We welcome feedback about how we can improve it. To submit feedback, click **Send Feedback > Google SecOps Security Product Feedback** on this page.

     * Second file - **requirements.txt:**
           
           functions-framework==3.*
           google-cloud-storage==2.*
           urllib3>=2.0.0
           

  3. Click **Deploy** to save and deploy the function.

  4. Wait for deployment to complete (2-3 minutes).


**Note:** The Pub/Sub trigger configuration automatically creates the necessary subscriptions and permissions.

### How the function collects events

  * The function signs in once per run, lists the sets the user can view, and calls the **Get detailed raw events** API of each set with a filter on `eventDate`, paging with `nextCursor` in chronological order.
  * Each event is written with the additional `setID` field so that the set is preserved in the log.
  * The state file keeps, per set, the newest `lastEventDate` seen and the hashes of the events inside the overlap window. Every run re-reads `OVERLAP_MINUTES` before that watermark and drops the events it already wrote, so agents that report late are still collected without duplicates.
  * Any API, sign-in or storage error fails the run and leaves the watermark unchanged, so the next run retries the same window.



## Create a Cloud Scheduler job

Cloud Scheduler will publish messages to the Pub/Sub topic at regular intervals, triggering the Cloud Run function.

  1. In the **Google Cloud console** , go to **Cloud Scheduler**.
  2. Click **Create Job**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | `cyberark-epm-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the Pub/Sub topic `cyberark-epm-trigger`  
**Message body** | `{}` (empty JSON object)  
  4. Click **Create**.




### Schedule frequency options

Choose frequency based on log volume and latency requirements:

Frequency | Cron Expression | Use Case  
---|---|---  
Every 15 minutes | `*/15 * * * *` | Low latency  
Every hour | `0 * * * *` | Standard (recommended)  
Every 6 hours | `0 */6 * * *` | Low volume, batch processing  
**Note:** The EPM events APIs are limited to 1,000 calls per 5 minutes and 100,000 events per 24 hours per tenant, and to one sign-in per minute per user. Do not schedule the function more often than every 5 minutes. If the tenant produces more than 100,000 raw events a day, restrict `EPM_SET_IDS` to the sets you need.

### Test the integration

  1. In the **Cloud Scheduler** console, find your job.
  2. Click **Force run** to trigger the job manually.
  3. Wait a few seconds.
  4. Go to **Cloud Run > Services**.
  5. Click your function name (`cyberark-epm-collector`).
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         Found N sets
         Set <set-id> (<set-name>): fetching events from YYYY-MM-DDTHH:MM:SS+00:00 to YYYY-MM-DDTHH:MM:SS+00:00
         Set <set-id>: page 1 retrieved X events
         Wrote X records to gs://cyberark-epm-secops-logs/cyberark-epm/events_YYYYMMDDTHHMMSSZ.ndjson
         Successfully processed X records
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click your bucket name.

  10. Navigate to the prefix folder (`cyberark-epm/`).

  11. Verify that a new `.ndjson` file was created with the current timestamp.




If you see errors in the logs:

  * **HTTP 401** : Check `EPM_USERNAME` and `EPM_PASSWORD`, or that the sign-in was repeated within a minute
  * **HTTP 403** : The user lacks a role on the set, or the tenant's API usage limit was reached
  * **HTTP 404** : Wrong set ID in `EPM_SET_IDS`
  * **HTTP 429** : Rate limiting - function retries with backoff
  * **Missing environment variables** : Check all required variables are set



## Retrieve the Google SecOps service account

Google SecOps uses a unique service account to read data from your Cloud Storage bucket. You must grant this service account access to your bucket.

### Get the service account email

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `CyberArk EPM logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **CyberArk Endpoint Privilege Manager (EPM)** as the **Log type**.
  7. Click **Get Service Account**.
  8. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  9. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Don't use service accounts from other documentation or examples.
  10. Click **Next**.

  11. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the Cloud Storage bucket URI with the prefix path:
           
           gs://cyberark-epm-secops-logs/cyberark-epm/
           

       * Replace `cyberark-epm-secops-logs` with your Cloud Storage bucket name.
**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never delete files** : Never delete files from the source (recommended for testing).
       * **Delete transferred files and empty directories** : Delete files and empty directories from the source after a successful fetch completes.

**Note:** If you select a deletion option, the service account must have **Storage Object Admin** role instead of Storage Object Viewer. Update IAM permissions accordingly.
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days)

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)

     * **Ingestion labels** : The label to be applied to the events from this feed

  12. Click **Next**.

  13. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## Grant IAM permissions to the Google SecOps service account

The Google SecOps service account needs two roles on your Cloud Storage bucket: **Storage Object Viewer** to read the log objects, and a bucket-level role to read the bucket metadata.

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name.
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

Log Field | UDM Mapping | Logic  
---|---|---  
`accessTargetType_label` | `additional.fields` | Merged  
`accessaction_label` | `additional.fields` | Merged  
`agentEventCount_label` | `additional.fields` | Merged  
`arrivalTime_label` | `additional.fields` | Merged  
`deceptionType_label` | `additional.fields` | Merged  
`eventCount_label` | `additional.fields` | Merged  
`logonAttemptTypeId_label` | `additional.fields` | Merged  
`logonStatusId_label` | `additional.fields` | Merged  
`modificationTime_label` | `additional.fields` | Merged  
`originalFileName_label` | `additional.fields` | Merged  
`owner_label` | `additional.fields` | Merged  
`packageName_label` | `additional.fields` | Merged  
`publisher_field` | `additional.fields` | Merged  
`publisher_label` | `additional.fields` | Merged  
`setID_label` | `additional.fields` | Merged  
`skippedCount_label` | `additional.fields` | Merged  
`sourceProcessSigner_field` | `additional.fields` | Merged  
`sourceProcessSigner_label` | `additional.fields` | Merged  
`sourceType_label` | `additional.fields` | Merged  
`threatProtectionActionId_label` | `additional.fields` | Merged  
`threatProtectionAction_label` | `additional.fields` | Merged  
`user_is_admin_label` | `additional.fields` | Merged  
`winEventRecordId_label` | `additional.fields` | Merged  
`winEventType_label` | `additional.fields` | Merged  
`workingDirectory_label` | `additional.fields` | Merged  
`displayName` | `metadata.description` | Directly mapped  
`eachevent.displayName` | `metadata.description` | Directly mapped  
`lastEventDate` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`has_principal` | `metadata.event_type` | Mapped: `true` → `STATUS_UPDATE`  
`has_principal_user` | `metadata.event_type` | Mapped: `true` → `USER_UNCATEGORIZED`  
`eachevent.eventType` | `metadata.product_event_type` | Directly mapped  
`eventType` | `metadata.product_event_type` | Directly mapped  
`productName` | `metadata.product_version` | Directly mapped  
`productVersion` | `metadata.product_version` | Directly mapped  
`url` | `network.http.referral_url` | Directly mapped  
`agentId` | `principal.asset.asset_id` | Directly mapped  
`eachevent.agentId` | `principal.asset.asset_id` | Directly mapped  
`computerName` | `principal.asset.hostname` | Directly mapped  
`sourceName` | `principal.file.full_path` | Directly mapped  
`computerName` | `principal.hostname` | Directly mapped  
`eachevent.computerName` | `principal.hostname` | Directly mapped  
`operatingSystemType` | `principal.platform` | Directly mapped  
`operating_system_type` | `principal.platform` | Mapped: `Windows` → `WINDOWS`  
`company` | `principal.user.company_name` | Directly mapped  
`eachevent.userName` | `principal.user.userid` | Directly mapped  
`userName` | `principal.user.userid` | Directly mapped  
`sec_result` | `security_result` | Merged  
`threat_protection_action` | `security_result.action_details` | Directly mapped  
`fileDescription` | `security_result.description` | Directly mapped  
`eachevent.policyName` | `security_result.rule_name` | Directly mapped  
`policyName` | `security_result.rule_name` | Directly mapped  
`justification` | `security_result.summary` | Directly mapped  
`fileQualifier` | `target.asset.asset_id` | Directly mapped  
`software` | `target.asset.software` | Merged  
`eachevent.filePath` | `target.file.full_path` | Directly mapped  
`filePath` | `target.file.full_path` | Directly mapped  
`eachevent.hash` | `target.file.sha1` | Directly mapped  
`hash` | `target.file.sha1` | Directly mapped  
`fileSize` | `target.file.size` | Directly mapped  
`eachevent.processCommandLine` | `target.process.command_line` | Renamed/mapped  
`processCommandLine` | `target.process.command_line` | Directly mapped  
`fileName` | `target.process.file.names` | Merged  
`eachevent.sourceProcessCommandLine` | `target.process.parent_process.command_line` | Renamed/mapped  
`sourceProcessCommandLine` | `target.process.parent_process.command_line` | Directly mapped  
`each_event.sourceProcessHash` | `target.process.parent_process.file.sha1` | Renamed/mapped  
`sourceProcessHash` | `target.process.parent_process.file.sha1` | Directly mapped  
`sourceProcessPublisher_label` | `target.resource.attribute.labels` | Merged  
`exposed_accountName` | `target.user.attribute.labels` | Merged  
`exposed_domain` | `target.user.attribute.labels` | Merged  
`exposed_source` | `target.user.attribute.labels` | Merged  
`exposed_username` | `target.user.attribute.labels` | Merged  
`sourceProcessUsername` | `target.user.userid` | Directly mapped  
N/A | `metadata.event_type` | Constant: `STATUS_UPDATE`  
N/A | `metadata.product_name` | Constant: `EPM`  
N/A | `metadata.vendor_name` | Constant: `CYBERARK`  
N/A | `principal.platform` | Constant: `WINDOWS`  
N/A | `security_result.alert_state` | Constant: `ALERTING`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cyberark-epm-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
