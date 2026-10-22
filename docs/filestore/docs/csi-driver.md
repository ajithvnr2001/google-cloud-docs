---
url: https://docs.cloud.google.com/filestore/docs/csi-driver/
title: Access Filestore instances with the Filestore CSI driver \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:52:37.966597+00:00
---

# Access Filestore instances with the Filestore CSI driver  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/csi-driver/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  Access Filestore instances with the Filestore CSI driver Stay organized with collections  Save and categorize content based on your preferences. 

The Filestore CSI driver is the primary way for you to use [Filestore instances](https://docs.cloud.google.com/filestore/docs/overview) with Google Kubernetes Engine (GKE). The Filestore CSI driver provides a fully-managed experience powered by the open source [Google Cloud Filestore CSI driver](https://github.com/kubernetes-sigs/gcp-filestore-csi-driver).

The Filestore CSI driver version is tied to Kubernetes minor version numbers. The Filestore CSI driver version is typically the latest driver available at the time that the Kubernetes minor version is released. The drivers update automatically when the cluster is upgraded to the latest GKE patch.

**Note:** Because the Filestore CSI driver and some of the other associated CSI components are deployed as separate containers, they incur resource usage (VM CPU, memory, and boot disk) on Kubernetes nodes. VM CPU usage is typically tens of millicores and memory usage is typically tens of MiB. Boot disk usage is mostly incurred by the logs of the CSI driver and other system containers in the Deployment. For details about pricing for Autopilot and Standard clusters, see [Google Kubernetes Engine pricing](https://cloud.google.com/kubernetes-engine/pricing).

## Benefits

The Filestore CSI driver provides the following benefits:

  * You have access to fully-managed NFS storage through the Kubernetes APIs ([`kubectl`](https://kubernetes.io/docs/tasks/administer-cluster/access-cluster-api)).

  * You can use the GKE Filestore CSI driver to dynamically provision your PersistentVolumes.

  * You can use volume snapshots with the GKE Filestore CSI driver. [CSI volume snapshots](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/volume-snapshots) can be used to create [Filestore backups](https://docs.cloud.google.com/filestore/docs/backups).

A Filestore backup creates a differential copy of the file share, including all file data and metadata, and stores it separate from the instance. You can restore this copy to a new Filestore instance only. Restoring to an existing Filestore instance is not supported. You can use the CSI volume snapshot API to trigger Filestore backups, by adding a `type:backup` field in the [volume snapshot class](https://github.com/kubernetes-sigs/gcp-filestore-csi-driver/blob/master/examples/kubernetes/backups-restore/backup-volumesnapshotclass.yaml#L7).

  * You can use [volume expansion](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/volume-expansion) with the GKE Filestore CSI driver. Volume expansion lets you resize your volume's capacity.

  * You can access existing Filestore instances by [using pre-provisioned Filestore instances in Kubernetes workloads](https://github.com/kubernetes-sigs/gcp-filestore-csi-driver/blob/master/docs/kubernetes/pre-provisioned-pv.md). You can also dynamically create or delete Filestore instances and use them in Kubernetes workloads with a [StorageClass](https://github.com/kubernetes-sigs/gcp-filestore-csi-driver/blob/master/examples/kubernetes/demo-sc.yaml) or a [Deployment](https://github.com/kubernetes-sigs/gcp-filestore-csi-driver/blob/master/examples/kubernetes/demo-deployment.yaml).

  * Supports [Filestore multishares for GKE](https://docs.cloud.google.com/filestore/docs/multishares). This feature lets you create a Filestore instance and allocate multiple smaller NFS-mounted PersistentVolumes for it simultaneously across any number of GKE clusters.

  * Supports independent performance scaling. You can dynamically scale Filestore performance (IOPS) independently of storage capacity at runtime without service disruption.




## Requirements

  * To use the Filestore CSI driver, your clusters must meet the following requirements:

    * The required GKE version depends on the Filestore service tier, and the features you intend to use. See the Supported service tiers, protocols, and GKE versions table for supported combinations.
    * The Filestore CSI driver is supported for clusters using Linux nodes only. Windows Server nodes are not supported.
    * The minimum instance size is 1 TiB.

To learn more, see [Service tiers](https://docs.cloud.google.com/filestore/docs/service-tiers).




### Supported service tiers, protocols, and GKE versions

The following table outlines the supported combinations of Filestore service tiers, protocols, and the minimum required GKE versions for use with the Filestore CSI driver.

Service tier | Share type | GKE minimum version for NFSv3  | GKE minimum version for NFSv4.1  
---|---|---|---  
Enterprise | Single share, multishare | 1.25 | 1.33 (single share only)  
Zonal (1 TiB - 9.75 TiB) | Single share | 1.31 | 1.33  
Zonal (10 TiB - 100 TiB) | Single share | 1.27 | 1.33  
Regional(1 TiB - 9.75 TiB) | Single share | 1.33.4-gke.1172000 | 1.33.4-gke.1172000  
Regional(10 TiB - 100 TiB) | Single share | 1.33.4-gke.1172000 | 1.33.4-gke.1172000  
Basic HDD (100 GiB - 63.9 TiB) | Single share | 1.33 | Not supported  
Basic HDD | Single share | 1.21 | Not supported  
Basic SSD | Single share | 1.21 | Not supported  
  
Filestore uses the NFSv3 file system protocol on the Filestore instance by default and supports any NFSv3-compatible client. 

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Cloud Filestore API and the Google Kubernetes Engine API. 
[ Enable APIs ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com,file.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Ensure that you have an existing Autopilot or Standard cluster. If you need one, [create an Autopilot cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster). The Filestore CSI driver is enabled by default for Autopilot clusters.

  * If you want to use Filestore on a Shared VPC network, see the additional setup instructions in Use Filestore with Shared VPC.




## Enable the Filestore CSI driver on your Standard cluster

**Note:** The Filestore CSI driver is enabled by default for Autopilot clusters.

To enable the Filestore CSI driver on Standard clusters, use the Google Cloud CLI or the Google Cloud console.

To enable the driver on an existing Standard cluster, complete the following steps:

### gcloud
    
    
    gcloud container clusters update CLUSTER_NAME \
       --update-addons=GcpFilestoreCsiDriver=ENABLED
    

Replace `CLUSTER_NAME` with the name of the existing cluster.

### Console

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the cluster list, click the name of the cluster you want to modify.

  3. Under **Features** , next to the **Filestore CSI driver** field, click _edit_ **Edit Filestore CSI driver**.

  4. Select the **Enable Filestore CSI driver** checkbox.

  5. Click **Save Changes**.




If you want to use Filestore on a Shared VPC network, see Enable the Filestore CSI driver on a new cluster with Shared VPC.

After you enable the Filestore CSI driver, you can use the driver in Kubernetes volumes using the driver and provisioner name: `filestore.csi.storage.gke.io`.

## Disable the Filestore CSI driver

You can disable the Filestore CSI driver on an existing Autopilot or Standard cluster by using the Google Cloud CLI or the Google Cloud console.

**Note:** We strongly recommend not to manually disable the Filestore CSI driver on Autopilot clusters. Doing so causes any Pods using PersistentVolumes owned by the driver to fail to terminate. New pods attempting to use those PersistentVolumes will also fail to start.

### gcloud
    
    
    gcloud container clusters update CLUSTER_NAME \
        --update-addons=GcpFilestoreCsiDriver=DISABLED \
        --region REGION
    

Replace the following values:

  * `CLUSTER_NAME`: the name of the existing cluster.
  * `REGION`: the region for your cluster (such as, `us-central1`).



### Console

  1. In the Google Cloud console, go to the Google Kubernetes Engine menu.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the cluster list, click the name of the cluster you want to modify.

  3. Under **Features** , next to the **Filestore CSI driver** field, click _edit_ **Edit Filestore CSI driver**.

  4. Clear the **Enable Filestore CSI driver** checkbox.

  5. Click **Save Changes**.




## Access pre-existing Filestore instances using the Filestore CSI driver

This section describes the typical process for using a Kubernetes volume to access pre-existing Filestore instances using Filestore CSI driver in GKE:

### Create a PersistentVolume and a PersistentVolumeClaim to access the instance

  1. Create a manifest file like the one shown in the following example, and name it `preprov-filestore.yaml`:
         
         apiVersion: v1
         kind: PersistentVolume
         metadata:
           name: PV_NAME
         spec:
           storageClassName: ""
           capacity:
             storage: 1Ti
           accessModes:
             - ReadWriteMany
           persistentVolumeReclaimPolicy: Retain
           volumeMode: Filesystem
           csi:
             driver: filestore.csi.storage.gke.io
             volumeHandle: "modeInstance/FILESTORE_INSTANCE_LOCATION/FILESTORE_INSTANCE_NAME/FILESTORE_SHARE_NAME"
             volumeAttributes:
               ip: FILESTORE_INSTANCE_IP
               volume: FILESTORE_SHARE_NAME
               protocol: FILESYSTEM_PROTOCOL
           claimRef:
             name: PVC_NAME
             namespace: NAMESPACE
         ---
         kind: PersistentVolumeClaim
         apiVersion: v1
         metadata:
           name: PVC_NAME
           namespace: NAMESPACE
         spec:
           accessModes:
             - ReadWriteMany
           storageClassName: ""
           resources:
             requests:
               storage: 1Ti
         

  2. To create the `PersistentVolumeClaim` and `PersistentVolume` resources based on the `preprov-filestore.yaml` manifest file, run the following command:
         
         kubectl apply -f preprov-filestore.yaml
         




To specify the NFSv4.1 file system protocol, set the `protocol` field to `NFS_V4_1` in the `volumeAttributes` field of a `PersistentVolume` object. To use the NFSv3 file system protocol, set the `protocol` field to `NFS_V3` or omit the `protocol` field.

Then, proceed to create a Deployment that consumes the volume.

## Create a volume using the Filestore CSI driver

The following sections describe the typical process for using a Kubernetes volume backed by a Filestore CSI driver in GKE:

  * Create a StorageClass
  * Use a PersistentVolumeClaim to access the volume
  * Create a Deployment that consumes the volume



### Create a StorageClass

After you enable the Filestore CSI driver, GKE automatically installs the following [StorageClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes#storageclasses) for provisioning Filestore instances:

  * `zonal-rwx`, using the [Filestore zonal tier](https://docs.cloud.google.com/filestore/docs/service-tiers).
  * `enterprise-rwx`, using the [Filestore enterprise tier](https://docs.cloud.google.com/filestore/docs/service-tiers), where each Kubernetes PersistentVolume maps to a Filestore instance.
  * `enterprise-multishare-rwx`, using the [Filestore enterprise tier](https://docs.cloud.google.com/filestore/docs/service-tiers), where each Kubernetes PersistentVolume maps to a share of a given Filestore instance. To learn more, see [Filestore multishares for Google Kubernetes Engine](https://docs.cloud.google.com/filestore/docs/multishares).
  * `standard-rwx`, using the [Filestore basic HDD service tier](https://docs.cloud.google.com/filestore/docs/service-tiers).
  * `premium-rwx`, using the [Filestore basic SSD service tier](https://docs.cloud.google.com/filestore/docs/service-tiers).



Each StorageClass is only available in GKE clusters running in their respective supported GKE version numbers. For a list of supported versions required for each service tier, see Requirements.

You can find the name of your installed `StorageClass` by running the following command:
    
    
    kubectl get sc
    

**Note:** The pre-installed StorageClasses use `volumeBindingMode: WaitForFirstConsumer`. This means that the Filestore instance is not provisioned immediately after creating the PersistentVolumeClaim. The instance is only created when a Pod that references the PersistentVolumeClaim is scheduled.

You can also install a different `StorageClass` that uses the Filestore CSI driver by adding `filestore.csi.storage.gke.io` in the `provisioner` field.

Filestore needs to know on which network to create the new instance. The automatically installed StorageClasses use the default network created for GKE clusters. If you have deleted this network or want to use a different network, you must create a new StorageClass as described in the following steps. Otherwise, the automatically installed StorageClasses won't work.

  1. Save the following manifest as `filestore-example-class.yaml`:
         
         apiVersion: storage.k8s.io/v1
         kind: StorageClass
         metadata:
           name: filestore-example
         provisioner: filestore.csi.storage.gke.io
         volumeBindingMode: Immediate
         allowVolumeExpansion: true
         parameters:
           tier: standard
           network: default
         

From the manifest, consider the following parameter configuration:

     * Setting `volumeBindingMode` to `Immediate` allows the provisioning of the volume to begin immediately. This is possible because Filestore instances are accessible from any zone. Therefore GKE does not need to know the zone where the Pod is scheduled, in contrast with Compute Engine persistent disk. When set to `WaitForFirstConsumer`, GKE begins provisioning only after the Pod is scheduled. For more information, see [VolumeBindingMode](https://kubernetes.io/docs/concepts/storage/storage-classes/#volume-binding-mode).
     * Any supported [Filestore tier](https://docs.cloud.google.com/filestore/docs/service-tiers) can be specified in the [`tier` parameter](https://docs.cloud.google.com/filestore/docs/reference/rest/v1/Tier) (for example, `BASIC_HDD`, `BASIC_SSD`, `ZONAL`, or `ENTERPRISE`).
     * The [`network` parameter](https://docs.cloud.google.com/filestore/docs/reference/rest/v1/projects.locations.instances#networkconfig) can be used when provisioning Filestore instances on non-default VPCs. Non-default VPCs require special [firewall rules](https://docs.cloud.google.com/filestore/docs/configuring-firewall) to be set up.
     * The [`protocol` parameter](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/FileProtocol) can be used to set the file system protocol of the Filestore instance. It can take the following values: `NFS_V3` (default) and `NFS_V4_1`. The default protocol is `NFS_V3`.
  2. To create a `StorageClass` resource based on the `filestore-example-class.yaml` manifest file, run the following command:
         
         kubectl create -f filestore-example-class.yaml
         




If you want to use Filestore on a Shared VPC network, see Create a StorageClass when using the Filestore CSI driver with Shared VPC.

### Use a PersistentVolumeClaim to access the volume

You can create a `PersistentVolumeClaim` resource that references the Filestore CSI driver's `StorageClass`.

You can use either a pre-installed or custom `StorageClass`.

The following example manifest file creates a `PersistentVolumeClaim` that references the `StorageClass` named `filestore-example`.

  1. Save the following manifest file as `pvc-example.yaml`:
         
         kind: PersistentVolumeClaim
         apiVersion: v1
         metadata:
           name: podpvc
         spec:
           accessModes:
           - ReadWriteMany
           storageClassName: filestore-example
           resources:
             requests:
               storage: 1Ti
         

  2. To create a `PersistentVolumeClaim` resource based on the `pvc-example.yaml` manifest file, run the following command:
         
         kubectl create -f pvc-example.yaml
         




### Create a Deployment that consumes the volume

The following example Deployment manifest consumes the `PersistentVolume` resource named `pvc-example.yaml`.

Multiple Pods can share the same `PersistentVolumeClaim` resource.

  1. Save the following manifest as `filestore-example-deployment.yaml`:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: web-server-deployment
           labels:
             app: nginx
         spec:
           replicas: 3
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
                 - mountPath: /usr/share/nginx/html
                   name: mypvc
               volumes:
               - name: mypvc
                 persistentVolumeClaim:
                   claimName: podpvc
         ---
         kind: PersistentVolumeClaim
         apiVersion: v1
         metadata:
           name: podpvc
         spec:
           accessModes:
             - ReadWriteMany
           storageClassName: filestore-example
           resources:
             requests:
               storage: 1Ti
         

  2. To create a Deployment based on the `filestore-example-deployment.yaml` manifest file, run the following command:
         
         kubectl apply -f filestore-example-deployment.yaml
         

  3. Confirm the Deployment was successfully created:
         
         kubectl get deployment
         

It might take a while for Filestore instances to complete provisioning. Before that, deployments won't report a `READY` status. You can check the progress by monitoring your PVC status by running the following command:
         
         kubectl get pvc
         

You should see the PVC reach a `BOUND` status, when the volume provisioning completes.




## Dynamically scale Filestore performance using `VolumeAttributesClass`

The Filestore CSI driver supports [custom performance](https://docs.cloud.google.com/filestore/docs/custom-performance) for Zonal and Regional service tiers. Custom performance configuration lets you adjust the application performance according to your workload needs, scaling it up and down as required. Ensure that your GKE cluster version is 1.35 or later.

To allow for smooth performance scaling, you can define multiple performance tiers using the `VolumeAttributesClass` API. Having predefined tiers lets you dynamically update performance settings on existing volumes by switching between them at runtime without re-provisioning the volume or experiencing downtime.

### Default performance tiers

The following table lists the predefined performance tiers. To define a custom performance tier, see Define performance tiers.

Performance tier name | Parameter | Maximum IOPS  
---|---|---  
`filestore-high-performance-fixed` | `max-iops` | `"17000"`  
`filestore-min-performance-scaling` | `max-iops-per-tb` | `"4000"`  
`filestore-moderate-performance-scaling` | `max-iops-per-tb` | `"10000"`  
  
### Define performance tiers

You define multiple performance tiers by creating `VolumeAttributesClass` resources. In the following example, you create a moderate and high performance tier using a fixed IOPS rate (`max-iops`). You can also use an IOPS-per-TiB ratio (`max-iops-per-tb`) which scales linearly with the volume size.

Specify `max-iops` or `max-iops-per-tb` values that yield at least 2,000 provisioned IOPS. If the calculated IOPS is less than 2,000, the system automatically rounds the value up to this minimum.

  1. Save the following manifest as `performance-tiers.yaml`:
         
         apiVersion: storage.k8s.io/v1
         kind: VolumeAttributesClass
         metadata:
           name: filestore-moderate
         driverName: filestore.csi.storage.gke.io
         parameters:
           max-iops: "4000"
         ---
         apiVersion: storage.k8s.io/v1
         kind: VolumeAttributesClass
         metadata:
           name: filestore-high
         driverName: filestore.csi.storage.gke.io
         parameters:
           max-iops: "10000"
         ---
         apiVersion: storage.k8s.io/v1
         kind: VolumeAttributesClass
         metadata:
           name: filestore-density-based
         driverName: filestore.csi.storage.gke.io
         parameters:
           max-iops-per-tb: "5000"
         

  2. Create the `VolumeAttributesClass` resources:
         
         kubectl apply -f performance-tiers.yaml
         




### Create a `PersistentVolumeClaim` with an initial performance tier

To create a `PersistentVolumeClaim` with a performance configuration, reference the `VolumeAttributesClass` in your `PersistentVolumeClaim` resource.

  1. Save the following manifest as `pvc-custom-performance.yaml`, referencing the `filestore-moderate` tier:
         
         apiVersion: v1
         kind: PersistentVolumeClaim
         metadata:
           name: filestore-pvc
         spec:
           accessModes:
             - ReadWriteMany
           storageClassName: regional-rwx
           volumeAttributesClassName: filestore-moderate
           resources:
             requests:
               storage: 1Ti
         

  2. Create the `PersistentVolumeClaim`:
         
         kubectl apply -f pvc-custom-performance.yaml
         




### Update the `PersistentVolumeClaim` to use a different performance tier

  1. When your workload requires higher performance, update the `volumeAttributesClassName` in your `pvc-custom-performance.yaml` file to `filestore-high`:
         
         apiVersion: v1
          kind: PersistentVolumeClaim
          metadata:
            name: filestore-pvc
          spec:
            accessModes:
              - ReadWriteMany
            storageClassName: regional-rwx
            volumeAttributesClassName: filestore-high
            resources:
              requests:
                storage: 1Ti
          ```
         

  2. Apply the change:
         
         kubectl apply -f pvc-custom-performance.yaml
         

The Filestore CSI driver processes the update dynamically. 

  3. Verify the performance status:
         
         kubectl describe pvc filestore-pvc
         

Check the **Events** section in the command output to verify if the attributes were successfully modified.




## Label Filestore instances

You can use [labels](https://docs.cloud.google.com/filestore/docs/tags-and-labels#labels) to group related instances and store metadata about an instance. A label is a key-value pair that helps you organize your Filestore instances. You can attach a label to each resource, then filter the resources based on their labels.

You can provide labels by using the `labels` key in `StorageClass.parameters`. A Filestore instance can be labeled with information about what `PersistentVolumeClaim`/`PersistentVolume` the instance was created for. Custom label keys and values must comply with the label [naming convention](https://docs.cloud.google.com/resource-manager/docs/creating-managing-labels#requirements). See the Kubernetes [storage class example](https://github.com/kubernetes-sigs/gcp-filestore-csi-driver/blob/master/examples/kubernetes/sc-labels.yaml) to apply custom labels to the Filestore instance.

## Use NFSv4.1 file system protocol with Filestore

The Filestore CSI driver supports the NFSv4.1 file system protocol with GKE version 1.33 or later. In case of static provisioning, set the `protocol` field to `NFS_V4_1` in the `volumeAttributes` field of a `PersistentVolume` object.

For dynamic provisioning, set the `protocol` field to `NFS_V4_1` in the parameters of a `StorageClass` object.
    
    
    apiVersion: storage.k8s.io/v1
    kind: StorageClass
    metadata:
      name: enterprise-nfsv41-rwx
    provisioner: filestore.csi.storage.gke.io
    parameters:
      tier: enterprise
      instance-storageclass-label: "enterprise-nfsv41-rwx"
      protocol: NFS_V4_1
    volumeBindingMode: WaitForFirstConsumer
    allowVolumeExpansion: true
    

**Note:** When creating the `StorageClass` object, consider the following limitations: 

  * Don't configure `protocol: NFS_V4_1` and `multishare: "true"` in the same `StorageClass` object definition. The NFSv4.1 protocol only supports single-share instances, whereas Filestore. multishares for GKE require the NFSv3 protocol.
  * A `StorageClass` object definition can't combine a Filestore NFSv4.1 protocol instance with `mountOptions` set to nfsvers=3.



For more information, see [NFSv4.1 limitations](https://docs.cloud.google.com/filestore/docs/service-tiers#nfsv41-limitations).

## Use fsgroup with Filestore volumes

Kubernetes uses `fsGroup` to change permissions and ownership of the volume to match a user-requested `fsGroup` in the Pod's [SecurityContext](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/#set-the-security-context-for-a-pod). An `fsGroup` is a supplemental group that applies to all containers in a Pod. You can [apply an fsgroup ](https://github.com/kubernetes-sigs/gcp-filestore-csi-driver/blob/master/docs/kubernetes/fsgroup.md) to volumes provisioned by the Filestore CSI driver.

## Configure IP access rules with Filestore volumes

Filestore supports [IP-based access control rules](https://docs.cloud.google.com/filestore/docs/creating-instances#configure_ip-based_access_control) for volumes. This feature is available on GKE clusters running version 1.29.5 or later.

This feature allows administrators to specify which IP address ranges are allowed to access a Filestore instance provisioned dynamically through GKE. This enhances security by restricting access to only authorized clients, especially in scenarios where the GKE cluster's IP range is too broad, potentially exposing the Filestore instance to unauthorized users or applications.

These rules can be configured directly through the Filestore API, or through the Filestore CSI driver when a volume is created. You can provide the selected configuration in JSON format in the StorageClass using the `nfs-export-options-on-create` parameter.

The following example manifest shows how to specify the configuration:
    
    
    apiVersion: storage.k8s.io/v1
    kind: StorageClass
    metadata:
      name: filestore-example
    provisioner: filestore.csi.storage.gke.io
    volumeBindingMode: Immediate
    allowVolumeExpansion: true
    parameters:
      tier: "enterprise"
      nfs-export-options-on-create: '[
        {
          "accessMode": "READ_WRITE",
          "ipRanges": [
            "10.0.0.0/24"
          ],
          "squashMode": "ROOT_SQUASH",
          "anonUid": "1003",
          "anonGid": "1003"
        },
        {
          "accessMode": "READ_WRITE",
          "ipRanges": [
            "10.0.0.0/28"
          ],
          "squashMode": "NO_ROOT_SQUASH"
        }
      ]'
    

**Note:** Use the node primary IP range instead of the Pod IP in the `nfs-export-options-on-create` parameter.

### Security options

Filestore IP access rules simplify the configuration of shared file storage permissions for your GKE workloads. However, understanding how it manages file ownership and access requires grasping a few key concepts:

  * **NFS and user mappings** NFS (Network File System) is the protocol used by Filestore. It works by mapping users on client systems (your GKE Pods) to users on the Filestore server. If a file on the server is owned by user ID 1003, and a client connects with user ID 1003, they'll have access to the file.

  * **Root squashing and`anonUid`:**

    * **Root Squashing[`ROOT_SQUASH`](https://docs.cloud.google.com/filestore/docs/creating-instances#configure_ip-based_access_control)** is a security feature that prevents clients from accessing the Filestore instance with full root privileges. When root squashing is enabled, root users on client systems are mapped to a non-privileged user specified by the [`anonUid`](https://docs.cloud.google.com/filestore/docs/creating-instances#configure_ip-based_access_control) setting.

    * **No Root Squashing (`NO_ROOT_SQUASH`)** allows clients to access the Filestore instance with full root privileges, which is convenient for initial setup but less secure for regular operations.

  * **Initial Setup and Permissions:** By default, a new Filestore instance is owned entirely by the root user. If you enable root squashing without first setting up permissions for other users, you'll lose access. This is why you need at least one NFS export rule with `NO_ROOT_SQUASH` to initially configure access for other users and groups.




#### Recommendations

  * **Initial Setup:** Always start with at least one NFS export rule that specifies an administrator range with `READ_WRITE` permissions and allows `NO_ROOT_SQUASH` access. Use this access to create directories, set permissions, and assign ownership as needed.
  * **Security:** Enable root squashing (`ROOT_SQUASH`) to enhance security. Note that after a volume is created, you can only modify the access rules through the Filestore API.
  * **Shared Access:** Use `fsGroup` in your [Pod security contexts](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/#set-the-security-context-for-a-pod) to manage group ownership of shared volumes. Make sure not to overlap your setting with the `ROOT_SQUASH` mode. Doing so returns an `Access denied` error message.



## Use Filestore with Shared VPC

This section covers how to use a Filestore instance on a Shared VPC network from a service project.

### Set up a cluster with Shared VPC

To set up your clusters with a Shared VPC network, follow these steps:

  1. [Create a host and service project](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-shared-vpc#overview).
  2. [Enable the Kubernetes Engine API on both your host and service projects](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-shared-vpc#enabling_the_api_in_your_projects).
  3. [In your host project, create a network and a subnet](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-shared-vpc#creating_a_network_and_two_subnets).
  4. [Enable Shared VPC in the host project](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-shared-vpc#enabling_and_granting_roles).
  5. [On the host project, grant the `HostServiceAgent` user role binding for the service project's GKE service account](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-shared-vpc#grant_host_service_agent_role).
  6. [Enable private service access on the Shared VPC network](https://docs.cloud.google.com/filestore/docs/shared-vpc#enable_private_service_access_on_the_network).



### Enable the Filestore CSI driver on a new cluster with Shared VPC

To enable the Filestore CSI driver on a new cluster with Shared VPC, follow these steps:

  1. Verify the usable subnets and secondary ranges. When creating a cluster, you must specify a subnet and the secondary IP address ranges to be used for the cluster's Pods and Service.
         
         gcloud container subnets list-usable \
            --project=SERVICE_PROJECT_ID \
            --network-project=HOST_PROJECT_ID
         

The output is similar to the following:
         
         PROJECT                   REGION       NETWORK     SUBNET  RANGE
         HOST_PROJECT_ID  us-central1  shared-net  tier-1  10.0.4.0/22
         ┌──────────────────────┬───────────────┬─────────────────────────────┐
         │ SECONDARY_RANGE_NAME │ IP_CIDR_RANGE │            STATUS           │
         ├──────────────────────┼───────────────┼─────────────────────────────┤
         │ tier-1-pods          │ 10.4.0.0/14   │ usable for pods or services │
         │ tier-1-services      │ 10.0.32.0/20  │ usable for pods or services │
         └──────────────────────┴───────────────┴─────────────────────────────┘
         

  2. Create a GKE cluster. The following examples show how you can use gcloud CLI to create an Autopilot or Standard cluster configured for Shared VPC. The following examples use the network, subnet, and range names from [Creating a network and two subnets](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-shared-vpc#creating_a_network_and_two_subnets).

### Autopilot
         
         gcloud container clusters create-auto tier-1-cluster \
            --project=SERVICE_PROJECT_ID \
            --region=COMPUTE_REGION \
            --network=projects/HOST_PROJECT_ID/global/networks/NETWORK_NAME \
            --subnetwork=projects/HOST_PROJECT_ID/regions/COMPUTE_REGION/subnetworks/SUBNET_NAME \
            --cluster-secondary-range-name=tier-1-pods \
            --services-secondary-range-name=tier-1-services
         

### Standard
         
         gcloud container clusters create tier-1-cluster \
            --project=SERVICE_PROJECT_ID \
            --zone=COMPUTE_REGION \
            --enable-ip-alias \
            --network=projects/HOST_PROJECT_ID/global/networks/NETWORK_NAME \
            --subnetwork=projects/HOST_PROJECT_ID/regions/COMPUTE_REGION/subnetworks/SUBNET_NAME \
            --cluster-secondary-range-name=tier-1-pods \
            --services-secondary-range-name=tier-1-services \
            --addons=GcpFilestoreCsiDriver
         

  3. Create firewall rules to allow communication between nodes, Pods, and Services in your cluster. The following example shows how you can create a firewall rule named `my-shared-net-rule-2`.
         
         gcloud compute firewall-rules create my-shared-net-rule-2 \
            --project HOST_PROJECT_ID \
            --network=NETWORK_NAME \
            --allow=tcp,udp \
            --direction=INGRESS \
            --source-ranges=10.0.4.0/22,10.4.0.0/14,10.0.32.0/20
         

In the example, the source ranges IP values come from the previous step where you verified the usable subnets and secondary ranges.




### Create a StorageClass when using the Filestore CSI driver with Shared VPC

The following example shows how you can create a StorageClass when using the Filestore CSI driver with Shared VPC:
    
    
    cat <<EOF | kubectl apply -f -
    
    apiVersion: storage.k8s.io/v1
    kind: StorageClass
    metadata:
      name: filestore-sharedvpc-example
    provisioner: filestore.csi.storage.gke.io
    parameters:
      network: "projects/HOST_PROJECT_ID/global/networks/SHARED_VPC_NAME"
      connect-mode: PRIVATE_SERVICE_ACCESS
      reserved-ip-range: RESERVED_IP_RANGE_NAME
    allowVolumeExpansion: true
    
    EOF
    

Replace the following:

  * `HOST_PROJECT_ID`: the ID or name of the host project of the Shared VPC network.
  * `SHARED_VPC_NAME`: the name of the Shared VPC network you created earlier.
  * `RESERVED_IP_RANGE_NAME`: the name of the specific reserved IP address range to provision Filestore instance in. This field is optional. If a reserved IP address range is specified, it must be a named address range instead of a direct CIDR value.



If you want to provision a volume backed by Filestore multishares on GKE clusters running version 1.23 or later, see [Optimize storage with Filestore multishares for GKE](https://docs.cloud.google.com/filestore/docs/optimize-multishares#dynamic_provisioning_on_a_shared_vpc).

## Reconnect Filestore single share volumes

If you are using Filestore with the basic HDD, basic SSD, or enterprise (single share) tier, you can follow these instructions to reconnect your existing Filestore instance to your GKE workloads.

  1. Find the details of your pre-provisioned Filestore instance by following the instructions in [Getting information about a specific instance](https://docs.cloud.google.com/filestore/docs/getting-instance-information#get-instance).

  2. Redeploy your PersistentVolume specification. In the `volumeAttributes` field, modify the following fields to use the same values as your Filestore instance from step 1:

     * `ip`: Modify this value to the pre-provisioned Filestore instance IP address.
     * `volume`: Modify this value to the pre-provisioned Filestore instance's share name. In the `claimRef` make sure you reference the same PersistentVolumeClaim in step 2.
  3. Redeploy your PersistentVolumeClaim specification.

  4. Check the binding status of your PersistentVolumeClaim and PersistentVolume by running `kubectl get pvc`.

  5. Redeploy your Pod specification and ensure that your Pod is able to access the Filestore share again.




## What's next

  * [Learn how to deploy a stateful Filestore workload on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/stateful-workload).
  * [Learn how to share a Filestore enterprise instance with multiple Persistent Volumes](https://docs.cloud.google.com/filestore/docs/multishares).
  * [Learn how to use volume expansion](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/volume-expansion).
  * [Learn how to use volume snapshots](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/volume-snapshots).
  * [Read more about the CSI driver on GitHub](https://github.com/kubernetes-sigs/gcp-filestore-csi-driver).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
