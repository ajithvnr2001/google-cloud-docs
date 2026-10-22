---
url: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/columnar-engine/add-frequent-expressions/
title: Optimize queries with virtual columns for expressions \u00a0|\u00a0 AlloyDB Omni using the RPM orchestrator: Current (18.4.0) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:38:38.908795+00:00
---

# Optimize queries with virtual columns for expressions  |  AlloyDB Omni using the RPM orchestrator: Current (18.4.0)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/columnar-engine/add-frequent-expressions/

This page documents AlloyDB Omni version **18.4.0** using the **RPM orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM orchestrator: Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/overview)



Send feedback 

#  Optimize queries with virtual columns for expressions Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.4.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/columnar-engine/add-frequent-expressions)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/columnar-engine/add-frequent-expressions)

This page describes how to use virtual columns for expressions in the columnar engine to accelerate queries. **Note:** This feature is supported for PostgreSQL version 16 and higher.

The columnar engine can materialize and cache the results of frequently used expressions. By pre-computing and storing these results, AlloyDB Omni avoids repeated parsing and evaluation of the same expressions across multiple queries. This process improves query performance and reduces CPU consumption, especially for analytical workloads on large datasets.

Some use cases for virtual columns for expressions are as follows:

  * Filtering on JSON attributes: when you frequently filter queries based on specific key-value pairs within a JSON column.
  * Complex expression evaluation: for queries that involve complex or computationally-intensive expressions.



When you enable the virtual columns for expressions scan, queries that use the columnar engine and contain frequently used expressions are optimized automatically. The columnar engine automatically refreshes these virtual columns when it refreshes the base columns.

## Supported expressions in virtual columns

AlloyDB Omni supports `->` and `->>` operators on JSON and JSONB columns.

## Before you begin

  1. Enable the columnar engine for your AlloyDB Omni cluster. For more information, see [Configure the columnar engine](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/columnar-engine/configure).

  2. Add the base columns of expressions to the columnar engine. For more information, see [Manage column store content manually](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/columnar-engine/manage-content-manually).




## Enable virtual columns for expressions

You can enable support for virtual columns for expressions for an instance by using the `ALTER SYSTEM` command.

**Note:** You don't need to restart the database after you enable the `google_columnar_engine.enable_virtual_columns_scan` flag.

Run the `ALTER SYSTEM` PostgreSQL command, and then reload the configuration:
    
    
    ALTER SYSTEM SET google_columnar_engine.enable_virtual_columns_scan = 'on';
    SELECT pg_reload_conf();
    

## Add virtual columns for expressions

To add commonly used expressions to the columnar engine, use the `psql` client to call the `google_columnar_engine_add` function. These expressions are populated into the columnar engine as columns in addition to the columns that already exist in the database.

You can specify multiple expressions as comma-separated values.
    
    
    SELECT google_columnar_engine_add(
        relation => 'DB.SCHEMA.TABLE_NAME',
        columns => 'COLUMN_NAME, COLUMN_NAME',
        expressions => '"EXP1", "EXP2", "EXP3"');
    

Replace the following:

  * `DB.SCHEMA`: the database schema where your table is stored.
  * `TABLE_NAME`: the name of the table where your column is stored.
  * `COLUMN_NAME`: the name of the columns that include the expressions.
  * `EXP1`, `EXP2`, `EXP3`: a comma-separated list of expressions. The JSON Extract expressions supported are `->` and `->>`.



For example, to add `user ->> 'email'` and `user ->> 'name'` expressions for the `employee` table in the `public` schema, use the following query:
    
    
        SELECT google_columnar_engine_add(
        relation => 'postgres.public.employee',
        expressions => '"user ->> ''email''", "user ->> ''name''"'
        );
    

Expression syntax:

  * Enclose the entire expression value within single quotes, for example, `expressions => '"EXP1", "EXP2", "EXP3"'`.
  * Separate multiple expressions with commas.
  * Enclose each individual expression in double quotes.
  * Escape any single quote in an expression by using another single quote.



## View virtual columns for expressions

To find all expressions added for a specific table, query the `g_columnar_virtual_columns` view:
    
    
      SELECT * FROM g_columnar_virtual_columns;
    

## Remove virtual columns for expressions

To remove an expression, call the `google_columnar_engine_drop()` function:
    
    
    SELECT google_columnar_engine_drop(
      relation => 'DB.SCHEMA.TABLE_NAME',
      expressions => '"EXP1", "EXP2", "EXP3"'
    );
    

Replace the following:

  * `DB.SCHEMA`: the database schema where your table is stored.
  * `TABLE_NAME`: the name of the table where your column is stored.
  * `EXP1`, `EXP2`, `EXP3`: a comma-separated list of expressions in the table in the same format as used when adding expressions. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
