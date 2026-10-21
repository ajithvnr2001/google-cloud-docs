---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/DeployOperationMetadata/
title: DeployOperationMetadata \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:42:49.971386+00:00
---

# DeployOperationMetadata  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/DeployOperationMetadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  DeployOperationMetadata Stay organized with collections  Save and categorize content based on your preferences. 

Runtime operation information for `[ModelGardenService.Deploy](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations/deploy#google.cloud.aiplatform.v1.ModelGardenService.Deploy)`.

Fields  
  
`genericMetadata` `object (`[GenericOperationMetadata](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/GenericOperationMetadata)`)` The operation generic information. | `publisherModel` `string` Output only. The name of the model resource. | `destination` `string` Output only. The resource name of the Location to deploy the model in. Format: `projects/{project}/locations/{location}` | `projectNumber` `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The project number where the deploy model request is sent. | `modelId` `string` Output only. The model id to be used at query time. | JSON representation  
---  
      
    
    {
      "genericMetadata": {
        object ([GenericOperationMetadata](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/GenericOperationMetadata))
      },
      "publisherModel": string,
      "destination": string,
      "projectNumber": string,
      "modelId": string
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-12 UTC."],[],[]] 
