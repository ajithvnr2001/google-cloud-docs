---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/express-mode/rest/v1beta1/publishers.models/countTokens/
title: Method: publishers.models.countTokens \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:19:31.327928+00:00
---

# Method: publishers.models.countTokens  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/express-mode/rest/v1beta1/publishers.models/countTokens/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: publishers.models.countTokens Stay organized with collections  Save and categorize content based on your preferences. 

Perform a token count in express mode.

### Endpoint

post  `https://aiplatform.googleapis.com/v1beta1/{model}:countTokens`

### Path parameters

`model` `string` Required. The name of the model requested to perform token counting. Format: `/publishers/google/models/*`

### Request body

The request body contains data with the following structure: | Fields  
  
`model` `string` Optional. The name of the publisher model requested to serve the prediction. Format: `publishers/google/models/*` | `instances[]` `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)` Optional. The instances that are the input to token counting call. Schema is identical to the prediction schema of the underlying model. | `contents[]` `object (`[Content](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/Content)`)` Optional. Input content. | `tools[]` `object (`[Tool](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.cachedContents#Tool)`)` Optional. A list of `Tools` the model may use to generate the next response.A `Tool` is a piece of code that enables the system to interact with external systems to perform an action, or set of actions, outside of knowledge and scope of the model. | `systemInstruction` `object (`[Content](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/Content)`)` Optional. The user provided system instructions for the model. Note: only text should be used in parts and content in each part will be in a separate paragraph. | `generationConfig` `object (`[GenerationConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/GeminiExample#GenerationConfig)`)` Optional. Generation config that the model will use to generate the response.

### Response body

If successful, the response body contains an instance of `[CountTokensResponse](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/CountTokensResponse)`. Send feedback  Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. Last updated 2026-07-13 UTC. Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-13 UTC."],[],[]] 
