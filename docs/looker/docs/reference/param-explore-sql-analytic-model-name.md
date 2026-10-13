---
url: https://docs.cloud.google.com/looker/docs/reference/param-explore-sql-analytic-model-name/
title: sql_analytic_model_name (for Explores) \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:23.648540+00:00
---

# sql_analytic_model_name (for Explores)  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-explore-sql-analytic-model-name/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  sql_analytic_model_name (for Explores) Stay organized with collections  Save and categorize content based on your preferences. 

**Preview:** This feature is subject to the "Pre-GA Offerings Terms" in the [General Service Terms](https://cloud.google.com/terms/service-terms#1) section of the Service Specific Terms. Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages). 

If you encounter an issue during the Public Preview of Looker interoperability with analytic models, report it to [database_analytic_models_feedback@google.com](mailto:database_analytic_models_feedback@google.com).

> This page refers to the `sql_analytic_model_name` parameter that is part of an [Explore](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore).
> 
> `sql_analytic_model_name` can also be used as part of a view, described on the [`sql_analytic_model_name` (for views)](https://docs.cloud.google.com/looker/docs/reference/param-view-sql-analytic-model-name) parameter documentation page.

## Usage
    
    
    explore: explore_name {
      sql_analytic_model_name: analytic_model_name ;;
    }
    

Hierarchy [Model File](https://docs.cloud.google.com/looker/docs/reference/param-model) [`explore`](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) `sql_analytic_model_name` |  Default Value None Accepts An in-database analytic model name Special Rules

  * Analytic models are supported only for BigQuery and Snowflake connections.
  * `sql_analytic_model_name` for Explores should be used only when the same view can describe multiple analytic models on your database. 
  * The analytic model referenced by `sql_analytic_model_name` must be accessible within the database connection of its model.
  * If the analytic model is in a different database, schema, project, or dataset than the default path you defined in your database connection, you must scope the analytic model name.

  
---|---  
  
## Definition

For BigQuery and Snowflake connections, the `sql_analytic_model_name` parameter specifies the name of an existing [in-database analytic model](https://docs.cloud.google.com/looker/docs/analytic-models) (a [BigQuery Graph](https://docs.cloud.google.com/bigquery/docs/graph-overview) or a [semantic view in Snowflake](https://docs.snowflake.com/en/user-guide/views-semantic/overview)) to use as the basis for a LookML Explore. 

In most cases, you use the [`sql_analytic_model_name` (for views)](https://docs.cloud.google.com/looker/docs/reference/param-view-sql-analytic-model-name) parameter to specify an analytic model in your view file. Then, in that view file, you define LookML dimensions and measures that are based on the analytic model in your database. However, in cases where your database has multiple analytic models that can be defined by the same LookML fields, you can use the `sql_analytic_model_name` parameter under an `explore` parameter. 

When you specify a `sql_analytic_model_name` under an `explore` parameter, the Explore will override the analytic model specified in the view file and instead query the analytic model that you specified in the `sql_analytic_model_name` under the `explore` parameter. In this case, the Explore will use the LookML measures and dimensions that are defined in the view file, but apply them to the analytic model that's specified in the `sql_analytic_model_name` parameter of the `explore` parameter.

### Scoping analytic model names

When you reference an analytic model by using the analytic model name alone, Looker uses the default search path (the database and schema) that your Looker admin has configured in the settings for the database connection.

If you need to reference an analytic model in a different database and schema that isn't in the database user's default search path, you can scope the analytic model name by using the `<database_name>.<schema_name>.<analytic_model_name>` format to point to another database or schema:

  * To reference an analytic model from a different schema, use `<schema_name>.<analytic_model_name>`.
  * To reference an analytic model from a different database, use the full `<database_name>.<schema_name>.<analytic_model_name>`.



For a Google BigQuery connection, you can reference an analytic model in a different project and dataset by scoping the analytic model name using the format `<project_name>.<dataset_name>.<analytic_model_name>`. See the [Google BigQuery connection](https://docs.cloud.google.com/looker/docs/db-config-google-bigquery#billing_project_id) documentation page for additional information.

## Example

Here is an example LookML view called `MyStoreGraphView` that's based on a `StoreGraph` BigQuery Graph on a BigQuery database, including dimensions and measures that are mapped to the Graph:
    
    
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
    

Assuming that the database has another Graph called `ShopDetailsGraph` with the same elements as the `StoreGraph`, here is an Explore that overrides the `sql_analytic_model_name` value in the `MyStoreGraphView` view file. The Explore will have the same LookML dimensions and measures that are defined in the `MyStoreGraphView`, but the Explore will query the `ShopDetailsGraph` analytic model:
    
    
    explore: MyStoreGraphView {
      sql_analytic_model_name: ShopDetailsGraph ;;
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

When the `sql_analytic_model_name` parameter is used within an [`explore`](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) object, that `explore` object is in turn included in a [model](https://docs.cloud.google.com/looker/docs/reference/param-model) object. (The Hierarchy on this page shows this relationship chain.) The model object has a database [`connection`](https://docs.cloud.google.com/looker/docs/reference/param-model-connection) defined in it. When you reference an analytic model in the `sql_analytic_model_name` parameter, the analytic model needs to be accessible within the associated connection specified in the model file.

The default [database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#database) and [schema](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#schema) (or, for Google BigQuery, the [billing project](https://docs.cloud.google.com/looker/docs/db-config-google-bigquery#billing_project_id) and [dataset](https://docs.cloud.google.com/looker/docs/db-config-google-bigquery#dataset)) are defined by your Looker admin when they [create the Looker connection to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
