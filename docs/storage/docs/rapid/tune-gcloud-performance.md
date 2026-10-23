---
url: https://docs.cloud.google.com/storage/docs/rapid/tune-gcloud-performance/
title: Tune gcloud CLI performance for zonal buckets \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:55.675316+00:00
---

# Tune gcloud CLI performance for zonal buckets  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/rapid/tune-gcloud-performance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Tune gcloud CLI performance for zonal buckets Stay organized with collections  Save and categorize content based on your preferences. 

When you read objects from zonal buckets in [Rapid Bucket](https://docs.cloud.google.com/storage/docs/rapid/rapid-bucket) by using the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/storage), the CLI automatically applies default concurrency and slicing configurations based on available system resources.

This document describes these default configurations and explains how to tune gcloud CLI performance for specific workloads by configuring concurrency, process scaling, and opt-in features, such as NIC isolation.

Before you tune performance settings, you must [create a zonal bucket](https://docs.cloud.google.com/storage/docs/rapid/create-zonal-buckets). If you download objects to an attached storage volume, such as [Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks) or Local SSD, [format and mount the volume](https://docs.cloud.google.com/compute/docs/disks/format-mount-disk-linux) in your environment. If you plan to mount zonal buckets as a file system instead of using the gcloud CLI, see [Cloud Storage FUSE performance for Rapid Bucket](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/performance#rapid-bucket). For general slicing concepts, see [Sliced object downloads](https://docs.cloud.google.com/storage/docs/sliced-object-downloads).

## Default concurrency and slicing configurations

The default configurations that are described in this section apply specifically when you read objects from zonal buckets in [Rapid Bucket](https://docs.cloud.google.com/storage/docs/rapid/rapid-bucket) by using the gcloud CLI version 583.0.0 or later. For standard Cloud Storage buckets, the gcloud CLI applies its own default concurrency settings.

For zonal buckets, the gcloud CLI automatically sets default concurrency and slicing parameters based on the number of available virtual CPU (vCPU) cores and whether you download a single object or multiple objects. These defaults configure the following properties:

  * **Process count** : [`storage/process_count`](https://docs.cloud.google.com/sdk/gcloud/reference/config/set#process_count)
  * **Thread count** : [`storage/thread_count`](https://docs.cloud.google.com/sdk/gcloud/reference/config/set#thread_count)
  * **Slicing threshold** : [`storage/sliced_object_download_threshold`](https://docs.cloud.google.com/sdk/gcloud/reference/config/set#sliced_object_download_threshold)
  * **Max components** : [`storage/sliced_object_download_max_components`](https://docs.cloud.google.com/sdk/gcloud/reference/config/set#sliced_object_download_max_components)
  * **Component size** : [`storage/sliced_object_download_component_size`](https://docs.cloud.google.com/sdk/gcloud/reference/config/set#sliced_object_download_component_size)



The following sections list the default values for single-object and multi-object downloads.

### Single-object downloads

When you download a single object, the gcloud CLI applies the following default values:

Available vCPUs | Process count | Thread count | Slicing threshold | Max components | Component size  
---|---|---|---|---|---  
`≥ 8` | `8` | `2` | `50 MiB` | `16` | `5 MiB`  
`< 8` | `4` | `2` | `50 MiB` | `8` | `5 MiB`  
  
### Multi-object downloads

When you download multiple objects simultaneously, the gcloud CLI applies the following default values:

Available vCPUs | Process count | Thread count | Slicing threshold | Max components | Component size  
---|---|---|---|---|---  
`≥ 48` | `min(96, available_cores * 0.75)` | `1` | `10 MiB` | `5` | `5 MiB`  
`4 to 47` | `16` | `4` | `10 MiB` | `10` | `5 MiB`  
`< 4` | `2` | `10` | `50 MiB` | `10` | `5 MiB`  
**Note:** For machines with 48 or more vCPUs, the gcloud CLI allocates 75% of available vCPUs to worker processes (for example, 66 processes on an 88-vCPU VM), up to a maximum of 96 processes.

## Configure concurrency and slicing properties

To configure and apply custom tuning settings, complete the following steps:

  1. [Install or update](https://docs.cloud.google.com/sdk/docs/install-sdk) the Google Cloud CLI to version 583.0.0 or later.

  2. In your development environment, run the [`gcloud config configurations create`](https://docs.cloud.google.com/sdk/gcloud/reference/topic/configurations) command to create and activate a configuration profile:
         
         gcloud config configurations create CONFIGURATION_NAME

Replace `CONFIGURATION_NAME` with a name for your configuration profile, such as `rapid-perf`.

  3. Run the [`gcloud config set`](https://docs.cloud.google.com/sdk/docs/properties) command to configure concurrency and slicing properties:
         
         gcloud config set storage/thread_count THREAD_COUNT
         gcloud config set storage/process_count PROCESS_COUNT
         gcloud config set storage/sliced_object_download_threshold THRESHOLD_SIZE
         gcloud config set storage/sliced_object_download_component_size COMPONENT_SIZE
         gcloud config set storage/sliced_object_download_max_components MAX_COMPONENTS

Replace the following:

     * `THREAD_COUNT`: the number of threads per worker process, such as `1`.
     * `PROCESS_COUNT`: the number of worker processes, such as `64`.
     * `THRESHOLD_SIZE`: the minimum object size threshold to trigger slicing, such as `128 MiB` for multi-gigabyte workloads (or `32 MiB` for smaller objects).
     * `COMPONENT_SIZE`: the target size of each download slice, such as `128 MiB` for multi-gigabyte workloads (or `32 MiB` for smaller objects).
     * `MAX_COMPONENTS`: the maximum number of slice components per object, such as `16`.

For more information about these properties, see Tuning recommendations.

  4. To download objects to your local storage path, run the [`gcloud storage cp`](https://docs.cloud.google.com/sdk/gcloud/reference/storage) command:
         
         gcloud storage cp -r gs://BUCKET_NAME/SOURCE_PATH LOCAL_DESTINATION_PATH

Replace the following:

     * `BUCKET_NAME`: the name of your zonal bucket.
     * `SOURCE_PATH`: the source directory or object path in your bucket.
     * `LOCAL_DESTINATION_PATH`: your local directory path (such as `./data/`) or the mount point of your local storage volume (such as `/mnt/hyperdisk/data/`).



## Tuning recommendations

Use the following recommendations to tune concurrency, slicing, and system resources for your workloads.

### Process count

Set the [`storage/process_count` property](https://docs.cloud.google.com/sdk/gcloud/reference/config/set#process_count) to scale parallel worker processes based on available CPU cores. Limit the process count to a maximum of 80% of available CPU cores:
    
    
    storage/process_count = min(target_cores, 0.8 * available_cores)
    

Where:

  * `target_cores`: the number of CPU cores or worker processes you want to allocate for your transfer (such as `64`).
  * `available_cores`: the total number of virtual CPUs (vCPUs) available on your machine (for example, by running `nproc` on Linux).



For example, if your target is 64 worker processes on a machine with 80 or more vCPUs, set `storage/process_count` to `64`. On a machine with fewer than 80 vCPUs, set `storage/process_count` to 80% of available vCPUs (for example, `51` on a 64-vCPU VM).

### Thread count

Set the [`storage/thread_count` property](https://docs.cloud.google.com/sdk/gcloud/reference/config/set#thread_count) to control the number of threads per worker process. On machines with 48 or more vCPUs, set `storage/thread_count` to `1`.

Restricting each worker process to a single thread on machines with 48 or more vCPUs reduces Python Global Interpreter Lock (GIL) and gRPC thread contention.

### Slicing threshold

Set the [`storage/sliced_object_download_threshold` property](https://docs.cloud.google.com/sdk/gcloud/reference/config/set#sliced_object_download_threshold) to specify the minimum object size required to trigger sliced downloads.

We recommend setting `storage/sliced_object_download_threshold` to a value equal to or greater than `storage/sliced_object_download_component_size`.

### Slices per object

Set the [`storage/sliced_object_download_component_size`](https://docs.cloud.google.com/sdk/gcloud/reference/config/set#sliced_object_download_component_size) and [`storage/sliced_object_download_max_components`](https://docs.cloud.google.com/sdk/gcloud/reference/config/set#sliced_object_download_max_components) properties to control the number of parallel slices generated per object. The gcloud CLI calculates slices per object using the following formula:
    
    
    Slices per object = min(object_size / component_size, max_components)
    

If an object is large enough that slicing it by the `component_size` value would exceed the `max_components` value, the gcloud CLI ignores the `component_size` value and divides the object evenly into `max_components` slices. For example, downloading a 100 GiB object with `component_size=128 MiB` and `max_components=16` produces 16 slices of 6.25 GiB each.

The gcloud CLI downloads each slice independently and in parallel based on your total worker capacity (`storage/process_count` × `storage/thread_count`).

### Worker saturation

To maintain high worker utilization throughout a transfer, you must adjust the process count, thread count, component size, and max components. These adjustments ensure that typical transfers generate enough total slices to equal or exceed your total worker capacity:
    
    
    Total slices across all objects >= storage/process_count * storage/thread_count
    

For example, consider downloading four objects using 64 worker processes (`process_count=64` and `thread_count=1`):

  * **Four 2 GiB objects** : setting `component_size=128 MiB` generates 16 slices per object (4 × 16 = 64 slices), which fully utilizes all 64 worker processes.
  * **Four 512 MiB objects** : setting `component_size=32 MiB` generates 16 slices per object (4 × 16 = 64 slices), which fully utilizes all 64 worker processes. In contrast, using `component_size=128 MiB` on 512 MiB objects produces only 4 slices per object (16 total slices), leaving 48 worker processes idle.



### NIC isolation

On Linux machines with more than 16 CPU cores, you can enable network interface card (NIC) isolation by setting the [`storage/use_nic_isolation` property](https://docs.cloud.google.com/sdk/gcloud/reference/config/set#use_nic_isolation) to `True`:
    
    
    gcloud config set storage/use_nic_isolation True

When you enable this property, the gcloud CLI sets CPU affinity (`os.sched_setaffinity()`). This configuration isolates 10% of CPU cores for network hardware interrupt requests (IRQs) and reserves the remaining cores for data processing.

**Note:** NIC isolation is supported only on Linux.

## What's next

  * [Learn about Rapid Bucket](https://docs.cloud.google.com/storage/docs/rapid/rapid-bucket).
  * [Create zonal buckets](https://docs.cloud.google.com/storage/docs/rapid/create-zonal-buckets).
  * [Read and append to objects in zonal buckets](https://docs.cloud.google.com/storage/docs/rapid/use-objects-in-zonal-buckets).
  * [Understand direct connectivity for Cloud Storage](https://docs.cloud.google.com/storage/docs/direct-connectivity).
  * [Understand sliced object downloads](https://docs.cloud.google.com/storage/docs/sliced-object-downloads).
  * [Tune Cloud Storage FUSE performance for Rapid Bucket](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/performance#rapid-bucket).
  * [Manage gcloud CLI properties](https://docs.cloud.google.com/sdk/docs/properties).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
