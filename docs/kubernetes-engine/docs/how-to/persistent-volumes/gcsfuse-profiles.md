---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/gcsfuse-profiles/
title: Automate performance tuning with Cloud Storage FUSE profiles \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:02:08.625747+00:00
---

# Automate performance tuning with Cloud Storage FUSE profiles  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/gcsfuse-profiles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Automate performance tuning with Cloud Storage FUSE profiles Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document describes how you can automatically tune the performance of the [Cloud Storage FUSE CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cloud-storage-fuse-csi-driver) and accelerate data access of your AI/ML workloads by using the Cloud Storage FUSE profiles on Google Kubernetes Engine (GKE).

Cloud Storage FUSE profiles automate the critical performance tuning process. Instead of manually adjusting settings, you can apply predefined profiles that configure the CSI driver for you. For your AI/ML applications, using these profiles can lead to faster training and inference times with reduced operational overhead.

This document is for Application developers and Machine learning (ML) engineers who want to improve the performance of their applications without deep storage tuning expertise. To learn more about common roles, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

Before reading this document, make sure that you're familiar with the basics of Cloud Storage, Kubernetes, and the Cloud Storage FUSE CSI driver. Also, review the [requirements for using the Cloud Storage FUSE CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cloud-storage-fuse-csi-driver#requirements).

## Benefits of using Cloud Storage FUSE profiles

To automate performance tuning for AI/ML workloads, Cloud Storage FUSE profiles use [predefined Cloud Storage FUSE configurations](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/profile-based-configurations) and apply additional GKE-specific settings. These settings are based on [Cloud Storage FUSE performance tuning best practices](https://docs.cloud.google.com/storage/docs/gcsfuse-performance). Using predefined profiles offers the following benefits:

  * **Simplified performance tuning** : use predefined Cloud Storage FUSE profiles to apply the optimized configurations for common AI/ML workloads, such as training, serving, and checkpointing.
  * **Dynamic, resource-aware optimization** : using the Cloud Storage FUSE profiles lets the CSI driver automatically adjust cache sizes and select the optimal cache medium, such as RAM or Local SSD, based on bucket or sub-directory characteristics, such as size, object count, and location type, sidecar limits, and your node's available resources.
  * **Accelerated read performance** : when you use the `gcsfusecsi-serving` profile, GKE automatically enables [Rapid Cache](https://docs.cloud.google.com/storage/docs/rapid/rapid-cache) to improve read performance for your serving workloads.
  * **Performance tuning insights** : you gain insight into the automated tuning decisions through structured logs that detail the input signals from your environment and the resulting configurations applied by the driver. For more information, see View recommendation insights



As [Cloud Storage FUSE best practices](https://docs.cloud.google.com/storage/docs/gcsfuse-performance) evolve, the profiles are updated over time through new GKE releases.

## Limitations

  * You can't use Cloud Storage FUSE profiles with the [Cloud Storage FUSE CSI ephemeral volumes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-ephemeral).
  * The profiles don't support [dynamic mounting](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/mount-bucket#dynamic-mount), where you specify an underscore (_) to mount all buckets that the Kubernetes ServiceAccount can access.
  * Overriding the sidecar image with a custom private sidecar image isn't supported. For more information, see [Configure a private image for the sidecar container](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-sidecar#configure-a-private-image).



## Requirements

  * Your GKE cluster must be running version 1.35.1-gke.1616000 or later.
  * Your cluster must have the Cloud Storage FUSE CSI driver enabled. If you're creating a new cluster, or enabling the driver on an existing one, refer to the following steps in the document to set up the Cloud Storage FUSE CSI driver for GKE: 
    * [Create the Cloud Storage bucket](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-setup#create-bucket).
    * [Enable the Cloud Storage FUSE CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-setup#enable).
    * [Configure access to Cloud Storage buckets](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-setup#authentication).



## Costs

In addition to the standard [GKE](https://docs.cloud.google.com/kubernetes-engine/pricing) and [Cloud Storage](https://docs.cloud.google.com/storage/pricing) costs associated with the Cloud Storage FUSE CSI Driver, using Cloud Storage FUSE profiles incurs the following costs.

### Bucket scanning costs

Cloud Storage FUSE profiles perform a background scan of your bucket or subdirectory. By default, this scan occurs every seven days. Bucket scanning incurs [Cloud Storage Class A operation charges](https://docs.cloud.google.com/storage/pricing#operation-charges) for listing objects.

### Rapid Cache costs

The `gcsfusecsi-serving` profile automatically enables Rapid Cache, which is billed according to [Cloud Storage Rapid Cache pricing](https://cloud.google.com/storage/pricing#rapid-cache). To avoid incurring charges for cache instances when they are no longer needed, see [Cost controls](https://docs.cloud.google.com/storage/docs/rapid/rapid-cache#cost-controls).

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Cloud Storage API and the Google Kubernetes Engine API. 
[ Enable APIs ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com,storage.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Choose a Google Cloud region that is appropriate for your needs. Although we _recommend_ creating your GKE cluster and your Cloud Storage bucket in the same region to optimize performance and cost, it's _mandatory_ to do so when you use the `gcsfusecsi-serving` profile or plan to enable Rapid Cache.
  * Ensure that you have an existing Cloud Storage bucket containing the dataset, model, or checkpoints for your AI/ML workload. If you need to create a bucket, see [Create a bucket](https://docs.cloud.google.com/storage/docs/creating-buckets).



## Select a performance profile

Choose a profile that best matches your workload. Each profile corresponds to a pre-installed StorageClass on your cluster. For detailed definitions of the Cloud Storage FUSE profiles, see the corresponding StorageClass configuration reference.

Profile | StorageClass name | Optimized for | Key features  
---|---|---|---  
Training | `gcsfusecsi-training` | High-throughput reads | Optimizes data latency for GPUs and TPUs during training on large datasets.  
Checkpointing | `gcsfusecsi-checkpointing` | High-throughput writes | Minimizes time required to save large checkpoints, reducing training pauses.  
Serving | `gcsfusecsi-serving` | Data access and caching | Enables Rapid Cache by default to accelerate read operations.  
  
You can verify the StorageClasses installed in your cluster by running the following command:
    
    
    kubectl get sc -l gke-gcsfuse/profile=true
    

### Configure IAM permissions

Grant the [GKE Service Agent](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/service-accounts#kubernetes-engine-service-agent) permissions to analyze your Cloud Storage bucket and manage Rapid Cache.

Replace the following placeholders when running the commands in this section:

  * `GCS_PROJECT`: the project ID containing your Cloud Storage bucket.
  * `PROJECT_NUMBER`: the project number of your GKE cluster project.
  * `BUCKET_NAME`: the name of your Cloud Storage bucket.



Choose one of the following options that matches your profile and usage needs.

#### Option A: Custom role (Recommended)

This option is required for the Serving profile, or if Rapid Cache is used. If you use the Serving profile or plan to manually enable Rapid Cache for other profiles, you must grant permissions to manage that cache.

**Note:** This custom role is comprehensive. It includes all necessary permissions for all profiles (Serving, Training, and Checkpointing). If you set up this role, you don't need to add any other storage roles for the other profiles.

  1. Create a custom IAM role that allows scanning objects and creating Rapid Cache caches:
         
         gcloud iam roles create gke.gcsfuse.profileUser \
           --project=GCS_PROJECT \
           --title="GKE GCSFuse Profile User" \
           --description="Allows scanning Cloud Storage buckets for objects, retrieving bucket metadata, and creating caches." \
           --permissions="storage.objects.list,storage.buckets.get,storage.anywhereCaches.create,storage.anywhereCaches.get,storage.anywhereCaches.list,storage.anywhereCaches.update"
         

  2. Bind the custom role to the GKE Service agent for your specific bucket:
         
         gcloud storage buckets add-iam-policy-binding gs://BUCKET_NAME \
           --project=GCS_PROJECT \
           --member="serviceAccount:service-PROJECT_NUMBER@container-engine-robot.iam.gserviceaccount.com" \
           --role="projects/GCS_PROJECT/roles/gke.gcsfuse.profileUser"
         




#### Option B: Standard role for Training and Checkpointing profiles

If you're using only the Training or Checkpointing profiles and don't plan to use Rapid Cache, run the following command:
    
    
    gcloud storage buckets add-iam-policy-binding gs://BUCKET_NAME \
        --project=GCS_PROJECT \
        --member="serviceAccount:service-PROJECT_NUMBER@container-engine-robot.iam.gserviceaccount.com" \
        --role="roles/storage.legacyBucketReader"
    

## Deploy a workload with a Cloud Storage FUSE profile

Follow these steps to deploy a workload with a Cloud Storage FUSE profile.

  1. Create a PersistentVolume (PV) manifest that references one of the Cloud Storage FUSE profile StorageClasses:
         
         apiVersion: v1
         kind: PersistentVolume
         metadata:
           name: my-pv
         spec:
           accessModes:
           - ReadWriteMany
           capacity:
             storage: 5Gi
           persistentVolumeReclaimPolicy: Retain
           **storageClassName : STORAGECLASS_NAME**
           mountOptions:
             - only-dir=BUCKET_DIR_PATH # Optional
           csi:
             driver: gcsfuse.csi.storage.gke.io
             volumeHandle: BUCKET_NAME
         

Replace the following:

     * `STORAGECLASS_NAME`: the StorageClass name of the profile that you want to use. The value must be `gcsfusecsi-training`, `gcsfusecsi-checkpointing`, or `gcsfusecsi-serving`.
     * `BUCKET_DIR_PATH`: (optional) the path within your Cloud Storage bucket, if you're mounting a specific directory. If specified, GKE scans this path for optimization. If omitted, GKE scans the entire bucket.
     * `BUCKET_NAME`: the Cloud Storage bucket name you specified when [configuring access to Cloud Storage buckets](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-setup#authentication).
  2. Create a PersistentVolumeClaim (PVC) that requests the same StorageClass as your PV:
         
         apiVersion: v1
         kind: PersistentVolumeClaim
         metadata:
           name: my-pvc
           namespace: NAMESPACE
         spec:
           accessModes:
             - ReadWriteMany
           resources:
             requests:
               storage: 5Gi
           volumeName: my-pv
           **storageClassName : STORAGECLASS_NAME**
         

Replace the following:

     * `NAMESPACE`: the namespace where you want to deploy your Pod.
     * `STORAGECLASS_NAME`: the StorageClass name as listed in your PV.
  3. Consume the PVC in your Deployment:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: my-deployment
           namespace: NAMESPACE
         spec:
           replicas: 3
           selector:
             matchLabels:
               app: my-app
           template:
             metadata:
               labels:
                 app: my-app
               annotations:
                 **gke-gcsfuse/volumes : "true"**
             spec:
               serviceAccountName: KSA_NAME
               containers:
               - name: my-container
                 image: busybox
                 volumeMounts:
                 - name: my-gcs-volume
                   mountPath: "/data"
               volumes:
               - name: my-gcs-volume
                 persistentVolumeClaim:
                   claimName: my-pvc
         

Replace the following:

     * `NAMESPACE`: the namespace where you want to deploy your Pod.
     * `KSA_NAME`: the Kubernetes ServiceAccount name that you created when [configuring access to Cloud Storage buckets](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-setup#authentication).



After it's deployed, the CSI driver automatically calculates optimal cache sizes and mount options based on your node's resources, such as GPUs or TPUs, memory, Local SSD, the bucket or sub-directory size, and the sidecar resource limits.

## Verify the automated optimization

GKE background processes automatically analyze your bucket, and synchronize Rapid Cache (if being used).

### Check the status of both the bucket scan and the cache

After you create the PV, follow these steps to check the status of both the bucket scan and the cache. You don't need to wait for the Pod to be deployed.

  1. Check the PV status:
         
         kubectl describe pv my-pv
         

  2. In the output, verify that the `ScanOperationSucceeded` event appears. The output is similar to the following:
         
         Normal  ScanOperationSucceeded  gke-gcsfuse-scanner  Bucket scan completed successfully for bucket "my-bucket", directory "my-dir": "526893" objects, "57690897566" bytes
         

  3. If you use the `gcsfusecsi-serving` profile, verify that the `AnywhereCacheSyncSucceeded` event appears after the caching layer is ready. The output is similar to the following:
         
         Normal  AnywhereCacheSyncSucceeded  gke-gcsfuse-scanner  Anywhere Cache sync succeeded for PV "my-pv": us-central1-c:running
         

**Note:** Rapid Cache creation can take several minutes to several hours. Your workloads aren't blocked during this time and can read data directly from the bucket until the cache is operational. For more information, see [Create a cache](https://docs.cloud.google.com/storage/docs/rapid/rapid-cache#create).
  4. Verify that the PV annotations are updated with the scan result:
         
         gke-gcsfuse/bucket-scan-status: completed
         gke-gcsfuse/bucket-scan-num-objects: 526893
         gke-gcsfuse/bucket-scan-total-size-bytes: 57690897566
         gke-gcsfuse/bucket-scan-location-type: multi-region
         gke-gcsfuse/bucket-scan-hns-enabled: true
         gke-gcsfuse/bucket-scan-last-updated-time: 2025-12-10T22:48:38Z
         




### Check Pod status

After you deploy the Pod, run the following command:
    
    
    kubectl get pods -n NAMESPACE
    

Replace `NAMESPACE` with the namespace where you deployed your Pods.

Your Pods should now be in `RUNNING` status, with performance best practices automatically applied. If your Pods show the `SchedulingGated` status, it indicates that GKE is still scanning your bucket or sub-directory. The Pods remain in this state until the CSI controller completes the scan and updates the PV.

To understand the specific tuning decisions logged by the driver after the Pod starts, see View recommendation insights.

If you encounter any errors, see the Troubleshooting section.

## StorageClass configuration reference

This section provides the StorageClass manifests for the pre-installed Cloud Storage FUSE profiles, and a detailed reference for the mount options and parameters used by the Profiles. These configurations let the `gcsfuse.csi.storage.gke.io` driver automate performance tuning and resource management for your AI/ML workloads.

**Note:** Training and Checkpointing profiles don't have Rapid Cache enabled by default. To enable it for these workloads, add the `anywhereCacheZones` parameter to your PV manifest under the `spec.csi.volumeAttributes` field.

### Training
    
    
    apiVersion: storage.k8s.io/v1
    kind: StorageClass
    metadata:
      name: gcsfusecsi-training
      labels:
        gke-gcsfuse/profile: "true"
    provisioner: gcsfuse.csi.storage.gke.io
    mountOptions:
      - **profile:aiml-training**
    parameters:
      skipCSIBucketAccessCheck: "true"
      gcsfuseMetadataPrefetchOnMount: "true"
      fuseFileCacheMediumPriority: "gpu:ram|lssd,tpu:ram,general_purpose:ram|lssd"
      fuseMemoryAllocatableFactor: "0.7"
      fuseEphemeralStorageAllocatableFactor: "0.85"
      bucketScanResyncPeriod: "168h"
      bucketScanTimeout: "2m"
    

### Checkpointing
    
    
    apiVersion: storage.k8s.io/v1
    kind: StorageClass
    metadata:
      name: gcsfusecsi-checkpointing
      labels:
        gke-gcsfuse/profile: "true"
    provisioner: gcsfuse.csi.storage.gke.io
    mountOptions:
      - **profile:aiml-checkpointing**
      - read_ahead_kb=1024
    parameters:
      skipCSIBucketAccessCheck: "true"
      gcsfuseMetadataPrefetchOnMount: "true"
      fuseFileCacheMediumPriority: "gpu:ram|lssd,tpu:ram,general_purpose:ram|lssd"
      fuseMemoryAllocatableFactor: "0.7"
      fuseEphemeralStorageAllocatableFactor: "0.85"
      bucketScanResyncPeriod: "168h"
      bucketScanTimeout: "2m"
    

### Serving
    
    
    apiVersion: storage.k8s.io/v1
    kind: StorageClass
    metadata:
      name: gcsfusecsi-serving
      labels:
        gke-gcsfuse/profile: "true"
    provisioner: gcsfuse.csi.storage.gke.io
    mountOptions:
      - **profile:aiml-serving**
      - read_ahead_kb=131072
      - file-cache:max-size-mb:0
      - read:enable-buffered-read:true
      - read:global-max-blocks:80
    parameters:
      **anywhereCacheZones : "*"**
      anywhereCacheAdmissionPolicy: "admit-on-first-miss"
      anywhereCacheTTL: "1h"
      skipCSIBucketAccessCheck: "true"
      gcsfuseMetadataPrefetchOnMount: "true"
      fuseFileCacheMediumPriority: "gpu:ram|lssd,tpu:ram,general_purpose:ram|lssd"
      fuseMemoryAllocatableFactor: "0.7"
      fuseEphemeralStorageAllocatableFactor: "0.85"
      bucketScanResyncPeriod: "168h"
      bucketScanTimeout: "2m"
    

The profiles use the following mount options and parameters for the `gcsfuse.csi.storage.gke.io` driver:

  * **`mountOptions`** : 
    * `profile`: applies [a predefined set of Cloud Storage FUSE optimizations](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/profile-based-configurations) tailored for AI/ML workloads. The valid values for the pre-installed profiles are `aiml-training`, `aiml-checkpointing`, and `aiml-serving`.
    * `read_ahead_kb`: specifies the size of the [read-ahead buffer](https://docs.cloud.google.com/storage/docs/gcsfuse-performance#increase-read-ahead-size) in kilobytes (KB). This option allows Cloud Storage FUSE to prefetch data from Cloud Storage, potentially improving read performance for sequential access patterns.
    * `file-cache:max-size-mb`: for the Serving profile, specifies the maximum size in mebibytes (MiB) for the file cache. In serving workloads, where models are typically loaded into GPU or TPU memory only once, this parameter is set to `0` to disable the local Cloud Storage FUSE [file cache](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#file-cache-max-size-mb), which helps to prevent redundant disk I/O and saves local storage.
    * `read:enable-buffered-read`: for the Serving profile, enables Cloud Storage FUSE to [manage its own internal buffers](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#enable-buffered-read), which helps to reduce the number of small, expensive system calls between the application and the kernel.
    * `read:global-max-blocks`: for the Serving profile, limits the total number of [concurrent memory blocks](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#read-global-max-blocks) used for buffered reads. This option helps to prevent the FUSE process from consuming all available RAM when serving multiple requests.
  * **`parameters`** : 
    * `skipCSIBucketAccessCheck`: when set to `"true"`, makes the CSI driver [skip the initial bucket access check](https://docs.cloud.google.com/storage/docs/gcsfuse-performance#security-token-service). This parameter helps to reduce calls to the [Security Token Service](https://docs.cloud.google.com/iam/docs/reference/sts/rest) to avoid potential quota issues.
    * `gcsfuseMetadataPrefetchOnMount`: when set to `"true"`, directs the CSI driver to initiate [prefetching](https://docs.cloud.google.com/storage/docs/gcsfuse-performance#pre-populate-the-metadata-cache) of object metadata from Cloud Storage into the local cache as soon as the volume is mounted. This parameter can accelerate the first access to files.
    * `fuseFileCacheMediumPriority`: defines the priority order for storage media used by the Cloud Storage FUSE [file cache](https://docs.cloud.google.com/storage/docs/gcsfuse-performance#enable-file-caching-and-parallel-downloads). It allows specifying different preferences for nodes with GPUs, TPUs, or general-purpose nodes. Media options include `ram` and `lssd` (Local SSD, if available and enabled).
    * `fuseMemoryAllocatableFactor`: specifies in string format a fraction that limits the maximum memory that Cloud Storage FUSE caches can consume, relative to the node's total allocatable memory and sidecar's memory limit.
    * `fuseEphemeralStorageAllocatableFactor`: limits Cloud Storage FUSE cache usage of ephemeral storage on the node (such as Local SSD for file caching), relative to the node's allocatable ephemeral storage or the sidecar's ephemeral storage limited for caching.
    * `bucketScanResyncPeriod`: sets the time interval at which the PV is re-scanned to detect changes made to the Cloud Storage bucket.
    * `bucketScanTimeout`: the maximum duration allowed for a single bucket scan operation. If the scan exceeds this time, partial results may be used.
    * `anywhereCacheZones`: specifies a comma-separated list of [supported zones](https://docs.cloud.google.com/storage/docs/rapid/rapid-cache#supported-locations) where the Rapid Cache caches are created, for example, `"us-central1-a,us-central1-b"`. To use all zones available to the cluster, use `"*"` as the value. Setting this to `"none"` or leaving it unspecified disables Rapid Cache.
    * `anywhereCacheTTL`: the [Time To Live (TTL)](https://docs.cloud.google.com/storage/docs/rapid/rapid-cache#create) for data stored in the Rapid Cache cache, measured from the last access. If you change this value, existing Rapid Cache instances are updated with the new TTL.
    * `anywhereCacheAdmissionPolicy`: determines when to admit data into the Rapid Cache cache after a [_read miss_](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/caching#read-path) (when requested data isn't found in the cache). Options include `"admit-on-first-miss"`, which admits data on the first read miss, or `"admit-on-second-miss"`, which admits data only on a second read miss for the same object. If you change this value, existing Rapid Cache instances are updated with the new policy.



## Optional: Fine-tune profile configurations

You can customize specific settings in a profile while still benefiting from its base configuration. Use the following options to adjust a profile without creating a new StorageClass.

### Override mount options and parameters

To modify specific behaviors, add mount options to the `spec.mountOptions` field, or CSI parameters to the `spec.csi.volumeAttributes` field in your PV. GKE applies your manual settings on top of the profile's defaults.

The following example shows how to override the `read_ahead_kb` mount option and disables the `gcsfuseMetadataPrefetchOnMount` parameter in the Serving profile.
    
    
    apiVersion: v1
    kind: PersistentVolume
    metadata:
      name: my-pv-override
    spec:
      accessModes:
      - ReadWriteMany
      capacity:
        storage: 5Gi
      persistentVolumeReclaimPolicy: Retain
      storageClassName: gcsfusecsi-serving
      mountOptions:
      - **read_ahead_kb=2048** # Overrides the profile's default.
      csi:
        driver: gcsfuse.csi.storage.gke.io
        volumeHandle: my-gcs-bucket
        volumeAttributes:
          **gcsfuseMetadataPrefetchOnMount : "false"** # Overrides the profile's default.
    

Common use cases include the following:

  * To enable Rapid Cache for a Training profile, add the `anywhereCacheZones` parameter directly to your PV spec.
  * To adjust specific Cloud Storage FUSE behaviors, such as increasing the `read_ahead_kb` size, to meet the unique requirements of a particular workload.



When you manually configure cache sizes, consider the following:

  * Specifying a manual cache size overrides automatic dynamic sizing for that specific component only. Dynamic sizing continues for all other components on a best-effort basis within the remaining resource budget.
  * Setting a `metadata-cache` or `file-cache` option, such as `metadata-cache:stat-cache-max-size-mb`, doesn't disable automatic calculation for other cache types.
  * If you manually specify `file-cache:max-size-mb`, you must also configure a [custom read cache volume](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-sidecar#configure-custom-read-cache-volume). This helps to ensure that a storage medium with sufficient capacity is explicitly defined for your custom cache size.



### Bypass bucket scanning with annotations

You can bypass the automatic bucket scanning process by providing your own object count and size metrics by using annotations. The CSI driver uses these values to calculate optimal performance configurations without scanning the bucket.

The following example shows how to add the `gke-gcsfuse/bucket-scan-status: "override"` annotation to your PV, along with the specific metric annotations.
    
    
    apiVersion: v1
    kind: PersistentVolume
    metadata:
      name: my-pv-override
      annotations:
        **gke-gcsfuse/bucket-scan-status : "override"**
        **gke-gcsfuse/bucket-scan-num-objects : 19238**
        **gke-gcsfuse/bucket-scan-total-size-bytes : 94837465**
    spec:
      accessModes:
      - ReadWriteMany
      capacity:
        storage: 5Gi
      persistentVolumeReclaimPolicy: Retain
      storageClassName: STORAGECLASS_NAME
      csi:
        driver: gcsfuse.csi.storage.gke.io
        volumeHandle: BUCKET_NAME
    

Common use cases include the following:

  * If you already know your bucket's size and object count, especially for inference workloads where data rarely changes, you can bypass the scanning time at startup.
  * If the Cloud Storage API is temporarily unavailable, these annotations can help you maintain performance while the underlying services are being fixed.



## Troubleshooting

Use the following information to monitor the status of Cloud Storage FUSE profiles and resolve common issues encountered during bucket scanning and cache synchronization.

### Invalid configuration parameter (`InvalidArgument`)

The background optimization tasks failed to start because one or more parameters provided in your manifest were invalid.

**Symptom**

The PV shows a `ScanOperationStartError` or `AnywhereCacheSyncError` event with a message containing `rpc error: code = InvalidArgument`. Examples include:

  * `Bucket scan timeout configuration error: rpc error: code = InvalidArgument desc = invalid duration format for "INVALID_DURATION".`
  * `Anywhere Cache sync failed for PV "PV_NAME": rpc error: code = InvalidArgument desc = failed to get anywhere cache "CACHE_NAME" ... invalid anywhere cache "CACHE_NAME" provided.`



**Cause**

One or more parameters in your PV's `spec.csi.volumeAttributes` field are formatted incorrectly or contain values that the system can't parse.

**Resolution**

Correct the invalid parameter values in your PV manifest and re-deploy the PV. Ensure that all duration values (like `bucketScanTimeout`) use the correct format (for example, `2m` or `10m`) and that all profile-specific settings match the valid supported values.

### Permission denied when scanning Cloud Storage bucket

GKE can't access the specified Cloud Storage bucket to perform the required performance analysis.

**Symptom**

The PV shows a `ScanOperationStartError` event with an `Error 403: Forbidden` message indicating that the caller doesn't have `storage.buckets.get` access.

**Cause**

The GKE Service Agent is missing the required IAM permissions, or the bucket name is incorrect.

**Resolution**

  * Verify that the bucket name in your PV's `volumeHandle` field is correct and that the bucket exists.
  * Ensure the GKE Service Agent permissions are granted to the `service-PROJECT_NUMBER@container-engine-robot.iam.gserviceaccount.com` identity for the specific bucket. For more information, see Configure IAM permissions.



### Rapid Cache location mismatch

The Rapid Cache cache couldn't be created because the requested zone is not compatible with the bucket's location.

**Symptom**

The PV shows an `AnywhereCacheSyncWarning` event with the message: `Invalid zone. Rapid Cache isn't available in the requested zone.`

**Cause**

Rapid Cache caches must be created in zones that reside within the bucket's regional location. This error typically occurs when your GKE cluster and Cloud Storage bucket are in different regions.

**Resolution**

Move your Cloud Storage bucket to a region that matches your GKE cluster location and re-deploy the PV.

### Bucket scan timed out

The analysis of the Cloud Storage bucket took longer than the configured timeout, resulting in partial optimization results.

**Symptom**

The PV shows a `ScanOperationTimedOut` event. The PV is annotated with partial results for the object count and total size.

**Cause**

The bucket contains an exceptionally large number of objects (typically several millions) that cannot be fully listed within the default two-minute timeout.

**Resolution**

  * Set a larger value for the `bucketScanTimeout` field in your PV's `spec.csi.volumeAttributes` section, for example, `10m`.
  * If the bucket size is static, bypass scanning by manually providing the object count and size.



#### Metadata cache capped by memory budget

The driver limited the metadata cache size to fit within the node's available resources, which might reduce performance.

**Symptom**

The logs contain a message stating that the required metadata stat cache size was capped to the available Cloud Storage FUSE memory budget.

**Cause**

The metadata cache for the number of objects in your bucket exceeds the memory allocated to the Cloud Storage FUSE sidecar or the node's available memory.

**Resolution**

  * Use the `only-dir` mount option to scope the volume to a smaller subdirectory with fewer objects.
  * Increase the memory limit for the [Cloud Storage FUSE sidecar container](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-sidecar#configure-sidecar-resource-limits). 
    * If sidecar limits are already sufficient, use a node type with more allocatable memory.



#### File cache disabled due to resource limits

GKE disabled the local file cache because it could not find a suitable storage medium with enough space.

**Symptom**

The logs show the warning: `No suitable file cache medium found or requirement exceeded limits for all options`.

**Cause**

The calculated file cache size exceeds both the available node's RAM and the available Local SSD storage.

**Resolution**

  * Use the `only-dir` mount option to scope the volume to a smaller subdirectory with fewer objects.
  * Increase the Cloud Storage FUSE sidecar's [resource limits](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-sidecar#configure-sidecar-resource-limits).
  * Use a node type with more memory or enable Local SSDs on your node pool.



### Monitor status by using PersistentVolume events

GKE logs key configuration events and errors to the PV. To check these events, run the following command:
    
    
    kubectl describe pv PV_NAME
    

After the bucket scan succeeds, you see a `ScanOperationSucceeded` event. If you use the `gcsfusecsi-serving` profile, you see an `AnywhereCacheSyncSucceeded` event after the caching layer is operational.

### Monitor status by using CSI driver logs

The Cloud Storage FUSE CSI driver logs detailed configuration decisions and performance insights. To view these logs in [Cloud Logging](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface), use the following query:
    
    
    resource.type="k8s_container"
    resource.labels.pod_name=~"gcsfusecsi-node-.*"
    

### View recommendation insights

To understand the specific input signals and decisions made by the automated tuning logic, search the CSI driver logs for the `GCSFuseCSIRecommendation` string. The resulting JSON payload provides detailed metrics, including the following:

  * `inputSignals`: the bucket object count, total data size, and available node resources (RAM and ephemeral storage).
  * `decision`: the final calculated cache sizes and the selected storage medium (`ram` or `lssd`).


    
    
    {
      "insertId": "INSERT_ID",
      "jsonPayload": {
        "decision": {
          "fileCacheBytes": 300000000,
          "fileCacheMedium": "lssd",
          "metadataStatCacheBytes": 4500,
        },
        "target": {
          "nodeName": "NODE_NAME",
          "pvName": "PV_NAME",
          "podName": "POD_NAME"
        },
        "message": "GCSFuseCSIRecommendation: Recommended cache configs for PV PV_NAME and Pod POD_NAME: FileCache: 287MiB (lssd) | MetadataStatCache: 1MiB | Expand for full details",
        "inputSignals": {
          "requiredFileCacheBytes": 300000000,
          "fuseBudgetMemoryBytes": 187904819,
          "sidecarLimitMemoryBytes": 268435456,
          "nodeType": "gpu",
          "bucketTotalObjects": 3,
          "nodeAllocatableMemoryBytes": 191291998208,
          "bucketTotalDataSizeBytes": 300000000,
          "bucketLocationType": "multi-region",
          "bucketHNSEnabled": true,
          "sidecarLimitEphemeralStorageBytes": 0,
          "requiredMetadataStatCacheBytes": 4500,
          "nodeAllocatableEphemeralStorageBytes": 1317908854882,
          "nodeHasEphemeralStorageLSSD": true,
          "fuseBudgetEphemeralStorageBytes": 1120222526649
        }
      },
      ...
    }
    

## Clean up

To avoid incurring charges to your Google Cloud account for the resources created in this guide, perform the following steps:

  1. Delete the Deployment:
         
         kubectl delete deployment my-deployment -n NAMESPACE
         

Replace `NAMESPACE` with the Kubernetes namespace where you created the Deployment.

  2. Delete the PersistentVolumeClaim:
         
         kubectl delete pvc my-pvc -n NAMESPACE
         

Replace `NAMESPACE` with the Kubernetes namespace where you created the PVC.

  3. Delete the PersistentVolume:
         
         kubectl delete pv my-pv
         

  4. If you used the `gcsfusecsi-serving` profile or manually enabled Rapid Cache, follow the instructions to [Disable a cache](https://docs.cloud.google.com/storage/docs/rapid/use-rapid-cache#disable-cache) to stop incurring charges for cache instances.




## What's next

  * Learn more about the [Cloud Storage FUSE CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/cloud-storage-fuse-csi-driver).
  * Learn how to [manually optimize Cloud Storage FUSE CSI driver for performance](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-perf).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
