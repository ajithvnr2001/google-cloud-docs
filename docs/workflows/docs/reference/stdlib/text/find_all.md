---
url: https://docs.cloud.google.com/workflows/docs/reference/stdlib/text/find_all/
title: Function: text.find_all \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:21:26.296339+00:00
---

# Function: text.find_all  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/stdlib/text/find_all/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Function: text.find_all Stay organized with collections  Save and categorize content based on your preferences. 

Finds the index of all instances of a substring in a string.

The string is indexed over code points using a zero-based index. Only non-overlapping matches are found, starting from the leftmost match.

## Arguments

Arguments  
---  
`source` |  `string` The string that will be searched.  
`substr` |  `string` The substring to search for.  
  
## Returns

A sorted list of indexes where the substring is found. If no match is found, an empty list is returned.

## Raised exceptions

Exceptions  
---  
`TypeError` | If either `source` or `substr` is not a string.  
`ValueError` | If `substr` is not UTF-8 encoded.  
  
## Examples

### Example 1
    
    
    # Find substring ("00") in source string ("00000")
    - returnStep:
        return: ${text.find_all("00000", "00")}  # returns `[0, 2]`

### Example 2
    
    
    # Find substring ("l") in source string ("Hello World")
    - returnStep:
        return: ${text.find_all("Hello World", "l")}  # returns `[2, 3, 9]`

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
