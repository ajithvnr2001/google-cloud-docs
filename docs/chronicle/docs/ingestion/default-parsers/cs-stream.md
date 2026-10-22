---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cs-stream/
title: Collect CrowdStrike Falcon Event Streams logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:54:56.994881+00:00
---

# Collect CrowdStrike Falcon Event Streams logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cs-stream/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect CrowdStrike Falcon Event Streams logs

**Parser Version:** 12.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest CrowdStrike Falcon Event Streams logs to Google Security Operations using Google Cloud Storage V2. CrowdStrike Falcon Event Streams provides a real-time streaming API that delivers security event data from the Falcon platform, including detection events, audit events, authentication activity, and incident updates. The Event Streams API uses a persistent HTTP connection with the `/sensors/entities/datafeed/v2` endpoint to push events in near real-time, supporting offset-based resumption for reliable delivery.

## Before you begin

Make sure you have the following prerequisites:

  * Google SecOps instance.
  * A GCP project with Cloud Storage API enabled.
  * Permissions to create and manage GCS buckets.
  * Permissions to manage IAM policies on GCS buckets.
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs.
  * Privileged access to **CrowdStrike Falcon Console** with permissions to create API clients.



## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `cs-stream-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Configure CrowdStrike Falcon API access

### Create API client

  1. Sign in to the **CrowdStrike Falcon Console**.
  2. In the navigation menu, go to **Support and resources > Resources and tools > API clients and keys**.
  3. Click **Create API client**.
  4. Provide the following configuration details: 
     * **Client name** : Enter a descriptive name (for example, `Google SecOps Event Streams Integration`).
     * **Description** (optional): Enter a description (for example, `API client for streaming events to GCS`).
  5. In the **API Scopes** section, select the following permission: 
     * **Event streams** : Select **Read** (required to consume the streaming API).
  6. Click **Create**.



### Record API credentials

After creating the API client, you receive the following credentials:

  * **Client ID** : A 32-character lowercase hexadecimal string.
  * **Client Secret** : A 40-character alphanumeric string.
  * **Base URL** : The fully qualified domain name for the CrowdStrike API (for example, `api.crowdstrike.com` or `api.us-2.crowdstrike.com`).



**Important** : Copy and save the **Client Secret** immediately. It is only displayed once and cannot be retrieved later.

**Note:** Store these credentials securely in a password manager or secrets management system.

### Regional endpoints

CrowdStrike operates in multiple regions with different API endpoints:

Region | Base URL  
---|---  
**US-1** | `api.crowdstrike.com`  
**US-2** | `api.us-2.crowdstrike.com`  
**EU-1** | `api.eu-1.crowdstrike.com`  
**US-GOV-1** | `api.laggar.gcw.crowdstrike.com`  
  
**Important** : Use the base URL that corresponds to your CrowdStrike Falcon Console login region.

### Verify permissions

To verify the API client has the required permissions:

  1. Sign in to the **CrowdStrike Falcon Console**.
  2. Navigate to **Support and resources > Resources and tools > API clients and keys**.
  3. Find the API client you created and verify that the **Event streams** scope shows **Read** access.



### Test API access

  * Test your credentials before proceeding with the integration:
        
        CLIENT_ID="<your-client-id>"
        CLIENT_SECRET="<your-client-secret>"
        BASE_URL="https://api.crowdstrike.com"
        
        # Get OAuth2 token
        TOKEN=$(curl -s -X POST "${BASE_URL}/oauth2/token" \
          -H "Content-Type: application/x-www-form-urlencoded" \
          -d "client_id=${CLIENT_ID}&client_secret=${CLIENT_SECRET}" | python3 -c "import sys,json; print(json.load(sys.stdin)['access_token'])")
        
        # Test Event Streams API access (discover available data feeds)
        curl -s -H "Authorization: Bearer ${TOKEN}" \
          "${BASE_URL}/sensors/entities/datafeed/v2?appId=secops-test&format=flatjson"
        




A successful response returns a JSON object containing `resources` with `dataFeedURL` and `sessionToken` fields for each available stream partition.

## Create service account for Cloud Run function

The Cloud Run function needs a service account with permissions to write to GCS bucket and be invoked by Pub/Sub.

### Create service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `cs-stream-collector-sa`
     * **Service account description** : Enter `Service account for Cloud Run function to collect CrowdStrike Event Streams logs`
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
  2. Click on your bucket name (for example, `cs-stream-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `cs-stream-collector-sa@PROJECT_ID.iam.gserviceaccount.com`)
     * **Assign roles** : Select **Storage Object Admin**
  6. Click **Save**.



## Create Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `cs-stream-trigger`
     * Leave other settings as default
  4. Click **Create**.



## Create Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to connect to the CrowdStrike Event Streams API, consume events, and write them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `cs-stream-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose `cs-stream-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select `cs-stream-collector-sa`
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `cs-stream-logs` | GCS bucket name  
`GCS_PREFIX` | `crowdstrike/stream` | Prefix for log files  
`STATE_KEY` | `crowdstrike/stream/state.json` | State file path  
`CS_BASE_URL` | `https://api.crowdstrike.com` | CrowdStrike API base URL  
`CS_CLIENT_ID` | `your-client-id` | API Client ID  
`CS_CLIENT_SECRET` | `your-client-secret` | API Client Secret  
`CS_APP_ID` | `secops-stream-collector` | Unique app ID for Event Streams (max 32 alphanumeric characters)  
`STREAM_TIMEOUT` | `300` | Stream read timeout in seconds  
`MAX_RECORDS` | `10000` | Max records per run  
  10. In the **Variables & Secrets** section, scroll down to **Requests** :

     * **Request timeout** : Enter `600` seconds (10 minutes)
  11. Go to the **Settings** tab:

     * In the **Resources** section: 
       * **Memory** : Select **512 MiB** or higher
       * **CPU** : Select **1**
  12. In the **Revision scaling** section:

     * **Minimum number of instances** : Enter `0`
     * **Maximum number of instances** : Enter `1` (only one stream consumer should run at a time)
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
           from datetime import datetime, timezone
           
           # Initialize HTTP client with timeouts
           http = urllib3.PoolManager(
               timeout=urllib3.Timeout(connect=5.0, read=30.0),
               retries=False,
           )
           
           # Initialize Storage client
           storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
           
           # Environment variables
           GCS_BUCKET = os.environ.get('GCS_BUCKET')
           GCS_PREFIX = os.environ.get('GCS_PREFIX', 'crowdstrike/stream')
           STATE_KEY = os.environ.get('STATE_KEY', 'crowdstrike/stream/state.json')
           CS_BASE_URL = os.environ.get('CS_BASE_URL', 'https://api.crowdstrike.com')
           CS_CLIENT_ID = os.environ.get('CS_CLIENT_ID')
           CS_CLIENT_SECRET = os.environ.get('CS_CLIENT_SECRET')
           CS_APP_ID = os.environ.get('CS_APP_ID', 'secops-stream-collector')
           STREAM_TIMEOUT = int(os.environ.get('STREAM_TIMEOUT', '300'))
           MAX_RECORDS = int(os.environ.get('MAX_RECORDS', '10000'))
           
           def get_oauth_token(base_url: str, client_id: str, client_secret: str) -> str:
               """Get CrowdStrike OAuth2 access token."""
               token_url = f"{base_url}/oauth2/token"
               body = f"client_id={client_id}&client_secret={client_secret}"
               response = http.request(
                   'POST', token_url,
                   body=body.encode('utf-8'),
                   headers={'Content-Type': 'application/x-www-form-urlencoded'}
               )
               if response.status != 200:
                   raise Exception(f"OAuth token request failed: {response.status}")
               data = json.loads(response.data.decode('utf-8'))
               return data['access_token']
           
           def refresh_stream_session(base_url: str, token: str, app_id: str, partition: int = 0):
               """Refresh an active stream session to keep it alive."""
               refresh_url = (
                   f"{base_url}/sensors/entities/datafeed-actions/v1/{partition}"
                   f"?appId={app_id}&action_name=refresh_active_stream_session"
               )
               response = http.request(
                   'POST', refresh_url,
                   headers={
                       'Authorization': f'Bearer {token}',
                       'Content-Type': 'application/json',
                   }
               )
               if response.status == 200:
                   print("Stream session refreshed successfully")
               else:
                   print(f"Warning: Stream session refresh returned {response.status}")
           
           @functions_framework.cloud_event
           def main(cloud_event):
               """
               Cloud Run function triggered by Pub/Sub to fetch CrowdStrike
               Event Streams data and write to GCS.
               """
           
               if not all([GCS_BUCKET, CS_BASE_URL, CS_CLIENT_ID, CS_CLIENT_SECRET]):
                   print('Error: Missing required environment variables')
                   return
           
               try:
                   bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(GCS_BUCKET)
           
                   # Load state
                   state = load_state(bucket, STATE_KEY)
           
                   # Get OAuth token
                   token = get_oauth_token(CS_BASE_URL, CS_CLIENT_ID, CS_CLIENT_SECRET)
                   headers = {
                       'Authorization': f'Bearer {token}',
                       'Accept': 'application/json',
                   }
           
                   # Discover available data feeds
                   discover_url = (
                       f"{CS_BASE_URL}/sensors/entities/datafeed/v2"
                       f"?appId={CS_APP_ID}&format=flatjson"
                   )
                   response = http.request('GET', discover_url, headers=headers)
           
                   if response.status != 200:
                       print(f"Failed to discover data feed: {response.status}")
                       print(f"Response: {response.data.decode('utf-8')}")
                       return
           
                   feed_data = json.loads(response.data.decode('utf-8'))
                   resources = feed_data.get('resources', [])
           
                   if not resources:
                       print("No data feed resources available")
                       return
           
                   feed_url = resources[0].get('dataFeedURL', '')
                   session_token = resources[0].get(
                       'sessionToken', {}
                   ).get('token', '')
           
                   if not feed_url or not session_token:
                       print("Missing feed URL or session token")
                       return
           
                   # Build stream URL with offset if available
                   stream_url = feed_url
                   offset = [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get('offset')
                   if offset:
                       stream_url = f"{feed_url}&offset={offset}"
           
                   # Connect to Event Stream
                   stream_headers = {
                       'Authorization': f'Token {session_token}',
                       'Accept': 'application/json',
                       'Connection': 'keep-alive',
                   }
           
                   stream_http = urllib3.PoolManager(
                       timeout=urllib3.Timeout(
                           connect=10.0, read=float(STREAM_TIMEOUT)
                       ),
                       retries=False,
                   )
           
                   print(f"Connecting to Event Stream...")
                   resp = stream_http.request(
                       'GET', stream_url,
                       headers=stream_headers,
                       preload_content=False
                   )
           
                   if resp.status != 200:
                       print(f"Stream connection failed: {resp.status}")
                       return
           
                   records = []
                   latest_offset = offset
                   now = datetime.now(timezone.utc)
           
                   for line in resp.stream(4096):
                       decoded = line.decode('utf-8').strip()
                       if not decoded:
                           continue
           
                       try:
                           event = json.loads(decoded)
                           records.append(event)
           
                           event_offset = event.get(
                               'metadata', {}
                           ).get('offset')
                           if event_offset is not None:
                               latest_offset = event_offset
           
                           if len(records) >= MAX_RECORDS:
                               print(
                                   f"Reached max records limit ({MAX_RECORDS})"
                               )
                               break
                       except json.JSONDecodeError:
                           continue
           
                   resp.release_conn()
           
                   if not records:
                       print("No new events found in stream.")
                       # Refresh stream session to keep it alive
                       refresh_stream_session(
                           CS_BASE_URL, token, CS_APP_ID
                       )
                       return
           
                   # Write to GCS as NDJSON
                   timestamp = now.strftime('%Y%m%d_%H%M%S')
                   object_key = f"{GCS_PREFIX}/logs_{timestamp}.ndjson"
                   blob = bucket.blob(object_key)
           
                   ndjson = '\n'.join(
                       [json.dumps(r, ensure_ascii=False) for r in records]
                   ) + '\n'
                   blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
                       ndjson, content_type='application/x-ndjson'
                   )
           
                   print(
                       f"Wrote {len(records)} records to "
                       f"gs://{GCS_BUCKET}/{object_key}"
                   )
           
                   # Save state with latest offset
                   new_state = {
                       'offset': latest_offset,
                       'last_run': now.isoformat()
                   }
                   save_state(bucket, STATE_KEY, new_state)
           
                   # Refresh stream session to keep it alive
                   refresh_stream_session(
                       CS_BASE_URL, token, CS_APP_ID
                   )
           
                   print(f"Successfully processed {len(records)} events")
           
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
           
           def save_state(bucket, key, state: dict):
               """Save state to GCS."""
               try:
                   blob = bucket.blob(key)
                   blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
                       json.dumps(state, indent=2),
                       content_type='application/json'
                   )
                   print(f"Saved state: {[state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state)}")
               except Exception as e:
                   print(f"Warning: Could not save state: {e}")
           

**requirements.txt:**
    
    ```none
    functions-framework==3.*
    google-cloud-storage==2.*
    urllib3>=2.0.0
    ```
    

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
**Name** | `cs-stream-collector-scheduled`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `*/15 * * * *` (every 15 minutes)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select `cs-stream-trigger`  
**Message body** | `{}` (empty JSON object)  
  4. Click **Create**.




### Test the integration

  1. In the **Cloud Scheduler** console, find your job.
  2. Click **Force run** to trigger the job manually.
  3. Wait a few seconds.
  4. Go to **Cloud Run > Services**.
  5. Click on `cs-stream-collector`.
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         Connecting to Event Stream...
         Wrote X records to gs://cs-stream-logs/crowdstrike/stream/logs_YYYYMMDD_HHMMSS.ndjson
         Stream session refreshed successfully
         Successfully processed X events
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click on `cs-stream-logs`.

  10. Navigate to the `crowdstrike/stream/` folder.

  11. Verify that a new `.ndjson` file was created with the current timestamp.




If you see errors in the logs:

  * **HTTP 401** : Check API credentials in environment variables
  * **HTTP 403** : Verify API client has **Event streams: Read** scope
  * **HTTP 429** : Rate limiting - adjust scheduler frequency or increase `STREAM_TIMEOUT`
  * **Missing environment variables** : Check all required variables are set
  * **No data feed resources available** : Verify `CS_APP_ID` is unique and does not exceed 32 alphanumeric characters



## Retrieve the Google SecOps service account

Google SecOps uses a unique service account to read data from your GCS bucket. You must grant this service account access to your bucket.

### Get the service account email

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `CrowdStrike Event Streams logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **CrowdStrike Falcon Streaming** as the **Log type**.
  7. Click **Get Service Account**.
  8. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  9. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Don't use service accounts from other documentation or examples.
  10. Click **Next**.

  11. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://cs-stream-logs/crowdstrike/stream/
           

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
  2. Click on `cs-stream-logs`.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Paste the Google SecOps service account email
     * **Assign roles** : Select **Storage Object Viewer**
  6. Click **Save**.

**Note:** If you plan to use the deletion option "Delete transferred files" or "Delete transferred files and empty directories," grant **Storage Object Admin** role instead of Storage Object Viewer.



## Need more help?

For more information about Google Security Operations feeds, see [Google Security Operations feeds documentation](https://docs.cloud.google.com/chronicle/docs/administration/feed-management). For information about requirements for each feed type, see [Feed configuration by type](https://docs.cloud.google.com/chronicle/docs/reference/feed-management-api#feed_configuration_by_type).

For reference, see the [CrowdStrike Falcon Event Streams parser documentation](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cs-stream).

## UDM mapping delta reference

On September 15, 2026, Google SecOps released a new version of the CrowdStrike Falcon Event Streams parser, which includes significant changes to the mapping of CrowdStrike Falcon Event Streams log fields to UDM fields.

### Log-field mapping delta

The following table lists the mapping delta for CrowdStrike Falcon Event Streams log-to-UDM fields exposed before September 15, 2026, and subsequently (listed in the **Old mapping** and **New mapping** columns, respectively):

Log field | Old mapping | New mapping | Reason for change  
---|---|---|---  
`deviceId` | `additional.fields` | `principal.asset.asset_id` | Mapped to a more specific UDM field instead of labels.  
`event.AuditKeyValues (report_name)` | `security_result.detection_fields` | `target.file.names` | Mapped to a more specific UDM field instead of labels.  
`event.IdpPolicyRuleName` | `security_result.detection_fields` | `security_result.rule_name` | Mapped to a more specific UDM field instead of labels.  
`event.MitreAttack.TacticID` | `security_result.detection_fields` | `security_result.tactic.id` | Mapped to a more specific UDM field instead of labels.  
`event.MitreAttack.TechniqueID` | `security_result.detection_fields` | `security_result.technique.id` | Mapped to a more specific UDM field instead of labels.  
`event.NetworkAccesse.RemoteAddress` | `principal.ip` | `target.ip` | Updated because `event.NetworkAccesse.RemoteAddress` represents the target device address.  
`event.TacticId` | `security_result.detection_fields` | `security_result.tactic.id` | Mapped to a more specific UDM field instead of labels.  
`event.TechniqueId` | `security_result.detection_fields` | `security_result.technique.id` | Mapped to a more specific UDM field instead of labels.  
`event.UserId` | `principal.user.userid` | `principal.user.email_addresses`,  
`principal.user.userid` | If `event.UserId` is an email address, it maps to `principal.user.email_addresses`; otherwise, it maps to `principal.user.userid`.  
`remoteAddress` | `principal.ip` | `target.ip` | Updated because `remoteAddress` represents the target device address.  
`ruleName` | `security_result.detection_fields` | `security_result.rule_name` | Mapped to a more specific UDM field instead of labels.  
`serviceName` | `metadata.description`,  
`target.application` | `target.application` | Removed redundant mapping.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cs-stream-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
