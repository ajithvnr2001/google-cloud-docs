---
url: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/timestamp-as_unix_seconds/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:55:19.882521+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/timestamp-as_unix_seconds/




Stay organized with collections  Save and categorize content based on your preferences. 

### timestamp.as_unix_seconds

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules) [ Search ](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)
    
    
    timestamp.as_unix_seconds(timestamp [, time_zone])
    

#### Description

This function returns an integer representing the number of seconds past a Unix epoch for the given timestamp string.

  * `timestamp` is a string representing a valid epoch timestamp. The format needs to be `%F %T`.
  * `time_zone` is optional and is a string representing a time zone. If omitted, the default is `GMT`. You can specify time zones using string literals. The options are as follows: 
    * The TZ database name, for example `America/Los_Angeles`. For more information, see the [list of tz database time zones on Wikipedia](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).
    * The time zone offset from UTC, in the format`(+|-)H[H][:M[M]]`, for example: "-08:00".



Here are examples of valid `time_zone` specifiers, which you can pass as the second argument to time extraction functions:
    
    
    "America/Los_Angeles", or "-08:00". ("PST" is not supported)
    "America/New_York", or "-05:00". ("EST" is not supported)
    "Europe/London"
    "UTC"
    "GMT"
    

#### Param data types

`STRING`, `STRING`

#### Return type

`INT`

#### Code samples

##### Example 1

Valid epoch timestamp
    
    
    timestamp.as_unix_seconds("2024-02-22 10:43:00") = 1708598580
    

##### Example 2

Valid epoch timestamp with the America/New_York time zone
    
    
    timestamp.as_unix_seconds("2024-02-22 10:43:00", "America/New_York") = 1708616580
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
