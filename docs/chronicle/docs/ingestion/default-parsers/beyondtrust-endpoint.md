---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/beyondtrust-endpoint/
title: Collect BeyondTrust Endpoint Privilege Management (EPM) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:35:07.571291+00:00
---

# Collect BeyondTrust Endpoint Privilege Management (EPM) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/beyondtrust-endpoint/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect BeyondTrust Endpoint Privilege Management (EPM) logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest BeyondTrust Endpoint Privilege Management (EPM) logs to Google Security Operations using Cloud Storage. The parser focuses on transforming raw JSON log data from BeyondTrust Endpoint into a structured format conforming to the Google SecOps UDM. It first initializes default values for various fields and then parses the JSON payload, subsequently mapping specific fields from the raw log into corresponding UDM fields within the `event.idm.read_only_udm` object.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A Google Cloud project with Cloud Storage API enabled
  * Permissions to create and manage Cloud Storage buckets
  * Permissions to manage Identity and Access Management (IAM) policies on Cloud Storage buckets
  * Permissions to create Cloud Run function services, Pub/Sub topics, and Cloud Scheduler jobs
  * Privileged access to BeyondTrust Endpoint Privilege Management tenant or API



## Create a Cloud Storage bucket

  1. Go to the [Google Cloud console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `beyondtrust-epm-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Collect BeyondTrust EPM API credentials

  1. Sign in to the BeyondTrust Privilege Management web console as an administrator.
  2. Go to **Configuration > Settings > API Settings**.
  3. Click **Create an API Account**.
  4. Provide the following configuration details: 
     * **Name** : Enter `Google SecOps Collector`.
     * **API Access** : Enable **Reporting (Read Only)**. The `/management-api/v3/Events/FromStartDate` endpoint used by this collector belongs to the **Reporting** permission category. Enable **Audit (Read Only)** as well only if you also intend to collect web console activity audits.
  5. Copy and save the **Client ID** and **Client Secret**.
  6. Copy the API base URL shown at the top of the **API Settings** page. This is typically `https://<your-tenant>-services.pm.beyondtrustcloud.com`. You will use this as `BPT_API_URL`.

**Note:** Copy the value from the console rather than constructing it. Tenants administered at `app.beyondtrust.io` use a different host.



## Create a service account for Cloud Run function

The Cloud Run function needs a service account with permissions to write to the Cloud Storage bucket and be invoked by Pub/Sub.

### Create the service account

  1. In the Google Cloud console, go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `beyondtrust-epm-collector-sa`.
     * **Service account description** : Enter `Service account for Cloud Run function to collect BeyondTrust EPM logs`.
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

  * **Storage Object Admin** : Writes logs to a Cloud Storage bucket and manage state files
  * **Cloud Run Invoker** : Allows Pub/Sub to invoke the function
  * **Cloud Functions Invoker** : Allows function invocation



### Grant IAM permissions on a Cloud Storage bucket

Grant the service account write permissions on the Cloud Storage bucket:

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email. For example, `beyondtrust-epm-collector-sa@PROJECT_ID.iam.gserviceaccount.com`.
     * **Assign roles** : Select **Storage Object Admin**.
  6. Click **Save**.



## Create a Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **Google Cloud Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `beyondtrust-epm-trigger`.
     * Leave other settings as default.
  4. Click **Create**.



## Create a Cloud Run function to collect logs

The Cloud Run function is triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from BeyondTrust EPM API and writes them to Cloud Storage.

  1. In the Google Cloud console, go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function**. Use an inline editor to create a function.
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `beyondtrust-epm-collector`  
**Region** | Select the region matching your Cloud Storage bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose the topic `beyondtrust-epm-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub automatically handles authentication when invoking the function.
  7. Go to and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select the service account `beyondtrust-epm-collector-sa`.
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value  
---|---  
`GCS_BUCKET` | `beyondtrust-epm-logs`  
`GCS_PREFIX` | `beyondtrust-epm/`  
`STATE_KEY` | `beyondtrust-epm-state.json`  
`BPT_API_URL` | `https://yourtenant-services.pm.beyondtrustcloud.com`  
`CLIENT_ID` | `your-client-id`  
`CLIENT_SECRET` | `your-client-secret`  
`RECORD_SIZE` | `1000`  
`MAX_BATCHES` | `50`  
`LOOKBACK_HOURS` | `24`  
     * `RECORD_SIZE`: records per request. `/Events/FromStartDate` accepts 1 to 1000; the function clamps higher values.
     * `MAX_BATCHES`: safety limit on requests per run. If a run hits it, the cursor still advances to what was written, so the next run continues from there rather than repeating work.
     * `LOOKBACK_HOURS`: how far back the first run reaches. BeyondTrust retains passive events (codes 106, 107, 603, 706) for 30 days and all other events for 90 days, so a longer lookback returns nothing older than that.
     * `LOOKBACK_HOURS`: how far back to reach on the very first run, before any cursor exists.
**Note:** The OAuth scope (`urn:management:api`) and the API paths are fixed values and are set in the function code, so they aren't environment variables.**Note:** `STATE_KEY` points outside the log prefix on purpose. The feed ingests every object under its bucket URI and, when a deletion option is selected, deletes what it transferred. Keeping the state file out of that prefix stops it from being ingested as log data and from being deleted, which would reset collection and re-ingest duplicate events.
  10. In the **Variables & Secrets** tab go to **Requests** :

     * **Request timeout** : Enter `600` seconds (10 minutes).
  11. Go to the **Settings** tab in **Containers** :

     * In the **Resources** section: 
       * **Memory** : Select **512 MiB** or higher.
       * **CPU** : Select **1**.
     * Click **Done**.
  12. Scroll to **Execution environment** :

     * Select **Default** (recommended).
  13. In the **Revision scaling** section:

     * **Minimum number of instances** : Enter `0`.
     * **Maximum number of instances** : Enter `100` (or adjust based on expected load).
  14. Click **Create**.

  15. Wait for the service to be created (1-2 minutes).

  16. After the service is created, the **inline code editor** opens automatically.




### Add a function code

  1. Enter **main** in **Function entry point**
  2. In the inline code editor, create two files:

     * First file - **main.py:**
**Note:** The token endpoint is `/oauth/connect/token`. The PowerShell sample published with the ECS events documentation shows `/oauth/token`; that sample is wrong. Every BeyondTrust API guide from 21.7 to the current release documents `/oauth/connect/token`, and BeyondTrust's own Sentinel connector, QRadar workflow and Splunk app all call `/oauth/connect/token`. To confirm the endpoint for a specific tenant, request `https://<tenant>-services.pm.beyondtrustcloud.com/oauth/.well-known/openid-configuration` and read `token_endpoint`.
    
    import hashlib
    import json
    import os
    import re
    import time
    import urllib3
    import uuid
    from datetime import datetime, timedelta, timezone
    from urllib.parse import urlencode
    
    import functions_framework
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    from google.cloud.exceptions import NotFound
    
    # Initialize HTTP client with timeouts
    http = urllib3.PoolManager(
        timeout=urllib3.Timeout(connect=5.0, read=60.0),
        retries=False,
    )
    
    # Initialize Storage client
    storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    
    TOKEN_PATH = '/oauth/connect/token'
    # Events/FromStartDate is the endpoint BeyondTrust documents for bulk extraction:
    # "A new API is exposed to extract the events in bulk." It takes only StartDate and
    # RecordSize. Events/search is not usable here: it requires an OperatingSystem value,
    # it is a single string with no documented "all" value, so it can only ever return one
    # operating system per call.
    EVENTS_PATH = '/management-api/v3/Events/FromStartDate'
    OAUTH_SCOPE = 'urn:management:api'
    # RecordSize accepts 1 to 1000.
    MAX_RECORD_SIZE = 1000
    
    class FetchError(Exception):
        """Raised when the BeyondTrust API call fails.
    
        The cursor must never advance on a failed fetch, otherwise the events in the
        failed window are skipped permanently.
        """
    
    def rfc3339(dt: datetime) -> str:
        """Render a datetime the way StartDate accepts it: milliseconds and a literal Z."""
        return dt.astimezone(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
    
    def parse_iso(stamp: str) -> datetime:
        """Parse any ISO 8601 timestamp shape the API emits.
    
        event.ingested comes back with a +00:00 offset and up to seven fractional
        digits, e.g. 2026-08-03T13:29:55.1109163+00:00. fromisoformat's tolerance for
        long fractions varies across Python versions, so the fraction is trimmed to
        microseconds first.
        """
        text = stamp.strip()
        if text.endswith('Z'):
            text = text[:-1] + '+00:00'
        text = re.sub(r'\.(\d{1,6})\d*', r'.\1', text, count=1)
        parsed = datetime.fromisoformat(text)
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=timezone.utc)
        return parsed
    
    def canonical(stamp: str) -> str:
        """Re-render an API timestamp into the one form StartDate accepts.
    
        The API returns event.ingested as +00:00-offset ISO 8601 but rejects that
        same shape as a StartDate value with 400 "Invalid Start date format": it
        accepts only Z-suffixed values. Every timestamp that came from the API must
        pass through here before being sent back or persisted.
        """
        return rfc3339(parse_iso(stamp))
    
    def event_id(evt: dict) -> str:
        """Return the event's identity for deduplication.
    
        Falls back to a content hash when event.id is absent, so an id-less event
        still deduplicates instead of being re-ingested on every boundary re-read.
        """
        explicit = str((evt.get('event') or {}).get('id') or '')
        if explicit:
            return explicit
        digest = hashlib.sha256(
            json.dumps(evt, sort_keys=True, ensure_ascii=False).encode('utf-8')
        ).hexdigest()
        return f'sha256:{digest}'
    
    def event_ingested(evt: dict) -> str:
        """Return the Elastic ingestion timestamp, which is what StartDate filters on."""
        return str((evt.get('event') or {}).get('ingested') or '')
    
    def next_millisecond(stamp: str) -> str:
        """Return the canonical timestamp one millisecond later.
    
        Used only when a full batch fits inside a single ingestion millisecond. Without
        this the cursor cannot move and the collector stalls on that timestamp forever.
        """
        return rfc3339(parse_iso(stamp) + timedelta(milliseconds=1))
    
    @functions_framework.cloud_event
    def main(cloud_event):
        """Fetch BeyondTrust EPM events and write them to Cloud Storage as NDJSON.
    
        Args:
                cloud_event: CloudEvent object containing the Pub/Sub message.
        """
        bucket_name = os.environ.get('GCS_BUCKET')
        prefix = os.environ.get('GCS_PREFIX', 'beyondtrust-epm/')
        state_key = os.environ.get('STATE_KEY', 'beyondtrust-epm-state.json')
    
        api_url = (os.environ.get('BPT_API_URL') or '').rstrip('/')
        client_id = os.environ.get('CLIENT_ID')
        client_secret = os.environ.get('CLIENT_SECRET')
        # Clamp both ends: the API rejects RecordSize outside 1 to 1000, and a
        # misconfigured 0 would otherwise crash-loop on a 400 every run.
        record_size = min(max(int(os.environ.get('RECORD_SIZE', '1000')), 1), MAX_RECORD_SIZE)
        max_batches = int(os.environ.get('MAX_BATCHES', '50'))
        lookback_hours = int(os.environ.get('LOOKBACK_HOURS', '24'))
    
        if not all([bucket_name, api_url, client_id, client_secret]):
            raise RuntimeError(
                'Missing required environment variables: '
                'GCS_BUCKET, BPT_API_URL, CLIENT_ID, CLIENT_SECRET'
            )
    
        bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
        state = load_state(bucket, state_key)
    
        # StartDate is a rising cursor on the Elastic ingestion timestamp, not a closed
        # window. There is no EndDate on this endpoint.
    
        if [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get('last_ingested'):
            # canonical() also repairs state written by the previous script revision,
            # which persisted the API's raw +00:00 form that StartDate rejects.
            try:
                start_date = canonical(state['last_ingested'])
            except (ValueError, TypeError, AttributeError) as e:
                raise RuntimeError(
                    f'Unparseable last_ingested in gs://{bucket_name}/{state_key}: '
                    f'{state["last_ingested"]!r}. Fix or delete that object; deleting '
                    f'restarts collection from the lookback window.'
                ) from e
        else:
            start_date = rfc3339(datetime.now(timezone.utc) - timedelta(hours=lookback_hours))
    
        seen_ids = set([state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get('seen_ids', []))
        print(f'Collecting events ingested from {start_date}')
    
        token = get_oauth_token(api_url, client_id, client_secret)
        fresh, cursor, drained = fetch_events(
            api_url, token, start_date, record_size, max_batches, seen_ids
        )
    
        if not fresh:
            print('No new events. Cursor left unchanged.')
            return
    
        # Everything that can fail is computed before the upload: a crash between the
        # upload and save_state replays the batch on the next run, so the window where
        # side effects exist without recorded state must stay minimal. The retained ids
        # share the cursor millisecond, because those are exactly the ones the
        # inclusive StartDate will return again.
        retained = {
            event_id(e) for e in fresh
            if event_ingested(e) and canonical(event_ingested(e)) == cursor
        }
        if cursor == start_date:
            # The cursor millisecond did not advance, so ids retained by earlier runs
            # are still on the boundary; dropping them would re-ingest their events.
            retained |= seen_ids
    
        timestamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
        # The random suffix keeps concurrent executions (Pub/Sub delivers at least
        # once) from overwriting each other's object within the same second.
        filename = (
            f'{prefix}beyondtrust-epm-events-{timestamp}-'
            f'{uuid.uuid4().hex[:8]}.ndjson'
        )
        ndjson = '\n'.join(json.dumps(e, ensure_ascii=False) for e in fresh) + '\n'
        bucket.blob(filename).[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
            ndjson, content_type='application/x-ndjson'
        )
        print(f'Wrote {len(fresh)} events to gs://{bucket_name}/{filename}')
    
        save_state(bucket, state_key, {
            'last_ingested': cursor,
            'seen_ids': sorted(retained),
            'updated_at': rfc3339(datetime.now(timezone.utc)),
        })
    
        if not drained:
            print(
                f'Stopped after {max_batches} batches with more events available. '
                'The cursor advanced, so the next run continues from here.'
            )
    
    def fetch_events(api_url, token, start_date, record_size, max_batches, seen_ids):
        """Read forward from start_date until the API returns a short batch.
    
        The response envelope has no page count and no next-page token, so a batch
        shorter than record_size is the only documented end-of-data signal.
    
        StartDate is inclusive and the cursor lands on the newest event's timestamp, so
        every batch re-returns the events sharing it. Deduplication by event id therefore
        has to happen as batches arrive, not only between runs.
    
        Returns:
        Tuple of (new events, cursor to persist, whether the stream was drained).
    
        Raises:
        FetchError: on any API or transport failure, so the caller cannot mistake a
        failed fetch for an empty result and advance the cursor.
        """
        headers = {
            'Authorization': f'Bearer {token}',
            'Accept': 'application/json',
        }
    
        all_events = []
        seen = set(seen_ids)
        cursor = start_date
    
        for batch in range(1, max_batches + 1):
            query = urlencode({'StartDate': cursor, 'RecordSize': record_size})
            body = request_with_retry(f'{api_url}{EVENTS_PATH}?{query}', headers)
    
            events = body.get('events') or []
            new = [e for e in events if event_id(e) not in seen]
            seen.update(event_id(e) for e in events if event_id(e))
            all_events.extend(new)
            print(f'Batch {batch}: {len(events)} events, {len(new)} new')
    
            # Termination is judged on what the API returned, not on what survived
            # deduplication: a batch can be full and still be entirely duplicates.
            # The newest stamp in the batch, not events[-1]: ordering is a client-side
            # convention, not a documented guarantee, and a misordered tail would
            # regress the cursor and re-ingest events already written.
            stamps = [canonical(s) for s in (event_ingested(e) for e in events) if s]
    
            if len(events) < record_size:
                # Short batch: the stream is drained.
                if events and not stamps:
                    print(
                        'Warning: no event in the final batch carries event.ingested; '
                        'cursor left unchanged.'
                    )
                if stamps:
                    cursor = max(max(stamps), cursor)
                return all_events, cursor, True
    
            if not stamps:
                raise FetchError(
                    'No event in a full batch carries event.ingested, '
                    'so the cursor cannot advance'
                )
            batch_max = max(stamps)
            if batch_max <= cursor:
                # A full batch fits inside one ingestion millisecond. Stepping past it is the only
                # way to make progress; holding the cursor here stalls collection forever.
                # Events beyond record_size at that exact millisecond are unreachable, which
                # needs more than 1000 events in one millisecond.
                print(
                    f'Warning: a full batch shares ingestion timestamp {batch_max}; '
                    'stepping past it. Events beyond RecordSize at that timestamp are skipped.'
                )
                cursor = next_millisecond(cursor)
            else:
                cursor = batch_max
    
        return all_events, cursor, False
    
    def request_with_retry(url, headers, attempts=4):
        """GET with backoff on 429 and 5xx.
    
        The documented rate limit is 1000 requests per 100 seconds.
        """
        backoff = 1.0
        for attempt in range(1, attempts + 1):
            try:
                response = http.request('GET', url, headers=headers)
            except Exception as e:
                raise FetchError(f'Request to {url} failed: {e}') from e
    
            if response.status in (429, 500, 502, 503, 504) and attempt < attempts:
                retry_after = response.headers.get('Retry-After')
                try:
                    delay = int(retry_after) if retry_after else backoff
                except (TypeError, ValueError):
                    delay = backoff
                # Retry-After is server-controlled input: bound it so a bogus value
                # cannot sleep past the function timeout or crash time.sleep.
                delay = min(max(delay, 1.0), 60.0)
                print(f'HTTP {response.status}. Retrying in {delay}s...')
                time.sleep(delay)
                backoff = min(backoff * 2, 30.0)
                continue
    
            if response.status != 200:
                raise FetchError(
                    f'Request failed: {response.status} {response.data.decode("utf-8")}'
                )
    
            text = response.data.decode('utf-8')
            # BeyondTrust's sample folds "Owner" into "owner" before parsing, but that
            # workaround exists for PowerShell's case-insensitive ConvertFrom-Json.
            # Python parses case-sensitively, and the SecOps parser maps file.Owner.*
            # and file.owner to different UDM fields, so both keys must survive.
            try:
                return json.loads(text)
            except json.JSONDecodeError as e:
                raise FetchError(f'Malformed JSON response: {e}') from e
    
        raise FetchError(f'Giving up on {url} after {attempts} attempts')
    
    def get_oauth_token(api_url, client_id, client_secret):
        """Get an access token using the OAuth client credentials flow.
    
        The token is valid for one hour.
        """
        body = urlencode({
            'grant_type': 'client_credentials',
            'client_id': client_id,
            'client_secret': client_secret,
            'scope': OAUTH_SCOPE,
        })
        response = http.request(
            'POST',
            f'{api_url}{TOKEN_PATH}',
            body=body,
            headers={'Content-Type': 'application/x-www-form-urlencoded'},
        )
        if response.status != 200:
            raise FetchError(
                f'Token request failed: {response.status} '
                f'{response.data.decode("utf-8")}'
            )
        return json.loads(response.data.decode('utf-8'))['access_token']
    
    def load_state(bucket, key):
        """Read the collector state from Cloud Storage.
    
        Only a missing object is a cold start. Any other error is raised: swallowing it
        would reset collection to the lookback window and re-ingest that period.
        """
        blob = bucket.blob(key)
        try:
            return json.loads(blob.[download_as_text](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_download_as_text)())
        except NotFound:
            print('No state file found. Starting from the lookback window.')
            return {}
    
    def save_state(bucket, key, state):
        """Write the collector state to Cloud Storage.
    
        Failures are raised, not logged. A run that cannot record its cursor must fail,
        otherwise the next run repeats the same window.
        """
        bucket.blob(key).[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
            json.dumps(state, indent=2), content_type='application/json'
        )
        print(f"Saved state: last_ingested={[state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get('last_ingested')}")
    

**Note:** This script is provided as an example and is not officially supported. We welcome feedback about how we can improve it. To submit feedback, click **Send Feedback > Google SecOps Security Product Feedback** on this page.

     * Second file: **requirements.txt:**
    
    functions-framework==3.*
    google-cloud-storage==2.*
    urllib3>=2.0.0
    

  3. Click **Deploy** to save and deploy the function.

  4. Wait for deployment to complete (2-3 minutes).

**Note:** The Pub/Sub trigger configuration automatically creates the necessary subscriptions and permissions.



## Create a Cloud Scheduler job

Cloud Scheduler publishes messages to the Pub/Sub topic at regular intervals, triggering the Cloud Run function.

  1. In the Google Cloud console, go to **Cloud Scheduler**.
  2. Click **Create Job**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | `beyondtrust-epm-collector-hourly`  
**Region** | Select the same region as the Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the topic `beyondtrust-epm-trigger`  
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
  
### Test the scheduler job

  1. In the **Cloud Scheduler** console, find your job.
  2. Click **Force run** to trigger manually.
  3. Wait a few seconds and go to **Cloud Run > Services > beyondtrust-epm-collector > Logs**.
  4. Verify the function executed successfully.
  5. Check the Cloud Storage bucket to confirm logs were written.



## Retrieve the Google SecOps service account

Google SecOps uses a unique service account to read data from your Cloud Storage bucket. You must grant this service account access to your bucket.

### Get the service account email

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `BeyondTrust EPM logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **BeyondTrust Endpoint Privilege Management** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Don't use service accounts from other documentation or examples.



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



## Configure a feed in Google SecOps to ingest BeyondTrust EPM logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `BeyondTrust EPM logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **BeyondTrust Endpoint Privilege Management** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the Cloud Storage bucket URI with the prefix path:
           
           gs://beyondtrust-epm-logs/beyondtrust-epm/
           

       * **Replace:**

         * `beyondtrust-epm-logs`: Your Cloud Storage bucket name.
         * `beyondtrust-epm/`: Optional prefix/folder path where logs are stored (leave empty for root).
       * **Examples:**

         * Root bucket: `gs://beyondtrust-epm-logs/`
         * With prefix: `gs://beyondtrust-epm-logs/beyondtrust-epm/`
**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never delete files** : Never delete files from the source. This is recommended for testing purposes.
       * **Delete transferred files and empty directories** : Delete files and empty directories from the source after a successful fetch completes.

**Note:** Grant both roles. **Storage Object Viewer** does not grant the bucket-level permission the feed needs, and the **Storage Legacy Bucket** roles do not grant permission to read object contents.
     * **Maximum File Age** : Include files modified in the last number of days. Default is 180 days.

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).

     * **Ingestion labels** : The label to be applied to the events from this feed.

  9. Click **Next**.

  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`DomainIdentifier_label` | `additional.fields` | Merged  
`WatsonEventType_label` | `additional.fields` | Merged  
`action_label` | `additional.fields` | Merged  
`activity_id_label` | `additional.fields` | Merged  
`app_id_label` | `additional.fields` | Merged  
`app_insights_instrumentation_key_label` | `additional.fields` | Merged  
`asimov_instrumentation_key_label` | `additional.fields` | Merged  
`authorization_request_control_authorization_label` | `additional.fields` | Merged  
`bundle_name_label` | `additional.fields` | Merged  
`changedBy_label` | `additional.fields` | Merged  
`code_signature_subject_name_label` | `additional.fields` | Merged  
`collector_api_key_label` | `additional.fields` | Merged  
`command_label` | `additional.fields` | Merged  
`configuration_application_group_description_label` | `additional.fields` | Merged  
`configuration_application_group_identifier_label` | `additional.fields` | Merged  
`configuration_application_group_name_label` | `additional.fields` | Merged  
`configuration_application_identifier_label` | `additional.fields` | Merged  
`configuration_application_type_label` | `additional.fields` | Merged  
`configuration_identifier_label` | `additional.fields` | Merged  
`configuration_message_identifier_label` | `additional.fields` | Merged  
`configuration_message_name_label` | `additional.fields` | Merged  
`configuration_message_type_label` | `additional.fields` | Merged  
`configuration_name_label` | `additional.fields` | Merged  
`configuration_revision_number_label` | `additional.fields` | Merged  
`configuration_rule_identifier_label` | `additional.fields` | Merged  
`configuration_rule_on_demand_label` | `additional.fields` | Merged  
`configuration_rule_script_outcome_rule_affected_label` | `additional.fields` | Merged  
`configuration_token_identifier_label` | `additional.fields` | Merged  
`configuration_token_name_label` | `additional.fields` | Merged  
`configuration_workstyle_description_label` | `additional.fields` | Merged  
`configuration_workstyle_identifier_label` | `additional.fields` | Merged  
`configuration_workstyle_name_label` | `additional.fields` | Merged  
`content_length_label` | `additional.fields` | Merged  
`content_type_label` | `additional.fields` | Merged  
`domainNetBIOSName_label` | `additional.fields` | Merged  
`domain_label` | `additional.fields` | Merged  
`entity_label` | `additional.fields` | Merged  
`entity_name_label` | `additional.fields` | Merged  
`event_action_label` | `additional.fields` | Merged  
`exitstatus_label` | `additional.fields` | Merged  
`file_hash_md5_label` | `additional.fields` | Merged  
`file_hash_sha1_label` | `additional.fields` | Merged  
`file_hash_sha256_label` | `additional.fields` | Merged  
`file_version_label` | `additional.fields` | Merged  
`gid_label` | `additional.fields` | Merged  
`group_data_id_label` | `additional.fields` | Merged  
`group_id_label` | `additional.fields` | Merged  
`group_label` | `additional.fields` | Merged  
`handle_label` | `additional.fields` | Merged  
`host_name_label` | `additional.fields` | Merged  
`host_uptime_labels` | `additional.fields` | Merged  
`http_host_label` | `additional.fields` | Merged  
`id_label` | `additional.fields` | Merged  
`iolog_label` | `additional.fields` | Merged  
`is_opted_in_label` | `additional.fields` | Merged  
`linenum_label` | `additional.fields` | Merged  
`local_identifier_label` | `additional.fields` | Merged  
`locale_label` | `additional.fields` | Merged  
`master_utcoffset_label` | `additional.fields` | Merged  
`masterlocale_label` | `additional.fields` | Merged  
`owner_identifier_label` | `additional.fields` | Merged  
`parent_entity_id_label` | `additional.fields` | Merged  
`parent_process_exec_label` | `additional.fields` | Merged  
`parent_process_label` | `additional.fields` | Merged  
`pbmasterdnodename_label` | `additional.fields` | Merged  
`pipeName_label` | `additional.fields` | Merged  
`process_entity_id_label` | `additional.fields` | Merged  
`process_hash_label` | `additional.fields` | Merged  
`process_name_label` | `additional.fields` | Merged  
`process_parent_name_label` | `additional.fields` | Merged  
`process_start_time_label` | `additional.fields` | Merged  
`processexe_label` | `additional.fields` | Merged  
`product_label` | `additional.fields` | Merged  
`product_type_label` | `additional.fields` | Merged  
`product_version_label` | `additional.fields` | Merged  
`requestuser_label` | `additional.fields` | Merged  
`runargv_label` | `additional.fields` | Merged  
`runcwd_label` | `additional.fields` | Merged  
`runeffectivegroup_label` | `additional.fields` | Merged  
`runeffectiveuser_label` | `additional.fields` | Merged  
`runhost_label` | `additional.fields` | Merged  
`schema_version_label` | `additional.fields` | Merged  
`sku_name_label` | `additional.fields` | Merged  
`telemetry_level_label` | `additional.fields` | Merged  
`tenant_id_label` | `additional.fields` | Merged  
`type_label` | `additional.fields` | Merged  
`uid_label` | `additional.fields` | Merged  
`user_id_label` | `additional.fields` | Merged  
`user_name_label` | `additional.fields` | Merged  
`vs_exe_version_label` | `additional.fields` | Merged  
`inter_host` | `intermediary.hostname` | Directly mapped  
`Processes.description` | `metadata.description` | Directly mapped  
`details` | `metadata.description` | Directly mapped  
`event_data.reason` | `metadata.description` | Directly mapped  
`file.pe.description` | `metadata.description` | Directly mapped  
`created` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`datetime` | `metadata.event_timestamp` | Parsed as `MMM dd HH:mm:ss`  
`has_principal` | `metadata.event_type` | Mapped: `true` → `STATUS_UPDATE`  
`has_user` | `metadata.event_type` | Mapped: `true` → `USER_UNCATEGORIZED`  
`parent_working_directory_label` | `metadata.ingestion_labels` | Merged  
`working_directory_label` | `metadata.ingestion_labels` | Merged  
`auditType` | `metadata.product_event_type` | Directly mapped  
`event_datas.ActionId` | `metadata.product_log_id` | Directly mapped  
`labels.related_item_id` | `metadata.product_log_id` | Directly mapped  
`uniqueid` | `metadata.product_log_id` | Directly mapped  
`masterdversion` | `metadata.product_version` | Directly mapped  
`headers.http_version` | `network.application_protocol_version` | Directly mapped  
`headers.request_method` | `network.http.method` | Directly mapped  
`host.os.platform` | `principal.administrative_domain` | Directly mapped  
`Processes.process` | `principal.application` | Directly mapped  
`agent_ephemeral_id_label` | `principal.asset.attribute.labels` | Merged  
`agent_id_label` | `principal.asset.attribute.labels` | Merged  
`agent_version_label` | `principal.asset.attribute.labels` | Merged  
`ecs_version_label` | `principal.asset.attribute.labels` | Merged  
`_hardware` | `principal.asset.hardware` | Merged  
`host.hostname` | `principal.asset.hostname` | Directly mapped  
`submithost` | `principal.asset.hostname` | Directly mapped  
`ip_address` | `principal.asset.ip` | Merged  
`masterhostip` | `principal.asset.ip` | Merged  
`submithostip` | `principal.asset.ip` | Merged  
`file.path` | `principal.file.full_path` | Directly mapped  
`lineinfile` | `principal.file.full_path` | Directly mapped  
`host.hostname` | `principal.hostname` | Directly mapped  
`submithost` | `principal.hostname` | Directly mapped  
`ip_address` | `principal.ip` | Merged  
`masterhostip` | `principal.ip` | Merged  
`submithostip` | `principal.ip` | Merged  
`mac` | `principal.mac` | Merged  
`host.os.name` | `principal.platform_version` | Directly mapped  
`host.os.version` | `principal.platform_version` | Directly mapped  
`process.command_line` | `principal.process.command_line` | Directly mapped  
`runcommand` | `principal.process.command_line` | Directly mapped  
`process.executable` | `principal.process.file.full_path` | Directly mapped  
`cmd` | `principal.process.parent_process.command_line` | Directly mapped  
`Processes.process_path` | `principal.process.parent_process.file.full_path` | Directly mapped  
`process.parent.executable` | `principal.process.parent_process.file.full_path` | Directly mapped  
`Processes.parent_process_id` | `principal.process.parent_process.pid` | Directly mapped  
`Processes.process_id` | `principal.process.pid` | Directly mapped  
`logpid` | `principal.process.pid` | Directly mapped  
`file.Owner.DomainName` | `principal.user.company_name` | Directly mapped  
`file.Owner.Name` | `principal.user.user_display_name` | Directly mapped  
`runuser` | `principal.user.user_display_name` | Directly mapped  
`userName` | `principal.user.user_display_name` | Directly mapped  
`Processes.user` | `principal.user.userid` | Directly mapped  
`userId` | `principal.user.userid` | Directly mapped  
`userid` | `principal.user.userid` | Directly mapped  
`Processes.user_id` | `principal.user.windows_sid` | Directly mapped  
`EPMWinMac.Configuration.Rule.Action` | `security_result.action` | Merged  
`security_result_action` | `security_result.action` | Merged  
`event_data.outcome` | `security_result.category_details` | Merged  
`host.os.version` | `security_result.category_details` | Merged  
`EPMWinMac.Configuration.Application.Description` | `security_result.description` | Directly mapped  
`EPMWinMac.Configuration.Message.Description` | `security_result.description` | Directly mapped  
`host.os.type` | `src.administrative_domain` | Directly mapped  
`file.name` | `src.file.names` | Merged  
`host.os.full` | `src.platform_version` | Directly mapped  
`host.os.family` | `target.administrative_domain` | Directly mapped  
`Processes.dest` | `target.asset.hostname` | Directly mapped  
`file.extension` | `target.file.mime_type` | Directly mapped  
`Processes.dest` | `target.hostname` | Directly mapped  
`host.domain` | `target.hostname` | Directly mapped  
`file_DriveType_label` | `target.resource.attribute.labels` | Merged  
`file_drive_letter_label` | `target.resource.attribute.labels` | Merged  
`owner_label` | `target.resource.attribute.labels` | Merged  
N/A | `metadata.event_type` | Constant: `USER_UNCATEGORIZED`  
N/A | `metadata.product_name` | Constant: `Beyondtrust Privilege Management`  
N/A | `metadata.vendor_name` | Constant: `Beyondtrust Privilege Management`  
N/A | `network.application_protocol` | Constant: `HTTP`  
N/A | `principal.platform` | Constant: `MAC`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/beyondtrust-endpoint-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
