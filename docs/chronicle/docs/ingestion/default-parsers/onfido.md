---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/onfido/
title: Collect Entrust Identity Verification (formerly Onfido) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:11:40.207713+00:00
---

# Collect Entrust Identity Verification (formerly Onfido) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/onfido/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Entrust Identity Verification (formerly Onfido) logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Entrust Identity Verification (formerly known as Onfido) logs to Google Security Operations using Google Cloud Storage V2. The parser transforms raw Onfido verification check and report logs into the Google SecOps UDM schema.

Entrust Identity Verification is a cloud-based identity verification platform that automates document verification, biometric analysis, and fraud detection. It provides a REST API for managing applicants, verification checks, and reports, enabling organizations to integrate identity verification workflows into their applications.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * An Entrust Identity Verification (formerly Onfido) account with API access
  * An Onfido API token with sufficient permissions to read checks and reports



## Collect Onfido API credentials

### Get API token

  1. Sign in to the [Onfido Dashboard](https://dashboard.onfido.com/).
  2. Go to **Developers > API Tokens**.
  3. Copy an existing live API token, or click **Generate API token** to create a new one.
  4. Enter a name for the token (for example, `Google Security Operations Integration`).
  5. Select **Live** as the token type.
  6. Copy and save the API token securely.

**Note:** The API token is displayed only once. Store it in a secure location immediately after creation.



### Verify permissions

To verify the API token has the required permissions:

  1. Sign in to the [Onfido Dashboard](https://dashboard.onfido.com/).
  2. Go to **Developers > API Tokens**.
  3. Confirm the token is listed with **Live** status and is not revoked.
  4. Verify the token has read access to checks and reports by testing API access.



### Test API access

  * Test your credentials before proceeding with the integration:
        
        # Replace with your actual API token
        ONFIDO_API_TOKEN="your-api-token"
        
        # Test API access - list checks
        curl -v -H "Authorization: Token token=${ONFIDO_API_TOKEN}" \
          "[https://api.onfido.com/v3.6/checks](https://api.onfido.com/v3.6/checks)"
        




A successful response returns HTTP 200 with a JSON object containing a `checks` array.

## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.

  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `onfido-verification-logs`)  
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
     * **Service account name** : Enter `onfido-logs-collector-sa`.
     * **Service account description** : Enter `Service account for Cloud Run function to collect Onfido verification logs`.
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
     * **Add principals** : Enter the service account email (for example, `onfido-logs-collector-sa@PROJECT_ID.iam.gserviceaccount.com`).
     * **Assign roles** : Select **Storage Object Admin**.
  6. Click **Save**.



## Create Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `onfido-logs-trigger`.
     * Leave other settings as default.
  4. Click **Create**.



## Create Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch verification checks and reports from the Onfido API and write them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `onfido-logs-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose `onfido-logs-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select `onfido-logs-collector-sa`.
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `onfido-verification-logs` | GCS bucket name  
`GCS_PREFIX` | `onfido-logs` | Prefix for log files  
`STATE_KEY` | `onfido-logs/state.json` | State file path  
`ONFIDO_API_TOKEN` | `your-api-token-here` | Onfido API token  
`MAX_RECORDS` | `1000` | Max records per run  
`PAGE_SIZE` | `100` | Records per page  
`LOOKBACK_HOURS` | `24` | Initial lookback period  
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

  15. After the service is created, the **inline code editor** will open automatically.




### Add function code

  1. Enter **main** in **Function entry point**.
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
    
    # Environment variables
    GCS_BUCKET = os.environ.get('GCS_BUCKET')
    GCS_PREFIX = os.environ.get('GCS_PREFIX', 'onfido-logs')
    STATE_KEY = os.environ.get('STATE_KEY', 'onfido-logs/state.json')
    ONFIDO_API_TOKEN = os.environ.get('ONFIDO_API_TOKEN')
    MAX_RECORDS = int(os.environ.get('MAX_RECORDS', '1000'))
    PAGE_SIZE = int(os.environ.get('PAGE_SIZE', '100'))
    LOOKBACK_HOURS = int(os.environ.get('LOOKBACK_HOURS', '24'))
    
    API_BASE = '[https://api.onfido.com/v3.6](https://api.onfido.com/v3.6)'
    
    def parse_datetime(value: str) -> datetime:
        """Parse ISO datetime string to datetime object."""
        if [value](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.ObjectCustomContextPayload.html#google_cloud_storage_blob_ObjectCustomContextPayload_value).endswith("Z"):
            value = value[:-1] + "+00:00"
        return datetime.fromisoformat(value)
    
    @functions_framework.cloud_event
    def main(cloud_event):
        """
        Cloud Run function triggered by Pub/Sub to fetch Onfido verification
        checks and reports and write to GCS.
    
        Args:
            cloud_event: CloudEvent object containing Pub/Sub message
        """
    
        if not all([GCS_BUCKET, ONFIDO_API_TOKEN]):
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
                    # Overlap by 2 minutes to catch any delayed events
                    last_time = last_time - timedelta(minutes=2)
                except Exception as e:
                    print(f"Warning: Could not parse last_event_time: {e}")
    
            if last_time is None:
                last_time = now - timedelta(hours=LOOKBACK_HOURS)
    
            print(f"Fetching logs from {last_time.isoformat()} to {now.isoformat()}")
    
            # Fetch checks
            checks, newest_check_time = fetch_checks(
                api_token=ONFIDO_API_TOKEN,
                start_time=last_time,
                end_time=now,
                page_size=PAGE_SIZE,
                max_records=MAX_RECORDS,
            )
    
            # Fetch reports for each check
            all_records = []
            for check in checks:
                check_record = check.copy()
                check_id = check.get('id')
                if check_id:
                    reports = fetch_reports(api_token=ONFIDO_API_TOKEN, check_id=check_id)
                    check_record['reports'] = reports
                all_records.append(check_record)
    
            if not all_records:
                print("No new log records found.")
                save_state(bucket, STATE_KEY, now.isoformat())
                return
    
            # Write to GCS as NDJSON
            timestamp = now.strftime('%Y%m%d_%H%M%S')
            object_key = f"{GCS_PREFIX}/logs_{timestamp}.ndjson"
            blob = bucket.blob(object_key)
    
            ndjson = '\n'.join([json.dumps(record, ensure_ascii=False) for record in all_records]) + '\n'
            blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(ndjson, content_type='application/x-ndjson')
    
            print(f"Wrote {len(all_records)} records to gs://{GCS_BUCKET}/{object_key}")
    
            # Update state with newest event time
            if newest_check_time:
                save_state(bucket, STATE_KEY, newest_check_time)
            else:
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
    
    def fetch_checks(api_token: str, start_time: datetime, end_time: datetime, page_size: int, max_records: int):
        """
        Fetch verification checks from the Onfido API with pagination and rate limiting.
    
        Args:
            api_token: Onfido API token
            start_time: Start time for check query
            end_time: End time for check query
            page_size: Number of records per page
            max_records: Maximum total records to fetch
    
        Returns:
            Tuple of (checks list, newest_event_time ISO string)
        """
        headers = {
            'Authorization': f'Token token={api_token}',
            'Accept': 'application/json',
            'User-Agent': 'GoogleSecOps-OnfidoCollector/1.0'
        }
    
        records = []
        newest_time = None
        page_num = 0
        backoff = 1.0
        current_page = 1
    
        while True:
            page_num += 1
    
            if len(records) >= max_records:
                print(f"Reached max_records limit ({max_records})")
                break
    
            url = f"{API_BASE}/checks?page={current_page}&per_page={page_size}"
    
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
                    return [], None
    
                data = json.loads(response.data.decode('utf-8'))
    
                page_results = data.get('checks', [])
    
                if not page_results:
                    print(f"No more results (empty page)")
                    break
    
                # Filter checks within the time window
                filtered = []
                for check in page_results:
                    created_at = check.get('created_at')
                    if created_at:
                        try:
                            check_time = parse_datetime(created_at)
                            if start_time <= check_time <= end_time:
                                filtered.append(check)
                            if newest_time is None or check_time > parse_datetime(newest_time):
                                newest_time = created_at
                        except Exception as e:
                            print(f"Warning: Could not parse check time: {e}")
                            filtered.append(check)
    
                print(f"Page {page_num}: Retrieved {len(page_results)} checks, {len(filtered)} in time window")
                records.extend(filtered)
    
                # Check for more results
                if len(page_results) < page_size:
                    print(f"Reached last page (size={len(page_results)} < limit={page_size})")
                    break
    
                current_page += 1
    
            except Exception as e:
                print(f"Error fetching checks: {e}")
                return [], None
    
        print(f"Retrieved {len(records)} total checks from {page_num} pages")
        return records[:max_records], newest_time
    
    def fetch_reports(api_token: str, check_id: str):
        """
        Fetch reports for a specific check from the Onfido API.
    
        Args:
            api_token: Onfido API token
            check_id: Check ID to fetch reports for
    
        Returns:
            List of report objects
        """
        headers = {
            'Authorization': f'Token token={api_token}',
            'Accept': 'application/json',
            'User-Agent': 'GoogleSecOps-OnfidoCollector/1.0'
        }
    
        url = f"{API_BASE}/reports?check_id={check_id}"
    
        try:
            response = http.request('GET', url, headers=headers)
    
            if response.status == 429:
                time.sleep(2)
                response = http.request('GET', url, headers=headers)
    
            if response.status != 200:
                print(f"Error fetching reports for check {check_id}: HTTP {response.status}")
                return []
    
            data = json.loads(response.data.decode('utf-8'))
            reports = data.get('reports', [])
            return reports
    
        except Exception as e:
            print(f"Error fetching reports for check {check_id}: {e}")
            return []
    

     * Second file: **requirements.txt:**
    
    functions-framework==3.*
    google-cloud-storage==2.*
    urllib3>=2.0.0
    

**Note:** This script is provided as an example and is not officially supported. We welcome feedback about how we can improve it. To submit feedback, click **Send Feedback > Google SecOps Security Product Feedback** on this page.
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
**Name** | `onfido-logs-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select `onfido-logs-trigger`  
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
  5. Click on `onfido-logs-collector`.
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         Fetching logs from YYYY-MM-DDTHH:MM:SS+00:00 to YYYY-MM-DDTHH:MM:SS+00:00
         Page 1: Retrieved X checks, X in time window
         Wrote X records to gs://bucket-name/onfido-logs/logs_YYYYMMDD_HHMMSS.ndjson
         Successfully processed X records
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click your bucket name.

  10. Navigate to the `onfido-logs/` folder.

  11. Verify that a new `.ndjson` file was created with the current timestamp.




If you see errors in the logs:

  * **HTTP 401** : Check the Onfido API token in environment variables
  * **HTTP 403** : Verify the API token has live access and is not revoked
  * **HTTP 429** : Rate limiting - function will automatically retry with backoff
  * **Missing environment variables** : Check all required variables are set



## Configure a feed in Google SecOps to ingest Onfido logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Onfido Verification Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Onfido** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address. You will use it in the next step.

**Note:** Each Google SecOps instance has a unique service account. Do not use service accounts from other documentation or examples.
  9. Click **Next**.

  10. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://onfido-verification-logs/onfido-logs/
           

       * Replace: 
         * `onfido-verification-logs`: Your GCS bucket name.
         * `onfido-logs`: Optional prefix/folder path where logs are stored (leave empty for root).
**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never** : Never deletes any files after transfers (recommended for testing).
       * **Delete transferred files** : Deletes files after successful transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.
**Note:** If you select a deletion option, the service account must have **Storage Object Admin** role instead of Storage Object Viewer. Update IAM permissions accordingly.
     * **Maximum File Age** : Include files modified in the last number of days. Default is 180 days.

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
| read_only_udm.metadata.vendor_name | Set to "ONFIDO".  
| read_only_udm.metadata.product_name | Set to "ONFIDO".  
| read_only_udm.metadata.log_type | Set to "ONFIDO".  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/onfido-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
