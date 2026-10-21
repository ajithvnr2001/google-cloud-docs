---
url: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/math-sqrt/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:27:46.088199+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/math-sqrt/




Stay organized with collections  Save and categorize content based on your preferences. 

### math.sqrt

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules) [ Search ](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)
    
    
    math.sqrt(number)
    

#### Description

Returns the square root of the given number. Returns 0 in case of negative numbers.

#### Param data types

`INT|FLOAT`

#### Return type

`FLOAT`

#### Code samples

##### Example 1

This example returns the square root of an int argument.
    
    
    math.sqrt(3) = 1.732051
    

##### Example 2

This example returns the square root of a negative int argument.
    
    
    math.sqrt(-3) = 0.000000
    

##### Example 3

This example returns the square root of zero argument.
    
    
    math.sqrt(0) = 0.000000
    

##### Example 4

This example returns the square root of a float argument.
    
    
    math.sqrt(9.223372) = 3.037000
    

##### Example 5

This example returns the square root of a negative float argument.
    
    
    math.sqrt(0-1.200000) = 0.000000
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
