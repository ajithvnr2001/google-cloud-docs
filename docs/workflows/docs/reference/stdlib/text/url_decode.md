---
url: https://docs.cloud.google.com/workflows/docs/reference/stdlib/text/url_decode/
title: Function: text.url_decode \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:21:30.967809+00:00
---

# Function: text.url_decode  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/stdlib/text/url_decode/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Function: text.url_decode Stay organized with collections  Save and categorize content based on your preferences. 

Returns a string with pluses and percent-escaped characters converted to UTF-8.

Percent-escaped characters (`%xx`) are replaced with their reserved character equivalents. Plus signs (`+`) are replaced with spaces. Percent-encoded sequences are converted into UTF-8.

## Arguments

Arguments  
---  
`source` |  `string` The string that will be converted.  
  
## Returns

An unescaped copy of the `source` string with pluses converted to spaces.

## Raised exceptions

Exceptions  
---  
`TypeError` | If `source` is not a string.  
`ValueError` | If `source` contains any `%` not followed by two hexadecimal characters.  
  
## Examples
    
    
    # Return string converted to UTF-8
    # Returns "a/b/c?item=d+e"
    - returnStep:
        return: ${text.url_decode("a%2Fb%2Fc%3Fitem%3Dd%2Be")}

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
