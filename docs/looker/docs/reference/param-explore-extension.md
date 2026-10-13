---
url: https://docs.cloud.google.com/looker/docs/reference/param-explore-extension/
title: extension (for Explores) \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:21.778337+00:00
---

# extension (for Explores)  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-explore-extension/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  extension (for Explores) Stay organized with collections  Save and categorize content based on your preferences. 

> This page refers to the `extension` parameter that is part of an [Explore](https://docs.cloud.google.com/looker/docs/reference/param-explore).
> 
> `extension` can also be used as part of a view, as described on the [`extension` (for views)](https://docs.cloud.google.com/looker/docs/reference/param-view-extension) parameter documentation page.
> 
> `extension` can also be used as part of a LookML dashboard, as described on [Dashboard parameters](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard#extension) documentation page.

## Usage
    
    
    
    explore: explore_name {
      extension: required
    }
    

Hierarchy [Model File](https://docs.cloud.google.com/looker/docs/reference/param-model) [`explore`](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) `extension` |  Default Value None Accepts The value "required"   
---|---  
  
## Definition

The `extension: required` parameter flags an Explore as requiring extension, which means that the Explore cannot be used on its own. The contents and settings of the Explore will only be used when the Explore is extended using the [`extends`](https://docs.cloud.google.com/looker/docs/reference/param-explore-extends) parameter in another Explore.

An Explore with `extension: required` is not visible to users on its own; it is intended only to act as a starting point to be extended by other Explores.

The `extension` parameter accepts only the value `required`. If you don't want to require extension for an Explore, leave out the `extension` parameter entirely.

An Explore with `extension: required` cannot be used as an `explore_source` for a [data test](https://docs.cloud.google.com/looker/docs/reference/param-model-test). The [LookML Validator](https://docs.cloud.google.com/looker/docs/lookml-validation#validating_your_changes) will generate an error that the `explore_source` cannot be found.

See [Reusing Code with Extends](https://docs.cloud.google.com/looker/docs/reusing-code-with-extends) for more information on using `extends` for LookML objects.

## Example

This `basic_order_fields` Explore has the `extension: required` parameter, so the Explore itself will not be visible to users:
    
    
    explore: basic_order_fields {
      extension: required
    }
    

To make use of the `basic_order_fields` Explore, we can create another Explore that extends it, like this:
    
    
    explore: marketing_order_fields {
      extends: [basic_order_fields]
    }
    

It may be tempting to turn on [`hidden`](https://docs.cloud.google.com/looker/docs/reference/param-explore-hidden) to hide **Basic Order Fields** , but remember that such a setting is going to be inherited by any Explore that is based on **Basic Order Fields**. In this particular example, **Marketing Order Fields** would be hidden as well if you turned on [`hidden`](https://docs.cloud.google.com/looker/docs/reference/param-explore-hidden).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-09-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-09-19 UTC."],[],[]] 
