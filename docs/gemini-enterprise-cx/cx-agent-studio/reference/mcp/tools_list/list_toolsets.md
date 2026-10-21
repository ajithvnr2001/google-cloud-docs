---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_toolsets/
title: MCP Tools Reference: ces.googleapis.com \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T13:01:51.788097+00:00
---

# MCP Tools Reference: ces.googleapis.com  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_toolsets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  MCP Tools Reference: ces.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `list_toolsets`

Lists toolsets in the given app.

The following code sample shows how to use `curl` to call the `list_toolsets` MCP tool. 

Curl Request  
---  
      
    
    curl --location 'https://ces.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "list_toolsets",
        "arguments": {
          // Provide these details according to the MCP tool specification.
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'  
  
## Input Schema

Request message for `AgentService.ListToolsets`.

### ListToolsetsRequest

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
`parent` |  `string` Required. The resource name of the app to list toolsets from.  
`pageSize` |  `integer` Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.  
`pageToken` |  `string` Optional. The `next_page_token` value returned from a previous list `AgentService.ListToolsets` call.  
`filter` |  `string` Optional. Filter to be applied when listing the toolsets. See <https://google.aip.dev/160> for more details.  
`orderBy` |  `string` Optional. Field to sort by. Only "name" and "create_time" is supported. See <https://google.aip.dev/132#ordering> for more details.  
  
## Output Schema

Response message for `AgentService.ListToolsets`.

### ListToolsetsResponse

JSON representation  
---  
      
    
    {
      "toolsets": [
        {
          object ([Toolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_toolsets#Output.Schema.Toolset))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`toolsets[]` |  `object (`[Toolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_toolsets#Output.Schema.Toolset)`)` The list of toolsets.  
`nextPageToken` |  `string` A token that can be sent as `ListToolsetsRequest.page_token` to retrieve the next page. Absence of this field indicates there are no subsequent pages.  
  
### Toolset

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
      "executionType": enum ([ExecutionType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ExecutionType)),
      "toolFakeConfig": {
        object ([ToolFakeConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ToolFakeConfig))
      },
    
      // Union field toolset_type can be only one of the following:
      "mcpToolset": {
        object ([McpToolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_toolsets#Output.Schema.McpToolset))
      },
      "openApiToolset": {
        object ([OpenApiToolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_toolsets#Output.Schema.OpenApiToolset))
      },
      "connectorToolset": {
        object ([ConnectorToolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_toolsets#Output.Schema.ConnectorToolset))
      }
      // End of list of possible types for union field toolset_type.
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
`executionType` |  `enum (`[ExecutionType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ExecutionType)`)` Optional. The execution type of the tools in the toolset.  
`toolFakeConfig` |  `object (`[ToolFakeConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ToolFakeConfig)`)` Optional. Configuration for tools behavior in fake mode.  
Union field `toolset_type`. The type of the toolset. `toolset_type` can be only one of the following:  
`mcpToolset` |  `object (`[McpToolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_toolsets#Output.Schema.McpToolset)`)` Optional. A toolset that contains a list of tools that are offered by the MCP server.  
`openApiToolset` |  `object (`[OpenApiToolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_toolsets#Output.Schema.OpenApiToolset)`)` Optional. A toolset that contains a list of tools that are defined by an OpenAPI schema.  
`connectorToolset` |  `object (`[ConnectorToolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_toolsets#Output.Schema.ConnectorToolset)`)` Optional. A toolset that generates tools from an Integration Connectors Connection.  
  
### McpToolset

JSON representation  
---  
      
    
    {
      "serverAddress": string,
      "apiAuthentication": {
        object ([ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ApiAuthentication))
      },
      "serviceDirectoryConfig": {
        object ([ServiceDirectoryConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ServiceDirectoryConfig))
      },
      "tlsConfig": {
        object ([TlsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.TlsConfig))
      },
      "customHeaders": {
        string: string,
        ...
      },
      "toolOverrides": [
        {
          object ([McpToolOverride](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_toolsets#Output.Schema.McpToolOverride))
        }
      ]
    }  
  
Fields  
---  
`serverAddress` |  `string` Required. The address of the MCP server, for example, "https://example.com/mcp/". If the server is built with the MCP SDK, the url should be suffixed with "/mcp/". Only Streamable HTTP transport based servers are supported. See <https://modelcontextprotocol.io/specification/2025-03-26/basic/transports#streamable-http> for more details.  
`apiAuthentication` |  `object (`[ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ApiAuthentication)`)` Optional. Authentication information required to access tools and execute a tool against the MCP server. For bearer token authentication, the token applies only to tool execution, not to listing tools. This requires that tools can be listed without authentication.  
`serviceDirectoryConfig` |  `object (`[ServiceDirectoryConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ServiceDirectoryConfig)`)` Optional. Service Directory configuration for VPC-SC, used to resolve service names within a perimeter.  
`tlsConfig` |  `object (`[TlsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.TlsConfig)`)` Optional. The TLS configuration. Includes the custom server certificates that the client should trust.  
`customHeaders` |  `map (key: string, value: string)` Optional. The custom headers to send in the request to the MCP server. The values must be in the format `$context.variables.<name_of_variable>` and can be set in the session variables. See <https://docs.cloud.google.com/customer-engagement-ai/conversational-agents/ps/tool/open-api#openapi-injection> for more details.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`toolOverrides[]` |  `object (`[McpToolOverride](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_toolsets#Output.Schema.McpToolOverride)`)` Optional. Overrides for individual tools within this toolset. This allows overriding specific details like descriptions, names, or pinning the tools' states so they aren't fully dynamic.  
  
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
  
### ServiceDirectoryConfig

JSON representation  
---  
      
    
    {
      "service": string
    }  
  
Fields  
---  
`service` |  `string` Required. The name of [Service Directory](https://cloud.google.com/service-directory) service. Format: `projects/{project}/locations/{location}/namespaces/{namespace}/services/{service}`. Location of the service directory must be the same as the location of the app.  
  
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
  
### McpToolOverride

JSON representation  
---  
      
    
    {
      "tool": string,
      "nameOverride": string,
      "descriptionOverride": string,
      "snapshot": {
        object ([McpToolDefinition](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_toolsets#Output.Schema.McpToolDefinition))
      }
    }  
  
Fields  
---  
`tool` |  `string` Required. The original name of the tool as it is emitted by the MCP server.  
`nameOverride` |  `string` Optional. If present, this tool uses this name in the Agent instead of the original name. This is primarily used as an alias if the MCP server offers poorly named tools.  
`descriptionOverride` |  `string` Optional. If present, this tool uses this description instead of the original description from the server.  
`snapshot` |  `object (`[McpToolDefinition](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_toolsets#Output.Schema.McpToolDefinition)`)` Output only. If present, this tool is "Pinned" and uses the snapshot values as fallbacks if the server becomes temporarily unavailable or if no Override is present.  
  
### McpToolDefinition

JSON representation  
---  
      
    
    {
      "description": string,
      "inputSchema": {
        object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema))
      },
      "outputSchema": {
        object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema))
      }
    }  
  
Fields  
---  
`description` |  `string` Output only. The description of the MCP tool. This can be overridden by `description_override` in `McpToolOverride`.  
`inputSchema` |  `object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema)`)` Output only. The schema of the input arguments of the MCP tool.  
`outputSchema` |  `object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema)`)` Output only. The schema of the output arguments of the MCP tool.  
  
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
  
### OpenApiToolset

JSON representation  
---  
      
    
    {
      "openApiSchema": string,
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
`openApiSchema` |  `string` Required. The OpenAPI schema of the toolset.  
`apiAuthentication` |  `object (`[ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ApiAuthentication)`)` Optional. Authentication information required by the API.  
`tlsConfig` |  `object (`[TlsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.TlsConfig)`)` Optional. The TLS configuration. Includes the custom server certificates  
`serviceDirectoryConfig` |  `object (`[ServiceDirectoryConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ServiceDirectoryConfig)`)` Optional. Service Directory configuration.  
`ignoreUnknownFields` |  `boolean` Optional. If true, the agent will ignore unknown fields in the API response for all operations defined in the OpenAPI schema.  
`url` |  `string` Optional. The server URL of the Open API schema. This field is only set in toolsets in the environment dependencies during the export process if the schema contains a server url. During the import process, if this url is present in the environment dependencies and the schema has the $env_var placeholder, it will replace the placeholder in the schema.  
  
### ConnectorToolset

JSON representation  
---  
      
    
    {
      "connection": string,
      "authConfig": {
        object ([EndUserAuthConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.EndUserAuthConfig))
      },
      "connectorActions": [
        {
          object ([Action](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.Action))
        }
      ]
    }  
  
Fields  
---  
`connection` |  `string` Required. The full resource name of the referenced Integration Connectors Connection. Format: `projects/{project}/locations/{location}/connections/{connection}`  
`authConfig` |  `object (`[EndUserAuthConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.EndUserAuthConfig)`)` Optional. Configures how authentication is handled in Integration Connectors. By default, an admin authentication is passed in the Integration Connectors API requests. You can override it with a different end-user authentication config. **Note** : The Connection must have authentication override enabled in order to specify an EUC configuration here - otherwise, the Toolset creation will fail. See: <https://cloud.google.com/application-integration/docs/configure-connectors-task#configure-authentication-override>  
`connectorActions[]` |  `object (`[Action](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.Action)`)` Required. The list of connector actions/entity operations to generate tools for.  
  
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



Destructive Hint: ❌ | Idempotent Hint: ✅ | Read Only Hint: ✅ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
