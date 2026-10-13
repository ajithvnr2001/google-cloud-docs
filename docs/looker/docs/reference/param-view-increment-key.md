---
url: https://docs.cloud.google.com/looker/docs/reference/param-view-increment-key/
title: increment_key \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:30.737316+00:00
---

# increment_key  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-view-increment-key/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  increment_key Stay organized with collections  Save and categorize content based on your preferences. 

## Usage
    
    
    view: my_view {
      derived_table: {
        increment_key: "created_date"
        ...
      }
    }
    

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) [`derived_table`](https://docs.cloud.google.com/looker/docs/reference/param-view-derived-table) `increment_key` \- or - [Model File](https://docs.cloud.google.com/looker/docs/reference/param-model) [`explore`](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) [`aggregate_table`](https://docs.cloud.google.com/looker/docs/reference/param-explore-aggregate-table) [`materialization`](https://docs.cloud.google.com/looker/docs/reference/param-explore-aggregate-table#materialization) `increment_key` |  Default Value None Accepts The name of a time-based LookML dimension Special Rules `increment_key` is supported only with [persistent tables](https://docs.cloud.google.com/looker/docs/derived-tables#adding_persistence), and only for specific dialects  
---|---  
  
## Definition

You can create [incremental PDTs](https://docs.cloud.google.com/looker/docs/incremental-pdts) in your project if your dialect supports them. An incremental PDT is a [persistent derived table (PDT)](https://docs.cloud.google.com/looker/docs/derived-tables#persistent_derived_table) that Looker builds by appending fresh data to the table, instead of rebuilding the table in its entirety. See the [Incremental PDTs](https://docs.cloud.google.com/looker/docs/incremental-pdts) documentation page for more information.

`increment_key` is the parameter that makes a PDT into an incremental PDT by specifying the time increment for which fresh data should be queried and appended to the PDT. In addition to the `increment_key`, you can optionally provide an [`increment_offset`](https://docs.cloud.google.com/looker/docs/reference/param-view-increment-offset) to specify the number of previous time periods (at the increment key's granularity) that are rebuilt to account for late-arriving data.

> The `increment_key` for a PDT is independent of the PDT's persistence trigger. See the [Incremental PDTs](https://docs.cloud.google.com/looker/docs/incremental-pdts#example_scenarios) documentation page for some example scenarios that show the interaction of `increment_key`, `increment_offset`, and persistence strategy.
> 
> The `increment_key` parameter works only with supported dialects, and only with tables that have a [persistence strategy](https://docs.cloud.google.com/looker/docs/derived-tables#adding_persistence), such as PDTs and [aggregate tables](https://docs.cloud.google.com/looker/docs/aggregate_awareness#adding_aggregate_tables_to_your_project) (which are a type of PDT).

The `increment_key` must specify a time-based LookML dimension:

  * For [LookML-based PDTs](https://docs.cloud.google.com/looker/docs/derived-tables#native_derived_tables), the `increment_key` must be based on a LookML dimension that is defined in the view on which the PDT's [`explore_source`](https://docs.cloud.google.com/looker/docs/reference/param-view-explore-source) is based. See the Creating an incremental LookML-based PDT section on this page for an example.
  * For [aggregate tables](https://docs.cloud.google.com/looker/docs/aggregate_awareness#adding_aggregate_tables_to_your_project), the `increment_key` must be based on a LookML dimension that is defined in the view on which the aggregate table's Explore is based. See the Creating an incremental aggregate table section on this page for an example.
  * For [SQL-based PDTs](https://docs.cloud.google.com/looker/docs/derived-tables#sql-based_derived_tables), the `increment_key` must be based on a LookML dimension that is defined inside the PDT's view file. See the Creating an incremental SQL-based PDT on this page for an example.



In addition, the `increment_key` must be:

  * A truncated absolute time, such as day, month, year, or fiscal quarter. Timeframes such as day of the week are not supported.
  * A timestamp that increases predictably with new data, such as order created date. In other words, a timestamp should be used as an increment key only if the newest data that's added to the table also has the latest timestamp. A timestamp such as user birthday wouldn't work as an increment key, since a birthday timestamp does not increase reliably with new users being added to the table.



## Creating an incremental LookML-based PDT

To make a [LookML-based (native)](https://docs.cloud.google.com/looker/docs/derived-tables#native_derived_tables) PDT into an incremental PDT, use the `increment_key` parameter to specify the name of a time-based LookML dimension. The dimension must be defined in the view on which the PDT's [`explore_source`](https://docs.cloud.google.com/looker/docs/reference/param-view-explore-source) is based.

For example, here is a view file for a PDT based on LookML, using the [`explore_source`](https://docs.cloud.google.com/looker/docs/reference/param-view-explore-source) LookML parameter. The PDT is created from the `flights` Explore, which in this case is based on the `flights` view:
    
    
    view: flights_lookml_incremental_pdt {
      derived_table: {
        indexes: ["id"]
        increment_key: "departure_date"
        increment_offset: 3
        datagroup_trigger: flights_default_datagroup
        distribution_style: all
        explore_source: flights {
          column: id {}
          column: carrier {}
          column: departure_date {}
        }
      }
    
      dimension: id {
        type: number
      }
      dimension: carrier {
        type: string
      }
      dimension: departure_date {
        type: date
      }
    }
    

This table will build in its entirety the first time a query is run on it. After that, the PDT will be rebuilt in increments of one day (`increment_key: departure_date`), going back three days (`increment_offset: 3`).

The `departure_date` dimension is actually the `date` [timeframe](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#timeframes) from the `departure` dimension group. (See the [`dimension_group`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group) parameter documentation page for an overview of how dimension groups work.) The dimension group and timeframe are both defined in the `flights` view, which is the `explore_source` for this PDT. Here is how the `departure` dimension group is defined in the `flights` view file:
    
    
    ...
      dimension_group: departure {
        type: time
        timeframes: [
          raw,
          date,
          week,
          month,
          year
        ]
        sql: ${TABLE}.dep_time ;;
      }
    ...
    
    

## Creating an incremental SQL-based PDT

> Looker suggests that you use [LookML-based (native) derived tables](https://docs.cloud.google.com/looker/docs/derived-tables#native_derived_tables) as the base for incremental PDTs, as opposed to using [SQL-based derived tables](https://docs.cloud.google.com/looker/docs/derived-tables#sql-based_derived_tables). Native derived tables inherently handle the complex logic that's required for incremental PDTs. SQL-based PDTs rely on manually created logic, which is prone to error when it's used with highly complex functionality.

To define an incremental [SQL-based](https://docs.cloud.google.com/looker/docs/derived-tables#sql-based_derived_tables) PDT, use `increment_key` and (optionally) `increment_offset` as you would with a LookML-based PDT. However, because SQL-based PDTs aren't based on LookML view files, there are additional requirements for making a SQL-based PDT into an incremental PDT:

  * You must base the increment key on a time-based LookML dimension that you define in the PDT's view file.
  * You must provide a `{% incrementcondition %}` Liquid filter in the PDT to connect the increment key to the database time column that the increment key is based on. The `{% incrementcondition %}` filter must specify the name of the column in your database, not a SQL alias nor the name of a dimension that is based on the column (see the following example).



The basic format for the Liquid filter is:
    
    
       WHERE {% incrementcondition %} database_table_name.database_time_column {% endincrementcondition %}
    

For example, here is the view file for a SQL-based PDT that is rebuilt in increments of one day (`increment_key: "dep_date"`), where data from the last three days will be added to the table when it is rebuilt (`increment_offset: 3`):
    
    
    view: sql_based_incremental_date_pdt {
      derived_table: {
        datagroup_trigger: flights_default_datagroup
        increment_key: "dep_date"
        increment_offset: 3
        distribution_style: all
        sql: SELECT
            flights.id2  AS "id",
            flights.origin  AS "origin",
            DATE(flights.leaving_time )  AS "departure"
          FROM public.flights  AS flights
          WHERE {% incrementcondition %} flights.leaving_time {%  endincrementcondition %}
              ;;
      }
    
      dimension_group: dep {
        type: time
        timeframes: [date, week, month, year]
        datatype: date
        sql:  ${TABLE}.departure
        ;;
      }
      dimension: id {
          type: number
        }
        dimension: origin {
          type: string
      }
    }
    
    

Note the following about this example:

  * The derived table is based on a SQL statement. The SQL statement creates a column in the derived table that is based on the `flights.leaving_time` column in the database. The column is given the alias `departure`.
  * The PDT's view file defines a dimension group called `dep`. 
    * The dimension group's [`sql`](https://docs.cloud.google.com/looker/docs/reference/param-field-sql) parameter indicates that the dimension group is based on the `departure` column in the derived table.
    * The dimension group's [`timeframes`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#timeframes) parameter includes `date` as a timeframe.
  * The derived table's `increment_key` uses the `dep_date` dimension, which is a dimension based on the `date` timeframe of the `dep` dimension group. (See the [`dimension_group`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group) parameter documentation page for an overview of how dimension groups work.)
  * The `{% incrementcondition %}` Liquid filter is used to connect the increment key to the `flights.leaving_time` column in the database. 
    * The `{% incrementcondition %}` must specify the name of a `TIMESTAMP` column in your database (or it must evaluate to a `TIMESTAMP` column in your database).
    * The `{% incrementcondition %}` must evaluate against what is available in the `FROM` clause that defines your PDT, such as columns from the table that is specified in the `FROM` clause. The `{% incrementcondition %}` cannot refer to the result of the `SELECT` statement, such as an alias that has been given to a column in the SQL statement, or the name of a dimension that is based on the column. In this example, the `{% incrementcondition %}` is `flights.leaving_time`. Since the `FROM` clause specifies the `flights` table, the `{% incrementcondition %}` can refer to columns from the `flights` table.
    * The `{% incrementcondition %}` must point to the same database column that is used for the increment key. In this example, the increment key is `dep_date`, a dimension that is defined by the `departure` column in the PDT, which is an alias for the `flights.leaving_time` column in the database. Therefore, the filter points to `flights.leaving_time`:


    
    
    WHERE {% incrementcondition %} flights.leaving_time {%  endincrementcondition %}
    

You can add to the `WHERE` clause to create other filters. For example, if the database table goes back many years, you can create a filter so that the initial build of the PDT uses only data after a certain date. This `WHERE` creates a PDT with data from after January 1, 2020:
    
    
    WHERE {% incrementcondition %} flights.leaving_time {%  endincrementcondition %}
      AND flights.leaving_time > '2020-01-01'
    

You can also use the `WHERE` clause to parse data in SQL into a timestamp and then give it an alias. For example, the following incremental PDT uses a 15-minute increment that is based on the `text_column`, which is string data that has been parsed into timestamp data:
    
    
    view: sql_based_incremental_15min_pdt {
      derived_table: {
        datagroup_trigger: flights_default_datagroup
        increment_key: "event_minute15"
        increment_offset: 1
        sql: SELECT PARSE_TIMESTAMP("%c", flights.text_column) as parsed_timestamp_column,
            flights.id2  AS "id",
            flights.origin  AS "origin",
          FROM public.flights  AS flights
          WHERE {% incrementcondition %} PARSE_TIMESTAMP("%c", flights.text_column)
              {% endincrementcondition %} ;;
      }
    
      dimension_group: event {
        type: time
        timeframes: [raw, minute15, hour, date, week, month, year]
        datatype: timestamp
        sql:  ${TABLE}.parsed_timestamp_column ;;
      }
      dimension: id {
        type: number
      }
      dimension: origin {
        type: string
      }
    }
    

You can use the alias for the SQL in the dimension group `sql` definition, but you must use the SQL expression in the `WHERE` clause. And then, because `minute15` was set up as timeframe in the `event` dimension group, you can then use `event_minute15` as the increment key to get a 15-minute increment for the PDT.

## Creating an incremental aggregate table

To make an incremental [aggregate table](https://docs.cloud.google.com/looker/docs/aggregate_awareness#adding_aggregate_tables_to_your_project), add `increment_key` and (optionally) `increment_offset` under the [`materialization`](https://docs.cloud.google.com/looker/docs/reference/param-explore-aggregate-table#materialization) parameter of the [`aggregate_table`](https://docs.cloud.google.com/looker/docs/reference/param-explore-aggregate-table) parameter. Use the `increment_key` parameter to specify the name of a time-based LookML dimension. The dimension must be defined in the view on which the aggregate table's Explore is based.

For example, this aggregate table is based on the `accidents` Explore, which in this case is based on the `accidents` view. The aggregate table is rebuilt in increments of one week (`increment_key: event_week`), going back two weeks (`increment_offset: 2`):
    
    
    explore: accidents {
      . . .
      aggregate_table: accidents_daily {
        query: {
          dimensions: [event_date, id, weather_condition]
          measures: [count]
        }
        materialization: {
          datagroup_trigger: flights_default_datagroup
          increment_key: "event_week"
          increment_offset: 2
        }
      }
    }
    
    

The increment key uses the `event_week` dimension, which is based on the `week` [timeframe](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#timeframes) from the `event` dimension group. (See the [`dimension_group`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group) parameter documentation page for an overview of how dimension groups work.) The dimension group and timeframe are both defined in the `accidents` view:
    
    
    . . .
    view: accidents {
      . . .
      dimension_group: event {
          type: time
          timeframes: [
            raw,
            date,
            week,
            year
          ]
          sql: ${TABLE}.event_date ;;
      }
      . . .
    }
    

## Things to consider

### Optimize the source table for time-based queries

Make sure that the incremental PDT's source table is optimized for time-based queries. Specifically, the time-based column that's used for the increment key must have an optimization strategy, such as [partitioning](https://docs.cloud.google.com/looker/docs/reference/param-view-partition-keys), [sortkeys](https://docs.cloud.google.com/looker/docs/reference/param-view-sortkeys), [indexes](https://docs.cloud.google.com/looker/docs/reference/param-view-indexes), or whatever optimization strategy is supported for your dialect. Source table optimization is strongly recommended because each time the incremental table is updated, Looker queries the source table to determine the latest values of the time-based column that's being used for the increment key. If the source table isn't optimized for these queries, Looker's query for the latest values may be slow and expensive.

## Supported database dialects for incremental PDTs

For Looker to support incremental PDTs in your Looker project, your database dialect must support [Data Definition Language (DDL)](https://en.wikipedia.org/wiki/Data_definition_language) commands that enable deleting and inserting rows.

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
