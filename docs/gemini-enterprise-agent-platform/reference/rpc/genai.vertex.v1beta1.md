---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1
title: Package genai.vertex.v1beta1 \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:00:04.887540+00:00
---

# Package genai.vertex.v1beta1  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Package genai.vertex.v1beta1 Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[InteractionsHttpService](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.InteractionsHttpService)` (interface)
  * `[AgentInteraction](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.AgentInteraction)` (message)
  * `[AllowedTools](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.AllowedTools)` (message)
  * `[AntigravityAgentConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.AntigravityAgentConfig)` (message)
  * `[ArgumentsDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ArgumentsDelta)` (message)
  * `[AudioContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.AudioContent)` (message)
  * `[AudioContent.MimeType](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.AudioContent.MimeType)` (enum)
  * `[AudioDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.AudioDelta)` (message)
  * `[AudioResponseFormat](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.AudioResponseFormat)` (message)
  * `[AudioResponseFormat.Delivery](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.AudioResponseFormat.Delivery)` (enum)
  * `[AudioResponseFormat.MimeType](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.AudioResponseFormat.MimeType)` (enum)
  * `[CancelInteractionHttpTranscoderRequest](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.CancelInteractionHttpTranscoderRequest)` (message)
  * `[CancelInteractionRequest](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.CancelInteractionRequest)` (message)
  * `[CodeExecution](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.CodeExecution)` (message)
  * `[CodeExecutionCallContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.CodeExecutionCallContent)` (message) **(deprecated)**
  * `[CodeExecutionCallContent.CodeExecutionCallArguments](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.CodeExecutionCallContent.CodeExecutionCallArguments)` (message)
  * `[CodeExecutionCallContent.CodeExecutionCallArguments.Language](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.CodeExecutionCallContent.CodeExecutionCallArguments.Language)` (enum)
  * `[CodeExecutionCallDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.CodeExecutionCallDelta)` (message)
  * `[CodeExecutionCallStep](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.CodeExecutionCallStep)` (message)
  * `[CodeExecutionCallStep.CodeExecutionCallStepArguments](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.CodeExecutionCallStep.CodeExecutionCallStepArguments)` (message)
  * `[CodeExecutionCallStep.CodeExecutionCallStepArguments.Language](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.CodeExecutionCallStep.CodeExecutionCallStepArguments.Language)` (enum)
  * `[CodeExecutionResultContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.CodeExecutionResultContent)` (message) **(deprecated)**
  * `[CodeExecutionResultDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.CodeExecutionResultDelta)` (message)
  * `[CodeExecutionResultStep](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.CodeExecutionResultStep)` (message)
  * `[CodeMenderAgentConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.CodeMenderAgentConfig)` (message)
  * `[CodeMenderAgentConfig.FileContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.CodeMenderAgentConfig.FileContent)` (message)
  * `[CodeMenderAgentConfig.FindRequest](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.CodeMenderAgentConfig.FindRequest)` (message)
  * `[CodeMenderAgentConfig.FindRequest.Mode](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.CodeMenderAgentConfig.FindRequest.Mode)` (enum)
  * `[CodeMenderAgentConfig.FixRequest](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.CodeMenderAgentConfig.FixRequest)` (message)
  * `[CodeMenderAgentConfig.SessionConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.CodeMenderAgentConfig.SessionConfig)` (message)
  * `[ComputerUse](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ComputerUse)` (message)
  * `[ComputerUse.Environment](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ComputerUse.Environment)` (enum)
  * `[ComputerUse.SafetyPolicy](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ComputerUse.SafetyPolicy)` (enum)
  * `[Content](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Content)` (message)
  * `[ContentDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ContentDelta)` (message)
  * `[ContentDeltaData](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ContentDeltaData)` (message)
  * `[ContentList](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ContentList)` (message)
  * `[ContentStart](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ContentStart)` (message)
  * `[ContentStop](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ContentStop)` (message)
  * `[CreateInteractionHttpRequest](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.CreateInteractionHttpRequest)` (message)
  * `[CreateInteractionHttpTranscoderRequest](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.CreateInteractionHttpTranscoderRequest)` (message)
  * `[CreateInteractionRequest](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.CreateInteractionRequest)` (message)
  * `[DeepResearchAgentConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.DeepResearchAgentConfig)` (message)
  * `[DeepResearchAgentConfig.VisualizationMode](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.DeepResearchAgentConfig.VisualizationMode)` (enum)
  * `[DeleteInteractionRequest](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.DeleteInteractionRequest)` (message)
  * `[DeleteInteractionResponse](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.DeleteInteractionResponse)` (message)
  * `[DocumentContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.DocumentContent)` (message)
  * `[DocumentContent.MimeType](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.DocumentContent.MimeType)` (enum)
  * `[DocumentDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.DocumentDelta)` (message)
  * `[DynamicAgentConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.DynamicAgentConfig)` (message)
  * `[EnvironmentConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.EnvironmentConfig)` (message)
  * `[EnvironmentConfig.EgressRule](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.EnvironmentConfig.EgressRule)` (message)
  * `[EnvironmentConfig.EnvironmentNetworkEgressAllowlist](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.EnvironmentConfig.EnvironmentNetworkEgressAllowlist)` (message)
  * `[EnvironmentConfig.NetworkMode](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.EnvironmentConfig.NetworkMode)` (enum)
  * `[EnvironmentConfig.Source](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.EnvironmentConfig.Source)` (message)
  * `[EnvironmentConfig.Source.Type](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.EnvironmentConfig.Source.Type)` (enum)
  * `[Error](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Error)` (message)
  * `[ErrorEvent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ErrorEvent)` (message)
  * `[ExaAISearchConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ExaAISearchConfig)` (message)
  * `[Field](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Field)` (message)
  * `[FileCitation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.FileCitation)` (message)
  * `[FileSearch](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.FileSearch)` (message)
  * `[FileSearchCallContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.FileSearchCallContent)` (message) **(deprecated)**
  * `[FileSearchCallDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.FileSearchCallDelta)` (message)
  * `[FileSearchCallStep](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.FileSearchCallStep)` (message)
  * `[FileSearchResultContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.FileSearchResultContent)` (message) **(deprecated)**
  * `[FileSearchResultContent.FileSearchResult](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.FileSearchResultContent.FileSearchResult)` (message)
  * `[FileSearchResultDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.FileSearchResultDelta)` (message)
  * `[FileSearchResultStep](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.FileSearchResultStep)` (message)
  * `[Function](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Function)` (message)
  * `[FunctionCallContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.FunctionCallContent)` (message) **(deprecated)**
  * `[FunctionCallDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.FunctionCallDelta)` (message)
  * `[FunctionCallStep](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.FunctionCallStep)` (message)
  * `[FunctionResultContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.FunctionResultContent)` (message) **(deprecated)**
  * `[FunctionResultDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.FunctionResultDelta)` (message)
  * `[FunctionResultStep](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.FunctionResultStep)` (message)
  * `[FunctionResultSubcontent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.FunctionResultSubcontent)` (message)
  * `[FunctionResultSubcontentList](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.FunctionResultSubcontentList)` (message)
  * `[GenerationConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GenerationConfig)` (message)
  * `[GetInteractionHttpTranscoderRequest](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GetInteractionHttpTranscoderRequest)` (message)
  * `[GetInteractionRequest](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GetInteractionRequest)` (message)
  * `[GoogleMaps](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GoogleMaps)` (message)
  * `[GoogleMapsCallContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GoogleMapsCallContent)` (message) **(deprecated)**
  * `[GoogleMapsCallContent.GoogleMapsCallArguments](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GoogleMapsCallContent.GoogleMapsCallArguments)` (message)
  * `[GoogleMapsCallDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GoogleMapsCallDelta)` (message)
  * `[GoogleMapsCallStep](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GoogleMapsCallStep)` (message)
  * `[GoogleMapsCallStep.GoogleMapsCallStepArguments](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GoogleMapsCallStep.GoogleMapsCallStepArguments)` (message)
  * `[GoogleMapsResultContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GoogleMapsResultContent)` (message) **(deprecated)**
  * `[GoogleMapsResultContent.GoogleMapsResult](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GoogleMapsResultContent.GoogleMapsResult)` (message)
  * `[GoogleMapsResultContent.GoogleMapsResult.Places](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GoogleMapsResultContent.GoogleMapsResult.Places)` (message)
  * `[GoogleMapsResultDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GoogleMapsResultDelta)` (message)
  * `[GoogleMapsResultStep](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GoogleMapsResultStep)` (message)
  * `[GoogleMapsResultStep.GoogleMapsResultItem](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GoogleMapsResultStep.GoogleMapsResultItem)` (message)
  * `[GoogleMapsResultStep.GoogleMapsResultItem.GoogleMapsResultPlaces](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GoogleMapsResultStep.GoogleMapsResultItem.GoogleMapsResultPlaces)` (message)
  * `[GoogleSearch](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GoogleSearch)` (message)
  * `[GoogleSearch.SearchType](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GoogleSearch.SearchType)` (enum)
  * `[GoogleSearchCallContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GoogleSearchCallContent)` (message) **(deprecated)**
  * `[GoogleSearchCallContent.GoogleSearchCallArguments](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GoogleSearchCallContent.GoogleSearchCallArguments)` (message)
  * `[GoogleSearchCallDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GoogleSearchCallDelta)` (message)
  * `[GoogleSearchCallStep](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GoogleSearchCallStep)` (message)
  * `[GoogleSearchCallStep.GoogleSearchCallStepArguments](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GoogleSearchCallStep.GoogleSearchCallStepArguments)` (message)
  * `[GoogleSearchResultContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GoogleSearchResultContent)` (message) **(deprecated)**
  * `[GoogleSearchResultContent.GoogleSearchResult](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GoogleSearchResultContent.GoogleSearchResult)` (message)
  * `[GoogleSearchResultDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GoogleSearchResultDelta)` (message)
  * `[GoogleSearchResultStep](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GoogleSearchResultStep)` (message)
  * `[GoogleSearchResultStep.GoogleSearchResultItem](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GoogleSearchResultStep.GoogleSearchResultItem)` (message)
  * `[HarmCategory](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.HarmCategory)` (enum)
  * `[ImageConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ImageConfig)` (message) **(deprecated)**
  * `[ImageContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ImageContent)` (message)
  * `[ImageContent.MimeType](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ImageContent.MimeType)` (enum)
  * `[ImageDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ImageDelta)` (message)
  * `[ImageResponseFormat](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ImageResponseFormat)` (message)
  * `[ImageResponseFormat.AspectRatio](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ImageResponseFormat.AspectRatio)` (enum)
  * `[ImageResponseFormat.Delivery](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ImageResponseFormat.Delivery)` (enum)
  * `[ImageResponseFormat.ImageSize](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ImageResponseFormat.ImageSize)` (enum)
  * `[ImageResponseFormat.MimeType](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ImageResponseFormat.MimeType)` (enum)
  * `[Interaction](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Interaction)` (message)
  * `[Interaction.Status](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Interaction.Status)` (enum)
  * `[Interaction.Usage](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Interaction.Usage)` (message)
  * `[Interaction.Usage.GroundingToolCount](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Interaction.Usage.GroundingToolCount)` (message)
  * `[Interaction.Usage.GroundingToolCount.Type](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Interaction.Usage.GroundingToolCount.Type)` (enum)
  * `[Interaction.Usage.ModalityTokens](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Interaction.Usage.ModalityTokens)` (message)
  * `[InteractionCompleteEvent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.InteractionCompleteEvent)` (message) **(deprecated)**
  * `[InteractionCompletedSseEvent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.InteractionCompletedSseEvent)` (message)
  * `[InteractionCreatedSseEvent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.InteractionCreatedSseEvent)` (message)
  * `[InteractionMetadata](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.InteractionMetadata)` (message)
  * `[InteractionStartEvent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.InteractionStartEvent)` (message) **(deprecated)**
  * `[InteractionStatusUpdate](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.InteractionStatusUpdate)` (message)
  * `[InteractionStreamingEvent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.InteractionStreamingEvent)` (message)
  * `[LegacyAudioContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.LegacyAudioContent)` (message) **(deprecated)**
  * `[LegacyDocumentContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.LegacyDocumentContent)` (message) **(deprecated)**
  * `[LegacyImageContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.LegacyImageContent)` (message) **(deprecated)**
  * `[LegacyTextContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.LegacyTextContent)` (message) **(deprecated)**
  * `[LegacyVideoContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.LegacyVideoContent)` (message) **(deprecated)**
  * `[ListInteractionsHttpTranscoderRequest](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ListInteractionsHttpTranscoderRequest)` (message)
  * `[ListInteractionsRequest](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ListInteractionsRequest)` (message)
  * `[ListInteractionsResponse](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ListInteractionsResponse)` (message)
  * `[ListValue](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ListValue)` (message)
  * `[LocalEnvironmentConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.LocalEnvironmentConfig)` (message)
  * `[McpServer](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.McpServer)` (message)
  * `[McpServerToolCallContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.McpServerToolCallContent)` (message)
  * `[McpServerToolCallDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.McpServerToolCallDelta)` (message)
  * `[McpServerToolCallStep](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.McpServerToolCallStep)` (message)
  * `[McpServerToolResultContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.McpServerToolResultContent)` (message)
  * `[McpServerToolResultDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.McpServerToolResultDelta)` (message)
  * `[McpServerToolResultStep](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.McpServerToolResultStep)` (message)
  * `[MediaResolution](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.MediaResolution)` (enum)
  * `[ModelInteraction](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ModelInteraction)` (message)
  * `[ModelOutputStep](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ModelOutputStep)` (message)
  * `[ParallelAISearchConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ParallelAISearchConfig)` (message)
  * `[PlaceCitation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.PlaceCitation)` (message)
  * `[RagStoreConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.RagStoreConfig)` (message)
  * `[RagStoreConfig.RagResource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.RagStoreConfig.RagResource)` (message)
  * `[RagStoreConfig.RagRetrievalConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.RagStoreConfig.RagRetrievalConfig)` (message)
  * `[RagStoreConfig.RagRetrievalConfig.Filter](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.RagStoreConfig.RagRetrievalConfig.Filter)` (message)
  * `[RagStoreConfig.RagRetrievalConfig.HybridSearch](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.RagStoreConfig.RagRetrievalConfig.HybridSearch)` (message)
  * `[RagStoreConfig.RagRetrievalConfig.Ranking](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.RagStoreConfig.RagRetrievalConfig.Ranking)` (message)
  * `[RagStoreConfig.RagRetrievalConfig.Ranking.RankService](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.RagStoreConfig.RagRetrievalConfig.Ranking.RankService)` (message)
  * `[ResponseFormat](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ResponseFormat)` (message)
  * `[ResponseFormatList](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ResponseFormatList)` (message)
  * `[ResponseModality](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ResponseModality)` (enum)
  * `[Retrieval](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Retrieval)` (message)
  * `[Retrieval.RetrievalType](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Retrieval.RetrievalType)` (enum)
  * `[RetrievalCallDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.RetrievalCallDelta)` (message)
  * `[RetrievalCallStep](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.RetrievalCallStep)` (message)
  * `[RetrievalCallStep.RetrievalStepArguments](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.RetrievalCallStep.RetrievalStepArguments)` (message)
  * `[RetrievalResultDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.RetrievalResultDelta)` (message)
  * `[RetrievalResultStep](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.RetrievalResultStep)` (message)
  * `[ReviewSnippet](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ReviewSnippet)` (message)
  * `[SafetySetting](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.SafetySetting)` (message)
  * `[SafetySetting.HarmBlockMethod](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.SafetySetting.HarmBlockMethod)` (enum)
  * `[SafetySetting.HarmBlockThreshold](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.SafetySetting.HarmBlockThreshold)` (enum)
  * `[ServerToolCallDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ServerToolCallDelta)` (message)
  * `[ServerToolResultDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ServerToolResultDelta)` (message)
  * `[Step](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Step)` (message)
  * `[StepDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.StepDelta)` (message)
  * `[StepDeltaData](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.StepDeltaData)` (message)
  * `[StepList](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.StepList)` (message)
  * `[StepStart](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.StepStart)` (message)
  * `[StepStop](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.StepStop)` (message)
  * `[Struct](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Struct)` (message)
  * `[TextAnnotationDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.TextAnnotationDelta)` (message)
  * `[TextContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.TextContent)` (message)
  * `[TextContent.Annotation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.TextContent.Annotation)` (message)
  * `[TextDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.TextDelta)` (message)
  * `[TextResponseFormat](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.TextResponseFormat)` (message)
  * `[TextResponseFormat.MimeType](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.TextResponseFormat.MimeType)` (enum)
  * `[ThinkingLevel](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ThinkingLevel)` (enum)
  * `[ThinkingSummaries](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ThinkingSummaries)` (enum)
  * `[ThoughtContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ThoughtContent)` (message) **(deprecated)**
  * `[ThoughtSignatureDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ThoughtSignatureDelta)` (message)
  * `[ThoughtStep](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ThoughtStep)` (message)
  * `[ThoughtSummaryContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ThoughtSummaryContent)` (message)
  * `[ThoughtSummaryDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ThoughtSummaryDelta)` (message)
  * `[Tool](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Tool)` (message)
  * `[ToolCallContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ToolCallContent)` (message) **(deprecated)**
  * `[ToolCallDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ToolCallDelta)` (message)
  * `[ToolCallStep](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ToolCallStep)` (message)
  * `[ToolChoiceConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ToolChoiceConfig)` (message)
  * `[ToolChoiceType](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ToolChoiceType)` (enum)
  * `[ToolResultContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ToolResultContent)` (message) **(deprecated)**
  * `[ToolResultDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ToolResultDelta)` (message)
  * `[ToolResultStep](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ToolResultStep)` (message)
  * `[TranscriptionConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.TranscriptionConfig)` (message)
  * `[Turn](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Turn)` (message) **(deprecated)**
  * `[TurnList](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.TurnList)` (message) **(deprecated)**
  * `[UrlCitation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.UrlCitation)` (message)
  * `[UrlContext](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.UrlContext)` (message)
  * `[UrlContextCallContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.UrlContextCallContent)` (message) **(deprecated)**
  * `[UrlContextCallContent.UrlContextCallArguments](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.UrlContextCallContent.UrlContextCallArguments)` (message)
  * `[UrlContextCallDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.UrlContextCallDelta)` (message)
  * `[UrlContextCallStep](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.UrlContextCallStep)` (message)
  * `[UrlContextCallStep.UrlContextCallStepArguments](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.UrlContextCallStep.UrlContextCallStepArguments)` (message)
  * `[UrlContextResultContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.UrlContextResultContent)` (message) **(deprecated)**
  * `[UrlContextResultContent.UrlContextResult](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.UrlContextResultContent.UrlContextResult)` (message)
  * `[UrlContextResultContent.UrlContextResult.Status](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.UrlContextResultContent.UrlContextResult.Status)` (enum)
  * `[UrlContextResultDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.UrlContextResultDelta)` (message)
  * `[UrlContextResultStep](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.UrlContextResultStep)` (message)
  * `[UrlContextResultStep.UrlContextResultItem](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.UrlContextResultStep.UrlContextResultItem)` (message)
  * `[UrlContextResultStep.UrlContextResultItem.Status](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.UrlContextResultStep.UrlContextResultItem.Status)` (enum)
  * `[UserInputStep](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.UserInputStep)` (message)
  * `[Value](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Value)` (message)
  * `[VertexAISearchConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.VertexAISearchConfig)` (message)
  * `[VideoConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.VideoConfig)` (message)
  * `[VideoConfig.Task](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.VideoConfig.Task)` (enum)
  * `[VideoContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.VideoContent)` (message)
  * `[VideoContent.MediaProcessing](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.VideoContent.MediaProcessing)` (message)
  * `[VideoContent.MimeType](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.VideoContent.MimeType)` (enum)
  * `[VideoContent.Processing](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.VideoContent.Processing)` (enum)
  * `[VideoContent.StaticMediaProcessing](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.VideoContent.StaticMediaProcessing)` (message)
  * `[VideoDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.VideoDelta)` (message)
  * `[VideoResponseFormat](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.VideoResponseFormat)` (message)
  * `[VideoResponseFormat.AspectRatio](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.VideoResponseFormat.AspectRatio)` (enum)
  * `[VideoResponseFormat.Delivery](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.VideoResponseFormat.Delivery)` (enum)
  * `[VideoResponseFormat.Resolution](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.VideoResponseFormat.Resolution)` (enum)
  * `[WordInfo](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.WordInfo)` (message)



## InteractionsHttpService

API that acts as the transcoder for users to interact with models and agents.

CancelInteractionHttp  
---  
` rpc CancelInteractionHttp(`[CancelInteractionHttpTranscoderRequest](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.CancelInteractionHttpTranscoderRequest)`) returns (`[HttpBody](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/google.api#google.api.HttpBody)`) ` Cancels an interaction.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `aiplatform.interactions.cancel`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
CreateInteractionHttp  
---  
` rpc CreateInteractionHttp(`[CreateInteractionHttpTranscoderRequest](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.CreateInteractionHttpTranscoderRequest)`) returns (`[HttpBody](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/google.api#google.api.HttpBody)`) `

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `aiplatform.interactions.create`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
GetInteractionHttp  
---  
` rpc GetInteractionHttp(`[GetInteractionHttpTranscoderRequest](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GetInteractionHttpTranscoderRequest)`) returns (`[HttpBody](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/google.api#google.api.HttpBody)`) ` Gets an interaction.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `aiplatform.interactions.get`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
ListInteractionsHttp  
---  
` rpc ListInteractionsHttp(`[ListInteractionsHttpTranscoderRequest](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ListInteractionsHttpTranscoderRequest)`) returns (`[HttpBody](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/google.api#google.api.HttpBody)`) ` Lists interactions.

Authorization scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `aiplatform.interactions.list`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
  
## AgentInteraction

Interaction for generating the completion using agents.

Fields  
---  
`agent` |  `string` The name of the `Agent` used for generating the completion.  
Union field `agent_config`. Configuration parameters for the agent interaction. `agent_config` can be only one of the following:  
`dynamic_config` |  `[DynamicAgentConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.DynamicAgentConfig)`  
`deep_research_config` |  `[DeepResearchAgentConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.DeepResearchAgentConfig)`  
`code_mender_config` |  `[CodeMenderAgentConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.CodeMenderAgentConfig)`  
`antigravity_config` |  `[AntigravityAgentConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.AntigravityAgentConfig)` Antigravity agent configuration. This configuration is session-level settings that are passed to the agent runtime on a per-request basis.  
  
## AllowedTools

The configuration for allowed tools.

Fields  
---  
`mode` |  `[ToolChoiceType](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ToolChoiceType)` The mode of the tool choice.  
`tools[]` |  `string` The names of the allowed tools.  
  
## AntigravityAgentConfig

Configuration for the Antigravity agent runtime. Provides server-side control over the agent's execution environment and tool configuration.

Fields  
---  
`max_total_tokens` |  `int64` Max total tokens for the agent run.  
Union field `model_config`.`model_config` can be only one of the following:  
`model` |  `string` The model to use for agent reasoning.  
  
## ArgumentsDelta

Fields  
---  
`arguments` |  `string`  
  
## AudioContent

An audio content block.

Fields  
---  
`mime_type_string` |  `string` Flexible MIME type string of the audio, superseding mime_type = 1. Note: Bespoke logic in the GAOS parser/serializer maps this to the "mime_type" JSON key.  
`channels` |  `int32` The number of audio channels.  
`sample_rate` |  `int32` The sample rate of the audio.  
Union field `data_or_uri`. The audio content. `data_or_uri` can be only one of the following:  
`data` |  `bytes` The audio content.  
`uri` |  `string` The URI of the audio.  
  
## MimeType

Enums  
---  
`TYPE_UNSPECIFIED` |   
`TYPE_WAV` | WAV audio format  
`TYPE_MP3` | MP3 audio format  
`TYPE_AIFF` | AIFF audio format  
`TYPE_AAC` | AAC audio format  
`TYPE_OGG` | OGG audio format  
`TYPE_FLAC` | FLAC audio format  
`TYPE_MPEG` | MPEG audio format  
`TYPE_M4A` | M4A audio format  
`TYPE_L16` | L16 audio format  
`TYPE_S16LE` | S16LE audio format  
`TYPE_OPUS` | OPUS audio format  
`TYPE_ALAW` | ALAW audio format  
`TYPE_MULAW` | MULAW audio format  
`TYPE_VIDEO_AUDIO_S16LE` | Video audio S16LE format (internal)  
`TYPE_WEBM` | WEBM audio format  
  
## AudioDelta

Fields  
---  
`mime_type` |  `[MimeType](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.AudioContent.MimeType)`  
`rate  
**(deprecated)**` |  `int32` This item is deprecated!Deprecated. Use sample_rate instead. The value is ignored.  
`sample_rate` |  `int32` The sample rate of the audio.  
`channels` |  `int32` The number of audio channels.  
Union field `data_or_uri`.`data_or_uri` can be only one of the following:  
`data` |  `bytes`  
`uri` |  `string`  
  
## AudioResponseFormat

Configuration for audio output format.

Fields  
---  
`mime_type` |  `[MimeType](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.AudioResponseFormat.MimeType)` The MIME type of the audio output.  
`delivery` |  `[Delivery](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.AudioResponseFormat.Delivery)` The delivery mode for the audio output.  
`sample_rate` |  `int32` Sample rate in Hz.  
`bit_rate` |  `int32` Bit rate in bits per second (bps). Only applicable for compressed formats (MP3, Opus).  
  
## Delivery

Delivery mode for audio output.

Enums  
---  
`DELIVERY_UNSPECIFIED` | Default value. This value is unused.  
`INLINE` | Audio data is returned inline in the response.  
`URI` | Audio data is returned as a URI.  
  
## MimeType

Supported MIME types for audio output.

Enums  
---  
`TYPE_UNSPECIFIED` | Default value. This value is unused.  
`TYPE_MP3` | MP3 audio format.  
`TYPE_OGG_OPUS` | OGG Opus audio format.  
`TYPE_L16` | Raw PCM (L16) audio format.  
`TYPE_WAV` | WAV audio format.  
`TYPE_ALAW` | A-law audio format.  
`TYPE_MULAW` | Mu-law audio format.  
  
## CancelInteractionHttpTranscoderRequest

Request for InteractionsHttpService.CancelInteractionHttp.

Fields  
---  
`name` |  `string` Required. The name of the interaction to cancel. Format: interactionsHttp/{interaction}  
  
## CancelInteractionRequest

Fields  
---  
`name` |  `string` Required. The name of the interaction to cancel. Format: `interactions/{interaction}`.  
  
## CodeExecution

This type has no fields.

A tool that can be used by the model to execute code.

## CodeExecutionCallContent

This item is deprecated!

Code execution content.

Fields  
---  
`arguments` |  `[CodeExecutionCallArguments](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.CodeExecutionCallContent.CodeExecutionCallArguments)` Required. The arguments to pass to the code execution.  
  
## CodeExecutionCallArguments

The arguments to pass to the code execution.

Fields  
---  
`language` |  `[Language](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.CodeExecutionCallContent.CodeExecutionCallArguments.Language)` Programming language of the `code`.  
`code` |  `string` The code to be executed.  
  
## Language

Supported programming languages for the generated code.

Enums  
---  
`LANGUAGE_UNSPECIFIED` | Unspecified language. This value should not be used.  
`PYTHON` | Python >= 3.10, with numpy and simpy available.  
  
## CodeExecutionCallDelta

Fields  
---  
`arguments` |  `[CodeExecutionCallArguments](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.CodeExecutionCallContent.CodeExecutionCallArguments)`  
  
## CodeExecutionCallStep

Code execution call step.

Fields  
---  
`arguments` |  `[CodeExecutionCallStepArguments](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.CodeExecutionCallStep.CodeExecutionCallStepArguments)` Required. The arguments to pass to the code execution.  
  
## CodeExecutionCallStepArguments

The arguments to pass to the code execution.

Fields  
---  
`language` |  `[Language](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.CodeExecutionCallStep.CodeExecutionCallStepArguments.Language)` Programming language of the `code`.  
`code` |  `string` The code to be executed.  
  
## Language

Supported programming languages for the generated code.

Enums  
---  
`LANGUAGE_UNSPECIFIED` | Unspecified language. This value should not be used.  
`PYTHON` | Python >= 3.10, with numpy and simpy available.  
  
## CodeExecutionResultContent

This item is deprecated!

Code execution result content.

Fields  
---  
`result` |  `string` Required. The output of the code execution.  
`is_error` |  `bool` Whether the code execution resulted in an error.  
  
## CodeExecutionResultDelta

Fields  
---  
`result` |  `string`  
`is_error` |  `bool`  
  
## CodeExecutionResultStep

Code execution result step.

Fields  
---  
`result` |  `string` Required. The output of the code execution.  
`is_error` |  `bool` Whether the code execution resulted in an error.  
  
## CodeMenderAgentConfig

Configuration for the CodeMender agent.

Fields  
---  
`session_id` |  `string` Parameter for grouping multiple interactions that belong to the same CodeMender session.  
`session_config` |  `[SessionConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.CodeMenderAgentConfig.SessionConfig)` Optional session-specific configurations to override default agent behavior.  
`model` |  `string` The name of the model to use for the CodeMender agent. One CodeMender session will only use one model.  
Union field `request`. CodeMender's request type. Set exactly one of find_request/fix_request only on the first round to start a session; on subsequent rounds (e.g. submitting tool results), leave this unset and identify the session via session_id. This oneof is intentionally not a subtype_source discriminator so it can be omitted on resume rounds. `request` can be only one of the following:  
`find_request` |  `[FindRequest](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.CodeMenderAgentConfig.FindRequest)` Parameters for finding vulnerabilities.  
`fix_request` |  `[FixRequest](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.CodeMenderAgentConfig.FixRequest)` Parameters for fixing vulnerabilities.  
  
## FileContent

Content of a single file in the codebase.

Fields  
---  
`path` |  `string` The relative path of the file from the project root.  
`content` |  `string` The UTF-8 encoded text content of the file.  
  
## FindRequest

Request parameters specific to FIND sessions, used for discovering vulnerabilities in a codebase.

Fields  
---  
`source_files[]` |  `[FileContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.CodeMenderAgentConfig.FileContent)` A list of source files to provide as context for the scan.  
`finding_id` |  `string` The identifier of a specific finding to verify. This is primarily used in VERIFY mode to focus the agent's execution-based validation on a single vulnerability.  
`description` |  `string` Additional context or custom instructions provided by the user to guide the vulnerability analysis.  
`mode` |  `[Mode](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.CodeMenderAgentConfig.FindRequest.Mode)` The mode of the find session.  
  
## Mode

Defines the depth and thoroughness of the find session.

Enums  
---  
`MODE_UNSPECIFIED` | Default value. This value is unused.  
`MODE_SCAN` | Fast scan using only the initial classifier.  
`MODE_VERIFY` | Performs classification followed by detailed investigation.  
  
## FixRequest

Request parameters specific to FIX sessions, used for generating and validating security patches.

Fields  
---  
`source_files[]` |  `[FileContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.CodeMenderAgentConfig.FileContent)` A list of source files providing context for the remediation. These files are typically the ones containing the identified vulnerability.  
`finding_id` |  `string` The identifier of the specific security finding to be remediated. This ID maps to a previously discovered vulnerability.  
`description` |  `string` Additional context or custom instructions provided by the user to guide the patch generation process.  
  
## SessionConfig

The configuration of CodeMender sessions.

Fields  
---  
`max_rounds` |  `int32` The maximum number of interaction rounds the agent is allowed to perform before reaching a timeout.  
  
## ComputerUse

A tool that can be used by the model to interact with the computer.

Fields  
---  
`environment` |  `[Environment](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ComputerUse.Environment)` The environment being operated.  
`excluded_predefined_functions[]` |  `string` The list of predefined functions that are excluded from the model call.  
`enable_prompt_injection_detection` |  `bool` Whether enable the prompt injection detection check on computer-use request.  
`disabled_safety_policies[]` |  `[SafetyPolicy](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ComputerUse.SafetyPolicy)` Optional. Disabled safety policies for computer use.  
  
## Environment

Represents the environment being operated, such as a web browser.

Enums  
---  
`ENVIRONMENT_UNSPECIFIED` | Defaults to browser.  
`BROWSER` | Operates in a web browser.  
`MOBILE` | Operates in a mobile environment.  
`DESKTOP` | Operates in a desktop environment.  
  
## SafetyPolicy

Enums  
---  
`SAFETY_POLICY_UNSPECIFIED` | Unspecified safety policy.  
`FINANCIAL_TRANSACTIONS` | Safety policy for financial transactions.  
`SENSITIVE_DATA_MODIFICATION` | Safety policy for sensitive data modification.  
`COMMUNICATION_TOOL` | Safety policy for communication tools (e.g. Gmail, Chat, Meet).  
`ACCOUNT_CREATION` | Safety policy for account creation.  
`DATA_MODIFICATION` | Safety policy for data modification.  
`USER_CONSENT_MANAGEMENT` | Safety policy for user consent management.  
`LEGAL_TERMS_AND_AGREEMENTS` | Safety policy for legal terms and agreements.  
  
## Content

The content of the response.

Fields  
---  
Union field `type`.`type` can be only one of the following:  
`text` |  `[TextContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.TextContent)`  
`image` |  `[ImageContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ImageContent)`  
`audio` |  `[AudioContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.AudioContent)`  
`document` |  `[DocumentContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.DocumentContent)`  
`video` |  `[VideoContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.VideoContent)`  
`thought  
**(deprecated)**` |  `[ThoughtContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ThoughtContent)` This item is deprecated!  
`tool_call  
**(deprecated)**` |  `[ToolCallContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ToolCallContent)` This item is deprecated!  
`tool_result  
**(deprecated)**` |  `[ToolResultContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ToolResultContent)` This item is deprecated!  
  
## ContentDelta

Fields  
---  
`index` |  `int32`  
`delta` |  `[ContentDeltaData](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ContentDeltaData)`  
  
## ContentDeltaData

The delta content data for a content block.

Fields  
---  
Union field `type`. The type of the delta content. `type` can be only one of the following:  
`text` |  `[TextDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.TextDelta)`  
`image` |  `[ImageDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ImageDelta)`  
`audio` |  `[AudioDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.AudioDelta)`  
`document` |  `[DocumentDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.DocumentDelta)`  
`video` |  `[VideoDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.VideoDelta)`  
`thought_summary` |  `[ThoughtSummaryDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ThoughtSummaryDelta)`  
`thought_signature` |  `[ThoughtSignatureDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ThoughtSignatureDelta)`  
`tool_call` |  `[ToolCallDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ToolCallDelta)`  
`tool_result` |  `[ToolResultDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ToolResultDelta)`  
`text_annotation` |  `[TextAnnotationDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.TextAnnotationDelta)`  
  
## ContentList

A list of Content.

Fields  
---  
`contents[]` |  `[Content](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Content)` The contents of the list.  
  
## ContentStart

Fields  
---  
`index` |  `int32`  
`content` |  `[Content](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Content)`  
  
## ContentStop

Fields  
---  
`index` |  `int32`  
  
## CreateInteractionHttpRequest

Request message for [InteractionsService.CreateInteractionHttp].

Fields  
---  
`parent` |  `string` Required. The parent resource where this interaction will be created. Format: `projects/{project}/locations/{location}`Supported only by the Vertex API only.  
`http_body` |  `[HttpBody](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/google.api#google.api.HttpBody)` Required. The interaction to create.  
  
## CreateInteractionHttpTranscoderRequest

Request message for InteractionsHttpService.CreateInteractionHttp.

Fields  
---  
`parent` |  `string` Required. The parent resource where this interaction will be created. Format: `projects/{project}/locations/{location}`Supported only by the Vertex API only.  
`http_body` |  `[HttpBody](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/google.api#google.api.HttpBody)` Required. The interaction to create.  
  
## CreateInteractionRequest

Configuration parameters for creating an interaction.

Fields  
---  
`stream` |  `bool` Input only. Whether the interaction will be streamed.  
`store` |  `bool` Input only. Whether to store the response and request for later retrieval.  
`interaction` |  `[Interaction](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Interaction)` The interaction to create.  
`background` |  `bool` Input only. Whether to run the model interaction in the background.  
  
## DeepResearchAgentConfig

Configuration for the Deep Research agent.

Fields  
---  
`thinking_summaries` |  `[ThinkingSummaries](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ThinkingSummaries)` Whether to include thought summaries in the response.  
`visualization` |  `[VisualizationMode](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.DeepResearchAgentConfig.VisualizationMode)` Whether to include visualizations in the response.  
`collaborative_planning` |  `bool` Enables human-in-the-loop planning for the Deep Research agent. If set to true, the Deep Research agent will provide a research plan in its response. The agent will then proceed only if the user confirms the plan in the next turn.  
`enable_bigquery_tool` |  `bool` Enables bigquery tool for the Deep Research agent.  
  
## VisualizationMode

Enum for visualization mode. Eventually we will support an interactive mode where the user can choose whether to include HTML visualizations in the response.

Enums  
---  
`UNSPECIFIED` | The default visualization mode. Will default to AUTO.  
`OFF` | Do not include visualizations.  
`AUTO` | Automatically include visualizations.  
  
## DeleteInteractionRequest

Request for InteractionService.DeleteInteraction.

Fields  
---  
`name` |  `string` Required. The name of the interaction to delete. Format: interactions/{interaction}  
  
## DeleteInteractionResponse

This type has no fields.

Response for InteractionService.DeleteInteraction.

## DocumentContent

A document content block.

Fields  
---  
`mime_type_string` |  `string` Flexible MIME type string of the document, superseding mime_type = 1. Note: Bespoke logic in the GAOS parser/serializer maps this to the "mime_type" JSON key.  
Union field `data_or_uri`. The document content. `data_or_uri` can be only one of the following:  
`data` |  `bytes` The document content.  
`uri` |  `string` The URI of the document.  
  
## MimeType

Enums  
---  
`TYPE_UNSPECIFIED` |   
`TYPE_PDF` | PDF document format  
`TYPE_CSV` | CSV document format  
  
## DocumentDelta

Fields  
---  
`mime_type` |  `[MimeType](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.DocumentContent.MimeType)`  
Union field `data_or_uri`.`data_or_uri` can be only one of the following:  
`data` |  `bytes`  
`uri` |  `string`  
  
## DynamicAgentConfig

Configuration for dynamic agents.

Fields  
---  
`config` |  `[Struct](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Struct)` For agents that are not supported statically in the API definition.  
  
## EnvironmentConfig

Configuration for a custom environment.

Fields  
---  
`sources[]` |  `[Source](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.EnvironmentConfig.Source)`  
`environment_id` |  `string` Optional. The environment ID for the interaction. If specified, the request will update the existing environment instead of creating a new one.  
Union field `network`. Network configuration for the environment. `network` can be only one of the following:  
`network_allowlist` |  `[EnvironmentNetworkEgressAllowlist](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.EnvironmentConfig.EnvironmentNetworkEgressAllowlist)` Allow only specific domains.  
`network_mode` |  `[NetworkMode](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.EnvironmentConfig.NetworkMode)` Network egress mode.  
  
## EgressRule

A single domain allowlist rule with optional header injection.

Fields  
---  
`domain` |  `string` Domain to allow outbound requests to. Supports wildcards (e.g. '*.googleapis.com'). Use '*' to allow all domains.  
`transform` |  `map<string, string>` Headers to inject into requests matching this rule. Key: header name (e.g., "Authorization"). Value: header value (e.g., "Bearer your-token").  
  
## EnvironmentNetworkEgressAllowlist

Network egress configuration for the environment.

Fields  
---  
`allowlist[]` |  `[EgressRule](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.EnvironmentConfig.EgressRule)` List of allowed domains and their configurations. Set to `"disabled"` to block all network egress.  
  
## NetworkMode

Network egress mode for non-allowlist configurations.

Enums  
---  
`NETWORK_MODE_UNSPECIFIED` | Default value. Unused.  
`DISABLED` | All network egress is blocked.  
  
## Source

A source to be mounted into the environment.

Fields  
---  
`type` |  `[Type](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.EnvironmentConfig.Source.Type)`  
`source` |  `string` The source of the environment. For Cloud Storage, this is the Cloud Storage path. For GitHub, this is the GitHub path.  
`target` |  `string` Where the source should appear in the environment.  
`content` |  `string` The inline content if `type` is `INLINE`.  
`encoding` |  `string` Optional encoding for inline content (e.g. `base64`).  
  
## Type

Enums  
---  
`TYPE_UNSPECIFIED` |   
`GCS` | A Cloud Storage bucket.  
`INLINE` | Inline content.  
`REPOSITORY` | A generic repository. The protocol prefix in the source URL identifies the provider (e.g., github://, gcs://).  
`SKILL_REGISTRY` | A skill resource from the Skill Registry Service. Skill: projects/{project}/locations/{location}/skills/{skill} SkillRevision: projects/{project}/locations/{location}/skills/{skill}/revisions/{revision} Support mounting all skills under a project: projects/{project}/locations/{location}/skills.  
  
## Error

Error message from an interaction.

Fields  
---  
`code` |  `string` A URI that identifies the error type.  
`message` |  `string` A human-readable error message.  
  
## ErrorEvent

Fields  
---  
`error` |  `[Error](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Error)`  
  
## ExaAISearchConfig

Used to specify configuration for ExaAISearch.

Fields  
---  
`api_key` |  `string` Required. The API key for ExaAiSearch.  
`custom_config` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` Optional. This field can be used to pass any parameter from the Exa.ai Search API.  
  
## Field

Represents a single field in a struct.

Fields  
---  
`name` |  `string`  
`value` |  `[Value](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Value)`  
  
## FileCitation

A file citation annotation.

Fields  
---  
`document_uri` |  `string` The URI of the file.  
`file_name` |  `string` The name of the file.  
`source` |  `string` Source attributed for a portion of the text.  
`custom_metadata` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` User provided metadata about the retrieved context.  
`page_number` |  `int32` Page number of the cited document, if applicable.  
`media_id` |  `string` Media ID in-case of image citations, if applicable.  
  
## FileSearch

A tool that can be used by the model to search files.

Fields  
---  
`file_search_store_names[]` |  `string` The file search store names to search.  
`top_k` |  `int32` The number of semantic retrieval chunks to retrieve.  
`metadata_filter` |  `string` Metadata filter to apply to the semantic retrieval documents and chunks.  
  
## FileSearchCallContent

This type has no fields.

This item is deprecated!

File Search content.

## FileSearchCallDelta

This type has no fields.

## FileSearchCallStep

This type has no fields.

File Search call step.

## FileSearchResultContent

This item is deprecated!

File Search result content.

Fields  
---  
`result[]` |  `[FileSearchResult](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.FileSearchResultContent.FileSearchResult)` The results of the File Search.  
  
## FileSearchResult

This type has no fields.

The result of the File Search.

## FileSearchResultDelta

Fields  
---  
`result[]` |  `[FileSearchResult](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.FileSearchResultContent.FileSearchResult)`  
  
## FileSearchResultStep

This type has no fields.

File Search result step.

## Function

A tool that can be used by the model.

Fields  
---  
`name` |  `string` The name of the function.  
`description` |  `string` A description of the function.  
`parameters` |  `[Value](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Value)` The JSON Schema for the function's parameters.  
  
## FunctionCallContent

This item is deprecated!

A function tool call content block.

Fields  
---  
`name` |  `string` Required. The name of the tool to call.  
`arguments` |  `[Struct](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Struct)` Required. The arguments to pass to the function.  
  
## FunctionCallDelta

Fields  
---  
`name` |  `string`  
`arguments` |  `[Struct](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Struct)`  
  
## FunctionCallStep

A function tool call step.

Fields  
---  
`name` |  `string` Required. The name of the tool to call.  
`arguments` |  `[Struct](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Struct)` Required. The arguments to pass to the function.  
  
## FunctionResultContent

This item is deprecated!

A function tool result content block.

Fields  
---  
`name` |  `string` The name of the tool that was called.  
`is_error` |  `bool` Whether the tool call resulted in an error.  
Union field `result`. The result of the tool call. `result` can be only one of the following:  
`struct_result` |  `[Struct](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Struct)`  
`content_list` |  `[FunctionResultSubcontentList](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.FunctionResultSubcontentList)`  
`string_result` |  `string`  
  
## FunctionResultDelta

Fields  
---  
`name` |  `string`  
`is_error` |  `bool`  
`result` |  `[Value](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Value)`  
  
## FunctionResultStep

Result of a function tool call.

Fields  
---  
`name` |  `string` The name of the tool that was called.  
`is_error` |  `bool` Whether the tool call resulted in an error.  
`result` |  `[Value](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Value)` Required. The result of the tool call.  
  
## FunctionResultSubcontent

Fields  
---  
Union field `type`.`type` can be only one of the following:  
`text` |  `[TextContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.TextContent)`  
`image` |  `[ImageContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ImageContent)`  
  
## FunctionResultSubcontentList

Fields  
---  
`contents[]` |  `[FunctionResultSubcontent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.FunctionResultSubcontent)`  
  
## GenerationConfig

Configuration parameters for model interactions.

Fields  
---  
`temperature  
**(deprecated)**` |  `float` This item is deprecated!Controls the randomness of the output.  
`top_p  
**(deprecated)**` |  `float` This item is deprecated!The maximum cumulative probability of tokens to consider when sampling.  
`seed` |  `int32` Seed used in decoding for reproducibility.  
`stop_sequences[]` |  `string` A list of character sequences that will stop output interaction.  
`thinking_level` |  `[ThinkingLevel](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ThinkingLevel)` The level of thought tokens that the model should generate.  
`thinking_summaries` |  `[ThinkingSummaries](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ThinkingSummaries)` Whether to include thought summaries in the response.  
`max_output_tokens` |  `int32` The maximum number of tokens to include in the response.  
`image_config  
**(deprecated)**` |  `[ImageConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ImageConfig)` This item is deprecated!Configuration for image interaction.  
`video_config` |  `[VideoConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.VideoConfig)` Configuration for video generation.  
`transcription_config` |  `[TranscriptionConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.TranscriptionConfig)` Optional. Configuration for speech recognition (transcription). If present, ASR is enabled.  
Union field `tool_choice`. The tool choice configuration. `tool_choice` can be only one of the following:  
`tool_choice_mode` |  `[ToolChoiceType](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ToolChoiceType)` The mode of the tool choice.  
`tool_choice_config` |  `[ToolChoiceConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ToolChoiceConfig)` The config for the tool choice.  
  
## GetInteractionHttpTranscoderRequest

Request for InteractionsHttpService.GetInteractionHttp.

Fields  
---  
`name` |  `string` Required. The name of the interaction to retrieve. Format: interactionsHttp/{interaction}  
`stream` |  `bool` If true, streams the interaction events as Server-Sent Events.  
`last_event_id` |  `string` If set, resumes the interaction stream from the chunk after the event marked by the event id. Can only be used if `stream` is true.  
`include_input  
**(deprecated)**` |  `bool` This item is deprecated!If true, includes the input in the response.  
  
## GetInteractionRequest

Request for InteractionService.GetInteraction.

Fields  
---  
`name` |  `string` Required. The name of the interaction to retrieve. Format: interactions/{interaction}  
`stream` |  `bool` If true, streams the interaction events as Server-Sent Events.  
`last_event_id` |  `string` If set, resumes the interaction stream from the chunk after the event marked by the event id. Can only be used if `stream` is true.  
`include_input  
**(deprecated)**` |  `bool` This item is deprecated!If true, includes the input in the response.  
  
## GoogleMaps

A tool that can be used by the model to call Google Maps.

Fields  
---  
`enable_widget` |  `bool` Whether to return a widget context token in the tool call result of the response.  
`latitude` |  `double` The latitude of the user's location.  
`longitude` |  `double` The longitude of the user's location.  
  
## GoogleMapsCallContent

This item is deprecated!

Google Maps content.

Fields  
---  
`arguments` |  `[GoogleMapsCallArguments](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GoogleMapsCallContent.GoogleMapsCallArguments)` The arguments to pass to the Google Maps tool.  
  
## GoogleMapsCallArguments

The arguments to pass to the Google Maps tool.

Fields  
---  
`queries[]` |  `string` The queries to be executed.  
  
## GoogleMapsCallDelta

Fields  
---  
`arguments` |  `[GoogleMapsCallArguments](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GoogleMapsCallContent.GoogleMapsCallArguments)` The arguments to pass to the Google Maps tool.  
  
## GoogleMapsCallStep

Google Maps call step.

Fields  
---  
`arguments` |  `[GoogleMapsCallStepArguments](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GoogleMapsCallStep.GoogleMapsCallStepArguments)` The arguments to pass to the Google Maps tool.  
  
## GoogleMapsCallStepArguments

The arguments to pass to the Google Maps tool.

Fields  
---  
`queries[]` |  `string` The queries to be executed.  
  
## GoogleMapsResultContent

This item is deprecated!

Google Maps result content.

Fields  
---  
`result[]` |  `[GoogleMapsResult](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GoogleMapsResultContent.GoogleMapsResult)` Required. The results of the Google Maps.  
  
## GoogleMapsResult

The result of the Google Maps.

Fields  
---  
`places[]` |  `[Places](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GoogleMapsResultContent.GoogleMapsResult.Places)` The places that were found.  
`widget_context_token` |  `string` Resource name of the Google Maps widget context token.  
  
## Places

Fields  
---  
`place_id` |  `string` The ID of the place, in `places/{place_id}` format.  
`name` |  `string` Title of the place.  
`url` |  `string` URI reference of the place.  
`review_snippets[]` |  `[ReviewSnippet](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ReviewSnippet)` Snippets of reviews that are used to generate answers about the features of a given place in Google Maps.  
  
## GoogleMapsResultDelta

Fields  
---  
`result[]` |  `[GoogleMapsResult](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GoogleMapsResultContent.GoogleMapsResult)` The results of the Google Maps.  
  
## GoogleMapsResultStep

Google Maps result step.

Fields  
---  
`result[]` |  `[GoogleMapsResultItem](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GoogleMapsResultStep.GoogleMapsResultItem)`  
  
## GoogleMapsResultItem

The result of the Google Maps.

Fields  
---  
`places[]` |  `[GoogleMapsResultPlaces](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GoogleMapsResultStep.GoogleMapsResultItem.GoogleMapsResultPlaces)`  
`widget_context_token` |  `string`  
  
## GoogleMapsResultPlaces

Fields  
---  
`place_id` |  `string`  
`name` |  `string`  
`url` |  `string`  
`review_snippets[]` |  `[ReviewSnippet](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ReviewSnippet)`  
  
## GoogleSearch

A tool that can be used by the model to search Google.

Fields  
---  
`search_types[]` |  `[SearchType](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GoogleSearch.SearchType)` The types of search grounding to enable.  
  
## SearchType

The types of search grounding to enable.

Enums  
---  
`SEARCH_TYPE_UNSPECIFIED` | Unspecified search type. This value should not be used.  
`SEARCH_TYPE_WEB_SEARCH` | Setting this field enables web search. Only text results are returned.  
`SEARCH_TYPE_IMAGE_SEARCH` | Setting this field enables image search. Image bytes are returned.  
`SEARCH_TYPE_ENTERPRISE_WEB_SEARCH` | Setting this field enables enterprise web search.  
  
## GoogleSearchCallContent

This item is deprecated!

Google Search content.

Fields  
---  
`arguments` |  `[GoogleSearchCallArguments](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GoogleSearchCallContent.GoogleSearchCallArguments)` Required. The arguments to pass to Google Search.  
`search_type` |  `[SearchType](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GoogleSearch.SearchType)` The type of search grounding enabled.  
  
## GoogleSearchCallArguments

The arguments to pass to Google Search.

Fields  
---  
`queries[]` |  `string` Web search queries for the following-up web search.  
  
## GoogleSearchCallDelta

Fields  
---  
`arguments` |  `[GoogleSearchCallArguments](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GoogleSearchCallContent.GoogleSearchCallArguments)`  
  
## GoogleSearchCallStep

Google Search call step.

Fields  
---  
`arguments` |  `[GoogleSearchCallStepArguments](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GoogleSearchCallStep.GoogleSearchCallStepArguments)` Required. The arguments to pass to Google Search.  
`search_type` |  `[SearchType](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GoogleSearch.SearchType)` The type of search grounding enabled.  
  
## GoogleSearchCallStepArguments

The arguments to pass to Google Search.

Fields  
---  
`queries[]` |  `string` Web search queries for the following-up web search.  
  
## GoogleSearchResultContent

This item is deprecated!

Google Search result content.

Fields  
---  
`result[]` |  `[GoogleSearchResult](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GoogleSearchResultContent.GoogleSearchResult)` Required. The results of the Google Search.  
`is_error` |  `bool` Whether the Google Search resulted in an error.  
  
## GoogleSearchResult

The result of the Google Search.

Fields  
---  
`search_suggestions` |  `string` Web content snippet that can be embedded in a web page or an app webview.  
  
## GoogleSearchResultDelta

Fields  
---  
`result[]` |  `[GoogleSearchResult](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GoogleSearchResultContent.GoogleSearchResult)`  
`is_error` |  `bool`  
  
## GoogleSearchResultStep

Google Search result step.

Fields  
---  
`result[]` |  `[GoogleSearchResultItem](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GoogleSearchResultStep.GoogleSearchResultItem)` Required. The results of the Google Search.  
`is_error` |  `bool` Whether the Google Search resulted in an error.  
  
## GoogleSearchResultItem

The result of the Google Search.

Fields  
---  
`search_suggestions` |  `string` Web content snippet that can be embedded in a web page or an app webview.  
  
## HarmCategory

Harm categories that can be detected in user input and model responses.

Enums  
---  
`HARM_CATEGORY_UNSPECIFIED` | Default value. This value is unused.  
`HARM_CATEGORY_HATE_SPEECH` | Content that promotes violence or incites hatred against individuals or groups based on certain attributes.  
`HARM_CATEGORY_DANGEROUS_CONTENT` | Content that promotes, facilitates, or enables dangerous activities.  
`HARM_CATEGORY_HARASSMENT` | Abusive, threatening, or content intended to bully, torment, or ridicule.  
`HARM_CATEGORY_SEXUALLY_EXPLICIT` | Content that contains sexually explicit material.  
`HARM_CATEGORY_CIVIC_INTEGRITY` | Deprecated: Election filter is not longer supported. The harm category is civic integrity.This item is deprecated!  
`HARM_CATEGORY_IMAGE_HATE` | Images that contain hate speech.  
`HARM_CATEGORY_IMAGE_DANGEROUS_CONTENT` | Images that contain dangerous content.  
`HARM_CATEGORY_IMAGE_HARASSMENT` | Images that contain harassment.  
`HARM_CATEGORY_IMAGE_SEXUALLY_EXPLICIT` | Images that contain sexually explicit content.  
`HARM_CATEGORY_JAILBREAK` | Prompts designed to bypass safety filters.  
  
## ImageConfig

This item is deprecated!

The configuration for image interaction.

Fields  
---  
`aspect_ratio` |  `string` The aspect ratio of the image to generate. Supported aspect ratios: 1:1, 2:3, 3:2, 3:4, 4:3, 9:16, 16:9, 21:9.If not specified, the model will choose a default aspect ratio based on any reference images provided.  
`image_size` |  `string` Specifies the size of generated images. Supported values are `1K`, `2K`, `4K`. If not specified, the model will use default value `1K`.  
  
## ImageContent

An image content block.

Fields  
---  
`mime_type_string` |  `string` Flexible MIME type string of the image, superseding mime_type = 1. Note: Bespoke logic in the GAOS parser/serializer maps this to the "mime_type" JSON key.  
`resolution` |  `[MediaResolution](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.MediaResolution)` The resolution of the media.  
Union field `data_or_uri`. The image content. `data_or_uri` can be only one of the following:  
`data` |  `bytes` The image content.  
`uri` |  `string` The URI of the image.  
  
## MimeType

Enums  
---  
`TYPE_UNSPECIFIED` |   
`TYPE_PNG` | PNG image format  
`TYPE_JPEG` | JPEG image format  
`TYPE_WEBP` | WebP image format  
`TYPE_HEIC` | HEIC image format  
`TYPE_HEIF` | HEIF image format  
`TYPE_GIF` | GIF image format  
`TYPE_BMP` | BMP image format  
`TYPE_TIFF` | TIFF image format  
`TYPE_VIDEO_FRAME_JPEG2000` | Video frame JPEG2000 format (internal)  
`TYPE_VIDEO_JPEG2000` | Video only frame JPEG2000 format (internal)  
  
## ImageDelta

Fields  
---  
`mime_type` |  `[MimeType](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ImageContent.MimeType)`  
`resolution` |  `[MediaResolution](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.MediaResolution)` The resolution of the media.  
Union field `data_or_uri`.`data_or_uri` can be only one of the following:  
`data` |  `bytes`  
`uri` |  `string`  
  
## ImageResponseFormat

Configuration for image output format.

Fields  
---  
`mime_type` |  `[MimeType](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ImageResponseFormat.MimeType)` The MIME type of the image output.  
`delivery` |  `[Delivery](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ImageResponseFormat.Delivery)` The delivery mode for the image output.  
`aspect_ratio` |  `[AspectRatio](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ImageResponseFormat.AspectRatio)` The aspect ratio for the image output.  
`image_size` |  `[ImageSize](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ImageResponseFormat.ImageSize)` The size of the image output.  
  
## AspectRatio

Supported aspect ratios for image output.

Enums  
---  
`ASPECT_RATIO_UNSPECIFIED` | Default value. This value is unused.  
`ASPECT_RATIO_ONE_BY_ONE` | 1:1 aspect ratio.  
`ASPECT_RATIO_TWO_BY_THREE` | 2:3 aspect ratio.  
`ASPECT_RATIO_THREE_BY_TWO` | 3:2 aspect ratio.  
`ASPECT_RATIO_THREE_BY_FOUR` | 3:4 aspect ratio.  
`ASPECT_RATIO_FOUR_BY_THREE` | 4:3 aspect ratio.  
`ASPECT_RATIO_FOUR_BY_FIVE` | 4:5 aspect ratio.  
`ASPECT_RATIO_FIVE_BY_FOUR` | 5:4 aspect ratio.  
`ASPECT_RATIO_NINE_BY_SIXTEEN` | 9:16 aspect ratio.  
`ASPECT_RATIO_SIXTEEN_BY_NINE` | 16:9 aspect ratio.  
`ASPECT_RATIO_TWENTY_ONE_BY_NINE` | 21:9 aspect ratio.  
`ASPECT_RATIO_ONE_BY_EIGHT` | 1:8 aspect ratio.  
`ASPECT_RATIO_EIGHT_BY_ONE` | 8:1 aspect ratio.  
`ASPECT_RATIO_ONE_BY_FOUR` | 1:4 aspect ratio.  
`ASPECT_RATIO_FOUR_BY_ONE` | 4:1 aspect ratio.  
  
## Delivery

Delivery mode for image output.

Enums  
---  
`DELIVERY_UNSPECIFIED` | Default value. This value is unused.  
`INLINE` | Image data is returned inline in the response.  
`URI` | Image data is returned as a URI.  
  
## ImageSize

Supported image sizes for image output.

Enums  
---  
`IMAGE_SIZE_UNSPECIFIED` | Default value. This value is unused.  
`IMAGE_SIZE_FIVE_TWELVE` | 512px image size.  
`IMAGE_SIZE_ONE_K` | 1K image size.  
`IMAGE_SIZE_TWO_K` | 2K image size.  
`IMAGE_SIZE_FOUR_K` | 4K image size.  
  
## MimeType

Supported MIME types for image output.

Enums  
---  
`TYPE_UNSPECIFIED` | Default value. This value is unused.  
`TYPE_JPEG` | JPEG image format.  
  
## Interaction

Response for InteractionService.CreateInteraction.

Fields  
---  
`id` |  `string` Required. Output only. A unique identifier for the interaction completion.  
`status` |  `[Status](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Interaction.Status)` Required. Output only. The status of the interaction.  
`created` |  `string` Required. Output only. The time at which the response was created in ISO 8601 format (YYYY-MM-DDThh:mm:ssZ).  
`updated` |  `string` Required. Output only. The time at which the response was last updated in ISO 8601 format (YYYY-MM-DDThh:mm:ssZ).  
`system_instruction` |  `string` System instruction for the interaction.  
`tools[]` |  `[Tool](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Tool)` A list of tool declarations the model may call during interaction.  
`usage` |  `[Usage](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Interaction.Usage)` Output only. Statistics on the interaction request's token usage.  
`response_modalities[]  
**(deprecated)**` |  `[ResponseModality](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ResponseModality)` This item is deprecated!The requested modalities of the response (TEXT, IMAGE, AUDIO).  
`response_mime_type  
**(deprecated)**` |  `string` This item is deprecated!The mime type of the response. This is required if response_format is set.  
`previous_interaction_id` |  `string` The ID of the previous interaction, if any.  
`environment_id` |  `string` Output only. The environment ID for the interaction. Only populated if environment config is set in the request.  
`steps[]` |  `[Step](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Step)` Required. Output only. The steps that make up the interaction, when included in the response.  
`safety_settings[]` |  `[SafetySetting](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.SafetySetting)` Safety settings for the interaction.  
`labels` |  `map<string, string>` The labels with user-defined metadata for the request.Label keys and values can be no longer than 63 characters (Unicode codepoints) and can only contain lowercase letters, numeric characters, underscores, and dashes. International characters are allowed. Label values are optional. Label keys must start with a letter.  
`errors[]` |  `[Error](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Error)` Output only. Diagnostic faults / platform errors recorded on the interaction.  
Union field `input`. The input for the interaction. `input` can be only one of the following:  
`content_list  
**(deprecated)**` |  `[ContentList](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ContentList)` This item is deprecated!The inputs for the interaction.  
`string_content` |  `string` A string input for the interaction, it will be processed as a single text input.  
`turn_list  
**(deprecated)**` |  `[TurnList](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.TurnList)` This item is deprecated!The turns for the interaction.  
`step_list` |  `[StepList](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.StepList)` Input only. The steps for the interaction.  
`content` |  `[Content](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Content)` The content for the interaction.  
Union field `response_format_config`. Enforces that the generated response is a JSON object that complies with the JSON schema specified in this field. `response_format_config` can be only one of the following:  
`response_format  
**(deprecated)**` |  `[Value](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Value)` This item is deprecated!Enforces that the generated response is a JSON object that complies with the JSON schema specified in this field.  
`response_format_list` |  `[ResponseFormatList](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ResponseFormatList)`  
`response_format_singleton` |  `[ResponseFormat](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ResponseFormat)`  
Union field `request_type`. The request type for the interaction. `request_type` can be only one of the following:  
`model_interaction` |  `[ModelInteraction](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ModelInteraction)` Interaction for generating the completion using models.  
`agent_interaction` |  `[AgentInteraction](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.AgentInteraction)` Interaction for generating the completion using agents.  
Union field `environment`. The environment configuration for the interaction. Can be an object specifying remote environment sources or a string referencing an existing environment ID. `environment` can be only one of the following:  
`env_id` |  `string` The environment ID for the interaction. Can be 'remote' for default environment.  
`remote_environment` |  `[EnvironmentConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.EnvironmentConfig)`  
`local_environment` |  `[LocalEnvironmentConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.LocalEnvironmentConfig)` The agent's environment lives on the client connection: its built-in environment operations (filesystem ops and running commands) are yielded to the client to execute, instead of running in a server-managed sandbox. Mutually exclusive with `remote_environment`. (Independent of any client-declared function tools, which are always executed on the client regardless of this field.)  
  
## Status

The status of the interaction.

Enums  
---  
`UNSPECIFIED` | Default value. This value is unused.  
`IN_PROGRESS` | The interaction is in progress.  
`REQUIRES_ACTION` | The interaction requires action/input from the user.  
`COMPLETED` | The interaction is completed.  
`FAILED` | The interaction failed.  
`CANCELLED` | The interaction was cancelled.  
`INCOMPLETE` | The interaction is completed, but contains incomplete results (e.g. hitting max_tokens).  
`BUDGET_EXCEEDED` | Deprecated: Token and execution budget exhaustion returns INCOMPLETE (11).This item is deprecated!  
`QUEUED` | The interaction is queued, waiting for processing (e.g. waiting for off-peak capacity).  
  
## Usage

Statistics on the interaction request's token usage.

Fields  
---  
`total_input_tokens` |  `int32` Number of tokens in the prompt (context).  
`input_tokens_by_modality[]` |  `[ModalityTokens](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Interaction.Usage.ModalityTokens)` A breakdown of input token usage by modality.  
`total_cached_tokens` |  `int32` Number of tokens in the cached part of the prompt (the cached content).  
`cached_tokens_by_modality[]` |  `[ModalityTokens](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Interaction.Usage.ModalityTokens)` A breakdown of cached token usage by modality.  
`total_output_tokens` |  `int32` Total number of tokens across all the generated responses.  
`output_tokens_by_modality[]` |  `[ModalityTokens](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Interaction.Usage.ModalityTokens)` A breakdown of output token usage by modality.  
`total_tool_use_tokens` |  `int32` Number of tokens present in tool-use prompt(s).  
`tool_use_tokens_by_modality[]` |  `[ModalityTokens](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Interaction.Usage.ModalityTokens)` A breakdown of tool-use token usage by modality.  
`total_thought_tokens` |  `int32` Number of tokens of thoughts for thinking models.  
`total_tokens` |  `int32` Total token count for the interaction request (prompt + responses + other internal tokens).  
`grounding_tool_count[]` |  `[GroundingToolCount](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Interaction.Usage.GroundingToolCount)` Grounding tool count.  
  
## GroundingToolCount

The number of grounding tool counts.

Fields  
---  
`type` |  `[Type](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Interaction.Usage.GroundingToolCount.Type)` The grounding tool type associated with the count.  
`count` |  `int32` The number of grounding tool counts.  
  
## Type

The type of grounding tool.

Enums  
---  
`TYPE_UNSPECIFIED` | Default value. This value is unused.  
`GOOGLE_SEARCH` | Grounding with Google Web Search and Image Search, & Web Grounding for Enterprise.  
`GOOGLE_MAPS` | Grounding with Google Maps.  
`RETRIEVAL` | Grounding with customer's data, for example, VertexAISearch.  
  
## ModalityTokens

The token count for a single response modality.

Fields  
---  
`modality` |  `[ResponseModality](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ResponseModality)` The modality associated with the token count.  
`tokens` |  `int32` Number of tokens for the modality.  
  
## InteractionCompleteEvent

This item is deprecated!

Fields  
---  
`interaction` |  `[Interaction](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Interaction)` Required. The completed interaction with empty outputs to reduce the payload size. Use the preceding ContentDelta events for the actual output.  
  
## InteractionCompletedSseEvent

Signals that the Interaction completed. Sent when the Interaction receives Complete/Cancel or naturally terminates. No more input can be sent to the Interaction after this.

Fields  
---  
`interaction` |  `[Interaction](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Interaction)` Required. Partial completed interaction resource emitted at the end of the stream.  
  
## InteractionCreatedSseEvent

Server response confirming that a new interaction was created.

Fields  
---  
`interaction` |  `[Interaction](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Interaction)` Required. Partial interaction resource emitted when the stream is created.  
  
## InteractionMetadata

Metadata for an interaction, used for listing interactions.

Fields  
---  
`id` |  `string` Output only. A unique identifier for the interaction completion.  
`status` |  `[Status](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Interaction.Status)` Output only. The status of the interaction.  
`created` |  `string` Output only. The time at which the response was created in ISO 8601 format (YYYY-MM-DDThh:mm:ssZ).  
`updated` |  `string` Output only. The time at which the response was last updated in ISO 8601 format (YYYY-MM-DDThh:mm:ssZ).  
  
## InteractionStartEvent

This item is deprecated!

Fields  
---  
`interaction` |  `[Interaction](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Interaction)`  
  
## InteractionStatusUpdate

Fields  
---  
`interaction_id` |  `string`  
`status` |  `[Status](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Interaction.Status)`  
  
## InteractionStreamingEvent

Fields  
---  
`event_id` |  `string` The event_id token to be used to resume the interaction stream, from this event.  
Union field `event_type`. The event data. `event_type` can be only one of the following:  
`interaction_start_event  
**(deprecated)**` |  `[InteractionStartEvent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.InteractionStartEvent)` This item is deprecated!The interaction data, used for interaction.start events. Legacy event, used when steps are disabled.  
`interaction_complete_event  
**(deprecated)**` |  `[InteractionCompleteEvent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.InteractionCompleteEvent)` This item is deprecated!The interaction data, used for interaction.complete events. Legacy event, used when steps are disabled.  
`interaction_created_event` |  `[InteractionCreatedSseEvent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.InteractionCreatedSseEvent)` The interaction data, used for interaction.created events. Used when steps are enabled.  
`interaction_completed_event` |  `[InteractionCompletedSseEvent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.InteractionCompletedSseEvent)` The interaction data, used for interaction.completed events. Used when steps are enabled.  
`interaction_status_update` |  `[InteractionStatusUpdate](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.InteractionStatusUpdate)` The interaction status data, used for interaction.status_update events.  
`content_start  
**(deprecated)**` |  `[ContentStart](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ContentStart)` This item is deprecated!The content block start data, used for content.start events. Legacy content-based streaming event, used when steps are disabled.  
`content_delta  
**(deprecated)**` |  `[ContentDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ContentDelta)` This item is deprecated!The content block delta data, used for content.delta events. Legacy content-based streaming event, used when steps are disabled.  
`content_stop  
**(deprecated)**` |  `[ContentStop](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ContentStop)` This item is deprecated!The content block stop data, used for content.stop events. Legacy content-based streaming event, used when steps are disabled.  
`error_event` |  `[ErrorEvent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ErrorEvent)` The error event data, used for error events.  
`step_start` |  `[StepStart](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.StepStart)` The step start data, used for step.start events. Step-based streaming event, used when steps are enabled.  
`step_delta` |  `[StepDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.StepDelta)` The step delta data, used for step.delta events. Step-based streaming event, used when steps are enabled.  
`step_stop` |  `[StepStop](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.StepStop)` The step stop data, used for step.stop events. Step-based streaming event, used when steps are enabled.  
  
## LegacyAudioContent

This item is deprecated!

Fields  
---  
`mime_type_string` |  `string`  
`rate` |  `int32`  
`channels` |  `int32`  
`sample_rate` |  `int32`  
Union field `data_or_uri`.`data_or_uri` can be only one of the following:  
`data` |  `bytes`  
`uri` |  `string`  
  
## LegacyDocumentContent

This item is deprecated!

Fields  
---  
`mime_type_string` |  `string`  
Union field `data_or_uri`.`data_or_uri` can be only one of the following:  
`data` |  `bytes`  
`uri` |  `string`  
  
## LegacyImageContent

This item is deprecated!

Fields  
---  
`mime_type_string` |  `string`  
`resolution` |  `[MediaResolution](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.MediaResolution)`  
Union field `data_or_uri`.`data_or_uri` can be only one of the following:  
`data` |  `bytes`  
`uri` |  `string`  
  
## LegacyTextContent

This item is deprecated!

Fields  
---  
`text` |  `string`  
`annotations[]` |  `[Annotation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.TextContent.Annotation)`  
  
## LegacyVideoContent

This item is deprecated!

Fields  
---  
`mime_type_string` |  `string`  
`resolution` |  `[MediaResolution](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.MediaResolution)`  
`name` |  `string`  
Union field `data_or_uri`.`data_or_uri` can be only one of the following:  
`data` |  `bytes`  
`uri` |  `string`  
Union field `processing`.`processing` can be only one of the following:  
`processing_type` |  `[Processing](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.VideoContent.Processing)`  
`processing_config` |  `[MediaProcessing](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.VideoContent.MediaProcessing)`  
  
## ListInteractionsHttpTranscoderRequest

Request message for InteractionsHttpService.ListInteractionsHttp.

Fields  
---  
`parent` |  `string` Required. The parent, which owns this collection of interactions. Format: `projects/{project}/locations/{location}`Supported only by the Agent Platform Platform.  
`page_size` |  `int32` The maximum number of `Interactions` to return (per page). The service may return fewer `Interactions`.If unspecified, at most 10 `Interactions` will be returned. The maximum size limit is 20 `Interactions` per page.  
`page_token` |  `string` A page token, received from a previous `ListInteractions` call.Provide the `next_page_token` returned in the response as an argument to the next request to retrieve the next page.When paginating, all other parameters provided to `ListInteractions` must match the call that provided the page token.  
  
## ListInteractionsRequest

Fields  
---  
`parent` |  `string` Required. The parent, which owns this collection of interactions. Format: `projects/{project}/locations/{location}`Supported only by the Agent Platform Platform.  
`page_size` |  `int32` The maximum number of `Interactions` to return (per page). The service may return fewer `Interactions`.If unspecified, at most 10 `Interactions` will be returned. The maximum size limit is 20 `Interactions` per page. Note: Vertex API does supports page size up to 500.  
`page_token` |  `string` A page token, received from a previous `ListInteractions` call.Provide the `next_page_token` returned in the response as an argument to the next request to retrieve the next page.When paginating, all other parameters provided to `ListInteractions` must match the call that provided the page token.Note: Vertex API does not enforce this requirement on page_size.  
  
## ListInteractionsResponse

Fields  
---  
`interaction_metadatas[]` |  `[InteractionMetadata](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.InteractionMetadata)` The `InteractionMetadata` from the specified collection.  
`next_page_token` |  `string` A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
## ListValue

`ListValue` is a wrapper around a repeated field of values.

Fields  
---  
`values[]` |  `[Value](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Value)` Repeated field of dynamically typed values.  
  
## LocalEnvironmentConfig

This type has no fields.

Configuration for an environment that lives on the client connection rather than in a server-managed sandbox.

When set (via Interaction.local_environment), the agent's filesystem and shell are treated as living on the client: the agent's built-in environment operations (e.g. reading/listing/editing files and running commands) are suspended on the server and yielded back to the client to execute, with their results returned on a subsequent turn. This is mutually exclusive with a server-managed `EnvironmentConfig` (remote_environment), since the environment is either on the client or in a server sandbox, never both.

This governs only the agent's built-in environment. Client-declared function tools are always executed on the client regardless of this field.

## McpServer

A MCPServer is a server that can be called by the model to perform actions.

Fields  
---  
`name` |  `string` The name of the MCPServer.  
`headers` |  `map<string, string>` Optional: Fields for authentication headers, timeouts, etc., if needed.  
`allowed_tools[]` |  `[AllowedTools](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.AllowedTools)` The allowed tools.  
Union field `transport`.`transport` can be only one of the following:  
`url` |  `string` The full URL for the MCPServer endpoint. Example: "https://api.example.com/mcp"  
  
## McpServerToolCallContent

MCPServer tool call content.

Fields  
---  
`name` |  `string` Required. The name of the tool which was called.  
`server_name` |  `string` Required. The name of the used MCP server.  
`arguments` |  `[Struct](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Struct)` Required. The JSON object of arguments for the function.  
  
## McpServerToolCallDelta

Fields  
---  
`name` |  `string`  
`server_name` |  `string`  
`arguments` |  `[Struct](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Struct)`  
  
## McpServerToolCallStep

MCPServer tool call step.

Fields  
---  
`name` |  `string` Required. The name of the tool which was called.  
`server_name` |  `string` Required. The name of the used MCP server.  
`arguments` |  `[Struct](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Struct)` Required. The JSON object of arguments for the function.  
  
## McpServerToolResultContent

MCPServer tool result content.

Fields  
---  
`name` |  `string` Name of the tool which is called for this specific tool call.  
`server_name` |  `string` The name of the used MCP server.  
Union field `result`. The output from the MCP server call. Can be simple text or rich content. `result` can be only one of the following:  
`struct_result` |  `[Struct](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Struct)`  
`content_list` |  `[FunctionResultSubcontentList](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.FunctionResultSubcontentList)`  
`string_result` |  `string`  
  
## McpServerToolResultDelta

Fields  
---  
`name` |  `string`  
`server_name` |  `string`  
`result` |  `[Value](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Value)`  
  
## McpServerToolResultStep

MCPServer tool result step.

Fields  
---  
`name` |  `string` Name of the tool which is called for this specific tool call.  
`server_name` |  `string` The name of the used MCP server.  
`result` |  `[Value](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Value)` Required. The output from the MCP server call. Can be simple text or rich content.  
  
## MediaResolution

Resolution for input media (images/video).

Enums  
---  
`MEDIA_RESOLUTION_UNSPECIFIED` | Default value. This value is unused.  
`LOW` | Low resolution.  
`MEDIUM` | Medium resolution.  
`HIGH` | High resolution.  
`ULTRA_HIGH` | Ultra high resolution.  
  
## ModelInteraction

Interaction for generating the completion using models.

Fields  
---  
`model` |  `string` The name of the `Model` used for generating the completion.  
`generation_config` |  `[GenerationConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GenerationConfig)` Input only. Configuration parameters for the model interaction.  
  
## ModelOutputStep

Output generated by the model.

Fields  
---  
`content[]` |  `[Content](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Content)`  
`error  
**(deprecated)**` |  `[Status](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/google.rpc#google.rpc.Status)` This item is deprecated!The error result of the operation in case of failure or cancellation.  
  
## ParallelAISearchConfig

Used to specify configuration for ParallelAISearch.

Fields  
---  
`api_key` |  `string` Optional. The API key for ParallelAiSearch.  
`custom_config` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` Optional. Custom configs for ParallelAiSearch.  
  
## PlaceCitation

A place citation annotation.

Fields  
---  
`place_id` |  `string` The ID of the place, in `places/{place_id}` format.  
`name` |  `string` Title of the place.  
`url` |  `string` URI reference of the place.  
`review_snippets[]` |  `[ReviewSnippet](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ReviewSnippet)` Snippets of reviews that are used to generate answers about the features of a given place in Google Maps.  
  
## RagStoreConfig

Use to specify configuration for RAG Store.

Fields  
---  
`rag_resources[]` |  `[RagResource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.RagStoreConfig.RagResource)` Optional. The representation of the rag source.  
`similarity_top_k  
**(deprecated)**` |  `int32` This item is deprecated!Optional. Number of top k results to return from the selected corpora.  
`vector_distance_threshold  
**(deprecated)**` |  `double` This item is deprecated!Optional. Only return results with vector distance smaller than the threshold.  
`rag_retrieval_config` |  `[RagRetrievalConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.RagStoreConfig.RagRetrievalConfig)` Optional. The retrieval config for the Rag query.  
  
## RagResource

The definition of the Rag resource.

Fields  
---  
`rag_corpus` |  `string` Optional. RagCorpora resource name.  
`rag_file_ids[]` |  `string` Optional. rag_file_id. The files should be in the same rag_corpus set in rag_corpus field.  
  
## RagRetrievalConfig

Specifies the context retrieval config.

Fields  
---  
`top_k` |  `int32` Optional. The number of contexts to retrieve.  
`hybrid_search` |  `[HybridSearch](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.RagStoreConfig.RagRetrievalConfig.HybridSearch)` Optional. Config for Hybrid Search.  
`filter` |  `[Filter](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.RagStoreConfig.RagRetrievalConfig.Filter)` Optional. Config for filters.  
`ranking` |  `[Ranking](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.RagStoreConfig.RagRetrievalConfig.Ranking)` Optional. Config for ranking and reranking.  
  
## Filter

Config for filters.

Fields  
---  
`metadata_filter` |  `string` Optional. String for metadata filtering.  
Union field `vector_db_threshold`. Filter contexts retrieved from the vector DB based on either vector distance or vector similarity. `vector_db_threshold` can be only one of the following:  
`vector_distance_threshold` |  `double` Optional. Only returns contexts with vector distance smaller than the threshold.  
`vector_similarity_threshold` |  `double` Optional. Only returns contexts with vector similarity larger than the threshold.  
  
## HybridSearch

Config for Hybrid Search.

Fields  
---  
`alpha` |  `float` Optional. Alpha value controls the weight between dense and sparse vector search results.  
  
## Ranking

Config for ranking and reranking.

Fields  
---  
Union field `ranking_config`. Config options for ranking. `ranking_config` can be only one of the following:  
`rank_service` |  `[RankService](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.RagStoreConfig.RagRetrievalConfig.Ranking.RankService)` Config for Rank Service.  
  
## RankService

Config for Rank Service.

Fields  
---  
`model_name` |  `string` Optional. The model name of the rank service.  
  
## ResponseFormat

Fields  
---  
Union field `type`.`type` can be only one of the following:  
`audio` |  `[AudioResponseFormat](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.AudioResponseFormat)`  
`text` |  `[TextResponseFormat](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.TextResponseFormat)`  
`image` |  `[ImageResponseFormat](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ImageResponseFormat)`  
`video` |  `[VideoResponseFormat](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.VideoResponseFormat)`  
`struct_value` |  `[Struct](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Struct)` Multi-discriminator values is already enabled in GAOS  
  
## ResponseFormatList

Fields  
---  
`response_formats[]` |  `[ResponseFormat](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ResponseFormat)`  
  
## ResponseModality

The modality of the response.

Enums  
---  
`RESPONSE_MODALITY_UNSPECIFIED` | Default value. This value is unused.  
`TEXT` | Indicates the model should return text.  
`IMAGE` | Indicates the model should return images.  
`AUDIO` | Indicates the model should return audio.  
`VIDEO` | Indicates the model should return video.  
`DOCUMENT` | Indicates the model should return documents.  
  
## Retrieval

A tool that can be used by the model to retrieve files.

Fields  
---  
`retrieval_types[]` |  `[RetrievalType](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Retrieval.RetrievalType)` The types of file retrieval to enable.  
`vertex_ai_search_config` |  `[VertexAISearchConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.VertexAISearchConfig)` Used to specify configuration for VertexAISearch.  
`exa_ai_search_config` |  `[ExaAISearchConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ExaAISearchConfig)` Used to specify configuration for ExaAISearch.  
`parallel_ai_search_config` |  `[ParallelAISearchConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ParallelAISearchConfig)` Used to specify configuration for ParallelAISearch.  
`rag_store_config` |  `[RagStoreConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.RagStoreConfig)` Used to specify configuration for RagStore.  
  
## RetrievalType

The types of file retrieval to enable.

Enums  
---  
`RETRIEVAL_TYPE_UNSPECIFIED` |   
`RETRIEVAL_TYPE_VERTEX_AI_SEARCH` |   
`RETRIEVAL_TYPE_RAG_STORE` |   
`RETRIEVAL_TYPE_EXA_AI_SEARCH` |   
`RETRIEVAL_TYPE_PARALLEL_AI_SEARCH` |   
  
## RetrievalCallDelta

Used by Vertex Retrieval tools such as Parallel AI, Exa AI, Agent Platform Search, etc. RetrievalType decides which tool is used.

Fields  
---  
`arguments` |  `[RetrievalStepArguments](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.RetrievalCallStep.RetrievalStepArguments)` Required. The arguments to pass to the Retrieval tool.  
`retrieval_type` |  `[RetrievalType](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Retrieval.RetrievalType)` The type of retrieval tools.  
  
## RetrievalCallStep

Retrieval call step. Used by Vertex Retrieval tools such as Parallel AI, Exa AI, Agent Platform Search, etc. RetrievalType decides which tool is used.

Fields  
---  
`arguments` |  `[RetrievalStepArguments](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.RetrievalCallStep.RetrievalStepArguments)` Required. The arguments to pass to the retrieval tool.  
`retrieval_type` |  `[RetrievalType](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Retrieval.RetrievalType)` The type of retrieval tools.  
  
## RetrievalStepArguments

The arguments to pass to Retrieval tools.

Fields  
---  
`queries[]` |  `string` Queries for Retrieval information.  
  
## RetrievalResultDelta

Used by Vertex Retrieval tools such as Parallel AI, Exa AI, Agent Platform Search, etc. ToolResultDelta.type

Fields  
---  
`is_error` |  `bool` Whether the retrieval resulted in an error.  
  
## RetrievalResultStep

Vertex Retrieval result step. Used by Vertex Retrieval tools such as Parallel AI, Exa AI, Agent Platform Search, etc.

Fields  
---  
`is_error` |  `bool` Whether the retrieval resulted in an error.  
  
## ReviewSnippet

Encapsulates a snippet of a user review that answers a question about the features of a specific place in Google Maps.

Fields  
---  
`title` |  `string` Title of the review.  
`url` |  `string` A link that corresponds to the user review on Google Maps.  
`review_id` |  `string` The ID of the review snippet.  
  
## SafetySetting

A safety setting that affects the safety-blocking behavior.

A `SafetySetting` consists of a harm `category` and a `threshold` for that category.

Fields  
---  
`type` |  `[HarmCategory](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.HarmCategory)` Required. The type of harm category to be blocked.  
`threshold` |  `[HarmBlockThreshold](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.SafetySetting.HarmBlockThreshold)` Required. The threshold for blocking content. If the harm probability exceeds this threshold, the content will be blocked.  
`method` |  `[HarmBlockMethod](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.SafetySetting.HarmBlockMethod)` Optional. The method for blocking content. If not specified, the default behavior is to use the probability score.  
  
## HarmBlockMethod

The method for blocking content.

Enums  
---  
`HARM_BLOCK_METHOD_UNSPECIFIED` | The harm block method is unspecified.  
`SEVERITY` | The harm block method uses both probability and severity scores.  
`PROBABILITY` | The harm block method uses the probability score.  
  
## HarmBlockThreshold

Thresholds for blocking content based on harm probability.

Enums  
---  
`HARM_BLOCK_THRESHOLD_UNSPECIFIED` | The harm block threshold is unspecified.  
`BLOCK_LOW_AND_ABOVE` | Block content with a low harm probability or higher.  
`BLOCK_MEDIUM_AND_ABOVE` | Block content with a medium harm probability or higher.  
`BLOCK_ONLY_HIGH` | Block content with a high harm probability.  
`BLOCK_NONE` | Do not block any content, regardless of its harm probability.  
`OFF` | Turn off the safety filter entirely.  
  
## ServerToolCallDelta

Fields  
---  
`signature` |  `bytes` A signature hash for backend validation.  
Union field `type`.`type` can be only one of the following:  
`code_execution_call` |  `[CodeExecutionCallDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.CodeExecutionCallDelta)`  
`url_context_call` |  `[UrlContextCallDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.UrlContextCallDelta)`  
`google_search_call` |  `[GoogleSearchCallDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GoogleSearchCallDelta)`  
`mcp_server_tool_call` |  `[McpServerToolCallDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.McpServerToolCallDelta)`  
`file_search_call` |  `[FileSearchCallDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.FileSearchCallDelta)`  
`google_maps_call` |  `[GoogleMapsCallDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GoogleMapsCallDelta)`  
`retrieval_call` |  `[RetrievalCallDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.RetrievalCallDelta)`  
  
## ServerToolResultDelta

Fields  
---  
`signature` |  `bytes` A signature hash for backend validation.  
Union field `type`.`type` can be only one of the following:  
`code_execution_result` |  `[CodeExecutionResultDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.CodeExecutionResultDelta)`  
`url_context_result` |  `[UrlContextResultDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.UrlContextResultDelta)`  
`google_search_result` |  `[GoogleSearchResultDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GoogleSearchResultDelta)`  
`mcp_server_tool_result` |  `[McpServerToolResultDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.McpServerToolResultDelta)`  
`file_search_result` |  `[FileSearchResultDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.FileSearchResultDelta)`  
`google_maps_result` |  `[GoogleMapsResultDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GoogleMapsResultDelta)`  
`retrieval_result` |  `[RetrievalResultDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.RetrievalResultDelta)`  
  
## Step

A step in the interaction.

Fields  
---  
Union field `type`.`type` can be only one of the following:  
`thought` |  `[ThoughtStep](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ThoughtStep)`  
`tool_call` |  `[ToolCallStep](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ToolCallStep)`  
`tool_result` |  `[ToolResultStep](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ToolResultStep)`  
`user_input` |  `[UserInputStep](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.UserInputStep)` DO NOT USE -- These are for 3P JSON only  
`model_output` |  `[ModelOutputStep](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ModelOutputStep)`  
`text  
**(deprecated)**` |  `[LegacyTextContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.LegacyTextContent)` This item is deprecated!  
`image  
**(deprecated)**` |  `[LegacyImageContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.LegacyImageContent)` This item is deprecated!  
`audio  
**(deprecated)**` |  `[LegacyAudioContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.LegacyAudioContent)` This item is deprecated!  
`document  
**(deprecated)**` |  `[LegacyDocumentContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.LegacyDocumentContent)` This item is deprecated!  
`video  
**(deprecated)**` |  `[LegacyVideoContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.LegacyVideoContent)` This item is deprecated!  
  
## StepDelta

Fields  
---  
`index` |  `int32`  
`delta` |  `[StepDeltaData](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.StepDeltaData)`  
  
## StepDeltaData

Fields  
---  
Union field `type`.`type` can be only one of the following:  
`text` |  `[TextDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.TextDelta)`  
`image` |  `[ImageDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ImageDelta)`  
`audio` |  `[AudioDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.AudioDelta)`  
`document` |  `[DocumentDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.DocumentDelta)`  
`video` |  `[VideoDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.VideoDelta)`  
`thought_summary` |  `[ThoughtSummaryDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ThoughtSummaryDelta)`  
`thought_signature` |  `[ThoughtSignatureDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ThoughtSignatureDelta)`  
`text_annotation_delta` |  `[TextAnnotationDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.TextAnnotationDelta)`  
`arguments_delta` |  `[ArgumentsDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ArgumentsDelta)`  
`server_tool_call` |  `[ServerToolCallDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ServerToolCallDelta)`  
`server_tool_result` |  `[ServerToolResultDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ServerToolResultDelta)`  
`function_result` |  `[FunctionResultDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.FunctionResultDelta)`  
  
## StepList

A list of Steps.

Fields  
---  
`steps[]` |  `[Step](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Step)` The steps of the list.  
  
## StepStart

Fields  
---  
`index` |  `int32`  
`step` |  `[Step](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Step)`  
  
## StepStop

Fields  
---  
`index` |  `int32`  
`usage` |  `[Usage](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Interaction.Usage)` Cumulative model usage stats from the start of the session.  
`step_usage` |  `[Usage](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Interaction.Usage)` Model usage stats for this specific step.  
  
## Struct

`Struct` represents a structured data value, consisting of fields which map to dynamically typed values.

Fields  
---  
`fields[]` |  `[Field](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Field)` Dynamically typed fields. List instead of map because LLMs are sensitive to ordering, and we want to give users full control.  
  
## TextAnnotationDelta

Fields  
---  
`annotations[]` |  `[Annotation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.TextContent.Annotation)` Citation information for model-generated content.  
  
## TextContent

A text content block.

Fields  
---  
`text` |  `string` Required. The text content.  
`annotations[]` |  `[Annotation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.TextContent.Annotation)` Citation information for model-generated content.  
  
## Annotation

Citation information for model-generated content.

Fields  
---  
`start_index` |  `int32` Start of segment of the response that is attributed to this source.Index indicates the start of the segment, measured in bytes.  
`end_index` |  `int32` End of the attributed segment, exclusive.  
Union field `type`. The type of annotation. `type` can be only one of the following:  
`url_citation` |  `[UrlCitation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.UrlCitation)` NOTE: We use these instead of the Citation message for historical reasons. A URL citation annotation.  
`file_citation` |  `[FileCitation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.FileCitation)` A file citation annotation.  
`place_citation` |  `[PlaceCitation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.PlaceCitation)` A place citation annotation.  
`word_info` |  `[WordInfo](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.WordInfo)` Word-level ASR annotation with timing and speaker info.  
  
## TextDelta

Fields  
---  
`text` |  `string`  
  
## TextResponseFormat

Configuration for text output format.

Fields  
---  
`mime_type` |  `[MimeType](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.TextResponseFormat.MimeType)` The MIME type of the text output.  
`schema` |  `[Struct](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Struct)` The JSON schema that the output should conform to. Only applicable when mime_type is application/json.  
  
## MimeType

Supported MIME types for text output.

Enums  
---  
`TYPE_UNSPECIFIED` | Default value. This value is unused.  
`TYPE_APPLICATION_JSON` | JSON output format.  
`TYPE_TEXT_PLAIN` | Plain text output format.  
  
## ThinkingLevel

The level of thought tokens that the model should generate.

Enums  
---  
`THINKING_LEVEL_UNSPECIFIED` | Default value. This value is unused.  
`THINKING_LEVEL_MINIMAL` | Little to no thinking.  
`THINKING_LEVEL_LOW` | Low thinking level.  
`THINKING_LEVEL_MEDIUM` | Medium thinking level.  
`THINKING_LEVEL_HIGH` | High thinking level.  
  
## ThinkingSummaries

Whether to include thought summaries in the response.

Enums  
---  
`THINKING_SUMMARIES_UNSPECIFIED` | Default value. This value is unused.  
`THINKING_SUMMARIES_AUTO` | Auto thinking summaries.  
`THINKING_SUMMARIES_NONE` | No thinking summaries.  
  
## ThoughtContent

This item is deprecated!

A thought content block.

Fields  
---  
`signature` |  `bytes` Signature to match the backend source to be part of the generation.  
  
## ThoughtSignatureDelta

Fields  
---  
`signature` |  `bytes` Signature to match the backend source to be part of the generation.  
  
## ThoughtStep

A thought step.

Fields  
---  
`signature` |  `bytes` A signature hash for backend validation.  
`summary[]` |  `[Content](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Content)` A summary of the thought.  
  
## ThoughtSummaryContent

Fields  
---  
Union field `type`.`type` can be only one of the following:  
`text` |  `[TextContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.TextContent)`  
`image` |  `[ImageContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ImageContent)`  
  
## ThoughtSummaryDelta

Fields  
---  
`content` |  `[Content](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Content)` A new summary item to be added to the thought.  
  
## Tool

A tool that can be used by the model.

Fields  
---  
Union field `type`. The tool to use. `type` can be only one of the following:  
`function` |  `[Function](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Function)` A function that can be used by the model.  
`code_execution` |  `[CodeExecution](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.CodeExecution)` A tool that can be used by the model to execute code.  
`url_context` |  `[UrlContext](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.UrlContext)` A tool that can be used by the model to fetch URL context.  
`computer_use` |  `[ComputerUse](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ComputerUse)` Tool to support the model interacting directly with the computer.  
`mcp_server` |  `[McpServer](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.McpServer)` A MCPServer is a server that can be called by the model to perform actions.  
`google_search` |  `[GoogleSearch](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GoogleSearch)` A tool that can be used by the model to search Google.  
`file_search` |  `[FileSearch](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.FileSearch)` A tool that can be used by the model to search files.  
`google_maps` |  `[GoogleMaps](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GoogleMaps)` A tool that can be used by the model to search Google Maps.  
`retrieval` |  `[Retrieval](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Retrieval)` A tool that can be used by the model to retrieve files.  
  
## ToolCallContent

This item is deprecated!

Tool call content.

Fields  
---  
`id` |  `string` Required. A unique ID for this specific tool call.  
`signature` |  `bytes` A signature hash for backend validation.  
Union field `type`.`type` can be only one of the following:  
`function_call` |  `[FunctionCallContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.FunctionCallContent)`  
`code_execution_call` |  `[CodeExecutionCallContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.CodeExecutionCallContent)`  
`url_context_call` |  `[UrlContextCallContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.UrlContextCallContent)`  
`mcp_server_tool_call` |  `[McpServerToolCallContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.McpServerToolCallContent)`  
`google_search_call` |  `[GoogleSearchCallContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GoogleSearchCallContent)`  
`file_search_call` |  `[FileSearchCallContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.FileSearchCallContent)`  
`google_maps_call` |  `[GoogleMapsCallContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GoogleMapsCallContent)`  
  
## ToolCallDelta

Fields  
---  
`id` |  `string` Required. A unique ID for this specific tool call.  
`signature` |  `bytes` A signature hash for backend validation.  
Union field `type`.`type` can be only one of the following:  
`function_call` |  `[FunctionCallDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.FunctionCallDelta)`  
`code_execution_call` |  `[CodeExecutionCallDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.CodeExecutionCallDelta)`  
`url_context_call` |  `[UrlContextCallDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.UrlContextCallDelta)`  
`google_search_call` |  `[GoogleSearchCallDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GoogleSearchCallDelta)`  
`mcp_server_tool_call` |  `[McpServerToolCallDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.McpServerToolCallDelta)`  
`file_search_call` |  `[FileSearchCallDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.FileSearchCallDelta)`  
`google_maps_call` |  `[GoogleMapsCallDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GoogleMapsCallDelta)`  
  
## ToolCallStep

Tool call step.

Fields  
---  
`id` |  `string` Required. A unique ID for this specific tool call.  
`signature` |  `bytes` A signature hash for backend validation.  
Union field `type`.`type` can be only one of the following:  
`function_call` |  `[FunctionCallStep](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.FunctionCallStep)`  
`code_execution_call` |  `[CodeExecutionCallStep](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.CodeExecutionCallStep)`  
`url_context_call` |  `[UrlContextCallStep](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.UrlContextCallStep)`  
`mcp_server_tool_call` |  `[McpServerToolCallStep](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.McpServerToolCallStep)`  
`google_search_call` |  `[GoogleSearchCallStep](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GoogleSearchCallStep)`  
`file_search_call` |  `[FileSearchCallStep](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.FileSearchCallStep)`  
`google_maps_call` |  `[GoogleMapsCallStep](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GoogleMapsCallStep)`  
`retrieval_call` |  `[RetrievalCallStep](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.RetrievalCallStep)`  
  
## ToolChoiceConfig

The tool choice configuration containing allowed tools.

Fields  
---  
`allowed_tools` |  `[AllowedTools](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.AllowedTools)` The allowed tools.  
  
## ToolChoiceType

The type of tool choice.

Enums  
---  
`TOOL_CHOICE_TYPE_UNSPECIFIED` | Default value. This value is unused.  
`AUTO` | Auto tool choice.  
`ANY` | Any tool choice.  
`NONE` | No tool choice.  
`VALIDATED` | Validated tool choice.  
  
## ToolResultContent

This item is deprecated!

Tool result content.

Fields  
---  
`call_id` |  `string` Required. ID to match the ID from the function call block.  
`signature` |  `bytes` A signature hash for backend validation.  
Union field `type`.`type` can be only one of the following:  
`function_result` |  `[FunctionResultContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.FunctionResultContent)`  
`code_execution_result` |  `[CodeExecutionResultContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.CodeExecutionResultContent)`  
`url_context_result` |  `[UrlContextResultContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.UrlContextResultContent)`  
`google_search_result` |  `[GoogleSearchResultContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GoogleSearchResultContent)`  
`mcp_server_tool_result` |  `[McpServerToolResultContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.McpServerToolResultContent)`  
`file_search_result` |  `[FileSearchResultContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.FileSearchResultContent)`  
`google_maps_result` |  `[GoogleMapsResultContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GoogleMapsResultContent)`  
  
## ToolResultDelta

Fields  
---  
`call_id` |  `string` Required. ID to match the ID from the function call block.  
`signature` |  `bytes` A signature hash for backend validation.  
Union field `type`.`type` can be only one of the following:  
`function_result` |  `[FunctionResultDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.FunctionResultDelta)`  
`code_execution_result` |  `[CodeExecutionResultDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.CodeExecutionResultDelta)`  
`url_context_result` |  `[UrlContextResultDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.UrlContextResultDelta)`  
`google_search_result` |  `[GoogleSearchResultDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GoogleSearchResultDelta)`  
`mcp_server_tool_result` |  `[McpServerToolResultDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.McpServerToolResultDelta)`  
`file_search_result` |  `[FileSearchResultDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.FileSearchResultDelta)`  
`google_maps_result` |  `[GoogleMapsResultDelta](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GoogleMapsResultDelta)`  
  
## ToolResultStep

Tool result step.

Fields  
---  
`call_id` |  `string` Required. ID to match the ID from the function call block.  
`signature` |  `bytes` A signature hash for backend validation.  
Union field `type`.`type` can be only one of the following:  
`function_result` |  `[FunctionResultStep](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.FunctionResultStep)`  
`code_execution_result` |  `[CodeExecutionResultStep](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.CodeExecutionResultStep)`  
`url_context_result` |  `[UrlContextResultStep](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.UrlContextResultStep)`  
`google_search_result` |  `[GoogleSearchResultStep](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GoogleSearchResultStep)`  
`mcp_server_tool_result` |  `[McpServerToolResultStep](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.McpServerToolResultStep)`  
`file_search_result` |  `[FileSearchResultStep](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.FileSearchResultStep)`  
`google_maps_result` |  `[GoogleMapsResultStep](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.GoogleMapsResultStep)`  
`retrieval_result` |  `[RetrievalResultStep](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.RetrievalResultStep)`  
  
## TranscriptionConfig

Configuration for speech recognition (transcription).

Fields  
---  
`language_codes[]` |  `string` Optional. BCP-47 language codes providing hints about the languages present in the audio. If omitted or empty, defaults to automatic language detection.  
`custom_vocabulary[]` |  `string` Optional. A list of custom vocabulary phrases to bias the speech recognition model toward recognizing specific terms.  
`timestamp_granularities[]  
**(deprecated)**` |  `string` This item is deprecated!Optional. The granularity of timestamps to include in the transcription output. Supported values: "word". If empty, no timestamps are generated.  
`diarization_mode  
**(deprecated)**` |  `string` This item is deprecated!Optional. Configures speaker diarization. Supported values: "speaker".  
`adaptation_phrases[]  
**(deprecated)**` |  `string` This item is deprecated!Optional. A list of phrases to bias the ASR model towards.  
  
## Turn

This item is deprecated!

Fields  
---  
`role` |  `string` The originator of this turn. Must be user for input or model for model output.  
Union field `content`.`content` can be only one of the following:  
`content_list` |  `[ContentList](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ContentList)` The content of the turn. An array of Content objects.  
`content_string` |  `string` The content of the turn. A single string.  
  
## TurnList

This type has no fields.

This item is deprecated!

A list of Turns.

## UrlCitation

A URL citation annotation.

Fields  
---  
`url` |  `string` The URL.  
`title` |  `string` The title of the URL.  
  
## UrlContext

This type has no fields.

A tool that can be used by the model to fetch URL context.

## UrlContextCallContent

This item is deprecated!

URL context content.

Fields  
---  
`arguments` |  `[UrlContextCallArguments](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.UrlContextCallContent.UrlContextCallArguments)` Required. The arguments to pass to the URL context.  
  
## UrlContextCallArguments

The arguments to pass to the URL context.

Fields  
---  
`urls[]` |  `string` The URLs to fetch.  
  
## UrlContextCallDelta

Fields  
---  
`arguments` |  `[UrlContextCallArguments](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.UrlContextCallContent.UrlContextCallArguments)`  
  
## UrlContextCallStep

URL context call step.

Fields  
---  
`arguments` |  `[UrlContextCallStepArguments](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.UrlContextCallStep.UrlContextCallStepArguments)` Required. The arguments to pass to the URL context.  
  
## UrlContextCallStepArguments

The arguments to pass to the URL context.

Fields  
---  
`urls[]` |  `string` The URLs to fetch.  
  
## UrlContextResultContent

This item is deprecated!

URL context result content.

Fields  
---  
`result[]` |  `[UrlContextResult](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.UrlContextResultContent.UrlContextResult)` Required. The results of the URL context.  
`is_error` |  `bool` Whether the URL context resulted in an error.  
  
## UrlContextResult

The result of the URL context.

Fields  
---  
`url` |  `string` The URL that was fetched.  
`status` |  `[Status](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.UrlContextResultContent.UrlContextResult.Status)` The status of the URL retrieval.  
  
## Status

The status of the URL retrieval.

Enums  
---  
`STATUS_UNSPECIFIED` | Unspecified status. This value should not be used.  
`SUCCESS` | Url retrieval is successful.  
`ERROR` | Url retrieval is failed due to error.  
`PAYWALL` | Url retrieval is failed because the content is behind paywall.  
`UNSAFE` | Url retrieval is failed because the content is unsafe.  
  
## UrlContextResultDelta

Fields  
---  
`result[]` |  `[UrlContextResult](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.UrlContextResultContent.UrlContextResult)`  
`is_error` |  `bool`  
  
## UrlContextResultStep

URL context result step.

Fields  
---  
`result[]` |  `[UrlContextResultItem](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.UrlContextResultStep.UrlContextResultItem)` Required. The results of the URL context.  
`is_error` |  `bool` Whether the URL context resulted in an error.  
  
## UrlContextResultItem

The result of the URL context.

Fields  
---  
`url` |  `string` The URL that was fetched.  
`status` |  `[Status](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.UrlContextResultStep.UrlContextResultItem.Status)` The status of the URL retrieval.  
  
## Status

The status of the URL retrieval.

Enums  
---  
`STATUS_UNSPECIFIED` |   
`SUCCESS` |   
`ERROR` |   
`PAYWALL` |   
`UNSAFE` |   
  
## UserInputStep

Input provided by the user.

Fields  
---  
Union field `content`.`content` can be only one of the following:  
`content_list` |  `[ContentList](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ContentList)` The content of the step. An array of Content objects.  
`content_string` |  `string` The content of the step. A single string.  
  
## Value

`Value` represents a dynamically typed value which can be either null, a number, a string, a boolean, a recursive struct value, or a list of values. A producer of value is expected to set one of these variants. Absence of any variant indicates an error.

Fields  
---  
Union field `kind`. The kind of value. `kind` can be only one of the following:  
`null_value` |  `[NullValue](https://protobuf.dev/reference/protobuf/google.protobuf/#null-value)` Represents a null value.  
`number_value` |  `double` Represents a double value.  
`string_value` |  `string` Represents a string value.  
`bool_value` |  `bool` Represents a boolean value.  
`struct_value` |  `[Struct](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Struct)` Represents a structured value.  
`list_value` |  `[ListValue](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.ListValue)` Represents a repeated `Value`.  
`content_value` |  `[Content](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.Content)` Represents rich content (text, image, etc.).  
  
## VertexAISearchConfig

Used to specify configuration for VertexAISearch.

Fields  
---  
`engine` |  `string` Optional. Used to specify Agent Platform Search engine.  
`datastores[]` |  `string` Optional. Used to specify Agent Platform Search datastores.  
  
## VideoConfig

Configuration options for video generation.

Fields  
---  
`task` |  `[Task](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.VideoConfig.Task)` Optional task mode for video generation. If not specified, the model automatically determines the appropriate mode based on the provided text prompt and input media.  
  
## Task

Supported video generation tasks.

Enums  
---  
`TASK_UNSPECIFIED` | Unspecified task. The task is inferred from the input prompt and media.  
`TEXT_TO_VIDEO` | Generates video solely from a text prompt.  
`IMAGE_TO_VIDEO` | Generates video from one or two source images. The first image defines the starting frame, and the optional second image defines the ending frame.  
`REFERENCE_TO_VIDEO` | Generates video using reference media (such as images, audio, or video).  
`EDIT` | Modifies an existing input video.  
`EXTEND` | Extends an existing input video.  
  
## VideoContent

A video content block.

Fields  
---  
`mime_type_string` |  `string` Flexible MIME type string of the video, superseding mime_type = 1. Note: Bespoke logic in the GAOS parser/serializer maps this to the "mime_type" JSON key.  
`resolution` |  `[MediaResolution](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.MediaResolution)` The resolution of the media.  
`name` |  `string` A user-defined name for this content block. Can be referenced by the model in the final response.  
Union field `data_or_uri`. The video content. `data_or_uri` can be only one of the following:  
`data` |  `bytes` The video content.  
`uri` |  `string` The URI of the video.  
Union field `processing`. How the model processes this video for understanding. `processing` can be only one of the following:  
`processing_type` |  `[Processing](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.VideoContent.Processing)`  
`processing_config` |  `[MediaProcessing](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.VideoContent.MediaProcessing)`  
  
## MediaProcessing

Fields  
---  
Union field `type`.`type` can be only one of the following:  
`static` |  `[StaticMediaProcessing](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.VideoContent.StaticMediaProcessing)`  
  
## MimeType

Enums  
---  
`TYPE_UNSPECIFIED` |   
`TYPE_MP4` | MP4 video format  
`TYPE_MPEG` | MPEG video format  
`TYPE_MPG` | MPG video format  
`TYPE_MOV` | MOV video format  
`TYPE_AVI` | AVI video format  
`TYPE_X_FLV` | FLV video format  
`TYPE_WEBM` | WebM video format  
`TYPE_WMV` | WMV video format  
`TYPE_3GPP` | 3GPP video format  
`TYPE_YT_BEYOND` | YouTube video format (internal)  
`TYPE_JPEG2000` | JPEG 2000 video format  
  
## Processing

How the model processes input media for understanding.

Enums  
---  
`PROCESSING_UNSPECIFIED` | Default. Uses model-specific processing (3.5 Pro+ --> AGENTIC, older models --> STATIC)  
`STATIC` | Fixed-rate frame extraction. All frames placed in context.  
`AGENTIC` | Model-driven dynamic navigation.  
  
## StaticMediaProcessing

Fields  
---  
`start_offset` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Optional. Segment start time. Specified as a decimal number of seconds followed by an 's' suffix, e.g., "10.5s". Must be non-negative.  
`end_offset` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Optional. Segment end time. Specified as a decimal number of seconds followed by an 's' suffix, e.g., "30s". Must be non-negative and greater than `start_offset` if `start_offset` is set.  
`fps` |  `double` Optional. Video frame-rate sampling density.  
  
## VideoDelta

Fields  
---  
`mime_type` |  `[MimeType](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.VideoContent.MimeType)`  
`resolution` |  `[MediaResolution](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.MediaResolution)` The resolution of the media.  
Union field `data_or_uri`.`data_or_uri` can be only one of the following:  
`data` |  `bytes`  
`uri` |  `string`  
  
## VideoResponseFormat

Configuration for video output format.

Fields  
---  
`delivery` |  `[Delivery](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.VideoResponseFormat.Delivery)` The delivery mode for the video output.  
`gcs_uri` |  `string` The Cloud Storage URI to store the video output. Required for Vertex if delivery mode is URI.  
`aspect_ratio` |  `[AspectRatio](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.VideoResponseFormat.AspectRatio)` The aspect ratio for the video output.  
`duration` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` The duration for the video output.  
`resolution` |  `[Resolution](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rpc/genai.vertex.v1beta1#genai.vertex.v1beta1.VideoResponseFormat.Resolution)` The video output resolution. Defaults to 720p.  
  
## AspectRatio

Supported aspect ratios for video output.

Enums  
---  
`ASPECT_RATIO_UNSPECIFIED` | Default value. This value is unused.  
`ASPECT_RATIO_SIXTEEN_BY_NINE` | 16:9 aspect ratio.  
`ASPECT_RATIO_NINE_BY_SIXTEEN` | 9:16 aspect ratio.  
  
## Delivery

Delivery mode for video output.

Enums  
---  
`DELIVERY_UNSPECIFIED` | Default value. This value is unused.  
`INLINE` | Video data is returned inline in the response.  
`URI` | Video data is returned as a URI.  
  
## Resolution

Supported resolutions for video output.

Enums  
---  
`RESOLUTION_UNSPECIFIED` | Default value. This value is unused.  
`RESOLUTION_THREE_SIXTY_P` | 360p resolution.  
`RESOLUTION_SEVEN_TWENTY_P` | 720p resolution.  
`RESOLUTION_TEN_EIGHTY_P` | 1080p resolution.  
`RESOLUTION_FOUR_K` | 4K resolution.  
  
## WordInfo

Word-level ASR annotation for transcription output. Carries the word text, optional timing, and optional speaker attribution.

Fields  
---  
`text` |  `string` The transcribed word.  
`start_offset` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Start offset in time of the word relative to the start of the audio. Present when timestamp_granularities contains "word".  
`end_offset` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` End offset in time of the word relative to the start of the audio. Present when timestamp_granularities contains "word".  
`speaker` |  `string` Optional. Speaker label for this word (e.g. "spk_1", "spk_2"). Present when diarization_mode is set in TranscriptionConfig.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
