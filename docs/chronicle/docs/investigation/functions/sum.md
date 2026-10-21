---
url: https://docs.cloud.google.com/chronicle/docs/investigation/functions/sum/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T04:12:16.885157+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/investigation/functions/sum/




Stay organized with collections  Save and categorize content based on your preferences. 

### **`sum`**

The `sum` function returns the sum of values within a numeric column. It ignores `NULL` values during the calculation. It is often used with `match` to calculate the sums within different groups in the data.

Syntax | Param data types | Return type  
---|---|---  
`sum(numericExpression)` | `NUMBER` | `NUMBER`  
  
#### Code Sample

  * Find all the events where `target.ip` is not empty. For all the events that match on `principal.ip`, store a sum of `network.sent_bytes` in a variable called `sent_bytes`.
        
        target.ip != ""
        match:
          principal.ip
        outcome:
          $sent_bytes = sum(network.sent_bytes)
        




Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-27 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-27 UTC."],[],[]] 
