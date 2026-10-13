---
url: https://docs.cloud.google.com/oracle/database/docs/reference/mcp/
title: MCP Reference: oracledatabase.googleapis.com \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:08:55.336095+00:00
---

# MCP Reference: oracledatabase.googleapis.com  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/reference/mcp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Reference ](https://docs.cloud.google.com/oracle/database/docs/apis)



Send feedback 

#  MCP Reference: oracledatabase.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

A [Model Context Protocol (MCP) server](https://modelcontextprotocol.io/docs/learn/server-concepts) acts as a proxy between an external service that provides context, data, or capabilities to a Large Language Model (LLM) or AI application. MCP servers connect AI applications to external systems such as databases and web services, translating their responses into a format that the AI application can understand.

### Server Setup

You must [enable MCP servers](https://docs.cloud.google.com/mcp/enable-disable-mcp-servers) and [set up authentication](https://docs.cloud.google.com/mcp/authenticate-mcp) before use. For more information about using Google and Google Cloud remote MCP servers, see [Google Cloud MCP servers overview](https://docs.cloud.google.com/mcp/overview). 

Oracle Database MCP server provides tools to interact with Oracle Database

### Server Endpoints

An MCP service endpoint is the network address and communication interface (usually a URL) of the MCP server that an AI application (the Host for the MCP client) uses to establish a secure, standardized connection. It is the point of contact for the LLM to request context, call a tool, or access a resource. Google MCP endpoints can be global or regional.

The Oracle [Database@Google](mailto:Database@Google) Cloud API MCP server has the following MCP endpoint:

  * https://oracledatabase.googleapis.com/mcp



## MCP Tools

An [MCP tool](https://modelcontextprotocol.io/legacy/concepts/tools) is a function or executable capability that an MCP server exposes to a LLM or AI application to perform an action in the real world.

The oracledatabase.googleapis.com MCP server has the following tools:

MCP Tools  
---  
[list_autonomous_databases](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/list_autonomous_databases) |  List autonomous databases (ADBs) in a Google Cloud project in the given location.   
[create_autonomous_database](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/create_autonomous_database) |  Create an Autonomous Database (ADB). This request can be used to create a new ADB instance or a clone of an existing ADB or an ADB Disaster Recovery (DR) instance. If the source config is not specified, a new ADB instance is created. If the source config is specified, a clone of the source is created. If the source is specified and the source is an ADB DR instance, then a new ADB DR instance is created. While creating a new ADB instance, it can have Public IP support or Private IP support. In case of Private IP support, the request should contain the ODBSubnetwork details. If a request is Public IP mLTS is required mandatorily.   
[get_autonomous_database](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/get_autonomous_database) |  Get details for an autonomous database (ADB) in a Google Cloud project in the given location.   
[create_exadata_infrastructure](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/create_exadata_infrastructure) |  Create a Cloud Exadata Infrastructure. A user needs a Cloud Exadata Infrastructure to create a Cloud Exadata VM cluster.   
[get_exadata_infrastructure](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/get_exadata_infrastructure) |  Get details for an Exadata Infrastructure in a Google Cloud project in the given location.   
[list_exadata_infrastructures](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/list_exadata_infrastructures) |  List Exadata Infrastructures in a Google Cloud project in the given location.   
[list_db_servers](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/list_db_servers) |  List Db Servers in a Google Cloud project in the given location for a given Cloud Exadata Infrastructure. For creation of a Cloud Vm Cluster, we need to know the Db Servers in a Cloud Exadata Infrastructure. This API will be used by the MCP service to get the Db Servers.   
[create_cloud_vm_cluster](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/create_cloud_vm_cluster) |  Create a Cloud Vm Cluster. A Cloud Vm Cluster is a set of Virtual Machines (VMs) on a Cloud Exadata Infrastructure.   
[get_cloud_vm_cluster](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/get_cloud_vm_cluster) |  Get details for a Cloud Vm Cluster in a Google Cloud project in the given location.   
[list_cloud_vm_clusters](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/list_cloud_vm_clusters) |  List Cloud Vm Clusters in a Google Cloud project in the given location.   
[create_exascale_db_storage_vault](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/create_exascale_db_storage_vault) |  Create an Exascale Db Storage Vault.   
[get_exascale_db_storage_vault](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/get_exascale_db_storage_vault) |  Get details for an Exascale DB Storage Vault in a Google Cloud project in the given location.   
[list_exascale_db_storage_vaults](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/list_exascale_db_storage_vaults) |  List Exascale DB Storage Vaults in a Google Cloud project in the given location.   
[create_exadb_vm_cluster](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/create_exadb_vm_cluster) |  Create an Exadb Vm Cluster. An Exadb Vm Cluster is a set of Virtual Machines (VMs) on an Exadata Infrastructure.   
[get_exadb_vm_cluster](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/get_exadb_vm_cluster) |  Get details for an Exadb Vm Cluster in a Google Cloud project in the given location.   
[list_exadb_vm_clusters](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/list_exadb_vm_clusters) |  List Exadb Vm Clusters in a Google Cloud project in the given location.   
[create_db_system](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/create_db_system) |  Create a DbSystem (BaseDB).   
[get_db_system](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/get_db_system) |  Get details for a Db system in a Google Cloud project in the given location.   
[list_db_systems](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/list_db_systems) |  List Db systems in a Google Cloud project in the given location.   
[create_odb_network](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/create_odb_network) |  Create an ODB Network. An ODB Network connects a Google Cloud VPC network to Oracle Database resources.   
[get_odb_network](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/get_odb_network) |  Get details for an ODB Network in a Google Cloud project in the given location.   
[list_odb_networks](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/list_odb_networks) |  List ODB Networks in a Google Cloud project in the given location.   
[create_odb_subnet](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/create_odb_subnet) |  Create an ODB Subnet. An ODB Subnet is a subnetwork within an ODB Network.   
[get_odb_subnet](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/get_odb_subnet) |  Get details for an ODB Subnet in a Google Cloud project in the given location.   
[list_odb_subnets](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/list_odb_subnets) |  List ODB Subnets in a Google Cloud project in the given location.   
[get_operation](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/get_operation) |  Get the status of a long-running operation. A long-running operation can take several minutes to complete. If an operation takes an extended amount of time, then use a command line tool to pause for 30 seconds before rechecking the status of the operation.   
  
### Get MCP tool specifications

To get the MCP tool specifications for all tools in an MCP server, use the `tools/list` method. The following example demonstrates how to use `curl` to list all tools and their specifications currently available within the MCP server. 

Curl Request  
---  
      
    
                          
    curl --location 'https://oracledatabase.googleapis.com/mcp' \
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
