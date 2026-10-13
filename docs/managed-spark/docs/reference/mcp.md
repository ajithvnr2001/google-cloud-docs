---
url: https://docs.cloud.google.com/managed-spark/docs/reference/mcp/
title: MCP Reference: dataproc.googleapis.com \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:44:39.508185+00:00
---

# MCP Reference: dataproc.googleapis.com  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/reference/mcp/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Reference ](https://docs.cloud.google.com/managed-spark/docs/reference)



Send feedback 

#  MCP Reference: dataproc.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

A [Model Context Protocol (MCP) server](https://modelcontextprotocol.io/docs/learn/server-concepts) acts as a proxy between an external service that provides context, data, or capabilities to a Large Language Model (LLM) or AI application. MCP servers connect AI applications to external systems such as databases and web services, translating their responses into a format that the AI application can understand.

### Server Setup

You must [enable MCP servers](https://docs.cloud.google.com/mcp/enable-disable-mcp-servers) and [set up authentication](https://docs.cloud.google.com/mcp/authenticate-mcp) before use. For more information about using Google and Google Cloud remote MCP servers, see [Google Cloud MCP servers overview](https://docs.cloud.google.com/mcp/overview). 

Dataproc MCP server provides tools to interact with Dataproc

### Server Endpoints

An MCP service endpoint is the network address and communication interface (usually a URL) of the MCP server that an AI application (the Host for the MCP client) uses to establish a secure, standardized connection. It is the point of contact for the LLM to request context, call a tool, or access a resource. Google MCP endpoints can be global or [regional](https://docs.cloud.google.com/managed-spark/docs/concepts/cluster-region#location_and_regional_endpoints).

The dataproc.googleapis.com MCP server has the following MCP endpoint:

  * https://dataproc.googleapis.com/mcp



## MCP Tools

An [MCP tool](https://modelcontextprotocol.io/legacy/concepts/tools) is a function or executable capability that an MCP server exposes to a LLM or AI application to perform an action in the real world.

The dataproc.googleapis.com MCP server has the following tools:

MCP Tools  
---  
[list_clusters](https://docs.cloud.google.com/managed-spark/docs/reference/mcp/tools_list/list_clusters) |  List Dataproc clusters in a Google Cloud project   
[get_cluster](https://docs.cloud.google.com/managed-spark/docs/reference/mcp/tools_list/get_cluster) |  Get a Dataproc cluster in a Google Cloud project   
[create_cluster](https://docs.cloud.google.com/managed-spark/docs/reference/mcp/tools_list/create_cluster) |  Create a Dataproc cluster in a Google Cloud project   
[delete_cluster](https://docs.cloud.google.com/managed-spark/docs/reference/mcp/tools_list/delete_cluster) |  Delete a Dataproc cluster in a Google Cloud project   
[list_jobs](https://docs.cloud.google.com/managed-spark/docs/reference/mcp/tools_list/list_jobs) |  List Dataproc jobs in a Google Cloud project   
[get_job](https://docs.cloud.google.com/managed-spark/docs/reference/mcp/tools_list/get_job) |  Get a Dataproc job in a Google Cloud project   
[list_batches](https://docs.cloud.google.com/managed-spark/docs/reference/mcp/tools_list/list_batches) |  List Dataproc batches in a Google Cloud project   
[get_batch](https://docs.cloud.google.com/managed-spark/docs/reference/mcp/tools_list/get_batch) |  Get a Dataproc batch in a Google Cloud project   
[create_batch](https://docs.cloud.google.com/managed-spark/docs/reference/mcp/tools_list/create_batch) |  Create a Dataproc Batch in a Google Cloud project   
[delete_batch](https://docs.cloud.google.com/managed-spark/docs/reference/mcp/tools_list/delete_batch) |  Delete a Dataproc Batch in a Google Cloud project   
[list_sessions](https://docs.cloud.google.com/managed-spark/docs/reference/mcp/tools_list/list_sessions) |  List Dataproc Sessions in a Google Cloud project   
[get_session](https://docs.cloud.google.com/managed-spark/docs/reference/mcp/tools_list/get_session) |  Get a Dataproc session in a Google Cloud project   
[create_session](https://docs.cloud.google.com/managed-spark/docs/reference/mcp/tools_list/create_session) |  Create a Dataproc Session in a Google Cloud project   
[delete_session](https://docs.cloud.google.com/managed-spark/docs/reference/mcp/tools_list/delete_session) |  Delete a Dataproc Session in a Google Cloud project   
[get_operation](https://docs.cloud.google.com/managed-spark/docs/reference/mcp/tools_list/get_operation) |  Gets the status of a long-running operation.**_Usage_** Some tools (for example, `create_cluster` and `delete_cluster`) return a long-running operation. You can use this tool to get the status of the operation. It can be called repeatedly to poll the status of a long running operation**Parameters** * `name`: The name of the operation to get. * `name` should be the name returned by the tool that initiated the operation. * `name` should be in the format of `projects/{project}/locations/{location}/operations/{operation}`.  
  
### Get MCP tool specifications

To get the MCP tool specifications for all tools in an MCP server, use the `tools/list` method. The following example demonstrates how to use `curl` to list all tools and their specifications currently available within the MCP server. 

Curl Request  
---  
      
    
    curl --location 'https://dataproc.googleapis.com/mcp' \
      --header 'content-type: application/json' \
      --header 'accept: application/json, text/event-stream' \
      --data '{
        "method": "tools/list",
        "jsonrpc": "2.0",
        "id": 1
        }'
                          
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-11 UTC."],[],[]] 
