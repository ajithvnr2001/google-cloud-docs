---
url: https://docs.cloud.google.com/looker/docs/reference/param-view-publish-as-db-view/
title: publish_as_db_view \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:31.561732+00:00
---

# publish_as_db_view  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-view-publish-as-db-view/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  publish_as_db_view Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This is an advanced topic that assumes that the reader has a solid knowledge of LookML, aggregate tables, and persistent derived tables (PDTs). To start learning about LookML, see the [Get ready for development](https://docs.cloud.google.com/looker/docs/data-modeling) documentation page. To learn about aggregate tables, see the [Aggregate Awareness](https://docs.cloud.google.com/looker/docs/aggregate_awareness#adding_aggregate_tables_to_your_project) documentation page. To learn more about PDTs, see the [Derived tables in Looker](https://docs.cloud.google.com/looker/docs/derived-tables#persistent-derived-tables) documentation page.

## Usage
    
    
    view: my_view {
      derived_table: {
        publish_as_db_view: yes
        ...
      }
    }
    

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) [`derived_table`](https://docs.cloud.google.com/looker/docs/reference/param-view-derived-table) `publish_as_db_view` \- or - [Model File](https://docs.cloud.google.com/looker/docs/reference/param-model) [`explore`](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) [`aggregate_table`](https://docs.cloud.google.com/looker/docs/reference/param-explore-aggregate-table) [`materialization`](https://docs.cloud.google.com/looker/docs/reference/param-explore-aggregate-table#materialization) `publish_as_db_view` |  Default Value `no` Accepts A Boolean (`yes` or `no`) Special Rules

  * The stable database view is published (created) on the next cycle of the [Looker regenerator](https://docs.cloud.google.com/looker/docs/derived-tables#the_looker_regenerator) after the LookML of the persisted table is [deployed to production](https://docs.cloud.google.com/looker/docs/version-control-and-deploying-changes#deploying_to_production) with `publish_as_db_view: yes`
  * Stable database views are supported only for persisted tables that use datagroup or `sql_trigger_value` [persistence strategies](https://docs.cloud.google.com/looker/docs/derived-tables#persistence_strategies). Persisted tables that use `persist_for` aren't supported. 
  * Stable database views are supported only for database connections with `CREATE VIEW` permissions for the temporary schema. 

  
---|---  
  
## Definition

**Notes:**

  * The `publish_as_db_view` parameter is supported only for persisted tables that use the datagroup or `sql_trigger_value` [persistence strategies](https://docs.cloud.google.com/looker/docs/derived-tables#persistence_strategies). Persisted tables that use `persist_for` aren't supported.
  * In addition, the account that Looker uses to connect to your database must have `CREATE VIEW` permissions for the temporary schema on your database. See The database connection must have `CREATE VIEW` permissions on this page for more information.



The `publish_as_db_view` parameter lets you flag persisted tables (which include both [persistent derived tables](https://docs.cloud.google.com/looker/docs/derived-tables#persistent-derived-tables) and [aggregate tables](https://docs.cloud.google.com/looker/docs/aggregate_awareness#adding_aggregate_tables_to_your_project)) for querying outside of Looker. For persisted tables with `publish_as_db_view` set to `yes`, Looker creates a stable database view on the database for the persisted table. The stable database view is created on the database itself so that it can be queried outside of Looker. The concept of a _stable database view_ is different from a _LookML view_ , since LookML views exist on your Looker instance and not in your database itself.

The stable database view will be published (created) on the next cycle of the [Looker regenerator](https://docs.cloud.google.com/looker/docs/derived-tables#the_looker_regenerator) after the persisted table's LookML is [deployed to production](https://docs.cloud.google.com/looker/docs/version-control-and-deploying-changes#deploying_to_production) with `publish_as_db_view: yes`.

**Note:** Once Looker creates the stable database view on the database, the persisted table must be built before you can query the stable database view on the database.

## Examples

### Creating a stable database view for a PDT

Create the `e_flights_pdt` PDT for which a stable database view is created on the database:
    
    
    view: e_flights_pdt {
      derived_table: {
        publish_as_db_view: yes
        datagroup_trigger: e_flights_default_datagroup
        explore_source: ontime {
          timezone: "America/Los_Angeles"
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
    
    

The stable database view for `e_flights_pdt` will be published on the next cycle of the [Looker regenerator](https://docs.cloud.google.com/looker/docs/derived-tables#the_looker_regenerator) after the PDT's LookML is deployed to production. Once Looker builds the PDT, you can then query the stable database view on the database.

### Creating a stable database view for an aggregate table

Create the `weekly_orders` aggregate table for which a stable database view is created on the database:
    
    
    explore: orders {
      aggregate_table: weekly_orders {
        materialization: {
          sql_trigger_value: SELECT CURDATE() ;;
          publish_as_db_view:  yes
        }
        query: {
          dimensions: [orders.status, orders.created_week]
          measures: [orders.count]
        }
      }
    }
    
    

The stable database view for the `weekly_orders` aggregate table will be published on the next cycle of the [Looker regenerator](https://docs.cloud.google.com/looker/docs/derived-tables#the_looker_regenerator) after the aggregate table's LookML is deployed to production. Once Looker builds the aggregate table, you can then query the stable database view on the database.

## Accessing the stable database view

When the stable database view is published for a persisted table, you can query it directly once you get the stable name. There are two ways to get the stable view name for a persisted table:

  * PDT details modal
  * SQL tab of an Explore



### PDT details modal

If you are an admin or a user with the [`see_pdts`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#see_pdts) permission, you can use the **Persistent Derived Tables** page in the **Admin** section of Looker to get the stable database view name for a persisted table:

  1. Click the Looker **Main menu** icon menu and select **Admin** , if the **Admin** menu isn't already displayed. (If you are in the **Explore** or **Develop** section of the Looker **Main menu** , you may have to click the back arrow to see the **Admin** menu.)
  2. From the **Admin** menu, select **Persistent Derived Tables**.
  3. On the **Persistent Derived Tables** page, search for the name of your persisted table.
  4. Click the three-dot menu for your persisted table, and then select **PDT Details**.
  5. In the [**PDT Details** modal](https://docs.cloud.google.com/looker/docs/admin-panel-database-pdts#pdt_details_modal), look for the **Stable Name** field.



To query the stable view table directly, add the scratch schema name before the table name. For example, if the scratch schema name is `tmp`, you can query the stable database view with a command like this:
    
    
    SELECT * from tmp.CL_e_redlook_e_redlook_inc_pdt
    
    

### SQL tab of an Explore

If you don't have access to the **Persistent Derived Tables** admin page, you can use the information that is included on the **SQL** tab of an Explore to determine the stable view name for a persisted table. The stable view name uses this format:
    
    
    SCRATCH_SCHEMA_NAME.CONNECTION_REGISTRATION_KEY_MODEL_NAME_VIEW_NAME
    

For example, if you have a persisted table that is in the model named `faa` and a view with the name `e_flights_pdt`, you only need the scratch schema name and the connection registration key. You can find both from the **SQL** tab in the **Data** section of a query on the persisted table. In the `CREATE TABLE` or `FROM` statement in the **SQL** tab, you can find the information as follows:

  * The connection registration key is two characters; depending on your database dialect, it will follow either a dollar sign or the first underscore in the persisted table's table name.
  * The scratch schema name is the beginning of the string following `CREATE TABLE` or `FROM`, before the "`.`"



In all the following example queries, the connection registration key is `LB`, and the scratch schema name is `tmp`.

Here is an example of a Looker-generated SQL query with a `CREATE TABLE` statement for a dialect that uses a dollar sign before the connection registration key. The view name is `e_flights_pdt`, and the generated derived table name is `tmp.LR$LBC5Q1576702903774_e_flights_pdt`.
    
    
    generate derived table e_flights_pdt
    Building e_flight::e_flights_pdt in dev mode on instance b6ff28049851f1954156526c66ca9912
    CREATE TABLE tmp.LR$LBC5Q1576702903774_e_flights_pdt (INDEX(flight_num)) SELECT
      ontime.flight_num AS `flight_num`
      ontime.carrier AS `carrier,
        (TIMESTAMP(DATE (CONVERT_TZ(ontime.arr_time, 'UTC', 'America/Los_Angeles')))) AS
          `arr_date``
    FROM `flightstats`.`ontime` AS `ontime`
    GROUP BY
      1,
      2,
      3
    -- finished e_flights_pdt => tmp.LR$LBC5Q1576702903774_e_flights_pdt
    
    SELECT
      e_flights_pdt.flight_num AS `e_flights_pdt.flight_num`,
      e_flights_pdt.carrier AS `e_flights_pdt.carrier`
    FROM tmp.LR$LBC5Q1576702903774_e_flights_pdt AS e_flights_pdt
    GROUP BY
      1,
      2
    ORDER BY
      e_flights_pdt.flight_num
    LIMIT 5
    

Here is an example of a Looker-generated SQL query with a `FROM` statement for a dialect that uses an underscore sign before the connection registration key. The view name is `e_flights_pdt`, and the generated derived table name is `tmp.LR_LBFIM1580333699953_e_flights_pdt`.
    
    
    --use existing e flights pdt in tmp.LR_LBFIM1580333699953_e_flights_pdt
    
    SELECT
      e_flights_pdt.id AS `e_flights_pdt.id`,
      DATE(e_flights_pdt.faa_event_date) AS `e_flights_pdt. faa_event_date`
    FROM tmp.LR_LBFIM1580333699953_e_flights_pdt AS e_flights_pdt
    
    GROUP BY 1,2
    ORDER BY DATE(e_flights_pdt.faa_event_date) DESC
    LIMIT 5
    

Again, the stable database view has the following format:
    
    
    SCRATCH_SCHEMA_NAME.CONNECTION_REGISTRATION_KEY_MODEL_NAME_VIEW_NAME
    

Here are all the values:

  * SCRATCH_SCHEMA_NAME is `tmp`
  * CONNECTION_REGISTRATION_KEY is `LB`
  * MODEL_NAME is `faa`
  * VIEW_NAME is `e_flights_pdt`



This, then, is the persisted table's stable database view name:

`tmp.LB_faa_e_flights_pdt`

Once you have the stable database view name, you can query it directly. For example:
    
    
    SELECT * from tmp.LB_faa_e_flights_pdt
    
    

## Things to consider

### Some dialects require additional syntax

If the connection registration key begins with a number, some dialects require double quotes, backticks, brackets, or similar syntax around the second part of the stable database view name. For example, Amazon Redshift requires double quotes; so, if your connection registration key begins with a number, this would be the format:

`[scratch schema name]."[connection registration key]_[model_name]_[view_name]"`

For example, if the connection registration key is `84`, you would put quotes around the second part of the stable table name, after the period. So your queries to the database would look something like this:
    
    
    SELECT * from tmp."84_faa_e_flights_pdt"
    
    

Consult the documentation for your dialect for information on the specific syntax required.

### The database connection must have `CREATE VIEW` permissions

To create a view on your database, the account that Looker uses to connect to your database must have `CREATE VIEW` permissions for the database's temporary schema.

The database username, password, and temporary schema are configured when you [connect Looker to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db).

You can [test your connection](https://docs.cloud.google.com/looker/docs/admin-panel-database-connections#testing_connections) to see if stable view names are supported for your connection. If your dialect supports stable view names and if [PDTs are enabled on the connection](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#persistent_derived_tables), Looker will test the connection to see if it will allow stable views:

  * If the connection allows stable views, the connection test will return a result such as `Can use stable views in temp schema "docsexamples_scratch" in database "flightstats"`.
  * If the connection doesn't allow stable views, the connection test will return a result such as `Cannot use stable views in temp schema "docsexamples" in database "flightstats"`, along with further details such as `CREATE VIEW command denied to user 'docsexamples'`.



## Dialect support for stable database views

The ability to create a persisted table stable database view depends on the database dialect that your Looker connection is using. In the latest release of Looker, the following dialects support the persisted table stable database view:

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
