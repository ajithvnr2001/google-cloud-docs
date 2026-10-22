---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/nagios/
title: Collect Nagios XI logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:55:57.422536+00:00
---

# Collect Nagios XI logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/nagios/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Nagios XI logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

**Note:** This feature is covered by [Pre-GA Offerings Terms](https://chronicle.security/legal/service-terms/) of the Google Security Operations Service Specific Terms. Pre-GA features might have limited support, and changes to pre-GA features might not be compatible with other pre-GA versions. For more information, see the [Google SecOps Technical Support Service guidelines](https://chronicle.security/legal/technical-support-services-guidelines/) and the [Google SecOps Service Specific Terms](https://chronicle.security/legal/service-terms/).  
If this feature isn't visible in your environment, see [Manage preview features](https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage) or contact your system administrator.

This document explains how to ingest Nagios XI logs to Google Security Operations using Google Cloud Storage V2.

Nagios XI is a comprehensive infrastructure monitoring solution that provides monitoring of servers, networks, applications, and services. It tracks host and service status, performance metrics, and generates alerts for IT infrastructure issues through its REST API.

## Before you begin

Ensure that you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage, Cloud Run, Pub/Sub, and Cloud Scheduler APIs enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * Privileged access to Nagios XI with user management permissions
  * Nagios XI version 5 or later (REST API support)



## Configure Nagios XI API access

To enable Google SecOps to retrieve monitoring data, you need to create a user account with API access and read-only permissions.

### Create a read-only user with API access

  1. Sign in to the **Nagios XI** web interface with administrator privileges.
  2. Go to **Admin > Manage Users**.
  3. Click **Add New User**.
  4. Provide the following configuration details: 
     * **Username** : Enter a descriptive name (for example, `chronicle-integration`)
     * **Password** : Enter a secure password
     * **Name** : Enter `Chronicle Integration User`
     * **Email Address** : Enter a valid email address
  5. In the **Security Settings** section, configure the following: 
     * **Authorization Level** : Select **User**
     * **Can see all hosts and services** : Check this option
     * **Read-only access** : Check this option
     * **API access** : Check this option
  6. Uncheck the following options: 
     * **Force Password Change at Next Login**
     * **Email User Account Information**
     * **Create as Monitoring Contact**
  7. Ensure **Account Enabled** is checked.
  8. Click **Add User**.



### Retrieve the API key

  1. In the **Manage Users** page, click on the user account (`chronicle-integration`).
  2. In the user account settings page, locate the **API Key** field.
  3. Copy the API key value.

**Note:** Each user has a unique API key. If you need to regenerate the API key, click **Generate new API key** in the user account settings. The old API key will be invalidated immediately.**Note:** Store the API key securely. It provides read access to all monitoring data in Nagios XI.



### Verify permissions

To verify the account has the required permissions:

  1. Sign in to **Nagios XI** with the `chronicle-integration` user account.
  2. Go to **Home > Host Status**.
  3. If you can see all monitored hosts and services, you have the required permissions.
  4. If you cannot see hosts or services, contact your administrator to grant **Can see all hosts and services** permission.



### Test API access

  * Test your credentials before proceeding with the integration:
        
        # Replace with your actual values
        NAGIOS_HOST="https://your-nagios-server.example.com"
        API_KEY="your-api-key"
        
        # Test API access - query host status
        curl -k "${NAGIOS_HOST}/nagiosxi/api/v1/objects/hoststatus?apikey=${API_KEY}&pretty=1"
        

A successful response returns a JSON object containing host status information.




## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `nagios-xi-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Create service account for Cloud Run function

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `nagios-logs-collector-sa`
     * **Service account description** : Enter `Service account for Cloud Run function to collect Nagios XI logs`
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



### Grant IAM permissions on GCS bucket

  1. Go to **Cloud Storage > Buckets**.
  2. Click on your bucket name (`nagios-xi-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (`nagios-logs-collector-sa@PROJECT_ID.iam.gserviceaccount.com`)
     * **Assign roles** : Select **Storage Object Admin**
  6. Click **Save**.



## Create Pub/Sub topic

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `nagios-logs-trigger`
     * Leave other settings as default
  4. Click **Create**.



## Create Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from the Nagios XI REST API and write them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `nagios-logs-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose `nagios-logs-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select `nagios-logs-collector-sa`
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `nagios-xi-logs` | GCS bucket name  
`GCS_PREFIX` | `nagios-xi` | Prefix for log files  
`STATE_KEY` | `nagios-xi/state.json` | State file path  
`NAGIOS_BASE_URL` | `https://your-nagios-server.example.com` | Nagios XI base URL  
`NAGIOS_API_KEY` | `your-api-key` | Nagios XI API key  
`MAX_RECORDS` | `1000` | Max records per endpoint per run  
`PAGE_SIZE` | `200` | Records per API page  
`LOOKBACK_HOURS` | `24` | Initial lookback period  
  10. In the **Variables & Secrets** section, scroll down to **Requests** :

     * **Request timeout** : Enter `600` seconds (10 minutes)
  11. Go to the **Settings** tab:

     * In the **Resources** section: 
       * **Memory** : Select **512 MiB** or higher
       * **CPU** : Select **1**
  12. In the **Revision scaling** section:

     * **Minimum number of instances** : Enter `0`
     * **Maximum number of instances** : Enter `100`
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
           
           http = urllib3.PoolManager(
             timeout=urllib3.Timeout(connect=5.0, read=30.0),
             retries=False,
           )
           
           storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
           
           GCS_BUCKET = os.environ.get('GCS_BUCKET')
           GCS_PREFIX = os.environ.get('GCS_PREFIX', 'nagios-xi')
           STATE_KEY = os.environ.get('STATE_KEY', 'nagios-xi/state.json')
           NAGIOS_BASE_URL = os.environ.get('NAGIOS_BASE_URL', '').rstrip('/')
           NAGIOS_API_KEY = os.environ.get('NAGIOS_API_KEY')
           MAX_RECORDS = int(os.environ.get('MAX_RECORDS', '1000'))
           PAGE_SIZE = int(os.environ.get('PAGE_SIZE', '200'))
           LOOKBACK_HOURS = int(os.environ.get('LOOKBACK_HOURS', '24'))
           
           ENDPOINTS = [
             'hoststatus',
             'servicestatus',
             'statehistory',
             'logentries',
           ]
           
           @functions_framework.cloud_event
           def main(cloud_event):
             if not all([GCS_BUCKET, NAGIOS_BASE_URL, NAGIOS_API_KEY]):
               print('Error: Missing required environment variables')
               return
           
             try:
               bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(GCS_BUCKET)
               state = load_state(bucket)
               now = datetime.now(timezone.utc)
           
               if isinstance(state, dict) and [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get('last_event_time'):
                 try:
                   last_val = state['last_event_time']
                   if last_val.endswith('Z'):
                     last_val = last_val[:-1] + '+00:00'
                   last_time = datetime.fromisoformat(last_val)
                   last_time = last_time - timedelta(minutes=2)
                 except Exception as e:
                   print(f"Warning: Could not parse last_event_time: {e}")
                   last_time = now - timedelta(hours=LOOKBACK_HOURS)
               else:
                 last_time = now - timedelta(hours=LOOKBACK_HOURS)
           
               print(f"Fetching logs from {last_time.isoformat()} to {now.isoformat()}")
           
               start_ts = int(last_time.timestamp())
               end_ts = int(now.timestamp())
           
               all_records = []
               newest_time = None
           
               for endpoint in ENDPOINTS:
                 records, endpoint_newest = fetch_nagios_endpoint(
                   endpoint, start_ts, end_ts
                 )
                 for record in records:
                   record['_nagios_endpoint'] = endpoint
                 all_records.extend(records)
           
                 if endpoint_newest:
                   if newest_time is None or endpoint_newest > newest_time:
                     newest_time = endpoint_newest
           
               if not all_records:
                 print("No new records found.")
                 save_state(bucket, now.isoformat())
                 return
           
               timestamp = now.strftime('%Y%m%d_%H%M%S')
               object_key = f"{GCS_PREFIX}/nagios_logs_{timestamp}.ndjson"
               blob = bucket.blob(object_key)
           
               ndjson = '\n'.join(
                 [json.dumps(r, ensure_ascii=False, default=str) for r in all_records]
               ) + '\n'
               blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(ndjson, content_type='application/x-ndjson')
           
               print(f"Wrote {len(all_records)} records to gs://{GCS_BUCKET}/{object_key}")
           
               if newest_time:
                 save_state(bucket, newest_time)
               else:
                 save_state(bucket, now.isoformat())
           
               print(f"Successfully processed {len(all_records)} records")
           
             except Exception as e:
               print(f'Error processing logs: {str(e)}')
               raise
           
           def fetch_nagios_endpoint(endpoint, start_ts, end_ts):
             base_url = f"{NAGIOS_BASE_URL}/nagiosxi/api/v1/objects/{endpoint}"
           
             records = []
             newest_time = None
             start_index = 0
             page_num = 0
             backoff = 1.0
           
             while True:
               page_num += 1
           
               if len(records) >= MAX_RECORDS:
                 print(f"{endpoint}: Reached max_records limit ({MAX_RECORDS})")
                 break
           
               remaining = min(PAGE_SIZE, MAX_RECORDS - len(records))
               params = [
                 f"apikey={NAGIOS_API_KEY}",
                 f"starttime={start_ts}",
                 f"endtime={end_ts}",
                 f"records={remaining}",
                 f"start={start_index}",
               ]
               url = f"{base_url}?{'&'.join(params)}"
           
               try:
                 response = http.request('GET', url)
           
                 if response.status == 429:
                   retry_after = int(response.headers.get('Retry-After', str(int(backoff))))
                   print(f"{endpoint}: Rate limited (429). Retrying after {retry_after}s...")
                   time.sleep(retry_after)
                   backoff = min(backoff * 2, 30.0)
                   continue
           
                 backoff = 1.0
           
                 if response.status != 200:
                   print(f"{endpoint}: HTTP Error {response.status}")
                   response_text = response.data.decode('utf-8')
                   print(f"Response body: {response_text}")
                   break
           
                 data = json.loads(response.data.decode('utf-8'))
           
                 record_count = data.get('recordcount', 0)
                 result_key = get_result_key(endpoint)
                 page_results = data.get(result_key, [])
           
                 if not page_results:
                   print(f"{endpoint}: No more results at offset {start_index}")
                   break
           
                 print(f"{endpoint} page {page_num}: Retrieved {len(page_results)} events")
                 records.extend(page_results)
           
                 for event in page_results:
                   try:
                     event_time = event.get('state_time') or event.get('status_update_time') or event.get('entry_time')
                     if event_time:
                       if newest_time is None or event_time > newest_time:
                         newest_time = event_time
                   except Exception as e:
                     print(f"Warning: Could not parse event time: {e}")
           
                 if len(page_results) < remaining:
                   print(f"{endpoint}: Reached last page (returned {len(page_results)} < {remaining})")
                   break
           
                 start_index += len(page_results)
           
               except Exception as e:
                 print(f"{endpoint}: Error fetching logs: {e}")
                 break
           
             print(f"{endpoint}: Retrieved {len(records)} total records from {page_num} pages")
             return records, newest_time
           
           def get_result_key(endpoint):
             key_map = {
               'hoststatus': 'hoststatus',
               'servicestatus': 'servicestatus',
               'statehistory': 'statehistory',
               'logentries': 'logentry',
             }
             return key_map.get(endpoint, endpoint)
           
           def load_state(bucket):
             try:
               blob = bucket.blob(STATE_KEY)
               if blob.exists():
                 return json.loads(blob.[download_as_text](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_download_as_text)())
             except Exception as e:
               print(f"Warning: Could not load state: {e}")
             return {}
           
           def save_state(bucket, last_event_time_iso):
             try:
               state = {
                 'last_event_time': last_event_time_iso,
                 'last_run': datetime.now(timezone.utc).isoformat()
               }
               blob = bucket.blob(STATE_KEY)
               blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
                 json.dumps(state, indent=2),
                 content_type='application/json'
               )
               print(f"Saved state: last_event_time={last_event_time_iso}")
             except Exception as e:
               print(f"Warning: Could not save state: {e}")
           

     * **requirements.txt:**
           
           functions-framework==3.*
           google-cloud-storage==2.*
           urllib3>=2.0.0
           

  3. Click **Deploy** to save and deploy the function.

  4. Wait for deployment to complete (2-3 minutes).

**Note:** The Pub/Sub trigger configuration automatically creates the necessary subscriptions and permissions.



## Create Cloud Scheduler job

  1. In the **GCP Console** , go to **Cloud Scheduler**.
  2. Click **Create Job**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | `nagios-logs-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select `nagios-logs-trigger`  
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

  1. In the **Cloud Scheduler** console, find your job (`nagios-logs-collector-hourly`).
  2. Click **Force run** to trigger the job manually.
  3. Wait a few seconds.
  4. Go to **Cloud Run > Services**.
  5. Click on `nagios-logs-collector`.
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         Fetching logs from YYYY-MM-DDTHH:MM:SS+00:00 to YYYY-MM-DDTHH:MM:SS+00:00
         hoststatus page 1: Retrieved X events
         servicestatus page 1: Retrieved X events
         statehistory page 1: Retrieved X events
         logentries page 1: Retrieved X events
         Wrote X records to gs://nagios-xi-logs/nagios-xi/nagios_logs_YYYYMMDD_HHMMSS.ndjson
         Successfully processed X records
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click on `nagios-xi-logs`.

  10. Navigate to the `nagios-xi/` folder.

  11. Verify that a new `.ndjson` file was created with the current timestamp.




If you see errors in the logs:

  * **HTTP 401** : Verify the `NAGIOS_API_KEY` environment variable is correct and the user has **API access** enabled
  * **HTTP 403** : Verify the user account has **Can see all hosts and services** permission
  * **HTTP 429** : Rate limiting -- the function will automatically retry with backoff
  * **Missing environment variables** : Verify all required variables are set in the Cloud Run function configuration



## Retrieve the Google SecOps service account

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Nagios XI Logs GCS`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Nagios** as the **Log type**.
  7. Click **Get Service Account**.
  8. A unique service account email is displayed. For example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  9. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Don't use service accounts from other documentation or examples.
  10. Click **Next**.

  11. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://nagios-xi-logs/nagios-xi/
           

**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never** : Never deletes any files after transfers (recommended for testing).
       * **Delete transferred files** : Deletes files after successful transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.

**Note:** If you select a deletion option, the service account must have **Storage Object Admin** role instead of Storage Object Viewer. Update IAM permissions accordingly.
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days)

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)

     * **Ingestion labels** : The label to be applied to the events from this feed

  12. Click **Next**.

  13. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## Grant IAM permissions to the Google SecOps service account

  1. Go to **Cloud Storage > Buckets**.
  2. Click on `nagios-xi-logs`.
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
src_ip | has_principal | Set to "true" if merge of src_ip to principal.ip and principal.asset.ip succeeds  
src_ip | principal.asset.ip | Value copied directly  
src_ip | principal.ip | Value copied directly  
jobid | jobid_label.key | Set to "Jobid"  
jobid | jobid_label.value | Value copied directly  
jobid_label | principal.resource.attribute.labels | Merged from jobid_label  
pid | principal.process.pid | Value copied directly  
ent | metadata.product_event_type | Value copied directly  
description | metadata.description | Value copied directly  
msg_ip | has_target | Set to "true" if merge of msg_ip to target.ip and target.asset.ip succeeds  
msg_ip | target.asset.ip | Value copied directly  
msg_ip | target.ip | Value copied directly  
port | target.port | Value copied directly and converted to integer  
column1 | principal.asset.hostname | Value from column1 if ent == "SERVICE ALERT", else from column2 if ent == "SERVICE NOTIFICATION"  
column1 | principal.hostname | Value from column1 if ent == "SERVICE ALERT", else from column2 if ent == "SERVICE NOTIFICATION"  
column1 | principal.user.user_display_name | Value copied directly if ent == "SERVICE NOTIFICATION"  
column2 | security_result.summary | Value from column3 if ent == "SERVICE ALERT" and column2 not empty, else from column3 if ent == "SERVICE NOTIFICATION"  
column3 | security_result.summary | Value from column3 if ent == "SERVICE ALERT" and column3 not empty, else from column3 if ent == "SERVICE NOTIFICATION"  
column4 | security_result.severity | Value copied directly if column4 in ["LOW", "MEDIUM", "HIGH", "CRITICAL"] and ent in ["SERVICE NOTIFICATION", "SERVICE ALERT"]  
column4 | security_result.severity_details | Value copied directly if column4 not in ["LOW", "MEDIUM", "HIGH", "CRITICAL"] and ent in ["SERVICE NOTIFICATION", "SERVICE ALERT"]  
has_principal | metadata.event_type | Set to "NETWORK_CONNECTION" if has_principal and has_target true, else "STATUS_UPDATE" if has_principal true, else "USER_UNCATEGORIZED" if has_principal_user true, else "GENERIC_EVENT"  
has_target | metadata.event_type |   
has_principal_user | metadata.event_type |   
security_result | event.idm.read_only_udm.security_result | Merged from security_result  
metadata | event.idm.read_only_udm.metadata | Renamed from metadata  
target | event.idm.read_only_udm.target | Renamed from target  
principal | event.idm.read_only_udm.principal | Renamed from principal  
network | event.idm.read_only_udm.network | Renamed from network  
metadata.product_name | metadata.product_name | Set to "NAGIOS"  
metadata.vendor_name | metadata.vendor_name | Set to "NAGIOS"  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/nagios-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
