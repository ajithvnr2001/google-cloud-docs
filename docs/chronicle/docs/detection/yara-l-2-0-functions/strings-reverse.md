---
url: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/strings-reverse/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T07:54:12.520938+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/strings-reverse/




Stay organized with collections  Save and categorize content based on your preferences. 

### strings.reverse

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules) [ Search ](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)
    
    
    strings.reverse(STRING)
    

#### Description

Returns a string that is the reverse of the input string.

#### Param data types

`STRING`

#### Return type

`STRING`

#### Code samples

##### Example 1

The following example passes a short string.
    
    
    strings.reverse("str") = "rts"  // The function returns 'rts'.
    

##### Example 2

The following example passes an empty string.
    
    
    strings.reverse("") = ""
    

##### Example 3

The following example passes a palindrome.
    
    
    strings.reverse("tacocat") = "tacocat"
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
