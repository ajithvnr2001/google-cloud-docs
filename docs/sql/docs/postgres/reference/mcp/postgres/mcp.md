---
url: https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/
title: MCP Reference: cloud-sql \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:14:40.293369+00:00
---

# MCP Reference: cloud-sql  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Reference ](https://docs.cloud.google.com/sql/docs/postgres/apis)



Send feedback 

#  MCP Reference: cloud-sql Stay organized with collections  Save and categorize content based on your preferences. 

Cloud SQL Admin API for MCP

A [Model Context Protocol (MCP) server](https://modelcontextprotocol.io/docs/learn/server-concepts) acts as a proxy between an external service that provides context, data, or capabilities to a Large Language Model (LLM) or AI application. MCP servers connect AI applications to external systems such as databases and web services, translating their responses into a format that the AI application can understand.

### Server Setup

You must [enable MCP servers](https://docs.cloud.google.com/mcp/enable-disable-mcp-servers) and [set up authentication](https://docs.cloud.google.com/mcp/authenticate-mcp) before use. For more information about using Google and Google Cloud remote MCP servers, see [Google Cloud MCP servers overview](https://docs.cloud.google.com/mcp/overview). 

### Server Endpoints

An MCP service endpoint is the network address and communication interface (usually a URL) of the MCP server that an AI application (the Host for the MCP client) uses to establish a secure, standardized connection. It is the point of contact for the LLM to request context, call a tool, or access a resource. Google MCP endpoints can be global or regional.

The Cloud SQL Admin API MCP server offers the following MCP toolset endpoints:

  * https://sqladmin.googleapis.com/mcp
  * https://sqladmin.googleapis.com/mcp/readonly
  * https://sqladmin.googleapis.com/mcp/instance_manage
  * https://sqladmin.googleapis.com/mcp/query_execution



## MCP Tools

An [MCP tool](https://modelcontextprotocol.io/legacy/concepts/tools) is a function or executable capability that an MCP server exposes to a LLM or AI application to perform an action in the real world. Toolsets are a group of tools that are useful for a specific task. Using toolsets can help your agent perform better because it decreases the number of tools available to your agent.

### Toolsets

The cloud-sql MCP server has the following toolsets:

MCP Toolsets  
---  
Endpoint | Description | Tools  
/mcp | All tools available Cloud SQL OneMCP API. | `

  * [list_instances](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/list_instances)
  * [get_instance](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/get_instance)
  * [create_instance](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance)
  * [update_instance](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/update_instance)
  * [clone_instance](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/clone_instance)
  * [postgres_upgrade_precheck](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/postgres_upgrade_precheck)
  * [get_operation](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/get_operation)
  * [execute_sql](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/execute_sql)
  * [execute_sql_readonly](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/execute_sql_readonly)
  * [list_users](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/list_users)
  * [create_user](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_user)
  * [update_user](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/update_user)
  * [create_backup](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_backup)
  * [restore_backup](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/restore_backup)
  * [import_data](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/import_data)

`  
/mcp/readonly | Read-only operations for Cloud SQL. | `

  * [list_instances](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/list_instances)
  * [get_instance](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/get_instance)
  * [get_operation](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/get_operation)
  * [postgres_upgrade_precheck](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/postgres_upgrade_precheck)
  * [execute_sql_readonly](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/execute_sql_readonly)
  * [list_users](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/list_users)

`  
/mcp/instance_manage | Creating, modifying, and managing Cloud SQL instances. | `

  * [list_instances](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/list_instances)
  * [get_instance](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/get_instance)
  * [create_instance](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_instance)
  * [update_instance](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/update_instance)
  * [clone_instance](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/clone_instance)
  * [postgres_upgrade_precheck](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/postgres_upgrade_precheck)
  * [get_operation](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/get_operation)

`  
/mcp/query_execution | Executing SQL statements with read/write privileges. | `

  * [execute_sql](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/execute_sql)
  * [get_operation](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/get_operation)
  * [list_instances](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/list_instances)
  * [get_instance](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/get_instance)
  * [list_users](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/list_users)
  * [create_user](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp/postgres/mcp/tools_list/create_user)

`  
  
### Get MCP tool specifications

To get the MCP tool specifications for all tools in an MCP server, use the `tools/list` method. The following example demonstrates how to use `curl` to list all tools and their specifications currently available within the MCP server. 

Curl Request  
---  
      
    
    curl --location 'https://sqladmin.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
        "method": "tools/list",
        "jsonrpc": "2.0",
        "id": 1
    }'  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
