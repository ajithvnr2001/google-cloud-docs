---
url: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/cast-as_float/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:43:34.694687+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/cast-as_float/




Stay organized with collections  Save and categorize content based on your preferences. 

### cast.as_float

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules) [ Search ](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)
    
    
    cast.as_float(string_to_cast)
    

#### Description

Converts a numeric string into a float. Any function calls with values that cannot be casted return 0. Floats maintain precision up to 7 decimal digits.

#### Param data types

`STRING`

#### Return type

`FLOAT`

#### Code samples

##### Example 1

Casting a non-numeric string returns 0.
    
    
    cast.as_float("str") = 0.0000000
    

##### Example 2

Casting an empty string returns 0.
    
    
    cast.as_float("") = 0.0000000
    

##### Example 3

Casting a valid numeric string returns a float value.
    
    
    cast.as_float("1.012345678") = 1.0123456
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
