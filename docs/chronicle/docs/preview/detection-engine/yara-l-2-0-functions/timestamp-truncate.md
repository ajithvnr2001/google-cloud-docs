---
url: https://docs.cloud.google.com/chronicle/docs/preview/detection-engine/yara-l-2-0-functions/timestamp-truncate/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T13:25:15.748721+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/preview/detection-engine/yara-l-2-0-functions/timestamp-truncate/




Stay organized with collections  Save and categorize content based on your preferences. 

### timestamp.truncate

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules) [ Search ](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)
    
    
    timestamp.truncate(epoch, time_unit, timezone)
    

#### Description

Returns an integer representing the Unix seconds of the truncated time. By default truncates the `DAY` version of this function if second argument is not specified. Time_unit can be specified as SECOND, MINUTE, HOUR, DAY, WEEK, ISOWEEK, MONTH, QUARTER, YEAR, or ISOYEAR.

#### Param data types

`INT`, `STRING`, `STRING`

#### Return type

`INT`

#### Code samples

Get Unix seconds of the truncated time.

##### Example 1

This example extracts the day from the timestamp.
    
    
    timestamp.truncate(1716921177, "DAY", "America/Los_Angeles") = 1716879600
    

##### Example 2

This example extracts the minute from the timestamp.
    
    
    timestamp.truncate(1230192123, "MINUTE", "GMT") = 1230192120
    

##### Example 3

This example extracts the hour from the timestamp.
    
    
    timestamp.truncate(1230192123, "HOUR", "GMT") = 1230192000
    

##### Example 4

This example extracts the week from the timestamp.
    
    
    timestamp.truncate(1230192123, "WEEK", "GMT") = 1229817600
    

##### Example 5

This example extracts the ISO week from the timestamp.
    
    
    timestamp.truncate(1230192123, "ISOWEEK", "GMT") = 1229904000
    

##### Example 6

This example extracts the month from the timestamp.
    
    
    timestamp.truncate(1230192123, "MONTH", "GMT") = 1228089600
    

##### Example 7

This example extracts the quarter from the timestamp.
    
    
    timestamp.truncate(1230192123, "QUARTER", "GMT") = 1222819200
    

##### Example 8

This example extracts the year from the timestamp.
    
    
    timestamp.truncate(1230192123, "YEAR", "GMT") = 1199145600
    

##### Example 9

This example extracts the ISO year from the timestamp.
    
    
    timestamp.truncate(1230192123, "ISOYEAR", "GMT") = 1199059200
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
