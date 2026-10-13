---
url: https://docs.cloud.google.com/looker/docs/reference/param-field-convert-tz/
title: convert_tz \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:34.110440+00:00
---

# convert_tz  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-field-convert-tz/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  convert_tz Stay organized with collections  Save and categorize content based on your preferences. 

## Usage
    
    
    view: view_name {
      dimension: field_name {
        convert_tz: yes | no
      }
    }
    

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) [Field Type](https://docs.cloud.google.com/looker/docs/reference/param-field) `convert_tz` |  Possible Field Types Dimension, Dimension Group, Measure, Filter, Parameter Accepts A Boolean (yes or no)  
---|---  
  
## Definition

Looker has various [time zone settings](https://docs.cloud.google.com/looker/docs/using-time-zone-settings) that convert time-based data between different time zones. Looker does time zone conversion by default. If you don't want Looker to perform a time zone conversion for a particular [`dimension`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension), [`dimension_group`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group) (with [`type: time`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#type_time)), or [`filter` field](https://docs.cloud.google.com/looker/docs/reference/param-field-filter), then you can use the `convert_tz` parameter. This parameter can be useful for fields that are already converted to the appropriate time zone, or in some advanced situations where you need to avoid a double time zone conversion.

In general, time computations (differences, durations, etc.) only work correctly when you operate on time values that are all converted to the same time zone. It is important to keep time zones in mind when writing LookML.

## Examples

Don't perform time zone conversion for the `local_created` dimension group:
    
    
    dimension_group: local_created {
      type: time
      timeframes: [time, date, week, month]
      sql: ${TABLE}.local_created_at ;;
      convert_tz: no
    }
    

## Things to consider

`convert_tz: no` applies only to a dimension, not to a filter that uses the dimension. In other words, filters _always_ perform time zone conversion. When you specify `convert_tz: no`, time-based data values are displayed in the [database time zone](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#database_time_zone), but are filtered using the [query time zone](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#query_time_zone).

Because filters always do time zone conversion, a difference between the database time zone and query time zone could cause data to unexpectedly be included or excluded from a dataset. To avoid this, ensure that the query time zone is set to the same value as the database time zone.

If [**User Specific Time Zones**](https://docs.cloud.google.com/looker/docs/using-time-zone-settings#user_specific_time_zones) is enabled, set the time zone drop-down menu (located next to the **Run** button on Explores, Looks, and dashboards) to the same value as the database time zone. If **User Specific Time Zones** is disabled, set the [**Query Time Zone**](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#query_time_zone) to the same value as the database time zone.

If you're using [custom filters](https://docs.cloud.google.com/looker/docs/filtering-and-limiting#custom_filters), keep time zone conversion enabled to ensure valid date comparisons. If you turn off time zone conversion with `convert_tz: no` and include the field in a custom filter, your date comparisons may be invalid.

## Database dialect support for time zone conversion

For Looker to convert time zones in your Looker project, your database dialect must support time zone conversion. The following table shows which dialects support time zone conversion in the latest release of Looker:

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
