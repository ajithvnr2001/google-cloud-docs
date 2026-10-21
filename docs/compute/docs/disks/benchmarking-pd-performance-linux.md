---
url: https://docs.cloud.google.com/compute/docs/disks/benchmarking-pd-performance-linux/
title: Benchmark Persistent Disk performance on a Linux VM \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T12:57:33.977886+00:00
---

# Benchmark Persistent Disk performance on a Linux VM  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/benchmarking-pd-performance-linux/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Benchmark Persistent Disk performance on a Linux VM Stay organized with collections  Save and categorize content based on your preferences. 

Linux 

This document describes how to benchmark [Persistent Disk performance](https://docs.cloud.google.com/compute/docs/disks/performance) on Linux virtual machines (VMs). For Windows VMs, see [Benchmark persistent disk performance on a Windows VM](https://docs.cloud.google.com/compute/docs/disks/benchmarking-pd-performance-windows).

To benchmark Persistent Disk performance on Linux, use [Flexible I/O tester (FIO)](https://fio.readthedocs.io/) instead of other disk benchmarking tools such as [`dd`](https://en.wikipedia.org/wiki/Dd_\(Unix\)). By default, `dd` uses a very low I/O queue depth, and might not accurately test disk performance. In general, avoid using special devices such as `/dev/urandom`, `/dev/random`, and `/dev/zero` in your Persistent Disk performance benchmarks.

To measure IOPS and throughput of a disk in use on a running instance, benchmark the file system with its intended configuration. Use this option to test a realistic workload without losing the contents of your existing disk. Note that when you benchmark the file system on an existing disk, there are many factors specific to your development environment that may affect benchmarking results, and you may not reach the [disk performance limits](https://docs.cloud.google.com/compute/docs/disks/performance).

To measure the raw performance of a persistent disk, benchmark the block device directly. Use this option to compare raw disk performance to [disk performance limits](https://docs.cloud.google.com/compute/docs/disks/performance#type_comparison).

The following commands work with Debian or Ubuntu operating systems with the `apt` package manager.

### Benchmarking IOPS and throughput of a disk on a running instance

If you want to measure IOPS and throughput for a realistic workload on an active disk on a running instance without losing the contents of your disk, benchmark against a new directory on the existing file system. Each `fio` test runs for five minutes.

  1. [Connect to your instance](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance).

  2. Install dependencies:
         
         sudo apt update
         sudo apt install -y fio
         

  3. In the terminal, list the disks that are attached to your VM and find the disk that you want to test. If your persistent disk is not yet formatted, [format and mount the disk](https://docs.cloud.google.com/compute/docs/disks/format-mount-disk-linux).
         
         sudo lsblk
         
         
         NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
         sda      8:0    0   10G  0 disk
         └─sda1   8:1    0   10G  0 part /
         sdb      8:32   0  2.5T  0 disk /mnt/disks/mnt_dir
         

In this example, we test a 2,500 GB SSD persistent disk with device ID `sdb`.

  4. Create a new directory, `fiotest`, on the disk. In this example, the disk is mounted at `/mnt/disks/mnt_dir`:
         
         TEST_DIR=/mnt/disks/mnt_dir/fiotest
         sudo mkdir -p $TEST_DIR
         

  5. Test write throughput by performing sequential writes with multiple parallel streams (16+), using an I/O block size of 1 MB and an I/O depth of at least 64:
         
         sudo fio --name=write_throughput --directory=$TEST_DIR --numjobs=16 \
         --size=10G --time_based --runtime=5m --ramp_time=2s --ioengine=libaio \
         --direct=1 --verify=0 --bs=1M --iodepth=64 --rw=write \
         --group_reporting=1 --iodepth_batch_submit=64 \
         --iodepth_batch_complete_max=64
         

  6. Test write IOPS by performing random writes, using an I/O block size of 4 KB and an I/O depth of at least 256:
         
         sudo fio --name=write_iops --directory=$TEST_DIR --size=10G \
         --time_based --runtime=5m --ramp_time=2s --ioengine=libaio --direct=1 \
         --verify=0 --bs=4K --iodepth=256 --rw=randwrite --group_reporting=1  \
         --iodepth_batch_submit=256  --iodepth_batch_complete_max=256
         

  7. Test read throughput by performing sequential reads with multiple parallel streams (16+), using an I/O block size of 1 MB and an I/O depth of at least 64:
         
         sudo fio --name=read_throughput --directory=$TEST_DIR --numjobs=16 \
         --size=10G --time_based --runtime=5m --ramp_time=2s --ioengine=libaio \
         --direct=1 --verify=0 --bs=1M --iodepth=64 --rw=read \
         --group_reporting=1 \
         --iodepth_batch_submit=64 --iodepth_batch_complete_max=64
         

  8. Test read IOPS by performing random reads, using an I/O block size of 4 KB and an I/O depth of at least 256:
         
         sudo fio --name=read_iops --directory=$TEST_DIR --size=10G \
         --time_based --runtime=5m --ramp_time=2s --ioengine=libaio --direct=1 \
         --verify=0 --bs=4K --iodepth=256 --rw=randread --group_reporting=1 \
         --iodepth_batch_submit=256  --iodepth_batch_complete_max=256
         

  9. Clean up:
         
         sudo rm $TEST_DIR/write* $TEST_DIR/read*
         




### Benchmarking raw persistent disk performance

If you want to measure the performance of persistent disks alone outside of your development environment, test read and write performance for a block device on a throwaway persistent disk and VM. Each `fio` test runs for five minutes. The following commands assume a 2,500 GB SSD persistent disk attached to your VM. If your device size is different, modify the value of the `--filesize` argument. This disk size is necessary to achieve the 32 vCPU VM throughput limits. For more information, see [Block storage performance](https://docs.cloud.google.com/compute/docs/disks/performance).

**Warning:** The commands in this section overwrite the contents of /dev/sdb. _We strongly recommend using a throwaway VM and disk_.

  1. [Create and start a VM instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).

  2. [Add a Persistent Disk to your VM instance](https://docs.cloud.google.com/compute/docs/disks/add-persistent-disk) which you intend to benchmark.

  3. [Connect to your instance](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance).

  4. Install dependencies:
         
         sudo apt-get update
         sudo apt-get install -y fio
         

  5. Fill the disk with nonzero data. Persistent disk reads from empty blocks have a latency profile that is different from blocks that contain data. We recommend filling the disk before running any read latency benchmarks.
         
         # Running this command causes data loss on the second device.
         # We strongly recommend using a throwaway VM and disk.
         sudo fio --name=fill_disk \
           --filename=/dev/sdb --filesize=2500G \
           --ioengine=libaio --direct=1 --verify=0 --randrepeat=0 \
           --bs=128K --iodepth=64 --rw=randwrite \
           --iodepth_batch_submit=64 --iodepth_batch_complete_max=64
         

  6. Test write bandwidth by performing sequential writes with multiple parallel streams (16+), using 1 MB as the I/O size and having an I/O depth that is greater than or equal to 64.
         
         # Running this command causes data loss on the second device.
         # We strongly recommend using a throwaway VM and disk.
         sudo fio --name=write_bandwidth_test \
           --filename=/dev/sdb --filesize=2500G \
           --time_based --ramp_time=2s --runtime=5m \
           --ioengine=libaio --direct=1 --verify=0 --randrepeat=0 \
           --bs=1M --iodepth=64 --iodepth_batch_submit=64 --iodepth_batch_complete_max=64 \
           --rw=write --numjobs=16 --offset_increment=100G
         

  7. Test write IOPS. To achieve maximum PD IOPS, you must maintain a deep I/O queue. If, for example, the write latency is 1 millisecond, the VM can achieve, at most, 1,000 IOPS for each I/O in flight. To achieve 15,000 write IOPS, the VM must maintain at least 15 I/Os in flight. If your disk and VM are able to achieve 30,000 write IOPS, the number of I/Os in flight must be at least 30 I/Os. If the I/O size is larger than 4 KB, the VM might reach the bandwidth limit before it reaches the IOPS limit.
         
         # Running this command causes data loss on the second device.
         # We strongly recommend using a throwaway VM and disk.
         sudo fio --name=write_iops_test \
           --filename=/dev/sdb --filesize=2500G \
           --time_based --ramp_time=2s --runtime=5m \
           --ioengine=libaio --direct=1 --verify=0 --randrepeat=0 \
           --bs=4K --iodepth=256 --rw=randwrite \
           --iodepth_batch_submit=256 --iodepth_batch_complete_max=256
         

  8. Test write latency. While testing I/O latency, the VM must not reach maximum bandwidth or IOPS; otherwise, the observed latency won't reflect actual persistent disk I/O latency. For example, if the IOPS limit is reached at an I/O depth of 30 and the `fio` command has double that, then the total IOPS remains the same and the reported I/O latency doubles.
         
         # Running this command causes data loss on the second device.
         # We strongly recommend using a throwaway VM and disk.
         sudo fio --name=write_latency_test \
           --filename=/dev/sdb --filesize=2500G \
           --time_based --ramp_time=2s --runtime=5m \
           --ioengine=libaio --direct=1 --verify=0 --randrepeat=0 \
           --bs=4K --iodepth=4 --rw=randwrite --iodepth_batch_submit=4 \
           --iodepth_batch_complete_max=4
         

  9. Test read bandwidth by performing sequential reads with multiple parallel streams (16+), using 1 MB as the I/O size and having an I/O depth that is equal to 64 or greater.
         
         sudo fio --name=read_bandwidth_test \
           --filename=/dev/sdb --filesize=2500G \
           --time_based --ramp_time=2s --runtime=5m \
           --ioengine=libaio --direct=1 --verify=0 --randrepeat=0 \
           --bs=1M --iodepth=64 --rw=read --numjobs=16 --offset_increment=100G \
           --iodepth_batch_submit=64 --iodepth_batch_complete_max=64
         

  10. Test read IOPS. To achieve the maximum PD IOPS, you must maintain a deep I/O queue. If, for example, the I/O size is larger than 4 KB, the VM might reach the bandwidth limit before it reaches the IOPS limit. To achieve the maximum 100k read IOPS, specify `--iodepth=256` for this test.
         
         sudo fio --name=read_iops_test \
           --filename=/dev/sdb --filesize=2500G \
           --time_based --ramp_time=2s --runtime=5m \
           --ioengine=libaio --direct=1 --verify=0 --randrepeat=0 \
           --bs=4K --iodepth=256 --rw=randread \
           --iodepth_batch_submit=256 --iodepth_batch_complete_max=256
         

  11. Test read latency. It's important to fill the disk with data to get a realistic latency measurement. It's important that the VM not reach IOPS or throughput limits during this test because after the persistent disk reaches its saturation limit, it pushes back on incoming I/Os and this is reflected as an artificial increase in I/O latency.
         
         sudo fio --name=read_latency_test \
           --filename=/dev/sdb --filesize=2500G \
           --time_based --ramp_time=2s --runtime=5m \
           --ioengine=libaio --direct=1 --verify=0 --randrepeat=0 \
           --bs=4K --iodepth=4 --rw=randread \
           --iodepth_batch_submit=4 --iodepth_batch_complete_max=4
         

  12. Test sequential read bandwidth.
         
         sudo fio --name=read_bandwidth_test \
           --filename=/dev/sdb --filesize=2500G \
           --time_based --ramp_time=2s --runtime=5m \
           --ioengine=libaio --direct=1 --verify=0 --randrepeat=0 \
           --numjobs=4 --thread --offset_increment=500G \
           --bs=1M --iodepth=64 --rw=read \
           --iodepth_batch_submit=64  --iodepth_batch_complete_max=64
         

  13. Test sequential write bandwidth.
         
         sudo fio --name=write_bandwidth_test \
           --filename=/dev/sdb --filesize=2500G \
           --time_based --ramp_time=2s --runtime=5m \
           --ioengine=libaio --direct=1 --verify=0 --randrepeat=0 \
           --numjobs=4 --thread --offset_increment=500G \
           --bs=1M --iodepth=64 --rw=write \
           --iodepth_batch_submit=64  --iodepth_batch_complete_max=64
         

  14. Clean up the throwaway Persistent Disk and VM:

     1. [Delete the disk](https://docs.cloud.google.com/compute/docs/samples/compute-disk-delete) used for benchmarking performance.
     2. [Delete the VM](https://docs.cloud.google.com/compute/docs/instances/deleting-instance) created for benchmarking performance.



## What's next

  * Learn how to monitor your disk performance by [reviewing disk performance metrics](https://docs.cloud.google.com/compute/docs/disks/review-disk-metrics).
  * Learn about [Persistent Disk pricing](https://docs.cloud.google.com/compute/disks-image-pricing#persistentdisk).
  * Learn how to [optimize Persistent Disk performance](https://docs.cloud.google.com/compute/docs/disks/optimizing-pd-performance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
