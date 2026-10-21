---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tenable-io/
title: Collect Tenable Vulnerability Management logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:38:06.638563+00:00
---

# Collect Tenable Vulnerability Management logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tenable-io/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Tenable Vulnerability Management logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Tenable Vulnerability Management (formerly Tenable.io) logs to Google Security Operations. It describes two ingestion methods: a Cloud Storage pipeline that pulls data from the Tenable export API, and a Tenable Data Stream that pushes data to an Amazon S3 bucket. Choose the method that matches your environment.

Tenable Vulnerability Management (formerly Tenable.io) is a cloud-based vulnerability management platform powered by Nessus technology that provides comprehensive vulnerability coverage with the ability to predict which security issues to remediate first.

The parser extracts vulnerability and asset findings from Tenable JSON logs and maps the fields to the UDM, handling domain, IPv4 and IPv6 indicators, severity, and asset attributes.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Privileged access to the **Tenable Vulnerability Management** console (the **Administrator** role)
  * For **Method 1 (Google Cloud Storage)** : a Google Cloud project with billing enabled and permissions to create Cloud Storage buckets, service accounts, Pub/Sub topics, Cloud Run functions, and Cloud Scheduler jobs
  * For **Method 2 (Amazon S3)** : an AWS account with permissions to create S3 buckets and Identity and Access Management (IAM) roles and users



Choose one of the following methods:

  * **Method 1: Google Cloud Storage**. A Cloud Run function pulls vulnerability and asset data from the Tenable export API and writes it to a Cloud Storage bucket. Use this method to keep the pipeline entirely on Google Cloud.
  * **Method 2: Amazon S3**. Tenable Data Stream continuously pushes your Tenable data to an Amazon S3 bucket. Use this method if you prefer the built-in Tenable push integration. Tenable Data Stream supports Amazon S3 only.



## Method 1: Google Cloud Storage

This method uses a Cloud Run function, triggered by Cloud Scheduler through Pub/Sub, to pull vulnerability and asset data from the Tenable Vulnerability Management export API and write it to a Cloud Storage bucket. Google SecOps then ingests the data from the bucket.

### Collect Tenable Vulnerability Management API credentials

  1. Sign in to **Tenable Vulnerability Management** at `https://cloud.tenable.com`.
  2. In the upper-right corner, click your user-profile icon and select **My Account**.
  3. Click **API Keys**.
  4. Click **Generate**.
  5. Copy and save the **Access Key** and **Secret Key**.

**Note:** The keys are shown only once. Generating new keys invalidates the existing keys. Use a dedicated integration user with at least the **Basic** role.



### Create a Google Cloud Storage bucket

  1. In the **Google Cloud console** , go to **Cloud Storage > Buckets**.
  2. Click **Create**.
  3. Provide the following configuration details: 
     * **Name** : Enter a globally unique name (for example, `tenable-vulnerability-logs`).
     * **Location type** : Choose a location.
     * **Storage class** : Select **Standard**.
  4. Click **Create**.



### Create a service account for the Cloud Run function

  1. In the **Google Cloud console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `tenable-collector-sa`.
     * **Service account description** : Enter `Service account for the Tenable export collector`.
  4. Click **Create and Continue**.
  5. Click **Done**.



### Grant the service account access to the bucket

  1. Go to **Cloud Storage > Buckets**.
  2. Click your bucket name (for example, `tenable-vulnerability-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Enter the service account email (for example, `tenable-collector-sa@PROJECT_ID.iam.gserviceaccount.com`).
     * **Assign roles** : Select **Storage Object Admin**.
  6. Click **Save**.



### Create a Pub/Sub topic

  1. In the **Google Cloud console** , go to **Pub/Sub > Topics**.
  2. Click **Create topic**.
  3. Enter a **Topic ID** (for example, `tenable-collector-trigger`).
  4. Click **Create**.



### Create the Cloud Run function to collect logs

The Cloud Run function is triggered by Pub/Sub messages from Cloud Scheduler. It authenticates to the Tenable export API with your API keys, runs the vulnerability and asset exports, and writes each export chunk to the bucket in JSON format.

  1. In the **Google Cloud console** , go to **Cloud Run**.
  2. Click **Create service**.
  3. Select **Function** to use the inline code editor.
  4. Provide the following configuration details: 
     * **Service name** : Enter `tenable-collector`.
     * **Region** : Select the region matching your bucket (for example, `us-central1`).
     * **Runtime** : Select **Python 3.12** or later.
  5. In the **Trigger** section: 
     1. Click **Add trigger**.
     2. Select **Cloud Pub/Sub**.
     3. In **Select a Cloud Pub/Sub topic** , select `tenable-collector-trigger`.
     4. Click **Save**.
  6. In the **Authentication** section, select **Require authentication**.
  7. Expand **Containers, Networking, Security** , and on the **Security** tab set **Service account** to `tenable-collector-sa`.
  8. On the **Containers > Variables & Secrets** tab, add the following environment variables:

Variable name | Example value  
---|---  
`TIO_ACCESS_KEY` | `your-tenable-access-key`  
`TIO_SECRET_KEY` | `your-tenable-secret-key`  
`GCS_BUCKET` | `tenable-vulnerability-logs`  
`GCS_PREFIX` | `tenable/`  
`NUM_ASSETS` | `1000`  
`ASSET_CHUNK_SIZE` | `1000`  
`SEVERITIES` | `low,medium,high,critical`  
`HTTP_TIMEOUT` | `120`  
**Note:** Use the **Access Key** and **Secret Key** from the **Collect Tenable Vulnerability Management API credentials** section. For production, store the keys in **Secret Manager** and reference them as secrets instead of plain environment variables.
  9. Set the **Request timeout** to `600` seconds and **Memory** to **512 MiB** or higher.

  10. Click **Create**. After the service is created, the inline code editor opens.




#### Add the function code

  1. In the **Function entry point** field, enter `main`.
  2. In the inline code editor, replace the contents of `requirements.txt` with the following:
         
         functions-framework==3.*
         google-cloud-storage==2.*
         requests==2.*
         

  3. Replace the contents of `main.py` with the following code:
         
         import json
         import os
         import time
         
         import functions_framework
         import requests
         from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
         
         BASE = "https://cloud.tenable.com"
         ACCESS_KEY = os.environ["TIO_ACCESS_KEY"]
         SECRET_KEY = os.environ["TIO_SECRET_KEY"]
         GCS_BUCKET = os.environ["GCS_BUCKET"]
         GCS_PREFIX = os.environ.get("GCS_PREFIX", "tenable/")
         NUM_ASSETS = int(os.environ.get("NUM_ASSETS", "1000"))
         ASSET_CHUNK_SIZE = int(os.environ.get("ASSET_CHUNK_SIZE", "1000"))
         SEVERITIES = [s for s in os.environ.get("SEVERITIES", "low,medium,high,critical").split(",") if s]
         HTTP_TIMEOUT = int(os.environ.get("HTTP_TIMEOUT", "120"))
         
         HEADERS = {
             "X-ApiKeys": f"accessKey={ACCESS_KEY};secretKey={SECRET_KEY}",
             "Content-Type": "application/json",
             "Accept": "application/json",
         }
         
         storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
         
         def _request(method, path, **kwargs):
             """Call the Tenable API, honoring HTTP 429 Retry-After. Do not multi-thread."""
             while True:
                 resp = requests.request(method, f"{BASE}{path}", headers=HEADERS, timeout=HTTP_TIMEOUT, **kwargs)
                 if resp.status_code == 429:
                     time.sleep(int(resp.headers.get("Retry-After", "30")))
                     continue
                 resp.raise_for_status()
                 return resp
         
         def _write_chunk(bucket, name, payload):
             """Write one export chunk (a JSON array) to the bucket."""
             blob = bucket.blob(f"{GCS_PREFIX}{name}")
             blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(json.dumps(payload), content_type="application/json")
         
         def _run_export(bucket, label, request_path, status_kind, body):
             """Request an export, poll until FINISHED, and write each chunk to the bucket."""
             export_uuid = _request("POST", request_path, json=body).json()["export_uuid"]
             written = set()
             while True:
                 status = _request("GET", f"/{status_kind}/export/{export_uuid}/status").json()
                 for chunk_id in status.get("chunks_available", []):
                     if chunk_id in written:
                         continue
                     chunk = _request("GET", f"/{status_kind}/export/{export_uuid}/chunks/{chunk_id}").json()
                     _write_chunk(bucket, f"{label}_{export_uuid}_{chunk_id}.json", chunk)
                     written.add(chunk_id)
                 state = status.get("status")
                 if state == "FINISHED":
                     break
                 if state in ("ERROR", "CANCELLED"):
                     raise RuntimeError(f"{label} export {export_uuid} ended as {[state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state)}")
                 time.sleep(15)
             print(f"{label}: wrote {len(written)} chunk(s) for export {export_uuid}")
         
         @functions_framework.cloud_event
         def main(cloud_event):
             bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(GCS_BUCKET)
             # Vulnerabilities: request path and status/chunk paths both use /vulns/export; body uses num_assets.
             _run_export(
                 bucket, "vulns", "/vulns/export", "vulns",
                 {"num_assets": NUM_ASSETS, "include_unlicensed": False, "filters": {"severity": SEVERITIES}},
             )
             # Assets: request path is /assets/v2/export (body uses chunk_size); status/chunk paths drop the v2.
             _run_export(
                 bucket, "assets", "/assets/v2/export", "assets",
                 {"chunk_size": ASSET_CHUNK_SIZE},
             )
             return "ok"
         

  4. Click **Save and deploy**.




### Create a Cloud Scheduler job

  1. In the **Google Cloud console** , go to **Cloud Scheduler**.
  2. Click **Create job**.
  3. Provide the following configuration details: 
     * **Name** : Enter `tenable-collector-schedule`.
     * **Region** : Select the same region as the Cloud Run function.
     * **Frequency** : Enter a cron schedule (for example, `0 */6 * * *` to run every six hours).
     * **Timezone** : Select your timezone.
  4. For **Target type** , select **Pub/Sub**.
  5. Select the `tenable-collector-trigger` topic.
  6. In the **Message body** , enter `run`.
  7. Click **Create**.



### Configure a feed in Google SecOps to ingest from Google Cloud Storage

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Tenable Vulnerability Management GCS`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **tenable.io** as the **Log type**.
  7. Click **Get Service Account**. Copy the displayed service account email.
  8. Click **Next**.
  9. Specify values for the following input parameters: 
     * **Storage bucket URI** : Enter the bucket URI, including the prefix (for example, `gs://tenable-vulnerability-logs/tenable/`).
     * **Source deletion option** : Select the deletion option according to your preference.
     * **Maximum File Age** : Include files modified in the last number of days. Default is 180 days.
  10. Click **Next** , review the configuration, and then click **Submit**.



### Grant the Google SecOps service account access to the bucket

  1. Go to **Cloud Storage > Buckets** and click your bucket name.
  2. Go to the **Permissions** tab and click **Grant access**.
  3. In **Add principals** , enter the service account email you copied from the feed.
  4. Assign the **Storage Object Viewer** role (or **Storage Object Admin** if you selected a source deletion option).
  5. Click **Save**.



## Method 2: Amazon S3

This method uses Tenable Data Stream to continuously push your Tenable data to an Amazon S3 bucket in JSON format. Google SecOps then ingests the data from the bucket. Tenable Data Stream supports Amazon S3 only and authenticates to your AWS account using an IAM role that Tenable assumes (a cross-account trust relationship with an External ID).

### Create an Amazon S3 bucket

  1. Create an **Amazon S3 bucket** by following the AWS guide: [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html).
  2. Save the bucket **Name** and **Region** for later reference (for example, `tenable-vm-logs`).



### Create an IAM role for Tenable Data Stream

Tenable assumes this role to write data to your bucket. Tenable provides the exact trust policy and bucket policy in the console, including the Tenable AWS account and a generated External ID.

  1. In **Tenable Vulnerability Management** , go to **Settings > Tenable Data Stream** and click **Add an Integration**. Keep this dialog open to copy the trust policy and External ID in a later step.
  2. In the AWS console, go to **IAM > Roles > Create role**.
  3. Select **Custom trust policy** and paste the trust policy from the Tenable **IAM Role Guidelines** panel (click **Copy Trust Policy**). The trust policy has the following shape:
         
         {
             "Version": "2012-10-17",
             "Statement": [
                 {
                     "Effect": "Allow",
                     "Principal": { "AWS": "arn:aws:iam::<TENABLE_AWS_ACCOUNT_ID>:root" },
                     "Action": "sts:AssumeRole",
                     "Condition": { "StringEquals": { "sts:ExternalId": "<TENABLE_EXTERNAL_ID>" } }
                 }
             ]
         }
         

  4. Click **Next** , then create and attach a policy that grants Tenable write access to the bucket (replace `tenable-vm-logs` with your bucket name):
         
         {
             "Version": "2012-10-17",
             "Statement": [
                 {
                     "Effect": "Allow",
                     "Action": ["s3:PutObject", "s3:GetBucketLocation", "s3:ListBucket"],
                     "Resource": [
                         "arn:aws:s3:::tenable-vm-logs",
                         "arn:aws:s3:::tenable-vm-logs/*"
                     ]
                 }
             ]
         }
         

**Note:** If the bucket uses SSE-KMS encryption, also grant the role `kms:GenerateDataKey` on the KMS key.
  5. Enter a role name (for example, `TenableDataStreamRole`) and click **Create role**. Save the **Role Name** and your **AWS Account ID**.




### Configure Tenable Data Stream

  1. Return to the **Add an Integration** dialog in **Tenable Vulnerability Management** (**Settings > Tenable Data Stream**).
  2. Provide the following configuration details: 
     * **Integration Name** : Enter a descriptive name (for example, `Google SecOps Integration`).
     * **Integration Type** : Select **AWS S3** (the only available option).
     * **Integration Data** : Select the data types to stream (for example, **Assets** , **Vulnerabilities** , and **Host Audit**).
     * **Email Notification** (optional): Enter an email address to be notified if the stream state changes.
  3. Click **Next** and provide the IAM role details: 
     * **AWS Account ID** : Enter your AWS account ID.
     * **IAM Role Name** : Enter the role you created (for example, `TenableDataStreamRole`).
     * **External ID** : Use the External ID shown by Tenable in this dialog (the same value referenced in the trust policy).
  4. Click **Next** and provide the bucket details: 
     * **S3 Bucket Name** : Enter your bucket name (for example, `tenable-vm-logs`).
     * **Path Prefix** : Enter a prefix for organizing files (for example, `tenable/`).
  5. Click **Save**. Tenable continuously writes JSON data to your bucket.

**Note:** Don't delete the role, change its trust relationship, or remove the bucket permissions after setup, because these are the most common causes of a failed stream.



### Create an IAM user for Google SecOps to read the bucket

Google SecOps reads the bucket using a separate read-only IAM user (this identity is independent of the role Tenable uses to write).

  1. In the AWS console, go to **IAM > Users > Create user**.
  2. Enter a username (for example, `secops-tenable-reader`) and click **Next**.
  3. Click **Next** , then **Create user**.
  4. Select the user, go to the **Permissions** tab, and click **Add permissions > Create inline policy > JSON**. Paste the following read-only policy (replace `tenable-vm-logs` with your bucket name):
         
         {
             "Version": "2012-10-17",
             "Statement": [
                 {
                     "Effect": "Allow",
                     "Action": ["s3:GetObject", "s3:ListBucket", "s3:GetBucketLocation"],
                     "Resource": [
                         "arn:aws:s3:::tenable-vm-logs",
                         "arn:aws:s3:::tenable-vm-logs/*"
                     ]
                 }
             ]
         }
         

**Note:** If you select a source deletion option in the feed, also grant `s3:DeleteObject` on `arn:aws:s3:::tenable-vm-logs/*`.
  5. Go to the **Security credentials** tab and click **Create access key**.

  6. Select **Third-party service** as the use case, click **Next** , then **Create access key**.

  7. Copy and save the **Access key** and **Secret access key**.




### Configure a feed in Google SecOps to ingest from Amazon S3

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Tenable Vulnerability Management S3`).
  5. Select **Amazon S3 V2** as the **Source type**.
  6. Select **tenable.io** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters: 
     * **S3 URI** : Enter the bucket URI, including the prefix (for example, `s3://tenable-vm-logs/tenable/`).
     * **Source deletion option** : Select the deletion option according to your preference.
     * **Maximum File Age** : Include files modified in the last number of days. Default is 180 days.
     * **Access Key ID** : Enter the read-only IAM user access key.
     * **Secret Access Key** : Enter the read-only IAM user secret key.
  9. Click **Next** , review the configuration, and then click **Submit**.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`payload.path` | `about.file.full_path` | Directly mapped  
`payload.md5` | `about.file.md5` | Directly mapped  
`asset.uuid` | `entity.asset.asset_id` | Directly mapped  
`id` | `entity.asset.asset_id` | Directly mapped  
`payload_id` | `entity.asset.asset_id` | Directly mapped  
`ssh_fingerprints.0` | `entity.asset.attribute.labels.value` | Directly mapped  
`system_types.0` | `entity.asset.attribute.labels.value` | Directly mapped  
`asset.hostname` | `entity.asset.hostname` | Directly mapped  
`asset.last_scan_target` | `entity.asset.hostname` | Directly mapped  
`host` | `entity.asset.hostname` | Directly mapped  
`scan.target` | `entity.asset.hostname` | Directly mapped  
`asset.ipv4` | `entity.asset.ip` | Merged  
`ip` | `entity.asset.ip` | Merged  
`ipaddr` | `entity.asset.ip` | Merged  
`prinIP` | `entity.asset.ip` | Merged  
`scan_ipaddr` | `entity.asset.ip` | Merged  
`updateIndex` | `entity.asset.ip` | Mapped: `0` → `update_ipv4_0`  
`update_ipv4_0` | `entity.asset.ip` | Merged  
`asset.mac_address` | `entity.asset.mac` | Merged  
`mac` | `entity.asset.mac` | Merged  
`fqdns.0` | `entity.asset.network_domain` | Directly mapped  
`netbios_names.0` | `entity.asset.network_domain` | Directly mapped  
`os_family` | `entity.asset.platform_software.platform` | Directly mapped  
`asset.operating_system.0` | `entity.asset.platform_software.platform_version` | Directly mapped  
`asset.uuid` | `entity.asset.product_object_id` | Directly mapped  
`id` | `entity.asset.product_object_id` | Directly mapped  
`payload_id` | `entity.asset.product_object_id` | Directly mapped  
`vuln.vulnerabilities` | `entity.asset.vulnerabilities` | Merged  
`vuln1.vulnerabilities` | `entity.asset.vulnerabilities` | Merged  
`vuln2.vulnerabilities` | `entity.asset.vulnerabilities` | Merged  
`asset.device_type` | `metadata.description` | Directly mapped  
`plugin.description` | `metadata.description` | Directly mapped  
`has_entity_asset` | `metadata.entity_type` | Mapped: `true` → `ASSET`  
`first_found` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`last_found` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`scan.completed_at` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`scan.started_at` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`has_entity_asset` | `metadata.product_name` | Mapped: `true` → `Tenable IO`  
`has_entity_asset` | `metadata.vendor_name` | Mapped: `true` → `Tenable IO`  
`port.protocol` | `network.ip_protocol` | Directly mapped  
`asset.network_id` | `network.session_id` | Directly mapped  
`sec_res.description` | `security_result.description` | Directly mapped  
`asset_agent_uuid_label` | `security_result.detection_fields` | Merged  
`asset_bios_uuid_label` | `security_result.detection_fields` | Merged  
`asset_netbios_name_label` | `security_result.detection_fields` | Merged  
`finding_id_label` | `security_result.detection_fields` | Merged  
`plugin_family_id_label` | `security_result.detection_fields` | Merged  
`plugin_family_label` | `security_result.detection_fields` | Merged  
`plugin_risk_factor_label` | `security_result.detection_fields` | Merged  
`plugin_xrefs_label` | `security_result.detection_fields` | Merged  
`risk_factor_label` | `security_result.detection_fields` | Merged  
`scan_label` | `security_result.detection_fields` | Merged  
`scan_schedule_uuid_label` | `security_result.detection_fields` | Merged  
`scan_started_at_label` | `security_result.detection_fields` | Merged  
`scan_uuid_label` | `security_result.detection_fields` | Merged  
`see_also_label` | `security_result.detection_fields` | Merged  
`severity_default_id_label` | `security_result.detection_fields` | Merged  
`severity_id_label` | `security_result.detection_fields` | Merged  
`severity_label` | `security_result.detection_fields` | Merged  
`severity_modification_type_label` | `security_result.detection_fields` | Merged  
`update_finding_id_label` | `security_result.detection_fields` | Merged  
`update_first_scan_time_label` | `security_result.detection_fields` | Merged  
`update_last_licensed_scan_date_label` | `security_result.detection_fields` | Merged  
`update_last_scan_id_label` | `security_result.detection_fields` | Merged  
`update_last_scan_time_label` | `security_result.detection_fields` | Merged  
`update_last_schedule_id_label` | `security_result.detection_fields` | Merged  
`update_plugin_cvss3_vector_access_complexity_label` | `security_result.detection_fields` | Merged  
`update_plugin_cvss3_vector_access_vector_label` | `security_result.detection_fields` | Merged  
`update_plugin_cvss3_vector_authentication_label` | `security_result.detection_fields` | Merged  
`update_plugin_cvss3_vector_availability_impact_label` | `security_result.detection_fields` | Merged  
`update_plugin_cvss3_vector_confidentiality_impact_label` | `security_result.detection_fields` | Merged  
`update_plugin_cvss3_vector_integrity_impact_label` | `security_result.detection_fields` | Merged  
`update_plugin_cvss3_vector_privileges_required_label` | `security_result.detection_fields` | Merged  
`update_plugin_cvss3_vector_raw_label` | `security_result.detection_fields` | Merged  
`update_plugin_cvss3_vector_user_interaction_label` | `security_result.detection_fields` | Merged  
`update_plugin_cvss_base_score_label` | `security_result.detection_fields` | Merged  
`update_plugin_cvss_vector_access_complexity_label` | `security_result.detection_fields` | Merged  
`update_plugin_cvss_vector_access_vector_label` | `security_result.detection_fields` | Merged  
`update_plugin_cvss_vector_authentication_label` | `security_result.detection_fields` | Merged  
`update_plugin_cvss_vector_availability_impact_label` | `security_result.detection_fields` | Merged  
`update_plugin_cvss_vector_confidentiality_impact_label` | `security_result.detection_fields` | Merged  
`update_plugin_cvss_vector_integrity_impact_label` | `security_result.detection_fields` | Merged  
`update_plugin_cvss_vector_raw_label` | `security_result.detection_fields` | Merged  
`update_plugin_see_also_label` | `security_result.detection_fields` | Merged  
`update_plugin_stig_severity_label` | `security_result.detection_fields` | Merged  
`update_plugin_vpr_driver_cvss3_impact_score_label` | `security_result.detection_fields` | Merged  
`update_plugin_vpr_drivers_age_of_vuln_lower_bound_label` | `security_result.detection_fields` | Merged  
`update_plugin_vpr_drivers_age_of_vuln_upper_bound_label` | `security_result.detection_fields` | Merged  
`update_plugin_vpr_drivers_cvss_impact_score_predicted_label` | `security_result.detection_fields` | Merged  
`update_plugin_vpr_drivers_exploit_code_maturity_label` | `security_result.detection_fields` | Merged  
`update_plugin_vpr_drivers_product_coverage_label` | `security_result.detection_fields` | Merged  
`update_plugin_vpr_drivers_threat_intensity_last28_label` | `security_result.detection_fields` | Merged  
`update_plugin_vpr_drivers_threat_recency_lower_bound_label` | `security_result.detection_fields` | Merged  
`update_plugin_vpr_drivers_threat_recency_upper_bound_label` | `security_result.detection_fields` | Merged  
`update_plugin_vpr_score_label` | `security_result.detection_fields` | Merged  
`update_plugin_vpr_updated_label` | `security_result.detection_fields` | Merged  
`update_plugin_vpr_v2_cve_id_label` | `security_result.detection_fields` | Merged  
`update_plugin_vpr_v2_exploit_code_maturity_label` | `security_result.detection_fields` | Merged  
`update_plugin_vpr_v2_in_the_news_intensity_last30_label` | `security_result.detection_fields` | Merged  
`update_plugin_vpr_v2_in_the_news_recency_label` | `security_result.detection_fields` | Merged  
`update_plugin_vpr_v2_malware_observations_intensity_last30_label` | `security_result.detection_fields` | Merged  
`update_plugin_vpr_v2_malware_observations_recency_label` | `security_result.detection_fields` | Merged  
`update_plugin_vpr_v2_on_cisa_kev_label` | `security_result.detection_fields` | Merged  
`update_plugin_vuln_publication_date_label` | `security_result.detection_fields` | Merged  
`update_plugin_xrefs_id_type_label` | `security_result.detection_fields` | Merged  
`update_plugin_xrefs_type_label` | `security_result.detection_fields` | Merged  
`update_scan_started_at_label` | `security_result.detection_fields` | Merged  
`update_severity_default_id_label` | `security_result.detection_fields` | Merged  
`update_severity_id_label` | `security_result.detection_fields` | Merged  
`update_severity_modification_type_label` | `security_result.detection_fields` | Merged  
`updates_asset_netbios_name_label` | `security_result.detection_fields` | Merged  
`updates_plugin_vpr_v2_exploit_probability_label` | `security_result.detection_fields` | Merged  
`updates_plugin_vpr_v2_label` | `security_result.detection_fields` | Merged  
`updates_plugin_vpr_v2_percentile_label` | `security_result.detection_fields` | Merged  
`updates_plugin_vpr_v2_vpr_severity_label` | `security_result.detection_fields` | Merged  
`version_label` | `security_result.detection_fields` | Merged  
`xref_label` | `security_result.detection_fields` | Merged  
`severity` | `security_result.severity` | Directly mapped  
N/A | `entity.asset.attribute.labels.key` | Constant: `ssh_fingerprints`  
N/A | `metadata.entity_type` | Constant: `ASSET`  
N/A | `metadata.product_name` | Constant: `Tenable IO`  
N/A | `metadata.vendor_name` | Constant: `Tenable IO`  
N/A | `security_result.severity` | Constant: `CRITICAL`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/tenable-io-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
