---
url: https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/list_bindings/
title: MCP Tools Reference: agentregistry.googleapis.com \u00a0|\u00a0 Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:06:28.955610+00:00
---

# MCP Tools Reference: agentregistry.googleapis.com  |  Agent Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/list_bindings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Reference ](https://docs.cloud.google.com/agent-registry/apis)



Send feedback 

#  MCP Tools Reference: agentregistry.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `list_bindings`

Return a paginated list of bindings within a specified Google Cloud project and location.

The following code sample shows how to use `curl` to call the `list_bindings` MCP tool. 

Curl Request  
---  
      
    
    curl --location 'https://agentregistry.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "list_bindings",
        "arguments": {
          // Provide these details according to the MCP tool specification.
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'  
  
## Input Schema

Message for requesting a list of Bindings.

### ListBindingsRequest

JSON representation  
---  
      
    
    {
      "parent": string,
      "pageSize": integer,
      "pageToken": string,
      "filter": string,
      "orderBy": string
    }  
  
Fields  
---  
`parent` |  `string` Required. The project and location to list bindings in. Expected format: `projects/{project}/locations/{location}`.  
`pageSize` |  `integer` Optional. Requested page size. Server may return fewer items than requested. Page size is 500 if unspecified and is capped at `500` even if a larger value is given.  
`pageToken` |  `string` Optional. A token identifying a page of results the server should return.  
`filter` |  `string` Optional. A query string used to filter the list of bindings returned. The filter expression must follow AIP-160 syntax.  
`orderBy` |  `string` Optional. Hint for how to order the results  
  
## Output Schema

Message for response to listing Bindings

### ListBindingsResponse

JSON representation  
---  
      
    
    {
      "bindings": [
        {
          object ([Binding](https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/list_bindings#Output.Schema.Binding))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`bindings[]` |  `object (`[Binding](https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/list_bindings#Output.Schema.Binding)`)` The list of Binding resources matching the parent and filter criteria in the request. Each Binding resource follows the format: `projects/{project}/locations/{location}/bindings/{binding}`.  
`nextPageToken` |  `string` A token identifying a page of results the server should return. Used in `page_token`.  
  
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
