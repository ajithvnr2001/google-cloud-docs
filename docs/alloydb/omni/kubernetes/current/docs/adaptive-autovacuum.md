---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/adaptive-autovacuum/
title: Configure adaptive autovacuum \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: Current (18.4.0) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:28:57.933007+00:00
---

# Configure adaptive autovacuum  |  AlloyDB Omni using the container orchestrator: Current (18.4.0)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/adaptive-autovacuum/

This page documents AlloyDB Omni version **18.4.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/overview)



Send feedback 

#  Configure adaptive autovacuum Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.4.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/adaptive-autovacuum)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/adaptive-autovacuum)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/adaptive-autovacuum)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/adaptive-autovacuum)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/adaptive-autovacuum)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/adaptive-autovacuum)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/adaptive-autovacuum)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/adaptive-autovacuum)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/adaptive-autovacuum)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/adaptive-autovacuum)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/adaptive-autovacuum)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/adaptive-autovacuum)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/adaptive-autovacuum)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/adaptive-autovacuum)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/adaptive-autovacuum)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/adaptive-autovacuum)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/adaptive-autovacuum)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/adaptive-autovacuum)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/adaptive-autovacuum)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/adaptive-autovacuum)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/adaptive-autovacuum)

This page provides an overview of AlloyDB Omni adaptive autovacuum and describes how to configure it. 

Vacuuming is an important PostgreSQL database maintenance operation. It is used to reclaim storage space occupied by updated or deleted rows to avoid table or index bloat. It is also used for freezing transaction IDs to [prevent transaction ID wraparound](https://www.postgresql.org/docs/current/routine-vacuuming.html#VACUUM-FOR-WRAPAROUND) and for updating the table statistics.

For more information about vacuuming, see [Routine vacuuming](https://www.postgresql.org/docs/current/routine-vacuuming.html).

To automate the process of vacuuming and collectively updating the table statistics, AlloyDB Omni supports adaptive autovacuum. _Adaptive autovacuum_ enables automatic adjustment of vacuum workload when your workload changes, removes dead tuples, and updates table statistics.

Autovacuum ensures a reliable and consistent application transactional performance and maintains high availability of the system by preventing transaction ID wraparound.

By default, AlloyDB Omni enables adaptive autovacuum. You can disable or modify adaptive autovacuum on AlloyDB Omni by using database flags.

## Benefits

Adaptive autovacuum offers the following benefits:

  * **Automatic adjustment of resources.** AlloyDB Omni automatically adjusts resources such as CPU, I/O, number of vacuum processes, and memory for the vacuum process based on the real time status of the workload and available resources without affecting the system performance.

  * **Prevention of transaction ID wraparound.** AlloyDB Omni monitors the vacuum progress and transaction ID consumption speed. When necessary, AlloyDB Omni throttles its transaction ID consumption by vacuuming every table in the database, preventing transaction ID wraparound.

  * **Periodic vacuum for tables.** AlloyDB Omni triggers autovacuum based on the number of dead tuples and the pages that need to be scanned. It removes dead tuples in a timely manner to avoid table or index bloat.

  * **Automatic detection of blockers.** AlloyDB Omni automatically detects blockers, such as long running transactions, orphan prepared transactions, orphan replication slots, and shows warning messages similar to the following in the `postgres` log:
        
        Found a backend process PROCESS_ID with a long running transaction whose transaction
        id age AGE is larger than or equal to the transaction age threshold AGE_THRESHOLD.
        




## Configure adaptive autovacuum

By default, adaptive autovacuum is enabled on AlloyDB Omni. You can disable adaptive autovacuum by setting an instance's `enable_google_adaptive_autovacuum` database flag to `off`.

AlloyDB Omni supports several standard PostgreSQL database flags related to vacuum and autovacuum, for example, `vacuum_cost_delay` and `autovacuum_vacuum_cost_delay`. You don't need to set values in any of these flags for adaptive autovacuum to work because adaptive autovacuum adapts and optimizes its behavior to your real workloads. If you set values in these flags, then adaptive autovacuum adjusts its behavior to take your preferences into account.

To see the complete list of supported PostgreSQL database flags related to vacuum and autovacuum, see [vacuum flags](https://www.postgresql.org/docs/current/runtime-config-resource.html#GUC-VACUUM-COST-DELAY) and [autovacuum flags](https://www.postgresql.org/docs/current/runtime-config-autovacuum.html).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
