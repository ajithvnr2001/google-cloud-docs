---
url: https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/get_agent/
title: MCP Tools Reference: agentregistry.googleapis.com \u00a0|\u00a0 Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:06:28.121510+00:00
---

# MCP Tools Reference: agentregistry.googleapis.com  |  Agent Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/get_agent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Reference ](https://docs.cloud.google.com/agent-registry/apis)



Send feedback 

#  MCP Tools Reference: agentregistry.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `get_agent`

Retrieve the full metadata and configuration details of a specific agent using its unique resource name. Use this when you already know the agent's ID and need to inspect its capabilities, protocols, or endpoints.

The following code sample shows how to use `curl` to call the `get_agent` MCP tool. 

Curl Request  
---  
      
    
    curl --location 'https://agentregistry.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "get_agent",
        "arguments": {
          // Provide these details according to the MCP tool specification.
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'  
  
## Input Schema

Message for getting a Agent

### GetAgentRequest

JSON representation  
---  
      
    
    {
      "name": string
    }  
  
Fields  
---  
`name` |  `string` Required. Name of the resource  
  
## Output Schema

Represents an Agent. "A2A" below refers to the Agent-to-Agent protocol.

### Agent

JSON representation  
---  
      
    
    {
      "name": string,
      "agentId": string,
      "location": string,
      "displayName": string,
      "description": string,
      "version": string,
      "protocols": [
        {
          object ([Protocol](https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/list_agents#Output.Schema.Protocol))
        }
      ],
      "skills": [
        {
          object ([Skill](https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/list_agents#Output.Schema.Skill))
        }
      ],
      "uid": string,
      "createTime": string,
      "updateTime": string,
      "attributes": {
        string: {
          object
        },
        ...
      },
      "card": {
        object ([Card](https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/list_agents#Output.Schema.Card))
      }
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of an Agent. Format: `projects/{project}/locations/{location}/agents/{agent}`.  
`agentId` |  `string` Output only. A stable, globally unique identifier for agents.  
`location` |  `string` Output only. The location where agent is hosted. The value is defined by the hosting environment (i.e. cloud provider).  
`displayName` |  `string` Output only. The display name of the agent, often obtained from the A2A Agent Card.  
`description` |  `string` Output only. The description of the Agent, often obtained from the A2A Agent Card. Empty if Agent Card has no description.  
`version` |  `string` Output only. The version of the Agent, often obtained from the A2A Agent Card. Empty if Agent Card has no version or agent is not an A2A Agent.  
`protocols[]` |  `object (`[Protocol](https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/list_agents#Output.Schema.Protocol)`)` Output only. The connection details for the Agent.  
`skills[]` |  `object (`[Skill](https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/list_agents#Output.Schema.Skill)`)` Output only. Skills the agent possesses, often obtained from the A2A Agent Card.  
`uid` |  `string` Output only. A universally unique identifier for the Agent.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Create time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Update time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`attributes` |  `map (key: string, value: object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format))` Output only. Attributes of the Agent. Valid values:

  * `agentregistry.googleapis.com/system/Framework`: {"framework": "google-adk"} - the agent framework used to develop the Agent. Example values: "google-adk", "langchain", "custom".
  * `agentregistry.googleapis.com/system/RuntimeIdentity`: {"principal": "principal://..."} - the runtime identity associated with the Agent.
  * `agentregistry.googleapis.com/system/RuntimeReference`: {"uri": "//..."}
  * the URI of the underlying resource hosting the Agent, for example, the Reasoning Engine URI.

An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`card` |  `object (`[Card](https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/list_agents#Output.Schema.Card)`)` Output only. Full Agent Card payload, when available.  
  
### Protocol

JSON representation  
---  
      
    
    {
      "type": enum ([Type](https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/list_agents#Output.Schema.Type)),
      "protocolVersion": string,
      "interfaces": [
        {
          object ([Interface](https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/list_agents#Output.Schema.Interface))
        }
      ]
    }  
  
Fields  
---  
`type` |  `enum (`[Type](https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/list_agents#Output.Schema.Type)`)` Output only. The type of the protocol.  
`protocolVersion` |  `string` Output only. The version of the protocol, for example, the A2A Agent Card version.  
`interfaces[]` |  `object (`[Interface](https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/list_agents#Output.Schema.Interface)`)` Output only. The connection details for the Agent.  
  
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
  
### Skill

JSON representation  
---  
      
    
    {
      "id": string,
      "name": string,
      "description": string,
      "tags": [
        string
      ],
      "examples": [
        string
      ]
    }  
  
Fields  
---  
`id` |  `string` Output only. A unique identifier for the agent's skill.  
`name` |  `string` Output only. A human-readable name for the agent's skill.  
`description` |  `string` Output only. A more detailed description of the skill.  
`tags[]` |  `string` Output only. Keywords describing the skill.  
`examples[]` |  `string` Output only. Example prompts or scenarios this skill can handle.  
  
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
  
### AttributesEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": {
        object
      }
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)`  
  
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
  
### Card

JSON representation  
---  
      
    
    {
      "type": enum ([Type](https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/list_agents#Output.Schema.Type_1)),
      "content": {
        object
      }
    }  
  
Fields  
---  
`type` |  `enum (`[Type](https://docs.cloud.google.com/agent-registry/reference/mcp/tools_list/list_agents#Output.Schema.Type_1)`)` Output only. The type of agent card.  
`content` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Output only. The content of the agent card.  
  
### Type

The type of the protocol.

Enums  
---  
`TYPE_UNSPECIFIED` | Unspecified type.  
`A2A_AGENT` | The interfaces point to an A2A Agent following the A2A specification.  
`CUSTOM` | Agent does not follow any standard protocol.  
  
### ProtocolBinding

The protocol binding of the interface.

Enums  
---  
`PROTOCOL_BINDING_UNSPECIFIED` | Unspecified transport protocol.  
`JSONRPC` | JSON-RPC specification.  
`GRPC` | gRPC specification.  
`HTTP_JSON` | HTTP+JSON specification.  
  
### NullValue

Represents a JSON `null`.

`NullValue` is a sentinel, using an enum with only one value to represent the null value for the `Value` type union.

A field of type `NullValue` with any value other than `0` is considered invalid. Most ProtoJSON serializers will emit a `Value` with a `null_value` set as a JSON `null` regardless of the integer value, and so will round trip to a `0` value.

Enums  
---  
`NULL_VALUE` | Null value.  
  
### Type

Represents the type of the agent card.

Enums  
---  
`TYPE_UNSPECIFIED` | Unspecified type.  
`A2A_AGENT_CARD` | Indicates that the card is an A2A Agent Card.  
  
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
