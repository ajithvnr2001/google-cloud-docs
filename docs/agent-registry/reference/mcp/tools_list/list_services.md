---
url: https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/list_services/
title: MCP Tools Reference: agentregistry.googleapis.com \u00a0|\u00a0 Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:06:28.604711+00:00
---

# MCP Tools Reference: agentregistry.googleapis.com  |  Agent Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/list_services/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Reference ](https://docs.cloud.google.com/agent-registry/apis)



Send feedback 

#  MCP Tools Reference: agentregistry.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `list_services`

List services in a given project and location. A service can represent a manually onboarded MCP server, agent or REST endpoint.

The following code sample shows how to use `curl` to call the `list_services` MCP tool. 

Curl Request  
---  
      
    
    curl --location 'https://agentregistry.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "list_services",
        "arguments": {
          // Provide these details according to the MCP tool specification.
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'  
  
## Input Schema

Message for requesting list of Services

### ListServicesRequest

JSON representation  
---  
      
    
    {
      "parent": string,
      "pageSize": integer,
      "pageToken": string,
      "filter": string
    }  
  
Fields  
---  
`parent` |  `string` Required. The project and location to list services in. Expected format: `projects/{project}/locations/{location}`.  
`pageSize` |  `integer` Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.  
`pageToken` |  `string` Optional. A token identifying a page of results the server should return.  
`filter` |  `string` Optional. A query string used to filter the list of services returned. The filter expression must follow AIP-160 syntax.Filtering is supported on the `name`, `display_name`, `description`, and `labels` fields.Some examples:

  * `name = "projects/p1/locations/l1/services/s1"`
  * `display_name = "my-service"`
  * `description : "myservice description"`
  * `labels.env = "prod"`

  
  
## Output Schema

Message for response to listing Services

### ListServicesResponse

JSON representation  
---  
      
    
    {
      "services": [
        {
          object ([Service](https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/list_services#Output.Schema.Service))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`services[]` |  `object (`[Service](https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/list_services#Output.Schema.Service)`)` The list of Service resources matching the parent and filter criteria in the request. Each Service resource follows the format: `projects/{project}/locations/{location}/services/{service}`.  
`nextPageToken` |  `string` A token identifying a page of results the server should return. Used in `page_token`.  
  
### Service

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "interfaces": [
        {
          object ([Interface](https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/list_agents#Output.Schema.Interface))
        }
      ],
      "registryResource": string,
      "createTime": string,
      "updateTime": string,
    
      // Union field spec can be only one of the following:
      "agentSpec": {
        object ([AgentSpec](https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/list_services#Output.Schema.AgentSpec))
      },
      "mcpServerSpec": {
        object ([McpServerSpec](https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/list_services#Output.Schema.McpServerSpec))
      },
      "endpointSpec": {
        object ([EndpointSpec](https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/list_services#Output.Schema.EndpointSpec))
      }
      // End of list of possible types for union field spec.
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the Service. Format: `projects/{project}/locations/{location}/services/{service}`.  
`displayName` |  `string` Optional. User-defined display name for the Service. Can have a maximum length of `63` characters.  
`description` |  `string` Optional. User-defined description of an Service. Can have a maximum length of `2048` characters.  
`interfaces[]` |  `object (`[Interface](https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/list_agents#Output.Schema.Interface)`)` Optional. The connection details for the Service.  
`registryResource` |  `string` Output only. The resource name of the resulting Agent, MCP Server, or Endpoint. Format:

  * `projects/{project}/locations/{location}/mcpServers/{mcp_server}`
  * `projects/{project}/locations/{location}/agents/{agent}`
  * `projects/{project}/locations/{location}/endpoints/{endpoint}`

  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Create time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Update time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
Union field `spec`. The spec of the service. At least one of the specs must be set. `spec` can be only one of the following:  
`agentSpec` |  `object (`[AgentSpec](https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/list_services#Output.Schema.AgentSpec)`)` Optional. The spec of the Agent. When `agent_spec` is set, the type of the service is Agent.  
`mcpServerSpec` |  `object (`[McpServerSpec](https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/list_services#Output.Schema.McpServerSpec)`)` Optional. The spec of the MCP Server. When `mcp_server_spec` is set, the type of the service is MCP Server.  
`endpointSpec` |  `object (`[EndpointSpec](https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/list_services#Output.Schema.EndpointSpec)`)` Optional. The spec of the Endpoint. When `endpoint_spec` is set, the type of the service is Endpoint.  
  
### AgentSpec

JSON representation  
---  
      
    
    {
      "type": enum ([Type](https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/list_services#Output.Schema.Type)),
      "content": {
        object
      }
    }  
  
Fields  
---  
`type` |  `enum (`[Type](https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/list_services#Output.Schema.Type)`)` Required. The type of the agent spec content.  
`content` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. The content of the Agent spec in the JSON format. This payload is validated against the schema for the specified type. The content size is limited to `10KB`.  
  
### Struct

JSON representation  
---  
      
    
    {
      "fields": {
        string: value,
        ...
      }
    }  
  
Fields  
---  
`fields` |  `map (key: string, value: value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format))` Unordered map of dynamically typed values.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
### FieldsEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": value
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)`  
  
### Value

JSON representation  
---  
      
    
    {
    
      // Union field kind can be only one of the following:
      "nullValue": null,
      "numberValue": number,
      "stringValue": string,
      "boolValue": boolean,
      "structValue": {
        object
      },
      "listValue": array
      // End of list of possible types for union field kind.
    }  
  
Fields  
---  
Union field `kind`. The kind of value. `kind` can be only one of the following:  
`nullValue` |  `null` Represents a JSON `null`.  
`numberValue` |  `number` Represents a JSON number. Must not be `NaN`, `Infinity` or `-Infinity`, since those are not supported in JSON. This also cannot represent large Int64 values, since JSON format generally does not support them in its number type.  
`stringValue` |  `string` Represents a JSON string.  
`boolValue` |  `boolean` Represents a JSON boolean (`true` or `false` literal in JSON).  
`structValue` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Represents a JSON object.  
`listValue` |  `array (`[ListValue](https://protobuf.dev/reference/protobuf/google.protobuf/#list-value)` format)` Represents a JSON array.  
  
### ListValue

JSON representation  
---  
      
    
    {
      "values": [
        value
      ]
    }  
  
Fields  
---  
`values[]` |  `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)` Repeated field of dynamically typed values.  
  
### McpServerSpec

JSON representation  
---  
      
    
    {
      "type": enum ([Type](https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/list_services#Output.Schema.Type_1)),
      "content": {
        object
      }
    }  
  
Fields  
---  
`type` |  `enum (`[Type](https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/list_services#Output.Schema.Type_1)`)` Required. The type of the MCP Server spec content.  
`content` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. The content of the MCP Server spec. This payload is validated against the schema for the specified type. The content size is limited to `10KB`.  
  
### EndpointSpec

JSON representation  
---  
      
    
    {
      "type": enum ([Type](https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/list_services#Output.Schema.Type_2)),
      "content": {
        object
      }
    }  
  
Fields  
---  
`type` |  `enum (`[Type](https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/list_services#Output.Schema.Type_2)`)` Required. The type of the endpoint spec content.  
`content` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. The content of the endpoint spec. Reserved for future use.  
  
### Interface

JSON representation  
---  
      
    
    {
      "url": string,
      "protocolBinding": enum ([ProtocolBinding](https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/list_agents#Output.Schema.ProtocolBinding))
    }  
  
Fields  
---  
`url` |  `string` Required. The destination URL.  
`protocolBinding` |  `enum (`[ProtocolBinding](https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/list_agents#Output.Schema.ProtocolBinding)`)` Required. The protocol binding of the interface.  
  
### Timestamp

JSON representation  
---  
      
    
    {
      "seconds": string,
      "nanos": integer
    }  
  
Fields  
---  
`seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be between -62135596800 and 253402300799 inclusive (which corresponds to 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z).  
`nanos` |  `integer` Non-negative fractions of a second at nanosecond resolution. This field is the nanosecond portion of the duration, not an alternative to seconds. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be between 0 and 999,999,999 inclusive.  
  
### Type

The type of the agent spec.

Enums  
---  
`TYPE_UNSPECIFIED` | Unspecified type.  
`NO_SPEC` | There is no spec for the Agent. The `content` field must be empty.  
`A2A_AGENT_CARD` | The content is an A2A Agent Card following the A2A specification. The `interfaces` field must be empty.  
  
### NullValue

Represents a JSON `null`.

`NullValue` is a sentinel, using an enum with only one value to represent the null value for the `Value` type union.

A field of type `NullValue` with any value other than `0` is considered invalid. Most ProtoJSON serializers will emit a `Value` with a `null_value` set as a JSON `null` regardless of the integer value, and so will round trip to a `0` value.

Enums  
---  
`NULL_VALUE` | Null value.  
  
### Type

The type of the MCP Server spec. Additional values may be added in the future.

Enums  
---  
`TYPE_UNSPECIFIED` | Unspecified type.  
`NO_SPEC` | There is no spec for the MCP Server. The `content` field must be empty.  
`TOOL_SPEC` | The content is a MCP Tool Spec following the One MCP specification. The payload is the same as the `tools/list` response.  
  
### Type

The type of the endpoint spec. Additional values may be added in the future.

Enums  
---  
`TYPE_UNSPECIFIED` | Unspecified type.  
`NO_SPEC` | There is no spec for the Endpoint. The `content` field must be empty.  
  
### ProtocolBinding

The protocol binding of the interface.

Enums  
---  
`PROTOCOL_BINDING_UNSPECIFIED` | Unspecified transport protocol.  
`JSONRPC` | JSON-RPC specification.  
`GRPC` | gRPC specification.  
`HTTP_JSON` | HTTP+JSON specification.  
  
### Tool Annotations

[Tool annotations](https://modelcontextprotocol.io/specification/latest/schema#toolannotations) are sent to MCP clients to describe the basic risk of a given tool. Most clients treat these hints as untrusted, but they can be used to decide when a confirmation prompt might be sent to a user. 

Along with the title string, the following boolean hints are defined as follows: 

  * `readOnlyHint`: If true, the tool doesn't modify its environment. Default: false.
  * `destructiveHint`: If true, then the tool can perform destructive actions. If false, then the tool can only perform additive actions. Default: true.
  * `idempotentHint`: If true, then calling the tool repeatedly with the same arguments will have no additional effect on its environment. Default: false.
  * `openWorldHint`: If true, then the tool can interact with an 'open world' of external entities. If false, then the tool can only interact with internal entities. For example, a web search tool would be open world, while a memory tool would not be open world.



Destructive Hint: ❌ | Idempotent Hint: ✅ | Read Only Hint: ✅ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-17 UTC."],[],[]] 
