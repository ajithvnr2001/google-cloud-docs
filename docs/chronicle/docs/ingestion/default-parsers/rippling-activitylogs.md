---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/rippling-activitylogs/
title: Collect Rippling activity logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:54:41.850408+00:00
---

# Collect Rippling activity logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/rippling-activitylogs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Rippling activity logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Rippling activity logs to Google Security Operations using Google Cloud Storage. Rippling is a workforce management platform that provides HR, IT, and Finance solutions including payroll, benefits, employee onboarding, device management, and application provisioning. The Company Activity API provides audit logs of administrative and user actions across the Rippling platform.

## Before you begin

Ensure that you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * Privileged access to Rippling (API token with access to Company Activity)



## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `rippling-activity-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Collect Rippling API credentials

  1. Sign in to **Rippling Admin**.
  2. Go to **Search > API Tokens**. 
     * Alternative path: **Settings > Company Settings > API Tokens**.
  3. Click **Create API token**.
  4. Provide the following configuration details: 
     * **Name** : Enter a unique and meaningful name (for example, `Google SecOps GCS Export`).
     * **API version** : Select **Base API (v1)**.
     * **Scopes/Permissions** : Enable **company:activity:read** (required for Company Activity).
  5. Click **Create**.
  6. Copy and save the token value in a secure location. You will use it as a bearer token.

**Note:** The API token will only be displayed once. Store it securely.



## Create service account for Cloud Run function

The Cloud Run function needs a service account with permissions to write to GCS bucket.

### Create service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `rippling-logs-collector-sa`.
     * **Service account description** : Enter `Service account for Cloud Run function to collect Rippling activity logs`.
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
     * **Add principals** : Enter the service account email (for example, `rippling-logs-collector-sa@your-project.iam.gserviceaccount.com`).
     * **Assign roles** : Select **Storage Object Admin**.
  6. Click **Save**.



## Create Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `rippling-activity-trigger`.
     * Leave other settings as default.
  4. Click **Create**.



## Create Cloud Run function to collect logs

The Cloud Run function is triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from Rippling Company Activity API and write them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `rippling-activity-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose the topic `rippling-activity-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select the service account `rippling-logs-collector-sa`.
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value  
---|---  
`GCS_BUCKET` | `rippling-activity-logs`  
`GCS_PREFIX` | `rippling/activity/`  
`STATE_KEY` | `rippling/activity/state.json`  
`RIPPLING_API_TOKEN` | `your-api-token`  
`RIPPLING_ACTIVITY_URL` | `https://api.rippling.com/platform/api/company_activity`  
`LIMIT` | `1000`  
`MAX_PAGES` | `10`  
`LOOKBACK_MINUTES` | `60`  
`END_LAG_SECONDS` | `120`  
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
    from datetime import datetime, timezone, timedelta
    import time
    
    # Initialize HTTP client
    http = urllib3.PoolManager(timeout=urllib3.Timeout(connect=5.0, read=60.0), retries=False)
    
    # Initialize Storage client
    storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    
    @functions_framework.cloud_event
    def main(cloud_event):
        """
        Cloud Run function triggered by Pub/Sub to fetch logs from Rippling Company Activity API and write to GCS.
    
        Args:
            cloud_event: CloudEvent object containing Pub/Sub message
        """
    
        # Get environment variables
        bucket_name = os.environ.get('GCS_BUCKET')
        prefix = os.environ.get('GCS_PREFIX', 'rippling/activity/')
        state_key = os.environ.get('STATE_KEY', 'rippling/activity/state.json')
    
        # Rippling API configuration
        api_token = os.environ.get('RIPPLING_API_TOKEN')
        activity_url = os.environ.get('RIPPLING_ACTIVITY_URL', 'https://api.rippling.com/platform/api/company_activity')
        limit = int(os.environ.get('LIMIT', '1000'))
        max_pages = int(os.environ.get('MAX_PAGES', '10'))
        lookback_minutes = int(os.environ.get('LOOKBACK_MINUTES', '60'))
        end_lag_seconds = int(os.environ.get('END_LAG_SECONDS', '120'))
    
        if not all([bucket_name, api_token]):
            print('Error: Missing required environment variables')
            return
    
        try:
            # Get GCS bucket
            bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
    
            # Load state (last processed timestamp and cursor)
            state = load_state(bucket, state_key)
            since_iso = [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get('since')
            next_cursor = [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get('next')
    
            # Calculate time window
            run_end = datetime.now(timezone.utc) - timedelta(seconds=end_lag_seconds)
            end_iso = run_end.replace(microsecond=0).isoformat().replace('+00:00', 'Z')
    
            if since_iso is None:
                since_iso = iso_from_epoch(time.time() - lookback_minutes * 60)
            else:
                try:
                    since_iso = (parse_iso(since_iso) + timedelta(seconds=1)).replace(microsecond=0).isoformat().replace('+00:00', 'Z')
                except Exception:
                    since_iso = iso_from_epoch(time.time() - lookback_minutes * 60)
    
            print(f'Processing logs from {since_iso} to {end_iso}')
    
            run_ts_iso = end_iso
            pages = 0
            total = 0
            newest_ts = None
            pending_next = None
    
            # Fetch logs with pagination
            while pages < max_pages:
                params = {'limit': str(limit)}
    
                if next_cursor:
                    params['next'] = next_cursor
                else:
                    params['startDate'] = since_iso
                    params['endDate'] = end_iso
    
                # Build URL with query parameters
                url = build_url(activity_url, params)
    
                # Fetch data from Rippling API
                headers = {
                    'Authorization': f'Bearer {api_token}',
                    'Accept': 'application/json'
                }
    
                # Implement exponential backoff for rate limiting
                backoff = 1.0
                max_retries = 3
                retry_count = 0
    
                while retry_count < max_retries:
                    response = http.request('GET', url, headers=headers, timeout=60.0)
    
                    if response.status == 429:
                        retry_after = int(response.headers.get('Retry-After', str(int(backoff))))
                        print(f'Rate limited (429). Retrying after {retry_after}s...')
                        time.sleep(retry_after)
                        backoff = min(backoff * 2, 30.0)
                        retry_count += 1
                        continue
    
                    break
    
                if response.status != 200:
                    print(f'Error: API returned status {response.status}')
                    break
    
                data = json.loads(response.data.decode('utf-8'))
    
                # Write page to GCS
                write_to_gcs(bucket, prefix, data, run_ts_iso, pages)
    
                # Extract events
                events = data.get('events') or []
                total += len(events) if isinstance(events, list) else 0
    
                # Track newest timestamp
                if isinstance(events, list):
                    for ev in events:
                        t = ev.get('timestamp') or ev.get('time') or ev.get('event_time')
                        if isinstance(t, str):
                            try:
                                dt_ts = parse_iso(t)
                                if newest_ts is None or dt_ts > newest_ts:
                                    newest_ts = dt_ts
                            except Exception:
                                pass
    
                # Check for next page
                nxt = data.get('next')
                pages += 1
    
                if nxt:
                    next_cursor = nxt
                    pending_next = nxt
                    continue
                else:
                    pending_next = None
                    break
    
            # Update state
            new_since_iso = (newest_ts or run_end).replace(microsecond=0).isoformat().replace('+00:00', 'Z')
            save_state(bucket, state_key, {'since': new_since_iso, 'next': pending_next})
    
            print(f'Successfully processed {total} events across {pages} pages')
            print(f'Updated state: since={new_since_iso}, next={pending_next}')
    
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
    
    def write_to_gcs(bucket, prefix, payload, run_ts_iso, page_index):
        """Write payload to GCS."""
        try:
            day_path = parse_iso(run_ts_iso).strftime('%Y/%m/%d')
            key = f"{prefix.strip('/')}/{day_path}/{run_ts_iso.replace(':', '').replace('-', '')}-page{page_index:05d}-company_activity.json"
    
            blob = bucket.blob(key)
            blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
                json.dumps(payload, separators=(',', ':')),
                content_type='application/json'
            )
            print(f'Wrote page {page_index} to {key}')
        except Exception as e:
            print(f'Error writing to GCS: {str(e)}')
            raise
    
    def parse_iso(ts):
        """Parse ISO 8601 timestamp."""
        if ts.endswith('Z'):
            ts = ts[:-1] + '+00:00'
        return datetime.fromisoformat(ts)
    
    def iso_from_epoch(sec):
        """Convert epoch seconds to ISO 8601 timestamp."""
        return datetime.fromtimestamp(sec, tz=timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')
    
    def build_url(base, params):
        """Build URL with query parameters."""
        if not params:
            return base
        query_string = '&'.join([f'{k}={v}' for k, v in params.items()])
        return f'{base}?{query_string}'
    

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
**Name** | `rippling-activity-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the topic `rippling-activity-trigger`  
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



### Test the scheduler job

  1. In the **Cloud Scheduler** console, find your job.
  2. Click **Force run** to trigger manually.
  3. Wait a few seconds and go to **Cloud Run > Services > rippling-activity-collector > Logs**.
  4. Verify the function executed successfully.
  5. Check the GCS bucket to confirm logs were written.



## Retrieve the Google SecOps service account

Google SecOps uses a unique service account to read data from your GCS bucket. You must grant this service account access to your bucket.

### Get the service account email

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Rippling Activity Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Rippling Activity Logs** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
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



## Configure a feed in Google SecOps to ingest Rippling Activity Logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Rippling Activity Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Rippling Activity Logs** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://rippling-activity-logs/rippling/activity/
           

       * Replace:

         * `rippling-activity-logs`: Your GCS bucket name.
         * `rippling/activity/`: Prefix/folder path where logs are stored (must match `GCS_PREFIX` environment variable).
**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never** : Never deletes any files after transfers (recommended for testing).
       * **Delete transferred files** : Deletes files after successful transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.

**Note:** If you select a deletion option, the service account must have **Storage Object Admin** role instead of Storage Object Viewer. Update IAM permissions accordingly.
     * **Maximum File Age** : Include files modified in the last number of days. Default is 180 days.

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces) (for example, `rippling.activity`).

     * **Ingestion labels** : Optional label to be applied to the events from this feed.

  9. Click **Next**.

  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
`accuracy_radius_label` | `additional.fields` | Merged  
`company_label` | `additional.fields` | Merged  
`finger_label` | `additional.fields` | Merged  
`linked_events_key_label` | `additional.fields` | Merged  
`owner_label` | `additional.fields` | Merged  
`processing_state_label` | `additional.fields` | Merged  
`spoke_label` | `additional.fields` | Merged  
`subject_version_label` | `additional.fields` | Merged  
`has_target` | `extensions.auth.type` | Mapped: `true` → `PHYSICAL`  
`event_type` | `metadata.event_type` | Directly mapped  
`name` | `metadata.product_event_type` | Directly mapped  
`prop_id` | `metadata.product_log_id` | Directly mapped  
`data.request_data.authentication_context.login_username` | `network.email.mail_id` | Directly mapped  
`data.request_data.authentication_context.mfa_method` | `network.http.method` | Directly mapped  
`data.request_data.authentication_context.login_agent` | `network.http.user_agent` | Directly mapped  
`data.initiator.display_name` | `principal.asset.hostname` | Directly mapped  
`data.search_string` | `principal.asset.hostname` | Directly mapped  
`subjects.display_name` | `principal.asset.hostname` | Directly mapped  
`data.initiator.display_name` | `principal.hostname` | Directly mapped  
`data.search_string` | `principal.hostname` | Directly mapped  
`subjects.display_name` | `principal.hostname` | Directly mapped  
`data.initiator.icon` | `principal.url` | Directly mapped  
`subjects.icon` | `principal.url` | Directly mapped  
`data.initiator.email` | `principal.user.email_addresses` | Merged  
`emailid` | `principal.user.email_addresses` | Mapped: `^.+@.+$` → `data.initiator.email`  
`data._subject_group_name_cache` | `principal.user.group_identifiers` | Merged  
`data._subject_role_name_cache` | `principal.user.role_name` | Directly mapped  
`data.initiator.role` | `principal.user.userid` | Directly mapped  
`data.subject_group` | `principal.user.userid` | Directly mapped  
`subjects.instance` | `principal.user.userid` | Directly mapped  
`data.event_reason.reason` | `security_result.category_details` | Merged  
`data.event_reason.message` | `security_result.summary` | Directly mapped  
`data.request_data.os` | `src.platform_version` | Directly mapped  
`data.request_data.ip` | `target.asset.ip` | Merged  
`data.request_data.ip` | `target.ip` | Merged  
`data.request_data.city` | `target.location.city` | Directly mapped  
`data.request_data.country` | `target.location.country_or_region` | Directly mapped  
`geo_latitude` | `target.location.region_latitude` | Renamed/mapped  
`geo_longitude` | `target.location.region_longitude` | Renamed/mapped  
`data.request_data.state` | `target.location.state` | Directly mapped  
N/A | `extensions.auth.type` | Constant: `PHYSICAL`  
N/A | `metadata.product_name` | Constant: `RIPPLING_ACTIVITYLOGS`  
N/A | `metadata.vendor_name` | Constant: `RIPPLING_ACTIVITYLOGS`  
N/A | `src.platform` | Constant: `MAC`  
N/A | `target.resource.resource_type` | Constant: `TASK`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/rippling-activitylogs-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
