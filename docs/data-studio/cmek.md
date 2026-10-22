---
url: https://docs.cloud.google.com/data-studio/cmek/
title: Customer-managed encryption keys (CMEK) \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:36.053889+00:00
---

# Customer-managed encryption keys (CMEK)  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/cmek/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Customer-managed encryption keys (CMEK) Stay organized with collections  Save and categorize content based on your preferences. 

**Data Studio Pro feature**

The features and functionality described in this page are available to Data Studio Pro users.

[Get Data Studio Pro.](https://docs.cloud.google.com/data-studio/about-pro)

By default, Data Studio encrypts customer content at rest. Data Studio handles encryption for you without any additional actions on your part. This option is called _Google default encryption_. 

If you want to control your encryption keys, then you can use customer-managed encryption keys (CMEKs) in [Cloud KMS](https://docs.cloud.google.com/kms/docs) with CMEK-integrated services including Data Studio. Using Cloud KMS keys gives you control over their protection level, location, rotation schedule, usage and access permissions, and cryptographic boundaries. Using Cloud KMS also lets you view audit logs and control key lifecycles. Instead of Google owning and managing the symmetric [key encryption keys (KEKs)](https://docs.cloud.google.com/kms/docs/envelope-encryption#key_encryption_keys) that protect your data, you control and manage these keys in Cloud KMS.

After you set up your resources with CMEKs, the experience of accessing your Data Studio resources is similar to using Google default encryption. For more information about your encryption options, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek).

With CMEK, you can use your own cryptographic keys for encrypting Data Studio Pro data at rest. Using CMEK gives you additional control over your data and helps you meet internal or external compliance regulations.

## CMEK and customer-managed storage

If you enable CMEK, you must also enable Data Studio Pro's customer-managed storage option, which lets you use Cloud Storage and BigQuery to store data in the Data Studio Pro Google Cloud project. Data Studio Pro uses your Cloud Key Management Service keys to protect resources such as report and data source configurations and scheduled emails. For data extracts and file uploads that are stored in your Google Cloud project, you can protect your data by applying CMEK to your Google Cloud storage resources.

## Before you begin

In order to enable and use CMEK, you must meet the following prerequisites:

  * You can enable CMEK only when you create a new Data Studio Pro subscription.
  * To enable CMEK, you must also enable and configure [customer-managed storage](https://docs.cloud.google.com/data-studio/cms). For customer-managed storage, you must provide a Cloud Storage bucket and a BigQuery dataset within your Google Cloud project for Data Studio Pro to use for storing data extracts and file uploads. To protect data that's stored within these resources, you can apply CMEK configurations to them.
  * To enable CMEK, you must also enable and configure a [data location](https://docs.cloud.google.com/data-studio/data-residency.).
  * You must have a symmetric encryption key in Cloud KMS to use for CMEK. This key must be in the same region that you select for data location.
  * You must have the necessary IAM roles to create keys in Cloud KMS. For more information, see [Required roles](https://docs.cloud.google.com/kms/docs/cmek#required-roles).



## Enable CMEK for a subscription

You can only enable CMEK when creating a new Data Studio Pro subscription. You cannot enable CMEK for an existing Pro subscription.

To enable CMEK, follow these steps when you [create a new Data Studio Pro subscription](https://docs.cloud.google.com/data-studio/start-a-new-pro-subscription):

  1. When prompted, select **Use a customer-managed encryption key**.
  2. Enter or paste the key resource name into the **Key resource name** field.
  3. Grant the Data Studio Pro service account that is shown in the user interface the **Cloud KMS CryptoKey Encrypter/Decrypter** role in Cloud KMS.
  4. Click **Next** to continue with subscription setup.



## What is encrypted with CMEK

When you enable CMEK for your Data Studio Pro subscription, encryption of customer content is handled in two ways:

  * **Data that is encrypted by Data Studio Pro using your Cloud KMS key:** Data Studio Pro uses your specified key to encrypt data such as report and data source configurations and scheduled emails.
  * **Data that is stored in your Google Cloud project:** Enabling CMEK requires you to use customer-managed storage. The following data types are stored in Cloud Storage and BigQuery resources that you provide: 
    * Data extracts
    * CSV and Excel file uploads These resources are encrypted using any CMEK configurations that you apply to them in Cloud Storage and BigQuery. Data Studio Pro does not automatically apply CMEK to these resources when you enable CMEK for your subscription.



## Key management

As a security or compliance administrator, you can perform key management tasks using Cloud KMS. Data Studio Pro calls Cloud KMS for all encryption and decryption operations.

You can perform the following key management tasks:

  * **Key revocation:** You can revoke Data Studio Pro's access to a key to make your data immediately unavailable.
  * **Auditing:** You can inspect key access logs in Cloud KMS to audit every operation where your keys were used to encrypt or decrypt data.



### Key rotation

When you rotate your key, Cloud KMS creates a new version of the key that is used to encrypt new assets. Existing assets are not re-encrypted and continue to be protected by the key version with which they were encrypted. Data Studio Pro does not support re-encrypting existing assets with the new key version.

Because previous key versions are still required to access existing assets that were encrypted with them, you shouldn't delete or disable previous key versions unless your goal is to permanently remove access to those assets. Deleting or disabling a key version that is protecting data will make that data inaccessible.

If your CMEK key becomes unavailable—for example, if you disable or delete the key—Data Studio Pro will return error messages instead of displaying reports or data sources that use the encrypted data. Any data kept in memory is deleted within 15 minutes of detecting a disabled key. The Data Studio homepage remains accessible because it does not contain customer content.

## Cloud KMS quotas and Data Studio

When you use CMEK in Data Studio, your projects can consume Cloud KMS cryptographic requests quotas. Each time Data Studio Pro uses one of your keys to encrypt or decrypt data, that operation counts toward your project's quota.

Encryption and decryption operations using CMEK keys affect Cloud KMS quotas in these ways:

  * For software CMEK keys generated in Cloud KMS, no Cloud KMS quota is consumed.
  * For hardware CMEK keys—sometimes called Cloud HSM keys—encryption and decryption operations count against [Cloud HSM quotas](https://docs.cloud.google.com/kms/quotas#hsm) in the project that contains the key.
  * For external CMEK keys—sometimes called Cloud EKM keys—encryption and decryption operations count against [Cloud EKM quotas](https://docs.cloud.google.com/kms/quotas#ekm) in the project that contains the key.



For more information, see [Cloud KMS quotas](https://docs.cloud.google.com/kms/quotas).

## Enforce CMEK with organization policies

Data Studio Pro supports organization policies that let you control encryption settings across your organization.

You can use the following constraints to manage CMEK:

  * **`constraints/gcp.restrictNonCmekServices`** : Requires the use of CMEK for all new Data Studio Pro subscriptions. To enforce this, add `datastudio.googleapis.com` to the deny list for this constraint.
  * **`constraints/gcp.restrictCmekCryptoKeyProjects`** : Restricts which Google Cloud projects can supply Cloud KMS keys for Data Studio Pro. To configure this, add the allowed projects to the allow list for this constraint (for example, `under:projects/ALLOWED_PROJECT_ID`).



For instructions on configuring these policies, see [Enforce CMEK with organization policies](https://docs.cloud.google.com/kms/docs/cmek-org-policy).

## Limitations of CMEK

CMEK has the following limitations:

  * You can enable CMEK only when you create a new Data Studio Pro subscription. You cannot enable or disable CMEK for an existing subscription.
  * You can move content from a CMEK-enabled project only to another project that has an active Data Studio Pro subscription.
  * If you downgrade from Data Studio Pro to the no-cost version of Data Studio, or if your subscription is canceled, CMEK features will continue to work for a 30-day grace period. After that, data sources that were created using CMEK will be deleted.
  * If you downgrade from Data Studio Pro to the no-cost version of Data Studio, or if your subscription is canceled, you must wait 30 days before you can reuse the same Google Cloud project to create a new Data Studio Pro subscription.



## What's next

  * Learn more about [CMEK](https://docs.cloud.google.com/kms/docs/cmek).
  * Learn more about [Cloud KMS](https://docs.cloud.google.com/kms/docs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
