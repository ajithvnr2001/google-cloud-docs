---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gcp-cloudidentity-deviceusers/
title: Collect Cloud Identity Device Users logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:39:03.180889+00:00
---

# Collect Cloud Identity Device Users logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gcp-cloudidentity-deviceusers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Cloud Identity Device Users logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to collect Cloud Identity Device Users logs into Google Security Operations using the **Third Party API** method, which is the recommended approach. The parser first extracts data from JSON formatted `Cloud Identity Device Users` logs and transforms the timestamp to the standardized format. Then, it maps specific fields from the raw log data to the corresponding fields in the unified data model (UDM) for user entities, their relationships to assets, and additional user attributes like management and password states.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * **Domain-Wide Delegation setup** for a Service Account. The Service Account must be authorized for the following scope: 
    * **`https://www.googleapis.com/auth/cloud-identity.devices.readonly`**
  * The following APIs are enabled in your Google Cloud project: 
    * **Cloud Identity API**
    * **Google Workspace Admin SDK**
    * **Alert Center API**



## Recommended: Set up Third Party API Feeds

There are two different entry points to set up feeds in the Google SecOps platform: 

  * **SIEM Settings > Feeds > Add New Feed**
  * **Content Hub > Content Packs > Get Started**



## How to set up the Google Cloud Identity Device Users feed

  1. Click the **Google Cloud Compute platform** pack.
  2. Locate the **Google Cloud Identity Device Users** log type and click **Add new feed**.
  3. Specify values for the following fields: 
     * **Source Type** : Select **Third party API**.
     * **OAuth JWT endpoint** : Enter the OAuth token endpoint: `https://oauth2.googleapis.com/token`
     * **JWT claims issuer** : Enter the Enter the **email address** of the Service Account (found in the Service Account's JSON key file).
     * **JWT claims subject** : Enter the email address of the user who is granted the role of **services admin** or **super admin** in the Workspace console (the user being impersonated through Domain-Wide Delegation).
     * **JWT claims audience** : Enter the endpoint again: `https://oauth2.googleapis.com/token`
     * **RSA private key** : Paste the full contents of the **private key** from the Service Account's JSON key file (including the `-----BEGIN PRIVATE KEY-----` and `-----END PRIVATE KEY-----` lines).



**Advanced options**

  * **Feed Name** : A prepopulated value that identifies the feed.
  * **Asset Namespace** : Namespace associated with the feed.
  * **Ingestion Labels** : Labels applied to all events from this feed.


  1. Click **Create feed**.

**Note:** The Content Hub is not available on the SIEM standalone platform. To upgrade, contact your Google SecOps representative.

For more information about configuring multiple feeds for different log types within this product family, see [Configure feeds by product](https://docs.cloud.google.com/chronicle/docs/ingestion/ingestion-entities/configure-multiple-feeds).

## Alternate Method: Ingestion via Cloud Storage

  1. Sign in to the [Google Cloud console](https://console.cloud.google.com/).
  2. Go to the **Cloud Storage Buckets** page.

[Go to Buckets](https://console.cloud.google.com/storage/browser)

  3. Click **Create**.

  4. On the **Create a bucket** page, enter your bucket information. After each of the following steps, click **Continue** to proceed to the next step:

     1. In the **Get started** section, do the following:

        1. Enter a unique name that meets the bucket name requirements; for example, **gcp-cloudidentity-users-logs**.
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

     4. In the **Choose how to control access to objects** section, clear **Enforce public access prevention** , and select an **Access control** model for your bucket's objects.

**Note:** If public access prevention is already enforced by your project's organization policy, the **Enforce public access prevention on this bucket** checkbox is locked.
     5. In the **Choose how to protect object data** section, do the following:

        1. Select any of the options under **Data protection** that you want to set for your bucket.
        2. To choose how your object data will be encrypted, click the expander arrow labeled **Data encryption** , and select a data encryption method.
  5. Click **Create**.


**Note:** Be sure to provide your Google SecOps service account with permissions to Read or Read & Write to the newly created bucket.

### Configure Cloud Identity Device Users logs export

  1. Sign in to the [Google Cloud console](https://console.cloud.google.com/).
  2. Go to **Logging > Log Router**.
  3. Click **Create Sink**.
  4. Provide the following configuration parameters:

     * **Sink Name** : enter a meaningful name; for example, `Cloudidentity-Users-Sink`.
     * **Sink Destination** : select **Cloud Storage Storage** and enter the URI for your bucket; for example, `gs://gcp-cloudidentity-users-logs/`.
     * **Log Filter** :
           
           logName="projects/<your-project-id>/logs/cloudaudit.googleapis.com%2Factivity"
           resource.type="cloud_identity_user"
           

     * **Set Export Options** : include all log entries.

  5. Click **Create**.




### Configure permissions for Cloud Storage

  1. Go to **IAM & Admin > IAM**.
  2. Locate the **Cloud Logging** service account.
  3. Grant the **roles/storage.admin** on the bucket.



## UDM Mapping Table

Log Field | UDM Mapping | Logic  
---|---|---  
collection_time.nanos | timestamp.nanos | Directly mapped from the log field. Represents the event timestamp in nanoseconds.  
collection_time.seconds | timestamp.seconds | Directly mapped from the log field. Represents the event timestamp in seconds.  
createTime | entity.metadata.creation_timestamp | Directly mapped from the log field after being parsed by the `date` filter. Represents the creation timestamp of the user.  
managementState | entity.additional.fields.value.string_value | Directly mapped from the log field. Represents the management state of the user.  
name | entity.entity.resource.name | Directly mapped from the log field. Represents the full resource name of the device user.  
passwordState | entity.additional.fields.value.string_value | Directly mapped from the log field. Represents the password state of the user. This field is only mapped if the `passwordState` field exists in the raw log.  
userEmail | entity.entity.user.email_addresses | Directly mapped from the log field. Represents the email address of the user.  
| entity.additional.fields.key | Set to a constant value `Management State` within the parser. This field is used to provide context to the `managementState` value.  
| entity.additional.fields.key | Set to a constant value `Password State` within the parser. This field is used to provide context to the `passwordState` value and is only present if `passwordState` exists in the raw log.  
| entity.entity.user.product_object_id | Extracted from the `name` field using the `grok` filter, capturing the `deviceuser_id` portion. Represents the unique identifier of the device user.  
| entity.metadata.collected_timestamp.nanos | Copied from `collection_time.nanos`. Represents the timestamp when the log was collected.  
| entity.metadata.collected_timestamp.seconds | Copied from `collection_time.seconds`. Represents the timestamp when the log was collected.  
| entity.metadata.entity_type | Set to a constant value `USER` within the parser.  
| entity.metadata.product_name | Set to a constant value `GCP Cloud Identity Device Users` within the parser.  
| entity.metadata.vendor_name | Set to a constant value `Google Cloud Platform` within the parser.  
| relations.entity.asset.product_object_id | Extracted from the `name` field using the `grok` filter, capturing the `device_id` portion. Represents the unique identifier of the device.  
| relations.entity_type | Set to a constant value `ASSET` within the parser.  
| relations.relationship | Set to a constant value `MEMBER` within the parser.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-cloudidentity-deviceusers-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
