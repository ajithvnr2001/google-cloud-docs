---
url: https://docs.cloud.google.com/chronicle/docs/investigation/functions/earliest/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T00:44:49.762513+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/investigation/functions/earliest/




Stay organized with collections  Save and categorize content based on your preferences. 

### **`earliest`**

Supported in:

[ Dashboards ](https://docs.cloud.google.com/chronicle/docs/reports/dashboards-overview) [ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules) [ Search ](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)

The `earliest` function returns the earliest timestamp from a set of records with microsecond resolution.

Syntax | Param data types | Return type  
---|---|---  
`earliest(timestamp)` | `TIMESTAMP` | `TIMESTAMP`  
  
#### Code sample

  * For all the events that match on `hostname`, store the earliest of `metadata.event_timestamp` in the `start` variable.
        
        $hostname = principal.hostname
        match:
          $hostname
        outcome:
          $start = earliest(metadata.event_timestamp)
        




Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
