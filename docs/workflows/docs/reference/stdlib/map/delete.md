---
url: https://docs.cloud.google.com/workflows/docs/reference/stdlib/map/delete/
title: Function: map.delete \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:21:15.434732+00:00
---

# Function: map.delete  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/stdlib/map/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Function: map.delete Stay organized with collections  Save and categorize content based on your preferences. 

Takes a map, creates a copy of the map, and removes the item for the specified key.

If the key doesn't exist in the map, the function returns a copy of the original map.

For example, if you have `map1 = {key1: value1, key2: value2}` and `key = key3`, `map.delete(map, key)` returns `{key1: value1, key2: value2}`.

## Arguments

Arguments  
---  
`map` | The map to delete from.  
`key` | A string that represents the specified key to remove from the map.  
  
## Returns

A copy of the map with the item specified by the key removed.

## Raised exceptions

Exceptions  
---  
`TypeError` | If `map` is not a map (dictionary) or the `key` is not a string.  
  
## Examples
    
    
    # Remove item for specified key from copy of map
    # Returns `{"key1": "hello"}`
    - init:
        assign:
          - my_map: {"key1": "hello", "key2": "world"}
    - returnStep:
        return: ${map.delete(my_map, "key2")}

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
