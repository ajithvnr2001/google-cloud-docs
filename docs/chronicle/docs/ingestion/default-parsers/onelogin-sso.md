---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/onelogin-sso/
title: Collect OneLogin by One Identity logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:29:18.167391+00:00
---

# Collect OneLogin by One Identity logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/onelogin-sso/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect OneLogin by One Identity logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest OneLogin by One Identity logs to Google Security Operations using Google Cloud Storage V2.

OneLogin by One Identity is a cloud-based identity and access management (IAM) platform that provides single sign-on (SSO), multi-factor authentication (MFA), and user provisioning for enterprise applications. The OneLogin Events API provides programmatic access to event logs including user authentication, provisioning, policy changes, and administrative actions.

## Before you begin

Make sure that you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * Privileged access to the OneLogin Administration portal with Super Admin or equivalent role
  * API credentials (Client ID and Client Secret) configured in the OneLogin Administration portal



## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `onelogin-sso-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Collect OneLogin by One Identity API credentials

### Create API credentials

  1. Sign in to the [OneLogin Administration portal](https://app.onelogin.com/login).
  2. Go to **Developers > API Credentials**.
  3. Click **New Credential**.
  4. Enter a name for the credential (for example, `Google SecOps Integration`).
  5. Select **Read All** as the permissions scope.
  6. Click **Save**.

  7. Copy and save the following details in a secure location:

     * **Client ID** : The API client ID displayed on the credential page
     * **Client Secret** : The API client secret displayed on the credential page
**Note:** The client secret is displayed only once after creation. Store it securely. If lost, you will need to regenerate the credentials.



### Determine your OneLogin API region

The OneLogin API base URL depends on your data center region:

Region | API Base URL  
---|---  
US | `https://api.us.onelogin.com`  
EU | `https://api.eu.onelogin.com`  
**Note:** Check your OneLogin instance URL to determine your region. If your login URL contains `.eu.`, use the EU API base URL.

### Verify permissions

To verify the API credentials have the required permissions:

  1. Sign in to the OneLogin Administration portal.
  2. Go to **Developers > API Credentials**.
  3. Click on the credential name (for example, `Google SecOps Integration`).
  4. Confirm the **Read All** scope is selected. If not, update the scope and click **Save**.



### Test API access

  * Test your credentials before proceeding with the integration:
        
        # Replace with your actual credentials
        ONELOGIN_CLIENT_ID="your-client-id"
        ONELOGIN_CLIENT_SECRET="your-client-secret"
        ONELOGIN_API_BASE="[https://api.us.onelogin.com](https://api.us.onelogin.com)"
        
        # Get access token
        TOKEN=$(curl -s -X POST "${ONELOGIN_API_BASE}/auth/oauth2/v2/token" \
          -H "Content-Type: application/json" \
          -d "{\"grant_type\": \"client_credentials\", \"client_id\": \"${ONELOGIN_CLIENT_ID}\", \"client_secret\": \"${ONELOGIN_CLIENT_SECRET}\"}" \
          | jq -r '.access_token')
        
        # Test API access - list recent events
        curl -s -X GET "${ONELOGIN_API_BASE}/api/2/events?limit=1" \
          -H "Authorization: Bearer ${TOKEN}"
        




## Create service account for Cloud Run function

The Cloud Run function needs a service account with permissions to write to GCS bucket and be invoked by Pub/Sub.

### Create service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details:

     * **Service account name** : Enter `onelogin-sso-logs-collector-sa`
     * **Service account description** : Enter `Service account for Cloud Run function to collect OneLogin by One Identity logs`
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
  2. Click on your bucket name (for example, `onelogin-sso-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details:

     * **Add principals** : Enter the service account email (for example, `onelogin-sso-logs-collector-sa@PROJECT_ID.iam.gserviceaccount.com`)
     * **Assign roles** : Select **Storage Object Admin**
  6. Click **Save**.




## Create Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details:

     * **Topic ID** : Enter `onelogin-sso-logs-trigger`
     * Leave other settings as default
  4. Click **Create**.




## Create Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from the OneLogin Events API and write them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `onelogin-sso-logs-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose the topic `onelogin-sso-logs-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select the service account `onelogin-sso-logs-collector-sa`.
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `onelogin-sso-logs` | GCS bucket name  
`GCS_PREFIX` | `onelogin` | Prefix for log files  
`STATE_KEY` | `onelogin/state.json` | State file path  
`ONELOGIN_CLIENT_ID` | `your-client-id` | OneLogin API client ID  
`ONELOGIN_CLIENT_SECRET` | `your-client-secret` | OneLogin API client secret  
`ONELOGIN_API_BASE` | `https://api.us.onelogin.com` | OneLogin API base URL  
`MAX_RECORDS` | `5000` | Max records per run  
`PAGE_SIZE` | `250` | Records per page (max 250)  
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
    GCS_PREFIX = os.environ.get('GCS_PREFIX', 'onelogin')
    STATE_KEY = os.environ.get('STATE_KEY', 'onelogin/state.json')
    ONELOGIN_CLIENT_ID = os.environ.get('ONELOGIN_CLIENT_ID')
    ONELOGIN_CLIENT_SECRET = os.environ.get('ONELOGIN_CLIENT_SECRET')
    ONELOGIN_API_BASE = os.environ.get('ONELOGIN_API_BASE')
    MAX_RECORDS = int(os.environ.get('MAX_RECORDS', '5000'))
    PAGE_SIZE = int(os.environ.get('PAGE_SIZE', '250'))
    LOOKBACK_HOURS = int(os.environ.get('LOOKBACK_HOURS', '24'))
    
    def parse_datetime(value: str) -> datetime:
      """Parse ISO datetime string to datetime object."""
      if [value](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.ObjectCustomContextPayload.html#google_cloud_storage_blob_ObjectCustomContextPayload_value).endswith("Z"):
        value = value[:-1] + "+00:00"
      return datetime.fromisoformat(value)
    
    def get_access_token():
      """
      Obtain OAuth2 access token using client credentials grant.
      OneLogin uses /auth/oauth2/v2/token endpoint.
      """
      base_url = ONELOGIN_API_BASE.rstrip('/')
      token_url = f"{base_url}/auth/oauth2/v2/token"
    
      headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      }
    
      body = json.dumps({
        'grant_type': 'client_credentials',
        'client_id': ONELOGIN_CLIENT_ID,
        'client_secret': ONELOGIN_CLIENT_SECRET
      })
    
      backoff = 1.0
      for attempt in range(3):
        response = http.request('POST', token_url, body=body, headers=headers)
    
        if response.status == 429:
          retry_after = int(response.headers.get('Retry-After', str(int(backoff))))
          print(f"Rate limited (429) on token request. Retrying after {retry_after}s...")
          time.sleep(retry_after)
          backoff = min(backoff * 2, 30.0)
          continue
    
        if response.status != 200:
          raise RuntimeError(f"Failed to get access token: {response.status} - {response.data.decode('utf-8')}")
    
        data = json.loads(response.data.decode('utf-8'))
        return data['access_token']
    
      raise RuntimeError("Failed to get access token after 3 retries")
    
    @functions_framework.cloud_event
    def main(cloud_event):
      """
      Cloud Run function triggered by Pub/Sub to fetch OneLogin
      event logs and write to GCS.
    
      Args:
        cloud_event: CloudEvent object containing Pub/Sub message
      """
    
      if not all([GCS_BUCKET, ONELOGIN_CLIENT_ID, ONELOGIN_CLIENT_SECRET, ONELOGIN_API_BASE]):
        print('Error: Missing required environment variables')
        return
    
      try:
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
    
        # Get access token
        token = get_access_token()
    
        # Fetch events
        records, newest_event_time = fetch_logs(
          token=token,
          start_time=last_time,
          end_time=now,
          page_size=PAGE_SIZE,
          max_records=MAX_RECORDS,
        )
    
        if not records:
          print("No new log records found.")
          save_state(bucket, STATE_KEY, now.isoformat())
          return
    
        # Write to GCS as NDJSON
        timestamp = now.strftime('%Y%m%d_%H%M%S')
        object_key = f"{GCS_PREFIX}/logs_{timestamp}.ndjson"
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
    
    def fetch_logs(token: str, start_time: datetime, end_time: datetime, page_size: int, max_records: int):
      """
      Fetch event logs from the OneLogin Events API v2
      with cursor-based pagination and rate limiting.
    
      Args:
        token: OAuth2 access token
        start_time: Start time for log query
        end_time: End time for log query
        page_size: Number of records per page (max 250)
        max_records: Maximum total records to fetch
    
      Returns:
        Tuple of (records list, newest_event_time ISO string)
      """
      base_url = ONELOGIN_API_BASE.rstrip('/')
      endpoint = f"{base_url}/api/2/events"
    
      headers = {
        'Authorization': f'Bearer {token}',
        'Accept': 'application/json',
        'User-Agent': 'GoogleSecOps-OneLoginSSOCollector/1.0'
      }
    
      records = []
      newest_time = None
      page_num = 0
      backoff = 1.0
    
      start_iso = start_time.strftime('%Y-%m-%dT%H:%M:%SZ')
      end_iso = end_time.strftime('%Y-%m-%dT%H:%M:%SZ')
    
      cursor = None
    
      while True:
        page_num += 1
    
        if len(records) >= max_records:
          print(f"Reached max_records limit ({max_records})")
          break
    
        params = [
          f"limit={min(page_size, max_records - len(records))}",
          f"since={start_iso}",
          f"until={end_iso}"
        ]
        if cursor:
          params.append(f"cursor={cursor}")
    
        url = f"{endpoint}?{'&'.join(params)}"
    
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
            return records, newest_time
    
          data = json.loads(response.data.decode('utf-8'))
    
          page_results = data.get('data', [])
    
          if not page_results:
            print(f"No more results (empty page)")
            break
    
          print(f"Page {page_num}: Retrieved {len(page_results)} events")
          records.extend(page_results)
    
          # Track newest event time
          for event in page_results:
            try:
              event_time = event.get('created_at')
              if event_time:
                if newest_time is None or parse_datetime(event_time) > parse_datetime(newest_time):
                  newest_time = event_time
            except Exception as e:
              print(f"Warning: Could not parse event time: {e}")
    
          # Check for next page using cursor from pagination
          pagination = data.get('pagination', {})
          cursor = pagination.get('after_cursor')
          if not cursor:
            print("No more pages (no next cursor)")
            break
    
        except Exception as e:
          print(f"Error fetching logs: {e}")
          return records, newest_time
    
      print(f"Retrieved {len(records)} total records from {page_num} pages")
      return records, newest_time
    

**Note:** This script is provided as an example and is not officially supported. We welcome feedback about how we can improve it. To submit feedback, click **Send Feedback > Google SecOps Security Product Feedback** on this page.

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
**Name** | `onelogin-sso-logs-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the topic `onelogin-sso-logs-trigger`  
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
  5. Click on `onelogin-sso-logs-collector`.
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         Fetching logs from YYYY-MM-DDTHH:MM:SS+00:00 to YYYY-MM-DDTHH:MM:SS+00:00
         Page 1: Retrieved X events
         Wrote X records to gs://onelogin-sso-logs/onelogin/logs_YYYYMMDD_HHMMSS.ndjson
         Successfully processed X records
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click on your bucket name (`onelogin-sso-logs`).

  10. Navigate to the `onelogin/` folder.

  11. Verify that a new `.ndjson` file was created with the current timestamp.




If you see errors in the logs:

  * **HTTP 401** : Check API credentials in environment variables
  * **HTTP 403** : Verify API credentials have the Read All scope in the OneLogin Administration portal
  * **HTTP 429** : Rate limiting - function will automatically retry with backoff
  * **Missing environment variables** : Check all required variables are set



## Configure a feed in Google SecOps to ingest OneLogin by One Identity logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `OneLogin SSO Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **OneLogin** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address.

**Note:** Each Google SecOps instance has a unique service account. Do not use service accounts from other documentation or examples.
  9. Click **Next**.

  10. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://onelogin-sso-logs/onelogin/
           

       * Replace: 
         * `onelogin-sso-logs`: Your GCS bucket name.
         * `onelogin`: Optional prefix/folder path where logs are stored (leave empty for root).
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
  2. Click on your bucket name.
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
id | metadata.product_log_id | Directly mapped  
created_at | metadata.event_timestamp | Converted to timestamp  
account_id | principal.namespace | Directly mapped, converted to string  
actor_user_id | principal.user.userid | Directly mapped, converted to string  
actor_user_name | principal.user.user_display_name | Directly mapped  
user_id | target.user.userid | Directly mapped, converted to string  
user_name | target.user.user_display_name | Directly mapped  
event_type_id | metadata.product_event_type | Directly mapped, converted to string  
ipaddr | principal.ip | Directly mapped  
notes | metadata.description | Directly mapped  
app_id | target.application | Directly mapped, converted to string  
app_name | target.resource.name | Directly mapped  
group_id | target.group.product_object_id | Directly mapped, converted to string  
group_name | target.group.group_display_name | Directly mapped  
directory_id | additional.fields.value.string_value (key: directory_id) | Directly mapped  
role_id | principal.user.attribute.roles.id | Directly mapped, converted to string  
role_name | principal.user.attribute.roles.name | Directly mapped  
otp_device_id | additional.fields.value.string_value (key: otp_device_id) | Directly mapped  
otp_device_name | additional.fields.value.string_value (key: otp_device_name) | Directly mapped  
policy_id | security_result.rule_id | Directly mapped, converted to string  
policy_name | security_result.rule_name | Directly mapped  
client_id | additional.fields.value.string_value (key: client_id) | Directly mapped  
browser_fingerprint | additional.fields.value.string_value (key: browser_fingerprint) | Directly mapped  
custom_message | security_result.description | Directly mapped  
error_description | security_result.description | Directly mapped if custom_message is empty  
| metadata.vendor_name | Set to "OneLogin"  
| metadata.product_name | Set to "OneLogin SSO"  
| metadata.log_type | Set to "ONELOGIN_SSO"  
| metadata.event_type | Determined based on event_type_id: USER_LOGIN for authentication events, USER_RESOURCE_ACCESS for app access events, USER_CHANGE_PERMISSIONS for role/permission changes, GENERIC_EVENT otherwise  
`user_attributes.username` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`adc_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`adc_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`user_attributes.openid_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`user_attributes.samaccountname` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`user_attributes.member_of` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`user_attributes.group_id` | `event.idm.read_only_udm.target.group.product_object_id` | Mapped from changelog  
`user_attributes.lastname` | `principal.user.last_name` | Mapped from changelog  
`user_attributes.firstname` | `principal.user.first_name` | Mapped from changelog  
`user_attributes.department` | `principal.user.department` | Mapped from changelog  
`user_attributes.title` | `principal.user.title` | Mapped from changelog  
`user_attributes.email` | `principal.user.email_addresses` | Mapped from changelog  
`id` | `metadata.product_object_id` | Mapped from changelog  
`assuming_acting_user_id` | `additional.fields` | Mapped from changelog  
`directory_sync_run_id` | `additional.fields` | Mapped from changelog  
`resource_type_id` | `additional.fields` | Mapped from changelog  
`user_agent` | `network.http.parsed_user_agent` | Mapped from changelog  
`otp_device_id` | `principal.asset_id` | Mapped from changelog  
`actor_system` | `additional.fields` | Mapped from changelog  
`operation_name` | `additional.fields` | Mapped from changelog  
`resolution` | `additional.fields` | Mapped from changelog  
`risk_cookie_id` | `additional.fields` | Mapped from changelog  
`event_type_ids` | `additional.fields` | Mapped from changelog  
`since` | `additional.fields` | Mapped from changelog  
`until` | `additional.fields` | Mapped from changelog  
`proxy_ip` | `intermediary.ip` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/onelogin-sso-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
