---
url: https://docs.cloud.google.com/looker/docs/reference/param-view-distribution/
title: distribution \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:30.241601+00:00
---

# distribution  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-view-distribution/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  distribution Stay organized with collections  Save and categorize content based on your preferences. 

## Usage
    
    
    view: my_view {
      derived_table: {
        distribution: "customer_id"
        ...
      }
    }
    

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) [`derived_table`](https://docs.cloud.google.com/looker/docs/reference/param-view-derived-table) `distribution` \- or - [Model File](https://docs.cloud.google.com/looker/docs/reference/param-model) [`explore`](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) [`aggregate_table`](https://docs.cloud.google.com/looker/docs/reference/param-explore-aggregate-table) [`materialization`](https://docs.cloud.google.com/looker/docs/reference/param-explore-aggregate-table#materialization) `distribution` |  Default Value None Accepts The name of a column in a derived table or aggregate table Special Rules `distribution` is supported only for Redshift and Aster databases.   
---|---  
  
## Definition

The `distribution` parameter lets you specify the column from a [persistent derived table](https://docs.cloud.google.com/looker/docs/derived-tables#persistent-derived-tables) (PDT) or an [aggregate table](https://docs.cloud.google.com/looker/docs/reference/param-explore-aggregate-table) on which to apply a distribution key. The distribution key spreads the data around a cluster. When two tables are joined by the column specified in the `distribution` parameter, the database can find the joined data on the same node to minimize internode I/O. The `distribution` parameter works only with Redshift and Aster databases. For other SQL dialects (such as MySQL and Postgres), use [`indexes`](https://docs.cloud.google.com/looker/docs/reference/param-view-indexes) instead.

> The `distribution` parameter works only with tables that are [persistent](https://docs.cloud.google.com/looker/docs/derived-tables#adding_persistence), such as PDTs and aggregate tables. `distribution` is not supported for [derived tables](https://docs.cloud.google.com/looker/docs/creating-ndts) without a persistence strategy.
> 
> In addition, the `distribution` parameter is not supported for derived tables that are defined using [`create_process`](https://docs.cloud.google.com/looker/docs/reference/param-view-create-process) or [`sql_create`](https://docs.cloud.google.com/looker/docs/reference/param-view-sql-create).

Generally speaking, a distribution key should be applied to the column that will be acting as a foreign key (the column you use to join your table to others). Refer to the documentation for your dialect for best practices.

## Examples

Create a `customer_order_facts` persistent derived table with a distribution key on `customer_id`:
    
    
    view: customer_order_facts {
      derived_table: {
        explore_source: order {
          column: customer_id { field: order.customer_id }
          column: lifetime_orders { field: order.lifetime_orders }
        }
        datagroup_trigger: order_datagroup
        distribution: "customer_id"
      }
    }
    

Create a `customer_order_facts` derived table based on a SQL query with a distribution key on `customer_id`:
    
    
    view: customer_order_facts {
      derived_table: {
        sql:
          SELECT
            customer_id,
            COUNT(*) AS lifetime_orders
          FROM
            order ;;
        persist_for: "24 hours"
        distribution: "customer_id"
      }
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-12 UTC."],[],[]] 
