---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.toolsets
title: REST Resource: projects.locations.apps.toolsets \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T13:11:18.177354+00:00
---

# REST Resource: projects.locations.apps.toolsets  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.toolsets

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  REST Resource: projects.locations.apps.toolsets Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Toolset
    * JSON representation
    * McpToolset
      * JSON representation
    * McpToolOverride
      * JSON representation
    * McpToolDefinition
      * JSON representation
    * OpenApiToolset
      * JSON representation
    * ConnectorToolset
      * JSON representation
  * Methods



## Resource: Toolset

A toolset represents a group of dynamically managed tools that can be used by the agent.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "timeout": string,
      "createTime": string,
      "updateTime": string,
      "etag": string,
      "executionType": enum ([ExecutionType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ExecutionType)),
      "toolFakeConfig": {
        object ([ToolFakeConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ToolFakeConfig))
      },
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "mcpToolset": {
        object ([McpToolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.toolsets#Toolset.McpToolset))
      },
      "openApiToolset": {
        object ([OpenApiToolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.toolsets#Toolset.OpenApiToolset))
      },
      "connectorToolset": {
        object ([ConnectorToolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.toolsets#Toolset.ConnectorToolset))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`name` |  `string` Identifier. The unique identifier of the toolset. Format: `projects/{project}/locations/{location}/apps/{app}/toolsets/{toolset}`  
`displayName` |  `string` Optional. The display name of the toolset. Must be unique within the same app.  
`description` |  `string` Optional. The description of the toolset.  
`timeout` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. The timeout for the toolset execution. If not set, the default timeout is 30 seconds for `SYNCHRONOUS` toolsets and 60 seconds for `ASYNCHRONOUS` toolsets.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the toolset was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the toolset was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`etag` |  `string` ETag used to ensure the object hasn't changed during a read-modify-write operation. If the etag is empty, the update will overwrite any concurrent changes.  
`executionType` |  `enum (`[ExecutionType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ExecutionType)`)` Optional. The execution type of the tools in the toolset.  
`toolFakeConfig` |  `object (`[ToolFakeConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ToolFakeConfig)`)` Optional. Configuration for tools behavior in fake mode.  
The type of the toolset. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`mcpToolset` |  `object (`[McpToolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.toolsets#Toolset.McpToolset)`)` Optional. A toolset that contains a list of tools that are offered by the MCP server.  
`openApiToolset` |  `object (`[OpenApiToolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.toolsets#Toolset.OpenApiToolset)`)` Optional. A toolset that contains a list of tools that are defined by an OpenAPI schema.  
`connectorToolset` |  `object (`[ConnectorToolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.toolsets#Toolset.ConnectorToolset)`)` Optional. A toolset that generates tools from an Integration Connectors Connection.  
End of mutually exclusive fields.  
  
### McpToolset

A toolset that contains a list of tools that are offered by the MCP server.

JSON representation  
---  
      
    
    {
      "serverAddress": string,
      "apiAuthentication": {
        object ([ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ApiAuthentication))
      },
      "serviceDirectoryConfig": {
        object ([ServiceDirectoryConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ServiceDirectoryConfig))
      },
      "tlsConfig": {
        object ([TlsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/TlsConfig))
      },
      "customHeaders": {
        string: string,
        ...
      },
      "toolOverrides": [
        {
          object ([McpToolOverride](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.toolsets#Toolset.McpToolOverride))
        }
      ]
    }  
  
Fields  
---  
`serverAddress` |  `string` Required. The address of the MCP server, for example, "https://example.com/mcp/". If the server is built with the MCP SDK, the url should be suffixed with "/mcp/". Only Streamable HTTP transport based servers are supported. See <https://modelcontextprotocol.io/specification/2025-03-26/basic/transports#streamable-http> for more details.  
`apiAuthentication` |  `object (`[ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ApiAuthentication)`)` Optional. Authentication information required to access tools and execute a tool against the MCP server. For bearer token authentication, the token applies only to tool execution, not to listing tools. This requires that tools can be listed without authentication.  
`serviceDirectoryConfig` |  `object (`[ServiceDirectoryConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ServiceDirectoryConfig)`)` Optional. Service Directory configuration for VPC-SC, used to resolve service names within a perimeter.  
`tlsConfig` |  `object (`[TlsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/TlsConfig)`)` Optional. The TLS configuration. Includes the custom server certificates that the client should trust.  
`customHeaders` |  `map (key: string, value: string)` Optional. The custom headers to send in the request to the MCP server. The values must be in the format `$context.variables.<name_of_variable>` and can be set in the session variables. See <https://docs.cloud.google.com/customer-engagement-ai/conversational-agents/ps/tool/open-api#openapi-injection> for more details.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`toolOverrides[]` |  `object (`[McpToolOverride](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.toolsets#Toolset.McpToolOverride)`)` Optional. Overrides for individual tools within this toolset. This allows overriding specific details like descriptions, names, or pinning the tools' states so they aren't fully dynamic.  
  
### McpToolOverride

Overrides associated with a given tool in a Toolset. This enables "pinning" or "overriding" of tool definitions from the external dynamic server.

JSON representation  
---  
      
    
    {
      "tool": string,
      "nameOverride": string,
      "descriptionOverride": string,
      "snapshot": {
        object ([McpToolDefinition](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.toolsets#Toolset.McpToolDefinition))
      }
    }  
  
Fields  
---  
`tool` |  `string` Required. The original name of the tool as it is emitted by the MCP server.  
`nameOverride` |  `string` Optional. If present, this tool uses this name in the Agent instead of the original name. This is primarily used as an alias if the MCP server offers poorly named tools.  
`descriptionOverride` |  `string` Optional. If present, this tool uses this description instead of the original description from the server.  
`snapshot` |  `object (`[McpToolDefinition](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.toolsets#Toolset.McpToolDefinition)`)` Output only. If present, this tool is "Pinned" and uses the snapshot values as fallbacks if the server becomes temporarily unavailable or if no Override is present.  
  
### McpToolDefinition

Container for a tool's core definition elements that are snapshot. Schemas in the snapshot are used as-is and cannot be overridden.

JSON representation  
---  
      
    
    {
      "description": string,
      "inputSchema": {
        object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Schema))
      },
      "outputSchema": {
        object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Schema))
      }
    }  
  
Fields  
---  
`description` |  `string` Output only. The description of the MCP tool. This can be overridden by `descriptionOverride` in `McpToolOverride`.  
`inputSchema` |  `object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Schema)`)` Output only. The schema of the input arguments of the MCP tool.  
`outputSchema` |  `object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Schema)`)` Output only. The schema of the output arguments of the MCP tool.  
  
### OpenApiToolset

A toolset that contains a list of tools that are defined by an OpenAPI schema.

JSON representation  
---  
      
    
    {
      "openApiSchema": string,
      "apiAuthentication": {
        object ([ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ApiAuthentication))
      },
      "tlsConfig": {
        object ([TlsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/TlsConfig))
      },
      "serviceDirectoryConfig": {
        object ([ServiceDirectoryConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ServiceDirectoryConfig))
      },
      "ignoreUnknownFields": boolean,
      "url": string
    }  
  
Fields  
---  
`openApiSchema` |  `string` Required. The OpenAPI schema of the toolset.  
`apiAuthentication` |  `object (`[ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ApiAuthentication)`)` Optional. Authentication information required by the API.  
`tlsConfig` |  `object (`[TlsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/TlsConfig)`)` Optional. The TLS configuration. Includes the custom server certificates  
`serviceDirectoryConfig` |  `object (`[ServiceDirectoryConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ServiceDirectoryConfig)`)` Optional. Service Directory configuration.  
`ignoreUnknownFields` |  `boolean` Optional. If true, the agent will ignore unknown fields in the API response for all operations defined in the OpenAPI schema.  
`url` |  `string` Optional. The server URL of the Open API schema. This field is only set in toolsets in the environment dependencies during the export process if the schema contains a server url. During the import process, if this url is present in the environment dependencies and the schema has the $env_var placeholder, it will replace the placeholder in the schema.  
  
### ConnectorToolset

A toolset that generates tools from an Integration Connectors Connection.

JSON representation  
---  
      
    
    {
      "connection": string,
      "authConfig": {
        object ([EndUserAuthConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EndUserAuthConfig))
      },
      "connectorActions": [
        {
          object ([Action](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Action))
        }
      ]
    }  
  
Fields  
---  
`connection` |  `string` Required. The full resource name of the referenced Integration Connectors Connection. Format: `projects/{project}/locations/{location}/connections/{connection}`  
`authConfig` |  `object (`[EndUserAuthConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EndUserAuthConfig)`)` Optional. Configures how authentication is handled in Integration Connectors. By default, an admin authentication is passed in the Integration Connectors API requests. You can override it with a different end-user authentication config. **Note** : The Connection must have authentication override enabled in order to specify an EUC configuration here - otherwise, the Toolset creation will fail. See: <https://cloud.google.com/application-integration/docs/configure-connectors-task#configure-authentication-override>  
`connectorActions[]` |  `object (`[Action](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Action)`)` Required. The list of connector actions/entity operations to generate tools for.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.toolsets/create)`

|  Creates a new toolset in the given app.  
  
### `[delete](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.toolsets/delete)`

|  Deletes the specified toolset.  
  
### `[get](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.toolsets/get)`

|  Gets details of the specified toolset.  
  
### `[list](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.toolsets/list)`

|  Lists toolsets in the given app.  
  
### `[patch](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.toolsets/patch)`

|  Updates the specified toolset.  
  
### `[retrieveTools](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.toolsets/retrieveTools)`

|  Retrieve the list of tools included in the specified toolset.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
