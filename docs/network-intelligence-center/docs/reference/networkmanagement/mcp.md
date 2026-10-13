---
url: https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/
title: MCP Reference: networkmanagement.googleapis.com \u00a0|\u00a0 Network Intelligence Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:22:45.652696+00:00
---

# MCP Reference: networkmanagement.googleapis.com  |  Network Intelligence Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Reference ](https://docs.cloud.google.com/network-intelligence-center/docs/apis)



Send feedback 

#  MCP Reference: networkmanagement.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

A [Model Context Protocol (MCP) server](https://modelcontextprotocol.io/docs/learn/server-concepts) acts as a proxy between an external service that provides context, data, or capabilities to a Large Language Model (LLM) or AI application. MCP servers connect AI applications to external systems such as databases and web services, translating their responses into a format that the AI application can understand.

### Server Setup

You must [enable MCP servers](https://docs.cloud.google.com/mcp/enable-disable-mcp-servers) and [set up authentication](https://docs.cloud.google.com/mcp/authenticate-mcp) before use. For more information about using Google and Google Cloud remote MCP servers, see [Google Cloud MCP servers overview](https://docs.cloud.google.com/mcp/overview). 

MCP Server for Network Management (Connectivity Tests).

### Server Endpoints

An MCP service endpoint is the network address and communication interface (usually a URL) of the MCP server that an AI application (the Host for the MCP client) uses to establish a secure, standardized connection. It is the point of contact for the LLM to request context, call a tool, or access a resource. Google MCP endpoints can be global or regional.

The networkmanagement.googleapis.com MCP server has the following MCP endpoint:

  * https://networkmanagement.googleapis.com/mcp



## MCP Tools

An [MCP tool](https://modelcontextprotocol.io/legacy/concepts/tools) is a function or executable capability that an MCP server exposes to a LLM or AI application to perform an action in the real world.

The networkmanagement.googleapis.com MCP server has the following tools:

MCP Tools  
---  
[create_connectivity_test](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test) |  Creates and runs a Connectivity Test from the source to the destination endpoint. Test runs are billable after the project exceeds its free limit. Note that only test runs with results other than 'UNDETERMINED' are billable. AI agents should poll for results using get_connectivity_test and delete the test resource using delete_connectivity_test after that.   
[get_connectivity_test](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/get_connectivity_test) |  Gets the details of a specific Connectivity Test.   
[list_connectivity_tests](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/list_connectivity_tests) |  Lists all Connectivity Tests owned by a project.   
[delete_connectivity_test](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/delete_connectivity_test) |  Deletes a specific Connectivity Test.   
  
### Get MCP tool specifications

To get the MCP tool specifications for all tools in an MCP server, use the `tools/list` method. The following example demonstrates how to use `curl` to list all tools and their specifications currently available within the MCP server. 

Curl Request  
---  
      
    
    curl --location 'https://networkmanagement.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
        "method": "tools/list",
        "jsonrpc": "2.0",
        "id": 1
    }'
                          
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-17 UTC."],[],[]] 
