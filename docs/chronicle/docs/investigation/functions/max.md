---
url: https://docs.cloud.google.com/chronicle/docs/investigation/functions/max/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:32:22.019426+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/investigation/functions/max/




Stay organized with collections  Save and categorize content based on your preferences. 

### **`max`**

The `max` function returns the maximum of the values within a numeric column. It is often used with `match` to get the maximum value within each group in the data.

Syntax | Param data types | Return type  
---|---|---  
`max(numericExpression)` | `NUMBER` | `NUMBER`  
  
#### Code Sample

  * Find all the events where `target.ip` is not empty. For all the events that match on `principal.ip`, store the maximum of `metadata.event_timestamp.seconds` in a variable called `max_seconds`.
        
        target.ip != ""
        match:
          principal.ip
        outcome:
          $max_seconds = max(metadata.event_timestamp.seconds)
        




Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-27 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-27 UTC."],[],[]] 
