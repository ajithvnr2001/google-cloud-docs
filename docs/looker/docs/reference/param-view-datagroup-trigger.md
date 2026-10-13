---
url: https://docs.cloud.google.com/looker/docs/reference/param-view-datagroup-trigger/
title: datagroup_trigger \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:30.045365+00:00
---

# datagroup_trigger  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-view-datagroup-trigger/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  datagroup_trigger Stay organized with collections  Save and categorize content based on your preferences. 

## Usage
    
    
    view: my_view {
      derived_table: {
        datagroup_trigger: my_datagroup
        ...
      }
    }
    

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-explore-view-name) [`derived_table`](https://docs.cloud.google.com/looker/docs/reference/param-view-derived-table) `datagroup_trigger` |  Default Value None Accepts The name of a [datagroup](https://docs.cloud.google.com/looker/docs/reference/param-model-datagroup) defined in the model file   
---|---  
  
## Definition

`datagroup_trigger` lets you specify the datagroup to use as a caching policy for the derived table. The datagroup itself is defined in the model file using the [`datagroup`](https://docs.cloud.google.com/looker/docs/reference/param-model-datagroup) parameter.

Adding the `datagroup_trigger` parameter to a derived table makes the derived table a [persistent derived table (PDT)](https://docs.cloud.google.com/looker/docs/derived-tables#persistent_derived_table). The table is written into a scratch schema on your database and regenerated as specified by the `datagroup` parameter.

If you use `datagroup_trigger` for your PDT, you don't need to use the [`sql_trigger_value`](https://docs.cloud.google.com/looker/docs/reference/param-view-sql-trigger-value) or [`persist_for`](https://docs.cloud.google.com/looker/docs/reference/param-view-persist-for-for-derived-table) parameters. If you do, you will get a warning in the Looker IDE, and only the `datagroup_trigger` will be used.

## Examples

Create a persistent [native derived table](https://docs.cloud.google.com/looker/docs/creating-ndts) called `customer_orders` that is rebuilt when triggered by the datagroup named `order_datagroup`:
    
    
    view: customer_orders {
      derived_table: {
        explore_source: order {
          column: customer_id { field: order.customer_id }
          column: lifetime_orders { field: order.lifetime_orders }
        }
        datagroup_trigger: order_datagroup
      }
    }
    

Create a `customer_orders` persistent derived table based on a SQL query that is rebuilt when triggered by the datagroup called `etl_datagroup`:
    
    
    view: customer_orders {
      derived_table: {
        sql:
          SELECT
            customer_id,
            COUNT(*) AS lifetime_orders
          FROM
            order
          GROUP BY 1 ;;
        datagroup_trigger: etl_datagroup
      }
    }
    

## Common challenges

If you have PDTs that are dependent on other PDTs, be careful not to specify incompatible datagroup caching policies.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
