---
url: https://docs.cloud.google.com/workflows/docs/reference/googleapis/cloudbuild/v1/projects.locations.workerPools/list/
title: Method: googleapis.cloudbuild.v1.projects.locations.workerPools.list \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:59:58.032584+00:00
---

# Method: googleapis.cloudbuild.v1.projects.locations.workerPools.list  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/googleapis/cloudbuild/v1/projects.locations.workerPools/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Method: googleapis.cloudbuild.v1.projects.locations.workerPools.list Stay organized with collections  Save and categorize content based on your preferences. 

Lists `WorkerPool`s.

## Arguments

Parameters  
---  
`parent` |  `string` Required. The parent of the collection of `WorkerPools`. Format: `projects/{project}/locations/{location}`.  
`pageSize` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The maximum number of `WorkerPool`s to return. The service may return fewer than this value. If omitted, the server will use a sensible default.  
`pageToken` |  `string` A page token, received from a previous `ListWorkerPools` call. Provide this to retrieve the subsequent page.  
  
## Raised exceptions

Exceptions  
---  
`ConnectionError` | In case of a network problem (such as DNS failure or refused connection).  
`HttpError` | If the response status is >= 400 (excluding 429 and 503).  
`TimeoutError` | If a long-running operation takes longer to finish than the specified timeout limit.  
`TypeError` | If an operation or function receives an argument of the wrong type.  
`ValueError` | If an operation or function receives an argument of the right type but an inappropriate value. For example, a negative timeout.  
  
## Response

If successful, the response contains an instance of [`ListWorkerPoolsResponse`](https://docs.cloud.google.com/workflows/docs/reference/googleapis/cloudbuild/v1/Overview#ListWorkerPoolsResponse).

## Subworkflow snippet

Some fields might be optional or required. To identify required fields, refer to the [API documentation](https://cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.workerPools/list).

### YAML
    
    
    - list:
        call: googleapis.cloudbuild.v1.projects.locations.workerPools.list
        args:
            parent: ...
            pageSize: ...
            pageToken: ...
        result: listResult

### JSON
    
    
    [
      {
        "list": {
          "call": "googleapis.cloudbuild.v1.projects.locations.workerPools.list",
          "args": {
            "parent": "...",
            "pageSize": "...",
            "pageToken": "..."
          },
          "result": "listResult"
        }
      }
    ]

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
