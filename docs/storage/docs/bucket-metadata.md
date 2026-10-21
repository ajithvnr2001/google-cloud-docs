---
url: https://docs.cloud.google.com/storage/docs/bucket-metadata/
title: Bucket metadata \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:52:22.723379+00:00
---

# Bucket metadata  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/bucket-metadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Bucket metadata Stay organized with collections  Save and categorize content based on your preferences. 

The metadata for a Cloud Storage bucket identifies the bucket's properties and lets you control how the bucket behaves. A bucket's metadata includes non-editable fields such as the bucket name and project number, as well as configurable settings like the default storage class, lifecycle rules, and IAM roles.

## Overview of bucket metadata

Metadata is stored as `key: value` pairs, where the `value` can take a variety of forms, including strings, arrays, or even nested `key:value` pairs. For example, the bucket name is a string, while a bucket Object Lifecycle Management configuration is an array of rules in which each rule contains several child `key: value` pairs.

The mutability of metadata varies:

  * Some metadata is read-only.

  * Some metadata can be set when the bucket is [created](https://docs.cloud.google.com/storage/docs/creating-buckets), but can't be edited or removed.

  * Some metadata can be added and edited, but can't be removed.

  * Some metadata can be added, edited, and removed at any time.




## Non-editable metadata

The following metadata is set during bucket creation, and cannot be edited or removed:

  * [Bucket name](https://docs.cloud.google.com/storage/docs/buckets#naming)

  * The [project](https://docs.cloud.google.com/storage/docs/projects) the bucket is a part of

  * Generation number

    * A bucket's generation number uniquely identifies the version of the bucket even if more than one version of a bucket share the same name.

    * A bucket's generation value never changes.

    * There is no guarantee that generation numbers increase for successive versions, only that each new version has a unique generation number.

    * There is no relationship between generation numbers of unrelated buckets.

  * Metageneration number

    * A bucket's metageneration number uniquely identifies the metadata state of the bucket. The metageneration number is `1` at the time of bucket creation and increases each time you modify the bucket's metadata.
  * Whether [hierarchical namespace](https://docs.cloud.google.com/storage/docs/hns-overview) is enabled for the bucket




## Editable metadata

Editable bucket metadata is metadata whose values you can typically modify at any time. In some cases, such as the bucket being subject to an [organization policy constraint](https://docs.cloud.google.com/storage/docs/org-policy-constraints), there are restrictions on modifying certain metadata values.

Metadata overview | Link to guide | Notes  
---|---|---  
[Access Control Lists (ACLs)](https://docs.cloud.google.com/storage/docs/access-control/lists) | [Create and managing ACLs](https://docs.cloud.google.com/storage/docs/access-control/create-manage-lists) | Recommended only for XML users.  
[Default ACLs](https://docs.cloud.google.com/storage/docs/access-control/lists#default) | [Set default object ACLs](https://docs.cloud.google.com/storage/docs/access-control/create-manage-lists#defaultobjects) |   
[Identity and Access Management (IAM) policies](https://docs.cloud.google.com/storage/docs/access-control/iam)1 | [Use IAM permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions) |   
[Billing (Requester Pays)](https://docs.cloud.google.com/storage/docs/requester-pays) | [Use Requester Pays](https://docs.cloud.google.com/storage/docs/using-requester-pays) |   
[Cross-origin resource sharing (CORS) configuration](https://docs.cloud.google.com/storage/docs/cross-origin) | [Set up and view CORS configurations](https://docs.cloud.google.com/storage/docs/using-cors) |   
[Default storage class](https://docs.cloud.google.com/storage/docs/storage-classes) | [Change the default storage class](https://docs.cloud.google.com/storage/docs/changing-default-storage-class) | Set during bucket creation and can be edited, but not removed.  
[Data encryption](https://docs.cloud.google.com/storage/docs/encryption) | [Configure which encryption methods are allowed or restricted](https://docs.cloud.google.com/storage/docs/encryption/enforce-encryption-types) | Updating this setting doesn't affect the encryption type of any objects that already exist in the bucket.  
[Default Cloud KMS encryption key](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys) | [Use default Cloud KMS keys](https://docs.cloud.google.com/storage/docs/encryption/using-customer-managed-keys#use-default-keys) |   
[Default event-based holds](https://docs.cloud.google.com/storage/docs/object-holds#default-holds)1 | [Work with the default event-based hold property](https://docs.cloud.google.com/storage/docs/holding-objects#use-default-hold) |   
[Public access prevention](https://docs.cloud.google.com/storage/docs/public-access-prevention)1 | [Use public access prevention](https://docs.cloud.google.com/storage/docs/using-public-access-prevention) |   
[Uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access)1 | [Use uniform bucket-level access](https://docs.cloud.google.com/storage/docs/using-uniform-bucket-level-access) | Only editable for the first 90 days after you enable uniform bucket-level access on a bucket.  
[Lifecycle configuration policy](https://docs.cloud.google.com/storage/docs/lifecycle) | [Manage object lifecycles](https://docs.cloud.google.com/storage/docs/managing-lifecycles) |   
[Autoclass](https://docs.cloud.google.com/storage/docs/autoclass) | [Use Autoclass](https://docs.cloud.google.com/storage/docs/using-autoclass) |   
[Turbo replication](https://docs.cloud.google.com/storage/docs/availability-durability#turbo-replication)1 | [Manage turbo replication](https://docs.cloud.google.com/storage/docs/managing-turbo-replication) |   
Usage logs and storage logs | [Usage logs configuration](https://docs.cloud.google.com/storage/docs/access-logs) |   
[Bucket Lock](https://docs.cloud.google.com/storage/docs/bucket-lock)2 | [Use and locking retention policies](https://docs.cloud.google.com/storage/docs/using-bucket-lock) | Only editable if you don't lock the retention policy.  
[Object Retention Lock](https://docs.cloud.google.com/storage/docs/object-lock) | [Enable and use object retention configurations](https://docs.cloud.google.com/storage/docs/using-object-lock) | Once enabled for a bucket, cannot be disabled.  
[Object Versioning configuration](https://docs.cloud.google.com/storage/docs/object-versioning) | [Use Object Versioning](https://docs.cloud.google.com/storage/docs/using-object-versioning) |   
[Bucket labels](https://docs.cloud.google.com/storage/docs/tags-and-labels) | [Use bucket labels](https://docs.cloud.google.com/storage/docs/using-bucket-labels) |   
[Soft delete retention duration](https://docs.cloud.google.com/storage/docs/soft-delete) | [Use soft delete](https://docs.cloud.google.com/storage/docs/use-soft-delete) |   
Website configuration | [Assign specialty pages for static websites](https://docs.cloud.google.com/storage/docs/hosting-static-website#specialty-pages) |   
[Bucket location](https://docs.cloud.google.com/storage/docs/locations) | [Relocate buckets](https://docs.cloud.google.com/storage/docs/bucket-relocation/relocate-buckets) | Before you relocate a bucket, review the [Bucket relocation overview](https://docs.cloud.google.com/storage/docs/bucket-relocation/overview) page.  
  
1 This metadata cannot be viewed or managed using the XML API.

2 You can use the XML API to set this metadata during bucket creation, but not to view or manage this metadata.

## What's next

  * Learn how to [view bucket metadata](https://docs.cloud.google.com/storage/docs/getting-bucket-metadata).
  * Learn how to [get bucket size](https://docs.cloud.google.com/storage/docs/getting-bucket-size).
  * Learn more about [buckets](https://docs.cloud.google.com/storage/docs/buckets).
  * Read more about [object metadata](https://docs.cloud.google.com/storage/docs/metadata).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
