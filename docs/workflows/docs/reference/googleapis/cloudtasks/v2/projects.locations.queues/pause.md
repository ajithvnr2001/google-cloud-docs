---
url: https://docs.cloud.google.com/workflows/docs/reference/googleapis/cloudtasks/v2/projects.locations.queues/pause/
title: Method: googleapis.cloudtasks.v2.projects.locations.queues.pause \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:22:07.634760+00:00
---

# Method: googleapis.cloudtasks.v2.projects.locations.queues.pause  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/googleapis/cloudtasks/v2/projects.locations.queues/pause/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Method: googleapis.cloudtasks.v2.projects.locations.queues.pause Stay organized with collections  Save and categorize content based on your preferences. 

Pauses the queue. If a queue is paused then the system will stop dispatching tasks until the queue is resumed via ResumeQueue. Tasks can still be added when the queue is paused. A queue is paused if its state is PAUSED.

## Arguments

Parameters  
---  
`name` |  `string` Required. The queue name. For example: `projects/PROJECT_ID/location/LOCATION_ID/queues/QUEUE_ID`  
  
## Raised exceptions

Exceptions  
---  
`ConnectionError` | In case of a network problem (such as DNS failure or refused connection).  
`HttpError` | If the response status is >= 400 (excluding 429 and 503).  
`TimeoutError` | If a long-running operation takes longer to finish than the specified timeout limit.  
`TypeError` | If an operation or function receives an argument of the wrong type.  
`ValueError` | If an operation or function receives an argument of the right type but an inappropriate value. For example, a negative timeout.  
  
## Response

If successful, the response contains an instance of [`Queue`](https://docs.cloud.google.com/workflows/docs/reference/googleapis/cloudtasks/v2/Overview#Queue).

## Subworkflow snippet

Some fields might be optional or required. To identify required fields, refer to the [API documentation](https://cloud.google.com/tasks/docs/reference/rest/v2/projects.locations.queues/pause).

### YAML
    
    
    - pause:
        call: googleapis.cloudtasks.v2.projects.locations.queues.pause
        args:
            name: ...
        result: pauseResult

### JSON
    
    
    [
      {
        "pause": {
          "call": "googleapis.cloudtasks.v2.projects.locations.queues.pause",
          "args": {
            "name": "..."
          },
          "result": "pauseResult"
        }
      }
    ]

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
