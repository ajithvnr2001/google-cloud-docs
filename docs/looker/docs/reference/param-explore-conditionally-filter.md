---
url: https://docs.cloud.google.com/looker/docs/reference/param-explore-conditionally-filter/
title: conditionally_filter \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:20.892268+00:00
---

# conditionally_filter  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-explore-conditionally-filter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  conditionally_filter Stay organized with collections  Save and categorize content based on your preferences. 

## Usage
    
    
    explore: explore_name {
      conditionally_filter: {
        filters: [field_name: "filter expression", field_name: "filter expression", ...]
        unless: [field_name, field_name, ...]
      }
    }
    

Hierarchy [Model File](https://docs.cloud.google.com/looker/docs/reference/param-model) [`explore`](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) `conditionally_filter` |  Default Value None Accepts One or more filter specifications of a field name and a [Looker filter expression](https://docs.cloud.google.com/looker/docs/filter-expressions), plus a list of one or more field names in the `unless` section   
---|---  
  
## Definition

The `conditionally_filter` parameter lets you define a set of default filters that users can override _if_ they apply at least one filter from a second list that you define.

This parameter is typically used to prevent users from accidentally creating very large queries that may be too expensive to run on your database. For example, you might force a user to limit their query to the previous week, unless they've explicitly asked for a larger date range.

Filters applied in `conditionally_filter` appear to the user after they have run their query. While users can change the default `value` that you set, they cannot completely remove the filter unless they apply at least one of the filters you specify in the `unless` subparameter.

The field names you use can be the name of a [`dimension`](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types) or [`measure`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types).

To reference a dimension or measure that is part of a joined view rather than part of this Explore, use `view_name.field_name`.

## Examples

Consider the following example:
    
    
    explore: order {
      conditionally_filter: {
        filters: [id: "123", customer.id: "678,789"]
        unless: [date]
      }
    
      join: customer {
        sql_on: ${order.customer_id} = ${customer.id} ;;
      }
    }
    

In this case the `id` filter refers to the `id` field from the Explore called `order`. The `customer.id` filter refers to the `id` field from the view called `customer`. Both filters will be applied unless the user sets an order date in the Explore UI. This example also demonstrates that you can require multiple filters.

The default value that you specify can accept [these types of expressions](https://docs.cloud.google.com/looker/docs/filter-expressions).

You can also force the user to use an **Order ID** filter (with a default value of "123" that they can change) unless they apply an **Order Date** filter:
    
    
    explore: order {
      conditionally_filter: {
        filters: [id: "123"]
        unless: [date]
      }
    }
    

Alternatively, force the user to use an **Order ID** filter (with a default value of "123" or "234" that they can change) unless they apply an **Order Date** or **Order Time** filter:
    
    
    explore: order {
      conditionally_filter: {
        filters: [id: "123,234"]
        unless: [date, time]
      }
    }
    

Or, force the user to use an **Order ID** filter (default value of "123") and a **Customer City** filter (with default of "Chicago"), unless they apply an **Order Date** or **Customer Date** filter:
    
    
    explore: order {
      conditionally_filter: {
        filters: [id: "123", customer.city: "Chicago"]
        unless: [date, customer.date]
      }
    
      join: customer {
        sql_on: ${order.customer_id} = ${customer.id} ;;
      }
    }
    

## Common challenges

### A user cannot remove every filter when `conditionally_filter` is used

There is no way to run a query without _any_ filters when `conditionally_filter` is used. A user must use the conditional filters you specify, or their own filters from the `unless` list.

### `conditionally_filter` with a dimension of `type: time` in a group puts the group's other dimensions in the `unless` subparameter

If the `field` you specify within `conditionally_filter` is a time-based dimension that is part of a [dimension group](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group), then Looker will treat all of that group's other dimensions as if they were subject to an [`unless`](https://docs.cloud.google.com/looker/docs/reference/param-explore-conditionally-filter#definition) subparameter for that conditional filter — even if you don't include an `unless` subparameter.

The following two blocks of LookML are interpreted identically. Here, `conditionally_filter` is applied to a time-based dimension `event_date` that is part of the `event` dimension group. No `unless` conditions are specified, but Looker will treat the other dimensions in the `event` group as though they had been specified with the `unless` subparameter.

LookML block 1:
    
    
    explore: logs {
      # Make sure there is always a filter on event_date, event_week, event_month or event_year
      # Default to the last complete day of data
      conditionally_filter: {
        filters: [logs.event_date: "1 days ago for 1 day"]
      }
    
    view: logs {
      # Combine the partition date filters and the time filters into a single field group.
      dimension_group: event {
        type: time
        timeframes: [date,week,month,year]
        sql: _PARTITIONTIME ;;
      }
    }
    

LookML block 2:
    
    
    explore: logs {
      # Make sure there is always a filter on event_date, event_week, event_month or event_year
      # Default to the last complete day of data
      conditionally_filter: {
        filters: [logs.event_date: "1 days ago for 1 day"]
        unless: [event_week, event_month, event_year]
      }
    
    view: logs {
      # Combine the partition date filters and the time filters into a single field group.
      dimension_group: event {
        type: time
        timeframes: [date,week,month,year]
        sql: _PARTITIONTIME ;;
      }
    }
    

Looker interprets the two LookML blocks the same way, even though only the second LookML block explicitly applies the `unless` subparameter to the `event` group's other dimensions.

## Things to know

### There is a method to apply `conditionally_filter` to a subset of users

To apply a conditional filter for some users but not others, you can use [model permissions](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#model_sets). You need to create two models: one in which `conditionally_filter` is used, and one in which it is not. You can then grant access to the proper models on a user-specific basis.

### If you want to use `conditionally_filter` without `unless`, just use `always_filter` instead

To force users to use a specific set of filters no matter what, but let them change the default value, use [`always_filter`](https://docs.cloud.google.com/looker/docs/reference/param-explore-always-filter) instead.

### If you want filters that cannot be changed at all, consider `sql_always_where`

If you want an Explore to have filters that are the same for everyone, and _not_ let the users change the filter value, use [`sql_always_where`](https://docs.cloud.google.com/looker/docs/reference/param-explore-sql-always-where).

### If you want user-specific filters that cannot be changed, consider `access_filter`

If you want an Explore to have filters that are specific to each user, but cannot be removed or changed, use [`access_filter`](https://docs.cloud.google.com/looker/docs/reference/param-explore-access-filter).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-09-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-09-19 UTC."],[],[]] 
