---
url: https://docs.cloud.google.com/workflows/docs/reference/stdlib/text/url_encode_plus/
title: Function: text.url_encode_plus \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:21:32.869705+00:00
---

# Function: text.url_encode_plus  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/stdlib/text/url_encode_plus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Function: text.url_encode_plus Stay organized with collections  Save and categorize content based on your preferences. 

Returns a string with percent-encoded reserved characters, and spaces replaced by pluses (`+`).

The reserved characters in the original string are replaced with their percent-escaped representation (`%xx`). Letters, digits, and the characters `.-_` are not escaped.

## Arguments

Arguments  
---  
`source` |  `string` The string that will be converted.  
  
## Returns

A percent-encoded copy of the `source` string with spaces converted to pluses.

## Raised exceptions

Exceptions  
---  
`TypeError` | If `source` is not a string.  
  
## Examples
    
    
    # Return string with percent-encoded reserved characters and pluses
    # Returns "a%2Fb%2Fc%3Fitem%3Dd%2Be+f"
    - returnStep:
        return: ${text.url_encode_plus("a/b/c?item=d+e f")}

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
