---
url: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/arrays-length/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:02:02.081280+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/arrays-length/




Stay organized with collections  Save and categorize content based on your preferences. 

### arrays.length

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules) [ Search ](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)
    
    
    arrays.length(repeatedField)
    

#### Description

Returns the number of repeated field elements.

#### Param data types

`LIST`

#### Return type

`NUMBER`

#### Code samples

##### Example 1

Returns the number of repeated field elements.
    
    
    arrays.length($e.principal.ip) = 2
    

##### Example 2

If multiple repeated fields are along the path, returns the total number of repeated field elements.
    
    
    arrays.length($e.intermediary.ip) = 3
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
