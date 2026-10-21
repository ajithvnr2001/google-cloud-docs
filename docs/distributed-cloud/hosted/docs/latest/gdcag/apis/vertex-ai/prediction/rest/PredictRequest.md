---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/prediction/rest/PredictRequest/
title: PredictRequest \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:13:52.755872+00:00
---

# PredictRequest  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/prediction/rest/PredictRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  PredictRequest Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Request message for `PredictionService.Predict`.

JSON representation  
---  
      
    
    {
      "endpoint": string,
      "instances": [
        value
      ],
      "parameters": value
    }  
  
Fields  
---  
`endpoint` |  `string` Required. The name of the Endpoint requested to serve the prediction. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}`  
`instances[]` |  `value (`[Value](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Value)` format)` Required. The instances that are the input to the prediction call. A DeployedModel may have an upper limit on the number of instances it supports per request. In case of customer-created Models, the behaviour is as documented by that Model. The schema of any single instance may be specified on the Endpoint's DeployedModels.  
`parameters` |  `value (`[Value](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Value)` format)` The parameters that govern the prediction. The schema of the parameters may be specified on the Endpoint's DeployedModels.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-10 UTC."],[],[]] 
