---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3
title: Dialogflow v3 API - Namespace Google.Cloud.Dialogflow.Cx.V3 (3.2.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:30:41.328061+00:00
---

# Dialogflow v3 API - Namespace Google.Cloud.Dialogflow.Cx.V3 (3.2.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Dialogflow v3 API - Namespace Google.Cloud.Dialogflow.Cx.V3 (3.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.2.0 (latest)  3.1.0  3.0.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 

## Classes 

### [Action](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Action)

Action performed by end user or Dialogflow agent in the conversation.

### [AdvancedSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AdvancedSettings)

Hierarchical advanced settings for agent/flow/page/fulfillment/parameter. Settings exposed at lower level overrides the settings exposed at higher level. Overriding occurs at the sub-setting level. For example, the playback_interruption_settings at fulfillment level only overrides the playback_interruption_settings at the agent level, leaving other settings at the agent level unchanged.

DTMF settings does not override each other. DTMF settings set at different levels define DTMF detections running in parallel.

Hierarchy: Agent->Flow->Page->Fulfillment/Parameter.

### [AdvancedSettings.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AdvancedSettings.Types)

Container for nested types declared in the AdvancedSettings message type.

### [AdvancedSettings.Types.DtmfSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AdvancedSettings.Types.DtmfSettings)

Define behaviors for DTMF (dual tone multi frequency).

### [AdvancedSettings.Types.LoggingSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AdvancedSettings.Types.LoggingSettings)

Define behaviors on logging.

### [AdvancedSettings.Types.SpeechSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AdvancedSettings.Types.SpeechSettings)

Define behaviors of speech to text detection.

### [Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent)

Agents are best described as Natural Language Understanding (NLU) modules that transform user requests into actionable data. You can include agents in your app, product, or service to determine user intent and respond to the user in a natural way.

After you create an agent, you can add [Intents][google.cloud.dialogflow.cx.v3.Intent], [Entity Types][google.cloud.dialogflow.cx.v3.EntityType], [Flows][google.cloud.dialogflow.cx.v3.Flow], [Fulfillments][google.cloud.dialogflow.cx.v3.Fulfillment], [Webhooks][google.cloud.dialogflow.cx.v3.Webhook], [TransitionRouteGroups][google.cloud.dialogflow.cx.v3.TransitionRouteGroup] and so on to manage the conversation flows.

### [Agent.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent.Types)

Container for nested types declared in the Agent message type.

### [Agent.Types.AnswerFeedbackSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent.Types.AnswerFeedbackSettings)

Settings for answer feedback collection.

### [Agent.Types.ClientCertificateSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent.Types.ClientCertificateSettings)

Settings for custom client certificates.

### [Agent.Types.GenAppBuilderSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent.Types.GenAppBuilderSettings)

Settings for Gen App Builder.

### [Agent.Types.GitIntegrationSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent.Types.GitIntegrationSettings)

Settings for connecting to Git repository for an agent.

### [Agent.Types.GitIntegrationSettings.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent.Types.GitIntegrationSettings.Types)

Container for nested types declared in the GitIntegrationSettings message type.

### [Agent.Types.GitIntegrationSettings.Types.GithubSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent.Types.GitIntegrationSettings.Types.GithubSettings)

Settings of integration with GitHub.

### [Agent.Types.PersonalizationSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent.Types.PersonalizationSettings)

Settings for end user personalization.

### [AgentGenerativeSettingsName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentGenerativeSettingsName)

Resource name for the `AgentGenerativeSettings` resource.

### [AgentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentName)

Resource name for the `Agent` resource.

### [AgentUtterance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentUtterance)

AgentUtterance represents one message sent by the agent.

### [AgentValidationResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentValidationResult)

The response message for [Agents.GetAgentValidationResult][google.cloud.dialogflow.cx.v3.Agents.GetAgentValidationResult].

### [AgentValidationResultName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentValidationResultName)

Resource name for the `AgentValidationResult` resource.

### [Agents](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agents)

Service for managing [Agents][google.cloud.dialogflow.cx.v3.Agent].

### [Agents.AgentsBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agents.AgentsBase)

Base class for server-side implementations of Agents

### [Agents.AgentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agents.AgentsClient)

Client for Agents

### [AgentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentsClient)

Agents client wrapper, for convenient use.

### [AgentsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentsClientBuilder)

Builder class for [AgentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentsClient) to provide simple configuration of credentials, endpoint etc.

### [AgentsClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentsClientImpl)

Agents client wrapper implementation, for convenient use.

### [AgentsSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentsSettings)

Settings for [AgentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentsClient) instances.

### [AnswerFeedback](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AnswerFeedback)

Stores information about feedback provided by users about a response.

### [AnswerFeedback.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AnswerFeedback.Types)

Container for nested types declared in the AnswerFeedback message type.

### [AnswerFeedback.Types.RatingReason](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AnswerFeedback.Types.RatingReason)

Stores extra information about why users provided thumbs down rating.

### [AudioInput](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AudioInput)

Represents the natural speech audio to be processed.

### [BargeInConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.BargeInConfig)

Configuration of the barge-in behavior. Barge-in instructs the API to return a detected utterance at a proper time while the client is playing back the response audio from a previous request. When the client sees the utterance, it should stop the playback and immediately get ready for receiving the responses for the current request.

The barge-in handling requires the client to start streaming audio input as soon as it starts playing back the audio from the previous response. The playback is modeled into two phases:

  * No barge-in phase: which goes first and during which speech detection should not be carried out.

  * Barge-in phase: which follows the no barge-in phase and during which the API starts speech detection and may inform the client that an utterance has been detected. Note that no-speech event is not expected in this phase.




The client provides this configuration in terms of the durations of those two phases. The durations are measured in terms of the audio length from the start of the input audio.

No-speech event is a response with END_OF_UTTERANCE without any transcript following up.

### [BatchDeleteTestCasesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.BatchDeleteTestCasesRequest)

The request message for [TestCases.BatchDeleteTestCases][google.cloud.dialogflow.cx.v3.TestCases.BatchDeleteTestCases].

### [BatchRunTestCasesMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.BatchRunTestCasesMetadata)

Metadata returned for the [TestCases.BatchRunTestCases][google.cloud.dialogflow.cx.v3.TestCases.BatchRunTestCases] long running operation.

### [BatchRunTestCasesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.BatchRunTestCasesRequest)

The request message for [TestCases.BatchRunTestCases][google.cloud.dialogflow.cx.v3.TestCases.BatchRunTestCases].

### [BatchRunTestCasesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.BatchRunTestCasesResponse)

The response message for [TestCases.BatchRunTestCases][google.cloud.dialogflow.cx.v3.TestCases.BatchRunTestCases].

### [BoostSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.BoostSpec)

Boost specification to boost certain documents. A copy of google.cloud.discoveryengine.v1main.BoostSpec, field documentation is available at <https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/BoostSpec>

### [BoostSpec.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.BoostSpec.Types)

Container for nested types declared in the BoostSpec message type.

### [BoostSpec.Types.ConditionBoostSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.BoostSpec.Types.ConditionBoostSpec)

Boost applies to documents which match a condition.

### [BoostSpec.Types.ConditionBoostSpec.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.BoostSpec.Types.ConditionBoostSpec.Types)

Container for nested types declared in the ConditionBoostSpec message type.

### [BoostSpec.Types.ConditionBoostSpec.Types.BoostControlSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.BoostSpec.Types.ConditionBoostSpec.Types.BoostControlSpec)

Specification for custom ranking based on customer specified attribute value. It provides more controls for customized ranking than the simple (condition, boost) combination above.

### [BoostSpec.Types.ConditionBoostSpec.Types.BoostControlSpec.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.BoostSpec.Types.ConditionBoostSpec.Types.BoostControlSpec.Types)

Container for nested types declared in the BoostControlSpec message type.

### [BoostSpec.Types.ConditionBoostSpec.Types.BoostControlSpec.Types.ControlPoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.BoostSpec.Types.ConditionBoostSpec.Types.BoostControlSpec.Types.ControlPoint)

The control points used to define the curve. The curve defined through these control points can only be monotonically increasing or decreasing(constant values are acceptable).

### [BoostSpecs](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.BoostSpecs)

Boost specifications for data stores.

### [CalculateCoverageRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.CalculateCoverageRequest)

The request message for [TestCases.CalculateCoverage][google.cloud.dialogflow.cx.v3.TestCases.CalculateCoverage].

### [CalculateCoverageRequest.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.CalculateCoverageRequest.Types)

Container for nested types declared in the CalculateCoverageRequest message type.

### [CalculateCoverageResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.CalculateCoverageResponse)

The response message for [TestCases.CalculateCoverage][google.cloud.dialogflow.cx.v3.TestCases.CalculateCoverage].

### [Changelog](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Changelog)

Changelogs represents a change made to a given agent.

### [ChangelogName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ChangelogName)

Resource name for the `Changelog` resource.

### [Changelogs](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Changelogs)

Service for managing [Changelogs][google.cloud.dialogflow.cx.v3.Changelog].

### [Changelogs.ChangelogsBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Changelogs.ChangelogsBase)

Base class for server-side implementations of Changelogs

### [Changelogs.ChangelogsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Changelogs.ChangelogsClient)

Client for Changelogs

### [ChangelogsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ChangelogsClient)

Changelogs client wrapper, for convenient use.

### [ChangelogsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ChangelogsClientBuilder)

Builder class for [ChangelogsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ChangelogsClient) to provide simple configuration of credentials, endpoint etc.

### [ChangelogsClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ChangelogsClientImpl)

Changelogs client wrapper implementation, for convenient use.

### [ChangelogsSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ChangelogsSettings)

Settings for [ChangelogsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ChangelogsClient) instances.

### [CloudConversationDebuggingInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.CloudConversationDebuggingInfo)

Cloud conversation info for easier debugging. It will get populated in `StreamingDetectIntentResponse` or `StreamingAnalyzeContentResponse` when the flag `enable_debugging_info` is set to true in corresponding requests.

### [CodeBlock](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.CodeBlock)

Represents a code block.

### [CompareVersionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.CompareVersionsRequest)

The request message for [Versions.CompareVersions][google.cloud.dialogflow.cx.v3.Versions.CompareVersions].

### [CompareVersionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.CompareVersionsResponse)

The response message for [Versions.CompareVersions][google.cloud.dialogflow.cx.v3.Versions.CompareVersions].

### [ContinuousTestResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ContinuousTestResult)

Represents a result from running a test case in an agent environment.

### [ContinuousTestResult.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ContinuousTestResult.Types)

Container for nested types declared in the ContinuousTestResult message type.

### [ContinuousTestResultName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ContinuousTestResultName)

Resource name for the `ContinuousTestResult` resource.

### [ConversationTurn](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ConversationTurn)

One interaction between a human and virtual agent. The human provides some input and the virtual agent provides a response.

### [ConversationTurn.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ConversationTurn.Types)

Container for nested types declared in the ConversationTurn message type.

### [ConversationTurn.Types.UserInput](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ConversationTurn.Types.UserInput)

The input from the human user.

### [ConversationTurn.Types.VirtualAgentOutput](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ConversationTurn.Types.VirtualAgentOutput)

The output from the virtual agent.

### [CreateAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.CreateAgentRequest)

The request message for [Agents.CreateAgent][google.cloud.dialogflow.cx.v3.Agents.CreateAgent].

### [CreateEntityTypeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.CreateEntityTypeRequest)

The request message for [EntityTypes.CreateEntityType][google.cloud.dialogflow.cx.v3.EntityTypes.CreateEntityType].

### [CreateEnvironmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.CreateEnvironmentRequest)

The request message for [Environments.CreateEnvironment][google.cloud.dialogflow.cx.v3.Environments.CreateEnvironment].

### [CreateExampleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.CreateExampleRequest)

The request message for [Examples.CreateExample][google.cloud.dialogflow.cx.v3.Examples.CreateExample].

### [CreateExperimentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.CreateExperimentRequest)

The request message for [Experiments.CreateExperiment][google.cloud.dialogflow.cx.v3.Experiments.CreateExperiment].

### [CreateFlowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.CreateFlowRequest)

The request message for [Flows.CreateFlow][google.cloud.dialogflow.cx.v3.Flows.CreateFlow].

### [CreateGeneratorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.CreateGeneratorRequest)

The request message for [Generators.CreateGenerator][google.cloud.dialogflow.cx.v3.Generators.CreateGenerator].

### [CreateIntentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.CreateIntentRequest)

The request message for [Intents.CreateIntent][google.cloud.dialogflow.cx.v3.Intents.CreateIntent].

### [CreatePageRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.CreatePageRequest)

The request message for [Pages.CreatePage][google.cloud.dialogflow.cx.v3.Pages.CreatePage].

### [CreatePlaybookRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.CreatePlaybookRequest)

The request message for [Playbooks.CreatePlaybook][google.cloud.dialogflow.cx.v3.Playbooks.CreatePlaybook].

### [CreatePlaybookVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.CreatePlaybookVersionRequest)

The request message for [Playbooks.CreatePlaybookVersion][google.cloud.dialogflow.cx.v3.Playbooks.CreatePlaybookVersion].

### [CreateSecuritySettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.CreateSecuritySettingsRequest)

The request message for [SecuritySettings.CreateSecuritySettings][].

### [CreateSessionEntityTypeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.CreateSessionEntityTypeRequest)

The request message for [SessionEntityTypes.CreateSessionEntityType][google.cloud.dialogflow.cx.v3.SessionEntityTypes.CreateSessionEntityType].

### [CreateTestCaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.CreateTestCaseRequest)

The request message for [TestCases.CreateTestCase][google.cloud.dialogflow.cx.v3.TestCases.CreateTestCase].

### [CreateToolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.CreateToolRequest)

The request message for [Tools.CreateTool][google.cloud.dialogflow.cx.v3.Tools.CreateTool].

### [CreateToolVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.CreateToolVersionRequest)

The request message for [Tools.CreateToolVersion][google.cloud.dialogflow.cx.v3.Tools.CreateToolVersion]. The request message for [Tools.CreateToolVersion][google.cloud.dialogflow.cx.v3.Tools.CreateToolVersion].

### [CreateTransitionRouteGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.CreateTransitionRouteGroupRequest)

The request message for [TransitionRouteGroups.CreateTransitionRouteGroup][google.cloud.dialogflow.cx.v3.TransitionRouteGroups.CreateTransitionRouteGroup].

### [CreateVersionOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.CreateVersionOperationMetadata)

Metadata associated with the long running operation for [Versions.CreateVersion][google.cloud.dialogflow.cx.v3.Versions.CreateVersion].

### [CreateVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.CreateVersionRequest)

The request message for [Versions.CreateVersion][google.cloud.dialogflow.cx.v3.Versions.CreateVersion].

### [CreateWebhookRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.CreateWebhookRequest)

The request message for [Webhooks.CreateWebhook][google.cloud.dialogflow.cx.v3.Webhooks.CreateWebhook].

### [DataStoreConnection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DataStoreConnection)

A data store connection. It represents a data store in Discovery Engine and the type of the contents it contains.

### [DataStoreConnectionSignals](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DataStoreConnectionSignals)

Data store connection feature output signals. Might be only partially field if processing stop before the final answer. Reasons for this can be, but are not limited to: empty UCS search results, positive RAI check outcome, grounding failure, ...

### [DataStoreConnectionSignals.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DataStoreConnectionSignals.Types)

Container for nested types declared in the DataStoreConnectionSignals message type.

### [DataStoreConnectionSignals.Types.AnswerGenerationModelCallSignals](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DataStoreConnectionSignals.Types.AnswerGenerationModelCallSignals)

Diagnostic info related to the answer generation model call.

### [DataStoreConnectionSignals.Types.AnswerPart](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DataStoreConnectionSignals.Types.AnswerPart)

Answer part with citation.

### [DataStoreConnectionSignals.Types.CitedSnippet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DataStoreConnectionSignals.Types.CitedSnippet)

Snippet cited by the answer generation model.

### [DataStoreConnectionSignals.Types.GroundingSignals](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DataStoreConnectionSignals.Types.GroundingSignals)

Grounding signals.

### [DataStoreConnectionSignals.Types.GroundingSignals.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DataStoreConnectionSignals.Types.GroundingSignals.Types)

Container for nested types declared in the GroundingSignals message type.

### [DataStoreConnectionSignals.Types.RewriterModelCallSignals](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DataStoreConnectionSignals.Types.RewriterModelCallSignals)

Diagnostic info related to the rewriter model call.

### [DataStoreConnectionSignals.Types.SafetySignals](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DataStoreConnectionSignals.Types.SafetySignals)

Safety check results.

### [DataStoreConnectionSignals.Types.SafetySignals.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DataStoreConnectionSignals.Types.SafetySignals.Types)

Container for nested types declared in the SafetySignals message type.

### [DataStoreConnectionSignals.Types.SearchSnippet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DataStoreConnectionSignals.Types.SearchSnippet)

Search snippet details.

### [DataStoreName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DataStoreName)

Resource name for the `DataStore` resource.

### [DeidentifyTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DeidentifyTemplateName)

Resource name for the `DeidentifyTemplate` resource.

### [DeleteAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DeleteAgentRequest)

The request message for [Agents.DeleteAgent][google.cloud.dialogflow.cx.v3.Agents.DeleteAgent].

### [DeleteEntityTypeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DeleteEntityTypeRequest)

The request message for [EntityTypes.DeleteEntityType][google.cloud.dialogflow.cx.v3.EntityTypes.DeleteEntityType].

### [DeleteEnvironmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DeleteEnvironmentRequest)

The request message for [Environments.DeleteEnvironment][google.cloud.dialogflow.cx.v3.Environments.DeleteEnvironment].

### [DeleteExampleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DeleteExampleRequest)

The request message for [Examples.DeleteExample][google.cloud.dialogflow.cx.v3.Examples.DeleteExample].

### [DeleteExperimentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DeleteExperimentRequest)

The request message for [Experiments.DeleteExperiment][google.cloud.dialogflow.cx.v3.Experiments.DeleteExperiment].

### [DeleteFlowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DeleteFlowRequest)

The request message for [Flows.DeleteFlow][google.cloud.dialogflow.cx.v3.Flows.DeleteFlow].

### [DeleteGeneratorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DeleteGeneratorRequest)

The request message for [Generators.DeleteGenerator][google.cloud.dialogflow.cx.v3.Generators.DeleteGenerator].

### [DeleteIntentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DeleteIntentRequest)

The request message for [Intents.DeleteIntent][google.cloud.dialogflow.cx.v3.Intents.DeleteIntent].

### [DeletePageRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DeletePageRequest)

The request message for [Pages.DeletePage][google.cloud.dialogflow.cx.v3.Pages.DeletePage].

### [DeletePlaybookRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DeletePlaybookRequest)

The request message for [Playbooks.DeletePlaybook][google.cloud.dialogflow.cx.v3.Playbooks.DeletePlaybook].

### [DeletePlaybookVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DeletePlaybookVersionRequest)

The request message for [Playbooks.DeletePlaybookVersion][google.cloud.dialogflow.cx.v3.Playbooks.DeletePlaybookVersion].

### [DeleteSecuritySettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DeleteSecuritySettingsRequest)

The request message for [SecuritySettings.DeleteSecuritySettings][].

### [DeleteSessionEntityTypeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DeleteSessionEntityTypeRequest)

The request message for [SessionEntityTypes.DeleteSessionEntityType][google.cloud.dialogflow.cx.v3.SessionEntityTypes.DeleteSessionEntityType].

### [DeleteToolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DeleteToolRequest)

The request message for [Tools.DeleteTool][google.cloud.dialogflow.cx.v3.Tools.DeleteTool].

### [DeleteToolVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DeleteToolVersionRequest)

The request message for [Tools.DeleteToolVersion][google.cloud.dialogflow.cx.v3.Tools.DeleteToolVersion].

### [DeleteTransitionRouteGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DeleteTransitionRouteGroupRequest)

The request message for [TransitionRouteGroups.DeleteTransitionRouteGroup][google.cloud.dialogflow.cx.v3.TransitionRouteGroups.DeleteTransitionRouteGroup].

### [DeleteVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DeleteVersionRequest)

The request message for [Versions.DeleteVersion][google.cloud.dialogflow.cx.v3.Versions.DeleteVersion].

### [DeleteWebhookRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DeleteWebhookRequest)

The request message for [Webhooks.DeleteWebhook][google.cloud.dialogflow.cx.v3.Webhooks.DeleteWebhook].

### [DeployFlowMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DeployFlowMetadata)

Metadata returned for the [Environments.DeployFlow][google.cloud.dialogflow.cx.v3.Environments.DeployFlow] long running operation.

### [DeployFlowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DeployFlowRequest)

The request message for [Environments.DeployFlow][google.cloud.dialogflow.cx.v3.Environments.DeployFlow].

### [DeployFlowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DeployFlowResponse)

The response message for [Environments.DeployFlow][google.cloud.dialogflow.cx.v3.Environments.DeployFlow].

### [Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Deployment)

Represents a deployment in an environment. A deployment happens when a flow version configured to be active in the environment. You can configure running pre-deployment steps, e.g. running validation test cases, experiment auto-rollout, etc.

### [Deployment.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Deployment.Types)

Container for nested types declared in the Deployment message type.

### [Deployment.Types.Result](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Deployment.Types.Result)

Result of the deployment.

### [DeploymentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DeploymentName)

Resource name for the `Deployment` resource.

### [Deployments](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Deployments)

Service for managing [Deployments][google.cloud.dialogflow.cx.v3.Deployment].

### [Deployments.DeploymentsBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Deployments.DeploymentsBase)

Base class for server-side implementations of Deployments

### [Deployments.DeploymentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Deployments.DeploymentsClient)

Client for Deployments

### [DeploymentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DeploymentsClient)

Deployments client wrapper, for convenient use.

### [DeploymentsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DeploymentsClientBuilder)

Builder class for [DeploymentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DeploymentsClient) to provide simple configuration of credentials, endpoint etc.

### [DeploymentsClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DeploymentsClientImpl)

Deployments client wrapper implementation, for convenient use.

### [DeploymentsSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DeploymentsSettings)

Settings for [DeploymentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DeploymentsClient) instances.

### [DetectIntentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DetectIntentRequest)

The request to detect user's intent.

### [DetectIntentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DetectIntentResponse)

The message returned from the DetectIntent method.

### [DetectIntentResponse.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DetectIntentResponse.Types)

Container for nested types declared in the DetectIntentResponse message type.

### [DtmfInput](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DtmfInput)

Represents the input for dtmf event.

### [EntityType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityType)

Entities are extracted from user input and represent parameters that are meaningful to your application. For example, a date range, a proper name such as a geographic location or landmark, and so on. Entities represent actionable data for your application.

When you define an entity, you can also include synonyms that all map to that entity. For example, "soft drink", "soda", "pop", and so on.

There are three types of entities:

  * **System** \- entities that are defined by the Dialogflow API for common data types such as date, time, currency, and so on. A system entity is represented by the `EntityType` type.

  * **Custom** \- entities that are defined by you that represent actionable data that is meaningful to your application. For example, you could define a `pizza.sauce` entity for red or white pizza sauce, a `pizza.cheese` entity for the different types of cheese on a pizza, a `pizza.topping` entity for different toppings, and so on. A custom entity is represented by the `EntityType` type.

  * **User** \- entities that are built for an individual user such as favorites, preferences, playlists, and so on. A user entity is represented by the [SessionEntityType][google.cloud.dialogflow.cx.v3.SessionEntityType] type.




For more information about entity types, see the [Dialogflow documentation](https://cloud.google.com/dialogflow/docs/entities-overview).

### [EntityType.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityType.Types)

Container for nested types declared in the EntityType message type.

### [EntityType.Types.Entity](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityType.Types.Entity)

An **entity entry** for an associated entity type.

### [EntityType.Types.ExcludedPhrase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityType.Types.ExcludedPhrase)

An excluded entity phrase that should not be matched.

### [EntityTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityTypeName)

Resource name for the `EntityType` resource.

### [EntityTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityTypes)

Service for managing [EntityTypes][google.cloud.dialogflow.cx.v3.EntityType].

### [EntityTypes.EntityTypesBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityTypes.EntityTypesBase)

Base class for server-side implementations of EntityTypes

### [EntityTypes.EntityTypesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityTypes.EntityTypesClient)

Client for EntityTypes

### [EntityTypesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityTypesClient)

EntityTypes client wrapper, for convenient use.

### [EntityTypesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityTypesClientBuilder)

Builder class for [EntityTypesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityTypesClient) to provide simple configuration of credentials, endpoint etc.

### [EntityTypesClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityTypesClientImpl)

EntityTypes client wrapper implementation, for convenient use.

### [EntityTypesSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityTypesSettings)

Settings for [EntityTypesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityTypesClient) instances.

### [Environment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Environment)

Represents an environment for an agent. You can create multiple versions of your agent and publish them to separate environments. When you edit an agent, you are editing the draft agent. At any point, you can save the draft agent as an agent version, which is an immutable snapshot of your agent. When you save the draft agent, it is published to the default environment. When you create agent versions, you can publish them to custom environments. You can create a variety of custom environments for testing, development, production, etc.

### [Environment.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Environment.Types)

Container for nested types declared in the Environment message type.

### [Environment.Types.TestCasesConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Environment.Types.TestCasesConfig)

The configuration for continuous tests.

### [Environment.Types.VersionConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Environment.Types.VersionConfig)

Configuration for the version.

### [Environment.Types.WebhookConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Environment.Types.WebhookConfig)

Configuration for webhooks.

### [EnvironmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EnvironmentName)

Resource name for the `Environment` resource.

### [Environments](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Environments)

Service for managing [Environments][google.cloud.dialogflow.cx.v3.Environment].

### [Environments.EnvironmentsBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Environments.EnvironmentsBase)

Base class for server-side implementations of Environments

### [Environments.EnvironmentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Environments.EnvironmentsClient)

Client for Environments

### [EnvironmentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EnvironmentsClient)

Environments client wrapper, for convenient use.

### [EnvironmentsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EnvironmentsClientBuilder)

Builder class for [EnvironmentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EnvironmentsClient) to provide simple configuration of credentials, endpoint etc.

### [EnvironmentsClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EnvironmentsClientImpl)

Environments client wrapper implementation, for convenient use.

### [EnvironmentsSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EnvironmentsSettings)

Settings for [EnvironmentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EnvironmentsClient) instances.

### [EventHandler](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EventHandler)

An event handler specifies an [event][google.cloud.dialogflow.cx.v3.EventHandler.event] that can be handled during a session. When the specified event happens, the following actions are taken in order:

  * If there is a [`trigger_fulfillment`][google.cloud.dialogflow.cx.v3.EventHandler.trigger_fulfillment] associated with the event, it will be called.
  * If there is a [`target_page`][google.cloud.dialogflow.cx.v3.EventHandler.target_page] associated with the event, the session will transition into the specified page.
  * If there is a [`target_flow`][google.cloud.dialogflow.cx.v3.EventHandler.target_flow] associated with the event, the session will transition into the specified flow.



### [EventInput](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EventInput)

Represents the event to trigger.

### [Example](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Example)

Example represents a sample execution of the playbook in the conversation.

An example consists of a list of ordered actions performed by end user or Dialogflow agent according the playbook instructions to fulfill the task.

### [ExampleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExampleName)

Resource name for the `Example` resource.

### [Examples](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Examples)

Service for managing [Examples][google.cloud.dialogflow.cx.v3.Example].

### [Examples.ExamplesBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Examples.ExamplesBase)

Base class for server-side implementations of Examples

### [Examples.ExamplesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Examples.ExamplesClient)

Client for Examples

### [ExamplesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExamplesClient)

Examples client wrapper, for convenient use.

### [ExamplesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExamplesClientBuilder)

Builder class for [ExamplesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExamplesClient) to provide simple configuration of credentials, endpoint etc.

### [ExamplesClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExamplesClientImpl)

Examples client wrapper implementation, for convenient use.

### [ExamplesSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExamplesSettings)

Settings for [ExamplesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExamplesClient) instances.

### [Experiment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Experiment)

Represents an experiment in an environment.

### [Experiment.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Experiment.Types)

Container for nested types declared in the Experiment message type.

### [Experiment.Types.Definition](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Experiment.Types.Definition)

Definition of the experiment.

### [Experiment.Types.Result](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Experiment.Types.Result)

The inference result which includes an objective metric to optimize and the confidence interval.

### [Experiment.Types.Result.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Experiment.Types.Result.Types)

Container for nested types declared in the Result message type.

### [Experiment.Types.Result.Types.ConfidenceInterval](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Experiment.Types.Result.Types.ConfidenceInterval)

A confidence interval is a range of possible values for the experiment objective you are trying to measure.

### [Experiment.Types.Result.Types.Metric](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Experiment.Types.Result.Types.Metric)

Metric and corresponding confidence intervals.

### [Experiment.Types.Result.Types.VersionMetrics](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Experiment.Types.Result.Types.VersionMetrics)

Version variant and associated metrics.

### [ExperimentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExperimentName)

Resource name for the `Experiment` resource.

### [Experiments](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Experiments)

Service for managing [Experiments][google.cloud.dialogflow.cx.v3.Experiment].

### [Experiments.ExperimentsBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Experiments.ExperimentsBase)

Base class for server-side implementations of Experiments

### [Experiments.ExperimentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Experiments.ExperimentsClient)

Client for Experiments

### [ExperimentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExperimentsClient)

Experiments client wrapper, for convenient use.

### [ExperimentsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExperimentsClientBuilder)

Builder class for [ExperimentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExperimentsClient) to provide simple configuration of credentials, endpoint etc.

### [ExperimentsClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExperimentsClientImpl)

Experiments client wrapper implementation, for convenient use.

### [ExperimentsSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExperimentsSettings)

Settings for [ExperimentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExperimentsClient) instances.

### [ExportAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportAgentRequest)

The request message for [Agents.ExportAgent][google.cloud.dialogflow.cx.v3.Agents.ExportAgent].

### [ExportAgentRequest.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportAgentRequest.Types)

Container for nested types declared in the ExportAgentRequest message type.

### [ExportAgentRequest.Types.GitDestination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportAgentRequest.Types.GitDestination)

Settings for exporting to a git branch.

### [ExportAgentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportAgentResponse)

The response message for [Agents.ExportAgent][google.cloud.dialogflow.cx.v3.Agents.ExportAgent].

### [ExportEntityTypesMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportEntityTypesMetadata)

Metadata returned for the [EntityTypes.ExportEntityTypes][google.cloud.dialogflow.cx.v3.EntityTypes.ExportEntityTypes] long running operation.

### [ExportEntityTypesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportEntityTypesRequest)

The request message for [EntityTypes.ExportEntityTypes][google.cloud.dialogflow.cx.v3.EntityTypes.ExportEntityTypes].

### [ExportEntityTypesRequest.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportEntityTypesRequest.Types)

Container for nested types declared in the ExportEntityTypesRequest message type.

### [ExportEntityTypesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportEntityTypesResponse)

The response message for [EntityTypes.ExportEntityTypes][google.cloud.dialogflow.cx.v3.EntityTypes.ExportEntityTypes].

### [ExportFlowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportFlowRequest)

The request message for [Flows.ExportFlow][google.cloud.dialogflow.cx.v3.Flows.ExportFlow].

### [ExportFlowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportFlowResponse)

The response message for [Flows.ExportFlow][google.cloud.dialogflow.cx.v3.Flows.ExportFlow].

### [ExportIntentsMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportIntentsMetadata)

Metadata returned for the [Intents.ExportIntents][google.cloud.dialogflow.cx.v3.Intents.ExportIntents] long running operation.

### [ExportIntentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportIntentsRequest)

The request message for [Intents.ExportIntents][google.cloud.dialogflow.cx.v3.Intents.ExportIntents].

### [ExportIntentsRequest.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportIntentsRequest.Types)

Container for nested types declared in the ExportIntentsRequest message type.

### [ExportIntentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportIntentsResponse)

The response message for [Intents.ExportIntents][google.cloud.dialogflow.cx.v3.Intents.ExportIntents].

### [ExportPlaybookRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportPlaybookRequest)

The request message for [Playbooks.ExportPlaybook][google.cloud.dialogflow.cx.v3.Playbooks.ExportPlaybook].

### [ExportPlaybookRequest.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportPlaybookRequest.Types)

Container for nested types declared in the ExportPlaybookRequest message type.

### [ExportPlaybookResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportPlaybookResponse)

The response message for [Playbooks.ExportPlaybook][google.cloud.dialogflow.cx.v3.Playbooks.ExportPlaybook].

### [ExportTestCasesMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportTestCasesMetadata)

Metadata returned for the [TestCases.ExportTestCases][google.cloud.dialogflow.cx.v3.TestCases.ExportTestCases] long running operation. This message currently has no fields.

### [ExportTestCasesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportTestCasesRequest)

The request message for [TestCases.ExportTestCases][google.cloud.dialogflow.cx.v3.TestCases.ExportTestCases].

### [ExportTestCasesRequest.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportTestCasesRequest.Types)

Container for nested types declared in the ExportTestCasesRequest message type.

### [ExportTestCasesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportTestCasesResponse)

The response message for [TestCases.ExportTestCases][google.cloud.dialogflow.cx.v3.TestCases.ExportTestCases].

### [FilterSpecs](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.FilterSpecs)

Filter specifications for data stores.

### [Flow](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Flow)

Flows represents the conversation flows when you build your chatbot agent.

A flow consists of many pages connected by the transition routes. Conversations always start with the built-in Start Flow (with an all-0 ID). Transition routes can direct the conversation session from the current flow (parent flow) to another flow (sub flow). When the sub flow is finished, Dialogflow will bring the session back to the parent flow, where the sub flow is started.

Usually, when a transition route is followed by a matched intent, the intent will be "consumed". This means the intent won't activate more transition routes. However, when the followed transition route moves the conversation session into a different flow, the matched intent can be carried over and to be consumed in the target flow.

### [Flow.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Flow.Types)

Container for nested types declared in the Flow message type.

### [Flow.Types.MultiLanguageSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Flow.Types.MultiLanguageSettings)

Settings for multi-lingual agents.

### [FlowImportStrategy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.FlowImportStrategy)

The flow import strategy used for resource conflict resolution associated with an [ImportFlowRequest][google.cloud.dialogflow.cx.v3.ImportFlowRequest].

### [FlowInvocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.FlowInvocation)

Stores metadata of the invocation of a CX flow.

### [FlowName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.FlowName)

Resource name for the `Flow` resource.

### [FlowTraceMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.FlowTraceMetadata)

Metadata of the flow trace.

### [FlowTransition](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.FlowTransition)

Stores metadata of the transition to a target CX flow. Flow transition actions exit the caller playbook and enter the child flow.

### [FlowValidationResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.FlowValidationResult)

The response message for [Flows.GetFlowValidationResult][google.cloud.dialogflow.cx.v3.Flows.GetFlowValidationResult].

### [FlowValidationResultName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.FlowValidationResultName)

Resource name for the `FlowValidationResult` resource.

### [Flows](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Flows)

Service for managing [Flows][google.cloud.dialogflow.cx.v3.Flow].

### [Flows.FlowsBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Flows.FlowsBase)

Base class for server-side implementations of Flows

### [Flows.FlowsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Flows.FlowsClient)

Client for Flows

### [FlowsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.FlowsClient)

Flows client wrapper, for convenient use.

### [FlowsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.FlowsClientBuilder)

Builder class for [FlowsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.FlowsClient) to provide simple configuration of credentials, endpoint etc.

### [FlowsClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.FlowsClientImpl)

Flows client wrapper implementation, for convenient use.

### [FlowsSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.FlowsSettings)

Settings for [FlowsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.FlowsClient) instances.

### [Form](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Form)

A form is a data model that groups related parameters that can be collected from the user. The process in which the agent prompts the user and collects parameter values from the user is called form filling. A form can be added to a [page][google.cloud.dialogflow.cx.v3.Page]. When form filling is done, the filled parameters will be written to the [session][google.cloud.dialogflow.cx.v3.SessionInfo.parameters].

### [Form.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Form.Types)

Container for nested types declared in the Form message type.

### [Form.Types.Parameter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Form.Types.Parameter)

Represents a form parameter.

### [Form.Types.Parameter.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Form.Types.Parameter.Types)

Container for nested types declared in the Parameter message type.

### [Form.Types.Parameter.Types.FillBehavior](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Form.Types.Parameter.Types.FillBehavior)

Configuration for how the filling of a parameter should be handled.

### [FulfillIntentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.FulfillIntentRequest)

Request of [FulfillIntent][]

### [FulfillIntentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.FulfillIntentResponse)

Response of [FulfillIntent][]

### [Fulfillment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Fulfillment)

A fulfillment can do one or more of the following actions at the same time:

  * Generate rich message responses.
  * Set parameter values.
  * Call the webhook.



Fulfillments can be called at various stages in the [Page][google.cloud.dialogflow.cx.v3.Page] or [Form][google.cloud.dialogflow.cx.v3.Form] lifecycle. For example, when a [DetectIntentRequest][google.cloud.dialogflow.cx.v3.DetectIntentRequest] drives a session to enter a new page, the page's entry fulfillment can add a static response to the [QueryResult][google.cloud.dialogflow.cx.v3.QueryResult] in the returning [DetectIntentResponse][google.cloud.dialogflow.cx.v3.DetectIntentResponse], call the webhook (for example, to load user data from a database), or both.

### [Fulfillment.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Fulfillment.Types)

Container for nested types declared in the Fulfillment message type.

### [Fulfillment.Types.ConditionalCases](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Fulfillment.Types.ConditionalCases)

A list of cascading if-else conditions. Cases are mutually exclusive. The first one with a matching condition is selected, all the rest ignored.

### [Fulfillment.Types.ConditionalCases.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Fulfillment.Types.ConditionalCases.Types)

Container for nested types declared in the ConditionalCases message type.

### [Fulfillment.Types.ConditionalCases.Types.Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Fulfillment.Types.ConditionalCases.Types.Case)

Each case has a Boolean condition. When it is evaluated to be True, the corresponding messages will be selected and evaluated recursively.

### [Fulfillment.Types.ConditionalCases.Types.Case.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Fulfillment.Types.ConditionalCases.Types.Case.Types)

Container for nested types declared in the Case message type.

### [Fulfillment.Types.ConditionalCases.Types.Case.Types.CaseContent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Fulfillment.Types.ConditionalCases.Types.Case.Types.CaseContent)

The list of messages or conditional cases to activate for this case.

### [Fulfillment.Types.GeneratorSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Fulfillment.Types.GeneratorSettings)

Generator settings used by the LLM to generate a text response.

### [Fulfillment.Types.SetParameterAction](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Fulfillment.Types.SetParameterAction)

Setting a parameter value.

### [GcsDestination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GcsDestination)

Google Cloud Storage location for a Dialogflow operation that writes or exports objects (e.g. exported agent or transcripts) outside of Dialogflow.

### [GenerativeSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GenerativeSettings)

Settings for Generative AI.

### [GenerativeSettings.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GenerativeSettings.Types)

Container for nested types declared in the GenerativeSettings message type.

### [GenerativeSettings.Types.FallbackSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GenerativeSettings.Types.FallbackSettings)

Settings for Generative Fallback.

### [GenerativeSettings.Types.FallbackSettings.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GenerativeSettings.Types.FallbackSettings.Types)

Container for nested types declared in the FallbackSettings message type.

### [GenerativeSettings.Types.FallbackSettings.Types.PromptTemplate](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GenerativeSettings.Types.FallbackSettings.Types.PromptTemplate)

Prompt template.

### [GenerativeSettings.Types.KnowledgeConnectorSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GenerativeSettings.Types.KnowledgeConnectorSettings)

Settings for knowledge connector. These parameters are used for LLM prompt like "You are <agent>. You are a helpful and verbose <agent_identity> at <business>, <business_description>. Your task is to help humans on <agent_scope>".

### [Generator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Generator)

Generators contain prompt to be sent to the LLM model to generate text. The prompt can contain parameters which will be resolved before calling the model. It can optionally contain banned phrases to ensure the model responses are safe.

### [Generator.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Generator.Types)

Container for nested types declared in the Generator message type.

### [Generator.Types.ModelParameter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Generator.Types.ModelParameter)

Parameters to be passed to the LLM. If not set, default values will be used.

### [Generator.Types.Placeholder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Generator.Types.Placeholder)

Represents a custom placeholder in the prompt text.

### [GeneratorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GeneratorName)

Resource name for the `Generator` resource.

### [Generators](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Generators)

Service for managing [Generators][google.cloud.dialogflow.cx.v3.Generator]

### [Generators.GeneratorsBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Generators.GeneratorsBase)

Base class for server-side implementations of Generators

### [Generators.GeneratorsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Generators.GeneratorsClient)

Client for Generators

### [GeneratorsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GeneratorsClient)

Generators client wrapper, for convenient use.

### [GeneratorsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GeneratorsClientBuilder)

Builder class for [GeneratorsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GeneratorsClient) to provide simple configuration of credentials, endpoint etc.

### [GeneratorsClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GeneratorsClientImpl)

Generators client wrapper implementation, for convenient use.

### [GeneratorsSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GeneratorsSettings)

Settings for [GeneratorsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GeneratorsClient) instances.

### [GetAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GetAgentRequest)

The request message for [Agents.GetAgent][google.cloud.dialogflow.cx.v3.Agents.GetAgent].

### [GetAgentValidationResultRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GetAgentValidationResultRequest)

The request message for [Agents.GetAgentValidationResult][google.cloud.dialogflow.cx.v3.Agents.GetAgentValidationResult].

### [GetChangelogRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GetChangelogRequest)

The request message for [Changelogs.GetChangelog][google.cloud.dialogflow.cx.v3.Changelogs.GetChangelog].

### [GetDeploymentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GetDeploymentRequest)

The request message for [Deployments.GetDeployment][google.cloud.dialogflow.cx.v3.Deployments.GetDeployment].

### [GetEntityTypeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GetEntityTypeRequest)

The request message for [EntityTypes.GetEntityType][google.cloud.dialogflow.cx.v3.EntityTypes.GetEntityType].

### [GetEnvironmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GetEnvironmentRequest)

The request message for [Environments.GetEnvironment][google.cloud.dialogflow.cx.v3.Environments.GetEnvironment].

### [GetExampleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GetExampleRequest)

The request message for [Examples.GetExample][google.cloud.dialogflow.cx.v3.Examples.GetExample].

### [GetExperimentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GetExperimentRequest)

The request message for [Experiments.GetExperiment][google.cloud.dialogflow.cx.v3.Experiments.GetExperiment].

### [GetFlowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GetFlowRequest)

The response message for [Flows.GetFlow][google.cloud.dialogflow.cx.v3.Flows.GetFlow].

### [GetFlowValidationResultRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GetFlowValidationResultRequest)

The request message for [Flows.GetFlowValidationResult][google.cloud.dialogflow.cx.v3.Flows.GetFlowValidationResult].

### [GetGenerativeSettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GetGenerativeSettingsRequest)

Request for [GetGenerativeSettings][google.cloud.dialogflow.cx.v3.Agents.GetGenerativeSettings] RPC.

### [GetGeneratorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GetGeneratorRequest)

The request message for [Generators.GetGenerator][google.cloud.dialogflow.cx.v3.Generators.GetGenerator].

### [GetIntentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GetIntentRequest)

The request message for [Intents.GetIntent][google.cloud.dialogflow.cx.v3.Intents.GetIntent].

### [GetPageRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GetPageRequest)

The request message for [Pages.GetPage][google.cloud.dialogflow.cx.v3.Pages.GetPage].

### [GetPlaybookRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GetPlaybookRequest)

The request message for [Playbooks.GetPlaybook][google.cloud.dialogflow.cx.v3.Playbooks.GetPlaybook].

### [GetPlaybookVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GetPlaybookVersionRequest)

The request message for [Playbooks.GetPlaybookVersion][google.cloud.dialogflow.cx.v3.Playbooks.GetPlaybookVersion].

### [GetSecuritySettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GetSecuritySettingsRequest)

The request message for [SecuritySettingsService.GetSecuritySettings][google.cloud.dialogflow.cx.v3.SecuritySettingsService.GetSecuritySettings].

### [GetSessionEntityTypeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GetSessionEntityTypeRequest)

The request message for [SessionEntityTypes.GetSessionEntityType][google.cloud.dialogflow.cx.v3.SessionEntityTypes.GetSessionEntityType].

### [GetTestCaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GetTestCaseRequest)

The request message for [TestCases.GetTestCase][google.cloud.dialogflow.cx.v3.TestCases.GetTestCase].

### [GetTestCaseResultRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GetTestCaseResultRequest)

The request message for [TestCases.GetTestCaseResult][google.cloud.dialogflow.cx.v3.TestCases.GetTestCaseResult].

### [GetToolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GetToolRequest)

The request message for [Tools.GetTool][google.cloud.dialogflow.cx.v3.Tools.GetTool].

### [GetToolVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GetToolVersionRequest)

The request message for [Tools.GetToolVersion][google.cloud.dialogflow.cx.v3.Tools.GetToolVersion].

### [GetTransitionRouteGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GetTransitionRouteGroupRequest)

The request message for [TransitionRouteGroups.GetTransitionRouteGroup][google.cloud.dialogflow.cx.v3.TransitionRouteGroups.GetTransitionRouteGroup].

### [GetVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GetVersionRequest)

The request message for [Versions.GetVersion][google.cloud.dialogflow.cx.v3.Versions.GetVersion].

### [GetWebhookRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GetWebhookRequest)

The request message for [Webhooks.GetWebhook][google.cloud.dialogflow.cx.v3.Webhooks.GetWebhook].

### [Handler](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Handler)

Handler can be used to define custom logic to be executed based on the user-specified triggers.

### [Handler.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Handler.Types)

Container for nested types declared in the Handler message type.

### [Handler.Types.EventHandler](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Handler.Types.EventHandler)

A handler that is triggered by the specified [event][google.cloud.dialogflow.cx.v3.Handler.EventHandler.event].

### [Handler.Types.LifecycleHandler](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Handler.Types.LifecycleHandler)

A handler that is triggered on the specific [lifecycle_stage][google.cloud.dialogflow.cx.v3.Handler.LifecycleHandler.lifecycle_stage] of the playbook execution.

### [ImportEntityTypesMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ImportEntityTypesMetadata)

Metadata returned for the [EntityTypes.ImportEntityTypes][google.cloud.dialogflow.cx.v3.EntityTypes.ImportEntityTypes] long running operation.

### [ImportEntityTypesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ImportEntityTypesRequest)

The request message for [EntityTypes.ImportEntityTypes][google.cloud.dialogflow.cx.v3.EntityTypes.ImportEntityTypes].

### [ImportEntityTypesRequest.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ImportEntityTypesRequest.Types)

Container for nested types declared in the ImportEntityTypesRequest message type.

### [ImportEntityTypesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ImportEntityTypesResponse)

The response message for [EntityTypes.ImportEntityTypes][google.cloud.dialogflow.cx.v3.EntityTypes.ImportEntityTypes].

### [ImportEntityTypesResponse.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ImportEntityTypesResponse.Types)

Container for nested types declared in the ImportEntityTypesResponse message type.

### [ImportEntityTypesResponse.Types.ConflictingResources](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ImportEntityTypesResponse.Types.ConflictingResources)

Conflicting resources detected during the import process. Only filled when [REPORT_CONFLICT][ImportEntityTypesResponse.REPORT_CONFLICT] is set in the request and there are conflicts in the display names.

### [ImportFlowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ImportFlowRequest)

The request message for [Flows.ImportFlow][google.cloud.dialogflow.cx.v3.Flows.ImportFlow].

### [ImportFlowRequest.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ImportFlowRequest.Types)

Container for nested types declared in the ImportFlowRequest message type.

### [ImportFlowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ImportFlowResponse)

The response message for [Flows.ImportFlow][google.cloud.dialogflow.cx.v3.Flows.ImportFlow].

### [ImportIntentsMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ImportIntentsMetadata)

Metadata returned for the [Intents.ImportIntents][google.cloud.dialogflow.cx.v3.Intents.ImportIntents] long running operation.

### [ImportIntentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ImportIntentsRequest)

The request message for [Intents.ImportIntents][google.cloud.dialogflow.cx.v3.Intents.ImportIntents].

### [ImportIntentsRequest.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ImportIntentsRequest.Types)

Container for nested types declared in the ImportIntentsRequest message type.

### [ImportIntentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ImportIntentsResponse)

The response message for [Intents.ImportIntents][google.cloud.dialogflow.cx.v3.Intents.ImportIntents].

### [ImportIntentsResponse.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ImportIntentsResponse.Types)

Container for nested types declared in the ImportIntentsResponse message type.

### [ImportIntentsResponse.Types.ConflictingResources](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ImportIntentsResponse.Types.ConflictingResources)

Conflicting resources detected during the import process. Only filled when [REPORT_CONFLICT][ImportIntentsResponse.REPORT_CONFLICT] is set in the request and there are conflicts in the display names.

### [ImportPlaybookRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ImportPlaybookRequest)

The request message for [Playbooks.ImportPlaybook][google.cloud.dialogflow.cx.v3.Playbooks.ImportPlaybook].

### [ImportPlaybookResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ImportPlaybookResponse)

The response message for [Playbooks.ImportPlaybook][google.cloud.dialogflow.cx.v3.Playbooks.ImportPlaybook].

### [ImportPlaybookResponse.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ImportPlaybookResponse.Types)

Container for nested types declared in the ImportPlaybookResponse message type.

### [ImportPlaybookResponse.Types.ConflictingResources](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ImportPlaybookResponse.Types.ConflictingResources)

Conflicting resources detected during the import process. Only filled when [REPORT_CONFLICTS][ImportPlaybookResponse.REPORT_CONFLICTS] is set in the request and there are conflicts in the display names.

### [ImportTestCasesMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ImportTestCasesMetadata)

Metadata returned for the [TestCases.ImportTestCases][google.cloud.dialogflow.cx.v3.TestCases.ImportTestCases] long running operation.

### [ImportTestCasesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ImportTestCasesRequest)

The request message for [TestCases.ImportTestCases][google.cloud.dialogflow.cx.v3.TestCases.ImportTestCases].

### [ImportTestCasesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ImportTestCasesResponse)

The response message for [TestCases.ImportTestCases][google.cloud.dialogflow.cx.v3.TestCases.ImportTestCases].

### [InlineDestination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.InlineDestination)

Inline destination for a Dialogflow operation that writes or exports objects (e.g. [intents][google.cloud.dialogflow.cx.v3.Intent]) outside of Dialogflow.

### [InlineSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.InlineSchema)

A type schema object that's specified inline.

### [InlineSource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.InlineSource)

Inline source for a Dialogflow operation that reads or imports objects (e.g. [intents][google.cloud.dialogflow.cx.v3.Intent]) into Dialogflow.

### [InputAudioConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.InputAudioConfig)

Instructs the speech recognizer on how to process the audio content.

### [InspectTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.InspectTemplateName)

Resource name for the `InspectTemplate` resource.

### [Intent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Intent)

An intent represents a user's intent to interact with a conversational agent.

You can provide information for the Dialogflow API to use to match user input to an intent by adding training phrases (i.e., examples of user input) to your intent.

### [Intent.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Intent.Types)

Container for nested types declared in the Intent message type.

### [Intent.Types.Parameter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Intent.Types.Parameter)

Represents an intent parameter.

### [Intent.Types.TrainingPhrase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Intent.Types.TrainingPhrase)

Represents an example that the agent is trained on to identify the intent.

### [Intent.Types.TrainingPhrase.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Intent.Types.TrainingPhrase.Types)

Container for nested types declared in the TrainingPhrase message type.

### [Intent.Types.TrainingPhrase.Types.Part](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Intent.Types.TrainingPhrase.Types.Part)

Represents a part of a training phrase.

### [IntentCoverage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.IntentCoverage)

Intent coverage represents the percentage of all possible intents in the agent that are triggered in any of a parent's test cases.

### [IntentCoverage.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.IntentCoverage.Types)

Container for nested types declared in the IntentCoverage message type.

### [IntentCoverage.Types.Intent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.IntentCoverage.Types.Intent)

The agent's intent.

### [IntentInput](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.IntentInput)

Represents the intent to trigger programmatically rather than as a result of natural language processing.

### [IntentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.IntentName)

Resource name for the `Intent` resource.

### [Intents](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Intents)

Service for managing [Intents][google.cloud.dialogflow.cx.v3.Intent].

### [Intents.IntentsBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Intents.IntentsBase)

Base class for server-side implementations of Intents

### [Intents.IntentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Intents.IntentsClient)

Client for Intents

### [IntentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.IntentsClient)

Intents client wrapper, for convenient use.

### [IntentsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.IntentsClientBuilder)

Builder class for [IntentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.IntentsClient) to provide simple configuration of credentials, endpoint etc.

### [IntentsClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.IntentsClientImpl)

Intents client wrapper implementation, for convenient use.

### [IntentsSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.IntentsSettings)

Settings for [IntentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.IntentsClient) instances.

### [KnowledgeConnectorSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.KnowledgeConnectorSettings)

The Knowledge Connector settings for this page or flow. This includes information such as the attached Knowledge Bases, and the way to execute fulfillment.

### [LanguageInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.LanguageInfo)

Represents the language information of the request.

### [ListAgentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListAgentsRequest)

The request message for [Agents.ListAgents][google.cloud.dialogflow.cx.v3.Agents.ListAgents].

### [ListAgentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListAgentsResponse)

The response message for [Agents.ListAgents][google.cloud.dialogflow.cx.v3.Agents.ListAgents].

### [ListChangelogsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListChangelogsRequest)

The request message for [Changelogs.ListChangelogs][google.cloud.dialogflow.cx.v3.Changelogs.ListChangelogs].

### [ListChangelogsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListChangelogsResponse)

The response message for [Changelogs.ListChangelogs][google.cloud.dialogflow.cx.v3.Changelogs.ListChangelogs].

### [ListContinuousTestResultsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListContinuousTestResultsRequest)

The request message for [Environments.ListContinuousTestResults][google.cloud.dialogflow.cx.v3.Environments.ListContinuousTestResults].

### [ListContinuousTestResultsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListContinuousTestResultsResponse)

The response message for [Environments.ListTestCaseResults][].

### [ListDeploymentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListDeploymentsRequest)

The request message for [Deployments.ListDeployments][google.cloud.dialogflow.cx.v3.Deployments.ListDeployments].

### [ListDeploymentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListDeploymentsResponse)

The response message for [Deployments.ListDeployments][google.cloud.dialogflow.cx.v3.Deployments.ListDeployments].

### [ListEntityTypesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListEntityTypesRequest)

The request message for [EntityTypes.ListEntityTypes][google.cloud.dialogflow.cx.v3.EntityTypes.ListEntityTypes].

### [ListEntityTypesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListEntityTypesResponse)

The response message for [EntityTypes.ListEntityTypes][google.cloud.dialogflow.cx.v3.EntityTypes.ListEntityTypes].

### [ListEnvironmentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListEnvironmentsRequest)

The request message for [Environments.ListEnvironments][google.cloud.dialogflow.cx.v3.Environments.ListEnvironments].

### [ListEnvironmentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListEnvironmentsResponse)

The response message for [Environments.ListEnvironments][google.cloud.dialogflow.cx.v3.Environments.ListEnvironments].

### [ListExamplesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListExamplesRequest)

The request message for [Examples.ListExamples][google.cloud.dialogflow.cx.v3.Examples.ListExamples].

### [ListExamplesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListExamplesResponse)

The response message for [Examples.ListExamples][google.cloud.dialogflow.cx.v3.Examples.ListExamples].

### [ListExperimentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListExperimentsRequest)

The request message for [Experiments.ListExperiments][google.cloud.dialogflow.cx.v3.Experiments.ListExperiments].

### [ListExperimentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListExperimentsResponse)

The response message for [Experiments.ListExperiments][google.cloud.dialogflow.cx.v3.Experiments.ListExperiments].

### [ListFlowsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListFlowsRequest)

The request message for [Flows.ListFlows][google.cloud.dialogflow.cx.v3.Flows.ListFlows].

### [ListFlowsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListFlowsResponse)

The response message for [Flows.ListFlows][google.cloud.dialogflow.cx.v3.Flows.ListFlows].

### [ListGeneratorsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListGeneratorsRequest)

The request message for [Generators.ListGenerators][google.cloud.dialogflow.cx.v3.Generators.ListGenerators].

### [ListGeneratorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListGeneratorsResponse)

The response message for [Generators.ListGenerators][google.cloud.dialogflow.cx.v3.Generators.ListGenerators].

### [ListIntentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListIntentsRequest)

The request message for [Intents.ListIntents][google.cloud.dialogflow.cx.v3.Intents.ListIntents].

### [ListIntentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListIntentsResponse)

The response message for [Intents.ListIntents][google.cloud.dialogflow.cx.v3.Intents.ListIntents].

### [ListPagesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListPagesRequest)

The request message for [Pages.ListPages][google.cloud.dialogflow.cx.v3.Pages.ListPages].

### [ListPagesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListPagesResponse)

The response message for [Pages.ListPages][google.cloud.dialogflow.cx.v3.Pages.ListPages].

### [ListPlaybookVersionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListPlaybookVersionsRequest)

The request message for [Playbooks.ListPlaybookVersions][google.cloud.dialogflow.cx.v3.Playbooks.ListPlaybookVersions].

### [ListPlaybookVersionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListPlaybookVersionsResponse)

The response message for [Playbooks.ListPlaybookVersions][google.cloud.dialogflow.cx.v3.Playbooks.ListPlaybookVersions].

### [ListPlaybooksRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListPlaybooksRequest)

The request message for [Playbooks.ListPlaybooks][google.cloud.dialogflow.cx.v3.Playbooks.ListPlaybooks].

### [ListPlaybooksResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListPlaybooksResponse)

The response message for [Playbooks.ListPlaybooks][google.cloud.dialogflow.cx.v3.Playbooks.ListPlaybooks].

### [ListSecuritySettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListSecuritySettingsRequest)

The request message for [SecuritySettings.ListSecuritySettings][].

### [ListSecuritySettingsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListSecuritySettingsResponse)

The response message for [SecuritySettings.ListSecuritySettings][].

### [ListSessionEntityTypesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListSessionEntityTypesRequest)

The request message for [SessionEntityTypes.ListSessionEntityTypes][google.cloud.dialogflow.cx.v3.SessionEntityTypes.ListSessionEntityTypes].

### [ListSessionEntityTypesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListSessionEntityTypesResponse)

The response message for [SessionEntityTypes.ListSessionEntityTypes][google.cloud.dialogflow.cx.v3.SessionEntityTypes.ListSessionEntityTypes].

### [ListTestCaseResultsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListTestCaseResultsRequest)

The request message for [TestCases.ListTestCaseResults][google.cloud.dialogflow.cx.v3.TestCases.ListTestCaseResults].

### [ListTestCaseResultsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListTestCaseResultsResponse)

The response message for [TestCases.ListTestCaseResults][google.cloud.dialogflow.cx.v3.TestCases.ListTestCaseResults].

### [ListTestCasesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListTestCasesRequest)

The request message for [TestCases.ListTestCases][google.cloud.dialogflow.cx.v3.TestCases.ListTestCases].

### [ListTestCasesRequest.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListTestCasesRequest.Types)

Container for nested types declared in the ListTestCasesRequest message type.

### [ListTestCasesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListTestCasesResponse)

The response message for [TestCases.ListTestCases][google.cloud.dialogflow.cx.v3.TestCases.ListTestCases].

### [ListToolVersionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListToolVersionsRequest)

The request message for [Tools.ListToolVersions][google.cloud.dialogflow.cx.v3.Tools.ListToolVersions].

### [ListToolVersionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListToolVersionsResponse)

The response message for [Tools.ListToolVersions][google.cloud.dialogflow.cx.v3.Tools.ListToolVersions].

### [ListToolsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListToolsRequest)

The request message for [Tools.ListTools][google.cloud.dialogflow.cx.v3.Tools.ListTools].

### [ListToolsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListToolsResponse)

The response message for [Tools.ListTools][google.cloud.dialogflow.cx.v3.Tools.ListTools].

### [ListTransitionRouteGroupsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListTransitionRouteGroupsRequest)

The request message for [TransitionRouteGroups.ListTransitionRouteGroups][google.cloud.dialogflow.cx.v3.TransitionRouteGroups.ListTransitionRouteGroups].

### [ListTransitionRouteGroupsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListTransitionRouteGroupsResponse)

The response message for [TransitionRouteGroups.ListTransitionRouteGroups][google.cloud.dialogflow.cx.v3.TransitionRouteGroups.ListTransitionRouteGroups].

### [ListVersionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListVersionsRequest)

The request message for [Versions.ListVersions][google.cloud.dialogflow.cx.v3.Versions.ListVersions].

### [ListVersionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListVersionsResponse)

The response message for [Versions.ListVersions][google.cloud.dialogflow.cx.v3.Versions.ListVersions].

### [ListWebhooksRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListWebhooksRequest)

The request message for [Webhooks.ListWebhooks][google.cloud.dialogflow.cx.v3.Webhooks.ListWebhooks].

### [ListWebhooksResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListWebhooksResponse)

The response message for [Webhooks.ListWebhooks][google.cloud.dialogflow.cx.v3.Webhooks.ListWebhooks].

### [LlmModelSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.LlmModelSettings)

Settings for LLM models.

### [LoadVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.LoadVersionRequest)

The request message for [Versions.LoadVersion][google.cloud.dialogflow.cx.v3.Versions.LoadVersion].

### [LookupEnvironmentHistoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.LookupEnvironmentHistoryRequest)

The request message for [Environments.LookupEnvironmentHistory][google.cloud.dialogflow.cx.v3.Environments.LookupEnvironmentHistory].

### [LookupEnvironmentHistoryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.LookupEnvironmentHistoryResponse)

The response message for [Environments.LookupEnvironmentHistory][google.cloud.dialogflow.cx.v3.Environments.LookupEnvironmentHistory].

### [Match](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Match)

Represents one match result of [MatchIntent][].

### [Match.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Match.Types)

Container for nested types declared in the Match message type.

### [MatchIntentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.MatchIntentRequest)

Request of [MatchIntent][].

### [MatchIntentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.MatchIntentResponse)

Response of [MatchIntent][].

### [ModelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ModelName)

Resource name for the `Model` resource.

### [NluSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.NluSettings)

Settings related to NLU.

### [NluSettings.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.NluSettings.Types)

Container for nested types declared in the NluSettings message type.

### [OutputAudioConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.OutputAudioConfig)

Instructs the speech synthesizer how to generate the output audio content.

### [Page](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Page)

A Dialogflow CX conversation (session) can be described and visualized as a state machine. The states of a CX session are represented by pages.

For each flow, you define many pages, where your combined pages can handle a complete conversation on the topics the flow is designed for. At any given moment, exactly one page is the current page, the current page is considered active, and the flow associated with that page is considered active. Every flow has a special start page. When a flow initially becomes active, the start page page becomes the current page. For each conversational turn, the current page will either stay the same or transition to another page.

You configure each page to collect information from the end-user that is relevant for the conversational state represented by the page.

For more information, see the [Page guide](https://cloud.google.com/dialogflow/cx/docs/concept/page).

### [PageInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.PageInfo)

Represents page information communicated to and from the webhook.

### [PageInfo.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.PageInfo.Types)

Container for nested types declared in the PageInfo message type.

### [PageInfo.Types.FormInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.PageInfo.Types.FormInfo)

Represents form information.

### [PageInfo.Types.FormInfo.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.PageInfo.Types.FormInfo.Types)

Container for nested types declared in the FormInfo message type.

### [PageInfo.Types.FormInfo.Types.ParameterInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.PageInfo.Types.FormInfo.Types.ParameterInfo)

Represents parameter information.

### [PageInfo.Types.FormInfo.Types.ParameterInfo.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.PageInfo.Types.FormInfo.Types.ParameterInfo.Types)

Container for nested types declared in the ParameterInfo message type.

### [PageName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.PageName)

Resource name for the `Page` resource.

### [Pages](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Pages)

Service for managing [Pages][google.cloud.dialogflow.cx.v3.Page].

### [Pages.PagesBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Pages.PagesBase)

Base class for server-side implementations of Pages

### [Pages.PagesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Pages.PagesClient)

Client for Pages

### [PagesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.PagesClient)

Pages client wrapper, for convenient use.

### [PagesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.PagesClientBuilder)

Builder class for [PagesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.PagesClient) to provide simple configuration of credentials, endpoint etc.

### [PagesClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.PagesClientImpl)

Pages client wrapper implementation, for convenient use.

### [PagesSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.PagesSettings)

Settings for [PagesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.PagesClient) instances.

### [ParameterDefinition](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ParameterDefinition)

Defines the properties of a parameter. Used to define parameters used in the agent and the input / output parameters for each fulfillment.

### [ParameterDefinition.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ParameterDefinition.Types)

Container for nested types declared in the ParameterDefinition message type.

### [Phrase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Phrase)

Text input which can be used for prompt or banned phrases.

### [Playbook](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Playbook)

Playbook is the basic building block to instruct the LLM how to execute a certain task.

A playbook consists of a goal to accomplish, an optional list of step by step instructions (the step instruction may refers to name of the custom or default plugin tools to use) to perform the task, a list of contextual input data to be passed in at the beginning of the invoked, and a list of output parameters to store the playbook result.

### [Playbook.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Playbook.Types)

Container for nested types declared in the Playbook message type.

### [Playbook.Types.Instruction](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Playbook.Types.Instruction)

Message of the Instruction of the playbook.

### [Playbook.Types.Step](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Playbook.Types.Step)

Message of single step execution.

### [PlaybookImportStrategy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.PlaybookImportStrategy)

The playbook import strategy used for resource conflict resolution associated with an [ImportPlaybookRequest][google.cloud.dialogflow.cx.v3.ImportPlaybookRequest].

### [PlaybookInput](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.PlaybookInput)

Input of the playbook.

### [PlaybookInvocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.PlaybookInvocation)

Stores metadata of the invocation of a child playbook.

### [PlaybookName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.PlaybookName)

Resource name for the `Playbook` resource.

### [PlaybookOutput](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.PlaybookOutput)

Output of the playbook.

### [PlaybookTraceMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.PlaybookTraceMetadata)

Metadata of the playbook trace.

### [PlaybookTransition](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.PlaybookTransition)

Stores metadata of the transition to another target playbook. Playbook transition actions exit the caller playbook and enter the target playbook.

### [PlaybookVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.PlaybookVersion)

Playbook version is a snapshot of the playbook at certain timestamp.

### [PlaybookVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.PlaybookVersionName)

Resource name for the `PlaybookVersion` resource.

### [Playbooks](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Playbooks)

Service for managing [Playbooks][google.cloud.dialogflow.cx.v3.Playbook].

### [Playbooks.PlaybooksBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Playbooks.PlaybooksBase)

Base class for server-side implementations of Playbooks

### [Playbooks.PlaybooksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Playbooks.PlaybooksClient)

Client for Playbooks

### [PlaybooksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.PlaybooksClient)

Playbooks client wrapper, for convenient use.

### [PlaybooksClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.PlaybooksClientBuilder)

Builder class for [PlaybooksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.PlaybooksClient) to provide simple configuration of credentials, endpoint etc.

### [PlaybooksClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.PlaybooksClientImpl)

Playbooks client wrapper implementation, for convenient use.

### [PlaybooksSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.PlaybooksSettings)

Settings for [PlaybooksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.PlaybooksClient) instances.

### [QueryInput](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.QueryInput)

Represents the query input. It can contain one of:

  1. A conversational query in the form of text.

  2. An intent query that specifies which intent to trigger.

  3. Natural language speech audio to be processed.

  4. An event to be triggered.

  5. DTMF digits to invoke an intent and fill in parameter value.

  6. The results of a tool executed by the client.




### [QueryParameters](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.QueryParameters)

Represents the parameters of a conversational query.

### [QueryResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.QueryResult)

Represents the result of a conversational query.

### [ResourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ResourceName)

Resource name and display name.

### [ResponseMessage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ResponseMessage)

Represents a response message that can be returned by a conversational agent.

Response messages are also used for output audio synthesis. The approach is as follows:

  * If at least one OutputAudioText response is present, then all OutputAudioText responses are linearly concatenated, and the result is used for output audio synthesis.
  * If the OutputAudioText responses are a mixture of text and SSML, then the concatenated result is treated as SSML; otherwise, the result is treated as either text or SSML as appropriate. The agent designer should ideally use either text or SSML consistently throughout the bot design.
  * Otherwise, all Text responses are linearly concatenated, and the result is used for output audio synthesis.



This approach allows for more sophisticated user experience scenarios, where the text displayed to the user may differ from what is heard.

### [ResponseMessage.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ResponseMessage.Types)

Container for nested types declared in the ResponseMessage message type.

### [ResponseMessage.Types.ConversationSuccess](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ResponseMessage.Types.ConversationSuccess)

Indicates that the conversation succeeded, i.e., the bot handled the issue that the customer talked to it about.

Dialogflow only uses this to determine which conversations should be counted as successful and doesn't process the metadata in this message in any way. Note that Dialogflow also considers conversations that get to the conversation end page as successful even if they don't return [ConversationSuccess][google.cloud.dialogflow.cx.v3.ResponseMessage.ConversationSuccess].

You may set this, for example:

  * In the [entry_fulfillment][google.cloud.dialogflow.cx.v3.Page.entry_fulfillment] of a [Page][google.cloud.dialogflow.cx.v3.Page] if entering the page indicates that the conversation succeeded.
  * In a webhook response when you determine that you handled the customer issue.



### [ResponseMessage.Types.EndInteraction](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ResponseMessage.Types.EndInteraction)

Indicates that interaction with the Dialogflow agent has ended. This message is generated by Dialogflow only and not supposed to be defined by the user.

### [ResponseMessage.Types.KnowledgeInfoCard](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ResponseMessage.Types.KnowledgeInfoCard)

Represents info card response. If the response contains generative knowledge prediction, Dialogflow will return a payload with Infobot Messenger compatible info card.

Otherwise, the info card response is skipped.

### [ResponseMessage.Types.LiveAgentHandoff](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ResponseMessage.Types.LiveAgentHandoff)

Indicates that the conversation should be handed off to a live agent.

Dialogflow only uses this to determine which conversations were handed off to a human agent for measurement purposes. What else to do with this signal is up to you and your handoff procedures.

You may set this, for example:

  * In the [entry_fulfillment][google.cloud.dialogflow.cx.v3.Page.entry_fulfillment] of a [Page][google.cloud.dialogflow.cx.v3.Page] if entering the page indicates something went extremely wrong in the conversation.
  * In a webhook response when you determine that the customer issue can only be handled by a human.



### [ResponseMessage.Types.MixedAudio](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ResponseMessage.Types.MixedAudio)

Represents an audio message that is composed of both segments synthesized from the Dialogflow agent prompts and ones hosted externally at the specified URIs. The external URIs are specified via [play_audio][google.cloud.dialogflow.cx.v3.ResponseMessage.play_audio]. This message is generated by Dialogflow only and not supposed to be defined by the user.

### [ResponseMessage.Types.MixedAudio.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ResponseMessage.Types.MixedAudio.Types)

Container for nested types declared in the MixedAudio message type.

### [ResponseMessage.Types.MixedAudio.Types.Segment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ResponseMessage.Types.MixedAudio.Types.Segment)

Represents one segment of audio.

### [ResponseMessage.Types.OutputAudioText](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ResponseMessage.Types.OutputAudioText)

A text or ssml response that is preferentially used for TTS output audio synthesis, as described in the comment on the ResponseMessage message.

### [ResponseMessage.Types.PlayAudio](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ResponseMessage.Types.PlayAudio)

Specifies an audio clip to be played by the client as part of the response.

### [ResponseMessage.Types.TelephonyTransferCall](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ResponseMessage.Types.TelephonyTransferCall)

Represents the signal that telles the client to transfer the phone call connected to the agent to a third-party endpoint.

### [ResponseMessage.Types.Text](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ResponseMessage.Types.Text)

The text response message.

### [RestoreAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.RestoreAgentRequest)

The request message for [Agents.RestoreAgent][google.cloud.dialogflow.cx.v3.Agents.RestoreAgent].

### [RestoreAgentRequest.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.RestoreAgentRequest.Types)

Container for nested types declared in the RestoreAgentRequest message type.

### [RestoreAgentRequest.Types.GitSource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.RestoreAgentRequest.Types.GitSource)

Settings for restoring from a git branch

### [RestorePlaybookVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.RestorePlaybookVersionRequest)

The request message for [Playbooks.RestorePlaybookVersion][google.cloud.dialogflow.cx.v3.Playbooks.RestorePlaybookVersion].

### [RestorePlaybookVersionResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.RestorePlaybookVersionResponse)

The response message for [Playbooks.RestorePlaybookVersion][google.cloud.dialogflow.cx.v3.Playbooks.RestorePlaybookVersion].

### [RestoreToolVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.RestoreToolVersionRequest)

The request message for [Tools.RestoreToolVersion][google.cloud.dialogflow.cx.v3.Tools.RestoreToolVersion].

### [RestoreToolVersionResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.RestoreToolVersionResponse)

The response message for [Tools.RestoreToolVersion][google.cloud.dialogflow.cx.v3.Tools.RestoreToolVersion].

### [RolloutConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.RolloutConfig)

The configuration for auto rollout.

### [RolloutConfig.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.RolloutConfig.Types)

Container for nested types declared in the RolloutConfig message type.

### [RolloutConfig.Types.RolloutStep](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.RolloutConfig.Types.RolloutStep)

A single rollout step with specified traffic allocation.

### [RolloutState](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.RolloutState)

State of the auto-rollout process.

### [RunContinuousTestMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.RunContinuousTestMetadata)

Metadata returned for the [Environments.RunContinuousTest][google.cloud.dialogflow.cx.v3.Environments.RunContinuousTest] long running operation.

### [RunContinuousTestRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.RunContinuousTestRequest)

The request message for [Environments.RunContinuousTest][google.cloud.dialogflow.cx.v3.Environments.RunContinuousTest].

### [RunContinuousTestResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.RunContinuousTestResponse)

The response message for [Environments.RunContinuousTest][google.cloud.dialogflow.cx.v3.Environments.RunContinuousTest].

### [RunTestCaseMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.RunTestCaseMetadata)

Metadata returned for the [TestCases.RunTestCase][google.cloud.dialogflow.cx.v3.TestCases.RunTestCase] long running operation. This message currently has no fields.

### [RunTestCaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.RunTestCaseRequest)

The request message for [TestCases.RunTestCase][google.cloud.dialogflow.cx.v3.TestCases.RunTestCase].

### [RunTestCaseResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.RunTestCaseResponse)

The response message for [TestCases.RunTestCase][google.cloud.dialogflow.cx.v3.TestCases.RunTestCase].

### [SafetySettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SafetySettings)

Settings for Generative Safety.

### [SafetySettings.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SafetySettings.Types)

Container for nested types declared in the SafetySettings message type.

### [SafetySettings.Types.Phrase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SafetySettings.Types.Phrase)

Text input which can be used for prompt or banned phrases.

### [SafetySettings.Types.PromptSecuritySettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SafetySettings.Types.PromptSecuritySettings)

Settings for prompt security checks.

### [SafetySettings.Types.RaiSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SafetySettings.Types.RaiSettings)

Settings for Responsible AI.

### [SafetySettings.Types.RaiSettings.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SafetySettings.Types.RaiSettings.Types)

Container for nested types declared in the RaiSettings message type.

### [SafetySettings.Types.RaiSettings.Types.CategoryFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SafetySettings.Types.RaiSettings.Types.CategoryFilter)

Configuration of the sensitivity level for blocking an RAI category.

### [SearchConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SearchConfig)

Search configuration for UCS search queries.

### [SecretVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SecretVersionName)

Resource name for the `SecretVersion` resource.

### [SecuritySettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SecuritySettings)

Represents the settings related to security issues, such as data redaction and data retention. It may take hours for updates on the settings to propagate to all the related components and take effect.

### [SecuritySettings.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SecuritySettings.Types)

Container for nested types declared in the SecuritySettings message type.

### [SecuritySettings.Types.AudioExportSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SecuritySettings.Types.AudioExportSettings)

Settings for exporting audio.

### [SecuritySettings.Types.AudioExportSettings.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SecuritySettings.Types.AudioExportSettings.Types)

Container for nested types declared in the AudioExportSettings message type.

### [SecuritySettings.Types.InsightsExportSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SecuritySettings.Types.InsightsExportSettings)

Settings for exporting conversations to [Insights](https://cloud.google.com/contact-center/insights/docs).

### [SecuritySettingsName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SecuritySettingsName)

Resource name for the `SecuritySettings` resource.

### [SecuritySettingsService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SecuritySettingsService)

Service for managing security settings for Dialogflow.

### [SecuritySettingsService.SecuritySettingsServiceBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SecuritySettingsService.SecuritySettingsServiceBase)

Base class for server-side implementations of SecuritySettingsService

### [SecuritySettingsService.SecuritySettingsServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SecuritySettingsService.SecuritySettingsServiceClient)

Client for SecuritySettingsService

### [SecuritySettingsServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SecuritySettingsServiceClient)

SecuritySettingsService client wrapper, for convenient use.

### [SecuritySettingsServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SecuritySettingsServiceClientBuilder)

Builder class for [SecuritySettingsServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SecuritySettingsServiceClient) to provide simple configuration of credentials, endpoint etc.

### [SecuritySettingsServiceClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SecuritySettingsServiceClientImpl)

SecuritySettingsService client wrapper implementation, for convenient use.

### [SecuritySettingsServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SecuritySettingsServiceSettings)

Settings for [SecuritySettingsServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SecuritySettingsServiceClient) instances.

### [SentimentAnalysisResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SentimentAnalysisResult)

The result of sentiment analysis. Sentiment analysis inspects user input and identifies the prevailing subjective opinion, especially to determine a user's attitude as positive, negative, or neutral.

### [ServiceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ServiceName)

Resource name for the `Service` resource.

### [SessionEntityType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SessionEntityType)

Session entity types are referred to as **User** entity types and are entities that are built for an individual user such as favorites, preferences, playlists, and so on.

You can redefine a session entity type at the session level to extend or replace a [custom entity type][google.cloud.dialogflow.cx.v3.EntityType] at the user session level (we refer to the entity types defined at the agent level as "custom entity types").

Note: session entity types apply to all queries, regardless of the language.

For more information about entity types, see the [Dialogflow documentation](https://cloud.google.com/dialogflow/docs/entities-overview).

### [SessionEntityType.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SessionEntityType.Types)

Container for nested types declared in the SessionEntityType message type.

### [SessionEntityTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SessionEntityTypeName)

Resource name for the `SessionEntityType` resource.

### [SessionEntityTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SessionEntityTypes)

Service for managing [SessionEntityTypes][google.cloud.dialogflow.cx.v3.SessionEntityType].

### [SessionEntityTypes.SessionEntityTypesBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SessionEntityTypes.SessionEntityTypesBase)

Base class for server-side implementations of SessionEntityTypes

### [SessionEntityTypes.SessionEntityTypesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SessionEntityTypes.SessionEntityTypesClient)

Client for SessionEntityTypes

### [SessionEntityTypesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SessionEntityTypesClient)

SessionEntityTypes client wrapper, for convenient use.

### [SessionEntityTypesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SessionEntityTypesClientBuilder)

Builder class for [SessionEntityTypesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SessionEntityTypesClient) to provide simple configuration of credentials, endpoint etc.

### [SessionEntityTypesClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SessionEntityTypesClientImpl)

SessionEntityTypes client wrapper implementation, for convenient use.

### [SessionEntityTypesSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SessionEntityTypesSettings)

Settings for [SessionEntityTypesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SessionEntityTypesClient) instances.

### [SessionInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SessionInfo)

Represents session information communicated to and from the webhook.

### [SessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SessionName)

Resource name for the `Session` resource.

### [Sessions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Sessions)

A session represents an interaction with a user. You retrieve user input and pass it to the [DetectIntent][google.cloud.dialogflow.cx.v3.Sessions.DetectIntent] method to determine user intent and respond.

### [Sessions.SessionsBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Sessions.SessionsBase)

Base class for server-side implementations of Sessions

### [Sessions.SessionsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Sessions.SessionsClient)

Client for Sessions

### [SessionsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SessionsClient)

Sessions client wrapper, for convenient use.

### [SessionsClient.ServerStreamingDetectIntentStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SessionsClient.ServerStreamingDetectIntentStream)

Server streaming methods for [ServerStreamingDetectIntent(DetectIntentRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SessionsClient#Google_Cloud_Dialogflow_Cx_V3_SessionsClient_ServerStreamingDetectIntent_Google_Cloud_Dialogflow_Cx_V3_DetectIntentRequest_Google_Api_Gax_Grpc_CallSettings_).

### [SessionsClient.StreamingDetectIntentStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SessionsClient.StreamingDetectIntentStream)

Bidirectional streaming methods for [StreamingDetectIntent(CallSettings, BidirectionalStreamingSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SessionsClient#Google_Cloud_Dialogflow_Cx_V3_SessionsClient_StreamingDetectIntent_Google_Api_Gax_Grpc_CallSettings_Google_Api_Gax_Grpc_BidirectionalStreamingSettings_).

### [SessionsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SessionsClientBuilder)

Builder class for [SessionsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SessionsClient) to provide simple configuration of credentials, endpoint etc.

### [SessionsClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SessionsClientImpl)

Sessions client wrapper implementation, for convenient use.

### [SessionsSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SessionsSettings)

Settings for [SessionsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SessionsClient) instances.

### [SpeechProcessingMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SpeechProcessingMetadata)

Metadata of the speech-to-text and text-to-speech processing.

### [SpeechToTextSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SpeechToTextSettings)

Settings related to speech recognition.

### [SpeechWordInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SpeechWordInfo)

Information for a word recognized by the speech recognizer.

### [StartExperimentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.StartExperimentRequest)

The request message for [Experiments.StartExperiment][google.cloud.dialogflow.cx.v3.Experiments.StartExperiment].

### [StopExperimentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.StopExperimentRequest)

The request message for [Experiments.StopExperiment][google.cloud.dialogflow.cx.v3.Experiments.StopExperiment].

### [StreamingDetectIntentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.StreamingDetectIntentRequest)

The top-level message sent by the client to the [Sessions.StreamingDetectIntent][google.cloud.dialogflow.cx.v3.Sessions.StreamingDetectIntent] method.

Multiple request messages should be sent in order:

  1. The first message must contain [session][google.cloud.dialogflow.cx.v3.StreamingDetectIntentRequest.session], [query_input][google.cloud.dialogflow.cx.v3.StreamingDetectIntentRequest.query_input] plus optionally [query_params][google.cloud.dialogflow.cx.v3.StreamingDetectIntentRequest.query_params]. If the client wants to receive an audio response, it should also contain [output_audio_config][google.cloud.dialogflow.cx.v3.StreamingDetectIntentRequest.output_audio_config].

  2. If [query_input][google.cloud.dialogflow.cx.v3.StreamingDetectIntentRequest.query_input] was set to [query_input.audio.config][google.cloud.dialogflow.cx.v3.AudioInput.config], all subsequent messages must contain [query_input.audio.audio][google.cloud.dialogflow.cx.v3.AudioInput.audio] to continue with Speech recognition. If you decide to rather detect an intent from text input after you already started Speech recognition, please send a message with [query_input.text][google.cloud.dialogflow.cx.v3.QueryInput.text].

However, note that:

     * Dialogflow will bill you for the audio duration so far.
     * Dialogflow discards all Speech recognition results in favor of the input text.
     * Dialogflow will use the language code from the first message.



After you sent all input, you must half-close or abort the request stream.

### [StreamingDetectIntentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.StreamingDetectIntentResponse)

The top-level message returned from the [StreamingDetectIntent][google.cloud.dialogflow.cx.v3.Sessions.StreamingDetectIntent] method.

Multiple response messages can be returned in order:

  * If the `StreamingDetectIntentRequest.query_input.audio` field was set, the first M messages contain `recognition_result`. Each `recognition_result` represents a more complete transcript of what the user said. The last `recognition_result` has `is_final` set to `true`.

  * If the `StreamingDetectIntentRequest.enable_partial_response` field was true, the `detect_intent_response` field is populated for each of the following N responses, where 0 <= N <= 5. These responses set the [DetectIntentResponse.response_type][google.cloud.dialogflow.cx.v3.DetectIntentResponse.response_type] field to `PARTIAL`.




For the last response message, the `detect_intent_response` is fully populated, and [DetectIntentResponse.response_type][google.cloud.dialogflow.cx.v3.DetectIntentResponse.response_type] is set to `FINAL`.

### [StreamingRecognitionResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.StreamingRecognitionResult)

Contains a speech recognition result corresponding to a portion of the audio that is currently being processed or an indication that this is the end of the single requested utterance.

While end-user audio is being processed, Dialogflow sends a series of results. Each result may contain a `transcript` value. A transcript represents a portion of the utterance. While the recognizer is processing audio, transcript values may be interim values or finalized values. Once a transcript is finalized, the `is_final` value is set to true and processing continues for the next transcript.

If `StreamingDetectIntentRequest.query_input.audio.config.single_utterance` was true, and the recognizer has completed processing audio, the `message_type` value is set to `END_OF_SINGLE_UTTERANCE and the following (last) result contains the last finalized transcript.

The complete end-user utterance is determined by concatenating the finalized transcript values received for the series of results.

In the following example, single utterance is enabled. In the case where single utterance is not enabled, result 7 would not occur.
    
    
    Num | transcript              | message_type            | is_final
    --- | ----------------------- | ----------------------- | --------
    1   | "tube"                  | TRANSCRIPT              | false
    2   | "to be a"               | TRANSCRIPT              | false
    3   | "to be"                 | TRANSCRIPT              | false
    4   | "to be or not to be"    | TRANSCRIPT              | true
    5   | "that's"                | TRANSCRIPT              | false
    6   | "that is                | TRANSCRIPT              | false
    7   | unset                   | END_OF_SINGLE_UTTERANCE | unset
    8   | " that is the question" | TRANSCRIPT              | true
    

Concatenating the finalized transcripts with `is_final` set to true, the complete utterance becomes "to be or not to be that is the question".

### [StreamingRecognitionResult.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.StreamingRecognitionResult.Types)

Container for nested types declared in the StreamingRecognitionResult message type.

### [SubmitAnswerFeedbackRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SubmitAnswerFeedbackRequest)

The request to set the feedback for a bot answer.

### [SynthesizeSpeechConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SynthesizeSpeechConfig)

Configuration of how speech should be synthesized.

### [TestCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.TestCase)

Represents a test case.

### [TestCaseError](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.TestCaseError)

Error info for importing a test.

### [TestCaseName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.TestCaseName)

Resource name for the `TestCase` resource.

### [TestCaseResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.TestCaseResult)

Represents a result from running a test case in an agent environment.

### [TestCaseResultName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.TestCaseResultName)

Resource name for the `TestCaseResult` resource.

### [TestCases](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.TestCases)

Service for managing [Test Cases][google.cloud.dialogflow.cx.v3.TestCase] and [Test Case Results][google.cloud.dialogflow.cx.v3.TestCaseResult].

### [TestCases.TestCasesBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.TestCases.TestCasesBase)

Base class for server-side implementations of TestCases

### [TestCases.TestCasesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.TestCases.TestCasesClient)

Client for TestCases

### [TestCasesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.TestCasesClient)

TestCases client wrapper, for convenient use.

### [TestCasesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.TestCasesClientBuilder)

Builder class for [TestCasesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.TestCasesClient) to provide simple configuration of credentials, endpoint etc.

### [TestCasesClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.TestCasesClientImpl)

TestCases client wrapper implementation, for convenient use.

### [TestCasesSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.TestCasesSettings)

Settings for [TestCasesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.TestCasesClient) instances.

### [TestConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.TestConfig)

Represents configurations for a test case.

### [TestError](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.TestError)

Error info for running a test.

### [TestRunDifference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.TestRunDifference)

The description of differences between original and replayed agent output.

### [TestRunDifference.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.TestRunDifference.Types)

Container for nested types declared in the TestRunDifference message type.

### [TextInput](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.TextInput)

Represents the natural language text to be processed.

### [TextToSpeechSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.TextToSpeechSettings)

Settings related to speech synthesizing.

### [Tool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Tool)

A tool provides a list of actions which are available to the [Playbook][google.cloud.dialogflow.cx.v3.Playbook] to attain its goal. A Tool consists of a description of the tool's usage and a specification of the tool which contains the schema and authentication information.

### [Tool.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Tool.Types)

Container for nested types declared in the Tool message type.

### [Tool.Types.Authentication](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Tool.Types.Authentication)

Authentication information required for API calls

### [Tool.Types.Authentication.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Tool.Types.Authentication.Types)

Container for nested types declared in the Authentication message type.

### [Tool.Types.Authentication.Types.ApiKeyConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Tool.Types.Authentication.Types.ApiKeyConfig)

Config for authentication with API key.

### [Tool.Types.Authentication.Types.BearerTokenConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Tool.Types.Authentication.Types.BearerTokenConfig)

Config for authentication using bearer token.

### [Tool.Types.Authentication.Types.OAuthConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Tool.Types.Authentication.Types.OAuthConfig)

Config for authentication with OAuth.

### [Tool.Types.Authentication.Types.OAuthConfig.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Tool.Types.Authentication.Types.OAuthConfig.Types)

Container for nested types declared in the OAuthConfig message type.

### [Tool.Types.Authentication.Types.ServiceAccountAuthConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Tool.Types.Authentication.Types.ServiceAccountAuthConfig)

Configuration for authentication using a service account.

### [Tool.Types.Authentication.Types.ServiceAgentAuthConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Tool.Types.Authentication.Types.ServiceAgentAuthConfig)

Config for auth using [Diglogflow service agent](https://cloud.google.com/iam/docs/service-agents#dialogflow-service-agent).

### [Tool.Types.Authentication.Types.ServiceAgentAuthConfig.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Tool.Types.Authentication.Types.ServiceAgentAuthConfig.Types)

Container for nested types declared in the ServiceAgentAuthConfig message type.

### [Tool.Types.DataStoreTool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Tool.Types.DataStoreTool)

A DataStoreTool is a way to provide specifications needed to search a list of data stores.

### [Tool.Types.DataStoreTool.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Tool.Types.DataStoreTool.Types)

Container for nested types declared in the DataStoreTool message type.

### [Tool.Types.DataStoreTool.Types.FallbackPrompt](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Tool.Types.DataStoreTool.Types.FallbackPrompt)

A FallbackPrompt is a way to provide specifications for the Data Store fallback prompt when generating responses.

### [Tool.Types.FunctionTool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Tool.Types.FunctionTool)

A Function tool describes the functions to be invoked on the client side.

### [Tool.Types.OpenApiTool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Tool.Types.OpenApiTool)

An OpenAPI tool is a way to provide the Tool specifications in the Open API schema format.

### [Tool.Types.ServiceDirectoryConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Tool.Types.ServiceDirectoryConfig)

Configuration for tools using Service Directory.

### [Tool.Types.TLSConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Tool.Types.TLSConfig)

The TLS configuration.

### [Tool.Types.TLSConfig.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Tool.Types.TLSConfig.Types)

Container for nested types declared in the TLSConfig message type.

### [Tool.Types.TLSConfig.Types.CACert](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Tool.Types.TLSConfig.Types.CACert)

The CA certificate.

### [ToolCall](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ToolCall)

Represents a call of a specific tool's action with the specified inputs.

### [ToolCallResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ToolCallResult)

The result of calling a tool's action that has been executed by the client.

### [ToolCallResult.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ToolCallResult.Types)

Container for nested types declared in the ToolCallResult message type.

### [ToolCallResult.Types.Error](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ToolCallResult.Types.Error)

An error produced by the tool call.

### [ToolName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ToolName)

Resource name for the `Tool` resource.

### [ToolUse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ToolUse)

Stores metadata of the invocation of an action supported by a tool.

### [ToolVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ToolVersion)

Tool version is a snapshot of the tool at certain timestamp.

### [ToolVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ToolVersionName)

Resource name for the `ToolVersion` resource.

### [Tools](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Tools)

Service for managing [Tools][google.cloud.dialogflow.cx.v3.Tool].

### [Tools.ToolsBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Tools.ToolsBase)

Base class for server-side implementations of Tools

### [Tools.ToolsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Tools.ToolsClient)

Client for Tools

### [ToolsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ToolsClient)

Tools client wrapper, for convenient use.

### [ToolsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ToolsClientBuilder)

Builder class for [ToolsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ToolsClient) to provide simple configuration of credentials, endpoint etc.

### [ToolsClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ToolsClientImpl)

Tools client wrapper implementation, for convenient use.

### [ToolsSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ToolsSettings)

Settings for [ToolsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ToolsClient) instances.

### [TraceBlock](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.TraceBlock)

The trace block tracks a sequence of actions taken by the agent in a flow or a playbook.

### [TrainFlowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.TrainFlowRequest)

The request message for [Flows.TrainFlow][google.cloud.dialogflow.cx.v3.Flows.TrainFlow].

### [TransitionCoverage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.TransitionCoverage)

Transition coverage represents the percentage of all possible page transitions (page-level transition routes and event handlers, excluding transition route groups) present within any of a parent's test cases.

### [TransitionCoverage.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.TransitionCoverage.Types)

Container for nested types declared in the TransitionCoverage message type.

### [TransitionCoverage.Types.Transition](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.TransitionCoverage.Types.Transition)

A transition in a page.

### [TransitionCoverage.Types.TransitionNode](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.TransitionCoverage.Types.TransitionNode)

The source or target of a transition.

### [TransitionRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.TransitionRoute)

A transition route specifies a [intent][google.cloud.dialogflow.cx.v3.Intent] that can be matched and/or a data condition that can be evaluated during a session. When a specified transition is matched, the following actions are taken in order:

  * If there is a [`trigger_fulfillment`][google.cloud.dialogflow.cx.v3.TransitionRoute.trigger_fulfillment] associated with the transition, it will be called.
  * If there is a [`target_page`][google.cloud.dialogflow.cx.v3.TransitionRoute.target_page] associated with the transition, the session will transition into the specified page.
  * If there is a [`target_flow`][google.cloud.dialogflow.cx.v3.TransitionRoute.target_flow] associated with the transition, the session will transition into the specified flow.



### [TransitionRouteGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.TransitionRouteGroup)

A TransitionRouteGroup represents a group of [`TransitionRoutes`][google.cloud.dialogflow.cx.v3.TransitionRoute] to be used by a [Page][google.cloud.dialogflow.cx.v3.Page].

### [TransitionRouteGroupCoverage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.TransitionRouteGroupCoverage)

Transition route group coverage represents the percentage of all possible transition routes present within any of a parent's test cases. The results are grouped by the transition route group.

### [TransitionRouteGroupCoverage.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.TransitionRouteGroupCoverage.Types)

Container for nested types declared in the TransitionRouteGroupCoverage message type.

### [TransitionRouteGroupCoverage.Types.Coverage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.TransitionRouteGroupCoverage.Types.Coverage)

Coverage result message for one transition route group.

### [TransitionRouteGroupCoverage.Types.Coverage.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.TransitionRouteGroupCoverage.Types.Coverage.Types)

Container for nested types declared in the Coverage message type.

### [TransitionRouteGroupCoverage.Types.Coverage.Types.Transition](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.TransitionRouteGroupCoverage.Types.Coverage.Types.Transition)

A transition coverage in a transition route group.

### [TransitionRouteGroupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.TransitionRouteGroupName)

Resource name for the `TransitionRouteGroup` resource.

### [TransitionRouteGroups](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.TransitionRouteGroups)

Service for managing [TransitionRouteGroups][google.cloud.dialogflow.cx.v3.TransitionRouteGroup].

### [TransitionRouteGroups.TransitionRouteGroupsBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.TransitionRouteGroups.TransitionRouteGroupsBase)

Base class for server-side implementations of TransitionRouteGroups

### [TransitionRouteGroups.TransitionRouteGroupsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.TransitionRouteGroups.TransitionRouteGroupsClient)

Client for TransitionRouteGroups

### [TransitionRouteGroupsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.TransitionRouteGroupsClient)

TransitionRouteGroups client wrapper, for convenient use.

### [TransitionRouteGroupsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.TransitionRouteGroupsClientBuilder)

Builder class for [TransitionRouteGroupsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.TransitionRouteGroupsClient) to provide simple configuration of credentials, endpoint etc.

### [TransitionRouteGroupsClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.TransitionRouteGroupsClientImpl)

TransitionRouteGroups client wrapper implementation, for convenient use.

### [TransitionRouteGroupsSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.TransitionRouteGroupsSettings)

Settings for [TransitionRouteGroupsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.TransitionRouteGroupsClient) instances.

### [TypeSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.TypeSchema)

Encapsulates different type schema variations: either a reference to an a schema that's already defined by a tool, or an inline definition.

### [TypeSchema.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.TypeSchema.Types)

Container for nested types declared in the TypeSchema message type.

### [TypeSchema.Types.SchemaReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.TypeSchema.Types.SchemaReference)

A reference to the schema of an existing tool.

### [UpdateAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.UpdateAgentRequest)

The request message for [Agents.UpdateAgent][google.cloud.dialogflow.cx.v3.Agents.UpdateAgent].

### [UpdateEntityTypeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.UpdateEntityTypeRequest)

The request message for [EntityTypes.UpdateEntityType][google.cloud.dialogflow.cx.v3.EntityTypes.UpdateEntityType].

### [UpdateEnvironmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.UpdateEnvironmentRequest)

The request message for [Environments.UpdateEnvironment][google.cloud.dialogflow.cx.v3.Environments.UpdateEnvironment].

### [UpdateExampleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.UpdateExampleRequest)

The request message for [Examples.UpdateExample][google.cloud.dialogflow.cx.v3.Examples.UpdateExample].

### [UpdateExperimentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.UpdateExperimentRequest)

The request message for [Experiments.UpdateExperiment][google.cloud.dialogflow.cx.v3.Experiments.UpdateExperiment].

### [UpdateFlowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.UpdateFlowRequest)

The request message for [Flows.UpdateFlow][google.cloud.dialogflow.cx.v3.Flows.UpdateFlow].

### [UpdateGenerativeSettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.UpdateGenerativeSettingsRequest)

Request for [UpdateGenerativeSettings][google.cloud.dialogflow.cx.v3.Agents.UpdateGenerativeSettings] RPC.

### [UpdateGeneratorRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.UpdateGeneratorRequest)

The request message for [Generators.UpdateGenerator][google.cloud.dialogflow.cx.v3.Generators.UpdateGenerator].

### [UpdateIntentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.UpdateIntentRequest)

The request message for [Intents.UpdateIntent][google.cloud.dialogflow.cx.v3.Intents.UpdateIntent].

### [UpdatePageRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.UpdatePageRequest)

The request message for [Pages.UpdatePage][google.cloud.dialogflow.cx.v3.Pages.UpdatePage].

### [UpdatePlaybookRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.UpdatePlaybookRequest)

The request message for [Playbooks.UpdatePlaybook][google.cloud.dialogflow.cx.v3.Playbooks.UpdatePlaybook].

### [UpdateSecuritySettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.UpdateSecuritySettingsRequest)

The request message for [SecuritySettingsService.UpdateSecuritySettings][google.cloud.dialogflow.cx.v3.SecuritySettingsService.UpdateSecuritySettings].

### [UpdateSessionEntityTypeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.UpdateSessionEntityTypeRequest)

The request message for [SessionEntityTypes.UpdateSessionEntityType][google.cloud.dialogflow.cx.v3.SessionEntityTypes.UpdateSessionEntityType].

### [UpdateTestCaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.UpdateTestCaseRequest)

The request message for [TestCases.UpdateTestCase][google.cloud.dialogflow.cx.v3.TestCases.UpdateTestCase].

### [UpdateToolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.UpdateToolRequest)

The request message for [Tools.UpdateTool][google.cloud.dialogflow.cx.v3.Tools.UpdateTool].

### [UpdateTransitionRouteGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.UpdateTransitionRouteGroupRequest)

The request message for [TransitionRouteGroups.UpdateTransitionRouteGroup][google.cloud.dialogflow.cx.v3.TransitionRouteGroups.UpdateTransitionRouteGroup].

### [UpdateVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.UpdateVersionRequest)

The request message for [Versions.UpdateVersion][google.cloud.dialogflow.cx.v3.Versions.UpdateVersion].

### [UpdateWebhookRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.UpdateWebhookRequest)

The request message for [Webhooks.UpdateWebhook][google.cloud.dialogflow.cx.v3.Webhooks.UpdateWebhook].

### [UserUtterance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.UserUtterance)

UserUtterance represents one message sent by the customer.

### [ValidateAgentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ValidateAgentRequest)

The request message for [Agents.ValidateAgent][google.cloud.dialogflow.cx.v3.Agents.ValidateAgent].

### [ValidateFlowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ValidateFlowRequest)

The request message for [Flows.ValidateFlow][google.cloud.dialogflow.cx.v3.Flows.ValidateFlow].

### [ValidationMessage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ValidationMessage)

Agent/flow validation message.

### [ValidationMessage.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ValidationMessage.Types)

Container for nested types declared in the ValidationMessage message type.

### [VariantsHistory](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.VariantsHistory)

The history of variants update.

### [Version](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Version)

Represents a version of a flow.

### [Version.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Version.Types)

Container for nested types declared in the Version message type.

### [VersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.VersionName)

Resource name for the `Version` resource.

### [VersionVariants](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.VersionVariants)

A list of flow version variants.

### [VersionVariants.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.VersionVariants.Types)

Container for nested types declared in the VersionVariants message type.

### [VersionVariants.Types.Variant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.VersionVariants.Types.Variant)

A single flow version with specified traffic allocation.

### [Versions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Versions)

Service for managing [Versions][google.cloud.dialogflow.cx.v3.Version].

### [Versions.VersionsBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Versions.VersionsBase)

Base class for server-side implementations of Versions

### [Versions.VersionsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Versions.VersionsClient)

Client for Versions

### [VersionsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.VersionsClient)

Versions client wrapper, for convenient use.

### [VersionsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.VersionsClientBuilder)

Builder class for [VersionsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.VersionsClient) to provide simple configuration of credentials, endpoint etc.

### [VersionsClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.VersionsClientImpl)

Versions client wrapper implementation, for convenient use.

### [VersionsSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.VersionsSettings)

Settings for [VersionsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.VersionsClient) instances.

### [VoiceSelectionParams](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.VoiceSelectionParams)

Description of which voice to use for speech synthesis.

### [Webhook](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Webhook)

Webhooks host the developer's business logic. During a session, webhooks allow the developer to use the data extracted by Dialogflow's natural language processing to generate dynamic responses, validate collected data, or trigger actions on the backend.

### [Webhook.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Webhook.Types)

Container for nested types declared in the Webhook message type.

### [Webhook.Types.GenericWebService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Webhook.Types.GenericWebService)

Represents configuration for a generic web service.

### [Webhook.Types.GenericWebService.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Webhook.Types.GenericWebService.Types)

Container for nested types declared in the GenericWebService message type.

### [Webhook.Types.GenericWebService.Types.OAuthConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Webhook.Types.GenericWebService.Types.OAuthConfig)

Represents configuration of OAuth client credential flow for 3rd party API authentication.

### [Webhook.Types.GenericWebService.Types.SecretVersionHeaderValue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Webhook.Types.GenericWebService.Types.SecretVersionHeaderValue)

Represents the value of an HTTP header stored in a SecretManager secret version.

### [Webhook.Types.GenericWebService.Types.ServiceAccountAuthConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Webhook.Types.GenericWebService.Types.ServiceAccountAuthConfig)

Configuration for authentication using a service account.

### [Webhook.Types.ServiceDirectoryConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Webhook.Types.ServiceDirectoryConfig)

Represents configuration for a [Service Directory](https://cloud.google.com/service-directory) service.

### [WebhookName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.WebhookName)

Resource name for the `Webhook` resource.

### [WebhookRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.WebhookRequest)

The request message for a webhook call. The request is sent as a JSON object and the field names will be presented in camel cases.

You may see undocumented fields in an actual request. These fields are used internally by Dialogflow and should be ignored.

### [WebhookRequest.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.WebhookRequest.Types)

Container for nested types declared in the WebhookRequest message type.

### [WebhookRequest.Types.FulfillmentInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.WebhookRequest.Types.FulfillmentInfo)

Represents fulfillment information communicated to the webhook.

### [WebhookRequest.Types.IntentInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.WebhookRequest.Types.IntentInfo)

Represents intent information communicated to the webhook.

### [WebhookRequest.Types.IntentInfo.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.WebhookRequest.Types.IntentInfo.Types)

Container for nested types declared in the IntentInfo message type.

### [WebhookRequest.Types.IntentInfo.Types.IntentParameterValue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.WebhookRequest.Types.IntentInfo.Types.IntentParameterValue)

Represents a value for an intent parameter.

### [WebhookRequest.Types.SentimentAnalysisResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.WebhookRequest.Types.SentimentAnalysisResult)

Represents the result of sentiment analysis.

### [WebhookResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.WebhookResponse)

The response message for a webhook call.

### [WebhookResponse.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.WebhookResponse.Types)

Container for nested types declared in the WebhookResponse message type.

### [WebhookResponse.Types.FulfillmentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.WebhookResponse.Types.FulfillmentResponse)

Represents a fulfillment response to the user.

### [WebhookResponse.Types.FulfillmentResponse.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.WebhookResponse.Types.FulfillmentResponse.Types)

Container for nested types declared in the FulfillmentResponse message type.

### [Webhooks](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Webhooks)

Service for managing [Webhooks][google.cloud.dialogflow.cx.v3.Webhook].

### [Webhooks.WebhooksBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Webhooks.WebhooksBase)

Base class for server-side implementations of Webhooks

### [Webhooks.WebhooksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Webhooks.WebhooksClient)

Client for Webhooks

### [WebhooksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.WebhooksClient)

Webhooks client wrapper, for convenient use.

### [WebhooksClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.WebhooksClientBuilder)

Builder class for [WebhooksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.WebhooksClient) to provide simple configuration of credentials, endpoint etc.

### [WebhooksClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.WebhooksClientImpl)

Webhooks client wrapper implementation, for convenient use.

### [WebhooksSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.WebhooksSettings)

Settings for [WebhooksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.WebhooksClient) instances.

## Enums 

### [Action.ActionOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Action.ActionOneofCase)

Enum of possible cases for the "action" oneof.

### [Agent.SessionEntryResourceOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent.SessionEntryResourceOneofCase)

Enum of possible cases for the "session_entry_resource" oneof.

### [Agent.Types.GitIntegrationSettings.GitSettingsOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent.Types.GitIntegrationSettings.GitSettingsOneofCase)

Enum of possible cases for the "git_settings" oneof.

### [AgentGenerativeSettingsName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentGenerativeSettingsName.ResourceNameType)

The possible contents of [AgentGenerativeSettingsName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentGenerativeSettingsName).

### [AgentName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentName.ResourceNameType)

The possible contents of [AgentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentName).

### [AgentValidationResultName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentValidationResultName.ResourceNameType)

The possible contents of [AgentValidationResultName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentValidationResultName).

### [AnswerFeedback.Types.Rating](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AnswerFeedback.Types.Rating)

Represents thumbs up/down rating provided by user about a response.

### [AudioEncoding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AudioEncoding)

Audio encoding of the audio content sent in the conversational query request. Refer to the [Cloud Speech API documentation](https://cloud.google.com/speech-to-text/docs/basics) for more details.

### [BoostSpec.Types.ConditionBoostSpec.Types.BoostControlSpec.Types.AttributeType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.BoostSpec.Types.ConditionBoostSpec.Types.BoostControlSpec.Types.AttributeType)

The attribute(or function) for which the custom ranking is to be applied.

### [BoostSpec.Types.ConditionBoostSpec.Types.BoostControlSpec.Types.InterpolationType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.BoostSpec.Types.ConditionBoostSpec.Types.BoostControlSpec.Types.InterpolationType)

The interpolation type to be applied. Default will be linear (Piecewise Linear).

### [CalculateCoverageRequest.Types.CoverageType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.CalculateCoverageRequest.Types.CoverageType)

The type of coverage score requested.

### [CalculateCoverageResponse.CoverageTypeOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.CalculateCoverageResponse.CoverageTypeOneofCase)

Enum of possible cases for the "coverage_type" oneof.

### [ChangelogName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ChangelogName.ResourceNameType)

The possible contents of [ChangelogName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ChangelogName).

### [ContinuousTestResult.Types.AggregatedTestResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ContinuousTestResult.Types.AggregatedTestResult)

The overall result for a continuous test run in an agent environment.

### [ContinuousTestResultName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ContinuousTestResultName.ResourceNameType)

The possible contents of [ContinuousTestResultName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ContinuousTestResultName).

### [DataStoreConnectionSignals.Types.GroundingSignals.Types.GroundingDecision](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DataStoreConnectionSignals.Types.GroundingSignals.Types.GroundingDecision)

Represents the decision of the grounding check.

### [DataStoreConnectionSignals.Types.GroundingSignals.Types.GroundingScoreBucket](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DataStoreConnectionSignals.Types.GroundingSignals.Types.GroundingScoreBucket)

Grounding score buckets.

### [DataStoreConnectionSignals.Types.SafetySignals.Types.BannedPhraseMatch](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DataStoreConnectionSignals.Types.SafetySignals.Types.BannedPhraseMatch)

Specifies banned phrase match subject.

### [DataStoreConnectionSignals.Types.SafetySignals.Types.SafetyDecision](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DataStoreConnectionSignals.Types.SafetySignals.Types.SafetyDecision)

Safety decision. All kinds of check are incorporated into this final decision, including banned phrases check.

### [DataStoreName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DataStoreName.ResourceNameType)

The possible contents of [DataStoreName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DataStoreName).

### [DataStoreType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DataStoreType)

Type of a data store. Determines how search is performed in the data store.

### [DataType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DataType)

Defines data types that are supported for inlined schemas. These types are consistent with [google.protobuf.Value][google.protobuf.Value].

### [DeidentifyTemplateName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DeidentifyTemplateName.ResourceNameType)

The possible contents of [DeidentifyTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DeidentifyTemplateName).

### [Deployment.Types.State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Deployment.Types.State)

The state of the deployment.

### [DeploymentName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DeploymentName.ResourceNameType)

The possible contents of [DeploymentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DeploymentName).

### [DetectIntentResponse.Types.ResponseType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DetectIntentResponse.Types.ResponseType)

Represents different DetectIntentResponse types.

### [DetectIntentResponseView](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DetectIntentResponseView)

The response view specifies which fields in the [QueryResult][google.cloud.dialogflow.cx.v3.QueryResult] to return.

### [DocumentProcessingMode](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.DocumentProcessingMode)

The document processing mode of the data store.

### [EntityType.Types.AutoExpansionMode](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityType.Types.AutoExpansionMode)

Represents different entity type expansion modes. Automated expansion allows an agent to recognize values that have not been explicitly listed in the entity (for example, new kinds of shopping list items).

### [EntityType.Types.Kind](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityType.Types.Kind)

Represents kinds of entities.

### [EntityTypeName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityTypeName.ResourceNameType)

The possible contents of [EntityTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityTypeName).

### [EnvironmentName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EnvironmentName.ResourceNameType)

The possible contents of [EnvironmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EnvironmentName).

### [EventHandler.TargetOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EventHandler.TargetOneofCase)

Enum of possible cases for the "target" oneof.

### [ExampleName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExampleName.ResourceNameType)

The possible contents of [ExampleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExampleName).

### [Experiment.Types.Definition.VariantsOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Experiment.Types.Definition.VariantsOneofCase)

Enum of possible cases for the "variants" oneof.

### [Experiment.Types.Result.Types.CountType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Experiment.Types.Result.Types.CountType)

Types of count-based metric for Dialogflow experiment.

### [Experiment.Types.Result.Types.Metric.ValueOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Experiment.Types.Result.Types.Metric.ValueOneofCase)

Enum of possible cases for the "value" oneof.

### [Experiment.Types.Result.Types.MetricType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Experiment.Types.Result.Types.MetricType)

Types of ratio-based metric for Dialogflow experiment.

### [Experiment.Types.State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Experiment.Types.State)

The state of the experiment.

### [ExperimentName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExperimentName.ResourceNameType)

The possible contents of [ExperimentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExperimentName).

### [ExportAgentRequest.Types.DataFormat](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportAgentRequest.Types.DataFormat)

Data format of the exported agent.

### [ExportAgentResponse.AgentOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportAgentResponse.AgentOneofCase)

Enum of possible cases for the "agent" oneof.

### [ExportEntityTypesRequest.DestinationOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportEntityTypesRequest.DestinationOneofCase)

Enum of possible cases for the "destination" oneof.

### [ExportEntityTypesRequest.Types.DataFormat](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportEntityTypesRequest.Types.DataFormat)

Data format of the exported entity types.

### [ExportEntityTypesResponse.ExportedEntityTypesOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportEntityTypesResponse.ExportedEntityTypesOneofCase)

Enum of possible cases for the "exported_entity_types" oneof.

### [ExportFlowResponse.FlowOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportFlowResponse.FlowOneofCase)

Enum of possible cases for the "flow" oneof.

### [ExportIntentsRequest.DestinationOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportIntentsRequest.DestinationOneofCase)

Enum of possible cases for the "destination" oneof.

### [ExportIntentsRequest.Types.DataFormat](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportIntentsRequest.Types.DataFormat)

Data format of the exported intents.

### [ExportIntentsResponse.IntentsOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportIntentsResponse.IntentsOneofCase)

Enum of possible cases for the "intents" oneof.

### [ExportPlaybookRequest.Types.DataFormat](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportPlaybookRequest.Types.DataFormat)

Data format of the exported playbook.

### [ExportPlaybookResponse.PlaybookOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportPlaybookResponse.PlaybookOneofCase)

Enum of possible cases for the "playbook" oneof.

### [ExportTestCasesRequest.DestinationOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportTestCasesRequest.DestinationOneofCase)

Enum of possible cases for the "destination" oneof.

### [ExportTestCasesRequest.Types.DataFormat](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportTestCasesRequest.Types.DataFormat)

Data format of the exported test cases.

### [ExportTestCasesResponse.DestinationOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ExportTestCasesResponse.DestinationOneofCase)

Enum of possible cases for the "destination" oneof.

### [FlowName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.FlowName.ResourceNameType)

The possible contents of [FlowName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.FlowName).

### [FlowValidationResultName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.FlowValidationResultName.ResourceNameType)

The possible contents of [FlowValidationResultName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.FlowValidationResultName).

### [Fulfillment.Types.ConditionalCases.Types.Case.Types.CaseContent.CasesOrMessageOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Fulfillment.Types.ConditionalCases.Types.Case.Types.CaseContent.CasesOrMessageOneofCase)

Enum of possible cases for the "cases_or_message" oneof.

### [GeneratorName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GeneratorName.ResourceNameType)

The possible contents of [GeneratorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GeneratorName).

### [Handler.HandlerOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Handler.HandlerOneofCase)

Enum of possible cases for the "handler" oneof.

### [ImportEntityTypesRequest.EntityTypesOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ImportEntityTypesRequest.EntityTypesOneofCase)

Enum of possible cases for the "entity_types" oneof.

### [ImportEntityTypesRequest.Types.MergeOption](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ImportEntityTypesRequest.Types.MergeOption)

Merge option when display name conflicts exist during import.

### [ImportFlowRequest.FlowOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ImportFlowRequest.FlowOneofCase)

Enum of possible cases for the "flow" oneof.

### [ImportFlowRequest.Types.ImportOption](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ImportFlowRequest.Types.ImportOption)

Import option.

### [ImportIntentsRequest.IntentsOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ImportIntentsRequest.IntentsOneofCase)

Enum of possible cases for the "intents" oneof.

### [ImportIntentsRequest.Types.MergeOption](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ImportIntentsRequest.Types.MergeOption)

Merge option when display name conflicts exist during import.

### [ImportPlaybookRequest.PlaybookOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ImportPlaybookRequest.PlaybookOneofCase)

Enum of possible cases for the "playbook" oneof.

### [ImportStrategy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ImportStrategy)

Import strategies for the conflict resolution of resources (i.e. intents, entities, and webhooks) with identical display names during import operations.

### [ImportTestCasesRequest.SourceOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ImportTestCasesRequest.SourceOneofCase)

Enum of possible cases for the "source" oneof.

### [InspectTemplateName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.InspectTemplateName.ResourceNameType)

The possible contents of [InspectTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.InspectTemplateName).

### [IntentName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.IntentName.ResourceNameType)

The possible contents of [IntentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.IntentName).

### [IntentView](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.IntentView)

Represents the options for views of an intent. An intent can be a sizable object. Therefore, we provide a resource view that does not return training phrases in the response.

### [KnowledgeConnectorSettings.TargetOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.KnowledgeConnectorSettings.TargetOneofCase)

Enum of possible cases for the "target" oneof.

### [ListTestCasesRequest.Types.TestCaseView](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListTestCasesRequest.Types.TestCaseView)

Specifies how much test case information to include in the response.

### [Match.Types.MatchType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Match.Types.MatchType)

Type of a Match.

### [MatchIntentResponse.QueryOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.MatchIntentResponse.QueryOneofCase)

Enum of possible cases for the "query" oneof.

### [ModelName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ModelName.ResourceNameType)

The possible contents of [ModelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ModelName).

### [NluSettings.Types.ModelTrainingMode](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.NluSettings.Types.ModelTrainingMode)

NLU model training mode.

### [NluSettings.Types.ModelType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.NluSettings.Types.ModelType)

NLU model type.

### [OutputAudioEncoding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.OutputAudioEncoding)

Audio encoding of the output audio format in Text-To-Speech.

### [OutputState](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.OutputState)

Output state.

### [PageInfo.Types.FormInfo.Types.ParameterInfo.Types.ParameterState](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.PageInfo.Types.FormInfo.Types.ParameterInfo.Types.ParameterState)

Represents the state of a parameter.

### [PageName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.PageName.ResourceNameType)

The possible contents of [PageName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.PageName).

### [ParameterDefinition.Types.ParameterType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ParameterDefinition.Types.ParameterType)

Parameter types are used for validation. These types are consistent with [google.protobuf.Value][google.protobuf.Value].

### [Playbook.Types.PlaybookType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Playbook.Types.PlaybookType)

Type of the playbook.

### [Playbook.Types.Step.InstructionOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Playbook.Types.Step.InstructionOneofCase)

Enum of possible cases for the "instruction" oneof.

### [PlaybookName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.PlaybookName.ResourceNameType)

The possible contents of [PlaybookName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.PlaybookName).

### [PlaybookVersionName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.PlaybookVersionName.ResourceNameType)

The possible contents of [PlaybookVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.PlaybookVersionName).

### [QueryInput.InputOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.QueryInput.InputOneofCase)

Enum of possible cases for the "input" oneof.

### [QueryResult.QueryOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.QueryResult.QueryOneofCase)

Enum of possible cases for the "query" oneof.

### [ResponseMessage.MessageOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ResponseMessage.MessageOneofCase)

Enum of possible cases for the "message" oneof.

### [ResponseMessage.Types.MixedAudio.Types.Segment.ContentOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ResponseMessage.Types.MixedAudio.Types.Segment.ContentOneofCase)

Enum of possible cases for the "content" oneof.

### [ResponseMessage.Types.OutputAudioText.SourceOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ResponseMessage.Types.OutputAudioText.SourceOneofCase)

Enum of possible cases for the "source" oneof.

### [ResponseMessage.Types.ResponseType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ResponseMessage.Types.ResponseType)

Represents different response types.

### [ResponseMessage.Types.TelephonyTransferCall.EndpointOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ResponseMessage.Types.TelephonyTransferCall.EndpointOneofCase)

Enum of possible cases for the "endpoint" oneof.

### [RestoreAgentRequest.AgentOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.RestoreAgentRequest.AgentOneofCase)

Enum of possible cases for the "agent" oneof.

### [RestoreAgentRequest.Types.RestoreOption](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.RestoreAgentRequest.Types.RestoreOption)

Restore option.

### [SafetySettings.Types.PhraseMatchStrategy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SafetySettings.Types.PhraseMatchStrategy)

Strategy for matching phrases.

### [SafetySettings.Types.RaiSettings.Types.SafetyCategory](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SafetySettings.Types.RaiSettings.Types.SafetyCategory)

RAI categories to configure.

### [SafetySettings.Types.RaiSettings.Types.SafetyFilterLevel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SafetySettings.Types.RaiSettings.Types.SafetyFilterLevel)

Sensitivity level for RAI categories.

### [SecretVersionName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SecretVersionName.ResourceNameType)

The possible contents of [SecretVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SecretVersionName).

### [SecuritySettings.DataRetentionOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SecuritySettings.DataRetentionOneofCase)

Enum of possible cases for the "data_retention" oneof.

### [SecuritySettings.Types.AudioExportSettings.Types.AudioFormat](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SecuritySettings.Types.AudioExportSettings.Types.AudioFormat)

File format for exported audio file. Currently only in telephony recordings.

### [SecuritySettings.Types.PurgeDataType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SecuritySettings.Types.PurgeDataType)

Type of data we purge after retention settings triggers purge.

### [SecuritySettings.Types.RedactionScope](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SecuritySettings.Types.RedactionScope)

Defines what types of data to redact.

### [SecuritySettings.Types.RedactionStrategy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SecuritySettings.Types.RedactionStrategy)

Defines how we redact data.

### [SecuritySettings.Types.RetentionStrategy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SecuritySettings.Types.RetentionStrategy)

Defines how long we retain persisted data that contains sensitive info.

### [SecuritySettingsName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SecuritySettingsName.ResourceNameType)

The possible contents of [SecuritySettingsName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SecuritySettingsName).

### [ServiceName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ServiceName.ResourceNameType)

The possible contents of [ServiceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ServiceName).

### [SessionEntityType.Types.EntityOverrideMode](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SessionEntityType.Types.EntityOverrideMode)

The types of modifications for the session entity type.

### [SessionEntityTypeName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SessionEntityTypeName.ResourceNameType)

The possible contents of [SessionEntityTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SessionEntityTypeName).

### [SessionName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SessionName.ResourceNameType)

The possible contents of [SessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SessionName).

### [SpeechModelVariant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SpeechModelVariant)

Variant of the specified [Speech model][google.cloud.dialogflow.cx.v3.InputAudioConfig.model] to use.

See the [Cloud Speech documentation](https://cloud.google.com/speech-to-text/docs/enhanced-models) for which models have different variants. For example, the "phone_call" model has both a standard and an enhanced variant. When you use an enhanced model, you will generally receive higher quality results than for a standard model.

### [SsmlVoiceGender](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SsmlVoiceGender)

Gender of the voice as described in [SSML voice element](https://www.w3.org/TR/speech-synthesis11/#edef_voice).

### [StreamingDetectIntentResponse.ResponseOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.StreamingDetectIntentResponse.ResponseOneofCase)

Enum of possible cases for the "response" oneof.

### [StreamingRecognitionResult.Types.MessageType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.StreamingRecognitionResult.Types.MessageType)

Type of the response message.

### [TestCaseName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.TestCaseName.ResourceNameType)

The possible contents of [TestCaseName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.TestCaseName).

### [TestCaseResultName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.TestCaseResultName.ResourceNameType)

The possible contents of [TestCaseResultName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.TestCaseResultName).

### [TestResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.TestResult)

The test result for a test case and an agent environment.

### [TestRunDifference.Types.DiffType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.TestRunDifference.Types.DiffType)

What part of the message replay differs from the test case.

### [Tool.SpecificationOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Tool.SpecificationOneofCase)

Enum of possible cases for the "specification" oneof.

### [Tool.Types.Authentication.AuthConfigOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Tool.Types.Authentication.AuthConfigOneofCase)

Enum of possible cases for the "auth_config" oneof.

### [Tool.Types.Authentication.Types.OAuthConfig.Types.OauthGrantType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Tool.Types.Authentication.Types.OAuthConfig.Types.OauthGrantType)

OAuth grant types. Only [client credential grant](https://oauth.net/2/grant-types/client-credentials) is supported.

### [Tool.Types.Authentication.Types.RequestLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Tool.Types.Authentication.Types.RequestLocation)

The location of the API key in the request.

### [Tool.Types.Authentication.Types.ServiceAgentAuthConfig.Types.ServiceAgentAuth](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Tool.Types.Authentication.Types.ServiceAgentAuthConfig.Types.ServiceAgentAuth)

Indicate the auth token type generated from the [Diglogflow service agent](https://cloud.google.com/iam/docs/service-agents#dialogflow-service-agent).

### [Tool.Types.OpenApiTool.SchemaOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Tool.Types.OpenApiTool.SchemaOneofCase)

Enum of possible cases for the "schema" oneof.

### [Tool.Types.ToolType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Tool.Types.ToolType)

Represents the type of the tool.

### [ToolCallResult.ResultOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ToolCallResult.ResultOneofCase)

Enum of possible cases for the "result" oneof.

### [ToolName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ToolName.ResourceNameType)

The possible contents of [ToolName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ToolName).

### [ToolVersionName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ToolVersionName.ResourceNameType)

The possible contents of [ToolVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ToolVersionName).

### [TraceBlock.TraceMetadataOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.TraceBlock.TraceMetadataOneofCase)

Enum of possible cases for the "trace_metadata" oneof.

### [TransitionCoverage.Types.Transition.DetailOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.TransitionCoverage.Types.Transition.DetailOneofCase)

Enum of possible cases for the "detail" oneof.

### [TransitionCoverage.Types.TransitionNode.KindOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.TransitionCoverage.Types.TransitionNode.KindOneofCase)

Enum of possible cases for the "kind" oneof.

### [TransitionRoute.TargetOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.TransitionRoute.TargetOneofCase)

Enum of possible cases for the "target" oneof.

### [TransitionRouteGroupName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.TransitionRouteGroupName.ResourceNameType)

The possible contents of [TransitionRouteGroupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.TransitionRouteGroupName).

### [TypeSchema.SchemaOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.TypeSchema.SchemaOneofCase)

Enum of possible cases for the "schema" oneof.

### [ValidationMessage.Types.ResourceType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ValidationMessage.Types.ResourceType)

Resource types.

### [ValidationMessage.Types.Severity](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ValidationMessage.Types.Severity)

Severity level.

### [VariantsHistory.VariantsOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.VariantsHistory.VariantsOneofCase)

Enum of possible cases for the "variants" oneof.

### [Version.Types.State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Version.Types.State)

The state of the version.

### [VersionName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.VersionName.ResourceNameType)

The possible contents of [VersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.VersionName).

### [Webhook.Types.GenericWebService.Types.HttpMethod](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Webhook.Types.GenericWebService.Types.HttpMethod)

HTTP method to use when calling webhooks.

### [Webhook.Types.GenericWebService.Types.ServiceAgentAuth](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Webhook.Types.GenericWebService.Types.ServiceAgentAuth)

Indicate the auth token type generated from the [Diglogflow service agent](https://cloud.google.com/iam/docs/service-agents#dialogflow-service-agent).

### [Webhook.Types.GenericWebService.Types.WebhookType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Webhook.Types.GenericWebService.Types.WebhookType)

Represents the type of webhook configuration.

### [Webhook.WebhookOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Webhook.WebhookOneofCase)

Enum of possible cases for the "webhook" oneof.

### [WebhookName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.WebhookName.ResourceNameType)

The possible contents of [WebhookName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.WebhookName).

### [WebhookRequest.QueryOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.WebhookRequest.QueryOneofCase)

Enum of possible cases for the "query" oneof.

### [WebhookResponse.TransitionOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.WebhookResponse.TransitionOneofCase)

Enum of possible cases for the "transition" oneof.

### [WebhookResponse.Types.FulfillmentResponse.Types.MergeBehavior](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.WebhookResponse.Types.FulfillmentResponse.Types.MergeBehavior)

Defines merge behavior for `messages`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
