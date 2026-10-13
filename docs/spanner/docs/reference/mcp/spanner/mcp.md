---
url: https://docs.cloud.google.com/spanner/docs/reference/mcp/spanner/mcp/
title: MCP Reference: spanner.googleapis.com \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:30:27.263655+00:00
---

# MCP Reference: spanner.googleapis.com  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/reference/mcp/spanner/mcp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  MCP Reference: spanner.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

A [Model Context Protocol (MCP) server](https://modelcontextprotocol.io/docs/learn/server-concepts) acts as a proxy between an external service that provides context, data, or capabilities to a Large Language Model (LLM) or AI application. MCP servers connect AI applications to external systems such as databases and web services, translating their responses into a format that the AI application can understand.

### Server Setup

You must [enable MCP servers](https://docs.cloud.google.com/mcp/enable-disable-mcp-servers) and [set up authentication](https://docs.cloud.google.com/mcp/authenticate-mcp) before use. For more information about using Google and Google Cloud remote MCP servers, see [Google Cloud MCP servers overview](https://docs.cloud.google.com/mcp/overview). 

Spanner MCP Server provides tools to interact with Spanner

### Server Endpoints

An MCP service endpoint is the network address and communication interface (usually a URL) of the MCP server that an AI application (the Host for the MCP client) uses to establish a secure, standardized connection. It is the point of contact for the LLM to request context, call a tool, or access a resource. Google MCP endpoints can be global or regional.

The spanner.googleapis.com MCP server has the following MCP endpoint:

  * https://spanner.googleapis.com/mcp



## MCP Tools

An [MCP tool](https://modelcontextprotocol.io/legacy/concepts/tools) is a function or executable capability that an MCP server exposes to a LLM or AI application to perform an action in the real world.

The spanner.googleapis.com MCP server has the following tools:

MCP Tools  
---  
[get_instance](https://docs.cloud.google.com/spanner/docs/reference/mcp/spanner/mcp/tools_list/get_instance) |  Get information about a Spanner instance   
[list_instances](https://docs.cloud.google.com/spanner/docs/reference/mcp/spanner/mcp/tools_list/list_instances) |  List Spanner instances in a given project.

  * Response may include next_page_token to fetch additional instances using list_instances tool with page_token set.

  
[list_configs](https://docs.cloud.google.com/spanner/docs/reference/mcp/spanner/mcp/tools_list/list_configs) |  List instance configs in a given project.

  * Response may include next_page_token to fetch additional configs using list_configs tool with page_token set.

  
[get_config](https://docs.cloud.google.com/spanner/docs/reference/mcp/spanner/mcp/tools_list/get_config) |  Get information about a specific Spanner instance configuration.   
[create_instance](https://docs.cloud.google.com/spanner/docs/reference/mcp/spanner/mcp/tools_list/create_instance) |  Create a Spanner instance in a given project.   
[update_instance](https://docs.cloud.google.com/spanner/docs/reference/mcp/spanner/mcp/tools_list/update_instance) |  Update a Spanner instance.

  * While updating an instance always include instance name and config.

  
[create_database](https://docs.cloud.google.com/spanner/docs/reference/mcp/spanner/mcp/tools_list/create_database) |  Create a Spanner database in a given instance.   
[get_database_ddl](https://docs.cloud.google.com/spanner/docs/reference/mcp/spanner/mcp/tools_list/get_database_ddl) |  Get database schema for a given database.   
[list_databases](https://docs.cloud.google.com/spanner/docs/reference/mcp/spanner/mcp/tools_list/list_databases) |  List Spanner databases in a given spanner instance. * Response may include next_page_token to fetch additional databases using list_databases tool with page_token set.   
[create_session](https://docs.cloud.google.com/spanner/docs/reference/mcp/spanner/mcp/tools_list/create_session) |  Create a session in a given database for query executions using execute_sql tool.

  * Session can be reused to execute multiple concurrent operations.

  
[execute_sql](https://docs.cloud.google.com/spanner/docs/reference/mcp/spanner/mcp/tools_list/execute_sql) |  Execute SQL statement using a given session.

  * execute_sql tool can be used to execute DQL as well as DML statements.
  * Prefer using parameterized queries over literal values.
  * Use commit tool to commit result of a DML statement.
  * DDL statements are only supported using update_database_schema tool.

  
[execute_sql_readonly](https://docs.cloud.google.com/spanner/docs/reference/mcp/spanner/mcp/tools_list/execute_sql_readonly) |  Execute SQL query statement using a given session in a read-only transaction.

  * execute_sql_readonly tool can be used to execute DQL statements.
  * Prefer using parameterized queries over literal values.
  * DML statements and multi read transactions are only supported via execute_sql tool.
  * The transaction bit should not be set in the request and will default to single-use read-only transaction.

  
[commit](https://docs.cloud.google.com/spanner/docs/reference/mcp/spanner/mcp/tools_list/commit) |  Commit a transaction in a given session.

  * If commit is finalizing the result of a DML statement then commit request should include latest precommit_token returned by execute_sql tool.
  * If response to commit includes another precommit_token then issue another commit call to finalize the transaction with the latest precommit_token.

  
[update_database_schema](https://docs.cloud.google.com/spanner/docs/reference/mcp/spanner/mcp/tools_list/update_database_schema) |  Update schema for a given database.   
[get_operation](https://docs.cloud.google.com/spanner/docs/reference/mcp/spanner/mcp/tools_list/get_operation) |  Get status of a long-running operation.

  * Long running operation may take several minutes to complete. get_operation tool can be used to poll the status of a long running operation.

  
  
### Get MCP tool specifications

To get the MCP tool specifications for all tools in an MCP server, use the `tools/list` method. The following example demonstrates how to use `curl` to list all tools and their specifications currently available within the MCP server. 

Curl Request  
---  
      
    
                          curl --location 'https://spanner.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
        "method": "tools/list",
        "jsonrpc": "2.0",
        "id": 1
    }'
                          
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-16 UTC."],[],[]] 
