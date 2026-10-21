---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fireeye-hx/
title: Collect Trellix Endpoint Security HX (formerly FireEye HX) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:19:48.651934+00:00
---

# Collect Trellix Endpoint Security HX (formerly FireEye HX) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fireeye-hx/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Trellix Endpoint Security HX (formerly FireEye HX) logs

**Parser Version:** 30.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide explains how to ingest Trellix Endpoint Security HX (formerly known as FireEye HX) logs to Google Security Operations using Google Cloud Storage V2. Trellix Endpoint Security HX is an endpoint detection and response (EDR) platform that provides advanced threat detection, investigation, and containment capabilities. It uses intelligence-led protection and real-time indicators of compromise (IOC) to detect and respond to sophisticated attacks on endpoints.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance.
  * A GCP project with Cloud Storage API enabled.
  * Permissions to create and manage GCS buckets and IAM policies.
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs.
  * Privileged access to the Trellix Endpoint Security HX console with API access enabled.
  * A Trellix HX API user account with at least Analyst role.



## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project.
  3. In the navigation menu, go to **Cloud Storage** > **Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `fireeye-hx-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location closest to your Google SecOps instance  
**Storage class** | **Standard** (recommended for frequently accessed logs)  
**Access control** | **Uniform** (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Collect Trellix Endpoint Security HX API credentials

### Get the HX console URL

  1. Sign in to the **Trellix Endpoint Security HX** web console.
  2. Note the console URL from the browser address bar (Format: `https://<hx-hostname>:<port>`).



### Create or verify API user account

  1. Sign in to the Trellix HX console with an administrator account.
  2. Go to **Admin** > **User Accounts**.
  3. Create a new user or select an existing user for API access.
  4. Ensure the user has the **api_analyst** or **api_admin** role.
  5. Note the username and password for API access.



### Verify API access

  * Test your credentials before proceeding with the integration:
        
        HX_HOST="[https://hx-console.example.com:3000](https://hx-console.example.com:3000)"
        HX_USER="api_user"
        HX_PASS="api_password"
        
        # Authenticate and get token
        curl -k -X POST "$HX_HOST/hx/api/v3/token" \
            -u "$HX_USER:$HX_PASS"
        


**Note:** A successful response returns an HTTP 204 status with a `X-FeApi-Token` header containing the API token.

## Create service account for Cloud Run function

The Cloud Run function needs a service account with permissions to write to the GCS bucket and be invoked by Pub/Sub.

### Create service account

  1. In the **GCP Console** , go to **IAM & Admin** > **Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : `fireeye-hx-collector-sa`
     * **Service account description** : `Service account for Cloud Run function to collect Trellix HX logs`
  4. Click **Create and Continue**.
  5. In the **Grant this service account access to project** section, add the following roles: 
     1. **Storage Object Admin**
     2. **Cloud Run Invoker**
     3. **Cloud Functions Invoker**
  6. Click **Continue** then **Done**.



### Grant IAM permissions on GCS bucket

  1. Go to **Cloud Storage** > **Buckets**.
  2. Click on the bucket name (`fireeye-hx-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. **Add principals** : Enter the service account email.
  6. **Assign roles** : Select **Storage Object Admin**.
  7. Click **Save**.



## Create Pub/Sub topic

Create a topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub** > **Topics**.
  2. Click **Create topic**.
  3. **Topic ID** : `fireeye-hx-logs-trigger`.
  4. Click **Create**.



## Create Cloud Run function to collect logs

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function**.
  4. In the **Configure** section, provide the following details:

Setting | Value  
---|---  
**Service name** | `fireeye-hx-collector`  
**Region** | Select region matching your GCS bucket  
**Runtime** | **Python 3.12** or later  
  5. In the **Trigger** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose `fireeye-hx-logs-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section, select **Require authentication** and check **Identity and Access Management (IAM)**.

  7. Scroll down to **Containers, Networking, Security**.

  8. In the **Security** tab, select the service account `fireeye-hx-collector-sa`.

  9. In the **Containers** tab, click **Variables & Secrets** and add the following:

Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `fireeye-hx-logs` | GCS bucket name  
`GCS_PREFIX` | `hx-alerts` | Prefix for log files  
`STATE_KEY` | `hx-alerts/state.json` | State file path  
`HX_HOST` | `https://hx-console.example.com:3000` | HX console URL  
`HX_USER` | `api_user` | API username  
`HX_PASS` | `api_password` | API password  
`MAX_RECORDS` | `1000` | Max records per run  
`PAGE_SIZE` | `100` | Records per page  
`LOOKBACK_HOURS` | `24` | Initial lookback period  
  10. In **Requests** , set **Request timeout** to `600` seconds.

  11. Click **Create**. After the service is created, the **inline code editor** will open.




### Add function code

  1. Enter **main** in the **Entry point** field.
  2. Create the following files in the inline editor:

     * **main.py:**
    
    import functions_framework
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    import json
    import os
    import urllib3
    from datetime import datetime, timezone, timedelta
    import time
    
    # Disable SSL warnings for self-signed certs
    urllib3.disable_warnings(urllib3.[exceptions](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.exceptions.html).InsecureRequestWarning)
    
    # Initialize HTTP client with timeouts
    http = urllib3.PoolManager(
        timeout=urllib3.Timeout(connect=5.0, read=30.0),
        retries=False,
        cert_reqs='CERT_NONE',
    )
    
    # Initialize Storage client
    storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    
    # Environment variables
    GCS_BUCKET = os.environ.get('GCS_BUCKET')
    GCS_PREFIX = os.environ.get('GCS_PREFIX', 'hx-alerts')
    STATE_KEY = os.environ.get('STATE_KEY', 'hx-alerts/state.json')
    HX_HOST = os.environ.get('HX_HOST')
    HX_USER = os.environ.get('HX_USER')
    HX_PASS = os.environ.get('HX_PASS')
    MAX_RECORDS = int(os.environ.get('MAX_RECORDS', '1000'))
    PAGE_SIZE = int(os.environ.get('PAGE_SIZE', '100'))
    LOOKBACK_HOURS = int(os.environ.get('LOOKBACK_HOURS', '24'))
    
    def get_api_token(host, username, password):
        url = f"{host}/hx/api/v3/token"
        auth_string = f"{username}:{password}"
        import base64
        auth_b64 = base64.b64encode(auth_string.encode('utf-8')).decode('utf-8')
        headers = {'Authorization': f'Basic {auth_b64}'}
        response = http.request('POST', url, headers=headers)
        if response.status == 204:
            return response.headers.get('X-FeApi-Token')
        else:
            raise Exception(f"Authentication failed: HTTP {response.status}")
    
    @functions_framework.cloud_event
    def main(cloud_event):
        if not all([GCS_BUCKET, HX_HOST, HX_USER, HX_PASS]):
            print('Error: Missing required environment variables')
            return
        try:
            bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(GCS_BUCKET)
            state = load_state(bucket, STATE_KEY)
            now = datetime.now(timezone.utc)
            last_time = None
    
            if isinstance(state, dict) and [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get("last_event_time"):
                try:
                    last_time = parse_datetime(state["last_event_time"]) - timedelta(minutes=2)
                except Exception as e:
                    print(f"Warning: Could not parse last_event_time: {e}")
    
            if last_time is None:
                last_time = now - timedelta(hours=LOOKBACK_HOURS)
    
            print(f"Fetching alerts from {last_time.isoformat()} to {now.isoformat()}")
            token = get_api_token(HX_HOST, HX_USER, HX_PASS)
            alerts, newest_time = fetch_alerts(HX_HOST, token, last_time, now, PAGE_SIZE, MAX_RECORDS)
            hosts = fetch_hosts(HX_HOST, token)
            all_records = alerts + hosts
    
            if not all_records:
                print("No new records found.")
                save_state(bucket, STATE_KEY, now.isoformat())
                return
    
            timestamp = now.strftime('%Y%m%d_%H%M%S')
            object_key = f"{GCS_PREFIX}/logs_{timestamp}.ndjson"
            ndjson = '\n'.join([json.dumps(record, ensure_ascii=False) for record in all_records]) + '\n'
            bucket.blob(object_key).[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(ndjson, content_type='application/x-ndjson')
    
            print(f"Wrote {len(all_records)} records to gs://{GCS_BUCKET}/{object_key}")
            save_state(bucket, STATE_KEY, newest_time if newest_time else now.isoformat())
            release_token(HX_HOST, token)
            print(f"Successfully processed {len(all_records)} records")
        except Exception as e:
            print(f'Error processing logs: {str(e)}')
            raise
    
    def parse_datetime(value):
        if [value](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.ObjectCustomContextPayload.html#google_cloud_storage_blob_ObjectCustomContextPayload_value).endswith("Z"):
            value = value[:-1] + "+00:00"
        return datetime.fromisoformat(value)
    
    def load_state(bucket, key):
        try:
            blob = bucket.blob(key)
            if blob.exists():
                return json.loads(blob.[download_as_text](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_download_as_text)())
        except Exception as e:
            print(f"Warning: Could not load state: {e}")
        return {}
    
    def save_state(bucket, key, last_event_time_iso):
        try:
            state = {'last_event_time': last_event_time_iso}
            bucket.blob(key).[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(json.dumps(state, indent=2), content_type='application/json')
        except Exception as e:
            print(f"Warning: Could not save state: {e}")
    
    def fetch_alerts(host, token, start_time, end_time, page_size, max_records):
        endpoint = f"{host}/hx/api/v3/alerts"
        headers = {'X-FeApi-Token': token, 'Accept': 'application/json'}
        records = []; newest_time = None; offset = 0; backoff = 1.0
    
        while True:
            if len(records) >= max_records: break
            start_iso = start_time.strftime('%Y-%m-%dT%H:%M:%S.000Z')
            end_iso = end_time.strftime('%Y-%m-%dT%H:%M:%S.000Z')
            url = f"{endpoint}?sort=reported_at+asc&min_reported_at={start_iso}&max_reported_at={end_iso}&offset={offset}&limit={min(page_size, max_records - len(records))}"
    
            try:
                response = http.request('GET', url, headers=headers)
                if response.status == 429:
                    time.sleep(int(response.headers.get('Retry-After', str(int(backoff))))); backoff = min(backoff * 2, 30.0); continue
                backoff = 1.0
                if response.status != 200: break
                data = json.loads(response.data.decode('utf-8'))
                page_results = data.get('data', {}).get('entries', [])
                if not page_results: break
                records.extend(page_results)
                for alert in page_results:
                    event_time = alert.get('reported_at')
                    if event_time and (newest_time is None or event_time > newest_time): newest_time = event_time
                offset += len(page_results)
                if offset >= data.get('data', {}).get('total', 0): break
            except Exception: break
        return records, newest_time
    
    def fetch_hosts(host, token):
        endpoint = f"{host}/hx/api/v3/hosts"
        headers = {'X-FeApi-Token': token, 'Accept': 'application/json'}
        try:
            response = http.request('GET', f"{endpoint}?limit=100&offset=0", headers=headers)
            if response.status != 200: return []
            return json.loads(response.data.decode('utf-8')).get('data', {}).get('entries', [])
        except Exception: return []
    
    def release_token(host, token):
        try:
            http.request('DELETE', f"{host}/hx/api/v3/token", headers={'X-FeApi-Token': token})
        except Exception: pass
    

     * **requirements.txt:**
    
    functions-framework==3.*
    google-cloud-storage==2.*
    urllib3>=2.0.0
    

  3. Click **Deploy** to save and deploy the function.




## Create Cloud Scheduler job

  1. In the **GCP Console** , go to **Cloud Scheduler**.
  2. Click **Create Job**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | `fireeye-hx-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | **Pub/Sub**  
**Topic** | `fireeye-hx-logs-trigger`  
**Message body** | `{}`  
  4. Click **Create**.




### Test the integration

  1. In **Cloud Scheduler** , find your job and click **Force run**.
  2. Go to **Cloud Run** > **Services** > **Logs** to verify success.
  3. Check **Cloud Storage** to confirm a new `.ndjson` file exists in the `hx-alerts/` folder.



## Configure a feed in Google SecOps

  1. Go to **SIEM Settings** > **Feeds**.
  2. Click **Add New Feed** > **Configure a single feed**.
  3. **Feed name** : `Trellix HX Logs`.
  4. **Source type** : **Google Cloud Storage V2**.
  5. **Log type** : **FireEye HX**.
  6. Click **Get Service Account** and copy the email (e.g., `chronicle-12345678@...`).
  7. Click **Next**.
  8. **Storage bucket URL** : `gs://fireeye-hx-logs/hx-alerts/` (Include the trailing slash).
  9. **Source deletion option** : Select according to your preference.
  10. Click **Next** , review, and click **Submit**.



## Grant IAM permissions to the service account

The Google SecOps service account needs **Storage Object Viewer** role on your bucket.

  1. Go to **Cloud Storage** > **Buckets**.
  2. Select your bucket and go to the **Permissions** tab.
  3. Click **Grant access**.
  4. **Add principals** : Paste the Google SecOps service account email.
  5. **Assign roles** : Select **Storage Object Viewer**.
  6. Click **Save**.



## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
`alert.event_type` | `metadata.product_event_type` | Direct mapping.  
`alert.reported_at` | `metadata.event_timestamp` | Parsed as timestamp.  
`alert.source` | `principal.hostname` | Direct mapping.  
`alert.agent._id` | `principal.asset_id` | Direct mapping.  
`alert.indicator.display_name` | `security_result.threat_name` | Direct mapping.  
`alert.md5values` | `target.file.md5` | Direct mapping.  
N/A | `metadata.vendor_name` | Set to **Trellix**.  
N/A | `metadata.product_name` | Set to **Endpoint Security HX**.  
N/A | `metadata.log_type` | Set to **FIREEYE_HX**.  
`cs12` | `additional.fields` | Mapped from changelog  
`cs9` | `target.process.file.md5` | Mapped from changelog  
`account_name", "UUID", "Mitre", "host_details.data.sysinfo.url", "host_details.route", "host_details.data.reported_clone", and "host_details.data.timezone` | `security_result.detection_fields` | Mapped from changelog  
`Desc` | `metadata.description` | Mapped from changelog  
`Confidence` | `security_result.confidence` | Mapped from changelog  
`alert.appliance._id` | `additional.fields` | Mapped from changelog  
`host_details.data.stats.acqs", "host_details.data.stats.alerting_conditions", "host_details.data.stats.alerts", "host_details.data.stats.exploit_alerts", "host_details.data.stats.exploit_blocks", and "host_details.data.stats.false_positive_alerts` | `security_result.detection_fields` | Mapped from changelog  
`categoryOutcome", "cs13` | `additional.fields` | Mapped from changelog  
`cs6` | `target.process.file.sha1` | Mapped from changelog  
`host_details.message` | `security_result.action_details` | Mapped from changelog  
`alert.md5values", "alert.resolution", "alert.is_false_positive", and "alert.alert_type` | `additional.fields` | Mapped from changelog  
`type.threat_type` | `security_result.threat_name` | Mapped from changelog  
`ent.lms_event_id` | `metadata.product_log_id` | Mapped from changelog  
`email.smtp.mail_from` | `network.email.from` | Mapped from changelog  
`email.headers.subject` | `network.email.subject` | Mapped from changelog  
`email.headers.to` | `network.email.to` | Mapped from changelog  
`ent.type", "ent.id", "ent.name", "ent.object_source", "ent.binary", and "ent.attributes.scan_id` | `security_result.detection_fields` | Mapped from changelog  
`cs11Label` | `additional_cs11Label.key` | Mapped from changelog  
`cs11` | `additional_cs11.value` | Mapped from changelog  
`alert.sysinfo.mac_address` | `principal.mac` | Mapped from changelog  
`host_details.data.agent_version` | `metadata.product_version` | Mapped from changelog  
`alert.url` | `metadata.url_back_to_product` | Mapped from changelog  
`description` | `metadata.description` | Mapped from changelog  
`alert.agent._id` | `principal.asset.asset_id` | Mapped from changelog  
`alert.event_id` | `metadata.product_log_id` | Mapped from changelog  
`deviceCustomDate1Label` | `additional_deviceCustomDate1.key` | Mapped from changelog  
`deviceCustomDate1` | `additional_deviceCustomDate1.value` | Mapped from changelog  
`deviceCustomDate2` | `additional_deviceCustomDate2.value` | Mapped from changelog  
`client` | `principal.ip` | Mapped from changelog  
`principal_ip` | `principal.ip` | Mapped from changelog  
`remoteaddress` | `principal.ip` | Mapped from changelog  
`host_` | `principal.hostname` | Mapped from changelog  
`line` | `principal.application` | Mapped from changelog  
`username` | `principal.user.userid` | Mapped from changelog  
`client_app_type` | `principal.resource.attribute.labels` | Mapped from changelog  
`upstream` | `target.url` | Mapped from changelog  
`role` | `target.user.role_name` | Mapped from changelog  
`server` | `target.resource.attribute.labels` | Mapped from changelog  
`localusername` | `target.user.user_display_name` | Mapped from changelog  
`request` | `additional.fields` | Mapped from changelog  
`mlocked` | `additional.fields` | Mapped from changelog  
`kernel_stack` | `additional.fields` | Mapped from changelog  
`sessionID` | `network.session_id` | Mapped from changelog  
`auth_mechanism` | `extensions.auth.mechanism` | Mapped from changelog  
`authsubmethod` | `extensions.auth.auth_details` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fireeye-hx-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
