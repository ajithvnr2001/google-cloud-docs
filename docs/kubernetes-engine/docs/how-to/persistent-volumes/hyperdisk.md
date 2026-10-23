---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/hyperdisk/
title: Scale your storage performance with Hyperdisk \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:25.138796+00:00
---

# Scale your storage performance with Hyperdisk  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/hyperdisk/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Scale your storage performance with Hyperdisk Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

The Compute Engine Persistent Disk CSI driver is the primary way for you to access [Hyperdisk storage with Google Kubernetes Engine (GKE) clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/hyperdisk).

**Note:** Hyperdisk support is based on the machine type of your nodes. For the most up-to-date information, see [Machine type support](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#machine-type-support) in the Compute Engine documentation.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Set your default region and zone to one of the [supported values](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#hyperdisk_regions).



### Requirements

To use Hyperdisk volumes in GKE, your clusters must meet the following requirements:

  * Use Linux clusters running GKE version 1.26 or later. If you use a [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels), ensure that the channel has the minimum GKE version or later that is required for this driver. Provisioning Hyperdisk Balanced High Availability volumes requires GKE version 1.33 or later.
  * Make sure that the [Compute Engine Persistent Disk CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/gce-pd-csi-driver) is enabled. The Compute Engine Persistent Disk driver is enabled by default on new Autopilot and Standard clusters and cannot be disabled or edited when using Autopilot. If you need to enable the Compute Engine Persistent Disk CSI driver from your cluster, see [Enabling the Compute Engine Persistent Disk CSI Driver on an existing cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/gce-pd-csi-driver#enabling_the_on_an_existing_cluster).



## Create a Hyperdisk volume for GKE

This section provides an overview of creating a Hyperdisk volume backed by the Compute Engine CSI driver in GKE.

**Note:** When you create the PersistentVolumeClaim associated with the StorageClass, GKE automatically creates the underlying Google Cloud Hyperdisk backing storage and attaches the storage to a node. You don't need to separately create and attach Google Cloud Hyperdisk storage to your nodes.

### Create a StorageClass

The following [Persistent Disk storage `Type` fields](https://docs.cloud.google.com/compute/docs/disks#disk-types) are provided by the Compute Engine Persistent Disk CSI driver to support Hyperdisk:

  * `hyperdisk-balanced`
  * `hyperdisk-throughput`
  * `hyperdisk-extreme`
  * `hyperdisk-ml`
  * `hyperdisk-balanced-high-availability`



To create a new StorageClass with the throughput or IOPS level you want, use `pd.csi.storage.gke.io` in the provisioner field, and specify one of the Hyperdisk storage types.

Each Hyperdisk type has [default values](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-performance#default-perf) for performance determined by the initial disk size provisioned. When creating the StorageClass, you can optionally specify the following parameters depending on your Hyperdisk type. If you omit these parameters, GKE uses the capacity based disk type defaults instead. For guidance on allowable values for throughput or IOPS, see [Plan the performance level for your Hyperdisk volume](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/hyperdisk#plan).

Parameter | Hyperdisk Type | Usage  
---|---|---  
`provisioned-throughput-on-create` | Hyperdisk Balanced*, Hyperdisk Balanced High Availability, Hyperdisk Throughput | Express the throughput value in MiB/s using the "Mi" qualifier; for example, if your required throughput is 250 MiB/s, specify `"250Mi"` when creating the StorageClass.  
`provisioned-iops-on-create` | Hyperdisk Balanced, Hyperdisk Balanced High Availability, Hyperdisk Extreme | The IOPS value should be expressed without any qualifiers; for example, if you require 7,000 IOPS, specify `"7000"` when creating the StorageClass.  
  
* If you need enhanced security and are planning to use Confidential Google Kubernetes Engine Nodes, consider [creating Confidential mode for Hyperdisk Balanced](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/confidential-gke-nodes#creating_chd_pv), review additional [Confidential mode for Hyperdisk Balanced limitations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/confidential-gke-nodes#limitations), and learn more [about Confidential Google Kubernetes Engine Nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/confidential-gke-nodes). 

The following examples show how you can create a StorageClass for each Hyperdisk type:

### Hyperdisk Balanced

  1. Save the following manifest in a file named `hdb-example-class.yaml`:
         
         apiVersion: storage.k8s.io/v1
         kind: StorageClass
         metadata:
           name: balanced-storage
         provisioner: pd.csi.storage.gke.io
         volumeBindingMode: WaitForFirstConsumer
         allowVolumeExpansion: true
         parameters:
           **type : hyperdisk-balanced**
           provisioned-throughput-on-create: "250Mi"
           provisioned-iops-on-create: "7000"
         

  2. Create the StorageClass:
         
         kubectl create -f hdb-example-class.yaml
         




### Hyperdisk Throughput

  1. Save the following manifest in a file named `hdt-example-class.yaml`:
         
         apiVersion: storage.k8s.io/v1
         kind: StorageClass
         metadata:
           name: throughput-storage
         provisioner: pd.csi.storage.gke.io
         volumeBindingMode: WaitForFirstConsumer
         allowVolumeExpansion: true
         parameters:
           **type : hyperdisk-throughput**
           provisioned-throughput-on-create: "50Mi"
         

  2. Create the StorageClass:
         
         kubectl create -f hdt-example-class.yaml
         




### Hyperdisk Extreme

  1. Save the following manifest in a file named `hdx-example-class.yaml`:
         
         apiVersion: storage.k8s.io/v1
         kind: StorageClass
         metadata:
           name: extreme-storage
         provisioner: pd.csi.storage.gke.io
         volumeBindingMode: WaitForFirstConsumer
         allowVolumeExpansion: true
         parameters:
           **type : hyperdisk-extreme**
           provisioned-iops-on-create: "50000"
         

  2. Create the StorageClass:
         
         kubectl create -f hdx-example-class.yaml
         




### Hyperdisk Balanced HA

  1. Save the following manifest in a file named `hdb-ha-example-class.yaml`.

     * For zonal clusters, set the availability zones where you want to create the PersistentVolumes.

     * For regional clusters, you can choose to not set the `allowedTopologies` field to create the PersistentVolumes in two randomly selected availability zones at the time of Pod scheduling.

For more information on supported zones, see [hyperdisk regional availability](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#hyperdisk_regions).
    
    apiVersion: storage.k8s.io/v1
    kind: StorageClass
    metadata:
      name: balanced-ha-storage
    provisioner: pd.csi.storage.gke.io
    volumeBindingMode: WaitForFirstConsumer
    allowVolumeExpansion: true
    parameters:
      **type : hyperdisk-balanced-high-availability**
      provisioned-throughput-on-create: "250Mi"
      provisioned-iops-on-create: "7000"
    allowedTopologies:
    - matchLabelExpressions:
      - key: topology.gke.io/zone
        values:
        - ZONE1
        - ZONE2
    

  2. Create the StorageClass:
         
         kubectl create -f hdb-ha-example-class.yaml
         




To find the name of the StorageClasses available in your cluster, run the following command:
    
    
    kubectl get sc
    

### Create a PersistentVolumeClaim

You can create a PersistentVolumeClaim that references the Compute Engine Persistent Disk CSI driver's StorageClass.

### Hyperdisk Balanced

In this example, you specify the targeted storage capacity of the Hyperdisk Balanced volume as 20 GiB.

  1. Save the following PersistentVolumeClaim manifest in a file named `pvc-example.yaml`:
         
         kind: PersistentVolumeClaim
         apiVersion: v1
         metadata:
           name: podpvc
         spec:
           accessModes:
           - ReadWriteOnce
           storageClassName: balanced-storage
           resources:
             requests:
               storage: 20Gi
         

  2. Apply the PersistentVolumeClaim that references the StorageClass you created from the earlier example:
         
         kubectl apply -f pvc-example.yaml
         




### Hyperdisk Throughput

In this example, you specify the targeted storage capacity of the Hyperdisk Throughput volume as 2 TiB.

  1. Save the following PersistentVolumeClaim manifest in a file named `pvc-example.yaml`:
         
         kind: PersistentVolumeClaim
         apiVersion: v1
         metadata:
           name: podpvc
         spec:
           accessModes:
           - ReadWriteOnce
           storageClassName: throughput-storage
           resources:
             requests:
               storage: 2Ti
         

  2. Apply the PersistentVolumeClaim that references the StorageClass you created from the earlier example:
         
         kubectl apply -f pvc-example.yaml
         




### Hyperdisk Extreme

In this example, you specify the minimum storage capacity of the Hyperdisk Extreme volume as 64 GiB.

  1. Save the following PersistentVolumeClaim manifest in a file named `pvc-example.yaml`:
         
         kind: PersistentVolumeClaim
         apiVersion: v1
         metadata:
           name: podpvc
         spec:
           accessModes:
           - ReadWriteOnce
           storageClassName: extreme-storage
           resources:
             requests:
               storage: 64Gi
         

  2. Apply the PersistentVolumeClaim that references the StorageClass you created from the earlier example:
         
         kubectl apply -f pvc-example.yaml
         




### Hyperdisk Balanced HA

In this example, you specify the minimum storage capacity of the Hyperdisk Balanced High Availability volume as 20 GiB and the access mode as `ReadWriteOnce`. Hyperdisk Balanced High Availability also supports access modes of `ReadWriteMany` and `ReadWriteOncePod`. For differences and use cases of each access mode, see [Persistent Volume Access Modes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes).

  1. Save the following PersistentVolumeClaim manifest in a file named `pvc-example.yaml`:
         
         kind: PersistentVolumeClaim
         apiVersion: v1
         metadata:
           name: podpvc
         spec:
           accessModes:
           - ReadWriteOnce
           storageClassName: balanced-ha-storage
           resources:
             requests:
               storage: 20Gi
         

  2. Apply the PersistentVolumeClaim that references the StorageClass you created from the earlier example:
         
         kubectl apply -f pvc-example.yaml
         




### Create a Deployment to consume the Hyperdisk volume

When using Pods with PersistentVolumes, we recommend that you use a workload controller (such as a [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) or [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/)).

  1. The following example creates a manifest that configures a Pod for deploying a Nginx web server using the PersistentVolumeClaim created in the previous section. Save the following example manifest as `hyperdisk-example-deployment.yaml`:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: web-server-deployment
           labels:
             app: nginx
         spec:
           replicas: 1
           selector:
             matchLabels:
               app: nginx
           template:
             metadata:
               labels:
                 app: nginx
             spec:
               containers:
               - name: nginx
                 image: nginx
                 volumeMounts:
                 - mountPath: /var/lib/www/html
                   name: mypvc
               volumes:
               - name: mypvc
                 persistentVolumeClaim:
                   # Reference the PVC created earlier.
                   claimName: podpvc
                   readOnly: false
         

  2. To create a Deployment based on the `hyperdisk-example-deployment.yaml` manifest file, run the following command:
         
         kubectl apply -f hyperdisk-example-deployment.yaml
         

  3. Confirm the Deployment was successfully created:
         
         kubectl get deployment
         

It might take a few minutes for Hyperdisk instances to complete provisioning. When the deployment completes provisioning, it reports a `READY` status.

  4. You can check the progress by monitoring your PersistentVolumeClaim status by running the following command:
         
         kubectl get pvc
         




## Provision a Hyperdisk volume from a snapshot

To create a new Hyperdisk volume from an existing Persistent Disk snapshot, use the Google Cloud console, the Google Cloud CLI, or the [Compute Engine API](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks). To learn how to create a Persistent Disk snapshot, see [Creating and using volume snapshots](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/volume-snapshots#creating_and_using_a_volume_snapshot).

### Console

  1. Go to the **Disks** page in the Google Cloud console.

[Go to Disks](https://console.cloud.google.com/compute/disks)

  2. Click **Create Disk.**

  3. Under **Disk Type** , choose one of the following for disk type:

     * **Hyperdisk Balanced**
     * **Hyperdisk Extreme**
     * **Hyperdisk Throughput**
     * **Hyperdisk High Availability**
  4. Under **Disk source type** , click **Snapshot**.

  5. Select the name of the snapshot to restore.

  6. Select the size of the new disk, in GiB. This number must be equal to or larger than the original source disk for the snapshot.

  7. Set the **Provisioned throughput** or **Provisioned IOPS** you want for the disk, if different from the default values.

  8. Click **Create** to create the Hyperdisk volume.




### gcloud

Run the [`gcloud compute disks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/create) to create the Hyperdisk volume from a snapshot.

### Hyperdisk Balanced
    
    
    gcloud compute disks create DISK_NAME \
        --size=SIZE \
        --source-snapshot=SNAPSHOT_NAME \
        --provisioned-throughput=TRHROUGHPUT_LIMIT \
        --provisioned-iops=IOPS_LIMIT \
        --type=hyperdisk-balanced
    

Replace the following:

  * `DISK_NAME`: the name of the new disk.
  * `SIZE`: the size, in gibibytes (GiB) or tebibytes (TiB), of the new disk. For more information about capacity limitations, see [ Size and performance limits](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced#size_limits).
  * `SNAPSHOT_NAME`: the name of the snapshot being restored.
  * `THROUGHPUT_LIMIT`: Optional. For Hyperdisk Balanced disks, this is an integer that represents the throughput, measured in MiB/s, that the disk can reach. For more information about capacity limitations, see [ Size and performance limits](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced#size_limits).
  * `IOPS_LIMIT`: Optional. For Hyperdisk Balanced disks, this is the maximum number of IOPS that the disk can reach. For more information about capacity limitations, see [ Size and performance limits](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced#size_limits).



### Hyperdisk Throughput
    
    
    gcloud compute disks create DISK_NAME \
        --size=SIZE \
        --source-snapshot=SNAPSHOT_NAME \
        --provisioned-throughput=TRHROUGHPUT_LIMIT \
        --type=hyperdisk-throughput
    

Replace the following:

  * `DISK_NAME`: the name of the new disk.
  * `SIZE`: the size, in gibibytes (GiB or GB) or tebibytes (TiB or TB), of the new disk. For more information about capacity limitations, see [ Size and performance limits](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-throughput#size_limits).
  * `SNAPSHOT_NAME`: the name of the snapshot being restored.
  * `THROUGHPUT_LIMIT`: Optional: For Hyperdisk Throughput disks, this is an integer that represents the throughput, measured in MiB/s, that the disk can reach. For more information about capacity limitations, see [ Size and performance limits](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-throughput#size_limits).



### Hyperdisk Extreme
    
    
    gcloud compute disks create DISK_NAME \
        --size=SIZE \
        --source-snapshot=SNAPSHOT_NAME \
        --provisioned-iops=IOPS_LIMIT \
        --type=hyperdisk-extreme
    

Replace the following:

  * `DISK_NAME`: the name of the new disk.
  * `SIZE`: the size, in gibibytes (GiB or GB) or tebibytes (TiB or TB), of the new disk. For more information about capacity limitations, see [ Size and performance limits](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-extreme#size_limits).
  * `SNAPSHOT_NAME`: the name of the snapshot being restored.
  * `IOPS_LIMIT`: Optional: For Hyperdisk Extreme disks, this is the maximum number of I/O operations per second that the disk can reach. For more information about capacity limitations, see [ Size and performance limits](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-extreme#size_limits).



### Hyperdisk Balanced HA
    
    
    gcloud compute disks create DISK_NAME \
        --size=SIZE \
        --region=REGION \
        --replica-zones=('ZONE1', 'ZONE2') \
        --source-snapshot=SNAPSHOT_NAME \
        --provisioned-throughput=TRHROUGHPUT_LIMIT \
        --provisioned-iops=IOPS_LIMIT \
        --type=hyperdisk-balanced-high-availability
    

Replace the following:

  * `DISK_NAME`: the name of the new disk.
  * `SIZE`: the size, in gibibytes (GiB) or tebibytes (TiB), of the new disk. Refer to the [Compute Engine documentation](https://docs.cloud.google.com/compute/docs/disks/hyperdisks) for the latest capacity limitations.
  * `REGION`: the region of the new disk. Refer to the [Compute Engine documentation](https://docs.cloud.google.com/compute/docs/disks/hyperdisks) for the latest regional availability.
  * `ZONE1`, `ZONE2`: the zones within the region where the replicas will be located.
  * `SNAPSHOT_NAME`: the name of the snapshot being restored.
  * `THROUGHPUT_LIMIT`: Optional. For Hyperdisk Balanced High Availability disks, this is an integer that represents the throughput, measured in MiB/s, that the disk can reach. For more information about capacity limitations, see [ Size and performance limits](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced#size_limits)
  * `IOPS_LIMIT`: Optional. For Hyperdisk Balanced High Availability disks, this is the maximum number of IOPS that the disk can reach. For more information about capacity limitations, see [ Size and performance limits](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced#size_limits).



## Create a snapshot for a Hyperdisk volume

To create a snapshot from a Hyperdisk volume, follow the same steps as creating a snapshot for a Persistent Disk volume:

  * [Create a snapshot in Google Cloud console](https://docs.cloud.google.com/compute/docs/disks/create-snapshots#console)
  * [Create a snapshot using the gcloud CLI](https://docs.cloud.google.com/compute/docs/disks/create-snapshots#gcloud)



## Update the provisioned throughput or IOPS of an existing Hyperdisk volume

This section covers how to modify provisioned performance for Hyperdisk volumes.

### Throughput

Updating the provisioned throughput is supported for Hyperdisk Balanced, Hyperdisk Balanced High Availability and Hyperdisk Throughput volumes only.

To update the provisioned throughput level of your Hyperdisk volume, follow the Google Cloud console, gcloud CLI, or Compute Engine API instructions in [Changing the provisioned performance for a Hyperdisk volume](https://docs.cloud.google.com/compute/docs/disks/modify-hyperdisks#changing_the_provisioned_performance_for_a_volume).

You can change the provisioned throughput level (up to once every 4 hours) for a Hyperdisk volume after volume creation. New throughput levels might take up to 15 minutes to take effect. During the performance change, any performance SLA and SLO are not in effect. You can change the throughput level of an existing volume at any time, regardless of whether the disk is attached to a running instance or not.

The new throughput level you specify must adhere to the supported values for [Hyperdisk Balanced](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced#provisioned-tput-limits), [Hyperdisk Throughput](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-throughput#provisioned-tput-limits) and [Hyperdisk Balanced High Availability](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced-ha#provisioned-tput-limits) volumes, respectively.

To update the provisioned throughput level for a Hyperdisk volume, you must identify the name of the Persistent Disk backing your PersistentVolumeClaim and PersistentVolume resources:

  1. Go to the **Object browser** in the Google Cloud console.

[Go to Object Browser](https://console.cloud.google.com/kubernetes/object/browser)

  2. Find the entry for your PersistentVolumeClaim object.

  3. Click the **Volume** link .

  4. Open the YAML tab of the associated PersistentVolume. Locate the CSI `volumeHandle` value in this tab.

  5. Note the last element of this handle (it should have a value like "`pvc-XXXXX`"). This is the name of your PersistentVolumeClaim. You should also take note of the project and zone.




### IOPS

Updating the provisioned IOPS is supported for Hyperdisk Balanced, Hyperdisk Balanced High Availability and Hyperdisk Extreme volumes only.

To update the provisioned IOPS level of your Hyperdisk volume, follow the Google Cloud console, gcloud CLI, or Compute Engine API instructions in [Changing the provisioned performance for a Hyperdisk volume](https://docs.cloud.google.com/compute/docs/disks/modify-hyperdisks#changing_the_provisioned_performance_for_a_volume).

You can change the provisioned IOPS level (up to once every 4 hours) for a Hyperdisk IOPS volume after volume creation. New IOPS levels might take up to 15 minutes to take effect. During the performance change, any performance SLA and SLO are not in effect. You can change the IOPS level of an existing volume at any time, regardless of whether the disk is attached to a running instance or not.

The new IOPS level you specify must adhere to the supported values for [Hyperdisk Balanced](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced#provisioned-iops-limits) or [Hyperdisk Extreme](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-extreme#iops_limits) volumes, respectively.

To update the provisioned IOPS level for a Hyperdisk volume, you must identify the name of the Persistent Disk backing your PersistentVolumeClaim and PersistentVolume resources:

  1. Go to the **Object browser** in the Google Cloud console.

[Go to Object Browser](https://console.cloud.google.com/kubernetes/object/browser)

  2. Find the entry for your PersistentVolumeClaim object.

  3. Click the **Volume** link .

  4. Open the YAML tab of the associated PersistentVolume. Locate the CSI `volumeHandle` value in this tab.

  5. Note the last element of this handle (it should have a value like "`pvc-XXXXX`"). This is the name of your PersistentVolumeClaim. You should also take note of the project and zone.




## Monitor throughput or IOPS on a Hyperdisk volume

To monitor the provisioned performance of your Hyperdisk volume, see [Analyze provisioned IOPS and throughput](https://docs.cloud.google.com/compute/docs/disks/analyze-iops-hyperdisk) in the Compute Engine documentation.

## Troubleshooting

This section provides troubleshooting guidance to resolve issues with Hyperdisk volumes on GKE.

### Cannot change performance or capacity: ratio out of range

The following error occurs when you attempt to change the provisioned performance level or capacity, but the performance level or capacity that you picked is outside of the range that is acceptable for the volume:

  * `Requested provisioned throughput cannot be higher than <value>.`
  * `Requested provisioned throughput cannot be lower than <value>.`
  * `Requested provisioned throughput is too high for the requested disk size.`
  * `Requested provisioned throughput is too low for the requested disk size.`
  * `Requested disk size is too high for current provisioned throughput.`



The throughput provisioned for Hyperdisk Throughput volumes must meet the following requirements:

  * At least 10 MiB/s per TiB of capacity, and no more than 90 MiB/s per TiB of capacity.
  * At most 600 MiB/s per volume.



To resolve this issue, correct the requested throughput or capacity to be within the allowable range and reissue the command.

### Cannot change performance: rate limited

The following error occurs when you attempt to change the provisioned performance level, but the performance level has already been changed within the last 4 hours:
    
    
    Cannot update provisioned throughput due to being rate limited.
    Cannot update provisioned iops due to being rate limited.
    

Hyperdisk Throughput and IOPS volumes can have their provisioned performance updated once every 4 hours. To resolve this issue, wait for the cool-down timer for the volume to elapse, and then reissue the command.

## What's next

  * [Learn how to configure a GKE cluster with a Hyperdisk Balanced custom boot disk](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/custom-boot-disks).
  * [Learn how to migrate Persistent Disk volumes to Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/migrate-to-hyperdisk#gcloud).
  * [Learn how to use volume expansion](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/volume-expansion).
  * [Learn how to use volume snapshots](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/volume-snapshots).
  * [Read more about the driver on GitHub](https://github.com/kubernetes-sigs/gcp-compute-persistent-disk-csi-driver).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
