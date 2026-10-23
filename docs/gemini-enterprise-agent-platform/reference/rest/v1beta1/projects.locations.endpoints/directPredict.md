---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.endpoints/directPredict/
title: Method: endpoints.directPredict \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:56:32.635436+00:00
---

# Method: endpoints.directPredict  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.endpoints/directPredict/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: endpoints.directPredict Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.endpoints.directPredict

Perform an unary online prediction request to a gRPC model server for Vertex first-party products and frameworks.

### Endpoint

post  `https://{service-endpoint}/v1beta1/{endpoint}:directPredict`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`endpoint` `string` Required. The name of the Endpoint requested to serve the prediction. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}`

### Request body

The request body contains data with the following structure: | Fields  
  
`inputs[]` `object (`[Tensor](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Tensor)`)` The prediction input. | `parameters` `object (`[Tensor](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Tensor)`)` The parameters that govern the prediction.

### Response body

Response message for `[PredictionService.DirectPredict](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.endpoints/directPredict#google.cloud.aiplatform.v1beta1.PredictionService.DirectPredict)`. If successful, the response body contains data with the following structure: | Fields  
  
`outputs[]` `object (`[Tensor](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Tensor)`)` The prediction output. | `parameters` `object (`[Tensor](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Tensor)`)` The parameters that govern the prediction. | JSON representation  
---  
      
    
    {
      "outputs": [
        {
          object ([Tensor](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Tensor))
        }
      ],
      "parameters": {
        object ([Tensor](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Tensor))
      }
    }  
  
### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `endpoint` resource:

  * `aiplatform.endpoints.predict`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
