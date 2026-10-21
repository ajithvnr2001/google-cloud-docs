---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/prediction/rest/PredictResponse/
title: PredictResponse \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:13:54.735062+00:00
---

# PredictResponse  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/prediction/rest/PredictResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  PredictResponse Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Response message for `PredictionService.Predict`.

JSON representation  
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
  
Fields  
---  
`predictions[]` |  `value (`[Value](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Value)` format)` The predictions that are the output of the predictions call. The schema of any single prediction may be specified on the Endpoint's DeployedModels.  
`deployedModelId` |  `string` ID of the Endpoint's DeployedModel that served this prediction.  
`model` |  `string` Output only. The resource name of the Model which is deployed as the DeployedModel that this prediction hits.  
`modelVersionId` |  `string` Output only. The version ID of the Model which is deployed as the DeployedModel that this prediction hits.  
`modelDisplayName` |  `string` Output only. The display name of the Model which is deployed as the DeployedModel that this prediction hits.  
`metadata` |  `value (`[Value](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Value)` format)` Output only. Request-level metadata returned by the model. The metadata type will be dependent upon the model implementation.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-10 UTC."],[],[]] 
