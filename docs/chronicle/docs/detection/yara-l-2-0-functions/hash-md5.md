---
url: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/hash-md5/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:53:03.946086+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/hash-md5/




Stay organized with collections  Save and categorize content based on your preferences. 

### hash.md5

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules)
    
    
    hash.md5(string)
    

#### Description

Computes the hash of the string input using the MD5 algorithm.

#### Param data types

`STRING`

#### Return type

`STRING`

#### Code samples

##### Example 1

This example shows the MD5 hash when the input is a valid string.
    
    
    hash.md5("str") = "341be97d9aff90c9978347f66f945b77"
    

##### Example 2

This example shows the MD5 hash when the input is an empty string.
    
    
    hash.md5("") = "d41d8cd98f00b204e9800998ecf8427e"
    

##### Example 3

This example shows the MD5 hash when the input is non-ASCII characters.
    
    
    hash.md5("筒纸.中国") = "dfd1ba91f7305feae3cad551bce9ad7e"
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
