---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/mcafee-skyhigh-casb/
title: Collect Skyhigh Security CASB (formerly McAfee Skyhigh CASB) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T07:14:30.101026+00:00
---

# Collect Skyhigh Security CASB (formerly McAfee Skyhigh CASB) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/mcafee-skyhigh-casb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Skyhigh Security CASB (formerly McAfee Skyhigh CASB) logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Skyhigh Security CASB (formerly known as McAfee Skyhigh CASB) logs to Google Security Operations using Google Cloud Storage V2.

Skyhigh Security CASB is a cloud access security broker (CASB) that provides visibility, compliance, data security, and threat protection for cloud services. It monitors user activity across SaaS, PaaS, and IaaS environments, detecting anomalies, enforcing DLP policies, and generating incident and audit logs through its REST API.

## Before you begin

Make sure that you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * A Skyhigh Security CASB tenant with administrative access
  * API credentials from the Skyhigh Security console (Client ID and Client Secret)
  * The Skyhigh Cloud Connector installed and configured



## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `skyhigh-casb-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Collect Skyhigh Security CASB API credentials

### Create API client credentials

  1. Sign in to the [Skyhigh Security console](https://www.myshn.net).
  2. Go to **Settings > Infrastructure > API Integration**.
  3. Click **Create API Client**.
  4. Enter a name for the API client (for example, `Google SecOps Integration`).

  5. Select the following scopes:

     * **Incidents** : Read access to CASB incident data
     * **Anomalies** : Read access to anomaly events
     * **Audit Logs** : Read access to audit trail
  6. Click **Create**.

  7. Copy and save the following details in a secure location:

     * **Client ID** : The generated client identifier
     * **Client Secret** : The generated client secret (shown only once)
**Note:** The Client Secret is displayed only once at the time of creation. If you lose it, you must generate new credentials.



### Get tenant base URL

  1. Sign in to the [Skyhigh Security console](https://www.myshn.net).

  2. Note the base URL from the browser address bar. The format depends on your region:

     * US: `https://www.myshn.net`
     * EU: `https://www.myshn.eu`
     * SG: `https://www.myshn.sg`



### Test API access

  * Test your credentials before proceeding with the integration:
        
        # Replace with your actual credentials
        CLIENT_ID="your-client-id"
        CLIENT_SECRET="your-client-secret"
        BASE_URL="https://www.myshn.net"
        
        # Get OAuth 2.0 access token
        TOKEN=$(curl -s -X POST "${BASE_URL}/shnapi/rest/external/api/v1/oauth/token" \
            -H "Content-Type: application/x-www-form-urlencoded" \
            -d "grant_type=client_credentials&client_id=${CLIENT_ID}&client_secret=${CLIENT_SECRET}" \
            | python3 -c "import sys,json; print(json.load(sys.stdin)['access_token'])")
        
        # Test API access - list incidents
        curl -v -H "Authorization: Bearer ${TOKEN}" \
            "${BASE_URL}/shnapi/rest/external/api/v1/incidents?limit=1"
        




## Create service account for Cloud Run function

The Cloud Run function needs a service account with permissions to write to GCS bucket and be invoked by Pub/Sub.

### Create service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `skyhigh-casb-collector-sa`
     * **Service account description** : Enter `Service account for Cloud Run function to collect Skyhigh Security CASB logs`
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
  2. Click on your bucket name (for example, `skyhigh-casb-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.

  5. Provide the following configuration details:

     * **Add principals** : Enter the service account email (for example, `skyhigh-casb-collector-sa@PROJECT_ID.iam.gserviceaccount.com`)
     * **Assign roles** : Select **Storage Object Admin**
  6. Click **Save**.




## Create Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.

  3. Provide the following configuration details:

     * **Topic ID** : Enter `skyhigh-casb-logs-trigger`
     * Leave other settings as default
  4. Click **Create**.




## Create Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from the Skyhigh Security CASB API and write them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).

  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `skyhigh-casb-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose the topic `skyhigh-casb-logs-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select the service account `skyhigh-casb-collector-sa`.
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `skyhigh-casb-logs` | GCS bucket name  
`GCS_PREFIX` | `skyhigh-casb` | Prefix for log files  
`STATE_KEY` | `skyhigh-casb/state.json` | State file path  
`SKYHIGH_BASE_URL` | `https://www.myshn.net` | Skyhigh Security base URL  
`SKYHIGH_CLIENT_ID` | `your-client-id` | API Client ID  
`SKYHIGH_CLIENT_SECRET` | `your-client-secret` | API Client Secret  
`MAX_RECORDS` | `5000` | Max records per run  
`PAGE_SIZE` | `100` | Records per page  
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
    import base64
    import urllib.parse
    
    # Initialize HTTP client with timeouts
    http = urllib3.PoolManager(
      timeout=urllib3.Timeout(connect=5.0, read=30.0),
      retries=False,
    )
    
    # Initialize Storage client
    storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    
    # Environment variables
    GCS_BUCKET = os.environ.get('GCS_BUCKET')
    GCS_PREFIX = os.environ.get('GCS_PREFIX', 'skyhigh-casb')
    STATE_KEY = os.environ.get('STATE_KEY', 'skyhigh-casb/state.json')
    SKYHIGH_BASE_URL = os.environ.get('SKYHIGH_BASE_URL', '[https://www.myshn.net](https://www.myshn.net)')
    SKYHIGH_CLIENT_ID = os.environ.get('SKYHIGH_CLIENT_ID')
    SKYHIGH_CLIENT_SECRET = os.environ.get('SKYHIGH_CLIENT_SECRET')
    MAX_RECORDS = int(os.environ.get('MAX_RECORDS', '5000'))
    PAGE_SIZE = int(os.environ.get('PAGE_SIZE', '100'))
    LOOKBACK_HOURS = int(os.environ.get('LOOKBACK_HOURS', '24'))
    
    def get_access_token(base_url: str, client_id: str, client_secret: str) -> str:
      """Get OAuth 2.0 access token from Skyhigh Security."""
      token_url = f"{base_url}/shnapi/rest/external/api/v1/oauth/token"
      body = urllib.parse.urlencode({
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
      }).encode('utf-8')
    
      response = http.request(
        'POST',
        token_url,
        body=body,
        headers={'Content-Type': 'application/x-www-form-urlencoded'},
      )
    
      if response.status != 200:
        raise Exception(f"Failed to get access token: HTTP {response.status} - {response.data.decode('utf-8')}")
    
      token_data = json.loads(response.data.decode('utf-8'))
      return token_data['access_token']
    
    @functions_framework.cloud_event
    def main(cloud_event):
      """
      Cloud Run function triggered by Pub/Sub to fetch Skyhigh Security CASB
      logs and write to GCS.
    
      Args:
        cloud_event: CloudEvent object containing Pub/Sub message
      """
    
      if not all([GCS_BUCKET, SKYHIGH_BASE_URL, SKYHIGH_CLIENT_ID, SKYHIGH_CLIENT_SECRET]):
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
    
        # Get OAuth token
        access_token = get_access_token(SKYHIGH_BASE_URL, SKYHIGH_CLIENT_ID, SKYHIGH_CLIENT_SECRET)
        print("Successfully obtained access token")
    
        all_records = []
        newest_time = None
    
        # Fetch incidents
        incidents, inc_newest = fetch_logs(
          base_url=SKYHIGH_BASE_URL,
          access_token=access_token,
          endpoint_path="/shnapi/rest/external/api/v1/incidents",
          start_time=last_time,
          end_time=now,
          page_size=PAGE_SIZE,
          max_records=MAX_RECORDS,
          log_category="incidents",
        )
        all_records.extend(incidents)
        if inc_newest:
          newest_time = inc_newest
    
        # Fetch anomalies
        anomalies, anom_newest = fetch_logs(
          base_url=SKYHIGH_BASE_URL,
          access_token=access_token,
          endpoint_path="/shnapi/rest/external/api/v1/anomalies",
          start_time=last_time,
          end_time=now,
          page_size=PAGE_SIZE,
          max_records=MAX_RECORDS,
          log_category="anomalies",
        )
        all_records.extend(anomalies)
        if anom_newest and (newest_time is None or parse_datetime(anom_newest) > parse_datetime(newest_time)):
          newest_time = anom_newest
    
        if not all_records:
          print("No new log records found.")
          save_state(bucket, STATE_KEY, now.isoformat())
          return
    
        # Write to GCS as NDJSON
        timestamp = now.strftime('%Y%m%d_%H%M%S')
        object_key = f"{GCS_PREFIX}/logs_{timestamp}.ndjson"
        blob = bucket.blob(object_key)
    
        ndjson = '\n'.join([json.dumps(record, ensure_ascii=False) for record in all_records]) + '\n'
        blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(ndjson, content_type='application/x-ndjson')
    
        print(f"Wrote {len(all_records)} records to gs://{GCS_BUCKET}/{object_key}")
    
        # Update state with newest event time
        if newest_time:
          save_state(bucket, STATE_KEY, newest_time)
        else:
          save_state(bucket, STATE_KEY, now.isoformat())
    
        print(f"Successfully processed {len(all_records)} records")
    
      except Exception as e:
        print(f'Error processing logs: {str(e)}')
        raise
    
    def parse_datetime(value: str) -> datetime:
      """Parse ISO datetime string to datetime object."""
      if [value](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.ObjectCustomContextPayload.html#google_cloud_storage_blob_ObjectCustomContextPayload_value).endswith("Z"):
        value = value[:-1] + "+00:00"
      return datetime.fromisoformat(value)
    
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
    
    def fetch_logs(base_url: str, access_token: str, endpoint_path: str, start_time: datetime, end_time: datetime, page_size: int, max_records: int, log_category: str):
      """
      Fetch logs from Skyhigh Security CASB API with pagination
      and rate limiting.
    
      Args:
        base_url: Skyhigh Security base URL
        access_token: OAuth 2.0 access token
        endpoint_path: API endpoint path
        start_time: Start time for log query
        end_time: End time for log query
        page_size: Number of records per page
        max_records: Maximum total records to fetch
        log_category: Category name for logging
    
      Returns:
        Tuple of (records list, newest_event_time ISO string)
      """
      endpoint = f"{base_url.rstrip('/')}{endpoint_path}"
    
      headers = {
        'Authorization': f'Bearer {access_token}',
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'User-Agent': 'GoogleSecOps-SkyhighCASBCollector/1.0'
      }
    
      records = []
      newest_time = None
      page_num = 0
      backoff = 1.0
      offset = 0
    
      start_iso = start_time.strftime('%Y-%m-%dT%H:%M:%SZ')
      end_iso = end_time.strftime('%Y-%m-%dT%H:%M:%SZ')
    
      while True:
        page_num += 1
    
        if len(records) >= max_records:
          print(f"Reached max_records limit ({max_records}) for {log_category}")
          break
    
        limit = min(page_size, max_records - len(records))
        url = f"{endpoint}?start_time={start_iso}&end_time={end_iso}&offset={offset}&limit={limit}"
    
        try:
          response = http.request('GET', url, headers=headers)
    
          # Handle rate limiting with exponential backoff
          if response.status == 429:
            retry_after = int(response.headers.get('Retry-After', str(int(backoff))))
            print(f"Rate limited (429). Retrying after {retry_after}s...")
            time.sleep(retry_after)
            backoff = min(backoff * 2, 30.0)
            continue
    
          backoff = 1.0
    
          if response.status != 200:
            print(f"HTTP Error: {response.status} for {log_category}")
            response_text = response.data.decode('utf-8')
            print(f"Response body: {response_text}")
            return [], None
    
          data = json.loads(response.data.decode('utf-8'))
    
          page_results = data.get('data', data.get('results', data.get('items', [])))
    
          if not page_results:
            print(f"No more results (empty page) for {log_category}")
            break
    
          print(f"Page {page_num}: Retrieved {len(page_results)} {log_category} events")
          records.extend(page_results)
    
          # Track newest event time
          for event in page_results:
            try:
              event_time = event.get('timestamp') or event.get('created_at') or event.get('eventTime')
              if event_time:
                if newest_time is None or parse_datetime(str(event_time)) > parse_datetime(str(newest_time)):
                  newest_time = str(event_time)
            except Exception as e:
              print(f"Warning: Could not parse event time: {e}")
    
          # If we got fewer results than requested, no more pages
          if len(page_results) < limit:
            print(f"Last page reached for {log_category}")
            break
    
          offset += len(page_results)
    
        except Exception as e:
          print(f"Error fetching {log_category} logs: {e}")
          return [], None
    
      print(f"Retrieved {len(records)} total {log_category} records from {page_num} pages")
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
**Name** | `skyhigh-casb-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the topic `skyhigh-casb-logs-trigger`  
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
  5. Click on `skyhigh-casb-collector`.
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         Fetching logs from YYYY-MM-DDTHH:MM:SS+00:00 to YYYY-MM-DDTHH:MM:SS+00:00
         Successfully obtained access token
         Page 1: Retrieved X incidents events
         Page 1: Retrieved X anomalies events
         Wrote X records to gs://skyhigh-casb-logs/skyhigh-casb/logs_YYYYMMDD_HHMMSS.ndjson
         Successfully processed X records
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click on your bucket name (`skyhigh-casb-logs`).

  10. Navigate to the `skyhigh-casb/` folder.

  11. Verify that a new `.ndjson` file was created with the current timestamp.




If you see errors in the logs:

  * **HTTP 401** : Check API credentials in environment variables or token may be expired
  * **HTTP 403** : Verify API client has required scopes in Skyhigh Security console
  * **HTTP 429** : Rate limiting - function will automatically retry with backoff
  * **Missing environment variables** : Check all required variables are set



## Configure a feed in Google SecOps to ingest Skyhigh Security CASB logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Skyhigh Security CASB Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **McAfee Skyhigh CASB** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address.

**Note:** Each Google SecOps instance has a unique service account. Do not use service accounts from other documentation or examples.
  9. Click **Next**.

  10. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://skyhigh-casb-logs/skyhigh-casb/
           

       * Replace: 
         * `skyhigh-casb-logs`: Your GCS bucket name.
         * `skyhigh-casb`: Optional prefix/folder path where logs are stored (leave empty for root).
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

The Google SecOps service account needs **Storage Object Viewer** role on your GCS bucket.

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
EventReceivedTime | metadata.event_timestamp | Converted to timestamp from `yyyy-MM-dd HH:mm:ss` format  
FileSize | target.file.size | Directly mapped, converted to uinteger  
Hostname | principal.hostname | Directly mapped  
MessageSourceAddress | principal.ip | Directly mapped, merged if multiple instances  
Severity | additional.fields.value.string_value (key: SEVERITY) | Directly mapped  
SeverityValue | additional.fields.value.string_value (key: SEVERITY_VALUE) | Directly mapped  
SourceModuleName | additional.fields.value.string_value (key: SOURCE_MODULE_NAME) | Directly mapped  
SourceModuleType | principal.resource.resource_subtype | Directly mapped  
SyslogFacility | security_result.about.resource.attribute.labels.value (key: SYSLOG_FACILITY) | Directly mapped  
SyslogFacilityValue | security_result.about.resource.attribute.labels.value (key: SYSLOG_FACILITY_VALUE) | Directly mapped  
SyslogSeverity | security_result.about.resource.attribute.labels.value (key: SYSLOG_SEVERITY) | Directly mapped  
SyslogSeverityValue | security_result.about.resource.attribute.labels.value (key: SYSLOG_SEVERITY_VALUE) | Directly mapped  
activityName | metadata.product_event_type | Directly mapped, brackets removed  
actorId | principal.user.userid | Directly mapped, also added to email_addresses if it is an email  
actorIdType | principal.user.attribute.roles.name | Directly mapped  
collaborationSharedLink | security_result.about.resource.attribute.labels.value (key: COLLABORATION_SHARED_LINK) | Directly mapped  
contentItemId | target.file.full_path (if contentItemType is FILE) | Directly mapped, quotes removed  
contentItemId | target.url (if contentItemType is SAAS_RESOURCE) | Directly mapped, quotes removed  
contentItemHierarchy | additional.fields.value.string_value (key: CONTENT_ITEM_HIERARCHY) | Directly mapped, quotes removed  
contentItemName | target.resource.name | Directly mapped, quotes removed  
contentItemType | additional.fields.value.string_value (key: CONTENT_ITEM_TYPE) | Directly mapped  
incidentGroup | security_result.detection_fields.value (key: INCIDENT_GROUP) | Directly mapped  
incidentId | metadata.product_log_id | Directly mapped  
incidentRiskScore | security_result.detection_fields.value (key: INCIDENT_RISK_SCORE) | Directly mapped  
incidentRiskSeverityId |  | Used in combination with riskSeverity to determine security_result.severity  
informationAccountId | target.resource.product_object_id | Directly mapped  
informationAnomalyCategory | security_result.category_details | Directly mapped, quotes removed  
informationAnomalyCause | security_result.detection_fields.value (key: INFO_ANOMALY_CAUSE) | Directly mapped, quotes removed  
informationCategory | security_result.category_details | Directly mapped  
informationConfigType | additional.fields.value.string_value (key: INFORMATION_CONFIG_TYPE) | Directly mapped, quotes removed  
informationContentItemParent | target.resource.parent | Directly mapped, quotes removed  
informationEventId | additional.fields.value.string_value (key: INFORMATION_EVENT_ID) | Directly mapped  
informationExternalCollaboratorsCount | additional.fields.value.string_value (key: INFORMATION_COLLAB_COUNT) | Directly mapped  
informationFileTypes | additional.fields.value.list_value.values.string_value (key: FILE_TYPE) | Extracted from JSON-like string, brackets and quotes removed  
informationLastExecutedResponseLabel | additional.fields.value.string_value (key: INFORMATION_LAST_RESPONSE) | Directly mapped  
informationScanName | metadata.description | Directly mapped, quotes removed  
informationScanRunDate |  | Not mapped to UDM  
informationSource | additional.fields.value.string_value (key: INFORMATION_SOURCE) | Directly mapped  
informationUniqueMatchCount | additional.fields.value.string_value (key: INFORMATION_UNQ_MATCH_COUNT) | Directly mapped  
informationUserAttributesSAMAccountName | principal.user.user_display_name | Directly mapped, brackets removed  
instanceId | principal.resource.product_object_id | Directly mapped  
instanceName | principal.resource.name | Directly mapped, quotes removed  
policyId | security_result.rule_id | Directly mapped  
policyName | security_result.summary | Directly mapped, quotes removed  
response |  | Used to determine security_result.action (ALLOW or BLOCK)  
riskSeverity |  | Used in combination with incidentRiskSeverityId to determine security_result.severity, converted to uppercase  
serviceNames | target.application | Directly mapped, brackets, quotes and extra spaces removed  
sourceIps | principal.ip | Extracted from JSON-like string, merged if multiple instances  
status | additional.fields.value.string_value (key: STATUS) | Directly mapped  
threatCategory | security_result.threat_name | Directly mapped, quotes removed  
totalMatchCount | security_result.detection_fields.value (key: TOTAL_MATCH_COUNT) | Directly mapped  
N/A | metadata.vendor_name | `MCAFEE` \- Static value  
N/A | metadata.product_name | `MCAFEE_SKYHIGH_CASB` \- Static value  
N/A | metadata.log_type | `MCAFEE_SKYHIGH_CASB` \- Static value  
N/A | principal.resource.type | `VIRTUAL_MACHINE` \- Set if instanceName or instanceId are present  
N/A | metadata.event_type | Determined based on a set of conditions: - `USER_RESOURCE_UPDATE_CONTENT` if actorId, contentItemId or contentItemName are present - `USER_UNCATEGORIZED` if actorId and target are present - `STATUS_UPDATE` if Hostname or MessageSourceAddress are present - `GENERIC_EVENT` otherwise  
N/A | security_result.severity | Determined based on the combination of riskSeverity and incidentRiskSeverityId: - `LOW` if riskSeverity is `LOW` and incidentRiskSeverityId is `0` \- `MEDIUM` if riskSeverity is `MEDIUM` and incidentRiskSeverityId is `1` \- `HIGH` if riskSeverity is `HIGH` and incidentRiskSeverityId is `2` \- `INFORMATIONAL` if riskSeverity is `INFO` and incidentRiskSeverityId is `3`  
`column2` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`intermediary_host` | `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname` | Mapped from changelog  
`column3` | `event.idm.read_only_udm.network.http.response_code` | Mapped from changelog  
`column8` | `event.idm.read_only_udm.network.received_bytes` | Mapped from changelog  
`column9` | `event.idm.read_only_udm.network.sent_bytes` | Mapped from changelog  
`column10` | `event.idm.read_only_udm.network.http.user_agent` | Mapped from changelog  
`column10` | `event.idm.read_only_udm.network.http.parsed_user_agent` | Mapped from changelog  
`http_method` | `event.idm.read_only_udm.network.http.method` | Mapped from changelog  
`tar_host` | `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` | Mapped from changelog  
`tar_port` | `event.idm.read_only_udm.target.port` | Mapped from changelog  
`application_protocol` | `event.idm.read_only_udm.network.application_protocol` | Mapped from changelog  
`tar_url` | `event.idm.read_only_udm.target.url` | Mapped from changelog  
`http_version` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`column1` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`intermediary_application` | `event.idm.read_only_udm.intermediary.application` | Mapped from changelog  
`column5` | `event.idm.read_only_udm.security_result.category_details` | Mapped from changelog  
`column6` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column12` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`column7` | `event.idm.read_only_udm.target.file.mime_type` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/mcafee-skyhigh-casb-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
