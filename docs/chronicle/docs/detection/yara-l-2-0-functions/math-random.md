---
url: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/math-random/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:18:49.494678+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/math-random/




Stay organized with collections  Save and categorize content based on your preferences. 

### math.random

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules) [ Search ](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)
    
    
    math.random()
    

#### Description

Generates a pseudo-random value of type DOUBLE in the range of `[0, 1)`, inclusive of 0 and exclusive of 1.

#### Return type

`FLOAT`

#### Code samples

The following example checks whether the random value is in the range `[0, 1)`. `none if(math.random() >= 0 and math.random() < 1) = true`

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
