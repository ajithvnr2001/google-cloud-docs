---
url: https://docs.cloud.google.com/looker/docs/reference/param-view-extends/
title: extends (for views) \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:27.901386+00:00
---

# extends (for views)  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-view-extends/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  extends (for views) Stay organized with collections  Save and categorize content based on your preferences. 

> This page refers to the `extends` parameter that is part of a [view](https://docs.cloud.google.com/looker/docs/reference/param-view-view).
> 
> `extends` can also be used as part of an Explore, described on the [`extends` (for Explores)](https://docs.cloud.google.com/looker/docs/reference/param-explore-extends) parameter documentation page.
> 
> `extends` can also be used as part of a LookML dashboard, described on the [Dashboard parameters](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard#extends) documentation page.

## Usage
    
    
    view: view_name {
      extends: [view_name, view_name, ...]
    }
    

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) `extends` |  Default Value None Accepts Square brackets containing a comma-separated list of view names  
---|---  
  
## Definition

The `extends` parameter lets you build upon the content and settings from another view file, using the other view file as a starting point. If there are any conflicts, the extending view will use its own settings, overriding the settings of the view being extended. See [Reusing code with extends](https://docs.cloud.google.com/looker/docs/reusing-code-with-extends) for the details of how Looker does this.

> **Check out LookML refinements.**
> 
> Extending a view or an Explore is ideal for scenarios where you want to have multiple versions of the view or Explore. But if your goal is simply to modify a view or an Explore without editing the LookML file that contains it, you may want to use a refinement instead. You can also use an [`extends` parameter inside a refinement](https://docs.cloud.google.com/looker/docs/lookml-refinements#refinements_can_contain_extends). See the [LookML refinements](https://docs.cloud.google.com/looker/docs/lookml-refinements) documentation page for more information and use cases. 

When extending a view, it's important to use the [`sql_table_name`](https://docs.cloud.google.com/looker/docs/reference/param-view-sql-table-name) parameter on the view that is going to be extended, if it's not already there. The `sql_table_name` parameter defines the table in your database that will be queried by a view. For any view the default value is the name of the view. So, if you aren't already using `sql_table_name`, simply give it the same value as your view name.

It's also important that in our new view file we use the [`include`](https://docs.cloud.google.com/looker/docs/reference/param-model-include#using_include_in_a_view_file) parameter to point to the filename of the view we want to extend.

> Avoid extending views that are based on [persistent derived tables (PDTs)](https://docs.cloud.google.com/looker/docs/derived-tables#persistent_derived_table). Each extension of a PDT will create a new copy of the table in your database. In this case, you may want to use LookML refinements instead. See the [LookML refinements](https://docs.cloud.google.com/looker/docs/lookml-refinements) documentation page for more information and use cases.

## Example

Here's an example view file that we can extend. The view is named `looker_events` and the view's filename is `events.view`.

File: `events.view`
    
    
    view: looker_events {
      sql_table_name: looker_db.events ;;
      # The normal contents of the view follow
    }
    

Now we'll create a new view file and define a view that extends the `looker_events` view. In our new file, we must use the [`include`](https://docs.cloud.google.com/looker/docs/reference/param-model-include#using_include_in_a_view_file) parameter to point to the _file_ name of the view we want to extend:

File: `new_events.view`
    
    
    include: "events.view"
    view: name_of_the_new_view {
      extends: [looker_events]
    
      measure: additional_measure {
        type: count
      }
      # Additional things you want to add or change
    }
    

And then we've added a new measure that will show in our new view in addition to all the dimensions and measures that are defined in the `looker_events` view that we extended.

## Using metadata to see extensions for an object

You can click on an `explore` or a `view` parameter in the Looker IDE and use the metadata panel to see any extensions on the object, or to see what object it extends. See the [Metadata for LookML objects](https://docs.cloud.google.com/looker/docs/lookml-metadata) documentation page for information.

## Things to consider

### Some parameters are additive

In many cases, if the extending object contains the same parameter as the object that is being extended, the [extending object's values will override the parameter values of the extended object](https://docs.cloud.google.com/looker/docs/reusing-code-with-extends#step_3:_resolve_conflicts).

But extensions can be _additive_ for some parameters, meaning that the values from the extending object are used in conjunction with the values from the extended object.

The following parameters are _additive_ :

  * For dimensions and measures:

    * [`action`](https://docs.cloud.google.com/looker/docs/reference/param-field-action)
    * [`filters`](https://docs.cloud.google.com/looker/docs/reference/param-field-filters)
    * [`link`](https://docs.cloud.google.com/looker/docs/reference/param-field-link)
  * For views:

    * `extends` (you can [chain together multiple `extends`](https://docs.cloud.google.com/looker/docs/reusing-code-with-extends#chaining_together_multiple_extends))



In the following example, the `carriers` view has a `name` dimension with a `link` parameter:
    
    
    view: carriers {
      sql_table_name: flightstats.carriers ;;
    
      dimension: name {
        sql: ${TABLE}.name ;;
        type: string
        link: {
          label: "Google {{ value }}"
          url: "http://www.google.com/search?q={{ value }}"
          icon_url: "http://google.com/favicon.ico"
        }
      }
    }
    

And here is the `carriers_extended` view, which extends the `carriers` view. The `carriers_extended` view also has a `name` dimension with different settings in the `link` parameter:
    
    
    include: "/views/carriers.view.lkml"
    
    view: carriers_extended {
      extends: [carriers]
    
      dimension: name {
        sql: ${TABLE}.name ;;
        type: string
        link: {
          label: "Dashboard for {{ value }}"
          url: "https://docsexamples.dev.looker.com/dashboards/307?Carrier={{ value }}"
          icon_url: "https://www.looker.com/favicon.ico"
        }
      }
    }
    

In the `carriers_extended` view, the two `link` parameters are additive, so the `name` dimension will have both links.

![](https://docs.cloud.google.com/static/looker/docs/images/dev-refinements-additive-links-2114.png)

### Projects with localization

When extending an object, be aware that localization rules apply to your extensions as well. If you are extending an object and then defining new labels or descriptions, you should provide localization definitions in your project's locale strings files. See the [Localizing your LookML model](https://docs.cloud.google.com/looker/docs/model-localization#understanding_how_localization_rules_apply_to_extended_objects) documentation page for more information.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
