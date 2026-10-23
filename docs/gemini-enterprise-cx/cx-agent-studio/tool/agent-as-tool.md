---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/agent-as-tool/
title: Agent as a tool \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:13:02.028849+00:00
---

# Agent as a tool  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/agent-as-tool/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Agent as a tool Stay organized with collections  Save and categorize content based on your preferences. 

You can use existing agents as tools. This allows an active agent to reuse the capabilities of another agent without handing off the conversation to the other agent. The _agent-as-a-tool_ can be called either synchronously or asynchronously by the active agent.

Use asynchronous behavior when the agent-as-a-tool involves notable latency due to multiple LLM and tool calls. The active agent can call the agent-as-a-tool, and it will perform its work in the background. The active agent can continue the conversation with the end-user while the agent-as-a-tool is working on a response. Once work is completed, the agent-as-a-tool-completes, and the active agent can summarize the findings for the user.

Use synchronous behavior when you simply want to reuse existing agent behavior without handing off the conversation to another agent.

## Configuration

You can configure an agent-as-a-tool using either the normal tool creation button on the right side of the agent builder, or by using the **Create agent as a tool** context menu in a particular agent's title bar.

The tool requires the following configuration items:

  * **Agent** : The target agent for this tool.
  * **Name** : The tool name.
  * **Description** : Optional tool description.
  * **Advanced > Asynchronous**: When enabled (the default), the active agent will continue the session while the tool runs in the background.



It is recommended to [specify a text model for the agent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/agent#agent-settings) being used as a tool when your agent application uses an audio model:

  * This enables more complex workflows due to being able to use larger, slower models while the active agent uses a smaller, faster model.
  * Audio agent applications don't allow you to override the agent's model except when the agent is used as a tool.



## Instructions

When writing instructions for asynchronous tool calls, consider the following:

  * Asynchronous tools can send an immediate "pending" response when starting work. It helps to have your active agent handle this response in instructions.
  * It is helpful to instruct the agent to let the user know that it is working on a response.
  * Instruct the agent to avoid calling the same tool while waiting.
  * The agent-as-a-tool may request additional information from the user.



Sample instructions:
    
    
    * You MUST acknowledge the user's request with a short, conversational
      word or phrase (e.g., 'Okay', 'Got it', 'One second') prior to
      calling asynchronous tools.
    * For tools that execute asynchronously, ignore 'pending' results
      and continue conversing with the user while waiting for the complete result.
    * NEVER notify the user that a function result is 'pending'.
    * Do NOT call the same tool again while waiting for a complete result
      from a previous call of that same tool.
    * If {@TOOL: your_agent_tool} has follow up questions for the user,
      be sure to relay the answers back to the tool.
    

## Limitations

The following limitations apply:

  * An agent can call multiple agent-as-a-tools in parallel but not the same tool in parallel.
  * It is not be possible to assign the tool to the tool's root agent.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
