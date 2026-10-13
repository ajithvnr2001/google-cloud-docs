---
url: https://docs.cloud.google.com/looker/docs/reference/param-view-increment-offset/
title: increment_offset \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:30.639317+00:00
---

# increment_offset  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-view-increment-offset/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  increment_offset Stay organized with collections  Save and categorize content based on your preferences. 

## Usage
    
    
    view: my_view {
      derived_table: {
        increment_key: ["created_date"]
        increment_offset: 1
        ...
      }
    }
    

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) [`derived_table`](https://docs.cloud.google.com/looker/docs/reference/param-view-derived-table) `increment_offset` \- or - [Model File](https://docs.cloud.google.com/looker/docs/reference/param-model) [`explore`](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) [`aggregate_table`](https://docs.cloud.google.com/looker/docs/reference/param-explore-aggregate-table) [`materialization`](https://docs.cloud.google.com/looker/docs/reference/param-explore-aggregate-table#materialization) `increment_offset` |  Default Value 0 Accepts An integer Special Rules

  * `increment_offset` is supported only in conjunction with [`increment_key`](https://docs.cloud.google.com/looker/docs/reference/param-view-increment-key)
  * `increment_offset` and `increment_key` are supported only with [persistent tables](https://docs.cloud.google.com/looker/docs/derived-tables#adding_persistence)
  * `increment_offset` and `increment_key` are supported only for specific dialects

  
---|---  
  
## Definition

You can create [incremental PDTs](https://docs.cloud.google.com/looker/docs/incremental-pdts) in your project if your dialect supports them. An incremental PDT is a [persistent derived table (PDT)](https://docs.cloud.google.com/looker/docs/derived-tables#persistent_derived_table) that Looker builds by appending fresh data to the table, instead of rebuilding the table in its entirety. See the [Incremental PDTs](https://docs.cloud.google.com/looker/docs/incremental-pdts) documentation page for more information.

The [`increment_key`](https://docs.cloud.google.com/looker/docs/reference/param-view-increment-key) parameter specifies the time period for which fresh data should be queried and appended to the aggregate table. The `increment_offset` parameter is an optional parameter that you can use if you want to rebuild the table for previous time periods at the same time that fresh data is appended to the table. The `increment_offset` parameter defines the number of previous time periods that will be rebuilt when appending data to an incremental PDT.

The `increment_offset` parameter is useful in the case of late-arriving data, where previous time periods may have new data that wasn't included when the corresponding increment was originally built and appended to the PDT.

The default `increment_offset` value is `0`, which means that only the new data from the current increment is appended to the table. If you set the `increment_offset` to `1`, late-arriving data from the previous increment will be added to the table in addition to the new data from the current time increment.

> See the [Incremental PDTs](https://docs.cloud.google.com/looker/docs/incremental-pdts#example_scenarios) documentation page for some example scenarios that illustrate how incremental PDTs work and that show the interaction of `increment_key`, `increment_offset`, and persistence strategy.

See the Supported database dialects for incremental PDTs section on this page for the list of dialects that support incremental PDTs.

## Example

For example, this PDT is rebuilt in increments of one day (`increment_key: event_day`), going back three days (`increment_offset: 3`):
    
    
    derived_table: {
      datagroup_trigger: usagetable_etl
      increment_key: "event_day"
      increment_offset: 3
      explore_source: events {
        column: name { field: account.name }
        column: account_id { field: account.id }
        column: database_dialect {}
        column: count_events {}
        column: event_day {}
       }
     }
    

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
