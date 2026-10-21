---
url: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/math-abs/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:13:48.940286+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/math-abs/




Stay organized with collections  Save and categorize content based on your preferences. 

### math.abs

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules) [ Search ](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)
    
    
    math.abs(numericExpression)
    

#### Description

Returns the absolute value of an integer or float expression.

#### Param data types

`NUMBER`

#### Return type

`NUMBER`

#### Code samples

##### Example 1

This example returns True if the event was more than 5 minutes from the time specified (in seconds from the Unix epoch), regardless of whether the event came before or after the time specified. A call to `math.abs` cannot depend on multiple variables or placeholders. For example, you cannot replace the hardcoded time value of 1643687343 in the following example with `$e2.metadata.event_timestamp.seconds`.
    
    
    300 < math.abs($e1.metadata.event_timestamp.seconds - 1643687343)
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
