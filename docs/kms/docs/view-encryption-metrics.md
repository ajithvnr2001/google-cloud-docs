---
url: https://docs.cloud.google.com/kms/docs/view-encryption-metrics/
title: View encryption metrics \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:24:21.307999+00:00
---

# View encryption metrics  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/view-encryption-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Guides ](https://docs.cloud.google.com/kms/docs/key-management-service)



Send feedback 

#  View encryption metrics Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Key Management Service (Cloud KMS) displays metrics about the encryption keys that protect your data at rest. These metrics show how your resources are protected and whether your keys align with recommended practices. The metrics focus mostly on customer-managed encryption keys (CMEKs) used to protect resources in CMEK-integrated services. This guide shows you how to view your project's encryption metrics and helps you understand what they mean for your organization's security posture.

**Important:** Throughout this document, **resources** refers to [resources in CMEK-integrated services that support key usage tracking](https://docs.cloud.google.com/kms/docs/view-key-usage#tracked-resource-types). For example, "a key that doesn't protect any resources" is a key that isn't used as a CMEK to protect a trackable resource. Such a key might protect other data, including customer data in non-trackable resources in a CMEK-integrated service or data in a custom application.

For more information about recommended practices for using CMEKs to protect your resources in Google Cloud, see [Recommended practices for using CMEKs](https://docs.cloud.google.com/kms/docs/cmek-recommended-practices).

## Before you begin

  1. To get the permissions that you need to view encryption metrics, ask your administrator to grant you the following IAM roles on project or a parent resource: 

     * [Cloud KMS Encryption Dashboard Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms#cloudkms.encryptionDashboardViewer) (`roles/cloudkms.encryptionDashboardViewer`)
     * To view CMEK coverage details: [Cloud Asset Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudasset#cloudasset.viewer) (`roles/cloudasset.viewer`) 

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  2. If your organization uses a centralized key management model, with keys stored in a shared key project protecting resources in other projects, then you must grant the **Cloud KMS Organization Service Agent** role to the [Cloud KMS Organization Service Agent](https://docs.cloud.google.com/iam/docs/service-agents#cloud-kms-organization-service-agent):
         
         gcloud organizations add-iam-policy-binding ORGANIZATION_ID \
             --member=serviceAccount:service-org-ORGANIZATION_ID@gcp-sa-cloudkms.iam.gserviceaccount.com \
             --role=roles/cloudkms.orgServiceAgent
           

If you skip this step, the **Encryption metrics** dashboard might display incomplete information. For example, when you view encryption metrics for PROJECT_A, resources in PROJECT_B that are protected by a key in PROJECT_A wouldn't be included in the metrics.




## View encryption metrics

To view encryption metrics, follow these steps:

  1. In the Google Cloud console, go to the **Key Management** page.

[Go to Key Management](https://console.cloud.google.com/security/kms)

  2. Click the **Overview** tab, and then click **Encryption metrics**.

  3. Use the project picker to select a project. The dashboard shows the following encryption metrics for resources and keys in that project:

     * The **Resources in this project by protection type** and **Resource protection type by service** charts show CMEK coverage summary metrics.
     * The **Alignment to key usage recommended practices** chart shows key alignment summary metrics; you can also view key alignment details.
  4. Optional: To see a list of keys in each category, click the section that you want to view keys for. To filter the list of keys, enter your search terms in the filter_list **Filter** box and then press enter.




## View key alignment details

To view a list of keys in the project and see which recommended practices they are aligned with, follow these steps:

  1. On the **Encryption metrics** page, locate the **Alignment to key usage recommended practices** chart.

  2. Optional: To focus only on keys created by Cloud KMS Autokey, click the **Cloud KMS (Autokey)** tab. To focus only on keys created manually, click the **Cloud KMS (Manual)** tab.

  3. To view a list of keys and see whether they are aligned with each recommended practice, click the section that represents the category, and then click **View**.

The **Alignment to key usage recommended practices** page lists Cloud KMS keys in the selected project and shows whether each is **Aligned** or **Not aligned** with each recommendation. To learn more about what it means for a key to be **Aligned** or **Not aligned** for a recommendation, see Key alignment in this document.

  4. Optional: To filter the list of keys, enter your search terms in the filter_list **Filter** box and then press enter. For example, you can filter the list to only show keys that are **Aligned** with the **Granularity** recommendation.




## Understand encryption metrics

The encryption metrics dashboard uses the Cloud Asset Inventory service to gather information about your resources and Cloud KMS keys. The dashboard calculates metrics on demand using the latest available data.

The dashboard shows two main categories of metrics: CMEK coverage and key alignment. Both metrics show a summary view with aggregated information and a detailed view with a tabular list of resources or keys.

### CMEK coverage

CMEK coverage metrics in the **Resources in this project by protection type** and **Resource protection type by service** charts show how many of your resources are protected by CMEKs. This metric looks at resources for which CMEK integration and Cloud KMS key tracking are supported. Resources are grouped into the following categories:

  * **Google Managed Encryption** : resources protected by Google default encryption.
  * **Cloud KMS (Manual)** : resources protected by a CMEK that you create and manage manually.
  * **Cloud KMS (Autokey)** : resources protected by a CMEK provisioned and assigned by Cloud KMS Autokey.



CMEK coverage metrics are shown for the project as a whole and broken down by the service associated with each of the protected resources. You can use this information to assess how many of the resources in the selected project are using Google default encryption when they could use CMEKs.

For a list of supported resource types, see [Tracked resource types](https://docs.cloud.google.com/kms/docs/view-key-usage#tracked-resource-types).

### Key alignment

Key alignment metrics in the **Alignment to key usage recommended practices** chart show whether your Cloud KMS keys align with the following recommended security practices:

  * **Rotation period** : the key has an appropriate rotation period set.
  * **Granularity** : the key protects resources that are in one project and belong to one service.
  * **Separation of duties** : only service accounts have permission to encrypt and decrypt with the key.
  * **Location** : the key only protects resources that are in the same cloud location.



Key alignment metrics include all Cloud KMS symmetric encryption keys in the selected project, even if they aren't used to protect resources in a CMEK-integrated service. These metrics are assessed for keys, not key versions. For example, a key with no active key versions can still show as **Aligned** for any or all of these recommended practices.

The following sections provide more information about each of these practices.

#### Granularity

Key _granularity_ refers to the scale and scope of a key's intended usage. Keys can be highly granular, protecting only a single resource, or they can be less granular, protecting many resources. Using keys that are less granular increases the potential impact of security incidents including unauthorized access and accidental data loss.

In general, we recommend that each key is used as follows:

  * Used for a single Google Cloud project.
  * Used in a single location—for example, `us-central1`.
  * Used in a single service or product—for example, BigQuery.
  * Wherever possible, used for a single resource—for example, a single Cloud Storage bucket.



For most organizations, this strategy provides a good balance between the overhead of maintaining many highly granular keys and the potential risks of using less granular keys that are shared between many projects, services, or resources.

Keys created with Cloud KMS Autokey follow this recommendation.

Each key in your project is considered **Aligned** with this recommendation if the resources that it protects are all located within the same location, service, and project. A key is considered **Not aligned** with this recommendation if the resources that it protect are located in two or more locations, services, or projects.

If your keys are not aligned with this recommendation, consider whether adjusting your key granularity strategy is right for your organization. For more information about recommended practices for key granularity, see [Choose a key granularity strategy](https://docs.cloud.google.com/kms/docs/cmek-recommended-practices#granularity).

#### Location

In most cases, Cloud KMS keys used with CMEK-integrated services are required to be in the exact same Google Cloud region or multi-region where the resources they protect are located. However, a few services allow exceptions to this rule.

Each key in your project is considered **Aligned** with this recommendation if the resources that it protects are all located within the same location as the key—for example, a key in `us-central1` that protects resources in `us-central1`. Regional keys can protect zonal resources within the same region—for example, a key in `us-central1` that protects resources in `us-central1a`.

A key is considered **Not aligned** with this recommendation if it protects a resource in a different region or multi-region—for example, a key in the `us` multi-region that protects a Compute Engine disk in the `us-central1` region.

If your keys are not aligned with this recommendation, consider moving or replacing your resources or keys so that they are in the same location. For more information about locations, see [Cloud KMS locations](https://docs.cloud.google.com/kms/docs/locations).

#### Rotation

Rotating your keys regularly is an important aspect of information security. For example, some standards require you to rotate your keys on a certain schedule. Keys that protect sensitive workloads may need to be rotated more frequently. Cloud KMS lets you set up automatic key rotation for your keys to help ensure that your chosen schedule is followed.

Each key in your project is considered **Aligned** with this recommendation if it has a rotation schedule set. A key is considered **Not aligned** if it is not set up for automatic key rotation.

To enable automatic rotation, you can do any of the following:

  * [Manually create a new key with a custom rotation schedule](https://docs.cloud.google.com/kms/docs/create-key#rotation).
  * [Use Cloud KMS Autokey when you create a new resource](https://docs.cloud.google.com/kms/docs/create-resource-with-autokey). Keys created by Cloud KMS Autokey have a default rotation period of one year, but the rotation period can be changed after the key is created.
  * [Update an existing key to add a rotation schedule](https://docs.cloud.google.com/kms/docs/rotate-key#update-existing).



#### Separation of duties

Separation of duties is a security practice that aims to avoid giving users or other principals too many permissions. In the context of Cloud KMS and CMEK integrations, this means that the users who maintain your Cloud KMS keys shouldn't have permissions to use those keys, and the principals that use the keys to encrypt and decrypt your resources don't have other permissions on the keys.

Each key in your project is considered **Aligned** with this recommendation if both of the following are true:

  * The service account for the protected resource is the only principal with the `cloudkms.cryptoKeyVersions.useToEncrypt` and `cloudkms.cryptoKeyVersions.useToDecrypt` permissions on the key.
  * The service account for the protected resource doesn't have a role that grants key administration permissions on the key, including `roles/cloudkms.admin`, `roles/editor`, and `roles/owner`.



A key is considered **Not aligned** if the service account has administration permissions or another principal has encryption or decryption permissions.

If your keys are not aligned with this recommendation, review the IAM roles and permissions on your keys and other Cloud KMS resources and remove role and permission grants that are not needed. For more information about Cloud KMS roles and the permissions that they include, see [Permissions and roles](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles). For more information about viewing and removing IAM roles on Cloud KMS resources, see [Access control with IAM](https://docs.cloud.google.com/kms/docs/iam).

### Limitations

The **Encryption metrics** dashboard has the following limitations:

  * The dashboard shows metrics for one project at a time.
  * The dashboard has a limit of 10,000 resources or keys per project. If your project contains more than 10,000 keys or if the keys in your project protect more than 10,000 resources, only partial metrics are shown.
  * The dashboard relies on data from the [Cloud Asset Inventory service](https://docs.cloud.google.com/asset-inventory/docs/asset-inventory-overview). If any of the data in the Cloud Asset Inventory is out of date, the dashboard may show inaccurate or incomplete information.
  * The dashboard only considers symmetric keys for key alignment and CMEK coverage.
  * The dashboard only considers [resources that support key usage tracking](https://docs.cloud.google.com/kms/docs/view-key-usage#tracked-resource-types).
  * The key alignment metrics don't distinguish between keys that are in active use as CMEKs protecting trackable resources, keys that are in active use for other use cases, and keys that have no active key versions. For example, your key alignment data might include keys that are used for custom applications.
  * When key alignment data includes keys that protect non-trackable resources and custom applications, alignment details for these keys might not be accurate. For example, a key that is used in multiple custom applications across multiple projects might show as **Aligned** with the key granularity recommendations even though it isn't.



## What's next

  * Learn more about [key usage tracking](https://docs.cloud.google.com/kms/docs/view-key-usage).
  * Learn more about [recommended practices for customer-managed encryption keys](https://docs.cloud.google.com/kms/docs/cmek-recommended-practices).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
