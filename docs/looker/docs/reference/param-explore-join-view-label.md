---
url: https://docs.cloud.google.com/looker/docs/reference/param-explore-join-view-label/
title: view_label (for joins) \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:26.611149+00:00
---

# view_label (for joins)  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-explore-join-view-label/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  view_label (for joins) Stay organized with collections  Save and categorize content based on your preferences. 

> This page refers to the `view_label` parameter that is part of a [join](https://docs.cloud.google.com/looker/docs/reference/param-explore-join).
> 
> `view_label` can also be used as part of an [Explore](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore), described on the [`view_label` (for Explores)](https://docs.cloud.google.com/looker/docs/reference/param-explore-view-label) parameter documentation page.
> 
> `view_label` can also be used as part of a [dimension](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension), [measure](https://docs.cloud.google.com/looker/docs/reference/param-field-measure), or [filter](https://docs.cloud.google.com/looker/docs/reference/param-field-filter), described on the [`view_label` (for fields)](https://docs.cloud.google.com/looker/docs/reference/param-field-view-label) parameter documentation page.

## Usage
    
    
    explore: view_name {
      join: view_name_2 {
        view_label: "desired label"
      }
    }
    

Hierarchy [Model File](https://docs.cloud.google.com/looker/docs/reference/param-model) [`explore`](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) [`join`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join) `view_label` |  Default Value The name of the join Accepts A string  
---|---  
  
## Definition

`view_label` changes the way that a group of fields from a joined view are labeled in the field picker. You can use `view_label` to group a view's fields under the name of a different view.

![](https://docs.cloud.google.com/static/looker/docs/images/develop-funct-display-view_label-join-64.png)

You can use `view_label` when you need more than one view for modeling purposes, but those views represent the same entity to your business users. For example, consider an Explore called `order_items` with two joined views: `order_facts` and `orders`. You may want those views to retain separate names for modeling purposes. However, it might make things simpler for your users if they both appear as **Orders** in the UI.

If you do not explicitly add a `view_label` to a [`join`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join), the `view_label` defaults to the name of the join.

To change the names of the fields themselves, you can use the [`label`](https://docs.cloud.google.com/looker/docs/reference/param-field-label) parameter.

## Examples

Make the `customer_facts` view appear to be part of the **Customer** view in the field picker:
    
    
    explore: customer {
      join: customer_facts {
        view_label: "Customer"
        sql_on: ${customer.id} = ${customer_facts.customer_id} ;;
      }
    }
    

Make the `product_facts` view appear to be part of the **Product Info** view in the field picker:
    
    
    explore: product_info {
      join: product_facts {
        view_label: "Product Info"
        sql_on: ${product_info.product_id} = ${product_facts.product_id} ;;
      }
    }
    

## Common challenges

### `view_label` has no effect other than changing the field picker appearance

When you change the `view_label` of a [`join`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join), only the field picker is affected. The way that fields should be referenced in the LookML remains unchanged.

### Use proper capitalization when combining multiple views via `view_label`

If you want a joined view to be merged with another view in the field picker, make sure that the capitalization used in `view_label` is correct. The capitalization should match how the view name appears in the field picker. For example:
    
    
    explore: product_info {
      join: product_facts {
        view_label: "Product Info"
        sql_on: ${product_info.product_id} = ${product_facts.product_id} ;;
      }
    }
    

`product_info` will appear in the field picker as **Product Info** ; each word is capitalized, and underscores and changed to spaces. For this reason, we used `view_label: 'Product Info'` instead of `view_label: 'product_info'`.

## Things to know

### There are several ways to relabel a joined view

LookML has several ways to rename a joined view, all of which have different effects on the way that you write LookML. `view_label` is not appropriate for all use cases.

Situation | Proper LookML  
---|---  
Name a view differently than its underlying table, both in the field picker and when writing LookML | [`sql_table_name` for views](https://docs.cloud.google.com/looker/docs/reference/param-view-sql-table-name)  
Name a joined view differently than its underlying view, only in the field picker | `view_label` for joins  
Join the same view to an Explore multiple times, and apply a unique name to each case, both in the field picker and when writing LookML | [`from` for joins](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-from)  
If the same view can describe several different tables, choose the table to be used | [`sql_table_name` for joins](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-sql-table-name)  
  
### `view_label` affects the Explore's joined views

This parameter is similar to [`view_label` (for Explores)](https://docs.cloud.google.com/looker/docs/reference/param-explore-view-label) but affects the Explore's joined views instead of the base view. Unlike [`label` (for views)](https://docs.cloud.google.com/looker/docs/reference/param-view-label), this parameter only affects the view when displayed in that Explore.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
