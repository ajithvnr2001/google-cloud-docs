---
url: https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/performance-tuning-parameters/
title: AlloyDB Omni performance tuning parameters on a VM \u00a0|\u00a0 AlloyDB Omni using containers: 17.7.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:41:40.475387+00:00
---

# AlloyDB Omni performance tuning parameters on a VM  |  AlloyDB Omni using containers: 17.7.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/performance-tuning-parameters/

This page documents AlloyDB Omni version **17.7.0** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Containers: 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/overview)
  * [ Reference ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/reference/database-flags)



Send feedback 

#  AlloyDB Omni performance tuning parameters on a VM Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 17.7.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/performance-tuning-parameters)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/performance-tuning-parameters)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/performance-tuning-parameters)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/performance-tuning-parameters)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.10.0/docs/performance-tuning-parameters)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/performance-tuning-parameters)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/performance-tuning-parameters)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/performance-tuning-parameters)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/performance-tuning-parameters)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/performance-tuning-parameters)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/performance-tuning-parameters)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/performance-tuning-parameters)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/performance-tuning-parameters)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/performance-tuning-parameters)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/performance-tuning-parameters)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/performance-tuning-parameters)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/performance-tuning-parameters)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/performance-tuning-parameters)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.12.0/docs/performance-tuning-parameters)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/performance-tuning-parameters)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/performance-tuning-parameters)

This document describes performance tuning parameters that can improve AlloyDB Omni performance on a VM. These suggested tuning parameters are based on the results of running a set of workloads that exhibit different read and write patterns, caching behaviors, and index access patterns. 

Most default PostgreSQL parameter values remain unchanged, because the changes are limited to parameters that benefit the majority of applications. The suggested values of these parameters should generally improve performance on modern hardware.

Database parameter | AlloyDB Omni default | Suggested setting  
---|---|---  
`random_page_cost` | 4.0 | 1.1  
`temp_buffers` | 8 MB | 128 MB  
`max_wal_size` | 1 GB | 20 GB  
`min_wal_size` | 80 MB | 10 GB  
`default_toast_compression` | pglz | lz4  
`maintenance_work_mem` | 64 MB | 1 GB for smaller machines 2 GB for larger machines  
`max_worker_processes` | 64 | `max(64, # vCPUs)`  
`max_parallel_workers` | 8 | `max(8, # vCPUs)`  
`max_parallel_workers_per_gather` | 2 | `max(2, # vCPUs / 2)`  
`work_mem` | 4 MB | 128 to 512 MB, depending on workload and the amount of memory available  
`effective_cache_size` | 40% * DRAM | 80% * DRAM  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
