---
url: https://docs.cloud.google.com/looker/docs/reference/param-explore-query/
title: query \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:22.622657+00:00
---

# query  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-explore-query/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  query Stay organized with collections  Save and categorize content based on your preferences. 

> This page refers to the `query` parameter that is part of an [Explore](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore).
> 
> `query` can also be used as part of an aggregate table, as described on the [`aggregate_table`](https://docs.cloud.google.com/looker/docs/reference/param-explore-aggregate-table) parameter documentation page.

## Usage
    
    
    explore: explore_name {
      query: query_name {
        dimensions: [dimension1, dimension2, ... ]
        measures: [measure1, measure2, ... ]
        label: "Display Name in Field Picker"
        description: "Information about this query"
        pivots: [dimension1, dimension2, ... ]
        sorts: [field1: asc, field2: desc, ... ]
        filters: [field1: "value1", field2: "value2", ... ]
        limit: 100
      }
      ...
    }
    
    

Hierarchy [Model File](https://docs.cloud.google.com/looker/docs/reference/param-model) [`explore`](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) `query` |  Default Value None Accepts The name of the query and subparameters to define the query  
---|---  
  
## Definition

You can use the `query` parameter to create modeled analyses for an Explore. The modeled analyses are listed in the [Quick Start](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#choosing_a_quick_start_option_from_a_blank_explore) section of a blank Explore, or in the Quick Start pop-up after an Explore has already been run. See the Example section on this page for how it works.

Modeled analyses are helpful to beginner Looker users, since you can specify elements like the dimensions, measures, filters, and pivots that may be the most relevant and insightful.

## Defining a query in LookML

> Instead of creating the query's LookML from scratch, you can use an Explore to create the query's base LookML for you. For details, see the next section, Getting query LookML from an Explore.

The `query` parameter has the following subparameters:

Parameter Name | Description | Example  
---|---|---  
`label` | Optionally, adds a label for the `query`. The label is what is displayed in the Explore's field picker for the query. | ` label: "Weekly Sales Totals"`  
`description` | Optionally, adds a description about this query to inform your users. In the Explore, any queries with a description will have an information icon. The description text is displayed when a user hovers over the information icon. | `description: "Total value of all sales per day" `  
`dimensions` | A comma-separated list of the dimensions from the Explore to be included in your query. The `dimensions` field uses this syntax: `dimensions: [dimension1, dimension2, ...]` | `dimensions:  [orders.created_month, orders.country]`  
`measures` | A comma-separated list of the measures from the Explore to be included in your query. The `measures` field uses this syntax: `measures: [measure1, measure2, ...]` | `measures:  [orders.count]`  
`filters` | Optionally, adds filters to a `query`. Filters are added to the `WHERE` clause of the SQL that generates the query. The `filters` field uses this syntax: `filters: [field_name_1: "value1", field_name_2: "value2", ...]` | `filters: [orders.country: "United States", orders.state: "California"] `  
`limit` | Optionally, specifies the row limit of the query. | `limit: 10`  
`sorts` | Optionally, specifies sort fields and sort direction (ascending or descending) for the `query`.  The `sorts` field uses this syntax: `sorts: [field1: asc|desc, field2: asc|desc, ...] ` | `sorts: [order_items.total_sales: asc]`  
`pivots` | Optionally, pivots the results on the specified dimensions of the query. The `pivots` field uses this syntax: `pivots: [dimension1, dimension2, ...]`**NOTE** : The fields specified in the `pivots` parameter must also be specified in the `dimensions` parameter of the query.  | ` pivots: [created_quarter]`  
`timezone` |  Not supported The `timezone` parameter is not supported for the `query` parameter that is a subparameter of [`explore`](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore). A `query` under `explore` uses the same time zone used by the `explore`. | ``  
  
## Getting query LookML from an Explore

As a shortcut, Looker developers can borrow the functionality used to generate [`aggregate_table`](https://docs.cloud.google.com/looker/docs/reference/param-explore-aggregate-table) LookML from an Explore, then copy the aggregate table query LookML and use it as a starting point for modeled analysis LookML.

> When you copy the LookML for an aggregate table, you'll also copy some parameters that you don't want for your modeled query LookML. Specifically, once you copy the aggregate table LookML you need to delete the `aggregate_table` and `materialization` parameters, since they apply only to aggregate tables. (See the [`aggregate_table`](https://docs.cloud.google.com/looker/docs/reference/param-explore-aggregate-table) parameter documentation page for more information about those parameters.)
> 
> Also, the aggregate table `query` parameter supports only a subset of the parameters that are supported by modeled Explore queries. This means that once you copy the aggregate table `query` LookML, you can use additional parameters for your modeled query. See the Defining a query in LookML section on this page for a full list of the parameters supported for modeled queries.

To use an Explore to get a base for your modeled query LookML:

  1. In your Explore, select all of the fields and filters to include in your modeled query.
  2. Select **Run** to get the results.
  3. Select **Get LookML** from the [Explore Actions gear menu](https://docs.cloud.google.com/looker/docs/viewing-and-interacting-with-explores#the_explore_actions_gear_menu). This option is available for Looker developers only.

  4. Select the **Aggregate Table** tab.

  5. Looker provides the LookML for an Explore [refinement](https://docs.cloud.google.com/looker/docs/lookml-refinements) for an aggregate table. We can use the aggregate table's `query` LookML and modify that for a modeled Explore query. Copy the LookML and paste it into the associated model file, which is indicated in the comment preceding the Explore refinement. If the Explore is defined in a [separate Explore file](https://docs.cloud.google.com/looker/docs/other-project-files#explore_files), and not in a model file, you can add the refinement to the Explore's file instead of the model file.

From here, you can modify the aggregate table LookML to use for a modeled query:

  6. Keep only the `query` parameter and its subparameters. Delete the [`aggregate_table`](https://docs.cloud.google.com/looker/docs/reference/param-explore-aggregate-table) and [`materialization`](https://docs.cloud.google.com/looker/docs/reference/param-explore-aggregate-table#materialization) parameters, since they apply only to aggregate tables.

  7. Add a name for the query. As shown in the Example section on this page, the syntax is:

`query: query_name`
  8. Optionally, fill in any additional parameters for your modeled query. See the Defining a query in LookML section on this page for a full list of parameters supported for modeled queries.




## Example

This example creates an `order_count_by_month` modeled query for the `order_items` Explore:
    
    
    explore: +order_items {
      query: order_count_by_month {
         description: "Number of orders placed by month in 2019"
         dimensions: [orders.created_month]
          measures: [orders.count]
         filters: [orders.created_date: "2019"]
        }
      }
    
    

Users can [run the Quick Start analysis](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#quick_start) from the **Quick Start** section of the **Order Items** Explore.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
