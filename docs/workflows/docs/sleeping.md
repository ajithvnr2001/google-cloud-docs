---
url: https://docs.cloud.google.com/workflows/docs/sleeping/
title: Wait using polling \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:59.523518+00:00
---

# Wait using polling  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/sleeping/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Guides ](https://docs.cloud.google.com/workflows/docs/create-workflow-console)



Send feedback 

#  Wait using polling Stay organized with collections  Save and categorize content based on your preferences. 

Pausing a workflow execution lets you poll an external service or wait for a long-running operation to complete. The `sys.sleep` [standard library function](https://docs.cloud.google.com/workflows/docs/reference/stdlib/sys/sleep) suspends execution for a specified number of seconds, up to a maximum of 31536000 (one year).

## Pause a workflow

You can pause the execution of a workflow by adding a sleep step to your workflow's definition. This step includes a call to `sys.sleep` and specifies in seconds how long you want to pause the workflow:

### YAML
    
    
      - STEP_NAME:
          call: sys.sleep
          args:
              seconds: SLEEP_IN_SECONDS
        

### JSON
    
    
        [
          {
            "STEP_NAME": {
              "call": "sys.sleep",
              "args": {
                "seconds": "SLEEP_IN_SECONDS"
              }
            }
          }
        ]
        

## Poll for data

You can also use `sys.sleep` to poll for data over a given interval. For example, you might want to poll an API until a specific condition is met:

### YAML
    
    
      main:
          params: [jobId]
          steps:
            - checkJob:
                call: http.get
                args:
                    url: ${"https://example.com/jobs/" + jobId}
                    auth:
                        type: OAuth2
                result: jobStatus
            - checkIfDone:
                switch:
                  - condition: ${jobStatus.complete}
                    return: ${jobStatus}
            - wait:
                call: sys.sleep
                args:
                    seconds: 60
                next: checkJob
        

### JSON
    
    
      {
        "main": {
          "params": [
            "jobId"
          ],
          "steps": [
            {
              "checkJob": {
                "call": "http.get",
                "args": {
                  "url": "${\"https://example.com/jobs/\" + jobId}",
                  "auth": {
                    "type": "OAuth2"
                  }
                },
                "result": "jobStatus"
              }
            },
            {
              "checkIfDone": {
                "switch": [
                  {
                    "condition": "${jobStatus.complete}",
                    "return": "${jobStatus}"
                  }
                ]
              }
            },
            {
              "wait": {
                "call": "sys.sleep",
                "args": {
                  "seconds": 60
                },
                "next": "checkJob"
              }
            }
          ]
        }
      }
        

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
