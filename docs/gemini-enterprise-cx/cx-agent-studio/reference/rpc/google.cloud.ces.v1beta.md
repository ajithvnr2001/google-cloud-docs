---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta
title: Package google.cloud.ces.v1beta \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:58:38.148569+00:00
---

# Package google.cloud.ces.v1beta  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Package google.cloud.ces.v1beta Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[AgentService](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService)` (interface)
  * `[EvaluationService](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationService)` (interface)
  * `[SessionService](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.SessionService)` (interface)
  * `[ToolService](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ToolService)` (interface)
  * `[WidgetService](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.WidgetService)` (interface)
  * `[Action](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Action)` (message)
  * `[Action.EntityOperation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Action.EntityOperation)` (message)
  * `[Action.EntityOperation.OperationType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Action.EntityOperation.OperationType)` (enum)
  * `[Agent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Agent)` (message)
  * `[Agent.AgentToolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Agent.AgentToolset)` (message)
  * `[Agent.LlmAgent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Agent.LlmAgent)` (message)
  * `[Agent.RemoteA2aAgent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Agent.RemoteA2aAgent)` (message)
  * `[Agent.RemoteDialogflowAgent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Agent.RemoteDialogflowAgent)` (message)
  * `[AgentCard](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentCard)` (message)
  * `[AgentInterface](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentInterface)` (message)
  * `[AgentRegistryDeployment](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentRegistryDeployment)` (message)
  * `[AgentSkill](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentSkill)` (message)
  * `[AgentTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentTool)` (message)
  * `[AgentTransfer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentTransfer)` (message)
  * `[AggregatedMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AggregatedMetrics)` (message)
  * `[AggregatedMetrics.HallucinationMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AggregatedMetrics.HallucinationMetrics)` (message)
  * `[AggregatedMetrics.MetricsByAppVersion](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AggregatedMetrics.MetricsByAppVersion)` (message)
  * `[AggregatedMetrics.MetricsByTurn](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AggregatedMetrics.MetricsByTurn)` (message)
  * `[AggregatedMetrics.SemanticSimilarityMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AggregatedMetrics.SemanticSimilarityMetrics)` (message)
  * `[AggregatedMetrics.ToolCallLatencyMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AggregatedMetrics.ToolCallLatencyMetrics)` (message)
  * `[AggregatedMetrics.ToolMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AggregatedMetrics.ToolMetrics)` (message)
  * `[AggregatedMetrics.TurnLatencyMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AggregatedMetrics.TurnLatencyMetrics)` (message)
  * `[AmbientSoundConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AmbientSoundConfig)` (message)
  * `[AmbientSoundConfig.PrebuiltAmbientNoise](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AmbientSoundConfig.PrebuiltAmbientNoise)` (enum)
  * `[ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ApiAuthentication)` (message)
  * `[ApiKeyConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ApiKeyConfig)` (message)
  * `[ApiKeyConfig.RequestLocation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ApiKeyConfig.RequestLocation)` (enum)
  * `[App](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.App)` (message)
  * `[App.ToolExecutionMode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.App.ToolExecutionMode)` (enum)
  * `[App.VariableDeclaration](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.App.VariableDeclaration)` (message)
  * `[AppSnapshot](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AppSnapshot)` (message)
  * `[AppVersion](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AppVersion)` (message)
  * `[AudioEncoding](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AudioEncoding)` (enum)
  * `[AudioProcessingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AudioProcessingConfig)` (message)
  * `[AudioRecordingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AudioRecordingConfig)` (message)
  * `[BargeInConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.BargeInConfig)` (message)
  * `[BatchDeleteConversationsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.BatchDeleteConversationsRequest)` (message)
  * `[BatchDeleteConversationsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.BatchDeleteConversationsResponse)` (message)
  * `[BearerTokenConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.BearerTokenConfig)` (message)
  * `[BidiSessionClientMessage](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.BidiSessionClientMessage)` (message)
  * `[BidiSessionServerMessage](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.BidiSessionServerMessage)` (message)
  * `[BigQueryExportSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.BigQueryExportSettings)` (message)
  * `[Blob](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Blob)` (message)
  * `[Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Callback)` (message)
  * `[Changelog](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Changelog)` (message)
  * `[ChannelProfile](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ChannelProfile)` (message)
  * `[ChannelProfile.ChannelType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ChannelProfile.ChannelType)` (enum)
  * `[ChannelProfile.InstagramConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ChannelProfile.InstagramConfig)` (message)
  * `[ChannelProfile.PersonaProperty](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ChannelProfile.PersonaProperty)` (message)
  * `[ChannelProfile.PersonaProperty.Persona](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ChannelProfile.PersonaProperty.Persona)` (enum)
  * `[ChannelProfile.WebWidgetConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ChannelProfile.WebWidgetConfig)` (message)
  * `[ChannelProfile.WebWidgetConfig.Modality](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ChannelProfile.WebWidgetConfig.Modality)` (enum)
  * `[ChannelProfile.WebWidgetConfig.SecuritySettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ChannelProfile.WebWidgetConfig.SecuritySettings)` (message)
  * `[ChannelProfile.WebWidgetConfig.Theme](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ChannelProfile.WebWidgetConfig.Theme)` (enum)
  * `[ChannelProfile.WhatsAppConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ChannelProfile.WhatsAppConfig)` (message)
  * `[Chunk](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Chunk)` (message)
  * `[Citations](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Citations)` (message)
  * `[Citations.CitedChunk](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Citations.CitedChunk)` (message)
  * `[Citations.InlineCitation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Citations.InlineCitation)` (message)
  * `[ClientCertificateSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ClientCertificateSettings)` (message)
  * `[ClientFunction](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ClientFunction)` (message)
  * `[CloudLoggingSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.CloudLoggingSettings)` (message)
  * `[CodeBlock](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.CodeBlock)` (message)
  * `[ConnectorTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ConnectorTool)` (message)
  * `[ConnectorToolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ConnectorToolset)` (message)
  * `[Conversation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Conversation)` (message)
  * `[Conversation.ChannelType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Conversation.ChannelType)` (enum)
  * `[Conversation.InputType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Conversation.InputType)` (enum)
  * `[Conversation.Source](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Conversation.Source)` (enum)
  * `[Conversation.Turn](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Conversation.Turn)` (message)
  * `[ConversationLoggingSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ConversationLoggingSettings)` (message)
  * `[CreateAgentRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.CreateAgentRequest)` (message)
  * `[CreateAppRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.CreateAppRequest)` (message)
  * `[CreateAppVersionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.CreateAppVersionRequest)` (message)
  * `[CreateDeploymentRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.CreateDeploymentRequest)` (message)
  * `[CreateEvaluationDatasetRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.CreateEvaluationDatasetRequest)` (message)
  * `[CreateEvaluationExpectationRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.CreateEvaluationExpectationRequest)` (message)
  * `[CreateEvaluationRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.CreateEvaluationRequest)` (message)
  * `[CreateExampleRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.CreateExampleRequest)` (message)
  * `[CreateGuardrailRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.CreateGuardrailRequest)` (message)
  * `[CreateScheduledEvaluationRunRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.CreateScheduledEvaluationRunRequest)` (message)
  * `[CreateToolRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.CreateToolRequest)` (message)
  * `[CreateToolsetRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.CreateToolsetRequest)` (message)
  * `[CustomVoiceSample](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.CustomVoiceSample)` (message)
  * `[CustomVoiceSample.VoiceInstructionMode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.CustomVoiceSample.VoiceInstructionMode)` (enum)
  * `[CustomVoiceSample.Warning](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.CustomVoiceSample.Warning)` (message)
  * `[CustomVoiceSample.Warning.WarningType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.CustomVoiceSample.Warning.WarningType)` (enum)
  * `[DashboardSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DashboardSettings)` (message)
  * `[DataStore](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DataStore)` (message)
  * `[DataStore.ConnectorConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DataStore.ConnectorConfig)` (message)
  * `[DataStore.DataStoreType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DataStore.DataStoreType)` (enum)
  * `[DataStore.DocumentProcessingMode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DataStore.DocumentProcessingMode)` (enum)
  * `[DataStoreSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DataStoreSettings)` (message)
  * `[DataStoreSettings.Engine](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DataStoreSettings.Engine)` (message)
  * `[DataStoreSettings.Engine.Type](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DataStoreSettings.Engine.Type)` (enum)
  * `[DataStoreTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DataStoreTool)` (message)
  * `[DataStoreTool.BoostSpec](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DataStoreTool.BoostSpec)` (message)
  * `[DataStoreTool.BoostSpec.ConditionBoostSpec](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DataStoreTool.BoostSpec.ConditionBoostSpec)` (message)
  * `[DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec)` (message)
  * `[DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec.AttributeType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec.AttributeType)` (enum)
  * `[DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec.ControlPoint](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec.ControlPoint)` (message)
  * `[DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec.InterpolationType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec.InterpolationType)` (enum)
  * `[DataStoreTool.BoostSpecs](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DataStoreTool.BoostSpecs)` (message)
  * `[DataStoreTool.DataStoreSource](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DataStoreTool.DataStoreSource)` (message)
  * `[DataStoreTool.EngineSource](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DataStoreTool.EngineSource)` (message)
  * `[DataStoreTool.FilterParameterBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DataStoreTool.FilterParameterBehavior)` (enum)
  * `[DataStoreTool.GroundingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DataStoreTool.GroundingConfig)` (message)
  * `[DataStoreTool.ModalityConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DataStoreTool.ModalityConfig)` (message)
  * `[DataStoreTool.ModalityConfig.ModalityType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DataStoreTool.ModalityConfig.ModalityType)` (enum)
  * `[DataStoreTool.RewriterConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DataStoreTool.RewriterConfig)` (message)
  * `[DataStoreTool.SnippetsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DataStoreTool.SnippetsConfig)` (message)
  * `[DataStoreTool.SummarizationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DataStoreTool.SummarizationConfig)` (message)
  * `[DeleteAgentRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DeleteAgentRequest)` (message)
  * `[DeleteAppRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DeleteAppRequest)` (message)
  * `[DeleteAppVersionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DeleteAppVersionRequest)` (message)
  * `[DeleteConversationRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DeleteConversationRequest)` (message)
  * `[DeleteDeploymentRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DeleteDeploymentRequest)` (message)
  * `[DeleteEvaluationDatasetRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DeleteEvaluationDatasetRequest)` (message)
  * `[DeleteEvaluationExpectationRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DeleteEvaluationExpectationRequest)` (message)
  * `[DeleteEvaluationRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DeleteEvaluationRequest)` (message)
  * `[DeleteEvaluationResultRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DeleteEvaluationResultRequest)` (message)
  * `[DeleteEvaluationRunOperationMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DeleteEvaluationRunOperationMetadata)` (message)
  * `[DeleteEvaluationRunRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DeleteEvaluationRunRequest)` (message)
  * `[DeleteExampleRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DeleteExampleRequest)` (message)
  * `[DeleteGuardrailRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DeleteGuardrailRequest)` (message)
  * `[DeleteScheduledEvaluationRunRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DeleteScheduledEvaluationRunRequest)` (message)
  * `[DeleteToolRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DeleteToolRequest)` (message)
  * `[DeleteToolsetRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DeleteToolsetRequest)` (message)
  * `[DeployChannelResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DeployChannelResponse)` (message)
  * `[Deployment](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Deployment)` (message)
  * `[Deployment.Modality](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Deployment.Modality)` (enum)
  * `[EndSession](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EndSession)` (message)
  * `[EndUserAuthConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EndUserAuthConfig)` (message)
  * `[EndUserAuthConfig.Oauth2AuthCodeConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EndUserAuthConfig.Oauth2AuthCodeConfig)` (message)
  * `[EndUserAuthConfig.Oauth2JwtBearerConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EndUserAuthConfig.Oauth2JwtBearerConfig)` (message)
  * `[EndpointControlPolicy](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EndpointControlPolicy)` (message)
  * `[EndpointControlPolicy.EnforcementScope](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EndpointControlPolicy.EnforcementScope)` (enum)
  * `[ErrorHandlingSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ErrorHandlingSettings)` (message)
  * `[ErrorHandlingSettings.EndSessionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ErrorHandlingSettings.EndSessionConfig)` (message)
  * `[ErrorHandlingSettings.ErrorHandlingStrategy](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ErrorHandlingSettings.ErrorHandlingStrategy)` (enum)
  * `[ErrorHandlingSettings.FallbackResponseConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ErrorHandlingSettings.FallbackResponseConfig)` (message)
  * `[Evaluation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Evaluation)` (message)
  * `[Evaluation.Golden](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Evaluation.Golden)` (message)
  * `[Evaluation.GoldenExpectation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Evaluation.GoldenExpectation)` (message)
  * `[Evaluation.GoldenTurn](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Evaluation.GoldenTurn)` (message)
  * `[Evaluation.Scenario](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Evaluation.Scenario)` (message)
  * `[Evaluation.Scenario.TaskCompletionBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Evaluation.Scenario.TaskCompletionBehavior)` (enum)
  * `[Evaluation.Scenario.UserFact](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Evaluation.Scenario.UserFact)` (message)
  * `[Evaluation.Scenario.UserGoalBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Evaluation.Scenario.UserGoalBehavior)` (enum)
  * `[Evaluation.ScenarioExpectation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Evaluation.ScenarioExpectation)` (message)
  * `[Evaluation.ScenarioExpectation.ToolExpectation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Evaluation.ScenarioExpectation.ToolExpectation)` (message)
  * `[Evaluation.Step](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Evaluation.Step)` (message)
  * `[EvaluationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationConfig)` (message)
  * `[EvaluationConfig.EvaluationChannel](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationConfig.EvaluationChannel)` (enum)
  * `[EvaluationDataset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationDataset)` (message)
  * `[EvaluationErrorInfo](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationErrorInfo)` (message)
  * `[EvaluationErrorInfo.ErrorType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationErrorInfo.ErrorType)` (enum)
  * `[EvaluationExpectation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationExpectation)` (message)
  * `[EvaluationExpectation.LlmCriteria](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationExpectation.LlmCriteria)` (message)
  * `[EvaluationMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationMetricsConfig)` (message)
  * `[EvaluationMetricsConfig.ComparisonType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationMetricsConfig.ComparisonType)` (enum)
  * `[EvaluationMetricsConfig.ExpectationsMetMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationMetricsConfig.ExpectationsMetMetricsConfig)` (message)
  * `[EvaluationMetricsConfig.GoldenMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationMetricsConfig.GoldenMetricsConfig)` (message)
  * `[EvaluationMetricsConfig.HallucinationMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationMetricsConfig.HallucinationMetricsConfig)` (message)
  * `[EvaluationMetricsConfig.ScenarioMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationMetricsConfig.ScenarioMetricsConfig)` (message)
  * `[EvaluationMetricsConfig.SemanticSimilarityMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationMetricsConfig.SemanticSimilarityMetricsConfig)` (message)
  * `[EvaluationMetricsConfig.ToolCorrectnessMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationMetricsConfig.ToolCorrectnessMetricsConfig)` (message)
  * `[EvaluationMetricsConfig.UserGoalMetMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationMetricsConfig.UserGoalMetMetricsConfig)` (message)
  * `[EvaluationMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationMetricsThresholds)` (message)
  * `[EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds)` (message)
  * `[EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.ExpectationLevelMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.ExpectationLevelMetricsThresholds)` (message)
  * `[EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.TurnLevelMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.TurnLevelMetricsThresholds)` (message)
  * `[EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.TurnLevelMetricsThresholds.SemanticSimilarityChannel](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.TurnLevelMetricsThresholds.SemanticSimilarityChannel)` (enum)
  * `[EvaluationMetricsThresholds.HallucinationMetricBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationMetricsThresholds.HallucinationMetricBehavior)` (enum)
  * `[EvaluationMetricsThresholds.ToolMatchingSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationMetricsThresholds.ToolMatchingSettings)` (message)
  * `[EvaluationMetricsThresholds.ToolMatchingSettings.ExtraToolCallBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationMetricsThresholds.ToolMatchingSettings.ExtraToolCallBehavior)` (enum)
  * `[EvaluationPersona](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationPersona)` (message)
  * `[EvaluationPersona.SpeechConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationPersona.SpeechConfig)` (message)
  * `[EvaluationPersona.SpeechConfig.BackgroundEnvironment](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationPersona.SpeechConfig.BackgroundEnvironment)` (enum)
  * `[EvaluationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationResult)` (message)
  * `[EvaluationResult.EvaluationExpectationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationResult.EvaluationExpectationResult)` (message)
  * `[EvaluationResult.ExecutionState](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationResult.ExecutionState)` (enum)
  * `[EvaluationResult.GoldenExpectationOutcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationResult.GoldenExpectationOutcome)` (message)
  * `[EvaluationResult.GoldenExpectationOutcome.ToolInvocationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationResult.GoldenExpectationOutcome.ToolInvocationResult)` (message)
  * `[EvaluationResult.GoldenResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationResult.GoldenResult)` (message)
  * `[EvaluationResult.GoldenResult.TurnReplayResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationResult.GoldenResult.TurnReplayResult)` (message)
  * `[EvaluationResult.HallucinationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationResult.HallucinationResult)` (message)
  * `[EvaluationResult.Outcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationResult.Outcome)` (enum)
  * `[EvaluationResult.OutcomeMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationResult.OutcomeMetadata)` (enum)
  * `[EvaluationResult.OverallToolInvocationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationResult.OverallToolInvocationResult)` (message)
  * `[EvaluationResult.ScenarioExpectationOutcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationResult.ScenarioExpectationOutcome)` (message)
  * `[EvaluationResult.ScenarioExpectationOutcome.ObservedToolCall](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationResult.ScenarioExpectationOutcome.ObservedToolCall)` (message)
  * `[EvaluationResult.ScenarioResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationResult.ScenarioResult)` (message)
  * `[EvaluationResult.ScenarioRubricOutcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationResult.ScenarioRubricOutcome)` (message)
  * `[EvaluationResult.SemanticSimilarityResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationResult.SemanticSimilarityResult)` (message)
  * `[EvaluationResult.SpanLatency](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationResult.SpanLatency)` (message)
  * `[EvaluationResult.SpanLatency.Type](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationResult.SpanLatency.Type)` (enum)
  * `[EvaluationResult.TaskCompletionResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationResult.TaskCompletionResult)` (message)
  * `[EvaluationResult.ToolCallLatency](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationResult.ToolCallLatency)` (message)
  * `[EvaluationResult.UserGoalSatisfactionResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationResult.UserGoalSatisfactionResult)` (message)
  * `[EvaluationRun](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationRun)` (message)
  * `[EvaluationRun.EvaluationRunState](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationRun.EvaluationRunState)` (enum)
  * `[EvaluationRun.EvaluationRunSummary](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationRun.EvaluationRunSummary)` (message)
  * `[EvaluationRun.EvaluationType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationRun.EvaluationType)` (enum)
  * `[EvaluationRun.Progress](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationRun.Progress)` (message)
  * `[EvaluationRunCachingSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationRunCachingSettings)` (message)
  * `[EvaluationRunCachingSettings.EvaluationRunCachingMode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationRunCachingSettings.EvaluationRunCachingMode)` (enum)
  * `[EvaluationSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationSettings)` (message)
  * `[EvaluationSettings.ScenarioConversationInitiator](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationSettings.ScenarioConversationInitiator)` (enum)
  * `[EvaluationSettings.ScenarioExecutionMode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationSettings.ScenarioExecutionMode)` (enum)
  * `[EvaluationToolCallBehaviour](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationToolCallBehaviour)` (enum)
  * `[Event](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Event)` (message)
  * `[Example](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Example)` (message)
  * `[ExecuteToolRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ExecuteToolRequest)` (message)
  * `[ExecuteToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ExecuteToolResponse)` (message)
  * `[ExecutionType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ExecutionType)` (enum)
  * `[ExperimentConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ExperimentConfig)` (message)
  * `[ExperimentConfig.State](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ExperimentConfig.State)` (enum)
  * `[ExperimentConfig.VersionRelease](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ExperimentConfig.VersionRelease)` (message)
  * `[ExperimentConfig.VersionRelease.TrafficAllocation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ExperimentConfig.VersionRelease.TrafficAllocation)` (message)
  * `[ExportAppRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ExportAppRequest)` (message)
  * `[ExportAppRequest.ExportFormat](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ExportAppRequest.ExportFormat)` (enum)
  * `[ExportAppResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ExportAppResponse)` (message)
  * `[ExportEvaluationResultsOperationMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ExportEvaluationResultsOperationMetadata)` (message)
  * `[ExportEvaluationResultsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ExportEvaluationResultsRequest)` (message)
  * `[ExportEvaluationResultsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ExportEvaluationResultsResponse)` (message)
  * `[ExportEvaluationRunsOperationMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ExportEvaluationRunsOperationMetadata)` (message)
  * `[ExportEvaluationRunsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ExportEvaluationRunsRequest)` (message)
  * `[ExportEvaluationRunsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ExportEvaluationRunsResponse)` (message)
  * `[ExportEvaluationsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ExportEvaluationsRequest)` (message)
  * `[ExportEvaluationsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ExportEvaluationsResponse)` (message)
  * `[ExportOptions](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ExportOptions)` (message)
  * `[ExportOptions.ExportFormat](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ExportOptions.ExportFormat)` (enum)
  * `[ExpressionCondition](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ExpressionCondition)` (message)
  * `[FileContext](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.FileContext)` (message)
  * `[FileContext.FileBytes](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.FileContext.FileBytes)` (message)
  * `[FileSearchTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.FileSearchTool)` (message)
  * `[FileSearchTool.CorpusType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.FileSearchTool.CorpusType)` (enum)
  * `[GenerateAppResourceOperationMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GenerateAppResourceOperationMetadata)` (message)
  * `[GenerateAppResourceOperationMetadata.GenerationType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GenerateAppResourceOperationMetadata.GenerationType)` (enum)
  * `[GenerateAppResourceRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GenerateAppResourceRequest)` (message)
  * `[GenerateAppResourceRequest.AppGenerationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GenerateAppResourceRequest.AppGenerationConfig)` (message)
  * `[GenerateAppResourceRequest.AppVersionContext](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GenerateAppResourceRequest.AppVersionContext)` (message)
  * `[GenerateAppResourceRequest.EvaluationGenerationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GenerateAppResourceRequest.EvaluationGenerationConfig)` (message)
  * `[GenerateAppResourceRequest.EvaluationPersonasGenerationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GenerateAppResourceRequest.EvaluationPersonasGenerationConfig)` (message)
  * `[GenerateAppResourceRequest.HillClimbingFixConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GenerateAppResourceRequest.HillClimbingFixConfig)` (message)
  * `[GenerateAppResourceRequest.QualityReportGenerationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GenerateAppResourceRequest.QualityReportGenerationConfig)` (message)
  * `[GenerateAppResourceRequest.QualityReportGenerationConfig.LossAttributionAlgorithm](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GenerateAppResourceRequest.QualityReportGenerationConfig.LossAttributionAlgorithm)` (enum)
  * `[GenerateAppResourceRequest.RefineInstructions](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GenerateAppResourceRequest.RefineInstructions)` (message)
  * `[GenerateAppResourceRequest.ToolGenerationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GenerateAppResourceRequest.ToolGenerationConfig)` (message)
  * `[GenerateAppResourceRequest.ToolGenerationConfig.OpenApiToolsetGenerationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GenerateAppResourceRequest.ToolGenerationConfig.OpenApiToolsetGenerationConfig)` (message)
  * `[GenerateAppResourceRequest.ToolGenerationConfig.OpenApiToolsetGenerationConfig.OperationGenerationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GenerateAppResourceRequest.ToolGenerationConfig.OpenApiToolsetGenerationConfig.OperationGenerationConfig)` (message)
  * `[GenerateAppResourceResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GenerateAppResourceResponse)` (message)
  * `[GenerateAppResourceResponse.AppResources](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GenerateAppResourceResponse.AppResources)` (message)
  * `[GenerateAppResourceResponse.Evaluations](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GenerateAppResourceResponse.Evaluations)` (message)
  * `[GenerateAppResourceResponse.GenerateResultInfo](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GenerateAppResourceResponse.GenerateResultInfo)` (message)
  * `[GenerateAppResourceResponse.Tools](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GenerateAppResourceResponse.Tools)` (message)
  * `[GenerateChatTokenRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GenerateChatTokenRequest)` (message)
  * `[GenerateChatTokenResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GenerateChatTokenResponse)` (message)
  * `[GenerateEvaluationOperationMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GenerateEvaluationOperationMetadata)` (message)
  * `[GenerateEvaluationRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GenerateEvaluationRequest)` (message)
  * `[GenerateEvaluationRequest.EvaluationType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GenerateEvaluationRequest.EvaluationType)` (enum)
  * `[GetAgentRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GetAgentRequest)` (message)
  * `[GetAppRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GetAppRequest)` (message)
  * `[GetAppVersionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GetAppVersionRequest)` (message)
  * `[GetChangelogRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GetChangelogRequest)` (message)
  * `[GetConversationRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GetConversationRequest)` (message)
  * `[GetDeploymentRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GetDeploymentRequest)` (message)
  * `[GetEvaluationDatasetRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GetEvaluationDatasetRequest)` (message)
  * `[GetEvaluationExpectationRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GetEvaluationExpectationRequest)` (message)
  * `[GetEvaluationRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GetEvaluationRequest)` (message)
  * `[GetEvaluationResultRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GetEvaluationResultRequest)` (message)
  * `[GetEvaluationRunRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GetEvaluationRunRequest)` (message)
  * `[GetExampleRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GetExampleRequest)` (message)
  * `[GetGuardrailRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GetGuardrailRequest)` (message)
  * `[GetScheduledEvaluationRunRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GetScheduledEvaluationRunRequest)` (message)
  * `[GetSecuritySettingsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GetSecuritySettingsRequest)` (message)
  * `[GetToolRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GetToolRequest)` (message)
  * `[GetToolsetRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GetToolsetRequest)` (message)
  * `[GoAway](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GoAway)` (message)
  * `[GoldenRunMethod](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GoldenRunMethod)` (enum)
  * `[GoogleSearchSuggestions](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GoogleSearchSuggestions)` (message)
  * `[GoogleSearchTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GoogleSearchTool)` (message)
  * `[GoogleSearchTool.PromptConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GoogleSearchTool.PromptConfig)` (message)
  * `[Guardrail](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Guardrail)` (message)
  * `[Guardrail.CodeCallback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Guardrail.CodeCallback)` (message)
  * `[Guardrail.ContentFilter](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Guardrail.ContentFilter)` (message)
  * `[Guardrail.ContentFilter.MatchType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Guardrail.ContentFilter.MatchType)` (enum)
  * `[Guardrail.LlmPolicy](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Guardrail.LlmPolicy)` (message)
  * `[Guardrail.LlmPolicy.PolicyScope](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Guardrail.LlmPolicy.PolicyScope)` (enum)
  * `[Guardrail.LlmPromptSecurity](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Guardrail.LlmPromptSecurity)` (message)
  * `[Guardrail.LlmPromptSecurity.DefaultSecuritySettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Guardrail.LlmPromptSecurity.DefaultSecuritySettings)` (message)
  * `[Guardrail.ModelSafety](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Guardrail.ModelSafety)` (message)
  * `[Guardrail.ModelSafety.HarmBlockThreshold](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Guardrail.ModelSafety.HarmBlockThreshold)` (enum)
  * `[Guardrail.ModelSafety.HarmCategory](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Guardrail.ModelSafety.HarmCategory)` (enum)
  * `[Guardrail.ModelSafety.SafetySetting](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Guardrail.ModelSafety.SafetySetting)` (message)
  * `[Guardrail.Supervisor](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Guardrail.Supervisor)` (message)
  * `[Guardrail.Supervisor.DetectionMode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Guardrail.Supervisor.DetectionMode)` (enum)
  * `[Guardrail.Supervisor.Type](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Guardrail.Supervisor.Type)` (enum)
  * `[Image](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Image)` (message)
  * `[ImportAppRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ImportAppRequest)` (message)
  * `[ImportAppRequest.ImportOptions](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ImportAppRequest.ImportOptions)` (message)
  * `[ImportAppRequest.ImportOptions.ConflictResolutionStrategy](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ImportAppRequest.ImportOptions.ConflictResolutionStrategy)` (enum)
  * `[ImportAppResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ImportAppResponse)` (message)
  * `[ImportEvaluationsOperationMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ImportEvaluationsOperationMetadata)` (message)
  * `[ImportEvaluationsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ImportEvaluationsRequest)` (message)
  * `[ImportEvaluationsRequest.ConversationList](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ImportEvaluationsRequest.ConversationList)` (message)
  * `[ImportEvaluationsRequest.ImportOptions](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ImportEvaluationsRequest.ImportOptions)` (message)
  * `[ImportEvaluationsRequest.ImportOptions.ConflictResolutionStrategy](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ImportEvaluationsRequest.ImportOptions.ConflictResolutionStrategy)` (enum)
  * `[ImportEvaluationsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ImportEvaluationsResponse)` (message)
  * `[InputAudioConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.InputAudioConfig)` (message)
  * `[InstagramCredentials](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.InstagramCredentials)` (message)
  * `[InterruptionSignal](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.InterruptionSignal)` (message)
  * `[LanguageSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.LanguageSettings)` (message)
  * `[LatencyReport](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.LatencyReport)` (message)
  * `[LatencyReport.CallbackLatency](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.LatencyReport.CallbackLatency)` (message)
  * `[LatencyReport.GuardrailLatency](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.LatencyReport.GuardrailLatency)` (message)
  * `[LatencyReport.LatencyMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.LatencyReport.LatencyMetrics)` (message)
  * `[LatencyReport.LlmCallLatency](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.LatencyReport.LlmCallLatency)` (message)
  * `[LatencyReport.ToolLatency](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.LatencyReport.ToolLatency)` (message)
  * `[ListAgentsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListAgentsRequest)` (message)
  * `[ListAgentsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListAgentsResponse)` (message)
  * `[ListAppVersionsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListAppVersionsRequest)` (message)
  * `[ListAppVersionsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListAppVersionsResponse)` (message)
  * `[ListAppsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListAppsRequest)` (message)
  * `[ListAppsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListAppsResponse)` (message)
  * `[ListChangelogsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListChangelogsRequest)` (message)
  * `[ListChangelogsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListChangelogsResponse)` (message)
  * `[ListConversationsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListConversationsRequest)` (message)
  * `[ListConversationsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListConversationsResponse)` (message)
  * `[ListDeploymentsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListDeploymentsRequest)` (message)
  * `[ListDeploymentsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListDeploymentsResponse)` (message)
  * `[ListEvaluationDatasetsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListEvaluationDatasetsRequest)` (message)
  * `[ListEvaluationDatasetsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListEvaluationDatasetsResponse)` (message)
  * `[ListEvaluationExpectationsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListEvaluationExpectationsRequest)` (message)
  * `[ListEvaluationExpectationsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListEvaluationExpectationsResponse)` (message)
  * `[ListEvaluationResultsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListEvaluationResultsRequest)` (message)
  * `[ListEvaluationResultsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListEvaluationResultsResponse)` (message)
  * `[ListEvaluationRunsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListEvaluationRunsRequest)` (message)
  * `[ListEvaluationRunsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListEvaluationRunsResponse)` (message)
  * `[ListEvaluationsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListEvaluationsRequest)` (message)
  * `[ListEvaluationsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListEvaluationsResponse)` (message)
  * `[ListExamplesRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListExamplesRequest)` (message)
  * `[ListExamplesResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListExamplesResponse)` (message)
  * `[ListGuardrailsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListGuardrailsRequest)` (message)
  * `[ListGuardrailsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListGuardrailsResponse)` (message)
  * `[ListScheduledEvaluationRunsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListScheduledEvaluationRunsRequest)` (message)
  * `[ListScheduledEvaluationRunsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListScheduledEvaluationRunsResponse)` (message)
  * `[ListToolsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListToolsRequest)` (message)
  * `[ListToolsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListToolsResponse)` (message)
  * `[ListToolsetsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListToolsetsRequest)` (message)
  * `[ListToolsetsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListToolsetsResponse)` (message)
  * `[LoggingSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.LoggingSettings)` (message)
  * `[McpTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.McpTool)` (message)
  * `[McpTool.State](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.McpTool.State)` (enum)
  * `[McpToolDefinition](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.McpToolDefinition)` (message)
  * `[McpToolOverride](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.McpToolOverride)` (message)
  * `[McpToolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.McpToolset)` (message)
  * `[Message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Message)` (message)
  * `[MetricAnalysisSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.MetricAnalysisSettings)` (message)
  * `[MockConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.MockConfig)` (message)
  * `[MockConfig.UnmatchedToolCallBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.MockConfig.UnmatchedToolCallBehavior)` (enum)
  * `[MockedToolCall](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.MockedToolCall)` (message)
  * `[ModelSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ModelSettings)` (message)
  * `[ModelSettings.ThinkingLevel](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ModelSettings.ThinkingLevel)` (enum)
  * `[OAuthConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.OAuthConfig)` (message)
  * `[OAuthConfig.OauthGrantType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.OAuthConfig.OauthGrantType)` (enum)
  * `[OpenApiTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.OpenApiTool)` (message)
  * `[OpenApiToolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.OpenApiToolset)` (message)
  * `[OperationMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.OperationMetadata)` (message)
  * `[OptimizationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.OptimizationConfig)` (message)
  * `[OptimizationConfig.OptimizationStatus](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.OptimizationConfig.OptimizationStatus)` (enum)
  * `[OutputAudioConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.OutputAudioConfig)` (message)
  * `[PersonaRunConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.PersonaRunConfig)` (message)
  * `[PythonCodeCondition](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.PythonCodeCondition)` (message)
  * `[PythonFunction](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.PythonFunction)` (message)
  * `[QualityReport](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.QualityReport)` (message)
  * `[QualityReport.AgentIssues](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.QualityReport.AgentIssues)` (message)
  * `[QualityReport.Issue](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.QualityReport.Issue)` (message)
  * `[RecognitionResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.RecognitionResult)` (message)
  * `[RedactionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.RedactionConfig)` (message)
  * `[RemoteA2aConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.RemoteA2aConfig)` (message)
  * `[RemoteAgentTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.RemoteAgentTool)` (message)
  * `[RestoreAppVersionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.RestoreAppVersionRequest)` (message)
  * `[RestoreAppVersionResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.RestoreAppVersionResponse)` (message)
  * `[RetrieveToolSchemaRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.RetrieveToolSchemaRequest)` (message)
  * `[RetrieveToolSchemaResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.RetrieveToolSchemaResponse)` (message)
  * `[RetrieveToolsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.RetrieveToolsRequest)` (message)
  * `[RetrieveToolsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.RetrieveToolsResponse)` (message)
  * `[RunEvaluationOperationMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.RunEvaluationOperationMetadata)` (message)
  * `[RunEvaluationRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.RunEvaluationRequest)` (message)
  * `[RunEvaluationResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.RunEvaluationResponse)` (message)
  * `[RunEvaluationResultMetricsOperationMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.RunEvaluationResultMetricsOperationMetadata)` (message)
  * `[RunEvaluationResultMetricsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.RunEvaluationResultMetricsRequest)` (message)
  * `[RunEvaluationResultMetricsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.RunEvaluationResultMetricsResponse)` (message)
  * `[RunSessionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.RunSessionRequest)` (message)
  * `[RunSessionResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.RunSessionResponse)` (message)
  * `[ScheduledEvaluationRun](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ScheduledEvaluationRun)` (message)
  * `[ScheduledEvaluationRun.SchedulingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ScheduledEvaluationRun.SchedulingConfig)` (message)
  * `[ScheduledEvaluationRun.SchedulingConfig.Frequency](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ScheduledEvaluationRun.SchedulingConfig.Frequency)` (enum)
  * `[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Schema)` (message)
  * `[Schema.Type](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Schema.Type)` (enum)
  * `[SecuritySettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.SecuritySettings)` (message)
  * `[ServiceAccountAuthConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ServiceAccountAuthConfig)` (message)
  * `[ServiceAgentIdTokenAuthConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ServiceAgentIdTokenAuthConfig)` (message)
  * `[ServiceDirectoryConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ServiceDirectoryConfig)` (message)
  * `[SessionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.SessionConfig)` (message)
  * `[SessionConfig.RemoteDialogflowQueryParameters](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.SessionConfig.RemoteDialogflowQueryParameters)` (message)
  * `[SessionInput](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.SessionInput)` (message)
  * `[SessionOutput](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.SessionOutput)` (message)
  * `[SessionOutput.DiagnosticInfo](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.SessionOutput.DiagnosticInfo)` (message)
  * `[Span](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Span)` (message)
  * `[SynthesizeSpeechConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.SynthesizeSpeechConfig)` (message)
  * `[SystemTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.SystemTool)` (message)
  * `[TestPersonaVoiceRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.TestPersonaVoiceRequest)` (message)
  * `[TestPersonaVoiceResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.TestPersonaVoiceResponse)` (message)
  * `[TimeZoneSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.TimeZoneSettings)` (message)
  * `[TlsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.TlsConfig)` (message)
  * `[TlsConfig.CaCert](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.TlsConfig.CaCert)` (message)
  * `[Tool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Tool)` (message)
  * `[ToolCall](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ToolCall)` (message)
  * `[ToolCalls](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ToolCalls)` (message)
  * `[ToolFakeConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ToolFakeConfig)` (message)
  * `[ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ToolResponse)` (message)
  * `[ToolResponses](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ToolResponses)` (message)
  * `[Toolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Toolset)` (message)
  * `[ToolsetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ToolsetTool)` (message)
  * `[TransferRule](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.TransferRule)` (message)
  * `[TransferRule.DeterministicTransfer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.TransferRule.DeterministicTransfer)` (message)
  * `[TransferRule.Direction](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.TransferRule.Direction)` (enum)
  * `[TransferRule.DisablePlannerTransfer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.TransferRule.DisablePlannerTransfer)` (message)
  * `[TriggerAction](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.TriggerAction)` (message)
  * `[TriggerAction.GenerativeAnswer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.TriggerAction.GenerativeAnswer)` (message)
  * `[TriggerAction.RespondImmediately](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.TriggerAction.RespondImmediately)` (message)
  * `[TriggerAction.Response](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.TriggerAction.Response)` (message)
  * `[TriggerAction.TransferAgent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.TriggerAction.TransferAgent)` (message)
  * `[UpdateAgentRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.UpdateAgentRequest)` (message)
  * `[UpdateAppRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.UpdateAppRequest)` (message)
  * `[UpdateAppVersionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.UpdateAppVersionRequest)` (message)
  * `[UpdateDeploymentRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.UpdateDeploymentRequest)` (message)
  * `[UpdateEvaluationDatasetRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.UpdateEvaluationDatasetRequest)` (message)
  * `[UpdateEvaluationExpectationRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.UpdateEvaluationExpectationRequest)` (message)
  * `[UpdateEvaluationRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.UpdateEvaluationRequest)` (message)
  * `[UpdateExampleRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.UpdateExampleRequest)` (message)
  * `[UpdateGuardrailRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.UpdateGuardrailRequest)` (message)
  * `[UpdateScheduledEvaluationRunRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.UpdateScheduledEvaluationRunRequest)` (message)
  * `[UpdateSecuritySettingsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.UpdateSecuritySettingsRequest)` (message)
  * `[UpdateToolRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.UpdateToolRequest)` (message)
  * `[UpdateToolsetRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.UpdateToolsetRequest)` (message)
  * `[UploadEvaluationAudioRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.UploadEvaluationAudioRequest)` (message)
  * `[UploadEvaluationAudioResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.UploadEvaluationAudioResponse)` (message)
  * `[VpcScSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.VpcScSettings)` (message)
  * `[WebSearchQuery](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.WebSearchQuery)` (message)
  * `[WhatsAppCredentials](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.WhatsAppCredentials)` (message)
  * `[WidgetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.WidgetTool)` (message)
  * `[WidgetTool.DataMapping](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.WidgetTool.DataMapping)` (message)
  * `[WidgetTool.DataMapping.Mode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.WidgetTool.DataMapping.Mode)` (enum)
  * `[WidgetTool.TextResponseConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.WidgetTool.TextResponseConfig)` (message)
  * `[WidgetTool.TextResponseConfig.Type](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.WidgetTool.TextResponseConfig.Type)` (enum)
  * `[WidgetTool.WidgetType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.WidgetTool.WidgetType)` (enum)



## AgentService

The service that manages agent-related resources in Gemini Enterprise for Customer Engagement (CES).

BatchDeleteConversations  
---  
` rpc BatchDeleteConversations(`[BatchDeleteConversationsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.BatchDeleteConversationsRequest)`) returns (`[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Batch deletes the specified conversations.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `ces.conversations.delete`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
CreateAgent  
---  
` rpc CreateAgent(`[CreateAgentRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.CreateAgentRequest)`) returns (`[Agent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Agent)`) ` Creates a new agent in the given app.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `ces.agents.create`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
CreateApp  
---  
` rpc CreateApp(`[CreateAppRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.CreateAppRequest)`) returns (`[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Creates a new app in the given project and location.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `ces.apps.create`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
CreateAppVersion  
---  
` rpc CreateAppVersion(`[CreateAppVersionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.CreateAppVersionRequest)`) returns (`[AppVersion](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AppVersion)`) ` Creates a new app version in the given app.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `ces.appVersions.create`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
CreateDeployment  
---  
` rpc CreateDeployment(`[CreateDeploymentRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.CreateDeploymentRequest)`) returns (`[Deployment](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Deployment)`) ` Creates a new deployment in the given app.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `ces.deployments.create`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
CreateExample  
---  
` rpc CreateExample(`[CreateExampleRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.CreateExampleRequest)`) returns (`[Example](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Example)`) ` Creates a new example in the given app.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `ces.examples.create`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
CreateGuardrail  
---  
` rpc CreateGuardrail(`[CreateGuardrailRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.CreateGuardrailRequest)`) returns (`[Guardrail](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Guardrail)`) ` Creates a new guardrail in the given app.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `ces.guardrails.create`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
CreateTool  
---  
` rpc CreateTool(`[CreateToolRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.CreateToolRequest)`) returns (`[Tool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Tool)`) ` Creates a new tool in the given app.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `ces.tools.create`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
CreateToolset  
---  
` rpc CreateToolset(`[CreateToolsetRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.CreateToolsetRequest)`) returns (`[Toolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Toolset)`) ` Creates a new toolset in the given app.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `ces.toolsets.create`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
DeleteAgent  
---  
` rpc DeleteAgent(`[DeleteAgentRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DeleteAgentRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes the specified agent.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `ces.agents.delete`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
DeleteApp  
---  
` rpc DeleteApp(`[DeleteAppRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DeleteAppRequest)`) returns (`[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Deletes the specified app.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `ces.apps.delete`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
DeleteAppVersion  
---  
` rpc DeleteAppVersion(`[DeleteAppVersionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DeleteAppVersionRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes the specified app version.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `ces.appVersions.delete`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
DeleteConversation  
---  
` rpc DeleteConversation(`[DeleteConversationRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DeleteConversationRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes the specified conversation.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `ces.conversations.delete`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
DeleteDeployment  
---  
` rpc DeleteDeployment(`[DeleteDeploymentRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DeleteDeploymentRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes the specified deployment.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `ces.deployments.delete`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
DeleteExample  
---  
` rpc DeleteExample(`[DeleteExampleRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DeleteExampleRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes the specified example.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `ces.examples.delete`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
DeleteGuardrail  
---  
` rpc DeleteGuardrail(`[DeleteGuardrailRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DeleteGuardrailRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes the specified guardrail.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `ces.guardrails.delete`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
DeleteTool  
---  
` rpc DeleteTool(`[DeleteToolRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DeleteToolRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes the specified tool.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `ces.tools.delete`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
DeleteToolset  
---  
` rpc DeleteToolset(`[DeleteToolsetRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DeleteToolsetRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes the specified toolset.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `ces.toolsets.delete`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
ExportApp  
---  
` rpc ExportApp(`[ExportAppRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ExportAppRequest)`) returns (`[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Exports the specified app.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `ces.apps.export`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
GenerateAppResource  
---  
` rpc GenerateAppResource(`[GenerateAppResourceRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GenerateAppResourceRequest)`) returns (`[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Generates specific resources (e.g. agent) in the app using LLM assistant.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `ces.apps.update`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
GetAgent  
---  
` rpc GetAgent(`[GetAgentRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GetAgentRequest)`) returns (`[Agent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Agent)`) ` Gets details of the specified agent.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `ces.agents.get`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
GetApp  
---  
` rpc GetApp(`[GetAppRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GetAppRequest)`) returns (`[App](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.App)`) ` Gets details of the specified app.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `ces.apps.get`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
GetAppVersion  
---  
` rpc GetAppVersion(`[GetAppVersionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GetAppVersionRequest)`) returns (`[AppVersion](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AppVersion)`) ` Gets details of the specified app version.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `ces.appVersions.get`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
GetChangelog  
---  
` rpc GetChangelog(`[GetChangelogRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GetChangelogRequest)`) returns (`[Changelog](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Changelog)`) ` Gets the specified changelog.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `ces.changelogs.get`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
GetConversation  
---  
` rpc GetConversation(`[GetConversationRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GetConversationRequest)`) returns (`[Conversation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Conversation)`) ` Gets details of the specified conversation.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `ces.conversations.get`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
GetDeployment  
---  
` rpc GetDeployment(`[GetDeploymentRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GetDeploymentRequest)`) returns (`[Deployment](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Deployment)`) ` Gets details of the specified deployment.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `ces.deployments.get`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
GetExample  
---  
` rpc GetExample(`[GetExampleRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GetExampleRequest)`) returns (`[Example](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Example)`) ` Gets details of the specified example.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `ces.examples.get`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
GetGuardrail  
---  
` rpc GetGuardrail(`[GetGuardrailRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GetGuardrailRequest)`) returns (`[Guardrail](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Guardrail)`) ` Gets details of the specified guardrail.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `ces.guardrails.get`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
GetSecuritySettings  
---  
` rpc GetSecuritySettings(`[GetSecuritySettingsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GetSecuritySettingsRequest)`) returns (`[SecuritySettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.SecuritySettings)`) ` Retrieves the security settings for the project and location.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `ces.securitySettings.get`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
GetTool  
---  
` rpc GetTool(`[GetToolRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GetToolRequest)`) returns (`[Tool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Tool)`) ` Gets details of the specified tool.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `ces.tools.get`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
GetToolset  
---  
` rpc GetToolset(`[GetToolsetRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GetToolsetRequest)`) returns (`[Toolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Toolset)`) ` Gets details of the specified toolset.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `ces.toolsets.get`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
ImportApp  
---  
` rpc ImportApp(`[ImportAppRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ImportAppRequest)`) returns (`[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Imports the specified app.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `ces.apps.import`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
ListAgents  
---  
` rpc ListAgents(`[ListAgentsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListAgentsRequest)`) returns (`[ListAgentsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListAgentsResponse)`) ` Lists agents in the given app.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `ces.agents.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
ListAppVersions  
---  
` rpc ListAppVersions(`[ListAppVersionsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListAppVersionsRequest)`) returns (`[ListAppVersionsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListAppVersionsResponse)`) ` Lists all app versions in the given app.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `ces.appVersions.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
ListApps  
---  
` rpc ListApps(`[ListAppsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListAppsRequest)`) returns (`[ListAppsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListAppsResponse)`) ` Lists apps in the given project and location.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `ces.apps.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
ListChangelogs  
---  
` rpc ListChangelogs(`[ListChangelogsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListChangelogsRequest)`) returns (`[ListChangelogsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListChangelogsResponse)`) ` Lists the changelogs of the specified app.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `ces.changelogs.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
ListConversations  
---  
` rpc ListConversations(`[ListConversationsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListConversationsRequest)`) returns (`[ListConversationsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListConversationsResponse)`) ` Lists conversations in the given app.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `ces.conversations.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
ListDeployments  
---  
` rpc ListDeployments(`[ListDeploymentsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListDeploymentsRequest)`) returns (`[ListDeploymentsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListDeploymentsResponse)`) ` Lists deployments in the given app.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `ces.deployments.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
ListExamples  
---  
` rpc ListExamples(`[ListExamplesRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListExamplesRequest)`) returns (`[ListExamplesResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListExamplesResponse)`) ` Lists examples in the given app.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `ces.examples.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
ListGuardrails  
---  
` rpc ListGuardrails(`[ListGuardrailsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListGuardrailsRequest)`) returns (`[ListGuardrailsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListGuardrailsResponse)`) ` Lists guardrails in the given app.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `ces.guardrails.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
ListTools  
---  
` rpc ListTools(`[ListToolsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListToolsRequest)`) returns (`[ListToolsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListToolsResponse)`) ` Lists tools in the given app.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `ces.tools.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
ListToolsets  
---  
` rpc ListToolsets(`[ListToolsetsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListToolsetsRequest)`) returns (`[ListToolsetsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListToolsetsResponse)`) ` Lists toolsets in the given app.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `ces.toolsets.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
RestoreAppVersion  
---  
` rpc RestoreAppVersion(`[RestoreAppVersionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.RestoreAppVersionRequest)`) returns (`[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Restores the specified app version. This will create a new app version from the current draft app and overwrite the current draft with the specified app version.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `ces.appVersions.restore`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
UpdateAgent  
---  
` rpc UpdateAgent(`[UpdateAgentRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.UpdateAgentRequest)`) returns (`[Agent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Agent)`) ` Updates the specified agent.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `ces.agents.update`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
UpdateApp  
---  
` rpc UpdateApp(`[UpdateAppRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.UpdateAppRequest)`) returns (`[App](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.App)`) ` Updates the specified app.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `ces.apps.update`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
UpdateAppVersion  
---  
` rpc UpdateAppVersion(`[UpdateAppVersionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.UpdateAppVersionRequest)`) returns (`[AppVersion](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AppVersion)`) ` Updates the specified app version.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
UpdateDeployment  
---  
` rpc UpdateDeployment(`[UpdateDeploymentRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.UpdateDeploymentRequest)`) returns (`[Deployment](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Deployment)`) ` Updates the specified deployment.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `ces.deployments.update`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
UpdateExample  
---  
` rpc UpdateExample(`[UpdateExampleRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.UpdateExampleRequest)`) returns (`[Example](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Example)`) ` Updates the specified example.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `ces.examples.update`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
UpdateGuardrail  
---  
` rpc UpdateGuardrail(`[UpdateGuardrailRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.UpdateGuardrailRequest)`) returns (`[Guardrail](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Guardrail)`) ` Updates the specified guardrail.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `ces.guardrails.update`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
UpdateSecuritySettings  
---  
` rpc UpdateSecuritySettings(`[UpdateSecuritySettingsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.UpdateSecuritySettingsRequest)`) returns (`[SecuritySettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.SecuritySettings)`) ` Updates the security settings for the project and location.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `ces.securitySettings.update`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
UpdateTool  
---  
` rpc UpdateTool(`[UpdateToolRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.UpdateToolRequest)`) returns (`[Tool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Tool)`) ` Updates the specified tool.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `ces.tools.update`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
UpdateToolset  
---  
` rpc UpdateToolset(`[UpdateToolsetRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.UpdateToolsetRequest)`) returns (`[Toolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Toolset)`) ` Updates the specified toolset.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `ces.toolsets.update`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
  
## EvaluationService

EvaluationService exposes methods to perform evaluation for the CES app.

CreateEvaluation  
---  
` rpc CreateEvaluation(`[CreateEvaluationRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.CreateEvaluationRequest)`) returns (`[Evaluation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Evaluation)`) ` Creates an evaluation.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `ces.evaluations.create`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
CreateEvaluationDataset  
---  
` rpc CreateEvaluationDataset(`[CreateEvaluationDatasetRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.CreateEvaluationDatasetRequest)`) returns (`[EvaluationDataset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationDataset)`) ` Creates an evaluation dataset.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `ces.evaluationDatasets.create`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
CreateEvaluationExpectation  
---  
` rpc CreateEvaluationExpectation(`[CreateEvaluationExpectationRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.CreateEvaluationExpectationRequest)`) returns (`[EvaluationExpectation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationExpectation)`) ` Creates an evaluation expectation.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `ces.evaluationExpectations.create`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
CreateScheduledEvaluationRun  
---  
` rpc CreateScheduledEvaluationRun(`[CreateScheduledEvaluationRunRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.CreateScheduledEvaluationRunRequest)`) returns (`[ScheduledEvaluationRun](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ScheduledEvaluationRun)`) ` Creates a scheduled evaluation run.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
DeleteEvaluation  
---  
` rpc DeleteEvaluation(`[DeleteEvaluationRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DeleteEvaluationRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes an evaluation.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `ces.evaluations.delete`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
DeleteEvaluationDataset  
---  
` rpc DeleteEvaluationDataset(`[DeleteEvaluationDatasetRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DeleteEvaluationDatasetRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes an evaluation dataset.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `ces.evaluationDatasets.delete`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
DeleteEvaluationExpectation  
---  
` rpc DeleteEvaluationExpectation(`[DeleteEvaluationExpectationRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DeleteEvaluationExpectationRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes an evaluation expectation.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `ces.evaluationExpectations.delete`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
DeleteEvaluationResult  
---  
` rpc DeleteEvaluationResult(`[DeleteEvaluationResultRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DeleteEvaluationResultRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes an evaluation result.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `ces.evaluationResults.delete`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
DeleteEvaluationRun  
---  
` rpc DeleteEvaluationRun(`[DeleteEvaluationRunRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DeleteEvaluationRunRequest)`) returns (`[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Deletes an evaluation run.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `ces.evaluationRuns.delete`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
DeleteScheduledEvaluationRun  
---  
` rpc DeleteScheduledEvaluationRun(`[DeleteScheduledEvaluationRunRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DeleteScheduledEvaluationRunRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes a scheduled evaluation run.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ExportEvaluationResults  
---  
` rpc ExportEvaluationResults(`[ExportEvaluationResultsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ExportEvaluationResultsRequest)`) returns (`[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Exports evaluations results.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `ces.evaluations.export`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
ExportEvaluationRuns  
---  
` rpc ExportEvaluationRuns(`[ExportEvaluationRunsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ExportEvaluationRunsRequest)`) returns (`[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Exports evaluations runs.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `names` resource:

  * `ces.evaluationRuns.get`

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `ces.evaluations.export`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
ExportEvaluations  
---  
` rpc ExportEvaluations(`[ExportEvaluationsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ExportEvaluationsRequest)`) returns (`[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Exports evaluations.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `ces.evaluations.export`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
GenerateEvaluation  
---  
` rpc GenerateEvaluation(`[GenerateEvaluationRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GenerateEvaluationRequest)`) returns (`[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Creates a golden evaluation from a conversation.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `conversation` resource:

  * `ces.conversations.get`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
GetEvaluation  
---  
` rpc GetEvaluation(`[GetEvaluationRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GetEvaluationRequest)`) returns (`[Evaluation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Evaluation)`) ` Gets details of the specified evaluation.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `ces.evaluations.get`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
GetEvaluationDataset  
---  
` rpc GetEvaluationDataset(`[GetEvaluationDatasetRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GetEvaluationDatasetRequest)`) returns (`[EvaluationDataset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationDataset)`) ` Gets details of the specified evaluation dataset.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `ces.evaluationDatasets.get`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
GetEvaluationExpectation  
---  
` rpc GetEvaluationExpectation(`[GetEvaluationExpectationRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GetEvaluationExpectationRequest)`) returns (`[EvaluationExpectation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationExpectation)`) ` Gets details of the specified evaluation expectation.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `ces.evaluationExpectations.get`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
GetEvaluationResult  
---  
` rpc GetEvaluationResult(`[GetEvaluationResultRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GetEvaluationResultRequest)`) returns (`[EvaluationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationResult)`) ` Gets details of the specified evaluation result.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `ces.evaluationResults.get`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
GetEvaluationRun  
---  
` rpc GetEvaluationRun(`[GetEvaluationRunRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GetEvaluationRunRequest)`) returns (`[EvaluationRun](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationRun)`) ` Gets details of the specified evaluation run.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `ces.evaluationRuns.get`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
GetScheduledEvaluationRun  
---  
` rpc GetScheduledEvaluationRun(`[GetScheduledEvaluationRunRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GetScheduledEvaluationRunRequest)`) returns (`[ScheduledEvaluationRun](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ScheduledEvaluationRun)`) ` Gets details of the specified scheduled evaluation run.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ImportEvaluations  
---  
` rpc ImportEvaluations(`[ImportEvaluationsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ImportEvaluationsRequest)`) returns (`[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Imports evaluations into the app.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permissions on the `parent` resource:

  * `ces.evaluations.create`
  * `ces.evaluations.update`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
ListEvaluationDatasets  
---  
` rpc ListEvaluationDatasets(`[ListEvaluationDatasetsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListEvaluationDatasetsRequest)`) returns (`[ListEvaluationDatasetsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListEvaluationDatasetsResponse)`) ` Lists all evaluation datasets in the given app.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `ces.evaluationDatasets.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
ListEvaluationExpectations  
---  
` rpc ListEvaluationExpectations(`[ListEvaluationExpectationsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListEvaluationExpectationsRequest)`) returns (`[ListEvaluationExpectationsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListEvaluationExpectationsResponse)`) ` Lists all evaluation expectations in the given app.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `ces.evaluationExpectations.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
ListEvaluationResults  
---  
` rpc ListEvaluationResults(`[ListEvaluationResultsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListEvaluationResultsRequest)`) returns (`[ListEvaluationResultsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListEvaluationResultsResponse)`) ` Lists all evaluation results for a given evaluation.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `ces.evaluationResults.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
ListEvaluationRuns  
---  
` rpc ListEvaluationRuns(`[ListEvaluationRunsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListEvaluationRunsRequest)`) returns (`[ListEvaluationRunsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListEvaluationRunsResponse)`) ` Lists all evaluation runs in the given app.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `ces.evaluationRuns.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
ListEvaluations  
---  
` rpc ListEvaluations(`[ListEvaluationsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListEvaluationsRequest)`) returns (`[ListEvaluationsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListEvaluationsResponse)`) ` Lists all evaluations in the given app.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `ces.evaluations.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
ListScheduledEvaluationRuns  
---  
` rpc ListScheduledEvaluationRuns(`[ListScheduledEvaluationRunsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListScheduledEvaluationRunsRequest)`) returns (`[ListScheduledEvaluationRunsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListScheduledEvaluationRunsResponse)`) ` Lists all scheduled evaluation runs in the given app.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
RunEvaluation  
---  
` rpc RunEvaluation(`[RunEvaluationRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.RunEvaluationRequest)`) returns (`[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Runs an evaluation of the app.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `app` resource:

  * `ces.apps.runEvaluation`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
RunEvaluationResultMetrics  
---  
` rpc RunEvaluationResultMetrics(`[RunEvaluationResultMetricsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.RunEvaluationResultMetricsRequest)`) returns (`[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Runs metrics on an existing evaluation result.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
TestPersonaVoice  
---  
` rpc TestPersonaVoice(`[TestPersonaVoiceRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.TestPersonaVoiceRequest)`) returns (`[TestPersonaVoiceResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.TestPersonaVoiceResponse)`) ` Tests the voice of a persona. Also accepts a default persona.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `app` resource:

  * `ces.apps.get`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
UpdateEvaluation  
---  
` rpc UpdateEvaluation(`[UpdateEvaluationRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.UpdateEvaluationRequest)`) returns (`[Evaluation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Evaluation)`) ` Updates an evaluation.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `ces.evaluations.update`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
UpdateEvaluationDataset  
---  
` rpc UpdateEvaluationDataset(`[UpdateEvaluationDatasetRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.UpdateEvaluationDatasetRequest)`) returns (`[EvaluationDataset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationDataset)`) ` Updates an evaluation dataset.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `ces.evaluationDatasets.update`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
UpdateEvaluationExpectation  
---  
` rpc UpdateEvaluationExpectation(`[UpdateEvaluationExpectationRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.UpdateEvaluationExpectationRequest)`) returns (`[EvaluationExpectation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationExpectation)`) ` Updates an evaluation expectation.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `ces.evaluationExpectations.update`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
UpdateScheduledEvaluationRun  
---  
` rpc UpdateScheduledEvaluationRun(`[UpdateScheduledEvaluationRunRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.UpdateScheduledEvaluationRunRequest)`) returns (`[ScheduledEvaluationRun](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ScheduledEvaluationRun)`) ` Updates a scheduled evaluation run.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
UploadEvaluationAudio  
---  
` rpc UploadEvaluationAudio(`[UploadEvaluationAudioRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.UploadEvaluationAudioRequest)`) returns (`[UploadEvaluationAudioResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.UploadEvaluationAudioResponse)`) ` Uploads audio for use in Golden Evaluations. Stores the audio in the Cloud Storage bucket defined in 'App.logging_settings.evaluation_audio_recording_config.gcs_bucket' and returns a transcript.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `ces.evaluations.update`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
  
## SessionService

Session service provides APIs for interacting with CES agents.

BidiRunSession  
---  
` rpc BidiRunSession(`[BidiSessionClientMessage](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.BidiSessionClientMessage)`) returns (`[BidiSessionServerMessage](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.BidiSessionServerMessage)`) ` Establishes a bidirectional streaming connection with the CES agent. The agent processes continuous multimodal inputs (e.g., text, audio) and generates real-time multimodal output streams.\--- Client Request Stream --- The client streams requests in the following order:

  1. Initialization: The first message must contain `[SessionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.BidiSessionClientMessage.FIELDS.google.cloud.ces.v1beta.SessionConfig.google.cloud.ces.v1beta.BidiSessionClientMessage.config)`. For audio sessions, this should also include `[InputAudioConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.SessionConfig.FIELDS.google.cloud.ces.v1beta.InputAudioConfig.google.cloud.ces.v1beta.SessionConfig.input_audio_config)` and `[OutputAudioConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.SessionConfig.FIELDS.google.cloud.ces.v1beta.OutputAudioConfig.google.cloud.ces.v1beta.SessionConfig.output_audio_config)` to define audio processing and synthesis parameters.
  2. Interaction: Subsequent messages stream `[SessionInput](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.BidiSessionClientMessage.FIELDS.google.cloud.ces.v1beta.SessionInput.google.cloud.ces.v1beta.BidiSessionClientMessage.realtime_input)` containing real-time user input data.
  3. Termination: The client should half-close the stream when there is no more user input. It should also half-close upon receiving `[EndSession](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.BidiSessionServerMessage.FIELDS.google.cloud.ces.v1beta.EndSession.google.cloud.ces.v1beta.BidiSessionServerMessage.end_session)` or `[GoAway](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.BidiSessionServerMessage.FIELDS.google.cloud.ces.v1beta.GoAway.google.cloud.ces.v1beta.BidiSessionServerMessage.go_away)` from the agent.

\--- Server Response Stream --- For each interaction turn, the agent streams messages in the following sequence:

  1. Speech Recognition (First N messages): Contains `[RecognitionResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.BidiSessionServerMessage.FIELDS.google.cloud.ces.v1beta.RecognitionResult.google.cloud.ces.v1beta.BidiSessionServerMessage.recognition_result)` representing the concatenated user speech segments captured so far. This is only populated for audio sessions.
  2. Response (Next M messages): Contains `[SessionOutput](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.BidiSessionServerMessage.FIELDS.google.cloud.ces.v1beta.SessionOutput.google.cloud.ces.v1beta.BidiSessionServerMessage.session_output)` delivering the agent's response in various modalities (e.g., text, audio).
  3. Turn Completion (Final message of the turn): Contains `[SessionOutput](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.BidiSessionServerMessage.FIELDS.google.cloud.ces.v1beta.SessionOutput.google.cloud.ces.v1beta.BidiSessionServerMessage.session_output)` with `[turn_completed](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.SessionOutput.FIELDS.bool.google.cloud.ces.v1beta.SessionOutput.turn_completed)` set to true. This signals the end of the current turn and includes `[DiagnosticInfo](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.SessionOutput.FIELDS.google.cloud.ces.v1beta.SessionOutput.DiagnosticInfo.google.cloud.ces.v1beta.SessionOutput.diagnostic_info)` with execution details.

\--- Audio Best Practices --- 1. Streaming: Stream `[audio data](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.SessionInput.FIELDS.bytes.google.cloud.ces.v1beta.SessionInput.audio)` **CONTINUOUSLY** , even during silence. Recommended chunk size: 40-120ms (balances latency vs. efficiency).

  1. Playback & Interruption: Play `[audio responses](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.SessionOutput.FIELDS.bytes.google.cloud.ces.v1beta.SessionOutput.audio)` upon receipt. Stop playback immediately if an `[InterruptionSignal](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.BidiSessionServerMessage.FIELDS.google.cloud.ces.v1beta.InterruptionSignal.google.cloud.ces.v1beta.BidiSessionServerMessage.interruption_signal)` is received (e.g., user barge-in or new agent response).



Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `session` resource:

  * `ces.sessions.bidiRunSession`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
RunSession  
---  
` rpc RunSession(`[RunSessionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.RunSessionRequest)`) returns (`[RunSessionResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.RunSessionResponse)`) ` Initiates a single-turn interaction with the CES agent within a session.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `session` resource:

  * `ces.sessions.runSession`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
StreamRunSession  
---  
` rpc StreamRunSession(`[RunSessionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.RunSessionRequest)`) returns (`[RunSessionResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.RunSessionResponse)`) ` Initiates a single-turn interaction with the CES agent. Uses server-side streaming to deliver incremental results and partial responses as they are generated.By default, complete responses (e.g., messages from callbacks or full LLM responses) are sent to the client as soon as they are available. To enable streaming individual text chunks directly from the model, set `[enable_text_streaming](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.SessionConfig.FIELDS.bool.google.cloud.ces.v1beta.SessionConfig.enable_text_streaming)` to true.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `session` resource:

  * `ces.sessions.runSession`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
  
## ToolService

Tool service provides APIs for interacting with CES tools.

ExecuteTool  
---  
` rpc ExecuteTool(`[ExecuteToolRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ExecuteToolRequest)`) returns (`[ExecuteToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ExecuteToolResponse)`) ` Executes the given tool with the given arguments.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `ces.tools.execute`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
RetrieveToolSchema  
---  
` rpc RetrieveToolSchema(`[RetrieveToolSchemaRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.RetrieveToolSchemaRequest)`) returns (`[RetrieveToolSchemaResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.RetrieveToolSchemaResponse)`) ` Retrieve the schema of the given tool. The schema is computed on the fly for the given instance of the tool.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `ces.tools.get`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
RetrieveTools  
---  
` rpc RetrieveTools(`[RetrieveToolsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.RetrieveToolsRequest)`) returns (`[RetrieveToolsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.RetrieveToolsResponse)`) ` Retrieve the list of tools included in the specified toolset.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `toolset` resource:

  * `ces.toolsets.get`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
  
## WidgetService

Provides APIs for widgets to interact with CES APIs.

GenerateChatToken  
---  
` rpc GenerateChatToken(`[GenerateChatTokenRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GenerateChatTokenRequest)`) returns (`[GenerateChatTokenResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GenerateChatTokenResponse)`) ` Generates a session scoped token for chat widget to authenticate with Session APIs.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
  
## Action

Configuration of an Action for the tool to use. Note: This can be either an Action or an Operation. See <https://cloud.google.com/integration-connectors/docs/entities-operation-action> for details.

Fields  
---  
`input_fields[]` |  `string` Optional. Entity fields to use as inputs for the operation. If no fields are specified, all fields of the Entity will be used.  
`output_fields[]` |  `string` Optional. Entity fields to return from the operation. If no fields are specified, all fields of the Entity will be returned.  
Union field `action_spec`. Specification for an action to configure for the tool to use. `action_spec` can be only one of the following:  
`connection_action_id` |  `string` ID of a Connection action for the tool to use.  
`entity_operation` |  `[Action.EntityOperation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Action.EntityOperation)` Entity operation configuration for the tool to use.  
  
## EntityOperation

Entity CRUD operation specification.

Fields  
---  
`entity_id` |  `string` Required. ID of the entity.  
`operation` |  `[Action.EntityOperation.OperationType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Action.EntityOperation.OperationType)` Required. Operation to perform on the entity.  
  
## OperationType

The operation to perform on the entity.

Enums  
---  
`OPERATION_TYPE_UNSPECIFIED` | Operation type unspecified. Invalid, ConnectorTool create/update will fail.  
`LIST` | List operation.  
`GET` | Get operation.  
`CREATE` | Create operation.  
`UPDATE` | Update operation.  
`DELETE` | Delete operation.  
  
## Agent

An agent acts as the fundamental building block that provides instructions to the Large Language Model (LLM) for executing specific tasks.

Fields  
---  
`name` |  `string` Identifier. The unique identifier of the agent. Format: `projects/{project}/locations/{location}/apps/{app}/agents/{agent}`  
`display_name` |  `string` Required. Display name of the agent.  
`description` |  `string` Optional. Human-readable description of the agent.  
`model_settings` |  `[ModelSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ModelSettings)` Optional. Configurations for the LLM model.  
`instruction` |  `string` Optional. Instructions for the LLM model to guide the agent's behavior.  
`tools[]` |  `string` Optional. List of available tools for the agent. Format: `projects/{project}/locations/{location}/apps/{app}/tools/{tool}`  
`child_agents[]` |  `string` Optional. List of child agents in the agent tree. Format: `projects/{project}/locations/{location}/apps/{app}/agents/{agent}`  
`before_agent_callbacks[]` |  `[Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Callback)` Optional. The callbacks to execute before the agent is called. The provided callbacks are executed sequentially in the exact order they are given in the list. If a callback returns an overridden response, execution stops and any remaining callbacks are skipped.  
`after_agent_callbacks[]` |  `[Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Callback)` Optional. The callbacks to execute after the agent is called. The provided callbacks are executed sequentially in the exact order they are given in the list. If a callback returns an overridden response, execution stops and any remaining callbacks are skipped.  
`before_model_callbacks[]` |  `[Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Callback)` Optional. The callbacks to execute before the model is called. If there are multiple calls to the model, the callback will be executed multiple times. The provided callbacks are executed sequentially in the exact order they are given in the list. If a callback returns an overridden response, execution stops and any remaining callbacks are skipped.  
`after_model_callbacks[]` |  `[Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Callback)` Optional. The callbacks to execute after the model is called. If there are multiple calls to the model, the callback will be executed multiple times. The provided callbacks are executed sequentially in the exact order they are given in the list. If a callback returns an overridden response, execution stops and any remaining callbacks are skipped.  
`before_tool_callbacks[]` |  `[Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Callback)` Optional. The callbacks to execute before the tool is invoked. If there are multiple tool invocations, the callback will be executed multiple times. The provided callbacks are executed sequentially in the exact order they are given in the list. If a callback returns an overridden response, execution stops and any remaining callbacks are skipped.  
`after_tool_callbacks[]` |  `[Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Callback)` Optional. The callbacks to execute after the tool is invoked. If there are multiple tool invocations, the callback will be executed multiple times. The provided callbacks are executed sequentially in the exact order they are given in the list. If a callback returns an overridden response, execution stops and any remaining callbacks are skipped.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Timestamp when the agent was created.  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Timestamp when the agent was last updated.  
`guardrails[]` |  `string` Optional. List of guardrails for the agent. Format: `projects/{project}/locations/{location}/apps/{app}/guardrails/{guardrail}`  
`etag` |  `string` Etag used to ensure the object hasn't changed during a read-modify-write operation. If the etag is empty, the update will overwrite any concurrent changes.  
`toolsets[]` |  `[Agent.AgentToolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Agent.AgentToolset)` Optional. List of toolsets for the agent.  
`generated_summary` |  `string` Output only. If the agent is generated by the LLM assistant, this field contains a descriptive summary of the generation.  
`transfer_rules[]` |  `[TransferRule](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.TransferRule)` Optional. Agent transfer rules. If multiple rules match, the first one in the list will be used.  
`validation_errors[]` |  `string` Output only. Misconfigurations or errors in the agent that may affect agent quality.  
Union field `agent_type`. The type of agent. `agent_type` can be only one of the following:  
`llm_agent` |  `[Agent.LlmAgent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Agent.LlmAgent)` Optional. The default agent type.  
`remote_dialogflow_agent` |  `[Agent.RemoteDialogflowAgent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Agent.RemoteDialogflowAgent)` Optional. The remote [Dialogflow](https://cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents) agent to be used for the agent execution. If this field is set, all other agent level properties will be ignored.Note: If the Dialogflow agent is in a different project from the app, you should grant `roles/dialogflow.client` to the CES service agent `service-<PROJECT-NUMBER>@gcp-sa-ces.iam.gserviceaccount.com`.  
`remote_a2a_agent` |  `[Agent.RemoteA2aAgent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Agent.RemoteA2aAgent)` Optional. The remote [A2A](https://github.com/a2aproject/A2A) agent to be used for the agent execution.  
  
## AgentToolset

A toolset with a selection of its tools.

Fields  
---  
`toolset` |  `string` Required. The resource name of the toolset. Format: `projects/{project}/locations/{location}/apps/{app}/toolsets/{toolset}`  
`tool_ids[]` |  `string` Optional. The tools IDs to filter the toolset.  
  
## LlmAgent

This type has no fields.

Default agent type. The agent uses instructions and callbacks specified in the agent to perform the task using a large language model.

## RemoteA2aAgent

The agent which will transfer execution to a remote [A2A](https://github.com/a2aproject/A2A) agent.

Fields  
---  
`a2a_config` |  `[RemoteA2aConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.RemoteA2aConfig)` Required. The A2A connection configuration.  
  
## RemoteDialogflowAgent

The agent which will transfer execution to a remote [Dialogflow CX](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent) agent. The Dialogflow agent will process subsequent user queries until the session ends or flow ends, and the control is transferred back to the parent CES agent.

Fields  
---  
`agent` |  `string` Required. The [Dialogflow](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent) agent resource name. Format: `projects/{project}/locations/{location}/agents/{agent}`  
`flow_id` |  `string` Optional. The flow ID of the flow in the Dialogflow agent.  
`environment_id` |  `string` Optional. The environment ID of the Dialogflow agent to be used for the agent execution. If not specified, the draft environment will be used.  
`input_variable_mapping` |  `map<string, string>` Optional. The mapping of the app variables names to the Dialogflow session parameters names to be sent to the Dialogflow agent as input.  
`output_variable_mapping` |  `map<string, string>` Optional. The mapping of the Dialogflow session parameters names to the app variables names to be sent back to the CES agent after the Dialogflow agent execution ends.  
`respect_response_interruption_settings` |  `bool` Optional. Indicates whether to respect the message-level interruption settings configured in the Dialogflow agent.

  * If false: all response messages from the Dialogflow agent follow the app-level barge-in settings.
  * If true: only response messages with [`allow_playback_interruption`](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#text) set to true will be interruptable, all other messages follow the app-level barge-in settings.

  
`language_code_variable` |  `string` Optional. The name of the variable that contains the language code to be used for the Dialogflow session. If unspecified, the default language code of the Dialogflow agent will be used.  
  
## AgentCard

AgentCard conveys key information about a remote agent. It is a trimmed version of the AgentCard defined in the A2A protocol <https://a2a-protocol.org/dev/specification/#441-agentcard>

Fields  
---  
`name` |  `string` Required. A human-readable name for the agent.  
`description` |  `string` Required. A description of the agent's domain of action/solution space.  
`supported_interfaces[]` |  `[AgentInterface](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentInterface)` Required. Ordered list of supported interfaces. The first entry is preferred.  
`version` |  `string` Required. The version of the agent.  
`skills[]` |  `[AgentSkill](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentSkill)` Required. Skills represent a unit of ability an agent can perform. This may somewhat abstract but represents a more focused set of actions that the agent is highly likely to succeed at.  
  
## AgentInterface

Declares a combination of a target URL, transport and protocol version for interacting with the agent. This allows agents to expose the same functionality over multiple protocol binding mechanisms.

Fields  
---  
`url` |  `string` Required. The URL where this interface is available. Must be a valid absolute HTTPS URL in production. Example: "https://api.example.com/a2a/v1", "https://grpc.example.com/a2a"  
`protocol_binding` |  `string` Required. The protocol binding supported at this URL. This is an open form string, to be easily extended for other protocol bindings. The core ones officially supported are `JSONRPC`, `GRPC` and `HTTP+JSON`.  
`tenant` |  `string` Tenant ID to be used in the request when calling the agent.  
`protocol_version` |  `string` Required. The version of the A2A protocol this interface exposes. Use the latest supported minor version per major version. Examples: "0.3", "1.0"  
  
## AgentRegistryDeployment

Configuration and status for Agent Registry deployment.

Fields  
---  
`agent_registry_service_name` |  `string` Optional. Output only. The resource name of the deployed Agent Registry service. Format: `projects/{project}/locations/{location}/services/{service}`  
  
## AgentSkill

Represents a distinct capability or function that an agent can perform.

Fields  
---  
`id` |  `string` Required. A unique identifier for the agent's skill.  
`name` |  `string` Required. A human-readable name for the skill.  
`description` |  `string` Required. A detailed description of the skill.  
`tags[]` |  `string` Required. A set of keywords describing the skill's capabilities.  
`examples[]` |  `string` Example prompts or scenarios that this skill can handle.  
`input_modes[]` |  `string` The set of supported input media types for this skill, overriding the agent's defaults.  
`output_modes[]` |  `string` The set of supported output media types for this skill, overriding the agent's defaults.  
  
## AgentTool

Represents a tool that allows the agent to call another agent.

Fields  
---  
`name` |  `string` Required. The name of the agent tool.  
`description` |  `string` Optional. Description of the tool's purpose.  
`agent` |  `string` Optional. The resource name of the agent that is the entry point of the tool. Format: `projects/{project}/locations/{location}/agents/{agent}`  
  
## AgentTransfer

Represents an event indicating the transfer of a conversation to a different agent.

Fields  
---  
`target_agent` |  `string` Required. The agent to which the conversation is being transferred. The agent will handle the conversation from this point forward. Format: `projects/{project}/locations/{location}/apps/{app}/agents/{agent}`  
`display_name` |  `string` Output only. Display name of the agent.  
  
## AggregatedMetrics

Aggregated metrics for an evaluation or evaluation dataset.

Fields  
---  
`metrics_by_app_version[]` |  `[AggregatedMetrics.MetricsByAppVersion](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AggregatedMetrics.MetricsByAppVersion)` Output only. Aggregated metrics, grouped by app version ID.  
  
## HallucinationMetrics

Metrics for hallucination results.

Fields  
---  
`score` |  `float` Output only. The average hallucination score (0 to 1).  
  
## MetricsByAppVersion

Metrics aggregated per app version.

Fields  
---  
`app_version_id` |  `string` Output only. The app version ID.  
`tool_metrics[]` |  `[AggregatedMetrics.ToolMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AggregatedMetrics.ToolMetrics)` Output only. Metrics for each tool within this app version.  
`semantic_similarity_metrics[]` |  `[AggregatedMetrics.SemanticSimilarityMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AggregatedMetrics.SemanticSimilarityMetrics)` Output only. Metrics for semantic similarity within this app version.  
`hallucination_metrics[]` |  `[AggregatedMetrics.HallucinationMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AggregatedMetrics.HallucinationMetrics)` Output only. Metrics for hallucination within this app version.  
`tool_call_latency_metrics[]` |  `[AggregatedMetrics.ToolCallLatencyMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AggregatedMetrics.ToolCallLatencyMetrics)` Output only. Metrics for tool call latency within this app version.  
`turn_latency_metrics[]` |  `[AggregatedMetrics.TurnLatencyMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AggregatedMetrics.TurnLatencyMetrics)` Output only. Metrics for turn latency within this app version.  
`pass_count` |  `int32` Output only. The number of times the evaluation passed.  
`fail_count` |  `int32` Output only. The number of times the evaluation failed.  
`metrics_by_turn[]` |  `[AggregatedMetrics.MetricsByTurn](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AggregatedMetrics.MetricsByTurn)` Output only. Metrics aggregated per turn within this app version.  
  
## MetricsByTurn

Metrics aggregated per turn.

Fields  
---  
`turn_index` |  `int32` Output only. The turn index (0-based).  
`tool_metrics[]` |  `[AggregatedMetrics.ToolMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AggregatedMetrics.ToolMetrics)` Output only. Metrics for each tool within this turn.  
`semantic_similarity_metrics[]` |  `[AggregatedMetrics.SemanticSimilarityMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AggregatedMetrics.SemanticSimilarityMetrics)` Output only. Metrics for semantic similarity within this turn.  
`hallucination_metrics[]` |  `[AggregatedMetrics.HallucinationMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AggregatedMetrics.HallucinationMetrics)` Output only. Metrics for hallucination within this turn.  
`tool_call_latency_metrics[]` |  `[AggregatedMetrics.ToolCallLatencyMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AggregatedMetrics.ToolCallLatencyMetrics)` Output only. Metrics for tool call latency within this turn.  
`turn_latency_metrics[]` |  `[AggregatedMetrics.TurnLatencyMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AggregatedMetrics.TurnLatencyMetrics)` Output only. Metrics for turn latency within this turn.  
  
## SemanticSimilarityMetrics

Metrics for semantic similarity results.

Fields  
---  
`score` |  `float` Output only. The average semantic similarity score (0-4).  
  
## ToolCallLatencyMetrics

Metrics for tool call latency.

Fields  
---  
`tool` |  `string` Output only. The name of the tool.  
`average_latency` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Output only. The average latency of the tool calls.  
  
## ToolMetrics

Metrics for a single tool.

Fields  
---  
`tool` |  `string` Output only. The name of the tool.  
`pass_count` |  `int32` Output only. The number of times the tool passed.  
`fail_count` |  `int32` Output only. The number of times the tool failed.  
  
## TurnLatencyMetrics

Metrics for turn latency.

Fields  
---  
`average_latency` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Output only. The average latency of the turns.  
  
## AmbientSoundConfig

Configuration for the ambient sound to be played with the synthesized agent response, to enhance the naturalness of the conversation.

Fields  
---  
`volume_gain_db` |  `double` Optional. Volume gain (in dB) of the normal native volume supported by ambient noise, in the range [-96.0, 16.0]. If unset, or set to a value of 0.0 (dB), will play at normal native signal amplitude. A value of -6.0 (dB) will play at approximately half the amplitude of the normal native signal amplitude. A value of +6.0 (dB) will play at approximately twice the amplitude of the normal native signal amplitude. We strongly recommend not to exceed +10 (dB) as there's usually no effective increase in loudness for any value greater than that.  
Union field `source`. Ambient noise to be played with the synthesized agent response, to enhance the naturalness of the conversation. `source` can be only one of the following:  
`prebuilt_ambient_noise  
**(deprecated)**` |  `[AmbientSoundConfig.PrebuiltAmbientNoise](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AmbientSoundConfig.PrebuiltAmbientNoise)` This item is deprecated!Optional. Deprecated: `prebuilt_ambient_noise` is deprecated in favor of `prebuilt_ambient_sound`.  
`gcs_uri` |  `string` Optional. Ambient noise as a mono-channel, 16kHz WAV file stored in [Cloud Storage](https://cloud.google.com/storage).Note: Please make sure the CES service agent `service-<PROJECT-NUMBER>@gcp-sa-ces.iam.gserviceaccount.com` has `storage.objects.get` permission to the Cloud Storage object.  
`prebuilt_ambient_sound` |  `string` Optional. Name of the prebuilt ambient sound. Valid values are: - "coffee_shop" - "keyboard" - "keypad" - "hum" - "office_1" - "office_2" - "office_3" - "room_1" - "room_2" - "room_3" - "room_4" - "room_5" - "air_conditioner"  
  
## PrebuiltAmbientNoise

Prebuilt ambient noise.

Enums  
---  
`PREBUILT_AMBIENT_NOISE_UNSPECIFIED` | Not specified.  
`RETAIL_STORE` | Ambient noise of a retail store.  
`CONVENTION_HALL` | Ambient noise of a convention hall.  
`OUTDOOR` | Ambient noise of a street.  
  
## ApiAuthentication

Authentication information required for API calls.

Fields  
---  
Union field `auth_config`. The auth configuration. `auth_config` can be only one of the following:  
`api_key_config` |  `[ApiKeyConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ApiKeyConfig)` Optional. Config for API key auth.  
`oauth_config` |  `[OAuthConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.OAuthConfig)` Optional. Config for OAuth.  
`service_agent_id_token_auth_config` |  `[ServiceAgentIdTokenAuthConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ServiceAgentIdTokenAuthConfig)` Optional. Config for ID token auth generated from CES service agent.  
`service_account_auth_config` |  `[ServiceAccountAuthConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ServiceAccountAuthConfig)` Optional. Config for service account authentication.  
`bearer_token_config` |  `[BearerTokenConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.BearerTokenConfig)` Optional. Config for bearer token auth.  
  
## ApiKeyConfig

Configurations for authentication with API key.

Fields  
---  
`key_name` |  `string` Required. The parameter name or the header name of the API key. E.g., If the API request is "https://example.com/act?X-Api-Key=", "X-Api-Key" would be the parameter name.  
`api_key_secret_version` |  `string` Required. The name of the SecretManager secret version resource storing the API key. Format: `projects/{project}/secrets/{secret}/versions/{version}`Note: You should grant `roles/secretmanager.secretAccessor` role to the CES service agent `service-<PROJECT-NUMBER>@gcp-sa-ces.iam.gserviceaccount.com`.  
`request_location` |  `[ApiKeyConfig.RequestLocation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ApiKeyConfig.RequestLocation)` Required. Key location in the request.  
  
## RequestLocation

The location of the API key in the request.

Enums  
---  
`REQUEST_LOCATION_UNSPECIFIED` | Unspecified. This value should not be used.  
`HEADER` | Represents the key in http header.  
`QUERY_STRING` | Represents the key in query string.  
  
## App

An app serves as a top-level container for a group of agents, including the root agent and its sub-agents, along with their associated configurations. These agents work together to achieve specific goals within the app's context.

Fields  
---  
`name` |  `string` Identifier. The unique identifier of the app. Format: `projects/{project}/locations/{location}/apps/{app}`  
`display_name` |  `string` Required. Display name of the app.  
`description` |  `string` Optional. Human-readable description of the app.  
`pinned` |  `bool` Optional. Whether the app is pinned in the app list.  
`root_agent` |  `string` Optional. The root agent is the entry point of the app. Format: `projects/{project}/locations/{location}/apps/{app}/agents/{agent}`  
`language_settings` |  `[LanguageSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.LanguageSettings)` Optional. Language settings of the app.  
`time_zone_settings` |  `[TimeZoneSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.TimeZoneSettings)` Optional. TimeZone settings of the app.  
`audio_processing_config` |  `[AudioProcessingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AudioProcessingConfig)` Optional. Audio processing configuration of the app.  
`logging_settings` |  `[LoggingSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.LoggingSettings)` Optional. Logging settings of the app.  
`error_handling_settings` |  `[ErrorHandlingSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ErrorHandlingSettings)` Optional. Error handling settings of the app.  
`model_settings` |  `[ModelSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ModelSettings)` Optional. The default LLM model settings for the app. Individual resources (e.g. agents, guardrails) can override these configurations as needed.  
`tool_execution_mode` |  `[App.ToolExecutionMode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.App.ToolExecutionMode)` Optional. The tool execution mode for the app. If not provided, will default to PARALLEL.  
`evaluation_metrics_thresholds` |  `[EvaluationMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationMetricsThresholds)` Optional. The evaluation thresholds for the app.  
`variable_declarations[]` |  `[App.VariableDeclaration](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.App.VariableDeclaration)` Optional. The declarations of the variables.  
`predefined_variable_declarations[]` |  `[App.VariableDeclaration](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.App.VariableDeclaration)` Output only. The declarations of predefined variables for the app.  
`global_instruction` |  `string` Optional. Instructions for all the agents in the app. You can use this instruction to set up a stable identity or personality across all the agents.  
`guardrails[]` |  `string` Optional. List of guardrails for the app. Format: `projects/{project}/locations/{location}/apps/{app}/guardrails/{guardrail}`  
`data_store_settings` |  `[DataStoreSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DataStoreSettings)` Optional. The data store settings for the app.  
`default_channel_profile` |  `[ChannelProfile](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ChannelProfile)` Optional. The default channel profile used by the app.  
`metadata` |  `map<string, string>` Optional. Metadata about the app. This field can be used to store additional information relevant to the app's details or intended usages.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Timestamp when the app was created.  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Timestamp when the app was last updated.  
`etag` |  `string` Output only. Etag used to ensure the object hasn't changed during a read-modify-write operation. If the etag is empty, the update will overwrite any concurrent changes.  
`deployment_count` |  `int32` Output only. Number of deployments in the app.  
`client_certificate_settings` |  `[ClientCertificateSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ClientCertificateSettings)` Optional. The default client certificate settings for the app.  
`vpc_sc_settings` |  `[VpcScSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.VpcScSettings)` Optional. VPC-SC settings for the app.  
`locked` |  `bool` Optional. Indicates whether the app is locked for changes. If the app is locked, modifications to the app resources will be rejected.  
`evaluation_personas[]` |  `[EvaluationPersona](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationPersona)` Optional. The evaluation personas for the app. This field is used to define the personas that can be used for evaluation. Maximum of 30 personas can be defined.  
`evaluation_settings` |  `[EvaluationSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationSettings)` Optional. The evaluation settings for the app.  
`validation_errors[]` |  `string` Output only. Misconfigurations or warnings in the app.  
`dashboard_settings` |  `[DashboardSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DashboardSettings)` Optional. App-specific dashboard settings for linking and configuring Contact Center Insights dashboards.  
  
## ToolExecutionMode

Defines the tool execution behavior if there are **multiple** tools being selected by the agent **at the same time**.

Enums  
---  
`TOOL_EXECUTION_MODE_UNSPECIFIED` | Unspecified tool execution mode. Default to PARALLEL.  
`PARALLEL` | If there are multiple tools being selected, they will be executed in parallel, with the same [ToolContext](https://google.github.io/adk-docs/context/#the-different-types-of-context).  
`SEQUENTIAL` | If there are multiple tools being selected, they will be executed sequentially. The next tool will only be executed after the previous tool completes and it can see updated [ToolContext](https://google.github.io/adk-docs/context/#the-different-types-of-context) from the previous tool.  
  
## VariableDeclaration

Defines the structure and metadata for a variable.

Fields  
---  
`name` |  `string` Required. The name of the variable. The name must start with a letter or underscore and contain only letters, numbers, or underscores.  
`description` |  `string` Required. The description of the variable.  
`schema` |  `[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Schema)` Required. The schema of the variable.  
  
## AppSnapshot

A snapshot of the app.

Fields  
---  
`app` |  `[App](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.App)` Optional. The basic settings for the app.  
`agents[]` |  `[Agent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Agent)` Optional. List of agents in the app.  
`tools[]` |  `[Tool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Tool)` Optional. List of tools in the app.  
`examples[]` |  `[Example](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Example)` Optional. List of examples in the app.  
`guardrails[]` |  `[Guardrail](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Guardrail)` Optional. List of guardrails in the app.  
`toolsets[]` |  `[Toolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Toolset)` Optional. List of toolsets in the app.  
  
## AppVersion

In Customer Engagement Suite (CES), an app version is a snapshot of the app at a specific point in time. It is immutable and cannot be modified once created.

Fields  
---  
`name` |  `string` Identifier. The unique identifier of the app version. Format: `projects/{project}/locations/{location}/apps/{app}/versions/{version}`  
`display_name` |  `string` Optional. The display name of the app version.  
`description` |  `string` Optional. The description of the app version.  
`creator` |  `string` Output only. Email of the user who created the app version.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Timestamp when the app version was created.  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Timestamp when the app version was last updated.  
`snapshot` |  `[AppSnapshot](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AppSnapshot)` Output only. The snapshot of the app when the version is created.  
`etag` |  `string` Output only. Etag used to ensure the object hasn't changed during a read-modify-write operation. If the etag is empty, the update will overwrite any concurrent changes.  
  
## AudioEncoding

AudioEncoding specifies the encoding format for audio data.

Enums  
---  
`AUDIO_ENCODING_UNSPECIFIED` | Unspecified audio encoding.  
`LINEAR16` | 16-bit linear PCM audio encoding.  
`MULAW` | 8-bit samples that compand 14-bit audio samples using G.711 PCMU/mu-law.  
`ALAW` | 8-bit samples that compand 14-bit audio samples using G.711 PCMU/A-law.  
  
## AudioProcessingConfig

Configuration for how the input and output audio should be processed and delivered.

Fields  
---  
`synthesize_speech_configs` |  `map<string, `[SynthesizeSpeechConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.SynthesizeSpeechConfig)`>` Optional. Configuration of how the agent response should be synthesized, mapping from the language code to `[SynthesizeSpeechConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.SynthesizeSpeechConfig)`.If the configuration for the specified language code is not found, the configuration for the root language code will be used. For example, if the map contains "en-us" and "en", and the specified language code is "en-gb", then "en" configuration will be used.Note: Language code is case-insensitive.  
`barge_in_config` |  `[BargeInConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.BargeInConfig)` Optional. Configures the agent behavior for the user barge-in activities.  
`inactivity_timeout` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Optional. The duration of user inactivity (no speech or interaction) before the agent prompts the user for reengagement. If not set, the agent will not prompt the user for reengagement.  
`ambient_sound_config` |  `[AmbientSoundConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AmbientSoundConfig)` Optional. Configuration for the ambient sound to be played with the synthesized agent response, to enhance the naturalness of the conversation.  
`custom_voice_samples[]` |  `[CustomVoiceSample](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.CustomVoiceSample)` Optional. Configures custom voice samples for voice cloning.  
  
## AudioRecordingConfig

Configuration for how the audio interactions should be recorded.

Fields  
---  
`gcs_bucket` |  `string` Optional. The [Cloud Storage](https://cloud.google.com/storage) bucket to store the session audio recordings. The URI must start with "gs://".Please choose a bucket location that meets your data residency requirements.Note: If the Cloud Storage bucket is in a different project from the app, you should grant `storage.objects.create` permission to the CES service agent `service-<PROJECT-NUMBER>@gcp-sa-ces.iam.gserviceaccount.com`.  
`gcs_path_prefix` |  `string` Optional. The Cloud Storage path prefix for audio recordings.This prefix can include the following placeholders, which will be dynamically substituted at serving time: - $project: project ID - $location: app location - $app: app ID - $date: session date in YYYY-MM-DD format - $session: session IDIf the path prefix is not specified, the default prefix `$project/$location/$app/$date/$session/` will be used.  
  
## BargeInConfig

Configuration for how the user barge-in activities should be handled.

Fields  
---  
`disable_barge_in  
**(deprecated)**` |  `bool` This item is deprecated!Optional. Deprecated: `disable_barge_in` is deprecated in favor of `[`disable_barge_in_control`](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ChannelProfile.FIELDS.bool.google.cloud.ces.v1beta.ChannelProfile.disable_barge_in_control)` in ChannelProfile.Disables user barge-in while the agent is speaking. If true, user input during agent response playback will be ignored.  
`barge_in_awareness` |  `bool` Optional. If enabled, the agent will adapt its next response based on the assumption that the user hasn't heard the full preceding agent message. This should not be used in scenarios where agent responses are displayed visually.  
  
## BatchDeleteConversationsRequest

Request message for `[AgentService.BatchDeleteConversations](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.BatchDeleteConversations)`.

Fields  
---  
`parent` |  `string` Required. The resource name of the app to delete conversations from. Format: `projects/{project}/locations/{location}/apps/{app}`  
`conversations[]` |  `string` Required. The resource names of the conversations to delete.  
  
## BatchDeleteConversationsResponse

Response message for `[AgentService.BatchDeleteConversations](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.BatchDeleteConversations)`.

Fields  
---  
`deleted_conversations[]` |  `string` The list of conversations that were successfully deleted.  
`failed_conversations[]` |  `string` The list of conversations that failed to be deleted.  
`error_messages[]` |  `string` Optional. A list of error messages associated with conversations that failed to be deleted.  
  
## BearerTokenConfig

Configurations for authentication with a bearer token.

Fields  
---  
`token` |  `string` Required. The bearer token. Must be in the format `$context.variables.<name_of_variable>`.  
  
## BidiSessionClientMessage

The top-level message sent by the client for the `[SessionService.BidiRunSession](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.SessionService.BidiRunSession)` method.

Fields  
---  
Union field `message_type`. The type of the message. `message_type` can be only one of the following:  
`config` |  `[SessionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.SessionConfig)` Optional. The initial config message for the session.  
`realtime_input` |  `[SessionInput](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.SessionInput)` Optional. Realtime input for the session.  
  
## BidiSessionServerMessage

The top-level message returned from `[SessionService.BidiRunSession](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.SessionService.BidiRunSession)` method.

Fields  
---  
Union field `message_type`. The type of the message. `message_type` can be only one of the following:  
`session_output` |  `[SessionOutput](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.SessionOutput)` Optional. Processing result from the CES agent.  
`recognition_result` |  `[RecognitionResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.RecognitionResult)` Optional. Realtime speech recognition result for the audio input.  
`interruption_signal` |  `[InterruptionSignal](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.InterruptionSignal)` Optional. Indicates the agent's audio response has been interrupted.  
`end_session` |  `[EndSession](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EndSession)` Optional. Indicates that the session has ended.  
`go_away` |  `[GoAway](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GoAway)` Optional. Indicates that the server will disconnect soon and the client should half-close and restart the connection.  
  
## BigQueryExportSettings

Settings to describe the BigQuery export behaviors for the app.

Fields  
---  
`enabled` |  `bool` Optional. Indicates whether the BigQuery export is enabled.  
`project` |  `string` Optional. The **project ID** of the BigQuery dataset to export the data to.Note: If the BigQuery dataset is in a different project from the app, you should grant `roles/bigquery.admin` role to the CES service agent `service-<PROJECT-NUMBER>@gcp-sa-ces.iam.gserviceaccount.com`.  
`dataset` |  `string` Optional. The BigQuery **dataset ID** to export the data to.  
  
## Blob

Represents a blob input or output in the conversation.

Fields  
---  
`mime_type` |  `string` Required. The IANA standard MIME type of the source data.  
`data` |  `bytes` Required. Raw bytes of the blob.  
  
## Callback

A callback defines the custom logic to be executed at various stages of agent interaction.

Fields  
---  
`description` |  `string` Optional. Human-readable description of the callback.  
`disabled` |  `bool` Optional. Whether the callback is disabled. Disabled callbacks are ignored by the agent.  
`proactive_execution_enabled` |  `bool` Optional. If enabled, the callback will also be executed on intermediate model outputs. This setting only affects after model callback. **ENABLE WITH CAUTION**. Typically after model callback only needs to be executed after receiving all model responses. Enabling proactive execution may have negative implication on the execution cost and latency, and should only be enabled in rare situations.  
Union field `callback`. The callback to execute. `callback` can be only one of the following:  
`python_code` |  `string` Required. The python code to execute for the callback.  
  
## Changelog

Changelogs represent a change made to the app or to an resource within the app.

Fields  
---  
`name` |  `string` Identifier. The unique identifier of the changelog. Format: `projects/{project}/locations/{location}/apps/{app}/changelogs/{changelog}`  
`author` |  `string` Output only. Email address of the change author.  
`display_name` |  `string` Output only. Display name of the change. It typically should be the display name of the resource that was changed.  
`description` |  `string` Output only. Description of the change. which typically captures the changed fields in the resource.  
`resource` |  `string` Output only. The resource that was changed.  
`resource_type` |  `string` Output only. The type of the resource that was changed.  
`action` |  `string` Output only. The action that was performed on the resource.  
`original_resource` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` Output only. The original resource before the change.  
`new_resource` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` Output only. The new resource after the change.  
`dependent_resources[]` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` Output only. The dependent resources that were changed.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time when the change was made.  
`sequence_number` |  `int64` Output only. The monotonically increasing sequence number of the changelog.  
  
## ChannelProfile

A ChannelProfile configures the agent's behavior for a specific communication channel, such as web UI or telephony.

Fields  
---  
`profile_id` |  `string` Optional. The unique identifier of the channel profile.  
`channel_type` |  `[ChannelProfile.ChannelType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ChannelProfile.ChannelType)` Optional. The type of the channel profile.  
`persona_property` |  `[ChannelProfile.PersonaProperty](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ChannelProfile.PersonaProperty)` Optional. The persona property of the channel profile.  
`web_widget_config` |  `[ChannelProfile.WebWidgetConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ChannelProfile.WebWidgetConfig)` Optional. The configuration for the web widget.  
`whatsapp_config` |  `[ChannelProfile.WhatsAppConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ChannelProfile.WhatsAppConfig)` Optional. Configuration specific to WhatsApp deployments.  
`instagram_config` |  `[ChannelProfile.InstagramConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ChannelProfile.InstagramConfig)` Optional. Configuration specific to Instagram deployments.  
`disable_dtmf` |  `bool` Optional. Whether to disable DTMF (dual-tone multi-frequency).  
`disable_barge_in_control` |  `bool` Optional. Whether to disable user barge-in control in the conversation. - **true** : User interruptions are disabled while the agent is speaking. - **false** : The agent retains automatic control over when the user can interrupt.  
`noise_suppression_level` |  `string` Optional. The noise suppression level of the channel profile. Available values are "low", "moderate", "high", "very_high".  
  
## ChannelType

The type of the channel profile.

Enums  
---  
`UNKNOWN` | Unknown channel type.  
`WEB_UI` | Web UI channel.  
`API` | API channel.  
`TWILIO` | Twilio channel.  
`GOOGLE_TELEPHONY_PLATFORM` | Google Telephony Platform channel.  
`CONTACT_CENTER_AS_A_SERVICE` | Contact Center as a Service (CCaaS) channel.  
`CONTACT_CENTER_AS_A_SERVICE_CHAT` | Contact Center as a Service (CCaaS Chat) channel.  
`FIVE9` | Five9 channel.  
`CONTACT_CENTER_INTEGRATION` | Third party contact center integration channel.  
`WHATSAPP` | WhatsApp channel.  
`INSTAGRAM` | Instagram channel.  
  
## InstagramConfig

Configuration specific to Instagram deployments.

Fields  
---  
`instagram_account_id` |  `string` Required. The Instagram Account ID.  
`display_name` |  `string` Output only. The fetched Meta business page name.  
`thumbnail_url` |  `string` Output only. The fetched Meta business profile thumbnail URL.  
`description` |  `string` Output only. The description of the Meta business page or profile.  
  
## PersonaProperty

Represents the persona property of a channel.

Fields  
---  
`persona` |  `[ChannelProfile.PersonaProperty.Persona](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ChannelProfile.PersonaProperty.Persona)` Optional. The persona of the channel.  
  
## Persona

The persona of the channel.

Enums  
---  
`UNKNOWN` | UNKNOWN persona.  
`CONCISE` | The agent keeps the responses concise and to the point  
`CHATTY` | The agent provides additional context, explanations, and details  
  
## WebWidgetConfig

Message for configuration for the web widget.

Fields  
---  
`modality` |  `[ChannelProfile.WebWidgetConfig.Modality](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ChannelProfile.WebWidgetConfig.Modality)` Optional. The modality of the web widget.  
`theme` |  `[ChannelProfile.WebWidgetConfig.Theme](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ChannelProfile.WebWidgetConfig.Theme)` Optional. The theme of the web widget.  
`web_widget_title` |  `string` Optional. The title of the web widget.  
`security_settings` |  `[ChannelProfile.WebWidgetConfig.SecuritySettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ChannelProfile.WebWidgetConfig.SecuritySettings)` Optional. The security settings of the web widget.  
  
## Modality

Modality of the web widget.

Enums  
---  
`MODALITY_UNSPECIFIED` | Unknown modality.  
`CHAT_AND_VOICE` | Widget supports both chat and voice input.  
`VOICE_ONLY` | Widget supports only voice input.  
`CHAT_ONLY` | Widget supports only chat input.  
`CHAT_VOICE_AND_VIDEO` | Widget supports chat, voice, and video input.  
  
## SecuritySettings

Security settings for the web widget.

Fields  
---  
`enable_public_access` |  `bool` Optional. Indicates whether public access to the web widget is enabled. If `true`, the web widget will be publicly accessible. If `false`, the web widget must be integrated with your own authentication and authorization system to return valid credentials for accessing the CES agent.  
`enable_origin_check` |  `bool` Optional. Indicates whether origin check for the web widget is enabled. If `true`, the web widget will check the origin of the website that loads the web widget and only allow it to be loaded in the same origin or any of the allowed origins.  
`allowed_origins[]` |  `string` Optional. The origins that are allowed to host the web widget. An origin is defined by RFC 6454. If empty, all origins are allowed. A maximum of 100 origins is allowed. Example: "https://example.com"  
`enable_recaptcha` |  `bool` Optional. Indicates whether reCAPTCHA verification for the web widget is enabled.  
  
## Theme

Theme of the web widget.

Enums  
---  
`THEME_UNSPECIFIED` | Unknown theme.  
`LIGHT` | Light theme.  
`DARK` | Dark theme.  
  
## WhatsAppConfig

Configuration specific to WhatsApp deployments.

Fields  
---  
`waba_id` |  `string` Required. The WhatsApp Business Account ID.  
`phone_number_id` |  `string` Required. The Meta phone number ID.  
`phone_number` |  `string` Optional. The phone number in E.164 format.  
`display_name` |  `string` Output only. The fetched Meta business page name.  
`thumbnail_url` |  `string` Output only. The fetched Meta business profile thumbnail URL.  
`description` |  `string` Output only. The description of the Meta business page or profile.  
  
## Chunk

A chunk of content within a message.

Fields  
---  
Union field `data`. Chunk data. `data` can be only one of the following:  
`text` |  `string` Optional. Text data.  
`transcript` |  `string` Optional. Transcript associated with the audio.  
`blob` |  `[Blob](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Blob)` Optional. Blob data.  
`payload` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` Optional. Custom payload data.  
`image` |  `[Image](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Image)` Optional. Image data.  
`tool_call` |  `[ToolCall](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ToolCall)` Optional. Tool execution request.  
`tool_response` |  `[ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ToolResponse)` Optional. Tool execution response.  
`agent_transfer` |  `[AgentTransfer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentTransfer)` Optional. Agent transfer event.  
`updated_variables` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` A struct represents variables that were updated in the conversation, keyed by variable names.  
`default_variables` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` A struct represents default variables at the start of the conversation, keyed by variable names.  
  
## Citations

Citations associated with the agent response.

Fields  
---  
`cited_chunks[]` |  `[Citations.CitedChunk](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Citations.CitedChunk)` List of cited pieces of information.  
`inline_citations[]` |  `[Citations.InlineCitation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Citations.InlineCitation)` Optional. List of inline citations in the agent response.  
  
## CitedChunk

Piece of cited information.

Fields  
---  
`uri` |  `string` URI used for citation.  
`title` |  `string` Title of the cited document.  
`text` |  `string` Text used for citation.  
`requires_attribution` |  `bool` Whether this citation requires attribution to be shown to the end users.  
  
## InlineCitation

An inline citation in the response text.

Fields  
---  
`start_index` |  `int32` The starting index (in bytes) of the text segment in the agent response.  
`end_index` |  `int32` The ending index (in bytes) of the text segment in the agent response.  
`cited_chunk_indices[]` |  `int32` The indices of the cited chunks that back this text segment. Indices refer to the elements in `cited_chunks`.  
  
## ClientCertificateSettings

Settings for custom client certificates.

Fields  
---  
`tls_certificate` |  `string` Required. The TLS certificate encoded in PEM format. This string must include the begin header and end footer lines.  
`private_key` |  `string` Required. The name of the SecretManager secret version resource storing the private key encoded in PEM format. Format: `projects/{project}/secrets/{secret}/versions/{version}`  
`passphrase` |  `string` Optional. The name of the SecretManager secret version resource storing the passphrase to decrypt the private key. Should be left unset if the private key is not encrypted. Format: `projects/{project}/secrets/{secret}/versions/{version}`  
  
## ClientFunction

Represents a client-side function that the agent can invoke. When the tool is chosen by the agent, control is handed off to the client. The client is responsible for executing the function and returning the result as a `[ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ToolResponse)` to continue the interaction with the agent.

Fields  
---  
`name` |  `string` Required. The function name.  
`description` |  `string` Optional. The function description.  
`parameters` |  `[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Schema)` Optional. The schema of the function parameters.  
`response` |  `[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Schema)` Optional. The schema of the function response.  
  
## CloudLoggingSettings

Settings to describe the Cloud Logging behaviors for the app.

Fields  
---  
`enable_cloud_logging` |  `bool` Optional. Whether to enable Cloud Logging for the sessions.  
  
## CodeBlock

A code block to be executed instead of a real tool call.

Fields  
---  
`python_code` |  `string` Required. Python code which will be invoked in tool fake mode. Expected Python function signature - To catch all tool calls: def fake_tool_call(tool: Tool, input: dict[str, Any], callback_context: CallbackContext) -> Optional[dict[str, Any]]: To catch a specific tool call: def fake_{tool_id}(tool: Tool, input: dict[str, Any], callback_context: CallbackContext) -> Optional[dict[str, Any]]: If the function returns None, the real tool will be invoked instead.  
  
## ConnectorTool

A ConnectorTool allows connections to different integrations. See: <https://cloud.google.com/integration-connectors/docs/overview>.

Fields  
---  
`connection` |  `string` Required. The full resource name of the referenced Integration Connectors Connection. Format: `projects/{project}/locations/{location}/connections/{connection}`  
`action` |  `[Action](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Action)` Required. Action for the tool to use.  
`auth_config` |  `[EndUserAuthConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EndUserAuthConfig)` Optional. Configures how authentication is handled in Integration Connectors. By default, an admin authentication is passed in the Integration Connectors API requests. You can override it with a different end-user authentication config. **Note** : The Connection must have authentication override enabled in order to specify an EUC configuration here - otherwise, the ConnectorTool creation will fail. See <https://cloud.google.com/application-integration/docs/configure-connectors-task#configure-authentication-override> for details.  
`name` |  `string` Optional. The name of the tool that can be used by the Agent to decide whether to call this ConnectorTool.  
`description` |  `string` Optional. The description of the tool that can be used by the Agent to decide whether to call this ConnectorTool.  
  
## ConnectorToolset

A toolset that generates tools from an Integration Connectors Connection.

Fields  
---  
`connection` |  `string` Required. The full resource name of the referenced Integration Connectors Connection. Format: `projects/{project}/locations/{location}/connections/{connection}`  
`auth_config` |  `[EndUserAuthConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EndUserAuthConfig)` Optional. Configures how authentication is handled in Integration Connectors. By default, an admin authentication is passed in the Integration Connectors API requests. You can override it with a different end-user authentication config. **Note** : The Connection must have authentication override enabled in order to specify an EUC configuration here - otherwise, the Toolset creation will fail. See: <https://cloud.google.com/application-integration/docs/configure-connectors-task#configure-authentication-override>  
`connector_actions[]` |  `[Action](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Action)` Required. The list of connector actions/entity operations to generate tools for.  
  
## Conversation

A conversation represents an interaction between an end user and the CES app.

Fields  
---  
`name` |  `string` Identifier. The unique identifier of the conversation. Format: `projects/{project}/locations/{location}/apps/{app}/conversations/{conversation}`  
`start_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Timestamp when the conversation was created.  
`end_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Timestamp when the conversation was completed.  
`turns[]` |  `[Conversation.Turn](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Conversation.Turn)` Required. The turns in the conversation.  
`turn_count` |  `int32` Output only. The number of turns in the conversation.  
`channel_type  
**(deprecated)**` |  `[Conversation.ChannelType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Conversation.ChannelType)` This item is deprecated!DEPRECATED. Please use `[input_types](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Conversation.FIELDS.repeated.google.cloud.ces.v1beta.Conversation.InputType.google.cloud.ces.v1beta.Conversation.input_types)` instead.  
`source` |  `[Conversation.Source](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Conversation.Source)` Output only. Indicate the source of the conversation.  
`input_types[]` |  `[Conversation.InputType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Conversation.InputType)` Output only. The input types of the conversation.  
`entry_agent` |  `string` Output only. The agent that initially handles the conversation. If not specified, the conversation is handled by the root agent. Format: `projects/{project}/locations/{location}/apps/{app}/agents/{agent}`  
`deployment` |  `string` Output only. The deployment of the app used for processing the conversation. Format: `projects/{project}/locations/{location}/apps/{app}/deployments/{deployment}`  
`app_version` |  `string` Output only. The version of the app used for processing the conversation. Format: `projects/{project}/locations/{location}/apps/{app}/versions/{version}`  
`language_code` |  `string` Output only. The language code of the conversation.  
`messages[]  
**(deprecated)**` |  `[Message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Message)` This item is deprecated!Deprecated. Use turns instead.  
  
## ChannelType

The channel type of the conversation.

Enums  
---  
`CHANNEL_TYPE_UNSPECIFIED` | Unspecified channel type.  
`TEXT` | The conversation only contains text messages between the end user and the agent.  
`AUDIO` | The conversation contains audio messages between the end user and the agent.  
`MULTIMODAL` | The conversation multi-modal messages (e.g. image) between the end user and the agent.  
  
## InputType

Type of the input message.

Enums  
---  
`INPUT_TYPE_UNSPECIFIED` | Unspecified input type.  
`INPUT_TYPE_TEXT` | Text input.  
`INPUT_TYPE_EVENT` | Event input.  
`INPUT_TYPE_AUDIO` | Audio input.  
`INPUT_TYPE_IMAGE` | Image input.  
`INPUT_TYPE_BLOB` | Blob input.  
`INPUT_TYPE_TOOL_RESPONSE` | Client function tool response input.  
`INPUT_TYPE_VARIABLES` | Variables input.  
  
## Source

The source of the conversation.

Enums  
---  
`SOURCE_UNSPECIFIED` | Unspecified source.  
`LIVE` | The conversation is from the live end user.  
`SIMULATOR` | The conversation is from the simulator.  
`EVAL` | The conversation is from the evaluation.  
`AGENT_TOOL` | The conversation is from an agent tool. Agent tool runs the agent in a separate session, which is persisted for testing and debugging purposes.  
  
## Turn

All information about a single turn in the conversation.

Fields  
---  
`messages[]` |  `[Message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Message)` Optional. List of messages in the conversation turn, including user input, agent responses and intermediate events during the processing.  
`root_span` |  `[Span](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Span)` Optional. The root span of the action processing.  
`user_intended_text` |  `string` Optional. The intended ground-truth text from the Simulated Caller (Polysynth). Only populated when word error rate metrics are enabled.  
  
## ConversationLoggingSettings

Settings to describe the conversation logging behaviors for the app.

Fields  
---  
`disable_conversation_logging` |  `bool` Optional. Whether to disable conversation logging for the sessions.  
`retention_window` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Optional. Controls the retention window for the conversation. If not set, the conversation will be retained for 365 days.  
  
## CreateAgentRequest

Fields  
---  
`parent` |  `string` Required. The resource name of the app to create an agent in.  
`agent_id` |  `string` Optional. The ID to use for the agent, which will become the final component of the agent's resource name. If not provided, a unique ID will be automatically assigned for the agent.  
`agent` |  `[Agent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Agent)` Required. The agent to create.  
  
## CreateAppRequest

Request message for `[AgentService.CreateApp](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.CreateApp)`.

Fields  
---  
`parent` |  `string` Required. The resource name of the location to create an app in.  
`app_id` |  `string` Optional. The ID to use for the app, which will become the final component of the app's resource name. If not provided, a unique ID will be automatically assigned for the app.  
`app` |  `[App](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.App)` Required. The app to create.  
  
## CreateAppVersionRequest

Request message for `[AgentService.CreateAppVersion](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.CreateAppVersion)`

Fields  
---  
`parent` |  `string` Required. The resource name of the app to create an app version in.  
`app_version_id` |  `string` Optional. The ID to use for the app version, which will become the final component of the app version's resource name. If not provided, a unique ID will be automatically assigned for the app version.  
`app_version` |  `[AppVersion](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AppVersion)` Required. The app version to create.  
  
## CreateDeploymentRequest

Request message for `[AgentService.CreateDeployment](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.CreateDeployment)`.

Fields  
---  
`parent` |  `string` Required. The parent app. Format: `projects/{project}/locations/{location}/apps/{app}`  
`deployment_id` |  `string` Optional. The ID to use for the deployment, which will become the final component of the deployment's resource name. If not provided, a unique ID will be automatically assigned for the deployment.  
`deployment` |  `[Deployment](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Deployment)` Required. The deployment to create.  
  
## CreateEvaluationDatasetRequest

Request message for `[EvaluationService.CreateEvaluationDataset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationService.CreateEvaluationDataset)`.

Fields  
---  
`parent` |  `string` Required. The app to create the evaluation for. Format: `projects/{project}/locations/{location}/apps/{app}`  
`evaluation_dataset_id` |  `string` Optional. The ID to use for the evaluation dataset, which will become the final component of the evaluation dataset's resource name. If not provided, a unique ID will be automatically assigned for the evaluation.  
`evaluation_dataset` |  `[EvaluationDataset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationDataset)` Required. The evaluation dataset to create.  
  
## CreateEvaluationExpectationRequest

Request message for `[EvaluationService.CreateEvaluationExpectation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationService.CreateEvaluationExpectation)`.

Fields  
---  
`parent` |  `string` Required. The app to create the evaluation expectation for. Format: `projects/{project}/locations/{location}/apps/{app}`  
`evaluation_expectation_id` |  `string` Optional. The ID to use for the evaluation expectation, which will become the final component of the evaluation expectation's resource name. If not provided, a unique ID will be automatically assigned for the evaluation expectation.  
`evaluation_expectation` |  `[EvaluationExpectation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationExpectation)` Required. The evaluation expectation to create.  
  
## CreateEvaluationRequest

Request message for `[EvaluationService.CreateEvaluation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationService.CreateEvaluation)`.

Fields  
---  
`parent` |  `string` Required. The app to create the evaluation for. Format: `projects/{project}/locations/{location}/apps/{app}`  
`evaluation_id` |  `string` Optional. The ID to use for the evaluation, which will become the final component of the evaluation's resource name. If not provided, a unique ID will be automatically assigned for the evaluation.  
`evaluation` |  `[Evaluation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Evaluation)` Required. The evaluation to create.  
  
## CreateExampleRequest

Request message for `[AgentService.CreateExample](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.CreateExample)`.

Fields  
---  
`parent` |  `string` Required. The resource name of the app to create an example in.  
`example_id` |  `string` Optional. The ID to use for the example, which will become the final component of the example's resource name. If not provided, a unique ID will be automatically assigned for the example.  
`example` |  `[Example](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Example)` Required. The example to create.  
  
## CreateGuardrailRequest

Request message for `[AgentService.CreateGuardrail](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.CreateGuardrail)`.

Fields  
---  
`parent` |  `string` Required. The resource name of the app to create a guardrail in.  
`guardrail_id` |  `string` Optional. The ID to use for the guardrail, which will become the final component of the guardrail's resource name. If not provided, a unique ID will be automatically assigned for the guardrail.  
`guardrail` |  `[Guardrail](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Guardrail)` Required. The guardrail to create.  
  
## CreateScheduledEvaluationRunRequest

Request message for `[EvaluationService.CreateScheduledEvaluationRun](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationService.CreateScheduledEvaluationRun)`.

Fields  
---  
`parent` |  `string` Required. The app to create the scheduled evaluation run for. Format: `projects/{project}/locations/{location}/apps/{app}`  
`scheduled_evaluation_run_id` |  `string` Optional. The ID to use for the scheduled evaluation run, which will become the final component of the scheduled evaluation run's resource name. If not provided, a unique ID will be automatically assigned.  
`scheduled_evaluation_run` |  `[ScheduledEvaluationRun](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ScheduledEvaluationRun)` Required. The scheduled evaluation run to create.  
  
## CreateToolRequest

Request message for `[AgentService.CreateTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.CreateTool)`.

Fields  
---  
`parent` |  `string` Required. The resource name of the app to create a tool in.  
`tool_id` |  `string` Optional. The ID to use for the tool, which will become the final component of the tool's resource name. If not provided, a unique ID will be automatically assigned for the tool.  
`tool` |  `[Tool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Tool)` Required. The tool to create.  
  
## CreateToolsetRequest

Request message for `[AgentService.CreateToolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.CreateToolset)`.

Fields  
---  
`parent` |  `string` Required. The resource name of the app to create a toolset in.  
`toolset_id` |  `string` Optional. The ID to use for the toolset, which will become the final component of the toolset's resource name. If not provided, a unique ID will be automatically assigned for the toolset.  
`toolset` |  `[Toolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Toolset)` Required. The toolset to create.  
  
## CustomVoiceSample

Configuration for a custom voice sample used for voice cloning.

Fields  
---  
`name` |  `string` Optional. The user-defined name for the custom voice sample.  
`voice_sample_gcs_uri` |  `string` Optional. The Cloud Storage URI to the audio sample for voice cloning. The audio sample should be a mono-channel, 24kHz WAV file.  
`consent_audio_gcs_uri` |  `string` Optional. Consent audio for voice cloning.  
`voice_instruction` |  `string` Optional. Natural language instructions for voice style, tone, pacing, or pronunciation.  
`preview_audio_content` |  `bytes` Output only. Synthesized preview audio for custom voice, formatted as canonical WAV (LINEAR16, 24kHz, 16-bit, mono).  
`preview_text` |  `string` Optional. Text for synthesizing preview audio for custom voice.  
`warnings[]` |  `[CustomVoiceSample.Warning](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.CustomVoiceSample.Warning)` Output only. Warning messages encountered during voice clone processing (e.g. low audio level).  
`voice_instruction_mode` |  `[CustomVoiceSample.VoiceInstructionMode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.CustomVoiceSample.VoiceInstructionMode)` Optional. Instruction mode for the voice sample. If unspecified, defaults to NO_INSTRUCTION.  
  
## VoiceInstructionMode

Instruction mode for the voice sample.

Enums  
---  
`VOICE_INSTRUCTION_MODE_UNSPECIFIED` | Unspecified instruction mode. Defaults to NO_INSTRUCTION.  
`NO_INSTRUCTION` | No voice instruction will be used.  
`GENERATE_INSTRUCTION` | Voice instruction will be automatically generated by AI from the audio sample.  
`CUSTOM_INSTRUCTION` | Custom voice instruction provided by the user.  
  
## Warning

A warning message encountered during voice sample processing.

Fields  
---  
`message` |  `string` Output only. A human-readable description of the warning.  
`type` |  `[CustomVoiceSample.Warning.WarningType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.CustomVoiceSample.Warning.WarningType)` Output only. The type of the warning.  
  
## WarningType

Type of warning encountered during voice sample processing.

Enums  
---  
`WARNING_TYPE_UNSPECIFIED` | Unspecified warning type.  
`LOW_AUDIO_LEVEL` | The audio level of the voice sample is too low (e.g. low RMS amplitude).  
  
## DashboardSettings

Settings for dashboards associated with the app, that show up in the Monitoring view.

Fields  
---  
`default_dashboard` |  `string` Optional. The resource name of the default Contact Center Insights dashboard associated with the app. This is the dashboard that will be displayed when users navigate to the Monitoring view for the app.Format: `projects/{project}/locations/{location}/dashboards/{dashboard}`  
  
## DataStore

A DataStore resource in Vertex AI Search.

Fields  
---  
`name` |  `string` Required. Full resource name of the DataStore. Format: `projects/{project}/locations/{location}/collections/{collection}/dataStores/{dataStore}`  
`type` |  `[DataStore.DataStoreType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DataStore.DataStoreType)` Output only. The type of the data store. This field is readonly and populated by the server.  
`document_processing_mode` |  `[DataStore.DocumentProcessingMode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DataStore.DocumentProcessingMode)` Output only. The document processing mode for the data store connection. Only set for PUBLIC_WEB and UNSTRUCTURED data stores.  
`display_name` |  `string` Output only. The display name of the data store.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Timestamp when the data store was created.  
`connector_config` |  `[DataStore.ConnectorConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DataStore.ConnectorConfig)` Output only. The connector config for the data store connection.  
  
## ConnectorConfig

The connector config for the data store connection.

Fields  
---  
`collection` |  `string` Resource name of the collection the data store belongs to.  
`collection_display_name` |  `string` Display name of the collection the data store belongs to.  
`data_source` |  `string` The name of the data source. Example: `salesforce`, `jira`, `confluence`, `bigquery`.  
  
## DataStoreType

The type of the data store.

Enums  
---  
`DATA_STORE_TYPE_UNSPECIFIED` | Not specified. This value indicates that the data store type is not specified, so it will not be used during search.  
`PUBLIC_WEB` | A data store that contains public web content.  
`UNSTRUCTURED` | A data store that contains unstructured private data.  
`FAQ` | A data store that contains structured data used as FAQ.  
`CONNECTOR` | A data store that is a connector to a first-party or a third-party service.  
  
## DocumentProcessingMode

The document processing mode of the data store.

Enums  
---  
`DOCUMENT_PROCESSING_MODE_UNSPECIFIED` | Not specified.  
`DOCUMENTS` | Documents are processed as documents.  
`CHUNKS` | Documents are converted to chunks.  
  
## DataStoreSettings

Data store related settings for the app.

Fields  
---  
`engines[]` |  `[DataStoreSettings.Engine](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DataStoreSettings.Engine)` Output only. The engines for the app.  
  
## Engine

An engine to which the data stores are connected. See Vertex AI Search: <https://cloud.google.com/generative-ai-app-builder/docs/enterprise-search-introduction>.

Fields  
---  
`name` |  `string` Output only. The resource name of the engine. Format: `projects/{project}/locations/{location}/collections/{collection}/engines/{engine}`  
`type` |  `[DataStoreSettings.Engine.Type](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DataStoreSettings.Engine.Type)` Output only. The type of the engine.  
  
## Type

The type of the engine. See the documentation available at <https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/SolutionType> and <https://cloud.google.com/generative-ai-app-builder/docs/create-datastore-ingest>.

Enums  
---  
`TYPE_UNSPECIFIED` | Unspecified engine type.  
`ENGINE_TYPE_SEARCH` | The SOLUTION_TYPE_SEARCH engine for the app. All connector data stores added to the app will be added to this engine.  
`ENGINE_TYPE_CHAT` | Chat engine type. The SOLUTION_TYPE_CHAT engine for the app. All connector data stores added to the app will be added to this engine.  
  
## DataStoreTool

Tool to retrieve from Vertex AI Search datastore or engine for grounding. Accepts either a datastore or an engine, but not both. See Vertex AI Search: <https://cloud.google.com/generative-ai-app-builder/docs/enterprise-search-introduction>.

Fields  
---  
`name` |  `string` Required. The data store tool name.  
`description` |  `string` Optional. The tool description.  
`boost_specs[]` |  `[DataStoreTool.BoostSpecs](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DataStoreTool.BoostSpecs)` Optional. Boost specification to boost certain documents.  
`modality_configs[]` |  `[DataStoreTool.ModalityConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DataStoreTool.ModalityConfig)` Optional. The modality configs for the data store.  
`filter_parameter_behavior` |  `[DataStoreTool.FilterParameterBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DataStoreTool.FilterParameterBehavior)` Optional. The filter parameter behavior.  
Union field `search_source`. Defines the search source, either a single DataStore or an Engine. `search_source` can be only one of the following:  
`data_store_source` |  `[DataStoreTool.DataStoreSource](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DataStoreTool.DataStoreSource)` Optional. Search within a single specific DataStore.  
`engine_source` |  `[DataStoreTool.EngineSource](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DataStoreTool.EngineSource)` Optional. Search within an Engine (potentially across multiple DataStores).  
  
## BoostSpec

Boost specification to boost certain documents.

Fields  
---  
`condition_boost_specs[]` |  `[DataStoreTool.BoostSpec.ConditionBoostSpec](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DataStoreTool.BoostSpec.ConditionBoostSpec)` Required. A list of boosting specifications.  
  
## ConditionBoostSpec

Boost specification for a condition.

Fields  
---  
`condition` |  `string` Required. An expression which specifies a boost condition. The syntax is the same as filter expression syntax. Currently, the only supported condition is a list of BCP-47 lang codes. Example: To boost suggestions in languages en or fr: (lang_code: ANY("en", "fr"))  
`boost` |  `float` Optional. Strength of the boost, which should be in [-1, 1]. Negative boost means demotion. Default is 0.0.Setting to 1.0 gives the suggestions a big promotion. However, it does not necessarily mean that the top result will be a boosted suggestion.Setting to -1.0 gives the suggestions a big demotion. However, other suggestions that are relevant might still be shown.Setting to 0.0 means no boost applied. The boosting condition is ignored.  
`boost_control_spec` |  `[DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec)` Optional. Complex specification for custom ranking based on customer defined attribute value.  
  
## BoostControlSpec

Specification for custom ranking based on customer specified attribute value. It provides more controls for customized ranking than the simple (condition, boost) combination above.

Fields  
---  
`field_name` |  `string` Optional. The name of the field whose value will be used to determine the boost amount.  
`attribute_type` |  `[DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec.AttributeType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec.AttributeType)` Optional. The attribute type to be used to determine the boost amount. The attribute value can be derived from the field value of the specified field_name. In the case of numerical it is straightforward i.e. attribute_value = numerical_field_value. In the case of freshness however, attribute_value = (time.now() - datetime_field_value).  
`interpolation_type` |  `[DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec.InterpolationType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec.InterpolationType)` Optional. The interpolation type to be applied to connect the control points listed below.  
`control_points[]` |  `[DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec.ControlPoint](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec.ControlPoint)` Optional. The control points used to define the curve. The monotonic function (defined through the interpolation_type above) passes through the control points listed here.  
  
## AttributeType

The attribute(or function) for which the custom ranking is to be applied.

Enums  
---  
`ATTRIBUTE_TYPE_UNSPECIFIED` | Unspecified AttributeType.  
`NUMERICAL` | The value of the numerical field will be used to dynamically update the boost amount. In this case, the attribute_value (the x value) of the control point will be the actual value of the numerical field for which the boost_amount is specified.  
`FRESHNESS` | For the freshness use case the attribute value will be the duration between the current time and the date in the datetime field specified. The value must be formatted as an XSD `dayTimeDuration` value (a restricted subset of an ISO 8601 duration value). The pattern for this is: `[nD][T[nH][nM][nS]]`. E.g. `5D`, `3DT12H30M`, `T24H`.  
  
## ControlPoint

The control points used to define the curve. The curve defined through these control points can only be monotonically increasing or decreasing(constant values are acceptable).

Fields  
---  
`attribute_value` |  `string` Optional. Can be one of: 1. The numerical field value. 2. The duration spec for freshness: The value must be formatted as an XSD `dayTimeDuration` value (a restricted subset of an ISO 8601 duration value). The pattern for this is: `[nD][T[nH][nM][nS]]`.  
`boost_amount` |  `float` Optional. The value between -1 to 1 by which to boost the score if the attribute_value evaluates to the value specified above.  
  
## InterpolationType

The interpolation type to be applied. Default will be linear (Piecewise Linear).

Enums  
---  
`INTERPOLATION_TYPE_UNSPECIFIED` | Interpolation type is unspecified. In this case, it defaults to Linear.  
`LINEAR` | Piecewise linear interpolation will be applied.  
  
## BoostSpecs

Boost specifications to boost certain documents. For more information, please refer to <https://cloud.google.com/generative-ai-app-builder/docs/boosting>.

Fields  
---  
`data_stores[]` |  `string` Required. The Data Store where the boosting configuration is applied. Full resource name of DataStore, such as projects/{project}/locations/{location}/collections/{collection}/dataStores/{dataStore}.  
`spec[]` |  `[DataStoreTool.BoostSpec](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DataStoreTool.BoostSpec)` Required. A list of boosting specifications.  
  
## DataStoreSource

Configuration for searching within a specific DataStore.

Fields  
---  
`filter` |  `string` Optional. Filter specification for the DataStore. See: <https://cloud.google.com/generative-ai-app-builder/docs/filter-search-metadata>  
`data_store` |  `[DataStore](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DataStore)` Optional. The data store.  
  
## EngineSource

Configuration for searching within an Engine, potentially targeting specific DataStores.

Fields  
---  
`engine` |  `string` Required. Full resource name of the Engine. Format: `projects/{project}/locations/{location}/collections/{collection}/engines/{engine}`  
`data_store_sources[]` |  `[DataStoreTool.DataStoreSource](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DataStoreTool.DataStoreSource)` Optional. Use to target specific DataStores within the Engine. If empty, the search applies to all DataStores associated with the Engine.  
`filter` |  `string` Optional. A filter applied to the search across the Engine. Not relevant and not used if 'data_store_sources' is provided. See: <https://cloud.google.com/generative-ai-app-builder/docs/filter-search-metadata>  
  
## FilterParameterBehavior

Filter parameter behavior.

Enums  
---  
`FILTER_PARAMETER_BEHAVIOR_UNSPECIFIED` | Default filter behavior. Include filter parameter for connector datastores. For the rest of the datastore types, the filter input parameter is omitted.  
`ALWAYS_INCLUDE` | Always include filter parameter for all datastore types.  
`NEVER_INCLUDE` | The filter parameter is never included in the list of tool parameters, regardless of the datastore type.  
  
## GroundingConfig

Grounding configuration.

Fields  
---  
`grounding_level` |  `float` Optional. The groundedness threshold of the answer based on the retrieved sources. The value has a configurable range of [1, 5]. The level is used to threshold the groundedness of the answer, meaning that all responses with a groundedness score below the threshold will fall back to returning relevant snippets only.For example, a level of 3 means that the groundedness score must be 3 or higher for the response to be returned.  
`disabled` |  `bool` Optional. Whether grounding is disabled.  
  
## ModalityConfig

If specified, will apply the given configuration for the specified modality.

Fields  
---  
`modality_type` |  `[DataStoreTool.ModalityConfig.ModalityType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DataStoreTool.ModalityConfig.ModalityType)` Required. The modality type.  
`rewriter_config` |  `[DataStoreTool.RewriterConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DataStoreTool.RewriterConfig)` Optional. The rewriter config.  
`summarization_config` |  `[DataStoreTool.SummarizationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DataStoreTool.SummarizationConfig)` Optional. The summarization config.  
`grounding_config` |  `[DataStoreTool.GroundingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DataStoreTool.GroundingConfig)` Optional. The grounding configuration.  
`snippets_config` |  `[DataStoreTool.SnippetsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DataStoreTool.SnippetsConfig)` Optional. The snippets configuration.  
  
## ModalityType

The modality type.

Enums  
---  
`MODALITY_TYPE_UNSPECIFIED` | Unspecified modality type.  
`TEXT` | Text modality.  
`AUDIO` | Audio modality.  
  
## RewriterConfig

Rewriter configuration.

Fields  
---  
`model_settings` |  `[ModelSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ModelSettings)` Required. Configurations for the LLM model.  
`prompt` |  `string` Optional. The prompt definition. If not set, default prompt will be used.  
`disabled` |  `bool` Optional. Whether the rewriter is disabled.  
  
## SnippetsConfig

Snippets configuration.

Fields  
---  
`enable_snippets` |  `bool` Optional. Whether snippets are enabled.  
`max_snippets` |  `int32` Optional. Number of snippets to return per query. If unset, returns all snippets from the service by default.  
  
## SummarizationConfig

Summarization configuration.

Fields  
---  
`model_settings` |  `[ModelSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ModelSettings)` Optional. Configurations for the LLM model.  
`prompt` |  `string` Optional. The prompt definition. If not set, default prompt will be used.  
`disabled` |  `bool` Optional. Whether summarization is disabled.  
  
## DeleteAgentRequest

Request message for `[AgentService.DeleteAgent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.DeleteAgent)`.

Fields  
---  
`name` |  `string` Required. The resource name of the agent to delete.  
`force` |  `bool` Optional. Indicates whether to forcefully delete the agent, even if it is still referenced by other app/agents/examples.

  * If `force = false`, the deletion fails if other agents/examples reference it.
  * If `force = true`, delete the agent and remove it from all referencing apps/agents/examples.

  
`etag` |  `string` Optional. The current etag of the agent. If an etag is not provided, the deletion will overwrite any concurrent changes. If an etag is provided and does not match the current etag of the agent, deletion will be blocked and an ABORTED error will be returned.  
  
## DeleteAppRequest

Request message for `[AgentService.DeleteApp](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.DeleteApp)`.

Fields  
---  
`name` |  `string` Required. The resource name of the app to delete.  
`etag` |  `string` Optional. The current etag of the app. If an etag is not provided, the deletion will overwrite any concurrent changes. If an etag is provided and does not match the current etag of the app, deletion will be blocked and an ABORTED error will be returned.  
  
## DeleteAppVersionRequest

Request message for `[AgentService.DeleteAppVersion](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.DeleteAppVersion)`.

Fields  
---  
`name` |  `string` Required. The resource name of the app version to delete.  
`etag` |  `string` Optional. The current etag of the app version. If an etag is not provided, the deletion will overwrite any concurrent changes. If an etag is provided and does not match the current etag of the app version, deletion will be blocked and an ABORTED error will be returned.  
  
## DeleteConversationRequest

Request message for `[AgentService.DeleteConversation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.DeleteConversation)`.

Fields  
---  
`name` |  `string` Required. The resource name of the conversation to delete.  
`source  
**(deprecated)**` |  `[Conversation.Source](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Conversation.Source)` This item is deprecated!Optional. Indicate the source of the conversation. If not set, Source.Live will be applied by default.  
  
## DeleteDeploymentRequest

Request message for `[AgentService.DeleteDeployment](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.DeleteDeployment)`.

Fields  
---  
`name` |  `string` Required. The name of the deployment to delete. Format: `projects/{project}/locations/{location}/apps/{app}/deployments/{deployment}`  
`etag` |  `string` Optional. The etag of the deployment. If an etag is provided and does not match the current etag of the deployment, deletion will be blocked and an ABORTED error will be returned.  
  
## DeleteEvaluationDatasetRequest

Request message for `[EvaluationService.DeleteEvaluationDataset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationService.DeleteEvaluationDataset)`.

Fields  
---  
`name` |  `string` Required. The resource name of the evaluation dataset to delete.  
`etag` |  `string` Optional. The current etag of the evaluation dataset. If an etag is not provided, the deletion will overwrite any concurrent changes. If an etag is provided and does not match the current etag of the evaluation dataset, deletion will be blocked and an ABORTED error will be returned.  
  
## DeleteEvaluationExpectationRequest

Request message for `[EvaluationService.DeleteEvaluationExpectation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationService.DeleteEvaluationExpectation)`.

Fields  
---  
`name` |  `string` Required. The resource name of the evaluation expectation to delete.  
`etag` |  `string` Optional. The current etag of the evaluation expectation. If an etag is not provided, the deletion will overwrite any concurrent changes. If an etag is provided and does not match the current etag of the evaluation expectation, deletion will be blocked and an ABORTED error will be returned.  
  
## DeleteEvaluationRequest

Request message for `[EvaluationService.DeleteEvaluation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationService.DeleteEvaluation)`.

Fields  
---  
`name` |  `string` Required. The resource name of the evaluation to delete.  
`force` |  `bool` Optional. Indicates whether to forcefully delete the evaluation, even if it is still referenced by evaluation datasets.

  * If `force = false`, the deletion will fail if any datasets still reference the evaluation.
  * If `force = true`, all existing references from datasets will be removed and the evaluation will be deleted.

  
`etag` |  `string` Optional. The current etag of the evaluation. If an etag is not provided, the deletion will overwrite any concurrent changes. If an etag is provided and does not match the current etag of the evaluation, deletion will be blocked and an ABORTED error will be returned.  
  
## DeleteEvaluationResultRequest

Request message for `[EvaluationService.DeleteEvaluationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationService.DeleteEvaluationResult)`.

Fields  
---  
`name` |  `string` Required. The resource name of the evaluation result to delete.  
  
## DeleteEvaluationRunOperationMetadata

This type has no fields.

Operation metadata for `[EvaluationService.DeleteEvaluationRun](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationService.DeleteEvaluationRun)`.

## DeleteEvaluationRunRequest

Request message for `[EvaluationService.DeleteEvaluationRun](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationService.DeleteEvaluationRun)`.

Fields  
---  
`name` |  `string` Required. The resource name of the evaluation run to delete.  
  
## DeleteExampleRequest

Request message for `[AgentService.DeleteExample](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.DeleteExample)`.

Fields  
---  
`name` |  `string` Required. The resource name of the example to delete.  
`etag` |  `string` Optional. The current etag of the example. If an etag is not provided, the deletion will overwrite any concurrent changes. If an etag is provided and does not match the current etag of the example, deletion will be blocked and an ABORTED error will be returned.  
  
## DeleteGuardrailRequest

Request message for `[AgentService.DeleteGuardrail](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.DeleteGuardrail)`.

Fields  
---  
`name` |  `string` Required. The resource name of the guardrail to delete.  
`force` |  `bool` Optional. Indicates whether to forcefully delete the guardrail, even if it is still referenced by app/agents.

  * If `force = false`, the deletion fails if any apps/agents still reference the guardrail.
  * If `force = true`, all existing references from apps/agents will be removed and the guardrail will be deleted.

  
`etag` |  `string` Optional. The current etag of the guardrail. If an etag is not provided, the deletion will overwrite any concurrent changes. If an etag is provided and does not match the current etag of the guardrail, deletion will be blocked and an ABORTED error will be returned.  
  
## DeleteScheduledEvaluationRunRequest

Request message for `[EvaluationService.DeleteScheduledEvaluationRun](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationService.DeleteScheduledEvaluationRun)`.

Fields  
---  
`name` |  `string` Required. The resource name of the scheduled evaluation run to delete.  
`etag` |  `string` Optional. The etag of the ScheduledEvaluationRun. If provided, it must match the server's etag.  
  
## DeleteToolRequest

Request message for `[AgentService.DeleteTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.DeleteTool)`.

Fields  
---  
`name` |  `string` Required. The resource name of the tool to delete.  
`force` |  `bool` Optional. Indicates whether to forcefully delete the tool, even if it is still referenced by agents/examples.

  * If `force = false`, the deletion will fail if any agents still reference the tool.
  * If `force = true`, all existing references from agents will be removed and the tool will be deleted.

  
`etag` |  `string` Optional. The current etag of the tool. If an etag is not provided, the deletion will overwrite any concurrent changes. If an etag is provided and does not match the current etag of the tool, deletion will be blocked and an ABORTED error will be returned.  
  
## DeleteToolsetRequest

Request message for `[AgentService.DeleteToolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.DeleteToolset)`.

Fields  
---  
`name` |  `string` Required. The resource name of the toolset to delete.  
`force` |  `bool` Optional. Indicates whether to forcefully delete the toolset, even if it is still referenced by app/agents.

  * If `force = false`, the deletion fails if any agents still reference the toolset.
  * If `force = true`, all existing references from agents will be removed and the toolset will be deleted.

  
`etag` |  `string` Optional. The current etag of the toolset. If an etag is not provided, the deletion will overwrite any concurrent changes. If an etag is provided and does not match the current etag of the toolset, deletion will be blocked and an ABORTED error will be returned.  
  
## DeployChannelResponse

Response message for `AgentService.DeployChannel`.

Fields  
---  
`deployment` |  `[Deployment](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Deployment)` The created deployment.  
  
## Deployment

A deployment represents an immutable, queryable version of the app. It is used to deploy an app version with a specific channel profile.

Fields  
---  
`name` |  `string` Identifier. The resource name of the deployment. Format: `projects/{project}/locations/{location}/apps/{app}/deployments/{deployment}`  
`display_name` |  `string` Required. Display name of the deployment.  
`app_version` |  `string` Optional. The resource name of the app version to deploy. Format: `projects/{project}/locations/{location}/apps/{app}/versions/{version}` Use `projects/{project}/locations/{location}/apps/{app}/versions/-` to use the draft app.  
`channel_profile` |  `[ChannelProfile](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ChannelProfile)` Required. The channel profile used in the deployment.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Timestamp when this deployment was created.  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Timestamp when this deployment was last updated.  
`etag` |  `string` Output only. Etag used to ensure the object hasn't changed during a read-modify-write operation. If the etag is empty, the update will overwrite any concurrent changes.  
`experiment_config` |  `[ExperimentConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ExperimentConfig)` Optional. Experiment configuration for the deployment.  
`whatsapp_credentials` |  `[WhatsAppCredentials](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.WhatsAppCredentials)` Optional. Input only. Ephemeral WhatsApp credentials required when configuring a WhatsApp channel profile.  
`instagram_credentials` |  `[InstagramCredentials](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.InstagramCredentials)` Optional. Input only. Ephemeral Instagram credentials required when configuring a Instagram channel profile.  
`model_settings` |  `[ModelSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ModelSettings)` Optional. Model settings for the deployment. Overrides model settings configured at the app/agent levels. Note: Deployment-level model settings override is gated behind an allowlist. Contact the CXAS team to enable this field.  
`modality` |  `[Deployment.Modality](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Deployment.Modality)` Optional. The modality of the deployment. Note: Deployment-level modality override is gated behind an allowlist. Contact the CXAS team to enable this field.  
`agent_registry_deployment` |  `[AgentRegistryDeployment](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentRegistryDeployment)` Optional. Configuration for deploying this deployment to Agent Registry. If present, this deployment will be published to Agent Registry.  
  
## Modality

The modality of the deployment.

Enums  
---  
`MODALITY_UNSPECIFIED` | Unknown modality.  
`MODALITY_TEXT` | Text modality.  
`MODALITY_VOICE` | Voice modality.  
`MODALITY_VIDEO` | Video modality.  
  
## EndSession

Indicates the session has terminated, due to either successful completion (e.g. user says "Good bye!" ) or an agent escalation.

The agent will not process any further inputs after session is terminated and the client should half-close and disconnect after receiving all remaining responses from the agent.

Fields  
---  
`metadata` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` Optional. Provides additional information about the end session signal, such as the reason for ending the session.  
  
## EndUserAuthConfig

End-user authentication configuration used for Connection calls. The field values must be the names of context variables in the format `$context.variables.<name_of_variable>`.

Fields  
---  
Union field `auth_config`. The auth configuration. `auth_config` can be only one of the following:  
`oauth2_auth_code_config` |  `[EndUserAuthConfig.Oauth2AuthCodeConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EndUserAuthConfig.Oauth2AuthCodeConfig)` Oauth 2.0 Authorization Code authentication.  
`oauth2_jwt_bearer_config` |  `[EndUserAuthConfig.Oauth2JwtBearerConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EndUserAuthConfig.Oauth2JwtBearerConfig)` JWT Profile Oauth 2.0 Authorization Grant authentication.  
  
## Oauth2AuthCodeConfig

Oauth 2.0 Authorization Code authentication configuration.

Fields  
---  
`oauth_token` |  `string` Required. Oauth token parameter name to pass through. Must be in the format `$context.variables.<name_of_variable>`.  
  
## Oauth2JwtBearerConfig

JWT Profile Oauth 2.0 Authorization Grant authentication configuration.

Fields  
---  
`issuer` |  `string` Required. Issuer parameter name to pass through. Must be in the format `$context.variables.<name_of_variable>`.  
`subject` |  `string` Required. Subject parameter name to pass through. Must be in the format `$context.variables.<name_of_variable>`.  
`client_key` |  `string` Required. Client parameter name to pass through. Must be in the format `$context.variables.<name_of_variable>`.  
  
## EndpointControlPolicy

Defines project/location level endpoint control policy.

Fields  
---  
`enforcement_scope` |  `[EndpointControlPolicy.EnforcementScope](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EndpointControlPolicy.EnforcementScope)` Optional. The scope in which this policy's allowed_origins list is enforced.  
`allowed_origins[]` |  `string` Optional. The allowed HTTP(s) origins that tools in the App are able to directly call. The enforcement depends on the value of enforcement_scope and the VPC-SC status of the project. If a port number is not provided, all ports will be allowed. Otherwise, the port number must match exactly. For example, "https://example.com" will match "https://example.com:443" and any other port. "https://example.com:443" will only match "https://example.com:443".  
  
## EnforcementScope

Defines the scope in which this policy's allowed_origins list is enforced.

Enums  
---  
`ENFORCEMENT_SCOPE_UNSPECIFIED` | Unspecified. This policy will be treated as VPCSC_ONLY.  
`VPCSC_ONLY` | This policy applies only when VPC-SC is active.  
`ALWAYS` | This policy ALWAYS applies, regardless of VPC-SC status.  
  
## ErrorHandlingSettings

Settings to describe how errors should be handled in the app.

Fields  
---  
`error_handling_strategy` |  `[ErrorHandlingSettings.ErrorHandlingStrategy](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ErrorHandlingSettings.ErrorHandlingStrategy)` Optional. The strategy to use for error handling.  
`fallback_response_config` |  `[ErrorHandlingSettings.FallbackResponseConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ErrorHandlingSettings.FallbackResponseConfig)` Optional. Configuration for handling fallback responses.  
`end_session_config` |  `[ErrorHandlingSettings.EndSessionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ErrorHandlingSettings.EndSessionConfig)` Optional. Configuration for ending the session in case of system errors (e.g. LLM errors).  
  
## EndSessionConfig

Configuration for ending the session in case of system errors (e.g. LLM errors).

Fields  
---  
`escalate_session` |  `bool` Optional. Whether to escalate the session in `[EndSession](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EndSession)`. If session is escalated, `[metadata in EndSession](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EndSession.FIELDS.google.protobuf.Struct.google.cloud.ces.v1beta.EndSession.metadata)` will contain `session_escalated = true`. See <https://docs.cloud.google.com/customer-engagement-ai/conversational-agents/ps/deploy/google-telephony-platform#transfer_a_call_to_a_human_agent> for details.  
  
## ErrorHandlingStrategy

Defines the strategy for handling errors.

Enums  
---  
`ERROR_HANDLING_STRATEGY_UNSPECIFIED` | Unspecified error handling strategy.  
`NONE` | No specific handling is enabled.  
`FALLBACK_RESPONSE` | A fallback message will be returned to the user in case of system errors (e.g. LLM errors).  
`END_SESSION` | An `[EndSession](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EndSession)` signal will be emitted in case of system errors (e.g. LLM errors).  
  
## FallbackResponseConfig

Configuration for handling fallback responses.

Fields  
---  
`custom_fallback_messages` |  `map<string, string>` Optional. The fallback messages in case of system errors (e.g. LLM errors), mapped by [supported language code](https://docs.cloud.google.com/customer-engagement-ai/conversational-agents/ps/reference/language).  
`max_fallback_attempts` |  `int32` Optional. The maximum number of fallback attempts to make before the agent emitting `[EndSession](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EndSession)` Signal.  
  
## Evaluation

An evaluation represents all of the information needed to simulate and evaluate an agent.

Fields  
---  
`name` |  `string` Identifier. The unique identifier of this evaluation. Format: `projects/{project}/locations/{location}/apps/{app}/evaluations/{evaluation}`  
`display_name` |  `string` Required. User-defined display name of the evaluation. Unique within an App.  
`description` |  `string` Optional. User-defined description of the evaluation.  
`tags[]` |  `string` Optional. User defined tags to categorize the evaluation.  
`evaluation_datasets[]` |  `string` Output only. List of evaluation datasets the evaluation belongs to. Format: `projects/{project}/locations/{location}/apps/{app}/evaluationDatasets/{evaluationDataset}`  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Timestamp when the evaluation was created.  
`created_by` |  `string` Output only. The user who created the evaluation.  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Timestamp when the evaluation was last updated.  
`last_updated_by` |  `string` Output only. The user who last updated the evaluation.  
`evaluation_runs[]` |  `string` Output only. The EvaluationRuns that this Evaluation is associated with.  
`etag` |  `string` Output only. Etag used to ensure the object hasn't changed during a read-modify-write operation. If the etag is empty, the update will overwrite any concurrent changes.  
`aggregated_metrics` |  `[AggregatedMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AggregatedMetrics)` Output only. The aggregated metrics for this evaluation across all runs.  
`last_completed_result` |  `[EvaluationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationResult)` Output only. The latest evaluation result for this evaluation.  
`invalid` |  `bool` Output only. Whether the evaluation is invalid. This can happen if an evaluation is referencing a tool, toolset, or agent that has since been deleted.  
`last_ten_results[]` |  `[EvaluationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationResult)` Output only. The last 10 evaluation results for this evaluation. This is only populated if include_last_ten_results is set to true in the ListEvaluationsRequest or GetEvaluationRequest.  
`evaluation_metrics_threshold_override` |  `[EvaluationMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationMetricsThresholds)` Optional. Overrides metrics thresholds for this specific evaluation.  
`evaluation_metrics_config_override` |  `[EvaluationMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationMetricsConfig)` Optional. Overrides metrics config for this specific evaluation.  
Union field `inputs`. The inputs for the evaluation `inputs` can be only one of the following:  
`golden` |  `[Evaluation.Golden](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Evaluation.Golden)` Optional. The golden steps to be evaluated.  
`scenario` |  `[Evaluation.Scenario](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Evaluation.Scenario)` Optional. The config for a scenario.  
  
## Golden

The steps required to replay a golden conversation.

Fields  
---  
`turns[]` |  `[Evaluation.GoldenTurn](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Evaluation.GoldenTurn)` Required. The golden turns required to replay a golden conversation. The maximum number of allowed turns is 100.  
`evaluation_expectations[]` |  `string` Optional. The evaluation expectations to evaluate the replayed conversation against. Format: `projects/{project}/locations/{location}/apps/{app}/evaluationExpectations/{evaluationExpectation}`  
  
## GoldenExpectation

Represents a single, checkable requirement.

Fields  
---  
`note` |  `string` Optional. A note for this requirement, useful in reporting when specific checks fail. E.g., "Check_Payment_Tool_Called".  
`skip_evaluation` |  `bool` Optional. If set to true, this specific expectation will not be evaluated.  
`expectation_level_metrics_thresholds_override` |  `[EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.ExpectationLevelMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.ExpectationLevelMetricsThresholds)` Optional. Overrides metrics at the step level.  
`agent_response_semantic_similarity_metrics_config_override` |  `[EvaluationMetricsConfig.SemanticSimilarityMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationMetricsConfig.SemanticSimilarityMetricsConfig)` Optional. Overrides for agent_response semantic similarity metrics.  
`agent_response_hallucination_metrics_config_override` |  `[EvaluationMetricsConfig.HallucinationMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationMetricsConfig.HallucinationMetricsConfig)` Optional. Overrides for agent_response hallucination metrics.  
`comparison_type` |  `[EvaluationMetricsConfig.ComparisonType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationMetricsConfig.ComparisonType)` Optional. The comparison type to use for the expectation check.  
Union field `condition`. The actual check to perform. `condition` can be only one of the following:  
`tool_call` |  `[ToolCall](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ToolCall)` Optional. Check that a specific tool was called with the parameters.  
`tool_response` |  `[ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ToolResponse)` Optional. Check that a specific tool had the expected response.  
`agent_response` |  `[Message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Message)` Optional. Check that the agent responded with the correct response. The role "agent" is implied.  
`agent_transfer` |  `[AgentTransfer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentTransfer)` Optional. Check that the agent transferred the conversation to a different agent.  
`updated_variables` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` Optional. Check that the agent updated the session variables to the expected values. Used to also capture agent variable updates for golden evals.  
`mock_tool_response` |  `[ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ToolResponse)` Optional. The tool response to mock, with the parameters of interest specified. Any parameters not specified will be hallucinated by the LLM.  
`no_tool_calls` |  `bool` Optional. Check that no tools were called during this turn.  
  
## GoldenTurn

A golden turn defines a single turn in a golden conversation.

Fields  
---  
`steps[]` |  `[Evaluation.Step](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Evaluation.Step)` Required. The steps required to replay a golden conversation.  
`root_span` |  `[Span](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Span)` Optional. The root span of the golden turn for processing and maintaining audio information. The uri for the audio must contain audio saved in 16Khz sample rate.  
`turn_level_metrics_thresholds_override` |  `[EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.TurnLevelMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.TurnLevelMetricsThresholds)` Optional. Overrides for turn-level metric thresholds.  
`hallucination_metric_behavior_override` |  `[EvaluationMetricsThresholds.HallucinationMetricBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationMetricsThresholds.HallucinationMetricBehavior)` Optional. Override for turn-level hallucination metric behavior.  
  
## Scenario

The config for a scenario

Fields  
---  
`task` |  `string` Required. The task to be targeted by the scenario.  
`user_facts[]` |  `[Evaluation.Scenario.UserFact](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Evaluation.Scenario.UserFact)` Optional. The user facts to be used by the scenario.  
`max_turns` |  `int32` Optional. The maximum number of turns to simulate. The maximum allowed value is 100. The default value is 100.  
`rubrics[]` |  `string` Required. The rubrics to score the scenario against.  
`scenario_expectations[]` |  `[Evaluation.ScenarioExpectation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Evaluation.ScenarioExpectation)` Required. The ScenarioExpectations to evaluate the conversation produced by the user simulation.  
`variable_overrides` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` Optional. Variables / Session Parameters as context for the session, keyed by variable names. Members of this struct will override any default values set by the system.Note, these are different from user facts, which are facts known to the user. Variables are parameters known to the agent: i.e. MDN (phone number) passed by the telephony system.  
`task_completion_behavior  
**(deprecated)**` |  `[Evaluation.Scenario.TaskCompletionBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Evaluation.Scenario.TaskCompletionBehavior)` This item is deprecated!Optional. Deprecated. Use user_goal_behavior instead.  
`user_goal_behavior` |  `[Evaluation.Scenario.UserGoalBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Evaluation.Scenario.UserGoalBehavior)` Optional. The expected behavior of the user goal.  
`evaluation_expectations[]` |  `string` Optional. The evaluation expectations to evaluate the conversation produced by the simulation against. Format: `projects/{project}/locations/{location}/apps/{app}/evaluationExpectations/{evaluationExpectation}`  
`scenario_execution_mode` |  `[EvaluationSettings.ScenarioExecutionMode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationSettings.ScenarioExecutionMode)` Optional. The execution mode for scenario evaluations.  
  
## TaskCompletionBehavior

The expected behavior of the user task. This is used to determine whether the scenario is successful.

Enums  
---  
`TASK_COMPLETION_BEHAVIOR_UNSPECIFIED` | Behavior unspecified. Will default to TASK_SATISFIED.  
`TASK_SATISFIED` | The user task should be completed successfully.  
`TASK_REJECTED` | The user task should be rejected.  
  
## UserFact

Facts about the user as a key value pair.

Fields  
---  
`name` |  `string` Required. The name of the user fact.  
`value` |  `string` Required. The value of the user fact.  
  
## UserGoalBehavior

The expected behavior of the user goal. This is used to determine whether the scenario is successful.

Enums  
---  
`USER_GOAL_BEHAVIOR_UNSPECIFIED` | Behavior unspecified. Will default to USER_GOAL_SATISFIED.  
`USER_GOAL_SATISFIED` | The user goal should be completed successfully.  
`USER_GOAL_REJECTED` | The user goal should be rejected.  
`USER_GOAL_IGNORED` | Ignore the user goal status.  
  
## ScenarioExpectation

The expectation to evaluate the conversation produced by the simulation.

Fields  
---  
Union field `expectation`. The expectation to evaluate the conversation produced by the simulation. `expectation` can be only one of the following:  
`tool_expectation` |  `[Evaluation.ScenarioExpectation.ToolExpectation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Evaluation.ScenarioExpectation.ToolExpectation)` Optional. The tool call and response pair to be evaluated.  
`agent_response` |  `[Message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Message)` Optional. The agent response to be evaluated.  
  
## ToolExpectation

The tool call and response pair to be evaluated.

Fields  
---  
`expected_tool_call` |  `[ToolCall](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ToolCall)` Required. The expected tool call, with the parameters of interest specified. Any parameters not specified will be hallucinated by the LLM.  
`mock_tool_response` |  `[ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ToolResponse)` Required. The tool response to mock, with the parameters of interest specified. Any parameters not specified will be hallucinated by the LLM.  
  
## Step

A step defines a singular action to happen during the evaluation.

Fields  
---  
Union field `step`. The step to perform. `step` can be only one of the following:  
`user_input` |  `[SessionInput](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.SessionInput)` Optional. User input for the conversation.  
`agent_transfer` |  `[AgentTransfer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentTransfer)` Optional. Transfer the conversation to a different agent.  
`expectation` |  `[Evaluation.GoldenExpectation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Evaluation.GoldenExpectation)` Optional. Executes an expectation on the current turn.  
  
## EvaluationConfig

EvaluationConfig configures settings for running the evaluation.

Fields  
---  
`input_audio_config` |  `[InputAudioConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.InputAudioConfig)` Optional. Configuration for processing the input audio.  
`output_audio_config` |  `[OutputAudioConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.OutputAudioConfig)` Optional. Configuration for generating the output audio.  
`evaluation_channel` |  `[EvaluationConfig.EvaluationChannel](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationConfig.EvaluationChannel)` Optional. The channel to evaluate.  
`tool_call_behaviour` |  `[EvaluationToolCallBehaviour](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationToolCallBehaviour)` Optional. Specifies whether the evaluation should use real tool calls or fake tools.  
  
## EvaluationChannel

The channel to evaluate.

Enums  
---  
`EVALUATION_CHANNEL_UNSPECIFIED` | Unspecified evaluation channel.  
`TEXT` | Text-only evaluation channel.  
`AUDIO` | Audio evaluation channel.  
  
## EvaluationDataset

An evaluation dataset represents a set of evaluations that are grouped together basaed on shared tags.

Fields  
---  
`name` |  `string` Identifier. The unique identifier of this evaluation dataset. Format: `projects/{project}/locations/{location}/apps/{app}/evaluationDatasets/{evaluationDataset}`  
`display_name` |  `string` Required. User-defined display name of the evaluation dataset. Unique within an App.  
`evaluations[]` |  `string` Optional. Evaluations that are included in this dataset.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Timestamp when the evaluation dataset was created.  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Timestamp when the evaluation dataset was last updated.  
`etag` |  `string` Output only. Etag used to ensure the object hasn't changed during a read-modify-write operation. If the etag is empty, the update will overwrite any concurrent changes.  
`created_by` |  `string` Output only. The user who created the evaluation dataset.  
`last_updated_by` |  `string` Output only. The user who last updated the evaluation dataset.  
`aggregated_metrics` |  `[AggregatedMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AggregatedMetrics)` Output only. The aggregated metrics for this evaluation dataset across all runs.  
  
## EvaluationErrorInfo

Information about an error encountered during an evaluation execution.

Fields  
---  
`error_type` |  `[EvaluationErrorInfo.ErrorType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationErrorInfo.ErrorType)` Output only. The type of error.  
`error_message` |  `string` Output only. The error message.  
`session_id` |  `string` Output only. The session ID for the conversation that caused the error.  
`user_facing_error_message` |  `string` Output only. The user facing error message.  
  
## ErrorType

The type of error

Enums  
---  
`ERROR_TYPE_UNSPECIFIED` | Unspecified error type.  
`RUNTIME_FAILURE` | Failure during runtime execution.  
`CONVERSATION_RETRIEVAL_FAILURE` | Failure to retrieve conversation from CES Runtime.  
`METRIC_CALCULATION_FAILURE` | Failure to calculate a metric / outcome.  
`EVALUATION_UPDATE_FAILURE` | Failure to update the evaluation.  
`QUOTA_EXHAUSTED` | Ran out of quota.  
`USER_SIMULATION_FAILURE` | Failure during user simulation.  
  
## EvaluationExpectation

An evaluation expectation represents a specific criteria to evaluate against.

Fields  
---  
`name` |  `string` Identifier. The unique identifier of this evaluation expectation. Format: `projects/{project}/locations/{location}/apps/{app}/evaluationExpectations/{evaluation_expectation}`  
`display_name` |  `string` Required. User-defined display name. Must be unique within the app.  
`tags[]` |  `string` Optional. User-defined tags for expectations. Can be used to filter expectations.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Timestamp when the evaluation expectation was created.  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Timestamp when the evaluation expectation was last updated.  
`etag` |  `string` Output only. Etag used to ensure the object hasn't changed during a read-modify-write operation. If the etag is empty, the update will overwrite any concurrent changes.  
Union field `criteria`. The definition of the criteria used for evaluation. `criteria` can be only one of the following:  
`llm_criteria` |  `[EvaluationExpectation.LlmCriteria](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationExpectation.LlmCriteria)` Optional. Evaluation criteria based on an LLM prompt.  
  
## LlmCriteria

Configuration for LLM-based evaluation criteria.

Fields  
---  
`prompt` |  `string` Required. The prompt/instructions provided to the LLM judge.  
  
## EvaluationMetricsConfig

Configures the metrics for an evaluation.

Fields  
---  
`golden_metrics_config` |  `[EvaluationMetricsConfig.GoldenMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationMetricsConfig.GoldenMetricsConfig)` Optional. Configuration for the golden metrics for the evaluation.  
`scenario_metrics_config` |  `[EvaluationMetricsConfig.ScenarioMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationMetricsConfig.ScenarioMetricsConfig)` Optional. Configuration for the scenario metrics for the evaluation.  
  
## ComparisonType

Supported comparison types for checking the agent's response.

Enums  
---  
`COMPARISON_TYPE_UNSPECIFIED` | Unspecified comparison type. Behavior defaults to SEMANTIC_SIMILARITY for agent responses and tool calls.  
`EQUALS` | Exact string match.  
`CONTAINS` | Substring match (checks if the expected string is contained in the actual response).  
`SEMANTIC_SIMILARITY` | Semantic similarity match (evaluates meaning similarity using an LLM).  
  
## ExpectationsMetMetricsConfig

Configuration for the expectation level metrics for the evaluation. To disable the metric, set the message but do not set the `enable_expectations_met_metrics` field to true (or explicitly set it to false). To unset the configuration and fallback to the default behavior, omit the message entirely.

Fields  
---  
`enable_expectations_met_metrics` |  `bool` Optional. Whether to calculate the expectation level metrics for the evaluation.  
  
## GoldenMetricsConfig

Configuration for the golden metrics for the evaluation.

Fields  
---  
`semantic_similarity_metrics_config` |  `[EvaluationMetricsConfig.SemanticSimilarityMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationMetricsConfig.SemanticSimilarityMetricsConfig)` Optional. Global configuration for semantic similarity metrics.  
`tool_correctness_metrics_config` |  `[EvaluationMetricsConfig.ToolCorrectnessMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationMetricsConfig.ToolCorrectnessMetricsConfig)` Optional. Configuration for turn level tool correctness metrics.  
`step_tool_correctness_metrics_config` |  `[EvaluationMetricsConfig.ToolCorrectnessMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationMetricsConfig.ToolCorrectnessMetricsConfig)` Optional. Configuration for step level tool correctness metrics.  
  
## HallucinationMetricsConfig

Configuration for the hallucination metrics for the evaluation. To disable the metric, set the message but do not set the `enable_hallucination_metrics` field to true (or explicitly set it to false). To unset the configuration and fallback to the default behavior, omit the message entirely.

Fields  
---  
`enable_hallucination_metrics` |  `bool` Optional. Whether to calculate hallucination metrics for the evaluation.  
  
## ScenarioMetricsConfig

Configuration for the scenario metrics for the evaluation.

Fields  
---  
`user_goal_met_metrics_config` |  `[EvaluationMetricsConfig.UserGoalMetMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationMetricsConfig.UserGoalMetMetricsConfig)` Optional. Configuration for user goal met metrics.  
`expectations_met_metrics_config` |  `[EvaluationMetricsConfig.ExpectationsMetMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationMetricsConfig.ExpectationsMetMetricsConfig)` Optional. Configuration for expectation level metrics.  
  
## SemanticSimilarityMetricsConfig

Configuration for similarity metrics for the evaluation. To disable the metric, set the message but do not set the `enable_semantic_similarity_metrics` field to true (or explicitly set it to false). To unset the configuration and fallback to the default behavior, omit the message entirely.

Fields  
---  
`enable_semantic_similarity_metrics` |  `bool` Optional. Whether to calculate semantic similarity metrics for the evaluation.  
  
## ToolCorrectnessMetricsConfig

Configuration for correctness metrics for the evaluation. To disable the metric, set the message but do not set the `enable_tool_correctness_metrics` field to true (or explicitly set it to false). To unset the configuration and fallback to the default behavior, omit the message entirely.

Fields  
---  
`enable_tool_correctness_metrics` |  `bool` Optional. Whether to calculate tool correctness metrics for the evaluation.  
  
## UserGoalMetMetricsConfig

Configuration for the user goal met metrics for the evaluation. To disable the metric, set the message but do not set the `enable_user_goal_met_metrics` field to true (or explicitly set it to false). To unset the configuration and fallback to the default behavior, omit the message entirely.

Fields  
---  
`enable_user_goal_met_metrics` |  `bool` Optional. Whether to calculate the user goal met metrics for the evaluation.  
  
## EvaluationMetricsThresholds

Threshold settings for metrics in an Evaluation.

Fields  
---  
`golden_evaluation_metrics_thresholds` |  `[EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds)` Optional. The golden evaluation metrics thresholds.  
`hallucination_metric_behavior  
**(deprecated)**` |  `[EvaluationMetricsThresholds.HallucinationMetricBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationMetricsThresholds.HallucinationMetricBehavior)` This item is deprecated!Optional. Deprecated: Use `golden_hallucination_metric_behavior` instead. The hallucination metric behavior is currently used for golden evaluations.  
`golden_hallucination_metric_behavior` |  `[EvaluationMetricsThresholds.HallucinationMetricBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationMetricsThresholds.HallucinationMetricBehavior)` Optional. The hallucination metric behavior for golden evaluations.  
`scenario_hallucination_metric_behavior` |  `[EvaluationMetricsThresholds.HallucinationMetricBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationMetricsThresholds.HallucinationMetricBehavior)` Optional. The hallucination metric behavior for scenario evaluations.  
  
## GoldenEvaluationMetricsThresholds

Settings for golden evaluations.

Fields  
---  
`turn_level_metrics_thresholds` |  `[EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.TurnLevelMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.TurnLevelMetricsThresholds)` Optional. The turn level metrics thresholds.  
`expectation_level_metrics_thresholds` |  `[EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.ExpectationLevelMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.ExpectationLevelMetricsThresholds)` Optional. The expectation level metrics thresholds.  
`tool_matching_settings` |  `[EvaluationMetricsThresholds.ToolMatchingSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationMetricsThresholds.ToolMatchingSettings)` Optional. The tool matching settings. An extra tool call is a tool call that is present in the execution but does not match any tool call in the golden expectation.  
  
## ExpectationLevelMetricsThresholds

Expectation level metrics thresholds.

Fields  
---  
`tool_invocation_parameter_correctness_threshold` |  `float` Optional. The success threshold for individual tool invocation parameter correctness. Must be a float between 0 and 1. Default is 1.0.  
  
## TurnLevelMetricsThresholds

Turn level metrics thresholds.

Fields  
---  
`semantic_similarity_channel` |  `[EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.TurnLevelMetricsThresholds.SemanticSimilarityChannel](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.TurnLevelMetricsThresholds.SemanticSimilarityChannel)` Optional. The semantic similarity channel to use for evaluation.  
`semantic_similarity_success_threshold` |  `int32` Optional. The success threshold for semantic similarity. Must be an integer between 0 and 4. Default is >= 3.  
`overall_tool_invocation_correctness_threshold` |  `float` Optional. The success threshold for overall tool invocation correctness. Must be a float between 0 and 1. Default is 1.0.  
  
## SemanticSimilarityChannel

Semantic similarity channel to use.

Enums  
---  
`SEMANTIC_SIMILARITY_CHANNEL_UNSPECIFIED` | Metric unspecified. Defaults to TEXT.  
`TEXT` | Use text semantic similarity.  
`AUDIO` | Use audio semantic similarity.  
  
## HallucinationMetricBehavior

The hallucination metric behavior. Regardless of the behavior, the metric will always be calculated. The difference is that when disabled, the metric is not used to calculate the overall evaluation score.

Enums  
---  
`HALLUCINATION_METRIC_BEHAVIOR_UNSPECIFIED` | Unspecified hallucination metric behavior.  
`DISABLED` | Disable hallucination metric.  
`ENABLED` | Enable hallucination metric.  
  
## ToolMatchingSettings

Settings for matching tool calls.

Fields  
---  
`extra_tool_call_behavior` |  `[EvaluationMetricsThresholds.ToolMatchingSettings.ExtraToolCallBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationMetricsThresholds.ToolMatchingSettings.ExtraToolCallBehavior)` Optional. Behavior for extra tool calls. Defaults to FAIL.  
  
## ExtraToolCallBehavior

Defines the behavior when an extra tool call is encountered. An extra tool call is a tool call that is present in the execution but does not match any tool call in the golden expectation.

Enums  
---  
`EXTRA_TOOL_CALL_BEHAVIOR_UNSPECIFIED` | Unspecified behavior. Defaults to FAIL.  
`FAIL` | Fail the evaluation if an extra tool call is encountered.  
`ALLOW` | Allow the extra tool call.  
  
## EvaluationPersona

A persona represents an end user in an evaluation.

Fields  
---  
`name` |  `string` Required. The unique identifier of the persona. Format: `projects/{project}/locations/{location}/apps/{app}/evaluationPersonas/{evaluationPersona}`  
`description` |  `string` Optional. The description of the persona.  
`display_name` |  `string` Required. The display name of the persona. Unique within an app.  
`personality` |  `string` Required. An instruction for the agent on how to behave in the evaluation.  
`speech_config` |  `[EvaluationPersona.SpeechConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationPersona.SpeechConfig)` Optional. Configuration for how the persona sounds (TTS settings).  
  
## SpeechConfig

Configuration for Text-to-Speech generation.

Fields  
---  
`speaking_rate` |  `double` Optional. The speaking rate. 1.0 is normal. Lower is slower (e.g., 0.8), higher is faster (e.g., 1.5). Useful for testing how the agent handles fast talkers.  
`environment` |  `[EvaluationPersona.SpeechConfig.BackgroundEnvironment](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationPersona.SpeechConfig.BackgroundEnvironment)` Optional. The simulated audio environment.  
`voice_id` |  `string` Optional. The specific voice identifier/accent to use. Example: "en-US-Wavenet-D" or "en-GB-Standard-A"  
  
## BackgroundEnvironment

Simulated audio environment.

Enums  
---  
`BACKGROUND_ENVIRONMENT_UNSPECIFIED` | Background environment unspecified.  
`CALL_CENTER` | Call center environment.  
`TRAFFIC` | Traffic noise environment.  
`KIDS_NOISE` | Kids noise environment.  
`CAFE` | Cafe environment.  
  
## EvaluationResult

An evaluation result represents the output of running an Evaluation.

Fields  
---  
`name` |  `string` Identifier. The unique identifier of the evaluation result. Format: `projects/{project}/locations/{location}/apps/{app}/evaluations/{evaluation}/results/{result}`  
`display_name` |  `string` Required. Display name of the Evaluation Result. Unique within an Evaluation. By default, it has the following format: " result - ".  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Timestamp when the evaluation result was created.  
`evaluation_status` |  `[EvaluationResult.Outcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationResult.Outcome)` Output only. The outcome of the evaluation. Only populated if execution_state is COMPLETE.  
`evaluation_run` |  `string` Output only. The evaluation run that produced this result. Format: `projects/{project}/locations/{location}/apps/{app}/evaluationRuns/{evaluationRun}`  
`persona` |  `[EvaluationPersona](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationPersona)` Output only. The persona used to generate the conversation for the evaluation result.  
`error_info` |  `[EvaluationErrorInfo](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationErrorInfo)` Output only. Error information for the evaluation result.  
`error  
**(deprecated)**` |  `[Status](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.rpc#google.rpc.Status)` This item is deprecated!Output only. Deprecated: Use `error_info` instead. Errors encountered during execution.  
`initiated_by` |  `string` Output only. The user who initiated the evaluation run that resulted in this result.  
`app_version` |  `string` Output only. The app version used to generate the conversation that resulted in this result. Format: `projects/{project}/locations/{location}/apps/{app}/versions/{version}`  
`app_version_display_name` |  `string` Output only. The display name of the `app_version` that the evaluation ran against.  
`changelog` |  `string` Output only. The changelog of the app version that the evaluation ran against. This is populated if user runs evaluation on latest/draft.  
`changelog_create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The create time of the changelog of the app version that the evaluation ran against. This is populated if user runs evaluation on latest/draft.  
`execution_state` |  `[EvaluationResult.ExecutionState](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationResult.ExecutionState)` Output only. The state of the evaluation result execution.  
`evaluation_metrics_thresholds` |  `[EvaluationMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationMetricsThresholds)` Output only. The evaluation thresholds for the result.  
`config` |  `[EvaluationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationConfig)` Output only. The configuration used in the evaluation run that resulted in this result.  
`golden_run_method` |  `[GoldenRunMethod](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GoldenRunMethod)` Output only. The method used to run the golden evaluation.  
`root_span` |  `[Span](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Span)` Output only. The root span of the evaluation execution, which includes information about each step of the evaluation.  
`outcome_metadata` |  `[EvaluationResult.OutcomeMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationResult.OutcomeMetadata)` Output only. The outcome metadata of the evaluation. Only populated if execution_state is COMPLETE.  
Union field `result`. The result of the evaluation. Only populated when the execution_state is COMPLETED. `result` can be only one of the following:  
`golden_result` |  `[EvaluationResult.GoldenResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationResult.GoldenResult)` Output only. The outcome of a golden evaluation.  
`scenario_result` |  `[EvaluationResult.ScenarioResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationResult.ScenarioResult)` Output only. The outcome of a scenario evaluation.  
  
## EvaluationExpectationResult

The result of a single evaluation expectation.

Fields  
---  
`evaluation_expectation` |  `string` Output only. The evaluation expectation. Format: `projects/{project}/locations/{location}/apps/{app}/evaluationExpectations/{evaluation_expectation}`  
`prompt` |  `string` Output only. The prompt that was used for the evaluation.  
`outcome` |  `[EvaluationResult.Outcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationResult.Outcome)` Output only. The outcome of the evaluation expectation.  
`explanation` |  `string` Output only. The explanation for the result.  
  
## ExecutionState

The state of the evaluation result execution.

Enums  
---  
`EXECUTION_STATE_UNSPECIFIED` | Evaluation result execution state is not specified.  
`QUEUED` | Evaluation result execution is queued.  
`RUNNING` | Evaluation result execution is running.  
`COMPLETED` | Evaluation result execution has completed.  
`ERROR` | Evaluation result execution failed due to an internal error.  
`CANCELLED` | Evaluation result execution was cancelled.  
  
## GoldenExpectationOutcome

Specifies the expectation and the result of that expectation.

Fields  
---  
`expectation` |  `[Evaluation.GoldenExpectation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Evaluation.GoldenExpectation)` Output only. The expectation that was evaluated.  
`outcome` |  `[EvaluationResult.Outcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationResult.Outcome)` Output only. The outcome of the expectation.  
`semantic_similarity_result  
**(deprecated)**` |  `[EvaluationResult.SemanticSimilarityResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationResult.SemanticSimilarityResult)` This item is deprecated!Output only. The result of the semantic similarity check.  
`tool_invocation_result` |  `[EvaluationResult.GoldenExpectationOutcome.ToolInvocationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationResult.GoldenExpectationOutcome.ToolInvocationResult)` Output only. The result of the tool invocation check.  
Union field `result`. The result of the expectation. `result` can be only one of the following:  
`observed_tool_call` |  `[ToolCall](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ToolCall)` Output only. The result of the tool call expectation.  
`observed_tool_response` |  `[ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ToolResponse)` Output only. The result of the tool response expectation.  
`observed_agent_response` |  `[Message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Message)` Output only. The result of the agent response expectation.  
`observed_agent_transfer` |  `[AgentTransfer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentTransfer)` Output only. The result of the agent transfer expectation.  
`observed_payload` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` Output only. An observed custom payload. There are no expectations for custom payloads. This is only used for metrics calculation. The outcome is always SKIPPED.  
  
## ToolInvocationResult

The result of the tool invocation check.

Fields  
---  
`outcome` |  `[EvaluationResult.Outcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationResult.Outcome)` Output only. The outcome of the tool invocation check. This is determined by comparing the parameter_correctness_score to the threshold. If the score is equal to or above the threshold, the outcome will be PASS. Otherwise, the outcome will be FAIL.  
`explanation` |  `string` Output only. A free text explanation for the tool invocation result.  
`parameter_correctness_score` |  `float` Output only. The tool invocation parameter correctness score. This indicates the percent of parameters from the expected tool call that were also present in the actual tool call.  
  
## GoldenResult

The result of a golden evaluation.

Fields  
---  
`turn_replay_results[]` |  `[EvaluationResult.GoldenResult.TurnReplayResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationResult.GoldenResult.TurnReplayResult)` Output only. The result of running each turn of the golden conversation.  
`evaluation_expectation_results[]` |  `[EvaluationResult.EvaluationExpectationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationResult.EvaluationExpectationResult)` Output only. The results of the evaluation expectations.  
  
## TurnReplayResult

The result of running a single turn of the golden conversation.

Fields  
---  
`conversation` |  `string` Output only. The conversation that was generated for this turn.  
`expectation_outcome[]` |  `[EvaluationResult.GoldenExpectationOutcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationResult.GoldenExpectationOutcome)` Output only. The outcome of each expectation.  
`hallucination_result` |  `[EvaluationResult.HallucinationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationResult.HallucinationResult)` Output only. The result of the hallucination check.  
`tool_invocation_score  
**(deprecated)**` |  `float` This item is deprecated!Output only. Deprecated. Use OverallToolInvocationResult instead.  
`turn_latency` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Output only. Duration of the turn.  
`tool_call_latencies[]` |  `[EvaluationResult.ToolCallLatency](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationResult.ToolCallLatency)` Output only. The latency of each tool call in the turn.  
`semantic_similarity_result` |  `[EvaluationResult.SemanticSimilarityResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationResult.SemanticSimilarityResult)` Output only. The result of the semantic similarity check.  
`overall_tool_invocation_result` |  `[EvaluationResult.OverallToolInvocationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationResult.OverallToolInvocationResult)` Output only. The result of the overall tool invocation check.  
`error_info` |  `[EvaluationErrorInfo](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationErrorInfo)` Output only. Information about the error that occurred during this turn.  
`span_latencies[]` |  `[EvaluationResult.SpanLatency](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationResult.SpanLatency)` Output only. The latency of spans in the turn.  
`tool_ordered_invocation_score` |  `float` Output only. The overall tool ordered invocation score for this turn. This indicates the overall percent of tools from the expected turn that were actually invoked in the expected order.  
  
## HallucinationResult

The result of the hallucination check for a single turn.

Fields  
---  
`label` |  `string` Output only. The label associated with each score. Score 1: Justified Score 0: Not Justified Score -1: No Claim To Assess  
`explanation` |  `string` Output only. The explanation for the hallucination score.  
`score` |  `int32` Output only. The hallucination score. Can be -1, 0, 1.  
  
## Outcome

The outcome of the evaluation or expectation.

Enums  
---  
`OUTCOME_UNSPECIFIED` | Evaluation outcome is not specified.  
`PASS` | Evaluation/Expectation passed. In the case of an evaluation, this means that all expectations were met.  
`FAIL` | Evaluation/Expectation failed. In the case of an evaluation, this means that at least one expectation was not met.  
`SKIPPED` | Evaluation/Expectation was skipped.  
  
## OutcomeMetadata

Metadata about the outcome of the evaluation.

Enums  
---  
`OUTCOME_METADATA_UNSPECIFIED` | Unspecified outcome metadata.  
`GRACEFUL_HANDOFF` | The evaluation resulted in a graceful handoff to a human representative.  
  
## OverallToolInvocationResult

The result of the overall tool invocation check.

Fields  
---  
`outcome` |  `[EvaluationResult.Outcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationResult.Outcome)` Output only. The outcome of the tool invocation check. This is determined by comparing the tool_invocation_score to the overall_tool_invocation_correctness_threshold. If the score is equal to or above the threshold, the outcome will be PASS. Otherwise, the outcome will be FAIL.  
`tool_invocation_score` |  `float` The overall tool invocation score for this turn. This indicates the overall percent of tools from the expected turn that were actually invoked.  
  
## ScenarioExpectationOutcome

The outcome of a scenario expectation.

Fields  
---  
`expectation` |  `[Evaluation.ScenarioExpectation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Evaluation.ScenarioExpectation)` Output only. The expectation that was evaluated.  
`outcome` |  `[EvaluationResult.Outcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationResult.Outcome)` Output only. The outcome of the ScenarioExpectation.  
Union field `result`. The result of the expectation. `result` can be only one of the following:  
`observed_tool_call` |  `[EvaluationResult.ScenarioExpectationOutcome.ObservedToolCall](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationResult.ScenarioExpectationOutcome.ObservedToolCall)` Output only. The observed tool call.  
`observed_agent_response` |  `[Message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Message)` Output only. The observed agent response.  
  
## ObservedToolCall

The observed tool call and response.

Fields  
---  
`tool_call` |  `[ToolCall](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ToolCall)` Output only. The observed tool call.  
`tool_response` |  `[ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ToolResponse)` Output only. The observed tool response.  
  
## ScenarioResult

The outcome of a scenario evaluation.

Fields  
---  
`conversation` |  `string` Output only. The conversation that was generated in the scenario.  
`task` |  `string` Output only. The task that was used when running the scenario for this result.  
`user_facts[]` |  `[Evaluation.Scenario.UserFact](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Evaluation.Scenario.UserFact)` Output only. The user facts that were used by the scenario for this result.  
`expectation_outcomes[]` |  `[EvaluationResult.ScenarioExpectationOutcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationResult.ScenarioExpectationOutcome)` Output only. The outcome of each expectation.  
`rubric_outcomes[]` |  `[EvaluationResult.ScenarioRubricOutcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationResult.ScenarioRubricOutcome)` Output only. The outcome of the rubric.  
`hallucination_result[]` |  `[EvaluationResult.HallucinationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationResult.HallucinationResult)` Output only. The result of the hallucination check. There will be one hallucination result for each turn in the conversation.  
`task_completion_result  
**(deprecated)**` |  `[EvaluationResult.TaskCompletionResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationResult.TaskCompletionResult)` This item is deprecated!Output only. The result of the task completion check.  
`tool_call_latencies[]` |  `[EvaluationResult.ToolCallLatency](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationResult.ToolCallLatency)` Output only. The latency of each tool call execution in the conversation.  
`user_goal_satisfaction_result` |  `[EvaluationResult.UserGoalSatisfactionResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationResult.UserGoalSatisfactionResult)` Output only. The result of the user goal satisfaction check.  
`span_latencies[]` |  `[EvaluationResult.SpanLatency](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationResult.SpanLatency)` Output only. The latency of spans in the conversation.  
`evaluation_expectation_results[]` |  `[EvaluationResult.EvaluationExpectationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationResult.EvaluationExpectationResult)` Output only. The results of the evaluation expectations.  
`all_expectations_satisfied` |  `bool` Output only. Whether all expectations were satisfied for this turn.  
`task_completed` |  `bool` Output only. Whether the task was completed for this turn. This is a composite of all expectations satisfied, no hallucinations, and user goal satisfaction.  
  
## ScenarioRubricOutcome

The outcome of the evaluation against the rubric.

Fields  
---  
`rubric` |  `string` Output only. The rubric that was used to evaluate the conversation.  
`score_explanation` |  `string` Output only. The rater's response to the rubric.  
`score` |  `float` Output only. The score of the conversation against the rubric.  
  
## SemanticSimilarityResult

The result of the semantic similarity check.

Fields  
---  
`label` |  `string` Output only. The label associated with each score. Score 4: Fully Consistent Score 3: Mostly Consistent Score 2: Partially Consistent (Minor Omissions) Score 1: Largely Inconsistent (Major Omissions) Score 0: Completely Inconsistent / Contradictory  
`explanation` |  `string` Output only. The explanation for the semantic similarity score.  
`outcome` |  `[EvaluationResult.Outcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationResult.Outcome)` Output only. The outcome of the semantic similarity check. This is determined by comparing the score to the semantic_similarity_success_threshold. If the score is equal to or above the threshold, the outcome will be PASS. Otherwise, the outcome will be FAIL.  
`score` |  `int32` Output only. The semantic similarity score. Can be 0, 1, 2, 3, or 4.  
  
## SpanLatency

The latency of a span execution.

Fields  
---  
`type` |  `[EvaluationResult.SpanLatency.Type](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationResult.SpanLatency.Type)` Output only. The type of span.  
`display_name` |  `string` Output only. The display name of the span. Applicable to tool and guardrail spans.  
`start_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The start time of span.  
`end_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The end time of span.  
`execution_latency` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Output only. The latency of span.  
Union field `identifier`. The identifier of the specific item based on its type. `identifier` can be only one of the following:  
`resource` |  `string` Output only. The resource name of the guardrail or tool spans.  
`toolset` |  `[ToolsetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ToolsetTool)` Output only. The toolset tool identifier.  
`model` |  `string` Output only. The name of the LLM span.  
`callback` |  `string` Output only. The name of the user callback span.  
  
## Type

The type of span. Additional values may be added in the future.

Enums  
---  
`TYPE_UNSPECIFIED` | Default value. This value is unused.  
`TOOL` | Tool call span.  
`USER_CALLBACK` | User callback span.  
`GUARDRAIL` | Guardrail span.  
`LLM` | LLM span.  
  
## TaskCompletionResult

The result of the task completion check for the conversation.

Fields  
---  
`label` |  `string` Output only. The label associated with each score. Score 1: Task Completed Score 0: Task Not Completed Score -1: User Goal Undefined  
`explanation` |  `string` Output only. The explanation for the task completion score.  
`score` |  `int32` Output only. The task completion score. Can be -1, 0, 1  
  
## ToolCallLatency

The latency of a tool call execution.

Fields  
---  
`tool` |  `string` Output only. The name of the tool that got executed. Format: `projects/{project}/locations/{location}/apps/{app}/tools/{tool}`.  
`display_name` |  `string` Output only. The display name of the tool.  
`start_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The start time of the tool call execution.  
`end_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The end time of the tool call execution.  
`execution_latency` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Output only. The latency of the tool call execution.  
  
## UserGoalSatisfactionResult

The result of a user goal satisfaction check for a conversation.

Fields  
---  
`label` |  `string` Output only. The label associated with each score. Score 2: Graceful Handoff Score 1: User Task Satisfied Score 0: User Task Not Satisfied Score -1: User Task Unspecified  
`explanation` |  `string` Output only. The explanation for the user task satisfaction score.  
`score` |  `int32` Output only. The user task satisfaction score. Can be -1, 0, 1, 2.  
  
## EvaluationRun

An evaluation run represents an all the evaluation results from an evaluation execution.

Fields  
---  
`name` |  `string` Identifier. The unique identifier of the evaluation run. Format: `projects/{project}/locations/{location}/apps/{app}/evaluationRuns/{evaluationRun}`  
`display_name` |  `string` Optional. User-defined display name of the evaluation run. default: " run - ".  
`evaluation_results[]` |  `string` Output only. The evaluation results that are part of this run. Format: `projects/{project}/locations/{location}/apps/{app}/evaluations/{evaluation}/results/{result}`  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Timestamp when the evaluation run was created.  
`initiated_by` |  `string` Output only. The user who initiated the evaluation run.  
`app_version` |  `string` Output only. The app version to evaluate. Format: `projects/{project}/locations/{location}/apps/{app}/versions/{version}`  
`app_version_display_name` |  `string` Output only. The display name of the `app_version` that the evaluation ran against.  
`changelog` |  `string` Output only. The changelog of the app version that the evaluation ran against. This is populated if user runs evaluation on latest/draft.  
`changelog_create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The create time of the changelog of the app version that the evaluation ran against. This is populated if user runs evaluation on latest/draft.  
`evaluations[]` |  `string` Output only. The evaluations that are part of this run. The list may contain evaluations of either type. This field is mutually exclusive with `evaluation_dataset`. Format: `projects/{project}/locations/{location}/apps/{app}/evaluations/{evaluation}`  
`evaluation_dataset` |  `string` Output only. The evaluation dataset that this run is associated with. This field is mutually exclusive with `evaluations`. Format: `projects/{project}/locations/{location}/apps/{app}/evaluationDatasets/{evaluationDataset}`  
`evaluation_type` |  `[EvaluationRun.EvaluationType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationRun.EvaluationType)` Output only. The type of the evaluations in this run.  
`state` |  `[EvaluationRun.EvaluationRunState](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationRun.EvaluationRunState)` Output only. The state of the evaluation run.  
`progress` |  `[EvaluationRun.Progress](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationRun.Progress)` Output only. The progress of the evaluation run.  
`config` |  `[EvaluationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationConfig)` Output only. The configuration used in the run.  
`error  
**(deprecated)**` |  `[Status](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.rpc#google.rpc.Status)` This item is deprecated!Output only. Deprecated: Use error_info instead. Errors encountered during execution.  
`error_info` |  `[EvaluationErrorInfo](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationErrorInfo)` Output only. Error information for the evaluation run.  
`evaluation_run_summaries` |  `map<string, `[EvaluationRun.EvaluationRunSummary](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationRun.EvaluationRunSummary)`>` Output only. Map of evaluation name to EvaluationRunSummary.  
`latency_report` |  `[LatencyReport](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.LatencyReport)` Output only. Latency report for the evaluation run.  
`run_count` |  `int32` Output only. The number of times the evaluations inside the run were run.  
`persona_run_configs[]` |  `[PersonaRunConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.PersonaRunConfig)` Output only. The configuration to use for the run per persona.  
`optimization_config` |  `[OptimizationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.OptimizationConfig)` Optional. Configuration for running the optimization step after the evaluation run. If not set, the optimization step will not be run.  
`scheduled_evaluation_run` |  `string` Output only. The scheduled evaluation run resource name that created this evaluation run. This field is only set if the evaluation run was created by a scheduled evaluation run. Format: `projects/{project}/locations/{location}/apps/{app}/scheduledEvaluationRuns/{scheduled_evaluation_run}`  
`golden_run_method` |  `[GoldenRunMethod](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GoldenRunMethod)` Output only. The method used to run the evaluation.  
`operation` |  `string` Output only. The operation that created this evaluation run. Format: `projects/{project}/locations/{location}/operations/{operation}`  
  
## EvaluationRunState

The state of the evaluation run.

Enums  
---  
`EVALUATION_RUN_STATE_UNSPECIFIED` | Evaluation run state is not specified.  
`QUEUED` | Indicates the evaluation run is queued.  
`RUNNING` | Evaluation run is running.  
`COMPLETED` | Evaluation run has completed.  
`ERROR` | The evaluation run has an error.  
`CANCELLED` | Evaluation run was cancelled.  
  
## EvaluationRunSummary

Contains the summary of passed and failed result counts for a specific evaluation in an evaluation run.

Fields  
---  
`passed_count` |  `int32` Output only. Number of passed results for the associated Evaluation in this run.  
`failed_count` |  `int32` Output only. Number of failed results for the associated Evaluation in this run.  
`error_count` |  `int32` Output only. Number of error results for the associated Evaluation in this run.  
  
## EvaluationType

The type of the evaluations in this run. Additional values may be added in the future.

Enums  
---  
`EVALUATION_TYPE_UNSPECIFIED` | Evaluation type is not specified.  
`GOLDEN` | Golden evaluation.  
`SCENARIO` | Scenario evaluation.  
`MIXED` | Indicates the run includes a mix of golden and scenario evaluations.  
  
## Progress

The progress of the evaluation run.

Fields  
---  
`total_count` |  `int32` Output only. Total number of evaluation results in this run.  
`failed_count` |  `int32` Output only. Number of completed evaluation results with an outcome of FAIL. (EvaluationResult.execution_state is COMPLETED and EvaluationResult.evaluation_status is FAIL).  
`error_count` |  `int32` Output only. Number of evaluation results that failed to execute. (EvaluationResult.execution_state is ERROR).  
`completed_count` |  `int32` Output only. Number of evaluation results that finished successfully. (EvaluationResult.execution_state is COMPLETED).  
`passed_count` |  `int32` Output only. Number of completed evaluation results with an outcome of PASS. (EvaluationResult.execution_state is COMPLETED and EvaluationResult.evaluation_status is PASS).  
`cancelled_count` |  `int32` Output only. Number of evaluation results that were cancelled. (EvaluationResult.execution_state is CANCELLED).  
  
## EvaluationRunCachingSettings

Settings for evaluation run caching.

Fields  
---  
`run_caching_mode` |  `[EvaluationRunCachingSettings.EvaluationRunCachingMode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationRunCachingSettings.EvaluationRunCachingMode)` Optional. The caching mode to use for the evaluation run. If not set, default to FORCE_RUN.  
  
## EvaluationRunCachingMode

The evaluation result caching behavior. Controls whether to return the last completed evaluation result (if existing) or to execute a new evaluation.

Enums  
---  
`EVALUATION_RUN_CACHING_MODE_UNSPECIFIED` | The run caching mode is unspecified.  
`FORCE_RUN` | Always execute a full live simulation regardless of whether changelogs exist.  
`SKIP_IF_UNCHANGED` | Skip execution and copy previous verified results if no dependencies have mutated, the evaluation channel/run method are the same.  
  
## EvaluationSettings

Settings for evaluation.

Fields  
---  
`scenario_conversation_initiator` |  `[EvaluationSettings.ScenarioConversationInitiator](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationSettings.ScenarioConversationInitiator)` Optional. Who starts the conversation in a scenario evaluation.  
`golden_run_method` |  `[GoldenRunMethod](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GoldenRunMethod)` Optional. The default method used to run golden evaluations. This will be used if no golden_run_method is specified in the RunEvaluationRequest.  
`golden_evaluation_tool_call_behaviour` |  `[EvaluationToolCallBehaviour](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationToolCallBehaviour)` Optional. Configures the default tool call behaviour for golden evaluations.  
`scenario_evaluation_tool_call_behaviour` |  `[EvaluationToolCallBehaviour](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationToolCallBehaviour)` Optional. Configures the default tool call behaviour for scenario evaluations.  
`metrics_config` |  `[EvaluationMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationMetricsConfig)` Optional. Configures the default metrics for evaluations.  
`scenario_execution_mode` |  `[EvaluationSettings.ScenarioExecutionMode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationSettings.ScenarioExecutionMode)` Optional. The execution mode for scenario evaluations. If not provided, will default to QUALITY_OPTIMIZED.  
`evaluation_run_caching_settings` |  `[EvaluationRunCachingSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationRunCachingSettings)` Optional. The caching settings to use for the evaluation run.  
  
## ScenarioConversationInitiator

Determines who starts the conversation in a scenario evaluation session.

Enums  
---  
`SCENARIO_CONVERSATION_INITIATOR_UNSPECIFIED` | Unspecified. Defaults to USER.  
`USER` | The user starts the conversation.  
`AGENT` | The agent starts the conversation.  
  
## ScenarioExecutionMode

The execution mode for scenario evaluations.

Enums  
---  
`SCENARIO_EXECUTION_MODE_UNSPECIFIED` | Unspecified execution mode. Defaults to QUALITY_OPTIMIZED.  
`QUALITY_OPTIMIZED` | Quality optimized mode.  
`SPEED_OPTIMIZED` | Speed optimized mode.  
  
## EvaluationToolCallBehaviour

Configures the tool call behaviour for evaluation runs.

Enums  
---  
`EVALUATION_TOOL_CALL_BEHAVIOUR_UNSPECIFIED` | Unspecified tool call behavior. Will default to real tool calls.  
`REAL` | Use real tool calls.  
`FAKE` | Use fake tool calls.  
  
## Event

Event input.

Fields  
---  
`event` |  `string` Required. The name of the event.  
`variables` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` Optional. Additional variables associated with the event.  
  
## Example

An example represents a sample conversation between the user and the agent(s).

Fields  
---  
`name` |  `string` Identifier. The unique identifier of the example. Format: `projects/{project}/locations/{location}/apps/{app}/examples/{example}`  
`display_name` |  `string` Required. Display name of the example.  
`description` |  `string` Optional. Human-readable description of the example.  
`entry_agent` |  `string` Optional. The agent that initially handles the conversation. If not specified, the example represents a conversation that is handled by the root agent. Format: `projects/{project}/locations/{location}/apps/{app}/agents/{agent}`  
`messages[]` |  `[Message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Message)` Optional. The collection of messages that make up the conversation.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Timestamp when the example was created.  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Timestamp when the example was last updated.  
`invalid` |  `bool` Output only. The example may become invalid if referencing resources are deleted. Invalid examples will not be used as few-shot examples.  
`etag` |  `string` Etag used to ensure the object hasn't changed during a read-modify-write operation. If the etag is empty, the update will overwrite any concurrent changes.  
  
## ExecuteToolRequest

Request message for `[ToolService.ExecuteTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ToolService.ExecuteTool)`.

Fields  
---  
`parent` |  `string` Required. The resource name of the app which the tool/toolset belongs to. Format: `projects/{project}/locations/{location}/apps/{app}`  
`args` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` Optional. The input parameters and values for the tool in JSON object format.  
`mock_config` |  `[MockConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.MockConfig)` Optional. Mock configuration for the tool execution. If this field is set, tools that call other tools will be mocked based on the provided patterns and responses.  
Union field `tool_identifier`. The identifier of the tool to execute. It could be either a persisted tool or a tool from a toolset. `tool_identifier` can be only one of the following:  
`tool` |  `string` Optional. The name of the tool to execute. Format: projects/{project}/locations/{location}/apps/{app}/tools/{tool}  
`toolset_tool` |  `[ToolsetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ToolsetTool)` Optional. The toolset tool to execute. Only one tool should match the predicate from the toolset. Otherwise, an error will be returned.  
Union field `tool_execution_context`. Additional context to be provided for the tool execution `tool_execution_context` can be only one of the following:  
`variables` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` Optional. The variables that are available for the tool execution.  
`context` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` Optional. The [ToolCallContext](<https://docs.cloud.google.com/customer-engagement-ai/conversational-agents/ps/tool/python#environment> for details) to be passed to the Python tool.  
  
## ExecuteToolResponse

Response message for `[ToolService.ExecuteTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ToolService.ExecuteTool)`.

Fields  
---  
`response` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` The tool execution result in JSON object format. Use "output" key to specify tool response and "error" key to specify error details (if any). If "output" and "error" keys are not specified, then whole "response" is treated as tool execution result.  
`variables` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` The variable values at the end of the tool execution.  
`citations` |  `[Citations](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Citations)` Citations that provide the source information for the tool's execution.  
`google_search_suggestions` |  `[GoogleSearchSuggestions](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GoogleSearchSuggestions)` The suggestions returned from Google Search as a result of invoking the Google Search Tool during the tool execution.  
Union field `tool_identifier`. The identifier of the tool that got executed. `tool_identifier` can be only one of the following:  
`tool` |  `string` The name of the tool that got executed. Format: `projects/{project}/locations/{location}/apps/{app}/tools/{tool}`  
`toolset_tool` |  `[ToolsetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ToolsetTool)` The toolset tool that got executed.  
  
## ExecutionType

The execution type of the tool or toolset.

Enums  
---  
`EXECUTION_TYPE_UNSPECIFIED` | The execution type is unspecified. Defaults to `SYNCHRONOUS` if unspecified.  
`SYNCHRONOUS` | The tool is executed synchronously. The session is blocked until the tool returns.  
`ASYNCHRONOUS` | The tool is executed asynchronously. The session will continue while the tool is executing.  
  
## ExperimentConfig

Experiment for the deployment.

Fields  
---  
`version_release` |  `[ExperimentConfig.VersionRelease](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ExperimentConfig.VersionRelease)` Optional. Version release for the experiment.  
  
## State

State of the experiment.

Enums  
---  
`STATE_UNSPECIFIED` | Unspecified state.  
`PENDING` | Deprecated: This state is no longer used.  
`RUNNING` | Running state. Experiment is running and valid.  
`DONE` | Deprecated: This state is no longer used.  
`EXPIRED` | Deprecated: This state is no longer used.  
  
## VersionRelease

Version release for the experiment.

Fields  
---  
`state` |  `[ExperimentConfig.State](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ExperimentConfig.State)` Optional. State of the version release.  
`traffic_allocations[]` |  `[ExperimentConfig.VersionRelease.TrafficAllocation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ExperimentConfig.VersionRelease.TrafficAllocation)` Optional. Traffic allocations for the version release.  
  
## TrafficAllocation

Traffic allocation for the version release.

Fields  
---  
`id` |  `string` Optional. Id of the traffic allocation. Free format string, up to 128 characters.  
`traffic_percentage` |  `int32` Optional. Traffic percentage of the traffic allocation. Must be between 0 and 100.  
`app_version` |  `string` Optional. App version of the traffic allocation. Format: `projects/{project}/locations/{location}/apps/{app}/versions/{version}`  
  
## ExportAppRequest

Request message for `[AgentService.ExportApp](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.ExportApp)`.

Fields  
---  
`name` |  `string` Required. The resource name of the app to export.  
`export_format` |  `[ExportAppRequest.ExportFormat](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ExportAppRequest.ExportFormat)` Required. The format to export the app in.  
`gcs_uri` |  `string` Optional. The [Google Cloud Storage](https://cloud.google.com/storage/docs/) URI to which to export the app. The format of this URI must be `gs://<bucket-name>/<object-name>`. The exported app archive will be written directly to the specified GCS object.  
`app_version` |  `string` Optional. The resource name of the app version to export. Format: `projects/{project}/locations/{location}/apps/{app}/versions/{version}`.  
  
## ExportFormat

Export format for the app.

Enums  
---  
`EXPORT_FORMAT_UNSPECIFIED` | The export format is unspecified.  
`JSON` | The export format is JSON.  
`YAML` | The export format is YAML.  
  
## ExportAppResponse

Response message for `[AgentService.ExportApp](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.ExportApp)`.

Fields  
---  
Union field `app`. The exported app. `app` can be only one of the following:  
`app_content` |  `bytes` App folder compressed as a zip file.  
`app_uri` |  `string` The [Google Cloud Storage](https://cloud.google.com/storage/docs/) URI to which the app was exported.  
  
## ExportEvaluationResultsOperationMetadata

This type has no fields.

Operation metadata for `[EvaluationService.ExportEvaluationResults](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationService.ExportEvaluationResults)`.

## ExportEvaluationResultsRequest

Request message for `[EvaluationService.ExportEvaluationResults](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationService.ExportEvaluationResults)`.

Fields  
---  
`parent` |  `string` Required. The resource name of the evaluation to export evaluation results from. Format: `projects/{project}/locations/{location}/apps/{app}/evaluations/{evaluation}`  
`names[]` |  `string` Required. The resource names of the evaluation results to export.  
`export_options` |  `[ExportOptions](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ExportOptions)` Optional. The export options for the evaluation results.  
  
## ExportEvaluationResultsResponse

Response message for `[EvaluationService.ExportEvaluationResults](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationService.ExportEvaluationResults)`.

Fields  
---  
Union field `evaluation_results`. The exported evaluation results. `evaluation_results` can be only one of the following:  
`evaluation_results_content` |  `bytes` The content of the exported Evaluation Results. This will be populated if gcs_uri was not specified in the request.  
`evaluation_results_uri` |  `string` The Google Cloud Storage URI folder where the exported Evaluation Results were written. This will be populated if gcs_uri was specified in the request.  
  
## ExportEvaluationRunsOperationMetadata

This type has no fields.

Operation metadata for `[EvaluationService.ExportEvaluationRuns](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationService.ExportEvaluationRuns)`.

## ExportEvaluationRunsRequest

Request message for `[EvaluationService.ExportEvaluationRuns](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationService.ExportEvaluationRuns)`.

Fields  
---  
`parent` |  `string` Required. The resource name of the app to export evaluation runs from. Format: `projects/{project}/locations/{location}/apps/{app}`  
`names[]` |  `string` Required. The resource names of the evaluation runs to export.  
`export_options` |  `[ExportOptions](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ExportOptions)` Optional. The export options for the evaluation runs.  
  
## ExportEvaluationRunsResponse

Response message for `[EvaluationService.ExportEvaluationRuns](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationService.ExportEvaluationRuns)`.

Fields  
---  
Union field `evaluation_runs`. The exported evaluation runs. `evaluation_runs` can be only one of the following:  
`evaluation_runs_content` |  `bytes` The content of the exported Evaluation Runs. This will be populated if gcs_uri was not specified in the request.  
`evaluation_runs_uri` |  `string` The Google Cloud Storage URI folder where the exported Evaluation Runs were written. This will be populated if gcs_uri was specified in the request.  
  
## ExportEvaluationsRequest

Request message for `[EvaluationService.ExportEvaluations](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationService.ExportEvaluations)`.

Fields  
---  
`parent` |  `string` Required. The resource name of the app to export evaluations from. Format: `projects/{project}/locations/{location}/apps/{app}`  
`names[]` |  `string` Required. The resource names of the evaluations to export.  
`export_options` |  `[ExportOptions](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ExportOptions)` Optional. The export options for the evaluations.  
`include_evaluation_results` |  `bool` Optional. Includes evaluation results in the export. At least one of include_evaluation_results or include_evaluations must be set.  
`include_evaluations` |  `bool` Optional. Includes evaluations in the export. At least one of include_evaluation_results or include_evaluations must be set.  
  
## ExportEvaluationsResponse

Response message for `[EvaluationService.ExportEvaluations](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationService.ExportEvaluations)`.

Fields  
---  
`failed_evaluations` |  `map<string, string>` Output only. A map of evaluation resource names that could not be exported, to the reason why they failed.  
Union field `evaluations`. The exported evaluations. `evaluations` can be only one of the following:  
`evaluations_content` |  `bytes` The content of the exported Evaluations. This will be populated if gcs_uri was not specified in the request.  
`evaluations_uri` |  `string` The Google Cloud Storage URI folder where the exported evaluations were written. This will be populated if gcs_uri was specified in the request.  
  
## ExportOptions

Options for exporting CES evaluation resources.

Fields  
---  
`export_format` |  `[ExportOptions.ExportFormat](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ExportOptions.ExportFormat)` Optional. The format to export the evaluation results in. Defaults to JSON if not specified.  
`gcs_uri` |  `string` Optional. The Google Cloud Storage URI to write the exported Evaluation Results to.  
  
## ExportFormat

The format to export the items in. Defaults to JSON if not specified.

Enums  
---  
`EXPORT_FORMAT_UNSPECIFIED` | Unspecified format.  
`JSON` | JSON format.  
`YAML` | YAML format.  
  
## ExpressionCondition

Expression condition based on session state.

Fields  
---  
`expression` |  `string` Required. The string representation of cloud.api.Expression condition.  
  
## FileContext

Files to be used as context. Files can be provided as raw bytes.

Fields  
---  
Union field `file`. File provided as context. `file` can be only one of the following:  
`file_bytes` |  `[FileContext.FileBytes](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.FileContext.FileBytes)` Optional. File provided as raw bytes.  
  
## FileBytes

File provided as raw bytes.

Fields  
---  
`file_name` |  `string` Required. The name of the file provided as raw bytes.  
`mime_type` |  `string` Required. The IANA standard MIME type of the source data.  
`data` |  `bytes` Required. Raw bytes of the file.  
  
## FileSearchTool

The file search tool allows the agent to search across the files uploaded by the app/agent developer. It has presets to give relatively good quality search over the uploaded files and summarization of the retrieved results.

Fields  
---  
`corpus_type` |  `[FileSearchTool.CorpusType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.FileSearchTool.CorpusType)` Optional. The type of the corpus. Default is FULLY_MANAGED.  
`name` |  `string` Required. The tool name.  
`description` |  `string` Optional. The tool description.  
`file_corpus` |  `string` Optional. The corpus where files are stored. Format: projects/{project}/locations/{location}/ragCorpora/{rag_corpus}  
  
## CorpusType

The type of the Vertex RAG corpus.

Enums  
---  
`CORPUS_TYPE_UNSPECIFIED` | Unspecified corpus type.  
`USER_OWNED` | The corpus is created and owned by the user.  
`FULLY_MANAGED` | The corpus is created by the agent.  
  
## GenerateAppResourceOperationMetadata

Operation metadata for `[AgentService.GenerateAppResource](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.GenerateAppResource)`.

Fields  
---  
`generation_type` |  `[GenerateAppResourceOperationMetadata.GenerationType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GenerateAppResourceOperationMetadata.GenerationType)` Output only. The type of the operation.  
`message` |  `string` Output only. Human-readable status of the operation, if any.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time the operation was created.  
`end_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time the operation finished running.  
`target` |  `string` Output only. The resource name of the app that the operation is associated with. Format: `projects/{project}/locations/{location}/apps/{app}`.  
`partial_errors[]` |  `[Status](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.rpc#google.rpc.Status)` Output only. Error messages from the resource generation process.  
  
## GenerationType

The type of the generation operation.

Enums  
---  
`GENERATION_TYPE_UNSPECIFIED` | Unspecified operation type.  
`AGENT_RESTRUCTURE` | Agent instruction restructure type.  
`AGENT_REFINE` | Agent instruction refinement type.  
`AGENT_CREATE` | Agent creation from type.  
`TOOL_CREATE` | Tool creation type.  
`SCENARIO_CREATE` | Scenario creation type.  
`SCENARIO_CREATE_FROM_TRANSCRIPTS` | Scenario creation from transcripts type.  
`EVALUATION_PERSONA_CREATE` | Evaluation persona generation type.  
`QUALITY_REPORT_CREATE` | Quality report generation type.  
`INSTRUCTION_FOLLOWING_FIX` | Instruction following fix type (used for hill climbing fixes).  
  
## GenerateAppResourceRequest

Request message for `[AgentService.GenerateAppResource](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.GenerateAppResource)`.

Fields  
---  
`parent` |  `string` Required. The resource name of the app to generate the resource for.  
`refine_instructions[]` |  `[GenerateAppResourceRequest.RefineInstructions](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GenerateAppResourceRequest.RefineInstructions)` Optional. List of refine instructions to be used to refine the resource.  
`tool_generation_config` |  `[GenerateAppResourceRequest.ToolGenerationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GenerateAppResourceRequest.ToolGenerationConfig)` Optional. The configuration to be used to generate the tool.  
`app_generation_config` |  `[GenerateAppResourceRequest.AppGenerationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GenerateAppResourceRequest.AppGenerationConfig)` Optional. The configuration to be used to generate the agents and tools.  
`evaluation_generation_config` |  `[GenerateAppResourceRequest.EvaluationGenerationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GenerateAppResourceRequest.EvaluationGenerationConfig)` Optional. The configuration to be used to generate the evaluations.  
`evaluation_personas_generation_config` |  `[GenerateAppResourceRequest.EvaluationPersonasGenerationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GenerateAppResourceRequest.EvaluationPersonasGenerationConfig)` Optional. The configuration to be used to generate the evaluation personas.  
`quality_report_generation_config` |  `[GenerateAppResourceRequest.QualityReportGenerationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GenerateAppResourceRequest.QualityReportGenerationConfig)` Optional. The configuration to be used for quality report generation.  
`hill_climbing_fix_config` |  `[GenerateAppResourceRequest.HillClimbingFixConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GenerateAppResourceRequest.HillClimbingFixConfig)` Optional. The configuration to be used for hill climbing fixes.  
Union field `resource`. The resource to generate. `resource` can be only one of the following:  
`agent` |  `[Agent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Agent)` The agent resource to be used by the LLM assistant, can be empty for generating a new agent.  
`tool` |  `[Tool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Tool)` The tool resource to be used by the LLM assistant, can be empty for generating a new tool.  
`toolset` |  `[Toolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Toolset)` The toolset resource to be used by the LLM assistant, can be empty for generating a new toolset.  
`app_version_context` |  `[GenerateAppResourceRequest.AppVersionContext](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GenerateAppResourceRequest.AppVersionContext)` The app version context specifying the base snapshot and target agent.  
  
## AppGenerationConfig

The configuration to be used to generate the app.

Fields  
---  
`context` |  `string` Optional. The context which describes the requirements of the agents & tools to be generated.  
`file_contexts[]` |  `[FileContext](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.FileContext)` Optional. The files to be used as context.  
`dataset_id` |  `string` Optional. The insights dataset to be used to fetch conversation data for generating the agents & tools. Format: `projects/{project}/locations/{location}/datasets/{dataset}`.  
`generate_evaluations` |  `bool` Optional. Whether to generate the evaluations for the app. If true, the provided context will be used to generate the evaluations data.  
`gcs_location` |  `string` Optional. The Cloud Storage location to store the generated question answer data to be used by the Datastore tool. This data is generated only when using conversation data as an input source. The location must be in the same project as the app. Format: `gs://...`.  
  
## AppVersionContext

The app version context specifying the base snapshot and target agent.

Fields  
---  
`app_version` |  `string` The resource name of the app version to be used by the LLM assistant. Format: `projects/{project}/locations/{location}/apps/{app}/versions/{version}`  
`agent_resource_name` |  `string` The resource name of the target agent to be used by the LLM assistant. Format: `projects/{project}/locations/{location}/apps/{app}/agents/{agent}`  
  
## EvaluationGenerationConfig

The configuration to be used to generate the evaluations.

Fields  
---  
`dataset_id` |  `string` Optional. The insights dataset to be used to fetch conversation data for generating the evaluations. Format: `projects/{project}/locations/{location}/datasets/{dataset}`.  
  
## EvaluationPersonasGenerationConfig

This type has no fields.

The configuration to be used to generate the evaluation personas.

## HillClimbingFixConfig

The configuration to be used for hill climbing fixes.

Fields  
---  
`quality_report` |  `[QualityReport](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.QualityReport)` Required. The quality report used to inform the instruction following fix.  
  
## QualityReportGenerationConfig

The configuration to be used for quality report generation.

Fields  
---  
`evaluation_run` |  `string` Required. The evaluation run used to inform quality report analysis.  
`algorithm` |  `[GenerateAppResourceRequest.QualityReportGenerationConfig.LossAttributionAlgorithm](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GenerateAppResourceRequest.QualityReportGenerationConfig.LossAttributionAlgorithm)` Optional. The loss attribution algorithm to use.  
  
## LossAttributionAlgorithm

The algorithm to use for loss attribution.

Enums  
---  
`LOSS_ATTRIBUTION_ALGORITHM_UNSPECIFIED` | Unspecified.  
`APP_CENTRIC` | App-centric loss attribution. Treats the app as a single unit.  
`AGENT_CENTRIC` | Agent-centric loss attribution. Attributes loss to individual agents.  
  
## RefineInstructions

The instructions to be used to refine a part of the resource. The part of the resource can be specified with a start index, end index and a field mask. For example, if you want to refine a part of the agent instructions you can specify the index of the first character of the instructions, the index of the last character of the instructions and the field mask as "instructions".

Fields  
---  
`start_index` |  `int64` Required. The first character (inclusive) of the text to refine.  
`end_index` |  `int64` Required. The last character (inclusive) of the text to refine.  
`field_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Required. The field of the resource being refined. Only one field is allowed per RefineInstructions. If refining agent instructions, the field mask should be "instructions".  
`instructions` |  `string` Required. The instructions to refine the resource.  
  
## ToolGenerationConfig

The configuration to be used to generate a tool.

Fields  
---  
`context` |  `string` Optional. The context which describes the tool to be generated. This can be empty if the tool request & response are provided.  
`file_contexts[]` |  `[FileContext](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.FileContext)` Optional. The files to be used as context.  
`open_api_toolset_generation_config` |  `[GenerateAppResourceRequest.ToolGenerationConfig.OpenApiToolsetGenerationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GenerateAppResourceRequest.ToolGenerationConfig.OpenApiToolsetGenerationConfig)` Optional. The configuration to be used to generate an Open API schema.  
  
## OpenApiToolsetGenerationConfig

The configuration to be used to generate an Open API schema.

Fields  
---  
`uri` |  `string` Required. The base uri of the tool.  
`operation_generation_configs[]` |  `[GenerateAppResourceRequest.ToolGenerationConfig.OpenApiToolsetGenerationConfig.OperationGenerationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GenerateAppResourceRequest.ToolGenerationConfig.OpenApiToolsetGenerationConfig.OperationGenerationConfig)` Required. The list of operations to be added to the Open API schema.  
  
## OperationGenerationConfig

The configuration to be used to generate an operation in the Open API schema.

Fields  
---  
`method` |  `string` Required. The uri of the tool. This should include query and path parameters if any.  
`path` |  `string` Required. The path of the tool to be appended to the base uri. This should include query and path parameters if any.  
`request_json` |  `string` Required. A sample request to the tool in JSON format. Skip if the tool does not support request body.  
`response_json` |  `string` Required. A sample response from the tool in JSON format.  
  
## GenerateAppResourceResponse

Response message for `[AgentService.GenerateAppResource](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.GenerateAppResource)`.

Fields  
---  
`generate_result_info` |  `[GenerateAppResourceResponse.GenerateResultInfo](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GenerateAppResourceResponse.GenerateResultInfo)` Additional information about the generated result.  
Union field `generated_resource`. The generated resource. `generated_resource` can be only one of the following:  
`agent` |  `[Agent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Agent)` Agent generated by the LLM assistant.  
`toolset` |  `[Toolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Toolset)` Toolset generated by the LLM assistant. Supports Open API toolset schema generation.  
`app_snapshot` |  `[AppSnapshot](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AppSnapshot)` App snapshot generated by the LLM assistant. This snapshot contains the app, agents & tools generated by the LLM assistant.  
`tools` |  `[GenerateAppResourceResponse.Tools](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GenerateAppResourceResponse.Tools)` The list of tools generated by the LLM assistant.  
`evaluations` |  `[GenerateAppResourceResponse.Evaluations](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GenerateAppResourceResponse.Evaluations)` Evaluations generated by the LLM assistant.  
`app_resources` |  `[GenerateAppResourceResponse.AppResources](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GenerateAppResourceResponse.AppResources)` The app resources generated by the LLM assistant.  
`quality_report` |  `[QualityReport](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.QualityReport)` The quality report generated by the LLM assistant.  
  
## AppResources

The list of app resources generated by the LLM assistant.

Fields  
---  
`app_snapshot` |  `[AppSnapshot](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AppSnapshot)` The app snapshot generated by the LLM assistant. This snapshot contains the app, agents & tools generated by the LLM assistant.  
`evaluations[]` |  `[Evaluation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Evaluation)` The list of evaluations generated by the LLM assistant.  
  
## Evaluations

The list of evaluations generated by the LLM assistant.

Fields  
---  
`evaluations[]` |  `[Evaluation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Evaluation)` The list of generated evaluations.  
  
## GenerateResultInfo

This provides additional information about the generated result.

Fields  
---  
`explanation` |  `string` An explanation of the changes in the generated resource.  
  
## Tools

The list of tools generated by the LLM assistant.

Fields  
---  
`tools[]` |  `[Tool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Tool)` The list of tools generated by the LLM assistant.  
  
## GenerateChatTokenRequest

Request message for `[WidgetService.GenerateChatToken](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.WidgetService.GenerateChatToken)`.

Fields  
---  
`name` |  `string` Required. The session name to generate the chat token for. Format: projects/{project}/locations/{location}/apps/{app}/sessions/{session}  
`deployment` |  `string` Required. The deployment of the app to use for the session. Format: projects/{project}/locations/{location}/apps/{app}/deployments/{deployment}  
`recaptcha_token` |  `string` Optional. The reCAPTCHA token generated by the client-side chat widget.  
`live_handoff_enabled` |  `bool` Optional. Indicates if live handoff is enabled for the session.  
  
## GenerateChatTokenResponse

Response message for `[WidgetService.GenerateChatToken](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.WidgetService.GenerateChatToken)`.

Fields  
---  
`chat_token` |  `string` The session scoped token for chat widget to authenticate with Session APIs.  
`expire_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` The time at which the chat token expires.  
  
## GenerateEvaluationOperationMetadata

This type has no fields.

Operation metadata for `[EvaluationService.GenerateEvaluation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationService.GenerateEvaluation)`.

## GenerateEvaluationRequest

Request message for `[EvaluationService.GenerateEvaluation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationService.GenerateEvaluation)`.

Fields  
---  
`conversation` |  `string` Required. The conversation to create the golden evaluation for. Format: `projects/{project}/locations/{location}/apps/{app}/conversations/{conversation}`  
`source  
**(deprecated)**` |  `[Conversation.Source](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Conversation.Source)` This item is deprecated!Optional. Indicate the source of the conversation. If not set, all sources will be searched.  
`evaluation_type` |  `[GenerateEvaluationRequest.EvaluationType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GenerateEvaluationRequest.EvaluationType)` Optional. The type of evaluation to generate. Defaults to GOLDEN if unspecified.  
  
## EvaluationType

The type of evaluation to generate.

Enums  
---  
`EVALUATION_TYPE_UNSPECIFIED` | Unspecified type. Defaults to GOLDEN.  
`GOLDEN` | Golden evaluation.  
`SCENARIO` | Scenario evaluation.  
  
## GetAgentRequest

Request message for `[AgentService.GetAgent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.GetAgent)`.

Fields  
---  
`name` |  `string` Required. The resource name of the agent to retrieve.  
  
## GetAppRequest

Request message for `[AgentService.GetApp](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.GetApp)`.

Fields  
---  
`name` |  `string` Required. The resource name of the app to retrieve.  
  
## GetAppVersionRequest

Request message for `[AgentService.GetAppVersion](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.GetAppVersion)`.

Fields  
---  
`name` |  `string` Required. The resource name of the app version to retrieve.  
  
## GetChangelogRequest

Request message for `[AgentService.GetChangelog](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.GetChangelog)`.

Fields  
---  
`name` |  `string` Required. The resource name of the changelog to retrieve.  
  
## GetConversationRequest

Request message for `[AgentService.GetConversation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.GetConversation)`.

Fields  
---  
`name` |  `string` Required. The resource name of the conversation to retrieve.  
`source  
**(deprecated)**` |  `[Conversation.Source](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Conversation.Source)` This item is deprecated!Optional. Indicate the source of the conversation. If not set, all source will be searched.  
  
## GetDeploymentRequest

Request message for `[AgentService.GetDeployment](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.GetDeployment)`.

Fields  
---  
`name` |  `string` Required. The name of the deployment. Format: `projects/{project}/locations/{location}/apps/{app}/deployments/{deployment}`  
  
## GetEvaluationDatasetRequest

Request message for `[EvaluationService.GetEvaluationDataset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationService.GetEvaluationDataset)`.

Fields  
---  
`name` |  `string` Required. The resource name of the evaluation dataset to retrieve.  
  
## GetEvaluationExpectationRequest

Request message for `[EvaluationService.GetEvaluationExpectation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationService.GetEvaluationExpectation)`.

Fields  
---  
`name` |  `string` Required. The resource name of the evaluation expectation to retrieve.  
  
## GetEvaluationRequest

Request message for `[EvaluationService.GetEvaluation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationService.GetEvaluation)`.

Fields  
---  
`name` |  `string` Required. The resource name of the evaluation to retrieve.  
  
## GetEvaluationResultRequest

Request message for `[EvaluationService.GetEvaluationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationService.GetEvaluationResult)`.

Fields  
---  
`name` |  `string` Required. The resource name of the evaluation result to retrieve.  
  
## GetEvaluationRunRequest

Request message for `[EvaluationService.GetEvaluationRun](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationService.GetEvaluationRun)`.

Fields  
---  
`name` |  `string` Required. The resource name of the evaluation run to retrieve.  
  
## GetExampleRequest

Request message for `[AgentService.GetExample](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.GetExample)`.

Fields  
---  
`name` |  `string` Required. The resource name of the example to retrieve.  
  
## GetGuardrailRequest

Request message for `[AgentService.GetGuardrail](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.GetGuardrail)`.

Fields  
---  
`name` |  `string` Required. The resource name of the guardrail to retrieve.  
  
## GetScheduledEvaluationRunRequest

Request message for `[EvaluationService.GetScheduledEvaluationRun](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationService.GetScheduledEvaluationRun)`.

Fields  
---  
`name` |  `string` Required. The resource name of the scheduled evaluation run to retrieve.  
  
## GetSecuritySettingsRequest

Request message for `[AgentService.GetSecuritySettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.GetSecuritySettings)`.

Fields  
---  
`name` |  `string` Required. The resource name of the security settings to retrieve. Format: `projects/{project}/locations/{location}/securitySettings`  
  
## GetToolRequest

Request message for `[AgentService.GetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.GetTool)`.

Fields  
---  
`name` |  `string` Required. The resource name of the tool to retrieve.  
  
## GetToolsetRequest

Request message for `[AgentService.GetToolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.GetToolset)`.

Fields  
---  
`name` |  `string` Required. The resource name of the toolset to retrieve.  
  
## GoAway

This type has no fields.

Indicates that the server will disconnect soon and the client should half-close and restart the connection.

## GoldenRunMethod

The method used to run the evaluation.

Enums  
---  
`GOLDEN_RUN_METHOD_UNSPECIFIED` | Run method is not specified.  
`STABLE` | Run the evaluation as stable replay, where each turn is a unique session with the previous expected turns injected as context.  
`NAIVE` | Run the evaluation as naive replay, where the run is a single session with no context injected.  
  
## GoogleSearchSuggestions

Search suggestions from `[Google Search Tool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GoogleSearchTool)`.

Fields  
---  
`htmls[]` |  `string` Compliant HTML and CSS styling for search suggestions. The provided HTML and CSS automatically adapts to your device settings, displaying in either light or dark mode indicated by `@media(prefers-color-scheme)`.  
`web_search_queries[]` |  `[WebSearchQuery](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.WebSearchQuery)` List of queries used to perform the google search along with the search result URIs forming the search suggestions.  
  
## GoogleSearchTool

Represents a tool to perform Google web searches for grounding. See <https://cloud.google.com/customer-engagement-ai/conversational-agents/ps/tool#google-search>.

Fields  
---  
`name` |  `string` Required. The name of the tool.  
`description` |  `string` Optional. Description of the tool's purpose.  
`context_urls[]` |  `string` Optional. Content will be fetched directly from these URLs for context and grounding. Example: "https://example.com/path.html". A maximum of 20 URLs are allowed.  
`preferred_domains[]` |  `string` Optional. Specifies domains to restrict search results to. Example: "example.com", "another.site". A maximum of 20 domains can be specified.  
`exclude_domains[]` |  `string` Optional. List of domains to be excluded from the search results. Example: "example.com". A maximum of 2000 domains can be excluded.  
`prompt_config` |  `[GoogleSearchTool.PromptConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GoogleSearchTool.PromptConfig)` Optional. Prompt instructions passed to planner on how the search results should be processed for text and voice.  
  
## PromptConfig

Prompt settings used by the model when processing or summarizing the google search results.

Fields  
---  
`text_prompt` |  `string` Optional. Defines the prompt used for the system instructions when interacting with the agent in chat conversations. If not set, default prompt will be used.  
`voice_prompt` |  `string` Optional. Defines the prompt used for the system instructions when interacting with the agent in voice conversations. If not set, default prompt will be used.  
  
## Guardrail

Guardrail contains a list of checks and balances to keep the agents safe and secure.

Fields  
---  
`name` |  `string` Identifier. The unique identifier of the guardrail. Format: `projects/{project}/locations/{location}/apps/{app}/guardrails/{guardrail}`  
`display_name` |  `string` Required. Display name of the guardrail.  
`description` |  `string` Optional. Description of the guardrail.  
`enabled` |  `bool` Optional. Whether the guardrail is enabled.  
`action` |  `[TriggerAction](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.TriggerAction)` Optional. Action to take when the guardrail is triggered.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Timestamp when the guardrail was created.  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Timestamp when the guardrail was last updated.  
`etag` |  `string` Etag used to ensure the object hasn't changed during a read-modify-write operation. If the etag is empty, the update will overwrite any concurrent changes.  
Union field `guardrail_type`. Guardrail type. `guardrail_type` can be only one of the following:  
`content_filter` |  `[Guardrail.ContentFilter](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Guardrail.ContentFilter)` Optional. Guardrail that bans certain content from being used in the conversation.  
`llm_prompt_security` |  `[Guardrail.LlmPromptSecurity](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Guardrail.LlmPromptSecurity)` Optional. Guardrail that blocks the conversation if the prompt is considered unsafe based on the LLM classification.  
`llm_policy` |  `[Guardrail.LlmPolicy](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Guardrail.LlmPolicy)` Optional. Guardrail that blocks the conversation if the LLM response is considered violating the policy based on the LLM classification.  
`model_safety` |  `[Guardrail.ModelSafety](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Guardrail.ModelSafety)` Optional. Guardrail that blocks the conversation if the LLM response is considered unsafe based on the model safety settings.  
`code_callback` |  `[Guardrail.CodeCallback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Guardrail.CodeCallback)` Optional. Guardrail that potentially blocks the conversation based on the result of the callback execution.  
`supervisor` |  `[Guardrail.Supervisor](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Guardrail.Supervisor)` Optional. Guardrail that runs supervisor intervention.  
  
## CodeCallback

Guardrail that blocks the conversation based on the code callbacks provided.

Fields  
---  
`before_agent_callback` |  `[Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Callback)` Optional. The callback to execute before the agent is called. Each callback function is expected to return a structure (e.g., a dict or object) containing at least: - 'decision': Either 'OK' or 'TRIGGER'. - 'reason': A string explaining the decision. A 'TRIGGER' decision may halt further processing.  
`after_agent_callback` |  `[Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Callback)` Optional. The callback to execute after the agent is called. Each callback function is expected to return a structure (e.g., a dict or object) containing at least: - 'decision': Either 'OK' or 'TRIGGER'. - 'reason': A string explaining the decision. A 'TRIGGER' decision may halt further processing.  
`before_model_callback` |  `[Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Callback)` Optional. The callback to execute before the model is called. If there are multiple calls to the model, the callback will be executed multiple times. Each callback function is expected to return a structure (e.g., a dict or object) containing at least: - 'decision': Either 'OK' or 'TRIGGER'. - 'reason': A string explaining the decision. A 'TRIGGER' decision may halt further processing.  
`after_model_callback` |  `[Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Callback)` Optional. The callback to execute after the model is called. If there are multiple calls to the model, the callback will be executed multiple times. Each callback function is expected to return a structure (e.g., a dict or object) containing at least: - 'decision': Either 'OK' or 'TRIGGER'. - 'reason': A string explaining the decision. A 'TRIGGER' decision may halt further processing.  
  
## ContentFilter

Guardrail that bans certain content from being used in the conversation.

Fields  
---  
`banned_contents[]` |  `string` Optional. List of banned phrases. Applies to both user inputs and agent responses.  
`banned_contents_in_user_input[]` |  `string` Optional. List of banned phrases. Applies only to user inputs.  
`banned_contents_in_agent_response[]` |  `string` Optional. List of banned phrases. Applies only to agent responses.  
`match_type` |  `[Guardrail.ContentFilter.MatchType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Guardrail.ContentFilter.MatchType)` Required. Match type for the content filter.  
`disregard_diacritics` |  `bool` Optional. If true, diacritics are ignored during matching.  
  
## MatchType

Match type for the content filter.

Enums  
---  
`MATCH_TYPE_UNSPECIFIED` | Match type is not specified.  
`SIMPLE_STRING_MATCH` | Content is matched for substrings character by character.  
`WORD_BOUNDARY_STRING_MATCH` | Content only matches if the pattern found in the text is surrounded by word delimiters. Banned phrases can also contain word delimiters.  
`REGEXP_MATCH` | Content is matched using regular expression syntax.  
  
## LlmPolicy

Guardrail that blocks the conversation if the LLM response is considered violating the policy based on the LLM classification.

Fields  
---  
`max_conversation_messages` |  `int32` Optional. When checking this policy, consider the last 'n' messages in the conversation. When not set a default value of 10 will be used.  
`model_settings` |  `[ModelSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ModelSettings)` Optional. Model settings.  
`prompt` |  `string` Required. Policy prompt.  
`policy_scope` |  `[Guardrail.LlmPolicy.PolicyScope](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Guardrail.LlmPolicy.PolicyScope)` Required. Defines when to apply the policy check during the conversation. If set to `POLICY_SCOPE_UNSPECIFIED`, the policy will be applied to the user input. When applying the policy to the agent response, additional latency will be introduced before the agent can respond.  
`fail_open` |  `bool` Optional. If an error occurs during the policy check, fail open and do not trigger the guardrail.  
`allow_short_utterance` |  `bool` Optional. By default, the LLM policy check is bypassed for short utterances. Enabling this setting applies the policy check to all utterances, including those that would normally be skipped.  
  
## PolicyScope

Defines when to apply the policy check during the conversation.

Enums  
---  
`POLICY_SCOPE_UNSPECIFIED` | Policy scope is not specified.  
`USER_QUERY` | Policy check is triggered on user input.  
`AGENT_RESPONSE` | Policy check is triggered on agent response. Applying this policy scope will introduce additional latency before the agent can respond.  
`USER_QUERY_AND_AGENT_RESPONSE` | Policy check is triggered on both user input and agent response. Applying this policy scope will introduce additional latency before the agent can respond.  
  
## LlmPromptSecurity

Guardrail that blocks the conversation if the input is considered unsafe based on the LLM classification.

Fields  
---  
`fail_open` |  `bool` Optional. Determines the behavior when the guardrail encounters an LLM error. - If true: the guardrail is bypassed. - If false (default): the guardrail triggers/blocks.Note: If a custom policy is provided, this field is ignored in favor of the policy's 'fail_open' configuration.  
Union field `security_config`. Defines the security configuration mode. The user must choose one of the following configurations. `security_config` can be only one of the following:  
`default_settings` |  `[Guardrail.LlmPromptSecurity.DefaultSecuritySettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Guardrail.LlmPromptSecurity.DefaultSecuritySettings)` Optional. Use the system's predefined default security settings. To select this mode, include an empty 'default_settings' message in the request. The 'default_prompt_template' field within will be populated by the server in the response.  
`custom_policy` |  `[Guardrail.LlmPolicy](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Guardrail.LlmPolicy)` Optional. Use a user-defined LlmPolicy to configure the security guardrail.  
  
## DefaultSecuritySettings

Configuration for default system security settings.

Fields  
---  
`default_prompt_template` |  `string` Output only. The default prompt template used by the system. This field is for display purposes to show the user what prompt the system uses by default. It is OUTPUT_ONLY.  
  
## ModelSafety

Model safety settings overrides. When this is set, it will override the default settings and trigger the guardrail if the response is considered unsafe.

Fields  
---  
`safety_settings[]` |  `[Guardrail.ModelSafety.SafetySetting](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Guardrail.ModelSafety.SafetySetting)` Required. List of safety settings.  
  
## HarmBlockThreshold

Probability based thresholds levels for blocking.

Enums  
---  
`HARM_BLOCK_THRESHOLD_UNSPECIFIED` | Unspecified harm block threshold.  
`BLOCK_LOW_AND_ABOVE` | Block low threshold and above (i.e. block more).  
`BLOCK_MEDIUM_AND_ABOVE` | Block medium threshold and above.  
`BLOCK_ONLY_HIGH` | Block only high threshold (i.e. block less).  
`BLOCK_NONE` | Block none.  
`OFF` | Turn off the safety filter.  
  
## HarmCategory

Harm category.

Enums  
---  
`HARM_CATEGORY_UNSPECIFIED` | The harm category is unspecified.  
`HARM_CATEGORY_HATE_SPEECH` | The harm category is hate speech.  
`HARM_CATEGORY_DANGEROUS_CONTENT` | The harm category is dangerous content.  
`HARM_CATEGORY_HARASSMENT` | The harm category is harassment.  
`HARM_CATEGORY_SEXUALLY_EXPLICIT` | The harm category is sexually explicit content.  
`HARM_CATEGORY_PROFANITY` | The harm category is profanity.  
`HARM_CATEGORY_TOXIC` | The harm category is toxic.  
  
## SafetySetting

Safety setting.

Fields  
---  
`category` |  `[Guardrail.ModelSafety.HarmCategory](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Guardrail.ModelSafety.HarmCategory)` Required. The harm category.  
`threshold` |  `[Guardrail.ModelSafety.HarmBlockThreshold](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Guardrail.ModelSafety.HarmBlockThreshold)` Required. The harm block threshold.  
  
## Supervisor

Guardrail that runs supervisor intervention.

Fields  
---  
`type` |  `[Guardrail.Supervisor.Type](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Guardrail.Supervisor.Type)` Optional. The type of the supervisor.  
`detection_mode` |  `[Guardrail.Supervisor.DetectionMode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Guardrail.Supervisor.DetectionMode)` Optional. The detection mode of the supervisor.  
  
## DetectionMode

Detection mode of the supervisor.

Enums  
---  
`DETECTION_MODE_UNSPECIFIED` | Detection mode is unspecified. Default to NON_BLOCKING.  
`NON_BLOCKING` | Non blocking detection mode. Response is not blocked when the supervisor detection is ongoing.  
`BLOCKING` | Blocking detection mode. Response is blocked when the supervisor detection is ongoing.  
  
## Type

Type of supervisor.

Enums  
---  
`TYPE_UNSPECIFIED` | Type is unspecified.  
`INVALID_TEXT` | Invalid text issue type.  
`LANGUAGE_SHIFT` | Language shift issue type.  
`SPEAKER_SHIFT` | Speaker shift issue type.  
`AUDIO_MISMATCH` | Audio mismatch issue type.  
`MISSING_TOOL_CALL` | Missing tool call issue type.  
`CUSTOM` | Custom issue type.  
`CHOPPY_AUDIO` | Choppy audio issue type.  
`PROFANITY` | Agent profanity issue type.  
  
## Image

Represents an image input or output in the conversation.

Fields  
---  
`mime_type` |  `string` Required. The IANA standard MIME type of the source data. Supported image types includes: * image/png * image/jpeg * image/webp  
`data` |  `bytes` Required. Raw bytes of the image.  
`alt_text` |  `string` Optional. The alternative text for the image.  
  
## ImportAppRequest

Request message for `[AgentService.ImportApp](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.ImportApp)`.

Fields  
---  
`parent` |  `string` Required. The parent resource name with the location of the app to import.  
`display_name` |  `string` Optional. The display name of the app to import. * If the app is created on import, and the display name is specified, the imported app will use this display name. If a conflict is detected with an existing app, a timestamp will be appended to the display name to make it unique. * If the app is a reimport, this field should not be set. Providing a display name during reimport will result in an INVALID_ARGUMENT error.  
`app_id` |  `string` Optional. The ID to use for the imported app. * If not specified, a unique ID will be automatically assigned for the app. * Otherwise, the imported app will use this ID as the final component of its resource name. If an app with the same ID already exists at the specified location in the project, the content of the existing app will be replaced.  
`import_options` |  `[ImportAppRequest.ImportOptions](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ImportAppRequest.ImportOptions)` Optional. Options governing the import process for the app.  
`ignore_app_lock` |  `bool` Optional. Flag for overriding the app lock during import. If set to true, the import process will ignore the app lock.  
Union field `app`. The app to import. `app` can be only one of the following:  
`gcs_uri` |  `string` The [Google Cloud Storage](https://cloud.google.com/storage/docs/) URI from which to import app. The format of this URI must be `gs://<bucket-name>/<object-name>`.  
`app_content` |  `bytes` Raw bytes representing the compressed zip file with the app folder structure.  
Union field `json_patch`. The JSON patches to apply to the imported app. `json_patch` can be only one of the following:  
`json_patch_content` |  `string` Optional. Patch content as a JSON string.  
`json_patch_gcs_uri` |  `string` Optional. A Cloud Storage URI pointing to a JSON file containing the patches.  
  
## ImportOptions

Configuration options for the app import process. These options control how the import behaves, particularly when conflicts arise with existing app data.

Fields  
---  
`conflict_resolution_strategy` |  `[ImportAppRequest.ImportOptions.ConflictResolutionStrategy](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ImportAppRequest.ImportOptions.ConflictResolutionStrategy)` Optional. The strategy to use when resolving conflicts during import.  
`validate_only` |  `bool` Optional. Flag for dry-running the import process. If set to true, the import process will only perform validations and will not make any changes to the existing app or create a new one.  
  
## ConflictResolutionStrategy

Defines the strategy for handling conflicts when an app with the same ID already exists, or when imported resources (like Agents, Tools, etc.) have the same display names as existing resources within that app.

Enums  
---  
`CONFLICT_RESOLUTION_STRATEGY_UNSPECIFIED` | The conflict resolution strategy is unspecified.  
`REPLACE` | Replace existing data with imported data. If an app with the same `app_id` already exists, its content will be updated based on the imported app. - Resources (App, Agents, Tools, Examples, Guardrails, Toolsets) in the imported app that have the same display name as existing resources will overwrite the existing ones. - Imported resources with new display names will be created. - Existing resources that do not have a matching display name in the imported app will remain untouched.  
`OVERWRITE` | Overwrite existing data with imported data. If an app with the same `app_id` already exists, its content will be overwritten with the imported app. - Existing resources (Agents, Tools, Examples, Guardrails, Toolsets) in the app will be deleted. - Imported resources will be created as new resources.  
  
## ImportAppResponse

Response message for `[AgentService.ImportApp](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.ImportApp)`.

Fields  
---  
`name` |  `string` The resource name of the app that was imported.  
`warnings[]` |  `string` Warning messages generated during the import process. If errors occur for specific resources, they will not be included in the imported app and the error will be mentioned here.  
  
## ImportEvaluationsOperationMetadata

Represents the metadata of the long-running operation for `[EvaluationService.ImportEvaluations](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationService.ImportEvaluations)`.

Fields  
---  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time the operation was created.  
`end_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time the operation finished running.  
`status_message` |  `string` Output only. Human-readable status of the operation, if any.  
  
## ImportEvaluationsRequest

Request message for `[EvaluationService.ImportEvaluations](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationService.ImportEvaluations)`.

Fields  
---  
`parent` |  `string` Required. The app to import the evaluations into. Format: `projects/{project}/locations/{location}/apps/{app}`  
`import_options` |  `[ImportEvaluationsRequest.ImportOptions](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ImportEvaluationsRequest.ImportOptions)` Optional. Options governing the import process for the evaluations.  
Union field `source`. The source of the evaluations to import from. `source` can be only one of the following:  
`conversation_list` |  `[ImportEvaluationsRequest.ConversationList](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ImportEvaluationsRequest.ConversationList)` The conversations to import the evaluations from.  
`gcs_uri` |  `string` The [Google Cloud Storage](https://cloud.google.com/storage/docs/) URI from which to import evaluations. The format of this URI must be `gs://<bucket-name>/<object-name>`.  
`csv_content` |  `bytes` Raw bytes representing the csv file with the evaluations structure.  
  
## ConversationList

A list of conversation resource names.

Fields  
---  
`conversations[]` |  `string` Optional. Conversation resource names.  
  
## ImportOptions

Configuration options for the evaluation import process. These options control how the import behaves, particularly when conflicts arise with existing evaluations data.

Fields  
---  
`conflict_resolution_strategy` |  `[ImportEvaluationsRequest.ImportOptions.ConflictResolutionStrategy](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ImportEvaluationsRequest.ImportOptions.ConflictResolutionStrategy)` Optional. The strategy to use when resolving conflicts during import.  
  
## ConflictResolutionStrategy

Defines the strategy for handling conflicts when an evaluation with the same evaluation ID already exists in the app.

Enums  
---  
`CONFLICT_RESOLUTION_STRATEGY_UNSPECIFIED` | The conflict resolution strategy is unspecified.  
`OVERWRITE` | Overwrite the existing evaluation with the new one.  
`SKIP` | Keep the existing evaluation and skip the new one.  
`DUPLICATE` | Keep the existing evaluation and duplicate the new one as a new evaluation.  
  
## ImportEvaluationsResponse

Response message for `[EvaluationService.ImportEvaluations](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationService.ImportEvaluations)`.

Fields  
---  
`evaluations[]` |  `[Evaluation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Evaluation)` The list of evaluations that were imported into the app.  
`evaluation_results[]` |  `[EvaluationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationResult)` The list of evaluation results that were imported into the app.  
`evaluation_runs[]` |  `[EvaluationRun](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationRun)` The list of evaluation runs that were imported into the app.  
`error_messages[]` |  `string` Optional. A list of error messages associated with evaluations that failed to be imported.  
`import_failure_count` |  `int32` The number of evaluations that either failed to import entirely or completed import with one or more errors.  
`evaluation_result_import_failure_count` |  `int32` The number of evaluation results that either failed to import entirely or completed import with one or more errors.  
`evaluation_run_import_failure_count` |  `int32` The number of evaluation runs that either failed to import entirely or completed import with one or more errors.  
  
## InputAudioConfig

InputAudioConfig configures how the CES agent should interpret the incoming audio data.

Fields  
---  
`audio_encoding` |  `[AudioEncoding](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AudioEncoding)` Required. The encoding of the input audio data.  
`sample_rate_hertz` |  `int32` Required. The sample rate (in Hertz) of the input audio data.  
`noise_suppression_level` |  `string` Optional. Whether to enable noise suppression on the input audio. Available values are "low", "moderate", "high", "very_high".  
  
## InstagramCredentials

Ephemeral Meta credentials for Instagram native integration.

Fields  
---  
`auth_code` |  `string` Required. The Meta auth code provided by the embedded signup flow.  
`conversation_profile_id` |  `string` Optional. The Conversation Profile ID to use for the deployment.  
  
## InterruptionSignal

Indicates the agent's audio response has been interrupted. The client should immediately stop any current audio playback (e.g., due to user barge-in or a new agent response being generated).

Fields  
---  
`barge_in` |  `bool` Whether the interruption is caused by a user barge-in event.  
  
## LanguageSettings

Language settings of the app.

Fields  
---  
`default_language_code` |  `string` Optional. The default language code of the app.  
`supported_language_codes[]` |  `string` Optional. List of languages codes supported by the app, in addition to the `default_language_code`.  
`enable_multilingual_support` |  `bool` Optional. Enables multilingual support. If true, agents in the app will use pre-built instructions to improve handling of multilingual input.  
`fallback_action  
**(deprecated)**` |  `string` This item is deprecated!Optional. Deprecated: This feature is no longer supported. Use `enable_multilingual_support` instead to improve handling of multilingual input. The action to perform when an agent receives input in an unsupported language.This can be a predefined action or a custom tool call. Valid values are: - A tool's full resource name, which triggers a specific tool execution. - A predefined system action, such as "escalate" or "exit", which triggers an `[EndSession](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EndSession)` signal with corresponding `[metadata](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EndSession.FIELDS.google.protobuf.Struct.google.cloud.ces.v1beta.EndSession.metadata)` to terminate the conversation.  
  
## LatencyReport

Latency report for the evaluation run.

Fields  
---  
`tool_latencies[]` |  `[LatencyReport.ToolLatency](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.LatencyReport.ToolLatency)` Output only. Unordered list. Latency metrics for each tool.  
`callback_latencies[]` |  `[LatencyReport.CallbackLatency](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.LatencyReport.CallbackLatency)` Output only. Unordered list. Latency metrics for each callback.  
`guardrail_latencies[]` |  `[LatencyReport.GuardrailLatency](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.LatencyReport.GuardrailLatency)` Output only. Unordered list. Latency metrics for each guardrail.  
`llm_call_latencies[]` |  `[LatencyReport.LlmCallLatency](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.LatencyReport.LlmCallLatency)` Output only. Unordered list. Latency metrics for each LLM call.  
`session_count` |  `int32` Output only. The total number of sessions considered in the latency report.  
  
## CallbackLatency

Latency metrics for a single callback.

Fields  
---  
`stage` |  `string` Output only. The stage of the callback.  
`latency_metrics` |  `[LatencyReport.LatencyMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.LatencyReport.LatencyMetrics)` Output only. The latency metrics for the callback.  
  
## GuardrailLatency

Latency metrics for a single guardrail.

Fields  
---  
`guardrail` |  `string` Output only. The name of the guardrail. Format: `projects/{project}/locations/{location}/apps/{app}/guardrails/{guardrail}`.  
`guardrail_display_name` |  `string` Output only. The display name of the guardrail.  
`latency_metrics` |  `[LatencyReport.LatencyMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.LatencyReport.LatencyMetrics)` Output only. The latency metrics for the guardrail.  
  
## LatencyMetrics

Latency metrics for a component.

Fields  
---  
`p50_latency` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Output only. The 50th percentile latency.  
`p90_latency` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Output only. The 90th percentile latency.  
`p99_latency` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Output only. The 99th percentile latency.  
`call_count` |  `int32` Output only. The number of times the resource was called.  
  
## LlmCallLatency

Latency metrics for a single LLM call.

Fields  
---  
`model` |  `string` Output only. The name of the model.  
`latency_metrics` |  `[LatencyReport.LatencyMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.LatencyReport.LatencyMetrics)` Output only. The latency metrics for the LLM call.  
  
## ToolLatency

Latency metrics for a single tool.

Fields  
---  
`tool_display_name` |  `string` Output only. The display name of the tool.  
`latency_metrics` |  `[LatencyReport.LatencyMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.LatencyReport.LatencyMetrics)` Output only. The latency metrics for the tool.  
Union field `tool_identifier`. The identifier of the tool. `tool_identifier` can be only one of the following:  
`tool` |  `string` Output only. Format: `projects/{project}/locations/{location}/apps/{app}/tools/{tool}`.  
`toolset_tool` |  `[ToolsetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ToolsetTool)` Output only. The toolset tool identifier.  
  
## ListAgentsRequest

Request message for `[AgentService.ListAgents](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.ListAgents)`.

Fields  
---  
`parent` |  `string` Required. The resource name of the app to list agents from.  
`page_size` |  `int32` Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.  
`page_token` |  `string` Optional. The `[next_page_token](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListAgentsResponse.FIELDS.string.google.cloud.ces.v1beta.ListAgentsResponse.next_page_token)` value returned from a previous list `[AgentService.ListAgents](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.ListAgents)` call.  
`filter` |  `string` Optional. Filter to be applied when listing the agents. See <https://google.aip.dev/160> for more details.  
`order_by` |  `string` Optional. Field to sort by. Only "name" and "create_time" is supported. See <https://google.aip.dev/132#ordering> for more details.  
  
## ListAgentsResponse

Response message for `[AgentService.ListAgents](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.ListAgents)`.

Fields  
---  
`agents[]` |  `[Agent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Agent)` The list of agents.  
`next_page_token` |  `string` A token that can be sent as `[ListAgentsRequest.page_token](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListAgentsRequest.FIELDS.string.google.cloud.ces.v1beta.ListAgentsRequest.page_token)` to retrieve the next page. Absence of this field indicates there are no subsequent pages.  
  
## ListAppVersionsRequest

Request message for `[AgentService.ListAppVersions](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.ListAppVersions)`.

Fields  
---  
`parent` |  `string` Required. The resource name of the app to list app versions from.  
`page_size` |  `int32` Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.  
`page_token` |  `string` Optional. The `[next_page_token](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListAppVersionsResponse.FIELDS.string.google.cloud.ces.v1beta.ListAppVersionsResponse.next_page_token)` value returned from a previous list `[AgentService.ListAppVersions](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.ListAppVersions)` call.  
`filter` |  `string` Optional. Filter to be applied when listing the app versions. See <https://google.aip.dev/160> for more details.  
`order_by` |  `string` Optional. Field to sort by. Only "name" and "create_time" is supported. See <https://google.aip.dev/132#ordering> for more details.  
  
## ListAppVersionsResponse

Response message for `[AgentService.ListAppVersions](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.ListAppVersions)`.

Fields  
---  
`app_versions[]` |  `[AppVersion](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AppVersion)` The list of app versions.  
`next_page_token` |  `string` A token that can be sent as `[ListAppVersionsRequest.page_token](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListAppVersionsRequest.FIELDS.string.google.cloud.ces.v1beta.ListAppVersionsRequest.page_token)` to retrieve the next page. Absence of this field indicates there are no subsequent pages.  
  
## ListAppsRequest

Request message for `[AgentService.ListApps](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.ListApps)`.

Fields  
---  
`parent` |  `string` Required. The resource name of the location to list apps from.  
`page_size` |  `int32` Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.  
`page_token` |  `string` Optional. The `[next_page_token](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListAppsResponse.FIELDS.string.google.cloud.ces.v1beta.ListAppsResponse.next_page_token)` value returned from a previous list `[AgentService.ListApps](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.ListApps)` call.  
`filter` |  `string` Optional. Filter to be applied when listing the apps. See <https://google.aip.dev/160> for more details.  
`order_by` |  `string` Optional. Field to sort by. Only "name" and "create_time" is supported. See <https://google.aip.dev/132#ordering> for more details.  
  
## ListAppsResponse

Response message for `[AgentService.ListApps](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.ListApps)`.

Fields  
---  
`apps[]` |  `[App](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.App)` The list of apps.  
`next_page_token` |  `string` A token that can be sent as `[ListAppsRequest.page_token](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListAppsRequest.FIELDS.string.google.cloud.ces.v1beta.ListAppsRequest.page_token)` to retrieve the next page. Absence of this field indicates there are no subsequent pages.  
`unreachable[]` |  `string` Unordered list. Locations that could not be reached.  
  
## ListChangelogsRequest

Request message for `[AgentService.ListChangelogs](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.ListChangelogs)`.

Fields  
---  
`parent` |  `string` Required. The resource name of the app to list changelogs from.  
`page_size` |  `int32` Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.  
`page_token` |  `string` Optional. The `[next_page_token](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListChangelogsResponse.FIELDS.string.google.cloud.ces.v1beta.ListChangelogsResponse.next_page_token)` value returned from a previous list `[AgentService.ListChangelogs](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.ListChangelogs)` call.  
`filter` |  `string` Optional. Filter to be applied when listing the changelogs. See <https://google.aip.dev/160> for more details.The filter string can be used to filter by `action`, `resource_type`, `resource_name`, `author`, and `create_time`. The `:` comparator can be used for case-insensitive partial matching on string fields, while `=` performs an exact case-sensitive match.Examples: * `action:update` (case-insensitive partial match) * `action="Create"` (case-sensitive exact match) * `resource_type:agent` * `resource_name:my-agent` * `author:me@example.com` * `create_time > "2025-01-01T00:00:00Z"` * `create_time <= "2025-01-01T00:00:00Z" AND resource_type:tool`  
`order_by` |  `string` Optional. Field to sort by. Only "name" and "create_time" is supported. See <https://google.aip.dev/132#ordering> for more details.  
  
## ListChangelogsResponse

Response message for `[AgentService.ListChangelogs](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.ListChangelogs)`.

Fields  
---  
`changelogs[]` |  `[Changelog](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Changelog)` The list of changelogs.  
`next_page_token` |  `string` A token that can be sent as `[ListChangelogsRequest.page_token](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListChangelogsRequest.FIELDS.string.google.cloud.ces.v1beta.ListChangelogsRequest.page_token)` to retrieve the next page. Absence of this field indicates there are no subsequent pages.  
  
## ListConversationsRequest

Request message for `[AgentService.ListConversations](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.ListConversations)`.

Fields  
---  
`parent` |  `string` Required. The resource name of the app to list conversations from.  
`page_size` |  `int32` Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.  
`page_token` |  `string` Optional. The `[next_page_token](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListConversationsResponse.FIELDS.string.google.cloud.ces.v1beta.ListConversationsResponse.next_page_token)` value returned from a previous list `[AgentService.ListConversations](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.ListConversations)` call.  
`filter` |  `string` Optional. Filter to be applied when listing the conversations. See <https://google.aip.dev/160> for more details.  
`source` |  `[Conversation.Source](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Conversation.Source)` Optional. Indicate the source of the conversation. If not set, Source.Live will be applied by default. Will be deprecated in favor of `sources` field.  
`sources[]` |  `[Conversation.Source](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Conversation.Source)` Optional. Indicate the sources of the conversations. If not set, all available sources will be applied by default.  
  
## ListConversationsResponse

Response message for `[AgentService.ListConversations](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.ListConversations)`.

Fields  
---  
`conversations[]` |  `[Conversation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Conversation)` The list of conversations.  
`next_page_token` |  `string` A token that can be sent as `[ListConversationsRequest.page_token](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListConversationsRequest.FIELDS.string.google.cloud.ces.v1beta.ListConversationsRequest.page_token)` to retrieve the next page. Absence of this field indicates there are no subsequent pages.  
  
## ListDeploymentsRequest

Request message for `[AgentService.ListDeployments](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.ListDeployments)`.

Fields  
---  
`parent` |  `string` Required. The parent app. Format: `projects/{project}/locations/{location}/apps/{app}`  
`page_size` |  `int32` Optional. The maximum number of deployments to return. The service may return fewer than this value. If unspecified, at most 50 deployments will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`page_token` |  `string` Optional. A page token, received from a previous `ListDeployments` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `ListDeployments` must match the call that provided the page token.  
`order_by` |  `string` Optional. Field to sort by. Only "name" and "create_time" is supported. See <https://google.aip.dev/132#ordering> for more details.  
  
## ListDeploymentsResponse

Response message for `[AgentService.ListDeployments](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.ListDeployments)`.

Fields  
---  
`deployments[]` |  `[Deployment](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Deployment)` The list of deployments.  
`next_page_token` |  `string` A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
## ListEvaluationDatasetsRequest

Request message for `[EvaluationService.ListEvaluationDatasets](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationService.ListEvaluationDatasets)`.

Fields  
---  
`parent` |  `string` Required. The resource name of the app to list evaluation datasets from.  
`page_size` |  `int32` Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.  
`page_token` |  `string` Optional. The `[next_page_token](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListEvaluationDatasetsResponse.FIELDS.string.google.cloud.ces.v1beta.ListEvaluationDatasetsResponse.next_page_token)` value returned from a previous list `[EvaluationService.ListEvaluationDatasets](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationService.ListEvaluationDatasets)` call.  
`filter` |  `string` Optional. Filter to be applied when listing the evaluation datasets. See <https://google.aip.dev/160> for more details.  
`order_by` |  `string` Optional. Field to sort by. Only "name" and "create_time", and "update_time" are supported. Time fields are ordered in descending order, and the name field is ordered in ascending order. If not included, "update_time" will be the default. See <https://google.aip.dev/132#ordering> for more details.  
  
## ListEvaluationDatasetsResponse

Response message for `[EvaluationService.ListEvaluationDatasets](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationService.ListEvaluationDatasets)`.

Fields  
---  
`evaluation_datasets[]` |  `[EvaluationDataset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationDataset)` The list of evaluation datasets.  
`next_page_token` |  `string` A token that can be sent as `[ListEvaluationDatasetsRequest.page_token](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListEvaluationDatasetsRequest.FIELDS.string.google.cloud.ces.v1beta.ListEvaluationDatasetsRequest.page_token)` to retrieve the next page. Absence of this field indicates there are no subsequent pages.  
  
## ListEvaluationExpectationsRequest

Request message for `[EvaluationService.ListEvaluationExpectations](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationService.ListEvaluationExpectations)`.

Fields  
---  
`parent` |  `string` Required. The resource name of the app to list evaluation expectations from.  
`page_size` |  `int32` Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.  
`page_token` |  `string` Optional. The `[next_page_token](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListEvaluationExpectationsResponse.FIELDS.string.google.cloud.ces.v1beta.ListEvaluationExpectationsResponse.next_page_token)` value returned from a previous list `[EvaluationService.ListEvaluationExpectations](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationService.ListEvaluationExpectations)` call.  
`filter` |  `string` Optional. Filter to be applied when listing the evaluation expectations. See <https://google.aip.dev/160> for more details.  
`order_by` |  `string` Optional. Field to sort by. Only "name" and "create_time", and "update_time" are supported. Time fields are ordered in descending order, and the name field is ordered in ascending order. If not included, "update_time" will be the default. See <https://google.aip.dev/132#ordering> for more details.  
  
## ListEvaluationExpectationsResponse

Response message for `[EvaluationService.ListEvaluationExpectations](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationService.ListEvaluationExpectations)`.

Fields  
---  
`evaluation_expectations[]` |  `[EvaluationExpectation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationExpectation)` The list of evaluation expectations.  
`next_page_token` |  `string` A token that can be sent as `[ListEvaluationExpectationsRequest.page_token](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListEvaluationExpectationsRequest.FIELDS.string.google.cloud.ces.v1beta.ListEvaluationExpectationsRequest.page_token)` to retrieve the next page. Absence of this field indicates there are no subsequent pages.  
  
## ListEvaluationResultsRequest

Request message for `[EvaluationService.ListEvaluationResults](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationService.ListEvaluationResults)`.

Fields  
---  
`parent` |  `string` Required. The resource name of the evaluation to list evaluation results from. To filter by evaluation run, use `-` as the evaluation ID and specify the evaluation run ID in the filter. For example: `projects/{project}/locations/{location}/apps/{app}/evaluations/-`  
`page_size` |  `int32` Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.  
`page_token` |  `string` Optional. The `[next_page_token](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListEvaluationResultsResponse.FIELDS.string.google.cloud.ces.v1beta.ListEvaluationResultsResponse.next_page_token)` value returned from a previous list `[EvaluationService.ListEvaluationResults](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationService.ListEvaluationResults)` call.  
`filter` |  `string` Optional. Filter to be applied when listing the evaluation results. See <https://google.aip.dev/160> for more details.  
`order_by` |  `string` Optional. Field to sort by. Only "name" and "create_time", and "update_time" are supported. Time fields are ordered in descending order, and the name field is ordered in ascending order. If not included, "update_time" will be the default. See <https://google.aip.dev/132#ordering> for more details.  
  
## ListEvaluationResultsResponse

Response message for `[EvaluationService.ListEvaluationResults](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationService.ListEvaluationResults)`.

Fields  
---  
`evaluation_results[]` |  `[EvaluationResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationResult)` The list of evaluation results.  
`next_page_token` |  `string` A token that can be sent as `[ListEvaluationResultsRequest.page_token](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListEvaluationResultsRequest.FIELDS.string.google.cloud.ces.v1beta.ListEvaluationResultsRequest.page_token)` to retrieve the next page. Absence of this field indicates there are no subsequent pages.  
  
## ListEvaluationRunsRequest

Request message for `[EvaluationService.ListEvaluationRuns](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationService.ListEvaluationRuns)`.

Fields  
---  
`parent` |  `string` Required. The resource name of the app to list evaluation runs from.  
`page_size` |  `int32` Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.  
`page_token` |  `string` Optional. The `[next_page_token](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListEvaluationRunsResponse.FIELDS.string.google.cloud.ces.v1beta.ListEvaluationRunsResponse.next_page_token)` value returned from a previous list `[EvaluationService.ListEvaluationRuns](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationService.ListEvaluationRuns)` call.  
`filter` |  `string` Optional. Filter to be applied when listing the evaluation runs. See <https://google.aip.dev/160> for more details.  
`order_by` |  `string` Optional. Field to sort by. Only "name" and "create_time", and "update_time" are supported. Time fields are ordered in descending order, and the name field is ordered in ascending order. If not included, "update_time" will be the default. See <https://google.aip.dev/132#ordering> for more details.  
  
## ListEvaluationRunsResponse

Response message for `[EvaluationService.ListEvaluationRuns](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationService.ListEvaluationRuns)`.

Fields  
---  
`evaluation_runs[]` |  `[EvaluationRun](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationRun)` The list of evaluation runs.  
`next_page_token` |  `string` A token that can be sent as `[ListEvaluationRunsRequest.page_token](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListEvaluationRunsRequest.FIELDS.string.google.cloud.ces.v1beta.ListEvaluationRunsRequest.page_token)` to retrieve the next page. Absence of this field indicates there are no subsequent pages.  
  
## ListEvaluationsRequest

Request message for `[EvaluationService.ListEvaluations](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationService.ListEvaluations)`.

Fields  
---  
`parent` |  `string` Required. The resource name of the app to list evaluations from.  
`page_size` |  `int32` Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.  
`page_token` |  `string` Optional. The `[next_page_token](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListEvaluationsResponse.FIELDS.string.google.cloud.ces.v1beta.ListEvaluationsResponse.next_page_token)` value returned from a previous list `[EvaluationService.ListEvaluations](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationService.ListEvaluations)` call.  
`filter  
**(deprecated)**` |  `string` This item is deprecated!Optional. Deprecated: Use evaluation_filter and evaluation_run_filter instead.  
`evaluation_filter` |  `string` Optional. Filter to be applied on the evaluation when listing the evaluations. See <https://google.aip.dev/160> for more details. Supported fields: evaluation_datasets  
`evaluation_run_filter` |  `string` Optional. Filter string for fields on the associated EvaluationRun resources. See <https://google.aip.dev/160> for more details. Supported fields: create_time, initiated_by, app_version_display_name  
`order_by` |  `string` Optional. Field to sort by. Only "name" and "create_time", and "update_time" are supported. Time fields are ordered in descending order, and the name field is ordered in ascending order. If not included, "update_time" will be the default. See <https://google.aip.dev/132#ordering> for more details.  
`last_ten_results` |  `bool` Optional. Whether to include the last 10 evaluation results for each evaluation in the response.  
  
## ListEvaluationsResponse

Response message for `[EvaluationService.ListEvaluations](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationService.ListEvaluations)`.

Fields  
---  
`evaluations[]` |  `[Evaluation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Evaluation)` The list of evaluations.  
`next_page_token` |  `string` A token that can be sent as `[ListEvaluationsRequest.page_token](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListEvaluationsRequest.FIELDS.string.google.cloud.ces.v1beta.ListEvaluationsRequest.page_token)` to retrieve the next page. Absence of this field indicates there are no subsequent pages.  
  
## ListExamplesRequest

Request message for `[AgentService.ListExamples](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.ListExamples)`.

Fields  
---  
`parent` |  `string` Required. The resource name of the app to list examples from.  
`page_size` |  `int32` Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.  
`page_token` |  `string` Optional. The `[next_page_token](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListExamplesResponse.FIELDS.string.google.cloud.ces.v1beta.ListExamplesResponse.next_page_token)` value returned from a previous list `[AgentService.ListExamples](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.ListExamples)` call.  
`filter` |  `string` Optional. Filter to be applied when listing the examples. See <https://google.aip.dev/160> for more details.  
`order_by` |  `string` Optional. Field to sort by. Only "name" and "create_time" is supported. See <https://google.aip.dev/132#ordering> for more details.  
  
## ListExamplesResponse

Response message for `[AgentService.ListExamples](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.ListExamples)`.

Fields  
---  
`examples[]` |  `[Example](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Example)` The list of examples.  
`next_page_token` |  `string` A token that can be sent as `[ListExamplesRequest.page_token](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListExamplesRequest.FIELDS.string.google.cloud.ces.v1beta.ListExamplesRequest.page_token)` to retrieve the next page. Absence of this field indicates there are no subsequent pages.  
  
## ListGuardrailsRequest

Request message for `[AgentService.ListGuardrails](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.ListGuardrails)`.

Fields  
---  
`parent` |  `string` Required. The resource name of the app to list guardrails from.  
`page_size` |  `int32` Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.  
`page_token` |  `string` Optional. The `[next_page_token](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListGuardrailsResponse.FIELDS.string.google.cloud.ces.v1beta.ListGuardrailsResponse.next_page_token)` value returned from a previous list `[AgentService.ListGuardrails](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.ListGuardrails)` call.  
`filter` |  `string` Optional. Filter to be applied when listing the guardrails. See <https://google.aip.dev/160> for more details.  
`order_by` |  `string` Optional. Field to sort by. Only "name" and "create_time" is supported. See <https://google.aip.dev/132#ordering> for more details.  
  
## ListGuardrailsResponse

Response message for `[AgentService.ListGuardrails](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.ListGuardrails)`.

Fields  
---  
`guardrails[]` |  `[Guardrail](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Guardrail)` The list of guardrails.  
`next_page_token` |  `string` A token that can be sent as `[ListGuardrailsRequest.page_token](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListGuardrailsRequest.FIELDS.string.google.cloud.ces.v1beta.ListGuardrailsRequest.page_token)` to retrieve the next page. Absence of this field indicates there are no subsequent pages.  
  
## ListScheduledEvaluationRunsRequest

Request message for `[EvaluationService.ListScheduledEvaluationRuns](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationService.ListScheduledEvaluationRuns)`.

Fields  
---  
`parent` |  `string` Required. The resource name of the app to list scheduled evaluation runs from.  
`page_size` |  `int32` Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.  
`page_token` |  `string` Optional. The `[next_page_token](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListScheduledEvaluationRunsResponse.FIELDS.string.google.cloud.ces.v1beta.ListScheduledEvaluationRunsResponse.next_page_token)` value returned from a previous list `[EvaluationService.ListScheduledEvaluationRuns](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationService.ListScheduledEvaluationRuns)` call.  
`filter` |  `string` Optional. Filter to be applied when listing the scheduled evaluation runs. See <https://google.aip.dev/160> for more details. Currently supports filtering by: * request.evaluations:evaluation_id * request.evaluation_dataset:evaluation_dataset_id  
`order_by` |  `string` Optional. Field to sort by. Supported fields are: "name" (ascending), "create_time" (descending), "update_time" (descending), "next_scheduled_execution" (ascending), and "last_completed_run.create_time" (descending). If not included, "update_time" will be the default. See <https://google.aip.dev/132#ordering> for more details.  
  
## ListScheduledEvaluationRunsResponse

Response message for `[EvaluationService.ListScheduledEvaluationRuns](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationService.ListScheduledEvaluationRuns)`.

Fields  
---  
`scheduled_evaluation_runs[]` |  `[ScheduledEvaluationRun](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ScheduledEvaluationRun)` The list of scheduled evaluation runs.  
`next_page_token` |  `string` A token that can be sent as `[ListScheduledEvaluationRunsRequest.page_token](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListScheduledEvaluationRunsRequest.FIELDS.string.google.cloud.ces.v1beta.ListScheduledEvaluationRunsRequest.page_token)` to retrieve the next page. Absence of this field indicates there are no subsequent pages.  
  
## ListToolsRequest

Request message for `[AgentService.ListTools](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.ListTools)`.

Fields  
---  
`parent` |  `string` Required. The resource name of the app to list tools from.  
`page_size` |  `int32` Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.  
`page_token` |  `string` Optional. The `[next_page_token](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListToolsResponse.FIELDS.string.google.cloud.ces.v1beta.ListToolsResponse.next_page_token)` value returned from a previous list `[AgentService.ListTools](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.ListTools)` call.  
`filter` |  `string` Optional. Filter to be applied when listing the tools. Use "include_system_tools=true" to include system tools in the response. See <https://google.aip.dev/160> for more details.  
`order_by` |  `string` Optional. Field to sort by. Only "name" and "create_time" is supported. See <https://google.aip.dev/132#ordering> for more details.  
  
## ListToolsResponse

Response message for `[AgentService.ListTools](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.ListTools)`.

Fields  
---  
`tools[]` |  `[Tool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Tool)` The list of tools.  
`next_page_token` |  `string` A token that can be sent as `[ListToolsRequest.page_token](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListToolsRequest.FIELDS.string.google.cloud.ces.v1beta.ListToolsRequest.page_token)` to retrieve the next page. Absence of this field indicates there are no subsequent pages.  
  
## ListToolsetsRequest

Request message for `[AgentService.ListToolsets](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.ListToolsets)`.

Fields  
---  
`parent` |  `string` Required. The resource name of the app to list toolsets from.  
`page_size` |  `int32` Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.  
`page_token` |  `string` Optional. The `[next_page_token](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListToolsetsResponse.FIELDS.string.google.cloud.ces.v1beta.ListToolsetsResponse.next_page_token)` value returned from a previous list `[AgentService.ListToolsets](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.ListToolsets)` call.  
`filter` |  `string` Optional. Filter to be applied when listing the toolsets. See <https://google.aip.dev/160> for more details.  
`order_by` |  `string` Optional. Field to sort by. Only "name" and "create_time" is supported. See <https://google.aip.dev/132#ordering> for more details.  
  
## ListToolsetsResponse

Response message for `[AgentService.ListToolsets](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.ListToolsets)`.

Fields  
---  
`toolsets[]` |  `[Toolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Toolset)` The list of toolsets.  
`next_page_token` |  `string` A token that can be sent as `[ListToolsetsRequest.page_token](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ListToolsetsRequest.FIELDS.string.google.cloud.ces.v1beta.ListToolsetsRequest.page_token)` to retrieve the next page. Absence of this field indicates there are no subsequent pages.  
  
## LoggingSettings

Settings to describe the logging behaviors for the app.

Fields  
---  
`redaction_config` |  `[RedactionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.RedactionConfig)` Optional. Configuration for how sensitive data should be redacted.  
`audio_recording_config` |  `[AudioRecordingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AudioRecordingConfig)` Optional. Configuration for how audio interactions should be recorded. The audio is subject to redaction as configured in `[RedactionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.LoggingSettings.FIELDS.google.cloud.ces.v1beta.RedactionConfig.google.cloud.ces.v1beta.LoggingSettings.redaction_config)`.  
`unredacted_audio_recording_config` |  `[AudioRecordingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AudioRecordingConfig)` Optional. Configures an additional recording of unredacted audio. This can be used to maintain a raw audio copy when audio redaction is `[enabled](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.RedactionConfig.FIELDS.bool.google.cloud.ces.v1beta.RedactionConfig.enable_redaction)`, typically for auditing or monitoring purposes.  
`bigquery_export_settings` |  `[BigQueryExportSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.BigQueryExportSettings)` Optional. Configures the BigQuery export behaviors for the app. The conversation data is subject to redaction as configured in `[RedactionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.LoggingSettings.FIELDS.google.cloud.ces.v1beta.RedactionConfig.google.cloud.ces.v1beta.LoggingSettings.redaction_config)`.  
`unredacted_bigquery_export_settings` |  `[BigQueryExportSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.BigQueryExportSettings)` Optional. Configures the BigQuery export behaviors for the app. The unredacted conversation data will be exported to BigQuery tables if it is enabled.  
`cloud_logging_settings` |  `[CloudLoggingSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.CloudLoggingSettings)` Optional. Settings to describe the Cloud Logging behaviors for the app.  
`conversation_logging_settings` |  `[ConversationLoggingSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ConversationLoggingSettings)` Optional. Settings to describe the conversation logging behaviors for the app.  
`evaluation_audio_recording_config` |  `[AudioRecordingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AudioRecordingConfig)` Optional. Configuration for how audio interactions should be recorded for the evaluation. By default, audio recording is not enabled for evaluation sessions.  
`metric_analysis_settings` |  `[MetricAnalysisSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.MetricAnalysisSettings)` Optional. Settings to describe the conversation data collection behaviors for the LLM analysis pipeline for the app.  
  
## McpTool

An MCP tool. See <https://modelcontextprotocol.io/specification/2025-06-18/server/tools> for more details.

Fields  
---  
`name` |  `string` Required. The name of the MCP tool.  
`name_override` |  `string` Optional. The name override of the MCP tool. This is populated if the name was overridden by a Toolset override.  
`description` |  `string` Optional. The description of the MCP tool.  
`input_schema` |  `[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Schema)` Optional. The schema of the input arguments of the MCP tool.  
`output_schema` |  `[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Schema)` Optional. The schema of the output arguments of the MCP tool.  
`server_address` |  `string` Required. The server address of the MCP server, e.g., "https://example.com/mcp/". If the server is built with the MCP SDK, the url should be suffixed with "/mcp/". Only Streamable HTTP transport based servers are supported. This is the same as the server_address in the McpToolset. See <https://modelcontextprotocol.io/specification/2025-03-26/basic/transports#streamable-http> for more details.  
`api_authentication` |  `[ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ApiAuthentication)` Optional. Authentication information required to execute the tool against the MCP server. For bearer token authentication, the token applies only to tool execution, not to listing tools. This requires that tools can be listed without authentication.  
`tls_config` |  `[TlsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.TlsConfig)` Optional. The TLS configuration. Includes the custom server certificates that the client should trust.  
`service_directory_config` |  `[ServiceDirectoryConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ServiceDirectoryConfig)` Optional. Service Directory configuration for VPC-SC, used to resolve service names within a perimeter.  
`custom_headers` |  `map<string, string>` Optional. The custom headers to send in the request to the MCP server. The values must be in the format `$context.variables.<name_of_variable>` and can be set in the session variables. See <https://docs.cloud.google.com/customer-engagement-ai/conversational-agents/ps/tool/open-api#openapi-injection> for more details.  
`state` |  `[McpTool.State](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.McpTool.State)` Output only. The dynamic availability state of the tool on the external server.  
  
## State

Represents the dynamic availability state of the tool.

Enums  
---  
`STATE_UNSPECIFIED` | Default state.  
`ACTIVE` | The tool is available and actively offered by the server.  
`INACTIVE` | The tool is configured or pinned, but currently not offered by the server.  
`STALE` | The tool exists on the server, but does not match the version on the server.  
  
## McpToolDefinition

Container for a tool's core definition elements that are snapshot. Schemas in the snapshot are used as-is and cannot be overridden.

Fields  
---  
`description` |  `string` Output only. The description of the MCP tool. This can be overridden by `description_override` in `McpToolOverride`.  
`input_schema` |  `[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Schema)` Output only. The schema of the input arguments of the MCP tool.  
`output_schema` |  `[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Schema)` Output only. The schema of the output arguments of the MCP tool.  
  
## McpToolOverride

Overrides associated with a given tool in a Toolset. This enables "pinning" or "overriding" of tool definitions from the external dynamic server.

Fields  
---  
`tool` |  `string` Required. The original name of the tool as it is emitted by the MCP server.  
`name_override` |  `string` Optional. If present, this tool uses this name in the Agent instead of the original name. This is primarily used as an alias if the MCP server offers poorly named tools.  
`description_override` |  `string` Optional. If present, this tool uses this description instead of the original description from the server.  
`snapshot` |  `[McpToolDefinition](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.McpToolDefinition)` Output only. If present, this tool is "Pinned" and uses the snapshot values as fallbacks if the server becomes temporarily unavailable or if no Override is present.  
  
## McpToolset

A toolset that contains a list of tools that are offered by the MCP server.

Fields  
---  
`server_address` |  `string` Required. The address of the MCP server, for example, "https://example.com/mcp/". If the server is built with the MCP SDK, the url should be suffixed with "/mcp/". Only Streamable HTTP transport based servers are supported. See <https://modelcontextprotocol.io/specification/2025-03-26/basic/transports#streamable-http> for more details.  
`api_authentication` |  `[ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ApiAuthentication)` Optional. Authentication information required to access tools and execute a tool against the MCP server. For bearer token authentication, the token applies only to tool execution, not to listing tools. This requires that tools can be listed without authentication.  
`service_directory_config` |  `[ServiceDirectoryConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ServiceDirectoryConfig)` Optional. Service Directory configuration for VPC-SC, used to resolve service names within a perimeter.  
`tls_config` |  `[TlsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.TlsConfig)` Optional. The TLS configuration. Includes the custom server certificates that the client should trust.  
`custom_headers` |  `map<string, string>` Optional. The custom headers to send in the request to the MCP server. The values must be in the format `$context.variables.<name_of_variable>` and can be set in the session variables. See <https://docs.cloud.google.com/customer-engagement-ai/conversational-agents/ps/tool/open-api#openapi-injection> for more details.  
`tool_overrides[]` |  `[McpToolOverride](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.McpToolOverride)` Optional. Overrides for individual tools within this toolset. This allows overriding specific details like descriptions, names, or pinning the tools' states so they aren't fully dynamic.  
  
## Message

A message within a conversation.

Fields  
---  
`role` |  `string` Optional. The role within the conversation, e.g., user, agent.  
`chunks[]` |  `[Chunk](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Chunk)` Optional. Content of the message as a series of chunks.  
`event_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Optional. Timestamp when the message was sent or received. Should not be used if the message is part of an `[example](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Example)`.  
  
## MetricAnalysisSettings

Settings to describe the conversation data collection behaviors for LLM analysis metrics pipeline.

Fields  
---  
`llm_metrics_opted_out` |  `bool` Optional. Whether to collect conversation data for llm analysis metrics. If true, conversation data will not be collected for llm analysis metrics; otherwise, conversation data will be collected.  
  
## MockConfig

Mock tool calls configuration for the session.

Fields  
---  
`mocked_tool_calls[]` |  `[MockedToolCall](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.MockedToolCall)` Optional. All tool calls to mock for the duration of the session.  
`unmatched_tool_call_behavior` |  `[MockConfig.UnmatchedToolCallBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.MockConfig.UnmatchedToolCallBehavior)` Required. Beavhior for tool calls that don't match any args patterns in mocked_tool_calls.  
  
## UnmatchedToolCallBehavior

What to do when a tool call doesn't match any mocked tool calls.

Enums  
---  
`UNMATCHED_TOOL_CALL_BEHAVIOR_UNSPECIFIED` | Default value. This value is unused.  
`FAIL` | Throw an error for any tool calls that don't match a mock expected input pattern.  
`PASS_THROUGH` | For unmatched tool calls, pass the tool call through to real tool.  
  
## MockedToolCall

A mocked tool call.

Expresses the target tool + a pattern to match against that tool's args / inputs. If the pattern matches, then the mock response will be returned.

Fields  
---  
`tool  
**(deprecated)**` |  `string` This item is deprecated!Optional. Deprecated. Use tool_identifier instead.  
`expected_args_pattern` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` Required. A pattern to match against the args / inputs of all dispatched tool calls. If the tool call inputs match this pattern, then mock output will be returned.  
`mock_response` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` Optional. The mock response / output to return if the tool call args / inputs match the pattern.  
Union field `tool_identifier`. The identifier of the tool to mock. `tool_identifier` can be only one of the following:  
`tool_id` |  `string` Optional. The name of the tool to mock. Format: `projects/{project}/locations/{location}/apps/{app}/tools/{tool}`  
`toolset` |  `[ToolsetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ToolsetTool)` Optional. The toolset to mock.  
  
## ModelSettings

Model settings contains various configurations for the LLM model.

Fields  
---  
`model` |  `string` Optional. The LLM model that the agent should use. If not set, the agent will inherit the model from its parent agent.  
`thinking_level` |  `[ModelSettings.ThinkingLevel](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ModelSettings.ThinkingLevel)` Optional. The thinking level of the model.  
`temperature` |  `double` Optional. If set, this temperature will be used for the LLM model. Temperature controls the randomness of the model's responses. Lower temperatures produce responses that are more predictable. Higher temperatures produce responses that are more creative.  
  
## ThinkingLevel

Thinking level configuration for the model.

Enums  
---  
`THINKING_LEVEL_UNSPECIFIED` | Thinking level is unspecified.  
`DEFAULT` | Default thinking level.  
`LOW` | Low thinking level.  
`MEDIUM` | Medium thinking level.  
`HIGH` | High thinking level.  
  
## OAuthConfig

Configurations for authentication with OAuth.

Fields  
---  
`oauth_grant_type` |  `[OAuthConfig.OauthGrantType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.OAuthConfig.OauthGrantType)` Required. OAuth grant types.  
`client_id` |  `string` Required. The client ID from the OAuth provider.  
`client_secret_version` |  `string` Required. The name of the SecretManager secret version resource storing the client secret. Format: `projects/{project}/secrets/{secret}/versions/{version}`Note: You should grant `roles/secretmanager.secretAccessor` role to the CES service agent `service-<PROJECT-NUMBER>@gcp-sa-ces.iam.gserviceaccount.com`.  
`token_endpoint` |  `string` Required. The token endpoint in the OAuth provider to exchange for an access token.  
`scopes[]` |  `string` Optional. The OAuth scopes to grant.  
  
## OauthGrantType

OAuth grant types. Only [client credential grant](https://oauth.net/2/grant-types/client-credentials) is supported.

Enums  
---  
`OAUTH_GRANT_TYPE_UNSPECIFIED` | Unspecified. Defaults to CLIENT_CREDENTIAL.  
`CLIENT_CREDENTIAL` | Represents the [client credential flow](https://oauth.net/2/grant-types/client-credentials).  
  
## OpenApiTool

A remote API tool defined by an OpenAPI schema.

Fields  
---  
`open_api_schema` |  `string` Required. The OpenAPI schema in JSON or YAML format.  
`name` |  `string` Optional. The name of the tool. If not provided, the name of the tool will be derived from the OpenAPI schema, from `operation.operationId`.  
`description` |  `string` Optional. The description of the tool. If not provided, the description of the tool will be derived from the OpenAPI schema, from `operation.description` or `operation.summary`.  
`api_authentication` |  `[ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ApiAuthentication)` Optional. Authentication information required by the API.  
`tls_config` |  `[TlsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.TlsConfig)` Optional. The TLS configuration. Includes the custom server certificates that the client will trust.  
`service_directory_config` |  `[ServiceDirectoryConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ServiceDirectoryConfig)` Optional. Service Directory configuration.  
`ignore_unknown_fields` |  `bool` Optional. If true, the agent will ignore unknown fields in the API response.  
`url` |  `string` Optional. The server URL of the Open API schema. This field is only set in tools in the environment dependencies during the export process if the schema contains a server url. During the import process, if this url is present in the environment dependencies and the schema has the $env_var placeholder, it will replace the placeholder in the schema.  
  
## OpenApiToolset

A toolset that contains a list of tools that are defined by an OpenAPI schema.

Fields  
---  
`open_api_schema` |  `string` Required. The OpenAPI schema of the toolset.  
`api_authentication` |  `[ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ApiAuthentication)` Optional. Authentication information required by the API.  
`tls_config` |  `[TlsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.TlsConfig)` Optional. The TLS configuration. Includes the custom server certificates  
`service_directory_config` |  `[ServiceDirectoryConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ServiceDirectoryConfig)` Optional. Service Directory configuration.  
`ignore_unknown_fields` |  `bool` Optional. If true, the agent will ignore unknown fields in the API response for all operations defined in the OpenAPI schema.  
`url` |  `string` Optional. The server URL of the Open API schema. This field is only set in toolsets in the environment dependencies during the export process if the schema contains a server url. During the import process, if this url is present in the environment dependencies and the schema has the $env_var placeholder, it will replace the placeholder in the schema.  
  
## OperationMetadata

Represents the metadata of the long-running operation.

Fields  
---  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time the operation was created.  
`end_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time the operation finished running.  
`status_message` |  `string` Output only. Human-readable status of the operation, if any.  
`requested_cancellation` |  `bool` Output only. Identifies whether the user has requested cancellation of the operation. Operations that have been cancelled successfully have `[google.longrunning.Operation.error](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.longrunning#google.longrunning.Operation.FIELDS.google.rpc.Status.google.longrunning.Operation.error)` value with a `[google.rpc.Status.code](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.rpc#google.rpc.Status.FIELDS.int32.google.rpc.Status.code)` of `1`, corresponding to `Code.CANCELLED`.  
  
## OptimizationConfig

Configuration for running the optimization step after the evaluation run.

Fields  
---  
`generate_loss_report` |  `bool` Optional. Whether to generate a loss report.  
`assistant_session` |  `string` Output only. The assistant session to use for the optimization based on this evaluation run. Format: `projects/{project}/locations/{location}/apps/{app}/assistantSessions/{assistantSession}`  
`report_summary` |  `string` Output only. The summary of the loss report.  
`should_suggest_fix` |  `bool` Output only. Whether to suggest a fix for the losses.  
`status` |  `[OptimizationConfig.OptimizationStatus](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.OptimizationConfig.OptimizationStatus)` Output only. The status of the optimization run.  
`error_message` |  `string` Output only. The error message if the optimization run failed.  
`loss_report` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` Output only. The generated loss report.  
  
## OptimizationStatus

The status of the optimization run.

Enums  
---  
`OPTIMIZATION_STATUS_UNSPECIFIED` | Optimization status is not specified.  
`RUNNING` | Optimization is running.  
`COMPLETED` | Optimization has completed.  
`ERROR` | Optimization failed due to an internal error.  
  
## OutputAudioConfig

OutputAudioConfig configures how the CES agent should synthesize outgoing audio responses.

Fields  
---  
`audio_encoding` |  `[AudioEncoding](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AudioEncoding)` Required. The encoding of the output audio data.  
`sample_rate_hertz` |  `int32` Required. The sample rate (in Hertz) of the output audio data.  
  
## PersonaRunConfig

Configuration for running an evaluation for a specific persona.

Fields  
---  
`persona` |  `string` Optional. The persona to use for the evaluation. Format: `projects/{project}/locations/{location}/apps/{app}/evaluationPersonas/{evaluationPersona}`  
`task_count` |  `int32` Optional. The number of tasks to run for the persona.  
  
## PythonCodeCondition

Python code block to evaluate the condition.

Fields  
---  
`python_code` |  `string` Required. The python code to execute.  
  
## PythonFunction

A Python function tool.

Fields  
---  
`name` |  `string` Optional. The name of the Python function to execute. Must match a Python function name defined in the python code. Case sensitive. If the name is not provided, the first function defined in the python code will be used.  
`python_code` |  `string` Optional. The Python code to execute for the tool.  
`description` |  `string` Output only. The description of the Python function, parsed from the python code's docstring.  
`service_directory_config` |  `[ServiceDirectoryConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ServiceDirectoryConfig)` Optional. Service Directory configuration for the tool.  
  
## QualityReport

The report describing any identified quality issues in the app.

Fields  
---  
`issues[]` |  `[QualityReport.AgentIssues](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.QualityReport.AgentIssues)` Optional. The issues grouped by agent.  
`evaluation_runs[]` |  `string` Optional. A list of evaluation runs used to generate the quality report. Format: `projects/{project}/locations/{location}/evaluationRuns/{evaluationRun}`.  
`general_issues[]` |  `[QualityReport.Issue](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.QualityReport.Issue)` Optional. General issues not specific to any agent.  
  
## AgentIssues

Issues identified for a single agent.

Fields  
---  
`agent` |  `string` Optional. The name of the agent to which the issues are related. Format: `projects/{project}/locations/{location}/apps/{app}/agents/{agent}`  
`issues[]` |  `[QualityReport.Issue](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.QualityReport.Issue)` Optional. List of issues found for this agent.  
  
## Issue

The issue identified.

Fields  
---  
`description` |  `string` Optional. Description of the issue found.  
`occurrence_count` |  `int32` Optional. How many times this issue occurred.  
`proposed_solution` |  `string` Optional. Proposed solution to fix the issue by modifying instructions or tools.  
  
## RecognitionResult

Speech recognition result for the audio input.

Fields  
---  
`transcript` |  `string` Optional. Concatenated user speech segments captured during the current turn.  
  
## RedactionConfig

Configuration to instruct how sensitive data should be handled.

Fields  
---  
`enable_redaction` |  `bool` Optional. If true, redaction will be applied in various logging scenarios, including conversation history, Cloud Logging and audio recording.  
`inspect_template` |  `string` Optional. [DLP](https://cloud.google.com/dlp/docs) inspect template name to configure detection of sensitive data types.Format: `projects/{project}/locations/{location}/inspectTemplates/{inspect_template}`  
`deidentify_template` |  `string` Optional. [DLP](https://cloud.google.com/dlp/docs) deidentify template name to instruct on how to de-identify content.Format: `projects/{project}/locations/{location}/deidentifyTemplates/{deidentify_template}`  
  
## RemoteA2aConfig

Shared configuration for connecting to a remote [A2A](https://github.com/a2aproject/A2A) agent.

Fields  
---  
`api_authentication` |  `[ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ApiAuthentication)` Optional. Authentication configuration for calling the remote agent. Optional if the registry reference already handles authentication.  
`input_variable_mapping` |  `map<string, string>` Optional. Mapping of input variable names of remote agent to GECX variable names.  
`output_variable_mapping` |  `map<string, string>` Optional. Mapping of output variable names of remote agent to GECX variable names.  
`streaming_enabled` |  `bool` Optional. Whether streaming is enabled for the remote agent.  
`context_id` |  `string` Optional. If not empty, interactions with the remote A2A agent will use this context ID. This context_id field can refer to a session variable like `$context.variables.order_agent_session_id`.  
Union field `agent_spec`. Specification of the remote agent. `agent_spec` can be only one of the following:  
`agent_card` |  `[AgentCard](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentCard)` Optional. The full agent card defined inline.  
`agent_registry` |  `string` Optional. Reference to the agent in the Agent Registry. Format: `projects/{project}/locations/{location}/agents/{agent}`  
  
## RemoteAgentTool

Represents a tool that allows the agent to call another remote agent.

Fields  
---  
`name` |  `string` Required. The name of the tool.  
`description` |  `string` Required. The description of the tool.  
`agent_card` |  `[AgentCard](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentCard)` Required. The agent card of the remote agent that this tool invokes.  
`api_authentication` |  `[ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ApiAuthentication)` Optional. Authentication configuration for calling the remote agent.  
`stateful_agent` |  `bool` Optional. When enabled, the interaction between the CXAS app and the remote agent will share the same context. If the remote agent returns a context_id, it will be persisted for the entirety of the session for this remote agent tool.  
`input_variable_mapping` |  `map<string, string>` Optional. Mapping of input variable names of remote agent to GECX variable names.  
`output_variable_mapping` |  `map<string, string>` Optional. Mapping of output variable names of remote agent to GECX variable names.  
  
## RestoreAppVersionRequest

Request message for `[AgentService.RestoreAppVersion](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.RestoreAppVersion)`

Fields  
---  
`name` |  `string` Required. The resource name of the app version to restore.  
  
## RestoreAppVersionResponse

This type has no fields.

Response message for `[AgentService.RestoreAppVersion](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.RestoreAppVersion)`

## RetrieveToolSchemaRequest

Request message for `[ToolService.RetrieveToolSchema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ToolService.RetrieveToolSchema)`.

Fields  
---  
`parent` |  `string` Required. The resource name of the app which the tool/toolset belongs to. Format: `projects/{project}/locations/{location}/apps/{app}`  
Union field `tool_identifier`. The identifier of the tool to retrieve the schema for. It could be either a persisted tool or a tool from a toolset. `tool_identifier` can be only one of the following:  
`tool` |  `string` Optional. The name of the tool to retrieve the schema for. Format: projects/{project}/locations/{location}/apps/{app}/tools/{tool}  
`toolset_tool` |  `[ToolsetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ToolsetTool)` Optional. The toolset tool to retrieve the schema for. Only one tool should match the predicate from the toolset. Otherwise, an error will be returned.  
  
## RetrieveToolSchemaResponse

Response message for `[ToolService.RetrieveToolSchema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ToolService.RetrieveToolSchema)`.

Fields  
---  
`input_schema` |  `[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Schema)` The schema of the tool input parameters.  
`output_schema` |  `[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Schema)` The schema of the tool output parameters.  
Union field `tool_identifier`. The identifier of the tool that the schema is for. `tool_identifier` can be only one of the following:  
`tool` |  `string` The name of the tool that the schema is for. Format: `projects/{project}/locations/{location}/apps/{app}/tools/{tool}`  
`toolset_tool` |  `[ToolsetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ToolsetTool)` The toolset tool that the schema is for.  
  
## RetrieveToolsRequest

Request message for `[ToolService.RetrieveTools](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ToolService.RetrieveTools)`.

Fields  
---  
`toolset` |  `string` Required. The name of the toolset to retrieve the tools for. Format: `projects/{project}/locations/{location}/apps/{app}/toolsets/{toolset}`  
`tool_ids[]` |  `string` Optional. The identifiers of the tools to retrieve from the toolset. If empty, all tools in the toolset will be returned.  
`bypass_persistence_config` |  `bool` Optional. If true, the returned tools will contain raw descriptions and schemas directly from the server, bypassing any stored persistence configurations (overrides/snapshots).  
  
## RetrieveToolsResponse

Response message for `[ToolService.RetrieveTools](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ToolService.RetrieveTools)`.

Fields  
---  
`tools[]` |  `[Tool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Tool)` The list of tools that are included in the specified toolset.  
  
## RunEvaluationOperationMetadata

Operation metadata for `[EvaluationService.RunEvaluation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationService.RunEvaluation)`.

Fields  
---  
`evaluations[]` |  `string` Output only. The list of evaluations that were run. Format: `projects/{project}/locations/{location}/apps/{app}/evaluations/{evaluation}`  
`evaluation_run` |  `string` Output only. The evaluation run that was created. Format: `projects/{project}/locations/{location}/apps/{app}/evaluationRuns/{evaluation_run}`  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time the operation was created.  
`end_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time the operation completed.  
`verb` |  `string` Output only. The verb of the operation.  
`cancel_requested` |  `bool` Output only. Identifies whether the user has requested cancellation of the operation. Operations that have been cancelled successfully have `[google.longrunning.Operation.error](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.longrunning#google.longrunning.Operation.FIELDS.google.rpc.Status.google.longrunning.Operation.error)` value with a `[google.rpc.Status.code](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.rpc#google.rpc.Status.FIELDS.int32.google.rpc.Status.code)` of `1`, corresponding to `Code.CANCELLED`.  
  
## RunEvaluationRequest

Request message for `[EvaluationService.RunEvaluation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationService.RunEvaluation)`.

Fields  
---  
`app` |  `string` Required. The app to evaluate. Format: `projects/{project}/locations/{location}/apps/{app}`  
`evaluations[]` |  `string` Optional. List of evaluations to run. Format: `projects/{project}/locations/{location}/apps/{app}/evaluations/{evaluation}`  
`evaluation_dataset` |  `string` Optional. An evaluation dataset to run. Format: `projects/{project}/locations/{location}/apps/{app}/evaluationDatasets/{evaluationDataset}`  
`display_name` |  `string` Optional. The display name of the evaluation run.  
`app_version` |  `string` Optional. The app version to evaluate. At most one of `app_version` or `deployment` can be set. Format: `projects/{project}/locations/{location}/apps/{app}/versions/{version}`  
`config` |  `[EvaluationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationConfig)` Optional. The configuration to use for the run.  
`persona_run_configs[]` |  `[PersonaRunConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.PersonaRunConfig)` Optional. The configuration to use for the run per persona.  
`optimization_config` |  `[OptimizationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.OptimizationConfig)` Optional. Configuration for running the optimization step after the evaluation run. If not set, the optimization step will not be run.  
`scheduled_evaluation_run` |  `string` Optional. The resource name of the `ScheduledEvaluationRun` that is triggering this evaluation run.If this field is set, the `scheduled_evaluation_run` field on the created `EvaluationRun` resource will be populated from this value. Format: `projects/{project}/locations/{location}/apps/{app}/scheduledEvaluationRuns/{scheduled_evaluation_run}`  
`golden_run_method` |  `[GoldenRunMethod](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GoldenRunMethod)` Optional. The method to run the evaluation if it is a golden evaluation. If not set, default to STABLE.  
`generate_latency_report` |  `bool` Optional. Whether to generate a latency report for the evaluation run.  
`evaluation_run_caching_settings` |  `[EvaluationRunCachingSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationRunCachingSettings)` Optional. The caching settings to use for the evaluation run.  
`run_count` |  `int32` Optional. The number of times to run the evaluation. If not set, the default value is 1 per golden, and 5 per scenario.  
  
## RunEvaluationResponse

Response message for `[EvaluationService.RunEvaluation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationService.RunEvaluation)`.

Fields  
---  
`evaluation_run` |  `string` The name of the evaluation run that was created. Format: `projects/{project}/locations/{location}/apps/{app}/evaluationRuns/{evaluation_run}`  
  
## RunEvaluationResultMetricsOperationMetadata

This type has no fields.

Operation metadata for `[EvaluationService.RunEvaluationResultMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationService.RunEvaluationResultMetrics)`.

## RunEvaluationResultMetricsRequest

Request message for `[EvaluationService.RunEvaluationResultMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationService.RunEvaluationResultMetrics)`.

Fields  
---  
`evaluation_result_id` |  `string` Required. The evaluation result to run metrics for. Format: `projects/{project}/locations/{location}/apps/{app}/evaluations/{evaluation}/results/{evaluation_result_id}`  
  
## RunEvaluationResultMetricsResponse

Response message for `[EvaluationService.RunEvaluationResultMetrics](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationService.RunEvaluationResultMetrics)`.

Fields  
---  
`status` |  `[EvaluationResult.Outcome](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationResult.Outcome)` Output only. The status of the evaluation result metrics calculation.  
  
## RunSessionRequest

Request message for `[SessionService.RunSession](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.SessionService.RunSession)`.

Fields  
---  
`config` |  `[SessionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.SessionConfig)` Required. The configuration for the session.  
`inputs[]` |  `[SessionInput](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.SessionInput)` Required. Inputs for the session.  
  
## RunSessionResponse

Response message for `[SessionService.RunSession](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.SessionService.RunSession)`.

Fields  
---  
`outputs[]` |  `[SessionOutput](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.SessionOutput)` Outputs for the session.  
  
## ScheduledEvaluationRun

Represents a scheduled evaluation run configuration.

Fields  
---  
`name` |  `string` Identifier. The unique identifier of the scheduled evaluation run config. Format: projects/{projectId}/locations/{locationId}/apps/{appId}/scheduledEvaluationRuns/{scheduledEvaluationRunId}  
`display_name` |  `string` Required. User-defined display name of the scheduled evaluation run config.  
`request` |  `[RunEvaluationRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.RunEvaluationRequest)` Required. The RunEvaluationRequest to schedule  
`description` |  `string` Optional. User-defined description of the scheduled evaluation run.  
`scheduling_config` |  `[ScheduledEvaluationRun.SchedulingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ScheduledEvaluationRun.SchedulingConfig)` Required. Configuration for the timing and frequency with which to execute the evaluations.  
`active` |  `bool` Optional. Whether this config is active  
`last_completed_run` |  `string` Output only. The last successful EvaluationRun of this scheduled execution. Format: `projects/{project}/locations/{location}/apps/{app}/evaluationRuns/{evaluationRun}`  
`total_executions` |  `int32` Output only. The total number of times this run has been executed  
`next_scheduled_execution_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The next time this is scheduled to execute  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Timestamp when the scheduled evaluation run was created.  
`created_by` |  `string` Output only. The user who created the scheduled evaluation run.  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Timestamp when the evaluation was last updated.  
`last_updated_by` |  `string` Output only. The user who last updated the evaluation.  
`etag` |  `string` Output only. Etag used to ensure the object hasn't changed during a read-modify-write operation. If the etag is empty, the update will overwrite any concurrent changes.  
  
## SchedulingConfig

Eval scheduling configuration details

Fields  
---  
`frequency` |  `[ScheduledEvaluationRun.SchedulingConfig.Frequency](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ScheduledEvaluationRun.SchedulingConfig.Frequency)` Required. The frequency with which to run the eval  
`start_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Required. Timestamp when the eval should start.  
`days_of_week[]` |  `int32` Optional. The days of the week to run the eval. Applicable only for Weekly and Biweekly frequencies. 1 is Monday, 2 is Tuesday, ..., 7 is Sunday.  
  
## Frequency

The frequencies evals can be run at

Enums  
---  
`FREQUENCY_UNSPECIFIED` | The frequency is unspecified.  
`NONE` | Indicates a one-time scheduled run that should not repeat  
`DAILY` | Run the evaluation daily.  
`WEEKLY` | Run the evaluation weekly.  
`BIWEEKLY` | Run the evaluation biweekly.  
  
## Schema

Represents a select subset of an OpenAPI 3.0 schema object.

Fields  
---  
`type` |  `[Schema.Type](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Schema.Type)` Required. The type of the data.  
`properties` |  `map<string, `[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Schema)`>` Optional. Properties of Type.OBJECT.  
`required[]` |  `string` Optional. Required properties of Type.OBJECT.  
`description` |  `string` Optional. The description of the data.  
`items` |  `[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Schema)` Optional. Schema of the elements of Type.ARRAY.  
`nullable` |  `bool` Optional. Indicates if the value may be null.  
`unique_items` |  `bool` Optional. Indicate the items in the array must be unique. Only applies to TYPE.ARRAY.  
`prefix_items[]` |  `[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Schema)` Optional. Schemas of initial elements of Type.ARRAY.  
`additional_properties` |  `[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Schema)` Optional. Can either be a boolean or an object, controls the presence of additional properties.  
`any_of[]` |  `[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Schema)` Optional. The value should be validated against any (one or more) of the subschemas in the list.  
`enum[]` |  `string` Optional. Possible values of the element of primitive type with enum format. Examples: 1. We can define direction as : {type:STRING, format:enum, enum:["EAST", NORTH", "SOUTH", "WEST"]} 2. We can define apartment number as : {type:INTEGER, format:enum, enum:["101", "201", "301"]}  
`default` |  `[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` Optional. Default value of the data.  
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
`defs` |  `map<string, `[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Schema)`>` Optional. A map of definitions for use by `ref`. Only allowed at the root of the schema.  
`title` |  `string` Optional. The title of the schema.  
`min_items` |  `int64` Optional. Minimum number of the elements for Type.ARRAY.  
`max_items` |  `int64` Optional. Maximum number of the elements for Type.ARRAY.  
`minimum` |  `double` Optional. Minimum value for Type.INTEGER and Type.NUMBER.  
`maximum` |  `double` Optional. Maximum value for Type.INTEGER and Type.NUMBER.  
  
## Type

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
  
## SecuritySettings

Project/Location level security settings for CES.

Fields  
---  
`name` |  `string` Identifier. The unique identifier of the security settings. Format: `projects/{project}/locations/{location}/securitySettings`  
`endpoint_control_policy` |  `[EndpointControlPolicy](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EndpointControlPolicy)` Optional. Endpoint control related settings.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Create time of the security settings.  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Last update time of the security settings.  
`etag` |  `string` Output only. Etag of the security settings.  
  
## ServiceAccountAuthConfig

Configurations for authentication using a custom service account.

Fields  
---  
`service_account` |  `string` Required. The email address of the service account used for authentication. CES uses this service account to exchange an access token and the access token is then sent in the `Authorization` header of the request.The service account must have the `roles/iam.serviceAccountTokenCreator` role granted to the CES service agent `service-<PROJECT-NUMBER>@gcp-sa-ces.iam.gserviceaccount.com`.  
`scopes[]` |  `string` Optional. The OAuth scopes to grant. If not specified, the default scope `https://www.googleapis.com/auth/cloud-platform` is used.  
  
## ServiceAgentIdTokenAuthConfig

This type has no fields.

Configurations for authentication with [ID token](https://cloud.google.com/docs/authentication/token-types#id) generated from service agent.

## ServiceDirectoryConfig

Configuration for tools using Service Directory.

Fields  
---  
`service` |  `string` Required. The name of [Service Directory](https://cloud.google.com/service-directory) service. Format: `projects/{project}/locations/{location}/namespaces/{namespace}/services/{service}`. Location of the service directory must be the same as the location of the app.  
  
## SessionConfig

The configuration for the session.

Fields  
---  
`session` |  `string` Required. The unique identifier of the session. Format: `projects/{project}/locations/{location}/apps/{app}/sessions/{session}`  
`input_audio_config` |  `[InputAudioConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.InputAudioConfig)` Optional. Configuration for processing the input audio.  
`output_audio_config` |  `[OutputAudioConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.OutputAudioConfig)` Optional. Configuration for generating the output audio.  
`historical_contexts[]` |  `[Message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Message)` Optional. The historical context of the session, including user inputs, agent responses, and other messages. Typically, CES agent would manage session automatically so client doesn't need to explicitly populate this field. However, client can optionally override the historical contexts to force the session start from certain state.  
`entry_agent` |  `string` Optional. The entry agent to handle the session. If not specified, the session will be handled by the `[root agent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.App.FIELDS.string.google.cloud.ces.v1beta.App.root_agent)` of the app. Format: `projects/{project}/locations/{location}/apps/{app}/agents/{agent}`  
`deployment` |  `string` Optional. The deployment of the app to use for the session. Format: `projects/{project}/locations/{location}/apps/{app}/deployments/{deployment}`  
`time_zone` |  `string` Optional. The time zone of the user. If provided, the agent will use the time zone for date and time related variables. Otherwise, the agent will use the time zone specified in the App.time_zone_settings.The format is the IANA Time Zone Database time zone, e.g. "America/Los_Angeles".  
`use_tool_fakes` |  `bool` Optional. Whether to use tool fakes for the session. If this field is set, the agent will attempt use tool fakes instead of calling the real tools.  
`remote_dialogflow_query_parameters` |  `[SessionConfig.RemoteDialogflowQueryParameters](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.SessionConfig.RemoteDialogflowQueryParameters)` Optional. [QueryParameters](https://cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#queryparameters) to send to the remote [Dialogflow](https://cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents) agent when the session control is transferred to the remote agent.  
`enable_text_streaming` |  `bool` Optional. Whether to enable streaming text outputs from the model. By default, text outputs from the model are collected before sending to the client. NOTE: This is only supported for text (non-voice) sessions via `[StreamRunSession](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.SessionService.StreamRunSession)` or `[BidiRunSession](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.SessionService.BidiRunSession)`.  
`exclude_diagnostic_info` |  `bool` Optional. Whether to exclude diagnostic info from the session output.  
  
## RemoteDialogflowQueryParameters

[QueryParameters](https://cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#queryparameters) to send to the remote [Dialogflow](https://cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents) agent when the session control is transferred to the remote agent.

Fields  
---  
`webhook_headers` |  `map<string, string>` Optional. The HTTP headers to be sent as webhook_headers in [QueryParameters](https://cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#queryparameters).  
`payload` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` Optional. The payload to be sent in [QueryParameters](https://cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#queryparameters).  
`end_user_metadata` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` Optional. The end user metadata to be sent in [QueryParameters](https://cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#queryparameters).  
  
## SessionInput

Input for the session.

Fields  
---  
`will_continue` |  `bool` Optional. A flag to indicate if the current message is a fragment of a larger input in the bidi streaming session.When set to `true`, the agent defers processing until it receives a subsequent message where `will_continue` is `false`, or until the system detects an endpoint in the audio input.NOTE: This field does not apply to audio and DTMF inputs, as they are always processed automatically based on the endpointing signal.  
Union field `input_type`. The type of the input. `input_type` can be only one of the following:  
`text` |  `string` Optional. Text data from the end user.  
`dtmf` |  `string` Optional. DTMF digits from the end user.  
`audio` |  `bytes` Optional. Audio data from the end user.  
`tool_responses` |  `[ToolResponses](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ToolResponses)` Optional. Execution results for the tool calls from the client.  
`image` |  `[Image](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Image)` Optional. Image data from the end user.  
`blob` |  `[Blob](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Blob)` Optional. Blob data from the end user.  
`variables` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` Optional. Contextual variables for the session, keyed by name. Only variables declared in the app will be used by the CES agent.Unrecognized variables will still be sent to the [Dialogflow agent][Agent.RemoteDialogflowAgent] as additional session parameters.  
`event` |  `[Event](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Event)` Optional. Event input.  
  
## SessionOutput

Output for the session.

Fields  
---  
`turn_index` |  `int32` Indicates the sequential order of conversation turn to which this output belongs to, starting from 1.  
`turn_completed` |  `bool` If true, the CES agent has detected the end of the current conversation turn and will provide no further output for this turn.  
`diagnostic_info` |  `[SessionOutput.DiagnosticInfo](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.SessionOutput.DiagnosticInfo)` Optional. Diagnostic information contains execution details during the processing of the input. Only populated in the last SessionOutput (with `turn_completed=true`) for each turn.  
Union field `output_type`. The type of the output. `output_type` can be only one of the following:  
`text` |  `string` Output text from the CES agent.  
`audio` |  `bytes` Output audio from the CES agent.  
`tool_calls` |  `[ToolCalls](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ToolCalls)` Request for the client to execute the tools.  
`citations` |  `[Citations](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Citations)` Citations that provide the source information for the agent's generated text.  
`google_search_suggestions` |  `[GoogleSearchSuggestions](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GoogleSearchSuggestions)` The suggestions returned from Google Search as a result of invoking the `[GoogleSearchTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GoogleSearchTool)`.  
`end_session` |  `[EndSession](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EndSession)` Indicates the session has ended.  
`payload` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` Custom payload with structured output from the CES agent.  
`image` |  `[Image](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Image)` Output image from the CES agent.  
`progress` |  `string` Intermediate progress update from the CES agent.  
  
## DiagnosticInfo

Contains execution details during the processing.

Fields  
---  
`messages[]` |  `[Message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Message)` List of the messages that happened during the processing.  
`root_span` |  `[Span](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Span)` A trace of the entire request processing, represented as a root span. This span can contain nested child spans for specific operations.  
  
## Span

A span is a unit of work or a single operation during the request processing.

Fields  
---  
`name` |  `string` Output only. The name of the span.  
`start_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The start time of the span.  
`end_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The end time of the span.  
`duration` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Output only. The duration of the span.  
`attributes` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` Output only. Key-value attributes associated with the span.  
`child_spans[]` |  `[Span](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Span)` Output only. The child spans that are nested under this span.  
  
## SynthesizeSpeechConfig

Configuration for how the agent response should be synthesized.

Fields  
---  
`voice` |  `string` Optional. The name of the voice. If not set, the service will choose a voice based on the other parameters such as language_code.For the list of available voices, please refer to [Supported voices and languages](https://cloud.google.com/text-to-speech/docs/voices) from Cloud Text-to-Speech.  
`speaking_rate` |  `double` Optional. The speaking rate/speed in the range [0.25, 2.0]. 1.0 is the normal native speed supported by the specific voice. 2.0 is twice as fast, and 0.5 is half as fast. Values outside of the range [0.25, 2.0] will return an error.  
`model` |  `string` Optional. The model used to synthesize audio. Currently supported values: - "gemini-3.1-flash-tts-preview" If empty, Chirp3-HD is used.  
`instruction` |  `string` Optional. The instruction used to synthesize speech when using a generative model.  
  
## SystemTool

Pre-defined system tool.

Fields  
---  
`name` |  `string` Required. The name of the system tool.  
`description` |  `string` Output only. The description of the system tool.  
  
## TestPersonaVoiceRequest

Request message for `[EvaluationService.TestPersonaVoice](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationService.TestPersonaVoice)`.

Fields  
---  
`app` |  `string` Required. the resource name of the app to test the persona voice for. Format: `projects/{project}/locations/{location}/apps/{app}`  
`persona_id` |  `string` Required. The persona ID to test the voice for. Also accepts "default".  
`text` |  `string` Required. The text to test the voice for.  
  
## TestPersonaVoiceResponse

Response message for `[EvaluationService.TestPersonaVoice](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationService.TestPersonaVoice)`.

Fields  
---  
`audio` |  `bytes` The audio data bytes of the synthesized voice.  
  
## TimeZoneSettings

TimeZone settings of the app.

Fields  
---  
`time_zone` |  `string` Optional. The time zone of the app from the [time zone database](https://www.iana.org/time-zones), e.g., America/Los_Angeles, Europe/Paris.  
  
## TlsConfig

The TLS configuration.

Fields  
---  
`ca_certs[]` |  `[TlsConfig.CaCert](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.TlsConfig.CaCert)` Required. Specifies a list of allowed custom CA certificates for HTTPS verification.  
  
## CaCert

The CA certificate.

Fields  
---  
`display_name` |  `string` Required. The name of the allowed custom CA certificates. This can be used to disambiguate the custom CA certificates.  
`cert` |  `bytes` Required. The allowed custom CA certificates (in DER format) for HTTPS verification. This overrides the default SSL trust store. If this is empty or unspecified, CES will use Google's default trust store to verify certificates. N.B. Make sure the HTTPS server certificates are signed with "subject alt name". For instance a certificate can be self-signed using the following command:
    
    
       openssl x509 -req -days 200 -in example.com.csr \
         -signkey example.com.key \
         -out example.com.crt \
         -extfile <(printf "\nsubjectAltName='DNS:www.example.com'")
      
  
## Tool

A tool represents an action that the CES agent can take to achieve certain goals.

Fields  
---  
`name` |  `string` Identifier. The resource name of the tool. Format:

  * `projects/{project}/locations/{location}/apps/{app}/tools/{tool}` for standalone tools.
  * `projects/{project}/locations/{location}/apps/{app}/toolsets/{toolset}/tools/{tool}` for tools retrieved from a toolset.

These tools are dynamic and output-only; they cannot be referenced directly where a tool is expected.  
`display_name` |  `string` Output only. The display name of the tool, derived based on the tool's type. For example, display name of a [ClientFunction][Tool.ClientFunction] is derived from its `name` property.  
`execution_type` |  `[ExecutionType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ExecutionType)` Optional. The execution type of the tool.  
`timeout` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Optional. The timeout for the tool execution. If not set, the default timeout is 30 seconds for `SYNCHRONOUS` tools and 60 seconds for `ASYNCHRONOUS` tools.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Timestamp when the tool was created.  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Timestamp when the tool was last updated.  
`etag` |  `string` Etag used to ensure the object hasn't changed during a read-modify-write operation. If the etag is empty, the update will overwrite any concurrent changes.  
`generated_summary` |  `string` Output only. If the tool is generated by the LLM assistant, this field contains a descriptive summary of the generation.  
`tool_fake_config` |  `[ToolFakeConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ToolFakeConfig)` Optional. Configuration for tool behavior in fake mode.  
`read_only` |  `bool` Output only. Indicates whether the tool is read-only. If true, the tool cannot be modified by the user.  
Union field `tool_type`. The type of the tool. `tool_type` can be only one of the following:  
`client_function` |  `[ClientFunction](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ClientFunction)` Optional. The client function.  
`open_api_tool` |  `[OpenApiTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.OpenApiTool)` Optional. The open API tool.  
`google_search_tool` |  `[GoogleSearchTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.GoogleSearchTool)` Optional. The google search tool.  
`connector_tool` |  `[ConnectorTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ConnectorTool)` Optional. The Integration Connector tool.  
`data_store_tool` |  `[DataStoreTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.DataStoreTool)` Optional. The data store tool.  
`python_function` |  `[PythonFunction](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.PythonFunction)` Optional. The python function tool.  
`mcp_tool` |  `[McpTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.McpTool)` Optional. The MCP tool. An MCP tool cannot be created or updated directly and is managed by the MCP toolset.  
`file_search_tool` |  `[FileSearchTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.FileSearchTool)` Optional. The file search tool.  
`system_tool` |  `[SystemTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.SystemTool)` Optional. The system tool.  
`agent_tool` |  `[AgentTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentTool)` Optional. The agent tool.  
`widget_tool` |  `[WidgetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.WidgetTool)` Optional. The widget tool.  
`remote_agent_tool` |  `[RemoteAgentTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.RemoteAgentTool)` Optional. The remote agent tool.  
  
## ToolCall

Request for the client or the agent to execute the specified tool.

Fields  
---  
`id` |  `string` Optional. The unique identifier of the tool call. If populated, the client should return the execution result with the matching ID in `[ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ToolResponse.FIELDS.string.google.cloud.ces.v1beta.ToolResponse.id)`.  
`display_name` |  `string` Output only. Display name of the tool.  
`args` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` Optional. The input parameters and values for the tool in JSON object format.  
`parent_tool_call_id` |  `string` Output only. The id of the tool call that caused this one, when it was issued by a sub-agent working on behalf of a parent call. Empty for top-level calls. Lets a client group a sub-agent's work under the call that started it instead of rendering every step as a sibling.  
`agent_name` |  `string` Output only. Human-readable name of the agent that issued this call, e.g. "Contract Architect". Empty when the root agent issued it.  
Union field `tool_identifier`. The identifier of the tool to execute. It could be either a persisted tool or a tool from a toolset. `tool_identifier` can be only one of the following:  
`tool` |  `string` Optional. The name of the tool to execute. Format: `projects/{project}/locations/{location}/apps/{app}/tools/{tool}`  
`toolset_tool` |  `[ToolsetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ToolsetTool)` Optional. The toolset tool to execute.  
  
## ToolCalls

Request for the client to execute the tools and return the execution results before continuing the session.

Fields  
---  
`tool_calls[]` |  `[ToolCall](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ToolCall)` Optional. The list of tool calls to execute.  
  
## ToolFakeConfig

Configuration for tool behavior in fake mode.

Fields  
---  
`enable_fake_mode` |  `bool` Optional. Whether the tool is using fake mode.  
Union field `tool_response`. The response is either static or it is provided by a python function. `tool_response` can be only one of the following:  
`code_block` |  `[CodeBlock](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.CodeBlock)` Optional. Code block which will be executed instead of a real tool call.  
  
## ToolResponse

The execution result of a specific tool from the client or the agent.

Fields  
---  
`id` |  `string` Optional. The matching ID of the `[tool call](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ToolCall)` the response is for.  
`display_name` |  `string` Output only. Display name of the tool.  
`response` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` Required. The tool execution result in JSON object format. Use "output" key to specify tool response and "error" key to specify error details (if any). If "output" and "error" keys are not specified, then whole "response" is treated as tool execution result.  
`parent_tool_call_id` |  `string` Output only. The id of the tool call that caused this one, when it was issued by a sub-agent working on behalf of a parent call. Empty for top-level calls. Lets a client group a sub-agent's work under the call that started it instead of rendering every step as a sibling.  
`agent_name` |  `string` Output only. Human-readable name of the agent that issued this call, e.g. "Contract Architect". Empty when the root agent issued it.  
Union field `tool_identifier`. The identifier of the tool that got executed. It could be either a persisted tool or a tool from a toolset. `tool_identifier` can be only one of the following:  
`tool` |  `string` Optional. The name of the tool to execute. Format: `projects/{project}/locations/{location}/apps/{app}/tools/{tool}`  
`toolset_tool` |  `[ToolsetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ToolsetTool)` Optional. The toolset tool that got executed.  
  
## ToolResponses

Execution results for the requested tool calls from the client.

Fields  
---  
`tool_responses[]` |  `[ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ToolResponse)` Optional. The list of tool execution results.  
  
## Toolset

A toolset represents a group of dynamically managed tools that can be used by the agent.

Fields  
---  
`name` |  `string` Identifier. The unique identifier of the toolset. Format: `projects/{project}/locations/{location}/apps/{app}/toolsets/{toolset}`  
`display_name` |  `string` Optional. The display name of the toolset. Must be unique within the same app.  
`description` |  `string` Optional. The description of the toolset.  
`timeout` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Optional. The timeout for the toolset execution. If not set, the default timeout is 30 seconds for `SYNCHRONOUS` toolsets and 60 seconds for `ASYNCHRONOUS` toolsets.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Timestamp when the toolset was created.  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Timestamp when the toolset was last updated.  
`etag` |  `string` ETag used to ensure the object hasn't changed during a read-modify-write operation. If the etag is empty, the update will overwrite any concurrent changes.  
`execution_type` |  `[ExecutionType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ExecutionType)` Optional. The execution type of the tools in the toolset.  
`tool_fake_config` |  `[ToolFakeConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ToolFakeConfig)` Optional. Configuration for tools behavior in fake mode.  
Union field `toolset_type`. The type of the toolset. `toolset_type` can be only one of the following:  
`mcp_toolset` |  `[McpToolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.McpToolset)` Optional. A toolset that contains a list of tools that are offered by the MCP server.  
`open_api_toolset` |  `[OpenApiToolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.OpenApiToolset)` Optional. A toolset that contains a list of tools that are defined by an OpenAPI schema.  
`connector_toolset` |  `[ConnectorToolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ConnectorToolset)` Optional. A toolset that generates tools from an Integration Connectors Connection.  
  
## ToolsetTool

A tool that is created from a toolset.

Fields  
---  
`toolset` |  `string` Required. The resource name of the Toolset from which this tool is derived. Format: `projects/{project}/locations/{location}/apps/{app}/toolsets/{toolset}`  
`tool_id` |  `string` Optional. The tool ID to filter the tools to retrieve the schema for.  
  
## TransferRule

Rule for transferring to a specific agent.

Fields  
---  
`child_agent` |  `string` Required. The resource name of the child agent the rule applies to. Format: `projects/{project}/locations/{location}/apps/{app}/agents/{agent}`  
`direction` |  `[TransferRule.Direction](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.TransferRule.Direction)` Required. The direction of the transfer.  
Union field `rule_type`. The rule type. `rule_type` can be only one of the following:  
`deterministic_transfer` |  `[TransferRule.DeterministicTransfer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.TransferRule.DeterministicTransfer)` Optional. A rule that immediately transfers to the target agent when the condition is met.  
`disable_planner_transfer` |  `[TransferRule.DisablePlannerTransfer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.TransferRule.DisablePlannerTransfer)` Optional. Rule that prevents the planner from transferring to the target agent.  
  
## DeterministicTransfer

Deterministic transfer rule. When the condition evaluates to true, the transfer occurs.

Fields  
---  
Union field `condition_type`. The condition to evaluate. `condition_type` can be only one of the following:  
`expression_condition` |  `[ExpressionCondition](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ExpressionCondition)` Optional. A rule that evaluates a session state condition. If the condition evaluates to true, the transfer occurs.  
`python_code_condition` |  `[PythonCodeCondition](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.PythonCodeCondition)` Optional. A rule that uses Python code block to evaluate the conditions. If the condition evaluates to true, the transfer occurs.  
  
## Direction

The direction of the transfer.

Enums  
---  
`DIRECTION_UNSPECIFIED` | Unspecified direction.  
`PARENT_TO_CHILD` | Transfer from the parent agent to the child agent.  
`CHILD_TO_PARENT` | Transfer from the child agent to the parent agent.  
  
## DisablePlannerTransfer

A rule that prevents the planner from transferring to the target agent.

Fields  
---  
`expression_condition` |  `[ExpressionCondition](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ExpressionCondition)` Required. If the condition evaluates to true, planner will not be allowed to transfer to the target agent.  
  
## TriggerAction

Action that is taken when a certain precondition is met.

Fields  
---  
Union field `action`. The action to take. `action` can be only one of the following:  
`respond_immediately` |  `[TriggerAction.RespondImmediately](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.TriggerAction.RespondImmediately)` Optional. Immediately respond with a preconfigured response.  
`transfer_agent` |  `[TriggerAction.TransferAgent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.TriggerAction.TransferAgent)` Optional. Transfer the conversation to a different agent.  
`generative_answer` |  `[TriggerAction.GenerativeAnswer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.TriggerAction.GenerativeAnswer)` Optional. Respond with a generative answer.  
  
## GenerativeAnswer

The agent will immediately respond with a generative answer.

Fields  
---  
`prompt` |  `string` Required. The prompt to use for the generative answer.  
  
## RespondImmediately

The agent will immediately respond with a preconfigured response.

Fields  
---  
`responses[]` |  `[TriggerAction.Response](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.TriggerAction.Response)` Required. The canned responses for the agent to choose from. The response is chosen randomly.  
  
## Response

Represents a response from the agent.

Fields  
---  
`text` |  `string` Required. Text for the agent to respond with.  
`disabled` |  `bool` Optional. Whether the response is disabled. Disabled responses are not used by the agent.  
  
## TransferAgent

The agent will transfer the conversation to a different agent.

Fields  
---  
`agent` |  `string` Required. The name of the agent to transfer the conversation to. The agent must be in the same app as the current agent. Format: `projects/{project}/locations/{location}/apps/{app}/agents/{agent}`  
  
## UpdateAgentRequest

Request message for `[AgentService.UpdateAgent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.UpdateAgent)`.

Fields  
---  
`agent` |  `[Agent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Agent)` Required. The agent to update.  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Optional. Field mask is used to control which fields get updated. If the mask is not present, all fields will be updated.  
  
## UpdateAppRequest

Request message for `[AgentService.UpdateApp](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.UpdateApp)`.

Fields  
---  
`app` |  `[App](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.App)` Required. The app to update.  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Optional. Field mask is used to control which fields get updated. If the mask is not present, all fields will be updated.  
  
## UpdateAppVersionRequest

Request message for `[AgentService.UpdateAppVersion](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.UpdateAppVersion)`.

Fields  
---  
`app_version` |  `[AppVersion](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AppVersion)` Required. The app version to update.  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Optional. The list of fields to update. If empty, fields `display_name` and `description` will be updated.  
  
## UpdateDeploymentRequest

Request message for `[AgentService.UpdateDeployment](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.UpdateDeployment)`.

Fields  
---  
`deployment` |  `[Deployment](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Deployment)` Required. The deployment to update.  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Optional. The list of fields to update.  
  
## UpdateEvaluationDatasetRequest

Request message for `[EvaluationService.UpdateEvaluationDataset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationService.UpdateEvaluationDataset)`.

Fields  
---  
`evaluation_dataset` |  `[EvaluationDataset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationDataset)` Required. The evaluation dataset to update.  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Optional. Field mask is used to control which fields get updated. If the mask is not present, all fields will be updated.  
  
## UpdateEvaluationExpectationRequest

Request message for `[EvaluationService.UpdateEvaluationExpectation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationService.UpdateEvaluationExpectation)`.

Fields  
---  
`evaluation_expectation` |  `[EvaluationExpectation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationExpectation)` Required. The evaluation expectation to update.  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Optional. Field mask is used to control which fields get updated. If the mask is not present, all fields will be updated.  
  
## UpdateEvaluationRequest

Request message for `[EvaluationService.UpdateEvaluation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationService.UpdateEvaluation)`.

Fields  
---  
`evaluation` |  `[Evaluation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Evaluation)` Required. The evaluation to update.  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Optional. Field mask is used to control which fields get updated. If the mask is not present, all fields will be updated.  
  
## UpdateExampleRequest

Request message for `[AgentService.UpdateExample](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.UpdateExample)`.

Fields  
---  
`example` |  `[Example](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Example)` Required. The example to update.  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Optional. Field mask is used to control which fields get updated. If the mask is not present, all fields will be updated.  
  
## UpdateGuardrailRequest

Request message for `[AgentService.UpdateGuardrail](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.UpdateGuardrail)`.

Fields  
---  
`guardrail` |  `[Guardrail](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Guardrail)` Required. The guardrail to update.  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Optional. Field mask is used to control which fields get updated. If the mask is not present, all fields will be updated.  
  
## UpdateScheduledEvaluationRunRequest

Request message for `[EvaluationService.UpdateScheduledEvaluationRun](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationService.UpdateScheduledEvaluationRun)`.

Fields  
---  
`scheduled_evaluation_run` |  `[ScheduledEvaluationRun](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.ScheduledEvaluationRun)` Required. The scheduled evaluation run to update.  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Optional. Field mask is used to control which fields get updated. If the mask is not present, all fields will be updated.  
  
## UpdateSecuritySettingsRequest

Request message for `[AgentService.UpdateSecuritySettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.UpdateSecuritySettings)`.

Fields  
---  
`security_settings` |  `[SecuritySettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.SecuritySettings)` Required. The security settings to update.  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Optional. Field mask is used to control which fields get updated. If the mask is not present, all fields will be updated.  
  
## UpdateToolRequest

Request message for `[AgentService.UpdateTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.UpdateTool)`.

Fields  
---  
`tool` |  `[Tool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Tool)` Required. The tool to update.  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Optional. Field mask is used to control which fields get updated. If the mask is not present, all fields will be updated.  
  
## UpdateToolsetRequest

Request message for `[AgentService.UpdateToolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.AgentService.UpdateToolset)`.

Fields  
---  
`toolset` |  `[Toolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Toolset)` Required. The toolset to update.  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Optional. Field mask is used to control which fields get updated. If the mask is not present, all fields will be updated.  
  
## UploadEvaluationAudioRequest

Request message for `[EvaluationService.UploadEvaluationAudio](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationService.UploadEvaluationAudio)`.

Fields  
---  
`name` |  `string` Required. The resource name of the Evaluation for which to upload the evaluation audio. Format: `projects/{project}/locations/{location}/apps/{app}/evaluations/{evaluation}`  
`audio_content` |  `bytes` Required. The raw audio bytes. The format of the audio must be single-channel LINEAR16 with a sample rate of 16kHz (default InputAudioConfig).  
`previous_audio_gcs_uri` |  `string` Optional. The Google Cloud Storage URI of the previously uploaded audio file to be deleted. Format: `gs://<bucket-name>/<object-name>`  
  
## UploadEvaluationAudioResponse

Response message for `[EvaluationService.UploadEvaluationAudio](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.EvaluationService.UploadEvaluationAudio)`.

Fields  
---  
`audio_gcs_uri` |  `string` The Google Cloud Storage URI where the uploaded audio file is stored. Format: `gs://<bucket-name>/<object-name>`  
`transcript` |  `string` The transcript of the audio, generated by Cloud Speech-to-Text.  
`duration` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` The duration of the audio.  
  
## VpcScSettings

VPC-SC settings for the app.

Fields  
---  
`allowed_origins[]` |  `string` Optional. The allowed HTTP(s) origins that OpenAPI tools in the App are able to directly call when VPC Service Controls are enabled. These strings must match the origin exactly, including the port if specified. For example, "https://example.com" or "https://example.com:443". This list does not yet apply to Python tools that may make direct HTTP calls.  
  
## WebSearchQuery

Represents a single web search query and its associated search uri.

Fields  
---  
`query` |  `string` The search query text.  
`uri` |  `string` The URI to the Google Search results page for the query.  
  
## WhatsAppCredentials

Ephemeral Meta credentials for WhatsApp native integration.

Fields  
---  
`auth_code` |  `string` Required. The Meta auth code provided by the embedded signup flow.  
`pin` |  `string` Required. The 6-digit PIN created by the user for two-step verification.  
`phone_number` |  `string` Required. The phone number to register with WhatsApp.  
`business_account_id` |  `string` Required. The Business Account ID to use for the phone number.  
`waba_id` |  `string` Required. The WhatsApp Business Account ID.  
`conversation_profile_id` |  `string` Optional. The Conversation Profile ID to use for the deployment.  
  
## WidgetTool

Represents a widget tool that the agent can invoke. When the tool is chosen by the agent, agent will return the widget to the client. The client is responsible for processing the widget and generating the next user query to continue the interaction with the agent.

Fields  
---  
`name` |  `string` Required. The display name of the widget tool.  
`description` |  `string` Optional. The description of the widget tool.  
`widget_type` |  `[WidgetTool.WidgetType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.WidgetTool.WidgetType)` Optional. The type of the widget tool. If not specified, the default type will be CUSTOMIZED.  
`ui_config` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` Optional. Configuration for rendering the widget.  
`data_mapping` |  `[WidgetTool.DataMapping](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.WidgetTool.DataMapping)` Optional. The mapping that defines how data from a source tool is mapped to the widget's input parameters.  
`text_response_config` |  `[WidgetTool.TextResponseConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.WidgetTool.TextResponseConfig)` Optional. Configuration for always-included text responses.  
Union field `input`. The input of the widget tool. `input` can be only one of the following:  
`parameters` |  `[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.Schema)` Optional. The input parameters of the widget tool.  
  
## DataMapping

Configuration for mapping data from a source tool to the widget's input parameters.

Fields  
---  
`source_tool_name` |  `string` Optional. The resource name of the tool that provides the data for the widget (e.g., a search tool or a custom function). Format: `projects/{project}/locations/{location}/agents/{agent}/tools/{tool}`  
`field_mappings` |  `map<string, string>` Optional. A map of widget input parameter fields to the corresponding output fields of the source tool.  
`python_function` |  `[PythonFunction](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.PythonFunction)` Optional. Configuration for a Python function used to transform the source tool's output into the widget's input format.  
`mode` |  `[WidgetTool.DataMapping.Mode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.WidgetTool.DataMapping.Mode)` Optional. The mode of the data mapping.  
`python_script  
**(deprecated)**` |  `string` This item is deprecated!Deprecated: Use `python_function` instead.  
  
## Mode

The strategy used to map data from the source tool to the widget.

Enums  
---  
`MODE_UNSPECIFIED` | Unspecified mode.  
`FIELD_MAPPING` | Use the `field_mappings` map for data transformation.  
`PYTHON_SCRIPT` | Use the `python_script` for data transformation.  
  
## TextResponseConfig

Configuration for the text response returned with the widget.

Fields  
---  
`type` |  `[WidgetTool.TextResponseConfig.Type](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1beta#google.cloud.ces.v1beta.WidgetTool.TextResponseConfig.Type)` Optional. The strategy for providing the text response.  
`static_text` |  `string` Optional. The static text response to return when type is STATIC.  
`text_response_instruction` |  `string` Optional. Instruction for the LLM on how to generate the text response. Used as the description for the text response parameter if type is LLM_GENERATED.  
  
## Type

Defines how the text response is produced.

Enums  
---  
`TYPE_UNSPECIFIED` | Unspecified type.  
`NONE` | The LLM dynamically decides whether to generate a text response alongside the widget based on the conversation context.  
`LLM_GENERATED` | The LLM is explicitly required to generate a text response.  
`STATIC` | A pre-defined static text response is always used.  
  
## WidgetType

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
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
