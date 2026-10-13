---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.endpoints/directRawPredict/
title: Method: endpoints.directRawPredict \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:20:17.026552+00:00
---

# Method: endpoints.directRawPredict  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.endpoints/directRawPredict/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: endpoints.directRawPredict Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.endpoints.directRawPredict

Perform an unary online prediction request to a gRPC model server for custom containers.

### Endpoint

post  `https://{service-endpoint}/v1/{endpoint}:directRawPredict`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`endpoint` `string` Required. The name of the Endpoint requested to serve the prediction. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}`

### Request body

The request body contains data with the following structure: | Fields  
  
`methodName` `string` Fully qualified name of the API method being invoked to perform predictions.Format: `/namespace.Service/method/` Example: `/tensorflow.serving.PredictionService/endpoints.predict` | `input` `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` The prediction input.A base64-encoded string.

### Response body

Response message for `[PredictionService.DirectRawPredict](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.endpoints/directRawPredict#google.cloud.aiplatform.v1.PredictionService.DirectRawPredict)`. If successful, the response body contains data with the following structure: | Fields  
  
`output` `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` The prediction output.A base64-encoded string. | JSON representation  
---  
      
    
    {
      "output": string
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-04 UTC."],[],[]] 
