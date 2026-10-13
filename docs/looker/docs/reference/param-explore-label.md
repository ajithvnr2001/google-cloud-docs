---
url: https://docs.cloud.google.com/looker/docs/reference/param-explore-label/
title: label (for Explores) \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:22.669797+00:00
---

# label (for Explores)  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-explore-label/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  label (for Explores) Stay organized with collections  Save and categorize content based on your preferences. 

> This page refers to the `label` parameter that is part of an [Explore](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore).
> 
> `label` can also be used as part of a model, described on the [`label` (for models)](https://docs.cloud.google.com/looker/docs/reference/param-model-label) parameter documentation page.
> 
> `label` can also be used as part of a view, described on the [`label` (for views)](https://docs.cloud.google.com/looker/docs/reference/param-view-label) parameter documentation page.
> 
> `label` can also be used as part of a field, described on the [`label` (for fields)](https://docs.cloud.google.com/looker/docs/reference/param-field-label) parameter documentation page.
> 
> `label` can also be used as part of a reference line, described on the [Dashboard reference line parameters](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard-reference-line) documentation page.

## Usage
    
    
    
    explore: explore_name {
      label: "desired label"
    }
    

Hierarchy [Model File](https://docs.cloud.google.com/looker/docs/reference/param-model) [`explore`](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) `label` |  Default Value The name of the `explore`, with each word capitalized and underscores replaced by spaces Accepts A string   
---|---  
  
## Definition

`label` helps make Explores more user-friendly by allowing you to set the Explore titles in the Explore menu and in the Explores themselves.

![](https://docs.cloud.google.com/static/looker/docs/images/dev-explore-params-label-2412.png)

If you do not explicitly add a `label` to an Explore definition, the label defaults to the name of the [`explore`](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore), but nicely formatted. Underscores are changed to spaces, and each word is capitalized.

## Examples

Make the Explore menu option appear as **Users** instead of **User** :
    
    
    explore: user {
      label: "Users"
    }
    

Make the Explore menu option appear as **Product ID Info** instead of **Product Id Information** :
    
    
    explore: product_id_information {
      label: "Product ID Info"
    }
    

## Common challenges

### `label` has no effect other than changing the Explore menu appearance

When you change the `label` of an Explore, only the Explore menu is affected.

The way that fields should be referenced in the LookML goes unchanged. The way that fields will appear within the Explore UI is also unchanged. If you prefer the LookML references and field names to change, use the [`from`](https://docs.cloud.google.com/looker/docs/reference/param-explore-from) parameter instead.

## Things to know

### Avoid `label` when possible by naming Explores properly

If you know that you always want an Explore to appear in a certain manner to your business users, consider giving that name to the `explore` in your LookML. Then you won't need to use `label`.

Typically `label` is only used when you want to:

  * Change the way that an Explore name is formatted. For example, you can make the Explore name "abc_info" appear as "ABC Info" instead of "Abc Info".
  * Create two different Explores that are based on the same view.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
