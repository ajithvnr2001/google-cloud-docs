---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/proofpoint-tap-forensics/
title: Collect Proofpoint TAP Forensics logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:49:16.521736+00:00
---

# Collect Proofpoint TAP Forensics logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/proofpoint-tap-forensics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Proofpoint TAP Forensics logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Proofpoint TAP Forensics logs to Google Security Operations using Google Cloud Storage V2.

Proofpoint Targeted Attack Protection (TAP) is an advanced email security platform that detects, analyzes, and blocks threats delivered through email, including malicious attachments and URLs. The TAP Forensics API provides detailed forensic evidence about individual threats and campaigns observed in your environment, including sandbox analysis results, behavioral indicators, network activity, file system changes, and process execution data. These forensic indicators can be used to confirm compromise on a host, enrich security intelligence sources, or orchestrate updates to security endpoints.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * A Proofpoint TAP subscription with access to the Threat Insight Dashboard
  * TAP API service credentials (Service Principal and Secret) with permissions to access the SIEM API and Forensics API



## Generate Proofpoint TAP API service credentials

  1. Sign in to the **Proofpoint TAP Threat Insight Dashboard**.
  2. Go to **Settings > Connected Applications > Service Credentials**.
  3. Click **Create New Credential**.
  4. In the **Generated Service Credential** dialog, copy and securely store:

     * **Service Principal** : The principal identifier used for API authentication
     * **Secret** : The secret key used for API authentication
**Note:** The Secret is displayed only once during creation. If lost, you must generate a new credential. Service credentials are required for all TAP API requests and use HTTP Basic Authentication.



### Verify API access

  * Test your credentials before proceeding with the integration:
        
        PRINCIPAL="your-service-principal"
        SECRET="your-secret"
        
        # Test SIEM API access (fetch last 5 minutes of events)
        curl -s "https://tap-api-v2.proofpoint.com/v2/siem/all?format=json&sinceSeconds=300" \
          --user "${PRINCIPAL}:${SECRET}"
        
        # Test Forensics API access (requires a valid threatId)
        # curl -s "https://tap-api-v2.proofpoint.com/v2/forensics?threatId=<threatId>" \
        #   --user "${PRINCIPAL}:${SECRET}"
        




A successful SIEM API response returns a JSON object containing `messagesBlocked`, `messagesDelivered`, `clicksBlocked`, and `clicksPermitted` arrays.

  * If you receive a `401` error, verify that your Service Principal and Secret are correct.
  * If you receive a `403` error, confirm that your account has TAP API access enabled.



## Create a Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `proofpoint-tap-forensics-logs`)  
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
     * **Service account name** : Enter `tap-forensics-collector-sa`
     * **Service account description** : Enter `Service account for Cloud Run function to collect Proofpoint TAP Forensics logs`
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

  * **Storage Object Admin** : Write forensic evidence data to GCS bucket and manage state files
  * **Cloud Run Invoker** : Allow Pub/Sub to invoke the function
  * **Cloud Functions Invoker** : Allow function invocation



### Grant IAM permissions on GCS bucket

Grant the service account write permissions on the GCS bucket:

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `tap-forensics-collector-sa@PROJECT_ID.iam.gserviceaccount.com`)
     * **Assign roles** : Select **Storage Object Admin**
  6. Click **Save**.



## Create a Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `tap-forensics-collector-trigger`
     * Leave other settings as default
  4. Click **Create**.



## Create a Cloud Run function to collect forensic evidence

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch threat events from the Proofpoint TAP SIEM API, retrieve forensic evidence for each unique threat using the Forensics API, and write the results to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `tap-forensics-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose the topic `tap-forensics-collector-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select the service account `tap-forensics-collector-sa`
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `proofpoint-tap-forensics-logs` | GCS bucket name  
`GCS_PREFIX` | `tap-forensics` | Prefix for log files  
`STATE_KEY` | `tap-forensics/state.json` | State file path  
`TAP_PRINCIPAL` | `your-service-principal` | TAP API Service Principal  
`TAP_SECRET` | `your-secret` | TAP API Secret  
`LOOKBACK_HOURS` | `1` | Initial lookback period in hours (max 7 days)  
`MAX_THREATS` | `500` | Max unique threats to fetch forensics for per run  
  10. Scroll down in the **Variables & Secrets** section to **Requests** :

     * **Request timeout** : Enter `540` seconds (9 minutes)
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
             timeout=urllib3.Timeout(connect=10.0, read=60.0),
             retries=False,
           )
           
           # Initialize Storage client
           storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
           
           # Environment variables
           GCS_BUCKET = os.environ.get('GCS_BUCKET')
           GCS_PREFIX = os.environ.get('GCS_PREFIX', 'tap-forensics').strip('/')
           STATE_KEY = os.environ.get('STATE_KEY') or f"{GCS_PREFIX}/state.json"
           TAP_PRINCIPAL = os.environ.get('TAP_PRINCIPAL')
           TAP_SECRET = os.environ.get('TAP_SECRET')
           LOOKBACK_HOURS = int(os.environ.get('LOOKBACK_HOURS', '1'))
           MAX_THREATS = int(os.environ.get('MAX_THREATS', '500'))
           
           API_BASE = 'https://tap-api-v2.proofpoint.com'
           
           def get_auth_header():
             """Build HTTP Basic Authentication header."""
             auth_string = f"{TAP_PRINCIPAL}:{TAP_SECRET}"
             auth_bytes = auth_string.encode('utf-8')
             auth_b64 = base64.b64encode(auth_bytes).decode('utf-8')
             return f"Basic {auth_b64}"
           
           @functions_framework.cloud_event
           def main(cloud_event):
             """
             Cloud Run function triggered by Pub/Sub to fetch Proofpoint TAP
             forensic evidence and write to GCS.
           
             The function first queries the SIEM API to discover threat IDs,
             then calls the Forensics API for each unique threat to retrieve
             detailed forensic evidence (sandbox results, behavioral
             indicators, network activity, file changes, and process data).
           
             Args:
               cloud_event: CloudEvent object containing Pub/Sub message
             """
           
             if not all([GCS_BUCKET, TAP_PRINCIPAL, TAP_SECRET]):
               print('Error: Missing required environment variables')
               return
           
             try:
               bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(GCS_BUCKET)
           
               # Load state
               state = load_state(bucket, STATE_KEY)
           
               # Determine time window
               now = datetime.now(timezone.utc)
               last_time = None
           
               if isinstance(state, dict) and [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get('last_event_time'):
                 try:
                   last_time = parse_datetime(state['last_event_time'])
                   # Overlap by 2 minutes to catch delayed events
                   last_time = last_time - timedelta(minutes=2)
                 except Exception as e:
                   print(f"Warning: Could not parse last_event_time: {e}")
           
               if last_time is None:
                 last_time = now - timedelta(hours=LOOKBACK_HOURS)
           
               # TAP SIEM API allows max 1 hour per request and max 7 days lookback
               if (now - last_time) > timedelta(days=7):
                 last_time = now - timedelta(days=7)
                 print("Warning: Lookback capped to 7 days (TAP API limit)")
           
               print(f"Fetching threats from {last_time.isoformat()} to {now.isoformat()}")
           
               # Step 1: Fetch threat IDs from the SIEM API
               threat_ids = fetch_threat_ids(last_time, now)
           
               if not threat_ids:
                 print("No threats found in the specified time window.")
                 save_state(bucket, STATE_KEY, now.isoformat())
                 return
           
               print(f"Found {len(threat_ids)} unique threat IDs")
           
               # Step 2: Fetch forensic evidence for each threat
               forensic_records = fetch_forensics_for_threats(threat_ids)
           
               if not forensic_records:
                 print("No forensic evidence retrieved.")
                 save_state(bucket, STATE_KEY, now.isoformat())
                 return
           
               # Write to GCS as NDJSON
               timestamp = now.strftime('%Y%m%d_%H%M%S')
               object_key = f"{GCS_PREFIX}/tap_forensics_{timestamp}.ndjson"
               blob = bucket.blob(object_key)
           
               ndjson = '\n'.join(
                 [json.dumps(record, ensure_ascii=False) for record in forensic_records]
               ) + '\n'
               blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(ndjson, content_type='application/x-ndjson')
           
               print(f"Wrote {len(forensic_records)} records to gs://{GCS_BUCKET}/{object_key}")
           
               # Update state
               save_state(bucket, STATE_KEY, now.isoformat())
           
               print(f"Successfully processed forensics for {len(threat_ids)} threats")
           
             except Exception as e:
               print(f'Error processing TAP forensics: {str(e)}')
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
           
           def save_state(bucket, key, last_event_time_iso):
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
           
           def parse_datetime(value):
             """Parse ISO datetime string to datetime object."""
             if [value](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.ObjectCustomContextPayload.html#google_cloud_storage_blob_ObjectCustomContextPayload_value).endswith('Z'):
               value = value[:-1] + '+00:00'
             return datetime.fromisoformat(value)
           
           def fetch_threat_ids(start_time, end_time):
             """
             Fetch unique threat IDs from the TAP SIEM API by querying
             in 1-hour intervals within the specified time window.
           
             Args:
               start_time: Start of the time window (datetime)
               end_time: End of the time window (datetime)
           
             Returns:
               Set of unique threat ID strings
             """
             headers = {
               'Authorization': get_auth_header(),
               'Accept': 'application/json',
               'User-Agent': 'GoogleSecOps-TAPForensicsCollector/1.0',
             }
           
             threat_ids = set()
             current_start = start_time
             backoff = 1.0
           
             while current_start < end_time:
               # TAP SIEM API allows max 1 hour per request
               current_end = min(current_start + timedelta(hours=1), end_time)
           
               interval = (
                 f"{current_start.strftime('%Y-%m-%dT%H:%M:%SZ')}"
                 f"/{current_end.strftime('%Y-%m-%dT%H:%M:%SZ')}"
               )
               url = f"{API_BASE}/v2/siem/all?format=json&interval={interval}"
           
               try:
                 response = http.request('GET', url, headers=headers)
           
                 if response.status == 429:
                   retry_after = int(
                     response.headers.get('Retry-After', str(int(backoff)))
                   )
                   print(f"Rate limited (429). Retrying after {retry_after}s...")
                   time.sleep(retry_after)
                   backoff = min(backoff * 2, 60.0)
                   continue
           
                 backoff = 1.0
           
                 if response.status != 200:
                   print(f"SIEM API HTTP Error: {response.status}")
                   response_text = response.data.decode('utf-8')
                   print(f"Response body: {response_text[:500]}")
                   current_start = current_end
                   continue
           
                 data = json.loads(response.data.decode('utf-8'))
           
                 # Extract threat IDs from all event types
                 for key in ['messagesBlocked', 'messagesDelivered']:
                   for msg in data.get(key, []):
                     for threat_info in msg.get('threatsInfoMap', []):
                       tid = threat_info.get('threatID')
                       if tid:
                         threat_ids.add(tid)
           
                 for key in ['clicksBlocked', 'clicksPermitted']:
                   for click in data.get(key, []):
                     tid = click.get('threatID')
                     if tid:
                       threat_ids.add(tid)
           
                 event_count = sum(
                   len(data.get(k, []))
                   for k in [
                     'messagesBlocked',
                     'messagesDelivered',
                     'clicksBlocked',
                     'clicksPermitted',
                   ]
                 )
                 print(
                   f"Interval {interval}: {event_count} events, "
                   f"{len(threat_ids)} unique threats so far"
                 )
           
               except Exception as e:
                 print(f"Error fetching SIEM events: {e}")
           
               current_start = current_end
           
               if len(threat_ids) >= MAX_THREATS:
                 print(f"Reached max threats limit ({MAX_THREATS})")
                 break
           
             return threat_ids
           
           def fetch_forensics_for_threats(threat_ids):
             """
             Fetch forensic evidence for each threat ID from the
             Forensics API.
           
             Args:
               threat_ids: Set of threat ID strings
           
             Returns:
               List of forensic report dictionaries
             """
             headers = {
               'Authorization': get_auth_header(),
               'Accept': 'application/json',
               'User-Agent': 'GoogleSecOps-TAPForensicsCollector/1.0',
             }
           
             records = []
             backoff = 1.0
             processed = 0
             skipped = 0
           
             for threat_id in list(threat_ids)[:MAX_THREATS]:
               url = (
                 f"{API_BASE}/v2/forensics"
                 f"?threatId={threat_id}"
                 f"&includeCampaignForensics=true"
               )
           
               try:
                 response = http.request('GET', url, headers=headers)
           
                 if response.status == 429:
                   retry_after = int(
                     response.headers.get('Retry-After', str(int(backoff)))
                   )
                   print(f"Rate limited (429). Retrying after {retry_after}s...")
                   time.sleep(retry_after)
                   backoff = min(backoff * 2, 60.0)
                   # Retry the same threat
                   continue
           
                 backoff = 1.0
           
                 if response.status == 204:
                   skipped += 1
                   processed += 1
                   continue
           
                 if response.status != 200:
                   print(
                     f"Forensics API error for {threat_id}: "
                     f"HTTP {response.status}"
                   )
                   skipped += 1
                   processed += 1
                   continue
           
                 data = json.loads(response.data.decode('utf-8'))
                 reports = data.get('reports', [])
           
                 if reports:
                   # Add the threat ID to each report for correlation
                   for report in reports:
                     report['_threatId'] = threat_id
                   records.extend(reports)
           
                 processed += 1
           
                 if processed % 50 == 0:
                   print(
                     f"Progress: {processed}/{len(threat_ids)} threats, "
                     f"{len(records)} forensic reports collected"
                   )
           
               except Exception as e:
                 print(f"Error fetching forensics for {threat_id}: {e}")
                 skipped += 1
                 processed += 1
           
             print(
               f"Forensics collection complete: {processed} threats processed, "
               f"{skipped} skipped, {len(records)} reports collected"
             )
             return records
           

     * Second file - **requirements.txt:**
           
           functions-framework==3.*
           google-cloud-storage==2.*
           urllib3>=2.0.0
           

  3. Click **Deploy** to save and deploy the function.

  4. Wait for deployment to complete (2-3 minutes).

**Note:** The function first queries the TAP SIEM API `/v2/siem/all` endpoint to discover threat IDs from recent email security events, then calls the Forensics API `/v2/forensics` for each unique threat to retrieve detailed forensic evidence including sandbox results, behavioral indicators, DNS queries, network connections, file modifications, and process activity. The SIEM API supports a maximum of 1 hour per request and 7 days of lookback. The function automatically splits larger time windows into 1-hour intervals.



## Create a Cloud Scheduler job

Cloud Scheduler will publish messages to the Pub/Sub topic at regular intervals, triggering the Cloud Run function.

  1. In the **GCP Console** , go to **Cloud Scheduler**.
  2. Click **Create Job**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | `tap-forensics-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the topic `tap-forensics-collector-trigger`  
**Message body** | `{}` (empty JSON object)  
  4. Click **Create**.




### Schedule frequency options

Choose frequency based on log volume and latency requirements:

Frequency | Cron Expression | Use Case  
---|---|---  
Every 15 minutes | `*/15 * * * *` | High-volume environments with many threats  
Every hour | `0 * * * *` | Standard (recommended)  
Every 6 hours | `0 */6 * * *` | Low-volume environments  
**Note:** The TAP SIEM API has a throttle limit of 1800 requests per 24 hours. An hourly schedule uses 24 requests per day, well within the limit. If you use a 15-minute schedule, ensure your total daily API calls remain within the throttle threshold.

### Test the integration

  1. In the **Cloud Scheduler** console, find your job.
  2. Click **Force run** to trigger the job manually.
  3. Wait a few seconds.
  4. Go to **Cloud Run > Services**.
  5. Click on the function name `tap-forensics-collector`.
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         Fetching threats from YYYY-MM-DDTHH:MM:SS+00:00 to YYYY-MM-DDTHH:MM:SS+00:00
         Interval .../...: X events, Y unique threats so far
         Found Z unique threat IDs
         Forensics collection complete: Z threats processed, 0 skipped, N reports collected
         Wrote N records to gs://proofpoint-tap-forensics-logs/tap-forensics/tap_forensics_YYYYMMDD_HHMMSS.ndjson
         Successfully processed forensics for Z threats
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click your bucket name.

  10. Navigate to the prefix folder `tap-forensics/`.

  11. Verify that a new `.ndjson` file was created with the current timestamp.




If you see errors in the logs:

  * **HTTP 401** : Check TAP_PRINCIPAL and TAP_SECRET in environment variables. Verify the Service Principal and Secret are correct.
  * **HTTP 403** : Confirm that your TAP account has API access enabled.
  * **HTTP 429** : Rate limiting - function will automatically retry with backoff. Consider reducing schedule frequency.
  * **No threats found** : This is normal if no threats were detected in the time window. TAP only reports threats identified by URL Defense or Attachment Defense.
  * **Missing environment variables** : Check all required variables are set.



## Configure a feed in Google SecOps to ingest Proofpoint TAP Forensics logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Proofpoint TAP Forensics`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Proofpoint Tap Forensics** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Don't use service accounts from other documentation or examples.
  9. Click **Next**.

  10. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://proofpoint-tap-forensics-logs/tap-forensics/
           

       * Replace: 
         * `proofpoint-tap-forensics-logs`: Your GCS bucket name.
         * `tap-forensics`: Optional prefix/folder path where logs are stored (leave empty for root).
**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never** : Never deletes any files after transfers (recommended for testing).
       * **Delete transferred files** : Deletes files after successful transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.
**Note:** If you select a deletion option, the service account must have **Storage Object Admin** role instead of Storage Object Viewer. Update IAM permissions accordingly.
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days)

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)

     * **Ingestion labels** : The label to be applied to the events from this feed

  11. Click **Next**.

  12. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## Grant IAM permissions to the Google SecOps service account

The Google SecOps service account needs **Storage Object Viewer** role on your GCS bucket.

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name.
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
`malicious_label` | `additional.fields` | Merged  
`threat_type_label` | `additional.fields` | Merged  
`generated` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`has_principal` | `metadata.event_type` | Mapped: `true` → `STATUS_UPDATE`  
`protocol` | `network.ip_protocol` | Directly mapped  
`prin_ip` | `principal.asset.ip` | Merged  
`domain` | `principal.domain.name` | Directly mapped  
`path` | `principal.file.full_path` | Directly mapped  
`file_hash_sha256` | `principal.file.sha256` | Directly mapped  
`prin_ip` | `principal.ip` | Merged  
`port` | `principal.port` | Directly mapped  
`url` | `principal.url` | Directly mapped  
`_security_result` | `security_result` | Merged  
N/A | `metadata.event_type` | Constant: `STATUS_UPDATE`  
N/A | `metadata.product_event_type` | Constant: `Forensic Reports`  
N/A | `metadata.product_name` | Constant: `TAP Forensics`  
N/A | `metadata.vendor_name` | Constant: `Proofpoint`  
N/A | `principal.asset.platform_software.platform` | Constant: `WINDOWS`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/proofpoint-tap-forensics-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
