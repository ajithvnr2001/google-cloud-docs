---
url: https://docs.cloud.google.com/looker/docs/reference/param-field-case-sensitive/
title: case_sensitive (for fields) \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:35.229657+00:00
---

# case_sensitive (for fields)  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-field-case-sensitive/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  case_sensitive (for fields) Stay organized with collections  Save and categorize content based on your preferences. 

> This page refers to the `case_sensitive` parameter that is part of a [dimension](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension) or [filter](https://docs.cloud.google.com/looker/docs/reference/param-field-filter).
> 
> `case_sensitive` can also be used as part of a model, described on the [`case_sensitive` (for models)](https://docs.cloud.google.com/looker/docs/reference/param-model-case-sensitive) parameter documentation page.
> 
> `case_sensitive` can also be used as part of an Explore, described on the [`case_sensitive` (for Explores)](https://docs.cloud.google.com/looker/docs/reference/param-explore-case-sensitive) parameter documentation page.

## Usage
    
    
    view: view_name {
      dimension: field_name {
        case_sensitive:  no
      }
    }
    

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) [Field Type](https://docs.cloud.google.com/looker/docs/reference/param-field) `case_sensitive` |  Possible Field Types Dimension, Filter Accepts A Boolean (yes or no)  
---|---  
  
## Definition

When a [`dimension`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension) or [`filter`](https://docs.cloud.google.com/looker/docs/reference/param-field-filter) field is used as a filter, you can change its case-sensitivity by using the `case_sensitive` parameter. The `case_sensitive` parameter works with most dialects, although some dialects don't have the necessary SQL functions.

By default, `case_sensitivity` is on and filters are case-sensitive. However, some dialects don't support this parameter, as described in the `case_sensitive` is not supported by some SQL dialects section on this page.

## Examples

Stop filters on the `name` dimension from being case-sensitive:
    
    
    dimension: name {
      sql: ${TABLE}.name ;;
      case_sensitive: no
    }
    

## Common challenges

### `case_sensitive` is not supported by some SQL dialects

By default, `case_sensitivity` is on and filters are case-sensitive. If your SQL dialect doesn't support the `case_sensitive` parameter, case sensitivity will vary according to your database setup, which will _usually_ not be case-sensitive.

For Looker to support `case_sensitive` in your Looker project, your database dialect must also support it. The following table shows which dialects support `case_sensitive` in the latest release of Looker:

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
