---
url: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/window-last/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T18:58:06.982573+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/window-last/




Stay organized with collections  Save and categorize content based on your preferences. 

### window.last

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules)
    
    
    window.last(values_to_sort_by, values_to_return)
    

#### Description

This aggregation function returns a string value derived from an event with the highest correlated int value in the match window. An example use case is getting the userid from the event with the lowest timestamp in the match window (highest timestamp).

#### Param data types

`INT`, `STRING`

#### Return type

`STRING`

#### Code samples

Get a string value derived from an event with the highest correlated int value in the match window.
    
    
    rule test_windows_last {
    
    // This rule sets the outcome $last_event to the highest correlated int value
    // in the 5 minute match window.
    
      meta:
    
      events:
        $e.principal.user.userid = $userid
    
      match:
        $userid over 5m
    
      outcome:
        $last_event = window.last($e.metadata.event_timestamp.seconds, 
        $e.metadata.vendor_name)
        // yields v3 if the events in the match window are 1, 2 and 3 and 
        // corresponding values v1, v2, and v3.
    
      condition:
        $e
    }
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
