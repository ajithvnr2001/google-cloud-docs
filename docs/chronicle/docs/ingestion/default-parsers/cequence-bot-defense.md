---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cequence-bot-defense/
title: Collect Cequence Bot Defense logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:54:15.945439+00:00
---

# Collect Cequence Bot Defense logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cequence-bot-defense/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Cequence Bot Defense logs

**Parser Version:** 2.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Cequence Bot Defense logs to Google Security Operations using Google Cloud Storage V2.

Cequence Bot Defense is an API security and bot management platform that detects and mitigates automated threats targeting web applications and APIs. It generates logs about bot detection events, policy violations, and traffic analysis through the Cequence Unified API Protection (UAP) REST API.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * Privileged access to the Cequence UAP management console with administrator permissions
  * A Cequence API key with access to the Bot Defense events API



## Create a Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `cequence-bot-defense-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Collect Cequence Bot Defense API credentials

### Create an API key

  1. Sign in to the **Cequence UAP management console**.
  2. Navigate to **Settings > API Keys** (or **Administration > API Management**).
  3. Click **Create API Key** or **Generate New Key**.
  4. Enter a name for the API key (for example, `Google Security Operations Integration`).
  5. Assign the required permissions: 
     * **Read** access to Bot Defense events
     * **Read** access to attack data
  6. Copy and save the **API Key** value in a secure location.

**Note:** The API key is displayed only once. If lost, you must generate a new key.



### Determine the API base URL

The Cequence API base URL is tenant-specific:

Format | Example  
---|---  
Tenant URL | `https://your-tenant.cequence.ai/api/v2`  
**Note:** Replace `your-tenant` with your actual Cequence tenant name. Contact your Cequence administrator if you are unsure of your tenant URL.

### Verify API access

  * Test your credentials before proceeding with the integration:
        
        # Replace with your actual credentials
        CEQUENCE_API_KEY="your-api-key"
        CEQUENCE_BASE="https://your-tenant.cequence.ai/api/v2"
        
        curl -s -H "X-API-Key: ${CEQUENCE_API_KEY}" \
            "${CEQUENCE_BASE}/botdefense/events?limit=1" | head -c 500
        




## Create a service account for Cloud Run function

The Cloud Run function needs a service account with permissions to write to GCS bucket and be invoked by Pub/Sub.

### Create service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `cequence-logs-collector-sa`
     * **Service account description** : Enter `Service account for Cloud Run function to collect Cequence Bot Defense logs`
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



### Grant IAM permissions on a GCS bucket

Grant the service account write permissions on the GCS bucket:

  1. Go to **Cloud Storage > Buckets**.
  2. Click on your bucket name (for example, `cequence-bot-defense-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `cequence-logs-collector-sa@PROJECT_ID.iam.gserviceaccount.com`)
     * **Assign roles** : Select **Storage Object Admin**
  6. Click **Save**.



## Create a Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `cequence-logs-trigger`
     * Leave other settings as default
  4. Click **Create**.



## Create a Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from the Cequence UAP REST API and write them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `cequence-logs-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose the topic `cequence-logs-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select the service account `cequence-logs-collector-sa`.
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `cequence-bot-defense-logs` | GCS bucket name  
`GCS_PREFIX` | `cequence` | Prefix for log files  
`STATE_KEY` | `cequence/state.json` | State file path  
`CEQUENCE_API_BASE` | `https://your-tenant.cequence.ai/api/v2` | Cequence API base URL  
`CEQUENCE_API_KEY` | `your-api-key` | Cequence API key  
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

     * First file - **main.py:**
           
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
           GCS_PREFIX = os.environ.get('GCS_PREFIX', 'cequence')
           STATE_KEY = os.environ.get('STATE_KEY', 'cequence/state.json')
           CEQUENCE_API_BASE = os.environ.get('CEQUENCE_API_BASE')
           CEQUENCE_API_KEY = os.environ.get('CEQUENCE_API_KEY')
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
             Cloud Run function triggered by Pub/Sub to fetch Cequence Bot Defense
             event logs and write to GCS.
           
             Args:
               cloud_event: CloudEvent object containing Pub/Sub message
             """
           
             if not all([GCS_BUCKET, CEQUENCE_API_BASE, CEQUENCE_API_KEY]):
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
             Fetch bot defense event logs from Cequence UAP REST API
             with pagination and rate limiting.
           
             Args:
               start_time: Start time for log query
               end_time: End time for log query
               page_size: Number of records per page
               max_records: Maximum total records to fetch
           
             Returns:
               Tuple of (records list, newest_event_time ISO string)
             """
             api_base = CEQUENCE_API_BASE.rstrip('/')
             endpoint = f"{api_base}/botdefense/events"
           
             headers = {
               'X-API-Key': CEQUENCE_API_KEY,
               'Accept': 'application/json',
               'User-Agent': 'GoogleSecOps-CequenceCollector/1.0'
             }
           
             records = []
             newest_time = None
             page_num = 0
             backoff = 1.0
             offset = 0
           
             while True:
               page_num += 1
           
               if len(records) >= max_records:
                 print(f"Reached max_records limit ({max_records})")
                 break
           
               # Build query parameters
               params = {
                 'startTime': start_time.strftime('%Y-%m-%dT%H:%M:%SZ'),
                 'endTime': end_time.strftime('%Y-%m-%dT%H:%M:%SZ'),
                 'limit': min(page_size, max_records - len(records)),
                 'offset': offset
               }
           
               query_string = '&'.join(f"{k}={v}" for k, v in params.items())
               url = f"{endpoint}?{query_string}"
           
               try:
                 response = http.request(
                   'GET',
                   url,
                   headers=headers
                 )
           
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
           
                 page_results = data.get('events', data.get('results', data.get('data', [])))
           
                 if not page_results:
                   print(f"No more results (empty page)")
                   break
           
                 print(f"Page {page_num}: Retrieved {len(page_results)} events")
                 records.extend(page_results)
           
                 # Track newest event time
                 for event in page_results:
                   try:
                     event_ts = event.get('timestamp') or event.get('created') or event.get('eventTime')
                     if event_ts:
                       if isinstance(event_ts, (int, float)):
                         event_dt = datetime.fromtimestamp(event_ts / 1000, tz=timezone.utc)
                         event_time = event_dt.isoformat()
                       else:
                         event_time = str(event_ts)
                       if newest_time is None or parse_datetime(event_time) > parse_datetime(newest_time):
                         newest_time = event_time
                   except Exception as e:
                     print(f"Warning: Could not parse event time: {e}")
           
                 # Check for more results
                 offset += len(page_results)
                 if len(page_results) < page_size:
                   print("No more pages (partial page received)")
                   break
           
               except Exception as e:
                 print(f"Error fetching logs: {e}")
                 return [], None
           
             print(f"Retrieved {len(records)} total records from {page_num} pages")
             return records, newest_time
           

     * Second file - **requirements.txt:**
           
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
**Name** | `cequence-logs-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the topic `cequence-logs-trigger`  
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
  5. Click on `cequence-logs-collector`.
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         Fetching logs from YYYY-MM-DDTHH:MM:SS+00:00 to YYYY-MM-DDTHH:MM:SS+00:00
         Page 1: Retrieved X events
         Wrote X records to gs://cequence-bot-defense-logs/cequence/logs_YYYYMMDD_HHMMSS.ndjson
         Successfully processed X records
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click on your bucket name (`cequence-bot-defense-logs`).

  10. Navigate to the `cequence/` folder.

  11. Verify that a new `.ndjson` file was created with the current timestamp.




If you see errors in the logs:

  * **HTTP 401** : Check API key in environment variables
  * **HTTP 403** : Verify API key has required permissions in Cequence UAP console
  * **HTTP 429** : Rate limiting - function will automatically retry with backoff
  * **Missing environment variables** : Check all required variables are set



## Configure a feed in Google SecOps to ingest Cequence Bot Defense logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Cequence Bot Defense Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Cequence Bot Defense** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address.

**Note:** Each Google SecOps instance has a unique service account. Do not use service accounts from other documentation or examples.
  9. Click **Next**.

  10. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://cequence-bot-defense-logs/cequence/
           

       * Replace: 
         * `cequence-bot-defense-logs`: Your GCS bucket name.
         * `cequence`: Optional prefix/folder path where logs are stored (leave empty for root).
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
tag_label, additiondata fields | additional.fields | Merged from tag_label and key-value pairs from additiondata fields  
timestamp | metadata.event_timestamp | Parsed as timestamp using ISO8601 or yyyy-MM-ddTHH:mm:ss.SSS format  
| metadata.event_type | Set to "GENERIC_EVENT", then to "NETWORK_CONNECTION" if principal_present, target_present, and http_present are true, else to "STATUS_UPDATE" if principal_present is true  
x-forwarded-proto | network.application_protocol | Uppercased and brackets removed  
method | network.http.method | Uppercased  
user_agent | network.http.parsed_user_agent | Parsed user agent string  
referer | network.http.referral_url | Value copied directly if not empty or "-"  
status_code | network.http.response_code | Value copied directly if not empty  
user_agent | network.http.user_agent | Value copied directly if not empty  
sessionid | network.session_id | Value copied directly if not empty or "-"  
host | principal.asset.hostname | Value copied directly if not empty or "-"  
x-forwarded-for, client_ip | principal.asset.ip | Merged from IPs extracted from x-forwarded-for and client_ip  
host | principal.hostname | Value copied directly if not empty or "-"  
x-forwarded-for, client_ip | principal.ip | Merged from IPs extracted from x-forwarded-for and client_ip  
city | principal.location.city | Value copied directly if not empty  
country | principal.location.country_or_region | Value copied directly if not empty or "-"  
username | principal.user.userid | Value copied directly if not empty or "-"  
sec_action | security_result.action | Value copied directly (sec_action set to "ALLOW" if mitigation_action or action matches (?i)allow, else "BLOCK" if matches (?i)block)  
action | security_result.action_details | Value copied directly if not empty  
confidence | security_result.confidence_details | Converted to string  
weight_label, hash_component_label, experimental_label, policy_type_label, additiondata fields | security_result.detection_fields | Merged from weight_label, hash_component_label, experimental_label, policy_type_label, and additiondata fields  
ruleinfo.rule_id, policy.id | security_result.rule_id | Value from policy.id if present, else from ruleinfo.rule_id  
policy.name | security_result.rule_name | Value copied directly if not empty  
policy.type | security_result.rule_type | Value copied directly if not empty  
server_ip, x-envoy-external-address | target.asset.ip | Merged from server_ip and IPs extracted from x-envoy-external-address  
server_ip, x-envoy-external-address | target.ip | Merged from server_ip and IPs extracted from x-envoy-external-address  
uri | target.url | Value copied directly if not empty  
| metadata.product_name | Set to "CEQUENCE_BOT_DEFENSE"  
| metadata.vendor_name | Set to "CEQUENCE_BOT_DEFENSE"  
`experimental_confidence", "extracted_data.respbody", "successful_login", "transaction_id", and "tag` | `additional.fields` | Mapped from changelog  
`ruleinfo.weight", "ruleinfo.hash_component", "ruleinfo.experimental", "x-cloud-trace-context", "access-control-allow-headers, "access-control-allow-methods", and "access-control-allow-origin` | `security_result.detection_fields` | Mapped from changelog  
`x_ip` | `principal.ip` | Mapped from changelog  
`x_externalip` | `target.ip` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cequence-bot-defense-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
