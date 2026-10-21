---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gcp-vpc-flow/
title: Collect Google Cloud VPC Flow Logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T01:29:39.398273+00:00
---

# Collect Google Cloud VPC Flow Logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gcp-vpc-flow/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Google Cloud VPC Flow Logs

**Parser Version:** 6.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Google Cloud VPC Flow Logs to Google Security Operations using Google Cloud Storage.

VPC Flow Logs record a sample of network flows sent from and received by VM instances, including instances used as Google Kubernetes Engine nodes. These logs can be used for network monitoring, forensics, real-time security analysis, and expense optimization. Flow logs are aggregated by connection at configurable intervals and exported in near-real-time through Cloud Logging. A Logging sink routes the VPC Flow Logs to a Cloud Storage bucket, from which Google SecOps ingests them.

## Before you begin

Maker sure you have the following prerequisites:

  * A Google SecOps instance
  * A Google Cloud project with the following APIs enabled: 
    * Cloud Storage API
    * Cloud Logging API
    * Compute Engine API
  * Permissions to: 
    * Enable VPC Flow Logs on subnets
    * Create and manage Cloud Storage buckets
    * Manage IAM policies on Cloud Storage buckets
    * Create and manage Cloud Logging API sinks
  * At least one VPC subnet where you want to enable VPC Flow Logs



## Enable VPC Flow Logs on subnets

Before configuring the ingestion pipeline, make sure VPC Flow Logs are enabled on the target subnets. Google Cloud supports two APIs for managing VPC Flow Logs: the Network Management API (recommended) and the Compute Engine API.

### Using the Google Cloud console (Network Management API)

  1. In the [Google Cloud console](https://console.cloud.google.com/), go to **VPC network > VPC networks**.
  2. Click the **Subnets in current project** tab.
  3. Select the subnet where you want to enable flow logs.
  4. Click **Manage flow logs**.
  5. Click **Add new configuration**.
  6. Enter a configuration name.
  7. Configure the following optional settings: 
     * **Aggregation interval** : Select the aggregation interval (default: 5 seconds). Shorter intervals provide more granular data but increase log volume.
     * **Include metadata** : Select **Include all metadata** to include VM instance and VPC details.
     * **Secondary sampling rate** : Set the sampling rate (default: 100% for Network Management API). Higher rates capture more flows but increase log volume.
     * **Filter expression** : Optional CEL filter expression to include or exclude specific flows (maximum 2,048 characters).
  8. Click **Save**.



### Using the gcloud command-line tool (Network Management API)

  * Use the following syntax:
        
        gcloud network-management vpc-flow-logs-configs create <CONFIG_NAME> \
                --location=global \
                --subnet=projects/<PROJECT_ID>/regions/<REGION>/subnetworks/<SUBNET_NAME> \
                --aggregation-interval=INTERVAL_5_SEC \
                --metadata=INCLUDE_ALL_METADATA \
                --flow-sampling=1.0
        




Replace:

  * `<CONFIG_NAME>`: A descriptive configuration name (for example, `vpc-flow-logs-config`)
  * `<PROJECT_ID>`: Your Google Cloud project ID
  * `<REGION>`: The subnet region (for example, `us-central1`)
  * `<SUBNET_NAME>`: Your subnet name



### Using the gcloud command-line tool (Compute Engine API)

  * Use the following syntax:
        
        gcloud compute networks subnets update <SUBNET_NAME> \
                --region=<REGION> \
                --enable-flow-logs \
                --logging-aggregation-interval=interval-5-sec \
                --logging-metadata=include-all \
                --logging-flow-sampling=0.5 \
                --project=<PROJECT_ID>
        




Replace:

  * `<SUBNET_NAME>`: Your subnet name
  * `<REGION>`: The subnet region (for example, `us-central1`)
  * `<PROJECT_ID>`: Your Google Cloud project ID

**Note:** The Compute Engine API uses a default sampling rate of 50%, while the Network Management API defaults to 100%. Configurations created with the Compute Engine API cannot be managed with the Network Management API.



## Create a Google Cloud Storage bucket

  1. Go to the [Google Cloud console](https://console.cloud.google.com/).
  2. Select your project.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `vpc-flow-logs-bucket`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or a retention policy  
  6. Click **Create**.




## Create a Logging sink to export VPC Flow Logs to GCS

A Logging sink routes VPC Flow Logs from Logging to the Cloud Storage bucket. Google SecOps then ingests the exported objects from the bucket.

### Create the log sink

  1. In the [Google Cloud console](https://console.cloud.google.com/), go to **Logging > Log Router**.
  2. Click **Create sink**.
  3. Provide the following configuration details: 
     * **Sink name** : Enter a descriptive name (for example, `vpc-flow-to-gcs`).
     * **Sink description** : Enter `Route VPC Flow Logs to Cloud Storage for Google SecOps ingestion`.
  4. Click **Next**.
  5. In the **Select sink service** section: 
     * **Sink service** : Select **Cloud Storage bucket**.
     * **Select a Cloud Storage bucket** : Select the bucket `vpc-flow-logs-bucket`.
  6. Click **Next**.
  7. In the **Choose logs to include in sink** section, enter the following filter to capture VPC Flow Logs:
         
         resource.type="gce_subnetwork" AND log_id("compute.googleapis.com/vpc_flows")
         

**Note:** This filter captures VPC Flow Logs from all subnets in the project. To capture logs from a specific subnet, use the following filter:
         
         resource.type="gce_subnetwork" AND log_id("compute.googleapis.com/vpc_flows") AND resource.labels.subnetwork_name="<SUBNET_NAME>"
         

     * Replace `<SUBNET_NAME>` with the target subnet name.
  8. Click **Next**.

  9. Review the configuration and click **Create sink**.




### Grant the sink writer permission to write to the bucket

After creating the sink, Logging assigns the sink a writer service account (the writer identity). Grant this identity permission to write objects to the bucket.

  1. Go to **Logging > Log Router**.
  2. Locate the sink `vpc-flow-to-gcs`, click the three-dot menu, and select **View sink details**.
  3. Copy the **Writer identity** value (in the format `serviceAccount:p<PROJECT_NUMBER>-<ID>@gcp-sa-logging.iam.gserviceaccount.com`).
  4. Go to **Cloud Storage > Buckets**.
  5. Click the bucket `vpc-flow-logs-bucket`.
  6. Go to the **Permissions** tab.
  7. Click **Grant access**.
  8. Provide the following configuration details: 
     * **Add principals** : Paste the sink writer identity (without the `serviceAccount:` prefix).
     * **Assign roles** : Select **Storage Object Creator** (`roles/storage.objectCreator`).
  9. Click **Save**.



### Verify logs are being exported

  1. Go to **Cloud Storage > Buckets**.
  2. Click the bucket `vpc-flow-logs-bucket`.
  3. Wait a few minutes for the sink to write the first objects.
  4. Verify that a folder named `compute.googleapis.com/vpc_flows/` (or a dated path) is created and contains exported log files.

**Note:** Logging writes objects to the bucket in batches, so the first files can take several minutes to appear.



## Configure a feed in Google SecOps to ingest VPC Flow Logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `GCP VPC Flow Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **GCP VPC Flow** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address. You will use it in the next step.

**Note:** Each Google SecOps instance has a unique service account. Do not use service accounts from other documentation or examples.
  9. Click **Next**.

  10. Specify values for the following input parameters:

     * **Storage bucket URI** : Enter the GCS bucket URI with the prefix path:
           
           gs://vpc-flow-logs-bucket/compute.googleapis.com/vpc_flows/
           

       * Replace: 
         * `vpc-flow-logs-bucket`: Your GCS bucket name.
         * `compute.googleapis.com/vpc_flows`: Optional prefix/folder path where the sink writes logs (leave empty for root).
**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference:

       * **Never** : Never deletes any files after transfers (recommended for testing).
       * **Delete transferred files** : Deletes files after successful transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.
**Note:** If you select a deletion option, the service account must have **Storage Object Admin** role instead of Storage Object Viewer. Update IAM permissions accordingly.
     * **Maximum File Age (Days)** : Include files modified in the last number of days. Default is 180 days.

     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).

     * **Ingestion labels** : The label to be applied to the events from this feed.

  11. Click **Next**.

  12. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## Grant IAM permissions to the Google SecOps service account

The Google SecOps service account needs **Storage Object Viewer** role on your Cloud Storage bucket.

  1. Go to **Cloud Storage > Buckets**.
  2. Click the bucket `vpc-flow-logs-bucket`.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Paste the Google SecOps service account email.
     * **Assign roles** : Select **Storage Object Viewer** (`roles/storage.objectViewer`).
  6. Click **Save**.

**Note:** If you plan to use the deletion option "Delete transferred files" or "Delete transferred files and empty directories," grant **Storage Object Admin** role instead of Storage Object Viewer.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`_field` | `additional.fields` | Merged  
`textpayload_label` | `additional.fields` | Merged  
`tunnel_id_label` | `additional.fields` | Merged  
`description` | `metadata.description` | Directly mapped  
`timestamp` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`ts` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`event_type` | `metadata.event_type` | Directly mapped  
`product_event_type` | `metadata.product_event_type` | Directly mapped  
`product_log_id` | `metadata.product_log_id` | Directly mapped  
`product_name` | `metadata.product_name` | Directly mapped  
`product_version` | `metadata.product_version` | Directly mapped  
`vendor_name` | `metadata.vendor_name` | Directly mapped  
`ip_protocol_out` | `network.ip_protocol` | Directly mapped  
`jsonPayload.bytes_sent` | `network.sent_bytes` | Renamed/mapped  
`jsonPayload.packets_sent` | `network.sent_packets` | Renamed/mapped  
`principal.ip` | `principal.asset.ip` | Merged  
`target.ip` | `principal.asset.ip` | Merged  
`jsonPayload.src_instance.vm_name` | `principal.hostname` | Directly mapped  
`target.hostname` | `principal.hostname` | Renamed/mapped  
`jsonPayload.connection.src_ip` | `principal.ip` | Directly mapped  
`target.ip` | `principal.ip` | Merged  
`jsonPayload.src_location.city` | `principal.location.city` | Directly mapped  
`target.location.city` | `principal.location.city` | Renamed/mapped  
`jsonPayload.src_location.country` | `principal.location.country_or_region` | Directly mapped  
`target.location.country_or_region` | `principal.location.country_or_region` | Renamed/mapped  
`jsonPayload.src_instance.region` | `principal.location.name` | Directly mapped  
`resource.labels.location` | `principal.location.name` | Directly mapped  
`target.location.name` | `principal.location.name` | Renamed/mapped  
`jsonPayload.src_location.region` | `principal.location.state` | Directly mapped  
`target.location.state` | `principal.location.state` | Renamed/mapped  
`jsonPayload.src_vpc.project_id` | `principal.namespace` | Directly mapped  
`jsonPayload.src_vpc.vpc_name` | `principal.namespace` | Directly mapped  
`target.namespace` | `principal.namespace` | Renamed/mapped  
`jsonPayload.connection.src_port` | `principal.port` | Directly mapped  
`_field` | `principal.resource.attribute.labels` | Merged  
`key` | `principal.resource.attribute.labels` | Mapped: `jsonPayload_src_google_service_type` → `_field`  
`src_gke_cluster_location` | `principal.resource.attribute.labels` | Merged  
`src_gke_cluster_name` | `principal.resource.attribute.labels` | Merged  
`src_gke_namespace` | `principal.resource.attribute.labels` | Merged  
`src_gke_pod_name` | `principal.resource.attribute.labels` | Merged  
`logName` | `security_result.category_details` | Merged  
`severity` | `security_result.severity` | Mapped: `DEBUG` → `LOW`  
`principal.ip` | `target.asset.ip` | Merged  
`target.ip` | `target.asset.ip` | Merged  
`jsonPayload.dest_instance.vm_name` | `target.hostname` | Directly mapped  
`principal.hostname` | `target.hostname` | Renamed/mapped  
`jsonPayload.connection.dest_ip` | `target.ip` | Directly mapped  
`principal.ip` | `target.ip` | Merged  
`jsonPayload.dest_location.city` | `target.location.city` | Directly mapped  
`principal.location.city` | `target.location.city` | Renamed/mapped  
`jsonPayload.dest_location.country` | `target.location.country_or_region` | Directly mapped  
`principal.location.country_or_region` | `target.location.country_or_region` | Renamed/mapped  
`jsonPayload.dest_instance.region` | `target.location.name` | Directly mapped  
`principal.location.name` | `target.location.name` | Renamed/mapped  
`jsonPayload.dest_location.region` | `target.location.state` | Directly mapped  
`principal.location.state` | `target.location.state` | Renamed/mapped  
`jsonPayload.dest_vpc.project_id` | `target.namespace` | Directly mapped  
`jsonPayload.dest_vpc.vpc_name` | `target.namespace` | Directly mapped  
`principal.namespace` | `target.namespace` | Renamed/mapped  
`jsonPayload.connection.dest_port` | `target.port` | Renamed/mapped  
`dest_gke_cluster_location` | `target.resource.attribute.labels` | Merged  
`dest_gke_cluster_name` | `target.resource.attribute.labels` | Merged  
`dest_gke_namespace` | `target.resource.attribute.labels` | Merged  
`dest_gke_pod_name` | `target.resource.attribute.labels` | Merged  
`service_name_label` | `target.resource.attribute.labels` | Merged  
`service_namespace_label` | `target.resource.attribute.labels` | Merged  
`subnetwork_id_field` | `target.user.attribute.labels` | Merged  
N/A | `network.direction` | Constant: `OUTBOUND`  
N/A | `network.ip_protocol` | Constant: `network.ip_protocol`  
N/A | `network.sent_bytes` | Constant: `network.sent_bytes`  
N/A | `principal.hostname` | Constant: `target.hostname`  
N/A | `principal.location.city` | Constant: `target.location.city`  
N/A | `principal.location.country_or_region` | Constant: `target.location.country_or_region`  
N/A | `principal.location.name` | Constant: `target.location.name`  
N/A | `principal.location.state` | Constant: `target.location.state`  
N/A | `principal.namespace` | Constant: `target.namespace`  
N/A | `principal.port` | Constant: `principal.port`  
N/A | `security_result.severity` | Constant: `LOW`  
N/A | `target.hostname` | Constant: `principal.hostname`  
N/A | `target.location.city` | Constant: `principal.location.city`  
N/A | `target.location.country_or_region` | Constant: `principal.location.country_or_re...`  
N/A | `target.location.name` | Constant: `principal.location.name`  
N/A | `target.location.state` | Constant: `principal.location.state`  
N/A | `target.namespace` | Constant: `principal.namespace`  
N/A | `target.port` | Constant: `-99`  
`resource.labels.subnetwork_id` | `target.user.attribute.labels` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-vpc-flow-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
