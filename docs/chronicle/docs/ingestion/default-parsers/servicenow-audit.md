---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/servicenow-audit/
title: Collect ServiceNow audit logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:26:47.892531+00:00
---

# Collect ServiceNow audit logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/servicenow-audit/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect ServiceNow audit logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest ServiceNow audit logs to Google Security Operations using multiple methods.

## Option A: GCS with Cloud Run function

This method uses a Cloud Run function to periodically query the ServiceNow REST API for audit logs and store them in a GCS bucket. Google Security Operations then collects the logs from the GCS bucket.

### Before you begin

Ensure that you have the following prerequisites:

  * A Google SecOps instance
  * Privileged access to ServiceNow tenant or API with appropriate roles (typically `admin` or user with read access to sys_audit table)
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs



### Collect ServiceNow prerequisites (IDs, API keys, org IDs, tokens)

  1. Sign in to the **ServiceNow Admin Console**.
  2. Go to **System Security > Users and Groups > Users**.
  3. Create a new user or select an existing user with appropriate permissions to access audit logs.
  4. Copy and save in a secure location the following details:

     * **Username**
     * **Password**
     * **Instance URL** (for example, `https://instance.service-now.com`)
**Note:** The user must have read access to the sys_audit table. By default, this requires the `admin` role. For non-admin users, you must create custom ACLs to grant read access to sys_audit.



#### Configure ACL for non-admin users

If you want to use a non-admin user account, you must create a custom Access Control List (ACL) to grant read access to the sys_audit table:

  1. Sign in to the **ServiceNow Admin Console** as an administrator.
  2. Go to **System Security > Access Control (ACL)**.
  3. Click **New**.
  4. Provide the following configuration details: 
     * **Type** : Select **record**.
     * **Operation** : Select **read**.
     * **Name** : Enter `sys_audit`.
     * **Description** : Enter `Allow read access to sys_audit table for Chronicle integration`.
  5. In the **Requires role** field, add the role assigned to your integration user (for example, `chronicle_reader`).
  6. Click **Submit**.
  7. Verify the ACL is active and the user can query the sys_audit table.



### Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `servicenow-audit-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




### Create service account for Cloud Run function

The Cloud Run function needs a service account with permissions to write to GCS bucket and be invoked by Pub/Sub.

#### Create service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `servicenow-audit-collector-sa`.
     * **Service account description** : Enter `Service account for Cloud Run function to collect ServiceNow audit logs`.
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



#### Grant IAM permissions on GCS bucket

Grant the service account write permissions on the GCS bucket:

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `servicenow-audit-collector-sa@PROJECT_ID.iam.gserviceaccount.com`).
     * **Assign roles** : Select **Storage Object Admin**.
  6. Click **Save**.



### Create Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `servicenow-audit-trigger`.
     * Leave other settings as default.
  4. Click **Create**.



### Create Cloud Run function to collect logs

The Cloud Run function is triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from ServiceNow API and writes them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `servicenow-audit-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose the Pub/Sub topic (`servicenow-audit-trigger`).
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub automatically handles authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select the service account (`servicenow-audit-collector-sa`).
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `servicenow-audit-logs` | GCS bucket name  
`GCS_PREFIX` | `audit-logs` | Prefix for log files  
`STATE_KEY` | `audit-logs/state.json` | State file path  
`API_BASE_URL` | `https://instance.service-now.com` | ServiceNow instance URL  
`API_USERNAME` | `your-username` | ServiceNow username  
`API_PASSWORD` | `your-password` | ServiceNow password  
`PAGE_SIZE` | `1000` | Records per page  
`MAX_PAGES` | `1000` | Maximum pages to fetch  
**Note:** For production environments, it is strongly recommended to store credentials in Secret Manager instead of environment variables and reference them in your Cloud Run function code.
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




#### Add function code

  1. Enter **main** in the **Entry point** field.
  2. In the inline code editor, create two files:

     * First file: **main.py:**
           
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
               GCS_PREFIX = os.environ.get('GCS_PREFIX', 'audit-logs')
               STATE_KEY = os.environ.get('STATE_KEY', 'audit-logs/state.json')
               API_BASE = os.environ.get('API_BASE_URL')
               USERNAME = os.environ.get('API_USERNAME')
               PASSWORD = os.environ.get('API_PASSWORD')
               PAGE_SIZE = int(os.environ.get('PAGE_SIZE', '1000'))
               MAX_PAGES = int(os.environ.get('MAX_PAGES', '1000'))
           
               def parse_datetime(value: str) -> datetime:
                   """Parse ServiceNow datetime string to datetime object."""
                   # ServiceNow format: YYYY-MM-DD HH:MM:SS
                   try:
                       return datetime.strptime(value, '%Y-%m-%d %H:%M:%S').replace(tzinfo=timezone.utc)
                   except ValueError:
                       # Try ISO format as fallback
                       if [value](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.ObjectCustomContextPayload.html#google_cloud_storage_blob_ObjectCustomContextPayload_value).endswith("Z"):
                           value = value[:-1] + "+00:00"
                       return datetime.fromisoformat(value)
           
               @functions_framework.cloud_event
               def main(cloud_event):
                   """
                   Cloud Run function triggered by Pub/Sub to fetch ServiceNow audit logs and write to GCS.
           
                   Args:
                       cloud_event: CloudEvent object containing Pub/Sub message
                   """
           
                   if not all([GCS_BUCKET, API_BASE, USERNAME, PASSWORD]):
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
                           last_time = now - timedelta(hours=24)
           
                       print(f"Fetching logs from {last_time.strftime('%Y-%m-%d %H:%M:%S')} to {now.strftime('%Y-%m-%d %H:%M:%S')}")
           
                       # Fetch logs
                       records, newest_event_time = fetch_logs(
                           api_base=API_BASE,
                           username=USERNAME,
                           password=PASSWORD,
                           start_time=last_time,
                           end_time=now,
                           page_size=PAGE_SIZE,
                           max_pages=MAX_PAGES,
                       )
           
                       if not records:
                           print("No new log records found.")
                           save_state(bucket, STATE_KEY, now.strftime('%Y-%m-%d %H:%M:%S'))
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
                           save_state(bucket, STATE_KEY, now.strftime('%Y-%m-%d %H:%M:%S'))
           
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
           
               def save_state(bucket, key, last_event_time: str):
                   """Save the last event timestamp to GCS state file."""
                   try:
                       state = {'last_event_time': last_event_time}
                       blob = bucket.blob(key)
                       blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
                           json.dumps(state, indent=2),
                           content_type='application/json'
                       )
                       print(f"Saved state: last_event_time={last_event_time}")
                   except Exception as e:
                       print(f"Warning: Could not save state: {e}")
           
               def fetch_logs(api_base: str, username: str, password: str, start_time: datetime, end_time: datetime, page_size: int, max_pages: int):
                   """
                   Fetch logs from ServiceNow sys_audit table with pagination and rate limiting.
           
                   Args:
                       api_base: ServiceNow instance URL
                       username: ServiceNow username
                       password: ServiceNow password
                       start_time: Start time for log query
                       end_time: End time for log query
                       page_size: Number of records per page
                       max_pages: Maximum total pages to fetch
           
                   Returns:
                       Tuple of (records list, newest_event_time string)
                   """
                   # Clean up base URL
                   base_url = api_base.rstrip('/')
           
                   endpoint = f"{base_url}/api/now/table/sys_audit"
           
                   # Encode credentials using UTF-8
                   auth_string = f"{username}:{password}"
                   auth_bytes = auth_string.encode('utf-8')
                   auth_b64 = base64.b64encode(auth_bytes).decode('utf-8')
           
                   headers = {
                       'Authorization': f'Basic {auth_b64}',
                       'Accept': 'application/json',
                       'Content-Type': 'application/json',
                       'User-Agent': 'GoogleSecOps-ServiceNowCollector/1.0'
                   }
           
                   records = []
                   newest_time = None
                   page_num = 0
                   backoff = 1.0
                   offset = 0
           
                   # Format timestamps for ServiceNow (YYYY-MM-DD HH:MM:SS)
                   start_time_str = start_time.strftime('%Y-%m-%d %H:%M:%S')
           
                   while True:
                       page_num += 1
           
                       if len(records) >= page_size * max_pages:
                           print(f"Reached max_pages limit ({max_pages})")
                           break
           
                       # Build query parameters
                       # Use >= operator for sys_created_on field (on or after)
                       params = []
                       params.append(f"sysparm_query=sys_created_on>={start_time_str}")
                       params.append(f"sysparm_display_value=true")
                       params.append(f"sysparm_limit={page_size}")
                       params.append(f"sysparm_offset={offset}")
           
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
                           page_results = data.get('result', [])
           
                           if not page_results:
                               print(f"No more results (empty page)")
                               break
           
                           print(f"Page {page_num}: Retrieved {len(page_results)} events")
                           records.extend(page_results)
           
                           # Track newest event time
                           for event in page_results:
                               try:
                                   event_time = event.get('sys_created_on')
                                   if event_time:
                                       if newest_time is None or parse_datetime(event_time) > parse_datetime(newest_time):
                                           newest_time = event_time
                               except Exception as e:
                                   print(f"Warning: Could not parse event time: {e}")
           
                           # Check for more results
                           if len(page_results) < page_size:
                               print(f"Reached last page (size={len(page_results)} < limit={page_size})")
                               break
           
                           # Move to next page
                           offset += page_size
           
                           # Small delay to avoid rate limiting
                           time.sleep(0.1)
           
                       except Exception as e:
                           print(f"Error fetching logs: {e}")
                           return [], None
           
                   print(f"Retrieved {len(records)} total records from {page_num} pages")
                   return records, newest_time
               ```
           

     * Second file: **requirements.txt:**
           
           ```
           functions-framework==3.*
           google-cloud-storage==2.*
           urllib3>=2.0.0
           ```
           

  3. Click **Deploy** to save and deploy the function.

  4. Wait for deployment to complete (2-3 minutes).




### Create Cloud Scheduler job

Cloud scheduler publishes messages to the Pub/Sub topic at regular intervals, triggering the Cloud Run function.

  1. In the **GCP Console** , go to **Cloud Scheduler**.
  2. Click **Create Job**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | `servicenow-audit-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the Pub/Sub topic (`servicenow-audit-trigger`)  
**Message body** | `{}` (empty JSON object)  
  4. Click **Create**.




#### Schedule frequency options

  * Choose frequency based on log volume and latency requirements:

Frequency | Cron Expression | Use Case  
---|---|---  
Every 5 minutes | `*/5 * * * *` | High-volume, low-latency  
Every 15 minutes | `*/15 * * * *` | Medium volume  
Every hour | `0 * * * *` | Standard (recommended)  
Every 6 hours | `0 */6 * * *` | Low volume, batch processing  
Daily | `0 0 * * *` | Historical data collection  



#### Test the integration

  1. In the **Cloud Scheduler** console, find your job.
  2. Click **Force run** to trigger the job manually.
  3. Wait a few seconds.
  4. Go to **Cloud Run > Services**.
  5. Click on your function name (`servicenow-audit-collector`).
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for the following:
         
         Fetching logs from YYYY-MM-DD HH:MM:SS to YYYY-MM-DD HH:MM:SS
         Page 1: Retrieved X events
         Wrote X records to gs://bucket-name/audit-logs/logs_YYYYMMDD_HHMMSS.ndjson
         Successfully processed X records
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click your bucket name.

  10. Navigate to the prefix folder (`audit-logs/`).

  11. Verify that a new `.ndjson` file was created with the current timestamp.




If you see errors in the logs:

  * **HTTP 401** : Check API credentials in environment variables
  * **HTTP 403** : Verify account has required permissions (admin role or custom ACL for sys_audit)
  * **HTTP 429** : Rate limiting - function will automatically retry with backoff
  * **Missing environment variables** : Check all required variables are set



### Retrieve the Google SecOps service account

Google SecOps uses a unique service account to read data from your GCS bucket. You must grant this service account access to your bucket.

#### Get the service account email

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `ServiceNow Audit logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **ServiceNow Audit** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email is displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Do not use service accounts from other documentation or examples.



### Grant IAM permissions to the Google SecOps service account

The Google SecOps service account needs **Storage Object Viewer** role on your GCS bucket.

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Paste the Google SecOps service account email.
     * **Assign roles** : Select **Storage Object Viewer**.
  6. Click **Save**.

**Note:** If you plan to use the deletion option "Delete transferred files" or "Delete transferred files and empty directories," grant **Storage Object Admin** role instead of Storage Object Viewer.



### Configure a feed in Google SecOps to ingest ServiceNow Audit logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `ServiceNow Audit logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **ServiceNow Audit** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://servicenow-audit-logs/audit-logs/
           

       * Replace:

         * `servicenow-audit-logs`: Your GCS bucket name.
         * `audit-logs`: Prefix/folder path where logs are stored.
**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never** : Never deletes any files after transfers (recommended for testing).
       * **Delete transferred files** : Deletes files after successful transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.

**Note:** If you select a deletion option, the service account must have **Storage Object Admin** role instead of Storage Object Viewer. Update IAM permissions accordingly.
     * **Maximum File Age** : Include files modified in the last number of days. Default is 180 days.

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).

     * **Ingestion labels** : The label to be applied to the events from this feed.

  9. Click **Next**.

  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## Option B: Bindplane agent with syslog

This method uses a Bindplane agent to collect ServiceNow Audit logs and forward them to Google Security Operations. Since ServiceNow doesn't natively support syslog for audit logs, we'll use a script to query the ServiceNow REST API and forward the logs to the Bindplane agent via syslog.

### Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between Bindplane agent and ServiceNow
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the ServiceNow management console or appliance with appropriate roles (typically `admin` or user with read access to sys_audit table)



### Get Google SecOps credentials for the Bindplane agent

To authenticate the Bindplane agent to Google SecOps, choose one of the following methods:

  * **New deployments** : Use the Chronicle API (Option 1).
  * **Legacy deployments** : Continue using the ingestion authentication file (Option 2) until the Ingestion API is discontinued on July 20, 2027.



#### Option 1: Create a service account for the Chronicle API (recommended)

  1. Sign in to the [Google Cloud console](https://console.cloud.google.com/) and select the Google Cloud project that is linked to your Google SecOps instance.
  2. Go to **IAM & Admin > Service Accounts**.
  3. Click **Create service account**.
  4. Provide the following configuration details: 
     * **Service account name** : Enter a name for the account (for example, `bindplane-ingest`).
     * **Service account description** : Enter a description (for example, `Bindplane agent log ingestion`).
  5. Click **Create and continue**.
  6. In the **Grant this service account access to project** section, click **Select a role** and select **Chronicle Editor**.
  7. Click **Continue** , and then click **Done**.
  8. Click the service account you created, and then go to the **Keys** tab.
  9. Click **Add key > Create new key**.
  10. Select **JSON** and click **Create**. The key file is downloaded to your computer.
  11. Save the key file as `ingestion-auth.json` in the Bindplane collector directory (`/opt/observiq-otel-collector/ingestion-auth.json` on Linux or `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json` on Windows), or update `creds_file_path` in `config.yaml` to match the path where you save it.
  12. Go to **IAM & Admin > Settings** and copy the **Project number**. You'll need it for the exporter configuration.

**Note:** The JSON key is a credential. Restrict access to the file on the Bindplane host and rotate the key according to your organization's policy.

#### Option 2: Download the ingestion authentication file (legacy)

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **ingestion authentication file**.
  4. Save the file securely on the system where the Bindplane agent will be installed.

**Note:** This file authenticates the agent to the legacy Ingestion API (`malachiteingestion-pa.googleapis.com`), which Google has scheduled for end of life on July 20, 2027. Plan to move to Option 1 before that date.

### Get Google SecOps customer ID

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Profile**.
  3. Copy and save the **Customer ID** from the **Organization Details** section.

**Note:** The customer ID is required for configuring the Bindplane agent exporter.



### Install Bindplane agent

Install the Bindplane agent on your Windows or Linux operating system according to the following instructions.

#### Windows installation

  1. Open **Command Prompt** or **PowerShell** as an administrator.
  2. Run the following command:
         
         msiexec /i "https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi" /quiet
         

  3. Wait for the installation to complete.

  4. Verify the installation by running:
         
         sc query observiq-otel-collector
         




The service should show as **RUNNING**.

#### Linux installation

  1. Open a terminal with root or sudo privileges.
  2. Run the following command:
         
         sudo sh -c "$(curl -fsSlL https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh)" install_unix.sh
         

  3. Wait for the installation to complete.

  4. Verify the installation by running:
         
         sudo systemctl status observiq-otel-collector
         




The service should show as **active (running)**.

#### Additional installation resources

For additional installation options and troubleshooting, see [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

### Configure Bindplane agent to ingest syslog and send to Google SecOps

#### Locate the configuration file

**Linux:** `bash sudo nano /opt/observiq-otel-collector/config.yaml`

**Windows:** `cmd notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"`

#### Edit the configuration file

Replace the entire contents of `config.yaml` with the following configuration:
    
    
    ```yaml
    receivers:
      udplog:
        listen_address: "0.0.0.0:514"
    
    exporters:
      chronicle/servicenow_audit:
        protocol: https
        # Region of your instance, for example us, europe, asia-southeast1
        location: <LOCATION>
        # Project number of the Google Cloud project linked to the instance
        project: '<PROJECT_NUMBER>'
        compression: gzip
        creds_file_path: '/path/to/ingestion-authentication-file.json'
        customer_id: '<YOUR_CUSTOMER_ID>'
        endpoint: chronicle.googleapis.com
        log_type: 'SERVICENOW_AUDIT'
        raw_log_field: body
        ingestion_labels:
          service: servicenow
    
    service:
      pipelines:
        logs/servicenow_to_chronicle:
          receivers:
            - udplog
          exporters:
            - chronicle/servicenow_audit
    ```
    

#### Configuration parameters

Replace the following placeholders:

  * **`listen_address`** : IP address and port to listen on. Use `0.0.0.0:514` to listen on all interfaces on port 514.
  * **`creds_file_path`** : Full path to the service account JSON key file (Option 1): 
    * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
    * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
  * **`<YOUR_CUSTOMER_ID>`**: Customer ID from the previous step.
  * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
  * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
  * `endpoint`: Keep set to `chronicle.googleapis.com`.



#### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/servicenow_audit:
            compression: gzip
            creds_file_path: '/path/to/ingestion-authentication-file.json'
            customer_id: '<YOUR_CUSTOMER_ID>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: 'SERVICENOW_AUDIT'
            raw_log_field: body
            ingestion_labels:
              service: servicenow
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

#### Save the configuration file

After editing, save the file: * **Linux** : Press `Ctrl+O`, then `Enter`, then `Ctrl+X` * **Windows** : Click **File > Save**

### Restart the Bindplane agent to apply the changes

  * To restart the Bindplane agent in Linux, run the following command:
        
        sudo systemctl restart observiq-otel-collector
        

    1. Verify the service is running:
           
           sudo systemctl status observiq-otel-collector
           

    2. Check logs for errors:
           
           sudo journalctl -u observiq-otel-collector -f
           

  * To restart the Bindplane agent in Windows, choose one of the following options:

    * Using Command Prompt or PowerShell as administrator:
          
          net stop observiq-otel-collector && net start observiq-otel-collector
          

    * Using Services console:

    1. Press `Win+R`, type `services.msc`, and press Enter.
    2. Locate **observIQ OpenTelemetry Collector**.
    3. Right-click and select **Restart**.

    4. Verify the service is running:
           
           sc query observiq-otel-collector
           

    5. Check logs for errors:
           
           type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
           




### Create a script to forward ServiceNow Audit logs to syslog

Since ServiceNow doesn't natively support syslog for audit logs, we'll create a script that queries the ServiceNow REST API and forwards the logs to syslog. This script can be scheduled to run periodically.

#### Python Script Example (Linux)

  * Create a file named `servicenow_audit_to_syslog.py` with the following content:
        
        import urllib3
        import json
        import datetime
        import base64
        import socket
        import time
        import os
        
        # ServiceNow API details
        BASE_URL = 'https://instance.service-now.com'  # Replace with your ServiceNow instance URL
        USERNAME = 'admin'  # Replace with your ServiceNow username
        PASSWORD = 'password'  # Replace with your ServiceNow password
        
        # Syslog details
        SYSLOG_SERVER = '127.0.0.1'  # Replace with your Bindplane agent IP
        SYSLOG_PORT = 514  # Replace with your Bindplane agent port
        
        # State file to keep track of last run
        STATE_FILE = '/tmp/servicenow_audit_last_run.txt'
        
        # Pagination settings
        PAGE_SIZE = 1000
        MAX_PAGES = 1000
        
        def get_last_run_timestamp():
            try:
                with open(STATE_FILE, 'r') as f:
                    return f.read().strip()
            except:
                return '1970-01-01 00:00:00'
        
        def update_state_file(timestamp):
            with open(STATE_FILE, 'w') as f:
                f.write(timestamp)
        
        def send_to_syslog(message):
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(message.encode(), (SYSLOG_SERVER, SYSLOG_PORT))
            sock.close()
        
        def get_audit_logs(last_run_timestamp):
            """
            Query ServiceNow sys_audit table with proper pagination.
            Uses sys_created_on field for timestamp filtering.
            """
            # Encode credentials using UTF-8
            auth_string = f"{USERNAME}:{PASSWORD}"
            auth_bytes = auth_string.encode('utf-8')
            auth_encoded = base64.b64encode(auth_bytes).decode('utf-8')
        
            # Setup HTTP client
            http = urllib3.PoolManager()
            headers = {
                'Authorization': f'Basic {auth_encoded}',
                'Accept': 'application/json'
            }
        
            results = []
            offset = 0
        
            # Format timestamp for ServiceNow (YYYY-MM-DD HH:MM:SS format)
            # Convert ISO format to ServiceNow format if needed
            if 'T' in last_run_timestamp:
                last_run_timestamp = last_run_timestamp.replace('T', ' ').split('.')[0]
        
            for page in range(MAX_PAGES):
                # Build query with pagination
                # Use >= operator for sys_created_on field (on or after)
                query_params = (
                    f"sysparm_query=sys_created_on>={last_run_timestamp}"
                    f"&sysparm_display_value=true"
                    f"&sysparm_limit={PAGE_SIZE}"
                    f"&sysparm_offset={offset}"
                )
        
                url = f"{BASE_URL}/api/now/table/sys_audit?{query_params}"
        
                try:
                    response = http.request('GET', url, headers=headers)
        
                    if response.status == 200:
                        data = json.loads(response.data.decode('utf-8'))
                        chunk = data.get('result', [])
                        results.extend(chunk)
        
                        # Stop if we got fewer records than PAGE_SIZE (last page)
                        if len(chunk) < PAGE_SIZE:
                            break
        
                        # Move to next page
                        offset += PAGE_SIZE
                    else:
                        print(f"Error querying ServiceNow API: {response.status} - {response.data.decode('utf-8')}")
                        break
        
                except Exception as e:
                    print(f"Exception querying ServiceNow API: {str(e)}")
                    break
        
            return results
        
        def main():
            # Get last run timestamp
            last_run_timestamp = get_last_run_timestamp()
        
            # Current timestamp for this run
            current_timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
            # Query ServiceNow API for audit logs
            audit_logs = get_audit_logs(last_run_timestamp)
        
            if audit_logs:
                # Send each log to syslog
                for log in audit_logs:
                    # Format the log as JSON
                    log_json = json.dumps(log)
        
                    # Send to syslog
                    send_to_syslog(log_json)
        
                    # Sleep briefly to avoid flooding
                    time.sleep(0.01)
        
                # Update state file
                update_state_file(current_timestamp)
        
                print(f"Successfully forwarded {len(audit_logs)} audit logs to syslog")
            else:
                print("No new audit logs to forward")
        
        if __name__ == "__main__":
            main()
        




#### Set Up Scheduled Execution (Linux)

  * Make the script executable:
        
        chmod +x servicenow_audit_to_syslog.py
        

  * Create a cron job to run the script every hour:
        
        crontab -e
        

  * Add the following line:
        
        0 * * * * /usr/bin/python3 /path/to/servicenow_audit_to_syslog.py >> /tmp/servicenow_audit_to_syslog.log 2>&1
        




#### PowerShell Script Example (Windows)

  * Create a file named `ServiceNow-Audit-To-Syslog.ps1` with the following content:
        
        # ServiceNow API details
        $BaseUrl = 'https://instance.service-now.com'  # Replace with your ServiceNow instance URL
        $Username = 'admin'  # Replace with your ServiceNow username
        $Password = 'password'  # Replace with your ServiceNow password
        
        # Syslog details
        $SyslogServer = '127.0.0.1'  # Replace with your Bindplane agent IP
        $SyslogPort = 514  # Replace with your Bindplane agent port
        
        # State file to keep track of last run
        $StateFile = "$env:TEMP\ServiceNowAuditLastRun.txt"
        
        # Pagination settings
        $PageSize = 1000
        $MaxPages = 1000
        
        function Get-LastRunTimestamp {
            try {
                if (Test-Path $StateFile) {
                    return Get-Content $StateFile
                } else {
                    return '1970-01-01 00:00:00'
                }
            } catch {
                return '1970-01-01 00:00:00'
            }
        }
        
        function Update-StateFile {
            param([string]$Timestamp)
            Set-Content -Path $StateFile -Value $Timestamp
        }
        
        function Send-ToSyslog {
            param([string]$Message)
            $UdpClient = New-Object System.Net.Sockets.UdpClient
            $UdpClient.Connect($SyslogServer, $SyslogPort)
            $Encoding = [System.Text.Encoding]::ASCII
            $Bytes = $Encoding.GetBytes($Message)
            $UdpClient.Send($Bytes, $Bytes.Length)
            $UdpClient.Close()
        }
        
        function Get-AuditLogs {
            param([string]$LastRunTimestamp)
        
            # Create auth header using UTF-8 encoding
            $Auth = [System.Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes("${Username}:${Password}"))
            $Headers = @{
                Authorization = "Basic ${Auth}"
                Accept = 'application/json'
            }
        
            $Results = @()
            $Offset = 0
        
            # Format timestamp for ServiceNow (YYYY-MM-DD HH:MM:SS format)
            # Convert ISO format to ServiceNow format if needed
            if ($LastRunTimestamp -match 'T') {
                $LastRunTimestamp = $LastRunTimestamp -replace 'T', ' '
                $LastRunTimestamp = $LastRunTimestamp -replace '\.\d+', ''
            }
        
            for ($page = 0; $page -lt $MaxPages; $page++) {
                # Build query with pagination
                # Use >= operator for sys_created_on field (on or after)
                $QueryParams = "sysparm_query=sys_created_on>=${LastRunTimestamp}&sysparm_display_value=true&sysparm_limit=${PageSize}&sysparm_offset=${Offset}"
                $Url = "${BaseUrl}/api/now/table/sys_audit?${QueryParams}"
        
                try {
                    $Response = Invoke-RestMethod -Uri $Url -Headers $Headers -Method Get
                    $Chunk = $Response.result
                    $Results += $Chunk
        
                    # Stop if we got fewer records than PageSize (last page)
                    if ($Chunk.Count -lt $PageSize) {
                        break
                    }
        
                    # Move to next page
                    $Offset += $PageSize
                } catch {
                    Write-Error "Error querying ServiceNow API: $_"
                    break
                }
            }
        
            return $Results
        }
        
        # Main execution
        $LastRunTimestamp = Get-LastRunTimestamp
        $CurrentTimestamp = (Get-Date).ToString('yyyy-MM-dd HH:mm:ss')
        
        $AuditLogs = Get-AuditLogs -LastRunTimestamp $LastRunTimestamp
        
        if ($AuditLogs -and $AuditLogs.Count -gt 0) {
            # Send each log to syslog
            foreach ($Log in $AuditLogs) {
                # Format the log as JSON
                $LogJson = $Log | ConvertTo-Json -Compress
        
                # Send to syslog
                Send-ToSyslog -Message $LogJson
        
                # Sleep briefly to avoid flooding
                Start-Sleep -Milliseconds 10
            }
        
            # Update state file
            Update-StateFile -Timestamp $CurrentTimestamp
        
            Write-Output "Successfully forwarded $($AuditLogs.Count) audit logs to syslog"
        } else {
            Write-Output "No new audit logs to forward"
        }
        




#### Set Up Scheduled Execution (Windows)

  1. Open **Task Scheduler**.
  2. Click **Create Task**.
  3. Provide the following configuration: 
     * **Name** : `ServiceNowAuditToSyslog`
     * **Security options** : Run whether user is logged on or not
  4. Go to the **Triggers** tab.
  5. Click **New** and set it to run hourly.
  6. Go to the **Actions** tab.
  7. Click **New** and set: 
     * **Action** : Start a program
     * **Program/script** : `powershell.exe`
     * **Arguments** : `-ExecutionPolicy Bypass -File "C:\path\to\ServiceNow-Audit-To-Syslog.ps1"`
  8. Click **OK** to save the task.



## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
`Current_Value_label` | `additional.fields` | Merged  
`Instance_label` | `additional.fields` | Merged  
`Old_Value_label` | `additional.fields` | Merged  
`Operation_label` | `additional.fields` | Merged  
`Update_By_label` | `additional.fields` | Merged  
`exportByteSize_label` | `additional.fields` | Merged  
`exportRecordCount_label` | `additional.fields` | Merged  
`field_` | `additional.fields` | Merged  
`name_label` | `additional.fields` | Merged  
`operation_label` | `additional.fields` | Merged  
`system_property_label` | `additional.fields` | Merged  
`type_label` | `additional.fields` | Merged  
`name` | `extensions.auth.type` | Mapped: `logout` → `AUTHTYPE_UNSPECIFIED`  
`inter_hostname` | `intermediary.hostname` | Directly mapped  
`host` | `intermediary.ip` | Merged  
`descrip` | `metadata.description` | Directly mapped  
`description` | `metadata.description` | Directly mapped  
`_timestamp` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`sys_created_on` | `metadata.event_timestamp` | Parsed as `yyyy-MM-dd HH:mm:ss`  
`has_principal` | `metadata.event_type` | Mapped: `true` → `STATUS_UPDATE`  
`has_user` | `metadata.event_type` | Mapped: `true` → `USER_UNCATEGORIZED`  
`name` | `metadata.event_type` | Mapped: `logout` → `USER_LOGOUT`  
`sys_id` | `metadata.product_log_id` | Directly mapped  
`application` | `metadata.product_name` | Directly mapped  
`version` | `metadata.product_version` | Directly mapped  
`_session_id` | `network.session_id` | Directly mapped  
`_logger_name` | `principal.application` | Directly mapped  
`parm2` | `principal.asset.ip` | Merged  
`prin_ip` | `principal.asset.ip` | Merged  
`parm2` | `principal.ip` | Merged  
`prin_ip` | `principal.ip` | Merged  
`role` | `principal.user.attribute.roles` | Merged  
`parm1` | `principal.user.email_addresses` | Mapped: `user_id` → `parm1`  
`parm2` | `principal.user.email_addresses` | Mapped: `^.+@.+$` → `parm2`  
`user_id` | `principal.user.email_addresses` | Merged  
`user_name` | `principal.user.user_display_name` | Directly mapped  
`User` | `principal.user.userid` | Directly mapped  
`_logged_in_user` | `principal.user.userid` | Directly mapped  
`_user` | `principal.user.userid` | Directly mapped  
`src_usr` | `principal.user.userid` | Directly mapped  
`user` | `principal.user.userid` | Directly mapped  
`user_id` | `principal.user.userid` | Directly mapped  
`security_result_action` | `security_result.action` | Merged  
`status` | `security_result.action_details` | Directly mapped  
`_system_id` | `target.asset.hostname` | Directly mapped  
`claimed_by` | `target.asset.hostname` | Directly mapped  
`_system_id` | `target.hostname` | Directly mapped  
`claimed_by` | `target.hostname` | Directly mapped  
`dst_ip` | `target.ip` | Merged  
`claimed_by_data_label` | `target.resource.attribute.labels` | Merged  
`instance` | `target.resource.name` | Directly mapped  
`tablename` | `target.resource.name` | Directly mapped  
`documentkey` | `target.resource.product_object_id` | Directly mapped  
`uri` | `target.url` | Directly mapped  
`dst_usr` | `target.user.userid` | Directly mapped  
N/A | `extensions.auth.type` | Constant: `MACHINE`  
N/A | `metadata.event_type` | Constant: `USER_LOGIN`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/servicenow-audit-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
