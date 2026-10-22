---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/cmek/
title: Overview of Customer-managed encryption keys (CMEK) with Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:42.179867+00:00
---

# Overview of Customer-managed encryption keys (CMEK) with Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/cmek/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Overview of Customer-managed encryption keys (CMEK) with Backup and DR Stay organized with collections  Save and categorize content based on your preferences. 

By default, Google Cloud automatically encrypts data at rest using encryption keys managed by Google. If you have specific compliance or regulatory requirements related to the keys that protect your data, you can use [customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek).

With CMEK, you can protect your Backup and DR data using a cryptographic key that you control through Cloud Key Management Service. When you use CMEK, you manage the key in Cloud Key Management Service and control access by managing Identity and Access Management permissions on the key. If you temporarily disable or permanently destroy the CMEK, the data protected by that key becomes inaccessible.

## How Backup and DR uses CMEK

Backup and DR protects backups using CMEK in one of two ways, depending on the workload type:

  * **Vault-level CMEK** : uses the Cloud Key Management Service key configured directly on the backup vault to encrypt the backup data.

  * **Source-level CMEK** : inherits and uses the encryption key of the source workload, preserving its existing CMEK protection.




## Configuring a Backup vault container with CMEK

A **backup vault** is a secure, isolated logical container used to store and manage your backups. When you configure a backup vault with a CMEK, Backup and DR uses that key to protect the backups stored inside the vault.

For some resource types, a CMEK-enabled backup vault encrypts backup data using the vault's Cloud Key Management Service key.

For example, if one or more disks attached to a Compute Engine instance use CMEK, Backup and DR considers the instance CMEK-protected. You must back up such instances to a CMEK-enabled backup vault. If all disks attached to the instance use Google-managed encryption, then in the Google Cloud console, you must store backups in a non-CMEK backup vault. However, if you use the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), API, or Terraform, you can configure backups for an instance with Google-managed encryption to use a CMEK-enabled backup vault. When you store a backup in a CMEK-enabled backup vault, the vault's Cloud Key Management Service key encrypts the backup data, regardless of the instance's disk encryption status.

## Inherited settings

Backups inherit either the source workload key or uses the backup vault's CMEK to protect backups using CMEK depending on the resource type.

## Encryption using the source resource CMEK

For workload types that don't allow backups to use a different key from the source workload, Backup and DR preserves the source resource's encryption by using the source workload's own encryption key to protect backups.

This applies to the following workload types:

  * **Compute Engine disk and Persistent Disk backups** : If the source workloads use CMEK, their backups also use the same CMEK. If they use Google-managed encryption, their backups also use Google-managed encryption. You must store these backups in a backup vault that is not configured with CMEK.

  * **Cloud SQL instance backups** : Backup and DR uses the original database instance's key to encrypt the backup.




To perform these operations and access the source resource's Cloud Key Management Service key, Backup and DR uses its service agent. You must grant the service agent the necessary IAM permissions on the source key.

## Encryption key types used per workload type

The following table summarizes which encryption key is used for backups of different workload types:

Workload | Encryption key used for backup | CMEK support status  
---|---|---  
Compute Engine instance | Backup vault CMEK | Supported  
Compute Engine disk | The source disk encryption key | Supported  
Cloud SQL | The source instance's encryption key | Supported  
AlloyDB cluster | Backup vault CMEK key | Supported. Support for CMEK encryption of both GMEK-encrypted AlloyDB clusters and CMEK-encrypted AlloyDB clusters is provided by enhanced backup protection through Backup and DR.  
Filestore instance | Backup vault CMEK | Supported  
Google Cloud VMware Engine, Oracle database, and SQL Server database | - | Not supported  
  
### Considerations for using CMEK for Filestore

For enhanced backups, Backup and DR uses the backup vault CMEK using the Backup and DR service agent to encrypt the backup in the backup vault.

**Caution:** Disabling, deleting, or modifying permissions for a CMEK used by active Filestore backup chains makes those backups permanently unrestorable.

## Limitations

Backup and DR support for CMEK has the following limitations:

  * CMEK protection is only supported for Compute Engine instances, Persistent Disk, Filestore workloads, Cloud SQL, and AlloyDB cluster backups stored in backup vaults.

  * You can configure CMEK on a backup vault only at creation time.

  * You cannot enable, disable, or change CMEK on an existing backup vault.

  * The Cloud Key Management Service key must be in the same location as the backup vault. A backup vault in a region must use a key from the same region. A multi-regional backup vault must use a key from the same multi-region.

  * Cross-region backups must use a key from the same region as the backup vault.

  * Cross-region restores of CMEK-protected Compute Engine instances are only supported through the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), API or Terraform. For instructions, see [Restoring from a CMEK-enabled backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/compute-instance-restore#cross-region-cmek).

  * Backup and DR doesn't support customer-supplied encryption keys (CSEK).

  * The default backup vault and default backup plan use Google-managed encryption. To use CMEK, you must create a new backup vault and explicitly enable CMEK.




## Key revocation and enhanced backups

For enhanced backups, the source workload and the backup vault use different service agents to access the CMEK.

  * **Cloud SQL service agent** : if you revoke access to the CMEK from the Cloud SQL service agent, the source instance becomes suspended.

  * **Backup and DR service agent** : existing enhanced backups remain restorable as long as the Backup and DR service agent retains access to the CMEK. Revoking access from the Backup and DR service agent prevents new backups from being created and prevents existing backups from being restored.


**Note:** Backup and DR proactively blocks backup plan association (BPA) creation if the Backup and DR service agent (P4SA) of the vault project does not have permissions on the backup vault's CMEK key. Furthermore, because decryption permissions are anchored to the Backup and DR service agent (P4SA) in the vault project, backups can be restored even if the original workload project is deleted.

## Pricing

Backup and DR does not charge any additional fees for using CMEK. However, you are charged for the use of your keys in Cloud Key Management Service. For more information, see [Cloud Key Management Service pricing](https://docs.cloud.google.com/kms/pricing).

## What's next

  * Learn how to [use CMEK with Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/set-up-cmek)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
