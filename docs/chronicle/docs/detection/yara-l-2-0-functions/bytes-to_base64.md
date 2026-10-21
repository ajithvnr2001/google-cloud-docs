---
url: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/bytes-to_base64/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:53:07.410632+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/bytes-to_base64/




Stay organized with collections  Save and categorize content based on your preferences. 

### bytes.to_base64

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules) [ Search ](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)
    
    
    bytes.to_base64(bytes, optional_default_string)
    

#### Description

Function converts a `bytes` value to a `base64 encoded string`. Function calls with values that cannot be casted return an empty string by default.

#### Param data types

`BYTES`, `STRING`

#### Return type

`STRING`

#### Code samples

##### Raw Binary Bytes to Base64 Encoded String

The function converts the raw binary bytes to base64 encoded string.
    
    
    bytes.to_base64(b'000000006f8ec5586d026f9ddac56e9f2fe15b8a0000000001000000cd000000) = "AAAAAG+OxVhtAm+d2sVuny/hW4oAAAAAAQAAAM0AAAA="
    

##### Failed Conversion (Defaults to the Optionally Provided String)

The function defaults to the `"invalid bytes"` when the bytes value provided isn't valid.
    
    
    bytes.to_base64(b'000000006f8ec5586d", "invalid bytes") = "invalid bytes"
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
