---
url: https://docs.cloud.google.com/data-studio/extract/
title: Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:19:52.137747+00:00
---

# Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/extract/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# EXTRACT

Returns part of a date.

## Sample usage

```EXTRACT(QUARTER FROM Order Date)```

## Syntax

1) Returns a date part.

```EXTRACT( part FROM date_expression )```

2) Returns a Date from a Date & Time field or expression.

```EXTRACT(DATE FROM date_expression )```

### Parameters

```date_expression``` \- a Date or a Date & Time field or expression.

```part``` \- the date part to return. ```EXTRACT``` supports the following parts:

  * ```DAYOFWEEK``` : Returns values in the range [1, 7] with Sunday as the first day of the week.
  * ```DAY```
  * ```DAYOFYEAR```
  * ```WEEK``` : Returns the week number of the date in the range [0, 53]. Weeks begin with Sunday, and dates prior to the first Sunday of the year are in week 0.
  * ```ISOWEEK``` : Returns the [ISO 8601 week](https://en.wikipedia.org/wiki/ISO_week_date) number of the ```date_expression``` -. ```ISOWEEK``` s begin on Monday. Returns values in the range [1, 53]. The first ```ISOWEEK``` of each ISO year begins on the Monday before the first Thursday of the Gregorian calendar year.
  * ```MONTH```
  * ```QUARTER``` : Returns values in the range [1, 4].
  * ```YEAR```
  * ```ISOYEAR``` : Returns the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) week-numbering year, which is the Gregorian calendar year containing the Thursday of the week to which ```date_expression``` \- belongs.



## Return data types

  1. **Number** (integer)
  2. **Date**



## Examples

In the following example, ```EXTRACT``` returns a value corresponding to the ```DAY``` time part.

Example formula | Output  
---|---  
` EXTRACT(DAY FROM DATE '2013-12-25') ` |  25   
  
In the following example, ```EXTRACT``` returns values corresponding to different time parts from a column of dates near the end of the year.

Field name | Example formula  
---|---  
Isoyear  |  ` EXTRACT(ISOYEAR FROM Date) `  
Isoweek  |  ` EXTRACT(ISOWEEK FROM Date) `  
Year  |  ` EXTRACT(YEAR FROM Date) `  
Week  |  ` EXTRACT(WEEK FROM Date) `  
  
**Output:**

Input date | Isoyear | Isoweek | Year | Week  
---|---|---|---|---  
2015-12-23  |  2015  |  52  |  2015  |  51   
2015-12-24  |  2015  |  52  |  2015  |  51   
2015-12-25  |  2015  |  52  |  2015  |  51   
2015-12-26  |  2015  |  52  |  2015  |  51   
2015-12-27  |  2015  |  52  |  2015  |  52   
2015-12-28  |  2015  |  53  |  2015  |  52   
2015-12-29  |  2015  |  53  |  2015  |  52   
2015-12-30  |  2015  |  53  |  2015  |  52   
2015-12-31  |  2015  |  53  |  2015  |  52   
2016-01-01  |  2015  |  53  |  2016  |  0   
2016-01-02  |  2015  |  53  |  2016  |  0   
2016-01-03  |  2015  |  53  |  2016  |  1   
2016-01-04  |  2016  |  1  |  2016  |  1   
2016-01-05  |  2016  |  1  |  2016  |  1   
2016-01-06  |  2016  |  1  |  2016  |  1   
2016-01-07  |  2016  |  1  |  2016  |  1   
2016-01-08  |  2016  |  1  |  2016  |  1   
2016-01-09  |  2016  |  1  |  2016  |  1   
  
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
