---
url: https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/performance/
title: Performance tuning best practices \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:26:10.291198+00:00
---

# Performance tuning best practices  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/performance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Performance tuning best practices Stay organized with collections  Save and categorize content based on your preferences. 

Tuning key Cloud Storage FUSE features and configurations helps you maximize throughput and performance, especially for artificial intelligence and machine learning (AI/ML) workloads such as training, serving, and checkpointing. This document describes best practices for tuning Cloud Storage FUSE performance.

## Considerations

Before you apply the configurations we recommend in this page, consider the following:

  * You can apply the recommended configurations in this page using the following methods:

    * Cloud Storage FUSE [`profile` field](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/config-file#profile) or [`--profile` option](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#profile), which configures settings for AI/ML training, checkpointing, or serving workloads automatically when used.

    * [Cloud Storage FUSE configuration file](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/config-file)

    * [Cloud Storage FUSE CLI](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options)

    * For Google Kubernetes Engine only: [sample Google Kubernetes Engine YAML files](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/sample-yaml-files)

  * Make sure you're running the latest version of Cloud Storage FUSE. The recommended configurations should only be applied to Cloud Storage FUSE version 3.0 or later and the [Cloud Storage FUSE CSI driver for Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cloud-storage-fuse-csi-driver) that runs on GKE clusters version 1.32.2-gke.1297001 or later.

  * The recommended configurations cache Cloud Storage metadata for the length of the job and aren't checked after the initial mount of the file system. Therefore, we recommend that the file system is read-only or file system semantics are _write-to-new_ applications, meaning applications always write to new files, for optimal performance. The following AI/ML workloads are write-to-new:

    * Checkpointing

    * Training

    * Serving

    * [`jax.jit()`](https://docs.jax.dev/en/latest/jit-compilation.html) caching

  * The recommended configurations in this page have been validated for Cloud GPUs and Cloud TPU large machine types at scale where there is a large amount of memory and a high bandwidth network interface. Cloud GPUs and Cloud TPU machine types can differ in terms of the number of available resources such as CPU, memory, and local storage within their host node configuration. This can directly impact performance for configurations such as the following:

    * [A3 Ultra](https://docs.cloud.google.com/compute/docs/gpus#h200-gpus)

    * [A3 Mega](https://docs.cloud.google.com/compute/docs/gpus#h100-gpus) \- 1.8 TiB memory, with 6 TiB LSSD

    * [Cloud TPU v5e](https://docs.cloud.google.com/tpu/docs/v5e) \- 188 GiB memory, with no LSSD

    * [Cloud TPU v5p](https://docs.cloud.google.com/tpu/docs/v5p) \- 448 GiB memory, with no LSSD

    * [Cloud TPU v6e](https://docs.cloud.google.com/tpu/docs/v6e) (Trillium) - 1.5 TiB memory, with no LSSD

    * [Cloud TPU 7x](https://docs.cloud.google.com/tpu/docs/tpu7x) (Ironwood) - 1.1 TiB memory, with no LSSD




## Rapid Bucket support

Starting with version 3.7.1, Cloud Storage FUSE supports Rapid Bucket with optimized read path.

The optimized read path significantly improves performance by using the Linux kernel's read-ahead algorithm by default. To use this optimized read path, specific machine-level configuration changes are required for the `read_ahead_kb`, `max_background`, and `congestion_threshold` parameters. In Google Kubernetes Engine (GKE) environments using the Cloud Storage FUSE CSI driver, these configurations are fully managed and applied automatically. For Compute Engine VMs and other non-GKE environments, Cloud Storage FUSE requires `sudo` permissions to apply these changes automatically, or you must configure these parameters [manually](https://github.com/GoogleCloudPlatform/gcsfuse/releases/tag/v3.7.1).

When using the optimized read path for Rapid Bucket, keep the following behaviors and limitations in mind:

  * **File cache and buffered reader compatibility:** Because the optimized read path relies on the kernel's read-ahead algorithm, it is incompatible with the Cloud Storage FUSE file cache and buffered reader. By default, these features are inactive (no-op) for Rapid Bucket. If your workload requires the file cache or buffered reader, you must explicitly disable the kernel reader by setting `enable-kernel-reader: false` during mounting. This will cause Cloud Storage FUSE to use the standard read path, which is compatible with file caching and buffered reads.
  * **Mounting requirements:** The new read path is supported only for static mounts. It isn't supported when using dynamic mounting.



## Use buckets with hierarchical namespace enabled

Always use buckets with [hierarchical namespace](https://docs.cloud.google.com/storage/docs/hns-overview) enabled. Hierarchical namespace organizes your data into a hierarchical file system structure, which makes operations within the bucket more efficient, resulting in quicker response times and fewer overall list calls for every operation.

The benefits of hierarchical namespace include the following:

  * Buckets with hierarchical namespace provide up to eight times higher initial queries per second (QPS) compared to flat buckets. Hierarchical namespace supports 40,000 initial object read requests per second and 8,000 initial object write requests, which is significantly higher than typical Cloud Storage FUSE flat buckets, which offer only 5,000 object read requests per second initially and 1,000 initial object write requests.

  * Hierarchical namespace provides atomic directory renames, which are required for checkpointing with Cloud Storage FUSE to ensure atomicity. Using buckets with hierarchical namespace enabled is especially beneficial when checkpointing at scale because ML frameworks use directory renames to finalize checkpoints, which is a fast, atomic command, and is only supported in buckets with hierarchical namespace enabled. If you choose not to use a bucket with hierarchical namespace enabled, see Increase rename limit for non-HNS buckets.




To learn how to create a bucket with hierarchical namespace enabled, see [Create buckets with hierarchical namespace enabled](https://docs.cloud.google.com/storage/docs/create-hns-bucket). To learn how to mount a hierarchical namespace-enabled bucket, see [Mount buckets with hierarchical namespace enabled](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/mount-bucket#hns-folders). Hierarchical namespace is supported on Google Kubernetes Engine versions 1.31.1-gke.2008000 or later.

## Perform a directory-specific mount

If you want to access a specific directory within a bucket, you can mount only the specific directory using the [`only-dir`](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/config-file#only-dir) mount option instead of mounting the entire bucket. Performing a directory-specific mount accelerates list calls and reduces the overall number of list and stat calls by limiting the number of directories to traverse when resolving a filename, because `LookUpInode` calls and bucket or directory access requests automatically generate list and stat calls for each file or directory in the path.

To mount a specific directory, use one of the following methods:

###  Google Kubernetes Engine 

For persistent volumes, use the following mount configuration with the Cloud Storage FUSE CSI driver for Google Kubernetes Engine:
    
    
    mountOptions:
        - only-dir:DIRECTORY_NAME
    

For ephemeral volumes, append the mount configuration to the `volumeAttributes.mountOptions`, with flags separated by commas:
    
    
    mountOptions: "OTHER_OPTIONS,only-dir:DIRECTORY_NAME"
    

Replace `DIRECTORY_NAME` with the name of the directory you want to mount.

###  Compute Engine 

Run the `gcsfuse --only-dir` command to mount a specific directory on a Compute Engine virtual machine:
    
    
    gcsfuse --only-dir DIRECTORY_NAME BUCKET_NAME MOUNT_POINT
    

Replace the following:

  * `BUCKET_NAME` is the name of the bucket you want to mount the directory in.

  * `DIRECTORY_NAME` is the name of the directory you want to mount.

  * `MOUNT_POINT` is the local directory where your bucket will be mounted. For example, `/path/to/mount/point`.




For more information on how to perform a directory mount, see [Mount a directory within a bucket](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/mount-bucket#directory-mount).

## Increase metadata cache values

To improve performance for repeat reads, you can configure Cloud Storage FUSE to cache a large amount of metadata and bypass metadata expiration, which avoids repeated metadata requests to Cloud Storage and significantly improves performance.

Increasing metadata cache values is beneficial for workloads with repeat reads to avoid repetitive Cloud Storage calls and for read-only volumes where an infinite TTL can be set.

Consider the following before you increase metadata cache values:

  * An infinite time to live (TTL) should only be set for volumes that are either read-only or write-to-new only.

  * The metadata cache should only be enabled to grow significantly in size on nodes with large memory configurations because it caches all metadata for the specified mount point in each node and eliminates the need for additional access to Cloud Storage.

  * The configurations in this section cache all accessed metadata with an infinite TTL, which can affect consistency guarantees when changes are made on the same Cloud Storage bucket by any other client, for example, overwrites on a file or deletions of a file.

  * To verify memory consumption isn't impacted, validate that the amount of memory consumed by the metadata cache is acceptable to you, which can grow to be in gigabytes and depends on the number of files in the mounted buckets and how many mount points are being used. For example, each file's metadata takes roughly 1.5 KiB of memory, and relatively, the metadata of one million files takes approximately 1.5 GiB of memory. For more information, see [Overview of caching](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/caching).




Use the following instructions to configure Cloud Storage FUSE to cache a large amount of metadata and to bypass metadata expiration:

### `gcsfuse` options
    
    
    gcsfuse --metadata-cache-ttl-secs=-1 \
          --stat-cache-max-size-mb=-1 \
          BUCKET_NAME MOUNT_POINT
    

Replace the following:

  * `BUCKET_NAME` is the name of your bucket.

  * `MOUNT_POINT` is the local directory where your bucket will be mounted. For example, `/path/to/mount/point`.




### Configuration file
    
    
    metadata-cache:
    stat-cache-max-size-mb: -1
    ttl-secs: -1

###  Google Kubernetes Engine 
    
    
      mountOptions:
          - metadata-cache:ttl-secs:-1
          - metadata-cache:stat-cache-max-size-mb:-1
    

###  Compute Engine 
    
    
    gcsfuse --metadata-cache-ttl-secs=-1 \
          --stat-cache-max-size-mb=-1 \
          BUCKET_NAME MOUNT_POINT
    

Replace the following:

  * `BUCKET_NAME` is the name of your bucket.

  * `MOUNT_POINT` is the local directory where your bucket will be mounted. For example, `/path/to/mount/point`.




## Pre-populate the metadata cache

Before you run a workload, we recommend that you pre-populate the metadata cache, which significantly improves performance and substantially reduces the number of metadata calls to Cloud Storage, particularly if the [`implicit-dirs` field](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/config-file#implicit-dirs) or [`--implicit-dirs` option](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#implicit-dirs) is used. The Cloud Storage FUSE CSI driver for GKE provides an API that handles pre-populating the metadata cache, see [Use metadata prefetch to pre-populate the metadata cache](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-perf#metadata-prefetch).

**Note:** Running the `ls -R` command can pre-populate the metadata cache if the application doesn't do this itself. If the application accesses the entire directory structure from the current location to where `ls -R` is run from, this can quickly populate the entire metadata cache and list cache, if enabled.

To pre-populate the metadata cache, use one of the following methods:

###  Google Kubernetes Engine 

Set the `gcsfuseMetadataPrefetchOnMount` CSI volume attribute flag to `true`:

On Google Kubernetes Engine versions 1.32.1-gke.1357001 or later, you can enable metadata prefetch for a given volume using the `gcsfuseMetadataPrefetchOnMount` configuration option in the `volumeAttributes` field of your `PersistentVolume` definition. The `initContainer` method isn't needed when you use the `gcsfuseMetadataPrefetchOnMount` configuration option.
    
    
      apiVersion: v1
      kind: PersistentVolume
      metadata:
        name: training-bucket-pv
      spec:
        ...
        csi:
          volumeHandle: BUCKET_NAME
          volumeAttributes:
            ...
            gcsfuseMetadataPrefetchOnMount: "true"
      

Replace the following:

  * `BUCKET_NAME` is the name of your bucket.



Init container resources may vary depending on bucket contents and hierarchical layout, so consider [setting custom metadata prefetch sidecar resources](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-sidecar#configure-sidecar-resources) for higher limits.

### Linux

Manually run the `ls -R` command on the Cloud Storage FUSE mount point to recursively list all files and pre-populate the metadata cache:
    
    
    ls -R MOUNT_POINT > /dev/null

Replace the following:

`MOUNT_POINT`: the path to your Cloud Storage FUSE mount point.

###  Compute Engine 

Manually run the `ls -R` command on the Cloud Storage FUSE mount point to recursively list all files and pre-populate the metadata cache:
    
    
    ls -R MOUNT_POINT > /dev/null

Replace the following:

`MOUNT_POINT`: the path to your Cloud Storage FUSE mount point.

## Enable file caching and parallel downloads

File caching lets you store frequently accessed file data locally on your machine, speeding up repeat reads and reducing Cloud Storage costs. When you enable file caching, parallel downloads are automatically enabled as well. Parallel downloads utilize multiple workers to download a file in parallel using the file cache directory as a prefetch buffer, resulting in nine times faster model load time.

To learn how to enable and configure file caching and parallel downloads, see [Enable and configure file caching behavior](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/file-caching#configure). To use a sample configuration, see Sample configuration for enabling file caching and parallel downloads.

### Cloud GPUs and Cloud TPU considerations for using file caching and parallel downloads

The file cache can be hosted on Local SSDs, RAM, Persistent Disk, or Google Cloud Hyperdisk with the following guidance. In all cases, the data, or individual large file, must fit within the file cache directory's available capacity which is controlled using the [`max-size-mb` field](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/config-file#max-size-mb) or the [`--file-cache-max-size-mb` option](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#file-cache-max-size-mb).

#### Cloud GPUs considerations

Local SSDs are ideal for training data and checkpoint downloads. Cloud GPUs machine types include SSD capacity which can be used, such as A4 machine types that include 12 TiBs of SSD.

  * A RAM disk provides the best performance for loading model weights because of their small size compared to the unused amount of RAM on the system.

  * Persistent Disk or Google Cloud Hyperdisk can both be used as a cache.




#### Cloud TPU considerations

Cloud TPU don't support Local SSDs. If you use file caching on Cloud TPU without modification, the default location used is the boot volume, which isn't recommended and results in poor performance.

Instead of the boot volume, we recommend using a RAM disk, which is preferred for its performance and no incremental cost. However, a RAM disk is often constrained in size and most useful for serving model weights or checkpoint downloads depending on the size of the checkpoint and the available RAM. Additionally, we recommend using Persistent Disk and Google Cloud Hyperdisk for caching purposes.

### Sample configuration for enabling file caching and parallel downloads

By default, the file cache uses a Local SSD if the [`ephemeral-storage-local-ssd` mode](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create#--ephemeral-storage-local-ssd) is enabled for the Google Kubernetes Engine node. If no Local SSD is available, for example, on Cloud TPU machines, the file cache uses the Google Kubernetes Engine node's boot disk, which is not recommended. In this case, you can use a RAM disk as the cache directory, but consider the amount of RAM available for file caching versus what is needed by the pod.

### `gcsfuse` options
    
    
    gcsfuse --file-cache-max-size-mb=-1 \
          --file-cache-cache-file-for-range-read=true \
          --file-cache-enable-parallel-downloads=true \
          BUCKET_NAME
    

Replace the following:

  * `BUCKET_NAME` is the name of your bucket.



### Configuration file
    
    
    file-cache:
      max-size-mb: -1
      cache-file-for-range-read: true
      enable-parallel-downloads: true

###  Cloud GPUs 
    
    
    mountOptions:
        - file-cache:max-size-mb:-1
        - file-cache:cache-file-for-range-read:true
        - file-cache:enable-parallel-downloads:true
    
    # RAM disk file cache if LSSD not available. Uncomment to use
    # volumes:
    #   - name: gke-gcsfuse-cache
    #     emptyDir:
    #       medium: Memory
    

###  Cloud TPU 
    
    
    mountOptions:
        - file-cache:max-size-mb:-1
        - file-cache:cache-file-for-range-read:true
        - file-cache:enable-parallel-downloads:true
    
    volumes:
        - name: gke-gcsfuse-cache
          emptyDir:
            medium: Memory
    

###  Compute Engine 
    
    
    gcsfuse --file-cache-max-size-mb=-1 \
          --file-cache-cache-file-for-range-read=true \
          --file-cache-enable-parallel-downloads=true \
          BUCKET_NAME MOUNT_POINT
    

Replace the following:

  * `BUCKET_NAME` is the name of your bucket.

  * `MOUNT_POINT` is the local directory where your bucket will be mounted. For example, `/path/to/mount/point`.




## Disable negative stat cache entries

By default, Cloud Storage FUSE caches negative stat entries, meaning entries for files that don't exist, with a TTL of five seconds. In workloads where files are frequently created or deleted, such as distributed checkpointing, these cached entries can become stale quickly, which leads to performance issues. To avoid this, we recommend that you disable the negative stat cache for training, serving, and checkpointing workloads using the [`negative-ttl-secs` field](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/config-file#negative-ttl-secs) or the [`--metadata-cache-negative-ttl-secs` option](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#metadata-cache-negative-ttl-secs).

**Note:** Disabling the negative stat cache requires Cloud Storage FUSE version 2.8, available on Google Kubernetes Engine versions 1.32.1-gke.1200000 or later.

Use the following instructions to disable the negative stat cache:

### `gcsfuse` option
    
    
    gcsfuse --metadata-cache-negative-ttl-secs=0 \
      BUCKET_NAME
    

Replace the following:

  * `BUCKET_NAME` is the name of your bucket.



### Configuration file
    
    
    metadata-cache:
     negative-ttl-secs: 0

###  Google Kubernetes Engine 
    
    
    mountOptions:
        - metadata-cache:negative-ttl-secs:0
    

###  Compute Engine 
    
    
    gcsfuse --metadata-cache-negative-ttl-secs=0 \
      BUCKET_NAME MOUNT_POINT
    

Replace the following:

  * `BUCKET_NAME` is the name of your bucket.

  * `MOUNT_POINT` is the local directory where your bucket will be mounted. For example, `/path/to/mount/point`.




## Enable streaming writes

Streaming writes upload data directly to Cloud Storage as it's written, which reduces latency and disk space usage. This is particularly beneficial for large, sequential writes such as checkpoints. Streaming writes are enabled by default on Cloud Storage FUSE version 3.0 and later.

**Note:** Streaming writes are designed for sequential writes to a new, single file only. If you modify existing files, or perform out-of-order writes, it can cause Cloud Storage FUSE to automatically revert to the existing behavior of staging writes to a temporary file on disk.

If streaming writes aren't enabled by default, use the following instructions to enable them. Enabling streaming writes requires Cloud Storage FUSE version 3.0 which is available on Google Kubernetes Engine versions 1.32.1-gke.1729000 or later.

### `gcsfuse` option
    
    
    gcsfuse --enable-streaming-writes=true \
      BUCKET_NAME
    

Replace the following:

  * `BUCKET_NAME` is the name of your bucket.



### Configuration file
    
    
    write:
     enable-streaming-writes: true

###  Google Kubernetes Engine 
    
    
    mountOptions:
        - write:enable-streaming-writes:true
    

###  Compute Engine 
    
    
    gcsfuse --enable-streaming-writes=true \
      BUCKET_NAME MOUNT_POINT
    

Replace the following:

  * `BUCKET_NAME` is the name of your bucket.

  * `MOUNT_POINT` is the local directory where your bucket will be mounted. For example, `/path/to/mount/point`.




## Enable buffered reads

Buffered reads can improve sequential read performance for large files by two to five times by asynchronously prefetching parts of a Cloud Storage object into an in-memory buffer. This allows subsequent reads to be served from the buffer instead of requiring network calls.

Consider the following before you enable buffered reads:

  * Buffered reads are incompatible with file caching. If both buffered reads and file caching are enabled, file caching takes precedence and buffered reads are ignored.

  * Buffered reads can take up significant memory and compute resources.




To enable buffered reads, use the following instructions:

### CLI options
    
    
    gcsfuse --enable-buffered-read=true \
      BUCKET_NAME
    

Replace the following:

  * `BUCKET_NAME` is the name of your bucket.



### Configuration file
    
    
    read:
     enable-buffered-read: true

**Note:** We recommend using the [`--read-global-max-blocks` option](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#read-global-max-blocks) or [`read:global-max-blocks` field](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/config-file#read:global-max-blocks) to specify the maximum number of blocks available for buffered reads across all file handles.

## Increase kernel read-ahead size

For workloads that primarily involve sequential reads of large files such as serving and checkpoint restores, increasing the read-ahead size can significantly enhance performance. This can be done using the [`read_ahead_kb` Linux kernel parameter](https://www.kernel.org/doc/html/v5.4/block/queue-sysfs.html#read-ahead-kb-rw) on your local machine. We recommend that you increase the `read_ahead_kb` kernel parameter to 1 MB instead of using the default amount of 128 KB that's set on most Linux distributions. For Compute Engine instances, either `sudo` or `root` permissions are required to successfully increase the kernel parameter.

**Note:** Increasing the read-ahead size requires GKE versions 1.32.1-gke.1200000 or later.

To increase the `read_ahead_kb` kernel parameter to 1 MB for a specific Cloud Storage FUSE mounted directory, use the following instructions. Your bucket must be mounted to Cloud Storage FUSE before you run the command, otherwise, the kernel parameter doesn't increase.

For zonal buckets, Cloud Storage FUSE automatically manages the `read_ahead_kb` kernel parameter in Google Kubernetes Engine version1.35.0-gke.3047001 or later, and in Compute Engine environments using Cloud Storage FUSE version 3.7.0 or later. Because this is handled automatically, the `read_ahead_kb` mount option is no longer applicable; any value you provide will be ignored. Note that in Compute Engine environments, Cloud Storage FUSE requires root or passwordless sudo permissions to automatically manage this parameter.

###  Google Kubernetes Engine 
    
    
    mountOptions:
        - read_ahead_kb=1024

###  Compute Engine 
    
    
    export MOUNT_POINT=/path/to/mount/point
    echo 1024 | sudo tee /sys/class/bdi/0:$(stat -c "%d" $MOUNT_POINT)/read_ahead_kb
    

Replace the following:

  * `/path/to/mount/point`: the path on your local file system where the Cloud Storage bucket is mounted.



## Disable Security Token Service to avoid redundant checks

The Cloud Storage FUSE CSI driver for Google Kubernetes Engine has access checks to ensure pod recoverability due to user misconfiguration of workload identity bindings between the bucket and GKE service account, which can hit default Security Token Service API quotas at scale. This can be disabled by setting the [`skipCSIBucketAccessCheck`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/cloud-storage-fuse-csi-driver/volume-attr) volume attribute of the Persistent Volume CSI driver. We recommend that you make sure the GKE service account has the right access to the target Cloud Storage bucket to avoid mount failures for the pod.

Additionally, the Security Token Service quota must be increased beyond the default value of `6000` if a Google Kubernetes Engine cluster consists of more than 6,000 nodes, which can result in `429` errors if not increased in large scale deployments. The Security Token Service quota must be increased through the [Quotas and limits page](https://docs.cloud.google.com/storage/quotas). We recommend that you keep the quota equal to the number of mounts, for example, if there are 10,000 mounts in the cluster, the quota should be increased to `10000`.

To set the `skipCSIBucketAccessCheck` volume attribute, see the following sample configuration:
    
    
      volumeAttributes:
          - skipCSIBucketAccessCheck: "true"
       

## Optimize performance for OCDBT Orbax checkpoints

For workloads that use OCDBT-formatted Orbax checkpoints, you can improve serving and checkpoint restore performance by using the following guidance:

  * **Set transparent huge pages to`always`**: setting transparent huge pages to `always` improves performance by reducing memory fragmentation and system calls. This setting is most effective when large chunks of memory are allocated, which is common in these workloads. This setting is configured by default on Cloud TPU machines and only needs to be set on other machine types. To enable transparent huge pages on your local machine, run the following command with `root` permissions.
        
        echo always | tee /sys/kernel/mm/transparent_hugepage/enabled
        

In a GKE environment, you can create a privileged Pod to do the same thing.

  * **Increase kernel read-ahead size** : increasing kernel read-ahead size to 1024 KB improves sequential read performance. For more information, see Increase kernel read-ahead size.

  * **Set`ocdbt_target_data_file_size` to 200 MiB**: set the `ocdbt_target_data_file_size` to 200 MiB, which is optimal for read performance with Cloud Storage FUSE.

  * **Use DNS caching** : DNS caching reduces latency by caching DNS lookups locally. In GKE, you can enable [NodeLocal DNSCache](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-perf#use-nodelocal-dnscache-in-gke) to cache DNS lookups. Alternatively, use Cloud Storage FUSE version 3.5 or later on Compute Engine, or GKE version 1.34.1-gke.3899000 or later in a GKE environment.




## Other performance considerations

Beyond the primary optimizations discussed, several other factors can significantly impact the overall performance of Cloud Storage FUSE. The following sections describe additional performance considerations we recommend considering when you use Cloud Storage FUSE.

### Increase the rename limit for non-HNS buckets

Checkpointing workloads should always be done with a bucket that has hierarchical namespace enabled because of atomic and faster renames and higher QPS for reads and writes. However, if you accept the risk of directory renames not being atomic and taking longer, you can use the [`rename-dir-limit` field](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/config-file#rename-dir-limit) or the [`--rename-dir-limit` option](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#rename-dir-limit) if you're performing checkpointing using buckets without hierarchical namespace to specify a limit on the number of files or operations involved in a directory rename operation at any given time.

We recommend specifying this setting to a high value to prevent checkpointing failures. Because Cloud Storage FUSE uses a flat namespace and objects are immutable, a directory rename operation involves renaming and deleting all individual files within the directory. You can control the number of files affected by a rename operation by setting the `rename-dir-limit` `gcsfuse` option.

Use the following instructions to set the `rename-dir-limit` configuration option:

### `gcsfuse` option
    
    
    gcsfuse --rename-dir-limit=200000 \
      BUCKET_NAME
    

Replace the following:

  * `BUCKET_NAME` is the name of your bucket.



### Configuration file
    
    
    file-system:
     rename-dir-limit: 200000

###  Google Kubernetes Engine 
    
    
    mountOptions:
        - rename-dir-limit=200000
    

###  Compute Engine 
    
    
    gcsfuse --rename-dir-limit=200000 \
      BUCKET_NAME MOUNT_POINT
    

Replace the following:

  * `BUCKET_NAME` is the name of your bucket.

  * `MOUNT_POINT` is the local directory where your bucket will be mounted. For example, `/path/to/mount/point`.




### Kernel list caching

The list cache is a cache for directory and file list, or `ls`, responses that improves the speed of list operations. Unlike the stat cache, which are managed by Cloud Storage FUSE, the list cache is kept in the kernel's page cache and is controlled by the kernel based on memory availability.

Enabling kernel list caching is most beneficial for the following use cases:

  * **Workloads with repeated directory listings** : this configuration is especially useful for workloads that perform frequent full directory listings, such as AI/ML training runs. This can benefit both serving and training workloads.

  * **Read-only mounts** : list caching is recommended with read-only mounts to avoid consistency issues.




Enabling kernel list caching should be done with caution and should be used only if the file system is truly read-only with no expected directory content changes during the execution of a job. This is because with this flag, the local application never sees updates, especially if the TTL is set to `-1`.

For example, _Client 1_ lists `directoryA`, which causes `directoryA` to be a resident in the kernel list cache. _Client 2_ creates `fileB` under `directoryA` in the Cloud Storage bucket. _Client 1_ continuously checks for `fileB` in `directoryA`, which is essentially checking the kernel list cache entry and never goes over the network. _Client 1_ doesn't see that a new file is in the directory because the list of files is continuously served from the local kernel list cache. _Client 1_ then times out and the program is broken.

Use the following instruction to enable list caching:

### `gcsfuse` option
    
    
    gcsfuse --kernel-list-cache-ttl-secs=-1 \
      BUCKET_NAME
    

Replace the following:

  * `BUCKET_NAME` is the name of your bucket.



### Configuration file
    
    
    file-system:
     kernel-list-cache-ttl-secs: -1

###  Google Kubernetes Engine 
    
    
    mountOptions:
        - file-system:kernel-list-cache-ttl-secs:-1
    

###  Compute Engine 
    
    
    gcsfuse --kernel-list-cache-ttl-secs=-1 \
      BUCKET_NAME MOUNT_POINT
    

Replace the following:

  * `BUCKET_NAME` is the name of your bucket.

  * `MOUNT_POINT` is the local directory where your bucket will be mounted. For example, `/path/to/mount/point`.




When you use the [`file-system:kernel-list-cache-ttl-secs`](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/config-file#kernel-list-cache-ttl-secs) mount option, the values mean the following:

  * A positive value represents the TTL in seconds to keep the directory list response in the kernel's page cache.

  * A value of `-1` bypasses entry expiration and returns the list response from the cache when it's available.




### Use JAX persistent compilation (JIT) cache with Cloud Storage FUSE

JAX supports [Just-In-Time (JIT) cache](https://docs.jax.dev/en/latest/jit-compilation.html), an optional persistent compilation cache that stores compiled function artifacts. When you use this cache, you can significantly speed up subsequent script executions by avoiding redundant compilation steps.

To enable JIT caching, you must meet the following requirements:

  * **Use the latest version of JAX** : use JAX versions 0.5.1 or later for the latest cache features and optimizations.

  * **Maximize cache capacity** : to prevent performance degradation due to cache eviction, consider setting an unlimited cache size, particularly if you want to override default settings. You can achieve this by setting the environment variable:
        
        export JAX_COMPILATION_CACHE_MAX_SIZE=-1
        

  * **Ensure checkpoint pod YAML** : use the checkpoint configuration for the mountpoint for the JAX JIT cache.




## Configure Receive Flow Steering (RFS) for A4X

On Compute Engine instances, [Receive Packet Steering (RPS)](https://www.kernel.org/doc/html/latest/networking/scaling.html#receive-packet-steering-rps) and [Receive Flow Steering (RFS)](https://www.kernel.org/doc/html/latest/networking/scaling.html#receive-flow-steering-rfs) work together to improve network performance by intelligently distributing the processing of network packets across multiple CPUs. We recommend these settings for high-rate network traffic on machine types such as [A4X](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4x-series).

  * RPS distributes incoming network packets across different CPUs for processing. This helps to balance the load and prevent a single CPU from becoming a bottleneck, which is especially useful for high-rate network traffic and can contribute to lower latency.

  * RFS builds upon RPS to further reduce network latency by improving CPU cache efficiency. It steers packets to the specific CPU core where the application that will consume the packets is running, which increases the CPU's data cache hit rate and leads to lower network latency.




**Performance Benefits**

RFS significantly improves performance across various workloads, increasing throughput by up to 40%.

**Considerations**

While effective under load, these settings may not be useful in all scenarios:

  * **Single-threaded or single-flow workloads:** A single-flow workload occurs when all network traffic uses a single network connection (for example, a single massive file transfer over one TCP connection). These applications often see little benefit and may even experience a minor throughput decrease (e.g., ~7.7% in specific nginx tests). Single-flow applications are generally rare in high-performance contexts.

  * **Frequent thread migration:** If application threads frequently move between CPUs, RFS constantly updates CPU mappings(for example, applications using large dynamic worker thread pools where requests are frequently handed off between different cores), which can lead to excessive cross-CPU traffic and packet reordering.




### Configuration script

Run the following script on the guest operating system of your Compute Engine instance. The script requires `sudo` or `root` permissions to modify kernel parameters.

The script enables RPS, maps network queues to available CPUs in a round-robin fashion, and sets the per-queue flow table size to 65536.
    
    
    #!/bin/bash
    set -e
    
    # Note: This script uses 'apt' and is intended for Debian-based systems.
    # If 'iproute2' is not found, you may need to run 'sudo apt update' first.
    sudo apt install -y iproute2
    
    # This script enables and configures RPS (Receive Packet Steering) and RFS
    # (Receive Flow Steering) for the primary network interface.
    # It creates a 1:1 mapping of CPUs to receive queues and sets a specific
    # flow count for each queue.
    
    # --- Configuration ---
    # The desired number of flow entries per receive queue.
    RPS_FLOW_CNT_PER_QUEUE=65536
    
    # --- Script Body ---
    
    # 1. Auto-detect the primary network interface.
    INTERFACE=$(ip route | grep default | awk '{print $5}' | head -n 1)
    
    if [ -z "$INTERFACE" ]; then
      echo "Error: Could not determine the primary network interface."
      exit 1
    fi
    echo "Primary network interface detected: $INTERFACE"
    
    echo "Starting RPS/RFS configuration for interface: $INTERFACE"
    
    # 2. Determine the number of receive queues for the interface.
    NUM_QUEUES=$(ls -d /sys/class/net/$INTERFACE/queues/rx-* 2>/dev/null | wc -l)
    if [ "$NUM_QUEUES" -eq 0 ]; then
      echo "Error: No receive queues found for interface $INTERFACE."
      echo "Please check if the network driver supports multi-queue."
      exit 1
    fi
    echo "Found $NUM_QUEUES receive queues for interface $INTERFACE."
    
    # 3. Determine the number of CPUs.
    NUM_CPUS=$(nproc)
    if [ -z "$NUM_CPUS" ] || [ "$NUM_CPUS" -eq 0 ]; then
      echo "Error: Could not determine the number of CPUs."
      exit 1
    fi
    echo "Found $NUM_CPUS CPUs."
    
    # 4. Calculate and set the total socket flow entries.
    # This is the total number of entries in the global socket flow table.
    RPS_SOCK_FLOW_ENTRIES=$((NUM_QUEUES * RPS_FLOW_CNT_PER_QUEUE))
    echo "Setting the total RPS socket flow entries to $RPS_SOCK_FLOW_ENTRIES..."
    if ! echo "$RPS_SOCK_FLOW_ENTRIES" | sudo tee /proc/sys/net/core/rps_sock_flow_entries > /dev/null; then
      echo "Error: Failed to set rps_sock_flow_entries. Please run with sufficient privileges."
      exit 1
    fi
    
    # 5. Configure each receive queue.
    for i in $(seq 0 $((NUM_QUEUES - 1))); do
      RX_QUEUE="/sys/class/net/$INTERFACE/queues/rx-$i"
    
      # a) Assign a CPU to this queue (round-robin).
      CPU_INDEX=$((i % NUM_CPUS))
      CPU_BITMAP_HEX=$(printf '%x' $((1 << CPU_INDEX)))
      echo "Assigning CPU $CPU_INDEX (bitmap: $CPU_BITMAP_HEX) to queue rx-$i"
      if ! echo "$CPU_BITMAP_HEX" | sudo tee "$RX_QUEUE/rps_cpus" > /dev/null; then
        echo "Error writing bitmap to $RX_QUEUE/rps_cpus"
        exit 1
      fi
    
      # b) Set the flow count for this queue.
      echo "Setting flow count for $RX_QUEUE to $RPS_FLOW_CNT_PER_QUEUE"
      if ! echo "$RPS_FLOW_CNT_PER_QUEUE" | sudo tee "$RX_QUEUE/rps_flow_cnt" > /dev/null; then
        echo "Error writing to $RX_QUEUE/rps_flow_cnt"
        exit 1
      fi
    done
    
    echo "RPS and RFS configuration updated successfully for $INTERFACE."
    

## What's next

  * Use a [sample Google Kubernetes Engine YAML file](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/sample-yaml-files) to configure tuning best practices.

  * Learn about [profile-based configurations for AI/ML workloads](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/profile-based-configurations).

  * Learn how to [optimize the performance of the Cloud Storage FUSE CSI driver on Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-perf).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
