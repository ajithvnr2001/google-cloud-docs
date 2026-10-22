---
url: https://docs.cloud.google.com/compute/docs/disks/benchmarking-pd-performance-windows/
title: Benchmark Persistent Disk performance on a Windows VM \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:18.234700+00:00
---

# Benchmark Persistent Disk performance on a Windows VM  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/benchmarking-pd-performance-windows/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Benchmark Persistent Disk performance on a Windows VM Stay organized with collections  Save and categorize content based on your preferences. 

Windows 

This document describes how to benchmark [Persistent Disk performance](https://docs.cloud.google.com/compute/docs/disks/performance) on Windows virtual machine (VM) instances. For Linux VMs, see [benchmark Persistent Disk performance on a Linux VM](https://docs.cloud.google.com/compute/docs/disks/benchmarking-pd-performance-linux).

To measure IOPS and throughput of a disk in use on a running instance, benchmark the file system with its intended configuration. Use this option to test a realistic workload without losing the contents of your existing disk. Note that when you benchmark the file system on an existing disk, there are many factors specific to your development environment that may affect benchmarking results, and you may not reach the [disk performance limits](https://docs.cloud.google.com/compute/docs/disks/performance#machine-type-disk-limits).

To measure the raw performance of a Persistent Disk, benchmark the block device directly. Use this option to compare raw disk performance to disk performance limits.

On [C4 VMs](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4_series), Windows supports a maximum depth of 1024 per device submission queue. When a queue fills, Windows stops submitting I/O until the queue has partially drained, which significantly reduces performance. To avoid triggering this condition, we recommend limiting your benchmarking workloads to an aggregate queue depth of 1024 per attached volume.

### Configure benchmarking software

To benchmark Persistent Disk performance on Windows VMs, use [`DISKSPD`](https://github.com/microsoft/diskspd).

  1. [Connect to your VM instance](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows).

  2. Open Powershell and download the `DISKSPD` tool using the following command:
         
         $client = New-Object System.Net.WebClient
         $client.DownloadFile("https://github.com/Microsoft/diskspd/releases/latest/download/DiskSpd.zip","$env:temp\DiskSpd-download.zip")
         Expand-Archive -LiteralPath "$env:temp\DiskSpd-download.zip" C:\DISKSPD
         Get-ChildItem C:\DISKSPD
         

**Note:** You can also download the latest version of the `DISKSPD` tool directly from [GitHub](https://github.com/Microsoft/diskspd/releases/latest/download/DiskSpd.zip) and extract it manually.



### Benchmark IOPS and throughput of a disk on a running VM instance

To measure IOPS and throughput for a realistic workload on an active disk on a running VM instance without losing the contents of your disk, benchmark against a new directory on the existing file system.

In the following steps assume the disk to test is mounted as `D:` and the commands are executed in a **Command Prompt** (cmd.exe) window that has administrator privileges:

  1. [Connect to your VM](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows).

  2. Verify `DISKSPD` software configuration and change directory to the 64-bit binary:

**Note:** The following command assumes `DISKSPD` was installed at `C:\DISKSPD`.
         
         cd C:\DISKSPD\amd64
         

  3. Create a new 10 GB file named `DISKTEST.DAT` on the disk:
         
         set TESTFILE=D:\DISKTEST.DAT
         diskspd -d0 -c10G %TESTFILE%
         

  4. Test write throughput by performing sequential writes with multiple parallel streams (16 or more), using an I/O block size of 1 MB and an I/O depth of at least 64:
         
         diskspd -d300 -b1M -o64 -Sh -w100 -t16 -si %TESTFILE%
         

  5. Test write IOPS by performing random writes, using an I/O block size of 4 KB and an I/O depth of at least 256:
         
         diskspd -d300 -b4K -o256 -Sh -w100 -r %TESTFILE%
         

  6. Test read throughput by performing sequential reads with multiple parallel streams (16 or more), using an I/O block size of 1 MB and an I/O depth of at least 64:
         
         diskspd -d300 -b1M -o64 -Sh -t16 -si %TESTFILE%
         

  7. Test read IOPS by performing random reads, using an I/O block size of 4 KB and an I/O depth of at least 256:
         
         diskspd -d300 -b4K -o256 -Sh -r %TESTFILE%
         

  8. Clean up:
         
         del %TESTFILE%
         




### Benchmarking raw Persistent Disk performance

To measure the performance of Persistent Disk volumes alone outside of your development environment, test read and write performance for a block device on a throwaway Persistent Disk and VM.

**Warning:** The commands in this section overwrite the contents of your disk. **We strongly recommend using a throwaway VM and disk**.

  1. [Create and start a VM instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).

  2. [Add a Persistent Disk to the VM instance](https://docs.cloud.google.com/compute/docs/disks/add-persistent-disk) that you intend to benchmark.

  3. [Connect to your VM instance](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows).

  4. Verify `DISKSPD` software configuration and change directory to the 64-bit binary:

**Note:** The following command assumes DISKSPD was installed at C:\DISKSPD.
         
         cd C:\DISKSPD\amd64
         

  5. Verify that there are no non-reserved partitions on the disk. Enter `diskpart` into an elevated **Command Prompt** window.
         
         diskpart
         

  6. List the disks attached to the VM:
         
         DISKPART> list disk
         

The output shows the newly created 1 TB disk which is Disk 1 in the following example output:
         
         Disk ###  Status         Size     Free     Dyn  Gpt
           --------  -------------  -------  -------  ---  ---
           Disk 0    Online          120 GB  1024 KB        *
           Disk 1    Online         1024 GB  1023 GB        *
         

  7. Select the disk that you intend to benchmark.
         
         DISKPART> select disk 1
         

  8. List the partitions on the selected disk.
         
         DISKPART> list partition
         
         
         Partition ###  Type              Size       Offset
            -------------  ----------------  --------   -------
            Partition 1    Reserved              15 MB    17 KB
            Partition 2    Primary             1024 GB    16 MB
         

  9. Select the primary partition 2:
         
         DISKPART> select partition 2
         

  10. Delete the selected partition:
         
         DISKPART> delete partition
         

**Warning:** This step will cause permanent loss of data.
  11. Exit diskpart
         
         DISKPART> exit
         




The preceding steps should be repeated if the disk you intend to benchmark has any other partitions apart from the Reserved partition. When only the Reserved partition remains, continue with the following steps:

  1. After you've identified the disk and verified that there are no partitions, set the `TESTDRIVE` environment variable to '#' followed by the number of the disk to test.
         
         C:/> set TESTDRIVE=#1
         

  2. Test write throughput by performing sequential writes with multiple parallel streams (16 or more), using an I/O block size of 1 MB and an I/O depth of at least 64:
         
         diskspd -d300 -b1M -o64 -Sh -t16 -si -w0 %TESTDRIVE%
         

  3. Test write IOPS by performing random writes, using an I/O block size of 4 KB and an I/O depth of at least 256:
         
         diskspd -d300 -b4K -o256 -Sh -r -w0 %TESTDRIVE%
         

  4. Test write latency. While testing I/O latency, the VM must not reach maximum bandwidth or IOPS; otherwise, the observed latency won't reflect the actual Persistent Disk I/O latency.
         
         diskspd -d300 -b4K -o4 -Sh -r -w0 -L %TESTDRIVE%
         

  5. Test read throughput by performing sequential reads with multiple parallel streams (16 or more), using an I/O block size of 1 MB and an I/O depth of at least 64:
         
         diskspd -d300 -b1M -o64 -Sh -t16 -si %TESTDRIVE%
         

  6. Test read IOPS by performing random reads, using an I/O block size of 4 KB and an I/O depth of at least 256:
         
         diskspd -d300 -b4K -o256 -Sh -r %TESTDRIVE%
         

  7. To test read latency, it's important to fill the disk with data to get a realistic latency measurement. The VM must not reach IOPS or throughput limits during this test because after the Persistent Disk reaches its saturation limit, it pushes back on incoming I/O operations, and this is reflected as an artificial increase in I/O latency.
         
         diskspd -d300 -b4K -o4 -Sh -r -L %TESTDRIVE%
         

  8. Test sequential read bandwidth.
         
         diskspd -d300 -b1M -o64 -Sh -t4 -si %TESTDRIVE%
         

  9. Test sequential write bandwidth.
         
         diskspd -d300 -b1M -o64 -Sh -t4 -si -w100 %TESTDRIVE%
         

  10. Clean up the throwaway Persistent Disk and VM:

     1. [Delete the disk](https://docs.cloud.google.com/compute/docs/samples/compute-disk-delete) used for benchmarking performance.
     2. [Delete the VM](https://docs.cloud.google.com/compute/docs/instances/deleting-instance) created for benchmarking performance.



## What's next

  * Learn how to monitor your disk performance by [reviewing persistent disk performance metrics](https://docs.cloud.google.com/compute/docs/disks/review-disk-metrics).
  * Learn about [Persistent Disk pricing](https://docs.cloud.google.com/compute/disks-image-pricing#persistentdisk).
  * Learn how to [optimize Persistent Disk performance](https://docs.cloud.google.com/compute/docs/disks/optimizing-pd-performance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
