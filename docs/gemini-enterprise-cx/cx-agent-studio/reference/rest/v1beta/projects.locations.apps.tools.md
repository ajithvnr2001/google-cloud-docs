---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools
title: REST Resource: projects.locations.apps.tools \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:33:09.525638+00:00
---

# REST Resource: projects.locations.apps.tools  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  REST Resource: projects.locations.apps.tools Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Tool
    * JSON representation
    * ClientFunction
      * JSON representation
    * OpenApiTool
      * JSON representation
    * GoogleSearchTool
      * JSON representation
    * GoogleSearchTool.PromptConfig
      * JSON representation
    * ConnectorTool
      * JSON representation
    * DataStoreTool
      * JSON representation
    * DataStoreTool.DataStoreSource
      * JSON representation
    * DataStore
      * JSON representation
    * DataStore.DataStoreType
    * DataStore.DocumentProcessingMode
    * DataStore.ConnectorConfig
      * JSON representation
    * DataStoreTool.EngineSource
      * JSON representation
    * DataStoreTool.BoostSpecs
      * JSON representation
    * DataStoreTool.BoostSpec
      * JSON representation
    * DataStoreTool.BoostSpec.ConditionBoostSpec
      * JSON representation
    * DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec
      * JSON representation
    * DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec.AttributeType
    * DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec.InterpolationType
    * DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec.ControlPoint
      * JSON representation
    * DataStoreTool.ModalityConfig
      * JSON representation
    * DataStoreTool.ModalityConfig.ModalityType
    * DataStoreTool.RewriterConfig
      * JSON representation
    * DataStoreTool.SummarizationConfig
      * JSON representation
    * DataStoreTool.GroundingConfig
      * JSON representation
    * DataStoreTool.SnippetsConfig
      * JSON representation
    * DataStoreTool.FilterParameterBehavior
    * PythonFunction
      * JSON representation
    * McpTool
      * JSON representation
    * McpTool.State
    * FileSearchTool
      * JSON representation
    * FileSearchTool.CorpusType
    * SystemTool
      * JSON representation
    * AgentTool
      * JSON representation
    * WidgetTool
      * JSON representation
    * WidgetTool.WidgetType
    * WidgetTool.DataMapping
      * JSON representation
    * WidgetTool.DataMapping.Mode
    * WidgetTool.TextResponseConfig
      * JSON representation
    * WidgetTool.TextResponseConfig.Type
    * RemoteAgentTool
      * JSON representation
  * Methods



## Resource: Tool

A tool represents an action that the CES agent can take to achieve certain goals.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "executionType": enum ([ExecutionType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ExecutionType)),
      "timeout": string,
      "createTime": string,
      "updateTime": string,
      "etag": string,
      "generatedSummary": string,
      "toolFakeConfig": {
        object ([ToolFakeConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ToolFakeConfig))
      },
      "readOnly": boolean,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "clientFunction": {
        object ([ClientFunction](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.ClientFunction))
      },
      "openApiTool": {
        object ([OpenApiTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.OpenApiTool))
      },
      "googleSearchTool": {
        object ([GoogleSearchTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.GoogleSearchTool))
      },
      "connectorTool": {
        object ([ConnectorTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.ConnectorTool))
      },
      "dataStoreTool": {
        object ([DataStoreTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.DataStoreTool))
      },
      "pythonFunction": {
        object ([PythonFunction](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.PythonFunction))
      },
      "mcpTool": {
        object ([McpTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.McpTool))
      },
      "fileSearchTool": {
        object ([FileSearchTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.FileSearchTool))
      },
      "systemTool": {
        object ([SystemTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.SystemTool))
      },
      "agentTool": {
        object ([AgentTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.AgentTool))
      },
      "widgetTool": {
        object ([WidgetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.WidgetTool))
      },
      "remoteAgentTool": {
        object ([RemoteAgentTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.RemoteAgentTool))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the tool. Format:

  * `projects/{project}/locations/{location}/apps/{app}/tools/{tool}` for standalone tools.
  * `projects/{project}/locations/{location}/apps/{app}/toolsets/{toolset}/tools/{tool}` for tools retrieved from a toolset.

These tools are dynamic and output-only; they cannot be referenced directly where a tool is expected.  
`displayName` |  `string` Output only. The display name of the tool, derived based on the tool's type. For example, display name of a [ClientFunction][Tool.ClientFunction] is derived from its `name` property.  
`executionType` |  `enum (`[ExecutionType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ExecutionType)`)` Optional. The execution type of the tool.  
`timeout` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. The timeout for the tool execution. If not set, the default timeout is 30 seconds for `SYNCHRONOUS` tools and 60 seconds for `ASYNCHRONOUS` tools.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the tool was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the tool was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`etag` |  `string` Etag used to ensure the object hasn't changed during a read-modify-write operation. If the etag is empty, the update will overwrite any concurrent changes.  
`generatedSummary` |  `string` Output only. If the tool is generated by the LLM assistant, this field contains a descriptive summary of the generation.  
`toolFakeConfig` |  `object (`[ToolFakeConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ToolFakeConfig)`)` Optional. Configuration for tool behavior in fake mode.  
`readOnly` |  `boolean` Output only. Indicates whether the tool is read-only. If true, the tool cannot be modified by the user.  
The type of the tool. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`clientFunction` |  `object (`[ClientFunction](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.ClientFunction)`)` Optional. The client function.  
`openApiTool` |  `object (`[OpenApiTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.OpenApiTool)`)` Optional. The open API tool.  
`googleSearchTool` |  `object (`[GoogleSearchTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.GoogleSearchTool)`)` Optional. The google search tool.  
`connectorTool` |  `object (`[ConnectorTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.ConnectorTool)`)` Optional. The Integration Connector tool.  
`dataStoreTool` |  `object (`[DataStoreTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.DataStoreTool)`)` Optional. The data store tool.  
`pythonFunction` |  `object (`[PythonFunction](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.PythonFunction)`)` Optional. The python function tool.  
`mcpTool` |  `object (`[McpTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.McpTool)`)` Optional. The MCP tool. An MCP tool cannot be created or updated directly and is managed by the MCP toolset.  
`fileSearchTool` |  `object (`[FileSearchTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.FileSearchTool)`)` Optional. The file search tool.  
`systemTool` |  `object (`[SystemTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.SystemTool)`)` Optional. The system tool.  
`agentTool` |  `object (`[AgentTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.AgentTool)`)` Optional. The agent tool.  
`widgetTool` |  `object (`[WidgetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.WidgetTool)`)` Optional. The widget tool.  
`remoteAgentTool` |  `object (`[RemoteAgentTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.RemoteAgentTool)`)` Optional. The remote agent tool.  
End of mutually exclusive fields.  
  
### ClientFunction

Represents a client-side function that the agent can invoke. When the tool is chosen by the agent, control is handed off to the client. The client is responsible for executing the function and returning the result as a `[ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ToolResponse)` to continue the interaction with the agent.

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "parameters": {
        object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Schema))
      },
      "response": {
        object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Schema))
      }
    }  
  
Fields  
---  
`name` |  `string` Required. The function name.  
`description` |  `string` Optional. The function description.  
`parameters` |  `object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Schema)`)` Optional. The schema of the function parameters.  
`response` |  `object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Schema)`)` Optional. The schema of the function response.  
  
### OpenApiTool

A remote API tool defined by an OpenAPI schema.

JSON representation  
---  
      
    
    {
      "openApiSchema": string,
      "name": string,
      "description": string,
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
`openApiSchema` |  `string` Required. The OpenAPI schema in JSON or YAML format.  
`name` |  `string` Optional. The name of the tool. If not provided, the name of the tool will be derived from the OpenAPI schema, from `operation.operationId`.  
`description` |  `string` Optional. The description of the tool. If not provided, the description of the tool will be derived from the OpenAPI schema, from `operation.description` or `operation.summary`.  
`apiAuthentication` |  `object (`[ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ApiAuthentication)`)` Optional. Authentication information required by the API.  
`tlsConfig` |  `object (`[TlsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/TlsConfig)`)` Optional. The TLS configuration. Includes the custom server certificates that the client will trust.  
`serviceDirectoryConfig` |  `object (`[ServiceDirectoryConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ServiceDirectoryConfig)`)` Optional. Service Directory configuration.  
`ignoreUnknownFields` |  `boolean` Optional. If true, the agent will ignore unknown fields in the API response.  
`url` |  `string` Optional. The server URL of the Open API schema. This field is only set in tools in the environment dependencies during the export process if the schema contains a server url. During the import process, if this url is present in the environment dependencies and the schema has the $env_var placeholder, it will replace the placeholder in the schema.  
  
### GoogleSearchTool

Represents a tool to perform Google web searches for grounding. See <https://cloud.google.com/customer-engagement-ai/conversational-agents/ps/tool#google-search>.

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
        object ([GoogleSearchTool.PromptConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.GoogleSearchTool.PromptConfig))
      }
    }  
  
Fields  
---  
`name` |  `string` Required. The name of the tool.  
`description` |  `string` Optional. Description of the tool's purpose.  
`contextUrls[]` |  `string` Optional. Content will be fetched directly from these URLs for context and grounding. Example: "https://example.com/path.html". A maximum of 20 URLs are allowed.  
`preferredDomains[]` |  `string` Optional. Specifies domains to restrict search results to. Example: "example.com", "another.site". A maximum of 20 domains can be specified.  
`excludeDomains[]` |  `string` Optional. List of domains to be excluded from the search results. Example: "example.com". A maximum of 2000 domains can be excluded.  
`promptConfig` |  `object (`[GoogleSearchTool.PromptConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.GoogleSearchTool.PromptConfig)`)` Optional. Prompt instructions passed to planner on how the search results should be processed for text and voice.  
  
### GoogleSearchTool.PromptConfig

Prompt settings used by the model when processing or summarizing the google search results.

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

A ConnectorTool allows connections to different integrations. See: <https://cloud.google.com/integration-connectors/docs/overview>.

JSON representation  
---  
      
    
    {
      "connection": string,
      "action": {
        object ([Action](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Action))
      },
      "authConfig": {
        object ([EndUserAuthConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EndUserAuthConfig))
      },
      "name": string,
      "description": string
    }  
  
Fields  
---  
`connection` |  `string` Required. The full resource name of the referenced Integration Connectors Connection. Format: `projects/{project}/locations/{location}/connections/{connection}`  
`action` |  `object (`[Action](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Action)`)` Required. Action for the tool to use.  
`authConfig` |  `object (`[EndUserAuthConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EndUserAuthConfig)`)` Optional. Configures how authentication is handled in Integration Connectors. By default, an admin authentication is passed in the Integration Connectors API requests. You can override it with a different end-user authentication config. **Note** : The Connection must have authentication override enabled in order to specify an EUC configuration here - otherwise, the ConnectorTool creation will fail. See <https://cloud.google.com/application-integration/docs/configure-connectors-task#configure-authentication-override> for details.  
`name` |  `string` Optional. The name of the tool that can be used by the Agent to decide whether to call this ConnectorTool.  
`description` |  `string` Optional. The description of the tool that can be used by the Agent to decide whether to call this ConnectorTool.  
  
### DataStoreTool

Tool to retrieve from Vertex AI Search datastore or engine for grounding. Accepts either a datastore or an engine, but not both. See Vertex AI Search: <https://cloud.google.com/generative-ai-app-builder/docs/enterprise-search-introduction>.

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "boostSpecs": [
        {
          object ([DataStoreTool.BoostSpecs](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.DataStoreTool.BoostSpecs))
        }
      ],
      "modalityConfigs": [
        {
          object ([DataStoreTool.ModalityConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.DataStoreTool.ModalityConfig))
        }
      ],
      "filterParameterBehavior": enum ([DataStoreTool.FilterParameterBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.DataStoreTool.FilterParameterBehavior)),
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "dataStoreSource": {
        object ([DataStoreTool.DataStoreSource](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.DataStoreTool.DataStoreSource))
      },
      "engineSource": {
        object ([DataStoreTool.EngineSource](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.DataStoreTool.EngineSource))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`name` |  `string` Required. The data store tool name.  
`description` |  `string` Optional. The tool description.  
`boostSpecs[]` |  `object (`[DataStoreTool.BoostSpecs](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.DataStoreTool.BoostSpecs)`)` Optional. Boost specification to boost certain documents.  
`modalityConfigs[]` |  `object (`[DataStoreTool.ModalityConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.DataStoreTool.ModalityConfig)`)` Optional. The modality configs for the data store.  
`filterParameterBehavior` |  `enum (`[DataStoreTool.FilterParameterBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.DataStoreTool.FilterParameterBehavior)`)` Optional. The filter parameter behavior.  
Defines the search source, either a single DataStore or an Engine. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`dataStoreSource` |  `object (`[DataStoreTool.DataStoreSource](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.DataStoreTool.DataStoreSource)`)` Optional. Search within a single specific DataStore.  
`engineSource` |  `object (`[DataStoreTool.EngineSource](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.DataStoreTool.EngineSource)`)` Optional. Search within an Engine (potentially across multiple DataStores).  
End of mutually exclusive fields.  
  
### DataStoreTool.DataStoreSource

Configuration for searching within a specific DataStore.

JSON representation  
---  
      
    
    {
      "filter": string,
      "dataStore": {
        object ([DataStore](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.DataStore))
      }
    }  
  
Fields  
---  
`filter` |  `string` Optional. Filter specification for the DataStore. See: <https://cloud.google.com/generative-ai-app-builder/docs/filter-search-metadata>  
`dataStore` |  `object (`[DataStore](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.DataStore)`)` Optional. The data store.  
  
### DataStore

A DataStore resource in Vertex AI Search.

JSON representation  
---  
      
    
    {
      "name": string,
      "type": enum ([DataStore.DataStoreType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.DataStore.DataStoreType)),
      "documentProcessingMode": enum ([DataStore.DocumentProcessingMode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.DataStore.DocumentProcessingMode)),
      "displayName": string,
      "createTime": string,
      "connectorConfig": {
        object ([DataStore.ConnectorConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.DataStore.ConnectorConfig))
      }
    }  
  
Fields  
---  
`name` |  `string` Required. Full resource name of the DataStore. Format: `projects/{project}/locations/{location}/collections/{collection}/dataStores/{dataStore}`  
`type` |  `enum (`[DataStore.DataStoreType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.DataStore.DataStoreType)`)` Output only. The type of the data store. This field is readonly and populated by the server.  
`documentProcessingMode` |  `enum (`[DataStore.DocumentProcessingMode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.DataStore.DocumentProcessingMode)`)` Output only. The document processing mode for the data store connection. Only set for PUBLIC_WEB and UNSTRUCTURED data stores.  
`displayName` |  `string` Output only. The display name of the data store.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the data store was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`connectorConfig` |  `object (`[DataStore.ConnectorConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.DataStore.ConnectorConfig)`)` Output only. The connector config for the data store connection.  
  
### DataStore.DataStoreType

The type of the data store.

Enums  
---  
`DATA_STORE_TYPE_UNSPECIFIED` | Not specified. This value indicates that the data store type is not specified, so it will not be used during search.  
`PUBLIC_WEB` | A data store that contains public web content.  
`UNSTRUCTURED` | A data store that contains unstructured private data.  
`FAQ` | A data store that contains structured data used as FAQ.  
`CONNECTOR` | A data store that is a connector to a first-party or a third-party service.  
  
### DataStore.DocumentProcessingMode

The document processing mode of the data store.

Enums  
---  
`DOCUMENT_PROCESSING_MODE_UNSPECIFIED` | Not specified.  
`DOCUMENTS` | Documents are processed as documents.  
`CHUNKS` | Documents are converted to chunks.  
  
### DataStore.ConnectorConfig

The connector config for the data store connection.

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
  
### DataStoreTool.EngineSource

Configuration for searching within an Engine, potentially targeting specific DataStores.

JSON representation  
---  
      
    
    {
      "engine": string,
      "dataStoreSources": [
        {
          object ([DataStoreTool.DataStoreSource](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.DataStoreTool.DataStoreSource))
        }
      ],
      "filter": string
    }  
  
Fields  
---  
`engine` |  `string` Required. Full resource name of the Engine. Format: `projects/{project}/locations/{location}/collections/{collection}/engines/{engine}`  
`dataStoreSources[]` |  `object (`[DataStoreTool.DataStoreSource](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.DataStoreTool.DataStoreSource)`)` Optional. Use to target specific DataStores within the Engine. If empty, the search applies to all DataStores associated with the Engine.  
`filter` |  `string` Optional. A filter applied to the search across the Engine. Not relevant and not used if 'dataStoreSources' is provided. See: <https://cloud.google.com/generative-ai-app-builder/docs/filter-search-metadata>  
  
### DataStoreTool.BoostSpecs

Boost specifications to boost certain documents. For more information, please refer to <https://cloud.google.com/generative-ai-app-builder/docs/boosting>.

JSON representation  
---  
      
    
    {
      "dataStores": [
        string
      ],
      "spec": [
        {
          object ([DataStoreTool.BoostSpec](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.DataStoreTool.BoostSpec))
        }
      ]
    }  
  
Fields  
---  
`dataStores[]` |  `string` Required. The Data Store where the boosting configuration is applied. Full resource name of DataStore, such as projects/{project}/locations/{location}/collections/{collection}/dataStores/{dataStore}.  
`spec[]` |  `object (`[DataStoreTool.BoostSpec](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.DataStoreTool.BoostSpec)`)` Required. A list of boosting specifications.  
  
### DataStoreTool.BoostSpec

Boost specification to boost certain documents.

JSON representation  
---  
      
    
    {
      "conditionBoostSpecs": [
        {
          object ([DataStoreTool.BoostSpec.ConditionBoostSpec](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.DataStoreTool.BoostSpec.ConditionBoostSpec))
        }
      ]
    }  
  
Fields  
---  
`conditionBoostSpecs[]` |  `object (`[DataStoreTool.BoostSpec.ConditionBoostSpec](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.DataStoreTool.BoostSpec.ConditionBoostSpec)`)` Required. A list of boosting specifications.  
  
### DataStoreTool.BoostSpec.ConditionBoostSpec

Boost specification for a condition.

JSON representation  
---  
      
    
    {
      "condition": string,
      "boost": number,
      "boostControlSpec": {
        object ([DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec))
      }
    }  
  
Fields  
---  
`condition` |  `string` Required. An expression which specifies a boost condition. The syntax is the same as filter expression syntax. Currently, the only supported condition is a list of BCP-47 lang codes. Example: To boost suggestions in languages en or fr: (lang_code: ANY("en", "fr"))  
`boost` |  `number` Optional. Strength of the boost, which should be in [-1, 1]. Negative boost means demotion. Default is 0.0.Setting to 1.0 gives the suggestions a big promotion. However, it does not necessarily mean that the top result will be a boosted suggestion.Setting to -1.0 gives the suggestions a big demotion. However, other suggestions that are relevant might still be shown.Setting to 0.0 means no boost applied. The boosting condition is ignored.  
`boostControlSpec` |  `object (`[DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec)`)` Optional. Complex specification for custom ranking based on customer defined attribute value.  
  
### DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec

Specification for custom ranking based on customer specified attribute value. It provides more controls for customized ranking than the simple (condition, boost) combination above.

JSON representation  
---  
      
    
    {
      "fieldName": string,
      "attributeType": enum ([DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec.AttributeType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec.AttributeType)),
      "interpolationType": enum ([DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec.InterpolationType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec.InterpolationType)),
      "controlPoints": [
        {
          object ([DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec.ControlPoint](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec.ControlPoint))
        }
      ]
    }  
  
Fields  
---  
`fieldName` |  `string` Optional. The name of the field whose value will be used to determine the boost amount.  
`attributeType` |  `enum (`[DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec.AttributeType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec.AttributeType)`)` Optional. The attribute type to be used to determine the boost amount. The attribute value can be derived from the field value of the specified fieldName. In the case of numerical it is straightforward i.e. attributeValue = numerical_field_value. In the case of freshness however, attributeValue = (time.now() - datetime_field_value).  
`interpolationType` |  `enum (`[DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec.InterpolationType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec.InterpolationType)`)` Optional. The interpolation type to be applied to connect the control points listed below.  
`controlPoints[]` |  `object (`[DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec.ControlPoint](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec.ControlPoint)`)` Optional. The control points used to define the curve. The monotonic function (defined through the interpolationType above) passes through the control points listed here.  
  
### DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec.AttributeType

The attribute(or function) for which the custom ranking is to be applied.

Enums  
---  
`ATTRIBUTE_TYPE_UNSPECIFIED` | Unspecified AttributeType.  
`NUMERICAL` | The value of the numerical field will be used to dynamically update the boost amount. In this case, the attributeValue (the x value) of the control point will be the actual value of the numerical field for which the boostAmount is specified.  
`FRESHNESS` | For the freshness use case the attribute value will be the duration between the current time and the date in the datetime field specified. The value must be formatted as an XSD `dayTimeDuration` value (a restricted subset of an ISO 8601 duration value). The pattern for this is: `[nD][T[nH][nM][nS]]`. E.g. `5D`, `3DT12H30M`, `T24H`.  
  
### DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec.InterpolationType

The interpolation type to be applied. Default will be linear (Piecewise Linear).

Enums  
---  
`INTERPOLATION_TYPE_UNSPECIFIED` | Interpolation type is unspecified. In this case, it defaults to Linear.  
`LINEAR` | Piecewise linear interpolation will be applied.  
  
### DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec.ControlPoint

The control points used to define the curve. The curve defined through these control points can only be monotonically increasing or decreasing(constant values are acceptable).

JSON representation  
---  
      
    
    {
      "attributeValue": string,
      "boostAmount": number
    }  
  
Fields  
---  
`attributeValue` |  `string` Optional. Can be one of: 1. The numerical field value. 2. The duration spec for freshness: The value must be formatted as an XSD `dayTimeDuration` value (a restricted subset of an ISO 8601 duration value). The pattern for this is: `[nD][T[nH][nM][nS]]`.  
`boostAmount` |  `number` Optional. The value between -1 to 1 by which to boost the score if the attributeValue evaluates to the value specified above.  
  
### DataStoreTool.ModalityConfig

If specified, will apply the given configuration for the specified modality.

JSON representation  
---  
      
    
    {
      "modalityType": enum ([DataStoreTool.ModalityConfig.ModalityType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.DataStoreTool.ModalityConfig.ModalityType)),
      "rewriterConfig": {
        object ([DataStoreTool.RewriterConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.DataStoreTool.RewriterConfig))
      },
      "summarizationConfig": {
        object ([DataStoreTool.SummarizationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.DataStoreTool.SummarizationConfig))
      },
      "groundingConfig": {
        object ([DataStoreTool.GroundingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.DataStoreTool.GroundingConfig))
      },
      "snippetsConfig": {
        object ([DataStoreTool.SnippetsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.DataStoreTool.SnippetsConfig))
      }
    }  
  
Fields  
---  
`modalityType` |  `enum (`[DataStoreTool.ModalityConfig.ModalityType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.DataStoreTool.ModalityConfig.ModalityType)`)` Required. The modality type.  
`rewriterConfig` |  `object (`[DataStoreTool.RewriterConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.DataStoreTool.RewriterConfig)`)` Optional. The rewriter config.  
`summarizationConfig` |  `object (`[DataStoreTool.SummarizationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.DataStoreTool.SummarizationConfig)`)` Optional. The summarization config.  
`groundingConfig` |  `object (`[DataStoreTool.GroundingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.DataStoreTool.GroundingConfig)`)` Optional. The grounding configuration.  
`snippetsConfig` |  `object (`[DataStoreTool.SnippetsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.DataStoreTool.SnippetsConfig)`)` Optional. The snippets configuration.  
  
### DataStoreTool.ModalityConfig.ModalityType

The modality type.

Enums  
---  
`MODALITY_TYPE_UNSPECIFIED` | Unspecified modality type.  
`TEXT` | Text modality.  
`AUDIO` | Audio modality.  
  
### DataStoreTool.RewriterConfig

Rewriter configuration.

JSON representation  
---  
      
    
    {
      "modelSettings": {
        object ([ModelSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ModelSettings))
      },
      "prompt": string,
      "disabled": boolean
    }  
  
Fields  
---  
`modelSettings` |  `object (`[ModelSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ModelSettings)`)` Required. Configurations for the LLM model.  
`prompt` |  `string` Optional. The prompt definition. If not set, default prompt will be used.  
`disabled` |  `boolean` Optional. Whether the rewriter is disabled.  
  
### DataStoreTool.SummarizationConfig

Summarization configuration.

JSON representation  
---  
      
    
    {
      "modelSettings": {
        object ([ModelSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ModelSettings))
      },
      "prompt": string,
      "disabled": boolean
    }  
  
Fields  
---  
`modelSettings` |  `object (`[ModelSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ModelSettings)`)` Optional. Configurations for the LLM model.  
`prompt` |  `string` Optional. The prompt definition. If not set, default prompt will be used.  
`disabled` |  `boolean` Optional. Whether summarization is disabled.  
  
### DataStoreTool.GroundingConfig

Grounding configuration.

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
  
### DataStoreTool.SnippetsConfig

Snippets configuration.

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
  
### DataStoreTool.FilterParameterBehavior

Filter parameter behavior.

Enums  
---  
`FILTER_PARAMETER_BEHAVIOR_UNSPECIFIED` | Default filter behavior. Include filter parameter for connector datastores. For the rest of the datastore types, the filter input parameter is omitted.  
`ALWAYS_INCLUDE` | Always include filter parameter for all datastore types.  
`NEVER_INCLUDE` | The filter parameter is never included in the list of tool parameters, regardless of the datastore type.  
  
### PythonFunction

A Python function tool.

JSON representation  
---  
      
    
    {
      "name": string,
      "pythonCode": string,
      "description": string,
      "serviceDirectoryConfig": {
        object ([ServiceDirectoryConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ServiceDirectoryConfig))
      }
    }  
  
Fields  
---  
`name` |  `string` Optional. The name of the Python function to execute. Must match a Python function name defined in the python code. Case sensitive. If the name is not provided, the first function defined in the python code will be used.  
`pythonCode` |  `string` Optional. The Python code to execute for the tool.  
`description` |  `string` Output only. The description of the Python function, parsed from the python code's docstring.  
`serviceDirectoryConfig` |  `object (`[ServiceDirectoryConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ServiceDirectoryConfig)`)` Optional. Service Directory configuration for the tool.  
  
### McpTool

An MCP tool. See <https://modelcontextprotocol.io/specification/2025-06-18/server/tools> for more details.

JSON representation  
---  
      
    
    {
      "name": string,
      "nameOverride": string,
      "description": string,
      "inputSchema": {
        object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Schema))
      },
      "outputSchema": {
        object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Schema))
      },
      "serverAddress": string,
      "apiAuthentication": {
        object ([ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ApiAuthentication))
      },
      "tlsConfig": {
        object ([TlsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/TlsConfig))
      },
      "serviceDirectoryConfig": {
        object ([ServiceDirectoryConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ServiceDirectoryConfig))
      },
      "customHeaders": {
        string: string,
        ...
      },
      "state": enum ([McpTool.State](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.McpTool.State))
    }  
  
Fields  
---  
`name` |  `string` Required. The name of the MCP tool.  
`nameOverride` |  `string` Optional. The name override of the MCP tool. This is populated if the name was overridden by a Toolset override.  
`description` |  `string` Optional. The description of the MCP tool.  
`inputSchema` |  `object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Schema)`)` Optional. The schema of the input arguments of the MCP tool.  
`outputSchema` |  `object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Schema)`)` Optional. The schema of the output arguments of the MCP tool.  
`serverAddress` |  `string` Required. The server address of the MCP server, e.g., "https://example.com/mcp/". If the server is built with the MCP SDK, the url should be suffixed with "/mcp/". Only Streamable HTTP transport based servers are supported. This is the same as the serverAddress in the McpToolset. See <https://modelcontextprotocol.io/specification/2025-03-26/basic/transports#streamable-http> for more details.  
`apiAuthentication` |  `object (`[ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ApiAuthentication)`)` Optional. Authentication information required to execute the tool against the MCP server. For bearer token authentication, the token applies only to tool execution, not to listing tools. This requires that tools can be listed without authentication.  
`tlsConfig` |  `object (`[TlsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/TlsConfig)`)` Optional. The TLS configuration. Includes the custom server certificates that the client should trust.  
`serviceDirectoryConfig` |  `object (`[ServiceDirectoryConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ServiceDirectoryConfig)`)` Optional. Service Directory configuration for VPC-SC, used to resolve service names within a perimeter.  
`customHeaders` |  `map (key: string, value: string)` Optional. The custom headers to send in the request to the MCP server. The values must be in the format `$context.variables.<name_of_variable>` and can be set in the session variables. See <https://docs.cloud.google.com/customer-engagement-ai/conversational-agents/ps/tool/open-api#openapi-injection> for more details.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`state` |  `enum (`[McpTool.State](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.McpTool.State)`)` Output only. The dynamic availability state of the tool on the external server.  
  
### McpTool.State

Represents the dynamic availability state of the tool.

Enums  
---  
`STATE_UNSPECIFIED` | Default state.  
`ACTIVE` | The tool is available and actively offered by the server.  
`INACTIVE` | The tool is configured or pinned, but currently not offered by the server.  
`STALE` | The tool exists on the server, but does not match the version on the server.  
  
### FileSearchTool

The file search tool allows the agent to search across the files uploaded by the app/agent developer. It has presets to give relatively good quality search over the uploaded files and summarization of the retrieved results.

JSON representation  
---  
      
    
    {
      "corpusType": enum ([FileSearchTool.CorpusType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.FileSearchTool.CorpusType)),
      "name": string,
      "description": string,
      "fileCorpus": string
    }  
  
Fields  
---  
`corpusType` |  `enum (`[FileSearchTool.CorpusType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.FileSearchTool.CorpusType)`)` Optional. The type of the corpus. Default is FULLY_MANAGED.  
`name` |  `string` Required. The tool name.  
`description` |  `string` Optional. The tool description.  
`fileCorpus` |  `string` Optional. The corpus where files are stored. Format: projects/{project}/locations/{location}/ragCorpora/{rag_corpus}  
  
### FileSearchTool.CorpusType

The type of the Vertex RAG corpus.

Enums  
---  
`CORPUS_TYPE_UNSPECIFIED` | Unspecified corpus type.  
`USER_OWNED` | The corpus is created and owned by the user.  
`FULLY_MANAGED` | The corpus is created by the agent.  
  
### SystemTool

Pre-defined system tool.

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

Represents a tool that allows the agent to call another agent.

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

Represents a widget tool that the agent can invoke. When the tool is chosen by the agent, agent will return the widget to the client. The client is responsible for processing the widget and generating the next user query to continue the interaction with the agent.

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "widgetType": enum ([WidgetTool.WidgetType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.WidgetTool.WidgetType)),
      "uiConfig": {
        object
      },
      "dataMapping": {
        object ([WidgetTool.DataMapping](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.WidgetTool.DataMapping))
      },
      "textResponseConfig": {
        object ([WidgetTool.TextResponseConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.WidgetTool.TextResponseConfig))
      },
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "parameters": {
        object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Schema))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`name` |  `string` Required. The display name of the widget tool.  
`description` |  `string` Optional. The description of the widget tool.  
`widgetType` |  `enum (`[WidgetTool.WidgetType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.WidgetTool.WidgetType)`)` Optional. The type of the widget tool. If not specified, the default type will be CUSTOMIZED.  
`uiConfig` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. Configuration for rendering the widget.  
`dataMapping` |  `object (`[WidgetTool.DataMapping](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.WidgetTool.DataMapping)`)` Optional. The mapping that defines how data from a source tool is mapped to the widget's input parameters.  
`textResponseConfig` |  `object (`[WidgetTool.TextResponseConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.WidgetTool.TextResponseConfig)`)` Optional. Configuration for always-included text responses.  
The input of the widget tool. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`parameters` |  `object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Schema)`)` Optional. The input parameters of the widget tool.  
End of mutually exclusive fields.  
  
### WidgetTool.WidgetType

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
  
### WidgetTool.DataMapping

Configuration for mapping data from a source tool to the widget's input parameters.

JSON representation  
---  
      
    
    {
      "sourceToolName": string,
      "fieldMappings": {
        string: string,
        ...
      },
      "pythonFunction": {
        object ([PythonFunction](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.PythonFunction))
      },
      "mode": enum ([WidgetTool.DataMapping.Mode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.WidgetTool.DataMapping.Mode)),
      "pythonScript": string
    }  
  
Fields  
---  
`sourceToolName` |  `string` Optional. The resource name of the tool that provides the data for the widget (e.g., a search tool or a custom function). Format: `projects/{project}/locations/{location}/agents/{agent}/tools/{tool}`  
`fieldMappings` |  `map (key: string, value: string)` Optional. A map of widget input parameter fields to the corresponding output fields of the source tool.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`pythonFunction` |  `object (`[PythonFunction](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.PythonFunction)`)` Optional. Configuration for a Python function used to transform the source tool's output into the widget's input format.  
`mode` |  `enum (`[WidgetTool.DataMapping.Mode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.WidgetTool.DataMapping.Mode)`)` Optional. The mode of the data mapping.  
`pythonScript  
**(deprecated)**` |  `string` This item is deprecated!Deprecated: Use `pythonFunction` instead.  
  
### WidgetTool.DataMapping.Mode

The strategy used to map data from the source tool to the widget.

Enums  
---  
`MODE_UNSPECIFIED` | Unspecified mode.  
`FIELD_MAPPING` | Use the `fieldMappings` map for data transformation.  
`PYTHON_SCRIPT` | Use the `pythonScript` for data transformation.  
  
### WidgetTool.TextResponseConfig

Configuration for the text response returned with the widget.

JSON representation  
---  
      
    
    {
      "type": enum ([WidgetTool.TextResponseConfig.Type](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.WidgetTool.TextResponseConfig.Type)),
      "staticText": string,
      "textResponseInstruction": string
    }  
  
Fields  
---  
`type` |  `enum (`[WidgetTool.TextResponseConfig.Type](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.WidgetTool.TextResponseConfig.Type)`)` Optional. The strategy for providing the text response.  
`staticText` |  `string` Optional. The static text response to return when type is STATIC.  
`textResponseInstruction` |  `string` Optional. Instruction for the LLM on how to generate the text response. Used as the description for the text response parameter if type is LLM_GENERATED.  
  
### WidgetTool.TextResponseConfig.Type

Defines how the text response is produced.

Enums  
---  
`TYPE_UNSPECIFIED` | Unspecified type.  
`NONE` | The LLM dynamically decides whether to generate a text response alongside the widget based on the conversation context.  
`LLM_GENERATED` | The LLM is explicitly required to generate a text response.  
`STATIC` | A pre-defined static text response is always used.  
  
### RemoteAgentTool

Represents a tool that allows the agent to call another remote agent.

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "agentCard": {
        object ([AgentCard](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/AgentCard))
      },
      "apiAuthentication": {
        object ([ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ApiAuthentication))
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
`agentCard` |  `object (`[AgentCard](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/AgentCard)`)` Required. The agent card of the remote agent that this tool invokes.  
`apiAuthentication` |  `object (`[ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ApiAuthentication)`)` Optional. Authentication configuration for calling the remote agent.  
`statefulAgent` |  `boolean` Optional. When enabled, the interaction between the CXAS app and the remote agent will share the same context. If the remote agent returns a contextId, it will be persisted for the entirety of the session for this remote agent tool.  
`inputVariableMapping` |  `map (key: string, value: string)` Optional. Mapping of input variable names of remote agent to GECX variable names.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`outputVariableMapping` |  `map (key: string, value: string)` Optional. Mapping of output variable names of remote agent to GECX variable names.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools/create)`

|  Creates a new tool in the given app.  
  
### `[delete](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools/delete)`

|  Deletes the specified tool.  
  
### `[get](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools/get)`

|  Gets details of the specified tool.  
  
### `[list](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools/list)`

|  Lists tools in the given app.  
  
### `[patch](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools/patch)`

|  Updates the specified tool.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
