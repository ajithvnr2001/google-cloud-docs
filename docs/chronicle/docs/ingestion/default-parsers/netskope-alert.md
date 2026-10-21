---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/netskope-alert/
title: Collect Netskope Alerts logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T12:36:47.582891+00:00
---

# Collect Netskope Alerts logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/netskope-alert/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Netskope Alerts logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Netskope Alerts logs to Google Security Operations using Google Cloud Storage V2. Netskope is a cloud security platform that provides real-time data and threat protection for cloud services, websites, and private applications. Netskope Alerts capture security events including DLP violations, malware detections, anomalous behavior, compromised credentials, and policy violations across SaaS, IaaS, and web traffic.

**Note:** The Netskope v1 REST API is deprecated. This guide uses the Netskope REST API v2, which provides improved performance, pagination, and reliability.

For more information, see [Collect Netskope Alert logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/netskope-alert).

## Before you begin

Make sure that you have the following prerequisites:

  * A Google SecOps instance.
  * A GCP project with Cloud Storage API enabled.
  * Permissions to create and manage GCS buckets and IAM policies.
  * Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs.
  * Privileged access to the Netskope tenant admin console.
  * A Netskope REST API v2 token with read permissions for alerts.



## Collect Netskope API v2 credentials

### Create a REST API v2 token

  1. Sign in to the **Netskope tenant admin console** (for example, `https://your-tenant.goskope.com`).
  2. Go to **Settings** > **Tools** > **REST API v2**.
  3. Click **New Token**.
  4. Provide the following configuration details: 
     * **Token Name** : Enter a descriptive name (for example, `SecOps-Alert-Integration`).
     * **Expiry** : Set the token expiry date according to your security policy.
  5. Under **Endpoints** , enable the following: 
     * `/api/v2/events/data/alert` \- Read permission.
  6. Click **Save**.
  7. Copy and save the **token value** securely. The token is displayed only once.



### Verify API access

  * Test your credentials before proceeding with the integration:
        
        NETSKOPE_TENANT="[https://your-tenant.goskope.com](https://your-tenant.goskope.com)"
        API_TOKEN="your-api-v2-token"
        
        curl -v -H "Netskope-Api-Token: ${API_TOKEN}" \
            "${NETSKOPE_TENANT}/api/v2/events/data/alert?limit=1"
        


**Note:** A successful response returns HTTP 200 with JSON data. If you receive HTTP 401, verify the token. If you receive HTTP 403, verify the endpoint permissions on the token.

## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage** > **Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `netskope-alerts-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location closest to your Google SecOps instance  
**Storage class** | **Standard** (recommended for frequently accessed logs)  
**Access control** | **Uniform** (recommended)  
  6. Click **Create**.




## Create service account for Cloud Run function

The Cloud Run function needs a service account with permissions to write to GCS bucket and be invoked by Pub/Sub.

### Create service account

  1. In the **GCP Console** , go to **IAM & Admin** > **Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : `netskope-alerts-collector-sa`.
     * **Service account description** : `Service account for Cloud Run function to collect Netskope Alerts logs`.
  4. Click **Create and Continue**.
  5. In the **Grant this service account access to project** section, add the following roles: 
     1. **Storage Object Admin**
     2. **Cloud Run Invoker**
     3. **Cloud Functions Invoker**
  6. Click **Continue** and then **Done**.



### Grant IAM permissions on GCS bucket

  1. Go to **Cloud Storage** > **Buckets**.
  2. Click on the bucket `netskope-alerts-logs`.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `netskope-alerts-collector-sa@PROJECT_ID.iam.gserviceaccount.com`).
     * **Assign roles** : Select **Storage Object Admin**.
  6. Click **Save**.



## Create Pub/Sub topic

Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.

  1. In the **GCP Console** , go to **Pub/Sub** > **Topics**.
  2. Click **Create topic**.
  3. Provide the following configuration details: 
     * **Topic ID** : `netskope-alerts-trigger`.
     * Leave other settings as default.
  4. Click **Create**.



## Create Cloud Run function to collect logs

The Cloud Run function will be triggered by Pub/Sub messages from Cloud Scheduler to fetch alerts from the Netskope REST API v2 and write them to GCS.

  1. In the **GCP Console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function**.
  4. In the **Configure** section, provide the following configuration details:

Setting | Value  
---|---  
**Service name** | `netskope-alerts-collector`  
**Region** | Select region matching your GCS bucket (for example, `us-central1`)  
**Runtime** | **Python 3.12** or later  
  5. In the **Trigger** section:

     1. Click **\+ Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , choose `netskope-alerts-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section, select **Require authentication** and check **Identity and Access Management (IAM)**.

  7. Scroll down to **Containers, Networking, Security**.

  8. In the **Security** tab, select the service account `netskope-alerts-collector-sa`.

  9. In the **Containers** tab, click **Variables & Secrets** and add the following:

Variable Name | Example Value | Description  
---|---|---  
`GCS_BUCKET` | `netskope-alerts-logs` | GCS bucket name  
`GCS_PREFIX` | `netskope/alerts` | Prefix for log files  
`STATE_KEY` | `netskope/alerts/state.json` | State file path  
`NETSKOPE_TENANT` | `https://your-tenant.goskope.com` | Netskope tenant URL  
`NETSKOPE_API_TOKEN` | `your-api-v2-token` | REST API v2 token  
`MAX_RECORDS` | `5000` | Max records per run  
`PAGE_SIZE` | `1000` | Records per page  
`LOOKBACK_HOURS` | `24` | Initial lookback period  
  10. In the **Requests** section, set **Request timeout** to `600` seconds.

  11. In the **Settings** tab (Resources), select **512 MiB** memory and **1** CPU.

  12. Click **Create**. After the service is created, the **inline code editor** will open automatically.




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
    
    http = urllib3.PoolManager(
        timeout=urllib3.Timeout(connect=5.0, read=30.0),
        retries=False,
    )
    
    storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    
    GCS_BUCKET = os.environ.get('GCS_BUCKET')
    GCS_PREFIX = os.environ.get('GCS_PREFIX', 'netskope/alerts')
    STATE_KEY = os.environ.get('STATE_KEY', 'netskope/alerts/state.json')
    NETSKOPE_TENANT = os.environ.get('NETSKOPE_TENANT')
    NETSKOPE_API_TOKEN = os.environ.get('NETSKOPE_API_TOKEN')
    MAX_RECORDS = int(os.environ.get('MAX_RECORDS', '5000'))
    PAGE_SIZE = int(os.environ.get('PAGE_SIZE', '1000'))
    LOOKBACK_HOURS = int(os.environ.get('LOOKBACK_HOURS', '24'))
    
    def to_epoch_seconds(dt):
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return int(dt.timestamp())
    
    def parse_datetime(value):
        if isinstance(value, (int, float)):
            return datetime.fromtimestamp(value, tz=timezone.utc)
        if isinstance(value, str):
            if [value](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.ObjectCustomContextPayload.html#google_cloud_storage_blob_ObjectCustomContextPayload_value).endswith("Z"):
                value = value[:-1] + "+00:00"
            return datetime.fromisoformat(value)
        return None
    
    @functions_framework.cloud_event
    def main(cloud_event):
        if not all([GCS_BUCKET, NETSKOPE_TENANT, NETSKOPE_API_TOKEN]):
            print('Error: Missing required environment variables')
            return
    
        try:
            bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(GCS_BUCKET)
            state = load_state(bucket, STATE_KEY)
    
            now = datetime.now(timezone.utc)
            last_time = None
    
            if isinstance(state, dict) and [state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state).get("last_event_time"):
                try:
                    last_time = parse_datetime(state["last_event_time"])
                    last_time = last_time - timedelta(minutes=2)
                except Exception as e:
                    print(f"Warning: Could not parse last_event_time: {e}")
    
            if last_time is None:
                last_time = now - timedelta(hours=LOOKBACK_HOURS)
    
            print(f"Fetching alerts from {last_time.isoformat()} to {now.isoformat()}")
    
            records, newest_event_time = fetch_alerts(
                tenant=NETSKOPE_TENANT,
                token=NETSKOPE_API_TOKEN,
                start_time=last_time,
                end_time=now,
                page_size=PAGE_SIZE,
                max_records=MAX_RECORDS,
            )
    
            if not records:
                print("No new alert records found.")
                save_state(bucket, STATE_KEY, to_epoch_seconds(now))
                return
    
            timestamp = now.strftime('%Y%m%d_%H%M%S')
            object_key = f"{GCS_PREFIX}/alerts_{timestamp}.ndjson"
            blob = bucket.blob(object_key)
    
            ndjson = '\n'.join([json.dumps(r, ensure_ascii=False) for r in records]) + '\n'
            blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(ndjson, content_type='application/x-ndjson')
    
            print(f"Wrote {len(records)} records to gs://{GCS_BUCKET}/{object_key}")
    
            if newest_event_time:
                save_state(bucket, STATE_KEY, newest_event_time)
            else:
                save_state(bucket, STATE_KEY, to_epoch_seconds(now))
    
            print(f"Successfully processed {len(records)} records")
    
        except Exception as e:
            print(f'Error processing alerts: {str(e)}')
            raise
    
    def load_state(bucket, key):
        try:
            blob = bucket.blob(key)
            if blob.exists():
                state_data = blob.[download_as_text](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_download_as_text)()
                return json.loads(state_data)
        except Exception as e:
            print(f"Warning: Could not load state: {e}")
        return {}
    
    def save_state(bucket, key, last_event_time):
        try:
            state = {'last_event_time': last_event_time}
            blob = bucket.blob(key)
            blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
                json.dumps(state, indent=2),
                content_type='application/json'
            )
            print(f"Saved state: last_event_time={last_event_time}")
        except Exception as e:
            print(f"Warning: Could not save state: {e}")
    
    def fetch_alerts(tenant, token, start_time, end_time, page_size, max_records):
        base_url = tenant.rstrip('/')
        endpoint = f"{base_url}/api/v2/events/data/alert"
    
        headers = {
            'Netskope-Api-Token': token,
            'Accept': 'application/json',
            'User-Agent': 'GoogleSecOps-NetskopeAlertCollector/1.0'
        }
    
        records = []
        newest_time = None
        page_num = 0
        backoff = 1.0
    
        start_epoch = to_epoch_seconds(start_time)
        end_epoch = to_epoch_seconds(end_time)
        operation_id = None
    
        url = f"{endpoint}?limit={page_size}&starttime={start_epoch}&endtime={end_epoch}"
    
        while True:
            page_num += 1
    
            if len(records) >= max_records:
                print(f"Reached max_records limit ({max_records})")
                break
    
            if operation_id:
                url = f"{endpoint}?limit={page_size}&operation={operation_id}"
    
            try:
                response = http.request('GET', url, headers=headers)
    
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
                page_results = data.get('result', [])
    
                if not page_results:
                    print("No more results (empty page)")
                    break
    
                print(f"Page {page_num}: Retrieved {len(page_results)} alerts")
                records.extend(page_results)
    
                for event in page_results:
                    try:
                        event_time = event.get('timestamp')
                        if event_time:
                            if newest_time is None or event_time > newest_time:
                                newest_time = event_time
                    except Exception as e:
                        print(f"Warning: Could not parse event time: {e}")
    
                wait_time = data.get('wait_time')
                operation_id = data.get('operation')
    
                if not operation_id or len(page_results) < page_size:
                    break
    
                if wait_time and wait_time > 0:
                    time.sleep(wait_time)
    
            except Exception as e:
                print(f"Error fetching alerts: {e}")
                return [], None
    
        print(f"Retrieved {len(records)} total records from {page_num} pages")
        return records, newest_time
    

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
**Name** | `netskope-alerts-collector-hourly`  
**Region** | Select same region as Cloud Run function  
**Frequency** | `0 * * * *` (every hour, on the hour)  
**Timezone** | Select timezone (UTC recommended)  
**Target type** | **Pub/Sub**  
**Topic** | Select `netskope-alerts-trigger`  
**Message body** | `{}`  
  4. Click **Create**.




## Configure a feed in Google SecOps

  1. Go to **SIEM Settings** > **Feeds**.
  2. Click **Add New Feed** > **Configure a single feed**.
  3. **Feed name** : `Netskope Alerts`.
  4. **Source type** : **Google Cloud Storage V2**.
  5. **Log type** : **Netskope Alert**.
  6. Click **Get Service Account** and copy the email address provided.
  7. Click **Next**.
  8. **Storage bucket URL** : `gs://netskope-alerts-logs/netskope/alerts/` (Include the trailing slash).
  9. **Source deletion option** : Select according to your preference (e.g., **Never** for testing).
  10. Click **Next** , review, and click **Submit**.



## Grant IAM permissions to the Google SecOps service account

  1. Go to **Cloud Storage** > **Buckets**.
  2. Click on `netskope-alerts-logs`.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. **Add principals** : Paste the Google SecOps service account email.
  6. **Assign roles** : Select **Storage Object Viewer**. (Use **Storage Object Admin** if using a deletion option in the feed).
  7. Click **Save**.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`app_activity_label` | `additional.fields` | Merged  
`count_label` | `additional.fields` | Merged  
`object_field` | `additional.fields` | Merged  
`object_id_field` | `additional.fields` | Merged  
`object_type_field` | `additional.fields` | Merged  
`publisher_cn_field` | `additional.fields` | Merged  
`publisher_name_field` | `additional.fields` | Merged  
`site_label` | `additional.fields` | Merged  
`tunnel_id_field` | `additional.fields` | Merged  
`tunnel_type_field` | `additional.fields` | Merged  
`access_method` | `extensions.auth.auth_details` | Directly mapped  
`accessmethod` | `extensions.auth.auth_details` | Mapped when `result` != ``  
`activity` | `extensions.auth.type` | Mapped: `Login Failed` → `MACHINE`, `Login Successful` → `MACHINE`, `Login Attempt` → `MACHINE`  
`published` | `metadata.event_timestamp` | Parsed as `RFC 3339`  
`timestamp` | `metadata.event_timestamp` | Parsed as `RFC 3339`  
`Protocol` | `metadata.event_type` | Mapped: `HTTP` → `NETWORK_HTTP`  
`activity` | `metadata.event_type` | Mapped: `Introspection Scan` → `EMAIL_UNCATEGORIZED`, `Login Failed` → `USER_LOGIN`, `Login ...  
`has_principal` | `metadata.event_type` | Mapped: `true` → `NETWORK_HTTP`, `true` → `NETWORK_CONNECTION`  
`Id` | `metadata.product_log_id` | Mapped when `result` != ``  
`_id` | `metadata.product_log_id` | Directly mapped  
`protocol` | `network.application_protocol` | Renamed/mapped  
`from_user` | `network.email.from` | Directly mapped  
`useridemail` | `network.email.to` | Mapped: `@` → `useridemail`  
`user_agent` | `network.http.parsed_user_agent` | Renamed/mapped  
`useragent` | `network.http.parsed_user_agent` | Renamed/mapped  
`browser_version` | `network.http.parsed_user_agent.browser_version` | Directly mapped  
`browserversion` | `network.http.parsed_user_agent.browser_version` | Mapped when `result` != ``  
`page` | `network.http.referral_url` | Directly mapped  
`referer` | `network.http.referral_url` | Renamed/mapped  
`Browser` | `network.http.user_agent` | Mapped when `result` != ``  
`browser` | `network.http.user_agent` | Directly mapped  
`user_agent` | `network.http.user_agent` | Directly mapped  
`useragent` | `network.http.user_agent` | Directly mapped  
`ip_protocol_out` | `network.ip_protocol` | Directly mapped  
`server_bytes` | `network.received_bytes` | Renamed/mapped  
`client_bytes` | `network.sent_bytes` | Renamed/mapped  
`browserSessionid` | `network.session_id` | Mapped when `result` != ``  
`browser_sess` | `network.session_id` | Renamed/mapped  
`network_session_id` | `network.session_id` | Renamed/mapped  
`ja3` | `network.tls.client.ja3` | Directly mapped  
`ja3s` | `network.tls.server.ja3s` | Directly mapped  
`netskope_pop` | `observer.hostname` | Directly mapped  
`organization_unit` | `principal.administrative_domain` | Directly mapped  
`Host` | `principal.asset.hostname` | Mapped when `result` != ``  
`hostname` | `principal.asset.hostname` | Directly mapped  
`instance_id` | `principal.asset.hostname` | Directly mapped  
`srcIP` | `principal.asset.ip` | Merged  
`srcip` | `principal.asset.ip` | Merged  
`Host` | `principal.hostname` | Mapped when `result` != ``  
`hostname` | `principal.hostname` | Directly mapped  
`instance_id` | `principal.hostname` | Directly mapped  
`srcIP` | `principal.ip` | Merged  
`srcip` | `principal.ip` | Merged  
`src_location` | `principal.location.city` | Renamed/mapped  
`src_country` | `principal.location.country_or_region` | Renamed/mapped  
`srccountry` | `principal.location.country_or_region` | Mapped when `result` != ``  
`src_region` | `principal.location.name` | Renamed/mapped  
`srcregion` | `principal.location.name` | Mapped when `result` != ``  
`srclatitude` | `principal.location.region_coordinates.latitude` | Renamed/mapped  
`srclongitude` | `principal.location.region_coordinates.longitude` | Renamed/mapped  
`src_latitude` | `principal.location.region_latitude` | Renamed/mapped  
`src_longitude` | `principal.location.region_longitude` | Renamed/mapped  
`os` | `principal.platform` | Mapped: `(?i)Windows` → `WINDOWS`, `(?i)MAC` → `MAC`, `(?i)LINUX` → `LINUX`  
`os_version` | `principal.platform_version` | Renamed/mapped  
`osversion` | `principal.platform_version` | Mapped when `result` != ``  
`srcport` | `principal.port` | Renamed/mapped  
`from_user_category_label` | `principal.resource.attribute.labels` | Merged  
`Device` | `principal.resource.resource_subtype` | Mapped when `result` != ``  
`device` | `principal.resource.resource_subtype` | Directly mapped  
`User` | `principal.user.email_addresses` | Merged  
`matched_username` | `principal.user.email_addresses` | Merged  
`user` | `principal.user.email_addresses` | Merged  
`user` | `principal.user.userid` | Renamed/mapped  
`_security_result` | `security_result` | Merged  
`security_result1` | `security_result` | Merged  
`app` | `target.application` | Renamed/mapped  
`appName` | `target.application` | Mapped when `result` != ``  
`domain` | `target.asset.hostname` | Directly mapped  
`dstIP` | `target.asset.ip` | Merged  
`dst_ip` | `target.asset.ip` | Merged  
`dstip` | `target.asset.ip` | Merged  
`dlp_file` | `target.file.full_path` | Directly mapped  
`file_path` | `target.file.full_path` | Directly mapped  
`md5` | `target.file.md5` | Renamed/mapped  
`file_type` | `target.file.mime_type` | Directly mapped  
`sha256` | `target.file.sha256` | Renamed/mapped  
`file_size` | `target.file.size` | Renamed/mapped  
`domain` | `target.hostname` | Directly mapped  
`dstIP` | `target.ip` | Merged  
`dst_ip` | `target.ip` | Merged  
`dstip` | `target.ip` | Merged  
`dst_location` | `target.location.city` | Renamed/mapped  
`dst_country` | `target.location.country_or_region` | Renamed/mapped  
`dstcountry` | `target.location.country_or_region` | Mapped when `result` != ``  
`dst_region` | `target.location.name` | Renamed/mapped  
`dstregion` | `target.location.name` | Mapped when `result` != ``  
`dstlatitude` | `target.location.region_coordinates.latitude` | Renamed/mapped  
`dstlongitude` | `target.location.region_coordinates.longitude` | Renamed/mapped  
`dstport` | `target.port` | Renamed/mapped  
`app_session_label` | `target.resource.attribute.labels` | Merged  
`to_user_category_label` | `target.resource.attribute.labels` | Merged  
`Url` | `target.url` | Mapped when `result` != ``  
`url` | `target.url` | Renamed/mapped  
`to_user` | `target.user.email_addresses` | Mapped: `^.+@.+$` → `touser`  
`touser` | `target.user.email_addresses` | Mapped: `^.+@.+$` → `touser`  
N/A | `extensions.auth.type` | Constant: `MACHINE`  
N/A | `metadata.event_type` | Constant: `GENERIC_EVENT`  
N/A | `metadata.product_name` | Constant: `Netskope Alert`  
N/A | `metadata.vendor_name` | Constant: `Netskope`  
N/A | `network.http.parsed_user_agent.family` | Constant: `USER_DEFINED`  
N/A | `principal.platform` | Constant: `WINDOWS`  
N/A | `principal.resource.type` | Constant: `DEVICE`  
N/A | `target.asset.hostname` | Constant: `dsthost`  
N/A | `target.hostname` | Constant: `dsthost`  
`action` | `security_result.action_details` | Mapped from changelog  
`dlp_rule_severity` | `security_result.severity` | Mapped from changelog  
`useragent" and "user_agent` | `network.http.user_agent` | Mapped from changelog  
`traffic_type` | `security_result.detection_fields` | Mapped from changelog  
`device` | `principal.resource.resource_sub_type` | Mapped from changelog  
`type` | `security_result.detection_fields` | Mapped from changelog  
`app_session_id` | `target.resource.attribute.labels` | Mapped from changelog  
`malware_severity` | `security_result.severity` | Mapped from changelog  
`malware_type` | `security_result.detection_fields` | Mapped from changelog  
`threat_match_field` | `security_result.detection_fields` | Mapped from changelog  
`cci", "ccl` | `additional.fields` | Mapped from changelog  
`dlp_profile` | `security_result.rule_type` | Mapped from changelog  
`dlp_rule` | `security_result.rule_name` | Mapped from changelog  
`security_result.alert_state` | `ALERTING` | Mapped from changelog  
`security_result.alert_state` | `NOT_ALERTING` | Mapped from changelog  
`security_result.alert_state` | `UNSPECIFIED` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/netskope-alert-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
