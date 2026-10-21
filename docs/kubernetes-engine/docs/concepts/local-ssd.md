---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/local-ssd/
title: About Local SSD for GKE \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:02:05.002618+00:00
---

# About Local SSD for GKE  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/local-ssd/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  About Local SSD for GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

Local solid-state drives (SSDs) are fixed-size SSD drives, which can be mounted to a single Compute Engine VM. You can use Local SSD on GKE to get highly performant storage that is not persistent (_ephemeral_) that is attached to every node in your cluster. Local SSDs also provide [higher throughput and lower latency than standard disks](https://docs.cloud.google.com/compute/docs/disks/local-ssd#performance).

In version 1.25.3-gke.1800 and later, you can configure a GKE node pool to use Local SSD with an [NVMe interface](https://docs.cloud.google.com/compute/docs/disks/local-ssd#choose_an_interface) for local ephemeral storage or raw block storage.

If you are using GKE with Standard clusters, you can attach Local SSD volumes to nodes when you create node pools. This improves the performance of ephemeral storage for your workloads that use [emptyDir Volumes](https://kubernetes.io/docs/concepts/storage/volumes/#emptydir) or [local PersistentVolumes](https://kubernetes.io/docs/concepts/storage/volumes/#local). You can create node pools with Local SSD within your cluster's [machine type limits](https://docs.cloud.google.com/compute/docs/machine-types) and your project's [quotas](https://docs.cloud.google.com/kubernetes-engine/quotas).

A Local SSD disk is attached to only one [node](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture#nodes). Nodes themselves are ephemeral, meaning a workload can be scheduled onto a different node. To ensure that workloads requiring Local SSDs are scheduled to appropriate nodes, use [node affinity](https://kubernetes.io/docs/tasks/configure-pod-container/assign-pods-nodes-using-node-affinity/). For example, use the node label `cloud.google.com/gke-ephemeral-storage-local-ssd: "true"`.

When you configure Local SSDs, GKE automatically mounts the following directories onto the Local SSD volume for improved performance: `/var/lib/kubelet`, `/var/log/pods`, and `/var/lib/containerd`. This approach helps ensure faster access to critical kubelet data, Pod logs, and container runtime files.

**Note:** Ephemeral Local SSD on Autopilot clusters is not supported by most ComputeClasses. If you need ephemeral storage in your Autopilot clusters, use [generic ephemeral volumes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/generic-ephemeral-volumes) backed by Persistent Disk. Some types of GPU Pods have ephemeral Local SSD enabled by default depending on the GPU type. For more information, see [Request ephemeral storage for Autopilot GPU Pods](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-gpus#ephemeral-request).

For more information on the benefits and limitations of Local SSD, such as performance and the allowed number of SSD disks per machine type, see [Local SSDs](https://docs.cloud.google.com/compute/docs/disks#localssds) in the Compute Engine documentation.

## Why choose Local SSD for GKE

Local SSD is a good choice if your workloads have any of the following requirements:

  * You want to run applications that download and process data, such as AI or machine learning, analytics, batch processing, local caching, and in-memory databases.
  * Your applications have specialized storage needs and you want raw block access on high-performance ephemeral storage.
  * You want to run specialized data applications and want to operate Local SSD volumes like a node level cache for your Pods. You can use this approach to drive better performance for in-memory database applications like Aerospike or Redis.



### Ephemeral storage

We recommend using the `--ephemeral-storage-local-ssd` option to provision Local SSD for [node ephemeral storage](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#local-ephemeral-storage) (this is the default if you are using a [third generation machine series](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/local-ssd#3gen)). This approach puts the emptyDir volumes, container-writable layers, and images that together constitute your node ephemeral storage on Local SSD. The benefits include improved I/O bandwidth than the default Persistent Disk and improved Pod startup times.

Using Local SSD for node ephemeral storage means that boot disk Local SSD volumes are not available for other uses. Don't modify the Local SSD devices such as `/dev/nvme*` directly by using a privileged Daemonset, HostPath, or other mechanism; otherwise, the node may fail. If you need fine grained control over the Local SSD volumes, use the raw block approach instead.

### Block device storage

Block device storage enables random access to data in fixed-size blocks. Some specialized applications require direct access to block device storage because, for example, the file system layer introduces unneeded overhead.

Common scenarios for using block device storage include the following:

  * Databases where data is organized directly on the underlying storage.
  * Software which itself implements some kind of storage service (software-defined storage systems).



In GKE version v1.25.3-gke.1800 and later, you can create clusters and node pools with raw block local NVMe SSDs attached, by using the `--local-nvme-ssd-block` option. You can then customize block storage by formatting a filesystem of choice (such as ZFS or HDFS) and configuring RAID. This option is suitable if you need additional control to run workloads that specifically requires access to block storage backed by Local SSD.

You can also use the block access approach with Local SSD if you want a unified data cache to share data across Pods, and the data is tied to a node lifecycle. To do so, install a DaemonSet with a RAID configuration, format a filesystem, and use a local PersistentVolume to share data across Pods.

## Machine requirements

The way you provision Local SSD for your GKE clusters and node pools depends on your underlying machine type. GKE supports Local SSD volumes on Compute Engine first, second, and third generation [machine series](https://docs.cloud.google.com/compute/docs/machine-resource). Local SSD volumes require machine type `n1-standard-1` or larger. The default machine type, `e2-medium` is not supported. To identify your machine series, use the number in the machine type name. For example, N1 machines are first-generation and N2 machines are second generation. For a list of available machine series and types, see [Machine families resource and comparison guide](https://docs.cloud.google.com/compute/docs/machine-resource#machine_type_comparison) in the Compute Engine documentation.

GKE doesn't support using the [C4N machine series](https://docs.cloud.google.com/compute/docs/network-optimized-machines#c4n_series) with Local SSDs. Local SSD support is available with this machine series in [Preview](https://cloud.google.com/products#product-launch-stages) with Compute Engine.

### First and second generation machine series requirements

To use a first- or second-generation machine series with Local SSD, your cluster or node pool must be running GKE version 1.25.3-gke.1800 or later.

To provision Local SSD on a first or second generation machine series, you specify the number of Local SSD volumes to use with your VM. For a list of machine series and the corresponding allowable number of Local SSDs, see see [Choosing a valid number of Local SSDs](https://docs.cloud.google.com/compute/docs/disks/local-ssd#choose_number_local_ssds) in the Compute Engine documentation.

### Third and fourth generation machine series requirements

If you want to use a third generation machine series with Local SSD, your cluster or node pool must be running one of the following GKE versions or later:

  * 1.25.13-gke.200 to 1.26
  * 1.26.8-gke.200 to 1.27
  * 1.27.5-gke.200 to 1.28
  * 1.28.1-gke.200 to 1.29



If you want to use a fourth generation machine series with Local SSD, your cluster or node pool must be running one of the following GKE versions or later:

  * 1.32.1-gke.1357000



For third and fourth generation machine series, each machine type is pre-configured with either no Local SSD or a fixed amount of Local SSD volumes. You don't specify the number of Local SSD volumes to include. Instead, the Local SSD capacity that's available to your clusters is implicitly defined as part of the VM shape.

For a list of machine series and the corresponding allowable number of Local SSDs, see see [Choosing a valid number of Local SSDs](https://docs.cloud.google.com/compute/docs/disks/local-ssd#choose_number_local_ssds) in the Compute Engine documentation.

## Usage pattern for Local SSD volumes

To use Local SSD volumes in your clusters, follow these general steps:

  1. **Provision a node pool with Local SSD attached** : To create a GKE node pool with attached Local SSDs, pass in either the ephemeral storage or raw block storage parameter when you call the `create cluster` command. Setting the Local SSD parameters creates a GKE node pool with Local SSD attached and configured as local ephemeral storage or raw block storage depending on which parameters you choose. To learn more about options for provisioning Local SSD, see Local SSD parameters.
  2. **Access data from Local SSD volumes** : To use the data from Local SSD volumes, you can use a Kubernetes construct such as emptyDir or local persistent volume. To learn more about these options, see Local SSD access.



## Local SSD parameters on GKE

The following table summarizes the recommended parameters that GKE provides for provisioning Local SSD storage on clusters. You can use the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) to pass in these parameters.

Local SSD type | gcloud CLI command | GKE availability | Local SSD profile  
---|---|---|---  
Ephemeral Storage Local SSD | [`gcloud container clusters create   
--ephemeral-storage-local-ssd`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create#--ephemeral-storage-local-ssd) | v1.25.3-gke.1800 or later |  **Storage technology:** NVMe  **Data shared across pods:** No  **Data lifecycle:** Pod  **Size and need for RAID configuration:** Up to 9 TiB. GKE automatically configures RAID under the hood.  **Format:** File System (Kubernetes emptyDir)  **Kubernetes scheduler integration:** Fully integrated by default. Kubernetes scheduler helps ensure that space on the node is available before placement, and scale nodes if needed.  To learn how to use this API parameter, see [Provision and use Local SSD-backed ephemeral storage](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/local-ssd).  
Local NVMe SSD Block | [`gcloud container clusters create   
--local-nvme-ssd-block`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create#--local-nvme-ssd-block) | v1.25.3-gke.1800 or later |  **Storage technology:** NVMe  **Data shared across pods:** Yes, via Local PVs.  **Data lifecycle:** Node  **Size and need for RAID configuration:** Up to 9 TiB. You need to manually configure RAID for larger sizes.  **Format:** Raw block  **Kubernetes scheduler integration:** No, by default. You need to ensure capacity on nodes and handle noisy neighbors. If you opt-in to local PV, scheduling is integrated.  To learn how to use this API parameter, see [Provision and use Local SSD-backed raw block storage](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/local-ssd-raw).  
  
### Support for existing Local SSD parameters

**Note:** If you have a dependency on the following existing Local SSD parameters, they will continue to work as-is with no changes under their current terms and conditions. To benefit from newer underlying technologies (for example, NVMe as opposed to SCSI), we strongly encourage you to migrate to the recommended Local SSD parameters at your own schedule.

The following table summarizes these existing Local SSD parameters and their recommended substitutes:

Existing Local SSD parameters | gcloud CLI command | Local SSD profile | Recommended GA version of the Local SSD parameters  
---|---|---|---  
Local SSD Count parameter | [`gcloud container clusters create   
--local-ssd-count`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create#--local-ssd-count) |  **Storage technology:** SCSI **Data shared across pods:** Yes, via Local PVs  **Data lifecycle:** Node  **Size and need for RAID configuration:** 375 GiB. You need to manually configure RAID for larger sizes.  **Format:** File System (ext-4)  **Kubernetes scheduler integration:** No by default. You need to ensure capacity on nodes and handle noisy neighbors. If you opt-in to local PV, scheduling is integrated.  | [`gcloud container clusters create   
--ephemeral-storage-local-ssd`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create)  
Ephemeral Storage parameter (beta) | [`gcloud beta container clusters create   
--ephemeral-storage`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/clusters/create#--ephemeral-storage) |  **Storage technology:** NVMe  **Data shared across pods:** No  **Data lifecycle:** Pod  **Size and need for RAID configuration:** Up to 9 TiB. GKE automatically configures RAID under the hood.  **Format:** File System (Kubernetes emptyDir)  **Kubernetes scheduler integration:** Fully integrated by default. Kubernetes scheduler helps ensure that space on nodes is available before placement, and scales nodes if needed.  | [`gcloud container clusters create   
--ephemeral-storage-local-ssd`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create)  
Local SSD Volumes parameter (alpha) | [`gcloud alpha container clusters create   
--local-ssd-volumes`](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/clusters/create#--local-ssd-volumes) |  **Storage technology:** NVMe or SCSI  **Data shared across pods:** No  **Data lifecycle:** Node  **Size and need for RAID configuration:** 375 GiB. You need to manually configure RAID for larger sizes.  **Format:** File system (ext-4) or raw block  **Kubernetes scheduler integration:** No by default, You need to ensure capacity on nodes and handle noisy neighbors.  | [`gcloud container clusters create   
--local-nvme-ssd-block`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create)  
  
## Local SSD access

You can access Local SSD volumes with one of the following methods.

### emptyDir volume

In GKE version v1.25.3-gke.1800 and later, you can use ephemeral storage as an [emptyDir volume](https://kubernetes.io/docs/concepts/storage/volumes/#emptydir) backed by Local SSD, via the `--ephemeral-storage-local-ssd` option. We recommend this approach for most cases, including applications that need high-performance ephemeral scratch space.

GKE lets you [configure a node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/local-ssd#node-pool) to mount node ephemeral storage on Local SSD with an [NVMe interface](https://docs.cloud.google.com/compute/docs/disks/local-ssd#choose_an_interface).

To learn more, see [this example](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/local-ssd#example_ephemeral).

### Local persistent volume

A local persistent volume represents a local disk that is attached to a single node. Local persistent volumes allow you to share Local SSD resources across Pods. Because the local disk is a Local SSD disk, the data is still ephemeral.

We recommend this approach if any of the following run on your cluster:

  * Workloads using [StatefulSets](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/statefulset) and [volumeClaimTemplates](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/statefulset).
  * Workloads that share node pools. Each Local SSD volume can be reserved through a PersistentVolumeClaim, and specific HostPaths are not encoded directly in the Pod specification.
  * Pods that require data gravity to the same Local SSD. A Pod is always scheduled to the same node as its local PersistentVolume.



To learn more, see this [example](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/local-ssd-raw#example_local_pvs) and the open-source Kubernetes [Volumes](https://kubernetes.io/docs/concepts/storage/volumes/#local) documentation.

## Handling host maintenance

Some GKE nodes that use Local SSDs, such as Z3 machine types with more than 18 TiB of attached Titanium SSD, don't support live migration during host maintenance. Instead, the VM stops and restarts in place. For a list of machine families that have specific behaviors during maintenance events, see [About host events](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenanceevents) in the Compute Engine documentation.

Due to the potential for extended node downtime on machine types that restart, you should design your applications for resiliency and expect that Pods will be terminated and rescheduled on other nodes.

Similar to nodes with attached GPUs and TPUs, you can configure your cluster to gracefully manage these maintenance events. The GKE maintenance-handler component automatically detects upcoming maintenance on nodes with Local SSDs. Before maintenance begins, the handler taints the node to prevent new Pods from being scheduled and then safely evicts existing Pods. This allows the Pods to be rescheduled on other available nodes in the cluster and respects any PodDisruptionBudgets you have configured.

For detailed instructions on configuring your workloads to manage these events, see [Manage disruption to GKE nodes that don't live migrate](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/handle-disruption-gpu-tpu).

## Restrictions

  * Your application must gracefully handle losing access to data on Local SSD volumes. Data written to a Local SSD disk does not persist when the Pod or node is deleted, repaired, upgraded, or experiences an unrecoverable error.

The ephemeral storage Local SSD parameter configures Local SSD volumes to have a Pod-based data lifecycle, and the NVMe Local SSD block parameter configures Local SSD volumes to have a Node-based data lifecycle.

If you need persistent storage, we recommend you use a durable storage option (such as [Persistent Disk](https://docs.cloud.google.com/compute/docs/disks), [Filestore](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/filestore-for-gke), or [Cloud Storage](https://docs.cloud.google.com/storage)). You can also use regional replicas to minimize the risk of data loss during cluster lifecycle or application lifecycle operations.

  * Local SSD configuration settings cannot be modified once the node pool is created. You cannot enable, disable, or update the Local SSD configuration for an existing node pool. You have to delete the node pool and re-create a new one to make any changes.

  * Pods using emptyDir transparently use Local SSD; however, this is true for all Pods on all nodes in that node pool. GKE does not support having, in the same node pool, some Pods that use Local SSD emptyDir volumes backed by Local SSD and other Pods that use emptyDir volumes backed by a [node boot disk](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create#--disk-type). If you have workloads that use emptyDir volumes backed by a node boot disk, schedule the workloads on a different node pool.

  * Autopilot clusters and node auto-provisioning only support Local SSDs through [custom ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes)

  * We recommend using the [Local SSD as ephemeral storage](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/local-ssd) for workloads running on storage-optimized [Z3 VMs](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z3_series). Live migration is supported for these machines with the following conditions:

    * Z3 VMs with 18 TiB or less of attached Titanium SSD, but Z3 VMs with more than 18 TiB of Titanium SSD [are terminated](https://docs.cloud.google.com/compute/docs/instances/setting-vm-host-options#available_host_maintenance_properties) during [maintenance events](https://docs.cloud.google.com/compute/docs/instances/live-migration-process#limitations). For more information, see [Maintenance experience for Z3 instances](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z3_maintenance). Because Z3 VMs with more than 18 TiB of Titanium SSD are terminated, data in the Local SSD for the nodes might not be available during maintenance events, and [data recovery isn't assured](https://docs.cloud.google.com/compute/docs/disks/local-ssd#data_persistence) after maintenance. For more information, see [Disk persistence following instance termination](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#disk-persistence).

    * Z4D VMs with 41 TiB or less of attached Titanium SSD, but Z4D VMs with more than 41 TiB of attached Titanium SSD are terminated during maintenance events.




## What's next

  * Learn how to [provision and use Local SSD-backed ephemeral storage](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/local-ssd).
  * Learn how to [provision and use Local SSD-backed raw block storage](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/local-ssd-raw).
  * Learn how to [use dedicated Persistent Disks as ephemeral volumes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/generic-ephemeral-volumes).
  * Learn how to [create Volumes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/volumes).
  * Learn how to [use the Compute Engine persistent disk CSI Driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/gce-pd-csi-driver).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
