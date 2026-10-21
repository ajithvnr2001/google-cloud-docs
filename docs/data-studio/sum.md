---
url: https://docs.cloud.google.com/data-studio/sum/
title: SUM \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:24:31.659501+00:00
---

# SUM  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/sum/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  SUM Stay organized with collections  Save and categorize content based on your preferences. 

Returns the sum of all values in a set of numbers.

## Sample usage

`SUM(Quantity Sold)`

## Syntax

`SUM(X)`

### Parameters

  * `X` \- A numeric field or expression.



### Notes

  * `X` cannot be an aggregated field or the result of an aggregation function.



## Example

Consider the following example. The data source contains a field called "Quantity Sold" with the number of items sold per purchase. Use the `SUM` function to compute the sum of these values.

Example formula | Input | Output  
---|---|---  
`SUM(Quantity Sold)` | 

  * 95
  * 100
  * 92

| 287  
  
## Related resources

  * [Calculated fields](https://docs.cloud.google.com/data-studio/about-calculated-fields)
  * [Data Studio function list](https://docs.cloud.google.com/data-studio/function-list)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
