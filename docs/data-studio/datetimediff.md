---
url: https://docs.cloud.google.com/data-studio/datetimediff/
title: Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:20:35.558186+00:00
---

# Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/datetimediff/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# DATETIME_DIFF

Returns the number of part boundaries between two dates.

## Sample usage

`DATETIME_DIFF(Order Date, Ship Date, DAY)`

## Syntax

`DATETIME_DIFF( date_expression, date_expression, part )`

### Parameters

  * `date_expression` \- a Date or a Date & Time field or expression. If the first date expression occurs before the second date expression, then the result is zero or negative.
  * `part` \- the time part to return. `DATETIME_DIFF` supports the following parts: 
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

Number (integer)

## Examples

The second and third example in the following table show the result of `DATETIME_DIFF` for two date values that are 24 hours apart. `DATETIME_DIFF` with the part `WEEK` returns 1 because `DATETIME_DIFF` counts the number of part boundaries in this range of date values. Each `WEEK` begins on Sunday, so there is one part boundary between Saturday, 2017-10-14 00:00:00 and Sunday, 2017-10-15 00:00:00.

Example formula | Output  
---|---  
`DATETIME_DIFF( DATETIME "2010-07-07 10:20:00", DATETIME "2008-12-25 15:30:00", DAY )` |  559   
`DATETIME_DIFF( DATETIME "2017-10-15 00:00:00", DATETIME "2017-10-14 00:00:00", DAY )` |  1   
`DATETIME_DIFF( DATETIME "2017-10-15 00:00:00", DATETIME "2017-10-14 00:00:00", WEEK )` |  1   
  
The following example shows the result of `DATETIME_DIFF` for two dates in different years. `DATETIME_DIFF` with the date part `YEAR` returns 3 because it counts the number of Gregorian calendar year boundaries between the two date values. `DATETIME_DIFF` with the date part `ISOYEAR` returns 2 because the second date value belongs to the ISO year 2015. The first Thursday of the 2015 calendar year was 2015-01-01, so the ISO year 2015 begins on the preceding Monday, 2014-12-29.

Example formula  | Output   
---|---  
`DATETIME_DIFF(DATETIME '2017-12-30 00:00:00', DATETIME '2014-12-30 00:00:00', YEAR)` |  3   
`DATETIME_DIFF(DATETIME '2017-12-30 00:00:00', DATETIME '2014-12-30 00:00:00', ISOYEAR)` |  2   
  
The following example shows the result of `DATETIME_DIFF` for two days in succession. The first date falls on a Monday and the second date falls on a Sunday. `DATETIME_DIFF` with the date part `ISOWEEK` also returns 1 because ISO weeks begin on Monday.

Example formula  | Output   
---|---  
DATETIME_DIFF(DATE '2017-12-18', DATE '2017-12-17', WEEK) |  0   
`DATETIME_DIFF(DATE '2017-12-18', DATE'2017-12-17', ISOWEEK)` |  1   
  
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
