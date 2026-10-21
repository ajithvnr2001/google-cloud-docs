---
url: https://docs.cloud.google.com/chronicle/docs/investigation/functions/array/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:15:25.218702+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/investigation/functions/array/




Stay organized with collections  Save and categorize content based on your preferences. 

### **`array`**

The `array` function returns all values in the form of a list.

The maximum number of elements returned depends on where the query runs:

  * **Search** : truncates the list to a maximum of 1,000 random elements.
  * **Dashboards and Rules** : truncates the list to a maximum of 25 random elements.

Syntax | Param data types | Return type  
---|---|---  
`array(expression)` | `STRING` | `LIST`  
  
#### Code Sample

  * Return an array containing event types.
        
        $event_type = metadata.event_type
        outcome:
          $event_type_array = array($event_type)
        




Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-13 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-13 UTC."],[],[]] 
