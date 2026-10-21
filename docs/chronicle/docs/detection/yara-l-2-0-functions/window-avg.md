---
url: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/window-avg/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T03:54:50.828543+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/window-avg/




Stay organized with collections  Save and categorize content based on your preferences. 

### window.avg

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules)
    
    
    window.avg(numeric_values [, should_ignore_zero_values])
    

#### Description

Returns the average of the input values (which can be Integers or Floats). Setting the optional second argument to true ignores zero values.

#### Param data types

`INT|FLOAT`

#### Return type

`FLOAT`

#### Code samples

##### Example 1

This example shows the integer average.
    
    
    // This rule sets the outcome $size_mode to the average
    // file size in the 5 minute match window.
    events:
     $e.user.userid = $userid
    match:
     $userid over 5m
    outcome:
      $size_mode = window.avg($e.file.size) // yields 2.5 if the event file size values in the match window are 1, 2, 3 and 4
    

##### Example 2

This example shows the float average.
    
    
    events:
     $e.user.userid = $userid
    match:
     $userid over 5m
    outcome:
      $size_mode = window.avg($e.file.size) // yields 1.75 if the event file size values in the match window are 1.1 and 2.4
    

##### Example 3

Negative input average
    
    
    events:
     $e.user.userid = $userid
    match:
     $userid over 5m
    outcome:
      $size_mode = window.avg($e.file.size) // yields 0.6 if the event file size values in the match window are -1.1, 1.1, 0.0 and 2.4
    

##### Example 4

0 returns 0
    
    
    events:
     $e.user.userid = $userid
    match:
     $userid over 5m
    outcome:
      $size_mode = window.avg($e.file.size) // yields 0 if the event file size values in the match window is 0
    

##### Example 5

Ignoring 0 values
    
    
    events:
     $e.user.userid = $userid
    match:
     $userid over 5m
    outcome:
      $size_mode = window.avg($e.file.size, true) // yields 394 if the event file size values in the match window are 0, 0, 0 and 394
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
