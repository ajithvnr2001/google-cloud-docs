---
url: https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.services
title: REST Resource: projects.locations.services \u00a0|\u00a0 Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:06:42.777218+00:00
---

# REST Resource: projects.locations.services  |  Agent Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.services

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Reference ](https://docs.cloud.google.com/agent-registry/apis)



Send feedback 

#  REST Resource: projects.locations.services Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Service
    * JSON representation
  * AgentSpec
    * JSON representation
  * Type
  * McpServerSpec
    * JSON representation
  * Type
  * EndpointSpec
    * JSON representation
  * Type
  * Methods



## Resource: Service

Represents a user-defined Service.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "interfaces": [
        {
          object ([Interface](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/Interface))
        }
      ],
      "registryResource": string,
      "createTime": string,
      "updateTime": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "agentSpec": {
        object ([AgentSpec](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.services#AgentSpec))
      },
      "mcpServerSpec": {
        object ([McpServerSpec](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.services#McpServerSpec))
      },
      "endpointSpec": {
        object ([EndpointSpec](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.services#EndpointSpec))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the Service. Format: `projects/{project}/locations/{location}/services/{service}`.  
`displayName` |  `string` Optional. User-defined display name for the Service. Can have a maximum length of `63` characters.  
`description` |  `string` Optional. User-defined description of an Service. Can have a maximum length of `2048` characters.  
`interfaces[]` |  `object (`[Interface](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/Interface)`)` Optional. The connection details for the Service.  
`registryResource` |  `string` Output only. The resource name of the resulting Agent, MCP Server, or Endpoint. Format:

  * `projects/{project}/locations/{location}/mcpServers/{mcpServer}`
  * `projects/{project}/locations/{location}/agents/{agent}`
  * `projects/{project}/locations/{location}/endpoints/{endpoint}`

  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Create time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Update time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
The spec of the service. At least one of the specs must be set. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`agentSpec` |  `object (`[AgentSpec](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.services#AgentSpec)`)` Optional. The spec of the Agent. When `agentSpec` is set, the type of the service is Agent.  
`mcpServerSpec` |  `object (`[McpServerSpec](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.services#McpServerSpec)`)` Optional. The spec of the MCP Server. When `mcpServerSpec` is set, the type of the service is MCP Server.  
`endpointSpec` |  `object (`[EndpointSpec](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.services#EndpointSpec)`)` Optional. The spec of the Endpoint. When `endpointSpec` is set, the type of the service is Endpoint.  
End of mutually exclusive fields.  
  
## AgentSpec

The spec of the agent.

JSON representation  
---  
      
    
    {
      "type": enum ([Type](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.services#Type)),
      "content": {
        object
      }
    }  
  
Fields  
---  
`type` |  `enum (`[Type](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.services#Type)`)` Required. The type of the agent spec content.  
`content` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. The content of the Agent spec in the JSON format. This payload is validated against the schema for the specified type. The content size is limited to `10KB`.  
  
## Type

The type of the agent spec.

Enums  
---  
`TYPE_UNSPECIFIED` | Unspecified type.  
`NO_SPEC` | There is no spec for the Agent. The `content` field must be empty.  
`A2A_AGENT_CARD` | The content is an A2A Agent Card following the A2A specification. The `interfaces` field must be empty.  
  
## McpServerSpec

The spec of the MCP Server.

JSON representation  
---  
      
    
    {
      "type": enum ([Type](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.services#Type_1)),
      "content": {
        object
      }
    }  
  
Fields  
---  
`type` |  `enum (`[Type](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.services#Type_1)`)` Required. The type of the MCP Server spec content.  
`content` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. The content of the MCP Server spec. This payload is validated against the schema for the specified type. The content size is limited to `10KB`.  
  
## Type

The type of the MCP Server spec. Additional values may be added in the future.

Enums  
---  
`TYPE_UNSPECIFIED` | Unspecified type.  
`NO_SPEC` | There is no spec for the MCP Server. The `content` field must be empty.  
`TOOL_SPEC` | The content is a MCP Tool Spec following the One MCP specification. The payload is the same as the `tools/list` response.  
  
## EndpointSpec

The spec of the endpoint.

JSON representation  
---  
      
    
    {
      "type": enum ([Type](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.services#Type_2)),
      "content": {
        object
      }
    }  
  
Fields  
---  
`type` |  `enum (`[Type](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.services#Type_2)`)` Required. The type of the endpoint spec content.  
`content` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. The content of the endpoint spec. Reserved for future use.  
  
## Type

The type of the endpoint spec. Additional values may be added in the future.

Enums  
---  
`TYPE_UNSPECIFIED` | Unspecified type.  
`NO_SPEC` | There is no spec for the Endpoint. The `content` field must be empty.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.services/create)`

|  Creates a new Service in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.services/delete)`

|  Deletes a single Service.  
  
### `[get](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.services/get)`

|  Gets details of a single Service.  
  
### `[list](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.services/list)`

|  Lists Services in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.services/patch)`

|  Updates the parameters of a single Service.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-17 UTC."],[],[]] 
