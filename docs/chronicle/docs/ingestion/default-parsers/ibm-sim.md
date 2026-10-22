---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ibm-sim/
title: Collect IBM Security Identity Manager logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:34:01.529344+00:00
---

# Collect IBM Security Identity Manager logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ibm-sim/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect IBM Security Identity Manager logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest IBM Security Identity Manager logs into Google Security Operations using Google Cloud Storage V2.

IBM Security Identity Manager (ISIM) is an automated and policy-based solution that manages user access across IT environments, helping to drive effective identity management and governance across the enterprise. By using roles, accounts, and access permissions, it automates the creation, modification, recertification, and termination of user identities throughout the user lifecycle. The product is also known as IBM Security Verify Governance - Identity Manager in newer versions.

## Before you begin

Ensure that you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * Privileged access to IBM Security Identity Manager REST API
  * IBM Security Identity Manager version 7.0.2 or later, or IBM Security Verify Governance 10.0.1 or later
  * An ISIM user account with administrative privileges to access the REST API endpoints (`/itim/rest/activities` and `/itim/rest/requests`)
  * Network connectivity between the GCP project and the ISIM virtual appliance (firewall rules must allow HTTPS traffic on the ISIM port)



## Configure IBM Security Identity Manager API access

To enable Google SecOps to retrieve activity and request audit data, you need to configure a dedicated service account in ISIM with the required permissions for REST API access.

### Create a dedicated ISIM account for API access

  1. Sign in to the **IBM Security Identity Manager** administration console.
  2. Go to **Manage Users > Create User**.
  3. Create a new user account for the integration (for example, `secops-api-user`).
  4. Assign the **System Administrator** role or a custom role that includes permissions to view activities and requests through the REST API.
  5. Save the account credentials securely: 
     * **Username** : The ISIM login username (for example, `secops-api-user`)
     * **Password** : The ISIM login password



### Identify your ISIM API base URL

  * Your ISIM API base URL follows this format:
        
        https://<isim-hostname>:<port>
        

  * For example, if your ISIM virtual appliance hostname is `isim.example.com` and it uses the default HTTPS port:
        
        https://isim.example.com:9082
        

**Note:** The default port for ISIM is typically `9082` for HTTPS. Consult your ISIM administrator if you are unsure of the correct hostname and port.



### Test API access

  * Test your credentials before proceeding with the integration:
        
        # Replace with your actual credentials and ISIM URL
        ISIM_BASE_URL="https://isim.example.com:9082"
        ISIM_USER="chronicle-api-user"
        ISIM_PASS="your-password"
        
        # Authenticate and obtain session cookie
        curl -v -k -c cookies.txt \
            -d "j_username=${ISIM_USER}&j_password=${ISIM_PASS}" \
            "${ISIM_BASE_URL}/itim/j_security_check"
        
        # Retrieve CSRF token from systemusers/me endpoint
        curl -v -k -b cookies.txt \
            -H "Accept: application/json" \
            "${ISIM_BASE_URL}/itim/rest/systemusers/me"
        
        # Test activities endpoint
        curl -v -k -b cookies.txt \
            -H "Accept: application/json" \
            "${ISIM_BASE_URL}/itim/rest/activities"
        




A successful response returns a JSON array of recent ISIM activities.

## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `ibm-sim-logs-gcs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Create service account for Cloud Run function

The Cloud Run function needs a service account with permissions to write to GCS bucket and be invoked by Pub/Sub.

### Create service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `ibm-sim-collector-sa`
     * **Service account description** : Enter `Service account for Cloud Run function to collect IBM Security Identity Manager logs`
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
  2. Click on your bucket name (`ibm-sim-logs-gcs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (`ibm-sim-collector-sa@PROJECT_ID.iam.gserviceaccount.com`)
     * **Assign roles** : Select **Storage Object Admin**
  6. Click **Save**.



## Create Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `ibm-sim-logs-trigger`
     * Leave other settings as default
  4. Click **Create**.



## Create Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from the IBM Security Identity Manager REST API and write them to GCS.

To create Cloud Run function to collect logs, do the following:

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `ibm-sim-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose `ibm-sim-logs-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select `ibm-sim-collector-sa`
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:

Variable name | Example value | Description  
---|---|---  
`GCS_BUCKET` | `ibm-sim-logs-gcs` | GCS bucket name  
`GCS_PREFIX` | `ibm-sim` | Prefix for log files  
`STATE_KEY` | `ibm-sim/state.json` | State file path  
`ISIM_BASE_URL` | `https://isim.example.com:9082` | ISIM server base URL  
`ISIM_USERNAME` | `secops-api-user` | ISIM API username  
`ISIM_PASSWORD` | `your-password` | ISIM API password  
`LOOKBACK_HOURS` | `24` | Initial lookback period  
`PAGE_SIZE` | `100` | Records per API page  
`MAX_RECORDS` | `5000` | Max records per run  
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
           import urllib.parse
           from datetime import datetime, timezone, timedelta
           
           # Disable SSL warnings for self-signed certificates
           urllib3.disable_warnings(urllib3.[exceptions](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.exceptions.html).InsecureRequestWarning)
           
           http = urllib3.PoolManager(
               timeout=urllib3.Timeout(connect=10.0, read=60.0),
               retries=False,
               cert_reqs='CERT_NONE',
           )
           
           storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
           
           GCS_BUCKET = os.environ.get('GCS_BUCKET')
           GCS_PREFIX = os.environ.get('GCS_PREFIX', 'ibm-sim')
           STATE_KEY = os.environ.get('STATE_KEY', 'ibm-sim/state.json')
           ISIM_BASE_URL = os.environ.get('ISIM_BASE_URL', '').rstrip('/')
           ISIM_USERNAME = os.environ.get('ISIM_USERNAME')
           ISIM_PASSWORD = os.environ.get('ISIM_PASSWORD')
           LOOKBACK_HOURS = int(os.environ.get('LOOKBACK_HOURS', '24'))
           PAGE_SIZE = int(os.environ.get('PAGE_SIZE', '100'))
           MAX_RECORDS = int(os.environ.get('MAX_RECORDS', '5000'))
           
           @functions_framework.cloud_event
           def main(cloud_event):
               if not all([GCS_BUCKET, ISIM_BASE_URL, ISIM_USERNAME, ISIM_PASSWORD]):
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
           
                   session_cookies = authenticate()
                   csrf_token = get_csrf_token(session_cookies)
           
                   activities = fetch_activities(session_cookies, csrf_token, last_time, now)
                   requests_data = fetch_requests(session_cookies, csrf_token, last_time, now)
           
                   all_records = []
                   for a in activities:
                       a['_isim_record_type'] = 'activity'
                       all_records.append(a)
                   for r in requests_data:
                       r['_isim_record_type'] = 'request'
                       all_records.append(r)
           
                   if not all_records:
                       print("No new records found.")
                       save_state(bucket, now.isoformat())
                       return
           
                   timestamp = now.strftime('%Y%m%d_%H%M%S')
                   object_key = f"{GCS_PREFIX}/ibm_sim_audit_{timestamp}.ndjson"
                   blob = bucket.blob(object_key)
           
                   ndjson = '\n'.join(
                       [json.dumps(r, ensure_ascii=False, default=str) for r in all_records]
                   ) + '\n'
                   blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(ndjson, content_type='application/x-ndjson')
           
                   print(f"Wrote {len(all_records)} records to gs://{GCS_BUCKET}/{object_key}")
           
                   newest = find_newest_time(all_records)
                   save_state(bucket, newest if newest else now.isoformat())
           
                   print(f"Successfully processed {len(all_records)} records "
                       f"(activities: {len(activities)}, requests: {len(requests_data)})")
           
               except Exception as e:
                   print(f'Error processing logs: {str(e)}')
                   raise
           
           def authenticate():
               url = f"{ISIM_BASE_URL}/itim/j_security_check"
               encoded_body = urllib.parse.urlencode({
                   'j_username': ISIM_USERNAME,
                   'j_password': ISIM_PASSWORD
               }).encode('utf-8')
           
               response = http.request(
                   'POST', url,
                   body=encoded_body,
                   headers={'Content-Type': 'application/x-www-form-urlencoded'},
                   redirect=False
               )
           
               cookies = {}
               set_cookie_headers = response.headers.getlist('Set-Cookie') if hasattr(response.headers, 'getlist') else []
               if not set_cookie_headers:
                   raw = response.headers.get('Set-Cookie', '')
                   if raw:
                       set_cookie_headers = [raw]
           
               for cookie_header in set_cookie_headers:
                   parts = cookie_header.split(';')[0]
                   if '=' in parts:
                       name, value = parts.split('=', 1)
                       cookies[name.strip()] = [value](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.ObjectCustomContextPayload.html#google_cloud_storage_blob_ObjectCustomContextPayload_value).strip()
           
               if not cookies:
                   raise Exception(
                       f"Authentication failed: no session cookies returned "
                       f"(HTTP {response.status})"
                   )
           
               print("Successfully authenticated to ISIM")
               return cookies
           
           def get_csrf_token(cookies):
               url = f"{ISIM_BASE_URL}/itim/rest/systemusers/me"
               cookie_str = '; '.join([f"{k}={v}" for k, v in cookies.items()])
           
               response = http.request(
                   'GET', url,
                   headers={
                       'Accept': 'application/json',
                       'Cookie': cookie_str
                   }
               )
           
               if response.status != 200:
                   raise Exception(
                       f"Failed to get CSRF token: {response.status} - "
                       f"{response.data.decode('utf-8')}"
                   )
           
               data = json.loads(response.data.decode('utf-8'))
               csrf_token = None
           
               if isinstance(data, dict):
                   csrf_token = data.get('_csrf', data.get('CSRFToken'))
               if not csrf_token:
                   csrf_header = response.headers.get('CSRFToken', '')
                   if csrf_header:
                       csrf_token = csrf_header
           
               print("Successfully retrieved CSRF token")
               return csrf_token
           
           def fetch_activities(cookies, csrf_token, start_time, end_time):
               url = f"{ISIM_BASE_URL}/itim/rest/activities"
               cookie_str = '; '.join([f"{k}={v}" for k, v in cookies.items()])
           
               headers = {
                   'Accept': 'application/json',
                   'Cookie': cookie_str
               }
               if csrf_token:
                   headers['CSRFToken'] = csrf_token
           
               all_records = []
               start_index = 0
           
               while len(all_records) < MAX_RECORDS:
                   params = {
                       '_start': str(start_index),
                       '_count': str(min(PAGE_SIZE, MAX_RECORDS - len(all_records)))
                   }
                   query_string = urllib.parse.urlencode(params)
                   request_url = f"{url}?{query_string}"
           
                   response = http.request('GET', request_url, headers=headers)
           
                   if response.status != 200:
                       print(f"Activities query failed: {response.status} - "
                           f"{response.data.decode('utf-8')}")
                       break
           
                   page_results = json.loads(response.data.decode('utf-8'))
           
                   if isinstance(page_results, dict):
                       page_results = page_results.get('activities', page_results.get('items', []))
           
                   if not page_results:
                       break
           
                   all_records.extend(page_results)
                   print(f"Activities: Retrieved {len(page_results)} records "
                       f"(total: {len(all_records)})")
           
                   if len(page_results) < PAGE_SIZE:
                       break
           
                   start_index += len(page_results)
           
               print(f"Total activities fetched: {len(all_records)}")
               return all_records
           
           def fetch_requests(cookies, csrf_token, start_time, end_time):
               url = f"{ISIM_BASE_URL}/itim/rest/requests"
               cookie_str = '; '.join([f"{k}={v}" for k, v in cookies.items()])
           
               headers = {
                   'Accept': 'application/json',
                   'Cookie': cookie_str
               }
               if csrf_token:
                   headers['CSRFToken'] = csrf_token
           
               all_records = []
               start_index = 0
           
               while len(all_records) < MAX_RECORDS:
                   params = {
                       '_start': str(start_index),
                       '_count': str(min(PAGE_SIZE, MAX_RECORDS - len(all_records)))
                   }
                   query_string = urllib.parse.urlencode(params)
                   request_url = f"{url}?{query_string}"
           
                   response = http.request('GET', request_url, headers=headers)
           
                   if response.status != 200:
                       print(f"Requests query failed: {response.status} - "
                           f"{response.data.decode('utf-8')}")
                       break
           
                   page_results = json.loads(response.data.decode('utf-8'))
           
                   if isinstance(page_results, dict):
                       page_results = page_results.get('requests', page_results.get('items', []))
           
                   if not page_results:
                       break
           
                   all_records.extend(page_results)
                   print(f"Requests: Retrieved {len(page_results)} records "
                       f"(total: {len(all_records)})")
           
                   if len(page_results) < PAGE_SIZE:
                       break
           
                   start_index += len(page_results)
           
               print(f"Total requests fetched: {len(all_records)}")
               return all_records
           
           def find_newest_time(records):
               newest = None
               for r in records:
                   for field in ['completedTime', 'scheduledTime', 'startedTime',
                               'lastModified', 'requestDate', 'timestamp']:
                       t = r.get(field)
                       if t:
                           try:
                               if isinstance(t, (int, float)):
                                   dt = datetime.fromtimestamp(t / 1000, tz=timezone.utc)
                                   t_iso = dt.isoformat()
                               else:
                                   t_iso = str(t)
                               if newest is None or t_iso > newest:
                                   newest = t_iso
                           except Exception:
                               continue
               return newest
           
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


**Note:** The Pub/Sub trigger configuration automatically creates the necessary subscriptions and permissions. Because ISIM typically uses self-signed certificates, the function disables SSL verification. For production environments, consider importing your ISIM CA certificate into the Cloud Run function.

## Create Cloud Scheduler job

Cloud Scheduler will publish messages to the Pub/Sub topic at regular intervals, triggering the Cloud Run function.

  1. In the **GCP Console** , go to **Cloud Scheduler**.
  2. Click **Create Job**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | `ibm-sim-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select `ibm-sim-logs-trigger`  
**Message body** | `{}` (empty JSON object)  
  4. Click **Create**.




### Schedule frequency options

Choose frequency based on log volume and latency requirements:

Frequency | Cron expression | Use case  
---|---|---  
Every 5 minutes | `*/5 * * * *` | High-volume, low-latency  
Every 15 minutes | `*/15 * * * *` | Medium volume  
Every hour | `0 * * * *` | Standard (recommended)  
Every 6 hours | `0 */6 * * *` | Low volume, batch processing  
Daily | `0 0 * * *` | Historical data collection  
  
### Test the integration

  1. In the **Cloud Scheduler** console, find your job (`ibm-sim-collector-hourly`).
  2. Click **Force run** to trigger the job manually.
  3. Wait a few seconds.
  4. Go to **Cloud Run > Services**.
  5. Click on `ibm-sim-collector`.
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         Fetching logs from YYYY-MM-DDTHH:MM:SS+00:00 to YYYY-MM-DDTHH:MM:SS+00:00
         Successfully authenticated to ISIM
         Successfully retrieved CSRF token
         Activities: Retrieved X records (total: X)
         Requests: Retrieved X records (total: X)
         Wrote X records to gs://ibm-sim-logs-gcs/ibm-sim/ibm_sim_audit_YYYYMMDD_HHMMSS.ndjson
         Successfully processed X records (activities: X, requests: X)
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click on `ibm-sim-logs-gcs`.

  10. Navigate to the `ibm-sim/` folder.

  11. Verify that a new `.ndjson` file was created with the current timestamp.




If you see errors in the logs:

  * **HTTP 401/302** : Verify the `ISIM_USERNAME` and `ISIM_PASSWORD` environment variables are correct and the user account is not locked
  * **HTTP 403** : Verify the ISIM user account has administrator privileges for REST API access
  * **HTTP 404** : Verify the `ISIM_BASE_URL` is correct and includes the proper port number
  * **Connection errors** : Verify network connectivity between the Cloud Run function and the ISIM virtual appliance
  * **Missing environment variables** : Verify all required variables are set in the Cloud Run function configuration



## Retrieve the Google SecOps service account

Google SecOps uses a unique service account to read data from your GCS bucket. You must grant this service account access to your bucket.

### Get the service account email

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `IBM SIM Logs GCS`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **IBM Security Identity Manager** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         secops-12345678@secops-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Don't use service accounts from other documentation or examples.
  9. Click **Next**.

  10. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://ibm-sim-logs-gcs/ibm-sim/
           

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

To grant IAM permissions to the Google SecOps service account, do the following:

  1. Go to **Cloud Storage > Buckets**.
  2. Click on `ibm-sim-logs-gcs`.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Paste the Google SecOps service account email
     * **Assign roles** : Select **Storage Object Viewer**
  6. Click **Save**.

**Note:** If you plan to use the deletion option "Delete transferred files" or "Delete transferred files and empty directories," grant **Storage Object Admin** role instead of Storage Object Viewer.

## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
description | metadata.description | Description of the event  
receivedTime | metadata.event_timestamp | Timestamp when the event occurred  
metadata.event_type | metadata.event_type | Type of event  
version | metadata.product_version | Product version  
connectionId | network.session_id | Session identifier  
tls | network.tls.version | TLS version  
ip | principal.asset.ip | IP address of the asset  
hostname | principal.hostname | Hostname  
ip | principal.ip | IP address  
port | principal.port | Port number  
kv_data | principal.user.attribute.labels | User attribute labels  
action | security_result.action_details | Details of the action taken  
metadata.product_name | metadata.product_name | Product name  
metadata.vendor_name | metadata.vendor_name | Vendor name  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ibm-sim-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
