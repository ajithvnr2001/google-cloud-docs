---
url: https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/AgentCapabilities/
title: AgentCapabilities \u00a0|\u00a0 Data Agents \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:43:03.645365+00:00
---

# AgentCapabilities  |  Data Agents  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/AgentCapabilities/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)
  * [ Reference ](https://docs.cloud.google.com/gemini/data-agents/reference/rest)



Send feedback 

#  AgentCapabilities Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * AgentExtension
    * JSON representation



Defines the A2A feature set supported by the agent

JSON representation  
---  
      
    
    {
      "streaming": boolean,
      "pushNotifications": boolean,
      "extensions": [
        {
          object ([AgentExtension](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/AgentCapabilities#AgentExtension))
        }
      ]
    }  
  
Fields  
---  
`streaming` |  `boolean` If the agent will support streaming responses  
`pushNotifications` |  `boolean` If the agent can send push notifications to the clients webhook  
`extensions[]` |  `object (`[AgentExtension](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/AgentCapabilities#AgentExtension)`)` Extensions supported by this agent.  
  
## AgentExtension

A declaration of an extension supported by an Agent.

JSON representation  
---  
      
    
    {
      "uri": string,
      "description": string,
      "required": boolean,
      "params": {
        object
      }
    }  
  
Fields  
---  
`uri` |  `string` The URI of the extension. Example: "https://developers.google.com/identity/protocols/oauth2"  
`description` |  `string` A description of how this agent uses this extension. Example: "Google OAuth 2.0 authentication"  
`required` |  `boolean` Whether the client must follow specific requirements of the extension. Example: false  
`params` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional configuration for the extension.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
