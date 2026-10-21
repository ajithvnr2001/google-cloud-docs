---
url: https://docs.cloud.google.com/data-studio/currentdatetime/
title: Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:24:35.245526+00:00
---

# Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/currentdatetime/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# CURRENT_DATETIME

Returns the current date and time according to the specified or default timezone.

## Sample usage

`CURRENT_DATETIME()`  
`CURRENT_DATETIME("America/Los_Angeles")`

## Syntax

`CURRENT_DATETIME([time_zone_name])`

### Parameters

  * `time_zone_name` \- Optional. A text field or an expression that represents the time zone.



#### Time zone name

A time zone name is a tz identifier from the [tz database](http://www.iana.org/time-zones).

For a less comprehensive but simpler reference, see the [List of tz database time zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) on Wikipedia.

Examples:
    
    
    America/Los_Angeles
    America/Argentina/Buenos_Aires
    Etc/UTC
    Pacific/Auckland
    

When you use a time zone name, a space is required between the name and the rest of the timestamp:
    
    
    2014-09-27 12:30:00.45 America/Los_Angeles
    

Note that not all time zone names are interchangeable even if they report the same time during a given part of the year. For example, `America/Los_Angeles` reports the same time as `UTC-7:00` during daylight saving time (DST), but it reports the same time as `UTC-8:00` outside of DST.

If a time zone isn't specified, the default time zone value, UTC, is used.

If the `time_zone_name` parameter evaluates to `NULL`, this function returns `NULL`.

## Return data type

Date & Time

## Examples

Example formula  
---  
`CURRENT_DATETIME()`  
`CURRENT_DATETIME("America/Los_Angeles")`  
`CURRENT_DATETIME("Asia/Tokyo")`  
  
## Notes

This function is not available for [compatibility mode date types](https://docs.cloud.google.com/data-studio/dates-and-times#date_time_compatibility_mode).

## Related resources

  * [Dates and times](https://docs.cloud.google.com/data-studio/dates-and-times)
  * [Calculated fields](https://docs.cloud.google.com/data-studio/about-calculated-fields)
  * [Data Studio function list](https://docs.cloud.google.com/data-studio/function-list)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
