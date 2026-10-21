---
url: https://docs.cloud.google.com/data-studio/week/
title: Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:24:39.266164+00:00
---

# Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/week/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# WEEK

Returns the week number for a given date.

## Sample usage

`WEEK(Date)`

## Syntax

The following syntax returns the week number from a Date value.

`WEEK( date_expression )`

The following syntax returns the week number from a compatibility mode Date value.

`WEEK( X [, format_string ])`

### Parameters

  * `date_expression` \- a Date & Time field or expression.
  * `X` \- a field or expression that evaluates to Text, Number, or compatibility mode Date.
  * `format_string`\- format for `X`. Optional if `X` is correctly configured as a semantic date field.



#### Format strings for compatibility mode dates

Supported date functions accept the following input formats if `X` is a Text field or expression, or compatibility mode Date:

  * `BASIC`: %Y/%m/%d-%H:%M:%S
  * `DEFAULT_DASH`: %Y-%m-%d [%H:%M:%S]
  * `DEFAULT_SLASH`: %Y/%m/%d [%H:%M:%S]
  * `DEFAULT_DECIMAL`: %Y%m%d [%H:%M:%S]
  * `RFC_1123`: for example, Sat, 24 May 2008 20:09:47 GMT
  * `RFC_3339`: for example, 2008-05-24T20:09:47Z
  * `DECIMAL_DATE`: same as `DEFAULT_DECIMAL`



Any valid [strptime](http://pubs.opengroup.org/onlinepubs/009695399/functions/strptime.html) format is accepted.

Supported time functions accept the following input format if `X` is a Number field or expression:

  * `SECONDS`: seconds since Epoch
  * `MILLIS`: milliseconds since Epoch
  * `MICROS`: microseconds since Epoch
  * `NANOS`: nanoseconds since Epoch
  * `JULIAN_DATE`: days since Epoch



## Examples

Example formula | Input | Output  
---|---|---  
` WEEK(Date) ` |  Jan 1, 2019  |  1   
` WEEK(Date as Text, 'BASIC') ` |  2019/01/01-09:40:45  |  1   
` WEEK(Date as Number, 'SECONDS') ` |  1561784874  |  26   
` WEEK(Date as lots of Numbers, 'MILLIS') ` |  1562004058620  |  27   
  
## Notes

This function works with both compatibility mode dates and [upgraded Date and Date & Time](https://docs.cloud.google.com/data-studio/dates-and-times) data types.

This function returns the week number since the start of year per the ISO 8601 standard.

## Related resources

  * [Dates and times](https://docs.cloud.google.com/data-studio/dates-and-times)
  * [About calculated fields](https://docs.cloud.google.com/data-studio/about-calculated-fields)
  * [Data Studio function list](https://docs.cloud.google.com/data-studio/function-list)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
