---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/teamviewer/
title: Collect TeamViewer logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T22:43:32.136266+00:00
---

# Collect TeamViewer logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/teamviewer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect TeamViewer logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest TeamViewer logs to Google Security Operations using Google Cloud Storage. The parser extracts the audit events from JSON formatted logs. It iterates through event details, mapping specific properties to Unified Data Model (UDM) fields, handling participant and presenter information, and categorizing events based on user activity. The parser also performs data transformations, such as merging labels and converting timestamps to a standardized format.

## Before you begin

Ensure that you have the following prerequisites:

  * A Google SecOps instance
  * A Google Cloud project with Cloud Storage API enabled
  * Permissions to create and manage Cloud Storage buckets
  * Permissions to manage IAM policies on Cloud Storage buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * Privileged access to TeamViewer Management Console
  * TeamViewer Business, Premium, Corporate, or Tensor license (required for API access)



## Create a Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `teamviewer-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Get TeamViewer prerequisites

  1. Sign in to the **TeamViewer Management Console** at <https://login.teamviewer.com/>.
  2. Click your user icon in the upper right corner and select **Edit profile**.
  3. Select **Apps**.
  4. Click **Create script token**.
  5. Provide the following configuration details: 
     * **Token name** : Enter a descriptive name (for example, `Google SecOps Integration`).
     * **Permissions** : Select the following permissions: 
       * **Account management** > **View account data**
       * **Session management** > **View session data**
       * **Connection reporting** > **View connection reports**
  6. Click **Create**.
  7. Copy and save the generated script token in a secure location.

**Note:** The script token will only be displayed once. If you lose it, you will need to create a new token. The script token must include the Connection reporting permission corresponding to the Connections.Read scope required by `/api/v1/EventLogging`.
  8. Record your TeamViewer API Base URL: `https://webapi.teamviewer.com/api/v1`




### Verify permissions

To verify the account has the required permissions:

  1. Sign in to the **TeamViewer Management Console**.
  2. Go to **Edit profile > Apps**.
  3. Locate your script token in the list.
  4. Verify that **Connection reporting** > **View connection reports** is enabled.
  5. If this permission is not enabled, edit the token and add the required permission.



### Test API access

  * Test your credentials before proceeding with the integration:
        
        # Replace with your actual script token
        SCRIPT_TOKEN="your-script-token"
        API_BASE="https://webapi.teamviewer.com/api/v1"
        
        # Test API access
        curl -v -X POST -H "Authorization: Bearer ${SCRIPT_TOKEN}" \
          -H "Content-Type: application/json" \
          -H "Accept: application/json" \
          -d '{"StartDate": "2024-01-01T00:00:00Z", "EndDate": "2024-01-01T01:00:00Z"}' \
          "${API_BASE}/EventLogging"
        




If you receive a 200 response with JSON data, your credentials are configured correctly.

## Create a service account for the Cloud Run function

The Cloud Run function needs a service account with permissions to write to Cloud Storage bucket and be invoked by Pub/Sub.

### Create the service account

  1. In the **Google Cloud console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `teamviewer-collector-sa`.
     * **Service account description** : Enter `Service account for Cloud Run function to collect TeamViewer logs`.
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

  * **Storage Object Admin** : Write logs to Cloud Storage bucket and manage state files
  * **Cloud Run Invoker** : Allow Pub/Sub to invoke the function
  * **Cloud Functions Invoker** : Allow function invocation



### Grant IAM permissions on the Cloud Storage bucket

Grant the service account write permissions on the Cloud Storage bucket:

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name (for example, `teamviewer-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `teamviewer-collector-sa@PROJECT_ID.iam.gserviceaccount.com`).
     * **Assign roles** : Select **Storage Object Admin**.
  6. Click **Save**.



## Create a Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **Google Cloud console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `teamviewer-logs-trigger`.
     * Leave other settings as default.
  4. Click **Create**.



## Create a Cloud Run function to collect logs

The Cloud Run function is triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from TeamViewer API and writes them to Cloud Storage.

  1. In the **Google Cloud console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `teamviewer-logs-collector`  
**Region** | Select region matching your Cloud Storage bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose the Pub/Sub topic (`teamviewer-logs-trigger`).
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub automatically handles authentication when invoking the function.
  7. Navigate to and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select the service account (`teamviewer-collector-sa`).
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value  
---|---  
`GCS_BUCKET` | `teamviewer-logs`  
`GCS_PREFIX` | `teamviewer/audit/`  
`STATE_KEY` | `teamviewer/audit/state.json`  
`WINDOW_SECONDS` | `3600`  
`HTTP_TIMEOUT` | `60`  
`MAX_RETRIES` | `3`  
`USER_AGENT` | `teamviewer-to-gcs/1.0`  
`SCRIPT_TOKEN` | `your-script-token` (from TeamViewer prerequisites)  
`API_BASE_URL` | `https://webapi.teamviewer.com/api/v1`  
  10. In the **Variables & Secrets** section, navigate to **Requests** :

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




### Add the function code

  1. Enter **main** in **Function entry point**
  2. In the inline code editor, create two files:

     * First file: **main.py:**
    
    import functions_framework
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    import json
    import os
    import urllib.request
    import urllib.parse
    import urllib.error
    from datetime import datetime, timezone
    import time
    import uuid
    
    # Initialize Storage client
    storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    
    @functions_framework.cloud_event
    def main(cloud_event):
        """
        Cloud Run function triggered by Pub/Sub to fetch TeamViewer audit logs and write to GCS.
    
        Args:
            cloud_event: CloudEvent object containing Pub/Sub message
        """
    
        # Get environment variables
        bucket_name = os.environ.get('GCS_BUCKET')
        prefix = os.environ.get('GCS_PREFIX', 'teamviewer/audit/')
        state_key = os.environ.get('STATE_KEY', 'teamviewer/audit/state.json')
        window_sec = int(os.environ.get('WINDOW_SECONDS', '3600'))
        http_timeout = int(os.environ.get('HTTP_TIMEOUT', '60'))
        max_retries = int(os.environ.get('MAX_RETRIES', '3'))
        user_agent = os.environ.get('USER_AGENT', 'teamviewer-to-gcs/1.0')
    
        # TeamViewer API credentials
        api_base_url = os.environ.get('API_BASE_URL')
        script_token = os.environ.get('SCRIPT_TOKEN')
    
        if not all([bucket_name, api_base_url, script_token]):
            print('Error: Missing required environment variables')
            return
    
        try:
            # Get GCS bucket
            bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
    
            # Load state (last processed timestamp)
            state = load_state(bucket, state_key)
            now = time.time()
            from_ts = float([state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get('last_to_ts') or (now - window_sec))
            to_ts = now
    
            print(f'Fetching TeamViewer audit data from {iso_format(from_ts)} to {iso_format(to_ts)}')
    
            # Build audit API URL
            url = build_audit_url(api_base_url)
    
            print(f'Fetching TeamViewer audit data from: {url}')
    
            # Fetch audit data with retries and pagination
            all_records = []
            continuation_token = None
    
            # Inside main() loop:
            while True:
                blob_data, content_type, next_token = fetch_audit_data(
                    url, script_token, user_agent, http_timeout, max_retries, from_ts, to_ts, continuation_token
                )
    
                # Validate JSON data
                try:
                    audit_data = json.loads(blob_data)
                    records = audit_data.get('AuditEvents', [])
                    all_records.extend(records)
                    print(f"Retrieved {len(records)} audit records (total: {len(all_records)})")
    
                    # Check for pagination
                    if next_token:
                        continuation_token = next_token
                        print(f"Fetching next page with ContinuationToken: {continuation_token}")
                    else:
                        break
    
                except json.JSONDecodeError as e:
                    print(f"Warning: Invalid JSON received: {e}")
                    break
    
            if all_records:
                # Write to GCS
                key = put_audit_data(bucket, prefix, json.dumps({'AuditEvents': all_records}), 
                    'application/json', from_ts, to_ts)
                print(f'Successfully wrote {len(all_records)} audit records to {key}')
            else:
                print('No audit records found')
    
            # Update state
            state['last_to_ts'] = to_ts
            state['last_successful_run'] = now
            save_state(bucket, state_key, state)
    
        except Exception as e:
            print(f'Error processing TeamViewer logs: {str(e)}')
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
                json.dumps(state, separators=(',', ':')),
                content_type='application/json'
            )
        except Exception as e:
            print(f'Warning: Could not save state: {str(e)}')
    
    def iso_format(ts):
        """Convert Unix timestamp to ISO 8601 format."""
        return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(ts))
    
    def build_audit_url(api_base_url):
        """Build URL for TeamViewer audit API endpoint."""
        return f"{api_base_url.rstrip('/')}/EventLogging"
    
    def fetch_audit_data(url, script_token, user_agent, http_timeout, max_retries, from_ts, to_ts, continuation_token=None):
        """Fetch audit data from TeamViewer API with retries and pagination support."""
    
        # Construct JSON payload
        payload = {
            "StartDate": iso_format(from_ts),
            "EndDate": iso_format(to_ts)
        }
        if continuation_token:
            payload["ContinuationToken"] = continuation_token
    
        attempt = 0
        while True:
            req = urllib.request.Request(url, method='POST')
            req.add_header('User-Agent', user_agent)
            req.add_header('Authorization', f'Bearer {script_token}')
            req.add_header('Content-Type', 'application/json')
            req.add_header('Accept', 'application/json')
    
            # Encode payload as bytes for POST body
            data = json.dumps(payload).encode('utf-8')
    
            try:
                with urllib.request.urlopen(req, data=data, timeout=http_timeout) as r:
                    response_data = r.read()
                    content_type = r.headers.get('Content-Type') or 'application/json'
    
                    try:
                        data = json.loads(response_data)
                        next_token = data.get('ContinuationToken')
                    except:
                        next_token = None
    
                    return response_data, content_type, next_token
    
            except urllib.error.HTTPError as e:
                if e.code == 429:
                    attempt += 1
                    print(f'Rate limited (429) on attempt {attempt}')
                    if attempt > max_retries:
                        raise
                    time.sleep(min(60, 2 ** attempt) + (time.time() % 1))
                else:
                    print(f'HTTP error {e.code}: {e.reason}')
                    raise
            except urllib.error.URLError as e:
                attempt += 1
                print(f'URL error on attempt {attempt}: {e}')
                if attempt > max_retries:
                    raise
                time.sleep(min(60, 2 ** attempt) + (time.time() % 1))
    
    def put_audit_data(bucket, prefix, blob_data, content_type, from_ts, to_ts):
        """Write audit data to GCS."""
        ts_path = time.strftime('%Y/%m/%d', time.gmtime(to_ts))
        uniq = f"{int(time.time() * 1e6)}_{uuid.uuid4().hex[:8]}"
        key = f"{prefix}{ts_path}/teamviewer_audit_{int(from_ts)}_{int(to_ts)}_{uniq}.json"
    
        blob = bucket.blob(key)
        blob.[metadata](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_metadata) = {
            'source': 'teamviewer-audit',
            'from_timestamp': str(int(from_ts)),
            'to_timestamp': str(int(to_ts))
        }
        blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(blob_data, content_type=content_type)
    
        return key
    

**Note:** This script is provided as an example and is not officially supported. We welcome feedback about how we can improve it. To submit feedback, click **Send Feedback > Google SecOps Security Product Feedback** on this page.

     * Second file: **requirements.txt:**
    
    functions-framework==3.*
    google-cloud-storage==2.*
    

  3. Click **Deploy** to save and deploy the function.

  4. Wait for deployment to complete (2-3 minutes).

**Note:** The `/api/v1/EventLogging` endpoint is limited to 50 records per call. The implementation reads `ContinuationToken` from the response and loops until all records are retrieved.



## Create a Cloud Scheduler job

Cloud scheduler publishes messages to the Pub/Sub topic at regular intervals, triggering the Cloud Run function.

  1. In the **Google Cloud console** , go to **Cloud Scheduler**.
  2. Click **Create Job**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | `teamviewer-logs-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the Pub/Sub topic (`teamviewer-logs-trigger`)  
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

  1. In the **Cloud Scheduler** console, find your job (`teamviewer-logs-collector-hourly`).
  2. Click **Force run** to trigger the job manually.
  3. Wait a few seconds.
  4. Go to **Cloud Run > Services**.
  5. Click the function name (`teamviewer-logs-collector`).
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for the following:
         
         Fetching TeamViewer audit data from YYYY-MM-DDTHH:MM:SSZ to YYYY-MM-DDTHH:MM:SSZ
         Retrieved X audit records (total: X)
         Successfully wrote X audit records to teamviewer/audit/YYYY/MM/DD/teamviewer_audit_...json
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click your bucket name (`teamviewer-logs`).

  10. Navigate to the prefix folder (`teamviewer/audit/`).

  11. Verify that a new `.json` file was created with the current timestamp.




If you see errors in the logs:

  * **HTTP 401** : Check the `SCRIPT_TOKEN` environment variable matches your TeamViewer script token
  * **HTTP 403** : Verify the script token has **Connection reporting** > **View connection reports** permission
  * **HTTP 429** : Rate limiting - function will automatically retry with exponential backoff
  * **Missing environment variables** : Check all required variables (`GCS_BUCKET`, `API_BASE_URL`, `SCRIPT_TOKEN`) are set



## Retrieve the Google SecOps service account

Google SecOps uses a unique service account to read data from your Cloud Storage bucket. You must grant this service account access to your bucket.

### Get the service account email

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `TeamViewer logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **TeamViewer** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email is displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Don't use service accounts from other documentation or examples.



## Grant IAM permissions to the Google SecOps service account

The Google SecOps service account needs **Storage Object Viewer** role on your Cloud Storage bucket.

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name (`teamviewer-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Paste the Google SecOps service account email.
     * **Assign roles** : Select **Storage Object Viewer**.
  6. Click **Save**.

**Note:** If you plan to use the deletion option "Delete transferred files" or "Delete transferred files and empty directories," grant **Storage Object Admin** role instead of Storage Object Viewer.



## Configure a feed in Google SecOps to ingest TeamViewer logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `TeamViewer logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **TeamViewer** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the Cloud Storage bucket URI with the prefix path:
           
           gs://teamviewer-logs/teamviewer/audit/
           

       * Replace:

         * `teamviewer-logs`: Your Cloud Storage bucket name.
         * `teamviewer/audit/`: Prefix or path where logs are stored.
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

Log field | UDM mapping | Logic  
---|---|---  
AffectedItem | metadata.product_log_id | The value of AffectedItem from the raw log is directly mapped to this UDM field.  
EventDetails.NewValue | principal.resource.attribute.labels.value | If PropertyName contains (server), the NewValue is used as the value of a label in principal.resource.attribute.labels.  
EventDetails.NewValue | principal.user.user_display_name | If PropertyName is Name of participant, the NewValue is used as the user display name for the principal.  
EventDetails.NewValue | principal.user.userid | If PropertyName is ID of participant, the NewValue is used as the user ID for the principal.  
EventDetails.NewValue | security_result.about.labels.value | For all other PropertyName values (except those handled by specific conditions), the NewValue is used as the value of a label within the security_result.about.labels array.  
EventDetails.NewValue | target.file.full_path | If PropertyName is Source file, the NewValue is used as the full path for the target file.  
EventDetails.NewValue | target.resource.attribute.labels.value | If PropertyName contains (client), the NewValue is used as the value of a label in target.resource.attribute.labels.  
EventDetails.NewValue | target.user.user_display_name | If PropertyName is Name of presenter, the NewValue is parsed. If it's an integer, it's discarded. Otherwise, it's used as the user display name for the target.  
EventDetails.NewValue | target.user.userid | If PropertyName is ID of presenter, the NewValue is used as the user ID for the target.  
EventDetails.PropertyName | principal.resource.attribute.labels.key | If PropertyName contains (server), the PropertyName is used as the key of a label in principal.resource.attribute.labels.  
EventDetails.PropertyName | security_result.about.labels.key | For all other PropertyName values (except those handled by specific conditions), the PropertyName is used as the key of a label within the security_result.about.labels array.  
EventDetails.PropertyName | target.resource.attribute.labels.key | If PropertyName contains (client), the PropertyName is used as the key of a label in target.resource.attribute.labels.  
EventName | metadata.product_event_type | The value of EventName from the raw log is directly mapped to this UDM field.  
Timestamp | metadata.event_timestamp | The value of Timestamp from the raw log is parsed and used as the event timestamp in the metadata.  
metadata.event_type |  | Set to USER_UNCATEGORIZED if src_user (derived from ID of participant) is not empty, otherwise set to USER_RESOURCE_ACCESS.  
metadata.vendor_name |  | Hardcoded to TEAMVIEWER.  
metadata.product_name |  | Hardcoded to TEAMVIEWER.  
network.application_protocol |  | Hardcoded to TEAMVIEWER.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/teamviewer-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
