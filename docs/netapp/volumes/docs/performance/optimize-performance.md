---
url: https://docs.cloud.google.com/netapp/volumes/docs/performance/optimize-performance/
title: Optimize performance \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:44:37.381010+00:00
---

# Optimize performance  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/performance/optimize-performance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Optimize performance Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how you can optimize Google Cloud NetApp Volumes performance by adjusting volume and client-side configurations. These adjustments enhance throughput, reduce latency, and improve overall data transfer efficiency for your applications.

## Before you begin

Before you make changes to your volumes to optimize performance, review [performance considerations](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/volume-performance-sizing).

## Adjust volume settings

You can optimize performance by adjusting the following volume settings:

  * **Increase volume capacity** : you can increase the capacity of your Premium, Extreme or Standard service level volume to improve maximum achievable volume throughput. For volumes of the Flex File service level, increase storage pool's capacity instead. For the Flex Unified or Flex File custom-performance, increase the storage pool's throughput and IOPS.

  * **Upgrade your service level** : you can move a Premium service level volume to a storage pool with an Extreme service level to improve throughput.

  * **Use manual QoS pools to assign greater throughput** : you can decrease the assigned throughput of larger volumes with low throughput requirements, and increase the throughput of smaller volumes that need higher performance up to the available pool throughput.




Increasing volume capacity and upgrading service levels are both non-disruptive to I/O workloads in process on the volume and don't affect access to the volume in any way.

## Adjust the client

You can improve performance by adjusting the following settings on the client:

  * **Co-locate clients** : latency results are directly impacted by the capabilities and location of the client. For best results, place the client in the same region as the volume or as close as possible. Test the zonal impact by testing latency from a client in each zone and use the zone with the lowest latency.

  * **Configure Compute Engine network bandwidth** : the network capabilities of Compute Engine virtual machines depend on the instance type used. Typically, larger instances can drive more network throughput. We recommend that you select a client virtual machine with an appropriate network bandwidth capability, select the Google Virtual NIC (gVNIC) network interface and enable `Tier_1` performance. For more information, see Compute Engine documentation on [network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).

  * **Optimize your client settings** : for Linux clients, see [Optimize Linux NFS clients](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/optimize-linux-nfs-clients).




## Manual QoS

Manual quality of service (QoS) in NetApp Volumes lets you adjust volume performance to meet workload requirements and control storage costs.

Manual QoS offers the following benefits:

  * **Cost optimization** : scale volume performance within your storage pool capacity to optimize cloud costs.

  * **Instant throughput adjustment** : adjust volume throughput without downtime.

  * **Disaster recovery cost reduction** : lower QoS for replicated volumes to reduce disaster recovery costs for destination pools.

  * **Enhanced performance for clones or caches** : increase performance for clone or cache volumes with small allocated sizes.

  * **Flexible workload management** : use larger storage pools as containers for multiple workloads, adjusting each volume's throughput as needed.




### Considerations

  * You can manage manual QoS using the Google Cloud CLI, NetApp Volumes API, or Terraform. The Google Cloud console isn't supported.

  * Manual QoS is supported for the Flex Unified, Standard, Premium, and Extreme service levels and isn't available for the Flex File service level.




### Set up manual QoS limits

For volumes within a manual QoS storage pool, you can set throughput and capacity independently. The overall throughput of all volumes in a manual QoS pool is limited by the pool's total throughput. Pool throughput is determined by its allocated capacity and service level. For example, a 40 TiB Premium pool can achieve a maximum throughput of 2,560 MiBps at 64 MiBps per TiB, while a 200 TiB Extreme pool can support volumes with a combined throughput of 25,600 MiBps.

**Important:** You can create a new manual QoS pool, or change an existing auto QoS pool to manual. This change is permanent and you can't convert a manual QoS pool back to an auto QoS pool. However, you can move volumes from a manual pool to an auto pool.

Once the manual QoS pool is set up, you can set the required throughput limit for each volume within it. The maximum throughput limit for a single volume is 4.5 GiBps, or 30 GiBps for [large capacity volumes](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/overview#large-capacity-volumes).

The pool and volume commands or APIs display available and assigned throughput values for the pool to help you manage the total throughput. To create a manual QoS pool and define volume throughput, see Create a storage pool and Create a volume.

### Create a storage pool

### gcloud

Create a storage pool using manual QoS:
    
    
        gcloud netapp storage-pools create POOL_NAME \
           --project=PROJECT_ID \
           --location=LOCATION \
           --capacity=CAPACITY \
           --service-level=SERVICE_LEVEL \
           --qos-type=QOS_TYPE \
           --network=name=NETWORK_NAME

Replace the following information:

  * `POOL_NAME`: the name of the pool you want to create. Your pool name must be unique per location.

  * `PROJECT_ID`: the name of the project you want to create the storage pool in.

  * `LOCATION`: the location of the pool you want to create.

  * `CAPACITY`: the capacity of the pool in GiB.

  * `SERVICE_LEVEL`: the service level for your storage pool: Standard, Premium, or Extreme.

  * `QOS_TYPE`: the QoS type of your storage pool: auto or manual.

  * `NETWORK_NAME`: the name of the VPC.




### Edit a storage pool

### gcloud

Edit an existing auto QoS storage pool to use manual QoS:
    
    
        gcloud netapp storage-pools update POOL_NAME \
           --project=PROJECT_ID \
           --location=LOCATION \
           --qos-type=QOS_TYPE

Replace the following information:

  * `POOL_NAME`: the name of the pool you want to update.

  * `PROJECT_ID`: the name of the project.

  * `LOCATION`: the location of the pool.

  * `QOS_TYPE`: the updated QoS type for your storage pool. Only manual configuration is supported.




### Create a volume

### gcloud

Create a volume with specified manual QoS throughput limit using the following command:
    
    
    gcloud netapp volumes create VOLUME_NAME \
      --project=PROJECT_ID \
      --location=LOCATION \
      --storage-pool=STORAGE_POOL \
      --capacity=CAPACITY \
      --protocols=PROTOCOLS \
      --share-name=SHARE_NAME \
      --throughput-mibps=THROUGHPUT_MIBPS

Replace the following information:

  * `VOLUME_NAME`: the name of the volume. This name must be unique per location.

  * `PROJECT_ID`: the name of the project in which to create the volume.

  * `LOCATION`: the location for the volume.

  * `STORAGE_POOL`: the storage pool to create the volume in.

  * `CAPACITY`: the capacity of the volume. It defines the capacity that NAS clients see.

  * `PROTOCOLS`: choose the NAS protocols the volume is exported with. Valid choices are NFSv3, NFSv4, SMB, and the following combinations:

    * `nfsv3,nfsv4`
    * `nfsv3,smb`
    * `nfsv4,smb`

Depending on the protocol type you choose, we recommend that you add the protocol specific parameters like `export-policy` or `smb-settings`.

  * `SHARE_NAME`: the NFS export path or SMB share name of the volume.

  * `THROUGHPUT_MIBPS`: the throughput limit of the volume in MiBps.




For more information about additional optional flags, see [Google Cloud SDK documentation on volume creation](https://docs.cloud.google.com/sdk/gcloud/reference/netapp/volumes/create).

## What's next

Read about [volume migration](https://docs.cloud.google.com/netapp/volumes/docs/migrate/ontap/overview).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
