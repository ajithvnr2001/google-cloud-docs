---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/druva-backup/
title: Collect Druva Backup logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:45:27.416320+00:00
---

# Collect Druva Backup logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/druva-backup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Druva Backup logs

**Parser Version:** 2.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to collect Druva Backup logs by setting up a Google Cloud Run function that retrieves events from the Druva REST API and writes them to a Google Cloud Storage bucket, and then configuring a Google Security Operations feed using Google Cloud Storage V2.

Druva is a cloud-native data protection and management platform that provides backup, disaster recovery, and archival services for endpoints, SaaS applications, and enterprise workloads. The platform generates comprehensive audit trails, backup events, restore activities, and security alerts that can be integrated with SIEM solutions for monitoring and compliance.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A Google Cloud project with billing enabled
  * The following Google Cloud APIs enabled: 
    * Cloud Run functions API
    * Cloud Scheduler API
    * Cloud Storage API
    * Pub/Sub API
    * IAM API
  * Druva Cloud Administrator access to the Druva Cloud Platform Console
  * Access to the Druva Integration Center for API credential creation



## Create a Google Cloud Storage bucket

  1. Go to the [Google Cloud console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `druva-backup-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location closest to your Google SecOps instance (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.

**Note:** Save the bucket name. You will need it when configuring the Cloud Run function and the Google SecOps feed.



## Collect Druva API credentials

To enable the Cloud Run function to retrieve events from Druva, you need to create API credentials with OAuth 2.0 authentication.

### Create API credentials

  1. Sign in to the **Druva Cloud Platform Console**.
  2. From the **Global Navigation** menu, select **Integration Center**.
  3. In the left panel, click **API Credentials**.
  4. Click **New Credentials**.
  5. In the **New Credentials** window, provide the following details: **Name** : Enter a descriptive name (for example, `Google SecOps Cloud Storage Integration`).
  6. To apply authorization restrictions: 
     1. Select **Druva Cloud Administrator** to allow full access to data retrieval and modification.
     2. Alternatively, select **Product Administrator** and choose: **Cloud Admin (Read Only) role** : To restrict access to data retrieval only with no modification rights (recommended for SIEM integration)
  7. Click **Save**.



### Record API credentials

After creating the API credentials, the **Credential Details** window appears:

  1. Click the copy icon next to **Client ID** to copy the value to your clipboard.
  2. Save the Client ID securely (for example, `McNkxxxx4Vicxxxx4Ldpxxxx/09Uxxxx`).
  3. Click the copy icon next to **Secret Key** to copy the value to your clipboard.
  4. Save the Secret Key securely (for example, `Xmcxxxx8j5xxxx6NxxxxRbRxxxxNNyPt`).

**Important:** The Secret Key is displayed only once and cannot be retrieved after closing this dialog. If you lose your Secret Key, you must generate a new one by clicking **More options > Generate New Secret Key** on the API credential details page.**Note:** The Client ID and Secret Key are equivalent to username and password. They provide access to all Druva APIs and data. Do not share these credentials with unauthorized users.



## Create a service account

Create a dedicated service account for the Cloud Run function to access Google Cloud Storage.

  1. In the **Google Cloud console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `druva-backup-function` (or a descriptive name)
     * **Service account description** : Enter `Service account for Druva Backup Cloud Run function`
  4. Click **Create and Continue**.
  5. In the **Grant this service account access to project** section, add the following roles: 
     1. Click **Select a role** and select **Storage Object Admin**.
     2. Click **Add another role** and select **Cloud Run Invoker**.
  6. Click **Continue**.
  7. Click **Done**.
  8. Record the service account email (for example, `druva-backup-function@PROJECT_ID.iam.gserviceaccount.com`).

**Note:** The Storage Object Admin role allows the function to read and write state files and log files in the GCS bucket.



## Create a Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will use to trigger the Cloud Run function.

  1. In the **Google Cloud console** , go to **Pub/Sub > Topics**.
  2. Click **Create Topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `druva-backup-trigger`
  4. Uncheck **Add a default subscription**.
  5. Click **Create**.

**Note:** Save the full topic name (for example, `projects/PROJECT_ID/topics/druva-backup-trigger`). You will need it when configuring the Cloud Run function and Cloud Scheduler job.



## Create the Cloud Run function

### Prepare the function code

Create a Cloud Run function that authenticates with the Druva API using OAuth 2.0 client credentials, retrieves events via the events endpoint with pagination, and writes the results as NDJSON to the GCS bucket.

### Deploy the Cloud Run function

  1. In the **Google Cloud console** , go to **Cloud Run functions**.
  2. Click **Create Function**.
  3. Provide the following configuration details:

     * **Environment** : Select **2nd gen**
     * **Function name** : Enter `druva-backup-to-gcs`
     * **Region** : Select the region closest to your GCS bucket (for example, `us-central1`)
     * **Trigger type** : Select **Cloud Pub/Sub**
     * **Cloud Pub/Sub topic** : Select `druva-backup-trigger`
     * **Service account** : Select `druva-backup-function@PROJECT_ID.iam.gserviceaccount.com`
     * **Memory allocated** : `512 MiB`
     * **Timeout** : `540` seconds
     * **Maximum number of instances** : `1`
  4. Click **Next**.

  5. Select **Python 3.11** as the **Runtime**.

  6. Set the **Entry point** to `main`.

  7. In the **Source code** editor, replace the contents of `main.py` with the following:
         
         import base64
         import json
         import os
         import time
         from datetime import datetime, timezone, timedelta
         
         import requests
         from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
         
         GCS_BUCKET = os.environ["GCS_BUCKET"]
         GCS_PREFIX = os.environ.get("GCS_PREFIX", "druva_backup")
         STATE_KEY = os.environ.get("STATE_KEY", "druva_state.json")
         DRUVA_BASE_URL = os.environ.get("DRUVA_BASE_URL", "apis.druva.com")
         CLIENT_ID = os.environ["CLIENT_ID"]
         CLIENT_SECRET = os.environ["CLIENT_SECRET"]
         MAX_RECORDS = int(os.environ.get("MAX_RECORDS", "10000"))
         PAGE_SIZE = int(os.environ.get("PAGE_SIZE", "500"))
         LOOKBACK_HOURS = int(os.environ.get("LOOKBACK_HOURS", "24"))
         
         def get_oauth_token():
             """Obtain OAuth 2.0 access token using client credentials grant."""
             token_url = f"https://{DRUVA_BASE_URL}/token"
             payload = {
                 "grant_type": "client_credentials",
                 "scope": "read",
             }
             resp = requests.post(
                 token_url,
                 data=payload,
                 auth=(CLIENT_ID, CLIENT_SECRET),
                 timeout=30,
             )
             resp.raise_for_status()
             return resp.json()["access_token"]
         
         def load_state(storage_client):
             """Load the persisted state (last event time and tracker) from GCS."""
             bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(GCS_BUCKET)
             blob = bucket.blob(f"{GCS_PREFIX}/{STATE_KEY}")
             if blob.exists():
                 return json.loads(blob.[download_as_text](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_download_as_text)())
             return {}
         
         def save_state(storage_client, state):
             """Persist state to GCS."""
             bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(GCS_BUCKET)
             blob = bucket.blob(f"{GCS_PREFIX}/{STATE_KEY}")
             blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
                 json.dumps(state),
                 content_type="application/json",
             )
         
         def fetch_events(token, state):
             """Fetch events from Druva API with pagination via nextPageToken."""
             events_url = f"https://{DRUVA_BASE_URL}/insync/eventmanagement/v2/events"
             headers = {
                 "Authorization": f"Bearer {token}",
                 "Accept": "application/json",
             }
         
             params = {"pageSize": PAGE_SIZE}
         
             tracker = [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get("tracker")
             last_event_time = [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get("last_event_time")
         
             if tracker:
                 params["tracker"] = tracker
             elif last_event_time:
                 params["fromTime"] = last_event_time
             else:
                 lookback = datetime.now(timezone.utc) - timedelta(hours=LOOKBACK_HOURS)
                 params["fromTime"] = lookback.strftime("%Y-%m-%dT%H:%M:%SZ")
         
             all_events = []
             total_fetched = 0
         
             while total_fetched < MAX_RECORDS:
                 resp = requests.get(
                     events_url,
                     headers=headers,
                     params=params,
                     timeout=60,
                 )
                 resp.raise_for_status()
                 data = resp.json()
         
                 events = data.get("events", [])
                 all_events.extend(events)
                 total_fetched += len(events)
         
                 new_tracker = data.get("tracker")
                 next_page_token = data.get("nextPageToken")
         
                 if new_tracker:
                     state["tracker"] = new_tracker
         
                 if next_page_token:
                     params["nextPageToken"] = next_page_token
                     params.pop("tracker", None)
                     params.pop("fromTime", None)
                 else:
                     break
         
             if all_events:
                 last_ts = all_events[-1].get("eventTime", "")
                 if last_ts:
                     state["last_event_time"] = last_ts
         
             return all_events, state
         
         def write_events_to_gcs(storage_client, events):
             """Write events as NDJSON to GCS."""
             if not events:
                 return
         
             now = datetime.now(timezone.utc)
             filename = now.strftime("%Y%m%d_%H%M%S") + ".ndjson"
             blob_path = f"{GCS_PREFIX}/{now.strftime('%Y/%m/%d')}/{filename}"
         
             ndjson_lines = "\n".join(json.dumps(event) for event in events)
         
             bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(GCS_BUCKET)
             blob = bucket.blob(blob_path)
             blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
                 ndjson_lines,
                 content_type="application/x-ndjson",
             )
             print(f"Wrote {len(events)} events to gs://{GCS_BUCKET}/{blob_path}")
         
         def main(event, context):
             """Cloud Run function entry point triggered by Pub/Sub."""
             storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
         
             token = get_oauth_token()
         
             state = load_state(storage_client)
         
             events, updated_state = fetch_events(token, state)
         
             write_events_to_gcs(storage_client, events)
         
             save_state(storage_client, updated_state)
         
             print(f"Completed: fetched {len(events)} events")
             return f"OK: {len(events)} events"
         

  8. Replace the contents of `requirements.txt` with the following:
         
         requests>=2.31.0
         google-cloud-storage>=2.14.0
         




### Configure environment variables

  1. In the Cloud Run function configuration, go to the **Runtime, build, connections and security settings** section.
  2. Under **Runtime environment variables** , add the following variables:

     * `GCS_BUCKET`: The name of your GCS bucket (for example, `druva-backup-logs`)
     * `GCS_PREFIX`: The prefix path for log files (for example, `druva_backup`)
     * `STATE_KEY`: The state file name (for example, `druva_state.json`)
     * `DRUVA_BASE_URL`: The Druva API base URL: 
       * `apis.druva.com` for Druva Cloud (Standard)
       * `govcloudapis.druva.com` for Druva GovCloud
     * `CLIENT_ID`: The Client ID from the Druva API credentials
     * `CLIENT_SECRET`: The Secret Key from the Druva API credentials
     * `MAX_RECORDS`: Maximum number of records to fetch per invocation (for example, `10000`)
     * `PAGE_SIZE`: Number of events per API page (maximum `500`)
     * `LOOKBACK_HOURS`: Number of hours to look back on first run (for example, `24`)
**Note:** For production deployments, store the CLIENT_ID and CLIENT_SECRET in Google Cloud Secret Manager and reference them as secret environment variables instead of plain text.
  3. Click **Deploy**.

  4. Wait for the deployment to complete successfully.




## Create a Cloud Scheduler job

Create a Cloud Scheduler job to trigger the Cloud Run function at regular intervals.

  1. In the **Google Cloud console** , go to **Cloud Scheduler**.
  2. Click **Create Job**.
  3. Provide the following configuration details:

     * **Name** : Enter `druva-backup-scheduler`
     * **Region** : Select the same region as your Cloud Run function (for example, `us-central1`)
     * **Description** : Enter `Triggers Druva Backup log collection every 30 minutes`
     * **Frequency** : Enter `*/30 * * * *` (every 30 minutes)
     * **Timezone** : Select your preferred timezone (for example, `UTC`)
  4. Click **Continue**.

  5. Configure the **Target** :

     * **Target type** : Select **Pub/Sub**
     * **Cloud Pub/Sub topic** : Select `druva-backup-trigger`
     * **Message body** : Enter `{"trigger": "scheduled"}`
  6. Click **Create**.

**Note:** You can adjust the frequency based on your log volume requirements. For higher-volume environments, use `*/15 * * * *` (every 15 minutes). For lower-volume environments, use `0 * * * *` (every hour).



### Test the Cloud Scheduler job

  1. In the **Cloud Scheduler** list, locate `druva-backup-scheduler`.
  2. Click **Force Run** to trigger the function immediately.
  3. Verify the execution by checking: 
     * The Cloud Run function logs in **Cloud Run functions > druva-backup-to-gcs > Logs**
     * The GCS bucket for new NDJSON files in **Cloud Storage > druva-backup-logs**



## Retrieve the Google SecOps service account and configure the feed

### Get the service account email

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Druva Backup Events`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Druva Backup** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Do not use service accounts from other documentation or examples.



### Configure the feed

  1. Click **Next**.
  2. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://druva-backup-logs/druva_backup/
           

**Note:** Always include the trailing slash (/) at the end of the URI. Replace `druva-backup-logs` and `druva_backup` with your actual bucket name and prefix.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never** : Never deletes any files after transfers (recommended for testing)
       * **Delete transferred files** : Deletes files after successful transfer
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days)

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)

     * **Ingestion labels** : The label to be applied to the events from this feed

  3. Click **Next**.

  4. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## Grant IAM permissions to the Google SecOps service account

The Google SecOps service account needs **Storage Object Viewer** role on your GCS bucket to read the log files written by the Cloud Run function.

  1. Go to **Cloud Storage > Buckets**.
  2. Click on your bucket name (for example, `druva-backup-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Paste the Google SecOps service account email (for example, `chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com`)
     * **Assign roles** : Select **Storage Object Viewer**
  6. Click **Save**.

**Note:** If you selected the deletion option "Delete transferred files" or "Delete transferred files and empty directories," grant **Storage Object Admin** role instead of Storage Object Viewer.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
inSyncUserID, eventsGroupId, FilesMissed, FilesBackedup, TotalBackupSize, TotalBytesTransferred, facility, inSyncDataSourceID, initiator, event_type | additional.fields | Merged with labels created from each field if not empty  
initiator | extensions.auth.type | Set to "AUTHTYPE_UNSPECIFIED" if initiator matches email regex  
| metadata.event_type | Set to "USER_LOGIN" if has_target_user true and has_principal true; "STATUS_UPDATE" if has_principal true and has_target false; else "GENERIC_EVENT"  
eventID | metadata.product_log_id | Converted to string  
| metadata.product_name | Set to "DRUVA_BACKUP"  
clientVersion | metadata.product_version | Value copied directly  
inSyncDataSourceName | principal.asset.hostname | Value copied directly  
ip | principal.asset.ip | Merged from ip  
inSyncDataSourceName | principal.hostname | Value copied directly  
ip | principal.ip | Merged from ip  
clientOS | principal.platform | Set to "LINUX" if matches (?i)Linux; "WINDOWS" if matches (?i)windows; "MAC" if matches (?i)mac  
profileName | principal.resource.name | Value copied directly  
profileID | principal.resource.product_object_id | Converted to string  
eventState | security_result.action | Set to "ALLOW" if matches (?i)Success, else "BLOCK"  
eventState | security_result.action_details | Value copied directly  
severity | security_result.severity | Set to "LOW" if in [0,1,2,3,LOW]; "MEDIUM" if in [4,5,6,MEDIUM,SUBSTANTIAL,INFO]; "HIGH" if in [7,8,HIGH,SEVERE]; "CRITICAL" if in [9,10,VERY-HIGH,CRITICAL]  
inSyncUserEmail, initiator | target.user.email_addresses | Merged from inSyncUserEmail; also from initiator if matches email regex  
inSyncUserName | target.user.userid | Value copied directly  
| metadata.vendor_name | Set to "DRUVA_BACKUP"  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/druva-backup-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
