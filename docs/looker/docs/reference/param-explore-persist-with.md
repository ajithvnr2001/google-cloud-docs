---
url: https://docs.cloud.google.com/looker/docs/reference/param-explore-persist-with/
title: persist_with (for Explores) \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:23.083863+00:00
---

# persist_with (for Explores)  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-explore-persist-with/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  persist_with (for Explores) Stay organized with collections  Save and categorize content based on your preferences. 

> This page refers to the `persist_with` parameter that is part of an [Explore](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore).
> 
> `persist_with` can also be used as part of a model, described on the [`persist_with`](https://docs.cloud.google.com/looker/docs/reference/param-model-persist-with) parameter documentation page.

## Usage
    
    
    explore: explore_name {
      persist_with: airports_datagroup
    }
    

Hierarchy [Model File](https://docs.cloud.google.com/looker/docs/reference/param-model) [`explore`](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) `persist_with` |  Default Value None Accepts The name of a [datagroup](https://docs.cloud.google.com/looker/docs/reference/param-model-datagroup).   
---|---  
  
## Definition

Use `persist_with` under the `explore` parameter to specify a [`datagroup`](https://docs.cloud.google.com/looker/docs/reference/param-model-datagroup) caching policy to use for that specific Explore.

> To specify a default datagroup for all Explores in a model, you can use the [`persist_with`](https://docs.cloud.google.com/looker/docs/reference/param-model-persist-with) parameter at the model level.

If you include a `persist_with` parameter under the `explore` parameter and also at the model level, the Explore will use the datagroup caching policy specified under the `explore` parameter.

See [caching](https://docs.cloud.google.com/looker/docs/caching-and-datagroups#specifying_caching_policies_with_datagroup_parameters) for an overview of datagroups.

## Example

Use the `orders_datagroup` caching policy for an Explore:
    
    
    explore: customer_facts {
      persist_with: orders_datagroup
      ...
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
