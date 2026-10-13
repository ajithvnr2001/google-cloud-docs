---
url: https://docs.cloud.google.com/workflows/docs/reference/stdlib/text/split/
title: Function: text.split \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:21:29.183734+00:00
---

# Function: text.split  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/stdlib/text/split/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Function: text.split Stay organized with collections  Save and categorize content based on your preferences. 

Splits the source string into a list of all substrings between each instance of the separator.

The separator itself is excluded from the substrings. In the case of overlapping instances of the separator, the leftmost match is considered.

Empty substrings are included in the list.

If the separator is not found, then a list containing only the source string is returned.

## Arguments

Arguments  
---  
`source` |  `string` The string that will be split.  
`separator` |  `string` The separator used to split the string.  
  
## Returns

A list of substrings in `source`.

## Raised exceptions

Exceptions  
---  
`TypeError` | If either `source` or `separator` is not a string.  
`ValueError` | If `separator` is an empty string or is not UTF-8 encoded.  
  
## Examples

### Example 1
    
    
    # Overlapping separator instances; leftmost match is considered
    - returnStep:
        return: ${text.split("baaab", "aa")}  # returns `["b", "ab"]`

### Example 2
    
    
    # Separator is found at beginning of string
    - returnStep:
        return: ${text.split("abc", "a")}  # returns `["", "bc"]`

### Example 3
    
    
    # Separator is found at end of string
    - returnStep:
        return: ${text.split("abc", "c")}  # returns `["ab", ""]`

### Example 4
    
    
    # Consecutive instances of the separator
    - returnStep:
        return: ${text.split("abbc", "b")}  # returns `["a", "", "c"]`

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
