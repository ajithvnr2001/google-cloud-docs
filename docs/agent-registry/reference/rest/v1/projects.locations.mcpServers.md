---
url: https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.mcpServers
title: REST Resource: projects.locations.mcpServers \u00a0|\u00a0 Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:06:33.498696+00:00
---

# REST Resource: projects.locations.mcpServers  |  Agent Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.mcpServers

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Reference ](https://docs.cloud.google.com/agent-registry/apis)



Send feedback 

#  REST Resource: projects.locations.mcpServers Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: McpServer
    * JSON representation
  * Tool
    * JSON representation
  * Annotations
    * JSON representation
  * Methods



## Resource: McpServer

Represents an MCP (Model Context Protocol) Server.

JSON representation  
---  
      
    
    {
      "name": string,
      "mcpServerId": string,
      "displayName": string,
      "description": string,
      "interfaces": [
        {
          object ([Interface](https://docs.cloud.google.com/agent-registry/reference/rest/v1/Interface))
        }
      ],
      "tools": [
        {
          object ([Tool](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.mcpServers#Tool))
        }
      ],
      "createTime": string,
      "updateTime": string,
      "attributes": {
        string: {
          object
        },
        ...
      }
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the MCP Server. Format: `projects/{project}/locations/{location}/mcpServers/{mcpServer}`.  
`mcpServerId` |  `string` Output only. A stable, globally unique identifier for MCP Servers.  
`displayName` |  `string` Output only. The display name of the MCP Server.  
`description` |  `string` Output only. The description of the MCP Server.  
`interfaces[]` |  `object (`[Interface](https://docs.cloud.google.com/agent-registry/reference/rest/v1/Interface)`)` Output only. The connection details for the MCP Server.  
`tools[]` |  `object (`[Tool](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.mcpServers#Tool)`)` Output only. Tools provided by the MCP Server.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Create time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Update time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`attributes` |  `map (key: string, value: object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format))` Output only. Attributes of the MCP Server. Valid values:

  * `agentregistry.googleapis.com/system/RuntimeIdentity`: {"principal": "principal://..."} - the runtime identity associated with the MCP Server.
  * `agentregistry.googleapis.com/system/RuntimeReference`: {"uri": "//..."}
  * the URI of the underlying resource hosting the MCP Server, for example, the GKE Deployment.

An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
## Tool

Represents a single tool provided by an MCP Server.

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "annotations": {
        object ([Annotations](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.mcpServers#Annotations))
      }
    }  
  
Fields  
---  
`name` |  `string` Output only. Human-readable name of the tool.  
`description` |  `string` Output only. Description of what the tool does.  
`annotations` |  `object (`[Annotations](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.mcpServers#Annotations)`)` Output only. Annotations associated with the tool.  
  
## Annotations

Annotations describing the characteristics and behavior of a tool or operation.

JSON representation  
---  
      
    
    {
      "title": string,
      "destructiveHint": boolean,
      "idempotentHint": boolean,
      "openWorldHint": boolean,
      "readOnlyHint": boolean
    }  
  
Fields  
---  
`title` |  `string` Output only. A human-readable title for the tool.  
`destructiveHint` |  `boolean` Output only. If true, the tool may perform destructive updates to its environment. If false, the tool performs only additive updates. NOTE: This property is meaningful only when `readOnlyHint == false` Default: true  
`idempotentHint` |  `boolean` Output only. If true, calling the tool repeatedly with the same arguments will have no additional effect on its environment. NOTE: This property is meaningful only when `readOnlyHint == false` Default: false  
`openWorldHint` |  `boolean` Output only. If true, this tool may interact with an "open world" of external entities. If false, the tool's domain of interaction is closed. For example, the world of a web search tool is open, whereas that of a memory tool is not. Default: true  
`readOnlyHint` |  `boolean` Output only. If true, the tool does not modify its environment. Default: false  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.mcpServers/get)`

|  Gets details of a single McpServer.  
  
### `[list](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.mcpServers/list)`

|  Lists McpServers in a given project and location.  
  
### `[search](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.mcpServers/search)`

|  Searches McpServers in a given project and location.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-24 UTC."],[],[]] 
