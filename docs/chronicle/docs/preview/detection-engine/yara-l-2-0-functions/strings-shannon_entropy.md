---
url: https://docs.cloud.google.com/chronicle/docs/preview/detection-engine/yara-l-2-0-functions/strings-shannon_entropy/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T01:36:11.472428+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/preview/detection-engine/yara-l-2-0-functions/strings-shannon_entropy/




Stay organized with collections  Save and categorize content based on your preferences. 

### strings.shannon_entropy

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules) [ Search ](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)
    
    
    strings.shannon_entropy(string_to_calculate_entropy_for)
    

#### Description

A function that calculates the Shannon entropy of a string, and returns the result as a float. Low values of Shannon entropy indicates the provided string has a higher degree of predictability or certainty. For example, the same characters appearing many times in a string. High values of Shannon entropy indicate a higher degree of unpredictability or uncertainty. For example, a more even distribution of characters in a string where each character is equally likely to occur. High values of entropy can be useful for finding randomness in text; for example cryptographic, compressed, or randomly generated data.

#### Param data types

`STRING`

#### Return type

`FLOAT`

#### Code samples

This section contains examples that calculate the Shannon entropy of a string.

##### Example 1

Random string value.
    
    
    strings.shannon_entropy("asdkjqweuriownvancxoql1273hagjga") = 4.375
    

##### Example 2

Empty string value returns a -1.
    
    
    strings.shannon_entropy("") = -1
    

##### Example 3

Random string value with many characters.
    
    
    strings.shannon_entropy("abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890") = 5.169925
    

##### Example 4

Low entropy string.
    
    
    strings.shannon_entropy("google.com") = 2.646439
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
