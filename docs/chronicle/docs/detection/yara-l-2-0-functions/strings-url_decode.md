---
url: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/strings-url_decode/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:18:34.769725+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/strings-url_decode/




Stay organized with collections  Save and categorize content based on your preferences. 

### strings.url_decode

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules) [ Search ](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)
    
    
    strings.url_decode(url_string)
    

#### Description

Given a URL string, decode the escape characters and handle UTF-8 characters that have been encoded. Returns empty string if decoding fails.

#### Param data types

`STRING`

#### Return type

`STRING`

#### Code samples

##### Example 1

This example shows a positive test case.
    
    
    strings.url_decode("three%20nine%20four") = "three nine four"
    

##### Example 2

This example shows an empty string case.
    
    
    strings.url_decode("") // ""
    

##### Example 3

This example shows non-alphabet characters handling.
    
    
    strings.url_decode("%E4%B8%8A%E6%B5%B7%2B%E4%B8%AD%E5%9C%8B") // "上海+中國"
    

##### Example 4

This example shows a sample URL decoding.
    
    
    strings.url_decode("http://www.google.com%3Fparam1%3D%22+1+%3E+2+%22%26param2%3D2%3B") // 'http://www.google.com?param1="+1+>+2+"&param2=2;'
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
