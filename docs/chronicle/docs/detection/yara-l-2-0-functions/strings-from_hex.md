---
url: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/strings-from_hex/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:36:54.706267+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/strings-from_hex/




Stay organized with collections  Save and categorize content based on your preferences. 

### strings.from_hex

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules) [ Search ](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)
    
    
    strings.from_hex(hex_string)
    

#### Description

Returns the bytes associated with the given hex string.

#### Param data types

`STRING`

#### Return type

`BYTES`

#### Code samples

Get bytes associated with a given hex string. 

##### Example 1

This example shows non-hex character conversions.
    
    
    strings.from_hex("str") // returns empty bytes
    

##### Example 2

This example shows input with empty string.
    
    
    strings.from_hex("") // returns empty bytes
    

##### Example 3

This example shows hex string conversion.
    
    
    strings.from_hex("1234") // returns 1234 bytes
    

##### Example 4

This example shows non-ASCII characters conversion.
    
    
    strings.from_hex("筒纸.中国") // returns empty bytes
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
