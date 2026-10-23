---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.publishers.models/rawPredict/
title: Method: models.rawPredict \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:58:21.369109+00:00
---

# Method: models.rawPredict  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.publishers.models/rawPredict/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: models.rawPredict Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.publishers.models.rawPredict

Perform an online prediction with an arbitrary HTTP payload.

The response includes the following HTTP headers:

  * `X-Vertex-AI-Endpoint-id`: id of the `[Endpoint](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.endpoints#Endpoint)` that served this prediction.

  * `X-Vertex-AI-Deployed-Model-id`: id of the Endpoint's `[DeployedModel](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.endpoints#DeployedModel)` that served this prediction.




### Endpoint

post  `https://{service-endpoint}/v1beta1/{endpoint}:rawPredict`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`endpoint` `string` Required. The name of the Endpoint requested to serve the prediction. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}`

### Request body

The request body contains data with the following structure: | Fields  
  
`httpBody` `object (`[HttpBody](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/HttpBody)`)` The prediction input. Supports HTTP headers and arbitrary data payload.A `[DeployedModel](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.endpoints#DeployedModel)` may have an upper limit on the number of instances it supports per request. When this limit it is exceeded for an AutoML model, the `[models.rawPredict](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.endpoints/rawPredict#google.cloud.aiplatform.v1beta1.PredictionService.RawPredict)` method returns an error. When this limit is exceeded for a custom-trained model, the behavior varies depending on the model.You can specify the schema for each instance in the `[predictSchemata.instance_schema_uri](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/PredictSchemata#FIELDS.instance_schema_uri)` field when you create a `[Model](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.models#Model)`. This schema applies when you deploy the `Model` as a `DeployedModel` to an `[Endpoint](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.endpoints#Endpoint)` and use the `models.rawPredict` method.

### Response body

If successful, the response is a generic HTTP response whose format is defined by the method.

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `endpoint` resource:

  * `aiplatform.endpoints.predict`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs). Send feedback  Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. Last updated 2026-10-22 UTC. Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
