---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.publishers.models/enableModel/
title: Method: models.enableModel \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:12:10.682397+00:00
---

# Method: models.enableModel  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.publishers.models/enableModel/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: models.enableModel Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.publishers.models.enableModel

Enables model for the project if prerequisites are met (e.g. completed questionnaire and consents, or an active Private Offer).

### Endpoint

post  `https://{service-endpoint}/v1beta1/{parent}/{name}:enableModel`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`parent` `string` Required. The project requesting access for named model. Format: `projects/{project}` | `name` `string` Required. The name of the PublisherModel resource. Format: `publishers/{publisher}/models/{publisherModel}`

### Request body

The request body contains data with the following structure: | Fields  
  
`service  
**(deprecated)**` `string` Optional. The id links the Marketplace listing to the underlying Agent Platform model endpoint. Format: `services/{serviceId}` Format: `services/{serviceId}`

### Response body

Response message for `[ModelGardenService.EnableModel](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.publishers.models/enableModel#google.cloud.aiplatform.v1beta1.ModelGardenService.EnableModel)`. If successful, the response body contains data with the following structure: | Fields  
  
`publisherEndpoint` `string` Output only. The publisher endpoint that the project is enabled for. Format: `projects/{project}/locations/{location}/publishers/{publisher}/models/{publisherModel}` | `enablementState` `enum (`[EnablementState](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.publishers.models/enableModel#EnablementState)`)` Output only. The result of the model enablement. | JSON representation  
---  
      
    
    {
      "publisherEndpoint": string,
      "enablementState": enum ([EnablementState](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.publishers.models/enableModel#EnablementState))
    }  
  
## EnablementState

state of the models.enable response.

Enums  
---  
`ENABLEMENT_STATE_UNSPECIFIED` | The PublisherModel enable status is unclear. The API will default to this value.  
`ENABLEMENT_STATE_SUCCEEDED` | The PublisherModel is enabled successfully.  
`ENABLEMENT_STATE_FAILED` | The PublisherModel is failed to enable  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-09 UTC."],[],[]] 
