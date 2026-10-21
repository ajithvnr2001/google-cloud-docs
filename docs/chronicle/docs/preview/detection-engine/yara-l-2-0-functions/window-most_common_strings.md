---
url: https://docs.cloud.google.com/chronicle/docs/preview/detection-engine/yara-l-2-0-functions/window-most_common_strings/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T02:02:26.107913+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/preview/detection-engine/yara-l-2-0-functions/window-most_common_strings/




Stay organized with collections  Save and categorize content based on your preferences. 

### window.most_common_strings

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules) [ Search ](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)
    
    
    window.most_common_strings(strings, how_many_to_retrieve)
    

#### Description

Returns the specified number of most common strings in the input values.

#### Param data types

`STRING`, `INT`

#### Return type

`ARRAY_STRINGS`

#### Code samples

##### Example 1

This example shows the top two most common hostnames in five minutes.
    
    
    // This rule creates a detection when the most common hostname in 5 minutes for a user matches.
    events:
     $e.user.userid = $userid
    match:
     $userid over 5m
    outcome:
      $p1 = window.most_common_strings($e.principal.hostname, 1) // yields ["pear"] if the event hostname values in the match window are ["apple", "apple", "pear", "pear", "pear", "banana"].
    condition:
      $e and arrays.contains($p1, "apple")
    

##### Example 2

This example shows that the window size is more than the array size.
    
    
    events:
     $e.user.userid = $userid
    match:
     $userid over 5m
    outcome:
      $p1 = window.most_common_strings($e.principal.hostname, 100) // yields ["pear", "apple", "banana"] if the event hostname values in the match window are ["apple", "apple", "pear", "pear", "pear", "banana"].
    condition:
      $e and arrays.contains($p1, "apple")
    

##### Example 3

This example shows the default values are not ignored so most of times the top value will be 0 (adjust the second arg accordingly).
    
    
    events:
     $e.user.userid = $userid
    match:
     $userid over 5m
    outcome:
      $p1 = window.most_common_strings($e.principal.hostname, 1) // yields [""] if the event hostname values in the match window are ["", "", NULL, "banana"].
    condition:
      $e and arrays.contains($p1, "apple")
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
