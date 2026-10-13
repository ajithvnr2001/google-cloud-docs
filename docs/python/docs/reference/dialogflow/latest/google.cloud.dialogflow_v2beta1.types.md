---
url: https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types
title: Package types (2.52.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:43:01.505311+00:00
---

# Package types (2.52.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package types (2.52.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.52.0 (latest)  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.2  2.40.0  2.39.1  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.30.2  2.29.0  2.28.3  2.27.0  2.26.0  2.25.0  2.24.1  2.23.3  2.22.0  2.21.0  2.20.0  2.19.1  2.18.0  2.17.0  2.16.1  2.15.2  2.14.1  2.13.0  2.12.0  2.11.0  2.10.0  2.9.1  2.8.1  2.7.1  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.2  2.0.0  1.1.3  1.0.0  0.8.0  0.7.2 

API documentation for `dialogflow_v2beta1.types` package.

## Classes 

### [Agent](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Agent)

A Dialogflow agent is a virtual agent that handles conversations with your end-users. It is a natural language understanding module that understands the nuances of human language. Dialogflow translates end-user text or audio during a conversation to structured data that your apps and services can understand. You design and build a Dialogflow agent to handle the types of conversations required for your system.

For more information about agents, see the `Agent guide <https://cloud.google.com/dialogflow/docs/agents-overview>`__.

### [AgentAssistantFeedback](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.AgentAssistantFeedback)

Detail feedback of Agent Assistant result.

### [AgentAssistantRecord](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.AgentAssistantRecord)

Represents a record of a human agent assistant answer.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AgentCoachingContext](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.AgentCoachingContext)

Agent Coaching context that customer can configure.

### [AgentCoachingInstruction](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.AgentCoachingInstruction)

Agent Coaching instructions that customer can configure.

### [AgentCoachingSuggestion](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.AgentCoachingSuggestion)

Suggestion for coaching agents.

### [AnalyzeContentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.AnalyzeContentRequest)

The request message for Participants.AnalyzeContent.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AnalyzeContentResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.AnalyzeContentResponse)

The response message for Participants.AnalyzeContent.

### [AnnotatedMessagePart](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.AnnotatedMessagePart)

Represents a part of a message possibly annotated with an entity. The part can be an entity or purely a part of the message between two entities or message start/end.

### [AnswerFeedback](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.AnswerFeedback)

Represents feedback the customer has about the quality & correctness of a certain answer in a conversation.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AnswerRecord](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.AnswerRecord)

Answer records are records to manage answer history and feedbacks for Dialogflow.

Currently, answer record includes:

  * human agent assistant article suggestion
  * human agent assistant faq article



It doesn't include:

  * `DetectIntent` intent matching
  * `DetectIntent` knowledge



Answer records are not related to the conversation history in the Dialogflow Console. A Record is generated even when the end-user disables conversation history in the console. Records are created when there's a human agent assistant suggestion generated.

A typical workflow for customers provide feedback to an answer is:

  1. For human agent assistant, customers get suggestion via ListSuggestions API. Together with the answers, AnswerRecord.name are returned to the customers.
  2. The customer uses the AnswerRecord.name to call the [UpdateAnswerRecord][] method to send feedback about a specific answer that they believe is wrong.



.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ArticleAnswer](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ArticleAnswer)

Represents article answer.

### [AssistQueryParameters](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.AssistQueryParameters)

Represents the parameters of human assist query.

### [AudioEncoding](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.AudioEncoding)

Audio encoding of the audio content sent in the conversational query request. Refer to the `Cloud Speech API documentation <https://cloud.google.com/speech-to-text/docs/basics>`__ for more details.

### [AudioInput](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.AudioInput)

Represents the natural language speech audio to be processed.

### [AutomatedAgentConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.AutomatedAgentConfig)

Defines the Automated Agent to connect to a conversation.

### [AutomatedAgentReply](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.AutomatedAgentReply)

Represents a response from an automated agent.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [BargeInConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.BargeInConfig)

Configuration of the barge-in behavior. Barge-in instructs the API to return a detected utterance at a proper time while the client is playing back the response audio from a previous request. When the client sees the utterance, it should stop the playback and immediately get ready for receiving the responses for the current request.

The barge-in handling requires the client to start streaming audio input as soon as it starts playing back the audio from the previous response. The playback is modeled into two phases:

  * No barge-in phase: which goes first and during which speech detection should not be carried out.

  * Barge-in phase: which follows the no barge-in phase and during which the API starts speech detection and may inform the client that an utterance has been detected. Note that no-speech event is not expected in this phase.




The client provides this configuration in terms of the durations of those two phases. The durations are measured in terms of the audio length from the start of the input audio.

The flow goes like below:

::

\--> Time

without speech detection | utterance only | utterance or no-speech event | | +-------------+ | +------------+ | +---------------+ \----------+ no barge-in +-|-+ barge-in +-|-+ normal period +----------- +-------------+ | +------------+ | +---------------+

No-speech event is a response with END_OF_UTTERANCE without any transcript following up.

### [BatchCreateEntitiesRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.BatchCreateEntitiesRequest)

The request message for EntityTypes.BatchCreateEntities.

### [BatchCreateMessagesRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.BatchCreateMessagesRequest)

The request message for [Conversations.BatchCreateMessagesRequest][].

### [BatchCreateMessagesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.BatchCreateMessagesResponse)

The request message for [Conversations.BatchCreateMessagesResponse][].

### [BatchDeleteEntitiesRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.BatchDeleteEntitiesRequest)

The request message for EntityTypes.BatchDeleteEntities.

### [BatchDeleteEntityTypesRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.BatchDeleteEntityTypesRequest)

The request message for EntityTypes.BatchDeleteEntityTypes.

### [BatchDeleteIntentsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.BatchDeleteIntentsRequest)

The request message for Intents.BatchDeleteIntents.

### [BatchUpdateEntitiesRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.BatchUpdateEntitiesRequest)

The request message for EntityTypes.BatchUpdateEntities.

### [BatchUpdateEntityTypesRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.BatchUpdateEntityTypesRequest)

The request message for EntityTypes.BatchUpdateEntityTypes.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [BatchUpdateEntityTypesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.BatchUpdateEntityTypesResponse)

The response message for EntityTypes.BatchUpdateEntityTypes.

### [BatchUpdateIntentsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.BatchUpdateIntentsRequest)

The request message for Intents.BatchUpdateIntents.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [BatchUpdateIntentsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.BatchUpdateIntentsResponse)

The response message for Intents.BatchUpdateIntents.

### [BidiStreamingAnalyzeContentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.BidiStreamingAnalyzeContentRequest)

The request message for Participants.BidiStreamingAnalyzeContent.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [BidiStreamingAnalyzeContentResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.BidiStreamingAnalyzeContentResponse)

The response message for Participants.BidiStreamingAnalyzeContent.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [CesAppSpec](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.CesAppSpec)

Spec of CES app that the generator can choose from.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [CesToolSpec](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.CesToolSpec)

Spec of CES tool that the generator can choose from.

### [ClearSuggestionFeatureConfigOperationMetadata](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ClearSuggestionFeatureConfigOperationMetadata)

Metadata for a [ConversationProfile.ClearSuggestionFeatureConfig][] operation.

### [ClearSuggestionFeatureConfigRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ClearSuggestionFeatureConfigRequest)

The request message for [ConversationProfiles.ClearFeature][].

### [CloudConversationDebuggingInfo](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.CloudConversationDebuggingInfo)

Cloud conversation info for easier debugging. It will get populated in `StreamingDetectIntentResponse` or `StreamingAnalyzeContentResponse` when the flag `enable_debugging_info` is set to true in corresponding requests.

### [CompileSuggestionRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.CompileSuggestionRequest)

The request message for Participants.CompileSuggestion.

### [CompileSuggestionResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.CompileSuggestionResponse)

The response message for Participants.CompileSuggestion.

### [CompleteConversationRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.CompleteConversationRequest)

The request message for Conversations.CompleteConversation.

### [Connection](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Connection)

Represents a connection for SIP Trunk.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Context](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Context)

Dialogflow contexts are similar to natural language context. If a person says to you "they are orange", you need context in order to understand what "they" is referring to. Similarly, for Dialogflow to handle an end-user expression like that, it needs to be provided with context in order to correctly match an intent.

Using contexts, you can control the flow of a conversation. You can configure contexts for an intent by setting input and output contexts, which are identified by string names. When an intent is matched, any configured output contexts for that intent become active. While any contexts are active, Dialogflow is more likely to match intents that are configured with input contexts that correspond to the currently active contexts.

For more information about context, see the `Contexts guide <https://cloud.google.com/dialogflow/docs/contexts-overview>`__.

### [Conversation](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Conversation)

Represents a conversation. A conversation is an interaction between an agent, including live agents and Dialogflow agents, and a support customer. Conversations can include phone calls and text-based chat sessions.

### [ConversationContext](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ConversationContext)

Context of the conversation, including transcripts.

### [ConversationEvent](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ConversationEvent)

Represents a notification sent to Pub/Sub subscribers for conversation lifecycle events.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ConversationPhoneNumber](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ConversationPhoneNumber)

Represents a phone number for telephony integration. It allows for connecting a particular conversation over telephony.

### [ConversationProfile](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ConversationProfile)

Defines the services to connect to incoming Dialogflow conversations.

### [CreateContextRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.CreateContextRequest)

The request message for Contexts.CreateContext.

### [CreateConversationProfileRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.CreateConversationProfileRequest)

The request message for ConversationProfiles.CreateConversationProfile.

### [CreateConversationRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.CreateConversationRequest)

The request message for Conversations.CreateConversation.

### [CreateDocumentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.CreateDocumentRequest)

Request message for Documents.CreateDocument.

### [CreateEntityTypeRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.CreateEntityTypeRequest)

The request message for EntityTypes.CreateEntityType.

### [CreateEnvironmentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.CreateEnvironmentRequest)

The request message for Environments.CreateEnvironment.

### [CreateGeneratorEvaluationRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.CreateGeneratorEvaluationRequest)

Request of CreateGeneratorEvaluation.

### [CreateGeneratorRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.CreateGeneratorRequest)

Request message of CreateGenerator.

### [CreateIntentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.CreateIntentRequest)

The request message for Intents.CreateIntent.

### [CreateKnowledgeBaseRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.CreateKnowledgeBaseRequest)

Request message for KnowledgeBases.CreateKnowledgeBase.

### [CreateMessageRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.CreateMessageRequest)

The request message to create one Message. Currently it is only used in BatchCreateMessagesRequest.

### [CreateParticipantRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.CreateParticipantRequest)

The request message for Participants.CreateParticipant.

### [CreateSessionEntityTypeRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.CreateSessionEntityTypeRequest)

The request message for SessionEntityTypes.CreateSessionEntityType.

### [CreateSipTrunkRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.CreateSipTrunkRequest)

The request message for SipTrunks.CreateSipTrunk.

### [CreateToolRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.CreateToolRequest)

Request message of CreateTool.

### [CreateVersionRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.CreateVersionRequest)

The request message for Versions.CreateVersion.

### [CustomPronunciationParams](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.CustomPronunciationParams)

Pronunciation customization for a phrase.

### [DatastoreResponseReason](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.DatastoreResponseReason)

Response reason from datastore which indicates data serving status or answer quality degradation.

### [DeleteAgentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.DeleteAgentRequest)

The request message for Agents.DeleteAgent.

### [DeleteAllContextsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.DeleteAllContextsRequest)

The request message for Contexts.DeleteAllContexts.

### [DeleteContextRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.DeleteContextRequest)

The request message for Contexts.DeleteContext.

### [DeleteConversationProfileRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.DeleteConversationProfileRequest)

The request message for ConversationProfiles.DeleteConversationProfile.

This operation fails if the conversation profile is still referenced from a phone number.

### [DeleteDocumentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.DeleteDocumentRequest)

Request message for Documents.DeleteDocument.

### [DeleteEntityTypeRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.DeleteEntityTypeRequest)

The request message for EntityTypes.DeleteEntityType.

### [DeleteEnvironmentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.DeleteEnvironmentRequest)

The request message for Environments.DeleteEnvironment.

### [DeleteGeneratorEvaluationRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.DeleteGeneratorEvaluationRequest)

Request of DeleteGeneratorEvaluation.

### [DeleteGeneratorRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.DeleteGeneratorRequest)

Request of DeleteGenerator.

### [DeleteIntentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.DeleteIntentRequest)

The request message for Intents.DeleteIntent.

### [DeleteKnowledgeBaseRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.DeleteKnowledgeBaseRequest)

Request message for KnowledgeBases.DeleteKnowledgeBase.

### [DeletePhoneNumberRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.DeletePhoneNumberRequest)

The request message for PhoneNumbers.DeletePhoneNumber.

### [DeleteSessionEntityTypeRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.DeleteSessionEntityTypeRequest)

The request message for SessionEntityTypes.DeleteSessionEntityType.

### [DeleteSipTrunkRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.DeleteSipTrunkRequest)

The request message for SipTrunks.DeleteSipTrunk.

### [DeleteToolRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.DeleteToolRequest)

Request of DeleteTool.

### [DeleteVersionRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.DeleteVersionRequest)

The request message for Versions.DeleteVersion.

### [DetectIntentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.DetectIntentRequest)

The request to detect user's intent.

### [DetectIntentResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.DetectIntentResponse)

The message returned from the DetectIntent method.

### [DialogflowAssistAnswer](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.DialogflowAssistAnswer)

Represents a Dialogflow assist answer.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Document](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Document)

A knowledge document to be used by a KnowledgeBase.

For more information, see the `knowledge base guide <https://cloud.google.com/dialogflow/docs/how/knowledge-bases>`__.

Note: The `projects.agent.knowledgeBases.documents` resource is deprecated; only use `projects.knowledgeBases.documents`.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [DtmfParameters](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.DtmfParameters)

The message in the response that indicates the parameters of DTMF.

### [EncryptionSpec](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.EncryptionSpec)

A customer-managed encryption key specification that can be applied to all created resources (e.g. Conversation).

### [EntityType](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.EntityType)

Each intent parameter has a type, called the entity type, which dictates exactly how data from an end-user expression is extracted.

Dialogflow provides predefined system entities that can match many common types of data. For example, there are system entities for matching dates, times, colors, email addresses, and so on. You can also create your own custom entities for matching custom data. For example, you could define a vegetable entity that can match the types of vegetables available for purchase with a grocery store agent.

For more information, see the `Entity guide <https://cloud.google.com/dialogflow/docs/entities-overview>`__.

### [EntityTypeBatch](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.EntityTypeBatch)

This message is a wrapper around a collection of entity types.

### [Environment](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Environment)

You can create multiple versions of your agent and publish them to separate environments.

When you edit an agent, you are editing the draft agent. At any point, you can save the draft agent as an agent version, which is an immutable snapshot of your agent.

When you save the draft agent, it is published to the default environment. When you create agent versions, you can publish them to custom environments. You can create a variety of custom environments for:

  * testing
  * development
  * production
  * etc.



For more information, see the `versions and environments guide <https://cloud.google.com/dialogflow/docs/agents-versions>`__.

### [EnvironmentHistory](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.EnvironmentHistory)

The response message for Environments.GetEnvironmentHistory.

### [EvaluationStatus](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.EvaluationStatus)

A common evalaution pipeline status.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [EventInput](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.EventInput)

Events allow for matching intents by event name instead of the natural language input. For instance, input `<event: { name: "welcome_event", parameters: { name: "Sam" } }>` can trigger a personalized welcome response. The parameter `name` may be used by the agent in the response: `"Hello #welcome_event.name! What can I do for you today?"`.

### [ExportAgentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ExportAgentRequest)

The request message for Agents.ExportAgent.

### [ExportAgentResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ExportAgentResponse)

The response message for Agents.ExportAgent.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ExportOperationMetadata](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ExportOperationMetadata)

Metadata related to the Export Data Operations (e.g. ExportDocument).

### [FaqAnswer](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.FaqAnswer)

Represents answer from "frequently asked questions".

### [FewShotExample](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.FewShotExample)

Providing examples in the generator (i.e. building a few-shot generator) helps convey the desired format of the LLM response.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [FreeFormContext](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.FreeFormContext)

Free form generator context that customer can configure.

### [FreeFormSuggestion](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.FreeFormSuggestion)

Suggestion generated using free form generator.

### [Fulfillment](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Fulfillment)

By default, your agent responds to a matched intent with a static response. As an alternative, you can provide a more dynamic response by using fulfillment. When you enable fulfillment for an intent, Dialogflow responds to that intent by calling a service that you define. For example, if an end-user wants to schedule a haircut on Friday, your service can check your database and respond to the end-user with availability information for Friday.

For more information, see the `fulfillment guide <https://cloud.google.com/dialogflow/docs/fulfillment-overview>`__.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [GcsDestination](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.GcsDestination)

Google Cloud Storage location for the output.

### [GcsSource](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.GcsSource)

Google Cloud Storage location for single input.

### [GcsSources](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.GcsSources)

Google Cloud Storage locations for the inputs.

### [GenerateStatelessSuggestionRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.GenerateStatelessSuggestionRequest)

The request message for Conversations.GenerateStatelessSuggestion.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [GenerateStatelessSuggestionResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.GenerateStatelessSuggestionResponse)

The response message for Conversations.GenerateStatelessSuggestion.

### [GenerateStatelessSummaryRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.GenerateStatelessSummaryRequest)

The request message for Conversations.GenerateStatelessSummary.

### [GenerateStatelessSummaryResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.GenerateStatelessSummaryResponse)

The response message for Conversations.GenerateStatelessSummary.

### [GenerateSuggestionsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.GenerateSuggestionsRequest)

The request message for Conversations.GenerateSuggestions.

### [GenerateSuggestionsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.GenerateSuggestionsResponse)

The response message for Conversations.GenerateSuggestions.

### [Generator](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Generator)

LLM generator.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [GeneratorEvaluation](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.GeneratorEvaluation)

Represents evaluation result of a generator.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [GeneratorEvaluationConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.GeneratorEvaluationConfig)

Generator evaluation input config.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [GeneratorEvaluationOperationMetadata](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.GeneratorEvaluationOperationMetadata)

Metadata for a GeneratorEvaluations.CreateGeneratorEvaluation operation.

### [GeneratorSuggestion](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.GeneratorSuggestion)

Suggestion generated using a Generator.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [GetAgentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.GetAgentRequest)

The request message for Agents.GetAgent.

### [GetAnswerRecordRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.GetAnswerRecordRequest)

Request message for AnswerRecords.GetAnswerRecord.

### [GetContextRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.GetContextRequest)

The request message for Contexts.GetContext.

### [GetConversationProfileRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.GetConversationProfileRequest)

The request message for ConversationProfiles.GetConversationProfile.

### [GetConversationRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.GetConversationRequest)

The request message for Conversations.GetConversation.

### [GetDocumentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.GetDocumentRequest)

Request message for Documents.GetDocument.

### [GetEncryptionSpecRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.GetEncryptionSpecRequest)

The request to get location-level encryption specification.

### [GetEntityTypeRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.GetEntityTypeRequest)

The request message for EntityTypes.GetEntityType.

### [GetEnvironmentHistoryRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.GetEnvironmentHistoryRequest)

The request message for Environments.GetEnvironmentHistory.

### [GetEnvironmentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.GetEnvironmentRequest)

The request message for Environments.GetEnvironment.

### [GetFulfillmentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.GetFulfillmentRequest)

The request message for Fulfillments.GetFulfillment.

### [GetGeneratorEvaluationRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.GetGeneratorEvaluationRequest)

Request of GetGeneratorEvaluation.

### [GetGeneratorRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.GetGeneratorRequest)

Request message of GetGenerator.

### [GetIntentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.GetIntentRequest)

The request message for Intents.GetIntent.

### [GetKnowledgeBaseRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.GetKnowledgeBaseRequest)

Request message for KnowledgeBases.GetKnowledgeBase.

### [GetParticipantRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.GetParticipantRequest)

The request message for Participants.GetParticipant.

### [GetSessionEntityTypeRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.GetSessionEntityTypeRequest)

The request message for SessionEntityTypes.GetSessionEntityType.

### [GetSipTrunkRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.GetSipTrunkRequest)

The request message for SipTrunks.GetSipTrunk.

### [GetToolRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.GetToolRequest)

Request message of GetTool.

### [GetValidationResultRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.GetValidationResultRequest)

The request message for Agents.GetValidationResult.

### [GetVersionRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.GetVersionRequest)

The request message for Versions.GetVersion.

### [HumanAgentAssistantConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.HumanAgentAssistantConfig)

Defines the Human Agent Assistant to connect to a conversation.

### [HumanAgentAssistantEvent](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.HumanAgentAssistantEvent)

Output only. Represents a notification sent to Pub/Sub subscribers for agent assistant events in a specific conversation.

### [HumanAgentHandoffConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.HumanAgentHandoffConfig)

Defines the hand off to a live agent, typically on which external agent service provider to connect to a conversation.

Currently, this feature is not general available, please contact Google to get access.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ImportAgentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ImportAgentRequest)

The request message for Agents.ImportAgent.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ImportDocumentTemplate](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ImportDocumentTemplate)

The template used for importing documents.

### [ImportDocumentsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ImportDocumentsRequest)

Request message for Documents.ImportDocuments.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ImportDocumentsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ImportDocumentsResponse)

Response message for Documents.ImportDocuments.

### [InferenceParameter](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.InferenceParameter)

The parameters of inference.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [IngestContextReferencesRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.IngestContextReferencesRequest)

The request message for [ConversationsService.IngestContextReferences][].

### [IngestContextReferencesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.IngestContextReferencesResponse)

The response message for [ConversationsService.IngestContextReferences][].

### [IngestedContextReferenceDebugInfo](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.IngestedContextReferenceDebugInfo)

Debug information related to ingested context reference.

### [InitializeEncryptionSpecMetadata](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.InitializeEncryptionSpecMetadata)

Metadata for initializing a location-level encryption specification.

### [InitializeEncryptionSpecRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.InitializeEncryptionSpecRequest)

The request to initialize a location-level encryption specification.

### [InitializeEncryptionSpecResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.InitializeEncryptionSpecResponse)

The response to initialize a location-level encryption specification.

### [InputAudioConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.InputAudioConfig)

Instructs the speech recognizer on how to process the audio content.

### [InputTextConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.InputTextConfig)

Defines the language used in the input text.

### [Intent](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Intent)

An intent categorizes an end-user's intention for one conversation turn. For each agent, you define many intents, where your combined intents can handle a complete conversation. When an end-user writes or says something, referred to as an end-user expression or end-user input, Dialogflow matches the end-user input to the best intent in your agent. Matching an intent is also known as intent classification.

For more information, see the `intent guide <https://cloud.google.com/dialogflow/docs/intents-overview>`__.

### [IntentBatch](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.IntentBatch)

This message is a wrapper around a collection of intents.

### [IntentInput](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.IntentInput)

Represents the intent to trigger programmatically rather than as a result of natural language processing. The intent input is only used for V3 agent.

### [IntentSuggestion](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.IntentSuggestion)

Represents an intent suggestion.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [IntentView](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.IntentView)

Represents the options for views of an intent. An intent can be a sizable object. Therefore, we provide a resource view that does not return training phrases in the response by default.

### [KnowledgeAnswers](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.KnowledgeAnswers)

Represents the result of querying a Knowledge base.

### [KnowledgeAssistAnswer](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.KnowledgeAssistAnswer)

Represents a Knowledge Assist answer.

### [KnowledgeAssistDebugInfo](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.KnowledgeAssistDebugInfo)

Debug information related to Knowledge Assist feature.

### [KnowledgeBase](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.KnowledgeBase)

A knowledge base represents a collection of knowledge documents that you provide to Dialogflow. Your knowledge documents contain information that may be useful during conversations with end-users. Some Dialogflow features use knowledge bases when looking for a response to an end-user input.

For more information, see the `knowledge base guide <https://cloud.google.com/dialogflow/docs/how/knowledge-bases>`__.

Note: The `projects.agent.knowledgeBases` resource is deprecated; only use `projects.knowledgeBases`.

### [KnowledgeOperationMetadata](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.KnowledgeOperationMetadata)

Metadata in google::longrunning::Operation for Knowledge operations.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ListAnswerRecordsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListAnswerRecordsRequest)

Request message for AnswerRecords.ListAnswerRecords.

### [ListAnswerRecordsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListAnswerRecordsResponse)

Response message for AnswerRecords.ListAnswerRecords.

### [ListContextsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListContextsRequest)

The request message for Contexts.ListContexts.

### [ListContextsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListContextsResponse)

The response message for Contexts.ListContexts.

### [ListConversationProfilesRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListConversationProfilesRequest)

The request message for ConversationProfiles.ListConversationProfiles.

### [ListConversationProfilesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListConversationProfilesResponse)

The response message for ConversationProfiles.ListConversationProfiles.

### [ListConversationsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListConversationsRequest)

The request message for Conversations.ListConversations.

### [ListConversationsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListConversationsResponse)

The response message for Conversations.ListConversations.

### [ListDocumentsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListDocumentsRequest)

Request message for Documents.ListDocuments.

### [ListDocumentsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListDocumentsResponse)

Response message for Documents.ListDocuments.

### [ListEntityTypesRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListEntityTypesRequest)

The request message for EntityTypes.ListEntityTypes.

### [ListEntityTypesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListEntityTypesResponse)

The response message for EntityTypes.ListEntityTypes.

### [ListEnvironmentsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListEnvironmentsRequest)

The request message for Environments.ListEnvironments.

### [ListEnvironmentsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListEnvironmentsResponse)

The response message for Environments.ListEnvironments.

### [ListGeneratorEvaluationsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListGeneratorEvaluationsRequest)

Request of ListGeneratorEvaluations.

### [ListGeneratorEvaluationsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListGeneratorEvaluationsResponse)

Response of ListGeneratorEvaluations.

### [ListGeneratorsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListGeneratorsRequest)

Request message of ListGenerators.

### [ListGeneratorsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListGeneratorsResponse)

Response of ListGenerators.

### [ListIntentsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListIntentsRequest)

The request message for Intents.ListIntents.

### [ListIntentsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListIntentsResponse)

The response message for Intents.ListIntents.

### [ListKnowledgeBasesRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListKnowledgeBasesRequest)

Request message for KnowledgeBases.ListKnowledgeBases.

### [ListKnowledgeBasesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListKnowledgeBasesResponse)

Response message for KnowledgeBases.ListKnowledgeBases.

### [ListMessagesRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListMessagesRequest)

The request message for Conversations.ListMessages.

### [ListMessagesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListMessagesResponse)

The response message for Conversations.ListMessages.

### [ListParticipantsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListParticipantsRequest)

The request message for Participants.ListParticipants.

### [ListParticipantsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListParticipantsResponse)

The response message for Participants.ListParticipants.

### [ListPhoneNumbersRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListPhoneNumbersRequest)

The request message for PhoneNumbers.ListPhoneNumbers.

### [ListPhoneNumbersResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListPhoneNumbersResponse)

The response message for PhoneNumbers.ListPhoneNumbers.

### [ListSessionEntityTypesRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListSessionEntityTypesRequest)

The request message for SessionEntityTypes.ListSessionEntityTypes.

### [ListSessionEntityTypesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListSessionEntityTypesResponse)

The response message for SessionEntityTypes.ListSessionEntityTypes.

### [ListSipTrunksRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListSipTrunksRequest)

The request message for SipTrunks.ListSipTrunks.

### [ListSipTrunksResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListSipTrunksResponse)

The response message for SipTrunks.ListSipTrunks.

### [ListSuggestionsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListSuggestionsRequest)

The request message for Participants.ListSuggestions.

### [ListSuggestionsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListSuggestionsResponse)

The response message for Participants.ListSuggestions.

### [ListToolsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListToolsRequest)

Request message of ListTools.

### [ListToolsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListToolsResponse)

Response of ListTools.

### [ListVersionsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListVersionsRequest)

The request message for Versions.ListVersions.

### [ListVersionsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListVersionsResponse)

The response message for Versions.ListVersions.

### [LoggingConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.LoggingConfig)

Defines logging behavior for conversation lifecycle events.

### [Message](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Message)

Represents a message posted into a conversation.

### [MessageAnnotation](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.MessageAnnotation)

Represents the result of annotation for the message.

### [MessageEntry](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.MessageEntry)

Represents a message entry of a conversation.

### [NotificationConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.NotificationConfig)

Defines notification behavior.

### [OriginalDetectIntentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.OriginalDetectIntentRequest)

Represents the contents of the original request that was passed to the `[Streaming]DetectIntent` call.

### [OutputAudio](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.OutputAudio)

Represents the natural language speech audio to be played to the end user.

### [OutputAudioConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.OutputAudioConfig)

Instructs the speech synthesizer how to generate the output audio content. If this audio config is supplied in a request, it overrides all existing text-to-speech settings applied to the agent.

### [OutputAudioEncoding](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.OutputAudioEncoding)

Audio encoding of the output audio format in Text-To-Speech.

### [Participant](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Participant)

Represents a conversation participant (human agent, virtual agent, end-user).

### [PhoneNumber](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.PhoneNumber)

Represents a phone number. `PhoneNumber` resources enable phone calls to be answered by Dialogflow services and are added to a project through a PhoneNumberOrder.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ProbeDetails](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ProbeDetails)

The probe details of Sip Trunk peer hostname.

### [QueryInput](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.QueryInput)

Represents the query input. It can contain either:

  1. An audio config which instructs the speech recognizer how to process the speech audio.

  2. A conversational query in the form of text.

  3. An event that specifies which intent to trigger.




This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [QueryParameters](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.QueryParameters)

Represents the parameters of the conversational query.

### [QueryResult](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.QueryResult)

Represents the result of conversational query or event processing.

### [RaiSettings](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.RaiSettings)

Settings for Responsible AI checks.

### [ReloadDocumentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ReloadDocumentRequest)

Request message for Documents.ReloadDocument.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ResponseMessage](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ResponseMessage)

Response messages from an automated agent.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [RestoreAgentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.RestoreAgentRequest)

The request message for Agents.RestoreAgent.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [SearchAgentsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SearchAgentsRequest)

The request message for Agents.SearchAgents.

### [SearchAgentsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SearchAgentsResponse)

The response message for Agents.SearchAgents.

### [SearchKnowledgeAnswer](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SearchKnowledgeAnswer)

Represents a SearchKnowledge answer.

### [SearchKnowledgeDebugInfo](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SearchKnowledgeDebugInfo)

Debug information related to SearchKnowledge feature.

### [SearchKnowledgeRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SearchKnowledgeRequest)

The request message for Conversations.SearchKnowledge.

### [SearchKnowledgeResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SearchKnowledgeResponse)

The response message for Conversations.SearchKnowledge.

### [Sentiment](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Sentiment)

The sentiment, such as positive/negative feeling or association, for a unit of analysis, such as the query text. See: <https://cloud.google.com/natural-language/docs/basics#interpreting_sentiment_analysis_values> for how to interpret the result.

### [SentimentAnalysisRequestConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SentimentAnalysisRequestConfig)

Configures the types of sentiment analysis to perform.

### [SentimentAnalysisResult](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SentimentAnalysisResult)

The result of sentiment analysis. Sentiment analysis inspects user input and identifies the prevailing subjective opinion, especially to determine a user's attitude as positive, negative, or neutral. For [Participants.DetectIntent][], it needs to be configured in DetectIntentRequest.query_params. For [Participants.StreamingDetectIntent][], it needs to be configured in StreamingDetectIntentRequest.query_params. And for Participants.AnalyzeContent and Participants.StreamingAnalyzeContent, it needs to be configured in ConversationProfile.human_agent_assistant_config

### [ServiceLatency](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ServiceLatency)

Message to represent the latency of the service.

### [SessionEntityType](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SessionEntityType)

A session represents a conversation between a Dialogflow agent and an end-user. You can create special entities, called session entities, during a session. Session entities can extend or replace custom entity types and only exist during the session that they were created for. All session data, including session entities, is stored by Dialogflow for 20 minutes.

For more information, see the `session entity guide <https://cloud.google.com/dialogflow/docs/entities-session>`__.

### [SetAgentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SetAgentRequest)

The request message for Agents.SetAgent.

### [SetSuggestionFeatureConfigOperationMetadata](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SetSuggestionFeatureConfigOperationMetadata)

Metadata for a [ConversationProfile.SetSuggestionFeatureConfig][] operation.

### [SetSuggestionFeatureConfigRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SetSuggestionFeatureConfigRequest)

The request message for [ConversationProfiles.SetSuggestionFeature][].

### [SipConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SipConfig)

Defines the SIP configuration.

### [SipHostname](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SipHostname)

Represents a peer hostname for SIP Trunk.

### [SipTrunk](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SipTrunk)

SipTrunk is the resource that represents a SIP trunk to connect to Google Telephony platform SIP trunking service.

### [SmartReplyAnswer](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SmartReplyAnswer)

Represents a smart reply answer.

### [SpeechContext](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SpeechContext)

Hints for the speech recognizer to help with recognition in a specific conversation state.

### [SpeechModelVariant](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SpeechModelVariant)

Variant of the specified [Speech model][google.cloud.dialogflow.v2beta1.InputAudioConfig.model] to use.

See the `Cloud Speech documentation <https://cloud.google.com/speech-to-text/docs/enhanced-models>`__ for which models have different variants. For example, the "phone_call" model has both a standard and an enhanced variant. When you use an enhanced model, you will generally receive higher quality results than for a standard model.
    
    
        Please see the `Dialogflow
        docs <https://cloud.google.com/dialogflow/docs/data-logging>`__
        for how to make your project eligible for enhanced models.
    USE_STANDARD (2):
        Use standard model variant even if an enhanced model is
        available. See the `Cloud Speech
        documentation <https://cloud.google.com/speech-to-text/docs/enhanced-models>`__
        for details about enhanced models.
    USE_ENHANCED (3):
        Use an enhanced model variant:
    
        - If an enhanced variant does not exist for the given
          <xref uid="google.cloud.dialogflow.v2beta1.InputAudioConfig.model">model</xref>
          and request language, Dialogflow falls back to the
          standard variant.
    
          The `Cloud Speech
          documentation <https://cloud.google.com/speech-to-text/docs/enhanced-models>`__
          describes which models have enhanced variants.
    
        - If the API caller isn't eligible for enhanced models,
          Dialogflow returns an error. Please see the `Dialogflow
          docs <https://cloud.google.com/dialogflow/docs/data-logging>`__
          for how to make your project eligible.
    

### [SpeechToTextConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SpeechToTextConfig)

Configures speech transcription for ConversationProfile.

### [SpeechWordInfo](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SpeechWordInfo)

Information for a word recognized by the speech recognizer.

### [SsmlVoiceGender](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SsmlVoiceGender)

Gender of the voice as described in `SSML voice element <https://www.w3.org/TR/speech-synthesis11/#edef_voice>`__.

### [StreamingAnalyzeContentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.StreamingAnalyzeContentRequest)

The top-level message sent by the client to the Participants.StreamingAnalyzeContent method.

Multiple request messages should be sent in order:

  1. The first message must contain participant, config and optionally query_params. If you want to receive an audio response, it should also contain reply_audio_config. The message must not contain input.

  2. If config in the first message was set to audio_config, all subsequent messages must contain input_audio to continue with Speech recognition. If you decide to rather analyze text input after you already started Speech recognition, please send a message with StreamingAnalyzeContentRequest.input_text.

However, note that:

     * Dialogflow will bill you for the audio so far.
     * Dialogflow discards all Speech recognition results in favor of the text input.
  3. If StreamingAnalyzeContentRequest.config in the first message was set to StreamingAnalyzeContentRequest.text_config, then the second message must contain only input_text. Moreover, you must not send more than two messages.




After you sent all input, you must half-close or abort the request stream.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [StreamingAnalyzeContentResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.StreamingAnalyzeContentResponse)

The top-level message returned from the `StreamingAnalyzeContent` method.

Multiple response messages can be returned in order:

  1. If the input was set to streaming audio, the first one or more messages contain `recognition_result`. Each `recognition_result` represents a more complete transcript of what the user said. When a user speaks multiple sentences, the API will emit multiple messages where `is_final = true`. Each time the system detects a distinct pause or completed thought, it locks in that segment, marks it `is_final = true`, and then immediately starts a new recognition cycle for the next sentence on the same stream.

  2. In virtual agent stage: if `enable_partial_automated_agent_reply` is true, the following N (currently 1 <= N <= 4) messages contain `automated_agent_reply` and optionally `reply_audio` returned by the virtual agent. The first (N-1) `automated_agent_reply`\ s will have `automated_agent_reply_type` set to `PARTIAL`. The last `automated_agent_reply` has `automated_agent_reply_type` set to `FINAL`. If `enable_partial_automated_agent_reply` is not enabled, response stream only contains the final reply.

In human assist stage: the following N (N >= 1) messages contain `human_agent_suggestion_results`, `end_user_suggestion_results` or `message`.




### [StreamingDetectIntentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.StreamingDetectIntentRequest)

The top-level message sent by the client to the Sessions.StreamingDetectIntent method.

Multiple request messages should be sent in order:

  1. The first message must contain session, query_input plus optionally query_params. If the client wants to receive an audio response, it should also contain output_audio_config. The message must not contain input_audio.

  2. If query_input was set to query_input.audio_config, all subsequent messages must contain input_audio to continue with Speech recognition. If you decide to rather detect an intent from text input after you already started Speech recognition, please send a message with query_input.text.

However, note that:

     * Dialogflow will bill you for the audio duration so far.
     * Dialogflow discards all Speech recognition results in favor of the input text.
     * Dialogflow will use the language code from the first message.



After you sent all input, you must half-close or abort the request stream.

### [StreamingDetectIntentResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.StreamingDetectIntentResponse)

The top-level message returned from the `StreamingDetectIntent` method.

Multiple response messages can be returned in order:

  1. If the `StreamingDetectIntentRequest.input_audio` field was set, the `recognition_result` field is populated for one or more messages. See the StreamingRecognitionResult message for details about the result message sequence.

  2. The next message contains `response_id`, `query_result`, `alternative_query_results` and optionally `webhook_status` if a WebHook was called.

  3. If `output_audio_config` was specified in the request or agent-level speech synthesizer is configured, all subsequent messages contain `output_audio` and `output_audio_config`.




### [StreamingRecognitionResult](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.StreamingRecognitionResult)

Contains a speech recognition result corresponding to a portion of the audio that is currently being processed or an indication that this is the end of the single requested utterance.

While end-user audio is being processed, Dialogflow sends a series of results. Each result may contain a `transcript` value. A transcript represents a portion of the utterance. While the recognizer is processing audio, transcript values may be interim values or finalized values. Once a transcript is finalized, the `is_final` value is set to true and processing continues for the next transcript.

If `StreamingDetectIntentRequest.query_input.audio_config.single_utterance` was true, and the recognizer has completed processing audio, the `message_type` value is set to `END_OF_SINGLE_UTTERANCE and the following (last) result contains the last finalized transcript.

The complete end-user utterance is determined by concatenating the finalized transcript values received for the series of results.

In the following example, single utterance is enabled. In the case where single utterance is not enabled, result 8 would not occur.

::

Num | transcript | message_type | is_final  
---|---|---|---  
1 | "tube" | TRANSCRIPT | false  
2 | "to be a" | TRANSCRIPT | false  
3 | "to be" | TRANSCRIPT | false  
4 | "to be or not to be" | TRANSCRIPT | true  
5 | "that's" | TRANSCRIPT | false  
6 | "that is | TRANSCRIPT | false  
7 | " that is the question" | TRANSCRIPT | true  
8 | unset | END_OF_SINGLE_UTTERANCE | unset  
9 | ". Whether 'tis nobler" | TRANSCRIPT | true  
10 | " in the mind" | TRANSCRIPT | false  
11 | " in the mind to suffer" | TRANSCRIPT | true  
  
Concatenating the finalized transcripts with `is_final` set to true, the complete utterance becomes "to be or not to be that is the question".

### [SubAgent](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SubAgent)

Contains basic configuration for a sub-agent.

### [SuggestArticlesRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SuggestArticlesRequest)

The request message for Participants.SuggestArticles.

### [SuggestArticlesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SuggestArticlesResponse)

The response message for Participants.SuggestArticles.

### [SuggestConversationSummaryRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SuggestConversationSummaryRequest)

The request message for Conversations.SuggestConversationSummary.

### [SuggestConversationSummaryResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SuggestConversationSummaryResponse)

The response message for Conversations.SuggestConversationSummary.

### [SuggestDialogflowAssistsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SuggestDialogflowAssistsResponse)

The response message for Participants.SuggestDialogflowAssists.

### [SuggestFaqAnswersRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SuggestFaqAnswersRequest)

The request message for Participants.SuggestFaqAnswers.

### [SuggestFaqAnswersResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SuggestFaqAnswersResponse)

The request message for Participants.SuggestFaqAnswers.

### [SuggestKnowledgeAssistRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SuggestKnowledgeAssistRequest)

The request message for Participants.SuggestKnowledgeAssist.

### [SuggestKnowledgeAssistResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SuggestKnowledgeAssistResponse)

The response message for Participants.SuggestKnowledgeAssist.

### [SuggestSmartRepliesRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SuggestSmartRepliesRequest)

The request message for Participants.SuggestSmartReplies.

### [SuggestSmartRepliesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SuggestSmartRepliesResponse)

The response message for Participants.SuggestSmartReplies.

### [Suggestion](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Suggestion)

Represents a suggestion for a human agent.

### [SuggestionDedupingConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SuggestionDedupingConfig)

Config for suggestion deduping. NEXT_ID: 3

### [SuggestionFeature](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SuggestionFeature)

The type of Human Agent Assistant API suggestion to perform, and the maximum number of results to return for that type. Multiple `Feature` objects can be specified in the `features` list.

### [SuggestionInput](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SuggestionInput)

Represents the action to take for a tool call that requires confirmation.

### [SuggestionResult](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SuggestionResult)

One response of different type of suggestion response which is used in the response of Participants.AnalyzeContent and Participants.AnalyzeContent, as well as HumanAgentAssistantEvent.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [SummarizationContext](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SummarizationContext)

Summarization context that customer can configure.

### [SummarizationEvaluationMetrics](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SummarizationEvaluationMetrics)

Evaluation metrics for summarization generator.

### [SummarizationSection](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SummarizationSection)

Represents the section of summarization.

### [SummarizationSectionList](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SummarizationSectionList)

List of summarization sections.

### [SummarySuggestion](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SummarySuggestion)

Suggested summary of the conversation.

### [SynthesizeSpeechConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SynthesizeSpeechConfig)

Configuration of how speech should be synthesized.

### [TelephonyDtmf](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.TelephonyDtmf)

`DTMF <https://en.wikipedia.org/wiki/Dual-tone_multi-frequency_signaling>`__ digit in Telephony Gateway.

### [TelephonyDtmfEvents](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.TelephonyDtmfEvents)

A wrapper of repeated TelephonyDtmf digits.

### [TextInput](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.TextInput)

Represents the natural language text to be processed.

### [TextToSpeechSettings](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.TextToSpeechSettings)

Instructs the speech synthesizer on how to generate the output audio content.

### [Tool](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Tool)

Represents a tool.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ToolCall](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ToolCall)

Represents a call of a specific tool's action with the specified inputs.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ToolCallResult](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ToolCallResult)

The result of calling a tool's action.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ToolsetTool](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ToolsetTool)

A tool that is created from a toolset.

### [TrainAgentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.TrainAgentRequest)

The request message for Agents.TrainAgent.

### [TriggerEvent](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.TriggerEvent)

The event that triggers the generator and LLM execution.

### [UndeletePhoneNumberRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.UndeletePhoneNumberRequest)

The request message for PhoneNumbers.UndeletePhoneNumber.

### [UpdateAnswerRecordRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.UpdateAnswerRecordRequest)

Request message for AnswerRecords.UpdateAnswerRecord.

### [UpdateContextRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.UpdateContextRequest)

The request message for Contexts.UpdateContext.

### [UpdateConversationProfileRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.UpdateConversationProfileRequest)

The request message for ConversationProfiles.UpdateConversationProfile.

### [UpdateDocumentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.UpdateDocumentRequest)

Request message for Documents.UpdateDocument.

### [UpdateEntityTypeRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.UpdateEntityTypeRequest)

The request message for EntityTypes.UpdateEntityType.

### [UpdateEnvironmentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.UpdateEnvironmentRequest)

The request message for Environments.UpdateEnvironment.

### [UpdateFulfillmentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.UpdateFulfillmentRequest)

The request message for Fulfillments.UpdateFulfillment.

### [UpdateGeneratorRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.UpdateGeneratorRequest)

Request of UpdateGenerator.

### [UpdateIntentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.UpdateIntentRequest)

The request message for Intents.UpdateIntent.

### [UpdateKnowledgeBaseRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.UpdateKnowledgeBaseRequest)

Request message for KnowledgeBases.UpdateKnowledgeBase.

### [UpdateParticipantRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.UpdateParticipantRequest)

The request message for Participants.UpdateParticipant.

### [UpdatePhoneNumberRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.UpdatePhoneNumberRequest)

The request message for PhoneNumbers.UpdatePhoneNumber.

### [UpdateSessionEntityTypeRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.UpdateSessionEntityTypeRequest)

The request message for SessionEntityTypes.UpdateSessionEntityType.

### [UpdateSipTrunkRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.UpdateSipTrunkRequest)

The request message for SipTrunks.UpdateSipTrunk.

### [UpdateToolRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.UpdateToolRequest)

Request of UpdateTool.

### [UpdateVersionRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.UpdateVersionRequest)

The request message for Versions.UpdateVersion.

### [ValidationError](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ValidationError)

Represents a single validation error.

### [ValidationResult](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ValidationResult)

Represents the output of agent validation.

### [Version](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Version)

You can create multiple versions of your agent and publish them to separate environments.

When you edit an agent, you are editing the draft agent. At any point, you can save the draft agent as an agent version, which is an immutable snapshot of your agent.

When you save the draft agent, it is published to the default environment. When you create agent versions, you can publish them to custom environments. You can create a variety of custom environments for:

  * testing
  * development
  * production
  * etc.



For more information, see the `versions and environments guide <https://cloud.google.com/dialogflow/docs/agents-versions>`__.

### [VoiceSelectionParams](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.VoiceSelectionParams)

Description of which voice to use for speech synthesis.

### [WebhookRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.WebhookRequest)

The request message for a webhook call.

### [WebhookResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.WebhookResponse)

The response message for a webhook call.

This response is validated by the Dialogflow server. If validation fails, an error will be returned in the QueryResult.diagnostic_info field. Setting JSON fields to an empty value with the wrong type is a common error. To avoid this error:

  * Use `""` for empty strings
  * Use `{}` or `null` for empty objects
  * Use `[]` or `null` for empty arrays



For more information, see the `Protocol Buffers Language Guide <https://developers.google.com/protocol-buffers/docs/proto3#json>`__.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
