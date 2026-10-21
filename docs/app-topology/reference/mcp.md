---
url: https://docs.cloud.google.com/app-topology/reference/mcp/
title: MCP Reference: apptopology.googleapis.com \u00a0|\u00a0 App Topology \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:16:40.940844+00:00
---

# MCP Reference: apptopology.googleapis.com  |  App Topology  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-topology/reference/mcp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ App Topology ](https://docs.cloud.google.com/app-topology)
  * [ APIs & Reference ](https://docs.cloud.google.com/app-topology/apis)



Send feedback 

#  MCP Reference: apptopology.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

Service for generating and retrieving application and resource topologies.

A [Model Context Protocol (MCP) server](https://modelcontextprotocol.io/docs/learn/server-concepts) acts as a proxy between an external service that provides context, data, or capabilities to a Large Language Model (LLM) or AI application. MCP servers connect AI applications to external systems such as databases and web services, translating their responses into a format that the AI application can understand.

### Server Setup

You must [enable MCP servers](https://docs.cloud.google.com/mcp/enable-disable-mcp-servers) and [set up authentication](https://docs.cloud.google.com/mcp/authenticate-mcp) before use. For more information about using Google and Google Cloud remote MCP servers, see [Google Cloud MCP servers overview](https://docs.cloud.google.com/mcp/overview). 

### Server Endpoints

An MCP service endpoint is the network address and communication interface (usually a URL) of the MCP server that an AI application (the Host for the MCP client) uses to establish a secure, standardized connection. It is the point of contact for the LLM to request context, call a tool, or access a resource. Google MCP endpoints can be global or regional.

The App Topology API MCP server has the following global MCP endpoint:

  * https://apptopology.googleapis.com/mcp



## MCP Tools

An [MCP tool](https://modelcontextprotocol.io/legacy/concepts/tools) is a function or executable capability that an MCP server exposes to a LLM or AI application to perform an action in the real world.

### Tools

The apptopology.googleapis.com MCP server has the following tools:

MCP Tools  
---  
`[explore_schema](https://docs.cloud.google.com/app-topology/reference/mcp/tools_list/explore_schema)` |  Explores the topology schema via multi-hop BFS traversal from starting label names within a domain schema.   
`[generate_discovered_resources_topology](https://docs.cloud.google.com/app-topology/reference/mcp/tools_list/generate_discovered_resources_topology)` |  Generate the topology for all discovered (including non-registrable) resources for given project based on the view option and filters. Constructing filters requires valid node labels, edge labels, and properties, which can be retrieved in bulk via `get_schema` or incrementally explored via `explore_schema`.   
`[get_domain](https://docs.cloud.google.com/app-topology/reference/mcp/tools_list/get_domain)` |  Retrieve details about a specific, named topology domain.   
`[get_schema](https://docs.cloud.google.com/app-topology/reference/mcp/tools_list/get_schema)` |  GetSchema returns the complete schema (supported node and edge labels and properties for a domain) to construct filters. Alternatively, explore_schema provides incremental exploration of the topology schema.   
`[list_domains](https://docs.cloud.google.com/app-topology/reference/mcp/tools_list/list_domains)` |  ListDomains method returns all available topology domains in a specific location.   
  
### Get MCP tool specifications

To get the MCP tool specifications for all tools in an MCP server, use the `tools/list` method. The following example demonstrates how to use `curl` to list all tools and their specifications currently available within the MCP server. 

Curl Request  
---  
      
    
    curl --location 'https://apptopology.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
        "method": "tools/list",
        "jsonrpc": "2.0",
        "id": 1
    }'  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
