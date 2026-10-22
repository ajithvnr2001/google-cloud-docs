---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/iam-analysis/
title: Collect Identity and Access Management (IAM) Analysis context logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:37:11.286716+00:00
---

# Collect Identity and Access Management (IAM) Analysis context logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/iam-analysis/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Identity and Access Management (IAM) Analysis context logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to export and ingest IAM Analysis logs into Google Security Operations using Cloud Storage. The parser extracts user and resource information from IAM JSON data. It then maps the extracted fields to the UDM, creating user entities with associated roles and resource relationships, ultimately enriching security context within the Google SecOps platform.

## Before you begin

Ensure that you have the following prerequisites:

  * Google SecOps instance.
  * IAM is set up and active in your Google Cloud environment.
  * Privileged access to Google Cloud and appropriate permissions to access IAM logs.



## Create a Cloud Storage bucket

  1. Sign in to the [Google Cloud console](https://console.cloud.google.com/).
  2. Go to the **Cloud Storage Buckets** page.

[Go to Buckets](https://console.cloud.google.com/storage/browser)

  3. Click **Create**.

  4. On the **Create a bucket** page, enter your bucket information. After each of the following steps, click **Continue** to proceed to the next step:

     1. In the **Get started** section, do the following:

        1. Enter a unique name that meets the bucket name requirements; for example, **google-cloud-iam-logs**.
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

## Configure IAM Analysis logs export

  1. Sign in to the [Google Cloud console](https://console.cloud.google.com/).
  2. Go to **Logging > Log Router**.
  3. Click **Create Sink**.
  4. Provide the following configuration parameters:

     * **Sink Name** : enter a meaningful name; for example, `IAM-Analysis-Sink`.
     * **Sink Destination** : select **Cloud Storage Storage** and enter the URI for your bucket; for example, `gs://gcp-iam-analysis-logs/`.
     * **Log Filter** :
           
           logName="*iam*"
           resource.type="gce_instance"
           




## Configure permissions for Cloud Storage

  1. Go to **IAM & Admin > IAM**.
  2. Locate the **Cloud Logging** service account.
  3. Grant the **roles/storage.admin** on the bucket.



## Set up feeds

To configure a feed, follow these steps:

  1. Go to **SIEM Settings** > **Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed; for example, **IAM Analysis Logs**.
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **GCP IAM Analysis** as the **Log type**.
  7. Click **Get Service Account** next to the **Chronicle Service Account** field.
  8. Click **Next**.
  9. Specify values for the following input parameters:

     * **Storage Bucket URI** : Cloud Storage bucket URL; for example, `gs://gcp-iam-analysis-logs/`. This URL must end with a trailing forward slash (/).
     * **Source deletion options** : select the deletion option according to your preference.

**Note:** If you select the `Delete transferred files` or `Delete transferred files and empty directories` option, make sure that you granted appropriate permissions to the service account.
     * **Maximum File Age** : Includes files modified in the last number of days. Default is 180 days.

  10. Click **Next**.

  11. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## UDM Mapping Table

Log Field | UDM Mapping | Logic  
---|---|---  
accessControlLists.accesses.permission | relations.entity.resource.attribute.permissions.name | Directly from the `accessControlLists.accesses.permission` field in the raw log.  
attachedResourceFullName | relations.entity.resource.name | Directly from the `attachedResourceFullName` field in the raw log, but with any trailing resource names removed.  
| relations.entity.resource.attribute.cloud.environment | Set to `GOOGLE_CLOUD_PLATFORM`.  
| relations.entity.resource.product_object_id | For STORAGE_BUCKET, directly from the `attachedResourceFullName` field in the raw log, but with any trailing resource names removed. For BigQuery datasets, it's the `projectName` (extracted from `attachedResourceFullName`) followed by a colon and the `datasetName` (extracted from `attachedResourceFullName`) field.  
| relations.entity.resource.resource_type | Determined by the pattern of the `attachedResourceFullName` field in the raw log.  
| relations.entity_type | Set to `RESOURCE`, except for SERVICE_ACCOUNT, where it's set to `USER`.  
| relations.relationship | Set to `MEMBER`.  
| metadata.collected_timestamp | Directly from the `timestamp` field in the raw log.  
| metadata.entity_type | Set to `USER`.  
| metadata.product_name | Set to `GCP IAM ANALYSIS`.  
| metadata.vendor_name | Set to `Google Cloud Platform`.  
iamBinding.role | entity.user.attribute.roles.name | Directly from the `iamBinding.role` field in the raw log.  
identityList.identities.name | entity.user.attribute.roles.type | Set to `SERVICE_ACCOUNT` if the `identityList.identities.name` field contains the string `serviceAccount`.  
| entity.user.email_addresses | If the `identityList.identities.name` field contains an `@` symbol, it's treated as an email address.  
| entity.user.userid | If the `identityList.identities.name` field doesn't contain an `@` symbol, it's treated as a userid.  
identityList.identities.product_object_id | entity.user.product_object_id | Directly from the `identityList.identities.product_object_id` field in the raw log.  
timestamp | timestamp | Directly from the `timestamp` field in the raw log.  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
