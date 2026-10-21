---
url: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/timestamp-now/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:27:34.437253+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/timestamp-now/




Stay organized with collections  Save and categorize content based on your preferences. 

### timestamp.now

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules) [ Search ](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)
    
    
    timestamp.now()
    

#### Description

Returns the number of seconds since 1970-01-01 00:00:00 UTC. This is also known as _Unix epoch time_.

#### Return type

`INT`

#### Code samples

##### Example 1

The following example returns a timestamp for code executed on May 22, 2024 at 18:16:59.
    
    
    timestamp.now() = 1716401819 // Unix epoch time in seconds for May 22, 2024 at 18:16:59
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
