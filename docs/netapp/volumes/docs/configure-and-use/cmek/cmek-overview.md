---
url: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/cmek/cmek-overview/
title: Manage customer-managed encryption key policies \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:17:32.261391+00:00
---

# Manage customer-managed encryption key policies  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/cmek/cmek-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Manage customer-managed encryption key policies Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the use of customer-managed encryption keys (CMEK) to manage Google Cloud NetApp Volumes.

## About CMEK

NetApp Volumes always encrypts your data with volume-specific keys. NetApp Volumes always encrypts your data at rest.

With CMEK, Cloud Key Management Service wraps your stored volume keys. This feature gives you greater control over the encryption keys you use and the added security of storing the keys on a system or in a location different from the data. NetApp Volumes supports Cloud Key Management Service capabilities such as hardware security modules, and the full key management lifecycle of generate, use, rotate, and destroy.

NetApp Volumes supports one CMEK policy per region. A CMEK policy attaches to a storage pool and all volumes created in that pool use it. You can have a mix of storage pools with and without CMEK policies in a region. If you have pools without CMEK in a specific region, you can convert them to CMEK by using the migration action of a region's CMEK policy.

The use of CMEK is optional. If used, CMEK policies are region-specific. You can only configure one policy per region.

ONTAP-mode storage pools also use CMEK policies. You can't configure different key managers in ONTAP-mode.

## Considerations

The following sections include limitations for CMEK to consider.

### Key management

Using CMEK makes you solely responsible for your keys and your data.

**Important:** When you destroy or deactivate configured Cloud KMS keys, it prevents you from creating or accessing volumes, backups, and their data. Neither Google nor NetApp can help you to recover the volume data if this happens.

### Cloud KMS configurations

CMEK uses symmetric keys for encryption and decryption. After all volumes are deleted in a region for a project, the Cloud KMS configuration returns to a `Ready` created state. It's used again when you create the next volume in that region.

### Regional key rings

NetApp Volumes only supports regional KMS key rings and they need to reside in the same region as the CMEK policy.

### Service level

CMEK supports the Flex Unified, Flex File, Standard, Premium, and Extreme service levels storage pools.

### VPC Service Controls

For more information about using VPC Service Controls, see [Configure VPC Service Controls ingress rule for CMEK](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/cmek/verify-key-access#configure-vpc-service-controls-ingress-rule-for-cmek).

## CMEK organization policy

The CMEK [organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview) for NetApp Volumes gives organizations control over data encryption keys and restricts which keys can be used for CMEK. This is achieved by enforcing CMEK usage for encrypting data at rest in new storage pools and backup vaults and allowing organizations to manage encryption keys using Cloud KMS. The organization policy is enforced at storage pool and backup vault creation and doesn't affect existing storage pools and backup vaults.

Organization policies allow [administrators](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints#add-org-policy-admin) to apply and enforce consistent [constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) across all projects and resources. This is important for organizations that manage multiple projects and resources to enforce standardized policies.

There are two types of organization policy constraints that can be applied to CMEK:

  * **Restrict Non-CMEK Services** : lets you specify which services within an organization, project, or folder can be configured without CMEK. If you add a service to the deny list or exclude it in the allow list, then resources for that service will require CMEK. By default, this constraint allows the creation of non-CMEK resources.

  * **Restrict CMEK CryptoKey Projects** : lets you define which projects can provide [KMS keys](https://docs.cloud.google.com/kms/docs/object-hierarchy#key) for [CMEK](https://docs.cloud.google.com/kms/docs/using-other-products) when configuring resources within the organization, project, or folder. If this constraint is set, only KMS keys from the specified projects can be used for CMEK protected resources. If the constraint is not set, CryptoKeys from any project can be used.




For more information about how to apply an organization policy, see [Apply a CMEK organization policy](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/cmek/apply-CMEK-organization-policy).

## CMEK options

NetApp Volumes offers support for CMEKs, which can be stored as software keys, hardware keys within an [HSM cluster](https://docs.cloud.google.com/kms/docs/hsm), or as external keys stored in [Cloud External Key Manager (Cloud EKM)](https://docs.cloud.google.com/kms/docs/ekm).

For more information, see [Cloud Key Management Service](https://docs.cloud.google.com/kms/docs/key-management-service#cmek).

### Operational impact of key errors

A disabled Cloud KMS key or an inaccessible external key used in a CMEK policy can affect resources and operations for NetApp Volumes and backup vaults associated with that policy.

External keys are managed by a third-party, and Google Cloud isn't responsible for key availability.

#### Volumes

If the [External Key Manager (EKM)](https://docs.cloud.google.com/kms/docs/ekm#terminology) notifies [Cloud Key Management Service](https://docs.cloud.google.com/kms/docs/key-management-service) that an external key is unreachable, volumes using that key are taken offline, which prevents read and write operations. The same outcome occurs if a Cloud KMS key is disabled.

#### Backup vaults

**Note:** The CMEK backup feature is generally available (GA) for the Standard, Premium, Extreme, and Flex Unified service levels.

For backup vaults that use CMEK, you must ensure the availability of the key or keys that the backup vault references. When you rotate a key, the system performs a re-encryption operation on the backup vault using the new primary key. Until this operation completes, the rotated key must be available to the backup vault. If you delete the rotated key, you can't recover the backups that point to it. If the rotated key is unreachable or disabled, restores fail until the key is reachable or enabled.

If the primary key is disabled, unreachable, or destroyed, ongoing encryption operations fail. If you can't recover the primary key, you can't recover all encrypted backups that point to the key. The backup vault doesn't initiate new backup operations.

The backup vault's status includes details about the CMEK and the encryption status.

Users also receive an error with details about the key's current state if any of the following operations are attempted while EKM is unreachable or the Cloud KMS key is disabled in either source or destination regions for replication:

  * [Create a storage pool](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/storage-pools/create-storage-pool)

  * [Create a volume](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/create-volume)

  * [Create a snapshot](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volume-snapshots/create-manual-snapshots)

  * [Create a backup](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/create-backup)

  * [Mount a volume](https://docs.cloud.google.com/netapp/volumes/docs/get-started/quickstarts/mount-volume#mount_your_volume_on_a_client)

  * [Create a volume replication](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/create-volume-replication)

  * [Delete a snapshot](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volume-snapshots/delete-snapshot)

  * [Resume a replication](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/stop-or-resume-replication#resume_a_replication)

  * [Reverse and resume a replication](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/reverse-and-resume-replication)




## What's next

[Create a CMEK policy](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/cmek/create-cmek-policy).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
