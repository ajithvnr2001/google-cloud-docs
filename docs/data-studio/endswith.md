---
url: https://docs.cloud.google.com/data-studio/endswith/
title: ENDS_WITH \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:19:51.636137+00:00
---

# ENDS_WITH  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/endswith/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  ENDS_WITH Stay organized with collections  Save and categorize content based on your preferences. 

Returns `true` if the field or expression ends with the specified text; otherwise, returns `false`.

## Sample usage

```ENDS_WITH(Campaign, "Sale")```

## Syntax

```ENDS_WITH( X, text )```

### Parameters

  * `X` \- a field or expression of any type.
  * `text` \- the text to find within X. `text` can be a field, an expression, or a literal value. `text` is case-sensitive.



## Examples

Example formula | Input | Output  
---|---|---  
` ENDS_WITH(Campaign, "Sale") ` |  Summer Sale  |  true   
` ENDS_WITH(Campaign, "Summer") ` |  Summer Sale  |  false   
  
## Related resources

  * [Calculated fields](https://docs.cloud.google.com/data-studio/about-calculated-fields)
  * [Data Studio function list](https://docs.cloud.google.com/data-studio/function-list)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
