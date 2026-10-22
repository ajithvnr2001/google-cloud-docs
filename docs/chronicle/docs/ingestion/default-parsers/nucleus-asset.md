---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/nucleus-asset/
title: Collect Nucleus Asset Metadata logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:10:40.848094+00:00
---

# Collect Nucleus Asset Metadata logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/nucleus-asset/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Nucleus Asset Metadata logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Nucleus Security asset metadata logs to Google Security Operations using Google Cloud Storage V2.

Nucleus Security is a vulnerability management platform that aggregates and prioritizes asset metadata from multiple scanners, providing a unified view of your organization's security posture. The parser extracts fields from Nucleus asset data and maps them to the Unified Data Model (UDM), capturing asset identity, IP addresses, hostnames, and vulnerability scores.

## Before you begin

Make sure that you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * Privileged access to Nucleus Security with administrator permissions and API key access



## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `nucleus-asset-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Collect Nucleus Security API credentials

### Generate an API key

  1. Sign in to the [Nucleus Security platform](https://app.nucleussec.com/) with administrator credentials.
  2. Go to **Settings > API Keys**.
  3. Click **Generate API Key**.
  4. Enter a label for the key (for example, `Google Security Operations Integration`).
  5. Copy and securely store the API key.

**Note:** The API key provides read access to all projects and assets in your Nucleus Security account. Store it securely and do not share it.



### Identify your project ID

  1. Sign in to the Nucleus Security platform.
  2. Navigate to **Projects**.
  3. Click on the project you want to collect asset data from.
  4. Note the **Project ID** from the URL or project settings page.



### Verify permissions

To verify the API key has the required permissions:

  1. Sign in to the Nucleus Security platform.
  2. Go to **Settings > API Keys**.
  3. Confirm the API key you generated is listed and has an **Active** status.
  4. Verify the key has read access to the target project.



### Test API access

  * Test your credentials before proceeding with the integration:
        
        # Replace with your actual credentials
        API_KEY="<your-api-key>"
        PROJECT_ID="<your-project-id>"
        
        # Test API access - list assets
        curl -v -H "x-apikey: ${API_KEY}" \
          "https://app.nucleussec.com/nucleus/api/v1/projects/${PROJECT_ID}/assets?start=0&limit=10"
        




## Create service account for Cloud Run function

The Cloud Run function needs a service account with permissions to write to GCS bucket and be invoked by Pub/Sub.

### Create service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `nucleus-asset-collector-sa`
     * **Service account description** : Enter `Service account for Cloud Run function to collect Nucleus Security asset metadata logs`
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
  2. Click on your bucket name (for example, `nucleus-asset-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `nucleus-asset-collector-sa@PROJECT_ID.iam.gserviceaccount.com`)
     * **Assign roles** : Select **Storage Object Admin**
  6. Click **Save**.



## Create Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `nucleus-asset-trigger`
     * Leave other settings as default
  4. Click **Create**.



## Create Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch asset metadata from the Nucleus Security API and write it to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `nucleus-asset-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose the Pub/Sub topic (`nucleus-asset-trigger`).
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select the service account (`nucleus-asset-collector-sa`)
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `nucleus-asset-logs` | GCS bucket name  
`GCS_PREFIX` | `nucleus-assets` | Prefix for log files  
`STATE_KEY` | `nucleus-assets/state.json` | State file path  
`API_KEY` | `your-api-key` | Nucleus Security API key  
`PROJECT_ID` | `your-project-id` | Nucleus Security project ID  
`MAX_RECORDS` | `5000` | Max records per run  
`PAGE_SIZE` | `1000` | Records per page (max 1000)  
  10. In the **Variables & Secrets** section, scroll down to **Requests** :

     * **Request timeout** : Enter `600` seconds (10 minutes)
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

     * **main.py:**
    
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
    GCS_PREFIX = os.environ.get('GCS_PREFIX', 'nucleus-assets')
    STATE_KEY = os.environ.get('STATE_KEY', 'nucleus-assets/state.json')
    API_KEY = os.environ.get('API_KEY')
    PROJECT_ID = os.environ.get('PROJECT_ID')
    MAX_RECORDS = int(os.environ.get('MAX_RECORDS', '5000'))
    PAGE_SIZE = int(os.environ.get('PAGE_SIZE', '1000'))
    
    @functions_framework.cloud_event
    def main(cloud_event):
      """
      Cloud Run function triggered by Pub/Sub to fetch Nucleus Security
      asset metadata and write to GCS.
    
      Args:
        cloud_event: CloudEvent object containing Pub/Sub message
      """
    
      if not all([GCS_BUCKET, API_KEY, PROJECT_ID]):
        print('Error: Missing required environment variables')
        return
    
      try:
        # Get GCS bucket
        bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(GCS_BUCKET)
    
        # Load state
        state = load_state(bucket, STATE_KEY)
    
        now = datetime.now(timezone.utc)
        print(f"Starting asset metadata collection at {now.isoformat()}")
    
        # Fetch assets
        records, total = fetch_assets(
          api_key=API_KEY,
          project_id=PROJECT_ID,
          page_size=PAGE_SIZE,
          max_records=MAX_RECORDS,
        )
    
        if not records:
          print("No asset records found.")
          save_state(bucket, STATE_KEY, now.isoformat())
          return
    
        # Write to GCS as NDJSON
        timestamp = now.strftime('%Y%m%d_%H%M%S')
        object_key = f"{GCS_PREFIX}/assets_{timestamp}.ndjson"
        blob = bucket.blob(object_key)
    
        ndjson = '\n'.join([json.dumps(record, ensure_ascii=False) for record in records]) + '\n'
        blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(ndjson, content_type='application/x-ndjson')
    
        print(f"Wrote {len(records)} records to gs://{GCS_BUCKET}/{object_key}")
    
        # Update state
        save_state(bucket, STATE_KEY, now.isoformat())
    
        print(f"Successfully processed {len(records)} asset records")
    
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
    
    def save_state(bucket, key, last_event_time_iso: str):
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
    
    def fetch_assets(api_key: str, project_id: str, page_size: int, max_records: int):
      """
      Fetch asset metadata from Nucleus Security API with pagination.
    
      Args:
        api_key: Nucleus Security API key
        project_id: Nucleus project ID
        page_size: Number of records per page (max 1000)
        max_records: Maximum total records to fetch
    
      Returns:
        Tuple of (records list, total count)
      """
      endpoint = f"https://app.nucleussec.com/nucleus/api/v1/projects/{project_id}/assets"
    
      headers = {
        'x-apikey': api_key,
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'User-Agent': 'GoogleSecOps-NucleusAssetCollector/1.0',
      }
    
      records = []
      page_num = 0
      backoff = 1.0
      start_index = 0
    
      while True:
        page_num += 1
    
        if len(records) >= max_records:
          print(f"Reached max_records limit ({max_records})")
          break
    
        current_limit = min(page_size, max_records - len(records))
        url = f"{endpoint}?start={start_index}&limit={current_limit}"
    
        try:
          response = http.request('GET', url, headers=headers)
    
          # Handle rate limiting with exponential backoff
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
            return [], 0
    
          data = json.loads(response.data.decode('utf-8'))
    
          # Nucleus API returns a list of assets directly
          if isinstance(data, list):
            page_results = data
          else:
            page_results = data.get('assets', data.get('results', []))
    
          if not page_results:
            print(f"No more results (empty page)")
            break
    
          print(f"Page {page_num}: Retrieved {len(page_results)} assets")
          records.extend(page_results)
    
          # Check for more results
          if len(page_results) < current_limit:
            print(f"Reached last page (size={len(page_results)} < limit={current_limit})")
            break
    
          start_index += len(page_results)
    
        except Exception as e:
          print(f"Error fetching assets: {e}")
          return [], 0
    
      print(f"Retrieved {len(records)} total assets from {page_num} pages")
      return records, len(records)
    

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
**Name** | `nucleus-asset-collector-daily`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 0 * * *` (daily at midnight)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the Pub/Sub topic (`nucleus-asset-trigger`)  
**Message body** | `{}` (empty JSON object)  
  4. Click **Create**.




### Schedule frequency options

Choose frequency based on log volume and latency requirements:

Frequency | Cron Expression | Use Case  
---|---|---  
Every 5 minutes | `*/5 * * * *` | High-volume, low-latency  
Every 15 minutes | `*/15 * * * *` | Medium volume  
Every hour | `0 * * * *` | Standard  
Every 6 hours | `0 */6 * * *` | Low volume, batch processing  
Daily | `0 0 * * *` | Asset inventory snapshots (recommended)  
  
### Test the integration

  1. In the **Cloud Scheduler** console, find your job.
  2. Click **Force run** to trigger the job manually.
  3. Wait a few seconds.
  4. Go to **Cloud Run > Services**.
  5. Click on your function name (`nucleus-asset-collector`).
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         Starting asset metadata collection at YYYY-MM-DDTHH:MM:SS+00:00
         Page 1: Retrieved X assets
         Wrote X records to gs://nucleus-asset-logs/nucleus-assets/assets_YYYYMMDD_HHMMSS.ndjson
         Successfully processed X asset records
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click on your bucket name (`nucleus-asset-logs`).

  10. Navigate to the prefix folder (`nucleus-assets/`).

  11. Verify that a new `.ndjson` file was created with the current timestamp.




If you see errors in the logs:

  * **HTTP 401** : Check the API key in environment variables
  * **HTTP 403** : Verify the API key has read access to the project
  * **HTTP 429** : Rate limiting - function will automatically retry with backoff
  * **Missing environment variables** : Check all required variables are set



## Retrieve the Google SecOps service account

Google SecOps uses a unique service account to read data from your GCS bucket. You must grant this service account access to your bucket.

### Get the service account email

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Nucleus Asset Metadata Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Nucleus Asset Metadata** as the **Log type**.
  7. Click **Get Service Account**.
  8. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  9. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Don't use service accounts from other documentation or examples.
  10. Click **Next**.

  11. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://nucleus-asset-logs/nucleus-assets/
           

       * Replace: 
         * `nucleus-asset-logs`: Your GCS bucket name.
         * `nucleus-assets`: Optional prefix/folder path where logs are stored (leave empty for root).
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
  2. Click on your bucket name (for example, `nucleus-asset-logs`).
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
host_score_total, host_complianced_score, host_data_sensitivity_score, host_public, asset_tags | entity.asset.attribute.labels | Labels merged from host_score_total as "Host Score Total", host_complianced_score as "Host Complianced Score", host_data_sensitivity_score as "Host Data Sensitivity Score", host_public as "Host Public", and asset_tags parsed as key-value pairs  
asset_name | entity.asset.hostname | Extracted from asset_name using grok pattern if contains "http"  
ip_address | entity.asset.ip | Merged from ip_address  
asset_id | entity.asset.product_object_id | Value copied directly if not empty  
asset_name | entity.url | Extracted from asset_name using grok pattern if contains "http" and url_path not empty  
| metadata.entity_type | Set to "ASSET"  
| metadata.product_name | Set to "Nucleus Unified Vulnerability Management"  
| metadata.vendor_name | Set to "NUCLEUS"  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
