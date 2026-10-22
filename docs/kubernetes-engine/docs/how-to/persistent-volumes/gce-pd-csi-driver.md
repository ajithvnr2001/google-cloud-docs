---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/gce-pd-csi-driver/
title: Using the Compute Engine persistent disk CSI Driver \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:49.041025+00:00
---

# Using the Compute Engine persistent disk CSI Driver  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/gce-pd-csi-driver/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Using the Compute Engine persistent disk CSI Driver Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

Google Kubernetes Engine (GKE) provides a simple way for you to automatically deploy and manage the [Compute Engine persistent disk Container Storage Interface (CSI) Driver](https://github.com/kubernetes-sigs/gcp-compute-persistent-disk-csi-driver) in your clusters. The Compute Engine persistent disk CSI Driver is always enabled in Autopilot clusters and can't be disabled or edited. In Standard clusters, you must enable the Compute Engine persistent disk CSI Driver.

The Compute Engine persistent disk CSI Driver version is tied to GKE version numbers. The Compute Engine persistent disk CSI Driver version is typically the latest driver available at the time that the GKE version is released. The drivers update automatically when the cluster is upgraded to the latest GKE patch.

**Note:** Because the Compute Engine persistent disk CSI Driver and some of the other associated CSI components are deployed as separate containers, they incur resource usage (VM CPU, memory, and boot disk) on Kubernetes nodes. VM CPU usage is typically tens of millicores and memory usage is typically tens of MB. Boot disk usage is mostly incurred by the logs of the CSI driver and other system containers in the Deployment.

## Benefits

Using the Compute Engine persistent disk CSI Driver provides the following benefits:

  * It enables the automatic deployment and management of the persistent disk driver without having to manually set it up.
  * You can use customer-managed encryption keys (CMEKs). These keys are used to encrypt the data encryption keys that encrypt your data. To learn more about CMEK on GKE, see [Using CMEK](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/using-cmek).
  * You can use [volume snapshots](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/volume-snapshots) with the Compute Engine persistent disk CSI Driver. Volume snapshots let you create a copy of your volume at a specific point in time. You can use this copy to bring a volume back to a prior state or to provision a new volume.
  * You can use [volume cloning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/volume-cloning) with the Compute Engine persistent disk CSI Driver in clusters running GKE version 1.22 and later. Volume cloning lets you create a duplicate of your volume at a specific point in time, provisioned with all of the data of from the source volume.
  * Bug fixes and feature updates are rolled out independently from minor Kubernetes releases. This release schedule typically results in a faster release cadence.



## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



## Enable the Compute Engine persistent disk CSI Driver

To enable the Compute Engine persistent disk CSI Driver in existing Standard clusters, use the Google Cloud CLI or the Google Cloud console.

To enable the driver on an existing cluster, complete the following steps:

### gcloud
    
    
    gcloud container clusters update CLUSTER-NAME \
       --update-addons=GcePersistentDiskCsiDriver=ENABLED
    

Replace `CLUSTER-NAME` with the name of the existing cluster.

### Console

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the cluster list, click the name of the cluster you want to modify.

  3. Under **Features** , next to the **Compute Engine persistent disk CSI Driver** field, click _edit_ **Edit Compute Engine CSI driver**.

  4. Select the **Enable Compute Engine Persistent Disk CSI Driver** checkbox.

  5. Click **Save Changes**.




After you have enabled the Compute Engine persistent disk CSI Driver, you can use the driver in Kubernetes volumes by using the driver and provisioner name: `pd.csi.storage.gke.io`.

## Disable the Compute Engine persistent disk CSI Driver

You can disable the Compute Engine persistent disk CSI Driver for Standard clusters by using Google Cloud CLI or the Google Cloud console.

If you disable the driver, then any Pods currently using PersistentVolumes owned by the driver do not terminate. Any new Pods that try to use those PersistentVolumes also fail to start.

**Note:** As the `gcePersistentDisk` volume type is migrated to the Compute Engine persistent disk CSI Driver in version 1.22 and later, if you disable the persistent disk CSI driver, the `gcePersistentDisk` volume type also stops working.**Warning:** There is a known issue in GKE 1.21 and earlier if you are using the in-tree persistent disk driver and want to delete regional disks. A Compute Engine regional disk can leak when its related `PersistentVolume` resource is deleted. This problem can be detected when your API call to delete the regional disk fails and returns an error code other than `NotFound`. For more information, see this [GitHub issue](https://github.com/kubernetes/kubernetes/issues/109328).

To disable the driver on an existing Standard cluster, complete the following steps:

### gcloud
    
    
    gcloud container clusters update CLUSTER-NAME \
        --update-addons=GcePersistentDiskCsiDriver=DISABLED
    

Replace `CLUSTER-NAME` with the name of the existing cluster.

### Console

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the cluster list, click the name of the cluster you want to modify.

  3. Under **Features** , next to the **Compute Engine persistent disk CSI Driver** field, click _edit_ **Edit Compute Engine CSI driver**.

  4. Clear the **Enable Compute Engine Persistent Disk CSI Driver** checkbox.

  5. Click **Save Changes**.




## Use the Compute Engine persistent disk CSI Driver for Linux clusters

The following sections describe the typical process for using a Kubernetes volume backed by a CSI driver in GKE. These sections are specific to clusters using Linux.

### Create a StorageClass

After you enable the Compute Engine persistent disk CSI Driver, GKE automatically installs the following [StorageClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes#storageclasses):

  * `standard-rwo`, using balanced persistent disk
  * `premium-rwo`, using SSD persistent disk



For Autopilot clusters, the default StorageClass is `standard-rwo`, which uses the Compute Engine persistent disk CSI Driver. For Standard clusters, the default StorageClass uses the Kubernetes in-tree `gcePersistentDisk` volume plugin.

You can find the name of your installed StorageClasses by running the following command:
    
    
    kubectl get sc
    

You can also install a different StorageClass that uses the Compute Engine persistent disk CSI Driver by adding `pd.csi.storage.gke.io` in the provisioner field.

For example, you could create a StorageClass using the following file, which is named `pd-example-class.yaml`.
    
    
    apiVersion: storage.k8s.io/v1
    kind: StorageClass
    metadata:
      name: pd-example
    **provisioner : pd.csi.storage.gke.io**
    # Recommended setting. Delays the binding and provisioning of a PersistentVolume until a Pod that uses the
    # PersistentVolumeClaim is created and scheduled on a node.
    **volumeBindingMode : WaitForFirstConsumer**
    allowVolumeExpansion: true
    parameters:
      type: pd-balanced
    

You can specify the following [Persistent Disk types](https://docs.cloud.google.com/compute/docs/disks/persistent-disks#disk-types) in the `type` parameter:

  * `pd-balanced`
  * `pd-ssd`
  * `pd-standard`
  * `pd-extreme` (supported on GKE version 1.26 and later)



If using `pd-standard` or `pd-extreme`, see Unsupported machine types for additional usage restrictions.

When you use the `pd-extreme` option, you must also add the `provisioned-iops-on-create` field to your manifest. This field must be set to the same value as the [provisioned IOPS value](https://docs.cloud.google.com/compute/docs/disks/extreme-persistent-disk#provisioning_iops) that you specified when you created your persistent disk.
    
    
    apiVersion: storage.k8s.io/v1
    kind: StorageClass
    metadata:
      name: pd-extreme-example
    provisioner: pd.csi.storage.gke.io
    volumeBindingMode: WaitForFirstConsumer
    allowVolumeExpansion: true
    parameters:
      type: pd-extreme
      **provisioned-iops-on-create:'10000'**
    

After creating the `pd-example-class.yaml` file, run the following command:
    
    
    kubectl create -f pd-example-class.yaml
    

### Create a PersistentVolumeClaim

You can create a PersistentVolumeClaim that references the Compute Engine persistent disk CSI Driver's StorageClass.

The following file, named `pvc-example.yaml`, uses the pre-installed storage class `standard-rwo`:
    
    
    kind: PersistentVolumeClaim
    apiVersion: v1
    metadata:
      name: podpvc
    spec:
      accessModes:
      - ReadWriteOnce
      storageClassName: standard-rwo
      resources:
        requests:
          storage: 6Gi
    

After creating the PersistentVolumeClaim manifest, run the following command:
    
    
    kubectl create -f pvc-example.yaml
    

In the pre-installed StorageClass (`standard-rwo`), `volumeBindingMode` is set to `WaitForFirstConsumer`. When `volumeBindingMode` is set to `WaitForFirstConsumer`, the PersistentVolume is not provisioned until a Pod referencing the PersistentVolumeClaim is scheduled. If `volumeBindingMode` in the StorageClass is set to `Immediate` (or it's omitted), a persistent-disk-backed PersistentVolume is provisioned after the PersistentVolumeClaim is created.

### Create a Pod that consumes the volume

When using Pods with PersistentVolumes, we recommend that you use a workload controller (such as a Deployment or StatefulSet). Although you wouldn't typically use a standalone Pod, the following example uses one for simplicity.

The following example consumes the volume that you created in the previous section:
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: web-server
    spec:
      containers:
       - name: web-server
         image: nginx
         volumeMounts:
           # The path in the container where the volume will be mounted.
           - mountPath: /var/lib/www/html
             # The name of the volume that is being defined in the "volumes" section.
             name: mypvc
      volumes:
       - name: mypvc
         persistentVolumeClaim:
           # References the PersistentVolumeClaim created earlier.
           claimName: podpvc
           readOnly: false
    

### GKE Autopilot storage compatibility scheduling

In Autopilot clusters, GKE automatically manages node provisioning and resource allocation. To have Autopilot provision nodes that are compatible with the requested storage type, you must specify the `use-allowed-disk-topology: "true"` parameter in your custom `StorageClass` definition.

Configuring this parameter enforces the following scheduling behaviors:

  * The Cluster Autoscaler provisions only new nodes with machine types that support the requested disk type.
  * The Pod is scheduled on a compatible node. This scheduling prevents the Pod from getting stuck in the `ContainerCreating` or `Pending` states.



For more information, see [Supported node scheduling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/hyperdisk#supported_node_scheduling).

Newer machine series, such as C3 or E4, require Google Cloud Hyperdisk storage (such as `hyperdisk-balanced`). These machine series don't support earlier Persistent Disk volume types, such as standard Persistent Disk (`pd-standard`) or SSD Persistent Disk (`pd-ssd`) volumes. Storage compatibility affects scheduling as follows:

  * **Silent fallback** : if a stateful workload uses an earlier Persistent Disk volume type, such as standard Persistent Disk (`pd-standard`) or SSD Persistent Disk (`pd-ssd`) volumes, but doesn't explicitly request a specific machine series, GKE automatically schedules the Pods on E2 nodes because they support these Persistent Disk volume types. The workload silently falls back from the default newer hardware.
  * **Scheduling failure (Pending)** : you might explicitly request a newer machine series (for example, using `nodeSelector` fields or a custom ComputeClass). If you also attach an earlier Persistent Disk volume type, such as standard Persistent Disk (`pd-standard`) or SSD Persistent Disk (`pd-ssd`) volumes, GKE can't find a node that satisfies both constraints. The Pod remains in the `Pending` state.
  * **Multi-storage type conflict (Pending)** : if a Pod references multiple PVCs that use different storage types (for example, combining an earlier Persistent Disk volume type like standard Persistent Disk (`pd-standard`) and Google Cloud Hyperdisk storage), GKE might not be able to find a node type that supports all constraints. In this scenario, the Pod remains in the `Pending` state.
  * **Insufficient CPU request for extreme disks (Pending)** : extreme volume types, such as `hyperdisk-extreme` and `pd-extreme`, require large VM shapes with high vCPU counts. If your Pod requests too few vCPUs, GKE might provision a node shape that doesn't support the volume type, causing the Pod to remain in the `Pending` state. To help ensure proper scheduling, specify CPU requests that are large enough so that Autopilot provisions a supported VM shape. For the list of supported machine types and minimum vCPU requirements, see [Machine support](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#machine_type_restrictions).



For troubleshooting steps and details about how to verify this behavior by examining logs, see [Workload scheduled on older machine series or stuck in `Pending` state due to storage incompatibility](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/autopilot-clusters#storage-incompatibility-scheduling).

## Use the Compute Engine persistent disk CSI Driver for Windows clusters

The following sections describe the typical process for using a Kubernetes volume backed by a CSI driver in GKE. These sections are specific to clusters using Windows.

Ensure that the:

  * Cluster version is 1.19.7-gke.2000, 1.20.2-gke.2000, or later.
  * Node versions is 1.18.12-gke.1203, 1.19.6-gke.800, or later.



### Create a StorageClass

Creating a StorageClass for Windows is very similar to Linux. You should be aware that the StorageClass installed by default will not work for Windows because the file system type is different. Compute Engine persistent disk CSI Driver for Windows requires `NTFS` as the file system type.

For example, you could create a StorageClass using the following file named `pd- windows-class.yaml`. Make sure to add `csi.storage.k8s.io/fstype: NTFS` to the parameters list:
    
    
    apiVersion: storage.k8s.io/v1
    kind: StorageClass
    metadata:
      name: pd-sc-windows
    provisioner: pd.csi.storage.gke.io
    volumeBindingMode: WaitForFirstConsumer
    allowVolumeExpansion: true
    parameters:
      type: pd-balanced
      **csi.storage.k8s.io/fstype : NTFS**
    

### Create a PersistentVolumeClaim

After creating a StorageClass for Windows, you can now create a PersistentVolumeClaim that references that StorageClass:
    
    
    kind: PersistentVolumeClaim
    apiVersion: v1
    metadata:
      name: podpvc-windows
    spec:
      accessModes:
      - ReadWriteOnce
      **storageClassName : pd-sc-windows**
      resources:
        requests:
          storage: 6Gi
    

### Create a Pod that consumes the volume

The following example consumes the volume that you created in the previous task:
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: web-server
    spec:
      # Node selector to ensure the Pod runs on a Windows node.
      nodeSelector:
        kubernetes.io/os: windows
      containers:
        - name: iis-server
          # The container image to use.
          image: mcr.microsoft.com/windows/servercore/iis
          ports:
          - containerPort: 80
          volumeMounts:
          # The path in the container where the volume will be mounted.
          - mountPath: /var/lib/www/html
            name: mypvc
      volumes:
        - name: mypvc
          persistentVolumeClaim:
            # References the PersistentVolumeClaim created earlier.
            claimName: podpvc-windows
            readOnly: false
    

## Dynamically modify Hyperdisk IOPS and throughput by using `VolumeAttributeClass`

You can use `VolumeAttributesClass` with the Compute Engine persistent disk CSI Driver to dynamically modify persistent disk attributes, including IOPS and throughput. Ensure that your GKE cluster version is 1.34 or later.

This section demonstrates how to use `VolumeAttributesClass` to dynamically modify volume performance. You create two `VolumeAttributesClass` resources, `silver` and `gold`, to define different IOPS and throughput tiers. Then, you create a `StorageClass`, a `PersistentVolumeClaim` referencing the `silver` tier, and a Pod to consume the volume. Finally, you update the `PersistentVolumeClaim` to reference the `gold` tier, which makes a dynamic update to the volume's performance settings.

**Note:** Although StorageClass and Pod manifests for general Persistent Disk volume usage are covered earlier on this page, the following workflow is required to configure and verify the specific performance features of Google Cloud Hyperdisk.

### Create a `VolumeAttributesClass` to define performance tiers

This section defines `VolumeAttributesClass` resources with the example tiers named `silver` and `gold`.

  1. Save the following manifest as `vac-classes.yaml`:
         
         apiVersion: storage.k8s.io/v1
         kind: VolumeAttributesClass
         metadata:
           name: silver
         driverName: pd.csi.storage.gke.io
         parameters:
           iops: "3000"
           throughput: "188Mi"
         ---
         apiVersion: storage.k8s.io/v1
         kind: VolumeAttributesClass
         metadata:
           name: gold
         driverName: pd.csi.storage.gke.io
         parameters:
           iops: "6000"
           throughput: "345Mi"
         

  2. Apply the manifest:
         
         kubectl apply -f vac-classes.yaml
         




### Create a StorageClass for Hyperdisk

This section defines a `StorageClass` resource for provisioning Hyperdisk volumes.

  1. Save the following manifest as `hyperdisk-sc.yaml`:
         
         apiVersion: storage.k8s.io/v1
         kind: StorageClass
         metadata:
           name: hyperdisk-example
         provisioner: pd.csi.storage.gke.io
         volumeBindingMode: WaitForFirstConsumer
         allowVolumeExpansion: true
         parameters:
           type: hyperdisk-balanced
         

  2. Apply the manifest:
         
         kubectl apply -f hyperdisk-sc.yaml
         




### Create a PVC with an initial performance tier

This section creates a PVC and uses the initial tier named `silver`.

  1. Save the following manifest as `vac-silver-pvc.yaml`:
         
         apiVersion: v1
         kind: PersistentVolumeClaim
         metadata:
           name: test-pv-claim
         spec:
           accessModes:
           - ReadWriteOnce
           storageClassName: hyperdisk-example
           volumeAttributesClassName: silver
           resources:
             requests:
               storage: 200Gi
         

  2. Apply the manifest:
         
         kubectl apply -f vac-silver-pvc.yaml
         

  3. To provision a persistent volume, create a Pod that consumes the PVC. The `StorageClass` created in the previous section sets `volumeBindingMode: WaitForFirstConsumer`, which delays volume provisioning until a Pod consumes the PVC. Save the following manifest as `test-pod.yaml`:
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: test-pvc-pod
         spec:
           containers:
             - name: nginx-container
               image: nginx:latest
               ports:
                 - containerPort: 80
               volumeMounts:
                 - name: pvc-storage
                   mountPath: /usr/share/nginx/html
           volumes:
             - name: pvc-storage
               persistentVolumeClaim:
                 claimName: test-pv-claim
         

  4. Apply the manifest:
         
         kubectl apply -f test-pod.yaml
         

  5. To verify disk performance settings, see Verify disk performance settings in Google Cloud console. The **Provisioned IOPS** should be `3000` and **Provisioned throughput** should be `188`, respectively.




### Update the PVC to use a different performance tier

This section updates the PVC to use the `gold` tier instead of the `silver` tier.

  1. Save the following manifest as `vac-gold-pvc.yaml`:
         
         apiVersion: v1
         kind: PersistentVolumeClaim
         metadata:
           name: test-pv-claim
         spec:
           accessModes:
           - ReadWriteOnce
           storageClassName: hyperdisk-example
           volumeAttributesClassName: gold
           resources:
             requests:
               storage: 200Gi
         

  2. Apply the manifest:
         
         kubectl apply -f vac-gold-pvc.yaml
         

  3. To verify that disk performance settings are updated, see Verify disk performance settings in Google Cloud console. The **Provisioned IOPS** should be `6000` and **Provisioned throughput** should be `345`, respectively.




### Verify disk performance settings in Google Cloud console

You can verify that the IOPS and throughput settings are applied to the persistent disk by checking the disk details in the Google Cloud console.

  1. Get the disk name:
         
         PV_NAME=$(kubectl get pvc test-pv-claim -o=jsonpath='{.spec.volumeName}')
         DISK_NAME=$(kubectl get pv $PV_NAME -o=jsonpath='{.spec.csi.volumeHandle}' | sed 's|.*/||')
         echo "Persistent disk name: $DISK_NAME"
         

  2. In the Google Cloud console, go to the **Disks** page.

[Go to Disks](https://console.cloud.google.com/compute/disks)

  3. Click the name of the persistent disk that matches the disk name from the previous step's output.

  4. On the **Disk details** page, in the **Performance** section, view **Provisioned IOPS** and **Provisioned throughput**.




For more information, see [View the provisioned performance settings for Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/analyze-iops-hyperdisk#view_provisioned).

### Considerations for dynamic modification

  * **Re-apply previous configurations:** if a PVC can't bind with a volume attributes class due to an error, such as unavailable resources, you can safely re-apply the previous PVC.
  * **Quota Support:** Kubernetes control plane can enforce quotas on PVCs referencing a specific `VolumeAttributesClass` by using `scopeSelector` in `ResourceQuota`.



## Use the Compute Engine persistent disk CSI Driver with non-default filesystem types

The default filesystem type for Compute Engine persistent disks in GKE is `ext4`. You can also use the `xfs` storage type as long as your node image supports it. See [Storage driver support](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images#storage_driver_support) for a list of supported drivers by node image.

The following example shows you how to use `xfs` as the default filesystem type instead of `ext4` with the Compute Engine persistent disk CSI Driver.

### Create a StorageClass

  1. Save the following manifest as a YAML file named `pd-xfs-class.yaml`:
         
         apiVersion: storage.k8s.io/v1
         kind: StorageClass
         metadata:
           name: xfs-class
         provisioner: pd.csi.storage.gke.io
         parameters:
           # The type of Compute Engine persistent disk to provision.
           type: pd-balanced
           # Specify "xfs" as the filesystem type.
           csi.storage.k8s.io/fstype: xfs
         volumeBindingMode: WaitForFirstConsumer
         

  2. Apply the manifest:
         
         kubectl apply -f pd-xfs-class.yaml
         




### Create a PersistentVolumeClaim

  1. Save the following manifest as `pd-xfs-pvc.yaml`:
         
         apiVersion: v1
         kind: PersistentVolumeClaim
         metadata:
           name: xfs-pvc
         spec:
           # References the StorageClass created earlier.
           storageClassName: xfs-class
           accessModes:
             - ReadWriteOnce
           resources:
             requests:
               # The amount of storage requested.
               storage: 10Gi
         

  2. Apply the manifest:
         
         kubectl apply -f pd-xfs-pvc.yaml
         




### Create a Pod that consumes the volume

  1. Save the following manifest as `pd-xfs-pod.yaml`:
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: pd-xfs-pod
         spec:
           containers:
           - name: cloud-sdk
             image: google/cloud-sdk:slim
             # Keep the container running for 1 hour.
             args: ["sleep","3600"]
             volumeMounts:
             # The path in the container where the volume will be mounted.
             - mountPath: /xfs
               name: xfs-volume
           # Define the volumes available to the containers in the Pod.
           volumes:
           - name: xfs-volume
             persistentVolumeClaim:
               # References the PersistentVolumeClaim created earlier.
               claimName: xfs-pvc
         

  2. Apply the manifest:
         
         kubectl apply -f pd-xfs-pod.yaml
         




### Verify that the volume was mounted correctly

  1. Open a shell session in the Pod:
         
         kubectl exec -it pd-xfs-pod -- /bin/bash
         

  2. Look for `xfs` partitions:
         
         df -aTh --type=xfs
         

The output should be similar to the following:
         
         Filesystem     Type  Size  Used Avail Use% Mounted on
         /dev/sdb       xfs    30G   63M   30G   1% /xfs
         




## View logs for Compute Engine persistent disk CSI Driver

You can use Cloud Logging to view events that relate to the Compute Engine persistent disk CSI Driver. Logs can help you troubleshoot issues.

For more information about Cloud Logging, see [Viewing your GKE logs](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/using-logs).

To view logs for the Compute Engine persistent disk CSI Driver, complete the following steps:

  1. Go to the **Cloud Logging** page in the Google Cloud console.

[Go to Cloud Logging](https://console.cloud.google.com/logs)

  2. To filter log entries to show only the entries related to the CSI Driver that runs in your namespace, run the following Cloud Logging query:
         
         resource.type="k8s_container"
          resource.labels.project_id="PROJECT_ID"
          resource.labels.location="LOCATION"
          resource.labels.cluster_name="CLUSTER_NAME"
          resource.labels.namespace_name="kube-system"
          resource.labels.container_name="gce-pd-driver"
         

Replace the following:

     * `PROJECT_ID`: the name of your project.
     * `LOCATION`: the Compute Engine region or zone of the cluster.
     * `CLUSTER_NAME`: the name of your cluster.



## Known issues

### Unsupported machine types

If you are using the C3 series machine family, the `pd-standard` persistent disk type is not supported.

### Autopilot storage compatibility scheduling

For workloads running in Autopilot mode (in either Autopilot clusters or Standard clusters using Autopilot ComputeClasses), Pods with attached persistent storage are scheduled only on compatible machine series:

  * **Legacy Persistent Disks** : Pods using legacy `pd-standard` disks run only on machine series that support them, such as `E2` nodes.
  * **Hyperdisk** : Pods using next-generation storage like `hyperdisk-balanced` run on newer machine series, such as `C3` nodes.
  * **Pending state** : If you explicitly configure a Pod to run on a newer machine series (for example, by using node selectors to request `C3` nodes, or by configuring a custom ComputeClass) but attach a legacy `pd-standard` disk, the Pod remains in the `Pending` state indefinitely. This occurs because GKE cannot find a node that satisfies both the machine type and disk compatibility constraints. When you explicitly select a machine series, you are responsible for ensuring PersistentVolume and disk compatibility.



If you attempt to run a Pod on a machine, and the Pod uses an unsupported persistent disk type, you will see a warning message like the following emitted on the Pod:
    
    
    AttachVolume.Attach failed for volume "pvc-d7397693-5097-4a70-9df0-b10204611053" : rpc error: code = Internal desc = unknown Attach error: failed when waiting for zonal op: operation operation-1681408439910-5f93b68c8803d-6606e4ed-b96be2e7 failed (UNSUPPORTED_OPERATION): [pd-standard] features are not compatible for creating instance.
    

If your cluster has multiple node pools with different machine families, you can use [node taints](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) and [node affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) to limit where workloads can be scheduled. For example, you can use this approach to restrict a workload using `pd-standard` from running on an unsupported machine family.

If you are using the `pd-extreme` persistent disk type, you need to ensure that your disk is attached to a VM instance with a suitable machine shape. To learn more, refer to [Machine shape support](https://docs.cloud.google.com/compute/docs/disks/extreme-persistent-disk#machine_shape_support).

## What's next

  * [Learn how to use volume expansion](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/volume-expansion).
  * [Learn how to use volume snapshots](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/volume-snapshots).
  * [Learn how to use volume cloning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/volume-cloning).
  * [Learn how to create regional persistent disks](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/regional-pd).
  * [Read more about the driver on GitHub](https://github.com/kubernetes-sigs/gcp-compute-persistent-disk-csi-driver).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
