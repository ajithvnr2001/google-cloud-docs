---
url: https://docs.cloud.google.com/sql/docs/postgres/txid-wraparound/
title: Overcome transaction ID (TXID) wraparound protection \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:30:07.410590+00:00
---

# Overcome transaction ID (TXID) wraparound protection  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/txid-wraparound/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Overcome transaction ID (TXID) wraparound protection Stay organized with collections  Save and categorize content based on your preferences. 

This page describes what you can do when your database runs into Transaction ID Wraparound protection in PostgreSQL. It manifests as an `ERROR` message, as follows:
    
    
    database is not accepting commands to avoid wraparound data loss in database
    dbname.
    
    Stop the postmaster and vacuum that database in single-user mode.
    
    You might also need to commit or roll back old prepared transactions, or drop
    stale replication slots.

Alternatively, a `WARNING` message as follows might appear:
    
    
    database dbname must be vacuumed within 10985967 transactions.
    
    To avoid a database shutdown, execute a database-wide VACUUM in that database.

**Important:** The error message "Stop the postmaster and vacuum that database in single-user mode." is an outdated error from before PostgreSQL v.8.3 when this was actually true. In most cases, you don't have to switch to single-user mode. Instead, you can run the required `VACUUM` commands and perform tuning for `VACUUM` to run fast.

By default, you can't run any data manipulation language (DML), but you can still run `VACUUM`.

### Flag `cloudsql.enable_maintenance_mode` 

By default, you can't run any DDL or DML once the database is 'in wraparound' but Cloud SQL for PostgreSQL offers an emergency maintenance mode which gives you 500,000 more transaction IDs to use to get out of the situation without the need to restart the server in single-user mode.

To activate maintenance mode, set `cloudsql.enable_maintenance_mode` to `on` in the database session before using any commands requiring a transaction ID.
    
    
    SET cloudsql.enable_maintenance_mode = 'on';
    [ your SQL, DML or DDL commands here ]
    

This needs to be done in the session where you're performing the maintenance before you do anything requiring a transaction ID.

## Overview of steps

  * Find out which database and which tables are causing the wraparound.
  * Check if there's anything holding back (AUTO)VACUUM (for example, a stuck transaction ID).
  * Measure the speed of AUTOVACUUM. If it is slow, optionally, you can try to speed it up.
  * If needed, run a few more VACUUM commands manually.
  * Investigate other ways to speed up the vacuum. Sometimes the fastest way is to drop the table or some indexes.



Many of the recommendations for values of flags are purposefully not exact because they depend on many database parameters. Read the documents linked at the end of this page for a deeper analysis on this topic.

## Find the database and table causing the wraparound

### Finding the database

To find out which database or databases contain the tables that are causing the wraparound, run the following query:
    
    
    SELECT datname, 
           age(datfrozenxid), 
           2^31-1000000-age(datfrozenxid) as remaining
      FROM pg_database
     ORDER BY 3
    

The database with the `remaining` value close to 0 is the one causing the problem.

### Finding the table

Connect to that database and run the following query:
    
    
    SELECT c.relnamespace::regnamespace as schema_name,
           c.relname as table_name,
           greatest(age(c.relfrozenxid),age(t.relfrozenxid)) as age,
           2^31-1000000-greatest(age(c.relfrozenxid),age(t.relfrozenxid)) as remaining
      FROM pg_class c
      LEFT JOIN pg_class t ON c.reltoastrelid = t.oid
     WHERE c.relkind IN ('r', 'm')
     ORDER BY 4;
    

This query returns the table or tables causing the problem.

### For TEMPORARY tables

If the `schema_name` starts with `pg_temp_`, then the only way to resolve the problem is to drop the table because PostgreSQL doesn't let you VACUUM temporary tables created in other sessions. Sometimes if that session is open and accessible, you can vacuum the table there, but this is often not the case. Use the following SQL statements to drop the temp table:
    
    
    SET cloudsql.enable_maintenance_mode = 'on'; /* get extra transaction ids */
    DROP TABLE pg_temp_<N>.<tablename>;
    

If this was the only blocker, then in about a minute, the autovacuum picks up this change and moves the `datfrozenxid` forward in `pg_database`. This resolves the wraparound protection read-only state.

### Normal tables

For normal (that is non-temporary) tables, continue with the next steps below here to see if anything is blocking the clean-up, if the VACUUM is running fast enough, and it the most important table is being vacuumed.

## Check for a stuck transaction ID

One possible reason why the system can run out of transaction IDs is that PostgreSQL can't _freeze_ (that is, mark as visible to all transactions) any transaction IDs created after the oldest currently running transaction started. This is because of multiversion concurrency control (MVCC) rules. In extreme cases, such transactions can become so old that they make it impossible for VACUUM to clean up any old transactions for the entire 2 billion transaction ID wraparound limit and cause the whole system to stop accepting new DML. You typically also see warnings in the log file, saying `WARNING: oldest xmin is far in the past`.

You should move on to optimization only after the stuck transaction ID has been remediated.

Here are four potential reasons why there might be a stuck transaction ID, with information on how to mitigate each of them:

  * **Long running transactions:** Identify them and cancel or terminate the backend to unblock the vacuum.
  * **Orphaned prepare transactions:** Roll back these transactions.
  * **Abandoned replication slots:** Drop the abandoned slots.
  * **Long running transaction on replica, with`hot_standby_feedback = on`:** Identify them and cancel or terminate the backend to unblock the vacuum.



For these scenarios, the following query returns the age of the oldest transaction and the number of transactions left until wraparound:
    
    
     WITH q AS (
    SELECT
      (SELECT max(age(backend_xmin))
          FROM pg_stat_activity  WHERE state != 'idle' )       AS oldest_running_xact_age,
      (SELECT max(age(transaction)) FROM pg_prepared_xacts)    AS oldest_prepared_xact_age,
      (SELECT max(greatest(age(catalog_xmin),age(xmin))) FROM pg_replication_slots)        AS oldest_replication_slot_age,
      (SELECT max(age(backend_xmin)) FROM pg_stat_replication) AS oldest_replica_xact_age
    )
    SELECT *,
           2^31 - oldest_running_xact_age AS oldest_running_xact_left,
           2^31 - oldest_prepared_xact_age AS oldest_prepared_xact_left,
           2^31 - oldest_replication_slot_age AS oldest_replication_slot_left,
           2^31 - oldest_replica_xact_age AS oldest_replica_xact_left
    FROM q;

This query might return any of the _*_left_ values reported close to or less than 1 million away from wraparound. This value is the wraparound protection limit when PostgreSQL stops accepting new write commands. In this case, see either Remove VACUUM blockers or Tune VACUUM.

For example, the preceding query might return:
    
    
    ┌─[ RECORD 1 ]─────────────────┬────────────┐
    │ oldest_running_xact_age      │ 2146483655 │
    │ oldest_prepared_xact_age     │ 2146483655 │
    │ oldest_replication_slot_age  │ ¤          │
    │ oldest_replica_xact_age      │ ¤          │
    │ oldest_running_xact_left     │ 999993     │
    │ oldest_prepared_xact_left    │ 999993     │
    │ oldest_replication_slot_left │ ¤          │
    │ oldest_replica_xact_left     │ ¤          │
    └──────────────────────────────┴────────────┘

where `oldest_running_xact_left` and `oldest_prepared_xact_left` are within the 1 million wraparound protection limit. In this case, you must first remove the blockers for the VACUUM to be able to proceed.

## Remove VACUUM blockers

### Long-running transactions

In the preceding query, if `oldest_running_xact` is equal to `oldest_prepared_xact`, then go to the  Orphaned prepare transaction section, because the _latest running_ value includes also the prepared transactions.

You might first need to run the following command as the `postgres`user: 
    
    
    GRANT pg_signal_backend TO postgres;

If the offending transaction belongs to any of the system users (starting with `cloudsql...`), you can't cancel it directly. You must restart the database to cancel it.

To identify a long-running query, and cancel or terminate it to unblock the vacuum, first select a few of the oldest queries. The `LIMIT 10` line helps fit the result on the screen. You might need to repeat this after resolving the oldest running queries.
    
    
    SELECT pid,
           age(backend_xid) AS age_in_xids,
           now() - xact_start AS xact_age,
           now() - query_start AS query_age,
           state,
           query
     FROM pg_stat_activity
     WHERE state != 'idle'
     ORDER BY 2 DESC
     LIMIT 10;

If `age_in_xids` comes back as `NULL`, this means the transaction has not been allocated a permanent transaction ID and can be safely ignored.

Cancel the queries where the `xids_left_to_wraparound` is approaching 1M.

If `state` is `active`, then the query can be cancelled using `SELECT pg_cancel_backend(pid);`. Otherwise, you need to terminate the whole connection using `SELECT pg_terminate_backend(pid);`, where pid is the `pid` from the previous query

### Orphaned prepare transactions

**Note:** To commit a prepared transaction, you must be connected as the same user that originally executed the transaction. See the field `owner` in the following table. DB_NAME is the name of the database in your `pg_stat_progress_vacuum` view.

List all prepared transactions:
    
    
    DB_NAME=> SELECT age(transaction),* FROM pg_prepared_xacts ;
    ┌─[ RECORD 1 ]┬───────────────────────────────┐
    │ age         │ 2146483656                    │
    │ transaction │ 2455493932                    │
    │ gid         │ trx_id_pin                    │
    │ prepared    │ 2021-03-03 16:54:07.923158+00 │
    │ owner       │ postgres                      │
    │ database    │ DB_NAME                       │
    └─────────────┴───────────────────────────────┘

Roll back the oldest orphaned prepared transaction(s) by using the `gid` from the last query (in this case, `trx_id_pin`) as the transaction ID:
    
    
    ROLLBACK PREPARED trx_id_pin;
    

Alternatively, commit it: 
    
    
    COMMIT PREPARED trx_id_pin;
    

See the [SQL ROLLBACK PREPARED](https://www.postgresql.org/docs/13/sql-rollback-prepared.html) documentation for a full explanation.

### Abandoned replication slots

In case the replication slot is abandoned because the existing replica is either stopped, paused, or has some other issue, you can delete the replica from `gcloud` or Google Cloud console.

First, check that the replica is not disabled as described in [Managing read replicas](https://docs.cloud.google.com/sql/docs/postgres/replication/manage-replicas). If the replica is disabled, enable it again. If the lag still stays high, delete the replica,

The replication slots are visible in the `pg_replication_slots` system view.

The following query fetches the relevant info:
    
    
    SELECT *, age(xmin) AS age FROM pg_replication_slots;
    ┌─[ RECORD 1 ]────────┬─────────────────────────────────────────────────┐
    │ slot_name           │ cloudsql_1_355b114b_9ff4_4bc3_ac88_6a80199bd738 │
    │ plugin              │ ¤                                               │
    │ slot_type           │ physical                                        │
    │ datoid              │ ¤                                               │
    │ database            │ ¤                                               │
    │ active              │ t                                               │
    │ active_pid          │ 1126                                            │
    │ xmin                │ 2453745071                                      │
    │ catalog_xmin        │ ¤                                               │
    │ restart_lsn         │ C0/BEF7C2D0                                     │
    │ confirmed_flush_lsn │ ¤                                               │
    │ age                 │ 59                                              │
    └─────────────────────┴─────────────────────────────────────────────────┘

In this example, the `pg_replication_slots` value is healthy (age == 59). If the age was near 2 billion, you would want to delete the slot. There is no easy way to know which replica is which in case the query returns multiple records. So, check them all in case there is a long-running transaction on any replica.

### Long-running transactions on replicas

Check replicas for the oldest running transaction with `hot_standby_feedback` set to `on` and disable it on the replica.

The `backend_xmin` column in the `pg_stat_replication` view has the oldest `TXID` needed on the replica.

To move it forward, stop the query that holds it back on the replica. To discover which query is holding it back, use the query in Long running transactions, but this time, run it on the replica.

Another option is to restart the replica.

## Configure VACUUM

Set the following two flags:

  * autovacuum_vacuum_cost_delay = 0
  * autovacuum_work_mem = 1048576



The first disables any disk throttling for vacuuming by PostgreSQL so VACUUM can run at full speed. By default, autovacuum is throttled so it does not use up all disk IO on the slowest servers.

The second flag, `autovacuum_work_mem`, decreases the number of index cleanup passes. If possible, it should be large enough to store all IDs of dead rows in a table that VACUUM is going to clean up. When setting this value, consider that this is the maximum amount of local memory each running VACUUM can allocate. Make sure that you're not allowing more than is available, with some left in reserve. If you leave the database running in read-only mode, then also consider the local memory used for read-only queries.

On most systems, use the maximum value (1 GB or 1048576 kB, as shown in the sample). This value fits up to about 178 million dead tuples. Any more still causes multiple index scan passes.

These and other flags are explained in more detail in [Optimizing, monitoring, and troubleshooting VACUUM operations in PostgreSQL](https://docs.cloud.google.com/solutions/optimizing-monitoring-troubleshooting-vacuum-operations-postgresql).

After setting these flags, restart the database so that autovacuum starts with the new values.

You can use the `pg_stat_progress_vacuum` view to monitor the progress of autovacuum-started VACUUMs. This view shows VACUUMs running in all databases, and for tables (relations) from other databases that you can't look up the table name using the view column `relid`.

To identify the databases and tables that need vacuuming next, use queries from [Optimizing, monitoring, and troubleshooting VACUUM operations in PostgreSQL](https://docs.cloud.google.com/solutions/optimizing-monitoring-troubleshooting-vacuum-operations-postgresql). If the server VM is powerful enough and has the bandwidth for more parallel VACUUM processes than started by autovacuum, you can start some manual vacuums.

## Check VACUUM speed

This section describes how to check VACUUM speed and how to accelerate it, if needed.

### Check running autovacuums

All backends running VACUUM are visible in the system view [pg_stat_progress_vacuum](https://www.postgresql.org/docs/11/progress-reporting.html).

If the current phase is `scanning heap`, then you can monitor progress by watching changes in the column `heap_blks_scanned`. Unfortunately, there is no easy way to determine scan speed in other phases.

### Estimate the VACUUM scan speed

To estimate the scan speed, you need to first store the base values and then calculate the change over time to estimate the completion time. First, you need to save a snapshot of `heap_blks_scanned` together with a timestamp by using the following snapshot query:
    
    
    SELECT set_config('save.ts', clock_timestamp()::text, false),
           set_config('save.heap_blks_scanned', heap_blks_scanned::text, false)
    FROM pg_stat_progress_vacuum
    WHERE datname = 'DB_NAME';

Since we can't save anything in tables that are already in wraparound, use `set_config(flag, value)` to set two user-defined flags - `save.ts` and `save.heap_blks_scanned` \- to the current values from `pg_stat_progress_vacuum`.

In the next query, we use these two as the comparison base to determine speed and estimate completion time.

NOTE: `WHERE datname = DB_NAME` restricts the investigation to one database at a time. This number is enough if there is only one autovacuum running in this database, with more than one row per database. Extra filter conditions `('AND relid= …'')` need to be added to WHERE to indicate a single autovacuum row. This is also true for the next query.

Once you've saved the base values, you can run the following query:
    
    
    with q as (
        SELECT datname,
               phase,
               heap_blks_total,
               heap_blks_scanned,
               clock_timestamp() - current_setting('save.ts')::timestamp AS ts_delta,
               heap_blks_scanned - current_setting('save.heap_blks_scanned')::bigint AS scanned_delta
         FROM pg_stat_progress_vacuum
         WHERE datname = DB_NAME
    ), q2 AS (
    SELECT *,
           scanned_delta / extract('epoch' FROM ts_delta) AS pages_per_second
      FROM q
    )
    SELECT *,
           (heap_blks_total - heap_blks_scanned) / pages_per_second AS remaining_time
      FROM q2
    ;
    
    
    ┌─[ RECORD 1 ]──────┬──────────────────┐
    │ datname           │ DB_NAME          │
    │ phase             │ scanning heap    │
    │ heap_blks_total   │ 9497174          │
    │ heap_blks_scanned │ 18016            │
    │ ts_delta          │ 00:00:40.30126   │
    │ as_scanned_delta  │ 11642            │
    │ pages_per_second  │ 288.87434288655  │
    │ remaining_time    │ 32814.1222418038 │
    └───────────────────┴──────────────────┘

This query compares the current values to the save base values and calculates `pages_per_second` and `remaining_time`, which lets us decide if VACUUM is running fast enough or if we want to speed it up. The `remaining_time` value is only for the `scanning heap` phase. Other phases also take time, sometimes even more. You can [read more on vacuuming](https://www.postgresql.org/docs/13/sql-vacuum.html) and view blog posts on the internet discussing some of the complex aspects of vacuum.

## Speed up VACUUM

The easiest and fastest way to make VACUUM scan faster is setting `autovacuum_vacuum_cost_delay=0`. This can be done from the Google Cloud console.

Unfortunately, the already running VACUUM does not pick up this value and you might need to restart the database.

After a restart, you might see a result similar to the following:
    
    
    ┌─[ RECORD 1 ]──────┬──────────────────┐
    │ datname           │ DB_NAME          │
    │ phase             │ scanning heap    │
    │ heap_blks_total   │ 9497174          │
    │ heap_blks_scanned │ 222382           │
    │ ts_delta          │ 00:00:21.422615  │
    │ as_scanned_delta  │ 138235           │
    │ pages_per_second  │ 6452.76031894332 │
    │ remaining_time    │ 1437.33713040171 │
    └───────────────────┴──────────────────┘

In this sample, the speed increased from <300 pages/sec to ~6500 pages/sec, and the expected remaining time for the heap scanning phase decreased from 9 hours to 23 minutes.

The scan speed of the other phases is not as easy to measure, but they should show a similar speedup.

Also consider making `autovacuum_work_mem` as large as possible to avoid multiple passes over indexes. An index pass happens each time the memory is filled with dead tuple pointers.

If the database is not being used otherwise, set `autovacuum_work_mem` to have ~80% of memory free after allowing the required amount for `shared_buffers`. This is the upper limit for each of the autovacuum-started VACUUM processes. If you want to continue running read-only workloads, use less memory.

## Other ways to improve speed

### Avoid vacuuming indexes

For huge tables, VACUUM spends most of the time cleaning up indexes.

PostgreSQL 14 has special optimizations for avoiding index cleanup if the system is in danger of wraparound.

In PostgreSQL 12 and 13, you can manually run the following statement:
    
    
    VACUUM (INDEX_CLEANUP OFF, TRUNCATE OFF) <tablename>;
    

In versions 11 and older, you can `DROP` the index before running vacuum and recreate it later.

Dropping the index when an autovacuum is already running on that table requires cancelling the running vacuum and then immediately executing the drop index command before the autovacuum manages to start vacuum on that table again.

First, run the following statement to find the PID of the autovacuum process you need to terminate:
    
    
    SELECT pid, query 
      FROM pg_stat_activity
     WHERE state != 'idle'
       AND query ilike '%vacuum%';
    

Then run the following statements to terminate the running vacuum and drop one or more indexes:
    
    
    SET cloudsql.enable_maintenance_mode = 'on'; /* get extra transaction ids */
    SELECT pg_terminate_backend(<pid>);DROP INDEX <index1>;DROP INDEX <index2>; ...
    

### Drop the offending table

In some rare cases, you can drop the table. For example, if it's a table that's easy to restore from another source like a backup or other database.

You still need to use `cloudsql.enable_maintenance_mode = 'on'` and likely also terminate the VACUUM on that table as shown in the previous section.

### VACUUM FULL

In rare cases, it's faster to run `VACUUM FULL FREEZE`, usually when the table has only a small proportion of live tuples. This can be checked from the `pg_stat_user_tables` view (unless there has been a crash which has wiped out the statistics).

The `VACUUM FULL` command copies live tuples to a new file, so enough space has to be available for the new file and its indexes.

## What's next

  * Learn more about [VACUUM for wraparound](https://www.postgresql.org/docs/current/routine-vacuuming.html#VACUUM-FOR-WRAPAROUND)
  * Learn more about [routine vacuuming](https://www.postgresql.org/docs/current/routine-vacuuming.html).
  * Learn more about [automatic vacuuming](https://www.postgresql.org/docs/current/runtime-config-autovacuum.html)
  * Learn more about [ Optimizing, monitoring, and troubleshooting VACUUM operations in PostgreSQL](https://cloud.google.com/solutions/optimizing-monitoring-troubleshooting-vacuum-operations-postgresql)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
