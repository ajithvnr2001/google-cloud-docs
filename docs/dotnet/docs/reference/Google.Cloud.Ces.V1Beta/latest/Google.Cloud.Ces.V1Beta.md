---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta
title: Gemini Enterprise for Customer Experience v1beta API - Namespace Google.Cloud.Ces.V1Beta (1.0.0-beta09) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:39:42.477998+00:00
---

# Gemini Enterprise for Customer Experience v1beta API - Namespace Google.Cloud.Ces.V1Beta (1.0.0-beta09)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Gemini Enterprise for Customer Experience v1beta API - Namespace Google.Cloud.Ces.V1Beta (1.0.0-beta09) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta09 (latest)  1.0.0-beta08 

## Classes 

### [Action](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Action)

Configuration of an Action for the tool to use. Note: This can be either an Action or an Operation. See <https://cloud.google.com/integration-connectors/docs/entities-operation-action> for details.

### [Action.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Action.Types)

Container for nested types declared in the Action message type.

### [Action.Types.EntityOperation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Action.Types.EntityOperation)

Entity CRUD operation specification.

### [Action.Types.EntityOperation.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Action.Types.EntityOperation.Types)

Container for nested types declared in the EntityOperation message type.

### [Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent)

An agent acts as the fundamental building block that provides instructions to the Large Language Model (LLM) for executing specific tasks.

### [Agent.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent.Types)

Container for nested types declared in the Agent message type.

### [Agent.Types.AgentToolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent.Types.AgentToolset)

A toolset with a selection of its tools.

### [Agent.Types.LlmAgent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent.Types.LlmAgent)

Default agent type. The agent uses instructions and callbacks specified in the agent to perform the task using a large language model.

### [Agent.Types.RemoteDialogflowAgent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent.Types.RemoteDialogflowAgent)

The agent which will transfer execution to a remote [Dialogflow CX](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent) agent. The Dialogflow agent will process subsequent user queries until the session ends or flow ends, and the control is transferred back to the parent CES agent.

### [AgentCard](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AgentCard)

AgentCard conveys key information about a remote agent. It is a trimmed version of the AgentCard defined in the A2A protocol <https://a2a-protocol.org/dev/specification/#441-agentcard>

### [AgentInterface](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AgentInterface)

Declares a combination of a target URL, transport and protocol version for interacting with the agent. This allows agents to expose the same functionality over multiple protocol binding mechanisms.

### [AgentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AgentName)

Resource name for the `Agent` resource.

### [AgentService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AgentService)

The service that manages agent-related resources in Gemini Enterprise for Customer Engagement (CES).

### [AgentService.AgentServiceBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AgentService.AgentServiceBase)

Base class for server-side implementations of AgentService

### [AgentService.AgentServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AgentService.AgentServiceClient)

Client for AgentService

### [AgentServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AgentServiceClient)

AgentService client wrapper, for convenient use.

### [AgentServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AgentServiceClientBuilder)

Builder class for [AgentServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AgentServiceClient) to provide simple configuration of credentials, endpoint etc.

### [AgentServiceClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AgentServiceClientImpl)

AgentService client wrapper implementation, for convenient use.

### [AgentServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AgentServiceSettings)

Settings for [AgentServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AgentServiceClient) instances.

### [AgentSkill](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AgentSkill)

Represents a distinct capability or function that an agent can perform.

### [AgentTool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AgentTool)

Represents a tool that allows the agent to call another agent.

### [AgentTransfer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AgentTransfer)

Represents an event indicating the transfer of a conversation to a different agent.

### [AggregatedMetrics](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AggregatedMetrics)

Aggregated metrics for an evaluation or evaluation dataset.

### [AggregatedMetrics.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AggregatedMetrics.Types)

Container for nested types declared in the AggregatedMetrics message type.

### [AggregatedMetrics.Types.HallucinationMetrics](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AggregatedMetrics.Types.HallucinationMetrics)

Metrics for hallucination results.

### [AggregatedMetrics.Types.MetricsByAppVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AggregatedMetrics.Types.MetricsByAppVersion)

Metrics aggregated per app version.

### [AggregatedMetrics.Types.MetricsByTurn](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AggregatedMetrics.Types.MetricsByTurn)

Metrics aggregated per turn.

### [AggregatedMetrics.Types.SemanticSimilarityMetrics](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AggregatedMetrics.Types.SemanticSimilarityMetrics)

Metrics for semantic similarity results.

### [AggregatedMetrics.Types.ToolCallLatencyMetrics](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AggregatedMetrics.Types.ToolCallLatencyMetrics)

Metrics for tool call latency.

### [AggregatedMetrics.Types.ToolMetrics](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AggregatedMetrics.Types.ToolMetrics)

Metrics for a single tool.

### [AggregatedMetrics.Types.TurnLatencyMetrics](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AggregatedMetrics.Types.TurnLatencyMetrics)

Metrics for turn latency.

### [AmbientSoundConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AmbientSoundConfig)

Configuration for the ambient sound to be played with the synthesized agent response, to enhance the naturalness of the conversation.

### [AmbientSoundConfig.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AmbientSoundConfig.Types)

Container for nested types declared in the AmbientSoundConfig message type.

### [ApiAuthentication](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ApiAuthentication)

Authentication information required for API calls.

### [ApiKeyConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ApiKeyConfig)

Configurations for authentication with API key.

### [ApiKeyConfig.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ApiKeyConfig.Types)

Container for nested types declared in the ApiKeyConfig message type.

### [App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)

An app serves as a top-level container for a group of agents, including the root agent and its sub-agents, along with their associated configurations. These agents work together to achieve specific goals within the app's context.

### [App.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App.Types)

Container for nested types declared in the App message type.

### [App.Types.VariableDeclaration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App.Types.VariableDeclaration)

Defines the structure and metadata for a variable.

### [AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)

Resource name for the `App` resource.

### [AppSnapshot](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppSnapshot)

A snapshot of the app.

### [AppVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersion)

In Customer Engagement Suite (CES), an app version is a snapshot of the app at a specific point in time. It is immutable and cannot be modified once created.

### [AppVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersionName)

Resource name for the `AppVersion` resource.

### [AudioProcessingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AudioProcessingConfig)

Configuration for how the input and output audio should be processed and delivered.

### [AudioRecordingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AudioRecordingConfig)

Configuration for how the audio interactions should be recorded.

### [BargeInConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.BargeInConfig)

Configuration for how the user barge-in activities should be handled.

### [BatchDeleteConversationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.BatchDeleteConversationsRequest)

Request message for [AgentService.BatchDeleteConversations][google.cloud.ces.v1beta.AgentService.BatchDeleteConversations].

### [BatchDeleteConversationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.BatchDeleteConversationsResponse)

Response message for [AgentService.BatchDeleteConversations][google.cloud.ces.v1beta.AgentService.BatchDeleteConversations].

### [BearerTokenConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.BearerTokenConfig)

Configurations for authentication with a bearer token.

### [BidiSessionClientMessage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.BidiSessionClientMessage)

The top-level message sent by the client for the [SessionService.BidiRunSession][google.cloud.ces.v1beta.SessionService.BidiRunSession] method.

### [BidiSessionServerMessage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.BidiSessionServerMessage)

The top-level message returned from [SessionService.BidiRunSession][google.cloud.ces.v1beta.SessionService.BidiRunSession] method.

### [BigQueryExportSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.BigQueryExportSettings)

Settings to describe the BigQuery export behaviors for the app.

### [Blob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Blob)

Represents a blob input or output in the conversation.

### [Callback](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Callback)

A callback defines the custom logic to be executed at various stages of agent interaction.

### [Changelog](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Changelog)

Changelogs represent a change made to the app or to an resource within the app.

### [ChangelogName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ChangelogName)

Resource name for the `Changelog` resource.

### [ChannelProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ChannelProfile)

A ChannelProfile configures the agent's behavior for a specific communication channel, such as web UI or telephony.

### [ChannelProfile.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ChannelProfile.Types)

Container for nested types declared in the ChannelProfile message type.

### [ChannelProfile.Types.InstagramConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ChannelProfile.Types.InstagramConfig)

Configuration specific to Instagram deployments.

### [ChannelProfile.Types.PersonaProperty](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ChannelProfile.Types.PersonaProperty)

Represents the persona property of a channel.

### [ChannelProfile.Types.PersonaProperty.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ChannelProfile.Types.PersonaProperty.Types)

Container for nested types declared in the PersonaProperty message type.

### [ChannelProfile.Types.WebWidgetConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ChannelProfile.Types.WebWidgetConfig)

Message for configuration for the web widget.

### [ChannelProfile.Types.WebWidgetConfig.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ChannelProfile.Types.WebWidgetConfig.Types)

Container for nested types declared in the WebWidgetConfig message type.

### [ChannelProfile.Types.WebWidgetConfig.Types.SecuritySettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ChannelProfile.Types.WebWidgetConfig.Types.SecuritySettings)

Security settings for the web widget.

### [ChannelProfile.Types.WhatsAppConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ChannelProfile.Types.WhatsAppConfig)

Configuration specific to WhatsApp deployments.

### [Chunk](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Chunk)

A chunk of content within a message.

### [Citations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Citations)

Citations associated with the agent response.

### [Citations.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Citations.Types)

Container for nested types declared in the Citations message type.

### [Citations.Types.CitedChunk](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Citations.Types.CitedChunk)

Piece of cited information.

### [ClientCertificateSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ClientCertificateSettings)

Settings for custom client certificates.

### [ClientFunction](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ClientFunction)

Represents a client-side function that the agent can invoke. When the tool is chosen by the agent, control is handed off to the client. The client is responsible for executing the function and returning the result as a [ToolResponse][google.cloud.ces.v1beta.ToolResponse] to continue the interaction with the agent.

### [CloudLoggingSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CloudLoggingSettings)

Settings to describe the Cloud Logging behaviors for the app.

### [CodeBlock](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CodeBlock)

A code block to be executed instead of a real tool call.

### [ConnectorTool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ConnectorTool)

A ConnectorTool allows connections to different integrations. See: <https://cloud.google.com/integration-connectors/docs/overview>.

### [ConnectorToolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ConnectorToolset)

A toolset that generates tools from an Integration Connectors Connection.

### [Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Conversation)

A conversation represents an interaction between an end user and the CES app.

### [Conversation.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Conversation.Types)

Container for nested types declared in the Conversation message type.

### [Conversation.Types.Turn](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Conversation.Types.Turn)

All information about a single turn in the conversation.

### [ConversationLoggingSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ConversationLoggingSettings)

Settings to describe the conversation logging behaviors for the app.

### [ConversationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ConversationName)

Resource name for the `Conversation` resource.

### [CreateAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateAgentRequest)

Request message for [AgentService.CreateAgent][google.cloud.ces.v1beta.AgentService.CreateAgent].

### [CreateAppRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateAppRequest)

Request message for [AgentService.CreateApp][google.cloud.ces.v1beta.AgentService.CreateApp].

### [CreateAppVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateAppVersionRequest)

Request message for [AgentService.CreateAppVersion][google.cloud.ces.v1beta.AgentService.CreateAppVersion]

### [CreateDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateDeploymentRequest)

Request message for [AgentService.CreateDeployment][google.cloud.ces.v1beta.AgentService.CreateDeployment].

### [CreateEvaluationDatasetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateEvaluationDatasetRequest)

Request message for [EvaluationService.CreateEvaluationDataset][google.cloud.ces.v1beta.EvaluationService.CreateEvaluationDataset].

### [CreateEvaluationExpectationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateEvaluationExpectationRequest)

Request message for [EvaluationService.CreateEvaluationExpectation][google.cloud.ces.v1beta.EvaluationService.CreateEvaluationExpectation].

### [CreateEvaluationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateEvaluationRequest)

Request message for [EvaluationService.CreateEvaluation][google.cloud.ces.v1beta.EvaluationService.CreateEvaluation].

### [CreateExampleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateExampleRequest)

Request message for [AgentService.CreateExample][google.cloud.ces.v1beta.AgentService.CreateExample].

### [CreateGuardrailRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateGuardrailRequest)

Request message for [AgentService.CreateGuardrail][google.cloud.ces.v1beta.AgentService.CreateGuardrail].

### [CreateScheduledEvaluationRunRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateScheduledEvaluationRunRequest)

Request message for [EvaluationService.CreateScheduledEvaluationRun][google.cloud.ces.v1beta.EvaluationService.CreateScheduledEvaluationRun].

### [CreateToolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateToolRequest)

Request message for [AgentService.CreateTool][google.cloud.ces.v1beta.AgentService.CreateTool].

### [CreateToolsetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.CreateToolsetRequest)

Request message for [AgentService.CreateToolset][google.cloud.ces.v1beta.AgentService.CreateToolset].

### [DataStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DataStore)

A DataStore resource in Vertex AI Search.

### [DataStore.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DataStore.Types)

Container for nested types declared in the DataStore message type.

### [DataStore.Types.ConnectorConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DataStore.Types.ConnectorConfig)

The connector config for the data store connection.

### [DataStoreSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DataStoreSettings)

Data store related settings for the app.

### [DataStoreSettings.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DataStoreSettings.Types)

Container for nested types declared in the DataStoreSettings message type.

### [DataStoreSettings.Types.Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DataStoreSettings.Types.Engine)

An engine to which the data stores are connected. See Vertex AI Search: <https://cloud.google.com/generative-ai-app-builder/docs/enterprise-search-introduction>.

### [DataStoreSettings.Types.Engine.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DataStoreSettings.Types.Engine.Types)

Container for nested types declared in the Engine message type.

### [DataStoreTool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DataStoreTool)

Tool to retrieve from Vertex AI Search datastore or engine for grounding. Accepts either a datastore or an engine, but not both. See Vertex AI Search: <https://cloud.google.com/generative-ai-app-builder/docs/enterprise-search-introduction>.

### [DataStoreTool.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DataStoreTool.Types)

Container for nested types declared in the DataStoreTool message type.

### [DataStoreTool.Types.BoostSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DataStoreTool.Types.BoostSpec)

Boost specification to boost certain documents.

### [DataStoreTool.Types.BoostSpec.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DataStoreTool.Types.BoostSpec.Types)

Container for nested types declared in the BoostSpec message type.

### [DataStoreTool.Types.BoostSpec.Types.ConditionBoostSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DataStoreTool.Types.BoostSpec.Types.ConditionBoostSpec)

Boost specification for a condition.

### [DataStoreTool.Types.BoostSpec.Types.ConditionBoostSpec.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DataStoreTool.Types.BoostSpec.Types.ConditionBoostSpec.Types)

Container for nested types declared in the ConditionBoostSpec message type.

### [DataStoreTool.Types.BoostSpec.Types.ConditionBoostSpec.Types.BoostControlSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DataStoreTool.Types.BoostSpec.Types.ConditionBoostSpec.Types.BoostControlSpec)

Specification for custom ranking based on customer specified attribute value. It provides more controls for customized ranking than the simple (condition, boost) combination above.

### [DataStoreTool.Types.BoostSpec.Types.ConditionBoostSpec.Types.BoostControlSpec.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DataStoreTool.Types.BoostSpec.Types.ConditionBoostSpec.Types.BoostControlSpec.Types)

Container for nested types declared in the BoostControlSpec message type.

### [DataStoreTool.Types.BoostSpec.Types.ConditionBoostSpec.Types.BoostControlSpec.Types.ControlPoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DataStoreTool.Types.BoostSpec.Types.ConditionBoostSpec.Types.BoostControlSpec.Types.ControlPoint)

The control points used to define the curve. The curve defined through these control points can only be monotonically increasing or decreasing(constant values are acceptable).

### [DataStoreTool.Types.BoostSpecs](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DataStoreTool.Types.BoostSpecs)

Boost specifications to boost certain documents. For more information, please refer to <https://cloud.google.com/generative-ai-app-builder/docs/boosting>.

### [DataStoreTool.Types.DataStoreSource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DataStoreTool.Types.DataStoreSource)

Configuration for searching within a specific DataStore.

### [DataStoreTool.Types.EngineSource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DataStoreTool.Types.EngineSource)

Configuration for searching within an Engine, potentially targeting specific DataStores.

### [DataStoreTool.Types.GroundingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DataStoreTool.Types.GroundingConfig)

Grounding configuration.

### [DataStoreTool.Types.ModalityConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DataStoreTool.Types.ModalityConfig)

If specified, will apply the given configuration for the specified modality.

### [DataStoreTool.Types.ModalityConfig.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DataStoreTool.Types.ModalityConfig.Types)

Container for nested types declared in the ModalityConfig message type.

### [DataStoreTool.Types.RewriterConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DataStoreTool.Types.RewriterConfig)

Rewriter configuration.

### [DataStoreTool.Types.SummarizationConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DataStoreTool.Types.SummarizationConfig)

Summarization configuration.

### [DatasetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DatasetName)

Resource name for the `Dataset` resource.

### [DeidentifyTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeidentifyTemplateName)

Resource name for the `DeidentifyTemplate` resource.

### [DeleteAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteAgentRequest)

Request message for [AgentService.DeleteAgent][google.cloud.ces.v1beta.AgentService.DeleteAgent].

### [DeleteAppRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteAppRequest)

Request message for [AgentService.DeleteApp][google.cloud.ces.v1beta.AgentService.DeleteApp].

### [DeleteAppVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteAppVersionRequest)

Request message for [AgentService.DeleteAppVersion][google.cloud.ces.v1beta.AgentService.DeleteAppVersion].

### [DeleteConversationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteConversationRequest)

Request message for [AgentService.DeleteConversation][google.cloud.ces.v1beta.AgentService.DeleteConversation].

### [DeleteDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteDeploymentRequest)

Request message for [AgentService.DeleteDeployment][google.cloud.ces.v1beta.AgentService.DeleteDeployment].

### [DeleteEvaluationDatasetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteEvaluationDatasetRequest)

Request message for [EvaluationService.DeleteEvaluationDataset][google.cloud.ces.v1beta.EvaluationService.DeleteEvaluationDataset].

### [DeleteEvaluationExpectationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteEvaluationExpectationRequest)

Request message for [EvaluationService.DeleteEvaluationExpectation][google.cloud.ces.v1beta.EvaluationService.DeleteEvaluationExpectation].

### [DeleteEvaluationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteEvaluationRequest)

Request message for [EvaluationService.DeleteEvaluation][google.cloud.ces.v1beta.EvaluationService.DeleteEvaluation].

### [DeleteEvaluationResultRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteEvaluationResultRequest)

Request message for [EvaluationService.DeleteEvaluationResult][google.cloud.ces.v1beta.EvaluationService.DeleteEvaluationResult].

### [DeleteEvaluationRunOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteEvaluationRunOperationMetadata)

Operation metadata for [EvaluationService.DeleteEvaluationRun][google.cloud.ces.v1beta.EvaluationService.DeleteEvaluationRun].

### [DeleteEvaluationRunRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteEvaluationRunRequest)

Request message for [EvaluationService.DeleteEvaluationRun][google.cloud.ces.v1beta.EvaluationService.DeleteEvaluationRun].

### [DeleteExampleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteExampleRequest)

Request message for [AgentService.DeleteExample][google.cloud.ces.v1beta.AgentService.DeleteExample].

### [DeleteGuardrailRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteGuardrailRequest)

Request message for [AgentService.DeleteGuardrail][google.cloud.ces.v1beta.AgentService.DeleteGuardrail].

### [DeleteScheduledEvaluationRunRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteScheduledEvaluationRunRequest)

Request message for [EvaluationService.DeleteScheduledEvaluationRun][google.cloud.ces.v1beta.EvaluationService.DeleteScheduledEvaluationRun].

### [DeleteToolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteToolRequest)

Request message for [AgentService.DeleteTool][google.cloud.ces.v1beta.AgentService.DeleteTool].

### [DeleteToolsetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeleteToolsetRequest)

Request message for [AgentService.DeleteToolset][google.cloud.ces.v1beta.AgentService.DeleteToolset].

### [Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Deployment)

A deployment represents an immutable, queryable version of the app. It is used to deploy an app version with a specific channel profile.

### [DeploymentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeploymentName)

Resource name for the `Deployment` resource.

### [DialogflowAgentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DialogflowAgentName)

Resource name for the `DialogflowAgent` resource.

### [EndSession](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EndSession)

Indicates the session has terminated, due to either successful completion (e.g. user says "Good bye!" ) or an agent escalation.

The agent will not process any further inputs after session is terminated and the client should half-close and disconnect after receiving all remaining responses from the agent.

### [EndUserAuthConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EndUserAuthConfig)

End-user authentication configuration used for Connection calls. The field values must be the names of context variables in the format `$context.variables.<name_of_variable>`.

### [EndUserAuthConfig.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EndUserAuthConfig.Types)

Container for nested types declared in the EndUserAuthConfig message type.

### [EndUserAuthConfig.Types.Oauth2AuthCodeConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EndUserAuthConfig.Types.Oauth2AuthCodeConfig)

Oauth 2.0 Authorization Code authentication configuration.

### [EndUserAuthConfig.Types.Oauth2JwtBearerConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EndUserAuthConfig.Types.Oauth2JwtBearerConfig)

JWT Profile Oauth 2.0 Authorization Grant authentication configuration.

### [EndpointControlPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EndpointControlPolicy)

Defines project/location level endpoint control policy.

### [EndpointControlPolicy.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EndpointControlPolicy.Types)

Container for nested types declared in the EndpointControlPolicy message type.

### [EngineName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EngineName)

Resource name for the `Engine` resource.

### [ErrorHandlingSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ErrorHandlingSettings)

Settings to describe how errors should be handled in the app.

### [ErrorHandlingSettings.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ErrorHandlingSettings.Types)

Container for nested types declared in the ErrorHandlingSettings message type.

### [ErrorHandlingSettings.Types.EndSessionConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ErrorHandlingSettings.Types.EndSessionConfig)

Configuration for ending the session in case of system errors (e.g. LLM errors).

### [ErrorHandlingSettings.Types.FallbackResponseConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ErrorHandlingSettings.Types.FallbackResponseConfig)

Configuration for handling fallback responses.

### [Evaluation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Evaluation)

An evaluation represents all of the information needed to simulate and evaluate an agent.

### [Evaluation.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Evaluation.Types)

Container for nested types declared in the Evaluation message type.

### [Evaluation.Types.Golden](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Evaluation.Types.Golden)

The steps required to replay a golden conversation.

### [Evaluation.Types.GoldenExpectation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Evaluation.Types.GoldenExpectation)

Represents a single, checkable requirement.

### [Evaluation.Types.GoldenTurn](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Evaluation.Types.GoldenTurn)

A golden turn defines a single turn in a golden conversation.

### [Evaluation.Types.Scenario](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Evaluation.Types.Scenario)

The config for a scenario

### [Evaluation.Types.Scenario.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Evaluation.Types.Scenario.Types)

Container for nested types declared in the Scenario message type.

### [Evaluation.Types.Scenario.Types.UserFact](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Evaluation.Types.Scenario.Types.UserFact)

Facts about the user as a key value pair.

### [Evaluation.Types.ScenarioExpectation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Evaluation.Types.ScenarioExpectation)

The expectation to evaluate the conversation produced by the simulation.

### [Evaluation.Types.ScenarioExpectation.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Evaluation.Types.ScenarioExpectation.Types)

Container for nested types declared in the ScenarioExpectation message type.

### [Evaluation.Types.ScenarioExpectation.Types.ToolExpectation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Evaluation.Types.ScenarioExpectation.Types.ToolExpectation)

The tool call and response pair to be evaluated.

### [Evaluation.Types.Step](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Evaluation.Types.Step)

A step defines a singular action to happen during the evaluation.

### [EvaluationConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationConfig)

EvaluationConfig configures settings for running the evaluation.

### [EvaluationConfig.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationConfig.Types)

Container for nested types declared in the EvaluationConfig message type.

### [EvaluationDataset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationDataset)

An evaluation dataset represents a set of evaluations that are grouped together basaed on shared tags.

### [EvaluationDatasetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationDatasetName)

Resource name for the `EvaluationDataset` resource.

### [EvaluationErrorInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationErrorInfo)

Information about an error encountered during an evaluation execution.

### [EvaluationErrorInfo.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationErrorInfo.Types)

Container for nested types declared in the EvaluationErrorInfo message type.

### [EvaluationExpectation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationExpectation)

An evaluation expectation represents a specific criteria to evaluate against.

### [EvaluationExpectation.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationExpectation.Types)

Container for nested types declared in the EvaluationExpectation message type.

### [EvaluationExpectation.Types.LlmCriteria](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationExpectation.Types.LlmCriteria)

Configuration for LLM-based evaluation criteria.

### [EvaluationExpectationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationExpectationName)

Resource name for the `EvaluationExpectation` resource.

### [EvaluationMetricsConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationMetricsConfig)

Configures the metrics for an evaluation.

### [EvaluationMetricsConfig.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationMetricsConfig.Types)

Container for nested types declared in the EvaluationMetricsConfig message type.

### [EvaluationMetricsConfig.Types.ExpectationsMetMetricsConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationMetricsConfig.Types.ExpectationsMetMetricsConfig)

Configuration for the expectation level metrics for the evaluation. To disable the metric, set the message but do not set the `enable_expectations_met_metrics` field to true (or explicitly set it to false). To unset the configuration and fallback to the default behavior, omit the message entirely.

### [EvaluationMetricsConfig.Types.GoldenMetricsConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationMetricsConfig.Types.GoldenMetricsConfig)

Configuration for the golden metrics for the evaluation.

### [EvaluationMetricsConfig.Types.HallucinationMetricsConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationMetricsConfig.Types.HallucinationMetricsConfig)

Configuration for the hallucination metrics for the evaluation. To disable the metric, set the message but do not set the `enable_hallucination_metrics` field to true (or explicitly set it to false). To unset the configuration and fallback to the default behavior, omit the message entirely.

### [EvaluationMetricsConfig.Types.ScenarioMetricsConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationMetricsConfig.Types.ScenarioMetricsConfig)

Configuration for the scenario metrics for the evaluation.

### [EvaluationMetricsConfig.Types.SemanticSimilarityMetricsConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationMetricsConfig.Types.SemanticSimilarityMetricsConfig)

Configuration for similarity metrics for the evaluation. To disable the metric, set the message but do not set the `enable_semantic_similarity_metrics` field to true (or explicitly set it to false). To unset the configuration and fallback to the default behavior, omit the message entirely.

### [EvaluationMetricsConfig.Types.ToolCorrectnessMetricsConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationMetricsConfig.Types.ToolCorrectnessMetricsConfig)

Configuration for correctness metrics for the evaluation. To disable the metric, set the message but do not set the `enable_tool_correctness_metrics` field to true (or explicitly set it to false). To unset the configuration and fallback to the default behavior, omit the message entirely.

### [EvaluationMetricsConfig.Types.UserGoalMetMetricsConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationMetricsConfig.Types.UserGoalMetMetricsConfig)

Configuration for the user goal met metrics for the evaluation. To disable the metric, set the message but do not set the `enable_user_goal_met_metrics` field to true (or explicitly set it to false). To unset the configuration and fallback to the default behavior, omit the message entirely.

### [EvaluationMetricsThresholds](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationMetricsThresholds)

Threshold settings for metrics in an Evaluation.

### [EvaluationMetricsThresholds.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationMetricsThresholds.Types)

Container for nested types declared in the EvaluationMetricsThresholds message type.

### [EvaluationMetricsThresholds.Types.GoldenEvaluationMetricsThresholds](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationMetricsThresholds.Types.GoldenEvaluationMetricsThresholds)

Settings for golden evaluations.

### [EvaluationMetricsThresholds.Types.GoldenEvaluationMetricsThresholds.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationMetricsThresholds.Types.GoldenEvaluationMetricsThresholds.Types)

Container for nested types declared in the GoldenEvaluationMetricsThresholds message type.

### [EvaluationMetricsThresholds.Types.GoldenEvaluationMetricsThresholds.Types.ExpectationLevelMetricsThresholds](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationMetricsThresholds.Types.GoldenEvaluationMetricsThresholds.Types.ExpectationLevelMetricsThresholds)

Expectation level metrics thresholds.

### [EvaluationMetricsThresholds.Types.GoldenEvaluationMetricsThresholds.Types.TurnLevelMetricsThresholds](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationMetricsThresholds.Types.GoldenEvaluationMetricsThresholds.Types.TurnLevelMetricsThresholds)

Turn level metrics thresholds.

### [EvaluationMetricsThresholds.Types.GoldenEvaluationMetricsThresholds.Types.TurnLevelMetricsThresholds.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationMetricsThresholds.Types.GoldenEvaluationMetricsThresholds.Types.TurnLevelMetricsThresholds.Types)

Container for nested types declared in the TurnLevelMetricsThresholds message type.

### [EvaluationMetricsThresholds.Types.ToolMatchingSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationMetricsThresholds.Types.ToolMatchingSettings)

Settings for matching tool calls.

### [EvaluationMetricsThresholds.Types.ToolMatchingSettings.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationMetricsThresholds.Types.ToolMatchingSettings.Types)

Container for nested types declared in the ToolMatchingSettings message type.

### [EvaluationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationName)

Resource name for the `Evaluation` resource.

### [EvaluationPersona](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationPersona)

A persona represents an end user in an evaluation.

### [EvaluationPersona.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationPersona.Types)

Container for nested types declared in the EvaluationPersona message type.

### [EvaluationPersona.Types.SpeechConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationPersona.Types.SpeechConfig)

Configuration for Text-to-Speech generation.

### [EvaluationPersona.Types.SpeechConfig.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationPersona.Types.SpeechConfig.Types)

Container for nested types declared in the SpeechConfig message type.

### [EvaluationResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationResult)

An evaluation result represents the output of running an Evaluation.

### [EvaluationResult.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationResult.Types)

Container for nested types declared in the EvaluationResult message type.

### [EvaluationResult.Types.EvaluationExpectationResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationResult.Types.EvaluationExpectationResult)

The result of a single evaluation expectation.

### [EvaluationResult.Types.GoldenExpectationOutcome](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationResult.Types.GoldenExpectationOutcome)

Specifies the expectation and the result of that expectation.

### [EvaluationResult.Types.GoldenExpectationOutcome.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationResult.Types.GoldenExpectationOutcome.Types)

Container for nested types declared in the GoldenExpectationOutcome message type.

### [EvaluationResult.Types.GoldenExpectationOutcome.Types.ToolInvocationResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationResult.Types.GoldenExpectationOutcome.Types.ToolInvocationResult)

The result of the tool invocation check.

### [EvaluationResult.Types.GoldenResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationResult.Types.GoldenResult)

The result of a golden evaluation.

### [EvaluationResult.Types.GoldenResult.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationResult.Types.GoldenResult.Types)

Container for nested types declared in the GoldenResult message type.

### [EvaluationResult.Types.GoldenResult.Types.TurnReplayResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationResult.Types.GoldenResult.Types.TurnReplayResult)

The result of running a single turn of the golden conversation.

### [EvaluationResult.Types.HallucinationResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationResult.Types.HallucinationResult)

The result of the hallucination check for a single turn.

### [EvaluationResult.Types.OverallToolInvocationResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationResult.Types.OverallToolInvocationResult)

The result of the overall tool invocation check.

### [EvaluationResult.Types.ScenarioExpectationOutcome](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationResult.Types.ScenarioExpectationOutcome)

The outcome of a scenario expectation.

### [EvaluationResult.Types.ScenarioExpectationOutcome.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationResult.Types.ScenarioExpectationOutcome.Types)

Container for nested types declared in the ScenarioExpectationOutcome message type.

### [EvaluationResult.Types.ScenarioExpectationOutcome.Types.ObservedToolCall](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationResult.Types.ScenarioExpectationOutcome.Types.ObservedToolCall)

The observed tool call and response.

### [EvaluationResult.Types.ScenarioResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationResult.Types.ScenarioResult)

The outcome of a scenario evaluation.

### [EvaluationResult.Types.ScenarioRubricOutcome](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationResult.Types.ScenarioRubricOutcome)

The outcome of the evaluation against the rubric.

### [EvaluationResult.Types.SemanticSimilarityResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationResult.Types.SemanticSimilarityResult)

The result of the semantic similarity check.

### [EvaluationResult.Types.SpanLatency](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationResult.Types.SpanLatency)

The latency of a span execution.

### [EvaluationResult.Types.SpanLatency.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationResult.Types.SpanLatency.Types)

Container for nested types declared in the SpanLatency message type.

### [EvaluationResult.Types.TaskCompletionResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationResult.Types.TaskCompletionResult)

The result of the task completion check for the conversation.

### [EvaluationResult.Types.ToolCallLatency](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationResult.Types.ToolCallLatency)

The latency of a tool call execution.

### [EvaluationResult.Types.UserGoalSatisfactionResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationResult.Types.UserGoalSatisfactionResult)

The result of a user goal satisfaction check for a conversation.

### [EvaluationResultName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationResultName)

Resource name for the `EvaluationResult` resource.

### [EvaluationRun](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationRun)

An evaluation run represents an all the evaluation results from an evaluation execution.

### [EvaluationRun.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationRun.Types)

Container for nested types declared in the EvaluationRun message type.

### [EvaluationRun.Types.EvaluationRunSummary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationRun.Types.EvaluationRunSummary)

Contains the summary of passed and failed result counts for a specific evaluation in an evaluation run.

### [EvaluationRun.Types.Progress](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationRun.Types.Progress)

The progress of the evaluation run.

### [EvaluationRunCachingSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationRunCachingSettings)

Settings for evaluation run caching.

### [EvaluationRunCachingSettings.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationRunCachingSettings.Types)

Container for nested types declared in the EvaluationRunCachingSettings message type.

### [EvaluationRunName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationRunName)

Resource name for the `EvaluationRun` resource.

### [EvaluationService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationService)

EvaluationService exposes methods to perform evaluation for the CES app.

### [EvaluationService.EvaluationServiceBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationService.EvaluationServiceBase)

Base class for server-side implementations of EvaluationService

### [EvaluationService.EvaluationServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationService.EvaluationServiceClient)

Client for EvaluationService

### [EvaluationServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationServiceClient)

EvaluationService client wrapper, for convenient use.

### [EvaluationServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationServiceClientBuilder)

Builder class for [EvaluationServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationServiceClient) to provide simple configuration of credentials, endpoint etc.

### [EvaluationServiceClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationServiceClientImpl)

EvaluationService client wrapper implementation, for convenient use.

### [EvaluationServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationServiceSettings)

Settings for [EvaluationServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationServiceClient) instances.

### [EvaluationSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationSettings)

Settings for evaluation.

### [EvaluationSettings.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationSettings.Types)

Container for nested types declared in the EvaluationSettings message type.

### [Event](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Event)

Event input.

### [Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Example)

An example represents a sample conversation between the user and the agent(s).

### [ExampleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ExampleName)

Resource name for the `Example` resource.

### [ExecuteToolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ExecuteToolRequest)

Request message for [ToolService.ExecuteTool][google.cloud.ces.v1beta.ToolService.ExecuteTool].

### [ExecuteToolResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ExecuteToolResponse)

Response message for [ToolService.ExecuteTool][google.cloud.ces.v1beta.ToolService.ExecuteTool].

### [ExperimentConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ExperimentConfig)

Experiment for the deployment.

### [ExperimentConfig.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ExperimentConfig.Types)

Container for nested types declared in the ExperimentConfig message type.

### [ExperimentConfig.Types.VersionRelease](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ExperimentConfig.Types.VersionRelease)

Version release for the experiment.

### [ExperimentConfig.Types.VersionRelease.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ExperimentConfig.Types.VersionRelease.Types)

Container for nested types declared in the VersionRelease message type.

### [ExperimentConfig.Types.VersionRelease.Types.TrafficAllocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ExperimentConfig.Types.VersionRelease.Types.TrafficAllocation)

Traffic allocation for the version release.

### [ExportAppRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ExportAppRequest)

Request message for [AgentService.ExportApp][google.cloud.ces.v1beta.AgentService.ExportApp].

### [ExportAppRequest.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ExportAppRequest.Types)

Container for nested types declared in the ExportAppRequest message type.

### [ExportAppResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ExportAppResponse)

Response message for [AgentService.ExportApp][google.cloud.ces.v1beta.AgentService.ExportApp].

### [ExportEvaluationResultsOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ExportEvaluationResultsOperationMetadata)

Operation metadata for [EvaluationService.ExportEvaluationResults][google.cloud.ces.v1beta.EvaluationService.ExportEvaluationResults].

### [ExportEvaluationResultsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ExportEvaluationResultsRequest)

Request message for [EvaluationService.ExportEvaluationResults][google.cloud.ces.v1beta.EvaluationService.ExportEvaluationResults].

### [ExportEvaluationResultsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ExportEvaluationResultsResponse)

Response message for [EvaluationService.ExportEvaluationResults][google.cloud.ces.v1beta.EvaluationService.ExportEvaluationResults].

### [ExportEvaluationRunsOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ExportEvaluationRunsOperationMetadata)

Operation metadata for [EvaluationService.ExportEvaluationRuns][google.cloud.ces.v1beta.EvaluationService.ExportEvaluationRuns].

### [ExportEvaluationRunsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ExportEvaluationRunsRequest)

Request message for [EvaluationService.ExportEvaluationRuns][google.cloud.ces.v1beta.EvaluationService.ExportEvaluationRuns].

### [ExportEvaluationRunsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ExportEvaluationRunsResponse)

Response message for [EvaluationService.ExportEvaluationRuns][google.cloud.ces.v1beta.EvaluationService.ExportEvaluationRuns].

### [ExportEvaluationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ExportEvaluationsRequest)

Request message for [EvaluationService.ExportEvaluations][google.cloud.ces.v1beta.EvaluationService.ExportEvaluations].

### [ExportEvaluationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ExportEvaluationsResponse)

Response message for [EvaluationService.ExportEvaluations][google.cloud.ces.v1beta.EvaluationService.ExportEvaluations].

### [ExportOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ExportOptions)

Options for exporting CES evaluation resources.

### [ExportOptions.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ExportOptions.Types)

Container for nested types declared in the ExportOptions message type.

### [ExpressionCondition](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ExpressionCondition)

Expression condition based on session state.

### [FileContext](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.FileContext)

Files to be used as context. Files can be provided as raw bytes.

### [FileContext.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.FileContext.Types)

Container for nested types declared in the FileContext message type.

### [FileContext.Types.FileBytes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.FileContext.Types.FileBytes)

File provided as raw bytes.

### [FileSearchTool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.FileSearchTool)

The file search tool allows the agent to search across the files uploaded by the app/agent developer. It has presets to give relatively good quality search over the uploaded files and summarization of the retrieved results.

### [FileSearchTool.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.FileSearchTool.Types)

Container for nested types declared in the FileSearchTool message type.

### [GenerateAppResourceOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateAppResourceOperationMetadata)

Operation metadata for [AgentService.GenerateAppResource][google.cloud.ces.v1beta.AgentService.GenerateAppResource].

### [GenerateAppResourceOperationMetadata.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateAppResourceOperationMetadata.Types)

Container for nested types declared in the GenerateAppResourceOperationMetadata message type.

### [GenerateAppResourceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateAppResourceRequest)

Request message for [AgentService.GenerateAppResource][google.cloud.ces.v1beta.AgentService.GenerateAppResource].

### [GenerateAppResourceRequest.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateAppResourceRequest.Types)

Container for nested types declared in the GenerateAppResourceRequest message type.

### [GenerateAppResourceRequest.Types.AppGenerationConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateAppResourceRequest.Types.AppGenerationConfig)

The configuration to be used to generate the app.

### [GenerateAppResourceRequest.Types.AppVersionContext](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateAppResourceRequest.Types.AppVersionContext)

The app version context specifying the base snapshot and target agent.

### [GenerateAppResourceRequest.Types.EvaluationGenerationConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateAppResourceRequest.Types.EvaluationGenerationConfig)

The configuration to be used to generate the evaluations.

### [GenerateAppResourceRequest.Types.EvaluationPersonasGenerationConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateAppResourceRequest.Types.EvaluationPersonasGenerationConfig)

The configuration to be used to generate the evaluation personas.

### [GenerateAppResourceRequest.Types.HillClimbingFixConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateAppResourceRequest.Types.HillClimbingFixConfig)

The configuration to be used for hill climbing fixes.

### [GenerateAppResourceRequest.Types.QualityReportGenerationConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateAppResourceRequest.Types.QualityReportGenerationConfig)

The configuration to be used for quality report generation.

### [GenerateAppResourceRequest.Types.QualityReportGenerationConfig.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateAppResourceRequest.Types.QualityReportGenerationConfig.Types)

Container for nested types declared in the QualityReportGenerationConfig message type.

### [GenerateAppResourceRequest.Types.RefineInstructions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateAppResourceRequest.Types.RefineInstructions)

The instructions to be used to refine a part of the resource. The part of the resource can be specified with a start index, end index and a field mask. For example, if you want to refine a part of the agent instructions you can specify the index of the first character of the instructions, the index of the last character of the instructions and the field mask as "instructions".

### [GenerateAppResourceRequest.Types.ToolGenerationConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateAppResourceRequest.Types.ToolGenerationConfig)

The configuration to be used to generate a tool.

### [GenerateAppResourceRequest.Types.ToolGenerationConfig.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateAppResourceRequest.Types.ToolGenerationConfig.Types)

Container for nested types declared in the ToolGenerationConfig message type.

### [GenerateAppResourceRequest.Types.ToolGenerationConfig.Types.OpenApiToolsetGenerationConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateAppResourceRequest.Types.ToolGenerationConfig.Types.OpenApiToolsetGenerationConfig)

The configuration to be used to generate an Open API schema.

### [GenerateAppResourceRequest.Types.ToolGenerationConfig.Types.OpenApiToolsetGenerationConfig.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateAppResourceRequest.Types.ToolGenerationConfig.Types.OpenApiToolsetGenerationConfig.Types)

Container for nested types declared in the OpenApiToolsetGenerationConfig message type.

### [GenerateAppResourceRequest.Types.ToolGenerationConfig.Types.OpenApiToolsetGenerationConfig.Types.OperationGenerationConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateAppResourceRequest.Types.ToolGenerationConfig.Types.OpenApiToolsetGenerationConfig.Types.OperationGenerationConfig)

The configuration to be used to generate an operation in the Open API schema.

### [GenerateAppResourceResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateAppResourceResponse)

Response message for [AgentService.GenerateAppResource][google.cloud.ces.v1beta.AgentService.GenerateAppResource].

### [GenerateAppResourceResponse.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateAppResourceResponse.Types)

Container for nested types declared in the GenerateAppResourceResponse message type.

### [GenerateAppResourceResponse.Types.AppResources](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateAppResourceResponse.Types.AppResources)

The list of app resources generated by the LLM assistant.

### [GenerateAppResourceResponse.Types.Evaluations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateAppResourceResponse.Types.Evaluations)

The list of evaluations generated by the LLM assistant.

### [GenerateAppResourceResponse.Types.GenerateResultInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateAppResourceResponse.Types.GenerateResultInfo)

This provides additional information about the generated result.

### [GenerateAppResourceResponse.Types.Tools](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateAppResourceResponse.Types.Tools)

The list of tools generated by the LLM assistant.

### [GenerateChatTokenRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateChatTokenRequest)

Request message for [WidgetService.GenerateChatToken][google.cloud.ces.v1beta.WidgetService.GenerateChatToken].

### [GenerateChatTokenResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateChatTokenResponse)

Response message for [WidgetService.GenerateChatToken][google.cloud.ces.v1beta.WidgetService.GenerateChatToken].

### [GenerateEvaluationOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateEvaluationOperationMetadata)

Operation metadata for [EvaluationService.GenerateEvaluation][google.cloud.ces.v1beta.EvaluationService.GenerateEvaluation].

### [GenerateEvaluationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateEvaluationRequest)

Request message for [EvaluationService.GenerateEvaluation][google.cloud.ces.v1beta.EvaluationService.GenerateEvaluation].

### [GenerateEvaluationRequest.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateEvaluationRequest.Types)

Container for nested types declared in the GenerateEvaluationRequest message type.

### [GetAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetAgentRequest)

Request message for [AgentService.GetAgent][google.cloud.ces.v1beta.AgentService.GetAgent].

### [GetAppRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetAppRequest)

Request message for [AgentService.GetApp][google.cloud.ces.v1beta.AgentService.GetApp].

### [GetAppVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetAppVersionRequest)

Request message for [AgentService.GetAppVersion][google.cloud.ces.v1beta.AgentService.GetAppVersion].

### [GetChangelogRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetChangelogRequest)

Request message for [AgentService.GetChangelog][google.cloud.ces.v1beta.AgentService.GetChangelog].

### [GetConversationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetConversationRequest)

Request message for [AgentService.GetConversation][google.cloud.ces.v1beta.AgentService.GetConversation].

### [GetDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetDeploymentRequest)

Request message for [AgentService.GetDeployment][google.cloud.ces.v1beta.AgentService.GetDeployment].

### [GetEvaluationDatasetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetEvaluationDatasetRequest)

Request message for [EvaluationService.GetEvaluationDataset][google.cloud.ces.v1beta.EvaluationService.GetEvaluationDataset].

### [GetEvaluationExpectationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetEvaluationExpectationRequest)

Request message for [EvaluationService.GetEvaluationExpectation][google.cloud.ces.v1beta.EvaluationService.GetEvaluationExpectation].

### [GetEvaluationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetEvaluationRequest)

Request message for [EvaluationService.GetEvaluation][google.cloud.ces.v1beta.EvaluationService.GetEvaluation].

### [GetEvaluationResultRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetEvaluationResultRequest)

Request message for [EvaluationService.GetEvaluationResult][google.cloud.ces.v1beta.EvaluationService.GetEvaluationResult].

### [GetEvaluationRunRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetEvaluationRunRequest)

Request message for [EvaluationService.GetEvaluationRun][google.cloud.ces.v1beta.EvaluationService.GetEvaluationRun].

### [GetExampleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetExampleRequest)

Request message for [AgentService.GetExample][google.cloud.ces.v1beta.AgentService.GetExample].

### [GetGuardrailRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetGuardrailRequest)

Request message for [AgentService.GetGuardrail][google.cloud.ces.v1beta.AgentService.GetGuardrail].

### [GetScheduledEvaluationRunRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetScheduledEvaluationRunRequest)

Request message for [EvaluationService.GetScheduledEvaluationRun][google.cloud.ces.v1beta.EvaluationService.GetScheduledEvaluationRun].

### [GetSecuritySettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetSecuritySettingsRequest)

Request message for [AgentService.GetSecuritySettings][google.cloud.ces.v1beta.AgentService.GetSecuritySettings].

### [GetToolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetToolRequest)

Request message for [AgentService.GetTool][google.cloud.ces.v1beta.AgentService.GetTool].

### [GetToolsetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GetToolsetRequest)

Request message for [AgentService.GetToolset][google.cloud.ces.v1beta.AgentService.GetToolset].

### [GoAway](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GoAway)

Indicates that the server will disconnect soon and the client should half-close and restart the connection.

### [GoogleSearchSuggestions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GoogleSearchSuggestions)

Search suggestions from [Google Search Tool][google.cloud.ces.v1beta.GoogleSearchTool].

### [GoogleSearchTool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GoogleSearchTool)

Represents a tool to perform Google web searches for grounding. See <https://cloud.google.com/customer-engagement-ai/conversational-agents/ps/tool#google-search>.

### [GoogleSearchTool.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GoogleSearchTool.Types)

Container for nested types declared in the GoogleSearchTool message type.

### [GoogleSearchTool.Types.PromptConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GoogleSearchTool.Types.PromptConfig)

Prompt settings used by the model when processing or summarizing the google search results.

### [Guardrail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail)

Guardrail contains a list of checks and balances to keep the agents safe and secure.

### [Guardrail.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail.Types)

Container for nested types declared in the Guardrail message type.

### [Guardrail.Types.CodeCallback](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail.Types.CodeCallback)

Guardrail that blocks the conversation based on the code callbacks provided.

### [Guardrail.Types.ContentFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail.Types.ContentFilter)

Guardrail that bans certain content from being used in the conversation.

### [Guardrail.Types.ContentFilter.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail.Types.ContentFilter.Types)

Container for nested types declared in the ContentFilter message type.

### [Guardrail.Types.LlmPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail.Types.LlmPolicy)

Guardrail that blocks the conversation if the LLM response is considered violating the policy based on the LLM classification.

### [Guardrail.Types.LlmPolicy.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail.Types.LlmPolicy.Types)

Container for nested types declared in the LlmPolicy message type.

### [Guardrail.Types.LlmPromptSecurity](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail.Types.LlmPromptSecurity)

Guardrail that blocks the conversation if the input is considered unsafe based on the LLM classification.

### [Guardrail.Types.LlmPromptSecurity.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail.Types.LlmPromptSecurity.Types)

Container for nested types declared in the LlmPromptSecurity message type.

### [Guardrail.Types.LlmPromptSecurity.Types.DefaultSecuritySettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail.Types.LlmPromptSecurity.Types.DefaultSecuritySettings)

Configuration for default system security settings.

### [Guardrail.Types.ModelSafety](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail.Types.ModelSafety)

Model safety settings overrides. When this is set, it will override the default settings and trigger the guardrail if the response is considered unsafe.

### [Guardrail.Types.ModelSafety.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail.Types.ModelSafety.Types)

Container for nested types declared in the ModelSafety message type.

### [Guardrail.Types.ModelSafety.Types.SafetySetting](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail.Types.ModelSafety.Types.SafetySetting)

Safety setting.

### [GuardrailName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GuardrailName)

Resource name for the `Guardrail` resource.

### [Image](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Image)

Represents an image input or output in the conversation.

### [ImportAppRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ImportAppRequest)

Request message for [AgentService.ImportApp][google.cloud.ces.v1beta.AgentService.ImportApp].

### [ImportAppRequest.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ImportAppRequest.Types)

Container for nested types declared in the ImportAppRequest message type.

### [ImportAppRequest.Types.ImportOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ImportAppRequest.Types.ImportOptions)

Configuration options for the app import process. These options control how the import behaves, particularly when conflicts arise with existing app data.

### [ImportAppRequest.Types.ImportOptions.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ImportAppRequest.Types.ImportOptions.Types)

Container for nested types declared in the ImportOptions message type.

### [ImportAppResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ImportAppResponse)

Response message for [AgentService.ImportApp][google.cloud.ces.v1beta.AgentService.ImportApp].

### [ImportEvaluationsOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ImportEvaluationsOperationMetadata)

Represents the metadata of the long-running operation for [EvaluationService.ImportEvaluations][google.cloud.ces.v1beta.EvaluationService.ImportEvaluations].

### [ImportEvaluationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ImportEvaluationsRequest)

Request message for [EvaluationService.ImportEvaluations][google.cloud.ces.v1beta.EvaluationService.ImportEvaluations].

### [ImportEvaluationsRequest.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ImportEvaluationsRequest.Types)

Container for nested types declared in the ImportEvaluationsRequest message type.

### [ImportEvaluationsRequest.Types.ConversationList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ImportEvaluationsRequest.Types.ConversationList)

A list of conversation resource names.

### [ImportEvaluationsRequest.Types.ImportOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ImportEvaluationsRequest.Types.ImportOptions)

Configuration options for the evaluation import process. These options control how the import behaves, particularly when conflicts arise with existing evaluations data.

### [ImportEvaluationsRequest.Types.ImportOptions.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ImportEvaluationsRequest.Types.ImportOptions.Types)

Container for nested types declared in the ImportOptions message type.

### [ImportEvaluationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ImportEvaluationsResponse)

Response message for [EvaluationService.ImportEvaluations][google.cloud.ces.v1beta.EvaluationService.ImportEvaluations].

### [InputAudioConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.InputAudioConfig)

InputAudioConfig configures how the CES agent should interpret the incoming audio data.

### [InspectTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.InspectTemplateName)

Resource name for the `InspectTemplate` resource.

### [InstagramCredentials](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.InstagramCredentials)

Ephemeral Meta credentials for Instagram native integration.

### [InterruptionSignal](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.InterruptionSignal)

Indicates the agent's audio response has been interrupted. The client should immediately stop any current audio playback (e.g., due to user barge-in or a new agent response being generated).

### [LanguageSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.LanguageSettings)

Language settings of the app.

### [LatencyReport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.LatencyReport)

Latency report for the evaluation run.

### [LatencyReport.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.LatencyReport.Types)

Container for nested types declared in the LatencyReport message type.

### [LatencyReport.Types.CallbackLatency](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.LatencyReport.Types.CallbackLatency)

Latency metrics for a single callback.

### [LatencyReport.Types.GuardrailLatency](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.LatencyReport.Types.GuardrailLatency)

Latency metrics for a single guardrail.

### [LatencyReport.Types.LatencyMetrics](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.LatencyReport.Types.LatencyMetrics)

Latency metrics for a component.

### [LatencyReport.Types.LlmCallLatency](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.LatencyReport.Types.LlmCallLatency)

Latency metrics for a single LLM call.

### [LatencyReport.Types.ToolLatency](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.LatencyReport.Types.ToolLatency)

Latency metrics for a single tool.

### [ListAgentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListAgentsRequest)

Request message for [AgentService.ListAgents][google.cloud.ces.v1beta.AgentService.ListAgents].

### [ListAgentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListAgentsResponse)

Response message for [AgentService.ListAgents][google.cloud.ces.v1beta.AgentService.ListAgents].

### [ListAppVersionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListAppVersionsRequest)

Request message for [AgentService.ListAppVersions][google.cloud.ces.v1beta.AgentService.ListAppVersions].

### [ListAppVersionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListAppVersionsResponse)

Response message for [AgentService.ListAppVersions][google.cloud.ces.v1beta.AgentService.ListAppVersions].

### [ListAppsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListAppsRequest)

Request message for [AgentService.ListApps][google.cloud.ces.v1beta.AgentService.ListApps].

### [ListAppsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListAppsResponse)

Response message for [AgentService.ListApps][google.cloud.ces.v1beta.AgentService.ListApps].

### [ListChangelogsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListChangelogsRequest)

Request message for [AgentService.ListChangelogs][google.cloud.ces.v1beta.AgentService.ListChangelogs].

### [ListChangelogsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListChangelogsResponse)

Response message for [AgentService.ListChangelogs][google.cloud.ces.v1beta.AgentService.ListChangelogs].

### [ListConversationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListConversationsRequest)

Request message for [AgentService.ListConversations][google.cloud.ces.v1beta.AgentService.ListConversations].

### [ListConversationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListConversationsResponse)

Response message for [AgentService.ListConversations][google.cloud.ces.v1beta.AgentService.ListConversations].

### [ListDeploymentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListDeploymentsRequest)

Request message for [AgentService.ListDeployments][google.cloud.ces.v1beta.AgentService.ListDeployments].

### [ListDeploymentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListDeploymentsResponse)

Response message for [AgentService.ListDeployments][google.cloud.ces.v1beta.AgentService.ListDeployments].

### [ListEvaluationDatasetsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListEvaluationDatasetsRequest)

Request message for [EvaluationService.ListEvaluationDatasets][google.cloud.ces.v1beta.EvaluationService.ListEvaluationDatasets].

### [ListEvaluationDatasetsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListEvaluationDatasetsResponse)

Response message for [EvaluationService.ListEvaluationDatasets][google.cloud.ces.v1beta.EvaluationService.ListEvaluationDatasets].

### [ListEvaluationExpectationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListEvaluationExpectationsRequest)

Request message for [EvaluationService.ListEvaluationExpectations][google.cloud.ces.v1beta.EvaluationService.ListEvaluationExpectations].

### [ListEvaluationExpectationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListEvaluationExpectationsResponse)

Response message for [EvaluationService.ListEvaluationExpectations][google.cloud.ces.v1beta.EvaluationService.ListEvaluationExpectations].

### [ListEvaluationResultsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListEvaluationResultsRequest)

Request message for [EvaluationService.ListEvaluationResults][google.cloud.ces.v1beta.EvaluationService.ListEvaluationResults].

### [ListEvaluationResultsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListEvaluationResultsResponse)

Response message for [EvaluationService.ListEvaluationResults][google.cloud.ces.v1beta.EvaluationService.ListEvaluationResults].

### [ListEvaluationRunsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListEvaluationRunsRequest)

Request message for [EvaluationService.ListEvaluationRuns][google.cloud.ces.v1beta.EvaluationService.ListEvaluationRuns].

### [ListEvaluationRunsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListEvaluationRunsResponse)

Response message for [EvaluationService.ListEvaluationRuns][google.cloud.ces.v1beta.EvaluationService.ListEvaluationRuns].

### [ListEvaluationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListEvaluationsRequest)

Request message for [EvaluationService.ListEvaluations][google.cloud.ces.v1beta.EvaluationService.ListEvaluations].

### [ListEvaluationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListEvaluationsResponse)

Response message for [EvaluationService.ListEvaluations][google.cloud.ces.v1beta.EvaluationService.ListEvaluations].

### [ListExamplesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListExamplesRequest)

Request message for [AgentService.ListExamples][google.cloud.ces.v1beta.AgentService.ListExamples].

### [ListExamplesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListExamplesResponse)

Response message for [AgentService.ListExamples][google.cloud.ces.v1beta.AgentService.ListExamples].

### [ListGuardrailsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListGuardrailsRequest)

Request message for [AgentService.ListGuardrails][google.cloud.ces.v1beta.AgentService.ListGuardrails].

### [ListGuardrailsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListGuardrailsResponse)

Response message for [AgentService.ListGuardrails][google.cloud.ces.v1beta.AgentService.ListGuardrails].

### [ListScheduledEvaluationRunsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListScheduledEvaluationRunsRequest)

Request message for [EvaluationService.ListScheduledEvaluationRuns][google.cloud.ces.v1beta.EvaluationService.ListScheduledEvaluationRuns].

### [ListScheduledEvaluationRunsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListScheduledEvaluationRunsResponse)

Response message for [EvaluationService.ListScheduledEvaluationRuns][google.cloud.ces.v1beta.EvaluationService.ListScheduledEvaluationRuns].

### [ListToolsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListToolsRequest)

Request message for [AgentService.ListTools][google.cloud.ces.v1beta.AgentService.ListTools].

### [ListToolsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListToolsResponse)

Response message for [AgentService.ListTools][google.cloud.ces.v1beta.AgentService.ListTools].

### [ListToolsetsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListToolsetsRequest)

Request message for [AgentService.ListToolsets][google.cloud.ces.v1beta.AgentService.ListToolsets].

### [ListToolsetsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ListToolsetsResponse)

Response message for [AgentService.ListToolsets][google.cloud.ces.v1beta.AgentService.ListToolsets].

### [LoggingSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.LoggingSettings)

Settings to describe the logging behaviors for the app.

### [McpTool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.McpTool)

An MCP tool. See <https://modelcontextprotocol.io/specification/2025-06-18/server/tools> for more details.

### [McpTool.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.McpTool.Types)

Container for nested types declared in the McpTool message type.

### [McpToolDefinition](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.McpToolDefinition)

Container for a tool's core definition elements that are snapshot. Schemas in the snapshot are used as-is and cannot be overridden.

### [McpToolOverride](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.McpToolOverride)

Overrides associated with a given tool in a Toolset. This enables "pinning" or "overriding" of tool definitions from the external dynamic server.

### [McpToolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.McpToolset)

A toolset that contains a list of tools that are offered by the MCP server.

### [Message](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Message)

A message within a conversation.

### [MetricAnalysisSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.MetricAnalysisSettings)

Settings to describe the conversation data collection behaviors for LLM analysis metrics pipeline.

### [MockConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.MockConfig)

Mock tool calls configuration for the session.

### [MockConfig.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.MockConfig.Types)

Container for nested types declared in the MockConfig message type.

### [MockedToolCall](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.MockedToolCall)

A mocked tool call.

Expresses the target tool + a pattern to match against that tool's args / inputs. If the pattern matches, then the mock response will be returned.

### [ModelSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ModelSettings)

Model settings contains various configurations for the LLM model.

### [OAuthConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OAuthConfig)

Configurations for authentication with OAuth.

### [OAuthConfig.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OAuthConfig.Types)

Container for nested types declared in the OAuthConfig message type.

### [Omnichannel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Omnichannel)

Represents an Omnichannel resource.

### [OmnichannelIntegrationConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OmnichannelIntegrationConfig)

OmnichannelIntegrationConfig contains all App integration configs.

### [OmnichannelIntegrationConfig.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OmnichannelIntegrationConfig.Types)

Container for nested types declared in the OmnichannelIntegrationConfig message type.

### [OmnichannelIntegrationConfig.Types.CesAppConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OmnichannelIntegrationConfig.Types.CesAppConfig)

Configs for CES app.

### [OmnichannelIntegrationConfig.Types.ChannelConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OmnichannelIntegrationConfig.Types.ChannelConfig)

ChannelConfig contains config for various of app integration.

### [OmnichannelIntegrationConfig.Types.RoutingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OmnichannelIntegrationConfig.Types.RoutingConfig)

Routing config specify how/who to route app events to a subscriber.

### [OmnichannelIntegrationConfig.Types.SubscriberConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OmnichannelIntegrationConfig.Types.SubscriberConfig)

Configs of subscribers.

### [OmnichannelIntegrationConfig.Types.WhatsappConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OmnichannelIntegrationConfig.Types.WhatsappConfig)

How Omnichannel should receive/reply events from WhatsApp.

### [OmnichannelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OmnichannelName)

Resource name for the `Omnichannel` resource.

### [OmnichannelOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OmnichannelOperationMetadata)

Represents the metadata of the long-running operation.

### [OpenApiTool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OpenApiTool)

A remote API tool defined by an OpenAPI schema.

### [OpenApiToolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OpenApiToolset)

A toolset that contains a list of tools that are defined by an OpenAPI schema.

### [OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OperationMetadata)

Represents the metadata of the long-running operation.

### [OptimizationConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OptimizationConfig)

Configuration for running the optimization step after the evaluation run.

### [OptimizationConfig.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OptimizationConfig.Types)

Container for nested types declared in the OptimizationConfig message type.

### [OutputAudioConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OutputAudioConfig)

OutputAudioConfig configures how the CES agent should synthesize outgoing audio responses.

### [PersonaRunConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.PersonaRunConfig)

Configuration for running an evaluation for a specific persona.

### [PythonCodeCondition](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.PythonCodeCondition)

Python code block to evaluate the condition.

### [PythonFunction](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.PythonFunction)

A Python function tool.

### [QualityReport](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.QualityReport)

The report describing any identified quality issues in the app.

### [QualityReport.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.QualityReport.Types)

Container for nested types declared in the QualityReport message type.

### [QualityReport.Types.AgentIssues](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.QualityReport.Types.AgentIssues)

Issues identified for a single agent.

### [QualityReport.Types.Issue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.QualityReport.Types.Issue)

The issue identified.

### [RecognitionResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.RecognitionResult)

Speech recognition result for the audio input.

### [RedactionConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.RedactionConfig)

Configuration to instruct how sensitive data should be handled.

### [RemoteAgentTool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.RemoteAgentTool)

Represents a tool that allows the agent to call another remote agent.

### [RestoreAppVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.RestoreAppVersionRequest)

Request message for [AgentService.RestoreAppVersion][google.cloud.ces.v1beta.AgentService.RestoreAppVersion]

### [RestoreAppVersionResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.RestoreAppVersionResponse)

Response message for [AgentService.RestoreAppVersion][google.cloud.ces.v1beta.AgentService.RestoreAppVersion]

### [RetrieveToolSchemaRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.RetrieveToolSchemaRequest)

Request message for [ToolService.RetrieveToolSchema][google.cloud.ces.v1beta.ToolService.RetrieveToolSchema].

### [RetrieveToolSchemaResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.RetrieveToolSchemaResponse)

Response message for [ToolService.RetrieveToolSchema][google.cloud.ces.v1beta.ToolService.RetrieveToolSchema].

### [RetrieveToolsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.RetrieveToolsRequest)

Request message for [ToolService.RetrieveTools][google.cloud.ces.v1beta.ToolService.RetrieveTools].

### [RetrieveToolsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.RetrieveToolsResponse)

Response message for [ToolService.RetrieveTools][google.cloud.ces.v1beta.ToolService.RetrieveTools].

### [RunEvaluationOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.RunEvaluationOperationMetadata)

Operation metadata for [EvaluationService.RunEvaluation][google.cloud.ces.v1beta.EvaluationService.RunEvaluation].

### [RunEvaluationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.RunEvaluationRequest)

Request message for [EvaluationService.RunEvaluation][google.cloud.ces.v1beta.EvaluationService.RunEvaluation].

### [RunEvaluationResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.RunEvaluationResponse)

Response message for [EvaluationService.RunEvaluation][google.cloud.ces.v1beta.EvaluationService.RunEvaluation].

### [RunEvaluationResultMetricsOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.RunEvaluationResultMetricsOperationMetadata)

Operation metadata for [EvaluationService.RunEvaluationResultMetrics][google.cloud.ces.v1beta.EvaluationService.RunEvaluationResultMetrics].

### [RunEvaluationResultMetricsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.RunEvaluationResultMetricsRequest)

Request message for [EvaluationService.RunEvaluationResultMetrics][google.cloud.ces.v1beta.EvaluationService.RunEvaluationResultMetrics].

### [RunEvaluationResultMetricsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.RunEvaluationResultMetricsResponse)

Response message for [EvaluationService.RunEvaluationResultMetrics][google.cloud.ces.v1beta.EvaluationService.RunEvaluationResultMetrics].

### [RunSessionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.RunSessionRequest)

Request message for [SessionService.RunSession][google.cloud.ces.v1beta.SessionService.RunSession].

### [RunSessionResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.RunSessionResponse)

Response message for [SessionService.RunSession][google.cloud.ces.v1beta.SessionService.RunSession].

### [ScheduledEvaluationRun](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ScheduledEvaluationRun)

Represents a scheduled evaluation run configuration.

### [ScheduledEvaluationRun.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ScheduledEvaluationRun.Types)

Container for nested types declared in the ScheduledEvaluationRun message type.

### [ScheduledEvaluationRun.Types.SchedulingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ScheduledEvaluationRun.Types.SchedulingConfig)

Eval scheduling configuration details

### [ScheduledEvaluationRun.Types.SchedulingConfig.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ScheduledEvaluationRun.Types.SchedulingConfig.Types)

Container for nested types declared in the SchedulingConfig message type.

### [ScheduledEvaluationRunName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ScheduledEvaluationRunName)

Resource name for the `ScheduledEvaluationRun` resource.

### [Schema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Schema)

Represents a select subset of an OpenAPI 3.0 schema object.

### [Schema.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Schema.Types)

Container for nested types declared in the Schema message type.

### [SecretVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SecretVersionName)

Resource name for the `SecretVersion` resource.

### [SecuritySettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SecuritySettings)

Project/Location level security settings for CES.

### [SecuritySettingsName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SecuritySettingsName)

Resource name for the `SecuritySettings` resource.

### [ServiceAccountAuthConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ServiceAccountAuthConfig)

Configurations for authentication using a custom service account.

### [ServiceAgentIdTokenAuthConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ServiceAgentIdTokenAuthConfig)

Configurations for authentication with [ID token](https://cloud.google.com/docs/authentication/token-types#id) generated from service agent.

### [ServiceDirectoryConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ServiceDirectoryConfig)

Configuration for tools using Service Directory.

### [ServiceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ServiceName)

Resource name for the `Service` resource.

### [SessionConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SessionConfig)

The configuration for the session.

### [SessionConfig.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SessionConfig.Types)

Container for nested types declared in the SessionConfig message type.

### [SessionConfig.Types.RemoteDialogflowQueryParameters](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SessionConfig.Types.RemoteDialogflowQueryParameters)

[QueryParameters](https://cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#queryparameters) to send to the remote [Dialogflow](https://cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents) agent when the session control is transferred to the remote agent.

### [SessionInput](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SessionInput)

Input for the session.

### [SessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SessionName)

Resource name for the `Session` resource.

### [SessionOutput](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SessionOutput)

Output for the session.

### [SessionOutput.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SessionOutput.Types)

Container for nested types declared in the SessionOutput message type.

### [SessionOutput.Types.DiagnosticInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SessionOutput.Types.DiagnosticInfo)

Contains execution details during the processing.

### [SessionService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SessionService)

Session service provides APIs for interacting with CES agents.

### [SessionService.SessionServiceBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SessionService.SessionServiceBase)

Base class for server-side implementations of SessionService

### [SessionService.SessionServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SessionService.SessionServiceClient)

Client for SessionService

### [SessionServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SessionServiceClient)

SessionService client wrapper, for convenient use.

### [SessionServiceClient.BidiRunSessionStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SessionServiceClient.BidiRunSessionStream)

Bidirectional streaming methods for [BidiRunSession(CallSettings, BidirectionalStreamingSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SessionServiceClient#Google_Cloud_Ces_V1Beta_SessionServiceClient_BidiRunSession_Google_Api_Gax_Grpc_CallSettings_Google_Api_Gax_Grpc_BidirectionalStreamingSettings_).

### [SessionServiceClient.StreamRunSessionStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SessionServiceClient.StreamRunSessionStream)

Server streaming methods for [StreamRunSession(RunSessionRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SessionServiceClient#Google_Cloud_Ces_V1Beta_SessionServiceClient_StreamRunSession_Google_Cloud_Ces_V1Beta_RunSessionRequest_Google_Api_Gax_Grpc_CallSettings_).

### [SessionServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SessionServiceClientBuilder)

Builder class for [SessionServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SessionServiceClient) to provide simple configuration of credentials, endpoint etc.

### [SessionServiceClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SessionServiceClientImpl)

SessionService client wrapper implementation, for convenient use.

### [SessionServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SessionServiceSettings)

Settings for [SessionServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SessionServiceClient) instances.

### [Span](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Span)

A span is a unit of work or a single operation during the request processing.

### [SynthesizeSpeechConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SynthesizeSpeechConfig)

Configuration for how the agent response should be synthesized.

### [SystemTool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SystemTool)

Pre-defined system tool.

### [TestPersonaVoiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.TestPersonaVoiceRequest)

Request message for [EvaluationService.TestPersonaVoice][google.cloud.ces.v1beta.EvaluationService.TestPersonaVoice].

### [TestPersonaVoiceResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.TestPersonaVoiceResponse)

Response message for [EvaluationService.TestPersonaVoice][google.cloud.ces.v1beta.EvaluationService.TestPersonaVoice].

### [TimeZoneSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.TimeZoneSettings)

TimeZone settings of the app.

### [TlsConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.TlsConfig)

The TLS configuration.

### [TlsConfig.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.TlsConfig.Types)

Container for nested types declared in the TlsConfig message type.

### [TlsConfig.Types.CaCert](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.TlsConfig.Types.CaCert)

The CA certificate.

### [Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool)

A tool represents an action that the CES agent can take to achieve certain goals.

### [ToolCall](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ToolCall)

Request for the client or the agent to execute the specified tool.

### [ToolCalls](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ToolCalls)

Request for the client to execute the tools and return the execution results before continuing the session.

### [ToolFakeConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ToolFakeConfig)

Configuration for tool behavior in fake mode.

### [ToolName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ToolName)

Resource name for the `Tool` resource.

### [ToolResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ToolResponse)

The execution result of a specific tool from the client or the agent.

### [ToolResponses](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ToolResponses)

Execution results for the requested tool calls from the client.

### [ToolService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ToolService)

Tool service provides APIs for interacting with CES tools.

### [ToolService.ToolServiceBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ToolService.ToolServiceBase)

Base class for server-side implementations of ToolService

### [ToolService.ToolServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ToolService.ToolServiceClient)

Client for ToolService

### [ToolServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ToolServiceClient)

ToolService client wrapper, for convenient use.

### [ToolServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ToolServiceClientBuilder)

Builder class for [ToolServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ToolServiceClient) to provide simple configuration of credentials, endpoint etc.

### [ToolServiceClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ToolServiceClientImpl)

ToolService client wrapper implementation, for convenient use.

### [ToolServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ToolServiceSettings)

Settings for [ToolServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ToolServiceClient) instances.

### [Toolset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset)

A toolset represents a group of dynamically managed tools that can be used by the agent.

### [ToolsetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ToolsetName)

Resource name for the `Toolset` resource.

### [ToolsetTool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ToolsetTool)

A tool that is created from a toolset.

### [TransferRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.TransferRule)

Rule for transferring to a specific agent.

### [TransferRule.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.TransferRule.Types)

Container for nested types declared in the TransferRule message type.

### [TransferRule.Types.DeterministicTransfer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.TransferRule.Types.DeterministicTransfer)

Deterministic transfer rule. When the condition evaluates to true, the transfer occurs.

### [TransferRule.Types.DisablePlannerTransfer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.TransferRule.Types.DisablePlannerTransfer)

A rule that prevents the planner from transferring to the target agent.

### [TriggerAction](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.TriggerAction)

Action that is taken when a certain precondition is met.

### [TriggerAction.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.TriggerAction.Types)

Container for nested types declared in the TriggerAction message type.

### [TriggerAction.Types.GenerativeAnswer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.TriggerAction.Types.GenerativeAnswer)

The agent will immediately respond with a generative answer.

### [TriggerAction.Types.RespondImmediately](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.TriggerAction.Types.RespondImmediately)

The agent will immediately respond with a preconfigured response.

### [TriggerAction.Types.Response](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.TriggerAction.Types.Response)

Represents a response from the agent.

### [TriggerAction.Types.TransferAgent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.TriggerAction.Types.TransferAgent)

The agent will transfer the conversation to a different agent.

### [UpdateAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateAgentRequest)

Request message for [AgentService.UpdateAgent][google.cloud.ces.v1beta.AgentService.UpdateAgent].

### [UpdateAppRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateAppRequest)

Request message for [AgentService.UpdateApp][google.cloud.ces.v1beta.AgentService.UpdateApp].

### [UpdateDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateDeploymentRequest)

Request message for [AgentService.UpdateDeployment][google.cloud.ces.v1beta.AgentService.UpdateDeployment].

### [UpdateEvaluationDatasetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateEvaluationDatasetRequest)

Request message for [EvaluationService.UpdateEvaluationDataset][google.cloud.ces.v1beta.EvaluationService.UpdateEvaluationDataset].

### [UpdateEvaluationExpectationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateEvaluationExpectationRequest)

Request message for [EvaluationService.UpdateEvaluationExpectation][google.cloud.ces.v1beta.EvaluationService.UpdateEvaluationExpectation].

### [UpdateEvaluationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateEvaluationRequest)

Request message for [EvaluationService.UpdateEvaluation][google.cloud.ces.v1beta.EvaluationService.UpdateEvaluation].

### [UpdateExampleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateExampleRequest)

Request message for [AgentService.UpdateExample][google.cloud.ces.v1beta.AgentService.UpdateExample].

### [UpdateGuardrailRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateGuardrailRequest)

Request message for [AgentService.UpdateGuardrail][google.cloud.ces.v1beta.AgentService.UpdateGuardrail].

### [UpdateScheduledEvaluationRunRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateScheduledEvaluationRunRequest)

Request message for [EvaluationService.UpdateScheduledEvaluationRun][google.cloud.ces.v1beta.EvaluationService.UpdateScheduledEvaluationRun].

### [UpdateSecuritySettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateSecuritySettingsRequest)

Request message for [AgentService.UpdateSecuritySettings][google.cloud.ces.v1beta.AgentService.UpdateSecuritySettings].

### [UpdateToolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateToolRequest)

Request message for [AgentService.UpdateTool][google.cloud.ces.v1beta.AgentService.UpdateTool].

### [UpdateToolsetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UpdateToolsetRequest)

Request message for [AgentService.UpdateToolset][google.cloud.ces.v1beta.AgentService.UpdateToolset].

### [UploadEvaluationAudioRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UploadEvaluationAudioRequest)

Request message for [EvaluationService.UploadEvaluationAudio][google.cloud.ces.v1beta.EvaluationService.UploadEvaluationAudio].

### [UploadEvaluationAudioResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.UploadEvaluationAudioResponse)

Response message for [EvaluationService.UploadEvaluationAudio][google.cloud.ces.v1beta.EvaluationService.UploadEvaluationAudio].

### [VpcScSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.VpcScSettings)

VPC-SC settings for the app.

### [WebSearchQuery](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.WebSearchQuery)

Represents a single web search query and its associated search uri.

### [WhatsAppCredentials](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.WhatsAppCredentials)

Ephemeral Meta credentials for WhatsApp native integration.

### [WidgetService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.WidgetService)

Provides APIs for widgets to interact with CES APIs.

### [WidgetService.WidgetServiceBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.WidgetService.WidgetServiceBase)

Base class for server-side implementations of WidgetService

### [WidgetService.WidgetServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.WidgetService.WidgetServiceClient)

Client for WidgetService

### [WidgetServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.WidgetServiceClient)

WidgetService client wrapper, for convenient use.

### [WidgetServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.WidgetServiceClientBuilder)

Builder class for [WidgetServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.WidgetServiceClient) to provide simple configuration of credentials, endpoint etc.

### [WidgetServiceClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.WidgetServiceClientImpl)

WidgetService client wrapper implementation, for convenient use.

### [WidgetServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.WidgetServiceSettings)

Settings for [WidgetServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.WidgetServiceClient) instances.

### [WidgetTool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.WidgetTool)

Represents a widget tool that the agent can invoke. When the tool is chosen by the agent, agent will return the widget to the client. The client is responsible for processing the widget and generating the next user query to continue the interaction with the agent.

### [WidgetTool.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.WidgetTool.Types)

Container for nested types declared in the WidgetTool message type.

### [WidgetTool.Types.DataMapping](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.WidgetTool.Types.DataMapping)

Configuration for mapping data from a source tool to the widget's input parameters.

### [WidgetTool.Types.DataMapping.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.WidgetTool.Types.DataMapping.Types)

Container for nested types declared in the DataMapping message type.

### [WidgetTool.Types.TextResponseConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.WidgetTool.Types.TextResponseConfig)

Configuration for the text response returned with the widget.

### [WidgetTool.Types.TextResponseConfig.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.WidgetTool.Types.TextResponseConfig.Types)

Container for nested types declared in the TextResponseConfig message type.

## Enums 

### [Action.ActionSpecOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Action.ActionSpecOneofCase)

Enum of possible cases for the "action_spec" oneof.

### [Action.Types.EntityOperation.Types.OperationType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Action.Types.EntityOperation.Types.OperationType)

The operation to perform on the entity.

### [Agent.AgentTypeOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Agent.AgentTypeOneofCase)

Enum of possible cases for the "agent_type" oneof.

### [AgentName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AgentName.ResourceNameType)

The possible contents of [AgentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AgentName).

### [AmbientSoundConfig.SourceOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AmbientSoundConfig.SourceOneofCase)

Enum of possible cases for the "source" oneof.

### [AmbientSoundConfig.Types.PrebuiltAmbientNoise](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AmbientSoundConfig.Types.PrebuiltAmbientNoise)

Prebuilt ambient noise.

### [ApiAuthentication.AuthConfigOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ApiAuthentication.AuthConfigOneofCase)

Enum of possible cases for the "auth_config" oneof.

### [ApiKeyConfig.Types.RequestLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ApiKeyConfig.Types.RequestLocation)

The location of the API key in the request.

### [App.Types.ToolExecutionMode](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App.Types.ToolExecutionMode)

Defines the tool execution behavior if there are **multiple** tools being selected by the agent **at the same time**.

### [AppName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName.ResourceNameType)

The possible contents of [AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName).

### [AppVersionName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersionName.ResourceNameType)

The possible contents of [AppVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppVersionName).

### [AudioEncoding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AudioEncoding)

AudioEncoding specifies the encoding format for audio data.

### [BidiSessionClientMessage.MessageTypeOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.BidiSessionClientMessage.MessageTypeOneofCase)

Enum of possible cases for the "message_type" oneof.

### [BidiSessionServerMessage.MessageTypeOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.BidiSessionServerMessage.MessageTypeOneofCase)

Enum of possible cases for the "message_type" oneof.

### [Callback.CallbackOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Callback.CallbackOneofCase)

Enum of possible cases for the "callback" oneof.

### [ChangelogName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ChangelogName.ResourceNameType)

The possible contents of [ChangelogName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ChangelogName).

### [ChannelProfile.Types.ChannelType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ChannelProfile.Types.ChannelType)

The type of the channel profile.

### [ChannelProfile.Types.PersonaProperty.Types.Persona](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ChannelProfile.Types.PersonaProperty.Types.Persona)

The persona of the channel.

### [ChannelProfile.Types.WebWidgetConfig.Types.Modality](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ChannelProfile.Types.WebWidgetConfig.Types.Modality)

Modality of the web widget.

### [ChannelProfile.Types.WebWidgetConfig.Types.Theme](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ChannelProfile.Types.WebWidgetConfig.Types.Theme)

Theme of the web widget.

### [Chunk.DataOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Chunk.DataOneofCase)

Enum of possible cases for the "data" oneof.

### [Conversation.Types.ChannelType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Conversation.Types.ChannelType)

The channel type of the conversation.

### [Conversation.Types.InputType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Conversation.Types.InputType)

Type of the input message.

### [Conversation.Types.Source](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Conversation.Types.Source)

The source of the conversation.

### [ConversationName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ConversationName.ResourceNameType)

The possible contents of [ConversationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ConversationName).

### [DataStore.Types.DataStoreType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DataStore.Types.DataStoreType)

The type of the data store.

### [DataStore.Types.DocumentProcessingMode](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DataStore.Types.DocumentProcessingMode)

The document processing mode of the data store.

### [DataStoreSettings.Types.Engine.Types.Type](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DataStoreSettings.Types.Engine.Types.Type)

The type of the engine. See the documentation available at <https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/SolutionType> and <https://cloud.google.com/generative-ai-app-builder/docs/create-datastore-ingest>.

### [DataStoreTool.SearchSourceOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DataStoreTool.SearchSourceOneofCase)

Enum of possible cases for the "search_source" oneof.

### [DataStoreTool.Types.BoostSpec.Types.ConditionBoostSpec.Types.BoostControlSpec.Types.AttributeType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DataStoreTool.Types.BoostSpec.Types.ConditionBoostSpec.Types.BoostControlSpec.Types.AttributeType)

The attribute(or function) for which the custom ranking is to be applied.

### [DataStoreTool.Types.BoostSpec.Types.ConditionBoostSpec.Types.BoostControlSpec.Types.InterpolationType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DataStoreTool.Types.BoostSpec.Types.ConditionBoostSpec.Types.BoostControlSpec.Types.InterpolationType)

The interpolation type to be applied. Default will be linear (Piecewise Linear).

### [DataStoreTool.Types.FilterParameterBehavior](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DataStoreTool.Types.FilterParameterBehavior)

Filter parameter behavior.

### [DataStoreTool.Types.ModalityConfig.Types.ModalityType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DataStoreTool.Types.ModalityConfig.Types.ModalityType)

The modality type.

### [DatasetName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DatasetName.ResourceNameType)

The possible contents of [DatasetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DatasetName).

### [DeidentifyTemplateName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeidentifyTemplateName.ResourceNameType)

The possible contents of [DeidentifyTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeidentifyTemplateName).

### [DeploymentName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeploymentName.ResourceNameType)

The possible contents of [DeploymentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeploymentName).

### [DialogflowAgentName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DialogflowAgentName.ResourceNameType)

The possible contents of [DialogflowAgentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DialogflowAgentName).

### [EndUserAuthConfig.AuthConfigOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EndUserAuthConfig.AuthConfigOneofCase)

Enum of possible cases for the "auth_config" oneof.

### [EndpointControlPolicy.Types.EnforcementScope](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EndpointControlPolicy.Types.EnforcementScope)

Defines the scope in which this policy's allowed_origins list is enforced.

### [EngineName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EngineName.ResourceNameType)

The possible contents of [EngineName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EngineName).

### [ErrorHandlingSettings.Types.ErrorHandlingStrategy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ErrorHandlingSettings.Types.ErrorHandlingStrategy)

Defines the strategy for handling errors.

### [Evaluation.InputsOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Evaluation.InputsOneofCase)

Enum of possible cases for the "inputs" oneof.

### [Evaluation.Types.GoldenExpectation.ConditionOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Evaluation.Types.GoldenExpectation.ConditionOneofCase)

Enum of possible cases for the "condition" oneof.

### [Evaluation.Types.Scenario.Types.TaskCompletionBehavior](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Evaluation.Types.Scenario.Types.TaskCompletionBehavior)

The expected behavior of the user task. This is used to determine whether the scenario is successful.

### [Evaluation.Types.Scenario.Types.UserGoalBehavior](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Evaluation.Types.Scenario.Types.UserGoalBehavior)

The expected behavior of the user goal. This is used to determine whether the scenario is successful.

### [Evaluation.Types.ScenarioExpectation.ExpectationOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Evaluation.Types.ScenarioExpectation.ExpectationOneofCase)

Enum of possible cases for the "expectation" oneof.

### [Evaluation.Types.Step.StepOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Evaluation.Types.Step.StepOneofCase)

Enum of possible cases for the "step" oneof.

### [EvaluationConfig.Types.EvaluationChannel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationConfig.Types.EvaluationChannel)

The channel to evaluate.

### [EvaluationDatasetName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationDatasetName.ResourceNameType)

The possible contents of [EvaluationDatasetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationDatasetName).

### [EvaluationErrorInfo.Types.ErrorType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationErrorInfo.Types.ErrorType)

The type of error

### [EvaluationExpectation.CriteriaOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationExpectation.CriteriaOneofCase)

Enum of possible cases for the "criteria" oneof.

### [EvaluationExpectationName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationExpectationName.ResourceNameType)

The possible contents of [EvaluationExpectationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationExpectationName).

### [EvaluationMetricsConfig.Types.ComparisonType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationMetricsConfig.Types.ComparisonType)

Supported comparison types for checking the agent's response.

### [EvaluationMetricsThresholds.Types.GoldenEvaluationMetricsThresholds.Types.TurnLevelMetricsThresholds.Types.SemanticSimilarityChannel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationMetricsThresholds.Types.GoldenEvaluationMetricsThresholds.Types.TurnLevelMetricsThresholds.Types.SemanticSimilarityChannel)

Semantic similarity channel to use.

### [EvaluationMetricsThresholds.Types.HallucinationMetricBehavior](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationMetricsThresholds.Types.HallucinationMetricBehavior)

The hallucination metric behavior. Regardless of the behavior, the metric will always be calculated. The difference is that when disabled, the metric is not used to calculate the overall evaluation score.

### [EvaluationMetricsThresholds.Types.ToolMatchingSettings.Types.ExtraToolCallBehavior](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationMetricsThresholds.Types.ToolMatchingSettings.Types.ExtraToolCallBehavior)

Defines the behavior when an extra tool call is encountered. An extra tool call is a tool call that is present in the execution but does not match any tool call in the golden expectation.

### [EvaluationName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationName.ResourceNameType)

The possible contents of [EvaluationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationName).

### [EvaluationPersona.Types.SpeechConfig.Types.BackgroundEnvironment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationPersona.Types.SpeechConfig.Types.BackgroundEnvironment)

Simulated audio environment.

### [EvaluationResult.ResultOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationResult.ResultOneofCase)

Enum of possible cases for the "result" oneof.

### [EvaluationResult.Types.ExecutionState](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationResult.Types.ExecutionState)

The state of the evaluation result execution.

### [EvaluationResult.Types.GoldenExpectationOutcome.ResultOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationResult.Types.GoldenExpectationOutcome.ResultOneofCase)

Enum of possible cases for the "result" oneof.

### [EvaluationResult.Types.Outcome](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationResult.Types.Outcome)

The outcome of the evaluation or expectation.

### [EvaluationResult.Types.ScenarioExpectationOutcome.ResultOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationResult.Types.ScenarioExpectationOutcome.ResultOneofCase)

Enum of possible cases for the "result" oneof.

### [EvaluationResult.Types.SpanLatency.IdentifierOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationResult.Types.SpanLatency.IdentifierOneofCase)

Enum of possible cases for the "identifier" oneof.

### [EvaluationResult.Types.SpanLatency.Types.Type](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationResult.Types.SpanLatency.Types.Type)

The type of span. Additional values may be added in the future.

### [EvaluationResultName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationResultName.ResourceNameType)

The possible contents of [EvaluationResultName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationResultName).

### [EvaluationRun.Types.EvaluationRunState](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationRun.Types.EvaluationRunState)

The state of the evaluation run.

### [EvaluationRun.Types.EvaluationType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationRun.Types.EvaluationType)

The type of the evaluations in this run. Additional values may be added in the future.

### [EvaluationRunCachingSettings.Types.EvaluationRunCachingMode](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationRunCachingSettings.Types.EvaluationRunCachingMode)

The evaluation result caching behavior. Controls whether to return the last completed evaluation result (if existing) or to execute a new evaluation.

### [EvaluationRunName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationRunName.ResourceNameType)

The possible contents of [EvaluationRunName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationRunName).

### [EvaluationSettings.Types.ScenarioConversationInitiator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationSettings.Types.ScenarioConversationInitiator)

Determines who starts the conversation in a scenario evaluation session.

### [EvaluationSettings.Types.ScenarioExecutionMode](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationSettings.Types.ScenarioExecutionMode)

The execution mode for scenario evaluations.

### [EvaluationToolCallBehaviour](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationToolCallBehaviour)

Configures the tool call behaviour for evaluation runs.

### [ExampleName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ExampleName.ResourceNameType)

The possible contents of [ExampleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ExampleName).

### [ExecuteToolRequest.ToolExecutionContextOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ExecuteToolRequest.ToolExecutionContextOneofCase)

Enum of possible cases for the "tool_execution_context" oneof.

### [ExecuteToolRequest.ToolIdentifierOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ExecuteToolRequest.ToolIdentifierOneofCase)

Enum of possible cases for the "tool_identifier" oneof.

### [ExecuteToolResponse.ToolIdentifierOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ExecuteToolResponse.ToolIdentifierOneofCase)

Enum of possible cases for the "tool_identifier" oneof.

### [ExecutionType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ExecutionType)

The execution type of the tool or toolset.

### [ExperimentConfig.Types.State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ExperimentConfig.Types.State)

State of the experiment.

### [ExportAppRequest.Types.ExportFormat](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ExportAppRequest.Types.ExportFormat)

Export format for the app.

### [ExportAppResponse.AppOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ExportAppResponse.AppOneofCase)

Enum of possible cases for the "app" oneof.

### [ExportEvaluationResultsResponse.EvaluationResultsOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ExportEvaluationResultsResponse.EvaluationResultsOneofCase)

Enum of possible cases for the "evaluation_results" oneof.

### [ExportEvaluationRunsResponse.EvaluationRunsOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ExportEvaluationRunsResponse.EvaluationRunsOneofCase)

Enum of possible cases for the "evaluation_runs" oneof.

### [ExportEvaluationsResponse.EvaluationsOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ExportEvaluationsResponse.EvaluationsOneofCase)

Enum of possible cases for the "evaluations" oneof.

### [ExportOptions.Types.ExportFormat](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ExportOptions.Types.ExportFormat)

The format to export the items in. Defaults to JSON if not specified.

### [FileContext.FileOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.FileContext.FileOneofCase)

Enum of possible cases for the "file" oneof.

### [FileSearchTool.Types.CorpusType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.FileSearchTool.Types.CorpusType)

The type of the Vertex RAG corpus.

### [GenerateAppResourceOperationMetadata.Types.GenerationType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateAppResourceOperationMetadata.Types.GenerationType)

The type of the generation operation.

### [GenerateAppResourceRequest.ResourceOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateAppResourceRequest.ResourceOneofCase)

Enum of possible cases for the "resource" oneof.

### [GenerateAppResourceRequest.Types.QualityReportGenerationConfig.Types.LossAttributionAlgorithm](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateAppResourceRequest.Types.QualityReportGenerationConfig.Types.LossAttributionAlgorithm)

The algorithm to use for loss attribution.

### [GenerateAppResourceResponse.GeneratedResourceOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateAppResourceResponse.GeneratedResourceOneofCase)

Enum of possible cases for the "generated_resource" oneof.

### [GenerateEvaluationRequest.Types.EvaluationType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateEvaluationRequest.Types.EvaluationType)

The type of evaluation to generate.

### [GoldenRunMethod](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GoldenRunMethod)

The method used to run the evaluation.

### [Guardrail.GuardrailTypeOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail.GuardrailTypeOneofCase)

Enum of possible cases for the "guardrail_type" oneof.

### [Guardrail.Types.ContentFilter.Types.MatchType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail.Types.ContentFilter.Types.MatchType)

Match type for the content filter.

### [Guardrail.Types.LlmPolicy.Types.PolicyScope](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail.Types.LlmPolicy.Types.PolicyScope)

Defines when to apply the policy check during the conversation.

### [Guardrail.Types.LlmPromptSecurity.SecurityConfigOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail.Types.LlmPromptSecurity.SecurityConfigOneofCase)

Enum of possible cases for the "security_config" oneof.

### [Guardrail.Types.ModelSafety.Types.HarmBlockThreshold](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail.Types.ModelSafety.Types.HarmBlockThreshold)

Probability based thresholds levels for blocking.

### [Guardrail.Types.ModelSafety.Types.HarmCategory](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Guardrail.Types.ModelSafety.Types.HarmCategory)

Harm category.

### [GuardrailName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GuardrailName.ResourceNameType)

The possible contents of [GuardrailName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GuardrailName).

### [ImportAppRequest.AppOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ImportAppRequest.AppOneofCase)

Enum of possible cases for the "app" oneof.

### [ImportAppRequest.Types.ImportOptions.Types.ConflictResolutionStrategy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ImportAppRequest.Types.ImportOptions.Types.ConflictResolutionStrategy)

Defines the strategy for handling conflicts when an app with the same ID already exists, or when imported resources (like Agents, Tools, etc.) have the same display names as existing resources within that app.

### [ImportEvaluationsRequest.SourceOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ImportEvaluationsRequest.SourceOneofCase)

Enum of possible cases for the "source" oneof.

### [ImportEvaluationsRequest.Types.ImportOptions.Types.ConflictResolutionStrategy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ImportEvaluationsRequest.Types.ImportOptions.Types.ConflictResolutionStrategy)

Defines the strategy for handling conflicts when an evaluation with the same evaluation ID already exists in the app.

### [InspectTemplateName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.InspectTemplateName.ResourceNameType)

The possible contents of [InspectTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.InspectTemplateName).

### [LatencyReport.Types.ToolLatency.ToolIdentifierOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.LatencyReport.Types.ToolLatency.ToolIdentifierOneofCase)

Enum of possible cases for the "tool_identifier" oneof.

### [McpTool.Types.State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.McpTool.Types.State)

Represents the dynamic availability state of the tool.

### [MockConfig.Types.UnmatchedToolCallBehavior](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.MockConfig.Types.UnmatchedToolCallBehavior)

What to do when a tool call doesn't match any mocked tool calls.

### [MockedToolCall.ToolIdentifierOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.MockedToolCall.ToolIdentifierOneofCase)

Enum of possible cases for the "tool_identifier" oneof.

### [OAuthConfig.Types.OauthGrantType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OAuthConfig.Types.OauthGrantType)

OAuth grant types. Only [client credential grant](https://oauth.net/2/grant-types/client-credentials) is supported.

### [OmnichannelIntegrationConfig.Types.ChannelConfig.ChannelConfigOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OmnichannelIntegrationConfig.Types.ChannelConfig.ChannelConfigOneofCase)

Enum of possible cases for the "channel_config" oneof.

### [OmnichannelIntegrationConfig.Types.SubscriberConfig.SubscriberConfigOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OmnichannelIntegrationConfig.Types.SubscriberConfig.SubscriberConfigOneofCase)

Enum of possible cases for the "subscriber_config" oneof.

### [OmnichannelName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OmnichannelName.ResourceNameType)

The possible contents of [OmnichannelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OmnichannelName).

### [OptimizationConfig.Types.OptimizationStatus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.OptimizationConfig.Types.OptimizationStatus)

The status of the optimization run.

### [RetrieveToolSchemaRequest.ToolIdentifierOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.RetrieveToolSchemaRequest.ToolIdentifierOneofCase)

Enum of possible cases for the "tool_identifier" oneof.

### [RetrieveToolSchemaResponse.ToolIdentifierOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.RetrieveToolSchemaResponse.ToolIdentifierOneofCase)

Enum of possible cases for the "tool_identifier" oneof.

### [ScheduledEvaluationRun.Types.SchedulingConfig.Types.Frequency](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ScheduledEvaluationRun.Types.SchedulingConfig.Types.Frequency)

The frequencies evals can be run at

### [ScheduledEvaluationRunName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ScheduledEvaluationRunName.ResourceNameType)

The possible contents of [ScheduledEvaluationRunName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ScheduledEvaluationRunName).

### [Schema.Types.Type](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Schema.Types.Type)

OpenAPI data types.

### [SecretVersionName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SecretVersionName.ResourceNameType)

The possible contents of [SecretVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SecretVersionName).

### [SecuritySettingsName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SecuritySettingsName.ResourceNameType)

The possible contents of [SecuritySettingsName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SecuritySettingsName).

### [ServiceName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ServiceName.ResourceNameType)

The possible contents of [ServiceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ServiceName).

### [SessionInput.InputTypeOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SessionInput.InputTypeOneofCase)

Enum of possible cases for the "input_type" oneof.

### [SessionName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SessionName.ResourceNameType)

The possible contents of [SessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SessionName).

### [SessionOutput.OutputTypeOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.SessionOutput.OutputTypeOneofCase)

Enum of possible cases for the "output_type" oneof.

### [Tool.ToolTypeOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Tool.ToolTypeOneofCase)

Enum of possible cases for the "tool_type" oneof.

### [ToolCall.ToolIdentifierOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ToolCall.ToolIdentifierOneofCase)

Enum of possible cases for the "tool_identifier" oneof.

### [ToolFakeConfig.ToolResponseOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ToolFakeConfig.ToolResponseOneofCase)

Enum of possible cases for the "tool_response" oneof.

### [ToolName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ToolName.ResourceNameType)

The possible contents of [ToolName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ToolName).

### [ToolResponse.ToolIdentifierOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ToolResponse.ToolIdentifierOneofCase)

Enum of possible cases for the "tool_identifier" oneof.

### [Toolset.ToolsetTypeOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Toolset.ToolsetTypeOneofCase)

Enum of possible cases for the "toolset_type" oneof.

### [ToolsetName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ToolsetName.ResourceNameType)

The possible contents of [ToolsetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ToolsetName).

### [TransferRule.RuleTypeOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.TransferRule.RuleTypeOneofCase)

Enum of possible cases for the "rule_type" oneof.

### [TransferRule.Types.DeterministicTransfer.ConditionTypeOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.TransferRule.Types.DeterministicTransfer.ConditionTypeOneofCase)

Enum of possible cases for the "condition_type" oneof.

### [TransferRule.Types.Direction](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.TransferRule.Types.Direction)

The direction of the transfer.

### [TriggerAction.ActionOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.TriggerAction.ActionOneofCase)

Enum of possible cases for the "action" oneof.

### [WidgetTool.InputOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.WidgetTool.InputOneofCase)

Enum of possible cases for the "input" oneof.

### [WidgetTool.Types.DataMapping.Types.Mode](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.WidgetTool.Types.DataMapping.Types.Mode)

The strategy used to map data from the source tool to the widget.

### [WidgetTool.Types.TextResponseConfig.Types.Type](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.WidgetTool.Types.TextResponseConfig.Types.Type)

Defines how the text response is produced.

### [WidgetTool.Types.WidgetType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.WidgetTool.Types.WidgetType)

All available widget types. New values may be added to this enum in the future.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-14 UTC."],[],[]] 
