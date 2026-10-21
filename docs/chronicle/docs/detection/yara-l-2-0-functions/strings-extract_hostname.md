---
url: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/strings-extract_hostname/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:08:59.249198+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/strings-extract_hostname/




Stay organized with collections  Save and categorize content based on your preferences. 

### strings.extract_hostname

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules) [ Search ](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)
    
    
    strings.extract_hostname(string)
    

#### Description

Extracts the hostname from a string. This function is case sensitive.

#### Param data types

`STRING`

#### Return type

`STRING`

#### Code samples

##### Example 1

This example returns an empty string.
    
    
    strings.extract_hostname("") = ""
    

##### Example 2

random string, not a URL
    
    
    strings.extract_hostname("1234") = "1234"
    

##### Example 3

multiple backslashes
    
    
    strings.extract_hostname("\\\\") = ""
    

##### Example 4

non-English characters handled gracefully
    
    
    strings.extract_hostname("http://例子.卷筒纸.中国") = "例子.卷筒纸.中国"
    

##### Example 5

handling URIs
    
    
    strings.extract_hostname("mailto:?to=&subject=&body=") = "mailto"
    

##### Example 6

multiple characters before actual URL
    
    
    strings.extract_hostname("     \t   !$5*^)&dahgsdfs;http://www.google.com") = "www.google.com"
    

##### Example 7

special characters in URI `#`
    
    
    strings.extract_hostname("test#@google.com") = "test"
    

##### Example 8

special characters in URL `#`
    
    
    strings.extract_hostname("https://test#@google.com") = "test"
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
