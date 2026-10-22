---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zendesk-crm/
title: Collect Zendesk CRM logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:55:50.093053+00:00
---

# Collect Zendesk CRM logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zendesk-crm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Zendesk CRM logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Zendesk Customer Relationship Management (CRM) logs to Google Security Operations using Google Cloud Storage. Zendesk CRM provides customer support and ticketing management capabilities. The platform tracks customer interactions, support tickets, and administrative activities through audit logs and ticket data.

## Before you begin

Ensure that you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run functions, Pub/Sub topics, and Cloud Scheduler jobs
  * Privileged access to Zendesk (Admin role required for API token creation)
  * Zendesk Enterprise plan (required for Audit Logs API access)



## Get Zendesk prerequisites

### Confirm plan and role

You must be a Zendesk Admin to create API tokens or OAuth clients. The Audit Logs API is available only on Enterprise plan and returns a maximum of 100 records per page. If your account isn't Enterprise, you can still collect incremental tickets data.

### Turn on API token access (one-time)

  1. In the **Admin Center** , go to **Apps and integrations > APIs > Zendesk API**.
  2. In the **Settings** tab, enable **Token Access**.



### Generate an API token (for Basic auth)

  1. Go to **Apps and integrations > APIs > Zendesk API**.
  2. Click the **Add API token** button.
  3. Optionally add a **API token description**.
  4. Click **Create**.
  5. Copy and save the API token now (you won't be able to view it again).
  6. Save the admin email that will authenticate with this token.

**Note:** Basic-auth format used by the Cloud Run function: `email_address/token:api_token`



### (Optional) Create an OAuth client (for Bearer auth instead of API token)

  1. Go to **Apps and integrations > APIs > Zendesk API**.
  2. Click the **OAuth Clients** tab.
  3. Click **Add OAuth client**.
  4. Fill in the **Client Name** , **Unique Identifier** (auto), **Redirect URLs** (can be placeholder if you only mint tokens with API).
  5. Click **Save**.
  6. Create an access token for the integration and grant the minimum scopes required by this guide: 
     * `tickets:read` (for Incremental Tickets)
     * `auditlogs:read` (for Audit Logs; Enterprise only)
  7. Copy the access token (paste into `ZENDESK_BEARER_TOKEN` environment variable) and record the client ID/secret securely (for future token refresh flows).



### Record your Zendesk base URL

Use `https://<your_subdomain>.zendesk.com` (paste into `ZENDESK_BASE_URL` environment variable).

### What to save for later

  * Base URL (for example, `https://acme.zendesk.com`)
  * Email Address of the administrator user (for API token auth)
  * API Token (if using `AUTH_MODE=token`) or OAuth access token (if using `AUTH_MODE=bearer`)
  * (Optional): OAuth client id/secret for lifecycle management



## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `zendesk-crm-logs`)  
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
     * **Service account name** : Enter `zendesk-crm-collector-sa`.
     * **Service account description** : Enter `Service account for Cloud Run function to collect Zendesk CRM logs`.
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
     * **Add principals** : Enter the service account email (for example, `zendesk-crm-collector-sa@PROJECT_ID.iam.gserviceaccount.com`).
     * **Assign roles** : Select **Storage Object Admin**.
  6. Click **Save**.



## Create Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `zendesk-crm-trigger`.
     * Leave other settings as default.
  4. Click **Create**.



## Create Cloud Run function to collect logs

The Cloud Run function is triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from Zendesk API and writes them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `zendesk-crm-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose the topic `zendesk-crm-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub automatically handles authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select the service account `zendesk-crm-collector-sa`.
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `zendesk-crm-logs` | GCS bucket name  
`GCS_PREFIX` | `zendesk/crm/` | Prefix for log files  
`STATE_KEY` | `zendesk/crm/state.json` | State file path  
`ZENDESK_BASE_URL` | `https://your_subdomain.zendesk.com` | Zendesk base URL  
`AUTH_MODE` | `token` | Authentication mode (`token` or `bearer`)  
`ZENDESK_EMAIL` | `analyst@example.com` | Admin email for API token auth  
`ZENDESK_API_TOKEN` | `<api_token>` | API token for authentication  
`ZENDESK_BEARER_TOKEN` | `<leave empty unless using OAuth bearer>` | OAuth bearer token (optional)  
`RESOURCES` | `audit_logs,incremental_tickets` | Resources to collect  
`MAX_PAGES` | `20` | Maximum pages per run  
`LOOKBACK_SECONDS` | `3600` | Initial lookback period  
`HTTP_TIMEOUT` | `60` | HTTP request timeout  
`HTTP_RETRIES` | `3` | HTTP retry attempts  
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

  15. After the service is created, the **inline code editor** opens automatically.




### Add function code

  1. Enter **main** in **Function entry point**
  2. In the inline code editor, create two files:

     * First file: **main.py:**
    
    import functions_framework
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    import json
    import os
    import urllib3
    from datetime import datetime, timezone
    import base64
    import time
    
    # Initialize HTTP client with timeouts
    http = urllib3.PoolManager(
        timeout=urllib3.Timeout(connect=5.0, read=30.0),
        retries=False,
    )
    
    # Initialize Storage client
    storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    
    @functions_framework.cloud_event
    def main(cloud_event):
        """
        Cloud Run function triggered by Pub/Sub to fetch logs from Zendesk API and write to GCS.
    
        Args:
            cloud_event: CloudEvent object containing Pub/Sub message
        """
    
        # Get environment variables
        bucket_name = os.environ.get('GCS_BUCKET')
        prefix = os.environ.get('GCS_PREFIX', 'zendesk/crm/')
        state_key = os.environ.get('STATE_KEY', 'zendesk/crm/state.json')
    
        base_url = os.environ.get('ZENDESK_BASE_URL', '').rstrip('/')
        auth_mode = os.environ.get('AUTH_MODE', 'token').lower()
        email = os.environ.get('ZENDESK_EMAIL', '')
        api_token = os.environ.get('ZENDESK_API_TOKEN', '')
        bearer = os.environ.get('ZENDESK_BEARER_TOKEN', '')
    
        resources = [r.strip() for r in os.environ.get('RESOURCES', 'audit_logs,incremental_tickets').split(',') if r.strip()]
        max_pages = int(os.environ.get('MAX_PAGES', '20'))
        lookback = int(os.environ.get('LOOKBACK_SECONDS', '3600'))
        http_timeout = int(os.environ.get('HTTP_TIMEOUT', '60'))
        http_retries = int(os.environ.get('HTTP_RETRIES', '3'))
    
        if not all([bucket_name, base_url]):
            print('Error: Missing required environment variables')
            return
    
        try:
            # Get GCS bucket
            bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
    
            # Load state
            state = load_state(bucket, state_key)
    
            print(f'Processing resources: {resources}')
    
            summary = []
    
            if 'audit_logs' in resources:
                res = fetch_audit_logs(
                    bucket, prefix, [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get('audit_logs', {}),
                    base_url, auth_mode, email, api_token, bearer,
                    max_pages, http_timeout, http_retries
                )
                state['audit_logs'] = {'next_url': res.get('next_url')}
                summary.append(res)
    
            if 'incremental_tickets' in resources:
                res = fetch_incremental_tickets(
                    bucket, prefix, [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get('incremental_tickets', {}),
                    base_url, auth_mode, email, api_token, bearer,
                    max_pages, lookback, http_timeout, http_retries
                )
                state['incremental_tickets'] = {'cursor': res.get('cursor')}
                summary.append(res)
    
            # Save state
            save_state(bucket, state_key, state)
    
            print(f'Successfully processed logs: {summary}')
    
        except Exception as e:
            print(f'Error processing logs: {str(e)}')
            raise
    
    def get_headers(auth_mode, email, api_token, bearer):
        """Get authentication headers."""
        if auth_mode == 'bearer' and bearer:
            return {
                'Authorization': f'Bearer {bearer}',
                'Accept': 'application/json'
            }
        if auth_mode == 'token' and email and api_token:
            auth_string = f'{email}/token:{api_token}'
            auth_bytes = auth_string.encode('utf-8')
            token = base64.b64encode(auth_bytes).decode('utf-8')
            return {
                'Authorization': f'Basic {token}',
                'Accept': 'application/json'
            }
        raise RuntimeError('Invalid auth settings: provide token (EMAIL + API_TOKEN) or BEARER')
    
    def http_get_json(url, headers, timeout, retries):
        """Make HTTP GET request with retries and exponential backoff."""
        attempt = 0
        backoff = 1.0
        while True:
            try:
                response = http.request('GET', url, headers=headers, timeout=timeout)
                if response.status == 200:
                    return json.loads(response.data.decode('utf-8'))
                elif response.status in (429, 500, 502, 503, 504) and attempt < retries:
                    retry_after = int(response.headers.get('Retry-After', int(backoff)))
                    print(f'HTTP {response.status}: Retrying after {retry_after}s (attempt {attempt + 1}/{retries})')
                    time.sleep(max(1, retry_after))
                    backoff = min(backoff * 2, 30.0)
                    attempt += 1
                    continue
                else:
                    raise Exception(f'HTTP {response.status}: {response.data.decode("utf-8")}')
            except Exception as e:
                if attempt < retries:
                    print(f'Request error: {e}. Retrying after {int(backoff)}s (attempt {attempt + 1}/{retries})')
                    time.sleep(backoff)
                    backoff = min(backoff * 2, 30.0)
                    attempt += 1
                    continue
                raise
    
    def put_page(bucket, prefix, payload, resource):
        """Write page to GCS."""
        ts = datetime.now(timezone.utc)
        key = f'{prefix}{ts.strftime("%Y/%m/%d/%H%M%S")}-zendesk-{resource}.json'
        blob = bucket.blob(key)
        blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
            json.dumps(payload),
            content_type='application/json'
        )
        return key
    
    def fetch_audit_logs(bucket, prefix, state, base_url, auth_mode, email, api_token, bearer, max_pages, timeout, retries):
        """Fetch audit logs with pagination."""
        headers = get_headers(auth_mode, email, api_token, bearer)
        next_url = [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get('next_url') or f'{base_url}/api/v2/audit_logs.json'
    
        pages = 0
        written = 0
        last_next = None
    
        while pages < max_pages and next_url:
            data = http_get_json(next_url, headers, timeout, retries)
            put_page(bucket, prefix, data, 'audit_logs')
            written += len(data.get('audit_logs', []))
    
            # Use next_page for pagination
            last_next = data.get('next_page')
            next_url = last_next
            pages += 1
    
            print(f'Audit logs page {pages}: Retrieved {len(data.get("audit_logs", []))} records')
    
        return {
            'resource': 'audit_logs',
            'pages': pages,
            'written': written,
            'next_url': last_next
        }
    
    def fetch_incremental_tickets(bucket, prefix, state, base_url, auth_mode, email, api_token, bearer, max_pages, lookback, timeout, retries):
        """Fetch incremental tickets with cursor-based pagination."""
        headers = get_headers(auth_mode, email, api_token, bearer)
        cursor = [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get('cursor')
    
        if not cursor:
            start = int(time.time()) - lookback
            next_url = f'{base_url}/api/v2/incremental/tickets/cursor.json?start_time={start}'
        else:
            next_url = f'{base_url}/api/v2/incremental/tickets/cursor.json?cursor={cursor}'
    
        pages = 0
        written = 0
        last_cursor = None
    
        while pages < max_pages and next_url:
            data = http_get_json(next_url, headers, timeout, retries)
            put_page(bucket, prefix, data, 'incremental_tickets')
            written += len(data.get('tickets', []))
    
            # Extract cursor from after_cursor field
            last_cursor = data.get('after_cursor')
            if last_cursor:
                next_url = f'{base_url}/api/v2/incremental/tickets/cursor.json?cursor={last_cursor}'
            else:
                next_url = None
    
            pages += 1
    
            print(f'Incremental tickets page {pages}: Retrieved {len(data.get("tickets", []))} records')
    
        return {
            'resource': 'incremental_tickets',
            'pages': pages,
            'written': written,
            'cursor': last_cursor
        }
    
    def load_state(bucket, key):
        """Load state from GCS."""
        try:
            blob = bucket.blob(key)
            if blob.exists():
                state_data = blob.[download_as_text](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_download_as_text)()
                return json.loads(state_data)
        except Exception as e:
            print(f'Warning: Could not load state: {str(e)}')
        return {'audit_logs': {}, 'incremental_tickets': {}}
    
    def save_state(bucket, key, state):
        """Save state to GCS."""
        try:
            blob = bucket.blob(key)
            blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
                json.dumps(state),
                content_type='application/json'
            )
        except Exception as e:
            print(f'Warning: Could not save state: {str(e)}')
    

     * Second file: **requirements.txt:**
    
    functions-framework==3.*
    google-cloud-storage==2.*
    urllib3>=2.0.0
    

  3. Click **Deploy** to save and deploy the function.

  4. Wait for deployment to complete (2-3 minutes).

**Note:** The Pub/Sub trigger configuration automatically creates the necessary subscriptions and permissions.



## Create Cloud Scheduler job

Cloud scheduler publishes messages to the Pub/Sub topic at regular intervals, triggering the Cloud Run function.

  1. In the **GCP Console** , go to **Cloud Scheduler**.
  2. Click **Create Job**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | `zendesk-crm-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the topic `zendesk-crm-trigger`  
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
**Note:** Zendesk API rate limit is 700 requests per minute for Enterprise Support and Help Center API, with a High Volume add-on increasing the limit to 2500 requests per minute. Adjust `MAX_PAGES` and schedule frequency to stay within rate limits.



### Test the integration

  1. In the **Cloud Scheduler** console, find your job.
  2. Click **Force run** to trigger the job manually.
  3. Wait a few seconds.
  4. Go to **Cloud Run > Services**.
  5. Click your function name `zendesk-crm-collector`.
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for the following:
         
         Processing resources: ['audit_logs', 'incremental_tickets']
         Audit logs page 1: Retrieved X records
         Incremental tickets page 1: Retrieved X records
         Successfully processed logs: [...]
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click your bucket name.

  10. Navigate to the prefix folder `zendesk/crm/`.

  11. Verify that new `.json` files were created with the current timestamp.




If you see errors in the logs:

  * **HTTP 401** : Check API credentials in environment variables
  * **HTTP 403** : Verify account has required permissions (Admin role, Enterprise plan for audit logs)
  * **HTTP 429** : Rate limiting - function will automatically retry with exponential backoff
  * **Missing environment variables** : Check all required variables are set



## Retrieve the Google SecOps service account

Google SecOps uses a unique service account to read data from your GCS bucket. You must grant this service account access to your bucket.

### Get the service account email

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Zendesk CRM logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Zendesk CRM** as the **Log type**. 
  7. Click **Get Service Account**. A unique service account email is displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Don't use service accounts from other documentation or examples.



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



## Configure a feed in Google SecOps to ingest Zendesk CRM logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Zendesk CRM logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Zendesk CRM** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://zendesk-crm-logs/zendesk/crm/
           

       * Replace:

         * `zendesk-crm-logs`: Your GCS bucket name.
         * `zendesk/crm/`: Prefix/folder path where logs are stored.
**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never** : Never deletes any files after transfers (recommended for testing).
       * **Delete transferred files** : Deletes files after successful transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.

**Note:** If you select a deletion option, the service account must have **Storage Object Admin** role instead of Storage Object Viewer. Update IAM permissions accordingly.
     * **Maximum File Age** : Include files modified in the last number of days. Default is 180 days.

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).

     * **Ingestion labels** : The label to be applied to the events from this feed.

  9. Click **Next**.

  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
`additional_data` | `additional.fields` | Merged  
`event_data_available` | `additional.fields` | Mapped: `true` → `additional_data`  
`map_field` | `additional.fields` | Merged  
`change_description` | `metadata.description` | Directly mapped  
`timestamp` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`has_principal` | `metadata.event_type` | Mapped: `true` → `STATUS_UPDATE`  
`has_user` | `metadata.event_type` | Mapped: `true` → `USER_UNCATEGORIZED`  
`id` | `metadata.product_log_id` | Directly mapped  
`method` | `network.http.method` | Directly mapped  
`client` | `network.http.parsed_user_agent` | Directly mapped  
`status` | `network.http.response_code` | Renamed/mapped  
`client` | `network.http.user_agent` | Directly mapped  
`ip_address` | `principal.asset.ip` | Merged  
`ip_address` | `principal.ip` | Merged  
`actor_name` | `principal.user.user_display_name` | Directly mapped  
`source_id` | `principal.user.userid` | Directly mapped  
`user_id` | `principal.user.userid` | Directly mapped  
`key` | `security_result.detection_fields` | Mapped: `authorization_type` → `map_field`  
`map_field` | `security_result.detection_fields` | Merged  
`origin_service` | `target.application` | Directly mapped  
`key` | `target.resource.attribute.labels` | Mapped: `"graphql_operation_name", "operation_type", "query","ticketId"` → `map_field`  
`map_field` | `target.resource.attribute.labels` | Merged  
`url` | `target.url` | Directly mapped  
`actor_id` | `target.user.userid` | Directly mapped  
N/A | `metadata.event_type` | Constant: `STATUS_UPDATE`  
N/A | `metadata.product_name` | Constant: `ZENDESK_CRM`  
N/A | `metadata.vendor_name` | Constant: `ZENDESK_CRM`  
N/A | `network.http.parsed_user_agent` | Constant: `parseduseragent`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/zendesk-crm-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
