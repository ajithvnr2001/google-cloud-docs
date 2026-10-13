---
url: https://docs.cloud.google.com/workflows/docs/reference/stdlib/text/find_all_regex/
title: Function: text.find_all_regex \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:21:26.860771+00:00
---

# Function: text.find_all_regex  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/stdlib/text/find_all_regex/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Function: text.find_all_regex Stay organized with collections  Save and categorize content based on your preferences. 

Finds all matches of a regular expression in a string.

A list of matches is returned, where each match has the starting index (zero-based) of the matched substring and the substring itself. In the case of overlapping matches, only the leftmost match is considered. If the overlapping matches start at the same index, then the longest match is considered.

## Arguments

Arguments  
---  
`source` |  `string` The source string to search.  
`regexp` |  `string` The regular expression used for the search. Uses [RE2 syntax](https://github.com/google/re2/wiki/Syntax).  
  
## Returns

A list of maps, where each map represents a match. The map has the keys `index` and `match` whose values are the starting index (`int`) of the substring and the substring itself (`string`), respectively. The list is sorted by the `index` key. If no match is found, an empty list is returned.

## Raised exceptions

Exceptions  
---  
`TypeError` | If either `source` or `regexp` is not a string.  
`ValueError` | If `regexp` is not UTF-8 encoded or is an invalid regular expression.  
  
## Examples
    
    
    # Find match of regular expression in string
    # Returns `[{"index":0,"match":"Hello"},{"index":5,"match":"World"}]`
    - returnStep:
        return: ${text.find_all_regex("HelloWorld", "Hello|World")}

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
