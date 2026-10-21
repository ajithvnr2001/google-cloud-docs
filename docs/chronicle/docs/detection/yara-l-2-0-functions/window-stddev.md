---
url: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/window-stddev/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:37:33.972847+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/window-stddev/




Stay organized with collections  Save and categorize content based on your preferences. 

### window.stddev

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules)
    
    
    window.stddev(numeric_values)
    

#### Description

Returns the standard deviation of input values in a match window.

#### Param data types

`INT|FLOAT`

#### Return type

`FLOAT`

#### Code samples

##### Example 1

This example returns the standard deviation of integers in a match window.
    
    
    // This rule creates a detection when the file size stddev in 5 minutes for a user is over a threshold.
    events:
     $e.user.userid = $userid
    match:
     $userid over 5m
    outcome:
      $p1 = window.stddev($e.file.size) // yields 4.0 if the event file size values in the match window are [10, 14, 18].
    condition:
      $e and #p1 > 2
    

##### Example 2

This example returns the standard deviation of floats in a match window.
    
    
    events:
     $e.user.userid = $userid
    match:
     $userid over 5m
    outcome:
      $p1 = window.stddev($e.file.size) // yields 4.488686 if the event file size values in the match window are [10.00, 14.80, 18.97].
    condition:
      $e and #p1 > 2
    

##### Example 3

This example returns the standard deviation in a match window that contains negative numbers.
    
    
    events:
     $e.user.userid = $userid
    match:
     $userid over 5m
    outcome:
      $p1 = window.stddev($e.file.size) // yields 48.644972 if the event file size values in the match window are [-1, -56, -98].
    condition:
      $e and #p1 > 2
    

##### Example 4

This example returns with zero standard deviation when all values in the match window are the same.
    
    
    events:
     $e.user.userid = $userid
    match:
     $userid over 5m
    outcome:
      $p1 = window.stddev($e.file.size) // yields 0.000000 if the event file size values in the match window are [1, 1, 1].
    condition:
      $e and #p1 > 2
    

##### Example 5

This example returns the standard deviation of a match window containing positive and negative numbers.
    
    
    events:
     $e.user.userid = $userid
    match:
     $userid over 5m
    outcome:
      $p1 = window.stddev($e.file.size) // yields 1.000000 if the event file size values in the match window are [1, 0, -1].
    condition:
      $e and #p1 > 10
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
