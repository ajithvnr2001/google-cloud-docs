---
url: https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/file-caching/
title: File caching in Cloud Storage FUSE \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:51:52.917395+00:00
---

# File caching in Cloud Storage FUSE  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/file-caching/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  File caching in Cloud Storage FUSE Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Storage FUSE file caching is a client-side read cache that improves the performance of repeat file reads by serving them from a faster cache storage of your choice. When file caching is enabled, Cloud Storage FUSE stores copies of frequently accessed files locally, which reduces latency and improves throughput for subsequent reads.

This document provides an overview of file caching and describes how to configure and use it.

## Benefits of file caching

File caching provides the following benefits:

  * **Improved performance for small and random I/Os** : file caching improves latency and throughput by serving reads directly from the cache media. Small and random I/O operations can be significantly faster when served from the cache.

  * **Parallel downloads enabled automatically** : parallel downloads are enabled automatically on Cloud Storage FUSE versions 2.12 and later when the file cache is enabled. Parallel downloads utilize multiple workers to download a file in parallel using the file cache directory as a prefetch buffer, which can result in up to nine times faster model load time. We recommend that you use parallel downloads for single-threaded read scenarios that load large files such as model serving and checkpoint restores. 

  * **Use of existing capacity** : file caching can use existing provisioned machine capacity for your cache directory without incurring charges for additional storage. This includes Local SSDs that come bundled with Cloud GPUs machine types such as [`a2-ultragpu`](https://docs.cloud.google.com/compute/docs/gpus#a100-gpus), [`a3-highgpu`](https://docs.cloud.google.com/compute/docs/gpus#h100-gpus), Persistent Disk (which is the boot disk used by each VM), or in-memory `/tmpfs`.

  * **Reduced charges** : cache hits are served locally and don't incur Cloud Storage operation or network charges.

  * **Improved total cost of ownership for AI and ML training** : file caching increases Cloud GPUs and Cloud TPU utilization by loading data faster, which reduces time to training and provides a greater price-performance ratio for artificial intelligence and machine learning (AI/ML) training workloads.




## Parallel downloads

Parallel downloads can improve read performance by using multiple workers to download multiple parts of a file in parallel using the file cache directory as a prefetch buffer. We recommend using parallel downloads for read scenarios that load large files such as model serving, checkpoint restores, and training on large objects.

Use cases for enabling file caching with parallel downloads include the following:

Use case type | Description  
---|---  
Training | Enable file caching if the data you want to access is read multiple times, whether the same file multiple times, or different offsets of the same file. If the dataset is larger than the file cache, the file cache should remain disabled, and instead, use one of the following methods: 

  * [`--file-cache-cache-file-for-range-read` `gcsfuse` option](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#file-cache-cache-file-for-range-read)
  * [`file-cache:cache-file-for-range-read` configuration file field](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/config-file#cache-file-for-range-read)

  
Serving model weights and checkpoint reads | Enable file caching with parallel downloads to be able to utilize parallel downloads, which loads large files much faster than if file caching and parallel downloads aren't used.  
  
## Considerations

  * **File cache time to live (TTL)** : if a file cache entry hasn't yet expired based on its TTL and the file is in the cache, read operations to that file are served from the local client cache without any request being issued to Cloud Storage.

  * **File cache entry expiration** : if a file cache entry has expired, a `GET` file attributes call is first made to Cloud Storage. If the file is missing or its attributes or contents have changed, the new content is retrieved. If the attributes were only invalidated but the content remains valid, meaning object generation hasn't changed, the content is served from the cache only after the attribute call confirms its validity. Both operations incur network latencies.

  * **File cache invalidation** : when a Cloud Storage FUSE client modifies a cached file or its attributes, that client's cache entry is immediately invalidated for consistency. However, other clients accessing the same file continue to read their cached versions until their individual TTL settings cause an invalidation.

  * **File size and available capacity** : the file being read must fit within the available capacity in the file cache directory, which you can control by using either the [`--file-cache-max-size-mb` option](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#file-cache-max-size-mb) or the [`file-cache:max-size-mb` field](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/config-file#max-size-mb). Note that you can't set a maximum size per file.

  * **Cache eviction** : the eviction of cached metadata and data is based on a least recently used (LRU) algorithm that begins once the space threshold configured per [`--file-cache-max-size-mb`](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#file-cache-max-size-mb) limit is reached. If the entry expires based on its TTL, a `GET` metadata call is first made to Cloud Storage and is subject to network latencies. Since the data and metadata are managed separately, you might experience one entity being evicted or invalidated and not the other.

  * **Cache persistence** : Cloud Storage FUSE caches aren't persisted on unmounts and restarts. For file caching, while the metadata entries needed to serve files from the cache are evicted on unmounts and restarts, data in the file cache might still be present in the file directory. We recommend that you delete data in the file cache directory after unmounts or restarts.

  * **Random and partial read management** : when the first file read operation starts from the beginning of the file, at offset `0`, the Cloud Storage FUSE file cache ingests and loads the entire file into the cache, even if you're only reading from a small range subset. This lets subsequent random or partial reads from the same object get served directly from the cache.

By default, reading from any other offset doesn't trigger an asynchronous full file fetch. To change this behavior so that Cloud Storage FUSE ingests a file to the cache upon an initial random read, set either the [`--file-cache-cache-file-for-range-read`](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#file-cache-cache-file-for-range-read) option or [`file-cache:cache-file-for-range-read`](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/config-file#cache-file-for-range-read) field to `true`.

We recommend that you enable this property if many different random or partial read operations are performed on the same object.

  * **Data security** : when you enable caching, Cloud Storage FUSE uses the cache directory you specified using either the [`--cache-dir`](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#cache-dir) option or [`cache-dir`](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/config-file#cache-dir) field as the underlying directory for the cache to persist files from your Cloud Storage bucket in an encrypted format. Any user or process that has access to this cache directory can access these files. We recommend restricting access to this directory.

  * **Direct or multiple access to the file cache** : using a process other than Cloud Storage FUSE to access or modify a file in the cache directory can lead to data corruption. Cloud Storage FUSE caches are specific to each Cloud Storage FUSE running process with no awareness across different Cloud Storage FUSE processes running on the same or different machines. Therefore, we don't recommend using the same cache directory for different Cloud Storage FUSE processes.

  * **Running multiple Cloud Storage FUSE processes on the same machine** : if multiple Cloud Storage FUSE processes need to run on the same machine, each Cloud Storage FUSE process should get its own specific cache directory, or use one of following methods to ensure your data doesn't get corrupted:

    * **Mount all buckets with a shared cache** : use dynamic mounting to mount all buckets you have access to in a single process with a shared cache. To learn more, see [Cloud Storage FUSE dynamic mounting](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/mount-bucket#dynamic-mount).

    * **Enable caching on a specific bucket** : enable caching on only a specified bucket using static mounting. To learn more, see [Cloud Storage FUSE static mounting](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/mount-bucket#static-mount).

    * **Cache only a specific folder or directory** : mount and cache only a specific bucket-level folder instead of mounting an entire bucket. To learn more, see [Mount a directory within a bucket](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/mount-bucket#directory-mount).




## Before you begin

The file cache requires a directory path to be used to cache files. You can create a new directory on an existing file system or create a new file system on provisioned storage. If you are provisioning new storage to be used, use the following instructions to create a new file system:

  1. For Google Cloud Hyperdisk, see [Create a new Google Cloud Hyperdisk volume](https://docs.cloud.google.com/compute/docs/disks/add-hyperdisk).

  2. For Persistent Disk, see [Create a new Persistent Disk volume](https://docs.cloud.google.com/compute/docs/disks/format-mount-disk-linux).

  3. For Local SSDs, see [Add a Local SSD to your VM](https://docs.cloud.google.com/compute/docs/disks/add-local-ssd).

  4. For in-memory RAM disks, see [Creating in-memory RAM disks](https://docs.cloud.google.com/compute/docs/disks/mount-ram-disks).




## Enable and configure file caching behavior

  1. Select the method through which you want to enable and configure file caching using one of the following methods:

     * Supply it as the value for a [`gcsfuse` option](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options)

     * Specify it in a [Cloud Storage FUSE configuration file](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/config-file)

**Note:** You can also use sample configurations to enable and configure file caching. For more information, see [Sample configuration for enabling file caching and parallel downloads](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/performance#sample-config-file-caching-parallel-downloads).
  2. Specify the cache directory you want to use with one of the following methods. This lets you enable the file cache for non-Google Kubernetes Engine deployments:

     * `gcsfuse` option: [`--cache-dir`](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#cache-dir)
     * Configuration file field: [`cache-dir`](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/config-file#cache-dir)

If you're using a Google Kubernetes Engine deployment using the Cloud Storage FUSE CSI driver for Google Kubernetes Engine, specify one of the following methods:

     * `gcsfuse` option: [`--file-cache-max-size-mb`](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#file-cache-max-size-mb)
     * Configuration file field: [`file-cache:max-size-mb`](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/config-file#max-size-mb)
**Note:** For more information on how to enable file caching on Google Kubernetes Engine, see [Enable and use file caching](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-perf#enable-and-use-file-caching).
  3. Optional: enable parallel downloads by setting one of the following methods to `true` if parallel downloads weren't enabled automatically:

     * `gcsfuse` option: [`--file-cache-enable-parallel-downloads`](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#file-cache-enable-parallel-downloads)
     * Configuration file field: [`file-cache:enable-parallel-downloads`](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/config-file#enable-parallel-downloads)
  4. Limit the total capacity the Cloud Storage FUSE cache can use within its mounted directory by adjusting one of the following options, which is automatically set to a value of `-1` when you specify a cache directory:

     * `gcsfuse` option: [`--file-cache-max-size-mb`](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#file-cache-max-size-mb)
     * Configuration file field: [`file-cache:max-size-mb`](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#file-cache-max-size-mb)

You can also specify a value in MiB or GiB to limit the cache size.

**Note:** If you're using Compute Engine virtual machines (VMs) such as standalone Cloud Storage FUSE or non-Google Kubernetes Engine based deployments, the `--file-cache-max-size-mb` option or `file-cache:max-size-mb` field is enabled automatically and set to `-1` when you enable `cache-dir`.
  5. Optional: bypass the TTL expiration of cached entries and serve file metadata from the cache if it's available using one of the following methods and setting a value of `-1`:

     * `gcsfuse` option: [`--metadata-cache-ttl-secs`](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#metadata-cache-ttl-secs)
     * Configuration file field: [`metadata-cache:ttl-secs`](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/config-file#ttl-secs)

The default is 60 seconds, and a value of `-1` sets it to unlimited. You can also specify a high value based on your requirements. We recommend that you set the `ttl-secs` value to as high as your workload lets you. For more information about the TTL for cached entries, see [Considerations](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/file-caching#considerations).

  6. Optional: enable the file cache's ability to asynchronously load the entire file into the cache if the file's first read operation starts from anywhere other than `offset 0` so that subsequent reads of different offsets from the same file can also be served from the cache. Use one of the following methods and set the option to `true`:

     * `gcsfuse` option: [`--file-cache-cache-file-for-range-read`](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#file-cache-cache-file-for-range-read)
     * Configuration file field: [`file-cache:cache-file-for-range-read`](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#file-cache-cache-file-for-range-read)
  7. Optional: configure stat caching. To learn more about stat cache, see [Overview of stat caching](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/stat-caching).

  8. Manually run the `ls -R` command on your mounted bucket before you run your workload to pre-populate metadata to ensure the stat cache populates ahead of the first read in a faster, batched method. For more information about how to improve first time read performance, see [Improve first-time reads](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/performance#pre-populate-the-metadata-cache).




Once you enable file caching, parallel downloads are enabled automatically on Cloud Storage FUSE versions 2.12 and later. If you're using an older version of Cloud Storage FUSE, set the `enable-parallel-downloads` option to `true` to enable parallel downloads.

## Configure supporting properties for parallel downloads

You can optionally configure the following supporting properties for parallel downloads using the Cloud Storage FUSE CLI or a Cloud Storage FUSE configuration file:

Property description | `gcsfuse` option | Configuration file field  
---|---|---  
The maximum number of workers that can be spawned per file to download the object from Cloud Storage into the file cache. | [`--file-cache-parallel-downloads-per-file`](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#file-cache-parallel-downloads-per-file) | [`file-cache:parallel-downloads-per-file`](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/config-file#parallel-downloads-per-file)  
The maximum number of workers that can be spawned at any given time across all file download jobs. The default is set to twice the number of CPU cores on your machine. To specify no limit, enter a value of `-1`. | [`--file-cache-max-parallel-downloads`](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#file-cache-max-parallel-downloads) | [`file-cache:max-parallel-downloads`](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/config-file#max-parallel-downloads)  
The size of each read request in MiB that each worker makes to Cloud Storage when downloading the object into the file cache. Note that a parallel download is only triggered if the file being read is the specified size. | [`--file-cache-download-chunk-size-mb`](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#file-cache-download-chunk-size-mb) | [`file-cache:download-chunk-size-mb`](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/config-file#download-chunk-size-mb)  
  
## Disable parallel downloads

To disable parallel downloads, set one of the following to `false`:

  * `gcsfuse` option: `--file-cache-enable-parallel-downloads`
  * Configuration file field: `file-cache:enable-parallel-downloads`



## Control cacheability at file granularity using regular expressions

By default, all files that are read are cached. You can control which files are cached at file granularity by using the optional `include-regex` and `exclude-regex` fields in the `file-cache` configuration. These fields let you specify regular expressions to match against file paths in the format `bucket_name/object_key`.

### Include specific files for caching

To cache only files that match a specific pattern, use the `include-regex` option. Any file that doesn't match this regular expression isn't cached. For example, to cache only `.tfrecord` files from your training dataset, specify the following in your configuration file:
    
    
    file-cache:
      include-regex: ".*\\.tfrecord$"
    

Or, use the `--file-cache-include-regex` flag:
    
    
    gcsfuse --file-cache-include-regex ".*\\.(tfrecord)$" ..
    

### Exclude specific files from caching

To prevent specific files from being cached, use the `exclude-regex` option. Any file that matches this regular expression isn't cached. For example, to exclude all files in a directory named `logs/`, specify the following in your configuration file:
    
    
    file-cache:
      exclude-regex: ".*/logs/.*"
    

Or, use the `--file-cache-exclude-regex` flag:
    
    
    gcsfuse --file-cache-exclude-regex ".*/logs/.*" ..
    

### Use include and exclude rules together

You can use both `include-regex` and `exclude-regex` at the same time. The `exclude-regex` rule is always evaluated first. If a file matches `exclude-regex`, it won't be cached, even if it also matches `include-regex`. For example, to cache all `.tfrecord` files except for those in the `output/` directory, specify the following in your configuration file:
    
    
    file-cache:
      include-regex: ".*\\.tfrecord$"
      exclude-regex: ".*/output/.*"
    

Or, use both flags:
    
    
    gcsfuse --file-cache-include-regex ".*\\.tfrecord$" --file-cache-exclude-regex ".*/output/.*" ..
    

## What's next

  * Review [considerations for caching in Cloud Storage FUSE](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/caching#considerations).

  * Learn how to improve [Cloud Storage FUSE performance](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/performance).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
