---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sap-successfactors/
title: Collect SAP SuccessFactors logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:52:54.603289+00:00
---

# Collect SAP SuccessFactors logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sap-successfactors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect SAP SuccessFactors logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest SAP SuccessFactors logs to Google Security Operations using Google Cloud Storage V2.

SAP SuccessFactors is a cloud-based human capital management (HCM) platform that manages core HR processes, talent management, payroll, and workforce analytics. It generates user activity, authentication, and audit trail logs that can be collected using the OData API.

## Before you begin

Ensure that you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * Privileged access to SAP SuccessFactors with administrator permissions
  * SAP SuccessFactors OData API access enabled for your tenant
  * Your SAP SuccessFactors API server URL (for example, `api15.sapsf.com`)



## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `sap-successfactors-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Collect SAP SuccessFactors API credentials

### Determine API server URL

The SAP SuccessFactors API server URL depends on your data center. Common API server URLs:

Data Center | API Server URL  
---|---  
DC2 (Amsterdam) | `https://api2.successfactors.eu`  
DC4 (Sydney) | `https://api4.successfactors.com`  
DC8 (Frankfurt) | `https://api8.successfactors.com`  
DC10 (US East) | `https://api10.successfactors.com`  
DC12 (Shanghai) | `https://api012.successfactors.cn`  
DC15 (US West) | `https://api15.sapsf.com`  
DC17 (Singapore) | `https://api17.sapsf.com`  
DC19 (UAE) | `https://api19.sapsf.com`  
**Note:** Confirm your actual API server URL from the SAP SuccessFactors admin console under **Admin Center > Company Settings** or from your SAP support documentation.

### Create API user credentials

  1. Sign in to **SAP SuccessFactors** as an administrator.
  2. Go to **Admin Center > Manage Permission Roles**.
  3. Create or select a role that includes the following permissions: 
     * **Manage Audit Trail** : Read access to audit data
     * **OData API** : Access to the OData API endpoints
  4. Go to **Admin Center > Manage Users**.
  5. Create a technical user or select an existing user for API integration.
  6. Assign the permission role to the user.
  7. Note the following credentials:

     * **Username** : The SAP SuccessFactors user ID (format: `USERNAME@COMPANY_ID`)
     * **Password** : The user's password
     * **Company ID** : Your SAP SuccessFactors company identifier
**Note:** SAP SuccessFactors uses Basic Authentication with the format `USERNAME@COMPANY_ID:PASSWORD` for OData API access.



### Verify permissions

To verify the account has the required permissions:

  1. Sign in to **SAP SuccessFactors**.
  2. Go to **Admin Center > Audit Trail**.
  3. If you can see audit trail data and export options, you have the required permissions.
  4. If you cannot see this option, contact your SAP administrator to grant the **Manage Audit Trail** permission.



### Test API access

  * Test your credentials before proceeding with the integration:
        
        # Replace with your actual credentials
        SF_USER="USERNAME@COMPANY_ID"
        SF_PASSWORD="your-password"
        API_SERVER="https://api15.sapsf.com"
        
        # Test API access - fetch audit trail metadata
        curl -v -u "${SF_USER}:${SF_PASSWORD}" \
          "${API_SERVER}/odata/v2/AuditTrail?\$top=1&\$format=json"
        




## Create a service account for Cloud Run function

The Cloud Run function needs a service account with permissions to write to GCS bucket and be invoked by Pub/Sub.

### Create the service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `sap-sf-logs-collector-sa`
     * **Service account description** : Enter `Service account for Cloud Run function to collect SAP SuccessFactors logs`
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
  2. Click on your bucket name (for example, `sap-successfactors-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `sap-sf-logs-collector-sa@PROJECT_ID.iam.gserviceaccount.com`)
     * **Assign roles** : Select **Storage Object Admin**
  6. Click **Save**.



## Create Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `sap-sf-logs-trigger`
     * Leave other settings as default
  4. Click **Create**.



## Create Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from SAP SuccessFactors OData API and write them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `sap-sf-logs-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose the topic `sap-sf-logs-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select the service account `sap-sf-logs-collector-sa`.
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `sap-successfactors-logs` | GCS bucket name  
`GCS_PREFIX` | `sf-logs` | Prefix for log files  
`STATE_KEY` | `sf-logs/state.json` | State file path  
`SF_API_SERVER` | `https://api15.sapsf.com` | SAP SuccessFactors API server URL  
`SF_USERNAME` | `USERNAME@COMPANY_ID` | SAP SuccessFactors username  
`SF_PASSWORD` | `your-password` | SAP SuccessFactors password  
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

     * First file **main.py** :
           
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
           GCS_PREFIX = os.environ.get('GCS_PREFIX', 'sf-logs')
           STATE_KEY = os.environ.get('STATE_KEY', 'sf-logs/state.json')
           SF_API_SERVER = os.environ.get('SF_API_SERVER')
           SF_USERNAME = os.environ.get('SF_USERNAME')
           SF_PASSWORD = os.environ.get('SF_PASSWORD')
           MAX_RECORDS = int(os.environ.get('MAX_RECORDS', '5000'))
           PAGE_SIZE = int(os.environ.get('PAGE_SIZE', '1000'))
           LOOKBACK_HOURS = int(os.environ.get('LOOKBACK_HOURS', '24'))
           
           def parse_datetime(value: str) -> datetime:
             """Parse ISO datetime string to datetime object."""
             if [value](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.ObjectCustomContextPayload.html#google_cloud_storage_blob_ObjectCustomContextPayload_value).endswith("Z"):
               value = value[:-1] + "+00:00"
             return datetime.fromisoformat(value)
           
           @functions_framework.cloud_event
           def main(cloud_event):
             """
             Cloud Run function triggered by Pub/Sub to fetch SAP SuccessFactors
             audit logs and write to GCS.
           
             Args:
               cloud_event: CloudEvent object containing Pub/Sub message
             """
           
             if not all([GCS_BUCKET, SF_API_SERVER, SF_USERNAME, SF_PASSWORD]):
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
                 api_server=SF_API_SERVER,
                 username=SF_USERNAME,
                 password=SF_PASSWORD,
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
           
           def fetch_logs(api_server: str, username: str, password: str, start_time: datetime, end_time: datetime, page_size: int, max_records: int):
             """
             Fetch audit trail logs from SAP SuccessFactors OData API with
             pagination and rate limiting.
           
             Args:
               api_server: SAP SuccessFactors API server URL
               username: SAP SuccessFactors username (USERNAME@COMPANY_ID)
               password: SAP SuccessFactors password
               start_time: Start time for log query
               end_time: End time for log query
               page_size: Number of records per page
               max_records: Maximum total records to fetch
           
             Returns:
               Tuple of (records list, newest_event_time ISO string)
             """
             base_url = api_server.rstrip('/')
           
             # Build Basic Auth header
             auth_string = f"{username}:{password}"
             auth_bytes = auth_string.encode('utf-8')
             auth_b64 = base64.b64encode(auth_bytes).decode('utf-8')
           
             headers = {
               'Authorization': f'Basic {auth_b64}',
               'Accept': 'application/json',
               'User-Agent': 'GoogleSecOps-SAPSFCollector/1.0'
             }
           
             records = []
             newest_time = None
             page_num = 0
             backoff = 1.0
             skip = 0
           
             # Format datetime for OData filter
             start_str = start_time.strftime("%Y-%m-%dT%H:%M:%S")
             end_str = end_time.strftime("%Y-%m-%dT%H:%M:%S")
           
             while True:
               page_num += 1
           
               if len(records) >= max_records:
                 print(f"Reached max_records limit ({max_records})")
                 break
           
               remaining = min(page_size, max_records - len(records))
               url = (
                 f"{base_url}/odata/v2/AuditTrail"
                 f"?$filter=changedDate ge datetime'{start_str}' and changedDate le datetime'{end_str}'"
                 f"&$top={remaining}"
                 f"&$skip={skip}"
                 f"&$format=json"
               )
           
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
           
                 # OData response structure
                 page_results = data.get('d', {}).get('results', [])
           
                 if not page_results:
                   print(f"No more results (empty page)")
                   break
           
                 print(f"Page {page_num}: Retrieved {len(page_results)} events")
                 records.extend(page_results)
           
                 # Track newest event time
                 for event in page_results:
                   try:
                     changed_date = event.get('changedDate', '')
                     # OData datetime format: /Date(1234567890000)/
                     if changed_date and changed_date.startswith('/Date('):
                       ms = int(changed_date.split('(')[1].split(')')[0].split('+')[0].split('-')[0])
                       event_dt = datetime.fromtimestamp(ms / 1000, tz=timezone.utc)
                       event_time = event_dt.isoformat()
                       if newest_time is None or parse_datetime(event_time) > parse_datetime(newest_time):
                         newest_time = event_time
                   except Exception as e:
                     print(f"Warning: Could not parse event time: {e}")
           
                 # Check for more results
                 if len(page_results) < remaining:
                   print(f"Reached last page (size={len(page_results)} < limit={remaining})")
                   break
           
                 skip += len(page_results)
           
               except Exception as e:
                 print(f"Error fetching logs: {e}")
                 return [], None
           
             print(f"Retrieved {len(records)} total records from {page_num} pages")
             return records, newest_time
           

     * Second file **requirements.txt** :
           
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
**Name** | `sap-sf-logs-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the topic `sap-sf-logs-trigger`  
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
  5. Click on `sap-sf-logs-collector`.
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         Fetching logs from YYYY-MM-DDTHH:MM:SS+00:00 to YYYY-MM-DDTHH:MM:SS+00:00
         Page 1: Retrieved X events
         Wrote X records to gs://sap-successfactors-logs/sf-logs/logs_YYYYMMDD_HHMMSS.ndjson
         Successfully processed X records
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click on your bucket name (`sap-successfactors-logs`).

  10. Navigate to the `sf-logs/` folder.

  11. Verify that a new `.ndjson` file was created with the current timestamp.




If you see errors in the logs: \- **HTTP 401** : Check API credentials in environment variables \- **HTTP 403** : Verify account has required permissions in SAP SuccessFactors \- **HTTP 429** : Rate limiting - function will automatically retry with backoff \- **Missing environment variables** : Check all required variables are set

## Configure a feed in Google SecOps to ingest SAP SuccessFactors logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `SAP SuccessFactors Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **SAP SuccessFactors** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address.

**Note:** Each Google SecOps instance has a unique service account. Do not use service accounts from other documentation or examples.
  9. Click **Next**.

  10. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://sap-successfactors-logs/sf-logs/
           

       * Replace: 
         * `sap-successfactors-logs`: Your GCS bucket name.
         * `sf-logs`: Optional prefix/folder path where logs are stored (leave empty for root).
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
module, functional_area, functional_sub_area, context_1_value, context_2_value, context_3_value, context_4_value, context_5_value, new_value, old_value, operation_performed, effective_start_date, effective_sequence | additional.fields | Tokens created from each field and merged if not empty and conditions met  
changed_by_user_first_name | intermediary_1.user.first_name | Value copied directly if not empty and secondary user present  
changed_by_user_last_name | intermediary_1.user.last_name | Value copied directly if not empty and secondary user present  
changed_by_user_username | intermediary_1.user.userid | Value copied directly if not empty and secondary user present  
proxy_user_first_name | intermediary_2.user.first_name | Value copied directly if not empty  
proxy_user_last_name | intermediary_2.user.last_name | Value copied directly if not empty  
proxy_user_username | intermediary_2.user.userid | Value copied directly if not empty  
| metadata.event_type | Set to "GENERIC_EVENT", overridden to "USER_RESOURCE_ACCESS" if context_1_key == "Role" or field_name == "Role", or "RESOURCE_PERMISSIONS_CHANGE" if subject user fields present and changed_by_user_username not present  
new_value | permission.name | Value copied from new_value if field_name == "Permission"  
secondary_user_email | principal.user.email_addresses | Value copied directly if not empty  
secondary_user_provisioner_id | principal.user.userid | Value copied directly if not empty  
context_1_value, new_value | role.name | Value from context_1_value if context_1_key == "Role"; otherwise from new_value if field_name == "Role name" or "Role"  
old_value, new_value | target.group.attribute.labels | Merged with tokens from old_value or new_value based on field_name  
context_1_value, new_value | target.group.group_display_name | Value from context_1_value if context_1_key == "Group"; otherwise from new_value if field_name == "Group" or "Group name"  
context_3_value | target.resource.name | Value copied from context_3_value if context_3_key == "Feature Name"  
context_2_value | target.resource.product_object_id | Value copied from context_2_value if context_2_key == "Feature Id"  
old_value, new_value | target.user.attribute.labels | Merged with tokens from old_value or new_value based on field_name  
new_value | target.user.attribute.permissions | Merged with permission object created from new_value if field_name == "Permission"  
context_1_value, new_value | target.user.attribute.roles | Merged with role object created from context_1_value if context_1_key == "Role", or from new_value if field_name == "Role name" or "Role"  
subject_user_first_name, first_name, first_name | target.user.first_name | Value from subject_user_first_name if not empty; otherwise extracted from context_1_value using grok if context_1_key == "Proxy Rights For"; otherwise extracted from context_2_value using grok if context_2_key == "User name"  
subject_user_last_name, last_name, last_name | target.user.last_name | Value from subject_user_last_name if not empty; otherwise extracted from context_1_value using grok if context_1_key == "Proxy Rights For"; otherwise extracted from context_2_value using grok if context_2_key == "User name"  
subject_user_id, context_1_value | target.user.userid | Value from subject_user_id if not empty; otherwise from context_1_value if context_1_key == "User"  
| metadata.product_name | Set to "SuccessFactors"  
| metadata.vendor_name | Set to "SAP"  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sap-successfactors-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
