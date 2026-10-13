---
url: https://docs.cloud.google.com/workflows/docs/reference/stdlib/text/match_regex/
title: Function: text.match_regex \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:21:27.348649+00:00
---

# Function: text.match_regex  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/stdlib/text/match_regex/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Function: text.match_regex Stay organized with collections  Save and categorize content based on your preferences. 

Reports whether a string contains a match of a regular expression.

## Arguments

Arguments  
---  
`source` |  `string` The string that will be searched.  
`regexp` |  `string` The regular expression that is matched. Uses [RE2 syntax](https://github.com/google/re2/wiki/Syntax).  
  
## Returns

True if `regexp` matches a substring in `source` and false otherwise.

## Raised exceptions

Exceptions  
---  
`TypeError` | If either `source` or `regexp` is not a string.  
`ValueError` | If `regexp` is not UTF-8 encoded or is an invalid regular expression.  
  
## Examples

### Example 1
    
    
    # Test match of regular expression; returns `true`
    - returnStep:
        return: ${text.match_regex("HelloWorld", "Hello|Goodbye")}

### Example 2
    
    
    # Test match of regular expression; returns `false`
    - returnStep:
        return: ${text.match_regex("HelloWorld", "Goodbye")}

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
