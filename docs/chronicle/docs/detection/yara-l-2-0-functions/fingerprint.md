---
url: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/fingerprint/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T17:28:13.409644+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/fingerprint/




Stay organized with collections  Save and categorize content based on your preferences. 

### fingerprint

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules)
    
    
    hash.fingerprint2011(byteOrString)
    

#### Description

This function calculates the `fingerprint2011` hash of an input byte sequence or string. This function returns an unsigned `INT` value in the range `[2, 0xFFFFFFFFFFFFFFFF]`.

**Note:** This function shouldn't be used as a cryptographic secure hash.

#### Param data types

`BTYE`, `STRING`

#### Return type

`INT`

#### Code sample
    
    
    id_fingerprint = hash.fingerprint2011("user123")
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
