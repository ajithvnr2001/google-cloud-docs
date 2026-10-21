---
url: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/math-pow/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:59:07.345451+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/math-pow/




Stay organized with collections  Save and categorize content based on your preferences. 

### math.pow

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules) [ Search ](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)
    
    
    math.pow(base, exponent)
    

#### Description

Returns the value of the first arg raised to the power of the second arg. Returns 0 in case of overflow.

#### Param data types

base: `INT|FLOAT` exponent: `INT|FLOAT`

#### Return type

`FLOAT`

#### Code samples

##### Example 1

This example shows an integer case.
    
    
    math.pow(2, 2) // 4.00
    

##### Example 2

This example shows a fraction base case.
    
    
    math.pow(2.200000, 3) // 10.648
    

##### Example 3

This example shows a fraction base and power case.
    
    
    math.pow(2.200000, 1.200000) // 2.575771
    

##### Example 4

This example shows a negative power case.
    
    
    math.pow(3, 0-3) // 0.037037
    

##### Example 5

This example shows a fraction power case.
    
    
    math.pow(3, 0-1.200000) // 0.267581
    

##### Example 6

This example shows a negative base case.
    
    
    math.pow(0-3, 0-3) // -0.037037
    

##### Example 7

This example shows a zero base case.
    
    
    math.pow(0, 3) // 0
    

##### Example 8

This example shows a zero power case.
    
    
    math.pow(9223372036854775807, 0) // 1
    

##### Example 9

This example shows a large base case.
    
    
    math.pow(9223372036854775807, 1.200000) // 57262152889751593549824
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
