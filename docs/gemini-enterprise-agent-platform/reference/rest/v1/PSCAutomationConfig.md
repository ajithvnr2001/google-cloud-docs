---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/PSCAutomationConfig/
title: PSCAutomationConfig \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:40:22.869950+00:00
---

# PSCAutomationConfig  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/PSCAutomationConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  PSCAutomationConfig Stay organized with collections  Save and categorize content based on your preferences. 

PSC config that is used to automatically create PSC endpoints in the user projects.

Fields  
  
`projectId` `string` Required. Project id used to create forwarding rule. | `network` `string` Required. The full name of the Google Compute Engine [network](https://cloud.google.com/compute/docs/networks-and-firewalls#networks). [Format](https://cloud.google.com/compute/docs/reference/rest/v1/networks/get): `projects/{project}/global/networks/{network}`. | `ipAddress` `string` Output only. IP address rule created by the PSC service automation. | `forwardingRule` `string` Output only. Forwarding rule created by the PSC service automation. | `state` `enum (`[PSCAutomationState](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/PSCAutomationConfig#PSCAutomationState)`)` Output only. The state of the PSC service automation. | `errorMessage` `string` Output only. Error message if the PSC service automation failed. | JSON representation  
---  
      
    
    {
      "projectId": string,
      "network": string,
      "ipAddress": string,
      "forwardingRule": string,
      "state": enum ([PSCAutomationState](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/PSCAutomationConfig#PSCAutomationState)),
      "errorMessage": string
    }  
  
## PSCAutomationState

The state of the PSC service automation.

Enums  
---  
`PSC_AUTOMATION_STATE_UNSPECIFIED` | Should not be used.  
`PSC_AUTOMATION_STATE_SUCCESSFUL` | The PSC service automation is successful.  
`PSC_AUTOMATION_STATE_FAILED` | The PSC service automation has failed.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-06 UTC."],[],[]] 
