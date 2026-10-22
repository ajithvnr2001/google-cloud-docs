---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloud-compute-context/
title: Collect Google Cloud Compute context logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:54:21.498927+00:00
---

# Collect Google Cloud Compute context logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloud-compute-context/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Google Cloud Compute context logs

**Parser Version:** 3.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to export and ingest Google Cloud Compute context logs into Google Security Operations using Cloud Storage. The parser extracts information from the logs in JSON format. It then normalizes and structures the extracted data into the Google SecOps UDM format, focusing on details about virtual machines like hardware specs, network configuration, security settings, and relationships to other entities. 

## Before you begin

Ensure that you have the following prerequisites:

  * Google SecOps instance.
  * Compute is set up and active in your Google Cloud environment.
  * Privileged access to Google Cloud and appropriate permissions.



### Create a Cloud Storage bucket

  1. Sign in to the [Google Cloud console](https://console.cloud.google.com/).
  2. Go to the **Cloud Storage Buckets** page.

[Go to Buckets](https://console.cloud.google.com/storage/browser)

  3. Click **Create**.

  4. On the **Create a bucket** page, enter your bucket information. After each of the following steps, click **Continue** to proceed to the next step:

     1. In the **Get started** section, do the following:

        1. Enter a unique name that meets the bucket name requirements; for example, **compute-context-logs**.
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

## Configure Google Cloud Compute logs export

  1. Sign in to the [Google Cloud console](https://console.cloud.google.com/).
  2. Go to **Logging > Log Router**.
  3. Click **Create Sink**.
  4. Provide the following configuration parameters:

     * **Sink Name** : enter a meaningful name; for example, `Compute-Context-Sink`.
     * **Sink Destination** : select **Cloud Storage Storage** and enter the URI for your bucket; for example, `gs://compute-context-logs/`.
     * **Log Filter** :
           
           logName="*compute*"
           resource.type="gce_instance"
           

  5. Click **Create**.




## Configure permissions for Cloud Storage

  1. Go to **IAM & Admin > IAM**.
  2. Locate the **Cloud Logging** service account.
  3. Grant the **roles/storage.admin** on the bucket.



## Set up feeds

There are two different entry points to set up feeds in the Google SecOps platform: 

  * **SIEM Settings > Feeds > Add New Feed**
  * **Content Hub > Content Packs > Get Started**



## How to set up the Google Cloud Compute Context feed

  1. Click the **Google Cloud Compute platform** pack.
  2. Locate the **GCP Compute Context** log type. 
  3. Specify the following values:

     * **Source Type** : Google Cloud Storage V2.
     * **Storage Bucket URI** : Cloud Storage bucket URL; for example, `gs://compute-context-logs/`. This URL must end with a trailing forward slash (/).
     * **Source deletion options** : select the deletion option according to your preference.

**Note:** If you select the `Delete transferred files` or `Delete transferred files and empty directories` option, make sure that you granted appropriate permissions to the service account.
     * **Maximum File Age** : Files modified in the last number of days. Default is 180 days.

     * **Chronicle Service Account** : Copy the Service Account. You'll need it to add permissions in the bucket for this Service Account to let Google SecOps read or delete data in the bucket.

**Advanced options**

     * **Feed Name** : A prepopulated value that identifies the feed.
     * **Asset Namespace** : Namespace associated with the feed.
     * **Ingestion Labels** : Labels applied to all events from this feed.
  4. Click **Create feed**.


**Note:** The Content Hub is not available on the SIEM standalone platform. To upgrade, contact your Google SecOps representative.

For more information about configuring multiple feeds for different log types within this product family, see [Configure feeds by product](https://docs.cloud.google.com/chronicle/docs/ingestion/ingestion-entities/configure-multiple-feeds).

## UDM Mapping Table

Log Field | UDM Mapping | Logic  
---|---|---  
ancestors | event.idm.entity.entity.asset.attribute.labels.value | Each ancestor value in the ancestors array is mapped to a separate label with the key `ancestors`.  
assetType | event.idm.entity.entity.asset.category | Directly mapped from the assetType field.  
asset_type | event.idm.entity.entity.asset.category | Directly mapped from the asset_type field.  
name | event.idm.entity.entity.resource.name | Directly mapped from the name field.  
resource.data.cpuPlatform | event.idm.entity.entity.asset.hardware.cpu_platform | Directly mapped from the resource.data.cpuPlatform field.  
resource.data.creationTimestamp | event.idm.entity.entity.asset.attribute.creation_time | Parsed to a timestamp format from the resource.data.creationTimestamp field.  
resource.data.id | event.idm.entity.entity.asset.product_object_id | Directly mapped from the resource.data.id field.  
resource.data.labels.business_function | event.idm.entity.entity.asset.attribute.labels.value | Directly mapped from the resource.data.labels.business_function field, with the key set to `business_function`.  
resource.data.labels.environment | event.idm.entity.entity.asset.attribute.labels.value | Directly mapped from the resource.data.labels.environment field, with the key set to `environment`.  
resource.data.labels.infra_location | event.idm.entity.entity.asset.attribute.labels.value | Directly mapped from the resource.data.labels.infra_location field, with the key set to `infra_location`.  
resource.data.labels.instance_group | event.idm.entity.user.group_identifiers | Directly mapped from the resource.data.labels.instance_group field.  
resource.data.labels.os | event.idm.entity.entity.asset.platform_software.platform_version | Directly mapped from the resource.data.labels.os field.  
resource.data.labels.primary_application | event.idm.entity.entity.asset.attribute.labels.value | Directly mapped from the resource.data.labels.primary_application field, with the key set to `primary_application`.  
resource.data.labels.project_code | event.idm.entity.entity.asset.attribute.labels.value | Directly mapped from the resource.data.labels.project_code field, with the key set to `project_code`.  
resource.data.lastStartTimestamp | event.idm.entity.entity.asset.last_boot_time | Parsed to a timestamp format from the resource.data.lastStartTimestamp field.  
resource.data.machineType | event.idm.entity.entity.asset.hardware.model | The machine type is extracted from the resource.data.machineType field using a regular expression.  
resource.data.name | event.idm.entity.entity.asset.hostname | Directly mapped from the resource.data.name field.  
resource.data.networkInterfaces.0.accessConfigs.0.natIP | event.idm.entity.entity.asset.nat_ip | The first NAT IP address from the first network interface is mapped.  
resource.data.networkInterfaces.0.network | event.idm.entity.entity.asset.attribute.cloud.vpc.name | The network ID is extracted from the resource.data.networkInterfaces.0.network field using a regular expression.  
resource.data.networkInterfaces.0.networkIP | event.idm.entity.entity.asset.ip | The IP address of the first network interface is mapped.  
resource.data.networkInterfaces.1.networkIP | event.idm.entity.entity.asset.ip | The IP address of the second network interface is mapped.  
resource.data.selfLink | event.idm.entity.entity.url | Directly mapped from the resource.data.selfLink field.  
resource.data.serviceAccounts.0.email | event.idm.entity.relations.entity.user.email_addresses | The email address of the first service account is mapped.  
resource.data.status | event.idm.entity.entity.asset.deployment_status | Mapped to `ACTIVE` if the status is one of `RUNNING`, `PROVISIONING`, `STAGING`, `STOPPING`, `SUSPENDING`, `SUSPENDED`, `REPAIRING`, `TERMINATED`. Otherwise, mapped to `DEPLOYMENT_STATUS_UNSPECIFIED`.  
| event.idm.entity.entity.asset.attribute.cloud.availability_zone | The availability zone is constructed by combining the region and zone_suffix fields.  
| event.idm.entity.entity.asset.attribute.cloud.environment | Set to `GOOGLE_CLOUD_PLATFORM`.  
| event.idm.entity.entity.asset.attribute.cloud.project.name | The project ID is extracted from the name field using a regular expression.  
| event.idm.entity.entity.asset.attribute.cloud.project.resource_type | Set to `CLOUD_PROJECT`.  
| event.idm.entity.entity.asset.attribute.cloud.vpc.resource_type | Set to `VPC_NETWORK`.  
| event.idm.entity.entity.resource.resource_type | Set to `VIRTUAL_MACHINE` if asset_type or assetType contains `Instance`.  
| event.idm.entity.entity.resource.type | Set to `VIRTUAL_MACHINE` if asset_type or assetType contains `Instance`.  
| event.idm.entity.metadata.collected_timestamp | Set to the Logstash event timestamp.  
| event.idm.entity.metadata.entity_type | Set to `ASSET`.  
| event.idm.entity.metadata.product_name | Set to `GCP Compute Context`.  
| event.idm.entity.metadata.vendor_name | Set to `Google Cloud Platform`.  
| event.idm.entity.relations.entity.user.attribute.cloud.environment | Set to `GOOGLE_CLOUD_PLATFORM`.  
| event.idm.entity.relations.entity_type | Set to `USER`.  
| event.idm.entity.relations.relationship | Set to `ADMINISTERS`.  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
