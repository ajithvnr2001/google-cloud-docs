---
url: https://docs.cloud.google.com/compute/docs/disks/optimize-hyperdisk/
title: Optimize Hyperdisk performance \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:47:43.905365+00:00
---

# Optimize Hyperdisk performance  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/optimize-hyperdisk/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Optimize Hyperdisk performance Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

After you provision your Google Cloud Hyperdisk volumes, your application and operating system might require performance tuning to meet your performance needs.

In the following sections, we describe a few key elements that can be tuned for better performance and how you can apply some of these elements to specific types of workloads.

For an overview of how Google Cloud Hyperdisk performance works, see [About Hyperdisk performance](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-performance).

## Use a high I/O queue depth

Hyperdisk volumes have higher latency than locally attached disks such as local SSDs because they are network-attached devices. They can provide very high IOPS and throughput, but you need to make sure that enough I/O requests are done in parallel. The number of I/O requests done in parallel is referred to as the _I/O queue depth_.

The following tables show the recommended I/O queue depth to ensure you can achieve a certain performance level. The tables use a slight overestimate of typical latency in order to show conservative recommendations. The example assumes that you are using an I/O size of 16 KB.

**Desired IOPS** | **Queue depth**  
---|---  
500 | 1  
1,000 | 2  
2,000 | 4  
4,000 | 8  
8,000 | 16  
16,000 | 32  
32,000 | 64  
64,000 | 128  
100,000 | 200  
200,000 | 400  
320,000 | 640  
**Desired throughput (MB/s)** | **Queue depth**  
---|---  
8 | 1  
16 | 2  
32 | 4  
64 | 8  
128 | 16  
256 | 32  
512 | 64  
1,000 | 128  
1,200 | 153  
  
## Ensure you have free CPUs

Reading and writing to Hyperdisk volumes requires CPU cycles from your VM. If your VM instance is starved for CPU, your application won't be able to manage the IOPS described earlier. To achieve very high, consistent IOPS levels, you must have CPUs free to process I/O.

## Disable database-level torn write protection to optimize writes

Because Google Cloud Hyperdisk provides built-in torn write protection, you can disable database-level protection features to reduce I/O overhead and increase database write throughput by up to 25%. To learn more about this feature, see [Torn-write protection](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#torn-write-protection) in the Hyperdisk overview page.

### Environment configuration requirements

For Hyperdisk's torn-write protection to be effective, database writes must not fragment before they reach the storage layer. Depending on your database, you can achieve this by using one of the following configuration options:

#### Option 1: Align layers to 16 KiB block boundaries (recommended for MySQL and PostgreSQL)

Configure your operating system, file system, and intermediate software layers to preserve the 16 KiB boundary. When you use this option, you must maintain this specific configuration:

  * **File system** : Use an `ext4` file system. You must create the file system with the `bigalloc` option and configure the file system's cluster size to 16 KiB (16,384 bytes) or a larger power-of-two multiple of 16 KiB:
        
        mkfs.ext4 -O bigalloc -C 16384 /dev/<var>DEVICE_NAME</var>
        

Replace `DEVICE_NAME` with the name of the storage device.

  * **Unsupported configurations** : Avoid configurations that can introduce torn writes above the block storage layer, such as the following:

    * Running containerized databases on Google Kubernetes Engine or self-hosted Kubernetes.
    * Storing database files on an `xfs` file system, which typically does not support sufficient block sizes on most Linux distributions.
    * Using redundant arrays of independent disks (RAID) configurations or logical volume managers (LVM) that strip I/O.
    * Using Hyperdisk with Local SSD caches, including `lvmcache`, `dm-cache`, or `bcache`.
    * Using nested virtualization for the database VM.



#### Option 2: Use Linux block atomic I/O (recommended for MariaDB)

If your database or application supports Linux block atomic I/O and accesses files using direct I/O (`O_DIRECT`), then you can bypass the configuration rules listed in option 1 provided that you meet the following conditions:

  * **RWF_ATOMIC flag** : The application must use the `pwritev2()` system call with the `RWF_ATOMIC` flag. When using this flag, the Linux kernel ensures that a write operation is processed as a single contiguous block by the underlying Hyperdisk device. If the kernel cannot guarantee atomicity, then the write call fails immediately to prevent data corruption.
  * **Operating system** : Must be Linux kernel version 6.11 or later.
  * **File system** : Must be `ext4` or `xfs` on Linux kernel version 6.13 or later.
  * **File access** : The application must open database files using direct I/O (`O_DIRECT`).
  * **Supported databases** : We recommend this option only for MariaDB version 11.x or later (for generic Linux RWF_ATOMIC support). MySQL and PostgreSQL don't support this feature.



For detailed database-specific optimization instructions, see [Configure MySQL on Compute Engine](https://docs.cloud.google.com/compute/docs/instances/mysql/mysql-workloads).

## Review Hyperdisk performance metrics

You can review disk performance metrics in [Cloud Monitoring](https://console.cloud.google.com/monitoring), Google Cloud's integrated monitoring solution. You can use these metrics to observe the performance of your disks and other VM resources under different application workloads.

To learn more, see [Reviewing disk performance metrics](https://docs.cloud.google.com/compute/docs/disks/review-disk-metrics).

You can also use the **Observability** page in the console to [view the disk performance metrics](https://docs.cloud.google.com/compute/docs/disks/analyze-iops-hyperdisk#viewing-performance-metrics).

## What's next

  * Learn about [Hyperdisk pricing](https://docs.cloud.google.com/compute/disks-image-pricing#hyperdisk).
  * [Analyze the provisioned IOPS for Hyperdisk volumes](https://docs.cloud.google.com/compute/docs/disks/analyze-iops-hyperdisk).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
