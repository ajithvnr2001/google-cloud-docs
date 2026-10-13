---
url: https://docs.cloud.google.com/workflows/docs/reference/stdlib/text/substring/
title: Function: text.substring \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:21:29.759955+00:00
---

# Function: text.substring  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/stdlib/text/substring/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Function: text.substring Stay organized with collections  Save and categorize content based on your preferences. 

Extracts the substring between two zero-based indexes of a source string.

A negative index is considered an offset from the end of the string. If an index is outside of the source string's range, it is clamped to the bounds of the range.

Both `start` and `end` arguments are required; otherwise, a deployment error occurs.

## Arguments

Arguments  
---  
`source` |  `string` The string whose substring will be returned.  
`start` |  `int` The start index (inclusive) of the substring. Index is zero-based.  
`end` |  `int` The end index (exclusive) of the substring. Index is zero-based.  
  
## Returns

The substring.

## Raised exceptions

Exceptions  
---  
`TypeError` | If `source` is not a string; or, if either `start` or `end` is not an integer.  
  
## Examples

### Example 1
    
    
    - returnStep:
        return: ${text.substring("hello", 2, 4)}  # returns "ll"

### Example 2
    
    
    # Negative index is offset from string end and clamped to range bounds
    - returnStep:
        return: ${text.substring("hello", -10, 10)}  # returns "hello"

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
