---
url: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/math-is_increasing/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:49:06.525731+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/math-is_increasing/




Stay organized with collections  Save and categorize content based on your preferences. 

### math.is_increasing

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules) [ Search ](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)
    
    
    math.is_increasing(num1, num2, num3)
    

#### Description

Takes a list of numeric values (integers or doubles) and returns `True` if the values are in ascending order, and `False` otherwise.

#### Param data types

`INT|FLOAT`, `INT|FLOAT`, `INT|FLOAT`

#### Return type

`BOOL`

#### Code samples

##### Example 1

This example includes timestamp-like values in seconds.
    
    
    math.is_increasing(1716769112, 1716769113, 1716769114) = true
    

##### Example 2

This example includes one negative double, one zero INT64, and one positive INT64 values.
    
    
    math.is_increasing(-1.200000, 0, 3) = true
    

##### Example 3

This example includes one negative double, one zero INT64, and one negative INT64 values.
    
    
    math.is_increasing(0-1.200000, 0, 0-3) = false
    

##### Example 4

This example includes two negative doubles and one zero INT64 value.
    
    
    math.is_increasing(0-1.200000, 0-1.50000, 0) = false
    

##### Example 5

This example includes one negative double and two values that are the same.
    
    
    math.is_increasing(0-1.200000, 0, 0) = false
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
