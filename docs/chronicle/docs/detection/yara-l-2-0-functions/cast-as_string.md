---
url: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/cast-as_string/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:03:21.909077+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/cast-as_string/




Stay organized with collections  Save and categorize content based on your preferences. 

### cast.as_string

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules) [ Search ](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)
    
    
    cast.as_string(int_or_bytes_or_bool, optional_default_string)
    

#### Description

The `cast.as_string` function transforms an `INT`, `BYTES`, or `BOOL` value into its string representation. You can provide an optional `default_string` argument to handle cases where the cast fails. If you omit the `default_string` argument, or if the input is an invalid `UTF-8` or `BASE64` byte sequence, the function returns an empty string.

#### Param data types

`INT|BYTES|BOOL`, `STRING`

#### Return type

`STRING`

#### Code samples

##### Integer to String Conversion

The function converts the integer `123` to the string `"123"`.
    
    
    cast.as_string(123) = "123"
    

##### Bytes to String Conversion

The function converts the raw binary `b'01` to the string `"\x01"`.
    
    
    cast.as_string(b'01, "") = "\x01"
    

##### Boolean to String Conversion

The function converts the boolean `true` to the string `"true"`.
    
    
    cast.as_string(true, "") = "true"
    

##### Failed Conversion (Defaults to the Optionally Provided String)

The function defaults to the string `"casting error"` when the value provided is invalid.
    
    
    cast.as_string(9223372036854775808, "casting error") = "casting error"
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
