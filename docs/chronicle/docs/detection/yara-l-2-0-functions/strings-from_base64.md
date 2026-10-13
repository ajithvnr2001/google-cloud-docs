---
url: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/strings-from_base64/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:29:00.511834+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/strings-from_base64/




Stay organized with collections  Save and categorize content based on your preferences. 

### strings.from_base64

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules) [ Search ](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)
    
    
    strings.from_base64(base64_encoded_string)
    

#### Description

Function converts a base64 encoded `STRING` value to a raw binary `BYTES` value. Function calls with values that cannot be casted return an empty `BYTES` by default.

#### Param data types

`STRING`

#### Return type

`BYTES`

#### Code samples

##### Base64 Encoded String to Bytes Conversion

The function converts a base64 encoded string to its raw binary bytes representation.
    
    
    strings.from_base64("AAAAAG+OxVhtAm+d2sVuny/hW4oAAAAAAQAAAM0AAAA=") = b'000000006f8ec5586d026f9ddac56e9f2fe15b8a0000000001000000cd000000
    

##### Failed Conversion (Defaults to Empty Bytes)

The function defaults to empty bytes if the provided value in invalid.
    
    
    strings.from_base64("invalid-value") = b'
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
