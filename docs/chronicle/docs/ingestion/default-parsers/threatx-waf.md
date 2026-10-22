---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/threatx-waf/
title: Collect ThreatX WAF logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:58:19.068026+00:00
---

# Collect ThreatX WAF logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/threatx-waf/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect ThreatX WAF logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest ThreatX WAF logs to Google Security Operations using Google Cloud Storage V2.

ThreatX WAF is an API and web application firewall that provides behavioral threat detection and bot protection. It monitors and analyzes traffic patterns to identify and block malicious requests targeting web applications and APIs. The ThreatX REST API provides programmatic access to event and entity logs.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * Privileged access to the ThreatX console with administrator permissions
  * A ThreatX API key and customer name



## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `threatx-waf-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Collect ThreatX WAF API credentials

### Obtain API key

  1. Sign in to the [ThreatX](https://app.threatx.com/) console as an administrator.
  2. Go to **Settings > API Keys**.
  3. Click **Generate API Key**.
  4. Enter a name for the API key (for example, `Google SecOps Integration`).
  5. Copy and save the following details in a secure location:

     * **API Key** : The generated API key value
     * **Customer Name** : Your ThreatX customer name (visible in the console URL or Settings page)
**Note:** The API key must have permissions to access event and entity endpoints. Contact ThreatX support if API access is not enabled for your account.



### Determine API base URL

The ThreatX API base URL:

Environment | API Base URL  
---|---  
Production | `https://provision.threatx.io/tx/api/v2`  
  
### Test API access

  * Test your credentials before proceeding with the integration:
        
        # Replace with your actual credentials
        THREATX_API_KEY="your-api-key"
        THREATX_CUSTOMER="your-customer-name"
        
        # Test API access - list entities
        curl -s -X POST "https://provision.threatx.io/tx/api/v2/entities/list" \
          -H "Content-Type: application/json" \
          -d "{\"api_key\": \"${THREATX_API_KEY}\", \"customer_name\": \"${THREATX_CUSTOMER}\", \"command\": {\"limit\": 1}}"
        




## Create service account for Cloud Run function

The Cloud Run function needs a service account with permissions to write to GCS bucket and be invoked by Pub/Sub.

### Create service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `threatx-waf-logs-collector-sa`
     * **Service account description** : Enter `Service account for Cloud Run function to collect ThreatX WAF logs`
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
  2. Click on your bucket name (for example, `threatx-waf-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `threatx-waf-logs-collector-sa@PROJECT_ID.iam.gserviceaccount.com`)
     * **Assign roles** : Select **Storage Object Admin**
  6. Click **Save**.



## Create Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `threatx-waf-logs-trigger`
     * Leave other settings as default
  4. Click **Create**.



## Create Cloud Run function to collect logs

  * The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from the ThreatX REST API and write them to GCS.


  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `threatx-waf-logs-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose the topic `threatx-waf-logs-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select the service account `threatx-waf-logs-collector-sa`.
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `threatx-waf-logs` | GCS bucket name  
`GCS_PREFIX` | `threatx` | Prefix for log files  
`STATE_KEY` | `threatx/state.json` | State file path  
`THREATX_API_KEY` | `your-api-key` | ThreatX API key  
`THREATX_CUSTOMER` | `your-customer-name` | ThreatX customer name  
`THREATX_API_BASE` | `https://provision.threatx.io/tx/api/v2` | ThreatX API base URL  
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

     * First file **main.py:**
    
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
    GCS_PREFIX = os.environ.get('GCS_PREFIX', 'threatx')
    STATE_KEY = os.environ.get('STATE_KEY', 'threatx/state.json')
    THREATX_API_KEY = os.environ.get('THREATX_API_KEY')
    THREATX_CUSTOMER = os.environ.get('THREATX_CUSTOMER')
    THREATX_API_BASE = os.environ.get('THREATX_API_BASE', 'https://provision.threatx.io/tx/api/v2')
    MAX_RECORDS = int(os.environ.get('MAX_RECORDS', '5000'))
    PAGE_SIZE = int(os.environ.get('PAGE_SIZE', '1000'))
    LOOKBACK_HOURS = int(os.environ.get('LOOKBACK_HOURS', '24'))
    
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
    
    @functions_framework.cloud_event
    def main(cloud_event):
        """
        Cloud Run function triggered by Pub/Sub to fetch ThreatX WAF
        event logs and write to GCS.
    
        Args:
            cloud_event: CloudEvent object containing Pub/Sub message
        """
    
        if not all([GCS_BUCKET, THREATX_API_KEY, THREATX_CUSTOMER]):
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
    
            # Fetch logs
            records, newest_event_time = fetch_logs(
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
    
    def fetch_logs(start_time: datetime, end_time: datetime, page_size: int, max_records: int):
        """
        Fetch event logs from ThreatX REST API
        with pagination and rate limiting.
    
        Args:
            start_time: Start time for log query
            end_time: End time for log query
            page_size: Number of records per page
            max_records: Maximum total records to fetch
    
        Returns:
            Tuple of (records list, newest_event_time ISO string)
        """
        api_base = THREATX_API_BASE.rstrip('/')
        endpoint = f"{api_base}/logs/list"
    
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'User-Agent': 'GoogleSecOps-ThreatXCollector/1.0'
        }
    
        records = []
        newest_time = None
        page_num = 0
        offset = 0
        backoff = 1.0
    
        start_epoch = int(start_time.timestamp())
        end_epoch = int(end_time.timestamp())
    
        while True:
            page_num += 1
    
            if len(records) >= max_records:
                print(f"Reached max_records limit ({max_records})")
                break
    
            body = json.dumps({
                'api_key': THREATX_API_KEY,
                'customer_name': THREATX_CUSTOMER,
                'command': {
                    'from': start_epoch,
                    'to': end_epoch,
                    'limit': min(page_size, max_records - len(records)),
                    'offset': offset
                }
            })
    
            try:
                response = http.request('POST', endpoint, body=body, headers=headers)
    
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
    
                page_results = data.get('Ok', {}).get('logs', data.get('Ok', []))
                if isinstance(page_results, dict):
                    page_results = page_results.get('data', [])
    
                if not page_results:
                    print(f"No more results (empty page)")
                    break
    
                print(f"Page {page_num}: Retrieved {len(page_results)} events")
                records.extend(page_results)
    
                # Track newest event time
                for event in page_results:
                    try:
                        event_ts = event.get('timestamp') or event.get('time')
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
                if len(page_results) < page_size:
                    print("No more pages (last page not full)")
                    break
    
                offset += len(page_results)
    
            except Exception as e:
                print(f"Error fetching logs: {e}")
                return [], None
    
        print(f"Retrieved {len(records)} total records from {page_num} pages")
        return records, newest_time
    

     * Second file **requirements.txt:**
    
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
**Name** | `threatx-waf-logs-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the topic `threatx-waf-logs-trigger`  
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
  5. Click on `threatx-waf-logs-collector`.
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         Fetching logs from YYYY-MM-DDTHH:MM:SS+00:00 to YYYY-MM-DDTHH:MM:SS+00:00
         Page 1: Retrieved X events
         Wrote X records to gs://threatx-waf-logs/threatx/logs_YYYYMMDD_HHMMSS.ndjson
         Successfully processed X records
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click on your bucket name (`threatx-waf-logs`).

  10. Navigate to the `threatx/` folder.

  11. Verify that a new `.ndjson` file was created with the current timestamp.




If you see errors in the logs:

  * **HTTP 401** : Check API key and customer name in environment variables
  * **HTTP 403** : Verify API key has required permissions in ThreatX console
  * **HTTP 429** : Rate limiting - function will automatically retry with backoff
  * **Missing environment variables** : Check all required variables are set



## Configure a feed in Google SecOps to ingest ThreatX WAF logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `ThreatX WAF Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **ThreatX WAF** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address.

**Note:** Each Google SecOps instance has a unique service account. Do not use service accounts from other documentation or examples.
  9. Click **Next**.

  10. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://threatx-waf-logs/threatx/
           

       * Replace: 
         * `threatx-waf-logs`: Your GCS bucket name.
         * `threatx`: Optional prefix/folder path where logs are stored (leave empty for root).
**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never** : Never deletes any files after transfers (recommended for testing).
       * **Delete transferred files** : Deletes files after successful transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.

**Note:** If you select a deletion option, the service account must have **Storage Object Admin** role instead of **Storage Object Viewer**. Update IAM permissions accordingly.
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

**Note:** If you plan to use the deletion option "Delete transferred files" or "Delete transferred files and empty directories," grant **Storage Object Admin** role instead of **Storage Object Viewer**.

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
action | additional.fields.action_label | Additional vendor-specific event data  
args | additional.fields.args_label | Additional vendor-specific event data  
content_length | additional.fields.content_length_label | Additional vendor-specific event data  
content_type | additional.fields.content_type_label | Additional vendor-specific event data  
cookie | additional.fields.cookie_label | Additional vendor-specific event data  
count | additional.fields.count_label | Additional vendor-specific event data  
entity.codename | additional.fields.entity_codename_label | Additional vendor-specific event data  
entity.hash | additional.fields.entity_hash_label | Additional vendor-specific event data  
facility | additional.fields.facility_label | Additional vendor-specific event data  
js_fingerprint | additional.fields.js_fingerprint_label | Additional vendor-specific event data  
msg_type | additional.fields.msg_type_label | Additional vendor-specific event data  
new_value | additional.fields.new_value_label | Additional vendor-specific event data  
old_value | additional.fields.old_value_label | Additional vendor-specific event data  
postblock_event | additional.fields.postblock_event_label | Additional vendor-specific event data  
random_id | additional.fields.random_id_label | Additional vendor-specific event data  
response_length | additional.fields.response_length_label | Additional vendor-specific event data  
ssl | additional.fields.ssl_label | Additional vendor-specific event data  
tenant_name | additional.fields.tenant_name_label | Additional vendor-specific event data  
tls_fingerprint | additional.fields.tls_fingerprint_label | Additional vendor-specific event data  
upstream_response_time | additional.fields.upstream_response_time_label | Additional vendor-specific event data  
version | additional.fields.version_label | Additional vendor-specific event data  
data.classification, rule.classification | security_result.detection_fields.classification_label, security_result.detection_fields.rule_classification_label | Security classification or action  
data.contrib_score, rule.contrib_score | security_result.detection_fields.contrib_score_label, security_result.detection_fields.rule_contrib_score_label | Security classification or action  
data.description, rule.description | security_result.detection_fields.description_label, security_result.detection_fields.rule_description_label | Security classification or action  
data.id, rule.id | security_result.detection_fields.id_label, security_result.detection_fields.rule_id_label | Security classification or action  
data.risk, rule.beta | security_result.detection_fields.risk_label, security_result.detection_fields.rule_beta_label | Security classification or action  
data.state, rule.state | security_result.detection_fields.state_label, security_result.detection_fields.rule_state_label | Security classification or action  
data.contrib_score | security_result.detection_fields.contrib _score_ %{index}_label | Security classification or action  
data.description | security_result.detection _fields.description_ %{index}_label | Security classification or action  
data.classification | security_result.detection _fields.classification_ %{index}_label | Security classification or action  
data.id | security_result.detection _fields.id_ %{index}_label | Security classification or action  
data.risk | security_result.detection _fields.risk_ %{index}_label | Security classification or action  
data.state | security_result.detection _fields.state_ %{index}_label | Security classification or action  
rule.blocking | security_result.detection_fields.rule_blocking_label | Security classification or action  
| metadata.description | Description of the event  
| metadata.event_type | Type of event (e.g., USER_LOGIN, NETWORK_CONNECTION)  
msg_id | metadata.product_log_id | Unique identifier for the log entry  
| metadata.product_name | Product name  
| metadata.vendor_name | Vendor/company name  
network.http.method | network.http.method | HTTP method used in the request  
status_code | network.http.response_code | HTTP response code  
user_agent | network.http.parsed_user_agent, network.http.user_agent | Parsed user agent string  
entity.ip_address, ip | principal.asset.ip, principal.ip | Source IP address of the connection  
hostname | principal.asset.hostname, principal.hostname | Source hostname  
user_email | principal.email | Email address of the user  
msg1 | principal.url | URL associated with the principal  
user_id | principal.user.userid | Unique identifier for the user  
request_id | target.resource.attribute.labels.request_id_label | Resource attributes  
subscription_id | target.resource.attribute.labels.subscription_ID_label | Resource attributes  
uri | target.resource.attribute.labels.uri_label | Resource attributes  
dst_domain, dst_host, username | target.asset.hostname, target.hostname | Destination hostname  
action | security_result.action | Action taken by the security product  
category | security_result.category_details | Security category details  
priority | security_result.priority | Priority level of the security event  
risk | security_result.risk_score | Risk score assigned to the event  
severity | security_result.severity | Severity level of the security event  
`rule.id", "rule.description", "rule.classification", "rule.state", "rule.contrib_score", "rule.beta", and "rule.blocking` | `security_result.detection_fields` | Mapped from changelog  
`action", "tenant_name", "random_id", "cookie", "js_fingerprint", "content_type", "postblock_event", "ssl", "content_length", "count", "upstream_response_time", "upstream_response_time", and "response_length` | `additional.fields` | Mapped from changelog  
`old_value" and "new_value` | `additional.fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/threatx-waf-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
