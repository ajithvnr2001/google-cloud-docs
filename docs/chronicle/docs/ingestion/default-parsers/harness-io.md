---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/harness-io/
title: Collect Harness IO audit logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:38:08.165894+00:00
---

# Collect Harness IO audit logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/harness-io/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Harness IO audit logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Harness IO audit logs to Google Security Operations using Google Cloud Storage. Harness is a continuous delivery and DevOps platform that provides tools for software delivery, feature flags, cloud cost management, and security testing.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * Privileged access to Harness with permissions to: 
    * Create API keys
    * Access audit logs
    * View account settings



## Collect Harness API credentials

### Create API key in Harness

  1. Sign in to the **Harness Platform**.
  2. Click your **User Profile**.
  3. Go to **My API Keys**.
  4. Click **\+ API Key**.
  5. Provide the following configuration details: 
     * **Name** : Enter a descriptive name (for example, `Google SecOps Integration`).
     * **Description** : Optional description.
  6. Click **Save**.
  7. Click **\+ Token** to create a new token.
  8. Provide the following configuration details: 
     * **Name** : Enter `Chronicle Feed Token`.
     * **Set Expiration** : Select an appropriate expiration time or **No Expiration** (for production use).
  9. Click **Generate Token**.
  10. Copy and save the token value securely. This token will be used as the `x-api-key` header value.

**Note:** The token is displayed only once. If you lose it, you'll need to generate a new token.**Note:** The API token must have the `core_audit_view` permission to access audit logs. This permission is typically granted through role assignments in Harness.



### Get Harness Account ID

  1. In the **Harness Platform** , note the **Account ID** from the URL.



Example URL: `https://app.harness.io/ng/account/YOUR_ACCOUNT_ID/...`. The `YOUR_ACCOUNT_ID` part is your Account Identifier.

Alternatively, go to **Account Settings > Overview** to view your **Account Identifier**.

  1. Copy and save the Account ID for use in the Cloud Run function.

**Note:** The Account ID is required for all API requests to Harness.



## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `harness-io-logs`)  
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
     * **Service account name** : Enter `harness-audit-collector-sa`.
     * **Service account description** : Enter `Service account for Cloud Run function to collect Harness IO audit logs`.
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
     * **Add principals** : Enter the service account email (for example, `harness-audit-collector-sa@PROJECT_ID.iam.gserviceaccount.com`).
     * **Assign roles** : Select **Storage Object Admin**.
  6. Click **Save**.



## Create Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `harness-audit-trigger`.
     * Leave other settings as default.
  4. Click **Create**.



## Create Cloud Run function to collect logs

The Cloud Run function is triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from Harness API and writes them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `harness-audit-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose the Pub/Sub topic (`harness-audit-trigger`).
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub automatically handles authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select the service account (`harness-audit-collector-sa`).
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`HARNESS_ACCOUNT_ID` | Your Harness Account ID | Account identifier from Harness  
`HARNESS_API_KEY` | Your API key token | Token with audit:read permissions  
`GCS_BUCKET` | `harness-io-logs` | GCS bucket name  
`GCS_PREFIX` | `harness/audit` | Prefix for GCS objects  
`STATE_KEY` | `harness/audit/state.json` | State file path in GCS  
     * **Optional environment variables:**
Variable Name | Default Value | Description  
---|---|---  
`HARNESS_API_BASE` | `https://app.harness.io` | Harness API base URL (override for self-hosted instances)  
`PAGE_SIZE` | `50` | Events per page (max 100)  
`START_MINUTES_BACK` | `60` | Initial lookback period in minutes  
`FILTER_MODULES` | None | Comma-separated modules (e.g., `CD,CI,CE`)  
`FILTER_ACTIONS` | None | Comma-separated actions (e.g., `CREATE,UPDATE,DELETE`)  
`STATIC_FILTER` | None | Pre-defined filter: `EXCLUDE_LOGIN_EVENTS` or `EXCLUDE_SYSTEM_EVENTS`  
`MAX_RETRIES` | `3` | Max retry attempts for rate limiting  
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
    from datetime import datetime, timedelta, timezone
    import time
    
    # Initialize HTTP client
    http = urllib3.PoolManager()
    
    # Initialize Storage client
    storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    
    # Configuration from Environment Variables
    API_BASE = os.environ.get("HARNESS_API_BASE", "https://app.harness.io").rstrip("/")
    ACCOUNT_ID = os.environ["HARNESS_ACCOUNT_ID"]
    API_KEY = os.environ["HARNESS_API_KEY"]
    BUCKET = os.environ["GCS_BUCKET"]
    PREFIX = os.environ.get("GCS_PREFIX", "harness/audit").strip("/")
    STATE_KEY = os.environ.get("STATE_KEY", "harness/audit/state.json")
    PAGE_SIZE = min(int(os.environ.get("PAGE_SIZE", "50")), 100)
    START_MINUTES_BACK = int(os.environ.get("START_MINUTES_BACK", "60"))
    
    # Optional filters
    FILTER_MODULES = os.environ.get("FILTER_MODULES", "").split(",") if os.environ.get("FILTER_MODULES") else None
    FILTER_ACTIONS = os.environ.get("FILTER_ACTIONS", "").split(",") if os.environ.get("FILTER_ACTIONS") else None
    STATIC_FILTER = os.environ.get("STATIC_FILTER")
    MAX_RETRIES = int(os.environ.get("MAX_RETRIES", "3"))
    
    # HTTP headers for Harness API
    HDRS = {
        "x-api-key": API_KEY,
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    
    def read_state(bucket):
        """Read checkpoint state from GCS."""
        try:
            blob = bucket.blob(STATE_KEY)
            if blob.exists():
                state_data = blob.[download_as_text](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_download_as_text)()
                state = json.loads(state_data)
                since_ms = [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get("since")
                page_token = [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get("pageToken")
                print(f"State loaded: since={since_ms}, pageToken={page_token}")
                return since_ms, page_token
        except Exception as e:
            print(f"Warning: Could not load state: {e}")
    
        print("No state file found, starting fresh collection")
        start_time = datetime.now(timezone.utc) - timedelta(minutes=START_MINUTES_BACK)
        since_ms = int(start_time.timestamp() * 1000)
        print(f"Initial since timestamp: {since_ms} ({start_time.isoformat()})")
        return since_ms, None
    
    def write_state(bucket, since_ms, page_token=None):
        """Write checkpoint state to GCS."""
        state = {
            "since": since_ms,
            "pageToken": page_token,
            "lastRun": int(time.time() * 1000),
            "lastRunISO": datetime.now(timezone.utc).isoformat()
        }
        try:
            blob = bucket.blob(STATE_KEY)
            blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
                json.dumps(state, indent=2),
                content_type="application/json"
            )
            print(f"State saved: since={since_ms}, pageToken={page_token}")
        except Exception as e:
            print(f"Error writing state: {e}")
            raise
    
    def fetch_harness_audits(since_ms, page_token=None, retry_count=0):
        """
        Fetch audit logs from Harness API with retry logic.
        API Endpoint: POST /audit/api/audits/listV2
        """
        try:
            # Build URL with query parameters
            url = (
                f"{API_BASE}/audit/api/audits/listV2"
                f"?accountIdentifier={ACCOUNT_ID}"
                f"&pageSize={PAGE_SIZE}"
            )
            if page_token:
                url += f"&pageToken={page_token}"
    
            print(f"Fetching from: {url[:100]}...")
    
            # Build request body with time filter and optional filters
            body_data = {
                "startTime": since_ms,
                "endTime": int(time.time() * 1000),
                "filterType": "Audit"
            }
    
            if FILTER_MODULES:
                body_data["modules"] = [m.strip() for m in FILTER_MODULES if m.strip()]
                print(f"Applying module filter: {body_data['modules']}")
    
            if FILTER_ACTIONS:
                body_data["actions"] = [a.strip() for a in FILTER_ACTIONS if a.strip()]
                print(f"Applying action filter: {body_data['actions']}")
    
            if STATIC_FILTER:
                body_data["staticFilter"] = STATIC_FILTER
                print(f"Applying static filter: {STATIC_FILTER}")
    
            # Make POST request
            response = http.request(
                'POST',
                url,
                body=json.dumps(body_data).encode('utf-8'),
                headers=HDRS,
                timeout=30.0
            )
    
            resp_data = json.loads(response.data.decode('utf-8'))
    
            if "status" not in resp_data:
                print(f"Response missing 'status' field: {response.data[:200]}")
    
            # Check response status
            if resp_data.get("status") != "SUCCESS":
                error_msg = resp_data.get("message", "Unknown error")
                raise Exception(f"API returned status: {resp_data.get('status')} - {error_msg}")
    
            # Extract data from response structure
            data_obj = resp_data.get("data", {})
            if not data_obj:
                print("Response 'data' object is empty or missing")
    
            events = data_obj.get("content", [])
            has_next = data_obj.get("hasNext", False)
            next_token = data_obj.get("pageToken")
    
            print(f"API response: {len(events)} events, hasNext={has_next}, pageToken={next_token}")
    
            if not events and data_obj:
                print(f"Empty events but data present. Data keys: {list(data_obj.keys())}")
    
            return {
                "events": events,
                "hasNext": has_next,
                "pageToken": next_token
            }
    
        except Exception as e:
            if hasattr(e, 'status') and e.status == 429:
                retry_after = 60
                print(f"Rate limit exceeded. Retry after {retry_after} seconds (attempt {retry_count + 1}/{MAX_RETRIES})")
                if retry_count < MAX_RETRIES:
                    print(f"Waiting {retry_after} seconds before retry...")
                    time.sleep(retry_after)
                    print(f"Retrying request (attempt {retry_count + 2}/{MAX_RETRIES})")
                    return fetch_harness_audits(since_ms, page_token, retry_count + 1)
                else:
                    raise Exception(f"Max retries ({MAX_RETRIES}) exceeded for rate limiting")
            print(f"Error in fetch_harness_audits: {e}")
            raise
    
    def upload_to_gcs(bucket, events):
        """Upload audit events to GCS in JSONL format."""
        if not events:
            print("No events to upload")
            return None
    
        try:
            # Create JSONL content (one JSON object per line)
            jsonl_lines = [json.dumps(event) for event in events]
            jsonl_content = "\n".join(jsonl_lines)
    
            # Generate GCS key with timestamp
            timestamp = datetime.now(timezone.utc)
            key = (
                f"{PREFIX}/"
                f"{timestamp:%Y/%m/%d}/"
                f"harness-audit-{timestamp:%Y%m%d-%H%M%S}.jsonl"
            )
    
            # Upload to GCS
            blob = bucket.blob(key)
            blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
                jsonl_content,
                content_type="application/x-ndjson"
            )
            blob.[metadata](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_metadata) = {
                "event-count": str(len(events)),
                "source": "harness-audit-function",
                "collection-time": timestamp.isoformat()
            }
            blob.patch()
    
            print(f"Uploaded {len(events)} events to gs://{BUCKET}/{key}")
            return key
    
        except Exception as e:
            print(f"Error uploading to GCS: {e}")
            raise
    
    @functions_framework.cloud_event
    def main(cloud_event):
        """
        Cloud Run function triggered by Pub/Sub to fetch Harness audit logs and write to GCS.
    
        Args:
            cloud_event: CloudEvent object containing Pub/Sub message
        """
        print("=== Harness Audit Collection Started ===")
        print(f"Configuration: API_BASE={API_BASE}, ACCOUNT_ID={ACCOUNT_ID[:8]}..., PAGE_SIZE={PAGE_SIZE}")
    
        if FILTER_MODULES:
            print(f"Module filter enabled: {FILTER_MODULES}")
        if FILTER_ACTIONS:
            print(f"Action filter enabled: {FILTER_ACTIONS}")
        if STATIC_FILTER:
            print(f"Static filter enabled: {STATIC_FILTER}")
    
        try:
            # Get GCS bucket
            bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(BUCKET)
    
            # Step 1: Read checkpoint state
            since_ms, page_token = read_state(bucket)
    
            if page_token:
                print("Resuming pagination from saved pageToken")
            else:
                since_dt = datetime.fromtimestamp(since_ms / 1000, tz=timezone.utc)
                print(f"Starting new collection from: {since_dt.isoformat()}")
    
            # Step 2: Collect all events with pagination
            all_events = []
            current_page_token = page_token
            page_count = 0
            max_pages = 100
            has_next = True
    
            while has_next and page_count < max_pages:
                page_count += 1
                print(f"--- Fetching page {page_count} ---")
    
                # Fetch one page of results
                result = fetch_harness_audits(since_ms, current_page_token)
    
                # Extract events
                events = result.get("events", [])
                all_events.extend(events)
                print(f"Page {page_count}: {len(events)} events (total: {len(all_events)})")
    
                # Check pagination status
                has_next = result.get("hasNext", False)
                current_page_token = result.get("pageToken")
    
                if not has_next:
                    print("Pagination complete (hasNext=False)")
                    break
    
                if not current_page_token:
                    print("hasNext=True but no pageToken, stopping pagination")
                    break
    
                # Small delay between pages to avoid rate limiting
                time.sleep(0.5)
    
            if page_count >= max_pages:
                print(f"Reached max pages limit ({max_pages}), stopping")
    
            # Step 3: Upload collected events to GCS
            if all_events:
                gcs_key = upload_to_gcs(bucket, all_events)
                print(f"Successfully uploaded {len(all_events)} total events")
            else:
                print("No new events to upload")
                gcs_key = None
    
            # Step 4: Update checkpoint state
            if not has_next:
                # Pagination complete - update since to current time for next run
                new_since = int(time.time() * 1000)
                write_state(bucket, new_since, None)
                print(f"Pagination complete, state updated with new since={new_since}")
            else:
                # Pagination incomplete - save pageToken for continuation
                write_state(bucket, since_ms, current_page_token)
                print("Pagination incomplete, saved pageToken for next run")
    
            # Step 5: Log result
            result = {
                "status": "Success",
                "eventsCollected": len(all_events),
                "pagesProcessed": page_count,
                "paginationComplete": not has_next,
                "gcsKey": gcs_key,
                "filters": {
                    "modules": FILTER_MODULES,
                    "actions": FILTER_ACTIONS,
                    "staticFilter": STATIC_FILTER
                }
            }
            print(f"Collection completed: {json.dumps(result)}")
    
        except Exception as e:
            print(f"Collection failed: {e}")
            raise
        finally:
            print("=== Harness Audit Collection Finished ===")
    

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
**Name** | `harness-audit-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the Pub/Sub topic (`harness-audit-trigger`)  
**Message body** | `{}` (empty JSON object)  
  4. Click **Create**.




### Schedule frequency options

  * Choose frequency based on log volume and latency requirements:

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
  5. Click on your function name (`harness-audit-collector`).
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for the following:
         
         === Harness Audit Collection Started ===
         State loaded: since=... or No state file found, starting fresh collection
         --- Fetching page 1 ---
         API response: X events, hasNext=...
         Uploaded X events to gs://harness-io-logs/harness/audit/...
         Successfully processed X records
         === Harness Audit Collection Finished ===
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click your bucket name.

  10. Navigate to the prefix folder (`harness/audit/`).

  11. Verify that a new `.jsonl` file was created with the current timestamp.




If you see errors in the logs:

  * **HTTP 401** : Check API credentials in environment variables
  * **HTTP 403** : Verify account has required permissions
  * **HTTP 429** : Rate limiting - function will automatically retry with backoff
  * **Missing environment variables** : Check all required variables are set

**Note:** The Cloud Run function will now execute automatically every hour to collect new audit logs.



## Retrieve the Google SecOps service account

Google SecOps uses a unique service account to read data from your GCS bucket. You must grant this service account access to your bucket.

### Get the service account email

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Harness Audit Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Harness IO** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email is displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Do not use service accounts from other documentation or examples.



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



## Configure a feed in Google SecOps to ingest Harness IO logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Harness Audit Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Harness IO** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://harness-io-logs/harness/audit/
           

       * Replace:

         * `harness-io-logs`: Your GCS bucket name.
         * `harness/audit`: Prefix/folder path where logs are stored.
       * **Examples:**

         * Root bucket: `gs://company-logs/`
         * With prefix: `gs://company-logs/harness-logs/`
         * With subfolder: `gs://company-logs/harness/audit/`
**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never** : Never deletes any files after transfers (recommended for testing).
       * **Delete transferred files** : Deletes files after successful transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.

**Note:** If you select a deletion option, the service account must have **Storage Object Admin** role instead of Storage Object Viewer. Update IAM permissions accordingly.
     * **Maximum File Age** : Include files modified in the last number of days. Default is 180 days.

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces). Enter `harness.audit`.

     * **Ingestion labels** : The label to be applied to the events from this feed.

  9. Click **Next**.

  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/harness-io-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
