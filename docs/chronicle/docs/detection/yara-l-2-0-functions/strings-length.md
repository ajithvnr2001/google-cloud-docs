---
url: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/strings-length/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T11:48:12.695335+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/strings-length/




Stay organized with collections  Save and categorize content based on your preferences. 

### strings.length

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules) [ Search ](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)
    
    
    strings.length(string_value)
    

#### Description

Returns the number of characters in the input string.

#### Param data types

`STRING`

#### Return type

`INT`

#### Code samples

##### Example 1

The following is an example with a string test.
    
    
    strings.length("str") = 3
    

##### Example 2

The following is an example with an empty string as input.
    
    
    strings.length("") = 0
    

##### Example 3

The following is an example with a special char string.
    
    
    strings.length("!@#$%^&*()-_") = 12
    

##### Example 4

The following is an example with a string with spaces.
    
    
    strings.length("This is a test string") = 21
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
