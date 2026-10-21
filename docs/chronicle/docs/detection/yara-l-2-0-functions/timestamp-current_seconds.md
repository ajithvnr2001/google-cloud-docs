---
url: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/timestamp-current_seconds/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:26:17.893270+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/timestamp-current_seconds/




Stay organized with collections  Save and categorize content based on your preferences. 

### timestamp.current_seconds

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules) [ Search ](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)
    
    
    timestamp.current_seconds()
    

#### Description

Returns an integer representing the current time in Unix seconds. This is approximately equal to the detection timestamp and is based on when the rule is run. This function is a synonym of the function `timestamp.now()`.

#### Param data types

`NONE`

#### Return type

`INT`

#### Code samples

##### Example 1

The following example returns `true` if the certificate has been expired for more than 24 hours. It calculates the time difference by subtracting the current Unix seconds, and then comparing using a greater than operator.
    
    
    86400 < timestamp.current_seconds() - $e.network.tls.certificate.not_after
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
