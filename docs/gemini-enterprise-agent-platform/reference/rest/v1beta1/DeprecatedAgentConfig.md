---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/DeprecatedAgentConfig/
title: DeprecatedAgentConfig \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T07:39:13.162588+00:00
---

# DeprecatedAgentConfig  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/DeprecatedAgentConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  DeprecatedAgentConfig Stay organized with collections  Save and categorize content based on your preferences. 

This item is deprecated!

Deprecated: Use `google.cloud.aiplatform.master.AgentConfig` in `agentEvalData` instead. Configuration for an Agent.

Fields  
  
`agentId` `string` Optional. Unique identifier of the agent. This id is used to refer to this agent, e.g., in AgentEvent.author, or in the `subAgents` field. It must be unique within the `agents` map. | `agentType` `string` Optional. The type or class of the agent (e.g., "LlmAgent", "RouterAgent", "ToolUseAgent"). Useful for the autorater to understand the expected behavior of the agent. | `description` `string` Optional. A high-level description of the agent's role and responsibilities. Critical for evaluating if the agent is routing tasks correctly. | `subAgents[]` `string` Optional. The list of valid agent IDs (names) that this agent can delegate to. This defines the directed edges in the agent system graph topology. | `developerInstruction` `object (`[InstanceData](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/InstanceData)`)` Optional. Contains instructions from the developer for the agent. Can be static or a dynamic prompt template used with the `AgentEvent.state_delta` field. | `tools_data` `Union type`  
  
Data for the tools available to the agent. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`toolsText` `string` A JSON string containing a list of tools available to an agent with info such as name, description, parameters and required parameters. | `tools` `object (`[Tools](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/DeprecatedAgentConfig#Tools)`)` List of tools. End of mutually exclusive fields. | JSON representation  
---  
      
    
    {
      "agentId": string,
      "agentType": string,
      "description": string,
      "subAgents": [
        string
      ],
      "developerInstruction": {
        object ([InstanceData](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/InstanceData))
      },
    
      // tools_data
      "toolsText": string,
      "tools": {
        object ([Tools](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/DeprecatedAgentConfig#Tools))
      }
      // Union type
    }  
  
## Tools

Represents a list of tools for an agent.

Fields  
  
`tool[]` `object (`[Tool](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/GeminiExample#Tool)`)` Optional. List of tools: each tool can have multiple function declarations. | JSON representation  
---  
      
    
    {
      "tool": [
        {
          object ([Tool](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/GeminiExample#Tool))
        }
      ]
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
