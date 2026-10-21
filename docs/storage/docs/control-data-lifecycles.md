---
url: https://docs.cloud.google.com/storage/docs/control-data-lifecycles/
title: Options for controlling data lifecycles \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:05.384104+00:00
---

# Options for controlling data lifecycles  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/control-data-lifecycles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Options for controlling data lifecycles Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Storage has features that help manage your objects' [storage classes](https://docs.cloud.google.com/storage/docs/storage-classes):

  * [**Object Lifecycle Management**](https://docs.cloud.google.com/storage/docs/lifecycle) can be configured for a bucket to give you more automated control over moving objects to colder storage classes. When you define a lifecycle configuration, Cloud Storage performs a specified action, such as setting a colder storage class for an object, only if the object meets your criteria.

  * [**Autoclass**](https://docs.cloud.google.com/storage/docs/autoclass) can be enabled on a bucket, which lets Cloud Storage manage the storage classes of objects in the bucket automatically.




If you are concerned that your application software or users might erroneously delete or replace objects at some point, Cloud Storage also has features that help you protect your data:

  * [**Soft delete**](https://docs.cloud.google.com/storage/docs/soft-delete) provides default bucket-level protection for your data from accidental or malicious deletion by preserving all recently deleted objects for a specified period of time. You can restore the deleted objects within this duration. For more information on how to restore soft-deleted objects, see [Use soft-deleted objects](https://docs.cloud.google.com/storage/docs/use-soft-deleted-objects).

  * [**Bucket Lock**](https://docs.cloud.google.com/storage/docs/bucket-lock): A retention policy that specifies a retention period can be [placed on a bucket](https://docs.cloud.google.com/storage/docs/using-bucket-lock#set-policy). Each object in the bucket must reach the specified age before it can be deleted or replaced.

  * [**Object Retention Lock**](https://docs.cloud.google.com/storage/docs/object-lock): A retention configuration that specifies a retain-until date and time can be [set for an individual object](https://docs.cloud.google.com/storage/docs/using-object-lock). The object cannot be deleted or replaced until after the specified date and time.

  * An [**object hold**](https://docs.cloud.google.com/storage/docs/object-holds) can be [placed on individual objects](https://docs.cloud.google.com/storage/docs/holding-objects#set-object-hold) to prevent anyone from deleting or replacing the object until the hold is removed.

  * [**Object Versioning**](https://docs.cloud.google.com/storage/docs/object-versioning) can be enabled on a bucket in order to retain older versions of objects. When the _live_ version of an object is deleted or replaced, it becomes _noncurrent_ if versioning is enabled on the bucket. If you accidentally delete a live object version, you can [restore the noncurrent version](https://docs.cloud.google.com/storage/docs/using-versioned-objects#restore) of it back to the live version.

**Caution:** Object Versioning **does not** protect your data if you [delete the entire bucket](https://docs.cloud.google.com/storage/docs/deleting-buckets).

Object Versioning increases storage costs, but this can be partially mitigated by configuring Object Lifecycle Management to delete older object versions. For one possible setup, see the lifecycle configuration example for [deleting objects](https://docs.cloud.google.com/storage/docs/lifecycle-configurations#deletion-example).

  * [**Object Lifecycle Management**](https://docs.cloud.google.com/storage/docs/lifecycle) can be configured for a bucket to give you more automated control over deleting objects. When you define a lifecycle configuration, Cloud Storage performs a specified action, such as deleting an object, only if the object meets your criteria.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
