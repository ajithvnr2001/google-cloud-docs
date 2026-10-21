---
url: https://docs.cloud.google.com/compute/docs/disks/optimizing-pd-performance/
title: Optimize Persistent Disk performance \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T14:21:29.875608+00:00
---

# Optimize Persistent Disk performance  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/optimizing-pd-performance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Optimize Persistent Disk performance Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

Persistent Disks give you the performance described in the [disk type chart](https://docs.cloud.google.com/compute/docs/disks/performance#performance_limits) if the Compute Engine instance drives usage that is sufficient to reach the performance limits. After you size your Persistent Disk volumes to meet your performance needs, your workload and operating system might need some tuning.

The following sections describe compute instance and workload characteristics that impact disk performance and discuss a few key elements that can be tuned for better performance. Some of the suggestions and how to apply some of them to specific types of workloads.

## Factors that affect disk performance

The following sections describe factors that impact disk performance for a compute instance.

  * Network egress caps on write throughput
  * Simultaneous reads and writes
  * Logical volume size
  * Multiple disks attached to a single compute instance



### Network egress caps on write throughput

Your compute instance has a [network egress cap](https://docs.cloud.google.com/vpc/docs/quota#per_instance) that depends on the machine type of the instance.

Compute Engine stores data on Persistent Disk with multiple parallel writes to ensure built-in redundancy. Also, each write request has some overhead that uses additional write bandwidth.

The maximum write traffic that a compute instance can issue is the network egress cap divided by a bandwidth multiplier that accounts for the replication and overhead.

The network egress caps are listed in the **Default egress bandwidth (Gbps)** column in the machine type tables for [general purpose](https://docs.cloud.google.com/compute/docs/general-purpose-machines), [compute-optimized](https://docs.cloud.google.com/compute/docs/compute-optimized-machines), [storage-optimized](https://docs.cloud.google.com/compute/docs/storage-optimized-machines), [memory-optimized](https://docs.cloud.google.com/compute/docs/memory-optimized-machines), and [accelerator-optimized](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines) machine families.

The bandwidth multiplier is approximately 1.16x at full network utilization meaning that 16% of bytes written are overhead. For regional Persistent Disk, the bandwidth multiplier is approximately 2.32x to account for additional replication overhead.

In a situation where Persistent Disk read and write operations compete with network egress bandwidth, 60% of the maximum network egress bandwidth, defined by the machine type, is allocated to Persistent Disk writes. The remaining 40% is available for all other network egress traffic. Refer to [egress bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth#vm-out) for details about other network egress traffic.

The following example shows how to calculate the maximum write bandwidth for a Persistent Disk on an [N1 compute instance](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n1_machines). The **bandwidth allocation** is the portion of network egress bandwidth allocated to Persistent Disk. The **maximum write bandwidth** is the maximum write bandwidth of the Persistent Disk adjusted for overhead.

vCPU Count | Network egress cap (MB/s) | Bandwidth allocation (MB/s) | Maximum write bandwidth (MB/s) | Maximum write bandwidth at full network utilization (MB/s)  
---|---|---|---|---  
1 | 250 | 150 | 216 | 129  
2-7 | 1,250 | 750 | 1,078 | 647  
8-15 | 2,000 | 1,200 | 1,724 | 1,034  
16+ | 4,000 | 2,400 | 3,448 | 2,069  
  
You can calculate the maximum Persistent Disk bandwidth using the following formulas:

**N1 instance with 1 vCPU**

The network egress cap is:

2 Gbps / 8 bits = 0.25 GB per second = 250 MB per second

Persistent Disk bandwidth allocation at full network utilization is:

250 MB per second * 0.6 = 150 MB per second.

Persistent Disk maximum write bandwidth with no network contention is:

  * Zonal disks: 250 MB per second / 1.16 ~= 216 MB per second
  * Regional disks: 250 MB per second / 2.32 ~= 108 MB per second



Persistent Disk maximum write bandwidth at full network utilization is:

  * Zonal disks: 150 MB per second / 1.16 ~= 129 MB per second
  * Regional disks: 150 MB per second / 2.32 ~= 65 MB per second



The network egress limits provide an upper bound on performance. Other factors may limit performance below this level. See the following sections for information on other performance constraints.

### Simultaneous reads and writes

For standard Persistent Disk, simultaneous reads and writes share the same resources. When your compute instance is using more read throughput or IOPS, it is able to perform fewer writes. Conversely, instances that use more write throughput or IOPS are able to perform fewer reads.

Persistent Disk volumes cannot simultaneously reach their maximum throughput and IOPS limits for both reads and writes.

The calculation for throughput is `IOPS * I/O size`. To take advantage of the maximum throughput limits for simultaneous reads and writes on SSD Persistent Disk, use an I/O size such that read and write IOPS combined don't exceed the IOPS limit.

The following table lists the IOPS limits per compute instance for simultaneous reads and writes.

Standard Persistent Disk | SSD Persistent Disk (8 vCPUs) | SSD Persistent Disk (32+ vCPUs) | SSD Persistent Disk (64+ vCPUs)  
---|---|---|---  
Read | Write | Read | Write | Read | Write | Read | Write  
7,500 | 0 | 15,000 | 0 | 60,000 | 0 | 100,000 | 0  
5,625 | 3,750 | 11,250 | 3,750 | 45,000 | 15,000 | 75,000 | 25,000  
3,750 | 7,500 | 7,500 | 7,500 | 30,000 | 30,000 | 50,000 | 50,000  
1875 | 11,250 | 3,750 | 11,250 | 15,000 | 45,000 | 25,000 | 75,000  
0 | 15,000 | 0 | 15,000 | 0 | 60,000 | 0 | 100,000  
  
The IOPS numbers in this table are based on an 8 KB I/O size. Other I/O sizes, such as 16 KB, might have different IOPS numbers but maintain the same read and write distribution.

The following table lists the throughput limits (MiB per second) per instance for simultaneous reads and writes.

Standard Persistent Disk | SSD Persistent Disk (6 to 14 vCPUs) | SSD Persistent Disk (16+ vCPUs)  
---|---|---  
Read | Write | Read | Write | Read | Write  
1200 | 0 | 800* | 800* | 1,200* | 1,200*  
900 | 100  
600 | 200  
300 | 300  
0 | 400  
  
* For SSD Persistent Disk, the max read throughput and max write throughput are independent of each other, so these limits are constant. 

### Logical volume size

Persistent Disk can be up to 64 TiB in size, and you can create single logical volumes of up to 257 TiB using logical volume management inside your compute instance. A larger volume size impacts performance in the following ways:

  * Not all local file systems work well at this scale. Common operations, such as mounting and file system checking might take longer than expected.
  * Maximum Persistent Disk performance is achieved at smaller sizes. Disks take longer to fully read or write with this much storage on one compute instance. If your application supports it, consider using multiple compute instances for greater total-system throughput.
  * Snapshotting large numbers of Persistent Disk might take longer than expected to complete and might provide an inconsistent view of your logical volume without careful coordination with your application.



### Multiple disks attached to a single compute instance

The performance limits of disks when you have multiple disks attached to a compute instance depend on whether the disks are of the same type or different types.

#### Multiple disks of the same type

If you have multiple disks of the same type attached to a compute instance in the same mode (for example, read/write), the performance limits are the same as the limits of a single disk that has the combined size of those disks. If you use all the disks at 100%, the aggregate performance limit is split evenly among the disks regardless of relative disk size.

For example, suppose you have a 200 GB `pd-standard` disk and a 1,000 GB `pd-standard` disk. If you don't use the 1,000 GB disk, then the 200 GB disk can reach the performance limit of a 1,200 GB standard disk. If you use both disks at 100%, then each has the performance limit of a 600 GB `pd-standard` disk (1,200 GB / 2 disks = 600 GB disk).

#### Multiple disks of different types

If you attach different types of disks to a compute instance, the maximum possible performance is the performance limit of the fastest disk that the compute instance supports. The cumulative performance of the attached disks won't exceed the performance limits of the fastest disk the compute instance supports.

## Optimize your disks for IOPS or throughput oriented workloads

Performance recommendations depend on whether you want to maximize IOPS or throughput.

### IOPS-oriented workloads

Databases, whether SQL or NoSQL, have usage patterns of random access to data. Google recommends the following values for IOPS-oriented workloads:

  * I/O queue depth values of 1 for each 400 to 800 of IOPS, up to a limit of 64 on large volumes

  * One free CPU for every 2,000 random read IOPS and 1 free CPU for every 2,500 random write IOPS

  * If the compute instance's machine type supports them, use Hyperdisk Extreme or Hyperdisk Balanced disks, which enable you to change the provisioned IOPS.




Lower readahead values are typically suggested in best practices documents for [MongoDB](http://docs.mongodb.org/), [Apache Cassandra](http://cassandra.apache.org/doc/latest/), and other database applications.

### Throughput-oriented workloads

Streaming operations, such as a Hadoop job, benefit from fast sequential reads, and larger I/O sizes can increase streaming performance.

  * Use an I/O size of 256 KB or larger.

  * If the compute instance's machine type supports them, use Hyperdisk Throughput or Hyperdisk Balanced disks, which enable you to change the provisioned throughput.

  * For standard Persistent Disk, use 8 or more parallel sequential I/O streams when possible. Standard Persistent Disk is designed to optimize I/O performance for sequential disk access, similar to a physical HDD hard drive.

  * Make sure your application is optimized for a reasonable data locality on large disks.

If your application accesses data that is distributed across different parts of a disk over a short period of time (hundreds of GB per vCPU), you won't achieve optimal IOPS. For best performance, optimize for data locality, weighing factors like the fragmentation of the disk and the randomness of accessed parts of the disk.

  * For SSD Persistent Disk, make sure the I/O scheduler in the operating system is configured to meet your specific needs.

On Linux-based systems, check if the I/O scheduler is set to `none`. This I/O scheduler doesn't reorder requests and is ideal for fast, random I/O devices.

    1. On the command line, verify the I/O schedule that is used by your Linux machine:
           
           cat /sys/block/sda/queue/scheduler
           

The output is similar to the following:
           
           [mq-deadline] none
           

The I/O scheduler that is currently active is displayed in square brackets (`[]`).

    2. If your I/O scheduler is not set to `none`, perform one of the following steps:

       * To change your default I/O scheduler to `none`, set `elevator=none` in the `GRUB_CMDLINE_LINUX` entry of the GRUB configuration file. Usually this file is located in `/etc/default/grub`, but on some earlier distributions, it might be located in a different directory.
    
    GRUB_CMDLINE_LINUX="elevator=none vconsole.keymap=us console=ttyS0,38400n8 vconsole.font=latarcyrheb-sun16
    

After updating the GRUB configuration file, [configure the bootloader](https://docs.cloud.google.com/compute/docs/import/import-existing-image#configure_bootloader) on the system so that it can boot on Compute Engine.

       * Alternatively, you can change the I/O scheduler at runtime:
    
    echo 'none' | sudo tee /sys/block/sda/queue/scheduler
    

If you use this method, the system switches back to the default I/O scheduler on reboot. Run the `cat` command again to verify your I/O scheduler.




## Workload changes that can improve disk performance

Certain workload behaviors can improve the performance of I/O operations on the attached disks.

### Use a high I/O queue depth

Persistent Disks have higher latency than locally attached disks such as Local SSD disks because they are network-attached devices. They can provide very high IOPS and throughput, but you must make sure that sufficient I/O requests are done in parallel. The number of I/O requests done in parallel is referred to as the _I/O queue depth_.

The following tables list the recommended I/O queue depth to ensure you can achieve a certain performance level. The tables use a slight overestimate of typical latency in order to show conservative recommendations. The example assumes that you are using an I/O size of 16 KB.

**Recommended I/O queue depth**

**For SSD, Balanced, and Extreme Persistent Disk:**

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
  
**For standard Persistent Disk:**

**Desired IOPS** | **Queue depth**  
---|---  
200 | 1  
400 | 2  
800 | 4  
1,600 | 8  
3,200 | 16  
6,400 | 32  
12,800 | 64  
15,000 | 75  
**Desired throughput (MB/s)** | **Queue depth**  
---|---  
3.2 | 1  
6.4 | 2  
12.8 | 4  
25.6 | 8  
51.2 | 16  
102.4 | 32  
204.8 | 64  
400 | 125  
  
### Generate enough I/Os using large I/O size

  * **Use large I/O size**

To ensure IOPS limits and latency don't bottleneck your application performance, use a minimum I/O size of 256 KB or higher.

Use large stripe sizes for distributed file system applications. A random I/O workload using large stripe sizes (4 MB or larger) achieves great performance on standard Persistent Disk due to how closely the workload mimics multiple sequential stream disk access.

  * **Make sure your application is generating enough I/O**

Make sure your application is generating enough I/Os to fully use the IOPS and throughput limits of the disk. To better understand your workload I/O pattern, [review disk usage and performance metrics in Cloud Monitoring](https://docs.cloud.google.com/compute/docs/disks/review-disk-metrics).

  * **Make sure there is enough available CPU on the instance that is generating the I/O**

If your compute instance is starved for CPU, your app won't be able to manage the IOPS described earlier. We recommend that you have one available CPU for every 2,000–2,500 IOPS of expected traffic.




### Limit heavy I/O loads to a maximum span

A span refers to a contiguous range of logical block addresses on a single physical disk. Heavy I/O loads achieve maximum performance when limited to a certain maximum span, which depends on the machine type of the compute instance to which the disk is attached, as listed in the following table.

Machine type | Recommended maximum span  
---|---  
  
  * m2-megamem-416
  * C2D VMs

| 25 TB  
All other machine types | 50 TB  
  
Spans on separate Persistent Disks that add up to 50 TB or less can be considered equal to a single 50 TB span for performance purposes.

## Operating system changes to improve disk performance

In some cases, you can enable or disable features at the operating system level, or configure the attached disks in specific ways to improve the disk performance.

### Avoid using `ext3` file systems in Linux

Using the `ext3` file system in a Linux compute instance can result in very poor performance under heavy write loads. Use `ext4` when possible. The `ext4` file system driver is backward compatible with `ext3` and `ext2` and supports mounting `ext3` file systems. The `ext4` file system is the default on most Linux operating systems.

If you can't migrate to `ext4`, as a workaround, you can mount `ext3` file systems with the `data=journal` mount option. This improves write IOPS at the cost of write throughput. Migrating to `ext4` can result in up to a 7x improvement in some benchmarks.

### Disable lazy initialization and enable DISCARD commands

Persistent Disks support discard operations or [`TRIM`](https://wikipedia.org/wiki/Trim_\(computing\)) commands, which allow operating systems to inform the disks when blocks are no longer in use. Discard support allows the operating system to mark disk blocks as no longer needed, without incurring the cost of zeroing out the blocks.

On most Linux operating systems, you enable discard operations when you mount a Persistent Disk on your compute instance. Windows Server 2012 R2 compute instances enable discard operations by default when you mount a Persistent Disk.

Enabling discard operations can boost general runtime performance, and it can also speed up the performance of your disk when it is first mounted. Formatting an entire disk volume can be time consuming, so _lazy formatting_ is a common practice. The downside of lazy formatting is that the cost is often then paid the first time the volume is mounted. By disabling lazy initialization and enabling discard operations, you can get fast format and mount operations.

  * Disable lazy initialization and enable discard operations when formatting a disk by passing the following parameters to [mkfs.ext4](http://linux.die.net/man/8/mkfs.ext4):
        
        -E lazy_itable_init=0,lazy_journal_init=0,discard
        

The `lazy_journal_init=0` parameter does not work on instances with [CentOS 6](https://docs.cloud.google.com/compute/docs/images#centos) or [RHEL 6](https://docs.cloud.google.com/compute/docs/images#rhel) images. For compute instances that use those operating systems, format the Persistent Disk without that parameter.
        
        -E lazy_itable_init=0,discard
        

  * Enable discard operations when mounting a disk by passing the following flag to the `mount` command:
        
        -o discard
        




Persistent Disk works well with the discard operations enabled. However, you can optionally run `fstrim` periodically in addition to, or instead of using discard operations. If you don't use discard operations, run `fstrim` before you create a snapshot of your boot disk. Trimming the file system lets you create smaller snapshot images, which reduces the cost of storing snapshots.

### Adjust the readahead value

To improve I/O performance, operating systems employ techniques such as [readahead](https://wikipedia.org/wiki/Readahead), where more of a file than was requested is read into memory with the assumption that subsequent reads are likely to need that data. Higher readahead increases throughput at the expense of memory and IOPS. Lower readahead increases IOPS at the expense of throughput.

On Linux systems, you can get and set the readahead value with the [blockdev](http://man7.org/linux/man-pages/man8/blockdev.8.html) command:
    
    
    $ sudo blockdev --getra /dev/DEVICE_ID
    
    
    
    $ sudo blockdev --setra VALUE /dev/DEVICE_ID
    

The readahead value is `<desired_readahead_bytes>` / 512 bytes.

For example, for an 8 MB readahead, 8 MB is 8388608 bytes (8 * 1024 * 1024).
    
    
    8388608 bytes / 512 bytes = 16384
    

You set blockdev to `16384`:
    
    
    $ sudo blockdev --setra 16384 /dev/DEVICE_ID
    

### Use a 4 KB sector size for `xfs`

When you format a disk with `xfs`, the default sector size is 512 bytes. To avoid read-modify-write overhead and improve performance, format your disk with a 4 KB sector size:
    
    
    $ sudo mkfs.xfs -s size=4096 /dev/DEVICE_NAME
    

Replace `DEVICE_NAME` with the device name of the disk that you are formatting. For example, `sdb`.

## Modify your compute instance or create a new instance

There are limits associated with each machine type that can impact the performance you can get from the attached disks. These limits include:

  * Persistent Disk performance increases as the number of available vCPUs increases.
  * Hyperdisk aren't supported with all machine types.
  * Network egress rates increase as the number of available vCPUs increases.



### Ensure you have free CPUs

Reading and writing to Persistent Disk volumes requires CPU cycles from your compute instance. To achieve very high, consistent IOPS levels, you must have CPUs free to process I/O.

To increase the number of vCPUs available with your compute instance, you can create a new compute instance, or you can [edit the machine type of a compute instance](https://docs.cloud.google.com/compute/docs/instances/changing-machine-type-of-stopped-instance).

### Consider using Google Cloud Hyperdisk

For higher IOPS and throughput, consider using [Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks) volumes instead of Persistent Disk if your machine series supports Hyperdisk.

To determine if your machine series supports Hyperdisk, see [Machine series support for Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#machine-type-support).

If your instance's machine series supports Hyperdisk, follow these steps to use Hyperdisk volumes:

  1. [Choose a Hyperdisk type](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#when-to-use) that meets your workload's needs.

  2. To switch to the Hyperdisk type you chose, see the instructions in [Change the disk type](https://docs.cloud.google.com/compute/docs/disks/migrate-to-hyperdisk).




### Change the instance's machine series to improve performance

Later generation machine series typically run on newer CPUs, which can offer better performance that their predecessors. Also, newer CPUs can support additional functionality to improve the performance of your workloads, such as [Advanced Matrix Extensions (AMX)](https://docs.cloud.google.com/compute/docs/cpu-platforms#intel-amx) or Intel Advanced Vector Extensions (AVX-512).

## What's next

  * Monitor your disk's performance by [reviewing disk performance metrics](https://docs.cloud.google.com/compute/docs/disks/review-disk-metrics). and [monitoring disk health](https://docs.cloud.google.com/compute/docs/disks/disk-health).
  * Benchmark Persistent Disk volumes attached to: 
    * [Linux instances](https://docs.cloud.google.com/compute/docs/disks/benchmarking-pd-performance-linux).
    * [Windows instances](https://docs.cloud.google.com/compute/docs/disks/benchmarking-pd-performance-windows).
  * Learn about [Persistent Disk pricing](https://docs.cloud.google.com/compute/disks-image-pricing#persistentdisk).
  * Learn how to monitor your disk performance by [reviewing disk performance metrics](https://docs.cloud.google.com/compute/docs/disks/review-disk-metrics).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
