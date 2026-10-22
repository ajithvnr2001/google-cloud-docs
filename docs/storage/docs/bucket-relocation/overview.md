---
url: https://docs.cloud.google.com/storage/docs/bucket-relocation/overview/
title: Bucket relocation \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:31:40.087516+00:00
---

# Bucket relocation  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/bucket-relocation/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Bucket relocation Stay organized with collections  Save and categorize content based on your preferences. 

Bucket relocation is available only if you've configured [Storage Intelligence](https://docs.cloud.google.com/storage/docs/storage-intelligence/overview).

This document describes how Cloud Storage bucket relocation helps you to relocate buckets serverlessly between geographic locations. Using bucket relocation, you can move an existing bucket from one location to another without changing the bucket's name or requiring manual transfer of data within the bucket.

Before you begin the relocation process, [plan your bucket relocation](https://docs.cloud.google.com/storage/docs/bucket-relocation/plan-bucket-relocation) to minimize disruption. For instructions about how to perform the relocation, see [relocate buckets](https://docs.cloud.google.com/storage/docs/bucket-relocation/relocate-buckets).

## Benefits

The benefits of bucket relocation are as follows:

  * **Simplified migration** : you can relocate buckets with minimal operational overhead. No complex scripting or multi-step processes are required.

  * **Continuous operation** : your applications remain accessible throughout the relocation process, with no downtime for read operations and minimal downtime for write operations.

  * **Improved performance** : colocating Compute Engine and Cloud Storage resources within the same region can reduce latency and enhance performance.

  * **Metadata preservation** : the bucket relocation process retains the object metadata. Retaining the object metadata maintains compatibility with existing applications and workflows after the bucket is moved.

  * **Storage class configurations** : you can maintain existing [ Cloud Storage class](https://docs.cloud.google.com/storage/docs/storage-classes) settings, including [Autoclass](https://docs.cloud.google.com/storage/docs/autoclass). Preserving the storage class helps to keep your cost structure consistent after the relocation.

**Note:** If your bucket uses [legacy storage classes](https://docs.cloud.google.com/storage/docs/storage-classes#legacy), they are converted to Standard storage class during the bucket relocation process.



## Use cases

The following are use cases you can achieve by relocating your buckets:

  * **Reduce data transfer cost** : avoid data transfer costs by relocating your bucket closer to the workloads accessing the bucket's data. For example, if your data is stored in the United States and primarily accessed from Europe, you can move your bucket to a European location to reduce data transfer costs.

  * **Improve performance** : improve your application's speed and response by moving your data closer to your Compute Engine workloads. For example, if your application runs in `us-central1` but your data resides in `asia-east1`, you can relocate your bucket to `us-central1` to reduce latency.

  * **Enhance resilience** : safeguard your critical data from regional outages. For example, if your data is stored in a single region, you can relocate it to a dual-region or multi-region for increased availability and disaster recovery.




## Relocation types

There are two types of bucket relocations:

  * **Bucket relocation with write downtime** : in bucket relocation with write downtime, there is a period where you can't perform object write operations during the bucket relocation process.

  * **Bucket relocation without write downtime** : in bucket relocation without write downtime, you can continue to perform object write operations without interruption while the bucket relocation happens in the background.




The bucket's source and destination locations determine whether a bucket relocation involves write downtime. The following table shows how your bucket's location affects write downtime during a relocation, including the differences between relocations with and without downtime.

Specification | Bucket relocation with write downtime | Bucket relocation without write downtime  
---|---|---  
Bucket location | Relocating a bucket between the following locations causes downtime:

  * Regions
  * Dual-regions
  * Multi-regions
  * Multi-regions and predefined dual-regions
  * Multi-regions and configurable dual-regions if the two locations have different [multi-region codes](https://docs.cloud.google.com/storage/docs/locations#location-mr)

| Relocating a bucket between the following locations causes no downtime if the two locations share the same multi-region code:

  * Configurable dual-regions
  * Multi-regions and configurable dual-regions

  
Write availability | You can't perform write operations during the final synchronization step. | Write operations continue uninterrupted during the relocation. **Note** : Relocations without write downtime take a minimum of seven days to complete, regardless of bucket size or object count. This minimum duration is required to let in-flight resumable uploads finish. Because relocation progress is non-linear and unpredictable, don't use early relocation progress to estimate total duration for larger relocations.   
User involvement | You must initiate the write downtime finalization step. | No explicit finalization step is required.  
Performance impact | You can't write or update objects in the bucket during the final synchronization step.| Object read and write latency might increase during the relocation.  
Bucket relocation cancellation | Faster than relocations without write downtime. | Cancellation isn't instantaneous and can take longer due to the need to backfill objects.  
Feature support| Provides less feature support than relocations without write downtime. For more information about the unsupported features, see [Unsupported features](https://docs.cloud.google.com/storage/docs/bucket-relocation/plan-bucket-relocation#compatibility-and-limitations).| Limitations exist for features such as [multipart uploads](https://docs.cloud.google.com/storage/docs/multipart-uploads), [retention policies](https://docs.cloud.google.com/storage/docs/bucket-lock#retention-policy), [Firebase](https://firebase.google.com/), and [appspot](https://docs.cloud.google.com/appengine/docs/standard/python3/runtime). For more information about these limitations, [Review the bucket compatibility requirements and limitations](https://docs.cloud.google.com/storage/docs/bucket-relocation/plan-bucket-relocation#compatibility-and-limitations).  
Minimum relocation duration  | None | Seven days. This minimum applies regardless of the bucket's total size or the number of objects it contains.  
  
## Understand the bucket relocation process

Bucket relocation helps you move your data from a source bucket to a destination bucket. The source bucket holds the data that you want to move and the destination bucket is where you want to move your data.

The following diagram shows the bucket relocation process flow:

[ ![Bucket relocation process flow.](https://docs.cloud.google.com/static/storage/docs/images/bucket-relocation-process-flow.jpeg)](https://docs.cloud.google.com/static/storage/docs/images/bucket-relocation-process-flow.jpeg) **Figure 1.** Bucket relocation process flow (click to enlarge).

* Final synchronization is only required for relocations with write downtime.

The following table lists the three primary steps and the description for each step:

Step | Description  
---|---  
**[Perform a dry run](https://docs.cloud.google.com/storage/docs/bucket-relocation/relocate-buckets#dry-run)**  
(Optional)| Simulates the bucket relocation process to identify potential issues before the actual data transfer begins.**Note:** We recommend you perform a dry run as it allows for the early detection of potential problems without impacting the actual relocation process.  
**[Initiate the relocation step](https://docs.cloud.google.com/storage/docs/bucket-relocation/relocate-buckets#initiate-relocation)** | Copies data from the source bucket to the destination bucket. The bucket metadata is write-locked to prevent any changes to the bucket that might affect the relocation process. However, you can write, modify, and delete objects in the bucket. The factors influencing the duration are as follows:

  * The frequency of object updates, deletions, or additions within the bucket directly impacts the copy duration. A higher rate of change requires more time. There's a maximum object movement rate `Rm, objects/second`. With `N` total objects and an update rate of `R objects/second`, the copy step duration can be estimated as `N / (Rm - R)` seconds.
  * Large buckets require more relocation time due to finite bandwidth.
  * The size of individual objects affects the copy time. Objects larger than 10 GB take longer to transfer than objects under 10 GB due to bandwidth constraints. For example, a 1 TB object takes one day to copy.

  
**[Initiate the final synchronization step](https://docs.cloud.google.com/storage/docs/bucket-relocation/relocate-buckets#initiate-final-sync)**  
(Only required for relocations with write downtime) | Once you initiate the final synchronization, the bucket is write-locked. As a result, you can't write or update any objects within the bucket during this time, preventing data inconsistencies. However, you can continue to read from the bucket.**Note:** During the final synchronization step, attempts to update objects in the bucket result in an HTTP `412` error. The error indicates that the bucket is undergoing a bucket relocation operation and has a write-lock in place, restricting any modifications to its objects. To successfully update the objects, it is necessary to defer the action until the ongoing bucket relocation operation and the associated synchronization process conclude. Upon completion, the write operations to the bucket are permitted.Once all data has been transferred, verified, and the bucket is operational in the new location, the write-lock is automatically removed. You can then resume writing and updating objects in the bucket.  
  
## Limitations

To relocate your bucket, verify that your bucket's configurations support relocating buckets by [reviewing the list of unsupported features and compatibility requirements](https://docs.cloud.google.com/storage/docs/bucket-relocation/plan-bucket-relocation#compatibility-and-limitations).

Bucket relocation isn't supported if the source and destination buckets are in the following locations:

Location type | Unsupported locations  
---|---  
[Regions](https://docs.cloud.google.com/storage/docs/locations#location-r) | 

  * `ME-CENTRAL1`
  * `ME-WEST1`

  
  
## Pricing

For details on pricing associated with bucket relocation, see [Cloud Storage pricing](https://docs.cloud.google.com/storage/pricing).

## What's next

  * Learn how to [plan a bucket relocation](https://docs.cloud.google.com/storage/docs/bucket-relocation/plan-bucket-relocation).
  * Learn how to [relocate buckets](https://docs.cloud.google.com/storage/docs/bucket-relocation/relocate-buckets).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
