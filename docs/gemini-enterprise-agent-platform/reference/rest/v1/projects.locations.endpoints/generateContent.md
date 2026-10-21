---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.endpoints/generateContent/
title: Method: endpoints.generateContent \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:20:17.922999+00:00
---

# Method: endpoints.generateContent  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.endpoints/generateContent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: endpoints.generateContent Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.endpoints.generateContent

Generate content with multimodal inputs.

### Endpoint

post  `https://{service-endpoint}/v1/{model}:generateContent`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`model` `string` Required. The fully qualified name of the publisher model or tuned model endpoint to use.Publisher model format: `projects/{project}/locations/{location}/publishers/*/models/*`Tuned model endpoint format: `projects/{project}/locations/{location}/endpoints/{endpoint}`

### Request body

The request body contains data with the following structure: | Fields  
  
`contents[]` `object (`[Content](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/Content)`)` Required. The content of the current conversation with the model.For single-turn queries, this is a single instance. For multi-turn queries, this is a repeated field that contains conversation history + latest request. | `cachedContent` `string` Optional. The name of the cached content used as context to serve the prediction. Note: only used in explicit caching, where users can have control over caching (e.g. what content to cache) and enjoy guaranteed cost savings. Format: `projects/{project}/locations/{location}/cachedContents/{cachedContent}` | `tools[]` `object (`[Tool](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.cachedContents#Tool)`)` Optional. A list of `Tools` the model may use to generate the next response.A `Tool` is a piece of code that enables the system to interact with external systems to perform an action, or set of actions, outside of knowledge and scope of the model. | `toolConfig` `object (`[ToolConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.cachedContents#ToolConfig)`)` Optional. Tool config. This config is shared for all tools provided in the request. | `labels` `map (key: string, value: string)` Optional. The labels with user-defined metadata for the request. It is used for billing and reporting only.label keys and values can be no longer than 63 characters (Unicode codepoints) and can only contain lowercase letters, numeric characters, underscores, and dashes. International characters are allowed. label values are optional. label keys must start with a letter. | `safetySettings[]` `object (`[SafetySetting](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/SafetySetting)`)` Optional. Per request settings for blocking unsafe content. Enforced on GenerateContentResponse.candidates. | `modelArmorConfig` `object (`[ModelArmorConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/ModelArmorConfig)`)` Optional. Settings for prompt and response sanitization using the Model Armor service. If supplied, safetySettings must not be supplied. | `generationConfig` `object (`[GenerationConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tuningJobs#GenerationConfig)`)` Optional. Generation config. | `systemInstruction` `object (`[Content](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/Content)`)` Optional. The user provided system instructions for the model. Note: only text should be used in parts and content in each part will be in a separate paragraph.

### Response body

If successful, the response body contains an instance of `[GenerateContentResponse](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/GenerateContentResponse)`. Send feedback  Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. Last updated 2026-05-05 UTC. Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-05 UTC."],[],[]] 
