---
url: https://docs.cloud.google.com/looker/docs/reference/param-view-extension/
title: extension (for views) \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:26.887374+00:00
---

# extension (for views)  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-view-extension/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  extension (for views) Stay organized with collections  Save and categorize content based on your preferences. 

> This page refers to the `extension` parameter that is part of a [view](https://docs.cloud.google.com/looker/docs/reference/param-view-view).
> 
> `extension` can also be used as part of an Explore, described on the [`extension` (for Explores)](https://docs.cloud.google.com/looker/docs/reference/param-explore-extension) parameter documentation page.
> 
> `extension` can also be used as part of a LookML dashboard, described on the [Dashboard parameters](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard#extension) documentation page.

## Usage
    
    
    view: view_name {
      extension: required
    }
    

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) `extension` |  Default Value None Accepts The value "required"   
---|---  
  
## Definition

The `extension: required` parameter flags a view as requiring extension, which means that the view cannot be used on its own. The contents and settings of the view will only be used when the view is extended using the [`extends`](https://docs.cloud.google.com/looker/docs/reference/param-view-extends) parameter in another view.

A view with `extension: required` is not visible to users on its own; it is intended only to act as a starting point to be extended by other views.

The `extension` parameter accepts only the value `required`. If you don't want to require extension for a view, leave out the `extension` parameter entirely.

See [Reusing code with extends](https://docs.cloud.google.com/looker/docs/reusing-code-with-extends) for more information on using `extends` for LookML objects.

## Example

The following `looker_events` view has the `extension: required` parameter, so the view itself won't be visible to users:

File: `events.view`
    
    
    view: looker_events {
      extension: required
      sql_table_name: looker_db.events ;;
      # The normal contents of the view follow
    }
    

If we want to make use of the `looker_events` view, we can create another view that extends it, like this:

File: `new_events.view`
    
    
    include: "events.view"
    view: name_of_the_new_view {
      extends: [looker_events]
    
      measure: additional_measure {
        type: count
      }
      # Additional things you want to add or change
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
