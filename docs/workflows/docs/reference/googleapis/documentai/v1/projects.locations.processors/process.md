---
url: https://docs.cloud.google.com/workflows/docs/reference/googleapis/documentai/v1/projects.locations.processors/process/
title: Method: googleapis.documentai.v1.projects.locations.processors.process \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:31:31.440067+00:00
---

# Method: googleapis.documentai.v1.projects.locations.processors.process  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/googleapis/documentai/v1/projects.locations.processors/process/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Method: googleapis.documentai.v1.projects.locations.processors.process Stay organized with collections  Save and categorize content based on your preferences. 

Processes a single document.

## Arguments

Parameters  
---  
`name` |  `string` Required. The resource name of the Processor or ProcessorVersion to use for processing. If a Processor is specified, the server will use its default version. Format: `projects/{project}/locations/{location}/processors/{processor}`, or `projects/{project}/locations/{location}/processors/{processor}/processorVersions/{processorVersion}`  
`location` |  `string` Location of the HTTP endpoint: `us` or `eu`. If not set, `us` is used by default.  
`body` |  `object ([GoogleCloudDocumentaiV1ProcessRequest](https://docs.cloud.google.com/workflows/docs/reference/googleapis/documentai/v1/Overview#GoogleCloudDocumentaiV1ProcessRequest))` Required.  
  
## Raised exceptions

Exceptions  
---  
`ConnectionError` | In case of a network problem (such as DNS failure or refused connection).  
`HttpError` | If the response status is >= 400 (excluding 429 and 503).  
`TimeoutError` | If a long-running operation takes longer to finish than the specified timeout limit.  
`TypeError` | If an operation or function receives an argument of the wrong type.  
`ValueError` | If an operation or function receives an argument of the right type but an inappropriate value. For example, a negative timeout.  
  
## Response

If successful, the response contains an instance of [`GoogleCloudDocumentaiV1ProcessResponse`](https://docs.cloud.google.com/workflows/docs/reference/googleapis/documentai/v1/Overview#GoogleCloudDocumentaiV1ProcessResponse).

## Subworkflow snippet

Some fields might be optional or required. To identify required fields, refer to the [API documentation](https://cloud.google.com/document-ai/docs/reference/rest/v1/projects.locations.processors/process).

### YAML
    
    
    - process:
        call: googleapis.documentai.v1.projects.locations.processors.process
        args:
            name: ...
            body:
                fieldMask: ...
                inlineDocument:
                    content: ...
                    entities: ...
                    entityRelations: ...
                    error:
                        code: ...
                        details: ...
                        message: ...
                    mimeType: ...
                    pages: ...
                    revisions: ...
                    shardInfo:
                        shardCount: ...
                        shardIndex: ...
                        textOffset: ...
                    text: ...
                    textChanges: ...
                    textStyles: ...
                    uri: ...
                rawDocument:
                    content: ...
                    mimeType: ...
                skipHumanReview: ...
        result: processResult

### JSON
    
    
    [
      {
        "process": {
          "call": "googleapis.documentai.v1.projects.locations.processors.process",
          "args": {
            "name": "...",
            "body": {
              "fieldMask": "...",
              "inlineDocument": {
                "content": "...",
                "entities": "...",
                "entityRelations": "...",
                "error": {
                  "code": "...",
                  "details": "...",
                  "message": "..."
                },
                "mimeType": "...",
                "pages": "...",
                "revisions": "...",
                "shardInfo": {
                  "shardCount": "...",
                  "shardIndex": "...",
                  "textOffset": "..."
                },
                "text": "...",
                "textChanges": "...",
                "textStyles": "...",
                "uri": "..."
              },
              "rawDocument": {
                "content": "...",
                "mimeType": "..."
              },
              "skipHumanReview": "..."
            }
          },
          "result": "processResult"
        }
      }
    ]

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
