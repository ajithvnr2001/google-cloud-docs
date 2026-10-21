---
url: https://docs.cloud.google.com/chronicle/docs/preview/detection-engine/yara-l-2-0-functions/window-least_common_strings/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:32:48.321877+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/preview/detection-engine/yara-l-2-0-functions/window-least_common_strings/




Stay organized with collections  Save and categorize content based on your preferences. 

### window.least_common_strings

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules) [ Search ](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)
    
    
    window.least_common_strings(string_val, how_many_to_return)
    

#### Description

Returns a specified number of least commonly occurring string elements in the input array.

#### Param data types

`STRING`, `INT`

#### Return type

`ARRAY_STRINGS`

#### Code samples

##### Example 1

This example shows the two least common hostnames in five minutes.
    
    
    // This rule creates a detection when the least common hostname in 5 minutes for a user matches.
    events:
     $e.user.userid = $userid
    match:
     $userid over 5m
    outcome:
      $p1 = window.least_common_strings($e.principal.hostname, 1) // yields ["banana"] if the event hostname values in the match window are ["apple", "apple", "pear", "pear", "pear", "banana"].
    condition:
      $e and arrays.contains($p1, "banana")
    

##### Example 2

This example shows that the number of values to return is more than the number of distinct values.
    
    
    events:
     $e.user.userid = $userid
    match:
     $userid over 5m
    outcome:
      $p1 = window.least_common_strings($e.principal.hostname, 100) // yields ["banana", "apple", "pear"] if the event hostname values in the match window are ["apple", "apple", "pear", "pear", "pear", "banana"].
    condition:
      $e and arrays.contains($p1, "banana")
    

##### Example 3

This example shows that default zero-values are ignored.
    
    
    events:
     $e.user.userid = $userid
    match:
     $userid over 5m
    outcome:
      $p1 = window.least_common_strings($e.principal.hostname, 1) // yields [""] if the event hostname values in the match window are ["", "banana"].
    condition:
      $e and arrays.contains($p1, "banana")
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
