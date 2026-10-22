---
url: https://docs.cloud.google.com/data-studio/formatdatetime/
title: Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:18.844596+00:00
---

# Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/formatdatetime/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# FORMAT_DATETIME

Converts a date or date and time to formatted text.

## Sample usage

`FORMAT_DATETIME("%c", Order Date)`

## Syntax

`FORMAT_DATETIME( format_string, date_expression )`

### Parameters

`format_string` \- See [Supported Format Elements For DATETIME](https://cloud.google.com/bigquery/docs/reference/standard-sql/format-elements#format_elements_date_time) for a list of format elements that this function supports.

`date_expression` \- a Date or a Date & Time field or expression.

## Return data type

Text 1

## Examples

Example formula | Output  
---|---  
` FORMAT_DATETIME("%x", DATE "2008-12-25") ` |  12/25/08   
` FORMAT_DATETIME("%c", DATETIME "2008-12-25 15:30:00") ` |  Thu Dec 25 15:30:00 2008   
` FORMAT_DATETIME("%b-%d-%Y", DATETIME "2008-12-25 15:30:00") ` |  Dec-25-2008   
  
## Notes

This function is not available for compatibility mode date types.

  1. Date strings may be interpreted as compatibility mode Date data types. To preserve the specified format, change the field type to Text.



## Related resources

  * [Dates and times](https://docs.cloud.google.com/data-studio/dates-and-times)
  * [Calculated fields](https://docs.cloud.google.com/data-studio/about-calculated-fields)
  * [Data Studio function list](https://docs.cloud.google.com/data-studio/function-list)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
