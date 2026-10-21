---
url: https://docs.cloud.google.com/looker/docs/best-practices/how-to-bucket-data-in-looker/
title: Bucketing in Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:11:34.897454+00:00
---

# Bucketing in Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/how-to-bucket-data-in-looker/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Bucketing in Looker Stay organized with collections  Save and categorize content based on your preferences. 

> _When you have[permission to create custom fields](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#create_custom_fields), you can create ad hoc [custom groups](https://docs.cloud.google.com/looker/docs/custom-fields#custom_grouping) for dimensions without using [logical functions](https://docs.cloud.google.com/looker/docs/functions-and-operators#logical_functions,_operators,_and_constants) in [Looker expressions](https://docs.cloud.google.com/looker/docs/creating-looker-expressions) or developing `CASE WHEN` logic in [`sql`](https://docs.cloud.google.com/looker/docs/reference/param-field-sql) parameters or [`type: case`](https://docs.cloud.google.com/looker/docs/reference/param-field-case) fields. _

> _You can also create ad hoc[custom bins](https://docs.cloud.google.com/looker/docs/custom-fields#custom_binning) for numeric type dimensions without needing to use [logical functions](https://docs.cloud.google.com/looker/docs/functions-and-operators#logical_functions,_operators,_and_constants) in [Looker expressions](https://docs.cloud.google.com/looker/docs/creating-looker-expressions) or needing to develop [`type: tier`](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#tier) LookML fields when you have [permission to create custom fields](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#create_custom_fields). _

Bucketing can be very useful for creating custom grouping dimensions in Looker. 

There are three ways to create buckets in Looker: 

  1. Using the [`tier`](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#tier) `dimension` type
  2. Using the [`case`](https://docs.cloud.google.com/looker/docs/reference/param-field-case) parameter
  3. Using a SQL `CASE WHEN` statement in the [`SQL`](https://docs.cloud.google.com/looker/docs/reference/param-field-sql) parameter of a LookML field



## Using `tier` for bucketing

To create integer buckets, we can simply define the `dimension` type as [`tier`](http://www.looker.com/docs/reference/field-reference/dimension-type-reference#tier): 
    
    
    dimension: users_lifetime_orders_tier {
      type: tier
      tiers: [0,1,2,5,10]
      sql: ${users_lifetime_orders} ;;
    }
    

You can use the [`style`](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#style) parameter to customize how your tiers appear when exploring. The four options for `style` are as follows: 

  1. [`classic`](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#classic)
  2. [`integer`](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#integer)
  3. [`interval`](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#interval)
  4. [`relational`](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#relational)



For example: 
    
    
    dimension: age_tier {
      type: tier
      tiers: [0,10,20,30,40,50,60,70,80]
      style: integer
      sql: ${age} ;;
    }
    

The `style` parameter `classic` is the default and takes the format `Tx[x,x]` with `Tx` indicating the tier number and `[x,x]` indicating the range. The following image is an Explore data table with **Users Count** grouped by **Users Age** : 

![The top available Users Age tier in the data table is T02\[10,20\] indicating a count of 808 users from ages 10 to 20.](https://docs.cloud.google.com/static/looker/docs/images/bucketing-in-looker-1-2210.png)

The next image shows examples of the other `style` parameter options: 

  * `interval` — With the format `[x,x]`, which indicates the lowest value and the highest value of a tier 
  * `integer` — With the format `x to x`, which indicates the lowest value and the highest value of a tier 
  * `relational` — With the format `>= x and <x`, which indicates that a value is greater than or equal to the lowest tier value and less than the highest tier value 



![](https://docs.cloud.google.com/static/looker/docs/images/bucketing-in-looker-2-2210.png)

###  Things to consider

Using `tier` in conjunction with [dimension fill](https://docs.cloud.google.com/looker/docs/creating-visualizations#filling_in_missing_dates_and_values) can result in unexpected tier buckets. 

For example, a `type: tier` dimension, **Age Tier** , will display tier buckets for **Below 0** and **0 to 9** when dimension fill is enabled, although the data does not include age values for those buckets: 

![](https://docs.cloud.google.com/static/looker/docs/images/bucketing-dimension-fill-on-2314.png)

When dimension fill is disabled for **Age Tier** , the buckets more accurately reflect the age values available in the data, beginning with the bucket **10 to 19** : 

![](https://docs.cloud.google.com/static/looker/docs/images/bucketing-dimension-fill-off-2318.png)

You can enable or disable dimension fill by hovering over the dimension name in the Explore, clicking the field-level [gear icon](https://docs.cloud.google.com/looker/docs/creating-visualizations#to_use_dimension_fill), and selecting either **Remove Filled in Tier Values** to disable, or **Fill in Missing Tier Values** to enable. 

Find out more about Looker [`tiers`](http://www.looker.com/docs/reference/lookml-reference/dimension-lookml-reference#tier) on the **Dimension, filter, and parameter types** documentation page. 

## Using `case` for bucketing

You can use the [`case`](http://www.looker.com/docs/reference/field-reference#case) parameter to create custom-named buckets with custom sorting. The `case` parameter is recommended for a fixed set of buckets, as it can help control the way values are presented, ordered, and used in UI filters and visualizations. For example, with `case`, a user will be able to select only the defined bucket values in a filter. 

To create buckets with `case`, you can define a dimension, like a bucket for order amounts: 
    
    
      dimension: order_amount_bucket {
        case: {
          when: {
            sql: ${order_amount} <= 50;;
            label: "Small"
          }
          when: {
            sql: ${order_amount} > 50 AND ${order_amount} <= 150;;
            label: "Medium"
          }
          when: {
            sql: ${order_amount} > 150;;
            label: "Large"
          }
          else:"Unknown"
        }
      }
    

The `case` parameter will typically sort values in the order in which the buckets are listed. For the `order_amount_bucket` dimension, the order of the buckets is **Small** , **Medium** , and **Large** : 

![](https://docs.cloud.google.com/static/looker/docs/images/bucketing-in-looker-3-2210.png)

If you would like to sort alphanumerically, add the [`alpha_sort`](https://docs.cloud.google.com/looker/docs/reference/param-field-case#choosing_the_sort_order_of_labels_with_alpha_sort) parameter to the dimension, like so: 
    
    
      dimension: order_amount_bucket {
        alpha_sort: yes
        case: {
          when: {
            sql: ${order_amount} <= 50;;
            label: "Small"
          }
          when: {
            sql: ${order_amount} > 50 AND ${order_amount} <= 150;;
            label: "Medium"
          }
          when: {
            sql: ${order_amount} > 150;;
            label: "Large"
          }
          else:"Unknown"
        }
      }
    

For dimensions where many distinct values are desired in the output (this would require you to define each output with a `WHEN` or an `ELSE` statement), or when you would like to implement a more complex `ELSE` statement, we recommend that you use a SQL `CASE WHEN`, discussed in the next section. 

Read more about the [`case`](https://docs.cloud.google.com/looker/docs/reference/param-field#sql_case) parameter on the **Field parameters** documentation page. 

## Using SQL `CASE WHEN` for bucketing

A SQL `CASE WHEN` statement is recommended for more complex bucketing, or for implementation of a more nuanced `ELSE` statement. 

For example, you may want to use different bucketing methods, depending on the destination of an order. A SQL `CASE WHEN` statement could be used to create a compound bucket dimension, where the `THEN` statement returns dimensions rather than strings: 
    
    
    dimension: compound_buckets {
      sql:
        CASE
          WHEN ${orders.destination} = 'US' THEN ${us_buckets}
          WHEN ${orders.destination} = 'CA' THEN ${canada_buckets}
        ELSE ${intl_buckets}
        END ;;
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
