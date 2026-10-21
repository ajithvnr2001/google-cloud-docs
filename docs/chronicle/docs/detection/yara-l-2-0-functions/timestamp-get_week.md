---
url: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/timestamp-get_week/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T13:50:11.034678+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/timestamp-get_week/




Stay organized with collections  Save and categorize content based on your preferences. 

### timestamp.get_week

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules) [ Search ](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)
    
    
    timestamp.get_week(unix_seconds [, time_zone])
    

#### Description

This function returns an integer in the range `[0, 53]` representing the week of the year. Weeks begin with Sunday. Dates before the first Sunday of the year are in week 0.

  * `unix_seconds` is an integer representing the number of seconds past Unix epoch, such as `$e.metadata.event_timestamp.seconds`, or a placeholder containing that value.
  * `time_zone` is optional and is a string representing a time zone. If omitted, the default is "GMT". You can specify time zones using string literals. The options are: 
    * The TZ database name, for example "America/Los_Angeles". For more information, see the ["TZ Database Name" column from this page](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)
    * The time zone offset from UTC, in the format`(+|-)H[H][:M[M]]`, for example: "-08:00".



Here are examples of valid `time_zone` specifiers, which you can pass as the second argument to time extraction functions:
    
    
    "America/Los_Angeles", or "-08:00". ("PST" is not supported)
    "America/New_York", or "-05:00". ("EST" is not supported)
    "Europe/London"
    "UTC"
    "GMT"
    

#### Param data types

`INT`, `STRING`

#### Return type

`INT`

#### Code samples

##### Example 1

In this example, the `time_zone` argument is omitted, so it defaults to "GMT".
    
    
    $ts = $e.metadata.collected_timestamp.seconds
    
    timestamp.get_week($ts) = 0
    

##### Example 2

This example uses a string literal to define the `time_zone`.
    
    
    $ts = $e.metadata.collected_timestamp.seconds
    
    timestamp.get_week($ts, "America/Los_Angeles") = 0
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
