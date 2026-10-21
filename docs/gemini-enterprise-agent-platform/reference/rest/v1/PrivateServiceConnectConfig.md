---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/PrivateServiceConnectConfig/
title: PrivateServiceConnectConfig \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T17:58:45.554487+00:00
---

# PrivateServiceConnectConfig  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/PrivateServiceConnectConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  PrivateServiceConnectConfig Stay organized with collections  Save and categorize content based on your preferences. 

Represents configuration for private service connect.

Fields  
  
`enablePrivateServiceConnect` `boolean` Required. If true, expose the IndexEndpoint via private service connect. | `projectAllowlist[]` `string` A list of Projects from which the forwarding rule will target the service attachment. | `pscAutomationConfigs[]` `object (`[PSCAutomationConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/PSCAutomationConfig)`)` Optional. List of projects and networks where the PSC endpoints will be created. This field is used by Online Inference(Prediction) only. | `serviceAttachment` `string` Output only. The name of the generated service attachment resource. This is only populated if the endpoint is deployed with PrivateServiceConnect. | JSON representation  
---  
      
    
    {
      "enablePrivateServiceConnect": boolean,
      "projectAllowlist": [
        string
      ],
      "pscAutomationConfigs": [
        {
          object ([PSCAutomationConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/PSCAutomationConfig))
        }
      ],
      "serviceAttachment": string
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-06 UTC."],[],[]] 
