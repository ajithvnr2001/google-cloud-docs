---
url: https://docs.cloud.google.com/data-studio/startswith/
title: STARTS_WITH \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:32:47.501021+00:00
---

# STARTS_WITH  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/startswith/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  STARTS_WITH Stay organized with collections  Save and categorize content based on your preferences. 

Returns `true` if the field or expression begins with the specified text; otherwise, returns `false`.

## Sample usage

`STARTS_WITH(Campaign, "Summer")`

## Syntax

`STARTS_WITH(X, text)`

### Parameters

  * `X` \- A field or expression of any type.
  * `text` \- The text to find within X. `text` can be a field, an expression, or a literal value. `text` is case-sensitive.



## Examples

Example formula | Input | Output  
---|---|---  
` STARTS_WITH(Campaign, "Summer")` | Summer Sale |  true  
` STARTS_WITH(Campaign, "Sale") ` |  Summer Sale |  false  
  
## Related resources

  * [Calculated fields](https://docs.cloud.google.com/data-studio/about-calculated-fields)
  * [Data Studio function list](https://docs.cloud.google.com/data-studio/function-list)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
