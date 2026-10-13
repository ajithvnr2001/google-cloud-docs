---
url: https://docs.cloud.google.com/workflows/docs/reference/googleapis/aiplatform/v1/projects.locations.metadataStores.executions/queryExecutionInputsAndOutputs/
title: Method: googleapis.aiplatform.v1.projects.locations.metadataStores.executions.queryExecutionInputsAndOutputs \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:23:12.074371+00:00
---

# Method: googleapis.aiplatform.v1.projects.locations.metadataStores.executions.queryExecutionInputsAndOutputs  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/googleapis/aiplatform/v1/projects.locations.metadataStores.executions/queryExecutionInputsAndOutputs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Method: googleapis.aiplatform.v1.projects.locations.metadataStores.executions.queryExecutionInputsAndOutputs Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Obtains the set of input and output Artifacts for this Execution, in the form of LineageSubgraph that also contains the Execution and connecting Events.

## Arguments

Parameters  
---  
`execution` |  `string` Required. The resource name of the Execution whose input and output Artifacts should be retrieved as a LineageSubgraph. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}/executions/{execution}`  
`region` |  `string` Required. Region of the HTTP endpoint. For example, if region is set to `us-central1`, the endpoint https://us-central1-integrations.googleapis.com will be used. See [service endpoints](https://cloud.google.com/vertex-ai/docs/reference/rest#rest_endpoints).  
  
## Raised exceptions

Exceptions  
---  
`ConnectionError` | In case of a network problem (such as DNS failure or refused connection).  
`HttpError` | If the response status is >= 400 (excluding 429 and 503).  
`TimeoutError` | If a long-running operation takes longer to finish than the specified timeout limit.  
`TypeError` | If an operation or function receives an argument of the wrong type.  
`ValueError` | If an operation or function receives an argument of the right type but an inappropriate value. For example, a negative timeout.  
  
## Response

If successful, the response contains an instance of [`GoogleCloudAiplatformV1LineageSubgraph`](https://cloud.google.com/workflows/docs/reference/googleapis/aiplatform/v1/Overview#GoogleCloudAiplatformV1LineageSubgraph).

## Subworkflow snippet

Some fields might be optional or required. To identify required fields, refer to the [API documentation](https://cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.metadataStores.executions/queryExecutionInputsAndOutputs).

### YAML
    
    
    - queryExecutionInputsAndOutputs:
        call: googleapis.aiplatform.v1.projects.locations.metadataStores.executions.queryExecutionInputsAndOutputs
        args:
            execution: ...
            region: ...
        result: queryExecutionInputsAndOutputsResult

### JSON
    
    
    [
      {
        "queryExecutionInputsAndOutputs": {
          "call": "googleapis.aiplatform.v1.projects.locations.metadataStores.executions.queryExecutionInputsAndOutputs",
          "args": {
            "execution": "...",
            "region": "..."
          },
          "result": "queryExecutionInputsAndOutputsResult"
        }
      }
    ]

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
