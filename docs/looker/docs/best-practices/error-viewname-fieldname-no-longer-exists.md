---
url: https://docs.cloud.google.com/looker/docs/best-practices/error-viewname-fieldname-no-longer-exists/
title: Error: view_name.field_name no longer exists on explore_name and will be ignored \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:11:42.772807+00:00
---

# Error: view_name.field_name no longer exists on explore_name and will be ignored  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/error-viewname-fieldname-no-longer-exists/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Error: view_name.field_name no longer exists on explore_name and will be ignored Stay organized with collections  Save and categorize content based on your preferences. 

After you run an [Explore](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores) or a [Look](https://docs.cloud.google.com/looker/docs/viewing-looks), you might occasionally see the following warning: 

`⚠️ view_name.field_name no longer exists on explore_name and will be ignored.`

![](https://docs.cloud.google.com/static/looker/docs/images/hc-view-name-field-name-no-longer-exists-error-2110.png)

This warning indicates that fields that you had previously selected or saved in an Explore or a Look are now no longer available. There are several potential causes for this occurrence:

  * The field or fields that are referenced in the warning exist only in [Development Mode](https://docs.cloud.google.com/looker/docs/dev-mode-prod-mode#development_mode), and you're viewing the Explore or Look in [Production Mode](https://docs.cloud.google.com/looker/docs/dev-mode-prod-mode#production_mode) (or vice versa). 

  * A [join](https://docs.cloud.google.com/looker/docs/reference/param-explore-join) was removed from the [`explore` file's LookML definition](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore), which removed the field that is referenced in the warning. 

For example, if you see the warning `users.name no longer exists on Companies, and will be ignored`, this may indicate that the `users` view and its fields are no longer joined to the `companies` Explore and are therefore unavailable in the Look or Explore. 

> You can use the [metadata panel in the IDE](https://docs.cloud.google.com/looker/docs/lookml-metadata#metadata_for_views) to see all `explore` definitions that reference a specific view.

  * A change was made to the view's name in its [file](https://docs.cloud.google.com/looker/docs/model-and-view-files#view_files), or the view reference in the `explore` LookML definition was changed with a parameter such as [`view_name`](https://docs.cloud.google.com/looker/docs/reference/param-explore-view-name). 

For example, an underlying view for an Explore called `users` was updated with a `view_name` parameter that references a view called `customers`: 
        
        explore: users {
                    view_name: customers
                }
            




## Resolving the warning if fields that are referenced in the warning were deleted intentionally 

If a field that is referenced in a warning was _intentionally_ removed by a LookML developer, follow these steps to resolve the warning for either a Look or an Explore. 

### Resolving the warning for a Look

To resolve the `view_name.field_name no longer exists on explore_name and will be ignored` warning for a Look:

  1. Select the **Edit** button in the top right corner to [edit the Look.](https://docs.cloud.google.com/looker/docs/saving-and-editing-looks#editing_looks)
  2. Once in edit mode, select the **x** next to each error message to clear the warning.
  3. Make a change, such as [adding](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#adding_more_dimensions_for_more_detail) any field from the field picker and then [removing](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#removing_fields) it, to activate the **Save** button. 
  4. Select **Save**.



This will update and save the Look to omit the deleted field or fields and the accompanying errors. 

### Resolving the warning for an Explore

To resolve the `view_name.field_name no longer exists on explore_name and will be ignored` warning for an Explore:

  1. Make a change, such as [adding](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#adding_more_dimensions_for_more_detail) any field from the field picker and then [removing](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#removing_fields) it.
  2. Select **Run** to rerun the Explore query.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
