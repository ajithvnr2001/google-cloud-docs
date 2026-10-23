---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-perf/
title: Manually optimize Cloud Storage FUSE CSI driver for performance \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:25.443736+00:00
---

# Manually optimize Cloud Storage FUSE CSI driver for performance  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-perf/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Manually optimize Cloud Storage FUSE CSI driver for performance Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This guide shows you how to optimize the performance of the [Cloud Storage FUSE CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cloud-storage-fuse-csi-driver) on Google Kubernetes Engine (GKE). For a simplified, automated way to optimize Cloud Storage FUSE performance for AI/ML workloads, see [Automate performance tuning with Cloud Storage FUSE profiles](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/gcsfuse-profiles). The manual steps in this document are for advanced users, or to address custom needs not covered by the profiles.

While Cloud Storage FUSE offers flexibility and scalability, careful configuration and tuning are crucial to achieve optimal performance. The performance of Cloud Storage FUSE can differ from a POSIX file system in terms of latency, throughput, and consistency. The goal of tuning is to minimize the overhead of metadata operations and maximize the efficiency of data access. If you are running AI/ML applications that consume data in Cloud Storage buckets, tuning the CSI driver can lead to faster training and inference times for your AI/ML applications.

This guide is for Developers and Machine learning (ML) engineers who want to improve the performance of their applications that access data stored in [Cloud Storage buckets](https://docs.cloud.google.com/storage/docs/buckets).

Before reading this page, ensure you're familiar with the basics of Cloud Storage, Kubernetes, and the Cloud Storage FUSE CSI driver. Make sure to also check the [GKE version requirements](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cloud-storage-fuse-csi-driver#requirements) for specific features you want to use.

## Configure mount options

The Cloud Storage FUSE CSI driver supports mount options to configure how Cloud Storage buckets are mounted on your local file system.

**Note:** The Cloud Storage FUSE CSI driver's `mountOptions` field is designed to flexibly accept strings based on either the CLI option names (for example, `file-cache-enable-parallel-downloads=true`) or the configuration file key structure (for example, `file-cache:enable-parallel-downloads:true`). This approach lets you use the format you find most convenient. You don't need to supply a separate configuration file; these options are parsed directly by the driver. For the full list of supported mount options, see the [Cloud Storage FUSE CLI](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#options) and [Cloud Storage FUSE configuration file](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/config-file#format-and-fields).

You can specify mount options in the following ways, depending on the type of volume you are using:

### CSI ephemeral volume

If you use [CSI ephemeral volumes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-ephemeral), specify the mount options in the `spec.volumes[n].csi.volumeAttributes.mountOptions` field of your Pod manifest.

You must specify the mount options as a string, with flags separated by commas and without spaces. For example:
    
    
      mountOptions: "implicit-dirs,file-cache:enable-parallel-downloads:true,file-cache:download-chunk-size-mb:3"
    

### Persistent volume

If you use [persistent volumes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-pv), specify the mount options in the `spec.mountOptions` field in your PersistentVolume manifest.

You must specify the mount options as a list. For example:
    
    
      mountOptions:
        - implicit-dirs
        - file-cache:enable-parallel-downloads:true
        - file-cache:download-chunk-size-mb:3
    

### Mount considerations

Use the following considerations when configuring mounts with the CSI driver:

#### General considerations

  * The following flags are disallowed: `app-name`, `temp-dir`, `foreground`, `log-file`, `log-format`, `key-file`, `token-url`, and `reuse-token-from-url`.
  * Cloud Storage FUSE doesn't make implicit directories visible by default.
  * If you only want to mount a directory in the bucket instead of the entire bucket, pass the directory relative path by using the `only-dir=relative/path/to/the/bucket/root` flag.



#### Security and permissions

  * If you use a [Security Context](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/) for your Pod or container, or if your container image uses a non-root user or group, you must set the `uid` and `gid` mount flags. You also need to use the `file-mode` and `dir-mode` mount flags to set the file system permissions. Note that you can't run `chmod`, `chown`, or `chgrp` commands against a Cloud Storage FUSE file system, so use `uid`, `gid`, `file-mode`, and `dir-mode` mount flags to get access for a non-root user or group.



#### Linux kernel mount options

  * If you need to configure the Linux kernel mount options, you can pass the options using the `o` flag. For example, if you don't want to permit direct execution of any binaries on the mounted file system, set the `o=noexec` flag. Each option requires a separate flag, for example, `o=noexec`,`o=noatime`. Only the following options are allowed: `exec`, `noexec`, `atime`, `noatime`, `sync`, `async`, and `dirsync`.



## Configure caching

This section provides an overview of caching options available with Cloud Storage FUSE CSI driver to enhance performance.

### File caching

You can use the Cloud Storage FUSE CSI driver with file caching to improve the read performance of applications that handle small files from Cloud Storage buckets. The Cloud Storage FUSE file cache feature is a client-based read cache that allows repeated file reads to be served more quickly from cache storage of your choice.

You can choose from a range of storage options for the read cache, including Local SSD, durable block storage like Google Cloud Hyperdisk or Persistent Disk, and RAM disk (memory), based on your price-performance needs.

#### Enable and use file caching

By default, the file caching feature is disabled on GKE. You must opt-in to enable file caching with the Cloud Storage FUSE CSI driver.

To enable and control file caching, [set the volume attribute `fileCacheCapacity`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/cloud-storage-fuse-csi-driver/volume-attr) or use the [`file-cache:max-size-mb`](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#options) mount option.

GKE uses an `emptyDir` volume by default for Cloud Storage FUSE file caching backed by the ephemeral storage configured on the node. This could be the boot disk attached to the node or a Local SSD on the node. If you enable [Local SSD](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/local-ssd) on the node, GKE uses the Local SSD to back the `emptyDir` volume.

You can [configure a custom read cache volume for the sidecar container](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-sidecar#configure-custom-read-cache-volume) to replace the default `emptyDir` volume for file caching in read operations.

**Note:** If you choose to use the default `emptyDir` volume for file caching, the value of Pod annotation `gke-gcsfuse/ephemeral-storage-limit` **must** be larger than the `fileCacheCapacity` volume attribute or the `file-cache:max-size-mb` mount option value. If a custom cache volume is used, the underlying volume size **must** be larger than the `fileCacheCapacity` volume attribute.

To learn more about best practices for file caching, see [Cloud Storage FUSE performance](https://docs.cloud.google.com/storage/docs/gcsfuse-performance).

#### Select the storage for backing your file cache

To select the storage for backing your file cache, refer to these considerations:

  * For GPU and CPU VM families that support [Local SSD](https://docs.cloud.google.com/compute/docs/disks/local-ssd) (for example, A3 VMs), we recommend using Local SSD.

    * For A3+ VMs, GKE automatically sets up Local SSD for your Pods to consume.
    * If your VM family does not support Local SSD, GKE uses the boot disk for caching. The default disk type for the boot disk on GKE is [`pd-balanced`](https://docs.cloud.google.com/compute/docs/disks/persistent-disks#disk-types).
    * If your VM family supports Local SSD but doesn't have the ephemeral storage on Local SSD enabled by default, you can enable Local SSD in your node pool. This applies to first and second generation machine families such as N1 and N2 machines. To learn more, see [Create a cluster with Local SSD](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/local-ssd#1st-or-2nd-generation).

To check if your node has ephemeral storage on Local SSD enabled, run the following command:
          
          kubectl describe node <code><var>NODE_NAME</var></code> | grep "cloud.google.com/gke-ephemeral-storage-local-ssd"
          

  * For TPU VM families, especially v6+, we recommend using RAM as a file cache for the best performance as these VM instances have larger RAM.

    * When using RAM, pay attention to out-of-memory (OOM) errors as they cause Pod disruptions. Cloud Storage FUSE consumes memory, so setting up a file cache to consume the sidecar container can result in OOM errors. To prevent such scenarios, adjust your file cache configuration `file-cache:max-size-mb` field to a smaller value.
    * For other TPU families, we recommend using [`pd-balanced` or `pd-ssd`](https://docs.cloud.google.com/compute/docs/disks/persistent-disks#disk-types). The default disk type for the boot disk on GKE is [`pd-balanced`](https://docs.cloud.google.com/compute/docs/disks/persistent-disks#disk-types).
  * Avoid using the boot disk for caching as it can lead to reduced performance and unexpected terminations. Instead, consider using a PersistentVolume backed by [durable block storage](https://docs.cloud.google.com/compute/docs/disks).




#### Use RAM disk-based file caching

You can use RAM disk for file caching or parallel download to reduce the overhead of using a boot disk if you are using a TPU VM with sufficiently large RAM.

To use a RAM disk with the Cloud Storage FUSE CSI driver, add the following to your manifest:
    
    
    volumes:
      - name: gke-gcsfuse-cache
        emptyDir:
          medium: Memory
    

### Stat cache

The Cloud Storage FUSE CSI driver enhances performance by caching file metadata, like size and modification time. The CSI driver enables this [stat cache](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/caching#stat-cache-overview) by default and reduces latency by storing information locally instead of repeatedly requesting it from Cloud Storage. You can configure its maximum size (the default is 32 MB) and how long the data stays in the cache (the default is 60 seconds). By fine-tuning the metadata cache, you can reduce API calls to Cloud Storage, to improve application performance and efficiency by minimizing network traffic and latency.

To learn more about best practices for stat caching, see the [Cloud Storage FUSE caching overview](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/caching#best-practices-stat-cache).

#### Use metadata prefetch to pre-populate the metadata cache

The metadata prefetch feature lets the Cloud Storage FUSE CSI driver proactively load relevant metadata about the objects in your Cloud Storage bucket into Cloud Storage FUSE caches. This approach reduces calls to Cloud Storage and is especially beneficial for applications accessing large datasets with many files, such as AI/ML training workloads.

This feature requires GKE version 1.32.1-gke.1357001 or later. This feature is not supported with Dynamic Mounting, where you specify an underscore (_) to mount all buckets that the Kubernetes ServiceAccount can access. If you use dynamic mounting, metadata prefetch is not performed.

To see performance gains from metadata prefetch, you must set the time to live (TTL) value of metadata cache items to unlimited. Typically, setting a TTL prevents cached content from becoming stale. When you set TTL to unlimited, you must take precaution not to change the contents of the bucket out-of-band (meaning allowing a different workload or actor to modify the workload). Out-of-band changes are not visible locally and could cause consistency issues.

To enable metadata prefetch, make the following configuration changes. We recommend enabling this feature on volumes that are heavily read.

  * Set the volume attribute `gcsfuseMetadataPrefetchOnMount: true`.
  * Update the following mount options: 
    * [`metadata-cache:stat-cache-max-size-mb:-1`](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#options) to unset stat cache capacity limit.
    * [`metadata-cache:type-cache-max-size-mb:-1`](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#options) to unset type cache capacity limit.
    * [`file-system:kernel-list-cache-ttl-secs:-1`](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#options) to prevent kernel list cache items from expiring.
    * [`metadata-cache:ttl-secs:-1`](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#options) to prevent cached metadata items from expiring.
  * To avoid workload interruptions, consider increasing the memory limit of the `gke-gcsfuse-metadata-prefetch` sidecar. 
    * Increase limits by setting Pod annotation `gke-gcsfuse/metadata-prefetch-memory-limit` to `"512Mi"` or higher. For more information, see [Configure sidecar container resources](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-sidecar#configure-sidecar-resources).
    * Alternatively, unset the memory limit by setting Pod annotation `gke-gcsfuse/metadata-prefetch-memory-limit` to `"0"` (only supported for Standard Clusters).



For an example, see the code sample in Improve large file read performance using parallel download.

### List cache

To speed up directory listings for applications, you can enable [list caching](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/caching#list-cache-overview). This feature stores directory listings in memory so repeated requests can be served faster. The list cache is disable by default; you can enable it by setting the [`kernel-list-cache-ttl-secs`](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#options) parameter in your mount options. This defines how long listings are cached.

**Note:** While caching improves performance, remember that it uses memory and the cache is invalidated when directory contents change.

## Improve large file sequential reads by using buffered read

Buffered reads can improve sequential read performance for large files by asynchronously prefetching parts of a Cloud Storage object into an in-memory buffer. Buffering allows subsequent reads to be served from the buffer instead of requiring network calls.

Consider the following before you enable buffered reads:

  * Buffered reads are incompatible with file caching. If both buffered reads and file caching are enabled, file caching takes precedence and buffered reads are ignored.

  * Buffered reads can use significant memory and compute resources.




To enable buffered reads, in your manifest, configure this additional setting using mount options: [`enable-buffered-read`](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#options).

We recommend using the mount options: [`read-global-max-blocks`](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#read-global-max-blocks) to specify the maximum number of blocks available for buffered reads across all file handles.

## Improve large file read performance using parallel download

You can use Cloud Storage FUSE parallel download to accelerate reading large files from Cloud Storage for multi-threaded downloads. Cloud Storage FUSE parallel download can be particularly beneficial for model serving use cases with reads over 1 GB in size.

Parallel downloads require the [file cache](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-perf#file-caching) to be enabled. Starting from GKE version 1.32.0-gke.1795000, Cloud Storage FUSE strictly enforces this requirement and throws the following error if you try to use parallel downloads without the file cache, which prevents your Pod from starting: `MountVolume.SetUp failed for volume "gcs-fuse-csi-pv" : rpc error: code = Internal desc = gcsfuse failed with error: Error: error while parsing config: error parsing parallel download config: file cache should be enabled for parallel download support`.

Common examples include:

  * Model serving, where you need a large prefetch buffer to accelerate model download during instance boot.
  * Checkpoint restores, where you need a read-only data cache to improve one-time access of multiple large files.

**Best practice** : 

Use parallel download for applications that perform single-threaded large file reads. Applications with high read-parallelism (using more than eight threads) may encounter lower performance with this feature.

To use parallel download with the Cloud Storage FUSE CSI driver, follow these steps:

  1. Create a cluster with file caching enabled, as described in Enable and use file caching.

  2. In your manifest, configure these additional settings using mount options to enable parallel download:

     1. Set [`file-cache:enable-parallel-downloads:true`](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#options).
     2. Adjust [`file-cache:parallel-downloads-per-file`](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#options), [`file-cache:parallel-downloads-per-file`](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#options), [`file-cache:max-parallel-downloads`](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#options), and [`file-cache:download-chunk-size-mb`](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#options) as needed.
  3. (Optional) If needed, consider tuning these [volume attributes](https://docs.cloud.google.com/kubernetes-engine/docs/reference/cloud-storage-fuse-csi-driver/volume-attr):

     * [`file-cache:cache-file-for-range-read`](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#options) for random or partial reads.
     * [`metadata-cache:stat-cache-max-size-mb`](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#options) and [`metadata-cache:type-cache-max-size-mb`](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#options) for training workloads.



### Reduce quota consumption from access control checks

By default, the CSI driver performs access control checks to help ensure that the Pod service account has access to your Cloud Storage buckets. This results in additional overhead in the form of Kubernetes Service API, Security Token Service, and IAM calls. Starting in GKE version 1.29.9-gke.1251000, you can use the [volume attribute `skipCSIBucketAccessCheck`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/cloud-storage-fuse-csi-driver/volume-attr) to skip such redundant checks and reduce quota consumption.

### Inference serving example

The following example shows how to enable parallel download for inference serving:

  1. Create a PersistentVolume and PersistentVolumeClaim manifest with the following specification:
         
         apiVersion: v1
         kind: PersistentVolume
         metadata:
           name: serving-bucket-pv
         spec:
           accessModes:
           - ReadWriteMany
           capacity:
             storage: 64Gi
           persistentVolumeReclaimPolicy: Retain
           storageClassName: example-storage-class
           claimRef:
             namespace: NAMESPACE
             name: serving-bucket-pvc
           mountOptions:
             - implicit-dirs #avoid if list cache enabled and doing metadata prefetch
             - metadata-cache:ttl-secs:-1
             - metadata-cache:stat-cache-max-size-mb:-1
             - metadata-cache:type-cache-max-size-mb:-1
             - file-cache:max-size-mb:-1
             - file-cache:cache-file-for-range-read:true
             - file-system:kernel-list-cache-ttl-secs:-1
             - file-cache:enable-parallel-downloads:true
             - read_ahead_kb=1024
           csi:
             driver: gcsfuse.csi.storage.gke.io
             volumeHandle: BUCKET_NAME
             volumeAttributes:
               skipCSIBucketAccessCheck: "true"
               gcsfuseMetadataPrefetchOnMount: "true"
         ---
         apiVersion: v1
         kind: PersistentVolumeClaim
         metadata:
           name: serving-bucket-pvc
           namespace: NAMESPACE
         spec:
           accessModes:
           - ReadWriteMany
           resources:
             requests:
               storage: 64Gi
           volumeName: serving-bucket-pv
           storageClassName: example-storage-class
         

Replace the following values:

     * `NAMESPACE`: the Kubernetes namespace where you want to deploy your Pod.
     * `BUCKET_NAME`: the Cloud Storage bucket name you specified when configuring access to the Cloud Storage buckets. You can specify an underscore (`_`) to mount all buckets that the Kubernetes ServiceAccount can access. To learn more, see [Dynamic mounting](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/mount-bucket#dynamic-mount) in the Cloud Storage FUSE documentation.
  2. Apply the manifest to the cluster:
         
         kubectl apply -f PV_FILE_PATH
         

Replace `PV_FILE_PATH` with the path to your YAML file.

  3. Create a Pod manifest with the following specification to consume the PersistentVolumeClaim, depending on whether you are using Local SSD-backed file caching or RAM disk-backed file caching:

### Local SSD
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: gcs-fuse-csi-example-pod
           namespace: NAMESPACE
           annotations:
             gke-gcsfuse/volumes: "true"
             gke-gcsfuse/cpu-limit: "0"
             gke-gcsfuse/memory-limit: "0"
             gke-gcsfuse/ephemeral-storage-limit: "0"
         spec:
           containers:
             # Your workload container spec
             ...
             volumeMounts:
             - name: serving-bucket-vol
               mountPath: /serving-data
               readOnly: true
           serviceAccountName: KSA_NAME
           volumes:
           - name: serving-bucket-vol
             persistentVolumeClaim:
               claimName: serving-bucket-pvc
         

### RAM disk
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: gcs-fuse-csi-example-pod
           namespace: NAMESPACE
           annotations:
             gke-gcsfuse/volumes: "true"
             gke-gcsfuse/cpu-limit: "0"
             gke-gcsfuse/memory-limit: "0"
             gke-gcsfuse/ephemeral-storage-limit: "0"
         spec:
           containers:
             # Your workload container spec
             ...
             volumeMounts:
             - name: serving-bucket-vol
               mountPath: /serving-data
               readOnly: true
           serviceAccountName: KSA_NAME **  volumes:
             - name: gke-gcsfuse-cache # gcsfuse file cache backed by RAM Disk
               emptyDir:
                 medium: Memory **
           - name: serving-bucket-vol
             persistentVolumeClaim:
               claimName: serving-bucket-pvc
         

  4. Apply the manifest to the cluster:
         
         kubectl apply -f POD_FILE_PATH
         

Replace `POD_FILE_PATH` with the path to your YAML file.




## Optimize DNS lookups using NodeLocal DNSCache in GKE

In GKE versions earlier than 1.34.1-gke.3899000, if you use Cloud Storage FUSE with the HTTP/1.1 protocol, the frequent establishment of new connections can lead to a high volume of DNS lookups. This behavior can impact performance, especially in GKE environments.

To optimize DNS lookups and reduce latency on earlier GKE versions, you should [deploy NodeLocal DNSCache](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/nodelocal-dns-cache).

  * **Standard Pods** : deploying NodeLocal DNSCache automatically optimizes DNS lookups for most standard pods in your cluster.

  * **Host network Pods** : Pods that use the `hostNetwork: true` setting require an additional configuration change to use the NodeLocal DNSCache. You must explicitly override the `dnsPolicy` in the pod's specification to `ClusterFirstWithHostNet`.




A separate DNS cache typically isn't required in the following scenarios, because caching is handled internally:

  * **Compute Engine VMs** : the VM's operating system kernel usually caches DNS lookups effectively, negating the need for an additional caching layer.

  * **GKE 1.34.1-gke.3899000 and later** : Cloud Storage FUSE shipped with these versions provides a built-in DNS cache, which resolves the high-frequency lookup issue internally.




## Configure volume attributes

Volume attributes let you configure specific behavior of the Cloud Storage FUSE CSI driver.

The Cloud Storage FUSE CSI driver doesn't allow you to directly specify the Cloud Storage FUSE configuration file. You can configure some of the fields in the configuration file using the Cloud Storage FUSE CSI volume attributes. The CSI driver handles translating the volume attribute values to the configuration file fields.

For the full list of supported volume attributes, see the [Volume attributes reference](https://docs.cloud.google.com/kubernetes-engine/docs/reference/cloud-storage-fuse-csi-driver/volume-attr).

You can specify the volume attributes in the following ways:

  * In the `spec.csi.volumeAttributes` field on a PersistentVolume manifest, if you use persistent volumes.
  * In the `spec.volumes[n].csi.volumeAttributes` field, if you use CSI ephemeral volumes.



In the manifest, the volume attributes can be specified as key-value pairs. For example:
    
    
    volumeAttributes:
      mountOptions: "implicit-dirs"
      fileCacheCapacity: "-1"
      gcsfuseLoggingSeverity: warning
    

## Cloud Storage FUSE metrics

The following Cloud Storage FUSE metrics are now available through the [GKE Monitoring API](https://docs.cloud.google.com/monitoring/docs/apis). Details about Cloud Storage FUSE metrics such as labels, type, and unit can be found in [GKE System Metrics](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes). These metrics are available for each Pod that uses Cloud Storage FUSE and you can use metrics to configure insights per volume and bucket.

Metrics are enabled by default starting in GKE version 1.33.0-gke.2248000 or later. To disable them, set the [volume attribute `disableMetrics`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/cloud-storage-fuse-csi-driver/volume-attr) to "true".

### File system metrics

File system metrics track the performance and health of your file system, including the number of operations, errors, and operation speed. These metrics can help identify bottlenecks and optimize performance.

  * `gcsfusecsi/fs_ops_count`
  * `gcsfusecsi/fs_ops_error_count`
  * `gcsfusecsi/fs_ops_latency`



### Cloud Storage metrics

You can monitor Cloud Storage metrics, including data volume, speed, and request activity, to understand how your applications interact with Cloud Storage buckets. This data can help you identify areas for optimization, such as improving read patterns or reducing the number of requests.

  * `gcsfusecsi/gcs_download_bytes_count`
  * `gcsfusecsi/gcs_read_count`
  * `gcsfusecsi/gcs_read_bytes_count`
  * `gcsfusecsi/gcs_reader_count`
  * `gcsfusecsi/gcs_request_count`
  * `gcsfusecsi/gcs_request_latencies`



### File cache metrics

You can monitor file cache metrics, including data read volume, speed, and cache hit rate, to optimize Cloud Storage FUSE and application performance. Analyze these metrics to improve your caching strategy and maximize cache hits.

  * `gcsfusecsi/file_cache_read_bytes_count`
  * `gcsfusecsi/file_cache_read_latencies`
  * `gcsfusecsi/file_cache_read_count`



## Enable Cloud Storage FUSE performance defaults

Starting with version 1.33.2-gke.4655000, GKE automatically enables a number of performance defaults for Cloud Storage FUSE running on nodes that are backed by [high-performance machine types](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/automated-configurations). These performance defaults are not supported from 1.34.1-gke.1431000 to 1.34.1-gke.3403001 due to a [known issue](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#December_03_2025).

During volume mount, the Cloud Storage FUSE CSI driver fetches the target's node instance type and passes it to Cloud Storage FUSE through a new mount option `machine-type`.

When it's passed a high-performance machine type, Cloud Storage FUSE automatically sets the following default mount options:

  * `metadata-cache:negative-ttl-secs:0`
  * `metadata-cache:ttl-secs:-1`
  * `metadata-cache:stat-cache-max-size-mb:1024`
  * `metadata-cache:type-cache-max-size-mb:128`
  * `implicit-dirs:true`
  * `file-system:rename-dir-limit:200000`
  * `write:global-max-blocks:1600`



If any of these mount options are explicitly specified, they won't be overwritten by the automatic defaults.

You can opt out of the feature by including `disable-autoconfig` in the mount options. For example:
    
    
    mountOptions: "implicit-dirs,disable-autoconfig"
    

## Best practices for performance tuning

This section lists some recommended performance tuning and optimization techniques for the Cloud Storage FUSE CSI driver.

  * **Leverage Hierarchical Namespace (HNS) buckets:** Opt for HNS buckets to achieve a substantial 8x increase in initial Queries Per Second (QPS). This choice also facilitates swift and atomic directory renames, a crucial requirement for efficient checkpointing with Cloud Storage FUSE. HNS buckets ensure a better file-like experience by supporting 40,000 object read requests and 8,000 object write requests per second, a significant improvement compared to the 8,000 object read requests and 1,000 object write requests per second offered by flat buckets.

  * **Mount specific directories when possible:** If your workload involves accessing a specific directory within a bucket, use the `--only-dir` flag during mounting. This focused approach expedites list calls, as it limits the scope of `LookUpInode` calls, which involve a `list+stat` call for every file or directory in the specified path. By narrowing the mount to the required subdirectory, you minimize these calls, leading to performance gains.

  * **Optimize metadata caching:** Configure your metadata caches to maximize their capacity and set an infinite time to live (TTL). This practice effectively caches all accessed metadata for the duration of your job, minimizing metadata access requests to Cloud Storage. This configuration proves particularly beneficial for read-only volumes, as it eliminates repeated Cloud Storage metadata lookups. However, verify that the memory consumption associated with these large metadata caches aligns with your system's capabilities.

  * **Maximize GKE sidecar resources:** Cloud Storage FUSE operates within a sidecar container in a GKE environment. To prevent resource bottlenecks, remove limitations on CPU and memory consumption for the sidecar container. This allows Cloud Storage FUSE to scale its resource utilization based on workload demands, preventing throttling, which helps ensure optimal throughput.

  * **Populate the metadata cache proactively:** Enable metadata prefetch for the CSI driver. This efficiently populates the metadata and list caches, minimizing metadata calls to Cloud Storage and accelerating the initial run. Many ML frameworks perform this automatically, but it's crucial to ensure this step for custom training code. To learn more, see [Use metadata prefetch to pre-populate the metadata cach](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-perf#metadata-prefetch).

  * **Utilize file cache and parallel downloads:** Enable the file cache feature, especially for multi-epoch training workloads, where data is read repeatedly. The file cache stores frequently accessed data on local storage (SSD in the case of A3 machines), improving read performance. Complement this with the parallel downloads feature, particularly for serving workloads, to expedite the download of large files by splitting them into smaller chunks and downloading them concurrently.

  * **Enable buffered reads:** Buffered reads can improve sequential read performance for large files by asynchronously prefetching parts of a Cloud Storage object into an in-memory buffer. Buffering allows subsequent reads to be served from the buffer instead of requiring network calls. For more information, see [Improve large file sequential reads using buffered read](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-perf#buffered-read).

  * **Optimize checkpoints:** For checkpointing with Cloud Storage FUSE, we strongly recommend using an HNS bucket. If using a non-HNS bucket, set the `rename-dir-limit` parameter to a high value to accommodate the directory renames often employed by ML frameworks during checkpointing. However, be aware that directory renames in non-HNS buckets might not be atomic and could take longer to complete.

  * **Enable list caching:** Engage list caching using the `--kernel-list-cache-ttl-secs` flag to further enhance performance. This feature caches directory and file listings, improving the speed of `ls` operations. List caching is especially beneficial for workloads involving repeated full directory listings, common in AI/ML training scenarios. It's advisable to use list caching with read-only mounts to maintain data consistency.

  * **Increase kernel read ahead:** For workloads that primarily involve sequential reads of large files, such as serving and checkpoint-restore, increasing the read-ahead size can significantly enhance performance. To increase Cloud Storage FUSE read-ahead, specify the `read_ahead_kb` flag in `mountOptions` and set it to 1MB (e.g. `read_ahead_kb=1024`). This feature requires GKE version 1.32.2-gke.1297001 or later. For zonal buckets, Cloud Storage FUSE automatically manages the `read_ahead_kb` kernel parameter in GKE version 1.35.0-gke.3047001 or later. Consequently, the `read_ahead_kb` mount option is not applicable, and any value provided to it will be ignored.

  * **Enable streaming writes:** Streaming writes is a new write path that uploads data directly to Cloud Storage as it's written. This approach differs from the default write method, which temporarily stages the entire write in a local directory and then uploads it to Cloud Storage upon a `close` or `fsync` operation. Streaming writes reduce both latency and disk space usage, making it particularly beneficial for large, sequential writes such as checkpoints. To enable streaming writes, specify the `enable-streaming-writes` command line flag in `mountOptions`.




## Troubleshoot issues

For more information about troubleshooting, refer to:

  * [Troubleshoot Cloud Storage FUSE out-of-memory (OOM) events](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/storage#gcsfuse-oom-events) using Cloud Profiler.
  * The [troubleshooting guide](https://github.com/GoogleCloudPlatform/gcs-fuse-csi-driver/blob/main/docs/troubleshooting.md) in the GitHub project documentation.



## What's next

  * [Explore additional samples for using the CSI driver on GitHub](https://github.com/GoogleCloudPlatform/gcs-fuse-csi-driver/blob/main/examples/README.md).
  * [Learn more about Cloud Storage FUSE](https://docs.cloud.google.com/storage/docs/gcs-fuse).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
