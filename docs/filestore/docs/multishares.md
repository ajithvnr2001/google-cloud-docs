---
url: https://docs.cloud.google.com/filestore/docs/multishares/
title: Filestore multishares for GKE \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:52:34.217563+00:00
---

# Filestore multishares for GKE  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/multishares/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  Filestore multishares for GKE Stay organized with collections  Save and categorize content based on your preferences. 

Filestore multishares for GKE allocates up to 80 [shares](https://docs.cloud.google.com/filestore/docs/creating-instances#instances-and-shares) across a single [enterprise-tier](https://docs.cloud.google.com/filestore/docs/service-tiers#enterprise) instance.

This capability optimizes share usage within your Filestore instances and provides the following benefits:

  * Gives users the control to estimate and set maximum share capacity
  * Optimizes the number of shares per instance
  * Optimizes the use of Filestore instances in their associated GKE storage pools
  * Improves cost



## Why use Filestore multishares for GKE?

A Filestore instance is a fully managed network-attached storage (NAS) system you can use with your GKE instances.

Filestore multishares for GKE combined with the [GKE Filestore CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/filestore-csi-driver), version 1.27, provides the following benefits:

  * Provides a comprehensive view of your [persistent volumes (PVs)](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) as one pool of storage. The driver dynamically creates or deletes Filestore instances as you add, delete, or resize volumes. The driver manages your Filestore instances as one large pool of volumes with common characteristics according to the StorageClass definition, and includes the ability to scale, or backup, each volume separately.

  * Supports [multiwriter access](https://docs.cloud.google.com/filestore/docs/overview#why) for applications that require a shared file system for data.

  * Supports [regional](https://docs.cloud.google.com/filestore/docs/regions) storage resilient to [zone](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones) outages.

  * Supports multiple shares with smaller, more flexible sizing for improved utilization and cost efficiency of each Filestore instance.

  * Allocates up to 80 shares across a single Filestore enterprise-tier instance:

    * Each share maps to a unique persistent volume in GKE.

    * Using GKE StorageClasses, you can restrict maximum share size to 128 GiB, 256 GiB, 512 GiB, or 1024 GiB (1 TiB).

Based on the size specified, the GKE Filestore CSI driver limits the maximum number of shares per Filestore instance, creating a maximum capacity of 80, 40, 20, or 10 shares per instance, respectively.

    * GKE Filestore CSI driver versions 1.23 through 1.26 still support up to 10 shares per enterprise instance.

  * Supports greater flexibility for organizations that require both smaller volumes for multiple clients and multiwriter access across a shared network:

    * Supports an extended share size of 10 GiB to 1 TiB (1024 GiB), or the maximum share size specified.

    * GKE Filestore CSI driver versions 1.23 through 1.26 support share sizes ranging between 100 GiB and 1 TiB.

  * Supports [dynamic volume provisioning](https://kubernetes.io/docs/concepts/storage/dynamic-provisioning/), scaling share and instance capacity up or down as needed:

    * If the application workload exceeds 80 [persistent volume claims (PVCs)](https://kubernetes.io/docs/concepts/storage/persistent-volumes/), the GKE Filestore CSI driver reflexively creates more Filestore instances and allocates the necessary shares dynamically across instances.

    * When you delete a PV, the GKE Filestore CSI driver reclaims the allocated share storage and removes the share. The GKE Filestore CSI driver also deletes the Filestore instance if all associated shares have been deleted.

    * When you create, delete, or edit the capacity of a PV, the GKE Filestore CSI driver adds or reclaims capacity of the associated Filestore instance to accommodate the capacity of all shares. The size of the Filestore instance can fluctuate in increments of 256 GiB.

    * The performance of the underlying Filestore enterprise multishare instance is shared, giving higher throughput for specific GKE PVs when needed.

    * This supports upscaling of PV capacity based on workload demands with near-zero downtime.

  * Supports backward compatibility with instances created using the GKE Filestore CSI driver versions 1.23 (the original version released with multishare capabilities) through version 1.26:

  * Shares on these instances can take advantage of the extended minimum share size of 10 GiB.




## StorageClasses and dynamic volume provisioning

In order to access the Filestore multishares feature, you must first enable the [GKE Filestore CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/filestore-csi-driver), version 1.23 or later. Once enabled, you can take advantage of GKE [StorageClasses](https://kubernetes.io/docs/concepts/storage/storage-classes/) which make use of an automated process called [dynamic volume provisioning](https://kubernetes.io/docs/concepts/storage/dynamic-provisioning/) to effectively manage the lifecycle of your [PVs](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistent-volumes) and [PVCs](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims).

The GKE Filestore CSI driver creates StorageClasses to meet your specific needs. The following table compares Filestore enterprise multishare performance in contrast with single share options:

Service tier | GKE StorageClass | Number of shares per instance | GKE PVC size | Filestore capacity | Incremental change | Deployment | Access mode  
---|---|---|---|---|---|---|---  
Basic HDD | `standard-rwx` | One | 100 GiB to 64 TiB | 100 GiB to 64 TiB | 1 GiB | Zonal | read/write many  
Basic SSD | `premium-rwx` | One | 2.5 TiB to 64 TiB | 2.5 TiB to 64 TiB | 1 GiB | Zonal | read/write many  
Enterprise | `enterprise-rwx` | One | 1 TiB to 10 TiB | 1 TiB to 10 TiB | 256 GiB | Regional | read/write many  
Enterprise with the multishares feature | `enterprise-multishare-rwx` | Up to 80 | 10 GiB to 1 TiB | Pool of Filestore instances, each 1 TiB to 10 TiB in size    
Each Filestore instance hosts up to  
80 PVs (shares), each 10 GiB to 1 TiB in size | 256 GiB per instance    
1 GiB per PVC (share)  | Regional | read/write many  
  
For a more detailed comparison of service tier options, see [Service tiers](https://docs.cloud.google.com/filestore/docs/service-tiers).

## How it works

Using GKE Filestore CSI driver version 1.27 and the `max-volume-size` StorageClass parameter, you have greater control to set a maximum share size. Referencing this value, the driver restricts the number of shares allowed on the instance.

To implement this capability, [create a new StorageClass](https://docs.cloud.google.com/filestore/docs/optimize-multishares#create_a_custom_storageclass) and include the parameter in your configuration file, assigning it one of the four accepted values listed in the first column:

Maximum volume size (share size) | Maximum number of shares per instance  
---|---  
128 GiB | 80  
256 GiB | 40  
512 GiB | 20  
1024 GiB (1 TiB) | 10  
  
If you want to restrict share size to 128 GiB, use the key-value pair `max-volume-size: "128Gi"`.

If a value is not specified for the `max-volume-size` parameter, or the parameter is omitted altogether, the driver assigns a default value of 1024 GiB per share. This effectively sets a maximum count of 10 shares on the instance. For a detailed example, see [Optimize multishares](https://docs.cloud.google.com/filestore/docs/optimize-multishares#create_a_custom_storageclass).

### Backward compatibility

The latest multishare feature supports backward compatibility with instances created using GKE Filestore CSI driver versions 1.23 (the original version released with multishare capabilities) through version 1.26:

  * Existing instances can create new PVCs, or shares, with the extended minimum size constraint. As a result, share size now ranges from 10 GiB to 1024 GiB (1 TiB) per share.

  * GKE Filestore CSI driver version 1.27 recognizes legacy enterprise instances and assigns them a default maximum share size limit of 1024 GiB. This means legacy instances are limited to no more than 10 shares per instance.




#### Legacy instance example

As an example, say you install GKE Filestore CSI driver version 1.25 and create a StorageClass labeled `enterprise-multishare-rwx`. You then provision a 1 TiB enterprise-tier instance, labeled F1, mapped to a single 100 GiB share. The driver references instance specifications noted in the StorageClass for this request.

You then upgrade the GKE Filestore CSI driver to version 1.27, and later provision ten new 10 GiB shares.

The StorageClass configuration file used to create F1 does not include the `max-volume-size` parameter and so the driver recognizes instance F1 as a legacy instance, assigning a default maximum share size of 1024 GiB for all new shares mapped to the instance. The driver then references this value on future requests that might include the instance. The new minimum share size of 10 GiB is also available.

Regarding the provision request for ten 10 GiB PVCs, nine are mapped to F1, and then a second instance, F2, is created to provision the final 10 GiB share.

Notice that the driver first recognizes the maximum allowed share size, and then uses that value to determine the maximum share count that can be mapped to a Filestore instance. Once an instance's maximum share count is met, new instances are created, if needed, to fill a provision request.

## Monitoring

For information on how to monitor instance performance, see [Monitoring instances and quota](https://docs.cloud.google.com/filestore/docs/monitoring-instances).

## Feature limitations

The following limitations apply:

  * The Filestore multishare feature is limited to the Filestore enterprise service tier.

  * GKE StorageClasses are immutable. Maximum share size should be chosen carefully.

If you need to change the maximum share size for your Filestore instances, you must create a new custom StorageClass with the updated size, create new instances, and then copy and move your data over.

  * Each Filestore enterprise instance can host up to 80 shares or GKE PVs. Exceeding 80 PVCs triggers the GKE Filestore CSI driver to create more Filestore instances and allocate those shares dynamically across instances. Creating a new Filestore share or PV may, in some circumstances, take extra time. If your application requires immediate PV provisioning, include the following specification in the StorageClass YAML file:

`volumeBindingMode: Immediate`

  * [Snapshots](https://docs.cloud.google.com/filestore/docs/snapshots) are not yet supported for Filestore multishares. If needed, you can use a [single share Filestore StorageClass](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/filestore-csi-driver#storage-class) to manually create snapshots through the Filestore API.

  * Multishare instances and associated shares can take several minutes to create and are not visible until create operations are complete.

  * Some PV delete operations can take significant time to finish. [PV create](https://docs.cloud.google.com/filestore/docs/csi-driver#create) or [PV expand](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/volume-expansion) operations initiated by PVCs defined by the same StorageClass may be blocked during this time.

  * The GKE Filestore CSI driver is supported for clusters using Linux.

  * If you anticipate workloads with higher metadata overhead, we recommend setting a maximum share size that can accommodate your application's capacity needs.

For example, say you provision a Filestore enterprise multishare instance, allowing a maximum size of 256 GiB per share, resulting in a set maximum limit of 40 shares on the instance.

For example, say a share on the instance experiences failed write operations, and in reviewing the instance's [free raw capacity percent metric](https://docs.cloud.google.com/filestore/docs/monitoring-instances#metric_definitions) in Metrics Explorer, you see that the instance lacks suitable capacity. We recommend you configure new multishare instances with a larger share size, say 512 GiB, to meet your workload needs. Note that this results in fewer allowed shares on the instance, in this example, 20.

  * The maximum share size values are limited to 128 GiB, 256 GiB, 512 GiB, or 1024 GiB (1 TiB).

  * For workloads that require shares 1 TiB in size, use a single share per instance.




## Pricing

Once billing is enabled, charges apply based on the underlying Filestore enterprise service tier. With shared capacity across multiple smaller volumes, users can benefit from a significant reduction in storage costs.

For more information see [Enterprise tier](https://docs.cloud.google.com/filestore/docs/service-tiers#enterprise) and [Allocating capacity](https://docs.cloud.google.com/filestore/docs/creating-instances).

## What's next

  * [Optimize storage with Filestore multishares for GKE](https://docs.cloud.google.com/filestore/docs/optimize-multishares).
  * [Use the GKE Filestore CSI Driver.](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/filestore-csi-driver)
  * [Use the GKE Filestore CSI Driver with Shared VPC.](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/filestore-csi-xpn)
  * [Create a GKE StorageClass](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/filestore-csi-driver#storage-class).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
