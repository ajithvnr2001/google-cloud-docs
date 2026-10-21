---
url: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/window-mode/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T11:12:08.617178+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/window-mode/




Stay organized with collections  Save and categorize content based on your preferences. 

### window.mode

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules)
    
    
    window.mode(values)
    

#### Description

Return the mode of the input values. In case of multiple possible mode values, only one of those values will be non-deterministically chosen as the return value.

#### Param data types

`INT|FLOAT|STRING`

#### Return type

`STRING`

#### Code samples

##### Example 1

Get mode of the values in the match window.
    
    
    // This rule sets the outcome $size_mode to the most frequently occurring
    // file size in the 5 minute match window.
    events:
     $e.user.userid = $userid
    match:
     $userid over 5m
    outcome:
      $size_mode = window.mode($e.file.size) // yields 1.6 if the event file size values in the match window are 1.6, 2, and 1.6
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
