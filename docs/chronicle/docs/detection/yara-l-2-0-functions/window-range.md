---
url: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/window-range/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T10:23:43.588636+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/window-range/




Stay organized with collections  Save and categorize content based on your preferences. 

### window.range

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules) [ Search ](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)
    
    
    window.range(numeric_values, optional should_ignore_zero_values)
    

#### Description

Returns the range of the values input values found (min, max inclusive). Each value can be an integer or a floating point. Setting the optional second argument to true ignores zero values.

#### Param data types

`INT|FLOAT`, `BOOL`

#### Return type

`ARRAY_FLOATS`

#### Code samples

The following code samples illustrate some of the ways you might use the `window.range` function.

##### Example: minimum and maximum integer

This example shows the minimum and maximum integer value.
    
    
    window.range([1, 2, 3, 4], false) = [1.000000, 4.000000]
    

##### Example: minimum and maximum floating point

This example shows the minimum and maximum floating point value.
    
    
    window.range([1.100000, 39.400000, 2.400000], false) = [1.100000, 39.400000]
    

##### Example: minimum and maximum negative integer

This example shows the minimum and maximum negative integer value.
    
    
    window.range([-1.100000, 1.100000, 0.000000, 2.400000], false) = [-1.100000, 2.400000]
    

##### Example: ignored 0 value

This example shows how 0 values are ignored when you set the second parameter.
    
    
    window.range([0, 0, 0, 394, 1], true) = [1.000000, 394.000000]
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
