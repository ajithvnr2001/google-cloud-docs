---
url: https://docs.cloud.google.com/data-studio/todate/
title: Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:53.451294+00:00
---

# Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/todate/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# TODATE

Returns a formatted compatibility mode date.

**Important:** This function only supports compatibility mode dates.

We recommend upgrading any older date fields in your data sources to the new Date or Date & Time types. After upgrading: 

  * You can use the `FORMAT_DATETIME` function to format a date as text.
  * You can use the `PARSE_DATE` and `PARSE_DATETIME` functions to convert text into Date and Date & Time fields.



[Learn more](https://docs.cloud.google.com/data-studio/formatdatetime).

You can use `TODATE` in 2 ways:

  * Create a compatibility mode date from Text fields.
  * Change the display format and granularity of a compatibility mode date.



## Sample usage

`TODATE(Text_Date,"%Y/%m/%d","%Y-%m-%d")`

`TODATE(Text_Date,"%Y/%m/%d","%Y-%m-%d")`

`TODATE(Response_Time, 'MILLIS', '%Y%m%d')`

`TODATE(Created_Time, 'DECIMAL_DATE', '%Y')`

## Syntax

`TODATE(field_expression, input_date_format, output_date_format)`

## Input formats

`input_date_format` is optional if `field_expression` is correctly configured as a semantic date.

`TODATE` accepts the following input format strings.

  * 'BASIC': %Y/%m/%d-%H:%M:%S

  * 'DEFAULT_DASH': %Y-%m-%d [%H:%M:%S]

  * 'DEFAULT_SLASH': %Y/%m/%d [%H:%M:%S]

  * 'DEFAULT_DECIMAL': %Y%m%d [%H:%M:%S]

  * 'RFC_1123': for example, Sat, 24 May 2008 20:09:47 GMT

  * 'RFC_3339': for example, 2008-05-24T20:09:47Z

  * 'SECONDS': seconds since Epoch

  * 'MILLIS': milliseconds since Epoch

  * 'MICROS': microseconds since Epoch

  * 'NANOS': nanoseconds since Epoch

  * 'JULIAN_DATE': days since Epoch

  * 'DECIMAL_DATE': same as 'DEFAULT_DECIMAL'

  * Any valid [strptime](http://pubs.opengroup.org/onlinepubs/009695399/functions/strptime.html) format. Optional if the value is already a datetime field.




## Output formats

`TODATE` accepts the following output format strings:

  * "%Y"  \- year
  * "%m"  \- month
  * "%d"  \- day
  * "%W"  \- yearweek number
  * "%w"  \- day of week
  * "%H"  \- hour
  * "%M"  \- minute



### Examples

Example formula  |  Input  |  Output   
---|---|---  
` TODATE(Text_Date,"%Y/%m/%d","%Y-%m-%d") ` |  2024/05/09  |  2024-05-09   
` TODATE(Response_Time, 'MILLIS', '%Y%m%d') ` |  1715294861000  |  20240509   
` TODATE(Created_time, 'DECIMAL_DATE', '%Y') ` |  20240509[11:34:12]  |  2024   
  
## Notes

`TODATE` returns compatibility mode Date data types.

## Related resources

  * [Dates and times](https://docs.cloud.google.com/data-studio/dates-and-times)
  * [Calculated fields](https://docs.cloud.google.com/data-studio/about-calculated-fields)
  * [Data Studio function list](https://docs.cloud.google.com/data-studio/function-list)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
