---
url: https://docs.cloud.google.com/compute/docs/disks/extreme-persistent-disk/
title: Extreme Persistent Disk \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:58:13.385397+00:00
---

# Extreme Persistent Disk  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/extreme-persistent-disk/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Extreme Persistent Disk Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

For high-end performance-critical applications, use Extreme Persistent Disk volumes. Extreme Persistent Disk volumes feature higher maximum IOPS and throughput than other Persistent Disk volumes, and let you provision IOPS and capacity separately. Extreme Persistent Disk is available in all [zones](https://docs.cloud.google.com/compute/docs/regions-zones).

When you create an Extreme Persistent Disk, you can provision 2,500 to 120,000 IOPS. If you need more than 125,000 IOPS, we recommend [Google Cloud Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks). Hyperdisk offers the highest IOPS and throughput in Compute Engine and is available on the latest machine types.

This document explains several restrictions of using Extreme Persistent Disk, considerations for reaching maximum possible performance levels, and how to provision IOPS using the Google Cloud console, the gcloud CLI or REST.

## Before you begin

  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




## Machine shape support

You can use N2, M2 and M3 machine series with Extreme Persistent Disk. N2 VMs require at least 64 vCPUs. The following is a list of machine types that support the maximum performance levels offered by Extreme Persistent Disk:

  * [N2](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n2_series):

    * **`n2-*-64`**
    * **`n2-*-80`**
    * **`n2-*-96`**
    * **`n2-*-128`**
  * [M2](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m2_series):

    * **`m2-*-208`**
    * **`m2-*-416`**
  * [M3](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m3_series):

    * **`m3-*-32`**
    * **`m3-*-64`**



All other machine types are not supported for production use. If you'd like to use an unsupported machine type, we recommend [Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks) instead.

N2 VMs with 64 or 80 vCPUs require the Intel Ice Lake CPU platform to reach the stated performance limits. N2 VMs using Intel Cascade Lake CPU platforms will have slightly lower performance. For more information, see [setting the minimum CPU platform for VM instances](https://docs.cloud.google.com/compute/docs/instances/specify-min-cpu-platform#startinginstancewithmincpuplatform).

## Performance limits for Extreme Persistent Disk

The following table lists the performance limits for the supported machine types.

Machine type | vCPU count | Maximum IOPS | Maximum read throughput (MB/s) | Maximum write throughput (MB/s)  
---|---|---|---|---  
N2 | 64 or 80 on Intel Cascade Lake | 120,000 | 2,200 | 2,200  
64 or more on Intel Ice Lake | 120,000 | 4,000 | 3,000  
M2 | 208 | 40,000 | 2,200 | 1,200  
416 | 40,000 | 2,200 | 1,200  
M3 | 64 or less | 40,000 | 2,200 | 1,200  
128 | 80,000 | 2,200 | 1,700  
  
### Performance limits and workload patterns

To reach the maximum performance levels offered by Extreme Persistent Disk volumes, you must consider the following workload parameters:

  * **I/O size** : Maximum IOPS limits assume that you are using an I/O size of 4 or 8 KB. Maximum throughput limits assume that you are using an I/O size of 1 MB.
  * **Queue length** : Queue length is the number of pending requests for a persistent disk. To reach maximum performance limits, you must tune your queue length according to the I/O size, IOPS, and latency sensitivity of your workload. Optimal queue length varies for each workload, but typically should be larger than 128.
  * **Working set size** : Working set size is the amount of data of a disk being accessed within a short period of time. To achieve optimal performance, limit working set sizes to less than 1.5 TB.
  * **Concurrent use of other persistent disks** : Extreme Persistent Disk volumes share the per-VM maximum IOPS and throughput limits with all other persistent disks attached to the same VM. When monitoring the performance of your Extreme Persistent Disk volumes, take into account any I/O requests that you are sending to other disks attached to the same VM.



## Other restrictions

  * Extreme Persistent Disk volumes are zonal only. You can't create regional Extreme Persistent Disks.
  * You cannot attach multiple VM instances in read-only mode to an Extreme Persistent Disk volume.
  * You cannot [create an image or machine image](https://docs.cloud.google.com/compute/docs/images/create-delete-deprecate-private-images#create_image) from an extreme persistent disk.
  * You can resize an Extreme Persistent Disk only once in a 6 hour period.



## Throughput

For Extreme Persistent Disk volumes, throughput scales with the number of IOPS you provision at a rate of 256 KB of throughput per I/O. However, throughput is ultimately capped by per-instance limits that depend on the number of vCPUs on the VM instance to which your extreme disks are attached.

Throughput for Extreme Persistent Disk volumes isn't full duplex. The maximum throughput limits listed in this document apply to the sum total of read and write throughput.

## Provisioning IOPS

To provision IOPS to match your workload requirements, do the following:

  1. Note the IOPS requirement of your workload.
  2. Determine the IOPS required to fulfill the throughput requirements of your workload. 
     * Required IOPS = throughput in KB per second / 256
  3. Set the provisioned IOPS to the larger of the two numbers.



###  Console 

  1. [Create a new persistent disk](https://docs.cloud.google.com/compute/docs/disks/add-persistent-disk#console).
  2. Under **Disk type** , select **Extreme persistent disk**.
  3. Under **Provisioned IOPS** , select the maximum IOPS limit in the range of 2,500 to 120,000 IOPS. There is a cost associated with the provisioned IOPS.



###  gcloud 

Use the [`gcloud compute disks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/create) to create a new disk and include the following flags:
    
    
    gcloud compute disks create DISK_NAME \
      --size=DISK_SIZE \
      --type=pd-extreme \
      --provisioned-iops=IOPS_LIMIT
    

Replace the following:

  * `DISK_NAME`: the name of the new disk
  * `DISK_SIZE`: the size, in GB, of the new disk. The default disk size for Extreme Persistent Disk volumes is 1,000 GB.
  * `IOPS_LIMIT`: the maximum IOPS limit in the range of 2,500 to 120,000 IOPS. There is a cost associated with the provisioned IOPS.



###  REST 

Use the [`disks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/insert) to create a new disk and include the following flags:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/disks
    
    {
     "name": "DISK_NAME",
     "type": "zones/ZONE/diskTypes/pd-extreme"
     "provisionedIops": "IOPS_LIMIT"
    }
    

Replace the following:

  * `PROJECT_ID`: your project ID
  * `ZONE`: the target zone for the disk
  * `DISK_NAME`: a name for the disk
  * `IOPS_LIMIT`: the maximum IOPS limit in the range of 2,500 to 120,000 IOPS. There is a cost associated with the provisioned IOPS.



## What's next?

  * Review [disk pricing](https://docs.cloud.google.com/compute/disks-image-pricing#disk) information.
  * Review [disk performance metrics](https://docs.cloud.google.com/compute/docs/disks/review-disk-metrics).
  * Learn how to [add an Extreme Persistent Disk volume to your VM](https://docs.cloud.google.com/compute/docs/disks/add-persistent-disk).
  * Learn how to [clone an Extreme Persistent Disk volume](https://docs.cloud.google.com/compute/docs/disks/clone-duplicate-disks).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
