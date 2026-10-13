---
url: https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v1/namespaces.jobs/list/
title: Method: googleapis.run.v1.namespaces.jobs.list \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:48:16.884587+00:00
---

# Method: googleapis.run.v1.namespaces.jobs.list  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/googleapis/run/v1/namespaces.jobs/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Method: googleapis.run.v1.namespaces.jobs.list Stay organized with collections  Save and categorize content based on your preferences. 

List jobs. Results are sorted by creation time, descending.

## Arguments

Parameters  
---  
`parent` |  `string` Required. The namespace from which the jobs should be listed. Replace {namespace} with the project ID or number. It takes the form namespaces/{namespace}. For example: namespaces/PROJECT_ID  
`continue` |  `string` Do not use. Currently not supported in Cloud Run connector. If you have to use this parameter, please use http calls.  
`fieldSelector` |  `string` Optional. Not supported by Cloud Run.  
`includeUninitialized` |  `boolean` Optional. Not supported by Cloud Run.  
`labelSelector` |  `string` Optional. Allows to filter resources based on a label. Supported operations are =, !=, exists, in, and notIn.  
`limit` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` Optional. The maximum number of records that should be returned.  
`resourceVersion` |  `string` Optional. Not supported by Cloud Run.  
`watch` |  `boolean` Optional. Not supported by Cloud Run.  
`location` |  `string` Location of the HTTP endpoint. For example, `us-central1` or `asia-southeast1`. If not set, the global endpoint https://run.googleapis.com will be used, which supports list methods only. See [service endpoints](https://cloud.google.com/run/docs/reference/rest#service-endpoint) for more location options.  
  
## Raised exceptions

Exceptions  
---  
`ConnectionError` | In case of a network problem (such as DNS failure or refused connection).  
`HttpError` | If the response status is >= 400 (excluding 429 and 503).  
`TimeoutError` | If a long-running operation takes longer to finish than the specified timeout limit.  
`TypeError` | If an operation or function receives an argument of the wrong type.  
`ValueError` | If an operation or function receives an argument of the right type but an inappropriate value. For example, a negative timeout.  
  
## Response

If successful, the response contains an instance of [`ListJobsResponse`](https://cloud.google.com/workflows/docs/reference/googleapis/run/v1/Overview#ListJobsResponse).

## Subworkflow snippet

Some fields might be optional or required. To identify required fields, refer to the [API documentation](https://cloud.google.com/run/docs/reference/rest/v1/namespaces.jobs/list).

### YAML
    
    
    - list:
        call: googleapis.run.v1.namespaces.jobs.list
        args:
            parent: ...
            continue: ...
            fieldSelector: ...
            includeUninitialized: ...
            labelSelector: ...
            limit: ...
            resourceVersion: ...
            watch: ...
        result: listResult

### JSON
    
    
    [
      {
        "list": {
          "call": "googleapis.run.v1.namespaces.jobs.list",
          "args": {
            "parent": "...",
            "continue": "...",
            "fieldSelector": "...",
            "includeUninitialized": "...",
            "labelSelector": "...",
            "limit": "...",
            "resourceVersion": "...",
            "watch": "..."
          },
          "result": "listResult"
        }
      }
    ]

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
