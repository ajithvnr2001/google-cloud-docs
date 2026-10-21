---
url: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/math-round/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T07:02:29.894741+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/math-round/




Stay organized with collections  Save and categorize content based on your preferences. 

### math.round

Supported in:

[ Search ](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)
    
    
    math.round(numericExpression, decimalPlaces)
    

#### Description

Returns a value rounded to the nearest integer or to the specified number of decimal places.

#### Param data types

`NUMBER`

#### Return type

`NUMBER`

#### Code samples
    
    
    math.round(10.7) // returns 11
    math.round(1.2567, 2) // returns 1.25
    math.round(0-10.7) // returns -11
    math.round(0-1.2) // returns -1
    math.round(4) // returns 4, math.round(integer) returns the integer
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
