---
url: https://docs.cloud.google.com/chronicle/docs/preview/detection-engine/yara-l-2-0-functions/arrays-filter_regex_contains/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T09:15:28.657694+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/preview/detection-engine/yara-l-2-0-functions/arrays-filter_regex_contains/




Stay organized with collections  Save and categorize content based on your preferences. 

### arrays.filter_regex_contains

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules) [ Search ](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)
    
    
    arrays.filter_regex_contains(array_of_strings, regex[, inverse=false])
    

#### Description

Filters the contents of the provided array to include only elements that contain the provided regular expression if the inverse is false or exclude elements if the inverse is true.

#### Param data types

`ARRAY_STRINGS`, `STRING`, `BOOL`

#### Return type

`ARRAY_STRINGS`

#### Code samples

Here are some examples of how to use the function:

##### Example 1

This example filters out anything that does not end in "inky".
    
    
    arrays.filter_regex_contains(["inky", "pinky", "blinky", "clyde"], ".*inky$", false) = ["inky", "pinky", "blinky"]
    

##### Example 2

This example filters out anything that does end in "inky".
    
    
    arrays.filter_regex_contains(["inky", "pinky", "blinky", "clyde"], ".*inky$", true) = ["clyde"]
    

##### Example 3

This example filters out everything.
    
    
    arrays.filter_regex_contains(["inky", "pinky", "blinky", "clyde"], "NOT_PRESENT", false) = [""]
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
