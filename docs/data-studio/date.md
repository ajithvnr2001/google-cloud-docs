---
url: https://docs.cloud.google.com/data-studio/date/
title: Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:24.547351+00:00
---

# Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/date/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# DATE

Creates a date.

## Sample usage

`DATE(Year, Month, Day)`  
`DATE(Order Date and Time)`

## Syntax

  1. Create a Date from Numbers.

`DATE( year, month, day )`
  2. Create a Date from a Date & Time.

`DATE( datetime_expression )`



### Parameters

  * `year` \- a Number field or expression representing the year.
  * `month` \- a Number field or expression representing the month.
  * `day` \- a Number field or expression representing the day.
  * `datetime_expression` \- a Date & Time field or expression.



## Return data type

Date

## Examples

Example formula | Output  
---|---  
` DATE(2020, 1, 10) ` |  2020-01-10   
` DATE(DATETIME "2020-1-10 23:59:59") ` |  2020-01-10   
  
## Notes

This function is not available for compatibility mode date types.

## Related resources

  * [Dates and times](https://docs.cloud.google.com/data-studio/dates-and-times)
  * [Calculated fields](https://docs.cloud.google.com/data-studio/about-calculated-fields)
  * [Data Studio function list](https://docs.cloud.google.com/data-studio/function-list)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
