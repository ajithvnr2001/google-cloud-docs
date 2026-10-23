---
url: https://docs.cloud.google.com/alloydb/docs/columnar-engine/tune-columnar-engine/
title: Tune the columnar engine for AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T06:00:08.406061+00:00
---

# Tune the columnar engine for AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/columnar-engine/tune-columnar-engine/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Tune the columnar engine for AlloyDB for PostgreSQL Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to tune the columnar engine for an AlloyDB instance. This document assumes that you are familiar with PostgreSQL.

## Adjust the CPU resources for maintenance tasks

The following example shows you how to configure the columnar engine to use 50% of the CPU cores:
    
    
    google_job_scheduler.maintenance_cpu_percentage = 50
    

The columnar engine uses up to 20% of CPU cores for background maintenance jobs, such as population, refresh, and recommendation. To adjust the CPU resources for maintenance tasks, set the `google_job_scheduler.maintenance_cpu_percentage` flag to a value from `0` to `100`. The default value is `20`. Setting this flag to `0` disables background maintenance jobs. For non-zero values, the lowest CPU utilization for background maintenance tasks is 1 vCPU.

## Add workers to accelerate columnar maintenance

The following example shows you how to set four worker processes:
    
    
    google_job_scheduler.max_parallel_workers_per_job = 4
    

The columnar engine uses up to two worker processes for population and refresh background jobs. To increase the speed of these operations, set the following flag to increase the number of worker processes for background jobs. The default setting is 2 worker processes. These processes run on limited CPU resources as specified in the `google_job_scheduler.maintenance_cpu_percentage` flag. This flag doesn't require a database restart.

## Change the auto-columnarization schedule

The following example shows you how to set the auto-columnarization schedule to six hours:
    
    
    google_columnar_engine.auto_columnarization_schedule = 'EVERY 6 HOURS'
    

The auto-columnarization schedule can be set in the `google_columnar_engine.auto_columnarization_schedule` flag based upon anticipated scan-heavy workloads. Specify one or more hours for this flag. Changing the value of this flag doesn't require a database restart.

## Manually populate the columnar engine

The following example shows you how to manually populate the columnar engine:
    
    
    google_columnar_engine.enable_auto_columnarization = OFF
    

If you prefer to only manually populate the columnar engine, set the `google_columnar_engine.enable_auto_columnarization` flag to `OFF`. The default value of this flag is `ON`. Changing the value of this flag doesn't require a database restart. See [Manage column store content manually](https://docs.cloud.google.com/alloydb/docs/columnar-engine/manage-content-manually) for more information.

## Tuning the columnar engine population heap size

The following example shows you how to configure the `google_columnar_engine.population_heap_size_in_mb` flag:
    
    
    google_columnar_engine.population_heap_size_in_mb = 250
    

To convert data to columnar format, the columnar engine allocates the amount of memory in megabytes specified by the `google_columnar_engine.population_heap_size_in_mb` flag. Once the conversion is complete, this memory is immediately deallocated, typically within seconds.

The recommended values for the `google_columnar_engine.population_heap_size_in_mb` setting range from a minimum of 200 MB to a maximum of 1000 MB. However, the allowed flag values are from 0 to 2147483647 MB.

The default value of 250 MB for the `google_columnar_engine.population_heap_size_in_mb` flag works well for most typical database usage. However, you might face situations where you need to increase this value.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
