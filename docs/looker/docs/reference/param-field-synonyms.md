---
url: https://docs.cloud.google.com/looker/docs/reference/param-field-synonyms/
title: synonyms \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:39.544409+00:00
---

# synonyms  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-field-synonyms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  synonyms Stay organized with collections  Save and categorize content based on your preferences. 

## Usage
    
    
    view: view_name {
      dimension: field_name {
        synonyms: ["synonym1", "synonym2", "…"]
      }
    }
    

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) [Field Type](https://docs.cloud.google.com/looker/docs/reference/param-field) `synonyms` |  Possible Field Types Dimension, Dimension group, Measure, Filter, Parameter Accepts A string or a list of strings  
---|---  
  
## Definition

The `synonyms` LookML parameter lets you specify a list of words or phrases that can be used to help large language models or application developers understand other ways that users may refer to a field. Synonyms aren't surfaced in a Looker Explore but instead appear as part of a field's metadata when you use the Looker API to [get information about a LookML model](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/LookmlModel/lookml_model_explore).

**Important:** The **Use Legacy LookML Runtime** [legacy feature](https://docs.cloud.google.com/looker/docs/legacy-feature-schedule#current_legacy_features) must be disabled to use `synonyms`.

## Example
    
    
    dimension: customer_password {
      type: string
      sql: ${TABLE}.customer_password ;;
      synonyms: ["password"]
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
