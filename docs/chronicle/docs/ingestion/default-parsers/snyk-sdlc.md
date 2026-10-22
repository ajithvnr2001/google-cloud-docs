---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/snyk-sdlc/
title: Collect Snyk group-level audit logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:35:58.388450+00:00
---

# Collect Snyk group-level audit logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/snyk-sdlc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Snyk group-level audit logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Snyk group-level audit logs to Google Security Operations using Google Cloud Storage. The parser first cleans up unnecessary fields from the raw logs. Then, it extracts relevant information like user details, event type, and timestamps, transforming and mapping them into the Google SecOps UDM schema for standardized security log representation.

## Before you begin

Ensure that you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * Privileged access to Snyk (Group Admin) and an API token with access to the Group
  * Snyk Enterprise plan (audit logs endpoints are only available on Enterprise plans)



## Collect Snyk Group level audit logs prerequisites (IDs, API keys, org IDs, tokens)

  1. In Snyk, click your avatar > **Account settings** > **API token**.
  2. Click **Revoke & regenerate** (or **Generate**) and copy the token.
  3. Save this token as the `SNYK_API_TOKEN` environment variable.
  4. In Snyk, switch to your Group (top-left switcher).
  5. Go to **Group settings**.
  6. Copy the `<GROUP_ID>` from the URL: `https://app.snyk.io/group/<GROUP_ID>/settings`. 
     * Or use REST API: `GET https://api.snyk.io/rest/groups?version=2024-01-04` and pick the `id`.
  7. Ensure the token user has **View Audit Logs** (`group.audit.read`) permission.



### Verify permissions

To verify the account has the required permissions:

  1. Sign in to Snyk.
  2. Switch to your Group (top-left switcher).
  3. Go to **Group settings**.
  4. If you can see the **Audit logs** option in the left navigation, you have the required permissions.
  5. If you cannot see this option, contact your administrator to grant **View Audit Logs** (`group.audit.read`) permission.

**Note:** Audit logs endpoints require a Snyk Enterprise plan. If API calls fail with 403 errors despite correct configuration, verify your subscription level.



### Test API access

  * Test your credentials before proceeding with the integration:
        
        # Replace with your actual credentials
        SNYK_API_TOKEN="your-token-here"
        SNYK_GROUP_ID="your-group-id-here"
        SNYK_API_VERSION="2024-01-04"
        
        # Test API access
        curl -v -H "Authorization: token ${SNYK_API_TOKEN}" \
          "https://api.snyk.io/rest/groups/${SNYK_GROUP_ID}/audit_logs/search?version=${SNYK_API_VERSION}&size=10"
        




## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `snyk-audit`)  
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
     * **Service account name** : Enter `snyk-audit-collector-sa`.
     * **Service account description** : Enter `Service account for Cloud Run function to collect Snyk group-level audit logs`.
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
  2. Click your bucket name (for example, `snyk-audit`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `snyk-audit-collector-sa@PROJECT_ID.iam.gserviceaccount.com`).
     * **Assign roles** : Select **Storage Object Admin**.
  6. Click **Save**.



## Create Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `snyk-audit-trigger`.
     * Leave other settings as default.
  4. Click **Create**.



## Create Cloud Run function to collect logs

The Cloud Run function is triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from Snyk API and writes them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `snyk-audit-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose the Pub/Sub topic (`snyk-audit-trigger`).
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub automatically handles authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select the service account (`snyk-audit-collector-sa`).
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value  
---|---  
`GCS_BUCKET` | `snyk-audit`  
`GCS_PREFIX` | `snyk/audit/`  
`STATE_KEY` | `snyk/audit/state.json`  
`SNYK_GROUP_ID` | `<your_group_id>`  
`SNYK_API_TOKEN` | `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`  
`SNYK_API_BASE` | `https://api.snyk.io` (optional)  
`SNYK_API_VERSION` | `2024-01-04`  
`SIZE` | `100`  
`MAX_PAGES` | `20`  
`LOOKBACK_SECONDS` | `3600`  
`EVENTS` | (optional) `group.create,org.user.add`  
`EXCLUDE_EVENTS` | (optional) `api.access`  
**Note:** The `SNYK_API_VERSION` value should match the current recommended version from Snyk's Audit Logs API documentation. Check Snyk's documentation periodically to ensure you are using the latest stable version.
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
    import time
    import urllib.parse
    
    # Initialize HTTP client
    http = urllib3.PoolManager()
    
    # Initialize Storage client
    storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    
    @functions_framework.cloud_event
    def main(cloud_event):
        """
        Cloud Run function triggered by Pub/Sub to fetch Snyk group-level audit logs and write to GCS.
    
        Args:
            cloud_event: CloudEvent object containing Pub/Sub message
        """
    
        # Get environment variables
        bucket_name = os.environ.get('GCS_BUCKET')
        prefix = os.environ.get('GCS_PREFIX', 'snyk/audit/')
        state_key = os.environ.get('STATE_KEY', 'snyk/audit/state.json')
    
        # Snyk API configuration
        api_base = os.environ.get('SNYK_API_BASE', 'https://api.snyk.io').rstrip('/')
        group_id = os.environ.get('SNYK_GROUP_ID', '').strip()
        api_token = os.environ.get('SNYK_API_TOKEN', '').strip()
        api_version = os.environ.get('SNYK_API_VERSION', '2024-01-04').strip()
    
        size = int(os.environ.get('SIZE', '100'))
        max_pages = int(os.environ.get('MAX_PAGES', '20'))
        lookback_seconds = int(os.environ.get('LOOKBACK_SECONDS', '3600'))
    
        events_csv = os.environ.get('EVENTS', '').strip()
        exclude_events_csv = os.environ.get('EXCLUDE_EVENTS', '').strip()
    
        if not all([bucket_name, group_id, api_token]):
            print('Error: Missing required environment variables')
            return
    
        try:
            # Get GCS bucket
            bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
    
            # Load state (last cursor)
            state = load_state(bucket, state_key)
            cursor = [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get('cursor')
    
            print(f'Starting log collection with cursor: {cursor}')
    
            # Prepare headers for Snyk REST API
            headers = {
                'Authorization': f'token {api_token}',
                'Accept': 'application/vnd.api+json'
            }
    
            pages = 0
            total = 0
            last_cursor = cursor
    
            # Only for the very first run (no saved cursor), constrain the time window
            first_run_from_iso = None
            if not cursor and lookback_seconds > 0:
                first_run_from_iso = time.strftime(
                    '%Y-%m-%dT%H:%M:%SZ',
                    time.gmtime(time.time() - lookback_seconds)
                )
    
            while pages < max_pages:
                payload = fetch_page(
                    api_base, group_id, headers, api_version, size,
                    cursor, first_run_from_iso, events_csv, exclude_events_csv
                )
    
                # Write payload to GCS
                write_to_gcs(bucket, prefix, payload)
    
                # Extract items count
                data_obj = payload.get('data') or {}
                items = data_obj.get('items') or []
                if isinstance(items, list):
                    total += len(items)
    
                # Parse next cursor
                cursor = parse_next_cursor_from_links(payload.get('links'))
                pages += 1
    
                if not cursor:
                    break
    
                # After first page, disable from-filter
                first_run_from_iso = None
    
            # Save state
            if cursor and cursor != last_cursor:
                save_state(bucket, state_key, {'cursor': cursor})
    
            print(f'Successfully processed {total} events across {pages} pages. Next cursor: {cursor}')
    
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
                json.dumps(state),
                content_type='application/json'
            )
        except Exception as e:
            print(f'Warning: Could not save state: {str(e)}')
    
    def write_to_gcs(bucket, prefix, payload):
        """Write payload to GCS."""
        ts = time.strftime('%Y/%m/%d/%H%M%S', time.gmtime())
        key = f"{prefix.rstrip('/')}/{ts}-snyk-group-audit.json"
        blob = bucket.blob(key)
        blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
            json.dumps(payload, separators=(',', ':')),
            content_type='application/json'
        )
        print(f'Wrote payload to {key}')
    
    def parse_next_cursor_from_links(links):
        """Parse next cursor from links object."""
        if not links:
            return None
        nxt = links.get('next')
        if not nxt:
            return None
        try:
            q = urllib.parse.urlparse(nxt).query
            params = urllib.parse.parse_qs(q)
            cur = params.get('cursor')
            return cur[0] if cur else None
        except Exception:
            return None
    
    def as_list(csv_str):
        """Convert comma-separated string to list."""
        return [x.strip() for x in csv_str.split(',') if x.strip()]
    
    def fetch_page(api_base, group_id, headers, api_version, size, cursor, first_run_from_iso, events_csv, exclude_events_csv):
        """Fetch a single page from Snyk audit logs API."""
        base_path = f'/rest/groups/{group_id}/audit_logs/search'
        params = {
            'version': api_version,
            'size': size,
        }
    
        if cursor:
            params['cursor'] = cursor
        elif first_run_from_iso:
            params['from'] = first_run_from_iso
    
        events = as_list(events_csv)
        exclude_events = as_list(exclude_events_csv)
    
        if events and exclude_events:
            exclude_events = []
    
        if events:
            params['events'] = events
        if exclude_events:
            params['exclude_events'] = exclude_events
    
        url = f"{api_base}{base_path}?{urllib.parse.urlencode(params, doseq=True)}"
    
        response = http.request('GET', url, headers=headers, timeout=60.0)
    
        if response.status == 429 or response.status >= 500:
            retry_after = int(response.headers.get('Retry-After', '1'))
            time.sleep(max(1, retry_after))
            response = http.request('GET', url, headers=headers, timeout=60.0)
    
        if response.status != 200:
            raise Exception(f'API request failed with status {response.status}: {response.data.decode("utf-8")}')
    
        return json.loads(response.data.decode('utf-8'))
    

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
**Name** | `snyk-audit-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the Pub/Sub topic (`snyk-audit-trigger`)  
**Message body** | `{}`  
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

  1. In the **Cloud Scheduler** console, find your job (`snyk-audit-collector-hourly`).
  2. Click **Force run** to trigger the job manually.
  3. Wait a few seconds.
  4. Go to **Cloud Run > Services**.
  5. Click on the function name (`snyk-audit-collector`).
  6. Click the **Logs** tab.
  7. Verify the function executed successfully. Look for the following:
         
         Starting log collection with cursor: None
         Page 1: Retrieved X events
         Wrote payload to snyk/audit/YYYY/MM/DD/HHMMSS-snyk-group-audit.json
         Successfully processed X events across Y pages. Next cursor: ...
         

  8. Go to **Cloud Storage > Buckets**.

  9. Click your bucket name (for example, `snyk-audit`).

  10. Navigate to the prefix folder (`snyk/audit/`).

  11. Verify that a new `.json` file was created with the current timestamp.




If you see errors in the logs:

  * **HTTP 401** : Check `SNYK_API_TOKEN` in environment variables
  * **HTTP 403** : Verify the token user has `group.audit.read` permission and that your Snyk subscription is an Enterprise plan
  * **HTTP 429** : Rate limiting - function will automatically retry with backoff
  * **Missing environment variables** : Check all required variables are set (`GCS_BUCKET`, `SNYK_GROUP_ID`, `SNYK_API_TOKEN`)



## Retrieve the Google SecOps service account

Google SecOps uses a unique service account to read data from your GCS bucket. You must grant this service account access to your bucket.

### Get the service account email

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Snyk Group Audit Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Snyk Group level audit Logs** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email is displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Do not use service accounts from other documentation or examples.



## Grant IAM permissions to the Google SecOps service account

The Google SecOps service account needs **Storage Object Viewer** role on your GCS bucket.

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name (for example, `snyk-audit`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Paste the Google SecOps service account email.
     * **Assign roles** : Select **Storage Object Viewer**.
  6. Click **Save**.

**Note:** If you plan to use the deletion option "Delete transferred files" or "Delete transferred files and empty directories," grant **Storage Object Admin** role instead of Storage Object Viewer.



## Configure a feed in Google SecOps to ingest Snyk Group level audit Logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Snyk Group Audit Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Snyk Group level audit Logs** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://snyk-audit/snyk/audit/
           

       * Replace:

         * `snyk-audit`: Your GCS bucket name.
         * `snyk/audit/`: Prefix/folder path where logs are stored.
**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never** : Never deletes any files after transfers (recommended for testing).
       * **Delete transferred files** : Deletes files after successful transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.

**Note:** If you select a deletion option, the service account must have **Storage Object Admin** role instead of Storage Object Viewer. Update IAM permissions accordingly.
     * **Maximum File Age** : Include files modified in the last number of days. Default is 180 days.

     * **Asset namespace** : `snyk.group_audit`

     * **Ingestion labels** : Add if desired.

  9. Click **Next**.

  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
content.url | principal.url | Directly mapped from the content.url field in the raw log.  
created | metadata.event_timestamp | Parsed from the created field in the raw log using the ISO8601 format.  
event | metadata.product_event_type | Directly mapped from the event field in the raw log.  
groupId | principal.user.group_identifiers | Directly mapped from the groupId field in the raw log.  
orgId | principal.user.attribute.labels.key | Set to "orgId".  
orgId | principal.user.attribute.labels.value | Directly mapped from the orgId field in the raw log.  
userId | principal.user.userid | Directly mapped from the userId field in the raw log.  
N/A | metadata.event_type | Hardcoded to "USER_UNCATEGORIZED" in the parser code.  
N/A | metadata.log_type | Hardcoded to "SNYK_SDLC" in the parser code.  
N/A | metadata.product_name | Hardcoded to "SNYK SDLC" in the parser code.  
N/A | metadata.vendor_name | Hardcoded to "SNYK_SDLC" in the parser code.  
`jsonapi_version` | `event.idm.read_only_udm.metadata.product_version` | Mapped from changelog  
`data_type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`file` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`requestId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`hostname` | `event.idm.read_only_udm.principal.hostname` | Mapped from changelog  
`projectName` | `event.idm.read_only_udm.principal.resource.name` | Mapped from changelog  
`target_remote_url` | `event.idm.read_only_udm.target.url` | Mapped from changelog  
`targetFile` | `event.idm.read_only_udm.target.file.full_path` | Mapped from changelog  
`project_id` | `event.idm.read_only_udm.target.user.attribute.labels` | Mapped from changelog  
`field_check` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`group_id` | `event.idm.read_only_udm.principal.user.group_identifiers` | Mapped from changelog  
`org_id` | `event.idm.read_only_udm.principal.user.attribute.labels` | Mapped from changelog  
`user_id` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`event` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`created` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`snyk_request_id` | `additional.fields` | Mapped from changelog  
`http_method_details` | `network.http.method_details` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/snyk-sdlc-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
