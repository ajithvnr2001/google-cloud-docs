---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/local-ssd/
title: Provision and use Local SSD-backed ephemeral storage \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:02:05.264830+00:00
---

# Provision and use Local SSD-backed ephemeral storage  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/local-ssd/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Provision and use Local SSD-backed ephemeral storage Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page explains how to provision Local SSD storage on Google Kubernetes Engine (GKE) clusters, and how to configure workloads to consume data from Local SSD-backed ephemeral storage attached to nodes in your cluster.

**Note:** Local SSD volumes require machine type `n1-standard-1` or larger; the default machine type, `e2-medium` is not supported. You can learn more about [machine types](https://docs.cloud.google.com/compute/docs/machine-types) in the Compute Engine documentation.

To learn more about Local SSD support on GKE, see [About Local SSD storage](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/local-ssd#emptydir-volume).

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



## Create a cluster or node pool with Local SSD-backed ephemeral storage

Use the Google Cloud CLI to create a cluster or node pool with Local SSD-backed ephemeral storage.

Use the `--ephemeral-storage-local-ssd` option to attach fully-managed [local ephemeral storage](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#local-ephemeral-storage) backed by Local SSD volumes. This storage is tied to the lifecycle of your Pods. When your Pods request ephemeral storage, GKE schedules them to run on nodes that have Local SSD volumes configured as ephemeral storage. If you want more specialized or granular control over your Local SSDs, we recommend using [Local SSD-backed raw block storage](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/local-ssd-raw#cluster) instead.

If you have [cluster autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-autoscaler) enabled, GKE autoscales your nodes when the cluster needs more ephemeral storage space. Your Pods can access data on Local SSD volumes through the [`emptyDir`](https://kubernetes.io/docs/concepts/storage/volumes/#emptydir) volume.

**Note:** If you were using the `--local-ssd-count` option during the Preview, we strongly encourage switching to the `--ephemeral-storage-local-ssd` option instead to take advantage of more performant storage backed by NVMe.

The gcloud CLI command you run to create the cluster or node pool depends on which [machine series generation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/local-ssd#machine) of your selected machine type. For example, N1 and N2 machine types belong to a first and second generation machine series respectively, while C3 machine types belong to a third generation machine series.

### Create a cluster with Local SSD

### 1st or 2nd Generation

If you are using a machine type from a first or second generation machine series, create your cluster by specifying the `--ephemeral-storage-local-ssd count=NUMBER_OF_DISKS` option. This option provisions the specified number of [Local SSD volumes](https://docs.cloud.google.com/compute/docs/disks/local-ssd) on each node to use for kubelet ephemeral storage.

These settings apply to the default node pool only. If subsequent node pools need Local SSD, specify that during node pool creation.

To create a cluster running on GKE version 1.25.3-gke.1800 or later in which the default pool uses Local SSD volumes, run the following command:
    
    
    gcloud container clusters create CLUSTER_NAME \
        --ephemeral-storage-local-ssd count=NUMBER_OF_DISKS \
        --machine-type=MACHINE_TYPE \
        --release-channel CHANNEL_NAME
    

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster.
  * `NUMBER_OF_DISKS`: the number of Local SSD volumes to provision on each node. These volumes are combined into a single logical volume during node setup. The maximum number of volumes [varies by machine type and region](https://docs.cloud.google.com/compute/docs/disks#local_ssd_machine_type_restrictions). Note that some Local SSD capacity is [reserved for system use](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-node-sizes#local_ephemeral_storage_reservation).
  * `MACHINE_TYPE`: the machine type to use. This field is required, as Local SSD cannot be used with the default `e2-medium` type.
  * `CHANNEL_NAME`: a [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels) that includes GKE versions later than 1.25.3-gke.1800. If you prefer not to use a release channel, you can also use the `--cluster-version` flag instead of `--release-channel`, specifying a valid version later than 1.25.3-gke.1800. To determine the valid versions, use the `gcloud container get-server-config` command.



### 3rd or 4th Generation

If you use a machine type from a third or fourth generation machine series, you don't need to specify any Local SSD options when creating a cluster. The [number of disks](https://docs.cloud.google.com/compute/docs/disks/local-ssd#choose_number_local_ssds) attached to each node depends on the machine type.

To create a cluster, run the following command:
    
    
    gcloud container clusters create CLUSTER_NAME \
      --machine-type=MACHINE_TYPE \
      --cluster-version CLUSTER_VERSION
    

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster.
  * `MACHINE_TYPE`: the machine type to use from a third or fourth generation machine series.
  * `CLUSTER_VERSION`: a [GKE cluster version](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/local-ssd#3gen) that supports Local SSD on machines types from a third or fourth generation machine series.



### Create a node pool with Local SSD

### 1st or 2nd Generation

To create a node pool running on GKE version 1.25.3-gke.1800 or later that uses Local SSD volumes, run the following command:
    
    
    gcloud container node-pools create POOL_NAME \
        --cluster=CLUSTER_NAME \
        --ephemeral-storage-local-ssd count=NUMBER_OF_DISKS \
        --machine-type=MACHINE_TYPE
    

Replace the following:

  * `POOL_NAME`: the name of your new node pool.
  * `CLUSTER_NAME`: the name of the cluster.
  * `NUMBER_OF_DISKS`: the number of Local SSD volumes to provision on each node. These volumes are combined into a single logical volume during node setup. The maximum number of volumes [varies by machine type and region](https://docs.cloud.google.com/compute/docs/disks#local_ssd_machine_type_restrictions). Note that some Local SSD capacity is [reserved for system use](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-node-sizes#local_ephemeral_storage_reservation).
  * `MACHINE_TYPE`: the machine type to use. This field is required, as Local SSD cannot be used with the default `e2-medium` type.



### 3rd or 4th Generation

If you use a machine type from a third or fourth generation machine series, you do not need to specify any Local SSD options when creating a node pool. The number of volumes attached to each node depends on the machine type.

To create a node pool, run the following command:
    
    
    gcloud container node-pools create POOL_NAME \
      --cluster=CLUSTER_NAME \
      --machine-type=MACHINE_TYPE \
      --node-version NODE_VERSION
    

Replace the following:

  * `POOL_NAME`: the name of the new node pool.
  * `CLUSTER_NAME`: the name of the cluster.
  * `MACHINE_TYPE`: the machine type to use from a third or fourth generation machine series.
  * `NODE_VERSION`: a [GKE node pool version](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/local-ssd#3gen) that supports Local SSD on machines types from a third or fourth generation machine series.



Nodes in the node pool are created with a `cloud.google.com/gke-ephemeral-storage-local-ssd=true` label. You can verify the labels by running the following command:
    
    
    kubectl describe node NODE_NAME
    

## Use Local SSD-backed ephemeral storage with Autopilot clusters

You can use Local SSDs for ephemeral storage when you configure your Pods in one of the following ways:

  * You explicitly select a machine series to run your Pods and specify either the `cloud.google.com/gke-ephemeral-storage-local-ssd: "true"` nodeSelector or a capacity reservation that has Local SSDs. To learn more about machine series selection on Autopilot, see [Optimize Autopilot Pod performance by choosing a machine series](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/performance-pods#choose-machine-series).
  * You request a GPU type that supports Local SSDs and specify either the `cloud.google.com/gke-ephemeral-storage-local-ssd: "true"` nodeSelector or a capacity reservation that has Local SSDs. NVIDIA H100 (80GB) GPUs and NVIDIA A100 (80GB) GPUs always use Local SSDs for ephemeral storage, and you can't specify the node selector for those GPUs. To learn more about requesting GPUs on Autopilot, see [Request GPUs in your containers](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-gpus#request-gpus).



See Machine series that support Local SSD in Autopilot for a list of machine series compatible with Local SSDs.

### Request Local SSDs directly in workload manifests

To use Local SSD for ephemeral storage, add the `cloud.google.com/gke-ephemeral-storage-local-ssd: "true"` nodeSelector to your workload manifest. For example, the following Pod manifest selects Local SSDs as ephemeral storage for GPU Pods:
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: l4-localssd-pod
    spec:
      containers:
      - name: my-gpu-container
        image: nvidia/cuda:11.0.3-runtime-ubuntu20.04
        command: ["/bin/bash", "-c", "--"]
        args: ["while true; do sleep 600; done;"]
        resources:
          requests:
            cpu: 16
            memory: 64Gi
            ephemeral-storage: 800Gi
          limits:
           cpu: 16
           memory: 64Gi
           ephemeral-storage: 800Gi
           nvidia.com/gpu: 8
     **** nodeSelector:
        cloud.google.com/gke-accelerator: nvidia-l4
        cloud.google.com/gke-ephemeral-storage-local-ssd: "true"
    

### Request Local SSDs with capacity reservations

If you use a Compute Engine capacity reservation to reserve machines that have Local SSDs, Autopilot attaches available Local SSDs from the reservation to your nodes, and you don't need to explicitly select Local SSDs in the workload manifest. To learn more about using reservations with Autopilot, see [Consume capacity reservations in Autopilot clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/consuming-reservations#consume-capacity-autopilot).

For example, the following Pod manifest selects a specific reservation that has Local SSDs:
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: local-ssd-pod
    spec:
      nodeSelector:
        cloud.google.com/machine-family: MACHINE_SERIES
        **cloud.google.com/reservation-name : localssd-count-reservation
        cloud.google.com/reservation-affinity: "specific"**
      containers:
      - name: my-container
        image: "k8s.gcr.io/pause"
        resources:
          requests:
            cpu: 6
            memory: "25Gi"
            ephemeral-storage: "100Gi"
          limits:
            cpu: 12
            memory: "50Gi"
            ephemeral-storage: "200Gi"
    

Replace `MACHINE_SERIES` with a supported machine series that also supports Local SSDs. If your specified machine series doesn't support Local SSDs, the deployment fails with an error.

**Note:** Autopilot only attaches Local SSDs if the capacity reservation has the "specific" consumption type. You can attach Local SSDs from specific reservations in GKE version 1.32.1-gke.1622000 and later.

### Machine series that support Local SSD in Autopilot

Autopilot clusters support using Local SSDs for ephemeral storage with the following machine series:

Machine series | Supports Local SSD  
---|---  
[C4N machine series](https://docs.cloud.google.com/compute/docs/network-optimized-machines#c4n_series)  
`c4n` |   
[C4D machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4d_series) (1.32.9-gke.1711000 or later)  
`c4d` |   
[C4A machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4a_series) (see [requirements and limitations](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/arm-on-gke#arm-requirements-limitations))  
`c4a` |   
[C4 machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4_series)  
`c4` |   
[C3 machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c3_series)  
`c3` |   
[C3D machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c3d_series)  
`c3d` |   
[C2 machine series](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#c2_series)  
`c2` |  (only with capacity reservation)  
[C2D machine series](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#c2d_series)  
`c2d` |  (only with capacity reservation)  
[H3 machine series](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#h3_series)  
`h3` |   
[Tau T2D machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#t2d_machines)  
`t2d` |   
[Tau T2A machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#t2a_machines)  
`t2a` |   
[E2 machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#e2_machine_types)  
`e2` |   
[N4 machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4_series)  
`n4` |   
[N4D machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4d_series)  
`n4d` |   
[N2 machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n2_series)  
`n2` |  (only with capacity reservation)  
[N2D machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n2d_machines)  
`n2d` |  (only with capacity reservation)  
[N1 machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n1_machines)  
`n1` |  (only with capacity reservation)  
[Z3 machine series](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z3_series)  
`z3` |  (always bundled)  
[Z4D machine series](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z4d_series) (1.36.3-gke.1244000 or later)  
`z4d` |  (always bundled)  
[A2 Standard machine series](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a2-standard-vms)  
`a2-highgpu, a2-megagpu` |  (only with capacity reservation)  
[A2 Ultra machine series](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a2-ultra-vms)  
`a2-ultragpu` |  (always bundled)  
[A3 machine series](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-vms)  
`a3` |  (always bundled)  
[A4 machine series](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4-vms)  
`a4` |  (always bundled)  
[A4X machine series](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4x-vms)  
`a4x` |  (always bundled)  
[G2 machine series](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g2-vms)  
`g2` |   
[G4 machine series](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g4-series)  
`g4` |  (except for the one-eighth GPU configuration, `g4-standard-6`)  
  
## Using the legacy API parameter

The `--local-ssd-count` option is a legacy API parameter that supports SCSI Local SSD. The Compute Engine third generation machine series does not support SCSI and only supports NVMe. You should only use this option with Windows Server clusters. If you are currently using the legacy API parameter on Linux clusters, we recommend that you use the `--ephemeral-storage-local-ssd` option instead.

### Local SSD on Windows Server clusters

**Note:** Local SSD support for Windows Server is only available via the Local SSD count parameter (`gcloud container clusters create --local-ssd-count`).

When you use Local SSD with your [clusters running Windows Server node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-cluster-windows), you need to log in to the node and format the volume before using it. In the following example, the Local SSD volume is formatted with the NTFS file system. You can also create directories under the volume. In this example, the directories are under disk D.
    
    
    PS C:\> Get-Disk | Where partitionstyle -eq 'raw' | Initialize-Disk -PartitionStyle MBR -PassThru | New-Partition -AssignDriveLetter -UseMaximumSize | Format-Volume -FileSystem ntfs -Confirm:$false
    PS C:\> mkdir D:\test-ssd
    

## Access Local SSD volumes

The following example shows how you can access Local SSD-backed ephemeral storage.

### Ephemeral storage as an emptyDir volume

A GKE node pool can be configured to use Local SSD for ephemeral storage, including `emptyDir` volumes.

The following Pod manifest uses an `emptyDir` and a node selector of `cloud.google.com/gke-ephemeral-storage-local-ssd`. You can apply a similar technique for Deployment manifests or StatefulSet manifests.

When choosing the ephemeral storage resource request, take into account the Local SSD capacity [reserved for system use](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-node-sizes#local_ephemeral_storage_reservation).
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: POD_NAME
    spec:
      containers:
        - name: CONTAINER_NAME
          image: "registry.k8s.io/pause"
          resources:
            requests:
              ephemeral-storage: "200Gi"
          volumeMounts:
            - mountPath: /cache
              name: scratch-volume
      nodeSelector:
        cloud.google.com/gke-ephemeral-storage-local-ssd: "true"
      volumes:
        - name: scratch-volume
          emptyDir: {}
    

## Troubleshooting

For troubleshooting instructions, refer to [Troubleshooting storage in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/troubleshooting-gke-storage#local-ssds).

## What's next

  * Learn more about [Local SSD for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/local-ssd).
  * Learn how to [use dedicated Persistent Disks as ephemeral volumes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/generic-ephemeral-volumes).
  * Learn how to [provision and use Local SSD-backed raw block storage](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/local-ssd-raw).
  * Learn more about [storage for GKE clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/storage-overview).
  * Learn more about [GKE node sizing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-node-sizes).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
