---
url: https://docs.cloud.google.com/database-center/docs/reference/mcp/
title: MCP Reference: databasecenter.googleapis.com \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:51:30.957953+00:00
---

# MCP Reference: databasecenter.googleapis.com  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-center/docs/reference/mcp/

  * [ Reference ](https://docs.cloud.google.com/database-center/docs/reference)



#  MCP Reference: databasecenter.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

A [Model Context Protocol (MCP) server](https://modelcontextprotocol.io/docs/learn/server-concepts) acts as a proxy between an external service that provides context, data, or capabilities to a Large Language Model (LLM) or AI application. MCP servers connect AI applications to external systems such as databases and web services, translating their responses into a format that the AI application can understand.

### Server Setup

You must [enable MCP servers](https://docs.cloud.google.com/mcp/enable-disable-mcp-servers) and [set up authentication](https://docs.cloud.google.com/mcp/authenticate-mcp) before use. For more information about using Google and Google Cloud remote MCP servers, see [Google Cloud MCP servers overview](https://docs.cloud.google.com/mcp/overview). 

Database Center API for MCP

### Server Endpoints

An MCP service endpoint is the network address and communication interface (usually a URL) of the MCP server that an AI application (the Host for the MCP client) uses to establish a secure, standardized connection. It is the point of contact for the LLM to request context, call a tool, or access a resource. Google MCP endpoints can be global or regional.

The databasecenter.googleapis.com MCP server has the following MCP endpoint:

  * https://databasecenter.googleapis.com/mcp



## MCP Tools

An [MCP tool](https://modelcontextprotocol.io/legacy/concepts/tools) is a function or executable capability that an MCP server exposes to a LLM or AI application to perform an action in the real world.

The databasecenter.googleapis.com MCP server has the following tools:

MCP Tools  
---  
[list_products](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_products) |  Provides a list of all possible database products which can be used to filter database resources.   
[list_fleet_inventory](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_inventory) |  This tool retrieves aggregated statistics and inventory information about the database resources. It can group the results by various dimensions like product type, engine, location, etc. This is useful for understanding the overall composition and distribution of the database fleet.   
[list_fleet_health_issues](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_health_issues) |  This tool provides statistics about various health issues and signals detected across the database fleet. It helps in identifying the number of resources affected by different types of issues, categorized by signal types.   
[list_fleet_issues](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_issues) |  This tool provides a list of issues and recommendations that a user has access to and that are within the requested scope. Use this tool to identify specific database resources affected by health issues based on different categories like availability, data protection, security, performance and cost. It supports filtering issues by criteria such as product type, location, issue severity, tags, and labels. You can also apply filters for specific signal types and their associated products. The results can be sorted by signal type, product, location, or issue severity. If you need aggregated issue statistics instead of a list of individual issues, use the list_fleet_health_issues tool.   
[list_fleet_resource_groups](https://docs.cloud.google.com/database-center/docs/reference/mcp/tools_list/list_fleet_resource_groups) |  This tool provides a list of database resource groups. A database resource group represents a collection of related database instances, such as a primary server and any read replicas. The tool supports powerful filtering on various attributes like location, product type, engine, tags, and labels, as well as sorting, enabling detailed exploration of your database fleet.   
  
### Get MCP tool specifications

To get the MCP tool specifications for all tools in an MCP server, use the `tools/list` method. The following example demonstrates how to use `curl` to list all tools and their specifications currently available within the MCP server. 

Curl Request  
---  
      
    
                          curl --location 'https://databasecenter.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
        "method": "tools/list",
        "jsonrpc": "2.0",
        "id": 1
    }'
                          
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-22 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-22 UTC."],[],[]] 
