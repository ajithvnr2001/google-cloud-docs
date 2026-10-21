---
url: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/strings-split/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T03:17:40.433244+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/strings-split/




Stay organized with collections  Save and categorize content based on your preferences. 

### strings.split

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules) [ Search ](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)
    
    
    strings.split(string, delimiter)
    

#### Description

Splits string value using the delimiter argument. The default delimiter is a comma (`,`).

#### Param data types

`STRING`, `STRING`

#### Return type

`ARRAY_STRINGS`

#### Code samples

The following code samples illustrate some of the ways you might use the `strings.split` function.

##### Example: split string with default

The following example splits the string using the default delimiter, which is a comma.
    
    
    strings.split("a,b,c,d") = ["a", "b", "c", "d"]
    

##### Example: split string with colon

The following example splits the string at each colon (`:`).
    
    
    strings.split("a:b:c:d", ":") = ["a", "b", "c", "d"]
    

##### Example: missing delimiter

The following example is missing the delimiter in the string value.
    
    
    strings.split("a,b,c,d", ":") = ["a,b,c,d"]
    

##### Example: empty delimiter

The following example has an empty delimiter string.
    
    
    strings.split("abc", "") = ["a", "b", "c"]
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
