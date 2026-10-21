---
url: https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/
title: MCP Reference: redis.googleapis.com \u00a0|\u00a0 Memorystore for Redis Cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:10:55.245249+00:00
---

# MCP Reference: redis.googleapis.com  |  Memorystore for Redis Cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis Cluster ](https://docs.cloud.google.com/memorystore/docs/cluster)
  * [ Reference ](https://docs.cloud.google.com/memorystore/docs/cluster/apis)



Send feedback 

#  MCP Reference: redis.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

A [Model Context Protocol (MCP) server](https://modelcontextprotocol.io/docs/learn/server-concepts) acts as a proxy between an external service that provides context, data, or capabilities to a Large Language Model (LLM) or AI application. MCP servers connect AI applications to external systems such as databases and web services, translating their responses into a format that the AI application can understand.

### Server Setup

You must [enable MCP servers](https://docs.cloud.google.com/mcp/enable-disable-mcp-servers) and [set up authentication](https://docs.cloud.google.com/mcp/authenticate-mcp) before use. For more information about using Google and Google Cloud remote MCP servers, see [Google Cloud MCP servers overview](https://docs.cloud.google.com/mcp/overview). 

This is an MCP server which provides tools to manage Memorystore for Redis instances and Redis clusters.

### Server Endpoints

An MCP service endpoint is the network address and communication interface (usually a URL) of the MCP server that an AI application (the Host for the MCP client) uses to establish a secure, standardized connection. It is the point of contact for the LLM to request context, call a tool, or access a resource. Google MCP endpoints can be global or regional.

The redis.googleapis.com MCP server has the following MCP endpoint:

  * https://redis.googleapis.com/mcp



## MCP Tools

An [MCP tool](https://modelcontextprotocol.io/legacy/concepts/tools) is a function or executable capability that an MCP server exposes to a LLM or AI application to perform an action in the real world.

The redis.googleapis.com MCP server has the following tools:

MCP Tools  
---  
[list_clusters](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/list_clusters) |  List all clusters in Memorystore for Redis Cluster.   
[get_cluster](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/get_cluster) |  Get detailed information about a cluster in Memorystore for Redis Cluster.   
[create_cluster](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/create_cluster) |  Create a cluster in Memorystore for Redis Cluster.   
[delete_cluster](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/delete_cluster) |  Delete a cluster in Memorystore for Redis Cluster.   
[update_cluster](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/update_cluster) |  Update a cluster in Memorystore for Redis Cluster.   
[get_cluster_certificate_authority](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/get_cluster_certificate_authority) |  Get the certificate authority for a cluster in Memorystore for Redis Cluster.   
[reschedule_cluster_maintenance](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/reschedule_cluster_maintenance) |  Reschedule maintenance for a cluster in Memorystore for Redis Cluster.   
[list_backup_collections](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/list_backup_collections) |  List all Memorystore for Redis Cluster backup collections.   
[get_backup_collection](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/get_backup_collection) |  Get detailed information about a Memorystore for Redis Cluster backup collection.   
[list_backups](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/list_backups) |  List all Memorystore for Redis Cluster backups.   
[get_backup](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/get_backup) |  Get detailed information about a Memorystore for Redis Cluster backup.   
[delete_backup](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/delete_backup) |  Delete a Memorystore for Redis Cluster backup.   
[export_backup](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/export_backup) |  Export a Memorystore for Redis Cluster backup.   
[backup_cluster](https://docs.cloud.google.com/memorystore/docs/cluster/reference/mcp/tools_list/backup_cluster) |  Back up a cluster in Memorystore for Redis Cluster.   
  
### Get MCP tool specifications

To get the MCP tool specifications for all tools in an MCP server, use the `tools/list` method. The following example demonstrates how to use `curl` to list all tools and their specifications currently available within the MCP server. 

Curl Request  
---  
      
    
                          curl --location 'https://redis.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
        "method": "tools/list",
        "jsonrpc": "2.0",
        "id": 1
    }'
                          
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-06 UTC."],[],[]] 
