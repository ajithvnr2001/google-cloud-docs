---
url: https://docs.cloud.google.com/looker/docs/custom-calendars/
title: Using custom calendars in Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:13.343037+00:00
---

# Using custom calendars in Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/custom-calendars/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Using custom calendars in Looker Stay organized with collections  Save and categorize content based on your preferences. 

For dialects that support it, the custom calendar feature in Looker lets you define a custom calendar in your database, such as a specific fiscal or retail calendar, and then apply the calendar to a date-based dimension group in your LookML model. Your users can then create Explore queries using your custom timeframes, such as `custom_week`, `custom_period`, as if they were standard timeframes.

## Prerequisites

Before using custom calendars, ensure the following prerequisites are met:

  * You must have a Looker connection to a dialect that supports custom calendars.
  * You must create a calendar table in your database that you can then model as a view in Looker. Looker uses the calendar table in your database to calculate custom timeframes. See the Create a calendar table in your database section for more information.
  * Your LookML project must use the new LookML runtime. If the [**Use Legacy LookML Runtime**](https://docs.cloud.google.com/looker/docs/legacy-feature-schedule#new_lookml_runtime) legacy feature is enabled on your instance, you must add the [`new_lookml_runtime: yes`](https://docs.cloud.google.com/looker/docs/reference/param-manifest-new-lookml-runtime) statement to your project's manifest file.



## Creating a custom calendar

To implement a custom calendar, you need to perform these general steps that are described in the following sections:

  1. Create your calendar table in your database
  2. Define your custom calendar view in LookML
  3. Create a custom calendar dimension group



### Create a calendar table in your database

To calculate dates for custom calendars, Looker needs a dedicated calendar table in your database that defines your custom timeframes. Your table must have a reference date column that uses the standard calendar date. Looker joins your calendar table to your data tables (such as an `orders` table) based on the reference date column.

The column names in the calendar table are flexible. When you define the custom calendar view in LookML, you will use the `calendar_definition` block to map the columns in your database to standard custom timeframe names. 

The following is an example table schema for a calendar table named `fiscal_calendar_table`.

Column Name | Data Type | Description  
---|---|---  
`reference_date` | `DATE` | The standard calendar date (such as '2023-01-01'). Used for joining. Should be a unique or primary key.  
`fiscal_day_num` | `INTEGER` | The numeric custom date or ordinal day of the year (such as 1).  
`fiscal_year` | `VARCHAR` | The fiscal year (such as 'FY2023').  
`fiscal_year_num` | `INTEGER` | The numeric fiscal year (such as 2023).  
`fiscal_quarter_of_year` | `VARCHAR` | The fiscal quarter (such as 'FQ1').  
`fiscal_quarter_of_year_num` | `INTEGER` | The numeric fiscal quarter (such as 1).  
`fiscal_week_of_year` | `VARCHAR` | The fiscal week of the year (such as 'Week01', 'FW01').  
`fiscal_week_of_year_num` | `INTEGER` | The numeric fiscal week of the year (such as 1).  
`fiscal_period_of_year` | `VARCHAR` | A custom period name (such as 'P01').  
`fiscal_period_of_year_num` | `INTEGER` | The numeric custom period (such as 1).  
`season` | `VARCHAR` | A custom season name (such as 'Winter').  
`season_num` | `INTEGER` | The numeric custom season (such as 1).  
`prev_week_num` | `INTEGER` | The ordinal value for the previous week (such as 52 or 53). Looker needs this value to calculate [period-over-period measures](https://docs.cloud.google.com/looker/docs/period-over-period) in cases where the current week is 1 and the previous week in your calendar isn't 52. Using `prev_week_num` is necessary only if you want to use period-over-period measures with custom calendars, and only if your custom calendar doesn't have 52 weeks.  
`prev_day_num` | `INTEGER` | The ordinal value for the previous day (such as 364 or 371). Looker needs this value to calculate period-over-period measures in cases where the current day is 1 and the previous day in your calendar isn't 364. Using `prev_day_num` is necessary only if you want to use period-over-period measures with custom calendars, and only if your custom calendar doesn't have 364 days.  
  
To illustrate, here are some sample rows from the `fiscal_calendar_table` table:

`reference_date` | `fiscal_day_num` | `fiscal_year` | `fiscal_year_num` | `fiscal_period` | `fiscal_period_num` | `prev_week_num` | `prev_day_num`  
---|---|---|---|---|---|---|---  
`2023-12-25` | `359` | `FY2024` | `2024` | `P01` | `1` | `51` | `358`  
`2023-12-26` | `360` | `FY2024` | `2024` | `P01` | `1` | `51` | `359`  
`2024-01-01` | `1` | `FY2024` | `2024` | `P02` | `2` | `52` | `364`  
`2024-01-02` | `2` | `FY2024` | `2024` | `P02` | `2` | `52` | `1`  
  
### Define your custom calendar view in LookML

After you have created a calendar table in your database, you need to create a LookML view to model the database calendar table. 

**Tip:** The easiest way to create the view file is to use the [**Create View From Table**](https://docs.cloud.google.com/looker/docs/creating-project-files#adding_a_new_view_from_an_existing_database_table) option in the Looker IDE to have Looker automatically model the fields of your table. After Looker creates the view file, you can then add the `calendar_definition` parameter block, modify any of the automatically-created dimensions, and add any other dimension definitions you need.

The custom calendar view file must include the following:

  * The [`sql_table_name`](https://docs.cloud.google.com/looker/docs/reference/param-view-sql-table-name) parameter that points to the custom calendar table in your database. 
  * The [`calendar_definition`](https://docs.cloud.google.com/looker/docs/reference/param-view-calendar-definition) block to map your table's columns to the Looker custom timeframe types.
  * [`dimension`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension) parameters to model the columns of the custom calendar table in your database. 



Here is an example view file called `fiscal_calendar.view.lkml` that models the example `fiscal_calendar_table`:
    
    
    view: fiscal_calendar {
      sql_table_name: fiscal_calendar_table ;;
      calendar_definition: {
        reference_date: reference_date
        timeframe_mapping: {
          custom_year: fiscal_year
          custom_quarter: fiscal_quarter_of_year
          custom_date: fiscal_date
          custom_week: fiscal_week_of_year
          custom_period: fiscal_period_of_year
          custom_season: season
        }
        timeframe_ordinal_mapping: {
          custom_year: fiscal_year_num
          custom_quarter: fiscal_quarter_of_year_num
          custom_date: fiscal_day_num
          custom_week: fiscal_week_of_year_num
          custom_period: fiscal_period_of_year_num
          custom_season: season_num
        }
        previous_ordinal_mapping: {
          custom_week: prev_week_num
          custom_date: prev_day_num
        }
      }
    
      dimension: reference_date {
        type: date
        primary_key: yes
        sql: ${TABLE}.reference_date ;; # Assuming column name is reference_date
      }
    
      dimension: fiscal_date {
        type: string
        sql: FORMAT_TIMESTAMP('%Y-%m-%d', ${TABLE}.reference_date) ;;
      }
    
      dimension: fiscal_day_num {
        type: number
        sql: ${TABLE}.fiscal_day_num ;;
      }
    
      dimension: fiscal_year {
        type: string
        sql: ${TABLE}.fiscal_year ;;
      }
    
      dimension: fiscal_year_num {
        type: number
        sql: ${TABLE}.fiscal_year_num ;;
      }
    
      # ... other dimensions for quarters, weeks, periods, seasons, etc. ...
    
      # Example placeholder dimensions for unused timeframes
      dimension: season {
        type: string
        sql: 'N/A' ;;
        hidden: yes
      }
      dimension: season_num {
        type: number
        sql: 0 ;;
        hidden: yes
      }
    }
    
    

See the [`calendar_definition`](https://docs.cloud.google.com/looker/docs/reference/param-view-calendar-definition) parameter page for details on the `calendar_definition` parameters.

### Create a custom calendar dimension group

After you have created a calendar table in your database and modeled the database calendar table in LookML, you can create a [dimension group of `type: custom_calendar`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#custom_calendar_type) that is based on the custom calendar view.

For example, here is a view filed named `orders.view.lkml` that defines a custom calendar dimension group.
    
    
    include: "/views/fiscal_calendar.view"
    
    view: orders {
      sql_table_name: public.orders ;;
    
      dimension_group: created {
        type: custom_calendar
    
        # Optional list of allowed timeframes
        custom_timeframes: [
          custom_date,
          custom_week,
          custom_year
        ]
        sql: ${TABLE}.created_at ;;
        based_on_calendar: fiscal_calendar  # This links to your calendar view
      }
    }
    

With this LookML, Looker will automatically create a new set of custom timeframes for the `created` dimension group (such as "Fiscal Year", "Fiscal Week"). Users can then use these fields for exploring, reporting, and filtering.

See the [`dimension_group`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#custom_calendar_type) documentation page for the details on creating a dimension group for custom calendars.

## Things to consider

Note the following limitations with custom calendars:

  * **Filtered measures:** Custom calendars aren't supported for filtered measures: You can't reference a custom calendar dimension in the [`filters`](https://docs.cloud.google.com/looker/docs/reference/param-field-filters) parameter of a measure.
  * **Advanced filters:** Custom calendars aren't supported in advanced filters: You can't reference a custom calendar dimension in [Looker filter expressions](https://docs.cloud.google.com/looker/docs/filter-expressions#date_and_time).
  * **Symmetric aggregates:** In some complex join scenarios, [symmetric aggregates](https://docs.cloud.google.com/looker/docs/working-with-joins#symmetric-aggregates) may not be fully supported for queries involving custom calendar dimensions.
  * **Dimension fill:** Looker cannot [dimension fill](https://docs.cloud.google.com/looker/docs/creating-visualizations#filling_in_missing_dates_and_values) missing dates for custom calendar dimensions.
  * **Filtering beyond calendar boundaries:** If a filter is applied to a custom timeframe that results in a date that is not in the calendar then unexpected results may be returned. This has to do with the ordinal arithmetic that is used to calculate the beginning of a period.
  * **`OR` filters:** [`OR` filters](https://docs.cloud.google.com/looker/docs/and-or-filters-in-explores) are not supported for queries with custom calendars.
  * **Timezone conversion behavior:** Looker honors the existing timezone conversion semantics. That is, if the database and query timezone match then no timezone conversion is applied. If they disagree, then Looker applies the timezone conversion. You can override this behavior by specifying [`convert_tz: no`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#convert_tz) to your custom calendar dimension group.
  * **Default sorting:** Looker applies a default sort to the first date field when custom calendar fields are selected. The user can then [specify different data sorting](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#sorting_data).
  * **Custom calendar filters:** Custom calendar dimensions support specific filter options, such as **is in the last 3 custom years** or **is this custom period**. For more information, see the [Custom calendar filters](https://docs.cloud.google.com/looker/docs/filtering-and-limiting#custom_calendar_filters) section of the **Filtering and limiting data** documentation page.



## Supported database dialects for custom calendars

The following table shows which dialects support custom calendars in the latest release of Looker:

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

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
