---
url: https://docs.cloud.google.com/workflows/docs/reference/googleapis/documentai/v1beta3/projects.locations.processors/create/
title: Method: googleapis.documentai.v1beta3.projects.locations.processors.create \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:45:19.202778+00:00
---

# Method: googleapis.documentai.v1beta3.projects.locations.processors.create  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/googleapis/documentai/v1beta3/projects.locations.processors/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Method: googleapis.documentai.v1beta3.projects.locations.processors.create Stay organized with collections  Save and categorize content based on your preferences. 

Creates a processor from the type processor that the user chose. The processor will be at "ENABLED" state by default after its creation.

## Arguments

Parameters  
---  
`parent` |  `string` Required. The parent (project and location) under which to create the processor. Format: `projects/{project}/locations/{location}`  
`location` |  `string` Location of the HTTP endpoint: `us` or `eu`. If not set, `us` is used by default.  
`body` |  `object ([GoogleCloudDocumentaiV1beta3Processor](https://docs.cloud.google.com/workflows/docs/reference/googleapis/documentai/v1beta3/Overview#GoogleCloudDocumentaiV1beta3Processor))` Required.  
  
## Raised exceptions

Exceptions  
---  
`ConnectionError` | In case of a network problem (such as DNS failure or refused connection).  
`HttpError` | If the response status is >= 400 (excluding 429 and 503).  
`TimeoutError` | If a long-running operation takes longer to finish than the specified timeout limit.  
`TypeError` | If an operation or function receives an argument of the wrong type.  
`ValueError` | If an operation or function receives an argument of the right type but an inappropriate value. For example, a negative timeout.  
  
## Response

If successful, the response contains an instance of [`GoogleCloudDocumentaiV1beta3Processor`](https://docs.cloud.google.com/workflows/docs/reference/googleapis/documentai/v1beta3/Overview#GoogleCloudDocumentaiV1beta3Processor).

## Subworkflow snippet

Some fields might be optional or required. To identify required fields, refer to the [API documentation](https://cloud.google.com/document-ai/docs/reference/rest/v1beta3/projects.locations.processors/create).

### YAML
    
    
    - create:
        call: googleapis.documentai.v1beta3.projects.locations.processors.create
        args:
            parent: ...
            body:
                createTime: ...
                defaultProcessorVersion: ...
                displayName: ...
                kmsKeyName: ...
                type: ...
        result: createResult

### JSON
    
    
    [
      {
        "create": {
          "call": "googleapis.documentai.v1beta3.projects.locations.processors.create",
          "args": {
            "parent": "...",
            "body": {
              "createTime": "...",
              "defaultProcessorVersion": "...",
              "displayName": "...",
              "kmsKeyName": "...",
              "type": "..."
            }
          },
          "result": "createResult"
        }
      }
    ]

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
