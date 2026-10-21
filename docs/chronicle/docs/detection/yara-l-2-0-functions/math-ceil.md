---
url: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/math-ceil/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:41:20.634012+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/math-ceil/




Stay organized with collections  Save and categorize content based on your preferences. 

### math.ceil

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules) [ Search ](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)
    
    
    math.ceil(number)
    

#### Description

Returns the smallest integer that is not less than the given number (rounding up). Will return 0 if the input is null or too big to fit in an int64.

#### Param data types

`FLOAT`

#### Return type

`INT`

#### Code samples

This section contains examples of using `math.ceil`.

##### Example 1

This example returns the ceil of a whole number.
    
    
    math.ceil(2.000000) = 2
    

##### Example 2

This example returns the ceil of a negative number.
    
    
    math.ceil(0-1.200000) = -1
    

##### Example 3

This example returns 0 as the ceil of a number that is too big for a 64 bit integer.
    
    
    math.ceil(184467440737095516160.0) = 0
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
