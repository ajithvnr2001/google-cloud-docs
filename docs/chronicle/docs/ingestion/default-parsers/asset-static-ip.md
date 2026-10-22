---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/asset-static-ip/
title: Collect Static IP asset context data logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:51:38.637532+00:00
---

# Collect Static IP asset context data logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/asset-static-ip/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Static IP asset context data logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Static IP asset context data into Google Security Operations using Google Cloud Storage V2.

Static IP is an asset context data type that maps static IP addresses to hostnames and asset metadata. By ingesting this data, you enrich events in Google SecOps with additional context about network assets, enabling more accurate correlation, investigation, and alerting. Because this data is typically maintained in on-premise systems or exported as flat files, you must upload the files to a Google Cloud Storage (GCS) bucket, and then configure a Google SecOps feed to ingest them.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A Google Cloud project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Static IP asset data exported as a structured file (for example, CSV or JSON)
  * Access to the system or directory where the Static IP data files are stored



## Create a Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `asset-static-ip-data`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location closest to your Google SecOps instance (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed data)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.

**Note:** Record the bucket name. You will use it when configuring the Google SecOps feed.



## Configure an automated export of Static IP data to GCS

Static IP asset context data is typically maintained as flat files (CSV, JSON) on an internal system such as an IP address management (IPAM) platform, a CMDB, or a network inventory database. To keep the data in GCS current, configure an automated export pipeline using one of the following approaches.

### Option 1: Cloud Scheduler with Cloud Build (recommended)

Use Cloud Build triggered by Cloud Scheduler to run a containerized export job on a schedule. This approach requires no persistent VM and uses Google-managed infrastructure.

  1. Create a service account for the export job:

     1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
     2. Click **Create Service Account**.
     3. Provide the following configuration details: 
        * **Service account name** : Enter `static-ip-export-sa`
        * **Service account description** : Enter `Service account for automated Static IP data export to GCS`
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
                 apt-get update && apt-get install -y curl jq
                 # Export Static IP data from your source system
                 # Replace with the actual command for your environment
                 # Example: query IPAM API, export from CMDB, or generate from network scan
                 curl -s -H "Authorization: Bearer $${API_TOKEN}" \
                   "https://your-ipam-system.example.com/api/v1/static-ips" \
                   -o /workspace/static_ip_data.json
                 # Upload to GCS
                 gcloud storage cp /workspace/static_ip_data.json \
                   gs://${_BUCKET_NAME}/static-ip/static_ip_$(date -u +%Y%m%d_%H%M%S).json
         substitutions:
           _BUCKET_NAME: 'asset-static-ip-data'
         

**Note:** Replace the `curl` command with the actual export command for your source system (IPAM API, CMDB export, database query, or network scan tool).
  3. Create a Cloud Scheduler job to trigger the build:

     1. In the **GCP Console** , go to **Cloud Scheduler**.
     2. Click **Create Job**.
     3. Provide the following configuration details:

Setting | Value  
---|---  
**Name** | `static-ip-export-daily`  
**Region** | Select the same region as your GCS bucket  
**Frequency** | `0 2 * * *` (daily at 2:00 AM UTC)  
**Timezone** | UTC (recommended)  
**Target type** | HTTP  
**URL** | `https://cloudbuild.googleapis.com/v1/projects/YOUR_PROJECT_ID/builds`  
**HTTP method** | POST  
**Auth header** | Add OAuth token  
**Service account** | `static-ip-export-sa@YOUR_PROJECT_ID.iam.gserviceaccount.com`  
     4. Click **Create**.




### Option 2: Storage Transfer Service (for on-premise file systems)

If the Static IP data is stored on an on-premise file system, use Google Cloud Storage Transfer Service with a Transfer Agent.

  1. In the **GCP Console** , go to **Storage Transfer Service**.
  2. Click **Create transfer job**.
  3. Select **POSIX filesystem** as the source.
  4. Follow the instructions to install the [Storage Transfer Agent](https://docs.cloud.google.com/storage-transfer/docs/managing-on-prem-agents) on a machine with access to the Static IP data files.
  5. Configure the transfer job:

Setting | Value  
---|---  
**Source directory** | Path to the directory containing Static IP data files  
**Destination bucket** | `asset-static-ip-data`  
**Destination path** | `static-ip/`  
**Schedule** | Set a recurring schedule (for example, daily)  
  6. Click **Create**.




## Retrieve the Google SecOps service account

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Static IP Asset Data`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Static IP** as the **Log type**.
  7. Click **Get Service Account**.
  8. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  9. Copy the email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Do not use service accounts from other documentation or examples.



## Grant IAM permissions to the Google SecOps service account

The Google SecOps service account needs the **Storage Object Viewer** role on your GCS bucket.

  1. Go to **Cloud Storage > Buckets**.
  2. Click on your bucket name (for example, `asset-static-ip-data`).
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
  4. In the **Feed name** field, enter a name for the feed (for example, `Static IP Asset Data`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Static IP** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI:
           
           gs://asset-static-ip-data/static-ip/
           

       * Replace `asset-static-ip-data` with your GCS bucket name.
       * Replace `static-ip` with your configured prefix path.
**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never** : Never deletes any files after transfers (recommended for testing).
       * **Delete transferred files** : Deletes files after successful transfer.
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
`date` | `metadata.event_timestamp` | Parsed as `RFC 3339`  
`client_mac` | `network.dhcp.chaddr` | Directly mapped  
`client_hostname` | `network.dhcp.client_hostname` | Directly mapped  
`client_ip` | `network.dhcp.yiaddr` | Directly mapped  
`client_hostname` | `principal.hostname` | Directly mapped  
`client_ip` | `principal.ip` | Merged  
`client_mac` | `principal.mac` | Merged  
N/A | `metadata.event_type` | Constant: `NETWORK_DHCP`  
N/A | `metadata.product_name` | Constant: `PCAP DHCP`  
N/A | `network.application_protocol` | Constant: `DHCP`  
N/A | `network.dhcp.type` | Constant: `ACK`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/asset-static-ip-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
