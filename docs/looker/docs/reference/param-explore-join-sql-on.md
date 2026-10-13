---
url: https://docs.cloud.google.com/looker/docs/reference/param-explore-join-sql-on/
title: sql_on \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:25.836767+00:00
---

# sql_on  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-explore-join-sql-on/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  sql_on Stay organized with collections  Save and categorize content based on your preferences. 

## Usage
    
    
    explore: view_name_1 {
      join: view_name_2 {
        sql_on: ${view_name_1.id} = ${view_name_2.id} ;;
      }
    }
    

Hierarchy [Model File](https://docs.cloud.google.com/looker/docs/reference/param-model) [`explore`](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) [`join`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join) `sql_on` |  Default Value None Accepts A SQL `ON` clause Special Rules `sql_on`, [`sql_foreign_key`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-sql-foreign-key), and [`foreign_key`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-foreign-key) may not be used at the same time within the same [`join`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join)  
---|---  
  
## Definition

`sql_on` establishes a join relationship between a view and its Explore, based on a SQL `ON` clause that you provide.

For LookML, the order of conditions in `sql_on` doesn't matter. So `sql_on: ${order.user_id} = ${user.id} ;;` and `sql_on: ${user.id} = ${order.user_id} ;;` are equivalent. You can put the conditions in either order, unless the order is relevant to your database's SQL dialect.

A view can be joined directly to an Explore when using `sql_on`, or it can be joined through a second view that is already joined to that Explore.

An example of the first case, where a view is joined directly to the Explore, looks like this:
    
    
    explore: order {
      join: customer {
        sql_on: ${order.customer_id} = ${customer.id} ;;
      }
    }
    

The SQL that Looker would generate from this LookML is:
    
    
    SELECT    ...
    FROM      order
    LEFT JOIN customer
    ON        order.customer_id = customer.id
    

In the second case, a view is joined to an Explore through an intermediate view that is already joined to that Explore. An example of that would be:
    
    
    explore: order_items {
      join: order {
        sql_on: ${order_items.order_id} = ${order.id} ;;
      }
      join: customer {
        sql_on: ${order.customer_id} = ${customer.id} ;;
      }
    }
    

Here `customer` can't be joined directly to `order_items`. Instead it must be joined through `order`. The SQL that Looker would generate from this LookML is:
    
    
    SELECT    ...
    FROM      order_items
    LEFT JOIN order
    ON        order_items.order_id = order.id
    LEFT JOIN customer
    ON        order.customer_id = customer.id
    

To make this work properly, you can see that we just need to use the correct view names in our field references. Since `customer` needs to join to a field in `order`, we reference `${order.customer_id}`.

> In some older models, you might see fields referenced with the `view_name.native_column_name` syntax. While this still works, using the `${view_name.looker_dimension_name}` syntax instead has an important advantage: you can avoid the need for the [`required_joins`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-required-joins) parameter. This concept is explained in more detail in the Use `required_joins` when `${view_name.looker_dimension_name}` syntax can't be used section on this page.

### Conditional joins

It's also possible to allow user input to be used in `sql_on`. Although there are various reasons you may want to do this, optimizing query speed on MPP databases (such as Redshift) is a major use case, as described in the [Conditions in Join Clauses](https://discuss.google.dev/t/conditions-in-join-clauses-3-20/115996) Community post.

To add user input to your join condition, you'll first need to create a filter for their input. These types of filters are described in more detail on our [Templated Filters](https://docs.cloud.google.com/looker/docs/templated-filters) page. Their basic form is:
    
    
    view: view_name {
      filter: filter_name {
        type: number | datetime | date | string
      }
    }
    

Once you've added a filter to collect the user input, you use it in your `sql_on` parameter like this:
    
    
    {% condition view_name.filter_name %} view_name.dimension_name {% endcondition %}
    

For example:
    
    
    explore: order {
      join: customer {
        sql_on:
          ${order.customer_id} = ${customer.id} AND
          {% condition customer.creation_date_filter %} customer.created_at {% endcondition %} ;;
      }
    }
    

This would be interpreted to mean: set `customer.created_at` equal to the value from `customer.creation_date_filter`.

### Using `_in_query`, `_is_selected`, and `_is_filtered` Liquid variables

The `_in_query`, `_is_selected`, and `_is_filtered` [Liquid variables](https://docs.cloud.google.com/looker/docs/liquid-variable-reference#in-query-variables) can be useful when used with `sql_on` parameter. They can allow you to modify join relationships based on the fields that a user has selected for their query. For example:
    
    
    explore: dates {
      join: dynamic_order_counts {
        sql_on:
          ${dynamic_order_counts.period} =
          {% if dates.reporting_date._in_query %}
            ${dates.date_string}
          {% elsif dates.reporting_week._in_query %}
            ${dates.week_string}
          {% else %}
            ${dates.month_string}
          {% endif %} ;;
      }
    }
    

## Examples

Join the view named `customer` to the Explore named `order` by matching up the `customer_id` dimension from `order` with the `id` dimension from `customer`:
    
    
    explore: order {
      join: customer {
        sql_on: ${order.customer_id} = ${customer.id} ;;
      }
    }
    

Join the view named `customer` to the Explore named `order_items` through the view called `order`. Match up the `customer_id` dimension from `order` with the `id` dimension from `customer`. Match up the `order_id` dimension from `order_items` with the `id` dimension from `order`. This would be specified as follows:
    
    
    explore: order_items {
      join: order {
        sql_on: ${order_items.order_id} = ${order.id} ;;
      }
      join: customer {
        sql_on: ${order.customer_id} = ${customer.id} ;;
      }
    }
    

Join the views named `order` and `inventory_items` to the Explore named `order_items`. Match up the `inventory_id` dimension from `order_items` with the `id` dimension from `inventory_item`. Match up the `order_id` dimension from `order_items` with the `id` dimension from `order`. This would be specified as follows:
    
    
    explore: order_items {
      join: order {
        sql_on: ${order_items.order_id} = ${order.id} ;;
      }
      join: inventory_item {
        sql_on: ${order_items.inventory_id} = ${inventory_item.id} ;;
      }
    }
    

## Things to know

### Use `required_joins` when `${view_name.looker_dimension_name}` syntax can't be used

When you reference fields in `sql_on` using the `${view_name.looker_dimension_name}` syntax, you do not need to worry about using [`required_joins`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-required-joins).

However, some older models still use the `view_name.native_column_name` syntax. There are also some cases when you cannot use the `${view_name.looker_dimension_name}` syntax, such as when you want to apply custom SQL.

In these situations, you may need to use `required_joins`. They are discussed in more detail on the [`required_joins`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-required-joins) parameter documentation page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
