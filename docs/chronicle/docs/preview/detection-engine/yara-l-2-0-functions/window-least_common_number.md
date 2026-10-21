---
url: https://docs.cloud.google.com/chronicle/docs/preview/detection-engine/yara-l-2-0-functions/window-least_common_number/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:48:43.827905+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/preview/detection-engine/yara-l-2-0-functions/window-least_common_number/




Stay organized with collections  Save and categorize content based on your preferences. 

### window.least_common_number

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules) [ Search ](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)
    
    
    window.least_common_number( numbers, number_of_least_common_values)
    

#### Description

Returns the specified number of least common int or float in the input values. A maximum of 1000 values can be extracted.

#### Param data types

`INT|FLOAT`, `INT`

#### Return type

`ARRAY_FLOATS`

#### Code samples
    
    
    // This rule sets the outcome $least_common_values to the least common int or float in the input values
    // in the 5 minute match window.
    events:
     $e.user.userid = $userid
    match:
     $userid over 5m
    outcome:
      $least_common_values = window.least_common_number($e.target.asset.location.region_latitude, 3) // Returns 35.227087,37.422407 and 32.715738 for given latitudes: 37.422407, 40.712775, 40.712775, 40.712775, 32.715738, 35.227087, 32.715738
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
