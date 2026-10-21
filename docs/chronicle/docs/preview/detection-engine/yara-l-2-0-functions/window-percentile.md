---
url: https://docs.cloud.google.com/chronicle/docs/preview/detection-engine/yara-l-2-0-functions/window-percentile/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:54:30.003373+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/preview/detection-engine/yara-l-2-0-functions/window-percentile/




Stay organized with collections  Save and categorize content based on your preferences. 

### window.percentile

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules) [ Search ](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)
    
    
    window.percentile(values, percentile)
    

#### Description

This function returns the specified percentile of the input values.

The percentile is a number between 0 and 100.

#### Param data types

`INT|FLOAT`, `INT`

#### Return type

`FLOAT`

#### Code samples

This example returns the median (50th percentile) of the values in the match window.
    
    
    // This rule creates a detection when the median file size in 5 minutes for a user is over a threshold.
    events:
     $e.user.userid = $userid
    match:
     $userid over 5m
    outcome:
      $p50 = window.percentile($e.file.size, 50) // yields 2.0 if the event file size values in the match window are 1, 2, and 3.
    condition:
      $e and $p50 > 10
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
