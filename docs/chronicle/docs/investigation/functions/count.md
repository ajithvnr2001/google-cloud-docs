---
url: https://docs.cloud.google.com/chronicle/docs/investigation/functions/count/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:06:50.407903+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/investigation/functions/count/




Stay organized with collections  Save and categorize content based on your preferences. 

### **`count`**

The `count` function returns the number of rows within a group. It is often used with `match` to get counts for specific groups in the data.

Syntax | Param data types | Return type  
---|---|---  
`count(expression)` | `STRING` | `NUMBER`  
  
#### Code Sample

  * Return the count of successful user logins over time.
        
        metadata.event_type = "USER_LOGIN"
        $security_result = security_result.action
        $security_result = "ALLOW"
        $date = timestamp.get_date(metadata.event_timestamp.seconds, "America/Los_Angeles")
        match:
            $security_result, $date
        outcome:
            $event_count = count(metadata.id)
        




Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-27 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-27 UTC."],[],[]] 
