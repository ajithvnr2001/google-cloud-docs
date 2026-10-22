---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cs-filevantage/
title: Collect CrowdStrike FileVantage logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:54:11.158506+00:00
---

# Collect CrowdStrike FileVantage logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cs-filevantage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect CrowdStrike FileVantage logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest CrowdStrike FileVantage logs to Google Security Operations using Google Cloud Storage. CrowdStrike FileVantage is a file integrity monitoring solution that tracks changes to critical files and directories across your environment.

## Before you begin

Ensure that you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * Privileged access to CrowdStrike Falcon Console

**Note:** The CrowdStrike FileVantage API endpoints and scopes described in this guide are documented in the CrowdStrike Falcon API. Access to the full API documentation requires a CrowdStrike customer or partner account. Contact CrowdStrike support if you need assistance with API access.



## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `crowdstrike-filevantage-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Collect CrowdStrike FileVantage API credentials

  1. Sign in to the **CrowdStrike Falcon Console**.
  2. Go to **Support and resources > API clients and keys**.
  3. Click **Add new API client**.
  4. Provide the following configuration details: 
     * **Client name** : Enter a descriptive name (for example, `Google SecOps FileVantage Integration`).
     * **Description** : Enter a brief description of the integration purpose.
     * **API scopes** : Select **Falcon FileVantage:read**.
  5. Click **Add** to complete the process.
  6. Copy and save in a secure location the following details:

     * **Client ID**
     * **Client Secret**
     * **Base URL** (determines your cloud region)
**Note:** The user account must have CrowdStrike Falcon Administrator role to create API clients.



### Verify permissions

To verify the account has the required permissions:

  1. Sign in to the **CrowdStrike Falcon Console**.
  2. Go to **Support and resources > API clients and keys**.
  3. If you can see the **API clients and keys** page and create new API clients, you have the required permissions.
  4. If you cannot access this page, contact your CrowdStrike administrator to grant Falcon Administrator role.



### Test API access

  * Test your credentials before proceeding with the integration:
        
        # Replace with your actual credentials
        FALCON_CLIENT_ID="your-client-id"
        FALCON_CLIENT_SECRET="your-client-secret"
        FALCON_BASE_URL="https://api.crowdstrike.com"
        
        # Get OAuth token
        TOKEN=$(curl -s -X POST "${FALCON_BASE_URL}/oauth2/token" \
          -H "Content-Type: application/x-www-form-urlencoded" \
          -d "client_id=${FALCON_CLIENT_ID}&client_secret=${FALCON_CLIENT_SECRET}&grant_type=client_credentials" \
          | grep -o '"access_token":"[^"]*' | cut -d'"' -f4)
        
        # Test FileVantage API access
        curl -v -H "Authorization: Bearer ${TOKEN}" \
          "${FALCON_BASE_URL}/filevantage/queries/changes/v3?limit=1"
        




## Create service account for Cloud Run function

The Cloud Run function needs a service account with permissions to write to GCS bucket and be invoked by Pub/Sub.

### Create service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `crowdstrike-filevantage-sa`.
     * **Service account description** : Enter `Service account for Cloud Run function to collect CrowdStrike FileVantage logs`.
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
  2. Click your bucket name (for example, `crowdstrike-filevantage-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `crowdstrike-filevantage-sa@PROJECT_ID.iam.gserviceaccount.com`).
     * **Assign roles** : Select **Storage Object Admin**.
  6. Click **Save**.



## Create Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `crowdstrike-filevantage-trigger`.
     * Leave other settings as default.
  4. Click **Create**.



## Create Cloud Run function to collect logs

The Cloud Run function is triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from CrowdStrike FileVantage API and writes them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `crowdstrike-filevantage-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose the Pub/Sub topic (`crowdstrike-filevantage-trigger`).
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub automatically handles authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select the service account (`crowdstrike-filevantage-sa`).
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value  
---|---  
`GCS_BUCKET` | `crowdstrike-filevantage-logs`  
`GCS_PREFIX` | `filevantage/`  
`STATE_KEY` | `filevantage/state.json`  
`FALCON_CLIENT_ID` | `your-client-id`  
`FALCON_CLIENT_SECRET` | `your-client-secret`  
`FALCON_BASE_URL` | `https://api.crowdstrike.com` (US-1) / `https://api.us-2.crowdstrike.com` (US-2) / `https://api.eu-1.crowdstrike.com` (EU-1)  
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
    from datetime import datetime, timezone, timedelta
    import time
    
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
        Cloud Run function triggered by Pub/Sub to fetch CrowdStrike FileVantage logs and write to GCS.
    
        Args:
            cloud_event: CloudEvent object containing Pub/Sub message
        """
    
        # Get environment variables
        bucket_name = os.environ.get('GCS_BUCKET')
        prefix = os.environ.get('GCS_PREFIX', 'filevantage/')
        state_key = os.environ.get('STATE_KEY', 'filevantage/state.json')
        client_id = os.environ.get('FALCON_CLIENT_ID')
        client_secret = os.environ.get('FALCON_CLIENT_SECRET')
        base_url = os.environ.get('FALCON_BASE_URL')
    
        if not all([bucket_name, client_id, client_secret, base_url]):
            print('Error: Missing required environment variables')
            return
    
        try:
            # Get GCS bucket
            bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
    
            # Get OAuth token
            token_url = f"{base_url}/oauth2/token"
            token_headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Accept': 'application/json'
            }
            token_data = f"client_id={client_id}&client_secret={client_secret}&grant_type=client_credentials"
    
            token_response = http.request(
                'POST',
                token_url,
                body=token_data.encode('utf-8'),
                headers=token_headers
            )
    
            if token_response.status != 200:
                print(f"Failed to get OAuth token: {token_response.status}")
                print(f"Response: {token_response.data.decode('utf-8')}")
                return
    
            token_data_json = json.loads(token_response.data.decode('utf-8'))
            access_token = token_data_json['access_token']
    
            # Get last checkpoint
            last_timestamp = get_last_checkpoint(bucket, state_key)
    
            # Fetch file changes using v3 endpoint (high volume query)
            changes_url = f"{base_url}/filevantage/queries/changes/v3"
            headers = {
                'Authorization': f'Bearer {access_token}',
                'Accept': 'application/json'
            }
    
            # Build query parameters
            params = []
            params.append('limit=5000')
            params.append('sort=action_timestamp|asc')
    
            if last_timestamp:
                params.append(f"filter=action_timestamp:>'{last_timestamp}'")
    
            query_url = f"{changes_url}?{'&'.join(params)}"
    
            backoff = 1.0
            max_retries = 3
    
            for attempt in range(max_retries):
                response = http.request('GET', query_url, headers=headers)
    
                if response.status == 429:
                    retry_after = int(response.headers.get('Retry-After', str(int(backoff))))
                    print(f"Rate limited (429). Retrying after {retry_after}s...")
                    time.sleep(retry_after)
                    backoff = min(backoff * 2, 30.0)
                    continue
    
                if response.status != 200:
                    print(f"Failed to query changes: {response.status}")
                    print(f"Response: {response.data.decode('utf-8')}")
                    return
    
                break
            else:
                print("Max retries exceeded")
                return
    
            response_data = json.loads(response.data.decode('utf-8'))
            change_ids = response_data.get('resources', [])
    
            if not change_ids:
                print("No new changes found")
                return
    
            # Get detailed change information using v2 endpoint
            details_url = f"{base_url}/filevantage/entities/changes/v2"
            batch_size = 500
            all_changes = []
            latest_timestamp = last_timestamp
    
            for i in range(0, len(change_ids), batch_size):
                batch_ids = change_ids[i:i + batch_size]
    
                # Build query string with multiple ids parameters
                ids_params = '&'.join([f'ids={id}' for id in batch_ids])
                details_query_url = f"{details_url}?{ids_params}"
    
                backoff = 1.0
                for attempt in range(max_retries):
                    details_response = http.request('GET', details_query_url, headers=headers)
    
                    if details_response.status == 429:
                        retry_after = int(details_response.headers.get('Retry-After', str(int(backoff))))
                        print(f"Rate limited (429). Retrying after {retry_after}s...")
                        time.sleep(retry_after)
                        backoff = min(backoff * 2, 30.0)
                        continue
    
                    if details_response.status == 200:
                        details_data = json.loads(details_response.data.decode('utf-8'))
                        changes = details_data.get('resources', [])
                        all_changes.extend(changes)
    
                        # Track latest timestamp
                        for change in changes:
                            change_time = change.get('action_timestamp')
                            if change_time and (not latest_timestamp or change_time > latest_timestamp):
                                latest_timestamp = change_time
                        break
                    else:
                        print(f"Failed to get change details (batch {i//batch_size + 1}): {details_response.status}")
                        break
    
            if all_changes:
                # Store logs in GCS
                timestamp = datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')
                blob_name = f"{prefix}filevantage_changes_{timestamp}.json"
                blob = bucket.blob(blob_name)
                log_lines = '\n'.join(json.dumps(change) for change in all_changes)
                blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(log_lines, content_type='application/json')
    
                # Update checkpoint
                save_checkpoint(bucket, state_key, latest_timestamp)
    
                print(f"Stored {len(all_changes)} changes in GCS: {blob_name}")
    
        except Exception as e:
            print(f"Error: {str(e)}")
            raise
    
    def get_last_checkpoint(bucket, key):
        """Get the last processed timestamp from GCS state file"""
        try:
            blob = bucket.blob(key)
            if blob.exists():
                state_data = blob.[download_as_text](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_download_as_text)()
                state = json.loads(state_data)
                return [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get('last_timestamp')
        except Exception as e:
            print(f"Error reading checkpoint: {e}")
        return None
    
    def save_checkpoint(bucket, key, timestamp):
        """Save the last processed timestamp to GCS state file"""
        try:
            state = {
                'last_timestamp': timestamp,
                'updated_at': datetime.now(timezone.utc).isoformat()
            }
            blob = bucket.blob(key)
            blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
                json.dumps(state),
                content_type='application/json'
            )
        except Exception as e:
            print(f"Error saving checkpoint: {e}")
    

     * Second file: **requirements.txt:**
    
    functions-framework==3.*
    google-cloud-storage==2.*
    urllib3>=2.0.0
    

  3. Click **Deploy** to save and deploy the function.

  4. Wait for deployment to complete (2-3 minutes).

**Note:** The Pub/Sub trigger configuration automatically creates the necessary subscriptions and permissions.



## Create Cloud Scheduler job

Cloud Scheduler publishes messages to the Pub/Sub topic at regular intervals, triggering the Cloud Run function.

  1. In the **GCP Console** , go to **Cloud Scheduler**.
  2. Click **Create Job**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | `crowdstrike-filevantage-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `*/15 * * * *` (every 15 minutes)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the Pub/Sub topic (`crowdstrike-filevantage-trigger`)  
**Message body** | `{}` (empty JSON object)  
  4. Click **Create**.

**Note:** A 15-minute polling interval is recommended to avoid hitting rate limits while maintaining reasonable data freshness. Adjust based on your log volume and latency requirements.



### Test the scheduler job

  1. In the **Cloud Scheduler** console, find your job (`crowdstrike-filevantage-hourly`).
  2. Click **Force run** to trigger manually.
  3. Wait a few seconds and go to **Cloud Run > Services > crowdstrike-filevantage-collector > Logs**.
  4. Verify the function executed successfully.
  5. Check the GCS bucket (`crowdstrike-filevantage-logs`) to confirm logs were written.



## Retrieve the Google SecOps service account

Google SecOps uses a unique service account to read data from your GCS bucket. You must grant this service account access to your bucket.

### Get the service account email

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `CrowdStrike FileVantage logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **CrowdStrike Filevantage** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email is displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Don't use service accounts from other documentation or examples.



## Grant IAM permissions to the Google SecOps service account

The Google SecOps service account needs **Storage Object Viewer** role on your GCS bucket.

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name (for example, `crowdstrike-filevantage-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Paste the Google SecOps service account email.
     * **Assign roles** : Select **Storage Object Viewer**.
  6. Click **Save**.

**Note:** If you plan to use the deletion option "Delete transferred files" or "Delete transferred files and empty directories," grant **Storage Object Admin** role instead of Storage Object Viewer.



## Configure a feed in Google SecOps to ingest CrowdStrike FileVantage logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `CrowdStrike FileVantage logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **CrowdStrike Filevantage** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://crowdstrike-filevantage-logs/filevantage/
           

       * Replace:

         * `crowdstrike-filevantage-logs`: Your GCS bucket name.
         * `filevantage/`: Prefix/folder path where logs are stored.
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




## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cs-filevantage-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
