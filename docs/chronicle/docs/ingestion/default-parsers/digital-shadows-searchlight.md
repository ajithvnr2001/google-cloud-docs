---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/digital-shadows-searchlight/
title: Collect ReliaQuest GreyMatter DRP (formerly Digital Shadows SearchLight) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:18:31.329475+00:00
---

# Collect ReliaQuest GreyMatter DRP (formerly Digital Shadows SearchLight) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/digital-shadows-searchlight/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect ReliaQuest GreyMatter DRP (formerly Digital Shadows SearchLight) logs

**Parser Version:** 2.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest ReliaQuest GreyMatter DRP (formerly known as Digital Shadows SearchLight) logs to Google Security Operations using Google Cloud Storage. The parser extracts security event data from the JSON logs. It initializes Unified Data Model (UDM) fields, parses the JSON payload, maps relevant fields to the UDM schema, extracts entities like email and hostname using grok patterns, and constructs the security_result and metadata objects within the UDM event.

## Before you begin

Make sure that you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
  * Privileged access to Digital Shadows SearchLight tenant



## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `digital-shadows-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Collect Digital Shadows SearchLight API credentials

  1. Sign in to the **Digital Shadows SearchLight Portal**.
  2. Go to **Settings > API Credentials**.
  3. Create a new API client or key pair.
  4. Copy and save in a secure location the following details:

     * **API Key** : Your 6-character API key
     * **API Secret** : Your 32-character API secret
     * **Account ID** : Your account ID (required for most tenants)
     * **API Base URL** : `https://api.searchlight.app/v1` or `https://portal-digitalshadows.com/api/v1`
**Note:** These credentials will be used by the Cloud Run function to authenticate to the Digital Shadows SearchLight API. Contact your Digital Shadows representative if you need assistance obtaining API credentials.



## Create service account for Cloud Run function

The Cloud Run function needs a service account with permissions to write to GCS bucket.

### Create service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `digital-shadows-collector-sa`.
     * **Service account description** : Enter `Service account for Cloud Run function to collect Digital Shadows SearchLight logs`.
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

**Note:** This role is required for the service account to write logs to GCS bucket and manage state files.



### Grant IAM permissions on GCS bucket

Grant the service account write permissions on the GCS bucket:

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `digital-shadows-collector-sa@PROJECT_ID.iam.gserviceaccount.com`).
     * **Assign roles** : Select **Storage Object Admin**.
  6. Click **Save**.



## Create Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : Enter `digital-shadows-trigger`.
     * Leave other settings as default.
  4. Click **Create**.



## Create Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from Digital Shadows SearchLight API and write them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** (use an inline editor to create a function).
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `digital-shadows-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | Select **Python 3.12** or later  
  5. In the **Trigger (optional)** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In**Select a Cloud Pub/Sub topic** , choose the topic (`digital-shadows-trigger`).
     4. Click **Save**.
  6. In the **Authentication** section:

     1. Select **Require authentication**.
     2. Check**Identity and Access Management (IAM)**.
**Note:** Pub/Sub will automatically handle authentication when invoking the function.
  7. Scroll down and expand **Containers, Networking, Security**.

  8. Go to the **Security** tab:

     * **Service account** : Select the service account (`digital-shadows-collector-sa`).
  9. Go to the **Containers** tab:

     1. Click **Variables & Secrets**.
     2. Click **\+ Add variable** for each environment variable:
Variable Name | Example Value  
---|---  
`GCS_BUCKET` | `digital-shadows-logs`  
`GCS_PREFIX` | `digital-shadows-searchlight`  
`STATE_KEY` | `digital-shadows-searchlight/state.json`  
`DS_API_KEY` | `your-6-character-api-key`  
`DS_API_SECRET` | `your-32-character-api-secret`  
`API_BASE` | `https://api.searchlight.app/v1`  
`DS_ACCOUNT_ID` | `your-account-id`  
`PAGE_SIZE` | `100`  
`MAX_PAGES` | `10`  
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

  16. After the service is created, the **inline code editor** will open automatically.




### Add function code

  1. Enter **main** in **Function entry point**
  2. In the inline code editor, create two files:

     * **main.py:**
    
    import functions_framework
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    import json
    import os
    import base64
    import logging
    import time
    from datetime import datetime, timedelta, timezone
    from urllib.parse import urlencode
    import urllib3
    
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    
    HTTP = urllib3.PoolManager(retries=False)
    
    storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    
    def _basic_auth_header(key: str, secret: str) -> str:
        token = base64.b64encode(f"{key}:{secret}".encode("utf-8")).decode("utf-8")
        return f"Basic {token}"
    
    def _load_state(bucket, key, default_days=30) -> str:
        """Return ISO8601 checkpoint (UTC)."""
        try:
            blob = bucket.blob(key)
            if blob.exists():
                state_data = blob.[download_as_text](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_download_as_text)()
                state = json.loads(state_data)
                ts = [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get("last_timestamp")
                if ts:
                    return ts
        except Exception as e:
            logger.warning(f"State read error: {e}")
        return (datetime.now(timezone.utc) - timedelta(days=default_days)).isoformat()
    
    def _save_state(bucket, key, ts: str) -> None:
        blob = bucket.blob(key)
        blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
            json.dumps({"last_timestamp": ts}),
            content_type="application/json"
        )
    
    def _get_json(url: str, headers: dict, params: dict, backoff_s=2, max_retries=3) -> dict:
        qs = f"?{urlencode(params)}" if params else ""
        for attempt in range(max_retries):
            r = HTTP.request("GET", f"{url}{qs}", headers=headers)
            if r.status == 200:
                return json.loads(r.data.decode("utf-8"))
            if r.status in (429, 500, 502, 503, 504):
                wait = backoff_s * (2 ** attempt)
                logger.warning(f"HTTP {r.status} from DS API, retrying in {wait}s")
                time.sleep(wait)
                continue
            raise RuntimeError(f"DS API error {r.status}: {r.data[:200]}")
        raise RuntimeError("Exceeded retry budget for DS API")
    
    def _collect(api_base, headers, path, since_ts, account_id, page_size, max_pages, time_param):
        items = []
        for page in range(max_pages):
            params = {
                "limit": page_size,
                "offset": page * page_size,
                time_param: since_ts,
            }
            if account_id:
                params["account-id"] = account_id
            data = _get_json(f"{api_base}/{path}", headers, params)
            batch = data.get("items") or data.get("data") or []
            if not batch:
                break
            items.extend(batch)
            if len(batch) < page_size:
                break
        return items
    
    @functions_framework.cloud_event
    def main(cloud_event):
        """
        Cloud Run function triggered by Pub/Sub to fetch logs from Digital Shadows SearchLight API and write to GCS.
    
        Args:
            cloud_event: CloudEvent object containing Pub/Sub message
        """
    
        bucket_name = os.environ["GCS_BUCKET"]
        api_key = os.environ["DS_API_KEY"]
        api_secret = os.environ["DS_API_SECRET"]
    
        prefix = os.environ.get("GCS_PREFIX", "digital-shadows-searchlight")
        state_key = os.environ.get("STATE_KEY", "digital-shadows-searchlight/state.json")
        api_base = os.environ.get("API_BASE", "https://api.searchlight.app/v1")
        account_id = os.environ.get("DS_ACCOUNT_ID", "")
        page_size = int(os.environ.get("PAGE_SIZE", "100"))
        max_pages = int(os.environ.get("MAX_PAGES", "10"))
    
        try:
            bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
    
            last_ts = _load_state(bucket, state_key)
            logger.info(f"Checkpoint: {last_ts}")
    
            headers = {
                "Authorization": _basic_auth_header(api_key, api_secret),
                "Accept": "application/json",
                "User-Agent": "Chronicle-DigitalShadows-GCS/1.0",
            }
    
            records = []
    
            incidents = _collect(
                api_base, headers, "incidents", last_ts, account_id,
                page_size, max_pages, time_param="published-after"
            )
            for incident in incidents:
                incident['_source_type'] = 'incident'
            records.extend(incidents)
    
            intel_incidents = _collect(
                api_base, headers, "intel-incidents", last_ts, account_id,
                page_size, max_pages, time_param="published-after"
            )
            for intel in intel_incidents:
                intel['_source_type'] = 'intelligence_incident'
            records.extend(intel_incidents)
    
            indicators = _collect(
                api_base, headers, "indicators", last_ts, account_id,
                page_size, max_pages, time_param="lastUpdated-after"
            )
            for indicator in indicators:
                indicator['_source_type'] = 'ioc'
            records.extend(indicators)
    
            if records:
                newest = max(
                    (r.get("updated") or r.get("raised") or r.get("lastUpdated") or last_ts)
                    for r in records
                )
    
                key = f"{prefix}/digital_shadows_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}.json"
                body = "\n".join(json.dumps(r, separators=(",", ":")) for r in records)
    
                blob = bucket.blob(key)
                blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(body, content_type="application/x-ndjson")
    
                _save_state(bucket, state_key, newest)
                msg = f"Wrote {len(records)} records to gs://{bucket_name}/{key}"
            else:
                msg = "No new records"
    
            logger.info(msg)
            print(msg)
    
        except Exception as e:
            logger.error(f"Error processing logs: {str(e)}")
            raise
    

     * **requirements.txt:**
    
    functions-framework==3.*
    google-cloud-storage==2.*
    urllib3>=2.0.0
    

  3. Click **Deploy** to save and deploy the function.

  4. Wait for deployment to complete (2-3 minutes).

**Note:** This script is provided as an example and is not officially supported. We welcome feedback about how we can improve it. To submit feedback, click Send Feedback > Google SecOps Security Product Feedback on this page. API endpoints are based on third-party integrations; confirm with Digital Shadows support for your tenancy.



## Create Cloud Scheduler job

Cloud Scheduler will publish messages to the Pub/Sub topic at regular intervals, triggering the Cloud Run function.

  1. In the **GCP Console** , go to **Cloud Scheduler**.
  2. Click **Create Job**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | `digital-shadows-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | Pub/Sub  
**Topic** | Select the topic (`digital-shadows-trigger`)  
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
  
### Test the scheduler job

  1. In the **Cloud Scheduler** console, find your job.
  2. Click **Force run** to trigger manually.
  3. Wait a few seconds and go to **Cloud Run > Services > digital-shadows-collector > Logs**.
  4. Verify the function executed successfully.
  5. Check the GCS bucket to confirm logs were written.



## Configure a feed in Google SecOps to ingest Digital Shadows SearchLight logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Digital Shadows SearchLight logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Digital Shadows SearchLight** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address. You will use it in the next step.

**Note:** Each Google SecOps instance has a unique service account. Do not use service accounts from other documentation or examples.
  9. Click **Next**.

  10. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
    
    gs://digital-shadows-logs/digital-shadows-searchlight/
    

     * Replace:

     * `digital-shadows-logs`: Your GCS bucket name.

     * `digital-shadows-searchlight`: Optional prefix/folder path where logs are stored (leave empty for root).

**Examples:** \- Root bucket: `gs://company-logs/` \- With prefix: `gs://company-logs/digital-shadows-searchlight/` \- With subfolder: `gs://company-logs/vendor/application/`

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



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`about_event-created` | `about.labels` | Merged  
`about_state` | `about.labels` | Merged  
`about_triage-item-id` | `about.labels` | Merged  
`about_triage-item-source-alert-id` | `about.labels` | Merged  
`about_triage-item-source-incident-id` | `about.labels` | Merged  
`about_triage-item_portal-id` | `about.labels` | Merged  
`about_triage-item_raised` | `about.labels` | Merged  
`about_triage-item_updated` | `about.labels` | Merged  
`event-created` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`classification` | `metadata.product_event_type` | Mapped when `event-num` != ``  
`event-num` | `metadata.product_log_id` | Mapped when `event-num` != ``  
`about` | `security_result.about` | Renamed/mapped  
`event-action` | `security_result.action_details` | Directly mapped  
`risk` | `security_result.category_details` | Merged  
`alert.description` | `security_result.description` | Directly mapped  
`risk-level` | `security_result.severity_details` | Directly mapped  
`triage-item.title` | `security_result.summary` | Directly mapped  
`triage-item-id` | `security_result.threat_id` | Directly mapped  
`classification` | `security_result.threat_name` | Directly mapped  
`triage-item.portal-id` | `security_result.url_back_to_product` | Directly mapped  
`_hostname` | `target.hostname` | Mapped when `event-num` != ``  
`_commit_url` | `target.url` | Mapped when `event-num` != ``  
`_repo_url` | `target.url` | Mapped when `event-num` != ``  
`_email` | `target.user.email_addresses` | Merged  
N/A | `security_result.threat_status` | Constant: `ACTIVE`  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
