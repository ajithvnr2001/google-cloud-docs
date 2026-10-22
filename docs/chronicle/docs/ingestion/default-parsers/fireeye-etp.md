---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fireeye-etp/
title: Collect Trellix Email Security Cloud (formerly FireEye ETP) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:08:21.958606+00:00
---

# Collect Trellix Email Security Cloud (formerly FireEye ETP) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fireeye-etp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Trellix Email Security Cloud (formerly FireEye ETP) logs

**Parser Version:** 10.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Trellix Email Security - Cloud Edition (formerly known as FireEye ETP) logs to Google Security Operations using Google Cloud Storage V2 via a Cloud Run function.

Trellix Email Security - Cloud Edition, is a cloud-based email security gateway that protects against advanced email threats including phishing, malware, business email compromise, and impersonation attacks. The solution provides comprehensive inbound and outbound email security with URL defense, attachment sandboxing, and real-time threat intelligence powered by the Trellix Advanced Research Center.

## Before you begin

Make sure that you have the following prerequisites:

  * A Google SecOps instance.
  * A Google Cloud project with the following APIs enabled: 
    * Cloud Storage
    * Cloud Run functions
    * Cloud Scheduler
    * Pub/Sub
    * Cloud Build
  * Permissions to create and manage GCS buckets, Cloud Run functions, Pub/Sub topics, and Cloud Scheduler jobs.
  * Privileged access to the FireEye ETP (Trellix Email Security - Cloud Edition) admin console.
  * Administrator permissions to create API keys in the Trellix portal.
  * A FireEye ETP API key with access to the Alerts endpoint.



## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project.
  3. In the navigation menu, go to **Cloud Storage** > **Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (e.g., `fireeye-etp-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (e.g., `us-central1`)  
**Storage class** | **Standard** (recommended for frequently accessed logs)  
**Access control** | **Uniform** (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Collect FireEye ETP API credentials

To enable the Cloud Run function to retrieve alerts from FireEye ETP, you need to create an API key with appropriate permissions.

**Note:** FireEye ETP uses API Key authentication via the `x-fireeye-api-key` HTTP header. The API key must be associated with the Email Threat Prevention product.

### Create API key

  1. Sign in to the **FireEye ETP** admin console.
  2. In the top navigation bar, click **My Settings**.
  3. Click the **API Keys** tab.
  4. Click **Create API Key**.
  5. In the **Products** section, select **Email Threat Prevention**.
  6. In the **Entitlements** section, select all available entitlements.
  7. Click **Create** or **Generate**.



### Record API credentials

Record the following information:

  * **API Key** : Your unique API key.
  * **Base URL** : The fully qualified domain name for your region (e.g., `etp.us.fireeye.com`).

**Important:** Copy and save the API key immediately. Some versions of the interface may not allow you to retrieve it after closing the dialog.

Common base URLs include:

  * `etp.us.fireeye.com` (US)
  * `etp.eu.fireeye.com` (EU)
  * `etp.ap.fireeye.com` (APAC)



### Verify API permissions

Product/Entitlement | Purpose  
---|---  
**Email Threat Prevention** | Access to email alerts, trace data, and threat information  
**All Entitlements** | Full access to alerts, email trace, and quarantine APIs  
  
### Test API access

  * Verify that your API key is valid:
        
        curl -s -o /dev/null -w "%{http_code}" \
            -H "x-fireeye-api-key: YOUR_API_KEY" \
            "[https://etp.us.fireeye.com/api/v1/alerts?size=1](https://etp.us.fireeye.com/api/v1/alerts?size=1)"
        




A **200** response code confirms that the API key is valid.

## Create service account for Cloud Run function

The Cloud Run function requires a service account with permissions to write logs to GCS and receive Pub/Sub messages.

  1. In the **Google Cloud Console** , go to **IAM & Admin** > **Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide a name (e.g., `fireeye-etp-ingestion`) and description.
  4. Grant the following roles: 
     * **Storage Object Admin**
     * **Cloud Run Invoker**
  5. Click **Done**.



## Create Pub/Sub topic

  1. In the **Google Cloud Console** , go to **Pub/Sub** > **Topics**.
  2. Click **Create Topic**.
  3. **Topic ID** : `fireeye-etp-trigger`.
  4. Click **Create**.



## Create Cloud Run function

Create a Cloud Run function that queries the FireEye ETP Alerts API and writes results as NDJSON to GCS.

### Prepare the function code

  1. In the **Google Cloud Console** , go to **Cloud Run functions**.
  2. Click **Create function**.
  3. **Environment** : **2nd gen**.
  4. **Function name** : `fireeye-etp-ingestion`.
  5. **Region** : Select the same region as your GCS bucket.
  6. **Trigger type** : **Cloud Pub/Sub**.
  7. **Cloud Pub/Sub topic** : `fireeye-etp-trigger`.
  8. **Service account** : Select the service account created earlier.
  9. Click **Next**.
  10. **Runtime** : **Python 3.11** (or later).
  11. **Entry point** : `main`.
  12. In **main.py** , paste the following:
         
         """Cloud Run function to ingest FireEye ETP alerts into GCS."""
         
         import json
         import os
         import time
         from datetime import datetime, timedelta, timezone
         
         import functions_framework
         import urllib3
         from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
         
         GCS_BUCKET = os.environ["GCS_BUCKET"]
         GCS_PREFIX = os.environ.get("GCS_PREFIX", "fireeye_etp")
         STATE_KEY = os.environ.get("STATE_KEY", "fireeye_etp_state.json")
         API_KEY = os.environ["API_KEY"]
         API_BASE = os.environ.get("API_BASE", "etp.us.fireeye.com")
         MAX_RECORDS = int(os.environ.get("MAX_RECORDS", "10000"))
         PAGE_SIZE = int(os.environ.get("PAGE_SIZE", "100"))
         LOOKBACK_HOURS = int(os.environ.get("LOOKBACK_HOURS", "1"))
         
         http = urllib3.PoolManager()
         gcs = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
         
         def _load_state() -> dict:
                 """Load the last event time from GCS state file."""
                 bucket = gcs.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(GCS_BUCKET)
                 blob = bucket.blob(f"{GCS_PREFIX}/{STATE_KEY}")
                 if blob.exists():
                         return json.loads(blob.[download_as_text](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_download_as_text)())
                 return {}
         
         def _save_state(state: dict) -> None:
                 """Persist the state dict back to GCS."""
                 bucket = gcs.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(GCS_BUCKET)
                 blob = bucket.blob(f"{GCS_PREFIX}/{STATE_KEY}")
                 blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(
                         json.dumps(state), content_type="application/json"
                 )
         
         def _api_get(path: str, params: dict, retries: int = 5) -> dict:
                 """Execute a GET request against the FireEye ETP API with retry on 429."""
                 url = f"https://{API_BASE}{path}"
                 headers = {
                         "x-fireeye-api-key": API_KEY,
                         "Accept": "application/json",
                 }
                 backoff = 2
                 for attempt in range(retries):
                         resp = http.request(
                                 "GET", url, headers=headers, fields=params
                         )
                         if resp.status == 200:
                                 return json.loads(resp.data.decode("utf-8"))
                         if resp.status == 429:
                                 wait = backoff * (2 ** attempt)
                                 print(
                                         f"Rate limited (429). Retrying in {wait}s "
                                         f"(attempt {attempt + 1}/{retries})."
                                 )
                                 time.sleep(wait)
                                 continue
                         raise RuntimeError(
                                 f"FireEye ETP API error: {resp.status} — {resp.data.decode('utf-8')}"
                         )
                 raise RuntimeError(
                         "FireEye ETP API rate limit exceeded after maximum retries."
                 )
         
         def _fetch_alerts(since: str) -> list:
                 """Fetch alerts from FireEye ETP with offset-based pagination."""
                 all_alerts = []
                 offset = 0
                 while len(all_alerts) < MAX_RECORDS:
                         params = {
                                 "from_last_modified_on": since,
                                 "size": str(PAGE_SIZE),
                                 "offset": str(offset),
                         }
                         data = _api_get("/api/v1/alerts", params)
                         alerts = data.get("data", [])
                         if not alerts:
                                 break
                         all_alerts.extend(alerts)
                         offset += len(alerts)
                         if len(alerts) < PAGE_SIZE:
                                 break
                 return all_alerts[:MAX_RECORDS]
         
         def _write_ndjson(alerts: list, run_ts: str) -> str:
                 """Write alerts as NDJSON to GCS and return the blob path."""
                 bucket = gcgcs.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)CS_BUCKET)
                 blob_path = (
                         f"{GCS_PREFIX}/year={run_ts[:4]}/month={run_ts[5:7]}/"
                         f"day={run_ts[8:10]}/{run_ts}_alerts.ndjson"
                 )
                 blob = bucket.blob(blob_path)
                 ndjson = "\n".join(json.dumps(a, separators=(",", ":")) for a in alerts)
                 blob.up[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)djson, content_type="application/x-ndjson")
                 return blob_path
         
         @functions_framework.cloud_event
         def main(cloud_event):
                 """Entry point triggered by Pub/Sub via Cloud Scheduler."""
                 state = _load_state()
                 now = datetime.now(timezone.utc)
                 since = st[state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state)et(
                         "last_event_time",
                         (now - timedelta(hours=LOOKBACK_HOURS)).strftime(
                                 "%Y-%m-%dT%H:%M:%S.000"
                         ),
                 )
                 print(f"Fetching FireEye ETP alerts since {since}.")
                 alerts = _fetch_alerts(since)
                 if not alerts:
                         print("No new alerts found.")
                         return "OK"
                 run_ts = now.strftime("%Y-%m-%dT%H%M%SZ")
                 blob_path = _write_ndjson(alerts, run_ts)
                 print(f"Wrote {len(alerts)} alerts to gs://{GCS_BUCKET}/{blob_path}.")
                 latest = max(
                         a.get("attributes", {})
                         .get("meta", {})
                         .get("last_modified_on", since)
                         for a in alerts
                 )
                 state["last_event_time"] = latest
                 _save_state(state)
                 print(f"State updated. last_event_time={latest}.")
                 return "OK"
         

  13. In **requirements.txt** , paste:
         
         functions-framework==3.*
         google-cloud-storage==2.*
         urllib3==2.*
         




### Configure environment variables

Under **Runtime environment variables** , add the following:

Variable | Example Value  
---|---  
`GCS_BUCKET` | `fireeye-etp-logs`  
`GCS_PREFIX` | `fireeye_etp`  
`STATE_KEY` | `fireeye_etp_state.json`  
`API_KEY` | _Your FireEye ETP API key_  
`API_BASE` | `etp.us.fireeye.com`  
`MAX_RECORDS` | `10000`  
`PAGE_SIZE` | `100`  
`LOOKBACK_HOURS` | `1`  
  
  1. Set **Memory allocated** to **256 MB** and **Timeout** to **540** seconds.
  2. Click **Deploy**.



## Create Cloud Scheduler job

  1. In the **Google Cloud Console** , go to **Cloud Scheduler**.
  2. Click **Create Job**.
  3. **Name** : `fireeye-etp-ingestion-schedule`.
  4. **Frequency** : `*/5 * * * *` (every 5 minutes).
  5. **Timezone** : `UTC`.
  6. Click **Continue**.
  7. **Target type** : **Pub/Sub**.
  8. **Cloud Pub/Sub topic** : `fireeye-etp-trigger`.
  9. **Message body** : `{"run": true}`.
  10. Click **Create**.



## Retrieve the Google SecOps service account

  1. Go to **SIEM Settings** > **Feeds**.
  2. Click **Add New Feed** and select **Configure a single feed**.
  3. **Feed name** : `FireEye ETP Alerts`.
  4. **Source type** : **Google Cloud Storage V2**.
  5. **Log type** : **FireEye ETP**.
  6. Click **Get Service Account** and copy the email displayed.
  7. Click **Next**.
  8. **Storage bucket URL** : `gs://fireeye-etp-logs/fireeye_etp/` (Include the trailing slash).
  9. **Source deletion option** : Select according to your preference.
  10. Click **Next** , review, and click **Submit**.



## Grant IAM permissions

The service account needs **Storage Object Viewer** role on your bucket.

  1. Go to **Cloud Storage** > **Buckets**.
  2. Select your bucket and click the **Permissions** tab.
  3. Click **Grant access**.
  4. **Add principals** : Paste the Google SecOps service account email.
  5. **Assign roles** : Select **Storage Object Viewer**.
  6. Click **Save**.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
| about | Merged from about_field  
| about.file.full_path | Value from entry.attributes.email.attachment if not empty  
| about.file.md5 | Value from entry.attributes.alert.malware_md5  
| about.hostname | Extracted from entry.attributes.email.attachment  
| about.url | Normalized full_path if starts with hxxp  
| additional.fields | Merged from numerous internal labels and metadata fields  
| intermediary | Merged from intermediary  
| intermediary.ip | Merged from alert.smtp-message.ip_address  
| intermediary.location.country_or_region | Set to %{alert.smtp-message.country}  
| intermediary.user.email_addresses | Merged from src_email  
| metadata.description | Set to %{alert.name}  
| metadata.event_timestamp | Matched from accepted_timestamp, last_modified_on, or attack-time  
| metadata.event_type | Categorized based on network, user, or status update conditions  
| metadata.product_log_id | Set to message ID, attribute ID, or alert UUID  
| metadata.product_version | Set to %{version}  
| metadata.url_back_to_product | Set to %{entry.links.detail}  
| network.application_protocol | Set to "SMTP"  
| network.direction | Uppercased traffic_type (INBOUND/OUTBOUND)  
| network.dns_domain | Set to %{attributes.domain}  
| network.email.cc | Merged from cc fields in headers or arrays  
| network.email.from | Set from SMTP or header "from" fields  
| network.email.mail_id | Set from downstream or original message ID  
| network.email.subject | Merged from header subject fields  
| network.email.to | Merged from SMTP recipients or header "to" fields  
| principal.administrative_domain | Set to ETP message ID or source domain  
| principal.asset.hostname | Set to source host or downstream hostname  
| principal.asset.ip | Merged from sender_ip or source_ip fields  
| principal.asset.mac | Merged from source MAC if not empty  
| principal.hostname | Set to source host or downstream hostname  
| principal.ip | Merged from sender_ip or source_ip fields  
| principal.labels | Merged with mail_from and rcpt_to labels  
| principal.location.country_or_region | Set to source country code  
| principal.mac | Merged from source MAC if not empty  
| principal.user.email_addresses | Merged from alert.smtp-message.from  
| principal.user.user_display_name | Set from header display name fields  
| principal.user.userid | Set to original message ID  
| principal.email | Set from header email fields  
| security_result | Merged from multiple result structures  
| security_result.about.resource.attribute.creation_time | Matched from alert timestamp fields  
| security_result.action | "BLOCK" if status is dropped, quarantined, or deleted  
| security_result.action_details | Set to %{alert.action}  
| security_result.attack_details.tactics | Merged based on MITRE IDs or names  
| security_result.attack_details.techniques | Merged based on MITRE technique data  
| security_result.category | "MAIL_PHISHING" if threat_type matches Phishing  
| security_result.category_details | Merged from threat_type or verdict  
| security_result.detection_fields | Merged from numerous status and verdict labels  
| security_result.risk_score | Set to 5.0 or 10.0 based on severity  
| security_result.severity | Set to high/medium/low based on alert severity  
| security_result.severity_details | Set to %{alert_severity}  
| security_result.summary | Set from last_malware or downstream description  
| security_result.threat_id | Set from legacy ID or trace ID  
| security_result.threat_name | Set from summary or malware name  
| security_result.verdict_info | Merged if verdict is RISKWARE  
| target.asset.hostname | Set from delivery message hostname  
| target.file.first_seen_time | Matched from alert attack-time  
| target.file.first_submission_time | Matched from malware submission time  
| target.file.full_path | Set from original malware path  
| target.file.md5 | Set from malware MD5 sum  
| target.file.names | Merged from malware name  
| target.file.sha256 | Set from malware SHA256  
| target.file.size | Set from delivery message bytes  
| target.hostname | Set from delivery message hostname  
| target.labels | Merged with queue and protocol labels  
| target.url | Set from original malware URL  
| target.user.email_addresses | Merged from target email and recipient fields  
| metadata.vendor_name | Set to "FireEye"  
| metadata.product_name | Set to "ETP"  
`smtp-message.threat_type` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`smtp-message.protocol` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`entry.attributes.email.smtp.rcpt_to` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`entry.attributes.email.smtp.mail_from` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`alert.smtp-message.last-malware` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`alert.smtp-message.protocol` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`alert.smtp-message.queue-id` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`alert.ack` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`mta_msg_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`msg` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`domain` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`original` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`alert_date` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`smtp-message.ip_address` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`smtp-message.threat_type` | `event.idm.read_only_udm.security_result.summary` | Mapped from changelog  
`smtp-message.threat_type_description` | `event.idm.read_only_udm.security_result.description` | Mapped from changelog  
`email-header.to` | `event.idm.read_only_udm.network.email.to` | Mapped from changelog  
`smtp-message.to` | `event.idm.read_only_udm.network.email.to` | Mapped from changelog  
`email-header.from` | `event.idm.read_only_udm.network.email.from` | Mapped from changelog  
`email-header.cc` | `event.idm.read_only_udm.network.email.cc` | Mapped from changelog  
`email-header.subject` | `event.idm.read_only_udm.network.email.subject` | Mapped from changelog  
`email-header.message-id` | `event.idm.read_only_udm.network.email.mail_id` | Mapped from changelog  
`malware.name` | `event.idm.read_only_udm.security_result.threat_name` | Mapped from changelog  
`malware.stype` | `event.idm.read_only_udm.security_result.threat_id` | Mapped from changelog  
`sha256` | `event.idm.read_only_udm.security_result.about.file.sha256` | Mapped from changelog  
`md5` | `event.idm.read_only_udm.security_result.about.file.md5` | Mapped from changelog  
`email_status` | `event.idm.read_only_udm.security_result.action` | Mapped from changelog  
`email_status` | `event.idm.read_only_udm.security_result.action_details` | Mapped from changelog  
`smtp-message.from` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`smtp-message.last-malware` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`smtp-message.country` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`smtp-message.queue-id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ack` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`is_read` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`alert.smtp-message.threat_type_description` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`custom.riskware_action` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`custom.riskware_result` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`alert_type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`traffic_type` | `event.idm.read_only_udm.network.direction` | Mapped from changelog  
`domain_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`,` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`custom` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`alert.smtp-message.threat_type` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`alert.email-header.cc` | `event.idm.read_only_udm.network.email.cc` | Mapped from changelog  
`action_yara` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`verdict_yara` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`delivery_timestamp` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`syslog_process` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`timestamp` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`usr_display_name` | `event.idm.read_only_udm.principal.user.user_display_name` | Mapped from changelog  
`is_retro` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`alert.email-header.to` | `event.idm.read_only_udm.target.user.email_addresses` | Mapped from changelog  
`alert.action` | `event.idm.read_only_udm.security_result.action_details` | Mapped from changelog  
`alert.attack-time` | `event.idm.read_only_udm.target.file.first_seen_time` | Mapped from changelog  
`alert.dst.smtp-to` | `event.idm.read_only_udm.target.user.email_addresses` | Mapped from changelog  
`alert.email-header.from` | `event.idm.read_only_udm.network.email.from` | Mapped from changelog  
`alert.email-header.message-id` | `event.idm.read_only_udm.network.email.mail_id` | Mapped from changelog  
`alert.email-header.subject` | `event.idm.read_only_udm.network.email.subject` | Mapped from changelog  
`alert.ack` | `event.idm.read_only_udm.target.labels` | Mapped from changelog  
`alert.explanation.malware-detected.malware.application` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`alert.explanation.malware-detected.malware.downloaded-at` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`alert.explanation.malware-detected.malware.executed-at` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`alert.explanation.malware-detected.malware.md5sum` | `event.idm.read_only_udm.target.file.md5` | Mapped from changelog  
`alert.explanation.malware-detected.malware.md5sum` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`alert.explanation.malware-detected.malware.name` | `event.idm.read_only_udm.target.file.names` | Mapped from changelog  
`alert.explanation.malware-detected.malware.original` | `event.idm.read_only_udm.target.url` | Mapped from changelog  
`alert.explanation.malware-detected.malware.original` | `event.idm.read_only_udm.target.file.full_path` | Mapped from changelog  
`alert.explanation.malware-detected.malware.original` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`alert.explanation.malware-detected.malware.profile` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`alert.explanation.malware-detected.malware.sha256` | `event.idm.read_only_udm.target.file.sha256` | Mapped from changelog  
`alert.explanation.malware-detected.malware.sha256` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`alert.explanation.malware-detected.malware.stype` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`alert.explanation.malware-detected.malware.submitted-at` | `event.idm.read_only_udm.target.file.first_submission_time` | Mapped from changelog  
`alert.explanation.malware-detected.malware.type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`alert.interface.interface` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`alert.interface.mode` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`alert.name` | `event.idm.read_only_udm.metadata.description` | Mapped from changelog  
`alert.occurred` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`alert.sc-version` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`alert.severity` | `event.idm.read_only_udm.security_result.severity` | Mapped from changelog  
`alert.smtp-message.country` | `event.idm.read_only_udm.intermediary.location.country_or_region` | Mapped from changelog  
`alert.smtp-message.date` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`alert.smtp-message.from` | `event.idm.read_only_udm.principal.user.email_addresses` | Mapped from changelog  
`alert.smtp-message.ip_address` | `event.idm.read_only_udm.intermediary.ip` | Mapped from changelog  
`alert.smtp-message.last-malware` | `event.idm.read_only_udm.target.labels` | Mapped from changelog  
`alert.smtp-message.protocol` | `event.idm.read_only_udm.target.labels` | Mapped from changelog  
`alert.smtp-message.queue-id` | `event.idm.read_only_udm.target.labels` | Mapped from changelog  
`alert.smtp-message.to` | `event.idm.read_only_udm.network.email.to` | Mapped from changelog  
`alert.src.domain` | `event.idm.read_only_udm.principal.administrative_domain` | Mapped from changelog  
`alert.src.smtp-mail-from` | `event.idm.read_only_udm.principal.user.email_addresses` | Mapped from changelog  
`alert.uuid` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`mitre_mapping.bale.bale_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`mitre_mapping.bale.name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`mitre_mapping.bale.os_change_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`mitre_mapping.bale.severity` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`mitre_mapping.bale.description` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`mitre_mapping.bale.id` | `event.idm.read_only_udm.security_result.attack_details.techniques` | Mapped from changelog  
`tactics_data` | `event.idm.read_only_udm.security_result.attack_details.tactics` | Mapped from changelog  
`alert.src.url` | `event.idm.read_only_udm.principal.url` | Mapped from changelog  
`mta_msg_id` | `event.idm.read_only_udm.target.labels` | Mapped from changelog  
`msg` | `event.idm.read_only_udm.about.labels` | Mapped from changelog  
`parent_uuid` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`verdict` | `event.idm.read_only_udm.security_result.verdict_info` | Mapped from changelog  
`version` | `event.idm.read_only_udm.metadata.product_version` | Mapped from changelog  
`report_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`object_uuid` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`type", "InternalId", "attributes.acceptedDateTime", "attributes.lastModifiedDateTime", "attributes.senderSMTP", "attributes.status", and "attributes.urlDomains` | `additional.fields` | Mapped from changelog  
`attributes.countryCode` | `principal.location.country_or_region` | Mapped from changelog  
`attributes.senderIP` | `principal.ip` | Mapped from changelog  
`attributes.recipientSMTP` | `network.email.to` | Mapped from changelog  
`attributes.senderHeader` | `network.email.from` | Mapped from changelog  
`attributes.subject` | `network.email.subject` | Mapped from changelog  
`alert.attributes.alert.malware_md5` | `about.file.md5` | Mapped from changelog  
`id", "alert.explanation.analysis","alert.explanation.malware_os_analysis","email.dod_report_id" and "email.status` | `security_result.detection_fields` | Mapped from changelog  
`alert.sha256` | `about.file.sha256` | Mapped from changelog  
`alert.severity` | `security_result.severity` | Mapped from changelog  
`email.smtp.mail_from` | `network.email.from` | Mapped from changelog  
`email.smtp.recipients` | `network.email.to` | Mapped from changelog  
`email.headers.subject` | `network.email.subject` | Mapped from changelog  
`email.source_ip` | `principal.ip` | Mapped from changelog  
`alert.explanation.malware_detected.malware.threat_type` | `security_result.category` | Mapped from changelog  
`alert.explanation.malware_detected.malware.trace_iden` | `security_result.threat_id` | Mapped from changelog  
`alert.explanation.malware_detected.malware.name` | `security_result.threat_name` | Mapped from changelog  
`email.source_country` | `principal.location.country_or_region` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fireeye-etp-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
