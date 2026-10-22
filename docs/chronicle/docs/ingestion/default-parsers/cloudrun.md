---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloudrun/
title: Collect Cloud Run logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:38:29.101215+00:00
---

# Collect Cloud Run logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloudrun/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Cloud Run logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide explains how to export Cloud Run logs to Google Security Operations using Cloud Storage. The parser extracts fields from JSON logs, transforming them into the Unified Data Model (UDM). It handles various log formats, including HTTP request data and system audit logs, mapping relevant fields to UDM while also enriching the data with labels and metadata specific to Cloud Run.

## Before You Begin

Ensure that you have the following prerequisites:

  * Google SecOps instance.
  * Cloud Run is set up and active in your Google Cloud environment.
  * Privileged access to Google Cloud.



## Create a Google Cloud Storage Bucket

  1. Sign in to the [Google Cloud console](https://console.cloud.google.com/).
  2. Go to the **Cloud Storage Buckets** page.

[Go to Buckets](https://console.cloud.google.com/storage/browser)

  3. Click **Create**.

  4. On the **Create a bucket** page, enter your bucket information. After each of the following steps, click **Continue** to proceed to the next step:

     1. In the **Get started** section, do the following:

        1. Enter a unique name that meets the bucket name requirements; for example, **cloudrun-logs**.
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

## Configure Log Export in Cloud Run

  1. On the Google Cloud **Welcome** page, click the **Cloud Run** icon.
  2. Search **Logging** in the search bar at the top and click **Enter**.
  3. In **Log Explorer** , filter the logs by choosing **Cloud Run** in **Log Name** and click **Apply**.
  4. Click **More Actions > Create Sink** from the menu.
  5. Provide the following configurations: 
     1. **Sink Details** : enter a name and description.
     2. Click **Next**.
     3. **Sink Destination** : select **Cloud Storage Bucket**.
     4. **Cloud Storage Bucket** : select the bucket created earlier or create a new bucket.
     5. Click **Next**.
     6. **Choose Logs to include in Sink** : a default log is populated when you select an option in Cloud Storage Bucket.
     7. Click **Next**.
     8. Optional: **Choose Logs to filter out of Sink** : select the logs that you would like not to sink.
  6. Click **Create Sink**.



## Set up feeds

To configure a feed, follow these steps:

  1. Go to **SIEM Settings** > **Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed; for example, **Cloud Run Logs**.
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **GCP Cloud Run** as the **Log type**.
  7. Click **Get Service Account** as the **Chronicle Service Account**.
  8. Click **Next**.
  9. Specify values for the following input parameters:

     * **Storage Bucket URI** : Google Cloud storage bucket URL in **`gs://my-bucket/<value>/`** format. This URL must end with a trailing forward slash (/).
     * **Source deletion options** : select deletion option according to your preference.

**Note:** If you select the `Delete transferred files` or `Delete transferred files and empty directories` option, make sure that you granted appropriate permissions to the service account.
     * **Maximum File Age** : Includes files modified in the last number of days. Default is 180 days.

  10. Click **Next**.

  11. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## UDM Mapping Table

Log Field | UDM Mapping | Logic  
---|---|---  
`httpRequest.latency` | `target.resource.attribute.labels.[]` | The value of `httpRequest.latency` from the raw log is used as the value for a label with key `http_request_latency` within `target.resource.attribute.labels`.  
`httpRequest.protocol` | `network.application_protocol` | If `httpRequest.protocol` contains `HTTP`, the UDM field is set to `HTTP`.  
`httpRequest.remoteIp` | `principal.asset.ip` | The value of `httpRequest.remoteIp` from the raw log is used.  
`httpRequest.remoteIp` | `principal.ip` | The value of `httpRequest.remoteIp` from the raw log is used.  
`httpRequest.requestMethod` | `network.http.method` | The value of `httpRequest.requestMethod` from the raw log is used.  
`httpRequest.requestSize` | `network.sent_bytes` | The value of `httpRequest.requestSize` from the raw log is converted to an unsigned integer and used.  
`httpRequest.requestUrl` | `target.url` | The value of `httpRequest.requestUrl` from the raw log is used.  
`httpRequest.responseSize` | `network.received_bytes` | The value of `httpRequest.responseSize` from the raw log is converted to an unsigned integer and used.  
`httpRequest.serverIp` | `target.asset.ip` | The value of `httpRequest.serverIp` from the raw log is used.  
`httpRequest.serverIp` | `target.ip` | The value of `httpRequest.serverIp` from the raw log is used.  
`httpRequest.status` | `network.http.response_code` | The value of `httpRequest.status` from the raw log is converted to an integer and used.  
`httpRequest.userAgent` | `network.http.parsed_user_agent` | The value of `httpRequest.userAgent` from the raw log is parsed as a user agent string.  
`httpRequest.userAgent` | `network.http.user_agent` | The value of `httpRequest.userAgent` from the raw log is used.  
`insertId` | `metadata.product_log_id` | The value of `insertId` from the raw log is used.  
`labels.instanceId` | `additional.fields.[]` | The value of `labels.instanceId` is used as the value for a label with key `instanceId` within `additional.fields`.  
`labels.run.googleapis.com_execution_name` | `additional.fields.[]` | The value of `labels.run.googleapis.com_execution_name` is used as the value for a label with key `execution_name` within `additional.fields`.  
`labels.run.googleapis.com_task_attempt` | `additional.fields.[]` | The value of `labels.run.googleapis.com_task_attempt` is used as the value for a label with key `task_attempt` within `additional.fields`.  
`labels.run.googleapis.com_task_index` | `additional.fields.[]` | The value of `labels.run.googleapis.com_task_index` is used as the value for a label with key `task_index` within `additional.fields`.  
`logName` | `metadata.product_event_type` | The value of `logName` from the raw log is used.  
`resource.labels.configuration_name` | `target.resource.attribute.labels.[]` | The value of `resource.labels.configuration_name` is used as the value for a label with key `configuration_name` within `target.resource.attribute.labels`.  
`resource.labels.job_name` | `additional.fields.[]` | The value of `resource.labels.job_name` is used as the value for a label with key `job_name` within `additional.fields`.  
`resource.labels.location` | `target.location.name` | The value of `resource.labels.location` from the raw log is used.  
`resource.labels.project_id` | `target.resource.attribute.labels.[]` | The value of `resource.labels.project_id` is used as the value for a label with key `project_id` within `target.resource.attribute.labels`.  
`resource.labels.revision_name` | `target.resource.attribute.labels.[]` | The value of `resource.labels.revision_name` is used as the value for a label with key `revision_name` within `target.resource.attribute.labels`.  
`resource.labels.service_name` | `target.resource.attribute.labels.[]` | The value of `resource.labels.service_name` is used as the value for a label with key `service_name` within `target.resource.attribute.labels`.  
`resource.type` | `target.resource.resource_subtype` | The value of `resource.type` from the raw log is used.  
`severity` | `security_result.severity` | If the value of `severity` matches `Info` (case-insensitive), the UDM field is set to `INFORMATIONAL`.  
`textPayload` | `additional.fields.[]` | The value of `textPayload` is used as the value for a label with key `Textpayload` within `additional.fields`.  
`timestamp` | `metadata.event_timestamp` | The value of `timestamp` from the raw log is parsed as a timestamp.  
`timestamp` | `timestamp` | The value of `timestamp` from the raw log is parsed as a timestamp. Determined by parser logic based on the presence of certain fields. Defaults to `GENERIC_EVENT`. If `has_principal_ip`, `has_target_ip`, and `httpRequest.protocol` matches `HTTP`, it's set to `NETWORK_HTTP`. Hardcoded to `GCP_RUN`. Hardcoded to `GCP_RUN`. Hardcoded to `Google Cloud Platform`. Hardcoded to `GOOGLE_CLOUD_PLATFORM`.  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
