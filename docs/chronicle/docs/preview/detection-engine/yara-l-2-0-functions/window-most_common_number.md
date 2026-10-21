---
url: https://docs.cloud.google.com/chronicle/docs/preview/detection-engine/yara-l-2-0-functions/window-most_common_number/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:38:22.964236+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/preview/detection-engine/yara-l-2-0-functions/window-most_common_number/




Stay organized with collections  Save and categorize content based on your preferences. 

### window.most_common_number

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules) [ Search ](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)
    
    
    window.most_common_number(numbers, how_many_to_retrieve)
    

#### Description

Return the specified number of most common integers or floats in the input values.

#### Param data types

`INT|FLOAT`, `INT`

#### Return type

`ARRAY_FLOATS`

#### Code samples

##### Example 1

Top 1 This rule sets the value of the outcome variable $p1 to an array containing just the most common file size
    
    
    events:
     $e.user.userid = $userid
    match:
     $userid over 5m
    outcome:
      $p1 = window.most_common_number($e.file.size, 1) // yields 66 if the event file size values in the match window are 33, 33, 66, 66, 66 and 1.
    condition:
      $e
    

##### Example 2

Here, number of retrieves more than number of file sizes.
    
    
    events:
     $e.user.userid = $userid
    match:
     $userid over 5m
    outcome:
      $p100 = window.most_common_number($e.file.size, 100) // yields [15.130000, 9.180000, 1.000000] if the event file size values in the match window are [9.18, 9.18, 15.13, 15.13, 15.13, 1.00].
    condition:
      $e
    

##### Example 3

Default values are not ignored so a lot of times the top value will be 0 (adjust the second arg accordingly).
    
    
    events:
     $e.user.userid = $userid
    match:
     $userid over 5m
    outcome:
      $p1 = window.most_common_number($e.file.size, 1) // yields [0] if the event file size values in the match window are [0, 0, NULL, 123].
    condition:
      $e
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
