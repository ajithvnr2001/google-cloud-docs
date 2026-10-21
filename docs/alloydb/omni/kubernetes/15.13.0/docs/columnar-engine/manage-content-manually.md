---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/columnar-engine/manage-content-manually/
title: Manage column store content manually \u00a0|\u00a0 AlloyDB Omni for Kubernetes: 15.13.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:57:02.343345+00:00
---

# Manage column store content manually  |  AlloyDB Omni for Kubernetes: 15.13.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/columnar-engine/manage-content-manually/

This page documents AlloyDB Omni version **15.13.0** using the **Kubernetes** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For Kubernetes: 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/overview)



Send feedback 

#  Manage column store content manually Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.13.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/columnar-engine/manage-content-manually)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/columnar-engine/manage-content-manually)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/columnar-engine/manage-content-manually)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/columnar-engine/manage-content-manually)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/columnar-engine/manage-content-manually)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/columnar-engine/manage-content-manually)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/columnar-engine/manage-content-manually)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/columnar-engine/manage-content-manually)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/columnar-engine/manage-content-manually)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/columnar-engine/manage-content-manually)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/columnar-engine/manage-content-manually)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/columnar-engine/manage-content-manually)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/columnar-engine/manage-content-manually)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/columnar-engine/manage-content-manually)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/columnar-engine/manage-content-manually)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/columnar-engine/manage-content-manually)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/columnar-engine/manage-content-manually)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/columnar-engine/manage-content-manually)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/columnar-engine/manage-content-manually)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/columnar-engine/manage-content-manually)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/columnar-engine/manage-content-manually)

This page describes how to manage the content of the columnar engine's column store by manually adding and removing columns. 

Based on your workload, you can manually add columns to the column store or drop some or all of the columns of a table or a materialized view from the column store. Query evaluation automatically uses the stored columnar data to answer queries.

When choosing which tables, materialized views and columns to add to the column store, consider both the size of the column store and the shape of the workload. Good candidates for selection include large tables or views that are frequently scanned. Within these tables or views, identify any large non-unique indexes used by the OLAP workload. You can add these indexes' columns to the column store and potentially drop the indexes, thereby eliminating the performance cost associated with their maintenance on the primary instance.

Use one of the following methods to manage the content of the columnar engine's column store:

  * Manage column store content by updating database flags
  * Manage column store content using SQL functions



See [What data you can add to the column store](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/columnar-engine/overview#limitations) for information about what data types and data sources you can use when adding tables, columns, and materialized views to the column store.

## Manage column store content by updating database flags

You can manage column store content manually by updating the `google_columnar_engine.relations` database flag. The flag has a single value that specifies all of your column store's data sources. During the restart, columns specified in this flag are automatically populated into the column store.

You can use this flag together with [auto-columnarization](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/columnar-engine/manage-content-recommendations). If the columnar engine has memory available after populating the columns you specify through the `google_columnar_engine.relations` flag, then auto-columnarization adds further columns to the column store, as needed.

### Add columns using flags

To add columns to the column store, define an instance's `google_columnar_engine.relations` flag. Set its value to a comma-separated list of items, with each item specifying a list of columns to include from a specific table, in this format:
    
    
    DATABASE_NAME.SCHEMA_NAME.TABLE_NAME(COLUMN_LIST)
    

Replace the following:

  * DATABASE_NAME: the database containing the columns to add to the column store.

  * SCHEMA_NAME: the schema identifying the tables or the materialized views to add to the column store—for example, `public`.

  * TABLE_NAME: the table or the materialized view containing the columns to add to the column store.

  * COLUMN_LIST: a comma-separated list of the columns to add to the column store.




To add all of one table's or one materialized view's columns, omit the column list:
    
    
    DATABASE_NAME.SCHEMA_NAME.TABLE_NAME
    

**Caution:** Running this example unsets all database flags from the instance except for the flags that it specifies.
    
    
    ALTER SYSTEM SET google_columnar_engine.relations='DATABASE_NAME.SCHEMA_NAME.TABLE_NAME(COLUMN_1,COLUMN_2)';

### Drop columns using flags

To drop columns from the column store, set a new value for the `google_columnar_engine.relations` flag described in [Add columns using flags](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/columnar-engine/manage-content-manually#by-flag), leaving out the columns that you want to drop.

To drop all of the columns from the column store, unset the `google_columnar_engine.relations` flag from your instance.

For more information on setting database flags on an instance, see [Configure AlloyDB Omni database parameters](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/configure-database-flags).

## Manage column store content using SQL functions

You can manage column store content manually by using SQL functions.

### Add columns using SQL functions

Run the `google_columnar_engine_add` SQL function to add columns to the column store.

This method adds the specified columns to the column store and manages the columns in the connected node only. The new columns don't persist within the store across instance restarts.

This method does not change the `google_columnar_engine.relations` database flag. [Auto columnarization](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/columnar-engine/manage-content-recommendations) does not consider columns added by this SQL function.

### psql Client
    
    
    SELECT google_columnar_engine_add(
        relation => 'TABLE_NAME',
        columns => 'COLUMN_LIST'
    );
    

Replace the following: 
  * 'TABLE_NAME': A string containing the name of the table or the materialized view. If the table or the view is in a schema other than `public`, specify the name of the schema, a dot, and the name of the table or the view; for example, `'myschema.mytable'`.
  * 'COLUMN_LIST': A string containing a comma-separated, case-sensitive list of the names of the columns you want to add. If you want to add all of the table's or the materialized view's columns to the column store, omit this parameter.



### Drop columns using SQL functions

Run the `google_columnar_engine_drop` SQL function as follows:

### psql Client
    
    
    SELECT google_columnar_engine_drop(
        relation => 'TABLE_NAME',
        columns => 'COLUMN_LIST'
    );
    

Replace the following: 

  * 'TABLE_NAME': A string containing the name of the table or the materialized view. If the table or the view is in a schema other than `public`, specify the name of the schema, a dot, and the name of the table or the view; for example, `'myschema.mytable'`.
  * 'COLUMN_LIST': A string containing a comma-separated, case-sensitive list of the names of the columns you want to add. If you want to add all of the table's or the materialized view's columns to the column store, omit this parameter.



You can use the `google_columnar_engine_drop` function to remove columns added by editing the `google_columnar_engine.relations` database flag. However, when you do so, those columns are added back to the columnar store when the instance is restarted.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
