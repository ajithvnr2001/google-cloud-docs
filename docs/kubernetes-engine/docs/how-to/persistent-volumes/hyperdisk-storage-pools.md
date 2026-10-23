---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/hyperdisk-storage-pools/
title: Optimize storage performance and cost with Hyperdisk Storage Pools \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:08.569633+00:00
---

# Optimize storage performance and cost with Hyperdisk Storage Pools  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/hyperdisk-storage-pools/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Optimize storage performance and cost with Hyperdisk Storage Pools Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document shows you how to optimize Google Kubernetes Engine (GKE) storage performance and cost in GKE by using Hyperdisk Storage Pools.

For stateful workloads in GKE clusters, use GKE Hyperdisk Storage Pools to optimize storage performance and cost. These pools let you efficiently share storage capacity, throughput, and IOPS across multiple Hyperdisk volumes. Hyperdisk support depends on your nodes' machine types. For more information, see [Machine series support for Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#machine-type-support).

This document is for storage specialists who deploy GKE stateful workloads. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Overview

Storage pools logically group physical storage devices, allowing you to segment your resources. You can provision [Google Cloud Hyperdisks](https://docs.cloud.google.com/compute/docs/disks/hyperdisks) within these Storage Pools essentially creating Hyperdisk Storage Pools. [Hyperdisk Storage Pools](https://docs.cloud.google.com/compute/docs/disks/storage-pools) offer pre-provisioned capacity, throughput, and IOPS that your GKE cluster disks can share.

You can use Hyperdisk Storage Pools to manage your storage resources more efficiently and cost-effectively. This lets you take advantage of efficiency technologies such as deduplication and thin provisioning.

In this guide, you use the `us-east4-c` zone to create the Hyperdisk Balanced Storage Pool and other resources.

## Planning considerations

Consider the following requirements and limitations before provisioning and consuming your Hyperdisk Storage Pool.

### Creating and managing Storage Pools

Following requirements and limitations apply:

  * All the limitations of [Compute Engine Hyperdisk Storage Pools](https://docs.cloud.google.com/compute/docs/disks/storage-pools#sp_limitations) apply.
  * All the limitations of [creating disks in a Hyperdisk Storage Pool](https://docs.cloud.google.com/compute/docs/disks/use-storage-pool-capacity#limitations) apply.
  * The type of Hyperdisk Storage Pool you create determines the type of disks that you can create in the storage pool. See [Types of Hyperdisk Storage Pools](https://docs.cloud.google.com/compute/docs/disks/storage-pools#sp-types).



### Provisioning boot disks in Storage Pools

Following requirements and limitations apply:

  * Provisioning boot disks in Storage Pools is not supported on node pools with [node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-auto-provisioning) enabled.
  * Ensure that the [node locations of the cluster](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create#--node-locations) and [node locations of the node pool](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--node-locations) exactly match the zones of the storage pool.
  * Ensure that the machine type running your Pod supports attaching Hyperdisk Balanced disk type. Hyperdisk Throughput is not supported as a boot disk. See [Hyperdisk Machine type support documentation](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#machine-type-support).
  * You can provision boot disks in Storage Pools only on manually created or updated node pools.



### Provisioning attached disk in Storage Pools

Following requirements and limitations apply:

  * The minimum required GKE version for provisioning attached disks in Storage Pools is 1.29.2-gke.1035000 and later.
  * Ensure that the [Compute Engine Persistent Disk CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/gce-pd-csi-driver) is enabled. The Compute Engine Persistent Disk driver is enabled by default on new Autopilot and Standard clusters and cannot be disabled or edited in Autopilot clusters. To enable the driver, see [Enabling the Compute Engine Persistent Disk CSI Driver on an existing cluster.](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/gce-pd-csi-driver#enabling_the_on_an_existing_cluster)
  * Ensure that the storage pool is in at least one of the node locations of the cluster and node locations of the node pool.
  * You can only provision Hyperdisk Throughput and Hyperdisk Balanced attached disks in Storage Pools. The type of the attached disk must match the type of the Storage Pool. For more information, see [Types of Hyperdisk Storage Pools](https://docs.cloud.google.com/compute/docs/disks/storage-pools#sp-types).
  * Within a StorageClass, only 1 Storage Pool per zone is allowed.
  * Within a StorageClass, all Storage Pools must have the Storage Pool type.
  * Ensure that the machine type running your Pod supports attaching the type of disk you're using from the Storage Pool. For more information, see [Hyperdisk Machine type support](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#machine-type-support).



## Quota

When creating a Hyperdisk Storage Pool, you can configure it with either [standard or advanced provisioning](https://docs.cloud.google.com/compute/docs/disks/storage-pools#provisioning-types) for capacity and performance. If you want to increase the quota for capacity, throughput, or IOPS, request higher quota for the relevant quota filter.

For more information, see [View the quotas for your project](https://docs.cloud.google.com/docs/quotas/view-manage#viewing_all_quota_console) and [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase).

Use the following quota filters for Hyperdisk Balanced Storage Pools:

  * `HDB-STORAGE-POOL-TOTAL-ADVANCED-CAPACITY-per-project-region`: to increase the capacity with Advanced capacity provisioning.
  * `HDB-STORAGE-POOL-TOTAL-ADVANCED-IOPS-per-project-region`: to increase the IOPS with Advanced performance provisioning.
  * `HDB-STORAGE-POOL-TOTAL-ADVANCED-THROUGHPUT-per-project-region`: to increase the throughput with Advanced performance provisioning.
  * `HDB-TOTAL-GB-per-project-region`: to increase the capacity with Standard capacity provisioning.
  * `HDB-TOTAL-IOPS-per-project-region`: to increase the IOPS with Standard performance provisioning.
  * `HDB-TOTAL-THROUGHPUT-per-project-region`: to increase the throughput with Standard performance provisioning.



Use the following quota filters for Hyperdisk Throughput Storage Pools:

  * `HDT-STORAGE-POOL-TOTAL-ADVANCED-CAPACITY-per-project-region`: to increase the capacity with Advanced capacity provisioning.
  * `HDT-STORAGE-POOL-TOTAL-ADVANCED-THROUGHPUT-per-project-region`: to increase the throughput with Advanced performance provisioning.
  * `HDT-TOTAL-GB-per-project-region`: to increase the capacity with Standard capacity provisioning.
  * `HDT-TOTAL-THROUGHPUT-per-project-region`: to increase the throughput with Standard performance provisioning.



For example, if you want to increase the total capacity for Hyperdisk Balanced Storage Pools with Advanced capacity provisioning, per project and per region, request a higher quota for the following filter:

`hdb-storage-pool-total-advanced-capacity-per-project-region`.

## Pricing

See [Hyperdisk Storage Pools pricing ](https://docs.cloud.google.com/compute/docs/disks/storage-pools#pricing) for pricing details.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Review the [supported regions and zones](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced#supported-regions) for creating your Hyperdisk Balanced Storage Pool.



## Create a Hyperdisk Storage Pool

Create a Hyperdisk Storage Pool before you provision boot disks or attached disks in that Storage Pool. For more information, see [Create Hyperdisk Storage Pools](https://docs.cloud.google.com/compute/docs/disks/create-storage-pools).

Make sure you create Storage Pools in one of the [supported zones](https://docs.cloud.google.com/compute/docs/disks/storage-pools#hdbsp-regions).

For example, use the following command to create a Hyperdisk Balanced Storage Pool with Advanced capacity and Advanced performance, and provision 10 TB capacity, 10000 IOPS/s and 1024 MBps throughput in the `us-east4-c` zone:
    
    
    export PROJECT_ID=PROJECT_ID
    export ZONE=us-east4-c
    gcloud compute storage-pools create pool-$ZONE \
      --provisioned-capacity=10tb --storage-pool-type=hyperdisk-balanced \
      --zone=$ZONE --project=$PROJECT_ID --capacity-provisioning-type=advanced \
      --performance-provisioning-type=advanced --provisioned-iops=10000 \
      --provisioned-throughput=1024
    

Replace `PROJECT_ID` with your Google Cloud account project ID.

### Inspect Storage Pool zones

  * For Autopilot clusters and Standard clusters with node auto-provisioning enabled, you can create a Storage Pool in any zone within the cluster's region. If no node pool exists in the zone where you created the Storage Pool, Pods remain in `Pending` state until the GKE Cluster Autoscaler can provision a new node pool in that zone.

  * For Standard clusters without node auto-provisioning, create Storage Pools in your cluster's default node zones as Storage Pools are zonal resources. You can set the node zones of your cluster using the `--node-locations` flag.

    * For zonal clusters, if you don't specify the `--node-locations`, all nodes are created in the cluster's primary zone.
    * For regional clusters, if you don't specify the `--node-locations`, GKE distributes your worker nodes in three randomly chosen zones within the region.



To inspect a cluster's default node zones, run the following command:
    
    
    gcloud container clusters describe CLUSTER_NAME | yq '.locations'
    

Replace `CLUSTER_NAME` with the name of the cluster you'd be creating while provisioning a boot disk or attached disk.

## Provision a GKE boot disk in a Hyperdisk Storage Pool

You can provision a GKE boot disk in a Hyperdisk Storage Pool when doing any of the following:

  * When creating a new GKE cluster
  * When creating a new node pool
  * When updating an existing node pool



### When creating a cluster

To create a GKE cluster with boot disks provisioned in a Storage Pool, use the following command:
    
    
    gcloud container clusters create CLUSTER_NAME \
      --disk-type=DISK_TYPE --storage-pools=STORAGE_POOL,[...] \
      --node-locations=ZONE,[...] --machine-type=MACHINE_TYPE \
      --location=CONTROL_PLANE_LOCATION
    

Replace the following:

  * `CLUSTER_NAME`: Provide a unique name for the cluster you're creating.
  * `DISK_TYPE`: Set this to `hyperdisk-balanced.` If left blank, the disk type defaults to Hyperdisk Balanced.
  * `STORAGE_POOL,[...]`: A comma-separated list of the Storage Pool resource paths (example, `projects/my-project/zones/us-east4-c/storagePools/pool-us-east4-c`) where the cluster's boot disks will be provisioned. Make sure the zones in the Storage Pool resource paths match the zones in `--node-locations`.
  * `ZONE,[...]`: A comma-separated list of zones where your node footprint should be replicated. For regional clusters, you can specify regions instead. All zones must be in the same region as the cluster, specified by the `--location` flag.
  * `MACHINE_TYPE`: The supported machine type you want to use for your nodes.
  * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.



### When creating a node pool

To create a GKE node pool with boot disks provisioned in a Storage Pool, use the following command:
    
    
    gcloud container node-pools create NODE_POOL_NAME \
      --disk-type=DISK_TYPE --storage-pools=STORAGE_POOL,[...] \
      --node-locations=ZONE,[...] --machine-type=MACHINE_TYPE \
      --location=CONTROL_PLANE_LOCATION --cluster=CLUSTER_NAME
    

Replace the following::

  * `NODE_POOL_NAME`: Provide a unique name for the node pool you're creating.
  * `DISK_TYPE`: Set this to `hyperdisk-balanced.` If left blank, the disk type defaults to Hyperdisk Balanced.
  * `STORAGE_POOL,[...]`: A comma-separated list of the Storage Pool resource paths (example, `projects/my-project/zones/us-east4-c/storagePools/pool-us-east4-c`) where the cluster's boot disks will be provisioned. Make sure the zones in Storage Pool resource paths match the values in `--node-locations`.
  * `ZONE,[...]`: A comma-separated list of zones where your node footprint should be replicated. All zones must be in the same region as the cluster, specified by the `-location` flag.
  * `MACHINE_TYPE`: The supported machine type you want to use for your nodes.
  * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.
  * `CLUSTER_NAME`: An existing cluster where you're creating the node pool.



### When updating a node pool

You can use an `update` command to add or replace Storage Pools in a node pool. This command can't be used to remove Storage Pools from a node pool.

To update a GKE node pool so that its boot disks are provisioned in a Storage Pool, use the following command.
    
    
    gcloud container node-pools update NODE_POOL_NAME \
     --storage-pools=STORAGE_POOL,[...] \
     --location=CONTROL_PLANE_LOCATION --cluster=CLUSTER_NAME
    

  * `NODE_POOL_NAME`: The name of an existing node pool which you want to update to use a Storage Pool.
  * `STORAGE_POOL,[...]`: A comma-separated list of existing Storage Pool resource paths (example, `projects/my-project/zones/us-east4-c/storagePools/pool-us-east4-c`). Make sure the zones in the Storage Pool resource paths match the zone of the node pool you're updating.
  * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.
  * `CLUSTER_NAME`: The name of the GKE cluster this node pool belongs to.



This change requires recreating the nodes, which can cause disruption to your running workloads. For details about this specific change, find the corresponding row in the [manual changes that recreate the nodes using a node upgrade strategy without respecting maintenance policies](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managing-clusters#manual-changes-strategy-but-no-respect-policies) table. To learn more about node updates, see [Planning for node update disruptions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managing-clusters#plan-node-disruption).

**Caution:** GKE immediately begins recreating the nodes for this change using the node upgrade strategy, regardless of active maintenance policies. GKE depends on [resource availability](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-upgrades-quota) for the change. Disabling node auto-upgrades [doesn't prevent this change](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades#disable-only-versions). Ensure that your workloads running on the nodes are prepared for disruption before you initiate this change.

## Provision a GKE attached disk in a Hyperdisk Storage Pool

In this section:

  * You create a new GKE cluster with attached disks provisioned in a Storage Pool.
  * Create a StorageClass for dynamically provisioning a [PersistentVolume](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes#persistentvolumes) (PV) when a Pod requests it through a [PersistentVolumeClaim](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes#persistentvolumeclaims) (PVC). In order for a PV to consume the Storage Pool's shared resources, you specify the Storage Pool using the `storage-pools` parameter in your StorageClass. The StorageClass is then used in a PVC to provision the Hyperdisk Balanced volume that will be used by the Pod.
  * Create a PVC to request a PV--a piece of Hyperdisk storage--for a Pod from your GKE cluster. This lets you benefit from the Storage Pool's shared resources.
  * Create a Deployment that uses a PVC to ensure that your application has access to persistent storage even after Pod restarts and rescheduling.



### Create a GKE cluster

Before you begin, review the considerations for provisioning an attached disk.

###  Autopilot 

To create an Autopilot cluster using the gcloud CLI, see [Create an Autopilot cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster).

Example:
    
    
    gcloud container clusters create-auto CLUSTER_NAME --location=CONTROL_PLANE_LOCATION
    

Replace the following:

  * `CLUSTER_NAME`: Provide a unique name for the cluster you're creating.
  * `CONTROL_PLANE_LOCATION`: the Compute Engine [region](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster.



To select a supported machine type, you specify the `cloud.google.com/compute-class: Performance` nodeSelector while creating a Deployment. For a list of Compute Engine machine series available with the Performance compute class, see [Supported machine series](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/performance-pods#supported-machine-series).

###  Standard 

To create a Standard Zonal cluster using the gcloud CLI, see [Creating a zonal cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-zonal-cluster).

To create a Standard Regional cluster using the gcloud CLI, see [Creating a regional cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-regional-cluster).

Example:
    
    
    gcloud container clusters create CLUSTER_NAME --location=CONTROL_PLANE_LOCATION --project=PROJECT_ID --machine-type=MACHINE_TYPE --disk-type="DISK_TYPE"
    

Replace the following:

  * `CLUSTER_NAME`: Provide a unique name for the cluster you're creating.
  * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.
  * `PROJECT_ID`: Your Google Cloud account project ID.
  * `MACHINE_TYPE`: The supported machine type you want to use for your nodes.
  * `DISK_TYPE`: Set this to `hyperdisk-balanced.` If left blank, the disk type defaults to Hyperdisk Balanced.



### Create a StorageClass

In Kubernetes, to indicate that you want your PV to be created inside a Storage Pool, use a StorageClass. To learn more, see [StorageClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes#storageclasses).

To create a new StorageClass with the throughput or IOPS level you want:

  * Use `pd.csi.storage.gke.io` in the provisioner field.
  * Specify the Hyperdisk Balanced storage type.
  * Specify the `storage-pools`parameter with value as a list of specific Storage Pools that you want to use. Each Storage Pool in the list must be specified in the format: `projects/PROJECT_ID/zones/ZONE/storagePools/STORAGE_POOL_NAME.`
  * Optionally, specify the performance parameters `provisioned-throughput-on-create` and `provisioned-iops-on-create.`



Each Hyperdisk type has [default values](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-performance#default-perf) for performance determined by the initial disk size provisioned. When creating a StorageClass, you can optionally specify the following parameters depending on your Hyperdisk type. If you omit these parameters, GKE uses the capacity based disk type defaults.

Parameter | Hyperdisk Type | Usage  
---|---|---  
`provisioned-throughput-on-create` | Hyperdisk Balanced, Hyperdisk Throughput | Express the throughput value in MiB/s using the "Mi" qualifier; for example, if your required throughput is 250 MiB/s, specify `"250Mi"` when creating the StorageClass.  
`provisioned-iops-on-create` | Hyperdisk Balanced, Hyperdisk IOPS | The IOPS value should be expressed without any qualifiers; for example, if you require 7,000 IOPS, specify `"7000"` when creating the StorageClass.  
  
For guidance on allowable values for throughput or IOPS, see [Plan the performance level for your Hyperdisk volume](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/hyperdisk#plan).

Use the following manifest to create and apply a StorageClass named `storage-pools-sc` for dynamically provisioning a PV in the Storage Pool `projects/my-project/zones/us-east4-c/storagePools/pool-us-east4-c`:
    
    
    kubectl apply -f - <<EOF
    apiVersion: storage.k8s.io/v1
    kind: StorageClass
    metadata:
     name: storage-pools-sc
    provisioner: pd.csi.storage.gke.io
    volumeBindingMode: WaitForFirstConsumer
    allowVolumeExpansion: true
    parameters:
     type: hyperdisk-balanced
     provisioned-throughput-on-create: "140Mi"
     provisioned-iops-on-create: "3000"
     storage-pools: projects/my-project/zones/us-east4-c/storagePools/pool-us-east4-c
    EOF
    

By utilizing the `volumeBindingMode: WaitForFirstConsumer` in this StorageClass, the binding and provisioning of a PVC is delayed until a Pod using the PVC is created. This approach helps ensure that the PV is not provisioned prematurely, and there is zone matching between the PV, and the Pod consuming it. If their zones don't match, the Pod remains in a `Pending` state.

### Create a PersistentVolumeClaim (PVC)

Create a PVC that references the `storage-pools-sc` StorageClass that you created.

Use the following manifest to create a PVC named `my-pvc`, with 2048 GiB as the target storage capacity for the Hyperdisk Balanced volume:
    
    
    kubectl apply -f - <<EOF
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
     name: my-pvc
    spec:
     storageClassName: storage-pools-sc
     accessModes:
     - ReadWriteOnce
     resources:
      requests:
       storage: 2048Gi
    EOF
    

### Create a Deployment that uses the PVC

**Best practice** : 

When using Pods with PersistentVolumes, use a workload controller such as a [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) or a [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/).

To ensure that Pods can be scheduled on a node pool with a machine series supporting Hyperdisk Balanced, configure a Deployment with the `cloud.google.com/machine-family` node selector. For more information, see [machine type support for Hyperdisks](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#machine-type-support). You use `c3` machine series in the following sample Deployment.

Create and apply the following manifest to configure a Pod for deploying a Postgres web server using the PVC created in the previous section:

###  Autopilot 

On Autopilot clusters, specify the `cloud.google.com/compute-class: Performance` nodeSelector to provision a Hyperdisk Balanced volume. For more information, see [Request a dedicated node for a Pod](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/performance-pods#one-pod-per-node).
    
    
    kubectl apply -f - <<EOF
    apiVersion: apps/v1
    kind: Deployment
    metadata:
     name: postgres
    spec:
     selector:
      matchLabels:
       app: postgres
     template:
      metadata:
       labels:
        app: postgres
      spec:
       nodeSelector:
        **cloud.google.com/machine-family : c3**
        **cloud.google.com/compute-class : Performance**
       containers:
       - name: postgres
        image: postgres:14-alpine
        args: [ "sleep", "3600" ]
        volumeMounts:
        - name: sdk-volume
         mountPath: /usr/share/data/
       volumes:
       - name: sdk-volume
        persistentVolumeClaim:
         claimName: my-pvc
    EOF
    

###  Standard 

On Standard clusters without node auto-provisioning enabled, make sure a node pool with the specified machine series is up and running before creating the Deployment. Otherwise the Pod fails to schedule.
    
    
    kubectl apply -f - <<EOF
    apiVersion: apps/v1
    kind: Deployment
    metadata:
     name: postgres
    spec:
     selector:
      matchLabels:
       app: postgres
     template:
      metadata:
       labels:
        app: postgres
      spec:
       nodeSelector:
        **cloud.google.com/machine-family : c3**
       containers:
       - name: postgres
        image: postgres:14-alpine
        args: [ "sleep", "3600" ]
        volumeMounts:
        - name: sdk-volume
         mountPath: /usr/share/data/
       volumes:
       - name: sdk-volume
        persistentVolumeClaim:
         claimName: my-pvc
    EOF
    

Confirm that the Deployment was successfully created:
    
    
     kubectl get deployment
    

It might take a few minutes for Hyperdisk instances to complete provisioning and display a `READY` status.

### Confirm if the attached disk is provisioned

  1. Check if your PVC named `my-pvc` has been successfully bound to a PV:
         
         kubectl get pvc my-pvc
         

The output is similar to the following:
         
         NAME     STATUS  VOLUME                   CAPACITY  ACCESS MODES  STORAGECLASS    AGE
         my-pvc    Bound  pvc-1ff52479-4c81-4481-aa1d-b21c8f8860c6  2Ti    RWO      storage-pools-sc  2m24s
         

  2. Check if the volume has been provisioned as specified in your StorageClass and PVC:
         
         gcloud compute storage-pools list-disks pool-us-east4-c --zone=us-east4-c
         

The output is similar to the following:
         
         NAME                   STATUS PROVISIONED_IOPS PROVISIONED_THROUGHPUT SIZE_GB
         pvc-1ff52479-4c81-4481-aa1d-b21c8f8860c6 READY  3000       140           2048
         




## Snapshot and restore attached disks in Storage Pools

Moving disks in or out of a storage pool is not permitted. To move a disk in or out of a storage pool, recreate the disk from a snapshot. For more information, see [Change the disk type](https://docs.cloud.google.com/compute/docs/disks/migrate-to-hyperdisk).

In this section:

  * You write a test file to the disk provisioned in your Pod.
  * Create a volume snapshot and delete the test file from that disk.
  * Restore the snapshot to a new disk within the same Storage Pool, effectively recovering the deleted data.



### Create a test file

To create and verify a test file:

  1. Get the Pod name of the Postgres Deployment:
         
         kubectl get pods -l app=postgres
         

The output is similar to the following:
         
         NAME             READY  STATUS  RESTARTS  AGE
         postgres-78fc84c9ff-77vx6  1/1   Running  0     44s
         

  2. Create a test file `hello.txt` in the Pod:
         
         kubectl exec postgres-78fc84c9ff-77vx6 \
          -- sh -c 'echo "Hello World!" > /usr/share/data/hello.txt'
         

  3. Verify that the test file is created:
         
         kubectl exec postgres-78fc84c9ff-77vx6 \
          -- sh -c 'cat /usr/share/data/hello.txt'
         Hello World!
         




### Create a volume snapshot and delete test file

To create and verify a snapshot:

  1. Create a VolumeSnapshotClass that specifies how the snapshot of your volumes should be taken and managed:
         
         kubectl apply -f - <<EOF
         apiVersion: snapshot.storage.k8s.io/v1
         kind: VolumeSnapshotClass
         metadata:
          name: my-snapshotclass
         driver: pd.csi.storage.gke.io
         deletionPolicy: Delete
         EOF
         

  2. Create a VolumeSnapshot and take the snapshot from the volume that's bound to the `my-pvc` PersistentVolumeClaim:
         
         kubectl apply -f - <<EOF
         apiVersion: snapshot.storage.k8s.io/v1
         kind: VolumeSnapshot
         metadata:
          name: my-snapshot
         spec:
          volumeSnapshotClassName: my-snapshotclass
          source:
           persistentVolumeClaimName: my-pvc
         EOF
         

  3. Verify that the volume snapshot content is created:
         
         kubectl get volumesnapshotcontents
         

The output is similar to the following:
         
         NAME                        READYTOUSE  RESTORESIZE   DELETIONPOLICY  DRIVER         VOLUMESNAPSHOTCLASS  VOLUMESNAPSHOT  VOLUMESNAPSHOTNAMESPACE  AGE
         snapcontent-e778fde2-5f1c-4a42-a43d-7f9d41d093da  false    2199023255552  Delete      pd.csi.storage.gke.io  my-snapshotclass   my-snapshot   default          33s
         

  4. Confirm that the snapshot is ready to use:
         
         kubectl get volumesnapshot \
          -o custom-columns='NAME:.metadata.name,READY:.status.readyToUse'
         

The output is similar to the following:
         
         NAME     READY
         my-snapshot  true
         

  5. Delete the original test file `hello.txt` that was created in the Pod `postgres-78fc84c9ff-77vx6`:
         
         kubectl exec postgres-78fc84c9ff-77vx6 \
           -- sh -c 'rm /usr/share/data/hello.txt'
         




### Restore the volume snapshot

To restore the volume snapshot and data, follow these steps:

  1. Create a new PVC that restores data from a snapshot, and ensures that the new volume is provisioned within the same Storage Pool (`storage-pools-sc`) as the original volume. Apply the following manifest:
         
         kubectl apply -f - <<EOF
         apiVersion: v1
         kind: PersistentVolumeClaim
         metadata:
          name: pvc-restore
         spec:
          dataSource:
           name: my-snapshot
           kind: VolumeSnapshot
           apiGroup: snapshot.storage.k8s.io
          storageClassName: storage-pools-sc
          accessModes:
           - ReadWriteOnce
          resources:
           requests:
            storage: 2048Gi
         EOF
         

  2. Update the existing Deployment named `postgres` so that it uses the newly restored PVC you just created. Apply the following manifest:
         
         kubectl apply -f - <<EOF
         apiVersion: apps/v1
         kind: Deployment
         metadata:
          name: postgres
         spec:
          selector:
           matchLabels:
            app: postgres
          template:
           metadata:
            labels:
             app: postgres
           spec:
            nodeSelector:
             cloud.google.com/machine-family: c3
            containers:
            - name: postgres
             image: google/cloud-sdk:slim
             args: [ "sleep", "3600" ]
             volumeMounts:
             - name: sdk-volume
              mountPath: /usr/share/data/
            volumes:
            - name: sdk-volume
             persistentVolumeClaim:
              claimName: pvc-restore
         EOF
         

  3. Get the name of the newly created Pod that is part of the `postgres` Deployment:
         
         kubectl get pods -l app=postgres
         

The output is similar to the following:
         
         NAME             READY  STATUS    RESTARTS  AGE
         postgres-59f89cfd8c-42qtj  1/1   Running    0     40s
         

  4. Verify that the `hello.txt` file, which was previously deleted, now exists in the new Pod (`postgres-59f89cfd8c-42qtj`) after restoring the volume from the snapshot:
         
         kubectl exec postgres-59f89cfd8c-42qtj \
          -- sh -c 'cat /usr/share/data/hello.txt'
         Hello World!
         

This validates that the snapshot and restore process was successfully completed and that the data from the snapshot has been restored to the new PV that's accessible to the Pod.

  5. Confirm that the volume created from the snapshot is located within the your Storage Pool:
         
         kubectl get pvc pvc-restore
         

The output is similar to the following:
         
         NAME     STATUS  VOLUME                   CAPACITY  ACCESS MODES  STORAGECLASS    AGE
         pvc-restore  Bound  pvc-b287c387-bc51-4100-a00e-b5241d411c82  2Ti    RWO      storage-pools-sc  2m24s
         

  6. Check if the new volume is provisioned as specified in your StorageClass and PVC:
         
         gcloud compute storage-pools list-disks pool-us-east4-c --zone=us-east4-c
         

The output is similar to the following where you can see the new volume `pvc-b287c387-bc51-4100-a00e-b5241d411c82` provisioned in the same storage pool.
         
         NAME                   STATUS PROVISIONED_IOPS PROVISIONED_THROUGHPUT SIZE_GB
         pvc-1ff52479-4c81-4481-aa1d-b21c8f8860c6 READY  3000       140           2048
         pvc-b287c387-bc51-4100-a00e-b5241d411c82 READY  3000       140           2048
         




This configuration helps ensure that the restored volume benefits from the shared resources and capabilities of the pool.

## Migrate existing volumes into a Storage Pool

Use snapshot and restore to migrate volumes that exist outside of a Storage Pool, into a Storage Pool.

Ensure that the following conditions are met:

  * Your new PVC `pvc-restore` references a StorageClass that **does specify** the `storage-pools` parameter, pointing to the Storage Pool you want to move the volume into.
  * The source PV that's being snapshotted should be associated with a PVC with a StorageClass that **doesn't specify** the `storage-pools` parameter.



After you restore from a snapshot into a new volume, you can delete the source PVC and PV.

## Clean up

To avoid incurring charges to your Google Cloud account, delete the storage resources you created in this guide. First delete all the disks within the Storage Pool and then delete the Storage Pool.

### Delete the boot disk

When you delete a node (by scaling down the node pool) or an entire node pool, the associated boot disks are automatically deleted. You can also delete the cluster to automatically delete the boot disks of all node pools within it.

For more information, see:

  * [Scale a node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools#resizing_a_node_pool).
  * [Delete a node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools#deleting_a_node_pool).
  * [Delete a cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deleting-a-cluster).



### Delete the attached disk

To delete the attached disk provisioned in a Hyperdisk Storage Pool:

  1. Delete the Pod that uses the PVC:
         
         kubectl delete deployments postgres
         

  2. Delete the PVC that uses the Hyperdisk Storage Pool StorageClass.
         
         kubectl delete pvc my-pvc
         

Confirm that the PVC `pvc-1ff52479-4c81-4481-aa1d-b21c8f8860c6` has been deleted:
         
         gcloud compute storage-pools list-disks pool-us-east4-c --zone=us-east4-c
         




### Delete the Hyperdisk Storage Pool

Delete the Hyperdisk Storage Pool with the following command:
    
    
    gcloud compute storage-pools delete pool-us-east4-c --zone=us-east4-c --project=my-project
    

## What's next

  * See [Troubleshooting storage in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/storage).
  * Read more about the [Persistent Disk CSI driver on GitHub](https://github.com/kubernetes-sigs/gcp-compute-persistent-disk-csi-driver).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
