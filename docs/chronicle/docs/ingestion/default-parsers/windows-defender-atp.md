---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/windows-defender-atp/
title: Collect Microsoft Defender for Endpoint logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:06:34.061701+00:00
---

# Collect Microsoft Defender for Endpoint logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/windows-defender-atp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Microsoft Defender for Endpoint logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Microsoft Defender for Endpoint (Advanced Threat Protection) logs to Google Security Operations using Google Cloud Storage V2.

Microsoft Defender for Endpoint is an enterprise endpoint security platform that provides preventative protection, post-breach detection, automated investigation, and response capabilities. It generates alerts, incidents, device inventory, and advanced hunting telemetry data that can be streamed via the Microsoft Security API to external storage for analysis in Google SecOps.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * A Microsoft 365 E5 or Microsoft Defender for Endpoint P2 license
  * Global Administrator or Security Administrator role in Microsoft Entra ID (Azure AD)
  * An application registered in Microsoft Entra ID with the required API permissions



## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `defender-atp-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location closest to your Google SecOps instance  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Register an application in Microsoft Entra ID

  1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com/).
  2. Go to **Identity > Applications > App registrations**.
  3. Click **New registration**.
  4. Provide the following configuration details: 
     * **Name** : Enter a descriptive name (for example, `SecOps-Defender-ATP-Integration`)
     * **Supported account types** : Select **Accounts in this organizational directory only**
     * **Redirect URI** : Leave blank
  5. Click **Register**.
  6. On the application overview page, copy and save the following values: 
     * **Application (client) ID**
     * **Directory (tenant) ID**



### Create a client secret

  1. In the application page, go to **Certificates & secrets**.
  2. Click **New client secret**.
  3. Provide the following configuration details: 
     * **Description** : Enter `SecOps Integration Secret`
     * **Expires** : Select an expiration period (for example, **24 months**)
  4. Click **Add**.
  5. Copy and save the **Value** of the client secret immediately.

**Note:** The client secret value is only displayed once. If you navigate away without copying it, you must create a new secret.



### Grant API permissions

  1. In the application page, go to **API permissions**.
  2. Click **Add a permission**.
  3. Select **APIs my organization uses**.
  4. Search for and select **WindowsDefenderATP**.
  5. Select **Application permissions**.
  6. Select the following permissions: 
     * **Alert.Read.All** \- Read all alerts
     * **Machine.Read.All** \- Read all machine information
     * **SecurityRecommendation.Read.All** \- Read security recommendations
     * **Vulnerability.Read.All** \- Read vulnerability information
     * **AdvancedQuery.Read.All** \- Run advanced queries
  7. Click **Add permissions**.
  8. Click **Grant admin consent for (your organization)**.
  9. Confirm by clicking **Yes**.



### Verify permissions

  1. In the **API permissions** page, verify that all permissions show **Granted for (your organization)** in the **Status** column.
  2. If any permissions show **Not granted** , click **Grant admin consent** again.



### Test API access

  * Test your credentials before proceeding with the integration:
        
        TENANT_ID="<your-tenant-id>"
        CLIENT_ID="<your-client-id>"
        CLIENT_SECRET="<your-client-secret>"
        
        # Get OAuth token
        TOKEN=$(curl -s -X POST "https://login.microsoftonline.com/${TENANT_ID}/oauth2/v2.0/token" \
            -H "Content-Type: application/x-www-form-urlencoded" \
            -d "client_id=${CLIENT_ID}&scope=https://api.securitycenter.microsoft.com/.default&client_secret=${CLIENT_SECRET}&grant_type=client_credentials" | python3 -c "import sys,json;print(json.load(sys.stdin)['access_token'])")
        
        # Test API access
        curl -s -H "Authorization: Bearer ${TOKEN}" "https://api.securitycenter.microsoft.com/api/alerts?\$top=1" | python3 -m json.tool
        




## Create service account for Cloud Run function

The Cloud Run function needs a service account with permissions to write to GCS bucket and be invoked by Pub/Sub.

### Create service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `defender-atp-collector-sa`
     * **Service account description** : Enter `Service account for Cloud Run function to collect Microsoft Defender for Endpoint logs`
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
  2. Click on your bucket name (for example, `defender-atp-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `defender-atp-collector-sa@PROJECT_ID.iam.gserviceaccount.com`)
     * **Assign roles** : Select **Storage Object Admin**
  6. Click **Save**.



## Create Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `defender-atp-trigger`
     * Leave other settings as default
  4. Click **Create**.



## Create Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from Microsoft Defender for Endpoint API and write them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `defender-atp-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose `defender-atp-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select `defender-atp-collector-sa`
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `defender-atp-logs` | GCS bucket name  
`GCS_PREFIX` | `defender-atp` | Prefix for log files  
`STATE_KEY` | `defender-atp/state.json` | State file path  
`TENANT_ID` | `your-tenant-id` | Microsoft Entra ID tenant ID  
`CLIENT_ID` | `your-client-id` | Application (client) ID  
`CLIENT_SECRET` | `your-client-secret` | Client secret value  
`MAX_RECORDS` | `10000` | Max records per run  
`PAGE_SIZE` | `1000` | Records per API page  
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
           GCS_PREFIX = os.environ.get('GCS_PREFIX', 'defender-atp')
           STATE_KEY = os.environ.get('STATE_KEY', 'defender-atp/state.json')
           TENANT_ID = os.environ.get('TENANT_ID')
           CLIENT_ID = os.environ.get('CLIENT_ID')
           CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
           MAX_RECORDS = int(os.environ.get('MAX_RECORDS', '10000'))
           PAGE_SIZE = int(os.environ.get('PAGE_SIZE', '1000'))
           LOOKBACK_HOURS = int(os.environ.get('LOOKBACK_HOURS', '24'))
           
           def get_access_token(tenant_id, client_id, client_secret):
             """Get OAuth 2.0 access token from Microsoft Entra ID."""
             token_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
             body = (
               f"client_id={client_id}"
               f"&scope=https%3A%2F%2Fapi.securitycenter.microsoft.com%2F.default"
               f"&client_secret={client_secret}"
               f"&grant_type=client_credentials"
             )
             headers = {'Content-Type': 'application/x-www-form-urlencoded'}
             response = http.request('POST', token_url, body=body.encode('utf-8'), headers=headers)
             if response.status != 200:
               raise Exception(f"Token request failed: {response.status} - {response.data.decode('utf-8')}")
             token_data = json.loads(response.data.decode('utf-8'))
             return token_data['access_token']
           
           def parse_datetime(value):
             """Parse ISO datetime string to datetime object."""
             if [value](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.ObjectCustomContextPayload.html#google_cloud_storage_blob_ObjectCustomContextPayload_value).endswith("Z"):
               value = value[:-1] + "+00:00"
             return datetime.fromisoformat(value)
           
           @functions_framework.cloud_event
           def main(cloud_event):
             """Cloud Run function triggered by Pub/Sub to fetch Defender for Endpoint logs."""
             if not all([GCS_BUCKET, TENANT_ID, CLIENT_ID, CLIENT_SECRET]):
               print('Error: Missing required environment variables')
               return
           
             try:
               bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(GCS_BUCKET)
               state = load_state(bucket, STATE_KEY)
           
               now = datetime.now(timezone.utc)
               last_time = None
           
               if isinstance(state, dict) and [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get("last_event_time"):
                 try:
                   last_time = parse_datetime(state["last_event_time"])
                   last_time = last_time - timedelta(minutes=2)
                 except Exception as e:
                   print(f"Warning: Could not parse last_event_time: {e}")
           
               if last_time is None:
                 last_time = now - timedelta(hours=LOOKBACK_HOURS)
           
               print(f"Fetching alerts from {last_time.isoformat()} to {now.isoformat()}")
           
               token = get_access_token(TENANT_ID, CLIENT_ID, CLIENT_SECRET)
           
               records, newest_event_time = fetch_alerts(
                 token=token,
                 start_time=last_time,
                 end_time=now,
                 page_size=PAGE_SIZE,
                 max_records=MAX_RECORDS,
               )
           
               if not records:
                 print("No new alert records found.")
                 save_state(bucket, STATE_KEY, now.isoformat())
                 return
           
               timestamp = now.strftime('%Y%m%d_%H%M%S')
               object_key = f"{GCS_PREFIX}/logs_{timestamp}.ndjson"
               blob = bucket.blob(object_key)
           
               ndjson = '\n'.join([json.dumps(record, ensure_ascii=False) for record in records]) + '\n'
               blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(ndjson, content_type='application/x-ndjson')
           
               print(f"Wrote {len(records)} records to gs://{GCS_BUCKET}/{object_key}")
           
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
           
           def fetch_alerts(token, start_time, end_time, page_size, max_records):
             """Fetch alerts from Microsoft Defender for Endpoint API with pagination."""
             base_url = "https://api.securitycenter.microsoft.com/api/alerts"
             headers = {
               'Authorization': f'Bearer {token}',
               'Accept': 'application/json',
               'Content-Type': 'application/json',
             }
           
             start_iso = start_time.strftime('%Y-%m-%dT%H:%M:%SZ')
             end_iso = end_time.strftime('%Y-%m-%dT%H:%M:%SZ')
           
             filter_query = f"alertCreationTime ge {start_iso} and alertCreationTime le {end_iso}"
             url = f"{base_url}?$filter={filter_query}&$top={page_size}&$orderby=alertCreationTime asc"
           
             records = []
             newest_time = None
             page_num = 0
             backoff = 1.0
           
             while url:
               page_num += 1
           
               if len(records) >= max_records:
                 print(f"Reached max_records limit ({max_records})")
                 break
           
               try:
                 response = http.request('GET', url, headers=headers)
           
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
                 page_results = data.get('value', [])
           
                 if not page_results:
                   print(f"No more results (empty page)")
                   break
           
                 print(f"Page {page_num}: Retrieved {len(page_results)} alerts")
                 records.extend(page_results)
           
                 for alert in page_results:
                   try:
                     event_time = alert.get('alertCreationTime')
                     if event_time:
                       if newest_time is None or parse_datetime(event_time) > parse_datetime(newest_time):
                         newest_time = event_time
                   except Exception as e:
                     print(f"Warning: Could not parse event time: {e}")
           
                 url = data.get('@odata.nextLink')
           
               except Exception as e:
                 print(f"Error fetching alerts: {e}")
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
**Name** | `defender-atp-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select `defender-atp-trigger`  
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
  
### Test the integration

  1. In the **Cloud Scheduler** console, find your job.
  2. Click **Force run** to trigger the job manually.
  3. Wait a few seconds.
  4. Go to **Cloud Run > Services**.
  5. Click on `defender-atp-collector`.
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         Fetching alerts from YYYY-MM-DDTHH:MM:SS+00:00 to YYYY-MM-DDTHH:MM:SS+00:00
         Page 1: Retrieved X alerts
         Wrote X records to gs://defender-atp-logs/defender-atp/logs_YYYYMMDD_HHMMSS.ndjson
         Successfully processed X records
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click on your bucket name (for example, `defender-atp-logs`).

  10. Navigate to the `defender-atp/` folder.

  11. Verify that a new `.ndjson` file was created with the current timestamp.




If you see errors in the logs:

  * **HTTP 401** : Check API credentials (TENANT_ID, CLIENT_ID, CLIENT_SECRET) in environment variables
  * **HTTP 403** : Verify the application has the required API permissions and admin consent is granted
  * **HTTP 429** : Rate limiting - function will automatically retry with backoff
  * **Missing environment variables** : Check all required variables are set



## Retrieve the Google SecOps service account

Google SecOps uses a unique service account to read data from your GCS bucket. You must grant this service account access to your bucket.

### Get the service account email

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Defender ATP Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Microsoft Defender for Endpoint** as the **Log type**.
  7. Click **Get Service Account**.
  8. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  9. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Don't use service accounts from other documentation or examples.
  10. Click **Next**.

  11. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://defender-atp-logs/defender-atp/
           

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

The Google SecOps service account needs **Storage Object Viewer** role on your GCS bucket.

  1. Go to **Cloud Storage > Buckets**.
  2. Click on your bucket name (for example, `defender-atp-logs`).
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
| metadata.vendor_name | The metadata.vendor_name UDM field is set to Microsoft.  
| metadata.product_name | The metadata.product_name UDM field is set to Microsoft Defender for Endpoint.  
id | metadata.product_log_id | id log field is mapped to the metadata.product_log_id UDM field.  
alertCreationTime | metadata.event_timestamp | alertCreationTime log field is mapped to the metadata.event_timestamp UDM field.  
title | security_result.summary | title log field is mapped to the security_result.summary UDM field.  
description | security_result.description | description log field is mapped to the security_result.description UDM field.  
category | security_result.category_details | category log field is mapped to the security_result.category_details UDM field.  
severity | security_result.severity | severity log field is mapped to the security_result.severity UDM field.  
status | security_result.detection_fields[status] | status log field is mapped to the security_result.detection_fields UDM field.  
classification | security_result.detection_fields[classification] | classification log field is mapped to the security_result.detection_fields UDM field.  
determination | security_result.detection_fields[determination] | determination log field is mapped to the security_result.detection_fields UDM field.  
investigationState | security_result.detection_fields[investigationState] | investigationState log field is mapped to the security_result.detection_fields UDM field.  
computerDnsName | principal.hostname | computerDnsName log field is mapped to the principal.hostname UDM field.  
machineId | principal.asset.asset_id | machineId log field is mapped to the principal.asset.asset_id UDM field.  
relatedUser.userName | principal.user.userid | relatedUser.userName log field is mapped to the principal.user.userid UDM field.  
relatedUser.domainName | principal.administrative_domain | relatedUser.domainName log field is mapped to the principal.administrative_domain UDM field.  
threatName | security_result.threat_name | threatName log field is mapped to the security_result.threat_name UDM field.  
threatFamilyName | security_result.threat_name | threatFamilyName log field is mapped to the security_result.threat_name UDM field.  
detectionSource | security_result.detection_fields[detectionSource] | detectionSource log field is mapped to the security_result.detection_fields UDM field.  
evidence | security_result.detection_fields[evidence] | evidence log field is mapped to the security_result.detection_fields UDM field.  
`properties.Application` | `principal.application` | Mapped from changelog  
`properties.AccountDisplayName` | `principal.user.user_display_name` | Mapped from changelog  
`properties.AccountId` | `principal.user.product_object_id` | Mapped from changelog  
`properties.AccountType` | `principal.user.attribute.labels` | Mapped from changelog  
`properties.UserAgent` | `network.http.user_agent` | Mapped from changelog  
`properties.RawEventData.Id", "properties.RawEventData.item.id", "properties.RawEventData.ParentFolder.Id", "properties.AppInstanceId", "properties.ActivityType", "properties.ActivityObjects", "properties.ApplicationId", "properties.DeviceType", "properties.EnforcementMode", "properties.IsAnonymousProxy", "properties.IsAdminOperation", "properties.IsExternalUser", "properties.IsImpersonated", "properties.RawEventData.MDATPDeviceId", "properties.AdditionalFields.IsSatelliteProvider", "properties.RawEventData.DestinationLocationType", "properties.RawEventData.CreationTime", "properties.RawEventData.FileExtension", "properties.RawEventData.Hidden", "properties.RawEventData.FileType", "properties.IPCategory", "properties.ISP", "properties.IPTags", "properties.RawEventData.UserType", "properties.RawEventData.Version" and "properties.RawEventData.Workload", "properties.UserAgentTags", "operationName", "properties.ObjectType", "properties.RawEventData.Operation", "properties.ObjectName", "properties.RawEventData.Scope","properties.RawEventData.ClientProcessName", "properties.RawEventData.ClientInfoString", "properties.RawEventData.ClientRequestId", "properties.RawEventData.ClientVersion", "properties.RawEventData.ExternalAccess", "properties.RawEventData.LogonType", "properties.RawEventData.LogonUserSid", "properties.RawEventData.MailboxGuid", and "properties.RawEventData.UserKey` | `additional.fields` | Mapped from changelog  
`properties.RawEventData.ClientIP" and "properties.IPAddress` | `principal.ip` | Mapped from changelog  
`properties.RawEventData.DeviceName` | `principal.hostname` | Mapped from changelog  
`metadata.event_type` | `FILE_CREATION` | Mapped from changelog  
`properties.AccountObjectId` | `principal.user.userid` | Mapped from changelog  
`properties.CountryCode` | `principal.location.country_or_region` | Mapped from changelog  
`properties.City` | `principal.location.city` | Mapped from changelog  
`properties.RawEventData.Application` | `principal.application` | Mapped from changelog  
`properties.RawEventData.TargetFilePath` | `target.file.full_path` | Mapped from changelog  
`properties.IPAddress` | `principal.ip` | Mapped from changelog  
`properties.ApplicationId` | `additional.fields` | Mapped from changelog  
`properties.RawEventData.FileExtension` | `additional.fields` | Mapped from changelog  
`properties.RawEventData.MDATPDeviceId` | `additional.fields` | Mapped from changelog  
`properties.RawEventData.FileType` | `additional.fields` | Mapped from changelog  
`properties.RawEventData.Sha1` | `target.process.file.sha1` | Mapped from changelog  
`properties.RawEventData.Sha256` | `target.process.file.sha256` | Mapped from changelog  
`properties.RawEventData.FileSize` | `target.process.file.size` | Mapped from changelog  
`metadata.entity_type` | `ASSET` | Mapped from changelog  
`properties.DeviceId` | `entity.asset.asset_id` | Mapped from changelog  
`AdditionalFields" and "properties.AdditionalFields` | `principal.resource.attribute.labels` | Mapped from changelog  
`tenantId` | `resource_ancestors.product_object_id` | Mapped from changelog  
`properties.RawEventData.Sha1` | `principal.process.file.sha1` | Mapped from changelog  
`properties.RawEventData.Sha256` | `principal.process.file.sha256` | Mapped from changelog  
`properties.RawEventData.FileSize` | `principal.process.file.size` | Mapped from changelog  
`properties.InitiatingProcessVersionInfoCompanyName` | `principal.user.company_name` | Mapped from changelog  
`properties.InitiatingProcessVersionInfoProductVersion` | `metadata.product_version` | Mapped from changelog  
`properties.InitiatingProcessVersionInfoInternalFileName` | `principal.resource.attribute.labels` | Mapped from changelog  
`properties.InitiatingProcessVersionInfoOriginalFileName` | `principal.resource.attribute.labels` | Mapped from changelog  
`properties.properties.InitiatingProcessVersionInfoFileDescription` | `principal.resource.attribute.labels` | Mapped from changelog  
`properties.AlertId` | `metadata.product_log_id` | Mapped from changelog  
`properties.ReportId` | `target.resource.product_object_id` | Mapped from changelog  
`properties.DeviceId` | `principal.asset_id` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/windows-defender-atp-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
