---
url: https://docs.cloud.google.com/data-studio/log/
title: LOG \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:06.544732+00:00
---

# LOG  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/log/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  LOG Stay organized with collections  Save and categorize content based on your preferences. 

Returns the logarithm of a number with respect to a base.

The mathematical base used by the `LOG(X)` function varies depending on the data source connector being used.

  * For BigQuery and most other connectors, `LOG(X)` computes the natural logarithm (base _e_).
  * For connectors such as Google Sheets, MySQL, PostgreSQL, Looker, and Extract Data, `LOG(X)` may default to base 2.



The function `LOG(X, base)` with a second argument to specify the base is NOT supported.

**Tip:** For base 10 logarithms, use the `LOG10(X)` function. To calculate a logarithm with a different base 'B', you can use the change of base formula: `LOG10(X) / LOG10(B)`.

## Sample usage

`LOG(256)`

## Syntax

`LOG( value )`

### Parameter

`value` \- The value for which to calculate the logarithm using base e (Euler's number). `value` must be a positive number.

## Examples

Example formula | Input | Output  
---|---|---  
` LOG(My field) ` |  2.718281828459045  |  1   
` LOG(My field) ` |  128  |  4.852030264   
  
## Related resources

  * [Calculated fields](https://docs.cloud.google.com/data-studio/about-calculated-fields)
  * [Data Studio function list](https://docs.cloud.google.com/data-studio/function-list)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
