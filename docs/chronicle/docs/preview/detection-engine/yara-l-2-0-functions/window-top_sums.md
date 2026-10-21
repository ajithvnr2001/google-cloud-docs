---
url: https://docs.cloud.google.com/chronicle/docs/preview/detection-engine/yara-l-2-0-functions/window-top_sums/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T17:26:15.959644+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/preview/detection-engine/yara-l-2-0-functions/window-top_sums/




Stay organized with collections  Save and categorize content based on your preferences. 

### window.top_sums

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules) [ Search ](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)
    
    
    window.top_sums(strings, weights, how_many_to_retrieve)
    

#### Description

Return the specified number of most common strings and corresponding weight in the input values in string:weight format. Default values are not ignored.

#### Param data types

`STRING`, `INT`, `INT`

#### Return type

`ARRAY_STRINGS`

#### Code samples

##### Example 1

This example shows the top two window sizes.
    
    
    events:
     $e.user.userid = $userid
    match:
     $userid over 5m
    outcome:
      $p1 = window.top_sums($e.principal.hostname, $e.file.size, 2) // yields ["a:100", "c:20"] if the event hostname values in the match window are ["a", "b", "b", "c"] and file sizes are [100, 5, 10, 20].
    condition:
      $e and arrays.contains($p1, "apple")
    

##### Example 2

This example shows handling when window size is more than array size.
    
    
    events:
     $e.user.userid = $userid
    match:
     $userid over 5m
    outcome:
      $p1 = window.top_sums($e.principal.hostname, $e.file.size, 100) // yields ["a:100", "c:20", "b:15"] if the event hostname values in the match window are ["a", "b", "b", "c"] and file sizes are [100, 5, 10, 20].
    condition:
      $e and arrays.contains($p1, "apple")
    

##### Example 3

This example shows handling when some input strings have same weight.
    
    
    events:
     $e.user.userid = $userid
    match:
     $userid over 5m
    outcome:
      $p1 = window.top_sums($e.principal.hostname, $e.file.size, 3) // yields ["a:20", "c:20", "b:15"] if the event hostname values in the match window are ["a", "b", "b", "c"] and file sizes are [20, 5, 10, 20].
    condition:
      $e and arrays.contains($p1, "apple")
    

##### Example 4

This example shows handling when some input strings have zero weight.
    
    
    events:
     $e.user.userid = $userid
    match:
     $userid over 5m
    outcome:
      $p1 = window.top_sums($e.principal.hostname, $e.file.size, 3) // yields ["c:21", "a:20"] if the event hostname values in the match window are ["a", "b", "b", "c"] and file sizes are [20, 0, 0, 21].
    condition:
      $e and arrays.contains($p1, "apple")
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
