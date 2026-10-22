---
url: https://docs.cloud.google.com/alloydb/docs/cmek/
title: About CMEK \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:48.923347+00:00
---

# About CMEK  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/cmek/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  About CMEK Stay organized with collections  Save and categorize content based on your preferences. 

This page describes customer-managed encryption keys (CMEK) for AlloyDB for PostgreSQL.

For more information about CMEK in general, including when and why to enable this feature, see the [Cloud KMS documentation](https://docs.cloud.google.com/kms/docs/cmek).

By default, AlloyDB for PostgreSQL encrypts customer content at rest. AlloyDB handles encryption for you without any additional actions on your part. This option is called _Google default encryption_. 

If you want to control your encryption keys, then you can use customer-managed encryption keys (CMEKs) in [Cloud KMS](https://docs.cloud.google.com/kms/docs) with CMEK-integrated services including AlloyDB. Using Cloud KMS keys gives you control over their protection level, location, rotation schedule, usage and access permissions, and cryptographic boundaries. Using Cloud KMS also lets you view audit logs and control key lifecycles. Instead of Google owning and managing the symmetric [key encryption keys (KEKs)](https://docs.cloud.google.com/kms/docs/envelope-encryption#key_encryption_keys) that protect your data, you control and manage these keys in Cloud KMS.

After you set up your resources with CMEKs, the experience of accessing your AlloyDB resources is similar to using Google default encryption. For more information about your encryption options, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek).

To learn how to use manually created CMEKs to protect your AlloyDB resources, see [Use CMEK](https://docs.cloud.google.com/alloydb/docs/use-cmek).

## CMEK with Cloud KMS Autokey

You can either create CMEKs manually to protect your AlloyDB resources or use Cloud KMS Autokey. With Autokey, key rings and keys are generated on demand to support resource creation in AlloyDB. Service agents that use the keys for encrypt and decrypt operations are created if they don't already exist and are granted the required Identity and Access Management (IAM) roles. For more information, see [Autokey overview](https://docs.cloud.google.com/kms/docs/autokey-overview).

AlloyDB is only compatible with Cloud KMS Autokey when creating resources using Terraform or the REST API.

## A self-managed alternative to Google-managed encryption

By default, all data at rest in Google Cloud, including the data in AlloyDB, is protected using Google-managed [default encryption](https://docs.cloud.google.com/docs/security/encryption/default-encryption). Google Cloud handles and manages this default encryption for you without any additional actions on your part.

If you have specific compliance or regulatory requirements related to the keys that protect your data, you can use CMEK instead. With CMEK, your AlloyDB cluster is protected using a key that you control and manage in [Cloud Key Management Service (KMS)](https://docs.cloud.google.com/kms). You can choose the [protection level](https://docs.cloud.google.com/kms/docs/protection-levels) of your key.

## Features

  * **Data access control:** Administrators can rotate, manage access to, and disable or destroy the key that you used to protect data at rest in AlloyDB.

Key management is handled by [Cloud KMS](https://docs.cloud.google.com/kms/docs/cmek). Clusters don't automatically re-encrypt themselves with the newer key version after rotation. Clusters are encrypted by the primary version of the CMEK at the time of cluster creation. To rotate cluster encryption, create a backup and restore the cluster with newer key version. For more information, see [Data backup and recovery overview](https://docs.cloud.google.com/alloydb/docs/backup/overview).

  * **Auditability:** If you [enable audit logging](https://docs.cloud.google.com/logging/docs/audit/configure-data-access#config-console-enable) for Cloud KMS API in your project, all actions on the key, including those performed by AlloyDB, are logged and viewable in [Cloud Logging](https://docs.cloud.google.com/logging/docs/view/logs-explorer-summary).

  * **Performance:** Using CMEK introduces no changes to AlloyDB performance.




## Pricing

AlloyDB bills for a CMEK-enabled cluster just like any other cluster; there are no additional AlloyDB costs. For more information, see [AlloyDB for PostgreSQL pricing](https://cloud.google.com/alloydb/pricing).

You are billed by Cloud KMS for the cost of the key and for encryption and decryption operations when AlloyDB uses the key. For more information, see [Cloud Key Management Service pricing](https://cloud.google.com/kms/pricing).

## What is protected with CMEK

AlloyDB uses your Cloud KMS key to protect _data at rest_ in the following ways:

  * If you enable CMEK on a cluster, then AlloyDB uses your key to encrypt all of your cluster's data in storage.
  * If you specify a CMEK configuration when [creating an on-demand backup](https://docs.cloud.google.com/alloydb/docs/backup/create-on-demand), then AlloyDB uses your key to encrypt that backup.
  * If you enable CMEK with your cluster's [continuous or automated backup configuration](https://docs.cloud.google.com/alloydb/docs/backup/configure), then AlloyDB uses your key to encrypt your ongoing backups.

**Note:** If you don't provide a continuous or automated backup encryption configuration, AlloyDB uses the cluster encryption configuration.



Whether you use a Google-owned and Google-managed encryption keys or CMEK, AlloyDB has three layers of encryption:

  1. AlloyDB breaks data at rest into chunks for storage, and encrypts each chunk with an individual encryption key. The key that it uses to encrypt the data in a chunk is called a data encryption key (DEK).

Because of the high volume of keys at Google, and the need for low latency and high availability, AlloyDB stores each DEK near the data that it encrypts.

  2. AlloyDB encrypts each DEK with a key encryption key (KEK) that's held by the cluster.

  3. Finally, AlloyDB encrypts the KEK with your cluster's Cloud Key Management Service-based encryption key, which is either a Google-owned and Google-managed encryption key or a CMEK key.




You can also [view the key versions](https://docs.cloud.google.com/alloydb/docs/use-cmek#view-cluster) that are being used to protect a cluster.

## Enable CMEK

To allow an AlloyDB cluster to use CMEK, you must specify the Cloud KMS key at the time of [cluster creation](https://docs.cloud.google.com/alloydb/docs/use-cmek#create-db).

AlloyDB is able to access the key on your behalf after you grant the [Cloud KMS CryptoKey Encrypter/Decrypter](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#predefined) (`roles/cloudkms.cryptoKeyEncrypterDecrypter`) role to a [AlloyDB service agent](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents).

For detailed instructions, refer to [Use CMEK](https://docs.cloud.google.com/alloydb/docs/use-cmek).

## Manage keys

Use Cloud KMS for all key-management operations. AlloyDB cannot detect or act upon any key changes until they are propagated by Cloud KMS. Some operations, such as disabling or destroying a key, can take [up to three hours to propagate](https://docs.cloud.google.com/kms/docs/consistency); changes to permissions usually propagate much faster.

After the cluster is created, AlloyDB calls Cloud KMS about every five minutes to make sure that the key is still valid.

If AlloyDB detects that your Cloud KMS key has been disabled or destroyed, an operation to make your cluster's data inaccessible begins immediately. If AlloyDB's calls to Cloud KMS detect that a formerly disabled key has been re-enabled, it restores access automatically.

## Use and manage external keys

As an alternative to using keys that reside on Cloud KMS, you can use keys residing with a [supported external key management partner](https://docs.cloud.google.com/kms/docs/ekm#supported_partners). To do this, use Cloud External Key Manager (Cloud EKM) to create and manage _external keys_ , which are pointers to keys that reside outside of Google Cloud. For more information, see [Cloud External Key Manager](https://docs.cloud.google.com/kms/docs/ekm).

After you create an external key with Cloud EKM, you can apply it to a new AlloyDB cluster by providing the ID of that key when [creating the cluster](https://docs.cloud.google.com/alloydb/docs/cluster-create). This procedure is the same as applying a Cloud KMS key to a new cluster.

You can use Key Access Justifications as part of Cloud EKM. Key Access Justifications lets you view the reason for each Cloud EKM request. Additionally, based on the justification provided, you can automatically approve or deny a request. For more information, see [Overview](https://docs.cloud.google.com/assured-workloads/key-access-justifications/docs/overview).

Google lacks control over the availability of keys in an external key management partner system.

**Caution:** If an external key is deleted or cannot be recovered, any AlloyDB clusters encrypted with that key become permanently inaccessible.

## Key unavailability

**Caution:** If a Cloud KMS key is deleted, any AlloyDB clusters encrypted with that key become permanently inaccessible.

If you disable the Cloud KMS key that is used to encrypt an AlloyDB cluster, AlloyDB instances belonging to that cluster will experience downtime within 30 minutes. Re-enabling the key brings the instances back up.

In infrequent scenarios, such as during periods when Cloud KMS is unavailable, AlloyDB might be unable to retrieve the status of your key from Cloud KMS. In this scenario, AlloyDB continues to support full cluster operations on a best-effort basis for a period of up to 30 minutes to minimize the impact of any temporary outages on your workload.

After 30 minutes, if AlloyDB is still unable to connect with Cloud KMS, AlloyDB begins taking the cluster offline as a protective measure. The data in your AlloyDB cluster remains inaccessible until your cluster can reconnect with Cloud KMS and Cloud KMS responds that the key is active.

## Backups and restoration

AlloyDB also protects [backups](https://docs.cloud.google.com/alloydb/docs/backup/overview) with either CMEK or the default Google-managed encryption. If a backup is CMEK-enabled, it is encrypted using the primary version of the KMS key at the time of backup creation. After a backup is created, its key and key version cannot be modified, even if the KMS key is rotated. For more information, see [Backing up a cluster](https://docs.cloud.google.com/alloydb/docs/use-cmek#backup).

When you [restore](https://docs.cloud.google.com/alloydb/docs/backup/restore) a cluster from a backup, the restored cluster defaults to using Google-managed encryption, but you can specify a CMEK key to use instead. To restore a CMEK-enabled backup, both the key and key version that was used to encrypt the backup must be available.

## Logging

You can audit the requests that AlloyDB sends to Cloud KMS on your behalf in Cloud Logging, if you have [enabled audit logging](https://docs.cloud.google.com/logging/docs/audit/configure-data-access#config-console-enable) for the Cloud KMS API in your project. These [Cloud KMS log entries](https://docs.cloud.google.com/kms/docs/audit-logging) are visible in [Cloud Logging](https://docs.cloud.google.com/logging/docs/view/logs-explorer-summary). For more information, see [Viewing audit logs for a Cloud KMS key](https://docs.cloud.google.com/alloydb/docs/use-cmek#viewing_audit_logs_for_a_key).

## What's next

  * [Use CMEK](https://docs.cloud.google.com/alloydb/docs/use-cmek)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
