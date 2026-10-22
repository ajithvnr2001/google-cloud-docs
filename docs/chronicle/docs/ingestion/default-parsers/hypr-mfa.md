---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/hypr-mfa/
title: Collect HYPR MFA logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:27:05.987938+00:00
---

# Collect HYPR MFA logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/hypr-mfa/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect HYPR MFA logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest HYPR MFA logs to Google Security Operations using webhooks or Google Cloud Storage V2.

HYPR MFA is a passwordless multi-factor authentication solution that provides phishing-resistant authentication using FIDO2 passkeys, biometrics, and mobile-initiated login. HYPR replaces traditional passwords with secure public key cryptography to eliminate credential-based attacks while streamlining user authentication across workstations, web applications, and cloud services.

## Before you begin

Ensure that you have the following prerequisites:

  * A Google SecOps instance
  * Administrative access to HYPR Control Center
  * Contact HYPR Support to enable Custom Event Hooks for the RP application you wish to monitor



## Collection method differences

HYPR MFA supports two methods for sending logs to Google Security Operations:

  * **Webhook (recommended)** : HYPR sends events in real-time to Google Security Operations via Custom Event Hooks. This method provides immediate event delivery and requires no additional infrastructure.
  * **Google Cloud Storage** : HYPR events are collected via API and stored in GCS, then ingested by Google Security Operations. This method provides batch processing and historical data retention.



Choose the method that best fits your requirements:

Feature | Webhook | Google Cloud Storage  
---|---|---  
**Latency** | Real-time (seconds) | Batch (minutes to hours)  
**Infrastructure** | None required | GCP project with Cloud Run function  
**Historical data** | Limited to event stream | Full retention in GCS  
**Setup complexity** | Simple | Moderate  
**Cost** | Minimal | GCP compute and storage costs  
  
## Option 1: Configure webhook integration

### Create webhook feed in Google SecOps

#### Create the feed

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `HYPR MFA Events`).
  5. Select **Webhook** as the **Source type**.
  6. Select **HYPR MFA** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters: 
     * **Split delimiter** (optional): Leave empty. Each webhook request contains a single JSON event.
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).
     * **Ingestion labels** : The label to be applied to the events from this feed.
  9. Click **Next**.
  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.



#### Generate and save secret key

After creating the feed, you must generate a secret key for authentication:

  1. On the feed details page, click **Generate Secret Key**.
  2. A dialog displays the secret key.
  3. **Copy and save** the secret key securely.

**Important:** The secret key is displayed only once and cannot be retrieved later. If you lose it, you must generate a new secret key.

#### Get the feed endpoint URL

  1. Go to the **Details** tab of the feed.
  2. In the **Endpoint Information** section, copy the **Feed endpoint URL**.
  3. The URL format is:
         
         https://{region}-chronicle.googleapis.com/v1/{parent}/logs:import
         

Where `{region}` is the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`), and `{parent}` is the resource path in the format `projects/<PROJECT_ID>/locations/<LOCATION>/instances/<INSTANCE_ID>/logTypes/<LOG_TYPE>`.

  4. Save this URL for the next steps.

  5. Click **Done**.




### Create Google Cloud API key

Chronicle requires an API key for authentication. Create a restricted API key in the Google Cloud Console.

#### Create the API key

  1. Go to the [Google Cloud Console Credentials page](https://console.cloud.google.com/apis/credentials).
  2. Select your project (the project associated with your Chronicle instance).
  3. Click **Create credentials > API key**.
  4. An API key is created and displayed in a dialog.
  5. Click **Edit API key** to restrict the key.



#### Restrict the API key

  1. In the **API key** settings page: 
     * **Name** : Enter a descriptive name (for example, `Chronicle Webhook API Key`).
  2. Under **API restrictions** : 
     1. Select **Restrict key**.
     2. In the **Select APIs** dropdown, search for and select **Google SecOps API** (or **Chronicle API**).
  3. Click **Save**.
  4. **Copy** the API key value from the **API key** field at the top of the page.
  5. Save the API key securely.

**Note:** Restricting the API key ensures it can only be used with the Chronicle API, reducing security risk if the key is compromised.

### Configure HYPR MFA Custom Event Hook

#### Construct the webhook URL with headers

HYPR supports custom headers for authentication. Use the headers authentication method for better security.

  * **Endpoint URL (without parameters):**
        
        <ENDPOINT_URL>
        

  * **Headers:**
        
        x-goog-chronicle-auth: <API_KEY>
        x-chronicle-auth: <SECRET_KEY>
        

    * Replace: 
      * `<ENDPOINT_URL>`: The feed endpoint URL from the previous step.
      * `<API_KEY>`: The Google Cloud API key you created.
      * `<SECRET_KEY>`: The secret key from Chronicle feed creation.



#### Prepare the Custom Event Hook JSON configuration

  * HYPR Custom Event Hooks are configured using JSON. Prepare the following JSON configuration, replacing the placeholder values:
        
        {
          "name": "Chronicle SIEM Integration",
          "eventType": "ALL",
          "invocationEndpoint": "<ENDPOINT_URL>",
          "httpMethod": "POST",
          "authType": "API_KEY",
          "authParams": {
            "apiKeyAuthParameters": {
              "apiKeyName": "x-goog-chronicle-auth",
              "apiKeyValue": "<API_KEY>"
            },
            "invocationHttpParameters": {
              "headerParameters": [
                {
                  "key": "Content-Type",
                  "value": "application/json",
                  "isValueSecret": false
                },
                {
                  "key": "x-chronicle-auth",
                  "value": "<SECRET_KEY>",
                  "isValueSecret": true
                }
              ]
            }
          }
        }
        

    * Replace:

      * `<ENDPOINT_URL>`: The Chronicle feed endpoint URL.
      * `<API_KEY>`: The Google Cloud API key.
      * `<SECRET_KEY>`: The Chronicle secret key.
    * **Configuration parameters:**

    * **name** : A descriptive name for the event hook (for example, `Chronicle SIEM Integration`).

    * **eventType** : Set to `ALL` to send all HYPR events, or specify specific event tags such as `AUTHENTICATION`, `REGISTRATION`, or `ACCESS_TOKEN`.

    * **invocationEndpoint** : The Chronicle feed endpoint URL.

    * **httpMethod** : Set to `POST`.

    * **authType** : Set to `API_KEY` for API key authentication.

    * **apiKeyName** : The header name for the API key (`x-goog-chronicle-auth`).

    * **apiKeyValue** : The Google Cloud API key value.

    * **headerParameters** : Additional headers including `Content-Type: application/json` and the Chronicle secret key in the `x-chronicle-auth` header.




#### Create the Custom Event Hook in HYPR Control Center

  1. Sign in to **HYPR Control Center** as an administrator.
  2. In the left navigation menu, click **Integrations**.
  3. On the **Integrations** page, click **Add New Integration**.
  4. HYPR Control Center displays available integrations.
  5. Click the tile under **Event Hooks** for **Custom Events**.
  6. Click **Add New Event Hook**.
  7. On the **Add New Event Hook** dialog, paste the JSON content you prepared into the text field.
  8. Click **Add Event Hook**.
  9. HYPR Control Center returns to the **Event Hooks** page.



The Custom Event Hook is now configured and will begin sending events to Google SecOps.

### Verify webhook is working

#### Check HYPR Control Center event hook status

  1. Sign in to **HYPR Control Center**.
  2. Go to **Integrations**.
  3. Click the **Custom Events** integration.
  4. In the **Event Hooks** table, verify that your event hook is listed.
  5. Click the event hook name to view details.
  6. Verify the configuration matches your settings.



#### Check Chronicle feed status

  1. Go to **SIEM Settings > Feeds** in Chronicle.
  2. Locate your webhook feed.
  3. Check the **Status** column (should be **Active**).
  4. Check **Events received** count (should be incrementing).
  5. Check **Last succeeded on** timestamp (should be recent).



#### Verify logs in Chronicle

  1. Go to **Search > UDM Search**.
  2. Use the following query:
         
         metadata.vendor_name = "HYPR" AND metadata.product_name = "MFA"
         

  3. Adjust time range to last 1 hour.

  4. Verify events appear in results.




### Authentication methods reference

HYPR Custom Event Hooks support multiple authentication methods. The recommended method for Chronicle is API key authentication with custom headers.

#### API Key Authentication (Recommended for Chronicle)

  * **Configuration:**
        
        {
          "authType": "API_KEY",
          "authParams": {
            "apiKeyAuthParameters": {
              "apiKeyName": "x-goog-chronicle-auth",
              "apiKeyValue": "<API_KEY>"
            },
            "invocationHttpParameters": {
              "headerParameters": [
                {
                  "key": "Content-Type",
                  "value": "application/json",
                  "isValueSecret": false
                },
                {
                  "key": "x-chronicle-auth",
                  "value": "<SECRET_KEY>",
                  "isValueSecret": true
                }
              ]
            }
          }
        }
        

  * **Advantages:**

    * API key and secret sent in headers (more secure than URL parameters).
    * Supports multiple authentication headers.
    * Headers not logged in web server access logs.



#### Basic Authentication

  * **Configuration:**
        
        {
          "authType": "BASIC",
          "authParams": {
            "basicAuthParameters": {
              "username": "your-username",
              "password": "your-password"
            },
            "invocationHttpParameters": {
              "headerParameters": [
                {
                  "key": "Content-Type",
                  "value": "application/json",
                  "isValueSecret": false
                }
              ]
            }
          }
        }
        

    * **Use case:** When the target system requires HTTP Basic Authentication.



#### OAuth 2.0 Client Credentials

  * **Configuration:**
        
        {
          "authType": "OAUTH_CLIENT_CREDENTIALS",
          "authParams": {
            "oauthParameters": {
              "clientParameters": {
                "clientId": "your-client-id",
                "clientSecret": "your-client-secret"
              },
              "authorizationEndpoint": "https://login.example.com/oauth2/v2.0/token",
              "httpMethod": "POST",
              "oauthHttpParameters": {
                "bodyParameters": [
                  {
                    "key": "scope",
                    "value": "api://your-api/.default",
                    "isValueSecret": false
                  },
                  {
                    "key": "grant_type",
                    "value": "client_credentials",
                    "isValueSecret": false
                  }
                ]
              }
            },
            "invocationHttpParameters": {
              "headerParameters": [
                {
                  "key": "Content-Type",
                  "value": "application/json",
                  "isValueSecret": false
                }
              ]
            }
          }
        }
        

    * **Use case:** When the target system requires OAuth 2.0 authentication.



### Event types and filtering

HYPR events are grouped using the `eventTags` parameter. You can configure the Custom Event Hook to send all events or filter by specific event types.

#### Event tags

  * **AUTHENTICATION** : User authentication events (login, unlock).
  * **REGISTRATION** : Device registration events (pairing mobile devices, security keys).
  * **ACCESS_TOKEN** : Access token generation and usage events.
  * **AUDIT** : Audit log events (administrative actions, configuration changes).



#### Configure event filtering

To send only specific event types, modify the `eventType` parameter in the JSON configuration:

  * **Send all events:**
        
        {
          "eventType": "ALL"
        }
        

  * **Send only authentication events:**
        
        {
          "eventType": "AUTHENTICATION"
        }
        

  * **Send only registration events:**
        
        {
          "eventType": "REGISTRATION"
        }
        


**Note:** For comprehensive security monitoring, it is recommended to use `"eventType": "ALL"` to capture all HYPR events.

## Option 2: Configure Google Cloud Storage integration

### Additional prerequisites for GCS integration

In addition to the prerequisites listed in the "Before you begin" section, you need:

  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * HYPR API credentials (contact HYPR Support for API access)



### Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `hypr-mfa-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




### Collect HYPR API credentials

Contact HYPR Support to obtain API credentials for accessing HYPR event data. You will need:

  * **API Base URL** : Your HYPR instance URL (for example, `https://your-tenant.hypr.com`)
  * **API Token** : Authentication token for API access
  * **RP App ID** : The Relying Party application ID to monitor

**Note:** HYPR API access requires special permissions. Contact HYPR Support to enable API access for your tenant.

### Create service account for Cloud Run function

The Cloud Run function needs a service account with permissions to write to GCS bucket and be invoked by Pub/Sub.

#### Create service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `hypr-logs-collector-sa`.
     * **Service account description** : Enter `Service account for Cloud Run function to collect HYPR MFA logs`.
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



#### Grant IAM permissions on GCS bucket

Grant the service account (`hypr-logs-collector-sa`) write permissions on the GCS bucket:

  1. Go to **Cloud Storage > Buckets**.
  2. Click on your bucket name (for example, `hypr-mfa-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `hypr-logs-collector-sa@PROJECT_ID.iam.gserviceaccount.com`).
     * **Assign roles** : Select **Storage Object Admin**.
  6. Click **Save**.



### Create Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `hypr-logs-trigger`.
     * Leave other settings as default.
  4. Click **Create**.



### Create Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from HYPR API and write them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `hypr-logs-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose the Pub/Sub topic (`hypr-logs-trigger`).
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select the service account (`hypr-logs-collector-sa`).
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `hypr-mfa-logs` | GCS bucket name  
`GCS_PREFIX` | `hypr-events` | Prefix for log files  
`STATE_KEY` | `hypr-events/state.json` | State file path  
`HYPR_API_URL` | `https://your-tenant.hypr.com` | HYPR API base URL  
`HYPR_API_TOKEN` | `your-api-token` | HYPR API authentication token  
`HYPR_RP_APP_ID` | `your-rp-app-id` | HYPR RP application ID  
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




#### Add function code

  1. Enter **main** in the **Entry point** field.
  2. In the inline code editor, create two files:

     * First file: **main.py:**
    
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
    GCS_PREFIX = os.environ.get('GCS_PREFIX', 'hypr-events')
    STATE_KEY = os.environ.get('STATE_KEY', 'hypr-events/state.json')
    HYPR_API_URL = os.environ.get('HYPR_API_URL')
    HYPR_API_TOKEN = os.environ.get('HYPR_API_TOKEN')
    HYPR_RP_APP_ID = os.environ.get('HYPR_RP_APP_ID')
    MAX_RECORDS = int(os.environ.get('MAX_RECORDS', '1000'))
    PAGE_SIZE = int(os.environ.get('PAGE_SIZE', '100'))
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
    
    @functions_framework.cloud_event
    def main(cloud_event):
        """
        Cloud Run function triggered by Pub/Sub to fetch HYPR MFA logs and write to GCS.
    
        Args:
            cloud_event: CloudEvent object containing Pub/Sub message
        """
    
        if not all([GCS_BUCKET, HYPR_API_URL, HYPR_API_TOKEN, HYPR_RP_APP_ID]):
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
    
            # Convert to Unix milliseconds for HYPR API
            start_millis = to_unix_millis(last_time)
            end_millis = to_unix_millis(now)
    
            # Fetch logs
            records, newest_event_time = fetch_logs(
                api_url=HYPR_API_URL,
                api_token=HYPR_API_TOKEN,
                rp_app_id=HYPR_RP_APP_ID,
                start_time_ms=start_millis,
                end_time_ms=end_millis,
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
    
    def fetch_logs(api_url: str, api_token: str, rp_app_id: str, start_time_ms: int, end_time_ms: int, page_size: int, max_records: int):
        """
        Fetch logs from HYPR API with pagination and rate limiting.
    
        Args:
            api_url: HYPR API base URL
            api_token: HYPR API authentication token
            rp_app_id: HYPR RP application ID
            start_time_ms: Start time in Unix milliseconds
            end_time_ms: End time in Unix milliseconds
            page_size: Number of records per page
            max_records: Maximum total records to fetch
    
        Returns:
            Tuple of (records list, newest_event_time ISO string)
        """
        # Clean up API URL
        base_url = api_url.rstrip('/')
    
        endpoint = f"{base_url}/rp/api/versioned/events"
    
        # Bearer token authentication
        headers = {
            'Authorization': f'Bearer {api_token}',
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'User-Agent': 'GoogleSecOps-HYPRCollector/1.0'
        }
    
        records = []
        newest_time = None
        page_num = 0
        backoff = 1.0
    
        # Offset-based pagination
        start_index = 0
    
        while True:
            page_num += 1
    
            if len(records) >= max_records:
                print(f"Reached max_records limit ({max_records})")
                break
    
            # Build request parameters
            params = []
            params.append(f"rpAppId={rp_app_id}")
            params.append(f"startDate={start_time_ms}")
            params.append(f"endDate={end_time_ms}")
            params.append(f"start={start_index}")
            params.append(f"limit={min(page_size, max_records - len(records))}")
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
                    return [], None
    
                data = json.loads(response.data.decode('utf-8'))
    
                # Extract results
                page_results = data.get('data', [])
    
                if not page_results:
                    print(f"No more results (empty page)")
                    break
    
                print(f"Page {page_num}: Retrieved {len(page_results)} events")
                records.extend(page_results)
    
                # Track newest event time
                for event in page_results:
                    try:
                        # HYPR uses LOGGEDTIMEINUTC field with Unix milliseconds
                        event_time_ms = event.get('LOGGEDTIMEINUTC')
                        if event_time_ms:
                            event_dt = datetime.fromtimestamp(event_time_ms / 1000, tz=timezone.utc)
                            event_time = event_dt.isoformat()
                            if newest_time is None or parse_datetime(event_time) > parse_datetime(newest_time):
                                newest_time = event_time
                    except Exception as e:
                        print(f"Warning: Could not parse event time: {e}")
    
                # Check for more results
                current_size = data.get('size', 0)
                if current_size < page_size:
                    print(f"Reached last page (size={current_size} < limit={page_size})")
                    break
    
                start_index += current_size
    
            except Exception as e:
                print(f"Error fetching logs: {e}")
                return [], None
    
        print(f"Retrieved {len(records)} total records from {page_num} pages")
        return records, newest_time
    

     * Second file: **requirements.txt:**
    
    functions-framework==3.*
    google-cloud-storage==2.*
    urllib3>=2.0.0
    

  3. Click **Deploy** to save and deploy the function.

  4. Wait for deployment to complete (2-3 minutes).

**Note:** The Pub/Sub trigger configuration automatically creates the necessary subscriptions and permissions.



### Create Cloud Scheduler job

Cloud Scheduler will publish messages to the Pub/Sub topic (`hypr-logs-trigger`) at regular intervals, triggering the Cloud Run function.

  1. In the **GCP Console** , go to **Cloud Scheduler**.
  2. Click **Create Job**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | `hypr-logs-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the Pub/Sub topic (`hypr-logs-trigger`)  
**Message body** | `{}` (empty JSON object)  
  4. Click **Create**.




#### Schedule frequency options

Choose frequency based on log volume and latency requirements:

Frequency | Cron Expression | Use Case  
---|---|---  
Every 5 minutes | `*/5 * * * *` | High-volume, low-latency  
Every 15 minutes | `*/15 * * * *` | Medium volume  
Every hour | `0 * * * *` | Standard (recommended)  
Every 6 hours | `0 */6 * * *` | Low volume, batch processing  
Daily | `0 0 * * *` | Historical data collection  
  
#### Test the integration

  1. In the **Cloud Scheduler** console, find your job (`hypr-logs-collector-hourly`).
  2. Click **Force run** to trigger the job manually.
  3. Wait a few seconds.
  4. Go to **Cloud Run > Services**.
  5. Click your function name (`hypr-logs-collector`).
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         Fetching logs from YYYY-MM-DDTHH:MM:SS+00:00 to YYYY-MM-DDTHH:MM:SS+00:00
         Page 1: Retrieved X events
         Wrote X records to gs://bucket-name/prefix/logs_YYYYMMDD_HHMMSS.ndjson
         Successfully processed X records
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click on your bucket name (for example, `hypr-mfa-logs`).

  10. Navigate to the prefix folder (for example, `hypr-events/`).

  11. Verify that a new `.ndjson` file was created with the current timestamp.




If you see errors in the logs:

  * **HTTP 401** : Check API credentials in environment variables
  * **HTTP 403** : Verify HYPR API token has required permissions and RP App ID is correct
  * **HTTP 429** : Rate limiting - function will automatically retry with backoff
  * **Missing environment variables** : Check all required variables are set



### Retrieve the Google SecOps service account

Google SecOps uses a unique service account to read data from your GCS bucket. You must grant this service account access to your bucket.

#### Configure a feed in Google SecOps to ingest HYPR MFA logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `HYPR MFA Logs from GCS`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **HYPR MFA** as the **Log type**.

  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Don't use service accounts from other documentation or examples.
  9. Click **Next**.

  10. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://hypr-mfa-logs/hypr-events/
           

       * Replace: 
         * `hypr-mfa-logs`: Your GCS bucket name.
         * `hypr-events`: Optional prefix/folder path where logs are stored (leave empty for root).
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




### Grant IAM permissions to the Google SecOps service account

The Google SecOps service account needs **Storage Object Viewer** role on your GCS bucket.

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name (for example, `hypr-mfa-logs`).
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
| extensions.auth.type | Authentication type (e.g., SSO, MFA)  
| metadata.event_type | Type of event (e.g., USER_LOGIN, NETWORK_CONNECTION)  
EVENTNAME | metadata.product_event_type | Product-specific event type  
ID | metadata.product_log_id | Product-specific log ID  
USERAGENT | network.http.parsed_user_agent | Parsed HTTP user agent  
USERAGENT | network.http.user_agent | HTTP user agent string  
SESSIONID | network.session_id | Session ID  
DEVICEMODEL | principal.asset.hardware.model | Hardware model of the asset  
COMPANION,MACHINEDOMAIN | principal.asset.hostname | Hostname of the asset  
REMOTEIP | principal.asset.ip | IP address of the asset  
DEVICEID | principal.asset_id | Unique identifier for the asset  
COMPANION,MACHINEDOMAIN | principal.hostname | Hostname associated with the principal  
REMOTEIP | principal.ip | IP address associated with the principal  
DEVICEOS | principal.platform | Platform (e.g., WINDOWS, LINUX)  
DEVICEOSVERSION | principal.platform_version | Version of the platform  
ISSUCCESSFUL | security_result.action | Action taken by the security system (e.g., ALLOW, BLOCK)  
MESSAGE | security_result.description | Description of the security result  
MACHINEUSERNAME | target.user.user_display_name | Display name of the user  
FIDOUSER | target.user.userid | User ID  
| metadata.product_name | Product name  
| metadata.vendor_name | Vendor/company name  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/hypr-mfa-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
