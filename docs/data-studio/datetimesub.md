---
url: https://docs.cloud.google.com/data-studio/datetimesub/
title: Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:24:36.912651+00:00
---

# Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/datetimesub/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# DATETIME_SUB

Subtracts a specified time interval from a date.

## Sample usage

`DATETIME_SUB(Order Date, INTERVAL 1 WEEK)`

## Syntax

`DATETIME_SUB( datetime_expression, INTERVAL integer part )`

### Parameters

  * `datetime_expression` \- a Date or a Date & Time field or expression.
  * `integer` \- a whole numeric field or expression representing the number of parts to subtract.
  * `part` \- the unit of time measurement to subtract. DATETIME_ADD supports the following values for `part`: 
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
`DATETIME_SUB(DATETIME "2008-12-25 15:30:00", INTERVAL 10 MINUTE)` |  2008-12-25 15:20:00   
`DATETIME_SUB(DATE "2008-12-25", INTERVAL 5 DAY)` |  2008-12-20   
  
## Notes

This function is not available for compatibility mode date types.

Special handling is required for `MONTH`, `QUARTER`, and `YEAR` parts when the date is at (or near) the last day of the month. If the resulting month has fewer days than the original Date or Date & Time's day, then the result day is the last day of the new month.

## Related resources

  * [Dates and times](https://docs.cloud.google.com/data-studio/dates-and-times)
  * [Calculated fields](https://docs.cloud.google.com/data-studio/about-calculated-fields)
  * [Data Studio function list](https://docs.cloud.google.com/data-studio/function-list)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
