---
url: https://docs.cloud.google.com/netapp/volumes/docs/performance/performance-benchmarks/
title: Performance benchmarks \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:16:51.606450+00:00
---

# Performance benchmarks  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/performance/performance-benchmarks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Performance benchmarks Stay organized with collections  Save and categorize content based on your preferences. 

This page shows the performance limits of a single Google Cloud NetApp Volumes volume from multiple client virtual machines. Use the information on this page to size your workloads.

## Performance testing

The following test results display performance limits. In these tests, the volume has sufficient capacity so that the throughput doesn't affect benchmark testing. Allocating a single volume's capacity beyond the following throughput numbers doesn't yield additional performance gains.

Note that performance testing was completed using Fio.

For the performance testing results, be aware of the following considerations:

  * Standard, Premium, and Extreme service level performance scales throughput with volume capacity until limits are reached. All Flex service levels scale with the capabilities of the storage pool and all volumes in a pool share the pool's performance.

  * The Flex Unified and Flex File service level with custom performance provides independent scaling of capacity, IOPS, and throughput.

  * IOPS results are purely informational.

  * The numbers used to produce the following results are set up to show maximum results. The following results should be considered an estimate of the maximum achievable throughput capacity assignment.

  * Using multiple fast volumes per project may be subject to per project limits.

  * The following performance testing results cover only NFSv3, SMB, and iSCSI protocols. Other protocol types such as NFSv4.1 were not used to test NetApp Volumes performance.




## Volume throughput limits for NFSv3 access

The following sections provide details on volume throughput limits for NFSv3 access.

### Flex File service level with custom performance

The following tests were run with a single volume in a Flex custom performance zonal storage pool. The pool was configured with the maximum throughput and IOPS, and the results were captured.

#### 64 KiB block size (Sequential I/O)

These results were captured using Fio with the following settings:

  * 64 KiB block size against a single volume with six `n2-standard-32` virtual machines

  * Red Hat 9 OS

  * 96 GiB working set for each virtual machine with a combined total of 576 GiB

  * `nconnect` mount option configured on each host for a value of 16

  * `rsize` and `wsize` mount options configured at 65536

  * Volume size was 10 TiB of the Flex service level with custom performance. For testing, the custom performance was set to its maximum values of 5,120 MiBps and 160,000 IOPS.




Fio was run with 8 jobs on each virtual machine for a total of 48 jobs. The following table demonstrates that a single volume is estimated to be capable of handling approximately 4,300 MiBps of pure sequential reads and 1,480 MiBps of pure sequential writes with a 64 KiB block size over NFSv3.

##### Benchmark results for NFS 64 KiB Sequential 6 `n2-standard-32` Red Hat 9 VMs

| 100% Read and 0% Write | 75% Read and 25% Write | 50% Read and 50% Write | 25% Read and 75% Write | 0% Read and 100% Write  
---|---|---|---|---|---  
Read MiBps | 4,304 | 2,963 | 1,345 | 464 | 0  
Write MiBps | 0 | 989 | 1,344 | 1,390 | 1,476  
  
#### 8 KiB block size (Random I/O)

These results were captured using Fio with the following settings:

  * 8 KiB block size against a single volume with six `n2-standard-32` virtual machines

  * Red Hat 9 OS

  * 96 GiB working set for each virtual machine with a combined total of 576 GiB

  * `nconnect` mount option configured on each host for a value of 16

  * `rsize` and `wsize` mount options on each host configured at 65536

  * Volume size was 10 TiB of the Flex service level with custom performance. For testing, the custom performance was set to its maximum values of 5,120 MiBps and 160,000 IOPS.




Fio was run with 8 jobs on each virtual machine for a total of 48 jobs. The following table demonstrates that a single volume is estimated to be capable of handling approximately 126,400 pure random read IOPS and 78,600 of pure random write IOPS with an 8 KiB block size over NFSv3.

##### Benchmark results for NFS 8 KiB Random 6 `n2-standard-32` Red Hat 9 VMs

| 100% Read and 0% Write | 75% Read and 25% Write | 50% Read and 50% Write | 25% Read and 75% Write | 0% Read and 100% Write  
---|---|---|---|---|---  
Read IOPS | 126,397 | 101,740 | 57,223 | 23,600 | 0  
Write IOPS | 0 | 33,916 | 57,217 | 70,751 | 78,582  
  
### Extreme service level

The following tests were run with a single volume in an Extreme storage pool and results were captured.

#### 64 KiB block size (Sequential I/O)

These results were captured using Fio with the following settings:

  * 64 KiB block size against a single volume with six `n2-standard-32` virtual machines

  * Red Hat 9 OS

  * 1 TiB working set for each virtual machine with a combined total of 6 TiB

  * `nconnect` mount option configured on each host for a value of 16

  * Volume size was 75 TiB of the Extreme service level




Fio was run with 8 jobs on each virtual machine for a total of 48 jobs. The following table demonstrates that a single volume is estimated to be capable of handling between around 5,240 MiBps of pure sequential reads and around 2,180 MiBps of pure sequential writes with a 64 KiB block size over NFSv3.

##### Benchmark results for NFS 64 KiB Sequential 6 `n2-standard-32` Red Hat 9 VMs

| 100% Read and 0% Write | 75% Read and 25% Write | 50% Read and 50% Write | 25% Read and 75% Write | 0% Read and 100% Write  
---|---|---|---|---|---  
Read MiBps | 5,237 | 2,284 | 1,415 | 610 | 0  
Write MiBps | 0 | 764 | 1,416 | 1,835 | 2,172  
  
#### 256 KiB block size (Sequential I/O)

These results were captured using Fio with the following settings:

  * 256 KiB block size against a single volume with six `n2-standard-32` virtual machines

  * Red Hat 9 OS

  * 1 TiB working set for each virtual machine with a combined total of 6 TiB

  * `nconnect` mount option configured on each host for a value of 16

  * Volume size was 75 TiB of the Extreme service level




Fio was run with 8 jobs on each virtual machine for a total of 48 jobs. The following table demonstrates that a single volume is estimated to be capable of handling between around 4,930 MiBps of pure sequential reads and around 2,440 MiBps of pure sequential writes with a 256 KiB block size over NFSv3.

##### Benchmark results for NFS 256 KiB Sequential 6 `n2-standard-32` Red Hat 9 VMs

| 100% Read and 0% Write | 75% Read and 25% Write | 50% Read and 50% Write | 25% Read and 75% Write | 0% Read and 100% Write  
---|---|---|---|---|---  
Read MiBps | 4,928 | 2,522 | 1,638 | 677 | 0  
Write MiBps | 0 | 839 | 1,640 | 2,036 | 2,440  
  
#### 4 KiB block size (Random I/O)

These results were captured using Fio with the following settings:

  * 4 KiB block size against a single volume with six `n2-standard-32` virtual machines

  * Red Hat 9 OS

  * 1 TiB working set for each virtual machine with a combined total of 6 TiB

  * `nconnect` mount option configured on each host for a value of 16

  * Volume size was 75 TiB of the Extreme service level




Fio was run with 8 jobs on each virtual machine for a total of 48 jobs. The following table demonstrates that a single volume is estimated to be capable of handling between ~380,000 pure random read IOPS and around 120,000 pure random write IOPS with a 4 KiB block size over NFSv3.

##### Benchmark results for NFS 4 KiB Random 6 `n2-standard-32` Red Hat 9 VMs

| 100% Read and 0% Write | 75% Read and 25% Write | 50% Read and 50% Write | 25% Read and 75% Write | 0% Read and 100% Write  
---|---|---|---|---|---  
Read IOPS | 380,000 | 172,000 | 79,800 | 32,000 | 0  
Write IOPS | 0 | 57,300 | 79,800 | 96,200 | 118,000  
  
#### 8 KiB block size (Random I/O)

These results were captured using Fio with the following settings:

  * 8 KiB block size against a single volume with six `n2-standard-32` virtual machines

  * Red Hat 9 OS

  * 1 TiB working set for each virtual machine with a combined total of 6 TiB

  * `nconnect` mount option configured on each host for a value of 16

  * Volume size was 75 TiB of the Extreme service level




Fio was run with 8 jobs on each virtual machine for a total of 48 jobs. The following table demonstrates that a single volume is estimated to be capable of handling between ~270,000 pure random read IOPS and ~110,000 pure random write IOPS with an 8 KiB block size over NFSv3.

##### Benchmark results for NFS 8 KiB Random 6 `n2-standard-32` Red Hat 9 VMs

| 100% Read and 0% Write | 75% Read and 25% Write | 50% Read and 50% Write | 25% Read and 75% Write | 0% Read and 100% Write  
---|---|---|---|---|---  
Read IOPS | 265,000 | 132,000 | 66,900 | 30,200 | 0  
Write IOPS | 0 | 44,100 | 66,900 | 90,500 | 104,000  
  
## Volume throughput limits for SMB access

The following sections provide details for volume throughput limits for SMB access.

### 64 KiB block size (Sequential I/O)

These results were captured using Fio with the following settings:

  * 64 KiB block size against a single volume with six `n2-standard-32` virtual machines

  * Windows 2022 OS

  * 1 TiB working set for each virtual machine with a combined total of 6 TiB

  * SMB Connect Count Per RSS Network Interface client-side option configured on each virtual machine for a value of 16

  * Volume size was 75 TiB of the Extreme service level




Fio was run with 8 jobs on each virtual machine for a total of 48 jobs. The following table demonstrates that a single volume is estimated to be capable of handling between ~5,130 MiBps of pure sequential reads and ~1,790 MiBps of pure sequential writes with a 64 KiB block size over SMB.

#### SMB 64 KiB Sequential 6 `n2-standard-32` Windows 2022 VMs

| 100% Read and 0% Write | 75% Read and 25% Write | 50% Read and 50% Write | 25% Read and 75% Write | 0% Read and 100% Write  
---|---|---|---|---|---  
Read MiBps | 5,128 | 2,675 | 1,455 | 559 | 0  
Write MiBps | 0 | 892 | 1,454 | 1,676 | 1,781  
  
### 256 KiB block size (Sequential I/O)

These results were captured using Fio with the following settings:

  * 256 KiB block size against a single volume with six n2-standard-32 virtual machines

  * Windows 2022 OS

  * 1 TiB working set for each virtual machine with a combined total of 6 TiB

  * SMB Connection Count Per RSS Network Interface client-side option configured on each host for a value of 16

  * Volume size was 75 TiB of the Extreme service level




Fio was run with 8 jobs on each virtual machine for a total of 48 jobs. The following table demonstrates that a single volume is estimated to be capable of handling between ~4,620 MiBps of pure sequential reads and ~1,830 MiBps of pure sequential writes with a 256 KiB block size over SMB.

#### SMB 256 KiB Sequential 6 `n2-standard-32` Windows 2022 VMs

| 100% Read and 0% Write | 75% Read and 25% Write | 50% Read and 50% Write | 25% Read and 75% Write | 0% Read and 100% Write  
---|---|---|---|---|---  
Read MiBps | 4,617 | 2,708 | 1,533 | 584 | 0  
Write MiBps | 0 | 900 | 1,534 | 1,744 | 1,826  
  
### 4 KiB block size (Random I/O)

These results were captured using Fio with the following settings:

  * 4 KiB block size against a single volume with six `n2-standard-32` virtual machines

  * Windows 2022 OS

  * 1 TiB working set for each virtual machine for a combined total of 6 TiB

  * SMB Connection Count Per RSS Network Interface client-side option enabled on each host for a value of 16

  * Volume size was 75 TiB of the Extreme service level




Fio was run with 8 jobs on each virtual machine for a total of 48 jobs. The following table demonstrates that a single volume is estimated to be capable of handling between ~390,000 pure random read IOPS and ~110,000 pure random write IOPS with a 4 KiB block size over SMB.

#### Benchmark results for SMB 4 KiB Random 6 `n2-standard-32` Windows 2022 VMs

| 100% Read and 0% Write | 75% Read and 25% Write | 50% Read and 50% Write | 25% Read and 75% Write | 0% Read and 100% Write  
---|---|---|---|---|---  
Read IOPS | 390,900 | 164,700 | 84,200 | 32,822 | 0  
Write IOPS | 0 | 54,848 | 84,200 | 98,500 | 109,300  
  
### 8 KiB block size (Random I/O)

These results were captured using Fio with the following settings:

  * 8 KiB block size against a single volume with six `n2-standard-32` virtual machines

  * Windows 2022 OS

  * 1 TiB working set for each virtual machine for a combined total of 6 TiB

  * SMB Connection Count Per RSS Network Interface client-side option configured on each host for the value of 16

  * Volume size was 75 TiB of the Extreme service level




Fio was run with 8 jobs on each virtual machine for a total of 48 jobs. The following table demonstrates that a single volume is estimated to be capable of handling between ~280,000 pure random read IOPS and ~90,000 pure random write IOPS with an 8 KiB block size over SMB.

#### Benchmark results for SMB 8 KiB Random 6 `n2-standard-32` Windows 2022 VMs

| 100% Read and 0% Write | 75% Read and 25% Write | 50% Read and 50% Write | 25% Read and 75% Write | 0% Read and 100% Write  
---|---|---|---|---|---  
Read IOPS | 271,800 | 135,900 | 65,700 | 28,093 | 0  
Write IOPS | 0 | 45,293 | 65,900 | 84,400 | 85,500  
  
## Volume throughput limits for iSCSI access

The following sections describe volume throughput limits for iSCSI access with the Flex Unified service level.

The following tests were run with six 1 TiB volumes in a Flex Unified custom performance regional storage pool. The pool was configured with the maximum throughput and IOPS, and the results were captured.

### 64 KiB block size (Sequential I/O)

These results were captured using Fio with the following settings:

  * 64 KiB block size for 6 volumes with 6 `n2-standard-32` virtual machines

  * Red Hat Enterprise Linux (RHEL) 9 OS

  * 720 GiB working set for each virtual machine, with a combined total of 4,320 GiB

  * iSCSI with the `nr_sessions` parameter on each host set to 16

  * Each volume size is 1 TiB from a storage pool of 10 TiB capacity




Fio was run with 24 jobs on each virtual machine with `iodepth` set to 1. The following table demonstrates that a storage pool is estimated to be capable of handling between ~4,915 MiBps of pure sequential reads and ~2,375 MiBps of pure sequential writes with a 64 KiB block size over iSCSI.

#### iSCSI 64 KiB Sequential 6 `n2-standard-32` RHEL 9 VMs

| 100% Read and 0% Write | 75% Read and 25% Write | 50% Read and 50% Write | 25% Read and 75% Write | 0% Read and 100% Write  
---|---|---|---|---|---  
Read MiBps | 4,915 | 3,642 | 1,846 | 701 | 0  
Write MiBps | 0 | 1,214 | 1,844 | 2,104 | 2,375  
  
### 256 KiB block size (Sequential I/O)

These results were captured using Fio with the following settings:

  * 256 KiB block size for 6 volumes with 6 `n2-standard-32` virtual machines

  * RHEL 9 OS

  * 720 GiB working set for each virtual machine, with a combined total of 4,320 GiB

  * iSCSI with the `nr_sessions` parameter on each host set to 16

  * Each volume size is 1 TiB from a storage pool of 10 TiB capacity




Fio was run with 24 jobs on each virtual machine with `iodepth` set to 1. The following table demonstrates that a storage pool is estimated to be capable of handling between ~4,954 MiBps of pure sequential reads and ~2,648 MiBps of pure sequential writes with a 256 KiB block size over iSCSI.

#### iSCSI 256 KiB Sequential 6 `n2-standard-32` RHEL 9 VMs

| 100% Read and 0% Write | 75% Read and 25% Write | 50% Read and 50% Write | 25% Read and 75% Write | 0% Read and 100% Write  
---|---|---|---|---|---  
Read MiBps | 4,954 | 3,774 | 2,387 | 859 | 0  
Write MiBps | 0 | 1,259 | 2,389 | 2,574 | 2,648  
  
### 4 KiB block size (Random I/O)

These results were captured using Fio with the following settings:

  * 4 KiB block size for 6 volumes with 6 `n2-standard-32` virtual machines

  * RHEL 9 OS

  * 720 GiB working set for each virtual machine, with a combined total of 4,320 GiB

  * iSCSI with the `nr_sessions` parameter on each host set to 16

  * Each volume size is 1 TiB from a storage pool of 10 TiB capacity




Fio was run with 24 jobs on each virtual machine with `iodepth` set to 4. The following table demonstrates that a storage pool is estimated to be capable of handling between ~160,000 pure random read IOPS and ~160,000 pure random write IOPS with a 4 KiB block size over iSCSI.

#### iSCSI 4 KiB Random 6 `n2-standard-32` RHEL 9 VMs

| 100% Read and 0% Write | 75% Read and 25% Write | 50% Read and 50% Write | 25% Read and 75% Write | 0% Read and 100% Write  
---|---|---|---|---|---  
Read IOPS | 159,861 | 120,061 | 80,047 | 40,027 | 0  
Write IOPS | 0 | 40,031 | 80,056 | 120,060 | 160,072  
  
### 8 KiB block size (Random I/O)

These results were captured using Fio with the following settings:

  * 8 KiB block size for 6 volumes with 6 `n2-standard-32` virtual machines

  * RHEL 9 OS

  * 720 GiB working set for each virtual machine, with a combined total of 4,320 GiB

  * iSCSI with the `nr_sessions` parameter on each host set to 16

  * Each volume size is 1 TiB from a storage pool of 10 TiB capacity




Fio was run with 24 jobs on each virtual machine with `iodepth` set to 4. The following table demonstrates that a storage pool is estimated to be capable of handling between ~158,000 pure random read IOPS and ~140,400 pure random write IOPS with an 8 KiB block size over iSCSI.

#### iSCSI 8 KiB Random 6 `n2-standard-32` RHEL 9 VMs

| 100% Read and 0% Write | 75% Read and 25% Write | 50% Read and 50% Write | 25% Read and 75% Write | 0% Read and 100% Write  
---|---|---|---|---|---  
Read IOPS | 157,780 | 120,028 | 80,102 | 39,866 | 0  
Write IOPS | 0 | 40,035 | 80,070 | 119,565 | 140,366  
  
## Database workload benchmarks

This section provides application-level database benchmark results for Oracle and Microsoft SQL Server workloads over iSCSI on NetApp Volumes. These real-world measurements supplement the synthetic storage benchmark data.

### Considerations

Consider the following factors when reviewing these database benchmark results:

  * The database benchmark results represent measurements under specific testing conditions.

  * Real-world performance varies based on workload characteristics and configurations such as host sizing, network, database, iSCSI, multipath, and deployment architecture.




### Oracle database

The following tests ran on an Oracle Database 23c using the Silly Little Oracle Benchmark (SLOB) tool over iSCSI and to capture performance results for analysis.

Workload profile | Storage IOPS | Latency  
---|---|---  
100% Read | ~157,000 | 0.40 ms  
90% Read and 10% Write | ~145,000 | 0.38 ms  
  
Storage IOPS values represent backend storage I/O observed during testing. Total storage IOPS is calculated as the sum of read and write IOPS for the 90% read and 10% write workload.

For more information, see [Oracle performance on Google Cloud NetApp Volumes over iSCSI](https://community.netapp.com/community/discussion/467905/oracle-performance-on-google-cloud-netapp-volumes-over-iscsi/p1).

### Microsoft SQL Server

The following tests ran on Microsoft SQL Server workloads using the SQL storage benchmark (SSB) tool over iSCSI with single LUN configurations and to capture performance results for analysis.

Workload profile | Storage IOPS | Latency  
---|---|---  
100% Read | ~140,000 | <1 ms  
80% Read and 20% Write | ~100,000 | <1 ms  
  
These performance values represent sustained storage performance at low-latency operating points. Total storage IOPS is calculated as the sum of read and write IOPS for the 80% read and 20% write workload.

## Electronic design automation workload benchmarks

NetApp Volumes large volume support offers high-performance parallel file systems that are ideal for electronic design automation workloads. These file systems provide up to 1 PiB of capacity and deliver high I/O and throughput rates at low latency.

Electronic design automation workloads have different performance requirements between the frontend and backend phases. The frontend phase prioritizes metadata and IOPS, while the backend phase focuses on throughput.

An industry-standard electronic design automation benchmark with mixed frontend and backend workloads, using a large volume with multiple NFSv3 clients that are evenly distributed over 6 IP addresses, can achieve up to 21.5 GiBps throughput and up to 1,350,000 IOPS.

## What's next

[Monitor performance](https://docs.cloud.google.com/netapp/volumes/docs/performance/monitor-performance).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
