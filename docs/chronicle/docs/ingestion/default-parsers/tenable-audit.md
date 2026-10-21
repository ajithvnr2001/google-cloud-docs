---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tenable-audit/
title: Collect Tenable Audit logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:18:07.300816+00:00
---

# Collect Tenable Audit logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tenable-audit/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Tenable Audit logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Tenable Audit logs to Google Security Operations using Cloud Storage V2.

Tenable Vulnerability Management (formerly Tenable.io) is a cloud-based vulnerability management platform (cloud.tenable.com) whose activity log records user authentication, API access, configuration changes, and administrative actions. The Tenable Vulnerability Management REST API provides programmatic access to these activity log events.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A Google Cloud project with Cloud Storage API enabled
  * Permissions to create and manage Cloud Storage buckets
  * Permissions to manage Identity and Access Management (IAM) policies on Cloud Storage buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * Privileged access to Tenable Vulnerability Management (cloud.tenable.com) with the **Administrator** role
  * Tenable Vulnerability Management API keys (access key and secret key) generated on a user account with the **Administrator** role



## Create a Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `tenable-audit-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Collect Tenable Vulnerability Management API credentials

### Generate API keys

  1. Sign in to [Tenable Vulnerability Management](https://cloud.tenable.com/).
  2. In the upper-right corner of any page, click the blue user circle, and then click **My Profile**. The **My Account** page appears.
  3. Go to the **API Keys** tab.
  4. Click **Generate**. The **Generate API Keys** window appears with a warning.

"Caution: Generating keys replaces any existing API keys on this user account, including keys already used by other integrations. Use a dedicated user account for this integration, or update every application that used the previous keys."

  5. Review the warning and click **Generate**.

**Tip:** If the **Generate** button is inactive, ask your administrator to enable API access for the account.
  6. Copy and save the following details in a secure location:

     * **Access Key** : The API access key
     * **Secret Key** : The API secret key
**Note:** Copy both keys before you leave the **API Keys** tab. After you close the tab, neither key can be retrieved and you must generate a replacement pair. Store both keys securely as environment variables.



### Verify API access

  * Test your credentials before proceeding with the integration:
        
        # Replace with your actual credentials
        ACCESS_KEY="your-access-key"
        SECRET_KEY="your-secret-key"
        
        curl -s -H "X-ApiKeys: accessKey=${ACCESS_KEY};secretKey=${SECRET_KEY}" \
            "https://cloud.tenable.com/audit-log/v1/events?limit=1" | head -c 500
        




### Verify permissions

To verify the account has the required permissions:

  1. Sign in to [Tenable Vulnerability Management](https://cloud.tenable.com/).
  2. In the left navigation, click **Settings**.
  3. Click the **Access Control** tile.
  4. Click the **Users** tab, and then click the user account used for this integration.
  5. Verify that the account has the **Administrator** role. The activity log endpoint requires the Administrator user role: no custom role grants access to the activity log, and any other role receives an HTTP 403 response.

**Note:** Opening the **Access Control** page itself requires the Administrator role. If you cannot open it, ask your Tenable administrator to confirm the account's role.
  6. If you do not have the required permissions, contact your Tenable Vulnerability Management administrator.




## Create a service account for the Cloud Run function

The Cloud Run function needs a service account with permissions to write to the Cloud Storage bucket and be invoked by Pub/Sub.

### Create the service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `tenable-audit-collector-sa`
     * **Service account description** : Enter `Service account for Cloud Run function to collect Tenable Audit logs`
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
  2. Click your bucket name (for example, `tenable-audit-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `tenable-audit-collector-sa@PROJECT_ID.iam.gserviceaccount.com`)
     * **Assign roles** : Select **Storage Object Admin**
  6. Click **Save**.



## Create a Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `tenable-audit-trigger`
     * Leave other settings as default
  4. Click **Create**.



## Create a Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from the Tenable Vulnerability Management REST API and write them to Cloud Storage.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `tenable-audit-collector`  
**Region** | Select region matching your Cloud Storage bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose the topic `tenable-audit-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select the service account `tenable-audit-collector-sa`.
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `tenable-audit-logs` | Cloud Storage bucket name  
`GCS_PREFIX` | `tenable` | Prefix for log files  
`STATE_KEY` | `tenable-state.json` | State path, outside the log prefix  
`TENABLE_ACCESS_KEY` | `your-access-key` | Tenable Vulnerability Management access key  
`TENABLE_SECRET_KEY` | `your-secret-key` | Tenable Vulnerability Management secret key  
`MAX_RECORDS` | `5000` | Max records per run  
`PAGE_SIZE` | `1000` | Records per page  
`LOOKBACK_HOURS` | `24` | Initial lookback period  
`OVERLAP_MINUTES` | `2` | Minutes re-read before the watermark to catch late-indexed events  
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

     * First file - **main.py** :
    
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
    GCS_PREFIX = os.environ.get('GCS_PREFIX', 'tenable')
    # STATE_KEY must stay OUTSIDE GCS_PREFIX. The feed ingests every object under
    # its bucket URI and, with a deletion option selected, deletes what it
    # transferred. A state file inside the prefix would be ingested as log data and
    # then deleted, resetting collection and re-ingesting duplicates.
    STATE_KEY = os.environ.get('STATE_KEY', 'tenable-state.json')
    TENABLE_ACCESS_KEY = os.environ.get('TENABLE_ACCESS_KEY')
    TENABLE_SECRET_KEY = os.environ.get('TENABLE_SECRET_KEY')
    MAX_RECORDS = int(os.environ.get('MAX_RECORDS', '5000'))
    # The audit-log API accepts a limit up to 10000.
    PAGE_SIZE = int(os.environ.get('PAGE_SIZE', '1000'))
    LOOKBACK_HOURS = int(os.environ.get('LOOKBACK_HOURS', '24'))
    # The query re-reads this many minutes before the watermark so that events
    # Tenable indexes late are still collected. Re-read events are dropped by id.
    OVERLAP_MINUTES = int(os.environ.get('OVERLAP_MINUTES', '2'))
    
    TENABLE_API_BASE = 'https://cloud.tenable.com'
    
    class FetchError(Exception):
      """Raised when the Tenable API call fails.
    
      The watermark must never advance on a failed fetch, otherwise every event in
      the failed window is skipped permanently.
      """
    
    def parse_datetime(value: str) -> datetime:
      """Parse a Tenable `received` timestamp into an aware datetime.
    
      Tenable returns ISO 8601 with either whole seconds (2018-12-31T23:09:40Z) or
      fractional seconds (2024-01-16T15:12:47.334Z). Fractional digits are trimmed
      to microseconds because fromisoformat accepts at most six.
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
      """Fetch Tenable Vulnerability Management activity log events and write them to Cloud Storage.
    
      Args:
        cloud_event: CloudEvent object containing the Pub/Sub message.
      """
      if not all([GCS_BUCKET, TENABLE_ACCESS_KEY, TENABLE_SECRET_KEY]):
        # Raise rather than return: a bare return acks the Pub/Sub message and
        # reports the run as successful, silently discarding the schedule tick.
        raise RuntimeError('Missing required environment variables')
    
      bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(GCS_BUCKET)
      state = load_state(bucket, STATE_KEY)
    
      now = datetime.now(timezone.utc)
      watermark = None
      if [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get('last_event_time'):
        watermark = parse_datetime(state['last_event_time'])
      seen_ids = set([state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get('seen_ids', []))
    
      if watermark is None:
        start_time = now - timedelta(hours=LOOKBACK_HOURS)
      else:
        start_time = watermark - timedelta(minutes=OVERLAP_MINUTES)
    
      print(f"Fetching logs from {start_time.isoformat()} to {now.isoformat()}")
    
      # A FetchError propagates: the run fails, the watermark is untouched, and the
      # next invocation retries the same window.
      records, newest_event_time = fetch_logs(
        start_time=start_time,
        page_size=PAGE_SIZE,
        max_records=MAX_RECORDS,
      )
    
      # Drop events already written by an earlier run. Without this the overlap
      # window re-emits its events on every invocation, and an idle tenant has its
      # newest events rewritten to a new object every hour.
      fresh = [r for r in records if str(r.get('id', '')) not in seen_ids]
      print(f"Fetched {len(records)} records, {len(fresh)} new after deduplication")
    
      if not fresh:
        print("No new log records found. Watermark left unchanged.")
        return
    
      if not newest_event_time:
        raise FetchError('Records were returned but no `received` timestamp could be parsed')
    
      timestamp = now.strftime('%Y%m%dT%H%M%SZ')
      object_key = f"{GCS_PREFIX}/logs_{timestamp}.ndjson"
      blob = bucket.blob(object_key)
    
      ndjson = '\n'.join(json.dumps(record, ensure_ascii=False) for record in fresh) + '\n'
      blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(ndjson, content_type='application/x-ndjson')
    
      print(f"Wrote {len(fresh)} records to gs://{GCS_BUCKET}/{object_key}")
    
      # Advance the watermark only after the data is durably written.
      new_watermark = parse_datetime(newest_event_time)
      if watermark and new_watermark < watermark:
        new_watermark = watermark
    
      # Retain only the ids still inside the overlap window, so the state file
      # stays small while covering every event the next query can re-read.
      cutoff = new_watermark - timedelta(minutes=OVERLAP_MINUTES)
      retained = []
      for record in records:
        received = record.get('received')
        if not received:
          continue
        try:
          if parse_datetime(received) >= cutoff:
            retained.append(str(record.get('id', '')))
        except ValueError:
          continue
    
      save_state(bucket, STATE_KEY, {
        'last_event_time': new_watermark.isoformat(),
        'seen_ids': sorted(i for i in set(retained) if i),
      })
    
      print(f"Successfully processed {len(fresh)} records")
    
    def load_state(bucket, key):
      """Read the collector state from Cloud Storage.
    
      Only a missing object is treated as a cold start. Any other error is raised:
      swallowing it would silently reset collection to the full lookback window and
      re-ingest that entire period.
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
    
    def fetch_logs(start_time: datetime, page_size: int, max_records: int):
      """Fetch audit events from the Tenable Vulnerability Management API.
    
      Uses offset pagination, which is what the endpoint documents: the request
      accepts `limit` (maximum 10000) and `offset`, and the response `pagination`
      object returns `offset`, `limit`, `count` and `total`.
    
      Args:
        start_time: Exclusive lower bound for the `received` timestamp
        page_size: Records per page (the API accepts up to 10000)
        max_records: Maximum total records to fetch in one run
    
      Returns:
        Tuple of (records list, newest `received` value as an ISO 8601 string).
    
      Raises:
        FetchError: on any API or transport failure, so the caller cannot mistake
          a failed fetch for an empty result and advance the watermark.
      """
      endpoint = f"{TENABLE_API_BASE}/audit-log/v1/events"
    
      headers = {
        'X-ApiKeys': f'accessKey={TENABLE_ACCESS_KEY};secretKey={TENABLE_SECRET_KEY}',
        'Accept': 'application/json',
        'User-Agent': 'GoogleSecOps-TenableAuditCollector/1.0'
      }
    
      records = []
      newest_time = None
      page_num = 0
      backoff = 1.0
      rate_limit_retries = 0
      MAX_RATE_LIMIT_RETRIES = 5
      offset = 0
    
      while True:
        page_num += 1
    
        if len(records) >= max_records:
          # Stop cleanly. The remaining events stay ahead of the watermark and
          # are collected by the next run.
          print(f"Reached max_records limit ({max_records})")
          break
    
        # Every parameter is rebuilt per page. `sort=received:asc` is required:
        # a time watermark is only correct over an ascending scan, otherwise a
        # truncated run advances the watermark past events it never read.
        params = {
          'f': f'date.gt:{start_time.strftime("%Y-%m-%dT%H:%M:%SZ")}',
          'sort': 'received:asc',
          'limit': min(page_size, max_records - len(records)),
          'offset': offset,
        }
        url = f"{endpoint}?" + '&'.join(f"{k}={v}" for k, v in params.items())
    
        try:
          response = http.request('GET', url, headers=headers)
        except Exception as e:
          raise FetchError(f'Request to {endpoint} failed: {e}') from e
    
        if response.status == 429:
          rate_limit_retries += 1
          if rate_limit_retries > MAX_RATE_LIMIT_RETRIES:
            raise FetchError('Rate limited repeatedly; giving up without advancing the watermark')
          raw_retry_after = response.headers.get('Retry-After')
          try:
            # Retry-After may also be an HTTP date, which int() cannot parse.
            retry_after = int(raw_retry_after) if raw_retry_after else int(backoff)
          except (TypeError, ValueError):
            retry_after = int(backoff)
          print(f"Rate limited (429). Retrying after {retry_after}s...")
          time.sleep(retry_after)
          backoff = min(backoff * 2, 30.0)
          continue
    
        backoff = 1.0
        rate_limit_retries = 0
    
        if response.status != 200:
          body = response.data.decode('utf-8')
          raise FetchError(f'HTTP {response.status} from the Tenable audit log API: {body}')
    
        try:
          data = json.loads(response.data.decode('utf-8'))
        except json.JSONDecodeError as e:
          raise FetchError(f'Malformed JSON response from the Tenable audit log API: {e}') from e
    
        page_results = data.get('events', [])
    
        if not page_results:
          print("No more results (empty page)")
          break
    
        print(f"Page {page_num}: Retrieved {len(page_results)} events")
        records.extend(page_results)
    
        for event in page_results:
          received = event.get('received')
          if not received:
            continue
          try:
            if newest_time is None or parse_datetime(received) > parse_datetime(newest_time):
              newest_time = received
          except ValueError as e:
            print(f"Warning: Could not parse event time {received!r}: {e}")
    
        offset += len(page_results)
        total = data.get('pagination', {}).get('total')
        if total is not None and offset >= total:
          print("No more pages (all matching events retrieved)")
          break
    
      print(f"Retrieved {len(records)} total records from {page_num} pages")
      return records, newest_time
    

**Note:** This script is provided as an example and is not officially supported. We welcome feedback about how we can improve it. To submit feedback, click **Send Feedback > Google SecOps Security Product Feedback** on this page.

     * Second file - **requirements.txt** :
    
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
**Name** | `tenable-audit-collector-hourly`  
**Region** | Select same region as the Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the topic `tenable-audit-trigger`  
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

  1. In the **Cloud Scheduler** console, find your job.
  2. Click **Force run** to trigger the job manually.
  3. Wait a few seconds.
  4. Go to **Cloud Run > Services**.
  5. Click on `tenable-audit-collector`.
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         Fetching logs from YYYY-MM-DDTHH:MM:SS+00:00 to YYYY-MM-DDTHH:MM:SS+00:00
         Page 1: Retrieved X events
         Fetched X records, Y new after deduplication
         Wrote Y records to gs://tenable-audit-logs/tenable/logs_YYYYMMDDTHHMMSSZ.ndjson
         Saved state: last_event_time=YYYY-MM-DDTHH:MM:SS+00:00
         Successfully processed Y records
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click your bucket name (`tenable-audit-logs`).

  10. Navigate to the `tenable/` folder.

  11. Verify that a new `.ndjson` file was created with the current timestamp.




On a run where nothing new arrived, the function logs `No new log records found. Watermark left unchanged.` and writes no object. This is expected: re-writing the same events would duplicate them in Google SecOps.

If you see errors in the logs:

  * **HTTP 401** : Check API keys in environment variables
  * **HTTP 403** : The account is not an Administrator. The activity log endpoint requires the Administrator [64] user role.
  * **HTTP 429** : Rate limiting. The function retries with backoff and then fails the run without advancing its watermark, so no events are skipped.
  * **Missing environment variables** : Check all required variables are set



## Configure a feed in Google SecOps to ingest Tenable Audit logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Tenable Audit Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Tenable Audit** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address.

**Note:** Each Google SecOps instance has a unique service account. Do not use service accounts from other documentation or examples.
  9. Click **Next**.

  10. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the Cloud Storage bucket URI with the prefix path:
           
           gs://tenable-audit-logs/tenable/
           

       * **Replace:**
         * `tenable-audit-logs`: Your Cloud Storage bucket name.
         * `tenable`: Optional prefix/folder path where logs are stored (leave empty for root).
**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never delete files** : Never delete files from the source (recommended for testing).
       * **Delete transferred files and empty directories** : Delete files and empty directories from the source after a successful fetch completes.

**Note:** Grant both roles. **Storage Object Viewer** does not grant the bucket-level permission the feed needs, and the **Storage Legacy Bucket** roles do not grant permission to read object contents.
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
`crud_label` | `additional.fields` | Merged  
`fields_label` | `additional.fields` | Merged  
`field_name` | `extensions.auth.mechanism` | Mapped: `X-Access-Type` → `mech_label`  
`mech_label` | `extensions.auth.mechanism` | Merged  
`extension_value` | `extensions.auth.type` | Directly mapped  
`description` | `metadata.description` | Directly mapped  
`received` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`has_principal` | `metadata.event_type` | Mapped values (5 total, e.g. `true` → `USER_LOGIN`, `true` → `USER_CREATION`, `true` → `USER...  
`has_user` | `metadata.event_type` | Mapped: `true` → `USER_UNCATEGORIZED`  
`action` | `metadata.product_event_type` | Directly mapped  
`id` | `metadata.product_log_id` | Directly mapped  
`field_name` | `principal.asset.ip` | Mapped: `X-Forwarded-For` → `ip`  
`ip` | `principal.asset.ip` | Merged  
`field_name` | `principal.ip` | Mapped: `X-Forwarded-For` → `ip`  
`ip` | `principal.ip` | Merged  
`actor.name` | `principal.user.email_addresses` | Merged  
`actor.id` | `principal.user.userid` | Directly mapped  
`AUTH_VIOLOATION` | `security_result.category` | Merged  
`is_failure` | `security_result.category` | Mapped: `true` → `AUTH_VIOLOATION`  
`is_anonymous_label` | `security_result.detection_fields` | Merged  
`is_failure_label` | `security_result.detection_fields` | Merged  
`target1.name` | `target.user.email_addresses` | Merged  
`target1.type` | `target.user.role_name` | Directly mapped  
`target1.id` | `target.user.userid` | Directly mapped  
N/A | `extensions.auth.type` | Constant: `AUTHTYPE_UNSPECIFIED`  
N/A | `metadata.event_type` | Constant: `USER_LOGIN`  
N/A | `metadata.product_name` | Constant: `TENABLE AUDIT`  
N/A | `metadata.vendor_name` | Constant: `TENABLE`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/tenable-audit-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
