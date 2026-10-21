---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models/get/
title: Method: models.get \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T16:50:57.857026+00:00
---

# Method: models.get  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models/get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: models.get Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : publishers.models.get

Gets a Model Garden publisher model.

### Endpoint

get  `https://{service-endpoint}/v1beta1/{name}`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`name` `string` Required. The name of the PublisherModel resource. Format: `publishers/{publisher}/models/{publisherModel}`

### Query parameters

| `languageCode` `string` Optional. The IETF BCP-47 language code representing the language in which the publisher model's text information should be written in. | `view` `enum (`[PublisherModelView](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/PublisherModelView)`)` Optional. PublisherModel view specifying which fields to read. | `isHuggingFaceModel` `boolean` Optional. Boolean indicates whether the requested model is a Hugging Face model. | `huggingFaceToken` `string` Optional. token used to access Hugging Face gated models. | `includeEquivalentModelGardenModelDeploymentConfigs` `boolean` Optional. Whether to cnclude the deployment configs from the equivalent Model Garden model if the requested model is a Hugging Face model.

### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[PublisherModel](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models#PublisherModel)`. Send feedback  Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. Last updated 2026-05-04 UTC. Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-04 UTC."],[],[]] 
