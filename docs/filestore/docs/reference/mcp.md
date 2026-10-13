---
url: https://docs.cloud.google.com/filestore/docs/reference/mcp/
title: MCP Reference: file.googleapis.com \u00a0|\u00a0 Filestore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:55:00.188319+00:00
---

# MCP Reference: file.googleapis.com  |  Filestore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/reference/mcp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Reference ](https://docs.cloud.google.com/filestore/docs/apis)



Send feedback 

#  MCP Reference: file.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

This server provides tools to manage Filestore resources like instances, snapshots, and backups.

A [Model Context Protocol (MCP) server](https://modelcontextprotocol.io/docs/learn/server-concepts) acts as a proxy between an external service that provides context, data, or capabilities to a Large Language Model (LLM) or AI application. MCP servers connect AI applications to external systems such as databases and web services, translating their responses into a format that the AI application can understand.

### Server Setup

You must [enable MCP servers](https://docs.cloud.google.com/mcp/enable-disable-mcp-servers) and [set up authentication](https://docs.cloud.google.com/mcp/authenticate-mcp) before use. For more information about using Google and Google Cloud remote MCP servers, see [Google Cloud MCP servers overview](https://docs.cloud.google.com/mcp/overview). 

### Server Endpoints

An MCP service endpoint is the network address and communication interface (usually a URL) of the MCP server that an AI application (the Host for the MCP client) uses to establish a secure, standardized connection. It is the point of contact for the LLM to request context, call a tool, or access a resource. Google MCP endpoints can be global or regional.

The Cloud Filestore API MCP server has the following global MCP endpoint:

  * https://file.googleapis.com/mcp



## MCP Tools

An [MCP tool](https://modelcontextprotocol.io/legacy/concepts/tools) is a function or executable capability that an MCP server exposes to a LLM or AI application to perform an action in the real world.

### Tools

The file.googleapis.com MCP server has the following tools:

MCP Tools  
---  
`[list_instances](https://docs.cloud.google.com/filestore/docs/reference/mcp/tools_list/list_instances)` |  Lists all Filestore instances.   
`[get_instance](https://docs.cloud.google.com/filestore/docs/reference/mcp/tools_list/get_instance)` |  Gets the details of a specific Filestore instance.   
`[list_snapshots](https://docs.cloud.google.com/filestore/docs/reference/mcp/tools_list/list_snapshots)` |  Lists all snapshots for a specific Filestore instance.   
`[get_snapshot](https://docs.cloud.google.com/filestore/docs/reference/mcp/tools_list/get_snapshot)` |  Gets the details of a specific snapshot.   
`[create_snapshot](https://docs.cloud.google.com/filestore/docs/reference/mcp/tools_list/create_snapshot)` |  Creates a new snapshot of a Filestore instance.   
`[list_backups](https://docs.cloud.google.com/filestore/docs/reference/mcp/tools_list/list_backups)` |  Lists all backups.   
`[get_backup](https://docs.cloud.google.com/filestore/docs/reference/mcp/tools_list/get_backup)` |  Gets the details of a specific backup.   
`[create_backup](https://docs.cloud.google.com/filestore/docs/reference/mcp/tools_list/create_backup)` |  Creates a new backup.   
  
### Get MCP tool specifications

To get the MCP tool specifications for all tools in an MCP server, use the `tools/list` method. The following example demonstrates how to use `curl` to list all tools and their specifications currently available within the MCP server. 

Curl Request  
---  
      
    
                          
    curl --location 'https://file.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
        "method": "tools/list",
        "jsonrpc": "2.0",
        "id": 1
    }'
                          
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-29 UTC."],[],[]] 
