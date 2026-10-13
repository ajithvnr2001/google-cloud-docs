---
url: https://docs.cloud.google.com/looker/docs/best-practices/dry-cookbook-1/
title: Maximizing code reusability with DRY LookML: Define fields once, use substitution operators everywhere \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:01:49.246593+00:00
---

# Maximizing code reusability with DRY LookML: Define fields once, use substitution operators everywhere  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/dry-cookbook-1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Maximizing code reusability with DRY LookML: Define fields once, use substitution operators everywhere Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This page is part of the [Looker cookbook: Maximizing code reusability with DRY LookML](https://docs.cloud.google.com/looker/docs/best-practices/dry-lookml-cookbook).

LookML field definitions can change over time. For example, a database column name may change, or you may need to change the definition of a LookML field for other reasons.

If you use the syntax `{TABLE}.field_name` to reference a database column directly in multiple places, you must update each reference manually. Any fields that reference that dimension can break if you forget to update them, and Looker will display an error:

![Looker displays the error Unknown column order_items.sale_price in field list.](https://docs.cloud.google.com/static/looker/docs/images/dry-cookbook-substitution-operator-error-2304.png)

To make your LookML projects more efficient and easier to maintain, you can define fields in one place and use the substitution operator (`$`) to reference those fields everywhere else.

This page provides an example of using the substitution operator (with the syntax `${field_name}`) to reference a single dimension in the definitions of multiple LookML fields.

## Ingredients

  * [Substitution operators](https://docs.cloud.google.com/looker/docs/sql-and-referring-to-lookml#substitution_operator_)
  * The LookML [`dimension`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension) parameter
  * The LookML [`sql`](https://docs.cloud.google.com/looker/docs/reference/param-field-sql) parameter
  * The LookML [`sql_table_name`](https://docs.cloud.google.com/looker/docs/reference/param-view-sql-table-name) parameter



## Prerequisites

  * [A configured LookML model](https://docs.cloud.google.com/looker/docs/generating-a-model#when_you_need_to_configure_models)
  * [Permissions to develop LookML](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#permission_sets)



## Example: Referencing the underlying database column only once for a dimension

Define a database table column in a LookML project once using the syntax `${TABLE}.field_name` in the dimension's `sql` parameter. Then reference the dimension using the syntax `${field_name}` or `${view_name.field_name}` elsewhere in your project. This lets you maintain the LookML definition of the database column in one place (the original `${TABLE}.field_name` dimension), which is helpful if you need to reference it in multiple places in your project.

As an example, you can use the syntax `${TABLE}.sale_price` to define a base dimension called `sale_price` in a view called `order_items`:
    
    
      dimension: sale_price {
        type: number
        value_format_name: usd
        sql: ${TABLE}.sale_price ;;
        description: "The price at which an item is set to sell."
      }
    
    

When you define other fields that reference the `sale_price` dimension, can use the syntax `${sale_price}` within the `order_items` view (or use the syntax `${order_items.sale_price}` to reference the `sale_price` dimension in other views).

**Important:** If you want to reference a field that is from another view, you need to make sure that view is joined to the [Explore](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) where the field is being used.
    
    
    dimension: profit {
      type: number
      value_format_name: usd
      sql: ${sale_price} - ${inventory_items.cost} ;;
      description: "The difference between an item's sale price and an item's cost."
    }
    
    dimension: item_gross_margin {
      type: number
      value_format_name: percent_2
      sql: 1.0 * ${profit}/NULLIF(${sale_price},0) ;;
    }
    
    measure: total_sale_price {
      type: sum
      value_format_name: usd
      sql: ${sale_price} ;;
    }
    
    

In this example, if the column name for the dimension `sale_price` changes, you will only need to update the `${TABLE}.sale_price` reference once, in the definition of the base `sale_price` dimension. This change will then propagate automatically to the `profit`, `item_gross_margin`, and `total_sale_price` fields, as well as all other fields that reference the `sale_price` dimension.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
