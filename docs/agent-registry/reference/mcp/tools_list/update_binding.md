---
url: https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/update_binding/
title: MCP Tools Reference: agentregistry.googleapis.com \u00a0|\u00a0 Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:06:29.416055+00:00
---

# MCP Tools Reference: agentregistry.googleapis.com  |  Agent Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/update_binding/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Reference ](https://docs.cloud.google.com/agent-registry/apis)



Send feedback 

#  MCP Tools Reference: agentregistry.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `update_binding`

Update the specification or parameters of an existing binding.

The following code sample shows how to use `curl` to call the `update_binding` MCP tool. 

Curl Request  
---  
      
    
    curl --location 'https://agentregistry.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "update_binding",
        "arguments": {
          // Provide these details according to the MCP tool specification.
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'  
  
## Input Schema

Message for updating a Binding

### UpdateBindingRequest

JSON representation  
---  
      
    
    {
      "binding": {
        object ([Binding](https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/list_bindings#Output.Schema.Binding))
      },
      "updateMask": string,
      "requestId": string
    }  
  
Fields  
---  
`binding` |  `object (`[Binding](https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/list_bindings#Output.Schema.Binding)`)` Required. The Binding resource that is being updated.  
`updateMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Optional. Field mask is used to specify the fields to be overwritten in the Binding resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields present in the request will be overwritten.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
`requestId` |  `string` Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).  
  
### Binding

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "source": {
        object ([Source](https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/list_bindings#Output.Schema.Source))
      },
      "target": {
        object ([Target](https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/list_bindings#Output.Schema.Target))
      },
      "createTime": string,
      "updateTime": string,
    
      // Union field binding can be only one of the following:
      "authProviderBinding": {
        object ([AuthProviderBinding](https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/list_bindings#Output.Schema.AuthProviderBinding))
      }
      // End of list of possible types for union field binding.
    }  
  
Fields  
---  
`name` |  `string` Required. Identifier. The resource name of the Binding. Format: `projects/{project}/locations/{location}/bindings/{binding}`.  
`displayName` |  `string` Optional. User-defined display name for the Binding. Can have a maximum length of `63` characters.  
`description` |  `string` Optional. User-defined description of a Binding. Can have a maximum length of `2048` characters.  
`source` |  `object (`[Source](https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/list_bindings#Output.Schema.Source)`)` Optional. The source Agent of the Binding.  
`target` |  `object (`[Target](https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/list_bindings#Output.Schema.Target)`)` Required. The target Agent Registry Resource of the Binding.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when this binding was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when this binding was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
Union field `binding`. The configuration for the Binding. `binding` can be only one of the following:  
`authProviderBinding` |  `object (`[AuthProviderBinding](https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/list_bindings#Output.Schema.AuthProviderBinding)`)` The binding for AuthProvider.  
  
### AuthProviderBinding

JSON representation  
---  
      
    
    {
      "authProvider": string,
      "scopes": [
        string
      ],
      "continueUri": string
    }  
  
Fields  
---  
`authProvider` |  `string` Required. The resource name of the target AuthProvider. Format:

  * `projects/{project}/locations/{location}/authProviders/{auth_provider}`

  
`scopes[]` |  `string` Optional. The list of OAuth2 scopes of the AuthProvider.  
`continueUri` |  `string` Optional. The continue URI of the AuthProvider. The URI is used to reauthenticate the user and finalize the managed OAuth flow.  
  
### Source

JSON representation  
---  
      
    
    {
    
      // Union field source_type can be only one of the following:
      "identifier": string
      // End of list of possible types for union field source_type.
    }  
  
Fields  
---  
Union field `source_type`. The type of the source, currently only supports Agents. Potential future fields include 'tag', etc. `source_type` can be only one of the following:  
`identifier` |  `string` The identifier of the source Agent. Format:

  * `urn:agent:{publisher}:{namespace}:{name}`

  
  
### Target

JSON representation  
---  
      
    
    {
    
      // Union field target_type can be only one of the following:
      "identifier": string
      // End of list of possible types for union field target_type.
    }  
  
Fields  
---  
Union field `target_type`. The type of the target, currently only supports an AgentRegistry Resource. Potential future fields include 'tag', etc. `target_type` can be only one of the following:  
`identifier` |  `string` The identifier of the target Agent, MCP Server, or Endpoint. Format:

  * `urn:agent:{publisher}:{namespace}:{name}`
  * `urn:mcp:{publisher}:{namespace}:{name}`
  * `urn:endpoint:{publisher}:{namespace}:{name}`

  
  
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
  
### FieldMask

JSON representation  
---  
      
    
    {
      "paths": [
        string
      ]
    }  
  
Fields  
---  
`paths[]` |  `string` The set of field mask paths.  
  
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
