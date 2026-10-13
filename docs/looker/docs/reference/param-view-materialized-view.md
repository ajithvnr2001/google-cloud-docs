---
url: https://docs.cloud.google.com/looker/docs/reference/param-view-materialized-view/
title: materialized_view \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:31.955492+00:00
---

# materialized_view  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-view-materialized-view/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  materialized_view Stay organized with collections  Save and categorize content based on your preferences. 

## Usage
    
    
    view: my_view {
      derived_table: {
        materialized_view: yes
        ...
      }
    }
    

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) [`derived_table`](https://docs.cloud.google.com/looker/docs/reference/param-view-derived-table) `materialized_view` |  Default Value `no` Accepts A Boolean (`yes` or `no`) Special Rules `materialized_view` is supported only on specific dialects  
---|---  
  
## Definition

> The materialized view functionality is an advanced feature. Depending on your dialect, a materialized view can consume large resources, so it is important that you understand your dialect's implementation of materialized views. See your dialect's documentation for information on the behavior of your dialect and the frequency with which the dialect refreshes data for materialized views.

Materialized views allow you to leverage your database's functionality to persist derived tables in your Looker project. If your database dialect supports materialized views and your [Looker connection](https://docs.cloud.google.com/looker/docs/admin-panel-database-connections) is configured with the [**Persistent Derived Tables**](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#persistent_derived_tables) option enabled, you can create a materialized view by specifying `materialized_view: yes` for a derived table. Materialized views are supported for both [native derived tables](https://docs.cloud.google.com/looker/docs/derived-tables#native_derived_tables) and [SQL-based derived tables](https://docs.cloud.google.com/looker/docs/derived-tables#sql-based_derived_tables).

Similar to a [persistent derived table (PDT)](https://docs.cloud.google.com/looker/docs/derived-tables#persistent_derived_tables_\(pdts\)), a materialized view is a query result that is stored as a table in the scratch schema of your database. The key difference between a PDT and a materialized view is in how tables are refreshed:

  * For PDTs, the [persistence strategy](https://docs.cloud.google.com/looker/docs/derived-tables#persistence_strategies) is defined in Looker, and the persistence is managed by Looker.
  * For materialized views, the database is responsible for maintaining and refreshing the data in the table.



For this reason, the materialized view functionality requires advanced knowledge of your dialect and its features. In most cases, your database will refresh the materialized view any time the database detects new data in the tables that are queried by the materialized view. Materialized views are optimal for scenarios that require real-time data.

If a derived table with a `materialized_view: yes` statement also has a [datagroup](https://docs.cloud.google.com/looker/docs/reference/param-model-datagroup), [`sql_trigger_value`](https://docs.cloud.google.com/looker/docs/reference/param-view-sql-trigger-value), or [`persist_for`](https://docs.cloud.google.com/looker/docs/reference/param-view-persist-for-for-derived-table) parameter, the `materialized_view: yes` statement will take precedence.

## Example

This `e_flights_pdt` derived table has the statement `materialized_view: yes`, so a materialized view is created in the database's scratch schema:
    
    
    view: e_flights_pdt {
      derived_table: {
        materialized_view: yes
        explore_source: ontime {
          column: flight_num {}
          column: carrier {}
          column: arr_date {}
        }
      }
      dimension: flight_num {}
      dimension: carrier {}
      dimension: arr_date {
        type: date
      }
    }
    
    

## When Looker creates the materialized view

Looker generates materialized views in the same way as other PDTs. If you create the materialized view and query it in Development Mode, Looker will create a development version of the materialized view, which can be used for production as well. See the [Persisted tables in Development Mode](https://docs.cloud.google.com/looker/docs/derived-tables#persisted_tables_in_development_mode) section on the [Derived tables in Looker](https://docs.cloud.google.com/looker/docs/derived-tables) documentation page for details.

Otherwise, the materialized view is created during the [Looker regenerator's](https://docs.cloud.google.com/looker/docs/derived-tables#the_looker_regenerator) next cycle, after the associated derived table's LookML is [deployed to production](https://docs.cloud.google.com/looker/docs/version-control-and-deploying-changes#deploying_to_production) with `materialized_view: yes`.

## Stable database views for materialized views

Looker automatically creates a _stable database view_ for each materialized view. The stable database view is created on the database itself, so that it can be queried outside of Looker. This is the same stable view functionality that is used with the [`publish_as_db_view`](https://docs.cloud.google.com/looker/docs/reference/param-view-publish-as-db-view) parameter.

Looker creates the stable view during the Looker regenerator's next cycle, after the materialized view's LookML is deployed to production. Once the stable database view is published, you can query it directly.

Admins or users with the [`see_pdts`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#see_pdts) permission can get the stable database view name from the [**PDT Details** modal](https://docs.cloud.google.com/looker/docs/admin-panel-database-pdts#pdt_details_modal) on the Persistent Derived Tables page in the **Admin** section of Looker.

To query a materialized view directly, just add the scratch schema name before the table name. For example, if the stable database view name is `NN_e_redflight_e_redflight_publish_as_db` and the scratch schema name is `tmp`, you can query the stable database view with a command like this:
    
    
    SELECT * from tmp.NN_e_redflight_e_redflight_publish_as_db
    
    

## Requirements for materialized views

To use materialized views in your Looker project, you need the following:

  * A database dialect that supports materialized views. See the Dialect support for materialized views section on this page for the list of dialects that support materialized views.
  * A scratch schema on your database. This can be any schema on your database, but we recommend creating a new schema that will be used only for this purpose. Your database administrator must configure the schema with write permission for the Looker database user.
  * A [Looker connection](https://docs.cloud.google.com/looker/docs/admin-panel-database-connections) that is configured with the [**Persistent Derived Tables**](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#persistent_derived_tables) option enabled. This is usually set up when you initially configure your Looker connection (see the [Looker dialects](https://docs.cloud.google.com/looker/docs/dialects) documentation page for instructions for your database dialect), but you can also enable PDTs for your connection after the initial setup.
  * A Looker connection with the `CREATE TABLE` permission for the temporary schema on your database. This is the same permission that is required for creating PDTs. In addition, to create the stable database view for the materialized view, the connection must have `CREATE VIEW` permissions for the temporary schema on your database. You can [test the connection](https://docs.cloud.google.com/looker/docs/admin-panel-database-connections#testing_connections) to verify that the connection has these permissions: 
    * If PDTs are enabled on the connection, and the connection has the `CREATE TABLE` permission, the connection test will return a result such as `Can use persistent derived tables in temp schema "docsexamples_scratch" in database "demo_db"`.
    * If the connection allows stable views and the connection has the `CREATE VIEW` permission, the connection test will return a result such as `Can use stable views in temp schema "docsexamples_scratch" in database "flightstats"`.



## Important considerations for materialized views

With materialized views, Looker does not maintain and refresh the data in the table. For this reason, the materialized view functionality requires advanced knowledge of your dialect and its features. Here are some things to consider when you're creating a materialized view:

  * Some dialects have limitations for materialized views, such as default maximum refresh intervals and support for joins. Looker does not generate LookML errors about dialect-specific functionality of materialized views. Instead, Looker will generate an error if the materialized view fails to build, either as an event in the [PDT Event Log](https://docs.cloud.google.com/looker/docs/admin-panel-database-pdts#pdt_event_log_model) or as a runtime error if you try to query the materialized view. Consult your dialect's documentation about limitations for materialized views.
  * Some dialects check for query freshness when materialized views are queried, which may add a small delay to getting query results. Consult your dialect's documentation to see if this is the case for your dialect.
  * Some dialects will attempt to refresh the materialized view incrementally instead of fully rebuilding it. Consult your dialect's documentation for information.
  * If your materialized view uses a base table that is dropped from the database, you may not be able to query the materialized view, and new versions will fail to build.
  * If a derived table with a `materialized_view: yes` statement also has a [datagroup](https://docs.cloud.google.com/looker/docs/reference/param-model-datagroup), [`sql_trigger_value`](https://docs.cloud.google.com/looker/docs/reference/param-view-sql-trigger-value), or [`persist_for`](https://docs.cloud.google.com/looker/docs/reference/param-view-persist-for-for-derived-table) parameter, the `materialized_view: yes` statement will take precedence.
  * Materialized views support the same dialect-specific parameters that are supported by derived tables in general, such as [partitioning](https://docs.cloud.google.com/looker/docs/reference/param-view-partition-keys), [sortkeys](https://docs.cloud.google.com/looker/docs/reference/param-view-sortkeys), and [indexes](https://docs.cloud.google.com/looker/docs/reference/param-view-indexes).
  * In the case of [cascading derived tables](https://docs.cloud.google.com/looker/docs/derived-tables#cascading_derived_tables), materialized views can depend on Looker PDTs, with the following caveats: 
    * You cannot use a derived table with the [`persist_for`](https://docs.cloud.google.com/looker/docs/derived-tables#persist_for) persistence strategy in the definition of a derived table with `materialized_view: yes`. For materialized views, the source table for a materialized view must always be present on the database. `persist_for` derived tables are dropped from your database after the amount of time specified in the `persist_for` parameter, so they are not guaranteed to be present on the database.
    * PDTs rebuild with a unique name, so if a materialized view uses a PDT in its definition, the materialized view will update to point at the new version of the PDT each time the PDT is rebuilt. This means that the materialized view will essentially rebuild from scratch if a dependency completely rebuilds, which may impact performance. In this case, a better option is to reference a base table that is append-only, or to reference an [incremental PDT](https://docs.cloud.google.com/looker/docs/incremental-pdts) that is defined using Looker.



## Dialect support for materialized views

The ability to make a derived table into a materialized view depends on the database dialect that your Looker connection is using. In the current Looker release, the following dialects support materialized views:

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
