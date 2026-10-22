---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/proofpoint-web-browser-isolation/
title: Collect Proofpoint Web Browser Isolation logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:18:49.611481+00:00
---

# Collect Proofpoint Web Browser Isolation logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/proofpoint-web-browser-isolation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Proofpoint Web Browser Isolation logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Proofpoint Web Browser Isolation logs to Google Security Operations using Google Cloud Storage V2.

Proofpoint Web Browser Isolation is a remote browser isolation service that protects users from web-based threats by rendering web content in a secure cloud environment, preventing malicious code from reaching the endpoint. It provides browsing activity logs through the Proofpoint TAP SIEM API. The parser extracts fields from isolation event data and maps them to the Unified Data Model (UDM), capturing URL classifications, user actions, security dispositions, and browsing session metadata.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * Privileged access to Proofpoint with TAP SIEM API credentials (Service Principal and API Secret)



## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `proofpoint-wbi-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Collect Proofpoint TAP SIEM API credentials

### Obtain API credentials

  1. Sign in to the [Proofpoint TAP dashboard](https://threatinsight.proofpoint.com/).
  2. Navigate to **Settings > Connected Applications**.
  3. Click **Create New Credential** (or use an existing SIEM API credential).
  4. Copy and securely store the following credentials:

     * **Service Principal** : Copy this value
     * **API Secret** : Copy this value
**Note:** The TAP SIEM API uses HTTP Basic authentication with the Service Principal as the username and the API Secret as the password. Contact Proofpoint support to confirm that browser isolation events are included in your subscription tier.



### Verify permissions

To verify the API credentials have the required permissions:

  1. Sign in to the Proofpoint TAP dashboard.
  2. Navigate to **Settings > Connected Applications**.
  3. Confirm the credential is listed and has an **Active** status.
  4. Verify the credential has SIEM API access enabled.



### Test API access

  * Test your credentials before proceeding with the integration:
        
        # Replace with your actual credentials
        SERVICE_PRINCIPAL="<your-service-principal>"
        API_SECRET="<your-api-secret>"
        
        # Test TAP SIEM API access - fetch events from last hour
        curl -v -u "${SERVICE_PRINCIPAL}:${API_SECRET}" \
          "https://tap-api-v2.proofpoint.com/v2/siem/all?format=json&sinceSeconds=3600"
        




## Create a service account for the Cloud Run function

The Cloud Run function needs a service account with permissions to write to GCS bucket and be invoked by Pub/Sub.

### Create service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `proofpoint-wbi-collector-sa`
     * **Service account description** : Enter `Service account for Cloud Run function to collect Proofpoint Web Browser Isolation logs`
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
  2. Click on your bucket name (for example, `proofpoint-wbi-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `proofpoint-wbi-collector-sa@PROJECT_ID.iam.gserviceaccount.com`)
     * **Assign roles** : Select **Storage Object Admin**
  6. Click **Save**.



## Create a Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `proofpoint-wbi-trigger`
     * Leave other settings as default
  4. Click **Create**.



## Create a Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch browser isolation events from the Proofpoint TAP SIEM API and write them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `proofpoint-wbi-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose the Pub/Sub topic (`proofpoint-wbi-trigger`).
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select the service account (`proofpoint-wbi-collector-sa`)
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `proofpoint-wbi-logs` | GCS bucket name  
`GCS_PREFIX` | `wbi-logs` | Prefix for log files  
`STATE_KEY` | `wbi-logs/state.json` | State file path  
`SERVICE_PRINCIPAL` | `your-service-principal` | Proofpoint TAP Service Principal  
`API_SECRET` | `your-api-secret` | Proofpoint TAP API Secret  
`LOOKBACK_SECONDS` | `3600` | Lookback period in seconds (default: 1 hour)  
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

     * First file - **main.py:**
           
           import functions_framework
           from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
           import json
           import os
           import urllib3
           from datetime import datetime, timezone, timedelta
           import time
           import base64
           
           # Initialize HTTP client with timeouts
           http = urllib3.PoolManager(
             timeout=urllib3.Timeout(connect=5.0, read=60.0),
             retries=False,
           )
           
           # Initialize Storage client
           storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
           
           # Environment variables
           GCS_BUCKET = os.environ.get('GCS_BUCKET')
           GCS_PREFIX = os.environ.get('GCS_PREFIX', 'wbi-logs')
           STATE_KEY = os.environ.get('STATE_KEY', 'wbi-logs/state.json')
           SERVICE_PRINCIPAL = os.environ.get('SERVICE_PRINCIPAL')
           API_SECRET = os.environ.get('API_SECRET')
           LOOKBACK_SECONDS = int(os.environ.get('LOOKBACK_SECONDS', '3600'))
           
           TAP_API_BASE = "https://tap-api-v2.proofpoint.com/v2/siem"
           
           def parse_datetime(value: str) -> datetime:
             """Parse ISO datetime string to datetime object."""
             if [value](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.ObjectCustomContextPayload.html#google_cloud_storage_blob_ObjectCustomContextPayload_value).endswith("Z"):
               value = value[:-1] + "+00:00"
             return datetime.fromisoformat(value)
           
           @functions_framework.cloud_event
           def main(cloud_event):
             """
             Cloud Run function triggered by Pub/Sub to fetch Proofpoint
             Web Browser Isolation events via TAP SIEM API and write to GCS.
           
             Args:
               cloud_event: CloudEvent object containing Pub/Sub message
             """
           
             if not all([GCS_BUCKET, SERVICE_PRINCIPAL, API_SECRET]):
               print('Error: Missing required environment variables')
               return
           
             try:
               # Get GCS bucket
               bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(GCS_BUCKET)
           
               # Load state
               state = load_state(bucket, STATE_KEY)
           
               now = datetime.now(timezone.utc)
           
               # Determine since_seconds from state
               since_seconds = LOOKBACK_SECONDS
               if isinstance(state, dict) and [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get("last_event_time"):
                 try:
                   last_time = parse_datetime(state["last_event_time"])
                   elapsed = (now - last_time).total_seconds()
                   # Add 120 seconds overlap to catch delayed events
                   since_seconds = int(elapsed) + 120
                   # TAP API maximum is 1 hour (3600 seconds)
                   since_seconds = min(since_seconds, 3600)
                 except Exception as e:
                   print(f"Warning: Could not parse last_event_time: {e}")
           
               print(f"Fetching events from last {since_seconds} seconds")
           
               # Build auth header (Basic auth)
               auth_string = f"{SERVICE_PRINCIPAL}:{API_SECRET}"
               auth_bytes = auth_string.encode('utf-8')
               auth_b64 = base64.b64encode(auth_bytes).decode('utf-8')
           
               # Fetch all SIEM events
               records = fetch_siem_events(
                 auth_b64=auth_b64,
                 since_seconds=since_seconds,
               )
           
               if not records:
                 print("No new events found.")
                 save_state(bucket, STATE_KEY, now.isoformat())
                 return
           
               # Write to GCS as NDJSON
               timestamp = now.strftime('%Y%m%d_%H%M%S')
               object_key = f"{GCS_PREFIX}/logs_{timestamp}.ndjson"
               blob = bucket.blob(object_key)
           
               ndjson = '\n'.join([json.dumps(record, ensure_ascii=False) for record in records]) + '\n'
               blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(ndjson, content_type='application/x-ndjson')
           
               print(f"Wrote {len(records)} records to gs://{GCS_BUCKET}/{object_key}")
           
               # Update state
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
           
           def fetch_siem_events(auth_b64: str, since_seconds: int):
             """
             Fetch events from the Proofpoint TAP SIEM API.
           
             The TAP SIEM API returns all event types (clicks, messages, isolation)
             in a single response. The sinceSeconds parameter controls the lookback window
             (maximum 3600 seconds / 1 hour).
           
             Args:
               auth_b64: Base64-encoded Service Principal:API Secret for Basic auth
               since_seconds: Fetch events from the last N seconds (max 3600)
           
             Returns:
               List of event records
             """
             headers = {
               'Authorization': f'Basic {auth_b64}',
               'Accept': 'application/json',
               'User-Agent': 'GoogleSecOps-ProofpointWBICollector/1.0',
             }
           
             url = f"{TAP_API_BASE}/all?format=json&sinceSeconds={since_seconds}"
             backoff = 1.0
             max_retries = 3
           
             for attempt in range(max_retries):
               try:
                 response = http.request('GET', url, headers=headers)
           
                 # Handle rate limiting with exponential backoff
                 if response.status == 429:
                   retry_after = int(response.headers.get('Retry-After', str(int(backoff))))
                   print(f"Rate limited (429). Retrying after {retry_after}s...")
                   time.sleep(retry_after)
                   backoff = min(backoff * 2, 30.0)
                   continue
           
                 if response.status != 200:
                   print(f"HTTP Error: {response.status}")
                   response_text = response.data.decode('utf-8')
                   print(f"Response body: {response_text}")
                   return []
           
                 data = json.loads(response.data.decode('utf-8'))
           
                 # TAP SIEM API returns events grouped by type
                 all_events = []
           
                 # Collect all event types
                 for key in ['clicksPermitted', 'clicksBlocked', 'messagesDelivered', 'messagesBlocked']:
                   events = data.get(key, [])
                   if events:
                     for event in events:
                       event['_tap_event_type'] = key
                     all_events.extend(events)
                     print(f"Retrieved {len(events)} {key} events")
           
                 print(f"Total events retrieved: {len(all_events)}")
                 return all_events
           
               except Exception as e:
                 print(f"Error fetching SIEM events (attempt {attempt + 1}): {e}")
                 if attempt < max_retries - 1:
                   time.sleep(backoff)
                   backoff = min(backoff * 2, 30.0)
           
             return []
           

     * Second file - **requirements.txt:**
           
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
**Name** | `proofpoint-wbi-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the Pub/Sub topic (`proofpoint-wbi-trigger`)  
**Message body** | `{}` (empty JSON object)  
  4. Click **Create**.




### Schedule frequency options

Choose frequency based on log volume and latency requirements:

Frequency | Cron Expression | Use Case  
---|---|---  
Every 5 minutes | `*/5 * * * *` | High-volume, low-latency  
Every 15 minutes | `*/15 * * * *` | Medium volume  
Every hour | `0 * * * *` | Standard (recommended)  
**Note:** The Proofpoint TAP SIEM API has a maximum lookback of 3600 seconds (1 hour). Schedule the function to run at least once per hour to avoid missing events.

### Test the integration

  1. In the **Cloud Scheduler** console, find your job.
  2. Click **Force run** to trigger the job manually.
  3. Wait a few seconds.
  4. Go to **Cloud Run > Services**.
  5. Click on your function name (`proofpoint-wbi-collector`).
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         Fetching events from last 3600 seconds
         Retrieved X clicksPermitted events
         Retrieved X messagesDelivered events
         Total events retrieved: X
         Wrote X records to gs://proofpoint-wbi-logs/wbi-logs/logs_YYYYMMDD_HHMMSS.ndjson
         Successfully processed X records
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click on your bucket name (`proofpoint-wbi-logs`).

  10. Navigate to the prefix folder (`wbi-logs/`).

  11. Verify that a new `.ndjson` file was created with the current timestamp.




If you see errors in the logs:

  * **HTTP 401** : Check the Service Principal and API Secret in environment variables
  * **HTTP 403** : Verify the credential has SIEM API access and browser isolation events are included in your subscription
  * **HTTP 429** : Rate limiting - function will automatically retry with backoff
  * **Missing environment variables** : Check all required variables are set



## Retrieve the Google SecOps service account

Google SecOps uses a unique service account to read data from your GCS bucket. You must grant this service account access to your bucket.

### Get the service account email

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Proofpoint Web Browser Isolation Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Proofpoint Web Browser Isolation** as the **Log type**.
  7. Click **Get Service Account**.
  8. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  9. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Don't use service accounts from other documentation or examples.
  10. Click **Next**.

  11. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://proofpoint-wbi-logs/wbi-logs/
           

       * Replace: 
         * `proofpoint-wbi-logs`: Your GCS bucket name.
         * `wbi-logs`: Optional prefix/folder path where logs are stored (leave empty for root).
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
  2. Click on your bucket name (for example, `proofpoint-wbi-logs`).
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
| metadata.event_type | Type of the event  
categories | metadata.product_event_type | Product-specific event type  
parentPageURL | metadata.url_back_to_product | URL linking back to the product  
region | principal.location.country_or_region | Country or region of the principal's location  
zone | principal.location.name | Name of the principal's location  
userId | principal.user.product_object_id | Product-specific identifier for the user  
userName | principal.user.userid | User identifier  
security_result | security_result | Security result details  
disposition | security_result.action | Security action taken  
disposition | security_result.action_details | Details of the security action  
classification | security_result.detection_fields | Detection-related fields  
url | target.url | URL of the target resource  
| metadata.product_name | Product name  
| metadata.vendor_name | Vendor name  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/proofpoint-web-browser-isolation-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
