---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/proofpoint-tap-threats/
title: Collect Proofpoint TAP Threats logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:16:56.436010+00:00
---

# Collect Proofpoint TAP Threats logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/proofpoint-tap-threats/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Proofpoint TAP Threats logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Proofpoint TAP Threats logs to Google Security Operations using Cloud Storage V2. Proofpoint Targeted Attack Protection (TAP) is an advanced email security platform that detects, analyzes, and blocks threats delivered through email, including malicious attachments and URLs. The TAP Threat API returns a summary of each threat that TAP has identified in your environment: its classification, status, severity, detection type, and the threat actors, malware families, techniques, and brands associated with it. A Cloud Run function discovers the threats observed in your environment through the TAP SIEM API and writes their Threat API summaries to a Cloud Storage bucket, from which Google SecOps ingests them.

**Note:** The `PROOFPOINT_TAP_THREATS` log type carries threat summaries from the Threat API, not the blocked and delivered message and click events of the SIEM API. To ingest those events, configure the **Proofpoint TAP** (`PROOFPOINT_MAIL`) feed, which reads the SIEM API directly; see [Collect Proofpoint TAP logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/proofpoint-mail). Both feeds can run side by side against the same TAP credentials.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A Google Cloud project with Cloud Storage API enabled
  * Permissions to create and manage Cloud Storage buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * A Proofpoint TAP subscription with access to the Threat Insight Dashboard
  * TAP API service credentials (Service Principal and Secret) with permissions to access the SIEM API



## Generate Proofpoint TAP API service credentials

  1. Sign in to the **Proofpoint TAP Threat Insight Dashboard**.
  2. Go to **Settings > Connected Applications > Service Credentials**.
  3. Click **Create New Credential**.
  4. In the **Generated Service Credential** dialog, copy and securely store the following:

     * **Service Principal** : The principal identifier used for API authentication
     * **Secret** : The secret key used for API authentication
**Note:** The Secret is displayed only once during creation. If you lose it, you must generate a new credential. Service credentials are required for all TAP API requests and use HTTP Basic Authentication.



### Verify API access

  * Test your credentials before proceeding with the integration as follows:
        
        PRINCIPAL="your-service-principal"
        SECRET="your-secret"
        
        # Test SIEM API access (fetch last hour of events)
        curl -s "https://tap-api-v2.proofpoint.com/v2/siem/all?format=json&sinceSeconds=3600" \
          --user "${PRINCIPAL}:${SECRET}"
        

A successful response returns a JSON object containing `messagesBlocked`, `messagesDelivered`, `clicksBlocked`, and `clicksPermitted` arrays. If you receive a `401` error, verify that your Service Principal and Secret are correct. If you receive a `403` error, confirm that your account has TAP API access enabled.

Then take a `threatID` value from any event in that response and test the Threat API, which is the source of the records this guide ingests:
        
        THREAT_ID="<threatID from a SIEM event>"
        
        curl -s "https://tap-api-v2.proofpoint.com/v2/threat/summary/${THREAT_ID}" \
          --user "${PRINCIPAL}:${SECRET}"
        

A successful response is a JSON object with `id`, `identifiedAt`, `name`, `type`, `category`, `status`, and the `actors`, `families`, `malware`, `techniques`, and `brands` arrays. If the SIEM response had no events, the environment has had no TAP-identified threats in the last hour; the function still runs correctly and writes nothing until a threat appears.




## Create a Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `proofpoint-tap-threats-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Create a service account for the Cloud Run function

The Cloud Run function needs a service account with permissions to write to a Cloud Storage bucket and be invoked by Pub/Sub.

### Create the service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `tap-threats-collector-sa`
     * **Service account description** : Enter `Service account for Cloud Run function to collect Proofpoint TAP Threats logs`
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

  * **Storage Object Admin** : Write threat event data to Cloud Storage bucket and manage state files
  * **Cloud Run Invoker** : Allow Pub/Sub to invoke the function
  * **Cloud Functions Invoker** : Allow function invocation



### Grant Identity and Access Management (IAM) permissions on the Cloud Storage bucket

Grant the service account write permissions on the Cloud Storage bucket:

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `tap-threats-collector-sa@PROJECT_ID.iam.gserviceaccount.com`)
     * **Assign roles** : Select **Storage Object Admin**
  6. Click **Save**.



## Create a Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `tap-threats-collector-trigger`
     * Leave other settings as default
  4. Click **Create**.



## Create the Cloud Run function to collect threat events

  * The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler. It reads the TAP SIEM API to find the threat IDs observed in your environment, fetches the summary of each threat from the TAP Threat API, and writes the summaries to Cloud Storage.


  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Write a function**.
  3. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `tap-threats-collector`  
**Region** | Select region matching your Cloud Storage bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  4. In the **Trigger** section, click **Add trigger** and select **Pub/Sub trigger**.

  5. In the **Eventarc trigger** pane, provide the following configuration details:

     * **Trigger name** : Keep the generated name or enter a name for the trigger.
     * **Trigger type** : Select **Google Sources**.
     * **Event provider** : Select **Pub/Sub**.
     * **Event type** : Select **google.cloud.pubsub.topic.v1.messagePublished**.
     * **Select a Cloud Pub/Sub topic** : Choose the topic `tap-threats-collector-trigger`.
     * **Region** : Select the same region as the function.
     * **Service account** : Select the service account `tap-threats-collector-sa`.
  6. Click **Save trigger**.

**Note:** The trigger options come from Eventarc. If **Pub/Sub trigger** is not listed, enable the **Eventarc API** for the project and reload the page. If the pane reports that the service account is missing the **Eventarc Event Receiver** or **Cloud Run Invoker** role, click **Grant**.
  7. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Select **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  8. Navigate to and expand **Containers, Networking, Security**.

  9. Go to the **Security** tab:

     * **Service account** : Select the service account `tap-threats-collector-sa`
  10. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `proofpoint-tap-threats-logs` | Cloud Storage bucket name  
`GCS_PREFIX` | `tap-threats` | Prefix for log files  
`STATE_KEY` | `tap-threats-state.json` | State path, outside the log prefix  
`TAP_PRINCIPAL` | `your-service-principal` | TAP API Service Principal  
`TAP_SECRET` | `your-secret` | TAP API Secret  
`LOOKBACK_HOURS` | `24` | Initial discovery window in hours on first run (max 168, the SIEM API limit)  
`OVERLAP_MINUTES` | `10` | Re-read window before the watermark, to catch late-indexed SIEM events  
`MAX_THREATS` | `500` | Max threat summaries fetched per run; the rest stay queued in the state file  
`SEEN_RETENTION_DAYS` | `7` | Days a threat ID is remembered after it was last seen  
**Note:** `STATE_KEY` points outside the log prefix on purpose. The feed ingests every object under its bucket URI and, when a deletion option is selected, deletes what it transferred. Keeping the state file out of that prefix stops it from being ingested as log data and from being deleted, which would reset collection and re-ingest duplicate events.
  11. In the **Variables & Secrets** section, go to **Requests** :

     * **Request timeout** : Enter `540` seconds (9 minutes)
  12. Go to the **Settings** tab:

     * In the **Resources** section: 
       * **Memory** : Select **512 MiB** or higher
       * **CPU** : Select **1**
  13. In the **Revision scaling** section:

     * **Minimum number of instances** : Enter `0`
     * **Maximum number of instances** : Enter `100` (or adjust based on expected load)
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
    import base64
    import hashlib
    import json
    import os
    import urllib3
    from urllib.parse import quote
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
    GCS_PREFIX = os.environ.get('GCS_PREFIX', 'tap-threats')
    # STATE_KEY must stay OUTSIDE GCS_PREFIX. The feed ingests every object under
    # its bucket URI and, with a deletion option selected, deletes what it
    # transferred. A state file inside the prefix would be ingested as log data and
    # then deleted, resetting collection and re-ingesting duplicates.
    STATE_KEY = os.environ.get('STATE_KEY', 'tap-threats-state.json')
    API_BASE = os.environ.get('TAP_API_BASE', 'https://tap-api-v2.proofpoint.com')
    TAP_PRINCIPAL = os.environ.get('TAP_PRINCIPAL')
    TAP_SECRET = os.environ.get('TAP_SECRET')
    # The SIEM API accepts at most 7 days of lookback.
    LOOKBACK_HOURS = min(int(os.environ.get('LOOKBACK_HOURS', '24')), 168)
    # The discovery query re-reads this many minutes before the watermark so that
    # events the SIEM API indexes late still surface their threat IDs.
    OVERLAP_MINUTES = int(os.environ.get('OVERLAP_MINUTES', '10'))
    # Maximum threat summaries fetched per run. The rest stay queued in the state.
    MAX_THREATS = int(os.environ.get('MAX_THREATS', '500'))
    # Days a threat ID stays in the state after it was last seen in SIEM events.
    SEEN_RETENTION_DAYS = int(os.environ.get('SEEN_RETENTION_DAYS', '7'))
    
    class FetchError(Exception):
        """Raised when a Proofpoint API call fails.
    
        The watermark must never advance on a failed fetch, otherwise the threats
        referenced in the failed window are never looked up.
        """
    
    def parse_datetime(value: str) -> datetime:
        """Parse an ISO 8601 datetime string into an aware datetime."""
        if [value](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.ObjectCustomContextPayload.html#google_cloud_storage_blob_ObjectCustomContextPayload_value).endswith('Z'):
            value = value[:-1] + '+00:00'
        dt = datetime.fromisoformat(value)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt
    
    def tap_time(dt: datetime) -> str:
        """Render a datetime in the YYYY-MM-DDThh:mm:ssZ form the SIEM API accepts."""
        return dt.astimezone(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    
    def auth_header() -> str:
        """Build the HTTP Basic header from the service principal and secret."""
        token = base64.b64encode(f'{TAP_PRINCIPAL}:{TAP_SECRET}'.encode('utf-8')).decode('utf-8')
        return f'Basic {token}'
    
    def content_hash(record: dict) -> str:
        """Hash a threat summary so an unchanged summary is not written twice."""
        return hashlib.sha256(
            json.dumps(record, sort_keys=True, ensure_ascii=False).encode('utf-8')
        ).hexdigest()
    
    @functions_framework.cloud_event
    def main(cloud_event):
        """Discover threat IDs in TAP SIEM events and write their Threat API summaries.
    
        The PROOFPOINT_TAP_THREATS parser reads the Threat API summary schema, not the
        SIEM API events. The SIEM API is used only to find which threat IDs were
        observed; every message and click event for those threats is what the
        Proofpoint TAP (PROOFPOINT_MAIL) feed carries.
    
        Args:
            cloud_event: CloudEvent object containing the Pub/Sub message.
        """
        if not all([GCS_BUCKET, TAP_PRINCIPAL, TAP_SECRET]):
            # Raise rather than return: a bare return acks the Pub/Sub message and
            # reports the run as successful, silently discarding the schedule tick.
            raise RuntimeError('Missing required environment variables')
    
        bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(GCS_BUCKET)
        state = load_state(bucket, STATE_KEY)
    
        now = datetime.now(timezone.utc)
        watermark = None
        if [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get('last_event_time'):
            watermark = parse_datetime(state['last_event_time'])
        # threat_id -> {'hash': sha256 of the last written summary, 'seen': ISO time}
        seen = [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get('seen_threats', {})
        pending = list([state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get('pending_threat_ids', []))
    
        if watermark is None:
            start_time = now - timedelta(hours=LOOKBACK_HOURS)
        else:
            start_time = max(watermark - timedelta(minutes=OVERLAP_MINUTES), now - timedelta(days=7))
    
        headers = {
            'Authorization': auth_header(),
            'Accept': 'application/json',
            'User-Agent': 'GoogleSecOps-TAPThreatsCollector/2.0',
        }
    
        print(f"Discovering threats in SIEM events from {start_time.isoformat()} to {now.isoformat()}")
    
        # A FetchError here propagates: the run fails, the watermark is untouched,
        # and the next invocation retries the same window.
        discovered, newest_event_time = discover_threat_ids(headers, start_time, now)
    
        for threat_id in discovered:
            seen.setdefault(threat_id, {})['seen'] = now.isoformat()
            if threat_id not in pending:
                pending.append(threat_id)
        print(f"Discovered {len(discovered)} threat IDs, {len(pending)} queued for lookup")
    
        batch = pending[:MAX_THREATS]
        fresh = []
        for threat_id in batch:
            summary = fetch_threat_summary(headers, threat_id)
            if summary is None:
                # The Threat API has no summary for this ID; drop it from the queue.
                seen.setdefault(threat_id, {})['seen'] = now.isoformat()
                continue
            digest = content_hash(summary)
            if seen.get(threat_id, {}).get('hash') == digest:
                # Unchanged since it was last written; nothing new to ingest.
                continue
            fresh.append((threat_id, digest, summary))
        remaining = pending[len(batch):]
        if remaining:
            print(f"Reached max_threats limit ({MAX_THREATS}); {len(remaining)} threat IDs stay queued")
    
        # Forget threat IDs not seen for SEEN_RETENTION_DAYS so the state stays small.
        cutoff = now - timedelta(days=SEEN_RETENTION_DAYS)
        seen = {
            tid: info for tid, info in seen.items()
            if info.get('seen') and parse_datetime(info['seen']) >= cutoff
        }
    
        if fresh:
            timestamp = now.strftime('%Y%m%dT%H%M%SZ')
            object_key = f"{GCS_PREFIX}/threats_{timestamp}.ndjson"
            blob = bucket.blob(object_key)
            ndjson = '\n'.join(json.dumps(summary, ensure_ascii=False) for _, _, summary in fresh) + '\n'
            blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(ndjson, content_type='application/x-ndjson')
            print(f"Wrote {len(fresh)} threat summaries to gs://{GCS_BUCKET}/{object_key}")
            for threat_id, digest, _ in fresh:
                seen.setdefault(threat_id, {})['hash'] = digest
        else:
            print("No new or changed threat summaries.")
    
        # Advance the watermark only after the data is durably written. When the
        # window held no events at all, keep the old watermark so a late-indexed
        # event is still picked up by the next overlap.
        new_watermark = watermark
        if newest_event_time:
            candidate = parse_datetime(newest_event_time)
            if new_watermark is None or candidate > new_watermark:
                new_watermark = candidate
    
        save_state(bucket, STATE_KEY, {
            'last_event_time': new_watermark.isoformat() if new_watermark else None,
            'seen_threats': seen,
            'pending_threat_ids': remaining,
        })
    
        print(f"Successfully processed {len(fresh)} threat summaries")
    
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
        print(f"Saved state: last_event_time={[state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get('last_event_time')}, "
              f"{len([state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get('seen_threats', {}))} known threats, "
              f"{len([state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get('pending_threat_ids', []))} pending")
    
    def request_json(url: str, headers: dict):
        """Call a TAP API endpoint and return the decoded JSON body.
    
        Returns None on HTTP 404, which the Threat API uses for an unknown ID.
        Raises FetchError on any other transport or HTTP failure, so that the
        caller does not mistake a failed call for an empty result.
        """
        backoff = 1.0
        for attempt in range(5):
            try:
                response = http.request('GET', url, headers=headers)
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
                backoff = min(backoff * 2, 60.0)
                continue
    
            if response.status == 404:
                return None
    
            if response.status != 200:
                raise FetchError(f'HTTP {response.status} from {url}: {response.data.decode("utf-8", "replace")[:500]}')
    
            try:
                return json.loads(response.data.decode('utf-8'))
            except json.JSONDecodeError as e:
                raise FetchError(f'Malformed JSON response from {url}: {e}') from e
    
        raise FetchError('Rate limited repeatedly; giving up without advancing the watermark')
    
    def discover_threat_ids(headers: dict, start_time: datetime, end_time: datetime):
        """Read TAP SIEM events in one-hour windows and collect the threat IDs they reference.
    
        Returns:
            Tuple of (ordered list of unique threat IDs, newest event time ISO string).
        """
        threat_ids = []
        newest_time = None
        current_start = start_time
    
        while current_start < end_time:
            # The SIEM API allows at most one hour per request.
            current_end = min(current_start + timedelta(hours=1), end_time)
            interval = f'{tap_time(current_start)}/{tap_time(current_end)}'
            url = f'{API_BASE}/v2/siem/all?format=json&interval={quote(interval, safe="/:")}'
    
            data = request_json(url, headers)
            if data is None:
                raise FetchError(f'SIEM API returned 404 for interval {interval}')
    
            window_count = 0
            for key in ('messagesBlocked', 'messagesDelivered'):
                for message in data.get(key) or []:
                    window_count += 1
                    stamp = message.get('messageTime')
                    for info in message.get('threatsInfoMap') or []:
                        tid = info.get('threatID')
                        if tid and tid not in threat_ids:
                            threat_ids.append(tid)
                        stamp = stamp or info.get('threatTime')
                    if stamp and (newest_time is None or parse_datetime(stamp) > parse_datetime(newest_time)):
                        newest_time = stamp
            for key in ('clicksBlocked', 'clicksPermitted'):
                for click in data.get(key) or []:
                    window_count += 1
                    tid = click.get('threatID')
                    if tid and tid not in threat_ids:
                        threat_ids.append(tid)
                    stamp = click.get('clickTime') or click.get('threatTime')
                    if stamp and (newest_time is None or parse_datetime(stamp) > parse_datetime(newest_time)):
                        newest_time = stamp
    
            print(f"Interval {interval}: {window_count} events, {len(threat_ids)} unique threats so far")
            current_start = current_end
    
        return threat_ids, newest_time
    
    def fetch_threat_summary(headers: dict, threat_id: str):
        """Fetch one threat summary from the Threat API, or None if TAP has no summary for it."""
        url = f'{API_BASE}/v2/threat/summary/{quote(threat_id, safe="")}'
        summary = request_json(url, headers)
        if summary is None:
            print(f"Threat {threat_id}: no summary available (404)")
            return None
        if 'id' not in summary:
            summary['id'] = threat_id
        return summary
    

**Note:** This script is provided as an example and is not officially supported. We welcome feedback about how we can improve it. To submit feedback, click **Send Feedback > Google SecOps Security Product Feedback** on this page.

     * Second file - **requirements.txt:**
    
    functions-framework==3.*
    google-cloud-storage==2.*
    urllib3>=2.0.0
    

  3. Click **Deploy** to save and deploy the function.

  4. Wait for deployment to complete (2-3 minutes).




### How the function collects threats

  * The function reads the TAP SIEM API `/v2/siem/all` endpoint in one-hour intervals from its watermark and collects the `threatID` values referenced by blocked and delivered messages and blocked and permitted clicks. The SIEM events themselves are not written; only the threat IDs are used.
  * For each discovered threat ID it calls `/v2/threat/summary/{threatId}` and writes the summary as one NDJSON record. A summary is written again only when its content changed since it was last written, for example when the threat status moves from `active` to `cleared`.
  * The state file keeps the newest SIEM event time as the watermark, the hash of the last written summary per threat, and the threat IDs still queued when a run reaches `MAX_THREATS`. Every run re-reads `OVERLAP_MINUTES` before the watermark and processes the queue first, so nothing is lost when a run is capped or an event is indexed late.
  * Any API or storage error fails the run and leaves the watermark unchanged, so the next run retries the same window.

**Note:** The SIEM API allows 1,800 requests per rolling 24 hours per endpoint. An hourly schedule with a 10-minute overlap uses about 48 of them a day. The Threat API has no throttle.



## Create a Cloud Scheduler job

Cloud Scheduler will publish messages to the Pub/Sub topic at regular intervals, triggering the Cloud Run function.

  1. In the **GCP Console** , go to **Cloud Scheduler**.
  2. Click **Create Job**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | `tap-threats-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the topic `tap-threats-collector-trigger`  
**Message body** | `{}` (empty JSON object)  
  4. Click **Create**.




### Schedule frequency options

Choose frequency based on log volume and latency requirements:

Frequency | Cron Expression | Use Case  
---|---|---  
Every 15 minutes | `*/15 * * * *` | High-volume environments with many threats  
Every hour | `0 * * * *` | Standard (recommended)  
Every 6 hours | `0 */6 * * *` | Low-volume environments  
**Note:** The TAP SIEM API has a throttle limit of 1,800 requests per 24 hours. An hourly schedule uses 24 requests per day, well within the limit. If you use a 15-minute schedule, make sure your total daily API calls remain within the throttle threshold.

### Test the integration

  1. In the **Cloud Scheduler** console, find your job.
  2. Click **Force run** to trigger the job manually.
  3. Wait a few seconds.
  4. Go to **Cloud Run > Services**.
  5. Click the function name `tap-threats-collector`.
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         Discovering threats in SIEM events from YYYY-MM-DDTHH:MM:SS+00:00 to YYYY-MM-DDTHH:MM:SS+00:00
         Interval .../...: X events, Y unique threats so far
         Discovered Y threat IDs, Y queued for lookup
         Wrote Z threat summaries to gs://proofpoint-tap-threats-logs/tap-threats/threats_YYYYMMDDTHHMMSSZ.ndjson
         Successfully processed Z threat summaries
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click your bucket name.

  10. Navigate to the prefix folder `tap-threats/`.

  11. Verify that a new `.ndjson` file was created with the current timestamp.




If you see errors in the logs:

  * **HTTP 401** : Check TAP_PRINCIPAL and TAP_SECRET in environment variables. Verify the Service Principal and Secret are correct.
  * **HTTP 403** : Confirm that your TAP account has API access enabled.
  * **HTTP 429** : Rate limiting - function will automatically retry with backoff. Consider reducing schedule frequency.
  * **No new or changed threat summaries** : This is normal if no threats were observed in the time window, or if every observed threat was already written with the same content. TAP only reports threats identified by URL Defense or Attachment Defense.
  * **Missing environment variables** : Check all required variables are set.



## Configure a feed in Google SecOps to ingest Proofpoint TAP Threats logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Proofpoint TAP Threats`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Proofpoint Tap Threats** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Don't use service accounts from other documentation or examples.
  9. Click **Next**.

  10. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the Cloud Storage bucket URI with the prefix path:
           
           gs://proofpoint-tap-threats-logs/tap-threats/
           

       * Replace: 
         * `proofpoint-tap-threats-logs`: Your Cloud Storage bucket name.
         * `tap-threats`: Optional prefix orfolder path where logs are stored (leave empty for root).
**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference: 
       * **Never delete files** : Never delete files from the source (recommended for testing).
       * **Delete transferred files and empty directories** : Delete files and empty directories from the source after a successful fetch completes.
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days)
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)
     * **Ingestion labels** : The label to be applied to the events from this feed
  11. Click **Next**.

  12. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




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
`detectionType_label` | `additional.fields` | Merged  
`geoTargeted_label` | `additional.fields` | Merged  
`notable_label` | `additional.fields` | Merged  
`verticallyTargeted_label` | `additional.fields` | Merged  
`identifiedAt` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`has_principal` | `metadata.event_type` | Mapped: `true` → `NETWORK_CONNECTION`, `true` → `STATUS_UPDATE`  
`type` | `metadata.product_event_type` | Directly mapped  
`id` | `metadata.product_log_id` | Directly mapped  
`_associations` | `security_result.associations` | Merged  
`_techniques` | `security_result.attack_details.techniques` | Merged  
`_category` | `security_result.category` | Merged  
`_category_details` | `security_result.category_details` | Merged  
`notable` | `security_result.priority` | Mapped: `true` → `HIGH_PRIORITY`  
`name` | `security_result.threat_name` | Directly mapped  
`status` | `security_result.threat_status` | Mapped: `active` → `ACTIVE`, `cleared` → `CLEARED`  
`_verdict_info` | `security_result.verdict_info` | Merged  
N/A | `metadata.event_type` | Constant: `NETWORK_CONNECTION`  
N/A | `metadata.product_event_type` | Constant: `Proofpoint_Threats_Feed`  
N/A | `metadata.product_name` | Constant: `TAP Threats`  
N/A | `metadata.vendor_name` | Constant: `Proofpoint`  
N/A | `security_result.priority` | Constant: `HIGH_PRIORITY`  
N/A | `security_result.threat_status` | Constant: `ACTIVE`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/proofpoint-tap-threats-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
