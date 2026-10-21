---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/local-ssd-raw/
title: Provision and use Local SSD-backed raw block storage \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:23:00.620201+00:00
---

# Provision and use Local SSD-backed raw block storage  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/local-ssd-raw/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Provision and use Local SSD-backed raw block storage Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page explains how to provision Local SSD storage on Google Kubernetes Engine (GKE) clusters, and how to configure workloads to consume data from Local SSD-backed raw block storage attached to nodes in your cluster.

Using this Local SSD option gives you more control over the underlying storage and lets you build your own node-level cache for Pods to deliver better performance for your applications. You can also customize this option by installing a file system on Local SSD disks by running a DaemonSet to configure RAID and format disks as needed.

**Note:** Local SSD volumes require machine type `n1-standard-1` or larger; the default machine type, `e2-medium` is not supported. To learn more, see [machine types](https://docs.cloud.google.com/compute/docs/machine-resource) in the Compute Engine documentation.**Warning:** Don't use the Local SSD as raw block storage for your storage-optimized [Z3 VMs](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z3_series), [Z4D VMs](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z4d_series), or [Z4M VMs](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z4m_series). Data in the Local SSD in Z3, Z4D, or Z4M nodes might not be available during [maintenance events](https://docs.cloud.google.com/compute/docs/instances/live-migration-process#limitations), and [data recovery isn't assured](https://docs.cloud.google.com/compute/docs/disks/local-ssd#data_persistence) after maintenance. Instead, use the [Local SSD as ephemeral storage](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/local-ssd) for your workloads running on Z3, Z4D, or Z4M VMs.

To learn more about Local SSD support for raw block access on GKE, see [About local SSDs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/local-ssd#block-access).

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



## Create a cluster or node pool with Local SSD-backed raw block storage

Use the gcloud CLI with the `--local-nvme-ssd-block` option to create a cluster with Local SSD-backed raw block storage.

**Note:** To use Local SSD-backed raw block storage, you must manually configure the devices. Local SSD disks are not formatted for RAID. You are also responsible for ensuring capacity on nodes and handling potential disruptions from co-located workloads. If you use [local PersistentVolume](https://kubernetes.io/docs/concepts/storage/volumes/#local), scheduling is integrated. If you don't need data to persist across the Pod lifecycle, or if you don't have special performance requirements, use the [`--ephemeral-storage-local-ssd`](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/local-ssd) option which should fit most use cases.

The gcloud CLI command you run to create the cluster or node pool depends on which [machine series generation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/local-ssd#machine) the machine type you are using belongs to. For example, N1 and N2 machine types belong to a first and second generation machine series respectively, while C3 machine types belong to a third generation machine series.

### Create a cluster with Local SSD

### 1st or 2nd Generation

If you use a machine type from a first or second generation machine series, you create your cluster by specifying the `--local-nvme-ssd-block count=NUMBER_OF_DISKS` option. The option specifies the number of [Local SSD disks](https://docs.cloud.google.com/compute/docs/disks/local-ssd) to attach to each node. The maximum number [varies by machine type and region](https://docs.cloud.google.com/compute/docs/disks#local_ssd_machine_type_restrictions).

To create a cluster:
    
    
    gcloud container clusters create CLUSTER_NAME \
        --local-nvme-ssd-block count=NUMBER_OF_DISKS \
        --machine-type=MACHINE_TYPE \
        --release-channel CHANNEL_NAME
    

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster.
  * `NUMBER_OF_DISKS`: the number of Local SSD disks to provision on each node. The maximum number of disks [varies by machine type and region](https://docs.cloud.google.com/compute/docs/disks#local_ssd_machine_type_restrictions).
  * `MACHINE_TYPE`: the first or second generation machine type to use. Specifying this field is required, because you can't use Local SSDs with the default `e2-medium` type.
  * `CHANNEL_NAME`: a [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels) that includes GKE versions later than 1.25.3-gke.1800.



### 3rd or 4th Generation

If you use a machine type from a third or fourth generation machine series, use the `--local-nvme-ssd-block` option, without a count field, to create a cluster. GKE automatically provisions Local SSD capacity for your cluster based on the VM shape. The maximum number [varies by machine type and region](https://docs.cloud.google.com/compute/docs/disks#local_ssd_machine_type_restrictions).
    
    
    gcloud container clusters create CLUSTER_NAME \
        --machine-type=MACHINE_TYPE \
        --cluster-version CLUSTER_VERSION \
        --local-nvme-ssd-block
    

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster.
  * `MACHINE_TYPE`: the machine type to use from a third or fourth generation machine series.
  * `CLUSTER_VERSION`: a [GKE cluster version](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/local-ssd#3gen) that supports Local SSD on machines types from a third or fourth generation machine series.



### Create a node pool with Local SSD

### 1st or 2nd Generation

To create a node pool that uses Local SSD disks for raw block access, run the following command:
    
    
    gcloud container node-pools create POOL_NAME \
        --cluster=CLUSTER_NAME \
        --machine-type=MACHINE_TYPE \
        --local-nvme-ssd-block count=NUMBER_OF_DISKS
    

Replace the following:

  * `POOL_NAME`: the name of your new node pool.
  * `CLUSTER_NAME`: the name of the cluster.
  * `MACHINE_TYPE`: the first or second generation machine type to use. Specifying this field is required, as Local SSD cannot be used with the default `e2-medium` type.
  * `NUMBER_OF_DISKS`: the number of Local SSD disks to provision on each node. The maximum number of disks [varies by machine type and region](https://docs.cloud.google.com/compute/docs/disks#local_ssd_machine_type_restrictions).



### 3rd or 4th Generation

If you use a machine type from a third or fourth generation machine series, use the `--local-nvme-ssd-block` option, without a count field, to create a cluster:
    
    
    gcloud container node-pools create POOL_NAME \
        --cluster=CLUSTER_NAME \
        --machine-type=MACHINE_TYPE \
        --node-version NODE_VERSION \
        --local-nvme-ssd-block
    

Replace the following:

  * `POOL_NAME`: the name of the new node pool.
  * `CLUSTER_NAME`: the name of the cluster.
  * `MACHINE_TYPE`: the machine type to use from a third or fourth generation machine type.
  * `NODE_VERSION`: a [GKE node pool version](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/local-ssd#3gen) that supports Local SSD on machine types from a third or fourth generation machine series.



Nodes in the node pool are created with a `cloud.google.com/gke-local-nvme-ssd=true` label. You can verify the labels by running the following command:
    
    
    kubectl describe node NODE_NAME
    

For each Local SSD attached to the node pool, the host OS creates a symbolic link (symlink) to access the disk under an ordinal folder, and a symlink with a universally unique identifier (UUID). For example, if you create a node pool with three local SSDs using the `--local-nvme-ssd-block` option, the host OS creates the following symlinks for the disks:

  * `/dev/disk/by-id/google-local-ssd-block0`
  * `/dev/disk/by-id/google-local-ssd-block1`
  * `/dev/disk/by-id/google-local-ssd-block2`



Correspondingly, the host OS also creates the following symlinks with UUIDs for the disks:

  * `/dev/disk/by-uuid/google-local-ssds-nvme-block/local-ssd-GENERATED_UUID1`
  * `/dev/disk/by-uuid/google-local-ssds-nvme-block/local-ssd-GENERATED_UUID2`
  * `/dev/disk/by-uuid/google-local-ssds-nvme-block/local-ssd-GENERATED_UUID3`



This helps ensure that the disks can be accessed using a unique identifier.

## Access Local SSD volumes

The following example shows how you can access Local SSD-backed raw block storage.

### Local PersistentVolumes

Local SSD volumes can be mounted as Pods using [PersistentVolumes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes).

You can create PersistentVolumes from Local SSD by manually creating a PersistentVolume, or by running the local volume static provisioner.

#### Limitations of local PersistentVolumes

**Note:** When using [release channels](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels), auto-upgrade and auto-repair cannot be disabled. We do not recommend using local PersistentVolumes with clusters in a release channel.

  * [Cluster autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler) and [dynamic provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes#dynamic_provisioning) are not supported with local PersistentVolumes.

  * Upgrading a GKE cluster or repairing nodes deletes the Compute Engine instances, which also deletes all data on the Local SSD disks.

  * Don't enable [node auto-upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-auto-upgrades) or [node auto-repair](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-auto-repair) for clusters or node pools using Local SSD for persistent data. You must back up your application data first, then restore the data to a new cluster or node pool.


**Caution:** Clusters and node pools created with the Google Cloud console have node auto-upgrade enabled by default. To disable, refer to [node auto-upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-auto-upgrades).

  * Local PersistentVolume objects are not automatically cleaned up when a node is deleted, upgraded, repaired, or scaled down. We recommend that you periodically scan and delete stale Local PersistentVolume objects associated with deleted nodes.



#### Manually create the PersistentVolume

You can manually create a PersistentVolume for each Local SSD on each node in your cluster.

Use the `nodeAffinity` field in a PersistentVolume object to reference a Local SSD on a specific node. The following example shows the PersistentVolume specification for Local SSD on nodes running Linux:
    
    
    apiVersion: v1
    kind: PersistentVolume
    metadata:
      name: "example-local-pv"
    spec:
      capacity:
        storage: 375Gi
      accessModes:
      - "ReadWriteOnce"
      persistentVolumeReclaimPolicy: "Retain"
      storageClassName: "local-storage"
      local:
        path: "/mnt/disks/ssd0"
      nodeAffinity:
        required:
          nodeSelectorTerms:
          - matchExpressions:
            - key: "kubernetes.io/hostname"
              operator: "In"
              values:
              - "gke-test-cluster-default-pool-926ddf80-f166"
    

In this example, the Local SSD disks are manually configured for RAID and formatted, then mounted at `/mnt/disks/ssd0` on node `gke-test-cluster-default-pool-926ddf80-f166`. The nodeAffinity field is used to help assign workloads to nodes with Local SSDs that are manually configured for RAID. If you only have one node in your cluster or if you've configured RAID for all nodes, the nodeAffinity field is not needed.

The corresponding PersistenVolumeClaim specification looks like the following:
    
    
      kind: PersistentVolumeClaim
      apiVersion: v1
      metadata:
        name: ssd-local-claim
      spec:
        accessModes:
        - ReadWriteOnce
        storageClassName: local-storage
        resources:
          requests:
            storage: 37Gi
    

If you delete the PersistentVolume, you must manually erase the data from the disk.

#### Run the local volume static provisioner

**Note:** The local volume static provisioner is a community project and not maintained or supported by Google. It also cannot be used with Windows.

You can create PersistentVolumes for Local SSD automatically using the local volume static provisioner. The provisioner is a [DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/) that manages the Local SSD disks on each node, creates and deletes the PersistentVolumes for them, and cleans up the data on the Local SSD disks when the PersistentVolume is released.

To run the local volume static provisioner:

  1. Use a DaemonSet to configure RAID and format the disks:

     1. Download the [`gke-daemonset-raid-disks.yaml`](https://raw.githubusercontent.com/kubernetes-sigs/sig-storage-local-static-provisioner/master/examples/gke-daemonset-raid-disks.yaml) specification.
     2. Deploy the RAID disks DaemonSet. The DaemonSet sets a RAID 0 array on all Local SSD disks and formats the device to an `ext4` filesystem.
            
            kubectl create -f gke-daemonset-raid-disks.yaml
            

  2. Download the [`gke-nvme-ssd-block-raid.yaml`](https://raw.githubusercontent.com/kubernetes-sigs/sig-storage-local-static-provisioner/master/helm/generated_examples/gke-nvme-ssd-block-raid.yaml) specification, and modify the specification's namespace fields as needed.

The specification includes these resources:

     * ServiceAccount for the provisioner
     * ClusterRole and ClusterRoleBindings for permissions to: 
       * Create and Delete PersistentVolume objects
       * Get Node objects
     * ConfigMap with provisioner settings for GKE
     * DaemonSet for running the provisioner
  3. Deploy the provisioner:
         
         kubectl create -f gke-nvme-ssd-block-raid.yaml
         

After the provisioner is running successfully, it creates a PersistentVolume object for the RAID Local SSD device in the cluster.

  4. Save the following PersistentVolumeClaim manifest as `provisioner-pvc-example.yaml`:
         
         kind: PersistentVolumeClaim
         apiVersion: v1
         metadata:
           name: PVC_NAME
         spec:
           accessModes:
           - ReadWriteOnce
           resources:
             requests:
               storage: 50Gi
           storageClassName: nvme-ssd-block
         

Replace `PVC_NAME` with the name of your PersistentVolumeClaim.

  5. Create the PersistentVolumeClaim:
         
         kubectl create -f provisioner-pvc-example.yaml
         

  6. Save the following Pod manifest as `provisioner-pod-example.yaml`:
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: POD_NAME
         spec:
           containers:
           - name: "shell"
             image: "ubuntu:14.04"
             command: ["/bin/sh", "-c"]
             args: ["echo 'hello world' > /cache/test.txt && sleep 1 && cat /cache/test.txt && sleep 3600"]
             volumeMounts:
             - mountPath: /cache
               name: local-ssd-storage
           volumes:
           - name: local-ssd-storage
             persistentVolumeClaim:
               claimName: PVC_NAME
         

Replace `POD_NAME` with the name of your Pod.

  7. Create the Pod:
         
         kubectl create -f provisioner-pod-example.yaml
         




#### Enable delayed volume binding

**Note:** If you followed the instructions to run the local volume static provisioner, its manifest provides an appropriate StorageClass definition. **If you use the local volume static provisioner, you do not need to perform the steps in this section.**

For improved scheduling, we recommend that you also create a StorageClass with `volumeBindingMode: WaitForFirstConsumer`. This delays PersistentVolumeClaim binding until Pod scheduling, so that a Local SSD is chosen from an appropriate node that can run the Pod. This enhanced scheduling behavior considers Pod CPU and memory requests, node affinity, Pod affinity and anti-affinity, and multiple PersistentVolumeClaim requests, along with which nodes have available local SSDs, when selecting a node for a runnable Pod.

This example uses delayed volume binding mode:
    
    
    apiVersion: storage.k8s.io/v1
    kind: StorageClass
    metadata:
      name: "local-nvme"
    provisioner: "kubernetes.io/no-provisioner"
    volumeBindingMode: "WaitForFirstConsumer"
    

To create a StorageClass with delayed binding, save the YAML manifest to a local file and apply it to the cluster using the following command:
    
    
    kubectl apply -f filename
    

## Troubleshooting

For troubleshooting instructions, refer to [Troubleshooting storage in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/troubleshooting-gke-storage#local-ssds).

## What's next

  * [Learn more about node pools](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
