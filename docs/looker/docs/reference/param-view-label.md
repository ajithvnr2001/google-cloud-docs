---
url: https://docs.cloud.google.com/looker/docs/reference/param-view-label/
title: label (for views) \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:29.019676+00:00
---

# label (for views)  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-view-label/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  label (for views) Stay organized with collections  Save and categorize content based on your preferences. 

> This page refers to the `label` parameter that is part of a [view](https://docs.cloud.google.com/looker/docs/reference/param-view).
> 
> `label` can also be used as part of a model, described on the [Model parameters](https://docs.cloud.google.com/looker/docs/reference/param-model) documentation page.
> 
> `label` can also be used as part of an Explore, described on the [`label` (for Explores)](https://docs.cloud.google.com/looker/docs/reference/param-explore-label) parameter documentation page.
> 
> `label` can also be used as part of a field, described on the[`label` (for fields)](https://docs.cloud.google.com/looker/docs/reference/param-field-label) parameter documentation page.
> 
> `label` can also be used as part of a reference line, described on the [Dashboard reference line parameters](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard-reference-line) documentation page.

## Usage
    
    
    view: view_name {
      label: "desired label for the view"
    }
    

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) `label` |  Default Value The view name Accepts A string  
---|---  
  
## Definition

The `label` parameter helps make Explores more user-friendly by allowing you to set the view names that appear in the [field picker](https://docs.cloud.google.com/looker/docs/changing-explore-menu-and-field-picker). If not specified, the label defaults to the name of the view.

## Example

In the field picker, make the view appear as **Product ID Info** for a view named `product_id_information`:
    
    
    view: product_id_information {
      label: "Product ID Info"
    }
    

## Things to consider

### A `label` does not change LookML references

The label affects only the displayed name of the view in the Explore; the label does not affect how you refer to the view in LookML. Views with labels are still referenced with the normal `${view_name.field_name}` syntax in your LookML files.

### A `label` can affect multiple Explores

Unlike [view_label (for Explores)](https://docs.cloud.google.com/looker/docs/reference/param-explore-view-label) and [view_label (for joins)](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-view-label), this parameter affects all Explores that use the view.

### A `label` isn't necessary if you name views thoughtfully

A view does not need a `label` parameter if the name already appears and is formatted how you want your users to see it in the field picker. If you know how you want a view to appear to your users, you can often consider this when naming it, avoiding the need to use `label`.

Typically `label` is only used when you want to perform one of the following tasks:

  * Change the way that a view name is formatted. For example, you can make the view name "abc_info" appear as "ABC Info" instead of "Abc Info"
  * Create two different views with different dimensions and measures that are based on the same SQL table



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
