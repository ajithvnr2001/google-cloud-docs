---
url: https://docs.cloud.google.com/looker/docs/reference/param-model-persist-with/
title: persist_with (for models) \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:19.114342+00:00
---

# persist_with (for models)  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-model-persist-with/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  persist_with (for models) Stay organized with collections  Save and categorize content based on your preferences. 

> This page refers to the `persist_with` parameter that is part of a [model](https://docs.cloud.google.com/looker/docs/reference/param-model).
> 
> `persist_with` can also be used as part of an Explore, described on the [`persist_with`](https://docs.cloud.google.com/looker/docs/reference/param-explore-persist-with) parameter documentation page.

## Usage
    
    
    
    persist_with: airports_datagroup
    

Hierarchy [Model File](https://docs.cloud.google.com/looker/docs/reference/param-model) `persist_with` |  Default Value None Accepts The name of a [datagroup](https://docs.cloud.google.com/looker/docs/reference/param-model-datagroup).   
---|---  
  
## Definition

Use `persist_with` at the model level to specify the default [`datagroup`](https://docs.cloud.google.com/looker/docs/reference/param-model-datagroup) caching policy to use for all Explores in the model. See the [Caching queries and rebuilding PDTs with datagroups](https://docs.cloud.google.com/looker/docs/caching-and-datagroups#specifying_caching_policies_with_datagroup_parameters) documentation page for an overview of datagroups.

> To specify a datagroup for just one or more Explores, or to override the default datagroup for one or more Explores, you can use the [`persist_with` parameter for `explore`](https://docs.cloud.google.com/looker/docs/reference/param-explore-persist-with) to specify a different datagroup for those Explores.

## Example

Use the `orders_datagroup` caching policy for all Explores in the model:
    
    
    persist_with: orders_datagroup
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
