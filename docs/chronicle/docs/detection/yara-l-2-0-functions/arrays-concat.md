---
url: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/arrays-concat/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:36:56.799687+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/arrays-concat/




Stay organized with collections  Save and categorize content based on your preferences. 

### arrays.concat

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules) [ Search ](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)
    
    
    arrays.concat(string_array, string_array)
    

#### Description

Returns a new string array by copying elements from original string arrays.

#### Param data types

`ARRAY_STRINGS`, `ARRAY_STRINGS`

#### Return type

`ARRAY_STRINGS`

#### Code samples

##### Example 1

The following example concatenates two different string arrays.
    
    
    arrays.concat(["test1", "test2"], ["test3"]) = ["test1", "test2", "test3"]
    

##### Example 2

The following example concatenates arrays with empty string.
    
    
    arrays.concat([""], [""]) = ["", ""]
    

##### Example 3

The following example concatenates empty arrays.
    
    
    arrays.concat([], []) = []
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
