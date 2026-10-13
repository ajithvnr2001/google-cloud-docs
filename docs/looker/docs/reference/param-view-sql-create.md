---
url: https://docs.cloud.google.com/looker/docs/reference/param-view-sql-create/
title: sql_create \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:32.555597+00:00
---

# sql_create  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-view-sql-create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  sql_create Stay organized with collections  Save and categorize content based on your preferences. 

## Usage
    
    
    derived_table: customer_order_facts {
      sql_create: {
          SQL statement ;;
      }
    }
    

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) [`derived_table`](https://docs.cloud.google.com/looker/docs/reference/param-view-derived-table) `sql_create` |  Default Value None Accepts A SQL statement   
---|---  
  
## Definition

`sql_create` enables custom Data Definition Language (DDL) commands for building [persistent derived tables (PDTs)](https://docs.cloud.google.com/looker/docs/derived-tables#persistent_derived_tables_\(pdts\)). `sql_create` will issue a statement as is, without Looker's usual error checking. The only requirement is that the statement results in the creation and execution of a PDT. This lets you, for example, create PDTs that support the Google [BigQuery ML](https://docs.cloud.google.com/bigquery/docs/bigqueryml) machine learning models.

For PDTs that are defined with `sql_create`, you cannot use any of the following parameters: 

  * [`indexes`](https://docs.cloud.google.com/looker/docs/reference/param-view-indexes)
  * [`cluster_keys`](https://docs.cloud.google.com/looker/docs/reference/param-view-cluster-keys)
  * [`distribution`](https://docs.cloud.google.com/looker/docs/reference/param-view-distribution)
  * [`distribution_style`](https://docs.cloud.google.com/looker/docs/reference/param-view-distribution-style)
  * [`partition_keys`](https://docs.cloud.google.com/looker/docs/reference/param-view-partition-keys)
  * [`sortkeys`](https://docs.cloud.google.com/looker/docs/reference/param-view-sortkeys)



## Examples

Create a PDT for BigQuery ML queries that predict likelihood of future purchases:
    
    
    view: future_purchase_model {
      derived_table: {
        datagroup_trigger: bqml_datagroup
        sql_create:
          CREATE OR REPLACE MODEL ${SQL_TABLE_NAME}
          OPTIONS(model_type='logistic_reg'
            , labels=['will_purchase_in_future']
            , min_rel_progress = 0.005
            , max_iterations = 40
            ) AS
          SELECT
             * EXCEPT(fullVisitorId, visitId)
          FROM ${training_input.SQL_TABLE_NAME};;
      }
    }
    

## Things to consider

### `${SQL_TABLE_NAME}` substitution operator

You can use the `${SQL_TABLE_NAME}` substitution operator to substitute in the computed name of the PDT being created. This ensures the SQL statement will correctly include the PDT name given in the LookML `view` parameter.

> `sql_create` must create a table with the name indicated by the `${SQL_TABLE_NAME}` substitution operator, or it will be rebuilt from scratch on every trigger check interval specified in a connection's [**PDT and Datagroup Maintenance Schedule**](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#pdt_and_datagroup_maintenance_schedule) setting (the default is five minutes). This can cause unexpected query traffic on your database or data warehouse.

### Use `create_process` to create a PDT in multiple steps

If your database dialect requires custom DDL commands, and you want to issue multiple commands to create a PDT, you can use [`create_process`](https://docs.cloud.google.com/looker/docs/reference/param-view-create-process) to issue multiple custom DDL commands in a specific order.

### Tables defined with `sql_create` can't be used for incremental PDTs

To be used as an [incremental PDT](https://docs.cloud.google.com/looker/docs/incremental-pdts), a SQL-based PDT must have a query defined using the [`sql`](https://docs.cloud.google.com/looker/docs/reference/param-view-sql-for-derived-table) parameter. SQL-based PDTs that are defined with the `sql_create` parameter or the [`create_process`](https://docs.cloud.google.com/looker/docs/reference/param-view-create-process) parameter cannot be incrementally built.

This is because Looker uses an [INSERT or a MERGE command to create the increments](https://docs.cloud.google.com/looker/docs/incremental-pdts#example_1) for an incremental PDT. The derived table cannot be defined using custom Data Definition Language (DDL) statements, since Looker wouldn't be able to determine which DDL statements would be required to create an accurate increment.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
