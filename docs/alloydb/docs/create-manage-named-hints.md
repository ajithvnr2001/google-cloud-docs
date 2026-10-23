---
url: https://docs.cloud.google.com/alloydb/docs/create-manage-named-hints/
title: Create and manage named hints \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:42:36.692479+00:00
---

# Create and manage named hints  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/create-manage-named-hints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Create and manage named hints Stay organized with collections  Save and categorize content based on your preferences. 

To control how the AlloyDB for PostgreSQL query planner generates execution plans without modifying your application queries, you can create, verify, view, enable, disable, and delete _named hints_. Named hints associate a query with a set of hints that specify details of the preferred execution plan. When the query planner generates an execution plan for the associated query, it applies the hints and automatically reapplies them on subsequent executions of the query. For example, you can use named hints to force an index scan instead of a sequential scan on a table, or to enforce a specific join order across multiple tables.

Named hints in AlloyDB support all the hints from the [open source `pg_hint_plan` extension](https://github.com/ossc-db/pg_hint_plan/blob/master/docs/hint_list.md) and the following hints for the [columnar engine](https://docs.cloud.google.com/alloydb/docs/columnar-engine/about):

  * `ColumnarScan(table)`: forces a columnar scan on the table.

  * `NoColumnarScan(table)`: disables a columnar scan on the table.




AlloyDB lets you create named hints for both parameterized queries and non-parameterized queries, which this document refers to as _parameter-sensitive queries_.

**Important:** Before using the named hints feature, consider the potential overhead it can add to the system performance. While named hints can resolve query plans with issues, they add extra time in query optimization to look up matching plans in the catalog and requests optimizer to apply multiple hints in the named hints. While the overheads are often negligible in complex queries, they might be significant in less complex queries. For example, in our internal testing, the extra query compilation time exceeded 10% for short-planning (less than 1 millisecond) queries.

## Workflow

Using named hints involves the following steps:

  1. Identify the query for which you want to create named hints.

  2. Create named hints with hints to be applied when the query is next executed.

  3. Verify the application of the named hints.




This page uses the following table and index for examples:
    
    
    CREATE TABLE t(a INT, b INT);
    CREATE INDEX t_idx1 ON t(a);
    

**Important:** If you used a previous version of the named hints feature, then you need to drop the previous `google_auto_hints` extension in all your databases using the following command:
    
    
      DROP EXTENSION IF EXISTS google_auto_hints;
    

To continue using the named hints that you created using an earlier version, recreate them by following the instructions in this page.

## Before you begin

  * Enable the named hints feature on your instance. Set the `alloydb.enable_named_hints` flag to `on`. You can enable this flag at the server-wide level or at the session level. To minimize overhead that might result from using this feature, enable this flag only at the session level.

For more information, see [Configure an instance's database flags](https://docs.cloud.google.com/alloydb/docs/instance-configure-database-flags#console).

**Note:** To force the same query plan on your read pool instance, enable the named hints feature on the read pool instance.

To verify that the flag is enabled, run the `show alloydb.enable_named_hints;` command. If the flag is enabled, the output returns "on".

  * For each database in which you want to use named hints, [create an extension](https://docs.cloud.google.com/alloydb/docs/instance-configure-extensions) in the database from the AlloyDB primary instance as the `alloydbsuperuser` or the `postgres` user:
        
        CREATE EXTENSION google_auto_hints CASCADE;
        




### Required roles

To get the permissions that you need to create and manage named hints, ask your administrator to grant you the following Identity and Access Management (IAM) roles:

  * [`alloydbsuperuser`](https://docs.cloud.google.com/alloydb/docs/database-users/about#predefined-role) role



While the default permission only allows the user with the `alloydbsuperuser` role to create named hints, you can optionally grant the write permission to the other users or roles of the database so that they can create named hints.
    
    
    GRANT INSERT,DELETE,UPDATE ON hint_plan.plan_patches, hint_plan.hints TO role_name;
    GRANT USAGE ON SEQUENCE hint_plan.hints_id_seq, hint_plan.plan_patches_id_seq TO role_name;
    

## Identify the query

You can use the query ID to identify the query whose default plan needs tuning. The query ID becomes available after at least one execution of the query.

Use the following methods to identify the query ID:

  * Run the `EXPLAIN (VERBOSE)` command, as shown in the following example:
        
        EXPLAIN (VERBOSE) SELECT * FROM t WHERE a = 99;
                                QUERY PLAN
        ----------------------------------------------------------
        Seq Scan on public.t  (cost=0.00..38.25 rows=11 width=8)
          Output: a, b
          Filter: (t.a = 99)
        Query Identifier: -6875839275481643436
        

In the output, the query ID is `-6875839275481643436`.

  * Query the `pg_stat_statements` view.

If you enabled the `pg_stat_statements` extension, you can find the query ID by querying the `pg_stat_statements` view, as shown in the following example:
        
        select query, queryid from pg_stat_statements;
        




## Create named hints

To create named hints, use the `google_create_named_hints()` function, which creates an association between the query and the hints in the database.
    
    
    SELECT google_create_named_hints(
    HINTS_NAME=>'HINTS_NAME',
    SQL_ID=>QUERY_ID,
    SQL_TEXT=>QUERY_TEXT,
    APPLICATION_NAME=>'APPLICATION_NAME',
    HINTS=>'HINTS',
    DISABLED=>DISABLED);
    

Replace the following:

  * `HINTS_NAME`: a name for the named hints. This must be unique within the database.
  * `SQL_ID` (Optional): query ID of the query for which you are creating the named hints.

You can use either the query ID or the query text—the `SQL_TEXT` parameter—to create named hints. However, we recommend that you use the query ID to create named hints because AlloyDB automatically locates the normalized query text based on the query ID.

  * `SQL_TEXT` (Optional): query text of the query for which you are creating the named hints.

When you use the query text, the text must be the same as the intended query, except for the literal and constant values in the query. Any mismatch, including case difference, can result in the named hints not being applied. To learn how to create named hints for queries with literals and constants, see Create parameter-sensitive named hints.

  * `APPLICATION_NAME` (Optional): name of the session client application for which you want to use the named hints. An empty string lets you apply the named hints to the query regardless of the client application issuing the query.

  * `HINTS`: a space-separated list of the hints for the query.

  * `DISABLED` (Optional): BOOL. If `TRUE`, initially creates the named hints initially as disabled.




Example:
    
    
    SELECT google_create_named_hints(
    HINTS_NAME=>'my_hint1',
    SQL_ID=>-6875839275481643436,
    SQL_TEXT=>NULL,
    APPLICATION_NAME=>'',
    HINTS=>'IndexScan(t)',
    DISABLED=>NULL);
    

This query creates a named hints named `my_hint1`. Its hint `IndexScan(t)` is applied by the planner to force an index scan on the table `t` on the next run of this example query.

After creating named hints, you can use the `google_named_hints_view` to confirm if the named hints is created, as shown in the following example:
    
    
    postgres=>\x
    postgres=>select * from google_named_hints_view limit 1;
    -[ RECORD 1 ]-----+-----------------------------
    hints_name | my_hint1
    sql_id | -6875839275481643436
    id | 9
    query_string | SELECT * FROM t WHERE a = ?;
    application_name |
    hints | IndexScan(t)
    disabled | f
    

After the named hints are created on the primary instance, they're automatically applied to the associated queries on the read pool instance, provided that you enabled the named hints feature on the read pool instance as well.

### Create parameter-sensitive named hints

By default, when named hints are created for a query, the associated query text is normalized by replacing any literal and constant value in the query text with a parameter marker, such as `?`. The named hints are then used for that normalized query even with a different value for the parameter marker.

For example, running the following query allows another query, such as `SELECT * FROM t WHERE a = 99;`, to use the named hints `my_hint2` by default.
    
    
    SELECT google_create_named_hints(
      HINTS_NAME=>'my_hint2',
      SQL_ID=>NULL,
      SQL_TEXT=>'SELECT * FROM t WHERE a = ?;',
      APPLICATION_NAME=>'',
      HINTS=>'SeqScan(t)',
      DISABLED=>NULL);
    

Then a query, such as `SELECT * FROM t WHERE a = 99;`, can use the named hints `my_hint2` by default.

AlloyDB also lets you create named hints for non-parameterized query texts, in which each literal and constant value in the query text is significant when matching queries.

When you apply parameter-sensitive named hints, two queries which only differ in the corresponding literal or constant values are also considered different. If you want to force plans for both queries, you must create separate named hints for each query. However, you can use different hints for the two named hints.

To create parameter-sensitive named hints, set the `SENSITIVE_TO_PARAM` parameter of the `google_create_named_hints()` function to `TRUE`, as shown in the following example:
    
    
    SELECT google_create_named_hints(
    HINTS_NAME=>'my_hint3',
    SQL_ID=>NULL,
    SQL_TEXT=>'SELECT * FROM t WHERE a = 88;',
    APPLICATION_NAME=>'',
    HINTS=>'IndexScan(t)',
    DISABLED=>NULL,
    SENSITIVE_TO_PARAM=>TRUE);
    

The query `SELECT * FROM t WHERE a = 99;` can't use the named hints `my_hint3`, because the literal value "99" doesn't match "88".

When you use parameter-sensitive named hints, consider the following:

  * Parameter-sensitive named hints don't support a mixture of literal and constant values and parameter markers in the query text.
  * When you create parameter-sensitive named hints and a default named hints for the same query, the parameter-sensitive named hints are preferred over the default named hints.
  * If you want to use the query ID to create parameter-sensitive named hints, make sure that the query executed in the current session. The parameter values from the most recent execution (in the current session) are used to create the named hints.



## Verify the application of the named hints

After you create the named hints, use the following methods to verify that the query plan is forced accordingly.

  * Use the `EXPLAIN` command or the `EXPLAIN (ANALYZE)` command.

To view the hints that the planner is trying to apply, you can set the following flags at the session level before you run the `EXPLAIN` command:
        
        SET pg_hint_plan.debug_print = ON;
        SET client_min_messages = LOG;
        

  * Use the [`auto_explain`](https://docs.cloud.google.com/alloydb/docs/reference/extensions) extension.




## Manage named hints

AlloyDB lets you view, enable and disable, and delete named hints.

### View named hints

To view existing named hints, use the `google_named_hints_view` function, as shown in the following example:
    
    
    postgres=>\x
    postgres=>select * from google_named_hints_view limit 1;
    -[ RECORD 1 ]-----+-----------------------------
    hints_name | my_hint1
    sql_id | -6875839275481643436
    id | 9
    query_string | SELECT * FROM t WHERE a = ?;
    application_name |
    hints | IndexScan(t)
    disabled | f
    

### Enable named hints

To enable existing named hints, use the `google_enable_named_hints(HINTS_NAME)` function. By default, named hints are enabled when you create them.

For example, to re-enable the previously disabled named hints `my_hint1` from the database, run the following function:
    
    
    SELECT google_enable_named_hints('my_hint1');
    

### Disable named hints

To disable existing named hints, use the `google_disable_named_hints(HINTS_NAME)` function.

For example, to delete the example named hints `my_hint1` from the database, run the following function:
    
    
    SELECT google_disable_named_hints('my_hint1');
    

### Delete named hints

To delete named hints, use the `google_delete_named_hints(HINTS_NAME)` function.

For example, to delete the example named hints `my_hint1` from the database, run the following function:
    
    
    SELECT google_delete_named_hints('my_hint1');
    

## Disable the named hints feature

To disable the named hints feature on your instance, set the `alloydb.enable_named_hints` flag to `off`. For more information, see [Configure an instance's database flags](https://docs.cloud.google.com/alloydb/docs/instance-configure-database-flags#console).

## Limitations

Using named hints have the following limitations:

  * When you use a query ID to create named hints, the original query text has a length limitation of 2048 characters.
  * Given the semantics of a complex query, not all hints and their combinations can be fully applied. We recommend that you test the intended hints on your queries before you deploy named hints in production.
  * Forcing join orders for complex queries is limited.
  * Using named hints to influence plan selection can interfere with future AlloyDB optimizer improvements. Make sure that you revisit the choice of using named hints and accordingly adjust the named hints when the following events occur:

    * There's a significant change in workload.
    * A new AlloyDB rollout or upgrade involving optimizer changes and improvements is available.
    * Other query tuning methods are applied to the same queries.
    * The use of named hints adds significant overhead to system performance.



For more information about limitations, see the [`pg_hint_plan` documentation](https://github.com/ossc-db/pg_hint_plan/blob/master/docs/functional_limitations.md).

## What's Next

  * [Learn about the AlloyDB columnar engine](https://docs.cloud.google.com/alloydb/docs/columnar-engine/about)
  * [Use the index advisor with Query Insights](https://docs.cloud.google.com/alloydb/docs/use-index-advisor-with-query-insights)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
