---
url: https://docs.cloud.google.com/data-studio/concat/
title: CONCAT \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:20:34.839482+00:00
---

# CONCAT  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/concat/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  CONCAT Stay organized with collections  Save and categorize content based on your preferences. 

Returns text that is the concatenation of two or more fields or expressions.

## Sample usage

`CONCAT(Campaign, ", ", Campaign Code)`

## Syntax

`CONCAT( X, Y [, Z,...])`

### Parameters

  * `X` \- literal text, a field, or an expression containing at least one field.
  * `Y` \- literal text, a field,or an expression containing at least one field.
  * `Z` \- literal text, a field, or an expression containing at least one field.



### Notes

  * Aggregated fields cannot be used as parameters.



## Examples

In the following examples, note that you can use either single quotes or double quotes, but they must be used consistently.

Example formula | Output  
---|---  
`CONCAT(Campaign, ", ", Campaign Code)` | Summer Sale, SS01  
`CONCAT('Browser: ', Browser, ' OS Version: ', OS version)` | Browser: Edge Version: 85.0.564.44  
  
## Related resources

  * [Calculated fields](https://docs.cloud.google.com/data-studio/about-calculated-fields)
  * [Data Studio function list](https://docs.cloud.google.com/data-studio/function-list)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
