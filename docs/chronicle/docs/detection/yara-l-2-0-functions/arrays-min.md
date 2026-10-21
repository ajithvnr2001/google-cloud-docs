---
url: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/arrays-min/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T14:08:10.971513+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/arrays-min/




Stay organized with collections  Save and categorize content based on your preferences. 

### arrays.min

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules) [ Search ](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)
    
    
    arrays.min(array_of_ints_or_floats[, ignore_zeros=false])
    

#### Description

Returns the smallest element in an array or zero if the array is empty. If the second, optional argument is set to true, elements equal to zero are ignored.

#### Param data types

`ARRAY_INTS|ARRAY_FLOATS`, `BOOL`

#### Return type

`FLOAT`

#### Code samples

Here are some examples of how to use the function:

##### Example 1

This example returns the smallest element in an array of integers.
    
    
    arrays.min([10, 20]) = 10.000000
    

##### Example 2

This example returns the smallest element in an array of floats.
    
    
    arrays.min([10.000000, 20.000000]) = 10.000000
    

##### Example 3

This example returns the smallest element in an array of floats, while ignoring the zeroes.
    
    
    arrays.min([10.000000, 20.000000, 0.0], true) = 10.000000
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
