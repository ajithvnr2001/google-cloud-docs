---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.models/listCheckpoints/
title: Method: models.listCheckpoints \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T02:12:29.460636+00:00
---

# Method: models.listCheckpoints  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.models/listCheckpoints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: models.listCheckpoints Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.models.listCheckpoints

Lists checkpoints of the specified model version.

### Endpoint

get  `https://{service-endpoint}/v1/{name}:listCheckpoints`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`name` `string` Required. The name of the model version to list checkpoints for. `projects/{project}/locations/{location}/models/{model}@{version}` Example: `projects/{project}/locations/{location}/models/{model}@2` or `projects/{project}/locations/{location}/models/{model}@golden` If no version id or alias is specified, the latest version will be used.

### Query parameters

| `pageSize` `integer` Optional. The standard list page size. | `pageToken` `string` Optional. The standard list page token. Typically obtained via `[nextPageToken](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.models/listCheckpoints#body.ListModelVersionCheckpointsResponse.FIELDS.next_page_token)` of the previous `[models.listCheckpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.models/listCheckpoints#google.cloud.aiplatform.v1.ModelService.ListModelVersionCheckpoints)` call.

### Request body

The request body must be empty.

### Response body

Response message for `[ModelService.ListModelVersionCheckpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.models/listCheckpoints#google.cloud.aiplatform.v1.ModelService.ListModelVersionCheckpoints)` If successful, the response body contains data with the following structure: | Fields  
  
`checkpoints[]` `object (`[ModelVersionCheckpoint](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.models/listCheckpoints#ModelVersionCheckpoint)`)` List of Model version checkpoints. | `nextPageToken` `string` A token to retrieve the next page of results. Pass to `[ListModelVersionCheckpointsRequest.page_token](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.models/listCheckpoints#body.QUERY_PARAMETERS.page_token)` to obtain that page. | JSON representation  
---  
      
    
    {
      "checkpoints": [
        {
          object ([ModelVersionCheckpoint](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.models/listCheckpoints#ModelVersionCheckpoint))
        }
      ],
      "nextPageToken": string
    }  
  
## ModelVersionCheckpoint

This item is deprecated!

Describes the machine learning model version checkpoint.

Fields  
  
`checkpointId` `string` The id of the checkpoint. | `epoch` `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The epoch of the checkpoint. | `step` `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The step of the checkpoint. | JSON representation  
---  
      
    
    {
      "checkpointId": string,
      "epoch": string,
      "step": string
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-04 UTC."],[],[]] 
