---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/forseti/
title: Collect Forseti Open Source logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T08:55:34.222797+00:00
---

# Collect Forseti Open Source logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/forseti/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Forseti Open Source logs

**Parser Version:** 2.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Forseti Open Source logs to Google Security Operations using Google Cloud Storage V2.

Forseti Security is a community-driven collection of open-source tools designed to improve the security of Google Cloud Platform environments. Forseti take inventory snapshots of GCP resources, scans for access control compliance, and provides visibility into Cloud IAM policies.

**Important:** The Forseti Security project was archived on **January 11, 2025** , and is now read-only. This integration guide is intended for existing Forseti deployments. Organizations should evaluate whether to continue using Forseti or migrate to alternative security monitoring solutions.

## Before you begin

Make sure that you have the following prerequisites:

  * A Google SecOps instance.
  * A GCP project with the Cloud Storage API enabled.
  * Permissions to create and manage GCS buckets and IAM policies.
  * An existing Forseti Security deployment.
  * Access to the Forseti server configuration file (`forseti_conf_server.yaml`).



## Create Google Cloud Storage bucket

### Using Google Cloud Console

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage** > **Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (e.g., `forseti-violations-export`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (e.g., `us-central1`)  
**Storage class** | **Standard** (recommended for frequently accessed logs)  
**Access control** | **Uniform** (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




### Using gcloud command-line tool

  * Alternatively, create a bucket using the `gcloud` command:
        
        gcloud storage buckets create gs://forseti-violations-export \
            --location=us-central1 \
            --default-storage-class=STANDARD
        

  * Replace `forseti-violations-export` with your required globally unique bucket name.

  * Replace `us-central1` with your preferred region.




## Configure Forseti Security to export violations to GCS

Forseti Security uses a **notifier configuration** in the `forseti_conf_server.yaml` file to export scanner violations to GCS.

  1. Connect to your Forseti server VM using **SSH** : `bash gcloud compute ssh forseti-server-vm --project=YOUR_PROJECT_ID --zone=YOUR_ZONE`
  2. Open the configuration file for editing: `bash sudo nano /home/ubuntu/forseti-security/configs/forseti_conf_server.yaml` _If using GCS-based configuration, download it first:_ `bash gsutil cp gs://YOUR_FORSETI_SERVER_BUCKET/configs/forseti_conf_server.yaml ~/forseti_conf_server.yaml`
  3. Navigate to the `notifier` section and locate the `resources` subsection.
  4. For each violation resource type you want to export, configure the `gcs_violations` notifier:
         
         notifier:
             resources:
                 - resource: iam_policy_violations
                     should_notify: true
                     notifiers:
                         - name: gcs_violations
                             configuration:
                                 data_format: csv
                                 gcs_path: gs://forseti-violations-export/violations/
                 - resource: firewall_rule_violations
                     should_notify: true
                     notifiers:
                         - name: gcs_violations
                             configuration:
                                 data_format: csv
                                 gcs_path: gs://forseti-violations-export/violations/
                 - resource: cloudsql_acl_violations
                     should_notify: true
                     notifiers:
                         - name: gcs_violations
                             configuration:
                                 data_format: csv
                                 gcs_path: gs://forseti-violations-export/violations/
                 - resource: bucket_acl_violations
                     should_notify: true
                     notifiers:
                         - name: gcs_violations
                             configuration:
                                 data_format: csv
                                 gcs_path: gs://forseti-violations-export/violations/
                 - resource: config_validator_violations
                     should_notify: true
                     notifiers:
                         - name: gcs_violations
                             configuration:
                                 data_format: csv
                                 gcs_path: gs://forseti-violations-export/violations/
         

**Key Parameters:**

     * `resource`: The violation type (e.g., `iam_policy_violations`).
     * `data_format`: Set to `csv` or `json`.
     * `gcs_path`: The Cloud Storage path (must include a trailing slash).
  5. Save the file and, if necessary, upload it back to GCS.

  6. Reload the configuration: `bash forseti server configuration reload`

  7. Verify: `bash forseti server configuration get | grep gcs_violations`




## Retrieve the Google SecOps service account

### Configure a feed in Google SecOps

  1. Go to **SIEM Settings** > **Feeds**.
  2. Click **Add New Feed** and select **Configure a single feed**.
  3. **Feed name** : Enter a name (e.g., `Forseti Violations`).
  4. **Source type** : Select **Google Cloud Storage V2**.
  5. **Log type** : Select **Forseti Open Source**.
  6. Click **Get Service Account**.
  7. Copy the unique service account email (e.g., `chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com`).
  8. Click **Next**.
  9. Specify input parameters: 
     * **Storage bucket URL** : `gs://forseti-violations-export/violations/`
     * **Source deletion option** : Select according to your preference (e.g., **Never** for testing).
  10. Click **Next** , review the configuration, and click **Submit**.



## Grant IAM permissions to the Google SecOps service account

### Using Google Cloud Console

  1. Go to **Cloud Storage** > **Buckets**.
  2. Click your bucket name and go to the **Permissions** tab.
  3. Click **Grant access**.
  4. **Add principals** : Paste the Google SecOps service account email.
  5. **Assign roles** : Select **Storage Object Viewer**. (Use **Storage Object Admin** if you selected a deletion option in the feed).
  6. Click **Save**.


  * Using gcloud command-line tool
        
        gcloud storage buckets add-iam-policy-binding gs://forseti-violations-export \
            --member="serviceAccount:CHRONICLE_SERVICE_ACCOUNT_EMAIL" \
            --role="roles/storage.objectViewer"
        




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`data.resource_data.instanceGroupUrls` | `about` | Merged from array of instanceGroupUrls.  
`data.resource_data.nodePools.*.statusMessage` | `metadata.description` | Value from nodePool.statusMessage.  
`data.resource_type` | `metadata.event_type` | Specific types for KMS/FW; else **GENERIC_EVENT**.  
`data.scanner_index_id` | `metadata.product_log_id` | Value copied directly as string.  
N/A | `metadata.product_name` | Set to **FORSETI SECURITY**.  
N/A | `metadata.vendor_name` | Set to **FORSETI**.  
`data.resource_data.direction` | `network.direction` | Set to **INBOUND** if direction is INGRESS.  
`data.resource_data.endpoint` | `principal.ip` | Value copied directly.  
`data.full_name`, `serviceAccount` | `principal.user.userid` | Extracted from `full_name` or `serviceAccount`.  
`data.violation_type` | `security_result.category` | Mapped to **POLICY_VIOLATION** or **ACL_VIOLATION**.  
`data.rule_name` | `security_result.rule_name` | Value copied directly.  
`data.full_name` | `target.asset.attribute.cloud.project.id` | Extracted from `full_name` using grok.  
`data.resource_type` | `target.resource.resource_type` | Mapped to specific type based on `resource_type`.  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
