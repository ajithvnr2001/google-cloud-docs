---
url: https://docs.cloud.google.com/alloydb/docs/troubleshoot/troubleshoot-bigquery-fdw/
title: Troubleshoot the BigQuery foreign data wrapper extension \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:43:37.500748+00:00
---

# Troubleshoot the BigQuery foreign data wrapper extension  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/troubleshoot/troubleshoot-bigquery-fdw/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Troubleshoot the BigQuery foreign data wrapper extension Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to resolve common issues with the `bigquery_fdw` extension. For information on using the BigQuery foreign data wrapper to access data, see [Configure AlloyDB access to real-time data in BigQuery](https://docs.cloud.google.com/alloydb/docs/configure-access-real-time-data).

## Extension and metadata issues

This section lists extension and metadata errors that you might encounter and provides suggestions for how to fix each of them.

### The bigquery_fdw extension is disabled

**Recommended fix**

To resolve this issue, follow these steps:

  1. Ensure that the database flag `bigquery_fdw.enabled` is set to `on`. You can verify this in one of the following ways:

     * [View the current database flags on the instance](https://docs.cloud.google.com/alloydb/docs/instance-configure-database-flags#gcloud).
     * [Connect to the instance](https://docs.cloud.google.com/alloydb/docs/connection-overview) and run the following command in `psql`:
    
    SHOW bigquery_fdw.enabled;
    

  2. If the `bigquery_fdw.enabled` flag is `off`, [set `bigquery_fdw.enabled` to `on`](https://docs.cloud.google.com/alloydb/docs/instance-configure-database-flags).




## Permission and access issues

This section lists permission and access errors that you might encounter and provides recommended fixes.

### Access Denied: Table permission bigquery.tables.get denied

The extension failed to create a BigQuery read session with the following error:
    
    
    Error in non-idempotent operation: Access Denied: Table TABLE_NAME: Permission bigquery.tables.get denied on table TABLE_NAME (or it may not exist).
    

This indicates that the AlloyDB for PostgreSQL cluster service account lacks BigQuery data viewer permissions.

**Recommended fix**

To resolve this issue, provide the primary cluster `service_account_email` with one of the following roles:

  * BigQuery Data Viewer (`roles/bigquery.dataViewer`)
  * A custom role containing the `bigquery.tables.get` and `bigquery.tables.getData` permissions.



### Access bigquery.readsessions.create denied

The extension failed to create a BigQuery read session with the following error:
    
    
    Error in non-idempotent operation: request failed: the user does not have 'bigquery.readsessions.create' permission for PROJECT_NAME.
    

This indicates that the AlloyDB cluster service account lacks BigQuery read session user permissions.

**Recommended fix**

To resolve this issue, provide the primary cluster's `service_account_email` with one of the following roles:

  * BigQuery Read Session User (`roles/bigquery.readSessionUser`)
  * A custom role containing the `bigquery.readsessions.create` and `bigquery.readsessions.getData` permissions.



### User does not have bigquery.jobs.create permission

The extension failed to create a BigQuery read session with the following error:
    
    
    Error in non-idempotent operation: Access Denied: Project PROJECT_NAME: User does not have bigquery.jobs.create permission in project PROJECT_NAME.
    

**Recommended fix**

To resolve this issue, provide the AlloyDB cluster `service_account_email` with one of the following roles:

  * BigQuery Job User (`roles/bigquery.jobUser`).
  * A custom role containing the `bigquery.jobs.create` permission.



## Configuration and data type issues

This section lists configuration and data type errors that you might encounter and provides recommended fixes.

### Selected fields don't exist in the table schema

The following issues occurred:
    
    
    Error in non-idempotent operation: request failed: The following selected fields do not exist in the table schema: POSTGRES_COLUMN_NAME(S).
    Error in non-idempotent operation: Unrecognized name: POSTGRES_COLUMN_NAME(S);
    

This indicates incorrect column names in the foreign table definition.

**Recommended fix**

To resolve this issue, make sure that the exact column name (case-sensitive) exists on the corresponding BigQuery table specified in the definition.

### Invalid input syntax for type mapping

The operation failed with the following error:
    
    
    ERROR: invalid input syntax for type POSTGRES_COLUMN_DATA_TYPE: BIGQUERY_COLUMN_VALUE_RECEIVED.
    

This indicates an incorrect column data type mapping in the foreign table definition.

**Recommended fix**

To resolve this issue, ensure that the data type mapping is compatible—for example, a string column in BigQuery can't map to an integer column in PostgreSQL. For more information, see [Data type mappings](https://docs.cloud.google.com/alloydb/docs/configure-access-real-time-data#data-type-mappings).

### Unsupported BigQuery column data type

The following issues occurred:
    
    
    ERROR: bigquery_fdw extension encountered internal error for column: POSTGRES_COLUMN_DATA_TYPE. Only avro logical type: AVRO_BIGQUERY_LOGICAL_TYPE is supported for avro type: AVRO_BIGQUERY_DATA_TYPE.
    encountered internal error for column:POSTGRES_COLUMN_NAME. Data type: BIGQUERY_DATA_TYPE is not supported.
    

This indicates the column data type being queried isn't supported.

**Recommended fix**

To resolve this issue, see [Data type mappings](https://docs.cloud.google.com/alloydb/docs/configure-access-real-time-data#data-type-mappings).

### Non-table entities cannot be read

The extension failed with the following error:
    
    
    ERROR: bigquery_fdw extension failed to create BigQuery read session with error: Error in non-idempotent operation: request failed: non-table entities cannot be read with the storage API.
    

This indicates the BigQuery table type being queried isn't supported.

**Recommended fix**

To resolve this issue, ensure that you are querying a supported BigQuery entity type, such as a standard table.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
