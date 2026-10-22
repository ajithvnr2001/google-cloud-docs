---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/salesforce-commerce-cloud/
title: Collect Salesforce Commerce Cloud logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:33:32.152684+00:00
---

# Collect Salesforce Commerce Cloud logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/salesforce-commerce-cloud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Salesforce Commerce Cloud logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Salesforce Commerce Cloud logs to Google Security Operations using Google Cloud Storage V2.

Salesforce Commerce Cloud is an e-commerce platform that generates transaction, access, and security audit logs. A Cloud Run function connects to the Salesforce Commerce Cloud WebDAV endpoint on a schedule, downloads log files, writes them to a GCS bucket in NDJSON format, and Google SecOps ingests them through a GCS V2 feed.

## Before you begin

Mkae sure you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * Privileged access to Salesforce Commerce Cloud Business Manager with WebDAV access permission



## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `sfcc-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Collect Salesforce Commerce Cloud credentials

### Configure WebDAV access

  1. Sign in to **Business Manager** for your Salesforce Commerce Cloud instance.
  2. Go to **Administration > Organization > Roles & Permissions**.
  3. Verify that your user account has the **WebDAV File Access** permission enabled.
  4. Note your SFCC instance hostname (for example, `development-yoursite-dw.demandware.net`).
  5. Save the following credentials in a secure location:

     * **SFCC Host** : Your instance hostname (for example, `development-yoursite-dw.demandware.net`).
     * **Username** : Your Business Manager username.
     * **Password** : Your Business Manager password.
**Note:** WebDAV access must be enabled for your user account in **Administration > Organization > Roles & Permissions**.



### Verify permissions

To verify the account has the required permissions:

  1. Sign in to **Business Manager** for your Salesforce Commerce Cloud instance.
  2. Go to **Administration > Site Development > Development Setup**.
  3. Click **Log Files** under the WebDAV section.
  4. If you can see log file directories, you have the required permissions.
  5. If you cannot see this option, contact your SFCC administrator to grant WebDAV access.



### Test API access

  * Test your credentials before proceeding with the integration:
        
        # Replace with your actual credentials
        SFCC_HOST="development-yoursite-dw.demandware.net"
        USERNAME="your-username"
        PASSWORD="your-password"
        
        # Test WebDAV access to log directory
        curl -v -u "${USERNAME}:${PASSWORD}" \
          "https://${SFCC_HOST}/on/demandware.servlet/webdav/Sites/Logs/"
        




## Create service account for Cloud Run function

The Cloud Run function needs a service account with permissions to write to GCS bucket and be invoked by Pub/Sub.

### Create service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `sfcc-logs-collector-sa`.
     * **Service account description** : Enter `Service account for Cloud Run function to collect Salesforce Commerce Cloud logs`.
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
  2. Click your bucket name (for example, `sfcc-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `sfcc-logs-collector-sa@your-project.iam.gserviceaccount.com`).
     * **Assign roles** : Select **Storage Object Admin**.
  6. Click **Save**.



## Create Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `sfcc-logs-trigger`.
     * Leave other settings as default.
  4. Click **Create**.



## Create Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from Salesforce Commerce Cloud WebDAV and write them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `sfcc-logs-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose the topic `sfcc-logs-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select the service account `sfcc-logs-collector-sa`.
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `sfcc-logs` | GCS bucket name  
`GCS_PREFIX` | `sfcc` | Prefix for log files  
`STATE_KEY` | `sfcc/state.json` | State file path  
`SFCC_HOST` | `development-yoursite-dw.demandware.net` | SFCC instance hostname  
`SFCC_USERNAME` | `your-username` | Business Manager username  
`SFCC_PASSWORD` | `your-password` | Business Manager password  
`LOG_DIRS` | `security,error,warn,customerror` | Comma-separated log directories  
`LOOKBACK_HOURS` | `24` | Initial lookback period  
  10. Scroll down in the **Variables & Secrets** tab to **Requests** :

     * **Request timeout** : Enter `600` seconds (10 minutes).
  11. Go to the **Settings** tab in **Containers** :

     * In the **Resources** section: 
       * **Memory** : Select **512 MiB** or higher.
       * **CPU** : Select **1**.
     * Click **Done**.
  12. Scroll down to **Execution environment** :

     * Select **Default** (recommended).
  13. In the **Revision scaling** section:

     * **Minimum number of instances** : Enter `0`.
     * **Maximum number of instances** : Enter `100` (or adjust based on expected load).
  14. Click **Create**.

  15. Wait for the service to be created (1-2 minutes).

  16. After the service is created, the **inline code editor** will open automatically.




### Add function code

  1. Enter **main** in **Function entry point**.
  2. In the inline code editor, create two files:

     * First file - **main.py:**
           
           import functions_framework
           from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
           import json
           import os
           import urllib3
           from datetime import datetime, timezone, timedelta
           import time
           import base64
           import re
           
           # Initialize HTTP client with timeouts
           http = urllib3.PoolManager(
             timeout=urllib3.Timeout(connect=10.0, read=60.0),
             retries=False,
           )
           
           # Initialize Storage client
           storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
           
           # Environment variables
           GCS_BUCKET = os.environ.get('GCS_BUCKET')
           GCS_PREFIX = os.environ.get('GCS_PREFIX', 'sfcc')
           STATE_KEY = os.environ.get('STATE_KEY', 'sfcc/state.json')
           SFCC_HOST = os.environ.get('SFCC_HOST')
           SFCC_USERNAME = os.environ.get('SFCC_USERNAME')
           SFCC_PASSWORD = os.environ.get('SFCC_PASSWORD')
           LOG_DIRS = [d.strip() for d in os.environ.get('LOG_DIRS', 'security,error,warn,customerror').split(',') if d.strip()]
           LOOKBACK_HOURS = int(os.environ.get('LOOKBACK_HOURS', '24'))
           
           def parse_datetime(value: str) -> datetime:
             """Parse ISO datetime string to datetime object."""
             if [value](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.ObjectCustomContextPayload.html#google_cloud_storage_blob_ObjectCustomContextPayload_value).endswith("Z"):
               value = value[:-1] + "+00:00"
             return datetime.fromisoformat(value)
           
           @functions_framework.cloud_event
           def main(cloud_event):
             """
             Cloud Run function triggered by Pub/Sub to fetch Salesforce Commerce Cloud
             logs via WebDAV and write to GCS.
           
             Args:
               cloud_event: CloudEvent object containing Pub/Sub message
             """
           
             if not all([GCS_BUCKET, SFCC_HOST, SFCC_USERNAME, SFCC_PASSWORD]):
               print('Error: Missing required environment variables')
               return
           
             try:
               bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(GCS_BUCKET)
           
               # Load state
               state = load_state(bucket, STATE_KEY)
           
               now = datetime.now(timezone.utc)
               last_time = None
           
               if isinstance(state, dict) and [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get("last_event_time"):
                 try:
                   last_time = parse_datetime(state["last_event_time"])
                 except Exception as e:
                   print(f"Warning: Could not parse last_event_time: {e}")
           
               if last_time is None:
                 last_time = now - timedelta(hours=LOOKBACK_HOURS)
           
               print(f"Fetching logs since {last_time.isoformat()}")
           
               # Build auth header
               credentials = f"{SFCC_USERNAME}:{SFCC_PASSWORD}"
               encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
               headers = {
                 'Authorization': f'Basic {encoded_credentials}',
                 'User-Agent': 'GoogleSecOps-SFCCCollector/1.0'
               }
           
               total_files = 0
               webdav_base = f"https://{SFCC_HOST}/on/demandware.servlet/webdav/Sites/Logs"
           
               for log_dir in LOG_DIRS:
                 print(f"Processing log directory: {log_dir}")
                 files_processed = fetch_and_upload_logs(
                   bucket=bucket,
                   webdav_base=webdav_base,
                   log_dir=log_dir,
                   headers=headers,
                   since=last_time,
                   now=now,
                 )
                 total_files += files_processed
           
               if total_files == 0:
                 print("No new log files found.")
               else:
                 print(f"Successfully processed {total_files} log files")
           
               save_state(bucket, STATE_KEY, now.isoformat())
           
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
           
           def list_webdav_files(webdav_url: str, headers: dict):
             """List files in a WebDAV directory using PROPFIND."""
             backoff = 1.0
             max_retries = 3
           
             for attempt in range(max_retries):
               response = http.request('PROPFIND', webdav_url, headers={**headers, 'Depth': '1'})
           
               if response.status == 429:
                 retry_after = int(response.headers.get('Retry-After', str(int(backoff))))
                 print(f"Rate limited (429). Retrying after {retry_after}s...")
                 time.sleep(retry_after)
                 backoff = min(backoff * 2, 30.0)
                 continue
           
               if response.status not in (200, 207):
                 print(f"HTTP Error listing {webdav_url}: {response.status}")
                 return []
           
               content = response.data.decode('utf-8')
               # Parse file names from WebDAV PROPFIND XML response
               files = re.findall(r'<D:href>([^<]+)</D:href>', content)
               return [f for f in files if not f.endswith('/')]
           
             return []
           
           def fetch_and_upload_logs(bucket, webdav_base: str, log_dir: str, headers: dict, since: datetime, now: datetime):
             """
             Fetch log files from a WebDAV directory and upload to GCS.
           
             Args:
               bucket: GCS bucket object
               webdav_base: WebDAV base URL
               log_dir: Log directory name
               headers: HTTP headers with auth
               since: Only process files newer than this
               now: Current time for file naming
           
             Returns:
               Number of files processed
             """
             dir_url = f"{webdav_base}/{log_dir}/"
             files = list_webdav_files(dir_url, headers)
             files_processed = 0
             backoff = 1.0
           
             for file_path in files:
               file_name = file_path.split('/')[-1]
               if not file_name:
                 continue
           
               # Download file
               file_url = f"https://{SFCC_HOST}{file_path}"
           
               response = http.request('GET', file_url, headers=headers)
           
               if response.status == 429:
                 retry_after = int(response.headers.get('Retry-After', str(int(backoff))))
                 print(f"Rate limited (429). Retrying after {retry_after}s...")
                 time.sleep(retry_after)
                 backoff = min(backoff * 2, 30.0)
                 response = http.request('GET', file_url, headers=headers)
           
               if response.status != 200:
                 print(f"Error downloading {file_name}: {response.status}")
                 continue
           
               backoff = 1.0
               content = response.data
           
               if not content:
                 continue
           
               # Upload to GCS
               timestamp = now.strftime('%Y%m%d_%H%M%S')
               object_key = f"{GCS_PREFIX}/{log_dir}/{file_name}_{timestamp}"
               blob = bucket.blob(object_key)
           
               # Convert log lines to NDJSON
               lines = content.decode('utf-8', errors='replace').splitlines()
               records = []
               for line in lines:
                 line = line.strip()
                 if line:
                   try:
                     record = json.loads(line)
                   except json.JSONDecodeError:
                     record = {'raw_log': line, 'log_dir': log_dir, 'source_file': file_name}
                   records.append(record)
           
               if records:
                 ndjson = '\n'.join([json.dumps(r, ensure_ascii=False) for r in records]) + '\n'
                 blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(ndjson, content_type='application/x-ndjson')
                 print(f"Uploaded {len(records)} records from {file_name} to gs://{GCS_BUCKET}/{object_key}")
                 files_processed += 1
           
             return files_processed
           

     * Second file - **requirements.txt:**
           
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
**Name** | `sfcc-logs-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the topic `sfcc-logs-trigger`  
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

  1. In the **Cloud Scheduler** console, find your job (`sfcc-logs-collector-hourly`).
  2. Click **Force run** to trigger manually.
  3. Wait a few seconds and go to **Cloud Run > Services > sfcc-logs-collector > Logs**.
  4. Verify the function executed successfully. Look for:
         
         Fetching logs since YYYY-MM-DDTHH:MM:SS+00:00
         Processing log directory: security
         Uploaded X records from filename.log to gs://sfcc-logs/sfcc/security/filename.log_YYYYMMDD_HHMMSS
         Successfully processed X log files
         

  5. Check the GCS bucket (`sfcc-logs`) to confirm logs were written.




If you see errors in the logs:

  * **HTTP 401** : Check SFCC credentials in environment variables
  * **HTTP 403** : Verify account has WebDAV File Access permission in Business Manager
  * **HTTP 429** : Rate limiting - function will automatically retry with backoff
  * **Missing environment variables** : Check all required variables are set



## Configure a feed in Google SecOps to ingest Salesforce Commerce Cloud logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Salesforce Commerce Cloud Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Salesforce Commerce Cloud** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address. You will use it in the next step.

**Note:** Each Google SecOps instance has a unique service account. Do not use service accounts from other documentation or examples.
  9. Click **Next**.

  10. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://sfcc-logs/sfcc/
           

       * Replace: 
         * `sfcc-logs`: Your GCS bucket name.
         * `sfcc/`: Prefix/folder path where logs are stored.
**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never** : Never deletes any files after transfers (recommended for testing).
       * **Delete transferred files** : Deletes files after successful transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.

**Note:** If you select a deletion option, the service account must have **Storage Object Admin** role instead of Storage Object Viewer. Update IAM permissions accordingly.
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days).

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).

     * **Ingestion labels** : The label to be applied to the events from this feed.

  11. Click **Next**.

  12. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## Grant IAM permissions to the Google SecOps service account

The Google SecOps service account needs **Storage Object Viewer** role on your GCS bucket.

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name (`sfcc-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Paste the Google SecOps service account email.
     * **Assign roles** : Select **Storage Object Viewer**.
  6. Click **Save**.

**Note:** If you plan to use the deletion option "Delete transferred files" or "Delete transferred files and empty directories," grant **Storage Object Admin** role instead of Storage Object Viewer.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`auth.mechanism` | `extensions.auth.mechanism` | Merged  
`csv_format` | `extensions.auth.mechanism` | Mapped: `false` → `auth.mechanism`  
`event_id` | `extensions.auth.mechanism` | Mapped: `Login: Success` → `auth.mechanism`  
`mechanism` | `extensions.auth.mechanism` | Merged  
`LoginType` | `extensions.auth.type` | Mapped: `Application` → `AUTHTYPE_UNSPECIFIED`  
`csv_format` | `extensions.auth.type` | Mapped: `false` → `AUTHTYPE_UNSPECIFIED`  
`event_id` | `extensions.auth.type` | Mapped values (6 total, e.g. ` "Login", "LoginAsEvent", "IdentityVerificationEvent", "LoginE...  
`eventType.name` | `metadata.description` | Directly mapped  
`metadata_description` | `metadata.description` | Directly mapped  
`collected_timestamp` | `metadata.event_timestamp` | Parsed as `yyyyMMddHHmmss`  
`createdAt` | `metadata.event_timestamp` | Parsed as `UNIX_MS`  
`createdDate` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ss.SSS`  
`timestamp` | `metadata.event_timestamp` | Parsed as `yyyyMMddHHmmss`  
`ts_date` | `metadata.event_timestamp` | Parsed as `yyyy-MM-dd HH:mm:ss.SSSZ`  
`csv_format` | `metadata.event_type` | Mapped: `false` → `USER_LOGIN`, `false` → `USER_LOGOUT`, `false` → `USER_RESOURCE_UPDATE_CON...  
`event_id` | `metadata.event_type` | Mapped: `Login: Success` → `USER_LOGIN`, `Logout` → `USER_LOGOUT`  
`event_type` | `metadata.event_type` | Directly mapped  
`label` | `metadata.ingestion_labels` | Merged  
`resource_name` | `metadata.ingestion_labels` | Mapped: `"ReportEvent","SessionHijackingEventStore","BulkApiResultEventStore","CredentialStu...  
`attrs.cat` | `metadata.product_event_type` | Renamed/mapped  
`eventType.id` | `metadata.product_event_type` | Directly mapped  
`event_id` | `metadata.product_event_type` | Directly mapped  
`event_identifier` | `metadata.product_log_id` | Directly mapped  
`id` | `metadata.product_log_id` | Directly mapped  
`protocol` | `network.application_protocol` | Directly mapped  
`transaction_id` | `network.dhcp.transaction_id` | Directly mapped  
`referral_url` | `network.http.referral_url` | Directly mapped  
`request_status` | `network.http.response_code` | Directly mapped  
`attrs.Application` | `principal.application` | Renamed/mapped  
`enterpriseId` | `principal.group.product_object_id` | Directly mapped  
`attrs.src` | `principal.ip` | Merged  
`csv_format` | `principal.ip` | Mapped: `false` → `attrs.src`  
`event_id` | `principal.ip` | Mapped: `Login: Success` → `attrs.src`  
`Status_LK` | `principal.labels` | Merged  
`Status_LK` | `principal.resource.attribute.labels` | Merged  
`browser_name` | `principal.resource.name` | Directly mapped  
`memberId` | `principal.resource.product_object_id` | Directly mapped  
`principal_resource_type` | `principal.resource.type` | Directly mapped  
`attrs.usrName` | `principal.user.email_addresses` | Merged  
`csv_format` | `principal.user.email_addresses` | Mapped: `false` → `attrs.usrName`  
`src_email` | `principal.user.email_addresses` | Merged  
`attrs.USER_ID_DERIVED` | `principal.user.product_object_id` | Renamed/mapped  
`employee.employeeName` | `principal.user.user_display_name` | Directly mapped  
`user_display_name` | `principal.user.user_display_name` | Directly mapped  
`attrs.usrName` | `principal.user.userid` | Directly mapped  
`employee.userName` | `principal.user.userid` | Directly mapped  
`login_key` | `principal.user.userid` | Directly mapped  
`user_id` | `principal.user.userid` | Directly mapped  
`csv_format` | `security_result` | Mapped: `false` → `sec_result`  
`event_id` | `security_result` | Mapped: `Login: Success` → `sec_result`  
`sec_result` | `security_result` | Merged  
`sr` | `security_result` | Merged  
`action` | `security_result.action` | Merged  
`eventSource.name` | `src.resource.name` | Directly mapped  
`eventSource.id` | `src.resource.product_object_id` | Directly mapped  
`organization_id` | `target.administrative_domain` | Directly mapped  
`target_hostname` | `target.asset.hostname` | Directly mapped  
`device_id` | `target.asset_id` | Directly mapped  
`target_hostname` | `target.hostname` | Directly mapped  
`call_time` | `target.resource.attribute.labels` | Merged  
`cpu` | `target.resource.attribute.labels` | Merged  
`db_cpu` | `target.resource.attribute.labels` | Merged  
`db_type` | `target.resource.attribute.labels` | Merged  
`duration_time` | `target.resource.attribute.labels` | Merged  
`entry_p` | `target.resource.attribute.labels` | Merged  
`exe_time` | `target.resource.attribute.labels` | Merged  
`no_sql_que` | `target.resource.attribute.labels` | Merged  
`ope` | `target.resource.attribute.labels` | Merged  
`rows_proc` | `target.resource.attribute.labels` | Merged  
`run` | `target.resource.attribute.labels` | Merged  
`ses_level` | `target.resource.attribute.labels` | Merged  
`ss_type` | `target.resource.attribute.labels` | Merged  
`total_time` | `target.resource.attribute.labels` | Merged  
`user_ty` | `target.resource.attribute.labels` | Merged  
`verify_method` | `target.resource.attribute.labels` | Merged  
`attrs.AccountId` | `target.resource.id` | Renamed/mapped  
`attrs.CaseId` | `target.resource.id` | Renamed/mapped  
`attrs.ContactId` | `target.resource.id` | Renamed/mapped  
`eventSource.id` | `target.resource.id` | Directly mapped  
`request_id` | `target.resource.id` | Directly mapped  
`eventSource.name` | `target.resource.name` | Directly mapped  
`object.name` | `target.resource.name` | Directly mapped  
`resource_name` | `target.resource.name` | Directly mapped  
`object.id` | `target.resource.product_object_id` | Directly mapped  
`event_id` | `target.resource.resource_type` | Mapped: `PlatformEncryption` → `ACCESS_POLICY`, `ApexCallout` → `ACCESS_POLICY`, `ApexTrigge...  
`target_resource_type` | `target.resource.resource_type` | Directly mapped  
`event_id` | `target.resource.type` | Mapped: `(QueuedExecution/ApexExecution)` → `BATCH`, `ApexTrigger` → `DATABASE_TRIGGER`, `Co...  
`attrs.LoginUrl` | `target.url` | Renamed/mapped  
`attrs.attributes.url` | `target.url` | Renamed/mapped  
`uri` | `target.url` | Directly mapped  
`attrs.usrName` | `target.user.email_addresses` | Merged  
`csv_format` | `target.user.email_addresses` | Mapped: `false` → `attrs.usrName`  
`event_id` | `target.user.email_addresses` | Mapped: `Logout` → `attrs.usrName`  
`target_user_display_name` | `target.user.user_display_name` | Directly mapped  
`target_user_name` | `target.user.userid` | Directly mapped  
N/A | `extensions.auth.auth_details` | Constant: `ACTIVE`  
N/A | `extensions.auth.type` | Constant: `SSO`  
N/A | `metadata.event_type` | Constant: `GENERIC_EVENT`  
N/A | `metadata.product_name` | Constant: `SALESFORCE`  
N/A | `metadata.vendor_name` | Constant: `SALESFORCE`  
N/A | `target.resource.resource_type` | Constant: `ACCESS_POLICY`  
N/A | `target.resource.type` | Constant: `BATCH`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/salesforce-commerce-cloud-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
