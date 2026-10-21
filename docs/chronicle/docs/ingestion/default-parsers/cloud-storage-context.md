---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloud-storage-context/
title: Collect Cloud Storage context logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T12:11:06.973731+00:00
---

# Collect Cloud Storage context logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloud-storage-context/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Cloud Storage context logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to export and ingest Cloud Storage context logs into Google Security Operations using Cloud Storage. The parser cleans up and structures incoming JSON data from Cloud Storage logs. Then, it maps relevant fields to the unified data model (UDM), enriching the data with labels and metadata for consistent representation and analysis within the security ecosystem. 

## Before you begin

Ensure that you have the following prerequisites:

  * Google SecOps instance.
  * Cloud Storage is set up and active in your Google Cloud environment.
  * Privileged access to Google Cloud and appropriate permissions.



## Create a Cloud Storage bucket

  1. Sign in to the [Google Cloud console](https://console.cloud.google.com/).
  2. Go to the **Cloud Storage Buckets** page.

[Go to Buckets](https://console.cloud.google.com/storage/browser)

  3. Click **Create**.

  4. On the **Create a bucket** page, enter your bucket information. After each of the following steps, click **Continue** to proceed to the next step:

     1. In the **Get started** section, do the following:

        1. Enter a unique name that meets the bucket name requirements; for example, **google-storage-context-logs**.
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

## Configure Cloud Storage context logs export

  1. Sign in to the [Google Cloud console](https://console.cloud.google.com/).
  2. Go to **Logging > Log Router**.
  3. Click **Create Sink**.
  4. Provide the following configuration parameters:

     * **Sink Name** : enter a meaningful name; for example, `Storage-Context-Sink`.
     * **Sink Destination** : select **Cloud Storage Storage** and enter the URI for your bucket; for example, `gs://google-storage-context-logs/`.
     * **Log Filter** :
           
           logName="*storage*"
           resource.type="gcs_bucket"
           

  5. Click **Create**.




## Configure permissions for Cloud Storage

  1. Go to **IAM & Admin > IAM**.
  2. Locate the **Cloud Logging** service account.
  3. Grant the **roles/storage.admin** on the bucket.



## Set up feeds

There are two different entry points to set up feeds in the Google SecOps platform: 

  * **SIEM Settings > Feeds > Add New Feed**
  * **Content Hub > Content Packs > Get Started**



## How to set up the Cloud storage context feed

  1. Click the **Google Cloud Compute platform** pack.
  2. Locate the **GCP Google Cloud Storage Context** log type and click **Add new feed**.
  3. Specify values for the following fields:

     * **Source Type** : **Google Cloud Storage V2**.
     * **Storage Bucket URI** : Cloud Storage bucket URL; for example, `gs://compute-context-logs/`. This URL must end with a trailing forward slash (/).
     * **Source deletion options** : select the deletion option according to your preference.

**Note:** If you select the `Delete transferred files` or `Delete transferred files and empty directories` option, make sure that you granted appropriate permissions to the service account.

  * **Maximum File Age** : Include files modified within the last number of days. Default is 180 days.



**Advanced options**

  * **Feed Name** : A prepopulated value that identifies the feed.
  * **Asset Namespace** : Namespace associated with the feed.
  * **Ingestion Labels** : Labels applied to all events from this feed.


  1. Click **Create feed.**

**Note:** The Content Hub is not available on the SIEM standalone platform. To upgrade, contact your Google SecOps representative.

For more information about configuring multiple feeds for different log types within this product family, see [Configure feeds by product](https://docs.cloud.google.com/chronicle/docs/ingestion/ingestion-entities/configure-multiple-feeds).

## UDM Mapping Table

Log field | UDM mapping | Logic  
---|---|---  
ancestors | event.idm.entity.entity.resource.attribute.labels.value | The ancestor value is extracted from the ancestors array in the raw log.  
assetType | event.idm.entity.entity.resource.type | Directly mapped from the assetType field in the raw log.  
insertId | event.idm.entity.metadata.product_entity_id | Directly mapped from the insertId field in the raw log.  
labels.compute.googleapis.com/resource_name | event.idm.entity.entity.resource.name | Directly mapped from the labels.compute.googleapis.com/resource_name field in the raw log.  
labels.k8s-pod/controller-revision-hash | event.idm.entity.entity.file.sha1 | Directly mapped from the labels.k8s-pod/controller-revision-hash field in the raw log.  
labels.k8s-pod/name | event.idm.entity.entity.resource.attribute.labels.value | Directly mapped from the labels.k8s-pod/name field in the raw log.  
labels.k8s-pod/pod-template-generation | event.idm.entity.entity.resource.attribute.labels.value | Directly mapped from the labels.k8s-pod/pod-template-generation field in the raw log.  
logName | event.idm.entity.entity.resource.attribute.labels.value | Directly mapped from the logName field in the raw log.  
name | event.idm.entity.entity.resource.name | Directly mapped from the name field in the raw log.  
receiveTimestamp | event.idm.entity.entity.resource.attribute.creation_time | Converted to timestamp format from the receiveTimestamp field in the raw log.  
resource.data.iamConfiguration.publicAccessPrevention | event.idm.entity.entity.resource.attribute.labels.value | Directly mapped from the resource.data.iamConfiguration.publicAccessPrevention field in the raw log.  
resource.data.id | event.idm.entity.entity.resource.product_object_id | Directly mapped from the resource.data.id field in the raw log.  
resource.data.kind | event.idm.entity.entity.resource.type | Directly mapped from the resource.data.kind field in the raw log.  
resource.data.labels.app_id | event.idm.entity.entity.resource.attribute.labels.value | Directly mapped from the resource.data.labels.app_id field in the raw log.  
resource.data.labels.app_name | event.idm.entity.entity.resource.attribute.labels.value | Directly mapped from the resource.data.labels.app_name field in the raw log.  
resource.data.labels.bucket_id | event.idm.entity.entity.resource.attribute.labels.value | Directly mapped from the resource.data.labels.bucket_id field in the raw log.  
resource.data.labels.data_classification | event.idm.entity.entity.resource.attribute.labels.value | Directly mapped from the resource.data.labels.data_classification field in the raw log.  
resource.data.labels.dept_name | event.idm.entity.entity.resource.attribute.labels.value | Directly mapped from the resource.data.labels.dept_name field in the raw log.  
resource.data.labels.dept_no | event.idm.entity.entity.resource.attribute.labels.value | Directly mapped from the resource.data.labels.dept_no field in the raw log.  
resource.data.labels.environment | event.idm.entity.entity.resource.attribute.labels.value | Directly mapped from the resource.data.labels.environment field in the raw log.  
resource.data.labels.goog-composer-environment | event.idm.entity.entity.resource.attribute.labels.value | Directly mapped from the resource.data.labels.goog-composer-environment field in the raw log.  
resource.data.labels.goog-composer-location | event.idm.entity.entity.resource.attribute.labels.value | Directly mapped from the resource.data.labels.goog-composer-location field in the raw log.  
resource.data.labels.goog-composer-version | event.idm.entity.entity.resource.attribute.labels.value | Directly mapped from the resource.data.labels.goog-composer-version field in the raw log.  
resource.data.labels.technical_contact | event.idm.entity.entity.resource.attribute.labels.value | Directly mapped from the resource.data.labels.technical_contact field in the raw log.  
resource.data.labels.type | event.idm.entity.entity.resource.attribute.labels.value | Directly mapped from the resource.data.labels.type field in the raw log.  
resource.data.location | event.idm.entity.entity.location.name | Directly mapped from the resource.data.location field in the raw log.  
resource.data.projectNumber | event.idm.entity.entity.resource.attribute.cloud.project.id | Directly mapped from the resource.data.projectNumber field in the raw log.  
resource.data.selfLink | event.idm.entity.entity.url | Directly mapped from the resource.data.selfLink field in the raw log.  
resource.data.timeCreated | event.idm.entity.entity.resource.attribute.creation_time | Converted to timestamp format from the resource.data.timeCreated field in the raw log.  
resource.data.updated | event.idm.entity.entity.resource.attribute.last_update_time | Converted to timestamp format from the resource.data.updated field in the raw log.  
resource.discoveryDocumentUri | event.idm.entity.entity.file.full_path | Directly mapped from the resource.discoveryDocumentUri field in the raw log.  
resource.labels.cluster_name | event.idm.entity.entity.resource.attribute.labels.value | Directly mapped from the resource.labels.cluster_name field in the raw log.  
resource.labels.container_name | event.idm.entity.entity.resource.attribute.labels.value | Directly mapped from the resource.labels.container_name field in the raw log.  
resource.labels.location | event.idm.entity.entity.location.name | Directly mapped from the resource.labels.location field in the raw log.  
resource.labels.namespace_name | event.idm.entity.entity.resource.attribute.labels.value | Directly mapped from the resource.labels.namespace_name field in the raw log.  
resource.labels.pod_name | event.idm.entity.entity.resource.attribute.labels.value | Directly mapped from the resource.labels.pod_name field in the raw log.  
resource.labels.project_id | event.idm.entity.entity.resource.attribute.cloud.project.id | Directly mapped from the resource.labels.project_id field in the raw log.  
resource.parent | event.idm.entity.entity.resource.parent | Directly mapped from the resource.parent field in the raw log.  
resource.type | event.idm.entity.entity.resource.type | Directly mapped from the resource.type field in the raw log.  
resource.version | event.idm.entity.entity.resource.attribute.labels.value | Directly mapped from the resource.version field in the raw log.  
textPayload | event.idm.entity.entity.resource.attribute.labels.value | Directly mapped from the textPayload field in the raw log.  
N/A | event.idm.entity.metadata.collected_timestamp | The collected timestamp is the log entry timestamp.  
N/A | event.idm.entity.metadata.entity_type | Hardcoded to `RESOURCE`.  
N/A | event.idm.entity.metadata.product_name | Hardcoded to `GCP Storage Context`.  
N/A | event.idm.entity.metadata.vendor_name | Hardcoded to `Google Cloud Platform`.  
N/A | event.idm.entity.entity.resource.attribute.cloud.environment | Hardcoded to `GOOGLE_CLOUD_PLATFORM`.  
N/A | event.idm.entity.entity.resource.resource_type | Hardcoded to `STORAGE_BUCKET`.  
N/A | event.timestamp | The event timestamp is the log entry timestamp.  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
