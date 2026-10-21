---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-ua/
title: Collect Cisco Umbrella Audit logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T07:22:04.023337+00:00
---

# Collect Cisco Umbrella Audit logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-ua/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Cisco Umbrella Audit logs

**Parser Version:** 3.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Cisco Umbrella Audit logs to Google Security Operations using Google Cloud Storage V2. Cisco Umbrella Audit logs capture administrative actions performed within the Cisco Umbrella dashboard, including policy changes, user management activities, and configuration modifications. These logs provide an audit trail for compliance and security monitoring of your Umbrella deployment.

## Before you begin

Make sure that you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * A Cisco Umbrella account with admin privileges
  * Cisco Umbrella API credentials (API key and secret) with `reports:read` scope



## Collect Cisco Umbrella API credentials

### Create an Umbrella API key

  1. Sign in to the [Cisco Umbrella dashboard](https://dashboard.umbrella.com).
  2. Go to **Admin > API Keys**.
  3. Click **Create API Key**.
  4. Provide the following configuration details: 
     * **Key Name** : Enter a descriptive name (for example, `Google SecOps Audit Log Integration`).
     * **Key Scope** : Select **Reports** with **Read-Only** access.
  5. Click **Create**.
  6. Copy and save the following values securely:

     * **API Key** : Copy this value.
     * **API Secret** : Copy this value.
**Note:** The API secret is only displayed once. Store it securely before closing the dialog.
  7. Note the **Organization ID** displayed at the top of the **API Keys** page. You will need this value later.




### Verify API access

The Cisco Umbrella API uses OAuth 2.0 authentication. Test your credentials before proceeding with the integration:

  1. Obtain an access token:
         
         API_KEY="<your-api-key>"
         API_SECRET="<your-api-secret>"
         
         TOKEN=$(curl -s -u "$API_KEY:$API_SECRET" \
           --url "https://api.umbrella.com/auth/v2/token" \
           -H "Content-Type: application/x-www-form-urlencoded" \
           -d "grant_type=client_credentials" | python3 -c "import sys,json; print(json.load(sys.stdin)['access_token'])")
         
         echo "$TOKEN"
         

  2. Use the token to retrieve audit logs:
         
         ORG_ID="<your-org-id>"
         
         curl -s -H "Authorization: Bearer $TOKEN" \
           "https://api.umbrella.com/reports/v2/audit?organizationId=$ORG_ID&limit=1"
         

**Note:** Access tokens expire after one hour. The Cloud Run function handles token renewal automatically.



## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `cisco-umbrella-audit-logs`)  
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
     * **Service account name** : Enter `umbrella-audit-collector-sa`
     * **Service account description** : Enter `Service account for Cloud Run function to collect Cisco Umbrella Audit logs`
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
  2. Click on your bucket name.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `umbrella-audit-collector-sa@PROJECT_ID.iam.gserviceaccount.com`)
     * **Assign roles** : Select **Storage Object Admin**
  6. Click **Save**.



## Create Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `umbrella-audit-trigger`
     * Leave other settings as default
  4. Click **Create**.



## Create Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from the Cisco Umbrella Audit API and write them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `umbrella-audit-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose the Pub/Sub topic `umbrella-audit-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select `umbrella-audit-collector-sa`
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `cisco-umbrella-audit-logs` | GCS bucket name  
`GCS_PREFIX` | `umbrella-audit` | Prefix for log files  
`STATE_KEY` | `umbrella-audit/state.json` | State file path  
`UMBRELLA_API_KEY` | `your-api-key` | Umbrella API key (OAuth 2.0 client ID)  
`UMBRELLA_API_SECRET` | `your-api-secret` | Umbrella API secret (OAuth 2.0 client secret)  
`UMBRELLA_ORG_ID` | `your-org-id` | Umbrella Organization ID  
`MAX_RECORDS` | `1000` | Max records per run  
`PAGE_SIZE` | `100` | Records per page  
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
    GCS_PREFIX = os.environ.get('GCS_PREFIX', 'umbrella-audit')
    STATE_KEY = os.environ.get('STATE_KEY', 'umbrella-audit/state.json')
    API_KEY = os.environ.get('UMBRELLA_API_KEY')
    API_SECRET = os.environ.get('UMBRELLA_API_SECRET')
    ORG_ID = os.environ.get('UMBRELLA_ORG_ID')
    MAX_RECORDS = int(os.environ.get('MAX_RECORDS', '1000'))
    PAGE_SIZE = int(os.environ.get('PAGE_SIZE', '100'))
    LOOKBACK_HOURS = int(os.environ.get('LOOKBACK_HOURS', '24'))
    
    # OAuth 2.0 token endpoint
    TOKEN_URL = 'https://api.umbrella.com/auth/v2/token'
    
    def parse_datetime(value: str) -> datetime:
      """Parse ISO datetime string to datetime object."""
      if [value](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.ObjectCustomContextPayload.html#google_cloud_storage_blob_ObjectCustomContextPayload_value).endswith("Z"):
        value = value[:-1] + "+00:00"
      return datetime.fromisoformat(value)
    
    def get_access_token(api_key, api_secret):
      """
      Obtain an OAuth 2.0 access token from the Cisco Umbrella API
      using the client credentials grant.
    
      Returns:
        Access token string
      """
      auth_string = f"{api_key}:{api_secret}"
      auth_bytes = auth_string.encode('utf-8')
      auth_b64 = base64.b64encode(auth_bytes).decode('utf-8')
    
      headers = {
        'Authorization': f'Basic {auth_b64}',
        'Content-Type': 'application/x-www-form-urlencoded',
      }
    
      response = http.request(
        'POST',
        TOKEN_URL,
        headers=headers,
        body='grant_type=client_credentials',
      )
    
      if response.status != 200:
        raise RuntimeError(
          f"Failed to obtain access token: HTTP {response.status} "
          f"- {response.data.decode('utf-8')}"
        )
    
      token_data = json.loads(response.data.decode('utf-8'))
      return token_data['access_token']
    
    @functions_framework.cloud_event
    def main(cloud_event):
      """
      Cloud Run function triggered by Pub/Sub to fetch Cisco Umbrella Audit logs
      and write to GCS.
    
      Args:
        cloud_event: CloudEvent object containing Pub/Sub message
      """
    
      if not all([GCS_BUCKET, API_KEY, API_SECRET, ORG_ID]):
        print('Error: Missing required environment variables')
        return
    
      try:
        bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(GCS_BUCKET)
        state = load_state(bucket, STATE_KEY)
    
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
    
        # Obtain OAuth 2.0 access token
        access_token = get_access_token(API_KEY, API_SECRET)
        print("Successfully obtained OAuth 2.0 access token")
    
        records, newest_event_time = fetch_logs(
          access_token=access_token,
          org_id=ORG_ID,
          start_time=last_time,
          end_time=now,
          page_size=PAGE_SIZE,
          max_records=MAX_RECORDS,
        )
    
        if not records:
          print("No new log records found.")
          save_state(bucket, STATE_KEY, now.isoformat())
          return
    
        timestamp = now.strftime('%Y%m%d_%H%M%S')
        object_key = f"{GCS_PREFIX}/logs_{timestamp}.ndjson"
        blob = bucket.blob(object_key)
    
        ndjson = '\n'.join(
          [json.dumps(record, ensure_ascii=False) for record in records]
        ) + '\n'
        blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(ndjson, content_type='application/x-ndjson')
    
        print(f"Wrote {len(records)} records to gs://{GCS_BUCKET}/{object_key}")
    
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
    
    def fetch_logs(access_token, org_id, start_time, end_time, page_size, max_records):
      """
      Fetch audit logs from Cisco Umbrella Reports API with pagination
      and rate limiting. Uses OAuth 2.0 bearer token authentication.
    
      Returns:
        Tuple of (records list, newest_event_time ISO string)
      """
      endpoint = f"https://api.umbrella.com/reports/v2/audit"
    
      headers = {
        'Authorization': f'Bearer {access_token}',
        'Accept': 'application/json',
        'User-Agent': 'GoogleSecOps-UmbrellaAuditCollector/1.0'
      }
    
      records = []
      newest_time = None
      page_num = 0
      offset = 0
      backoff = 1.0
    
      start_iso = start_time.strftime('%Y-%m-%dT%H:%M:%SZ')
      end_iso = end_time.strftime('%Y-%m-%dT%H:%M:%SZ')
    
      while True:
        page_num += 1
    
        if len(records) >= max_records:
          print(f"Reached max_records limit ({max_records})")
          break
    
        limit = min(page_size, max_records - len(records))
        url = (
          f"{endpoint}"
          f"?organizationId={org_id}"
          f"&from={start_iso}&to={end_iso}"
          f"&limit={limit}&offset={offset}"
        )
    
        try:
          response = http.request('GET', url, headers=headers)
    
          if response.status == 429:
            retry_after = int(
              response.headers.get('Retry-After', str(int(backoff)))
            )
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
          page_results = data if isinstance(data, list) else data.get('data', [])
    
          if not page_results:
            print("No more results (empty page)")
            break
    
          print(f"Page {page_num}: Retrieved {len(page_results)} events")
          records.extend(page_results)
    
          for event in page_results:
            try:
              event_time = event.get('createdAt')
              if event_time:
                if newest_time is None or parse_datetime(
                  event_time
                ) > parse_datetime(newest_time):
                  newest_time = event_time
            except Exception as e:
              print(f"Warning: Could not parse event time: {e}")
    
          if len(page_results) < limit:
            print(
              f"Reached last page (size={len(page_results)} < limit={limit})"
            )
            break
    
          offset += len(page_results)
    
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

**Note:** The Pub/Sub trigger configuration automatically creates the necessary subscriptions and permissions.



## Create Cloud Scheduler job

Cloud Scheduler will publish messages to the Pub/Sub topic at regular intervals, triggering the Cloud Run function.

  1. In the **GCP Console** , go to **Cloud Scheduler**.
  2. Click **Create Job**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | `umbrella-audit-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the Pub/Sub topic `umbrella-audit-trigger`  
**Message body** | `{}` (empty JSON object)  
  4. Click **Create**.




### Test the integration

  1. In the **Cloud Scheduler** console, find your job.
  2. Click **Force run** to trigger the job manually.
  3. Wait a few seconds.
  4. Go to **Cloud Run > Services**.
  5. Click on your function name (`umbrella-audit-collector`).
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         Fetching logs from YYYY-MM-DDTHH:MM:SS+00:00 to YYYY-MM-DDTHH:MM:SS+00:00
         Page 1: Retrieved X events
         Wrote X records to gs://cisco-umbrella-audit-logs/umbrella-audit/logs_YYYYMMDD_HHMMSS.ndjson
         Successfully processed X records
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click on your bucket name.

  10. Navigate to the `umbrella-audit/` folder.

  11. Verify that a new `.ndjson` file was created with the current timestamp.




If you see errors in the logs:

  * **HTTP 401** : Check API credentials in environment variables
  * **HTTP 403** : Verify the API key has Audit Logs read scope
  * **HTTP 429** : Rate limiting - function will automatically retry with backoff
  * **Missing environment variables** : Check all required variables are set



## Retrieve the Google SecOps service account

Google SecOps uses a unique service account to read data from your GCS bucket. You must grant this service account access to your bucket.

### Get the service account email

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Cisco Umbrella Audit Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Cisco Umbrella Audit** as the **Log type**.
  7. Click **Get Service Account**.
  8. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  9. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Do not use service accounts from other documentation or examples.
  10. Click **Next**.

  11. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://cisco-umbrella-audit-logs/umbrella-audit/
           

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
`_field` | `additional.fields` | Merged  
`identities_label` | `additional.fields` | Merged  
`key` | `additional.fields` | Mapped: ` "permissions", "dynamic", "bundleTypeId", "modifiedAt", "organizationId", "name", ...  
`column1` | `metadata.event_timestamp` | Parsed as `yyyy-MM-dd HH:mm:ss`  
`column2` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`createdAt` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`date_time` | `metadata.event_timestamp` | Parsed as `yyyy-MM-dd HH:mm:ss`  
`has_principal` | `metadata.event_type` | Mapped: `true` → `STATUS_UPDATE`  
`has_user` | `metadata.event_type` | Mapped: `true` → `USER_UNCATEGORIZED`  
`network_dns_details_present` | `metadata.event_type` | Mapped: `true` → `NETWORK_DNS`  
`product_log_id` | `metadata.product_log_id` | Directly mapped  
`network_dns_details_present` | `network.application_protocol` | Mapped: `true` → `DNS`  
`question` | `network.dns.questions` | Merged  
`dns.response_code` | `network.dns.response_code` | Renamed/mapped  
`mail_to` | `network.email.to` | Mapped: `^.+@.+$` → `mail_to`  
`action_type` | `network.http.method` | Directly mapped  
`identity` | `principal.asset.hostname` | Directly mapped  
`external_ip` | `principal.asset.ip` | Mapped: `internal_ip` → `external_ip`  
`internal_ip` | `principal.asset.ip` | Merged  
`ip` | `principal.asset.ip` | Merged  
`principal_ip` | `principal.asset.ip` | Merged  
`identity` | `principal.hostname` | Directly mapped  
`external_ip` | `principal.ip` | Mapped: `internal_ip` → `external_ip`  
`internal_ip` | `principal.ip` | Merged  
`ip` | `principal.ip` | Merged  
`principal_ip` | `principal.ip` | Merged  
`identity` | `principal.location.city` | Directly mapped  
`identity` | `principal.location.name` | Directly mapped  
`column5` | `principal.resource.name` | Directly mapped  
`id` | `principal.resource.product_object_id` | Directly mapped  
`email` | `principal.user.email_addresses` | Mapped: `^.+@.+$` → `email`  
`principal_user_email` | `principal.user.email_addresses` | Mapped: `^.+@.+$` → `principal_user_email`  
`user_mail` | `principal.user.email_addresses` | Mapped: `^.+@.+$` → `user_mail`  
`displayname` | `principal.user.user_display_name` | Directly mapped  
`principal_user` | `principal.user.user_display_name` | Directly mapped  
`user` | `principal.user.userid` | Directly mapped  
`security_result_action` | `security_result.action` | Merged  
`action` | `security_result.action_details` | Directly mapped  
`action_type` | `security_result.action_details` | Directly mapped  
`categories_json.categories` | `security_result.category_details` | Renamed/mapped  
`rule_name` | `security_result.rule_name` | Directly mapped  
N/A | `metadata.event_type` | Constant: `NETWORK_DNS`  
N/A | `metadata.product_name` | Constant: `CISCO UMBERLLA`  
N/A | `metadata.vendor_name` | Constant: `CISCO UMBERLLA`  
N/A | `network.application_protocol` | Constant: `DNS`  
`most_granular_identity", "most_granular_identity_type", "identity_types" and "blocked_categories` | `additional.fields` | Mapped from changelog  
`internal_ip" and "external_ip` | `principal.ip` | Mapped from changelog  
`dns_query_type` | `network.dns.questions.type` | Mapped from changelog  
`dns_response_code` | `network.dns.response_code` | Mapped from changelog  
`domain` | `network.dns.questions.name` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-umbrella-audit-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
