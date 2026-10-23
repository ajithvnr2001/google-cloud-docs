---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards.experiments.runs/batchCreate/
title: Method: runs.batchCreate \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:56:38.922620+00:00
---

# Method: runs.batchCreate  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards.experiments.runs/batchCreate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: runs.batchCreate Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.tensorboards.experiments.runs.batchCreate

Batch create TensorboardRuns.

### Endpoint

post  `https://{service-endpoint}/v1/{parent}/runs:batchCreate`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`parent` `string` Required. The resource name of the TensorboardExperiment to create the TensorboardRuns in. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}` The parent field in the CreateTensorboardRunRequest messages must match this field.

### Request body

The request body contains data with the following structure: | Fields  
  
`requests[]` `object (`[CreateTensorboardRunRequest](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards.experiments.runs/batchCreate#CreateTensorboardRunRequest)`)` Required. The request message specifying the TensorboardRuns to create. A maximum of 1000 TensorboardRuns can be created in a batch.

### Response body

Response message for `[TensorboardService.BatchCreateTensorboardRuns](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards.experiments.runs/batchCreate#google.cloud.aiplatform.v1.TensorboardService.BatchCreateTensorboardRuns)`. If successful, the response body contains data with the following structure: | Fields  
  
`tensorboardRuns[]` `object (`[TensorboardRun](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards.experiments.runs#TensorboardRun)`)` The created TensorboardRuns. | JSON representation  
---  
      
    
    {
      "tensorboardRuns": [
        {
          object ([TensorboardRun](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards.experiments.runs#TensorboardRun))
        }
      ]
    }  
  
### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `aiplatform.tensorboardRuns.batchCreate`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## CreateTensorboardRunRequest

Request message for `[TensorboardService.CreateTensorboardRun](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards.experiments.runs/create#google.cloud.aiplatform.v1.TensorboardService.CreateTensorboardRun)`.

Fields  
  
`parent` `string` Required. The resource name of the TensorboardExperiment to create the TensorboardRun in. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}` | `tensorboardRun` `object (`[TensorboardRun](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards.experiments.runs#TensorboardRun)`)` Required. The TensorboardRun to create. | `tensorboardRunId` `string` Required. The id to use for the Tensorboard run, which becomes the final component of the Tensorboard run's resource name.This value should be 1-128 characters, and valid characters are `/[a-z][0-9]-/`. | JSON representation  
---  
      
    
    {
      "parent": string,
      "tensorboardRun": {
        object ([TensorboardRun](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards.experiments.runs#TensorboardRun))
      },
      "tensorboardRunId": string
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
