---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/PredictResponse/
title: PredictResponse \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:26:28.879628+00:00
---

# PredictResponse  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/PredictResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  PredictResponse Stay organized with collections  Save and categorize content based on your preferences. 

Response message for `[PredictionService.Predict](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.endpoints/predict#google.cloud.aiplatform.v1beta1.PredictionService.Predict)`.

Fields  
  
`predictions[]` `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)` The predictions that are the output of the predictions call. The schema of each prediction depends on the type of request.

  * For a generative AI request to a Text Embedding model, see `TextEmbeddingPredictionResult`
  * For a generative AI request to a Multimodal Embedding model, see `VisionEmbeddingModelResult`
  * For a video generation request to a Veo model, see `VideoGenerationModelResult`
  * For a traditional machine learning request to a deployed custom model, the schema of each prediction is defined by the model's `[predictionSchemaUri](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/PredictSchemata#FIELDS.prediction_schema_uri)`.

| `deployedModelId` `string` id of the Endpoint's DeployedModel that served this prediction. | `model` `string` Output only. The resource name of the Model which is deployed as the DeployedModel that this prediction hits. | `modelVersionId` `string` Output only. The version id of the Model which is deployed as the DeployedModel that this prediction hits. | `modelDisplayName` `string` Output only. The `[display name](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.models#Model.FIELDS.display_name)` of the Model which is deployed as the DeployedModel that this prediction hits. | `metadata` `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)` Output only. Request-level metadata returned by the model. The metadata type will be dependent upon the model implementation. | JSON representation  
---  
      
    
    {
      "predictions": [
        value
      ],
      "deployedModelId": string,
      "model": string,
      "modelVersionId": string,
      "modelDisplayName": string,
      "metadata": value
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-12 UTC."],[],[]] 
