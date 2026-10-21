---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.reasoningEngines/executeCode/
title: Method: reasoningEngines.executeCode \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T10:42:40.873584+00:00
---

# Method: reasoningEngines.executeCode  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.reasoningEngines/executeCode/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: reasoningEngines.executeCode Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.reasoningEngines.executeCode

Executes code statelessly.

### Endpoint

post  `https://{service-endpoint}/v1/{name}:executeCode`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`name` `string` Required. The resource name of the sandbox environment to execute. Format: `projects/{project}/locations/{location}/reasoningEngines/{reasoningEngine}`

### Request body

The request body contains data with the following structure: | Fields  
  
`inputs[]` `object (`[Chunk](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/Chunk)`)` Required. The inputs used for the stateless code execution.

### Response body

Response message for `[SandboxEnvironmentExecutionService.ExecuteCode](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.reasoningEngines/executeCode#google.cloud.aiplatform.v1.SandboxEnvironmentExecutionService.ExecuteCode)`. If successful, the response body contains data with the following structure: | Fields  
  
`outputs[]` `object (`[Chunk](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/Chunk)`)` The outputs from the sandbox environment. | JSON representation  
---  
      
    
    {
      "outputs": [
        {
          object ([Chunk](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/Chunk))
        }
      ]
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-10 UTC."],[],[]] 
