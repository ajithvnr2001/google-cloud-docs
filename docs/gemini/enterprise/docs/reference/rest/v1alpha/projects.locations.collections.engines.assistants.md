---
url: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants
title: REST Resource: projects.locations.collections.engines.assistants \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:52:34.394210+00:00
---

# REST Resource: projects.locations.collections.engines.assistants  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Reference ](https://docs.cloud.google.com/gemini/enterprise/docs/apis)



Send feedback 

#  REST Resource: projects.locations.collections.engines.assistants Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Assistant
    * JSON representation
  * GenerationConfig
    * JSON representation
  * SystemInstruction
    * JSON representation
  * WebGroundingType
  * MapsGroundingType
  * VertexAiAgentConfig
    * JSON representation
  * ActionList
    * JSON representation
  * ActionInfo
    * JSON representation
  * ToolList
    * JSON representation
  * ToolInfo
    * JSON representation
  * CustomerPolicy
    * JSON representation
  * BannedPhrase
    * JSON representation
  * BannedPhraseMatchType
  * ModelArmorConfig
    * JSON representation
  * FailureMode
  * VertexAiSearchToolConfig
    * JSON representation
  * AgentConfig
    * JSON representation
  * VertexAiSdkAgentConnectionInfo
    * JSON representation
  * HttpAgentConnectionInfo
    * JSON representation
  * Image
    * JSON representation
  * Methods



## Resource: Assistant

Discovery Engine Assistant resource.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "generationConfig": {
        object ([GenerationConfig](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants#GenerationConfig))
      },
      "googleSearchGroundingEnabled": boolean,
      "webGroundingType": enum ([WebGroundingType](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants#WebGroundingType)),
      "defaultWebGroundingToggleOff": boolean,
      "mapsGroundingType": enum ([MapsGroundingType](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants#MapsGroundingType)),
      "defaultMapsGroundingToggleOff": boolean,
      "vertexAiAgentConfigs": [
        {
          object ([VertexAiAgentConfig](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants#VertexAiAgentConfig))
        }
      ],
      "enabledActions": {
        string: {
          object ([ActionList](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants#ActionList))
        },
        ...
      },
      "enabledTools": {
        string: {
          object ([ToolList](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants#ToolList))
        },
        ...
      },
      "customerPolicy": {
        object ([CustomerPolicy](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants#CustomerPolicy))
      },
      "vertexAiSearchToolConfig": {
        object ([VertexAiSearchToolConfig](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants#VertexAiSearchToolConfig))
      },
      "styleAndFormattingInstructions": string,
      "agentConfigs": [
        {
          object ([AgentConfig](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants#AgentConfig))
        }
      ],
      "enableEndUserAgentCreation": boolean,
      "disableLocationContext": boolean,
      "createTime": string,
      "updateTime": string,
      "knowledgeCatalogEnabled": boolean
    }  
  
Fields  
---  
`name` |  `string` Immutable. Resource name of the assistant. Format: `projects/{project}/locations/{location}/collections/{collection}/engines/{engine}/assistants/{assistant}`It must be a UTF-8 encoded string with a length limit of 1024 characters.  
`displayName` |  `string` Required. The assistant display name.It must be a UTF-8 encoded string with a length limit of 128 characters.  
`description` |  `string` Optional. Description for additional information. Expected to be shown on the configuration UI, not to the users of the assistant.  
`generationConfig` |  `object (`[GenerationConfig](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants#GenerationConfig)`)` Optional. Configuration for the generation of the assistant response.  
`googleSearchGroundingEnabled  
**(deprecated)**` |  `boolean` This item is deprecated!Optional. Deprecated: Use `[webGroundingType](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants#Assistant.FIELDS.web_grounding_type)` instead.  
`webGroundingType` |  `enum (`[WebGroundingType](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants#WebGroundingType)`)` Optional. The type of web grounding to use.  
`defaultWebGroundingToggleOff` |  `boolean` Optional. This field controls the default web grounding toggle for end users if `webGroundingType` is set to `WEB_GROUNDING_TYPE_GOOGLE_SEARCH` or `WEB_GROUNDING_TYPE_ENTERPRISE_WEB_SEARCH`. By default, this field is set to false. If `webGroundingType` is `WEB_GROUNDING_TYPE_GOOGLE_SEARCH` or `WEB_GROUNDING_TYPE_ENTERPRISE_WEB_SEARCH`, end users will have web grounding enabled by default on UI. If true, grounding toggle will be disabled by default on UI. End users can still enable web grounding in the UI if web grounding is enabled.  
`mapsGroundingType` |  `enum (`[MapsGroundingType](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants#MapsGroundingType)`)` Optional. The type of Google Maps grounding to use.  
`defaultMapsGroundingToggleOff` |  `boolean` Optional. This field controls the default maps grounding toggle for end users if `mapsGroundingType` is set to `MAPS_GROUNDING_TYPE_GOOGLE_MAPS`. By default, this field is set to false. If `mapsGroundingType` is `MAPS_GROUNDING_TYPE_GOOGLE_MAPS`, end users will have maps grounding enabled by default on UI. If true, the grounding toggle will default to the OFF position in the UI. End users can still enable maps grounding in the UI if maps grounding is enabled.  
`vertexAiAgentConfigs[]  
**(deprecated)**` |  `object (`[VertexAiAgentConfig](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants#VertexAiAgentConfig)`)` This item is deprecated!Optional. Deprecated: Will be replaced by Dialogflow agents in AgentService. List of Vertex AI Agents that can be reached through the assistant.  
`enabledActions  
**(deprecated)**` |  `map (key: string, value: object (`[ActionList](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants#ActionList)`))` This item is deprecated!Optional. Deprecated: will be replaced by `[enabledTools](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants#Assistant.FIELDS.enabled_tools)` instead. The enabled actions on this assistant. The keys are connector name, for example "projects/{projectId}/locations/{locationId}/collections/{collectionId}/dataconnector The values consist of admin enabled actions towards the connector instance. Admin can selectively enable multiple actions on any of the connector instances that they created in the project. For example {"jira1ConnectorName": [(actionId1, "createTicket"), (actionId2, "transferTicket")], "gmail1ConnectorName": [(actionId3, "sendEmail"),..] }  
`enabledTools` |  `map (key: string, value: object (`[ToolList](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants#ToolList)`))` Optional. Note: not implemented yet. Use `[enabledActions](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants#Assistant.FIELDS.enabled_actions)` instead. The enabled tools on this assistant. The keys are connector name, for example "projects/{projectId}/locations/{locationId}/collections/{collectionId}/dataconnector The values consist of admin enabled tools towards the connector instance. Admin can selectively enable multiple tools on any of the connector instances that they created in the project. For example {"jira1ConnectorName": [(toolId1, "createTicket"), (toolId2, "transferTicket")], "gmail1ConnectorName": [(toolId3, "sendEmail"),..] }  
`customerPolicy` |  `object (`[CustomerPolicy](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants#CustomerPolicy)`)` Optional. Customer policy for the assistant.  
`vertexAiSearchToolConfig` |  `object (`[VertexAiSearchToolConfig](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants#VertexAiSearchToolConfig)`)` Optional. Configuration options for the Vertex AI Search tool.  
`styleAndFormattingInstructions  
**(deprecated)**` |  `string` This item is deprecated!Optional. Deprecated: Please use `[additionalSystemInstruction](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants#SystemInstruction.FIELDS.additional_system_instruction)` instead. Common system instruction snippet for setting conversation style, tone and formatting. Added to all LLM prompts via the placeholder `[STYLE_AND_FORMATTING_INSTRUCTIONS]`.  
`agentConfigs[]  
**(deprecated)**` |  `object (`[AgentConfig](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants#AgentConfig)`)` This item is deprecated!Optional. Deprecated: Please use AgentService instead. List of Agents that can be reached through the assistant.  
`enableEndUserAgentCreation` |  `boolean` Optional. Indicates whether end users are allowed to create agents in the Agentspace.  
`disableLocationContext` |  `boolean` Optional. Indicates whether to disable user location context. By default, user location context is enabled.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Represents the time when this Assistant was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Represents the time when this Assistant was most recently updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`knowledgeCatalogEnabled` |  `boolean` Optional. Indicates whether Knowledge Catalog is enabled for this specific assistant. When enabled, it powers discovery context using organizational data. If unspecified, defaults to true.  
  
## GenerationConfig

Configuration for the generation of the assistant response.

JSON representation  
---  
      
    
    {
      "defaultModelId": string,
      "allowedModelIds": [
        string
      ],
      "systemInstruction": {
        object ([SystemInstruction](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants#SystemInstruction))
      },
      "defaultLanguage": string
    }  
  
Fields  
---  
`defaultModelId` |  `string` Optional. The default model to use for assistant.  
`allowedModelIds[]` |  `string` Optional. The list of models that are allowed to be used for assistant.  
`systemInstruction` |  `object (`[SystemInstruction](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants#SystemInstruction)`)` System instruction, also known as the prompt preamble for LLM calls. See also <https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/system-instructions>  
`defaultLanguage` |  `string` The default language to use for the generation of the assistant response. Use an ISO 639-1 language code such as `en`. If not specified, the language will be automatically detected.  
  
## SystemInstruction

System instruction, also known as the prompt preamble for LLM calls.

JSON representation  
---  
      
    
    {
      "additionalSystemInstruction": string
    }  
  
Fields  
---  
`additionalSystemInstruction` |  `string` Optional. Additional system instruction that will be added to the default system instruction.  
  
## WebGroundingType

The type of web grounding to use.

Enums  
---  
`WEB_GROUNDING_TYPE_UNSPECIFIED` | Default, unspecified setting. This is the same as disabled.  
`WEB_GROUNDING_TYPE_DISABLED` | Web grounding is disabled.  
`WEB_GROUNDING_TYPE_GOOGLE_SEARCH` | Grounding with Google Search is enabled.  
`WEB_GROUNDING_TYPE_ENTERPRISE_WEB_SEARCH` | Grounding with Enterprise Web Search is enabled.  
  
## MapsGroundingType

The type of Google Maps grounding to use.

Enums  
---  
`MAPS_GROUNDING_TYPE_UNSPECIFIED` | Default, unspecified setting. This is the same as disabled.  
`MAPS_GROUNDING_TYPE_DISABLED` | Maps grounding is disabled.  
`MAPS_GROUNDING_TYPE_GOOGLE_MAPS` | Grounding with Google Maps is enabled.  
  
## VertexAiAgentConfig

This item is deprecated!

Deprecated: Use Dialogflow agents in AgentService instead. Represents an external Vertex AI Agent that can be reached through the assistant.

JSON representation  
---  
      
    
    {
      "displayName": string,
      "name": string,
      "toolDescription": string
    }  
  
Fields  
---  
`displayName` |  `string` Required. Display name of the Vertex AI Agent used for reference in the assistant.  
`name` |  `string` Required. Resource name of the Vertex AI Agent. Format: `projects/{project}/locations/{location}/agents/{agent}`  
`toolDescription` |  `string` Required. The tool description of the Vertex AI Agent. This description will be used by the LLM to decide whether the agent is relevant to the user question and the question should be routed to the agent.  
  
## ActionList

This item is deprecated!

Deprecated: Will be replaced by `[ToolList](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants#ToolList)` instead. The enabled actions on a connector

JSON representation  
---  
      
    
    {
      "actionInfo": [
        {
          object ([ActionInfo](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants#ActionInfo))
        }
      ]
    }  
  
Fields  
---  
`actionInfo[]` |  `object (`[ActionInfo](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants#ActionInfo)`)` The list of actions with corresponding action information.  
  
## ActionInfo

This item is deprecated!

Deprecated: Will be replaced by `[ToolInfo](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants#ToolInfo)` instead. Information to identify an action.

JSON representation  
---  
      
    
    {
      "actionName": string,
      "actionDisplayName": string
    }  
  
Fields  
---  
`actionName` |  `string` The name of the action as defined by DataConnectorService.QueryAvailableActions.  
`actionDisplayName` |  `string` The display name of the action.  
  
## ToolList

The enabled tools on a connector

JSON representation  
---  
      
    
    {
      "toolInfo": [
        {
          object ([ToolInfo](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants#ToolInfo))
        }
      ]
    }  
  
Fields  
---  
`toolInfo[]` |  `object (`[ToolInfo](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants#ToolInfo)`)` The list of tools with corresponding tool information.  
  
## ToolInfo

Information to identify a tool.

JSON representation  
---  
      
    
    {
      "toolName": string,
      "toolDisplayName": string
    }  
  
Fields  
---  
`toolName` |  `string` The name of the tool as defined by DataConnectorService.QueryAvailableActions. Note: it's using `action` in the DataConnectorService apis, but they are the same as the `tool` here.  
`toolDisplayName` |  `string` The display name of the tool.  
  
## CustomerPolicy

Customer-defined policy for the assistant.

JSON representation  
---  
      
    
    {
      "bannedPhrases": [
        {
          object ([BannedPhrase](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants#BannedPhrase))
        }
      ],
      "modelArmorConfig": {
        object ([ModelArmorConfig](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants#ModelArmorConfig))
      },
      "dataProtectionPolicy": {
        object ([DataProtectionPolicy](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/DataProtectionPolicy))
      }
    }  
  
Fields  
---  
`bannedPhrases[]` |  `object (`[BannedPhrase](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants#BannedPhrase)`)` Optional. List of banned phrases.  
`modelArmorConfig` |  `object (`[ModelArmorConfig](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants#ModelArmorConfig)`)` Optional. Model Armor configuration to be used for sanitizing user prompts and assistant responses.  
`dataProtectionPolicy` |  `object (`[DataProtectionPolicy](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/DataProtectionPolicy)`)` Optional. data protection policy to be used for sanitizing file uploads.  
  
## BannedPhrase

Definition of a customer-defined banned phrase. A banned phrase is not allowed to appear in the user query or the LLM response, or else the answer will be refused.

JSON representation  
---  
      
    
    {
      "phrase": string,
      "matchType": enum ([BannedPhraseMatchType](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants#BannedPhraseMatchType)),
      "ignoreDiacritics": boolean
    }  
  
Fields  
---  
`phrase` |  `string` Required. The raw string content to be banned.  
`matchType` |  `enum (`[BannedPhraseMatchType](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants#BannedPhraseMatchType)`)` Optional. Match type for the banned phrase.  
`ignoreDiacritics` |  `boolean` Optional. If true, diacritical marks (e.g., accents, umlauts) are ignored when matching banned phrases. For example, "cafe" would match "café".  
  
## BannedPhraseMatchType

The matching method for the banned phrase.

Enums  
---  
`BANNED_PHRASE_MATCH_TYPE_UNSPECIFIED` | Defaults to SIMPLE_STRING_MATCH.  
`SIMPLE_STRING_MATCH` | The banned phrase matches if it is found anywhere in the text as an exact substring.  
`WORD_BOUNDARY_STRING_MATCH` | Banned phrase only matches if the pattern found in the text is surrounded by word delimiters. The phrase itself may still contain word delimiters.  
  
## ModelArmorConfig

Configuration for customer defined Model Armor templates to be used for sanitizing user prompts and assistant responses.

JSON representation  
---  
      
    
    {
      "userPromptTemplate": string,
      "responseTemplate": string,
      "failureMode": enum ([FailureMode](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants#FailureMode))
    }  
  
Fields  
---  
`userPromptTemplate` |  `string` Optional. The resource name of the Model Armor template for sanitizing user prompts. Format: `projects/{project}/locations/{location}/templates/{templateId}`If not specified, no sanitization will be applied to the user prompt.  
`responseTemplate` |  `string` Optional. The resource name of the Model Armor template for sanitizing assistant responses. Format: `projects/{project}/locations/{location}/templates/{templateId}`If not specified, no sanitization will be applied to the assistant response.  
`failureMode` |  `enum (`[FailureMode](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants#FailureMode)`)` Optional. Defines the failure mode for Model Armor sanitization.  
  
## FailureMode

Determines the behavior when Model Armor fails to process a request.

Enums  
---  
`FAILURE_MODE_UNSPECIFIED` | Unspecified failure mode, default behavior is `FAIL_CLOSED`.  
`FAIL_OPEN` | In case of a Model Armor processing failure, the request is allowed to proceed without any changes.  
`FAIL_CLOSED` | In case of a Model Armor processing failure, the request is rejected.  
  
## VertexAiSearchToolConfig

Configuration options for the Vertex AI Search tool that the assistant may use when processing queries.

JSON representation  
---  
      
    
    {
      "llmSystemInstructions": string
    }  
  
Fields  
---  
`llmSystemInstructions  
**(deprecated)**` |  `string` This item is deprecated!Deprecated: Please refrain from using this field. System instructions for answering based on the search results of Vertex AI Search. Note that the answer produced by the search tool may differ from the final answer of the assistant.In general, system instructions are a set of natural language instructions that the model processes before it processes prompts. It tells the model how it should behave and respond to prompts. See <https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/system-instructions>Example: "Use information only from the sources to answer. Also, make sure to nicely format the answer with Markdown."If not specified, the internal default will be used.  
  
## AgentConfig

This item is deprecated!

Deprecated: Please use AgentService instead. Configuration options for the agents that the assistant may call when processing queries.

JSON representation  
---  
      
    
    {
      "id": string,
      "displayName": string,
      "toolDescription": string,
      "icon": {
        object ([Image](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants#Image))
      },
      "authorizations": [
        string
      ],
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "vertexAiSdkAgentConnectionInfo": {
        object ([VertexAiSdkAgentConnectionInfo](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants#VertexAiSdkAgentConnectionInfo))
      },
      "httpAgentConnectionInfo": {
        object ([HttpAgentConnectionInfo](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants#HttpAgentConnectionInfo))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`id` |  `string` Required. A unique, human-readable ID for the agent. Must match the following regular expression: `[a-z][a-zA-Z0-9_-]*`.  
`displayName` |  `string` Required. Display name of the agent used for reference in the assistant.  
`toolDescription` |  `string` Required. The tool description of the agent. This description will be used by the LLM to decide whether the agent is relevant to the user question and the question should be routed to the agent.  
`icon` |  `object (`[Image](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants#Image)`)` Required. The icon that represents the agent on the UI.  
`authorizations[]` |  `string` Optional. Resource names of the required authorizations. If the user is not authorized, the service will return a number of authorization URIs that the user must open in a browser and authorize. Once all authorizations are granted, the user can retry the query, and the authorizations will be forwarded to the agent.Format: `projects/{project}/locations/{location}/authorizations/{authorization}`  
The connection configuration of the agent. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`vertexAiSdkAgentConnectionInfo` |  `object (`[VertexAiSdkAgentConnectionInfo](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants#VertexAiSdkAgentConnectionInfo)`)` Required. Connection information for a Vertex AI SDK agent  
`httpAgentConnectionInfo` |  `object (`[HttpAgentConnectionInfo](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants#HttpAgentConnectionInfo)`)` Required. Connection info for an HTTP agent.  
End of mutually exclusive fields.  
  
## VertexAiSdkAgentConnectionInfo

Connection information for a Vertex AI SDK agent - currently only agents exposed through Reasoning Engines are supported.

JSON representation  
---  
      
    
    {
      "reasoningEngine": string
    }  
  
Fields  
---  
`reasoningEngine` |  `string` Resource name of the reasoning engine exposing the agent. Format: `projects/{project}/locations/{location}/reasoningEngines/{reasoningEngine}`  
  
## HttpAgentConnectionInfo

A agent that is reachable by the assistant via HTTP.

JSON representation  
---  
      
    
    {
      "httpUri": string
    }  
  
Fields  
---  
`httpUri` |  `string` Required. The HTTP address of the agent, e.g. "https://example.com/agent1".  
  
## Image

Represents an image.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "uri": string,
      "content": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
Can be either a URI or the content encoded as a base64 string. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`uri` |  `string` Required. Image URI.  
`content` |  `string` Required. Base64-encoded image file contents.  
End of mutually exclusive fields.  
  
## Methods  
  
---  
  
### `[assist](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants/assist)`

|  Assists the user with a query.  
  
### `[create](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants/create)`

|  Creates an `[Assistant](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants#Assistant)`.  
  
### `[createCachedContent](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants/createCachedContent)`

|  Creates an explicit context cache (Vertex `CachedContent`); its `name` is passed as `cachedContent` on subsequent GenerateContent requests.  
  
### `[delete](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants/delete)`

|  Deletes an `[Assistant](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants#Assistant)`.  
  
### `[deleteCachedContent](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants/deleteCachedContent)`

|  Deletes a context cache created by CreateCachedContent (releases storage before TTL).  
  
### `[generateContent](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants/generateContent)`

|  Generates content from a model on behalf of a first-party Gemini Enterprise client (unary).  
  
### `[get](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants/get)`

|  Gets an `[Assistant](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants#Assistant)`.  
  
### `[list](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants/list)`

|  Lists all `[Assistant](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants#Assistant)`s under an `[Engine](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines#Engine)`.  
  
### `[patch](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants/patch)`

|  Updates an `[Assistant](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants#Assistant)`  
  
### `[predict](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants/predict)`

|  Serves a unary prediction from a model on behalf of a first-party Gemini Enterprise client.  
  
### `[streamAssist](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants/streamAssist)`

|  Assists the user with a query in a streaming fashion.  
  
### `[streamGenerateContent](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants/streamGenerateContent)`

|  Server-streaming variant of GenerateContent.  
  
### `[streamRawPredict](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants/streamRawPredict)`

|  Server-streaming raw prediction, for models that use a raw request/response protocol rather than the generateContent shape.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
