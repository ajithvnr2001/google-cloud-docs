---
url: https://docs.cloud.google.com/alloydb/docs/adaptive-autovacuum/
title: Configure adaptive autovacuum \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:06.040003+00:00
---

# Configure adaptive autovacuum  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/adaptive-autovacuum/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Configure adaptive autovacuum Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of AlloyDB for PostgreSQL adaptive autovacuum and describes how to configure it.

Vacuuming is an important PostgreSQL database maintenance operation. It is used to reclaim storage space occupied by updated or deleted rows to avoid table or index bloat. It is also used for freezing transaction IDs to [prevent transaction ID wraparound](https://www.postgresql.org/docs/current/routine-vacuuming.html#VACUUM-FOR-WRAPAROUND) and for updating the table statistics. 

For more information about vacuuming, see [Routine vacuuming](https://www.postgresql.org/docs/current/routine-vacuuming.html).

To automate the process of vacuuming and collectively updating the table statistics, AlloyDB supports adaptive autovacuum. _Adaptive autovacuum_ enables automatic adjustment of vacuum workload when your workload changes, removes dead tuples, and updates table statistics. 

Autovacuum ensures a reliable and consistent application transactional performance and maintains high availability of the system by preventing transaction ID wraparound.

By default, AlloyDB enables adaptive autovacuum. You can disable or modify adaptive autovacuum on AlloyDB by using database flags.

## Benefits

Adaptive autovacuum offers the following benefits:

  * **Automatic adjustment of resources.** AlloyDB automatically adjusts resources such as CPU, I/O, number of vacuum processes, and memory for the vacuum process based on the real time status of the workload and available resources without affecting the system performance.

  * **Prevention of transaction ID wraparound.** AlloyDB monitors the vacuum progress and transaction ID consumption speed. When necessary, AlloyDB throttles its transaction ID consumption by vacuuming every table in the database, preventing transaction ID wraparound.

  * **Periodic vacuum for tables.** AlloyDB triggers autovacuum based on the number of dead tuples and the pages that need to be scanned. It removes dead tuples in a timely manner to avoid table or index bloat.

  * **Automatic detection of blockers.** AlloyDB automatically detects blockers such as long running transactions, orphan prepared transactions, orphan replication slots, and shows warning messages similar to the following in the `postgres` log:
        
        Found a backend process PROCESS_ID with a long running transaction whose transaction
        id age AGE is larger than or equal to the transaction age threshold AGE_THRESHOLD.
        




## Configure adaptive autovacuum

By default, adaptive autovacuum is enabled on AlloyDB. You can disable adaptive autovacuum by setting an instance's `enable_google_adaptive_autovacuum` database flag to `off`.

For more information about setting database flags, see [Configure an instance's database flags](https://docs.cloud.google.com/alloydb/docs/instance-configure-database-flags).

AlloyDB supports several standard PostgreSQL database flags related to vacuum and autovacuum, for example, `vacuum_cost_delay` and `autovacuum_vacuum_cost_delay`. You do not need to set values in any of these flags for adaptive autovacuum to work because adaptive autovacuum adapts and optimizes its behavior to your real workloads. If you set values in these flags, then adaptive autovacuum adjusts its behavior to take your preferences into account.

To see the complete list of supported PostgreSQL database flags related to vacuum and autovacuum, see [vacuum flags](https://www.postgresql.org/docs/current/runtime-config-resource.html#GUC-VACUUM-COST-DELAY) and [autovacuum flags](https://www.postgresql.org/docs/current/runtime-config-autovacuum.html).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
