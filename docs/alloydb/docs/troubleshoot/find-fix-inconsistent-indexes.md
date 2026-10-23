---
url: https://docs.cloud.google.com/alloydb/docs/troubleshoot/find-fix-inconsistent-indexes/
title: Find and fix inconsistent indexes \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:14.650617+00:00
---

# Find and fix inconsistent indexes  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/troubleshoot/find-fix-inconsistent-indexes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Find and fix inconsistent indexes Stay organized with collections  Save and categorize content based on your preferences. 

Inconsistencies in database indexes can occur for a variety of reasons including software defects, hardware issues, or underlying changes in behavior such as sort order changes.

The PostgreSQL community has built tools to identify and remediate such issues. This includes tools like [`amcheck`](https://www.postgresql.org/docs/current/amcheck.html), which is recommended by the PostgreSQL community to identify consistency issues, including issues that earlier versions of PostgreSQL 14 exhibited.

This playbook is a reference for AlloyDB for PostgreSQL users who experience these consistency issues. The playbook provides information that helps PostgreSQL users identify and remediate inconsistent indexes.

Resolving an index's inconsistencies involves the following steps:

  1. Before you begin.

Before you begin reindexing, you should back up your database, set the correct permissions, verify your `psql` client version, and enable the `amcheck` extension.

  2. Check for inconsistent indexes.

One statement identifies unique and primary key violations, and another statement detects a variety of other inconsistencies.

  3. Fix the index's inconsistencies.

Reindexing an index fixes all its inconsistencies. You may need to adjust your instance's memory settings to improve performance.

  4. Monitor reindexing operations.

We recommend that you monitor the progress of the reindexing operation to ensure that the operation is progressing and is not blocked.

  5. Verify that the indexes are consistent.

After you have successfully reindexed your index, we recommend that you verify that your index does not contain any inconsistencies.




## Before you begin

### Back up your AlloyDB cluster's data

To ensure that no data is lost during reindexing, we recommend that you back up your cluster's data. For more information, see [Create an on-demand backup](https://docs.cloud.google.com/alloydb/docs/backup/create-on-demand).

**Caution:** If you restore the backup taken before the index inconsistency was fixed, it can reintroduce the inconsistency.

### Set the `alloydbsuperuser` permission

To complete the steps on this page, you must have `alloydbsuperuser` permissions. For more information see [AlloyDB's predefined PostgreSQL roles](https://docs.cloud.google.com/alloydb/docs/database-users/about#predefined-role).

### Ensure that the `psql` client version is 9.6 or higher

To complete the steps on this page, you must ensure that your `psql` client version is 9.6 or higher. Run the command `psql --version` to verify your current `psql` client version.

### Enable the amcheck extension

To check for index inconsistencies, you must enable the `amcheck` extension.

### Code Sample
    
    
      CREATE EXTENSION amcheck;
      

## Check for inconsistent indexes

The following sections describe how to check for inconsistent indexes by checking for an index's inconsistencies as well as unique and primary key violations.

### Check for inconsistencies

In each database, run the following statement to check for inconsistencies:

### Code Sample
    
    
    DO $$
    DECLARE
      r RECORD;
      version varchar(100);
    BEGIN
      RAISE NOTICE 'Started relhasindex validation on database: %', current_database();
      FOR r IN
        SELECT indexrelid::regclass relname
          FROM pg_index
        WHERE indrelid NOT IN (SELECT oid FROM pg_class WHERE relhasindex) LOOP
          RAISE LOG 'Failed to check index %: %', r.relname, 'relhasindex is false, want true';
          RAISE WARNING 'Failed to check index %: %', r.relname, 'relhasindex is false, want true';
      END LOOP;
      RAISE NOTICE 'Finished relhasindex validation on database: %', current_database();
    
      RAISE NOTICE 'Started b-tree amcheck on database: %', current_database();
      SHOW server_version into version;
      SELECT split_part(version, '.', 1) into version;
      FOR r IN
        SELECT c.oid, c.oid::regclass relname, i.indisunique
          FROM pg_index i
          JOIN pg_opclass op ON i.indclass[0] = op.oid
          JOIN pg_am am ON op.opcmethod = am.oid
          JOIN pg_class c ON i.indexrelid = c.oid
          JOIN pg_namespace n ON c.relnamespace = n.oid
         WHERE am.amname = 'btree'
           AND c.relpersistence != 't'
           AND c.relkind = 'i'
           AND i.indisready AND i.indisvalid LOOP
        BEGIN
          RAISE NOTICE 'Checking index %:', r.relname;
          PERFORM bt_index_check(index => r.oid, heapallindexed => r.indisunique);
        EXCEPTION
          WHEN undefined_function THEN
            RAISE EXCEPTION 'Failed to find the amcheck extension';
          WHEN OTHERS THEN
            RAISE LOG 'Failed to check index %: %', r.relname, sqlerrm;
            RAISE WARNING 'Failed to check index %: %', r.relname, sqlerrm;
            END;
      END LOOP;
      RAISE NOTICE 'Finished b-tree amcheck on database: %', current_database();
    END $$;

You should receive output similar to the following:

### Code Sample
    
    
      WARNING:  Failed to check index t_i_key: relhasindex is false, want true
      NOTICE:  Checking index t_pkey:
      NOTICE:  Checking index t_i_key:
      WARNING:  Failed to check index t_i_key: item order invariant violated for index "t_i_key"
      NOTICE:  Checking index t_j_key:
      WARNING:  Failed to check index t_j_key: item order invariant violated for index "t_j_key"
      NOTICE:  Checking index ij:
      WARNING:  Failed to check index ij: item order invariant violated for index "ij"

**Warning:** If your output doesn't contain WARNING notices, unique or key violations could still exist. To check for violations, perform the procedures in Identify and fix unique and primary key violations.

For more information about viewing logs, see [View logs by using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).

### Identify and fix unique and primary key violations

This section describes how to check your index for unique and primary key violations, and if some exist, how you fix them.

#### Identify unique key violations

Unique key violations must be fixed before you reindex an index. To check for all unique key violations, run the following command in each database:

### Code Sample
    
    
    WITH q AS (
        /* this gets info for all UNIQUE indexes */
        SELECT indexrelid::regclass as idxname,
               indrelid::regclass as tblname,
               indcollation,
               pg_get_indexdef(indexrelid),
               format('(%s)',(select string_agg(quote_ident(attname), ', ')
                  from pg_attribute a
                  join unnest(indkey) ia(nr) on ia.nr = a.attnum
                 where attrelid = indrelid)) as idxfields,
               COALESCE(substring(pg_get_indexdef(indexrelid) FROM '[)] (WHERE .*)$'), '') as whereclause
          FROM pg_index
         WHERE indisunique
         /* next line excludes indexes not affected by collation changes */
           AND trim(replace(indcollation::text, '0', '')) != ''
    )
    SELECT
     /* the format constructs the query to execute for each index */
     format(
    $sql$
    DO $$ BEGIN RAISE NOTICE 'checking index %3$I%2$I on table %1$I %4$I'; END;$$;
    SELECT this,
           prev,
           /* we detect both reversed ordering or just not unique */
           (CASE WHEN this = prev THEN 'DUPLICATE' ELSE 'BACKWARDS' END) as violation_type
      FROM (SELECT %2$s AS this,
                   lag(%2$s) OVER (ORDER BY %2$s) AS prev
              FROM %1$s %4$s
            ) s
     WHERE this <= prev and this IS NOT NULL and prev IS NOT NULL;  /* change to just '<' if looking for reverse order in index */
    $sql$, tblname, idxfields, idxname, whereclause
    )
      FROM q
    -- LIMIT 20 /* may use limit for testing */
    -- the next line tells psql to executes this query and then execute each returned line separately
    \gexec

The output of the script is similar to the following:

### Output
    
    
      NOTICE:  checking index=users_email_key on table=users key_columns="(email)"
      NOTICE:  checking index=games_title_key on table=games  key_columns="(title)"
              this        |        prev        | violation_type
      --------------------+--------------------+----------------
      Game #16 $soccer 2  | Game #16 $soccer 2 | DUPLICATE
      Game #18 $soccer 2  | Game #18 $soccer 2 | DUPLICATE
      Game #2 $soccer 2   | Game #2 $soccer 2  | DUPLICATE
      Game #5 $soccer 2   | Game #5 $soccer 2  | DUPLICATE

In this output, the table header `NOTICE` shows the index, column, and table for the values displayed below it. If your output contains rows displaying `DUPLICATE` or `BACKWARDS`, then this shows corruption in the index and may need to be fixed. Rows with `BACKWARDS` indicate possible duplicate values that might be hidden. If you see either of these entries in the table, see Fix duplicate key violations.

#### Fix duplicate key violations

If you have identified a duplicate unique index or if a reindex operation fails due to a duplicate key violation error, complete the following steps to find and remove the duplicate key(s).

**Note:** You need to repeat the following steps for each index that has key violations.

  1. Extract the `key_columns` from the `NOTICE` table header, as shown in the preceding sample output. In the following example, the key column is `email`.

### Output
         
         NOTICE:  checking index=users_email_key on table=users key_columns="(email)"

Use these values in KEY_COLUMNS in the query in step 3.

  2. Find the schema for your table. Use `psql` to connect to your database and run the following command:

### Code Sample
         
         \dt TABLE_NAME

The value in the `schema` column is the value you use for SCHEMA_NAME in the query in step 3. 

For example, for the following query:
         
         \dt games
          

The output is similar to the following:
         
         List of relations
          Schema  | Name  | Type  | Owner
          --------+-------+-------+----------
          public  | games | table | postgres
          (1 row)
          

  3. Run the following statements to force a full table scan and get duplicate keys.

### Code Sample
         
         SET enable_indexscan = off;
         SET enable_bitmapscan = off;
         SET enable_indexonlyscan = off;
         
         SELECT KEY_COLUMNS, count(*)
           FROM SCHEMA_NAME.TABLE_NAME
         GROUP BY KEY_COLUMNS
         HAVING count(*) > 1;

**Note:** If your database is large, this statement may take a long time to complete.

In the above statement, KEY_COLUMNS are one or more columns covered by the unique index or primary key in the table you are checking. These were identified when you checked for unique key violations. The statement returns the duplicate keys and a count of the duplicates for each.

For example, for the following query:
         
         SELECT name,count(*)
             FROM public.TEST_NAMES
           GROUP BY name
           HAVING count(*) > 1;
           

The output is similar to the following:
         
         name                | count
           --------------------+-------
           Johnny              |     2
           Peter               |     2
         (2 rows)

In this case, continue to the next step to remove the duplicate keys.

If any of the columns in KEY_COLUMNS are null, you can ignore them because unique constraints do not apply for NULL columns.

If no duplicate keys are found, you can move to Fix inconsistent indexes.

  4. Optional but recommended: Create a backup for the records containing duplicate keys. Run the following statement to create backup records:

### Code Sample
         
         CREATE TABLE SCHEMA_NAME.TABLE_NAME_bak
         AS SELECT * FROM SCHEMA_NAME.TABLE_NAME
         WHERE (KEY_COLUMNS)
         IN (KEY_VALUES);

In this statement, KEY_VALUES is a list of values copied from the result of the previous step. For example: 

### Code Sample
         
         CREATE TABLE public.TEST_NAMES_bak
           AS SELECT * FROM public.TEST_NAMES
           WHERE (name) IN (('Johnny'),('Peter'))
           

For a large number of rows, it is easier to replace the ((KEY_VALUES)) parameter in the `IN` statement with the `SELECT` statement from step 2 without the `count` parameter. For example:

### Code Sample
         
         CREATE TABLE SCHEMA_NAME.TABLE_NAME_bak
           AS SELECT * FROM SCHEMA_NAME.TABLE_NAME
           WHERE (KEY_COLUMNS)
           IN ( SELECT (KEY_COLUMNS)
           FROM SCHEMA_NAME.TABLE_NAME
           GROUP BY (KEY_COLUMNS)
           HAVING count(*) > 1);

  5. Add a replication role to the user to disable triggers:

### Code Sample
         
         ALTER USER CURRENT_USER with REPLICATION;
         SET session_replication_role = replica;

  6. Run the following statement to delete the duplicate keys:

### Code Sample
         
         BEGIN;
         
         DELETE FROM  SCHEMA_NAME.TABLE_NAME a
               USING  (
                       SELECT   min(ctid) AS ctid,
                               KEY_COLUMNS
                       FROM     SCHEMA_NAME.TABLE_NAME
                       GROUP BY KEY_COLUMNS
                               HAVING count(*) > 1 ) b
               WHERE a.KEY_COLUMNS = b.KEY_COLUMNS
               AND   a.ctid <> b.ctid;
           

For example, for multi-column KEY_COLUMNS:

### Code Sample
         
         DELETE FROM public.test_random a
               USING (
                      SELECT min(ctid) AS ctid,
                      day, rnum
               FROM public.test_random
               GROUP BY day, rnum
                      HAVING count(*) > 1 ) b
               WHERE a.day=b.day and a.rnum = b.rnum
               AND a.ctid <> b.ctid;

Where _day_ and _rnum_ are KEY_COLUMNS. 

Running this statement keeps one row and deletes others for each set of duplicate rows. If you want to control which version of the row gets deleted, run the following filter in the delete statement:

### Code Sample
         
         DELETE FROM  SCHEMA_NAME.TABLE_NAME
         WHERE ( KEY_COLUMNS, ctid) = (KEY_VALUES, CTID_VALUE);

**Warning:** Committing this transaction mutates your database and removes duplicate keys. Make sure that you don't delete any data that's still needed. Restoring from a backup might restore the inconsistent indexes.
  7. Complete the following steps to check that the `DELETE` command returned the expected number of rows without any errors:

     1. Run the following statement to identify the rows in which tables were changed:

### Code Sample
            
            SELECT schemaname, relname, n_tup_del, n_tup_upd
              FROM pg_stat_xact_all_tables
            WHERE n_tup_del+n_tup_upd > 0;

     2. If all the rows are correct, commit the `DELETE` transaction:

### Code Sample
            
            END;

     3. If there are errors, roll back the changes to fix the errors:

### Code Sample
            
            ROLLBACK;

  8. After the duplicate keys are deleted, you can reindex your index.

## Fix inconsistent indexes

The following sections describe how you can fix the index inconsistencies found in your instance.

**Note:** If your index has unique and primary key violations, you must fix these before reindexing.

Depending on how your database is configured, you may need to do the following for each index identified in the previous steps:

     1. Prepare to reindex your index.

     2. Reindex your index.

     3. If the reindex operation fails due to foreign key violations, you must [find and fix these violations](https://docs.cloud.google.com/alloydb/docs/troubleshoot/fix-foreign-keys).

     4. Run the reindex operation again.

### Prepare to reindex your index

#### Find the index size

Indexing larger databases requires more time than smaller databases. To improve the speed of index and reindex operations of larger databases, you can allocate more memory and CPU power to these operations. This is an important step in planning your reindex operation. After you know the index size, you can set the memory size used by the reindex operation and set the number of parallel workers.

Run the following statement to find the index size, in kilobytes, of the index that you want to fix:

### Code Sample
    
    SELECT i.relname                                      AS index_name,
           pg_size_pretty(pg_relation_size(x.indexrelid)) AS index_size
    FROM   pg_index x
           JOIN pg_class i
             ON i.oid = x.indexrelid
    WHERE  i.relname = 'INDEX_NAME';

The output of this statement is similar to the following:

### Output
    
    index_name | index_size
    ------------+------------
     my_index   | 16 kB
    (1 row)

#### Set memory size to use for reindexing

Based on the size of your index as determined in the previous section, it is important to set the appropriate value for the [`maintenance_work_mem`](https://www.postgresql.org/docs/17//runtime-config-resource.html#GUC-MAINTENANCE-WORK-MEM) configuration parameter. This parameter specifies the amount of memory to use for the reindexing operation. For example, if your index size is greater than 15 GB, we recommend that you adjust your maintenance memory.

The following example shows how to set `maintenance_work_mem`:

### Code Sample
    
    SET maintenance_work_mem TO "1GB";

**Note:** The value of `maintenance_work_mem` is set for each session. You don't need to restart your instance after changing the value. However, if you connect to the database again in a new session, the value from the previous setting is not saved.

Indexing larger databases requires more time than smaller databases. To improve the speed of index and reindex operations, we recommend setting `maintenance_work_mem` to at least 2% of the instance memory for instances with 4GB or more memory during this reindexing operation.

#### Set the number of parallel workers

You can increase the number of parallel workers for reindexing by setting the [`max_parallel_maintenance_workers`](https://www.postgresql.org/docs/current/runtime-config-resource.html#GUC-MAX-PARALLEL-MAINTENANCE-WORKERS) configuration parameter in the database. The default value of this parameter is 2 but can be set to a higher value to increase the number of workers for reindexing. For instances with 8 or more vCPU cores, we recommend setting the `max_parallel_maintenance_workers` flag value to 4.

The following shows how to identify the values set for these parameters:

### Code Sample
    
    SHOW max_parallel_maintenance_workers;
    SHOW max_worker_processes;
    SHOW max_parallel_workers;

The `max_parallel_maintenance_workers` parameter is a subset of `max_worker_processes` and limited by `max_parallel_workers`. If you require more parallel workers, increase the value of `max_worker_processes` and `max_parallel_workers`.

The following example shows how to set `max_parallel_maintenance_workers`:

### Code Sample
    
    SET max_parallel_maintenance_workers TO 4;

The `max_parallel_maintenance_workers` parameter does not guarantee the allocation of workers. To confirm that you have multiple parallel workers started by the reindexing, run the following query from another session after you have started the reindex:

### Code Sample
    
    SELECT
    leader.leader_pid,leader.pid "worker_pid",leader.query
    FROM
    pg_stat_activity leader, pg_stat_activity worker
    WHERE leader.leader_pid = worker.pid;

### Reindex your index

You can reindex an index without blocking your production workload using the `pg_repack` utility. This utility automates and simplifies the concurrent reindex process, enabling you to reindex without downtime. For this procedure, use `pg_repack` version 1.4.7.

Complete the following steps to reindex your index using `pg_repack`:

     1. Download, compile, and install the `pg_repack` utility from the [pg_repack page](https://reorg.github.io/pg_repack/).

     2. Create the `pg_repack` extension:

### Code Sample
            
            CREATE EXTENSION pg_repack;

     3. Run the following command to reindex your index concurrently:

### Code Sample
            
            pg_repack -h HOSTIP -p 5432 -U USERNAME -d "DATABASE_NAME" -i "INDEX_NAME" --no-superuser-check --no-kill-backend --wait-timeout=3600

**Note:** `pg_repack` does not allow you to reindex an index on a materialized view.

This command has output similar to the following:

### Output
            
            INFO: repacking index "public.t_i_key"

If any errors occurred when running `pg_repack`, you can correct the error and try again. After you have fixed all of your unique key indexes and primary key indexes, you should [check for foreign key violations](https://docs.cloud.google.com/alloydb/docs/troubleshoot/fix-foreign-keys) and fix any that are found.

### Find and fix foreign key violations

For information about how to find and fix foreign key violations, see [Find and fix foreign key violations](https://docs.cloud.google.com/alloydb/docs/troubleshoot/fix-foreign-keys).

## Monitor reindexing operations

Occasionally, the reindex operation may be blocked by other sessions. We recommended that you check this every 4 hours. If the reindex operation is blocked, you can cancel the blocking session so the reindex operation can complete.

Complete the following steps to identify blocking and waiting sessions and then cancel them in the INDEX operation:

     1. To identify blocking sessions, run the following query:

### Code Sample
            
            SELECT pid,
                  usename,
                  pg_blocking_pids(pid) AS blocked_by,
                  query                 AS blocked_query
            FROM   pg_stat_activity
            WHERE  cardinality(pg_blocking_pids(pid)) > 0;

     2. To cancel a session, run the following query using the PID of the blocking session from the previous query:

### Code Sample
            
            SELECT pg_cancel_backend(PID);

## Verify that your indexes are consistent

You must continue to check for index inconsistencies for each inconsistent index. After you have fixed all your instance's inconsistent indexes and key violations, you can check that no issues exist by following the steps in the previous sections:

     * Check for an index's inconsistencies

     * Check for unique key violations

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

     * ### Products and pricing

       * [ See all products ](https://cloud.google.com/products/)
       * [ Google Cloud pricing ](https://cloud.google.com/pricing/)
       * [ Google Cloud Marketplace ](https://cloud.google.com/marketplace/)
       * [ Contact sales ](https://cloud.google.com/contact/)
     * ### Support

       * [ Community forums ](https://discuss.google.dev/c/google-cloud/14/)
       * [ Support ](https://cloud.google.com/support-hub/)
       * [ Release Notes ](https://docs.cloud.google.com/release-notes)
       * [ System status ](https://status.cloud.google.com)
     * ### Resources

       * [ GitHub ](https://github.com/googlecloudPlatform/)
       * [ Getting Started with Google Cloud ](https://docs.cloud.google.com/docs/get-started/)
       * [ Code samples ](https://docs.cloud.google.com/docs/samples)
       * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture/)
       * [ Training and Certification ](https://cloud.google.com/learn/training/)
       * [ Builders Hub ](https://me.developers.google.com/)
     * ### Engage

       * [ Blog ](https://cloud.google.com/blog/)
       * [ Events ](https://cloud.google.com/events/)
       * [ X (Twitter) ](https://x.com/googlecloud)
       * [ Google Cloud on YouTube ](https://www.youtube.com/googlecloud)
       * [ Google Cloud Tech on YouTube ](https://www.youtube.com/googlecloudplatform)

[ ![Google Developers](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup-google-for-developers.svg)](https://developers.google.com/)
     * [ Android ](https://developer.android.com/)
     * [ Chrome ](https://developer.chrome.com/)
     * [ Firebase ](https://firebase.google.com/)
     * [ Google AI ](https://ai.google.com/)
     * [ About Google ](https://about.google/)
     * [ Privacy ](https://policies.google.com/privacy)
     * [ Site terms ](https://policies.google.com/terms?hl=en)
     * [ Google Cloud terms ](https://cloud.google.com/product-terms)
     * Manage cookies 
     * [ Our third decade of climate action: join us ](https://cloud.google.com/sustainability)
     * Sign up for the Google Cloud newsletter [ Subscribe ](https://cloud.google.com/newsletter/)
     * English
     * Deutsch
     * Español
     * Español – América Latina
     * Français
     * Indonesia
     * Italiano
     * Português
     * Português – Brasil
     * עברית
     * 中文 – 简体
     * 中文 – 繁體
     * 日本語
     * 한국어



