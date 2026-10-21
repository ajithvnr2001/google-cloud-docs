---
url: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/strings-trim/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:02:09.215936+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/strings-trim/




Stay organized with collections  Save and categorize content based on your preferences. 

### strings.trim

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules) [ Search ](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)
    
    
    strings.trim(string_to_trim, cutset)
    

#### Description

Trims leading and trailing white spaces from a given string. Also, remove unwanted characters (specified by the cutset argument) from the input string.

#### Param data types

`STRING`, `STRING`

#### Return type

`STRING`

#### Code samples

The following are example use cases.

##### Example 1

In the following example, the same string is passed as the input string and the cutset, which results in an empty string.
    
    
    strings.trim("str", "str") // ""
    

##### Example 2

In the following example, an empty string is passed as the cutset, which results in the original string str because there are no characters specified in the cutset to remove.
    
    
    strings.trim("str", "") = "str"
    

##### Example 3

In the following example, the function yields an empty string because the input string is already empty and there are no characters to remove.
    
    
    strings.trim("", "str") = ""
    

##### Example 4

In the following example, the function yields str because the trim function removes the following:

  * trailing whitespace in "a aastraa aa "
  * the characters specified in the cutset (space, a)


    
    
    strings.trim("a aastraa aa ", " a") = "str"
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
