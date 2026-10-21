---
url: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/strings-ltrim/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:06:44.789609+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/strings-ltrim/




Stay organized with collections  Save and categorize content based on your preferences. 

### strings.ltrim

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules) [ Search ](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)
    
    
    strings.ltrim(string_to_trim, cutset)
    

#### Description

Trims leading white spaces from a given string. This function removes leading characters present in that cutset.

#### Param data types

`STRING`, `STRING`

#### Return type

`STRING`

#### Code samples

The following are example use cases.

##### Example 1

This example uses the same first and second argument.
    
    
    strings.ltrim("str", "str") = ""
    

##### Example 2

This example uses an empty string as the second argument.
    
    
    strings.ltrim("str", "") = "str"
    

##### Example 3

This example uses an empty string as the first argument, and a string as the second argument.
    
    
    strings.ltrim("", "str") = ""
    

##### Example 4

This example uses strings that contain white spaces, and a string as the second argument.
    
    
    strings.ltrim("a aastraa aa ", " a") = "straa aa "
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
