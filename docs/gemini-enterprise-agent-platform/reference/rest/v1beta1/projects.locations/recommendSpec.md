---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations/recommendSpec/
title: Method: locations.recommendSpec \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T11:02:33.504227+00:00
---

# Method: locations.recommendSpec  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations/recommendSpec/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: locations.recommendSpec Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.recommendSpec

Gets a Model's spec recommendations. This API is called by UI, SDK, and internal.

### Endpoint

post  `https://{service-endpoint}/v1beta1/{parent}:recommendSpec`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`parent` `string` Required. The resource name of the Location from which to recommend specs. The users must have permission to make a call in the project. Format: `projects/{project}/locations/{location}`.

### Request body

The request body contains data with the following structure: | Fields  
  
`gcsUri` `string` Required. The Google Cloud Storage URI of the custom model, storing weights and config files (which can be used to infer the base model). | `checkMachineAvailability` `boolean` Optional. If true, check machine availability for the recommended regions. Only return the machine spec in regions where the machine is available. | `checkUserQuota` `boolean` Optional. If true, check user quota for the recommended regions. Returns all the machine spec in regions they are available, and also the user quota state for each machine type in each region.

### Response body

Response message for `[ModelService.RecommendSpec](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations/recommendSpec#google.cloud.aiplatform.v1beta1.ModelService.RecommendSpec)`. If successful, the response body contains data with the following structure: | Fields  
  
`baseModel` `string` Output only. The base model used to finetune the custom model. | `recommendations[]` `object (`[Recommendation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations/recommendSpec#Recommendation)`)` Output only. Recommendations of deployment options for the given custom weights model. | `specs[]` `object (`[MachineAndModelContainerSpec](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations/recommendSpec#MachineAndModelContainerSpec)`)` Output only. The machine and model container specs. | JSON representation  
---  
      
    
    {
      "baseModel": string,
      "recommendations": [
        {
          object ([Recommendation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations/recommendSpec#Recommendation))
        }
      ],
      "specs": [
        {
          object ([MachineAndModelContainerSpec](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations/recommendSpec#MachineAndModelContainerSpec))
        }
      ]
    }  
  
## Recommendation

Recommendation of one deployment option for the given custom weights model in one region. Contains the machine and container spec, and user accelerator quota state.

Fields  
  
`region` `string` The region for the deployment spec (machine). | `spec` `object (`[MachineAndModelContainerSpec](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations/recommendSpec#MachineAndModelContainerSpec)`)` Output only. The machine and model container specs. | `userQuotaState` `enum (`[QuotaState](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations/recommendSpec#QuotaState)`)` Output only. The user accelerator quota state. | JSON representation  
---  
      
    
    {
      "region": string,
      "spec": {
        object ([MachineAndModelContainerSpec](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations/recommendSpec#MachineAndModelContainerSpec))
      },
      "userQuotaState": enum ([QuotaState](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations/recommendSpec#QuotaState))
    }  
  
## MachineAndModelContainerSpec

A machine and model container spec.

Fields  
  
`machineSpec` `object (`MachineSpec`)` Output only. The machine spec. | `containerSpec` `object (`[ModelContainerSpec](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/ModelContainerSpec)`)` Output only. The model container spec. | JSON representation  
---  
      
    
    {
      "machineSpec": {
        object (MachineSpec)
      },
      "containerSpec": {
        object ([ModelContainerSpec](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/ModelContainerSpec))
      }
    }  
  
## QuotaState

The user accelerator quota state.

Enums  
---  
`QUOTA_STATE_UNSPECIFIED` | Unspecified quota state. Quota information not available.  
`QUOTA_STATE_USER_HAS_QUOTA` | user has enough accelerator quota for the machine type.  
`QUOTA_STATE_NO_USER_QUOTA` | user does not have enough accelerator quota for the machine type.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-12 UTC."],[],[]] 
