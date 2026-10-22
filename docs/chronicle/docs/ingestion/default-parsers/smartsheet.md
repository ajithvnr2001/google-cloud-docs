---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/smartsheet/
title: Collect Smartsheet logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:37:55.180993+00:00
---

# Collect Smartsheet logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/smartsheet/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Smartsheet logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Smartsheet logs to Google Security Operations using Google Cloud Storage.

Smartsheet is a collaborative work management platform that provides spreadsheet-like project management, task tracking, and workflow automation for enterprise teams. The Event Reporting API provides audit logs covering 100+ event types including user actions, data access, sharing changes, and administrative operations across your Smartsheet organization.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run functions, Pub/Sub topics, and Cloud Scheduler jobs
  * A Smartsheet Enterprise plan with Event Reporting add-on enabled
  * A Smartsheet System Admin account with API access



## Collect Smartsheet API credentials

### Generate an API access token

  1. Sign in to your [Smartsheet](https://app.smartsheet.com/) account with a System Admin account.
  2. At the bottom of the left navigation bar, select your **Account** (profile image), then go to **Personal Settings**.
  3. Navigate to the **API Access** tab.
  4. Click **Generate new access token**.
  5. Enter a name for the token (for example, `SecOps SIEM Integration`).
  6. Click **OK**.
  7. Copy and save the access token securely.

**Note:** The access token is displayed only once. If you lose it, you must revoke the token and generate a new one. Only licensed Smartsheet users on Business and Enterprise plans have access to the API.



### Verify permissions

To verify the account has the required permissions:

  1. Sign in to your Smartsheet account.
  2. Go to **Account** (profile image) **> Personal Settings > API Access**.
  3. If you can see the **Manage API Access Tokens** page and generate tokens, you have the required permissions.
  4. If you cannot access these options, contact your Smartsheet System Admin to grant API access.



### Test API access

  * Test your credentials before proceeding with the integration:
        
        # Replace with your actual access token
        SMARTSHEET_TOKEN="<your-access-token>"
        
        # Test Event Reporting API access
        curl -v -H "Authorization: Bearer ${SMARTSHEET_TOKEN}" \
          "https://api.smartsheet.com/2.0/events?since=$(date -u -d '1 hour ago' +%Y-%m-%dT%H:%M:%SZ)&maxCount=10"
        




If you see these errors:

  * **HTTP 401** : Verify the access token is correct.
  * **HTTP 403** : Confirm the account has System Admin privileges and the Event Reporting add-on is enabled for your plan.



## Create a Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `smartsheet-audit-logs`)  
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
     * **Service account name** : Enter `smartsheet-logs-sa`.
     * **Service account description** : Enter `Service account for Cloud Run function to collect Smartsheet audit logs`.
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



### Grant IAM permissions on the GCS bucket

Grant the service account write permissions on the GCS bucket:

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name (for example, `smartsheet-audit-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `smartsheet-logs-sa@PROJECT_ID.iam.gserviceaccount.com`).
     * **Assign roles** : Select **Storage Object Admin**.
  6. Click **Save**.



## Create a Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `smartsheet-logs-trigger`.
     * Leave other settings as default.
  4. Click **Create**.



## Create a Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from Smartsheet Event Reporting API and write them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `smartsheet-logs-to-gcs`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose `smartsheet-logs-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select `smartsheet-logs-sa`.
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value  
---|---  
`GCS_BUCKET` | `smartsheet-audit-logs`  
`GCS_PREFIX` | `smartsheet/events/`  
`STATE_KEY` | `smartsheet/events/state.json`  
`SMARTSHEET_TOKEN` | `<your-smartsheet-access-token>`  
`MAX_COUNT` | `1000`  
`TIMEOUT` | `30`  
**Note:** The `MAX_COUNT` value controls the maximum number of events returned per API request. The Smartsheet Event Reporting API supports a maximum of 10,000 events per request; 1,000 is recommended for consistent performance.
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

  15. After the service is created, the **inline code editor** will open automatically.




### Add the function code

  1. Enter **main** in **Function entry point**.
  2. In the inline code editor, create two files:

     * First file: **main.py:**
           
           import functions_framework
           from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
           import json
           import os
           import urllib3
           from datetime import datetime, timezone
           import uuid
           import gzip
           import io
           
           # Initialize HTTP client with timeouts
           http = urllib3.PoolManager(
             timeout=urllib3.Timeout(connect=5.0, read=30.0),
             retries=False,
           )
           
           # Initialize Storage client
           storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
           
           # Environment variables
           GCS_BUCKET = os.environ.get('GCS_BUCKET')
           GCS_PREFIX = os.environ.get('GCS_PREFIX', 'smartsheet/events/')
           STATE_KEY = os.environ.get('STATE_KEY', 'smartsheet/events/state.json')
           SMARTSHEET_TOKEN = os.environ.get('SMARTSHEET_TOKEN')
           MAX_COUNT = int(os.environ.get('MAX_COUNT', '1000'))
           TIMEOUT = int(os.environ.get('TIMEOUT', '30'))
           
           EVENTS_URL = "https://api.smartsheet.com/2.0/events"
           
           @functions_framework.cloud_event
           def main(cloud_event):
             """
             Cloud Run function triggered by Pub/Sub to fetch Smartsheet
             Event Reporting audit logs and write to GCS.
           
             Args:
               cloud_event: CloudEvent object containing Pub/Sub message
             """
           
             if not all([GCS_BUCKET, SMARTSHEET_TOKEN]):
               print('Error: Missing required environment variables')
               return
           
             try:
               bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(GCS_BUCKET)
           
               # Load state
               state = load_state(bucket, STATE_KEY)
               stream_position = [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get('stream_position')
           
               print(f'Fetching events from stream position: {stream_position or "latest"}')
           
               # Fetch events
               total_written = 0
               has_more = True
           
               while has_more:
                 events, new_position, more = fetch_events(stream_position)
           
                 if events:
                   write_chunk(bucket, events, datetime.now(timezone.utc))
                   total_written += len(events)
           
                 if new_position:
                   stream_position = new_position
           
                 has_more = more and total_written < 50000
           
               # Save state
               state['stream_position'] = stream_position
               save_state(bucket, STATE_KEY, state)
           
               print(f'Successfully processed {total_written} events')
           
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
               print(f'Warning: Could not load state: {str(e)}')
           
             return {}
           
           def save_state(bucket, key, state):
             """Save state to GCS."""
             try:
               state['updated_at'] = datetime.now(timezone.utc).isoformat()
               blob = bucket.blob(key)
               blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
                 json.dumps(state),
                 content_type='application/json'
               )
             except Exception as e:
               print(f'Warning: Could not save state: {str(e)}')
           
           def write_chunk(bucket, items, ts):
             """Write log chunk to GCS as compressed NDJSON."""
             key = f"{GCS_PREFIX}{ts:%Y/%m/%d}/smartsheet-events-{uuid.uuid4()}.json.gz"
           
             buf = io.BytesIO()
             with gzip.GzipFile(fileobj=buf, mode='w') as gz:
               for rec in items:
                 gz.write((json.dumps(rec) + '\n').encode('utf-8'))
           
             buf.seek(0)
             blob = bucket.blob(key)
             blob.[upload_from_file](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_file)(buf, content_type='application/gzip')
           
             print(f'Wrote {len(items)} events to {key}')
             return key
           
           def fetch_events(stream_position):
             """
             Fetch events from Smartsheet Event Reporting API.
           
             The API uses a streaming model with streamPosition for pagination.
             On first call (no streamPosition), it returns the current position
             without events. Subsequent calls return events since the position.
           
             Returns:
               Tuple of (events list, new stream position, has more data)
             """
             headers = {
               'Authorization': f'Bearer {SMARTSHEET_TOKEN}',
               'Accept': 'application/json'
             }
           
             params = [f'maxCount={MAX_COUNT}']
             if stream_position:
               params.append(f'streamPosition={stream_position}')
           
             url = f"{EVENTS_URL}?{'&'.join(params)}"
           
             response = http.request(
               'GET',
               url,
               headers=headers,
               timeout=TIMEOUT
             )
           
             if response.status == 429:
               retry_after = int(response.headers.get('Retry-After', '60'))
               print(f'Rate limited (429). Retry-After: {retry_after}s')
               import time
               time.sleep(min(retry_after, 120))
               return fetch_events(stream_position)
           
             if response.status != 200:
               print(f'API request failed: {response.status}')
               response_text = response.data.decode('utf-8')
               print(f'Response body: {response_text}')
               raise Exception(f'Failed to fetch events: {response.status}')
           
             data = json.loads(response.data.decode('utf-8'))
           
             events = data.get('data', []) or []
             new_position = data.get('nextStreamPosition')
             more_available = data.get('moreEventsAvailable', False)
           
             if events:
               print(f'Retrieved {len(events)} events')
           
             return events, new_position, more_available
           

     * Second file: **requirements.txt:**
           
           functions-framework==3.*
           google-cloud-storage==2.*
           urllib3>=2.0.0
           

  3. Click **Deploy** to save and deploy the function.

  4. Wait for deployment to complete (2-3 minutes).

**Note:** The Pub/Sub trigger configuration automatically creates the necessary subscriptions and permissions. The Smartsheet Event Reporting API uses a streaming model with `streamPosition` for pagination. On the first run (without a saved stream position), the API returns the current position without events. Subsequent runs fetch events that occurred since the saved position.



## Create a Cloud Scheduler job

Cloud Scheduler will publish messages to the Pub/Sub topic at regular intervals, triggering the Cloud Run function.

  1. In the **GCP Console** , go to **Cloud Scheduler**.
  2. Click **Create Job**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | `smartsheet-logs-schedule-15min`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `*/15 * * * *` (every 15 minutes)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select `smartsheet-logs-trigger`  
**Message body** | `{}` (empty JSON object)  
  4. Click **Create**.




### Schedule frequency options

Choose frequency based on log volume and latency requirements:

Frequency | Cron Expression | Use Case  
---|---|---  
Every 5 minutes | `*/5 * * * *` | High-volume, low-latency  
Every 15 minutes | `*/15 * * * *` | Standard (recommended)  
Every hour | `0 * * * *` | Low volume  
Every 6 hours | `0 */6 * * *` | Batch processing  
  
### Test the integration

  1. In the **Cloud Scheduler** console, find your job (for example, `smartsheet-logs-schedule-15min`).
  2. Click **Force run** to trigger the job manually.
  3. Wait a few seconds.
  4. Go to **Cloud Run > Services**.
  5. Click on the function name (`smartsheet-logs-to-gcs`).
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         Fetching events from stream position: <position>
         Retrieved X events
         Wrote X events to smartsheet/events/YYYY/MM/DD/smartsheet-events-UUID.json.gz
         Successfully processed X events
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click your bucket name (`smartsheet-audit-logs`).

  10. Navigate to the prefix folder (`smartsheet/events/`).

  11. Verify that a new `.json.gz` file was created with the current timestamp.




If you see errors in the logs:

  * **HTTP 401** : Check the Smartsheet access token in environment variables
  * **HTTP 403** : Verify the account has System Admin privileges and Event Reporting is enabled
  * **HTTP 429** : Rate limiting - the function will automatically retry with backoff
  * **Missing environment variables** : Check all required variables are set in Cloud Run function configuration



## Retrieve the Google SecOps service account

Google SecOps uses a unique service account to read data from your GCS bucket. You must grant this service account access to your bucket.

## Configure a feed in Google SecOps to ingest Smartsheet logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Smartsheet Audit Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Smartsheet** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address. You will use it in the next step.

**Note:** Each Google SecOps instance has a unique service account. Do not use service accounts from other documentation or examples.
  9. Click **Next**.

  10. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
    
    gs://smartsheet-audit-logs/smartsheet/events/
    

     * Replace:

       * `smartsheet-audit-logs`: Your GCS bucket name.
       * `smartsheet/events/`: Prefix path where logs are stored.
**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference: 
       * **Never** : Never deletes any files after transfers (recommended for testing).
       * **Delete transferred files** : Deletes files after successful transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.
**Note:** If you select a deletion option, the service account must have **Storage Object Admin** role instead of Storage Object Viewer. Update IAM permissions accordingly.
     * **Maximum File Age** : Include files modified in the last number of days. Default is 180 days.
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).
     * **Ingestion labels** : The label to be applied to the events from this feed.
  11. Click **Next**.

  12. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## Grant IAM permissions to the Google SecOps service account

The Google SecOps service account needs **Storage Object Viewer** role on your GCS bucket.

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name (for example, `smartsheet-audit-logs`).
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
`accessLevel_label` | `additional.fields` | Merged  
`appName_label` | `additional.fields` | Merged  
`attachmentName_label` | `additional.fields` | Merged  
`cellLinkSourceSheetId_label` | `additional.fields` | Merged  
`dashboardName_label` | `additional.fields` | Merged  
`folderName_label` | `additional.fields` | Merged  
`formatType_label` | `additional.fields` | Merged  
`includeAttachments_label` | `additional.fields` | Merged  
`includeDiscussions_label` | `additional.fields` | Merged  
`mergeType_label` | `additional.fields` | Merged  
`rowCount_label` | `additional.fields` | Merged  
`rowsMoved_label` | `additional.fields` | Merged  
`sheetId_label` | `additional.fields` | Merged  
`sheetName_label` | `additional.fields` | Merged  
`sheetRowId_label` | `additional.fields` | Merged  
`sourceFolderId_label` | `additional.fields` | Merged  
`sourceObjectId_label` | `additional.fields` | Merged  
`sourceSheetId_label` | `additional.fields` | Merged  
`sourceType_label` | `additional.fields` | Merged  
`tokenDisplayValue_label` | `additional.fields` | Merged  
`tokenUserId_label` | `additional.fields` | Merged  
`userId_label` | `additional.fields` | Merged  
`workspaceId_label` | `additional.fields` | Merged  
`additionalDetails.accessScopes` | `metadata.description` | Directly mapped  
`additionalDetails_tokenExpirationTimestamp` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ssZ`  
`eventTimestamp` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ssZ`  
`has_principal` | `metadata.event_type` | Mapped: `true` → `USER_UNCATEGORIZED`  
`accessTokenName` | `metadata.product_log_id` | Directly mapped  
`eventId` | `metadata.product_log_id` | Directly mapped  
`additionalDetails.appClientId` | `principal.user.userid` | Directly mapped  
`requestUserId` | `principal.user.userid` | Directly mapped  
`object_id` | `security_result.about.labels` | Merged  
`source_label` | `security_result.about.labels` | Merged  
`object_type` | `security_result.about.resource.attribute.labels` | Merged  
`action` | `security_result.action_details` | Directly mapped  
`userId` | `target.user.userid` | Directly mapped  
N/A | `metadata.event_type` | Constant: `USER_UNCATEGORIZED`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/smartsheet-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
