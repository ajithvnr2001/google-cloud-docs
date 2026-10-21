---
url: https://docs.cloud.google.com/chronicle/docs/investigation/functions/count-distinct/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T07:19:56.615175+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/investigation/functions/count-distinct/




Stay organized with collections  Save and categorize content based on your preferences. 

### **`count_distinct`**

The `count_distinct` function returns the number of rows that have distinct values within a group. It is often used with `match` to get counts for specific groups in the data.

**Note:** Missing or uninitialized Unified Data Model (UDM) fields default to zero values (such as `""`, `0`, or `"UNKNOWN_ACTION"`) instead of `NULL`. Because `count_distinct` evaluates zero values as valid data, it counts them as unique items. If a field is uninitialized in some events, `count_distinct` counts the zero value as an additional distinct item, increasing your total count by one. To exclude default values from your count, add a filter in the `events` section of your query (for example, `$userid != ""`).Syntax | Param data types | Return type  
---|---|---  
`count_distinct(expression)` | `STRING` | `NUMBER`  
  
#### Code Samples

  * **Return count of distinct user logins**

Return the count of distinct successful user logins over time.
        
        metadata.event_type = "USER_LOGIN"
          $security_result = security_result.action
          $security_result = "ALLOW"
          $date = timestamp.get_date(metadata.event_timestamp.seconds, "America/Los_Angeles")
          match:
              $security_result, $date
          outcome:
              $event_count = count_distinct(metadata.id)
        

  * **Exclude default values from distinct counts**

The following example filters out uninitialized user IDs so `count_distinct` doesn't include default empty strings in the total count:
        
        metadata.event_type = "USER_LOGIN"
        $userid = principal.user.userid
        $userid != ""
        match:
            metadata.event_type
        outcome:
            $distinct_users = count_distinct($userid)
        




Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-27 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-27 UTC."],[],[]] 
