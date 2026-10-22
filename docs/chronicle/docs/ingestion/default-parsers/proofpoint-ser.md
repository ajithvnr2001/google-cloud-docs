---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/proofpoint-ser/
title: Collect Proofpoint Secure Email Relay logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:10:46.484652+00:00
---

# Collect Proofpoint Secure Email Relay logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/proofpoint-ser/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Proofpoint Secure Email Relay logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Proofpoint Secure Email Relay logs to Google Security Operations using Cloud Storage V2.

Proofpoint Secure Email Relay (SER) is a managed relay for application generated mail, such as transactional and notification messages. SER reports on that traffic through its Reporting API, one of the SER configuration APIs. The API returns aggregate usage figures: the licensed throughput position, daily volume and message counts, and counters for each relay user. The parser maps those figures to the Unified Data Model (UDM), recording them as labels alongside the relay user identity.

**Note:** SER reporting is aggregated. The API doesn't expose per-message resources, so the ingested events carry counts and volumes, rather than metadata for individual messages, such as subject, recipients, or message ID.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A Google Cloud project with Cloud Storage API enabled
  * Permissions to create and manage Cloud Storage buckets
  * Permissions to manage Identity and Access Management (IAM) policies on Cloud Storage buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * Administrator access to the Proofpoint Secure Email Relay portal, including permission to create API keys



## Create a Cloud Storage bucket

  1. Go to the [Google Cloud console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `proofpoint-ser-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Collect Proofpoint SER API credentials

Access to the Reporting API is granted by an API key issued from the Proofpoint API Key Management service. The key is not created inside the SER console itself, which is why it doesn't appear under any of the SER navigation entries.

### Create an API key

  1. Sign in to the [Proofpoint Secure Email Relay portal](https://ser.proofpoint.com/) with administrator credentials.
  2. Open the **App Switcher** in the top left corner.
  3. Go to **Services > API Key Management**.
  4. Click **Create Key**.
  5. Select **Secure Email Relay** as the product.
  6. Copy and securely store the following values:

     * **Key** : used as the `client_id`
     * **Secret** : used as the `client_secret`
**Note:** The key and secret are displayed on screen one time only. The secret cannot be viewed again afterwards, so copy both values before leaving the page. The key and secret expire one year after activation.



### Verify permissions

The **API Key Management** service is shared across multiple Proofpoint products, which is why you access it through the App Switcher rather than the SER navigation menu. To gain access to the SER configuration APIs, including the Reporting API, you must select **Secure Email Relay** as the product when creating your key.

If **API Key Management** doesn't appear in the App Switcher, your account lacks the API management permission. Contact your Proofpoint administrator or account team so they can grant you the permission.

### Test API access

  * The Reporting API uses the OAuth 2.0 client credentials grant. Exchange the key and secret for a bearer token, then call the API with that token.
        
        # Replace with the values you copied
        CLIENT_ID="<your-key>"
        CLIENT_SECRET="<your-secret>"
        
        # 1. Exchange the key and secret for an access token
        ACCESS_TOKEN=$(curl -s -X POST "https://auth.proofpoint.com/v1/token" \
          -H "Content-Type: application/x-www-form-urlencoded" \
          -d "grant_type=client_credentials" \
          -d "client_id=${CLIENT_ID}" \
          -d "client_secret=${CLIENT_SECRET}" \
          | python3 -c "import json,sys; print(json.load(sys.stdin)['access_token'])")
        
        # 2. Call the Reporting API with the token
        curl -v -H "Authorization: Bearer ${ACCESS_TOKEN}" \
          "https://reporting.ser.proofpoint.com/v1/usage/overview"
        




A successful call returns a JSON object whose `data` member contains `throughputLimit`, `licenseStartDate`, `licenseEndDate`, and the throughput averages.

**Note:** The Reporting API accepts the access token only as an `Authorization: Bearer` header.

## Create a service account for the Cloud Run function

The Cloud Run function needs a service account with permissions to write to a Cloud Storage bucket and be invoked by Pub/Sub.

### Create the service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `proofpoint-ser-collector-sa`
     * **Service account description** : Enter `Service account for Cloud Run function to collect Proofpoint Secure Email Relay logs`
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

  * **Storage Object Admin** : Write logs to a Cloud Storage bucket and manage state files
  * **Cloud Run Invoker** : Allow Pub/Sub to invoke the function
  * **Cloud Functions Invoker** : Allow function invocation



### Grant IAM permissions on the Cloud Storage bucket

Grant the service account write permissions on the Cloud Storage bucket:

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name (for example, `proofpoint-ser-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `proofpoint-ser-collector-sa@PROJECT_ID.iam.gserviceaccount.com`)
     * **Assign roles** : Select **Storage Object Admin**
  6. Click **Save**.



## Create a Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `proofpoint-ser-trigger`
     * Leave other settings as default
  4. Click **Create**.



## Create a Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch usage reports from the SER Reporting API and write them to Cloud Storage.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `proofpoint-ser-collector`  
**Region** | Select region matching your Cloud Storage bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose the Pub/Sub topic (`proofpoint-ser-trigger`).
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Go to and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select the service account (`proofpoint-ser-collector-sa`)
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `proofpoint-ser-logs` | Cloud Storage bucket name  
`GCS_PREFIX` | `ser-logs` | Prefix for log files  
`STATE_KEY` | `ser-logs-state.json` | State path, outside the log prefix  
`TOKEN_URL` | `https://auth.proofpoint.com/v1/token` | OAuth 2.0 token endpoint  
`API_BASE` | `https://reporting.ser.proofpoint.com` | SER Reporting API base URL  
`CLIENT_ID` | `your-key` | The **Key** from API Key Management  
`CLIENT_SECRET` | `your-secret` | The **Secret** from API Key Management  
`PAGE_SIZE` | `50` | Relay users requested per page  
`MAX_PAGES` | `200` | Page ceiling for relay user pagination  
`REPORT_DAY_OFFSET` | `1` | Report on the day this many days back  
`MAX_BACKFILL_DAYS` | `7` | Most days a single run will backfill  
`SEEN_RETENTION_DAYS` | `7` | Days of deduplication keys kept in state  
**Note:** `STATE_KEY` points outside the log prefix on purpose. The feed ingests every object under its bucket URI and, when a deletion option is selected, deletes what it transferred. Keeping the state file out of that prefix stops it from being ingested as log data and from being deleted, which would reset collection and re-ingest duplicate events.
  10. In the **Variables & Secrets** section, go to **Requests** :

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
        import hashlib
        import json
        import os
        import time
        import urllib.parse
        import urllib3
        from datetime import date, datetime, timezone, timedelta
        
        # Initialize HTTP client with timeouts
        http = urllib3.PoolManager(
            timeout=urllib3.Timeout(connect=5.0, read=30.0),
            retries=False,
        )
        
        # Initialize Storage client
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
        
        # Environment variables
        GCS_BUCKET = os.environ.get('GCS_BUCKET')
        GCS_PREFIX = os.environ.get('GCS_PREFIX', 'ser-logs')
        # STATE_KEY must stay OUTSIDE GCS_PREFIX. The feed ingests every object under
        # its bucket URI and, with a deletion option selected, deletes what it
        # transferred. A state file inside the prefix would be ingested as log data and
        # then deleted, resetting collection and re-ingesting duplicates.
        STATE_KEY = os.environ.get('STATE_KEY', 'ser-logs-state.json')
        TOKEN_URL = os.environ.get('TOKEN_URL', 'https://auth.proofpoint.com/v1/token')
        API_BASE = os.environ.get('API_BASE', 'https://reporting.ser.proofpoint.com')
        CLIENT_ID = os.environ.get('CLIENT_ID')
        CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
        PAGE_SIZE = int(os.environ.get('PAGE_SIZE', '50'))
        MAX_PAGES = int(os.environ.get('MAX_PAGES', '200'))
        # The Reporting API filters on whole calendar days, so the collector reports on
        # a day that has already finished rather than on a partial one.
        REPORT_DAY_OFFSET = int(os.environ.get('REPORT_DAY_OFFSET', '1'))
        MAX_BACKFILL_DAYS = int(os.environ.get('MAX_BACKFILL_DAYS', '7'))
        SEEN_RETENTION_DAYS = int(os.environ.get('SEEN_RETENTION_DAYS', '7'))
        
        MAX_RATE_LIMIT_RETRIES = 5
        
        class FetchError(Exception):
            """Raised when a Proofpoint SER API call fails.
        
            Collection must fail loudly. Returning an empty result on an API error is
            indistinguishable from a day with no traffic, and would let the run record
            a day it never actually read.
            """
        
        def get_access_token():
            """Exchange the API key and secret for an OAuth 2.0 bearer token.
        
            The SER configuration APIs use the client credentials grant with the
            credentials in the form body. The returned token is sent to each API
            host as an Authorization: Bearer header.
            """
            body = urllib.parse.urlencode({
                'grant_type': 'client_credentials',
                'client_id': CLIENT_ID,
                'client_secret': CLIENT_SECRET,
            })
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Accept': 'application/json',
            }
        
            try:
                response = http.request('POST', TOKEN_URL, body=body, headers=headers)
            except Exception as e:
                raise FetchError(f'Token request to {TOKEN_URL} failed: {e}') from e
        
            if response.status != 200:
                raise FetchError(f'HTTP {response.status} from {TOKEN_URL}: {response.data.decode("utf-8")}')
        
            try:
                token = json.loads(response.data.decode('utf-8')).get('access_token')
            except json.JSONDecodeError as e:
                raise FetchError(f'Malformed token response from {TOKEN_URL}: {e}') from e
        
            if not token:
                raise FetchError('Token response did not contain an access_token')
        
            return token
        
        def call_api(token, method, path, body=None):
            """Call one Reporting API endpoint and return the decoded JSON body.
        
            Every failure raises. A caller that mistook an error for an empty report
            would record the day as collected and never come back to it.
            """
            url = f'{API_BASE}{path}'
            headers = {
                'Authorization': f'Bearer {token}',
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'User-Agent': 'GoogleSecOps-ProofpointSERCollector/1.0',
            }
            payload = json.dumps(body) if body is not None else None
            backoff = 1.0
            retries = 0
        
            while True:
                try:
                    response = http.request(method, url, body=payload, headers=headers)
                except Exception as e:
                    raise FetchError(f'Request to {url} failed: {e}') from e
        
                if response.status == 429:
                    retries += 1
                    if retries > MAX_RATE_LIMIT_RETRIES:
                        raise FetchError(f'Rate limited repeatedly by {url}; giving up without recording the day')
                    raw_retry_after = response.headers.get('Retry-After')
                    try:
                        # Retry-After may also be an HTTP date, which int() cannot parse.
                        delay = int(raw_retry_after) if raw_retry_after else int(backoff)
                    except (TypeError, ValueError):
                        delay = int(backoff)
                    print(f'Rate limited (429) on {path}. Retrying after {delay}s...')
                    time.sleep(delay)
                    backoff = min(backoff * 2, 30.0)
                    continue
        
                if response.status != 200:
                    raise FetchError(f'HTTP {response.status} from {url}: {response.data.decode("utf-8")}')
        
                try:
                    return json.loads(response.data.decode('utf-8'))
                except json.JSONDecodeError as e:
                    raise FetchError(f'Malformed JSON response from {url}: {e}') from e
        
        def as_list(value):
            """Return a response data member as a list.
        
            The Reporting API returns data as an object on some endpoints and as an
            array on others, and the published schema declares neither.
            """
            if value is None:
                return []
            if isinstance(value, list):
                return value
            return [value]
        
        def collect_day(token, day, include_overview):
            """Collect one reporting day and return the records to write.
        
            The nesting of each record is chosen to match what the parser expects.
            Rows carrying acceptedMessages are emitted bare, because the parser nests
            those under data itself. The other two responses are emitted whole, so
            that their data and metadata envelope survives to the parser.
            """
            records = []
        
            # Licensed throughput position. This endpoint takes no date and reports
            # the tenant's standing right now, so it is collected once per run rather
            # than once per day: a backfill would otherwise write the same snapshot
            # against every day it catches up on.
            if include_overview:
                records.append(call_api(token, 'GET', '/v1/usage/overview'))
        
            # Volume in bytes for the day. One envelope per row, so that the
            # totalThroughput in metadata stays attached to the row it describes.
            data_trend = call_api(token, 'POST', '/v1/usage/data-trend', {
                'dates': day,
                'interval': 'day',
            })
            for element in as_list(data_trend.get('data')):
                records.append({'data': [element], 'metadata': data_trend.get('metadata', {})})
        
            # Message counters for the day.
            message_trend = call_api(token, 'POST', '/v1/usage/message-trend', {
                'dates': day,
                'interval': 'day',
            })
            records.extend(as_list(message_trend.get('data')))
        
            # Per relay user counters, paginated.
            page = 1
            while True:
                if page > MAX_PAGES:
                    raise FetchError(f'Relay user pagination for {day} exceeded MAX_PAGES ({MAX_PAGES})')
        
                payload = call_api(token, 'POST', '/v1/usage/relay-users', {
                    'dates': day,
                    'pageNum': page,
                    'pageSize': PAGE_SIZE,
                })
                elements = as_list(payload.get('data'))
                if not elements:
                    break
        
                records.extend(elements)
        
                pagination = (payload.get('metadata') or {}).get('pagination') or {}
                total_pages = pagination.get('totalPages')
                if not total_pages or page >= total_pages:
                    break
                page += 1
        
            return records
        
        def record_key(record):
            """Return the deduplication identity of one record.
        
            Reporting rows are aggregates and carry no identifier of their own, so
            identity is the content hash. Keys are held per reporting day, which makes
            a repeated run of the same day a no-op without ever suppressing a new day
            whose figures happen to be identical.
            """
            return 'sha256:' + hashlib.sha256(
                json.dumps(record, sort_keys=True, ensure_ascii=False).encode('utf-8')
            ).hexdigest()
        
        def pending_days(last_report_date, target):
            """Return the reporting days still to collect, oldest first."""
            if not last_report_date:
                start = target
            else:
                start = date.fromisoformat(last_report_date) + timedelta(days=1)
        
            if start > target:
                return []
        
            if (target - start).days >= MAX_BACKFILL_DAYS:
                start = target - timedelta(days=MAX_BACKFILL_DAYS - 1)
                print(f'Backfill capped at {MAX_BACKFILL_DAYS} days. Days before {start.isoformat()} are not collected.')
        
            return [start + timedelta(days=offset) for offset in range((target - start).days + 1)]
        
        def prune_seen(seen, target):
            """Drop deduplication keys for days outside the retention window."""
            cutoff = target - timedelta(days=SEEN_RETENTION_DAYS)
            return {day: keys for day, keys in seen.items() if date.fromisoformat(day) >= cutoff}
        
        @functions_framework.cloud_event
        def main(cloud_event):
            """Fetch Proofpoint SER usage reports and write them to Cloud Storage.
        
            Args:
                cloud_event: CloudEvent object containing the Pub/Sub message.
            """
            if not all([GCS_BUCKET, CLIENT_ID, CLIENT_SECRET]):
                # Raise rather than return: a bare return acks the Pub/Sub message and
                # reports the run as successful, silently discarding the schedule tick.
                raise RuntimeError('Missing required environment variables')
        
            bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(GCS_BUCKET)
            state = load_state(bucket, STATE_KEY)
            seen = [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get('seen') or {}
        
            now = datetime.now(timezone.utc)
            target = (now - timedelta(days=REPORT_DAY_OFFSET)).date()
        
            days = pending_days([state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get('last_report_date'), target)
            if not days:
                print(f'Nothing to collect. {target.isoformat()} is already recorded.')
                return
        
            token = get_access_token()
        
            for day in days:
                key = day.isoformat()
                print(f'Collecting reporting day {key}')
        
                # A FetchError here propagates: the run fails, the state is left at the
                # last day that was fully written, and the next run retries this day.
                records = collect_day(token, key, include_overview=(day == days[-1]))
        
                day_seen = set(seen.get(key, []))
                fresh = []
                for record in records:
                    digest = record_key(record)
                    if digest in day_seen:
                        continue
                    day_seen.add(digest)
                    fresh.append(record)
        
                print(f'{key}: fetched {len(records)} records, {len(fresh)} new after deduplication')
        
                if fresh:
                    timestamp = now.strftime('%Y%m%dT%H%M%SZ')
                    object_key = f'{GCS_PREFIX}/usage_{key}_{timestamp}.ndjson'
                    blob = bucket.blob(object_key)
        
                    ndjson = '\n'.join(json.dumps(record, ensure_ascii=False) for record in fresh) + '\n'
                    blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(ndjson, content_type='application/x-ndjson')
        
                    print(f'Wrote {len(fresh)} records to gs://{GCS_BUCKET}/{object_key}')
        
                # Record the day only after its data is durably written.
                seen[key] = sorted(day_seen)
                state['last_report_date'] = key
                state['seen'] = prune_seen(seen, target)
                save_state(bucket, STATE_KEY, state)
        
            print(f'Successfully processed {len(days)} reporting day(s)')
        
        def load_state(bucket, key):
            """Read the collector state from Cloud Storage.
        
            Only a missing object is treated as a cold start. Any other error is
            raised: swallowing it would silently restart collection and re-ingest the
            whole backfill window.
            """
            blob = bucket.blob(key)
            try:
                return json.loads(blob.[download_as_text](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_download_as_text)())
            except NotFound:
                print('No state file found. Starting from the most recent completed day.')
                return {}
        
        def save_state(bucket, key, state):
            """Write the collector state to Cloud Storage.
        
            Failures are raised, not logged. If the state write fails after the data
            was uploaded, the next run repeats the same day and duplicates it.
            """
            blob = bucket.blob(key)
            blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
                json.dumps(state, indent=2),
                content_type='application/json',
            )
            print(f'Saved state: last_report_date={[state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get("last_report_date")}')
        

**Note:** This script is provided as an example and is not officially supported. We welcome feedback about how we can improve it. To submit feedback, click **Send Feedback > Google SecOps Security Product Feedback** on this page.

  * Second file - **requirements.txt:**
        
        functions-framework==3.*
        google-cloud-storage==2.*
        urllib3>=2.0.0
        



  1. Click **Deploy** to save and deploy the function.
  2. Wait for deployment to complete (2-3 minutes).

**Note:** The Pub/Sub trigger configuration automatically creates the necessary subscriptions and permissions.



## Create a Cloud Scheduler job

Cloud Scheduler will publish messages to the Pub/Sub topic at regular intervals, triggering the Cloud Run function.

  1. In the **GCP Console** , go to **Cloud Scheduler**.
  2. Click **Create Job**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | `proofpoint-ser-collector-daily`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 2 * * *` (daily, at 02:00)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the Pub/Sub topic (`proofpoint-ser-trigger`)  
**Message body** | `{}` (empty JSON object)  
  4. Click **Create**.




### Schedule frequency options

The Reporting API aggregates by calendar day, so a completed day is collected once. Run the job daily, after the reporting day has closed in your tenant's timezone:

Frequency | Cron Expression | Use Case  
---|---|---  
Daily at 02:00 | `0 2 * * *` | Standard (recommended)  
Daily at 06:00 | `0 6 * * *` | Tenants whose reporting settles later  
Twice daily | `0 2,14 * * *` | Adds a same day retry if the first run failed  
  
A run that finds its day already recorded exits without writing anything, so an extra run costs one API call and never duplicates data.

### Test the integration

  1. In the **Cloud Scheduler** console, find your job.
  2. Click **Force run** to trigger the job manually.
  3. Wait a few seconds.
  4. Go to **Cloud Run > Services**.
  5. Click your function name (`proofpoint-ser-collector`).
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         Collecting reporting day YYYY-MM-DD
         YYYY-MM-DD: fetched X records, X new after deduplication
         Wrote X records to gs://proofpoint-ser-logs/ser-logs/usage_YYYY-MM-DD_YYYYMMDDTHHMMSSZ.ndjson
         Saved state: last_report_date=YYYY-MM-DD
         Successfully processed 1 reporting day(s)
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click your bucket name (`proofpoint-ser-logs`).

  10. Navigate to the prefix folder (`ser-logs/`).

  11. Verify that a new `.ndjson` file was created with the current timestamp.




If you see errors in the logs:

  * **HTTP 400 from the token endpoint** : The key or secret is wrong, or the key has expired. `invalid_client` means the pair was rejected; create a replacement key.
  * **HTTP 401 from the Reporting API** : The bearer token was not sent or is no longer valid.
  * **HTTP 429** : Rate limiting. The function retries with backoff and fails the run if the limit persists, leaving the day to the next run.
  * **Missing environment variables** : Check all required variables are set.



## Retrieve the Google SecOps service account

Google SecOps uses a unique service account to read data from your Cloud Storage bucket. You must grant this service account access to your bucket.

### Get the service account email

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Proofpoint SER Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **ProofPoint Secure Email Relay** as the **Log type**.
  7. Click **Get Service Account**.
  8. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  9. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Don't use service accounts from other documentation or examples.
  10. Click **Next**.

  11. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the Cloud Storage bucket URI with the prefix path:
           
           gs://proofpoint-ser-logs/ser-logs/
           

       * Replace: 
         * `proofpoint-ser-logs`: Your Cloud Storage bucket name.
         * `ser-logs`: Optional prefix or folder path where logs are stored (leave empty for root).
**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never delete files** : Never delete files from the source (recommended for testing).
       * **Delete transferred files and empty directories** : Delete files and empty directories from the source after a successful fetch completes.
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days)

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)

     * **Ingestion labels** : The label to be applied to the events from this feed

  12. Click **Next**.

  13. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## Grant IAM permissions to the Google SecOps service account

The Google SecOps service account needs two roles on your Cloud Storage bucket: **Storage Object Viewer** to read the log objects, and a bucket-level role to read the bucket metadata.

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name (for example, `proofpoint-ser-logs`).
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
`acceptedMessages_label` | `additional.fields` | Merged  
`acceptedThroughput_label` | `additional.fields` | Merged  
`average30DayThroughput_label` | `additional.fields` | Merged  
`average7DayThroughput_label` | `additional.fields` | Merged  
`averageDailyThroughput_label` | `additional.fields` | Merged  
`avgAcceptedMessageSize_label` | `additional.fields` | Merged  
`blockedMessages_label` | `additional.fields` | Merged  
`data_totalThroughput_label` | `additional.fields` | Merged  
`deliveredMessages_label` | `additional.fields` | Merged  
`licenseEndDate_label` | `additional.fields` | Merged  
`licenseStartDate_label` | `additional.fields` | Merged  
`map_label` | `additional.fields` | Merged  
`metadata_totalThroughput_label` | `additional.fields` | Merged  
`quarantinedMessages_label` | `additional.fields` | Merged  
`rejectedMessages_label` | `additional.fields` | Merged  
`remainingThroughput_label` | `additional.fields` | Merged  
`requestedMessages_label` | `additional.fields` | Merged  
`requestedThroughput_label` | `additional.fields` | Merged  
`sentMessages_label` | `additional.fields` | Merged  
`throughputForecast_label` | `additional.fields` | Merged  
`throughputLimit_label` | `additional.fields` | Merged  
`throughput_label` | `additional.fields` | Merged  
`totalMessages_label` | `additional.fields` | Merged  
`undeliveredMessages_label` | `additional.fields` | Merged  
`data.name` | `metadata.description` | Directly mapped  
`desc` | `metadata.description` | Directly mapped  
`data.date` | `metadata.event_timestamp` | Parsed as `yyyy-MM-dd`  
`event_type` | `metadata.event_type` | Directly mapped  
`fromEnvelope` | `network.email.bounce_address` | Directly mapped  
`fromHeader` | `network.email.from` | Directly mapped  
`applicationName` | `principal.administrative_domain` | Directly mapped  
`principal_host` | `principal.asset.hostname` | Directly mapped  
`principal_host` | `principal.hostname` | Directly mapped  
`principal_port` | `principal.port` | Directly mapped  
`data.relayUserId` | `principal.user.product_object_id` | Directly mapped  
`userId` | `principal.user.product_object_id` | Directly mapped  
`applicationUserName` | `principal.user.user_display_name` | Directly mapped  
`senderName` | `target.administrative_domain` | Directly mapped  
`senderId` | `target.user.product_object_id` | Directly mapped  
N/A | `metadata.product_name` | Constant: `PROOFPOINT SER`  
N/A | `metadata.vendor_name` | Constant: `PROOFPOINT`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/proofpoint-ser-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
