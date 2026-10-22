---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zerofox-platform/
title: Collect ZeroFox platform logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:55:45.617216+00:00
---

# Collect ZeroFox platform logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zerofox-platform/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect ZeroFox platform logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest ZeroFox Platform logs to Google Security Operations using Google Cloud Storage. ZeroFox Platform provides digital risk protection by monitoring and analyzing threats across social media, mobile apps, cloud, email, and other digital channels.

## Before you begin

Ensure that you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * Privileged access to ZeroFox Platform tenant



## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `zerofox-platform-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Collect ZeroFox Platform credentials

### Get ZeroFox personal access token

  1. Sign in to the ZeroFox Platform at <https://cloud.zerofox.com>.
  2. Go to **Settings > Data Connections > API Data Feeds**. 
     * Direct URL (after login): <https://cloud.zerofox.com/data_connectors/api>
     * Note: If you don't see this menu item, contact your ZeroFox administrator for access. The menu may also be labeled **Data Connectors > API Data Feeds** depending on your tenant UI version.
  3. Click **Generate Token** or **Create Personal Access Token**.
  4. Provide the following configuration details: 
     * **Name** : Enter a descriptive name (for example, `Google SecOps GCS Ingestion`).
     * **Expiration** : Select a rotation period according to your organization's security policy.
     * **Permissions/Feeds** : Select read permissions for: 
       * **Alerts**
       * **CTI feeds**
       * Other data types you want to export
  5. Click **Generate**.
  6. Copy and save the generated Personal Access Token in a secure location (you won't be able to view it again).
  7. Save the **ZEROFOX_BASE_URL** : `https://api.zerofox.com` (default for most tenants).

**Note:** If your tenant uses a different base URL, verify this with your ZeroFox administrator or check your tenant's API documentation.



### Verify permissions

To verify the account has the required permissions:

  1. Sign in to ZeroFox Platform.
  2. Go to **Settings** (⚙️) > **Data Connections > API Data Feeds**.
  3. If you can see the **API Data Feeds** section and generate tokens, you have the required permissions.
  4. If you cannot see this option, contact your administrator to grant API access permissions.



### Test API access

  * Test your credentials before proceeding with the integration:
        
        # Replace with your actual credentials
        ZEROFOX_API_TOKEN="your-personal-access-token"
        ZEROFOX_BASE_URL="https://api.zerofox.com"
        
        # Test API access (example endpoint - adjust based on your data type)
        curl -v -H "Authorization: Bearer $ZEROFOX_API_TOKEN" \
          -H "Accept: application/json" \
          "$ZEROFOX_BASE_URL/v1/alerts?limit=1"
        

**Note:** The exact endpoint path may vary depending on your ZeroFox tenant configuration. If the default `/v1/alerts` endpoint does not work, consult your ZeroFox API documentation or contact ZeroFox support for the correct endpoint URL. You may need to set a custom `URL_TEMPLATE` environment variable in the Cloud Run function.



## Create service account for Cloud Run function

The Cloud Run function needs a service account with permissions to write to GCS bucket and be invoked by Pub/Sub.

### Create service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `zerofox-logs-collector-sa`.
     * **Service account description** : Enter `Service account for Cloud Run function to collect ZeroFox Platform logs`.
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

Grant the service account (`zerofox-logs-collector-sa`) write permissions on the GCS bucket:

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name (for example, `zerofox-platform-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `zerofox-logs-collector-sa@PROJECT_ID.iam.gserviceaccount.com`).
     * **Assign roles** : Select **Storage Object Admin**.
  6. Click **Save**.



## Create Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `zerofox-logs-trigger`.
     * Leave other settings as default.
  4. Click **Create**.



## Create Cloud Run function to collect logs

The Cloud Run function is triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from ZeroFox Platform API and writes them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `zerofox-logs-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose the Pub/Sub topic (`zerofox-logs-trigger`).
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub automatically handles authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select the service account (`zerofox-logs-collector-sa`).
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `zerofox-platform-logs` | GCS bucket name  
`GCS_PREFIX` | `zerofox/platform` | Prefix for log files  
`STATE_KEY` | `zerofox/platform/state.json` | State file path  
`ZEROFOX_BASE_URL` | `https://api.zerofox.com` | API base URL  
`ZEROFOX_API_TOKEN` | `your-zerofox-personal-access-token` | Personal access token  
`LOOKBACK_HOURS` | `24` | Initial lookback period  
`PAGE_SIZE` | `200` | Records per page  
`MAX_PAGES` | `20` | Maximum pages per run  
`HTTP_TIMEOUT` | `60` | HTTP request timeout in seconds  
`HTTP_RETRIES` | `3` | Number of HTTP retries  
`URL_TEMPLATE` | (optional) | Custom URL template with `{SINCE}`, `{PAGE_TOKEN}`, `{PAGE_SIZE}`  
**Note:** The `URL_TEMPLATE` variable is optional. If not set, the function will use the default alerts endpoint (`/v1/alerts`). If your tenant uses a different endpoint structure, set this variable to match your ZeroFox API documentation. Example: `https://api.zerofox.com/v1/alerts?since={SINCE}&limit={PAGE_SIZE}&page_token={PAGE_TOKEN}`
  10. In the **Variables & Secrets** section, scroll down to **Requests** :

     * **Request timeout** : Enter `600` seconds (10 minutes).
  11. Go to the **Settings** tab:

     * In the **Resources** section: 
       * **Memory** : Select **512 MiB** or higher.
       * **CPU** : Select **1**.
  12. In the **Revision scaling** section:

     * **Minimum number of instances** : Enter `0`.
     * **Maximum number of instances** : Enter `100` (or adjust based on expected load).
  13. Click **Create**.

  14. Wait for the service to be created (1-2 minutes).

  15. After the service is created, the **inline code editor** opens automatically.




### Add function code

  1. Enter **main** in **Function entry point**
  2. In the inline code editor, create two files:

     * First file: **main.py:**
    
    import functions_framework
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    import json
    import os
    import urllib3
    from datetime import datetime, timezone, timedelta
    import time
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
    GCS_PREFIX = os.environ.get('GCS_PREFIX', 'zerofox/platform')
    STATE_KEY = os.environ.get('STATE_KEY', 'zerofox/platform/state.json')
    ZEROFOX_BASE_URL = os.environ.get('ZEROFOX_BASE_URL', 'https://api.zerofox.com')
    ZEROFOX_API_TOKEN = os.environ.get('ZEROFOX_API_TOKEN')
    LOOKBACK_HOURS = int(os.environ.get('LOOKBACK_HOURS', '24'))
    PAGE_SIZE = int(os.environ.get('PAGE_SIZE', '200'))
    MAX_PAGES = int(os.environ.get('MAX_PAGES', '20'))
    HTTP_TIMEOUT = int(os.environ.get('HTTP_TIMEOUT', '60'))
    HTTP_RETRIES = int(os.environ.get('HTTP_RETRIES', '3'))
    URL_TEMPLATE = os.environ.get('URL_TEMPLATE', '')
    
    def parse_datetime(value: str) -> datetime:
        """Parse ISO datetime string to datetime object."""
        if [value](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.ObjectCustomContextPayload.html#google_cloud_storage_blob_ObjectCustomContextPayload_value).endswith("Z"):
            value = value[:-1] + "+00:00"
        return datetime.fromisoformat(value)
    
    @functions_framework.cloud_event
    def main(cloud_event):
        """
        Cloud Run function triggered by Pub/Sub to fetch ZeroFox Platform logs and write to GCS.
    
        Args:
            cloud_event: CloudEvent object containing Pub/Sub message
        """
    
        if not all([GCS_BUCKET, ZEROFOX_BASE_URL, ZEROFOX_API_TOKEN]):
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
    
            if isinstance(state, dict) and [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get("last_since"):
                try:
                    last_time = parse_datetime(state["last_since"])
                    # Overlap by 2 minutes to catch any delayed events
                    last_time = last_time - timedelta(minutes=2)
                except Exception as e:
                    print(f"Warning: Could not parse last_since: {e}")
    
            if last_time is None:
                last_time = now - timedelta(hours=LOOKBACK_HOURS)
    
            since_iso = last_time.strftime('%Y-%m-%dT%H:%M:%SZ')
            print(f"Fetching logs since {since_iso}")
    
            # Fetch logs
            records, newest_since = fetch_logs(
                api_base=ZEROFOX_BASE_URL,
                api_token=ZEROFOX_API_TOKEN,
                since=since_iso,
                page_size=PAGE_SIZE,
                max_pages=MAX_PAGES,
            )
    
            if not records:
                print("No new log records found.")
                save_state(bucket, STATE_KEY, since_iso)
                return
    
            # Write to GCS as NDJSON
            timestamp = now.strftime('%Y%m%d_%H%M%S')
            object_key = f"{GCS_PREFIX}/logs_{timestamp}.ndjson"
            blob = bucket.blob(object_key)
    
            ndjson = '\n'.join([json.dumps(record, ensure_ascii=False) for record in records]) + '\n'
            blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(ndjson, content_type='application/x-ndjson')
    
            print(f"Wrote {len(records)} records to gs://{GCS_BUCKET}/{object_key}")
    
            # Update state with newest timestamp
            if newest_since:
                save_state(bucket, STATE_KEY, newest_since)
            else:
                save_state(bucket, STATE_KEY, since_iso)
    
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
    
    def save_state(bucket, key, last_since: str):
        """Save the last since timestamp to GCS state file."""
        try:
            state = {'last_since': last_since}
            blob = bucket.blob(key)
            blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
                json.dumps(state, indent=2),
                content_type='application/json'
            )
            print(f"Saved state: last_since={last_since}")
        except Exception as e:
            print(f"Warning: Could not save state: {e}")
    
    def fetch_logs(api_base: str, api_token: str, since: str, page_size: int, max_pages: int):
        """
        Fetch logs from ZeroFox Platform API with pagination and rate limiting.
    
        Args:
            api_base: API base URL
            api_token: Personal access token
            since: ISO timestamp for filtering logs
            page_size: Number of records per page
            max_pages: Maximum pages to fetch
    
        Returns:
            Tuple of (records list, newest_since ISO string)
        """
        # Use URL_TEMPLATE if provided, otherwise construct default alerts endpoint
        if URL_TEMPLATE:
            base_url = URL_TEMPLATE.replace("{SINCE}", urllib.parse.quote(since))
        else:
            base_url = f"{api_base}/v1/alerts?since={urllib.parse.quote(since)}"
    
        headers = {
            'Authorization': f'Bearer {api_token}',
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'User-Agent': 'GoogleSecOps-ZeroFoxCollector/1.0'
        }
    
        records = []
        newest_since = since
        page_num = 0
        page_token = ""
        backoff = 1.0
    
        while page_num < max_pages:
            page_num += 1
    
            # Construct URL with pagination
            if URL_TEMPLATE:
                url = (base_url
                       .replace("{PAGE_TOKEN}", urllib.parse.quote(page_token))
                       .replace("{PAGE_SIZE}", str(page_size)))
            else:
                url = f"{base_url}&limit={page_size}"
                if page_token:
                    url += f"&page_token={urllib.parse.quote(page_token)}"
    
            attempt = 0
            while attempt <= HTTP_RETRIES:
                try:
                    response = http.request('GET', url, headers=headers, timeout=HTTP_TIMEOUT)
    
                    # Handle rate limiting with exponential backoff
                    if response.status == 429:
                        retry_after = int(response.headers.get('Retry-After', str(int(backoff))))
                        print(f"Rate limited (429). Retrying after {retry_after}s...")
                        time.sleep(retry_after)
                        backoff = min(backoff * 2, 30.0)
                        attempt += 1
                        continue
    
                    backoff = 1.0
    
                    if response.status != 200:
                        print(f"HTTP Error: {response.status}")
                        response_text = response.data.decode('utf-8')
                        print(f"Response body: {response_text}")
                        return records, newest_since
    
                    data = json.loads(response.data.decode('utf-8'))
    
                    # Extract results (try multiple possible keys)
                    page_results = []
                    for key in ('results', 'data', 'alerts', 'items', 'logs', 'events'):
                        if isinstance(data.get(key), list):
                            page_results = data[key]
                            break
    
                    if not page_results:
                        print(f"No more results (empty page)")
                        return records, newest_since
    
                    print(f"Page {page_num}: Retrieved {len(page_results)} events")
                    records.extend(page_results)
    
                    # Track newest timestamp
                    for event in page_results:
                        try:
                            # Try multiple possible timestamp fields
                            event_time = (event.get('timestamp') or 
                                        event.get('created_at') or 
                                        event.get('last_modified') or 
                                        event.get('event_time') or 
                                        event.get('log_time') or 
                                        event.get('updated_at'))
                            if event_time and isinstance(event_time, str):
                                if event_time > newest_since:
                                    newest_since = event_time
                        except Exception as e:
                            print(f"Warning: Could not parse event time: {e}")
    
                    # Check for next page token
                    next_token = (data.get('next') or 
                                data.get('next_token') or 
                                data.get('nextPageToken') or 
                                data.get('next_page_token'))
    
                    if isinstance(next_token, dict):
                        next_token = (next_token.get('token') or 
                                    next_token.get('cursor') or 
                                    next_token.get('value'))
    
                    if not next_token:
                        print("No more pages (no next token)")
                        return records, newest_since
    
                    page_token = str(next_token)
                    break
    
                except urllib3.[exceptions](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.exceptions.html).HTTPError as e:
                    if attempt < HTTP_RETRIES:
                        print(f"HTTP error (attempt {attempt + 1}/{HTTP_RETRIES}): {e}")
                        time.sleep(1 + attempt)
                        attempt += 1
                        continue
                    else:
                        print(f"Error fetching logs after {HTTP_RETRIES} retries: {e}")
                        return records, newest_since
                except Exception as e:
                    print(f"Error fetching logs: {e}")
                    return records, newest_since
    
        print(f"Retrieved {len(records)} total records from {page_num} pages")
        return records, newest_since
    

     * Second file: **requirements.txt:**
    
    functions-framework==3.*
    google-cloud-storage==2.*
    urllib3>=2.0.0
    

  3. Click **Deploy** to save and deploy the function.

  4. Wait for deployment to complete (2-3 minutes).

**Note:** The Pub/Sub trigger configuration automatically creates the necessary subscriptions and permissions.



## Create Cloud Scheduler job

Cloud scheduler publishes messages to the Pub/Sub topic (`zerofox-logs-trigger`) at regular intervals, triggering the Cloud Run function.

  1. In the **GCP Console** , go to **Cloud Scheduler**.
  2. Click **Create Job**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | `zerofox-logs-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the Pub/Sub topic (`zerofox-logs-trigger`)  
**Message body** | `{}` (empty JSON object)  
  4. Click **Create**.




### Schedule frequency options

  * Choose frequency based on log volume and latency requirements:

Frequency | Cron Expression | Use Case  
---|---|---  
Every 5 minutes | `*/5 * * * *` | High-volume, low-latency  
Every 15 minutes | `*/15 * * * *` | Medium volume  
Every hour | `0 * * * *` | Standard (recommended)  
Every 6 hours | `0 */6 * * *` | Low volume, batch processing  
Daily | `0 0 * * *` | Historical data collection  



### Test the integration

  1. In the **Cloud Scheduler** console, find your job (`zerofox-logs-collector-hourly`).
  2. Click **Force run** to trigger the job manually.
  3. Wait a few seconds.
  4. Go to **Cloud Run > Services**.
  5. Click your function name (`zerofox-logs-collector`).
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for the following:
         
         Fetching logs since YYYY-MM-DDTHH:MM:SSZ
         Page 1: Retrieved X events
         Wrote X records to gs://zerofox-platform-logs/zerofox/platform/logs_YYYYMMDD_HHMMSS.ndjson
         Successfully processed X records
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click your bucket name (`zerofox-platform-logs`).

  10. Navigate to the prefix folder (`zerofox/platform/`).

  11. Verify that a new `.ndjson` file was created with the current timestamp.




If you see errors in the logs:

  * **HTTP 401** : Check API credentials in environment variables. Verify the `ZEROFOX_API_TOKEN` is correct and has not expired.
  * **HTTP 403** : Verify the ZeroFox account has required permissions for Alerts and CTI feeds. Go to **Settings > Data Connections > API Data Feeds** and check token permissions.
  * **HTTP 404** : The default `/v1/alerts` endpoint may not be correct for your tenant. Set the `URL_TEMPLATE` environment variable to match your ZeroFox API documentation or contact ZeroFox support.
  * **HTTP 429** : Rate limiting - function will automatically retry with exponential backoff.
  * **Missing environment variables** : Check all required variables are set in the Cloud Run function configuration.



## Retrieve the Google SecOps service account

Google SecOps uses a unique service account to read data from your GCS bucket. You must grant this service account access to your bucket.

### Get the service account email

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `ZeroFox Platform Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **ZeroFox Platform** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email is displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Don't use service accounts from other documentation or examples.



## Grant IAM permissions to the Google SecOps service account

The Google SecOps service account needs **Storage Object Viewer** role on your GCS bucket.

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name (`zerofox-platform-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Paste the Google SecOps service account email.
     * **Assign roles** : Select **Storage Object Viewer**.
  6. Click **Save**.

**Note:** If you plan to use the deletion option "Delete transferred files" or "Delete transferred files and empty directories," grant **Storage Object Admin** role instead of Storage Object Viewer.



## Configure a feed in Google SecOps to ingest ZeroFox Platform logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `ZeroFox Platform Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **ZeroFox Platform** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://zerofox-platform-logs/zerofox/platform/
           

       * Replace:

         * `zerofox-platform-logs`: Your GCS bucket name.
         * `zerofox/platform`: Prefix/folder path where logs are stored.
**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never** : Never deletes any files after transfers (recommended for testing).
       * **Delete transferred files** : Deletes files after successful transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.

**Note:** If you select a deletion option, the Google SecOps service account must have **Storage Object Admin** role instead of Storage Object Viewer. Update IAM permissions accordingly.
     * **Maximum File Age** : Include files modified in the last number of days. Default is 180 days.

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).

     * **Ingestion labels** : The label to be applied to the events from this feed.

  9. Click **Next**.

  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
`ai_confidence_display_color_label` | `additional.fields` | Merged  
`ai_confidence_display_icon_label` | `additional.fields` | Merged  
`ai_confidence_display_name_label` | `additional.fields` | Merged  
`arecord_list` | `additional.fields` | Merged  
`browser_label` | `additional.fields` | Merged  
`created_at_label` | `additional.fields` | Merged  
`model_name_label` | `additional.fields` | Merged  
`mx_record_list` | `additional.fields` | Merged  
`ns_record_list` | `additional.fields` | Merged  
`redirect_list` | `additional.fields` | Merged  
`screenshot_label` | `additional.fields` | Merged  
`soa_record_list` | `additional.fields` | Merged  
`tag_list` | `additional.fields` | Merged  
`tier_1_2_label` | `additional.fields` | Merged  
`tier_1_label` | `additional.fields` | Merged  
`tier_2_label` | `additional.fields` | Merged  
`timestamp_modify_tags_label` | `additional.fields` | Merged  
`txt_record_list` | `additional.fields` | Merged  
`whois_label` | `additional.fields` | Merged  
`metadata1` | `metadata` | Renamed/mapped  
`created_at` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`timestamp` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`event_metadata.navigation_metadata.user_agent` | `network.http.user_agent` | Directly mapped  
`event_metadata.unicode_domain_name` | `principal.administrative_domain` | Directly mapped  
`asset.id` | `principal.asset.asset_id` | Directly mapped  
`device_name_label` | `principal.asset.attribute.labels` | Merged  
`ip` | `principal.asset.hostname` | Directly mapped  
`ip` | `principal.asset.ip` | Merged  
`asset.entity_group.name` | `principal.group.group_display_name` | Directly mapped  
`asset.entity_group.id` | `principal.group.product_object_id` | Renamed/mapped  
`asset.name` | `principal.hostname` | Directly mapped  
`host_name` | `principal.hostname` | Directly mapped  
`ip` | `principal.hostname` | Directly mapped  
`ip` | `principal.ip` | Merged  
`os` | `principal.platform` | Mapped: `(?i)Windows` → `WINDOWS`, `(?i)Linux` → `LINUX`, `(?i)Mac` → `MAC`  
`os` | `principal.platform_version` | Directly mapped  
`last_modified_label` | `principal.resource.attribute.labels` | Merged  
`id` | `principal.resource.id` | Directly mapped  
`asset.image` | `principal.url` | Directly mapped  
`perpetrator.display_name` | `principal.user.user_display_name` | Directly mapped  
`perpetrator.id` | `principal.user.userid` | Directly mapped  
`log_sec_res` | `security_result` | Merged  
`alert_type` | `security_result.category_details` | Merged  
`detect.confidence` | `security_result.confidence_score` | Directly mapped  
`index` | `security_result.confidence_score` | Mapped: `0` → `float`  
`alert_reason_label` | `security_result.detection_fields` | Merged  
`detect_confidence_label` | `security_result.detection_fields` | Merged  
`detect_label` | `security_result.detection_fields` | Merged  
`escalated_label` | `security_result.detection_fields` | Merged  
`network_label` | `security_result.detection_fields` | Merged  
`perpetrator_timestamp_label` | `security_result.detection_fields` | Merged  
`reviewed_label` | `security_result.detection_fields` | Merged  
`rule_group_id_label` | `security_result.detection_fields` | Merged  
`sec_status_label` | `security_result.detection_fields` | Merged  
`type_label` | `security_result.detection_fields` | Merged  
`rule_id` | `security_result.rule_id` | Directly mapped  
`rule_name` | `security_result.rule_name` | Directly mapped  
`severity` | `security_result.severity_details` | Directly mapped  
`content` | `security_result.summary` | Directly mapped  
`offending_content_url` | `security_result.url_back_to_product` | Directly mapped  
N/A | `principal.platform` | Constant: `WINDOWS`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/zerofox-platform-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
