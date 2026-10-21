---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/custom-dns/
title: Collect Custom DNS logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T12:43:40.908162+00:00
---

# Collect Custom DNS logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/custom-dns/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Custom DNS logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Custom DNS logs to Google Security Operations using Google Cloud Storage V2.

Custom DNS is a generic log type for DNS server logs from custom or unsupported DNS implementations. It captures DNS query and response data including domains, record types, and client information. Because these logs come from non-standard DNS sources, you must export them to a Google Cloud Storage (GCS) bucket, and then configure a Google SecOps feed to ingest them.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A Google Cloud project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * A DNS server or service generating logs in a supported format (JSON recommended)
  * Administrative access to the DNS server to configure log exports



## Create a Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `custom-dns-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location closest to your Google SecOps instance (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.

**Note:** Record the bucket name. You will use it when configuring the Google SecOps feed.



## Configure an automated export of DNS logs to GCS

The method for exporting DNS logs depends on your DNS server implementation. Choose the approach that best matches your environment.

### Option 1: Cloud Logging sink (for DNS servers on GCE)

If your DNS server runs on a Google Compute Engine instance and logs to Cloud Logging, create a log sink to export DNS logs directly to GCS.

  1. In the **GCP Console** , go to **Logging > Log Router**.
  2. Click **Create Sink**.
  3. Provide the following configuration details:

Setting | Value  
---|---  
**Sink name** | `custom-dns-to-gcs`  
**Sink destination** | Cloud Storage bucket  
**Bucket** | `custom-dns-logs`  
**Inclusion filter** | A filter matching your DNS log entries (for example, `resource.type="gce_instance" AND logName="projects/YOUR_PROJECT_ID/logs/dns"`)  
  4. Click **Create Sink**.

**Note:** The log sink automatically writes matching log entries to the GCS bucket as JSON files. No additional scheduling is needed.



### Option 2: Cloud Scheduler with Cloud Build (for on-premises DNS servers)

Use Cloud Build triggered by Cloud Scheduler to run a containerized export job that collects DNS logs from a remote server and writes them to GCS.

  1. Create a service account for the export job:

     1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
     2. Click **Create Service Account**.
     3. Provide the following configuration details: 
        * **Service account name** : Enter `dns-log-export-sa`
        * **Service account description** : Enter `Service account for automated DNS log export to GCS`
     4. Click **Create and Continue**.
     5. Add the following roles: 
        * **Storage Object Admin** (to write files to GCS)
        * **Cloud Build Editor** (to run Cloud Build jobs)
     6. Click **Done**.
  2. Create a Cloud Build configuration file (`cloudbuild.yaml`):
         
         steps:
           - name: 'gcr.io/cloud-builders/gcloud'
             entrypoint: 'bash'
             args:
               - '-c'
               - |
                 # Collect DNS logs from your server
                 # Replace with the actual command for your environment
                 # Example: pull logs via syslog-ng, rsync from remote server, or query DNS log API
                 curl -s -H "Authorization: Bearer $${API_TOKEN}" \
                   "https://your-dns-server.example.com/api/logs?format=json" \
                   -o /workspace/dns_logs.json
                 # Upload to GCS
                 gcloud storage cp /workspace/dns_logs.json \
                   gs://${_BUCKET_NAME}/dns/dns_logs_$(date -u +%Y%m%d_%H%M%S).json
         substitutions:
           _BUCKET_NAME: 'custom-dns-logs'
         

**Note:** Replace the `curl` command with the actual command for your DNS server. For example, use `scp` to copy log files from a remote server, or use an API call to query a DNS management platform.
  3. Create a Cloud Scheduler job to trigger the build:

     1. In the **GCP Console** , go to **Cloud Scheduler**.
     2. Click **Create Job**.
     3. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | `dns-log-export-hourly`  
**Region** | Select the same region as your GCS bucket  
**Frequency** | `0 * * * *` (every hour)  
**Timezone** | UTC (recommended)  
**Target type** | HTTP  
**URL** | `https://cloudbuild.googleapis.com/v1/projects/YOUR_PROJECT_ID/builds`  
**HTTP method** | POST  
**Auth header** | Add OAuth token  
**Service account** | `dns-log-export-sa@YOUR_PROJECT_ID.iam.gserviceaccount.com`  
     4. Click **Create**.




### Option 3: Storage Transfer Service (for on-premises file systems)

If DNS logs are written to a local file system, use Storage Transfer Service with a Transfer Agent to move them to GCS.

  1. In the **GCP Console** , go to **Storage Transfer Service**.
  2. Click **Create transfer job**.
  3. Select **POSIX filesystem** as the source.
  4. Follow the instructions to install the [Storage Transfer Agent](https://docs.cloud.google.com/storage-transfer/docs/managing-on-prem-agents) on the DNS server or a machine with access to the DNS log files.
  5. Configure the transfer job:

Setting | Value  
---|---  
**Source directory** | Path to the DNS log file directory  
**Destination bucket** | `custom-dns-logs`  
**Destination path** | `dns/`  
**Schedule** | Set a recurring schedule (for example, every hour)  
  6. Click **Create**.




## Retrieve the Google SecOps service account

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Custom DNS Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Custom DNS** as the **Log type**.
  7. Click **Get Service Account**.
  8. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  9. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Do not use service accounts from other documentation or examples.



## Grant IAM permissions to the Google SecOps service account

The Google SecOps service account needs **Storage Object Viewer** role on your GCS bucket.

  1. Go to **Cloud Storage > Buckets**.
  2. Click on your bucket name (for example, `custom-dns-logs`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Paste the Google SecOps service account email (for example, `chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com`).
     * **Assign roles** : Select **Storage Object Viewer**.
  6. Click **Save**.

**Note:** If you plan to use the deletion option "Delete transferred files" or "Delete transferred files and empty directories," grant **Storage Object Admin** role instead of Storage Object Viewer.



## Configure the Google SecOps feed

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Custom DNS Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Custom DNS** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **Storage bucket URI** : Enter the GCS bucket URI:
           
           gs://custom-dns-logs/dns/
           

       * Replace `custom-dns-logs` with your GCS bucket name.
       * Replace `dns` with your configured prefix path.
**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never** : Never deletes any files after transfers (recommended for testing).
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.

**Note:** If you select a deletion option, the Google SecOps service account must have **Storage Object Admin** role instead of Storage Object Viewer. Update IAM permissions accordingly.
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days).

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).

     * **Ingestion labels** : The label to be applied to the events from this feed.

  9. Click **Next**.

  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`receiveTimestamp` | `metadata.event_timestamp` | Parsed as `RFC 3339`  
`message` | `metadata.event_type` | Mapped: `"dns_query"` → `NETWORK_DNS`  
`jsonPayload.msg` | `metadata.product_event_type` | Directly mapped  
`insertId` | `metadata.product_log_id` | Directly mapped  
`message` | `metadata.product_name` | Mapped: `"dns_query"` → `Custom DNS`  
`message` | `metadata.vendor_name` | Mapped: `"dns_query"` → `CUSTOM`  
`message` | `network.application_protocol` | Mapped: `"dns_query"` → `DNS`  
`dns_answers` | `network.dns.answers` | Merged  
`message` | `network.dns.answers` | Mapped: `"dns_query"` → `dns_answers`  
`dns_question` | `network.dns.questions` | Merged  
`message` | `network.dns.questions` | Mapped: `"dns_query"` → `dns_question`  
`dns.response_code` | `network.dns.response_code` | Renamed/mapped  
`message` | `principal.hostname` | Mapped: `"dns_query"` → `jsonPayload.dns_query.server`  
`jsonPayload.dns_query.server` | `principal.ip` | Merged  
`message` | `principal.ip` | Mapped: `"dns_query"` → `jsonPayload.dns_query.server`  
`message` | `security_result` | Mapped: `"dns_query"` → `security_result`  
`logName` | `security_result.category_details` | Merged  
`message` | `security_result.category_details` | Mapped: `"dns_query"` → `logName`  
`message` | `security_result.severity` | Mapped: `"dns_query"` → `INFORMATIONAL`, `"dns_query"` → `MEDIUM`, `"dns_query"` → `HIGH`  
`labels.application` | `target.application` | Directly mapped  
`message` | `target.hostname` | Mapped: `"dns_query"` → `jsonPayload.dns_query.server`  
`jsonPayload.dns_query.server` | `target.ip` | Merged  
`message` | `target.ip` | Mapped: `"dns_query"` → `jsonPayload.dns_query.server`  
`component_label` | `target.labels` | Merged  
`instance_group_label` | `target.labels` | Merged  
`message` | `target.labels` | Mapped: `"dns_query"` → `component_label`, `"dns_query"` → `instance_group_label`  
`labels.region` | `target.location.country_or_region` | Directly mapped  
`resource.labels.zone` | `target.resource.attribute.cloud.availability_zone` | Directly mapped  
`message` | `target.resource.attribute.cloud.environment` | Mapped: `"dns_query"` → `GOOGLE_CLOUD_PLATFORM`  
`resource.labels.project_id` | `target.resource.attribute.cloud.project.id` | Directly mapped  
`message` | `target.resource.resource_type` | Mapped: `"dns_query"` → `VIRTUAL_MACHINE`  
N/A | `metadata.event_type` | Constant: `NETWORK_DNS`  
N/A | `metadata.product_name` | Constant: `Custom DNS`  
N/A | `metadata.vendor_name` | Constant: `CUSTOM`  
N/A | `network.application_protocol` | Constant: `DNS`  
N/A | `principal.hostname` | Constant: `jsonPayload.dns_query.server`  
N/A | `security_result.severity` | Constant: `INFORMATIONAL`  
N/A | `target.hostname` | Constant: `jsonPayload.dns_query.server`  
N/A | `target.resource.attribute.cloud.environment` | Constant: `GOOGLE_CLOUD_PLATFORM`  
N/A | `target.resource.resource_type` | Constant: `VIRTUAL_MACHINE`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/custom-dns-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
