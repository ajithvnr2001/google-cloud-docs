---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards.experiments/batchCreate/
title: Method: experiments.batchCreate \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:56:39.703120+00:00
---

# Method: experiments.batchCreate  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards.experiments/batchCreate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: experiments.batchCreate Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.tensorboards.experiments.batchCreate

Batch create TensorboardTimeSeries that belong to a TensorboardExperiment.

### Endpoint

post  `https://{service-endpoint}/v1/{parent}:batchCreate`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`parent` `string` Required. The resource name of the TensorboardExperiment to create the TensorboardTimeSeries in. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}` The TensorboardRuns referenced by the parent fields in the CreateTensorboardTimeSeriesRequest messages must be sub resources of this TensorboardExperiment.

### Request body

The request body contains data with the following structure: | Fields  
  
`requests[]` `object (`[CreateTensorboardTimeSeriesRequest](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards.experiments/batchCreate#CreateTensorboardTimeSeriesRequest)`)` Required. The request message specifying the TensorboardTimeSeries to create. A maximum of 1000 TensorboardTimeSeries can be created in a batch.

### Response body

Response message for `[TensorboardService.BatchCreateTensorboardTimeSeries](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards.experiments/batchCreate#google.cloud.aiplatform.v1.TensorboardService.BatchCreateTensorboardTimeSeries)`. If successful, the response body contains data with the following structure: | Fields  
  
`tensorboardTimeSeries[]` `object (`[TensorboardTimeSeries](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards.experiments.runs.timeSeries#TensorboardTimeSeries)`)` The created TensorboardTimeSeries. | JSON representation  
---  
      
    
    {
      "tensorboardTimeSeries": [
        {
          object ([TensorboardTimeSeries](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards.experiments.runs.timeSeries#TensorboardTimeSeries))
        }
      ]
    }  
  
### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `aiplatform.tensorboardTimeSeries.batchCreate`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## CreateTensorboardTimeSeriesRequest

Request message for `[TensorboardService.CreateTensorboardTimeSeries](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards.experiments.runs.timeSeries/create#google.cloud.aiplatform.v1.TensorboardService.CreateTensorboardTimeSeries)`.

Fields  
  
`parent` `string` Required. The resource name of the TensorboardRun to create the TensorboardTimeSeries in. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}` | `tensorboardTimeSeriesId` `string` Optional. The user specified unique id to use for the TensorboardTimeSeries, which becomes the final component of the TensorboardTimeSeries's resource name. This value should match "[a-z0-9][a-z0-9-]{0, 127}" | `tensorboardTimeSeries` `object (`[TensorboardTimeSeries](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards.experiments.runs.timeSeries#TensorboardTimeSeries)`)` Required. The TensorboardTimeSeries to create. | JSON representation  
---  
      
    
    {
      "parent": string,
      "tensorboardTimeSeriesId": string,
      "tensorboardTimeSeries": {
        object ([TensorboardTimeSeries](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards.experiments.runs.timeSeries#TensorboardTimeSeries))
      }
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
