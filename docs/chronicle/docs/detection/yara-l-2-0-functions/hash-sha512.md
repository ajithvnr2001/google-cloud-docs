---
url: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/hash-sha512/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T09:34:57.663542+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/hash-sha512/




Stay organized with collections  Save and categorize content based on your preferences. 

### hash.sha512

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules)
    
    
    hash.sha512(string)
    

#### Description

Returns the SHA-512 hash of the input string.

#### Param data types

`STRING`

#### Return type

`STRING`

#### Code samples

##### Example 1

This example shows the SHA-512 hash when the input is a valid string.
    
    
    hash.sha512("str") = "32cdec9e4b5ffffa909024b4a710850ee2e1b4d3f19ffd8f24898c3e84019997acfa1f9ddd0dfdca21288dc92ca766a0cb10e0cd7b2d6926deffeccc59239502"
    

##### Example 2

This example shows the SHA-512 hash when the input is an empty string.
    
    
    hash.sha512("") = "cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e"
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
