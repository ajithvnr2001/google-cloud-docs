---
url: https://docs.cloud.google.com/storage/docs/soft-delete/
title: Soft delete overview \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:36.468724+00:00
---

# Soft delete overview  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/soft-delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Soft delete overview Stay organized with collections  Save and categorize content based on your preferences. 

[Setup](https://docs.cloud.google.com/storage/docs/use-soft-delete) [Usage](https://docs.cloud.google.com/storage/docs/use-soft-deleted-objects)

Soft delete helps protect your Cloud Storage data in case an object or bucket is accidentally or maliciously deleted. The soft delete feature preserves objects and buckets that get deleted or overwritten by retaining them in a soft-deleted state for a specified period of time. During this time, the object or bucket can't be permanently deleted and can be restored.

Soft delete is enabled by default for all buckets that support it, with a default retention duration of 7 days. You can [set a different default retention duration by using tags](https://docs.cloud.google.com/storage/docs/use-tags-for-soft-delete).

This page describes how soft delete works.

**Caution:** If a bucket primarily contains temporary data, enabling soft delete can result in significantly increased storage costs. To learn how to mitigate soft delete costs for such buckets, see Reduce costs for temporary objects.

## Soft delete policies

When soft delete is enabled on a bucket, deleting the bucket or the objects within the bucket results in the resource entering a soft-deleted state instead of being permanently deleted. To enable soft delete on a bucket, you set a soft delete policy that defines how long soft-deleted resources are retained.

Soft delete policies work in the following ways:

  * The soft delete policy includes a retention duration that defines how long soft-deleted resources are retained before being permanently deleted. The default retention duration is 7 days and you can customize the retention duration to anywhere between 7 to 90 days. To disable soft delete, you set the retention duration to 0.

  * A default soft delete policy is automatically set on all newly created buckets, except for buckets that use products or capabilities that are incompatible with soft delete (such as zonal buckets that use [Rapid Bucket](https://docs.cloud.google.com/storage/docs/rapid/rapid-bucket)).

  * You can set, edit, or disable a soft delete policy when you create or update a bucket.

When you edit a soft delete policy, the changes you make only apply to resources that are deleted after the new policy takes effect. Resources that were deleted prior to the new policy taking effect are retained for the original retention duration that was in effect when the resource got deleted. In other words, existing soft-deleted resources continue to adhere to the retention period that was active at their time of deletion.

For example, say you set a soft delete policy on a bucket that has a retention duration of seven days. You delete the object `object-A.png`, which becomes soft deleted. Next, you change the policy's retention duration to 10 days and then you delete the object `object-B.png`, which also becomes soft deleted. `object-A.png` will be retained for seven days in the soft-deleted state, while `object-B.png` will be retained for 10 days.

Changes to the retention period of a soft delete policy take up to 30 seconds to propagate.




To learn how to set and manage soft delete policies on buckets, see [Set and manage soft delete policies](https://docs.cloud.google.com/storage/docs/use-soft-delete).

## Properties of soft-deleted resources

When a bucket or object is deleted under an active soft delete policy, the resource transitions to a soft-deleted state. You can restore soft-deleted resources during their retention duration.

Soft-deleted resources have the following characteristics:

  * Soft-deleted objects and buckets cannot be read, modified, or overwritten. The only supported operations are listing them or restoring them.

  * Soft-deleted resources are hidden from list operations by default. To view soft-deleted resources, you must explicitly specify a flag or filter to view the resources.

  * You cannot modify a soft-deleted bucket or list its contents until the bucket itself is restored. The method you use to restore a soft-deleted bucket affects whether the objects in the bucket are also restored:

    * You can restore a soft-deleted bucket and its objects at the same time by using the Google Cloud console.

    * Restoring a bucket using the Google Cloud CLI or the JSON API restores only the empty bucket. You must then restore the objects in a separate operation to recover its contents.

  * If a bucket name is taken by a new live bucket, you can't restore the soft-deleted bucket until the conflicting live bucket is removed.

  * If your project is deleted, any bucket that has soft delete enabled is retained for the soft delete retention duration or the [Google Cloud project recovery window](https://docs.cloud.google.com/resource-manager/docs/delete-restore-projects), whichever time period is shorter. After this time period, the bucket is permanently deleted.

If you restore a deleted project, buckets that were live when the project was deleted are restored as live buckets. Buckets that were soft-deleted when the project was deleted remain soft-deleted until their retention duration ends.

Buckets that don't have soft delete enabled might be deleted immediately when a project is deleted, and might not be restorable.

  * Some Cloud Storage capabilities are compatible with soft delete policies but don't affect soft-deleted objects. Examples of such capabilities are Autoclass, Object Lifecycle Management, Bucket Lock, and Object Retention Lock.




For instructions on restoring soft-deleted objects or buckets, see [Restore soft-deleted objects](https://docs.cloud.google.com/storage/docs/use-soft-deleted-objects) or [Restore soft-deleted buckets](https://docs.cloud.google.com/storage/docs/use-soft-deleted-buckets).

## Object restores

When you restore a soft-deleted object, Cloud Storage creates a new, live copy of that object within the same bucket. The original, soft-deleted version remains in the background until its retention period officially expires. The following list describes core restore behaviors:

  * When you restore an object, Cloud Storage generates a new version of the object. For more information about object versions, see [Object immutability](https://docs.cloud.google.com/storage/docs/objects#immutability).

  * If a live object with the same name as a soft-deleted object already exists when you restore the soft-deleted object, the restored object will overwrite the existing live version. The overwritten object that was formerly live is then automatically soft-deleted.

In this specific scenario, your bucket will contain two copies of the restored object (one new live copy and the old soft-deleted copy) alongside the newly soft-deleted version of the object that was overwritten.

  * Regardless of the object's original storage tier or any active Autoclass settings, all restored objects are written to the Standard storage class.




### Object restore methods

You can restore soft-deleted objects by using one of two execution paths, based on your scale requirements:

  * [Restoring objects one at a time](https://docs.cloud.google.com/storage/docs/use-soft-deleted-objects#restore): Used to synchronously restore individual objects.

  * [Restoring objects in bulk](https://docs.cloud.google.com/storage/docs/use-soft-deleted-objects#bulk-restore): Used for large-scale data recovery. You can initiate asynchronous [long-running operations](https://google.aip.dev/151) to recover large groups of objects that match specific filter criteria.




### Restoring objects with duplicate paths

Although rare, duplicate soft-deleted objects with identical names and generation values can occur in [buckets with hierarchical namespace enabled](https://docs.cloud.google.com/storage/docs/hns-overview). This conflict can happen if you rename folders that contain objects with duplicate names in buckets with [hierarchical namespace](https://docs.cloud.google.com/storage/docs/hns-overview) enabled. In this scenario, it's rare but possible that two soft-deleted objects might coincidentally share the same [generation number](https://docs.cloud.google.com/storage/docs/metadata#generation-number).

To understand this scenario, see the following example:

  1. You have an object named `cat.png` inside a folder named `my-folder-A`. `cat.png` is assigned a generation number of `999`. You delete `cat.png`, which becomes soft deleted.

  2. You delete the empty parent folder `my-folder-A`.

  3. Elsewhere in your storage, you have a folder named `my-folder-B`. Inside this folder is a different object named `cat.png`. Purely by coincidence, this `cat.png` object is also assigned a generation number of `999`. You rename `my-folder-B` to `my-folder-A`. Because of hierarchical namespace, the object's path changes to `my-folder-A/cat.png`.

  4. You delete this second `cat.png`, which becomes soft deleted.




Now, there are two soft-deleted objects named `cat.png` with the generation number `999`.

To restore, list, or access a specific soft-deleted object version among duplicates, you must supply a unique `restoreToken` parameter in your request. Including the `restoreToken` parameter is required when restoring, listing, or accessing soft-deleted object versions in buckets with hierarchical namespace enabled. Failing to include the `restoreToken` parameter when duplicates objects exist results in an error prompting you for the token. Submitting the wrong token, name, or generation number will return an error indicating that the object couldn't be found. For more information on the `restoreToken` parameter, see the [`objects.restore` method](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/restore).

## Pricing

Soft-deleted objects continue to accrue storage charges until their retention period expires and they're permanently deleted. Objects that get soft deleted before their minimum storage duration ends incur early deletion charges, unless that object was stored in Standard storage.

For detailed information about costs associated with soft delete, see [Cloud Storage pricing](https://docs.cloud.google.com/storage/pricing).

### Reduce costs for temporary objects when using soft delete

If a bucket primarily contains short-lived, temporary objects, enabling soft delete on the bucket can result in significantly increased storage costs. To help reduce costs for temporary objects, we recommend the following:

  * If you need to rename an object, use the [`objects.move` JSON API method](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/move) to rename the object. Don't rename the object by copying it.

  * Store temporary objects in buckets that don't have soft delete enabled.




Temporary objects typically have a short lifecycle before they're deleted. Temporary objects might be:

  * Data that is used as the source for creating [composite objects](https://docs.cloud.google.com/storage/docs/composite-objects)

  * Data that is regenerated for a short-lived purpose, like query results or staging files

  * Data from workloads that have a high write and delete frequency (for example, millions of deletions daily)

  * Data that can be permanently deleted by accident with zero impact on production continuity




## Interactions with other products and features

When soft delete is enabled, it behaves with other products and features in the following ways:

  * [Rapid Bucket](https://docs.cloud.google.com/storage/docs/rapid/rapid-bucket): Zonal buckets that use Rapid Bucket don't support soft delete.

  * [Object Lifecycle Management](https://docs.cloud.google.com/storage/docs/lifecycle):

    * Object Lifecycle Management rules don't affect soft-deleted objects. It is not possible to use Object Lifecycle Management to change the storage class of soft-deleted objects or to permanently delete then.

    * Objects deleted by Object Lifecycle Management become soft-deleted. If you also have Object Versioning enabled on your bucket, deleted live objects become noncurrent and deleted noncurrent objects become soft-deleted.

  * [Object Versioning](https://docs.cloud.google.com/storage/docs/object-versioning): When you delete a noncurrent object, it becomes soft-deleted.

  * [XML API multipart uploads](https://docs.cloud.google.com/storage/docs/multipart-uploads): XML API multipart upload [parts](https://docs.cloud.google.com/storage/docs/xml-api/put-object-multipart) are not protected by soft delete.

  * [Autoclass](https://docs.cloud.google.com/storage/docs/autoclass):

    * Autoclass management fees are not assessed for soft-deleted objects.

    * Autoclass does not change the storage class of soft-deleted objects.

    * When you restore a soft-deleted object, the resulting object is set to the Standard storage class.

  * [Bucket Lock](https://docs.cloud.google.com/storage/docs/bucket-lock) and [Object Retention Lock](https://docs.cloud.google.com/storage/docs/object-lock) features: These features will prevent you from deleting objects until they fulfill their retention policies. Soft delete then provides an additional layer of protection by retaining deleted objects for a separate soft delete retention duration.

  * [Pub/Sub notifications](https://cloud.google.com/support-hub): Restoring a soft-deleted version of an object triggers an [OBJECT_FINALIZE](https://docs.cloud.google.com/storage/docs/pubsub-notifications#events) event.

  * [Managed folders](https://docs.cloud.google.com/storage/docs/managed-folders): Soft delete cannot restore the IAM policies on [managed folders](https://docs.cloud.google.com/storage/docs/managed-folders). If you soft delete an object and delete a managed folder that grants IAM policies for the object, you might have to recreate those IAM policies before you have the necessary permissions to restore the soft-deleted object.

  * [Tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview): If you create a bucket without including a soft delete setting yourself, the Cloud Storage default is to create the bucket with a seven day soft delete retention duration. You can change this default by [using a tag](https://docs.cloud.google.com/storage/docs/use-tags-for-soft-delete). The tag can change the default retention duration for new buckets to be any value between 7 and 90 days, or it can change the default to disable soft delete on new buckets. You can also use tags to disable soft delete by default. 

  * [Recommender](https://docs.cloud.google.com/storage/docs/soft-delete-recommender): You can enable the Recommender API to receive suggestions and insights on enabling or disabling soft delete based on Cloud Billing costs and usage. To learn more, see [soft delete recommender](https://docs.cloud.google.com/storage/docs/soft-delete-recommender). 




## What's next

  * Learn how to [set soft delete policies](https://docs.cloud.google.com/storage/docs/use-soft-delete).
  * Learn how to [restore soft-deleted objects](https://docs.cloud.google.com/storage/docs/use-soft-deleted-objects).
  * Learn about the [`storage.softDeletePolicySeconds` policy constraint](https://docs.cloud.google.com/storage/docs/org-policy-constraints#soft-delete-retention).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
