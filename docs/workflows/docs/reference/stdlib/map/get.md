---
url: https://docs.cloud.google.com/workflows/docs/reference/stdlib/map/get/
title: Function: map.get \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:21:15.981620+00:00
---

# Function: map.get  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/stdlib/map/get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Function: map.get Stay organized with collections  Save and categorize content based on your preferences. 

Performs a safe lookup on a map, returning `null` if the key is not found.

For nested maps, a list of keys can be used to drill down into the map, using a nested key lookup. For example, `map.get(my2DMap, ["key1", "key2"])` is equivalent to `map.get(map.get(my2DMap, "key1"), "key2")`.

You can use the conditional function [`default`](https://cloud.google.com/workflows/docs/reference/stdlib/expression-helpers#conditional_functions) with `map.get` to safely access optional values in a map. For an example, see [Read map values](https://cloud.google.com/workflows/docs/reference/syntax/maps#reading-map).

## Arguments

Arguments  
---  
`map` | The map to perform the lookup on.  
`keys` | A string or list of strings used for the lookup. If a list is used, the function is called repeatedly, using the list of keys.  
  
## Returns

If `keys` is a single string, returns the indexed value. If the input is not a map or if the map does not contain the key, returns null.

If `keys` is a list, then a nested key lookup is performed and the value is returned. If any of the nested objects are not maps or if the key does not exist in the map then `null` is returned.

## Raised exceptions

Exceptions  
---  
`TypeError` | If the key is not a string or a list of strings.  
  
## Examples
    
    
    # Retrieve item for specified key from map
    # Returns "world"
    - init:
        assign:
          - my_map: {"key1": "hello", "key2": "world"}
    - returnStep:
        return: ${map.get(my_map, "key2")}

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
