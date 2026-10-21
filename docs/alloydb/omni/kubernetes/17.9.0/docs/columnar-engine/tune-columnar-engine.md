---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/columnar-engine/tune-columnar-engine/
title: Tune the columnar engine for AlloyDB Omni \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: 17.9.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:45:15.382641+00:00
---

# Tune the columnar engine for AlloyDB Omni  |  AlloyDB Omni using the container orchestrator: 17.9.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/columnar-engine/tune-columnar-engine/

This page documents AlloyDB Omni version **17.9.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/overview)



Send feedback 

#  Tune the columnar engine for AlloyDB Omni Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 17.9.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/columnar-engine/tune-columnar-engine)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/columnar-engine/tune-columnar-engine)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/columnar-engine/tune-columnar-engine)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/columnar-engine/tune-columnar-engine)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/columnar-engine/tune-columnar-engine)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/columnar-engine/tune-columnar-engine)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/columnar-engine/tune-columnar-engine)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/columnar-engine/tune-columnar-engine)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/columnar-engine/tune-columnar-engine)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/columnar-engine/tune-columnar-engine)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/columnar-engine/tune-columnar-engine)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/columnar-engine/tune-columnar-engine)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/columnar-engine/tune-columnar-engine)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/columnar-engine/tune-columnar-engine)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/columnar-engine/tune-columnar-engine)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/columnar-engine/tune-columnar-engine)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/columnar-engine/tune-columnar-engine)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/columnar-engine/tune-columnar-engine)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/columnar-engine/tune-columnar-engine)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/columnar-engine/tune-columnar-engine)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/columnar-engine/tune-columnar-engine)

This document describes how to tune the columnar engine for AlloyDB Omni. This document assumes that you are familiar with PostgreSQL. 

### Adjust the CPU resources for maintenance tasks

This example configures the columnar engine to use 50% of the CPU cores.
    
    
    google_job_scheduler.maintenance_cpu_percentage = 50
    

Columnar engine uses up to 20% of CPU cores for background maintenance jobs, such as population, refresh, and recommendation. To adjust the CPU resources to allow for maintenance tasks, set the `google_job_scheduler.maintenance_cpu_percentage` flag to a value from 20 to 100. The default value is 20. The lowest CPU utilization for background maintenance tasks is 1 vCPU.

### Increase the speed of worker processes

This example sets four worker processes.
    
    
    google_job_scheduler.max_parallel_workers_per_job = 4
    

The columnar engine uses up to two worker processes for population and refresh background jobs. To increase the speed of these operations, set the following flag to increase the number of worker processes for background jobs. The default setting is 2 worker processes. These processes run on limited CPU resources as specified in the `google_job_scheduler.maintenance_cpu_percentage` flag. This flag does not require the database to be restarted.

### Change the auto-columnarization schedule

This example sets the auto-columnarization schedule to six hours.
    
    
    google_columnar_engine.auto_columnarization_schedule = 'EVERY 6 HOURS'
    

The auto-columnarization schedule can be set in the `google_columnar_engine.auto_columnarization_schedule` flag based upon anticipated scan-heavy workloads. Specify one or more hours for this flag. Changing the value of this flag does not require a database restart.

### Manually populate the columnar engine

This example lets you only manually populate the columnar engine.
    
    
    google_columnar_engine.enable_auto_columnarization = OFF
    

If you prefer to only manually populate the columnar engine, set the `google_columnar_engine.enable_auto_columnarization` flag to `OFF`. By default, the flag is set to `ON`. Changing the value of this flag does not require a database restart. See [Manage Content Manually](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/columnar-engine/manage-content-manually) section for more details.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
