---
url: https://docs.cloud.google.com/alloydb/docs/columnar-engine/add-frequent-expressions/
title: Optimize queries with virtual columns for expressions \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:43:39.992881+00:00
---

# Optimize queries with virtual columns for expressions  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/columnar-engine/add-frequent-expressions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Optimize queries with virtual columns for expressions Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — Virtual columns for expressions**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to use virtual columns for expressions in columnar engine to accelerate queries.

**Note:** This feature is supported for PostgreSQL version 16 and higher.

The columnar engine can materialize and cache the results of frequently used expressions. By pre-computing and storing these results, AlloyDB avoids repeated parsing and evaluation of the same expressions across multiple queries. This process improves query performance and reduces CPU consumption, especially for analytical workloads on large datasets.

Some use cases for virtual columns for expressions are as follows:

  * **Filtering on JSON attributes:** when you frequently filter queries based on specific key-value pairs within a JSON column.
  * **Complex expression evaluation:** for queries that involve complex or computationally-intensive expressions.



When you enable the virtual columns for expressions scan, queries that use the columnar engine and contain frequently used expressions are optimized automatically. The columnar engine automatically refreshes these virtual columns when it refreshes the base columns.

### Supported expressions in virtual columns

AlloyDB supports `->` and `->>` operators on JSON and JSONB columns in the ([Preview](https://cloud.google.com/products#product-launch-stages)) release.

## Before you begin

  1. Enable columnar engine for your AlloyDB cluster. For more information, see [Configure the columnar engine](https://docs.cloud.google.com/alloydb/docs/columnar-engine/configure).

  2. Identify frequently used expressions in your AlloyDB queries by using [query insights](https://docs.cloud.google.com/alloydb/docs/query-insights-overview).

  3. Add the base columns of expressions to columnar engine. For more information, see [Manage column store content manually](https://docs.cloud.google.com/alloydb/docs/columnar-engine/manage-content-manually).




## Enable virtual columns for expressions

You can enable support for virtual columns for expressions for an instance using the [gcloud beta alloydb instances update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/alloydb/instances/update) command.

To use the gcloud CLI, you can [install and initialize](https://docs.cloud.google.com/sdk/docs/install-sdk) the Google Cloud CLI, or you can use [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell).

**Note:** You don't need to restart the database after you enable the `google_columnar_engine.enable_virtual_columns_scan` flag.
    
    
        gcloud beta alloydb instances update INSTANCE_ID \
            --region=REGION_ID \
            --cluster=CLUSTER_ID \
            --project=PROJECT_ID \
            --update-mode=INPLACE \
            --add-database-flags="google_columnar_engine.enable_virtual_columns_scan=on"

Replace the following:

  * `INSTANCE_ID`: your AlloyDB instance ID.
  * `REGION_ID`: the region of your AlloyDB instance.
  * `CLUSTER_ID`: the cluster ID of your AlloyDB instance.
  * `PROJECT_ID`: your Google Cloud project ID.



To set this flag at the session-level, run the following:
    
    
    SET google_columnar_engine.enable_virtual_columns_scan=on;
    

## Add virtual columns for expressions

To add commonly used expressions to the columnar engine, use the psql client to call the `google_columnar_engine_add` function. These expressions are populated into columnar engine as columns in addition to the columns that already exist in the database.

You can specify multiple expressions as comma-separated values.
    
    
        SELECT google_columnar_engine_add(
        relation => 'DB.SCHEMA.TABLE_NAME',
        columns => 'COLUMN_NAME, COLUMN_NAME',
        expressions => 'EXP1, EXP2, EXP3'
        );
    

Replace the following:

  * `DB.SCHEMA`: the database schema where your table is stored.
  * `TABLE_NAME`: the name of the table where your column is stored.
  * `COLUMN_NAME`: the name of the columns that include the expressions.
  * `EXP1, EXP2, EXP3` with a comma-separated list of expressions The JSON Extract expressions supported are `->` and `->>`.

For example, to add `user ->> 'email'` and `user ->> 'name'` expressions for the `employee` table in the `public` schema, use the following query:
        
        SELECT google_columnar_engine_add(
            relation => 'postgres.public.employee',
            expressions => '"user ->> ''email''", "user ->> ''name''"'
            );
        

**Expression Syntax:**

    * Enclose the entire expression value within single quotes—for example, `expressions => 'EXP1,EXP2,EXP3'`.
    * Separate multiple expressions with commas.
    * Enclose each individual expression in double quotes.
    * Escape any single quote in an expression by using another single quote.

For example, to add the `col -> 'level1'` and `col -> 'level1' ->> 'level2'` expression, use the following format:
    
    expressions => '"col -> ''level1''", "col -> ''level1'' ->> ''level2''"'
    




### Virtual columns for expressions example

This example demonstrates how to use the virtual columns for expressions feature. Create a `users` table with a `profile` JSONB column and populate it with sample data. Then, based on query analysis, add the frequently used `profile ->> 'email'` expression to the columnar engine with the `google_columnar_engine_add` function. The columnar engine then uses this frequent expression to help optimize subsequent queries.

To add this example frequent expression to the columnar engine, follow these steps:

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click the name of your cluster in the **Resource name** column.

  3. In the navigation pane, click **AlloyDB Studio**.

  4. To create the `users` table with a `profile` JSONB column, run the following:
         
         CREATE TABLE users (
         id int,
         username TEXT,
         profile JSONB
         );
         

  5. To populate the `users` table with sample data, run the following:
         
         INSERT INTO users (id, username, profile)
         SELECT
             i,
             'user' || i,
             jsonb_build_object(
                 'name', 'User ' || i,
                 'email', 'user' || i || '@example.com',
                 'active', (i % 2 = 0)
             )
         FROM generate_series(1, 100000) AS i;
         

  6. To improve the performance of the query that includes the frequently used expression, add the `profile ->> 'email'` expression to the columnar engine:
         
         SELECT google_columnar_engine_add(
             relation => 'users',
             columns => 'username, profile',
             expressions => '"profile ->> ''email''"'
         );
         

  7. Run a query that uses the frequent expression and observe the time the query takes to complete.
         
         SELECT username
         FROM users
         WHERE profile->>'email' = 'user50000@example.com';
         

  8. Enable the virtual columns for expressions feature.
         
         SET google_columnar_engine.enable_virtual_columns_scan=on;
         

  9. Rerun the query that uses the frequent expression and observe the time it takes for the query to complete.
         
         SELECT username
         FROM users
         WHERE profile->>'email' = 'user50000@example.com';
         




The query runtime is faster after you enable virtual columns for expressions.

## View virtual columns for expressions

To find all expressions added for a specific table, query the `g_columnar_virtual_columns` view:
    
    
        SELECT * FROM g_columnar_virtual_columns;
    

The output looks similar to the following, where the `description` field shows the all expressions added for a table (relation).
    
    
    SELECT * FROM g_columnar_virtual_columns;
    category           | expression
    database_name      | testdb
    schemas            | {public}
    relations          | {users}
    description        | profile->>'email'
    column_data_type   | text
    status             | Usable
    last_accessed_time | 2026-02-04 06:25:32.499601+00
    num_times_accessed | 1
    

## Remove virtual columns for expressions

To remove an expression, call the `google_columnar_engine_drop()` function:
    
    
        SELECT google_columnar_engine_drop(
          relation => 'DB.SCHEMA.TABLE_NAME',
          expressions => 'EXP1, EXP2, EXP3'
        );
    

Replace `EXP1, EXP2, EXP3` with a comma-separated list of expressions in the table in the same format as used when adding expressions.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
