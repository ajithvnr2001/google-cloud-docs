---
url: https://docs.cloud.google.com/workflows/docs/reference/stdlib/time/parse/
title: Function: time.parse \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:21:34.040798+00:00
---

# Function: time.parse  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/stdlib/time/parse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Function: time.parse Stay organized with collections  Save and categorize content based on your preferences. 

Parses the given RFC 3339-compatible string into a timestamp.

## Arguments

Arguments  
---  
`value` |  `string` A string formatted according to the subset of ISO 8601 defined by [RFC 3339 section 5.6](https://datatracker.ietf.org/doc/html/rfc3339#section-5.6), with up to a microsecond precision.  
  
## Returns

The timestamp corresponding to the string, as a floating point number in seconds since epoch.

## Raised exceptions

Exceptions  
---  
`TypeError` | If `time` is not a string.  
`ValueError` | If `time` is not compatible with [RFC 3339 section 5.6](https://datatracker.ietf.org/doc/html/rfc3339#section-5.6).  
  
## Examples
    
    
    # Parse given RFC 3339-compatible string into a timestamp
    # For example, returns `1715169660`
    - returnStep:
        return: ${time.parse("2024-05-08T12:01:00.000000Z")}

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
