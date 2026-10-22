---
url: https://docs.cloud.google.com/storage/docs/bucket-relocation/plan-bucket-relocation/
title: Plan your bucket relocation \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:31:51.910705+00:00
---

# Plan your bucket relocation  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/bucket-relocation/plan-bucket-relocation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Plan your bucket relocation Stay organized with collections  Save and categorize content based on your preferences. 

Before you [relocate a bucket](https://docs.cloud.google.com/storage/docs/bucket-relocation/overview), verify your bucket usage and plan for potential downtime. Planning your relocation also helps you maintain data compatibility and control storage costs.

The following sections describe the planning steps.

## Determine your bucket relocation type

When relocating your bucket, it's important to understand that there might be a write downtime period during the final synchronization step where you can't update or upload new objects. Additionally, you won't be able to change your bucket's configuration during the relocation process. To determine if your relocation involves downtime, see [Relocation types](https://docs.cloud.google.com/storage/docs/bucket-relocation/overview#relocation-types).

## Review the unsupported features and the compatibility requirements

Identify any configurations in your source bucket that don't support bucket relocation and the configurations that require action to support bucket relocation. If your bucket uses unsupported configurations that can't be modified, or if the source or destination is an [unsupported location](https://docs.cloud.google.com/storage/docs/bucket-relocation/overview#limitations), you must manually copy the objects into a different bucket in the destination location, instead of relocating the bucket with its objects. For details, see [Move data between buckets](https://docs.cloud.google.com/storage/docs/moving-buckets).

The following sections describe the unsupported features and the compatibility requirements.

### Unsupported features

The following table describes the features that aren't compatible with bucket relocation. In some cases, you can reconfigure a feature to support bucket relocation:

Feature | Compatibility status | Required action before initiating the bucket relocation  
---|---|---  
[Hierarchical namespace](https://docs.cloud.google.com/storage/docs/hns-overview) | Not supported for bucket relocations with write downtime. | If a bucket has hierarchical namespace enabled, you can only relocate it if the process doesn't involve write downtime  
[Appspot buckets](https://docs.cloud.google.com/appengine/docs/standard/using-cloud-storage) | Not supported. | You can't relocate Appspot buckets. Consider migrating Container Registry to Artifact Registry as a workaround for default buckets created by App Engine.  
[Firebase buckets](https://firebase.google.com/docs/storage) | Not supported. | You can't relocate Firebase buckets.  
[Object holds](https://docs.cloud.google.com/storage/docs/object-holds) | Not supported.  
You can't relocate buckets containing objects with holds. | To use bucket relocation, remove the object holds.  
[Managed folders](https://docs.cloud.google.com/storage/docs/managed-folders) | Not supported.  
You can't relocate buckets containing managed folders. | To use bucket relocation, delete the managed folders.  
[Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys) or [customer-supplied encryption keys (CSEK)](https://docs.cloud.google.com/storage/docs/encryption/customer-supplied-keys) | Not supported for relocations with write downtime. | To use bucket relocation, remove the customer-managed encryption keys or customer-supplied encryption keys. After removal, Cloud Storage automatically protects your data using the [standard Cloud Storage encryption](https://docs.cloud.google.com/storage/docs/encryption/default-keys).   
[Rapid Cache](https://docs.cloud.google.com/storage/docs/rapid/rapid-cache) | Not supported for bucket relocations without write downtime and partially supported for bucket relocations with write downtime. |  For relocating buckets without write downtime, disable Rapid Cache before initiating the relocation. For relocating buckets with write downtime, disable Rapid Cache before the [final synchronization step](https://docs.cloud.google.com/storage/docs/bucket-relocation/relocate-buckets#initiate-final-sync).  
[Bucket lock](https://docs.cloud.google.com/storage/docs/bucket-lock) | Not supported for buckets with an active retention policy. If the retention policy is **[locked (Bucket Lock is enabled)](https://docs.cloud.google.com/storage/docs/bucket-lock#policy-locks)** , the policy is irreversible. As a result, Cloud Storage doesn't support relocating the bucket. | If the retention policy is **[unlocked](https://docs.cloud.google.com/storage/docs/bucket-lock#retention-policy)** , you must remove the policy before you can proceed with the relocation.  
[Object Retention lock](https://docs.cloud.google.com/storage/docs/object-lock) | Not supported. Once Object Retention Lock is enabled, you can't disable it. | You can't relocate buckets that have Object Retention Lock enabled.  
[Tags](https://docs.cloud.google.com/storage/docs/tags-and-labels) | Not supported for relocations with write downtime. |  You must detach tags that are directly attached to the bucket. **Note:** Tags created at the project or organization level, but not directly attached to the bucket, don't prevent relocation.If any of the tags being detached from your source bucket are used for access control, you must use an alternative method to set up the [IAM roles](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) to secure the data in your bucket. To do so, complete the following steps:

  1. Copy your tag configuration to refer to while you configure IAM roles. After you've verified your IAM settings, you can delete the copy.
  2. [Configure IAM permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions) to match your existing access control rules.
  3. [Detach any existing tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#detaching) from the source bucket.

  
[Inventory report configurations](https://docs.cloud.google.com/storage/docs/insights/inventory-reports) | Existing inventory report configurations aren't preserved during the relocation process. | Save your existing inventory report configurations manually before starting the relocation process, so that you can recreate them after the relocation process is complete. For information about managing inventory report configurations, see [Create and manage inventory report configurations](https://docs.cloud.google.com/storage/docs/insights/using-inventory-reports).  
  
### Feature compatibility during bucket relocation

The following table describes how other Cloud Storage capabilities work when you relocate a bucket. The behavior might vary depending on the relocation mode:

Feature | Relocation with write downtime | Relocation without write downtime  
---|---|---  
Autoclass behavior |  Autoclass is temporarily paused during the final synchronization step. The pause might delay objects moving to colder storage classes. For details, see [Autoclass object transitions when relocating buckets](https://docs.cloud.google.com/storage/docs/autoclass#autoclass-object-transitions).  | Autoclass behavior isn't affected.  
BigQuery and BigLake tables | BigLake external tables and BigQuery tables using Apache Iceberg become inaccessible after a relocation and require manual recreation. Automatic detection of impacted tables isn't available. | Supported.  
Object size limit | 2 TB limit applies to object sizes. | No size limit.  
Multipart uploads |  Compatibility and behavior for [multipart uploads](https://docs.cloud.google.com/storage/docs/multipart-uploads) depend on the status of the upload when you start a bucket relocation: 

  * **New multipart uploads** : Not supported.   
Starting a multipart upload after the relocation has been initiated is not supported leading to a failure to start the upload. The multipart upload attempt fails with a `FAILED_PRECONDITION` error.
  * **In-progress multipart uploads:** Not supported.   
In-progress multipart uploads that are not completed before the final synchronization step block the finalization of the relocation. After you finish or cancel the in-progress multipart upload, you can retry the finalization step.
  * **Finished multipart uploads:** Supported.   
If a multipart upload is started before the bucket relocation starts and completed before the final synchronization step, the objects that were uploaded are relocated without requiring a re-upload.

|  Compatibility and behavior for multipart uploads depend on the status of the upload when you start a bucket relocation: 

  * **New multipart uploads** : Not supported.   
Starting a multipart upload after the relocation has been initiated is not supported leading to a failure to start the upload. The multipart upload attempt fails with a `FAILED_PRECONDITION` error.
  * **In-progress multipart uploads:** Not supported.   
You must complete or cancel any in-progress multipart uploads before starting the bucket relocation.
  * **Finished multipart uploads:** Supported.

  
Resumable uploads | Not supported.   
In-progress resumable uploads must be finalized before the final synchronization step of the bucket relocation process to avoid data loss. | Supported.  
Relocation across projects | Not supported.   
You can't relocate buckets across projects. | Supported.  
Metadata updates | Not supported.   
You can't update a bucket's metadata during relocation. | Supported.  
Request rate ramp-up | Relocated buckets are subject to the same request rate ramp-up guidelines as newly created buckets. | Not applicable.  
  
## Analyze the bucket characteristics

To estimate your bucket relocation time, analyze your bucket's characteristics and usage, considering the following factors:

  * **At-rest bytes** : The total amount of data stored in the bucket impacts storage costs and transfer time.

  * **Replication** : Replicating the bucket to other regions, either synchronously or asynchronously, impacts data availability, durability, and cost. For details, see [Data availability and durability](https://docs.cloud.google.com/storage/docs/availability-durability).

  * **Data transfer** : The amount of data transferred out of the bucket during the relocation impacts the data transfer cost calculations. To calculate your bucket's data transfer costs, see [Cloud Storage pricing](https://docs.cloud.google.com/storage/pricing).

  * **Usage patterns** : Understanding bucket activity levels, or how busy the bucket is, through usage patterns helps you prevent unexpected conflicts during the relocation. To understand your bucket's usage patterns, you can analyze your logs. For details, see [Usage logs and storage logs](https://docs.cloud.google.com/storage/docs/access-logs).

  * **Bucket write operations** : Frequent bucket write operations during the relocation process increase the cost and duration. Relocation progress is non-linear and unpredictable. Don't use the duration of smaller moves to estimate the time required for larger relocations. To monitor how frequently objects are written to your bucket, see [Overview of monitoring in Cloud Storage](https://docs.cloud.google.com/storage/docs/monitoring).




## Define your relocation goals

Based on your analysis of the bucket characteristics, identify the reasons for moving your bucket. The following are common goals for relocating a bucket:

  * **Cost management** : Reduce storage costs by moving to a lower-cost region or minimize data transfer costs by moving data closer to its access location. You'll need to calculate your Cloud Storage and data transfer costs and compare them to potential costs in different locations. For details about calculating costs for your Cloud Storage, see [ Cloud Storage pricing](https://docs.cloud.google.com/storage/pricing).

  * **Performance enhancement** : Improve data access speed and application performance by relocating the bucket closer to users or applications. To do so, identify the geographic regions where performance is critical and relocate your buckets.

  * **Reliability improvement** : Enhance data durability and disaster recovery capabilities by using dual- or multi-region configurations.




## Decide on the bucket location

Based on your analysis and goals, choose the most suitable storage location for the bucket you're relocating from the following options:

  * **Single-region** : Store data in a single region that is cost-effective for applications with users concentrated in one geographic area.

  * **Dual-region** : Maintain two copies of your data in two regions within the same continent, providing higher availability and disaster recovery capabilities within a specific geographic area.

  * **Multi-region** : Distribute data across multiple regions, offering the highest level of availability and durability.




To learn more about choosing a location, see [Considerations for choosing a location](https://docs.cloud.google.com/storage/docs/locations#considerations).

## Understand the factors that affect the relocation time

Several factors affect the relocation time, and understanding them can help to estimate the required time. While these factors offer a helpful starting point for planning and scheduling your relocation, actual relocation times might be longer or shorter than the estimated time. Therefore, when scheduling your relocation, add buffer time to account for potential delays. The following sections describe the factors that affect the relocation time.

**Note:** When estimating the time needed for relocating buckets, include a 1-2 hour setup time. The setup time includes validating the new bucket destination and preparing for the move. The setup time is the same for all buckets regardless of the bucket size. For small buckets, the setup time makes the entire relocation seem slow. For large buckets, the actual data transfer takes longer, so the setup time is less noticeable.

### Relocation service limits

The following table describes the limits that affect the relocation time:

Factor | Value | Description  
---|---|---  
**Maximum request rate per job** | 10,000 objects per second |  These are the number of copy requests the service can handle per second. A higher request rate means more files can be moved simultaneously. If your bucket has many small files, a high request rate speeds up the migration. If you have only a few large files, this factor has less impact.   
**Maximum overall bandwidth per project** | 10 GBps |  This is the maximum speed or bandwidth at which you can transfer data for a single project within a source location. If you're moving multiple buckets within the same project, then the buckets share the bandwidth. A higher bandwidth means more data can be transferred at once. Even with a high request rate, if the bandwidth is small, the overall transfer is slow.   
**Maximum bandwidth per single object** | 8 MBps |  This is the maximum speed at which you can transfer a single object. A higher bandwidth per single object means you can transfer the objects at a faster rate. This is the speed limit for moving one object at a time. Even with a high request rate and high bandwidth per bucket, if individual objects have a speed limit, they can take more time to transfer.   
**Maximum concurrent relocations per project** | 30 relocations |  The bucket relocation service supports up to 30 concurrent relocations from the same location within a project.   
  
### Relocation Time to Live limit

To help with resource utilization and prevent relocations from running indefinitely, a Time to Live (TTL) limit applies to all bucket relocations. TTL refers to the maximum time allowed for the entire relocation process to complete.

The maximum time allowed to complete a bucket relocation is 28 days and includes all phases of the relocation process, such as the initial copy, incremental updates, and final synchronization.

If the relocation process exceeds the 28-day TTL limit, the relocation operation fails.

### Ongoing bucket activity

If you continue to write new objects, delete existing ones, or update objects in the bucket during the relocation, these operations compete for resources with the copy requests and can slow down the relocation process.

### Lifecycle rules

If you have lifecycle rules configured for your bucket, such as automatically deleting or archiving objects after a specific time, these actions increase the overall relocation time.

## Configure Storage Intelligence

You must configure Storage Intelligence for both the source and destination locations. You can configure Storage Intelligence at different levels of your [Google Cloud resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#resource-hierarchy-detail). You can also use inclusion and exclusion filters to include relevant buckets in your Storage Intelligence configuration. For details, see [Configure Storage Intelligence](https://docs.cloud.google.com/storage/docs/storage-intelligence/configure-and-manage-storage-intelligence#configure-storage-intelligence).

## Enable soft delete for relocations with write downtime

If your bucket relocation involves write downtime, then you must enable [soft delete](https://docs.cloud.google.com/storage/docs/soft-delete) on the bucket and set the [retention duration](https://docs.cloud.google.com/storage/docs/soft-delete#retention-duration) to at least seven days. The retention duration is the amount of time that soft delete keeps deleted objects before permanently deleting them. For information about how to configure the soft delete retention duration, see [Use soft delete](https://docs.cloud.google.com/storage/docs/use-soft-delete). To determine whether your relocation involves downtime, see [Relocation types](https://docs.cloud.google.com/storage/docs/bucket-relocation/overview#relocation-types).

**Note:** When you relocate a bucket, all objects, including those that are soft-deleted, move with it. To reduce the overall data in a bucket you plan to relocate, permanently delete any unwanted objects before enabling soft delete on that bucket.

## Check quotas and limits

Quotas and cloud capacity assessments are tied to specific regions or zones. As a result, when you move a bucket to a new location, you need to verify that the new location has sufficient quotas to accommodate the bucket's data. For more information about quotas and limits, see [Quotas and limits](https://docs.cloud.google.com/storage/quotas).

## What's next

  * Learn how to [relocate buckets](https://docs.cloud.google.com/storage/docs/bucket-relocation/relocate-buckets).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
