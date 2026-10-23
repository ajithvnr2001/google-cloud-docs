---
url: https://docs.cloud.google.com/alloydb/docs/adaptive-autovacuum/
title: Configure adaptive autovacuum \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:42:52.609917+00:00
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

To reclaim storage space from updated or deleted rows, update table statistics, and prevent transaction ID wraparound, AlloyDB for PostgreSQL enables adaptive autovacuum by default. _Adaptive autovacuum_ automatically adjusts vacuum workloads as your database traffic changes, removes dead tuples, and maintains consistent transactional performance and high availability.

Vacuuming is a critical PostgreSQL maintenance operation that prevents table or index bloat and freezes transaction IDs to [prevent transaction ID wraparound](https://www.postgresql.org/docs/current/routine-vacuuming.html#VACUUM-FOR-WRAPAROUND). For more information, see [Routine vacuuming](https://www.postgresql.org/docs/current/routine-vacuuming.html).

You can disable or modify adaptive autovacuum in AlloyDB by using database flags.

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

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
