---
url: https://docs.cloud.google.com/looker/docs/reference/param-explore-always-filter/
title: always_filter \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:21.221899+00:00
---

# always_filter  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-explore-always-filter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  always_filter Stay organized with collections  Save and categorize content based on your preferences. 

## Usage
    
    
    explore: explore_name {
      always_filter:  {
        filters:  [field_name: "filter expression", field_name: "filter expression", ...]
      }
    }
    

Hierarchy [Model File](https://docs.cloud.google.com/looker/docs/reference/param-model) [`explore`](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) `always_filter` |  Default Value None Accepts A field name and a [Looker filter expression](https://docs.cloud.google.com/looker/docs/filter-expressions)  
---|---  
  
## Definition

The `always_filter` parameter lets you require users to include a set of filters for an Explore. After you define the filters and their default values by using the `always_filter` parameter, then the Explore automatically displays your configured filter settings. 

The filters that you specify in the `always_filter` parameter can't be removed from the Explore. However, your users can modify the filter by changing the filter's values or by changing the filter's condition from the condition drop-down menu. Your users can also remove all values from the filter, which has the same effect as removing the filter. 

If you want an Explore to have filters that can't be modified or removed, use one of the following parameters instead:

  * To configure filters that are the same for everyone and that can't be seen or changed in any way, you can use [`sql_always_where`](https://docs.cloud.google.com/looker/docs/reference/param-explore-sql-always-where).
  * To configure filters that are specific to each user and that can't be seen or changed in any way, you can use [`access_filter`](https://docs.cloud.google.com/looker/docs/reference/param-explore-access-filter).



In the `always_filter` parameter, the field that's referenced in the `filters` subparameter can be a [dimension](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types), [measure](https://docs.cloud.google.com/looker/docs/reference/param-measure-types), [filter](https://docs.cloud.google.com/looker/docs/reference/param-field-filter), or [parameter](https://docs.cloud.google.com/looker/docs/reference/param-field-parameter). If you need to reference a dimension or measure that is part of a joined view rather than part of this Explore, use `view_name.field_name`. For example:
    
    
    explore: order {
      always_filter: {
        filters: [id: "123", customer.id: "789"]
      }
      join: customer {
        sql_on: ${order.customer_id} = ${customer.id} ;;
      }
    }
    

Here the `id` filter refers to the `id` field from `order`. The `customer.id` filter refers to the `id` field from `customer`. This example also demonstrates that you can add multiple filters.

For each `field_name: "filter expression"` pair, the filter expression can be an absolute value or you can use [Looker filter expressions](https://docs.cloud.google.com/looker/docs/filter-expressions), depending on the type of field that you're filtering on.

## Examples

Configure a default filter for the Explore on the **Order ID** field (with a default value of "123"):
    
    
    explore: order {
      always_filter: {
        filters: [id: "123"]
      }
    }
    

Configure a default filter for the Explore on the **Order Created Date** field (with a default value of the previous seven days):
    
    
    explore: order {
      always_filter: {
        filters: [created_date: "7 days"]
      }
    }
    

Configure a default filter for the Explore on the **Order ID** field (default value of "123"), the **Order City** field (default value of "Chicago"), and the **Customer Age** field (default value of greater than or equal to 18):
    
    
    explore: order {
      always_filter: {
        filters: [id: "123", city: "Chicago", customer.age: ">=18"]
      }
      join: customer {
        sql_on: ${order.customer_id} = ${customer.id} ;;
      }
    }
    

## Things to consider

### Users can't remove a filter specified by `always_filter`

Although users may change the condition or the default value for their query, they can't remove a filter that has been added by `always_filter`. If you want to pre-load filters for an Explore in a way that lets users completely remove the filters, consider creating a query that includes suggested filters and then [sharing the query](https://docs.cloud.google.com/looker/docs/sharing-data) with users so they can use the query and its filters as a starting point.

### Setting a blank default value

If you want to create a default filter with a **blank** default value, you can do so by specifying `"-EMPTY"` in the filter values:
    
    
    always_filter: {
      filters: [products.category: "-EMPTY"]
    }
    

### The `always_filter` parameter overrides a `default_value` filter setting

The `always_filter` parameter overrides the [`default_value`](https://docs.cloud.google.com/looker/docs/reference/param-field-default-value) setting for the field. If you declare a value with `always_filter`, that value will be the default in the Explore. If you don't declare a value with `always_filter`, then "is any value" is the filter default in the Explore.

### `always_filter` affects existing Looks and dashboard tiles

Adding the `always_filter` parameter to an existing `explore` definition adds the set of filters with the default values to any Looks, Explores, or dashboard tiles that are based on that `explore`, including previously saved Looks and dashboard tiles that are based on the `explore`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
