---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/redcanary-edr/
title: Collect Red Canary EDR logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:36:29.447847+00:00
---

# Collect Red Canary EDR logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/redcanary-edr/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Red Canary EDR logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Red Canary EDR logs to Google Security Operations using Google Cloud Storage V2.

Red Canary is a managed detection and response (MDR) platform that provides endpoint threat detection and investigation. Because Red Canary exports telemetry and detection data as files, you must upload those logs to a Google Cloud Storage (GCS) bucket, and then configure a Google SecOps feed to ingest them.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A Google Cloud project with billing enabled
  * Privileged access to the Red Canary console with permissions to configure data export
  * Access to Red Canary EDR log files



## Create a Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `redcanary-edr-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location closest to your Google SecOps instance (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.

**Note:** Record the bucket name. You will use it when configuring the Google SecOps feed.



## Export Red Canary EDR logs to GCS

Red Canary provides a **Canary Exporter** tool (Docker container) for bulk data export, plus webhook automation for pushing data to external destinations.

### Option A: Use Canary Exporter

  1. Deploy the [Canary Exporter](https://docs.redcanary.com/docs/export-data-from-red-canary) Docker container on a host with network access to GCS.
  2. Configure the exporter with your Red Canary API credentials.
  3. Set the export destination to a local directory or AWS S3.
  4. Upload exported files from the local directory to GCS using a Cloud Run function or the Google Cloud Console.



### Option B: Configure webhook automation

  1. In the Red Canary portal, go to **Integrations > Automation**.
  2. Create a webhook that sends detection data to a Cloud Run function endpoint, which writes the data to GCS.



## Retrieve the Google SecOps service account

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Red Canary EDR Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Red Canary** as the **Log type**.
  7. Click **Get Service Account**.
  8. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  9. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Do not use service accounts from other documentation or examples.



## Grant IAM permissions to the Google SecOps service account

The Google SecOps service account needs **Storage Object Viewer** role on your GCS bucket.

  1. Go to **Cloud Storage > Buckets**.
  2. Click on your bucket name (for example, `redcanary-edr-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Paste the Google SecOps service account email (for example, `chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com`).
     * **Assign roles** : Select **Storage Object Viewer**.
  6. Click **Save**.

**Note:** If you plan to use the deletion option "Delete transferred files and empty directories," grant **Storage Object Admin** role instead of Storage Object Viewer.



## Configure the Google SecOps feed

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Red Canary EDR Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Red Canary** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI:
           
           gs://redcanary-edr-logs/redcanary-logs/
           

       * Replace `redcanary-edr-logs` with your GCS bucket name
       * Replace `redcanary-logs` with your configured prefix path
**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never delete files** : Never deletes any files after transfers (recommended for testing).
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.

**Note:** If you select a deletion option, the Google SecOps service account must have **Storage Object Admin** role instead of Storage Object Viewer. Update IAM permissions accordingly.
     * **Maximum File Age (Days)** : Include files modified in the last number of days (default is 180 days).

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).

     * **Ingestion labels** : The label to be applied to the events from this feed.

  9. Click **Next**.

  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`endpoint_status_label` | `about.labels` | Merged  
`endpoint_type_label` | `about.labels` | Merged  
`event_type_cd` | `about.labels` | Mapped values (9 total, e.g. `endpoint_metadata` → `endpoint_status_label`, `endpoint_metada...  
`is_telemetry_collection_enabled_label` | `about.labels` | Merged  
`monitoring_status_label` | `about.labels` | Merged  
`physical_memory_bytes_label` | `about.labels` | Merged  
`process_standard_error_label` | `about.labels` | Merged  
`process_standard_input_label` | `about.labels` | Merged  
`process_standard_output_label` | `about.labels` | Merged  
`remote_location_cd_label` | `about.labels` | Merged  
`activity_at_ts` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`registration_time` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`event_type_cd` | `metadata.event_type` | Mapped: `endpoint_metadata` → `STATUS_HEARTBEAT`, `network_connection` → `NETWORK_CONNECTION...  
`event_type_cd` | `metadata.product_event_type` | Renamed/mapped  
`sensor_product_ver` | `metadata.product_version` | Renamed/mapped  
`direction_cd` | `network.direction` | Renamed/mapped  
`protocol_cd` | `network.ip_protocol` | Renamed/mapped  
`sensor_product_cd` | `observer.application` | Renamed/mapped  
`sensor_id` | `observer.asset_id` | Directly mapped  
`user_domain` | `principal.administrative_domain` | Renamed/mapped  
`domain` | `principal.hostname` | Renamed/mapped  
`host_name` | `principal.hostname` | Renamed/mapped  
`hostname` | `principal.hostname` | Renamed/mapped  
`event_type_cd` | `principal.ip` | Mapped: `endpoint_metadata` → `ips`, `network_connection` → `local_ip`  
`ips` | `principal.ip` | Merged  
`local_ip` | `principal.ip` | Merged  
`mac_addresses` | `principal.mac` | Renamed/mapped  
`endpoint_platform` | `principal.platform` | Renamed/mapped  
`endpoint_operating_system` | `principal.platform_version` | Renamed/mapped  
`local_port` | `principal.port` | Renamed/mapped  
`user_name` | `principal.user.user_display_name` | Renamed/mapped  
`user_uid` | `principal.user.userid` | Renamed/mapped  
`process_name` | `target.application` | Renamed/mapped  
`event_type_cd` | `target.ip` | Mapped: `network_connection` → `remote_ip`  
`remote_ip` | `target.ip` | Merged  
`remote_port` | `target.port` | Renamed/mapped  
`process_command_line` | `target.process.command_line` | Renamed/mapped  
`process_path` | `target.process.file.full_path` | Renamed/mapped  
`process_md5` | `target.process.file.md5` | Renamed/mapped  
`process_sha1` | `target.process.file.sha1` | Renamed/mapped  
`process_sha256` | `target.process.file.sha256` | Renamed/mapped  
`parent_process_command_line` | `target.process.parent_process.command_line` | Renamed/mapped  
`parent_process_path` | `target.process.parent_process.file.full_path` | Renamed/mapped  
`parent_process_md5` | `target.process.parent_process.file.md5` | Renamed/mapped  
`parent_process_sha1` | `target.process.parent_process.file.sha1` | Renamed/mapped  
`parent_process_sha256` | `target.process.parent_process.file.sha256` | Renamed/mapped  
`parent_process_pid` | `target.process.parent_process.pid` | Renamed/mapped  
`parent_process_native_id` | `target.process.parent_process.product_specific_process_id` | Directly mapped  
`process_pid` | `target.process.pid` | Renamed/mapped  
`process_native_id` | `target.process.product_specific_process_id` | Directly mapped  
N/A | `metadata.event_type` | Constant: `STATUS_HEARTBEAT`  
N/A | `metadata.product_name` | Constant: `EDR`  
N/A | `metadata.vendor_name` | Constant: `REDCANARY`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/redcanary-edr-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
