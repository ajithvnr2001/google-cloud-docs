---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/hyperdisk/
title: About Hyperdisk for GKE \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:56.667052+00:00
---

# About Hyperdisk for GKE  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/hyperdisk/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  About Hyperdisk for GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

Google Cloud Hyperdisk is a network block storage option offered on GKE. You can use this storage option in your GKE clusters in a similar way as with other Compute Engine Persistent Disk volumes with added flexibility to tune performance for your workload. Compared to Persistent Disk storage, Hyperdisk provides substantially higher maximum input/output operations per second (IOPS) and throughput. Unlike Persistent Disk volumes where performance is shared across all volumes attached to a node, with Hyperdisk, you can specify and tune the level of performance for each Hyperdisk volume.

**Note:** Google Cloud Hyperdisk support is subject to the disks and machine type of your node. Refer to the [Compute Engine documentation](https://docs.cloud.google.com/compute/docs/disks/hyperdisks) for the latest supported machine types, performance limits, and capacity limits per VM.

You can choose from the following Hyperdisk options on GKE:

Storage option | GKE operation mode | Description  
---|---|---  
Hyperdisk Balanced | Autopilot  
Standard | The best fit for most workloads. This is a good option for deploying most enterprise and line-of-business apps, as well as databases and web servers.  
Hyperdisk Throughput | Autopilot  
Standard | Optimized for cost-efficient high-throughput. This is a good option if your use case targets scale-out analytics (for example, Hadoop or Kafka) and throughput-oriented cost-sensitive workloads.  
Hyperdisk Extreme | Autopilot  
Standard | Optimized for IOPS performance. This is a good option if you are deploying high-performance workloads, such as database management systems.  
Hyperdisk ML | Autopilot  
Standard | Optimized for AI/ML training and inference workloads that need to load model weights quickly. Use this option for AI/ML workloads that have high peak read throughput requirements. This is the best option to reduce idleness of GPU/TPU resources when loading data.  
Hyperdisk Balanced High Availability | Autopilot  
Standard | Similar performance level as Hyperdisk Balanced that helps reduce costs with synchronous replication across two zones in a region. Use this option for building workloads that require high availability, or for workloads that require multiple nodes in a region to concurrently write to the same disk.  
  
## Benefits

  * With Hyperdisk, you have more predictable performance on stateful workloads that you deploy.
  * With Hyperdisk, you can provision, manage, and scale your stateful workloads on GKE without the cost and complexity of managing a on-premises storage area network (SAN).
  * Hyperdisk storage capacity is partitioned and made available to GKE nodes as individual volumes. Hyperdisk volumes are decoupled from nodes enabling you to attach, detach, and move volumes between nodes. Data stored in Hyperdisk volumes persist over node reboots and deletions. You can also add multiple Hyperdisk volumes to a single GKE node.



## Pricing

You are billed for the total provisioned capacity of your Hyperdisk volumes until you delete them. You are charged per GiB per month. Additionally, you are billed for the following:

  * Hyperdisk Balanced charges a monthly rate for the provisioned IOPS and provisioned throughput (in MiB/s) in excess of the baseline values of 3,000 IOPS and 140 MiB/s throughput.
  * Hyperdisk Extreme charges a monthly rate based on the provisioned IOPS.
  * Hyperdisk Throughput charges a monthly rate based on the provisioned throughput (in MiB/s).



For pricing information, refer to [Disk pricing](https://docs.cloud.google.com/compute/disks-image-pricing#disk) in the Compute Engine documentation.

## Limitations

  * After volume creation, you can only modify the following settings through the Compute Engine API: 
    * Throughput: Hyperdisk Throughput and Hyperdisk Balanced volumes
    * IOPS: Hyperdisk Extreme and Hyperdisk Balanced volumes
  * You can only attach Hyperdisk volumes to [specific instance types](https://docs.cloud.google.com/compute/docs/machine-resource#machine_type_comparison); Read-Only attachments are not supported.
  * Hyperdisk ML-specific limitations: 
    * Hyperdisk ML can't be used as boot disks.
    * Hyperdisk ML can't be used in multi-writer mode.
    * Hyperdisk ML doesn't support Storage Pools.
  * Hyperdisk Balanced HA-specific limitations: 
    * Hyperdisk Balanced HA cannot be used in Kubernetes [`ReadOnlyMany` mode](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes).
    * Hyperdisk Balanced HA doesn't support snapshots if the volume is in `ReadWriteMany` access mode.
    * Also see the [Limitations](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk#restrictions) section in the Compute Engine documentation on regional disks.
  * See the [Restrictions and Limitations](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#limitations) section in the Compute Engine documentation for additional information.



## Supported node scheduling

You can automatically schedule Hyperdisk based workloads to [supported nodes](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#machine-type-support) with a custom StorageClass. To enable this behavior, create your StorageClass with the `use-allowed-disk-topology: "true"` parameter. To use this feature, the cluster and nodepools must be 1.34.1-gke.2541000 or later. Volumes provisioned with this StorageClass will not schedule on nodepools at lower versions.

The following shows an example of a StorageClass with the feature enabled.
    
    
    apiVersion: storage.k8s.io/v1
    kind: StorageClass
    metadata:
      name: hyperdisk-balanced-compatible-scheduling
    provisioner: pd.csi.storage.gke.io
    volumeBindingMode: WaitForFirstConsumer
    allowVolumeExpansion: true
    parameters:
      type: hyperdisk-balanced
      use-allowed-disk-topology: "true"
    

## Automated disk type selection

In version 1.35.3-gke.1290000 or later, you can specify your preferred disk types for Hyperdisk and Persistent Disk in a StorageClass. GKE automatically selects a disk type for your workloads based on the machine type of the node. This approach lets you create a single StorageClass that supports multiple VM generations, which is necessary when you use [custom ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes) for multi-series capacity fallback. Because newer machine series such as C4, C4D, and N4 support only Hyperdisk and older series such as N2 and N2D support Persistent Disk, a StorageClass pinned to a single disk type can prevent stateful Pods from failing over across machine generations during a zonal resource shortage. With automated disk type selection, you can provision Hyperdisk-compatible machine series like C4, C3, and N4 while falling back to Persistent Disk on machine series like N2D or C2.

To enable automatic disk selection, you set the `parameters.type` field in a StorageClass to a value of `dynamic`. You can specify your preferred disk types by using the following parameters:

Dynamic disk type parameters |   
---|---  
`hyperdisk-type` | The [Hyperdisk type](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/hyperdisk) to use on nodes that support Hyperdisk. If you omit this parameter, the default value is `hyperdisk-balanced`.  
`pd-type` | The [Persistent Disk type](https://docs.cloud.google.com/compute/docs/disks/persistent-disks#disk-types) to use on nodes that support Persistent Disk. If you omit this parameter, the default value is `pd-balanced`.  
`disk-type-preference` | The storage type to use on nodes that support both Hyperdisk and Persistent Disk. Specify one of the following values:

  * `hyperdisk-type`: use Hyperdisk. If you omit the `disk-type-preference` parameter, this is the default value.
  * `pd-type`: use Persistent Disk instead of Hyperdisk.

  
  
You can use any of the other block storage parameters for Hyperdisk and Persistent Disk in the StorageClass. When GKE creates a volume that uses a specific disk type, GKE applies only the parameters that correspond to that type.

**Best practice** : 

Specify the `use-allowed-disk-topology: true` parameter so that GKE schedules Pods only to nodes that support your specified disk types, as described in Supported node scheduling.

The following StorageClass shows how to configure dynamic disk type selection that prioritizes `hyperdisk-balanced` for supported nodes and automatically uses `pd-balanced` for others.
    
    
    apiVersion: storage.k8s.io/v1
    kind: StorageClass
    metadata:
      name: dynamic-volume
    provisioner: pd.csi.storage.gke.io
    volumeBindingMode: WaitForFirstConsumer
    allowVolumeExpansion: true
    parameters:
      type: dynamic
      pd-type: pd-balanced
      hyperdisk-type: hyperdisk-balanced
      use-allowed-disk-topology: "true"
      # The parameters below only apply to the hyperdisk-type and are ignored if
      # the pd-type is selected.
      provisioned-throughput-on-create: "250Mi"
      provisioned-iops-on-create: "3000"
    

## Hyperdisk and Autopilot Compute Classes

If you want to use Hyperdisk on Autopilot clusters that use [Compute Classes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-compute-classes), make sure your node's machine type is both [supported by Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#machine-type-support) and [supported by the Compute Class](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-compute-classes#when-to-use).

The following example shows how you can specify the `nodeSelector` property to control Pod scheduling on Autopilot clusters with the **Performance** Compute Class, when using Hyperdisk Balanced.
    
    
    cloud.google.com/compute-class: "Performance"
    cloud.google.com/machine-family: "c3"
    

For more information, see [Choose Compute Classes for Autopilot Pods](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-compute-classes#request-compute-class).

## Plan the performance level for your Hyperdisk volumes

Use the following considerations to plan the right level of performance for your Hyperdisk volumes.

### Hyperdisk Balanced

With Hyperdisk Balanced, you can provision capacity separately from throughput and IOPS. To provision throughput or IOPS, you select the level for a given volume. Individual volumes have full throughput isolation—each volume can use all the specified throughput or IOPS capacity for that volume. However, the throughput or IOPS is ultimately limited by per-instance limits on the VM instance to which your volumes are attached. To learn more about these limits, see [Provisioned performance for Hyperdisk Balanced](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced#about-provisioned-performance-for-hyperdisk-balanced) in the Compute Engine documentation.

Both read and write operations count against the throughput and IOPS limit provisioned for a Hyperdisk Balanced volume. The throughput or IOPS provisioned and the maximum limits apply to the combined total of read and write operations.

If the total throughput or IOPS provisioned for one or more Hyperdisk volumes exceeds the total throughput or IOPS available at the VM instance level, the performance is limited to the instance performance level.

### Hyperdisk Throughput

With Hyperdisk Throughput, you can provision capacity separately from throughput. To provision throughput, you select the level for a given volume. Individual volumes have full throughput isolation—each gets the throughput provisioned to it. However, the throughput is ultimately capped by per-instance limits on the VM instance to which your volumes are attached. To learn more about these limits, see [About provisioned performance](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-throughput#about_provisioned_performance) in the Compute Engine documentation. Both read and write operations count against the throughput limit provisioned for a Hyperdisk Throughput volume. The throughput provisioned and the maximum limits apply to the combined total of read and write throughput.

When defining a StorageClass, throughput provisioned for Hyperdisk Throughput volumes must follow these rules:

  * At least 10 MiB/s per TiB of capacity, and no more than 90 MiB/s per TiB of capacity, depending on the machine type.
  * At most 600 MiB/s per volume, depending on the machine type.



If the total throughput provisioned for one or more Hyperdisk Throughput volumes exceeds the total throughput available at the VM instance level, the throughput is limited to the instance throughput level.

### Hyperdisk Extreme

With Hyperdisk Extreme, you can provision capacity separately from the IOPS level. To provision the IOPS level, you specify the IOPS limit for a given volume. Individual volumes have full IOPS level isolation—each gets the IOPS level provisioned to it. However, the IOPS is ultimately capped by per-instance limits on the VM instance to which your volumes are attached. To learn more about these limits, see [About provisioned performance](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-extreme#about_provisioned_performance) in the Compute Engine documentation.

Both read and write operations count against the IOPS limit provisioned for a Hyperdisk Extreme volume. The IOPS provisioned, and the maximum limits listed in this document, apply to the total of read and write IOPS.

When defining a StorageClass, IOPS provisioned for Hyperdisk Extreme volumes must be no more than 350,000 IOPS, depending on the machine type.

If the total IOPS provisioned for one or more Hyperdisk Extreme volumes exceeds the total IOPS available at the VM instance level, the performance is limited to the instance IOPS level. If there are multiple Hyperdisk and Persistent Disk volumes attached to the same VM requesting IOPS at the same time, and the VM limits are reached, then each volume has an IOPS level proportional to their share in the total IOPS provisioned across all attached Hyperdisk Extreme volumes.

### Hyperdisk ML

With Hyperdisk ML, you can provision capacity separately from performance. To provision performance, you select the throughput level for a given volume. Individual volumes have full performance isolation—each gets the performance provisioned to it.

When one volume is attached to multiple instances, the provisioned throughput will be dynamically distributed across instances. However, the throughput is ultimately capped by per-instance limits on the VM instance to which your volumes are attached.

Both read and write operations count against the throughput limits provisioned for a Hyperdisk ML volume when in `READ-WRITE-SINGLE` mode. The throughput provisioned and the maximum limits apply to the total of read and write throughput.

Throughput provisioned for Hyperdisk ML volumes must follow the following rules:

  * Minimum: the greater of (0.12 MBps * disk size) in GiB or 400 MBps.
  * Maximum: (1,600 MBps * disk size) in GiB, but not more than 1.2 TBps.
  * If the volume is attached to more than 20 instances in `READ-ONLY-MANY` mode, then the throughput value needs to be at least 100 MBps * number of instances attached.



If the total throughput provisioned for one or more Hyperdisk ML volumes exceeds the total throughput available at the instance level, the performance will be limited to the instance-level performance.

### Hyperdisk Balanced HA

With Hyperdisk Balanced High Availability, you can provision capacity separately from throughput and IOPS. To provision throughput or IOPS, you select the level of throughput and IOPS for a given volume. Individual volumes have full throughput isolation—each volume can use all the specified throughput or IOPS capacity for that volume. However, the throughput or IOPS is ultimately limited by per-instance limits on the VM instance to which your volumes are attached. To learn more about these limits, see [About Google Cloud Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks) in the Compute Engine documentation.

Both read and write operations count against the throughput and IOPS limit that's provisioned for a Hyperdisk Balanced High Availability volume. The provisioned throughput or IOPS and the maximum limits apply to the combined total of read and write operations.

If the total throughput or IOPS that are provisioned for one or more Hyperdisk volumes exceeds the total throughput or IOPS available at the VM instance level, the performance is limited to the instance-level performance.

## What's next

  * [Create a storage class for Hyperdisk Balanced, Throughput, Extreme or Balanced High Availability](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/hyperdisk#create-storageclass).
  * [Create a storage class for Hyperdisk ML](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/hyperdisk-ml).
  * [Learn how to migrate Persistent Disk volumes to Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/migrate-to-hyperdisk#gcloud).
  * [Scale your storage performance using Hyperdisk on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/hyperdisk).
  * [Optimize storage performance and cost with Hyperdisk Storage Pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/hyperdisk-storage-pools).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
