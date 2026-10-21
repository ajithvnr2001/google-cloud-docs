---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1
title: Package google.cloud.ces.v1 \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:19:12.125279+00:00
---

# Package google.cloud.ces.v1  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Package google.cloud.ces.v1 Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[AgentService](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService)` (interface)
  * `[SessionService](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.SessionService)` (interface)
  * `[ToolService](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ToolService)` (interface)
  * `[WidgetService](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.WidgetService)` (interface)
  * `[Action](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Action)` (message)
  * `[Action.EntityOperation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Action.EntityOperation)` (message)
  * `[Action.EntityOperation.OperationType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Action.EntityOperation.OperationType)` (enum)
  * `[Agent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Agent)` (message)
  * `[Agent.AgentToolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Agent.AgentToolset)` (message)
  * `[Agent.LlmAgent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Agent.LlmAgent)` (message)
  * `[Agent.RemoteA2aAgent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Agent.RemoteA2aAgent)` (message)
  * `[Agent.RemoteDialogflowAgent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Agent.RemoteDialogflowAgent)` (message)
  * `[AgentCard](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentCard)` (message)
  * `[AgentInterface](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentInterface)` (message)
  * `[AgentRegistryDeployment](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentRegistryDeployment)` (message)
  * `[AgentSkill](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentSkill)` (message)
  * `[AgentTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentTool)` (message)
  * `[AgentTransfer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentTransfer)` (message)
  * `[AmbientSoundConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AmbientSoundConfig)` (message)
  * `[AmbientSoundConfig.PrebuiltAmbientNoise](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AmbientSoundConfig.PrebuiltAmbientNoise)` (enum)
  * `[ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ApiAuthentication)` (message)
  * `[ApiKeyConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ApiKeyConfig)` (message)
  * `[ApiKeyConfig.RequestLocation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ApiKeyConfig.RequestLocation)` (enum)
  * `[App](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.App)` (message)
  * `[App.ToolExecutionMode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.App.ToolExecutionMode)` (enum)
  * `[App.VariableDeclaration](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.App.VariableDeclaration)` (message)
  * `[AppSnapshot](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AppSnapshot)` (message)
  * `[AppVersion](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AppVersion)` (message)
  * `[AudioEncoding](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AudioEncoding)` (enum)
  * `[AudioProcessingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AudioProcessingConfig)` (message)
  * `[AudioRecordingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AudioRecordingConfig)` (message)
  * `[BargeInConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.BargeInConfig)` (message)
  * `[BatchDeleteConversationsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.BatchDeleteConversationsRequest)` (message)
  * `[BatchDeleteConversationsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.BatchDeleteConversationsResponse)` (message)
  * `[BearerTokenConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.BearerTokenConfig)` (message)
  * `[BidiSessionClientMessage](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.BidiSessionClientMessage)` (message)
  * `[BidiSessionServerMessage](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.BidiSessionServerMessage)` (message)
  * `[BigQueryExportSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.BigQueryExportSettings)` (message)
  * `[Blob](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Blob)` (message)
  * `[Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Callback)` (message)
  * `[Changelog](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Changelog)` (message)
  * `[ChannelProfile](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ChannelProfile)` (message)
  * `[ChannelProfile.ChannelType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ChannelProfile.ChannelType)` (enum)
  * `[ChannelProfile.InstagramConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ChannelProfile.InstagramConfig)` (message)
  * `[ChannelProfile.PersonaProperty](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ChannelProfile.PersonaProperty)` (message)
  * `[ChannelProfile.PersonaProperty.Persona](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ChannelProfile.PersonaProperty.Persona)` (enum)
  * `[ChannelProfile.WebWidgetConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ChannelProfile.WebWidgetConfig)` (message)
  * `[ChannelProfile.WebWidgetConfig.Modality](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ChannelProfile.WebWidgetConfig.Modality)` (enum)
  * `[ChannelProfile.WebWidgetConfig.SecuritySettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ChannelProfile.WebWidgetConfig.SecuritySettings)` (message)
  * `[ChannelProfile.WebWidgetConfig.Theme](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ChannelProfile.WebWidgetConfig.Theme)` (enum)
  * `[ChannelProfile.WhatsAppConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ChannelProfile.WhatsAppConfig)` (message)
  * `[Chunk](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Chunk)` (message)
  * `[Citations](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Citations)` (message)
  * `[Citations.CitedChunk](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Citations.CitedChunk)` (message)
  * `[Citations.InlineCitation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Citations.InlineCitation)` (message)
  * `[ClientCertificateSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ClientCertificateSettings)` (message)
  * `[ClientFunction](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ClientFunction)` (message)
  * `[CloudLoggingSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.CloudLoggingSettings)` (message)
  * `[CodeBlock](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.CodeBlock)` (message)
  * `[ConnectorTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ConnectorTool)` (message)
  * `[ConnectorToolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ConnectorToolset)` (message)
  * `[Conversation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Conversation)` (message)
  * `[Conversation.ChannelType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Conversation.ChannelType)` (enum)
  * `[Conversation.InputType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Conversation.InputType)` (enum)
  * `[Conversation.Source](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Conversation.Source)` (enum)
  * `[Conversation.Turn](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Conversation.Turn)` (message)
  * `[ConversationLoggingSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ConversationLoggingSettings)` (message)
  * `[CreateAgentRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.CreateAgentRequest)` (message)
  * `[CreateAppRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.CreateAppRequest)` (message)
  * `[CreateAppVersionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.CreateAppVersionRequest)` (message)
  * `[CreateDeploymentRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.CreateDeploymentRequest)` (message)
  * `[CreateExampleRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.CreateExampleRequest)` (message)
  * `[CreateGuardrailRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.CreateGuardrailRequest)` (message)
  * `[CreateToolRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.CreateToolRequest)` (message)
  * `[CreateToolsetRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.CreateToolsetRequest)` (message)
  * `[CustomVoiceSample](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.CustomVoiceSample)` (message)
  * `[CustomVoiceSample.VoiceInstructionMode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.CustomVoiceSample.VoiceInstructionMode)` (enum)
  * `[CustomVoiceSample.Warning](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.CustomVoiceSample.Warning)` (message)
  * `[CustomVoiceSample.Warning.WarningType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.CustomVoiceSample.Warning.WarningType)` (enum)
  * `[DashboardSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DashboardSettings)` (message)
  * `[DataStore](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DataStore)` (message)
  * `[DataStore.ConnectorConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DataStore.ConnectorConfig)` (message)
  * `[DataStore.DataStoreType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DataStore.DataStoreType)` (enum)
  * `[DataStore.DocumentProcessingMode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DataStore.DocumentProcessingMode)` (enum)
  * `[DataStoreSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DataStoreSettings)` (message)
  * `[DataStoreSettings.Engine](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DataStoreSettings.Engine)` (message)
  * `[DataStoreSettings.Engine.Type](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DataStoreSettings.Engine.Type)` (enum)
  * `[DataStoreTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DataStoreTool)` (message)
  * `[DataStoreTool.BoostSpec](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DataStoreTool.BoostSpec)` (message)
  * `[DataStoreTool.BoostSpec.ConditionBoostSpec](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DataStoreTool.BoostSpec.ConditionBoostSpec)` (message)
  * `[DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec)` (message)
  * `[DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec.AttributeType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec.AttributeType)` (enum)
  * `[DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec.ControlPoint](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec.ControlPoint)` (message)
  * `[DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec.InterpolationType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec.InterpolationType)` (enum)
  * `[DataStoreTool.BoostSpecs](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DataStoreTool.BoostSpecs)` (message)
  * `[DataStoreTool.DataStoreSource](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DataStoreTool.DataStoreSource)` (message)
  * `[DataStoreTool.EngineSource](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DataStoreTool.EngineSource)` (message)
  * `[DataStoreTool.FilterParameterBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DataStoreTool.FilterParameterBehavior)` (enum)
  * `[DataStoreTool.GroundingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DataStoreTool.GroundingConfig)` (message)
  * `[DataStoreTool.ModalityConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DataStoreTool.ModalityConfig)` (message)
  * `[DataStoreTool.ModalityConfig.ModalityType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DataStoreTool.ModalityConfig.ModalityType)` (enum)
  * `[DataStoreTool.RewriterConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DataStoreTool.RewriterConfig)` (message)
  * `[DataStoreTool.SnippetsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DataStoreTool.SnippetsConfig)` (message)
  * `[DataStoreTool.SummarizationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DataStoreTool.SummarizationConfig)` (message)
  * `[DeleteAgentRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DeleteAgentRequest)` (message)
  * `[DeleteAppRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DeleteAppRequest)` (message)
  * `[DeleteAppVersionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DeleteAppVersionRequest)` (message)
  * `[DeleteConversationRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DeleteConversationRequest)` (message)
  * `[DeleteDeploymentRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DeleteDeploymentRequest)` (message)
  * `[DeleteExampleRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DeleteExampleRequest)` (message)
  * `[DeleteGuardrailRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DeleteGuardrailRequest)` (message)
  * `[DeleteToolRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DeleteToolRequest)` (message)
  * `[DeleteToolsetRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DeleteToolsetRequest)` (message)
  * `[DeployChannelResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DeployChannelResponse)` (message)
  * `[Deployment](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Deployment)` (message)
  * `[Deployment.Modality](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Deployment.Modality)` (enum)
  * `[EndSession](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.EndSession)` (message)
  * `[EndUserAuthConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.EndUserAuthConfig)` (message)
  * `[EndUserAuthConfig.Oauth2AuthCodeConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.EndUserAuthConfig.Oauth2AuthCodeConfig)` (message)
  * `[EndUserAuthConfig.Oauth2JwtBearerConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.EndUserAuthConfig.Oauth2JwtBearerConfig)` (message)
  * `[EndpointControlPolicy](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.EndpointControlPolicy)` (message)
  * `[EndpointControlPolicy.EnforcementScope](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.EndpointControlPolicy.EnforcementScope)` (enum)
  * `[ErrorHandlingSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ErrorHandlingSettings)` (message)
  * `[ErrorHandlingSettings.EndSessionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ErrorHandlingSettings.EndSessionConfig)` (message)
  * `[ErrorHandlingSettings.ErrorHandlingStrategy](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ErrorHandlingSettings.ErrorHandlingStrategy)` (enum)
  * `[ErrorHandlingSettings.FallbackResponseConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ErrorHandlingSettings.FallbackResponseConfig)` (message)
  * `[EvaluationMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.EvaluationMetricsThresholds)` (message)
  * `[EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds)` (message)
  * `[EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.ExpectationLevelMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.ExpectationLevelMetricsThresholds)` (message)
  * `[EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.TurnLevelMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.TurnLevelMetricsThresholds)` (message)
  * `[EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.TurnLevelMetricsThresholds.SemanticSimilarityChannel](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.TurnLevelMetricsThresholds.SemanticSimilarityChannel)` (enum)
  * `[EvaluationMetricsThresholds.HallucinationMetricBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.EvaluationMetricsThresholds.HallucinationMetricBehavior)` (enum)
  * `[EvaluationMetricsThresholds.ToolMatchingSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.EvaluationMetricsThresholds.ToolMatchingSettings)` (message)
  * `[EvaluationMetricsThresholds.ToolMatchingSettings.ExtraToolCallBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.EvaluationMetricsThresholds.ToolMatchingSettings.ExtraToolCallBehavior)` (enum)
  * `[Event](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Event)` (message)
  * `[Example](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Example)` (message)
  * `[ExecuteToolRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ExecuteToolRequest)` (message)
  * `[ExecuteToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ExecuteToolResponse)` (message)
  * `[ExecutionType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ExecutionType)` (enum)
  * `[ExperimentConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ExperimentConfig)` (message)
  * `[ExperimentConfig.State](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ExperimentConfig.State)` (enum)
  * `[ExperimentConfig.VersionRelease](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ExperimentConfig.VersionRelease)` (message)
  * `[ExperimentConfig.VersionRelease.TrafficAllocation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ExperimentConfig.VersionRelease.TrafficAllocation)` (message)
  * `[ExportAppRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ExportAppRequest)` (message)
  * `[ExportAppRequest.ExportFormat](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ExportAppRequest.ExportFormat)` (enum)
  * `[ExportAppResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ExportAppResponse)` (message)
  * `[ExpressionCondition](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ExpressionCondition)` (message)
  * `[FileSearchTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.FileSearchTool)` (message)
  * `[FileSearchTool.CorpusType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.FileSearchTool.CorpusType)` (enum)
  * `[GenerateChatTokenRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.GenerateChatTokenRequest)` (message)
  * `[GenerateChatTokenResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.GenerateChatTokenResponse)` (message)
  * `[GetAgentRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.GetAgentRequest)` (message)
  * `[GetAppRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.GetAppRequest)` (message)
  * `[GetAppVersionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.GetAppVersionRequest)` (message)
  * `[GetChangelogRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.GetChangelogRequest)` (message)
  * `[GetConversationRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.GetConversationRequest)` (message)
  * `[GetDeploymentRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.GetDeploymentRequest)` (message)
  * `[GetExampleRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.GetExampleRequest)` (message)
  * `[GetGuardrailRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.GetGuardrailRequest)` (message)
  * `[GetToolRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.GetToolRequest)` (message)
  * `[GetToolsetRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.GetToolsetRequest)` (message)
  * `[GoAway](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.GoAway)` (message)
  * `[GoogleSearchSuggestions](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.GoogleSearchSuggestions)` (message)
  * `[GoogleSearchTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.GoogleSearchTool)` (message)
  * `[GoogleSearchTool.PromptConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.GoogleSearchTool.PromptConfig)` (message)
  * `[Guardrail](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Guardrail)` (message)
  * `[Guardrail.CodeCallback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Guardrail.CodeCallback)` (message)
  * `[Guardrail.ContentFilter](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Guardrail.ContentFilter)` (message)
  * `[Guardrail.ContentFilter.MatchType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Guardrail.ContentFilter.MatchType)` (enum)
  * `[Guardrail.LlmPolicy](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Guardrail.LlmPolicy)` (message)
  * `[Guardrail.LlmPolicy.PolicyScope](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Guardrail.LlmPolicy.PolicyScope)` (enum)
  * `[Guardrail.LlmPromptSecurity](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Guardrail.LlmPromptSecurity)` (message)
  * `[Guardrail.LlmPromptSecurity.DefaultSecuritySettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Guardrail.LlmPromptSecurity.DefaultSecuritySettings)` (message)
  * `[Guardrail.ModelSafety](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Guardrail.ModelSafety)` (message)
  * `[Guardrail.ModelSafety.HarmBlockThreshold](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Guardrail.ModelSafety.HarmBlockThreshold)` (enum)
  * `[Guardrail.ModelSafety.HarmCategory](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Guardrail.ModelSafety.HarmCategory)` (enum)
  * `[Guardrail.ModelSafety.SafetySetting](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Guardrail.ModelSafety.SafetySetting)` (message)
  * `[Guardrail.Supervisor](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Guardrail.Supervisor)` (message)
  * `[Guardrail.Supervisor.DetectionMode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Guardrail.Supervisor.DetectionMode)` (enum)
  * `[Guardrail.Supervisor.Type](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Guardrail.Supervisor.Type)` (enum)
  * `[Image](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Image)` (message)
  * `[ImportAppRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ImportAppRequest)` (message)
  * `[ImportAppRequest.ImportOptions](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ImportAppRequest.ImportOptions)` (message)
  * `[ImportAppRequest.ImportOptions.ConflictResolutionStrategy](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ImportAppRequest.ImportOptions.ConflictResolutionStrategy)` (enum)
  * `[ImportAppResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ImportAppResponse)` (message)
  * `[InputAudioConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.InputAudioConfig)` (message)
  * `[InstagramCredentials](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.InstagramCredentials)` (message)
  * `[InterruptionSignal](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.InterruptionSignal)` (message)
  * `[LanguageSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.LanguageSettings)` (message)
  * `[ListAgentsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ListAgentsRequest)` (message)
  * `[ListAgentsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ListAgentsResponse)` (message)
  * `[ListAppVersionsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ListAppVersionsRequest)` (message)
  * `[ListAppVersionsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ListAppVersionsResponse)` (message)
  * `[ListAppsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ListAppsRequest)` (message)
  * `[ListAppsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ListAppsResponse)` (message)
  * `[ListChangelogsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ListChangelogsRequest)` (message)
  * `[ListChangelogsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ListChangelogsResponse)` (message)
  * `[ListConversationsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ListConversationsRequest)` (message)
  * `[ListConversationsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ListConversationsResponse)` (message)
  * `[ListDeploymentsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ListDeploymentsRequest)` (message)
  * `[ListDeploymentsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ListDeploymentsResponse)` (message)
  * `[ListExamplesRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ListExamplesRequest)` (message)
  * `[ListExamplesResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ListExamplesResponse)` (message)
  * `[ListGuardrailsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ListGuardrailsRequest)` (message)
  * `[ListGuardrailsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ListGuardrailsResponse)` (message)
  * `[ListToolsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ListToolsRequest)` (message)
  * `[ListToolsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ListToolsResponse)` (message)
  * `[ListToolsetsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ListToolsetsRequest)` (message)
  * `[ListToolsetsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ListToolsetsResponse)` (message)
  * `[LoggingSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.LoggingSettings)` (message)
  * `[McpTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.McpTool)` (message)
  * `[McpTool.State](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.McpTool.State)` (enum)
  * `[McpToolDefinition](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.McpToolDefinition)` (message)
  * `[McpToolOverride](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.McpToolOverride)` (message)
  * `[McpToolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.McpToolset)` (message)
  * `[Message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Message)` (message)
  * `[MetricAnalysisSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.MetricAnalysisSettings)` (message)
  * `[MockConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.MockConfig)` (message)
  * `[MockConfig.UnmatchedToolCallBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.MockConfig.UnmatchedToolCallBehavior)` (enum)
  * `[MockedToolCall](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.MockedToolCall)` (message)
  * `[ModelSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ModelSettings)` (message)
  * `[ModelSettings.ThinkingLevel](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ModelSettings.ThinkingLevel)` (enum)
  * `[OAuthConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.OAuthConfig)` (message)
  * `[OAuthConfig.OauthGrantType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.OAuthConfig.OauthGrantType)` (enum)
  * `[OpenApiTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.OpenApiTool)` (message)
  * `[OpenApiToolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.OpenApiToolset)` (message)
  * `[OperationMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.OperationMetadata)` (message)
  * `[OutputAudioConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.OutputAudioConfig)` (message)
  * `[PythonCodeCondition](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.PythonCodeCondition)` (message)
  * `[PythonFunction](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.PythonFunction)` (message)
  * `[RecognitionResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.RecognitionResult)` (message)
  * `[RedactionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.RedactionConfig)` (message)
  * `[RemoteA2aConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.RemoteA2aConfig)` (message)
  * `[RemoteAgentTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.RemoteAgentTool)` (message)
  * `[RestoreAppVersionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.RestoreAppVersionRequest)` (message)
  * `[RestoreAppVersionResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.RestoreAppVersionResponse)` (message)
  * `[RetrieveToolSchemaRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.RetrieveToolSchemaRequest)` (message)
  * `[RetrieveToolSchemaResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.RetrieveToolSchemaResponse)` (message)
  * `[RetrieveToolsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.RetrieveToolsRequest)` (message)
  * `[RetrieveToolsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.RetrieveToolsResponse)` (message)
  * `[RunSessionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.RunSessionRequest)` (message)
  * `[RunSessionResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.RunSessionResponse)` (message)
  * `[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Schema)` (message)
  * `[Schema.Type](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Schema.Type)` (enum)
  * `[SecuritySettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.SecuritySettings)` (message)
  * `[ServiceAccountAuthConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ServiceAccountAuthConfig)` (message)
  * `[ServiceAgentIdTokenAuthConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ServiceAgentIdTokenAuthConfig)` (message)
  * `[ServiceDirectoryConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ServiceDirectoryConfig)` (message)
  * `[SessionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.SessionConfig)` (message)
  * `[SessionConfig.RemoteDialogflowQueryParameters](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.SessionConfig.RemoteDialogflowQueryParameters)` (message)
  * `[SessionInput](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.SessionInput)` (message)
  * `[SessionOutput](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.SessionOutput)` (message)
  * `[SessionOutput.DiagnosticInfo](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.SessionOutput.DiagnosticInfo)` (message)
  * `[Span](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Span)` (message)
  * `[SynthesizeSpeechConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.SynthesizeSpeechConfig)` (message)
  * `[SystemTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.SystemTool)` (message)
  * `[TimeZoneSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.TimeZoneSettings)` (message)
  * `[TlsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.TlsConfig)` (message)
  * `[TlsConfig.CaCert](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.TlsConfig.CaCert)` (message)
  * `[Tool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Tool)` (message)
  * `[ToolCall](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ToolCall)` (message)
  * `[ToolCalls](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ToolCalls)` (message)
  * `[ToolFakeConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ToolFakeConfig)` (message)
  * `[ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ToolResponse)` (message)
  * `[ToolResponses](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ToolResponses)` (message)
  * `[Toolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Toolset)` (message)
  * `[ToolsetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ToolsetTool)` (message)
  * `[TransferRule](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.TransferRule)` (message)
  * `[TransferRule.DeterministicTransfer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.TransferRule.DeterministicTransfer)` (message)
  * `[TransferRule.Direction](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.TransferRule.Direction)` (enum)
  * `[TransferRule.DisablePlannerTransfer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.TransferRule.DisablePlannerTransfer)` (message)
  * `[TriggerAction](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.TriggerAction)` (message)
  * `[TriggerAction.GenerativeAnswer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.TriggerAction.GenerativeAnswer)` (message)
  * `[TriggerAction.RespondImmediately](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.TriggerAction.RespondImmediately)` (message)
  * `[TriggerAction.Response](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.TriggerAction.Response)` (message)
  * `[TriggerAction.TransferAgent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.TriggerAction.TransferAgent)` (message)
  * `[UpdateAgentRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.UpdateAgentRequest)` (message)
  * `[UpdateAppRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.UpdateAppRequest)` (message)
  * `[UpdateAppVersionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.UpdateAppVersionRequest)` (message)
  * `[UpdateDeploymentRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.UpdateDeploymentRequest)` (message)
  * `[UpdateExampleRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.UpdateExampleRequest)` (message)
  * `[UpdateGuardrailRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.UpdateGuardrailRequest)` (message)
  * `[UpdateToolRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.UpdateToolRequest)` (message)
  * `[UpdateToolsetRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.UpdateToolsetRequest)` (message)
  * `[VpcScSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.VpcScSettings)` (message)
  * `[WebSearchQuery](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.WebSearchQuery)` (message)
  * `[WhatsAppCredentials](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.WhatsAppCredentials)` (message)
  * `[WidgetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.WidgetTool)` (message)
  * `[WidgetTool.DataMapping](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.WidgetTool.DataMapping)` (message)
  * `[WidgetTool.DataMapping.Mode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.WidgetTool.DataMapping.Mode)` (enum)
  * `[WidgetTool.TextResponseConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.WidgetTool.TextResponseConfig)` (message)
  * `[WidgetTool.TextResponseConfig.Type](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.WidgetTool.TextResponseConfig.Type)` (enum)
  * `[WidgetTool.WidgetType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.WidgetTool.WidgetType)` (enum)



## AgentService

The service that manages agent-related resources in Gemini Enterprise for Customer Engagement (CES).

BatchDeleteConversations  
---  
` rpc BatchDeleteConversations(`[BatchDeleteConversationsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.BatchDeleteConversationsRequest)`) returns (`[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Batch deletes the specified conversations.

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
` rpc CreateAgent(`[CreateAgentRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.CreateAgentRequest)`) returns (`[Agent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Agent)`) ` Creates a new agent in the given app.

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
` rpc CreateApp(`[CreateAppRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.CreateAppRequest)`) returns (`[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Creates a new app in the given project and location.

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
` rpc CreateAppVersion(`[CreateAppVersionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.CreateAppVersionRequest)`) returns (`[AppVersion](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AppVersion)`) ` Creates a new app version in the given app.

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
` rpc CreateDeployment(`[CreateDeploymentRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.CreateDeploymentRequest)`) returns (`[Deployment](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Deployment)`) ` Creates a new deployment in the given app.

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
` rpc CreateExample(`[CreateExampleRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.CreateExampleRequest)`) returns (`[Example](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Example)`) ` Creates a new example in the given app.

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
` rpc CreateGuardrail(`[CreateGuardrailRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.CreateGuardrailRequest)`) returns (`[Guardrail](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Guardrail)`) ` Creates a new guardrail in the given app.

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
` rpc CreateTool(`[CreateToolRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.CreateToolRequest)`) returns (`[Tool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Tool)`) ` Creates a new tool in the given app.

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
` rpc CreateToolset(`[CreateToolsetRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.CreateToolsetRequest)`) returns (`[Toolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Toolset)`) ` Creates a new toolset in the given app.

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
` rpc DeleteAgent(`[DeleteAgentRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DeleteAgentRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes the specified agent.

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
` rpc DeleteApp(`[DeleteAppRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DeleteAppRequest)`) returns (`[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Deletes the specified app.

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
` rpc DeleteAppVersion(`[DeleteAppVersionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DeleteAppVersionRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes the specified app version.

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
` rpc DeleteConversation(`[DeleteConversationRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DeleteConversationRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes the specified conversation.

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
` rpc DeleteDeployment(`[DeleteDeploymentRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DeleteDeploymentRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes the specified deployment.

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
` rpc DeleteExample(`[DeleteExampleRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DeleteExampleRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes the specified example.

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
` rpc DeleteGuardrail(`[DeleteGuardrailRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DeleteGuardrailRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes the specified guardrail.

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
` rpc DeleteTool(`[DeleteToolRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DeleteToolRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes the specified tool.

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
` rpc DeleteToolset(`[DeleteToolsetRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DeleteToolsetRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes the specified toolset.

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
` rpc ExportApp(`[ExportAppRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ExportAppRequest)`) returns (`[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Exports the specified app.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `ces.apps.export`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
GetAgent  
---  
` rpc GetAgent(`[GetAgentRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.GetAgentRequest)`) returns (`[Agent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Agent)`) ` Gets details of the specified agent.

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
` rpc GetApp(`[GetAppRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.GetAppRequest)`) returns (`[App](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.App)`) ` Gets details of the specified app.

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
` rpc GetAppVersion(`[GetAppVersionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.GetAppVersionRequest)`) returns (`[AppVersion](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AppVersion)`) ` Gets details of the specified app version.

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
` rpc GetChangelog(`[GetChangelogRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.GetChangelogRequest)`) returns (`[Changelog](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Changelog)`) ` Gets the specified changelog.

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
` rpc GetConversation(`[GetConversationRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.GetConversationRequest)`) returns (`[Conversation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Conversation)`) ` Gets details of the specified conversation.

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
` rpc GetDeployment(`[GetDeploymentRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.GetDeploymentRequest)`) returns (`[Deployment](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Deployment)`) ` Gets details of the specified deployment.

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
` rpc GetExample(`[GetExampleRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.GetExampleRequest)`) returns (`[Example](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Example)`) ` Gets details of the specified example.

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
` rpc GetGuardrail(`[GetGuardrailRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.GetGuardrailRequest)`) returns (`[Guardrail](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Guardrail)`) ` Gets details of the specified guardrail.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `ces.guardrails.get`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
GetTool  
---  
` rpc GetTool(`[GetToolRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.GetToolRequest)`) returns (`[Tool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Tool)`) ` Gets details of the specified tool.

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
` rpc GetToolset(`[GetToolsetRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.GetToolsetRequest)`) returns (`[Toolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Toolset)`) ` Gets details of the specified toolset.

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
` rpc ImportApp(`[ImportAppRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ImportAppRequest)`) returns (`[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Imports the specified app.

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
` rpc ListAgents(`[ListAgentsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ListAgentsRequest)`) returns (`[ListAgentsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ListAgentsResponse)`) ` Lists agents in the given app.

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
` rpc ListAppVersions(`[ListAppVersionsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ListAppVersionsRequest)`) returns (`[ListAppVersionsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ListAppVersionsResponse)`) ` Lists all app versions in the given app.

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
` rpc ListApps(`[ListAppsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ListAppsRequest)`) returns (`[ListAppsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ListAppsResponse)`) ` Lists apps in the given project and location.

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
` rpc ListChangelogs(`[ListChangelogsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ListChangelogsRequest)`) returns (`[ListChangelogsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ListChangelogsResponse)`) ` Lists the changelogs of the specified app.

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
` rpc ListConversations(`[ListConversationsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ListConversationsRequest)`) returns (`[ListConversationsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ListConversationsResponse)`) ` Lists conversations in the given app.

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
` rpc ListDeployments(`[ListDeploymentsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ListDeploymentsRequest)`) returns (`[ListDeploymentsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ListDeploymentsResponse)`) ` Lists deployments in the given app.

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
` rpc ListExamples(`[ListExamplesRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ListExamplesRequest)`) returns (`[ListExamplesResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ListExamplesResponse)`) ` Lists examples in the given app.

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
` rpc ListGuardrails(`[ListGuardrailsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ListGuardrailsRequest)`) returns (`[ListGuardrailsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ListGuardrailsResponse)`) ` Lists guardrails in the given app.

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
` rpc ListTools(`[ListToolsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ListToolsRequest)`) returns (`[ListToolsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ListToolsResponse)`) ` Lists tools in the given app.

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
` rpc ListToolsets(`[ListToolsetsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ListToolsetsRequest)`) returns (`[ListToolsetsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ListToolsetsResponse)`) ` Lists toolsets in the given app.

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
` rpc RestoreAppVersion(`[RestoreAppVersionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.RestoreAppVersionRequest)`) returns (`[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Restores the specified app version. This will create a new app version from the current draft app and overwrite the current draft with the specified app version.

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
` rpc UpdateAgent(`[UpdateAgentRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.UpdateAgentRequest)`) returns (`[Agent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Agent)`) ` Updates the specified agent.

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
` rpc UpdateApp(`[UpdateAppRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.UpdateAppRequest)`) returns (`[App](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.App)`) ` Updates the specified app.

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
` rpc UpdateAppVersion(`[UpdateAppVersionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.UpdateAppVersionRequest)`) returns (`[AppVersion](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AppVersion)`) ` Updates the specified app version.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
UpdateDeployment  
---  
` rpc UpdateDeployment(`[UpdateDeploymentRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.UpdateDeploymentRequest)`) returns (`[Deployment](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Deployment)`) ` Updates the specified deployment.

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
` rpc UpdateExample(`[UpdateExampleRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.UpdateExampleRequest)`) returns (`[Example](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Example)`) ` Updates the specified example.

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
` rpc UpdateGuardrail(`[UpdateGuardrailRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.UpdateGuardrailRequest)`) returns (`[Guardrail](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Guardrail)`) ` Updates the specified guardrail.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `ces.guardrails.update`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
UpdateTool  
---  
` rpc UpdateTool(`[UpdateToolRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.UpdateToolRequest)`) returns (`[Tool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Tool)`) ` Updates the specified tool.

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
` rpc UpdateToolset(`[UpdateToolsetRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.UpdateToolsetRequest)`) returns (`[Toolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Toolset)`) ` Updates the specified toolset.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `ces.toolsets.update`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
  
## SessionService

Session service provides APIs for interacting with CES agents.

BidiRunSession  
---  
` rpc BidiRunSession(`[BidiSessionClientMessage](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.BidiSessionClientMessage)`) returns (`[BidiSessionServerMessage](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.BidiSessionServerMessage)`) ` Establishes a bidirectional streaming connection with the CES agent. The agent processes continuous multimodal inputs (e.g., text, audio) and generates real-time multimodal output streams.\--- Client Request Stream --- The client streams requests in the following order:

  1. Initialization: The first message must contain `[SessionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.BidiSessionClientMessage.FIELDS.google.cloud.ces.v1.SessionConfig.google.cloud.ces.v1.BidiSessionClientMessage.config)`. For audio sessions, this should also include `[InputAudioConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.SessionConfig.FIELDS.google.cloud.ces.v1.InputAudioConfig.google.cloud.ces.v1.SessionConfig.input_audio_config)` and `[OutputAudioConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.SessionConfig.FIELDS.google.cloud.ces.v1.OutputAudioConfig.google.cloud.ces.v1.SessionConfig.output_audio_config)` to define audio processing and synthesis parameters.
  2. Interaction: Subsequent messages stream `[SessionInput](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.BidiSessionClientMessage.FIELDS.google.cloud.ces.v1.SessionInput.google.cloud.ces.v1.BidiSessionClientMessage.realtime_input)` containing real-time user input data.
  3. Termination: The client should half-close the stream when there is no more user input. It should also half-close upon receiving `[EndSession](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.BidiSessionServerMessage.FIELDS.google.cloud.ces.v1.EndSession.google.cloud.ces.v1.BidiSessionServerMessage.end_session)` or `[GoAway](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.BidiSessionServerMessage.FIELDS.google.cloud.ces.v1.GoAway.google.cloud.ces.v1.BidiSessionServerMessage.go_away)` from the agent.

\--- Server Response Stream --- For each interaction turn, the agent streams messages in the following sequence:

  1. Speech Recognition (First N messages): Contains `[RecognitionResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.BidiSessionServerMessage.FIELDS.google.cloud.ces.v1.RecognitionResult.google.cloud.ces.v1.BidiSessionServerMessage.recognition_result)` representing the concatenated user speech segments captured so far. This is only populated for audio sessions.
  2. Response (Next M messages): Contains `[SessionOutput](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.BidiSessionServerMessage.FIELDS.google.cloud.ces.v1.SessionOutput.google.cloud.ces.v1.BidiSessionServerMessage.session_output)` delivering the agent's response in various modalities (e.g., text, audio).
  3. Turn Completion (Final message of the turn): Contains `[SessionOutput](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.BidiSessionServerMessage.FIELDS.google.cloud.ces.v1.SessionOutput.google.cloud.ces.v1.BidiSessionServerMessage.session_output)` with `[turn_completed](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.SessionOutput.FIELDS.bool.google.cloud.ces.v1.SessionOutput.turn_completed)` set to true. This signals the end of the current turn and includes `[DiagnosticInfo](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.SessionOutput.FIELDS.google.cloud.ces.v1.SessionOutput.DiagnosticInfo.google.cloud.ces.v1.SessionOutput.diagnostic_info)` with execution details.

\--- Audio Best Practices --- 1. Streaming: Stream `[audio data](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.SessionInput.FIELDS.bytes.google.cloud.ces.v1.SessionInput.audio)` **CONTINUOUSLY** , even during silence. Recommended chunk size: 40-120ms (balances latency vs. efficiency).

  1. Playback & Interruption: Play `[audio responses](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.SessionOutput.FIELDS.bytes.google.cloud.ces.v1.SessionOutput.audio)` upon receipt. Stop playback immediately if an `[InterruptionSignal](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.BidiSessionServerMessage.FIELDS.google.cloud.ces.v1.InterruptionSignal.google.cloud.ces.v1.BidiSessionServerMessage.interruption_signal)` is received (e.g., user barge-in or new agent response).



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
` rpc RunSession(`[RunSessionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.RunSessionRequest)`) returns (`[RunSessionResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.RunSessionResponse)`) ` Initiates a single-turn interaction with the CES agent within a session.

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
` rpc StreamRunSession(`[RunSessionRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.RunSessionRequest)`) returns (`[RunSessionResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.RunSessionResponse)`) ` Initiates a single-turn interaction with the CES agent. Uses server-side streaming to deliver incremental results and partial responses as they are generated.By default, complete responses (e.g., messages from callbacks or full LLM responses) are sent to the client as soon as they are available. To enable streaming individual text chunks directly from the model, set `[enable_text_streaming](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.SessionConfig.FIELDS.bool.google.cloud.ces.v1.SessionConfig.enable_text_streaming)` to true.

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
` rpc ExecuteTool(`[ExecuteToolRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ExecuteToolRequest)`) returns (`[ExecuteToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ExecuteToolResponse)`) ` Executes the given tool with the given arguments.

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
` rpc RetrieveToolSchema(`[RetrieveToolSchemaRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.RetrieveToolSchemaRequest)`) returns (`[RetrieveToolSchemaResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.RetrieveToolSchemaResponse)`) ` Retrieve the schema of the given tool. The schema is computed on the fly for the given instance of the tool.

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
` rpc RetrieveTools(`[RetrieveToolsRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.RetrieveToolsRequest)`) returns (`[RetrieveToolsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.RetrieveToolsResponse)`) ` Retrieve the list of tools included in the specified toolset.

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
` rpc GenerateChatToken(`[GenerateChatTokenRequest](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.GenerateChatTokenRequest)`) returns (`[GenerateChatTokenResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.GenerateChatTokenResponse)`) ` Generates a session scoped token for chat widget to authenticate with Session APIs.

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
`entity_operation` |  `[Action.EntityOperation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Action.EntityOperation)` Entity operation configuration for the tool to use.  
  
## EntityOperation

Entity CRUD operation specification.

Fields  
---  
`entity_id` |  `string` Required. ID of the entity.  
`operation` |  `[Action.EntityOperation.OperationType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Action.EntityOperation.OperationType)` Required. Operation to perform on the entity.  
  
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
`model_settings` |  `[ModelSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ModelSettings)` Optional. Configurations for the LLM model.  
`instruction` |  `string` Optional. Instructions for the LLM model to guide the agent's behavior.  
`tools[]` |  `string` Optional. List of available tools for the agent. Format: `projects/{project}/locations/{location}/apps/{app}/tools/{tool}`  
`child_agents[]` |  `string` Optional. List of child agents in the agent tree. Format: `projects/{project}/locations/{location}/apps/{app}/agents/{agent}`  
`before_agent_callbacks[]` |  `[Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Callback)` Optional. The callbacks to execute before the agent is called. The provided callbacks are executed sequentially in the exact order they are given in the list. If a callback returns an overridden response, execution stops and any remaining callbacks are skipped.  
`after_agent_callbacks[]` |  `[Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Callback)` Optional. The callbacks to execute after the agent is called. The provided callbacks are executed sequentially in the exact order they are given in the list. If a callback returns an overridden response, execution stops and any remaining callbacks are skipped.  
`before_model_callbacks[]` |  `[Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Callback)` Optional. The callbacks to execute before the model is called. If there are multiple calls to the model, the callback will be executed multiple times. The provided callbacks are executed sequentially in the exact order they are given in the list. If a callback returns an overridden response, execution stops and any remaining callbacks are skipped.  
`after_model_callbacks[]` |  `[Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Callback)` Optional. The callbacks to execute after the model is called. If there are multiple calls to the model, the callback will be executed multiple times. The provided callbacks are executed sequentially in the exact order they are given in the list. If a callback returns an overridden response, execution stops and any remaining callbacks are skipped.  
`before_tool_callbacks[]` |  `[Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Callback)` Optional. The callbacks to execute before the tool is invoked. If there are multiple tool invocations, the callback will be executed multiple times. The provided callbacks are executed sequentially in the exact order they are given in the list. If a callback returns an overridden response, execution stops and any remaining callbacks are skipped.  
`after_tool_callbacks[]` |  `[Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Callback)` Optional. The callbacks to execute after the tool is invoked. If there are multiple tool invocations, the callback will be executed multiple times. The provided callbacks are executed sequentially in the exact order they are given in the list. If a callback returns an overridden response, execution stops and any remaining callbacks are skipped.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Timestamp when the agent was created.  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Timestamp when the agent was last updated.  
`guardrails[]` |  `string` Optional. List of guardrails for the agent. Format: `projects/{project}/locations/{location}/apps/{app}/guardrails/{guardrail}`  
`etag` |  `string` Etag used to ensure the object hasn't changed during a read-modify-write operation. If the etag is empty, the update will overwrite any concurrent changes.  
`toolsets[]` |  `[Agent.AgentToolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Agent.AgentToolset)` Optional. List of toolsets for the agent.  
`generated_summary` |  `string` Output only. If the agent is generated by the LLM assistant, this field contains a descriptive summary of the generation.  
`transfer_rules[]` |  `[TransferRule](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.TransferRule)` Optional. Agent transfer rules. If multiple rules match, the first one in the list will be used.  
`validation_errors[]` |  `string` Output only. Misconfigurations or errors in the agent that may affect agent quality.  
Union field `agent_type`. The type of agent. `agent_type` can be only one of the following:  
`llm_agent` |  `[Agent.LlmAgent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Agent.LlmAgent)` Optional. The default agent type.  
`remote_dialogflow_agent` |  `[Agent.RemoteDialogflowAgent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Agent.RemoteDialogflowAgent)` Optional. The remote [Dialogflow](https://cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents) agent to be used for the agent execution. If this field is set, all other agent level properties will be ignored.Note: If the Dialogflow agent is in a different project from the app, you should grant `roles/dialogflow.client` to the CES service agent `service-<PROJECT-NUMBER>@gcp-sa-ces.iam.gserviceaccount.com`.  
`remote_a2a_agent` |  `[Agent.RemoteA2aAgent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Agent.RemoteA2aAgent)` Optional. The remote [A2A](https://github.com/a2aproject/A2A) agent to be used for the agent execution.  
  
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
`a2a_config` |  `[RemoteA2aConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.RemoteA2aConfig)` Required. The A2A connection configuration.  
  
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
`supported_interfaces[]` |  `[AgentInterface](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentInterface)` Required. Ordered list of supported interfaces. The first entry is preferred.  
`version` |  `string` Required. The version of the agent.  
`skills[]` |  `[AgentSkill](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentSkill)` Required. Skills represent a unit of ability an agent can perform. This may somewhat abstract but represents a more focused set of actions that the agent is highly likely to succeed at.  
  
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
  
## AmbientSoundConfig

Configuration for the ambient sound to be played with the synthesized agent response, to enhance the naturalness of the conversation.

Fields  
---  
`volume_gain_db` |  `double` Optional. Volume gain (in dB) of the normal native volume supported by ambient noise, in the range [-96.0, 16.0]. If unset, or set to a value of 0.0 (dB), will play at normal native signal amplitude. A value of -6.0 (dB) will play at approximately half the amplitude of the normal native signal amplitude. A value of +6.0 (dB) will play at approximately twice the amplitude of the normal native signal amplitude. We strongly recommend not to exceed +10 (dB) as there's usually no effective increase in loudness for any value greater than that.  
Union field `source`. Ambient noise to be played with the synthesized agent response, to enhance the naturalness of the conversation. `source` can be only one of the following:  
`prebuilt_ambient_noise  
**(deprecated)**` |  `[AmbientSoundConfig.PrebuiltAmbientNoise](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AmbientSoundConfig.PrebuiltAmbientNoise)` This item is deprecated!Optional. Deprecated: `prebuilt_ambient_noise` is deprecated in favor of `prebuilt_ambient_sound`.  
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
`api_key_config` |  `[ApiKeyConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ApiKeyConfig)` Optional. Config for API key auth.  
`oauth_config` |  `[OAuthConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.OAuthConfig)` Optional. Config for OAuth.  
`service_agent_id_token_auth_config` |  `[ServiceAgentIdTokenAuthConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ServiceAgentIdTokenAuthConfig)` Optional. Config for ID token auth generated from CES service agent.  
`service_account_auth_config` |  `[ServiceAccountAuthConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ServiceAccountAuthConfig)` Optional. Config for service account authentication.  
`bearer_token_config` |  `[BearerTokenConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.BearerTokenConfig)` Optional. Config for bearer token auth.  
  
## ApiKeyConfig

Configurations for authentication with API key.

Fields  
---  
`key_name` |  `string` Required. The parameter name or the header name of the API key. E.g., If the API request is "https://example.com/act?X-Api-Key=", "X-Api-Key" would be the parameter name.  
`api_key_secret_version` |  `string` Required. The name of the SecretManager secret version resource storing the API key. Format: `projects/{project}/secrets/{secret}/versions/{version}`Note: You should grant `roles/secretmanager.secretAccessor` role to the CES service agent `service-<PROJECT-NUMBER>@gcp-sa-ces.iam.gserviceaccount.com`.  
`request_location` |  `[ApiKeyConfig.RequestLocation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ApiKeyConfig.RequestLocation)` Required. Key location in the request.  
  
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
`language_settings` |  `[LanguageSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.LanguageSettings)` Optional. Language settings of the app.  
`time_zone_settings` |  `[TimeZoneSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.TimeZoneSettings)` Optional. TimeZone settings of the app.  
`audio_processing_config` |  `[AudioProcessingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AudioProcessingConfig)` Optional. Audio processing configuration of the app.  
`logging_settings` |  `[LoggingSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.LoggingSettings)` Optional. Logging settings of the app.  
`error_handling_settings` |  `[ErrorHandlingSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ErrorHandlingSettings)` Optional. Error handling settings of the app.  
`model_settings` |  `[ModelSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ModelSettings)` Optional. The default LLM model settings for the app. Individual resources (e.g. agents, guardrails) can override these configurations as needed.  
`tool_execution_mode` |  `[App.ToolExecutionMode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.App.ToolExecutionMode)` Optional. The tool execution mode for the app. If not provided, will default to PARALLEL.  
`evaluation_metrics_thresholds` |  `[EvaluationMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.EvaluationMetricsThresholds)` Optional. The evaluation thresholds for the app.  
`variable_declarations[]` |  `[App.VariableDeclaration](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.App.VariableDeclaration)` Optional. The declarations of the variables.  
`predefined_variable_declarations[]` |  `[App.VariableDeclaration](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.App.VariableDeclaration)` Output only. The declarations of predefined variables for the app.  
`global_instruction` |  `string` Optional. Instructions for all the agents in the app. You can use this instruction to set up a stable identity or personality across all the agents.  
`guardrails[]` |  `string` Optional. List of guardrails for the app. Format: `projects/{project}/locations/{location}/apps/{app}/guardrails/{guardrail}`  
`data_store_settings` |  `[DataStoreSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DataStoreSettings)` Optional. The data store settings for the app.  
`default_channel_profile` |  `[ChannelProfile](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ChannelProfile)` Optional. The default channel profile used by the app.  
`metadata` |  `map<string, string>` Optional. Metadata about the app. This field can be used to store additional information relevant to the app's details or intended usages.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Timestamp when the app was created.  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Timestamp when the app was last updated.  
`etag` |  `string` Output only. Etag used to ensure the object hasn't changed during a read-modify-write operation. If the etag is empty, the update will overwrite any concurrent changes.  
`deployment_count` |  `int32` Output only. Number of deployments in the app.  
`client_certificate_settings` |  `[ClientCertificateSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ClientCertificateSettings)` Optional. The default client certificate settings for the app.  
`vpc_sc_settings` |  `[VpcScSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.VpcScSettings)` Optional. VPC-SC settings for the app.  
`locked` |  `bool` Optional. Indicates whether the app is locked for changes. If the app is locked, modifications to the app resources will be rejected.  
`validation_errors[]` |  `string` Output only. Misconfigurations or warnings in the app.  
`dashboard_settings` |  `[DashboardSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DashboardSettings)` Optional. App-specific dashboard settings for linking and configuring Contact Center Insights dashboards.  
  
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
`schema` |  `[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Schema)` Required. The schema of the variable.  
  
## AppSnapshot

A snapshot of the app.

Fields  
---  
`app` |  `[App](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.App)` Optional. The basic settings for the app.  
`agents[]` |  `[Agent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Agent)` Optional. List of agents in the app.  
`tools[]` |  `[Tool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Tool)` Optional. List of tools in the app.  
`examples[]` |  `[Example](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Example)` Optional. List of examples in the app.  
`guardrails[]` |  `[Guardrail](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Guardrail)` Optional. List of guardrails in the app.  
`toolsets[]` |  `[Toolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Toolset)` Optional. List of toolsets in the app.  
  
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
`snapshot` |  `[AppSnapshot](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AppSnapshot)` Output only. The snapshot of the app when the version is created.  
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
`synthesize_speech_configs` |  `map<string, `[SynthesizeSpeechConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.SynthesizeSpeechConfig)`>` Optional. Configuration of how the agent response should be synthesized, mapping from the language code to `[SynthesizeSpeechConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.SynthesizeSpeechConfig)`.If the configuration for the specified language code is not found, the configuration for the root language code will be used. For example, if the map contains "en-us" and "en", and the specified language code is "en-gb", then "en" configuration will be used.Note: Language code is case-insensitive.  
`barge_in_config` |  `[BargeInConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.BargeInConfig)` Optional. Configures the agent behavior for the user barge-in activities.  
`inactivity_timeout` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Optional. The duration of user inactivity (no speech or interaction) before the agent prompts the user for reengagement. If not set, the agent will not prompt the user for reengagement.  
`ambient_sound_config` |  `[AmbientSoundConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AmbientSoundConfig)` Optional. Configuration for the ambient sound to be played with the synthesized agent response, to enhance the naturalness of the conversation.  
`custom_voice_samples[]` |  `[CustomVoiceSample](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.CustomVoiceSample)` Optional. Configures custom voice samples for voice cloning.  
  
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
**(deprecated)**` |  `bool` This item is deprecated!Optional. Deprecated: `disable_barge_in` is deprecated in favor of `[`disable_barge_in_control`](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ChannelProfile.FIELDS.bool.google.cloud.ces.v1.ChannelProfile.disable_barge_in_control)` in ChannelProfile.Disables user barge-in while the agent is speaking. If true, user input during agent response playback will be ignored.  
`barge_in_awareness` |  `bool` Optional. If enabled, the agent will adapt its next response based on the assumption that the user hasn't heard the full preceding agent message. This should not be used in scenarios where agent responses are displayed visually.  
  
## BatchDeleteConversationsRequest

Request message for `[AgentService.BatchDeleteConversations](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.BatchDeleteConversations)`.

Fields  
---  
`parent` |  `string` Required. The resource name of the app to delete conversations from. Format: `projects/{project}/locations/{location}/apps/{app}`  
`conversations[]` |  `string` Required. The resource names of the conversations to delete.  
  
## BatchDeleteConversationsResponse

Response message for `[AgentService.BatchDeleteConversations](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.BatchDeleteConversations)`.

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

The top-level message sent by the client for the `[SessionService.BidiRunSession](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.SessionService.BidiRunSession)` method.

Fields  
---  
Union field `message_type`. The type of the message. `message_type` can be only one of the following:  
`config` |  `[SessionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.SessionConfig)` Optional. The initial config message for the session.  
`realtime_input` |  `[SessionInput](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.SessionInput)` Optional. Realtime input for the session.  
  
## BidiSessionServerMessage

The top-level message returned from `[SessionService.BidiRunSession](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.SessionService.BidiRunSession)` method.

Fields  
---  
Union field `message_type`. The type of the message. `message_type` can be only one of the following:  
`session_output` |  `[SessionOutput](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.SessionOutput)` Optional. Processing result from the CES agent.  
`recognition_result` |  `[RecognitionResult](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.RecognitionResult)` Optional. Realtime speech recognition result for the audio input.  
`interruption_signal` |  `[InterruptionSignal](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.InterruptionSignal)` Optional. Indicates the agent's audio response has been interrupted.  
`end_session` |  `[EndSession](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.EndSession)` Optional. Indicates that the session has ended.  
`go_away` |  `[GoAway](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.GoAway)` Optional. Indicates that the server will disconnect soon and the client should half-close and restart the connection.  
  
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
`channel_type` |  `[ChannelProfile.ChannelType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ChannelProfile.ChannelType)` Optional. The type of the channel profile.  
`persona_property` |  `[ChannelProfile.PersonaProperty](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ChannelProfile.PersonaProperty)` Optional. The persona property of the channel profile.  
`web_widget_config` |  `[ChannelProfile.WebWidgetConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ChannelProfile.WebWidgetConfig)` Optional. The configuration for the web widget.  
`whatsapp_config` |  `[ChannelProfile.WhatsAppConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ChannelProfile.WhatsAppConfig)` Optional. Configuration specific to WhatsApp deployments.  
`instagram_config` |  `[ChannelProfile.InstagramConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ChannelProfile.InstagramConfig)` Optional. Configuration specific to Instagram deployments.  
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
`persona` |  `[ChannelProfile.PersonaProperty.Persona](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ChannelProfile.PersonaProperty.Persona)` Optional. The persona of the channel.  
  
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
`modality` |  `[ChannelProfile.WebWidgetConfig.Modality](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ChannelProfile.WebWidgetConfig.Modality)` Optional. The modality of the web widget.  
`theme` |  `[ChannelProfile.WebWidgetConfig.Theme](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ChannelProfile.WebWidgetConfig.Theme)` Optional. The theme of the web widget.  
`web_widget_title` |  `string` Optional. The title of the web widget.  
`security_settings` |  `[ChannelProfile.WebWidgetConfig.SecuritySettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ChannelProfile.WebWidgetConfig.SecuritySettings)` Optional. The security settings of the web widget.  
  
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
`blob` |  `[Blob](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Blob)` Optional. Blob data.  
`payload` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` Optional. Custom payload data.  
`image` |  `[Image](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Image)` Optional. Image data.  
`tool_call` |  `[ToolCall](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ToolCall)` Optional. Tool execution request.  
`tool_response` |  `[ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ToolResponse)` Optional. Tool execution response.  
`agent_transfer` |  `[AgentTransfer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentTransfer)` Optional. Agent transfer event.  
`updated_variables` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` A struct represents variables that were updated in the conversation, keyed by variable names.  
`default_variables` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` A struct represents default variables at the start of the conversation, keyed by variable names.  
  
## Citations

Citations associated with the agent response.

Fields  
---  
`cited_chunks[]` |  `[Citations.CitedChunk](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Citations.CitedChunk)` List of cited pieces of information.  
`inline_citations[]` |  `[Citations.InlineCitation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Citations.InlineCitation)` Optional. List of inline citations in the agent response.  
  
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

Represents a client-side function that the agent can invoke. When the tool is chosen by the agent, control is handed off to the client. The client is responsible for executing the function and returning the result as a `[ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ToolResponse)` to continue the interaction with the agent.

Fields  
---  
`name` |  `string` Required. The function name.  
`description` |  `string` Optional. The function description.  
`parameters` |  `[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Schema)` Optional. The schema of the function parameters.  
`response` |  `[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Schema)` Optional. The schema of the function response.  
  
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
`action` |  `[Action](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Action)` Required. Action for the tool to use.  
`auth_config` |  `[EndUserAuthConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.EndUserAuthConfig)` Optional. Configures how authentication is handled in Integration Connectors. By default, an admin authentication is passed in the Integration Connectors API requests. You can override it with a different end-user authentication config. **Note** : The Connection must have authentication override enabled in order to specify an EUC configuration here - otherwise, the ConnectorTool creation will fail. See <https://cloud.google.com/application-integration/docs/configure-connectors-task#configure-authentication-override> for details.  
`name` |  `string` Optional. The name of the tool that can be used by the Agent to decide whether to call this ConnectorTool.  
`description` |  `string` Optional. The description of the tool that can be used by the Agent to decide whether to call this ConnectorTool.  
  
## ConnectorToolset

A toolset that generates tools from an Integration Connectors Connection.

Fields  
---  
`connection` |  `string` Required. The full resource name of the referenced Integration Connectors Connection. Format: `projects/{project}/locations/{location}/connections/{connection}`  
`auth_config` |  `[EndUserAuthConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.EndUserAuthConfig)` Optional. Configures how authentication is handled in Integration Connectors. By default, an admin authentication is passed in the Integration Connectors API requests. You can override it with a different end-user authentication config. **Note** : The Connection must have authentication override enabled in order to specify an EUC configuration here - otherwise, the Toolset creation will fail. See: <https://cloud.google.com/application-integration/docs/configure-connectors-task#configure-authentication-override>  
`connector_actions[]` |  `[Action](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Action)` Required. The list of connector actions/entity operations to generate tools for.  
  
## Conversation

A conversation represents an interaction between an end user and the CES app.

Fields  
---  
`name` |  `string` Identifier. The unique identifier of the conversation. Format: `projects/{project}/locations/{location}/apps/{app}/conversations/{conversation}`  
`start_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Timestamp when the conversation was created.  
`end_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Timestamp when the conversation was completed.  
`turns[]` |  `[Conversation.Turn](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Conversation.Turn)` Required. The turns in the conversation.  
`turn_count` |  `int32` Output only. The number of turns in the conversation.  
`channel_type  
**(deprecated)**` |  `[Conversation.ChannelType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Conversation.ChannelType)` This item is deprecated!DEPRECATED. Please use `[input_types](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Conversation.FIELDS.repeated.google.cloud.ces.v1.Conversation.InputType.google.cloud.ces.v1.Conversation.input_types)` instead.  
`source` |  `[Conversation.Source](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Conversation.Source)` Output only. Indicate the source of the conversation.  
`input_types[]` |  `[Conversation.InputType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Conversation.InputType)` Output only. The input types of the conversation.  
`entry_agent` |  `string` Output only. The agent that initially handles the conversation. If not specified, the conversation is handled by the root agent. Format: `projects/{project}/locations/{location}/apps/{app}/agents/{agent}`  
`deployment` |  `string` Output only. The deployment of the app used for processing the conversation. Format: `projects/{project}/locations/{location}/apps/{app}/deployments/{deployment}`  
`app_version` |  `string` Output only. The version of the app used for processing the conversation. Format: `projects/{project}/locations/{location}/apps/{app}/versions/{version}`  
`language_code` |  `string` Output only. The language code of the conversation.  
`messages[]  
**(deprecated)**` |  `[Message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Message)` This item is deprecated!Deprecated. Use turns instead.  
  
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
`messages[]` |  `[Message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Message)` Optional. List of messages in the conversation turn, including user input, agent responses and intermediate events during the processing.  
`root_span` |  `[Span](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Span)` Optional. The root span of the action processing.  
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
`agent` |  `[Agent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Agent)` Required. The agent to create.  
  
## CreateAppRequest

Request message for `[AgentService.CreateApp](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.CreateApp)`.

Fields  
---  
`parent` |  `string` Required. The resource name of the location to create an app in.  
`app_id` |  `string` Optional. The ID to use for the app, which will become the final component of the app's resource name. If not provided, a unique ID will be automatically assigned for the app.  
`app` |  `[App](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.App)` Required. The app to create.  
  
## CreateAppVersionRequest

Request message for `[AgentService.CreateAppVersion](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.CreateAppVersion)`

Fields  
---  
`parent` |  `string` Required. The resource name of the app to create an app version in.  
`app_version_id` |  `string` Optional. The ID to use for the app version, which will become the final component of the app version's resource name. If not provided, a unique ID will be automatically assigned for the app version.  
`app_version` |  `[AppVersion](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AppVersion)` Required. The app version to create.  
  
## CreateDeploymentRequest

Request message for `[AgentService.CreateDeployment](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.CreateDeployment)`.

Fields  
---  
`parent` |  `string` Required. The parent app. Format: `projects/{project}/locations/{location}/apps/{app}`  
`deployment_id` |  `string` Optional. The ID to use for the deployment, which will become the final component of the deployment's resource name. If not provided, a unique ID will be automatically assigned for the deployment.  
`deployment` |  `[Deployment](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Deployment)` Required. The deployment to create.  
  
## CreateExampleRequest

Request message for `[AgentService.CreateExample](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.CreateExample)`.

Fields  
---  
`parent` |  `string` Required. The resource name of the app to create an example in.  
`example_id` |  `string` Optional. The ID to use for the example, which will become the final component of the example's resource name. If not provided, a unique ID will be automatically assigned for the example.  
`example` |  `[Example](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Example)` Required. The example to create.  
  
## CreateGuardrailRequest

Request message for `[AgentService.CreateGuardrail](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.CreateGuardrail)`.

Fields  
---  
`parent` |  `string` Required. The resource name of the app to create a guardrail in.  
`guardrail_id` |  `string` Optional. The ID to use for the guardrail, which will become the final component of the guardrail's resource name. If not provided, a unique ID will be automatically assigned for the guardrail.  
`guardrail` |  `[Guardrail](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Guardrail)` Required. The guardrail to create.  
  
## CreateToolRequest

Request message for `[AgentService.CreateTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.CreateTool)`.

Fields  
---  
`parent` |  `string` Required. The resource name of the app to create a tool in.  
`tool_id` |  `string` Optional. The ID to use for the tool, which will become the final component of the tool's resource name. If not provided, a unique ID will be automatically assigned for the tool.  
`tool` |  `[Tool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Tool)` Required. The tool to create.  
  
## CreateToolsetRequest

Request message for `[AgentService.CreateToolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.CreateToolset)`.

Fields  
---  
`parent` |  `string` Required. The resource name of the app to create a toolset in.  
`toolset_id` |  `string` Optional. The ID to use for the toolset, which will become the final component of the toolset's resource name. If not provided, a unique ID will be automatically assigned for the toolset.  
`toolset` |  `[Toolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Toolset)` Required. The toolset to create.  
  
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
`warnings[]` |  `[CustomVoiceSample.Warning](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.CustomVoiceSample.Warning)` Output only. Warning messages encountered during voice clone processing (e.g. low audio level).  
`voice_instruction_mode` |  `[CustomVoiceSample.VoiceInstructionMode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.CustomVoiceSample.VoiceInstructionMode)` Optional. Instruction mode for the voice sample. If unspecified, defaults to NO_INSTRUCTION.  
  
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
`type` |  `[CustomVoiceSample.Warning.WarningType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.CustomVoiceSample.Warning.WarningType)` Output only. The type of the warning.  
  
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
`type` |  `[DataStore.DataStoreType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DataStore.DataStoreType)` Output only. The type of the data store. This field is readonly and populated by the server.  
`document_processing_mode` |  `[DataStore.DocumentProcessingMode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DataStore.DocumentProcessingMode)` Output only. The document processing mode for the data store connection. Only set for PUBLIC_WEB and UNSTRUCTURED data stores.  
`display_name` |  `string` Output only. The display name of the data store.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Timestamp when the data store was created.  
`connector_config` |  `[DataStore.ConnectorConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DataStore.ConnectorConfig)` Output only. The connector config for the data store connection.  
  
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
`engines[]` |  `[DataStoreSettings.Engine](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DataStoreSettings.Engine)` Output only. The engines for the app.  
  
## Engine

An engine to which the data stores are connected. See Vertex AI Search: <https://cloud.google.com/generative-ai-app-builder/docs/enterprise-search-introduction>.

Fields  
---  
`name` |  `string` Output only. The resource name of the engine. Format: `projects/{project}/locations/{location}/collections/{collection}/engines/{engine}`  
`type` |  `[DataStoreSettings.Engine.Type](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DataStoreSettings.Engine.Type)` Output only. The type of the engine.  
  
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
`boost_specs[]` |  `[DataStoreTool.BoostSpecs](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DataStoreTool.BoostSpecs)` Optional. Boost specification to boost certain documents.  
`modality_configs[]` |  `[DataStoreTool.ModalityConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DataStoreTool.ModalityConfig)` Optional. The modality configs for the data store.  
`filter_parameter_behavior` |  `[DataStoreTool.FilterParameterBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DataStoreTool.FilterParameterBehavior)` Optional. The filter parameter behavior.  
Union field `search_source`. Defines the search source, either a single DataStore or an Engine. `search_source` can be only one of the following:  
`data_store_source` |  `[DataStoreTool.DataStoreSource](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DataStoreTool.DataStoreSource)` Optional. Search within a single specific DataStore.  
`engine_source` |  `[DataStoreTool.EngineSource](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DataStoreTool.EngineSource)` Optional. Search within an Engine (potentially across multiple DataStores).  
  
## BoostSpec

Boost specification to boost certain documents.

Fields  
---  
`condition_boost_specs[]` |  `[DataStoreTool.BoostSpec.ConditionBoostSpec](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DataStoreTool.BoostSpec.ConditionBoostSpec)` Required. A list of boosting specifications.  
  
## ConditionBoostSpec

Boost specification for a condition.

Fields  
---  
`condition` |  `string` Required. An expression which specifies a boost condition. The syntax is the same as filter expression syntax. Currently, the only supported condition is a list of BCP-47 lang codes. Example: To boost suggestions in languages en or fr: (lang_code: ANY("en", "fr"))  
`boost` |  `float` Optional. Strength of the boost, which should be in [-1, 1]. Negative boost means demotion. Default is 0.0.Setting to 1.0 gives the suggestions a big promotion. However, it does not necessarily mean that the top result will be a boosted suggestion.Setting to -1.0 gives the suggestions a big demotion. However, other suggestions that are relevant might still be shown.Setting to 0.0 means no boost applied. The boosting condition is ignored.  
`boost_control_spec` |  `[DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec)` Optional. Complex specification for custom ranking based on customer defined attribute value.  
  
## BoostControlSpec

Specification for custom ranking based on customer specified attribute value. It provides more controls for customized ranking than the simple (condition, boost) combination above.

Fields  
---  
`field_name` |  `string` Optional. The name of the field whose value will be used to determine the boost amount.  
`attribute_type` |  `[DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec.AttributeType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec.AttributeType)` Optional. The attribute type to be used to determine the boost amount. The attribute value can be derived from the field value of the specified field_name. In the case of numerical it is straightforward i.e. attribute_value = numerical_field_value. In the case of freshness however, attribute_value = (time.now() - datetime_field_value).  
`interpolation_type` |  `[DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec.InterpolationType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec.InterpolationType)` Optional. The interpolation type to be applied to connect the control points listed below.  
`control_points[]` |  `[DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec.ControlPoint](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DataStoreTool.BoostSpec.ConditionBoostSpec.BoostControlSpec.ControlPoint)` Optional. The control points used to define the curve. The monotonic function (defined through the interpolation_type above) passes through the control points listed here.  
  
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
`spec[]` |  `[DataStoreTool.BoostSpec](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DataStoreTool.BoostSpec)` Required. A list of boosting specifications.  
  
## DataStoreSource

Configuration for searching within a specific DataStore.

Fields  
---  
`filter` |  `string` Optional. Filter specification for the DataStore. See: <https://cloud.google.com/generative-ai-app-builder/docs/filter-search-metadata>  
`data_store` |  `[DataStore](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DataStore)` Optional. The data store.  
  
## EngineSource

Configuration for searching within an Engine, potentially targeting specific DataStores.

Fields  
---  
`engine` |  `string` Required. Full resource name of the Engine. Format: `projects/{project}/locations/{location}/collections/{collection}/engines/{engine}`  
`data_store_sources[]` |  `[DataStoreTool.DataStoreSource](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DataStoreTool.DataStoreSource)` Optional. Use to target specific DataStores within the Engine. If empty, the search applies to all DataStores associated with the Engine.  
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
`modality_type` |  `[DataStoreTool.ModalityConfig.ModalityType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DataStoreTool.ModalityConfig.ModalityType)` Required. The modality type.  
`rewriter_config` |  `[DataStoreTool.RewriterConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DataStoreTool.RewriterConfig)` Optional. The rewriter config.  
`summarization_config` |  `[DataStoreTool.SummarizationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DataStoreTool.SummarizationConfig)` Optional. The summarization config.  
`grounding_config` |  `[DataStoreTool.GroundingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DataStoreTool.GroundingConfig)` Optional. The grounding configuration.  
`snippets_config` |  `[DataStoreTool.SnippetsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DataStoreTool.SnippetsConfig)` Optional. The snippets configuration.  
  
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
`model_settings` |  `[ModelSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ModelSettings)` Required. Configurations for the LLM model.  
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
`model_settings` |  `[ModelSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ModelSettings)` Optional. Configurations for the LLM model.  
`prompt` |  `string` Optional. The prompt definition. If not set, default prompt will be used.  
`disabled` |  `bool` Optional. Whether summarization is disabled.  
  
## DeleteAgentRequest

Request message for `[AgentService.DeleteAgent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.DeleteAgent)`.

Fields  
---  
`name` |  `string` Required. The resource name of the agent to delete.  
`force` |  `bool` Optional. Indicates whether to forcefully delete the agent, even if it is still referenced by other app/agents/examples.

  * If `force = false`, the deletion fails if other agents/examples reference it.
  * If `force = true`, delete the agent and remove it from all referencing apps/agents/examples.

  
`etag` |  `string` Optional. The current etag of the agent. If an etag is not provided, the deletion will overwrite any concurrent changes. If an etag is provided and does not match the current etag of the agent, deletion will be blocked and an ABORTED error will be returned.  
  
## DeleteAppRequest

Request message for `[AgentService.DeleteApp](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.DeleteApp)`.

Fields  
---  
`name` |  `string` Required. The resource name of the app to delete.  
`etag` |  `string` Optional. The current etag of the app. If an etag is not provided, the deletion will overwrite any concurrent changes. If an etag is provided and does not match the current etag of the app, deletion will be blocked and an ABORTED error will be returned.  
  
## DeleteAppVersionRequest

Request message for `[AgentService.DeleteAppVersion](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.DeleteAppVersion)`.

Fields  
---  
`name` |  `string` Required. The resource name of the app version to delete.  
`etag` |  `string` Optional. The current etag of the app version. If an etag is not provided, the deletion will overwrite any concurrent changes. If an etag is provided and does not match the current etag of the app version, deletion will be blocked and an ABORTED error will be returned.  
  
## DeleteConversationRequest

Request message for `[AgentService.DeleteConversation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.DeleteConversation)`.

Fields  
---  
`name` |  `string` Required. The resource name of the conversation to delete.  
`source  
**(deprecated)**` |  `[Conversation.Source](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Conversation.Source)` This item is deprecated!Optional. Indicate the source of the conversation. If not set, Source.Live will be applied by default.  
  
## DeleteDeploymentRequest

Request message for `[AgentService.DeleteDeployment](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.DeleteDeployment)`.

Fields  
---  
`name` |  `string` Required. The name of the deployment to delete. Format: `projects/{project}/locations/{location}/apps/{app}/deployments/{deployment}`  
`etag` |  `string` Optional. The etag of the deployment. If an etag is provided and does not match the current etag of the deployment, deletion will be blocked and an ABORTED error will be returned.  
  
## DeleteExampleRequest

Request message for `[AgentService.DeleteExample](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.DeleteExample)`.

Fields  
---  
`name` |  `string` Required. The resource name of the example to delete.  
`etag` |  `string` Optional. The current etag of the example. If an etag is not provided, the deletion will overwrite any concurrent changes. If an etag is provided and does not match the current etag of the example, deletion will be blocked and an ABORTED error will be returned.  
  
## DeleteGuardrailRequest

Request message for `[AgentService.DeleteGuardrail](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.DeleteGuardrail)`.

Fields  
---  
`name` |  `string` Required. The resource name of the guardrail to delete.  
`force` |  `bool` Optional. Indicates whether to forcefully delete the guardrail, even if it is still referenced by app/agents.

  * If `force = false`, the deletion fails if any apps/agents still reference the guardrail.
  * If `force = true`, all existing references from apps/agents will be removed and the guardrail will be deleted.

  
`etag` |  `string` Optional. The current etag of the guardrail. If an etag is not provided, the deletion will overwrite any concurrent changes. If an etag is provided and does not match the current etag of the guardrail, deletion will be blocked and an ABORTED error will be returned.  
  
## DeleteToolRequest

Request message for `[AgentService.DeleteTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.DeleteTool)`.

Fields  
---  
`name` |  `string` Required. The resource name of the tool to delete.  
`force` |  `bool` Optional. Indicates whether to forcefully delete the tool, even if it is still referenced by agents/examples.

  * If `force = false`, the deletion will fail if any agents still reference the tool.
  * If `force = true`, all existing references from agents will be removed and the tool will be deleted.

  
`etag` |  `string` Optional. The current etag of the tool. If an etag is not provided, the deletion will overwrite any concurrent changes. If an etag is provided and does not match the current etag of the tool, deletion will be blocked and an ABORTED error will be returned.  
  
## DeleteToolsetRequest

Request message for `[AgentService.DeleteToolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.DeleteToolset)`.

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
`deployment` |  `[Deployment](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Deployment)` The created deployment.  
  
## Deployment

A deployment represents an immutable, queryable version of the app. It is used to deploy an app version with a specific channel profile.

Fields  
---  
`name` |  `string` Identifier. The resource name of the deployment. Format: `projects/{project}/locations/{location}/apps/{app}/deployments/{deployment}`  
`display_name` |  `string` Required. Display name of the deployment.  
`app_version` |  `string` Optional. The resource name of the app version to deploy. Format: `projects/{project}/locations/{location}/apps/{app}/versions/{version}` Use `projects/{project}/locations/{location}/apps/{app}/versions/-` to use the draft app.  
`channel_profile` |  `[ChannelProfile](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ChannelProfile)` Required. The channel profile used in the deployment.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Timestamp when this deployment was created.  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Timestamp when this deployment was last updated.  
`etag` |  `string` Output only. Etag used to ensure the object hasn't changed during a read-modify-write operation. If the etag is empty, the update will overwrite any concurrent changes.  
`experiment_config` |  `[ExperimentConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ExperimentConfig)` Optional. Experiment configuration for the deployment.  
`whatsapp_credentials` |  `[WhatsAppCredentials](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.WhatsAppCredentials)` Optional. Input only. Ephemeral WhatsApp credentials required when configuring a WhatsApp channel profile.  
`instagram_credentials` |  `[InstagramCredentials](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.InstagramCredentials)` Optional. Input only. Ephemeral Instagram credentials required when configuring a Instagram channel profile.  
`model_settings` |  `[ModelSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ModelSettings)` Optional. Model settings for the deployment. Overrides model settings configured at the app/agent levels. Note: Deployment-level model settings override is gated behind an allowlist. Contact the CXAS team to enable this field.  
`modality` |  `[Deployment.Modality](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Deployment.Modality)` Optional. The modality of the deployment. Note: Deployment-level modality override is gated behind an allowlist. Contact the CXAS team to enable this field.  
`agent_registry_deployment` |  `[AgentRegistryDeployment](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentRegistryDeployment)` Optional. Configuration for deploying this deployment to Agent Registry. If present, this deployment will be published to Agent Registry.  
  
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
`oauth2_auth_code_config` |  `[EndUserAuthConfig.Oauth2AuthCodeConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.EndUserAuthConfig.Oauth2AuthCodeConfig)` Oauth 2.0 Authorization Code authentication.  
`oauth2_jwt_bearer_config` |  `[EndUserAuthConfig.Oauth2JwtBearerConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.EndUserAuthConfig.Oauth2JwtBearerConfig)` JWT Profile Oauth 2.0 Authorization Grant authentication.  
  
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
`enforcement_scope` |  `[EndpointControlPolicy.EnforcementScope](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.EndpointControlPolicy.EnforcementScope)` Optional. The scope in which this policy's allowed_origins list is enforced.  
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
`error_handling_strategy` |  `[ErrorHandlingSettings.ErrorHandlingStrategy](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ErrorHandlingSettings.ErrorHandlingStrategy)` Optional. The strategy to use for error handling.  
`fallback_response_config` |  `[ErrorHandlingSettings.FallbackResponseConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ErrorHandlingSettings.FallbackResponseConfig)` Optional. Configuration for handling fallback responses.  
`end_session_config` |  `[ErrorHandlingSettings.EndSessionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ErrorHandlingSettings.EndSessionConfig)` Optional. Configuration for ending the session in case of system errors (e.g. LLM errors).  
  
## EndSessionConfig

Configuration for ending the session in case of system errors (e.g. LLM errors).

Fields  
---  
`escalate_session` |  `bool` Optional. Whether to escalate the session in `[EndSession](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.EndSession)`. If session is escalated, `[metadata in EndSession](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.EndSession.FIELDS.google.protobuf.Struct.google.cloud.ces.v1.EndSession.metadata)` will contain `session_escalated = true`. See <https://docs.cloud.google.com/customer-engagement-ai/conversational-agents/ps/deploy/google-telephony-platform#transfer_a_call_to_a_human_agent> for details.  
  
## ErrorHandlingStrategy

Defines the strategy for handling errors.

Enums  
---  
`ERROR_HANDLING_STRATEGY_UNSPECIFIED` | Unspecified error handling strategy.  
`NONE` | No specific handling is enabled.  
`FALLBACK_RESPONSE` | A fallback message will be returned to the user in case of system errors (e.g. LLM errors).  
`END_SESSION` | An `[EndSession](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.EndSession)` signal will be emitted in case of system errors (e.g. LLM errors).  
  
## FallbackResponseConfig

Configuration for handling fallback responses.

Fields  
---  
`custom_fallback_messages` |  `map<string, string>` Optional. The fallback messages in case of system errors (e.g. LLM errors), mapped by [supported language code](https://docs.cloud.google.com/customer-engagement-ai/conversational-agents/ps/reference/language).  
`max_fallback_attempts` |  `int32` Optional. The maximum number of fallback attempts to make before the agent emitting `[EndSession](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.EndSession)` Signal.  
  
## EvaluationMetricsThresholds

Threshold settings for metrics in an Evaluation.

Fields  
---  
`golden_evaluation_metrics_thresholds` |  `[EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds)` Optional. The golden evaluation metrics thresholds.  
`hallucination_metric_behavior  
**(deprecated)**` |  `[EvaluationMetricsThresholds.HallucinationMetricBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.EvaluationMetricsThresholds.HallucinationMetricBehavior)` This item is deprecated!Optional. Deprecated: Use `golden_hallucination_metric_behavior` instead. The hallucination metric behavior is currently used for golden evaluations.  
`golden_hallucination_metric_behavior` |  `[EvaluationMetricsThresholds.HallucinationMetricBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.EvaluationMetricsThresholds.HallucinationMetricBehavior)` Optional. The hallucination metric behavior for golden evaluations.  
`scenario_hallucination_metric_behavior` |  `[EvaluationMetricsThresholds.HallucinationMetricBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.EvaluationMetricsThresholds.HallucinationMetricBehavior)` Optional. The hallucination metric behavior for scenario evaluations.  
  
## GoldenEvaluationMetricsThresholds

Settings for golden evaluations.

Fields  
---  
`turn_level_metrics_thresholds` |  `[EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.TurnLevelMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.TurnLevelMetricsThresholds)` Optional. The turn level metrics thresholds.  
`expectation_level_metrics_thresholds` |  `[EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.ExpectationLevelMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.ExpectationLevelMetricsThresholds)` Optional. The expectation level metrics thresholds.  
`tool_matching_settings` |  `[EvaluationMetricsThresholds.ToolMatchingSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.EvaluationMetricsThresholds.ToolMatchingSettings)` Optional. The tool matching settings. An extra tool call is a tool call that is present in the execution but does not match any tool call in the golden expectation.  
  
## ExpectationLevelMetricsThresholds

Expectation level metrics thresholds.

Fields  
---  
`tool_invocation_parameter_correctness_threshold` |  `float` Optional. The success threshold for individual tool invocation parameter correctness. Must be a float between 0 and 1. Default is 1.0.  
  
## TurnLevelMetricsThresholds

Turn level metrics thresholds.

Fields  
---  
`semantic_similarity_channel` |  `[EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.TurnLevelMetricsThresholds.SemanticSimilarityChannel](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.TurnLevelMetricsThresholds.SemanticSimilarityChannel)` Optional. The semantic similarity channel to use for evaluation.  
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
`extra_tool_call_behavior` |  `[EvaluationMetricsThresholds.ToolMatchingSettings.ExtraToolCallBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.EvaluationMetricsThresholds.ToolMatchingSettings.ExtraToolCallBehavior)` Optional. Behavior for extra tool calls. Defaults to FAIL.  
  
## ExtraToolCallBehavior

Defines the behavior when an extra tool call is encountered. An extra tool call is a tool call that is present in the execution but does not match any tool call in the golden expectation.

Enums  
---  
`EXTRA_TOOL_CALL_BEHAVIOR_UNSPECIFIED` | Unspecified behavior. Defaults to FAIL.  
`FAIL` | Fail the evaluation if an extra tool call is encountered.  
`ALLOW` | Allow the extra tool call.  
  
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
`messages[]` |  `[Message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Message)` Optional. The collection of messages that make up the conversation.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Timestamp when the example was created.  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Timestamp when the example was last updated.  
`invalid` |  `bool` Output only. The example may become invalid if referencing resources are deleted. Invalid examples will not be used as few-shot examples.  
`etag` |  `string` Etag used to ensure the object hasn't changed during a read-modify-write operation. If the etag is empty, the update will overwrite any concurrent changes.  
  
## ExecuteToolRequest

Request message for `[ToolService.ExecuteTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ToolService.ExecuteTool)`.

Fields  
---  
`parent` |  `string` Required. The resource name of the app which the tool/toolset belongs to. Format: `projects/{project}/locations/{location}/apps/{app}`  
`args` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` Optional. The input parameters and values for the tool in JSON object format.  
`mock_config` |  `[MockConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.MockConfig)` Optional. Mock configuration for the tool execution. If this field is set, tools that call other tools will be mocked based on the provided patterns and responses.  
Union field `tool_identifier`. The identifier of the tool to execute. It could be either a persisted tool or a tool from a toolset. `tool_identifier` can be only one of the following:  
`tool` |  `string` Optional. The name of the tool to execute. Format: projects/{project}/locations/{location}/apps/{app}/tools/{tool}  
`toolset_tool` |  `[ToolsetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ToolsetTool)` Optional. The toolset tool to execute. Only one tool should match the predicate from the toolset. Otherwise, an error will be returned.  
Union field `tool_execution_context`. Additional context to be provided for the tool execution `tool_execution_context` can be only one of the following:  
`variables` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` Optional. The variables that are available for the tool execution.  
`context` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` Optional. The [ToolCallContext](<https://docs.cloud.google.com/customer-engagement-ai/conversational-agents/ps/tool/python#environment> for details) to be passed to the Python tool.  
  
## ExecuteToolResponse

Response message for `[ToolService.ExecuteTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ToolService.ExecuteTool)`.

Fields  
---  
`response` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` The tool execution result in JSON object format. Use "output" key to specify tool response and "error" key to specify error details (if any). If "output" and "error" keys are not specified, then whole "response" is treated as tool execution result.  
`variables` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` The variable values at the end of the tool execution.  
`citations` |  `[Citations](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Citations)` Citations that provide the source information for the tool's execution.  
`google_search_suggestions` |  `[GoogleSearchSuggestions](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.GoogleSearchSuggestions)` The suggestions returned from Google Search as a result of invoking the Google Search Tool during the tool execution.  
Union field `tool_identifier`. The identifier of the tool that got executed. `tool_identifier` can be only one of the following:  
`tool` |  `string` The name of the tool that got executed. Format: `projects/{project}/locations/{location}/apps/{app}/tools/{tool}`  
`toolset_tool` |  `[ToolsetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ToolsetTool)` The toolset tool that got executed.  
  
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
`version_release` |  `[ExperimentConfig.VersionRelease](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ExperimentConfig.VersionRelease)` Optional. Version release for the experiment.  
  
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
`state` |  `[ExperimentConfig.State](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ExperimentConfig.State)` Optional. State of the version release.  
`traffic_allocations[]` |  `[ExperimentConfig.VersionRelease.TrafficAllocation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ExperimentConfig.VersionRelease.TrafficAllocation)` Optional. Traffic allocations for the version release.  
  
## TrafficAllocation

Traffic allocation for the version release.

Fields  
---  
`id` |  `string` Optional. Id of the traffic allocation. Free format string, up to 128 characters.  
`traffic_percentage` |  `int32` Optional. Traffic percentage of the traffic allocation. Must be between 0 and 100.  
`app_version` |  `string` Optional. App version of the traffic allocation. Format: `projects/{project}/locations/{location}/apps/{app}/versions/{version}`  
  
## ExportAppRequest

Request message for `[AgentService.ExportApp](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.ExportApp)`.

Fields  
---  
`name` |  `string` Required. The resource name of the app to export.  
`export_format` |  `[ExportAppRequest.ExportFormat](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ExportAppRequest.ExportFormat)` Required. The format to export the app in.  
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

Response message for `[AgentService.ExportApp](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.ExportApp)`.

Fields  
---  
Union field `app`. The exported app. `app` can be only one of the following:  
`app_content` |  `bytes` App folder compressed as a zip file.  
`app_uri` |  `string` The [Google Cloud Storage](https://cloud.google.com/storage/docs/) URI to which the app was exported.  
  
## ExpressionCondition

Expression condition based on session state.

Fields  
---  
`expression` |  `string` Required. The string representation of cloud.api.Expression condition.  
  
## FileSearchTool

The file search tool allows the agent to search across the files uploaded by the app/agent developer. It has presets to give relatively good quality search over the uploaded files and summarization of the retrieved results.

Fields  
---  
`corpus_type` |  `[FileSearchTool.CorpusType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.FileSearchTool.CorpusType)` Optional. The type of the corpus. Default is FULLY_MANAGED.  
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
  
## GenerateChatTokenRequest

Request message for `[WidgetService.GenerateChatToken](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.WidgetService.GenerateChatToken)`.

Fields  
---  
`name` |  `string` Required. The session name to generate the chat token for. Format: projects/{project}/locations/{location}/apps/{app}/sessions/{session}  
`deployment` |  `string` Required. The deployment of the app to use for the session. Format: projects/{project}/locations/{location}/apps/{app}/deployments/{deployment}  
`recaptcha_token` |  `string` Optional. The reCAPTCHA token generated by the client-side chat widget.  
`live_handoff_enabled` |  `bool` Optional. Indicates if live handoff is enabled for the session.  
  
## GenerateChatTokenResponse

Response message for `[WidgetService.GenerateChatToken](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.WidgetService.GenerateChatToken)`.

Fields  
---  
`chat_token` |  `string` The session scoped token for chat widget to authenticate with Session APIs.  
`expire_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` The time at which the chat token expires.  
  
## GetAgentRequest

Request message for `[AgentService.GetAgent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.GetAgent)`.

Fields  
---  
`name` |  `string` Required. The resource name of the agent to retrieve.  
  
## GetAppRequest

Request message for `[AgentService.GetApp](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.GetApp)`.

Fields  
---  
`name` |  `string` Required. The resource name of the app to retrieve.  
  
## GetAppVersionRequest

Request message for `[AgentService.GetAppVersion](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.GetAppVersion)`.

Fields  
---  
`name` |  `string` Required. The resource name of the app version to retrieve.  
  
## GetChangelogRequest

Request message for `[AgentService.GetChangelog](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.GetChangelog)`.

Fields  
---  
`name` |  `string` Required. The resource name of the changelog to retrieve.  
  
## GetConversationRequest

Request message for `[AgentService.GetConversation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.GetConversation)`.

Fields  
---  
`name` |  `string` Required. The resource name of the conversation to retrieve.  
`source  
**(deprecated)**` |  `[Conversation.Source](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Conversation.Source)` This item is deprecated!Optional. Indicate the source of the conversation. If not set, all source will be searched.  
  
## GetDeploymentRequest

Request message for `[AgentService.GetDeployment](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.GetDeployment)`.

Fields  
---  
`name` |  `string` Required. The name of the deployment. Format: `projects/{project}/locations/{location}/apps/{app}/deployments/{deployment}`  
  
## GetExampleRequest

Request message for `[AgentService.GetExample](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.GetExample)`.

Fields  
---  
`name` |  `string` Required. The resource name of the example to retrieve.  
  
## GetGuardrailRequest

Request message for `[AgentService.GetGuardrail](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.GetGuardrail)`.

Fields  
---  
`name` |  `string` Required. The resource name of the guardrail to retrieve.  
  
## GetToolRequest

Request message for `[AgentService.GetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.GetTool)`.

Fields  
---  
`name` |  `string` Required. The resource name of the tool to retrieve.  
  
## GetToolsetRequest

Request message for `[AgentService.GetToolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.GetToolset)`.

Fields  
---  
`name` |  `string` Required. The resource name of the toolset to retrieve.  
  
## GoAway

This type has no fields.

Indicates that the server will disconnect soon and the client should half-close and restart the connection.

## GoogleSearchSuggestions

Search suggestions from `[Google Search Tool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.GoogleSearchTool)`.

Fields  
---  
`htmls[]` |  `string` Compliant HTML and CSS styling for search suggestions. The provided HTML and CSS automatically adapts to your device settings, displaying in either light or dark mode indicated by `@media(prefers-color-scheme)`.  
`web_search_queries[]` |  `[WebSearchQuery](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.WebSearchQuery)` List of queries used to perform the google search along with the search result URIs forming the search suggestions.  
  
## GoogleSearchTool

Represents a tool to perform Google web searches for grounding. See <https://cloud.google.com/customer-engagement-ai/conversational-agents/ps/tool#google-search>.

Fields  
---  
`name` |  `string` Required. The name of the tool.  
`description` |  `string` Optional. Description of the tool's purpose.  
`context_urls[]` |  `string` Optional. Content will be fetched directly from these URLs for context and grounding. Example: "https://example.com/path.html". A maximum of 20 URLs are allowed.  
`preferred_domains[]` |  `string` Optional. Specifies domains to restrict search results to. Example: "example.com", "another.site". A maximum of 20 domains can be specified.  
`exclude_domains[]` |  `string` Optional. List of domains to be excluded from the search results. Example: "example.com". A maximum of 2000 domains can be excluded.  
`prompt_config` |  `[GoogleSearchTool.PromptConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.GoogleSearchTool.PromptConfig)` Optional. Prompt instructions passed to planner on how the search results should be processed for text and voice.  
  
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
`action` |  `[TriggerAction](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.TriggerAction)` Optional. Action to take when the guardrail is triggered.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Timestamp when the guardrail was created.  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Timestamp when the guardrail was last updated.  
`etag` |  `string` Etag used to ensure the object hasn't changed during a read-modify-write operation. If the etag is empty, the update will overwrite any concurrent changes.  
Union field `guardrail_type`. Guardrail type. `guardrail_type` can be only one of the following:  
`content_filter` |  `[Guardrail.ContentFilter](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Guardrail.ContentFilter)` Optional. Guardrail that bans certain content from being used in the conversation.  
`llm_prompt_security` |  `[Guardrail.LlmPromptSecurity](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Guardrail.LlmPromptSecurity)` Optional. Guardrail that blocks the conversation if the prompt is considered unsafe based on the LLM classification.  
`llm_policy` |  `[Guardrail.LlmPolicy](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Guardrail.LlmPolicy)` Optional. Guardrail that blocks the conversation if the LLM response is considered violating the policy based on the LLM classification.  
`model_safety` |  `[Guardrail.ModelSafety](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Guardrail.ModelSafety)` Optional. Guardrail that blocks the conversation if the LLM response is considered unsafe based on the model safety settings.  
`code_callback` |  `[Guardrail.CodeCallback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Guardrail.CodeCallback)` Optional. Guardrail that potentially blocks the conversation based on the result of the callback execution.  
`supervisor` |  `[Guardrail.Supervisor](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Guardrail.Supervisor)` Optional. Guardrail that runs supervisor intervention.  
  
## CodeCallback

Guardrail that blocks the conversation based on the code callbacks provided.

Fields  
---  
`before_agent_callback` |  `[Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Callback)` Optional. The callback to execute before the agent is called. Each callback function is expected to return a structure (e.g., a dict or object) containing at least: - 'decision': Either 'OK' or 'TRIGGER'. - 'reason': A string explaining the decision. A 'TRIGGER' decision may halt further processing.  
`after_agent_callback` |  `[Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Callback)` Optional. The callback to execute after the agent is called. Each callback function is expected to return a structure (e.g., a dict or object) containing at least: - 'decision': Either 'OK' or 'TRIGGER'. - 'reason': A string explaining the decision. A 'TRIGGER' decision may halt further processing.  
`before_model_callback` |  `[Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Callback)` Optional. The callback to execute before the model is called. If there are multiple calls to the model, the callback will be executed multiple times. Each callback function is expected to return a structure (e.g., a dict or object) containing at least: - 'decision': Either 'OK' or 'TRIGGER'. - 'reason': A string explaining the decision. A 'TRIGGER' decision may halt further processing.  
`after_model_callback` |  `[Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Callback)` Optional. The callback to execute after the model is called. If there are multiple calls to the model, the callback will be executed multiple times. Each callback function is expected to return a structure (e.g., a dict or object) containing at least: - 'decision': Either 'OK' or 'TRIGGER'. - 'reason': A string explaining the decision. A 'TRIGGER' decision may halt further processing.  
  
## ContentFilter

Guardrail that bans certain content from being used in the conversation.

Fields  
---  
`banned_contents[]` |  `string` Optional. List of banned phrases. Applies to both user inputs and agent responses.  
`banned_contents_in_user_input[]` |  `string` Optional. List of banned phrases. Applies only to user inputs.  
`banned_contents_in_agent_response[]` |  `string` Optional. List of banned phrases. Applies only to agent responses.  
`match_type` |  `[Guardrail.ContentFilter.MatchType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Guardrail.ContentFilter.MatchType)` Required. Match type for the content filter.  
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
`model_settings` |  `[ModelSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ModelSettings)` Optional. Model settings.  
`prompt` |  `string` Required. Policy prompt.  
`policy_scope` |  `[Guardrail.LlmPolicy.PolicyScope](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Guardrail.LlmPolicy.PolicyScope)` Required. Defines when to apply the policy check during the conversation. If set to `POLICY_SCOPE_UNSPECIFIED`, the policy will be applied to the user input. When applying the policy to the agent response, additional latency will be introduced before the agent can respond.  
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
`default_settings` |  `[Guardrail.LlmPromptSecurity.DefaultSecuritySettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Guardrail.LlmPromptSecurity.DefaultSecuritySettings)` Optional. Use the system's predefined default security settings. To select this mode, include an empty 'default_settings' message in the request. The 'default_prompt_template' field within will be populated by the server in the response.  
`custom_policy` |  `[Guardrail.LlmPolicy](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Guardrail.LlmPolicy)` Optional. Use a user-defined LlmPolicy to configure the security guardrail.  
  
## DefaultSecuritySettings

Configuration for default system security settings.

Fields  
---  
`default_prompt_template` |  `string` Output only. The default prompt template used by the system. This field is for display purposes to show the user what prompt the system uses by default. It is OUTPUT_ONLY.  
  
## ModelSafety

Model safety settings overrides. When this is set, it will override the default settings and trigger the guardrail if the response is considered unsafe.

Fields  
---  
`safety_settings[]` |  `[Guardrail.ModelSafety.SafetySetting](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Guardrail.ModelSafety.SafetySetting)` Required. List of safety settings.  
  
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
`category` |  `[Guardrail.ModelSafety.HarmCategory](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Guardrail.ModelSafety.HarmCategory)` Required. The harm category.  
`threshold` |  `[Guardrail.ModelSafety.HarmBlockThreshold](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Guardrail.ModelSafety.HarmBlockThreshold)` Required. The harm block threshold.  
  
## Supervisor

Guardrail that runs supervisor intervention.

Fields  
---  
`type` |  `[Guardrail.Supervisor.Type](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Guardrail.Supervisor.Type)` Optional. The type of the supervisor.  
`detection_mode` |  `[Guardrail.Supervisor.DetectionMode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Guardrail.Supervisor.DetectionMode)` Optional. The detection mode of the supervisor.  
  
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

Request message for `[AgentService.ImportApp](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.ImportApp)`.

Fields  
---  
`parent` |  `string` Required. The parent resource name with the location of the app to import.  
`display_name` |  `string` Optional. The display name of the app to import. * If the app is created on import, and the display name is specified, the imported app will use this display name. If a conflict is detected with an existing app, a timestamp will be appended to the display name to make it unique. * If the app is a reimport, this field should not be set. Providing a display name during reimport will result in an INVALID_ARGUMENT error.  
`app_id` |  `string` Optional. The ID to use for the imported app. * If not specified, a unique ID will be automatically assigned for the app. * Otherwise, the imported app will use this ID as the final component of its resource name. If an app with the same ID already exists at the specified location in the project, the content of the existing app will be replaced.  
`import_options` |  `[ImportAppRequest.ImportOptions](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ImportAppRequest.ImportOptions)` Optional. Options governing the import process for the app.  
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
`conflict_resolution_strategy` |  `[ImportAppRequest.ImportOptions.ConflictResolutionStrategy](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ImportAppRequest.ImportOptions.ConflictResolutionStrategy)` Optional. The strategy to use when resolving conflicts during import.  
`validate_only` |  `bool` Optional. Flag for dry-running the import process. If set to true, the import process will only perform validations and will not make any changes to the existing app or create a new one.  
  
## ConflictResolutionStrategy

Defines the strategy for handling conflicts when an app with the same ID already exists, or when imported resources (like Agents, Tools, etc.) have the same display names as existing resources within that app.

Enums  
---  
`CONFLICT_RESOLUTION_STRATEGY_UNSPECIFIED` | The conflict resolution strategy is unspecified.  
`REPLACE` | Replace existing data with imported data. If an app with the same `app_id` already exists, its content will be updated based on the imported app. - Resources (App, Agents, Tools, Examples, Guardrails, Toolsets) in the imported app that have the same display name as existing resources will overwrite the existing ones. - Imported resources with new display names will be created. - Existing resources that do not have a matching display name in the imported app will remain untouched.  
`OVERWRITE` | Overwrite existing data with imported data. If an app with the same `app_id` already exists, its content will be overwritten with the imported app. - Existing resources (Agents, Tools, Examples, Guardrails, Toolsets) in the app will be deleted. - Imported resources will be created as new resources.  
  
## ImportAppResponse

Response message for `[AgentService.ImportApp](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.ImportApp)`.

Fields  
---  
`name` |  `string` The resource name of the app that was imported.  
`warnings[]` |  `string` Warning messages generated during the import process. If errors occur for specific resources, they will not be included in the imported app and the error will be mentioned here.  
  
## InputAudioConfig

InputAudioConfig configures how the CES agent should interpret the incoming audio data.

Fields  
---  
`audio_encoding` |  `[AudioEncoding](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AudioEncoding)` Required. The encoding of the input audio data.  
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
**(deprecated)**` |  `string` This item is deprecated!Optional. Deprecated: This feature is no longer supported. Use `enable_multilingual_support` instead to improve handling of multilingual input. The action to perform when an agent receives input in an unsupported language.This can be a predefined action or a custom tool call. Valid values are: - A tool's full resource name, which triggers a specific tool execution. - A predefined system action, such as "escalate" or "exit", which triggers an `[EndSession](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.EndSession)` signal with corresponding `[metadata](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.EndSession.FIELDS.google.protobuf.Struct.google.cloud.ces.v1.EndSession.metadata)` to terminate the conversation.  
  
## ListAgentsRequest

Request message for `[AgentService.ListAgents](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.ListAgents)`.

Fields  
---  
`parent` |  `string` Required. The resource name of the app to list agents from.  
`page_size` |  `int32` Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.  
`page_token` |  `string` Optional. The `[next_page_token](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ListAgentsResponse.FIELDS.string.google.cloud.ces.v1.ListAgentsResponse.next_page_token)` value returned from a previous list `[AgentService.ListAgents](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.ListAgents)` call.  
`filter` |  `string` Optional. Filter to be applied when listing the agents. See <https://google.aip.dev/160> for more details.  
`order_by` |  `string` Optional. Field to sort by. Only "name" and "create_time" is supported. See <https://google.aip.dev/132#ordering> for more details.  
  
## ListAgentsResponse

Response message for `[AgentService.ListAgents](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.ListAgents)`.

Fields  
---  
`agents[]` |  `[Agent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Agent)` The list of agents.  
`next_page_token` |  `string` A token that can be sent as `[ListAgentsRequest.page_token](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ListAgentsRequest.FIELDS.string.google.cloud.ces.v1.ListAgentsRequest.page_token)` to retrieve the next page. Absence of this field indicates there are no subsequent pages.  
  
## ListAppVersionsRequest

Request message for `[AgentService.ListAppVersions](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.ListAppVersions)`.

Fields  
---  
`parent` |  `string` Required. The resource name of the app to list app versions from.  
`page_size` |  `int32` Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.  
`page_token` |  `string` Optional. The `[next_page_token](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ListAppVersionsResponse.FIELDS.string.google.cloud.ces.v1.ListAppVersionsResponse.next_page_token)` value returned from a previous list `[AgentService.ListAppVersions](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.ListAppVersions)` call.  
`filter` |  `string` Optional. Filter to be applied when listing the app versions. See <https://google.aip.dev/160> for more details.  
`order_by` |  `string` Optional. Field to sort by. Only "name" and "create_time" is supported. See <https://google.aip.dev/132#ordering> for more details.  
  
## ListAppVersionsResponse

Response message for `[AgentService.ListAppVersions](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.ListAppVersions)`.

Fields  
---  
`app_versions[]` |  `[AppVersion](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AppVersion)` The list of app versions.  
`next_page_token` |  `string` A token that can be sent as `[ListAppVersionsRequest.page_token](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ListAppVersionsRequest.FIELDS.string.google.cloud.ces.v1.ListAppVersionsRequest.page_token)` to retrieve the next page. Absence of this field indicates there are no subsequent pages.  
  
## ListAppsRequest

Request message for `[AgentService.ListApps](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.ListApps)`.

Fields  
---  
`parent` |  `string` Required. The resource name of the location to list apps from.  
`page_size` |  `int32` Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.  
`page_token` |  `string` Optional. The `[next_page_token](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ListAppsResponse.FIELDS.string.google.cloud.ces.v1.ListAppsResponse.next_page_token)` value returned from a previous list `[AgentService.ListApps](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.ListApps)` call.  
`filter` |  `string` Optional. Filter to be applied when listing the apps. See <https://google.aip.dev/160> for more details.  
`order_by` |  `string` Optional. Field to sort by. Only "name" and "create_time" is supported. See <https://google.aip.dev/132#ordering> for more details.  
  
## ListAppsResponse

Response message for `[AgentService.ListApps](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.ListApps)`.

Fields  
---  
`apps[]` |  `[App](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.App)` The list of apps.  
`next_page_token` |  `string` A token that can be sent as `[ListAppsRequest.page_token](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ListAppsRequest.FIELDS.string.google.cloud.ces.v1.ListAppsRequest.page_token)` to retrieve the next page. Absence of this field indicates there are no subsequent pages.  
`unreachable[]` |  `string` Unordered list. Locations that could not be reached.  
  
## ListChangelogsRequest

Request message for `[AgentService.ListChangelogs](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.ListChangelogs)`.

Fields  
---  
`parent` |  `string` Required. The resource name of the app to list changelogs from.  
`page_size` |  `int32` Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.  
`page_token` |  `string` Optional. The `[next_page_token](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ListChangelogsResponse.FIELDS.string.google.cloud.ces.v1.ListChangelogsResponse.next_page_token)` value returned from a previous list `[AgentService.ListChangelogs](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.ListChangelogs)` call.  
`filter` |  `string` Optional. Filter to be applied when listing the changelogs. See <https://google.aip.dev/160> for more details.The filter string can be used to filter by `action`, `resource_type`, `resource_name`, `author`, and `create_time`. The `:` comparator can be used for case-insensitive partial matching on string fields, while `=` performs an exact case-sensitive match.Examples: * `action:update` (case-insensitive partial match) * `action="Create"` (case-sensitive exact match) * `resource_type:agent` * `resource_name:my-agent` * `author:me@example.com` * `create_time > "2025-01-01T00:00:00Z"` * `create_time <= "2025-01-01T00:00:00Z" AND resource_type:tool`  
`order_by` |  `string` Optional. Field to sort by. Only "name" and "create_time" is supported. See <https://google.aip.dev/132#ordering> for more details.  
  
## ListChangelogsResponse

Response message for `[AgentService.ListChangelogs](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.ListChangelogs)`.

Fields  
---  
`changelogs[]` |  `[Changelog](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Changelog)` The list of changelogs.  
`next_page_token` |  `string` A token that can be sent as `[ListChangelogsRequest.page_token](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ListChangelogsRequest.FIELDS.string.google.cloud.ces.v1.ListChangelogsRequest.page_token)` to retrieve the next page. Absence of this field indicates there are no subsequent pages.  
  
## ListConversationsRequest

Request message for `[AgentService.ListConversations](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.ListConversations)`.

Fields  
---  
`parent` |  `string` Required. The resource name of the app to list conversations from.  
`page_size` |  `int32` Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.  
`page_token` |  `string` Optional. The `[next_page_token](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ListConversationsResponse.FIELDS.string.google.cloud.ces.v1.ListConversationsResponse.next_page_token)` value returned from a previous list `[AgentService.ListConversations](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.ListConversations)` call.  
`filter` |  `string` Optional. Filter to be applied when listing the conversations. See <https://google.aip.dev/160> for more details.  
`source` |  `[Conversation.Source](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Conversation.Source)` Optional. Indicate the source of the conversation. If not set, Source.Live will be applied by default. Will be deprecated in favor of `sources` field.  
`sources[]` |  `[Conversation.Source](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Conversation.Source)` Optional. Indicate the sources of the conversations. If not set, all available sources will be applied by default.  
  
## ListConversationsResponse

Response message for `[AgentService.ListConversations](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.ListConversations)`.

Fields  
---  
`conversations[]` |  `[Conversation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Conversation)` The list of conversations.  
`next_page_token` |  `string` A token that can be sent as `[ListConversationsRequest.page_token](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ListConversationsRequest.FIELDS.string.google.cloud.ces.v1.ListConversationsRequest.page_token)` to retrieve the next page. Absence of this field indicates there are no subsequent pages.  
  
## ListDeploymentsRequest

Request message for `[AgentService.ListDeployments](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.ListDeployments)`.

Fields  
---  
`parent` |  `string` Required. The parent app. Format: `projects/{project}/locations/{location}/apps/{app}`  
`page_size` |  `int32` Optional. The maximum number of deployments to return. The service may return fewer than this value. If unspecified, at most 50 deployments will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`page_token` |  `string` Optional. A page token, received from a previous `ListDeployments` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `ListDeployments` must match the call that provided the page token.  
`order_by` |  `string` Optional. Field to sort by. Only "name" and "create_time" is supported. See <https://google.aip.dev/132#ordering> for more details.  
  
## ListDeploymentsResponse

Response message for `[AgentService.ListDeployments](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.ListDeployments)`.

Fields  
---  
`deployments[]` |  `[Deployment](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Deployment)` The list of deployments.  
`next_page_token` |  `string` A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
## ListExamplesRequest

Request message for `[AgentService.ListExamples](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.ListExamples)`.

Fields  
---  
`parent` |  `string` Required. The resource name of the app to list examples from.  
`page_size` |  `int32` Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.  
`page_token` |  `string` Optional. The `[next_page_token](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ListExamplesResponse.FIELDS.string.google.cloud.ces.v1.ListExamplesResponse.next_page_token)` value returned from a previous list `[AgentService.ListExamples](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.ListExamples)` call.  
`filter` |  `string` Optional. Filter to be applied when listing the examples. See <https://google.aip.dev/160> for more details.  
`order_by` |  `string` Optional. Field to sort by. Only "name" and "create_time" is supported. See <https://google.aip.dev/132#ordering> for more details.  
  
## ListExamplesResponse

Response message for `[AgentService.ListExamples](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.ListExamples)`.

Fields  
---  
`examples[]` |  `[Example](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Example)` The list of examples.  
`next_page_token` |  `string` A token that can be sent as `[ListExamplesRequest.page_token](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ListExamplesRequest.FIELDS.string.google.cloud.ces.v1.ListExamplesRequest.page_token)` to retrieve the next page. Absence of this field indicates there are no subsequent pages.  
  
## ListGuardrailsRequest

Request message for `[AgentService.ListGuardrails](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.ListGuardrails)`.

Fields  
---  
`parent` |  `string` Required. The resource name of the app to list guardrails from.  
`page_size` |  `int32` Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.  
`page_token` |  `string` Optional. The `[next_page_token](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ListGuardrailsResponse.FIELDS.string.google.cloud.ces.v1.ListGuardrailsResponse.next_page_token)` value returned from a previous list `[AgentService.ListGuardrails](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.ListGuardrails)` call.  
`filter` |  `string` Optional. Filter to be applied when listing the guardrails. See <https://google.aip.dev/160> for more details.  
`order_by` |  `string` Optional. Field to sort by. Only "name" and "create_time" is supported. See <https://google.aip.dev/132#ordering> for more details.  
  
## ListGuardrailsResponse

Response message for `[AgentService.ListGuardrails](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.ListGuardrails)`.

Fields  
---  
`guardrails[]` |  `[Guardrail](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Guardrail)` The list of guardrails.  
`next_page_token` |  `string` A token that can be sent as `[ListGuardrailsRequest.page_token](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ListGuardrailsRequest.FIELDS.string.google.cloud.ces.v1.ListGuardrailsRequest.page_token)` to retrieve the next page. Absence of this field indicates there are no subsequent pages.  
  
## ListToolsRequest

Request message for `[AgentService.ListTools](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.ListTools)`.

Fields  
---  
`parent` |  `string` Required. The resource name of the app to list tools from.  
`page_size` |  `int32` Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.  
`page_token` |  `string` Optional. The `[next_page_token](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ListToolsResponse.FIELDS.string.google.cloud.ces.v1.ListToolsResponse.next_page_token)` value returned from a previous list `[AgentService.ListTools](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.ListTools)` call.  
`filter` |  `string` Optional. Filter to be applied when listing the tools. Use "include_system_tools=true" to include system tools in the response. See <https://google.aip.dev/160> for more details.  
`order_by` |  `string` Optional. Field to sort by. Only "name" and "create_time" is supported. See <https://google.aip.dev/132#ordering> for more details.  
  
## ListToolsResponse

Response message for `[AgentService.ListTools](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.ListTools)`.

Fields  
---  
`tools[]` |  `[Tool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Tool)` The list of tools.  
`next_page_token` |  `string` A token that can be sent as `[ListToolsRequest.page_token](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ListToolsRequest.FIELDS.string.google.cloud.ces.v1.ListToolsRequest.page_token)` to retrieve the next page. Absence of this field indicates there are no subsequent pages.  
  
## ListToolsetsRequest

Request message for `[AgentService.ListToolsets](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.ListToolsets)`.

Fields  
---  
`parent` |  `string` Required. The resource name of the app to list toolsets from.  
`page_size` |  `int32` Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.  
`page_token` |  `string` Optional. The `[next_page_token](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ListToolsetsResponse.FIELDS.string.google.cloud.ces.v1.ListToolsetsResponse.next_page_token)` value returned from a previous list `[AgentService.ListToolsets](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.ListToolsets)` call.  
`filter` |  `string` Optional. Filter to be applied when listing the toolsets. See <https://google.aip.dev/160> for more details.  
`order_by` |  `string` Optional. Field to sort by. Only "name" and "create_time" is supported. See <https://google.aip.dev/132#ordering> for more details.  
  
## ListToolsetsResponse

Response message for `[AgentService.ListToolsets](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.ListToolsets)`.

Fields  
---  
`toolsets[]` |  `[Toolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Toolset)` The list of toolsets.  
`next_page_token` |  `string` A token that can be sent as `[ListToolsetsRequest.page_token](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ListToolsetsRequest.FIELDS.string.google.cloud.ces.v1.ListToolsetsRequest.page_token)` to retrieve the next page. Absence of this field indicates there are no subsequent pages.  
  
## LoggingSettings

Settings to describe the logging behaviors for the app.

Fields  
---  
`redaction_config` |  `[RedactionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.RedactionConfig)` Optional. Configuration for how sensitive data should be redacted.  
`audio_recording_config` |  `[AudioRecordingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AudioRecordingConfig)` Optional. Configuration for how audio interactions should be recorded. The audio is subject to redaction as configured in `[RedactionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.LoggingSettings.FIELDS.google.cloud.ces.v1.RedactionConfig.google.cloud.ces.v1.LoggingSettings.redaction_config)`.  
`unredacted_audio_recording_config` |  `[AudioRecordingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AudioRecordingConfig)` Optional. Configures an additional recording of unredacted audio. This can be used to maintain a raw audio copy when audio redaction is `[enabled](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.RedactionConfig.FIELDS.bool.google.cloud.ces.v1.RedactionConfig.enable_redaction)`, typically for auditing or monitoring purposes.  
`bigquery_export_settings` |  `[BigQueryExportSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.BigQueryExportSettings)` Optional. Configures the BigQuery export behaviors for the app. The conversation data is subject to redaction as configured in `[RedactionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.LoggingSettings.FIELDS.google.cloud.ces.v1.RedactionConfig.google.cloud.ces.v1.LoggingSettings.redaction_config)`.  
`unredacted_bigquery_export_settings` |  `[BigQueryExportSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.BigQueryExportSettings)` Optional. Configures the BigQuery export behaviors for the app. The unredacted conversation data will be exported to BigQuery tables if it is enabled.  
`cloud_logging_settings` |  `[CloudLoggingSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.CloudLoggingSettings)` Optional. Settings to describe the Cloud Logging behaviors for the app.  
`conversation_logging_settings` |  `[ConversationLoggingSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ConversationLoggingSettings)` Optional. Settings to describe the conversation logging behaviors for the app.  
`evaluation_audio_recording_config` |  `[AudioRecordingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AudioRecordingConfig)` Optional. Configuration for how audio interactions should be recorded for the evaluation. By default, audio recording is not enabled for evaluation sessions.  
`metric_analysis_settings` |  `[MetricAnalysisSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.MetricAnalysisSettings)` Optional. Settings to describe the conversation data collection behaviors for the LLM analysis pipeline for the app.  
  
## McpTool

An MCP tool. See <https://modelcontextprotocol.io/specification/2025-06-18/server/tools> for more details.

Fields  
---  
`name` |  `string` Required. The name of the MCP tool.  
`name_override` |  `string` Optional. The name override of the MCP tool. This is populated if the name was overridden by a Toolset override.  
`description` |  `string` Optional. The description of the MCP tool.  
`input_schema` |  `[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Schema)` Optional. The schema of the input arguments of the MCP tool.  
`output_schema` |  `[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Schema)` Optional. The schema of the output arguments of the MCP tool.  
`server_address` |  `string` Required. The server address of the MCP server, e.g., "https://example.com/mcp/". If the server is built with the MCP SDK, the url should be suffixed with "/mcp/". Only Streamable HTTP transport based servers are supported. This is the same as the server_address in the McpToolset. See <https://modelcontextprotocol.io/specification/2025-03-26/basic/transports#streamable-http> for more details.  
`api_authentication` |  `[ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ApiAuthentication)` Optional. Authentication information required to execute the tool against the MCP server. For bearer token authentication, the token applies only to tool execution, not to listing tools. This requires that tools can be listed without authentication.  
`tls_config` |  `[TlsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.TlsConfig)` Optional. The TLS configuration. Includes the custom server certificates that the client should trust.  
`service_directory_config` |  `[ServiceDirectoryConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ServiceDirectoryConfig)` Optional. Service Directory configuration for VPC-SC, used to resolve service names within a perimeter.  
`custom_headers` |  `map<string, string>` Optional. The custom headers to send in the request to the MCP server. The values must be in the format `$context.variables.<name_of_variable>` and can be set in the session variables. See <https://docs.cloud.google.com/customer-engagement-ai/conversational-agents/ps/tool/open-api#openapi-injection> for more details.  
`state` |  `[McpTool.State](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.McpTool.State)` Output only. The dynamic availability state of the tool on the external server.  
  
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
`input_schema` |  `[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Schema)` Output only. The schema of the input arguments of the MCP tool.  
`output_schema` |  `[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Schema)` Output only. The schema of the output arguments of the MCP tool.  
  
## McpToolOverride

Overrides associated with a given tool in a Toolset. This enables "pinning" or "overriding" of tool definitions from the external dynamic server.

Fields  
---  
`tool` |  `string` Required. The original name of the tool as it is emitted by the MCP server.  
`name_override` |  `string` Optional. If present, this tool uses this name in the Agent instead of the original name. This is primarily used as an alias if the MCP server offers poorly named tools.  
`description_override` |  `string` Optional. If present, this tool uses this description instead of the original description from the server.  
`snapshot` |  `[McpToolDefinition](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.McpToolDefinition)` Output only. If present, this tool is "Pinned" and uses the snapshot values as fallbacks if the server becomes temporarily unavailable or if no Override is present.  
  
## McpToolset

A toolset that contains a list of tools that are offered by the MCP server.

Fields  
---  
`server_address` |  `string` Required. The address of the MCP server, for example, "https://example.com/mcp/". If the server is built with the MCP SDK, the url should be suffixed with "/mcp/". Only Streamable HTTP transport based servers are supported. See <https://modelcontextprotocol.io/specification/2025-03-26/basic/transports#streamable-http> for more details.  
`api_authentication` |  `[ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ApiAuthentication)` Optional. Authentication information required to access tools and execute a tool against the MCP server. For bearer token authentication, the token applies only to tool execution, not to listing tools. This requires that tools can be listed without authentication.  
`service_directory_config` |  `[ServiceDirectoryConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ServiceDirectoryConfig)` Optional. Service Directory configuration for VPC-SC, used to resolve service names within a perimeter.  
`tls_config` |  `[TlsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.TlsConfig)` Optional. The TLS configuration. Includes the custom server certificates that the client should trust.  
`custom_headers` |  `map<string, string>` Optional. The custom headers to send in the request to the MCP server. The values must be in the format `$context.variables.<name_of_variable>` and can be set in the session variables. See <https://docs.cloud.google.com/customer-engagement-ai/conversational-agents/ps/tool/open-api#openapi-injection> for more details.  
`tool_overrides[]` |  `[McpToolOverride](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.McpToolOverride)` Optional. Overrides for individual tools within this toolset. This allows overriding specific details like descriptions, names, or pinning the tools' states so they aren't fully dynamic.  
  
## Message

A message within a conversation.

Fields  
---  
`role` |  `string` Optional. The role within the conversation, e.g., user, agent.  
`chunks[]` |  `[Chunk](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Chunk)` Optional. Content of the message as a series of chunks.  
`event_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Optional. Timestamp when the message was sent or received. Should not be used if the message is part of an `[example](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Example)`.  
  
## MetricAnalysisSettings

Settings to describe the conversation data collection behaviors for LLM analysis metrics pipeline.

Fields  
---  
`llm_metrics_opted_out` |  `bool` Optional. Whether to collect conversation data for llm analysis metrics. If true, conversation data will not be collected for llm analysis metrics; otherwise, conversation data will be collected.  
  
## MockConfig

Mock tool calls configuration for the session.

Fields  
---  
`mocked_tool_calls[]` |  `[MockedToolCall](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.MockedToolCall)` Optional. All tool calls to mock for the duration of the session.  
`unmatched_tool_call_behavior` |  `[MockConfig.UnmatchedToolCallBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.MockConfig.UnmatchedToolCallBehavior)` Required. Beavhior for tool calls that don't match any args patterns in mocked_tool_calls.  
  
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
`toolset` |  `[ToolsetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ToolsetTool)` Optional. The toolset to mock.  
  
## ModelSettings

Model settings contains various configurations for the LLM model.

Fields  
---  
`model` |  `string` Optional. The LLM model that the agent should use. If not set, the agent will inherit the model from its parent agent.  
`thinking_level` |  `[ModelSettings.ThinkingLevel](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ModelSettings.ThinkingLevel)` Optional. The thinking level of the model.  
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
`oauth_grant_type` |  `[OAuthConfig.OauthGrantType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.OAuthConfig.OauthGrantType)` Required. OAuth grant types.  
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
`api_authentication` |  `[ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ApiAuthentication)` Optional. Authentication information required by the API.  
`tls_config` |  `[TlsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.TlsConfig)` Optional. The TLS configuration. Includes the custom server certificates that the client will trust.  
`service_directory_config` |  `[ServiceDirectoryConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ServiceDirectoryConfig)` Optional. Service Directory configuration.  
`ignore_unknown_fields` |  `bool` Optional. If true, the agent will ignore unknown fields in the API response.  
`url` |  `string` Optional. The server URL of the Open API schema. This field is only set in tools in the environment dependencies during the export process if the schema contains a server url. During the import process, if this url is present in the environment dependencies and the schema has the $env_var placeholder, it will replace the placeholder in the schema.  
  
## OpenApiToolset

A toolset that contains a list of tools that are defined by an OpenAPI schema.

Fields  
---  
`open_api_schema` |  `string` Required. The OpenAPI schema of the toolset.  
`api_authentication` |  `[ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ApiAuthentication)` Optional. Authentication information required by the API.  
`tls_config` |  `[TlsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.TlsConfig)` Optional. The TLS configuration. Includes the custom server certificates  
`service_directory_config` |  `[ServiceDirectoryConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ServiceDirectoryConfig)` Optional. Service Directory configuration.  
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
  
## OutputAudioConfig

OutputAudioConfig configures how the CES agent should synthesize outgoing audio responses.

Fields  
---  
`audio_encoding` |  `[AudioEncoding](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AudioEncoding)` Required. The encoding of the output audio data.  
`sample_rate_hertz` |  `int32` Required. The sample rate (in Hertz) of the output audio data.  
  
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
`service_directory_config` |  `[ServiceDirectoryConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ServiceDirectoryConfig)` Optional. Service Directory configuration for the tool.  
  
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
`api_authentication` |  `[ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ApiAuthentication)` Optional. Authentication configuration for calling the remote agent. Optional if the registry reference already handles authentication.  
`input_variable_mapping` |  `map<string, string>` Optional. Mapping of input variable names of remote agent to GECX variable names.  
`output_variable_mapping` |  `map<string, string>` Optional. Mapping of output variable names of remote agent to GECX variable names.  
`streaming_enabled` |  `bool` Optional. Whether streaming is enabled for the remote agent.  
`context_id` |  `string` Optional. If not empty, interactions with the remote A2A agent will use this context ID. This context_id field can refer to a session variable like `$context.variables.order_agent_session_id`.  
Union field `agent_spec`. Specification of the remote agent. `agent_spec` can be only one of the following:  
`agent_card` |  `[AgentCard](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentCard)` Optional. The full agent card defined inline.  
`agent_registry` |  `string` Optional. Reference to the agent in the Agent Registry. Format: `projects/{project}/locations/{location}/agents/{agent}`  
  
## RemoteAgentTool

Represents a tool that allows the agent to call another remote agent.

Fields  
---  
`name` |  `string` Required. The name of the tool.  
`description` |  `string` Required. The description of the tool.  
`agent_card` |  `[AgentCard](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentCard)` Required. The agent card of the remote agent that this tool invokes.  
`api_authentication` |  `[ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ApiAuthentication)` Optional. Authentication configuration for calling the remote agent.  
`stateful_agent` |  `bool` Optional. When enabled, the interaction between the CXAS app and the remote agent will share the same context. If the remote agent returns a context_id, it will be persisted for the entirety of the session for this remote agent tool.  
`input_variable_mapping` |  `map<string, string>` Optional. Mapping of input variable names of remote agent to GECX variable names.  
`output_variable_mapping` |  `map<string, string>` Optional. Mapping of output variable names of remote agent to GECX variable names.  
  
## RestoreAppVersionRequest

Request message for `[AgentService.RestoreAppVersion](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.RestoreAppVersion)`

Fields  
---  
`name` |  `string` Required. The resource name of the app version to restore.  
  
## RestoreAppVersionResponse

This type has no fields.

Response message for `[AgentService.RestoreAppVersion](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.RestoreAppVersion)`

## RetrieveToolSchemaRequest

Request message for `[ToolService.RetrieveToolSchema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ToolService.RetrieveToolSchema)`.

Fields  
---  
`parent` |  `string` Required. The resource name of the app which the tool/toolset belongs to. Format: `projects/{project}/locations/{location}/apps/{app}`  
Union field `tool_identifier`. The identifier of the tool to retrieve the schema for. It could be either a persisted tool or a tool from a toolset. `tool_identifier` can be only one of the following:  
`tool` |  `string` Optional. The name of the tool to retrieve the schema for. Format: projects/{project}/locations/{location}/apps/{app}/tools/{tool}  
`toolset_tool` |  `[ToolsetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ToolsetTool)` Optional. The toolset tool to retrieve the schema for. Only one tool should match the predicate from the toolset. Otherwise, an error will be returned.  
  
## RetrieveToolSchemaResponse

Response message for `[ToolService.RetrieveToolSchema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ToolService.RetrieveToolSchema)`.

Fields  
---  
`input_schema` |  `[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Schema)` The schema of the tool input parameters.  
`output_schema` |  `[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Schema)` The schema of the tool output parameters.  
Union field `tool_identifier`. The identifier of the tool that the schema is for. `tool_identifier` can be only one of the following:  
`tool` |  `string` The name of the tool that the schema is for. Format: `projects/{project}/locations/{location}/apps/{app}/tools/{tool}`  
`toolset_tool` |  `[ToolsetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ToolsetTool)` The toolset tool that the schema is for.  
  
## RetrieveToolsRequest

Request message for `[ToolService.RetrieveTools](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ToolService.RetrieveTools)`.

Fields  
---  
`toolset` |  `string` Required. The name of the toolset to retrieve the tools for. Format: `projects/{project}/locations/{location}/apps/{app}/toolsets/{toolset}`  
`tool_ids[]` |  `string` Optional. The identifiers of the tools to retrieve from the toolset. If empty, all tools in the toolset will be returned.  
`bypass_persistence_config` |  `bool` Optional. If true, the returned tools will contain raw descriptions and schemas directly from the server, bypassing any stored persistence configurations (overrides/snapshots).  
  
## RetrieveToolsResponse

Response message for `[ToolService.RetrieveTools](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ToolService.RetrieveTools)`.

Fields  
---  
`tools[]` |  `[Tool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Tool)` The list of tools that are included in the specified toolset.  
  
## RunSessionRequest

Request message for `[SessionService.RunSession](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.SessionService.RunSession)`.

Fields  
---  
`config` |  `[SessionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.SessionConfig)` Required. The configuration for the session.  
`inputs[]` |  `[SessionInput](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.SessionInput)` Required. Inputs for the session.  
  
## RunSessionResponse

Response message for `[SessionService.RunSession](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.SessionService.RunSession)`.

Fields  
---  
`outputs[]` |  `[SessionOutput](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.SessionOutput)` Outputs for the session.  
  
## Schema

Represents a select subset of an OpenAPI 3.0 schema object.

Fields  
---  
`type` |  `[Schema.Type](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Schema.Type)` Required. The type of the data.  
`properties` |  `map<string, `[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Schema)`>` Optional. Properties of Type.OBJECT.  
`required[]` |  `string` Optional. Required properties of Type.OBJECT.  
`description` |  `string` Optional. The description of the data.  
`items` |  `[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Schema)` Optional. Schema of the elements of Type.ARRAY.  
`nullable` |  `bool` Optional. Indicates if the value may be null.  
`unique_items` |  `bool` Optional. Indicate the items in the array must be unique. Only applies to TYPE.ARRAY.  
`prefix_items[]` |  `[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Schema)` Optional. Schemas of initial elements of Type.ARRAY.  
`additional_properties` |  `[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Schema)` Optional. Can either be a boolean or an object, controls the presence of additional properties.  
`any_of[]` |  `[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Schema)` Optional. The value should be validated against any (one or more) of the subschemas in the list.  
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
`defs` |  `map<string, `[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Schema)`>` Optional. A map of definitions for use by `ref`. Only allowed at the root of the schema.  
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
`endpoint_control_policy` |  `[EndpointControlPolicy](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.EndpointControlPolicy)` Optional. Endpoint control related settings.  
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
`input_audio_config` |  `[InputAudioConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.InputAudioConfig)` Optional. Configuration for processing the input audio.  
`output_audio_config` |  `[OutputAudioConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.OutputAudioConfig)` Optional. Configuration for generating the output audio.  
`historical_contexts[]` |  `[Message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Message)` Optional. The historical context of the session, including user inputs, agent responses, and other messages. Typically, CES agent would manage session automatically so client doesn't need to explicitly populate this field. However, client can optionally override the historical contexts to force the session start from certain state.  
`entry_agent` |  `string` Optional. The entry agent to handle the session. If not specified, the session will be handled by the `[root agent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.App.FIELDS.string.google.cloud.ces.v1.App.root_agent)` of the app. Format: `projects/{project}/locations/{location}/apps/{app}/agents/{agent}`  
`deployment` |  `string` Optional. The deployment of the app to use for the session. Format: `projects/{project}/locations/{location}/apps/{app}/deployments/{deployment}`  
`time_zone` |  `string` Optional. The time zone of the user. If provided, the agent will use the time zone for date and time related variables. Otherwise, the agent will use the time zone specified in the App.time_zone_settings.The format is the IANA Time Zone Database time zone, e.g. "America/Los_Angeles".  
`use_tool_fakes` |  `bool` Optional. Whether to use tool fakes for the session. If this field is set, the agent will attempt use tool fakes instead of calling the real tools.  
`remote_dialogflow_query_parameters` |  `[SessionConfig.RemoteDialogflowQueryParameters](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.SessionConfig.RemoteDialogflowQueryParameters)` Optional. [QueryParameters](https://cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#queryparameters) to send to the remote [Dialogflow](https://cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents) agent when the session control is transferred to the remote agent.  
`enable_text_streaming` |  `bool` Optional. Whether to enable streaming text outputs from the model. By default, text outputs from the model are collected before sending to the client. NOTE: This is only supported for text (non-voice) sessions via `[StreamRunSession](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.SessionService.StreamRunSession)` or `[BidiRunSession](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.SessionService.BidiRunSession)`.  
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
`tool_responses` |  `[ToolResponses](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ToolResponses)` Optional. Execution results for the tool calls from the client.  
`image` |  `[Image](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Image)` Optional. Image data from the end user.  
`blob` |  `[Blob](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Blob)` Optional. Blob data from the end user.  
`variables` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` Optional. Contextual variables for the session, keyed by name. Only variables declared in the app will be used by the CES agent.Unrecognized variables will still be sent to the [Dialogflow agent][Agent.RemoteDialogflowAgent] as additional session parameters.  
`event` |  `[Event](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Event)` Optional. Event input.  
  
## SessionOutput

Output for the session.

Fields  
---  
`turn_index` |  `int32` Indicates the sequential order of conversation turn to which this output belongs to, starting from 1.  
`turn_completed` |  `bool` If true, the CES agent has detected the end of the current conversation turn and will provide no further output for this turn.  
`diagnostic_info` |  `[SessionOutput.DiagnosticInfo](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.SessionOutput.DiagnosticInfo)` Optional. Diagnostic information contains execution details during the processing of the input. Only populated in the last SessionOutput (with `turn_completed=true`) for each turn.  
Union field `output_type`. The type of the output. `output_type` can be only one of the following:  
`text` |  `string` Output text from the CES agent.  
`audio` |  `bytes` Output audio from the CES agent.  
`tool_calls` |  `[ToolCalls](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ToolCalls)` Request for the client to execute the tools.  
`citations` |  `[Citations](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Citations)` Citations that provide the source information for the agent's generated text.  
`google_search_suggestions` |  `[GoogleSearchSuggestions](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.GoogleSearchSuggestions)` The suggestions returned from Google Search as a result of invoking the `[GoogleSearchTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.GoogleSearchTool)`.  
`end_session` |  `[EndSession](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.EndSession)` Indicates the session has ended.  
`payload` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` Custom payload with structured output from the CES agent.  
`image` |  `[Image](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Image)` Output image from the CES agent.  
`progress` |  `string` Intermediate progress update from the CES agent.  
  
## DiagnosticInfo

Contains execution details during the processing.

Fields  
---  
`messages[]` |  `[Message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Message)` List of the messages that happened during the processing.  
`root_span` |  `[Span](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Span)` A trace of the entire request processing, represented as a root span. This span can contain nested child spans for specific operations.  
  
## Span

A span is a unit of work or a single operation during the request processing.

Fields  
---  
`name` |  `string` Output only. The name of the span.  
`start_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The start time of the span.  
`end_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The end time of the span.  
`duration` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Output only. The duration of the span.  
`attributes` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` Output only. Key-value attributes associated with the span.  
`child_spans[]` |  `[Span](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Span)` Output only. The child spans that are nested under this span.  
  
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
  
## TimeZoneSettings

TimeZone settings of the app.

Fields  
---  
`time_zone` |  `string` Optional. The time zone of the app from the [time zone database](https://www.iana.org/time-zones), e.g., America/Los_Angeles, Europe/Paris.  
  
## TlsConfig

The TLS configuration.

Fields  
---  
`ca_certs[]` |  `[TlsConfig.CaCert](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.TlsConfig.CaCert)` Required. Specifies a list of allowed custom CA certificates for HTTPS verification.  
  
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
`execution_type` |  `[ExecutionType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ExecutionType)` Optional. The execution type of the tool.  
`timeout` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Optional. The timeout for the tool execution. If not set, the default timeout is 30 seconds for `SYNCHRONOUS` tools and 60 seconds for `ASYNCHRONOUS` tools.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Timestamp when the tool was created.  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Timestamp when the tool was last updated.  
`etag` |  `string` Etag used to ensure the object hasn't changed during a read-modify-write operation. If the etag is empty, the update will overwrite any concurrent changes.  
`generated_summary` |  `string` Output only. If the tool is generated by the LLM assistant, this field contains a descriptive summary of the generation.  
`tool_fake_config` |  `[ToolFakeConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ToolFakeConfig)` Optional. Configuration for tool behavior in fake mode.  
`read_only` |  `bool` Output only. Indicates whether the tool is read-only. If true, the tool cannot be modified by the user.  
Union field `tool_type`. The type of the tool. `tool_type` can be only one of the following:  
`client_function` |  `[ClientFunction](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ClientFunction)` Optional. The client function.  
`open_api_tool` |  `[OpenApiTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.OpenApiTool)` Optional. The open API tool.  
`google_search_tool` |  `[GoogleSearchTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.GoogleSearchTool)` Optional. The google search tool.  
`connector_tool` |  `[ConnectorTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ConnectorTool)` Optional. The Integration Connector tool.  
`data_store_tool` |  `[DataStoreTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.DataStoreTool)` Optional. The data store tool.  
`python_function` |  `[PythonFunction](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.PythonFunction)` Optional. The python function tool.  
`mcp_tool` |  `[McpTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.McpTool)` Optional. The MCP tool. An MCP tool cannot be created or updated directly and is managed by the MCP toolset.  
`file_search_tool` |  `[FileSearchTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.FileSearchTool)` Optional. The file search tool.  
`system_tool` |  `[SystemTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.SystemTool)` Optional. The system tool.  
`agent_tool` |  `[AgentTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentTool)` Optional. The agent tool.  
`widget_tool` |  `[WidgetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.WidgetTool)` Optional. The widget tool.  
`remote_agent_tool` |  `[RemoteAgentTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.RemoteAgentTool)` Optional. The remote agent tool.  
  
## ToolCall

Request for the client or the agent to execute the specified tool.

Fields  
---  
`id` |  `string` Optional. The unique identifier of the tool call. If populated, the client should return the execution result with the matching ID in `[ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ToolResponse.FIELDS.string.google.cloud.ces.v1.ToolResponse.id)`.  
`display_name` |  `string` Output only. Display name of the tool.  
`args` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` Optional. The input parameters and values for the tool in JSON object format.  
`parent_tool_call_id` |  `string` Output only. The id of the tool call that caused this one, when it was issued by a sub-agent working on behalf of a parent call. Empty for top-level calls. Lets a client group a sub-agent's work under the call that started it instead of rendering every step as a sibling.  
`agent_name` |  `string` Output only. Human-readable name of the agent that issued this call, e.g. "Contract Architect". Empty when the root agent issued it.  
Union field `tool_identifier`. The identifier of the tool to execute. It could be either a persisted tool or a tool from a toolset. `tool_identifier` can be only one of the following:  
`tool` |  `string` Optional. The name of the tool to execute. Format: `projects/{project}/locations/{location}/apps/{app}/tools/{tool}`  
`toolset_tool` |  `[ToolsetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ToolsetTool)` Optional. The toolset tool to execute.  
  
## ToolCalls

Request for the client to execute the tools and return the execution results before continuing the session.

Fields  
---  
`tool_calls[]` |  `[ToolCall](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ToolCall)` Optional. The list of tool calls to execute.  
  
## ToolFakeConfig

Configuration for tool behavior in fake mode.

Fields  
---  
`enable_fake_mode` |  `bool` Optional. Whether the tool is using fake mode.  
Union field `tool_response`. The response is either static or it is provided by a python function. `tool_response` can be only one of the following:  
`code_block` |  `[CodeBlock](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.CodeBlock)` Optional. Code block which will be executed instead of a real tool call.  
  
## ToolResponse

The execution result of a specific tool from the client or the agent.

Fields  
---  
`id` |  `string` Optional. The matching ID of the `[tool call](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ToolCall)` the response is for.  
`display_name` |  `string` Output only. Display name of the tool.  
`response` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` Required. The tool execution result in JSON object format. Use "output" key to specify tool response and "error" key to specify error details (if any). If "output" and "error" keys are not specified, then whole "response" is treated as tool execution result.  
`parent_tool_call_id` |  `string` Output only. The id of the tool call that caused this one, when it was issued by a sub-agent working on behalf of a parent call. Empty for top-level calls. Lets a client group a sub-agent's work under the call that started it instead of rendering every step as a sibling.  
`agent_name` |  `string` Output only. Human-readable name of the agent that issued this call, e.g. "Contract Architect". Empty when the root agent issued it.  
Union field `tool_identifier`. The identifier of the tool that got executed. It could be either a persisted tool or a tool from a toolset. `tool_identifier` can be only one of the following:  
`tool` |  `string` Optional. The name of the tool to execute. Format: `projects/{project}/locations/{location}/apps/{app}/tools/{tool}`  
`toolset_tool` |  `[ToolsetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ToolsetTool)` Optional. The toolset tool that got executed.  
  
## ToolResponses

Execution results for the requested tool calls from the client.

Fields  
---  
`tool_responses[]` |  `[ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ToolResponse)` Optional. The list of tool execution results.  
  
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
`execution_type` |  `[ExecutionType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ExecutionType)` Optional. The execution type of the tools in the toolset.  
`tool_fake_config` |  `[ToolFakeConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ToolFakeConfig)` Optional. Configuration for tools behavior in fake mode.  
Union field `toolset_type`. The type of the toolset. `toolset_type` can be only one of the following:  
`mcp_toolset` |  `[McpToolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.McpToolset)` Optional. A toolset that contains a list of tools that are offered by the MCP server.  
`open_api_toolset` |  `[OpenApiToolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.OpenApiToolset)` Optional. A toolset that contains a list of tools that are defined by an OpenAPI schema.  
`connector_toolset` |  `[ConnectorToolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ConnectorToolset)` Optional. A toolset that generates tools from an Integration Connectors Connection.  
  
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
`direction` |  `[TransferRule.Direction](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.TransferRule.Direction)` Required. The direction of the transfer.  
Union field `rule_type`. The rule type. `rule_type` can be only one of the following:  
`deterministic_transfer` |  `[TransferRule.DeterministicTransfer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.TransferRule.DeterministicTransfer)` Optional. A rule that immediately transfers to the target agent when the condition is met.  
`disable_planner_transfer` |  `[TransferRule.DisablePlannerTransfer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.TransferRule.DisablePlannerTransfer)` Optional. Rule that prevents the planner from transferring to the target agent.  
  
## DeterministicTransfer

Deterministic transfer rule. When the condition evaluates to true, the transfer occurs.

Fields  
---  
Union field `condition_type`. The condition to evaluate. `condition_type` can be only one of the following:  
`expression_condition` |  `[ExpressionCondition](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ExpressionCondition)` Optional. A rule that evaluates a session state condition. If the condition evaluates to true, the transfer occurs.  
`python_code_condition` |  `[PythonCodeCondition](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.PythonCodeCondition)` Optional. A rule that uses Python code block to evaluate the conditions. If the condition evaluates to true, the transfer occurs.  
  
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
`expression_condition` |  `[ExpressionCondition](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.ExpressionCondition)` Required. If the condition evaluates to true, planner will not be allowed to transfer to the target agent.  
  
## TriggerAction

Action that is taken when a certain precondition is met.

Fields  
---  
Union field `action`. The action to take. `action` can be only one of the following:  
`respond_immediately` |  `[TriggerAction.RespondImmediately](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.TriggerAction.RespondImmediately)` Optional. Immediately respond with a preconfigured response.  
`transfer_agent` |  `[TriggerAction.TransferAgent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.TriggerAction.TransferAgent)` Optional. Transfer the conversation to a different agent.  
`generative_answer` |  `[TriggerAction.GenerativeAnswer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.TriggerAction.GenerativeAnswer)` Optional. Respond with a generative answer.  
  
## GenerativeAnswer

The agent will immediately respond with a generative answer.

Fields  
---  
`prompt` |  `string` Required. The prompt to use for the generative answer.  
  
## RespondImmediately

The agent will immediately respond with a preconfigured response.

Fields  
---  
`responses[]` |  `[TriggerAction.Response](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.TriggerAction.Response)` Required. The canned responses for the agent to choose from. The response is chosen randomly.  
  
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

Request message for `[AgentService.UpdateAgent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.UpdateAgent)`.

Fields  
---  
`agent` |  `[Agent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Agent)` Required. The agent to update.  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Optional. Field mask is used to control which fields get updated. If the mask is not present, all fields will be updated.  
  
## UpdateAppRequest

Request message for `[AgentService.UpdateApp](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.UpdateApp)`.

Fields  
---  
`app` |  `[App](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.App)` Required. The app to update.  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Optional. Field mask is used to control which fields get updated. If the mask is not present, all fields will be updated.  
  
## UpdateAppVersionRequest

Request message for `[AgentService.UpdateAppVersion](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.UpdateAppVersion)`.

Fields  
---  
`app_version` |  `[AppVersion](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AppVersion)` Required. The app version to update.  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Optional. The list of fields to update. If empty, fields `display_name` and `description` will be updated.  
  
## UpdateDeploymentRequest

Request message for `[AgentService.UpdateDeployment](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.UpdateDeployment)`.

Fields  
---  
`deployment` |  `[Deployment](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Deployment)` Required. The deployment to update.  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Optional. The list of fields to update.  
  
## UpdateExampleRequest

Request message for `[AgentService.UpdateExample](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.UpdateExample)`.

Fields  
---  
`example` |  `[Example](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Example)` Required. The example to update.  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Optional. Field mask is used to control which fields get updated. If the mask is not present, all fields will be updated.  
  
## UpdateGuardrailRequest

Request message for `[AgentService.UpdateGuardrail](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.UpdateGuardrail)`.

Fields  
---  
`guardrail` |  `[Guardrail](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Guardrail)` Required. The guardrail to update.  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Optional. Field mask is used to control which fields get updated. If the mask is not present, all fields will be updated.  
  
## UpdateToolRequest

Request message for `[AgentService.UpdateTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.UpdateTool)`.

Fields  
---  
`tool` |  `[Tool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Tool)` Required. The tool to update.  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Optional. Field mask is used to control which fields get updated. If the mask is not present, all fields will be updated.  
  
## UpdateToolsetRequest

Request message for `[AgentService.UpdateToolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.AgentService.UpdateToolset)`.

Fields  
---  
`toolset` |  `[Toolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Toolset)` Required. The toolset to update.  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Optional. Field mask is used to control which fields get updated. If the mask is not present, all fields will be updated.  
  
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
`widget_type` |  `[WidgetTool.WidgetType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.WidgetTool.WidgetType)` Optional. The type of the widget tool. If not specified, the default type will be CUSTOMIZED.  
`ui_config` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` Optional. Configuration for rendering the widget.  
`data_mapping` |  `[WidgetTool.DataMapping](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.WidgetTool.DataMapping)` Optional. The mapping that defines how data from a source tool is mapped to the widget's input parameters.  
`text_response_config` |  `[WidgetTool.TextResponseConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.WidgetTool.TextResponseConfig)` Optional. Configuration for always-included text responses.  
Union field `input`. The input of the widget tool. `input` can be only one of the following:  
`parameters` |  `[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.Schema)` Optional. The input parameters of the widget tool.  
  
## DataMapping

Configuration for mapping data from a source tool to the widget's input parameters.

Fields  
---  
`source_tool_name` |  `string` Optional. The resource name of the tool that provides the data for the widget (e.g., a search tool or a custom function). Format: `projects/{project}/locations/{location}/agents/{agent}/tools/{tool}`  
`field_mappings` |  `map<string, string>` Optional. A map of widget input parameter fields to the corresponding output fields of the source tool.  
`python_function` |  `[PythonFunction](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.PythonFunction)` Optional. Configuration for a Python function used to transform the source tool's output into the widget's input format.  
`mode` |  `[WidgetTool.DataMapping.Mode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.WidgetTool.DataMapping.Mode)` Optional. The mode of the data mapping.  
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
`type` |  `[WidgetTool.TextResponseConfig.Type](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rpc/google.cloud.ces.v1#google.cloud.ces.v1.WidgetTool.TextResponseConfig.Type)` Optional. The strategy for providing the text response.  
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
