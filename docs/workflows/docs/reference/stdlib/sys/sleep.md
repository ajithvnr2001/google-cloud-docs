---
url: https://docs.cloud.google.com/workflows/docs/reference/stdlib/sys/sleep/
title: Function: sys.sleep \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:21:23.884436+00:00
---

# Function: sys.sleep  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/stdlib/sys/sleep/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Function: sys.sleep Stay organized with collections  Save and categorize content based on your preferences. 

Suspends execution for the given number of seconds.

Maximum is 31536000 (one year).

For more information, see [Wait using polling](https://cloud.google.com/workflows/docs/sleeping).

## Arguments

Arguments  
---  
`seconds` | The number of seconds the execution should be suspended for.  
  
## Examples
    
    
    # Poll API until job status is complete
    main:
        params: [jobId]
        steps:
          - getJob:  # get job status
              call: http.get
              args:
                  url: ${"https://example.com/jobs/" + jobId}
                  auth:
                      type: OAuth2
              result: jobStatus
          - checkIfDone:  # check job status
              switch:
                - condition: ${jobStatus.complete}
                  return: ${jobStatus}  # stop polling
          - wait:
              call: sys.sleep
              args:
                  seconds: 60  # wait 60 seconds
              next: getJob

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
