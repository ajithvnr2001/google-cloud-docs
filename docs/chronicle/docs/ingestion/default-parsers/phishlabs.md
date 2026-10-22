---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/phishlabs/
title: Collect PhishLabs logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:56:15.933454+00:00
---

# Collect PhishLabs logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/phishlabs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect PhishLabs logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest PhishLabs logs to Google Security Operations using Google Cloud Storage V2.

PhishLabs (now Fortra Brand Protection) is a digital risk protection platform for detecting and mitigating phishing, brand abuse, and social media threats. It provides incident data and indicators of compromise (IOCs) through its Incident Data API and IOC API. The parser extracts fields from PhishLabs event data and maps them to the Unified Data Model (UDM), capturing email metadata, security classifications, and threat intelligence details.

## Before you begin

Make sure that you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * Privileged access to PhishLabs with a valid API token for the Incident Data API and IOC API



## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `phishlabs-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Collect PhishLabs API credentials

### Obtain API token

  1. Sign in to the [PhishLabs portal](https://www.phishlabs.com/).
  2. Navigate to your account settings or contact your PhishLabs (Fortra) account representative to obtain an API token.
  3. Copy and securely store the API token (Bearer token).

**Note:** The API token provides access to both the Incident Data API and the IOC API. Store it securely and do not share it.



### Verify permissions

To verify the API token has the required permissions:

  1. Sign in to the PhishLabs portal.
  2. Navigate to your account settings.
  3. Confirm the API token is active and has access to the Incident Data API.
  4. If you cannot access the API settings, contact your PhishLabs account representative.



### Test API access

  * Test your credentials before proceeding with the integration:
        
        # Replace with your actual credentials
        API_TOKEN="<your-api-token>"
        
        # Test Incident Data API access
        curl -v -H "Authorization: Bearer ${API_TOKEN}" \
          "https://caseapi.phishlabs.com/idapi/v1/incidents?limit=5&offset=0"
        




## Create service account for Cloud Run function

The Cloud Run function needs a service account with permissions to write to GCS bucket and be invoked by Pub/Sub.

### Create service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `phishlabs-collector-sa`
     * **Service account description** : Enter `Service account for Cloud Run function to collect PhishLabs logs`
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
  2. Click on your bucket name (for example, `phishlabs-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `phishlabs-collector-sa@PROJECT_ID.iam.gserviceaccount.com`)
     * **Assign roles** : Select **Storage Object Admin**
  6. Click **Save**.



## Create Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `phishlabs-logs-trigger`
     * Leave other settings as default
  4. Click **Create**.



## Create Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch incident and IOC data from the PhishLabs APIs and write them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `phishlabs-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose the Pub/Sub topic (`phishlabs-logs-trigger`).
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select the service account (`phishlabs-collector-sa`)
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `phishlabs-logs` | GCS bucket name  
`GCS_PREFIX` | `phishlabs` | Prefix for log files  
`STATE_KEY` | `phishlabs/state.json` | State file path  
`API_TOKEN` | `your-bearer-token` | PhishLabs API Bearer token  
`COLLECT_IOCS` | `true` | Also collect IOC data (true/false)  
`MAX_RECORDS` | `1000` | Max records per run  
`PAGE_SIZE` | `50` | Records per page  
`LOOKBACK_HOURS` | `24` | Initial lookback period  
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
    GCS_PREFIX = os.environ.get('GCS_PREFIX', 'phishlabs')
    STATE_KEY = os.environ.get('STATE_KEY', 'phishlabs/state.json')
    API_TOKEN = os.environ.get('API_TOKEN')
    COLLECT_IOCS = os.environ.get('COLLECT_IOCS', 'true').lower() == 'true'
    MAX_RECORDS = int(os.environ.get('MAX_RECORDS', '1000'))
    PAGE_SIZE = int(os.environ.get('PAGE_SIZE', '50'))
    LOOKBACK_HOURS = int(os.environ.get('LOOKBACK_HOURS', '24'))
    
    INCIDENT_API_BASE = "https://caseapi.phishlabs.com/idapi/v1"
    IOC_API_BASE = "https://ioc.phishlabs.com/api/v1"
    
    def parse_datetime(value: str) -> datetime:
      """Parse ISO datetime string to datetime object."""
      if [value](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.ObjectCustomContextPayload.html#google_cloud_storage_blob_ObjectCustomContextPayload_value).endswith("Z"):
        value = value[:-1] + "+00:00"
      return datetime.fromisoformat(value)
    
    @functions_framework.cloud_event
    def main(cloud_event):
      """
      Cloud Run function triggered by Pub/Sub to fetch PhishLabs
      incident and IOC data and write to GCS.
    
      Args:
        cloud_event: CloudEvent object containing Pub/Sub message
      """
    
      if not all([GCS_BUCKET, API_TOKEN]):
        print('Error: Missing required environment variables')
        return
    
      try:
        # Get GCS bucket
        bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(GCS_BUCKET)
    
        # Load state
        state = load_state(bucket, STATE_KEY)
    
        # Determine time window
        now = datetime.now(timezone.utc)
        last_time = None
    
        if isinstance(state, dict) and [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get("last_event_time"):
          try:
            last_time = parse_datetime(state["last_event_time"])
            last_time = last_time - timedelta(minutes=2)
          except Exception as e:
            print(f"Warning: Could not parse last_event_time: {e}")
    
        if last_time is None:
          last_time = now - timedelta(hours=LOOKBACK_HOURS)
    
        print(f"Fetching logs from {last_time.isoformat()} to {now.isoformat()}")
    
        all_records = []
    
        # Fetch incidents from Incident Data API
        incidents, newest_incident_time = fetch_incidents(
          token=API_TOKEN,
          page_size=PAGE_SIZE,
          max_records=MAX_RECORDS,
        )
        if incidents:
          all_records.extend(incidents)
          print(f"Collected {len(incidents)} incidents")
    
        # Fetch IOCs if enabled
        if COLLECT_IOCS:
          lookback_seconds = int((now - last_time).total_seconds())
          iocs, newest_ioc_time = fetch_iocs(
            token=API_TOKEN,
            since_seconds=lookback_seconds,
          )
          if iocs:
            all_records.extend(iocs)
            print(f"Collected {len(iocs)} IOCs")
    
        if not all_records:
          print("No new records found.")
          save_state(bucket, STATE_KEY, now.isoformat())
          return
    
        # Write to GCS as NDJSON
        timestamp = now.strftime('%Y%m%d_%H%M%S')
        object_key = f"{GCS_PREFIX}/logs_{timestamp}.ndjson"
        blob = bucket.blob(object_key)
    
        ndjson = '\n'.join([json.dumps(record, ensure_ascii=False) for record in all_records]) + '\n'
        blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(ndjson, content_type='application/x-ndjson')
    
        print(f"Wrote {len(all_records)} records to gs://{GCS_BUCKET}/{object_key}")
    
        # Update state
        save_state(bucket, STATE_KEY, now.isoformat())
    
        print(f"Successfully processed {len(all_records)} records")
    
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
    
    def fetch_incidents(token: str, page_size: int, max_records: int):
      """
      Fetch incidents from the PhishLabs Incident Data API with pagination.
    
      Args:
        token: Bearer token for authentication
        page_size: Number of records per page
        max_records: Maximum total records to fetch
    
      Returns:
        Tuple of (records list, newest_event_time ISO string)
      """
      headers = {
        'Authorization': f'Bearer {token}',
        'Accept': 'application/json',
        'User-Agent': 'GoogleSecOps-PhishLabsCollector/1.0',
      }
    
      records = []
      newest_time = None
      page_num = 0
      backoff = 1.0
      offset = 0
    
      while True:
        page_num += 1
    
        if len(records) >= max_records:
          print(f"Reached max_records limit ({max_records})")
          break
    
        current_limit = min(page_size, max_records - len(records))
        url = f"{INCIDENT_API_BASE}/incidents?limit={current_limit}&offset={offset}"
    
        try:
          response = http.request('GET', url, headers=headers)
    
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
            return [], None
    
          data = json.loads(response.data.decode('utf-8'))
    
          if isinstance(data, list):
            page_results = data
          else:
            page_results = data.get('incidents', data.get('results', []))
    
          if not page_results:
            print(f"No more incident results (empty page)")
            break
    
          print(f"Incidents page {page_num}: Retrieved {len(page_results)} events")
          records.extend(page_results)
    
          # Track newest event time
          for event in page_results:
            try:
              event_time = event.get('createdAt') or event.get('dateCreated')
              if event_time:
                if newest_time is None or parse_datetime(event_time) > parse_datetime(newest_time):
                  newest_time = event_time
            except Exception as e:
              print(f"Warning: Could not parse event time: {e}")
    
          if len(page_results) < current_limit:
            print(f"Reached last page (size={len(page_results)} < limit={current_limit})")
            break
    
          offset += len(page_results)
    
        except Exception as e:
          print(f"Error fetching incidents: {e}")
          return [], None
    
      print(f"Retrieved {len(records)} total incidents from {page_num} pages")
      return records, newest_time
    
    def fetch_iocs(token: str, since_seconds: int):
      """
      Fetch IOCs from the PhishLabs IOC API.
    
      Args:
        token: Bearer token for authentication
        since_seconds: Fetch IOCs from the last N seconds
    
      Returns:
        Tuple of (records list, newest_event_time ISO string)
      """
      headers = {
        'Authorization': f'Bearer {token}',
        'Accept': 'application/json',
        'User-Agent': 'GoogleSecOps-PhishLabsCollector/1.0',
      }
    
      # Convert seconds to a relative time string
      since_hours = max(1, since_seconds // 3600)
      url = f"{IOC_API_BASE}/iocs?since={since_hours}h"
    
      try:
        response = http.request('GET', url, headers=headers)
    
        if response.status != 200:
          print(f"IOC API HTTP Error: {response.status}")
          return [], None
    
        data = json.loads(response.data.decode('utf-8'))
    
        if isinstance(data, list):
          iocs = data
        else:
          iocs = data.get('iocs', data.get('results', []))
    
        print(f"Retrieved {len(iocs)} IOCs")
        return iocs, None
    
      except Exception as e:
        print(f"Error fetching IOCs: {e}")
        return [], None
    

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
**Name** | `phishlabs-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the Pub/Sub topic (`phishlabs-logs-trigger`)  
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
  5. Click on your function name (`phishlabs-collector`).
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         Fetching logs from YYYY-MM-DDTHH:MM:SS+00:00 to YYYY-MM-DDTHH:MM:SS+00:00
         Incidents page 1: Retrieved X events
         Collected X incidents
         Retrieved X IOCs
         Wrote X records to gs://phishlabs-logs/phishlabs/logs_YYYYMMDD_HHMMSS.ndjson
         Successfully processed X records
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click on your bucket name (`phishlabs-logs`).

  10. Navigate to the prefix folder (`phishlabs/`).

  11. Verify that a new `.ndjson` file was created with the current timestamp.




If you see errors in the logs:

  * **HTTP 401** : Check the API token in environment variables
  * **HTTP 403** : Verify the API token has access to the Incident Data API and IOC API
  * **HTTP 429** : Rate limiting - function will automatically retry with backoff
  * **Missing environment variables** : Check all required variables are set



## Retrieve the Google SecOps service account

Google SecOps uses a unique service account to read data from your GCS bucket. You must grant this service account access to your bucket.

### Get the service account email

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `PhishLabs Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **PhishLabs** as the **Log type**.
  7. Click **Get Service Account**.
  8. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  9. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Don't use service accounts from other documentation or examples.
  10. Click **Next**.

  11. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://phishlabs-logs/phishlabs/
           

       * Replace: 
         * `phishlabs-logs`: Your GCS bucket name.
         * `phishlabs`: Optional prefix/folder path where logs are stored (leave empty for root).
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
  2. Click on your bucket name (for example, `phishlabs-logs`).
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
service, closed, status, details.emailReportedBy, details.emailReceivedDate, details.payloadFamily, details.offlineUponReview | additional.fields | Additional vendor-specific event data that cannot be adequately represented within the formal sections of the UDM model  
description | metadata.description | Description of the event  
| metadata.event_type | Type of event (e.g., USER_LOGIN, NETWORK_CONNECTION)  
id | metadata.product_log_id | Unique identifier for the log entry from the product  
sender_email | network.email.from | Sender email address  
details.messageID | network.email.mail_id | Unique identifier for the email message  
emailData.address | network.email.reply_to | Reply-to email address  
title | network.email.subject | Subject line of the email  
emailData.address | network.email.to | Recipient email addresses  
duration | network.session_duration.seconds | Duration of the session in seconds  
detailUrl.url | principal.process.file.embedded_urls | URLs embedded in files associated with the process  
src_email | principal.user.email_addresses | Email addresses associated with the user  
user_name | principal.user.user_display_name | Display name of the user  
details.classification, details.severity, details.furtherReviewReason, details.subClassification, details.caseType, details.emailBody, details.submissionMethod, detailUrl.url, detailUrl.malicious, detailUrl.maliciousDomain | security_result | Security classification or action made by a security product  
| metadata.product_name | Product name  
| metadata.vendor_name | Vendor name  
`details.urls.url", "details.urls.malicious", and "details.urls.maliciousDomain` | `security_result.detection_fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/phishlabs-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
