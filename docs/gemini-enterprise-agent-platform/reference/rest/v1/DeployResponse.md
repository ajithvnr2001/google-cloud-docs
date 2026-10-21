---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/DeployResponse/
title: DeployResponse \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T11:57:58.990467+00:00
---

# DeployResponse  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/DeployResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  DeployResponse Stay organized with collections  Save and categorize content based on your preferences. 

Response message for `[ModelGardenService.Deploy](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations/deploy#google.cloud.aiplatform.v1.ModelGardenService.Deploy)`.

Fields  
  
`publisherModel` `string` Output only. The name of the PublisherModel resource. Format: `publishers/{publisher}/models/{publisherModel}@{versionId}`, or `publishers/hf-{hugging-face-author}/models/{hugging-face-model-name}@001` | `endpoint` `string` Output only. The name of the Endpoint created. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}` | `model` `string` Output only. The name of the Model created. Format: `projects/{project}/locations/{location}/models/{model}` | JSON representation  
---  
      
    
    {
      "publisherModel": string,
      "endpoint": string,
      "model": string
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-12 UTC."],[],[]] 
