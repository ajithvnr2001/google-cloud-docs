---
url: https://docs.cloud.google.com/chronicle/docs/investigation/functions/array-distinct/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T16:04:05.176597+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/investigation/functions/array-distinct/




Stay organized with collections  Save and categorize content based on your preferences. 

### **`array_distinct`**

The `array_distinct` function returns all distinct values in the form of a list. The deduplication to produce a distinct list is applied before truncation.

The maximum number of elements returned depends on where the query runs:

  * **Search** : Truncates the list to a maximum of 1,000 random elements.
  * **Dashboards and Rules** : Truncates the list to a maximum of 25 random elements.

**Note:** Missing or uninitialized Unified Data Model (UDM) fields default to zero values (such as `""`, `0`, or `"UNKNOWN_ACTION"`) instead of `NULL`. Because `array_distinct` treats zero values as valid data, it includes them in the returned list. For example, an outcome array containing only the empty string (`[""]`) displays as `[Unknown]` in your detection timeline. To remove default values from your array, add a filter in the `events` section of your query. When filtering repeated fields, use the `any` keyword (for example, `any $e.security_result.description != ""`) to preserve all array indexes during aggregation.Syntax | Param data types | Return type  
---|---|---  
`array_distinct(expression)` | `STRING` | `LIST`  
  
#### Code Samples

  * **Return distinct event types**

Return an array containing distinct event types.
        
        $event_type = metadata.event_type
        outcome:
          $event_type_array = array_distinct($event_type)
        

  * **Exclude default values from distinct arrays**

The following example filters out events that lack a security result description. It uses the any keyword on the repeated field to preserve all array indexes during outcome aggregation:
        
        events:
          $e.security_result[0].description != ""
          any $e.security_result.description = ""
        outcome:
          $security_result_description = array_distinct($e.security_result.description)
        




Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-13 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-13 UTC."],[],[]] 
