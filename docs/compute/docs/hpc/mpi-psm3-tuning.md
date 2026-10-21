---
url: https://docs.cloud.google.com/compute/docs/hpc/mpi-psm3-tuning/
title: Improve performance of MPI applications that use PSM3 \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:53:08.671078+00:00
---

# Improve performance of MPI applications that use PSM3  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/hpc/mpi-psm3-tuning/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Improve performance of MPI applications that use PSM3 Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the PSM3 configuration parameters that we recommend you use with MPI applications running on H4D compute instances and Cloud RDMA.

For information about all the available PSM3 configuration parameters, see [Intel Ethernet Fabric Suite Host Software User Guide](https://www.intel.com/content/www/us/en/content-details/632489/intel-ethernet-fabric-suite-host-software-user-guide.html).

## Recommendations for applications with bursty data flows or heavy UD traffic

Applications that experience sudden bursts of traffic or rely heavily on Unreliable Datagram (UD) mode can overwhelm the network interface, leading to packet drops at the source.

  * **Solution** : Configure the credit-based back pressure system to regulate transmit bursts and prevent packet loss at the transport layer. A Compute Engine H4D instance provides 256 total credits. We recommend that you allocate each vCPU a minimum of 1 fixed credit, with any remaining capacity placed in a shared pool.
  * **Recommended configuration** (Example for 192 ranks per node): For an operation with 192 ranks per node, if each vCPU gets 1 fixed credit, then the shared pool will be 256 - 192 = 64.
        
        IRDMA_SHARED_UD_CREDITS=64
        IRDMA_TRANSPARENT_UD_QD_OVERRIDE=1
        




Increasing the total credit count beyond recommended limits might lead to transmit drops at the source. Although oversubscribing (setting total credits higher than available) can improve performance for workloads with steady, low-density traffic patterns, it typically degrades performance for workloads characterized by sudden bursts or heavy UD traffic.

The environment variables you can use for tuning Cloud RDMA performance are as follows:

  * **IRDMA_SHARED_UD_CREDITS** : specifies the size of a global pool of UD credits that are available to all processes on a single node. With a value of 64, this means there is a shared reserve of 64 credits that any process can potentially use.
  * **IRDMA_TRANSPARENT_UD_QD_OVERRIDE** : limits queue depth for queue pairs (QPs) that use UD in the `irdma` driver. When set to `1`, it works with `IRDMA_SHARED_UD_CREDITS` to enforce transport-layer backpressure and prevent transmit queue overruns under heavy multi-process loads.



## Recommendations for applications with high reliability or high memory requirements

To ensure the reliability of UD packets on the receiver side, your RDMA applications must allocate enough receive buffers and keep slots available in the Completion Queue (CQ).

  * **Standard recommendation for high reliability** : Use the following environment variables to specify higher queue depths as a best effort to avoid receive queue (RX) UD packet drops.
        
        PSM3_NUM_RECV_WQES=32767
        PSM3_NUM_RECV_CQES=65536
        

  * **Exception for high memory requirements** : If your application faces out of memory (OOM) issues, then reduce the queue sizes but maintain the same proportion between the two values.

Applications such as High Performance Conjugate Gradients (HPCG) have massive memory requirements. Using the settings for the standard recommendation for high reliability can result in OOM errors. `PSM3_NUM_RECV_WQES` dictates the number of RX work queue entries (WQEs) and eager bounce buffers allocated per local endpoint. Higher values result in a larger memory overhead.




The environment variables you can use for improving reliability or memory utilization are:

  * **`PSM3_NUM_RECV_WQES`** : sets the number of RX WQEs to allocate. The UD QP is sized at `PSM3_NUM_RECV_WQES + 1032 WQEs`. This parameter also sets the number of UD receive eager bounce buffers (each of size `PSM3_MTU`) that are allocated for each local endpoint.

  * **`PSM3_NUM_RECV_CQES`** : controls the number of completion queue entries (CQEs) for receiving operations. This parameter helps ensure the reliability of UD packets on the receiver side by ensuring there are always slots available in the completion queue. A higher queue depth, for example 65536, helps to avoid RX UD packet drops but uses memory, and can result in OOM errors for memory-intensive applications.




## Recommendations for applications that don't reuse buffers

Some applications, such as High-performance LINPACK (HPL), allocate and free temporary communication buffers frequently instead of retaining and reusing them. This continuous cycle of requesting and releasing memory forces the system to constantly register and deregister memory pages, creating a significant performance bottleneck.

  * **Solution** : Use a custom memory allocator like `jemalloc` as a workaround. `jemalloc` is a high-performance, general-purpose memory allocator (malloc) designed to emphasize concurrency scaling and avoid memory fragmentation. By forcing the efficient recycling of large communication buffers (larger than 128 KB), this solution bypasses expensive kernel reallocation cycles and restores PSM3 performance.

  * **Recommended configuration** :

    1. Install `jemalloc`. For example, on Rocky Linux you can run the following commands that use the extra packages for Enterprise Linux (EPEL) repository:
           
           sudo dnf install epel-release
           sudo dnf install jemalloc
           

    2. Preload `jemalloc` and apply optimized cache limits before running your application:
           
           LD_PRELOAD="/usr/lib64/libjemalloc.so.2"
           export MALLOC_CONF="dirty_decay_ms:-1,muzzy_decay_ms:-1,lg_tcache_max:26"
           




The configuration command uses the following settings:

  * `LD_PRELOAD`: specifies the shared libraries to load before starting a process.
  * `MALLOC_CONF`: configures memory allocation behavior for `jemalloc`.
  * `dirty_decay_ms:-1` and `muzzy_decay_ms:-1`: instructs `jemalloc` to never return unused memory to the OS. This keeps pages permanently registered for immediate reuse.
  * `lg_tcache_max:26`: increases the per-thread memory cache limit to 64 MB, which ensures that large communication buffers are aggressively cached.



## What's next

  * Review other performance tuning recommendations at [Optimize and scale MPI with Cloud RDMA](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-mpi-application#optimize-and-scale).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
