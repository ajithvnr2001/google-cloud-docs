---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-cloudlock-casb/
title: Collect Cisco CloudLock CASB logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:52:37.451791+00:00
---

# Collect Cisco CloudLock CASB logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-cloudlock-casb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Cisco CloudLock CASB logs

**Parser Version:** 3.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Cisco CloudLock CASB logs to Google Security Operations using Google Cloud Storage. A Cloud Run function polls the Cisco CloudLock API on a schedule and writes incident, activity, and entity data to a GCS bucket, which Google SecOps then ingests via a GCS V2 feed.

Cisco CloudLock is a cloud-native Cloud Access Security Broker (CASB) that provides visibility and control over cloud applications. It helps organizations discover shadow IT, enforce data loss prevention policies, detect threats, and maintain compliance across SaaS applications.

**Note:** Cisco CloudLock has been integrated into Cisco Umbrella as part of Cisco's security portfolio consolidation. For new deployments, use Cisco Umbrella which includes CloudLock CASB functionality. This guide applies to existing standalone CloudLock deployments.

## Before you begin

Make sure that you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * Privileged access to Cisco CloudLock admin console
  * Cisco CloudLock API Base URL (provided by Cisco CloudLock Support)



## Get Cisco CloudLock API credentials

To get started, contact Cisco CloudLock Support to obtain your CloudLock API URL. The API base URL is specific to your tenant and is not publicly available. Generate an access token in the CloudLock application by navigating to the Authentication & API tab in the Settings page.

  1. Sign in to the **Cisco CloudLock** admin console.
  2. Go to **Settings > Authentication & API**.
  3. Under **API** , click **Generate** to create your access token.
  4. Copy and save the following details in a secure location:

     * **API Access Token** : The Bearer token displayed after clicking Generate.
     * **API Base URL** : Provided by Cisco CloudLock Support. The format is `https://{YourCloudlockAPIServer}`.
**Note:** Only one API token can be generated at a time per user, per CloudLock environment. Generating a new token invalidates any previously generated token.**Note:** API keys, passwords, secrets, and tokens allow access to your private customer data and should never be shared with another user or organization.



### Verify API access

  * Test your credentials before proceeding with the integration:
        
        CLOUDLOCK_API_TOKEN="your-api-token"
        CLOUDLOCK_API_BASE="https://your-cloudlock-api-server"
        
        curl -v -H "Authorization: Bearer ${CLOUDLOCK_API_TOKEN}" \
          "${CLOUDLOCK_API_BASE}/api/v2/incidents?limit=1"
        




A successful response returns HTTP 200 with a JSON object containing an `items` array. If you receive HTTP 401, verify the API token. If you receive HTTP 403, confirm the account has the required permissions.

## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `cisco-cloudlock-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Create service account for Cloud Run function

The Cloud Run function needs a service account with permissions to write to GCS bucket and be invoked by Pub/Sub.

### Create service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `cloudlock-data-export-sa`.
     * **Service account description** : Enter `Service account for Cloud Run function to collect Cisco CloudLock logs`.
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



### Grant IAM permissions on GCS bucket

Grant the service account write permissions on the GCS bucket:

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `cloudlock-data-export-sa@PROJECT_ID.iam.gserviceaccount.com`).
     * **Assign roles** : Select **Storage Object Admin**.
  6. Click **Save**.



## Create Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `cloudlock-data-export-trigger`.
     * Leave other settings as default.
  4. Click **Create**.



## Create Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from Cisco CloudLock API and write them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `cloudlock-data-export`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose the topic (`cloudlock-data-export-trigger`).
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select the service account (`cloudlock-data-export-sa`).
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `cisco-cloudlock-logs` | GCS bucket name  
`GCS_PREFIX` | `cloudlock/` | Prefix for log files  
`STATE_KEY` | `cloudlock/state.json` | State file path  
`CLOUDLOCK_API_TOKEN` | `your-api-token` | API Bearer token  
`CLOUDLOCK_API_BASE` | `https://your-cloudlock-api-server` | API base URL from CloudLock Support  
  10. Scroll down in the **Variables & Secrets** tab to **Requests** :

     * **Request timeout** : Enter `600` seconds (10 minutes).
  11. Go to the **Settings** tab in **Containers** :

     * In the **Resources** section: 
       * **Memory** : Select **512 MiB** or higher.
       * **CPU** : Select **1**.
     * Click **Done**.
  12. Scroll down to **Execution environment** :

     * Select **Default** (recommended).
  13. In the **Revision scaling** section:

     * **Minimum number of instances** : Enter `0`.
     * **Maximum number of instances** : Enter `100` (or adjust based on expected load).
  14. Click **Create**.

  15. Wait for the service to be created (1-2 minutes).

  16. After the service is created, the **inline code editor** will open automatically.




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
           
           @functions_framework.cloud_event
           def main(cloud_event):
               """
               Cloud Run function triggered by Pub/Sub to fetch logs from Cisco CloudLock API and write to GCS.
           
               Args:
                   cloud_event: CloudEvent object containing Pub/Sub message
               """
           
               # Get environment variables
               bucket_name = os.environ.get('GCS_BUCKET')
               prefix = os.environ.get('GCS_PREFIX', 'cloudlock/')
               state_key = os.environ.get('STATE_KEY', 'cloudlock/state.json')
               api_token = os.environ.get('CLOUDLOCK_API_TOKEN')
               api_base = os.environ.get('CLOUDLOCK_API_BASE')
           
               if not all([bucket_name, api_token, api_base]):
                   print('Error: Missing required environment variables')
                   return
           
               try:
                   # Get GCS bucket
                   bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
           
                   # Load state (last processed offset for each endpoint)
                   state = load_state(bucket, state_key)
           
                   print(f'Processing logs with state: {[state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state)}')
           
                   # Create Authorization header
                   headers = {
                       'Authorization': f'Bearer {api_token}',
                       'Content-Type': 'application/json'
                   }
           
                   # Fetch incidents data (using offset-based pagination)
                   incidents_offset = [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get('incidents_offset', 0)
                   incidents, new_incidents_offset = fetch_cloudlock_incidents(
                       http, api_base, headers, incidents_offset
                   )
           
                   if incidents:
                       upload_to_gcs_ndjson(bucket, prefix, 'incidents', incidents)
                       print(f'Uploaded {len(incidents)} incidents to GCS')
                       state['incidents_offset'] = new_incidents_offset
           
                   # Fetch activities data (using time-based filtering with offset pagination)
                   activities_last_time = [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get('activities_last_time')
                   if not activities_last_time:
                       activities_last_time = (datetime.now(timezone.utc) - timedelta(hours=24)).isoformat()
           
                   activities_offset = [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get('activities_offset', 0)
                   activities, new_activities_offset, newest_activity_time = fetch_cloudlock_activities(
                       http, api_base, headers, activities_last_time, activities_offset
                   )
           
                   if activities:
                       upload_to_gcs_ndjson(bucket, prefix, 'activities', activities)
                       print(f'Uploaded {len(activities)} activities to GCS')
                       state['activities_offset'] = new_activities_offset
                       if newest_activity_time:
                           state['activities_last_time'] = newest_activity_time
           
                   # Fetch entities data (using offset-based pagination)
                   entities_offset = [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get('entities_offset', 0)
                   entities, new_entities_offset = fetch_cloudlock_entities(
                       http, api_base, headers, entities_offset
                   )
           
                   if entities:
                       upload_to_gcs_ndjson(bucket, prefix, 'entities', entities)
                       print(f'Uploaded {len(entities)} entities to GCS')
                       state['entities_offset'] = new_entities_offset
           
                   # Update consolidated state
                   state['updated_at'] = datetime.now(timezone.utc).isoformat()
                   save_state(bucket, state_key, state)
           
                   print('CloudLock data export completed successfully')
           
               except Exception as e:
                   print(f'Error processing logs: {str(e)}')
                   raise
           
           def make_api_request(http, url, headers, retries=3):
               """Make API request with exponential backoff retry logic."""
               backoff = 1.0
               for attempt in range(retries):
                   try:
                       response = http.request('GET', url, headers=headers)
           
                       if response.status == 200:
                           return response
                       elif response.status == 429:
                           # Rate limit - CloudLock enforces per-endpoint rate limits
                           retry_after = int(response.headers.get('Retry-After', str(int(backoff))))
                           print(f'Rate limited (429), waiting {retry_after} seconds')
                           time.sleep(retry_after)
                           backoff = min(backoff * 2, 60.0)
                       else:
                           print(f'API request failed with status {response.status}: {response.data.decode("utf-8")}')
                           if response.status in (401, 403):
                               return None
                   except Exception as e:
                       print(f'Request attempt {attempt + 1} failed: {str(e)}')
                       if attempt < retries - 1:
                           wait_time = 2 ** attempt
                           time.sleep(wait_time)
                       else:
                           raise
           
               return None
           
           def fetch_cloudlock_incidents(http, api_base, headers, start_offset=0):
               """
               Fetch incidents data from Cisco CloudLock API using offset-based pagination.
           
               Endpoint: GET /api/v2/incidents
               Pagination: limit and offset query parameters.
               Response: JSON with 'items' array, 'total' count, and 'results' count.
               """
               url = f"{api_base}/api/v2/incidents"
           
               limit = 1000
               offset = start_offset
               all_data = []
           
               try:
                   while True:
                       # Build URL with parameters
                       full_url = f"{url}?limit={limit}&offset={offset}"
           
                       print(f"Fetching incidents with offset: {offset}")
           
                       response = make_api_request(http, full_url, headers)
                       if not response:
                           break
           
                       data = json.loads(response.data.decode('utf-8'))
           
                       # CloudLock API returns items in 'items' array
                       batch_data = data.get('items', [])
           
                       if not batch_data:
                           print("No more incidents to fetch")
                           break
           
                       all_data.extend(batch_data)
           
                       # Check if we've reached the end
                       total = data.get('total', 0)
                       results = data.get('results', len(batch_data))
           
                       print(f"Fetched {results} incidents (total available: {total})")
           
                       if results < limit or offset + results >= total:
                           print("Reached end of incidents")
                           break
           
                       offset += limit
           
                   print(f"Fetched {len(all_data)} total incidents")
                   return all_data, offset
           
               except Exception as e:
                   print(f"Error fetching incidents: {str(e)}")
                   return [], start_offset
           
           def fetch_cloudlock_activities(http, api_base, headers, from_time, start_offset=0):
               """
               Fetch activities data from Cisco CloudLock API using time-based filtering and offset pagination.
           
               Endpoint: GET /api/v2/activities
               Pagination: limit and offset query parameters.
               Note: Client-side time filtering is applied since the API may not support time range parameters.
               """
               url = f"{api_base}/api/v2/activities"
           
               limit = 1000
               offset = start_offset
               all_data = []
               newest_time = None
           
               try:
                   while True:
                       # Build URL with pagination
                       full_url = f"{url}?limit={limit}&offset={offset}"
           
                       print(f"Fetching activities with offset: {offset}")
           
                       response = make_api_request(http, full_url, headers)
                       if not response:
                           break
           
                       data = json.loads(response.data.decode('utf-8'))
                       batch_data = data.get('items', [])
           
                       if not batch_data:
                           print("No more activities to fetch")
                           break
           
                       # Filter activities by time (client-side filtering)
                       filtered_batch = []
                       for item in batch_data:
                           item_time = item.get('timestamp') or item.get('created_at')
                           if item_time and item_time >= from_time:
                               filtered_batch.append(item)
                               if not newest_time or item_time > newest_time:
                                   newest_time = item_time
           
                       all_data.extend(filtered_batch)
           
                       results = data.get('results', len(batch_data))
                       total = data.get('total', 0)
           
                       print(f"Fetched {results} activities, {len(filtered_batch)} after time filter (total available: {total})")
           
                       if results < limit or offset + results >= total:
                           print("Reached end of activities")
                           break
           
                       offset += limit
           
                   print(f"Fetched {len(all_data)} total activities")
                   return all_data, offset, newest_time
           
               except Exception as e:
                   print(f"Error fetching activities: {str(e)}")
                   return [], start_offset, None
           
           def fetch_cloudlock_entities(http, api_base, headers, start_offset=0):
               """
               Fetch entities data from Cisco CloudLock API using offset-based pagination.
           
               Endpoint: GET /api/v2/entities
               Note: This endpoint requires the Entity Cache feature. If not enabled,
               use the incident entities endpoint (/api/v2/incidents/{id}/entities) as an alternative.
               """
               url = f"{api_base}/api/v2/entities"
           
               limit = 1000
               offset = start_offset
               all_data = []
           
               try:
                   while True:
                       full_url = f"{url}?limit={limit}&offset={offset}"
           
                       print(f"Fetching entities with offset: {offset}")
           
                       response = make_api_request(http, full_url, headers)
                       if not response:
                           break
           
                       data = json.loads(response.data.decode('utf-8'))
                       batch_data = data.get('items', [])
           
                       if not batch_data:
                           print("No more entities to fetch")
                           break
           
                       all_data.extend(batch_data)
           
                       results = data.get('results', len(batch_data))
                       total = data.get('total', 0)
           
                       print(f"Fetched {results} entities (total available: {total})")
           
                       if results < limit or offset + results >= total:
                           print("Reached end of entities")
                           break
           
                       offset += limit
           
                   print(f"Fetched {len(all_data)} total entities")
                   return all_data, offset
           
               except Exception as e:
                   print(f"Error fetching entities: {str(e)}")
                   return [], start_offset
           
           def upload_to_gcs_ndjson(bucket, prefix, data_type, data):
               """Upload data to GCS bucket in NDJSON format (one JSON object per line)."""
               timestamp = datetime.now(timezone.utc).strftime('%Y/%m/%d/%H')
               filename = f"{prefix}{data_type}/{timestamp}/cloudlock_{data_type}_{int(datetime.now(timezone.utc).timestamp())}.jsonl"
           
               try:
                   # Convert to NDJSON format
                   ndjson_content = '\n'.join([json.dumps(item, separators=(',', ':')) for item in data])
           
                   blob = bucket.blob(filename)
                   blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
                       ndjson_content,
                       content_type='application/x-ndjson'
                   )
           
                   print(f"Successfully uploaded {filename} to GCS")
           
               except Exception as e:
                   print(f"Error uploading to GCS: {str(e)}")
                   raise
           
           def load_state(bucket, key):
               """Load state from GCS with separate tracking for each endpoint."""
               try:
                   blob = bucket.blob(key)
                   if blob.exists():
                       state_data = blob.[download_as_text](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_download_as_text)()
                       return json.loads(state_data)
               except Exception as e:
                   print(f'Warning: Could not load state: {str(e)}')
           
               print("No previous state found, starting fresh")
               return {}
           
           def save_state(bucket, key, state):
               """Save consolidated state to GCS."""
               try:
                   blob = bucket.blob(key)
                   blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
                       json.dumps(state, indent=2),
                       content_type='application/json'
                   )
                   print("Updated state successfully")
               except Exception as e:
                   print(f"Error updating state: {str(e)}")
                   raise
           

     * **requirements.txt:**
           
           functions-framework==3.*
           google-cloud-storage==2.*
           urllib3>=2.0.0
           

  3. Click **Deploy** to save and deploy the function.

  4. Wait for deployment to complete (2-3 minutes).

**Note:** This script uses Cisco CloudLock API v2 endpoints (`/api/v2/incidents`, `/api/v2/activities`, `/api/v2/entities`) with offset-based pagination (`limit` and `offset` query parameters) as documented in the [Cisco DevNet CloudLock API reference](https://developer.cisco.com/docs/cloud-security/cloudlock-api-getting-started/). The Entities endpoint requires the Entity Cache feature to be enabled. For production deployments, contact Cisco CloudLock Support to verify the most current API capabilities for your tenant.



## Create Cloud Scheduler job

Cloud Scheduler will publish messages to the Pub/Sub topic at regular intervals, triggering the Cloud Run function.

  1. In the **GCP Console** , go to **Cloud Scheduler**.
  2. Click **Create Job**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | `cloudlock-data-export-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the topic (`cloudlock-data-export-trigger`)  
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

  1. In the **Cloud Scheduler** console, find your job.
  2. Click **Force run** to trigger the job manually.
  3. Wait a few seconds.
  4. Go to **Cloud Run > Services**.
  5. Click on the function name (`cloudlock-data-export`).
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         Processing logs with state: {}
         Fetching incidents with offset: 0
         Fetched X incidents (total available: Y)
         Uploaded X incidents to GCS
         CloudLock data export completed successfully
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click on the bucket name (`cisco-cloudlock-logs`).

  10. Navigate to the `cloudlock/` prefix folder.

  11. Verify that new `.jsonl` files were created under the `incidents/`, `activities/`, or `entities/` subfolders.




If you see errors in the logs:

  * **HTTP 401** : Check the API token in environment variables
  * **HTTP 403** : Verify the CloudLock account has the required permissions
  * **HTTP 429** : Rate limiting - the function will automatically retry with backoff
  * **Missing environment variables** : Check all required variables are set
  * **Empty entities** : The Entities endpoint requires the Entity Cache feature - contact CloudLock Support to enable it



## Configure a feed in Google SecOps to ingest Cisco CloudLock logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Cisco CloudLock logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Cisco CloudLock** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Do not use service accounts from other documentation or examples.
  9. Click **Next**.

  10. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://cisco-cloudlock-logs/cloudlock/
           

       * Replace: 
         * `cisco-cloudlock-logs`: Your GCS bucket name.
         * `cloudlock/`: Optional prefix/folder path where logs are stored (leave empty for root).
**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never** : Never deletes any files after transfers (recommended for testing).
       * **Delete transferred files** : Deletes files after successful transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.
**Note:** If you select a deletion option, the service account must have **Storage Object Admin** role instead of Storage Object Viewer. Update IAM permissions accordingly.
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days).

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).

     * **Ingestion labels** : The label to be applied to the events from this feed.

  11. Click **Next**.

  12. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




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



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
created_at | about.resource.attribute.creation_time | The value of `created_at` from the raw log is parsed as a timestamp and mapped to the `about.resource.attribute.creation_time` field.  
created_at | about.resource.attribute.labels.key | The value of `created_at` is assigned to the labels key.  
created_at | about.resource.attribute.labels.value | The value of `created_at` is assigned to the labels value.  
entity.id | target.asset.product_object_id | The value of `entity.id` from the raw log is mapped to the `target.asset.product_object_id` field.  
entity.ip | target.ip | The value of `entity.ip` from the raw log is merged into the `target.ip` field.  
entity.mime_type | target.file.mime_type | The value of `entity.mime_type` from the raw log is mapped to the `target.file.mime_type` field when `entity.origin_type` is "document".  
entity.name | target.application | The value of `entity.name` from the raw log is mapped to the `target.application` field when `entity.origin_type` is "app".  
entity.name | target.file.full_path | The value of `entity.name` from the raw log is mapped to the `target.file.full_path` field when `entity.origin_type` is "document".  
entity.origin_id | target.resource.product_object_id | The value of `entity.origin_id` from the raw log is mapped to the `target.resource.product_object_id` field.  
entity.origin_type | target.resource.resource_subtype | The value of `entity.origin_type` from the raw log is mapped to the `target.resource.resource_subtype` field.  
entity.owner_email | target.user.email_addresses | The value of `entity.owner_email` from the raw log is merged into the `target.user.email_addresses` field if it matches an email regex.  
entity.owner_email | target.user.user_display_name | The value of `entity.owner_email` from the raw log is mapped to the `target.user.user_display_name` field if it does not match an email regex.  
entity.owner_name | target.user.user_display_name | The value of `entity.owner_name` from the raw log is mapped to the `target.user.user_display_name` field when `entity.owner_email` matches an email regex.  
entity.vendor.name | target.platform_version | The value of `entity.vendor.name` from the raw log is mapped to the `target.platform_version` field.  
id | metadata.product_log_id | The value of `id` from the raw log is mapped to the `metadata.product_log_id` field.  
incident_status | metadata.product_event_type | The value of `incident_status` from the raw log is mapped to the `metadata.product_event_type` field.  
policy.id | security_result.rule_id | The value of `policy.id` from the raw log is mapped to the `security_result.rule_id` field.  
policy.name | security_result.rule_name | The value of `policy.name` from the raw log is mapped to the `security_result.rule_name` field.  
severity | security_result.severity_details | The value of `severity` from the raw log is mapped to the `security_result.severity_details` field.  
updated_at | about.resource.attribute.labels.key | The value of `updated_at` is assigned to the labels key.  
updated_at | about.resource.attribute.labels.value | The value of `updated_at` is assigned to the labels value.  
updated_at | about.resource.attribute.last_update_time | The value of `updated_at` from the raw log is parsed as a timestamp and mapped to the `about.resource.attribute.last_update_time` field.  
N/A | metadata.event_timestamp | Derived from the `updated_at` field. The value is parsed as a timestamp and mapped.  
N/A | metadata.event_type | Set to "GENERIC_EVENT".  
N/A | metadata.product_name | Set to "CISCO_CLOUDLOCK_CASB".  
N/A | metadata.product_version | Set to "Cisco".  
N/A | metadata.vendor_name | Set to "CloudLock".  
N/A | security_result.alert_state | Set to "ALERTING" if `severity` is "ALERT" and `incident_status` is not "RESOLVED" or "DISMISSED". Set to "NOT_ALERTING" if `severity` is "ALERT" and `incident_status` is "RESOLVED" or "DISMISSED".  
N/A | security_result.detection_fields.key | Derived from the `matches` array, specifically the key of each match object. Also set to "true" if `severity` is "ALERT" and `incident_status` is "NEW".  
N/A | security_result.detection_fields.value | Derived from the `matches` array, specifically the value of each match object. Also set to "true" if `severity` is "ALERT" and `incident_status` is "NEW".  
N/A | security_result.severity | Set to "INFORMATIONAL" if `severity` is "INFO". Set to "CRITICAL" if `severity` is "CRITICAL". Derived from the `severity` field.  
N/A | security_result.summary | Set to "match count: " concatenated with the value of `match_count`.  
N/A | target.resource.resource_type | Set to "STORAGE_OBJECT" when `entity.origin_type` is "document".  
N/A | target.url | Derived from `entity.direct_url` when `entity.origin_type` is "document".  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
