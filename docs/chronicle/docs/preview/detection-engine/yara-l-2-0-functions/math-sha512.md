---
url: https://docs.cloud.google.com/chronicle/docs/preview/detection-engine/yara-l-2-0-functions/math-sha512/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T08:35:01.625662+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/preview/detection-engine/yara-l-2-0-functions/math-sha512/




Stay organized with collections  Save and categorize content based on your preferences. 

### math.sha512

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules) [ Search ](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)
    
    
    math.sha512(string)
    

#### Description

Returns the SHA-512 hash of the provided string.

#### Param data types

`STRING`

#### Return type

`STRING`

#### Code samples

Here are some examples of how to use the function:

##### Example 1

This example returns the SHA-512 hash of an empty string.
    
    
    math.sha512("") = "cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e"
    

##### Example 2

This example returns the SHA-512 hash of a random string.
    
    
    math.sha512("safsghadfghasd") = "8060da762183d083cabb52cb99ace1d6d66d803d2011a27cb6a659d28278f3c4ee91ef21e0e61fc9cdb10a1b94de03d6e69de968347ccd0f3c02cb396ae948bc"
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
