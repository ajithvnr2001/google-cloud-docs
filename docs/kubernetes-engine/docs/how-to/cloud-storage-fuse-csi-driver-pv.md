---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-pv/
title: Mount Cloud Storage buckets as persistent volumes \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:00:19.552100+00:00
---

# Mount Cloud Storage buckets as persistent volumes  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-pv/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Mount Cloud Storage buckets as persistent volumes Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This guide shows you how to use [Kubernetes persistent volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) backed by your Cloud Storage buckets to manage storage resources for your Kubernetes [Pods](https://kubernetes.io/docs/concepts/workloads/pods/) on Google Kubernetes Engine (GKE). Consider using this storage option if you are already familiar with PersistentVolumes and want consistency with your existing deployments that rely on this resource type.

This guide is for Platform admins and operators users who want to simplify storage management for their GKE applications.

Before reading this page, ensure you're familiar with Kubernetes persistent volumes, Kubernetes Pods, and Cloud Storage buckets.

If you want a streamlined Pod-based interface that requires no previous experience with Kubernetes persistent volumes, see [Mount Cloud Storage buckets as CSI ephemeral volumes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-ephemeral).

## Before you begin

Make sure you have completed these prerequisites:

  * Understand the [requirements](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cloud-storage-fuse-csi-driver#requirements) and [limitations](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cloud-storage-fuse-csi-driver#limitations) of the Cloud Storage FUSE CSI driver.
  * [Create the Cloud Storage bucket](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-setup#create-bucket)
  * [Enable the Cloud Storage FUSE CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-setup#enable)
  * [Configure access to Cloud Storage buckets](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-setup#authentication)



## How persistent volumes for Cloud Storage buckets work

With [static provisioning](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#static), you create one or more [PersistentVolume](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes#persistentvolumes) objects containing the details of the underlying storage system. Pods in your clusters can then consume the storage through [PersistentVolumeClaims](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes#persistentvolumeclaims).

Using a persistent volume backed by a Cloud Storage bucket involves these operations:

  1. **Storage definition** : You define a PersistentVolume in your GKE cluster, including the CSI driver to use and any required parameters. For Cloud Storage FUSE CSI driver, you specify the bucket name and other relevant details.

Optionally, you can fine-tune the performance of your CSI driver by using the [file caching](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-perf#file-caching) feature. File caching can boost GKE app performance by caching frequently accessed Cloud Storage files on a faster local disk.

Additionally, you can use the [parallel download](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-perf#parallel-download) feature to accelerate reading large files from Cloud Storage for multi-threaded downloads. You can use this feature to improve model load times, especially for reads of over 1 GB in size.

**Tip:** For additional ways to fine-tune the performance of your CSI driver, see [Optimize performance for the Cloud Storage FUSE CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-perf).
  2. **Driver invocation** : When a PersistentVolumeClaim requests storage matching the PersistentVolume's specification, GKE invokes the Cloud Storage FUSE CSI driver.

  3. **Bucket mounting** : The CSI driver mounts the bucket to the node where the requesting Pod is scheduled. This makes the bucket's contents accessible to the Pod as a directory in the Pod's local file system. To fine-tune how buckets are mounted in the file system, you can use [mount options](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-perf#mount-options). You can also use [volume attributes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-perf#volume-attributes) to configure specific behavior of the Cloud Storage FUSE CSI driver.

  4. **Re-attachment** : If the Pod restarts or is rescheduled to another node, the CSI driver remounts the same bucket to the new node, ensuring data accessibility.




## Create a PersistentVolume

  1. Create a PersistentVolume manifest with the following specification:

### Pod
         
         apiVersion: v1
         kind: PersistentVolume
         metadata:
           name: gcs-fuse-csi-pv
         spec:
           accessModes:
           - ReadWriteMany
           capacity:
             storage: 5Gi
           storageClassName: example-storage-class  **  mountOptions:
             - implicit-dirs
           csi:
             driver: gcsfuse.csi.storage.gke.io
             volumeHandle: BUCKET_NAME
           claimRef:
             name: gcs-fuse-csi-static-pvc
             namespace: NAMESPACE  **
         

Replace the following values:

     * NAMESPACE: the Kubernetes namespace where you want to deploy your Pod.
     * BUCKET_NAME: the Cloud Storage bucket name you specified when [configuring access to the Cloud Storage buckets](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-setup#authentication). You can specify an underscore (`_`) to mount all buckets that the Kubernetes ServiceAccount can access. To learn more, see [Dynamic mounting](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/mount-bucket#dynamic-mount) in the Cloud Storage FUSE documentation.

The example manifest shows these required settings:

     * `spec.csi.driver`: use `gcsfuse.csi.storage.gke.io` as the CSI driver name.

Optionally, you can adjust these variables:

     * `spec.mountOptions`: Pass [mount options](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-perf#mount-options) to Cloud Storage FUSE. Specify the flags as a list. For more details, see [persistent volume mount options](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#mount-options).
     * `spec.csi.volumeAttributes`: Pass additional [volume attributes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-perf#volume-attributes) to Cloud Storage FUSE.

### Pod (file caching)
    
    apiVersion: v1
    kind: PersistentVolume
    metadata:
      name: gcs-fuse-csi-pv
    spec:
      accessModes:
      - ReadWriteMany
      capacity:
        storage: 5Gi
      storageClassName: example-storage-class **  mountOptions:
        - implicit-dirs
        - file-cache:max-size-mb:-1
      csi:
        driver: gcsfuse.csi.storage.gke.io
        volumeHandle: BUCKET_NAME
      claimRef:
        name: gcs-fuse-csi-static-pvc
        namespace: NAMESPACE **
    

Replace the following values:

     * NAMESPACE: the Kubernetes namespace where you want to deploy your Pod.
     * BUCKET_NAME: the Cloud Storage bucket name you specified when configuring access to the Cloud Storage buckets. You can specify an underscore (`_`) to mount all buckets that the Kubernetes ServiceAccount can access. To learn more, see [Dynamic mounting](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/mount-bucket#dynamic-mount) in the Cloud Storage FUSE documentation.

### Pod (parallel download)
    
    apiVersion: v1
    kind: PersistentVolume
    metadata:
      name: gcs-fuse-csi-pv
    spec:
      accessModes:
      - ReadWriteMany
      capacity:
        storage: 5Gi
      storageClassName: example-storage-class **  mountOptions:
        - implicit-dirs
        - file-cache:enable-parallel-downloads:true
        - file-cache:max-size-mb:-1
      csi:
        driver: gcsfuse.csi.storage.gke.io
        volumeHandle: BUCKET_NAME
      claimRef:
        name: gcs-fuse-csi-static-pvc
        namespace: NAMESPACE **
    

Replace the following values:

     * NAMESPACE: the Kubernetes namespace where you want to deploy your Pod.
     * BUCKET_NAME: the Cloud Storage bucket name you specified when configuring access to the Cloud Storage buckets. You can specify an underscore (`_`) to mount all buckets that the Kubernetes ServiceAccount can access. To learn more, see [Dynamic mounting](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/mount-bucket#dynamic-mount) in the Cloud Storage FUSE documentation.

  2. Apply the manifest to the cluster:
         
         kubectl apply -f PV_FILE_PATH
         

Replace PV_FILE_PATH with the path to your YAML file.




## Create a PersistentVolumeClaim

  1. Create a PersistentVolumeClaim manifest with the following specification:
         
         apiVersion: v1
         kind: PersistentVolumeClaim
         metadata:
           name: gcs-fuse-csi-static-pvc
           namespace: NAMESPACE
         spec:
           accessModes:
           - ReadWriteMany
           resources:
             requests:
               storage: 5Gi
           storageClassName: example-storage-class
         

Replace the NAMESPACE with the Kubernetes namespace where you want to deploy your Pod.

To bind your PersistentVolume to a PersistentVolumeClaim, check these configuration settings:

     * `spec.storageClassName`: The `storageClassName` in the PersistentVolume and PersistentVolumeClaim manifests must match for the claim to bind to the volume. The Cloud Storage FUSE CSI driver doesn't use `StorageClass` objects. You only need to ensure the `storageClassName` field is identical in both resources. You can use an empty or non-empty string for this field; it does not need to refer to an existing StorageClass object and serves only as a binding label between the PV and PVC.
     * `spec.accessModes` fields in your PersistentVolume and PersistentVolumeClaim manifests should match.
     * `spec.capacity.storage` field in your PersistentVolume manifest should match the `spec.resources.requests.storage` in the PersistentVolumeClaim manifest. Since Cloud Storage buckets don't have size limits, you can put any number for capacity but it can't be empty.
  2. Apply the manifest to the cluster:
         
         kubectl apply -f PVC_FILE_PATH
         

Replace PVC_FILE_PATH with the path to your YAML file.




## Consume the volume in a Pod

  1. Create a Pod manifest with the following specification:
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: gcs-fuse-csi-example-static-pvc  **  namespace: NAMESPACE
           annotations:
             gke-gcsfuse/volumes: "true"
         spec:
           containers:
           - image: busybox
             name: busybox
             command: ["sleep"]
             args: ["infinity"]
             volumeMounts:
             - name: gcs-fuse-csi-static
               mountPath: /data
               readOnly: true
           serviceAccountName: KSA_NAME
           volumes:
           - name: gcs-fuse-csi-static
             persistentVolumeClaim:
               claimName: gcs-fuse-csi-static-pvc
               readOnly: true  **
         

Replace the following values:

     * NAMESPACE: the Kubernetes namespace where you want to deploy your Pod.
     * KSA_NAME: the Kubernetes ServiceAccount name that you created when [configuring access to the Cloud Storage buckets](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-setup#authentication).

The example manifest shows these required settings:

     * `metadata.annotations`: the annotation `gke-gcsfuse/volumes: "true"` is required. See [Configure the sidecar container](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-sidecar) for optional annotations.

Optionally, you can adjust these variables:

     * `spec.containers[n].volumeMounts[n].readOnly`: Specify true if only specific volume mounts are read-only.
     * `spec.volumes[n].persistentVolumeClaim.readOnly`: Specify true if all volume mounts are read-only.
  2. Apply the manifest to the cluster:
         
         kubectl apply -f POD_FILE_PATH
         

Replace POD_FILE_PATH with the path to your YAML file.




### (Optional) Mount the same Cloud Storage bucket with different PersistentVolumes

Starting from GKE version 1.33.0-gke.1932000, you can use multiple PersistentVolumes that are backed by the same Cloud Storage bucket. In each PersistentVolume object, you must use a unique `volumeHandle` in the format BUCKET_NAME:UNIQUE_SUFFIX.

An example use case could be mounting different PersistentVolumes with different mount options to the same Pod, where each PersistentVolume refers to the same Cloud Storage bucket.

## Troubleshoot issues

For more information about troubleshooting the Cloud Storage FUSE CSI driver, see the [troubleshooting guide](https://github.com/GoogleCloudPlatform/gcs-fuse-csi-driver/blob/main/docs/troubleshooting.md) in the GitHub project documentation.

## What's next

  * [Learn how to optimize performance for the Cloud Storage FUSE CSI driver.](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-perf)
  * [Explore additional samples for using the CSI driver on GitHub](https://github.com/GoogleCloudPlatform/gcs-fuse-csi-driver/blob/main/examples/README.md).
  * [Learn more about Cloud Storage FUSE](https://docs.cloud.google.com/storage/docs/gcs-fuse).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
