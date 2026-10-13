---
url: https://docs.cloud.google.com/looker/docs/reference/param-explore-view-label/
title: view_label (for Explores) \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:24.192722+00:00
---

# view_label (for Explores)  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-explore-view-label/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  view_label (for Explores) Stay organized with collections  Save and categorize content based on your preferences. 

> This page refers to the `view_label` parameter that is part of an [Explore](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore).
> 
> `view_label` can also be used as part of a [join](https://docs.cloud.google.com/looker/docs/reference/param-explore-join), described on the [`view_label` (for joins)](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-view-label) parameter documentation page.
> 
> `view_label` can also be used as part of a [dimension](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension), [measure](https://docs.cloud.google.com/looker/docs/reference/param-field-measure), or [filter](https://docs.cloud.google.com/looker/docs/reference/param-field-filter), described on the [`view_label` (for fields)](https://docs.cloud.google.com/looker/docs/reference/param-field-view-label) parameter documentation page.

## Usage
    
    
    explore: explore_name {
      view_label: "desired label for the view"
    }
    

Hierarchy [Model File](https://docs.cloud.google.com/looker/docs/reference/param-model) [`explore`](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) `view_label` |  Default Value The name of the Explore Accepts A string  
---|---  
  
## Definition

`view_label` changes the way that the group of fields from an Explore's base view will be labeled in the field picker.

![](https://docs.cloud.google.com/static/looker/docs/images/dev-explore-view_label-2516.png)

Sometimes `view_label` is used to add an underscore in front of the view name so that it sorts alphabetically to be the top view in the field picker. Alternatively, you can use it when you need more than one view for modeling purposes, but the views represent the same entity as far as business users are concerned. For example, you might have one view defined in your LookML as `customer` and another as `customer_facts`, and want them to retain those names for modeling purposes. However, it might make sense for both of them to appear as **Customer** to business users.

If you want to change the names of the fields themselves, you can use the [`label`](https://docs.cloud.google.com/looker/docs/reference/param-field-label) parameter.

## Examples

Make the `customer_facts` Explore appear to business users to be part of the **Customers** view:
    
    
    explore: customer_facts {
      view_label: "Customers"
    }
    

Make the `product_facts` Explore appear to users to be part of the **Product Info** view:
    
    
    explore: product_facts {
      view_label: "Product Info"
    }
    

## Things to consider

### `view_label` has no effect other than changing the field picker appearance

When you change the `view_label` of an [Explore](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore), only the field picker is affected. The way that the Explore appears in the **Explore** menu, and the way that fields should be referenced in the LookML, are both unchanged.

### Use proper capitalization when combining multiple views with `view_label`

If you want the fields from the Explore's base view to be merged with one of the Explore's joined views in the field picker, you'll need to make sure that the capitalization you use in `view_label` is correct. The capitalization you use should match how the view name appears in the field picker. Take this example:
    
    
    explore: product {
      view_label: "Product Info"
      join: product_info {
        sql_on: ${product.product_id} = ${product_info.product_id} ;;
      }
    }
    

The way that `product_info` will appear in the field picker is **Product Info** ; each word is capitalized, and underscores are changed to spaces. For this reason, we used `view_label: 'Product Info'` instead of `view_label: 'product_info'`.

### A field's `view_label` takes precedence over an Explore's `view_label`

If a field in an Explore has a `view_label`, the field will appear under its `view_label`, not the Explore's `view_label`. Consider this example, where both an Explore and a dimension have `view_label` values. 

In the model file, the Explore is defined with `view_label: "View Label on Explore"`:
    
    
    explore: us_births {
      label: "US births"
      view_label: "View Label on Explore"
    }
    
    

In the `us_births.view` file, the `state` dimension is defined with `view_label: "View Label on Field"`:
    
    
    view: us_births {
      label: "US births"
    
      dimension: state {
        view_label: "View Label on Field"
        type: string
        sql: ${TABLE}.state ;;
      }
    

In this case, the `state` dimension's `view_label` will override the Explore's `view_label`, so in the Explore the `state` dimension will appear under the "View Label on Field" `view_label`.

![](https://docs.cloud.google.com/static/looker/docs/images/dev-explore-vs-field-view_label-2516.png)

### `view_label` affects the Explore's base view

This parameter is similar to [`view_label` (for joins)](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-view-label) but affects the Explore's base view instead of the joined views. Unlike [`label` (for views)](https://docs.cloud.google.com/looker/docs/reference/param-view-label), this parameter only affects the base view in that Explore.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-09-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-09-16 UTC."],[],[]] 
