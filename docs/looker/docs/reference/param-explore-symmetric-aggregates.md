---
url: https://docs.cloud.google.com/looker/docs/reference/param-explore-symmetric-aggregates/
title: symmetric_aggregates \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:24.925158+00:00
---

# symmetric_aggregates  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-explore-symmetric-aggregates/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  symmetric_aggregates Stay organized with collections  Save and categorize content based on your preferences. 

## Usage
    
    
    explore: explore_name {
      symmetric_aggregates: yes
    }
    

Hierarchy [Model File](https://docs.cloud.google.com/looker/docs/reference/param-model) [`explore`](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) `symmetric_aggregates` |  Default Value `yes` Accepts A Boolean (`yes` or `no`)   
---|---  
  
## Definition

The `symmetric_aggregates` parameter determines whether or not symmetric aggregates will be applied within a given Explore. When `symmetric_aggregates` is on, aggregate functions return correct results, even when joins result in a fanout. Symmetric aggregates are described in more detail on the [Understanding symmetric aggregates](https://docs.cloud.google.com/looker/docs/best-practices/understanding-symmetric-aggregates) Best Practices page, and the fanout problem they solve is explained in [The problem of SQL fanouts](https://discuss.google.dev/t/the-problem-of-sql-fanouts/119220) Community post.

By default, symmetric aggregates are turned on for every Explore within Looker. This means that if your SQL dialect supports symmetric aggregates, you need to include the `symmetric_aggregates` parameter only if you'd like to disable that functionality for an Explore.

## Examples

Turn on symmetric aggregates for the `product` Explore:
    
    
    explore: product {
      symmetric_aggregates: yes  # the default value, could be excluded
    }
    

Turn off symmetric aggregates for the `customer` Explore:
    
    
    explore: customer {
      symmetric_aggregates: no
    }
    

## Things to consider

### Create joins carefully when symmetric aggregates are off

Symmetric aggregates protect certain calculations from giving incorrect results when a join results in a fanout. Therefore, if your dialect doesn't support symmetric aggregates, or if you choose to turn them off, you will need to be careful when you execute joins in Looker. This problem and the workarounds for it are described in great detail in the Community post [The problem of SQL fanouts](https://discuss.google.dev/t/the-problem-of-sql-fanouts/119220).

### Not all database dialects support median and percentile measure types with symmetric aggregates

When symmetric aggregates are enabled, Looker automatically converts the [`percentile`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#percentile) and [`median`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#median) measure types to [`percentile_distinct`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#percentile_distinct) and [`median_distinct`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#median_distinct) when a join involves a fanout. Not all database dialects that support symmetric aggregates support the `percentile_distinct` and `median_distinct` measure types. You can see whether your database dialect supports these measure types on the [Measure types](https://docs.cloud.google.com/looker/docs/reference/param-measure-types) documentation page.

If you receive an error similar to `SQL dialect doesn't support Symmetric Aggregates with percentiles, field ignored.`, this indicates that your database dialect doesn't support the `percentile_distinct` and `median_distinct` measure types. To work around this, change the measure type to `type: number` and then specify the aggregate function with `sql: median(${dimension})`. This disables symmetric aggregates, however.

### Symmetric aggregates and `Value Overflow` errors

When attempting to download or view dashboards, you may encounter an error such as `A LookML model issue occurred. Non-unique value/primary key (or sql_distinct_key), value overflow or collision when computing sum.`

When aggregating a measure with large values, background calculations for symmetric aggregation might cause decimal overflow errors. Decimal overflow errors are caused when Looker attempts to perform symmetric aggregation (for example, `type: sum`) with left joins for very large values that exceed 14 digits (values that are greater than 10,000,000,000,000).

To resolve this issue, you can use the [`precision` parameter](https://docs.cloud.google.com/looker/docs/reference/param-field-precision) and set it to `5` or lower. For example:
    
    
    measure: average_value {
      type: average
      precision: 5
      sql: ${value} ;;
    }
    

## Dialect support for symmetric aggregates

The ability to use symmetric aggregates depends on the database dialect your Looker connection is using. In the latest release of Looker, the following dialects support aggregate awareness:

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
