---
url: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/window-median/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T03:00:45.277386+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/window-median/




Stay organized with collections  Save and categorize content based on your preferences. 

### window.median

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules)
    
    
    window.median(numeric_values, should_ignore_zero_values)
    

#### Description

Return the median of the input values. If there are 2 median values, only 1 will be non-deterministically chosen as the return value.

#### Param data types

`INT|FLOAT`, `BOOL`

#### Return type

`FLOAT`

#### Code samples

##### Example 1

This example returns the median when the input values aren't zero.
    
    
    rule median_file_size {
        meta:
        events:
          $e.metadata.event_type = "FILE_COPY"
            $userid = $e.principal.user.userid
        match:
          $userid over 1h
        outcome:
          $median_file_size = window.median($e.principal.file.size) // returns 2 if the file sizes in the match window are [1, 2, 3]
      condition:
          $e
    }
    

##### Example 2

This example returns the median when the input includes some zero values that shouldn't be ignored.
    
    
    rule median_file_size {
        meta:
        events:
          $e.metadata.event_type = "FILE_COPY"
            $userid = $e.principal.user.userid
        match:
          $userid over 1h
        outcome:
          $median_file_size = window.median($e.principal.file.size) // returns 1 if the file sizes in the match window are [0,0, 1, 2, 3]
      condition:
          $e
    }
    

##### Example 3

This example returns the median when the input includes some zero values which should be ignored.
    
    
    rule median_file_size {
        meta:
        events:
          $e.metadata.event_type = "FILE_COPY"
            $userid = $e.principal.user.userid
        match:
          $userid over 1h
        outcome:
          $median_file_size = window.median($e.principal.file.size, true) // returns 2 if the file sizes in the match window are [0,0, 1, 2, 3]
      condition:
          $e
    }
    

##### Example 4

This example returns the median when the input includes all zero values which should be ignored.
    
    
    rule median_file_size {
        meta:
        events:
          $e.metadata.event_type = "FILE_COPY"
            $userid = $e.principal.user.userid
        match:
          $userid over 1h
        outcome:
          $median_file_size = window.median($e.principal.file.size) // returns 0 if the file sizes in the match window are [0,0]
      condition:
          $e
    }
    

##### Example 5

This example shows that, when there are multiple medians, only one median is returned.
    
    
    rule median_file_size {
        meta:
        events:
          $e.metadata.event_type = "FILE_COPY"
            $userid = $e.principal.user.userid
        match:
          $userid over 1h
        outcome:
          $median_file_size = window.median($e.principal.file.size) // returns 1 if the file sizes in the match window are [1, 2, 3, 4]
      condition:
          $e
    }
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
