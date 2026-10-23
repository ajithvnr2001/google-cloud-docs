---
url: https://docs.cloud.google.com/alloydb/docs/optimize-database-performance-compare-snapshots/
title: Optimize database performance by comparing performance snapshots \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:43:10.878411+00:00
---

# Optimize database performance by comparing performance snapshots  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/optimize-database-performance-compare-snapshots/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Optimize database performance by comparing performance snapshots Stay organized with collections  Save and categorize content based on your preferences. 

To identify and mitigate AlloyDB for PostgreSQL database performance issues, you can compare snapshots of system metrics between two points in time by manually generating performance snapshot reports. The system metrics captured in each snapshot include virtual CPU (vCPU) usage, memory usage, disk I/O, transaction count, and wait events.

## Automatic and manual snapshots

AlloyDB supports the following snapshots:

  * **Automatic snapshots:** By default, AlloyDB automatically captures snapshots once a day and stores the snapshots for 7 days. Automatic snapshots help to generate reports with daily workload granularity. You can configure the frequency and retention of an automatic snapshot.

  * **Manual snapshots:** You can manually capture snapshots and generate reports.




You can mix and match automatic and manual snapshots to generate performance reports. For example, you can generate a performance snapshot report that compares a manually generated snapshot to an automatic snapshot.

This document describes how to manually generate performance snapshot reports.

## How performance snapshot reports work

Performance snapshot reports are a built-in AlloyDB tool that captures and analyzes performance data to help you identify the cause of performance issues. This tool complements other AlloyDB observability features like [systems insights](https://docs.cloud.google.com/alloydb/docs/monitor-instance), [query insights](https://docs.cloud.google.com/alloydb/docs/query-insights-overview), and the [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer), which provide real-time metrics about your instance.

Performance snapshot reports display database metrics between two timestamps in a single report. You can use the performance snapshot report information to identify performance issues with your performance snapshot report instance, like decreased database performance during certain times of the day or decreased performance over a certain time period. When used on a read pool node, the report helps identify if replication lag is caused by system resource constraints, such as CPU or memory, or specific query conflicts, such as buffer pins.

Using the performance snapshot report, you compare the metrics to a performance baseline to gain insights into workload performance metrics, which you can use to optimize or troubleshoot database performance. A _baseline_ is a customized set of database snapshots that measure the standard performance and behavior of a database for a specific configuration and workload.

For information about wait events in performance snapshot report, see [Database performance snapshot report reference](https://docs.cloud.google.com/alloydb/docs/reference/database-performance-snapshot-report-reference).

## Required roles

Ensure that you have the [`alloydbsuperuser` role](https://docs.cloud.google.com/alloydb/docs/database-users/about#predefined-role). By default, AlloyDB grants the `pg_monitor` role to `alloydbsuperuser`. For more information, see [PostgreSQL predefined roles](https://www.postgresql.org/docs/current/predefined-roles.html).

If you prefer to use your other self-defined roles, run `GRANT pg_monitor TO my_user` as `alloydbsuperuser` first. For more information, see [Update an Identity and Access Management (IAM) account with the appropriate role](https://docs.cloud.google.com/alloydb/docs/manage-iam-authn#role).

## Create snapshots

Performance snapshots are a powerful tool for understanding and optimizing your database performance. They capture key system metrics at a specific point in time, allowing you to compare the performance of your database between two points in time. AlloyDB supports two types of snapshots:

  * **Snapshots of system metrics:** these snapshots capture key system metrics such as vCPU usage, memory usage, and disk I/O.
  * **Snapshots of system metrics and SQL execution statistics:** these snapshots contain all the system metrics from a standard snapshot, plus detailed SQL execution statistics from the `pg_stat_statements` extension.



This gives you the flexibility to choose the level of detail you need for your analysis.

### Create a snapshot of system metrics

Create a snapshot at the beginning and end of the workload you're interested in. The time interval between the two snapshots should be long enough to capture a representative sample of the workload.

Follow these steps to optimize AlloyDB database performance:

  1. Create baseline snapshots when your database is idle or when it experiences an average load.
  2. [Connect a `psql` client to an AlloyDB instance](https://docs.cloud.google.com/alloydb/docs/connect-psql). For a read pool node, you must connect directly to its IP address. For more information, see [retrieve the list of Read Pool node IP addresses](https://docs.cloud.google.com/alloydb/docs/troubleshoot/read-pools#list-nodes).
  3. Run `SELECT perfsnap.snap()`. The output looks similar to the following:
         
         postgres=# select perfsnap.snap();
          snap
         ------
             1
         (1 row)
         

The output of this command returns the snapshot ID (`snap_id`), which is `1` in this example. You need this ID to generate a performance snapshot report later. The `snap_id` in your own environment is likely different.

  4. Compare the reports that you created with both set of snapshots and identify changes that might improve performance. For more information about performance recommendations, see Database performance optimization recommendations.




After you obtain metrics from the resulting performance snapshot report, you can take another set of snapshots and repeat the process.

### Create a snapshot that contains statistics of SQL execution

By default, AlloyDB uses the `pg_stat_statements` extension to track SQL statements. To include detailed SQL execution statistics in your performance report, you first need to create the `pg_stat_statements` extension in your `postgres` database. Note that the capture of these statistics is enabled by the `pg_stat_statements.track` flag, not by the creation of the extension itself.

To create a snapshot that also contains SQL execution statistics, follow these steps: 

  1. Create the `pg_stat_statements` extension in the `postgres` database. 
         
         postgres=# CREATE EXTENSION pg_stat_statements;
         

  2. Now, when you take a snapshot, it automatically includes the SQL statistics from `pg_stat_statements`. 
         
         postgres=# select perfsnap.snap();
             snap
           ------
               2
           (1 row)
           


**Note:** The output of `perfsnap.snap()` is the same as when creating a snapshot of only system metrics. However, with the `pg_stat_statements` extension enabled, the snapshot now contains detailed SQL execution statistics, which you can view when you generate a performance snapshot report. If you generate a report using snapshots that don't contain these statistics, the SQL statistics section of the report is empty. **Tip:** The query ID field in the report is from the snapshot of `pg_stat_statements`. However, the snapshots don't contain query text due to storage concerns. If at the time you generate the report, a query ID doesn't have a match in `pg_stat_statements`, this is expected if the query didn't run recently and is evicted from `pg_stat_statements`. 

## View a list of snapshots

  1. [Connect a `psql` client to an AlloyDB instance](https://docs.cloud.google.com/alloydb/docs/connect-psql). For a read pool node, you must connect directly to its IP address using `psql`. For more information, see [retrieve the list of Read Pool node IP addresses](https://docs.cloud.google.com/alloydb/docs/troubleshoot/read-pools#list-nodes).
  2. Run `SELECT * FROM perfsnap.g$snapshots`. The output looks similar to the following: 
         
         postgres=# select * from perfsnap.g$snapshots;
          snap_id |           snap_time           | instance_id  |               node_id           | snap_description  | snap_type | is_baseline
         ---------+-------------------------------+--------------+---------------------------------+-------------------+-----------+-------------
                1 | 2023-11-13 22:13:43.159237+00 | perf-primary | sab3-perf-primary-cab835ef-4cm8 | Manual snapshot   | Manual    | f
                2 | 2023-11-13 22:53:40.49565+00  | perf-primary | sab3-perf-primary-cab835ef-4cm8 | Automatic snapshot| Automatic | f
                3 | 2023-11-13 22:56:42.57094+00  | perf-replica | sab3-perf-replica-b9250422-tz4n | Automatic snapshot| Automatic | f
                4 | 2023-11-13 22:56:42.59476+00  | perf-replica | sab3-perf-replica-b9250422-63q3 | Automatic snapshot| Automatic | f
                5 | 2023-11-13 23:11:55.23157+00  | perf-replica | sab3-perf-replica-b9250422-tz4n | Manual snapshot   | Manual    | f
         (5 rows)


**Note:** To support basic metrics tracking, AlloyDB automatically takes a snapshot once a day. The `node_id` is reassigned following failover or maintenance events. **Tip:** Replication lag might delay updates to `perfsnap.g$snapshots` on the read pool. If you don't see an immediate update, query the primary instance, which is the source of truth. 

## Generate a performance snapshot report

To generate a report that captures the difference between two snapshots, for example, snapshots 1 and 2, run: 
    
    
    SELECT perfsnap.report(1,2)
    

The second snapshot in a differential operation doesn't need to immediately follow the first snapshot. However, make sure you capture the second snapshot in the differential after the first snapshot.

**Tip:** If you encounter an error like `ERROR: canceling statement due to statement timeout` when you generate the performance snapshot report, we recommend that you increase the statement timeout for the session by running `SET statement_timeout to 300000`. Substitute a timeout value that best suits your report generation needs. This example statement equals 5 minutes because the `statement_timeout` unit is defined in milliseconds. **Note:** To generate a valid report, the snapshots must originate from the same node. The system checks this by ensuring the `node_id` values match. Attempting to use snapshots from different nodes, for example, `node_id_1` and `node_id_2` trigger the following error: `ERROR: Unable to generate a report because snapshots are not from same node: begin_node_id: node_id_1, end_node_id: node_id_2`. 

The generated performance snapshot report looks similar to the following abridged example.

### Example report

The following is an abridged example of a generated performance snapshot report:

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
    
     SQL Report
     ~~~~~~~~~~
     NOTE: Query might be empty if query ID does not have a match in pg_stat_statements at report time. This is expected if the query is not run recently.
     Per Query Information (Top 50) By Total Elapsed Time
     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     Query Text                                                                                                 UserID         DBID          DBName          QueryID            Total Elapsed Time(ms)    Execution Count       Avg Elapsed Time(ms)
     ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        prepare neword (INTEGER, INTEGER, INTEGER, INTEGER, INTEGER) as select neword($1,$2,$3,$4,$5,$6)        36272        36274            tpcc      -5467151541922966497           276400877.8014            36928106                    7.4848
     prepare payment (INTEGER, INTEGER, INTEGER, INTEGER, INTEGER, INTEGER, NUMERIC, VARCHAR) AS select p        36272        36274            tpcc       3864683359055073968           127719636.4656            36928456                    3.4586
                                            prepare delivery (INTEGER, INTEGER) AS select delivery($1,$2)        36272        36274            tpcc       2323704420019807054            48540963.0880             3694128                   13.1400
                                        prepare slev (INTEGER, INTEGER, INTEGER) AS select slev($1,$2,$3)        36272        36274            tpcc      -8637448842172635004            35361366.9271             3692785                    9.5758
     ...
    
     Per Query Information (Top 50) By Read IO
     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     Query Text                                                                                                 UserID         DBID          DBName          QueryID            Total ReadIO Time(ms)        Execution Count    Avg ReadIO Time(ms)    Total buffer hits         Avg buffer hits    Total blk reads         Avg blk reads
     -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
     prepare ostat (INTEGER, INTEGER, INTEGER, INTEGER, VARCHAR) AS select * from ostat($1,$2,$3,$4,$5) a        36272        36274            tpcc      -1640504351418263816              498072.4004             3693895                    0.1348            80360201         21.75486877672484              105858 0.028657555236410347
                                            prepare delivery (INTEGER, INTEGER) AS select delivery($1,$2)        36272        36274            tpcc       2323704420019807054                  12.5438             3694128                    0.0000          4477308168        1212.0067761593534             1219908 0.33022894712906536
         prepare neword (INTEGER, INTEGER, INTEGER, INTEGER, INTEGER) as select neword($1,$2,$3,$4,$5,$6)        36272        36274            tpcc      -5467151541922966497                   0.8039            36928106                    0.0000         10337394097         279.9329620912592             6245570 0.16912781825312134
                  SELECT name, default_version, installed_version FROM pg_catalog.pg_available_extensions           10            5        postgres       6619165036968781114                   0.0000                 361                    0.0000                 361                         1                   0                   0
     ...
    
     Per Query Information (Top 50) By Standard Deviation of Elapsed Time
     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     Query Text                                                                                                 UserID         DBID          DBName          QueryID            Begin STDDEV Elapsed Time(ms)  End STDDEV Elapsed Time(ms)
     --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                               SELECT COUNT($1) FROM perfsnap.g$snapshots           10            5        postgres      -8741741796612173369                      17.8084                      18.1239
                                            prepare delivery (INTEGER, INTEGER) AS select delivery($1,$2)        36272        36274            tpcc       2323704420019807054                      15.0626                      19.8495
         prepare neword (INTEGER, INTEGER, INTEGER, INTEGER, INTEGER) as select neword($1,$2,$3,$4,$5,$6)        36272        36274            tpcc      -5467151541922966497                      13.9820                      17.0074
                                        prepare slev (INTEGER, INTEGER, INTEGER) AS select slev($1,$2,$3)        36272        36274            tpcc      -8637448842172635004                       8.4333                       9.6205
    
     ----------------------------------------------------
     Created by G_STATS v1.0.100
     ----------------------------------------------------
    (xxx rows)
    
      

For information about report fields and performance optimization recommendations, see Database performance optimization recommendations. For more information about wait events in performance snapshot reports, see [Database performance snapshot report reference](https://docs.cloud.google.com/alloydb/docs/reference/database-performance-snapshot-report-reference).

## Delete a snapshot

Before you can delete snapshots that are part of an existing baseline, you must clear the baseline.

To delete a snapshot, run the following command:
    
    
    SELECT perfsnap.delete(SNAP_ID);
    

Replace `SNAP_ID` with the ID of the snapshot that you want to delete.

After you delete a snapshot, you can't recover it.

## Mark a snapshot as a performance baseline

To mark all snapshots with IDs between 1 and 3, for example, as a system performance baseline, run   
`SELECT perfsnap.make_baseline(1, 3)`.

## Clear performance baselines

To clear all baselines with IDs between 1 and 3, for example, run `SELECT perfsnap.clear_baseline(1, 3)`.

## Modify the frequency of automated snapshots

Automated snapshots are taken for primary instance and read nodes once per day by default.

To customize the frequency of automated snapshots, set the `perfsnap.interval` flag, which sets the automatic snapshot interval in seconds. For more information, see [Configure database flags](https://docs.cloud.google.com/alloydb/docs/instance-configure-database-flags).

We recommend that you set the value of the flag to at least several minutes to capture meaningful information.

**Note:** AlloyDB doesn't take an automated snapshot when CPU utilization exceeds 70%. 

To optimize resource usage, when you no longer need the customized frequency, reset the flag to the default value, which is 86400 seconds per day.

## Modify the retention of automated snapshots

To customize the retention period of automated snapshots, set the `perfsnap.retention` flag, which sets the duration for which automatic snapshots are kept. For more information, see [Configure database flags](https://docs.cloud.google.com/alloydb/docs/instance-configure-database-flags).

The default retention period is `7 days`.

## Optimize database performance using snapshot report results

Follow these steps to optimize AlloyDB database performance:

  1. Create baseline snapshots when your database is idle or when it's experiencing an average load.
  2. Start the workload or query whose performance you want to improve.
  3. When the workload or query reaches peak resource usage, create another set of snapshots. We recommend that you use the same interval for both reports.
  4. Compare the reports that you created with both set of snapshots and identify changes that might improve performance. For more information about performance recommendations, see Database performance optimization recommendations.



### Database performance optimization recommendations

The following table lists performance snapshot report sections and recommended improvements for each report section. For more information about performance snapshot report sections and wait events, see [Database performance snapshot report reference](https://docs.cloud.google.com/alloydb/docs/reference/database-performance-snapshot-report-reference).

**Section** | **Report field** | **Report field description** | **Optimization recommendations**  
---|---|---|---  
Snapshot details | Snapshot Details | Provides the host, PostgreSQL compatible release version, and the time when the machine is up and running. | N/A  
Snapshot ID | Lists the ID and the point-in-time of the snapshots that are used to create this report. | N/A  
System Insights | Host CPU | Host CPU utilization details. | If the CPU utilization is greater than 80%, then we recommend that you scale up to the next available size. For read pool instances, ensure the node size is the same as or greater than the primary instance. Smaller read nodes may not be able to keep up with the primary's WAL generation rate during heavy write workloads.  
Host Memory | Host memory utilization details. | If the free memory is less than 15%, then we recommend that you scale up to the next available size. For read pool instances, ensure the node size is the same as or greater than the primary instance. Smaller read nodes may not be able to keep up with the primary's WAL generation rate during heavy write workloads.  
Load Profile | Lists counters that help qualify your workload of Write-Ahead Logging (WAL) generated, I/O requirements, and connection management. | If the physical reads are higher than logical reads, consider scaling up to the next available size to support larger caching of data.  
Response Time and Wait Class Breakdown | Breakdown of the time that Postgres processes spent during the workload run. | Focus your tuning on shortening I/O wait if the processes are mostly in a wait state, for example.  
Database workload Information | Per Database Workload Information | Key metrics for each database, including commits, rollbacks, hit ratio, and information about temporary tables and sort operations. | If rollbacks are high, consider diagnosing your app.  
Per Database DML and DQL Information | Counters for query operations. | Qualify your workload as read-heavy or write-heavy.  
Database Conflict Information | Counters for common application and database issues. | Locate issues in your application if there is a deadlock. If **Buffer Pins** conflicts are high on a read pool instance, consider reducing the `max_standby_streaming_delay` value to allow replay to proceed, or move long-running queries to a different read pool to avoid holding pins for extended durations.  
Database Sizing Information | Shows how much the database has grown during the interval between two snapshots. This field also shows if the database has connection limits established. | Locate issues in your application if database growth is too large.  
Vacuum Information | Vacuum Information | Details of I/O and counters for vacuum operations. | By default, AlloyDB performs adaptive vacuuming. You can override some of the vacuum settings to suit your workload. For example, reduce vacuum operations if too much I/O is spent on these requests.  
Per Database Vacuum Information | Shows the following information: 

  * Current age of `datfrozenxid` (oldest unfrozen XIDs) of each database, or the number of transactions from `datfrozenxid` to the current transaction's XID.
  * Unfrozen transaction IDs consumed out of all transaction IDs.
  * Result of `autovacuum_freeze_max_age - age(pg_database.datfrozenxid)`, which indicates the approximate age gaps (in transactions) at the second snapshot time, when autovacuum is triggered to prevent wraparounds on a database-aggregated level.

| If the age of the Frozen XID field is too old, or if the percentage of consumed transactions is close to 90%, consider vacuuming. If the aggregate vacuum gap decreases, this indicates that a vacuum will be enforced by Postgres to prevent wraparound.  
Database Processes Wait Details | Detailed Backend & Background Processes Information | Details of all the waits by backend & background processes in the report interval. Information includes the cumulative wait time, CPU time, and the average time per wait type. | To decrease the wait on WALWrite, for example, increase the number of `wal_buffers` available to the database.  
Detailed Backend & Background Wait Event Histogram | This is included in the performance snapshot report by default. The list contains the wait event histogram for backend & background processes, which are divided into 32 buckets, from 1 us to more than 16 secs. | Locate the wait events and determine if there are too many wait events on the larger wait time bucket. There might be a problem with too many wait events or with each consumed time of wait.  
Misc statistics | Write Ahead Log (WAL) Statistics | Summary of WAL statistics. | If you experience too much sync time, adjust the related database flags (GUC) to improve your workload. GUC is the PostgreSQL subsystem that handles server configuration.  
Summary Statistics (across all databases) | Summary of all database operations that occur during the snapshot interval. | N/A  
Parameter Settings | Parameter Settings | Key Postgres configuration parameters at the end snapshot time. | Check the GUC parameter settings (the Postgres database flags) to determine if the values aren't expected or aren't recommended. For read pool instances experiencing high replication lag, consider adjusting the following: 

  * `max_standby_streaming_delay`: tune this to balance query cancellation frequency versus replication lag.
  * `alloydb.promote_cancel_to_terminate`: ensure this is `on` to forcefully terminate backends that are unresponsive to cancellation and blocking recovery.
  * `google_storage.log_replay_throttle_read_transactions`: use this to prioritize replication catch-up over read query latency when lag exceeds thresholds.

  
SQL Execution statistics | Per query Information (Top 50) By Total Elapsed Time | Lists top 50 queries that have spent most time elapsed during the two snapshots, as well as their total execution count, broken down by the user and database where the query is issued.  
`Elapsed time = Difference of total_exec_time in pg_stat_statements at the two snapshot time` | Use this section to identify your heaviest query that takes most of system time.  
Per Query Information (Top 50) By Read IO | Lists top 50 queries that have spent most Read IO time during the two snapshots, as well as their execution count, buffer hits, blk reads, both in total and on average.  
`ReadIO = blk_read_time + temp_blk_read_time` accumulated during the two snapshots  
`Buffer Hits = shared_blks_hit + local_blks_hit` accumulated during the two snapshots  
`Buffer Reads = shared_blks_read + local_blks_read` accumulated during the two snapshots  
These fields are tracked by AlloyDB by default since `track_io_timing` is set. | Use this section to identify I/O intensive queries, especially if they need to read from disks frequently.  
Per Query Information (Top 50) By Standard Deviation of Elapsed Time | List top 50 queries that have highest standard deviation of elapsed time, listing standard deviations computed at both the begin and the end snapshot time.  
Here the value references `stddev_exec_time` from `pg_stat_statements` | For query with high standard deviation, it means the query execution time varies a lot, and it might be time to look at I/O.  
  
## Limitations

  * To prevent space bloat from excessive storage consumption, you can manually create a maximum of 2500 snapshots on one instance.

  * If the number of snapshots exceeds the snapshot limit, then AlloyDB deletes all manual snapshots older than 90 days. To remain within the snapshot limit, you must clean up unnecessary snapshots before you take a new one.

  * AlloyDB periodically cleans up manual snapshots that are older than 90 days.




## What's next

  * Learn about [wait events in performance snapshot reports](https://docs.cloud.google.com/alloydb/docs/reference/database-performance-snapshot-report-reference).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
