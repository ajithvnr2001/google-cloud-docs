---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/bitwarden-event/
title: Collect Bitwarden Enterprise Event Logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:09:49.740899+00:00
---

# Collect Bitwarden Enterprise Event Logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/bitwarden-event/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Bitwarden Enterprise Event Logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Bitwarden Enterprise Event Logs to Google Security Operations using Google Cloud Storage. The parser transforms raw JSON formatted event logs into a structured format conforming to the SecOps UDM. It extracts relevant fields like user details, IP addresses, and event types, mapping them to corresponding UDM fields for consistent security analysis.

## Before you begin

Ensure that you have the following prerequisites:

  * A Google SecOps instance
  * Privileged access to Bitwarden tenant
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs



## Get Bitwarden API key and URL

  1. In the **Bitwarden Admin Console** , go to **Settings > Organization info > View API key**.
  2. Copy and save the following details to a secure location: 
     * **Client ID**
     * **Client Secret**
  3. Determine your Bitwarden endpoints (based on region):

     * **IDENTITY_URL** = `https://identity.bitwarden.com/connect/token` (EU: `https://identity.bitwarden.eu/connect/token`)
     * **API_BASE** = `https://api.bitwarden.com` (EU: `https://api.bitwarden.eu`)
**Note:** Bitwarden Enterprise Organizations typically need the Events feature enabled for organization events to be available. In the Admin Console, go to **Settings > Organization settings** to verify that Events are enabled if you are not receiving events from the API.**Note:** Only organization owners (and other roles Bitwarden permits) can view or rotate the Organization API key. The organization API key used here must be an Organization API (scope api.organization, client_id starting with "organization.") and not a personal API key.



## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `bitwarden-events`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Collect Bitwarden API prerequisites

You have already collected the Bitwarden API credentials in the previous step:

  * **Client ID** : Organization client ID from Bitwarden Admin Console
  * **Client Secret** : Organization client secret from Bitwarden Admin Console
  * **IDENTITY_URL** : `https://identity.bitwarden.com/connect/token` (or EU endpoint)
  * **API_BASE** : `https://api.bitwarden.com` (or EU endpoint)



## Create service account for Cloud Run function

The Cloud Run function needs a service account with permissions to write to GCS bucket and be invoked by Pub/Sub.

### Create service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `bitwarden-events-collector-sa`.
     * **Service account description** : Enter `Service account for Cloud Run function to collect Bitwarden Enterprise Event logs`.
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
  2. Click your bucket name.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `bitwarden-events-collector-sa@PROJECT_ID.iam.gserviceaccount.com`).
     * **Assign roles** : Select **Storage Object Admin**.
  6. Click **Save**.



## Create Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `bitwarden-events-trigger`.
     * Leave other settings as default.
  4. Click **Create**.



## Create Cloud Run function to collect logs

The Cloud Run function is triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from Bitwarden Events API and writes them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `bitwarden-events-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose the Pub/Sub topic (`bitwarden-events-trigger`).
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub automatically handles authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select the service account (`bitwarden-events-collector-sa`).
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value  
---|---  
`GCS_BUCKET` | `bitwarden-events`  
`GCS_PREFIX` | `bitwarden/events`  
`STATE_KEY` | `bitwarden/events/state.json`  
`BW_CLIENT_ID` | `organization.your-client-id`  
`BW_CLIENT_SECRET` | `your-client-secret`  
`IDENTITY_URL` | `https://identity.bitwarden.com/connect/token`  
`API_BASE` | `https://api.bitwarden.com`  
`MAX_PAGES` | `10`  
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

  15. After the service is created, the **inline code editor** opens automatically.




### Add function code

  1. Enter **main** in **Function entry point**
  2. In the inline code editor, create two files:

     * First file: **main.py:**
    
    import functions_framework
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    import json
    import os
    import urllib3
    from datetime import datetime, timezone
    import base64
    
    # Initialize HTTP client with timeouts
    http = urllib3.PoolManager(
        timeout=urllib3.Timeout(connect=5.0, read=30.0),
        retries=False,
    )
    
    # Initialize Storage client
    storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    
    @functions_framework.cloud_event
    def main(cloud_event):
        """
        Cloud Run function triggered by Pub/Sub to fetch events from Bitwarden API and write to GCS.
    
        Args:
            cloud_event: CloudEvent object containing Pub/Sub message
        """
    
        # Get environment variables
        bucket_name = os.environ.get('GCS_BUCKET')
        prefix = os.environ.get('GCS_PREFIX', 'bitwarden/events').strip('/')
        state_key = os.environ.get('STATE_KEY', 'bitwarden/events/state.json')
    
        # Bitwarden API credentials
        identity_url = os.environ.get('IDENTITY_URL', 'https://identity.bitwarden.com/connect/token')
        api_base = os.environ.get('API_BASE', 'https://api.bitwarden.com').rstrip('/')
        client_id = os.environ.get('BW_CLIENT_ID')
        client_secret = os.environ.get('BW_CLIENT_SECRET')
        max_pages = int(os.environ.get('MAX_PAGES', '10'))
    
        if not all([bucket_name, client_id, client_secret]):
            print('Error: Missing required environment variables')
            return
    
        try:
            # Get GCS bucket
            bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
    
            # Load state (continuation token)
            state = load_state(bucket, state_key)
            continuation_token = [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get('continuationToken')
    
            print(f'Processing events with continuation token: {continuation_token}')
    
            # Get OAuth token
            access_token = get_oauth_token(identity_url, client_id, client_secret)
    
            # Fetch events from Bitwarden API
            run_timestamp = int(datetime.now(timezone.utc).timestamp())
            pages = 0
            total_events = 0
            written_files = []
    
            while pages < max_pages:
                events_data = fetch_events(api_base, access_token, continuation_token)
    
                # Extract events array from API response
                events = events_data.get('data', [])
    
                # Only write file if there are events
                if events:
                    gcs_key = write_events_jsonl(bucket, events, prefix, run_timestamp, pages)
                    if gcs_key:
                        written_files.append(gcs_key)
                    total_events += len(events)
    
                pages += 1
    
                # Check for next page token
                next_token = events_data.get('continuationToken')
                if next_token:
                    continuation_token = next_token
                    continue
                else:
                    # No more pages
                    break
    
            # Save state only if there are more pages to continue in next run
            # If we hit MAX_PAGES and there's still a continuation token, save it
            # Otherwise, clear the state (set to None)
            save_state(bucket, state_key, {
                'continuationToken': continuation_token if pages >= max_pages and continuation_token else None
            })
    
            print(f'Successfully processed {total_events} events across {pages} pages')
            print(f'Files written: {len(written_files)}')
    
        except Exception as e:
            print(f'Error processing events: {str(e)}')
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
            blob = bucket.blob(key)
            blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
                json.dumps(state),
                content_type='application/json'
            )
        except Exception as e:
            print(f'Warning: Could not save state: {str(e)}')
    
    def get_oauth_token(identity_url, client_id, client_secret):
        """Get OAuth 2.0 access token from Bitwarden."""
        body_data = {
            'grant_type': 'client_credentials',
            'scope': 'api.organization',
            'client_id': client_id,
            'client_secret': client_secret
        }
    
        encoded_data = '&'.join([f'{k}={v}' for k, v in body_data.items()]).encode('utf-8')
    
        response = http.request(
            'POST',
            identity_url,
            body=encoded_data,
            headers={'Content-Type': 'application/x-www-form-urlencoded'}
        )
    
        if response.status != 200:
            raise Exception(f'Failed to get OAuth token: {response.status} {response.data.decode("utf-8")}')
    
        token_data = json.loads(response.data.decode('utf-8'))
        return token_data['access_token']
    
    def fetch_events(api_base, access_token, continuation_token=None):
        """Fetch events from Bitwarden API with pagination."""
        url = f'{api_base}/public/events'
        if continuation_token:
            url += f'?continuationToken={continuation_token}'
    
        response = http.request(
            'GET',
            url,
            headers={
                'Authorization': f'Bearer {access_token}',
                'Accept': 'application/json'
            }
        )
    
        if response.status == 429:
            retry_after = int(response.headers.get('Retry-After', '60'))
            print(f'Rate limited (429). Retrying after {retry_after}s...')
            import time
            time.sleep(retry_after)
            return fetch_events(api_base, access_token, continuation_token)
    
        if response.status != 200:
            raise Exception(f'Failed to fetch events: {response.status} {response.data.decode("utf-8")}')
    
        return json.loads(response.data.decode('utf-8'))
    
    def write_events_jsonl(bucket, events, prefix, run_timestamp, page_index):
        """
        Write events in JSONL format (one JSON object per line).
        Only writes if there are events to write.
        Returns the GCS key of the written file.
        """
        if not events:
            return None
    
        # Build JSONL content: one event per line
        lines = [json.dumps(event, separators=(',', ':')) for event in events]
        jsonl_content = '\n'.join(lines) + '\n'  # JSONL format with trailing newline
    
        # Generate unique filename with page number to avoid conflicts
        timestamp_str = datetime.fromtimestamp(run_timestamp, tz=timezone.utc).strftime('%Y/%m/%d/%H%M%S')
        key = f'{prefix}/{timestamp_str}-page{page_index:05d}-bitwarden-events.jsonl'
    
        blob = bucket.blob(key)
        blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
            jsonl_content,
            content_type='application/x-ndjson'
        )
    
        print(f'Wrote {len(events)} events to {key}')
        return key
    

     * Second file: **requirements.txt:**
    
    functions-framework==3.*
    google-cloud-storage==2.*
    urllib3>=2.0.0
    

  3. Click **Deploy** to save and deploy the function.

  4. Wait for deployment to complete (2-3 minutes).

**Note:** The Pub/Sub trigger configuration automatically creates the necessary subscriptions and permissions.**Note:** Bitwarden's Public API enforces rate limits and may return HTTP 429 responses under high request volume. If you encounter 429 responses, the function will automatically retry with exponential backoff. Consider adjusting MAX_PAGES or scheduling frequency if rate limiting occurs frequently.



## Create Cloud Scheduler job

Cloud Scheduler publishes messages to the Pub/Sub topic at regular intervals, triggering the Cloud Run function.

  1. In the **GCP Console** , go to **Cloud Scheduler**.
  2. Click **Create Job**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | `bitwarden-events-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the Pub/Sub topic (`bitwarden-events-trigger`)  
**Message body** | `{}` (empty JSON object)  
  4. Click **Create**.




### Schedule frequency options

  * Choose frequency based on log volume and latency requirements:

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
  5. Click on your function name (`bitwarden-events-collector`).
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         Processing events with continuation token: None
         Page 1: Retrieved X events
         Wrote X events to bitwarden/events/YYYY/MM/DD/HHMMSS-page00000-bitwarden-events.jsonl
         Successfully processed X events across 1 pages
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click your bucket name.

  10. Navigate to the prefix folder (`bitwarden/events/`).

  11. Verify that a new `.jsonl` file was created with the current timestamp.




If you see errors in the logs:

  * **HTTP 401** : Check API credentials in environment variables
  * **HTTP 403** : Verify account has required permissions and Events feature is enabled in Organization Settings
  * **HTTP 429** : Rate limiting - function will automatically retry with backoff
  * **Missing environment variables** : Check all required variables are set



## Retrieve the Google SecOps service account

Google SecOps uses a unique service account to read data from your GCS bucket. You must grant this service account access to your bucket.

### Get the service account email

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Bitwarden Events`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Bitwarden events** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Do not use service accounts from other documentation or examples.



## Grant IAM permissions to the Google SecOps service account

The Google SecOps service account needs **Storage Object Viewer** role on your GCS bucket.

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Paste the Google SecOps service account email.
     * **Assign roles** : Select **Storage Object Viewer**.
  6. Click **Save**.

**Note:** If you plan to use the deletion option "Delete transferred files" or "Delete transferred files and empty directories," grant **Storage Object Admin** role instead of Storage Object Viewer.



## Configure a feed in Google SecOps to ingest Bitwarden Enterprise Event Logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Bitwarden Events`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Bitwarden events** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://bitwarden-events/bitwarden/events/
           

       * Replace:

         * `bitwarden-events`: Your GCS bucket name.
         * `bitwarden/events/`: Prefix/folder path where logs are stored.
**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never** : Never deletes any files after transfers (recommended for testing).
       * **Delete transferred files** : Deletes files after successful transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.

**Note:** If you select a deletion option, the service account must have **Storage Object Admin** role instead of Storage Object Viewer. Update IAM permissions accordingly.
     * **Maximum File Age** : Include files modified in the last number of days. Default is 180 days.

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).

     * **Ingestion labels** : The label to be applied to the events from this feed.

  9. Click **Next**.

  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
actingUserId | target.user.userid | If enriched.actingUser.userId is empty or null, this field is used to populate the target.user.userid field.  
collectionID | security_result.detection_fields.key | Populates the key field within detection_fields in security_result.  
collectionID | security_result.detection_fields.value | Populates the value field within detection_fields in security_result.  
date | metadata.event_timestamp | Parsed and converted to a timestamp format and mapped to event_timestamp.  
enriched.actingUser.accessAll | security_result.rule_labels.key | Sets the value to "Access_All" within rule_labels in security_result.  
enriched.actingUser.accessAll | security_result.rule_labels.value | Populates the value field within rule_labels in security_result with the value from enriched.actingUser.accessAll converted to string.  
enriched.actingUser.email | target.user.email_addresses | Populates the email_addresses field within target.user.  
enriched.actingUser.id | metadata.product_log_id | Populates the product_log_id field within metadata.  
enriched.actingUser.id | target.labels.key | Sets the value to "ID" within target.labels.  
enriched.actingUser.id | target.labels.value | Populates the value field within target.labels with the value from enriched.actingUser.id.  
enriched.actingUser.name | target.user.user_display_name | Populates the user_display_name field within target.user.  
enriched.actingUser.object | target.labels.key | Sets the value to "Object" within target.labels.  
enriched.actingUser.object | target.labels.value | Populates the value field within target.labels with the value from enriched.actingUser.object.  
enriched.actingUser.resetPasswordEnrolled | target.labels.key | Sets the value to "ResetPasswordEnrolled" within target.labels.  
enriched.actingUser.resetPasswordEnrolled | target.labels.value | Populates the value field within target.labels with the value from enriched.actingUser.resetPasswordEnrolled converted to string.  
enriched.actingUser.twoFactorEnabled | security_result.rule_labels.key | Sets the value to "Two Factor Enabled" within rule_labels in security_result.  
enriched.actingUser.twoFactorEnabled | security_result.rule_labels.value | Populates the value field within rule_labels in security_result with the value from enriched.actingUser.twoFactorEnabled converted to string.  
enriched.actingUser.userId | target.user.userid | Populates the userid field within target.user.  
enriched.collection.id | additional.fields.key | Sets the value to "Collection ID" within additional.fields.  
enriched.collection.id | additional.fields.value.string_value | Populates the string_value field within additional.fields with the value from enriched.collection.id.  
enriched.collection.object | additional.fields.key | Sets the value to "Collection Object" within additional.fields.  
enriched.collection.object | additional.fields.value.string_value | Populates the string_value field within additional.fields with the value from enriched.collection.object.  
enriched.type | metadata.product_event_type | Populates the product_event_type field within metadata.  
groupId | target.user.group_identifiers | Adds the value to the group_identifiers array within target.user.  
ipAddress | principal.ip | Extracted IP address from the field and mapped to principal.ip.  
N/A | extensions.auth | An empty object is created by the parser.  
N/A | metadata.event_type | Determined based on the enriched.type and presence of principal and target information. Possible values: USER_LOGIN, STATUS_UPDATE, GENERIC_EVENT.  
N/A | security_result.action | Determined based on the enriched.type. Possible values: ALLOW, BLOCK.  
object | additional.fields.key | Sets the value to "Object" within additional.fields.  
object | additional.fields.value | Populates the value field within additional.fields with the value from object.  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
