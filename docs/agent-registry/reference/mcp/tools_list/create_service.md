---
url: https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/create_service/
title: MCP Tools Reference: agentregistry.googleapis.com \u00a0|\u00a0 Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:06:28.884332+00:00
---

# MCP Tools Reference: agentregistry.googleapis.com  |  Agent Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/create_service/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Reference ](https://docs.cloud.google.com/agent-registry/apis)



Send feedback 

#  MCP Tools Reference: agentregistry.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `create_service`

Manually register a new custom workload by creating a Service resource. A service can represent a manually onboarded MCP server, agent or REST endpoint. Use this to onboard third-party agents, remote MCP servers, or REST endpoints by providing their specification.

The following code sample shows how to use `curl` to call the `create_service` MCP tool. 

Curl Request  
---  
      
    
    curl --location 'https://agentregistry.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "create_service",
        "arguments": {
          // Provide these details according to the MCP tool specification.
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'  
  
## Input Schema

Message for creating a Service

### CreateServiceRequest

JSON representation  
---  
      
    
    {
      "parent": string,
      "serviceId": string,
      "service": {
        object ([Service](https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/list_services#Output.Schema.Service))
      },
      "requestId": string
    }  
  
Fields  
---  
`parent` |  `string` Required. The project and location to create the Service in. Expected format: `projects/{project}/locations/{location}`.  
`serviceId` |  `string` Required. The ID to use for the service, which will become the final component of the service's resource name.This value should be 4-63 characters, and valid characters are `/[a-z][0-9]-/`.  
`service` |  `object (`[Service](https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/list_services#Output.Schema.Service)`)` Required. The Service resource that is being created. Format: `projects/{project}/locations/{location}/services/{service}`.  
`requestId` |  `string` Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).  
  
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
  
## Output Schema

This resource represents a long-running operation that is the result of a network API call.

### Operation

JSON representation  
---  
      
    
    {
      "name": string,
      "metadata": {
        "@type": string,
        field1: ...,
        ...
      },
      "done": boolean,
    
      // Union field result can be only one of the following:
      "error": {
        object ([Status](https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/create_service#Output.Schema.Status))
      },
      "response": {
        "@type": string,
        field1: ...,
        ...
      }
      // End of list of possible types for union field result.
    }  
  
Fields  
---  
`name` |  `string` The server-assigned name, which is only unique within the same service that originally returns it. If you use the default HTTP mapping, the `name` should be a resource name ending with `operations/{unique_id}`.  
`metadata` |  `object` Service-specific metadata associated with the operation. It typically contains progress information and common metadata such as create time. Some services might not provide such metadata. Any method that returns a long-running operation should document the metadata type, if any.An object containing fields of an arbitrary type. An additional field `"@type"` contains a URI identifying the type. Example: `{ "id": 1234, "@type": "types.example.com/standard/id" }`.  
`done` |  `boolean` If the value is `false`, it means the operation is still in progress. If `true`, the operation is completed, and either `error` or `response` is available.  
Union field `result`. The operation result, which can be either an `error` or a valid `response`. If `done` == `false`, neither `error` nor `response` is set. If `done` == `true`, exactly one of `error` or `response` can be set. Some services might not provide the result. `result` can be only one of the following:  
`error` |  `object (`[Status](https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/create_service#Output.Schema.Status)`)` The error result of the operation in case of failure or cancellation.  
`response` |  `object` The normal, successful response of the operation. If the original method returns no data on success, such as `Delete`, the response is `google.protobuf.Empty`. If the original method is standard `Get`/`Create`/`Update`, the response should be the resource. For other methods, the response should have the type `XxxResponse`, where `Xxx` is the original method name. For example, if the original method name is `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.An object containing fields of an arbitrary type. An additional field `"@type"` contains a URI identifying the type. Example: `{ "id": 1234, "@type": "types.example.com/standard/id" }`.  
  
### Any

JSON representation  
---  
      
    
    {
      "typeUrl": string,
      "value": string
    }  
  
Fields  
---  
`typeUrl` |  `string` Identifies the type of the serialized Protobuf message with a URI reference consisting of a prefix ending in a slash and the fully-qualified type name.Example: type.googleapis.com/google.protobuf.StringValueThis string must contain at least one `/` character, and the content after the last `/` must be the fully-qualified name of the type in canonical form, without a leading dot. Do not write a scheme on these URI references so that clients do not attempt to contact them.The prefix is arbitrary and Protobuf implementations are expected to simply strip off everything up to and including the last `/` to identify the type. `type.googleapis.com/` is a common default prefix that some legacy implementations require. This prefix does not indicate the origin of the type, and URIs containing it are not expected to respond to any requests.All type URL strings must be legal URI references with the additional restriction (for the text format) that the content of the reference must consist only of alphanumeric characters, percent-encoded escapes, and characters in the following set (not including the outer backticks): `/-.~_!$&()*+,;=`. Despite our allowing percent encodings, implementations should not unescape them to prevent confusion with existing parsers. For example, `type.googleapis.com%2FFoo` should be rejected.In the original design of `Any`, the possibility of launching a type resolution service at these type URLs was considered but Protobuf never implemented one and considers contacting these URLs to be problematic and a potential security issue. Do not attempt to contact type URLs.  
`value` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Holds a Protobuf serialization of the type described by type_url.A base64-encoded string.  
  
### Status

JSON representation  
---  
      
    
    {
      "code": integer,
      "message": string,
      "details": [
        {
          "@type": string,
          field1: ...,
          ...
        }
      ]
    }  
  
Fields  
---  
`code` |  `integer` The status code, which should be an enum value of `google.rpc.Code`.  
`message` |  `string` A developer-facing error message, which should be in English. Any user-facing error message should be localized and sent in the `google.rpc.Status.details` field, or localized by the client.  
`details[]` |  `object` A list of messages that carry the error details. There is a common set of message types for APIs to use.An object containing fields of an arbitrary type. An additional field `"@type"` contains a URI identifying the type. Example: `{ "id": 1234, "@type": "types.example.com/standard/id" }`.  
  
### Tool Annotations

[Tool annotations](https://modelcontextprotocol.io/specification/latest/schema#toolannotations) are sent to MCP clients to describe the basic risk of a given tool. Most clients treat these hints as untrusted, but they can be used to decide when a confirmation prompt might be sent to a user. 

Along with the title string, the following boolean hints are defined as follows: 

  * `readOnlyHint`: If true, the tool doesn't modify its environment. Default: false.
  * `destructiveHint`: If true, then the tool can perform destructive actions. If false, then the tool can only perform additive actions. Default: true.
  * `idempotentHint`: If true, then calling the tool repeatedly with the same arguments will have no additional effect on its environment. Default: false.
  * `openWorldHint`: If true, then the tool can interact with an 'open world' of external entities. If false, then the tool can only interact with internal entities. For example, a web search tool would be open world, while a memory tool would not be open world.



Destructive Hint: ✅ | Idempotent Hint: ❌ | Read Only Hint: ❌ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-17 UTC."],[],[]] 
