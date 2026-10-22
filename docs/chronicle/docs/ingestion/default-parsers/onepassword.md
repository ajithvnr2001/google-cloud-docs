---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/onepassword/
title: Collect 1Password logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:06:39.819078+00:00
---

# Collect 1Password logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/onepassword/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect 1Password logs

**Parser Version:** 5.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest 1Password logs to Google Security Operations using Google Cloud Storage V2.

1Password is a password management platform that helps teams securely store, share, and manage credentials, secrets, and sensitive information. The 1Password Events API provides access to sign-in attempt and item usage data from your 1Password Business account.

## Before you begin

Ensure that you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * A [1Password Business](https://1password.com/pricing/password-manager) account
  * An owner or administrator role in your 1Password account



## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `onepassword-secops-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Collect 1Password credentials

### Set up Events Reporting integration

  1. Sign in to your account on [1Password.com](https://1password.com).
  2. Select **Integrations** in the sidebar.
  3. If you have previously set up other integrations, select **Directory** on the **Integrations** page.
  4. In the **Events Reporting** section, select **Other**.
  5. In the **Name** field, enter a name for the integration (for example, `Google SecOps Integration`).
  6. Click **Add Integration**.



### Create a bearer token

  1. On the integration details page, click **Add a Bearer Token**.
  2. Provide the following configuration details: 
     * **Token Name** : Enter a descriptive name (for example, `SecOps GCS Collector - SignIn and ItemUsage`)
     * **Expires After** : Select the expiration period according to your preference. Select **Never** for a non-expiring token, or choose **30 days** , **90 days** , or **180 days**.
     * **Events to Report** : Select the following checkboxes: 
       * **Sign-in attempts**
       * **Item usage events**
  3. Click **Issue Token**.
  4. On the **Save your token** page, click **Save in 1Password** or copy the token and save it in a secure location.

**Note:** The bearer token is a JWT credential displayed only once. If you lose the token, you must revoke it and issue a new one.
  5. Click **View Integration Details** to confirm the integration is active.




### Determine your Events API base URL

The base URL depends on the server that hosts your 1Password account:

If your account is hosted on | Your Events API base URL is  
---|---  
`1password.com` | `https://events.1password.com`  
`ent.1password.com` | `https://events.ent.1password.com`  
`1password.ca` | `https://events.1password.ca`  
`1password.eu` | `https://events.1password.eu`  
**Note:** To determine which server hosts your account, sign in to 1Password.com and check the domain in your browser address bar.

### Test API access

  * Test your credentials before proceeding with the integration:
        
        # Replace with your actual bearer token and base URL
        BEARER_TOKEN="<your-bearer-token>"
        API_BASE="https://events.1password.com"
        
        # Test API access using the introspect endpoint
        curl -v \
            -H "Authorization: Bearer $BEARER_TOKEN" \
            "$API_BASE/api/v2/auth/introspect"
        




A successful response returns a JSON object with the `features` field listing the event types your token can access (for example, `["signinattempts", "itemusages"]`).

## Create service account for Cloud Run function

The Cloud Run function needs a service account with permissions to write to GCS bucket and be invoked by Pub/Sub.

### Create service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `onepassword-logs-collector-sa`
     * **Service account description** : Enter `Service account for Cloud Run function to collect 1Password logs`
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
  2. Click your bucket (`onepassword-secops-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter `onepassword-logs-collector-sa@PROJECT_ID.iam.gserviceaccount.com`
     * **Assign roles** : Select **Storage Object Admin**
  6. Click **Save**.



## Create Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `onepassword-logs-trigger`
     * Leave other settings as default
  4. Click **Create**.



## Create Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch sign-in attempt and item usage logs from the 1Password Events API and write them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `onepassword-logs-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose `onepassword-logs-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select `onepassword-logs-collector-sa`
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:

Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `onepassword-secops-logs` | GCS bucket name  
`GCS_PREFIX` | `onepassword` | Prefix for log files  
`STATE_KEY` | `onepassword/state.json` | State file path  
`OP_API_BASE` | `https://events.1password.com` | 1Password Events API base URL  
`OP_BEARER_TOKEN` | `<your-bearer-token>` | 1Password Events API bearer token  
`MAX_RECORDS` | `10000` | Max records per endpoint per run  
`PAGE_SIZE` | `1000` | Records per page (max 1000)  
`LOOKBACK_HOURS` | `24` | Initial lookback period in hours  
  10. In the **Variables & Secrets** section, scroll to **Requests** :

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
           GCS_PREFIX = os.environ.get('GCS_PREFIX', 'onepassword')
           STATE_KEY = os.environ.get('STATE_KEY', 'onepassword/state.json')
           API_BASE = os.environ.get('OP_API_BASE')
           BEARER_TOKEN = os.environ.get('OP_BEARER_TOKEN')
           MAX_RECORDS = int(os.environ.get('MAX_RECORDS', '10000'))
           PAGE_SIZE = int(os.environ.get('PAGE_SIZE', '1000'))
           LOOKBACK_HOURS = int(os.environ.get('LOOKBACK_HOURS', '24'))
           
           # 1Password Events API v2 endpoints for sign-in and item usage
           ENDPOINTS = {
             'signinattempts': '/api/v2/signinattempts',
             'itemusages': '/api/v2/itemusages',
           }
           
           def parse_datetime(value: str) -> datetime:
             """Parse RFC 3339 datetime string to datetime object."""
             if [value](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.ObjectCustomContextPayload.html#google_cloud_storage_blob_ObjectCustomContextPayload_value).endswith('Z'):
               value = value[:-1] + '+00:00'
             return datetime.fromisoformat(value)
           
           @functions_framework.cloud_event
           def main(cloud_event):
             """
             Cloud Run function triggered by Pub/Sub to fetch 1Password
             sign-in attempt and item usage logs and write them to GCS
             as NDJSON.
             """
             if not all([GCS_BUCKET, API_BASE, BEARER_TOKEN]):
               print('Error: Missing required environment variables '
                   '(GCS_BUCKET, OP_API_BASE, OP_BEARER_TOKEN)')
               return
           
             try:
               bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(GCS_BUCKET)
           
               # Load state (stores cursors per endpoint)
               state = load_state(bucket, STATE_KEY)
           
               now = datetime.now(timezone.utc)
               total_records = 0
           
               for event_type, path in ENDPOINTS.items():
                 print(f'--- Processing endpoint: {event_type} ---')
           
                 saved_cursor = [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get(f'cursor_{event_type}')
           
                 records, last_cursor = fetch_endpoint(
                   api_base=API_BASE,
                   path=path,
                   bearer_token=BEARER_TOKEN,
                   saved_cursor=saved_cursor,
                   lookback_hours=LOOKBACK_HOURS,
                   page_size=PAGE_SIZE,
                   max_records=MAX_RECORDS,
                 )
           
                 if records:
                   timestamp = now.strftime('%Y%m%d_%H%M%S')
                   object_key = (f'{GCS_PREFIX}/'
                           f'{event_type}_{timestamp}.ndjson')
                   blob = bucket.blob(object_key)
           
                   ndjson = '\n'.join(
                     json.dumps(r, ensure_ascii=False) for r in records
                   ) + '\n'
                   blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
                     ndjson, content_type='application/x-ndjson'
                   )
           
                   print(f'Wrote {len(records)} {event_type} records '
                       f'to gs://{GCS_BUCKET}/{object_key}')
           
                 # Save cursor even if no records (for next poll)
                 if last_cursor:
                   state[f'cursor_{event_type}'] = last_cursor
           
                 total_records += len(records)
           
               # Save state with all cursors
               state['last_run'] = now.isoformat()
               save_state(bucket, STATE_KEY, state)
           
               print(f'Successfully processed {total_records} total records')
           
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
               print(f'Warning: Could not load state: {e}')
             return {}
           
           def save_state(bucket, key, state: dict):
             """Save state to GCS."""
             try:
               blob = bucket.blob(key)
               blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
                 json.dumps(state, indent=2),
                 content_type='application/json',
               )
               print(f'Saved state: {json.dumps(state)}')
             except Exception as e:
               print(f'Warning: Could not save state: {e}')
           
           def fetch_endpoint(api_base, path, bearer_token, saved_cursor,
                     lookback_hours, page_size, max_records):
             """
             Fetch events from a single 1Password Events API v2 endpoint.
           
             The 1Password Events API uses cursor-based pagination with POST
             requests. The first request sends a ResetCursor object with
             optional start_time and limit. Subsequent requests send the
             cursor returned from the previous response.
           
             Args:
               api_base: Events API base URL
               path: Endpoint path
               bearer_token: JWT bearer token
               saved_cursor: Cursor from previous run (or None)
               lookback_hours: Hours to look back on first run
               page_size: Max events per page (1-1000)
               max_records: Max total events per run
           
             Returns:
               Tuple of (records list, last_cursor string)
             """
             url = f'{api_base.rstrip("/")}{path}'
           
             headers = {
               'Authorization': f'Bearer {bearer_token}',
               'Content-Type': 'application/json',
               'Accept': 'application/json',
             }
           
             records = []
             cursor = saved_cursor
             page_num = 0
             backoff = 1.0
           
             while True:
               page_num += 1
           
               if len(records) >= max_records:
                 print(f'Reached max_records limit ({max_records})')
                 break
           
               # Build request body
               if cursor:
                 # Continuing cursor: resume from last position
                 body = json.dumps({'cursor': cursor})
               else:
                 # ResetCursor: first request or no saved state
                 start_time = (
                   datetime.now(timezone.utc)
                   - timedelta(hours=lookback_hours)
                 )
                 body = json.dumps({
                   'limit': page_size,
                   'start_time': start_time.strftime(
                     '%Y-%m-%dT%H:%M:%SZ'
                   ),
                 })
           
               try:
                 response = http.request(
                   'POST', url, body=body, headers=headers,
                 )
           
                 # Handle rate limiting (600 req/min, 30000 req/hour)
                 if response.status == 429:
                   retry_after = int(
                     response.headers.get(
                       'Retry-After', str(int(backoff))
                     )
                   )
                   print(f'Rate limited (429). Retrying after '
                       f'{retry_after}s...')
                   time.sleep(retry_after)
                   backoff = min(backoff * 2, 60.0)
                   continue
           
                 backoff = 1.0
           
                 if response.status != 200:
                   response_text = response.data.decode('utf-8')
                   print(f'HTTP Error {response.status}: '
                       f'{response_text}')
                   break
           
                 data = json.loads(response.data.decode('utf-8'))
           
                 page_items = data.get('items', [])
                 cursor = data.get('cursor')
                 has_more = data.get('has_more', False)
           
                 if page_items:
                   print(f'Page {page_num}: Retrieved '
                       f'{len(page_items)} events')
                   records.extend(page_items)
           
                 if not has_more:
                   print(f'No more pages (has_more=false)')
                   break
           
                 if not cursor:
                   print(f'No cursor returned, stopping')
                   break
           
               except urllib3.[exceptions](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.exceptions.html).HTTPError as e:
                 print(f'HTTP error: {str(e)}')
                 break
               except Exception as e:
                 print(f'Error fetching events: {str(e)}')
                 break
           
             print(f'Retrieved {len(records)} total records '
                 f'from {page_num} pages')
             return records, cursor
           

     * Second file: **requirements.txt:**
           
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
**Name** | `onepassword-logs-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select `onepassword-logs-trigger`  
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

  1. In the **Cloud Scheduler** console, find `onepassword-logs-collector-hourly`.
  2. Click **Force run** to trigger the job manually.
  3. Wait a few seconds.
  4. Go to **Cloud Run > Services**.
  5. Click `onepassword-logs-collector`.
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for:
         
         --- Processing endpoint: signinattempts ---
         Page 1: Retrieved X events
         Wrote X signinattempts records to gs://onepassword-secops-logs/onepassword/signinattempts_YYYYMMDD_HHMMSS.ndjson
         --- Processing endpoint: itemusages ---
         Page 1: Retrieved X events
         Wrote X itemusages records to gs://onepassword-secops-logs/onepassword/itemusages_YYYYMMDD_HHMMSS.ndjson
         Successfully processed X total records
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click `onepassword-secops-logs`.

  10. Navigate to the `onepassword/` folder.

  11. Verify that new `.ndjson` files were created with the current timestamp.




If you see errors in the logs:

  * **HTTP 401** : Check the bearer token in the `OP_BEARER_TOKEN` environment variable. The token may have expired.
  * **HTTP 429** : Rate limiting. The function automatically retries with backoff. The 1Password Events API allows 600 requests per minute and 30,000 requests per hour.
  * **Missing environment variables** : Check all required variables are set in the Cloud Run function configuration.
  * **No records returned** : Verify your bearer token has access to the requested event types using the introspect endpoint.



## Retrieve the Google SecOps service account

Google SecOps uses a unique service account to read data from your GCS bucket. You must grant this service account access to your bucket.

### Get the service account email

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `1Password Sign-In and Item Usage Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **1Password** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Don't use service accounts from other documentation or examples.
  9. Click **Next**.

  10. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://onepassword-secops-logs/onepassword/
           

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
  2. Click `onepassword-secops-logs`.
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
category | security_result.category_details | The value is taken from the `category` field in the raw log.  
client.app_name | principal.application | The value is taken from the `client.app_name` field in the raw log.  
client.app_version | metadata.product_version | The value is taken from the `client.app_version` field in the raw log.  
client.ip_address | principal.ip | The value is taken from the `client.ip_address` field in the raw log.  
client.os_name | principal.platform | The value is taken from the `client.os_name` field in the raw log and mapped to the corresponding UDM platform value (`LINUX`, `WINDOWS`, `MAC`).  
client.os_version | principal.platform_version | The value is taken from the `client.os_version` field in the raw log.  
client.platform_name | principal.resource.attribute.labels | The value is taken from the `client.platform_name` field in the raw log.  
client.platform_version | principal.asset.platform_software.platform_version | The value is taken from the `client.platform_version` field in the raw log.  
country | principal.location.country_or_region | The value is taken from the `country` field in the raw log if `location.country` is not present.  
item_uuid | security_result.about.resource.attribute.labels | The value is taken from the `item_uuid` field in the raw log.  
location.city | principal.location.city | The value is taken from the `location.city` field in the raw log.  
location.country | principal.location.country_or_region | The value is taken from the `location.country` field in the raw log.  
location.latitude | principal.location.region_latitude | The value is taken from the `location.latitude` field in the raw log.  
location.longitude | principal.location.region_longitude | The value is taken from the `location.longitude` field in the raw log.  
location.region | principal.location.name | The value is taken from the `location.region` field in the raw log.  
session.ip | principal.ip | The value is taken from the `session.ip` field in the raw log.  
session_uuid | network.session_id | The value is taken from the `session_uuid` field in the raw log.  
target_user.email | target.user.email_addresses | The value is taken from the `target_user.email` field in the raw log.  
target_user.uuid | target.user.userid | The value is taken from the `target_user.uuid` field in the raw log.  
timestamp | metadata.event_timestamp | The value is taken from the `timestamp` field in the raw log and converted to seconds and nanoseconds.  
type | additional.fields | The value is taken from the `type` field in the raw log.  
user.email | principal.user.email_addresses | The value is taken from the `user.email` field in the raw log.  
user.name | principal.user.user_display_name | The value is taken from the `user.name` field in the raw log.  
used_version | additional.fields | The value is taken from the `used_version` field in the raw log.  
uuid | principal.resource.attribute.labels | The value is taken from the `uuid` field in the raw log.  
vault_uuid | security_result.about.resource.attribute.labels | The value is taken from the `vault_uuid` field in the raw log.  
N/A | extensions.auth | An empty object is created for this field.  
N/A | metadata.event_type | Set to `USER_LOGIN` if category is `success` or `firewall_reported_success`, `STATUS_UPDATE` if no user information is present, and `USER_UNCATEGORIZED` otherwise.  
N/A | metadata.log_type | Set to `ONEPASSWORD`.  
N/A | metadata.product_name | Set to `ONEPASSWORD`.  
N/A | metadata.vendor_name | Set to `ONEPASSWORD`.  
N/A | security_result.action | Set to `ALLOW` if category is `success` or `firewall_reported_success`, `BLOCK` if category is `credentials_failed`, `mfa_failed`, `modern_version_failed`, or `firewall_failed`, and is left empty otherwise.  
`lt` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`item.actor_details.uuid` | `principal.user.userid` | Mapped from changelog  
`item.actor_details.name` | `principal.user.user_display_name` | Mapped from changelog  
`item.actor_details.email` | `principal.email` | Mapped from changelog  
`item.actor_uuid` | `security_result.about.resource.attribute.labels` | Mapped from changelog  
`item.object_type` | `additional.fields` | Mapped from changelog  
`item.object_uuid` | `security_result.about.resource.attribute.labels` | Mapped from changelog  
`item.aux_info` | `additional.fields` | Mapped from changelog  
`item.aux_uuid` | `security_result.about.resource.attribute.labels` | Mapped from changelog  
`item.session.uuid` | `network.session_id` | Mapped from changelog  
`item.session.device_uuid` | `target.resource.product_object_id` | Mapped from changelog  
`item.session.ip` | `principal.ip` | Mapped from changelog  
`target_user.name` | `target.user.user_display_name` | Mapped from changelog  
`uuid` | `principal.userid` | Mapped from changelog  
`type","action","used_version",` | `additional.fields` | Mapped from changelog  
`target_user.uuid` | `target.user.product_object_id` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/onepassword-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
