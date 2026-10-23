---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/optimize-database-performance-compare-snapshots/
title: Compare performance snapshots \u00a0|\u00a0 AlloyDB Omni for Kubernetes: 15.7.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:54:43.607266+00:00
---

# Compare performance snapshots  |  AlloyDB Omni for Kubernetes: 15.7.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/optimize-database-performance-compare-snapshots/

This page documents AlloyDB Omni version **15.7.0** using the **Kubernetes** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For Kubernetes: 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/overview)



Send feedback 

#  Compare performance snapshots Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.7.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/optimize-database-performance-compare-snapshots)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/optimize-database-performance-compare-snapshots)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/optimize-database-performance-compare-snapshots)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/optimize-database-performance-compare-snapshots)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/optimize-database-performance-compare-snapshots)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/optimize-database-performance-compare-snapshots)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/optimize-database-performance-compare-snapshots)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/optimize-database-performance-compare-snapshots)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/optimize-database-performance-compare-snapshots)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/optimize-database-performance-compare-snapshots)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/optimize-database-performance-compare-snapshots)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/optimize-database-performance-compare-snapshots)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/optimize-database-performance-compare-snapshots)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/optimize-database-performance-compare-snapshots)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/optimize-database-performance-compare-snapshots)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/optimize-database-performance-compare-snapshots)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/optimize-database-performance-compare-snapshots)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/optimize-database-performance-compare-snapshots)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/optimize-database-performance-compare-snapshots)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/optimize-database-performance-compare-snapshots)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/optimize-database-performance-compare-snapshots)

This document describes how to identify and mitigate AlloyDB Omni database performance issues by using a report that compares snapshots of system metrics between two different points in time. The system metrics captured in each snapshot include virtual CPU (vCPU) usage, memory usage, disk I/O, transaction count, and wait events. 

## How performance snapshot reports work

Performance snapshot reports are a built-in AlloyDB Omni tool that captures and analyzes performance data to help you identify the cause of performance issues.

Performance snapshot reports display database metrics between two timestamps in a single report. You can use the performance snapshot report information to identify performance issues with your performance snapshot report instance, like decreased database performance during certain times of the day or decreased performance over a certain time period.

Using the performance snapshot report, you compare the metrics to a performance baseline to gain insights into workload performance metrics, which you can use to optimize or troubleshoot database performance. A _baseline_ is a customized set of database snapshots that measure the standard performance and behavior of a database for a specific configuration and workload.

For information about wait events in performance snapshot report, see [Database performance snapshot report reference](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/reference/database-performance-snapshot-report-reference).

## Required roles

Ensure that you have the [`pg_monitor` role](https://www.postgresql.org/docs/15/predefined-roles.html). This role is granted to superusers, who can then grant `pg_monitor` to other users.

For example, `postgres` is the superuser by default. You can run `GRANT pg_monitor TO my_user` as `postgres` to allow `my_user` to use the performance snapshot tool as described in this document.

## Install performance snapshot report

`perfsnap` is the schema name that contains SQL functions that allow users to capture snapshots or generate reports. This schema is part of the AlloyDB Omni `g_stats` extension. Use the superuser role to install performance snapshot report.

To use the `perfsnap` APIs, connect to any database where users want to install the extension, and create the `g_stats` extension with the following command:
    
    
    CREATE EXTENSION IF NOT EXISTS g_stats;
    

## Create a snapshot of system metrics

Create a snapshot at the beginning and end of the workload you're interested in. The time interval between the two snapshots allows enough time for the workload to progress so that the system can accumulate metrics that reflect the workload. After you obtain metrics from the resulting performance snapshot report, you can take another set of snapshots and repeat the process.

  1. [Connect a `psql` client to an AlloyDB instance](https://docs.cloud.google.com/alloydb/docs/connect-psql).
  2. Run `SELECT perfsnap.snap()`. The output looks similar to the following:
         
         postgres=# select perfsnap.snap();
          snap
         ------
             1
         (1 row)
         




## View a list of snapshots

  1. [Connect a `psql` client to an AlloyDB instance](https://docs.cloud.google.com/alloydb/docs/connect-psql).
  2. Run `SELECT * FROM perfsnap.g$snapshots`. The output looks similar to the following:
         
         postgres=# select * from perfsnap.g$snapshots;
          snap_id |           snap_time           | instance_id | node_id | snap_description   | snap_type | is_baseline
         ---------+-------------------------------+-------------+---------+--------------------+-----------+-------------
                1 | 2023-11-13 22:13:43.159237+00 | sr-primary  |         | Manual snapshot    | Manual    | f
                2 | 2023-11-13 22:53:40.49565+00  | sr-primary  |         | Automatic snapshot | Automatic | f
         (2 rows)
         

**Note:** To support basic metrics tracking, AlloyDB automatically takes a snapshot once a day.



## Generate a snapshot report

To generate a report that captures the difference between snapshots 1 and 2, for example, run   
`SELECT perfsnap.report(1,2)`.

The second snapshot in a differential operation doesn't need to immediately follow the first snapshot. However, make sure you capture the second snapshot in the differential after the first snapshot.

The generated performance snapshot report looks similar to the following abridged example:

#### Example performance snapshot report
    
    
    $ psql -d postgres -U alloydbsuperuser
    postgres=> select perfsnap.report(22, 23);
    
    report
    --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
     PGSNAP DB Report for:
    
     Snapshot details
     --------------------------------------
     Host                   i841-sr-primary-2a34f46e-06bc
     Release                14.12
     Startup Time           2024-10-08 03:23:15+00
    
                  Snap Id    Snap Time
     ------------ ---------- ------------------------
     Begin Snap:          22 24.10.2024 04:33:56 (UTC) Automatic snapshot
       End Snap:          23 25.10.2024 04:38:56 (UTC) Automatic snapshot
        Elapsed:                      1 day 00:04:59.979321
    
     Database Cache sizes
     ~~~~~~~~~~~~~
                Shared Buffers:       31 GB        Block Size:         8192
          Effective Cache Size:       25 GB       WAL Buffers:        16384
    
     Host CPU
     ~~~~~~~~~~
           %User   %Nice %System   %Idle    %WIO    %IRQ   %SIRQ  %Steal  %Guest
         ------- ------- ------- ------- ------- ------- ------- ------- -------
            1.07    0.22    0.91   97.40    0.09    0.00    0.31    0.00    0.00
    
     Host Memory
     ~~~~~~~~~~~~
                  Total Memory:       63 GB
              Available Memory:       11 GB
                   Free Memory:      726 MB
                Buffers Memory:     3706 MB
    
     Load profile (in bytes)
     ~~~~~~~~~~~~~~~~~~~~~~~            Per Second         Per Transaction
                                        ------------       ---------------
                         Redo size:         63083.64               4489.93
                     Logical reads:          1961.21                139.59
                     ...
    
     Response Time Profile (in s)
     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     CPU time:               5399 (   0.39%)
     Wait time:           1386906 (  99.61%)
     Total time:           1392306
    
     Backend Processes Wait Class Breakdown (in s)
     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     IO                   119.300 (  98.91%)
     LWLock                 1.305 (   1.08%)
     IPC                     .010 (   0.01%)
     Lock                    .000 (   0.00%)
    
     Backend Processes Wait Information
     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     Event                                          Class         Waits      Time (us)      Avg (us)
     -------------------------------------- ------------- ------------- -------------- -------------
     CPU                                                                    1995948632
     WALInsert                                     LWLock             1           6656          6656
    
     Vacuum Information
     ~~~~~~~~~~~~~~~~~~~
                 Num Analyze operations:             1976
                  Num Vacuum operations:             3435
    
     Per Database Information
     ~~~~~~~~~~~~~~~~~~~~~~~~~
     Name                      Commits       Rollbacks     BlkRds        Blkhits       TempFiles     TempBytes
     ------------------------- ------------- ------------- ------------- ------------- ------------- -------------
     bench                             27939             0             0       7823038             0       0 bytes
     postgres                          39792             0             7      11089243             0       0 bytes
    
     Per Database DML & DQL Information
     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     Name                      Tuples returned  Tuples fetched   Tuples inserted  Tuples updated   Tuples deleted   Index splits     Index Only heap fetches   HOT updates
     ------------------------- ---------------- ---------------- ---------------- ---------------- ---------------- ---------------- ------------------------- ----------------
     bench                             16119481          4843262                0                0                0                0                        16                0
     postgres                          25415473          6327188                0               10                0                0                         0                8
    
     Per Database Conflict Information
     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     Name                      Lock Timeout  Old Snapshot  Buffer Pins   Deadlock
     ------------------------- ------------- ------------- ------------- -------------
     bench                                 0             0             0             0
     postgres                              0             0             0             0
    
     Per Database Vacuum Information
     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     Name                      Frozen XID    % Consumed    Aggregate Vacuum Gap
     ------------------------- ------------- ------------- --------------------
     bench                         179460916         9.00%         20539084
     postgres                      179339239         9.00%         20660761
    
     Per Database Sizing Information
     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                                        Conn.
     Name                 Collation     Limit   Tablespace           DB Size    Growth
     -------------------- ------------- ------- -------------------- ---------- ----------
     bench                C.UTF-8            -1 pg_default                80 GB    0 bytes
     postgres             C.UTF-8            -1 pg_default               135 MB    0 bytes
    
     Backend Wait Event Histogram
     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     Event                                          Class       Waits    <= 1us    <= 2us    <= 4us    <= 8us   <= 16us   <= 32us   <= 64us  <= 128us  <= 256us  <= 512us
     -------------------------------------- ------------- ----------- --------- --------- --------- --------- --------- --------- --------- --------- --------- --------
     WALInsert                                  LWLock             1         0         0         0         0         0         0         0         0         0         0
    
     Background Wait Event Histogram
     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     Event                                          Class       Waits    <= 1us    <= 2us    <= 4us    <= 8us   <= 16us   <= 32us   <= 64us  <= 128us  <= 256us  <= 512us
     -------------------------------------- ------------- ----------- --------- --------- --------- --------- --------- --------- --------- --------- --------- --------
     WALInsert                                  LWLock           542       107       174        39       113        93         8         1         1         0         1
    
     Write Ahead Log (WAL) Statistics
     --------------------------------
     Records       Full Page Images   Bytes        Buffers Full   Write         Sync          Write Time    Sync Time
     -----------   ----------------   -----------  ------------   -----------   -----------   -----------   -----------
         2936305                100     805989345             0             0             0             0             0
    
     Summary Stats (across all databases)
     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     Name                             Value
     -------------------------------- ----------------------------------
     Buffers evicted                  0
     Commits                          1216693
     ...
    
     Parameter Settings
     ~~~~~~~~~~~~~~~~~~~
     Parameter                         Value
     --------------------------------- --------------------------------------------------------------
     DateStyle                            ISO, MDY
     TimeZone                             UTC
     autovacuum                           on
     work_mem                             4096
    
     Columnar Engine available size  Columnar Engine configured size
     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                           14959MB                         19293MB
    
     Columnar Engine Statistics
     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     name                                                       count
     ---------------------------------------------------------- ------------
     CU Populations/Refreshes                                          13197
     CU Auto Refreshes                                                 10975
     ...
     Columnar Engine Ultra-fast Cache Statistics
     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     Ultra-fast Cache Size (MB):                        19200
     Ultra-fast Cache Used Size (MB):                       0
     Ultra-fast Cache Block Size (MB):                     80
    
     ----------------------------------------------------
     Created by G_STATS v1.0.100
     ----------------------------------------------------
    (xxx rows)
    
      

For information about report fields and performance optimization recommendations, see Database performance optimization recommendations. For more information about wait events in performance snapshot reports, see [Database performance snapshot report reference](https://docs.cloud.google.com/alloydb/docs/reference/database-performance-snapshot-report-reference).

## Delete a snapshot

Before you can delete snapshots that are part of an existing baseline, you must clear the baseline .

To delete a snapshot, run `SELECT perfsnap.delete(n)`. After you delete a snapshot, you can't recover it.

## Mark a snapshot as a performance baseline

To mark all snapshots with IDs between 1 and 3, for example, as a system performance baseline, run   
`SELECT perfsnap.make_baseline(1, 3)`.

## Clear performance baselines

To clear all baselines with IDs between 1 and 3, for example, run `SELECT perfsnap.clear_baseline(1, 3)`.

## Optimize database performance using snapshot report results

Follow these steps to optimize AlloyDB database performance:

  1. Create baseline snapshots when your database is idle or when it's experiencing an average load.
  2. Start the workload or query whose performance you want to improve.
  3. When the workload or query reaches peak resource usage, create another set of snapshots. We recommend that you use the same interval for both reports.
  4. Compare the reports that you created with both set of snapshots and identify changes that might improve performance. For more information about performance recommendations, see Database performance optimization recommendations.



### Database performance optimization recommendations

The following table lists performance snapshot report sections and recommended improvements for each report section. For more information about performance snapshot report sections and wait events, see [Database performance snapshot report reference](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/reference/database-performance-snapshot-report-reference).

**Section** | **Report field** | **Report field description** | **Optimization recommendations**  
---|---|---|---  
Snapshot details | Snapshot Details | Provides the host, PostgreSQL compatible release version, and the time when the machine is up and running. | N/A  
Snapshot ID | Lists the ID and the point-in-time of the snapshots that are used to create this report. | N/A  
System Insights | Host CPU | Host CPU utilization details.  | If the CPU utilization is greater than 80%, then we recommend that you move to a system with more vCPUs.  
Host Memory | Host memory utilization details. | If the free memory is less than 15%, then we recommend that you scale up to the next available size.  
Load Profile | Lists counters that help characterize your workload in terms of Write-Ahead Logging (WAL) generated, I/O requirements, and connection management. | If the physical reads are higher than logical reads, consider scaling up to the next available size to support larger caching of data.  
Response Time and Wait Class Breakdown | Breakdown of the time that Postgres processes spent during the workload run. | Focus your tuning on shortening I/O wait if the processes are mostly in a wait state, for example.  
Database workload Information | Per Database Workload Information | Key metrics for each database, including commits, rollbacks, hit ratio, and information about temporary tables and sort operations. | If rollbacks are high, consider diagnosing your app.  
Per Database DML and DQL Information | Counters for query operations.  | Qualify your workload as read-heavy or write-heavy.  
Database Conflict Information | Counters for common application and database issues. | Locate issues in your application if there is a deadlock.  
Database  
Sizing Information | Shows how much the database has grown during the interval between two snapshots. This field also shows if the database has connection limits established. | Locate issues in your application if database growth is too large.  
Vacuum Information | Vacuum Information | Details of I/O and counters for vacuum operations. | By default, AlloyDB performs adaptive vacuuming. You can override some of the vacuum settings to suit your workload. For example, reduce vacuum operations if too much I/O is spent on these requests.  
Per Database Vacuum Information | Shows the following information:  


  * Current age of `datfrozenxid` (oldest unfrozen XIDs) of each database, or the number of transactions from `datfrozenxid` to the current transaction's XID. 


  * Unfrozen transaction IDs consumed out of all transaction IDs. 


  * Result of `autovacuum_freeze_max_age - age(pg_database.datfrozenxid)`, which indicates the approximate age gaps (in transactions) at the second snapshot time, when autovacuum is triggered to prevent wraparounds on a database-aggregated level.

| If the age of the Frozen XID field is too old, or if the percentage of consumed transactions is close to 90%, consider vacuuming. If the aggregate vacuum gap decreases, this indicates that a vacuum will be enforced by Postgres to prevent wraparound.  
Database Processes Wait Details | Detailed Backend &  
Background Processes Information | Details of all the waits by backend & background processes in the report interval. Information includes the cumulative wait time, CPU time, and the average time per wait type. | To decrease the wait on WALWrite, for example, increase the number of `wal_buffers` available to the database.  
Detailed Backend & Background Wait Event Histogram | This is included in the performance snapshot report by default. The list contains the wait event histogram for backend & background processes, which are divided into 32 buckets, from 1 us to more than 16 secs. | Locate the wait events and determine if there are too many wait events on the larger wait time bucket. There might be a problem with too many wait events or with each consumed time of wait.  
Misc statistics | Write Ahead Log (WAL) Statistics | Summary of WAL statistics. | If you experience too much sync time, adjust the related database flags (GUC) to improve your workload. GUC is the PostgreSQL subsystem that handles server configuration.  
Summary Statistics (across all databases) | Summary of all database operations that occur during the snapshot interval. | N/A  
Parameter Settings | Parameter Settings | Key Postgres configuration parameters at the end snapshot time. | Check the GUC parameter settings (the Postgres database flags) to determine if the values aren't expected or aren't recommended.  
  
## Limitations

  * To avoid space bloat, you can manually create a maximum of 2500 snapshots on one instance. _Space bloat_ ensures that snapshots don't occupy too much storage space in your database.

  * If the number of snapshots exceeds the snapshot limit, then AlloyDB Omni deletes all manual snapshots older than 90 days. To remain within the snapshot limit, you must clean up unnecessary snapshots before you take a new one.

  * AlloyDB Omni periodically cleans up manual snapshots that are older than 90 days.




## What's next

  * Learn about [wait events in performance snapshot reports](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/reference/database-performance-snapshot-report-reference).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
