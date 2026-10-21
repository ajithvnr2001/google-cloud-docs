---
url: https://docs.cloud.google.com/managed-lustre/docs/performance-tiers/
title: Performance tiers \u00a0|\u00a0 Managed Lustre \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:39:56.223892+00:00
---

# Performance tiers  |  Managed Lustre  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-lustre/docs/performance-tiers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Managed Lustre ](https://docs.cloud.google.com/managed-lustre/docs/overview)



Send feedback 

#  Performance tiers Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud Managed Lustre offers different performance tiers to meet your specific workload requirements and budget. You can choose a tier that provides sustained, predictable performance for your entire file system, or a Dynamic tier that automatically optimizes storage costs for large, partially active datasets.

## Available tiers

The following table summarizes the performance tiers available for Managed Lustre.

Performance tier | Min capacity | Max capacity | Step size  
---|---|---|---  
**1,000 MBps per TiB** | 9,000 GiB | 10,008,000 GiB (9.5 PiB) | For storage capacities up to 2,556,000 GiB: 9,000 GiB  
For larger storage capacities: 72,000 GiB  
**500 MBps per TiB** | 18,000 GiB | 20,016,000 GiB (19.1 PiB) | For storage capacities up to 5,112,000 GiB: 18,000 GiB  
For larger storage capacities: 144,000 GiB  
**250 MBps per TiB** | 36,000 GiB | 40,032,000 GiB (38.2 PiB) | For storage capacities up to 10,224,000 GiB: 36,000 GiB  
For larger storage capacities: 288,000 GiB  
**125 MBps per TiB** | 72,000 GiB | 20,448,000 GiB (19.5 PiB) | 72,000 GiB  
**Dynamic** (25 MBps per TiB) | 472,000 GiB | 84,016,000 GiB (80.1 PiB) | 472,000 GiB  
  
Step sizes change once the instance size reaches a specific threshold.

You can increase the storage capacity of an instance after it's been created, up to the maximum value allowed for its performance tier and step size. If you create an instance within the smaller step size range for its tier, you cannot later increase it beyond the step size threshold. See [Limitations on increasing capacity](https://docs.cloud.google.com/managed-lustre/docs/increase-capacity#limitations) for details.

## Numbered tiers

Numbered tiers provide consistent, high-speed performance. These tiers are ideal for workloads that demand high throughput and low latency for every data access.

You choose a specific performance level when you create your instance, and that throughput is delivered consistently for your entire file system. Performance scales linearly with the amount of storage you provision. In addition to raw throughput, IOPS and metadata performance also scale with the instance's provisioned capacity and throughput.

Numbered tiers provide sub-millisecond latency.

  * **1,000 MBps per TiB** : Recommended for high-performance workloads and AI/ML training where throughput is critical.
  * **500 MBps per TiB** : For demanding AI/ML workloads, complex HPC applications, and data-intensive analytics that require substantial throughput but may benefit from a more balanced price-to-performance ratio.
  * **250 MBps per TiB** : Suitable for a broad range of HPC workloads, AI/ML inference, data preprocessing, and applications that require better performance than traditional NFS, at a cost-effective price point.
  * **125 MBps per TiB** : Designed for scenarios where large capacities and parallel file system access are key. Good for less I/O-bound parallel tasks.



## Dynamic tier

The Dynamic tier is a cost-effective solution designed to handle growing AI and HPC datasets by automatically optimizing performance based on data access patterns. It provides a single, unified namespace at petabyte scale, delivering high-speed access for active data stored in a high-performance cache while reducing the total cost of ownership for large datasets. Aggregate throughput available for the instance scales at 25 MBps per TiB.

The system intelligently manages data placement using an automated policy that helps ensure frequently used data remains highly performant. This process is transparent to users and applications, who interact with the file system as a single mount point with no manual data migration or management overhead required.

### Key benefits

  * Reduced storage costs: Lower your price-per-byte for large datasets by storing the majority of your data on cost-effective volume storage.
  * Single namespace at PB scale: Consolidate massive, growing datasets into a single mount point without needing to manually migrate or tier data between different storage systems.
  * Intelligent and automated: A transparent, block-level caching system helps ensure that high-performance storage is used for the most critical data.
  * Blended performance: Get sub-millisecond latency for active data and consistent, tens-of-milliseconds latency for less frequently accessed portions of the dataset.



## Detailed performance specifications

Follow the best practices in [Performance considerations](https://docs.cloud.google.com/managed-lustre/docs/performance) to help your instances achieve these IOPS and metadata performance numbers.

### IOPS

Maximum IOPS scale linearly per TiB of provisioned instance capacity.

Performance tier | Read IOPS (per TiB) | Write IOPS (per TiB)  
---|---|---  
**1,000 MBps per TiB** | 5,800 | 5,600  
**500 MBps per TiB** | 2,900 | 2,800  
**250 MBps per TiB** | 1,450 | 1,400  
**125 MBps per TiB** | 725 | 700  
**Dynamic** | 145 | 140  
  
### Metadata operations

Maximum metadata operations increase in steps based on capacity.

Every instance receives its first step of metadata performance at the minimum instance size (which is smaller than the standard capacity step).

For larger instances, performance increases each time the total capacity exceeds a multiple of the step size.

Performance tier | Capacity step (GiB) | File stats added per step | File creates added per step | File deletes added per step  
---|---|---|---|---  
**1,000 MBps per TiB** | 72,000 | 410,000 per second | 115,000 per second | 95,000 per second  
**500 MBps per TiB** | 144,000  
**250 MBps per TiB** | 288,000  
**125 MBps per TiB** | 576,000  
**Dynamic** | 3,776,000 | 275,000 per second | 115,000 per second | 130,000 per second  
  
**Example** : For the 1,000 MBps per TiB tier, the capacity step size is 72,000 GiB. If you create a 153,000 GiB instance, you receive 3 steps' worth of metadata performance:

  * Step 1: Granted at the minimum instance size.
  * Step 2: Granted when capacity exceeds 72,000 GiB.
  * Step 3: Granted when capacity exceeds 144,000 GiB.
  * Step 4: **Not reached**. Granted when capacity exceeds 216,000 GiB.



Because 153,000 GiB falls between the 144,000 GiB and 216,000 GiB thresholds, the instance receives three steps of performance: a maximum of 1,230,000 file stats per second (3 * 410,000).

## What's next

  * [Create a Managed Lustre instance](https://docs.cloud.google.com/managed-lustre/docs/create-instance)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
