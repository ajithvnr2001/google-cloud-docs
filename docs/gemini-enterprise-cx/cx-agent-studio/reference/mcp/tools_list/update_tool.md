---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/update_tool/
title: MCP Tools Reference: ces.googleapis.com \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:39:18.558820+00:00
---

# MCP Tools Reference: ces.googleapis.com  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/update_tool/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  MCP Tools Reference: ces.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `update_tool`

Updates the specified tool. Make sure to always pass an update mask in the input.

The following code sample shows how to use `curl` to call the `update_tool` MCP tool. 

Curl Request  
---  
      
    
    curl --location 'https://ces.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "update_tool",
        "arguments": {
          // Provide these details according to the MCP tool specification.
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'  
  
## Input Schema

Request message for `AgentService.UpdateTool`.

### UpdateToolRequest

JSON representation  
---  
      
    
    {
      "tool": {
        object ([Tool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.Tool))
      },
      "updateMask": string
    }  
  
Fields  
---  
`tool` |  `object (`[Tool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.Tool)`)` Required. The tool to update.  
`updateMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Optional. Field mask is used to control which fields get updated. If the mask is not present, all fields will be updated.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
  
### Tool

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "executionType": enum ([ExecutionType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ExecutionType)),
      "timeout": string,
      "createTime": string,
      "updateTime": string,
      "etag": string,
      "generatedSummary": string,
      "toolFakeConfig": {
        object ([ToolFakeConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ToolFakeConfig))
      },
      "readOnly": boolean,
    
      // Union field tool_type can be only one of the following:
      "clientFunction": {
        object ([ClientFunction](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ClientFunction))
      },
      "openApiTool": {
        object ([OpenApiTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.OpenApiTool))
      },
      "googleSearchTool": {
        object ([GoogleSearchTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.GoogleSearchTool))
      },
      "connectorTool": {
        object ([ConnectorTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ConnectorTool))
      },
      "dataStoreTool": {
        object ([DataStoreTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.DataStoreTool))
      },
      "pythonFunction": {
        object ([PythonFunction](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.PythonFunction))
      },
      "mcpTool": {
        object ([McpTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.McpTool))
      },
      "fileSearchTool": {
        object ([FileSearchTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.FileSearchTool))
      },
      "systemTool": {
        object ([SystemTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.SystemTool))
      },
      "agentTool": {
        object ([AgentTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.AgentTool))
      },
      "widgetTool": {
        object ([WidgetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.WidgetTool))
      },
      "remoteAgentTool": {
        object ([RemoteAgentTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.RemoteAgentTool))
      }
      // End of list of possible types for union field tool_type.
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the tool. Format:

  * `projects/{project}/locations/{location}/apps/{app}/tools/{tool}` for standalone tools.
  * `projects/{project}/locations/{location}/apps/{app}/toolsets/{toolset}/tools/{tool}` for tools retrieved from a toolset.

These tools are dynamic and output-only; they cannot be referenced directly where a tool is expected.  
`displayName` |  `string` Output only. The display name of the tool, derived based on the tool's type. For example, display name of a [ClientFunction][Tool.ClientFunction] is derived from its `name` property.  
`executionType` |  `enum (`[ExecutionType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ExecutionType)`)` Optional. The execution type of the tool.  
`timeout` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. The timeout for the tool execution. If not set, the default timeout is 30 seconds for `SYNCHRONOUS` tools and 60 seconds for `ASYNCHRONOUS` tools.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the tool was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the tool was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`etag` |  `string` Etag used to ensure the object hasn't changed during a read-modify-write operation. If the etag is empty, the update will overwrite any concurrent changes.  
`generatedSummary` |  `string` Output only. If the tool is generated by the LLM assistant, this field contains a descriptive summary of the generation.  
`toolFakeConfig` |  `object (`[ToolFakeConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ToolFakeConfig)`)` Optional. Configuration for tool behavior in fake mode.  
`readOnly` |  `boolean` Output only. Indicates whether the tool is read-only. If true, the tool cannot be modified by the user.  
Union field `tool_type`. The type of the tool. `tool_type` can be only one of the following:  
`clientFunction` |  `object (`[ClientFunction](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ClientFunction)`)` Optional. The client function.  
`openApiTool` |  `object (`[OpenApiTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.OpenApiTool)`)` Optional. The open API tool.  
`googleSearchTool` |  `object (`[GoogleSearchTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.GoogleSearchTool)`)` Optional. The google search tool.  
`connectorTool` |  `object (`[ConnectorTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ConnectorTool)`)` Optional. The Integration Connector tool.  
`dataStoreTool` |  `object (`[DataStoreTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.DataStoreTool)`)` Optional. The data store tool.  
`pythonFunction` |  `object (`[PythonFunction](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.PythonFunction)`)` Optional. The python function tool.  
`mcpTool` |  `object (`[McpTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.McpTool)`)` Optional. The MCP tool. An MCP tool cannot be created or updated directly and is managed by the MCP toolset.  
`fileSearchTool` |  `object (`[FileSearchTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.FileSearchTool)`)` Optional. The file search tool.  
`systemTool` |  `object (`[SystemTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.SystemTool)`)` Optional. The system tool.  
`agentTool` |  `object (`[AgentTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.AgentTool)`)` Optional. The agent tool.  
`widgetTool` |  `object (`[WidgetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.WidgetTool)`)` Optional. The widget tool.  
`remoteAgentTool` |  `object (`[RemoteAgentTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.RemoteAgentTool)`)` Optional. The remote agent tool.  
  
### ClientFunction

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "parameters": {
        object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema))
      },
      "response": {
        object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema))
      }
    }  
  
Fields  
---  
`name` |  `string` Required. The function name.  
`description` |  `string` Optional. The function description.  
`parameters` |  `object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema)`)` Optional. The schema of the function parameters.  
`response` |  `object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema)`)` Optional. The schema of the function response.  
  
### Schema

JSON representation  
---  
      
    
    {
      "type": enum ([Type](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Type)),
      "properties": {
        string: {
          object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema))
        },
        ...
      },
      "required": [
        string
      ],
      "description": string,
      "items": {
        object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema))
      },
      "nullable": boolean,
      "uniqueItems": boolean,
      "prefixItems": [
        {
          object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema))
        }
      ],
      "additionalProperties": {
        object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema))
      },
      "anyOf": [
        {
          object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema))
        }
      ],
      "enum": [
        string
      ],
      "default": value,
      "ref": string,
      "defs": {
        string: {
          object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema))
        },
        ...
      },
      "title": string,
      "minItems": string,
      "maxItems": string,
    
      // Union field _minimum can be only one of the following:
      "minimum": number
      // End of list of possible types for union field _minimum.
    
      // Union field _maximum can be only one of the following:
      "maximum": number
      // End of list of possible types for union field _maximum.
    }  
  
Fields  
---  
`type` |  `enum (`[Type](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Type)`)` Required. The type of the data.  
`properties` |  `map (key: string, value: object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema)`))` Optional. Properties of Type.OBJECT.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`required[]` |  `string` Optional. Required properties of Type.OBJECT.  
`description` |  `string` Optional. The description of the data.  
`items` |  `object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema)`)` Optional. Schema of the elements of Type.ARRAY.  
`nullable` |  `boolean` Optional. Indicates if the value may be null.  
`uniqueItems` |  `boolean` Optional. Indicate the items in the array must be unique. Only applies to TYPE.ARRAY.  
`prefixItems[]` |  `object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema)`)` Optional. Schemas of initial elements of Type.ARRAY.  
`additionalProperties` |  `object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema)`)` Optional. Can either be a boolean or an object, controls the presence of additional properties.  
`anyOf[]` |  `object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema)`)` Optional. The value should be validated against any (one or more) of the subschemas in the list.  
`enum[]` |  `string` Optional. Possible values of the element of primitive type with enum format. Examples: 1. We can define direction as : {type:STRING, format:enum, enum:["EAST", NORTH", "SOUTH", "WEST"]} 2. We can define apartment number as : {type:INTEGER, format:enum, enum:["101", "201", "301"]}  
`default` |  `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)` Optional. Default value of the data.  
`ref` |  `string` Optional. Allows indirect references between schema nodes. The value should be a valid reference to a child of the root `defs`.For example, the following schema defines a reference to a schema node named "Pet":
    
    
    type: object
    properties:
      pet:
        ref: #/defs/Pet
    defs:
      Pet:
        type: object
        properties:
          name:
            type: string
    

The value of the "pet" property is a reference to the schema node named "Pet". See details in <https://json-schema.org/understanding-json-schema/structuring>.  
`defs` |  `map (key: string, value: object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema)`))` Optional. A map of definitions for use by `ref`. Only allowed at the root of the schema.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`title` |  `string` Optional. The title of the schema.  
`minItems` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. Minimum number of the elements for Type.ARRAY.  
`maxItems` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. Maximum number of the elements for Type.ARRAY.  
Union field `_minimum`.`_minimum` can be only one of the following:  
`minimum` |  `number` Optional. Minimum value for Type.INTEGER and Type.NUMBER.  
Union field `_maximum`.`_maximum` can be only one of the following:  
`maximum` |  `number` Optional. Maximum value for Type.INTEGER and Type.NUMBER.  
  
### PropertiesEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": {
        object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema))
      }
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema)`)`  
  
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
  
### DefsEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": {
        object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema))
      }
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema)`)`  
  
### OpenApiTool

JSON representation  
---  
      
    
    {
      "openApiSchema": string,
      "name": string,
      "description": string,
      "apiAuthentication": {
        object ([ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ApiAuthentication))
      },
      "tlsConfig": {
        object ([TlsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.TlsConfig))
      },
      "serviceDirectoryConfig": {
        object ([ServiceDirectoryConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ServiceDirectoryConfig))
      },
      "ignoreUnknownFields": boolean,
      "url": string
    }  
  
Fields  
---  
`openApiSchema` |  `string` Required. The OpenAPI schema in JSON or YAML format.  
`name` |  `string` Optional. The name of the tool. If not provided, the name of the tool will be derived from the OpenAPI schema, from `operation.operationId`.  
`description` |  `string` Optional. The description of the tool. If not provided, the description of the tool will be derived from the OpenAPI schema, from `operation.description` or `operation.summary`.  
`apiAuthentication` |  `object (`[ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ApiAuthentication)`)` Optional. Authentication information required by the API.  
`tlsConfig` |  `object (`[TlsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.TlsConfig)`)` Optional. The TLS configuration. Includes the custom server certificates that the client will trust.  
`serviceDirectoryConfig` |  `object (`[ServiceDirectoryConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ServiceDirectoryConfig)`)` Optional. Service Directory configuration.  
`ignoreUnknownFields` |  `boolean` Optional. If true, the agent will ignore unknown fields in the API response.  
`url` |  `string` Optional. The server URL of the Open API schema. This field is only set in tools in the environment dependencies during the export process if the schema contains a server url. During the import process, if this url is present in the environment dependencies and the schema has the $env_var placeholder, it will replace the placeholder in the schema.  
  
### ApiAuthentication

JSON representation  
---  
      
    
    {
    
      // Union field auth_config can be only one of the following:
      "apiKeyConfig": {
        object ([ApiKeyConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ApiKeyConfig))
      },
      "oauthConfig": {
        object ([OAuthConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.OAuthConfig))
      },
      "serviceAgentIdTokenAuthConfig": {
        object (ServiceAgentIdTokenAuthConfig)
      },
      "serviceAccountAuthConfig": {
        object ([ServiceAccountAuthConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ServiceAccountAuthConfig))
      },
      "bearerTokenConfig": {
        object ([BearerTokenConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.BearerTokenConfig))
      }
      // End of list of possible types for union field auth_config.
    }  
  
Fields  
---  
Union field `auth_config`. The auth configuration. `auth_config` can be only one of the following:  
`apiKeyConfig` |  `object (`[ApiKeyConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ApiKeyConfig)`)` Optional. Config for API key auth.  
`oauthConfig` |  `object (`[OAuthConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.OAuthConfig)`)` Optional. Config for OAuth.  
`serviceAgentIdTokenAuthConfig` |  `object (`ServiceAgentIdTokenAuthConfig`)` Optional. Config for ID token auth generated from CES service agent.  
`serviceAccountAuthConfig` |  `object (`[ServiceAccountAuthConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ServiceAccountAuthConfig)`)` Optional. Config for service account authentication.  
`bearerTokenConfig` |  `object (`[BearerTokenConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.BearerTokenConfig)`)` Optional. Config for bearer token auth.  
  
### ApiKeyConfig

JSON representation  
---  
      
    
    {
      "keyName": string,
      "apiKeySecretVersion": string,
      "requestLocation": enum ([RequestLocation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.RequestLocation))
    }  
  
Fields  
---  
`keyName` |  `string` Required. The parameter name or the header name of the API key. E.g., If the API request is "https://example.com/act?X-Api-Key=", "X-Api-Key" would be the parameter name.  
`apiKeySecretVersion` |  `string` Required. The name of the SecretManager secret version resource storing the API key. Format: `projects/{project}/secrets/{secret}/versions/{version}`Note: You should grant `roles/secretmanager.secretAccessor` role to the CES service agent `service-<PROJECT-NUMBER>@gcp-sa-ces.iam.gserviceaccount.com`.  
`requestLocation` |  `enum (`[RequestLocation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.RequestLocation)`)` Required. Key location in the request.  
  
### OAuthConfig

JSON representation  
---  
      
    
    {
      "oauthGrantType": enum ([OauthGrantType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.OauthGrantType)),
      "clientId": string,
      "clientSecretVersion": string,
      "tokenEndpoint": string,
      "scopes": [
        string
      ]
    }  
  
Fields  
---  
`oauthGrantType` |  `enum (`[OauthGrantType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.OauthGrantType)`)` Required. OAuth grant types.  
`clientId` |  `string` Required. The client ID from the OAuth provider.  
`clientSecretVersion` |  `string` Required. The name of the SecretManager secret version resource storing the client secret. Format: `projects/{project}/secrets/{secret}/versions/{version}`Note: You should grant `roles/secretmanager.secretAccessor` role to the CES service agent `service-<PROJECT-NUMBER>@gcp-sa-ces.iam.gserviceaccount.com`.  
`tokenEndpoint` |  `string` Required. The token endpoint in the OAuth provider to exchange for an access token.  
`scopes[]` |  `string` Optional. The OAuth scopes to grant.  
  
### ServiceAccountAuthConfig

JSON representation  
---  
      
    
    {
      "serviceAccount": string,
      "scopes": [
        string
      ]
    }  
  
Fields  
---  
`serviceAccount` |  `string` Required. The email address of the service account used for authentication. CES uses this service account to exchange an access token and the access token is then sent in the `Authorization` header of the request.The service account must have the `roles/iam.serviceAccountTokenCreator` role granted to the CES service agent `service-<PROJECT-NUMBER>@gcp-sa-ces.iam.gserviceaccount.com`.  
`scopes[]` |  `string` Optional. The OAuth scopes to grant. If not specified, the default scope `https://www.googleapis.com/auth/cloud-platform` is used.  
  
### BearerTokenConfig

JSON representation  
---  
      
    
    {
      "token": string
    }  
  
Fields  
---  
`token` |  `string` Required. The bearer token. Must be in the format `$context.variables.<name_of_variable>`.  
  
### TlsConfig

JSON representation  
---  
      
    
    {
      "caCerts": [
        {
          object ([CaCert](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.CaCert))
        }
      ]
    }  
  
Fields  
---  
`caCerts[]` |  `object (`[CaCert](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.CaCert)`)` Required. Specifies a list of allowed custom CA certificates for HTTPS verification.  
  
### CaCert

JSON representation  
---  
      
    
    {
      "displayName": string,
      "cert": string
    }  
  
Fields  
---  
`displayName` |  `string` Required. The name of the allowed custom CA certificates. This can be used to disambiguate the custom CA certificates.  
`cert` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Required. The allowed custom CA certificates (in DER format) for HTTPS verification. This overrides the default SSL trust store. If this is empty or unspecified, CES will use Google's default trust store to verify certificates. N.B. Make sure the HTTPS server certificates are signed with "subject alt name". For instance a certificate can be self-signed using the following command:
    
    
       openssl x509 -req -days 200 -in example.com.csr \
         -signkey example.com.key \
         -out example.com.crt \
         -extfile <(printf "\nsubjectAltName='DNS:www.example.com'")
    

A base64-encoded string.  
  
### ServiceDirectoryConfig

JSON representation  
---  
      
    
    {
      "service": string
    }  
  
Fields  
---  
`service` |  `string` Required. The name of [Service Directory](https://cloud.google.com/service-directory) service. Format: `projects/{project}/locations/{location}/namespaces/{namespace}/services/{service}`. Location of the service directory must be the same as the location of the app.  
  
### GoogleSearchTool

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "contextUrls": [
        string
      ],
      "preferredDomains": [
        string
      ],
      "excludeDomains": [
        string
      ],
      "promptConfig": {
        object ([PromptConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.PromptConfig))
      }
    }  
  
Fields  
---  
`name` |  `string` Required. The name of the tool.  
`description` |  `string` Optional. Description of the tool's purpose.  
`contextUrls[]` |  `string` Optional. Content will be fetched directly from these URLs for context and grounding. Example: "https://example.com/path.html". A maximum of 20 URLs are allowed.  
`preferredDomains[]` |  `string` Optional. Specifies domains to restrict search results to. Example: "example.com", "another.site". A maximum of 20 domains can be specified.  
`excludeDomains[]` |  `string` Optional. List of domains to be excluded from the search results. Example: "example.com". A maximum of 2000 domains can be excluded.  
`promptConfig` |  `object (`[PromptConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.PromptConfig)`)` Optional. Prompt instructions passed to planner on how the search results should be processed for text and voice.  
  
### PromptConfig

JSON representation  
---  
      
    
    {
      "textPrompt": string,
      "voicePrompt": string
    }  
  
Fields  
---  
`textPrompt` |  `string` Optional. Defines the prompt used for the system instructions when interacting with the agent in chat conversations. If not set, default prompt will be used.  
`voicePrompt` |  `string` Optional. Defines the prompt used for the system instructions when interacting with the agent in voice conversations. If not set, default prompt will be used.  
  
### ConnectorTool

JSON representation  
---  
      
    
    {
      "connection": string,
      "action": {
        object ([Action](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.Action))
      },
      "authConfig": {
        object ([EndUserAuthConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.EndUserAuthConfig))
      },
      "name": string,
      "description": string
    }  
  
Fields  
---  
`connection` |  `string` Required. The full resource name of the referenced Integration Connectors Connection. Format: `projects/{project}/locations/{location}/connections/{connection}`  
`action` |  `object (`[Action](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.Action)`)` Required. Action for the tool to use.  
`authConfig` |  `object (`[EndUserAuthConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.EndUserAuthConfig)`)` Optional. Configures how authentication is handled in Integration Connectors. By default, an admin authentication is passed in the Integration Connectors API requests. You can override it with a different end-user authentication config. **Note** : The Connection must have authentication override enabled in order to specify an EUC configuration here - otherwise, the ConnectorTool creation will fail. See <https://cloud.google.com/application-integration/docs/configure-connectors-task#configure-authentication-override> for details.  
`name` |  `string` Optional. The name of the tool that can be used by the Agent to decide whether to call this ConnectorTool.  
`description` |  `string` Optional. The description of the tool that can be used by the Agent to decide whether to call this ConnectorTool.  
  
### Action

JSON representation  
---  
      
    
    {
      "inputFields": [
        string
      ],
      "outputFields": [
        string
      ],
    
      // Union field action_spec can be only one of the following:
      "connectionActionId": string,
      "entityOperation": {
        object ([EntityOperation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.EntityOperation))
      }
      // End of list of possible types for union field action_spec.
    }  
  
Fields  
---  
`inputFields[]` |  `string` Optional. Entity fields to use as inputs for the operation. If no fields are specified, all fields of the Entity will be used.  
`outputFields[]` |  `string` Optional. Entity fields to return from the operation. If no fields are specified, all fields of the Entity will be returned.  
Union field `action_spec`. Specification for an action to configure for the tool to use. `action_spec` can be only one of the following:  
`connectionActionId` |  `string` ID of a Connection action for the tool to use.  
`entityOperation` |  `object (`[EntityOperation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.EntityOperation)`)` Entity operation configuration for the tool to use.  
  
### EntityOperation

JSON representation  
---  
      
    
    {
      "entityId": string,
      "operation": enum ([OperationType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.OperationType))
    }  
  
Fields  
---  
`entityId` |  `string` Required. ID of the entity.  
`operation` |  `enum (`[OperationType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.OperationType)`)` Required. Operation to perform on the entity.  
  
### EndUserAuthConfig

JSON representation  
---  
      
    
    {
    
      // Union field auth_config can be only one of the following:
      "oauth2AuthCodeConfig": {
        object ([Oauth2AuthCodeConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.Oauth2AuthCodeConfig))
      },
      "oauth2JwtBearerConfig": {
        object ([Oauth2JwtBearerConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.Oauth2JwtBearerConfig))
      }
      // End of list of possible types for union field auth_config.
    }  
  
Fields  
---  
Union field `auth_config`. The auth configuration. `auth_config` can be only one of the following:  
`oauth2AuthCodeConfig` |  `object (`[Oauth2AuthCodeConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.Oauth2AuthCodeConfig)`)` Oauth 2.0 Authorization Code authentication.  
`oauth2JwtBearerConfig` |  `object (`[Oauth2JwtBearerConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.Oauth2JwtBearerConfig)`)` JWT Profile Oauth 2.0 Authorization Grant authentication.  
  
### Oauth2AuthCodeConfig

JSON representation  
---  
      
    
    {
      "oauthToken": string
    }  
  
Fields  
---  
`oauthToken` |  `string` Required. Oauth token parameter name to pass through. Must be in the format `$context.variables.<name_of_variable>`.  
  
### Oauth2JwtBearerConfig

JSON representation  
---  
      
    
    {
      "issuer": string,
      "subject": string,
      "clientKey": string
    }  
  
Fields  
---  
`issuer` |  `string` Required. Issuer parameter name to pass through. Must be in the format `$context.variables.<name_of_variable>`.  
`subject` |  `string` Required. Subject parameter name to pass through. Must be in the format `$context.variables.<name_of_variable>`.  
`clientKey` |  `string` Required. Client parameter name to pass through. Must be in the format `$context.variables.<name_of_variable>`.  
  
### DataStoreTool

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "boostSpecs": [
        {
          object ([BoostSpecs](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.BoostSpecs))
        }
      ],
      "modalityConfigs": [
        {
          object ([ModalityConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ModalityConfig))
        }
      ],
      "filterParameterBehavior": enum ([FilterParameterBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.FilterParameterBehavior)),
    
      // Union field search_source can be only one of the following:
      "dataStoreSource": {
        object ([DataStoreSource](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.DataStoreSource))
      },
      "engineSource": {
        object ([EngineSource](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.EngineSource))
      }
      // End of list of possible types for union field search_source.
    }  
  
Fields  
---  
`name` |  `string` Required. The data store tool name.  
`description` |  `string` Optional. The tool description.  
`boostSpecs[]` |  `object (`[BoostSpecs](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.BoostSpecs)`)` Optional. Boost specification to boost certain documents.  
`modalityConfigs[]` |  `object (`[ModalityConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ModalityConfig)`)` Optional. The modality configs for the data store.  
`filterParameterBehavior` |  `enum (`[FilterParameterBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.FilterParameterBehavior)`)` Optional. The filter parameter behavior.  
Union field `search_source`. Defines the search source, either a single DataStore or an Engine. `search_source` can be only one of the following:  
`dataStoreSource` |  `object (`[DataStoreSource](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.DataStoreSource)`)` Optional. Search within a single specific DataStore.  
`engineSource` |  `object (`[EngineSource](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.EngineSource)`)` Optional. Search within an Engine (potentially across multiple DataStores).  
  
### DataStoreSource

JSON representation  
---  
      
    
    {
      "filter": string,
      "dataStore": {
        object ([DataStore](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.DataStore))
      }
    }  
  
Fields  
---  
`filter` |  `string` Optional. Filter specification for the DataStore. See: <https://cloud.google.com/generative-ai-app-builder/docs/filter-search-metadata>  
`dataStore` |  `object (`[DataStore](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.DataStore)`)` Optional. The data store.  
  
### DataStore

JSON representation  
---  
      
    
    {
      "name": string,
      "type": enum ([DataStoreType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.DataStoreType)),
      "documentProcessingMode": enum ([DocumentProcessingMode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.DocumentProcessingMode)),
      "displayName": string,
      "createTime": string,
      "connectorConfig": {
        object ([ConnectorConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ConnectorConfig))
      }
    }  
  
Fields  
---  
`name` |  `string` Required. Full resource name of the DataStore. Format: `projects/{project}/locations/{location}/collections/{collection}/dataStores/{dataStore}`  
`type` |  `enum (`[DataStoreType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.DataStoreType)`)` Output only. The type of the data store. This field is readonly and populated by the server.  
`documentProcessingMode` |  `enum (`[DocumentProcessingMode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.DocumentProcessingMode)`)` Output only. The document processing mode for the data store connection. Only set for PUBLIC_WEB and UNSTRUCTURED data stores.  
`displayName` |  `string` Output only. The display name of the data store.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the data store was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`connectorConfig` |  `object (`[ConnectorConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ConnectorConfig)`)` Output only. The connector config for the data store connection.  
  
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
  
### ConnectorConfig

JSON representation  
---  
      
    
    {
      "collection": string,
      "collectionDisplayName": string,
      "dataSource": string
    }  
  
Fields  
---  
`collection` |  `string` Resource name of the collection the data store belongs to.  
`collectionDisplayName` |  `string` Display name of the collection the data store belongs to.  
`dataSource` |  `string` The name of the data source. Example: `salesforce`, `jira`, `confluence`, `bigquery`.  
  
### EngineSource

JSON representation  
---  
      
    
    {
      "engine": string,
      "dataStoreSources": [
        {
          object ([DataStoreSource](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.DataStoreSource))
        }
      ],
      "filter": string
    }  
  
Fields  
---  
`engine` |  `string` Required. Full resource name of the Engine. Format: `projects/{project}/locations/{location}/collections/{collection}/engines/{engine}`  
`dataStoreSources[]` |  `object (`[DataStoreSource](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.DataStoreSource)`)` Optional. Use to target specific DataStores within the Engine. If empty, the search applies to all DataStores associated with the Engine.  
`filter` |  `string` Optional. A filter applied to the search across the Engine. Not relevant and not used if 'data_store_sources' is provided. See: <https://cloud.google.com/generative-ai-app-builder/docs/filter-search-metadata>  
  
### BoostSpecs

JSON representation  
---  
      
    
    {
      "dataStores": [
        string
      ],
      "spec": [
        {
          object ([BoostSpec](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.BoostSpec))
        }
      ]
    }  
  
Fields  
---  
`dataStores[]` |  `string` Required. The Data Store where the boosting configuration is applied. Full resource name of DataStore, such as projects/{project}/locations/{location}/collections/{collection}/dataStores/{dataStore}.  
`spec[]` |  `object (`[BoostSpec](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.BoostSpec)`)` Required. A list of boosting specifications.  
  
### BoostSpec

JSON representation  
---  
      
    
    {
      "conditionBoostSpecs": [
        {
          object ([ConditionBoostSpec](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ConditionBoostSpec))
        }
      ]
    }  
  
Fields  
---  
`conditionBoostSpecs[]` |  `object (`[ConditionBoostSpec](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ConditionBoostSpec)`)` Required. A list of boosting specifications.  
  
### ConditionBoostSpec

JSON representation  
---  
      
    
    {
      "condition": string,
      "boost": number,
      "boostControlSpec": {
        object ([BoostControlSpec](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.BoostControlSpec))
      }
    }  
  
Fields  
---  
`condition` |  `string` Required. An expression which specifies a boost condition. The syntax is the same as filter expression syntax. Currently, the only supported condition is a list of BCP-47 lang codes. Example: To boost suggestions in languages en or fr: (lang_code: ANY("en", "fr"))  
`boost` |  `number` Optional. Strength of the boost, which should be in [-1, 1]. Negative boost means demotion. Default is 0.0.Setting to 1.0 gives the suggestions a big promotion. However, it does not necessarily mean that the top result will be a boosted suggestion.Setting to -1.0 gives the suggestions a big demotion. However, other suggestions that are relevant might still be shown.Setting to 0.0 means no boost applied. The boosting condition is ignored.  
`boostControlSpec` |  `object (`[BoostControlSpec](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.BoostControlSpec)`)` Optional. Complex specification for custom ranking based on customer defined attribute value.  
  
### BoostControlSpec

JSON representation  
---  
      
    
    {
      "fieldName": string,
      "attributeType": enum ([AttributeType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.AttributeType)),
      "interpolationType": enum ([InterpolationType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.InterpolationType)),
      "controlPoints": [
        {
          object ([ControlPoint](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ControlPoint))
        }
      ]
    }  
  
Fields  
---  
`fieldName` |  `string` Optional. The name of the field whose value will be used to determine the boost amount.  
`attributeType` |  `enum (`[AttributeType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.AttributeType)`)` Optional. The attribute type to be used to determine the boost amount. The attribute value can be derived from the field value of the specified field_name. In the case of numerical it is straightforward i.e. attribute_value = numerical_field_value. In the case of freshness however, attribute_value = (time.now() - datetime_field_value).  
`interpolationType` |  `enum (`[InterpolationType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.InterpolationType)`)` Optional. The interpolation type to be applied to connect the control points listed below.  
`controlPoints[]` |  `object (`[ControlPoint](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ControlPoint)`)` Optional. The control points used to define the curve. The monotonic function (defined through the interpolation_type above) passes through the control points listed here.  
  
### ControlPoint

JSON representation  
---  
      
    
    {
      "attributeValue": string,
      "boostAmount": number
    }  
  
Fields  
---  
`attributeValue` |  `string` Optional. Can be one of: 1. The numerical field value. 2. The duration spec for freshness: The value must be formatted as an XSD `dayTimeDuration` value (a restricted subset of an ISO 8601 duration value). The pattern for this is: `[nD][T[nH][nM][nS]]`.  
`boostAmount` |  `number` Optional. The value between -1 to 1 by which to boost the score if the attribute_value evaluates to the value specified above.  
  
### ModalityConfig

JSON representation  
---  
      
    
    {
      "modalityType": enum ([ModalityType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ModalityType)),
      "rewriterConfig": {
        object ([RewriterConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.RewriterConfig))
      },
      "summarizationConfig": {
        object ([SummarizationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.SummarizationConfig))
      },
      "groundingConfig": {
        object ([GroundingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.GroundingConfig))
      },
      "snippetsConfig": {
        object ([SnippetsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.SnippetsConfig))
      }
    }  
  
Fields  
---  
`modalityType` |  `enum (`[ModalityType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ModalityType)`)` Required. The modality type.  
`rewriterConfig` |  `object (`[RewriterConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.RewriterConfig)`)` Optional. The rewriter config.  
`summarizationConfig` |  `object (`[SummarizationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.SummarizationConfig)`)` Optional. The summarization config.  
`groundingConfig` |  `object (`[GroundingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.GroundingConfig)`)` Optional. The grounding configuration.  
`snippetsConfig` |  `object (`[SnippetsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.SnippetsConfig)`)` Optional. The snippets configuration.  
  
### RewriterConfig

JSON representation  
---  
      
    
    {
      "modelSettings": {
        object ([ModelSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ModelSettings))
      },
      "prompt": string,
      "disabled": boolean
    }  
  
Fields  
---  
`modelSettings` |  `object (`[ModelSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ModelSettings)`)` Required. Configurations for the LLM model.  
`prompt` |  `string` Optional. The prompt definition. If not set, default prompt will be used.  
`disabled` |  `boolean` Optional. Whether the rewriter is disabled.  
  
### ModelSettings

JSON representation  
---  
      
    
    {
      "model": string,
      "thinkingLevel": enum ([ThinkingLevel](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ThinkingLevel)),
    
      // Union field _temperature can be only one of the following:
      "temperature": number
      // End of list of possible types for union field _temperature.
    }  
  
Fields  
---  
`model` |  `string` Optional. The LLM model that the agent should use. If not set, the agent will inherit the model from its parent agent.  
`thinkingLevel` |  `enum (`[ThinkingLevel](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ThinkingLevel)`)` Optional. The thinking level of the model.  
Union field `_temperature`.`_temperature` can be only one of the following:  
`temperature` |  `number` Optional. If set, this temperature will be used for the LLM model. Temperature controls the randomness of the model's responses. Lower temperatures produce responses that are more predictable. Higher temperatures produce responses that are more creative.  
  
### SummarizationConfig

JSON representation  
---  
      
    
    {
      "modelSettings": {
        object ([ModelSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ModelSettings))
      },
      "prompt": string,
      "disabled": boolean
    }  
  
Fields  
---  
`modelSettings` |  `object (`[ModelSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ModelSettings)`)` Optional. Configurations for the LLM model.  
`prompt` |  `string` Optional. The prompt definition. If not set, default prompt will be used.  
`disabled` |  `boolean` Optional. Whether summarization is disabled.  
  
### GroundingConfig

JSON representation  
---  
      
    
    {
      "groundingLevel": number,
      "disabled": boolean
    }  
  
Fields  
---  
`groundingLevel` |  `number` Optional. The groundedness threshold of the answer based on the retrieved sources. The value has a configurable range of [1, 5]. The level is used to threshold the groundedness of the answer, meaning that all responses with a groundedness score below the threshold will fall back to returning relevant snippets only.For example, a level of 3 means that the groundedness score must be 3 or higher for the response to be returned.  
`disabled` |  `boolean` Optional. Whether grounding is disabled.  
  
### SnippetsConfig

JSON representation  
---  
      
    
    {
      "enableSnippets": boolean,
      "maxSnippets": integer
    }  
  
Fields  
---  
`enableSnippets` |  `boolean` Optional. Whether snippets are enabled.  
`maxSnippets` |  `integer` Optional. Number of snippets to return per query. If unset, returns all snippets from the service by default.  
  
### PythonFunction

JSON representation  
---  
      
    
    {
      "name": string,
      "pythonCode": string,
      "description": string,
      "serviceDirectoryConfig": {
        object ([ServiceDirectoryConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ServiceDirectoryConfig))
      }
    }  
  
Fields  
---  
`name` |  `string` Optional. The name of the Python function to execute. Must match a Python function name defined in the python code. Case sensitive. If the name is not provided, the first function defined in the python code will be used.  
`pythonCode` |  `string` Optional. The Python code to execute for the tool.  
`description` |  `string` Output only. The description of the Python function, parsed from the python code's docstring.  
`serviceDirectoryConfig` |  `object (`[ServiceDirectoryConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ServiceDirectoryConfig)`)` Optional. Service Directory configuration for the tool.  
  
### McpTool

JSON representation  
---  
      
    
    {
      "name": string,
      "nameOverride": string,
      "description": string,
      "inputSchema": {
        object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema))
      },
      "outputSchema": {
        object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema))
      },
      "serverAddress": string,
      "apiAuthentication": {
        object ([ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ApiAuthentication))
      },
      "tlsConfig": {
        object ([TlsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.TlsConfig))
      },
      "serviceDirectoryConfig": {
        object ([ServiceDirectoryConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ServiceDirectoryConfig))
      },
      "customHeaders": {
        string: string,
        ...
      },
      "state": enum ([State](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.State))
    }  
  
Fields  
---  
`name` |  `string` Required. The name of the MCP tool.  
`nameOverride` |  `string` Optional. The name override of the MCP tool. This is populated if the name was overridden by a Toolset override.  
`description` |  `string` Optional. The description of the MCP tool.  
`inputSchema` |  `object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema)`)` Optional. The schema of the input arguments of the MCP tool.  
`outputSchema` |  `object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema)`)` Optional. The schema of the output arguments of the MCP tool.  
`serverAddress` |  `string` Required. The server address of the MCP server, e.g., "https://example.com/mcp/". If the server is built with the MCP SDK, the url should be suffixed with "/mcp/". Only Streamable HTTP transport based servers are supported. This is the same as the server_address in the McpToolset. See <https://modelcontextprotocol.io/specification/2025-03-26/basic/transports#streamable-http> for more details.  
`apiAuthentication` |  `object (`[ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ApiAuthentication)`)` Optional. Authentication information required to execute the tool against the MCP server. For bearer token authentication, the token applies only to tool execution, not to listing tools. This requires that tools can be listed without authentication.  
`tlsConfig` |  `object (`[TlsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.TlsConfig)`)` Optional. The TLS configuration. Includes the custom server certificates that the client should trust.  
`serviceDirectoryConfig` |  `object (`[ServiceDirectoryConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ServiceDirectoryConfig)`)` Optional. Service Directory configuration for VPC-SC, used to resolve service names within a perimeter.  
`customHeaders` |  `map (key: string, value: string)` Optional. The custom headers to send in the request to the MCP server. The values must be in the format `$context.variables.<name_of_variable>` and can be set in the session variables. See <https://docs.cloud.google.com/customer-engagement-ai/conversational-agents/ps/tool/open-api#openapi-injection> for more details.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.State)`)` Output only. The dynamic availability state of the tool on the external server.  
  
### CustomHeadersEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `string`  
  
### FileSearchTool

JSON representation  
---  
      
    
    {
      "corpusType": enum ([CorpusType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.CorpusType)),
      "name": string,
      "description": string,
      "fileCorpus": string
    }  
  
Fields  
---  
`corpusType` |  `enum (`[CorpusType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.CorpusType)`)` Optional. The type of the corpus. Default is FULLY_MANAGED.  
`name` |  `string` Required. The tool name.  
`description` |  `string` Optional. The tool description.  
`fileCorpus` |  `string` Optional. The corpus where files are stored. Format: projects/{project}/locations/{location}/ragCorpora/{rag_corpus}  
  
### SystemTool

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string
    }  
  
Fields  
---  
`name` |  `string` Required. The name of the system tool.  
`description` |  `string` Output only. The description of the system tool.  
  
### AgentTool

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "agent": string
    }  
  
Fields  
---  
`name` |  `string` Required. The name of the agent tool.  
`description` |  `string` Optional. Description of the tool's purpose.  
`agent` |  `string` Optional. The resource name of the agent that is the entry point of the tool. Format: `projects/{project}/locations/{location}/agents/{agent}`  
  
### WidgetTool

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "widgetType": enum ([WidgetType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.WidgetType)),
      "uiConfig": {
        object
      },
      "dataMapping": {
        object ([DataMapping](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.DataMapping))
      },
      "textResponseConfig": {
        object ([TextResponseConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.TextResponseConfig))
      },
    
      // Union field input can be only one of the following:
      "parameters": {
        object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema))
      }
      // End of list of possible types for union field input.
    }  
  
Fields  
---  
`name` |  `string` Required. The display name of the widget tool.  
`description` |  `string` Optional. The description of the widget tool.  
`widgetType` |  `enum (`[WidgetType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.WidgetType)`)` Optional. The type of the widget tool. If not specified, the default type will be CUSTOMIZED.  
`uiConfig` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. Configuration for rendering the widget.  
`dataMapping` |  `object (`[DataMapping](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.DataMapping)`)` Optional. The mapping that defines how data from a source tool is mapped to the widget's input parameters.  
`textResponseConfig` |  `object (`[TextResponseConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.TextResponseConfig)`)` Optional. Configuration for always-included text responses.  
Union field `input`. The input of the widget tool. `input` can be only one of the following:  
`parameters` |  `object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema)`)` Optional. The input parameters of the widget tool.  
  
### DataMapping

JSON representation  
---  
      
    
    {
      "sourceToolName": string,
      "fieldMappings": {
        string: string,
        ...
      },
      "pythonFunction": {
        object ([PythonFunction](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.PythonFunction))
      },
      "mode": enum ([Mode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.Mode)),
      "pythonScript": string
    }  
  
Fields  
---  
`sourceToolName` |  `string` Optional. The resource name of the tool that provides the data for the widget (e.g., a search tool or a custom function). Format: `projects/{project}/locations/{location}/agents/{agent}/tools/{tool}`  
`fieldMappings` |  `map (key: string, value: string)` Optional. A map of widget input parameter fields to the corresponding output fields of the source tool.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`pythonFunction` |  `object (`[PythonFunction](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.PythonFunction)`)` Optional. Configuration for a Python function used to transform the source tool's output into the widget's input format.  
`mode` |  `enum (`[Mode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.Mode)`)` Optional. The mode of the data mapping.  
`pythonScript  
**(deprecated)**` |  `string` This item is deprecated!Deprecated: Use `python_function` instead.  
  
### FieldMappingsEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `string`  
  
### TextResponseConfig

JSON representation  
---  
      
    
    {
      "type": enum ([Type](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.Type_1)),
      "staticText": string,
      "textResponseInstruction": string
    }  
  
Fields  
---  
`type` |  `enum (`[Type](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.Type_1)`)` Optional. The strategy for providing the text response.  
`staticText` |  `string` Optional. The static text response to return when type is STATIC.  
`textResponseInstruction` |  `string` Optional. Instruction for the LLM on how to generate the text response. Used as the description for the text response parameter if type is LLM_GENERATED.  
  
### RemoteAgentTool

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "agentCard": {
        object ([AgentCard](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.AgentCard))
      },
      "apiAuthentication": {
        object ([ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ApiAuthentication))
      },
      "statefulAgent": boolean,
      "inputVariableMapping": {
        string: string,
        ...
      },
      "outputVariableMapping": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`name` |  `string` Required. The name of the tool.  
`description` |  `string` Required. The description of the tool.  
`agentCard` |  `object (`[AgentCard](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.AgentCard)`)` Required. The agent card of the remote agent that this tool invokes.  
`apiAuthentication` |  `object (`[ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ApiAuthentication)`)` Optional. Authentication configuration for calling the remote agent.  
`statefulAgent` |  `boolean` Optional. When enabled, the interaction between the CXAS app and the remote agent will share the same context. If the remote agent returns a context_id, it will be persisted for the entirety of the session for this remote agent tool.  
`inputVariableMapping` |  `map (key: string, value: string)` Optional. Mapping of input variable names of remote agent to GECX variable names.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`outputVariableMapping` |  `map (key: string, value: string)` Optional. Mapping of output variable names of remote agent to GECX variable names.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
### AgentCard

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "supportedInterfaces": [
        {
          object ([AgentInterface](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.AgentInterface))
        }
      ],
      "version": string,
      "skills": [
        {
          object ([AgentSkill](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.AgentSkill))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` Required. A human-readable name for the agent.  
`description` |  `string` Required. A description of the agent's domain of action/solution space.  
`supportedInterfaces[]` |  `object (`[AgentInterface](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.AgentInterface)`)` Required. Ordered list of supported interfaces. The first entry is preferred.  
`version` |  `string` Required. The version of the agent.  
`skills[]` |  `object (`[AgentSkill](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.AgentSkill)`)` Required. Skills represent a unit of ability an agent can perform. This may somewhat abstract but represents a more focused set of actions that the agent is highly likely to succeed at.  
  
### AgentInterface

JSON representation  
---  
      
    
    {
      "url": string,
      "protocolBinding": string,
      "tenant": string,
      "protocolVersion": string
    }  
  
Fields  
---  
`url` |  `string` Required. The URL where this interface is available. Must be a valid absolute HTTPS URL in production. Example: "https://api.example.com/a2a/v1", "https://grpc.example.com/a2a"  
`protocolBinding` |  `string` Required. The protocol binding supported at this URL. This is an open form string, to be easily extended for other protocol bindings. The core ones officially supported are `JSONRPC`, `GRPC` and `HTTP+JSON`.  
`tenant` |  `string` Tenant ID to be used in the request when calling the agent.  
`protocolVersion` |  `string` Required. The version of the A2A protocol this interface exposes. Use the latest supported minor version per major version. Examples: "0.3", "1.0"  
  
### AgentSkill

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
      ],
      "inputModes": [
        string
      ],
      "outputModes": [
        string
      ]
    }  
  
Fields  
---  
`id` |  `string` Required. A unique identifier for the agent's skill.  
`name` |  `string` Required. A human-readable name for the skill.  
`description` |  `string` Required. A detailed description of the skill.  
`tags[]` |  `string` Required. A set of keywords describing the skill's capabilities.  
`examples[]` |  `string` Example prompts or scenarios that this skill can handle.  
`inputModes[]` |  `string` The set of supported input media types for this skill, overriding the agent's defaults.  
`outputModes[]` |  `string` The set of supported output media types for this skill, overriding the agent's defaults.  
  
### InputVariableMappingEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `string`  
  
### OutputVariableMappingEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `string`  
  
### Duration

JSON representation  
---  
      
    
    {
      "seconds": string,
      "nanos": integer
    }  
  
Fields  
---  
`seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Signed seconds of the span of time. Must be from -315,576,000,000 to +315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`nanos` |  `integer` Signed fractions of a second at nanosecond resolution of the span of time. Durations less than one second are represented with a 0 `seconds` field and a positive or negative `nanos` field. For durations of one second or more, a non-zero value for the `nanos` field must be of the same sign as the `seconds` field. Must be from -999,999,999 to +999,999,999 inclusive.  
  
### ToolFakeConfig

JSON representation  
---  
      
    
    {
      "enableFakeMode": boolean,
    
      // Union field tool_response can be only one of the following:
      "codeBlock": {
        object ([CodeBlock](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.CodeBlock))
      }
      // End of list of possible types for union field tool_response.
    }  
  
Fields  
---  
`enableFakeMode` |  `boolean` Optional. Whether the tool is using fake mode.  
Union field `tool_response`. The response is either static or it is provided by a python function. `tool_response` can be only one of the following:  
`codeBlock` |  `object (`[CodeBlock](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.CodeBlock)`)` Optional. Code block which will be executed instead of a real tool call.  
  
### CodeBlock

JSON representation  
---  
      
    
    {
      "pythonCode": string
    }  
  
Fields  
---  
`pythonCode` |  `string` Required. Python code which will be invoked in tool fake mode. Expected Python function signature - To catch all tool calls: def fake_tool_call(tool: Tool, input: dict[str, Any], callback_context: CallbackContext) -> Optional[dict[str, Any]]: To catch a specific tool call: def fake_{tool_id}(tool: Tool, input: dict[str, Any], callback_context: CallbackContext) -> Optional[dict[str, Any]]: If the function returns None, the real tool will be invoked instead.  
  
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
  
### Type

OpenAPI data types.

Enums  
---  
`TYPE_UNSPECIFIED` | Type unspecified.  
`STRING` | String type.  
`INTEGER` | Integer type.  
`NUMBER` | Number type.  
`BOOLEAN` | Boolean type.  
`OBJECT` | Object type.  
`ARRAY` | Array type.  
  
### NullValue

Represents a JSON `null`.

`NullValue` is a sentinel, using an enum with only one value to represent the null value for the `Value` type union.

A field of type `NullValue` with any value other than `0` is considered invalid. Most ProtoJSON serializers will emit a `Value` with a `null_value` set as a JSON `null` regardless of the integer value, and so will round trip to a `0` value.

Enums  
---  
`NULL_VALUE` | Null value.  
  
### RequestLocation

The location of the API key in the request.

Enums  
---  
`REQUEST_LOCATION_UNSPECIFIED` | Unspecified. This value should not be used.  
`HEADER` | Represents the key in http header.  
`QUERY_STRING` | Represents the key in query string.  
  
### OauthGrantType

OAuth grant types. Only [client credential grant](https://oauth.net/2/grant-types/client-credentials) is supported.

Enums  
---  
`OAUTH_GRANT_TYPE_UNSPECIFIED` | Unspecified. Defaults to CLIENT_CREDENTIAL.  
`CLIENT_CREDENTIAL` | Represents the [client credential flow](https://oauth.net/2/grant-types/client-credentials).  
  
### OperationType

The operation to perform on the entity.

Enums  
---  
`OPERATION_TYPE_UNSPECIFIED` | Operation type unspecified. Invalid, ConnectorTool create/update will fail.  
`LIST` | List operation.  
`GET` | Get operation.  
`CREATE` | Create operation.  
`UPDATE` | Update operation.  
`DELETE` | Delete operation.  
  
### DataStoreType

The type of the data store.

Enums  
---  
`DATA_STORE_TYPE_UNSPECIFIED` | Not specified. This value indicates that the data store type is not specified, so it will not be used during search.  
`PUBLIC_WEB` | A data store that contains public web content.  
`UNSTRUCTURED` | A data store that contains unstructured private data.  
`FAQ` | A data store that contains structured data used as FAQ.  
`CONNECTOR` | A data store that is a connector to a first-party or a third-party service.  
  
### DocumentProcessingMode

The document processing mode of the data store.

Enums  
---  
`DOCUMENT_PROCESSING_MODE_UNSPECIFIED` | Not specified.  
`DOCUMENTS` | Documents are processed as documents.  
`CHUNKS` | Documents are converted to chunks.  
  
### AttributeType

The attribute(or function) for which the custom ranking is to be applied.

Enums  
---  
`ATTRIBUTE_TYPE_UNSPECIFIED` | Unspecified AttributeType.  
`NUMERICAL` | The value of the numerical field will be used to dynamically update the boost amount. In this case, the attribute_value (the x value) of the control point will be the actual value of the numerical field for which the boost_amount is specified.  
`FRESHNESS` | For the freshness use case the attribute value will be the duration between the current time and the date in the datetime field specified. The value must be formatted as an XSD `dayTimeDuration` value (a restricted subset of an ISO 8601 duration value). The pattern for this is: `[nD][T[nH][nM][nS]]`. E.g. `5D`, `3DT12H30M`, `T24H`.  
  
### InterpolationType

The interpolation type to be applied. Default will be linear (Piecewise Linear).

Enums  
---  
`INTERPOLATION_TYPE_UNSPECIFIED` | Interpolation type is unspecified. In this case, it defaults to Linear.  
`LINEAR` | Piecewise linear interpolation will be applied.  
  
### ModalityType

The modality type.

Enums  
---  
`MODALITY_TYPE_UNSPECIFIED` | Unspecified modality type.  
`TEXT` | Text modality.  
`AUDIO` | Audio modality.  
  
### ThinkingLevel

Thinking level configuration for the model.

Enums  
---  
`THINKING_LEVEL_UNSPECIFIED` | Thinking level is unspecified.  
`DEFAULT` | Default thinking level.  
`LOW` | Low thinking level.  
`MEDIUM` | Medium thinking level.  
`HIGH` | High thinking level.  
  
### FilterParameterBehavior

Filter parameter behavior.

Enums  
---  
`FILTER_PARAMETER_BEHAVIOR_UNSPECIFIED` | Default filter behavior. Include filter parameter for connector datastores. For the rest of the datastore types, the filter input parameter is omitted.  
`ALWAYS_INCLUDE` | Always include filter parameter for all datastore types.  
`NEVER_INCLUDE` | The filter parameter is never included in the list of tool parameters, regardless of the datastore type.  
  
### State

Represents the dynamic availability state of the tool.

Enums  
---  
`STATE_UNSPECIFIED` | Default state.  
`ACTIVE` | The tool is available and actively offered by the server.  
`INACTIVE` | The tool is configured or pinned, but currently not offered by the server.  
`STALE` | The tool exists on the server, but does not match the version on the server.  
  
### CorpusType

The type of the Vertex RAG corpus.

Enums  
---  
`CORPUS_TYPE_UNSPECIFIED` | Unspecified corpus type.  
`USER_OWNED` | The corpus is created and owned by the user.  
`FULLY_MANAGED` | The corpus is created by the agent.  
  
### WidgetType

All available widget types. New values may be added to this enum in the future.

Enums  
---  
`WIDGET_TYPE_UNSPECIFIED` | Unspecified widget type.  
`CUSTOM` | Custom widget type.  
`PRODUCT_CAROUSEL` | Product carousel widget.  
`PRODUCT_DETAILS` | Product details widget.  
`QUICK_ACTIONS` | Quick actions widget.  
`PRODUCT_COMPARISON` | Product comparison widget.  
`ADVANCED_PRODUCT_DETAILS` | Advanced product details widget.  
`SHORT_FORM` | Short form widget.  
`OVERALL_SATISFACTION` | Overall satisfaction widget.  
`ORDER_SUMMARY` | Order summary widget.  
`APPOINTMENT_DETAILS` | Appointment details widget.  
`APPOINTMENT_SCHEDULER` | Appointment scheduler widget.  
`CONTACT_FORM` | Contact form widget.  
  
### Mode

The strategy used to map data from the source tool to the widget.

Enums  
---  
`MODE_UNSPECIFIED` | Unspecified mode.  
`FIELD_MAPPING` | Use the `field_mappings` map for data transformation.  
`PYTHON_SCRIPT` | Use the `python_script` for data transformation.  
  
### Type

Defines how the text response is produced.

Enums  
---  
`TYPE_UNSPECIFIED` | Unspecified type.  
`NONE` | The LLM dynamically decides whether to generate a text response alongside the widget based on the conversation context.  
`LLM_GENERATED` | The LLM is explicitly required to generate a text response.  
`STATIC` | A pre-defined static text response is always used.  
  
### ExecutionType

The execution type of the tool or toolset.

Enums  
---  
`EXECUTION_TYPE_UNSPECIFIED` | The execution type is unspecified. Defaults to `SYNCHRONOUS` if unspecified.  
`SYNCHRONOUS` | The tool is executed synchronously. The session is blocked until the tool returns.  
`ASYNCHRONOUS` | The tool is executed asynchronously. The session will continue while the tool is executing.  
  
## Output Schema

A tool represents an action that the CES agent can take to achieve certain goals.

### Tool

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "executionType": enum ([ExecutionType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ExecutionType)),
      "timeout": string,
      "createTime": string,
      "updateTime": string,
      "etag": string,
      "generatedSummary": string,
      "toolFakeConfig": {
        object ([ToolFakeConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ToolFakeConfig))
      },
      "readOnly": boolean,
    
      // Union field tool_type can be only one of the following:
      "clientFunction": {
        object ([ClientFunction](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ClientFunction))
      },
      "openApiTool": {
        object ([OpenApiTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.OpenApiTool))
      },
      "googleSearchTool": {
        object ([GoogleSearchTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.GoogleSearchTool))
      },
      "connectorTool": {
        object ([ConnectorTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ConnectorTool))
      },
      "dataStoreTool": {
        object ([DataStoreTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.DataStoreTool))
      },
      "pythonFunction": {
        object ([PythonFunction](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.PythonFunction))
      },
      "mcpTool": {
        object ([McpTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.McpTool))
      },
      "fileSearchTool": {
        object ([FileSearchTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.FileSearchTool))
      },
      "systemTool": {
        object ([SystemTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.SystemTool))
      },
      "agentTool": {
        object ([AgentTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.AgentTool))
      },
      "widgetTool": {
        object ([WidgetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.WidgetTool))
      },
      "remoteAgentTool": {
        object ([RemoteAgentTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.RemoteAgentTool))
      }
      // End of list of possible types for union field tool_type.
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the tool. Format:

  * `projects/{project}/locations/{location}/apps/{app}/tools/{tool}` for standalone tools.
  * `projects/{project}/locations/{location}/apps/{app}/toolsets/{toolset}/tools/{tool}` for tools retrieved from a toolset.

These tools are dynamic and output-only; they cannot be referenced directly where a tool is expected.  
`displayName` |  `string` Output only. The display name of the tool, derived based on the tool's type. For example, display name of a [ClientFunction][Tool.ClientFunction] is derived from its `name` property.  
`executionType` |  `enum (`[ExecutionType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ExecutionType)`)` Optional. The execution type of the tool.  
`timeout` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. The timeout for the tool execution. If not set, the default timeout is 30 seconds for `SYNCHRONOUS` tools and 60 seconds for `ASYNCHRONOUS` tools.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the tool was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the tool was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`etag` |  `string` Etag used to ensure the object hasn't changed during a read-modify-write operation. If the etag is empty, the update will overwrite any concurrent changes.  
`generatedSummary` |  `string` Output only. If the tool is generated by the LLM assistant, this field contains a descriptive summary of the generation.  
`toolFakeConfig` |  `object (`[ToolFakeConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ToolFakeConfig)`)` Optional. Configuration for tool behavior in fake mode.  
`readOnly` |  `boolean` Output only. Indicates whether the tool is read-only. If true, the tool cannot be modified by the user.  
Union field `tool_type`. The type of the tool. `tool_type` can be only one of the following:  
`clientFunction` |  `object (`[ClientFunction](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ClientFunction)`)` Optional. The client function.  
`openApiTool` |  `object (`[OpenApiTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.OpenApiTool)`)` Optional. The open API tool.  
`googleSearchTool` |  `object (`[GoogleSearchTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.GoogleSearchTool)`)` Optional. The google search tool.  
`connectorTool` |  `object (`[ConnectorTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ConnectorTool)`)` Optional. The Integration Connector tool.  
`dataStoreTool` |  `object (`[DataStoreTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.DataStoreTool)`)` Optional. The data store tool.  
`pythonFunction` |  `object (`[PythonFunction](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.PythonFunction)`)` Optional. The python function tool.  
`mcpTool` |  `object (`[McpTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.McpTool)`)` Optional. The MCP tool. An MCP tool cannot be created or updated directly and is managed by the MCP toolset.  
`fileSearchTool` |  `object (`[FileSearchTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.FileSearchTool)`)` Optional. The file search tool.  
`systemTool` |  `object (`[SystemTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.SystemTool)`)` Optional. The system tool.  
`agentTool` |  `object (`[AgentTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.AgentTool)`)` Optional. The agent tool.  
`widgetTool` |  `object (`[WidgetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.WidgetTool)`)` Optional. The widget tool.  
`remoteAgentTool` |  `object (`[RemoteAgentTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.RemoteAgentTool)`)` Optional. The remote agent tool.  
  
### ClientFunction

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "parameters": {
        object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema))
      },
      "response": {
        object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema))
      }
    }  
  
Fields  
---  
`name` |  `string` Required. The function name.  
`description` |  `string` Optional. The function description.  
`parameters` |  `object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema)`)` Optional. The schema of the function parameters.  
`response` |  `object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema)`)` Optional. The schema of the function response.  
  
### Schema

JSON representation  
---  
      
    
    {
      "type": enum ([Type](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Type)),
      "properties": {
        string: {
          object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema))
        },
        ...
      },
      "required": [
        string
      ],
      "description": string,
      "items": {
        object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema))
      },
      "nullable": boolean,
      "uniqueItems": boolean,
      "prefixItems": [
        {
          object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema))
        }
      ],
      "additionalProperties": {
        object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema))
      },
      "anyOf": [
        {
          object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema))
        }
      ],
      "enum": [
        string
      ],
      "default": value,
      "ref": string,
      "defs": {
        string: {
          object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema))
        },
        ...
      },
      "title": string,
      "minItems": string,
      "maxItems": string,
    
      // Union field _minimum can be only one of the following:
      "minimum": number
      // End of list of possible types for union field _minimum.
    
      // Union field _maximum can be only one of the following:
      "maximum": number
      // End of list of possible types for union field _maximum.
    }  
  
Fields  
---  
`type` |  `enum (`[Type](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Type)`)` Required. The type of the data.  
`properties` |  `map (key: string, value: object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema)`))` Optional. Properties of Type.OBJECT.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`required[]` |  `string` Optional. Required properties of Type.OBJECT.  
`description` |  `string` Optional. The description of the data.  
`items` |  `object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema)`)` Optional. Schema of the elements of Type.ARRAY.  
`nullable` |  `boolean` Optional. Indicates if the value may be null.  
`uniqueItems` |  `boolean` Optional. Indicate the items in the array must be unique. Only applies to TYPE.ARRAY.  
`prefixItems[]` |  `object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema)`)` Optional. Schemas of initial elements of Type.ARRAY.  
`additionalProperties` |  `object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema)`)` Optional. Can either be a boolean or an object, controls the presence of additional properties.  
`anyOf[]` |  `object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema)`)` Optional. The value should be validated against any (one or more) of the subschemas in the list.  
`enum[]` |  `string` Optional. Possible values of the element of primitive type with enum format. Examples: 1. We can define direction as : {type:STRING, format:enum, enum:["EAST", NORTH", "SOUTH", "WEST"]} 2. We can define apartment number as : {type:INTEGER, format:enum, enum:["101", "201", "301"]}  
`default` |  `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)` Optional. Default value of the data.  
`ref` |  `string` Optional. Allows indirect references between schema nodes. The value should be a valid reference to a child of the root `defs`.For example, the following schema defines a reference to a schema node named "Pet":
    
    
    type: object
    properties:
      pet:
        ref: #/defs/Pet
    defs:
      Pet:
        type: object
        properties:
          name:
            type: string
    

The value of the "pet" property is a reference to the schema node named "Pet". See details in <https://json-schema.org/understanding-json-schema/structuring>.  
`defs` |  `map (key: string, value: object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema)`))` Optional. A map of definitions for use by `ref`. Only allowed at the root of the schema.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`title` |  `string` Optional. The title of the schema.  
`minItems` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. Minimum number of the elements for Type.ARRAY.  
`maxItems` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. Maximum number of the elements for Type.ARRAY.  
Union field `_minimum`.`_minimum` can be only one of the following:  
`minimum` |  `number` Optional. Minimum value for Type.INTEGER and Type.NUMBER.  
Union field `_maximum`.`_maximum` can be only one of the following:  
`maximum` |  `number` Optional. Maximum value for Type.INTEGER and Type.NUMBER.  
  
### PropertiesEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": {
        object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema))
      }
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema)`)`  
  
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
  
### DefsEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": {
        object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema))
      }
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema)`)`  
  
### OpenApiTool

JSON representation  
---  
      
    
    {
      "openApiSchema": string,
      "name": string,
      "description": string,
      "apiAuthentication": {
        object ([ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ApiAuthentication))
      },
      "tlsConfig": {
        object ([TlsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.TlsConfig))
      },
      "serviceDirectoryConfig": {
        object ([ServiceDirectoryConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ServiceDirectoryConfig))
      },
      "ignoreUnknownFields": boolean,
      "url": string
    }  
  
Fields  
---  
`openApiSchema` |  `string` Required. The OpenAPI schema in JSON or YAML format.  
`name` |  `string` Optional. The name of the tool. If not provided, the name of the tool will be derived from the OpenAPI schema, from `operation.operationId`.  
`description` |  `string` Optional. The description of the tool. If not provided, the description of the tool will be derived from the OpenAPI schema, from `operation.description` or `operation.summary`.  
`apiAuthentication` |  `object (`[ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ApiAuthentication)`)` Optional. Authentication information required by the API.  
`tlsConfig` |  `object (`[TlsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.TlsConfig)`)` Optional. The TLS configuration. Includes the custom server certificates that the client will trust.  
`serviceDirectoryConfig` |  `object (`[ServiceDirectoryConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ServiceDirectoryConfig)`)` Optional. Service Directory configuration.  
`ignoreUnknownFields` |  `boolean` Optional. If true, the agent will ignore unknown fields in the API response.  
`url` |  `string` Optional. The server URL of the Open API schema. This field is only set in tools in the environment dependencies during the export process if the schema contains a server url. During the import process, if this url is present in the environment dependencies and the schema has the $env_var placeholder, it will replace the placeholder in the schema.  
  
### ApiAuthentication

JSON representation  
---  
      
    
    {
    
      // Union field auth_config can be only one of the following:
      "apiKeyConfig": {
        object ([ApiKeyConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ApiKeyConfig))
      },
      "oauthConfig": {
        object ([OAuthConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.OAuthConfig))
      },
      "serviceAgentIdTokenAuthConfig": {
        object (ServiceAgentIdTokenAuthConfig)
      },
      "serviceAccountAuthConfig": {
        object ([ServiceAccountAuthConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ServiceAccountAuthConfig))
      },
      "bearerTokenConfig": {
        object ([BearerTokenConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.BearerTokenConfig))
      }
      // End of list of possible types for union field auth_config.
    }  
  
Fields  
---  
Union field `auth_config`. The auth configuration. `auth_config` can be only one of the following:  
`apiKeyConfig` |  `object (`[ApiKeyConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ApiKeyConfig)`)` Optional. Config for API key auth.  
`oauthConfig` |  `object (`[OAuthConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.OAuthConfig)`)` Optional. Config for OAuth.  
`serviceAgentIdTokenAuthConfig` |  `object (`ServiceAgentIdTokenAuthConfig`)` Optional. Config for ID token auth generated from CES service agent.  
`serviceAccountAuthConfig` |  `object (`[ServiceAccountAuthConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ServiceAccountAuthConfig)`)` Optional. Config for service account authentication.  
`bearerTokenConfig` |  `object (`[BearerTokenConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.BearerTokenConfig)`)` Optional. Config for bearer token auth.  
  
### ApiKeyConfig

JSON representation  
---  
      
    
    {
      "keyName": string,
      "apiKeySecretVersion": string,
      "requestLocation": enum ([RequestLocation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.RequestLocation))
    }  
  
Fields  
---  
`keyName` |  `string` Required. The parameter name or the header name of the API key. E.g., If the API request is "https://example.com/act?X-Api-Key=", "X-Api-Key" would be the parameter name.  
`apiKeySecretVersion` |  `string` Required. The name of the SecretManager secret version resource storing the API key. Format: `projects/{project}/secrets/{secret}/versions/{version}`Note: You should grant `roles/secretmanager.secretAccessor` role to the CES service agent `service-<PROJECT-NUMBER>@gcp-sa-ces.iam.gserviceaccount.com`.  
`requestLocation` |  `enum (`[RequestLocation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.RequestLocation)`)` Required. Key location in the request.  
  
### OAuthConfig

JSON representation  
---  
      
    
    {
      "oauthGrantType": enum ([OauthGrantType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.OauthGrantType)),
      "clientId": string,
      "clientSecretVersion": string,
      "tokenEndpoint": string,
      "scopes": [
        string
      ]
    }  
  
Fields  
---  
`oauthGrantType` |  `enum (`[OauthGrantType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.OauthGrantType)`)` Required. OAuth grant types.  
`clientId` |  `string` Required. The client ID from the OAuth provider.  
`clientSecretVersion` |  `string` Required. The name of the SecretManager secret version resource storing the client secret. Format: `projects/{project}/secrets/{secret}/versions/{version}`Note: You should grant `roles/secretmanager.secretAccessor` role to the CES service agent `service-<PROJECT-NUMBER>@gcp-sa-ces.iam.gserviceaccount.com`.  
`tokenEndpoint` |  `string` Required. The token endpoint in the OAuth provider to exchange for an access token.  
`scopes[]` |  `string` Optional. The OAuth scopes to grant.  
  
### ServiceAccountAuthConfig

JSON representation  
---  
      
    
    {
      "serviceAccount": string,
      "scopes": [
        string
      ]
    }  
  
Fields  
---  
`serviceAccount` |  `string` Required. The email address of the service account used for authentication. CES uses this service account to exchange an access token and the access token is then sent in the `Authorization` header of the request.The service account must have the `roles/iam.serviceAccountTokenCreator` role granted to the CES service agent `service-<PROJECT-NUMBER>@gcp-sa-ces.iam.gserviceaccount.com`.  
`scopes[]` |  `string` Optional. The OAuth scopes to grant. If not specified, the default scope `https://www.googleapis.com/auth/cloud-platform` is used.  
  
### BearerTokenConfig

JSON representation  
---  
      
    
    {
      "token": string
    }  
  
Fields  
---  
`token` |  `string` Required. The bearer token. Must be in the format `$context.variables.<name_of_variable>`.  
  
### TlsConfig

JSON representation  
---  
      
    
    {
      "caCerts": [
        {
          object ([CaCert](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.CaCert))
        }
      ]
    }  
  
Fields  
---  
`caCerts[]` |  `object (`[CaCert](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.CaCert)`)` Required. Specifies a list of allowed custom CA certificates for HTTPS verification.  
  
### CaCert

JSON representation  
---  
      
    
    {
      "displayName": string,
      "cert": string
    }  
  
Fields  
---  
`displayName` |  `string` Required. The name of the allowed custom CA certificates. This can be used to disambiguate the custom CA certificates.  
`cert` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Required. The allowed custom CA certificates (in DER format) for HTTPS verification. This overrides the default SSL trust store. If this is empty or unspecified, CES will use Google's default trust store to verify certificates. N.B. Make sure the HTTPS server certificates are signed with "subject alt name". For instance a certificate can be self-signed using the following command:
    
    
       openssl x509 -req -days 200 -in example.com.csr \
         -signkey example.com.key \
         -out example.com.crt \
         -extfile <(printf "\nsubjectAltName='DNS:www.example.com'")
    

A base64-encoded string.  
  
### ServiceDirectoryConfig

JSON representation  
---  
      
    
    {
      "service": string
    }  
  
Fields  
---  
`service` |  `string` Required. The name of [Service Directory](https://cloud.google.com/service-directory) service. Format: `projects/{project}/locations/{location}/namespaces/{namespace}/services/{service}`. Location of the service directory must be the same as the location of the app.  
  
### GoogleSearchTool

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "contextUrls": [
        string
      ],
      "preferredDomains": [
        string
      ],
      "excludeDomains": [
        string
      ],
      "promptConfig": {
        object ([PromptConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.PromptConfig))
      }
    }  
  
Fields  
---  
`name` |  `string` Required. The name of the tool.  
`description` |  `string` Optional. Description of the tool's purpose.  
`contextUrls[]` |  `string` Optional. Content will be fetched directly from these URLs for context and grounding. Example: "https://example.com/path.html". A maximum of 20 URLs are allowed.  
`preferredDomains[]` |  `string` Optional. Specifies domains to restrict search results to. Example: "example.com", "another.site". A maximum of 20 domains can be specified.  
`excludeDomains[]` |  `string` Optional. List of domains to be excluded from the search results. Example: "example.com". A maximum of 2000 domains can be excluded.  
`promptConfig` |  `object (`[PromptConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.PromptConfig)`)` Optional. Prompt instructions passed to planner on how the search results should be processed for text and voice.  
  
### PromptConfig

JSON representation  
---  
      
    
    {
      "textPrompt": string,
      "voicePrompt": string
    }  
  
Fields  
---  
`textPrompt` |  `string` Optional. Defines the prompt used for the system instructions when interacting with the agent in chat conversations. If not set, default prompt will be used.  
`voicePrompt` |  `string` Optional. Defines the prompt used for the system instructions when interacting with the agent in voice conversations. If not set, default prompt will be used.  
  
### ConnectorTool

JSON representation  
---  
      
    
    {
      "connection": string,
      "action": {
        object ([Action](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.Action))
      },
      "authConfig": {
        object ([EndUserAuthConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.EndUserAuthConfig))
      },
      "name": string,
      "description": string
    }  
  
Fields  
---  
`connection` |  `string` Required. The full resource name of the referenced Integration Connectors Connection. Format: `projects/{project}/locations/{location}/connections/{connection}`  
`action` |  `object (`[Action](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.Action)`)` Required. Action for the tool to use.  
`authConfig` |  `object (`[EndUserAuthConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.EndUserAuthConfig)`)` Optional. Configures how authentication is handled in Integration Connectors. By default, an admin authentication is passed in the Integration Connectors API requests. You can override it with a different end-user authentication config. **Note** : The Connection must have authentication override enabled in order to specify an EUC configuration here - otherwise, the ConnectorTool creation will fail. See <https://cloud.google.com/application-integration/docs/configure-connectors-task#configure-authentication-override> for details.  
`name` |  `string` Optional. The name of the tool that can be used by the Agent to decide whether to call this ConnectorTool.  
`description` |  `string` Optional. The description of the tool that can be used by the Agent to decide whether to call this ConnectorTool.  
  
### Action

JSON representation  
---  
      
    
    {
      "inputFields": [
        string
      ],
      "outputFields": [
        string
      ],
    
      // Union field action_spec can be only one of the following:
      "connectionActionId": string,
      "entityOperation": {
        object ([EntityOperation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.EntityOperation))
      }
      // End of list of possible types for union field action_spec.
    }  
  
Fields  
---  
`inputFields[]` |  `string` Optional. Entity fields to use as inputs for the operation. If no fields are specified, all fields of the Entity will be used.  
`outputFields[]` |  `string` Optional. Entity fields to return from the operation. If no fields are specified, all fields of the Entity will be returned.  
Union field `action_spec`. Specification for an action to configure for the tool to use. `action_spec` can be only one of the following:  
`connectionActionId` |  `string` ID of a Connection action for the tool to use.  
`entityOperation` |  `object (`[EntityOperation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.EntityOperation)`)` Entity operation configuration for the tool to use.  
  
### EntityOperation

JSON representation  
---  
      
    
    {
      "entityId": string,
      "operation": enum ([OperationType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.OperationType))
    }  
  
Fields  
---  
`entityId` |  `string` Required. ID of the entity.  
`operation` |  `enum (`[OperationType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.OperationType)`)` Required. Operation to perform on the entity.  
  
### EndUserAuthConfig

JSON representation  
---  
      
    
    {
    
      // Union field auth_config can be only one of the following:
      "oauth2AuthCodeConfig": {
        object ([Oauth2AuthCodeConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.Oauth2AuthCodeConfig))
      },
      "oauth2JwtBearerConfig": {
        object ([Oauth2JwtBearerConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.Oauth2JwtBearerConfig))
      }
      // End of list of possible types for union field auth_config.
    }  
  
Fields  
---  
Union field `auth_config`. The auth configuration. `auth_config` can be only one of the following:  
`oauth2AuthCodeConfig` |  `object (`[Oauth2AuthCodeConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.Oauth2AuthCodeConfig)`)` Oauth 2.0 Authorization Code authentication.  
`oauth2JwtBearerConfig` |  `object (`[Oauth2JwtBearerConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.Oauth2JwtBearerConfig)`)` JWT Profile Oauth 2.0 Authorization Grant authentication.  
  
### Oauth2AuthCodeConfig

JSON representation  
---  
      
    
    {
      "oauthToken": string
    }  
  
Fields  
---  
`oauthToken` |  `string` Required. Oauth token parameter name to pass through. Must be in the format `$context.variables.<name_of_variable>`.  
  
### Oauth2JwtBearerConfig

JSON representation  
---  
      
    
    {
      "issuer": string,
      "subject": string,
      "clientKey": string
    }  
  
Fields  
---  
`issuer` |  `string` Required. Issuer parameter name to pass through. Must be in the format `$context.variables.<name_of_variable>`.  
`subject` |  `string` Required. Subject parameter name to pass through. Must be in the format `$context.variables.<name_of_variable>`.  
`clientKey` |  `string` Required. Client parameter name to pass through. Must be in the format `$context.variables.<name_of_variable>`.  
  
### DataStoreTool

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "boostSpecs": [
        {
          object ([BoostSpecs](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.BoostSpecs))
        }
      ],
      "modalityConfigs": [
        {
          object ([ModalityConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ModalityConfig))
        }
      ],
      "filterParameterBehavior": enum ([FilterParameterBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.FilterParameterBehavior)),
    
      // Union field search_source can be only one of the following:
      "dataStoreSource": {
        object ([DataStoreSource](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.DataStoreSource))
      },
      "engineSource": {
        object ([EngineSource](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.EngineSource))
      }
      // End of list of possible types for union field search_source.
    }  
  
Fields  
---  
`name` |  `string` Required. The data store tool name.  
`description` |  `string` Optional. The tool description.  
`boostSpecs[]` |  `object (`[BoostSpecs](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.BoostSpecs)`)` Optional. Boost specification to boost certain documents.  
`modalityConfigs[]` |  `object (`[ModalityConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ModalityConfig)`)` Optional. The modality configs for the data store.  
`filterParameterBehavior` |  `enum (`[FilterParameterBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.FilterParameterBehavior)`)` Optional. The filter parameter behavior.  
Union field `search_source`. Defines the search source, either a single DataStore or an Engine. `search_source` can be only one of the following:  
`dataStoreSource` |  `object (`[DataStoreSource](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.DataStoreSource)`)` Optional. Search within a single specific DataStore.  
`engineSource` |  `object (`[EngineSource](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.EngineSource)`)` Optional. Search within an Engine (potentially across multiple DataStores).  
  
### DataStoreSource

JSON representation  
---  
      
    
    {
      "filter": string,
      "dataStore": {
        object ([DataStore](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.DataStore))
      }
    }  
  
Fields  
---  
`filter` |  `string` Optional. Filter specification for the DataStore. See: <https://cloud.google.com/generative-ai-app-builder/docs/filter-search-metadata>  
`dataStore` |  `object (`[DataStore](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.DataStore)`)` Optional. The data store.  
  
### DataStore

JSON representation  
---  
      
    
    {
      "name": string,
      "type": enum ([DataStoreType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.DataStoreType)),
      "documentProcessingMode": enum ([DocumentProcessingMode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.DocumentProcessingMode)),
      "displayName": string,
      "createTime": string,
      "connectorConfig": {
        object ([ConnectorConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ConnectorConfig))
      }
    }  
  
Fields  
---  
`name` |  `string` Required. Full resource name of the DataStore. Format: `projects/{project}/locations/{location}/collections/{collection}/dataStores/{dataStore}`  
`type` |  `enum (`[DataStoreType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.DataStoreType)`)` Output only. The type of the data store. This field is readonly and populated by the server.  
`documentProcessingMode` |  `enum (`[DocumentProcessingMode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.DocumentProcessingMode)`)` Output only. The document processing mode for the data store connection. Only set for PUBLIC_WEB and UNSTRUCTURED data stores.  
`displayName` |  `string` Output only. The display name of the data store.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the data store was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`connectorConfig` |  `object (`[ConnectorConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ConnectorConfig)`)` Output only. The connector config for the data store connection.  
  
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
  
### ConnectorConfig

JSON representation  
---  
      
    
    {
      "collection": string,
      "collectionDisplayName": string,
      "dataSource": string
    }  
  
Fields  
---  
`collection` |  `string` Resource name of the collection the data store belongs to.  
`collectionDisplayName` |  `string` Display name of the collection the data store belongs to.  
`dataSource` |  `string` The name of the data source. Example: `salesforce`, `jira`, `confluence`, `bigquery`.  
  
### EngineSource

JSON representation  
---  
      
    
    {
      "engine": string,
      "dataStoreSources": [
        {
          object ([DataStoreSource](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.DataStoreSource))
        }
      ],
      "filter": string
    }  
  
Fields  
---  
`engine` |  `string` Required. Full resource name of the Engine. Format: `projects/{project}/locations/{location}/collections/{collection}/engines/{engine}`  
`dataStoreSources[]` |  `object (`[DataStoreSource](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.DataStoreSource)`)` Optional. Use to target specific DataStores within the Engine. If empty, the search applies to all DataStores associated with the Engine.  
`filter` |  `string` Optional. A filter applied to the search across the Engine. Not relevant and not used if 'data_store_sources' is provided. See: <https://cloud.google.com/generative-ai-app-builder/docs/filter-search-metadata>  
  
### BoostSpecs

JSON representation  
---  
      
    
    {
      "dataStores": [
        string
      ],
      "spec": [
        {
          object ([BoostSpec](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.BoostSpec))
        }
      ]
    }  
  
Fields  
---  
`dataStores[]` |  `string` Required. The Data Store where the boosting configuration is applied. Full resource name of DataStore, such as projects/{project}/locations/{location}/collections/{collection}/dataStores/{dataStore}.  
`spec[]` |  `object (`[BoostSpec](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.BoostSpec)`)` Required. A list of boosting specifications.  
  
### BoostSpec

JSON representation  
---  
      
    
    {
      "conditionBoostSpecs": [
        {
          object ([ConditionBoostSpec](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ConditionBoostSpec))
        }
      ]
    }  
  
Fields  
---  
`conditionBoostSpecs[]` |  `object (`[ConditionBoostSpec](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ConditionBoostSpec)`)` Required. A list of boosting specifications.  
  
### ConditionBoostSpec

JSON representation  
---  
      
    
    {
      "condition": string,
      "boost": number,
      "boostControlSpec": {
        object ([BoostControlSpec](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.BoostControlSpec))
      }
    }  
  
Fields  
---  
`condition` |  `string` Required. An expression which specifies a boost condition. The syntax is the same as filter expression syntax. Currently, the only supported condition is a list of BCP-47 lang codes. Example: To boost suggestions in languages en or fr: (lang_code: ANY("en", "fr"))  
`boost` |  `number` Optional. Strength of the boost, which should be in [-1, 1]. Negative boost means demotion. Default is 0.0.Setting to 1.0 gives the suggestions a big promotion. However, it does not necessarily mean that the top result will be a boosted suggestion.Setting to -1.0 gives the suggestions a big demotion. However, other suggestions that are relevant might still be shown.Setting to 0.0 means no boost applied. The boosting condition is ignored.  
`boostControlSpec` |  `object (`[BoostControlSpec](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.BoostControlSpec)`)` Optional. Complex specification for custom ranking based on customer defined attribute value.  
  
### BoostControlSpec

JSON representation  
---  
      
    
    {
      "fieldName": string,
      "attributeType": enum ([AttributeType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.AttributeType)),
      "interpolationType": enum ([InterpolationType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.InterpolationType)),
      "controlPoints": [
        {
          object ([ControlPoint](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ControlPoint))
        }
      ]
    }  
  
Fields  
---  
`fieldName` |  `string` Optional. The name of the field whose value will be used to determine the boost amount.  
`attributeType` |  `enum (`[AttributeType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.AttributeType)`)` Optional. The attribute type to be used to determine the boost amount. The attribute value can be derived from the field value of the specified field_name. In the case of numerical it is straightforward i.e. attribute_value = numerical_field_value. In the case of freshness however, attribute_value = (time.now() - datetime_field_value).  
`interpolationType` |  `enum (`[InterpolationType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.InterpolationType)`)` Optional. The interpolation type to be applied to connect the control points listed below.  
`controlPoints[]` |  `object (`[ControlPoint](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ControlPoint)`)` Optional. The control points used to define the curve. The monotonic function (defined through the interpolation_type above) passes through the control points listed here.  
  
### ControlPoint

JSON representation  
---  
      
    
    {
      "attributeValue": string,
      "boostAmount": number
    }  
  
Fields  
---  
`attributeValue` |  `string` Optional. Can be one of: 1. The numerical field value. 2. The duration spec for freshness: The value must be formatted as an XSD `dayTimeDuration` value (a restricted subset of an ISO 8601 duration value). The pattern for this is: `[nD][T[nH][nM][nS]]`.  
`boostAmount` |  `number` Optional. The value between -1 to 1 by which to boost the score if the attribute_value evaluates to the value specified above.  
  
### ModalityConfig

JSON representation  
---  
      
    
    {
      "modalityType": enum ([ModalityType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ModalityType)),
      "rewriterConfig": {
        object ([RewriterConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.RewriterConfig))
      },
      "summarizationConfig": {
        object ([SummarizationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.SummarizationConfig))
      },
      "groundingConfig": {
        object ([GroundingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.GroundingConfig))
      },
      "snippetsConfig": {
        object ([SnippetsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.SnippetsConfig))
      }
    }  
  
Fields  
---  
`modalityType` |  `enum (`[ModalityType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ModalityType)`)` Required. The modality type.  
`rewriterConfig` |  `object (`[RewriterConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.RewriterConfig)`)` Optional. The rewriter config.  
`summarizationConfig` |  `object (`[SummarizationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.SummarizationConfig)`)` Optional. The summarization config.  
`groundingConfig` |  `object (`[GroundingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.GroundingConfig)`)` Optional. The grounding configuration.  
`snippetsConfig` |  `object (`[SnippetsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.SnippetsConfig)`)` Optional. The snippets configuration.  
  
### RewriterConfig

JSON representation  
---  
      
    
    {
      "modelSettings": {
        object ([ModelSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ModelSettings))
      },
      "prompt": string,
      "disabled": boolean
    }  
  
Fields  
---  
`modelSettings` |  `object (`[ModelSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ModelSettings)`)` Required. Configurations for the LLM model.  
`prompt` |  `string` Optional. The prompt definition. If not set, default prompt will be used.  
`disabled` |  `boolean` Optional. Whether the rewriter is disabled.  
  
### ModelSettings

JSON representation  
---  
      
    
    {
      "model": string,
      "thinkingLevel": enum ([ThinkingLevel](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ThinkingLevel)),
    
      // Union field _temperature can be only one of the following:
      "temperature": number
      // End of list of possible types for union field _temperature.
    }  
  
Fields  
---  
`model` |  `string` Optional. The LLM model that the agent should use. If not set, the agent will inherit the model from its parent agent.  
`thinkingLevel` |  `enum (`[ThinkingLevel](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ThinkingLevel)`)` Optional. The thinking level of the model.  
Union field `_temperature`.`_temperature` can be only one of the following:  
`temperature` |  `number` Optional. If set, this temperature will be used for the LLM model. Temperature controls the randomness of the model's responses. Lower temperatures produce responses that are more predictable. Higher temperatures produce responses that are more creative.  
  
### SummarizationConfig

JSON representation  
---  
      
    
    {
      "modelSettings": {
        object ([ModelSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ModelSettings))
      },
      "prompt": string,
      "disabled": boolean
    }  
  
Fields  
---  
`modelSettings` |  `object (`[ModelSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ModelSettings)`)` Optional. Configurations for the LLM model.  
`prompt` |  `string` Optional. The prompt definition. If not set, default prompt will be used.  
`disabled` |  `boolean` Optional. Whether summarization is disabled.  
  
### GroundingConfig

JSON representation  
---  
      
    
    {
      "groundingLevel": number,
      "disabled": boolean
    }  
  
Fields  
---  
`groundingLevel` |  `number` Optional. The groundedness threshold of the answer based on the retrieved sources. The value has a configurable range of [1, 5]. The level is used to threshold the groundedness of the answer, meaning that all responses with a groundedness score below the threshold will fall back to returning relevant snippets only.For example, a level of 3 means that the groundedness score must be 3 or higher for the response to be returned.  
`disabled` |  `boolean` Optional. Whether grounding is disabled.  
  
### SnippetsConfig

JSON representation  
---  
      
    
    {
      "enableSnippets": boolean,
      "maxSnippets": integer
    }  
  
Fields  
---  
`enableSnippets` |  `boolean` Optional. Whether snippets are enabled.  
`maxSnippets` |  `integer` Optional. Number of snippets to return per query. If unset, returns all snippets from the service by default.  
  
### PythonFunction

JSON representation  
---  
      
    
    {
      "name": string,
      "pythonCode": string,
      "description": string,
      "serviceDirectoryConfig": {
        object ([ServiceDirectoryConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ServiceDirectoryConfig))
      }
    }  
  
Fields  
---  
`name` |  `string` Optional. The name of the Python function to execute. Must match a Python function name defined in the python code. Case sensitive. If the name is not provided, the first function defined in the python code will be used.  
`pythonCode` |  `string` Optional. The Python code to execute for the tool.  
`description` |  `string` Output only. The description of the Python function, parsed from the python code's docstring.  
`serviceDirectoryConfig` |  `object (`[ServiceDirectoryConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ServiceDirectoryConfig)`)` Optional. Service Directory configuration for the tool.  
  
### McpTool

JSON representation  
---  
      
    
    {
      "name": string,
      "nameOverride": string,
      "description": string,
      "inputSchema": {
        object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema))
      },
      "outputSchema": {
        object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema))
      },
      "serverAddress": string,
      "apiAuthentication": {
        object ([ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ApiAuthentication))
      },
      "tlsConfig": {
        object ([TlsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.TlsConfig))
      },
      "serviceDirectoryConfig": {
        object ([ServiceDirectoryConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ServiceDirectoryConfig))
      },
      "customHeaders": {
        string: string,
        ...
      },
      "state": enum ([State](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.State))
    }  
  
Fields  
---  
`name` |  `string` Required. The name of the MCP tool.  
`nameOverride` |  `string` Optional. The name override of the MCP tool. This is populated if the name was overridden by a Toolset override.  
`description` |  `string` Optional. The description of the MCP tool.  
`inputSchema` |  `object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema)`)` Optional. The schema of the input arguments of the MCP tool.  
`outputSchema` |  `object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema)`)` Optional. The schema of the output arguments of the MCP tool.  
`serverAddress` |  `string` Required. The server address of the MCP server, e.g., "https://example.com/mcp/". If the server is built with the MCP SDK, the url should be suffixed with "/mcp/". Only Streamable HTTP transport based servers are supported. This is the same as the server_address in the McpToolset. See <https://modelcontextprotocol.io/specification/2025-03-26/basic/transports#streamable-http> for more details.  
`apiAuthentication` |  `object (`[ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ApiAuthentication)`)` Optional. Authentication information required to execute the tool against the MCP server. For bearer token authentication, the token applies only to tool execution, not to listing tools. This requires that tools can be listed without authentication.  
`tlsConfig` |  `object (`[TlsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.TlsConfig)`)` Optional. The TLS configuration. Includes the custom server certificates that the client should trust.  
`serviceDirectoryConfig` |  `object (`[ServiceDirectoryConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ServiceDirectoryConfig)`)` Optional. Service Directory configuration for VPC-SC, used to resolve service names within a perimeter.  
`customHeaders` |  `map (key: string, value: string)` Optional. The custom headers to send in the request to the MCP server. The values must be in the format `$context.variables.<name_of_variable>` and can be set in the session variables. See <https://docs.cloud.google.com/customer-engagement-ai/conversational-agents/ps/tool/open-api#openapi-injection> for more details.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.State)`)` Output only. The dynamic availability state of the tool on the external server.  
  
### CustomHeadersEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `string`  
  
### FileSearchTool

JSON representation  
---  
      
    
    {
      "corpusType": enum ([CorpusType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.CorpusType)),
      "name": string,
      "description": string,
      "fileCorpus": string
    }  
  
Fields  
---  
`corpusType` |  `enum (`[CorpusType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.CorpusType)`)` Optional. The type of the corpus. Default is FULLY_MANAGED.  
`name` |  `string` Required. The tool name.  
`description` |  `string` Optional. The tool description.  
`fileCorpus` |  `string` Optional. The corpus where files are stored. Format: projects/{project}/locations/{location}/ragCorpora/{rag_corpus}  
  
### SystemTool

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string
    }  
  
Fields  
---  
`name` |  `string` Required. The name of the system tool.  
`description` |  `string` Output only. The description of the system tool.  
  
### AgentTool

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "agent": string
    }  
  
Fields  
---  
`name` |  `string` Required. The name of the agent tool.  
`description` |  `string` Optional. Description of the tool's purpose.  
`agent` |  `string` Optional. The resource name of the agent that is the entry point of the tool. Format: `projects/{project}/locations/{location}/agents/{agent}`  
  
### WidgetTool

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "widgetType": enum ([WidgetType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.WidgetType)),
      "uiConfig": {
        object
      },
      "dataMapping": {
        object ([DataMapping](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.DataMapping))
      },
      "textResponseConfig": {
        object ([TextResponseConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.TextResponseConfig))
      },
    
      // Union field input can be only one of the following:
      "parameters": {
        object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema))
      }
      // End of list of possible types for union field input.
    }  
  
Fields  
---  
`name` |  `string` Required. The display name of the widget tool.  
`description` |  `string` Optional. The description of the widget tool.  
`widgetType` |  `enum (`[WidgetType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.WidgetType)`)` Optional. The type of the widget tool. If not specified, the default type will be CUSTOMIZED.  
`uiConfig` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. Configuration for rendering the widget.  
`dataMapping` |  `object (`[DataMapping](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.DataMapping)`)` Optional. The mapping that defines how data from a source tool is mapped to the widget's input parameters.  
`textResponseConfig` |  `object (`[TextResponseConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.TextResponseConfig)`)` Optional. Configuration for always-included text responses.  
Union field `input`. The input of the widget tool. `input` can be only one of the following:  
`parameters` |  `object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema)`)` Optional. The input parameters of the widget tool.  
  
### DataMapping

JSON representation  
---  
      
    
    {
      "sourceToolName": string,
      "fieldMappings": {
        string: string,
        ...
      },
      "pythonFunction": {
        object ([PythonFunction](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.PythonFunction))
      },
      "mode": enum ([Mode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.Mode)),
      "pythonScript": string
    }  
  
Fields  
---  
`sourceToolName` |  `string` Optional. The resource name of the tool that provides the data for the widget (e.g., a search tool or a custom function). Format: `projects/{project}/locations/{location}/agents/{agent}/tools/{tool}`  
`fieldMappings` |  `map (key: string, value: string)` Optional. A map of widget input parameter fields to the corresponding output fields of the source tool.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`pythonFunction` |  `object (`[PythonFunction](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.PythonFunction)`)` Optional. Configuration for a Python function used to transform the source tool's output into the widget's input format.  
`mode` |  `enum (`[Mode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.Mode)`)` Optional. The mode of the data mapping.  
`pythonScript  
**(deprecated)**` |  `string` This item is deprecated!Deprecated: Use `python_function` instead.  
  
### FieldMappingsEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `string`  
  
### TextResponseConfig

JSON representation  
---  
      
    
    {
      "type": enum ([Type](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.Type_1)),
      "staticText": string,
      "textResponseInstruction": string
    }  
  
Fields  
---  
`type` |  `enum (`[Type](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.Type_1)`)` Optional. The strategy for providing the text response.  
`staticText` |  `string` Optional. The static text response to return when type is STATIC.  
`textResponseInstruction` |  `string` Optional. Instruction for the LLM on how to generate the text response. Used as the description for the text response parameter if type is LLM_GENERATED.  
  
### RemoteAgentTool

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "agentCard": {
        object ([AgentCard](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.AgentCard))
      },
      "apiAuthentication": {
        object ([ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ApiAuthentication))
      },
      "statefulAgent": boolean,
      "inputVariableMapping": {
        string: string,
        ...
      },
      "outputVariableMapping": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`name` |  `string` Required. The name of the tool.  
`description` |  `string` Required. The description of the tool.  
`agentCard` |  `object (`[AgentCard](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.AgentCard)`)` Required. The agent card of the remote agent that this tool invokes.  
`apiAuthentication` |  `object (`[ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ApiAuthentication)`)` Optional. Authentication configuration for calling the remote agent.  
`statefulAgent` |  `boolean` Optional. When enabled, the interaction between the CXAS app and the remote agent will share the same context. If the remote agent returns a context_id, it will be persisted for the entirety of the session for this remote agent tool.  
`inputVariableMapping` |  `map (key: string, value: string)` Optional. Mapping of input variable names of remote agent to GECX variable names.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`outputVariableMapping` |  `map (key: string, value: string)` Optional. Mapping of output variable names of remote agent to GECX variable names.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
### AgentCard

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "supportedInterfaces": [
        {
          object ([AgentInterface](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.AgentInterface))
        }
      ],
      "version": string,
      "skills": [
        {
          object ([AgentSkill](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.AgentSkill))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` Required. A human-readable name for the agent.  
`description` |  `string` Required. A description of the agent's domain of action/solution space.  
`supportedInterfaces[]` |  `object (`[AgentInterface](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.AgentInterface)`)` Required. Ordered list of supported interfaces. The first entry is preferred.  
`version` |  `string` Required. The version of the agent.  
`skills[]` |  `object (`[AgentSkill](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.AgentSkill)`)` Required. Skills represent a unit of ability an agent can perform. This may somewhat abstract but represents a more focused set of actions that the agent is highly likely to succeed at.  
  
### AgentInterface

JSON representation  
---  
      
    
    {
      "url": string,
      "protocolBinding": string,
      "tenant": string,
      "protocolVersion": string
    }  
  
Fields  
---  
`url` |  `string` Required. The URL where this interface is available. Must be a valid absolute HTTPS URL in production. Example: "https://api.example.com/a2a/v1", "https://grpc.example.com/a2a"  
`protocolBinding` |  `string` Required. The protocol binding supported at this URL. This is an open form string, to be easily extended for other protocol bindings. The core ones officially supported are `JSONRPC`, `GRPC` and `HTTP+JSON`.  
`tenant` |  `string` Tenant ID to be used in the request when calling the agent.  
`protocolVersion` |  `string` Required. The version of the A2A protocol this interface exposes. Use the latest supported minor version per major version. Examples: "0.3", "1.0"  
  
### AgentSkill

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
      ],
      "inputModes": [
        string
      ],
      "outputModes": [
        string
      ]
    }  
  
Fields  
---  
`id` |  `string` Required. A unique identifier for the agent's skill.  
`name` |  `string` Required. A human-readable name for the skill.  
`description` |  `string` Required. A detailed description of the skill.  
`tags[]` |  `string` Required. A set of keywords describing the skill's capabilities.  
`examples[]` |  `string` Example prompts or scenarios that this skill can handle.  
`inputModes[]` |  `string` The set of supported input media types for this skill, overriding the agent's defaults.  
`outputModes[]` |  `string` The set of supported output media types for this skill, overriding the agent's defaults.  
  
### InputVariableMappingEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `string`  
  
### OutputVariableMappingEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `string`  
  
### Duration

JSON representation  
---  
      
    
    {
      "seconds": string,
      "nanos": integer
    }  
  
Fields  
---  
`seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Signed seconds of the span of time. Must be from -315,576,000,000 to +315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`nanos` |  `integer` Signed fractions of a second at nanosecond resolution of the span of time. Durations less than one second are represented with a 0 `seconds` field and a positive or negative `nanos` field. For durations of one second or more, a non-zero value for the `nanos` field must be of the same sign as the `seconds` field. Must be from -999,999,999 to +999,999,999 inclusive.  
  
### ToolFakeConfig

JSON representation  
---  
      
    
    {
      "enableFakeMode": boolean,
    
      // Union field tool_response can be only one of the following:
      "codeBlock": {
        object ([CodeBlock](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.CodeBlock))
      }
      // End of list of possible types for union field tool_response.
    }  
  
Fields  
---  
`enableFakeMode` |  `boolean` Optional. Whether the tool is using fake mode.  
Union field `tool_response`. The response is either static or it is provided by a python function. `tool_response` can be only one of the following:  
`codeBlock` |  `object (`[CodeBlock](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.CodeBlock)`)` Optional. Code block which will be executed instead of a real tool call.  
  
### CodeBlock

JSON representation  
---  
      
    
    {
      "pythonCode": string
    }  
  
Fields  
---  
`pythonCode` |  `string` Required. Python code which will be invoked in tool fake mode. Expected Python function signature - To catch all tool calls: def fake_tool_call(tool: Tool, input: dict[str, Any], callback_context: CallbackContext) -> Optional[dict[str, Any]]: To catch a specific tool call: def fake_{tool_id}(tool: Tool, input: dict[str, Any], callback_context: CallbackContext) -> Optional[dict[str, Any]]: If the function returns None, the real tool will be invoked instead.  
  
### Type

OpenAPI data types.

Enums  
---  
`TYPE_UNSPECIFIED` | Type unspecified.  
`STRING` | String type.  
`INTEGER` | Integer type.  
`NUMBER` | Number type.  
`BOOLEAN` | Boolean type.  
`OBJECT` | Object type.  
`ARRAY` | Array type.  
  
### NullValue

Represents a JSON `null`.

`NullValue` is a sentinel, using an enum with only one value to represent the null value for the `Value` type union.

A field of type `NullValue` with any value other than `0` is considered invalid. Most ProtoJSON serializers will emit a `Value` with a `null_value` set as a JSON `null` regardless of the integer value, and so will round trip to a `0` value.

Enums  
---  
`NULL_VALUE` | Null value.  
  
### RequestLocation

The location of the API key in the request.

Enums  
---  
`REQUEST_LOCATION_UNSPECIFIED` | Unspecified. This value should not be used.  
`HEADER` | Represents the key in http header.  
`QUERY_STRING` | Represents the key in query string.  
  
### OauthGrantType

OAuth grant types. Only [client credential grant](https://oauth.net/2/grant-types/client-credentials) is supported.

Enums  
---  
`OAUTH_GRANT_TYPE_UNSPECIFIED` | Unspecified. Defaults to CLIENT_CREDENTIAL.  
`CLIENT_CREDENTIAL` | Represents the [client credential flow](https://oauth.net/2/grant-types/client-credentials).  
  
### OperationType

The operation to perform on the entity.

Enums  
---  
`OPERATION_TYPE_UNSPECIFIED` | Operation type unspecified. Invalid, ConnectorTool create/update will fail.  
`LIST` | List operation.  
`GET` | Get operation.  
`CREATE` | Create operation.  
`UPDATE` | Update operation.  
`DELETE` | Delete operation.  
  
### DataStoreType

The type of the data store.

Enums  
---  
`DATA_STORE_TYPE_UNSPECIFIED` | Not specified. This value indicates that the data store type is not specified, so it will not be used during search.  
`PUBLIC_WEB` | A data store that contains public web content.  
`UNSTRUCTURED` | A data store that contains unstructured private data.  
`FAQ` | A data store that contains structured data used as FAQ.  
`CONNECTOR` | A data store that is a connector to a first-party or a third-party service.  
  
### DocumentProcessingMode

The document processing mode of the data store.

Enums  
---  
`DOCUMENT_PROCESSING_MODE_UNSPECIFIED` | Not specified.  
`DOCUMENTS` | Documents are processed as documents.  
`CHUNKS` | Documents are converted to chunks.  
  
### AttributeType

The attribute(or function) for which the custom ranking is to be applied.

Enums  
---  
`ATTRIBUTE_TYPE_UNSPECIFIED` | Unspecified AttributeType.  
`NUMERICAL` | The value of the numerical field will be used to dynamically update the boost amount. In this case, the attribute_value (the x value) of the control point will be the actual value of the numerical field for which the boost_amount is specified.  
`FRESHNESS` | For the freshness use case the attribute value will be the duration between the current time and the date in the datetime field specified. The value must be formatted as an XSD `dayTimeDuration` value (a restricted subset of an ISO 8601 duration value). The pattern for this is: `[nD][T[nH][nM][nS]]`. E.g. `5D`, `3DT12H30M`, `T24H`.  
  
### InterpolationType

The interpolation type to be applied. Default will be linear (Piecewise Linear).

Enums  
---  
`INTERPOLATION_TYPE_UNSPECIFIED` | Interpolation type is unspecified. In this case, it defaults to Linear.  
`LINEAR` | Piecewise linear interpolation will be applied.  
  
### ModalityType

The modality type.

Enums  
---  
`MODALITY_TYPE_UNSPECIFIED` | Unspecified modality type.  
`TEXT` | Text modality.  
`AUDIO` | Audio modality.  
  
### ThinkingLevel

Thinking level configuration for the model.

Enums  
---  
`THINKING_LEVEL_UNSPECIFIED` | Thinking level is unspecified.  
`DEFAULT` | Default thinking level.  
`LOW` | Low thinking level.  
`MEDIUM` | Medium thinking level.  
`HIGH` | High thinking level.  
  
### FilterParameterBehavior

Filter parameter behavior.

Enums  
---  
`FILTER_PARAMETER_BEHAVIOR_UNSPECIFIED` | Default filter behavior. Include filter parameter for connector datastores. For the rest of the datastore types, the filter input parameter is omitted.  
`ALWAYS_INCLUDE` | Always include filter parameter for all datastore types.  
`NEVER_INCLUDE` | The filter parameter is never included in the list of tool parameters, regardless of the datastore type.  
  
### State

Represents the dynamic availability state of the tool.

Enums  
---  
`STATE_UNSPECIFIED` | Default state.  
`ACTIVE` | The tool is available and actively offered by the server.  
`INACTIVE` | The tool is configured or pinned, but currently not offered by the server.  
`STALE` | The tool exists on the server, but does not match the version on the server.  
  
### CorpusType

The type of the Vertex RAG corpus.

Enums  
---  
`CORPUS_TYPE_UNSPECIFIED` | Unspecified corpus type.  
`USER_OWNED` | The corpus is created and owned by the user.  
`FULLY_MANAGED` | The corpus is created by the agent.  
  
### WidgetType

All available widget types. New values may be added to this enum in the future.

Enums  
---  
`WIDGET_TYPE_UNSPECIFIED` | Unspecified widget type.  
`CUSTOM` | Custom widget type.  
`PRODUCT_CAROUSEL` | Product carousel widget.  
`PRODUCT_DETAILS` | Product details widget.  
`QUICK_ACTIONS` | Quick actions widget.  
`PRODUCT_COMPARISON` | Product comparison widget.  
`ADVANCED_PRODUCT_DETAILS` | Advanced product details widget.  
`SHORT_FORM` | Short form widget.  
`OVERALL_SATISFACTION` | Overall satisfaction widget.  
`ORDER_SUMMARY` | Order summary widget.  
`APPOINTMENT_DETAILS` | Appointment details widget.  
`APPOINTMENT_SCHEDULER` | Appointment scheduler widget.  
`CONTACT_FORM` | Contact form widget.  
  
### Mode

The strategy used to map data from the source tool to the widget.

Enums  
---  
`MODE_UNSPECIFIED` | Unspecified mode.  
`FIELD_MAPPING` | Use the `field_mappings` map for data transformation.  
`PYTHON_SCRIPT` | Use the `python_script` for data transformation.  
  
### Type

Defines how the text response is produced.

Enums  
---  
`TYPE_UNSPECIFIED` | Unspecified type.  
`NONE` | The LLM dynamically decides whether to generate a text response alongside the widget based on the conversation context.  
`LLM_GENERATED` | The LLM is explicitly required to generate a text response.  
`STATIC` | A pre-defined static text response is always used.  
  
### ExecutionType

The execution type of the tool or toolset.

Enums  
---  
`EXECUTION_TYPE_UNSPECIFIED` | The execution type is unspecified. Defaults to `SYNCHRONOUS` if unspecified.  
`SYNCHRONOUS` | The tool is executed synchronously. The session is blocked until the tool returns.  
`ASYNCHRONOUS` | The tool is executed asynchronously. The session will continue while the tool is executing.  
  
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

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
