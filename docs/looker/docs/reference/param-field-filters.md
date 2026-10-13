---
url: https://docs.cloud.google.com/looker/docs/reference/param-field-filters/
title: filters (for fields) \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:35.657217+00:00
---

# filters (for fields)  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-field-filters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  filters (for fields) Stay organized with collections  Save and categorize content based on your preferences. 

> This page refers to the `filters` parameter that is part of a [measure](https://docs.cloud.google.com/looker/docs/reference/param-field-measure).
> 
> `filters` can also be used as part of a native derived table, described on the [`explore_source`](https://docs.cloud.google.com/looker/docs/reference/param-view-explore-source) parameter documentation page.
> 
> `filters` can also be used as part of a dashboard, described on the [Dashboard parameters](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard#filters-for-dashboard) documentation page.
> 
> `filters` can also be used as part of a dashboard element. A representative example of its usage is provided on the documentation page for [column chart elements](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard-column-chart#filters).

## Usage
    
    
    view: view_name {
      measure: field_name {
        filters: [dimension_name: "filter expression", dimension_name: "filter expression", ... ]
      }
    }
    

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) [Field Type](https://docs.cloud.google.com/looker/docs/reference/param-field) `filters` |  Possible Field Types Measure Accepts A set of dimension names and corresponding Looker filter expressions  
---|---  
  
## Definition

`filters` is an optional list of filter expressions that are applied to a measure calculation. It works only with the following measure types that perform aggregation:

  * `type: count`
  * `type: count_distinct`
  * `type: sum`
  * `type: average`



The syntax for filters is:
    
    
    filters: [dimension_name_1: "Looker filter expression", dimension_name_2: "Looker filter expression", ...]
    

Refer to [Looker's filter notation](https://docs.cloud.google.com/looker/docs/filter-expressions) for details on how to write valid filter expressions. Place the entire filter expression in quotation marks, as shown in the following examples.

You can also use `filters` with [Liquid parameters](https://docs.cloud.google.com/looker/docs/templated-filters#making_a_dynamic_measure_with_a_liquid_parameter) and [templated filters](https://docs.cloud.google.com/looker/docs/templated-filters#templated_filters) to create dynamic filtered measures with a filter value that can change dynamically based on user input on a dashboard or Look. This approach allows users to select filter values that only apply to a specific measure, without filtering the entire query in a global `WHERE` clause. See the Creating a dynamic filtered measure section later on this page for reference.

## Examples

There are many ways to use `filters` for measures. The following examples outline some solutions for common use cases.

### Filtering on multiple fields

In this example, the measure will count distinct IDs that were created in the past seven days and were not from users with disabled accounts. This example also illustrates how to add multiple filters to a field. Each filter expression requires its own complete `filters` parameter:
    
    
    measure: this_week_count {
      type: count_distinct
      sql: ${TABLE}.id ;;
      filters: [created_date: "7 days", user.status: "-disabled"]
      # Reference fields from other joined views with view_name.field_name syntax
      # Minus sign means "not" in this case, but check notation docs for details
    }
    

### Filtering on a `yesno` dimension

As another example, consider data that includes one row per person, who is either a regular employee or a contractor. There is a field, `is_contractor`, of type [`yesno`](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#yesno), which contains `yes` if the person is a contractor. This measure will count only rows for contractors:
    
    
    measure: contractor_count {
      type: count
      filters: [is_contractor: "yes"]
    }
    

### Adding multiple filter values

In this next example, the `filters` expression contains multiple values. The measure will count all rows that match any of the four values in the `state` field:
    
    
    measure: customers_by_state {
      type: count
      filters: [state: "California, Nevada, Washington, Oregon"]
    }
    

### Filtering `NULL` values

In this example, the measure will count distinct IDs that were created in the past seven days and include a value in the `user.email_address` field that is not `NULL`:
    
    
    measure: this_week_count_with_email {
      type: count_distinct
      sql: ${TABLE}.id ;;
      filters: [created_date: "7 days", user.email_address: "-NULL"]
    }
    

Because the field `user.email_address` is of type `string`, the `"-NULL"` syntax is used. See the [Looker filter expressions](https://docs.cloud.google.com/looker/docs/filter-expressions) documentation page for more information.

### Adding numeric filter conditions

In this example, the filter is given a numeric value. The measure will add only orders that have a `price` of more than 100:
    
    
    measure: total_amt_large_orders {
      type: sum
      filters: [orders.price: ">100"]
      sql: ${orders.price} ;;
    }
    

### Using AND to combine conditions

In this example, the measure uses a [filter expression](https://docs.cloud.google.com/looker/docs/filter-expressions) with the `AND` operator in order to compute the total orders from customers in the 18-25 age group:
    
    
    measure: sales_18_to_25 {
      type: sum
      filters: [customers.age: ">=18 AND <=25"]
      sql: ${orders.price} ;;
    }
    

### Using commas to combine conditions

In this example, the measure uses a [filter expression](https://docs.cloud.google.com/looker/docs/filter-expressions) with the `,` operator in order to compute the total orders from customers who are younger than 25 or older than 65:
    
    
    measure: sales_less_25_or_greater_65 {
      type: sum
      filters: [customers.age: "<25, >65"]
      sql: ${orders.price} ;;
    }
    

### Creating a dynamic filtered measure

In this example, a filter gives a user the option to see a count of orders — filtered by the status the user chooses — on a Look or dashboard filter:

First, create a [filter-only field](https://docs.cloud.google.com/looker/docs/reference/param-field-filter) that allows the user to select a value:
    
    
      filter: status_filter {
        type: string
        suggest_dimension: status
      }
    

Next, create a [hidden dimension](https://docs.cloud.google.com/looker/docs/reference/param-field-hidden) that leverages templated filters to capture the user selection from the previous filter-only field. This dimension will return **yes** whenever a value is selected in the filter field:
    
    
      dimension: status_satisfies_filter {
        type: yesno
        hidden: yes
        sql: {% condition status_filter %} ${status} {% endcondition %} ;;
      }
    

Lastly, create a measure that filters on the `type: yesno` dimension:
    
    
      measure: count_dynamic_status {
        type: count
        filters: [status_satisfies_filter: "yes"]
      }
    

If a user chooses not to select a value for the filter-only field, the SQL will default to **1=1** , which will not affect the measure values.

## Common challenges

### Don't use `filters` with measures of `type: number`

Many users try to use `filters` with measures of `type: number`, which does not work:
    
    
    # Will NOT work
    measure: total_food_profit {
      type: number
      sql: ${total_revenue} - ${total_cost} ;;
      filters: [segment: "food"]
    }
    measure: total_revenue {
      type: sum
      sql: ${revenue} ;;
    }
    measure: total_cost {
      type: sum
      sql: ${cost} ;;
    }
    
    

Instead, apply a `filters` parameter to any of the individual measures that make up the measure of `type: number`, as follows:
    
    
    # Will work
    measure: total_food_profit {
      type: number
      sql: ${total_food_revenue} - ${total_food_cost} ;;
    }
    measure: total_food_revenue {
      type: sum
      sql: ${revenue} ;;
      filters: [segment: "food"]
    }
    measure: total_food_cost {
      type: sum
      sql: ${cost} ;;
      filters: [segment: "food"]
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
