---
url: https://docs.cloud.google.com/looker/docs/reference/param-explore-tags/
title: tags (for Explores) \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:24.144175+00:00
---

# tags (for Explores)  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-explore-tags/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  tags (for Explores) Stay organized with collections  Save and categorize content based on your preferences. 

> This page refers to the `tags` parameter that is part of an [Explore](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore).
> 
> `tags` can also be used as part of a field, described on the [`tags` (for fields)](https://docs.cloud.google.com/looker/docs/reference/param-field-tags) parameter documentation page.

## Usage
    
    
    explore: explore_name {
      tags: ["string1","string2", ...]
    }
    

Hierarchy [Model File](https://docs.cloud.google.com/looker/docs/reference/param-model) [`explore`](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) `tags` |  Default Value None Accepts Square brackets containing a comma-separated list of strings  
---|---  
  
## Definition

The `tags` parameter lets you tag an Explore with text strings. These strings are not used by the Looker model but can be passed to other applications, such as [API calls](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/LookmlModel/lookml_model). `tags` can be useful for providing arbitrary metadata about a field to an outside application.

## Examples

Adds two text tags, "Confidential" and "Customer Data", to the `customer_information` Explore.
    
    
    explore: customer_information {
      tags: ["Confidential", "Customer Data"]
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
