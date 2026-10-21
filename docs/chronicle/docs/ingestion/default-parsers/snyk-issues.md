---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/snyk-issues/
title: Collect Snyk Group Issues logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:23:00.699605+00:00
---

# Collect Snyk Group Issues logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/snyk-issues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Snyk Group Issues logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Snyk Group Issues logs to Google Security Operations using Google Cloud Storage. Snyk is a developer security platform that helps organizations find and fix vulnerabilities in open source dependencies, container images, infrastructure as code configurations, and application code. Snyk Group Issues provide visibility into security vulnerabilities and license issues across all projects within a Snyk Group.

## Before you begin

Ensure that you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run functions, Pub/Sub topics, and Cloud Scheduler jobs
  * Privileged access to Snyk Group (API token with read access; Group ID)
  * Snyk Group Admin role assigned to the user with the API token (the user must be able to view Group Audit Logs and Group Issues)



## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `snyk-group-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Collect Snyk Group ID and API token

### Get Snyk API token

  1. Sign in to the Snyk UI at <https://app.snyk.io>.
  2. Go to **Account settings > API token**.
  3. Click **Generate** to generate the API token.
  4. Copy and save the token in a secure location to later use as `SNYK_TOKEN`.

**Note:** This token will be used by the Cloud Run function to authenticate to the Snyk API.



### Get Snyk Group ID

  1. In the Snyk UI, switch to your Group.
  2. Go to **Group settings**.
  3. Copy and save the Group ID from the URL (`https://app.snyk.io/group/<GROUP_ID>/...`) to later use as `GROUP_ID`.



### Assign Group Admin role

  1. In the Snyk UI, go to **Group settings > Members**.
  2. Locate the user associated with the API token.
  3. Assign the **Group Admin** role to the user.

**Note:** The user must be able to view Group Audit Logs and Group Issues.



### Note API endpoint

  * The REST API base endpoint varies by region. Identify your Snyk region and note the corresponding REST base URL:

Region | REST Base URL  
---|---  
SNYK-US-01 | `https://api.snyk.io/rest`  
SNYK-US-02 | `https://api.us.snyk.io/rest`  
SNYK-EU-01 | `https://api.eu.snyk.io/rest`  
SNYK-AU-01 | `https://api.au.snyk.io/rest`  
  
You will use this REST base URL as `API_BASE` in the Cloud Run function configuration. The function code constructs full endpoint URLs by appending paths like `/groups/{group_id}/audit_logs/search` to this base URL.

**Note:** Snyk audit logs endpoints are available only for Enterprise plans. Verify your plan includes access to Group audit logs and that your account has appropriate retention limits configured.



## Create service account for Cloud Run function

The Cloud Run function needs a service account with permissions to write to GCS bucket.

### Create service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `snyk-logs-collector-sa`.
     * **Service account description** : Enter `Service account for Cloud Run function to collect Snyk Group logs`.
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
     * **Add principals** : Enter the service account email (for example, `snyk-logs-collector-sa@PROJECT_ID.iam.gserviceaccount.com`).
     * **Assign roles** : Select **Storage Object Admin**.
  6. Click **Save**.



## Create Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `snyk-logs-trigger`.
     * Leave other settings as default.
  4. Click **Create**.



## Create Cloud Run function to collect logs

The Cloud Run function is triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from Snyk Group API and writes them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `snyk-group-logs-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose the topic `snyk-logs-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check **Identity and Access Management (IAM)**.
**Note:** Pub/Sub automatically handles authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select the service account `snyk-logs-collector-sa`.
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value  
---|---  
`GCS_BUCKET` | `snyk-group-logs`  
`GCS_PREFIX` | `snyk/group/`  
`STATE_KEY` | `snyk/group/state.json`  
`SNYK_TOKEN` | `your-snyk-api-token`  
`GROUP_ID` | `your-group-uuid`  
`API_BASE` | `https://api.snyk.io/rest`  
`SNYK_AUDIT_API_VERSION` | `2024-10-15`  
`SNYK_ISSUES_API_VERSION` | `2024-10-15`  
`AUDIT_PAGE_SIZE` | `100`  
`ISSUES_PAGE_LIMIT` | `100`  
`MAX_PAGES` | `20`  
`LOOKBACK_SECONDS` | `3600`  
**Note:** Set `API_BASE` to the correct REST base URL for your Snyk region. For SNYK-US-01, use `https://api.snyk.io/rest`. For SNYK-EU-01, use `https://api.eu.snyk.io/rest`. For SNYK-US-02, use `https://api.us.snyk.io/rest`. For SNYK-AU-01, use `https://api.au.snyk.io/rest`.
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
               import time
               import urllib.parse
               from urllib.request import Request, urlopen
               from urllib.parse import urlparse, parse_qs
               from urllib.error import HTTPError
           
               # Initialize Storage client
               storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
           
               @functions_framework.cloud_event
               def main(cloud_event):
                   """
                   Cloud Run function triggered by Pub/Sub to fetch logs from Snyk Group API and write to GCS.
           
                   Args:
                       cloud_event: CloudEvent object containing Pub/Sub message
                   """
           
                   # Get environment variables
                   bucket_name = os.environ.get('GCS_BUCKET')
                   prefix = os.environ.get('GCS_PREFIX', 'snyk/group/').strip()
                   state_key = os.environ.get('STATE_KEY', 'snyk/group/state.json').strip()
           
                   # Snyk API credentials
                   api_base = os.environ.get('API_BASE', 'https://api.snyk.io/rest').rstrip('/')
                   snyk_token = os.environ.get('SNYK_TOKEN').strip()
                   group_id = os.environ.get('GROUP_ID').strip()
           
                   # Page sizes & limits
                   audit_size = int(os.environ.get('AUDIT_PAGE_SIZE', '100'))
                   issues_limit = int(os.environ.get('ISSUES_PAGE_LIMIT', '100'))
                   max_pages = int(os.environ.get('MAX_PAGES', '20'))
           
                   # API versions
                   audit_api_version = os.environ.get('SNYK_AUDIT_API_VERSION', '2024-10-15').strip()
                   issues_api_version = os.environ.get('SNYK_ISSUES_API_VERSION', '2024-10-15').strip()
           
                   # First-run lookback
                   lookback_seconds = int(os.environ.get('LOOKBACK_SECONDS', '3600'))
           
                   if not all([bucket_name, snyk_token, group_id]):
                       print('Error: Missing required environment variables')
                       return
           
                   try:
                       # Get GCS bucket
                       bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
           
                       # Load state
                       state = load_state(bucket, state_key)
           
                       print('Starting Snyk Group logs collection')
           
                       # Pull audit logs
                       audit_res = pull_audit_logs(
                           bucket, prefix, state, api_base, snyk_token, group_id,
                           audit_api_version, audit_size, max_pages, lookback_seconds
                       )
                       print(f"Audit logs: {audit_res}")
           
                       # Pull issues
                       issues_res = pull_issues(
                           bucket, prefix, state, api_base, snyk_token, group_id,
                           issues_api_version, issues_limit, max_pages
                       )
                       print(f"Issues: {issues_res}")
           
                       # Save state
                       save_state(bucket, state_key, state)
           
                       print('Successfully completed Snyk Group logs collection')
           
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
           
               def _iso(ts):
                   """Convert timestamp to ISO format."""
                   return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(ts))
           
               def _http_get(url, headers):
                   """Make HTTP GET request with retry logic."""
                   req = Request(url, method='GET', headers=headers)
                   try:
                       with urlopen(req, timeout=60) as r:
                           return json.loads(r.read().decode('utf-8'))
                   except HTTPError as e:
                       if e.code in (429, 500, 502, 503, 504):
                           delay = int(e.headers.get('Retry-After', '1'))
                           time.sleep(max(1, delay))
                           with urlopen(req, timeout=60) as r2:
                               return json.loads(r2.read().decode('utf-8'))
                       raise
           
               def _write_page(bucket, prefix, kind, payload):
                   """Write page to GCS."""
                   ts = time.gmtime()
                   key = f"{prefix.rstrip('/')}/{time.strftime('%Y/%m/%d/%H%M%S', ts)}-snyk-{kind}.json"
                   blob = bucket.blob(key)
                   blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
                       json.dumps(payload, separators=(',', ':')),
                       content_type='application/json'
                   )
                   return key
           
               def _next_href(links):
                   """Extract next href from links."""
                   if not links:
                       return None
                   nxt = links.get('next')
                   if not nxt:
                       return None
                   if isinstance(nxt, str):
                       return nxt
                   if isinstance(nxt, dict):
                       return nxt.get('href')
                   return None
           
               def pull_audit_logs(bucket, prefix, state, api_base, snyk_token, group_id,
                                   audit_api_version, audit_size, max_pages, lookback_seconds):
                   """Pull audit logs from Snyk Group API."""
                   headers = {
                       'Authorization': f'token {snyk_token}',
                       'Accept': 'application/vnd.api+json',
                   }
           
                   cursor = [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get('audit_cursor')
                   pages = 0
                   total = 0
                   base = f"{api_base}/groups/{group_id}/audit_logs/search"
                   params = {
                       'version': audit_api_version,
                       'size': audit_size
                   }
           
                   if cursor:
                       params['cursor'] = cursor
                   else:
                       now = time.time()
                       params['from'] = _iso(now - lookback_seconds)
                       params['to'] = _iso(now)
           
                   while pages < max_pages:
                       url = f"{base}?{urllib.parse.urlencode(params, doseq=True)}"
                       payload = _http_get(url, headers)
                       _write_page(bucket, prefix, 'audit', payload)
           
                       data_items = (payload.get('data') or {}).get('items') or []
                       if isinstance(data_items, list):
                           total += len(data_items)
           
                       nxt = _next_href(payload.get('links'))
                       if not nxt:
                           break
           
                       q = parse_qs(urlparse(nxt).query)
                       cur = (q.get('cursor') or [None])[0]
                       if not cur:
                           break
           
                       params = {
                           'version': audit_api_version,
                           'size': audit_size,
                           'cursor': cur
                       }
                       state['audit_cursor'] = cur
                       pages += 1
           
                   return {
                       'pages': pages + 1 if total else pages,
                       'items': total,
                       'cursor': [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get('audit_cursor')
                   }
           
               def pull_issues(bucket, prefix, state, api_base, snyk_token, group_id,
                               issues_api_version, issues_limit, max_pages):
                   """Pull issues from Snyk Group API."""
                   headers = {
                       'Authorization': f'token {snyk_token}',
                       'Accept': 'application/vnd.api+json',
                   }
           
                   cursor = [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get('issues_cursor')
                   pages = 0
                   total = 0
                   base = f"{api_base}/groups/{group_id}/issues"
                   params = {
                       'version': issues_api_version,
                       'limit': issues_limit
                   }
           
                   if cursor:
                       params['starting_after'] = cursor
           
                   while pages < max_pages:
                       url = f"{base}?{urllib.parse.urlencode(params, doseq=True)}"
                       payload = _http_get(url, headers)
                       _write_page(bucket, prefix, 'issues', payload)
           
                       data_items = payload.get('data') or []
                       if isinstance(data_items, list):
                           total += len(data_items)
           
                       nxt = _next_href(payload.get('links'))
                       if not nxt:
                           break
           
                       q = parse_qs(urlparse(nxt).query)
                       cur = (q.get('starting_after') or [None])[0]
                       if not cur:
                           break
           
                       params = {
                           'version': issues_api_version,
                           'limit': issues_limit,
                           'starting_after': cur
                       }
                       state['issues_cursor'] = cur
                       pages += 1
           
                   return {
                       'pages': pages + 1 if total else pages,
                       'items': total,
                       'cursor': [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get('issues_cursor')
                   }
               ```
           

     * Second file: **requirements.txt:**
           
           functions-framework==3.*
           google-cloud-storage==2.*
           

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
**Name** | `snyk-group-logs-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the topic `snyk-logs-trigger`  
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
  3. Wait a few seconds and go to **Cloud Run > Services > snyk-group-logs-collector > Logs**.
  4. Verify the function executed successfully.
  5. Check the GCS bucket to confirm logs were written.



## Retrieve the Google SecOps service account

Google SecOps uses a unique service account to read data from your GCS bucket. You must grant this service account access to your bucket.

### Get the service account email

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Snyk Group Audit/Issues`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Snyk Group level audit/issues logs** as the **Log type**.
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



## Configure a feed in Google SecOps to ingest Snyk Group logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Snyk Group Audit/Issues`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Snyk Group level audit/issues logs** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://snyk-group-logs/snyk/group/
           

       * Replace:

         * `snyk-group-logs`: Your GCS bucket name.
         * `snyk/group/`: Optional prefix/folder path where logs are stored (leave empty for root).
       * **Examples:**

         * Root bucket: `gs://company-logs/`
         * With prefix: `gs://company-logs/snyk-logs/`
         * With subfolder: `gs://company-logs/snyk/group/`
**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference: 
       * **Never** : Never deletes any files after transfers (recommended for testing).
       * **Delete transferred files** : Deletes files after successful transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.
**Note:** If you select a deletion option, the service account must have **Storage Object Admin** role instead of Storage Object Viewer. Update IAM permissions accordingly.
     * **Maximum File Age** : Include files modified in the last number of days. Default is 180 days.
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces) (for example, `snyk.group`).
     * **Ingestion labels** : The label to be applied to the events from this feed.
  9. Click **Next**.

  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
`gitignore_label` | `additional.fields` | Merged  
`limit_label` | `additional.fields` | Merged  
`version_label` | `additional.fields` | Merged  
`created` | `metadata.event_timestamp` | Parsed as `RFC3339`  
`org_created` | `metadata.event_timestamp` | Parsed as `RFC3339`  
`project_created` | `metadata.event_timestamp` | Parsed as `RFC3339`  
`project_lastTestedDate` | `metadata.event_timestamp` | Parsed as `RFC3339`  
`has_principal` | `metadata.event_type` | Mapped: `true` → `NETWORK_CONNECTION`, `true` → `STATUS_UPDATE`  
`eventdata` | `metadata.product_event_type` | Directly mapped  
`content.http_method` | `network.http.method` | Directly mapped  
`content.requestId` | `network.session_id` | Directly mapped  
`org_name` | `principal.administrative_domain` | Directly mapped  
`snyk_request_id_label` | `principal.resource.attribute.labels` | Merged  
`org_url` | `principal.url` | Directly mapped  
`groupcreated_label` | `principal.user.attribute.labels` | Merged  
`groupname_label` | `principal.user.attribute.labels` | Merged  
`groupurl_label` | `principal.user.attribute.labels` | Merged  
`orgId_label` | `principal.user.attribute.labels` | Merged  
`orggroupid_label` | `principal.user.attribute.labels` | Merged  
`orgslug_label` | `principal.user.attribute.labels` | Merged  
`groupId` | `principal.user.groupid` | Directly mapped  
`org_group_name` | `principal.user.groupid` | Directly mapped  
`issueCountsBySeverity_critical_label` | `security_result.about.labels` | Merged  
`issueCountsBySeverity_high_label` | `security_result.about.labels` | Merged  
`issueCountsBySeverity_low_label` | `security_result.about.labels` | Merged  
`issueCountsBySeverity_medium_label` | `security_result.about.labels` | Merged  
`content.action` | `security_result.action_details` | Directly mapped  
`project_type` | `target.application` | Directly mapped  
`branch_label` | `target.resource.attribute.labels` | Merged  
`id_label` | `target.resource.attribute.labels` | Merged  
`imageTag_label` | `target.resource.attribute.labels` | Merged  
`isMonitored_label` | `target.resource.attribute.labels` | Merged  
`origin_label` | `target.resource.attribute.labels` | Merged  
`project_id_label` | `target.resource.attribute.labels` | Merged  
`readOnly_label` | `target.resource.attribute.labels` | Merged  
`testFrequency_label` | `target.resource.attribute.labels` | Merged  
`totalDependencies_label` | `target.resource.attribute.labels` | Merged  
`project_id` | `target.resource.id` | Directly mapped  
`project_name` | `target.resource.name` | Directly mapped  
`content_url` | `target.url` | Directly mapped  
`project_browseUrl` | `target.url` | Directly mapped  
N/A | `metadata.event_type` | Constant: `NETWORK_CONNECTION`  
N/A | `metadata.product_name` | Constant: `SNYK_ISSUES`  
N/A | `metadata.vendor_name` | Constant: `SNYK_ISSUES`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/snyk-issues-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
