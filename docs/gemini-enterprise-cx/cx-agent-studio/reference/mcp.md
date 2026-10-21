---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/
title: MCP Reference: ces.googleapis.com \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:58:36.242723+00:00
---

# MCP Reference: ces.googleapis.com  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  MCP Reference: ces.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

MCP server for Gemini Enterprise for Customer Experience API

A [Model Context Protocol (MCP) server](https://modelcontextprotocol.io/docs/learn/server-concepts) acts as a proxy between an external service that provides context, data, or capabilities to a Large Language Model (LLM) or AI application. MCP servers connect AI applications to external systems such as databases and web services, translating their responses into a format that the AI application can understand.

### Server Setup

You must [enable MCP servers](https://docs.cloud.google.com/mcp/enable-disable-mcp-servers) and [set up authentication](https://docs.cloud.google.com/mcp/authenticate-mcp) before use. For more information about using Google and Google Cloud remote MCP servers, see [Google Cloud MCP servers overview](https://docs.cloud.google.com/mcp/overview). 

### Server Endpoints

An MCP service endpoint is the network address and communication interface (usually a URL) of the MCP server that an AI application (the Host for the MCP client) uses to establish a secure, standardized connection. It is the point of contact for the LLM to request context, call a tool, or access a resource. Google MCP endpoints can be global or regional.

The Gemini Enterprise for Customer Experience API MCP server has the following global MCP endpoint:

  * https://ces.googleapis.com/mcp



## MCP Tools

An [MCP tool](https://modelcontextprotocol.io/legacy/concepts/tools) is a function or executable capability that an MCP server exposes to a LLM or AI application to perform an action in the real world.

### Tools

The ces.googleapis.com MCP server has the following tools:

MCP Tools  
---  
`[list_apps](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps)` |  Lists apps in the given project and location.   
`[get_app](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_app)` |  Gets details of the specified app.   
`[create_app](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_app)` |  Creates a new app in the given project and location.   
`[update_app](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/update_app)` |  Updates the specified app. Make sure to always pass an update mask in the input.   
`[delete_app](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/delete_app)` |  Deletes the specified app.   
`[list_agents](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents)` |  Lists agents in the given app.   
`[get_agent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_agent)` |  Gets details of the specified agent.   
`[create_agent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_agent)` |  Creates a new agent in the given app.   
`[update_agent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/update_agent)` |  Updates the specified agent. Make sure to always pass an update mask in the input.   
`[delete_agent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/delete_agent)` |  Deletes the specified agent.   
`[list_tools](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools)` |  Lists tools in the given app.   
`[get_tool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_tool)` |  Gets details of the specified tool.   
`[create_tool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_tool)` |  Creates a new tool in the given app.   
`[update_tool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/update_tool)` |  Updates the specified tool. Make sure to always pass an update mask in the input.   
`[delete_tool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/delete_tool)` |  Deletes the specified tool.   
`[list_guardrails](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_guardrails)` |  Lists guardrails in the given app.   
`[get_guardrail](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_guardrail)` |  Gets details of the specified guardrail.   
`[create_guardrail](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_guardrail)` |  Creates a new guardrail in the given app.   
`[update_guardrail](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/update_guardrail)` |  Updates the specified guardrail. Make sure to always pass an update mask in the input.   
`[delete_guardrail](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/delete_guardrail)` |  Deletes the specified guardrail.   
`[list_deployments](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_deployments)` |  Lists deployments in the given app.   
`[get_deployment](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_deployment)` |  Gets details of the specified deployment.   
`[create_deployment](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_deployment)` |  Creates a new deployment in the given app.   
`[update_deployment](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/update_deployment)` |  Updates the specified deployment. Make sure to always pass an update mask in the input.   
`[delete_deployment](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/delete_deployment)` |  Deletes the specified deployment.   
`[list_toolsets](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_toolsets)` |  Lists toolsets in the given app.   
`[get_toolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_toolset)` |  Gets details of the specified toolset.   
`[create_toolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_toolset)` |  Creates a new toolset in the given app.   
`[update_toolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/update_toolset)` |  Updates the specified toolset. Make sure to always pass an update mask in the input.   
`[delete_toolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/delete_toolset)` |  Deletes the specified toolset.   
`[list_app_versions](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions)` |  Lists all app versions in the given app.   
`[get_app_version](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_app_version)` |  Gets details of the specified app version.   
`[create_app_version](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_app_version)` |  Creates a new app version in the given app.   
`[delete_app_version](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/delete_app_version)` |  Deletes the specified app version.   
`[restore_app_version](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/restore_app_version)` |  Restores the specified app version.   
`[list_changelogs](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_changelogs)` |  Lists changelogs in the given app.   
`[get_changelog](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_changelog)` |  Gets details of the specified changelog.   
`[start_export_app](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/start_export_app)` |  Starts to export a CES app   
`[start_import_app](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/start_import_app)` |  Starts to import a CES app   
`[run_evaluation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/run_evaluation)` |  Runs an evaluation for a CES app   
`[create_evaluation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation)` |  Creates a new evaluation.   
`[create_evaluation_dataset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_evaluation_dataset)` |  Creates a new evaluation dataset.   
`[delete_evaluation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/delete_evaluation)` |  Deletes the specified evaluation.   
`[delete_evaluation_dataset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/delete_evaluation_dataset)` |  Deletes the specified evaluation dataset.   
`[generate_evaluation_from_conversation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/generate_evaluation_from_conversation)` |  Generates an evaluation from a conversation.   
`[get_evaluation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_evaluation)` |  Gets details of the specified evaluation.   
`[get_evaluation_dataset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_evaluation_dataset)` |  Gets details of the specified evaluation dataset.   
`[get_evaluation_result](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_evaluation_result)` |  Gets details of the specified evaluation result.   
`[get_evaluation_run](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_evaluation_run)` |  Gets details of the specified evaluation run.   
`[list_evaluation_datasets](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_evaluation_datasets)` |  Lists evaluation datasets.   
`[list_evaluation_results](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_evaluation_results)` |  Lists evaluation results.   
`[list_evaluation_runs](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_evaluation_runs)` |  Lists evaluation runs.   
`[list_evaluations](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_evaluations)` |  Lists evaluations.   
`[update_evaluation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/update_evaluation)` |  Updates the specified evaluation. Make sure to always pass an update mask in the input.   
`[update_evaluation_dataset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/update_evaluation_dataset)` |  Updates the specified evaluation dataset Make sure to always pass an update mask in the input.   
`[delete_evaluation_result](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/delete_evaluation_result)` |  Deletes the specified evaluation result.   
`[delete_evaluation_run](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/delete_evaluation_run)` |  Deletes the specified evaluation run.   
`[get_conversation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_conversation)` |  Gets details of the specified conversation.   
`[list_conversations](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_conversations)` |  Lists conversations.   
`[get_operation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_operation)` |  Gets the status of a long-running operation.**_Usage_** Some tools (for example, `run_evaluation`) return a long-running operation. You can use this tool to get the status of the operation. It can be called repeatedly to poll the status of a long running operation**Parameters** * `name`: The name of the operation to get. * `name` should be the name returned by the tool that initiated the operation. * `name` should be in the format of `projects/{project}/locations/{location}/operations/{operation}`.  
  
### Get MCP tool specifications

To get the MCP tool specifications for all tools in an MCP server, use the `tools/list` method. The following example demonstrates how to use `curl` to list all tools and their specifications currently available within the MCP server. 

Curl Request  
---  
      
    
    curl --location 'https://ces.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
        "method": "tools/list",
        "jsonrpc": "2.0",
        "id": 1
    }'  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-25 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-25 UTC."],[],[]] 
