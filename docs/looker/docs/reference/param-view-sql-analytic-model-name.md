---
url: https://docs.cloud.google.com/looker/docs/reference/param-view-sql-analytic-model-name/
title: sql_analytic_model_name (for views) \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:28.511688+00:00
---

# sql_analytic_model_name (for views)  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-view-sql-analytic-model-name/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  sql_analytic_model_name (for views) Stay organized with collections  Save and categorize content based on your preferences. 

**Preview:** This feature is subject to the "Pre-GA Offerings Terms" in the [General Service Terms](https://cloud.google.com/terms/service-terms#1) section of the Service Specific Terms. Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages). 

If you encounter an issue during the Public Preview of Looker interoperability with analytic models, report it to [database_analytic_models_feedback@google.com](mailto:database_analytic_models_feedback@google.com).

> This page refers to the `sql_analytic_model_name` parameter that is part of a [view](https://docs.cloud.google.com/looker/docs/reference/param-view-view).
> 
> `sql_analytic_model_name` can also be used as part of an Explore, described on the [`sql_analytic_model_name` (for Explores)](https://docs.cloud.google.com/looker/docs/reference/param-explore-sql-analytic-model-name) parameter documentation page.

## Usage
    
    
    view: view_name {
      sql_analytic_model_name: analytic_model_name ;;
    }
    

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) `sql_analytic_model_name` |  Default Value None Accepts An in-database analytic model name Special Rules

  * Analytic models are supported only for BigQuery and Snowflake connections.
  * The analytic model referenced by `sql_analytic_model_name` must be accessible within the database connection of its model.
  * If the analytic model is in a different database, schema, project, or dataset than the default path you defined in your database connection, you must scope the analytic model name.

  
---|---  
  
## Definition

For BigQuery and Snowflake connections, the `sql_analytic_model_name` parameter specifies the name of an existing [in-database analytic model](https://docs.cloud.google.com/looker/docs/analytic-models) (a [BigQuery Graph](https://docs.cloud.google.com/bigquery/docs/graph-overview) or a [semantic view in Snowflake](https://docs.snowflake.com/en/user-guide/views-semantic/overview)) to use as the basis for a LookML view. This lets you leverage analytic models defined directly in your database, such as [BigQuery Graph](https://docs.cloud.google.com/bigquery/docs/graph-overview) or [semantic views in Snowflake](https://docs.snowflake.com/en/user-guide/views-semantic/overview).

In this scenario, the analytic model object already exists in your database and is managed by your database; the analytic model isn't created, maintained, or governed by Looker. This is analogous to how regular database tables exposed as LookML views by using [`sql_table_name`](https://docs.cloud.google.com/looker/docs/reference/param-view-sql-table-name) aren't governed by Looker.

**Note:** If you instead want Looker to create a new analytic model and manage the analytic model, you can use the [`derived_analytic_model`](https://docs.cloud.google.com/looker/docs/reference/param-view-derived-analytic-model) parameter.

In the LookML view file, use the `sql_analytic_model_name` parameter to point Looker to the analytic model on your database. Then create Looker dimensions and measures to map to the analytic model so that you can use Looker to query the analytic model.

### Scoping analytic model names

When you reference an analytic model by using the analytic model name alone, Looker uses the default search path (the database and schema) that your Looker admin has configured in the settings for the database connection.

If you need to reference an analytic model in a different database and schema that isn't in the database user's default search path, you can scope the analytic model name by using the `<database_name>.<schema_name>.<analytic_model_name>` format to point to another database or schema:

  * To reference an analytic model from a different schema, use `<schema_name>.<analytic_model_name>`.
  * To reference an analytic model from a different database, use the full `<database_name>.<schema_name>.<analytic_model_name>`.



For a Google BigQuery connection, you can reference an analytic model in a different project and dataset by scoping the analytic model name using the format `<project_name>.<dataset_name>.<analytic_model_name>`. See the [Google BigQuery connection](https://docs.cloud.google.com/looker/docs/db-config-google-bigquery#billing_project_id) documentation page for additional information.

## Create LookML dimensions and measures based on your analytic view

After you create a view file and identify an analytic model as the `sql_analytic_model_name`, in the same view file you can then define LookML dimensions and measures that are based on the analytic model.

See your dialect's documentation for information about the proper SQL syntax to use for referring to elements in your analytic model. For example, to create a LookML dimension from a BigQuery Graph entity, you must use underscores to separate elements when scoping. For example, for BigQuery Graph, this LookML dimension is based on the `location_id` property in the `Stores` node table:
    
    
      dimension: location_id {
        type: number
        sql: Stores_location_id ;;
      }
    

However, to create a LookML dimension that's based on a Snowflake semantic view, you must use the unqualified name of a metric or dimension.

## Example

Here is an example BigQuery Graph named `StoreGraph` that is defined on a BigQuery database:
    
    
    CREATE OR REPLACE PROPERTY GRAPH mydataset.StoreGraph
      NODE TABLES (
        mydataset.Stores AS S,
        mydataset.Locations AS L
        PROPERTIES(id, name, population, MEASURE(SUM(population)) AS total_population)
      )
      EDGE TABLES (
        mydataset.Stores AS SL
        SOURCE KEY (location_id) REFERENCES L (id)
        DESTINATION KEY (name) REFERENCES S (name)
      );
    

And here is an example LookML view that's based on the `StoreGraph` BigQuery Graph, including dimensions and measures that are mapped to the Graph:
    
    
    view: MyStoreGraphView {
      sql_analytic_model_name: StoreGraph ;;
    
      dimension: location_id {
        type: number
        sql: Stores_location_id ;;
      }
    
      dimension: population {
        type: number
        sql: Locations_population ;;
      }
    
      dimension: location_name {
        type: string
        sql: Locations_name ;;
      }
    
      measure: locations_total_population {
        type: number
        sql: Locations_total_population ;;
      }
    }
    

## Things to consider

### Considerations for analytic models in Looker

When using in-database analytic models, keep the following considerations and limitations in mind:

  * **Data types:** Only the following data types for [dimensions](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types) and [measures](https://docs.cloud.google.com/looker/docs/reference/param-measure-types) are supported with analytic models: 

    * Supported for dimensions and measures: 
      * `string`
      * `number`
      * `date`
      * `yesno`
    * Supported for dimensions only: 
      * `time`
      * `date_time`
  * **Measures:**

    * **Base measures must be predefined:** Base measures must be predefined in the underlying database analytic model. Looker can't define a new base measure by performing an aggregation (such as [`type: sum`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#sum) or [`type: count`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#count)) on a dimension from an analytic model.
    * **Measures that are based on other measures are supported:** You can use the `sql` parameter of a LookML measure to perform non-aggregate computations that use predefined base measures from the analytic model. When you create a measure that's based on other measures, you can't define the new measure as an aggregate measure type such as `sum` or `count`. You must define the new measure as a non-aggregate measure type, such as [`string`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#string), [`number`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#number), [`date`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#date), or [`yesno`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#yesno). See the following example:
          
          measure: average_order_amount {
            type: number
            sql: ROUND(${total_order_amount} / NULLIF(${count_orders}, 0), 2) ;;
          }
          

  * **Joins:** An Explore whose base view is based on an analytic model can't include any joins. Similarly, a view that's based on an analytic model can't be joined into an Explore that has a standard LookML base view.

  * **Implicit joins:** Features that rely on implicit joins aren't supported for analytic models. Some examples of features that rely on implicit joins are [custom calendars](https://docs.cloud.google.com/looker/docs/custom-calendars) and fields that are defined with [`type: location`](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#location), [`type: distance`](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#distance), or [`type: zipcode`](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#zipcode). 

  * The following features are not supported with analytic models:

    * [Filtered measures](https://docs.cloud.google.com/looker/docs/reference/param-field-filters)
    * [Aggregate awareness](https://docs.cloud.google.com/looker/docs/aggregate_awareness)
    * [Looker legacy runtime](https://docs.cloud.google.com/looker/docs/legacy-feature-schedule#new_lookml_runtime)



### The analytic model must be accessible from the current connection

When the `sql_analytic_model_name` parameter is used within a [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) object, that `view` object can be referenced in an [`explore`](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) object, which is in turn referenced in a [model](https://docs.cloud.google.com/looker/docs/reference/param-model) object. The model object has a database [`connection`](https://docs.cloud.google.com/looker/docs/reference/param-model-connection) defined in it. When you reference an analytic model in the `sql_analytic_model_name` parameter, the analytic model needs to be accessible within the associated connection that's specified in the model file.

The default [database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#database) and [schema](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#schema) (or, for Google BigQuery, the [billing project](https://docs.cloud.google.com/looker/docs/db-config-google-bigquery#billing_project_id) and [dataset](https://docs.cloud.google.com/looker/docs/db-config-google-bigquery#dataset)) are defined by your Looker admin when they [create the Looker connection to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
