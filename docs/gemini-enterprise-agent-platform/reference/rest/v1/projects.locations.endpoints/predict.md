---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.endpoints/predict/
title: Method: endpoints.predict \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:20:18.588117+00:00
---

# Method: endpoints.predict  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.endpoints/predict/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: endpoints.predict Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.endpoints.predict

Perform an online inference. Use this method to run inference on Google's generative AI models as well as custom models deployed to Gemini Enterprise Agent Platform. This method supports both generative AI tasks (such as image generation, virtual try-on, text generation, and multimodal embeddings) and traditional machine learning tasks (such as classification and regression).

To run inference on a base (non-tuned) Gemini model, see `[endpoints.generateContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.endpoints/generateContent#google.cloud.aiplatform.v1.PredictionService.GenerateContent)`.

### Endpoint

post  `https://{service-endpoint}/v1/{endpoint}:predict`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`endpoint` `string` Required. The resource name of the publisher model or endpoint requested to serve the prediction. For Google models like Embedding or Veo, use the publisher model format. For tuned models or other models deployed to an Agent Platform endpoint, use the endpoint format.

  * Publisher model format: `projects/{project}/locations/{location}/publishers/google/models/{model}`
  * Endpoint format: `projects/{project}/locations/{location}/endpoints/{endpoint}`



### Request body

The request body contains data with the following structure: | Fields  
  
`instances[]` `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)` Required. The instances that are the input to the prediction call. A DeployedModel may have an upper limit on the number of instances it supports per request, and when it is exceeded the prediction call errors in case of AutoML Models, or, in case of customer created Models, the behavior is as documented by that Model. The schema of each instance depends on the type of request.

  * For a generative AI request to a Text Embedding model, see `[TextEmbeddingPredictionInstance](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/TextEmbeddingPredictionInstance)`
  * For a generative AI request to a Multimodal Embedding model, see `[VisionEmbeddingModelInstance](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/VisionEmbeddingModelInstance)`
  * For a video generation request to a Veo model, see `[VideoGenerationModelInstance](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/VideoGenerationModelInstance)`
  * For a traditional machine learning request to a deployed custom model, the schema of any single instance is defined by the model's `[instanceSchemaUri](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/PredictSchemata#FIELDS.instance_schema_uri)`.

| `parameters` `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)` The parameters that govern the prediction. The schema of the parameters depends on the type of request.

  * For a generative AI request to a Text Embedding model, see `[TextEmbeddingPredictionParams](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/TextEmbeddingPredictionParams)`
  * For a generative AI request to a Multimodal Embedding model, see `[VisionEmbeddingModelParams](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/VisionEmbeddingModelParams)`
  * For a video generation request to a Veo model, see `[VideoGenerationModelParams](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/VideoGenerationModelParams)`
  * For a traditional machine learning request to a deployed custom model, the schema of the parameters is defined by the model's `[parametersSchemaUri](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/PredictSchemata#FIELDS.parameters_schema_uri)`.

| `labels` `map (key: string, value: string)` Optional. The user labels for Imagen billing usage only. Only Imagen supports labels. For other use cases, it will be ignored.

### Response body

If successful, the response body contains an instance of `[PredictResponse](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/PredictResponse)`. Send feedback  Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. Last updated 2026-05-07 UTC. Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-07 UTC."],[],[]] 
