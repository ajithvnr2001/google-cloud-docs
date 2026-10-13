---
url: https://docs.cloud.google.com/looker/docs/reference/param-view-distribution-style/
title: distribution_style \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:30.451100+00:00
---

# distribution_style  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-view-distribution-style/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  distribution_style Stay organized with collections  Save and categorize content based on your preferences. 

## Usage
    
    
    view: my_view {
      derived_table: {
        distribution_style: all
        ...
      }
    }
    

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) [`derived_table`](https://docs.cloud.google.com/looker/docs/reference/param-view-derived-table) `distribution_style` \- or - [Model File](https://docs.cloud.google.com/looker/docs/reference/param-model) [`explore`](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) [`aggregate_table`](https://docs.cloud.google.com/looker/docs/reference/param-explore-aggregate-table) [`materialization`](https://docs.cloud.google.com/looker/docs/reference/param-explore-aggregate-table#materialization) `distribution_style` |  Default Value None Accepts A distribution style (`all` or `even`) Special Rules `distribution_style` is supported only on specific dialects  
---|---  
  
## Definition

`distribution_style` lets you specify how the query for a [persistent derived table](https://docs.cloud.google.com/looker/docs/derived-tables#persistent-derived-tables) (PDT) or an [aggregate table](https://docs.cloud.google.com/looker/docs/reference/param-explore-aggregate-table) is distributed across the nodes in a database.

> See the Dialect support for `distribution_style` section for the list of dialects that support `distribution_style`.

> The `distribution_style` parameter works only with tables that are [persistent](https://docs.cloud.google.com/looker/docs/derived-tables#adding_persistence), such as PDTs and aggregate tables. `distribution_style` is not supported for [derived tables](https://docs.cloud.google.com/looker/docs/creating-ndts) without a persistence strategy.

> In addition, the `distribution_style` parameter is not supported for derived tables that are defined using [`create_process`](https://docs.cloud.google.com/looker/docs/reference/param-view-create-process) or [`sql_create`](https://docs.cloud.google.com/looker/docs/reference/param-view-sql-create).
> 
> Lastly, `distribution_style` and [`distribution`](https://docs.cloud.google.com/looker/docs/reference/param-view-distribution) should not be used at the same time. If you want to distribute the rows of a table to different Redshift nodes based on a column value, use [`distribution`](https://docs.cloud.google.com/looker/docs/reference/param-view-distribution). Otherwise, use `distribution_style` to choose a different distribution strategy.

Redshift offers four distribution styles, which are described in the [Amazon Redshift documentation on distribution styles](http://docs.aws.amazon.com/redshift/latest/dg/c_choosing_dist_sort.html):

  * **ALL Distribution:** All rows are fully copied to each node. You can accomplish this type of distribution in Looker by using `distribution_style: all`.
  * **EVEN Distribution:** Rows are distributed to different nodes in a round-robin fashion. You can accomplish this type of distribution in Looker by using `distribution_style: even`.
  * **KEY Distribution:** Rows are distributed to different nodes based on unique values within a particular column. You can accomplish this type of distribution in Looker by using the [`distribution`](https://docs.cloud.google.com/looker/docs/reference/param-view-distribution) parameter.
  * **AUTO Distribution** Redshift assigns an optimal distribution style based on the size of the table data. Looker does not support this distribution type.



See the [Amazon Redshift documentation on distribution styles](http://docs.aws.amazon.com/redshift/latest/dg/c_choosing_dist_sort.html) for choosing the appropriate distribution strategy. If you don't specify a `distribution_style`, and don't use the [`distribution`](https://docs.cloud.google.com/looker/docs/reference/param-view-distribution) parameter instead, Looker will default to `all`.

## Examples

Create a `customer_order_facts` derived table with a distribution style of `all`:
    
    
    view: customer_order_facts {
      derived_table: {
        sql:
          SELECT
            customer_id,
            COUNT(*) AS lifetime_orders
          FROM
            order
          GROUP BY 1 ;;
        persist_for: "24 hours"
        distribution_style: all
      }
    }
    

## Dialect support for `distribution_style`

The ability to use `distribution_style` depends on the database dialect your Looker connection is using. In the latest release of Looker, the following dialects support `distribution_style`:

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
