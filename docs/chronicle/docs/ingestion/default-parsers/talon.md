---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/talon/
title: Collect Talon logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:54:19.176642+00:00
---

# Collect Talon logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/talon/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Talon logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Talon logs to Google Security Operations using Google Cloud Storage V2.

Talon (now part of Palo Alto Networks) is an enterprise browser security platform that provides secure browsing, data loss prevention (DLP), and access control for managed and unmanaged devices. After its acquisition, Talon has been integrated into the Prisma Access platform as Prisma Access Browser, with logs forwarded through Strata Logging Service. The Strata Logging Service API provides programmatic access to security event logs.

## Before you begin

Make sure that you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * Privileged access to Strata Cloud Manager with administrator permissions
  * OAuth2 client credentials (client ID, client secret, and TSG ID) from the Palo Alto Networks Hub



## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `talon-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Collect Talon API credentials

### Create OAuth2 client credentials

  1. Sign in to the [Palo Alto Networks Hub](https://hub.paloaltonetworks.com/).
  2. Go to **Settings > Service Accounts**.
  3. Click **Add Service Account**.
  4. Provide the following configuration details: 
     * **Name** : Enter a descriptive name (for example, `Google SecOps Talon Integration`).
     * **Role** : Select a role with logging read access.
  5. Click **Add**.
  6. Copy and save the following details in a secure location: 
     * **Client ID** : The OAuth2 client ID
     * **Client Secret** : The OAuth2 client secret
  7. Note the **Tenant Service Group (TSG) ID** from the Hub URL or Settings page.

**Note:** The service account must have permissions to access the Strata Logging Service API. Contact your Palo Alto Networks administrator if you need to enable API access.



### Determine API base URL

The Strata Logging Service API base URL:

Region | API Base URL  
---|---  
Global | `https://api.strata.paloaltonetworks.com`  
  
### Test API access

  * Test your credentials before proceeding with the integration:
        
        # Replace with your actual credentials
        CLIENT_ID="your-client-id"
        CLIENT_SECRET="your-client-secret"
        TSG_ID="your-tsg-id"
        
        # Get access token
        curl -s -X POST "https://auth.apps.paloaltonetworks.com/oauth2/access_token" \
          -H "Content-Type: application/x-www-form-urlencoded" \
          -d "grant_type=client_credentials&scope=tsg_id:${TSG_ID}" \
          -u "${CLIENT_ID}:${CLIENT_SECRET}"
        




## Create service account for Cloud Run function

The Cloud Run function needs a service account with permissions to write to GCS bucket and be invoked by Pub/Sub.

### Create service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `talon-logs-collector-sa`
     * **Service account description** : Enter `Service account for Cloud Run function to collect Talon logs`
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
  2. Click on your bucket name (for example, `talon-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `talon-logs-collector-sa@PROJECT_ID.iam.gserviceaccount.com`)
     * **Assign roles** : Select **Storage Object Admin**
  6. Click **Save**.



## Create Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `talon-logs-trigger`
     * Leave other settings as default
  4. Click **Create**.



## Create Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from the Strata Logging Service API and write them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `talon-logs-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose the topic `talon-logs-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select the service account `talon-logs-collector-sa`.
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `talon-logs` | GCS bucket name  
`GCS_PREFIX` | `talon` | Prefix for log files  
`STATE_KEY` | `talon/state.json` | State file path  
`CLIENT_ID` | `your-client-id` | OAuth2 client ID  
`CLIENT_SECRET` | `your-client-secret` | OAuth2 client secret  
`TSG_ID` | `your-tsg-id` | Tenant Service Group ID  
`API_BASE_URL` | `https://api.strata.paloaltonetworks.com` | Strata Logging Service API base URL  
`MAX_RECORDS` | `5000` | Max records per run  
`PAGE_SIZE` | `1000` | Records per page  
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
    GCS_PREFIX = os.environ.get('GCS_PREFIX', 'talon')
    STATE_KEY = os.environ.get('STATE_KEY', 'talon/state.json')
    CLIENT_ID = os.environ.get('CLIENT_ID')
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
    TSG_ID = os.environ.get('TSG_ID')
    API_BASE_URL = os.environ.get('API_BASE_URL', 'https://api.strata.paloaltonetworks.com')
    MAX_RECORDS = int(os.environ.get('MAX_RECORDS', '5000'))
    PAGE_SIZE = int(os.environ.get('PAGE_SIZE', '1000'))
    LOOKBACK_HOURS = int(os.environ.get('LOOKBACK_HOURS', '24'))
    
    AUTH_URL = "https://auth.apps.paloaltonetworks.com/oauth2/access_token"
    
    def to_unix_millis(dt: datetime) -> int:
      """Convert datetime to Unix epoch milliseconds."""
      if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
      dt = dt.astimezone(timezone.utc)
      return int(dt.timestamp() * 1000)
    
    def parse_datetime(value: str) -> datetime:
      """Parse ISO datetime string to datetime object."""
      if [value](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.ObjectCustomContextPayload.html#google_cloud_storage_blob_ObjectCustomContextPayload_value).endswith("Z"):
        value = value[:-1] + "+00:00"
      return datetime.fromisoformat(value)
    
    def get_access_token():
      """
      Obtain OAuth2 access token using client credentials grant.
      """
      import base64
      credentials = base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode()
    
      headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': f'Basic {credentials}',
        'Accept': 'application/json'
      }
    
      body = f"grant_type=client_credentials&scope=tsg_id:{TSG_ID}"
    
      backoff = 1.0
      for attempt in range(3):
        response = http.request('POST', AUTH_URL, body=body, headers=headers)
    
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
    
      raise RuntimeError("Failed to get access token after 3 retries")
    
    @functions_framework.cloud_event
    def main(cloud_event):
      """
      Cloud Run function triggered by Pub/Sub to fetch Talon
      (Prisma Access Browser) logs and write to GCS.
    
      Args:
        cloud_event: CloudEvent object containing Pub/Sub message
      """
    
      if not all([GCS_BUCKET, CLIENT_ID, CLIENT_SECRET, TSG_ID]):
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
            # Overlap by 2 minutes to catch any delayed events
            last_time = last_time - timedelta(minutes=2)
          except Exception as e:
            print(f"Warning: Could not parse last_event_time: {e}")
    
        if last_time is None:
          last_time = now - timedelta(hours=LOOKBACK_HOURS)
    
        print(f"Fetching logs from {last_time.isoformat()} to {now.isoformat()}")
    
        # Get access token
        token = get_access_token()
    
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
    
        # Update state with newest event time
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
      Fetch event logs from Strata Logging Service API
      with pagination and rate limiting.
    
      Args:
        token: OAuth2 access token
        start_time: Start time for log query
        end_time: End time for log query
        page_size: Number of records per page
        max_records: Maximum total records to fetch
    
      Returns:
        Tuple of (records list, newest_event_time ISO string)
      """
      api_base = API_BASE_URL.rstrip('/')
      endpoint = f"{api_base}/logging-service/v1/queries"
    
      headers = {
        'Authorization': f'Bearer {token}',
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'User-Agent': 'GoogleSecOps-TalonCollector/1.0'
      }
    
      records = []
      newest_time = None
      page_num = 0
      backoff = 1.0
    
      # Create log query
      query_body = json.dumps({
        'query': 'SELECT * FROM `firewall.traffic`',
        'startTime': int(start_time.timestamp()),
        'endTime': int(end_time.timestamp()),
        'maxWaitTime': 30000,
        'pageSize': min(page_size, max_records)
      })
    
      try:
        response = http.request('POST', endpoint, body=query_body, headers=headers)
    
        if response.status == 429:
          retry_after = int(response.headers.get('Retry-After', str(int(backoff))))
          print(f"Rate limited (429). Retrying after {retry_after}s...")
          time.sleep(retry_after)
          response = http.request('POST', endpoint, body=query_body, headers=headers)
    
        if response.status not in (200, 201):
          print(f"HTTP Error: {response.status}")
          response_text = response.data.decode('utf-8')
          print(f"Response body: {response_text}")
          return [], None
    
        data = json.loads(response.data.decode('utf-8'))
        query_id = data.get('queryId')
        query_status = data.get('queryStatus', '')
    
      except Exception as e:
        print(f"Error creating query: {e}")
        return [], None
    
      # Poll for results
      results_endpoint = f"{api_base}/logging-service/v1/queries/{query_id}/results"
      scroll_token = None
    
      while True:
        page_num += 1
    
        if len(records) >= max_records:
          print(f"Reached max_records limit ({max_records})")
          break
    
        try:
          params = {'pageSize': min(page_size, max_records - len(records))}
          if scroll_token:
            params['scrollToken'] = scroll_token
    
          url = results_endpoint + '?' + '&'.join(f'{k}={v}' for k, v in params.items())
          response = http.request('GET', url, headers=headers)
    
          # Handle rate limiting with exponential backoff
          if response.status == 429:
            retry_after = int(response.headers.get('Retry-After', str(int(backoff))))
            print(f"Rate limited (429). Retrying after {retry_after}s...")
            time.sleep(retry_after)
            backoff = min(backoff * 2, 30.0)
            continue
    
          if response.status == 202:
            print("Query still processing, waiting...")
            time.sleep(5)
            continue
    
          backoff = 1.0
    
          if response.status != 200:
            print(f"HTTP Error: {response.status}")
            response_text = response.data.decode('utf-8')
            print(f"Response body: {response_text}")
            return records, newest_time
    
          data = json.loads(response.data.decode('utf-8'))
    
          page_results = data.get('result', {}).get('logs', [])
    
          if not page_results:
            print(f"No more results (empty page)")
            break
    
          print(f"Page {page_num}: Retrieved {len(page_results)} events")
          records.extend(page_results)
    
          # Track newest event time
          for event in page_results:
            try:
              event_ts = event.get('time_generated') or event.get('receive_time')
              if event_ts:
                if isinstance(event_ts, (int, float)):
                  event_dt = datetime.fromtimestamp(event_ts, tz=timezone.utc)
                  event_time = event_dt.isoformat()
                else:
                  event_time = str(event_ts)
                if newest_time is None or parse_datetime(event_time) > parse_datetime(newest_time):
                  newest_time = event_time
            except Exception as e:
              print(f"Warning: Could not parse event time: {e}")
    
          # Check for more results
          scroll_token = data.get('result', {}).get('scrollToken')
          if not scroll_token:
            print("No more pages (no scroll token)")
            break
    
        except Exception as e:
          print(f"Error fetching logs: {e}")
          return records, newest_time
    
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
**Name** | `talon-logs-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the topic `talon-logs-trigger`  
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
  5. Click on `talon-logs-collector`.
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         Fetching logs from YYYY-MM-DDTHH:MM:SS+00:00 to YYYY-MM-DDTHH:MM:SS+00:00
         Page 1: Retrieved X events
         Wrote X records to gs://talon-logs/talon/logs_YYYYMMDD_HHMMSS.ndjson
         Successfully processed X records
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click on your bucket name (`talon-logs`).

  10. Navigate to the `talon/` folder.

  11. Verify that a new `.ndjson` file was created with the current timestamp.




If you see errors in the logs:

  * **HTTP 401** : Check OAuth2 credentials in environment variables
  * **HTTP 403** : Verify service account has required permissions in Strata Cloud Manager
  * **HTTP 429** : Rate limiting - function will automatically retry with backoff
  * **Missing environment variables** : Check all required variables are set



## Configure a feed in Google SecOps to ingest Talon logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Talon Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Talon** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address.

**Note:** Each Google SecOps instance has a unique service account. Do not use service accounts from other documentation or examples.
  9. Click **Next**.

  10. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://talon-logs/talon/
           

       * Replace: 
         * `talon-logs`: Your GCS bucket name.
         * `talon`: Optional prefix/folder path where logs are stored (leave empty for root).
**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never** : Never deletes any files after transfers (recommended for testing).
       * **Delete transferred files** : Deletes files after successful transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.

**Note:** If you select a deletion option, the service account must have **Storage Object Admin** role instead of Storage Object Viewer. Update IAM permissions accordingly.
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days)

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)

     * **Ingestion labels** : The label to be applied to the events from this feed

  11. Click **Next**.

  12. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## Grant IAM permissions to the Google SecOps service account

  * The Google SecOps service account needs **Storage Object Viewer** role on your GCS bucket.


  1. Go to **Cloud Storage > Buckets**.
  2. Click on your bucket name.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Paste the Google SecOps service account email
     * **Assign roles** : Select **Storage Object Viewer**
  6. Click **Save**.

**Note:** If you plan to use the deletion option "Delete transferred files" or "Delete transferred files and empty directories," grant **Storage Object Admin** role instead of Storage Object Viewer.

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
user.externalId, user.tenantExternalId, policy.action | additional.fields | Merged with labels for each source field if not empty  
timestamp | metadata.event_timestamp | Parsed using date filter with ISO8601 and yyyy-MM-ddTHH:mm:ss.SSSSSSSSSZ formats  
has_principal, has_target | metadata.event_type | Set to STATUS_UPDATE if has_principal is true and has_target is false, else GENERIC_EVENT  
user.tenantId | metadata.product_deployment_id | Value copied directly if not empty  
type | metadata.product_event_type | Value copied directly if not empty  
device.deviceUuid | metadata.product_log_id | Value copied directly if not empty  
network.protocol | network.application_protocol | Set to "HTTPS" if matches (?i)https  
network.http.method | network.http.method | Value copied directly if not empty  
device.userAgent | network.http.parsed_user_agent | Value copied directly if not empty  
device.userAgent | network.http.user_agent | Value copied directly if not empty  
user.tenantName | observer.hostname | Value copied directly if not empty  
device.hostname | principal.hostname | Value copied directly if not empty  
device.ipAddress | principal.ip | Extracted IP using grok pattern %{IP:prin_ip}, merged if not empty  
user.email | principal.user.email_addresses | Merged if matches email regex ^.+@.+$  
user.name | principal.user.user_display_name | Value copied directly if not empty  
user.id | principal.user.userid | Value copied directly if not empty  
device.browserType, device.browserVersion, device.browserBrand, batchId | security_result.about.resource.attribute.labels | Merged with labels for each source field if not empty  
policy.ruleId | security_result.rule_id | Value copied directly if not empty  
policy.ruleDescription | security_result.summary | Value copied directly if not empty  
device.os.type, event_platform | target.platform | Set to WINDOWS if device.os.type == "windows", else MAC if event_platform in ["Mac","iOS"], else LINUX if event_platform == "Lin"  
| metadata.product_name | Set to "Talon"  
| metadata.vendor_name | Set to "TALON"  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
