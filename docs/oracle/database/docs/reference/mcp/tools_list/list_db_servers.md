---
url: https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/list_db_servers/
title: MCP Tools Reference: oracledatabase.googleapis.com \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:08:56.088778+00:00
---

# MCP Tools Reference: oracledatabase.googleapis.com  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/list_db_servers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Reference ](https://docs.cloud.google.com/oracle/database/docs/apis)



Send feedback 

#  MCP Tools Reference: oracledatabase.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `list_db_servers`

List Db Servers in a Google Cloud project in the given location for a given Cloud Exadata Infrastructure. For creation of a Cloud Vm Cluster, we need to know the Db Servers in a Cloud Exadata Infrastructure. This API will be used by the MCP service to get the Db Servers.

The following sample demonstrate how to use `curl` to invoke the `list_db_servers` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://oracledatabase.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "list_db_servers",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

The request for `DbServer.List`.

### ListDbServersRequest

JSON representation  
---  
      
    
    {
      "parent": string,
      "pageSize": integer,
      "pageToken": string
    }  
  
Fields  
---  
`parent` |  `string` Required. The parent value for database server in the following format: projects/{project}/locations/{location}/cloudExadataInfrastructures/{cloudExadataInfrastructure}.  
`pageSize` |  `integer` Optional. The maximum number of items to return. If unspecified, a maximum of 50 db servers will be returned. The maximum value is 1000; values above 1000 will be reset to 1000.  
`pageToken` |  `string` Optional. A token identifying a page of results the server should return.  
  
## Output Schema

The response for `DbServer.List`.

### ListDbServersResponse

JSON representation  
---  
      
    
    {
      "dbServers": [
        {
          object ([DbServer](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/list_db_servers#Output.Schema.DbServer))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`dbServers[]` |  `object (`[DbServer](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/list_db_servers#Output.Schema.DbServer)`)` The list of database servers.  
`nextPageToken` |  `string` A token identifying a page of results the server should return.  
  
### DbServer

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "properties": {
        object ([DbServerProperties](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/list_db_servers#Output.Schema.DbServerProperties))
      }
    }  
  
Fields  
---  
`name` |  `string` Identifier. The name of the database server resource with the format: projects/{project}/locations/{location}/cloudExadataInfrastructures/{cloud_exadata_infrastructure}/dbServers/{db_server}  
`displayName` |  `string` Optional. User friendly name for this resource.  
`properties` |  `object (`[DbServerProperties](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/list_db_servers#Output.Schema.DbServerProperties)`)` Optional. Various properties of the database server.  
  
### DbServerProperties

JSON representation  
---  
      
    
    {
      "ocid": string,
      "ocpuCount": integer,
      "maxOcpuCount": integer,
      "memorySizeGb": integer,
      "maxMemorySizeGb": integer,
      "dbNodeStorageSizeGb": integer,
      "maxDbNodeStorageSizeGb": integer,
      "vmCount": integer,
      "state": enum (State),
      "dbNodeIds": [
        string
      ]
    }  
  
Fields  
---  
`ocid` |  `string` Output only. OCID of database server.  
`ocpuCount` |  `integer` Optional. OCPU count per database.  
`maxOcpuCount` |  `integer` Optional. Maximum OCPU count per database.  
`memorySizeGb` |  `integer` Optional. Memory allocated in GBs.  
`maxMemorySizeGb` |  `integer` Optional. Maximum memory allocated in GBs.  
`dbNodeStorageSizeGb` |  `integer` Optional. Local storage per VM.  
`maxDbNodeStorageSizeGb` |  `integer` Optional. Maximum local storage per VM.  
`vmCount` |  `integer` Optional. Vm count per database.  
`state` |  `enum (`State`)` Output only. State of the database server.  
`dbNodeIds[]` |  `string` Output only. OCID of database nodes associated with the database server.  
  
### Tool Annotations

Destructive Hint: ❌ | Idempotent Hint: ❌ | Read Only Hint: ✅ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-17 UTC."],[],[]] 
