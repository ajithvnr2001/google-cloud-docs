---
url: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/strings-rtrim/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T13:36:29.236202+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/strings-rtrim/




Stay organized with collections  Save and categorize content based on your preferences. 

### strings.rtrim

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules) [ Search ](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)
    
    
    strings.rtrim(string_to_trim, cutset)
    

#### Description

Trims trailing white spaces from a given string. Removes trailing characters that are present in that cutset.

#### Param data types

`STRING`, `STRING`

#### Return type

`STRING`

#### Code samples

The following are example use cases.

##### Example 1

The following example passes the same string as the first and second argument.
    
    
    strings.rtrim("str", "str") = ""
    

##### Example 2

The following example passes an empty string as the second argument.
    
    
    strings.rtrim("str", "") = "str"
    

##### Example 3

The following example passes an empty string as the first argument and a non-empty string as the second argument.
    
    
    strings.rtrim("", "str") = ""
    

##### Example 4

The following example passes a string containing white spaces as the first argument and a non-empty string as the second argument.
    
    
    strings.rtrim("a aastraa aa ", " a") = "a aasstr"
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
