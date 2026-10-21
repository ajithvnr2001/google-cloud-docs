---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/netdocuments/
title: Collect NetDocuments logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:48:56.799885+00:00
---

# Collect NetDocuments logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/netdocuments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect NetDocuments logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest NetDocuments logs to Google Security Operations using Google Cloud Storage V2.

NetDocuments is a cloud-based document management platform designed for legal and professional services organizations. It generates audit logs that track document access, modifications, sharing, and administrative activity through the NetDocuments REST API.

## Before you begin

Make sure that you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * Privileged access to NetDocuments (Repository Admin or Organization Admin role)
  * A NetDocuments application registration with OAuth2 credentials (client ID, client secret, and refresh token)



## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `netdocuments-audit-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Collect NetDocuments API credentials

### Register an application

  1. Sign in to the [NetDocuments Developer Portal](https://vault.netvoyage.com/neWeb2/developer.aspx) with an admin account.
  2. Navigate to **Applications** and click **Register Application**.
  3. Enter a name for the application (for example, `Google Security Operations Integration`).
  4. Set the **Application Type** to **Server (Confidential)**.
  5. Note the following credentials: 
     * **Client ID** : The OAuth2 client identifier
     * **Client Secret** : The OAuth2 client secret



### Generate refresh token

  1. Use the NetDocuments OAuth2 authorization flow to obtain a refresh token.
  2. Authorize the application with the required scopes: 
     * `read` (read access to documents and audit logs)
     * `full` (full access, if required by your organization)
  3. Complete the OAuth2 authorization code flow and save the **Refresh Token** securely.

**Note:** The refresh token is long-lived and used by the Cloud Run function to obtain short-lived access tokens. Store it securely as an environment variable.



### Determine API base URL

The NetDocuments API base URL depends on your data center region:

Region | API Base URL  
---|---  
US | `https://api.netdocuments.com/v2`  
EU | `https://api.eu.netdocuments.com/v2`  
AU | `https://api.au.netdocuments.com/v2`  
**Note:** Confirm your region from your NetDocuments account URL or contact your NetDocuments administrator.

### Verify permissions

To verify the account has the required permissions:

  1. Sign in to the **NetDocuments** admin portal.
  2. Go to **Repository Admin > Activity Logs**.
  3. If you can see the activity log section, you have the required permissions.
  4. If you cannot see this option, contact your NetDocuments administrator to grant Repository Admin or Organization Admin access.



## Create service account for Cloud Run function

The Cloud Run function needs a service account with permissions to write to GCS bucket and be invoked by Pub/Sub.

### Create service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `netdocuments-logs-collector-sa`
     * **Service account description** : Enter `Service account for Cloud Run function to collect NetDocuments logs`
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
  2. Click on your bucket name (for example, `netdocuments-audit-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `netdocuments-logs-collector-sa@PROJECT_ID.iam.gserviceaccount.com`)
     * **Assign roles** : Select **Storage Object Admin**
  6. Click **Save**.



## Create Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `netdocuments-logs-trigger`
     * Leave other settings as default
  4. Click **Create**.



## Create Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from the NetDocuments REST API and write them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `netdocuments-logs-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose the topic `netdocuments-logs-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select the service account `netdocuments-logs-collector-sa`.
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `netdocuments-audit-logs` | GCS bucket name  
`GCS_PREFIX` | `netdocuments` | Prefix for log files  
`STATE_KEY` | `netdocuments/state.json` | State file path  
`ND_API_BASE` | `https://api.netdocuments.com/v2` | NetDocuments API base URL  
`ND_CLIENT_ID` | `your-client-id` | OAuth2 client ID  
`ND_CLIENT_SECRET` | `your-client-secret` | OAuth2 client secret  
`ND_REFRESH_TOKEN` | `your-refresh-token` | OAuth2 refresh token  
`MAX_RECORDS` | `5000` | Max records per run  
`PAGE_SIZE` | `1000` | Records per page  
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
    GCS_PREFIX = os.environ.get('GCS_PREFIX', 'netdocuments')
    STATE_KEY = os.environ.get('STATE_KEY', 'netdocuments/state.json')
    ND_API_BASE = os.environ.get('ND_API_BASE', 'https://api.netdocuments.com/v2')
    ND_CLIENT_ID = os.environ.get('ND_CLIENT_ID')
    ND_CLIENT_SECRET = os.environ.get('ND_CLIENT_SECRET')
    ND_REFRESH_TOKEN = os.environ.get('ND_REFRESH_TOKEN')
    MAX_RECORDS = int(os.environ.get('MAX_RECORDS', '5000'))
    PAGE_SIZE = int(os.environ.get('PAGE_SIZE', '1000'))
    LOOKBACK_HOURS = int(os.environ.get('LOOKBACK_HOURS', '24'))
    
    def to_unix_millis(dt: datetime) -> int:
      """Convert datetime to Unix epoch milliseconds."""
      if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
      dt = dt.astimezone(timezone.utc)
      return int(dt.timestamp() * 1000)
    
    def parse_datetime(value: str) -> datetime:
      """Parse ISO datetime string to datetime object."""
      if [value](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.ObjectCustomContextPayload.html#google_cloud_storage_blob_ObjectCustomContextPayload_value).endswith("Z"):
        value = value[:-1] + "+00:00"
      return datetime.fromisoformat(value)
    
    def get_access_token():
      """
      Obtain an OAuth2 access token using the refresh token.
      """
      token_url = "https://api.netdocuments.com/v1/OAuth"
    
      # Build Basic auth header
      credentials = base64.b64encode(
        f"{ND_CLIENT_ID}:{ND_CLIENT_SECRET}".encode('utf-8')
      ).decode('utf-8')
    
      headers = {
        'Authorization': f'Basic {credentials}',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json'
      }
    
      body = f"grant_type=refresh_token&refresh_token={ND_REFRESH_TOKEN}"
    
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
      Cloud Run function triggered by Pub/Sub to fetch NetDocuments
      audit logs and write to GCS.
    
      Args:
        cloud_event: CloudEvent object containing Pub/Sub message
      """
    
      if not all([GCS_BUCKET, ND_CLIENT_ID, ND_CLIENT_SECRET, ND_REFRESH_TOKEN]):
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
    
        # Fetch logs
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
      Fetch audit logs from NetDocuments REST API
      with pagination and rate limiting.
    
      Args:
        token: OAuth2 access token
        start_time: Start time for log query
        end_time: End time for log query
        page_size: Number of records per page
        max_records: Maximum total records to fetch
    
      Returns:
        Tuple of (records list, newest_event_time ISO string)
      """
      api_base = ND_API_BASE.rstrip('/')
      endpoint = f"{api_base}/AuditLog/search"
    
      headers = {
        'Authorization': f'Bearer {token}',
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'User-Agent': 'GoogleSecOps-NetDocumentsCollector/1.0'
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
    
        # Build request body
        body = {
          'startDate': start_time.strftime('%Y-%m-%dT%H:%M:%SZ'),
          'endDate': end_time.strftime('%Y-%m-%dT%H:%M:%SZ'),
          '$top': min(page_size, max_records - len(records)),
          '$skip': offset
        }
    
        try:
          response = http.request(
            'POST',
            endpoint,
            body=json.dumps(body),
            headers=headers
          )
    
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
    
          page_results = data.get('results', data.get('value', []))
    
          if not page_results:
            print(f"No more results (empty page)")
            break
    
          print(f"Page {page_num}: Retrieved {len(page_results)} events")
          records.extend(page_results)
    
          # Track newest event time
          for event in page_results:
            try:
              event_ts = event.get('date') or event.get('timestamp') or event.get('created')
              if event_ts:
                event_time = str(event_ts)
                if newest_time is None or parse_datetime(event_time) > parse_datetime(newest_time):
                  newest_time = event_time
            except Exception as e:
              print(f"Warning: Could not parse event time: {e}")
    
          # Check for more results
          offset += len(page_results)
          if len(page_results) < page_size:
            print("No more pages (partial page received)")
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

**Note:** The Pub/Sub trigger configuration automatically creates the necessary subscriptions and permissions.



## Create Cloud Scheduler job

Cloud Scheduler will publish messages to the Pub/Sub topic at regular intervals, triggering the Cloud Run function.

  1. In the **GCP Console** , go to **Cloud Scheduler**.
  2. Click **Create Job**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | `netdocuments-logs-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the topic `netdocuments-logs-trigger`  
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
  5. Click on `netdocuments-logs-collector`.
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         Fetching logs from YYYY-MM-DDTHH:MM:SS+00:00 to YYYY-MM-DDTHH:MM:SS+00:00
         Page 1: Retrieved X events
         Wrote X records to gs://netdocuments-audit-logs/netdocuments/logs_YYYYMMDD_HHMMSS.ndjson
         Successfully processed X records
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click on your bucket name (`netdocuments-audit-logs`).

  10. Navigate to the `netdocuments/` folder.

  11. Verify that a new `.ndjson` file was created with the current timestamp.




If you see errors in the logs:

  * **HTTP 401** : Check OAuth2 credentials in environment variables
  * **HTTP 403** : Verify account has required Repository Admin or Organization Admin permissions
  * **HTTP 429** : Rate limiting - function will automatically retry with backoff
  * **Missing environment variables** : Check all required variables are set



## Configure a feed in Google SecOps to ingest NetDocuments logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `NetDocuments Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **NetDocuments** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address.

**Note:** Each Google SecOps instance has a unique service account. Do not use service accounts from other documentation or examples.
  9. Click **Next**.

  10. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://netdocuments-audit-logs/netdocuments/
           

       * Replace: 
         * `netdocuments-audit-logs`: Your GCS bucket name.
         * `netdocuments`: Optional prefix/folder path where logs are stored (leave empty for root).
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
description, name | metadata.description | A human-readable description of the event.  
date | metadata.event_timestamp | The time when the event occurred.  
| metadata.event_type | The type of event.  
source.id | principal.asset.hostname | The hostname of the asset associated with the principal.  
host | principal.asset.ip | The IP address of the asset associated with the principal.  
source.id | principal.hostname | The hostname associated with the principal.  
host | principal.ip | The IP address associated with the principal.  
source.name | principal.resource.attribute.labels | A map of labels for the principal's resource.  
user.email | principal.user.email_addresses | The email addresses associated with the user.  
user.memberType | principal.user.role_name | The role name of the user.  
user.name | principal.user.user_display_name | The display name of the user.  
user.id | principal.user.userid | The user ID of the principal.  
storageObject.fileExtension | target.file.mime_type | The MIME type of the target file.  
storageObject.name | target.file.names | The names of the target files.  
storageObject.size | target.file.size | The size of the target file in bytes.  
storageObject.version, storageObject.collabSpace, storageObject.NetBinder, storageObject.cabinet.name, storageObject.cabinet.id | target.resource.attribute.labels | A map of labels for the target resource.  
storageObject.docId | target.resource.product_object_id | The product-specific object ID of the target resource.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/netdocuments-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
