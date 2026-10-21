---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/AgentInfo/
title: AgentInfo \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T21:28:32.950376+00:00
---

# AgentInfo  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/AgentInfo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  AgentInfo Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Information about an agent involved in the conversation.

JSON representation  
---  
      
    
    {
      "agentId": string,
      "displayName": string,
      "team": string,
      "teams": [
        string
      ],
      "dispositionCode": string,
      "agentType": enum ([Role](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/Role)),
      "location": string
    }  
  
Fields  
---  
`agentId` |  `string` A user-specified string representing the agent.  
`displayName` |  `string` The agent's name.  
`team  
**(deprecated)**` |  `string` This item is deprecated!A user-specified string representing the agent's team. Deprecated in favor of the `teams` field.  
`teams[]` |  `string` User-specified strings representing the agent's teams.  
`dispositionCode` |  `string` A user-provided string indicating the outcome of the agent's segment of the call.  
`agentType` |  `enum (`[Role](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/Role)`)` The agent type, e.g. HUMAN_AGENT.  
`location` |  `string` The agent's location.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
