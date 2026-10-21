---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_agent/
title: MCP Tools Reference: ces.googleapis.com \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:30:55.351916+00:00
---

# MCP Tools Reference: ces.googleapis.com  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_agent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  MCP Tools Reference: ces.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `create_agent`

Creates a new agent in the given app.

The following code sample shows how to use `curl` to call the `create_agent` MCP tool. 

Curl Request  
---  
      
    
    curl --location 'https://ces.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "create_agent",
        "arguments": {
          // Provide these details according to the MCP tool specification.
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'  
  
## Input Schema

### CreateAgentRequest

JSON representation  
---  
      
    
    {
      "parent": string,
      "agentId": string,
      "agent": {
        object ([Agent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Agent))
      }
    }  
  
Fields  
---  
`parent` |  `string` Required. The resource name of the app to create an agent in.  
`agentId` |  `string` Optional. The ID to use for the agent, which will become the final component of the agent's resource name. If not provided, a unique ID will be automatically assigned for the agent.  
`agent` |  `object (`[Agent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Agent)`)` Required. The agent to create.  
  
### Agent

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "modelSettings": {
        object ([ModelSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ModelSettings))
      },
      "instruction": string,
      "tools": [
        string
      ],
      "childAgents": [
        string
      ],
      "beforeAgentCallbacks": [
        {
          object ([Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Callback))
        }
      ],
      "afterAgentCallbacks": [
        {
          object ([Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Callback))
        }
      ],
      "beforeModelCallbacks": [
        {
          object ([Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Callback))
        }
      ],
      "afterModelCallbacks": [
        {
          object ([Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Callback))
        }
      ],
      "beforeToolCallbacks": [
        {
          object ([Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Callback))
        }
      ],
      "afterToolCallbacks": [
        {
          object ([Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Callback))
        }
      ],
      "createTime": string,
      "updateTime": string,
      "guardrails": [
        string
      ],
      "etag": string,
      "toolsets": [
        {
          object ([AgentToolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.AgentToolset))
        }
      ],
      "generatedSummary": string,
      "transferRules": [
        {
          object ([TransferRule](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.TransferRule))
        }
      ],
      "validationErrors": [
        string
      ],
    
      // Union field agent_type can be only one of the following:
      "llmAgent": {
        object (LlmAgent)
      },
      "remoteDialogflowAgent": {
        object ([RemoteDialogflowAgent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.RemoteDialogflowAgent))
      },
      "remoteA2aAgent": {
        object ([RemoteA2aAgent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.RemoteA2aAgent))
      }
      // End of list of possible types for union field agent_type.
    }  
  
Fields  
---  
`name` |  `string` Identifier. The unique identifier of the agent. Format: `projects/{project}/locations/{location}/apps/{app}/agents/{agent}`  
`displayName` |  `string` Required. Display name of the agent.  
`description` |  `string` Optional. Human-readable description of the agent.  
`modelSettings` |  `object (`[ModelSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ModelSettings)`)` Optional. Configurations for the LLM model.  
`instruction` |  `string` Optional. Instructions for the LLM model to guide the agent's behavior.  
`tools[]` |  `string` Optional. List of available tools for the agent. Format: `projects/{project}/locations/{location}/apps/{app}/tools/{tool}`  
`childAgents[]` |  `string` Optional. List of child agents in the agent tree. Format: `projects/{project}/locations/{location}/apps/{app}/agents/{agent}`  
`beforeAgentCallbacks[]` |  `object (`[Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Callback)`)` Optional. The callbacks to execute before the agent is called. The provided callbacks are executed sequentially in the exact order they are given in the list. If a callback returns an overridden response, execution stops and any remaining callbacks are skipped.  
`afterAgentCallbacks[]` |  `object (`[Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Callback)`)` Optional. The callbacks to execute after the agent is called. The provided callbacks are executed sequentially in the exact order they are given in the list. If a callback returns an overridden response, execution stops and any remaining callbacks are skipped.  
`beforeModelCallbacks[]` |  `object (`[Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Callback)`)` Optional. The callbacks to execute before the model is called. If there are multiple calls to the model, the callback will be executed multiple times. The provided callbacks are executed sequentially in the exact order they are given in the list. If a callback returns an overridden response, execution stops and any remaining callbacks are skipped.  
`afterModelCallbacks[]` |  `object (`[Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Callback)`)` Optional. The callbacks to execute after the model is called. If there are multiple calls to the model, the callback will be executed multiple times. The provided callbacks are executed sequentially in the exact order they are given in the list. If a callback returns an overridden response, execution stops and any remaining callbacks are skipped.  
`beforeToolCallbacks[]` |  `object (`[Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Callback)`)` Optional. The callbacks to execute before the tool is invoked. If there are multiple tool invocations, the callback will be executed multiple times. The provided callbacks are executed sequentially in the exact order they are given in the list. If a callback returns an overridden response, execution stops and any remaining callbacks are skipped.  
`afterToolCallbacks[]` |  `object (`[Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Callback)`)` Optional. The callbacks to execute after the tool is invoked. If there are multiple tool invocations, the callback will be executed multiple times. The provided callbacks are executed sequentially in the exact order they are given in the list. If a callback returns an overridden response, execution stops and any remaining callbacks are skipped.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the agent was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the agent was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`guardrails[]` |  `string` Optional. List of guardrails for the agent. Format: `projects/{project}/locations/{location}/apps/{app}/guardrails/{guardrail}`  
`etag` |  `string` Etag used to ensure the object hasn't changed during a read-modify-write operation. If the etag is empty, the update will overwrite any concurrent changes.  
`toolsets[]` |  `object (`[AgentToolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.AgentToolset)`)` Optional. List of toolsets for the agent.  
`generatedSummary` |  `string` Output only. If the agent is generated by the LLM assistant, this field contains a descriptive summary of the generation.  
`transferRules[]` |  `object (`[TransferRule](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.TransferRule)`)` Optional. Agent transfer rules. If multiple rules match, the first one in the list will be used.  
`validationErrors[]` |  `string` Output only. Misconfigurations or errors in the agent that may affect agent quality.  
Union field `agent_type`. The type of agent. `agent_type` can be only one of the following:  
`llmAgent` |  `object (`LlmAgent`)` Optional. The default agent type.  
`remoteDialogflowAgent` |  `object (`[RemoteDialogflowAgent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.RemoteDialogflowAgent)`)` Optional. The remote [Dialogflow](https://cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents) agent to be used for the agent execution. If this field is set, all other agent level properties will be ignored.Note: If the Dialogflow agent is in a different project from the app, you should grant `roles/dialogflow.client` to the CES service agent `service-<PROJECT-NUMBER>@gcp-sa-ces.iam.gserviceaccount.com`.  
`remoteA2aAgent` |  `object (`[RemoteA2aAgent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.RemoteA2aAgent)`)` Optional. The remote [A2A](https://github.com/a2aproject/A2A) agent to be used for the agent execution.  
  
### RemoteDialogflowAgent

JSON representation  
---  
      
    
    {
      "agent": string,
      "flowId": string,
      "environmentId": string,
      "inputVariableMapping": {
        string: string,
        ...
      },
      "outputVariableMapping": {
        string: string,
        ...
      },
      "respectResponseInterruptionSettings": boolean,
      "languageCodeVariable": string
    }  
  
Fields  
---  
`agent` |  `string` Required. The [Dialogflow](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent) agent resource name. Format: `projects/{project}/locations/{location}/agents/{agent}`  
`flowId` |  `string` Optional. The flow ID of the flow in the Dialogflow agent.  
`environmentId` |  `string` Optional. The environment ID of the Dialogflow agent to be used for the agent execution. If not specified, the draft environment will be used.  
`inputVariableMapping` |  `map (key: string, value: string)` Optional. The mapping of the app variables names to the Dialogflow session parameters names to be sent to the Dialogflow agent as input.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`outputVariableMapping` |  `map (key: string, value: string)` Optional. The mapping of the Dialogflow session parameters names to the app variables names to be sent back to the CES agent after the Dialogflow agent execution ends.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`respectResponseInterruptionSettings` |  `boolean` Optional. Indicates whether to respect the message-level interruption settings configured in the Dialogflow agent.

  * If false: all response messages from the Dialogflow agent follow the app-level barge-in settings.
  * If true: only response messages with [`allow_playback_interruption`](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#text) set to true will be interruptable, all other messages follow the app-level barge-in settings.

  
`languageCodeVariable` |  `string` Optional. The name of the variable that contains the language code to be used for the Dialogflow session. If unspecified, the default language code of the Dialogflow agent will be used.  
  
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
  
### RemoteA2aAgent

JSON representation  
---  
      
    
    {
      "a2aConfig": {
        object ([RemoteA2aConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.RemoteA2aConfig))
      }
    }  
  
Fields  
---  
`a2aConfig` |  `object (`[RemoteA2aConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.RemoteA2aConfig)`)` Required. The A2A connection configuration.  
  
### RemoteA2aConfig

JSON representation  
---  
      
    
    {
      "apiAuthentication": {
        object ([ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ApiAuthentication))
      },
      "inputVariableMapping": {
        string: string,
        ...
      },
      "outputVariableMapping": {
        string: string,
        ...
      },
      "streamingEnabled": boolean,
      "contextId": string,
    
      // Union field agent_spec can be only one of the following:
      "agentCard": {
        object ([AgentCard](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.AgentCard))
      },
      "agentRegistry": string
      // End of list of possible types for union field agent_spec.
    }  
  
Fields  
---  
`apiAuthentication` |  `object (`[ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ApiAuthentication)`)` Optional. Authentication configuration for calling the remote agent. Optional if the registry reference already handles authentication.  
`inputVariableMapping` |  `map (key: string, value: string)` Optional. Mapping of input variable names of remote agent to GECX variable names.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`outputVariableMapping` |  `map (key: string, value: string)` Optional. Mapping of output variable names of remote agent to GECX variable names.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`streamingEnabled` |  `boolean` Optional. Whether streaming is enabled for the remote agent.  
`contextId` |  `string` Optional. If not empty, interactions with the remote A2A agent will use this context ID. This context_id field can refer to a session variable like `$context.variables.order_agent_session_id`.  
Union field `agent_spec`. Specification of the remote agent. `agent_spec` can be only one of the following:  
`agentCard` |  `object (`[AgentCard](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.AgentCard)`)` Optional. The full agent card defined inline.  
`agentRegistry` |  `string` Optional. Reference to the agent in the Agent Registry. Format: `projects/{project}/locations/{location}/agents/{agent}`  
  
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
  
### Callback

JSON representation  
---  
      
    
    {
      "description": string,
      "disabled": boolean,
      "proactiveExecutionEnabled": boolean,
    
      // Union field callback can be only one of the following:
      "pythonCode": string
      // End of list of possible types for union field callback.
    }  
  
Fields  
---  
`description` |  `string` Optional. Human-readable description of the callback.  
`disabled` |  `boolean` Optional. Whether the callback is disabled. Disabled callbacks are ignored by the agent.  
`proactiveExecutionEnabled` |  `boolean` Optional. If enabled, the callback will also be executed on intermediate model outputs. This setting only affects after model callback. **ENABLE WITH CAUTION**. Typically after model callback only needs to be executed after receiving all model responses. Enabling proactive execution may have negative implication on the execution cost and latency, and should only be enabled in rare situations.  
Union field `callback`. The callback to execute. `callback` can be only one of the following:  
`pythonCode` |  `string` Required. The python code to execute for the callback.  
  
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
  
### AgentToolset

JSON representation  
---  
      
    
    {
      "toolset": string,
      "toolIds": [
        string
      ]
    }  
  
Fields  
---  
`toolset` |  `string` Required. The resource name of the toolset. Format: `projects/{project}/locations/{location}/apps/{app}/toolsets/{toolset}`  
`toolIds[]` |  `string` Optional. The tools IDs to filter the toolset.  
  
### TransferRule

JSON representation  
---  
      
    
    {
      "childAgent": string,
      "direction": enum ([Direction](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Direction)),
    
      // Union field rule_type can be only one of the following:
      "deterministicTransfer": {
        object ([DeterministicTransfer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.DeterministicTransfer))
      },
      "disablePlannerTransfer": {
        object ([DisablePlannerTransfer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.DisablePlannerTransfer))
      }
      // End of list of possible types for union field rule_type.
    }  
  
Fields  
---  
`childAgent` |  `string` Required. The resource name of the child agent the rule applies to. Format: `projects/{project}/locations/{location}/apps/{app}/agents/{agent}`  
`direction` |  `enum (`[Direction](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Direction)`)` Required. The direction of the transfer.  
Union field `rule_type`. The rule type. `rule_type` can be only one of the following:  
`deterministicTransfer` |  `object (`[DeterministicTransfer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.DeterministicTransfer)`)` Optional. A rule that immediately transfers to the target agent when the condition is met.  
`disablePlannerTransfer` |  `object (`[DisablePlannerTransfer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.DisablePlannerTransfer)`)` Optional. Rule that prevents the planner from transferring to the target agent.  
  
### DeterministicTransfer

JSON representation  
---  
      
    
    {
    
      // Union field condition_type can be only one of the following:
      "expressionCondition": {
        object ([ExpressionCondition](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ExpressionCondition))
      },
      "pythonCodeCondition": {
        object ([PythonCodeCondition](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.PythonCodeCondition))
      }
      // End of list of possible types for union field condition_type.
    }  
  
Fields  
---  
Union field `condition_type`. The condition to evaluate. `condition_type` can be only one of the following:  
`expressionCondition` |  `object (`[ExpressionCondition](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ExpressionCondition)`)` Optional. A rule that evaluates a session state condition. If the condition evaluates to true, the transfer occurs.  
`pythonCodeCondition` |  `object (`[PythonCodeCondition](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.PythonCodeCondition)`)` Optional. A rule that uses Python code block to evaluate the conditions. If the condition evaluates to true, the transfer occurs.  
  
### ExpressionCondition

JSON representation  
---  
      
    
    {
      "expression": string
    }  
  
Fields  
---  
`expression` |  `string` Required. The string representation of cloud.api.Expression condition.  
  
### PythonCodeCondition

JSON representation  
---  
      
    
    {
      "pythonCode": string
    }  
  
Fields  
---  
`pythonCode` |  `string` Required. The python code to execute.  
  
### DisablePlannerTransfer

JSON representation  
---  
      
    
    {
      "expressionCondition": {
        object ([ExpressionCondition](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ExpressionCondition))
      }
    }  
  
Fields  
---  
`expressionCondition` |  `object (`[ExpressionCondition](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ExpressionCondition)`)` Required. If the condition evaluates to true, planner will not be allowed to transfer to the target agent.  
  
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
  
### ThinkingLevel

Thinking level configuration for the model.

Enums  
---  
`THINKING_LEVEL_UNSPECIFIED` | Thinking level is unspecified.  
`DEFAULT` | Default thinking level.  
`LOW` | Low thinking level.  
`MEDIUM` | Medium thinking level.  
`HIGH` | High thinking level.  
  
### Direction

The direction of the transfer.

Enums  
---  
`DIRECTION_UNSPECIFIED` | Unspecified direction.  
`PARENT_TO_CHILD` | Transfer from the parent agent to the child agent.  
`CHILD_TO_PARENT` | Transfer from the child agent to the parent agent.  
  
## Output Schema

An agent acts as the fundamental building block that provides instructions to the Large Language Model (LLM) for executing specific tasks.

### Agent

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "modelSettings": {
        object ([ModelSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ModelSettings))
      },
      "instruction": string,
      "tools": [
        string
      ],
      "childAgents": [
        string
      ],
      "beforeAgentCallbacks": [
        {
          object ([Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Callback))
        }
      ],
      "afterAgentCallbacks": [
        {
          object ([Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Callback))
        }
      ],
      "beforeModelCallbacks": [
        {
          object ([Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Callback))
        }
      ],
      "afterModelCallbacks": [
        {
          object ([Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Callback))
        }
      ],
      "beforeToolCallbacks": [
        {
          object ([Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Callback))
        }
      ],
      "afterToolCallbacks": [
        {
          object ([Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Callback))
        }
      ],
      "createTime": string,
      "updateTime": string,
      "guardrails": [
        string
      ],
      "etag": string,
      "toolsets": [
        {
          object ([AgentToolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.AgentToolset))
        }
      ],
      "generatedSummary": string,
      "transferRules": [
        {
          object ([TransferRule](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.TransferRule))
        }
      ],
      "validationErrors": [
        string
      ],
    
      // Union field agent_type can be only one of the following:
      "llmAgent": {
        object (LlmAgent)
      },
      "remoteDialogflowAgent": {
        object ([RemoteDialogflowAgent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.RemoteDialogflowAgent))
      },
      "remoteA2aAgent": {
        object ([RemoteA2aAgent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.RemoteA2aAgent))
      }
      // End of list of possible types for union field agent_type.
    }  
  
Fields  
---  
`name` |  `string` Identifier. The unique identifier of the agent. Format: `projects/{project}/locations/{location}/apps/{app}/agents/{agent}`  
`displayName` |  `string` Required. Display name of the agent.  
`description` |  `string` Optional. Human-readable description of the agent.  
`modelSettings` |  `object (`[ModelSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ModelSettings)`)` Optional. Configurations for the LLM model.  
`instruction` |  `string` Optional. Instructions for the LLM model to guide the agent's behavior.  
`tools[]` |  `string` Optional. List of available tools for the agent. Format: `projects/{project}/locations/{location}/apps/{app}/tools/{tool}`  
`childAgents[]` |  `string` Optional. List of child agents in the agent tree. Format: `projects/{project}/locations/{location}/apps/{app}/agents/{agent}`  
`beforeAgentCallbacks[]` |  `object (`[Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Callback)`)` Optional. The callbacks to execute before the agent is called. The provided callbacks are executed sequentially in the exact order they are given in the list. If a callback returns an overridden response, execution stops and any remaining callbacks are skipped.  
`afterAgentCallbacks[]` |  `object (`[Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Callback)`)` Optional. The callbacks to execute after the agent is called. The provided callbacks are executed sequentially in the exact order they are given in the list. If a callback returns an overridden response, execution stops and any remaining callbacks are skipped.  
`beforeModelCallbacks[]` |  `object (`[Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Callback)`)` Optional. The callbacks to execute before the model is called. If there are multiple calls to the model, the callback will be executed multiple times. The provided callbacks are executed sequentially in the exact order they are given in the list. If a callback returns an overridden response, execution stops and any remaining callbacks are skipped.  
`afterModelCallbacks[]` |  `object (`[Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Callback)`)` Optional. The callbacks to execute after the model is called. If there are multiple calls to the model, the callback will be executed multiple times. The provided callbacks are executed sequentially in the exact order they are given in the list. If a callback returns an overridden response, execution stops and any remaining callbacks are skipped.  
`beforeToolCallbacks[]` |  `object (`[Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Callback)`)` Optional. The callbacks to execute before the tool is invoked. If there are multiple tool invocations, the callback will be executed multiple times. The provided callbacks are executed sequentially in the exact order they are given in the list. If a callback returns an overridden response, execution stops and any remaining callbacks are skipped.  
`afterToolCallbacks[]` |  `object (`[Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Callback)`)` Optional. The callbacks to execute after the tool is invoked. If there are multiple tool invocations, the callback will be executed multiple times. The provided callbacks are executed sequentially in the exact order they are given in the list. If a callback returns an overridden response, execution stops and any remaining callbacks are skipped.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the agent was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the agent was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`guardrails[]` |  `string` Optional. List of guardrails for the agent. Format: `projects/{project}/locations/{location}/apps/{app}/guardrails/{guardrail}`  
`etag` |  `string` Etag used to ensure the object hasn't changed during a read-modify-write operation. If the etag is empty, the update will overwrite any concurrent changes.  
`toolsets[]` |  `object (`[AgentToolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.AgentToolset)`)` Optional. List of toolsets for the agent.  
`generatedSummary` |  `string` Output only. If the agent is generated by the LLM assistant, this field contains a descriptive summary of the generation.  
`transferRules[]` |  `object (`[TransferRule](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.TransferRule)`)` Optional. Agent transfer rules. If multiple rules match, the first one in the list will be used.  
`validationErrors[]` |  `string` Output only. Misconfigurations or errors in the agent that may affect agent quality.  
Union field `agent_type`. The type of agent. `agent_type` can be only one of the following:  
`llmAgent` |  `object (`LlmAgent`)` Optional. The default agent type.  
`remoteDialogflowAgent` |  `object (`[RemoteDialogflowAgent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.RemoteDialogflowAgent)`)` Optional. The remote [Dialogflow](https://cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents) agent to be used for the agent execution. If this field is set, all other agent level properties will be ignored.Note: If the Dialogflow agent is in a different project from the app, you should grant `roles/dialogflow.client` to the CES service agent `service-<PROJECT-NUMBER>@gcp-sa-ces.iam.gserviceaccount.com`.  
`remoteA2aAgent` |  `object (`[RemoteA2aAgent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.RemoteA2aAgent)`)` Optional. The remote [A2A](https://github.com/a2aproject/A2A) agent to be used for the agent execution.  
  
### RemoteDialogflowAgent

JSON representation  
---  
      
    
    {
      "agent": string,
      "flowId": string,
      "environmentId": string,
      "inputVariableMapping": {
        string: string,
        ...
      },
      "outputVariableMapping": {
        string: string,
        ...
      },
      "respectResponseInterruptionSettings": boolean,
      "languageCodeVariable": string
    }  
  
Fields  
---  
`agent` |  `string` Required. The [Dialogflow](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent) agent resource name. Format: `projects/{project}/locations/{location}/agents/{agent}`  
`flowId` |  `string` Optional. The flow ID of the flow in the Dialogflow agent.  
`environmentId` |  `string` Optional. The environment ID of the Dialogflow agent to be used for the agent execution. If not specified, the draft environment will be used.  
`inputVariableMapping` |  `map (key: string, value: string)` Optional. The mapping of the app variables names to the Dialogflow session parameters names to be sent to the Dialogflow agent as input.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`outputVariableMapping` |  `map (key: string, value: string)` Optional. The mapping of the Dialogflow session parameters names to the app variables names to be sent back to the CES agent after the Dialogflow agent execution ends.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`respectResponseInterruptionSettings` |  `boolean` Optional. Indicates whether to respect the message-level interruption settings configured in the Dialogflow agent.

  * If false: all response messages from the Dialogflow agent follow the app-level barge-in settings.
  * If true: only response messages with [`allow_playback_interruption`](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#text) set to true will be interruptable, all other messages follow the app-level barge-in settings.

  
`languageCodeVariable` |  `string` Optional. The name of the variable that contains the language code to be used for the Dialogflow session. If unspecified, the default language code of the Dialogflow agent will be used.  
  
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
  
### RemoteA2aAgent

JSON representation  
---  
      
    
    {
      "a2aConfig": {
        object ([RemoteA2aConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.RemoteA2aConfig))
      }
    }  
  
Fields  
---  
`a2aConfig` |  `object (`[RemoteA2aConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.RemoteA2aConfig)`)` Required. The A2A connection configuration.  
  
### RemoteA2aConfig

JSON representation  
---  
      
    
    {
      "apiAuthentication": {
        object ([ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ApiAuthentication))
      },
      "inputVariableMapping": {
        string: string,
        ...
      },
      "outputVariableMapping": {
        string: string,
        ...
      },
      "streamingEnabled": boolean,
      "contextId": string,
    
      // Union field agent_spec can be only one of the following:
      "agentCard": {
        object ([AgentCard](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.AgentCard))
      },
      "agentRegistry": string
      // End of list of possible types for union field agent_spec.
    }  
  
Fields  
---  
`apiAuthentication` |  `object (`[ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ApiAuthentication)`)` Optional. Authentication configuration for calling the remote agent. Optional if the registry reference already handles authentication.  
`inputVariableMapping` |  `map (key: string, value: string)` Optional. Mapping of input variable names of remote agent to GECX variable names.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`outputVariableMapping` |  `map (key: string, value: string)` Optional. Mapping of output variable names of remote agent to GECX variable names.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`streamingEnabled` |  `boolean` Optional. Whether streaming is enabled for the remote agent.  
`contextId` |  `string` Optional. If not empty, interactions with the remote A2A agent will use this context ID. This context_id field can refer to a session variable like `$context.variables.order_agent_session_id`.  
Union field `agent_spec`. Specification of the remote agent. `agent_spec` can be only one of the following:  
`agentCard` |  `object (`[AgentCard](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.AgentCard)`)` Optional. The full agent card defined inline.  
`agentRegistry` |  `string` Optional. Reference to the agent in the Agent Registry. Format: `projects/{project}/locations/{location}/agents/{agent}`  
  
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
  
### Callback

JSON representation  
---  
      
    
    {
      "description": string,
      "disabled": boolean,
      "proactiveExecutionEnabled": boolean,
    
      // Union field callback can be only one of the following:
      "pythonCode": string
      // End of list of possible types for union field callback.
    }  
  
Fields  
---  
`description` |  `string` Optional. Human-readable description of the callback.  
`disabled` |  `boolean` Optional. Whether the callback is disabled. Disabled callbacks are ignored by the agent.  
`proactiveExecutionEnabled` |  `boolean` Optional. If enabled, the callback will also be executed on intermediate model outputs. This setting only affects after model callback. **ENABLE WITH CAUTION**. Typically after model callback only needs to be executed after receiving all model responses. Enabling proactive execution may have negative implication on the execution cost and latency, and should only be enabled in rare situations.  
Union field `callback`. The callback to execute. `callback` can be only one of the following:  
`pythonCode` |  `string` Required. The python code to execute for the callback.  
  
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
  
### AgentToolset

JSON representation  
---  
      
    
    {
      "toolset": string,
      "toolIds": [
        string
      ]
    }  
  
Fields  
---  
`toolset` |  `string` Required. The resource name of the toolset. Format: `projects/{project}/locations/{location}/apps/{app}/toolsets/{toolset}`  
`toolIds[]` |  `string` Optional. The tools IDs to filter the toolset.  
  
### TransferRule

JSON representation  
---  
      
    
    {
      "childAgent": string,
      "direction": enum ([Direction](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Direction)),
    
      // Union field rule_type can be only one of the following:
      "deterministicTransfer": {
        object ([DeterministicTransfer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.DeterministicTransfer))
      },
      "disablePlannerTransfer": {
        object ([DisablePlannerTransfer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.DisablePlannerTransfer))
      }
      // End of list of possible types for union field rule_type.
    }  
  
Fields  
---  
`childAgent` |  `string` Required. The resource name of the child agent the rule applies to. Format: `projects/{project}/locations/{location}/apps/{app}/agents/{agent}`  
`direction` |  `enum (`[Direction](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Direction)`)` Required. The direction of the transfer.  
Union field `rule_type`. The rule type. `rule_type` can be only one of the following:  
`deterministicTransfer` |  `object (`[DeterministicTransfer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.DeterministicTransfer)`)` Optional. A rule that immediately transfers to the target agent when the condition is met.  
`disablePlannerTransfer` |  `object (`[DisablePlannerTransfer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.DisablePlannerTransfer)`)` Optional. Rule that prevents the planner from transferring to the target agent.  
  
### DeterministicTransfer

JSON representation  
---  
      
    
    {
    
      // Union field condition_type can be only one of the following:
      "expressionCondition": {
        object ([ExpressionCondition](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ExpressionCondition))
      },
      "pythonCodeCondition": {
        object ([PythonCodeCondition](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.PythonCodeCondition))
      }
      // End of list of possible types for union field condition_type.
    }  
  
Fields  
---  
Union field `condition_type`. The condition to evaluate. `condition_type` can be only one of the following:  
`expressionCondition` |  `object (`[ExpressionCondition](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ExpressionCondition)`)` Optional. A rule that evaluates a session state condition. If the condition evaluates to true, the transfer occurs.  
`pythonCodeCondition` |  `object (`[PythonCodeCondition](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.PythonCodeCondition)`)` Optional. A rule that uses Python code block to evaluate the conditions. If the condition evaluates to true, the transfer occurs.  
  
### ExpressionCondition

JSON representation  
---  
      
    
    {
      "expression": string
    }  
  
Fields  
---  
`expression` |  `string` Required. The string representation of cloud.api.Expression condition.  
  
### PythonCodeCondition

JSON representation  
---  
      
    
    {
      "pythonCode": string
    }  
  
Fields  
---  
`pythonCode` |  `string` Required. The python code to execute.  
  
### DisablePlannerTransfer

JSON representation  
---  
      
    
    {
      "expressionCondition": {
        object ([ExpressionCondition](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ExpressionCondition))
      }
    }  
  
Fields  
---  
`expressionCondition` |  `object (`[ExpressionCondition](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ExpressionCondition)`)` Required. If the condition evaluates to true, planner will not be allowed to transfer to the target agent.  
  
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
  
### ThinkingLevel

Thinking level configuration for the model.

Enums  
---  
`THINKING_LEVEL_UNSPECIFIED` | Thinking level is unspecified.  
`DEFAULT` | Default thinking level.  
`LOW` | Low thinking level.  
`MEDIUM` | Medium thinking level.  
`HIGH` | High thinking level.  
  
### Direction

The direction of the transfer.

Enums  
---  
`DIRECTION_UNSPECIFIED` | Unspecified direction.  
`PARENT_TO_CHILD` | Transfer from the parent agent to the child agent.  
`CHILD_TO_PARENT` | Transfer from the child agent to the parent agent.  
  
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
