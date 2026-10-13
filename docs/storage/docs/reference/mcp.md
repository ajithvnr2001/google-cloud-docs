---
url: https://docs.cloud.google.com/storage/docs/reference/mcp/
title: MCP Reference: storage.googleapis.com \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:34:59.620925+00:00
---

# MCP Reference: storage.googleapis.com  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/reference/mcp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  MCP Reference: storage.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

Storage MCP Service provides tools to interact with Cloud Storage.

A [Model Context Protocol (MCP) server](https://modelcontextprotocol.io/docs/learn/server-concepts) acts as a proxy between an external service that provides context, data, or capabilities to an Large Language Model (LLM) or AI application. MCP servers connect AI applications to external systems such as databases and web services, translating their responses into a format that the AI application can understand.

### Server Setup

You must [enable MCP servers](https://docs.cloud.google.com/mcp/enable-disable-mcp-servers) and [set up authentication](https://docs.cloud.google.com/mcp/authenticate-mcp) before use. For more information about using Google and Google Cloud remote MCP servers, see [Google Cloud MCP servers overview](https://docs.cloud.google.com/mcp/overview). 

### Server Endpoints

An MCP service endpoint is the network address and communication interface (usually a URL) of the MCP server that an AI application (the Host for the MCP client) uses to establish a secure, standardized connection. It is the point of contact for the LLM to request context, call a tool, or access a resource. Google MCP endpoints can be global or regional.

The Cloud Storage API MCP server has the following global MCP endpoint:

  * https://storage.googleapis.com/storage/mcp



## MCP Tools

An [MCP tool](https://modelcontextprotocol.io/legacy/concepts/tools) is a function or executable capability that an MCP server exposes to an LLM or AI application to perform an action in the real world.

### Tools

The storage.googleapis.com MCP server has the following tools:

MCP Tools  
---  
`[list_buckets](https://docs.cloud.google.com/storage/docs/reference/mcp/tools_list/list_buckets)` |  Lists the buckets of a project.   
`[list_objects](https://docs.cloud.google.com/storage/docs/reference/mcp/tools_list/list_objects)` |  Lists the objects in a bucket.   
`[create_bucket](https://docs.cloud.google.com/storage/docs/reference/mcp/tools_list/create_bucket)` |  Creates a bucket in a project.   
`[delete_bucket](https://docs.cloud.google.com/storage/docs/reference/mcp/tools_list/delete_bucket)` |  Deletes a bucket from a project.   
`[read_text](https://docs.cloud.google.com/storage/docs/reference/mcp/tools_list/read_text)` |  DEPRECATED: Use `read_object` instead. Reads non-binary text content from an object.   
`[read_object](https://docs.cloud.google.com/storage/docs/reference/mcp/tools_list/read_object)` |  Reads an object from Cloud Storage. Supports both text and binary content (it will output text for text content and binary for binary content).Constraints & Behavior: 

  * **Size Limit** : The maximum supported file size is 8MiB. Requests for larger objects will fail with an OutOfRange error.

  
`[write_text](https://docs.cloud.google.com/storage/docs/reference/mcp/tools_list/write_text)` |  Writes text content to an object, overwriting any existing content.   
`[delete_object](https://docs.cloud.google.com/storage/docs/reference/mcp/tools_list/delete_object)` |  Deletes an object from Cloud Storage.   
`[get_object_metadata](https://docs.cloud.google.com/storage/docs/reference/mcp/tools_list/get_object_metadata)` |  Gets the metadata of an object.   
  
### Get MCP tool specifications

To get the MCP tool specifications for all tools in an MCP server, use the `tools/list` method. The following example demonstrates how to use `curl` to list all tools and their specifications currently available within the MCP server. 

Curl Request  
---  
      
    
    curl --location 'https://storage.googleapis.com/storage/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
        "method": "tools/list",
        "jsonrpc": "2.0",
        "id": 1
    }'
                          
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-13 UTC."],[],[]] 
