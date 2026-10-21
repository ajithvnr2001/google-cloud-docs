---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/prediction/grpc/prediction.aiplatform.gdc.goog.v1
title: Package prediction.aiplatform.gdc.goog.v1 \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:13:54.315529+00:00
---

# Package prediction.aiplatform.gdc.goog.v1  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/prediction/grpc/prediction.aiplatform.gdc.goog.v1

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  Package prediction.aiplatform.gdc.goog.v1 Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[PredictionService](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/prediction/grpc/prediction.aiplatform.gdc.goog.v1#prediction.aiplatform.gdc.goog.v1.PredictionService)` (interface)
  * `[PredictRequest](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/prediction/grpc/prediction.aiplatform.gdc.goog.v1#prediction.aiplatform.gdc.goog.v1.PredictRequest)` (message)
  * `[PredictResponse](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/prediction/grpc/prediction.aiplatform.gdc.goog.v1#prediction.aiplatform.gdc.goog.v1.PredictResponse)` (message)
  * `[RawPredictRequest](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/prediction/grpc/prediction.aiplatform.gdc.goog.v1#prediction.aiplatform.gdc.goog.v1.RawPredictRequest)` (message)



## PredictionService

A service for online predictions and explanations.

Predict  
---  
` rpc Predict(`[PredictRequest](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/prediction/grpc/prediction.aiplatform.gdc.goog.v1#prediction.aiplatform.gdc.goog.v1.PredictRequest)`) returns (`[PredictResponse](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/prediction/grpc/prediction.aiplatform.gdc.goog.v1#prediction.aiplatform.gdc.goog.v1.PredictResponse)`) ` Perform an online prediction.  
RawPredict  
---  
` rpc RawPredict(`[RawPredictRequest](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/prediction/grpc/prediction.aiplatform.gdc.goog.v1#prediction.aiplatform.gdc.goog.v1.RawPredictRequest)`) returns (`[HttpBody](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/prediction/rest/HttpBody)`) ` Perform an online prediction with an arbitrary HTTP payload.The response includes the following HTTP headers:

  * `X-Vertex-AI-Endpoint-Id`: ID of the Endpoint that served this prediction.
  * `X-Vertex-AI-Deployed-Model-Id`: ID of the Endpoint's DeployedModel that served this prediction.

  
  
## PredictRequest

Request message for `[PredictionService.Predict](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/prediction/grpc/prediction.aiplatform.gdc.goog.v1#prediction.aiplatform.gdc.goog.v1.PredictionService.Predict)`.

Fields  
---  
`endpoint` |  `string` Required. The name of the Endpoint requested to serve the prediction. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}`  
`instances[]` |  ``[Value](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Value)`` Required. The instances that are the input to the prediction call. A DeployedModel may have an upper limit on the number of instances it supports per request. In case of customer-created Models, the behaviour is as documented by that Model. The schema of any single instance may be specified on the Endpoint's DeployedModels.  
`parameters` |  ``[Value](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Value)`` The parameters that govern the prediction. The schema of the parameters may be specified on the Endpoint's DeployedModels.  
  
## PredictResponse

Response message for `[PredictionService.Predict](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/prediction/grpc/prediction.aiplatform.gdc.goog.v1#prediction.aiplatform.gdc.goog.v1.PredictionService.Predict)`.

Fields  
---  
`predictions[]` |  ``[Value](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Value)`` The predictions that are the output of the predictions call. The schema of any single prediction may be specified on the Endpoint's DeployedModels.  
`deployed_model_id` |  `string` ID of the Endpoint's DeployedModel that served this prediction.  
`model` |  `string` Output only. The resource name of the Model which is deployed as the DeployedModel that this prediction hits.  
`model_version_id` |  `string` Output only. The version ID of the Model which is deployed as the DeployedModel that this prediction hits.  
`model_display_name` |  `string` Output only. The display name of the Model which is deployed as the DeployedModel that this prediction hits.  
`metadata` |  ``[Value](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Value)`` Output only. Request-level metadata returned by the model. The metadata type will be dependent upon the model implementation.  
  
## RawPredictRequest

Request message for `[PredictionService.RawPredict](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/prediction/grpc/prediction.aiplatform.gdc.goog.v1#prediction.aiplatform.gdc.goog.v1.PredictionService.RawPredict)`.

Fields  
---  
`endpoint` |  `string` Required. The name of the Endpoint requested to serve the prediction. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}`  
`http_body` |  ``[HttpBody](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/prediction/rest/HttpBody)`` The prediction input. Supports HTTP headers and arbitrary data payload.A DeployedModel may have an upper limit on the number of instances it supports per request. When this limit it is exceeded for an AutoML model, the `[RawPredict](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/prediction/grpc/prediction.aiplatform.gdc.goog.v1#prediction.aiplatform.gdc.goog.v1.PredictionService.RawPredict)` method returns an error. When this limit is exceeded for a custom-trained model, the behavior varies depending on the model.You can specify the schema for each instance in the PredictSchemata field when you create a Model. This schema applies when you deploy the `Model` as a `DeployedModel` to an Endpoint and use the `RawPredict` method.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-10 UTC."],[],[]] 
