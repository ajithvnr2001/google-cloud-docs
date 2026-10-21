---
url: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-disk-creation/
title: Troubleshooting disk creation and modification \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:22:33.540351+00:00
---

# Troubleshooting disk creation and modification  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-disk-creation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Troubleshooting disk creation and modification Stay organized with collections  Save and categorize content based on your preferences. 

This document lists errors that you might encounter when performing one of the following tasks:

  * Creating a Persistent Disk or Google Cloud Hyperdisk volume.
  * Modifying the provisioned size or performance of a Google Cloud Hyperdisk or Extreme Persistent Disk volume.



## The specified size or performance is invalid

When creating a Hyperdisk and Extreme Persistent Disk volume, or updating its provisioned performance, you might encounter errors if you specify a size or performance limit for the new disk that is too low or too high for the disk's type.

  * ERROR: (gcloud.compute.disks.create) Could not fetch resource:
           - Requested provisioned IOPS cannot be higher than 100,000.
           

  * ERROR: (gcloud.compute.disks.create) Could not fetch resource:
              - Requested provisioned throughput cannot be higher than 2,400.
              

  * ERROR: (gcloud.compute.disks.create) Could not fetch resource:
              - Disk size cannot be greater than 65,536 GB for disk type hyperdisk-ml.
              

  * ERROR: (gcloud.compute.disks.create) Could not fetch resource:
               Requested provisioned throughput cannot be smaller than 20.
              




**Resolution** :

To resolve this issue, specify limits that are within the allowed ranges for each Hyperdisk type. Valid values for each Hyperdisk type are in the Size limits and Performance limits sections of this document.

### Unable to increase provisioned IOPS due to disk size

When creating an Extreme Persistent Disk or Hyperdisk volume, or updating the provisioned performance of an existing disk, you might encounter one of the following errors if you specify an IOPS or throughput limit or that is too high for the disk's size:

  * Requested provisioned IOPS is too high for the current disk size
           

  * Requested provisioned throughput is too high for the requested disk size.
           




To resolve this issue, follow these steps.

  1. Decide if you want to increase the size of the disk to a value that supports the performance limit that you want, or choose a performance limit supported by the disk's current size. For valid limits for the disk type review the corresponding page from the following list:

     * [Hyperdisk Balanced](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced#size_limits)
     * [Hyperdisk Balanced High Availability](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced-ha#size_limits)
     * [Hyperdisk Extreme](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-extreme#size_limits)
     * [Hyperdisk ML](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-ml#size_limits)
     * [Hyperdisk Throughput](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-throughput#size_limits)
     * [Extreme Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/extreme-persistent-disk#performance_limits_and_workload_patterns)
  2. To use a different limit, retry the operation with the performance limit you chose in the previous step. Otherwise, to learn how to increase the size of a Hyperdisk or Extreme Persistent Disk, see [Increase the size of your Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/modify-hyperdisks#capacity_changes) or [Increase the size of a Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#increase_the_size_of_a_disk), respectively.




## Not specifying Hyperdisk Balanced High Availability as the disk type when converting a zonal disk to a regional disk

You might receive a message like the following when you try to create a regional disk from a zonal Hyperdisk Balanced or Hyperdisk Extreme disk.
    
    
    ERROR: (gcloud.compute.disks.create) ...
     - Creating a regional disk of type hyperdisk-balanced is not supported.
    

**Resolution**

To create a regional disk from a zonal Hyperdisk Balanced or Hyperdisk Extreme disk, clone the disk to a new Hyperdisk Balanced High Availability disk. If you clone the disk using the gcloud CLI or the REST, you must specify this disk type.

  * If you are using the gcloud CLI, include the `--disk-type=hyperdisk-balanced-high-availability` flag.
  * If you are using the Compute Engine API, include the `type` field in the request body with the value `hyperdisk-balanced-high-availability`.



For more information, see [Create a regional disk clone from a zonal disk](https://docs.cloud.google.com/compute/docs/disks/clone-duplicate-disks#create-regional-clone).

## Missing performance limit for Hyperdisk Balanced or Hyperdisk Balanced High Availability

When you create a Hyperdisk Balanced or Hyperdisk Balanced High Availability volume, if you specify a custom size for the disk, you must explicitly specify both the provisioned IOPS and the provisioned throughput. If you specify a custom size but omit one or both of the performance limits, you receive an error.

**Resolution**

To resolve this issue, specify both the provisioned IOPS and the provisioned throughput when you specify a custom size during disk creation. Valid values for each Hyperdisk type are in the Performance limits section of this page.

  * If you are using the gcloud CLI, include both the `--provisioned-iops` and `--provisioned-throughput` flags.
  * If you are using the REST, include both the `provisionedIops` and `provisionedThroughput` fields in the request body.



## Size limits for Hyperdisk volumes

The size you specify for a Hyperdisk volume must be within the ranges listed in following table.

Disk type | Minimum size | Maximum size | Default size  
---|---|---|---  
Hyperdisk Balanced | 4 GiB | 64 TiB1 | 100 GiB  
Hyperdisk Balanced High Availability | 4 GiB | 64 TiB | 100 GiB  
Hyperdisk Extreme | 64 GiB | 64 TiB | 1 TiB  
Hyperdisk Throughput | 2 TiB | 32 TiB | 2 TiB  
Hyperdisk ML | 4 GiB | 64 TiB | 100 GiB  
1**[Preview](https://cloud.google.com/products#product-launch-stages)** : C4 supports a maximum disk size of 128 TiB. For access to this feature, contact [hyperdisk-questions@google.com](https://mail.google.com/mail/?view=cm&fs=1&tf=1&to=hyperdisk-questions@google.com). 

However, the total size of all the Hyperdisk volumes that's attached to an instance can't exceed the [ instance's Hyperdisk size and attachment limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits#limits-instance).

## Performance limits for Hyperdisk volumes

The following table lists the limits for the performance that you can specify for each Hyperdisk type. However, the IOPS and throughput levels you can specify also depend on the volume's size. For a detailed summary of each limit, see the **Size and performance limits** section for [Hyperdisk Balanced](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced#size_limits), [Hyperdisk Balanced High Availability](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced-ha#size_limits), [Hyperdisk Extreme](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-extreme#size_limits), [Hyperdisk ML](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-ml#size_limits), and [Hyperdisk Throughput](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-throughput#size_limits).

Hyperdisk type | IOPS limit | Throughput limit (MiB/s)  
---|---|---  
Hyperdisk Balanced | 160,000 | 2,400  
Hyperdisk Balanced High Availability | 100,000 | 2,400  
Hyperdisk Extreme | 350,000 |  You can't provision a throughput level for Hyperdisk Extreme volumes. Each volume gets 250 MiB/s of throughput with every 1,000 IOPS, up to 5,000 MiB/s.  
Hyperdisk ML | You can't provision an IOPS level, but each MiB/s of provisioned throughput comes with 16 IOPS, up to 33,554,432 IOPS. | 2,097,152  
Hyperdisk Throughput | You can't provision an IOPS level, but each MiB/s of provisioned throughput comes with 4 IOPS, up to 9,600 IOPS. | 2,400  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
