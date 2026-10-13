---
url: https://docs.cloud.google.com/looker/docs/reference/param-field-allow-approximate-optimization/
title: allow_approximate_optimization \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:33.342513+00:00
---

# allow_approximate_optimization  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-field-allow-approximate-optimization/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  allow_approximate_optimization Stay organized with collections  Save and categorize content based on your preferences. 

## Usage
    
    
    view: view_name {
      measure: field_name {
        allow_approximate_optimization: yes 
      }
    }
    

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) [Field Type](https://docs.cloud.google.com/looker/docs/reference/param-field) `allow_approximate_optimization` |  Possible Field Types Measure Default Value `no` Accepts A Boolean (yes or no)  
---|---  
  
## Definition

For dialects that support [HyperLogLog sketches](https://en.wikipedia.org/wiki/HyperLogLog), Looker can leverage the HyperLogLog algorithm to approximate distinct counts for aggregate tables.

The `allow_approximate_optimization: yes` statement enables Looker to store HyperLogLog sketches in aggregate tables, which means that Looker can use approximations for distinct counts for [aggregate awareness](https://docs.cloud.google.com/looker/docs/aggregate_awareness).

See the Dialect support for distinct counts with aggregate awareness section on this page for the list of dialects that support distinct counts for aggregate tables using HyperLogLog sketches.

In general, distinct counts can't be supported with aggregate awareness because you can't get accurate data if you try to aggregate distinct counts. For example, if you are counting the distinct users on a website, there may be a user who came to the website twice, three weeks apart. If you tried to apply a weekly aggregate table to get a monthly count of distinct users on your website, that user would be counted twice in your monthly distinct count query, and the data would be incorrect.

One workaround for this is to create an aggregate table that exactly matches an Explore query, as described on the [Aggregate awareness](https://docs.cloud.google.com/looker/docs/aggregate_awareness#exact_match) documentation page. When the Explore query and an aggregate table query are the same, distinct count measures do provide accurate data, so they can be used for aggregate awareness.

The other option is to use approximations for distinct counts. The HyperLogLog algorithm is known to have about a 2% potential error. The `allow_approximate_optimization` parameter requires your Looker developers to acknowledge that it's okay to use approximate data for the measure so that the measure may be calculated approximately from aggregate tables.

With aggregate awareness, there are two cases where distinct counts come into play:

  * The first case is with measures of [`type: count_distinct`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#count_distinct).
  * The second case is with measures of [`type: count`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#count) that are actually being rendered by Looker as `count_distinct` measure types. As discussed on the [Aggregate awareness](https://docs.cloud.google.com/looker/docs/aggregate_awareness#symmetric_aggregates_for_explores_with_joins) documentation page, Looker renders `count` measures as `count_distinct` to avoid fanout miscalculations in Explores that [join](https://docs.cloud.google.com/looker/docs/reference/param-explore-join) multiple database tables.



In both of these cases, if your dialect supports HyperLogLog sketches, you can add the `allow_approximate_optimization: yes` statement to measures to enable approximate values. You can then include these measures in aggregate tables.

> Even for measures defined with `allow_approximate_optimization: yes`, Looker will return exact data when possible. For example, if the dimensions in an Explore query are a perfect match of the dimensions in an aggregate table, Looker can provide exact data for distinct counts, without having to approximate. In this case, you will see in the [Explore's SQL tab](https://docs.cloud.google.com/looker/docs/aggregate_awareness#sql_tab) that distinct count measures are being used for aggregate awareness without employing the HyperLogLog algorithm.

## Example

The `apx_unique_count` measure shown in this example is set for `allow_approximate_optimization: yes`, which means that the measure can be used in an [`aggregate_table`](https://docs.cloud.google.com/looker/docs/reference/param-explore-aggregate-table).
    
    
    measure: apx_unique_count {
      type: count_distinct
        allow_approximate_optimization: yes   # default value is no
      sql: ${id} ;;
    }
    

## Dialect support for distinct counts with aggregate awareness

Looker can use distinct counts for aggregate awareness with database dialects that support HyperLogLog sketches. In the latest release of Looker, the following SQL dialects are supported for distinct counts with aggregate awareness:

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
  
> Check your SQL dialect's documentation to understand the speed and accuracy tradeoffs of this method.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
