---
url: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/arrays-index_to_int/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:38:12.879644+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/arrays-index_to_int/




Stay organized with collections  Save and categorize content based on your preferences. 

### arrays.index_to_int

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules) [ Search ](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)
    
    
    arrays.index_to_int(array_of_inputs, index)
    

#### Description

Returns the value at a given index in an array as an integer.

The index is an integer value which represents the position of an element in the array. By default, the first element of an array has an index of 0, and the last element has an index of n-1, where n is the size of the array. Negative indexing allows accessing array elements relative to the end of the array. For example, an index of -1 refers to the last element in the array and an index of -2 refers to the second to last element in the array.

#### Param data types

`ARRAY_STRINGS|ARRAY_INTS|ARRAY_FLOATS`, `INT`

#### Return type

`INT`

#### Code samples

##### Example 1

This function call returns 0 when the value at the index is a non-numeric string.
    
    
    arrays.index_to_int(["str0", "str1", "str2"], 1) = 0
    

##### Example 2

This function returns the element at index -1.
    
    
    arrays.index_to_int(["44", "11", "22", "33"], 0-1) = 33
    

##### Example 3

Returns 0 for the out-of-bounds element.
    
    
    arrays.index_to_int(["44", "11", "22", "33"], 5) = 0
    

##### Example 4

This function fetches the element from the float array at index 1.
    
    
    arrays.index_to_int([1.100000, 1.200000, 1.300000], 1) = 1
    

##### Example 5

This function fetches the element from the int array at index 0.
    
    
    arrays.index_to_int([1, 2, 3], 0) = 1
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
