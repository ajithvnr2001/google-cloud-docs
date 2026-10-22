---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-node-sizes/
title: About GKE node sizing \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:00:35.087944+00:00
---

# About GKE node sizing  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-node-sizes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  About GKE node sizing Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page describes how to plan the size of nodes in Google Kubernetes Engine (GKE) Standard node pools to reduce the risk of workload disruptions and out-of-resource terminations.

This planning is not required in GKE Autopilot because Google Cloud manages the nodes for you. However, this document helps Autopilot cluster operators who want to understand how much of the resource capacity in a node is available for your workloads to use.

## Benefits of right-sized nodes

Ensuring that your nodes are correctly sized to accommodate your workloads and to handle spikes in activity provides benefits such as the following:

  * Better workload reliability because of a reduced risk of out-of-resource eviction.
  * Improved scalability for scaling workloads during high-traffic periods.
  * Lower costs because nodes aren't too large for your needs, which might result in wasted resources.



## Node allocatable resources

GKE nodes run system components that let the node function as a part of your cluster. These components use node resources, such as CPU and memory. You might notice a difference between your node's total resources, which are based on the size of the underlying Compute Engine instance, and the resources that are _available_ for your GKE workloads to request. This difference is because GKE reserves a predefined quantity of resources for system functionality and node reliability. The disk space that GKE reserves for system resources differs based on the [node image](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images#available_node_images). The remaining resources that are available for your workloads are called _allocatable resources_.

When you define Pods in a manifest, you can specify resource _requests_ and _limits_ in the Pod specification. When GKE places the Pods on a node, the Pod requests those specified resources from the allocatable resources on the node. When planning the size of the nodes in your node pools, you should consider how many resources your workloads need to function correctly.

**Warning:** [Hostpath volumes](https://kubernetes.io/docs/concepts/storage/volumes/#hostpath) and the host compute instance system use the same disk. This capacity is shared with system usage such as container images and the kubelet. If this disk becomes full, the system may evict workloads or become unstable. To learn more, see [Node pressure eviction](https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/) in the open source Kubernetes documentation.

### Check allocatable resources on a node

To inspect the allocatable resources on an existing node, run the following command:
    
    
    kubectl get node NODE_NAME \
        -o=yaml | grep -A 7 -B 7 capacity
    

Replace `NODE_NAME` with the name of the node.

The output is similar to the following:
    
    
    allocatable:
      attachable-volumes-gce-pd: "127"
      cpu: 3920m
      ephemeral-storage: "47060071478"
      hugepages-1Gi: "0"
      hugepages-2Mi: "0"
      memory: 13498416Ki
      pods: "110"
    capacity:
      attachable-volumes-gce-pd: "127"
      cpu: "4"
      ephemeral-storage: 98831908Ki
      hugepages-1Gi: "0"
      hugepages-2Mi: "0"
      memory: 16393264Ki
      pods: "110"
    

In this output, the values in the `allocatable` section are the allocatable resources on the node. The values in the `capacity` section are the total resources on the node. The units of ephemeral storage are bytes.

## GKE resource reservations

GKE reserves specific amounts of memory and CPU resources on nodes based on the total size of the resource available on the node. Larger machine types run more containers and Pods, so the amount of resources that GKE reserves scales up for larger machines. Windows Server nodes also require more resources than equivalent Linux nodes, to account for running the Windows OS and for the Windows Server components that can't run in containers.

### Memory and CPU reservations

The following sections describe the default memory and CPU reservations based on the machine type.

For Standard node pools running GKE 1.37 or later, you can customize the amount of CPU and memory reserved for system components. For more information, see [System resource reservations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-system-config#system-resource-reservations) ([Preview](https://cloud.google.com/products#product-launch-stages)).

**Note:** This document uses gibibytes (GiB) and mebibytes (MiB) for memory and storage values. However, the Google Cloud console uses gigabytes (GB) and megabytes (MB). This difference in units means that the allocatable capacity values that you see in the Google Cloud console might be different than the values that you calculate using this document.

#### Memory reservations

GKE calculates memory reservations in the following ways, depending on the GKE version that the node pool was created on:

  * If the node pool was created running GKE version 1.37 or later, GKE uses the following formula:
        
        MemoryReserved = Min(EarlierMemoryReservation, (15 MiB * MaxPodsPerNode) + BaseOverhead)
        

GKE uses the lower of a calculation that factors Pod density, or `EarlierMemoryReservation`, which is the reservation calculation for node pools created running 1.36 or earlier.

In this formula, the value of `BaseOverhead` depends on the node configuration, as follows:

    * **Container-Optimized OS node image** : 500 MiB
    * **Ubuntu node image** : 700 MiB
    * **Image streaming enabled** : an additional buffer, as described in [Memory reservation for Image streaming](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/image-streaming#memory-reservation).

An additional 100 MiB of memory is reserved for Pod eviction thresholds.

  * If the node pool was created running GKE version 1.36 or earlier, GKE uses the following formula. GKE uses this formula even if the node pool is later upgraded to version 1.37 or later:

    * 255 MiB for machines with less than 1 GiB of memory
    * 25% of the first 4 GiB of memory
    * 20% of the next 4 GiB of memory (up to 8 GiB)
    * 10% of the next 8 GiB of memory (up to 16 GiB)
    * 6% of the next 112 GiB of memory (up to 128 GiB)
    * 2% of any memory greater than 128 GiB
    * An additional 100 MiB of memory for Pod eviction thresholds
    * If Image streaming is enabled, an additional buffer, as described in [Memory reservation for Image streaming](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/image-streaming#memory-reservation).



#### CPU reservations

For node pools that were created on GKE version 1.37 or later, GKE limits the total CPU reservation to 1 vCPU (1000 mCPU) or less for standard, non-fractional compute instances. System components can still burst beyond this limit when needed. The 1 vCPU limit helps ensure that high-core compute instances don't lose multiple cores of allocatable capacity to system reservations. The 1 vCPU limit doesn't apply to node pools that were created on GKE version 1.36 or earlier. GKE calculates CPU reservations by using the following formula:

  * 6% of the first core
  * 1% of the next core (up to 2 cores)
  * 0.5% of the next 2 cores (up to 4 cores)
  * 0.25% of any cores greater than 4 cores



For [shared-core E2 machine types](https://docs.cloud.google.com/compute/docs/general-purpose-machines#sharedcore), GKE still reserves a total of 1060 millicores.

### Local ephemeral storage reservation

GKE provides nodes with local _ephemeral storage_ , backed by locally attached devices such as the node's boot disk or local SSDs. Ephemeral storage has no guarantee of availability, and data in ephemeral storage could be lost if a node fails and is deleted.

GKE reserves a portion of the node's total ephemeral storage as a single file system for the kubelet to use during Pod eviction, and for other system components running on the node. You can allocate the remaining ephemeral storage to your Pods to use for purposes such as logs. To learn how to specify ephemeral storage requests and limits in your Pods, refer to [Local ephemeral storage](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#local-ephemeral-storage).

GKE calculates the local ephemeral storage reservation as follows:
    
    
    EVICTION_THRESHOLD + SYSTEM_RESERVATION
    

The actual values vary based on the size and type of device that backs the storage.

#### Ephemeral storage backed by node boot disk

By default, ephemeral storage is backed by the node boot disk. In this case, GKE determines the value of the eviction threshold as follows:
    
    
    EVICTION_THRESHOLD = 10% * BOOT_DISK_CAPACITY
    

The eviction threshold is always 10% of the total boot disk capacity.

GKE determines the value of the system reservation as follows:
    
    
    SYSTEM_RESERVATION = Min(50% * BOOT_DISK_CAPACITY, 6GiB + 35% * BOOT_DISK_CAPACITY, 100 GiB)
    

The system reservation amount is the **lowest** of the following:

  * 50% of the boot disk capacity
  * 35% of the boot disk capacity + 6 GiB
  * 100 GiB



For example, if your boot disk is 300 GiB, the following values apply:

  * 50% of capacity: 150 GiB
  * 35% of capacity + 6 GiB: 111 GiB
  * 100 GiB



GKE would reserve the following:

  * System reservation: 100 GiB (the lowest value)
  * Eviction threshold: 30 GiB



The total reserved ephemeral storage is 130 GiB. The remaining capacity, 170 GiB, is allocatable ephemeral storage.

#### Ephemeral storage backed by local SSDs

If your ephemeral storage is backed by [local SSDs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/local-ssd), GKE calculates the eviction threshold as follows:
    
    
    EVICTION_THRESHOLD = 10% * SSD_NUMBER * 375 GiB
    

In this calculation, `SSD_NUMBER` is the number of attached local SSDs. All local SSDs are 375 GiB in size, so the eviction threshold is 10% of the total ephemeral storage capacity. Note this is computed before the drives are formatted, so the usable capacity is several percent less, depending on node image versions.

GKE calculates the system reservation depending on the number of attached SSDs, as follows:

Number of local SSDs | System reservation (GiB)  
---|---  
1 | 50 GiB  
2 | 75 GiB  
3 or more | 100 GiB  
  
## Use resource reservations to plan node sizes

  1. Consider the resource requirements of your workloads at deploy time and under load. This includes the requests and planned limits for the workloads, as well as overhead to accommodate scaling up.

  2. Consider whether you want a small number of large nodes or a large number of small nodes to run your workloads.

     * A small number of large nodes works well for resource-intensive workloads that don't require high availability. Node autoscaling is **less agile** because more Pods must be evicted for a scale-down to occur.
     * A large number of small nodes works well for highly-available workloads that aren't resource intensive. Node autoscaling is **more agile** because fewer Pods must be evicted for a scale-down to occur.
  3. Use the [Compute Engine machine family comparison guide](https://docs.cloud.google.com/compute/docs/machine-resource#machine_type_comparison) to determine the machine series and family that you want for your nodes.

  4. Consider the ephemeral storage requirements of your workloads. Is the node boot disk enough? Do you need local SSDs?

  5. Calculate the _allocatable resources_ on your chosen machine type using the information in the previous sections. Compare this to the resources and overhead that you need.

     * If your chosen machine type is too large, consider a smaller machine to avoid paying for the extra resources.
     * If your chosen machine type is too small, consider a larger machine to reduce the risk of workload disruptions.



## What's next

  * [Choose a machine type for a node pool](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--machine-type)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
