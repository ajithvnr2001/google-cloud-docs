---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/digitalguardian-edr/
title: Collect Fortra Digital Guardian (formerly Digital Guardian EDR) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:12:38.781388+00:00
---

# Collect Fortra Digital Guardian (formerly Digital Guardian EDR) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/digitalguardian-edr/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Fortra Digital Guardian (formerly Digital Guardian EDR) logs

**Parser Version:** 3.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Fortra Digital Guardian (formerly known as Digital Guardian EDR) logs to Google Security Operations using Google Cloud Storage V2 using a Cloud Run function.

Fortra Digital Guardian is a comprehensive data loss prevention and endpoint detection and response platform that provides visibility into system, user, and data events across endpoints, networks, and cloud applications. The Analytics & Reporting Cloud (ARC) service delivers advanced analytics, workflow, and reporting capabilities for holistic data protection. 

The Cloud Run function authenticates to the ARC Export API using OAuth 2.0, retrieves export data, acknowledges the bookmark to advance to the next chunk, writes the results as NDJSON to a GCS bucket, and Google SecOps ingests them through a GCS V2 feed.

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
  * Privileged access to the Digital Guardian Management Console (DGMC).
  * Access to Digital Guardian Analytics & Reporting Cloud (ARC) Tenant Settings.
  * Administrator permissions to configure Cloud Services in DGMC.
  * An Export Profile created in DGMC with a valid GUID.



## Create a Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage** > **Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (e.g., `digitalguardian-edr-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location closest to your instance (e.g., `us-central1`)  
**Storage class** | **Standard** (recommended for frequently accessed logs)  
**Access control** | **Uniform** (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.


**Note:** Record the bucket name. You will use it when configuring the Cloud Run function and the Google SecOps feed.

## Collect Digital Guardian API credentials

### Obtain API credentials

#### Get Client ID and Client Secret from ARC Tenant Settings

  1. Sign in to the **Digital Guardian ARC** portal.
  2. Go to **ARC Tenant Settings**.
  3. Copy and save the following values: 
     * **Tenant ID** : This is your Client ID.
     * **Authentication Token** : This is your Client Secret.

**Important:** Copy and save the Authentication Token immediately. It may not be retrievable later.

#### Get gateway URLs from DGMC

  1. Sign in to the **Digital Guardian Management Console (DGMC)**.
  2. Go to **System** > **Configuration** > **Cloud Services**.
  3. In the **API Access** section, record: 
     * **Access Gateway Base URL** : e.g., `https://accessgw-usw.msp.digitalguardian.com`
     * **Authorization Server URL** : e.g., `https://authsrv.msp.digitalguardian.com/as/token.oauth2`



### Create and configure an export profile

  1. In the **DGMC** , go to **Admin** > **Reports** > **Export Profiles**.
  2. Click **Create Export Profile**.
  3. Set **Export Format** to **JSON Flattened Table**.
  4. Click **Save** and copy the **GUID** from the profile details (format: `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`).



## Create the Cloud Run function

  * Prepare function source files

    * **requirements.txt**
          
          functions-framework==3.*
          google-cloud-storage==2.*
          urllib3==2.*
          

    * **main.py**
          
          """Cloud Run function to ingest Digital Guardian EDR logs into GCS."""
          
          import json
          import os
          import time
          import urllib.parse
          from datetime import datetime, timezone
          
          import functions_framework
          import urllib3
          from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
          
          GCS_BUCKET = os.environ["GCS_BUCKET"]
          GCS_PREFIX = os.environ.get("GCS_PREFIX", "digitalguardian_edr")
          STATE_KEY = os.environ.get("STATE_KEY", "digitalguardian_edr_state.json")
          AUTH_SERVER_URL = os.environ["AUTH_SERVER_URL"]
          ARC_SERVER_URL = os.environ["ARC_SERVER_URL"]
          CLIENT_ID = os.environ["CLIENT_ID"]
          CLIENT_SECRET = os.environ["CLIENT_SECRET"]
          EXPORT_PROFILE_GUID = os.environ["EXPORT_PROFILE_GUID"]
          MAX_RECORDS = int(os.environ.get("MAX_RECORDS", "10000"))
          
          http = urllib3.PoolManager()
          gcs = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
          
          def _get_access_token() -> str:
                  body = urllib.parse.urlencode({
                          "grant_type": "client_credentials",
                          "client_id": CLIENT_ID,
                          "client_secret": CLIENT_SECRET,
                          "scope": "client",
                  })
                  resp = http.request(
                          "POST",
                          AUTH_SERVER_URL,
                          body=body,
                          headers={"Content-Type": "application/x-www-form-urlencoded"},
                  )
                  if resp.status != 200:
                          raise RuntimeError(f"OAuth token request failed: {resp.status}")
                  return json.loads(resp.data.decode("utf-8"))["access_token"]
          
          def _arc_get(token: str, path: str, retries: int = 5) -> dict:
                  url = f"{ARC_SERVER_URL}{path}"
                  headers = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
                  backoff = 2
                  for attempt in range(retries):
                          resp = http.request("GET", url, headers=headers)
                          if resp.status == 200:
                                  return json.loads(resp.data.decode("utf-8"))
                          if resp.status == 429:
                                  time.sleep(backoff * (2 ** attempt))
                                  continue
                          raise RuntimeError(f"ARC API error: {resp.status}")
                  raise RuntimeError("ARC API rate limit exceeded.")
          
          def _arc_acknowledge(token: str) -> None:
                  url = f"{ARC_SERVER_URL}/rest/1.0/export/{EXPORT_PROFILE_GUID}/acknowledge"
                  headers = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
                  resp = http.request("POST", url, headers=headers)
                  if resp.status not in (200, 204):
                          raise RuntimeError(f"ARC acknowledge failed: {resp.status}")
          
          def _load_state() -> dict:
                  bucket = gcs.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(GCS_BUCKET)
                  blob = bucket.blob(f"{GCS_PREFIX}/{STATE_KEY}")
                  return json.loads(blob.[download_as_text](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_download_as_text)()) if blob.exists() else {}
          
          def _save_state(state: dict) -> None:
                  bucket = gcs.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(GCS_BUCKET)
                  blob = bucket.blob(f"{GCS_PREFIX}/{STATE_KEY}")
                  blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(json.dumps(state), content_type="application/json")
          
          def _fetch_export(token: str) -> list:
                  path = f"/rest/1.0/export/{EXPORT_PROFILE_GUID}"
                  data = _arc_get(token, path)
                  records = data if isinstance(data, list) else data.get("data", [])
                  return records[:MAX_RECORDS]
          
          def _write_ndjson(records: list, run_ts: str) -> str:
                  bucket = gcs.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(GCS_BUCKET)
                  blob_path = f"{GCS_PREFIX}/year={run_ts[:4]}/month={run_ts[5:7]}/day={run_ts[8:10]}/{run_ts}_export.ndjson"
                  blob = bucket.blob(blob_path)
                  ndjson = "\n".join(json.dumps(r, separators=(",", ":")) for r in records)
                  blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(ndjson, content_type="application/x-ndjson")
                  return blob_path
          
          @functions_framework.cloud_event
          def main(cloud_event):
                  state = _load_state()
                  now = datetime.now(timezone.utc)
                  token = _get_access_token()
                  records = _fetch_export(token)
                  if not records:
                          return "OK"
                  run_ts = now.strftime("%Y-%m-%dT%H%M%SZ")
                  blob_path = _write_ndjson(records, run_ts)
                  _arc_acknowledge(token)
                  state["last_run"] = now.isoformat()
                  _save_state(state)
                  return "OK"
          




## Retrieve the Google SecOps service account and configure the feed

  1. Go to **SIEM Settings** > **Feeds**.
  2. Click **Add New Feed**.
  3. Select **Google Cloud Storage V2** as the **Source type**.
  4. Select **Digital Guardian EDR** as the **Log type**.
  5. Click **Get Service Account** and copy the email address.
  6. Specify the **Storage bucket URL** : `gs://digitalguardian-edr-logs/digitalguardian_edr/` (ensure the trailing slash is included).



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`Application` | `target.application` | Value copied directly.  
`Bytes_Written` | `network.sent_bytes` | Converted to uinteger.  
`Command_Line` | `principal.process.command_line` | Cleaned of trailing quotes.  
`Computer_Name` | `principal.hostname` | Source hostname mapping.  
`Destination_File` | `target.file.names` | Direct mapping.  
`IP_Address` | `principal.ip` | Principal IP address.  
`Process_PID` | `principal.process.pid` | Process ID mapping.  
`Rule` | `security_result.rule_name` | Direct mapping.  
`Severity` | `security_result.severity` | Scaled to LOW, MEDIUM, HIGH, CRITICAL.  
`URL_Path` | `target.url` | Web destination mapping.  
`User_Name` | `principal.user.userid` | Extracted via grok.  
`security_action` | `security_result.action` | Direct mapping.  
N/A | `metadata.product_name` | Set to "Enterprise DLP Platform".  
N/A | `metadata.vendor_name` | Set to "DigitalGuardian".  
`Destination_File_Encryption` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`Alert_ID` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`Computer_Type` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`Operation` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`Printer_Jobname` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`Was_Destination_Classified` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`Was_Source_Classified` | `event.idm.read_only_udm.src.resource.attribute.labels` | Mapped from changelog  
`Source_File_Encryption` | `event.idm.read_only_udm.src.resource.attribute.labels` | Mapped from changelog  
`Source_Device_ID` | `event.idm.read_only_udm.src.resource.attribute.labels` | Mapped from changelog  
`Destination_Device_ID` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`Detail_Event_ID` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`Source_Device_Friendly_Name` | `event.idm.read_only_udm.src.resource.name` | Mapped from changelog  
`Source_Device_Product_Name` | `event.idm.read_only_udm.src.resource.resource_subtype` | Mapped from changelog  
`Source_Device_Serial_Number` | `event.idm.read_only_udm.src.resource.attribute.labels` | Mapped from changelog  
`File_Size_MB` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`Detail_File_Size_MB` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`Event_ID` | `event.idm.read_only_udm.security_result.rule_id` | Mapped from changelog  
`Block_Code` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`Policy` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`Agent_Local_Date` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Agent_Local_Time` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Agent_UTC_Time` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Source_File` | `src.file.names` | Mapped from changelog  
`Source_File_Extension` | `src.file.mime_type` | Mapped from changelog  
`Destination_File_Extension` | `target.file.mime_type` | Mapped from changelog  
`Source_Drive_Type` | `security_result.detection_fields` | Mapped from changelog  
`Destination_Drive_Type` | `security_result.detection_fields` | Mapped from changelog  
`Was_Removable` | `security_result.detection_fields` | Mapped from changelog  
`Was_Source_Removable` | `security_result.detection_fields` | Mapped from changelog  
`Product_Version` | `metadata.product_version` | Mapped from changelog  
`Process_SHA256_Hash` | `target.process.file.sha256` | Mapped from changelog  
`MD5_Checksum` | `target.process.file.md5` | Mapped from changelog  
`File_Extension` | `additional.fields` | Mapped from changelog  
`Protocol` | `network.ip_protocol` | Mapped from changelog  
`Command_Line1` | `principal.process.command_line` | Mapped from changelog  
`Network_Direction` | `network.direction` | Mapped from changelog  
`Local_Port` | `principal.port` | Mapped from changelog  
`Remote_Port` | `target.port` | Mapped from changelog  
`Dll_SHA1_Hash` | `target.process.file.sha1` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/digitalguardian-edr-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
