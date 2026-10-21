---
url: https://docs.cloud.google.com/data-studio/substr/
title: SUBSTR \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:00:37.665141+00:00
---

# SUBSTR  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/substr/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  SUBSTR Stay organized with collections  Save and categorize content based on your preferences. 

Returns a specific sequence of characters from the text.

## Sample usage

`SUBSTR(Campaign, 1, 6)`

## Syntax

`SUBSTR(X, start_index, length)`

### Parameters

  * `X` \- A field or expression of any type.
  * `start_index` \- The position from the start of the string from which to begin extracting.
  * `length` \- The number of characters to extract.



### Notes

  * The first character of a field is at index 1.
  * To begin extracting from the end of the string, use a negative index. The last character of a string is at index -1, the second to the last is at -2, etc.



## Examples

Example formula | Input | Output  
---|---|---  
`SUBSTR(Campaign, 1, 6)` | Summer Sale | Summer  
`SUBSTR(Campaign, -4, 4)` | Summer Sale | Sale  
  
## Related resources

  * [Calculated fields](https://docs.cloud.google.com/data-studio/about-calculated-fields)
  * [Data Studio function list](https://docs.cloud.google.com/data-studio/function-list)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
