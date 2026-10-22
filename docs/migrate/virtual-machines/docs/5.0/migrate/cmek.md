---
url: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/cmek/
title: Use Customer-managed encryption keys (CMEK) with Migrate to Virtual Machines \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:17:36.936156+00:00
---

# Use Customer-managed encryption keys (CMEK) with Migrate to Virtual Machines  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/cmek/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Virtual Machines ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0)
  * [ Guides ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/lifecycle)



Send feedback 

#  Use Customer-managed encryption keys (CMEK) with Migrate to Virtual Machines Stay organized with collections  Save and categorize content based on your preferences. 

By default, Migrate to Virtual Machines encrypts customer content at rest. Migrate to Virtual Machines handles encryption for you without any additional actions on your part. This option is called _Google default encryption_. 

If you want to control your encryption keys, then you can use customer-managed encryption keys (CMEKs) in [Cloud KMS](https://docs.cloud.google.com/kms/docs) with CMEK-integrated services including Migrate to Virtual Machines. Using Cloud KMS keys gives you control over their protection level, location, rotation schedule, usage and access permissions, and cryptographic boundaries. Using Cloud KMS also lets you [track key usage](https://docs.cloud.google.com/kms/docs/view-key-usage), view audit logs, and control key lifecycles. Instead of Google owning and managing the symmetric [key encryption keys (KEKs)](https://docs.cloud.google.com/kms/docs/envelope-encryption#key_encryption_keys) that protect your data, you control and manage these keys in Cloud KMS.

After you set up your resources with CMEKs, the experience of accessing your Migrate to Virtual Machines resources is similar to using Google default encryption. For more information about your encryption options, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek).

Migrate to Virtual Machines uses CMEK to encrypt the following data:

  * Data stored internally during a migration
  * Data on target Virtual Machine (VM) instances and VM disks
  * Data on target disks and machine images



The following sections describe these scenarios is more detail.

## Use CMEK to encrypt data stored during a migration

To encrypt data stored during a migration or import using CMEK, you must provide a reference to a Cloud KMS key when creating a migration source or import resource respectively. For instructions on using CMEK to encrypt data during a migration from various migration sources, see the following topics:

  * [Migration from an AWS source](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/how-to/create-an-aws-source#create_an_aws_source)
  * [Migration from an Azure source](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/how-to/create-an-azure-source#create-an-azure-source)
  * [Migration from a VMware source](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/how-to/migrate-connector#register)
  * [Import virtual disk images](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/image_import)
  * [Import machine images](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/machine-image-import)



## Use CMEK to encrypt data on target VM instances and VM disks

To encrypt data on target VM instances and VM disks using CMEK, you must provide a reference to a Cloud KMS key in the target details. For instructions on setting CMEK in the target details, see [setting CMEK for VM instances](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/how-to/migrating-vms#configure-target) and [setting CMEK for VM disks](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/how-to/migrating-disks#configure-target).

## Use CMEK to encrypt data on target disks and machine images

To encrypt data on target disks and machine images using CMEK, you must provide a reference to a Cloud KMS key in the target details. For instructions on setting CMEK in the target details, see [Import a virtual disk image to Compute Engine](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/image_import#import-disk) and [Import a machine image to Compute Engine](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/machine-image-import).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
