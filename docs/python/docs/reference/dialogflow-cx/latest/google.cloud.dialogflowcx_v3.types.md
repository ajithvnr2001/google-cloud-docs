---
url: https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types
title: Package types (2.8.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:48:58.565924+00:00
---

# Package types (2.8.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package types (2.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.8.0 (latest)  2.7.0  2.6.0  2.1.0  2.0.0  1.43.0  1.42.0  1.41.1  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.1  1.33.0  1.32.1  1.31.1  1.30.1  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.1  1.22.0  1.21.0  1.20.1  1.19.0  1.18.0  1.17.1  1.16.0  1.15.0  1.14.1  1.13.5  1.12.1  1.11.0  1.10.0  1.9.1  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.2  1.2.0  1.1.1  1.0.0  0.8.2  0.7.1  0.6.0  0.5.0  0.4.1  0.3.0  0.2.0  0.1.1 

API documentation for `dialogflowcx_v3.types` package.

## Classes 

### [Action](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.Action)

Action performed by end user or Dialogflow agent in the conversation.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AdvancedSettings](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.AdvancedSettings)

Hierarchical advanced settings for agent/flow/page/fulfillment/parameter. Settings exposed at lower level overrides the settings exposed at higher level. Overriding occurs at the sub-setting level. For example, the playback_interruption_settings at fulfillment level only overrides the playback_interruption_settings at the agent level, leaving other settings at the agent level unchanged.

DTMF settings does not override each other. DTMF settings set at different levels define DTMF detections running in parallel.

Hierarchy: Agent->Flow->Page->Fulfillment/Parameter.

### [Agent](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.Agent)

Agents are best described as Natural Language Understanding (NLU) modules that transform user requests into actionable data. You can include agents in your app, product, or service to determine user intent and respond to the user in a natural way.

After you create an agent, you can add Intents, [Entity Types][google.cloud.dialogflow.cx.v3.EntityType], Flows, Fulfillments, Webhooks, TransitionRouteGroups and so on to manage the conversation flows.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AgentUtterance](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.AgentUtterance)

AgentUtterance represents one message sent by the agent.

### [AgentValidationResult](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.AgentValidationResult)

The response message for Agents.GetAgentValidationResult.

### [AnswerFeedback](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.AnswerFeedback)

Stores information about feedback provided by users about a response.

### [AudioEncoding](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.AudioEncoding)

Audio encoding of the audio content sent in the conversational query request. Refer to the `Cloud Speech API documentation <https://cloud.google.com/speech-to-text/docs/basics>`__ for more details.

### [AudioInput](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.AudioInput)

Represents the natural speech audio to be processed.

### [BargeInConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.BargeInConfig)

Configuration of the barge-in behavior. Barge-in instructs the API to return a detected utterance at a proper time while the client is playing back the response audio from a previous request. When the client sees the utterance, it should stop the playback and immediately get ready for receiving the responses for the current request.

The barge-in handling requires the client to start streaming audio input as soon as it starts playing back the audio from the previous response. The playback is modeled into two phases:

  * No barge-in phase: which goes first and during which speech detection should not be carried out.

  * Barge-in phase: which follows the no barge-in phase and during which the API starts speech detection and may inform the client that an utterance has been detected. Note that no-speech event is not expected in this phase.




The client provides this configuration in terms of the durations of those two phases. The durations are measured in terms of the audio length from the start of the input audio.

No-speech event is a response with END_OF_UTTERANCE without any transcript following up.

### [BatchDeleteTestCasesRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.BatchDeleteTestCasesRequest)

The request message for TestCases.BatchDeleteTestCases.

### [BatchRunTestCasesMetadata](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.BatchRunTestCasesMetadata)

Metadata returned for the TestCases.BatchRunTestCases long running operation.

### [BatchRunTestCasesRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.BatchRunTestCasesRequest)

The request message for TestCases.BatchRunTestCases.

### [BatchRunTestCasesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.BatchRunTestCasesResponse)

The response message for TestCases.BatchRunTestCases.

### [BoostSpec](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.BoostSpec)

Boost specification to boost certain documents. A copy of google.cloud.discoveryengine.v1main.BoostSpec, field documentation is available at <https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/BoostSpec>

### [BoostSpecs](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.BoostSpecs)

Boost specifications for data stores.

### [CalculateCoverageRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.CalculateCoverageRequest)

The request message for TestCases.CalculateCoverage.

### [CalculateCoverageResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.CalculateCoverageResponse)

The response message for TestCases.CalculateCoverage.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Changelog](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.Changelog)

Changelogs represents a change made to a given agent.

### [CloudConversationDebuggingInfo](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.CloudConversationDebuggingInfo)

Cloud conversation info for easier debugging. It will get populated in `StreamingDetectIntentResponse` or `StreamingAnalyzeContentResponse` when the flag `enable_debugging_info` is set to true in corresponding requests.

### [CodeBlock](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.CodeBlock)

Represents a code block.

### [CompareVersionsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.CompareVersionsRequest)

The request message for Versions.CompareVersions.

### [CompareVersionsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.CompareVersionsResponse)

The response message for Versions.CompareVersions.

### [ContinuousTestResult](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ContinuousTestResult)

Represents a result from running a test case in an agent environment.

### [ConversationTurn](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ConversationTurn)

One interaction between a human and virtual agent. The human provides some input and the virtual agent provides a response.

### [CreateAgentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.CreateAgentRequest)

The request message for Agents.CreateAgent.

### [CreateEntityTypeRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.CreateEntityTypeRequest)

The request message for EntityTypes.CreateEntityType.

### [CreateEnvironmentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.CreateEnvironmentRequest)

The request message for Environments.CreateEnvironment.

### [CreateExampleRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.CreateExampleRequest)

The request message for Examples.CreateExample.

### [CreateExperimentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.CreateExperimentRequest)

The request message for Experiments.CreateExperiment.

### [CreateFlowRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.CreateFlowRequest)

The request message for Flows.CreateFlow.

### [CreateGeneratorRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.CreateGeneratorRequest)

The request message for Generators.CreateGenerator.

### [CreateIntentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.CreateIntentRequest)

The request message for Intents.CreateIntent.

### [CreatePageRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.CreatePageRequest)

The request message for Pages.CreatePage.

### [CreatePlaybookRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.CreatePlaybookRequest)

The request message for Playbooks.CreatePlaybook.

### [CreatePlaybookVersionRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.CreatePlaybookVersionRequest)

The request message for Playbooks.CreatePlaybookVersion.

### [CreateSecuritySettingsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.CreateSecuritySettingsRequest)

The request message for [SecuritySettings.CreateSecuritySettings][].

### [CreateSessionEntityTypeRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.CreateSessionEntityTypeRequest)

The request message for SessionEntityTypes.CreateSessionEntityType.

### [CreateTestCaseRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.CreateTestCaseRequest)

The request message for TestCases.CreateTestCase.

### [CreateToolRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.CreateToolRequest)

The request message for Tools.CreateTool.

### [CreateToolVersionRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.CreateToolVersionRequest)

The request message for Tools.CreateToolVersion. The request message for Tools.CreateToolVersion.

### [CreateTransitionRouteGroupRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.CreateTransitionRouteGroupRequest)

The request message for TransitionRouteGroups.CreateTransitionRouteGroup.

### [CreateVersionOperationMetadata](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.CreateVersionOperationMetadata)

Metadata associated with the long running operation for Versions.CreateVersion.

### [CreateVersionRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.CreateVersionRequest)

The request message for Versions.CreateVersion.

### [CreateWebhookRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.CreateWebhookRequest)

The request message for Webhooks.CreateWebhook.

### [DataStoreConnection](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.DataStoreConnection)

A data store connection. It represents a data store in Discovery Engine and the type of the contents it contains.

### [DataStoreConnectionSignals](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.DataStoreConnectionSignals)

Data store connection feature output signals. Might be only partially field if processing stop before the final answer. Reasons for this can be, but are not limited to: empty UCS search results, positive RAI check outcome, grounding failure, ...

### [DataStoreType](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.DataStoreType)

Type of a data store. Determines how search is performed in the data store.

### [DataType](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.DataType)

Defines data types that are supported for inlined schemas. These types are consistent with `google.protobuf.Value][google.protobuf.Value]`.

### [DeleteAgentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.DeleteAgentRequest)

The request message for Agents.DeleteAgent.

### [DeleteEntityTypeRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.DeleteEntityTypeRequest)

The request message for EntityTypes.DeleteEntityType.

### [DeleteEnvironmentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.DeleteEnvironmentRequest)

The request message for Environments.DeleteEnvironment.

### [DeleteExampleRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.DeleteExampleRequest)

The request message for Examples.DeleteExample.

### [DeleteExperimentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.DeleteExperimentRequest)

The request message for Experiments.DeleteExperiment.

### [DeleteFlowRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.DeleteFlowRequest)

The request message for Flows.DeleteFlow.

### [DeleteGeneratorRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.DeleteGeneratorRequest)

The request message for Generators.DeleteGenerator.

### [DeleteIntentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.DeleteIntentRequest)

The request message for Intents.DeleteIntent.

### [DeletePageRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.DeletePageRequest)

The request message for Pages.DeletePage.

### [DeletePlaybookRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.DeletePlaybookRequest)

The request message for Playbooks.DeletePlaybook.

### [DeletePlaybookVersionRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.DeletePlaybookVersionRequest)

The request message for Playbooks.DeletePlaybookVersion.

### [DeleteSecuritySettingsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.DeleteSecuritySettingsRequest)

The request message for [SecuritySettings.DeleteSecuritySettings][].

### [DeleteSessionEntityTypeRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.DeleteSessionEntityTypeRequest)

The request message for SessionEntityTypes.DeleteSessionEntityType.

### [DeleteToolRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.DeleteToolRequest)

The request message for Tools.DeleteTool.

### [DeleteToolVersionRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.DeleteToolVersionRequest)

The request message for Tools.DeleteToolVersion.

### [DeleteTransitionRouteGroupRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.DeleteTransitionRouteGroupRequest)

The request message for TransitionRouteGroups.DeleteTransitionRouteGroup.

### [DeleteVersionRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.DeleteVersionRequest)

The request message for Versions.DeleteVersion.

### [DeleteWebhookRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.DeleteWebhookRequest)

The request message for Webhooks.DeleteWebhook.

### [DeployFlowMetadata](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.DeployFlowMetadata)

Metadata returned for the Environments.DeployFlow long running operation.

### [DeployFlowRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.DeployFlowRequest)

The request message for Environments.DeployFlow.

### [DeployFlowResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.DeployFlowResponse)

The response message for Environments.DeployFlow.

### [Deployment](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.Deployment)

Represents a deployment in an environment. A deployment happens when a flow version configured to be active in the environment. You can configure running pre-deployment steps, e.g. running validation test cases, experiment auto-rollout, etc.

### [DetectIntentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.DetectIntentRequest)

The request to detect user's intent.

### [DetectIntentResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.DetectIntentResponse)

The message returned from the DetectIntent method.

### [DetectIntentResponseView](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.DetectIntentResponseView)

The response view specifies which fields in the QueryResult to return.
    
    
        <xref uid="google.cloud.dialogflow.cx.v3.QueryResult.diagnostic_info">QueryResult.diagnostic_info</xref>
    
        - [QueryResult.generative_info][]
        -
    
        <xref uid="google.cloud.dialogflow.cx.v3.QueryResult.trace_blocks">QueryResult.trace_blocks</xref>
        ----------------------------------------------------------------------------------
    
        <xref uid="google.cloud.dialogflow.cx.v3.QueryResult.data_store_connection_signals">QueryResult.data_store_connection_signals</xref>
    DETECT_INTENT_RESPONSE_VIEW_DEFAULT (3):
        Default response view omits the following fields:
        -------------------------------------------------
    
        <xref uid="google.cloud.dialogflow.cx.v3.QueryResult.trace_blocks">QueryResult.trace_blocks</xref>
    

### [DocumentProcessingMode](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.DocumentProcessingMode)

The document processing mode of the data store.

### [DtmfInput](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.DtmfInput)

Represents the input for dtmf event.

### [EntityType](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.EntityType)

Entities are extracted from user input and represent parameters that are meaningful to your application. For example, a date range, a proper name such as a geographic location or landmark, and so on. Entities represent actionable data for your application.

When you define an entity, you can also include synonyms that all map to that entity. For example, "soft drink", "soda", "pop", and so on.

There are three types of entities:

  * **System** \- entities that are defined by the Dialogflow API for common data types such as date, time, currency, and so on. A system entity is represented by the `EntityType` type.

  * **Custom** \- entities that are defined by you that represent actionable data that is meaningful to your application. For example, you could define a `pizza.sauce` entity for red or white pizza sauce, a `pizza.cheese` entity for the different types of cheese on a pizza, a `pizza.topping` entity for different toppings, and so on. A custom entity is represented by the `EntityType` type.

  * **User** \- entities that are built for an individual user such as favorites, preferences, playlists, and so on. A user entity is represented by the SessionEntityType type.




For more information about entity types, see the `Dialogflow documentation <https://cloud.google.com/dialogflow/docs/entities-overview>`__.

### [Environment](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.Environment)

Represents an environment for an agent. You can create multiple versions of your agent and publish them to separate environments. When you edit an agent, you are editing the draft agent. At any point, you can save the draft agent as an agent version, which is an immutable snapshot of your agent. When you save the draft agent, it is published to the default environment. When you create agent versions, you can publish them to custom environments. You can create a variety of custom environments for testing, development, production, etc.

### [EventHandler](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.EventHandler)

An event handler specifies an event that can be handled during a session. When the specified event happens, the following actions are taken in order:

  * If there is a [`trigger_fulfillment`][google.cloud.dialogflow.cx.v3.EventHandler.trigger_fulfillment] associated with the event, it will be called.
  * If there is a [`target_page`][google.cloud.dialogflow.cx.v3.EventHandler.target_page] associated with the event, the session will transition into the specified page.
  * If there is a [`target_flow`][google.cloud.dialogflow.cx.v3.EventHandler.target_flow] associated with the event, the session will transition into the specified flow.



This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [EventInput](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.EventInput)

Represents the event to trigger.

### [Example](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.Example)

Example represents a sample execution of the playbook in the conversation. An example consists of a list of ordered actions performed by end user or Dialogflow agent according the playbook instructions to fulfill the task.

### [Experiment](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.Experiment)

Represents an experiment in an environment.

### [ExportAgentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ExportAgentRequest)

The request message for Agents.ExportAgent.

### [ExportAgentResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ExportAgentResponse)

The response message for Agents.ExportAgent.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ExportEntityTypesMetadata](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ExportEntityTypesMetadata)

Metadata returned for the EntityTypes.ExportEntityTypes long running operation.

### [ExportEntityTypesRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ExportEntityTypesRequest)

The request message for EntityTypes.ExportEntityTypes.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ExportEntityTypesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ExportEntityTypesResponse)

The response message for EntityTypes.ExportEntityTypes.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ExportFlowRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ExportFlowRequest)

The request message for Flows.ExportFlow.

### [ExportFlowResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ExportFlowResponse)

The response message for Flows.ExportFlow.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ExportIntentsMetadata](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ExportIntentsMetadata)

Metadata returned for the Intents.ExportIntents long running operation.

### [ExportIntentsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ExportIntentsRequest)

The request message for Intents.ExportIntents.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ExportIntentsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ExportIntentsResponse)

The response message for Intents.ExportIntents.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ExportPlaybookRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ExportPlaybookRequest)

The request message for Playbooks.ExportPlaybook.

### [ExportPlaybookResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ExportPlaybookResponse)

The response message for Playbooks.ExportPlaybook.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ExportTestCasesMetadata](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ExportTestCasesMetadata)

Metadata returned for the TestCases.ExportTestCases long running operation. This message currently has no fields.

### [ExportTestCasesRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ExportTestCasesRequest)

The request message for TestCases.ExportTestCases.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ExportTestCasesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ExportTestCasesResponse)

The response message for TestCases.ExportTestCases.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [FilterSpecs](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.FilterSpecs)

Filter specifications for data stores.

### [Flow](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.Flow)

Flows represents the conversation flows when you build your chatbot agent. A flow consists of many pages connected by the transition routes. Conversations always start with the built-in Start Flow (with an all-0 ID). Transition routes can direct the conversation session from the current flow (parent flow) to another flow (sub flow). When the sub flow is finished, Dialogflow will bring the session back to the parent flow, where the sub flow is started.

Usually, when a transition route is followed by a matched intent, the intent will be "consumed". This means the intent won't activate more transition routes. However, when the followed transition route moves the conversation session into a different flow, the matched intent can be carried over and to be consumed in the target flow.

### [FlowImportStrategy](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.FlowImportStrategy)

The flow import strategy used for resource conflict resolution associated with an ImportFlowRequest.

### [FlowInvocation](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.FlowInvocation)

Stores metadata of the invocation of a CX flow.

### [FlowTraceMetadata](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.FlowTraceMetadata)

Metadata of the flow trace.

### [FlowTransition](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.FlowTransition)

Stores metadata of the transition to a target CX flow. Flow transition actions exit the caller playbook and enter the child flow.

### [FlowValidationResult](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.FlowValidationResult)

The response message for Flows.GetFlowValidationResult.

### [Form](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.Form)

A form is a data model that groups related parameters that can be collected from the user. The process in which the agent prompts the user and collects parameter values from the user is called form filling. A form can be added to a page. When form filling is done, the filled parameters will be written to the session.

### [FulfillIntentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.FulfillIntentRequest)

Request of [FulfillIntent][]

### [FulfillIntentResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.FulfillIntentResponse)

Response of [FulfillIntent][]

### [Fulfillment](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.Fulfillment)

A fulfillment can do one or more of the following actions at the same time:

  * Generate rich message responses.
  * Set parameter values.
  * Call the webhook.



Fulfillments can be called at various stages in the Page or Form lifecycle. For example, when a DetectIntentRequest drives a session to enter a new page, the page's entry fulfillment can add a static response to the QueryResult in the returning DetectIntentResponse, call the webhook (for example, to load user data from a database), or both.

### [GcsDestination](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.GcsDestination)

Google Cloud Storage location for a Dialogflow operation that writes or exports objects (e.g. exported agent or transcripts) outside of Dialogflow.

### [GenerativeSettings](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.GenerativeSettings)

Settings for Generative AI.

### [Generator](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.Generator)

Generators contain prompt to be sent to the LLM model to generate text. The prompt can contain parameters which will be resolved before calling the model. It can optionally contain banned phrases to ensure the model responses are safe.

### [GetAgentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.GetAgentRequest)

The request message for Agents.GetAgent.

### [GetAgentValidationResultRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.GetAgentValidationResultRequest)

The request message for Agents.GetAgentValidationResult.

### [GetChangelogRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.GetChangelogRequest)

The request message for Changelogs.GetChangelog.

### [GetDeploymentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.GetDeploymentRequest)

The request message for Deployments.GetDeployment.

### [GetEntityTypeRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.GetEntityTypeRequest)

The request message for EntityTypes.GetEntityType.

### [GetEnvironmentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.GetEnvironmentRequest)

The request message for Environments.GetEnvironment.

### [GetExampleRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.GetExampleRequest)

The request message for Examples.GetExample.

### [GetExperimentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.GetExperimentRequest)

The request message for Experiments.GetExperiment.

### [GetFlowRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.GetFlowRequest)

The response message for Flows.GetFlow.

### [GetFlowValidationResultRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.GetFlowValidationResultRequest)

The request message for Flows.GetFlowValidationResult.

### [GetGenerativeSettingsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.GetGenerativeSettingsRequest)

Request for GetGenerativeSettings RPC.

### [GetGeneratorRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.GetGeneratorRequest)

The request message for Generators.GetGenerator.

### [GetIntentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.GetIntentRequest)

The request message for Intents.GetIntent.

### [GetPageRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.GetPageRequest)

The request message for Pages.GetPage.

### [GetPlaybookRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.GetPlaybookRequest)

The request message for Playbooks.GetPlaybook.

### [GetPlaybookVersionRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.GetPlaybookVersionRequest)

The request message for Playbooks.GetPlaybookVersion.

### [GetSecuritySettingsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.GetSecuritySettingsRequest)

The request message for SecuritySettingsService.GetSecuritySettings.

### [GetSessionEntityTypeRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.GetSessionEntityTypeRequest)

The request message for SessionEntityTypes.GetSessionEntityType.

### [GetTestCaseRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.GetTestCaseRequest)

The request message for TestCases.GetTestCase.

### [GetTestCaseResultRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.GetTestCaseResultRequest)

The request message for TestCases.GetTestCaseResult.

### [GetToolRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.GetToolRequest)

The request message for Tools.GetTool.

### [GetToolVersionRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.GetToolVersionRequest)

The request message for Tools.GetToolVersion.

### [GetTransitionRouteGroupRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.GetTransitionRouteGroupRequest)

The request message for TransitionRouteGroups.GetTransitionRouteGroup.

### [GetVersionRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.GetVersionRequest)

The request message for Versions.GetVersion.

### [GetWebhookRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.GetWebhookRequest)

The request message for Webhooks.GetWebhook.

### [Handler](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.Handler)

Handler can be used to define custom logic to be executed based on the user-specified triggers.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ImportEntityTypesMetadata](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ImportEntityTypesMetadata)

Metadata returned for the EntityTypes.ImportEntityTypes long running operation.

### [ImportEntityTypesRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ImportEntityTypesRequest)

The request message for EntityTypes.ImportEntityTypes.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ImportEntityTypesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ImportEntityTypesResponse)

The response message for EntityTypes.ImportEntityTypes.

### [ImportFlowRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ImportFlowRequest)

The request message for Flows.ImportFlow.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ImportFlowResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ImportFlowResponse)

The response message for Flows.ImportFlow.

### [ImportIntentsMetadata](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ImportIntentsMetadata)

Metadata returned for the Intents.ImportIntents long running operation.

### [ImportIntentsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ImportIntentsRequest)

The request message for Intents.ImportIntents.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ImportIntentsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ImportIntentsResponse)

The response message for Intents.ImportIntents.

### [ImportPlaybookRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ImportPlaybookRequest)

The request message for Playbooks.ImportPlaybook.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ImportPlaybookResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ImportPlaybookResponse)

The response message for Playbooks.ImportPlaybook.

### [ImportStrategy](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ImportStrategy)

Import strategies for the conflict resolution of resources (i.e. intents, entities, and webhooks) with identical display names during import operations.

### [ImportTestCasesMetadata](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ImportTestCasesMetadata)

Metadata returned for the TestCases.ImportTestCases long running operation.

### [ImportTestCasesRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ImportTestCasesRequest)

The request message for TestCases.ImportTestCases.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ImportTestCasesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ImportTestCasesResponse)

The response message for TestCases.ImportTestCases.

### [InlineDestination](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.InlineDestination)

Inline destination for a Dialogflow operation that writes or exports objects (e.g. intents) outside of Dialogflow.

### [InlineSchema](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.InlineSchema)

A type schema object that's specified inline.

### [InlineSource](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.InlineSource)

Inline source for a Dialogflow operation that reads or imports objects (e.g. intents) into Dialogflow.

### [InputAudioConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.InputAudioConfig)

Instructs the speech recognizer on how to process the audio content.

### [Intent](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.Intent)

An intent represents a user's intent to interact with a conversational agent. You can provide information for the Dialogflow API to use to match user input to an intent by adding training phrases (i.e., examples of user input) to your intent.

### [IntentCoverage](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.IntentCoverage)

Intent coverage represents the percentage of all possible intents in the agent that are triggered in any of a parent's test cases.

### [IntentInput](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.IntentInput)

Represents the intent to trigger programmatically rather than as a result of natural language processing.

### [IntentView](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.IntentView)

Represents the options for views of an intent. An intent can be a sizable object. Therefore, we provide a resource view that does not return training phrases in the response.

### [KnowledgeConnectorSettings](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.KnowledgeConnectorSettings)

The Knowledge Connector settings for this page or flow. This includes information such as the attached Knowledge Bases, and the way to execute fulfillment.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [LanguageInfo](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.LanguageInfo)

Represents the language information of the request.

### [ListAgentsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ListAgentsRequest)

The request message for Agents.ListAgents.

### [ListAgentsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ListAgentsResponse)

The response message for Agents.ListAgents.

### [ListChangelogsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ListChangelogsRequest)

The request message for Changelogs.ListChangelogs.

### [ListChangelogsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ListChangelogsResponse)

The response message for Changelogs.ListChangelogs.

### [ListContinuousTestResultsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ListContinuousTestResultsRequest)

The request message for Environments.ListContinuousTestResults.

### [ListContinuousTestResultsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ListContinuousTestResultsResponse)

The response message for [Environments.ListTestCaseResults][].

### [ListDeploymentsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ListDeploymentsRequest)

The request message for Deployments.ListDeployments.

### [ListDeploymentsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ListDeploymentsResponse)

The response message for Deployments.ListDeployments.

### [ListEntityTypesRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ListEntityTypesRequest)

The request message for EntityTypes.ListEntityTypes.

### [ListEntityTypesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ListEntityTypesResponse)

The response message for EntityTypes.ListEntityTypes.

### [ListEnvironmentsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ListEnvironmentsRequest)

The request message for Environments.ListEnvironments.

### [ListEnvironmentsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ListEnvironmentsResponse)

The response message for Environments.ListEnvironments.

### [ListExamplesRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ListExamplesRequest)

The request message for Examples.ListExamples.

### [ListExamplesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ListExamplesResponse)

The response message for Examples.ListExamples.

### [ListExperimentsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ListExperimentsRequest)

The request message for Experiments.ListExperiments.

### [ListExperimentsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ListExperimentsResponse)

The response message for Experiments.ListExperiments.

### [ListFlowsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ListFlowsRequest)

The request message for Flows.ListFlows.

### [ListFlowsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ListFlowsResponse)

The response message for Flows.ListFlows.

### [ListGeneratorsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ListGeneratorsRequest)

The request message for Generators.ListGenerators.

### [ListGeneratorsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ListGeneratorsResponse)

The response message for Generators.ListGenerators.

### [ListIntentsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ListIntentsRequest)

The request message for Intents.ListIntents.

### [ListIntentsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ListIntentsResponse)

The response message for Intents.ListIntents.

### [ListPagesRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ListPagesRequest)

The request message for Pages.ListPages.

### [ListPagesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ListPagesResponse)

The response message for Pages.ListPages.

### [ListPlaybookVersionsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ListPlaybookVersionsRequest)

The request message for Playbooks.ListPlaybookVersions.

### [ListPlaybookVersionsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ListPlaybookVersionsResponse)

The response message for Playbooks.ListPlaybookVersions.

### [ListPlaybooksRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ListPlaybooksRequest)

The request message for Playbooks.ListPlaybooks.

### [ListPlaybooksResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ListPlaybooksResponse)

The response message for Playbooks.ListPlaybooks.

### [ListSecuritySettingsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ListSecuritySettingsRequest)

The request message for [SecuritySettings.ListSecuritySettings][].

### [ListSecuritySettingsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ListSecuritySettingsResponse)

The response message for [SecuritySettings.ListSecuritySettings][].

### [ListSessionEntityTypesRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ListSessionEntityTypesRequest)

The request message for SessionEntityTypes.ListSessionEntityTypes.

### [ListSessionEntityTypesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ListSessionEntityTypesResponse)

The response message for SessionEntityTypes.ListSessionEntityTypes.

### [ListTestCaseResultsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ListTestCaseResultsRequest)

The request message for TestCases.ListTestCaseResults.

### [ListTestCaseResultsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ListTestCaseResultsResponse)

The response message for TestCases.ListTestCaseResults.

### [ListTestCasesRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ListTestCasesRequest)

The request message for TestCases.ListTestCases.

### [ListTestCasesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ListTestCasesResponse)

The response message for TestCases.ListTestCases.

### [ListToolVersionsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ListToolVersionsRequest)

The request message for Tools.ListToolVersions.

### [ListToolVersionsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ListToolVersionsResponse)

The response message for Tools.ListToolVersions.

### [ListToolsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ListToolsRequest)

The request message for Tools.ListTools.

### [ListToolsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ListToolsResponse)

The response message for Tools.ListTools.

### [ListTransitionRouteGroupsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ListTransitionRouteGroupsRequest)

The request message for TransitionRouteGroups.ListTransitionRouteGroups.

### [ListTransitionRouteGroupsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ListTransitionRouteGroupsResponse)

The response message for TransitionRouteGroups.ListTransitionRouteGroups.

### [ListVersionsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ListVersionsRequest)

The request message for Versions.ListVersions.

### [ListVersionsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ListVersionsResponse)

The response message for Versions.ListVersions.

### [ListWebhooksRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ListWebhooksRequest)

The request message for Webhooks.ListWebhooks.

### [ListWebhooksResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ListWebhooksResponse)

The response message for Webhooks.ListWebhooks.

### [LlmModelSettings](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.LlmModelSettings)

Settings for LLM models.

### [LoadVersionRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.LoadVersionRequest)

The request message for Versions.LoadVersion.

### [LookupEnvironmentHistoryRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.LookupEnvironmentHistoryRequest)

The request message for Environments.LookupEnvironmentHistory.

### [LookupEnvironmentHistoryResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.LookupEnvironmentHistoryResponse)

The response message for Environments.LookupEnvironmentHistory.

### [Match](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.Match)

Represents one match result of [MatchIntent][].

### [MatchIntentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.MatchIntentRequest)

Request of [MatchIntent][].

### [MatchIntentResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.MatchIntentResponse)

Response of [MatchIntent][].

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [NluSettings](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.NluSettings)

Settings related to NLU.

### [OutputAudioConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.OutputAudioConfig)

Instructs the speech synthesizer how to generate the output audio content.

### [OutputAudioEncoding](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.OutputAudioEncoding)

Audio encoding of the output audio format in Text-To-Speech.

### [OutputState](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.OutputState)

Output state.

### [Page](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.Page)

A Dialogflow CX conversation (session) can be described and visualized as a state machine. The states of a CX session are represented by pages.

For each flow, you define many pages, where your combined pages can handle a complete conversation on the topics the flow is designed for. At any given moment, exactly one page is the current page, the current page is considered active, and the flow associated with that page is considered active. Every flow has a special start page. When a flow initially becomes active, the start page page becomes the current page. For each conversational turn, the current page will either stay the same or transition to another page.

You configure each page to collect information from the end-user that is relevant for the conversational state represented by the page.

For more information, see the `Page guide <https://cloud.google.com/dialogflow/cx/docs/concept/page>`__.

### [PageInfo](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.PageInfo)

Represents page information communicated to and from the webhook.

### [ParameterDefinition](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ParameterDefinition)

Defines the properties of a parameter. Used to define parameters used in the agent and the input / output parameters for each fulfillment.

### [Phrase](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.Phrase)

Text input which can be used for prompt or banned phrases.

### [Playbook](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.Playbook)

Playbook is the basic building block to instruct the LLM how to execute a certain task.

A playbook consists of a goal to accomplish, an optional list of step by step instructions (the step instruction may refers to name of the custom or default plugin tools to use) to perform the task, a list of contextual input data to be passed in at the beginning of the invoked, and a list of output parameters to store the playbook result.

### [PlaybookImportStrategy](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.PlaybookImportStrategy)

The playbook import strategy used for resource conflict resolution associated with an ImportPlaybookRequest.

### [PlaybookInput](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.PlaybookInput)

Input of the playbook.

### [PlaybookInvocation](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.PlaybookInvocation)

Stores metadata of the invocation of a child playbook.

### [PlaybookOutput](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.PlaybookOutput)

Output of the playbook.

### [PlaybookTraceMetadata](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.PlaybookTraceMetadata)

Metadata of the playbook trace.

### [PlaybookTransition](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.PlaybookTransition)

Stores metadata of the transition to another target playbook. Playbook transition actions exit the caller playbook and enter the target playbook.

### [PlaybookVersion](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.PlaybookVersion)

Playbook version is a snapshot of the playbook at certain timestamp.

### [QueryInput](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.QueryInput)

Represents the query input. It can contain one of:

  1. A conversational query in the form of text.

  2. An intent query that specifies which intent to trigger.

  3. Natural language speech audio to be processed.

  4. An event to be triggered.

  5. DTMF digits to invoke an intent and fill in parameter value.

  6. The results of a tool executed by the client.




This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [QueryParameters](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.QueryParameters)

Represents the parameters of a conversational query.

### [QueryResult](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.QueryResult)

Represents the result of a conversational query.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ResourceName](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ResourceName)

Resource name and display name.

### [ResponseMessage](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ResponseMessage)

Represents a response message that can be returned by a conversational agent.

Response messages are also used for output audio synthesis. The approach is as follows:

  * If at least one OutputAudioText response is present, then all OutputAudioText responses are linearly concatenated, and the result is used for output audio synthesis.
  * If the OutputAudioText responses are a mixture of text and SSML, then the concatenated result is treated as SSML; otherwise, the result is treated as either text or SSML as appropriate. The agent designer should ideally use either text or SSML consistently throughout the bot design.
  * Otherwise, all Text responses are linearly concatenated, and the result is used for output audio synthesis.



This approach allows for more sophisticated user experience scenarios, where the text displayed to the user may differ from what is heard.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [RestoreAgentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.RestoreAgentRequest)

The request message for Agents.RestoreAgent.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [RestorePlaybookVersionRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.RestorePlaybookVersionRequest)

The request message for Playbooks.RestorePlaybookVersion.

### [RestorePlaybookVersionResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.RestorePlaybookVersionResponse)

The response message for Playbooks.RestorePlaybookVersion.

### [RestoreToolVersionRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.RestoreToolVersionRequest)

The request message for Tools.RestoreToolVersion.

### [RestoreToolVersionResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.RestoreToolVersionResponse)

The response message for Tools.RestoreToolVersion.

### [RolloutConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.RolloutConfig)

The configuration for auto rollout.

### [RolloutState](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.RolloutState)

State of the auto-rollout process.

### [RunContinuousTestMetadata](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.RunContinuousTestMetadata)

Metadata returned for the Environments.RunContinuousTest long running operation.

### [RunContinuousTestRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.RunContinuousTestRequest)

The request message for Environments.RunContinuousTest.

### [RunContinuousTestResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.RunContinuousTestResponse)

The response message for Environments.RunContinuousTest.

### [RunTestCaseMetadata](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.RunTestCaseMetadata)

Metadata returned for the TestCases.RunTestCase long running operation. This message currently has no fields.

### [RunTestCaseRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.RunTestCaseRequest)

The request message for TestCases.RunTestCase.

### [RunTestCaseResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.RunTestCaseResponse)

The response message for TestCases.RunTestCase.

### [SafetySettings](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.SafetySettings)

Settings for Generative Safety.

### [SearchConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.SearchConfig)

Search configuration for UCS search queries.

### [SecuritySettings](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.SecuritySettings)

Represents the settings related to security issues, such as data redaction and data retention. It may take hours for updates on the settings to propagate to all the related components and take effect.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [SentimentAnalysisResult](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.SentimentAnalysisResult)

The result of sentiment analysis. Sentiment analysis inspects user input and identifies the prevailing subjective opinion, especially to determine a user's attitude as positive, negative, or neutral.

### [SessionEntityType](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.SessionEntityType)

Session entity types are referred to as **User** entity types and are entities that are built for an individual user such as favorites, preferences, playlists, and so on.

You can redefine a session entity type at the session level to extend or replace a [custom entity type][google.cloud.dialogflow.cx.v3.EntityType] at the user session level (we refer to the entity types defined at the agent level as "custom entity types").

Note: session entity types apply to all queries, regardless of the language.

For more information about entity types, see the `Dialogflow documentation <https://cloud.google.com/dialogflow/docs/entities-overview>`__.

### [SessionInfo](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.SessionInfo)

Represents session information communicated to and from the webhook.

### [SpeechModelVariant](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.SpeechModelVariant)

Variant of the specified [Speech model][google.cloud.dialogflow.cx.v3.InputAudioConfig.model] to use.

See the `Cloud Speech documentation <https://cloud.google.com/speech-to-text/docs/enhanced-models>`__ for which models have different variants. For example, the "phone_call" model has both a standard and an enhanced variant. When you use an enhanced model, you will generally receive higher quality results than for a standard model.
    
    
        - If an enhanced variant does not exist for the given
          <xref uid="google.cloud.dialogflow.cx.v3.InputAudioConfig.model">model</xref>
          and request language, Dialogflow falls back to the
          standard variant.
    
          The `Cloud Speech
          documentation <https://cloud.google.com/speech-to-text/docs/enhanced-models>`__
          describes which models have enhanced variants.
    

### [SpeechProcessingMetadata](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.SpeechProcessingMetadata)

Metadata of the speech-to-text and text-to-speech processing.

### [SpeechToTextSettings](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.SpeechToTextSettings)

Settings related to speech recognition.

### [SpeechWordInfo](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.SpeechWordInfo)

Information for a word recognized by the speech recognizer.

### [SsmlVoiceGender](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.SsmlVoiceGender)

Gender of the voice as described in `SSML voice element <https://www.w3.org/TR/speech-synthesis11/#edef_voice>`__.

### [StartExperimentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.StartExperimentRequest)

The request message for Experiments.StartExperiment.

### [StopExperimentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.StopExperimentRequest)

The request message for Experiments.StopExperiment.

### [StreamingDetectIntentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.StreamingDetectIntentRequest)

The top-level message sent by the client to the Sessions.StreamingDetectIntent method.

Multiple request messages should be sent in order:

  1. The first message must contain session, query_input plus optionally query_params. If the client wants to receive an audio response, it should also contain output_audio_config.

  2. If query_input was set to query_input.audio.config, all subsequent messages must contain query_input.audio.audio to continue with Speech recognition. If you decide to rather detect an intent from text input after you already started Speech recognition, please send a message with query_input.text.

However, note that:

     * Dialogflow will bill you for the audio duration so far.
     * Dialogflow discards all Speech recognition results in favor of the input text.
     * Dialogflow will use the language code from the first message.



After you sent all input, you must half-close or abort the request stream.

### [StreamingDetectIntentResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.StreamingDetectIntentResponse)

The top-level message returned from the StreamingDetectIntent method.

Multiple response messages can be returned in order:

  * If the `StreamingDetectIntentRequest.query_input.audio` field was set, the first M messages contain `recognition_result`. Each `recognition_result` represents a more complete transcript of what the user said. The last `recognition_result` has `is_final` set to `true`.

  * If the `StreamingDetectIntentRequest.enable_partial_response` field was true, the `detect_intent_response` field is populated for each of the following N responses, where 0 <= N <= 5. These responses set the DetectIntentResponse.response_type field to `PARTIAL`.




For the last response message, the `detect_intent_response` is fully populated, and DetectIntentResponse.response_type is set to `FINAL`.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [StreamingRecognitionResult](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.StreamingRecognitionResult)

Contains a speech recognition result corresponding to a portion of the audio that is currently being processed or an indication that this is the end of the single requested utterance.

While end-user audio is being processed, Dialogflow sends a series of results. Each result may contain a `transcript` value. A transcript represents a portion of the utterance. While the recognizer is processing audio, transcript values may be interim values or finalized values. Once a transcript is finalized, the `is_final` value is set to true and processing continues for the next transcript.

If `StreamingDetectIntentRequest.query_input.audio.config.single_utterance` was true, and the recognizer has completed processing audio, the `message_type` value is set to `END_OF_SINGLE_UTTERANCE and the following (last) result contains the last finalized transcript.

The complete end-user utterance is determined by concatenating the finalized transcript values received for the series of results.

In the following example, single utterance is enabled. In the case where single utterance is not enabled, result 7 would not occur.

::

Num | transcript | message_type | is_final  
---|---|---|---  
1 | "tube" | TRANSCRIPT | false  
2 | "to be a" | TRANSCRIPT | false  
3 | "to be" | TRANSCRIPT | false  
4 | "to be or not to be" | TRANSCRIPT | true  
5 | "that's" | TRANSCRIPT | false  
6 | "that is | TRANSCRIPT | false  
7 | unset | END_OF_SINGLE_UTTERANCE | unset  
8 | " that is the question" | TRANSCRIPT | true  
  
Concatenating the finalized transcripts with `is_final` set to true, the complete utterance becomes "to be or not to be that is the question".

### [SubmitAnswerFeedbackRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.SubmitAnswerFeedbackRequest)

The request to set the feedback for a bot answer.

### [SynthesizeSpeechConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.SynthesizeSpeechConfig)

Configuration of how speech should be synthesized.

### [TestCase](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.TestCase)

Represents a test case.

### [TestCaseError](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.TestCaseError)

Error info for importing a test.

### [TestCaseResult](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.TestCaseResult)

Represents a result from running a test case in an agent environment.

### [TestConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.TestConfig)

Represents configurations for a test case.

### [TestError](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.TestError)

Error info for running a test.

### [TestResult](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.TestResult)

The test result for a test case and an agent environment.

### [TestRunDifference](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.TestRunDifference)

The description of differences between original and replayed agent output.

### [TextInput](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.TextInput)

Represents the natural language text to be processed.

### [TextToSpeechSettings](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.TextToSpeechSettings)

Settings related to speech synthesizing.

### [Tool](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.Tool)

A tool provides a list of actions which are available to the Playbook to attain its goal. A Tool consists of a description of the tool's usage and a specification of the tool which contains the schema and authentication information.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ToolCall](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ToolCall)

Represents a call of a specific tool's action with the specified inputs.

### [ToolCallResult](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ToolCallResult)

The result of calling a tool's action that has been executed by the client.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ToolUse](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ToolUse)

Stores metadata of the invocation of an action supported by a tool.

### [ToolVersion](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ToolVersion)

Tool version is a snapshot of the tool at certain timestamp.

### [TraceBlock](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.TraceBlock)

The trace block tracks a sequence of actions taken by the agent in a flow or a playbook.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [TrainFlowRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.TrainFlowRequest)

The request message for Flows.TrainFlow.

### [TransitionCoverage](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.TransitionCoverage)

Transition coverage represents the percentage of all possible page transitions (page-level transition routes and event handlers, excluding transition route groups) present within any of a parent's test cases.

### [TransitionRoute](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.TransitionRoute)

A transition route specifies a intent that can be matched and/or a data condition that can be evaluated during a session. When a specified transition is matched, the following actions are taken in order:

  * If there is a [`trigger_fulfillment`][google.cloud.dialogflow.cx.v3.TransitionRoute.trigger_fulfillment] associated with the transition, it will be called.
  * If there is a [`target_page`][google.cloud.dialogflow.cx.v3.TransitionRoute.target_page] associated with the transition, the session will transition into the specified page.
  * If there is a [`target_flow`][google.cloud.dialogflow.cx.v3.TransitionRoute.target_flow] associated with the transition, the session will transition into the specified flow.



This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [TransitionRouteGroup](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.TransitionRouteGroup)

A TransitionRouteGroup represents a group of [`TransitionRoutes`][google.cloud.dialogflow.cx.v3.TransitionRoute] to be used by a Page.

### [TransitionRouteGroupCoverage](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.TransitionRouteGroupCoverage)

Transition route group coverage represents the percentage of all possible transition routes present within any of a parent's test cases. The results are grouped by the transition route group.

### [TypeSchema](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.TypeSchema)

Encapsulates different type schema variations: either a reference to an a schema that's already defined by a tool, or an inline definition.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [UpdateAgentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.UpdateAgentRequest)

The request message for Agents.UpdateAgent.

### [UpdateEntityTypeRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.UpdateEntityTypeRequest)

The request message for EntityTypes.UpdateEntityType.

### [UpdateEnvironmentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.UpdateEnvironmentRequest)

The request message for Environments.UpdateEnvironment.

### [UpdateExampleRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.UpdateExampleRequest)

The request message for Examples.UpdateExample.

### [UpdateExperimentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.UpdateExperimentRequest)

The request message for Experiments.UpdateExperiment.

### [UpdateFlowRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.UpdateFlowRequest)

The request message for Flows.UpdateFlow.

### [UpdateGenerativeSettingsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.UpdateGenerativeSettingsRequest)

Request for UpdateGenerativeSettings RPC.

### [UpdateGeneratorRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.UpdateGeneratorRequest)

The request message for Generators.UpdateGenerator.

### [UpdateIntentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.UpdateIntentRequest)

The request message for Intents.UpdateIntent.

### [UpdatePageRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.UpdatePageRequest)

The request message for Pages.UpdatePage.

### [UpdatePlaybookRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.UpdatePlaybookRequest)

The request message for Playbooks.UpdatePlaybook.

### [UpdateSecuritySettingsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.UpdateSecuritySettingsRequest)

The request message for SecuritySettingsService.UpdateSecuritySettings.

### [UpdateSessionEntityTypeRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.UpdateSessionEntityTypeRequest)

The request message for SessionEntityTypes.UpdateSessionEntityType.

### [UpdateTestCaseRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.UpdateTestCaseRequest)

The request message for TestCases.UpdateTestCase.

### [UpdateToolRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.UpdateToolRequest)

The request message for Tools.UpdateTool.

### [UpdateTransitionRouteGroupRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.UpdateTransitionRouteGroupRequest)

The request message for TransitionRouteGroups.UpdateTransitionRouteGroup.

### [UpdateVersionRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.UpdateVersionRequest)

The request message for Versions.UpdateVersion.

### [UpdateWebhookRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.UpdateWebhookRequest)

The request message for Webhooks.UpdateWebhook.

### [UserUtterance](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.UserUtterance)

UserUtterance represents one message sent by the customer.

### [ValidateAgentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ValidateAgentRequest)

The request message for Agents.ValidateAgent.

### [ValidateFlowRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ValidateFlowRequest)

The request message for Flows.ValidateFlow.

### [ValidationMessage](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.ValidationMessage)

Agent/flow validation message.

### [VariantsHistory](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.VariantsHistory)

The history of variants update.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Version](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.Version)

Represents a version of a flow.

### [VersionVariants](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.VersionVariants)

A list of flow version variants.

### [VoiceSelectionParams](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.VoiceSelectionParams)

Description of which voice to use for speech synthesis.

### [Webhook](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.Webhook)

Webhooks host the developer's business logic. During a session, webhooks allow the developer to use the data extracted by Dialogflow's natural language processing to generate dynamic responses, validate collected data, or trigger actions on the backend.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [WebhookRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.WebhookRequest)

The request message for a webhook call. The request is sent as a JSON object and the field names will be presented in camel cases.

You may see undocumented fields in an actual request. These fields are used internally by Dialogflow and should be ignored.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [WebhookResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.WebhookResponse)

The response message for a webhook call.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
