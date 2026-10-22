---
url: https://docs.cloud.google.com/filestore/docs/performance/
title: About instance performance \u00a0|\u00a0 Filestore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:59:29.023419+00:00
---

# About instance performance  |  Filestore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/performance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  About instance performance Stay organized with collections  Save and categorize content based on your preferences. 

This page introduces the performance options available for Filestore instances and provides general recommendations to optimize performance. When you use Google Cloud console to create zonal and regional instances, custom performance is enabled by default to let you scale IOPS independently of capacity to meet your specific workload needs. 

The following table provides a summary of performance limits for the lower and higher capacity ranges under custom performance settings:

Capacity range | Service tier | Capacity | Provisioned IOPS per TiB  
---|---|---|---  
**Lower capacity range** | Regional | 100 GiB to 10,239 GiB | 4,000 to 17,000  
| Zonal | 1 TiB to 9.75 TiB | 4,000 to 17,000  
**Higher capacity range** | Regional | 10 TiB to 100 TiB | 3,000 to 7,500  
| Zonal | 10 TiB to 100 TiB | 3,000 to 7,500  
  
## Understand performance calculations

The following table displays performance calculations based on provisioned IOPS per TiB and allocated capacity. The calculations are based on different capacity ranges to show how the values for read IOPS, write IOPS, read throughput, and write throughput change for the minimum and maximum IOPS per TiB values. 

For more information, see [Read and write IOPS](https://docs.cloud.google.com/filestore/docs/custom-performance#iops).

Capacity range | Minimum and maximum   
provisioned IOPS per TiB | Capacity | Read IOPS | Write IOPS | Read throughput (MiBps) | Write throughput (MiBps) | Single client read throughput (MiBps) | Single client write throughput (MiBps)  
---|---|---|---|---|---|---|---|---  
Lower capacity range   
(100 GiB to 10,239 GiB) | 4,000 | 100 GiB | 2,000* | 600 | 47 | 16 | 47 | 16  
600 GiB | 2,344 | 703 | 55 | 19 | 55 | 19  
1,024 GiB | 4,000 | 1,200 | 94 | 32 | 94 | 32  
10,239 GiB | 39,996 | 11,999 | 940 | 320 | 450 | 260  
17,000 | 100 GiB | 2,000 | 600 | 47 | 16 | 47 | 16  
600 GiB | 9,961 | 2,988 | 234 | 80 | 234 | 80  
1,024 GiB | 17,000 | 5,100 | 400 | 136 | 400 | 136  
10,239 GiB | 169,983 | 50,995 | 3,995 | 1,360 | 450 | 260  
Higher capacity range   
(10 TiB to 100 TiB) | 3,000 | 10 TiB | 30,000 | 9,000 | 705 | 240 | 705 | 240  
7,500 | 100 TiB | 750,000 | 225,000 | 17,625 | 6,000 | 1,600 | 800  
  
* 1,024 GiB instances require enabled custom performance with a minimum of 2,000 IOPS. For more information, see [Small capacity instances](https://docs.cloud.google.com/filestore/docs/%C2%A7/filestore/docs/service-tiers#small-instances).

## Performance scaling

In single- and few-client scenarios, you must increase the number of TCP connections with the [`nconnect`](https://man7.org/linux/man-pages/man5/nfs.5.html) mount option to achieve maximum NFS performance.

For specific service tiers, we recommend specifying the following number of connections between the client and server:

Tier | Capacity | Number of connections  
---|---|---  
Regional, zonal | 1-9.75 TiB | `nconnect=2`  
Regional, zonal | 10-100 TiB | `nconnect=7`  
Basic SSD | - | `nconnect=7`  
Enterprise | - | `nconnect=2`  
High scale SSD | - | `nconnect=7`  
  
In general, the larger the file share capacity and the fewer the connecting client VMs, the more performance you gain by specifying additional connections with `nconnect`.

## Recommended client machine type

We recommend having a Compute Engine [machine type](https://docs.cloud.google.com/compute/docs/machine-types), such as `n2-standard-8`, that provides an egress bandwidth of at least 16 Gbps. This egress bandwidth allows the client to achieve approximately 16 Gbps read bandwidth for cache-friendly workloads. For additional context, see [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).

## Linux client mount options

We recommend using the following NFS mount options, especially `hard` mount, `async`, and the `rsize` and `wsize` options, to achieve the best performance on Linux client VM instances. For more information on NFS mount options, see [nfs](https://linux.die.net/man/5/nfs).

Default option | Description  
---|---  
`hard` | The NFS client retries NFS requests indefinitely.  
`timeo=600` | The NFS client waits 600 deciseconds (60 seconds) before retrying an NFS request.  
`retrans=3` | The NFS client attempts NFS requests three times before taking further recovery action.  
`rsize=524288` | The NFS client can receive a maximum of 524,288 bytes from the NFS server per `READ` request.   
**Note** : For basic-tier instances, set the `rsize` value to `1048576`.  
`wsize=524288` | The NFS client can send a maximum of 524,288 bytes to the NFS server per `WRITE` request.  
`resvport` | The NFS client uses a privileged source port when communicating with the NFS server for this mount point.  
`async` | The NFS client delays sending application writes to the NFS server until certain conditions are met.   
**Caution** : Using the `sync` option significantly reduces performance.  
  
### Optimize the NFS read throughput with `read_ahead_kb` parameter

The NFS `read_ahead_kb` parameter specifies the amount of data, in kilobytes, that the Linux kernel should prefetch during a sequential read operation. As a result, the subsequent read requests can be served directly from memory to reduce latency and improve the overall performance.

For Linux kernel versions `5.4` and higher, the Linux NFS client uses a default `read_ahead_kb` value of 128 KB. We recommend increasing this value to 20 MB to improve the sequential read throughput.

After you successfully mount the file share on the Linux client VM, you can use the following script to manually adjust the `read_ahead_kb` parameter value:
    
    
    mount_point=MOUNT_POINT_DIRECTORY
    device_number=$(stat -c '%d' $mount_point)
    ((major = ($device_number & 0xFFF00) >> 8))
    ((minor = ($device_number & 0xFF) | (($device_number >> 12) & 0xFFF00)))
    sudo bash -c "echo 20480 > /sys/class/bdi/$major:$minor/read_ahead_kb"
    

Replace the following:

MOUNT_POINT_DIRECTORY is the path to the directory where the file share is mounted.

**Note:** You can't use this script directly with Google Kubernetes Engine (GKE) if the pod is not running as the root user. To set the `read_ahead_kb` parameter, use an [init container](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/) with root permissions or [DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/).

## Single and multiple client VM performance

Filestore's scalable service tiers are performance optimized for multiple client VMs, not a single client VM.

For zonal, regional, and enterprise instances, at least four client VMs are needed to take advantage of full performance. This ensures that all of the VMs in the underlying Filestore cluster are fully utilized.

For added context, the smallest scalable Filestore cluster has four VMs. Each client VM communicates with just one Filestore cluster VM, regardless of the number of NFS connections per client specified using the [`nconnect`](https://man7.org/linux/man-pages/man5/nfs.5.html) mount option. If using a single client VM, read and write operations are only performed from a single Filestore cluster VM.

## Capacity-based performance limits

Capacity-based limits apply to service tiers that don't support custom performance, such as basic tiers, or instances in which you manually deactivate custom performance.

Each Filestore service tier provides a different level of performance that might vary due to factors such as the use of caching, the number of client VMs, the [machine type](https://docs.cloud.google.com/compute/docs/machine-types) of the client VMs, and the workload tested.

The following table lists the maximum performance you can achieve when setting minimum and maximum capacity for each service tier. All table values are estimated limits.

Service tier | Capacity | Read IOPS | Write IOPS | Read throughput (MiBps) | Write throughput (MiBps) | Single client read throughput (MiBps) | Single client write throughput (MiBps)  
---|---|---|---|---|---|---|---  
Zonal | 1 TiB | 9,200 | 2,600 | 260 | 88 | 260 | 88  
9.75 TiB | 89,700 | 25,350 | 2,535 | 858 | 450 | 260  
10 TiB | 92,000 | 26,000 | 2,600 | 880 | 1,600 | 800  
100 TiB | 920,000 | 260,000 | 26,000 | 8,800 | 1,600 | 800  
Regional | 1 TiB | 12,000 | 4,000 | 120 | 100 | 120 | 100  
9.75 TiB | 117,000 | 39,000 | 1,170 | 975 | 450 | 260  
10 TiB | 92,000 | 26,000 | 2,600 | 880 | 1,600 | 800  
100 TiB | 920,000 | 260,000 | 26,000 | 8,800 | 1,600 | 800  
Enterprise | 1 TiB | 12,000 | 4,000 | 120 | 100 | 120 | 100  
10 TiB | 120,000 | 40,000 | 1,200 | 1,000 | 450 | 260  
Basic HDD | 1 TiB - 10 TiB | 600 | 1,000 | 100 | 100 | 100 | 100  
10 TiB - 63.9 TiB | 1,000 | 5,000 | 180 | 120 | 180 | 120  
Basic SSD | 2.5 TiB - 63.9 TiB | 60,000 | 25,000 | 1,200 | 350 | 1,200 | 350  
  
## Improve performance across Google Cloud resources

Operations across multiple Google Cloud resources, such as copying data from Cloud Storage to a Filestore instance using the Google Cloud CLI, can be slow. To help mitigate performance issues, try the following:

  * Ensure the Cloud Storage bucket, client VM, and Filestore instance all reside in the same [region](https://docs.cloud.google.com/filestore/docs/regions).

[Dual-regions](https://docs.cloud.google.com/storage/docs/locations#location-dr) provide a maximally-performant option for data stored in Cloud Storage. If using this option, ensure the other resources reside in one of the single regions contained in the dual-region. For example, if your Cloud Storage data resides in `us-central1,us-west1`, ensure that your client VM and Filestore instance reside in `us-central1`.

  * For a point of reference, verify the performance of a VM with a Persistent Disk (PD) attached and compare to the performance of a Filestore instance. 

    * If the PD-attached VM is similar or slower in performance when compared to the Filestore instance, this might indicate a performance bottleneck unrelated to Filestore. To improve the baseline performance of your non-Filestore resources, you can adjust the gcloud CLI properties associated with parallel composite uploads. For more information see [How tools and APIs use parallel composite uploads](https://docs.cloud.google.com/storage/docs/parallel-composite-uploads#behavior).
**Note:** The gcloud CLI has no built-in support for throttling requests. Users should experiment with requested values as optimal values can vary based on a number of factors including network speed, number of CPUs, and available memory.
    * If the performance of the Filestore instance is notably slower than the  
PD-attached VM, try spreading the operation over multiple VMs to improve performance of read operations from Cloud Storage.



## What's next

  * [Custom performance](https://docs.cloud.google.com/filestore/docs/custom-performance)
  * [Test performance](https://docs.cloud.google.com/filestore/docs/testing-performance)
  * [Troubleshoot performance-related issues](https://docs.cloud.google.com/filestore/docs/troubleshooting)
  * [Scale capacity](https://docs.cloud.google.com/filestore/docs/scale)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
