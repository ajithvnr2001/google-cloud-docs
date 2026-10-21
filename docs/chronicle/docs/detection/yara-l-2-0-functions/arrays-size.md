---
url: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/arrays-size/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T13:53:31.926109+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/arrays-size/




Stay organized with collections  Save and categorize content based on your preferences. 

### arrays.size

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules) [ Search ](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)
    
    
    arrays.size( array )
    

#### Description

Returns the size of the array. Returns 0 for an empty array.

#### Param data types

`ARRAY_STRINGS|ARRAY_INTS|ARRAY_FLOATS`

#### Return type

`INT`

#### Code samples

##### Example 1

This example uses a string array that contains two elements.
    
    
    arrays.size(["test1", "test2"]) = 2
    

##### Example 2

This example uses an int array that contains 3 elements.
    
    
    arrays.size([1, 2, 3]) = 3
    

##### Example 3

This example uses a float array thats contains 1 elements
    
    
    arrays.size([1.200000]) = 1
    

##### Example 4

This example uses an empty array.
    
    
    arrays.size([]) = 0
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
