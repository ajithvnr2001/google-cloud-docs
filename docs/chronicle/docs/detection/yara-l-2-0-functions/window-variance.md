---
url: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/window-variance/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:52:50.253813+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/window-variance/




Stay organized with collections  Save and categorize content based on your preferences. 

### window.variance

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules)
    
    
    window.variance(values)
    

#### Description

This function returns the specified variance of the input values.

#### Param data types

`INT|FLOAT`

#### Return type

`FLOAT`

#### Code samples

##### Example 1

This example returns the variance of all integers.
    
    
    // This rule creates a detection when the file size variance in 5 minutes for a user is over a threshold.
    events:
     $e.user.userid = $userid
    match:
     $userid over 5m
    outcome:
      $p1 = window.variance($e.file.size) // yields 16 if the event file size values in the match window are [10, 14, 18].
    condition:
      $e and #p1 > 10
    

##### Example 2

This example returns the variance of all floats.
    
    
    events:
     $e.user.userid = $userid
    match:
     $userid over 5m
    outcome:
      $p1 = window.variance($e.file.size) // yields 20.148300 if the event file size values in the match window are [10.00, 14.80, 18.97].
    condition:
      $e and #p1 > 10
    

##### Example 3

This example returns the variance of negative numbers.
    
    
    events:
     $e.user.userid = $userid
    match:
     $userid over 5m
    outcome:
      $p1 = window.variance($e.file.size) // yields 2366.333333 if the event file size values in the match window are [-1, -56, -98].
    condition:
      $e and #p1 > 10
    

##### Example 4

This example returns a small variance value.
    
    
    events:
     $e.user.userid = $userid
    match:
     $userid over 5m
    outcome:
      $p1 = window.variance($e.file.size) // yields 0.000000 if the event file size values in the match window are [0.000000, 0.000000, 0.000100].
    condition:
      $e and #p1 > 10
    

##### Example 5

This example returns a zero variance.
    
    
    events:
     $e.user.userid = $userid
    match:
     $userid over 5m
    outcome:
      $p1 = window.variance($e.file.size) // yields 0.000000 if the event file size values in the match window are [1, 1, 1].
    condition:
      $e and #p1 > 10
    

##### Example 6

This example returns the variance of positive and negative numbers.
    
    
    events:
     $e.user.userid = $userid
    match:
     $userid over 5m
    outcome:
      $p1 = window.variance($e.file.size) // yields 1.000000 if the event file size values in the match window are [1, 0, -1].
    condition:
      $e and #p1 > 10
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
