---
url: https://docs.cloud.google.com/looker/docs/reference/param-view-derived-table/
title: derived_table \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:29.318047+00:00
---

# derived_table  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-view-derived-table/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  derived_table Stay organized with collections  Save and categorize content based on your preferences. 

## Usage
    
    
    view: my_view {
      derived_table: { ... }
    }
    

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) `derived_table` |  Default Value None  
---|---  
  
## Definition

A derived table can be treated as if it is a normal table in your database. You can create either of the following types of derived tables:

  * A [native derived table](https://docs.cloud.google.com/looker/docs/derived-tables#native_derived_tables) that is defined using the [`explore_source`](https://docs.cloud.google.com/looker/docs/reference/param-view-explore-source) parameter
  * A [SQL-based derived table](https://docs.cloud.google.com/looker/docs/derived-tables#sql-based_derived_tables) using a raw SQL query that you define using the [`sql`](https://docs.cloud.google.com/looker/docs/reference/param-view-sql-for-derived-table) parameter



> Certain edge cases won't permit the use of the `sql` parameter. In such cases, Looker supports the following parameters for defining a SQL query for [PDTs](https://docs.cloud.google.com/looker/docs/derived-tables#persistent_derived_tables_\(pdts\)):
> 
> * [`create_process`](https://docs.cloud.google.com/looker/docs/reference/param-view-create-process)
> * [`sql_create`](https://docs.cloud.google.com/looker/docs/reference/param-view-sql-create)
> 
> With `sql`, `create_process`, or `sql_create` parameter, in all these cases you are defining the derived table with a SQL query, so these are all considered SQL-based derived tables.

The `derived_table` parameter begins a section of LookML where you define how a derived table should be calculated, what indexes or keys it should use, and when it should be regenerated.

Derived tables can be [temporary derived tables](https://docs.cloud.google.com/looker/docs/derived-tables#temporary_derived_tables) that are calculated ad hoc as users request data from them, or they can be [persistent derived tables (PDTs)](https://docs.cloud.google.com/looker/docs/derived-tables#persistent_derived_tables_\(pdts\)) that are persisted on your database by using a [persistence strategy](https://docs.cloud.google.com/looker/docs/derived-tables#persistence_strategies).

If your dialect supports them, you can use incremental PDTs in your project. An [incremental PDT](https://docs.cloud.google.com/looker/docs/incremental-pdts) is a PDT that is built incrementally by appending fresh data to the table, instead of rebuilding the table in its entirety. See the [Incremental PDTs](https://docs.cloud.google.com/looker/docs/incremental-pdts) documentation page for more information on incremental PDTs.

See the [Derived tables in Looker](https://docs.cloud.google.com/looker/docs/derived-tables) documentation page for more information on derived tables.

## Derived table subparameters

This section lists the derived table subparameters.

Parameter | Description  
---|---  
[`cluster_keys`](https://docs.cloud.google.com/looker/docs/reference/param-view-cluster-keys)`: ["column_name", "column_name", ...]` | Specifies that a PDT be clustered by one or more fields in BigQuery and Snowflake.  
[`create_process`](https://docs.cloud.google.com/looker/docs/reference/param-view-create-process)`: { [sql_step](https://docs.cloud.google.com/looker/docs/reference/param-view-create-process):SQL query ;; }` | Specifies an ordered sequence of steps to create a PDT on a database dialect that requires custom DDL commands.  
[`datagroup_trigger`](https://docs.cloud.google.com/looker/docs/reference/param-view-datagroup-trigger)`: datagroup_name` | Specifies the datagroup to use for the PDT rebuilding policy.  
[`distribution`](https://docs.cloud.google.com/looker/docs/reference/param-view-distribution)`: "column_name"` | Sets the distribution key of a PDT that is built in Redshift or Aster.  
[`distribution_style`](https://docs.cloud.google.com/looker/docs/reference/param-view-distribution-style)`: all | even` | Sets the distribution style of a PDT that is built in Redshift.  
[`explore_source`](https://docs.cloud.google.com/looker/docs/reference/param-view-explore-source)`: explore_name { # Desired subparameters (described on [explore_source](https://docs.cloud.google.com/looker/docs/reference/param-view-explore-source) page) }` | Specifies a native derived table based on an Explore.  
[`increment_key`](https://docs.cloud.google.com/looker/docs/reference/param-view-increment-key)`: "column_name"` | Specifies the time increment for which fresh data should be queried and appended to an incremental PDT.  
[`increment_offset`](https://docs.cloud.google.com/looker/docs/reference/param-view-increment-offset)`: N` | Specifies the number of previous time periods (at the increment key granularity) that are rebuilt to account for late arriving data for an incremental PDT.  
[`indexes`](https://docs.cloud.google.com/looker/docs/reference/param-view-indexes)`: ["column_name", "column_name", ...]` | Sets the indexes of a PDT built in a traditional database (for example, MySQL, Postgres) or an interleaved sort key in Redshift.  
[`interval_trigger`](https://docs.cloud.google.com/looker/docs/reference/param-view-interval-trigger)`: "N (seconds | minutes | hours)"` | Specifies a rebuild schedule for a PDT.  
[`materialized_view`](https://docs.cloud.google.com/looker/docs/reference/param-view-materialized-view)`: yes | no` | Creates a materialized view on your database for a derived table.  
[`partition_keys`](https://docs.cloud.google.com/looker/docs/reference/param-view-partition-keys)`: ["column_name", "column_name", ...]` | Specifies that a PDT be partitioned by one or more fields in Presto, or by a single date/time field in BigQuery.  
[`persist_for`](https://docs.cloud.google.com/looker/docs/reference/param-view-persist-for-for-derived-table)`: "N (seconds | minutes | hours)"` | Sets the maximum age of a PDT before it is regenerated.  
[`publish_as_db_view`](https://docs.cloud.google.com/looker/docs/reference/param-view-publish-as-db-view)`: yes | no` | Creates a stable database view for the PDT to enable querying the table outside of Looker.  
[`sortkeys`](https://docs.cloud.google.com/looker/docs/reference/param-view-sortkeys)`: ["column_name", "column_name", ...]` | Sets the sort keys of a PDT that is built in Redshift.  
[`sql`](https://docs.cloud.google.com/looker/docs/reference/param-view-sql-for-derived-table)`: SQL query ;;` | Declares the SQL query for a derived table.  
[`sql_create`](https://docs.cloud.google.com/looker/docs/reference/param-view-sql-create)`: { SQL query ;; }` | Defines a SQL CREATE statement to create a PDT on a database dialect that requires custom DDL commands.  
[`sql_trigger_value`](https://docs.cloud.google.com/looker/docs/reference/param-view-sql-trigger-value)`: SQL query ;;` | Specifies the condition that causes a PDT to be regenerated.  
[`table_compression`](https://docs.cloud.google.com/looker/docs/reference/param-view-table-compression)`: GZIP | SNAPPY` | Specifies the table compression to use for a PDT in Amazon Athena.  
[`table_format`](https://docs.cloud.google.com/looker/docs/reference/param-view-table-format)`: PARQUET | ORC | AVRO | JSON | TEXTFILE` | Specifies the table format to use for a PDT in Amazon Athena.  
  
## Examples

Create a `customer_order_facts` native derived table with the `explore_source` parameter:
    
    
    view: customer_order_facts {
      derived_table: {
        explore_source: order {
          column: customer_id { field: order.customer_id }
          column: lifetime_orders { field: order.count }
          column: lifetime_spend { field: order.total_spend }
        }
      }
    }
    

Create a `customer_order_facts` derived table with the `sql` parameter:
    
    
    view: customer_order_facts {
      derived_table: {
        sql:
          SELECT
            customer_id,
            COUNT(*) AS lifetime_orders,
            SUM(total) AS lifetime_spend
          FROM
            order
          GROUP BY
            customer_id ;;
      }
    }
    

## Things to consider

### Avoid overusing derived tables to create pure SQL solutions

Users who are particularly SQL savvy often use derived tables to solve problems with complex SQL queries, the results of which can then be exposed to users. While it may sometimes be necessary to do, it can also miss out on the modular, reusable nature of LookML and can lock users into rigid ways of exploring their data.

Our general suggestion is to think about the underlying purpose of your SQL query and then convert that logic into LookML, rather than copying and pasting existing queries into a derived table. If you need assistance creating analyses that don't rely on derived tables, Looker support analysts are here to help with best practices.

## Supported database dialects for derived tables

### Supported database dialects for temporary derived tables

For Looker to support derived tables in your Looker project, your database dialect must also support them. The following table shows which dialects support derived tables in the latest release of Looker:

Dialect | Supported?  
---|---  
Actian Avalanche|   
Amazon Athena|   
Amazon Aurora MySQL|   
Amazon Redshift|   
Amazon Redshift 2.1+|   
Amazon Redshift Serverless 2.1+|   
Apache Druid|   
Apache Druid 0.13.x - 0.17.x|   
Apache Druid 0.18+|   
Apache Hive 2.3+|   
Apache Hive 3.1.2+|   
Apache Spark 3+|   
ClickHouse|   
ClickHouse 26+|   
Cloudera Impala 3.1+|   
Cloudera Impala 3.1+ with Native Driver|   
Cloudera Impala with Native Driver|   
DataVirtuality|   
Databricks|   
Denodo 7|   
Denodo 8 & 9|   
Dremio|   
Dremio 11+|   
Dremio 26+ with Arrow Flight SQL|   
Exasol|   
Google BigQuery Legacy SQL|   
Google BigQuery Standard SQL|   
Google Cloud AlloyDB for PostgreSQL|   
Google Cloud PostgreSQL|   
Google Cloud SQL|   
Google Spanner|   
Greenplum|   
HyperSQL|   
IBM Netezza|   
MariaDB|   
Microsoft Azure PostgreSQL|   
Microsoft Azure SQL Database|   
Microsoft Azure Synapse Analytics|   
Microsoft SQL Server 2008+|   
Microsoft SQL Server 2012+|   
Microsoft SQL Server 2016|   
Microsoft SQL Server 2017+|   
MongoBI|   
MongoSQL|   
MySQL|   
MySQL 8.0.12+|   
Oracle|   
Oracle ADWC|   
PostgreSQL 9.5+|   
PostgreSQL pre-9.5|   
PrestoDB|   
PrestoSQL|   
SAP HANA|   
SAP HANA 2+|   
SingleStore|   
SingleStore 7+|   
Snowflake|   
Teradata|   
Trino|   
Vector|   
Vertica|   
  
### Supported database dialects for PDTs

For Looker to support PDTs in your Looker project, your database dialect must also support them.

To support any type of PDTs (either LookML-based or SQL-based), the dialect must support writes to the database, [among other requirements](https://docs.cloud.google.com/looker/docs/derived-tables#pdt_requirements). There are some read-only database configurations that don't allow persistence to work (most commonly Postgres hot-swap replica databases). In these cases, you can use [temporary derived tables](https://docs.cloud.google.com/looker/docs/derived-tables#temporary_derived_tables) instead.

The following table shows the dialects that support persistent [SQL-based derived tables](https://docs.cloud.google.com/looker/docs/derived-tables#sql-based_derived_tables) in the latest release of Looker:

Dialect | Supported?  
---|---  
Actian Avalanche|   
Amazon Athena|   
Amazon Aurora MySQL|   
Amazon Redshift|   
Amazon Redshift 2.1+|   
Amazon Redshift Serverless 2.1+|   
Apache Druid|   
Apache Druid 0.13.x - 0.17.x|   
Apache Druid 0.18+|   
Apache Hive 2.3+|   
Apache Hive 3.1.2+|   
Apache Spark 3+|   
ClickHouse|   
ClickHouse 26+|   
Cloudera Impala 3.1+|   
Cloudera Impala 3.1+ with Native Driver|   
Cloudera Impala with Native Driver|   
DataVirtuality|   
Databricks|   
Denodo 7|   
Denodo 8 & 9|   
Dremio|   
Dremio 11+|   
Dremio 26+ with Arrow Flight SQL|   
Exasol|   
Google BigQuery Legacy SQL|   
Google BigQuery Standard SQL|   
Google Cloud AlloyDB for PostgreSQL|   
Google Cloud PostgreSQL|   
Google Cloud SQL|   
Google Spanner|   
Greenplum|   
HyperSQL|   
IBM Netezza|   
MariaDB|   
Microsoft Azure PostgreSQL|   
Microsoft Azure SQL Database|   
Microsoft Azure Synapse Analytics|   
Microsoft SQL Server 2008+|   
Microsoft SQL Server 2012+|   
Microsoft SQL Server 2016|   
Microsoft SQL Server 2017+|   
MongoBI|   
MongoSQL|   
MySQL|   
MySQL 8.0.12+|   
Oracle|   
Oracle ADWC|   
PostgreSQL 9.5+|   
PostgreSQL pre-9.5|   
PrestoDB|   
PrestoSQL|   
SAP HANA|   
SAP HANA 2+|   
SingleStore|   
SingleStore 7+|   
Snowflake|   
Teradata|   
Trino|   
Vector|   
Vertica|   
  
To support persistent native derived tables (which have LookML-based queries), the dialect must also support a `CREATE TABLE` DDL function. Here is a list of the dialects that support persistent [native (LookML-based) derived tables](https://docs.cloud.google.com/looker/docs/derived-tables#native_derived_tables) in the latest release of Looker:

Dialect | Supported?  
---|---  
Actian Avalanche|   
Amazon Athena|   
Amazon Aurora MySQL|   
Amazon Redshift|   
Amazon Redshift 2.1+|   
Amazon Redshift Serverless 2.1+|   
Apache Druid|   
Apache Druid 0.13.x - 0.17.x|   
Apache Druid 0.18+|   
Apache Hive 2.3+|   
Apache Hive 3.1.2+|   
Apache Spark 3+|   
ClickHouse|   
ClickHouse 26+|   
Cloudera Impala 3.1+|   
Cloudera Impala 3.1+ with Native Driver|   
Cloudera Impala with Native Driver|   
DataVirtuality|   
Databricks|   
Denodo 7|   
Denodo 8 & 9|   
Dremio|   
Dremio 11+|   
Dremio 26+ with Arrow Flight SQL|   
Exasol|   
Google BigQuery Legacy SQL|   
Google BigQuery Standard SQL|   
Google Cloud AlloyDB for PostgreSQL|   
Google Cloud PostgreSQL|   
Google Cloud SQL|   
Google Spanner|   
Greenplum|   
HyperSQL|   
IBM Netezza|   
MariaDB|   
Microsoft Azure PostgreSQL|   
Microsoft Azure SQL Database|   
Microsoft Azure Synapse Analytics|   
Microsoft SQL Server 2008+|   
Microsoft SQL Server 2012+|   
Microsoft SQL Server 2016|   
Microsoft SQL Server 2017+|   
MongoBI|   
MongoSQL|   
MySQL|   
MySQL 8.0.12+|   
Oracle|   
Oracle ADWC|   
PostgreSQL 9.5+|   
PostgreSQL pre-9.5|   
PrestoDB|   
PrestoSQL|   
SAP HANA|   
SAP HANA 2+|   
SingleStore|   
SingleStore 7+|   
Snowflake|   
Teradata|   
Trino|   
Vector|   
Vertica|   
  
> PDTs are not supported for [Snowflake](https://docs.cloud.google.com/looker/docs/db-config-snowflake#oauth) connections that use OAuth.

### Supported database dialects for incremental PDTs

For Looker to support [incremental PDTs](https://docs.cloud.google.com/looker/docs/incremental-pdts) in your Looker project, your database dialect must support [Data Definition Language (DDL)](https://en.wikipedia.org/wiki/Data_definition_language) commands that enable deleting and inserting rows.

The following table shows which dialects support incremental PDTs in the latest release of Looker:

Dialect | Supported?  
---|---  
Actian Avalanche|   
Amazon Athena|   
Amazon Aurora MySQL|   
Amazon Redshift|   
Amazon Redshift 2.1+|   
Amazon Redshift Serverless 2.1+|   
Apache Druid|   
Apache Druid 0.13.x - 0.17.x|   
Apache Druid 0.18+|   
Apache Hive 2.3+|   
Apache Hive 3.1.2+|   
Apache Spark 3+|   
ClickHouse|   
ClickHouse 26+|   
Cloudera Impala 3.1+|   
Cloudera Impala 3.1+ with Native Driver|   
Cloudera Impala with Native Driver|   
DataVirtuality|   
Databricks|   
Denodo 7|   
Denodo 8 & 9|   
Dremio|   
Dremio 11+|   
Dremio 26+ with Arrow Flight SQL|   
Exasol|   
Google BigQuery Legacy SQL|   
Google BigQuery Standard SQL|   
Google Cloud AlloyDB for PostgreSQL|   
Google Cloud PostgreSQL|   
Google Cloud SQL|   
Google Spanner|   
Greenplum|   
HyperSQL|   
IBM Netezza|   
MariaDB|   
Microsoft Azure PostgreSQL|   
Microsoft Azure SQL Database|   
Microsoft Azure Synapse Analytics|   
Microsoft SQL Server 2008+|   
Microsoft SQL Server 2012+|   
Microsoft SQL Server 2016|   
Microsoft SQL Server 2017+|   
MongoBI|   
MongoSQL|   
MySQL|   
MySQL 8.0.12+|   
Oracle|   
Oracle ADWC|   
PostgreSQL 9.5+|   
PostgreSQL pre-9.5|   
PrestoDB|   
PrestoSQL|   
SAP HANA|   
SAP HANA 2+|   
SingleStore|   
SingleStore 7+|   
Snowflake|   
Teradata|   
Trino|   
Vector|   
Vertica|   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
