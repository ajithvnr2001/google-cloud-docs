---
url: https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/improve-database-performance-using-io-acceleration/
title: Improve AlloyDB Omni performance using I/O acceleration \u00a0|\u00a0 AlloyDB Omni using containers: 16.13.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:54:33.356961+00:00
---

# Improve AlloyDB Omni performance using I/O acceleration  |  AlloyDB Omni using containers: 16.13.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/improve-database-performance-using-io-acceleration/

This page documents AlloyDB Omni version **16.13.0** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Containers: 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/overview)



Send feedback 

#  Improve AlloyDB Omni performance using I/O acceleration Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 16.13.0keyboard_arrow_down

  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.10.0/docs/improve-database-performance-using-io-acceleration)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/improve-database-performance-using-io-acceleration)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/improve-database-performance-using-io-acceleration)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/improve-database-performance-using-io-acceleration)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/improve-database-performance-using-io-acceleration)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/improve-database-performance-using-io-acceleration)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/improve-database-performance-using-io-acceleration)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/improve-database-performance-using-io-acceleration)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/improve-database-performance-using-io-acceleration)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/improve-database-performance-using-io-acceleration)



**Preview —[AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/overview) **

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). You can process personal data for this feature as outlined in the [Cloud Data Processing Addendum](https://docs.cloud.google.com/terms/data-processing-addendum), subject to the obligations and restrictions described in the agreement under which you access Google Cloud. Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to enable a set of I/O acceleration features in AlloyDB Omni that can help improve your compute and I/O resource utilization for faster workloads and query performance.

**Note:** AlloyDB Omni I/O acceleration features are recommended for sandbox and development purposes only.

The following features are included:

  * Torn write protection
  * `O_DIRECT` support
  * Asynchronous I/O (AIO)
  * Streaming reads



To enable these I/O acceleration features, you enable the `alloydb_omni_atomic` Grand Unified Configuration (GUC) and set up AlloyDB Omni to be able to use the GUC.

## I/O acceleration features

The following sections describe the I/O acceleration features that the `alloydb_omni_atomic` GUC enables.

### Torn write protection

When you enable the `alloydb_omni_atomic` configuration, you turn off [full page writes](https://www.postgresql.org/docs/16/runtime-config-wal.html#GUC-FULL-PAGE-WRITES) to prevent the performance overhead of having to generate full page images for logging.

### O_DIRECT support

`O_DIRECT` support is a prerequisite for atomic writes. `O_DIRECT` applies to the PostgreSQL data directory and the AlloyDB Omni disk cache. For more information, see [Accelerate database performance using disk cache](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/configure-disk-cache).

`O_DIRECT` also offers the following benefits:

  * Using `O_DIRECT` lets you avoid the double-buffering problem in PostgreSQL. PostgreSQL manages its own buffer cache and can bypass the operating system kernel buffer cache.
  * `O_DIRECT` reduces operating the system CPU and memory overhead that are needed to maintain the kernel buffer cache.



### Asynchronous I/O

The `alloydb_omni_atomic` configuration provides asynchronous I/O (AIO) capabilities using the `io_uring` and `libaio` libraries. We recommend that you use `io_uring` to avoid the limitations of the older `libaio` library. AlloyDB Omni falls back to `libaio` when `io_uring` support isn't detected. This approach overcomes the loss of buffered I/O advantages such as readahead and write-combining, and it also ensures that the available I/O bandwidth of the underlying offered storage is maximized.

### Streaming reads

AlloyDB Omni uses streaming reads, similar to the PostgreSQL 17 feature, which provide improved sequential scans, `ANALYZE`, and `pg_prewarm` performance by using vectored I/O to read multiple blocks into the buffer cache. _Vectored I/O_ is a method in which a single procedure call can prefetch data from multiple buffers, which improves efficiency by reducing context switches and system calls.

AlloyDB Omni extends support to use streaming reads for reads from the AlloyDB Omni disk cache using AIO to amplify read performance. This approach facilitates effective read-ahead of buffers into the shared-memory pool from storage for queries to use, rather than having to read these blocks from storage every time they are needed.

## Before you begin

  1. Check your operating system and file system support.

     1. To ensure that the kernel supports [`RWF_ATOMIC`](https://man7.org/linux/man-pages/man2/readv.2.html), check the kernel version. In the following example, you use a Ubuntu 24.10 machine running the Linux 6.14 kernel that supports [atomic writes](https://lwn.net/Articles/552095/).
            
            > sudo hostnamectl
             ...
             Operating System: Ubuntu 24.10
                  Kernel: Linux 6.14.0-061400rc5-generic
            ...
            

     2. If your kernel doesn't have support for `RWF_ATOMIC`, we recommend that you update to a kernel version that supports `RWF_ATOMIC`. 

  2. To use AlloyDB Omni I/O acceleration features to test performance gains with torn write protection, enable the `alloydb_omni_atomic` Grand Unification Configuration (GUC). To use this GUC, you must have a supporting kernel and file system that provide atomic I/O and protect against torn writes.

The `RWF_ATOMIC` flag is used for atomic write support. By default, compatibility for `RWF_ATOMIC` is checked during startup. PostgreSQL fails to start if atomic writes with the `RWF_ATOMIC` flag can't be confirmed.

You can override this default behavior, but we recommend that you use a supported platform and the `force` option to avoid accidentally overriding optimal configuration settings.

You can override the `RWF_ATOMIC`compatibility check by using the`force_unsafe` option, but data safety isn't guaranteed with this override. We recommend that you don't use this option unless you're evaluating AlloyDB Omni in an environment that can't be upgraded to use the appropriate kernel and file system.

The following table lists `alloydb_omni_atomic` configuration settings and corresponding compatibility checks.

**`alloydb_omni_atomic` value** | **Startup compatibility check** | **Description**  
---|---|---  
           
         off

| N/A | This value turns off atomic mode. The feature is inactive.  
           
         force

| Performs startup compatibility check. Fails to start if `RWF_ATOMIC` write fails. | Sets atomic mode configs.  
           
         force_unsafe

| Doesn't perform a startup compatibility check. Returns a warning, but continues if `RWF_ATOMIC` write fails. | Sets atomic mode configs.  
  
In the `force`/`force_unsafe` configuration, `full_page_writes`, `io_combine_limit`, and `debug_io_direct` configurations are automatically set. You can override these configurations using the optional `on`/`on_unsafe` configuration.




## Set up AlloyDB Omni I/O acceleration features

  1. Set up the [XFS filesystem](https://en.wikipedia.org/wiki/XFS) for the data directory. XFS is used because it supports a file system block size greater than page size. AlloyDB Omni can use XFS to atomically write 8KiB blocks with full `RWF_ATOMIC` support.

     1. Create an XFS file system with a block size of 8KiB and mount it at the data directory (`DATA_DIR`) location.
            
            sudo mkfs.xfs -f -b size=8k /dev/$DEVICE
            sudo mount /dev/$DEVICE DATA_DIR
            

Make the following replacement:

        * `DATA_DIR`: the data directory location.
     2. Check the kernel logs to ensure that 8k blocks are used:
            
            > sudo journalctl -f
            ...
            kernel: XFS (sdc): EXPERIMENTAL large block size feature enabled.  Use at your own risk!
            kernel: XFS (sdc): Mounting V5 Filesystem 350aa26a-7555-4566-94c1-74e54ddc9250
            ...
            

  2. Optional: Set up the AlloyDB Omni disk cache.

Use the following example to create a file system using `ext4,` and then mount the file system.
         
         sudo /sbin/mkfs.ext4 -m 1 -F -E lazy_itable_init=0,lazy_journal_init=0 /dev/DEVICE
         sudo mount --make-shared -o noatime,discard,errors=panic /dev/DEVICE /OMNI_DISK_CACHE_DIRECTORY
         

Make the following replacement:

     * `DEVICE`: the entity with which the application interacts to perform I/O operations (reading or writing data).

To support optimal performance of AlloyDB Omni I/O acceleration features when primary storage doesn't offer higher Input/Output Operations Per Second (IOPS), we recommend that you set up AlloyDB Omni disk cache. For more information, see [Accelerate database performance using disk cache](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/configure-disk-cache).

**Note:** The disk cache doesn't need to support atomic writes because data in the cache is ephemeral. However, AlloyDB Omni I/O acceleration features still use `O_DIRECT` to access the cache.
  3. Download and run AlloyDB Omni.

     1. Download the latest AlloyDB Omni Docker container. For more information, see [Install AlloyDB Omni on a VM](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/deploy-vm).
     2. To use the disk cache, follow the instructions in [Accelerate database performance using disk cache](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/configure-disk-cache).
     3. To allow `io_uring`, add an additional argument, `--security-opts="seccomp:unconfined"`
            
            docker run -d --name CONTAINER_NAME \
               -e POSTGRES_PASSWORD=NEW_PASSWORD \
               -v DATA_DIR:/var/lib/postgresql/data \
               -v /OMNI_DISK_CACHE_DIRECTORY:/CACHE_DIRECTORY_PATH_INSIDE_CONTAINER \  # Only if disk cache is enabled
               -p HOST_PORT:5432 \
               --security-opts="seccomp:unconfined" \
               --restart=always \
               google/alloydbomni:16
            

Make the following replacements:

        * `CONTAINER_NAME`: the name of the AlloyDB Omni container in your host machine's container registry.
        * `NEW_PASSWORD`: the password assigned to the container's PostgreSQL user.
        * `DATA_DIR`: the data directory location.
        * `CACHE_DIRECTORY_PATH_INSIDE_CONTAINER`: the disk cache directory path inside the container.
        * `HOST_PORT`: the TCP post on the host machine that the container should publish its own port 5432 to.
  4. Configure AlloyDB Omni to use atomic I/O.

Set the `alloydb_omni_atomic` GUC to an appropriate value and restart the container.
         
         alter system set alloydb_omni_atomic='force';
         sudo docker restart CONTAINER_NAME;
         

Make the following replacements:

     * `CONTAINER_NAME`: the name of the AlloyDB Omni container in your host machine's container registry.



## Limitations

  * PostgreSQL 16 contains paths that perform single block I/O, which `O_DIRECT` slows down. There might be slower reads during database recovery (redo path), vacuum scans, and Omni disk cache prewarming.
  * AlloyDB Omni I/O acceleration features in read replicas aren't supported in [Preview](https://cloud.google.com/products?e=48754805&#product-launch-stages).
  * Under heavy workloads, ARM-based systems might exhibit lower performance due to architectural differences.
  * Due to its limitations with increased workloads, `libaio` is susceptible to resource unavailability. `io_uring` might experience memory allocation issues when available system memory is running low.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
