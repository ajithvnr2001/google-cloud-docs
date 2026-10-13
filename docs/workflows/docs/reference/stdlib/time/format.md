---
url: https://docs.cloud.google.com/workflows/docs/reference/stdlib/time/format/
title: Function: time.format \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:21:33.427425+00:00
---

# Function: time.format  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/stdlib/time/format/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Function: time.format Stay organized with collections  Save and categorize content based on your preferences. 

Formats the given timestamp as a human-readable string.

## Arguments

Arguments  
---  
`seconds` |  `integer|float` A timestamp in seconds since epoch.  
`timezone` |  `string` A timezone name from the tz database: <http://en.wikipedia.org/wiki/Tz_database>. If not specified or if an empty string, the default is UTC.  
  
## Returns

A timestamp string in ISO 8601 format, up to a microsecond precision. For example: "2024-01-10T16:15:54.615087Z".

## Examples
    
    
    # Format given timestamp as human-readable string
    # For example, returns "2024-07-12T12:50:33.000000Z"
    - returnStep:
        return: ${time.format(1720788633,"GMT")}
    # For example, returns "2024-07-12T12:50:33.000000Z"
    - returnStep:
        return: ${time.format(1720788633)}
    # For example, returns "2024-07-12T14:50:33.000000+02:00"
    - returnStep:
        return: ${time.format(1720788633,"Europe/Paris")}
    # Or, you can use `sys.now` which returns Unix time
    - returnStep:
        return: ${time.format(sys.now())}

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
