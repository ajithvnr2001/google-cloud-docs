---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/team-cymru-scout-threatintel/
title: Collect Team Cymru Scout Threat Intelligence logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:55:05.554906+00:00
---

# Collect Team Cymru Scout Threat Intelligence logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/team-cymru-scout-threatintel/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Team Cymru Scout Threat Intelligence logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Team Cymru Scout Threat Intelligence data to Google Security Operations using Google Cloud Storage. Team Cymru Scout provides threat intelligence data including account usage metrics, query limits, and foundation query statistics to help organizations monitor their security posture and threat intelligence consumption.

## Before you begin

Ensure that you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * Privileged access to Team Cymru Scout tenant



## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `team-cymru-scout-ti`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Collect Team Cymru Scout API credentials

  1. Sign in to the [Team Cymru Scout Platform](https://scout.cymru.com).
  2. Go to the **API Keys** page.
  3. Click the **Create** button.
  4. Provide the description for the key, if needed.
  5. Click the **Create Key** button to generate the API key.
  6. Copy and save in a secure location the following details:

     * **SCOUT_API_TOKEN** : API access token
     * **SCOUT_BASE_URL** : Scout API base URL (typically `https://scout.cymru.com`)
**Note:** The API token will be used by the Cloud Run function to authenticate to Team Cymru Scout API using `Authorization: Token <api_token>` header format. Team Cymru Scout also supports Basic authentication with username/password as an alternative to Token auth, but this integration uses token authentication.



### Test API access

  * Test your credentials before proceeding with the integration:
        
        # Replace with your actual credentials
        SCOUT_API_TOKEN="your-api-token"
        SCOUT_BASE_URL="https://scout.cymru.com"
        
        # Test API access to usage endpoint
        curl -v --request GET \
          --url "${SCOUT_BASE_URL}/api/scout/usage" \
          --header "Authorization: Token ${SCOUT_API_TOKEN}"
        




## Create service account for Cloud Run function

The Cloud Run function needs a service account with permissions to write to GCS bucket.

### Create service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `team-cymru-scout-ti-sa`.
     * **Service account description** : Enter `Service account for Cloud Run function to collect Team Cymru Scout Threat Intelligence data`.
  4. Click **Create and Continue**.
  5. In the **Grant this service account access to project** section: 
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

Grant the service account write permissions on the GCS bucket:

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `team-cymru-scout-ti-sa@PROJECT_ID.iam.gserviceaccount.com`).
     * **Assign roles** : Select **Storage Object Admin**.
  6. Click **Save**.



## Create Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `team-cymru-scout-ti-trigger`.
     * Leave other settings as default.
  4. Click **Create**.



## Create Cloud Run function to collect threat intelligence data

The Cloud Run function is triggered by Pub/Sub messages from Cloud Scheduler to fetch threat intelligence data from Team Cymru Scout API and writes them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `team-cymru-scout-ti-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In* _Select a Cloud Pub/Sub topic_ *, choose the topic `team-cymru-scout-ti-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub automatically handles authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select the service account `team-cymru-scout-ti-sa`.
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value  
---|---  
`GCS_BUCKET` | `team-cymru-scout-ti`  
`GCS_PREFIX` | `team-cymru/scout-ti/`  
`STATE_KEY` | `team-cymru/scout-ti/state.json`  
`SCOUT_BASE_URL` | `https://scout.cymru.com`  
`SCOUT_API_TOKEN` | `your-scout-api-token`  
`COLLECTION_INTERVAL_HOURS` | `1`  
`HTTP_TIMEOUT` | `60`  
`HTTP_RETRIES` | `3`  
**Note:** The `SCOUT_BASE_URL` should be `https://scout.cymru.com` as documented in the official Team Cymru Scout API documentation. The API token will be used with `Authorization: Token <api_token>` header format.
  10. Scroll down in the **Variables & Secrets** tab to **Requests** :

     * **Request timeout** : Enter `600` seconds (10 minutes).
  11. Go to the **Settings** tab in **Containers** :

     * In the **Resources** section: 
       * **Memory** : Select **512 MiB** or higher.
       * **CPU** : Select **1**.
     * Click **Done**.
  12. Scroll down to **Execution environment** :

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
    from datetime import datetime, timezone
    import time
    
    # Initialize HTTP client
    http = urllib3.PoolManager()
    
    # Initialize Storage client
    storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    
    @functions_framework.cloud_event
    def main(cloud_event):
        """
        Cloud Run function triggered by Pub/Sub to fetch usage data from Team Cymru Scout API and write to GCS.
    
        Args:
            cloud_event: CloudEvent object containing Pub/Sub message
        """
    
        # Get environment variables
        bucket_name = os.environ.get('GCS_BUCKET')
        prefix = os.environ.get('GCS_PREFIX', 'team-cymru/scout-ti/')
        state_key = os.environ.get('STATE_KEY', 'team-cymru/scout-ti/state.json')
        collection_interval_hours = int(os.environ.get('COLLECTION_INTERVAL_HOURS', '1'))
        http_timeout = int(os.environ.get('HTTP_TIMEOUT', '60'))
        http_retries = int(os.environ.get('HTTP_RETRIES', '3'))
    
        # Team Cymru Scout API credentials
        scout_base_url = os.environ.get('SCOUT_BASE_URL', 'https://scout.cymru.com')
        scout_api_token = os.environ.get('SCOUT_API_TOKEN')
    
        if not all([bucket_name, scout_api_token]):
            print('Error: Missing required environment variables')
            return
    
        try:
            # Get GCS bucket
            bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
    
            # Load state (last collection timestamp)
            state = load_state(bucket, state_key)
            now = time.time()
            last_collection = [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get('last_collection_ts', now - (collection_interval_hours * 3600))
    
            print(f'Collecting usage data at {iso_format(now)} (last collection: {iso_format(last_collection)})')
    
            # Fetch usage data from Team Cymru Scout API
            usage_data = fetch_usage_data(
                scout_base_url, 
                scout_api_token, 
                http_timeout,
                http_retries
            )
    
            if usage_data:
                # Add timestamp and event type
                usage_data['event_type'] = 'account_usage'
                usage_data['collection_timestamp'] = iso_format(now)
    
                # Write to GCS
                write_to_gcs(bucket, prefix, usage_data, now)
    
                # Update state
                save_state(bucket, state_key, {'last_collection_ts': now})
    
                print(f'Successfully collected and stored usage data')
            else:
                print('No usage data retrieved')
    
        except Exception as e:
            print(f'Error processing usage data: {str(e)}')
            raise
    
    def iso_format(ts):
        """Convert Unix timestamp to ISO 8601 format."""
        return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(ts))
    
    def load_state(bucket, key):
        """Load state from GCS."""
        try:
            blob = bucket.blob(key)
            if blob.exists():
                state_data = blob.[download_as_text](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_download_as_text)()
                return json.loads(state_data)
        except Exception as e:
            print(f'Warning: Could not load state: {str(e)}')
        return {}
    
    def save_state(bucket, key, state):
        """Save state to GCS."""
        try:
            blob = bucket.blob(key)
            blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
                json.dumps(state, separators=(',', ':')),
                content_type='application/json'
            )
        except Exception as e:
            print(f'Warning: Could not save state: {str(e)}')
    
    def http_request(url, method='GET', body=None, headers=None, timeout=60, retries=3):
        """Make HTTP request with retry logic."""
        attempt = 0
        while True:
            try:
                req_headers = headers or {}
                if body is not None:
                    req_headers['Content-Type'] = 'application/json'
                    body_bytes = body.encode('utf-8') if isinstance(body, str) else body
                else:
                    body_bytes = None
    
                response = http.request(
                    method,
                    url,
                    body=body_bytes,
                    headers=req_headers,
                    timeout=timeout
                )
    
                if response.status == 200:
                    return response.data, response.headers.get('Content-Type', 'application/json')
                elif response.status in (429, 500, 502, 503, 504) and attempt < retries:
                    delay = 1 + attempt
                    retry_after = response.headers.get('Retry-After')
                    if retry_after:
                        try:
                            delay = int(retry_after)
                        except:
                            pass
                    time.sleep(max(1, delay))
                    attempt += 1
                    continue
                else:
                    raise Exception(f'HTTP {response.status}: {response.data.decode("utf-8")}')
            except urllib3.[exceptions](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.exceptions.html).HTTPError as e:
                if attempt < retries:
                    time.sleep(1 + attempt)
                    attempt += 1
                    continue
                raise
    
    def fetch_usage_data(base_url, api_token, timeout, retries):
        """
        Fetch usage data from Team Cymru Scout API.
    
        Implementation mirrors the official Scout API example:
        curl --request GET --url 'https://scout.cymru.com/api/scout/usage' --header 'Authorization: Token valid_api_token'
        """
        # Use the documented /api/scout/usage endpoint
        url = f'{base_url}/api/scout/usage'
    
        # Use Token authentication as documented
        headers = {
            'Authorization': f'Token {api_token}',
            'Accept': 'application/json'
        }
    
        print(f'Fetching usage data from {url}')
    
        try:
            # Fetch data
            blob_data, content_type = http_request(url, method='GET', headers=headers, timeout=timeout, retries=retries)
    
            # Parse response
            usage_data = json.loads(blob_data.decode('utf-8'))
    
            print(f'Retrieved usage data: used_queries={usage_data.get("used_queries")}, query_limit={usage_data.get("query_limit")}')
    
            return usage_data
    
        except Exception as e:
            print(f'Error fetching usage data: {e}')
            return None
    
    def write_to_gcs(bucket, prefix, data, timestamp):
        """Write data to GCS."""
        # Create date-based path
        date_path = time.strftime('%Y/%m/%d', time.gmtime(timestamp))
        key = f'{prefix}{date_path}/usage_{int(timestamp)}.json'
    
        # Write as JSON
        blob = bucket.blob(key)
        blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
            json.dumps(data, separators=(',', ':')),
            content_type='application/json'
        )
        print(f'Wrote data to gs://{bucket.name}/{key}')
    

     * Second file: **requirements.txt:**
    
    functions-framework==3.*
    google-cloud-storage==2.*
    urllib3>=2.0.0
    

  3. Click **Deploy** to save and deploy the function.

  4. Wait for deployment to complete (2-3 minutes).

**Note:** The Pub/Sub trigger configuration automatically creates the necessary subscriptions and permissions. This implementation uses the documented Team Cymru Scout API endpoint `/api/scout/usage` with `Authorization: Token <api_token>` authentication as specified in the official Scout API documentation.



## Create Cloud Scheduler job

Cloud scheduler publishes messages to the Pub/Sub topic at regular intervals, triggering the Cloud Run function.

  1. In the **GCP Console** , go to **Cloud Scheduler**.
  2. Click **Create Job**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | `team-cymru-scout-ti-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the topic `team-cymru-scout-ti-trigger`  
**Message body** | `{}` (empty JSON object)  
  4. Click **Create**.




### Schedule frequency options

  * Choose frequency based on data volume and latency requirements:

Frequency | Cron Expression | Use Case  
---|---|---  
Every 5 minutes | `*/5 * * * *` | High-frequency monitoring  
Every 15 minutes | `*/15 * * * *` | Medium frequency  
Every hour | `0 * * * *` | Standard (recommended)  
Every 6 hours | `0 */6 * * *` | Low frequency  
Daily | `0 0 * * *` | Daily usage tracking  



### Test the scheduler job

  1. In the **Cloud Scheduler** console, find your job.
  2. Click **Force run** to trigger manually.
  3. Wait a few seconds and go to **Cloud Run > Services > team-cymru-scout-ti-collector > Logs**.
  4. Verify the function executed successfully.
  5. Check the GCS bucket to confirm usage data was written.



## Retrieve the Google SecOps service account

Google SecOps uses a unique service account to read data from your GCS bucket. You must grant this service account access to your bucket.

### Get the service account email

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Team Cymru Scout Threat Intelligence`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Team Cymru Scout Threat Intelligence** as the **Log type**.
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



## Configure a feed in Google SecOps to ingest Team Cymru Scout Threat Intelligence data

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Team Cymru Scout Threat Intelligence`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Team Cymru Scout Threat Intelligence** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://team-cymru-scout-ti/team-cymru/scout-ti/
           

       * Replace:

         * `team-cymru-scout-ti`: Your GCS bucket name.
         * `team-cymru/scout-ti/`: Prefix/folder path where logs are stored.
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
`date_index` | `additional.fields` | Mapped: `index` → `asns_label`, `index` → `country_label`, `index` → `service_label`, `index...  
`as_index` | `additional.fields.key` | Directly mapped  
`asns.label` | `additional.fields.key` | Directly mapped  
`child_index_info` | `additional.fields.key` | Directly mapped  
`child_tag_info` | `additional.fields.key` | Directly mapped  
`code_index` | `additional.fields.key` | Directly mapped  
`code_index_info` | `additional.fields.key` | Directly mapped  
`country.label` | `additional.fields.key` | Directly mapped  
`data.date` | `additional.fields.key` | Directly mapped  
`date` | `additional.fields.key` | Directly mapped  
`ind` | `additional.fields.key` | Directly mapped  
`index` | `additional.fields.key` | Directly mapped  
`index_alt` | `additional.fields.key` | Directly mapped  
`index_as_info` | `additional.fields.key` | Directly mapped  
`index_children` | `additional.fields.key` | Directly mapped  
`index_children_child` | `additional.fields.key` | Directly mapped  
`index_info` | `additional.fields.key` | Directly mapped  
`index_local_top_services` | `additional.fields.key` | Directly mapped  
`index_peer_as_info` | `additional.fields.key` | Directly mapped  
`index_peer_cc` | `additional.fields.key` | Directly mapped  
`index_peer_tags` | `additional.fields.key` | Directly mapped  
`index_peer_top_services` | `additional.fields.key` | Directly mapped  
`index_tags` | `additional.fields.key` | Directly mapped  
`info_index` | `additional.fields.key` | Directly mapped  
`keyword` | `additional.fields.key` | Directly mapped  
`name_index` | `additional.fields.key` | Directly mapped  
`server_index` | `additional.fields.key` | Directly mapped  
`service.label` | `additional.fields.key` | Directly mapped  
`tag.label` | `additional.fields.key` | Directly mapped  
`tag_index` | `additional.fields.key` | Directly mapped  
`tag_info` | `additional.fields.key` | Directly mapped  
`account_name` | `additional.fields.value.string_value` | Directly mapped  
`account_type` | `additional.fields.value.string_value` | Directly mapped  
`alt_arr` | `additional.fields.value.string_value` | Directly mapped  
`as_info_arr.as_name` | `additional.fields.value.string_value` | Directly mapped  
`as_info_arr.asn` | `additional.fields.value.string_value` | Directly mapped  
`certs_arr.common_name` | `additional.fields.value.string_value` | Directly mapped  
`certs_arr.event_count` | `additional.fields.value.string_value` | Directly mapped  
`certs_arr.first_seen` | `additional.fields.value.string_value` | Directly mapped  
`certs_arr.ip` | `additional.fields.value.string_value` | Directly mapped  
`certs_arr.issuer` | `additional.fields.value.string_value` | Directly mapped  
`certs_arr.issuer_common_name` | `additional.fields.value.string_value` | Directly mapped  
`certs_arr.last_seen` | `additional.fields.value.string_value` | Directly mapped  
`certs_arr.md5` | `additional.fields.value.string_value` | Directly mapped  
`certs_arr.not_after` | `additional.fields.value.string_value` | Directly mapped  
`certs_arr.not_before` | `additional.fields.value.string_value` | Directly mapped  
`certs_arr.port` | `additional.fields.value.string_value` | Directly mapped  
`certs_arr.self_signed` | `additional.fields.value.string_value` | Directly mapped  
`certs_arr.sha1` | `additional.fields.value.string_value` | Directly mapped  
`certs_arr.sha256` | `additional.fields.value.string_value` | Directly mapped  
`certs_arr.subject` | `additional.fields.value.string_value` | Directly mapped  
`certs_arr.valid_days` | `additional.fields.value.string_value` | Directly mapped  
`children_arr.id` | `additional.fields.value.string_value` | Directly mapped  
`children_arr.name` | `additional.fields.value.string_value` | Directly mapped  
`code` | `additional.fields.value.string_value` | Directly mapped  
`communications.event_count` | `additional.fields.value.string_value` | Directly mapped  
`data` | `additional.fields.value.string_value` | Directly mapped  
`data.count` | `additional.fields.value.string_value` | Directly mapped  
`end_date` | `additional.fields.value.string_value` | Directly mapped  
`event_count` | `additional.fields.value.string_value` | Directly mapped  
`event_type` | `additional.fields.value.string_value` | Directly mapped  
`fingerprint_arr.count` | `additional.fields.value.string_value` | Directly mapped  
`fingerprint_arr.event_count` | `additional.fields.value.string_value` | Directly mapped  
`fingerprint_arr.first_seen` | `additional.fields.value.string_value` | Directly mapped  
`fingerprint_arr.ip` | `additional.fields.value.string_value` | Directly mapped  
`fingerprint_arr.last_seen` | `additional.fields.value.string_value` | Directly mapped  
`fingerprint_arr.port` | `additional.fields.value.string_value` | Directly mapped  
`fingerprint_arr.signature` | `additional.fields.value.string_value` | Directly mapped  
`fingerprint_arr.type` | `additional.fields.value.string_value` | Directly mapped  
`fingerprints.event_count` | `additional.fields.value.string_value` | Directly mapped  
`fingerprints_arr.active_days` | `additional.fields.value.string_value` | Directly mapped  
`fingerprints_arr.distinct_ips` | `additional.fields.value.string_value` | Directly mapped  
`fingerprints_arr.event_count` | `additional.fields.value.string_value` | Directly mapped  
`fingerprints_arr.fingerprint` | `additional.fields.value.string_value` | Directly mapped  
`fingerprints_arr.first_seen` | `additional.fields.value.string_value` | Directly mapped  
`fingerprints_arr.ip` | `additional.fields.value.string_value` | Directly mapped  
`fingerprints_arr.last_seen` | `additional.fields.value.string_value` | Directly mapped  
`fingerprints_arr.port` | `additional.fields.value.string_value` | Directly mapped  
`fingerprints_arr.type` | `additional.fields.value.string_value` | Directly mapped  
`foundation_query_limit` | `additional.fields.value.string_value` | Directly mapped  
`indicator` | `additional.fields.value.string_value` | Directly mapped  
`indicator_type` | `additional.fields.value.string_value` | Directly mapped  
`local_country_codes` | `additional.fields.value.string_value` | Directly mapped  
`local_tags_arr.id` | `additional.fields.value.string_value` | Directly mapped  
`local_tags_arr.name` | `additional.fields.value.string_value` | Directly mapped  
`local_tags_children_arr.id` | `additional.fields.value.string_value` | Directly mapped  
`local_tags_children_arr.name` | `additional.fields.value.string_value` | Directly mapped  
`local_top_services_arr.description` | `additional.fields.value.string_value` | Directly mapped  
`local_top_services_arr.port` | `additional.fields.value.string_value` | Directly mapped  
`local_top_services_arr.proto_number` | `additional.fields.value.string_value` | Directly mapped  
`local_top_services_arr.service_name` | `additional.fields.value.string_value` | Directly mapped  
`open_ports.event_count` | `additional.fields.value.string_value` | Directly mapped  
`open_ports.unique_ports` | `additional.fields.value.string_value` | Directly mapped  
`open_ports_arr.css_color` | `additional.fields.value.string_value` | Directly mapped  
`open_ports_arr.event_count` | `additional.fields.value.string_value` | Directly mapped  
`open_ports_arr.first_seen` | `additional.fields.value.string_value` | Directly mapped  
`open_ports_arr.ip` | `additional.fields.value.string_value` | Directly mapped  
`open_ports_arr.last_seen` | `additional.fields.value.string_value` | Directly mapped  
`open_ports_arr.port` | `additional.fields.value.string_value` | Directly mapped  
`open_ports_arr.protocol` | `additional.fields.value.string_value` | Directly mapped  
`open_ports_arr.protocol_text` | `additional.fields.value.string_value` | Directly mapped  
`open_ports_arr.service` | `additional.fields.value.string_value` | Directly mapped  
`pdns.event_count` | `additional.fields.value.string_value` | Directly mapped  
`pdns_arr.active_days` | `additional.fields.value.string_value` | Directly mapped  
`pdns_arr.css_color` | `additional.fields.value.string_value` | Directly mapped  
`pdns_arr.distinct_ips` | `additional.fields.value.string_value` | Directly mapped  
`pdns_arr.domain` | `additional.fields.value.string_value` | Directly mapped  
`pdns_arr.domain_created` | `additional.fields.value.string_value` | Directly mapped  
`pdns_arr.domain_expires` | `additional.fields.value.string_value` | Directly mapped  
`pdns_arr.event_count` | `additional.fields.value.string_value` | Directly mapped  
`pdns_arr.first_seen` | `additional.fields.value.string_value` | Directly mapped  
`pdns_arr.ip` | `additional.fields.value.string_value` | Directly mapped  
`pdns_arr.last_seen` | `additional.fields.value.string_value` | Directly mapped  
`pdns_arr.registrar` | `additional.fields.value.string_value` | Directly mapped  
`pdns_arr.root` | `additional.fields.value.string_value` | Directly mapped  
`pdns_arr.tld` | `additional.fields.value.string_value` | Directly mapped  
`pdns_arr.type` | `additional.fields.value.string_value` | Directly mapped  
`peer_as_info_arr.as_name` | `additional.fields.value.string_value` | Directly mapped  
`peer_as_info_arr.asn` | `additional.fields.value.string_value` | Directly mapped  
`peer_country_codes` | `additional.fields.value.string_value` | Directly mapped  
`peer_tags_arr.id` | `additional.fields.value.string_value` | Directly mapped  
`peer_tags_arr.name` | `additional.fields.value.string_value` | Directly mapped  
`peer_tags_children_arr.id` | `additional.fields.value.string_value` | Directly mapped  
`peer_tags_children_arr.name` | `additional.fields.value.string_value` | Directly mapped  
`peer_tags_children_children_arr.id` | `additional.fields.value.string_value` | Directly mapped  
`peer_tags_children_children_arr.name` | `additional.fields.value.string_value` | Directly mapped  
`peer_top_services_arr.description` | `additional.fields.value.string_value` | Directly mapped  
`peer_top_services_arr.port` | `additional.fields.value.string_value` | Directly mapped  
`peer_top_services_arr.proto_number` | `additional.fields.value.string_value` | Directly mapped  
`peer_top_services_arr.service_name` | `additional.fields.value.string_value` | Directly mapped  
`peers_arr.event_count` | `additional.fields.value.string_value` | Directly mapped  
`peers_arr.first_seen` | `additional.fields.value.string_value` | Directly mapped  
`peers_arr.last_seen` | `additional.fields.value.string_value` | Directly mapped  
`peers_arr.local.ip` | `additional.fields.value.string_value` | Directly mapped  
`peers_arr.local.max_port` | `additional.fields.value.string_value` | Directly mapped  
`peers_arr.local.min_port` | `additional.fields.value.string_value` | Directly mapped  
`peers_arr.local.unique_ports` | `additional.fields.value.string_value` | Directly mapped  
`peers_arr.peer.ip` | `additional.fields.value.string_value` | Directly mapped  
`peers_arr.peer.max_port` | `additional.fields.value.string_value` | Directly mapped  
`peers_arr.peer.min_port` | `additional.fields.value.string_value` | Directly mapped  
`peers_arr.peer.unique_ports` | `additional.fields.value.string_value` | Directly mapped  
`peers_arr.proto` | `additional.fields.value.string_value` | Directly mapped  
`peers_arr.proto_text` | `additional.fields.value.string_value` | Directly mapped  
`query_limit` | `additional.fields.value.string_value` | Directly mapped  
`remaining_foundation_queries` | `additional.fields.value.string_value` | Directly mapped  
`remaining_queries` | `additional.fields.value.string_value` | Directly mapped  
`server.root` | `additional.fields.value.string_value` | Directly mapped  
`service_counts_arr.event_count` | `additional.fields.value.string_value` | Directly mapped  
`service_counts_arr.port` | `additional.fields.value.string_value` | Directly mapped  
`service_counts_arr.proto` | `additional.fields.value.string_value` | Directly mapped  
`service_counts_arr.proto_text` | `additional.fields.value.string_value` | Directly mapped  
`service_counts_arr.service.description` | `additional.fields.value.string_value` | Directly mapped  
`service_counts_arr.service.port` | `additional.fields.value.string_value` | Directly mapped  
`service_counts_arr.service.proto_number` | `additional.fields.value.string_value` | Directly mapped  
`service_counts_arr.service.service_name` | `additional.fields.value.string_value` | Directly mapped  
`start_date` | `additional.fields.value.string_value` | Directly mapped  
`summary.bgp_asn` | `additional.fields.value.string_value` | Directly mapped  
`summary.bgp_asname` | `additional.fields.value.string_value` | Directly mapped  
`summary.comms_total` | `additional.fields.value.string_value` | Directly mapped  
`summary.end_date` | `additional.fields.value.string_value` | Directly mapped  
`summary.insights.total` | `additional.fields.value.string_value` | Directly mapped  
`summary.open_ports.total` | `additional.fields.value.string_value` | Directly mapped  
`summary.open_ports.unique_ports` | `additional.fields.value.string_value` | Directly mapped  
`summary.pdns.total` | `additional.fields.value.string_value` | Directly mapped  
`summary.start_date` | `additional.fields.value.string_value` | Directly mapped  
`summary.total` | `additional.fields.value.string_value` | Directly mapped  
`summary.whois.as_name` | `additional.fields.value.string_value` | Directly mapped  
`summary.whois.asn` | `additional.fields.value.string_value` | Directly mapped  
`tag_data_arr.first_seen` | `additional.fields.value.string_value` | Directly mapped  
`tag_data_arr.last_seen` | `additional.fields.value.string_value` | Directly mapped  
`tag_data_arr.tag.css_color` | `additional.fields.value.string_value` | Directly mapped  
`tag_data_arr.tag.description` | `additional.fields.value.string_value` | Directly mapped  
`tag_data_arr.tag.id` | `additional.fields.value.string_value` | Directly mapped  
`tag_data_arr.tag.name` | `additional.fields.value.string_value` | Directly mapped  
`top_open_ports_arr.banner` | `additional.fields.value.string_value` | Directly mapped  
`top_open_ports_arr.banner_sha1` | `additional.fields.value.string_value` | Directly mapped  
`top_open_ports_arr.event_count` | `additional.fields.value.string_value` | Directly mapped  
`top_open_ports_arr.first_seen` | `additional.fields.value.string_value` | Directly mapped  
`top_open_ports_arr.ip` | `additional.fields.value.string_value` | Directly mapped  
`top_open_ports_arr.last_seen` | `additional.fields.value.string_value` | Directly mapped  
`top_open_ports_arr.port` | `additional.fields.value.string_value` | Directly mapped  
`top_open_ports_arr.protocol` | `additional.fields.value.string_value` | Directly mapped  
`top_open_ports_arr.protocol_text` | `additional.fields.value.string_value` | Directly mapped  
`top_open_ports_arr.service` | `additional.fields.value.string_value` | Directly mapped  
`top_peers_arr.event_count` | `additional.fields.value.string_value` | Directly mapped  
`top_peers_arr.ip` | `additional.fields.value.string_value` | Directly mapped  
`used_foundation_queries` | `additional.fields.value.string_value` | Directly mapped  
`used_foundation_queries_percentage` | `additional.fields.value.string_value` | Directly mapped  
`used_queries` | `additional.fields.value.string_value` | Directly mapped  
`used_queries_percentage` | `additional.fields.value.string_value` | Directly mapped  
`val.as_name` | `additional.fields.value.string_value` | Directly mapped  
`val.asn` | `additional.fields.value.string_value` | Directly mapped  
`val.id` | `additional.fields.value.string_value` | Directly mapped  
`val.message` | `additional.fields.value.string_value` | Directly mapped  
`val.name` | `additional.fields.value.string_value` | Directly mapped  
`val.rating` | `additional.fields.value.string_value` | Directly mapped  
`whois.about_contact_address` | `additional.fields.value.string_value` | Directly mapped  
`whois.about_contact_city` | `additional.fields.value.string_value` | Directly mapped  
`whois.about_contact_country` | `additional.fields.value.string_value` | Directly mapped  
`whois.about_contact_email` | `additional.fields.value.string_value` | Directly mapped  
`whois.about_contact_person` | `additional.fields.value.string_value` | Directly mapped  
`whois.about_contact_phone` | `additional.fields.value.string_value` | Directly mapped  
`whois.about_contact_role` | `additional.fields.value.string_value` | Directly mapped  
`whois.abuse_contact_id` | `additional.fields.value.string_value` | Directly mapped  
`whois.admin_contact_city` | `additional.fields.value.string_value` | Directly mapped  
`whois.admin_contact_country` | `additional.fields.value.string_value` | Directly mapped  
`whois.admin_contact_email` | `additional.fields.value.string_value` | Directly mapped  
`whois.admin_contact_id` | `additional.fields.value.string_value` | Directly mapped  
`whois.admin_contact_person` | `additional.fields.value.string_value` | Directly mapped  
`whois.admin_contact_phone` | `additional.fields.value.string_value` | Directly mapped  
`whois.admin_contact_role` | `additional.fields.value.string_value` | Directly mapped  
`whois.cidr` | `additional.fields.value.string_value` | Directly mapped  
`whois.description` | `additional.fields.value.string_value` | Directly mapped  
`whois.mnt_by_email` | `additional.fields.value.string_value` | Directly mapped  
`whois.mnt_lower_email` | `additional.fields.value.string_value` | Directly mapped  
`whois.mnt_router_email` | `additional.fields.value.string_value` | Directly mapped  
`whois.modified` | `additional.fields.value.string_value` | Directly mapped  
`whois.net_handle` | `additional.fields.value.string_value` | Directly mapped  
`whois.org_address` | `additional.fields.value.string_value` | Directly mapped  
`whois.org_city` | `additional.fields.value.string_value` | Directly mapped  
`whois.org_email` | `additional.fields.value.string_value` | Directly mapped  
`whois.org_id` | `additional.fields.value.string_value` | Directly mapped  
`whois.org_phone` | `additional.fields.value.string_value` | Directly mapped  
`whois.tech_contact_address` | `additional.fields.value.string_value` | Directly mapped  
`whois.tech_contact_city` | `additional.fields.value.string_value` | Directly mapped  
`whois.tech_contact_country` | `additional.fields.value.string_value` | Directly mapped  
`whois.tech_contact_email` | `additional.fields.value.string_value` | Directly mapped  
`whois.tech_contact_id` | `additional.fields.value.string_value` | Directly mapped  
`whois.tech_contact_person` | `additional.fields.value.string_value` | Directly mapped  
`whois.tech_contact_phone` | `additional.fields.value.string_value` | Directly mapped  
`whois.tech_contact_role` | `additional.fields.value.string_value` | Directly mapped  
`x509.event_count` | `additional.fields.value.string_value` | Directly mapped  
`x509_arr.common_name` | `additional.fields.value.string_value` | Directly mapped  
`x509_arr.count` | `additional.fields.value.string_value` | Directly mapped  
`x509_arr.first_seen` | `additional.fields.value.string_value` | Directly mapped  
`x509_arr.human_readable` | `additional.fields.value.string_value` | Directly mapped  
`x509_arr.ip` | `additional.fields.value.string_value` | Directly mapped  
`x509_arr.issuer` | `additional.fields.value.string_value` | Directly mapped  
`x509_arr.issuer_common_name` | `additional.fields.value.string_value` | Directly mapped  
`x509_arr.last_seen` | `additional.fields.value.string_value` | Directly mapped  
`x509_arr.md5` | `additional.fields.value.string_value` | Directly mapped  
`x509_arr.not_after` | `additional.fields.value.string_value` | Directly mapped  
`x509_arr.not_before` | `additional.fields.value.string_value` | Directly mapped  
`x509_arr.port` | `additional.fields.value.string_value` | Directly mapped  
`x509_arr.self_signed` | `additional.fields.value.string_value` | Directly mapped  
`x509_arr.serial` | `additional.fields.value.string_value` | Directly mapped  
`x509_arr.sha1` | `additional.fields.value.string_value` | Directly mapped  
`x509_arr.sha256` | `additional.fields.value.string_value` | Directly mapped  
`x509_arr.subject` | `additional.fields.value.string_value` | Directly mapped  
`x509_arr.validity_period` | `additional.fields.value.string_value` | Directly mapped  
`summary.last_seen` | `entity.domain.last_seen_time` | Parsed as `yyyy-MM-dd`  
`summary.whois.net_name` | `entity.domain.whois_server` | Directly mapped  
`indicator` | `entity.hostname` | Directly mapped  
`ip` | `entity.ip` | Merged  
`country_code` | `entity.location.country_or_region` | Directly mapped  
`summary.geo_ip_cc` | `entity.location.country_or_region` | Directly mapped  
`summary.whois.org_name` | `entity.network.organization_name` | Directly mapped  
`end_date` | `metadata.interval.end_time` | Parsed as `yyyy-MM-dd`  
`interval_end` | `metadata.interval.end_time` | Parsed as `yyyy-MM-dd`  
`interval_start` | `metadata.interval.start_time` | Parsed as `yyyy-MM-dd`  
`start_date` | `metadata.interval.start_time` | Parsed as `yyyy-MM-dd`  
N/A | `additional.fields.key` | Constant: `account_name`  
N/A | `metadata.entity_type` | Constant: `IP_ADDRESS`  
N/A | `metadata.event_type` | Constant: `GENERIC_EVENT`  
N/A | `metadata.product_name` | Constant: `Scout`  
N/A | `metadata.threat.threat_verdict` | Constant: `SUSPICIOUS`  
N/A | `metadata.vendor_name` | Constant: `TeamCymru`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/team-cymru-scout-threatintel-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
