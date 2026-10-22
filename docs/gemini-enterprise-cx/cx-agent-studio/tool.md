---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/
title: Tools \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:55:45.084046+00:00
---

# Tools  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Tools Stay organized with collections  Save and categorize content based on your preferences. 

Tools are used to connect your agent to external systems or inline code supplied to the agent. This allows your agent to interact with other systems to fetch, update, format, or analyze information. Sections on this page describe various types of tools that are supported.

## Create a tool

To create a tool:

  1. Click the tool icon on the right side of the agent builder.
  2. Select a tool type (see descriptions of tool types in this document).
  3. Provide the requested information for the tool.
  4. Use snake case for the tool name.
  5. Tool descriptions are supplied to agent models.



## Use a tool in an agent

After creating a tool, you need to instruct a particular agent to use the tool.

  1. Hover over an agent.
  2. Click **Add tool**.
  3. Select a tool.
  4. Describe how the tool should be used in your agent instructions.



## Test a tool

Before using a tool in your agent, you can test the tool in the console:

  1. Open the tool panel.
  2. Click the **Test Tool** button at the top of the panel.
  3. Provide input for the tool as defined by the tool schema. For example, if the schema is JSON with `place` and `city` properties, you could use the following input:
         
         {
           "place": "automobile repair center",
           "city": "austin texas"
         }
         

  4. Click **Submit**. The tool is executed with the input, and the output is populated.




After directly testing the tool, you can also test the tool by using [Preview agent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/preview-agent).

## Available tools

The following tools are available:

Tool | Description  
---|---  
[A2A Protocol](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/a2a-protocol) | Connect your agent to external agents using the A2A messaging standard. (Preview)  
[Agent as a tool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/agent-as-tool) | Reuse capabilities of agents without handing off to another agent.  
[Client function tools](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/function) | Code tools that are executed on the client side, not by the agent.  
[Confluence tools](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/confluence) | Connect your agent to a Confluence instance.  
[Data store tools](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/data-store) | Provide AI-generated agent responses based on website content and uploaded data.  
[File search tools](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/file) | Upload file or provide RAG knowledge base to an agent.  
[Google Maps tools](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/google-maps) | Connect your agent to Google Maps. (Preview)  
[Google Search tools](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/search) | Connect your agent the power of grounding with Google Search.  
[Integration Connector tools](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/connector) | Create tools that utilize your configured Connections.  
[Jira tools](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/jira) | Connect your agent to a Jira instance.  
[MCP tools](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/mcp) | Connect to a MCP server.  
[OpenAPI tools](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/open-api) | Connect to an external API using an OpenAPI schema.  
[Python code tools](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/python) | Provide Python code as a tool for your agent.  
[Salesforce tools](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/salesforce) | Connect your agent to a Salesforce instance.  
[Service Now tools](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/service-now) | Connect your agent to a Service Now instance.  
[SharePoint tools](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/sharepoint) | Connect your agent to a SharePoint instance.  
[System tools](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/system) | Built-in tools that can be used by the agent to perform common tasks.  
[Widget tools](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/widget) | Flexible widget tools to create rich user interactions.  
  
## Execution type

Tools support two execution types: _asynchronous_ (non-blocking) and _synchronous_ (blocking). Selecting the appropriate execution type depends on the latency of the tool and the desired agent experience. This setting is available in the **Advanced** tab of tool configuration.

### Synchronous execution type

This type should be used when the tool execution should block agent response generation until the tool response is available. The agent will not generate any response until the tool response is available. These tools should ideally have low latency (less than 5 seconds) to keep overall agent response latency low.

### Asynchronous execution type

This type should be used for non-blocking execution of tools. When a tool call is triggered, the agent will proceed with a "pending" response. The agent can continue talking to the user while the tool response is being fetched. Once the response is available, it is added to the context the next time an agent response is generated. Ideally used for tools with 5-60 second response latencies.

Conversation flow for asynchronous execution type:

  1. **Agent triggers function call** : The agent triggers a function call and is waiting for response. For example, invoke order status tool.
  2. **Tool pending response** : The tool immediately returns a `function_response` containing a pending status, such as `"status": "pending"`.
  3. **Agent handles pending tool** : The agent should be instructed to handle pending responses as desired. Example instruction: "Ask the user if they have any other questions while you are fetching order status". Example agent response: "Is there anything else I can do for you while I fetch your order status?".
  4. **Agent handles final response** : The actual tool response is available for the agent. This will be included as a context tag. For example:
         
         <context>function [<tool_name>] completed with response <response JSON></context>
         




## Best practices

Use the following best practices for tools:

  * Always write semantically meaningful tool names that are relevant to the task they perform.
  * Always provide high quality descriptions of your tools and the task or tasks they are capable of achieving.
  * For asynchronous tools, include detailed instructions for the following scenarios: 
    * Let the agent know that  is an asynchronous tool and will initially return a pending response.
    * Include instructions for how the agent should respond when the tool returns "pending".
    * Include instructions for how the agent should respond when the actual tool response is available.
    * Include instructions for how the agent should respond if the tool returns an error.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
