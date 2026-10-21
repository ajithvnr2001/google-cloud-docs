---
url: https://docs.cloud.google.com/compute/docs/disks/disk-encryption/
title: About disk encryption \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:18:32.397499+00:00
---

# About disk encryption  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/disk-encryption/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  About disk encryption Stay organized with collections  Save and categorize content based on your preferences. 

By default, Compute Engine [encrypts customer content at rest](https://docs.cloud.google.com/docs/security/encryption/default-encryption). Compute Engine automatically uses Google-owned and Google-managed encryption keys to encrypt your data.

However, you can customize the encryption Compute Engine uses for your resources by providing [key encryption keys (KEKs)](https://docs.cloud.google.com/docs/security/encryption/default-encryption#key_management). Key encryption keys don't directly encrypt your data, but encrypt the Google-owned and managed keys that Compute Engine uses to encrypt your data.

To provide key encryption keys, choose one of the following options:

  * **Recommended**. Use customer-managed encryption keys (CMEKs) in [Cloud KMS](https://docs.cloud.google.com/kms/docs) with Compute Engine. Using Cloud KMS keys gives you control over their protection level, location, rotation schedule, usage and access permissions, and cryptographic boundaries. Using Cloud KMS also lets you [track key usage](https://docs.cloud.google.com/kms/docs/view-key-usage), view audit logs, and control key life cycles. Instead of Google owning and managing the symmetric [key encryption keys (KEKs)](https://docs.cloud.google.com/kms/docs/envelope-encryption#key_encryption_keys) that protect your data, you control and manage these keys in Cloud KMS.

You can create CMEKs manually, or you can use Cloud KMS Autokey to have them created automatically on your behalf.

In most cases, after you create a CMEK-encrypted disk, you don't need to specify the key when working with the disk.

  * **([Deprecated](https://docs.cloud.google.com/compute/docs/deprecations))**. You can manage your own key encryption keys outside of Compute Engine, and provide the key whenever you create or manage a disk.

This option is known as _customer-supplied encryption keys_ (CSEKs). When you manage CSEK-encrypted resources, you must always specify the key you used when encrypting the resource.


**Caution:** Customer-supplied encryption keys (CSEK) for Compute Engine are [deprecated](https://docs.cloud.google.com/compute/docs/deprecations). For more information and instructions on alternatives, see [CSEK deprecation in Compute Engine](https://docs.cloud.google.com/compute/docs/deprecations/csek-deprecation-in-compute-engine). 

For more information about each encryption type, see [Customer-managed encryption keys](https://docs.cloud.google.com/kms/docs/cmek) and [Customer-supplied encryption keys](https://docs.cloud.google.com/docs/security/encryption/customer-supplied-encryption-keys).

To add an additional layer of security to your Hyperdisk Balanced disks, enable Confidential mode. Confidential mode adds hardware-based encryption to your Hyperdisk Balanced disks.

## Supported disk types

This section lists the supported encryption types for disks and other storage options offered by Compute Engine.

  * [Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/persistent-disks) volumes support Google-owned and managed keys, CMEKs and CSEKs.

  * [Google Cloud Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks) support CMEKs and Google-owned and managed keys. You can't use CSEKs to encrypt Hyperdisks.

  * [Local SSD disks](https://docs.cloud.google.com/compute/docs/disks#localssds) only support Google-owned and managed keys. You can't use CSEKs or CMEKs to encrypt Local SSD disks.

  * [Disk clones](https://docs.cloud.google.com/compute/docs/disks/create-disk-from-source#create-clone) and [machine images](https://docs.cloud.google.com/compute/docs/machine-images) support Google-owned and managed keys,CMEKs, and CSEKs.

  * [Standard snapshots](https://docs.cloud.google.com/compute/docs/disks/snapshots) and [instant snapshots](https://docs.cloud.google.com/compute/docs/disks/instant-snapshots) support Google-owned and managed keys, CMEKs, and CSEKs.




## Rotation for Google-owned and managed keys and CMEKs

Compute Engine rotates the Google-owned and managed keys used to protect your data on a yearly basis. Key rotation is an industry best practice for data security that limits the potential impact of a compromised key.

If you use CMEKs, Google recommends that you enable [automatic rotation](https://docs.cloud.google.com/kms/docs/rotate-key#automatic) for your resources.

For more information on rotating your keys, see [Rotate your Cloud KMS encryption key for a disk or standard snapshot](https://docs.cloud.google.com/compute/docs/disks/customer-managed-encryption#rotate_encryption).

## CMEK with Cloud KMS Autokey

If you choose to use Cloud KMS keys to protect your Compute Engine resources, you can either create CMEKs manually or use Cloud KMS Autokey to create the keys. With Autokey, key rings and keys are generated on demand as part of resource creation in Compute Engine. Service agents that use the keys for encrypt and decrypt operations are created if they don't already exist and are granted the required Identity and Access Management (IAM) roles. For more information, see [Autokey overview](https://docs.cloud.google.com/kms/docs/autokey-overview).

To learn how to use CMEKs created by Cloud KMS Autokey to protect your Compute Engine resources, see [Using Autokey with Compute Engine resources](https://docs.cloud.google.com/kms/docs/create-resource-with-autokey#compute-autokey).

### Snapshots

When using Autokey to create keys to protect your Compute Engine resources, Autokey doesn't create new keys for snapshots. You must encrypt a snapshot with the same key used to encrypt the source disk. If you create a snapshot using the Google Cloud console, the encryption key used by the disk is automatically applied to the snapshot. If you create a snapshot using the gcloud CLI, Terraform, or the Compute Engine API, you must get the resource identifier of the key used to encrypt the disk and then use that key to encrypt the snapshot.

## Encrypt disks with customer-managed encryption keys

For more information about how to use manually-created customer-managed encryption keys (CMEK) to encrypt disks and other Compute Engine resources, see [Protect resources by using Cloud Key Management Service keys](https://docs.cloud.google.com/compute/docs/disks/customer-managed-encryption).

## Encrypt disks with customer-supplied encryption keys

**Caution:** Customer-supplied encryption keys (CSEK) for Compute Engine are [deprecated](https://docs.cloud.google.com/compute/docs/deprecations). For more information and instructions on alternatives, see [CSEK deprecation in Compute Engine](https://docs.cloud.google.com/compute/docs/deprecations/csek-deprecation-in-compute-engine). 

To learn how to use customer-supplied encryption keys (CSEK) to encrypt disks and other Compute Engine resources, see [Encrypting disks with customer-supplied encryption keys](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption).

## Encrypting disks for Windows VMs with BitLocker

Google-owned and managed keys and CMEKs encrypt data at the volume layer. To add a second, independent layer of encryption to your disks, you can use an operating system-level encryption tool such as [BitLocker](https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/) for Windows. BitLocker is managed by the Windows operating system (OS) and Google doesn't have access to or manage the BitLocker keys.

**Warning:** If you lose access to your BitLocker keys, Google can't recover the keys and your data is unrecoverable until you recover the BitLocker keys. Therefore, to prevent data loss, implement a regionally redundant storage solution for your BitLocker keys. You should also make sure that your encryption never starts unless the recovery keys are stored in [Active Directory](https://docs.cloud.google.com/managed-microsoft-ad/docs).

For more information, see [Best practices for securing Windows VMs with BitLocker](https://docs.cloud.google.com/compute/docs/instances/windows/windows-best-practices#best-practices-bitlocker).

## View a disk's encryption type

To view a disk's encryption type, follow the steps in [View information about a disk's encryption](https://docs.cloud.google.com/compute/docs/disks/view-disk-details#view-encryption).

## Confidential mode for Hyperdisk Balanced

If you use [Confidential Computing](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview), you can extend the hardware-based encryption to your Hyperdisk Balanced volumes by enabling Confidential mode.

Confidential mode for your Hyperdisk Balanced volumes lets you enable additional security without having to refactor the application. Confidential mode is a property that you can specify when you create a new Hyperdisk Balanced volume.

Hyperdisk Balanced volumes in Confidential mode can only be used with Confidential VMs.

To create a Hyperdisk Balanced volume in Confidential mode, follow the steps in [Create a Hyperdisk Balanced volume in Confidential mode](https://docs.cloud.google.com/compute/docs/disks/customer-managed-encryption#encrypt_a_new_hd_confidential).

### Supported machine types for Hyperdisk Balanced volumes in Confidential mode

Hyperdisk Balanced volumes in Confidential mode can only be used with Confidential VMs that use the [N2D machine type](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n2d_machines).

### Supported regions for Hyperdisk Balanced volumes in Confidential mode

Confidential mode for Hyperdisk Balanced volumes is available in the following regions:

  * `europe-west4`
  * `us-central1`
  * `us-east4`
  * `us-east5`
  * `us-south1`
  * `us-west4`



### Limitations for Hyperdisk Balanced volumes in Confidential mode

  * Hyperdisk Extreme, Hyperdisk Throughput, Hyperdisk ML, and Hyperdisk Balanced High Availability don't support Confidential mode.
  * You can't suspend or resume a VM that uses Hyperdisk Balanced volumes in Confidential mode.
  * You can't use Hyperdisk Storage Pools with Hyperdisk Balanced volumes in Confidential mode.
  * You can't create a machine image or a custom image from a Hyperdisk Balanced volume in Confidential mode.



## What's next

  * To learn how to automate the creation of CMEKs, see [Cloud KMS with Autokey](https://docs.cloud.google.com/kms/docs/kms-autokey) ([Preview](https://cloud.google.com/products/#product-launch-stages)).
  * To learn how to create CMEKs, see [Create encryption keys with Cloud KMS](https://docs.cloud.google.com/kms/docs/create-encryption-keys).
  * Encrypt a disk with [customer-managed encryption keys (CMEKs)](https://docs.cloud.google.com/compute/docs/disks/customer-managed-encryption#encrypt_a_new_persistent_disk_with_cmek).
  * To create a Hyperdisk Balanced volume in Confidential mode, see [Create a Hyperdisk Balanced volume in Confidential mode](https://docs.cloud.google.com/compute/docs/disks/customer-managed-encryption#encrypt_a_new_hd_confidential).
  * Learn more [about the format and specification for CSEKs](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption#specifications).
  * To learn how guest-side Windows encryption interacts with Shielded VM, see [Using BitLocker with Shielded VM images](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#using-bitlocker).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
