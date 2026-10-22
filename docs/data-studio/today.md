---
url: https://docs.cloud.google.com/data-studio/today/
title: Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:53.300929+00:00
---

# Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/today/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# TODAY

Returns the current date according to the specified or default timezone.

## Sample usage

`TODAY()`

`TODAY("America/Los_Angeles")`

`TODAY("-08")`

## Syntax

`TODAY([time_zone])`

### Parameters

  * time_zone \- Optional. A text field or expression representing the timezone to use. If no timezone is specified, the default timezone UTC is used. See [Timezone definitions](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/timestamp_functions#timezone_definitions) for information on how to specify a time zone.

If the  time_zone parameter evaluates to `NULL`, this function returns `NULL`.




## Return data type

Date

## Examples

Example formula  |  Input  |  Output   
---|---|---  
` TODAY() ` |  January 10, 2020  |  2020-1-10   
  
## Notes

`TODAY` is a synonym for [`CURRENT_DATE`](https://docs.cloud.google.com/data-studio/currentdate).

## Related resources

  * [Dates and times](https://docs.cloud.google.com/data-studio/dates-and-times)
  * [Calculated fields](https://docs.cloud.google.com/data-studio/about-calculated-fields)
  * [Data Studio function list](https://docs.cloud.google.com/data-studio/function-list)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
