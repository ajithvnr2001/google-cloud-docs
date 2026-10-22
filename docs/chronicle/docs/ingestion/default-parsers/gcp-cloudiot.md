---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gcp-cloudiot/
title: Collect Google Cloud IoT logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:34:04.819499+00:00
---

# Collect Google Cloud IoT logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gcp-cloudiot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Google Cloud IoT logs

**Parser Version:** 5.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to export Google Cloud IoT logs to Google Security Operations using Cloud Storage. The parser extracts fields from JSON-formatted logs and then maps those fields to the corresponding fields in the Google SecOps UDM schema, ultimately transforming raw log data into a structured format suitable for security analysis.

## Before You Begin

Ensure that you have the following prerequisites:

  * Google SecOps instance
  * IoT is set up and active in your Google Cloud environment
  * Privileged access to Google Cloud



## Create a Google Cloud Storage Bucket

  1. Sign in to the [Google Cloud console](https://console.cloud.google.com/).
  2. Go to the **Cloud Storage Buckets** page.

[Go to Buckets](https://console.cloud.google.com/storage/browser)

  3. Click **Create**.

  4. On the **Create a bucket** page, enter your bucket information. After each of the following steps, click **Continue** to proceed to the next step:

     1. In the **Get started** section, do the following:

        1. Enter a unique name that meets the bucket name requirements; for example, **cloudiot-logs**.
        2. To enable hierarchical namespace, click the expander arrow to expand the **Optimize for file oriented and data-intensive workloads** section, and then select **Enable Hierarchical namespace on this bucket**.

**Note:** You cannot enable hierarchical namespace in an existing bucket.
        3. To add a bucket label, click the expander arrow to expand the **Labels** section.

        4. Click **Add label** , and specify a key and a value for your label.

     2. In the **Choose where to store your data** section, do the following:

        1. Select a **Location type**.
        2. Use the location type menu to select a **Location** where object data within your bucket will be permanently stored.

**Note:** If you select the **dual-region** location type, you can also choose to enable **turbo replication** by using the relevant checkbox.
        3. To set up cross-bucket replication, expand the **Set up cross-bucket replication** section.

     3. In the **Choose a storage class for your data** section, either select a **default storage class** for the bucket, or select **Autoclass** for automatic storage class management of your bucket's data.

     4. In the **Choose how to control access to objects** section, select **not** to enforce **public access prevention** , and select an **access control model** for your bucket's objects.

**Note:** If public access prevention is already enforced by your project's organization policy, the **Prevent public access** checkbox is locked.
     5. In the **Choose how to protect object data** section, do the following:

        1. Select any of the options under **Data protection** that you want to set for your bucket.
        2. To choose how your object data will be encrypted, click the expander arrow labeled **Data encryption** , and select a **Data encryption method**.
  5. Click **Create**.


**Note:** Be sure to provide your Google SecOps Service Account with permissions to **Read** or **Read & Write** to the newly created bucket.

## Configure Log Export in Google Cloud IoT

  1. Sign in to **Google Cloud** account using your privileged account.
  2. Search and select **Logging** in the search bar.
  3. In **Log Explorer** , filter the logs by choosing **Cloud IoT Core** and click **Apply**.
  4. Click **More Actions**.
  5. Click **Create Sink**.
  6. Provide the following configurations: 
     1. **Sink Details** : enter a name and description.
     2. Click **Next**.
     3. **Sink Destination** : select **Cloud Storage Bucket**.
     4. **Cloud Storage Bucket** : select the bucket created earlier or create a new bucket.
     5. Click **Next**.
     6. **Choose Logs to include in Sink** : a default log is populated when you select an option in Cloud Storage Bucket.
     7. Click **Next**.
     8. Optional: **Choose Logs to filter out of Sink** : select the logs that you would like not to sink.
  7. Click **Create Sink**.

  8. In the **GCP console** , go to **Logging > Log Router**.

  9. Click **Create Sink**.




## Set up feeds

To configure a feed, follow these steps:

  1. Go to **SIEM Settings** > **Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed; for example, **GCP Cloud IoT Logs**.
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **GCP Cloud IoT** as the **Log type**.
  7. Click **Get Service Account** as the **Chronicle Service Account**.
  8. Click **Next**.
  9. Specify values for the following input parameters:

     * **Storage Bucket URI** : Google Cloud storage bucket URL in **`gs://my-bucket/<value>/`** format.
     * **Source deletion options** : select deletion option according to your preference.

**Note:** If you select the `Delete transferred files` or `Delete transferred files and empty directories` option, make sure that you granted appropriate permissions to the service account.
     * **Maximum File Age** : Includes files modified in the last number of days. Default is 180 days

  10. Click **Next**.

  11. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## UDM Mapping Table

Log Field | UDM Mapping | Logic  
---|---|---  
insertId | metadata.product_log_id | Directly mapped from `insertId` field.  
jsonPayload.eventType | metadata.product_event_type | Directly mapped from `jsonPayload.eventType` field.  
jsonPayload.protocol | network.application_protocol | Directly mapped from `jsonPayload.protocol` field.  
jsonPayload.serviceName | target.application | Directly mapped from `jsonPayload.serviceName` field.  
jsonPayload.status.description | metadata.description | Directly mapped from `jsonPayload.status.description` field.  
jsonPayload.status.message | security_result.description | Directly mapped from `jsonPayload.status.message` field.  
labels.device_id | principal.asset_id | Value is set to `Device ID:` concatenated with the value of `labels.device_id` field.  
receiveTimestamp | metadata.event_timestamp | Parsed from the `receiveTimestamp` field and used to populate both `events.timestamp` and `metadata.event_timestamp`.  
resource.labels.device_num_id | target.resource.product_object_id | Directly mapped from `resource.labels.device_num_id` field.  
resource.labels.location | target.location.name | Directly mapped from `resource.labels.location` field.  
resource.labels.project_id | target.resource.name | Directly mapped from `resource.labels.project_id` field.  
resource.type | target.resource.resource_subtype | Directly mapped from `resource.type` field.  
severity | security_result.severity | Mapped from the `severity` field based on the following logic:  
\- If `severity` is `DEFAULT`, `DEBUG`, `INFO`, or `NOTICE`, then `security_result.severity` is set to `INFORMATIONAL`.  
\- If `severity` is `WARNING` or `ERROR`, then `security_result.severity` is set to `MEDIUM`.  
\- If `severity` is `CRITICAL`, `ALERT`, or `EMERGENCY`, then `security_result.severity` is set to `HIGH`.  
N/A | metadata.log_type | Hardcoded to `GCP_CLOUDIOT`.  
N/A | metadata.vendor_name | Hardcoded to `Google Cloud Platform`.  
N/A | metadata.event_type | Hardcoded to `GENERIC_EVENT`.  
N/A | metadata.product_name | Hardcoded to `GCP_CLOUDIOT`.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-cloudiot-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
