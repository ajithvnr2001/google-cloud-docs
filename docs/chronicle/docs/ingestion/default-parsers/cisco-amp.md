---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-amp/
title: Collect Cisco Secure Endpoint logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:52:22.770741+00:00
---

# Collect Cisco Secure Endpoint logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-amp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Cisco Secure Endpoint logs

**Parser Version:** 6.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Cisco Secure Endpoint logs to Google Security Operations using Google Cloud Storage. Cisco Secure Endpoint (formerly AMP for Endpoints) is a cloud-delivered endpoint security solution that provides advanced threat prevention, detection, and response across endpoints. The parser transforms raw JSON formatted logs into a structured format conforming to the UDM, extracts fields from nested JSON objects, maps them to the UDM schema, identifies event categories, assigns severity levels, and generates a unified event output, flagging security alerts when specific conditions are met.

## Before you begin

Make sure that you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * Privileged access to Cisco Secure Endpoint console with administrator permissions



## Collect Cisco Secure Endpoint API credentials

  1. Sign in to the **Cisco Secure Endpoint** console.
  2. Go to **Accounts > Organization Settings**.
  3. In the **Features** section, click **Configure API Credentials** to generate the Client ID and API Key.
  4. Click **New API Credential**.
  5. Provide the following configuration details: 
     * **Application Name** : Enter a name (for example, `Chronicle SecOps Integration`).
     * **Scope** : Select **Read-only** for basic event polling.
  6. Click **Create**.
  7. Copy and save in a secure location the following details:

     * **API Client ID**
     * **API Key**
**Note:** The API key is shown only once upon creation. Store it securely.
  8. Determine your **API Base URL** based on your region:

Region | API Base URL  
---|---  
North America | `https://api.amp.cisco.com`  
Europe | `https://api.eu.amp.cisco.com`  
Asia Pacific, Japan, and China | `https://api.apjc.amp.cisco.com`  



### Verify permissions

To verify the account has the required permissions:

  1. Sign in to the **Cisco Secure Endpoint** console.
  2. Go to **Accounts > Organization Settings**.
  3. If you can see the **Configure API Credentials** option under the **Features** section, you have the required permissions.
  4. If you cannot see this option, contact your administrator to grant administrator access permissions.



### Test API access

  * Test your credentials before proceeding with the integration:
        
        # Replace with your actual credentials
        AMP_CLIENT_ID="your-client-id"
        AMP_API_KEY="your-api-key"
        API_BASE="https://api.amp.cisco.com"
        
        # Test API access
        curl -v -u "${AMP_CLIENT_ID}:${AMP_API_KEY}" "${API_BASE}/v1/events?limit=1"
        




A successful response returns HTTP 200 with a JSON body containing an array of event objects.

## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `cisco-amp-logs`)  
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
     * **Service account name** : Enter `cisco-amp-collector-sa`.
     * **Service account description** : Enter `Service account for Cloud Run function to collect Cisco Secure Endpoint logs`.
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

Grant the service account (`cisco-amp-collector-sa`) write permissions on the GCS bucket:

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `cisco-amp-collector-sa@PROJECT_ID.iam.gserviceaccount.com`).
     * **Assign roles** : Select **Storage Object Admin**.
  6. Click **Save**.



## Create Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `cisco-amp-events-trigger`.
     * Leave other settings as default.
  4. Click **Create**.



## Create Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from Cisco Secure Endpoint API and write them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `cisco-amp-events-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose the Pub/Sub topic (`cisco-amp-events-trigger`).
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select the service account (`cisco-amp-collector-sa`).
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `cisco-amp-logs` | GCS bucket name  
`GCS_PREFIX` | `cisco-amp-events/` | Prefix for log files  
`STATE_KEY` | `cisco-amp-events/state.json` | State file path  
`API_BASE` | `https://api.amp.cisco.com` | API base URL  
`AMP_CLIENT_ID` | `your-client-id` | API client ID  
`AMP_API_KEY` | `your-api-key` | API key  
`PAGE_SIZE` | `500` | Records per page  
`MAX_PAGES` | `10` | Maximum pages to fetch  
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
    import base64
    
    # Initialize HTTP client with timeouts
    http = urllib3.PoolManager(
        timeout=urllib3.Timeout(connect=5.0, read=30.0),
        retries=False,
    )
    
    # Initialize Storage client
    storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    
    # Environment variables
    GCS_BUCKET = os.environ.get('GCS_BUCKET')
    GCS_PREFIX = os.environ.get('GCS_PREFIX', 'cisco-amp-events/')
    STATE_KEY = os.environ.get('STATE_KEY', 'cisco-amp-events/state.json')
    API_BASE = os.environ.get('API_BASE')
    AMP_CLIENT_ID = os.environ.get('AMP_CLIENT_ID')
    AMP_API_KEY = os.environ.get('AMP_API_KEY')
    PAGE_SIZE = int(os.environ.get('PAGE_SIZE', '500'))
    MAX_PAGES = int(os.environ.get('MAX_PAGES', '10'))
    
    def parse_datetime(value: str) -> datetime:
        """Parse ISO datetime string to datetime object."""
        if [value](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.ObjectCustomContextPayload.html#google_cloud_storage_blob_ObjectCustomContextPayload_value).endswith("Z"):
            value = value[:-1] + "+00:00"
        return datetime.fromisoformat(value)
    
    @functions_framework.cloud_event
    def main(cloud_event):
        """
        Cloud Run function triggered by Pub/Sub to fetch Cisco Secure Endpoint events and write to GCS.
    
        Args:
            cloud_event: CloudEvent object containing Pub/Sub message
        """
    
        if not all([GCS_BUCKET, API_BASE, AMP_CLIENT_ID, AMP_API_KEY]):
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
                last_time = now - timedelta(days=1)
    
            print(f"Fetching logs from {last_time.isoformat()} to {now.isoformat()}")
    
            # Fetch logs
            records, newest_event_time = fetch_logs(
                api_base=API_BASE,
                client_id=AMP_CLIENT_ID,
                api_key=AMP_API_KEY,
                start_time=last_time,
                page_size=PAGE_SIZE,
                max_pages=MAX_PAGES,
            )
    
            if not records:
                print("No new log records found.")
                save_state(bucket, STATE_KEY, now.isoformat())
                return
    
            # Write to GCS as NDJSON
            timestamp = now.strftime('%Y%m%d_%H%M%S')
            object_key = f"{GCS_PREFIX}cisco_amp_events_{timestamp}.ndjson"
            blob = bucket.blob(object_key)
    
            ndjson = '\n'.join([json.dumps(record, ensure_ascii=False) for record in records]) + '\n'
            blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(ndjson, content_type='application/x-ndjson')
    
            print(f"Wrote {len(records)} records to gs://{GCS_BUCKET}/{object_key}")
    
            # Update state with newest event time
            if newest_event_time:
                save_state(bucket, STATE_KEY, newest_event_time)
            else:
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
    
    def fetch_logs(api_base: str, client_id: str, api_key: str, start_time: datetime, page_size: int, max_pages: int):
        """
        Fetch logs from Cisco Secure Endpoint v1 API with pagination and rate limiting.
    
        Args:
            api_base: API base URL
            client_id: API client ID
            api_key: API key
            start_time: Start time for log query
            page_size: Number of records per page
            max_pages: Maximum total pages to fetch
    
        Returns:
            Tuple of (records list, newest_event_time ISO string)
        """
        # Clean up base URL
        base_url = api_base.rstrip('/')
    
        endpoint = f"{base_url}/v1/events"
    
        # Create Basic Auth header
        auth_string = f"{client_id}:{api_key}"
        auth_bytes = auth_string.encode('utf-8')
        auth_b64 = base64.b64encode(auth_bytes).decode('utf-8')
    
        headers = {
            'Authorization': f'Basic {auth_b64}',
            'Accept': 'application/json',
            'Accept-Encoding': 'gzip',
            'User-Agent': 'GoogleSecOps-CiscoAMPCollector/1.0'
        }
    
        records = []
        newest_time = None
        page_num = 0
        backoff = 1.0
    
        # Build initial URL with start_date parameter
        start_date_str = start_time.isoformat()
        if not start_date_str.endswith('Z'):
            start_date_str = start_date_str + 'Z' if start_date_str.endswith('+00:00') is False else start_date_str.replace('+00:00', 'Z')
        next_url = f"{endpoint}?limit={page_size}&start_date={start_date_str}"
    
        while next_url and page_num < max_pages:
            page_num += 1
    
            try:
                response = http.request('GET', next_url, headers=headers)
    
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
                    print(f"Response body: {response_text[:256]}")
                    return [], None
    
                data = json.loads(response.data.decode('utf-8'))
    
                # Extract events from response
                page_results = data.get('data', [])
    
                if not page_results:
                    print(f"No more results (empty page)")
                    break
    
                print(f"Page {page_num}: Retrieved {len(page_results)} events")
                records.extend(page_results)
    
                # Track newest event time
                for event in page_results:
                    try:
                        event_time = event.get('date')
                        if event_time:
                            if newest_time is None or parse_datetime(event_time) > parse_datetime(newest_time):
                                newest_time = event_time
                    except Exception as e:
                        print(f"Warning: Could not parse event time: {e}")
    
                # Check for next page URL in metadata
                next_url = data.get('metadata', {}).get('links', {}).get('next')
    
                if not next_url:
                    print("No more pages (no next URL)")
                    break
    
            except Exception as e:
                print(f"Error fetching logs: {e}")
                return [], None
    
        print(f"Retrieved {len(records)} total records from {page_num} pages")
        return records, newest_time
    

     * **requirements.txt:**
    
    functions-framework==3.*
    google-cloud-storage==2.*
    urllib3>=2.0.0
    

  3. Click **Deploy** to save and deploy the function.

  4. Wait for deployment to complete (2-3 minutes).

**Note:** The Pub/Sub trigger configuration automatically creates the necessary subscriptions and permissions. This script is provided as an example and is not officially supported. We welcome feedback about how we can improve it. To submit feedback, click Send Feedback > Google SecOps Security Product Feedback on this page.



## Create Cloud Scheduler job

Cloud Scheduler will publish messages to the Pub/Sub topic at regular intervals, triggering the Cloud Run function.

  1. In the **GCP Console** , go to **Cloud Scheduler**.
  2. Click **Create Job**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | `cisco-amp-events-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the Pub/Sub topic (`cisco-amp-events-trigger`)  
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
  5. Click on your function name (`cisco-amp-events-collector`).
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         Fetching logs from YYYY-MM-DDTHH:MM:SS+00:00 to YYYY-MM-DDTHH:MM:SS+00:00
         Page 1: Retrieved X events
         Wrote X records to gs://cisco-amp-logs/cisco-amp-events/cisco_amp_events_YYYYMMDD_HHMMSS.ndjson
         Successfully processed X records
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click your bucket name.

  10. Navigate to the prefix folder (`cisco-amp-events/`).

  11. Verify that a new `.ndjson` file was created with the current timestamp.




If you see errors in the logs:

  * **HTTP 401** : Check API credentials in environment variables
  * **HTTP 403** : Verify account has required permissions
  * **HTTP 429** : Rate limiting - function will automatically retry with backoff
  * **Missing environment variables** : Check all required variables are set



## Retrieve the Google SecOps service account

Google SecOps uses a unique service account to read data from your GCS bucket. You must grant this service account access to your bucket.

## Configure a feed in Google SecOps to ingest Cisco Secure Endpoint logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Cisco Secure Endpoint logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Cisco AMP** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address. You will use it in the next step.

**Note:** Each Google SecOps instance has a unique service account. Do not use service accounts from other documentation or examples.
  9. Click **Next**.

  10. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://cisco-amp-logs/cisco-amp-events/
           

       * Replace: 
         * `cisco-amp-logs`: Your GCS bucket name.
         * `cisco-amp-events/`: Prefix/folder path where logs are stored.
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
active | read_only_udm.principal.asset.active | The value of `computer.active` from the raw log is mapped to the `principal.asset.active` field.  
connector_guid | read_only_udm.principal.asset.uuid | The value of `computer.connector_guid` from the raw log is mapped to the `principal.asset.uuid` field.  
date | read_only_udm.metadata.event_timestamp.seconds | The value of `date` from the raw log is converted to a timestamp and mapped to the `metadata.event_timestamp.seconds` field.  
detection | read_only_udm.security_result.threat_name | The value of `detection` from the raw log is mapped to the `security_result.threat_name` field.  
detection_id | read_only_udm.security_result.detection_fields.value | The value of `detection_id` from the raw log is mapped to the `security_result.detection_fields` with key "Detection ID".  
error.error_code | read_only_udm.security_result.detection_fields.value | The value of `error.error_code` from the raw log is mapped to the `security_result.detection_fields` with key "Error Code".  
error.description | read_only_udm.security_result.detection_fields.value | The value of `error.description` from the raw log is mapped to the `security_result.detection_fields` with key "Error Description".  
event_type | read_only_udm.metadata.product_event_type | The value of `event_type` from the raw log is mapped to the `metadata.product_event_type` field.  
event_type_id | read_only_udm.metadata.product_log_id | The value of `event_type_id` from the raw log is mapped to the `metadata.product_log_id` field.  
external_ip | read_only_udm.principal.asset.external_ip | The value of `computer.external_ip` from the raw log is mapped to the `principal.asset.external_ip` field.  
file.disposition | read_only_udm.security_result.description | The value of `file.disposition` from the raw log is mapped to the `security_result.description` field.  
file.file_name | read_only_udm.target.file.names | The value of `file.file_name` from the raw log is mapped to the `target.file.names` field.  
file.file_path | read_only_udm.target.file.full_path | The value of `file.file_path` from the raw log is mapped to the `target.file.full_path` field.  
file.identity.md5 | read_only_udm.target.file.md5 | The value of `file.identity.md5` from the raw log is mapped to the `target.file.md5` field.  
file.identity.sha1 | read_only_udm.target.file.sha1 | The value of `file.identity.sha1` from the raw log is mapped to the `target.file.sha1` field.  
file.identity.sha256 | read_only_udm.target.file.sha256 | The value of `file.identity.sha256` from the raw log is mapped to the `target.file.sha256` field.  
file.parent.disposition | read_only_udm.target.resource.attribute.labels.value | The value of `file.parent.disposition` from the raw log is mapped to the `target.resource.attribute.labels` with key "Parent Disposition".  
file.parent.file_name | read_only_udm.target.resource.attribute.labels.value | The value of `file.parent.file_name` from the raw log is mapped to the `target.resource.attribute.labels` with key "Parent File Name".  
file.parent.identity.md5 | read_only_udm.target.resource.attribute.labels.value | The value of `file.parent.identity.md5` from the raw log is mapped to the `target.resource.attribute.labels` with key "Parent MD5".  
file.parent.identity.sha1 | read_only_udm.target.resource.attribute.labels.value | The value of `file.parent.identity.sha1` from the raw log is mapped to the `target.resource.attribute.labels` with key "Parent SHA1".  
file.parent.identity.sha256 | read_only_udm.target.resource.attribute.labels.value | The value of `file.parent.identity.sha256` from the raw log is mapped to the `target.resource.attribute.labels` with key "Parent SHA256".  
file.parent.process_id | read_only_udm.target.process.parent_process.pid | The value of `file.parent.process_id` from the raw log is mapped to the `target.process.parent_process.pid` field.  
hostname | read_only_udm.principal.asset.hostname | The value of `computer.hostname` from the raw log is mapped to the `principal.asset.hostname` field.  
ip | read_only_udm.principal.ip | The value of `computer.network_addresses.ip` from the raw log is mapped to the `principal.ip` field.  
mac | read_only_udm.principal.mac | The value of `computer.network_addresses.mac` from the raw log is mapped to the `principal.mac` field.  
severity | read_only_udm.security_result.severity | The value of `severity` from the raw log determines the value. If "Medium", set to "MEDIUM". If "High" or "Critical", set to "HIGH". If "Low", set to "LOW". Otherwise, set to "UNKNOWN_SEVERITY".  
timestamp | read_only_udm.metadata.event_timestamp.seconds | The value of `timestamp` from the raw log is converted to a timestamp and mapped to the `metadata.event_timestamp.seconds` field.  
user | read_only_udm.target.user.user_display_name | The value of `computer.user` from the raw log is mapped to the `target.user.user_display_name` field.  
vulnerabilities.cve | read_only_udm.extensions.vulns.vulnerabilities.cve_id | The value of `vulnerabilities.cve` from the raw log is mapped to the `extensions.vulns.vulnerabilities.cve_id` field.  
vulnerabilities.name | read_only_udm.extensions.vulns.vulnerabilities.name | The value of `vulnerabilities.name` from the raw log is mapped to the `extensions.vulns.vulnerabilities.name` field.  
vulnerabilities.score | read_only_udm.extensions.vulns.vulnerabilities.cvss_base_score | The value of `vulnerabilities.score` from the raw log is converted to a float and mapped to the `extensions.vulns.vulnerabilities.cvss_base_score` field.  
vulnerabilities.url | read_only_udm.extensions.vulns.vulnerabilities.vendor_knowledge_base_article_id | The value of `vulnerabilities.url` from the raw log is mapped to the `extensions.vulns.vulnerabilities.vendor_knowledge_base_article_id` field.  
vulnerabilities.version | read_only_udm.extensions.vulns.vulnerabilities.cvss_version | The value of `vulnerabilities.version` from the raw log is mapped to the `extensions.vulns.vulnerabilities.cvss_version` field.  
N/A | read_only_udm.metadata.event_type | Set to "SCAN_FILE" if event_type is one of: "Executed malware", "Threat Detected", "Potential Dropper Infection", "Cloud Recall Detection", "Malicious Activity Detection", "Exploit Prevention", "Multiple Infected Files", "Cloud IOC", "System Process Protection", "Vulnerable Application Detected", "Threat Quarantined", "Execution Blocked", "Cloud Recall Quarantine Successful", "Cloud Recall Restore from Quarantine Failed", "Cloud Recall Quarantine Attempt Failed", "Quarantine Failure", or if security_result.severity is "HIGH". Set to "SCAN_UNCATEGORIZED" if both has_principal and has_target are true. Otherwise, set to "GENERIC_EVENT".  
N/A | read_only_udm.metadata.log_type | Set to "CISCO_AMP".  
N/A | read_only_udm.metadata.vendor_name | Set to "CISCO_AMP".  
N/A | read_only_udm.security_result.summary | Set to event_type value if event_type is one of: "Threat Detected", "Exploit Prevention", "Executed malware", "Potential Dropper Infection", "Multiple Infected Files", "Vulnerable Application Detected", or if security_result.severity is "HIGH".  
N/A | is_alert | Set to true if event_type is one of: "Threat Detected", "Exploit Prevention", "Executed malware", "Potential Dropper Infection", "Multiple Infected Files", "Vulnerable Application Detected", or if security_result.severity is "HIGH".  
N/A | is_significant | Set to true if event_type is one of: "Threat Detected", "Exploit Prevention", "Executed malware", "Potential Dropper Infection", "Multiple Infected Files", "Vulnerable Application Detected", or if security_result.severity is "HIGH".  
`Compressed_sha256` | `additional.fields` | Mapped from changelog  
`analysis_action", "analysis_score", "analysis_status", "verdict_num", and "verdict_from` | `security_result.detection_fields` | Mapped from changelog  
`category` | `security_result.category_details` | Mapped from changelog  
`file_type` | `target.file.mime_type` | Mapped from changelog  
`upload_reason` | `metadata.description` | Mapped from changelog  
`active_connections","from","is_slow","instance_id","malwareverdict" and ,"verdict_str` | `additional.fields` | Mapped from changelog  
`Time` | `metadata.event_timestamp` | Mapped from changelog  
`file_extension` | `arget.resource.attribute.labels` | Mapped from changelog  
`filemime` | `target.file.mime_type` | Mapped from changelog  
`filename` | `target.file.full_path` | Mapped from changelog  
`host` | `principal.hostname` | Mapped from changelog  
`length_file` | `principal.resource.attribute.labels` | Mapped from changelog  
`uploadreason` | `security_result.description` | Mapped from changelog  
`ssl_bytes` | `network.sent_bytes` | Mapped from changelog  
`socket_bytes` | `network.received_bytes` | Mapped from changelog  
`file.disposition", "error.error_code", and "error.description` | `security_result.description` | Mapped from changelog  
`file.parent.disposition", "file.parent.file_name", "file.parent.identity.md5", "file.parent.identity.sha1", and "file.parent.identity.sha256` | `target.resource.attribute.labels` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-amp-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
