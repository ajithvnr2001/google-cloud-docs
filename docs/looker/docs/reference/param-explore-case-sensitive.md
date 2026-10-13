---
url: https://docs.cloud.google.com/looker/docs/reference/param-explore-case-sensitive/
title: case_sensitive (for Explores) \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:21.170868+00:00
---

# case_sensitive (for Explores)  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-explore-case-sensitive/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  case_sensitive (for Explores) Stay organized with collections  Save and categorize content based on your preferences. 

> This page refers to the `case_sensitive` parameter that is part of an [Explore](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore).
> 
> `case_sensitive` can also be used as part of a model, described on the [`case_sensitive` (for models)](https://docs.cloud.google.com/looker/docs/reference/param-model-case-sensitive) parameter documentation page.
> 
> `case_sensitive` can also be used as part of a dimension, described on the [`case_sensitive` (for fields)](https://docs.cloud.google.com/looker/docs/reference/param-field-case-sensitive) parameter documentation page.

## Usage
    
    
    explore: explore_name {
      case_sensitive: yes
    }
    

Hierarchy [Model File](https://docs.cloud.google.com/looker/docs/reference/param-model) [`explore`](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) `case_sensitive` |  Default Value `yes`, if the database dialect supports the parameter Accepts A Boolean (`yes` or `no`)  
---|---  
  
## Definition

`case_sensitive` determines whether or not filters will be treated as case-sensitive on a given Explore. All filters related to the Explore are affected, including those added in the Explore UI, Dashboard UI, and [`filters`](https://docs.cloud.google.com/looker/docs/reference/param-field-filters) parameter.

By default, `case_sensitivity` is on and filters are case-sensitive. However, some dialects don't support this parameter, as described in the `case_sensitive` is not supported by some SQL dialects section on this page.

`case_sensitive` works by adjusting the `WHERE` clause of the SQL that Looker generates. When `case_sensitive` is on, filters are expressed with `=` or `LIKE`, such as:
    
    
    WHERE name = 'bob'
    WHERE name LIKE '%bob%'
    

When `case_sensitive` is off, filters are expressed with `ILIKE` (or equivalent), such as:
    
    
    WHERE name ILIKE 'bob'
    

## Examples

Make all filters case-sensitive for the **Product** Explore:
    
    
    explore: product {
      case_sensitive: yes
    }
    

Make all filters not case-sensitive for the **Customer** Explore:
    
    
    explore: customer {
      case_sensitive: no
    }
    

## Common challenges

### `case_sensitive` is not supported by some SQL dialects

By default, `case_sensitivity` is on and filters are case-sensitive. If your SQL dialect doesn't support the `case_sensitive` parameter, case-sensitivity will vary according to your database setup, which will _usually not_ be case-sensitive.

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
  
## Things to know

### You can create a case-sensitive search in MySQL

It is possible to create a case-sensitive search in MySQL, even though MySQL does not support the `case_sensitive` parameter. In MySQL, certain data types — called binary strings — store text as a series of numbers. The capitalization of the text makes a difference in the numbers that are used. Therefore, if you convert your text to a binary string, you can make searches that are case-sensitive. For example:
    
    
    dimension: will_NOT_be_case_sensitive {
      sql: ${TABLE}.something ;;
    }
    
    dimension: will_be_case_sensitive {
      sql: CAST(${TABLE}.something AS BINARY) ;;
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
