---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloud-ids/
title: Collect Cloud Intrusion Detection System (Cloud IDS) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:33:33.597685+00:00
---

# Collect Cloud Intrusion Detection System (Cloud IDS) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloud-ids/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Cloud Intrusion Detection System (Cloud IDS) logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to export and ingest Cloud IDS logs into Google Security Operations using Cloud Storage. The parser transforms raw JSON formatted Cloud IDS logs from Google Cloud into a structured UDM format. It extracts relevant fields, maps them to UDM schema, categorizes events, and enriches the data with additional context like network direction and resource types. 

## Before you begin

Ensure that you have the following prerequisites:

  * Google SecOps instance.
  * Cloud IDS is set up and active in your Google Cloud environment.
  * Privileged access to Google Cloud and appropriate permissions to access Cloud IDS.



## Create a Cloud Storage bucket

  1. Sign in to the [Google Cloud console](https://console.cloud.google.com/).
  2. Go to the **Cloud Storage Buckets** page.

[Go to Buckets](https://console.cloud.google.com/storage/browser)

  3. Click **Create**.

  4. On the **Create a bucket** page, enter your bucket information. After each of the following steps, click **Continue** to proceed to the next step:

     1. In the **Get started** section, do the following:

        1. Enter a unique name that meets the bucket name requirements; for example, **gcp-ids-logs**.
        2. To enable hierarchical namespace, click the expander arrow to expand the **Optimize for file oriented and data-intensive workloads** section, and then select **Enable Hierarchical namespace on this bucket**.

**Note:** You cannot enable hierarchical namespace on an existing bucket.
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


**Note:** Be sure to provide your Google SecOps service account with permissions to Read or Read & Write to the newly created bucket.

## Configure Cloud IDS logs export

  1. Sign in to the [Google Cloud console](https://console.cloud.google.com/).
  2. Go to **Logging > Log Router**.
  3. Click **Create Sink**.
  4. Provide the following configuration parameters:

     * **Sink Name** : enter a meaningful name; for example, `google-cloud-ids-logs-sink`.
     * **Sink Destination** : select **Cloud Storage** and provide the Google Cloud storage bucket URI; for example, `gs://gcp-ids-logs`.
     * **Log Filter** :
           
           logName="projects/<your-project-id>/logs/cloud-ids"
           

  5. Click **Create**.




## Configure permissions for Cloud Storage

  1. Go to **IAM & Admin > IAM**.
  2. Locate the **Cloud Logging** service account.
  3. Grant the **roles/storage.admin** on the bucket.



## Set up feeds

To configure a feed, follow these steps:

  1. Go to **SIEM Settings** > **Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed; for example, **GCP IDS Logs**.
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **GCP IDS** as the **Log type**.
  7. Click **Get Service Account** next to the **Chronicle Service Account** field.
  8. Click **Next**.
  9. Specify values for the following input parameters: 
     * **Storage Bucket URI** : Cloud Storage bucket URL; for example, `gs://gcp-ids-logs`.
     * **Source deletion options** : select the deletion option according to your preference.. Note: If you select the `Delete transferred files` or `Delete transferred files and empty directories` option, make sure that you granted appropriate permissions to the service account.
     * **Maximum File Age** : Includes files modified in the last number of days. Default is 180 days
  10. Click **Next**.
  11. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.



## UDM Mapping Table

Log Field | UDM Mapping | Logic  
---|---|---  
insertId | metadata.product_log_id | Direct mapping.  
jsonPayload.alert_severity | security_result.severity | Direct mapping.  
jsonPayload.alert_time | metadata.event_timestamp | Direct mapping.  
jsonPayload.application | principal.application | Direct mapping, only if direction is server-to-client.  
jsonPayload.application | target.application | Direct mapping, only if direction is client-to-server or logName contains `traffic`.  
jsonPayload.category | security_result.category | Mapped based on the value of 'jsonPayload.category':  
\- 'dos': NETWORK_DENIAL_OF_SERVICE  
\- 'info-leak': NETWORK_SUSPICIOUS  
\- 'protocol-anomaly': NETWORK_MALICIOUS  
\- 'backdoor', 'spyware', 'trojan': SOFTWARE_MALICIOUS  
jsonPayload.category | security_result.category_details | Direct mapping.  
jsonPayload.cves | extensions.vulns.vulnerabilities.cve_id | Direct mapping, iterating over the array.  
jsonPayload.destination_ip_address | target.ip | Direct mapping.  
jsonPayload.destination_port | target.port | Direct mapping.  
jsonPayload.details | extensions.vulns.vulnerabilities.description | Direct mapping.  
jsonPayload.details | security_result.detection_fields.value | Mapped if 'jsonPayload.repeat_count' exists. The key is set to 'repeat_count'.  
jsonPayload.direction | network.direction | Mapped based on the value of 'jsonPayload.direction':  
\- 'client-to-server': OUTBOUND  
\- 'server-to-client': INBOUND  
jsonPayload.elapsed_time | network.session_duration.seconds | Direct mapping.  
jsonPayload.ip_protocol | network.ip_protocol | Direct mapping, converting to uppercase and then mapping to protocol number.  
jsonPayload.name | security_result.threat_name | Direct mapping.  
jsonPayload.network | principal.resource.name | Direct mapping, only if direction is server-to-client.  
jsonPayload.network | target.resource.name | Direct mapping, only if direction is client-to-server or logName contains `traffic`.  
jsonPayload.repeat_count | security_result.detection_fields.value | Mapped if it exists. The key is set to 'repeat_count'.  
jsonPayload.session_id | network.session_id | Direct mapping.  
jsonPayload.source_ip_address | principal.ip | Direct mapping.  
jsonPayload.source_port | principal.port | Direct mapping.  
jsonPayload.start_time | about.labels.value | Mapped if it exists. The key is set to 'start_time'.  
jsonPayload.start_time | additional.fields.value.string_value | Mapped if it exists. The key is set to 'start_time'.  
jsonPayload.threat_id | security_result.threat_id | Direct mapping.  
jsonPayload.total_bytes | about.labels.value | Mapped if it exists. The key is set to 'total_bytes'.  
jsonPayload.total_bytes | additional.fields.value.string_value | Mapped if it exists. The key is set to 'total_bytes'.  
jsonPayload.total_packets | about.labels.value | Mapped if it exists. The key is set to 'total_packets'.  
jsonPayload.total_packets | additional.fields.value.string_value | Mapped if it exists. The key is set to 'total_packets'.  
jsonPayload.type | security_result.detection_fields.value | Mapped if it exists. The key is set to 'type'.  
jsonPayload.uri_or_filename | target.file.full_path | Direct mapping.  
logName | security_result.category_details | Direct mapping.  
receiveTimestamp | metadata.collected_timestamp | Direct mapping.  
resource.labels.id | observer.resource.product_object_id | Direct mapping.  
resource.labels.location | observer.location.name | Direct mapping.  
resource.labels.resource_container | observer.resource.name | Direct mapping.  
resource.type | observer.resource.resource_subtype | Direct mapping.  
| metadata.event_type | Determined by a set of conditional rules based on the presence and values of other fields, defaulting to 'GENERIC_EVENT'.  
| metadata.vendor_name | Static value: `Google Cloud Platform`.  
| metadata.product_name | Static value: `GCP_IDS`.  
| metadata.log_type | Static value: `GCP_IDS`.  
| extensions.vulns.vulnerabilities.vendor | Static value: `GCP_IDS`, added for each CVE in 'jsonPayload.cves'.  
| principal.resource.resource_type | Static value: `VPC_NETWORK`, added if 'jsonPayload.network' exists and direction is server-to-client.  
| target.resource.resource_type | Static value: `VPC_NETWORK`, added if 'jsonPayload.network' exists and direction is client-to-server or logName contains `traffic`.  
| observer.resource.resource_type | Static value: `CLOUD_PROJECT`, added if 'resource.labels.resource_container' or 'resource.type' exists.  
| observer.resource.attribute.cloud.environment | Static value: `GOOGLE_CLOUD_PLATFORM`, added if 'resource.labels.resource_container' or 'resource.type' exists.  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
