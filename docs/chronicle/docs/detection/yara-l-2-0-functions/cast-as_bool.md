---
url: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/cast-as_bool/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:20:45.943723+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/cast-as_bool/




Stay organized with collections  Save and categorize content based on your preferences. 

### cast.as_bool

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules) [ Search ](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)
    
    
    cast.as_bool(string_or_int)
    

#### Description

Function converts an int or string value into a bool value. Function calls with values that cannot be casted will return FALSE. Returns TRUE only for integer 1 and case insensitive string 'true'.

#### Param data types

`INT|STRING`

#### Return type

`BOOL`

#### Code samples

##### Example 1

This example shows how to cast a non-boolean string
    
    
    cast.as_bool("123") = false
    

##### Example 2

Truthy integer (1)
    
    
    cast.as_bool(1) = true
    

##### Example 3

Truthy string
    
    
    cast.as_bool("true") = true
    

##### Example 4

Capital truthy string
    
    
    cast.as_bool("TRUE") = true
    

##### Example 5

Negative integer
    
    
    cast.as_bool(0-1) = false
    

##### Example 6

False integer (0)
    
    
    cast.as_bool(0) = false
    

##### Example 7

empty string
    
    
    cast.as_bool("") = false
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
