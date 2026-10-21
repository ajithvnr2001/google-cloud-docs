---
url: https://docs.cloud.google.com/agent-registry/reference/mcp/
title: MCP Reference: agentregistry.googleapis.com \u00a0|\u00a0 Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:06:27.508908+00:00
---

# MCP Reference: agentregistry.googleapis.com  |  Agent Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/reference/mcp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Reference ](https://docs.cloud.google.com/agent-registry/apis)



Send feedback 

#  MCP Reference: agentregistry.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

MCP server which exposes AgentRegistry APIs.

A [Model Context Protocol (MCP) server](https://modelcontextprotocol.io/docs/learn/server-concepts) acts as a proxy between an external service that provides context, data, or capabilities to a Large Language Model (LLM) or AI application. MCP servers connect AI applications to external systems such as databases and web services, translating their responses into a format that the AI application can understand.

### Server Setup

You must [enable MCP servers](https://docs.cloud.google.com/mcp/enable-disable-mcp-servers) and [set up authentication](https://docs.cloud.google.com/mcp/authenticate-mcp) before use. For more information about using Google and Google Cloud remote MCP servers, see [Google Cloud MCP servers overview](https://docs.cloud.google.com/mcp/overview). 

### Server Endpoints

An MCP service endpoint is the network address and communication interface (usually a URL) of the MCP server that an AI application (the Host for the MCP client) uses to establish a secure, standardized connection. It is the point of contact for the LLM to request context, call a tool, or access a resource. Google MCP endpoints can be global or regional.

The Agent Registry API MCP server has the following global MCP endpoint:

  * https://agentregistry.googleapis.com/mcp



## MCP Tools

An [MCP tool](https://modelcontextprotocol.io/legacy/concepts/tools) is a function or executable capability that an MCP server exposes to a LLM or AI application to perform an action in the real world.

### Tools

The agentregistry.googleapis.com MCP server has the following tools:

MCP Tools  
---  
`[list_agents](https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/list_agents)` |  Return a paginated list of agents within a specified Google Cloud project and location. Use this to enumerate all agents or filter by basic resource attributes. Don't use this for natural language discovery; use search_agents instead.   
`[search_agents](https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/search_agents)` |  Perform a keyword or prefix search to discover agents within a specific project and location. Use this when you need to find an agent based on natural language queries, specific skills, tags, or descriptions.   
`[get_agent](https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/get_agent)` |  Retrieve the full metadata and configuration details of a specific agent using its unique resource name. Use this when you already know the agent's ID and need to inspect its capabilities, protocols, or endpoints.   
`[list_endpoints](https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/list_endpoints)` |  Return a paginated list of registered endpoints accessed by agents in a given project and location.   
`[get_endpoint](https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/get_endpoint)` |  Retrieve details of a single registered endpoint using its unique resource name, including its connection interfaces and protocol bindings.   
`[list_mcp_servers](https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/list_mcp_servers)` |  Return a paginated list of MCP servers within a specified Google Cloud project and location. Use this to enumerate servers. For keyword discovery, use search_mcp_servers instead.   
`[search_mcp_servers](https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/search_mcp_servers)` |  Perform a keyword or prefix search to discover MCP servers. Use this to find servers based on the specific tools they offer, their descriptions, or natural language queries.   
`[get_mcp_server](https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/get_mcp_server)` |  Retrieve the full metadata of a specific MCP server using its unique resource name. Use this to inspect the exact tools and schemas exposed by a known server.   
`[list_services](https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/list_services)` |  List services in a given project and location. A service can represent a manually onboarded MCP server, agent or REST endpoint.   
`[get_service](https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/get_service)` |  Retrieve a specific service record. A service can represent a manually onboarded MCP server, agent or REST endpoint. This shows the underlying registration specification used to manually onboard a resource.   
`[create_service](https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/create_service)` |  Manually register a new custom workload by creating a Service resource. A service can represent a manually onboarded MCP server, agent or REST endpoint. Use this to onboard third-party agents, remote MCP servers, or REST endpoints by providing their specification.   
`[update_service](https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/update_service)` |  Update the specification or parameters of an existing service. A service can represent a manually onboarded MCP server, agent or REST endpoint. Use this to patch an uploaded Agent Card, MCP tool specification, or endpoint bindings.   
`[delete_service](https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/delete_service)` |  Delete a service record, effectively deregistering the manually onboarded agent, MCP server, or REST endpoint from the registry.   
`[list_bindings](https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/list_bindings)` |  Return a paginated list of bindings within a specified Google Cloud project and location.   
`[get_binding](https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/get_binding)` |  Retrieve details of a single binding using its unique resource name.   
`[create_binding](https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/create_binding)` |  Create a new binding between an agent and another resource (agent, MCP server, or endpoint).   
`[update_binding](https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/update_binding)` |  Update the specification or parameters of an existing binding.   
`[delete_binding](https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/delete_binding)` |  Delete a binding record, effectively removing the connection between resources.   
`[fetch_available_bindings](https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/fetch_available_bindings)` |  Fetch available bindings for a given source resource.   
`[get_operation](https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/get_operation)` |  Gets the latest state of a long-running operation.   
  
### Get MCP tool specifications

To get the MCP tool specifications for all tools in an MCP server, use the `tools/list` method. The following example demonstrates how to use `curl` to list all tools and their specifications currently available within the MCP server. 

Curl Request  
---  
      
    
    curl --location 'https://agentregistry.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
        "method": "tools/list",
        "jsonrpc": "2.0",
        "id": 1
    }'  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-17 UTC."],[],[]] 
