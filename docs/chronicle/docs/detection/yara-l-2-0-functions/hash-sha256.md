---
url: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/hash-sha256/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T16:03:48.919955+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/hash-sha256/




Stay organized with collections  Save and categorize content based on your preferences. 

### hash.sha256

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules)
    
    
    hash.sha256(string)
    

#### Description

Returns a SHA-256 hash of the input string.

#### Param data types

`STRING`

#### Return type

`STRING`

#### Code samples

##### Example 1

This example shows the SHA-256 hash when the input is a valid string.
    
    
    hash.sha256("str") = "8c25cb3686462e9a86d2883c5688a22fe738b0bbc85f458d2d2b5f3f667c6d5a"
    

##### Example 2

This example shows the SHA-256 hash when the input is an empty string.
    
    
    hash.sha256("") = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
