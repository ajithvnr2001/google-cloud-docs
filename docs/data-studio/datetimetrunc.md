---
url: https://docs.cloud.google.com/data-studio/datetimetrunc/
title: Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:19:39.367570+00:00
---

# Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/datetimetrunc/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# DATETIME_TRUNC

Truncates a date to the specified granularity.

## Sample usage

`DATETIME_TRUNC(Order Date, MONTH)`

## Syntax

`DATETIME_TRUNC( date_expression, part )`

### Parameters

`date_expression` \- a Date or a Date & Time field or expression.

`part` \- the time part to return. `DATETIME_TRUNC` supports the following time parts:

  * `MICROSECOND`: available for Date & Time fields or expressions.
  * `MILLISECOND`: available for Date & Time fields or expressions.
  * `SECOND`: available for Date & Time fields or expressions.
  * `MINUTE`: available for Date & Time fields or expressions.
  * `HOUR`: available for Date & Time fields or expressions.
  * `DAY`
  * `WEEK`: This date part begins on Sunday.
  * `ISOWEEK`: Uses [ISO 8601 week](https://en.wikipedia.org/wiki/ISO_week_date) boundaries. ISO weeks begin on Monday.
  * `MONTH`
  * `QUARTER`
  * `YEAR`
  * `ISOYEAR`: Uses the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) week-numbering year boundary. The ISO year boundary is the Monday of the first week whose Thursday belongs to the corresponding Gregorian calendar year.



## Return data type

Date & Time

## Examples

Example formula | Output  
---|---  
`DATETIME_TRUNC(DATE '2008-12-25', MONTH)` |  2008-12-01 00:00:00   
`DATETIME_TRUNC(DATETIME "2008-12-25 15:30:00", DAY)` |  2008-12-25 00:00:00   
  
In the following example, the original date_expression is in the Gregorian calendar year 2015. However, DATE_TRUNC with the ISOYEAR date part truncates the date_expression to the beginning of the ISO year, not the Gregorian calendar year. The first Thursday of the 2015 calendar year was 2015-01-01, so the ISO year 2015 begins on the preceding Monday, 2014-12-29. Therefore the ISO year boundary preceding the date_expression 2015-06-15 is 2014-12-29.

Example formula | Output  
---|---  
`DATE_TRUNC('2015-06-15', ISOYEAR)` |  2014-12-29   
`EXTRACT(ISOYEAR FROM DATETIME '2015-06-15')` |  2015   
  
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
