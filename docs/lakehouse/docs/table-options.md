---
url: https://docs.cloud.google.com/lakehouse/docs/table-options/
title: Configure table options \u00a0|\u00a0 Lakehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:25:57.384328+00:00
---

# Configure table options  |  Lakehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/table-options/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  Configure table options Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Configuring table options lets you opt in to BigQuery write interoperability or table management (automatic storage optimization) for your Apache Iceberg tables in the _Lakehouse runtime catalog_. These options serve as foundational settings that extend capabilities for operations on the table.

By configuring specific table properties, you can enable write interoperability with BigQuery DML or enable automatic table management (storage optimization).

When using tables in the Lakehouse runtime catalog, it's helpful to [understand the different table types and their opt-in capabilities](https://docs.cloud.google.com/lakehouse/docs/lakehouse-tables). To learn more about using Apache Iceberg tables specifically, see [Overview of Apache Iceberg tables](https://docs.cloud.google.com/lakehouse/docs/manage-tables).

## Before you begin

  1. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  2. Enable the BigLake API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=biglake.googleapis.com)

  3. [Set up the Lakehouse runtime catalog](https://docs.cloud.google.com/lakehouse/docs/lakehouse-iceberg-rest-catalog) with the Apache Iceberg REST catalog endpoint.



### Required roles

To get the permissions that you need to configure table options, ask your administrator to grant you the following IAM roles on your project and storage bucket: 

  * Configure table properties in [credential vending mode](https://docs.cloud.google.com/lakehouse/docs/lakehouse-iceberg-rest-catalog#credential-vending-mode): BigLake Editor (`roles/biglake.editor`) - the project 
  * Configure table properties in non-credential vending mode: 
    * BigLake Editor (`roles/biglake.editor`) - the project 
    * Storage Object User (`roles/storage.objectUser`) - the Cloud Storage bucket 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Configuration considerations

Consider the following requirements and default behaviors when configuring table options:

### Supported Iceberg tables

Only Apache Iceberg V2 (GA) and V3 (Preview) tables are supported. Iceberg V1 tables aren't supported. To upgrade existing V1 tables, see [Upgrade Iceberg V1 tables to V2](https://docs.cloud.google.com/lakehouse/docs/update-tables).

### Credential vending requirement

To opt in to automatic table management your Lakehouse runtime catalog must have [credential vending](https://docs.cloud.google.com/lakehouse/docs/credential-vending) enabled at the catalog level. Table management background jobs use the credential vending service account to authenticate and update underlying storage data files.

## Enable BigQuery DML

Enabling BigQuery data manipulation language (DML) statements unlocks write interoperability from BigQuery on Apache Iceberg tables created using open source engines.

Supported statements include `INSERT`, `UPDATE`, `DELETE`, and `MERGE`, as well as standard [DDL statements](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-definition-language) like `CREATE TABLE`, `ALTER TABLE`, and `DROP TABLE` except for those that are [not supported in Apache Iceberg tables in BigQuery](https://docs.cloud.google.com/bigquery/docs/biglake-iceberg-tables-in-bigquery#limitations).

### Enable BigQuery DML for new tables

When you [create a table](https://docs.cloud.google.com/lakehouse/docs/create-table#bigquery) from BigQuery, BigQuery DML and automatic table management are enabled by default. When you create a table from open-source engines, configure the `gcp.biglake.bigquery-dml.enabled = true` table property using your engine's DDL syntax.

**For example, in Spark SQL:**
    
    
    CREATE TABLE NAMESPACE.TABLE_NAME (id int, data string)
    USING ICEBERG
    TBLPROPERTIES ('gcp.biglake.bigquery-dml.enabled' = true);
    

### Enable BigQuery DML for existing tables

To enable BigQuery DML on an existing table, [update the table property](https://docs.cloud.google.com/lakehouse/docs/alter-table).

**For example, in Spark SQL:**
    
    
    ALTER TABLE NAMESPACE.TABLE_NAME
    SET TBLPROPERTIES ('gcp.biglake.bigquery-dml.enabled' = true);
    

### Disable BigQuery DML

Disabling BigQuery DML makes the table read-only for BigQuery and stops automatic table management.

**For example, in Spark SQL:**
    
    
    ALTER TABLE NAMESPACE.TABLE_NAME
    SET TBLPROPERTIES ('gcp.biglake.bigquery-dml.enabled' = false);
    

## Enable table management

Table management automates background processes to optimize storage and manage data and metadata lifecycle, such as compaction and garbage collection.

Table management lets you perform the following operations:

  * **Snapshot expiration and garbage collection:** Snapshot expiration manages the retention and deletion of data and metadata files from table snapshots. This runs automatically in the background after any data mutation. Snapshots are expired based on the user-configured Iceberg table properties `history.expire.max-snapshot-age-ms` and `history.expire.min-snapshots-to-keep` on the table. It removes expired snapshot entries by creating one more additional snapshot definition that is manifested by a new metadata file that no longer includes references to the snapshots that were removed.

    * Limitation: Snapshot expiration and associated garbage collection are skipped if the table uses tags or branches. For more information, see Limitations.

    * Limitation: Orphan file removal isn't handled by automatic table management. For more information, see Limitations.

  * **Coalesce (compaction):** Coalesce is responsible for maintaining the shape of the data, by merging small files into larger files. Coalesce runs automatically in the background after any data mutation. Files are selected for compaction if their average uncompressed size is less than 50% of the target file size of 256 MB. Each coalesce operation produces a new table snapshot. Coalesce jobs typically yield to and retry after any running DML operations. However, to prevent indefinite starvation of storage optimization, a coalesce job is forcibly triggered every 24 hours if data is eligible for coalesce.

  * **Monitoring table management jobs:** All background table management jobs are logged in BigQuery's `INFORMATION_SCHEMA.JOBS` view. You can query this view to track these operations, similar to how you monitor other BigQuery jobs. For more information about querying job information, see [Get Iceberg storage optimization jobs](https://docs.cloud.google.com/bigquery/docs/information-schema-jobs#get-iceberg-storage-optimization-jobs).

The frequency of table management jobs directly correlates with data mutation activity. Frequent small inserts or updates trigger more frequent background tasks. You might observe periods with no background jobs if there are no writes to the table. Conversely, high write volumes might result in more visible job activity in `INFORMATION_SCHEMA`.




### Enable table management for new tables

When you [create a table](https://docs.cloud.google.com/lakehouse/docs/create-table#bigquery) from BigQuery, DML and automatic table management are enabled by default. When you create a table from open-source engines, configure the `gcp.biglake.table-management.enabled` property. Enabling table management automatically enables BigQuery DML if it is not already enabled.

**For example, in Spark SQL:**
    
    
    CREATE TABLE NAMESPACE.TABLE_NAME (id int, data string)
    USING ICEBERG
    TBLPROPERTIES ('gcp.biglake.table-management.enabled' = true);
    

### Enable table management for existing tables

To enable table management on an existing table, [update the table property](https://docs.cloud.google.com/lakehouse/docs/alter-table).

**For example, in Spark SQL:**
    
    
    ALTER TABLE NAMESPACE.TABLE_NAME
    SET TBLPROPERTIES ('gcp.biglake.table-management.enabled' = true);
    

### Disable table management

Disabling table management prevents future background optimization jobs from being queued, though active in-progress jobs will complete. Disabling table management does not disable BigQuery DML.

###  Spark SQL 
    
    
    ALTER TABLE NAMESPACE.TABLE_NAME
    SET TBLPROPERTIES ('gcp.biglake.table-management.enabled' = false);
    

###  BigQuery 
    
    
    ALTER TABLE `PROJECT_ID.CATALOG_ID.NAMESPACE.TABLE_NAME`
    SET OPTIONS (`properties.gcp.biglake.table-management` = "disabled");
    

## Limitations

Limitations for managed capabilities (such as BigQuery write interoperability and automatic table management) include:

### General limitations

  * Managed capabilities are only supported with Apache Iceberg tables created in the Lakehouse runtime catalog using the Apache Iceberg REST catalog endpoint.
  * All existing limitations for Apache Iceberg tables managed by BigQuery apply to operations with managed capabilities enabled.
  * Managed capabilities are not supported for tables with Apache Iceberg format-version 3. Only format-version 2 (Iceberg v2 spec) tables can be opted in to managed capabilities.
  * Managed capabilities are not supported for tables that have advanced partitioning, such as partitioning by `STRING`, multi-column partitioning, or partition evolution.
  * Managed capabilities are not supported for tables configured with sort orders (for example, using the `WRITE ORDER BY` procedure or setting `write.distribution.mode = range`).
  * Managed capabilities are not supported for Iceberg v2 tables using merge-on-read mode. Only tables using copy-on-write update, delete, and merge mode can be opted in for managed capabilities.
  * Managed capabilities do not support data files compressed using `gzip`, `lz4`, or `brotli` codecs (`write.parquet.compression.codec`). Only `zstd` and `snappy` compression types are supported for data files.
  * Managed capabilities are not supported for tables if the schema contains nested primary key identifiers (`identifier-field-ids`) that reference nested paths or fields in a structure.
  * Managed capabilities are not supported for tables with custom data or metadata locations (`write.data.path` and `write.metadata.path`). The default Cloud Storage bucket location is required for holding data and metadata files.
  * BigQuery clustering is not supported for Apache Iceberg tables managed by the Lakehouse runtime catalog.
  * If a table is created with the `NUMERIC` data type in BigQuery, any schema updates from Spark will fail because Spark reads `NUMERIC` as `NUMERIC(38,9)`. As a workaround, when creating tables with the `NUMERIC` type in BigQuery, explicitly set the precision to `NUMERIC(38,9)`.
  * **Known issue:** Dropping a column in BigQuery using DDL (`ALTER TABLE ... DROP COLUMN`) followed immediately by re-adding a column with the same name is not supported.



### Limitations with time travel

  * When table management is enabled, the maximum recommended value for the `history.expire.max-snapshot-age-ms` property is 7 days.
  * BigQuery project-level or dataset-level configurations for [time travel](https://docs.cloud.google.com/bigquery/docs/time-travel#time_travel) do not apply. Only Iceberg table properties and defaults are active.



### Limitations with table management

  * Snapshot expiration is skipped for the entire table if the table contains snapshots with tags or branches. Custom retention set using `ALTER... RETAIN x DAYS` is ignored, and any values set for the `history.expire.max-ref-age-ms` property are ignored. Open source engines can still perform snapshot expiration.
  * Automatic table management does not expire schemas or partition specs. The `metadata.json` file retains the full history of schemas and partition specs, even if no snapshots refer to those schema IDs.
  * Orphan files created by BigQuery or open source engines are not cleaned up by automatic table management. Open source engines can perform orphan file cleanup (for example, using the [Spark remove_orphan_files procedure](https://iceberg.apache.org/docs/latest/spark-procedures/#remove_orphan_files) with the `prefix_listing` option set to `true`).

**Warning:** Running orphan file cleanup can delete files from active, long-running queries if the query runs longer than the `older_than` threshold (default is 3 days). Set the `older_than` parameter carefully.
  * Coalesce does not support z-ordering and linear sorting. If your table contains these properties, it is not guaranteed that the layout is maintained after coalesce runs. If your tables contain these properties, the best action is to not enable table management.




### Limitations with partitioning

  * When creating or registering tables from open source engines, managed capabilities only support partitioning on `DATE`, `DATETIME`, and `TIMESTAMP` field types with `hour`, `day`, `month`, and `year` transforms (except for the `hour` transform on `DATE` fields), and `INTEGER` field types.
  * Managed capabilities are not supported on tables with `IDENTITY` transforms. Users must explicitly specify the transformation.
  * `CREATE OR REPLACE` commands on tables with managed capabilities are only supported if they use the same partition spec. The following replacements are not supported: 
    * Replacing a non-partitioned table with a partitioned table.
    * Replacing a partitioned table with a non-partitioned table.
    * Replacing a partitioned table with a table using a different partitioning spec.
  * Custom partition field naming is not supported. Tables created or registered from open source engines must follow the engine's default partition field naming convention (appending `_` and the transform name, such as `_hour`, `_day`, `_month`, or `_year`). For example, for a field named `time_date` using the `DAY` transform, the expected partition field value is: `json { "field-id": 1, "source-id": 1, "name": "time_date_day", "transform": transform }`



### Limitations with custom Iceberg table properties

The following table behavior properties cannot be configured to non-default values when managed capabilities are enabled. Default values are hardcoded when any managed capability is enabled:

Property | Default value | Details  
---|---|---  
`format-version` | `2` | Managed capabilities only support Iceberg v2 tables.  
`write.format.default` | `parquet` | Tables only support data files in Parquet format.  
`write.data.path` | `table location + /data` | The default Cloud Storage bucket path configured for the Apache Iceberg REST catalog endpoint is used to write data files.  
`write.metadata.path` | `table location + /metadata` | The default Cloud Storage bucket path configured for the Apache Iceberg REST catalog endpoint is used to write metadata files.  
`write.delete.mode` | `copy-on-write` | BigQuery writes and table management jobs only support copy-on-write.  
`write.update.mode` | `copy-on-write` | BigQuery writes and table management jobs only support copy-on-write.  
`write.merge.mode` | `copy-on-write` | BigQuery writes and table management jobs only support copy-on-write.  
`write.delete.isolation-level` | Strict conflict detection | Changes that modify the `metadata.json` file (including data conflicts, metadata conflicts, phantom reads, or non-conflicting concurrent writes) cause the concurrent transaction to fail and retry.  
`write.update.isolation-level` | Strict conflict detection | Same behavior as `write.delete.isolation-level`.  
`write.merge.isolation-level` | Strict conflict detection | Same behavior as `write.delete.isolation-level`.  
  
The following properties can be configured when creating or altering tables from open source engines:

Property | Default value | Details  
---|---|---  
`write.parquet.compression-codec` | `zstd` | BigQuery writes and storage optimization only support `zstd` and `snappy` compression formats. Other compression formats (such as `gzip`, `brotli`, and `lz4`) are not supported.  
`write.metadata.compression-codec` | `null` | Can be configured to `null` or `gzip`.  
`history.expire.max-snapshot-age-ms` | `432000000` (5 days) | Can be configured to any positive integer, but recommended up to 7 days (604800000 ms) when table management is enabled. Table management jobs delete snapshots older than the specified duration.  
`history.expire.min-snapshots-to-keep` | `1` | Can be configured to any positive integer. Table management jobs retain at least this number of snapshots.  
  
Other Apache Iceberg write properties, such as `write.target-file-size-bytes` and `write.parquet.page-size-bytes`, can be configured from open source engines, but BigQuery writes and table management jobs might not comply with them.

## What's next

  * Learn how to [modify data with BigQuery DML](https://docs.cloud.google.com/lakehouse/docs/modify-data-dml).
  * Learn how to [query a table](https://docs.cloud.google.com/lakehouse/docs/query-table).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
