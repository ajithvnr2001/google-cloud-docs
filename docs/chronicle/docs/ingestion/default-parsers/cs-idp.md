---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cs-idp/
title: Collect CrowdStrike Identity Protection (IDP) Services logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:38:58.437733+00:00
---

# Collect CrowdStrike Identity Protection (IDP) Services logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cs-idp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect CrowdStrike Identity Protection (IDP) Services logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest CrowdStrike Identity Protection (IDP) Services logs to Google Security Operations using Google Cloud Storage. The integration uses the CrowdStrike Unified Alerts API to collect Identity Protection events and stores them in NDJSON format for processing by the built-in CS_IDP parser.

## Before you begin

Ensure that you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * Privileged access to CrowdStrike Falcon Console and API key management



## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `crowdstrike-idp-logs-bucket`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Get CrowdStrike Identity Protection prerequisites

  1. Sign in to the **CrowdStrike Falcon Console**.
  2. Go to **Support and Resources > API clients and keys**.
  3. Click **Add new API Client**.
  4. Provide the following configuration details: 
     * **Client Name** : Enter `Google SecOps IDP Integration`.
     * **Description** : Enter `API client for Google SecOps integration`.
     * **Scopes** : Select **Alerts: READ** (alerts:read) scope (this includes Identity Protection alerts).
  5. Click **Add**.
  6. Copy and save in a secure location the following details: 
     * **Client ID**
     * **Client Secret** (this is only shown once)
     * **Base URL** (examples: `api.crowdstrike.com` for US-1, `api.us-2.crowdstrike.com` for US-2, `api.eu-1.crowdstrike.com` for EU-1)



## Create service account for Cloud Run function

The Cloud Run function needs a service account with permissions to write to GCS bucket.

### Create service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `crowdstrike-idp-collector-sa`.
     * **Service account description** : Enter `Service account for Cloud Run function to collect CrowdStrike IDP logs`.
  4. Click **Create and Continue**.
  5. In the **Grant this service account access to project** section: 
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



#### Grant IAM permissions on GCS bucket

Grant the service account write permissions on the GCS bucket:

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `crowdstrike-idp-collector-sa@PROJECT_ID.iam.gserviceaccount.com`).
     * **Assign roles** : Select **Storage Object Admin**.
  6. Click **Save**.



## Create Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `crowdstrike-idp-trigger`.
     * Leave other settings as default.
  4. Click **Create**.



## Create Cloud Run function to collect logs

The Cloud Run function is triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from CrowdStrike Identity Protection API and writes them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `crowdstrike-idp-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose the topic `crowdstrike-idp-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub automatically handles authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select the service account `crowdstrike-idp-collector-sa`.
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value  
---|---  
`GCS_BUCKET` | `crowdstrike-idp-logs-bucket`  
`GCS_PREFIX` | `crowdstrike-idp/`  
`STATE_KEY` | `crowdstrike-idp/state.json`  
`CROWDSTRIKE_CLIENT_ID` | `your-client-id`  
`CROWDSTRIKE_CLIENT_SECRET` | `your-client-secret`  
`API_BASE` | `api.crowdstrike.com` (US-1), `api.us-2.crowdstrike.com` (US-2), `api.eu-1.crowdstrike.com` (EU-1)  
`ALERTS_LIMIT` | `1000` (optional, max 10000 per page)  
  10. Scroll down in the **Variables & Secrets** tab to **Requests** :

     * **Request timeout** : Enter `600` seconds (10 minutes).
  11. Go to the **Settings** tab in **Containers** :

     * In the **Resources** section: 
       * **Memory** : Select **512 MiB** or higher.
       * **CPU** : Select **1**.
     * Click **Done**.
  12. Scroll to **Execution environment** :

     * Select **Default** (recommended).
  13. In the **Revision scaling** section:

     * **Minimum number of instances** : Enter `0`.
     * **Maximum number of instances** : Enter `100` (or adjust based on expected load).
  14. Click **Create**.

  15. Wait for the service to be created (1-2 minutes).

  16. After the service is created, the **inline code editor** opens automatically.




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
    from urllib.parse import urlencode
    
    # Initialize HTTP client
    http = urllib3.PoolManager()
    
    # Initialize Storage client
    storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    
    @functions_framework.cloud_event
    def main(cloud_event):
        """
        Fetch CrowdStrike Identity Protection alerts (Unified Alerts API)
        and store RAW JSON (NDJSON) to GCS for the CS_IDP parser.
        No transformation is performed.
        """
    
        # Get environment variables
        bucket_name = os.environ.get('GCS_BUCKET')
        prefix = os.environ.get('GCS_PREFIX', 'crowdstrike-idp/')
        state_key = os.environ.get('STATE_KEY', 'crowdstrike-idp/state.json')
        client_id = os.environ.get('CROWDSTRIKE_CLIENT_ID')
        client_secret = os.environ.get('CROWDSTRIKE_CLIENT_SECRET')
        api_base = os.environ.get('API_BASE')
    
        if not all([bucket_name, client_id, client_secret, api_base]):
            print('Error: Missing required environment variables')
            return
    
        try:
            bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
    
            # Get OAuth token
            token = get_token(client_id, client_secret, api_base)
    
            # Load last processed timestamp
            last_ts = get_last_timestamp(bucket, state_key)
    
            # FQL filter for Identity Protection alerts only, newer than checkpoint
            fql_filter = f"product:'idp' + updated_timestamp:>'{last_ts}'"
            sort = 'updated_timestamp.asc'
    
            # Step 1: Get list of alert IDs
            all_ids = []
            per_page = int(os.environ.get('ALERTS_LIMIT', '1000'))
            offset = 0
    
            while True:
                page_ids = query_alert_ids(api_base, token, fql_filter, sort, per_page, offset)
                if not page_ids:
                    break
                all_ids.extend(page_ids)
                if len(page_ids) < per_page:
                    break
                offset += per_page
    
            if not all_ids:
                print('No new Identity Protection alerts.')
                return
    
            # Step 2: Get alert details in batches (max 1000 IDs per request)
            details = []
            max_batch = 1000
            for i in range(0, len(all_ids), max_batch):
                batch = all_ids[i:i + max_batch]
                details.extend(fetch_alert_details(api_base, token, batch))
    
            if details:
                # Sort by updated_timestamp
                details.sort(key=lambda d: d.get('updated_timestamp', d.get('created_timestamp', '')))
                latest = details[-1].get('updated_timestamp') or details[-1].get('created_timestamp')
    
                # Write to GCS
                timestamp = datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')
                blob_name = f"{prefix}cs_idp_{timestamp}.json"
                blob = bucket.blob(blob_name)
    
                # NDJSON format
                log_lines = '\n'.join([json.dumps(d, separators=(',', ':')) for d in details])
                blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(log_lines, content_type='application/x-ndjson')
    
                print(f'Wrote {len(details)} alerts to {blob_name}')
    
                # Update state
                update_state(bucket, state_key, latest)
    
        except Exception as e:
            print(f'Error processing alerts: {str(e)}')
            raise
    
    def get_token(client_id, client_secret, api_base):
        """Get OAuth2 token from CrowdStrike API"""
        url = f"https://{api_base}/oauth2/token"
        data = f"client_id={client_id}&client_secret={client_secret}&grant_type=client_credentials"
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    
        r = http.request('POST', url, body=data, headers=headers)
        if r.status != 200:
            raise Exception(f'Auth failed: {r.status} {r.data}')
    
        return json.loads(r.data.decode('utf-8'))['access_token']
    
    def query_alert_ids(api_base, token, fql_filter, sort, limit, offset):
        """Query alert IDs using filters"""
        url = f"https://{api_base}/alerts/queries/alerts/v2"
        params = {
            'filter': fql_filter,
            'sort': sort,
            'limit': str(limit),
            'offset': str(offset)
        }
        qs = urlencode(params)
    
        r = http.request('GET', f"{url}?{qs}", headers={'Authorization': f'Bearer {token}'})
        if r.status != 200:
            raise Exception(f'Query alerts failed: {r.status} {r.data}')
    
        resp = json.loads(r.data.decode('utf-8'))
        return resp.get('resources', [])
    
    def fetch_alert_details(api_base, token, composite_ids):
        """Fetch detailed alert data by composite IDs"""
        url = f"https://{api_base}/alerts/entities/alerts/v2"
        body = {'composite_ids': composite_ids}
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }
    
        r = http.request('POST', url, body=json.dumps(body).encode('utf-8'), headers=headers)
        if r.status != 200:
            raise Exception(f'Fetch alert details failed: {r.status} {r.data}')
    
        resp = json.loads(r.data.decode('utf-8'))
        return resp.get('resources', [])
    
    def get_last_timestamp(bucket, key, default='2023-01-01T00:00:00Z'):
        """Get last processed timestamp from GCS state file"""
        try:
            blob = bucket.blob(key)
            if blob.exists():
                state_data = blob.[download_as_text](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_download_as_text)()
                state = json.loads(state_data)
                return [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get('last_timestamp', default)
        except Exception as e:
            print(f'Warning: Could not load state: {str(e)}')
        return default
    
    def update_state(bucket, key, ts):
        """Update last processed timestamp in GCS state file"""
        state = {
            'last_timestamp': ts,
            'updated': datetime.now(timezone.utc).isoformat()
        }
        blob = bucket.blob(key)
        blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(json.dumps(state), content_type='application/json')
    

     * Second file: **requirements.txt:**
    
    functions-framework==3.*
    google-cloud-storage==2.*
    urllib3>=2.0.0
    

  3. Click **Deploy** to save and deploy the function.

  4. Wait for deployment to complete (2-3 minutes).




## Create Cloud Scheduler job

Cloud Scheduler publishes messages to the Pub/Sub topic at regular intervals, triggering the Cloud Run function.

  1. In the **GCP Console** , go to **Cloud Scheduler**.
  2. Click **Create Job**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | `crowdstrike-idp-collector-15m`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `*/15 * * * *` (every 15 minutes)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the topic `crowdstrike-idp-trigger`  
**Message body** | `{}` (empty JSON object)  
  4. Click **Create**.




### Test the scheduler job

  1. In the **Cloud Scheduler** console, find your job.
  2. Click **Force run** to trigger manually.
  3. Wait a few seconds and go to **Cloud Run > Services > crowdstrike-idp-collector > Logs**.
  4. Verify the function executed successfully.
  5. Check the GCS bucket to confirm logs were written.



## Retrieve the Google SecOps service account

Google SecOps uses a unique service account to read data from your GCS bucket. You must grant this service account access to your bucket.

### Get the service account email

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `CrowdStrike Identity Protection Services logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Crowdstrike Identity Protection Services** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Don't use service accounts from other documentation or examples.



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



## Configure a feed in Google SecOps to ingest CrowdStrike Identity Protection Services logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `CrowdStrike Identity Protection Services logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Crowdstrike Identity Protection Services** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://crowdstrike-idp-logs-bucket/crowdstrike-idp/
           

       * Replace:

         * `crowdstrike-idp-logs-bucket`: Your GCS bucket name.
         * `crowdstrike-idp/`: Prefix/folder path where logs are stored.
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

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cs-idp-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
