---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations/deployPublisherModel/
title: Method: locations.deployPublisherModel \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:43:35.849332+00:00
---

# Method: locations.deployPublisherModel  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations/deployPublisherModel/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: locations.deployPublisherModel Stay organized with collections  Save and categorize content based on your preferences. 

This item is deprecated!

**Full name** : projects.locations.deployPublisherModel

Deploys publisher models.

### Endpoint

post  `https://{service-endpoint}/v1beta1/{destination}:deployPublisherModel`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`destination` `string` Required. The resource name of the Location to deploy the model in. Format: `projects/{project}/locations/{location}`

### Request body

The request body contains data with the following structure: | Fields  
  
`model` `string` Required. The model to deploy. Format: 1. `publishers/{publisher}/models/{publisherModel}@{versionId}`, or `publishers/hf-{hugging-face-author}/models/{hugging-face-model-name}@001`. 2. Hugging Face model id like `google/gemma-2-2b-it`. 3. Custom model Google Cloud Storage URI like `gs://bucket`. 4. Custom model zip file like `https://example.com/a.zip`. | `endpointDisplayName` `string` Optional. The user-specified display name of the endpoint. If not set, a default name will be used. | `dedicatedResources` `object (`[DedicatedResources](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/DedicatedResources)`)` Optional. The dedicated resources to use for the endpoint. If not set, the default resources will be used. | `modelDisplayName` `string` Optional. The user-specified display name of the uploaded model. If not set, a default name will be used. | `huggingFaceAccessToken` `string` Optional. The Hugging Face read access token used to access the model artifacts of gated models. | `acceptEula` `boolean` Optional. Whether the user accepts the End user License Agreement (EULA) for the model.

### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ListOperationsResponse#Operation)`. Send feedback  Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. Last updated 2026-05-04 UTC. Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-04 UTC."],[],[]] 
