---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/armis-devices/
title: Collect Armis Devices logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:54:05.522961+00:00
---

# Collect Armis Devices logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/armis-devices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Armis Devices logs

**Parser Version:** 2.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Armis Devices logs to Google Security Operations using Google Cloud Storage V2.

Armis Centrix is an enterprise-class asset intelligence platform designed to provide visibility and protection for managed, unmanaged, and IoT/OT devices. The Armis Devices data stream captures the full device inventory observed across monitored networks, including hardware details, network attributes, risk assessments, and classification metadata. These device inventory logs can be exported through the Armis REST API and written to a GCS bucket for ingestion by Google SecOps.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * An Armis Centrix instance with API access
  * An Armis API secret key with permissions to read device data



## Generate an Armis API secret key

  1. Sign in to your **Armis Centrix** console at `https://<your-instance>.armis.com`.
  2. Navigate to **Settings > Asset Management & Security > API Management**.
  3. Click **Create** to generate a new API secret key.
  4. A dialog displays the secret key.
  5. **Copy and save** the secret key securely.

**Important:** The secret key is displayed only once during creation. Store it in a secure location. You will need this key to authenticate API requests.

### Verify API access

  * Test your credentials before proceeding with the integration:
        
        ARMIS_INSTANCE="https://your-instance.armis.com"
        ARMIS_SECRET_KEY="your-secret-key"
        
        # Get access token
        ACCESS_TOKEN=$(curl -s -X POST "${ARMIS_INSTANCE}/api/v1/access_token/" \
            -d "secret_key=${ARMIS_SECRET_KEY}" \
            | python3 -c "import sys,json; print(json.load(sys.stdin)['data']['access_token'])")
        
        echo "Access Token: ${ACCESS_TOKEN}"
        
        # Test device search
        curl -s "${ARMIS_INSTANCE}/api/v1/search/" \
            -H "Authorization: ${ACCESS_TOKEN}" \
            -G \
            --data-urlencode "aql=in:devices timeFrame:\"1 Hours\"" \
            --data-urlencode "length=1" \
            --data-urlencode "fields=id,name,type,category,model,manufacturer,ipAddress,macAddress,operatingSystem,riskLevel,site,firstSeen,lastSeen" \
            | python3 -m json.tool
        

**Note:** The access token is temporary. For the Cloud Run function, the token is automatically refreshed before each data collection run.



## Create a Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `armis-device-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Create a service account for the Cloud Run function

The Cloud Run function needs a service account with permissions to write to GCS bucket and be invoked by Pub/Sub.

### Create the service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `armis-devices-collector-sa`
     * **Service account description** : Enter `Service account for Cloud Run function to collect Armis device inventory logs`
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
  2. Click your bucket name.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `armis-devices-collector-sa@PROJECT_ID.iam.gserviceaccount.com`)
     * **Assign roles** : Select **Storage Object Admin**
  6. Click **Save**.



## Create a Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `armis-devices-trigger`
     * Leave other settings as default
  4. Click **Create**.



## Create a Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch device inventory records from the Armis REST API and write them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `armis-devices-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose the topic `armis-devices-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select the service account `armis-devices-collector-sa`
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `armis-device-logs` | GCS bucket name  
`GCS_PREFIX` | `armis-devices` | Prefix for log files  
`STATE_KEY` | `armis-devices/state.json` | State file path  
`ARMIS_INSTANCE_URL` | `https://your-instance.armis.com` | Armis instance URL  
`ARMIS_SECRET_KEY` | `your-secret-key` | Armis API secret key  
`PAGE_SIZE` | `1000` | Records per API page  
`MAX_RECORDS` | `50000` | Max records per run  
`LOOKBACK_HOURS` | `24` | Initial lookback period  
  10. Scroll down in the **Variables & Secrets** section to **Requests** :

     * **Request timeout** : Enter `540` seconds (9 minutes)
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
           import urllib.parse
           from datetime import datetime, timezone, timedelta
           import time
           
           # Initialize HTTP client with timeouts
           http = urllib3.PoolManager(
             timeout=urllib3.Timeout(connect=5.0, read=60.0),
             retries=False,
           )
           
           # Initialize Storage client
           storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
           
           # Environment variables
           GCS_BUCKET = os.environ.get('GCS_BUCKET')
           GCS_PREFIX = os.environ.get('GCS_PREFIX', 'armis-devices').strip('/')
           STATE_KEY = os.environ.get('STATE_KEY') or f"{GCS_PREFIX}/state.json"
           ARMIS_INSTANCE_URL = os.environ.get('ARMIS_INSTANCE_URL', '').rstrip('/')
           ARMIS_SECRET_KEY = os.environ.get('ARMIS_SECRET_KEY')
           PAGE_SIZE = int(os.environ.get('PAGE_SIZE', '1000'))
           MAX_RECORDS = int(os.environ.get('MAX_RECORDS', '50000'))
           LOOKBACK_HOURS = int(os.environ.get('LOOKBACK_HOURS', '24'))
           
           DEVICE_FIELDS = [
             'id', 'name', 'type', 'category', 'model', 'manufacturer',
             'ipAddress', 'macAddress', 'operatingSystem', 'operatingSystemVersion',
             'riskLevel', 'site', 'tags', 'firstSeen', 'lastSeen',
             'boundaries', 'customProperties', 'dataSources', 'userIds',
             'visibility', 'ppiSensitive'
           ]
           
           def parse_datetime(value):
             """Parse ISO datetime string to datetime object."""
             if not value:
               return None
             if [value](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.ObjectCustomContextPayload.html#google_cloud_storage_blob_ObjectCustomContextPayload_value).endswith("Z"):
               value = value[:-1] + "+00:00"
             try:
               return datetime.fromisoformat(value)
             except Exception:
               try:
                 return datetime.strptime(value, '%Y-%m-%dT%H:%M:%S')
               except Exception:
                 return None
           
           def get_access_token():
             """Obtain an access token from the Armis API."""
             url = f"{ARMIS_INSTANCE_URL}/api/v1/access_token/"
             body = urllib.parse.urlencode({'secret_key': ARMIS_SECRET_KEY})
             response = http.request(
               'POST', url,
               body=body,
               headers={'Content-Type': 'application/x-www-form-urlencoded'}
             )
             if response.status != 200:
               raise Exception(
                 f"Failed to get access token: HTTP {response.status} - "
                 f"{response.data.decode('utf-8')}"
               )
             data = json.loads(response.data.decode('utf-8'))
             return data['data']['access_token']
           
           @functions_framework.cloud_event
           def main(cloud_event):
             """
             Cloud Run function triggered by Pub/Sub to fetch
             Armis Device inventory records and write to GCS.
           
             Args:
               cloud_event: CloudEvent object containing Pub/Sub message
             """
           
             if not all([GCS_BUCKET, ARMIS_INSTANCE_URL, ARMIS_SECRET_KEY]):
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
                   # Overlap by 2 minutes to catch delayed events
                   if last_time:
                     last_time = last_time - timedelta(minutes=2)
                 except Exception as e:
                   print(f"Warning: Could not parse last_event_time: {e}")
           
               if last_time is None:
                 last_time = now - timedelta(hours=LOOKBACK_HOURS)
           
               print(
                 f"Fetching device logs from "
                 f"{last_time.isoformat()} to {now.isoformat()}"
               )
           
               # Get access token
               access_token = get_access_token()
               print("Successfully obtained Armis access token.")
           
               # Fetch device records
               records, newest_event_time = fetch_device_logs(
                 access_token=access_token,
                 start_time=last_time,
                 end_time=now,
               )
           
               if not records:
                 print("No new device records found.")
                 save_state(bucket, STATE_KEY, now.isoformat())
                 return
           
               # Write to GCS as NDJSON
               timestamp = now.strftime('%Y%m%d_%H%M%S')
               object_key = f"{GCS_PREFIX}/logs_{timestamp}.ndjson"
               blob = bucket.blob(object_key)
           
               ndjson = '\n'.join(
                 [json.dumps(record, ensure_ascii=False) for record in records]
               ) + '\n'
               blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
                 ndjson, content_type='application/x-ndjson'
               )
           
               print(
                 f"Wrote {len(records)} records to "
                 f"gs://{GCS_BUCKET}/{object_key}"
               )
           
               # Update state
               if newest_event_time:
                 save_state(bucket, STATE_KEY, newest_event_time)
               else:
                 save_state(bucket, STATE_KEY, now.isoformat())
           
               print(f"Successfully processed {len(records)} records")
           
             except Exception as e:
               print(f'Error processing device logs: {str(e)}')
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
           
           def save_state(bucket, key, last_event_time_iso):
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
           
           def fetch_device_logs(access_token, start_time, end_time):
             """
             Fetch device inventory logs from Armis REST API with pagination.
           
             Args:
               access_token: Armis API access token
               start_time: Start time for log query
               end_time: End time for log query
           
             Returns:
               Tuple of (records list, newest_event_time ISO string)
             """
             base_url = f"{ARMIS_INSTANCE_URL}/api/v1/search/"
             headers = {'Authorization': access_token}
           
             # Build AQL query with time filter
             start_str = start_time.strftime('%Y-%m-%dT%H:%M:%S')
             aql_query = f'in:devices after:{start_str}'
           
             records = []
             newest_time = None
             page_from = 0
             backoff = 1.0
           
             while True:
               if len(records) >= MAX_RECORDS:
                 print(f"Reached max_records limit ({MAX_RECORDS})")
                 break
           
               params = {
                 'aql': aql_query,
                 'from': str(page_from),
                 'orderBy': 'lastSeen',
                 'length': str(PAGE_SIZE),
                 'fields': ','.join(DEVICE_FIELDS),
               }
           
               try:
                 response = http.request(
                   'GET', base_url,
                   fields=params,
                   headers=headers
                 )
           
                 # Handle rate limiting with exponential backoff
                 if response.status == 429:
                   retry_after = int(
                     response.headers.get(
                       'Retry-After', str(int(backoff))
                     )
                   )
                   print(
                     f"Rate limited (429). "
                     f"Retrying after {retry_after}s..."
                   )
                   time.sleep(retry_after)
                   backoff = min(backoff * 2, 30.0)
                   continue
           
                 # Handle token expiry
                 if response.status == 401:
                   print("Access token expired, refreshing...")
                   access_token = get_access_token()
                   headers = {'Authorization': access_token}
                   continue
           
                 backoff = 1.0
           
                 if response.status != 200:
                   print(f"HTTP Error: {response.status}")
                   response_text = response.data.decode('utf-8')
                   print(f"Response body: {response_text}")
                   return records, newest_time
           
                 data = json.loads(response.data.decode('utf-8'))
                 result = data.get('data', {}).get('results', [])
                 total = data.get('data', {}).get('total', 0)
                 count = data.get('data', {}).get('count', 0)
                 next_from = data.get('data', {}).get('next')
           
                 if not result:
                   print(f"No more results (empty page)")
                   break
           
                 print(
                   f"Page from={page_from}: Retrieved {count} devices "
                   f"(total: {total})"
                 )
                 records.extend(result)
           
                 # Track newest event time using lastSeen
                 for device in result:
                   try:
                     event_time = device.get('lastSeen')
                     if event_time:
                       if newest_time is None:
                         newest_time = event_time
                       else:
                         current_dt = parse_datetime(event_time)
                         newest_dt = parse_datetime(newest_time)
                         if (
                           current_dt and newest_dt
                           and current_dt > newest_dt
                         ):
                           newest_time = event_time
                   except Exception as e:
                     print(
                       f"Warning: Could not parse "
                       f"event time: {e}"
                     )
           
                 # Check pagination
                 if next_from is None or count < PAGE_SIZE:
                   print("Reached last page")
                   break
           
                 page_from = next_from
           
               except Exception as e:
                 print(f"Error fetching device logs: {e}")
                 return records, newest_time
           
             print(f"Retrieved {len(records)} total device records")
             return records, newest_time
           

**Note:** This script is provided as an example and is not officially supported. We welcome feedback about how we can improve it. To submit feedback, click **Send Feedback > Google SecOps Security Product Feedback** on this page.

     * Second file - **requirements.txt:**
           
           functions-framework==3.*
           google-cloud-storage==2.*
           urllib3>=2.0.0
           

  3. Click **Deploy** to save and deploy the function.

  4. Wait for deployment to complete (2-3 minutes).

**Note:** The Armis API uses the `/search/` endpoint with ASQ (Armis Standard Query) syntax. The query `in:devices` targets device inventory records specifically. The `after:` filter is used for incremental data collection based on the `lastSeen` timestamp. The API returns paginated results using `from` and `length` parameters, with a `next` cursor in the response.



## Create a Cloud Scheduler job

Cloud Scheduler will publish messages to the Pub/Sub topic at regular intervals, triggering the Cloud Run function.

  1. In the **GCP Console** , go to **Cloud Scheduler**.
  2. Click **Create Job**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | `armis-devices-collector-daily`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 2 * * *` (daily at 2:00 AM)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the topic `armis-devices-trigger`  
**Message body** | `{}` (empty JSON object)  
  4. Click **Create**.




### Schedule frequency options

Choose frequency based on device inventory update rate and latency requirements:

Frequency | Cron Expression | Use Case  
---|---|---  
Every 6 hours | `0 */6 * * *` | Frequent inventory updates  
Daily | `0 2 * * *` | Standard (recommended)  
Every 12 hours | `0 */12 * * *` | Lower volume environments  
**Note:** Device inventory data changes less frequently than activity or alert data. A daily or twice-daily schedule is typically sufficient for most environments. The poll interval and scheduler frequency should match. If the poll interval is greater than the scheduler time, data loss may occur. If the poll interval is less than the scheduler time, data duplication may occur. The Armis API supports a maximum timeframe of 100 days.

### Test the integration

  1. In the **Cloud Scheduler** console, find your job.
  2. Click **Force run** to trigger the job manually.
  3. Wait a few seconds.
  4. Go to **Cloud Run > Services**.
  5. Click on the function name `armis-devices-collector`.
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         Fetching device logs from YYYY-MM-DDTHH:MM:SS+00:00 to YYYY-MM-DDTHH:MM:SS+00:00
         Successfully obtained Armis access token.
         Page from=0: Retrieved X devices (total: Y)
         Wrote X records to gs://armis-device-logs/armis-devices/logs_YYYYMMDD_HHMMSS.ndjson
         Successfully processed X records
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click your bucket name.

  10. Navigate to the prefix folder `armis-devices/`.

  11. Verify that a new `.ndjson` file was created with the current timestamp.




If you see errors in the logs:

  * **HTTP 400** : Check that the AQL query syntax is correct. Verify the Armis instance URL does not have a trailing slash.
  * **HTTP 401** : The access token expired or is invalid. The function automatically refreshes the token on 401 errors.
  * **HTTP 429** : Rate limiting - function will automatically retry with backoff.
  * **"Access token not found"** : Verify the Armis API secret key is correct.
  * **Missing environment variables** : Check all required variables are set.



## Configure a feed in Google SecOps to ingest Armis Devices logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Armis Devices`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Armis Devices** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Don't use service accounts from other documentation or examples.
  9. Click **Next**.

  10. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://armis-device-logs/armis-devices/
           

       * Replace: 
         * `armis-device-logs`: Your GCS bucket name.
         * `armis-devices`: Optional prefix/folder path where logs are stored (leave empty for root).
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
  2. Click your bucket name.
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
`datasource.firstSeen` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ssZZ`  
`datasource.lastSeen` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ssZZ`  
`firstSeen` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ssZZ`  
`lastSeen` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ssZZ`  
`time` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ss.SSSZZ`  
`id` | `metadata.product_entity_id` | Directly mapped  
`relation` | `relations` | Renamed/mapped  
N/A | `metadata.entity_type` | Constant: `ASSET`  
N/A | `metadata.product_name` | Constant: `ARMIS`  
N/A | `metadata.vendor_name` | Constant: `ARMIS`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/armis-devices-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
