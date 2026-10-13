---
url: https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/summary_class/
title: Package Classes (2.52.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:46:15.431398+00:00
---

# Package Classes (2.52.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/summary_class/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package Classes (2.52.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.52.0 (latest)  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.2  2.40.0  2.39.1  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.30.2  2.29.0  2.28.3  2.27.0  2.26.0  2.25.0  2.24.1  2.23.3  2.22.0  2.21.0  2.20.0  2.19.1  2.18.0  2.17.0  2.16.1  2.15.2  2.14.1  2.13.0  2.12.0  2.11.0  2.10.0  2.9.1  2.8.1  2.7.1  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.2  2.0.0  1.1.3  1.0.0  0.8.0  0.7.2 

Summary of entries of Classes for dialogflow.

## Classes 

### [AgentsAsyncClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.agents.AgentsAsyncClient)

Service for managing Agents.

### [AgentsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.agents.AgentsClient)

Service for managing Agents.

### [SearchAgentsAsyncPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.agents.pagers.SearchAgentsAsyncPager)

A pager for iterating through `search_agents` requests.

This class thinly wraps an initial [SearchAgentsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SearchAgentsResponse) object, and provides an `__aiter__` method to iterate through its `agents` field.

If there are more pages, the `__aiter__` method will make additional `SearchAgents` requests and continue to iterate through the `agents` field on the corresponding responses.

All the usual [SearchAgentsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SearchAgentsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [SearchAgentsPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.agents.pagers.SearchAgentsPager)

A pager for iterating through `search_agents` requests.

This class thinly wraps an initial [SearchAgentsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SearchAgentsResponse) object, and provides an `__iter__` method to iterate through its `agents` field.

If there are more pages, the `__iter__` method will make additional `SearchAgents` requests and continue to iterate through the `agents` field on the corresponding responses.

All the usual [SearchAgentsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SearchAgentsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [AnswerRecordsAsyncClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.answer_records.AnswerRecordsAsyncClient)

Service for managing AnswerRecords.

### [AnswerRecordsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.answer_records.AnswerRecordsClient)

Service for managing AnswerRecords.

### [ListAnswerRecordsAsyncPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.answer_records.pagers.ListAnswerRecordsAsyncPager)

A pager for iterating through `list_answer_records` requests.

This class thinly wraps an initial [ListAnswerRecordsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListAnswerRecordsResponse) object, and provides an `__aiter__` method to iterate through its `answer_records` field.

If there are more pages, the `__aiter__` method will make additional `ListAnswerRecords` requests and continue to iterate through the `answer_records` field on the corresponding responses.

All the usual [ListAnswerRecordsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListAnswerRecordsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListAnswerRecordsPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.answer_records.pagers.ListAnswerRecordsPager)

A pager for iterating through `list_answer_records` requests.

This class thinly wraps an initial [ListAnswerRecordsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListAnswerRecordsResponse) object, and provides an `__iter__` method to iterate through its `answer_records` field.

If there are more pages, the `__iter__` method will make additional `ListAnswerRecords` requests and continue to iterate through the `answer_records` field on the corresponding responses.

All the usual [ListAnswerRecordsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListAnswerRecordsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [CompanionAgentsAsyncClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.companion_agents.CompanionAgentsAsyncClient)

Service for managing companion agents.

### [CompanionAgentsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.companion_agents.CompanionAgentsClient)

Service for managing companion agents.

### [ListCompanionAgentsAsyncPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.companion_agents.pagers.ListCompanionAgentsAsyncPager)

A pager for iterating through `list_companion_agents` requests.

This class thinly wraps an initial [ListCompanionAgentsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListCompanionAgentsResponse) object, and provides an `__aiter__` method to iterate through its `companion_agents` field.

If there are more pages, the `__aiter__` method will make additional `ListCompanionAgents` requests and continue to iterate through the `companion_agents` field on the corresponding responses.

All the usual [ListCompanionAgentsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListCompanionAgentsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListCompanionAgentsPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.companion_agents.pagers.ListCompanionAgentsPager)

A pager for iterating through `list_companion_agents` requests.

This class thinly wraps an initial [ListCompanionAgentsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListCompanionAgentsResponse) object, and provides an `__iter__` method to iterate through its `companion_agents` field.

If there are more pages, the `__iter__` method will make additional `ListCompanionAgents` requests and continue to iterate through the `companion_agents` field on the corresponding responses.

All the usual [ListCompanionAgentsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListCompanionAgentsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ContextsAsyncClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.contexts.ContextsAsyncClient)

Service for managing Contexts.

### [ContextsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.contexts.ContextsClient)

Service for managing Contexts.

### [ListContextsAsyncPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.contexts.pagers.ListContextsAsyncPager)

A pager for iterating through `list_contexts` requests.

This class thinly wraps an initial [ListContextsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListContextsResponse) object, and provides an `__aiter__` method to iterate through its `contexts` field.

If there are more pages, the `__aiter__` method will make additional `ListContexts` requests and continue to iterate through the `contexts` field on the corresponding responses.

All the usual [ListContextsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListContextsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListContextsPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.contexts.pagers.ListContextsPager)

A pager for iterating through `list_contexts` requests.

This class thinly wraps an initial [ListContextsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListContextsResponse) object, and provides an `__iter__` method to iterate through its `contexts` field.

If there are more pages, the `__iter__` method will make additional `ListContexts` requests and continue to iterate through the `contexts` field on the corresponding responses.

All the usual [ListContextsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListContextsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ConversationDatasetsAsyncClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.conversation_datasets.ConversationDatasetsAsyncClient)

Conversation datasets.

Conversation datasets contain raw conversation files and their customizable metadata that can be used for model training.

### [ConversationDatasetsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.conversation_datasets.ConversationDatasetsClient)

Conversation datasets.

Conversation datasets contain raw conversation files and their customizable metadata that can be used for model training.

### [ListConversationDatasetsAsyncPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.conversation_datasets.pagers.ListConversationDatasetsAsyncPager)

A pager for iterating through `list_conversation_datasets` requests.

This class thinly wraps an initial [ListConversationDatasetsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListConversationDatasetsResponse) object, and provides an `__aiter__` method to iterate through its `conversation_datasets` field.

If there are more pages, the `__aiter__` method will make additional `ListConversationDatasets` requests and continue to iterate through the `conversation_datasets` field on the corresponding responses.

All the usual [ListConversationDatasetsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListConversationDatasetsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListConversationDatasetsPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.conversation_datasets.pagers.ListConversationDatasetsPager)

A pager for iterating through `list_conversation_datasets` requests.

This class thinly wraps an initial [ListConversationDatasetsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListConversationDatasetsResponse) object, and provides an `__iter__` method to iterate through its `conversation_datasets` field.

If there are more pages, the `__iter__` method will make additional `ListConversationDatasets` requests and continue to iterate through the `conversation_datasets` field on the corresponding responses.

All the usual [ListConversationDatasetsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListConversationDatasetsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ConversationModelsAsyncClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.conversation_models.ConversationModelsAsyncClient)

Manages a collection of models for human agent assistant.

### [ConversationModelsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.conversation_models.ConversationModelsClient)

Manages a collection of models for human agent assistant.

### [ListConversationModelEvaluationsAsyncPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.conversation_models.pagers.ListConversationModelEvaluationsAsyncPager)

A pager for iterating through `list_conversation_model_evaluations` requests.

This class thinly wraps an initial [ListConversationModelEvaluationsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListConversationModelEvaluationsResponse) object, and provides an `__aiter__` method to iterate through its `conversation_model_evaluations` field.

If there are more pages, the `__aiter__` method will make additional `ListConversationModelEvaluations` requests and continue to iterate through the `conversation_model_evaluations` field on the corresponding responses.

All the usual [ListConversationModelEvaluationsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListConversationModelEvaluationsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListConversationModelEvaluationsPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.conversation_models.pagers.ListConversationModelEvaluationsPager)

A pager for iterating through `list_conversation_model_evaluations` requests.

This class thinly wraps an initial [ListConversationModelEvaluationsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListConversationModelEvaluationsResponse) object, and provides an `__iter__` method to iterate through its `conversation_model_evaluations` field.

If there are more pages, the `__iter__` method will make additional `ListConversationModelEvaluations` requests and continue to iterate through the `conversation_model_evaluations` field on the corresponding responses.

All the usual [ListConversationModelEvaluationsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListConversationModelEvaluationsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListConversationModelsAsyncPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.conversation_models.pagers.ListConversationModelsAsyncPager)

A pager for iterating through `list_conversation_models` requests.

This class thinly wraps an initial [ListConversationModelsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListConversationModelsResponse) object, and provides an `__aiter__` method to iterate through its `conversation_models` field.

If there are more pages, the `__aiter__` method will make additional `ListConversationModels` requests and continue to iterate through the `conversation_models` field on the corresponding responses.

All the usual [ListConversationModelsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListConversationModelsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListConversationModelsPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.conversation_models.pagers.ListConversationModelsPager)

A pager for iterating through `list_conversation_models` requests.

This class thinly wraps an initial [ListConversationModelsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListConversationModelsResponse) object, and provides an `__iter__` method to iterate through its `conversation_models` field.

If there are more pages, the `__iter__` method will make additional `ListConversationModels` requests and continue to iterate through the `conversation_models` field on the corresponding responses.

All the usual [ListConversationModelsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListConversationModelsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ConversationProfilesAsyncClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.conversation_profiles.ConversationProfilesAsyncClient)

Service for managing ConversationProfiles.

### [ConversationProfilesClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.conversation_profiles.ConversationProfilesClient)

Service for managing ConversationProfiles.

### [ListConversationProfilesAsyncPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.conversation_profiles.pagers.ListConversationProfilesAsyncPager)

A pager for iterating through `list_conversation_profiles` requests.

This class thinly wraps an initial [ListConversationProfilesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListConversationProfilesResponse) object, and provides an `__aiter__` method to iterate through its `conversation_profiles` field.

If there are more pages, the `__aiter__` method will make additional `ListConversationProfiles` requests and continue to iterate through the `conversation_profiles` field on the corresponding responses.

All the usual [ListConversationProfilesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListConversationProfilesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListConversationProfilesPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.conversation_profiles.pagers.ListConversationProfilesPager)

A pager for iterating through `list_conversation_profiles` requests.

This class thinly wraps an initial [ListConversationProfilesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListConversationProfilesResponse) object, and provides an `__iter__` method to iterate through its `conversation_profiles` field.

If there are more pages, the `__iter__` method will make additional `ListConversationProfiles` requests and continue to iterate through the `conversation_profiles` field on the corresponding responses.

All the usual [ListConversationProfilesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListConversationProfilesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ConversationsAsyncClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.conversations.ConversationsAsyncClient)

Service for managing Conversations.

### [ConversationsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.conversations.ConversationsClient)

Service for managing Conversations.

### [ListConversationsAsyncPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.conversations.pagers.ListConversationsAsyncPager)

A pager for iterating through `list_conversations` requests.

This class thinly wraps an initial [ListConversationsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListConversationsResponse) object, and provides an `__aiter__` method to iterate through its `conversations` field.

If there are more pages, the `__aiter__` method will make additional `ListConversations` requests and continue to iterate through the `conversations` field on the corresponding responses.

All the usual [ListConversationsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListConversationsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListConversationsPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.conversations.pagers.ListConversationsPager)

A pager for iterating through `list_conversations` requests.

This class thinly wraps an initial [ListConversationsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListConversationsResponse) object, and provides an `__iter__` method to iterate through its `conversations` field.

If there are more pages, the `__iter__` method will make additional `ListConversations` requests and continue to iterate through the `conversations` field on the corresponding responses.

All the usual [ListConversationsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListConversationsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListMessagesAsyncPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.conversations.pagers.ListMessagesAsyncPager)

A pager for iterating through `list_messages` requests.

This class thinly wraps an initial [ListMessagesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListMessagesResponse) object, and provides an `__aiter__` method to iterate through its `messages` field.

If there are more pages, the `__aiter__` method will make additional `ListMessages` requests and continue to iterate through the `messages` field on the corresponding responses.

All the usual [ListMessagesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListMessagesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListMessagesPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.conversations.pagers.ListMessagesPager)

A pager for iterating through `list_messages` requests.

This class thinly wraps an initial [ListMessagesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListMessagesResponse) object, and provides an `__iter__` method to iterate through its `messages` field.

If there are more pages, the `__iter__` method will make additional `ListMessages` requests and continue to iterate through the `messages` field on the corresponding responses.

All the usual [ListMessagesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListMessagesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [DocumentsAsyncClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.documents.DocumentsAsyncClient)

Service for managing knowledge Documents.

### [DocumentsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.documents.DocumentsClient)

Service for managing knowledge Documents.

### [ListDocumentsAsyncPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.documents.pagers.ListDocumentsAsyncPager)

A pager for iterating through `list_documents` requests.

This class thinly wraps an initial [ListDocumentsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListDocumentsResponse) object, and provides an `__aiter__` method to iterate through its `documents` field.

If there are more pages, the `__aiter__` method will make additional `ListDocuments` requests and continue to iterate through the `documents` field on the corresponding responses.

All the usual [ListDocumentsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListDocumentsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListDocumentsPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.documents.pagers.ListDocumentsPager)

A pager for iterating through `list_documents` requests.

This class thinly wraps an initial [ListDocumentsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListDocumentsResponse) object, and provides an `__iter__` method to iterate through its `documents` field.

If there are more pages, the `__iter__` method will make additional `ListDocuments` requests and continue to iterate through the `documents` field on the corresponding responses.

All the usual [ListDocumentsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListDocumentsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [EncryptionSpecServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.encryption_spec_service.EncryptionSpecServiceAsyncClient)

Manages encryption spec settings for Dialogflow and Agent Assist.

### [EncryptionSpecServiceClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.encryption_spec_service.EncryptionSpecServiceClient)

Manages encryption spec settings for Dialogflow and Agent Assist.

### [EntityTypesAsyncClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.entity_types.EntityTypesAsyncClient)

Service for managing EntityTypes.

### [EntityTypesClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.entity_types.EntityTypesClient)

Service for managing EntityTypes.

### [ListEntityTypesAsyncPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.entity_types.pagers.ListEntityTypesAsyncPager)

A pager for iterating through `list_entity_types` requests.

This class thinly wraps an initial [ListEntityTypesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListEntityTypesResponse) object, and provides an `__aiter__` method to iterate through its `entity_types` field.

If there are more pages, the `__aiter__` method will make additional `ListEntityTypes` requests and continue to iterate through the `entity_types` field on the corresponding responses.

All the usual [ListEntityTypesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListEntityTypesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListEntityTypesPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.entity_types.pagers.ListEntityTypesPager)

A pager for iterating through `list_entity_types` requests.

This class thinly wraps an initial [ListEntityTypesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListEntityTypesResponse) object, and provides an `__iter__` method to iterate through its `entity_types` field.

If there are more pages, the `__iter__` method will make additional `ListEntityTypes` requests and continue to iterate through the `entity_types` field on the corresponding responses.

All the usual [ListEntityTypesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListEntityTypesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [EnvironmentsAsyncClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.environments.EnvironmentsAsyncClient)

Service for managing Environments.

### [EnvironmentsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.environments.EnvironmentsClient)

Service for managing Environments.

### [GetEnvironmentHistoryAsyncPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.environments.pagers.GetEnvironmentHistoryAsyncPager)

A pager for iterating through `get_environment_history` requests.

This class thinly wraps an initial [EnvironmentHistory](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.EnvironmentHistory) object, and provides an `__aiter__` method to iterate through its `entries` field.

If there are more pages, the `__aiter__` method will make additional `GetEnvironmentHistory` requests and continue to iterate through the `entries` field on the corresponding responses.

All the usual [EnvironmentHistory](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.EnvironmentHistory) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [GetEnvironmentHistoryPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.environments.pagers.GetEnvironmentHistoryPager)

A pager for iterating through `get_environment_history` requests.

This class thinly wraps an initial [EnvironmentHistory](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.EnvironmentHistory) object, and provides an `__iter__` method to iterate through its `entries` field.

If there are more pages, the `__iter__` method will make additional `GetEnvironmentHistory` requests and continue to iterate through the `entries` field on the corresponding responses.

All the usual [EnvironmentHistory](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.EnvironmentHistory) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListEnvironmentsAsyncPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.environments.pagers.ListEnvironmentsAsyncPager)

A pager for iterating through `list_environments` requests.

This class thinly wraps an initial [ListEnvironmentsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListEnvironmentsResponse) object, and provides an `__aiter__` method to iterate through its `environments` field.

If there are more pages, the `__aiter__` method will make additional `ListEnvironments` requests and continue to iterate through the `environments` field on the corresponding responses.

All the usual [ListEnvironmentsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListEnvironmentsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListEnvironmentsPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.environments.pagers.ListEnvironmentsPager)

A pager for iterating through `list_environments` requests.

This class thinly wraps an initial [ListEnvironmentsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListEnvironmentsResponse) object, and provides an `__iter__` method to iterate through its `environments` field.

If there are more pages, the `__iter__` method will make additional `ListEnvironments` requests and continue to iterate through the `environments` field on the corresponding responses.

All the usual [ListEnvironmentsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListEnvironmentsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [FulfillmentsAsyncClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.fulfillments.FulfillmentsAsyncClient)

Service for managing Fulfillments.

### [FulfillmentsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.fulfillments.FulfillmentsClient)

Service for managing Fulfillments.

### [GeneratorEvaluationsAsyncClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.generator_evaluations.GeneratorEvaluationsAsyncClient)

Service for managing generator evaluations.

### [GeneratorEvaluationsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.generator_evaluations.GeneratorEvaluationsClient)

Service for managing generator evaluations.

### [ListGeneratorEvaluationsAsyncPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.generator_evaluations.pagers.ListGeneratorEvaluationsAsyncPager)

A pager for iterating through `list_generator_evaluations` requests.

This class thinly wraps an initial [ListGeneratorEvaluationsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListGeneratorEvaluationsResponse) object, and provides an `__aiter__` method to iterate through its `generator_evaluations` field.

If there are more pages, the `__aiter__` method will make additional `ListGeneratorEvaluations` requests and continue to iterate through the `generator_evaluations` field on the corresponding responses.

All the usual [ListGeneratorEvaluationsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListGeneratorEvaluationsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListGeneratorEvaluationsPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.generator_evaluations.pagers.ListGeneratorEvaluationsPager)

A pager for iterating through `list_generator_evaluations` requests.

This class thinly wraps an initial [ListGeneratorEvaluationsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListGeneratorEvaluationsResponse) object, and provides an `__iter__` method to iterate through its `generator_evaluations` field.

If there are more pages, the `__iter__` method will make additional `ListGeneratorEvaluations` requests and continue to iterate through the `generator_evaluations` field on the corresponding responses.

All the usual [ListGeneratorEvaluationsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListGeneratorEvaluationsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [GeneratorsAsyncClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.generators.GeneratorsAsyncClient)

Generator Service for LLM powered Agent Assist. This service manages the configurations of user owned Generators, such as description, context and instruction, input/output format, etc. The generator resources will be used inside a conversation and will be triggered by TriggerEvent to query LLM for answers.

### [GeneratorsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.generators.GeneratorsClient)

Generator Service for LLM powered Agent Assist. This service manages the configurations of user owned Generators, such as description, context and instruction, input/output format, etc. The generator resources will be used inside a conversation and will be triggered by TriggerEvent to query LLM for answers.

### [ListGeneratorsAsyncPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.generators.pagers.ListGeneratorsAsyncPager)

A pager for iterating through `list_generators` requests.

This class thinly wraps an initial [ListGeneratorsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListGeneratorsResponse) object, and provides an `__aiter__` method to iterate through its `generators` field.

If there are more pages, the `__aiter__` method will make additional `ListGenerators` requests and continue to iterate through the `generators` field on the corresponding responses.

All the usual [ListGeneratorsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListGeneratorsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListGeneratorsPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.generators.pagers.ListGeneratorsPager)

A pager for iterating through `list_generators` requests.

This class thinly wraps an initial [ListGeneratorsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListGeneratorsResponse) object, and provides an `__iter__` method to iterate through its `generators` field.

If there are more pages, the `__iter__` method will make additional `ListGenerators` requests and continue to iterate through the `generators` field on the corresponding responses.

All the usual [ListGeneratorsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListGeneratorsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [IntentsAsyncClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.intents.IntentsAsyncClient)

Service for managing Intents.

### [IntentsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.intents.IntentsClient)

Service for managing Intents.

### [ListIntentsAsyncPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.intents.pagers.ListIntentsAsyncPager)

A pager for iterating through `list_intents` requests.

This class thinly wraps an initial [ListIntentsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListIntentsResponse) object, and provides an `__aiter__` method to iterate through its `intents` field.

If there are more pages, the `__aiter__` method will make additional `ListIntents` requests and continue to iterate through the `intents` field on the corresponding responses.

All the usual [ListIntentsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListIntentsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListIntentsPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.intents.pagers.ListIntentsPager)

A pager for iterating through `list_intents` requests.

This class thinly wraps an initial [ListIntentsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListIntentsResponse) object, and provides an `__iter__` method to iterate through its `intents` field.

If there are more pages, the `__iter__` method will make additional `ListIntents` requests and continue to iterate through the `intents` field on the corresponding responses.

All the usual [ListIntentsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListIntentsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [KnowledgeBasesAsyncClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.knowledge_bases.KnowledgeBasesAsyncClient)

Service for managing KnowledgeBases.

### [KnowledgeBasesClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.knowledge_bases.KnowledgeBasesClient)

Service for managing KnowledgeBases.

### [ListKnowledgeBasesAsyncPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.knowledge_bases.pagers.ListKnowledgeBasesAsyncPager)

A pager for iterating through `list_knowledge_bases` requests.

This class thinly wraps an initial [ListKnowledgeBasesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListKnowledgeBasesResponse) object, and provides an `__aiter__` method to iterate through its `knowledge_bases` field.

If there are more pages, the `__aiter__` method will make additional `ListKnowledgeBases` requests and continue to iterate through the `knowledge_bases` field on the corresponding responses.

All the usual [ListKnowledgeBasesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListKnowledgeBasesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListKnowledgeBasesPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.knowledge_bases.pagers.ListKnowledgeBasesPager)

A pager for iterating through `list_knowledge_bases` requests.

This class thinly wraps an initial [ListKnowledgeBasesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListKnowledgeBasesResponse) object, and provides an `__iter__` method to iterate through its `knowledge_bases` field.

If there are more pages, the `__iter__` method will make additional `ListKnowledgeBases` requests and continue to iterate through the `knowledge_bases` field on the corresponding responses.

All the usual [ListKnowledgeBasesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListKnowledgeBasesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ParticipantsAsyncClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.participants.ParticipantsAsyncClient)

Service for managing Participants.

### [ParticipantsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.participants.ParticipantsClient)

Service for managing Participants.

### [ListParticipantsAsyncPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.participants.pagers.ListParticipantsAsyncPager)

A pager for iterating through `list_participants` requests.

This class thinly wraps an initial [ListParticipantsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListParticipantsResponse) object, and provides an `__aiter__` method to iterate through its `participants` field.

If there are more pages, the `__aiter__` method will make additional `ListParticipants` requests and continue to iterate through the `participants` field on the corresponding responses.

All the usual [ListParticipantsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListParticipantsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListParticipantsPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.participants.pagers.ListParticipantsPager)

A pager for iterating through `list_participants` requests.

This class thinly wraps an initial [ListParticipantsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListParticipantsResponse) object, and provides an `__iter__` method to iterate through its `participants` field.

If there are more pages, the `__iter__` method will make additional `ListParticipants` requests and continue to iterate through the `participants` field on the corresponding responses.

All the usual [ListParticipantsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListParticipantsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [SessionEntityTypesAsyncClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.session_entity_types.SessionEntityTypesAsyncClient)

Service for managing SessionEntityTypes.

### [SessionEntityTypesClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.session_entity_types.SessionEntityTypesClient)

Service for managing SessionEntityTypes.

### [ListSessionEntityTypesAsyncPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.session_entity_types.pagers.ListSessionEntityTypesAsyncPager)

A pager for iterating through `list_session_entity_types` requests.

This class thinly wraps an initial [ListSessionEntityTypesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListSessionEntityTypesResponse) object, and provides an `__aiter__` method to iterate through its `session_entity_types` field.

If there are more pages, the `__aiter__` method will make additional `ListSessionEntityTypes` requests and continue to iterate through the `session_entity_types` field on the corresponding responses.

All the usual [ListSessionEntityTypesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListSessionEntityTypesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListSessionEntityTypesPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.session_entity_types.pagers.ListSessionEntityTypesPager)

A pager for iterating through `list_session_entity_types` requests.

This class thinly wraps an initial [ListSessionEntityTypesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListSessionEntityTypesResponse) object, and provides an `__iter__` method to iterate through its `session_entity_types` field.

If there are more pages, the `__iter__` method will make additional `ListSessionEntityTypes` requests and continue to iterate through the `session_entity_types` field on the corresponding responses.

All the usual [ListSessionEntityTypesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListSessionEntityTypesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [SessionsAsyncClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.sessions.SessionsAsyncClient)

A service used for session interactions.

For more information, see the `API interactions guide <https://cloud.google.com/dialogflow/docs/api-overview>`__.

### [SessionsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.sessions.SessionsClient)

A service used for session interactions.

For more information, see the `API interactions guide <https://cloud.google.com/dialogflow/docs/api-overview>`__.

### [SipTrunksAsyncClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.sip_trunks.SipTrunksAsyncClient)

Service for managing SipTrunks.

### [SipTrunksClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.sip_trunks.SipTrunksClient)

Service for managing SipTrunks.

### [ListSipTrunksAsyncPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.sip_trunks.pagers.ListSipTrunksAsyncPager)

A pager for iterating through `list_sip_trunks` requests.

This class thinly wraps an initial [ListSipTrunksResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListSipTrunksResponse) object, and provides an `__aiter__` method to iterate through its `sip_trunks` field.

If there are more pages, the `__aiter__` method will make additional `ListSipTrunks` requests and continue to iterate through the `sip_trunks` field on the corresponding responses.

All the usual [ListSipTrunksResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListSipTrunksResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListSipTrunksPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.sip_trunks.pagers.ListSipTrunksPager)

A pager for iterating through `list_sip_trunks` requests.

This class thinly wraps an initial [ListSipTrunksResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListSipTrunksResponse) object, and provides an `__iter__` method to iterate through its `sip_trunks` field.

If there are more pages, the `__iter__` method will make additional `ListSipTrunks` requests and continue to iterate through the `sip_trunks` field on the corresponding responses.

All the usual [ListSipTrunksResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListSipTrunksResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ToolsAsyncClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.tools.ToolsAsyncClient)

Tool Service for LLM powered Agent Assist. Tools can be used to interact with remote APIs (e.g. fetching orders) to retrieve additional information as input to LLM.

### [ToolsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.tools.ToolsClient)

Tool Service for LLM powered Agent Assist. Tools can be used to interact with remote APIs (e.g. fetching orders) to retrieve additional information as input to LLM.

### [ListToolsAsyncPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.tools.pagers.ListToolsAsyncPager)

A pager for iterating through `list_tools` requests.

This class thinly wraps an initial [ListToolsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListToolsResponse) object, and provides an `__aiter__` method to iterate through its `tools` field.

If there are more pages, the `__aiter__` method will make additional `ListTools` requests and continue to iterate through the `tools` field on the corresponding responses.

All the usual [ListToolsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListToolsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListToolsPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.tools.pagers.ListToolsPager)

A pager for iterating through `list_tools` requests.

This class thinly wraps an initial [ListToolsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListToolsResponse) object, and provides an `__iter__` method to iterate through its `tools` field.

If there are more pages, the `__iter__` method will make additional `ListTools` requests and continue to iterate through the `tools` field on the corresponding responses.

All the usual [ListToolsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListToolsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [VersionsAsyncClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.versions.VersionsAsyncClient)

Service for managing Versions.

### [VersionsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.versions.VersionsClient)

Service for managing Versions.

### [ListVersionsAsyncPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.versions.pagers.ListVersionsAsyncPager)

A pager for iterating through `list_versions` requests.

This class thinly wraps an initial [ListVersionsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListVersionsResponse) object, and provides an `__aiter__` method to iterate through its `versions` field.

If there are more pages, the `__aiter__` method will make additional `ListVersions` requests and continue to iterate through the `versions` field on the corresponding responses.

All the usual [ListVersionsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListVersionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListVersionsPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.versions.pagers.ListVersionsPager)

A pager for iterating through `list_versions` requests.

This class thinly wraps an initial [ListVersionsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListVersionsResponse) object, and provides an `__iter__` method to iterate through its `versions` field.

If there are more pages, the `__iter__` method will make additional `ListVersions` requests and continue to iterate through the `versions` field on the corresponding responses.

All the usual [ListVersionsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListVersionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [Agent](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Agent)

A Dialogflow agent is a virtual agent that handles conversations with your end-users. It is a natural language understanding module that understands the nuances of human language. Dialogflow translates end-user text or audio during a conversation to structured data that your apps and services can understand. You design and build a Dialogflow agent to handle the types of conversations required for your system.

For more information about agents, see the `Agent guide <https://cloud.google.com/dialogflow/docs/agents-overview>`__.

### [ApiVersion](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Agent.ApiVersion)

API version for the agent.

### [MatchMode](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Agent.MatchMode)

Match mode determines how intents are detected from user queries.

### [Tier](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Agent.Tier)

Represents the agent tier.

### [AgentAssistantFeedback](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.AgentAssistantFeedback)

Detail feedback of Agent Assist result.

### [AnswerRelevance](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.AgentAssistantFeedback.AnswerRelevance)

Relevance of an answer.

### [CompanionFeedback](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.AgentAssistantFeedback.CompanionFeedback)

Feedback for companion agent.

### [DocumentCorrectness](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.AgentAssistantFeedback.DocumentCorrectness)

Correctness of document.

### [DocumentEfficiency](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.AgentAssistantFeedback.DocumentEfficiency)

Efficiency of document.

### [KnowledgeAssistFeedback](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.AgentAssistantFeedback.KnowledgeAssistFeedback)

Feedback for knowledge assist.

### [KnowledgeSearchFeedback](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.AgentAssistantFeedback.KnowledgeSearchFeedback)

Feedback for knowledge search.

### [SummarizationFeedback](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.AgentAssistantFeedback.SummarizationFeedback)

Feedback for conversation summarization.

### [TextSectionsEntry](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.AgentAssistantFeedback.SummarizationFeedback.TextSectionsEntry)

The abstract base class for a message.

### [AgentAssistantRecord](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.AgentAssistantRecord)

Represents a record of a human agent assist answer.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AgentCoachingContext](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.AgentCoachingContext)

Agent Coaching context that customer can configure.

### [AgentCoachingInstruction](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.AgentCoachingInstruction)

Agent Coaching instructions that customer can configure.

### [DuplicateCheckResult](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.AgentCoachingInstruction.DuplicateCheckResult)

Duplication check for the suggestion.

### [DuplicateSuggestion](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.AgentCoachingInstruction.DuplicateCheckResult.DuplicateSuggestion)

The duplicate suggestion details.

### [TriggerEvent](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.AgentCoachingInstruction.TriggerEvent)

The event that should trigger this instruction.

### [AgentCoachingSuggestion](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.AgentCoachingSuggestion)

Suggestion for coaching agents.

### [AgentActionSuggestion](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.AgentCoachingSuggestion.AgentActionSuggestion)

Actions suggested for the agent. This is based on applicable instructions.

### [DuplicateCheckResult](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.AgentCoachingSuggestion.DuplicateCheckResult)

Duplication check for the suggestion.

### [DuplicateSuggestion](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.AgentCoachingSuggestion.DuplicateCheckResult.DuplicateSuggestion)

The duplicate suggestion details. Keeping answer_record and sources together as they are identifiers for duplicate suggestions.

### [SampleResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.AgentCoachingSuggestion.SampleResponse)

Sample response that the agent can use. This could be based on applicable instructions and ingested data from other systems.

### [Sources](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.AgentCoachingSuggestion.Sources)

Sources for the suggestion.

### [AnalyzeContentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.AnalyzeContentRequest)

The request message for Participants.AnalyzeContent.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AnalyzeContentResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.AnalyzeContentResponse)

The response message for Participants.AnalyzeContent.

### [AnnotatedMessagePart](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.AnnotatedMessagePart)

Represents a part of a message possibly annotated with an entity. The part can be an entity or purely a part of the message between two entities or message start/end.

### [AnswerFeedback](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.AnswerFeedback)

Represents feedback the customer has about the quality & correctness of a certain answer in a conversation.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [CorrectnessLevel](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.AnswerFeedback.CorrectnessLevel)

The correctness level of an answer.

### [AnswerRecord](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.AnswerRecord)

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
  2. The customer uses the AnswerRecord.name to call the AnswerRecords.UpdateAnswerRecord method to send feedback about a specific answer that they believe is wrong.



.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ArticleAnswer](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ArticleAnswer)

Represents article answer.

### [MetadataEntry](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ArticleAnswer.MetadataEntry)

The abstract base class for a message.

### [ArticleSuggestionModelMetadata](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ArticleSuggestionModelMetadata)

Metadata for article suggestion models.

### [AssistQueryParameters](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.AssistQueryParameters)

Represents the parameters of human assist query.

### [DocumentsMetadataFiltersEntry](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.AssistQueryParameters.DocumentsMetadataFiltersEntry)

The abstract base class for a message.

### [AudioEncoding](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.AudioEncoding)

Audio encoding of the audio content sent in the conversational query request. Refer to the `Cloud Speech API documentation <https://cloud.google.com/speech-to-text/docs/basics>`__ for more details.

### [AudioInput](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.AudioInput)

Represents the natural language speech audio to be processed.

### [AutomatedAgentConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.AutomatedAgentConfig)

Defines the Automated Agent to connect to a conversation.

### [AutomatedAgentReply](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.AutomatedAgentReply)

Represents a response from an automated agent.

### [AutomatedAgentReplyType](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.AutomatedAgentReply.AutomatedAgentReplyType)

Represents different automated agent reply types.

### [BatchCreateEntitiesRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.BatchCreateEntitiesRequest)

The request message for EntityTypes.BatchCreateEntities.

### [BatchDeleteEntitiesRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.BatchDeleteEntitiesRequest)

The request message for EntityTypes.BatchDeleteEntities.

### [BatchDeleteEntityTypesRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.BatchDeleteEntityTypesRequest)

The request message for EntityTypes.BatchDeleteEntityTypes.

### [BatchDeleteIntentsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.BatchDeleteIntentsRequest)

The request message for Intents.BatchDeleteIntents.

### [BatchUpdateEntitiesRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.BatchUpdateEntitiesRequest)

The request message for EntityTypes.BatchUpdateEntities.

### [BatchUpdateEntityTypesRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.BatchUpdateEntityTypesRequest)

The request message for EntityTypes.BatchUpdateEntityTypes.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [BatchUpdateEntityTypesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.BatchUpdateEntityTypesResponse)

The response message for EntityTypes.BatchUpdateEntityTypes.

### [BatchUpdateIntentsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.BatchUpdateIntentsRequest)

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [BatchUpdateIntentsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.BatchUpdateIntentsResponse)

The response message for Intents.BatchUpdateIntents.

### [BidiStreamingAnalyzeContentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.BidiStreamingAnalyzeContentRequest)

The request message for Participants.BidiStreamingAnalyzeContent.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Config](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.BidiStreamingAnalyzeContentRequest.Config)

The config of the session.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [VoiceSessionConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.BidiStreamingAnalyzeContentRequest.Config.VoiceSessionConfig)

The config about how to process the audio for a voice-based session.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Input](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.BidiStreamingAnalyzeContentRequest.Input)

Input for the conversation.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [TurnInput](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.BidiStreamingAnalyzeContentRequest.TurnInput)

Input that forms data for a single turn.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [BidiStreamingAnalyzeContentResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.BidiStreamingAnalyzeContentResponse)

The response message for Participants.BidiStreamingAnalyzeContent.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [BargeInSignal](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.BidiStreamingAnalyzeContentResponse.BargeInSignal)

Indicate the user barge-in has been detected.

### [TurnComplete](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.BidiStreamingAnalyzeContentResponse.TurnComplete)

Indicate that the turn is complete.

### [CancelQuery](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.CancelQuery)

Message to signal cancellation of the current query turn. Cancels the currently active interactive query, not any query running in the background.

### [CesAppSpec](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.CesAppSpec)

Deprecated: Use `CesToolSpec` instead. Spec of CES app that the generator can choose from.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [CesToolSpec](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.CesToolSpec)

Spec of CES tool that the generator can choose from.

### [ClearSuggestionFeatureConfigOperationMetadata](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ClearSuggestionFeatureConfigOperationMetadata)

Metadata for a ConversationProfiles.ClearSuggestionFeatureConfig operation.

### [ClearSuggestionFeatureConfigRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ClearSuggestionFeatureConfigRequest)

The request message for ConversationProfiles.ClearSuggestionFeatureConfig.

### [CloudConversationDebuggingInfo](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.CloudConversationDebuggingInfo)

Cloud conversation info for easier debugging. It will get populated in `StreamingDetectIntentResponse` or `StreamingAnalyzeContentResponse` when the flag `enable_debugging_info` is set to true in corresponding requests.

### [CompanionAgent](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.CompanionAgent)

Companion agent.

### [GuidanceSkillConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.CompanionAgent.GuidanceSkillConfig)

Guidance skill configuration.

### [KnowledgeSource](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.CompanionAgent.KnowledgeSource)

Knowledge source configuration for knowledge retrieval.

### [SkillConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.CompanionAgent.SkillConfig)

Skill configuration for the companion agent.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [SkillTriggerEvent](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.CompanionAgent.SkillConfig.SkillTriggerEvent)

The event that should trigger the skill.

### [TranslationSkillConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.CompanionAgent.TranslationSkillConfig)

Translation skill configuration for the companion agent.

### [TriggerEvent](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.CompanionAgent.TriggerEvent)

Event that triggers companion agent skills and guidance instructions.

### [CompanionSuggestion](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.CompanionSuggestion)

Represents a companion suggestion answer.

### [Guidance](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.CompanionSuggestion.Guidance)

Represents guidance for companion suggestion.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [KnowledgeSource](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.CompanionSuggestion.Guidance.KnowledgeSource)

Represents a knowledge source for the guidance.

### [CompleteConversationRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.CompleteConversationRequest)

The request message for Conversations.CompleteConversation.

### [Connection](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Connection)

Represents a connection for SIP Trunk.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [CertificateState](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Connection.CertificateState)

The state of Sip Trunk certificate authentication.

### [ErrorDetails](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Connection.ErrorDetails)

The error details of Sip Trunk connection authentication.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [State](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Connection.State)

The state of Sip Trunk connection.

### [Context](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Context)

Dialogflow contexts are similar to natural language context. If a person says to you "they are orange", you need context in order to understand what "they" is referring to. Similarly, for Dialogflow to handle an end-user expression like that, it needs to be provided with context in order to correctly match an intent.

Using contexts, you can control the flow of a conversation. You can configure contexts for an intent by setting input and output contexts, which are identified by string names. When an intent is matched, any configured output contexts for that intent become active. While any contexts are active, Dialogflow is more likely to match intents that are configured with input contexts that correspond to the currently active contexts.

For more information about context, see the `Contexts guide <https://cloud.google.com/dialogflow/docs/contexts-overview>`__.

### [Conversation](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Conversation)

Represents a conversation. A conversation is an interaction between an agent, including live agents and Dialogflow agents, and a support customer. Conversations can include phone calls and text-based chat sessions.

### [ContextReference](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Conversation.ContextReference)

Represents a section of ingested context information.

### [ContextContent](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Conversation.ContextReference.ContextContent)

Contents ingested.

### [ContentFormat](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Conversation.ContextReference.ContextContent.ContentFormat)

Represents the format of the ingested string.

### [UpdateMode](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Conversation.ContextReference.UpdateMode)

Represents the mode in which context reference contents are updated.

### [ConversationStage](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Conversation.ConversationStage)

Enumeration of the different conversation stages a conversation can be in. Reference: <https://cloud.google.com/agent-assist/docs/basics#conversation_stages>

### [GeneratorContext](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Conversation.GeneratorContext)

Represents the context of a generator.

### [GeneratorType](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Conversation.GeneratorContext.GeneratorType)

The available generator types.

### [IngestedContextReferencesEntry](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Conversation.IngestedContextReferencesEntry)

The abstract base class for a message.

### [InitialGeneratorContextsEntry](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Conversation.InitialGeneratorContextsEntry)

The abstract base class for a message.

### [LifecycleState](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Conversation.LifecycleState)

Enumeration of the completion status of the conversation.

### [TelephonyConnectionInfo](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Conversation.TelephonyConnectionInfo)

The information about phone calls connected via phone gateway to the conversation.

### [MimeContent](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Conversation.TelephonyConnectionInfo.MimeContent)

The mime content from the initial SIP INVITE.

### [SipHeader](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Conversation.TelephonyConnectionInfo.SipHeader)

The SIP headers from the initial SIP INVITE.

### [ConversationContext](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ConversationContext)

Context of the conversation, including transcripts.

### [ConversationDataset](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ConversationDataset)

Represents a conversation dataset that a user imports raw data into. The data inside ConversationDataset can not be changed after ImportConversationData finishes (and calling ImportConversationData on a dataset that already has data is not allowed).

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ConversationEvent](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ConversationEvent)

Represents a notification sent to Pub/Sub subscribers for conversation lifecycle events.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Type](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ConversationEvent.Type)

Enumeration of the types of events available.
    
    
        In general non-recoverable errors only occur if something
        was misconfigured in the ConversationProfile corresponding
        to the call. After a non-recoverable error, Dialogflow may
        stop responding.
    
        We don't fire this event:
    
        - in an API call because we can directly return the error,
          or,
        - when we can recover from an error.
    

### [ConversationInfo](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ConversationInfo)

Represents metadata of a conversation.

### [ConversationModel](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ConversationModel)

Represents a conversation model.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ModelType](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ConversationModel.ModelType)

Model type.

### [State](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ConversationModel.State)

State of the model.

### [ConversationModelEvaluation](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ConversationModelEvaluation)

Represents evaluation result of a conversation model.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ConversationPhoneNumber](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ConversationPhoneNumber)

Represents a phone number for telephony integration. It allows for connecting a particular conversation over telephony.

### [ConversationProfile](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ConversationProfile)

Defines the services to connect to incoming Dialogflow conversations.

### [CreateCompanionAgentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.CreateCompanionAgentRequest)

Request of CreateCompanionAgent.

### [CreateContextRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.CreateContextRequest)

The request message for Contexts.CreateContext.

### [CreateConversationDatasetOperationMetadata](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.CreateConversationDatasetOperationMetadata)

Metadata for [CreateConversationDataset][].

### [CreateConversationDatasetRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.CreateConversationDatasetRequest)

The request message for ConversationDatasets.CreateConversationDataset.

### [CreateConversationModelEvaluationOperationMetadata](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.CreateConversationModelEvaluationOperationMetadata)

Metadata for a ConversationModels.CreateConversationModelEvaluation operation.

### [State](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.CreateConversationModelEvaluationOperationMetadata.State)

State of CreateConversationModel operation.

### [CreateConversationModelEvaluationRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.CreateConversationModelEvaluationRequest)

The request message for ConversationModels.CreateConversationModelEvaluation

### [CreateConversationModelOperationMetadata](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.CreateConversationModelOperationMetadata)

Metadata for a ConversationModels.CreateConversationModel operation.

### [State](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.CreateConversationModelOperationMetadata.State)

State of CreateConversationModel operation.

### [CreateConversationModelRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.CreateConversationModelRequest)

The request message for ConversationModels.CreateConversationModel

### [CreateConversationProfileRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.CreateConversationProfileRequest)

The request message for ConversationProfiles.CreateConversationProfile.

### [CreateConversationRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.CreateConversationRequest)

The request message for Conversations.CreateConversation.

### [CreateDocumentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.CreateDocumentRequest)

Request message for Documents.CreateDocument.

### [CreateEntityTypeRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.CreateEntityTypeRequest)

The request message for EntityTypes.CreateEntityType.

### [CreateEnvironmentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.CreateEnvironmentRequest)

The request message for Environments.CreateEnvironment.

### [CreateGeneratorEvaluationRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.CreateGeneratorEvaluationRequest)

Request of CreateGeneratorEvaluation.

### [CreateGeneratorRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.CreateGeneratorRequest)

Request message of CreateGenerator.

### [CreateIntentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.CreateIntentRequest)

The request message for Intents.CreateIntent.

### [CreateKnowledgeBaseRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.CreateKnowledgeBaseRequest)

Request message for KnowledgeBases.CreateKnowledgeBase.

### [CreateParticipantRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.CreateParticipantRequest)

The request message for Participants.CreateParticipant.

### [CreateSessionEntityTypeRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.CreateSessionEntityTypeRequest)

The request message for SessionEntityTypes.CreateSessionEntityType.

### [CreateSipTrunkRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.CreateSipTrunkRequest)

The request message for SipTrunks.CreateSipTrunk.

### [CreateToolRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.CreateToolRequest)

Request message of CreateTool.

### [CreateVersionRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.CreateVersionRequest)

The request message for Versions.CreateVersion.

### [CustomPronunciationParams](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.CustomPronunciationParams)

Pronunciation customization for a phrase.

### [PhoneticEncoding](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.CustomPronunciationParams.PhoneticEncoding)

The phonetic encoding of the phrase.

### [DatastoreResponseReason](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.DatastoreResponseReason)

Response reason from datastore which indicates data serving status or answer quality degradation.

### [DeleteAgentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.DeleteAgentRequest)

The request message for Agents.DeleteAgent.

### [DeleteAllContextsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.DeleteAllContextsRequest)

The request message for Contexts.DeleteAllContexts.

### [DeleteCompanionAgentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.DeleteCompanionAgentRequest)

Request message for DeleteCompanionAgent.

### [DeleteContextRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.DeleteContextRequest)

The request message for Contexts.DeleteContext.

### [DeleteConversationDatasetOperationMetadata](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.DeleteConversationDatasetOperationMetadata)

Metadata for [DeleteConversationDataset][].

### [DeleteConversationDatasetRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.DeleteConversationDatasetRequest)

The request message for ConversationDatasets.DeleteConversationDataset.

### [DeleteConversationModelOperationMetadata](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.DeleteConversationModelOperationMetadata)

Metadata for a ConversationModels.DeleteConversationModel operation.

### [DeleteConversationModelRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.DeleteConversationModelRequest)

The request message for ConversationModels.DeleteConversationModel

### [DeleteConversationProfileRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.DeleteConversationProfileRequest)

The request message for ConversationProfiles.DeleteConversationProfile.

This operation fails if the conversation profile is still referenced from a phone number.

### [DeleteDocumentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.DeleteDocumentRequest)

Request message for Documents.DeleteDocument.

### [DeleteEntityTypeRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.DeleteEntityTypeRequest)

The request message for EntityTypes.DeleteEntityType.

### [DeleteEnvironmentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.DeleteEnvironmentRequest)

The request message for Environments.DeleteEnvironment.

### [DeleteGeneratorEvaluationRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.DeleteGeneratorEvaluationRequest)

Request of DeleteGeneratorEvaluation.

### [DeleteGeneratorRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.DeleteGeneratorRequest)

Request of DeleteGenerator.

### [DeleteIntentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.DeleteIntentRequest)

The request message for Intents.DeleteIntent.

### [DeleteKnowledgeBaseRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.DeleteKnowledgeBaseRequest)

Request message for KnowledgeBases.DeleteKnowledgeBase.

### [DeleteSessionEntityTypeRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.DeleteSessionEntityTypeRequest)

The request message for SessionEntityTypes.DeleteSessionEntityType.

### [DeleteSipTrunkRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.DeleteSipTrunkRequest)

The request message for SipTrunks.DeleteSipTrunk.

### [DeleteToolRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.DeleteToolRequest)

Request of DeleteTool.

### [DeleteVersionRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.DeleteVersionRequest)

The request message for Versions.DeleteVersion.

### [DeployConversationModelOperationMetadata](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.DeployConversationModelOperationMetadata)

Metadata for a ConversationModels.DeployConversationModel operation.

### [DeployConversationModelRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.DeployConversationModelRequest)

The request message for ConversationModels.DeployConversationModel

### [DetectIntentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.DetectIntentRequest)

The request to detect user's intent.

### [DetectIntentResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.DetectIntentResponse)

The message returned from the [DetectIntent][] method.

### [DialogflowAssistAnswer](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.DialogflowAssistAnswer)

Represents a Dialogflow assist answer.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Document](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Document)

A knowledge document to be used by a KnowledgeBase.

For more information, see the `knowledge base guide <https://cloud.google.com/dialogflow/docs/how/knowledge-bases>`__.

Note: The `projects.agent.knowledgeBases.documents` resource is deprecated; only use `projects.knowledgeBases.documents`.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [KnowledgeType](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Document.KnowledgeType)

The knowledge type of document content.
    
    
        CSV must have questions in the first column and
        answers in the second, with no header. Because
        of this explicit format, they are always parsed
        accurately.
    EXTRACTIVE_QA (2):
        Documents for which unstructured text is
        extracted and used for question answering.
    ARTICLE_SUGGESTION (3):
        The entire document content as a whole can be
        used for query results. Only for Contact Center
        Solutions on Dialogflow.
    AGENT_FACING_SMART_REPLY (4):
        The document contains agent-facing Smart
        Reply entries.
    

### [MetadataEntry](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Document.MetadataEntry)

The abstract base class for a message.

### [ReloadStatus](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Document.ReloadStatus)

The status of a reload attempt.

### [State](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Document.State)

Possible states of the document

### [DtmfParameters](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.DtmfParameters)

The message in the response that indicates the parameters of DTMF.

### [EncryptionSpec](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.EncryptionSpec)

A customer-managed encryption key specification that can be applied to all created resources (e.g. Conversation).

### [EntityType](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.EntityType)

Each intent parameter has a type, called the entity type, which dictates exactly how data from an end-user expression is extracted.

Dialogflow provides predefined system entities that can match many common types of data. For example, there are system entities for matching dates, times, colors, email addresses, and so on. You can also create your own custom entities for matching custom data. For example, you could define a vegetable entity that can match the types of vegetables available for purchase with a grocery store agent.

For more information, see the `Entity guide <https://cloud.google.com/dialogflow/docs/entities-overview>`__.

### [AutoExpansionMode](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.EntityType.AutoExpansionMode)

Represents different entity type expansion modes. Automated expansion allows an agent to recognize values that have not been explicitly listed in the entity (for example, new kinds of shopping list items).

### [Entity](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.EntityType.Entity)

An **entity entry** for an associated entity type.

### [Kind](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.EntityType.Kind)

Represents kinds of entities.

### [EntityTypeBatch](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.EntityTypeBatch)

This message is a wrapper around a collection of entity types.

### [Environment](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Environment)

You can create multiple versions of your agent and publish them to separate environments.

When you edit an agent, you are editing the draft agent. At any point, you can save the draft agent as an agent version, which is an immutable snapshot of your agent.

When you save the draft agent, it is published to the default environment. When you create agent versions, you can publish them to custom environments. You can create a variety of custom environments for:

  * testing
  * development
  * production
  * etc.



For more information, see the `versions and environments guide <https://cloud.google.com/dialogflow/docs/agents-versions>`__.

### [State](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Environment.State)

Represents an environment state. When an environment is pointed to a new agent version, the environment is temporarily set to the `LOADING` state. During that time, the environment keeps on serving the previous version of the agent. After the new agent version is done loading, the environment is set back to the `RUNNING` state.

### [EnvironmentHistory](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.EnvironmentHistory)

The response message for Environments.GetEnvironmentHistory.

### [Entry](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.EnvironmentHistory.Entry)

Represents an environment history entry.

### [EvaluationConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.EvaluationConfig)

The configuration for model evaluation.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [SmartComposeConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.EvaluationConfig.SmartComposeConfig)

Smart compose specific configuration for evaluation job.

### [SmartReplyConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.EvaluationConfig.SmartReplyConfig)

Smart reply specific configuration for evaluation job.

### [EvaluationStatus](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.EvaluationStatus)

A common evalaution pipeline status.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [EventInput](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.EventInput)

Events allow for matching intents by event name instead of the natural language input. For instance, input `<event: { name: "welcome_event", parameters: { name: "Sam" } }>` can trigger a personalized welcome response. The parameter `name` may be used by the agent in the response: `"Hello #welcome_event.name! What can I do for you today?"`.

### [ExportAgentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ExportAgentRequest)

The request message for Agents.ExportAgent.

### [ExportAgentResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ExportAgentResponse)

The response message for Agents.ExportAgent.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ExportDocumentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ExportDocumentRequest)

Request message for Documents.ExportDocument.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ExportOperationMetadata](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ExportOperationMetadata)

Metadata related to the Export Data Operations (e.g. ExportDocument).

### [FaqAnswer](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.FaqAnswer)

Represents answer from "frequently asked questions".

### [MetadataEntry](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.FaqAnswer.MetadataEntry)

The abstract base class for a message.

### [FewShotExample](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.FewShotExample)

Providing examples in the generator (i.e. building a few-shot generator) helps convey the desired format of the LLM response.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ExtraInfoEntry](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.FewShotExample.ExtraInfoEntry)

The abstract base class for a message.

### [FreeFormContext](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.FreeFormContext)

Free form generator context that customer can configure.

### [FreeFormSuggestion](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.FreeFormSuggestion)

Suggestion generated using free form generator.

### [Fulfillment](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Fulfillment)

By default, your agent responds to a matched intent with a static response. As an alternative, you can provide a more dynamic response by using fulfillment. When you enable fulfillment for an intent, Dialogflow responds to that intent by calling a service that you define. For example, if an end-user wants to schedule a haircut on Friday, your service can check your database and respond to the end-user with availability information for Friday.

For more information, see the `fulfillment guide <https://cloud.google.com/dialogflow/docs/fulfillment-overview>`__.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Feature](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Fulfillment.Feature)

Whether fulfillment is enabled for the specific feature.

### [Type](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Fulfillment.Feature.Type)

The type of the feature.

### [GenericWebService](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Fulfillment.GenericWebService)

Represents configuration for a generic web service. Dialogflow supports two mechanisms for authentications:

  * Basic authentication with username and password.
  * Authentication with additional authentication headers.



More information could be found at:

<https://cloud.google.com/dialogflow/docs/fulfillment-configure>.

### [RequestHeadersEntry](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Fulfillment.GenericWebService.RequestHeadersEntry)

The abstract base class for a message.

### [GcsDestination](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.GcsDestination)

Google Cloud Storage location for the output.

### [GcsSources](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.GcsSources)

Google Cloud Storage location for the inputs.

### [GenerateCompanionSuggestionsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.GenerateCompanionSuggestionsResponse)

Represents the response message for GenerateCompanionSuggestions.

### [GenerateStatelessSuggestionRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.GenerateStatelessSuggestionRequest)

The request message for Conversations.GenerateStatelessSuggestion.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ContextReferencesEntry](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.GenerateStatelessSuggestionRequest.ContextReferencesEntry)

The abstract base class for a message.

### [GenerateStatelessSuggestionResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.GenerateStatelessSuggestionResponse)

The response message for Conversations.GenerateStatelessSuggestion.

### [GenerateStatelessSummaryRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.GenerateStatelessSummaryRequest)

The request message for Conversations.GenerateStatelessSummary.

### [MinimalConversation](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.GenerateStatelessSummaryRequest.MinimalConversation)

The minimum amount of information required to generate a Summary without having a Conversation resource created.

### [GenerateStatelessSummaryResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.GenerateStatelessSummaryResponse)

The response message for Conversations.GenerateStatelessSummary.

### [Summary](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.GenerateStatelessSummaryResponse.Summary)

Generated summary for a conversation.

### [TextSectionsEntry](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.GenerateStatelessSummaryResponse.Summary.TextSectionsEntry)

The abstract base class for a message.

### [GenerateSuggestionsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.GenerateSuggestionsRequest)

The request message for Conversations.GenerateSuggestions.

### [GenerateSuggestionsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.GenerateSuggestionsResponse)

The response message for Conversations.GenerateSuggestions.

### [GeneratorSuggestionAnswer](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.GenerateSuggestionsResponse.GeneratorSuggestionAnswer)

A GeneratorSuggestion answer.

### [Generator](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Generator)

LLM generator.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [GeneratorEvaluation](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.GeneratorEvaluation)

Represents evaluation result of a generator.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [GeneratorEvaluationConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.GeneratorEvaluationConfig)

Generator evaluation input config.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AgentAssistInputDataConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.GeneratorEvaluationConfig.AgentAssistInputDataConfig)

The distinctive configs for Agent Assist conversations as the conversation source.

### [DatasetInputDataConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.GeneratorEvaluationConfig.DatasetInputDataConfig)

The distinctive configs for dataset as the conversation source.

### [InputDataConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.GeneratorEvaluationConfig.InputDataConfig)

Input data config details

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [SummaryGenerationOption](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.GeneratorEvaluationConfig.InputDataConfig.SummaryGenerationOption)

Summary generation options.

### [InputDataSourceType](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.GeneratorEvaluationConfig.InputDataSourceType)

Enumeration of input data source type.

### [SummarizationConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.GeneratorEvaluationConfig.SummarizationConfig)

Evaluation configs for summarization generator.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [GeneratorEvaluationOperationMetadata](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.GeneratorEvaluationOperationMetadata)

Metadata for a GeneratorEvaluations.CreateGeneratorEvaluation operation.

### [GeneratorSuggestion](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.GeneratorSuggestion)

Suggestion generated using a Generator.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ToolCallInfo](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.GeneratorSuggestion.ToolCallInfo)

Request and response for a tool call.

### [GetAgentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.GetAgentRequest)

The request message for Agents.GetAgent.

### [GetCompanionAgentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.GetCompanionAgentRequest)

Request message for GetCompanionAgent.

### [GetContextRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.GetContextRequest)

The request message for Contexts.GetContext.

### [GetConversationDatasetRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.GetConversationDatasetRequest)

The request message for ConversationDatasets.GetConversationDataset.

### [GetConversationModelEvaluationRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.GetConversationModelEvaluationRequest)

The request message for ConversationModels.GetConversationModelEvaluation

### [GetConversationModelRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.GetConversationModelRequest)

The request message for ConversationModels.GetConversationModel

### [GetConversationProfileRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.GetConversationProfileRequest)

The request message for ConversationProfiles.GetConversationProfile.

### [GetConversationRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.GetConversationRequest)

The request message for Conversations.GetConversation.

### [GetDocumentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.GetDocumentRequest)

Request message for Documents.GetDocument.

### [GetEncryptionSpecRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.GetEncryptionSpecRequest)

The request to get location-level encryption specification.

### [GetEntityTypeRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.GetEntityTypeRequest)

The request message for EntityTypes.GetEntityType.

### [GetEnvironmentHistoryRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.GetEnvironmentHistoryRequest)

The request message for Environments.GetEnvironmentHistory.

### [GetEnvironmentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.GetEnvironmentRequest)

The request message for Environments.GetEnvironment.

### [GetFulfillmentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.GetFulfillmentRequest)

The request message for Fulfillments.GetFulfillment.

### [GetGeneratorEvaluationRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.GetGeneratorEvaluationRequest)

Request of GetGeneratorEvaluation.

### [GetGeneratorRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.GetGeneratorRequest)

Request message of GetGenerator.

### [GetIntentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.GetIntentRequest)

The request message for Intents.GetIntent.

### [GetKnowledgeBaseRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.GetKnowledgeBaseRequest)

Request message for KnowledgeBases.GetKnowledgeBase.

### [GetParticipantRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.GetParticipantRequest)

The request message for Participants.GetParticipant.

### [GetSessionEntityTypeRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.GetSessionEntityTypeRequest)

The request message for SessionEntityTypes.GetSessionEntityType.

### [GetSipTrunkRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.GetSipTrunkRequest)

The request message for SipTrunks.GetSipTrunk.

### [GetToolRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.GetToolRequest)

Request message of GetTool.

### [GetValidationResultRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.GetValidationResultRequest)

The request message for Agents.GetValidationResult.

### [GetVersionRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.GetVersionRequest)

The request message for Versions.GetVersion.

### [GroundingChunk](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.GroundingChunk)

A piece of evidence that supports a claim made by the model.

This is used to show a citation for a claim made by the model. It contains a reference to the source of the information.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [RetrievedContext](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.GroundingChunk.RetrievedContext)

Context retrieved from a data source to ground the model's response. This is used when a retrieval tool fetches information from a user-provided corpus or a public dataset.

### [Web](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.GroundingChunk.Web)

A `Web` chunk is a piece of evidence that comes from a web page. It contains the URI of the web page, the title of the page, and the domain of the page. This is used to provide the user with a link to the source of the information.

### [GroundingMetadata](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.GroundingMetadata)

Grounding metadata contains sources, citations, and search entry points used to ground a generated answer or suggestion.

### [GroundingSupport](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.GroundingSupport)

A collection of supporting references for a segment or part of the model's response.

### [GuidanceInstruction](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.GuidanceInstruction)

Guidance instruction for the companion agent.

### [Action](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.GuidanceInstruction.Action)

Actions to take, including agent action and system action (automation).

### [HumanAgentAssistantConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.HumanAgentAssistantConfig)

Defines the Human Agent Assist to connect to a conversation.

### [ConversationModelConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.HumanAgentAssistantConfig.ConversationModelConfig)

Custom conversation models used in agent assist feature.

Supported feature: ARTICLE_SUGGESTION, SMART_COMPOSE, SMART_REPLY, CONVERSATION_SUMMARIZATION

### [ConversationProcessConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.HumanAgentAssistantConfig.ConversationProcessConfig)

Config to process conversation.

### [MessageAnalysisConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.HumanAgentAssistantConfig.MessageAnalysisConfig)

Configuration for analyses to run on each conversation message.

### [SuggestionConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.HumanAgentAssistantConfig.SuggestionConfig)

Detail human agent assistant config.

### [SuggestionFeatureConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.HumanAgentAssistantConfig.SuggestionFeatureConfig)

Config for suggestion features.

### [SuggestionQueryConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.HumanAgentAssistantConfig.SuggestionQueryConfig)

Config for suggestion query.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ContextFilterSettings](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.HumanAgentAssistantConfig.SuggestionQueryConfig.ContextFilterSettings)

Settings that determine how to filter recent conversation context when generating suggestions.

### [DialogflowQuerySource](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.HumanAgentAssistantConfig.SuggestionQueryConfig.DialogflowQuerySource)

Dialogflow source setting.

Supported feature: DIALOGFLOW_ASSIST.

### [HumanAgentSideConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.HumanAgentAssistantConfig.SuggestionQueryConfig.DialogflowQuerySource.HumanAgentSideConfig)

The configuration used for human agent side Dialogflow assist suggestion.

### [DocumentQuerySource](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.HumanAgentAssistantConfig.SuggestionQueryConfig.DocumentQuerySource)

Document source settings.

Supported features: SMART_REPLY, SMART_COMPOSE.

### [KnowledgeBaseQuerySource](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.HumanAgentAssistantConfig.SuggestionQueryConfig.KnowledgeBaseQuerySource)

Knowledge base source settings.

Supported features: ARTICLE_SUGGESTION, FAQ.

### [Sections](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.HumanAgentAssistantConfig.SuggestionQueryConfig.Sections)

Custom sections to return when requesting a summary of a conversation. This is only supported when `baseline_model_version` == '2.0'.

Supported features: CONVERSATION_SUMMARIZATION, CONVERSATION_SUMMARIZATION_VOICE.

### [SectionType](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.HumanAgentAssistantConfig.SuggestionQueryConfig.Sections.SectionType)

Selectable sections to return when requesting a summary of a conversation.

### [SuggestionTriggerSettings](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.HumanAgentAssistantConfig.SuggestionTriggerSettings)

Settings of suggestion trigger.

### [HumanAgentAssistantEvent](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.HumanAgentAssistantEvent)

Represents a notification sent to Cloud Pub/Sub subscribers for human agent assistant events in a specific conversation.

### [HumanAgentHandoffConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.HumanAgentHandoffConfig)

Defines the hand off to a live agent, typically on which external agent service provider to connect to a conversation.

Currently, this feature is not general available, please contact Google to get access.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [LivePersonConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.HumanAgentHandoffConfig.LivePersonConfig)

Configuration specific to `LivePerson <https://www.liveperson.com>`__.

### [SalesforceLiveAgentConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.HumanAgentHandoffConfig.SalesforceLiveAgentConfig)

Configuration specific to Salesforce Live Agent.

### [ImportAgentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ImportAgentRequest)

The request message for Agents.ImportAgent.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ImportConversationDataOperationMetadata](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ImportConversationDataOperationMetadata)

Metadata for a ConversationDatasets.ImportConversationData operation.

### [ImportConversationDataOperationResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ImportConversationDataOperationResponse)

Response used for ConversationDatasets.ImportConversationData long running operation.

### [ImportConversationDataRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ImportConversationDataRequest)

The request message for ConversationDatasets.ImportConversationData.

### [ImportDocumentTemplate](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ImportDocumentTemplate)

The template used for importing documents.

### [MetadataEntry](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ImportDocumentTemplate.MetadataEntry)

The abstract base class for a message.

### [ImportDocumentsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ImportDocumentsRequest)

Request message for Documents.ImportDocuments.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ImportDocumentsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ImportDocumentsResponse)

Response message for Documents.ImportDocuments.

### [InferenceParameter](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.InferenceParameter)

The parameters of inference.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [IngestContextReferencesRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.IngestContextReferencesRequest)

The request message for [ConversationsService.IngestContextReferences][].

### [ContextReferencesEntry](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.IngestContextReferencesRequest.ContextReferencesEntry)

The abstract base class for a message.

### [IngestContextReferencesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.IngestContextReferencesResponse)

The response message for [ConversationsService.IngestContextReferences][].

### [IngestedContextReferencesEntry](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.IngestContextReferencesResponse.IngestedContextReferencesEntry)

The abstract base class for a message.

### [IngestedContextReferenceDebugInfo](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.IngestedContextReferenceDebugInfo)

Debug information related to ingested context reference.

### [IngestedParameterDebugInfo](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.IngestedContextReferenceDebugInfo.IngestedParameterDebugInfo)

Debug information related to ingested parameters from context reference.

### [IngestionStatus](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.IngestedContextReferenceDebugInfo.IngestedParameterDebugInfo.IngestionStatus)

Enum representing the various states of parameter ingestion.

### [InitializeEncryptionSpecMetadata](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.InitializeEncryptionSpecMetadata)

Metadata for initializing a location-level encryption specification.

### [InitializeEncryptionSpecRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.InitializeEncryptionSpecRequest)

The request to initialize a location-level encryption specification.

### [InitializeEncryptionSpecResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.InitializeEncryptionSpecResponse)

The response to initialize a location-level encryption specification.

### [InputAudioConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.InputAudioConfig)

Instructs the speech recognizer how to process the audio content.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [InputConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.InputConfig)

Represents the configuration of importing a set of conversation files in Google Cloud Storage.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [InputDataset](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.InputDataset)

InputDataset used to create model or do evaluation. NextID:5

### [InputTextConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.InputTextConfig)

Defines the language used in the input text.

### [Intent](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Intent)

An intent categorizes an end-user's intention for one conversation turn. For each agent, you define many intents, where your combined intents can handle a complete conversation. When an end-user writes or says something, referred to as an end-user expression or end-user input, Dialogflow matches the end-user input to the best intent in your agent. Matching an intent is also known as intent classification.

For more information, see the `intent guide <https://cloud.google.com/dialogflow/docs/intents-overview>`__.

### [FollowupIntentInfo](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Intent.FollowupIntentInfo)

Represents a single followup intent in the chain.

### [Message](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Intent.Message)

A rich response message. Corresponds to the intent `Response` field in the Dialogflow console. For more information, see `Rich response messages <https://cloud.google.com/dialogflow/docs/intents-rich-messages>`__.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [BasicCard](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Intent.Message.BasicCard)

The basic card message. Useful for displaying information.

### [Button](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Intent.Message.BasicCard.Button)

The button object that appears at the bottom of a card.

### [OpenUriAction](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Intent.Message.BasicCard.Button.OpenUriAction)

Opens the given URI.

### [BrowseCarouselCard](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Intent.Message.BrowseCarouselCard)

Browse Carousel Card for Actions on Google. <https://developers.google.com/actions/assistant/responses#browsing_carousel>

### [BrowseCarouselCardItem](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Intent.Message.BrowseCarouselCard.BrowseCarouselCardItem)

Browsing carousel tile

### [OpenUrlAction](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Intent.Message.BrowseCarouselCard.BrowseCarouselCardItem.OpenUrlAction)

Actions on Google action to open a given url.

### [UrlTypeHint](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Intent.Message.BrowseCarouselCard.BrowseCarouselCardItem.OpenUrlAction.UrlTypeHint)

Type of the URI.

### [ImageDisplayOptions](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Intent.Message.BrowseCarouselCard.ImageDisplayOptions)

Image display options for Actions on Google. This should be used for when the image's aspect ratio does not match the image container's aspect ratio.

### [Card](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Intent.Message.Card)

The card response message.

### [Button](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Intent.Message.Card.Button)

Contains information about a button.

### [CarouselSelect](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Intent.Message.CarouselSelect)

The card for presenting a carousel of options to select from.

### [Item](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Intent.Message.CarouselSelect.Item)

An item in the carousel.

### [ColumnProperties](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Intent.Message.ColumnProperties)

Column properties for TableCard.

### [HorizontalAlignment](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Intent.Message.ColumnProperties.HorizontalAlignment)

Text alignments within a cell.

### [Image](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Intent.Message.Image)

The image response message.

### [LinkOutSuggestion](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Intent.Message.LinkOutSuggestion)

The suggestion chip message that allows the user to jump out to the app or website associated with this agent.

### [ListSelect](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Intent.Message.ListSelect)

The card for presenting a list of options to select from.

### [Item](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Intent.Message.ListSelect.Item)

An item in the list.

### [MediaContent](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Intent.Message.MediaContent)

The media content card for Actions on Google.

### [ResponseMediaObject](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Intent.Message.MediaContent.ResponseMediaObject)

Response media object for media content card.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ResponseMediaType](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Intent.Message.MediaContent.ResponseMediaType)

Format of response media type.

### [Platform](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Intent.Message.Platform)

The rich response message integration platform. See `Integrations <https://cloud.google.com/dialogflow/docs/integrations>`__.

### [QuickReplies](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Intent.Message.QuickReplies)

The quick replies response message.

### [SelectItemInfo](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Intent.Message.SelectItemInfo)

Additional info about the select item for when it is triggered in a dialog.

### [SimpleResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Intent.Message.SimpleResponse)

The simple response message containing speech or text.

### [SimpleResponses](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Intent.Message.SimpleResponses)

The collection of simple response candidates. This message in `QueryResult.fulfillment_messages` and `WebhookResponse.fulfillment_messages` should contain only one `SimpleResponse`.

### [Suggestion](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Intent.Message.Suggestion)

The suggestion chip message that the user can tap to quickly post a reply to the conversation.

### [Suggestions](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Intent.Message.Suggestions)

The collection of suggestions.

### [TableCard](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Intent.Message.TableCard)

Table card for Actions on Google.

### [TableCardCell](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Intent.Message.TableCardCell)

Cell of TableCardRow.

### [TableCardRow](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Intent.Message.TableCardRow)

Row of TableCard.

### [Text](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Intent.Message.Text)

The text response message.

### [Parameter](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Intent.Parameter)

Represents intent parameters.

### [TrainingPhrase](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Intent.TrainingPhrase)

Represents an example that the agent is trained on.

### [Part](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Intent.TrainingPhrase.Part)

Represents a part of a training phrase.

### [Type](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Intent.TrainingPhrase.Type)

Represents different types of training phrases.

### [WebhookState](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Intent.WebhookState)

Represents the different states that webhooks can be in.

### [IntentBatch](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.IntentBatch)

This message is a wrapper around a collection of intents.

### [IntentSuggestion](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.IntentSuggestion)

Represents an intent suggestion.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [IntentView](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.IntentView)

Represents the options for views of an intent. An intent can be a sizable object. Therefore, we provide a resource view that does not return training phrases in the response by default.

### [KnowledgeAssistAnswer](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.KnowledgeAssistAnswer)

Represents a Knowledge Assist answer.

### [AdditionalSuggestedQueryResult](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.KnowledgeAssistAnswer.AdditionalSuggestedQueryResult)

Represents a single suggested query result.

### [KnowledgeAnswer](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.KnowledgeAssistAnswer.KnowledgeAnswer)

Represents an answer from Knowledge. Currently supports FAQ and Generative answers.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [EventSource](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.KnowledgeAssistAnswer.KnowledgeAnswer.EventSource)

Details about source of Event answer.

### [FaqSource](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.KnowledgeAssistAnswer.KnowledgeAnswer.FaqSource)

Details about source of FAQ answer.

### [GenerativeSource](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.KnowledgeAssistAnswer.KnowledgeAnswer.GenerativeSource)

Details about source of Generative answer.

### [Snippet](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.KnowledgeAssistAnswer.KnowledgeAnswer.GenerativeSource.Snippet)

Snippet Source for a Generative Prediction.

### [SuggestedQuery](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.KnowledgeAssistAnswer.SuggestedQuery)

Represents a suggested query.

### [SearchContext](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.KnowledgeAssistAnswer.SuggestedQuery.SearchContext)

Search context is information useful for knowledge search that helps enrich the query. Example: search_context { key: "application name" value: "DesignApp" }

### [KnowledgeAssistDebugInfo](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.KnowledgeAssistDebugInfo)

Debug information related to Knowledge Assist feature.

### [KnowledgeAssistBehavior](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.KnowledgeAssistDebugInfo.KnowledgeAssistBehavior)

Configured behaviors for Knowedge Assist.

### [QueryCategorizationFailureReason](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.KnowledgeAssistDebugInfo.QueryCategorizationFailureReason)

Reason for query categorization failure.

### [QueryGenerationDebugInfo](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.KnowledgeAssistDebugInfo.QueryGenerationDebugInfo)

Debug information and model metadata for query generation.

### [QueryGenerationFailureReason](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.KnowledgeAssistDebugInfo.QueryGenerationFailureReason)

Reason for query generation failure.
    
    
        1. The trigger_event is CUSTOMER_MESSAGE or UNSPECIFIED, but
           the last message is not from the customer.
        2. The trigger_event is AGENT_MESSAGE, but the last message
           is not from the agent.
    

### [KnowledgeBase](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.KnowledgeBase)

A knowledge base represents a collection of knowledge documents that you provide to Dialogflow. Your knowledge documents contain information that may be useful during conversations with end-users. Some Dialogflow features use knowledge bases when looking for a response to an end-user input.

For more information, see the `knowledge base guide <https://cloud.google.com/dialogflow/docs/how/knowledge-bases>`__.

Note: The `projects.agent.knowledgeBases` resource is deprecated; only use `projects.knowledgeBases`.

### [KnowledgeOperationMetadata](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.KnowledgeOperationMetadata)

Metadata in google::longrunning::Operation for Knowledge operations.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [State](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.KnowledgeOperationMetadata.State)

States of the operation.

### [ListAnswerRecordsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListAnswerRecordsRequest)

Request message for AnswerRecords.ListAnswerRecords.

### [ListAnswerRecordsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListAnswerRecordsResponse)

Response message for AnswerRecords.ListAnswerRecords.

### [ListCompanionAgentsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListCompanionAgentsRequest)

Request message for ListCompanionAgents.

### [ListCompanionAgentsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListCompanionAgentsResponse)

Response message for ListCompanionAgents.

### [ListContextsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListContextsRequest)

The request message for Contexts.ListContexts.

### [ListContextsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListContextsResponse)

The response message for Contexts.ListContexts.

### [ListConversationDatasetsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListConversationDatasetsRequest)

The request message for ConversationDatasets.ListConversationDatasets.

### [ListConversationDatasetsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListConversationDatasetsResponse)

The response message for ConversationDatasets.ListConversationDatasets.

### [ListConversationModelEvaluationsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListConversationModelEvaluationsRequest)

The request message for ConversationModels.ListConversationModelEvaluations

### [ListConversationModelEvaluationsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListConversationModelEvaluationsResponse)

The response message for ConversationModels.ListConversationModelEvaluations

### [ListConversationModelsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListConversationModelsRequest)

The request message for ConversationModels.ListConversationModels

### [ListConversationModelsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListConversationModelsResponse)

The response message for ConversationModels.ListConversationModels

### [ListConversationProfilesRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListConversationProfilesRequest)

The request message for ConversationProfiles.ListConversationProfiles.

### [ListConversationProfilesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListConversationProfilesResponse)

The response message for ConversationProfiles.ListConversationProfiles.

### [ListConversationsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListConversationsRequest)

The request message for Conversations.ListConversations.

### [ListConversationsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListConversationsResponse)

The response message for Conversations.ListConversations.

### [ListDocumentsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListDocumentsRequest)

Request message for Documents.ListDocuments.

### [ListDocumentsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListDocumentsResponse)

Response message for Documents.ListDocuments.

### [ListEntityTypesRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListEntityTypesRequest)

The request message for EntityTypes.ListEntityTypes.

### [ListEntityTypesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListEntityTypesResponse)

The response message for EntityTypes.ListEntityTypes.

### [ListEnvironmentsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListEnvironmentsRequest)

The request message for Environments.ListEnvironments.

### [ListEnvironmentsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListEnvironmentsResponse)

The response message for Environments.ListEnvironments.

### [ListGeneratorEvaluationsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListGeneratorEvaluationsRequest)

Request of ListGeneratorEvaluations.

### [ListGeneratorEvaluationsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListGeneratorEvaluationsResponse)

Response of ListGeneratorEvaluations.

### [ListGeneratorsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListGeneratorsRequest)

Request message of ListGenerators.

### [ListGeneratorsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListGeneratorsResponse)

Response of ListGenerators.

### [ListIntentsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListIntentsRequest)

The request message for Intents.ListIntents.

### [ListIntentsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListIntentsResponse)

The response message for Intents.ListIntents.

### [ListKnowledgeBasesRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListKnowledgeBasesRequest)

Request message for KnowledgeBases.ListKnowledgeBases.

### [ListKnowledgeBasesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListKnowledgeBasesResponse)

Response message for KnowledgeBases.ListKnowledgeBases.

### [ListMessagesRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListMessagesRequest)

The request message for Conversations.ListMessages.

### [ListMessagesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListMessagesResponse)

The response message for Conversations.ListMessages.

### [ListParticipantsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListParticipantsRequest)

The request message for Participants.ListParticipants.

### [ListParticipantsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListParticipantsResponse)

The response message for Participants.ListParticipants.

### [ListSessionEntityTypesRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListSessionEntityTypesRequest)

The request message for SessionEntityTypes.ListSessionEntityTypes.

### [ListSessionEntityTypesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListSessionEntityTypesResponse)

The response message for SessionEntityTypes.ListSessionEntityTypes.

### [ListSipTrunksRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListSipTrunksRequest)

The request message for SipTrunks.ListSipTrunks.

### [ListSipTrunksResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListSipTrunksResponse)

The response message for SipTrunks.ListSipTrunks.

### [ListToolsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListToolsRequest)

Request message of ListTools.

### [ListToolsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListToolsResponse)

Response of ListTools.

### [ListVersionsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListVersionsRequest)

The request message for Versions.ListVersions.

### [ListVersionsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ListVersionsResponse)

The response message for Versions.ListVersions.

### [LoggingConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.LoggingConfig)

Defines logging behavior for conversation lifecycle events.

### [Message](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Message)

Represents a message posted into a conversation.

### [MessageAnnotation](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.MessageAnnotation)

Represents the result of annotation for the message.

### [MessageEntry](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.MessageEntry)

Represents a message entry of a conversation.

### [Role](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.MessageEntry.Role)

Enumeration of the roles a participant can play in a conversation.

### [NotificationConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.NotificationConfig)

Defines notification behavior.

### [MessageFormat](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.NotificationConfig.MessageFormat)

Format of cloud pub/sub message.

### [OriginalDetectIntentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.OriginalDetectIntentRequest)

Represents the contents of the original request that was passed to the `[Streaming]DetectIntent` call.

### [OutputAudio](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.OutputAudio)

Represents the natural language speech audio to be played to the end user.

### [OutputAudioConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.OutputAudioConfig)

Instructs the speech synthesizer on how to generate the output audio content. If this audio config is supplied in a request, it overrides all existing text-to-speech settings applied to the agent.

### [OutputAudioEncoding](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.OutputAudioEncoding)

Audio encoding of the output audio format in Text-To-Speech.

### [Participant](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Participant)

Represents a conversation participant (human agent, virtual agent, end-user).

### [AgentDesktopSource](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Participant.AgentDesktopSource)

Enumeration of the Agent Desktop Source when using prebuilt Agent Assist integration modules.

### [DocumentsMetadataFiltersEntry](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Participant.DocumentsMetadataFiltersEntry)

The abstract base class for a message.

### [Role](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Participant.Role)

Enumeration of the roles a participant can play in a conversation.

### [QueryInput](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.QueryInput)

Represents the query input. It can contain either:

  1. An audio config which instructs the speech recognizer how to process the speech audio.

  2. A conversational query in the form of text.

  3. An event that specifies which intent to trigger.




This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [QueryParameters](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.QueryParameters)

Represents the parameters of the conversational query.

### [WebhookHeadersEntry](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.QueryParameters.WebhookHeadersEntry)

The abstract base class for a message.

### [QueryResult](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.QueryResult)

Represents the result of conversational query or event processing.

### [RaiSettings](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.RaiSettings)

Settings for Responsible AI checks.

### [RaiCategoryConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.RaiSettings.RaiCategoryConfig)

Configuration for a specific RAI category.

### [RaiCategory](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.RaiSettings.RaiCategoryConfig.RaiCategory)

Enum for RAI category.

### [SensitivityLevel](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.RaiSettings.RaiCategoryConfig.SensitivityLevel)

Enum for user-configurable sensitivity levels.
    
    
        - DANGEROUS_CONTENT: BLOCK_FEW
        - SEXUALLY_EXPLICIT: BLOCK_SOME
        - HARASSMENT: BLOCK_SOME
        - HATE_SPEECH: BLOCK_SOME
    BLOCK_MOST (1):
        Block most potentially sensitive responses.
    BLOCK_SOME (2):
        Block some potentially sensitive responses.
    BLOCK_FEW (3):
        Block a few potentially sensitive responses.
    BLOCK_NONE (4):
        No filtering for this category.
    

### [ReloadDocumentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ReloadDocumentRequest)

Request message for Documents.ReloadDocument.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [RestoreAgentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.RestoreAgentRequest)

The request message for Agents.RestoreAgent.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [SearchAgentsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SearchAgentsRequest)

The request message for Agents.SearchAgents.

### [SearchAgentsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SearchAgentsResponse)

The response message for Agents.SearchAgents.

### [SearchEntryPoint](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SearchEntryPoint)

A web search entry point that can be used to display search results.

### [SearchKnowledgeAnswer](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SearchKnowledgeAnswer)

Represents a SearchKnowledge answer.

### [AnswerSource](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SearchKnowledgeAnswer.AnswerSource)

The sources of the answers.

### [AnswerType](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SearchKnowledgeAnswer.AnswerType)

The type of the answer.

### [SearchKnowledgeDebugInfo](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SearchKnowledgeDebugInfo)

Debug information related to SearchKnowledge feature.

### [SearchKnowledgeBehavior](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SearchKnowledgeDebugInfo.SearchKnowledgeBehavior)

Configured behaviors for SearchKnowledge.

### [SearchKnowledgeRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SearchKnowledgeRequest)

The request message for Conversations.SearchKnowledge.

### [QuerySource](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SearchKnowledgeRequest.QuerySource)

The source of the query. We use QuerySource to distinguish queries directly entered by agents and suggested queries from Participants.SuggestKnowledgeAssist. If SUGGESTED_QUERY source is specified, we will treat it as a continuation of a SuggestKnowledgeAssist call.

### [SearchConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SearchKnowledgeRequest.SearchConfig)

Configuration specific to search queries with data stores.

### [BoostSpecs](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SearchKnowledgeRequest.SearchConfig.BoostSpecs)

Boost specifications for data stores.

### [BoostSpec](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SearchKnowledgeRequest.SearchConfig.BoostSpecs.BoostSpec)

Boost specification to boost certain documents. A copy of google.cloud.discoveryengine.v1main.BoostSpec, field documentation is available at <https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/BoostSpec>

### [ConditionBoostSpec](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SearchKnowledgeRequest.SearchConfig.BoostSpecs.BoostSpec.ConditionBoostSpec)

Boost applies to documents which match a condition.

### [BoostControlSpec](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SearchKnowledgeRequest.SearchConfig.BoostSpecs.BoostSpec.ConditionBoostSpec.BoostControlSpec)

Specification for custom ranking based on customer specified attribute value. It provides more controls for customized ranking than the simple (condition, boost) combination above.

### [AttributeType](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SearchKnowledgeRequest.SearchConfig.BoostSpecs.BoostSpec.ConditionBoostSpec.BoostControlSpec.AttributeType)

The attribute(or function) for which the custom ranking is to be applied.

### [ControlPoint](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SearchKnowledgeRequest.SearchConfig.BoostSpecs.BoostSpec.ConditionBoostSpec.BoostControlSpec.ControlPoint)

The control points used to define the curve. The curve defined through these control points can only be monotonically increasing or decreasing(constant values are acceptable).

### [InterpolationType](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SearchKnowledgeRequest.SearchConfig.BoostSpecs.BoostSpec.ConditionBoostSpec.BoostControlSpec.InterpolationType)

The interpolation type to be applied. Default will be linear (Piecewise Linear).

### [FilterSpecs](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SearchKnowledgeRequest.SearchConfig.FilterSpecs)

Filter specification for data store queries.

### [SearchKnowledgeResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SearchKnowledgeResponse)

The response message for Conversations.SearchKnowledge.

### [Segment](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Segment)

A segment of the content.

### [Sentiment](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Sentiment)

The sentiment, such as positive/negative feeling or association, for a unit of analysis, such as the query text. See: <https://cloud.google.com/natural-language/docs/basics#interpreting_sentiment_analysis_values> for how to interpret the result.

### [SentimentAnalysisRequestConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SentimentAnalysisRequestConfig)

Configures the types of sentiment analysis to perform.

### [SentimentAnalysisResult](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SentimentAnalysisResult)

The result of sentiment analysis. Sentiment analysis inspects user input and identifies the prevailing subjective opinion, especially to determine a user's attitude as positive, negative, or neutral. For [DetectIntent][], it needs to be configured in DetectIntentRequest.query_params. For [StreamingDetectIntent][], it needs to be configured in StreamingDetectIntentRequest.query_params. And for Participants.AnalyzeContent and Participants.StreamingAnalyzeContent, it needs to be configured in ConversationProfile.human_agent_assistant_config

### [ServiceLatency](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ServiceLatency)

Message to represent the latency of the service.

### [InternalServiceLatency](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ServiceLatency.InternalServiceLatency)

Message to represent the latency of an internal service.

### [SessionEntityType](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SessionEntityType)

A session represents a conversation between a Dialogflow agent and an end-user. You can create special entities, called session entities, during a session. Session entities can extend or replace custom entity types and only exist during the session that they were created for. All session data, including session entities, is stored by Dialogflow for 20 minutes.

For more information, see the `session entity guide <https://cloud.google.com/dialogflow/docs/entities-session>`__.

### [EntityOverrideMode](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SessionEntityType.EntityOverrideMode)

The types of modifications for a session entity type.
    
    
        Note: Even in this override mode calls to
        `ListSessionEntityTypes`, `GetSessionEntityType`,
        `CreateSessionEntityType` and `UpdateSessionEntityType`
        only return the additional entities added in this session
        entity type. If you want to get the supplemented list,
        please call
        <xref uid="google.cloud.dialogflow.v2.EntityTypes.GetEntityType">EntityTypes.GetEntityType</xref>
        on the custom entity type and merge.
    

### [SetAgentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SetAgentRequest)

The request message for Agents.SetAgent.

### [SetSuggestionFeatureConfigOperationMetadata](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SetSuggestionFeatureConfigOperationMetadata)

Metadata for a ConversationProfiles.SetSuggestionFeatureConfig operation.

### [SetSuggestionFeatureConfigRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SetSuggestionFeatureConfigRequest)

The request message for ConversationProfiles.SetSuggestionFeatureConfig.

### [SipConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SipConfig)

Defines the SIP configuration.

### [SipTrunk](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SipTrunk)

SipTrunk is the resource that represents a SIP trunk to connect to Google Telephony platform SIP trunking service.

### [SmartReplyAnswer](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SmartReplyAnswer)

Represents a smart reply answer.

### [SmartReplyMetrics](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SmartReplyMetrics)

The evaluation metrics for smart reply model.

### [TopNMetrics](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SmartReplyMetrics.TopNMetrics)

Evaluation metrics when retrieving `n` smart replies with the model.

### [SmartReplyModelMetadata](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SmartReplyModelMetadata)

Metadata for smart reply models.

### [SpeechContext](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SpeechContext)

Hints for the speech recognizer to help with recognition in a specific conversation state.

### [SpeechModelVariant](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SpeechModelVariant)

Variant of the specified [Speech model][google.cloud.dialogflow.v2.InputAudioConfig.model] to use.

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
          <xref uid="google.cloud.dialogflow.v2.InputAudioConfig.model">model</xref>
          and request language, Dialogflow falls back to the
          standard variant.
    
          The `Cloud Speech
          documentation <https://cloud.google.com/speech-to-text/docs/enhanced-models>`__
          describes which models have enhanced variants.
    
        - If the API caller isn't eligible for enhanced models,
          Dialogflow returns an error. Please see the `Dialogflow
          docs <https://cloud.google.com/dialogflow/docs/data-logging>`__
          for how to make your project eligible.
    

### [SpeechToTextConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SpeechToTextConfig)

Configures speech transcription for ConversationProfile.

### [GeminiAsrConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SpeechToTextConfig.GeminiAsrConfig)

Configuration for using Gemini ASR models served via Vertex AI. This message is used to override the default Gemini ASR model or provide additional advanced parameters.

### [EndSensitivity](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SpeechToTextConfig.GeminiAsrConfig.EndSensitivity)

End of speech sensitivity.

### [StartSensitivity](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SpeechToTextConfig.GeminiAsrConfig.StartSensitivity)

Start of speech sensitivity.

### [SpeechWordInfo](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SpeechWordInfo)

Information for a word recognized by the speech recognizer.

### [SsmlVoiceGender](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SsmlVoiceGender)

Gender of the voice as described in `SSML voice element <https://www.w3.org/TR/speech-synthesis11/#edef_voice>`__.

### [StreamingAnalyzeContentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.StreamingAnalyzeContentRequest)

The top-level message sent by the client to the Participants.StreamingAnalyzeContent method.

Multiple request messages should be sent in order:

  1. The first message must contain participant, config and optionally query_params. If you want to receive an audio response, it should also contain reply_audio_config. The message must not contain input.

  2. If config in the first message was set to audio_config, all subsequent messages must contain input_audio to continue with Speech recognition. However, note that:

     * Dialogflow will bill you for the audio so far.
     * Dialogflow discards all Speech recognition results in favor of the text input.
  3. If StreamingAnalyzeContentRequest.config in the first message was set to StreamingAnalyzeContentRequest.text_config, then the second message must contain only input_text. Moreover, you must not send more than two messages.




After you sent all input, you must half-close or abort the request stream.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [StreamingAnalyzeContentResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.StreamingAnalyzeContentResponse)

The top-level message returned from the `StreamingAnalyzeContent` method.

Multiple response messages can be returned in order:

  1. If the input was set to streaming audio, the first one or more messages contain `recognition_result`. Each `recognition_result` represents a more complete transcript of what the user said. When a user speaks multiple sentences, the API will emit multiple messages where `is_final = true`. Each time the system detects a distinct pause or completed thought, it locks in that segment, marks it `is_final = true`, and then immediately starts a new recognition cycle for the next sentence on the same stream.

  2. In virtual agent stage: if `enable_partial_automated_agent_reply` is true, the following N (currently 1 <= N <= 4) messages contain `automated_agent_reply` and optionally `reply_audio` returned by the virtual agent. The first (N-1) `automated_agent_reply`\ s will have `automated_agent_reply_type` set to `PARTIAL`. The last `automated_agent_reply` has `automated_agent_reply_type` set to `FINAL`. If `enable_partial_automated_agent_reply` is not enabled, response stream only contains the final reply.

In human assist stage: the following N (N >= 1) messages contain `human_agent_suggestion_results`, `end_user_suggestion_results` or `message`.




### [StreamingDetectIntentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.StreamingDetectIntentRequest)

The top-level message sent by the client to the [StreamingDetectIntent][] method.

Multiple request messages should be sent in order:

  1. The first message must contain session, query_input plus optionally query_params. If the client wants to receive an audio response, it should also contain output_audio_config. The message must not contain input_audio.

  2. If query_input was set to query_input.audio_config, all subsequent messages must contain input_audio to continue with Speech recognition. If you decide to rather detect an intent from text input after you already started Speech recognition, please send a message with query_input.text.

However, note that:

     * Dialogflow will bill you for the audio duration so far.
     * Dialogflow discards all Speech recognition results in favor of the input text.
     * Dialogflow will use the language code from the first message.



After you sent all input, you must half-close or abort the request stream.

### [StreamingDetectIntentResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.StreamingDetectIntentResponse)

The top-level message returned from the [StreamingDetectIntent][] method.

Multiple response messages can be returned in order:

  1. If the StreamingDetectIntentRequest.input_audio field was set, the `recognition_result` field is populated for one or more messages. See the StreamingRecognitionResult message for details about the result message sequence.

  2. The next message contains `response_id`, `query_result` and optionally `webhook_status` if a WebHook was called.




### [StreamingReactiveCompanionSuggestionsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.StreamingReactiveCompanionSuggestionsRequest)

The request message for Participants.StreamingReactiveCompanionSuggestions.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [StreamingReactiveCompanionSuggestionsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.StreamingReactiveCompanionSuggestionsResponse)

The response message for Participants.StreamingReactiveCompanionSuggestions.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ReactiveModeResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.StreamingReactiveCompanionSuggestionsResponse.ReactiveModeResponse)

The complete response generated by the reactive mode capturing the entire accumulated streaming response, grounding metadata, and tool calls.

### [StreamingRecognitionResult](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.StreamingRecognitionResult)

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

### [MessageType](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.StreamingRecognitionResult.MessageType)

Type of the response message.

### [SuggestArticlesRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SuggestArticlesRequest)

The request message for Participants.SuggestArticles.

### [SuggestArticlesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SuggestArticlesResponse)

The response message for Participants.SuggestArticles.

### [SuggestConversationSummaryRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SuggestConversationSummaryRequest)

The request message for Conversations.SuggestConversationSummary.

### [SuggestConversationSummaryResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SuggestConversationSummaryResponse)

The response message for Conversations.SuggestConversationSummary.

### [Summary](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SuggestConversationSummaryResponse.Summary)

Generated summary for a conversation.

### [SummarySection](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SuggestConversationSummaryResponse.Summary.SummarySection)

A component of the generated summary.

### [TextSectionsEntry](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SuggestConversationSummaryResponse.Summary.TextSectionsEntry)

The abstract base class for a message.

### [SuggestFaqAnswersRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SuggestFaqAnswersRequest)

The request message for Participants.SuggestFaqAnswers.

### [SuggestFaqAnswersResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SuggestFaqAnswersResponse)

The request message for Participants.SuggestFaqAnswers.

### [SuggestKnowledgeAssistRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SuggestKnowledgeAssistRequest)

The request message for Participants.SuggestKnowledgeAssist.

### [SuggestKnowledgeAssistResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SuggestKnowledgeAssistResponse)

The response message for Participants.SuggestKnowledgeAssist.

### [SuggestSmartRepliesRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SuggestSmartRepliesRequest)

The request message for Participants.SuggestSmartReplies.

### [SuggestSmartRepliesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SuggestSmartRepliesResponse)

The response message for Participants.SuggestSmartReplies.

### [SuggestionDedupingConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SuggestionDedupingConfig)

Config for suggestion deduping. NEXT_ID: 3

### [SuggestionFeature](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SuggestionFeature)

The type of Human Agent Assistant API suggestion to perform, and the maximum number of results to return for that type. Multiple `Feature` objects can be specified in the `features` list.

### [Type](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SuggestionFeature.Type)

Defines the type of Human Agent Assistant feature.

### [SuggestionInput](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SuggestionInput)

Represents the action to take for a tool call that requires confirmation.

### [Action](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SuggestionInput.Action)

Indicate what type of action to take with the tool call.

### [SuggestionResult](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SuggestionResult)

One response of different type of suggestion response which is used in the response of Participants.AnalyzeContent and Participants.AnalyzeContent, as well as HumanAgentAssistantEvent.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [SummarizationContext](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SummarizationContext)

Summarization context that customer can configure.

### [SummarizationEvaluationMetrics](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SummarizationEvaluationMetrics)

Evaluation metrics for summarization generator.

### [AccuracyDecomposition](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SummarizationEvaluationMetrics.AccuracyDecomposition)

Decomposition details for accuracy.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AdherenceDecomposition](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SummarizationEvaluationMetrics.AdherenceDecomposition)

Decomposition details for adherence.

### [AdherenceRubric](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SummarizationEvaluationMetrics.AdherenceRubric)

Rubric result of the adherence evaluation. A rubric is ued to determine if the summary adheres to all aspects of the given instructions.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [CompletenessRubric](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SummarizationEvaluationMetrics.CompletenessRubric)

Rubric details of the completeness evaluation result.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ConversationDetail](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SummarizationEvaluationMetrics.ConversationDetail)

Aggregated evaluation result on conversation level. This conatins evaluation results of all the metrics and sections.

### [MetricDetail](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SummarizationEvaluationMetrics.ConversationDetail.MetricDetail)

Aggregated result on metric level. This conatins the evaluation results of all the sections.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [SectionDetail](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SummarizationEvaluationMetrics.ConversationDetail.MetricDetail.SectionDetail)

Section level result.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Decomposition](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SummarizationEvaluationMetrics.Decomposition)

Decomposition details

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [EvaluationResult](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SummarizationEvaluationMetrics.EvaluationResult)

Evaluation result that contains one of accuracy, adherence or completeness evaluation result.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [OverallScoresByMetric](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SummarizationEvaluationMetrics.OverallScoresByMetric)

Overall performance per metric. This is the aggregated score for each metric across all conversations that are selected for summarization evaluation.

### [SectionToken](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SummarizationEvaluationMetrics.SectionToken)

A pair of section name and input token count of the input summary section.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [SummarizationEvaluationResult](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SummarizationEvaluationMetrics.SummarizationEvaluationResult)

Evaluation result per conversation(&summary), metric and section.

### [SummarizationSection](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SummarizationSection)

Represents the section of summarization.

### [Type](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SummarizationSection.Type)

Type enum of the summarization sections.

### [SummarizationSectionList](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SummarizationSectionList)

List of summarization sections.

### [SummarySuggestion](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SummarySuggestion)

Suggested summary of the conversation.

### [SummarySection](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SummarySuggestion.SummarySection)

A component of the generated summary.

### [SynthesizeSpeechConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.SynthesizeSpeechConfig)

Configuration of how speech should be synthesized.

### [TelephonyDtmf](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.TelephonyDtmf)

`DTMF <https://en.wikipedia.org/wiki/Dual-tone_multi-frequency_signaling>`__ digit in Telephony Gateway.

### [TelephonyDtmfEvents](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.TelephonyDtmfEvents)

A wrapper of repeated TelephonyDtmf digits.

### [TextInput](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.TextInput)

Auxiliary proto messages.

Represents the natural language text to be processed.

### [TextToSpeechSettings](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.TextToSpeechSettings)

Instructs the speech synthesizer on how to generate the output audio content.

### [SynthesizeSpeechConfigsEntry](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.TextToSpeechSettings.SynthesizeSpeechConfigsEntry)

The abstract base class for a message.

### [Tool](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Tool)

Represents a tool.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ActionConfirmationRequirementEntry](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Tool.ActionConfirmationRequirementEntry)

The abstract base class for a message.

### [Authentication](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Tool.Authentication)

Authentication information required for API calls

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ApiKeyConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Tool.Authentication.ApiKeyConfig)

Config for authentication with API key.

### [BearerTokenConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Tool.Authentication.BearerTokenConfig)

Config for authentication using bearer token.

### [OAuthConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Tool.Authentication.OAuthConfig)

Config for authentication with OAuth.

### [OauthGrantType](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Tool.Authentication.OAuthConfig.OauthGrantType)

OAuth grant types. Only `client credential grant <https://oauth.net/2/grant-types/client-credentials>`__ is supported.

### [RequestLocation](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Tool.Authentication.RequestLocation)

The location of the API key in the request.

### [ServiceAgentAuthConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Tool.Authentication.ServiceAgentAuthConfig)

Config for auth using `Dialogflow service agent <https://cloud.google.com/iam/docs/service-agents#dialogflow-service-agent>`__.

### [ServiceAgentAuth](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Tool.Authentication.ServiceAgentAuthConfig.ServiceAgentAuth)

Indicate the auth token type generated from the `Diaglogflow service agent <https://cloud.google.com/iam/docs/service-agents#dialogflow-service-agent>`__.

### [ConfirmationRequirement](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Tool.ConfirmationRequirement)

Types of confirmation requirement.

### [ConnectorTool](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Tool.ConnectorTool)

A ConnectorTool enabling using Integration Connectors Connections as tools.

### [Action](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Tool.ConnectorTool.Action)

Configuration of a Connection operation for the tool to use.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [EntityOperation](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Tool.ConnectorTool.Action.EntityOperation)

Entity CRUD operation specification.

### [OperationType](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Tool.ConnectorTool.Action.EntityOperation.OperationType)

The operation to perform on the entity.

### [ExtensionTool](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Tool.ExtensionTool)

An ExtensionTool is a way to use Vertex Extensions as a tool.

### [FunctionTool](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Tool.FunctionTool)

A Function tool describes the functions to be invoked on the client side.

### [MethodType](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Tool.MethodType)

The method type of the tool.

### [OpenApiTool](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Tool.OpenApiTool)

An OpenAPI tool is a way to provide the Tool specifications in the Open API schema format.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ServiceDirectoryConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Tool.ServiceDirectoryConfig)

Configuration for tools using Service Directory.

### [TLSConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Tool.TLSConfig)

The TLS configuration.

### [CACert](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Tool.TLSConfig.CACert)

The CA certificate.

### [ToolCall](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ToolCall)

Represents a call of a specific tool's action with the specified inputs.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [State](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ToolCall.State)

Tool call states.

### [ToolCallEvents](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ToolCallEvents)

Represents events containing tool call execution progress.

### [ToolCallResult](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ToolCallResult)

The result of calling a tool's action.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Error](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ToolCallResult.Error)

An error produced by the tool call.

### [ToolCallSuggestion](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ToolCallSuggestion)

Structured wrapper that pairs tool execution details with strongly-typed citations.

### [ToolsetTool](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ToolsetTool)

A tool that is created from a toolset.

### [TrainAgentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.TrainAgentRequest)

The request message for Agents.TrainAgent.

### [TriggerEvent](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.TriggerEvent)

The event that triggers the generator and LLM execution.

### [UndeployConversationModelOperationMetadata](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.UndeployConversationModelOperationMetadata)

Metadata for a ConversationModels.UndeployConversationModel operation.

### [UndeployConversationModelRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.UndeployConversationModelRequest)

The request message for ConversationModels.UndeployConversationModel

### [UpdateAnswerRecordRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.UpdateAnswerRecordRequest)

Request message for AnswerRecords.UpdateAnswerRecord.

### [UpdateCompanionAgentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.UpdateCompanionAgentRequest)

Request message for UpdateCompanionAgent.

### [UpdateContextRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.UpdateContextRequest)

The request message for Contexts.UpdateContext.

### [UpdateConversationProfileRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.UpdateConversationProfileRequest)

The request message for ConversationProfiles.UpdateConversationProfile.

### [UpdateDocumentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.UpdateDocumentRequest)

Request message for Documents.UpdateDocument.

### [UpdateEntityTypeRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.UpdateEntityTypeRequest)

The request message for EntityTypes.UpdateEntityType.

### [UpdateEnvironmentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.UpdateEnvironmentRequest)

The request message for Environments.UpdateEnvironment.

### [UpdateFulfillmentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.UpdateFulfillmentRequest)

The request message for Fulfillments.UpdateFulfillment.

### [UpdateGeneratorRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.UpdateGeneratorRequest)

Request of UpdateGenerator.

### [UpdateIntentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.UpdateIntentRequest)

The request message for Intents.UpdateIntent.

### [UpdateKnowledgeBaseRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.UpdateKnowledgeBaseRequest)

Request message for KnowledgeBases.UpdateKnowledgeBase.

### [UpdateParticipantRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.UpdateParticipantRequest)

The request message for Participants.UpdateParticipant.

### [UpdateSessionEntityTypeRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.UpdateSessionEntityTypeRequest)

The request message for SessionEntityTypes.UpdateSessionEntityType.

### [UpdateSipTrunkRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.UpdateSipTrunkRequest)

The request message for SipTrunks.UpdateSipTrunk.

### [UpdateToolRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.UpdateToolRequest)

Request of UpdateTool.

### [UpdateVersionRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.UpdateVersionRequest)

The request message for Versions.UpdateVersion.

### [ValidationError](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ValidationError)

Represents a single validation error.

### [Severity](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ValidationError.Severity)

Represents a level of severity.

### [ValidationResult](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.ValidationResult)

Represents the output of agent validation.

### [Version](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Version)

You can create multiple versions of your agent and publish them to separate environments.

When you edit an agent, you are editing the draft agent. At any point, you can save the draft agent as an agent version, which is an immutable snapshot of your agent.

When you save the draft agent, it is published to the default environment. When you create agent versions, you can publish them to custom environments. You can create a variety of custom environments for:

  * testing
  * development
  * production
  * etc.



For more information, see the `versions and environments guide <https://cloud.google.com/dialogflow/docs/agents-versions>`__.

### [VersionStatus](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.Version.VersionStatus)

The status of a version.

### [VoiceSelectionParams](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.VoiceSelectionParams)

Description of which voice to use for speech synthesis.

### [WebhookRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.WebhookRequest)

The request message for a webhook call.

### [WebhookResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.types.WebhookResponse)

The response message for a webhook call.

This response is validated by the Dialogflow server. If validation fails, an error will be returned in the QueryResult.diagnostic_info field. Setting JSON fields to an empty value with the wrong type is a common error. To avoid this error:

  * Use `""` for empty strings
  * Use `{}` or `null` for empty objects
  * Use `[]` or `null` for empty arrays



For more information, see the `Protocol Buffers Language Guide <https://developers.google.com/protocol-buffers/docs/proto3#json>`__.

### [AgentsAsyncClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.agents.AgentsAsyncClient)

Service for managing Agents.

### [AgentsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.agents.AgentsClient)

Service for managing Agents.

### [SearchAgentsAsyncPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.agents.pagers.SearchAgentsAsyncPager)

A pager for iterating through `search_agents` requests.

This class thinly wraps an initial [SearchAgentsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SearchAgentsResponse) object, and provides an `__aiter__` method to iterate through its `agents` field.

If there are more pages, the `__aiter__` method will make additional `SearchAgents` requests and continue to iterate through the `agents` field on the corresponding responses.

All the usual [SearchAgentsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SearchAgentsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [SearchAgentsPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.agents.pagers.SearchAgentsPager)

A pager for iterating through `search_agents` requests.

This class thinly wraps an initial [SearchAgentsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SearchAgentsResponse) object, and provides an `__iter__` method to iterate through its `agents` field.

If there are more pages, the `__iter__` method will make additional `SearchAgents` requests and continue to iterate through the `agents` field on the corresponding responses.

All the usual [SearchAgentsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SearchAgentsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [AnswerRecordsAsyncClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.answer_records.AnswerRecordsAsyncClient)

Service for managing AnswerRecords.

### [AnswerRecordsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.answer_records.AnswerRecordsClient)

Service for managing AnswerRecords.

### [ListAnswerRecordsAsyncPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.answer_records.pagers.ListAnswerRecordsAsyncPager)

A pager for iterating through `list_answer_records` requests.

This class thinly wraps an initial [ListAnswerRecordsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListAnswerRecordsResponse) object, and provides an `__aiter__` method to iterate through its `answer_records` field.

If there are more pages, the `__aiter__` method will make additional `ListAnswerRecords` requests and continue to iterate through the `answer_records` field on the corresponding responses.

All the usual [ListAnswerRecordsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListAnswerRecordsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListAnswerRecordsPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.answer_records.pagers.ListAnswerRecordsPager)

A pager for iterating through `list_answer_records` requests.

This class thinly wraps an initial [ListAnswerRecordsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListAnswerRecordsResponse) object, and provides an `__iter__` method to iterate through its `answer_records` field.

If there are more pages, the `__iter__` method will make additional `ListAnswerRecords` requests and continue to iterate through the `answer_records` field on the corresponding responses.

All the usual [ListAnswerRecordsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListAnswerRecordsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ContextsAsyncClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.contexts.ContextsAsyncClient)

Service for managing Contexts.

### [ContextsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.contexts.ContextsClient)

Service for managing Contexts.

### [ListContextsAsyncPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.contexts.pagers.ListContextsAsyncPager)

A pager for iterating through `list_contexts` requests.

This class thinly wraps an initial [ListContextsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListContextsResponse) object, and provides an `__aiter__` method to iterate through its `contexts` field.

If there are more pages, the `__aiter__` method will make additional `ListContexts` requests and continue to iterate through the `contexts` field on the corresponding responses.

All the usual [ListContextsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListContextsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListContextsPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.contexts.pagers.ListContextsPager)

A pager for iterating through `list_contexts` requests.

This class thinly wraps an initial [ListContextsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListContextsResponse) object, and provides an `__iter__` method to iterate through its `contexts` field.

If there are more pages, the `__iter__` method will make additional `ListContexts` requests and continue to iterate through the `contexts` field on the corresponding responses.

All the usual [ListContextsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListContextsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ConversationProfilesAsyncClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.conversation_profiles.ConversationProfilesAsyncClient)

Service for managing ConversationProfiles.

### [ConversationProfilesClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.conversation_profiles.ConversationProfilesClient)

Service for managing ConversationProfiles.

### [ListConversationProfilesAsyncPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.conversation_profiles.pagers.ListConversationProfilesAsyncPager)

A pager for iterating through `list_conversation_profiles` requests.

This class thinly wraps an initial [ListConversationProfilesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListConversationProfilesResponse) object, and provides an `__aiter__` method to iterate through its `conversation_profiles` field.

If there are more pages, the `__aiter__` method will make additional `ListConversationProfiles` requests and continue to iterate through the `conversation_profiles` field on the corresponding responses.

All the usual [ListConversationProfilesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListConversationProfilesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListConversationProfilesPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.conversation_profiles.pagers.ListConversationProfilesPager)

A pager for iterating through `list_conversation_profiles` requests.

This class thinly wraps an initial [ListConversationProfilesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListConversationProfilesResponse) object, and provides an `__iter__` method to iterate through its `conversation_profiles` field.

If there are more pages, the `__iter__` method will make additional `ListConversationProfiles` requests and continue to iterate through the `conversation_profiles` field on the corresponding responses.

All the usual [ListConversationProfilesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListConversationProfilesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ConversationsAsyncClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.conversations.ConversationsAsyncClient)

Service for managing Conversations.

### [ConversationsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.conversations.ConversationsClient)

Service for managing Conversations.

### [ListConversationsAsyncPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.conversations.pagers.ListConversationsAsyncPager)

A pager for iterating through `list_conversations` requests.

This class thinly wraps an initial [ListConversationsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListConversationsResponse) object, and provides an `__aiter__` method to iterate through its `conversations` field.

If there are more pages, the `__aiter__` method will make additional `ListConversations` requests and continue to iterate through the `conversations` field on the corresponding responses.

All the usual [ListConversationsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListConversationsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListConversationsPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.conversations.pagers.ListConversationsPager)

A pager for iterating through `list_conversations` requests.

This class thinly wraps an initial [ListConversationsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListConversationsResponse) object, and provides an `__iter__` method to iterate through its `conversations` field.

If there are more pages, the `__iter__` method will make additional `ListConversations` requests and continue to iterate through the `conversations` field on the corresponding responses.

All the usual [ListConversationsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListConversationsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListMessagesAsyncPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.conversations.pagers.ListMessagesAsyncPager)

A pager for iterating through `list_messages` requests.

This class thinly wraps an initial [ListMessagesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListMessagesResponse) object, and provides an `__aiter__` method to iterate through its `messages` field.

If there are more pages, the `__aiter__` method will make additional `ListMessages` requests and continue to iterate through the `messages` field on the corresponding responses.

All the usual [ListMessagesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListMessagesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListMessagesPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.conversations.pagers.ListMessagesPager)

A pager for iterating through `list_messages` requests.

This class thinly wraps an initial [ListMessagesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListMessagesResponse) object, and provides an `__iter__` method to iterate through its `messages` field.

If there are more pages, the `__iter__` method will make additional `ListMessages` requests and continue to iterate through the `messages` field on the corresponding responses.

All the usual [ListMessagesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListMessagesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [DocumentsAsyncClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.documents.DocumentsAsyncClient)

Service for managing knowledge Documents.

### [DocumentsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.documents.DocumentsClient)

Service for managing knowledge Documents.

### [ListDocumentsAsyncPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.documents.pagers.ListDocumentsAsyncPager)

A pager for iterating through `list_documents` requests.

This class thinly wraps an initial [ListDocumentsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListDocumentsResponse) object, and provides an `__aiter__` method to iterate through its `documents` field.

If there are more pages, the `__aiter__` method will make additional `ListDocuments` requests and continue to iterate through the `documents` field on the corresponding responses.

All the usual [ListDocumentsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListDocumentsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListDocumentsPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.documents.pagers.ListDocumentsPager)

A pager for iterating through `list_documents` requests.

This class thinly wraps an initial [ListDocumentsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListDocumentsResponse) object, and provides an `__iter__` method to iterate through its `documents` field.

If there are more pages, the `__iter__` method will make additional `ListDocuments` requests and continue to iterate through the `documents` field on the corresponding responses.

All the usual [ListDocumentsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListDocumentsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [EncryptionSpecServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.encryption_spec_service.EncryptionSpecServiceAsyncClient)

Manages encryption spec settings for Dialogflow and Agent Assist.

### [EncryptionSpecServiceClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.encryption_spec_service.EncryptionSpecServiceClient)

Manages encryption spec settings for Dialogflow and Agent Assist.

### [EntityTypesAsyncClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.entity_types.EntityTypesAsyncClient)

Service for managing EntityTypes.

### [EntityTypesClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.entity_types.EntityTypesClient)

Service for managing EntityTypes.

### [ListEntityTypesAsyncPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.entity_types.pagers.ListEntityTypesAsyncPager)

A pager for iterating through `list_entity_types` requests.

This class thinly wraps an initial [ListEntityTypesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListEntityTypesResponse) object, and provides an `__aiter__` method to iterate through its `entity_types` field.

If there are more pages, the `__aiter__` method will make additional `ListEntityTypes` requests and continue to iterate through the `entity_types` field on the corresponding responses.

All the usual [ListEntityTypesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListEntityTypesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListEntityTypesPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.entity_types.pagers.ListEntityTypesPager)

A pager for iterating through `list_entity_types` requests.

This class thinly wraps an initial [ListEntityTypesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListEntityTypesResponse) object, and provides an `__iter__` method to iterate through its `entity_types` field.

If there are more pages, the `__iter__` method will make additional `ListEntityTypes` requests and continue to iterate through the `entity_types` field on the corresponding responses.

All the usual [ListEntityTypesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListEntityTypesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [EnvironmentsAsyncClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.environments.EnvironmentsAsyncClient)

Service for managing Environments.

### [EnvironmentsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.environments.EnvironmentsClient)

Service for managing Environments.

### [GetEnvironmentHistoryAsyncPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.environments.pagers.GetEnvironmentHistoryAsyncPager)

A pager for iterating through `get_environment_history` requests.

This class thinly wraps an initial [EnvironmentHistory](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.EnvironmentHistory) object, and provides an `__aiter__` method to iterate through its `entries` field.

If there are more pages, the `__aiter__` method will make additional `GetEnvironmentHistory` requests and continue to iterate through the `entries` field on the corresponding responses.

All the usual [EnvironmentHistory](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.EnvironmentHistory) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [GetEnvironmentHistoryPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.environments.pagers.GetEnvironmentHistoryPager)

A pager for iterating through `get_environment_history` requests.

This class thinly wraps an initial [EnvironmentHistory](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.EnvironmentHistory) object, and provides an `__iter__` method to iterate through its `entries` field.

If there are more pages, the `__iter__` method will make additional `GetEnvironmentHistory` requests and continue to iterate through the `entries` field on the corresponding responses.

All the usual [EnvironmentHistory](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.EnvironmentHistory) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListEnvironmentsAsyncPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.environments.pagers.ListEnvironmentsAsyncPager)

A pager for iterating through `list_environments` requests.

This class thinly wraps an initial [ListEnvironmentsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListEnvironmentsResponse) object, and provides an `__aiter__` method to iterate through its `environments` field.

If there are more pages, the `__aiter__` method will make additional `ListEnvironments` requests and continue to iterate through the `environments` field on the corresponding responses.

All the usual [ListEnvironmentsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListEnvironmentsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListEnvironmentsPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.environments.pagers.ListEnvironmentsPager)

A pager for iterating through `list_environments` requests.

This class thinly wraps an initial [ListEnvironmentsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListEnvironmentsResponse) object, and provides an `__iter__` method to iterate through its `environments` field.

If there are more pages, the `__iter__` method will make additional `ListEnvironments` requests and continue to iterate through the `environments` field on the corresponding responses.

All the usual [ListEnvironmentsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListEnvironmentsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [FulfillmentsAsyncClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.fulfillments.FulfillmentsAsyncClient)

Service for managing Fulfillments.

### [FulfillmentsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.fulfillments.FulfillmentsClient)

Service for managing Fulfillments.

### [GeneratorEvaluationsAsyncClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.generator_evaluations.GeneratorEvaluationsAsyncClient)

Service for managing generator evaluations.

### [GeneratorEvaluationsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.generator_evaluations.GeneratorEvaluationsClient)

Service for managing generator evaluations.

### [ListGeneratorEvaluationsAsyncPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.generator_evaluations.pagers.ListGeneratorEvaluationsAsyncPager)

A pager for iterating through `list_generator_evaluations` requests.

This class thinly wraps an initial [ListGeneratorEvaluationsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListGeneratorEvaluationsResponse) object, and provides an `__aiter__` method to iterate through its `generator_evaluations` field.

If there are more pages, the `__aiter__` method will make additional `ListGeneratorEvaluations` requests and continue to iterate through the `generator_evaluations` field on the corresponding responses.

All the usual [ListGeneratorEvaluationsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListGeneratorEvaluationsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListGeneratorEvaluationsPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.generator_evaluations.pagers.ListGeneratorEvaluationsPager)

A pager for iterating through `list_generator_evaluations` requests.

This class thinly wraps an initial [ListGeneratorEvaluationsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListGeneratorEvaluationsResponse) object, and provides an `__iter__` method to iterate through its `generator_evaluations` field.

If there are more pages, the `__iter__` method will make additional `ListGeneratorEvaluations` requests and continue to iterate through the `generator_evaluations` field on the corresponding responses.

All the usual [ListGeneratorEvaluationsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListGeneratorEvaluationsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [GeneratorsAsyncClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.generators.GeneratorsAsyncClient)

Generator Service for LLM powered Agent Assist. This service manages the configurations of user owned Generators, such as description, context and instruction, input/output format, etc. The generator resources will be used inside a conversation and will be triggered by TriggerEvent to query LLM for answers.

### [GeneratorsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.generators.GeneratorsClient)

Generator Service for LLM powered Agent Assist. This service manages the configurations of user owned Generators, such as description, context and instruction, input/output format, etc. The generator resources will be used inside a conversation and will be triggered by TriggerEvent to query LLM for answers.

### [ListGeneratorsAsyncPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.generators.pagers.ListGeneratorsAsyncPager)

A pager for iterating through `list_generators` requests.

This class thinly wraps an initial [ListGeneratorsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListGeneratorsResponse) object, and provides an `__aiter__` method to iterate through its `generators` field.

If there are more pages, the `__aiter__` method will make additional `ListGenerators` requests and continue to iterate through the `generators` field on the corresponding responses.

All the usual [ListGeneratorsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListGeneratorsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListGeneratorsPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.generators.pagers.ListGeneratorsPager)

A pager for iterating through `list_generators` requests.

This class thinly wraps an initial [ListGeneratorsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListGeneratorsResponse) object, and provides an `__iter__` method to iterate through its `generators` field.

If there are more pages, the `__iter__` method will make additional `ListGenerators` requests and continue to iterate through the `generators` field on the corresponding responses.

All the usual [ListGeneratorsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListGeneratorsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [IntentsAsyncClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.intents.IntentsAsyncClient)

Service for managing Intents.

### [IntentsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.intents.IntentsClient)

Service for managing Intents.

### [ListIntentsAsyncPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.intents.pagers.ListIntentsAsyncPager)

A pager for iterating through `list_intents` requests.

This class thinly wraps an initial [ListIntentsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListIntentsResponse) object, and provides an `__aiter__` method to iterate through its `intents` field.

If there are more pages, the `__aiter__` method will make additional `ListIntents` requests and continue to iterate through the `intents` field on the corresponding responses.

All the usual [ListIntentsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListIntentsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListIntentsPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.intents.pagers.ListIntentsPager)

A pager for iterating through `list_intents` requests.

This class thinly wraps an initial [ListIntentsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListIntentsResponse) object, and provides an `__iter__` method to iterate through its `intents` field.

If there are more pages, the `__iter__` method will make additional `ListIntents` requests and continue to iterate through the `intents` field on the corresponding responses.

All the usual [ListIntentsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListIntentsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [KnowledgeBasesAsyncClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.knowledge_bases.KnowledgeBasesAsyncClient)

Service for managing KnowledgeBases.

### [KnowledgeBasesClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.knowledge_bases.KnowledgeBasesClient)

Service for managing KnowledgeBases.

### [ListKnowledgeBasesAsyncPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.knowledge_bases.pagers.ListKnowledgeBasesAsyncPager)

A pager for iterating through `list_knowledge_bases` requests.

This class thinly wraps an initial [ListKnowledgeBasesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListKnowledgeBasesResponse) object, and provides an `__aiter__` method to iterate through its `knowledge_bases` field.

If there are more pages, the `__aiter__` method will make additional `ListKnowledgeBases` requests and continue to iterate through the `knowledge_bases` field on the corresponding responses.

All the usual [ListKnowledgeBasesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListKnowledgeBasesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListKnowledgeBasesPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.knowledge_bases.pagers.ListKnowledgeBasesPager)

A pager for iterating through `list_knowledge_bases` requests.

This class thinly wraps an initial [ListKnowledgeBasesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListKnowledgeBasesResponse) object, and provides an `__iter__` method to iterate through its `knowledge_bases` field.

If there are more pages, the `__iter__` method will make additional `ListKnowledgeBases` requests and continue to iterate through the `knowledge_bases` field on the corresponding responses.

All the usual [ListKnowledgeBasesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListKnowledgeBasesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ParticipantsAsyncClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.participants.ParticipantsAsyncClient)

Service for managing Participants.

### [ParticipantsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.participants.ParticipantsClient)

Service for managing Participants.

### [ListParticipantsAsyncPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.participants.pagers.ListParticipantsAsyncPager)

A pager for iterating through `list_participants` requests.

This class thinly wraps an initial [ListParticipantsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListParticipantsResponse) object, and provides an `__aiter__` method to iterate through its `participants` field.

If there are more pages, the `__aiter__` method will make additional `ListParticipants` requests and continue to iterate through the `participants` field on the corresponding responses.

All the usual [ListParticipantsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListParticipantsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListParticipantsPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.participants.pagers.ListParticipantsPager)

A pager for iterating through `list_participants` requests.

This class thinly wraps an initial [ListParticipantsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListParticipantsResponse) object, and provides an `__iter__` method to iterate through its `participants` field.

If there are more pages, the `__iter__` method will make additional `ListParticipants` requests and continue to iterate through the `participants` field on the corresponding responses.

All the usual [ListParticipantsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListParticipantsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListSuggestionsAsyncPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.participants.pagers.ListSuggestionsAsyncPager)

A pager for iterating through `list_suggestions` requests.

This class thinly wraps an initial [ListSuggestionsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListSuggestionsResponse) object, and provides an `__aiter__` method to iterate through its `suggestions` field.

If there are more pages, the `__aiter__` method will make additional `ListSuggestions` requests and continue to iterate through the `suggestions` field on the corresponding responses.

All the usual [ListSuggestionsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListSuggestionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListSuggestionsPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.participants.pagers.ListSuggestionsPager)

A pager for iterating through `list_suggestions` requests.

This class thinly wraps an initial [ListSuggestionsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListSuggestionsResponse) object, and provides an `__iter__` method to iterate through its `suggestions` field.

If there are more pages, the `__iter__` method will make additional `ListSuggestions` requests and continue to iterate through the `suggestions` field on the corresponding responses.

All the usual [ListSuggestionsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListSuggestionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [PhoneNumbersAsyncClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.phone_numbers.PhoneNumbersAsyncClient)

Service for managing PhoneNumbers.

### [PhoneNumbersClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.phone_numbers.PhoneNumbersClient)

Service for managing PhoneNumbers.

### [ListPhoneNumbersAsyncPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.phone_numbers.pagers.ListPhoneNumbersAsyncPager)

A pager for iterating through `list_phone_numbers` requests.

This class thinly wraps an initial [ListPhoneNumbersResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListPhoneNumbersResponse) object, and provides an `__aiter__` method to iterate through its `phone_numbers` field.

If there are more pages, the `__aiter__` method will make additional `ListPhoneNumbers` requests and continue to iterate through the `phone_numbers` field on the corresponding responses.

All the usual [ListPhoneNumbersResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListPhoneNumbersResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListPhoneNumbersPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.phone_numbers.pagers.ListPhoneNumbersPager)

A pager for iterating through `list_phone_numbers` requests.

This class thinly wraps an initial [ListPhoneNumbersResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListPhoneNumbersResponse) object, and provides an `__iter__` method to iterate through its `phone_numbers` field.

If there are more pages, the `__iter__` method will make additional `ListPhoneNumbers` requests and continue to iterate through the `phone_numbers` field on the corresponding responses.

All the usual [ListPhoneNumbersResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListPhoneNumbersResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [SessionEntityTypesAsyncClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.session_entity_types.SessionEntityTypesAsyncClient)

Service for managing SessionEntityTypes.

### [SessionEntityTypesClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.session_entity_types.SessionEntityTypesClient)

Service for managing SessionEntityTypes.

### [ListSessionEntityTypesAsyncPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.session_entity_types.pagers.ListSessionEntityTypesAsyncPager)

A pager for iterating through `list_session_entity_types` requests.

This class thinly wraps an initial [ListSessionEntityTypesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListSessionEntityTypesResponse) object, and provides an `__aiter__` method to iterate through its `session_entity_types` field.

If there are more pages, the `__aiter__` method will make additional `ListSessionEntityTypes` requests and continue to iterate through the `session_entity_types` field on the corresponding responses.

All the usual [ListSessionEntityTypesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListSessionEntityTypesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListSessionEntityTypesPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.session_entity_types.pagers.ListSessionEntityTypesPager)

A pager for iterating through `list_session_entity_types` requests.

This class thinly wraps an initial [ListSessionEntityTypesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListSessionEntityTypesResponse) object, and provides an `__iter__` method to iterate through its `session_entity_types` field.

If there are more pages, the `__iter__` method will make additional `ListSessionEntityTypes` requests and continue to iterate through the `session_entity_types` field on the corresponding responses.

All the usual [ListSessionEntityTypesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListSessionEntityTypesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [SessionsAsyncClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.sessions.SessionsAsyncClient)

A service used for session interactions.

For more information, see the `API interactions guide <https://cloud.google.com/dialogflow/docs/api-overview>`__.

### [SessionsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.sessions.SessionsClient)

A service used for session interactions.

For more information, see the `API interactions guide <https://cloud.google.com/dialogflow/docs/api-overview>`__.

### [SipTrunksAsyncClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.sip_trunks.SipTrunksAsyncClient)

Service for managing SipTrunks.

### [SipTrunksClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.sip_trunks.SipTrunksClient)

Service for managing SipTrunks.

### [ListSipTrunksAsyncPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.sip_trunks.pagers.ListSipTrunksAsyncPager)

A pager for iterating through `list_sip_trunks` requests.

This class thinly wraps an initial [ListSipTrunksResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListSipTrunksResponse) object, and provides an `__aiter__` method to iterate through its `sip_trunks` field.

If there are more pages, the `__aiter__` method will make additional `ListSipTrunks` requests and continue to iterate through the `sip_trunks` field on the corresponding responses.

All the usual [ListSipTrunksResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListSipTrunksResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListSipTrunksPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.sip_trunks.pagers.ListSipTrunksPager)

A pager for iterating through `list_sip_trunks` requests.

This class thinly wraps an initial [ListSipTrunksResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListSipTrunksResponse) object, and provides an `__iter__` method to iterate through its `sip_trunks` field.

If there are more pages, the `__iter__` method will make additional `ListSipTrunks` requests and continue to iterate through the `sip_trunks` field on the corresponding responses.

All the usual [ListSipTrunksResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListSipTrunksResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ToolsAsyncClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.tools.ToolsAsyncClient)

Tool Service for LLM powered Agent Assist. Tools can be used to interact with remote APIs (e.g. fetching orders) to retrieve additional information as input to LLM.

### [ToolsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.tools.ToolsClient)

Tool Service for LLM powered Agent Assist. Tools can be used to interact with remote APIs (e.g. fetching orders) to retrieve additional information as input to LLM.

### [ListToolsAsyncPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.tools.pagers.ListToolsAsyncPager)

A pager for iterating through `list_tools` requests.

This class thinly wraps an initial [ListToolsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListToolsResponse) object, and provides an `__aiter__` method to iterate through its `tools` field.

If there are more pages, the `__aiter__` method will make additional `ListTools` requests and continue to iterate through the `tools` field on the corresponding responses.

All the usual [ListToolsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListToolsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListToolsPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.tools.pagers.ListToolsPager)

A pager for iterating through `list_tools` requests.

This class thinly wraps an initial [ListToolsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListToolsResponse) object, and provides an `__iter__` method to iterate through its `tools` field.

If there are more pages, the `__iter__` method will make additional `ListTools` requests and continue to iterate through the `tools` field on the corresponding responses.

All the usual [ListToolsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListToolsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [VersionsAsyncClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.versions.VersionsAsyncClient)

Service for managing Versions.

### [VersionsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.versions.VersionsClient)

Service for managing Versions.

### [ListVersionsAsyncPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.versions.pagers.ListVersionsAsyncPager)

A pager for iterating through `list_versions` requests.

This class thinly wraps an initial [ListVersionsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListVersionsResponse) object, and provides an `__aiter__` method to iterate through its `versions` field.

If there are more pages, the `__aiter__` method will make additional `ListVersions` requests and continue to iterate through the `versions` field on the corresponding responses.

All the usual [ListVersionsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListVersionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListVersionsPager](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.versions.pagers.ListVersionsPager)

A pager for iterating through `list_versions` requests.

This class thinly wraps an initial [ListVersionsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListVersionsResponse) object, and provides an `__iter__` method to iterate through its `versions` field.

If there are more pages, the `__iter__` method will make additional `ListVersions` requests and continue to iterate through the `versions` field on the corresponding responses.

All the usual [ListVersionsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ListVersionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [Agent](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Agent)

A Dialogflow agent is a virtual agent that handles conversations with your end-users. It is a natural language understanding module that understands the nuances of human language. Dialogflow translates end-user text or audio during a conversation to structured data that your apps and services can understand. You design and build a Dialogflow agent to handle the types of conversations required for your system.

For more information about agents, see the `Agent guide <https://cloud.google.com/dialogflow/docs/agents-overview>`__.

### [ApiVersion](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Agent.ApiVersion)

API version for the agent.

### [MatchMode](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Agent.MatchMode)

Match mode determines how intents are detected from user queries.

### [Tier](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Agent.Tier)

Represents the agent tier.

### [AgentAssistantFeedback](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.AgentAssistantFeedback)

Detail feedback of Agent Assistant result.

### [AnswerRelevance](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.AgentAssistantFeedback.AnswerRelevance)

Relevance of an answer.

### [DocumentCorrectness](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.AgentAssistantFeedback.DocumentCorrectness)

Correctness of document.

### [DocumentEfficiency](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.AgentAssistantFeedback.DocumentEfficiency)

Efficiency of document.

### [KnowledgeAssistFeedback](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.AgentAssistantFeedback.KnowledgeAssistFeedback)

Feedback for knowledge assist.

### [KnowledgeSearchFeedback](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.AgentAssistantFeedback.KnowledgeSearchFeedback)

Feedback for knowledge search.

### [SummarizationFeedback](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.AgentAssistantFeedback.SummarizationFeedback)

Feedback for conversation summarization.

### [TextSectionsEntry](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.AgentAssistantFeedback.SummarizationFeedback.TextSectionsEntry)

The abstract base class for a message.

### [AgentAssistantRecord](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.AgentAssistantRecord)

Represents a record of a human agent assistant answer.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AgentCoachingContext](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.AgentCoachingContext)

Agent Coaching context that customer can configure.

### [AgentCoachingInstruction](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.AgentCoachingInstruction)

Agent Coaching instructions that customer can configure.

### [DuplicateCheckResult](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.AgentCoachingInstruction.DuplicateCheckResult)

Duplication check for the suggestion.

### [DuplicateSuggestion](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.AgentCoachingInstruction.DuplicateCheckResult.DuplicateSuggestion)

The duplicate suggestion details.

### [TriggerEvent](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.AgentCoachingInstruction.TriggerEvent)

The event that should trigger this instruction.

### [AgentCoachingSuggestion](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.AgentCoachingSuggestion)

Suggestion for coaching agents.

### [AgentActionSuggestion](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.AgentCoachingSuggestion.AgentActionSuggestion)

Actions suggested for the agent. This is based on applicable instructions.

### [DuplicateCheckResult](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.AgentCoachingSuggestion.DuplicateCheckResult)

Duplication check for the suggestion.

### [DuplicateSuggestion](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.AgentCoachingSuggestion.DuplicateCheckResult.DuplicateSuggestion)

The duplicate suggestion details. Keeping answer_record and sources together as they are identifiers for duplicate suggestions.

### [SampleResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.AgentCoachingSuggestion.SampleResponse)

Sample response that the agent can use. This could be based on applicable instructions and ingested data from other systems.

### [Sources](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.AgentCoachingSuggestion.Sources)

Sources for the suggestion.

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

### [CorrectnessLevel](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.AnswerFeedback.CorrectnessLevel)

The correctness level of an answer.

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

### [MetadataEntry](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ArticleAnswer.MetadataEntry)

The abstract base class for a message.

### [AssistQueryParameters](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.AssistQueryParameters)

Represents the parameters of human assist query.

### [DocumentsMetadataFiltersEntry](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.AssistQueryParameters.DocumentsMetadataFiltersEntry)

The abstract base class for a message.

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

### [AutomatedAgentReplyType](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.AutomatedAgentReply.AutomatedAgentReplyType)

Represents different automated agent reply types.

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

### [Config](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.BidiStreamingAnalyzeContentRequest.Config)

The config of the session.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [VoiceSessionConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.BidiStreamingAnalyzeContentRequest.Config.VoiceSessionConfig)

The config about how to process the audio for a voice-based session.

### [Input](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.BidiStreamingAnalyzeContentRequest.Input)

Input for the conversation.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [TurnInput](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.BidiStreamingAnalyzeContentRequest.TurnInput)

Input that forms data for a single turn.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [BidiStreamingAnalyzeContentResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.BidiStreamingAnalyzeContentResponse)

The response message for Participants.BidiStreamingAnalyzeContent.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [BargeInSignal](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.BidiStreamingAnalyzeContentResponse.BargeInSignal)

Indicate the user barge-in has been detected.

### [TurnComplete](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.BidiStreamingAnalyzeContentResponse.TurnComplete)

Indicate that the turn is complete.

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

### [CertificateState](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Connection.CertificateState)

The state of Sip Trunk certificate authentication.

### [ErrorDetails](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Connection.ErrorDetails)

The error details of Sip Trunk connection authentication.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [State](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Connection.State)

The state of Sip Trunk connection.

### [Context](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Context)

Dialogflow contexts are similar to natural language context. If a person says to you "they are orange", you need context in order to understand what "they" is referring to. Similarly, for Dialogflow to handle an end-user expression like that, it needs to be provided with context in order to correctly match an intent.

Using contexts, you can control the flow of a conversation. You can configure contexts for an intent by setting input and output contexts, which are identified by string names. When an intent is matched, any configured output contexts for that intent become active. While any contexts are active, Dialogflow is more likely to match intents that are configured with input contexts that correspond to the currently active contexts.

For more information about context, see the `Contexts guide <https://cloud.google.com/dialogflow/docs/contexts-overview>`__.

### [Conversation](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Conversation)

Represents a conversation. A conversation is an interaction between an agent, including live agents and Dialogflow agents, and a support customer. Conversations can include phone calls and text-based chat sessions.

### [ContextReference](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Conversation.ContextReference)

Represents a piece of ingested context information.

### [ContextContent](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Conversation.ContextReference.ContextContent)

Contents ingested.

### [ContentFormat](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Conversation.ContextReference.ContextContent.ContentFormat)

Represents the format of the ingested string.

### [UpdateMode](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Conversation.ContextReference.UpdateMode)

Represents the mode in which context reference contents are updated.

### [ConversationStage](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Conversation.ConversationStage)

Enumeration of the different conversation stages a conversation can be in. Reference: <https://cloud.google.com/agent-assist/docs/basics#conversation_stages>

### [GeneratorContext](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Conversation.GeneratorContext)

Represents the context of a generator.

### [GeneratorType](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Conversation.GeneratorContext.GeneratorType)

The available generator types.

### [IngestedContextReferencesEntry](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Conversation.IngestedContextReferencesEntry)

The abstract base class for a message.

### [InitialGeneratorContextsEntry](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Conversation.InitialGeneratorContextsEntry)

The abstract base class for a message.

### [LifecycleState](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Conversation.LifecycleState)

Enumeration of the completion status of the conversation.

### [TelephonyConnectionInfo](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Conversation.TelephonyConnectionInfo)

The information about phone calls connected via phone gateway to the conversation.

### [MimeContent](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Conversation.TelephonyConnectionInfo.MimeContent)

The mime content from the initial SIP INVITE.

### [SipHeader](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Conversation.TelephonyConnectionInfo.SipHeader)

The SIP headers from the initial SIP INVITE.

### [ConversationContext](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ConversationContext)

Context of the conversation, including transcripts.

### [ConversationEvent](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ConversationEvent)

Represents a notification sent to Pub/Sub subscribers for conversation lifecycle events.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Type](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ConversationEvent.Type)

Enumeration of the types of events available.
    
    
        In general non-recoverable errors only occur if something
        was misconfigured in the ConversationProfile corresponding
        to the call. After a non-recoverable error, Dialogflow may
        stop responding.
    
        We don't fire this event:
    
        - in an API call because we can directly return the error,
          or,
        - when we can recover from an error.
    

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

### [PhoneticEncoding](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.CustomPronunciationParams.PhoneticEncoding)

The phonetic encoding of the phrase.

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

### [KnowledgeType](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Document.KnowledgeType)

The knowledge type of document content.
    
    
        CSV must have questions in the first column and
        answers in the second, with no header. Because
        of this explicit format, they are always parsed
        accurately.
    EXTRACTIVE_QA (2):
        Documents for which unstructured text is
        extracted and used for question answering.
    ARTICLE_SUGGESTION (3):
        The entire document content as a whole can be
        used for query results. Only for Contact Center
        Solutions on Dialogflow.
    AGENT_FACING_SMART_REPLY (4):
        The document contains agent-facing Smart
        Reply entries.
    SMART_REPLY (4):
        The legacy enum for agent-facing smart reply
        feature.
    

### [MetadataEntry](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Document.MetadataEntry)

The abstract base class for a message.

### [ReloadStatus](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Document.ReloadStatus)

The status of a reload attempt.

### [State](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Document.State)

Possible states of the document

### [DtmfParameters](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.DtmfParameters)

The message in the response that indicates the parameters of DTMF.

### [EncryptionSpec](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.EncryptionSpec)

A customer-managed encryption key specification that can be applied to all created resources (e.g. Conversation).

### [EntityType](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.EntityType)

Each intent parameter has a type, called the entity type, which dictates exactly how data from an end-user expression is extracted.

Dialogflow provides predefined system entities that can match many common types of data. For example, there are system entities for matching dates, times, colors, email addresses, and so on. You can also create your own custom entities for matching custom data. For example, you could define a vegetable entity that can match the types of vegetables available for purchase with a grocery store agent.

For more information, see the `Entity guide <https://cloud.google.com/dialogflow/docs/entities-overview>`__.

### [AutoExpansionMode](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.EntityType.AutoExpansionMode)

Represents different entity type expansion modes. Automated expansion allows an agent to recognize values that have not been explicitly listed in the entity (for example, new kinds of shopping list items).

### [Entity](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.EntityType.Entity)

An **entity entry** for an associated entity type.

### [Kind](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.EntityType.Kind)

Represents kinds of entities.

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

### [State](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Environment.State)

Represents an environment state. When an environment is pointed to a new agent version, the environment is temporarily set to the `LOADING` state. During that time, the environment keeps on serving the previous version of the agent. After the new agent version is done loading, the environment is set back to the `RUNNING` state.

### [EnvironmentHistory](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.EnvironmentHistory)

The response message for Environments.GetEnvironmentHistory.

### [Entry](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.EnvironmentHistory.Entry)

Represents an environment history entry.

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

### [MetadataEntry](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.FaqAnswer.MetadataEntry)

The abstract base class for a message.

### [FewShotExample](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.FewShotExample)

Providing examples in the generator (i.e. building a few-shot generator) helps convey the desired format of the LLM response.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ExtraInfoEntry](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.FewShotExample.ExtraInfoEntry)

The abstract base class for a message.

### [FreeFormContext](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.FreeFormContext)

Free form generator context that customer can configure.

### [FreeFormSuggestion](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.FreeFormSuggestion)

Suggestion generated using free form generator.

### [Fulfillment](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Fulfillment)

By default, your agent responds to a matched intent with a static response. As an alternative, you can provide a more dynamic response by using fulfillment. When you enable fulfillment for an intent, Dialogflow responds to that intent by calling a service that you define. For example, if an end-user wants to schedule a haircut on Friday, your service can check your database and respond to the end-user with availability information for Friday.

For more information, see the `fulfillment guide <https://cloud.google.com/dialogflow/docs/fulfillment-overview>`__.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Feature](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Fulfillment.Feature)

Whether fulfillment is enabled for the specific feature.

### [Type](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Fulfillment.Feature.Type)

The type of the feature.

### [GenericWebService](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Fulfillment.GenericWebService)

Represents configuration for a generic web service. Dialogflow supports two mechanisms for authentications:

  * Basic authentication with username and password.
  * Authentication with additional authentication headers.



More information could be found at:

<https://cloud.google.com/dialogflow/docs/fulfillment-configure>.

### [RequestHeadersEntry](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Fulfillment.GenericWebService.RequestHeadersEntry)

The abstract base class for a message.

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

### [ContextReferencesEntry](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.GenerateStatelessSuggestionRequest.ContextReferencesEntry)

The abstract base class for a message.

### [GenerateStatelessSuggestionResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.GenerateStatelessSuggestionResponse)

The response message for Conversations.GenerateStatelessSuggestion.

### [GenerateStatelessSummaryRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.GenerateStatelessSummaryRequest)

The request message for Conversations.GenerateStatelessSummary.

### [MinimalConversation](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.GenerateStatelessSummaryRequest.MinimalConversation)

The minimum amount of information required to generate a Summary without having a Conversation resource created.

### [GenerateStatelessSummaryResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.GenerateStatelessSummaryResponse)

The response message for Conversations.GenerateStatelessSummary.

### [Summary](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.GenerateStatelessSummaryResponse.Summary)

Generated summary for a conversation.

### [TextSectionsEntry](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.GenerateStatelessSummaryResponse.Summary.TextSectionsEntry)

The abstract base class for a message.

### [GenerateSuggestionsRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.GenerateSuggestionsRequest)

The request message for Conversations.GenerateSuggestions.

### [GenerateSuggestionsResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.GenerateSuggestionsResponse)

The response message for Conversations.GenerateSuggestions.

### [GeneratorSuggestionAnswer](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.GenerateSuggestionsResponse.GeneratorSuggestionAnswer)

A GeneratorSuggestion answer.

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

### [AgentAssistInputDataConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.GeneratorEvaluationConfig.AgentAssistInputDataConfig)

The distinctive configs for Agent Assist conversations as the conversation source.

### [DatasetInputDataConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.GeneratorEvaluationConfig.DatasetInputDataConfig)

The distinctive configs for dataset as the conversation source.

### [InputDataConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.GeneratorEvaluationConfig.InputDataConfig)

Input data config details

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [SummaryGenerationOption](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.GeneratorEvaluationConfig.InputDataConfig.SummaryGenerationOption)

Summary generation options.

### [InputDataSourceType](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.GeneratorEvaluationConfig.InputDataSourceType)

Enumeration of input data source type.

### [SummarizationConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.GeneratorEvaluationConfig.SummarizationConfig)

Evaluation configs for summarization generator.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [GeneratorEvaluationOperationMetadata](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.GeneratorEvaluationOperationMetadata)

Metadata for a GeneratorEvaluations.CreateGeneratorEvaluation operation.

### [GeneratorSuggestion](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.GeneratorSuggestion)

Suggestion generated using a Generator.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ToolCallInfo](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.GeneratorSuggestion.ToolCallInfo)

Request and response for a tool call.

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

### [ConversationProcessConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.HumanAgentAssistantConfig.ConversationProcessConfig)

Config to process conversation.

### [MessageAnalysisConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.HumanAgentAssistantConfig.MessageAnalysisConfig)

Configuration for analyses to run on each conversation message.

### [SuggestionConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.HumanAgentAssistantConfig.SuggestionConfig)

Detail human agent assistant config.

### [SuggestionFeatureConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.HumanAgentAssistantConfig.SuggestionFeatureConfig)

Config for suggestion features.

### [SuggestionQueryConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.HumanAgentAssistantConfig.SuggestionQueryConfig)

Config for suggestion query.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ContextFilterSettings](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.HumanAgentAssistantConfig.SuggestionQueryConfig.ContextFilterSettings)

Settings that determine how to filter recent conversation context when generating suggestions.

### [DialogflowQuerySource](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.HumanAgentAssistantConfig.SuggestionQueryConfig.DialogflowQuerySource)

Dialogflow source setting.

Supported feature: DIALOGFLOW_ASSIST, ENTITY_EXTRACTION.

### [HumanAgentSideConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.HumanAgentAssistantConfig.SuggestionQueryConfig.DialogflowQuerySource.HumanAgentSideConfig)

The configuration used for human agent side Dialogflow assist suggestion.

### [DocumentQuerySource](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.HumanAgentAssistantConfig.SuggestionQueryConfig.DocumentQuerySource)

Document source settings.

Supported features: SMART_REPLY, SMART_COMPOSE.

### [KnowledgeBaseQuerySource](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.HumanAgentAssistantConfig.SuggestionQueryConfig.KnowledgeBaseQuerySource)

Knowledge base source settings.

Supported features: ARTICLE_SUGGESTION, FAQ.

### [Sections](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.HumanAgentAssistantConfig.SuggestionQueryConfig.Sections)

Custom sections to return when requesting a summary of a conversation. This is only supported when `baseline_model_version` == '2.0'.

Supported features: CONVERSATION_SUMMARIZATION, CONVERSATION_SUMMARIZATION_VOICE.

### [SectionType](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.HumanAgentAssistantConfig.SuggestionQueryConfig.Sections.SectionType)

Selectable sections to return when requesting a summary of a conversation.

### [SuggestionTriggerSettings](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.HumanAgentAssistantConfig.SuggestionTriggerSettings)

Settings of suggestion trigger.

### [HumanAgentAssistantEvent](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.HumanAgentAssistantEvent)

Output only. Represents a notification sent to Pub/Sub subscribers for agent assistant events in a specific conversation.

### [HumanAgentHandoffConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.HumanAgentHandoffConfig)

Defines the hand off to a live agent, typically on which external agent service provider to connect to a conversation.

Currently, this feature is not general available, please contact Google to get access.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [LivePersonConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.HumanAgentHandoffConfig.LivePersonConfig)

Configuration specific to `LivePerson <https://www.liveperson.com>`__.

### [SalesforceLiveAgentConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.HumanAgentHandoffConfig.SalesforceLiveAgentConfig)

Configuration specific to Salesforce Live Agent.

### [ImportAgentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ImportAgentRequest)

The request message for Agents.ImportAgent.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ImportDocumentTemplate](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ImportDocumentTemplate)

The template used for importing documents.

### [MetadataEntry](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ImportDocumentTemplate.MetadataEntry)

The abstract base class for a message.

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

### [ContextReferencesEntry](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.IngestContextReferencesRequest.ContextReferencesEntry)

The abstract base class for a message.

### [IngestContextReferencesResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.IngestContextReferencesResponse)

The response message for [ConversationsService.IngestContextReferences][].

### [IngestedContextReferencesEntry](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.IngestContextReferencesResponse.IngestedContextReferencesEntry)

The abstract base class for a message.

### [IngestedContextReferenceDebugInfo](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.IngestedContextReferenceDebugInfo)

Debug information related to ingested context reference.

### [IngestedParameterDebugInfo](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.IngestedContextReferenceDebugInfo.IngestedParameterDebugInfo)

Debug information related to ingested parameters from context reference.

### [IngestionStatus](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.IngestedContextReferenceDebugInfo.IngestedParameterDebugInfo.IngestionStatus)

Enum representing the various states of parameter ingestion.

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

### [FollowupIntentInfo](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Intent.FollowupIntentInfo)

Represents a single followup intent in the chain.

### [Message](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Intent.Message)

Corresponds to the `Response` field in the Dialogflow console.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [BasicCard](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Intent.Message.BasicCard)

The basic card message. Useful for displaying information.

### [Button](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Intent.Message.BasicCard.Button)

The button object that appears at the bottom of a card.

### [OpenUriAction](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Intent.Message.BasicCard.Button.OpenUriAction)

Opens the given URI.

### [BrowseCarouselCard](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Intent.Message.BrowseCarouselCard)

Browse Carousel Card for Actions on Google. <https://developers.google.com/actions/assistant/responses#browsing_carousel>

### [BrowseCarouselCardItem](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Intent.Message.BrowseCarouselCard.BrowseCarouselCardItem)

Browsing carousel tile

### [OpenUrlAction](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Intent.Message.BrowseCarouselCard.BrowseCarouselCardItem.OpenUrlAction)

Actions on Google action to open a given url.

### [UrlTypeHint](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Intent.Message.BrowseCarouselCard.BrowseCarouselCardItem.OpenUrlAction.UrlTypeHint)

Type of the URI.

### [ImageDisplayOptions](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Intent.Message.BrowseCarouselCard.ImageDisplayOptions)

Image display options for Actions on Google. This should be used for when the image's aspect ratio does not match the image container's aspect ratio.

### [Card](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Intent.Message.Card)

The card response message.

### [Button](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Intent.Message.Card.Button)

Optional. Contains information about a button.

### [CarouselSelect](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Intent.Message.CarouselSelect)

The card for presenting a carousel of options to select from.

### [Item](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Intent.Message.CarouselSelect.Item)

An item in the carousel.

### [ColumnProperties](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Intent.Message.ColumnProperties)

Column properties for TableCard.

### [HorizontalAlignment](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Intent.Message.ColumnProperties.HorizontalAlignment)

Text alignments within a cell.

### [Image](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Intent.Message.Image)

The image response message.

### [LinkOutSuggestion](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Intent.Message.LinkOutSuggestion)

The suggestion chip message that allows the user to jump out to the app or website associated with this agent.

### [ListSelect](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Intent.Message.ListSelect)

The card for presenting a list of options to select from.

### [Item](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Intent.Message.ListSelect.Item)

An item in the list.

### [MediaContent](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Intent.Message.MediaContent)

The media content card for Actions on Google.

### [ResponseMediaObject](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Intent.Message.MediaContent.ResponseMediaObject)

Response media object for media content card.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ResponseMediaType](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Intent.Message.MediaContent.ResponseMediaType)

Format of response media type.

### [Platform](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Intent.Message.Platform)

Represents different platforms that a rich message can be intended for.

### [QuickReplies](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Intent.Message.QuickReplies)

The quick replies response message.

### [RbmCardContent](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Intent.Message.RbmCardContent)

Rich Business Messaging (RBM) Card content

### [RbmMedia](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Intent.Message.RbmCardContent.RbmMedia)

Rich Business Messaging (RBM) Media displayed in Cards The following media-types are currently supported:

Image Types

  * image/jpeg
  * image/jpg'
  * image/gif
  * image/png



Video Types

  * video/h263
  * video/m4v
  * video/mp4
  * video/mpeg
  * video/mpeg4
  * video/webm



### [Height](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Intent.Message.RbmCardContent.RbmMedia.Height)

Media height

### [RbmCarouselCard](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Intent.Message.RbmCarouselCard)

Carousel Rich Business Messaging (RBM) rich card.

Rich cards allow you to respond to users with more vivid content, e.g. with media and suggestions.

If you want to show a single card with more control over the layout, please use RbmStandaloneCard instead.

### [CardWidth](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Intent.Message.RbmCarouselCard.CardWidth)

The width of the cards in the carousel.

### [RbmStandaloneCard](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Intent.Message.RbmStandaloneCard)

Standalone Rich Business Messaging (RBM) rich card.

Rich cards allow you to respond to users with more vivid content, e.g. with media and suggestions.

You can group multiple rich cards into one using RbmCarouselCard but carousel cards will give you less control over the card layout.

### [CardOrientation](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Intent.Message.RbmStandaloneCard.CardOrientation)

Orientation of the card.

### [ThumbnailImageAlignment](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Intent.Message.RbmStandaloneCard.ThumbnailImageAlignment)

Thumbnail preview alignment for standalone cards with horizontal layout.

### [RbmSuggestedAction](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Intent.Message.RbmSuggestedAction)

Rich Business Messaging (RBM) suggested client-side action that the user can choose from the card.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [RbmSuggestedActionDial](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Intent.Message.RbmSuggestedAction.RbmSuggestedActionDial)

Opens the user's default dialer app with the specified phone number but does not dial automatically.

### [RbmSuggestedActionOpenUri](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Intent.Message.RbmSuggestedAction.RbmSuggestedActionOpenUri)

Opens the user's default web browser app to the specified uri If the user has an app installed that is registered as the default handler for the URL, then this app will be opened instead, and its icon will be used in the suggested action UI.

### [RbmSuggestedActionShareLocation](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Intent.Message.RbmSuggestedAction.RbmSuggestedActionShareLocation)

Opens the device's location chooser so the user can pick a location to send back to the agent.

### [RbmSuggestedReply](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Intent.Message.RbmSuggestedReply)

Rich Business Messaging (RBM) suggested reply that the user can click instead of typing in their own response.

### [RbmSuggestion](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Intent.Message.RbmSuggestion)

Rich Business Messaging (RBM) suggestion. Suggestions allow user to easily select/click a predefined response or perform an action (like opening a web uri).

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [RbmText](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Intent.Message.RbmText)

Rich Business Messaging (RBM) text response with suggestions.

### [SelectItemInfo](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Intent.Message.SelectItemInfo)

Additional info about the select item for when it is triggered in a dialog.

### [SimpleResponse](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Intent.Message.SimpleResponse)

The simple response message containing speech or text.

### [SimpleResponses](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Intent.Message.SimpleResponses)

The collection of simple response candidates. This message in `QueryResult.fulfillment_messages` and `WebhookResponse.fulfillment_messages` should contain only one `SimpleResponse`.

### [Suggestion](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Intent.Message.Suggestion)

The suggestion chip message that the user can tap to quickly post a reply to the conversation.

### [Suggestions](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Intent.Message.Suggestions)

The collection of suggestions.

### [TableCard](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Intent.Message.TableCard)

Table card for Actions on Google.

### [TableCardCell](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Intent.Message.TableCardCell)

Cell of TableCardRow.

### [TableCardRow](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Intent.Message.TableCardRow)

Row of TableCard.

### [TelephonyPlayAudio](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Intent.Message.TelephonyPlayAudio)

Plays audio from a file in Telephony Gateway.

### [TelephonySynthesizeSpeech](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Intent.Message.TelephonySynthesizeSpeech)

Synthesizes speech and plays back the synthesized audio to the caller in Telephony Gateway.

Telephony Gateway takes the synthesizer settings from `DetectIntentResponse.output_audio_config` which can either be set at request-level or can come from the agent-level synthesizer config.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [TelephonyTransferCall](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Intent.Message.TelephonyTransferCall)

Transfers the call in Telephony Gateway.

### [Text](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Intent.Message.Text)

The text response message.

### [Parameter](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Intent.Parameter)

Represents intent parameters.

### [TrainingPhrase](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Intent.TrainingPhrase)

Represents an example that the agent is trained on.

### [Part](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Intent.TrainingPhrase.Part)

Represents a part of a training phrase.

### [Type](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Intent.TrainingPhrase.Type)

Represents different types of training phrases.

### [WebhookState](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Intent.WebhookState)

Represents the different states that webhooks can be in.

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

### [Answer](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.KnowledgeAnswers.Answer)

An answer from Knowledge Connector.

### [MatchConfidenceLevel](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.KnowledgeAnswers.Answer.MatchConfidenceLevel)

Represents the system's confidence that this knowledge answer is a good match for this conversational query.

### [KnowledgeAssistAnswer](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.KnowledgeAssistAnswer)

Represents a Knowledge Assist answer.

### [AdditionalSuggestedQueryResult](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.KnowledgeAssistAnswer.AdditionalSuggestedQueryResult)

Represents a single suggested query result.

### [KnowledgeAnswer](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.KnowledgeAssistAnswer.KnowledgeAnswer)

Represents an answer from Knowledge. Currently supports FAQ and Generative answers.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [EventSource](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.KnowledgeAssistAnswer.KnowledgeAnswer.EventSource)

Details about source of Event answer.

### [FaqSource](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.KnowledgeAssistAnswer.KnowledgeAnswer.FaqSource)

Details about source of FAQ answer.

### [GenerativeSource](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.KnowledgeAssistAnswer.KnowledgeAnswer.GenerativeSource)

Details about source of Generative answer.

### [Snippet](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.KnowledgeAssistAnswer.KnowledgeAnswer.GenerativeSource.Snippet)

Snippet Source for a Generative Prediction.

### [SuggestedQuery](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.KnowledgeAssistAnswer.SuggestedQuery)

Represents a suggested query.

### [SearchContext](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.KnowledgeAssistAnswer.SuggestedQuery.SearchContext)

Search context is information useful for knowledge search that helps enrich the query. Example: search_context { key: "application name" value: "DesignApp" }

### [KnowledgeAssistDebugInfo](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.KnowledgeAssistDebugInfo)

Debug information related to Knowledge Assist feature.

### [KnowledgeAssistBehavior](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.KnowledgeAssistDebugInfo.KnowledgeAssistBehavior)

Configured behaviors for Knowedge Assist.

### [QueryCategorizationFailureReason](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.KnowledgeAssistDebugInfo.QueryCategorizationFailureReason)

Reason for query categorization failure.

### [QueryGenerationDebugInfo](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.KnowledgeAssistDebugInfo.QueryGenerationDebugInfo)

Token usage metadata for query generation.

### [QueryGenerationFailureReason](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.KnowledgeAssistDebugInfo.QueryGenerationFailureReason)

Reason for query generation failure.
    
    
        1. The trigger_event is CUSTOMER_MESSAGE or UNSPECIFIED, but
           the last message is not from the customer.
        2. The trigger_event is AGENT_MESSAGE, but the last message
           is not from the agent.
    

### [KnowledgeBase](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.KnowledgeBase)

A knowledge base represents a collection of knowledge documents that you provide to Dialogflow. Your knowledge documents contain information that may be useful during conversations with end-users. Some Dialogflow features use knowledge bases when looking for a response to an end-user input.

For more information, see the `knowledge base guide <https://cloud.google.com/dialogflow/docs/how/knowledge-bases>`__.

Note: The `projects.agent.knowledgeBases` resource is deprecated; only use `projects.knowledgeBases`.

### [KnowledgeOperationMetadata](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.KnowledgeOperationMetadata)

Metadata in google::longrunning::Operation for Knowledge operations.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [State](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.KnowledgeOperationMetadata.State)

States of the operation.

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

### [Role](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.MessageEntry.Role)

Enumeration of the roles a participant can play in a conversation.

### [NotificationConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.NotificationConfig)

Defines notification behavior.

### [MessageFormat](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.NotificationConfig.MessageFormat)

Format of cloud pub/sub message.

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

### [AgentDesktopSource](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Participant.AgentDesktopSource)

Enumeration of the Agent Desktop Source when using prebuilt Agent Assist integration modules.

### [DocumentsMetadataFiltersEntry](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Participant.DocumentsMetadataFiltersEntry)

The abstract base class for a message.

### [Role](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Participant.Role)

Enumeration of the roles a participant can play in a conversation.

### [PhoneNumber](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.PhoneNumber)

Represents a phone number. `PhoneNumber` resources enable phone calls to be answered by Dialogflow services and are added to a project through a PhoneNumberOrder.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AllowedSipTrunks](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.PhoneNumber.AllowedSipTrunks)

List of SIP trunks that are allowed to make calls to this phone number.

### [LifecycleState](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.PhoneNumber.LifecycleState)

The states that a `PhoneNumber` can be in.

### [ProbeDetails](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ProbeDetails)

The probe details of Sip Trunk peer hostname.

### [ProbeStatus](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ProbeDetails.ProbeStatus)

The status of InitiateSipOptionsPing to peer hostname.

### [QueryInput](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.QueryInput)

Represents the query input. It can contain either:

  1. An audio config which instructs the speech recognizer how to process the speech audio.

  2. A conversational query in the form of text.

  3. An event that specifies which intent to trigger.




This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [QueryParameters](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.QueryParameters)

Represents the parameters of the conversational query.

### [WebhookHeadersEntry](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.QueryParameters.WebhookHeadersEntry)

The abstract base class for a message.

### [QueryResult](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.QueryResult)

Represents the result of conversational query or event processing.

### [RaiSettings](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.RaiSettings)

Settings for Responsible AI checks.

### [RaiCategoryConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.RaiSettings.RaiCategoryConfig)

Configuration for a specific RAI category.

### [RaiCategory](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.RaiSettings.RaiCategoryConfig.RaiCategory)

Enum for RAI category.

### [SensitivityLevel](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.RaiSettings.RaiCategoryConfig.SensitivityLevel)

Enum for user-configurable sensitivity levels.
    
    
        - DANGEROUS_CONTENT: BLOCK_FEW
        - SEXUALLY_EXPLICIT: BLOCK_SOME
        - HARASSMENT: BLOCK_SOME
        - HATE_SPEECH: BLOCK_SOME
    BLOCK_MOST (1):
        Block most potentially sensitive responses.
    BLOCK_SOME (2):
        Block some potentially sensitive responses.
    BLOCK_FEW (3):
        Block a few potentially sensitive responses.
    BLOCK_NONE (4):
        No filtering for this category.
    

### [ReloadDocumentRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ReloadDocumentRequest)

Request message for Documents.ReloadDocument.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ResponseMessage](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ResponseMessage)

Response messages from an automated agent.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [EndInteraction](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ResponseMessage.EndInteraction)

Indicates that interaction with the Dialogflow agent has ended.

### [LiveAgentHandoff](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ResponseMessage.LiveAgentHandoff)

Indicates that the conversation should be handed off to a human agent.

Dialogflow only uses this to determine which conversations were handed off to a human agent for measurement purposes. What else to do with this signal is up to you and your handoff procedures.

You may set this, for example:

  * In the entry fulfillment of a Dialogflow CX Page if entering the page indicates something went extremely wrong in the conversation.
  * In a webhook response when you determine that the customer issue can only be handled by a human.



### [MixedAudio](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ResponseMessage.MixedAudio)

Represents an audio message that is composed of both segments synthesized from the Dialogflow agent prompts and ones hosted externally at the specified URIs.

### [Segment](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ResponseMessage.MixedAudio.Segment)

Represents one segment of audio.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [TelephonyTransferCall](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ResponseMessage.TelephonyTransferCall)

Represents the signal that telles the client to transfer the phone call connected to the agent to a third-party endpoint.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Text](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ResponseMessage.Text)

The text response message.

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

### [AnswerSource](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SearchKnowledgeAnswer.AnswerSource)

The sources of the answers.

### [AnswerType](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SearchKnowledgeAnswer.AnswerType)

The type of the answer.

### [SearchKnowledgeDebugInfo](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SearchKnowledgeDebugInfo)

Debug information related to SearchKnowledge feature.

### [SearchKnowledgeBehavior](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SearchKnowledgeDebugInfo.SearchKnowledgeBehavior)

Configured behaviors for SearchKnowledge.

### [SearchKnowledgeRequest](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SearchKnowledgeRequest)

The request message for Conversations.SearchKnowledge.

### [QuerySource](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SearchKnowledgeRequest.QuerySource)

The source of the query. We use QuerySource to distinguish queries directly entered by agents and suggested queries from Participants.SuggestKnowledgeAssist. If SUGGESTED_QUERY source is specified, we will treat it as a continuation of a SuggestKnowledgeAssist call.

### [SearchConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SearchKnowledgeRequest.SearchConfig)

Configuration specific to search queries with data stores.

### [BoostSpecs](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SearchKnowledgeRequest.SearchConfig.BoostSpecs)

Boost specifications for data stores.

Maps from datastore name to their boost configuration. Do not specify more than one BoostSpecs for each datastore name. If multiple BoostSpecs are provided for the same datastore name, the behavior is undefined.

### [BoostSpec](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SearchKnowledgeRequest.SearchConfig.BoostSpecs.BoostSpec)

Boost specification to boost certain documents. A copy of google.cloud.discoveryengine.v1main.BoostSpec, field documentation is available at <https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/BoostSpec>

### [ConditionBoostSpec](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SearchKnowledgeRequest.SearchConfig.BoostSpecs.BoostSpec.ConditionBoostSpec)

Boost applies to documents which match a condition.

### [BoostControlSpec](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SearchKnowledgeRequest.SearchConfig.BoostSpecs.BoostSpec.ConditionBoostSpec.BoostControlSpec)

Specification for custom ranking based on customer specified attribute value. It provides more controls for customized ranking than the simple (condition, boost) combination above.

### [AttributeType](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SearchKnowledgeRequest.SearchConfig.BoostSpecs.BoostSpec.ConditionBoostSpec.BoostControlSpec.AttributeType)

The attribute(or function) for which the custom ranking is to be applied.

### [ControlPoint](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SearchKnowledgeRequest.SearchConfig.BoostSpecs.BoostSpec.ConditionBoostSpec.BoostControlSpec.ControlPoint)

The control points used to define the curve. The curve defined through these control points can only be monotonically increasing or decreasing(constant values are acceptable).

### [InterpolationType](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SearchKnowledgeRequest.SearchConfig.BoostSpecs.BoostSpec.ConditionBoostSpec.BoostControlSpec.InterpolationType)

The interpolation type to be applied. Default will be linear (Piecewise Linear).

### [FilterSpecs](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SearchKnowledgeRequest.SearchConfig.FilterSpecs)

Filter specification for data store queries.

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

### [InternalServiceLatency](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ServiceLatency.InternalServiceLatency)

Message to represent the latency of an internal service.

### [SessionEntityType](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SessionEntityType)

A session represents a conversation between a Dialogflow agent and an end-user. You can create special entities, called session entities, during a session. Session entities can extend or replace custom entity types and only exist during the session that they were created for. All session data, including session entities, is stored by Dialogflow for 20 minutes.

For more information, see the `session entity guide <https://cloud.google.com/dialogflow/docs/entities-session>`__.

### [EntityOverrideMode](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SessionEntityType.EntityOverrideMode)

The types of modifications for a session entity type.
    
    
        Note: Even in this override mode calls to
        `ListSessionEntityTypes`, `GetSessionEntityType`,
        `CreateSessionEntityType` and `UpdateSessionEntityType`
        only return the additional entities added in this session
        entity type. If you want to get the supplemented list,
        please call
        <xref uid="google.cloud.dialogflow.v2beta1.EntityTypes.GetEntityType">EntityTypes.GetEntityType</xref>
        on the custom entity type and merge.
    

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

### [ConnectionState](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SipHostname.ConnectionState)

The state of SBC hostname connection.

### [HostnameCertificateState](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SipHostname.HostnameCertificateState)

The state of Sip Trunk certificate authentication.

### [HostnameErrorDetails](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SipHostname.HostnameErrorDetails)

The error details of Sip Trunk hostnameconnection authentication.

### [SipTrunk](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SipTrunk)

SipTrunk is the resource that represents a SIP trunk to connect to Google Telephony platform SIP trunking service.

### [GoogleRootCertFile](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SipTrunk.GoogleRootCertFile)

The type of Google root certificate file used for mTLS.

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

### [MessageType](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.StreamingRecognitionResult.MessageType)

Type of the response message.

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

### [Summary](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SuggestConversationSummaryResponse.Summary)

Generated summary for a conversation.

### [SummarySection](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SuggestConversationSummaryResponse.Summary.SummarySection)

A component of the generated summary.

### [TextSectionsEntry](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SuggestConversationSummaryResponse.Summary.TextSectionsEntry)

The abstract base class for a message.

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

### [Article](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Suggestion.Article)

Represents suggested article.

### [MetadataEntry](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Suggestion.Article.MetadataEntry)

The abstract base class for a message.

### [FaqAnswer](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Suggestion.FaqAnswer)

Represents suggested answer from "frequently asked questions".

### [MetadataEntry](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Suggestion.FaqAnswer.MetadataEntry)

The abstract base class for a message.

### [SuggestionDedupingConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SuggestionDedupingConfig)

Config for suggestion deduping. NEXT_ID: 3

### [SuggestionFeature](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SuggestionFeature)

The type of Human Agent Assistant API suggestion to perform, and the maximum number of results to return for that type. Multiple `Feature` objects can be specified in the `features` list.

### [Type](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SuggestionFeature.Type)

Defines the type of Human Agent Assistant feature.

### [SuggestionInput](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SuggestionInput)

Represents the action to take for a tool call that requires confirmation.

### [Action](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SuggestionInput.Action)

Indicate what type of action to take with the tool call.

### [SuggestionResult](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SuggestionResult)

One response of different type of suggestion response which is used in the response of Participants.AnalyzeContent and Participants.AnalyzeContent, as well as HumanAgentAssistantEvent.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [SummarizationContext](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SummarizationContext)

Summarization context that customer can configure.

### [SummarizationEvaluationMetrics](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SummarizationEvaluationMetrics)

Evaluation metrics for summarization generator.

### [AccuracyDecomposition](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SummarizationEvaluationMetrics.AccuracyDecomposition)

Decomposition details for accuracy.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AdherenceDecomposition](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SummarizationEvaluationMetrics.AdherenceDecomposition)

Decomposition details for adherence.

### [AdherenceRubric](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SummarizationEvaluationMetrics.AdherenceRubric)

Rubric result of the adherence evaluation. A rubric is ued to determine if the summary adheres to all aspects of the given instructions.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [CompletenessRubric](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SummarizationEvaluationMetrics.CompletenessRubric)

Rubric details of the completeness evaluation result.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ConversationDetail](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SummarizationEvaluationMetrics.ConversationDetail)

Aggregated evaluation result on conversation level. This contains evaluation results of all the metrics and sections.

### [MetricDetail](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SummarizationEvaluationMetrics.ConversationDetail.MetricDetail)

Aggregated result on metric level. This contains the evaluation results of all the sections.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [SectionDetail](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SummarizationEvaluationMetrics.ConversationDetail.MetricDetail.SectionDetail)

Section level result.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Decomposition](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SummarizationEvaluationMetrics.Decomposition)

Decomposition details

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [EvaluationResult](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SummarizationEvaluationMetrics.EvaluationResult)

Evaluation result that contains one of accuracy, adherence or completeness evaluation result.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [OverallScoresByMetric](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SummarizationEvaluationMetrics.OverallScoresByMetric)

Overall performance per metric. This is the aggregated score for each metric across all conversations that are selected for summarization evaluation.

### [SectionToken](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SummarizationEvaluationMetrics.SectionToken)

A pair of section name and input token count of the input summary section.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [SummarizationEvaluationResult](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SummarizationEvaluationMetrics.SummarizationEvaluationResult)

Evaluation result per conversation(&summary), metric and section.

### [SummarizationSection](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SummarizationSection)

Represents the section of summarization.

### [Type](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SummarizationSection.Type)

Type enum of the summarization sections.

### [SummarizationSectionList](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SummarizationSectionList)

List of summarization sections.

### [SummarySuggestion](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SummarySuggestion)

Suggested summary of the conversation.

### [SummarySection](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SummarySuggestion.SummarySection)

A component of the generated summary.

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

### [SynthesizeSpeechConfigsEntry](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.TextToSpeechSettings.SynthesizeSpeechConfigsEntry)

The abstract base class for a message.

### [Tool](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Tool)

Represents a tool.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ActionConfirmationRequirementEntry](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Tool.ActionConfirmationRequirementEntry)

The abstract base class for a message.

### [Authentication](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Tool.Authentication)

Authentication information required for API calls

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ApiKeyConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Tool.Authentication.ApiKeyConfig)

Config for authentication with API key.

### [BearerTokenConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Tool.Authentication.BearerTokenConfig)

Config for authentication using bearer token.

### [OAuthConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Tool.Authentication.OAuthConfig)

Config for authentication with OAuth.

### [OauthGrantType](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Tool.Authentication.OAuthConfig.OauthGrantType)

OAuth grant types. Only `client credential grant <https://oauth.net/2/grant-types/client-credentials>`__ is supported.

### [RequestLocation](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Tool.Authentication.RequestLocation)

The location of the API key in the request.

### [ServiceAgentAuthConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Tool.Authentication.ServiceAgentAuthConfig)

Config for auth using `Dialogflow service agent <https://cloud.google.com/iam/docs/service-agents#dialogflow-service-agent>`__.

### [ServiceAgentAuth](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Tool.Authentication.ServiceAgentAuthConfig.ServiceAgentAuth)

Indicate the auth token type generated from the `Diaglogflow service agent <https://cloud.google.com/iam/docs/service-agents#dialogflow-service-agent>`__.

### [ConfirmationRequirement](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Tool.ConfirmationRequirement)

Types of confirmation requirement.

### [ConnectorTool](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Tool.ConnectorTool)

A ConnectorTool enabling using Integration Connectors Connections as tools.

### [Action](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Tool.ConnectorTool.Action)

Configuration of a Connection operation for the tool to use.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [EntityOperation](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Tool.ConnectorTool.Action.EntityOperation)

Entity CRUD operation specification.

### [OperationType](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Tool.ConnectorTool.Action.EntityOperation.OperationType)

The operation to perform on the entity.

### [ExtensionTool](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Tool.ExtensionTool)

An ExtensionTool is a way to use Vertex Extensions as a tool.

### [FunctionTool](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Tool.FunctionTool)

A Function tool describes the functions to be invoked on the client side.

### [MethodType](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Tool.MethodType)

The method type of the function.

### [OpenApiTool](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Tool.OpenApiTool)

An OpenAPI tool is a way to provide the Tool specifications in the Open API schema format.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ServiceDirectoryConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Tool.ServiceDirectoryConfig)

Configuration for tools using Service Directory.

### [TLSConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Tool.TLSConfig)

The TLS configuration.

### [CACert](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Tool.TLSConfig.CACert)

The CA certificate.

### [ToolCall](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ToolCall)

Represents a call of a specific tool's action with the specified inputs.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [State](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ToolCall.State)

Tool call states.

### [ToolCallResult](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ToolCallResult)

The result of calling a tool's action.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Error](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ToolCallResult.Error)

An error produced by the tool call.

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

### [Severity](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ValidationError.Severity)

Represents a level of severity.

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

### [VersionStatus](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Version.VersionStatus)

The status of a version.

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

## Modules 

### [pagers](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.agents.pagers)

API documentation for `dialogflow_v2.services.agents.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.answer_records.pagers)

API documentation for `dialogflow_v2.services.answer_records.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.companion_agents.pagers)

API documentation for `dialogflow_v2.services.companion_agents.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.contexts.pagers)

API documentation for `dialogflow_v2.services.contexts.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.conversation_datasets.pagers)

API documentation for `dialogflow_v2.services.conversation_datasets.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.conversation_models.pagers)

API documentation for `dialogflow_v2.services.conversation_models.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.conversation_profiles.pagers)

API documentation for `dialogflow_v2.services.conversation_profiles.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.conversations.pagers)

API documentation for `dialogflow_v2.services.conversations.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.documents.pagers)

API documentation for `dialogflow_v2.services.documents.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.entity_types.pagers)

API documentation for `dialogflow_v2.services.entity_types.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.environments.pagers)

API documentation for `dialogflow_v2.services.environments.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.generator_evaluations.pagers)

API documentation for `dialogflow_v2.services.generator_evaluations.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.generators.pagers)

API documentation for `dialogflow_v2.services.generators.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.intents.pagers)

API documentation for `dialogflow_v2.services.intents.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.knowledge_bases.pagers)

API documentation for `dialogflow_v2.services.knowledge_bases.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.participants.pagers)

API documentation for `dialogflow_v2.services.participants.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.session_entity_types.pagers)

API documentation for `dialogflow_v2.services.session_entity_types.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.sip_trunks.pagers)

API documentation for `dialogflow_v2.services.sip_trunks.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.tools.pagers)

API documentation for `dialogflow_v2.services.tools.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2.services.versions.pagers)

API documentation for `dialogflow_v2.services.versions.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.agents.pagers)

API documentation for `dialogflow_v2beta1.services.agents.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.answer_records.pagers)

API documentation for `dialogflow_v2beta1.services.answer_records.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.contexts.pagers)

API documentation for `dialogflow_v2beta1.services.contexts.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.conversation_profiles.pagers)

API documentation for `dialogflow_v2beta1.services.conversation_profiles.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.conversations.pagers)

API documentation for `dialogflow_v2beta1.services.conversations.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.documents.pagers)

API documentation for `dialogflow_v2beta1.services.documents.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.entity_types.pagers)

API documentation for `dialogflow_v2beta1.services.entity_types.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.environments.pagers)

API documentation for `dialogflow_v2beta1.services.environments.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.generator_evaluations.pagers)

API documentation for `dialogflow_v2beta1.services.generator_evaluations.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.generators.pagers)

API documentation for `dialogflow_v2beta1.services.generators.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.intents.pagers)

API documentation for `dialogflow_v2beta1.services.intents.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.knowledge_bases.pagers)

API documentation for `dialogflow_v2beta1.services.knowledge_bases.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.participants.pagers)

API documentation for `dialogflow_v2beta1.services.participants.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.phone_numbers.pagers)

API documentation for `dialogflow_v2beta1.services.phone_numbers.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.session_entity_types.pagers)

API documentation for `dialogflow_v2beta1.services.session_entity_types.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.sip_trunks.pagers)

API documentation for `dialogflow_v2beta1.services.sip_trunks.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.tools.pagers)

API documentation for `dialogflow_v2beta1.services.tools.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.services.versions.pagers)

API documentation for `dialogflow_v2beta1.services.versions.pagers` module.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
