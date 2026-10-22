---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-sdwan/
title: Collect Cisco Catalyst SD-WAN Manager logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:34:58.223761+00:00
---

# Collect Cisco Catalyst SD-WAN Manager logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-sdwan/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Cisco Catalyst SD-WAN Manager logs

**Parser Version:** 7.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Cisco Catalyst SD-WAN Manager (formerly known as vManage) logs to Google Security Operations using Google Cloud Storage. Cisco Catalyst SD-WAN Manager is a centralized network management system that provides visibility and control over SD-WAN fabric, enabling administrators to monitor network performance, configure policies, and manage security across distributed enterprise networks.

## Before you begin

Make sure that you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * Privileged access to the Cisco Catalyst SD-WAN Manager management console
  * Cisco Catalyst SD-WAN Manager user account with API access permissions



## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `cisco-sdwan-logs-bucket`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Collect Cisco Catalyst SD-WAN Manager API credentials

### Create API user account

  1. Sign in to the **Cisco Catalyst SD-WAN Manager console**.
  2. From the menu, go to **Administration > Manage Users**.
  3. Click **Add User**.
  4. Provide the following configuration details: 
     * **Username** : Enter a username for API access (for example, `chronicle-api`).
     * **Password** : Enter a strong password.
     * **Confirm Password** : Re-enter the password.
     * **User Group** : Select a user group with appropriate permissions (see the next section).
  5. Click **Add**.
  6. Copy and save in a secure location the following details:

     * **Username** : Your Catalyst SD-WAN Manager username.
     * **Password** : Your Catalyst SD-WAN Manager password.
     * **Catalyst SD-WAN Manager Base URL** : The base URL of your Catalyst SD-WAN Manager server (for example, `https://sdwan-manager.example.com:8443`).
**Note:** These credentials will be used by the Cloud Run function to authenticate to the Cisco Catalyst SD-WAN Manager API.



### Configure user permissions

The API user account requires specific permissions to access audit logs, alarms, and events.

  1. In the **Cisco Catalyst SD-WAN Manager console** , from the menu, go to **Administration > Manage Users > User Groups**.
  2. Select the user group assigned to the API user (or click **Add User Group** to create a new group).
  3. Click **Edit**.
  4. In the **Feature** section, ensure the following permissions are enabled: 
     * **Audit Log** : Select **Read** permission.
     * **Alarms** : Select **Read** permission.
     * **Events** : Select **Read** permission.
  5. Click **Update**.



### Verify API access

Test your credentials before proceeding with the integration:

  1. Open a terminal or command prompt.
  2. Run the following command to test authentication:
         
         # Replace with your actual credentials
         SDWAN_HOST="https://sdwan-manager.example.com:8443"
         SDWAN_USERNAME="chronicle-api"
         SDWAN_PASSWORD="your-password"
         
         # Test authentication using session-based login (returns JSESSIONID cookie)
         curl -c cookies.txt -X POST \
           "${SDWAN_HOST}/j_security_check" \
           -H "Content-Type: application/x-www-form-urlencoded" \
           -d "j_username=${SDWAN_USERNAME}&j_password=${SDWAN_PASSWORD}"
         
         # Get CSRF token (X-XSRF-TOKEN)
         curl -b cookies.txt \
           "${SDWAN_HOST}/dataservice/client/token"
         




If authentication is successful, the second command will return a CSRF token string.

**Note:** In production environments, configure valid TLS certificates on Catalyst SD-WAN Manager and verify certificates in the HTTP client. The code examples use certificate verification disabled for testing purposes only.

## Create service account for Cloud Run function

The Cloud Run function needs a service account with permissions to write to GCS bucket and be invoked by Pub/Sub.

### Create service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `cisco-sdwan-collector-sa`.
     * **Service account description** : Enter `Service account for Cloud Run function to collect Cisco Catalyst SD-WAN Manager logs`.
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
  2. Click on your bucket name.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `cisco-sdwan-collector-sa@PROJECT_ID.iam.gserviceaccount.com`).
     * **Assign roles** : Select **Storage Object Admin**.
  6. Click **Save**.



## Create Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `cisco-sdwan-trigger`.
     * Leave other settings as default.
  4. Click **Create**.



## Create Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from Cisco Catalyst SD-WAN Manager API and write them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `cisco-sdwan-log-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose the topic (`cisco-sdwan-trigger`).
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select the service account (`cisco-sdwan-collector-sa`).
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value  
---|---  
`GCS_BUCKET` | `cisco-sdwan-logs-bucket`  
`GCS_PREFIX` | `cisco-sdwan`  
`STATE_KEY` | `cisco-sdwan/state.json`  
`SDWAN_HOST` | `https://sdwan-manager.example.com:8443`  
`SDWAN_USERNAME` | `chronicle-api`  
`SDWAN_PASSWORD` | `your-sdwan-password`  
`LOOKBACK_HOURS` | `1`  
  10. Scroll down in the **Variables & Secrets** tab to **Requests** :

     * **Request timeout** : Enter `600` seconds (10 minutes).
  11. Go to the **Settings** tab in **Containers** :

     * In the **Resources** section: 
       * **Memory** : Select **512 MiB** or higher.
       * **CPU** : Select **1**.
  12. In the **Revision scaling** section:

     * **Minimum number of instances** : Enter `0`.
     * **Maximum number of instances** : Enter `100` (or adjust based on expected load).
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
           import urllib.parse
           from datetime import datetime, timezone, timedelta
           import time
           
           # Disable SSL warnings for self-signed certificates (testing only)
           urllib3.disable_warnings(urllib3.[exceptions](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.exceptions.html).InsecureRequestWarning)
           
           # Initialize HTTP client with timeouts
           http = urllib3.PoolManager(
               timeout=urllib3.Timeout(connect=10.0, read=60.0),
               cert_reqs='CERT_NONE',
               retries=urllib3.Retry(total=3, backoff_factor=1)
           )
           
           # Initialize Storage client
           storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
           
           # Environment variables
           SDWAN_HOST = os.environ.get('SDWAN_HOST', '').rstrip('/')
           SDWAN_USERNAME = os.environ.get('SDWAN_USERNAME', '')
           SDWAN_PASSWORD = os.environ.get('SDWAN_PASSWORD', '')
           GCS_BUCKET = os.environ.get('GCS_BUCKET', '')
           GCS_PREFIX = os.environ.get('GCS_PREFIX', 'cisco-sdwan')
           STATE_KEY = os.environ.get('STATE_KEY', 'cisco-sdwan/state.json')
           LOOKBACK_HOURS = int(os.environ.get('LOOKBACK_HOURS', '1'))
           
           class CatalystSDWANAPI:
               """Client for Cisco Catalyst SD-WAN Manager API (formerly vManage)."""
           
               def __init__(self, host, username, password):
                   self.host = host
                   self.username = username
                   self.password = password
                   self.jsessionid = None
                   self.xsrf_token = None
           
               def authenticate(self):
                   """Authenticate using session-based login (j_security_check)."""
                   try:
                       login_url = f"{self.host}/j_security_check"
                       login_data = urllib.parse.urlencode({
                           'j_username': self.username,
                           'j_password': self.password
                       }).encode('utf-8')
           
                       response = http.request(
                           'POST',
                           login_url,
                           body=login_data,
                           headers={'Content-Type': 'application/x-www-form-urlencoded'},
                       )
           
                       if b'<html>' in response.data or response.status != 200:
                           print(f"Authentication failed: HTTP {response.status}")
                           return False
           
                       # Extract JSESSIONID from Set-Cookie header
                       cookie_header = response.headers.get('Set-Cookie', '')
                       for part in cookie_header.split(','):
                           if 'JSESSIONID=' in part:
                               self.jsessionid = part.split('JSESSIONID=')[1].split(';')[0]
                               break
           
                       if not self.jsessionid:
                           print("Failed to extract JSESSIONID from response")
                           return False
           
                       # Get XSRF token
                       token_url = f"{self.host}/dataservice/client/token"
                       headers = {
                           'Content-Type': 'application/json',
                           'Cookie': f"JSESSIONID={self.jsessionid}"
                       }
                       response = http.request('GET', token_url, headers=headers)
           
                       if response.status == 200:
                           self.xsrf_token = response.data.decode('utf-8').strip()
                           print("Successfully authenticated with Catalyst SD-WAN Manager")
                           return True
                       else:
                           print(f"Failed to get XSRF token: HTTP {response.status}")
                           return False
           
                   except Exception as e:
                       print(f"Authentication error: {e}")
                       return False
           
               def _get_headers(self):
                   """Build headers for authenticated API requests."""
                   return {
                       'Content-Type': 'application/json',
                       'Accept': 'application/json',
                       'Cookie': f"JSESSIONID={self.jsessionid}",
                       'X-XSRF-TOKEN': self.xsrf_token
                   }
           
               def _build_query(self, last_epoch_ms=None):
                   """Build a query payload with entry_time filter."""
                   query = {
                       "query": {
                           "condition": "AND",
                           "rules": []
                       },
                       "size": 10000
                   }
                   if last_epoch_ms:
                       query["query"]["rules"].append({
                           "value": [str(last_epoch_ms)],
                           "field": "entry_time",
                           "type": "date",
                           "operator": "greater"
                       })
                   else:
                       query["query"]["rules"].append({
                           "value": [str(LOOKBACK_HOURS)],
                           "field": "entry_time",
                           "type": "date",
                           "operator": "last_n_hours"
                       })
                   return query
           
               def fetch_data(self, endpoint, last_epoch_ms=None):
                   """Fetch data from a /dataservice endpoint using POST with query body."""
                   url = f"{self.host}/dataservice/{endpoint}"
                   headers = self._get_headers()
                   query = self._build_query(last_epoch_ms)
           
                   try:
                       response = http.request(
                           'POST',
                           url,
                           body=json.dumps(query),
                           headers=headers,
                       )
           
                       if response.status == 200:
                           return json.loads(response.data.decode('utf-8'))
                       else:
                           print(f"Failed to get {endpoint}: HTTP {response.status}")
                           return None
           
                   except Exception as e:
                       print(f"Error fetching {endpoint}: {e}")
                       return None
           
           def load_state(bucket):
               """Load the last run timestamp (epoch ms) from GCS state file."""
               try:
                   blob = bucket.blob(STATE_KEY)
                   if blob.exists():
                       state_data = json.loads(blob.[download_as_text](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_download_as_text)())
                       return state_data.get('last_run_time')
               except Exception as e:
                   print(f"Warning: Could not load state: {e}")
               return None
           
           def save_state(bucket, epoch_ms):
               """Save the current run timestamp (epoch ms) to GCS state file."""
               try:
                   state_data = {
                       'last_run_time': epoch_ms,
                       'updated_at': datetime.now(timezone.utc).isoformat()
                   }
                   blob = bucket.blob(STATE_KEY)
                   blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
                       json.dumps(state_data),
                       content_type='application/json'
                   )
                   print(f"Saved state: last_run_time={epoch_ms}")
               except Exception as e:
                   print(f"Warning: Could not save state: {e}")
           
           def upload_to_gcs(bucket, records, log_type):
               """Upload log records to GCS as NDJSON."""
               if not records:
                   print(f"No {log_type} records to upload")
                   return 0
           
               dt = datetime.now(timezone.utc)
               object_key = (
                   f"{GCS_PREFIX}/{log_type}/"
                   f"{dt.strftime('%Y/%m/%d')}/"
                   f"{log_type}_{dt.strftime('%Y%m%d_%H%M%S')}.ndjson"
               )
           
               ndjson = '\n'.join(
                   json.dumps(record, ensure_ascii=False) for record in records
               ) + '\n'
           
               blob = bucket.blob(object_key)
               blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(ndjson, content_type='application/x-ndjson')
               print(f"Uploaded {len(records)} {log_type} records to gs://{GCS_BUCKET}/{object_key}")
               return len(records)
           
           @functions_framework.cloud_event
           def main(cloud_event):
               """
               Cloud Run function triggered by Pub/Sub.
               Fetches audit logs, alarms, and events from Cisco Catalyst SD-WAN Manager
               API and writes them to GCS as NDJSON files.
           
               Args:
                   cloud_event: CloudEvent object containing Pub/Sub message
               """
               print(f"Starting Cisco Catalyst SD-WAN Manager log collection at {datetime.now(timezone.utc).isoformat()}")
           
               if not all([SDWAN_HOST, SDWAN_USERNAME, SDWAN_PASSWORD, GCS_BUCKET]):
                   print("Error: Missing required environment variables")
                   return
           
               try:
                   bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(GCS_BUCKET)
           
                   # Load last run timestamp
                   last_run_time = load_state(bucket)
                   if last_run_time:
                       print(f"Resuming from last_run_time={last_run_time}")
                   else:
                       print(f"No previous state found, collecting last {LOOKBACK_HOURS} hour(s) of logs")
           
                   # Authenticate
                   api = CatalystSDWANAPI(SDWAN_HOST, SDWAN_USERNAME, SDWAN_PASSWORD)
                   if not api.authenticate():
                       print("Failed to authenticate with Catalyst SD-WAN Manager")
                       return
           
                   # Current timestamp for state tracking (epoch milliseconds)
                   current_time = int(datetime.now(timezone.utc).timestamp() * 1000)
           
                   # Collect audit logs, alarms, and events
                   endpoints = [
                       ('audit_logs', 'auditlog'),
                       ('alarms', 'alarms'),
                       ('events', 'events'),
                   ]
           
                   total_records = 0
                   for log_type, endpoint in endpoints:
                       try:
                           print(f"Collecting {log_type} from /dataservice/{endpoint}...")
                           response_data = api.fetch_data(endpoint, last_run_time)
                           if response_data and 'data' in response_data:
                               count = upload_to_gcs(bucket, response_data['data'], log_type)
                               total_records += count
                           else:
                               print(f"No {log_type} data returned")
                       except Exception as e:
                           print(f"Error processing {log_type}: {e}")
                           continue
           
                   # Update state
                   save_state(bucket, current_time)
           
                   print(f"Collection completed. Total records processed: {total_records}")
           
               except Exception as e:
                   print(f"Function execution error: {e}")
                   raise
           

     * **requirements.txt:**
           
           functions-framework==3.*
           google-cloud-storage==2.*
           urllib3>=2.0.0
           

**Note:** This script is provided as an example and is not officially supported. We welcome feedback about how we can improve it. To submit feedback, click **Send Feedback > Google SecOps Security Product Feedback** on this page.
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
**Name** | `cisco-sdwan-log-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the topic (`cisco-sdwan-trigger`)  
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
  5. Click on the function name (`cisco-sdwan-log-collector`).
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         Starting Cisco Catalyst SD-WAN Manager log collection at ...
         Successfully authenticated with Catalyst SD-WAN Manager
         Collecting audit_logs from /dataservice/auditlog...
         Uploaded N audit_logs records to gs://...
         Collection completed. Total records processed: N
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click on your bucket name.

  10. Navigate to the prefix folder (`cisco-sdwan/`).

  11. Verify that new `.ndjson` files were created with the current timestamp.




If you see errors in the logs:

  * **HTTP 401** : Check API credentials in environment variables
  * **HTTP 403** : Verify the user account has required Read permissions for Audit Log, Alarms, and Events
  * **Authentication failed** : Verify the Catalyst SD-WAN Manager base URL includes the correct port (default `8443`)
  * **Missing environment variables** : Check all required variables are set



## Configure a feed in Google SecOps to ingest Cisco Catalyst SD-WAN Manager logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Cisco Catalyst SD-WAN Manager logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Cisco SD-WAN** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Do not use service accounts from other documentation or examples.
  9. Click **Next**.

  10. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://cisco-sdwan-logs-bucket/cisco-sdwan/
           

       * Replace: 
         * `cisco-sdwan-logs-bucket`: Your GCS bucket name.
         * `cisco-sdwan/`: Optional prefix/folder path where logs are stored (leave empty for root).
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
  2. Click on your bucket name.
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
`Tunnel_id_label` | `additional.fields` | Merged  
`additional_tag` | `additional.fields` | Merged  
`count_label` | `additional.fields` | Merged  
`dst_vrf_label` | `additional.fields` | Merged  
`logfeature_label` | `additional.fields` | Merged  
`logmodule_label` | `additional.fields` | Merged  
`meta_sequenceId_label` | `additional.fields` | Merged  
`msg_label` | `additional.fields` | Merged  
`qfp_label` | `additional.fields` | Merged  
`result_label` | `additional.fields` | Merged  
`rsa_sha256_label` | `additional.fields` | Merged  
`rsa_type_label` | `additional.fields` | Merged  
`sequence_label` | `additional.fields` | Merged  
`src_vrf_label` | `additional.fields` | Merged  
`tenant_vpn_id_label` | `additional.fields` | Merged  
`thread_label` | `additional.fields` | Merged  
`tos_label` | `additional.fields` | Merged  
`unknown_tenant_label` | `additional.fields` | Merged  
`vlan_id_label` | `additional.fields` | Merged  
`vpn_id_label` | `additional.fields` | Merged  
`description_1` | `extensions.auth.type` | Mapped: `(?i)closed` → `AUTHTYPE_UNSPECIFIED`  
`msg1` | `extensions.auth.type` | Mapped: `authenticated` → `AUTHTYPE_UNSPECIFIED`  
`msgs` | `extensions.auth.type` | Mapped: `(?i)success` → `AUTHTYPE_UNSPECIFIED`  
`prod_type` | `extensions.auth.type` | Mapped: `(?i)LOGOUT` → `AUTHTYPE_UNSPECIFIED`  
`host_name` | `intermediary.asset.hostname` | Directly mapped  
`host_name` | `intermediary.hostname` | Directly mapped  
`inter_host` | `intermediary.hostname` | Directly mapped  
`logmsg` | `metadata.description` | Directly mapped  
`message_value` | `metadata.description` | Directly mapped  
`msgs` | `metadata.description` | Directly mapped  
`date_time` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`time` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`time_t` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`timestamp` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`description_1` | `metadata.event_type` | Mapped: `(?i)closed` → `USER_LOGOUT`  
`has_principal` | `metadata.event_type` | Mapped: `true` → `NETWORK_CONNECTION`, `true` → `STATUS_UPDATE`  
`has_principal_user` | `metadata.event_type` | Mapped: `true` → `USER_UNCATEGORIZED`  
`msg1` | `metadata.event_type` | Mapped: `authenticated` → `USER_LOGIN`  
`msgs` | `metadata.event_type` | Mapped: `(?i)success` → `USER_LOGIN`  
`prod_type` | `metadata.event_type` | Mapped: `(?i)LOGOUT` → `USER_LOGOUT`  
`prod_type` | `metadata.product_event_type` | Directly mapped  
`log_id` | `metadata.product_log_id` | Directly mapped  
`logid` | `metadata.product_log_id` | Directly mapped  
`application_protocol` | `network.application_protocol` | Mapped: `(?i)SSH` → `SSH`  
`message` | `network.application_protocol` | Mapped: `(?i)SSH` → `SSH`, `(?i)netconf` → `NETCONF`, `(?i)dhcp` → `DHCP`  
`type1` | `network.dhcp.type` | Mapped: `DHCPDISCOVER` → `DISCOVER`  
`message` | `network.ip_protocol` | Mapped: `(?i)tcp` → `TCP`  
`network_protocol` | `network.ip_protocol` | Directly mapped  
`bytes` | `network.sent_bytes` | Directly mapped  
`session_id` | `network.session_id` | Directly mapped  
`network_host` | `network.tls.cipher` | Directly mapped  
`hostname` | `principal.asset.hostname` | Directly mapped  
`host` | `principal.asset.ip` | Merged  
`initiator_ip` | `principal.asset.ip` | Merged  
`ip` | `principal.asset.ip` | Merged  
`ipaddress` | `principal.asset.ip` | Merged  
`logusersrcip` | `principal.asset.ip` | Merged  
`peer_ip` | `principal.asset.ip` | Merged  
`principal_ip` | `principal.asset.ip` | Merged  
`principal_ip1` | `principal.asset.ip` | Merged  
`proxy_host` | `principal.asset.ip` | Merged  
`src_ip` | `principal.asset.ip` | Merged  
`system_ip` | `principal.asset.ip` | Merged  
`addr` | `principal.hostname` | Directly mapped  
`hostname` | `principal.hostname` | Directly mapped  
`host` | `principal.ip` | Merged  
`initiator_ip` | `principal.ip` | Merged  
`ip` | `principal.ip` | Merged  
`ipaddress` | `principal.ip` | Merged  
`logusersrcip` | `principal.ip` | Merged  
`peer_ip` | `principal.ip` | Merged  
`principal_ip` | `principal.ip` | Merged  
`principal_ip1` | `principal.ip` | Merged  
`proxy_host` | `principal.ip` | Merged  
`src_ip` | `principal.ip` | Merged  
`system_ip` | `principal.ip` | Merged  
`initiator_port` | `principal.port` | Directly mapped  
`port` | `principal.port` | Directly mapped  
`ports` | `principal.port` | Directly mapped  
`principal_port` | `principal.port` | Directly mapped  
`principal_port1` | `principal.port` | Directly mapped  
`src_port` | `principal.port` | Directly mapped  
`process_path` | `principal.process.file.full_path` | Directly mapped  
`parent_pid` | `principal.process.parent_process.pid` | Directly mapped  
`pid` | `principal.process.pid` | Directly mapped  
`process_label` | `principal.resource.attribute.labels` | Merged  
`process_name_label` | `principal.resource.attribute.labels` | Merged  
`loguser` | `principal.user.userid` | Directly mapped  
`user1` | `principal.user.userid` | Directly mapped  
`user_id` | `principal.user.userid` | Directly mapped  
`username` | `principal.user.userid` | Directly mapped  
`action` | `security_result.action` | Merged  
`message` | `security_result.action` | Mapped: `(?i)(succeeded/accounting start/open/occurred/update/successfully/success)` → `acti...  
`classification` | `security_result.category_details` | Merged  
`msg1` | `security_result.description` | Directly mapped  
`Malware_label` | `security_result.detection_fields` | Merged  
`direction_label` | `security_result.detection_fields` | Merged  
`egress_interface_label` | `security_result.detection_fields` | Merged  
`ingress_interface_label` | `security_result.detection_fields` | Merged  
`log_prefix_label` | `security_result.detection_fields` | Merged  
`log_reason_label` | `security_result.detection_fields` | Merged  
`packet_label` | `security_result.detection_fields` | Merged  
`policy_label` | `security_result.detection_fields` | Merged  
`port_label` | `security_result.detection_fields` | Merged  
`protocol_label` | `security_result.detection_fields` | Merged  
`proxy_port_label` | `security_result.detection_fields` | Merged  
`sent_bytes_1_label` | `security_result.detection_fields` | Merged  
`sent_bytes_2_label` | `security_result.detection_fields` | Merged  
`tty_label` | `security_result.detection_fields` | Merged  
`type_label` | `security_result.detection_fields` | Merged  
`udp_packets_label` | `security_result.detection_fields` | Merged  
`priority` | `security_result.severity` | Mapped: `1` → `LOW`  
`description_1` | `security_result.summary` | Directly mapped  
`dst_ip` | `target.asset.ip` | Merged  
`ipadres` | `target.asset.ip` | Merged  
`logdeviceid` | `target.asset.ip` | Merged  
`responder_ip` | `target.asset.ip` | Merged  
`target_ip` | `target.asset.ip` | Merged  
`target_ip1` | `target.asset.ip` | Merged  
`filename` | `target.file.names` | Merged  
`dst_ip` | `target.ip` | Merged  
`ipadres` | `target.ip` | Merged  
`logdeviceid` | `target.ip` | Merged  
`responder_ip` | `target.ip` | Merged  
`target_ip` | `target.ip` | Merged  
`target_ip1` | `target.ip` | Merged  
`dst_port` | `target.port` | Directly mapped  
`prts` | `target.port` | Directly mapped  
`responder_port` | `target.port` | Directly mapped  
`target_port` | `target.port` | Directly mapped  
`target_port1` | `target.port` | Directly mapped  
`filetype` | `target.process.file.mime_type` | Directly mapped  
`parent_identifier_label` | `target.resource.attribute.labels` | Merged  
`specific_identifer_label` | `target.resource.attribute.labels` | Merged  
`target_name` | `target.resource.name` | Directly mapped  
`instance_id` | `target.resource.product_object_id` | Directly mapped  
`target_username` | `target.user.userid` | Directly mapped  
`user` | `target.user.userid` | Directly mapped  
N/A | `extensions.auth.type` | Constant: `AUTHTYPE_UNSPECIFIED`  
N/A | `metadata.event_type` | Constant: `USER_LOGIN`  
N/A | `network.application_protocol` | Constant: `SSH`  
N/A | `network.dhcp.type` | Constant: `DISCOVER`  
N/A | `network.ip_protocol` | Constant: `TCP`  
N/A | `security_result.severity` | Constant: `LOW`  
`rsa_type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`sha_256` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`NETCONF` | `event.idm.read_only_udm.network.application_protocol` | Mapped from changelog  
`TCP` | `event.idm.read_only_udm.network.ip_protocol` | Mapped from changelog  
`DHCP` | `event.idm.read_only_udm.network.application_protocol` | Mapped from changelog  
`username1` | `target.user.userid` | Mapped from changelog  
`security_result.action` | `ALLOW` | Mapped from changelog  
`ip_1` | `principal.ip` | Mapped from changelog  
`ip_2` | `target.ip` | Mapped from changelog  
`port_1` | `principal.port` | Mapped from changelog  
`port_2` | `target.port` | Mapped from changelog  
`message_1` | `metadata.description` | Mapped from changelog  
`malware` | `security_result.detection_fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-sdwan-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
