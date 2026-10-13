---
url: https://docs.cloud.google.com/looker/docs/reference/param-explore-description/
title: description (for Explores) \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:20.984226+00:00
---

# description (for Explores)  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-explore-description/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  description (for Explores) Stay organized with collections  Save and categorize content based on your preferences. 

> This page refers to the `description` parameter that is part of an [Explore](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore).
> 
> `description` can also be used as part of a field, described on the [`description` (for fields)](https://docs.cloud.google.com/looker/docs/reference/param-field-description) parameter documentation page.
> 
> `description` can also be used as part of a dashboard, described on the [Dashboard parameters](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard#description-for-dashboard) documentation page.

## Usage
    
    
    explore: explore_name {
      description: "Description I Want"
    }
    

Hierarchy [Model File](https://docs.cloud.google.com/looker/docs/reference/param-model) [`explore`](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) `description` |  Default Value None Accepts A string  
---|---  
  
## Definition

`description` lets you add information about the [Explore](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) to the UI, so users can get additional information while creating Explore queries. For example, here is a `description` parameter:
    
    
    explore: order_items {
      description: "Based on the individual items that comprise customer orders"
    }
    

If a `description` is added to an Explore, users can see the description by hovering over the information icon next to the Explore name at the top of the field picker.

![](https://docs.cloud.google.com/static/looker/docs/images/develop-params-description-explore-ui-2112.png)

Users can also view a description by hovering over the same information icon in the drop-down list of Explores.

![](https://docs.cloud.google.com/static/looker/docs/images/dev-description-explore-menu-2216.png)

If you do not explicitly add a `description` to an [Explore](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore), no description will be shown.

## Examples

Add a description to an Explore named **User** :
    
    
    explore: user {
      description: "All customer users, staff users are excluded"
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
