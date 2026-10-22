---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/mandiant-custom-ioc/
title: Collect Mandiant Threat Intelligence Custom IOC logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:37:29.154054+00:00
---

# Collect Mandiant Threat Intelligence Custom IOC logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/mandiant-custom-ioc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Mandiant Threat Intelligence Custom IOC logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Mandiant Threat Intelligence Custom IOC data to Google Security Operations using Google Cloud Storage V2.

Mandiant Threat Intelligence provides context-rich indicators of compromise (IOCs) including IP addresses, domains, URLs, file hashes, and email addresses. The platform delivers threat intelligence based on frontline incident response investigations, enabling security teams to identify and prioritize threats targeting their organization.

## Before you begin

Ensure that you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * Active Mandiant Advantage Threat Intelligence subscription
  * Privileged access to Mandiant Advantage portal



## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `mandiant-ioc-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Collect Mandiant Advantage credentials

### Get Mandiant site URL

  1. Sign in to your Mandiant Advantage instance.
  2. Note your site URL from the browser address bar. 
     * The URL is: `https://advantage.mandiant.com`



### Create API credentials

  1. Sign in to [Mandiant Advantage](https://advantage.mandiant.com/).
  2. Go to **Settings**.
  3. Scroll down to **API Access and Keys** or select it from the navigation menu.
  4. Click **Get Key ID and Secret**.
  5. Copy and save the API credentials securely: 
     * **Key ID** : Copy this value (also referred to as API Key ID or Public Key)
     * **Key Secret** : Copy this value (also referred to as API Secret or Private Key)

**Note:** The Key Secret is displayed only once. Store it in a secure location immediately. If you lose the secret, you must generate new credentials.

### Verify permissions

To verify the account has the required permissions:

  1. Sign in to Mandiant Advantage.
  2. Go to **Settings**.
  3. Review your user permissions under **User Information**.
  4. Verify that you have access to **Threat Intelligence** module.
  5. If you cannot see Threat Intelligence data, contact your Mandiant administrator to grant appropriate permissions.



### Test API access

  * Test your credentials before proceeding with the integration:
        
        # Replace with your actual credentials
        API_KEY_ID="your-key-id"
        API_SECRET="your-key-secret"
        API_BASE="https://api.intelligence.mandiant.com"
        
        # Get OAuth token
        TOKEN=$(curl -s -X POST "${API_BASE}/token" \
            -H "Content-Type: application/x-www-form-urlencoded" \
            -d "grant_type=client_credentials" \
            -u "${API_KEY_ID}:${API_SECRET}" | jq -r '.access_token')
        
        # Test API access
        curl -v -H "Authorization: Bearer ${TOKEN}" \
            "${API_BASE}/v4/indicator?limit=1"
        




If the test is successful, you should receive a JSON response with indicator data. If you receive an error:

  * **HTTP 401** : Check that API Key ID and Secret are correct
  * **HTTP 403** : Verify account has Threat Intelligence permissions
  * **HTTP 404** : Verify the API base URL is correct



## Create service account for Cloud Run function

The Cloud Run function needs a service account with permissions to write to GCS bucket and be invoked by Pub/Sub.

### Create service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `mandiant-ioc-collector-sa` (for example, `mandiant-ioc-collector-sa`)
     * **Service account description** : Enter `Service account for Cloud Run function to collect Mandiant IOC logs`
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



These roles are required for: \- **Storage Object Admin** : Write logs to GCS bucket and manage state files \- **Cloud Run Invoker** : Allow Pub/Sub to invoke the function \- **Cloud Functions Invoker** : Allow function invocation

### Grant IAM permissions on GCS bucket

Grant the service account write permissions on the GCS bucket:

  1. Go to **Cloud Storage > Buckets**.
  2. Click on your bucket name (for example, `mandiant-ioc-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `mandiant-ioc-collector-sa@PROJECT_ID.iam.gserviceaccount.com`)
     * **Assign roles** : Select **Storage Object Admin**
  6. Click **Save**.



## Create Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `mandiant-ioc-trigger` (for example, `mandiant-ioc-trigger`)
     * Leave other settings as default
  4. Click **Create**.



## Create Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch IOC data from Mandiant Threat Intelligence API and write them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `mandiant-ioc-collector` (for example, `mandiant-ioc-collector`)  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose the Pub/Sub topic (for example, `mandiant-ioc-trigger`).
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.

**Note:** Pub/Sub will automatically handle authentication when invoking the function.

  1. Scroll down and expand **Containers, Networking, Security**.
  2. Go to the **Security** tab: 
     * **Service account** : Select the service account (for example, `mandiant-ioc-collector-sa`)
  3. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `mandiant-ioc-logs` | GCS bucket name  
`GCS_PREFIX` | `mandiant-ioc` | Prefix for log files  
`STATE_KEY` | `mandiant-ioc/state.json` | State file path  
`API_BASE` | `https://api.intelligence.mandiant.com` | API base URL  
`API_KEY_ID` | `your-key-id` | Mandiant API Key ID  
`API_SECRET` | `your-key-secret` | Mandiant API Secret  
`MAX_RECORDS` | `1000` | Max records per run  
`PAGE_SIZE` | `100` | Records per page  
`LOOKBACK_HOURS` | `24` | Initial lookback period  
  4. In the **Variables & Secrets** section, scroll down to **Requests** :

     * **Request timeout** : Enter `600` seconds (10 minutes)
  5. Go to the **Settings** tab:

     * In the **Resources** section: 
       * **Memory** : Select **512 MiB** or higher
       * **CPU** : Select **1**
  6. In the **Revision scaling** section:

     * **Minimum number of instances** : Enter `0`
     * **Maximum number of instances** : Enter `100` (or adjust based on expected load)
  7. Click **Create**.

  8. Wait for the service to be created (1-2 minutes).

  9. After the service is created, the **inline code editor** will open automatically.




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
           
           # Initialize HTTP client with timeouts
           http = urllib3.PoolManager(
               timeout=urllib3.Timeout(connect=5.0, read=30.0),
               retries=False,
           )
           
           # Initialize Storage client
           storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
           
           # Environment variables
           GCS_BUCKET = os.environ.get('GCS_BUCKET')
           GCS_PREFIX = os.environ.get('GCS_PREFIX', 'mandiant-ioc')
           STATE_KEY = os.environ.get('STATE_KEY', 'mandiant-ioc/state.json')
           API_BASE = os.environ.get('API_BASE', 'https://api.intelligence.mandiant.com')
           API_KEY_ID = os.environ.get('API_KEY_ID')
           API_SECRET = os.environ.get('API_SECRET')
           MAX_RECORDS = int(os.environ.get('MAX_RECORDS', '1000'))
           PAGE_SIZE = int(os.environ.get('PAGE_SIZE', '100'))
           LOOKBACK_HOURS = int(os.environ.get('LOOKBACK_HOURS', '24'))
           
           def to_unix_seconds(dt: datetime) -> int:
               """Convert datetime to Unix epoch seconds."""
               if dt.tzinfo is None:
                   dt = dt.replace(tzinfo=timezone.utc)
               dt = dt.astimezone(timezone.utc)
               return int(dt.timestamp())
           
           def parse_datetime(value: str) -> datetime:
               """Parse ISO datetime string to datetime object."""
               if [value](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.ObjectCustomContextPayload.html#google_cloud_storage_blob_ObjectCustomContextPayload_value).endswith("Z"):
                   value = value[:-1] + "+00:00"
               return datetime.fromisoformat(value)
           
           @functions_framework.cloud_event
           def main(cloud_event):
               """
               Cloud Run function triggered by Pub/Sub to fetch Mandiant IOC data and write to GCS.
           
               Args:
                   cloud_event: CloudEvent object containing Pub/Sub message
               """
           
               if not all([GCS_BUCKET, API_BASE, API_KEY_ID, API_SECRET]):
                   print('Error: Missing required environment variables')
                   return
           
               try:
                   # Get GCS bucket
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
           
                   print(f"Fetching IOCs from {last_time.isoformat()} to {now.isoformat()}")
           
                   # Convert to Unix timestamps
                   start_epoch = to_unix_seconds(last_time)
                   end_epoch = to_unix_seconds(now)
           
                   # Fetch IOCs
                   records, newest_event_time = fetch_iocs(
                       api_base=API_BASE,
                       api_key_id=API_KEY_ID,
                       api_secret=API_SECRET,
                       start_epoch=start_epoch,
                       end_epoch=end_epoch,
                       page_size=PAGE_SIZE,
                       max_records=MAX_RECORDS,
                   )
           
                   if not records:
                       print("No new IOC records found.")
                       save_state(bucket, STATE_KEY, now.isoformat())
                       return
           
                   # Write to GCS as NDJSON
                   timestamp = now.strftime('%Y%m%d_%H%M%S')
                   object_key = f"{GCS_PREFIX}/iocs_{timestamp}.ndjson"
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
                   print(f'Error processing IOCs: {str(e)}')
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
           
           def get_oauth_token(api_base: str, api_key_id: str, api_secret: str) -> str:
               """Get OAuth 2.0 access token from Mandiant API."""
               token_url = f"{api_base}/token"
           
               # Create Basic Auth header
               auth_string = f"{api_key_id}:{api_secret}"
               auth_bytes = auth_string.encode('utf-8')
               auth_b64 = base64.b64encode(auth_bytes).decode('utf-8')
           
               headers = {
                   'Authorization': f'Basic {auth_b64}',
                   'Content-Type': 'application/x-www-form-urlencoded',
                   'Accept': 'application/json'
               }
           
               body = 'grant_type=client_credentials'
           
               try:
                   response = http.request('POST', token_url, body=body, headers=headers)
           
                   if response.status != 200:
                       print(f"Token request failed: {response.status}")
                       print(f"Response: {response.data.decode('utf-8')}")
                       raise Exception(f"Failed to get OAuth token: HTTP {response.status}")
           
                   token_data = json.loads(response.data.decode('utf-8'))
                   return token_data['access_token']
           
               except Exception as e:
                   print(f"Error getting OAuth token: {e}")
                   raise
           
           def fetch_iocs(api_base: str, api_key_id: str, api_secret: str, start_epoch: int, end_epoch: int, page_size: int, max_records: int):
               """
               Fetch IOCs from Mandiant Threat Intelligence API with pagination and rate limiting.
           
               Args:
                   api_base: API base URL
                   api_key_id: Mandiant API Key ID
                   api_secret: Mandiant API Secret
                   start_epoch: Start time in Unix epoch seconds
                   end_epoch: End time in Unix epoch seconds
                   page_size: Number of records per page
                   max_records: Maximum total records to fetch
           
               Returns:
                   Tuple of (records list, newest_event_time ISO string)
               """
               # Get OAuth token
               access_token = get_oauth_token(api_base, api_key_id, api_secret)
           
               endpoint = f"{api_base}/v4/indicator"
           
               headers = {
                   'Authorization': f'Bearer {access_token}',
                   'Accept': 'application/json',
                   'Content-Type': 'application/json',
                   'User-Agent': 'GoogleSecOps-MandiantCollector/1.0'
               }
           
               records = []
               newest_time = None
               page_num = 0
               backoff = 1.0
               next_url = None
           
               while True:
                   page_num += 1
           
                   if len(records) >= max_records:
                       print(f"Reached max_records limit ({max_records})")
                       break
           
                   # Build request URL
                   if next_url:
                       # Use next URL from pagination
                       url = next_url
                   else:
                       # First request with time filtering
                       params = []
                       params.append(f"start_epoch={start_epoch}")
                       params.append(f"end_epoch={end_epoch}")
                       params.append(f"limit={min(page_size, max_records - len(records))}")
                       url = f"{endpoint}?{'&'.join(params)}"
           
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
                           print(f"HTTP Error: {response.status}")
                           response_text = response.data.decode('utf-8')
                           print(f"Response body: {response_text}")
                           return [], None
           
                       data = json.loads(response.data.decode('utf-8'))
           
                       # Extract results
                       page_results = data.get('indicators', [])
           
                       if not page_results:
                           print(f"No more results (empty page)")
                           break
           
                       print(f"Page {page_num}: Retrieved {len(page_results)} IOCs")
                       records.extend(page_results)
           
                       # Track newest event time
                       for ioc in page_results:
                           try:
                               # Extract last_updated timestamp
                               event_time = ioc.get('last_updated')
                               if event_time:
                                   if newest_time is None or parse_datetime(event_time) > parse_datetime(newest_time):
                                       newest_time = event_time
                           except Exception as e:
                               print(f"Warning: Could not parse event time: {e}")
           
                       # Check for next page
                       next_url = data.get('next')
                       if not next_url:
                           print("No more pages (no next URL)")
                           break
           
                   except Exception as e:
                       print(f"Error fetching IOCs: {e}")
                       return [], None
           
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
**Name** | `mandiant-ioc-collector-hourly` (for example, `mandiant-ioc-collector-hourly`)  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the Pub/Sub topic (for example, `mandiant-ioc-trigger`)  
**Message body** | `{}` (empty JSON object)  
  4. Click **Create**.




### Schedule frequency options

  * Choose frequency based on IOC update volume and latency requirements:

Frequency | Cron Expression | Use Case  
---|---|---  
Every 5 minutes | `*/5 * * * *` | High-volume, low-latency  
Every 15 minutes | `*/15 * * * *` | Medium volume  
Every hour | `0 * * * *` | Standard (recommended)  
Every 6 hours | `0 */6 * * *` | Low volume, batch processing  
Daily | `0 0 * * *` | Historical data collection  



### Test the integration

  1. In the **Cloud Scheduler** console, find your job (for example, `mandiant-ioc-collector-hourly`).
  2. Click **Force run** to trigger the job manually.
  3. Wait a few seconds.
  4. Go to **Cloud Run > Services**.
  5. Click on your function name (for example, `mandiant-ioc-collector`).
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         Fetching IOCs from YYYY-MM-DDTHH:MM:SS+00:00 to YYYY-MM-DDTHH:MM:SS+00:00
         Page 1: Retrieved X IOCs
         Wrote X records to gs://bucket-name/mandiant-ioc/iocs_YYYYMMDD_HHMMSS.ndjson
         Successfully processed X records
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click on your bucket name (for example, `mandiant-ioc-logs`).

  10. Navigate to the prefix folder (for example, `mandiant-ioc/`).

  11. Verify that a new `.ndjson` file was created with the current timestamp.




If you see errors in the logs:

  * **HTTP 401** : Check API Key ID and Secret in environment variables
  * **HTTP 403** : Verify account has Threat Intelligence permissions
  * **HTTP 429** : Rate limiting - function will automatically retry with backoff
  * **Missing environment variables** : Check all required variables are set
  * **Token request failed** : Verify API credentials are correct and not expired



## Retrieve the Google SecOps service account

Google SecOps uses a unique service account to read data from your GCS bucket. You must grant this service account access to your bucket.

### Get the service account email

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Mandiant Custom IOC`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Mandiant Custom IOC** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Don't use service accounts from other documentation or examples.
  9. Click **Next**.

  10. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://mandiant-ioc-logs/mandiant-ioc/
           

       * Replace: 
         * `mandiant-ioc-logs`: Your GCS bucket name.
         * `mandiant-ioc`: Prefix/folder path where IOC logs are stored.
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
  2. Click on your bucket name (for example, `mandiant-ioc-logs`).
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
associated_hashes.value | entity.file.md5 | Value from associated_hashes.value if hash.type == "md5", else from value if type == "md5"  
value | entity.file.md5 |   
associated_hashes.value | entity.file.sha1 | Value from associated_hashes.value if hash.type == "sha1", else from value if type == "sha1"  
value | entity.file.sha1 |   
associated_hashes.value | entity.file.sha256 | Value from associated_hashes.value if hash.type == "sha256", else from value if type == "sha256"  
value | entity.file.sha256 |   
value | entity.hostname | Value copied directly if type == "fqdn"  
value | entity.ip | Value copied directly if type == "ipv4"  
threat_rating.threat_score | entity.labels | Merged label objects with key "threat_score" and value from threat_rating.threat_score, key "mscore" and value from mscore, key "is_exclusive" and value from is_exclusive, key "is_publishable" and value from is _publishable, and for each misp field, key "misp_ " and value from misp.  
mscore | entity.labels |   
is_exclusive | entity.labels |   
is_publishable | entity.labels |   
misp.akamai | entity.labels |   
misp.alexa | entity.labels |   
misp.alexa_1M | entity.labels |   
misp.amazon-aws | entity.labels |   
misp.apple | entity.labels |   
misp.automated-malware-analysis | entity.labels |   
misp.bank-website | entity.labels |   
misp.captive-portals | entity.labels |   
misp.censys-scanning | entity.labels |   
misp.cisco_1M | entity.labels |   
misp.cisco_top1000 | entity.labels |   
misp.cisco_top10k | entity.labels |   
misp.cisco_top20k | entity.labels |   
misp.cisco_top5k | entity.labels |   
misp.cloudflare | entity.labels |   
misp.common-contact-emails | entity.labels |   
misp.common-ioc-false-positive | entity.labels |   
misp.covid | entity.labels |   
misp.covid-19-cyber-threat-coalition-whitelist | entity.labels |   
misp.covid-19-krassi-whitelist | entity.labels |   
misp.crl-hostname | entity.labels |   
misp.crl-ip | entity.labels |   
misp.dax30 | entity.labels |   
misp.digitalside | entity.labels |   
misp.disposable-email | entity.labels |   
misp.dynamic-dns | entity.labels |   
misp.eicar.com | entity.labels |   
misp.empty-hashes | entity.labels |   
misp.fastly | entity.labels |   
misp.findip-host | entity.labels |   
misp.google | entity.labels |   
misp.google-chrome-crux-1million | entity.labels |   
misp.google-gcp | entity.labels |   
misp.google-gmail-sending-ips | entity.labels |   
misp.googlebot | entity.labels |   
misp.ipv6-linklocal | entity.labels |   
misp.majestic_million | entity.labels |   
misp.majestic_million_1M | entity.labels |   
misp.microsoft | entity.labels |   
misp.microsoft-attack-simulator | entity.labels |   
misp.microsoft-azure | entity.labels |   
misp.microsoft-azure-appid | entity.labels |   
misp.microsoft-azure-china | entity.labels |   
misp.microsoft-azure-germany | entity.labels |   
misp.microsoft-azure-us-gov | entity.labels |   
misp.microsoft-office365 | entity.labels |   
misp.microsoft-office365-cn | entity.labels |   
misp.microsoft-office365-ip | entity.labels |   
misp.microsoft-win10-connection-endpoints | entity.labels |   
misp.moz-top500 | entity.labels |   
misp.mozilla-CA | entity.labels |   
misp.mozilla-IntermediateCA | entity.labels |   
misp.multicast | entity.labels |   
misp.nioc-filehash | entity.labels |   
misp.openai-gptbot | entity.labels |   
misp.ovh-cluster | entity.labels |   
misp.parking-domain | entity.labels |   
misp.parking-domain-ns | entity.labels |   
misp.phone_numbers | entity.labels |   
misp.public-dns-hostname | entity.labels |   
misp.public-dns-v4 | entity.labels |   
misp.public-dns-v6 | entity.labels |   
misp.public-ipfs-gateways | entity.labels |   
misp.rfc1918 | entity.labels |   
misp.rfc3849 | entity.labels |   
misp.rfc5735 | entity.labels |   
misp.rfc6598 | entity.labels |   
misp.rfc6761 | entity.labels |   
misp.second-level-tlds | entity.labels |   
misp.security-provider-blogpost | entity.labels |   
misp.sinkholes | entity.labels |   
misp.smtp-receiving-ips | entity.labels |   
misp.smtp-sending-ips | entity.labels |   
misp.stackpath | entity.labels |   
misp.tenable-cloud-ipv4 | entity.labels |   
misp.tenable-cloud-ipv6 | entity.labels |   
misp.ti-falsepositives | entity.labels |   
misp.tlds | entity.labels |   
misp.tranco | entity.labels |   
misp.tranco10k | entity.labels |   
misp.umbrella-blockpage-hostname | entity.labels |   
misp.umbrella-blockpage-v4 | entity.labels |   
misp.umbrella-blockpage-v6 | entity.labels |   
misp.university_domains | entity.labels |   
misp.url-shortener | entity.labels |   
misp.vpn-ipv4 | entity.labels |   
misp.vpn-ipv6 | entity.labels |   
misp.whats-my-ip | entity.labels |   
misp.wikimedia | entity.labels |   
misp.zscaler | entity.labels |   
value | entity.url | Value copied directly if type == "url"  
last_seen | event.ioc.active_timerange.end | Date parsed from last_seen using ISO8601  
first_seen | event.ioc.active_timerange.start | Date parsed from first_seen using ISO8601  
sources.0.category | event.ioc.categorization | Joined from sources.0.category array with comma separator  
threat_rating.threat_score | event.ioc.confidence_score | Value copied directly  
value | event.ioc.domain_and_ports.domain | Value copied directly if type == "fqdn"  
event.ioc.feed_name | event.ioc.feed_name | Set to "Mandiant"  
value | event.ioc.ip_and_ports.ip_address | Converted to ipaddress if type == "ipv4"  
type | metadata.entity_type | Set to FILE if associated_hashes.type in md5 sha1 sha256, else DOMAIN_NAME if type == "fqdn", IP_ADDRESS if type == "ipv4", URL if type == "url", FILE if type in md5 sha1 sha256, UNKNOWN_ENTITYTYPE else  
associated_hashes.type | metadata.entity_type |   
custom_ioc_expire_date | metadata.interval.end_time | Date parsed from custom_ioc_expire_date using ISO8601 if type in fqdn ipv4 url  
first_seen | metadata.interval.start_time | Date parsed from first_seen using ISO8601 or UNIX  
id | metadata.product_entity_id | Value copied directly  
threat_det | metadata.threat | Merged from threat_det  
attributed_associations | threat_det.associations | Merged threat_association objects from attributed_associations and associations, with fields set from association.id, name, type, region_code.country_or_region, associated_actors, alias, role, first_reference_time, last_reference_time, industries_affected  
associations | threat_det.associations |   
campaigns | threat_det.campaigns | Merged campaign.name from campaigns array  
category | threat_det.category_details | Merged from category array  
threat_rating.confidence_level | threat_det.confidence | Set to LOW_CONFIDENCE if matches low, MEDIUM_CONFIDENCE if medium, HIGH_CONFIDENCE if high, else UNKNOWN_CONFIDENCE  
threat_rating.confidence_score | threat_det.confidence_details | Value from threat_rating.confidence_score converted to string, or from mscore if threat_rating.confidence_score empty  
mscore | threat_det.confidence_details |   
first_seen | threat_det.first_discovered_time | Date from first_seen if not empty, else from firstSeen, using ISO8601 or UNIX  
firstSeen | threat_det.first_discovered_time |   
first_seen | threat_det.last_updated_time | Date parsed from first_seen using ISO8601 or UNIX  
threat_rating.threat_score | threat_det.risk_score | Converted to float from threat_rating.threat_score if not empty, else from mscore  
mscore | threat_det.risk_score |   
threat_rating.severity_level | threat_det.severity | Set to LOW if low, MEDIUM if medium, HIGH if high, else UNKNOWN_SEVERITY  
threat_det.threat_feed_name | threat_det.threat_feed_name | Set to "Mandiant"  
value | threat_det.url_back_to_product | Set to "https://advantage.mandiant.com/search?query=%{value}" if type in fqdn ipv4 url md5  
verdict_simple.timestamp | threat_det.verdict_info | Merged from verdict_info_simple after setting verdict_time from timestamp, verdict_response from verdict if malicious, verdict_type from verdict_source  
verdict_simple.verdict | threat_det.verdict_info |   
verdict_simple.verdict_source | threat_det.verdict_info |   
metadata.product_name | metadata.product_name | Set to "MANDIANT_CUSTOM_IOC"  
metadata.vendor_name | metadata.vendor_name | Set to "MANDIANT_CUSTOM_IOC"  
`threat.threat_feed_name` | `Mandiant` | Mapped from changelog  
`threat_rating.threat_score` | `entity.entity.labels` | Mapped from changelog  
`threat_rating.severity_level` | `threat.severity` | Mapped from changelog  
`threat_rating.confidence_level` | `threat.confidence` | Mapped from changelog  
`verdict_simple.timestamp` | `verdict_info.verdict_time` | Mapped from changelog  
`category` | `threat.category_details` | Mapped from changelog  
`threat_rating.confidence_score` | `threat.confidence_details` | Mapped from changelog  
`threat_rating.threat_score` | `threat.risk_score` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/mandiant-custom-ioc-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
