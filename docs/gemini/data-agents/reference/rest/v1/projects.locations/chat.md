---
url: https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/chat/
title: Method: projects.locations.chat \u00a0|\u00a0 Data Agents \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:35:35.408194+00:00
---

# Method: projects.locations.chat  |  Data Agents  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/chat/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)
  * [ Reference ](https://docs.cloud.google.com/gemini/data-agents/reference/rest)



Send feedback 

#  Method: projects.locations.chat Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * ConversationReference
    * JSON representation
  * DataAgentContext
    * JSON representation
  * ContextVersion
  * ClientManagedResourceContext
    * JSON representation
  * LookerSettings
    * JSON representation
  * Credentials
    * JSON representation
  * OAuthCredentials
    * JSON representation
  * SecretBased
    * JSON representation
  * TokenBased
    * JSON representation
  * ThinkingMode
  * Model



Answers a data question by generating a stream of `[Message](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/Message)` objects.

### HTTP request

`POST https://geminidataanalytics.googleapis.com/v1/{parent=projects/*/locations/*}:chat`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent value for chat request. Pattern: `projects/{project}/locations/{location}`  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "messages": [
        {
          object ([Message](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/Message))
        }
      ],
      "credentials": {
        object ([Credentials](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/chat#Credentials))
      },
      "thinkingMode": enum ([ThinkingMode](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/chat#ThinkingMode)),
      "model": enum ([Model](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/chat#Model)),
    
      // Union field context_provider can be only one of the following:
      "inlineContext": {
        object ([Context](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.dataAgents#Context))
      },
      "conversationReference": {
        object ([ConversationReference](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/chat#ConversationReference))
      },
      "dataAgentContext": {
        object ([DataAgentContext](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/chat#DataAgentContext))
      },
      "clientManagedResourceContext": {
        object ([ClientManagedResourceContext](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/chat#ClientManagedResourceContext))
      }
      // End of list of possible types for union field context_provider.
    
      // Union field datasource_settings can be only one of the following:
      "lookerSettings": {
        object ([LookerSettings](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/chat#LookerSettings))
      }
      // End of list of possible types for union field datasource_settings.
    }  
  
Fields  
---  
`messages[]` |  `object (`[Message](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/Message)`)` Required. Content of current conversation.  
`credentials` |  `object (`[Credentials](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/chat#Credentials)`)` Optional. The credentials to use when calling the data source(s) specified in the context.This field can be used to provide credentials for various data sources. For example, when connecting to Looker, it currently supports both OAuth token and API key-based credentials, as described in [Authentication with an SDK](https://cloud.google.com/looker/docs/api-auth#authentication_with_an_sdk).  
`thinkingMode` |  `enum (`[ThinkingMode](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/chat#ThinkingMode)`)` Optional. The thinking mode to use for the agent loop. Defaults to THINKING_MODE_UNSPECIFIED if not specified.  
`model` |  `enum (`[Model](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/chat#Model)`)` Optional. The model to use for the agent loop when processing the request. This setting only has an effect when context.options.model is not set.  
Union field `context_provider`. Context Provider for the chat request. It can either be - inline_context, which is a context provided inline in the request. data_agent, which is a reference to a data agent resource. conversation_reference, which is a reference to a persisted conversation and context using conversation_id and agent_id. `context_provider` can be only one of the following:  
`inlineContext` |  `object (`[Context](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.dataAgents#Context)`)` Optional. Inline context for the chat request. Use this to chat statelessly (without managed conversation persistence and without an Agent) by passing all context inline.  
`conversationReference` |  `object (`[ConversationReference](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/chat#ConversationReference)`)` Optional. Reference to a persisted conversation and agent context. Use this to chat with an Agent using managed conversation persistence.  
`dataAgentContext` |  `object (`[DataAgentContext](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/chat#DataAgentContext)`)` Optional. Context for the chat request. Use this to chat with an Agent statelessly, without managed conversation persistence.  
`clientManagedResourceContext` |  `object (`[ClientManagedResourceContext](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/chat#ClientManagedResourceContext)`)` Optional. Context with client managed resources. Some clients may not use GDA managed resources including conversations and agents, instead they create and manage their own conversations and agents resources.  
Union field `datasource_settings`. Optional settings to customize request behavior, specific to the target datasource. `datasource_settings` can be only one of the following:  
`lookerSettings` |  `object (`[LookerSettings](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/chat#LookerSettings)`)` Optional. Looker specific settings.  
  
### Response body

If successful, the response body contains a stream of `[Message](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/Message)` instances.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## ConversationReference

Reference to a persisted conversation and agent context.

JSON representation  
---  
      
    
    {
      "conversation": string,
      "dataAgentContext": {
        object ([DataAgentContext](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/chat#DataAgentContext))
      }
    }  
  
Fields  
---  
`conversation` |  `string` Required. Name of the conversation resource. Format: `projects/{project}/locations/{location}/conversations/{conversationId}`  
`dataAgentContext` |  `object (`[DataAgentContext](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/chat#DataAgentContext)`)` Required. Context for the chat request using a data agent.  
  
## DataAgentContext

Context for the chat request using a data agent.

JSON representation  
---  
      
    
    {
      "dataAgent": string,
      "contextVersion": enum ([ContextVersion](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/chat#ContextVersion))
    }  
  
Fields  
---  
`dataAgent` |  `string` Required. The name of the data agent resource.  
`contextVersion` |  `enum (`[ContextVersion](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/chat#ContextVersion)`)` Optional. Version of context to be used by DCS (e.g. STAGING, PUBLISHED)  
  
## ContextVersion

List of context versions supported by DCS. There are two versions of context. This is to maintain versioning for the data agent.

Enums  
---  
`CONTEXT_VERSION_UNSPECIFIED` | Unspecified or unrecognized.  
`STAGING` | Using this version, DCS will use the latest staging context for the data agent.  
`PUBLISHED` | Using this version, DCS will use the latest published context for the data agent.  
  
## ClientManagedResourceContext

Context with client managed resources. Some clients may not use GDA managed resources including conversations and agents, instead they create and manage their own conversations and agents resources.

JSON representation  
---  
      
    
    {
      "inlineContext": {
        object ([Context](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.dataAgents#Context))
      },
      "conversationId": string,
      "agentId": string
    }  
  
Fields  
---  
`inlineContext` |  `object (`[Context](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.dataAgents#Context)`)` Required. Context for the chat request. Use this to chat without GDA API managed conversation and agent persistence by passing all context inline.  
`conversationId` |  `string` Optional. The client managed conversation id.  
`agentId` |  `string` Optional. The client managed agent id.  
  
## LookerSettings

Message to hold Looker specific custom settings.

JSON representation  
---  
      
    
    {
      "enableDevMode": boolean
    }  
  
Fields  
---  
`enableDevMode` |  `boolean` Optional. Whether to operate in Looker's Development Mode. If true, the API session will be switched to the "dev" workspace, allowing interaction with LookML changes in the user's development branch. If false or unset, the session remains in the default state (Production Mode). See <https://cloud.google.com/looker/docs/dev-mode-prod-mode>.  
  
## Credentials

Represents different forms of credential specification.

JSON representation  
---  
      
    
    {
    
      // Union field kind can be only one of the following:
      "oauth": {
        object ([OAuthCredentials](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/chat#OAuthCredentials))
      }
      // End of list of possible types for union field kind.
    }  
  
Fields  
---  
Union field `kind`. The kind of credentials. `kind` can be only one of the following:  
`oauth` |  `object (`[OAuthCredentials](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/chat#OAuthCredentials)`)` OAuth credentials.  
  
## OAuthCredentials

Represents OAuth credentials.

JSON representation  
---  
      
    
    {
    
      // Union field kind can be only one of the following:
      "secret": {
        object ([SecretBased](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/chat#SecretBased))
      },
      "token": {
        object ([TokenBased](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/chat#TokenBased))
      }
      // End of list of possible types for union field kind.
    }  
  
Fields  
---  
Union field `kind`. The kind of OAuth credentials. `kind` can be only one of the following:  
`secret` |  `object (`[SecretBased](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/chat#SecretBased)`)` Secret-based OAuth credentials.  
`token` |  `object (`[TokenBased](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/chat#TokenBased)`)` Token-based OAuth credentials.  
  
## SecretBased

The name of the secret containing the access token. Represents secret-based OAuth credentials.

JSON representation  
---  
      
    
    {
      "clientId": string,
      "clientSecret": string
    }  
  
Fields  
---  
`clientId` |  `string` Required. An OAuth client ID.  
`clientSecret` |  `string` Required. An OAuth client secret.  
  
## TokenBased

Read more about Looker access tokens here: <https://developers.looker.com/api/advanced-usage/looker-api-oauth>

JSON representation  
---  
      
    
    {
      "accessToken": string
    }  
  
Fields  
---  
`accessToken` |  `string` Required. The name of the secret containing the access token.  
  
## ThinkingMode

Mode of thinking for the agent.

Enums  
---  
`THINKING_MODE_UNSPECIFIED` | Unspecified thinking mode, agent will use THINKING mode by default except for BigQuery user defaulting to FAST mode by default.  
`FAST` | Fast mode, answers quickly.  
`THINKING` | Thinking mode, solves complex problems.  
  
## Model

Model selection for the agent for BigQuery users.

Enums  
---  
`MODEL_UNSPECIFIED` | No model specified. Either preview or non preview model can be used.  
`LATEST_GA_MODEL` | Use the most up-to-date non-preview model. This may constrain certain request level settings.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
