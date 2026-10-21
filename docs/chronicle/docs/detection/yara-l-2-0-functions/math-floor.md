---
url: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/math-floor/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:05:03.917215+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/math-floor/




Stay organized with collections  Save and categorize content based on your preferences. 

### math.floor

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules) [ Search ](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)
    
    
    math.floor(float_val)
    

#### Description

Returns the largest integer value that is not greater than the supplied value (rounding down). Returns 0 if the input is null or too large to fit into an int64.

#### Param data types

`FLOAT`

#### Return type

`INT`

#### Code samples

##### Example 1

This example shows a positive number case.
    
    
    math.floor(1.234568) = 1
    

##### Example 2

This example shows a negative number case.
    
    
    math.floor(0-1.234568) = -2
    

##### Example 3

This example shows a zero case.
    
    
    math.floor(0.000000) = 0
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
