---
url: https://docs.cloud.google.com/workflows/docs/reference/googleapis/aiplatform/v1/projects.locations.batchPredictionJobs/cancel/
title: Method: googleapis.aiplatform.v1.projects.locations.batchPredictionJobs.cancel \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:21:38.939003+00:00
---

# Method: googleapis.aiplatform.v1.projects.locations.batchPredictionJobs.cancel  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/googleapis/aiplatform/v1/projects.locations.batchPredictionJobs/cancel/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Method: googleapis.aiplatform.v1.projects.locations.batchPredictionJobs.cancel Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Cancels a BatchPredictionJob. Starts asynchronous cancellation on the BatchPredictionJob. The server makes the best effort to cancel the job, but success is not guaranteed. Clients can use JobService.GetBatchPredictionJob or other methods to check whether the cancellation succeeded or whether the job completed despite cancellation. On a successful cancellation, the BatchPredictionJob is not deleted;instead its BatchPredictionJob.state is set to `CANCELLED`. Any files already outputted by the job are not deleted.

## Arguments

Parameters  
---  
`name` |  `string` Required. The name of the BatchPredictionJob to cancel. Format: `projects/{project}/locations/{location}/batchPredictionJobs/{batch_prediction_job}`  
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

If successful, the response will be empty.

## Subworkflow snippet

Some fields might be optional or required. To identify required fields, refer to the [API documentation](https://cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.batchPredictionJobs/cancel).

### YAML
    
    
    - cancel:
        call: googleapis.aiplatform.v1.projects.locations.batchPredictionJobs.cancel
        args:
            name: ...
            region: ...
        result: cancelResult

### JSON
    
    
    [
      {
        "cancel": {
          "call": "googleapis.aiplatform.v1.projects.locations.batchPredictionJobs.cancel",
          "args": {
            "name": "...",
            "region": "..."
          },
          "result": "cancelResult"
        }
      }
    ]

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
