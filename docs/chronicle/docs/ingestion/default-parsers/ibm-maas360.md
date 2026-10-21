---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ibm-maas360/
title: Collect IBM MaaS360 logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T03:57:17.220404+00:00
---

# Collect IBM MaaS360 logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ibm-maas360/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect IBM MaaS360 logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest IBM MaaS360 logs into Google Security Operations using Google Cloud Storage V2.

IBM MaaS360 is a unified endpoint management (UEM) platform that provides mobile device management, application security, and threat management capabilities. It generates security events including admin login reports, admin changes audits, compliance rule events, device enrollment events, action history events, and security threat events such as SMS and email phishing and malware detections.

## Before you begin

Ensure that you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage, Cloud Run, Pub/Sub, and Cloud Scheduler APIs enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * Privileged access to the IBM MaaS360 portal with an administrator account
  * API access enabled for your IBM MaaS360 account (IBM Support must enable this feature)
  * An administrator account with the **Web Service - Access Keys** role assigned



## Enable API access for your IBM MaaS360 account

Before you can generate API credentials, API access must be enabled for your MaaS360 account. Submit a request to IBM MaaS360 Support to enable the Web Services API feature for your account. Once enabled, the **Web Services API** option becomes available under the **Setup** menu in the MaaS360 portal.

## Create a Web Services API role

To access the API, your administrator account must have the **Web Service - Access Keys** permission. If your account does not already have this role, create one:

  1. Sign in to the **IBM MaaS360 portal**.
  2. Go to **Setup > Portal Administration > Roles**.
  3. Click **Add Role**.
  4. In the **Basic Information** section, provide the following: 
     * **Role Name** : Enter a descriptive name (for example, `Web Service API`).
     * **Role Description** : Enter `Permissions to access the Web Service API`.
  5. For **Select Mode of Creation** , select **Create New** and click **Next**.
  6. From the available Access Rights, select **Web Service - Access Keys**.
  7. Click **Save**.



## Assign the API role to an administrator account

  1. Sign in to the **IBM MaaS360 portal**.
  2. Go to **Setup > Portal Administration > Administrators**.
  3. Click **Edit** next to the administrator account that will be used for the API integration, or create a new administrator account.
  4. Add the **Web Service API** role to the account.
  5. Click **Continue**.
  6. Sign out and sign back in with the updated administrator account for the role changes to take effect.



## Generate an App Access Key

  1. Sign in to the **IBM MaaS360 portal** with the administrator account that has the **Web Service API** role.
  2. Go to **Setup > Web Services API > Manage Access Keys**.
  3. Click **Generate Access Key**.
  4. Select **MaaS360 Web Services** as the key type.
  5. In the **Key Name** field, enter a descriptive name (for example, `Chronicle Integration`).
  6. Click **Generate**.
  7. Authenticate with your administrator password when prompted.
  8. Record the following credentials displayed after key generation:

     * **App ID**
     * **App Version**
     * **Platform ID**
     * **App Access Key**
**Note:** Copy and save these credentials immediately. The App Access Key cannot be retrieved after closing this dialog.



## Find your Billing ID

  1. Sign in to the **IBM MaaS360 portal**.
  2. Hover over the **profile menu** on the top right corner of the portal.
  3. Copy the **Account ID** value. This is your Billing ID.

**Note:** The Billing ID is also visible in the footer at the bottom of the MaaS360 portal page.



## Determine your API base URL

The API base URL depends on your MaaS360 instance. Your instance is determined by the first digit of your Billing ID:

Billing ID starts with | Instance | API base URL  
---|---|---  
**1** | M1 | `https://services.fiberlink.com`  
**2** | M2 | `https://services.m2.maas360.com`  
**3** | M3 | `https://services.m3.maas360.com`  
**4** | M4 | `https://services.m4.maas360.com`  
**Note:** You can also determine your instance from the URL displayed in your browser while logged in to the MaaS360 portal.

### Test API access

  * Test your credentials before proceeding with the integration:
        
        # Replace with your actual values
        API_BASE="https://services.m3.maas360.com"
        BILLING_ID="your-billing-id"
        USERNAME="your-admin-username"
        PASSWORD="your-admin-password"
        APP_ID="your-app-id"
        APP_VERSION="your-app-version"
        PLATFORM_ID="3"
        APP_ACCESS_KEY="your-app-access-key"
        
        # Test authentication
        curl -v -X POST "${API_BASE}/auth-apis/auth/1.0/authenticate/${BILLING_ID}" \
            -H "Content-Type: application/xml" \
            -H "Accept: application/json" \
            -d "<authRequest><maaS360AdminAuth><billingID>${BILLING_ID}</billingID><platformID>${PLATFORM_ID}</platformID><appID>${APP_ID}</appID><appVersion>${APP_VERSION}</appVersion><appAccessKey>${APP_ACCESS_KEY}</appAccessKey><userName>${USERNAME}</userName><password>${PASSWORD}</password></maaS360AdminAuth></authRequest>"
        




A successful response returns a JSON object containing the `authToken`.

## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `maas360-device-logs`)  
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
     * **Service account name** : Enter `maas360-logs-collector-sa`
     * **Service account description** : Enter `Service account for Cloud Run function to collect IBM MaaS360 logs`
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
  2. Click on your bucket name (`maas360-device-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (`maas360-logs-collector-sa@PROJECT_ID.iam.gserviceaccount.com`)
     * **Assign roles** : Select **Storage Object Admin**
  6. Click **Save**.



## Create Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `maas360-logs-trigger`
     * Leave other settings as default
  4. Click **Create**.



## Create Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from the IBM MaaS360 API and write them to GCS.

To create the Cloud Run function to collect logs, do the following:

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `maas360-logs-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose `maas360-logs-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select `maas360-logs-collector-sa`
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:

Variable name | Example value | Description  
---|---|---  
`GCS_BUCKET` | `maas360-device-logs` | GCS bucket name  
`GCS_PREFIX` | `maas360-logs` | Prefix for log files  
`STATE_KEY` | `maas360-logs/state.json` | State file path  
`API_BASE` | `https://services.m3.maas360.com` | MaaS360 API base URL for your instance  
`BILLING_ID` | `your-billing-id` | MaaS360 Account ID (Billing ID)  
`USERNAME` | `your-admin-username` | Administrator username  
`PASSWORD` | `your-admin-password` | Administrator password  
`APP_ID` | `your-app-id` | App ID from generated access key  
`APP_VERSION` | `1.0` | App Version from generated access key  
`PLATFORM_ID` | `your-platform-id` | Platform ID from generated access key  
`APP_ACCESS_KEY` | `your-app-access-key` | App Access Key from generated access key  
`PAGE_SIZE` | `250` | Records per page (25, 50, 100, 200, 250)  
`MAX_PAGES` | `100` | Maximum pages to fetch per run  
`LOOKBACK_HOURS` | `24` | Initial lookback period  
  10. In the **Variables & Secrets** section, scroll down to **Requests** :

     * **Request timeout** : Enter `600` seconds (10 minutes)
  11. Go to the **Settings** tab:

     * In the **Resources** section: 
       * **Memory** : Select **512 MiB** or higher
       * **CPU** : Select **1**
     * In the **Revision scaling** section: 
       * **Minimum number of instances** : Enter `0`
       * **Maximum number of instances** : Enter `100`
  12. Click **Create**.

  13. Wait for the service to be created (1-2 minutes).

  14. After the service is created, the **inline code editor** will open automatically.




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
           import xml.etree.ElementTree as ET
           
           # Initialize HTTP client with timeouts
           http = urllib3.PoolManager(
               timeout=urllib3.Timeout(connect=10.0, read=60.0),
               retries=False,
           )
           
           # Initialize Storage client
           storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
           
           # Environment variables
           GCS_BUCKET = os.environ.get('GCS_BUCKET')
           GCS_PREFIX = os.environ.get('GCS_PREFIX', 'maas360-logs')
           STATE_KEY = os.environ.get('STATE_KEY', 'maas360-logs/state.json')
           API_BASE = os.environ.get('API_BASE', '').rstrip('/')
           BILLING_ID = os.environ.get('BILLING_ID')
           USERNAME = os.environ.get('USERNAME')
           PASSWORD = os.environ.get('PASSWORD')
           APP_ID = os.environ.get('APP_ID')
           APP_VERSION = os.environ.get('APP_VERSION', '1.0')
           PLATFORM_ID = os.environ.get('PLATFORM_ID', '3')
           APP_ACCESS_KEY = os.environ.get('APP_ACCESS_KEY')
           PAGE_SIZE = int(os.environ.get('PAGE_SIZE', '250'))
           MAX_PAGES = int(os.environ.get('MAX_PAGES', '100'))
           LOOKBACK_HOURS = int(os.environ.get('LOOKBACK_HOURS', '24'))
           
           def authenticate():
               """Authenticate to MaaS360 API and return auth token."""
               url = f"{API_BASE}/auth-apis/auth/1.0/authenticate/{BILLING_ID}"
           
               auth_xml = (
                   '<authRequest>'
                   '<maaS360AdminAuth>'
                   f'<billingID>{BILLING_ID}</billingID>'
                   f'<platformID>{PLATFORM_ID}</platformID>'
                   f'<appID>{APP_ID}</appID>'
                   f'<appVersion>{APP_VERSION}</appVersion>'
                   f'<appAccessKey>{APP_ACCESS_KEY}</appAccessKey>'
                   f'<userName>{USERNAME}</userName>'
                   f'<password>{PASSWORD}</password>'
                   '</maaS360AdminAuth>'
                   '</authRequest>'
               )
           
               response = http.request(
                   'POST', url,
                   body=auth_xml.encode('utf-8'),
                   headers={
                       'Content-Type': 'application/xml',
                       'Accept': 'application/json',
                   }
               )
           
               if response.status != 200:
                   raise Exception(
                       f"Authentication failed with status {response.status}: "
                       f"{response.data.decode('utf-8')}"
                   )
           
               data = json.loads(response.data.decode('utf-8'))
               auth_token = data.get('authResponse', {}).get('authToken')
               if not auth_token:
                   raise Exception(
                       f"No authToken in response: {response.data.decode('utf-8')}"
                   )
           
               print("Successfully obtained MaaS360 auth token")
               return auth_token
           
           def fetch_devices(auth_token, last_reported_epoch_ms=None):
               """
               Fetch device records from MaaS360 Device Search API.
           
               Args:
                   auth_token: Authentication token
                   last_reported_epoch_ms: Filter for devices reported after this epoch (ms)
           
               Returns:
                   List of device records as dicts
               """
               url = f"{API_BASE}/device-apis/devices/2.0/search/customer/{BILLING_ID}"
           
               headers = {
                   'Authorization': f'MaaS token="{auth_token}"',
                   'Accept': 'application/json',
               }
           
               all_devices = []
               page_number = 1
           
               while page_number <= MAX_PAGES:
                   params = {
                       'pageSize': str(PAGE_SIZE),
                       'pageNumber': str(page_number),
                       'sortAttribute': 'lastReported',
                       'sortOrder': 'asc',
                   }
           
                   if last_reported_epoch_ms:
                       params['match'] = 'lastReportedSince'
                       params['lastReportedInEpochms'] = str(last_reported_epoch_ms)
           
                   query_string = '&'.join(
                       [f"{k}={v}" for k, v in params.items()]
                   )
                   request_url = f"{url}?{query_string}"
           
                   try:
                       response = http.request('GET', request_url, headers=headers)
           
                       if response.status == 429:
                           print("Rate limited (429). Stopping pagination.")
                           break
           
                       if response.status == 401:
                           print("Auth token expired (401). Re-authenticating...")
                           auth_token = authenticate()
                           headers['Authorization'] = f'MaaS token="{auth_token}"'
                           continue
           
                       if response.status != 200:
                           print(
                               f"HTTP Error: {response.status} - "
                               f"{response.data.decode('utf-8')}"
                           )
                           break
           
                       data = json.loads(response.data.decode('utf-8'))
           
                       devices = data.get('devices', {}).get('device', [])
                       if isinstance(devices, dict):
                           devices = [devices]
           
                       if not devices:
                           print(f"No more devices at page {page_number}")
                           break
           
                       all_devices.extend(devices)
                       print(
                           f"Page {page_number}: Retrieved {len(devices)} devices "
                           f"(total: {len(all_devices)})"
                       )
           
                       if len(devices) < PAGE_SIZE:
                           break
           
                       page_number += 1
           
                   except Exception as e:
                       print(f"Error fetching devices page {page_number}: {e}")
                       break
           
               print(f"Retrieved {len(all_devices)} total device records")
               return all_devices, auth_token
           
           def fetch_action_history(auth_token, last_reported_epoch_ms=None):
               """
               Fetch action history events from MaaS360.
           
               Args:
                   auth_token: Authentication token
                   last_reported_epoch_ms: Filter for events after this epoch (ms)
           
               Returns:
                   List of action history records as dicts
               """
               url = (
                   f"{API_BASE}/device-apis/devices/1.0/"
                   f"searchActionHistory/{BILLING_ID}"
               )
           
               headers = {
                   'Authorization': f'MaaS token="{auth_token}"',
                   'Accept': 'application/json',
               }
           
               all_actions = []
               page_number = 1
           
               while page_number <= MAX_PAGES:
                   params = {
                       'pageSize': str(PAGE_SIZE),
                       'pageNumber': str(page_number),
                   }
           
                   query_string = '&'.join(
                       [f"{k}={v}" for k, v in params.items()]
                   )
                   request_url = f"{url}?{query_string}"
           
                   try:
                       response = http.request('GET', request_url, headers=headers)
           
                       if response.status == 429:
                           print("Rate limited (429). Stopping pagination.")
                           break
           
                       if response.status == 401:
                           print("Auth token expired (401). Re-authenticating...")
                           auth_token = authenticate()
                           headers['Authorization'] = f'MaaS token="{auth_token}"'
                           continue
           
                       if response.status != 200:
                           print(
                               f"HTTP Error: {response.status} - "
                               f"{response.data.decode('utf-8')}"
                           )
                           break
           
                       data = json.loads(response.data.decode('utf-8'))
           
                       actions = data.get('actionHistory', {}).get('action', [])
                       if isinstance(actions, dict):
                           actions = [actions]
           
                       if not actions:
                           print(
                               f"No more action history at page {page_number}"
                           )
                           break
           
                       all_actions.extend(actions)
                       print(
                           f"Action history page {page_number}: "
                           f"{len(actions)} records "
                           f"(total: {len(all_actions)})"
                       )
           
                       if len(actions) < PAGE_SIZE:
                           break
           
                       page_number += 1
           
                   except Exception as e:
                       print(
                           f"Error fetching action history "
                           f"page {page_number}: {e}"
                       )
                       break
           
               print(f"Retrieved {len(all_actions)} action history records")
               return all_actions, auth_token
           
           @functions_framework.cloud_event
           def main(cloud_event):
               """
               Cloud Run function triggered by Pub/Sub to fetch IBM MaaS360
               device and action history logs and write to GCS.
               """
               required_vars = [
                   GCS_BUCKET, API_BASE, BILLING_ID,
                   USERNAME, PASSWORD, APP_ID, APP_ACCESS_KEY,
               ]
               if not all(required_vars):
                   print('Error: Missing required environment variables')
                   return
           
               try:
                   bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(GCS_BUCKET)
                   state = load_state(bucket)
                   now = datetime.now(timezone.utc)
           
                   last_reported_epoch_ms = None
                   if isinstance(state, dict) and [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get('last_reported_epoch_ms'):
                       last_reported_epoch_ms = int(
                           state['last_reported_epoch_ms']
                       )
                       overlap_ms = 2 * 60 * 1000
                       last_reported_epoch_ms = last_reported_epoch_ms - overlap_ms
                   else:
                       lookback = now - timedelta(hours=LOOKBACK_HOURS)
                       last_reported_epoch_ms = int(
                           lookback.timestamp() * 1000
                       )
           
                   print(
                       f"Fetching logs since epoch ms: {last_reported_epoch_ms} "
                       f"({datetime.fromtimestamp(last_reported_epoch_ms / 1000, tz=timezone.utc).isoformat()})"
                   )
           
                   auth_token = authenticate()
           
                   devices, auth_token = fetch_devices(
                       auth_token, last_reported_epoch_ms
                   )
                   actions, auth_token = fetch_action_history(
                       auth_token, last_reported_epoch_ms
                   )
           
                   all_records = []
                   newest_epoch_ms = last_reported_epoch_ms
           
                   for device in devices:
                       device['_maas360_record_type'] = 'device'
                       all_records.append(device)
                       epoch_ms = device.get('lastReportedInEpochms')
                       if epoch_ms:
                           try:
                               epoch_val = int(epoch_ms)
                               if epoch_val > newest_epoch_ms:
                                   newest_epoch_ms = epoch_val
                           except (ValueError, TypeError):
                               pass
           
                   for action in actions:
                       action['_maas360_record_type'] = 'action_history'
                       all_records.append(action)
           
                   if not all_records:
                       print("No new records found.")
                       save_state(
                           bucket,
                           int(now.timestamp() * 1000),
                       )
                       return
           
                   timestamp = now.strftime('%Y%m%d_%H%M%S')
                   object_key = (
                       f"{GCS_PREFIX}/maas360_logs_{timestamp}.ndjson"
                   )
                   blob = bucket.blob(object_key)
           
                   ndjson = '\n'.join(
                       [
                           json.dumps(r, ensure_ascii=False, default=str)
                           for r in all_records
                       ]
                   ) + '\n'
                   blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
                       ndjson, content_type='application/x-ndjson'
                   )
           
                   print(
                       f"Wrote {len(all_records)} records to "
                       f"gs://{GCS_BUCKET}/{object_key}"
                   )
           
                   save_state(bucket, newest_epoch_ms)
           
                   print(
                       f"Successfully processed {len(all_records)} records "
                       f"(devices: {len(devices)}, "
                       f"actions: {len(actions)})"
                   )
           
               except Exception as e:
                   print(f'Error processing logs: {str(e)}')
                   raise
           
           def load_state(bucket):
               """Load state from GCS."""
               try:
                   blob = bucket.blob(STATE_KEY)
                   if blob.exists():
                       return json.loads(blob.[download_as_text](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_download_as_text)())
               except Exception as e:
                   print(f"Warning: Could not load state: {e}")
               return {}
           
           def save_state(bucket, last_reported_epoch_ms):
               """Save the last reported epoch timestamp to GCS state file."""
               try:
                   state = {
                       'last_reported_epoch_ms': last_reported_epoch_ms,
                       'last_run': datetime.now(timezone.utc).isoformat(),
                   }
                   blob = bucket.blob(STATE_KEY)
                   blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
                       json.dumps(state, indent=2),
                       content_type='application/json',
                   )
                   print(
                       f"Saved state: last_reported_epoch_ms="
                       f"{last_reported_epoch_ms}"
                   )
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

Cloud Scheduler will publish messages to the Pub/Sub topic at regular intervals, triggering the Cloud Run function.

  1. In the **GCP Console** , go to **Cloud Scheduler**.
  2. Click **Create Job**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | `maas360-logs-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select `maas360-logs-trigger`  
**Message body** | `{}` (empty JSON object)  
  4. Click **Create**.




### Schedule frequency options

Choose frequency based on log volume and latency requirements:

Frequency | Cron expression | Use case  
---|---|---  
Every 15 minutes | `*/15 * * * *` | High-volume, low-latency  
Every hour | `0 * * * *` | Standard (recommended)  
Every 6 hours | `0 */6 * * *` | Low volume, batch processing  
Daily | `0 0 * * *` | Historical data collection  
  
### Test the integration

  1. In the **Cloud Scheduler** console, find your job (`maas360-logs-collector-hourly`).
  2. Click **Force run** to trigger the job manually.
  3. Wait a few seconds.
  4. Go to **Cloud Run > Services**.
  5. Click on `maas360-logs-collector`.
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         Fetching logs since epoch ms: XXXXXXXXXXXXX (YYYY-MM-DDTHH:MM:SS+00:00)
         Successfully obtained MaaS360 auth token
         Page 1: Retrieved X devices (total: X)
         Action history page 1: X records (total: X)
         Wrote X records to gs://maas360-device-logs/maas360-logs/maas360_logs_YYYYMMDD_HHMMSS.ndjson
         Successfully processed X records (devices: X, actions: X)
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click on `maas360-device-logs`.

  10. Navigate to the `maas360-logs/` folder.

  11. Verify that a new `.ndjson` file was created with the current timestamp.




If you see errors in the logs:

  * **HTTP 401** : Verify the `USERNAME`, `PASSWORD`, `APP_ID`, and `APP_ACCESS_KEY` environment variables are correct
  * **HTTP 403** : Verify the administrator account has the **Web Service - Access Keys** role assigned
  * **HTTP 429** : Rate limiting -- the function will stop pagination and resume on the next scheduled run
  * **Missing environment variables** : Verify all required variables are set in the Cloud Run function configuration



## Retrieve the Google SecOps service account

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `IBM MaaS360 Device Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **IBM MaaS360** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         secops-12345678@secops-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Don't use service accounts from other documentation or examples.
  9. Click **Next**.

  10. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://maas360-device-logs/maas360-logs/
           

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

To Grant IAM permissions to the Google SecOps service account, do the following:

  1. Go to **Cloud Storage > Buckets**.
  2. Click on `maas360-device-logs`.
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
firstRegisteredInEpochms | additional.fields | Converted to string and merged as key-value pairs from firstRegisteredInEpochms, lastRegisteredInEpochms, lastMdmRegisteredInEpochms, lastReportedInEpochms, isSupervisedDevice, testDevice, maas360ManagedStatus, itunesStoreAccountEnabled, installedDateInEpochms, sourceID, imeiEsn, installedDate, mailboxDeviceId, mailboxManaged, mailboxLastReportedInEpochms, mailboxLastReported, lastReported, policyComplianceState, userDomain, maas360Environment, encryptionStatus, enrollmentMode, deviceStatus, appComplianceState, ruleComplianceState, selectiveWipeStatus, jailbreakStatus, platformName, deviceOwner, ownership, customAssetNumber, deviceName, modelId, passcodeCompliance, mdmMailboxDeviceId, mdmPolicy, appVersion  
lastRegisteredInEpochms | additional.fields |   
lastMdmRegisteredInEpochms | additional.fields |   
lastReportedInEpochms | additional.fields |   
isSupervisedDevice | additional.fields |   
testDevice | additional.fields |   
maas360ManagedStatus | additional.fields |   
itunesStoreAccountEnabled | additional.fields |   
installedDateInEpochms | additional.fields |   
sourceID | additional.fields |   
imeiEsn | additional.fields |   
installedDate | additional.fields |   
mailboxDeviceId | additional.fields |   
mailboxManaged | additional.fields |   
mailboxLastReportedInEpochms | additional.fields |   
mailboxLastReported | additional.fields |   
lastReported | additional.fields |   
policyComplianceState | additional.fields |   
userDomain | additional.fields |   
maas360Environment | additional.fields |   
encryptionStatus | additional.fields |   
enrollmentMode | additional.fields |   
deviceStatus | additional.fields |   
appComplianceState | additional.fields |   
ruleComplianceState | additional.fields |   
selectiveWipeStatus | additional.fields |   
jailbreakStatus | additional.fields |   
platformName | additional.fields |   
deviceOwner | additional.fields |   
ownership | additional.fields |   
customAssetNumber | additional.fields |   
deviceName | additional.fields |   
modelId | additional.fields |   
passcodeCompliance | additional.fields |   
mdmMailboxDeviceId | additional.fields |   
mdmPolicy | additional.fields |   
appVersion | additional.fields |   
deviceName | entity.entity.asset.asset_id | Value copied directly  
deviceStatus | entity.entity.asset.deployment_status | Set to "ACTIVE" if deviceStatus == "Active"  
installedDate | entity.entity.asset.first_discover_time | Converted using date filter with format yyyy-MM-ddTHH:mm:ss  
manufacturer | entity.entity.asset.hardware.manufacturer | Value copied directly  
model | entity.entity.asset.hardware.model | Value copied directly  
platformSerialNumber | entity.entity.asset.hardware.serial_number | Value copied directly  
maas360DeviceID | entity.entity.asset.hostname | Value copied directly  
ownership | entity.entity.asset.labels | Merged key-value pairs from various fields  
deviceOwner | entity.entity.asset.labels |   
imeiEsn | entity.entity.asset.labels |   
maas360Environment | entity.entity.asset.labels |   
installLocation | entity.entity.asset.labels |   
maas360ManagedStatus | entity.entity.asset.labels |   
udid | entity.entity.asset.labels |   
mailboxDeviceId | entity.entity.asset.labels |   
mailboxManaged | entity.entity.asset.labels |   
phoneNumber | entity.entity.asset.labels |   
sourceID | entity.entity.asset.labels |   
itunesStoreAccountEnabled | entity.entity.asset.labels |   
unifiedTravelerDeviceId | entity.entity.asset.labels |   
enrollmentMode | entity.entity.asset.labels |   
platformName | entity.entity.asset.labels |   
deviceType | entity.entity.asset.labels |   
modelId | entity.entity.asset.labels |   
mdmPolicy | entity.entity.asset.labels |   
policyComplianceState | entity.entity.asset.labels |   
appComplianceState | entity.entity.asset.labels |   
ruleComplianceState | entity.entity.asset.labels |   
selectiveWipeStatus | entity.entity.asset.labels |   
jailbreakStatus | entity.entity.asset.labels |   
encryptionStatus | entity.entity.asset.labels |   
passcodeCompliance | entity.entity.asset.labels |   
mdmMailboxDeviceId | entity.entity.asset.labels |   
isSupervisedDevice | entity.entity.asset.labels |   
testDevice | entity.entity.asset.labels |   
lastReported | entity.entity.asset.last_discover_time | Converted using date filter with format yyyy-MM-ddTHH:mm:ss  
wifiMacAddress | entity.entity.asset.mac | Merged from wifiMacAddress  
userDomain | entity.entity.asset.network_domain | Value copied directly  
osVersion | entity.entity.asset.platform_software.platform_patch_level | Value copied directly  
osName | entity.entity.asset.platform_software.platform_version | Value copied directly  
deviceType | entity.entity.asset.type | Set to "MOBILE" if deviceType == "Smartphone"  
maas360DeviceID | entity.metadata.entity_type | Set to "ASSET" if maas360DeviceID not empty  
maas360DeviceID | entity.metadata.product_entity_id | Value copied directly  
entity.metadata.product_name | entity.metadata.product_name | Set to "IBM MaaS360"  
entity.metadata.vendor_name | entity.metadata.vendor_name | Set to "IBM"  
username | entity.relations.entity_type | Set to "USER" if username or emailAddress not empty  
emailAddress | entity.relations.entity_type |   
emailAddress | entity.relations.entity.user.email_addresses | Merged from emailAddress  
username | entity.relations.entity.user.userid | Value copied directly  
username | entity.relations.relationship | Set to "OWNS" if username or emailAddress not empty  
emailAddress | entity.relations.relationship |   
maas360DeviceID | metadata.event_type | Set to STATUS_UPDATE if maas360DeviceID not empty, else GENERIC_EVENT  
logType | metadata.product_event_type | Value copied directly  
appVersion | metadata.product_version | Value copied directly  
manufacturer | principal.asset.hardware.manufacturer | Value copied directly  
model | principal.asset.hardware.model | Value copied directly  
platformSerialNumber | principal.asset.hardware.serial_number | Value copied directly  
maas360DeviceID | principal.asset.hostname | Value copied directly  
maas360DeviceID | principal.hostname | Value copied directly  
wifiMacAddress | principal.mac | Merged if not empty and not "N/A"  
osName | principal.platform | Set to WINDOWS if matches (?i)windows; MAC if matches (?i)Mac  
osVersion | principal.platform_version | Value copied directly  
deviceType | principal.resource.name | Value copied directly  
unifiedTravelerDeviceId | principal.resource.product_object_id | Value copied directly  
emailAddress | principal.user.email_addresses | Merged from emailAddress  
username | principal.user.user_display_name | Value copied directly  
udid | principal.user.userid | Value copied directly  
metadata.product_name | metadata.product_name | Set to "IBM MaaS360"  
metadata.vendor_name | metadata.vendor_name | Set to "IBM"  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ibm-maas360-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
