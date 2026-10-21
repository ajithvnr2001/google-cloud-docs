---
url: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/arrays-index_to_float/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:07:06.428364+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/arrays-index_to_float/




Stay organized with collections  Save and categorize content based on your preferences. 

### arrays.index_to_float

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules) [ Search ](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)
    
    
    arrays.index_to_float(array, index)
    

#### Description

Returns the element at the given index of an array. The element at that index is returned as a float.

The index is an integer value which represents the position of an element in the array. By default, the first element of an array has an index of 0, and the last element has an index of n-1, where n is the size of the array. Negative indexing allows accessing array elements relative to the end of the array. For example, an index of -1 refers to the last element in the array and an index of -2 refers to the second to last element in the array.

#### Param data types

`ARRAY_STRINGS|ARRAY_INTS|ARRAY_FLOATS`, `INT`

#### Return type

`FLOAT`

#### Code samples

##### Example 1

The following example fetches an element at index 1 from an array of floats.
    
    
    arrays.index_to_float([1.2, 2.1, 3.5, 4.6], 1) // 2.1
    

##### Example 2

The following example fetches an element at index -1 from an array of floats.
    
    
    arrays.index_to_float([1.2, 2.1, 3.5, 4.6], 0-1) // 4.6
    

##### Example 3

The following example fetches an element for an index greater than the size of the array.
    
    
    arrays.index_to_float([1.2, 2.1, 3.5, 4.6], 6) // 0.0
    

##### Example 4

The following example fetches an element from an empty array.
    
    
    arrays.index_to_float([], 0) // 0.0
    

##### Example 5

The following example fetches an element at index 1 from a string array.
    
    
    arrays.index_to_float(["1.2", "3.3", "2.4"], 1) // 3.3
    

##### Example 6

The following example fetches an element at index 2 from an array of integers.
    
    
    arrays.index_to_float([1, 3, 2], 2) // 2.0
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
