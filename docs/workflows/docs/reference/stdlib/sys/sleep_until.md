---
url: https://docs.cloud.google.com/workflows/docs/reference/stdlib/sys/sleep_until/
title: Function: sys.sleep_until \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:21:25.627731+00:00
---

# Function: sys.sleep_until  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/stdlib/sys/sleep_until/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Function: sys.sleep_until Stay organized with collections  Save and categorize content based on your preferences. 

Suspends execution until the given time.

The latest allowed time is one year from now.

## Arguments

Arguments  
---  
`time` | Timestamp in ISO 8601 format until which execution is suspended, up to a microsecond precision.  
  
## Raised exceptions

Exceptions  
---  
`TypeError` | If `time` is not a string.  
`ValueError` | If `time` is not ISO 8601-compatible.  
  
## Examples
    
    
    # Pause execution of workflow until May 8, 2024 at 1:22:58 PM UTC
    # For example, returns "2024-05-08T13:22:58.120062Z"
    - pauseWorkflow:
        call: sys.sleep_until
        args:
            time: "2024-05-08T13:22:58Z"
    - returnStep:
        return: ${time.format(sys.now())}

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
