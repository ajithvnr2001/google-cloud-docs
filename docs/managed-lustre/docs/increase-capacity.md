---
url: https://docs.cloud.google.com/managed-lustre/docs/increase-capacity/
title: Increase the capacity of a Managed Lustre instance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:41:29.390022+00:00
---

# Increase the capacity of a Managed Lustre instance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-lustre/docs/increase-capacity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Managed Lustre ](https://docs.cloud.google.com/managed-lustre/docs/overview)



Send feedback 

#  Increase the capacity of a Managed Lustre instance Stay organized with collections  Save and categorize content based on your preferences. 

You can increase the storage capacity of your Managed Lustre instance. Capacity cannot be decreased.

When you increase an instance's capacity, you can continue to use the instance while the update operation is in progress.

**Tip:** If your instance is nearing full capacity and you're seeing `ENOSPC` errors ("no space left on disk") despite monitoring tools showing remaining capacity, refer to ENOSPC errors for mitigation strategies.

## Limitations on increasing capacity

For performance tiers with two different step sizes, the current capacity of the instance determines its maximum possible size.

If an instance's capacity is at or below the step size threshold, its size can be increased up to the threshold value itself. It cannot be expanded beyond this limit.

For example, in the 250 MBps per TiB tier, the threshold at which the step size changes is 10,224,000 GiB. Any instance created with a capacity at or below this threshold can only be expanded up to that 10,224,000 GiB limit.

## Calculate your new capacity

You can update an instance's capacity up to the maximum value allowed for its performance tier and step size. These values are as follows:

Performance tier | Min capacity | Max capacity | Step size  
---|---|---|---  
**1,000 MBps per TiB** | 9,000 GiB | 10,008,000 GiB (9.5 PiB) | For storage capacities up to 2,556,000 GiB: 9,000 GiB  
For larger storage capacities: 72,000 GiB  
**500 MBps per TiB** | 18,000 GiB | 20,016,000 GiB (19.1 PiB) | For storage capacities up to 5,112,000 GiB: 18,000 GiB  
For larger storage capacities: 144,000 GiB  
**250 MBps per TiB** | 36,000 GiB | 40,032,000 GiB (38.2 PiB) | For storage capacities up to 10,224,000 GiB: 36,000 GiB  
For larger storage capacities: 288,000 GiB  
**125 MBps per TiB** | 72,000 GiB | 20,448,000 GiB (19.5 PiB) | 72,000 GiB  
**Dynamic** (25 MBps per TiB) | 472,000 GiB | 84,016,000 GiB (80.1 PiB) | 472,000 GiB  
  
The updated capacity must be a multiple of the step size and cannot exceed the maximum for that step size.

Your Google Cloud project has throughput and capacity quotas that affect the available capacity per [Virtual Private Cloud (VPC) network](https://docs.cloud.google.com/vpc/docs/vpc) per zone. You might need to request additional throughput or capacity quota before increasing your instance's capacity. See [Quotas and limits](https://docs.cloud.google.com/managed-lustre/docs/quotas) for details.

### Capacity calculator

Use the following calculator to find a valid capacity for your selected performance tier.

## Update the instance capacity

You can use the Google Cloud console or the Google Cloud CLI to update the instance's capacity.

###  Google Cloud console 

  1. Go to the **Managed Lustre** page in the Google Cloud console.

[Go to Managed Lustre](https://console.cloud.google.com/managed-lustre/)

  2. Click the **Instance name** of the instance to update. The instance overview page is displayed.

  3. Click **Edit**.

  4. Enter the new storage capacity value. The value must be equal to or less than the maximum allowed capacity, and must be a multiple of the step size. See Calculate your new capacity for these values.

  5. Click **Submit**.




###  gcloud 

Use the [`gcloud lustre instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/lustre/instances/update) command to increase your instance's storage capacity:
    
    
    gcloud lustre instances update INSTANCE_NAME \
      --location=LOCATION \
      --capacity-gib=NEW_CAPACITY
    

Where:

  * INSTANCE_NAME is the instance to update.
  * LOCATION is the zone in which the instance resides.
  * NEW_CAPACITY is the new storage capacity for this instance in gibibytes (GiB). The value cannot exceed the maximum allowed capacity and must be a multiple of the step size. See Calculate your new capacity for these values.



###  REST 

To update an instance using the REST API, send a PATCH request to its specific endpoint:
    
    
    PATCH https://lustre.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/instances/INSTANCE_NAME?updateMask=capacityGib
    Authorization: Bearer [YOUR_ACCESS_TOKEN]
    
    {
      "capacityGib": NEW_CAPACITY
    }
    

Where the following values must be specified:

  * PROJECT_ID is your Google Cloud project ID.
  * ZONE is the instance's Google Cloud zone.
  * INSTANCE_NAME is the name of the Managed Lustre instance to update.
  * `updateMask=capacityGib` specifies the field to update. A field will only be overwritten if it is in the mask.
  * NEW_CAPACITY is the new storage capacity for this instance in gibibytes (GiB). The value cannot exceed the maximum allowed capacity and must be a multiple of the step size. See Calculate your new capacity for these values.



See the [`instances.patch`](https://docs.cloud.google.com/managed-lustre/docs/reference/rest/v1/projects.locations.instances/patch) API reference for more details.

Once the update request has been submitted, Managed Lustre checks your available quota. If sufficient quota exists, the instance capacity is increased over a period of time, depending on the size change. Increases can take from 20 minutes to an hour or more.

You can continue to use your instance during the update operation.

## View update status

You can view the status of an update request from the following interfaces.

###  Google Cloud console 

  1. Go to the **Managed Lustre** page in the Google Cloud console.

[Go to Managed Lustre](https://console.cloud.google.com/managed-lustre/)

  2. Click the instance name in the list. The **Instance Details** page appears, which includes the current status of your instance update request.




###  gcloud 

By default, the `gcloud lustre instances update` command waits for completion before returning the shell prompt:
    
    
    Request issued for: [my-instance]
    Waiting for operation [projects/my-project/locations/us-central1-a/operations/operation-1234567890-123] to complete...
    

Once complete, the command line displays `Updated instance [my-instance]` along with the instance details, including the updated capacity.

If you ran the update command with the `--async` flag, or otherwise need to query the update status from the command line, you can retrieve the operation details to see if the instance has finished updating:
    
    
    gcloud lustre operations describe OPERATION_ID \
      --location=ZONE
    

While the instance is updating, the response shows a `done: false` value. Once complete, `done` is set to `true`.

For example:
    
    
    $ gcloud lustre operations describe operation-1234567890-123abc456-789def012-a1b2c3d4 \
        --location=us-central1-a
    
    done: false
    metadata:
      '@type': type.googleapis.com/google.cloud.lustre.v1.OperationMetadata
      apiVersion: v1
      createTime: '2025-08-27T18:13:49.771203623Z'
      requestedCancellation: false
      target: projects/my-project/locations/us-central1-a/instances/my-instance
      verb: update
    name: projects/my-project/locations/us-central1-a/operations/operation-1234567890-123abc456-789def012-a1b2c3d4
    

###  REST 

To query the status of an update operation, use the operation ID from the response. The operation ID has the following format:

  * `operation-1234567890123-6127783ad26ea-88913969-02748053`



Send a request to the following endpoint:
    
    
    GET https://lustre.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/operations/OPERATION_ID
    Authorization: Bearer
    

If successful, the response body contains an instance of [Operation](https://docs.cloud.google.com/managed-lustre/docs/reference/rest/v1/projects.locations.operations).

## Performance after increasing capacity

A Managed Lustre instance's maximum throughput is determined by its storage capacity and performance tier. Increasing the storage capacity of an existing instance increases its maximum throughput as well.

The performance increase may not be seen until new data has been written. Throughput performance gradually improves as new data is written and redistributed across the additional storage.

**Note:** Metadata performance will increase only if the increase in capacity results in an additional 72 GBps of provisioned throughput.

## 'No space left on device' errors

As your file system approaches full capacity (typically more than 90% utilization), you might start receiving premature `No space left on device` or `FILESYSTEM_NO_SPACE_ON_DEVICE` (`ENOSPC`) errors, even if monitoring tools indicate that aggregate free space is still available.

This behavior can occur due to several underlying mechanisms in distributed file systems:

  * OST imbalance: Lustre stripes file data across multiple Object Storage Targets (OSTs). However, certain workload patterns can fill a single OST regardless of your striping configuration. Common causes include writing files in append mode (`O_APPEND`) or maintaining large unlinked files.

  * Post-expansion errors: You might continue to receive `ENOSPC` errors even after adding capacity to your cluster. While expanding capacity adds new OSTs, it does not automatically rebalance your pre-existing files onto the newly added targets.

  * Client space grants: Compute Engine clients dynamically reserve portions of disk space for better performance. This reserved grant space reduces the available physical pool, meaning capacity metrics may not reflect space that distributed clients have already claimed.

  * Inode exhaustion: Workloads that generate millions of files can exhaust the file system's available inodes before reaching physical storage limits, causing `ENOSPC` errors on new file creation.




Recommended mitigation strategies:

  * Monitor capacity and set up alerts: Monitor per-OST capacity utilization and individual inode metrics in addition to aggregate cluster capacity. Run the [`lfs df`](https://doc.lustre.org/lustre_manual.xhtml#file_striping.checking_free_space) command from a mounted client to view per-target capacity usage, use `lfs df -i` for per-target inode usage, or see [Monitor instances and operations](https://docs.cloud.google.com/managed-lustre/docs/monitoring#storage_capacity_metrics) for details on monitoring metrics.

Set up automated alerts to trigger when aggregate capacity or individual OST utilization exceeds 80% (see [Create a storage capacity alert](https://docs.cloud.google.com/managed-lustre/docs/monitoring#example_create_a_storage_capacity_alert)).

  * Increase capacity: Once aggregate capacity reaches 80-90%, consider [increasing the capacity of your Managed Lustre instance](https://docs.cloud.google.com/managed-lustre/docs/increase-capacity). You may need to [request additional quota](https://docs.cloud.google.com/managed-lustre/docs/quotas#request_additional_quota) before expansion.

  * Rebalance storage: Use the [`lfs migrate`](https://doc.lustre.org/lustre_manual.xhtml#idm140506433317008) command, preferably in non-blocking mode (`-n`), to manually transition files from over-utilized OSTs to emptier or newly-added OSTs.

  * Check for unlinked files on clients: Open-unlinked files are large files held open by a process even after being unlinked from the file system namespace. These orphaned files remain on disk, consuming space, but are not visible in standard directory listings. In this case, Cloud Monitoring capacity metrics and the `lfs df` command report higher space usage than `du` or `lfs find`. Use the `lsof` command on clients to identify these files by looking for entries that are marked as `(deleted)`. Once identified, terminating the process holding the file handle or restarting the application releases the file system space.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
