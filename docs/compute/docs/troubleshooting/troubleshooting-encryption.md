---
url: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-encryption/
title: Troubleshooting disk encryption \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:32.944061+00:00
---

# Troubleshooting disk encryption  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-encryption/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Troubleshooting disk encryption Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to resolve issues with [disk encryption](https://docs.cloud.google.com/compute/docs/disks/disk-encryption).

## Key rotation errors

This section lists the errors that you might encounter when [rotating a customer-managed encryption key](https://docs.cloud.google.com/compute/docs/disks/customer-managed-encryption#rotate_encryption) (CMEK) and provides suggestions for how to fix them.

### CMEK rotation is not supported for non-CMEK protected disks

The following error occurs when you try to [rotate a CMEK](https://docs.cloud.google.com/compute/docs/disks/customer-managed-encryption#rotate_encryption) on an unsupported resource:
    
    
    CMEK rotation is not supported for non-CMEK protected disks
    

To resolve this issue, confirm that your resource is protected using [Cloud Key Management Service](https://docs.cloud.google.com/kms/docs/view-key-usage).

### CMEK rotation is not supported for some Google Cloud Hyperdisk configurations

The following error message occurs when you try to rotate or change the CMEK for an online Confidential Hyperdisk volume, or an online Hyperdisk volume that isn't attached to one of the [supported machine types](https://docs.cloud.google.com/compute/docs/disks/customer-managed-encryption#limitations):
    
    
    CMEK Rotation is not supported for (confidential) Hyperdisk attached to machine type TYPE_X
    

To workaround this issue, complete the following steps:

  1. Detach the disk
  2. Rotate or change the CMEK using the [`compute.disks.updateKmsKey` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/updateKmsKey)
  3. Re-attach the disk



### Disk is already using the primary key version

The following warning message occurs when a disk or standard snapshot already uses the primary key version:
    
    
    WARNING: Some requests generated warnings:
     - Disk DISK_NAME is already using the primary kms key version KEY_VERSION.
    

In this scenario, the API call will succeed but the key version won't update.

This issue might occur due to a delay in the versioning update from KMS. To resolve this issue, re-attempt rotating the key at a later time.

If the task fails but you don't see the previous error message, you can manually rotate your Cloud KMS using the following steps:

  1. [Rotate your Cloud KMS key](https://docs.cloud.google.com/kms/docs/rotating-keys).
  2. [Create a snapshot of the encrypted disk](https://docs.cloud.google.com/compute/docs/disks/customer-managed-encryption#create_snapshot).
  3. Use the new snapshot to [create a new disk](https://docs.cloud.google.com/compute/docs/disks/customer-managed-encryption#create-disk-from-encrypted-snapshot) with the key rotated in the preceding step.
  4. Replace the disk attached to your VM that uses the old encryption key.



When you create the new disk, it uses the new key version for encryption. Any snapshots that you create from that disk use the latest primary key version.

When you rotate a key using Cloud Key Management Service, data that was encrypted with previous key versions is not automatically re-encrypted. For more information, see [Re-encrypting data](https://docs.cloud.google.com/kms/docs/re-encrypt-data). Rotating a key does not automatically [disable](https://docs.cloud.google.com/kms/docs/enable-disable) or [destroy](https://docs.cloud.google.com/kms/docs/destroy-restore) an existing key version.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
