---
url: https://docs.cloud.google.com/storage-transfer/docs/hns/
title: Transfer Cloud Storage hierarchical namespace buckets \u00a0|\u00a0 Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:36:40.776576+00:00
---

# Transfer Cloud Storage hierarchical namespace buckets  |  Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/hns/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)



Send feedback 

#  Transfer Cloud Storage hierarchical namespace buckets Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Storage hierarchical namespace stores data in a logical file system structure, using folders to organize objects. For details, see [Hierarchical namespace](https://docs.cloud.google.com/storage/docs/hns-overview).

Storage Transfer Service can transfer to and from Cloud Storage buckets that use hierarchical namespace. To successfully transfer the folders and folder metadata, additional permissions must be granted to the Storage Transfer Service service agent.

**Note:** Cross-bucket replication is not supported for hierarchical namespace buckets.

## Required permissions

In addition to the standard permissions required for a transfer, the Storage Transfer Service service agent must be granted the following IAM permissions.

When the source is a hierarchical namespace bucket:

  * `storage.folders.list` on the source bucket. This permission is included in the Storage Object Viewer (`roles/storage.objectViewer`) role that is [required for all transfers](https://docs.cloud.google.com/storage-transfer/docs/iam-cloud#manually_assigning_roles). No additional role is required.



When the destination is a hierarchical namespace bucket:

  * `storage.folders.create` on the destination bucket. This permission is included in the Storage Object User (`roles/storage.objectUser`) role. Grant this role in addition to the roles listed in [Agentless transfer permissions](https://docs.cloud.google.com/storage-transfer/docs/iam-cloud#manually_assigning_roles).



For instructions on adding roles to the service agent, see:

  * [Configure access to a source: Cloud Storage](https://docs.cloud.google.com/storage-transfer/docs/source-cloud-storage#grant_the_required_permissions)
  * [Configure access to a sink: Cloud Storage](https://docs.cloud.google.com/storage-transfer/docs/sink-cloud-storage#grant_the_required_permissions)



## Transfer behavior

When transferring between two hierarchical namespace buckets:

  * Objects and object metadata are transferred.
  * Folders and folder metadata are transferred.
  * Deletion of folders at source or sink is not supported.



When transferring from a hierarchical namespace bucket to a flat namespace bucket:

  * Objects and object metadata are transferred.
  * Folders are transferred as object prefixes. For example, `object1` in `folderA` is transferred to the destination as `folderA/object1`.
  * Folder metadata is not transferred.
  * Deletion of folders at source is not supported.



When transferring from a flat namespace bucket to a hierarchical namespace bucket:

  * Objects and object metadata are transferred.
  * Object prefixes are used to create any missing folders. For example, when transferring `folderA/object1`, Storage Transfer Service creates a new folder called `folderA` and transfers `object1` into that folder.
  * Deletion of folders at sink is not supported.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
