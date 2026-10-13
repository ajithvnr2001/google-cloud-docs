---
url: https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/summary_class/
title: Package Classes (0.20.5) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:59:21.942800+00:00
---

# Package Classes (0.20.5)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/summary_class/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package Classes (0.20.5) Stay organized with collections  Save and categorize content based on your preferences. 

0.20.5 (latest)  0.20.4  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.12  0.12.3  0.11.14  0.10.0  0.9.1  0.8.1  0.7.0  0.6.0  0.5.0  0.4.1  0.3.1  0.2.1  0.1.1 

Summary of entries of Classes for discoveryengine.

## Classes 

### [AssistantServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.assistant_service.AssistantServiceAsyncClient)

Service for managing Assistant configuration and assisting users.

### [AssistantServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.assistant_service.AssistantServiceClient)

Service for managing Assistant configuration and assisting users.

### [CmekConfigServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.cmek_config_service.CmekConfigServiceAsyncClient)

Service for managing CMEK related tasks

### [CmekConfigServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.cmek_config_service.CmekConfigServiceClient)

Service for managing CMEK related tasks

### [CompletionServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.completion_service.CompletionServiceAsyncClient)

Service for Auto-Completion.

### [CompletionServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.completion_service.CompletionServiceClient)

Service for Auto-Completion.

### [ControlServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.control_service.ControlServiceAsyncClient)

Service for performing CRUD operations on Controls. Controls allow for custom logic to be implemented in the serving path. Controls need to be attached to a Serving Config to be considered during a request.

### [ControlServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.control_service.ControlServiceClient)

Service for performing CRUD operations on Controls. Controls allow for custom logic to be implemented in the serving path. Controls need to be attached to a Serving Config to be considered during a request.

### [ListControlsAsyncPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.control_service.pagers.ListControlsAsyncPager)

A pager for iterating through `list_controls` requests.

This class thinly wraps an initial [ListControlsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListControlsResponse) object, and provides an `__aiter__` method to iterate through its `controls` field.

If there are more pages, the `__aiter__` method will make additional `ListControls` requests and continue to iterate through the `controls` field on the corresponding responses.

All the usual [ListControlsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListControlsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListControlsPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.control_service.pagers.ListControlsPager)

A pager for iterating through `list_controls` requests.

This class thinly wraps an initial [ListControlsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListControlsResponse) object, and provides an `__iter__` method to iterate through its `controls` field.

If there are more pages, the `__iter__` method will make additional `ListControls` requests and continue to iterate through the `controls` field on the corresponding responses.

All the usual [ListControlsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListControlsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ConversationalSearchServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.conversational_search_service.ConversationalSearchServiceAsyncClient)

Service for conversational search.

### [ConversationalSearchServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.conversational_search_service.ConversationalSearchServiceClient)

Service for conversational search.

### [ListConversationsAsyncPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.conversational_search_service.pagers.ListConversationsAsyncPager)

A pager for iterating through `list_conversations` requests.

This class thinly wraps an initial [ListConversationsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListConversationsResponse) object, and provides an `__aiter__` method to iterate through its `conversations` field.

If there are more pages, the `__aiter__` method will make additional `ListConversations` requests and continue to iterate through the `conversations` field on the corresponding responses.

All the usual [ListConversationsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListConversationsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListConversationsPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.conversational_search_service.pagers.ListConversationsPager)

A pager for iterating through `list_conversations` requests.

This class thinly wraps an initial [ListConversationsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListConversationsResponse) object, and provides an `__iter__` method to iterate through its `conversations` field.

If there are more pages, the `__iter__` method will make additional `ListConversations` requests and continue to iterate through the `conversations` field on the corresponding responses.

All the usual [ListConversationsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListConversationsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListSessionsAsyncPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.conversational_search_service.pagers.ListSessionsAsyncPager)

A pager for iterating through `list_sessions` requests.

This class thinly wraps an initial [ListSessionsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListSessionsResponse) object, and provides an `__aiter__` method to iterate through its `sessions` field.

If there are more pages, the `__aiter__` method will make additional `ListSessions` requests and continue to iterate through the `sessions` field on the corresponding responses.

All the usual [ListSessionsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListSessionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListSessionsPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.conversational_search_service.pagers.ListSessionsPager)

A pager for iterating through `list_sessions` requests.

This class thinly wraps an initial [ListSessionsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListSessionsResponse) object, and provides an `__iter__` method to iterate through its `sessions` field.

If there are more pages, the `__iter__` method will make additional `ListSessions` requests and continue to iterate through the `sessions` field on the corresponding responses.

All the usual [ListSessionsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListSessionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [DataStoreServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.data_store_service.DataStoreServiceAsyncClient)

Service for managing DataStore configuration.

### [DataStoreServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.data_store_service.DataStoreServiceClient)

Service for managing DataStore configuration.

### [ListDataStoresAsyncPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.data_store_service.pagers.ListDataStoresAsyncPager)

A pager for iterating through `list_data_stores` requests.

This class thinly wraps an initial [ListDataStoresResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListDataStoresResponse) object, and provides an `__aiter__` method to iterate through its `data_stores` field.

If there are more pages, the `__aiter__` method will make additional `ListDataStores` requests and continue to iterate through the `data_stores` field on the corresponding responses.

All the usual [ListDataStoresResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListDataStoresResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListDataStoresPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.data_store_service.pagers.ListDataStoresPager)

A pager for iterating through `list_data_stores` requests.

This class thinly wraps an initial [ListDataStoresResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListDataStoresResponse) object, and provides an `__iter__` method to iterate through its `data_stores` field.

If there are more pages, the `__iter__` method will make additional `ListDataStores` requests and continue to iterate through the `data_stores` field on the corresponding responses.

All the usual [ListDataStoresResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListDataStoresResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [DocumentServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.document_service.DocumentServiceAsyncClient)

Service for ingesting Document information of the customer's website.

### [DocumentServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.document_service.DocumentServiceClient)

Service for ingesting Document information of the customer's website.

### [ListDocumentsAsyncPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.document_service.pagers.ListDocumentsAsyncPager)

A pager for iterating through `list_documents` requests.

This class thinly wraps an initial [ListDocumentsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListDocumentsResponse) object, and provides an `__aiter__` method to iterate through its `documents` field.

If there are more pages, the `__aiter__` method will make additional `ListDocuments` requests and continue to iterate through the `documents` field on the corresponding responses.

All the usual [ListDocumentsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListDocumentsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListDocumentsPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.document_service.pagers.ListDocumentsPager)

A pager for iterating through `list_documents` requests.

This class thinly wraps an initial [ListDocumentsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListDocumentsResponse) object, and provides an `__iter__` method to iterate through its `documents` field.

If there are more pages, the `__iter__` method will make additional `ListDocuments` requests and continue to iterate through the `documents` field on the corresponding responses.

All the usual [ListDocumentsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListDocumentsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [EngineServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.engine_service.EngineServiceAsyncClient)

Service for managing Engine configuration.

### [EngineServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.engine_service.EngineServiceClient)

Service for managing Engine configuration.

### [ListEnginesAsyncPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.engine_service.pagers.ListEnginesAsyncPager)

A pager for iterating through `list_engines` requests.

This class thinly wraps an initial [ListEnginesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListEnginesResponse) object, and provides an `__aiter__` method to iterate through its `engines` field.

If there are more pages, the `__aiter__` method will make additional `ListEngines` requests and continue to iterate through the `engines` field on the corresponding responses.

All the usual [ListEnginesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListEnginesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListEnginesPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.engine_service.pagers.ListEnginesPager)

A pager for iterating through `list_engines` requests.

This class thinly wraps an initial [ListEnginesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListEnginesResponse) object, and provides an `__iter__` method to iterate through its `engines` field.

If there are more pages, the `__iter__` method will make additional `ListEngines` requests and continue to iterate through the `engines` field on the corresponding responses.

All the usual [ListEnginesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListEnginesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [GroundedGenerationServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.grounded_generation_service.GroundedGenerationServiceAsyncClient)

Service for grounded generation.

### [GroundedGenerationServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.grounded_generation_service.GroundedGenerationServiceClient)

Service for grounded generation.

### [IdentityMappingStoreServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.identity_mapping_store_service.IdentityMappingStoreServiceAsyncClient)

Service for managing Identity Mapping Stores.

### [IdentityMappingStoreServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.identity_mapping_store_service.IdentityMappingStoreServiceClient)

Service for managing Identity Mapping Stores.

### [ListIdentityMappingStoresAsyncPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.identity_mapping_store_service.pagers.ListIdentityMappingStoresAsyncPager)

A pager for iterating through `list_identity_mapping_stores` requests.

This class thinly wraps an initial [ListIdentityMappingStoresResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListIdentityMappingStoresResponse) object, and provides an `__aiter__` method to iterate through its `identity_mapping_stores` field.

If there are more pages, the `__aiter__` method will make additional `ListIdentityMappingStores` requests and continue to iterate through the `identity_mapping_stores` field on the corresponding responses.

All the usual [ListIdentityMappingStoresResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListIdentityMappingStoresResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListIdentityMappingStoresPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.identity_mapping_store_service.pagers.ListIdentityMappingStoresPager)

A pager for iterating through `list_identity_mapping_stores` requests.

This class thinly wraps an initial [ListIdentityMappingStoresResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListIdentityMappingStoresResponse) object, and provides an `__iter__` method to iterate through its `identity_mapping_stores` field.

If there are more pages, the `__iter__` method will make additional `ListIdentityMappingStores` requests and continue to iterate through the `identity_mapping_stores` field on the corresponding responses.

All the usual [ListIdentityMappingStoresResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListIdentityMappingStoresResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListIdentityMappingsAsyncPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.identity_mapping_store_service.pagers.ListIdentityMappingsAsyncPager)

A pager for iterating through `list_identity_mappings` requests.

This class thinly wraps an initial [ListIdentityMappingsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListIdentityMappingsResponse) object, and provides an `__aiter__` method to iterate through its `identity_mapping_entries` field.

If there are more pages, the `__aiter__` method will make additional `ListIdentityMappings` requests and continue to iterate through the `identity_mapping_entries` field on the corresponding responses.

All the usual [ListIdentityMappingsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListIdentityMappingsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListIdentityMappingsPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.identity_mapping_store_service.pagers.ListIdentityMappingsPager)

A pager for iterating through `list_identity_mappings` requests.

This class thinly wraps an initial [ListIdentityMappingsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListIdentityMappingsResponse) object, and provides an `__iter__` method to iterate through its `identity_mapping_entries` field.

If there are more pages, the `__iter__` method will make additional `ListIdentityMappings` requests and continue to iterate through the `identity_mapping_entries` field on the corresponding responses.

All the usual [ListIdentityMappingsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListIdentityMappingsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ProjectServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.project_service.ProjectServiceAsyncClient)

Service for operations on the Project.

### [ProjectServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.project_service.ProjectServiceClient)

Service for operations on the Project.

### [RankServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.rank_service.RankServiceAsyncClient)

Service for ranking text records.

### [RankServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.rank_service.RankServiceClient)

Service for ranking text records.

### [RecommendationServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.recommendation_service.RecommendationServiceAsyncClient)

Service for making recommendations.

### [RecommendationServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.recommendation_service.RecommendationServiceClient)

Service for making recommendations.

### [SchemaServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.schema_service.SchemaServiceAsyncClient)

Service for managing Schemas.

### [SchemaServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.schema_service.SchemaServiceClient)

Service for managing Schemas.

### [ListSchemasAsyncPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.schema_service.pagers.ListSchemasAsyncPager)

A pager for iterating through `list_schemas` requests.

This class thinly wraps an initial [ListSchemasResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListSchemasResponse) object, and provides an `__aiter__` method to iterate through its `schemas` field.

If there are more pages, the `__aiter__` method will make additional `ListSchemas` requests and continue to iterate through the `schemas` field on the corresponding responses.

All the usual [ListSchemasResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListSchemasResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListSchemasPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.schema_service.pagers.ListSchemasPager)

A pager for iterating through `list_schemas` requests.

This class thinly wraps an initial [ListSchemasResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListSchemasResponse) object, and provides an `__iter__` method to iterate through its `schemas` field.

If there are more pages, the `__iter__` method will make additional `ListSchemas` requests and continue to iterate through the `schemas` field on the corresponding responses.

All the usual [ListSchemasResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListSchemasResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [SearchServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.search_service.SearchServiceAsyncClient)

Service for search.

### [SearchServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.search_service.SearchServiceClient)

Service for search.

### [SearchAsyncPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.search_service.pagers.SearchAsyncPager)

A pager for iterating through `search` requests.

This class thinly wraps an initial [SearchResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchResponse) object, and provides an `__aiter__` method to iterate through its `results` field.

If there are more pages, the `__aiter__` method will make additional `Search` requests and continue to iterate through the `results` field on the corresponding responses.

All the usual [SearchResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [SearchLiteAsyncPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.search_service.pagers.SearchLiteAsyncPager)

A pager for iterating through `search_lite` requests.

This class thinly wraps an initial [SearchResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchResponse) object, and provides an `__aiter__` method to iterate through its `results` field.

If there are more pages, the `__aiter__` method will make additional `SearchLite` requests and continue to iterate through the `results` field on the corresponding responses.

All the usual [SearchResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [SearchLitePager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.search_service.pagers.SearchLitePager)

A pager for iterating through `search_lite` requests.

This class thinly wraps an initial [SearchResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchResponse) object, and provides an `__iter__` method to iterate through its `results` field.

If there are more pages, the `__iter__` method will make additional `SearchLite` requests and continue to iterate through the `results` field on the corresponding responses.

All the usual [SearchResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [SearchPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.search_service.pagers.SearchPager)

A pager for iterating through `search` requests.

This class thinly wraps an initial [SearchResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchResponse) object, and provides an `__iter__` method to iterate through its `results` field.

If there are more pages, the `__iter__` method will make additional `Search` requests and continue to iterate through the `results` field on the corresponding responses.

All the usual [SearchResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [SearchTuningServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.search_tuning_service.SearchTuningServiceAsyncClient)

Service for search tuning.

### [SearchTuningServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.search_tuning_service.SearchTuningServiceClient)

Service for search tuning.

### [ServingConfigServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.serving_config_service.ServingConfigServiceAsyncClient)

Service for operations related to ServingConfig.

### [ServingConfigServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.serving_config_service.ServingConfigServiceClient)

Service for operations related to ServingConfig.

### [SessionServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.session_service.SessionServiceAsyncClient)

Service for managing Sessions and Session-related resources.

### [SessionServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.session_service.SessionServiceClient)

Service for managing Sessions and Session-related resources.

### [ListSessionsAsyncPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.session_service.pagers.ListSessionsAsyncPager)

A pager for iterating through `list_sessions` requests.

This class thinly wraps an initial [ListSessionsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListSessionsResponse) object, and provides an `__aiter__` method to iterate through its `sessions` field.

If there are more pages, the `__aiter__` method will make additional `ListSessions` requests and continue to iterate through the `sessions` field on the corresponding responses.

All the usual [ListSessionsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListSessionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListSessionsPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.session_service.pagers.ListSessionsPager)

A pager for iterating through `list_sessions` requests.

This class thinly wraps an initial [ListSessionsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListSessionsResponse) object, and provides an `__iter__` method to iterate through its `sessions` field.

If there are more pages, the `__iter__` method will make additional `ListSessions` requests and continue to iterate through the `sessions` field on the corresponding responses.

All the usual [ListSessionsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListSessionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [SiteSearchEngineServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.site_search_engine_service.SiteSearchEngineServiceAsyncClient)

Service for managing site search related resources.

### [SiteSearchEngineServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.site_search_engine_service.SiteSearchEngineServiceClient)

Service for managing site search related resources.

### [FetchDomainVerificationStatusAsyncPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.site_search_engine_service.pagers.FetchDomainVerificationStatusAsyncPager)

A pager for iterating through `fetch_domain_verification_status` requests.

This class thinly wraps an initial [FetchDomainVerificationStatusResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.FetchDomainVerificationStatusResponse) object, and provides an `__aiter__` method to iterate through its `target_sites` field.

If there are more pages, the `__aiter__` method will make additional `FetchDomainVerificationStatus` requests and continue to iterate through the `target_sites` field on the corresponding responses.

All the usual [FetchDomainVerificationStatusResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.FetchDomainVerificationStatusResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [FetchDomainVerificationStatusPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.site_search_engine_service.pagers.FetchDomainVerificationStatusPager)

A pager for iterating through `fetch_domain_verification_status` requests.

This class thinly wraps an initial [FetchDomainVerificationStatusResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.FetchDomainVerificationStatusResponse) object, and provides an `__iter__` method to iterate through its `target_sites` field.

If there are more pages, the `__iter__` method will make additional `FetchDomainVerificationStatus` requests and continue to iterate through the `target_sites` field on the corresponding responses.

All the usual [FetchDomainVerificationStatusResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.FetchDomainVerificationStatusResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListTargetSitesAsyncPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.site_search_engine_service.pagers.ListTargetSitesAsyncPager)

A pager for iterating through `list_target_sites` requests.

This class thinly wraps an initial [ListTargetSitesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListTargetSitesResponse) object, and provides an `__aiter__` method to iterate through its `target_sites` field.

If there are more pages, the `__aiter__` method will make additional `ListTargetSites` requests and continue to iterate through the `target_sites` field on the corresponding responses.

All the usual [ListTargetSitesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListTargetSitesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListTargetSitesPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.site_search_engine_service.pagers.ListTargetSitesPager)

A pager for iterating through `list_target_sites` requests.

This class thinly wraps an initial [ListTargetSitesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListTargetSitesResponse) object, and provides an `__iter__` method to iterate through its `target_sites` field.

If there are more pages, the `__iter__` method will make additional `ListTargetSites` requests and continue to iterate through the `target_sites` field on the corresponding responses.

All the usual [ListTargetSitesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListTargetSitesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [UserEventServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.user_event_service.UserEventServiceAsyncClient)

Service for ingesting end user actions on a website to Discovery Engine API.

### [UserEventServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.user_event_service.UserEventServiceClient)

Service for ingesting end user actions on a website to Discovery Engine API.

### [UserLicenseServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.user_license_service.UserLicenseServiceAsyncClient)

Service for managing User Licenses.

### [UserLicenseServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.user_license_service.UserLicenseServiceClient)

Service for managing User Licenses.

### [ListUserLicensesAsyncPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.user_license_service.pagers.ListUserLicensesAsyncPager)

A pager for iterating through `list_user_licenses` requests.

This class thinly wraps an initial [ListUserLicensesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListUserLicensesResponse) object, and provides an `__aiter__` method to iterate through its `user_licenses` field.

If there are more pages, the `__aiter__` method will make additional `ListUserLicenses` requests and continue to iterate through the `user_licenses` field on the corresponding responses.

All the usual [ListUserLicensesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListUserLicensesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListUserLicensesPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.user_license_service.pagers.ListUserLicensesPager)

A pager for iterating through `list_user_licenses` requests.

This class thinly wraps an initial [ListUserLicensesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListUserLicensesResponse) object, and provides an `__iter__` method to iterate through its `user_licenses` field.

If there are more pages, the `__iter__` method will make additional `ListUserLicenses` requests and continue to iterate through the `user_licenses` field on the corresponding responses.

All the usual [ListUserLicensesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListUserLicensesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [AdvancedSiteSearchConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AdvancedSiteSearchConfig)

Configuration data for advance site search.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AlloyDbSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AlloyDbSource)

AlloyDB source import data from.

### [Answer](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Answer)

Defines an answer.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AnswerSkippedReason](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Answer.AnswerSkippedReason)

An enum for answer skipped reasons.
    
    
        Google skips the answer if the query is chit
        chat.
    OUT_OF_DOMAIN_QUERY_IGNORED (3):
        The out-of-domain query ignored case.
    
        Google skips the answer if there are no
        high-relevance search results.
    POTENTIAL_POLICY_VIOLATION (4):
        The potential policy violation case.
    
        Google skips the answer if there is a potential
        policy violation detected. This includes content
        that may be violent or toxic.
    NO_RELEVANT_CONTENT (5):
        The no relevant content case.
    
        Google skips the answer if there is no relevant
        content in the retrieved search results.
    JAIL_BREAKING_QUERY_IGNORED (6):
        The jail-breaking query ignored case.
    
        For example, "Reply in the tone of a competing
        company's CEO". Google skips the answer if the
        query is classified as a jail-breaking query.
    CUSTOMER_POLICY_VIOLATION (7):
        The customer policy violation case.
    
        Google skips the summary if there is a customer
        policy violation detected. The policy is defined
        by the customer.
    NON_ANSWER_SEEKING_QUERY_IGNORED_V2 (8):
        The non-answer seeking query ignored case.
    
        Google skips the answer if the query doesn't
        have clear intent.
    LOW_GROUNDED_ANSWER (9):
        The low-grounded answer case.
    
        Google skips the answer if a well grounded
        answer was unable to be generated.
    USER_DEFINED_CLASSIFICATION_QUERY_IGNORED (10):
        The user defined query classification ignored
        case.
        Google skips the answer if the query is
        classified as a user defined query
        classification.
    UNHELPFUL_ANSWER (11):
        The unhelpful answer case.
    
        Google skips the answer if the answer is not
        helpful. This can be due to a variety of
        factors, including but not limited to: the query
        is not answerable, the answer is not relevant to
        the query, or the answer is not well-formatted.
    

### [Citation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Answer.Citation)

Citation info for a segment.

### [CitationSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Answer.CitationSource)

Citation source.

### [GroundingSupport](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Answer.GroundingSupport)

Grounding support for a claim in `answer_text`.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [QueryUnderstandingInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Answer.QueryUnderstandingInfo)

Query understanding information.

### [QueryClassificationInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Answer.QueryUnderstandingInfo.QueryClassificationInfo)

Query classification information.

### [Type](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Answer.QueryUnderstandingInfo.QueryClassificationInfo.Type)

Query classification types.

### [Reference](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Answer.Reference)

Reference.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ChunkInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Answer.Reference.ChunkInfo)

Chunk information.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [DocumentMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Answer.Reference.ChunkInfo.DocumentMetadata)

Document metadata.

### [StructuredDocumentInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Answer.Reference.StructuredDocumentInfo)

Structured search information.

### [UnstructuredDocumentInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Answer.Reference.UnstructuredDocumentInfo)

Unstructured document information.

### [ChunkContent](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Answer.Reference.UnstructuredDocumentInfo.ChunkContent)

Chunk content.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [State](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Answer.State)

Enumeration of the state of the answer generation.

### [Step](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Answer.Step)

Step information.

### [Action](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Answer.Step.Action)

Action.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Observation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Answer.Step.Action.Observation)

Observation.

### [SearchResult](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Answer.Step.Action.Observation.SearchResult)

### [ChunkInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Answer.Step.Action.Observation.SearchResult.ChunkInfo)

Chunk information.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [SnippetInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Answer.Step.Action.Observation.SearchResult.SnippetInfo)

Snippet information.

### [SearchAction](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Answer.Step.Action.SearchAction)

Search action.

### [State](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Answer.Step.State)

Enumeration of the state of the step.

### [AnswerQueryRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AnswerQueryRequest)

Request message for ConversationalSearchService.AnswerQuery method.

### [AnswerGenerationSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AnswerQueryRequest.AnswerGenerationSpec)

Answer generation specification.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ModelSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AnswerQueryRequest.AnswerGenerationSpec.ModelSpec)

Answer Generation Model specification.

### [PromptSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AnswerQueryRequest.AnswerGenerationSpec.PromptSpec)

Answer generation prompt specification.

### [EndUserSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AnswerQueryRequest.EndUserSpec)

End user specification.

### [EndUserMetaData](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AnswerQueryRequest.EndUserSpec.EndUserMetaData)

End user metadata.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ChunkInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AnswerQueryRequest.EndUserSpec.EndUserMetaData.ChunkInfo)

Chunk information.

### [DocumentMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AnswerQueryRequest.EndUserSpec.EndUserMetaData.ChunkInfo.DocumentMetadata)

Document metadata contains the information of the document of the current chunk.

### [GroundingSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AnswerQueryRequest.GroundingSpec)

Grounding specification.

### [FilteringLevel](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AnswerQueryRequest.GroundingSpec.FilteringLevel)

Level to filter based on answer grounding.

### [QueryUnderstandingSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AnswerQueryRequest.QueryUnderstandingSpec)

Query understanding specification.

### [QueryClassificationSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AnswerQueryRequest.QueryUnderstandingSpec.QueryClassificationSpec)

Query classification specification.

### [Type](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AnswerQueryRequest.QueryUnderstandingSpec.QueryClassificationSpec.Type)

Query classification types.

### [QueryRephraserSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AnswerQueryRequest.QueryUnderstandingSpec.QueryRephraserSpec)

Query rephraser specification.

### [ModelSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AnswerQueryRequest.QueryUnderstandingSpec.QueryRephraserSpec.ModelSpec)

Query Rephraser Model specification.

### [ModelType](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AnswerQueryRequest.QueryUnderstandingSpec.QueryRephraserSpec.ModelSpec.ModelType)

Query rephraser types. Currently only supports single-hop (max_rephrase_steps = 1) model selections. For multi-hop (max_rephrase_steps > 1), there is only one default model.

### [RelatedQuestionsSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AnswerQueryRequest.RelatedQuestionsSpec)

Related questions specification.

### [SafetySpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AnswerQueryRequest.SafetySpec)

Safety specification. There are two use cases:

  1. when only safety_spec.enable is set, the BLOCK_LOW_AND_ABOVE threshold will be applied for all categories.
  2. when safety_spec.enable is set and some safety_settings are set, only specified safety_settings are applied.



### [SafetySetting](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AnswerQueryRequest.SafetySpec.SafetySetting)

Safety settings.

### [HarmBlockThreshold](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AnswerQueryRequest.SafetySpec.SafetySetting.HarmBlockThreshold)

Probability based thresholds levels for blocking.

### [SearchSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AnswerQueryRequest.SearchSpec)

Search specification.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [SearchParams](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AnswerQueryRequest.SearchSpec.SearchParams)

Search parameters.

### [SearchResultList](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AnswerQueryRequest.SearchSpec.SearchResultList)

Search result list.

### [SearchResult](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AnswerQueryRequest.SearchSpec.SearchResultList.SearchResult)

Search result.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ChunkInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AnswerQueryRequest.SearchSpec.SearchResultList.SearchResult.ChunkInfo)

Chunk information.

### [DocumentMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AnswerQueryRequest.SearchSpec.SearchResultList.SearchResult.ChunkInfo.DocumentMetadata)

Document metadata contains the information of the document of the current chunk.

### [UnstructuredDocumentInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AnswerQueryRequest.SearchSpec.SearchResultList.SearchResult.UnstructuredDocumentInfo)

Unstructured document information.

### [DocumentContext](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AnswerQueryRequest.SearchSpec.SearchResultList.SearchResult.UnstructuredDocumentInfo.DocumentContext)

Document context.

### [ExtractiveAnswer](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AnswerQueryRequest.SearchSpec.SearchResultList.SearchResult.UnstructuredDocumentInfo.ExtractiveAnswer)

Extractive answer. `Guide <https://cloud.google.com/generative-ai-app-builder/docs/snippets#get-answers>`__

### [ExtractiveSegment](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AnswerQueryRequest.SearchSpec.SearchResultList.SearchResult.UnstructuredDocumentInfo.ExtractiveSegment)

Extractive segment. `Guide <https://cloud.google.com/generative-ai-app-builder/docs/snippets#extractive-segments>`__ Answer generation will only use it if document_contexts is empty. This is supposed to be shorter snippets.

### [UserLabelsEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AnswerQueryRequest.UserLabelsEntry)

The abstract base class for a message.

### [AnswerQueryResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AnswerQueryResponse)

Response message for ConversationalSearchService.AnswerQuery method.

### [AssistAnswer](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AssistAnswer)

AssistAnswer resource, main part of AssistResponse.

### [AssistSkippedReason](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AssistAnswer.AssistSkippedReason)

Possible reasons for not answering an assist call.

### [Reply](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AssistAnswer.Reply)

One part of the multi-part response of the assist call.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [State](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AssistAnswer.State)

State of the answer generation.

### [AssistUserMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AssistUserMetadata)

User metadata of the request.

### [Assistant](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Assistant)

Discovery Engine Assistant resource.

### [AssistantContent](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AssistantContent)

Multi-modal content.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Blob](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AssistantContent.Blob)

Inline blob.

### [CodeExecutionResult](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AssistantContent.CodeExecutionResult)

Result of executing ExecutableCode.

### [Outcome](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AssistantContent.CodeExecutionResult.Outcome)

Enumeration of possible outcomes of the code execution.

### [ExecutableCode](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AssistantContent.ExecutableCode)

Code generated by the model that is meant to be executed by the model.

### [File](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AssistantContent.File)

A file, e.g., an audio summary.

### [AssistantGroundedContent](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AssistantGroundedContent)

A piece of content and possibly its grounding information.

Not all content needs grounding. Phrases like "Of course, I will gladly search it for you." do not need grounding.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [TextGroundingMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AssistantGroundedContent.TextGroundingMetadata)

Grounding details for text sources.

### [Reference](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AssistantGroundedContent.TextGroundingMetadata.Reference)

Referenced content and related document metadata.

### [DocumentMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AssistantGroundedContent.TextGroundingMetadata.Reference.DocumentMetadata)

Document metadata.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Segment](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AssistantGroundedContent.TextGroundingMetadata.Segment)

Grounding information for a segment of the text.

### [BatchCreateTargetSiteMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.BatchCreateTargetSiteMetadata)

Metadata related to the progress of the SiteSearchEngineService.BatchCreateTargetSites operation. This will be returned by the google.longrunning.Operation.metadata field.

### [BatchCreateTargetSitesRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.BatchCreateTargetSitesRequest)

Request message for SiteSearchEngineService.BatchCreateTargetSites method.

### [BatchCreateTargetSitesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.BatchCreateTargetSitesResponse)

Response message for SiteSearchEngineService.BatchCreateTargetSites method.

### [BatchGetDocumentsMetadataRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.BatchGetDocumentsMetadataRequest)

Request message for DocumentService.BatchGetDocumentsMetadata method.

### [FhirMatcher](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.BatchGetDocumentsMetadataRequest.FhirMatcher)

Matcher for the Documents by FHIR resource names.

### [Matcher](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.BatchGetDocumentsMetadataRequest.Matcher)

Matcher for the Documents. Currently supports matching by exact URIs.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [UrisMatcher](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.BatchGetDocumentsMetadataRequest.UrisMatcher)

Matcher for the Documents by exact uris.

### [BatchGetDocumentsMetadataResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.BatchGetDocumentsMetadataResponse)

Response message for DocumentService.BatchGetDocumentsMetadata method.

### [DocumentMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.BatchGetDocumentsMetadataResponse.DocumentMetadata)

The metadata of a Document.

### [MatcherValue](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.BatchGetDocumentsMetadataResponse.DocumentMetadata.MatcherValue)

The value of the matcher that was used to match the Document.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [State](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.BatchGetDocumentsMetadataResponse.State)

The state of the Document.

### [BatchUpdateUserLicensesMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.BatchUpdateUserLicensesMetadata)

Metadata related to the progress of the UserLicenseService.BatchUpdateUserLicenses operation. This will be returned by the google.longrunning.Operation.metadata field.

### [BatchUpdateUserLicensesRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.BatchUpdateUserLicensesRequest)

Request message for UserLicenseService.BatchUpdateUserLicenses method.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [InlineSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.BatchUpdateUserLicensesRequest.InlineSource)

The inline source for the input config for BatchUpdateUserLicenses method.

### [BatchUpdateUserLicensesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.BatchUpdateUserLicensesResponse)

Response message for UserLicenseService.BatchUpdateUserLicenses method.

### [BatchVerifyTargetSitesMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.BatchVerifyTargetSitesMetadata)

Metadata related to the progress of the SiteSearchEngineService.BatchVerifyTargetSites operation. This will be returned by the google.longrunning.Operation.metadata field.

### [BatchVerifyTargetSitesRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.BatchVerifyTargetSitesRequest)

Request message for SiteSearchEngineService.BatchVerifyTargetSites method.

### [BatchVerifyTargetSitesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.BatchVerifyTargetSitesResponse)

Response message for SiteSearchEngineService.BatchVerifyTargetSites method.

### [BigQuerySource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.BigQuerySource)

BigQuery source import data from.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [BigtableOptions](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.BigtableOptions)

The Bigtable Options object that contains information to support the import.

### [BigtableColumn](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.BigtableOptions.BigtableColumn)

The column of the Bigtable.

### [BigtableColumnFamily](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.BigtableOptions.BigtableColumnFamily)

The column family of the Bigtable.

### [Encoding](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.BigtableOptions.Encoding)

The encoding mode of a Bigtable column or column family.

### [FamiliesEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.BigtableOptions.FamiliesEntry)

The abstract base class for a message.

### [Type](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.BigtableOptions.Type)

The type of values in a Bigtable column or column family. The values are expected to be encoded using `HBase Bytes.toBytes <https://hbase.apache.org/1.4/apidocs/org/apache/hadoop/hbase/util/Bytes.html>`__ function when the encoding value is set to `BINARY`.

### [BigtableSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.BigtableSource)

The Cloud Bigtable source for importing data.

### [CheckGroundingRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.CheckGroundingRequest)

Request message for GroundedGenerationService.CheckGrounding method.

### [UserLabelsEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.CheckGroundingRequest.UserLabelsEntry)

The abstract base class for a message.

### [CheckGroundingResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.CheckGroundingResponse)

Response message for the GroundedGenerationService.CheckGrounding method.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [CheckGroundingFactChunk](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.CheckGroundingResponse.CheckGroundingFactChunk)

Fact chunk for grounding check.

### [Claim](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.CheckGroundingResponse.Claim)

Text and citation info for a claim in the answer candidate.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [CheckGroundingSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.CheckGroundingSpec)

Specification for the grounding check.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Chunk](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Chunk)

Chunk captures all raw metadata information of items to be recommended or searched in the chunk mode.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AnnotationMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Chunk.AnnotationMetadata)

The annotation metadata includes structured content in the current chunk.

### [ChunkMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Chunk.ChunkMetadata)

Metadata of the current chunk. This field is only populated on SearchService.Search API.

### [DocumentMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Chunk.DocumentMetadata)

Document metadata contains the information of the document of the current chunk.

### [PageSpan](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Chunk.PageSpan)

Page span of the chunk.

### [StructureType](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Chunk.StructureType)

Defines the types of the structured content that can be extracted.

### [StructuredContent](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Chunk.StructuredContent)

The structured content information.

### [CloudSqlSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.CloudSqlSource)

Cloud SQL source import data from.

### [CmekConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.CmekConfig)

Configurations used to enable CMEK data encryption with Cloud KMS keys.

### [NotebookLMState](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.CmekConfig.NotebookLMState)

States of NotebookLM.

### [State](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.CmekConfig.State)

States of the CmekConfig.

### [CollectUserEventRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.CollectUserEventRequest)

Request message for CollectUserEvent method.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [CompleteQueryRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.CompleteQueryRequest)

Request message for CompletionService.CompleteQuery method.

### [CompleteQueryResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.CompleteQueryResponse)

Response message for CompletionService.CompleteQuery method.

### [QuerySuggestion](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.CompleteQueryResponse.QuerySuggestion)

Suggestions as search queries.

### [CompletionInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.CompletionInfo)

Detailed completion information including completion attribution token and clicked completion info.

### [CompletionSuggestion](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.CompletionSuggestion)

Autocomplete suggestions that are imported from Customer.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Condition](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Condition)

Defines circumstances to be checked before allowing a behavior

### [QueryTerm](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Condition.QueryTerm)

Matcher for search request query

### [TimeRange](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Condition.TimeRange)

Used for time-dependent conditions.

### [Control](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Control)

Defines a conditioned behavior to employ during serving. Must be attached to a ServingConfig to be considered at serving time. Permitted actions dependent on `SolutionType`.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [BoostAction](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Control.BoostAction)

Adjusts order of products in returned list.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [InterpolationBoostSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Control.BoostAction.InterpolationBoostSpec)

Specification for custom ranking based on customer specified attribute value. It provides more controls for customized ranking than the simple (condition, boost) combination above.

### [AttributeType](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Control.BoostAction.InterpolationBoostSpec.AttributeType)

The attribute(or function) for which the custom ranking is to be applied.

### [ControlPoint](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Control.BoostAction.InterpolationBoostSpec.ControlPoint)

The control points used to define the curve. The curve defined through these control points can only be monotonically increasing or decreasing(constant values are acceptable).

### [InterpolationType](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Control.BoostAction.InterpolationBoostSpec.InterpolationType)

The interpolation type to be applied. Default will be linear (Piecewise Linear).

### [FilterAction](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Control.FilterAction)

Specified which products may be included in results. Uses same filter as boost.

### [PromoteAction](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Control.PromoteAction)

Promote certain links based on some trigger queries.

Example: Promote shoe store link when searching for `shoe` keyword. The link can be outside of associated data store.

### [RedirectAction](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Control.RedirectAction)

Redirects a shopper to the provided URI.

### [SynonymsAction](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Control.SynonymsAction)

Creates a set of terms that will act as synonyms of one another. Example: "happy" will also be considered as "glad", "glad" will also be considered as "happy".

### [Conversation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Conversation)

External conversation proto definition.

### [State](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Conversation.State)

Enumeration of the state of the conversation.

### [ConversationContext](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ConversationContext)

Defines context of the conversation

### [ConversationMessage](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ConversationMessage)

Defines a conversation message.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ConverseConversationRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ConverseConversationRequest)

Request message for ConversationalSearchService.ConverseConversation method.

### [UserLabelsEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ConverseConversationRequest.UserLabelsEntry)

The abstract base class for a message.

### [ConverseConversationResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ConverseConversationResponse)

Response message for ConversationalSearchService.ConverseConversation method.

### [CreateControlRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.CreateControlRequest)

Request for CreateControl method.

### [CreateConversationRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.CreateConversationRequest)

Request for CreateConversation method.

### [CreateDataStoreMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.CreateDataStoreMetadata)

Metadata related to the progress of the DataStoreService.CreateDataStore operation. This will be returned by the google.longrunning.Operation.metadata field.

### [CreateDataStoreRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.CreateDataStoreRequest)

Request for DataStoreService.CreateDataStore method.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [CreateDocumentRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.CreateDocumentRequest)

Request message for DocumentService.CreateDocument method.

### [CreateEngineMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.CreateEngineMetadata)

Metadata related to the progress of the EngineService.CreateEngine operation. This will be returned by the google.longrunning.Operation.metadata field.

### [CreateEngineRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.CreateEngineRequest)

Request for EngineService.CreateEngine method.

### [CreateIdentityMappingStoreRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.CreateIdentityMappingStoreRequest)

Request message for IdentityMappingStoreService.CreateIdentityMappingStore

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [CreateSchemaMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.CreateSchemaMetadata)

Metadata for Create Schema LRO.

### [CreateSchemaRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.CreateSchemaRequest)

Request message for SchemaService.CreateSchema method.

### [CreateSessionRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.CreateSessionRequest)

Request for CreateSession method.

### [CreateSitemapMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.CreateSitemapMetadata)

Metadata related to the progress of the SiteSearchEngineService.CreateSitemap operation. This will be returned by the google.longrunning.Operation.metadata field.

### [CreateSitemapRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.CreateSitemapRequest)

Request message for SiteSearchEngineService.CreateSitemap method.

### [CreateTargetSiteMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.CreateTargetSiteMetadata)

Metadata related to the progress of the SiteSearchEngineService.CreateTargetSite operation. This will be returned by the google.longrunning.Operation.metadata field.

### [CreateTargetSiteRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.CreateTargetSiteRequest)

Request message for SiteSearchEngineService.CreateTargetSite method.

### [CustomAttribute](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.CustomAttribute)

A custom attribute that is not explicitly modeled in a resource, e.g. UserEvent.

### [CustomTuningModel](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.CustomTuningModel)

Metadata that describes a custom tuned model.

### [MetricsEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.CustomTuningModel.MetricsEntry)

The abstract base class for a message.

### [ModelState](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.CustomTuningModel.ModelState)

The state of the model.

### [DataStore](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.DataStore)

DataStore captures global settings and configs at the DataStore level.

### [BillingEstimation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.DataStore.BillingEstimation)

Estimation of data size per data store.

### [ContentConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.DataStore.ContentConfig)

Content config of the data store.

### [DeleteCmekConfigMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.DeleteCmekConfigMetadata)

Metadata related to the progress of the CmekConfigService.DeleteCmekConfig operation. This will be returned by the google.longrunning.Operation.metadata field.

### [DeleteCmekConfigRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.DeleteCmekConfigRequest)

Request message for CmekConfigService.DeleteCmekConfig method.

### [DeleteControlRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.DeleteControlRequest)

Request for DeleteControl method.

### [DeleteConversationRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.DeleteConversationRequest)

Request for DeleteConversation method.

### [DeleteDataStoreMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.DeleteDataStoreMetadata)

Metadata related to the progress of the DataStoreService.DeleteDataStore operation. This will be returned by the google.longrunning.Operation.metadata field.

### [DeleteDataStoreRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.DeleteDataStoreRequest)

Request message for DataStoreService.DeleteDataStore method.

### [DeleteDocumentRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.DeleteDocumentRequest)

Request message for DocumentService.DeleteDocument method.

### [DeleteEngineMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.DeleteEngineMetadata)

Metadata related to the progress of the EngineService.DeleteEngine operation. This will be returned by the google.longrunning.Operation.metadata field.

### [DeleteEngineRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.DeleteEngineRequest)

Request message for EngineService.DeleteEngine method.

### [DeleteIdentityMappingStoreMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.DeleteIdentityMappingStoreMetadata)

Metadata related to the progress of the IdentityMappingStoreService.DeleteIdentityMappingStore operation. This will be returned by the google.longrunning.Operation.metadata field.

### [DeleteIdentityMappingStoreRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.DeleteIdentityMappingStoreRequest)

Request message for IdentityMappingStoreService.DeleteIdentityMappingStore

### [DeleteSchemaMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.DeleteSchemaMetadata)

Metadata for DeleteSchema LRO.

### [DeleteSchemaRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.DeleteSchemaRequest)

Request message for SchemaService.DeleteSchema method.

### [DeleteSessionRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.DeleteSessionRequest)

Request for DeleteSession method.

### [DeleteSitemapMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.DeleteSitemapMetadata)

Metadata related to the progress of the SiteSearchEngineService.DeleteSitemap operation. This will be returned by the google.longrunning.Operation.metadata field.

### [DeleteSitemapRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.DeleteSitemapRequest)

Request message for SiteSearchEngineService.DeleteSitemap method.

### [DeleteTargetSiteMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.DeleteTargetSiteMetadata)

Metadata related to the progress of the SiteSearchEngineService.DeleteTargetSite operation. This will be returned by the google.longrunning.Operation.metadata field.

### [DeleteTargetSiteRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.DeleteTargetSiteRequest)

Request message for SiteSearchEngineService.DeleteTargetSite method.

### [DisableAdvancedSiteSearchMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.DisableAdvancedSiteSearchMetadata)

Metadata related to the progress of the SiteSearchEngineService.DisableAdvancedSiteSearch operation. This will be returned by the google.longrunning.Operation.metadata field.

### [DisableAdvancedSiteSearchRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.DisableAdvancedSiteSearchRequest)

Request message for SiteSearchEngineService.DisableAdvancedSiteSearch method.

### [DisableAdvancedSiteSearchResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.DisableAdvancedSiteSearchResponse)

Response message for SiteSearchEngineService.DisableAdvancedSiteSearch method.

### [Document](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Document)

Document captures all raw metadata information of items to be recommended or searched.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AclInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Document.AclInfo)

ACL Information of the Document.

### [AccessRestriction](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Document.AclInfo.AccessRestriction)

AclRestriction to model complex inheritance restrictions.

Example: Modeling a "Both Permit" inheritance, where to access a child document, user needs to have access to parent document.

Document Hierarchy - Space_S --> Page_P.

Readers: Space_S: group_1, user_1 Page_P: group_2, group_3, user_2

Space_S ACL Restriction - { "acl_info": { "readers": [ { "principals": [ { "group_id": "group_1" }, { "user_id": "user_1" } ] } ] } }

Page_P ACL Restriction. { "acl_info": { "readers": [ { "principals": [ { "group_id": "group_2" }, { "group_id": "group_3" }, { "user_id": "user_2" } ], }, { "principals": [ { "group_id": "group_1" }, { "user_id": "user_1" } ], } ] } }

### [Content](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Document.Content)

Unstructured data linked to this document.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [IndexStatus](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Document.IndexStatus)

Index status of the document.

### [DocumentInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.DocumentInfo)

Detailed document information associated with a user event.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [DocumentProcessingConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.DocumentProcessingConfig)

A singleton resource of DataStore. If it's empty when DataStore is created and DataStore is set to DataStore.ContentConfig.CONTENT_REQUIRED, the default parser will default to digital parser.

### [ChunkingConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.DocumentProcessingConfig.ChunkingConfig)

Configuration for chunking config.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [LayoutBasedChunkingConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.DocumentProcessingConfig.ChunkingConfig.LayoutBasedChunkingConfig)

Configuration for the layout based chunking.

### [ParsingConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.DocumentProcessingConfig.ParsingConfig)

Related configurations applied to a specific type of document parser.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [DigitalParsingConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.DocumentProcessingConfig.ParsingConfig.DigitalParsingConfig)

The digital parsing configurations for documents.

### [LayoutParsingConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.DocumentProcessingConfig.ParsingConfig.LayoutParsingConfig)

The layout parsing configurations for documents.

### [OcrParsingConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.DocumentProcessingConfig.ParsingConfig.OcrParsingConfig)

The OCR parsing configurations for documents.

### [ParsingConfigOverridesEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.DocumentProcessingConfig.ParsingConfigOverridesEntry)

The abstract base class for a message.

### [DoubleList](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.DoubleList)

Double list.

### [EnableAdvancedSiteSearchMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.EnableAdvancedSiteSearchMetadata)

Metadata related to the progress of the SiteSearchEngineService.EnableAdvancedSiteSearch operation. This will be returned by the google.longrunning.Operation.metadata field.

### [EnableAdvancedSiteSearchRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.EnableAdvancedSiteSearchRequest)

Request message for SiteSearchEngineService.EnableAdvancedSiteSearch method.

### [EnableAdvancedSiteSearchResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.EnableAdvancedSiteSearchResponse)

Response message for SiteSearchEngineService.EnableAdvancedSiteSearch method.

### [Engine](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Engine)

Metadata that describes the training and serving parameters of an Engine.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ChatEngineConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Engine.ChatEngineConfig)

Configurations for a Chat Engine.

### [AgentCreationConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Engine.ChatEngineConfig.AgentCreationConfig)

Configurations for generating a Dialogflow agent.

Note that these configurations are one-time consumed by and passed to Dialogflow service. It means they cannot be retrieved using EngineService.GetEngine or EngineService.ListEngines API after engine creation.

### [ChatEngineMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Engine.ChatEngineMetadata)

Additional information of a Chat Engine. Fields in this message are output only.

### [CommonConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Engine.CommonConfig)

Common configurations for an Engine.

### [MediaRecommendationEngineConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Engine.MediaRecommendationEngineConfig)

Additional config specs for a Media Recommendation engine.

### [EngineFeaturesConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Engine.MediaRecommendationEngineConfig.EngineFeaturesConfig)

More feature configs of the selected engine type.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [MostPopularFeatureConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Engine.MediaRecommendationEngineConfig.MostPopularFeatureConfig)

Feature configurations that are required for creating a Most Popular engine.

### [OptimizationObjectiveConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Engine.MediaRecommendationEngineConfig.OptimizationObjectiveConfig)

Custom threshold for `cvr` optimization_objective.

### [RecommendedForYouFeatureConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Engine.MediaRecommendationEngineConfig.RecommendedForYouFeatureConfig)

Additional feature configurations for creating a `recommended-for-you` engine.

### [TrainingState](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Engine.MediaRecommendationEngineConfig.TrainingState)

The training state of the engine.

### [SearchEngineConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Engine.SearchEngineConfig)

Configurations for a Search Engine.

### [FactChunk](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.FactChunk)

Fact Chunk.

### [SourceMetadataEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.FactChunk.SourceMetadataEntry)

The abstract base class for a message.

### [FetchDomainVerificationStatusRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.FetchDomainVerificationStatusRequest)

Request message for SiteSearchEngineService.FetchDomainVerificationStatus method.

### [FetchDomainVerificationStatusResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.FetchDomainVerificationStatusResponse)

Response message for SiteSearchEngineService.FetchDomainVerificationStatus method.

### [FetchSitemapsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.FetchSitemapsRequest)

Request message for SiteSearchEngineService.FetchSitemaps method.

### [Matcher](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.FetchSitemapsRequest.Matcher)

Matcher for the Sitemaps. Currently only supports uris matcher.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [UrisMatcher](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.FetchSitemapsRequest.UrisMatcher)

Matcher for the Sitemaps by their uris.

### [FetchSitemapsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.FetchSitemapsResponse)

Response message for SiteSearchEngineService.FetchSitemaps method.

### [SitemapMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.FetchSitemapsResponse.SitemapMetadata)

Contains a Sitemap and its metadata.

### [FhirStoreSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.FhirStoreSource)

Cloud FhirStore source import data from.

### [FirestoreSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.FirestoreSource)

Firestore source import data from.

### [GcsSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.GcsSource)

Cloud Storage location for input content.

### [GenerateGroundedContentRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.GenerateGroundedContentRequest)

Top-level message sent by the client for the `GenerateGroundedContent` method.

### [DynamicRetrievalConfiguration](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.GenerateGroundedContentRequest.DynamicRetrievalConfiguration)

Describes the options to customize dynamic retrieval.

### [DynamicRetrievalPredictor](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.GenerateGroundedContentRequest.DynamicRetrievalConfiguration.DynamicRetrievalPredictor)

Describes the predictor settings for dynamic retrieval.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Version](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.GenerateGroundedContentRequest.DynamicRetrievalConfiguration.DynamicRetrievalPredictor.Version)

The version of the predictor to be used in dynamic retrieval.

### [GenerationSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.GenerateGroundedContentRequest.GenerationSpec)

Content generation specification.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [GroundingSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.GenerateGroundedContentRequest.GroundingSource)

Grounding source.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [EnterpriseWebRetrievalSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.GenerateGroundedContentRequest.GroundingSource.EnterpriseWebRetrievalSource)

Params for using enterprise web retrieval as grounding source.

### [GoogleSearchSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.GenerateGroundedContentRequest.GroundingSource.GoogleSearchSource)

Google Search config parameters.

### [InlineSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.GenerateGroundedContentRequest.GroundingSource.InlineSource)

Message to be used for grounding based on inline content.

### [AttributesEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.GenerateGroundedContentRequest.GroundingSource.InlineSource.AttributesEntry)

The abstract base class for a message.

### [SearchSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.GenerateGroundedContentRequest.GroundingSource.SearchSource)

Message to be used for grounding with Vertex AI Search.

### [GroundingSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.GenerateGroundedContentRequest.GroundingSpec)

Grounding specification.

### [UserLabelsEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.GenerateGroundedContentRequest.UserLabelsEntry)

The abstract base class for a message.

### [GenerateGroundedContentResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.GenerateGroundedContentResponse)

Response for the `GenerateGroundedContent` method.

### [Candidate](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.GenerateGroundedContentResponse.Candidate)

A response candidate generated from the model.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [GroundingMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.GenerateGroundedContentResponse.Candidate.GroundingMetadata)

Citation for the generated content.

### [DynamicRetrievalMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.GenerateGroundedContentResponse.Candidate.GroundingMetadata.DynamicRetrievalMetadata)

Describes the metadata about dynamic retrieval.

### [DynamicRetrievalPredictorMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.GenerateGroundedContentResponse.Candidate.GroundingMetadata.DynamicRetrievalPredictorMetadata)

Describes the metadata about the dynamic retrieval predictor.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Version](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.GenerateGroundedContentResponse.Candidate.GroundingMetadata.DynamicRetrievalPredictorMetadata.Version)

The version of the predictor which was used in dynamic retrieval.

### [GroundingSupport](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.GenerateGroundedContentResponse.Candidate.GroundingMetadata.GroundingSupport)

Grounding info for a claim in the candidate and its support.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ImageMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.GenerateGroundedContentResponse.Candidate.GroundingMetadata.ImageMetadata)

Metadata about an image from the web search.

### [Image](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.GenerateGroundedContentResponse.Candidate.GroundingMetadata.ImageMetadata.Image)

Metadata about the image.

### [WebsiteInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.GenerateGroundedContentResponse.Candidate.GroundingMetadata.ImageMetadata.WebsiteInfo)

Metadata about the website that the image is from.

### [RetrievalMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.GenerateGroundedContentResponse.Candidate.GroundingMetadata.RetrievalMetadata)

Describes the metadata associated with a retrieval step.

### [Source](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.GenerateGroundedContentResponse.Candidate.GroundingMetadata.RetrievalMetadata.Source)

Describes the source to which the metadata is associated to.

### [SearchEntryPoint](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.GenerateGroundedContentResponse.Candidate.GroundingMetadata.SearchEntryPoint)

Google search entry point.

### [GetAnswerRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.GetAnswerRequest)

Request for GetAnswer method.

### [GetCmekConfigRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.GetCmekConfigRequest)

Request message for GetCmekConfigRequest method.

### [GetControlRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.GetControlRequest)

Request for GetControl method.

### [GetConversationRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.GetConversationRequest)

Request for GetConversation method.

### [GetDataStoreRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.GetDataStoreRequest)

Request message for DataStoreService.GetDataStore method.

### [GetDocumentRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.GetDocumentRequest)

Request message for DocumentService.GetDocument method.

### [GetEngineRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.GetEngineRequest)

Request message for EngineService.GetEngine method.

### [GetIdentityMappingStoreRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.GetIdentityMappingStoreRequest)

Request message for IdentityMappingStoreService.GetIdentityMappingStore

### [GetSchemaRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.GetSchemaRequest)

Request message for SchemaService.GetSchema method.

### [GetSessionRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.GetSessionRequest)

Request for GetSession method.

### [GetSiteSearchEngineRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.GetSiteSearchEngineRequest)

Request message for SiteSearchEngineService.GetSiteSearchEngine method.

### [GetTargetSiteRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.GetTargetSiteRequest)

Request message for SiteSearchEngineService.GetTargetSite method.

### [GroundedGenerationContent](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.GroundedGenerationContent)

Base structured datatype containing multi-part content of a message.

### [Part](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.GroundedGenerationContent.Part)

Single part of content.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [GroundingFact](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.GroundingFact)

Grounding Fact.

### [AttributesEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.GroundingFact.AttributesEntry)

The abstract base class for a message.

### [HarmCategory](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.HarmCategory)

Harm categories that will block the content.

### [HealthcareFhirConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.HealthcareFhirConfig)

Config to data store for `HEALTHCARE_FHIR` vertical.

### [IdentityMappingEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.IdentityMappingEntry)

Identity Mapping Entry that maps an external identity to an internal identity.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [IdentityMappingEntryOperationMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.IdentityMappingEntryOperationMetadata)

IdentityMappingEntry LongRunningOperation metadata for IdentityMappingStoreService.ImportIdentityMappings and IdentityMappingStoreService.PurgeIdentityMappings

### [IdentityMappingStore](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.IdentityMappingStore)

Identity Mapping Store which contains Identity Mapping Entries.

### [ImportCompletionSuggestionsMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ImportCompletionSuggestionsMetadata)

Metadata related to the progress of the ImportCompletionSuggestions operation. This will be returned by the google.longrunning.Operation.metadata field.

### [ImportCompletionSuggestionsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ImportCompletionSuggestionsRequest)

Request message for CompletionService.ImportCompletionSuggestions method.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [InlineSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ImportCompletionSuggestionsRequest.InlineSource)

The inline source for CompletionSuggestions.

### [ImportCompletionSuggestionsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ImportCompletionSuggestionsResponse)

Response of the CompletionService.ImportCompletionSuggestions method. If the long running operation is done, this message is returned by the google.longrunning.Operations.response field if the operation is successful.

### [ImportDocumentsMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ImportDocumentsMetadata)

Metadata related to the progress of the ImportDocuments operation. This is returned by the google.longrunning.Operation.metadata field.

### [ImportDocumentsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ImportDocumentsRequest)

Request message for Import methods.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [InlineSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ImportDocumentsRequest.InlineSource)

The inline source for the input config for ImportDocuments method.

### [ReconciliationMode](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ImportDocumentsRequest.ReconciliationMode)

Indicates how imported documents are reconciled with the existing documents created or imported before.

### [ImportDocumentsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ImportDocumentsResponse)

Response of the ImportDocumentsRequest. If the long running operation is done, then this message is returned by the google.longrunning.Operations.response field if the operation was successful.

### [ImportErrorConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ImportErrorConfig)

Configuration of destination for Import related errors.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ImportIdentityMappingsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ImportIdentityMappingsRequest)

Request message for IdentityMappingStoreService.ImportIdentityMappings

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [InlineSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ImportIdentityMappingsRequest.InlineSource)

The inline source to import identity mapping entries from.

### [ImportIdentityMappingsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ImportIdentityMappingsResponse)

Response message for IdentityMappingStoreService.ImportIdentityMappings

### [ImportSuggestionDenyListEntriesMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ImportSuggestionDenyListEntriesMetadata)

Metadata related to the progress of the ImportSuggestionDenyListEntries operation. This is returned by the google.longrunning.Operation.metadata field.

### [ImportSuggestionDenyListEntriesRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ImportSuggestionDenyListEntriesRequest)

Request message for CompletionService.ImportSuggestionDenyListEntries method.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [InlineSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ImportSuggestionDenyListEntriesRequest.InlineSource)

The inline source for SuggestionDenyListEntry.

### [ImportSuggestionDenyListEntriesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ImportSuggestionDenyListEntriesResponse)

Response message for CompletionService.ImportSuggestionDenyListEntries method.

### [ImportUserEventsMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ImportUserEventsMetadata)

Metadata related to the progress of the Import operation. This is returned by the google.longrunning.Operation.metadata field.

### [ImportUserEventsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ImportUserEventsRequest)

Request message for the ImportUserEvents request.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [InlineSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ImportUserEventsRequest.InlineSource)

The inline source for the input config for ImportUserEvents method.

### [ImportUserEventsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ImportUserEventsResponse)

Response of the ImportUserEventsRequest. If the long running operation was successful, then this message is returned by the google.longrunning.Operations.response field if the operation was successful.

### [IndustryVertical](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.IndustryVertical)

The industry vertical associated with the DataStore.

### [Interval](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Interval)

A floating point interval.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ListCmekConfigsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListCmekConfigsRequest)

Request message for CmekConfigService.ListCmekConfigs method.

### [ListCmekConfigsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListCmekConfigsResponse)

Response message for CmekConfigService.ListCmekConfigs method.

### [ListControlsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListControlsRequest)

Request for ListControls method.

### [ListControlsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListControlsResponse)

Response for ListControls method.

### [ListConversationsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListConversationsRequest)

Request for ListConversations method.

### [ListConversationsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListConversationsResponse)

Response for ListConversations method.

### [ListCustomModelsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListCustomModelsRequest)

Request message for SearchTuningService.ListCustomModels method.

### [ListCustomModelsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListCustomModelsResponse)

Response message for SearchTuningService.ListCustomModels method.

### [ListDataStoresRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListDataStoresRequest)

Request message for DataStoreService.ListDataStores method.

### [ListDataStoresResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListDataStoresResponse)

Response message for DataStoreService.ListDataStores method.

### [ListDocumentsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListDocumentsRequest)

Request message for DocumentService.ListDocuments method.

### [ListDocumentsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListDocumentsResponse)

Response message for DocumentService.ListDocuments method.

### [ListEnginesRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListEnginesRequest)

Request message for EngineService.ListEngines method.

### [ListEnginesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListEnginesResponse)

Response message for EngineService.ListEngines method.

### [ListIdentityMappingStoresRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListIdentityMappingStoresRequest)

Request message for IdentityMappingStoreService.ListIdentityMappingStores

### [ListIdentityMappingStoresResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListIdentityMappingStoresResponse)

Response message for IdentityMappingStoreService.ListIdentityMappingStores

### [ListIdentityMappingsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListIdentityMappingsRequest)

Request message for IdentityMappingStoreService.ListIdentityMappings

### [ListIdentityMappingsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListIdentityMappingsResponse)

Response message for IdentityMappingStoreService.ListIdentityMappings

### [ListSchemasRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListSchemasRequest)

Request message for SchemaService.ListSchemas method.

### [ListSchemasResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListSchemasResponse)

Response message for SchemaService.ListSchemas method.

### [ListSessionsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListSessionsRequest)

Request for ListSessions method.

### [ListSessionsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListSessionsResponse)

Response for ListSessions method.

### [ListTargetSitesRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListTargetSitesRequest)

Request message for SiteSearchEngineService.ListTargetSites method.

### [ListTargetSitesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListTargetSitesResponse)

Response message for SiteSearchEngineService.ListTargetSites method.

### [ListUserLicensesRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListUserLicensesRequest)

Request message for UserLicenseService.ListUserLicenses.

### [ListUserLicensesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListUserLicensesResponse)

Response message for UserLicenseService.ListUserLicenses.

### [MediaInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.MediaInfo)

Media-specific user event information.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [NaturalLanguageQueryUnderstandingConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.NaturalLanguageQueryUnderstandingConfig)

Configuration for Natural Language Query Understanding.

### [Mode](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.NaturalLanguageQueryUnderstandingConfig.Mode)

Mode of Natural Language Query Understanding. When the NaturalLanguageQueryUnderstandingConfig.Mode is ENABLED, the natural language understanding capabilities will be enabled for a search request if the NaturalLanguageQueryUnderstandingSpec.FilterExtractionCondition in the SearchRequest is ENABLED.

### [PageInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.PageInfo)

Detailed page information.

### [PanelInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.PanelInfo)

Detailed panel information associated with a user event.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Principal](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Principal)

Principal identifier of a user or a group.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Project](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Project)

Metadata and configurations for a Google Cloud project in the service.

### [ServiceTerms](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Project.ServiceTerms)

Metadata about the terms of service.

### [State](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Project.ServiceTerms.State)

The agreement states this terms of service.

### [ServiceTermsMapEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Project.ServiceTermsMapEntry)

The abstract base class for a message.

### [ProvisionProjectMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ProvisionProjectMetadata)

Metadata associated with a project provision operation.

### [ProvisionProjectRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ProvisionProjectRequest)

Request for ProjectService.ProvisionProject method.

### [PurgeCompletionSuggestionsMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.PurgeCompletionSuggestionsMetadata)

Metadata related to the progress of the PurgeCompletionSuggestions operation. This is returned by the google.longrunning.Operation.metadata field.

### [PurgeCompletionSuggestionsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.PurgeCompletionSuggestionsRequest)

Request message for CompletionService.PurgeCompletionSuggestions method.

### [PurgeCompletionSuggestionsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.PurgeCompletionSuggestionsResponse)

Response message for CompletionService.PurgeCompletionSuggestions method.

### [PurgeDocumentsMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.PurgeDocumentsMetadata)

Metadata related to the progress of the PurgeDocuments operation. This will be returned by the google.longrunning.Operation.metadata field.

### [PurgeDocumentsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.PurgeDocumentsRequest)

Request message for DocumentService.PurgeDocuments method.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [InlineSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.PurgeDocumentsRequest.InlineSource)

The inline source for the input config for DocumentService.PurgeDocuments method.

### [PurgeDocumentsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.PurgeDocumentsResponse)

Response message for DocumentService.PurgeDocuments method. If the long running operation is successfully done, then this message is returned by the google.longrunning.Operations.response field.

### [PurgeErrorConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.PurgeErrorConfig)

Configuration of destination for Purge related errors.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [PurgeIdentityMappingsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.PurgeIdentityMappingsRequest)

Request message for IdentityMappingStoreService.PurgeIdentityMappings

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [InlineSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.PurgeIdentityMappingsRequest.InlineSource)

The inline source to purge identity mapping entries from.

### [PurgeSuggestionDenyListEntriesMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.PurgeSuggestionDenyListEntriesMetadata)

Metadata related to the progress of the PurgeSuggestionDenyListEntries operation. This is returned by the google.longrunning.Operation.metadata field.

### [PurgeSuggestionDenyListEntriesRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.PurgeSuggestionDenyListEntriesRequest)

Request message for CompletionService.PurgeSuggestionDenyListEntries method.

### [PurgeSuggestionDenyListEntriesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.PurgeSuggestionDenyListEntriesResponse)

Response message for CompletionService.PurgeSuggestionDenyListEntries method.

### [PurgeUserEventsMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.PurgeUserEventsMetadata)

Metadata related to the progress of the PurgeUserEvents operation. This will be returned by the google.longrunning.Operation.metadata field.

### [PurgeUserEventsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.PurgeUserEventsRequest)

Request message for PurgeUserEvents method.

### [PurgeUserEventsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.PurgeUserEventsResponse)

Response of the PurgeUserEventsRequest. If the long running operation is successfully done, then this message is returned by the google.longrunning.Operations.response field.

### [Query](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Query)

Defines a user inputed query.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [RankRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.RankRequest)

Request message for RankService.Rank method.

### [UserLabelsEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.RankRequest.UserLabelsEntry)

The abstract base class for a message.

### [RankResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.RankResponse)

Response message for RankService.Rank method.

### [RankingRecord](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.RankingRecord)

Record message for RankService.Rank method.

### [RecommendRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.RecommendRequest)

Request message for Recommend method.

### [ParamsEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.RecommendRequest.ParamsEntry)

The abstract base class for a message.

### [UserLabelsEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.RecommendRequest.UserLabelsEntry)

The abstract base class for a message.

### [RecommendResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.RecommendResponse)

Response message for Recommend method.

### [RecommendationResult](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.RecommendResponse.RecommendationResult)

RecommendationResult represents a generic recommendation result with associated metadata.

### [MetadataEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.RecommendResponse.RecommendationResult.MetadataEntry)

The abstract base class for a message.

### [RecrawlUrisMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.RecrawlUrisMetadata)

Metadata related to the progress of the SiteSearchEngineService.RecrawlUris operation. This will be returned by the google.longrunning.Operation.metadata field.

### [RecrawlUrisRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.RecrawlUrisRequest)

Request message for SiteSearchEngineService.RecrawlUris method.

### [RecrawlUrisResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.RecrawlUrisResponse)

Response message for SiteSearchEngineService.RecrawlUris method.

### [FailureInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.RecrawlUrisResponse.FailureInfo)

Details about why a particular URI failed to be crawled. Each FailureInfo contains one FailureReason per CorpusType.

### [FailureReason](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.RecrawlUrisResponse.FailureInfo.FailureReason)

Details about why crawling failed for a particular CorpusType, e.g., DESKTOP and MOBILE crawling may fail for different reasons.

### [CorpusType](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.RecrawlUrisResponse.FailureInfo.FailureReason.CorpusType)

CorpusType for the failed crawling operation.

### [Reply](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Reply)

Defines a reply message to user.

### [SafetyRating](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SafetyRating)

Safety rating corresponding to the generated content.

### [HarmProbability](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SafetyRating.HarmProbability)

Harm probability levels in the content.

### [HarmSeverity](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SafetyRating.HarmSeverity)

Harm severity levels.

### [Schema](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Schema)

Defines the structure and layout of a type of document data.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [SearchAddOn](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchAddOn)

Add-on that provides additional functionality for search.

### [SearchInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchInfo)

Detailed search information.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [SearchLinkPromotion](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchLinkPromotion)

Promotion proto includes uri and other helping information to display the promotion.

### [SearchRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest)

Request message for SearchService.Search method.

### [BoostSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest.BoostSpec)

Boost specification to boost certain documents.

### [ConditionBoostSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest.BoostSpec.ConditionBoostSpec)

Boost applies to documents which match a condition.

### [BoostControlSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest.BoostSpec.ConditionBoostSpec.BoostControlSpec)

Specification for custom ranking based on customer specified attribute value. It provides more controls for customized ranking than the simple (condition, boost) combination above.

### [AttributeType](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest.BoostSpec.ConditionBoostSpec.BoostControlSpec.AttributeType)

The attribute(or function) for which the custom ranking is to be applied.

### [ControlPoint](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest.BoostSpec.ConditionBoostSpec.BoostControlSpec.ControlPoint)

The control points used to define the curve. The curve defined through these control points can only be monotonically increasing or decreasing(constant values are acceptable).

### [InterpolationType](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest.BoostSpec.ConditionBoostSpec.BoostControlSpec.InterpolationType)

The interpolation type to be applied. Default will be linear (Piecewise Linear).

### [ContentSearchSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest.ContentSearchSpec)

A specification for configuring the behavior of content search.

### [ChunkSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest.ContentSearchSpec.ChunkSpec)

Specifies the chunk spec to be returned from the search response. Only available if the SearchRequest.ContentSearchSpec.search_result_mode is set to CHUNKS

### [ExtractiveContentSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest.ContentSearchSpec.ExtractiveContentSpec)

A specification for configuring the extractive content in a search response.

### [SearchResultMode](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest.ContentSearchSpec.SearchResultMode)

Specifies the search result mode. If unspecified, the search result mode defaults to `DOCUMENTS`.

### [SnippetSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest.ContentSearchSpec.SnippetSpec)

A specification for configuring snippets in a search response.

### [SummarySpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest.ContentSearchSpec.SummarySpec)

A specification for configuring a summary returned in a search response.

### [ModelPromptSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest.ContentSearchSpec.SummarySpec.ModelPromptSpec)

Specification of the prompt to use with the model.

### [ModelSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest.ContentSearchSpec.SummarySpec.ModelSpec)

Specification of the model.

### [CrowdingSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest.CrowdingSpec)

Specification for crowding. Crowding improves the diversity of search results by limiting the number of results that share the same field value. For example, crowding on the color field with a max_count of 3 and mode DROP_CROWDED_RESULTS will return at most 3 results with the same color across all pages.

### [Mode](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest.CrowdingSpec.Mode)

Enum describing the mode to use for documents that are crowded away. They can be dropped or demoted to the later pages.

### [CustomRankingParams](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest.CustomRankingParams)

Configuration parameters for the Custom Ranking feature.

### [DataStoreSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest.DataStoreSpec)

A struct to define data stores to filter on in a search call and configurations for those data stores. Otherwise, an `INVALID_ARGUMENT` error is returned.

### [DisplaySpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest.DisplaySpec)

Specifies features for display, like match highlighting.

### [MatchHighlightingCondition](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest.DisplaySpec.MatchHighlightingCondition)

Enum describing under which condition match highlighting should occur.

### [FacetSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest.FacetSpec)

A facet specification to perform faceted search.

### [FacetKey](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest.FacetSpec.FacetKey)

Specifies how a facet is computed.

### [ImageQuery](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest.ImageQuery)

Specifies the image query input.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [NaturalLanguageQueryUnderstandingSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest.NaturalLanguageQueryUnderstandingSpec)

Specification to enable natural language understanding capabilities for search requests.

### [ExtractedFilterBehavior](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest.NaturalLanguageQueryUnderstandingSpec.ExtractedFilterBehavior)

Enum describing how extracted filters are applied to the search.

### [FilterExtractionCondition](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest.NaturalLanguageQueryUnderstandingSpec.FilterExtractionCondition)

Enum describing under which condition filter extraction should occur.

### [ParamsEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest.ParamsEntry)

The abstract base class for a message.

### [QueryExpansionSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest.QueryExpansionSpec)

Specification to determine under which conditions query expansion should occur.

### [Condition](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest.QueryExpansionSpec.Condition)

Enum describing under which condition query expansion should occur.

### [RankingExpressionBackend](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest.RankingExpressionBackend)

The backend to use for the ranking expression evaluation.

### [RelevanceFilterSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest.RelevanceFilterSpec)

Relevance filtering specification.

### [RelevanceThresholdSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest.RelevanceFilterSpec.RelevanceThresholdSpec)

Specification for relevance filtering on a specific sub-search.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [RelevanceScoreSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest.RelevanceScoreSpec)

The specification for returning the document relevance score.

### [RelevanceThreshold](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest.RelevanceThreshold)

The relevance threshold of the search results. The higher relevance threshold is, the higher relevant results are shown and the less number of results are returned.

### [SearchAddonSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest.SearchAddonSpec)

SearchAddonSpec is used to disable add-ons for search as per new repricing model. By default if the SearchAddonSpec is not specified, we consider that the customer wants to enable them wherever applicable.

### [SearchAsYouTypeSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest.SearchAsYouTypeSpec)

Specification for search as you type in search requests.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Condition](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest.SearchAsYouTypeSpec.Condition)

Enum describing under which condition search as you type should occur.

### [Field](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest.SearchAsYouTypeSpec.Field)

A schema field to be used for Search As You Type scoring on this request. Overrides any data-store-level Search As You Type field configuration for the duration of the request.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [SessionSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest.SessionSpec)

Session specification.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [SpellCorrectionSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest.SpellCorrectionSpec)

The specification for query spell correction.

### [Mode](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest.SpellCorrectionSpec.Mode)

Enum describing under which mode spell correction should occur.

### [UserLabelsEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest.UserLabelsEntry)

The abstract base class for a message.

### [SearchResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchResponse)

Response message for SearchService.Search method.

### [Facet](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchResponse.Facet)

A facet result.

### [FacetValue](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchResponse.Facet.FacetValue)

A facet value which contains value names and their count.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [NaturalLanguageQueryUnderstandingInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchResponse.NaturalLanguageQueryUnderstandingInfo)

Information describing what natural language understanding was done on the input query.

### [StructuredExtractedFilter](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchResponse.NaturalLanguageQueryUnderstandingInfo.StructuredExtractedFilter)

The filters that were extracted from the input query represented in a structured form.

### [AndExpression](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchResponse.NaturalLanguageQueryUnderstandingInfo.StructuredExtractedFilter.AndExpression)

Logical `And` operator.

### [Expression](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchResponse.NaturalLanguageQueryUnderstandingInfo.StructuredExtractedFilter.Expression)

The expression denoting the filter that was extracted from the input query.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [GeolocationConstraint](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchResponse.NaturalLanguageQueryUnderstandingInfo.StructuredExtractedFilter.GeolocationConstraint)

Constraint of a geolocation field. Name of the geolocation field as defined in the schema.

### [NumberConstraint](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchResponse.NaturalLanguageQueryUnderstandingInfo.StructuredExtractedFilter.NumberConstraint)

Constraint expression of a number field. Example: price < 100.

### [Comparison](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchResponse.NaturalLanguageQueryUnderstandingInfo.StructuredExtractedFilter.NumberConstraint.Comparison)

The comparison operation that was performed.

### [OrExpression](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchResponse.NaturalLanguageQueryUnderstandingInfo.StructuredExtractedFilter.OrExpression)

Logical `Or` operator.

### [StringConstraint](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchResponse.NaturalLanguageQueryUnderstandingInfo.StructuredExtractedFilter.StringConstraint)

Constraint expression of a string field.

### [QueryExpansionInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchResponse.QueryExpansionInfo)

Information describing query expansion including whether expansion has occurred.

### [SearchResult](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchResponse.SearchResult)

Represents the search results.

### [ModelScoresEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchResponse.SearchResult.ModelScoresEntry)

The abstract base class for a message.

### [RankSignals](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchResponse.SearchResult.RankSignals)

A set of ranking signals.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [CustomSignal](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchResponse.SearchResult.RankSignals.CustomSignal)

Custom clearbox signal represented by name and value pair.

### [RetrievalSignals](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchResponse.SearchResult.RetrievalSignals)

Contains a set of signals used by the relevance filter.

### [RetrievalSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchResponse.SearchResult.RetrievalSignals.RetrievalSource)

Indicates the source of the retrieval.

### [SemanticState](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchResponse.SemanticState)

Semantic state of the search response.

### [SessionInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchResponse.SessionInfo)

Information about the session.

### [Summary](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchResponse.Summary)

Summary of the top N search results specified by the summary spec.

### [Citation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchResponse.Summary.Citation)

Citation info for a segment.

### [CitationMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchResponse.Summary.CitationMetadata)

Citation metadata.

### [CitationSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchResponse.Summary.CitationSource)

Citation source.

### [Reference](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchResponse.Summary.Reference)

Document reference.

### [ChunkContent](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchResponse.Summary.Reference.ChunkContent)

Chunk content.

### [SafetyAttributes](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchResponse.Summary.SafetyAttributes)

Safety Attribute categories and their associated confidence scores.

### [SummarySkippedReason](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchResponse.Summary.SummarySkippedReason)

An Enum for summary-skipped reasons.
    
    
        Only used when
        <xref uid="google.cloud.discoveryengine.v1.SearchRequest.ContentSearchSpec.SummarySpec.ignore_adversarial_query">SummarySpec.ignore_adversarial_query</xref>
        is set to `true`.
    NON_SUMMARY_SEEKING_QUERY_IGNORED (2):
        The non-summary seeking query ignored case.
    
        Google skips the summary if the query is chit chat. Only
        used when
        <xref uid="google.cloud.discoveryengine.v1.SearchRequest.ContentSearchSpec.SummarySpec.ignore_non_summary_seeking_query">SummarySpec.ignore_non_summary_seeking_query</xref>
        is set to `true`.
    OUT_OF_DOMAIN_QUERY_IGNORED (3):
        The out-of-domain query ignored case.
    
        Google skips the summary if there are no
        high-relevance search results. For example, the
        data store contains facts about company A but
        the user query is asking questions about company
        B.
    POTENTIAL_POLICY_VIOLATION (4):
        The potential policy violation case.
    
        Google skips the summary if there is a potential
        policy violation detected. This includes content
        that may be violent or toxic.
    LLM_ADDON_NOT_ENABLED (5):
        The LLM addon not enabled case.
    
        Google skips the summary if the LLM addon is not
        enabled.
    NO_RELEVANT_CONTENT (6):
        The no relevant content case.
    
        Google skips the summary if there is no relevant
        content in the retrieved search results.
    JAIL_BREAKING_QUERY_IGNORED (7):
        The jail-breaking query ignored case.
    
        For example, "Reply in the tone of a competing company's
        CEO". Only used when
        [SearchRequest.ContentSearchSpec.SummarySpec.ignore_jail_breaking_query]
        is set to `true`.
    CUSTOMER_POLICY_VIOLATION (8):
        The customer policy violation case.
    
        Google skips the summary if there is a customer
        policy violation detected. The policy is defined
        by the customer.
    NON_SUMMARY_SEEKING_QUERY_IGNORED_V2 (9):
        The non-answer seeking query ignored case.
    
        Google skips the summary if the query doesn't have clear
        intent. Only used when
        [SearchRequest.ContentSearchSpec.SummarySpec.ignore_non_answer_seeking_query]
        is set to `true`.
    TIME_OUT (10):
        The time out case.
    
        Google skips the summary if the time out.
    

### [SummaryWithMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchResponse.Summary.SummaryWithMetadata)

Summary with metadata information.

### [SearchTier](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchTier)

Tiers of search features. Different tiers might have different pricing. To learn more, check the pricing documentation.

### [SearchUseCase](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchUseCase)

Defines a further subdivision of `SolutionType`. Specifically applies to SOLUTION_TYPE_SEARCH.

### [ServingConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ServingConfig)

Configures metadata that is used to generate serving time results (e.g. search results or recommendation predictions). The ServingConfig is passed in the search and predict request and generates results.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [GenericConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ServingConfig.GenericConfig)

Specifies the configurations needed for Generic Discovery.Currently we support:

  * `content_search_spec`: configuration for generic content search.



### [MediaConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ServingConfig.MediaConfig)

Specifies the configurations needed for Media Discovery. Currently we support:

  * `demote_content_watched`: Threshold for watched content demotion. Customers can specify if using watched content demotion or use viewed detail page. Using the content watched demotion, customers need to specify the watched minutes or percentage exceeds the threshold, the content will be demoted in the recommendation result.
  * `promote_fresh_content`: cutoff days for fresh content promotion. Customers can specify if using content freshness promotion. If the content was published within the cutoff days, the content will be promoted in the recommendation result. Can only be set if SolutionType is SOLUTION_TYPE_RECOMMENDATION.



This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Session](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Session)

External session proto definition.

### [State](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Session.State)

Enumeration of the state of the session.

### [Turn](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Session.Turn)

Represents a turn, including a query from the user and a answer from service.

### [QueryConfigEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Session.Turn.QueryConfigEntry)

The abstract base class for a message.

### [SingleRegionKey](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SingleRegionKey)

Metadata for single-regional CMEKs.

### [SiteSearchEngine](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SiteSearchEngine)

SiteSearchEngine captures DataStore level site search persisting configurations. It is a singleton value per data store.

### [SiteVerificationInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SiteVerificationInfo)

Verification information for target sites in advanced site search.

### [SiteVerificationState](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SiteVerificationInfo.SiteVerificationState)

Site verification state.

### [Sitemap](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Sitemap)

A sitemap for the SiteSearchEngine.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [SolutionType](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SolutionType)

The type of solution.

### [SpannerSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SpannerSource)

The Spanner source for importing data

### [StreamAssistRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.StreamAssistRequest)

Request for the AssistantService.StreamAssist method.

### [AgentsSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.StreamAssistRequest.AgentsSpec)

Specification of agents that are used to serve the request.

### [AgentSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.StreamAssistRequest.AgentsSpec.AgentSpec)

Specification of an agent.

### [GenerationSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.StreamAssistRequest.GenerationSpec)

Assistant generation specification for the request. This allows to override the default generation configuration at the engine level.

### [ToolsSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.StreamAssistRequest.ToolsSpec)

Specification of tools that are used to serve the request.

### [ImageGenerationSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.StreamAssistRequest.ToolsSpec.ImageGenerationSpec)

Specification of the image generation tool.

### [VertexAiSearchSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.StreamAssistRequest.ToolsSpec.VertexAiSearchSpec)

Specification of the Vertex AI Search tool.

### [VideoGenerationSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.StreamAssistRequest.ToolsSpec.VideoGenerationSpec)

Specification of the video generation tool.

### [WebGroundingSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.StreamAssistRequest.ToolsSpec.WebGroundingSpec)

Specification of the web grounding tool.

### [StreamAssistResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.StreamAssistResponse)

Response for the AssistantService.StreamAssist method.

### [SessionInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.StreamAssistResponse.SessionInfo)

Information about the session.

### [SuggestionDenyListEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SuggestionDenyListEntry)

Suggestion deny list entry identifying the phrase to block from suggestions and the applied operation for the phrase.

### [MatchOperator](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SuggestionDenyListEntry.MatchOperator)

Operator for matching with the generated suggestions.

### [TargetSite](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.TargetSite)

A target site for the SiteSearchEngine.

### [FailureReason](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.TargetSite.FailureReason)

Site search indexing failure reasons.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [QuotaFailure](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.TargetSite.FailureReason.QuotaFailure)

Failed due to insufficient quota.

### [IndexingStatus](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.TargetSite.IndexingStatus)

Target site indexing status enumeration.
    
    
        1. target site deleted if unindexing is
            successful;
        2. state reverts to SUCCEEDED if the unindexing
            fails.
    CANCELLABLE (5):
        The target site change is pending but
        cancellable.
    CANCELLED (6):
        The target site change is cancelled.
    

### [Type](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.TargetSite.Type)

Possible target site types.

### [TextInput](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.TextInput)

Defines text input.

### [TrainCustomModelMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.TrainCustomModelMetadata)

Metadata related to the progress of the TrainCustomModel operation. This is returned by the google.longrunning.Operation.metadata field.

### [TrainCustomModelRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.TrainCustomModelRequest)

Request message for SearchTuningService.TrainCustomModel method.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [GcsTrainingInput](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.TrainCustomModelRequest.GcsTrainingInput)

Cloud Storage training data input.

### [TrainCustomModelResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.TrainCustomModelResponse)

Response of the TrainCustomModelRequest. This message is returned by the google.longrunning.Operations.response field.

### [MetricsEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.TrainCustomModelResponse.MetricsEntry)

The abstract base class for a message.

### [TransactionInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.TransactionInfo)

A transaction represents the entire purchase transaction.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [UpdateCmekConfigMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.UpdateCmekConfigMetadata)

Metadata related to the progress of the CmekConfigService.UpdateCmekConfig operation. This will be returned by the google.longrunning.Operation.metadata field.

### [UpdateCmekConfigRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.UpdateCmekConfigRequest)

Request message for UpdateCmekConfig method. rpc.

### [UpdateControlRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.UpdateControlRequest)

Request for UpdateControl method.

### [UpdateConversationRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.UpdateConversationRequest)

Request for UpdateConversation method.

### [UpdateDataStoreRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.UpdateDataStoreRequest)

Request message for DataStoreService.UpdateDataStore method.

### [UpdateDocumentRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.UpdateDocumentRequest)

Request message for DocumentService.UpdateDocument method.

### [UpdateEngineRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.UpdateEngineRequest)

Request message for EngineService.UpdateEngine method.

### [UpdateSchemaMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.UpdateSchemaMetadata)

Metadata for UpdateSchema LRO.

### [UpdateSchemaRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.UpdateSchemaRequest)

Request message for SchemaService.UpdateSchema method.

### [UpdateServingConfigRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.UpdateServingConfigRequest)

Request for UpdateServingConfig method.

### [UpdateSessionRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.UpdateSessionRequest)

Request for UpdateSession method.

### [UpdateTargetSiteMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.UpdateTargetSiteMetadata)

Metadata related to the progress of the SiteSearchEngineService.UpdateTargetSite operation. This will be returned by the google.longrunning.Operation.metadata field.

### [UpdateTargetSiteRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.UpdateTargetSiteRequest)

Request message for SiteSearchEngineService.UpdateTargetSite method.

### [UserEvent](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.UserEvent)

UserEvent captures all metadata information Discovery Engine API needs to know about how end users interact with your website.

### [AttributesEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.UserEvent.AttributesEntry)

The abstract base class for a message.

### [UserInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.UserInfo)

Information of an end user.

### [UserLicense](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.UserLicense)

User License information assigned by the admin.

### [LicenseAssignmentState](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.UserLicense.LicenseAssignmentState)

License assignment state enumeration.

### [WorkspaceConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.WorkspaceConfig)

Config to store data store type configuration for workspace data

### [Type](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.WorkspaceConfig.Type)

Specifies the type of Workspace App supported by this DataStore

### [WriteUserEventRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.WriteUserEventRequest)

Request message for WriteUserEvent method.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AclConfigServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.acl_config_service.AclConfigServiceAsyncClient)

Service for managing Acl Configuration.

### [AclConfigServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.acl_config_service.AclConfigServiceClient)

Service for managing Acl Configuration.

### [ChunkServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.chunk_service.ChunkServiceAsyncClient)

Service for displaying processed Chunk information of the customer's unstructured data.

### [ChunkServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.chunk_service.ChunkServiceClient)

Service for displaying processed Chunk information of the customer's unstructured data.

### [ListChunksAsyncPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.chunk_service.pagers.ListChunksAsyncPager)

A pager for iterating through `list_chunks` requests.

This class thinly wraps an initial [ListChunksResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListChunksResponse) object, and provides an `__aiter__` method to iterate through its `chunks` field.

If there are more pages, the `__aiter__` method will make additional `ListChunks` requests and continue to iterate through the `chunks` field on the corresponding responses.

All the usual [ListChunksResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListChunksResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListChunksPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.chunk_service.pagers.ListChunksPager)

A pager for iterating through `list_chunks` requests.

This class thinly wraps an initial [ListChunksResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListChunksResponse) object, and provides an `__iter__` method to iterate through its `chunks` field.

If there are more pages, the `__iter__` method will make additional `ListChunks` requests and continue to iterate through the `chunks` field on the corresponding responses.

All the usual [ListChunksResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListChunksResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [CompletionServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.completion_service.CompletionServiceAsyncClient)

Service for Auto-Completion.

### [CompletionServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.completion_service.CompletionServiceClient)

Service for Auto-Completion.

### [ControlServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.control_service.ControlServiceAsyncClient)

Service for performing CRUD operations on Controls. Controls allow for custom logic to be implemented in the serving path. Controls need to be attached to a Serving Config to be considered during a request.

### [ControlServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.control_service.ControlServiceClient)

Service for performing CRUD operations on Controls. Controls allow for custom logic to be implemented in the serving path. Controls need to be attached to a Serving Config to be considered during a request.

### [ListControlsAsyncPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.control_service.pagers.ListControlsAsyncPager)

A pager for iterating through `list_controls` requests.

This class thinly wraps an initial [ListControlsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListControlsResponse) object, and provides an `__aiter__` method to iterate through its `controls` field.

If there are more pages, the `__aiter__` method will make additional `ListControls` requests and continue to iterate through the `controls` field on the corresponding responses.

All the usual [ListControlsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListControlsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListControlsPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.control_service.pagers.ListControlsPager)

A pager for iterating through `list_controls` requests.

This class thinly wraps an initial [ListControlsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListControlsResponse) object, and provides an `__iter__` method to iterate through its `controls` field.

If there are more pages, the `__iter__` method will make additional `ListControls` requests and continue to iterate through the `controls` field on the corresponding responses.

All the usual [ListControlsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListControlsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ConversationalSearchServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.conversational_search_service.ConversationalSearchServiceAsyncClient)

Service for conversational search.

### [ConversationalSearchServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.conversational_search_service.ConversationalSearchServiceClient)

Service for conversational search.

### [ListConversationsAsyncPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.conversational_search_service.pagers.ListConversationsAsyncPager)

A pager for iterating through `list_conversations` requests.

This class thinly wraps an initial [ListConversationsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListConversationsResponse) object, and provides an `__aiter__` method to iterate through its `conversations` field.

If there are more pages, the `__aiter__` method will make additional `ListConversations` requests and continue to iterate through the `conversations` field on the corresponding responses.

All the usual [ListConversationsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListConversationsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListConversationsPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.conversational_search_service.pagers.ListConversationsPager)

A pager for iterating through `list_conversations` requests.

This class thinly wraps an initial [ListConversationsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListConversationsResponse) object, and provides an `__iter__` method to iterate through its `conversations` field.

If there are more pages, the `__iter__` method will make additional `ListConversations` requests and continue to iterate through the `conversations` field on the corresponding responses.

All the usual [ListConversationsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListConversationsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListSessionsAsyncPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.conversational_search_service.pagers.ListSessionsAsyncPager)

A pager for iterating through `list_sessions` requests.

This class thinly wraps an initial [ListSessionsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListSessionsResponse) object, and provides an `__aiter__` method to iterate through its `sessions` field.

If there are more pages, the `__aiter__` method will make additional `ListSessions` requests and continue to iterate through the `sessions` field on the corresponding responses.

All the usual [ListSessionsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListSessionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListSessionsPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.conversational_search_service.pagers.ListSessionsPager)

A pager for iterating through `list_sessions` requests.

This class thinly wraps an initial [ListSessionsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListSessionsResponse) object, and provides an `__iter__` method to iterate through its `sessions` field.

If there are more pages, the `__iter__` method will make additional `ListSessions` requests and continue to iterate through the `sessions` field on the corresponding responses.

All the usual [ListSessionsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListSessionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [DataStoreServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.data_store_service.DataStoreServiceAsyncClient)

Service for managing DataStore configuration.

### [DataStoreServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.data_store_service.DataStoreServiceClient)

Service for managing DataStore configuration.

### [ListDataStoresAsyncPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.data_store_service.pagers.ListDataStoresAsyncPager)

A pager for iterating through `list_data_stores` requests.

This class thinly wraps an initial [ListDataStoresResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListDataStoresResponse) object, and provides an `__aiter__` method to iterate through its `data_stores` field.

If there are more pages, the `__aiter__` method will make additional `ListDataStores` requests and continue to iterate through the `data_stores` field on the corresponding responses.

All the usual [ListDataStoresResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListDataStoresResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListDataStoresPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.data_store_service.pagers.ListDataStoresPager)

A pager for iterating through `list_data_stores` requests.

This class thinly wraps an initial [ListDataStoresResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListDataStoresResponse) object, and provides an `__iter__` method to iterate through its `data_stores` field.

If there are more pages, the `__iter__` method will make additional `ListDataStores` requests and continue to iterate through the `data_stores` field on the corresponding responses.

All the usual [ListDataStoresResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListDataStoresResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [DocumentServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.document_service.DocumentServiceAsyncClient)

Service for ingesting Document information of the customer's website.

### [DocumentServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.document_service.DocumentServiceClient)

Service for ingesting Document information of the customer's website.

### [ListDocumentsAsyncPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.document_service.pagers.ListDocumentsAsyncPager)

A pager for iterating through `list_documents` requests.

This class thinly wraps an initial [ListDocumentsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListDocumentsResponse) object, and provides an `__aiter__` method to iterate through its `documents` field.

If there are more pages, the `__aiter__` method will make additional `ListDocuments` requests and continue to iterate through the `documents` field on the corresponding responses.

All the usual [ListDocumentsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListDocumentsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListDocumentsPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.document_service.pagers.ListDocumentsPager)

A pager for iterating through `list_documents` requests.

This class thinly wraps an initial [ListDocumentsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListDocumentsResponse) object, and provides an `__iter__` method to iterate through its `documents` field.

If there are more pages, the `__iter__` method will make additional `ListDocuments` requests and continue to iterate through the `documents` field on the corresponding responses.

All the usual [ListDocumentsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListDocumentsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [EngineServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.engine_service.EngineServiceAsyncClient)

Service for managing Engine configuration.

### [EngineServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.engine_service.EngineServiceClient)

Service for managing Engine configuration.

### [ListEnginesAsyncPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.engine_service.pagers.ListEnginesAsyncPager)

A pager for iterating through `list_engines` requests.

This class thinly wraps an initial [ListEnginesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListEnginesResponse) object, and provides an `__aiter__` method to iterate through its `engines` field.

If there are more pages, the `__aiter__` method will make additional `ListEngines` requests and continue to iterate through the `engines` field on the corresponding responses.

All the usual [ListEnginesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListEnginesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListEnginesPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.engine_service.pagers.ListEnginesPager)

A pager for iterating through `list_engines` requests.

This class thinly wraps an initial [ListEnginesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListEnginesResponse) object, and provides an `__iter__` method to iterate through its `engines` field.

If there are more pages, the `__iter__` method will make additional `ListEngines` requests and continue to iterate through the `engines` field on the corresponding responses.

All the usual [ListEnginesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListEnginesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [EstimateBillingServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.estimate_billing_service.EstimateBillingServiceAsyncClient)

Service for managing billing estimations resources.

### [EstimateBillingServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.estimate_billing_service.EstimateBillingServiceClient)

Service for managing billing estimations resources.

### [EvaluationServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.evaluation_service.EvaluationServiceAsyncClient)

Service for managing Evaluations,

### [EvaluationServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.evaluation_service.EvaluationServiceClient)

Service for managing Evaluations,

### [ListEvaluationResultsAsyncPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.evaluation_service.pagers.ListEvaluationResultsAsyncPager)

A pager for iterating through `list_evaluation_results` requests.

This class thinly wraps an initial [ListEvaluationResultsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListEvaluationResultsResponse) object, and provides an `__aiter__` method to iterate through its `evaluation_results` field.

If there are more pages, the `__aiter__` method will make additional `ListEvaluationResults` requests and continue to iterate through the `evaluation_results` field on the corresponding responses.

All the usual [ListEvaluationResultsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListEvaluationResultsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListEvaluationResultsPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.evaluation_service.pagers.ListEvaluationResultsPager)

A pager for iterating through `list_evaluation_results` requests.

This class thinly wraps an initial [ListEvaluationResultsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListEvaluationResultsResponse) object, and provides an `__iter__` method to iterate through its `evaluation_results` field.

If there are more pages, the `__iter__` method will make additional `ListEvaluationResults` requests and continue to iterate through the `evaluation_results` field on the corresponding responses.

All the usual [ListEvaluationResultsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListEvaluationResultsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListEvaluationsAsyncPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.evaluation_service.pagers.ListEvaluationsAsyncPager)

A pager for iterating through `list_evaluations` requests.

This class thinly wraps an initial [ListEvaluationsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListEvaluationsResponse) object, and provides an `__aiter__` method to iterate through its `evaluations` field.

If there are more pages, the `__aiter__` method will make additional `ListEvaluations` requests and continue to iterate through the `evaluations` field on the corresponding responses.

All the usual [ListEvaluationsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListEvaluationsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListEvaluationsPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.evaluation_service.pagers.ListEvaluationsPager)

A pager for iterating through `list_evaluations` requests.

This class thinly wraps an initial [ListEvaluationsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListEvaluationsResponse) object, and provides an `__iter__` method to iterate through its `evaluations` field.

If there are more pages, the `__iter__` method will make additional `ListEvaluations` requests and continue to iterate through the `evaluations` field on the corresponding responses.

All the usual [ListEvaluationsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListEvaluationsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [GroundedGenerationServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.grounded_generation_service.GroundedGenerationServiceAsyncClient)

Service for grounded generation.

### [GroundedGenerationServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.grounded_generation_service.GroundedGenerationServiceClient)

Service for grounded generation.

### [ProjectServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.project_service.ProjectServiceAsyncClient)

Service for operations on the Project.

### [ProjectServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.project_service.ProjectServiceClient)

Service for operations on the Project.

### [RankServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.rank_service.RankServiceAsyncClient)

Service for ranking text records.

### [RankServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.rank_service.RankServiceClient)

Service for ranking text records.

### [RecommendationServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.recommendation_service.RecommendationServiceAsyncClient)

Service for making recommendations.

### [RecommendationServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.recommendation_service.RecommendationServiceClient)

Service for making recommendations.

### [SampleQueryServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.sample_query_service.SampleQueryServiceAsyncClient)

Service for managing SampleQuerys,

### [SampleQueryServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.sample_query_service.SampleQueryServiceClient)

Service for managing SampleQuerys,

### [ListSampleQueriesAsyncPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.sample_query_service.pagers.ListSampleQueriesAsyncPager)

A pager for iterating through `list_sample_queries` requests.

This class thinly wraps an initial [ListSampleQueriesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListSampleQueriesResponse) object, and provides an `__aiter__` method to iterate through its `sample_queries` field.

If there are more pages, the `__aiter__` method will make additional `ListSampleQueries` requests and continue to iterate through the `sample_queries` field on the corresponding responses.

All the usual [ListSampleQueriesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListSampleQueriesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListSampleQueriesPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.sample_query_service.pagers.ListSampleQueriesPager)

A pager for iterating through `list_sample_queries` requests.

This class thinly wraps an initial [ListSampleQueriesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListSampleQueriesResponse) object, and provides an `__iter__` method to iterate through its `sample_queries` field.

If there are more pages, the `__iter__` method will make additional `ListSampleQueries` requests and continue to iterate through the `sample_queries` field on the corresponding responses.

All the usual [ListSampleQueriesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListSampleQueriesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [SampleQuerySetServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.sample_query_set_service.SampleQuerySetServiceAsyncClient)

Service for managing SampleQuerySets,

### [SampleQuerySetServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.sample_query_set_service.SampleQuerySetServiceClient)

Service for managing SampleQuerySets,

### [ListSampleQuerySetsAsyncPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.sample_query_set_service.pagers.ListSampleQuerySetsAsyncPager)

A pager for iterating through `list_sample_query_sets` requests.

This class thinly wraps an initial [ListSampleQuerySetsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListSampleQuerySetsResponse) object, and provides an `__aiter__` method to iterate through its `sample_query_sets` field.

If there are more pages, the `__aiter__` method will make additional `ListSampleQuerySets` requests and continue to iterate through the `sample_query_sets` field on the corresponding responses.

All the usual [ListSampleQuerySetsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListSampleQuerySetsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListSampleQuerySetsPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.sample_query_set_service.pagers.ListSampleQuerySetsPager)

A pager for iterating through `list_sample_query_sets` requests.

This class thinly wraps an initial [ListSampleQuerySetsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListSampleQuerySetsResponse) object, and provides an `__iter__` method to iterate through its `sample_query_sets` field.

If there are more pages, the `__iter__` method will make additional `ListSampleQuerySets` requests and continue to iterate through the `sample_query_sets` field on the corresponding responses.

All the usual [ListSampleQuerySetsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListSampleQuerySetsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [SchemaServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.schema_service.SchemaServiceAsyncClient)

Service for managing Schemas.

### [SchemaServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.schema_service.SchemaServiceClient)

Service for managing Schemas.

### [ListSchemasAsyncPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.schema_service.pagers.ListSchemasAsyncPager)

A pager for iterating through `list_schemas` requests.

This class thinly wraps an initial [ListSchemasResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListSchemasResponse) object, and provides an `__aiter__` method to iterate through its `schemas` field.

If there are more pages, the `__aiter__` method will make additional `ListSchemas` requests and continue to iterate through the `schemas` field on the corresponding responses.

All the usual [ListSchemasResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListSchemasResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListSchemasPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.schema_service.pagers.ListSchemasPager)

A pager for iterating through `list_schemas` requests.

This class thinly wraps an initial [ListSchemasResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListSchemasResponse) object, and provides an `__iter__` method to iterate through its `schemas` field.

If there are more pages, the `__iter__` method will make additional `ListSchemas` requests and continue to iterate through the `schemas` field on the corresponding responses.

All the usual [ListSchemasResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListSchemasResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [SearchServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.search_service.SearchServiceAsyncClient)

Service for search.

### [SearchServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.search_service.SearchServiceClient)

Service for search.

### [SearchAsyncPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.search_service.pagers.SearchAsyncPager)

A pager for iterating through `search` requests.

This class thinly wraps an initial [SearchResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchResponse) object, and provides an `__aiter__` method to iterate through its `results` field.

If there are more pages, the `__aiter__` method will make additional `Search` requests and continue to iterate through the `results` field on the corresponding responses.

All the usual [SearchResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [SearchPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.search_service.pagers.SearchPager)

A pager for iterating through `search` requests.

This class thinly wraps an initial [SearchResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchResponse) object, and provides an `__iter__` method to iterate through its `results` field.

If there are more pages, the `__iter__` method will make additional `Search` requests and continue to iterate through the `results` field on the corresponding responses.

All the usual [SearchResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [SearchTuningServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.search_tuning_service.SearchTuningServiceAsyncClient)

Service for search tuning.

### [SearchTuningServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.search_tuning_service.SearchTuningServiceClient)

Service for search tuning.

### [ServingConfigServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.serving_config_service.ServingConfigServiceAsyncClient)

Service for operations related to ServingConfig.

### [ServingConfigServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.serving_config_service.ServingConfigServiceClient)

Service for operations related to ServingConfig.

### [ListServingConfigsAsyncPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.serving_config_service.pagers.ListServingConfigsAsyncPager)

A pager for iterating through `list_serving_configs` requests.

This class thinly wraps an initial [ListServingConfigsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListServingConfigsResponse) object, and provides an `__aiter__` method to iterate through its `serving_configs` field.

If there are more pages, the `__aiter__` method will make additional `ListServingConfigs` requests and continue to iterate through the `serving_configs` field on the corresponding responses.

All the usual [ListServingConfigsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListServingConfigsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListServingConfigsPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.serving_config_service.pagers.ListServingConfigsPager)

A pager for iterating through `list_serving_configs` requests.

This class thinly wraps an initial [ListServingConfigsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListServingConfigsResponse) object, and provides an `__iter__` method to iterate through its `serving_configs` field.

If there are more pages, the `__iter__` method will make additional `ListServingConfigs` requests and continue to iterate through the `serving_configs` field on the corresponding responses.

All the usual [ListServingConfigsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListServingConfigsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [SessionServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.session_service.SessionServiceAsyncClient)

Service for managing Sessions and Session-related resources.

### [SessionServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.session_service.SessionServiceClient)

Service for managing Sessions and Session-related resources.

### [ListFilesAsyncPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.session_service.pagers.ListFilesAsyncPager)

A pager for iterating through `list_files` requests.

This class thinly wraps an initial [ListFilesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListFilesResponse) object, and provides an `__aiter__` method to iterate through its `files` field.

If there are more pages, the `__aiter__` method will make additional `ListFiles` requests and continue to iterate through the `files` field on the corresponding responses.

All the usual [ListFilesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListFilesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListFilesPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.session_service.pagers.ListFilesPager)

A pager for iterating through `list_files` requests.

This class thinly wraps an initial [ListFilesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListFilesResponse) object, and provides an `__iter__` method to iterate through its `files` field.

If there are more pages, the `__iter__` method will make additional `ListFiles` requests and continue to iterate through the `files` field on the corresponding responses.

All the usual [ListFilesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListFilesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListSessionsAsyncPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.session_service.pagers.ListSessionsAsyncPager)

A pager for iterating through `list_sessions` requests.

This class thinly wraps an initial [ListSessionsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListSessionsResponse) object, and provides an `__aiter__` method to iterate through its `sessions` field.

If there are more pages, the `__aiter__` method will make additional `ListSessions` requests and continue to iterate through the `sessions` field on the corresponding responses.

All the usual [ListSessionsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListSessionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListSessionsPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.session_service.pagers.ListSessionsPager)

A pager for iterating through `list_sessions` requests.

This class thinly wraps an initial [ListSessionsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListSessionsResponse) object, and provides an `__iter__` method to iterate through its `sessions` field.

If there are more pages, the `__iter__` method will make additional `ListSessions` requests and continue to iterate through the `sessions` field on the corresponding responses.

All the usual [ListSessionsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListSessionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [SiteSearchEngineServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.site_search_engine_service.SiteSearchEngineServiceAsyncClient)

Service for managing site search related resources.

### [SiteSearchEngineServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.site_search_engine_service.SiteSearchEngineServiceClient)

Service for managing site search related resources.

### [FetchDomainVerificationStatusAsyncPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.site_search_engine_service.pagers.FetchDomainVerificationStatusAsyncPager)

A pager for iterating through `fetch_domain_verification_status` requests.

This class thinly wraps an initial [FetchDomainVerificationStatusResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.FetchDomainVerificationStatusResponse) object, and provides an `__aiter__` method to iterate through its `target_sites` field.

If there are more pages, the `__aiter__` method will make additional `FetchDomainVerificationStatus` requests and continue to iterate through the `target_sites` field on the corresponding responses.

All the usual [FetchDomainVerificationStatusResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.FetchDomainVerificationStatusResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [FetchDomainVerificationStatusPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.site_search_engine_service.pagers.FetchDomainVerificationStatusPager)

A pager for iterating through `fetch_domain_verification_status` requests.

This class thinly wraps an initial [FetchDomainVerificationStatusResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.FetchDomainVerificationStatusResponse) object, and provides an `__iter__` method to iterate through its `target_sites` field.

If there are more pages, the `__iter__` method will make additional `FetchDomainVerificationStatus` requests and continue to iterate through the `target_sites` field on the corresponding responses.

All the usual [FetchDomainVerificationStatusResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.FetchDomainVerificationStatusResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListTargetSitesAsyncPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.site_search_engine_service.pagers.ListTargetSitesAsyncPager)

A pager for iterating through `list_target_sites` requests.

This class thinly wraps an initial [ListTargetSitesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListTargetSitesResponse) object, and provides an `__aiter__` method to iterate through its `target_sites` field.

If there are more pages, the `__aiter__` method will make additional `ListTargetSites` requests and continue to iterate through the `target_sites` field on the corresponding responses.

All the usual [ListTargetSitesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListTargetSitesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListTargetSitesPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.site_search_engine_service.pagers.ListTargetSitesPager)

A pager for iterating through `list_target_sites` requests.

This class thinly wraps an initial [ListTargetSitesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListTargetSitesResponse) object, and provides an `__iter__` method to iterate through its `target_sites` field.

If there are more pages, the `__iter__` method will make additional `ListTargetSites` requests and continue to iterate through the `target_sites` field on the corresponding responses.

All the usual [ListTargetSitesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListTargetSitesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [UserEventServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.user_event_service.UserEventServiceAsyncClient)

Service for ingesting end user actions on a website to Discovery Engine API.

### [UserEventServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.user_event_service.UserEventServiceClient)

Service for ingesting end user actions on a website to Discovery Engine API.

### [AclConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.AclConfig)

Access Control Configuration.

### [AlloyDbSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.AlloyDbSource)

AlloyDB source import data from.

### [Answer](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Answer)

Defines an answer.

### [AnswerSkippedReason](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Answer.AnswerSkippedReason)

An enum for answer skipped reasons.
    
    
        Google skips the answer if there are no
        high-relevance search results.
    POTENTIAL_POLICY_VIOLATION (4):
        The potential policy violation case.
    
        Google skips the answer if there is a potential
        policy violation detected. This includes content
        that may be violent or toxic.
    NO_RELEVANT_CONTENT (5):
        The no relevant content case.
    
        Google skips the answer if there is no relevant
        content in the retrieved search results.
    JAIL_BREAKING_QUERY_IGNORED (6):
        The jail-breaking query ignored case.
    
        For example, "Reply in the tone of a competing
        company's CEO". Google skips the answer if the
        query is classified as a jail-breaking query.
    CUSTOMER_POLICY_VIOLATION (7):
        The customer policy violation case.
    
        Google skips the summary if there is a customer
        policy violation detected. The policy is defined
        by the customer.
    

### [Citation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Answer.Citation)

Citation info for a segment.

### [CitationSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Answer.CitationSource)

Citation source.

### [QueryUnderstandingInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Answer.QueryUnderstandingInfo)

Query understanding information.

### [QueryClassificationInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Answer.QueryUnderstandingInfo.QueryClassificationInfo)

Query classification information.

### [Type](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Answer.QueryUnderstandingInfo.QueryClassificationInfo.Type)

Query classification types.

### [Reference](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Answer.Reference)

Reference.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ChunkInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Answer.Reference.ChunkInfo)

Chunk information.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [DocumentMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Answer.Reference.ChunkInfo.DocumentMetadata)

Document metadata.

### [StructuredDocumentInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Answer.Reference.StructuredDocumentInfo)

Structured search information.

### [UnstructuredDocumentInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Answer.Reference.UnstructuredDocumentInfo)

Unstructured document information.

### [ChunkContent](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Answer.Reference.UnstructuredDocumentInfo.ChunkContent)

Chunk content.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [State](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Answer.State)

Enumeration of the state of the answer generation.

### [Step](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Answer.Step)

Step information.

### [Action](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Answer.Step.Action)

Action.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Observation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Answer.Step.Action.Observation)

Observation.

### [SearchResult](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Answer.Step.Action.Observation.SearchResult)

### [ChunkInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Answer.Step.Action.Observation.SearchResult.ChunkInfo)

Chunk information.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [SnippetInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Answer.Step.Action.Observation.SearchResult.SnippetInfo)

Snippet information.

### [SearchAction](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Answer.Step.Action.SearchAction)

Search action.

### [State](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Answer.Step.State)

Enumeration of the state of the step.

### [AnswerQueryRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.AnswerQueryRequest)

Request message for ConversationalSearchService.AnswerQuery method.

### [AnswerGenerationSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.AnswerQueryRequest.AnswerGenerationSpec)

Answer generation specification.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ModelSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.AnswerQueryRequest.AnswerGenerationSpec.ModelSpec)

Answer Generation Model specification.

### [PromptSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.AnswerQueryRequest.AnswerGenerationSpec.PromptSpec)

Answer generation prompt specification.

### [QueryUnderstandingSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.AnswerQueryRequest.QueryUnderstandingSpec)

Query understanding specification.

### [QueryClassificationSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.AnswerQueryRequest.QueryUnderstandingSpec.QueryClassificationSpec)

Query classification specification.

### [Type](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.AnswerQueryRequest.QueryUnderstandingSpec.QueryClassificationSpec.Type)

Query classification types.

### [QueryRephraserSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.AnswerQueryRequest.QueryUnderstandingSpec.QueryRephraserSpec)

Query rephraser specification.

### [RelatedQuestionsSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.AnswerQueryRequest.RelatedQuestionsSpec)

Related questions specification.

### [SafetySpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.AnswerQueryRequest.SafetySpec)

Safety specification.

### [SearchSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.AnswerQueryRequest.SearchSpec)

Search specification.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [SearchParams](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.AnswerQueryRequest.SearchSpec.SearchParams)

Search parameters.

### [SearchResultList](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.AnswerQueryRequest.SearchSpec.SearchResultList)

Search result list.

### [SearchResult](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.AnswerQueryRequest.SearchSpec.SearchResultList.SearchResult)

Search result.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ChunkInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.AnswerQueryRequest.SearchSpec.SearchResultList.SearchResult.ChunkInfo)

Chunk information.

### [UnstructuredDocumentInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.AnswerQueryRequest.SearchSpec.SearchResultList.SearchResult.UnstructuredDocumentInfo)

Unstructured document information.

### [DocumentContext](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.AnswerQueryRequest.SearchSpec.SearchResultList.SearchResult.UnstructuredDocumentInfo.DocumentContext)

Document context.

### [ExtractiveAnswer](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.AnswerQueryRequest.SearchSpec.SearchResultList.SearchResult.UnstructuredDocumentInfo.ExtractiveAnswer)

Extractive answer. `Guide <https://cloud.google.com/generative-ai-app-builder/docs/snippets#get-answers>`__

### [ExtractiveSegment](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.AnswerQueryRequest.SearchSpec.SearchResultList.SearchResult.UnstructuredDocumentInfo.ExtractiveSegment)

Extractive segment. `Guide <https://cloud.google.com/generative-ai-app-builder/docs/snippets#extractive-segments>`__

### [UserLabelsEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.AnswerQueryRequest.UserLabelsEntry)

The abstract base class for a message.

### [AnswerQueryResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.AnswerQueryResponse)

Response message for ConversationalSearchService.AnswerQuery method.

### [BatchCreateTargetSiteMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.BatchCreateTargetSiteMetadata)

Metadata related to the progress of the SiteSearchEngineService.BatchCreateTargetSites operation. This will be returned by the google.longrunning.Operation.metadata field.

### [BatchCreateTargetSitesRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.BatchCreateTargetSitesRequest)

Request message for SiteSearchEngineService.BatchCreateTargetSites method.

### [BatchCreateTargetSitesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.BatchCreateTargetSitesResponse)

Response message for SiteSearchEngineService.BatchCreateTargetSites method.

### [BatchGetDocumentsMetadataRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.BatchGetDocumentsMetadataRequest)

Request message for DocumentService.BatchGetDocumentsMetadata method.

### [Matcher](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.BatchGetDocumentsMetadataRequest.Matcher)

Matcher for the Documents. Currently supports matching by exact URIs.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [UrisMatcher](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.BatchGetDocumentsMetadataRequest.UrisMatcher)

Matcher for the Documents by exact uris.

### [BatchGetDocumentsMetadataResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.BatchGetDocumentsMetadataResponse)

Response message for DocumentService.BatchGetDocumentsMetadata method.

### [DocumentMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.BatchGetDocumentsMetadataResponse.DocumentMetadata)

The metadata of a Document.

### [MatcherValue](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.BatchGetDocumentsMetadataResponse.DocumentMetadata.MatcherValue)

The value of the matcher that was used to match the Document.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [State](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.BatchGetDocumentsMetadataResponse.State)

The state of the Document.

### [BatchVerifyTargetSitesMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.BatchVerifyTargetSitesMetadata)

Metadata related to the progress of the SiteSearchEngineService.BatchVerifyTargetSites operation. This will be returned by the google.longrunning.Operation.metadata field.

### [BatchVerifyTargetSitesRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.BatchVerifyTargetSitesRequest)

Request message for SiteSearchEngineService.BatchVerifyTargetSites method.

### [BatchVerifyTargetSitesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.BatchVerifyTargetSitesResponse)

Response message for SiteSearchEngineService.BatchVerifyTargetSites method.

### [BigQuerySource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.BigQuerySource)

BigQuery source import data from.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [BigtableOptions](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.BigtableOptions)

The Bigtable Options object that contains information to support the import.

### [BigtableColumn](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.BigtableOptions.BigtableColumn)

The column of the Bigtable.

### [BigtableColumnFamily](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.BigtableOptions.BigtableColumnFamily)

The column family of the Bigtable.

### [Encoding](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.BigtableOptions.Encoding)

The encoding mode of a Bigtable column or column family.

### [FamiliesEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.BigtableOptions.FamiliesEntry)

The abstract base class for a message.

### [Type](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.BigtableOptions.Type)

The type of values in a Bigtable column or column family. The values are expected to be encoded using `HBase Bytes.toBytes <https://hbase.apache.org/apidocs/org/apache/hadoop/hbase/util/Bytes.html>`__ function when the encoding value is set to `BINARY`.

### [BigtableSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.BigtableSource)

The Cloud Bigtable source for importing data.

### [CheckGroundingRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.CheckGroundingRequest)

Request message for GroundedGenerationService.CheckGrounding method.

### [UserLabelsEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.CheckGroundingRequest.UserLabelsEntry)

The abstract base class for a message.

### [CheckGroundingResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.CheckGroundingResponse)

Response message for the GroundedGenerationService.CheckGrounding method.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Claim](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.CheckGroundingResponse.Claim)

Text and citation info for a claim in the answer candidate.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [CheckGroundingSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.CheckGroundingSpec)

Specification for the grounding check.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Chunk](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Chunk)

Chunk captures all raw metadata information of items to be recommended or searched in the chunk mode.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ChunkMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Chunk.ChunkMetadata)

Metadata of the current chunk. This field is only populated on SearchService.Search API.

### [DocumentMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Chunk.DocumentMetadata)

Document metadata contains the information of the document of the current chunk.

### [PageSpan](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Chunk.PageSpan)

Page span of the chunk.

### [CloudSqlSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.CloudSqlSource)

Cloud SQL source import data from.

### [CollectUserEventRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.CollectUserEventRequest)

Request message for CollectUserEvent method.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [CompleteQueryRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.CompleteQueryRequest)

Request message for CompletionService.CompleteQuery method.

### [CompleteQueryResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.CompleteQueryResponse)

Response message for CompletionService.CompleteQuery method.

### [QuerySuggestion](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.CompleteQueryResponse.QuerySuggestion)

Suggestions as search queries.

### [CompletionInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.CompletionInfo)

Detailed completion information including completion attribution token and clicked completion info.

### [CompletionSuggestion](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.CompletionSuggestion)

Autocomplete suggestions that are imported from Customer.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Condition](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Condition)

Defines circumstances to be checked before allowing a behavior

### [QueryTerm](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Condition.QueryTerm)

Matcher for search request query

### [TimeRange](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Condition.TimeRange)

Used for time-dependent conditions.

### [Control](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Control)

Defines a conditioned behavior to employ during serving. Must be attached to a ServingConfig to be considered at serving time. Permitted actions dependent on `SolutionType`.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [BoostAction](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Control.BoostAction)

Adjusts order of products in returned list.

### [FilterAction](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Control.FilterAction)

Specified which products may be included in results. Uses same filter as boost.

### [RedirectAction](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Control.RedirectAction)

Redirects a shopper to the provided URI.

### [SynonymsAction](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Control.SynonymsAction)

Creates a set of terms that will act as synonyms of one another. Example: "happy" will also be considered as "glad", "glad" will also be considered as "happy".

### [Conversation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Conversation)

External conversation proto definition.

### [State](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Conversation.State)

Enumeration of the state of the conversation.

### [ConversationContext](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ConversationContext)

Defines context of the conversation

### [ConversationMessage](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ConversationMessage)

Defines a conversation message.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ConverseConversationRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ConverseConversationRequest)

Request message for ConversationalSearchService.ConverseConversation method.

### [UserLabelsEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ConverseConversationRequest.UserLabelsEntry)

The abstract base class for a message.

### [ConverseConversationResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ConverseConversationResponse)

Response message for ConversationalSearchService.ConverseConversation method.

### [CreateControlRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.CreateControlRequest)

Request for CreateControl method.

### [CreateConversationRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.CreateConversationRequest)

Request for CreateConversation method.

### [CreateDataStoreMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.CreateDataStoreMetadata)

Metadata related to the progress of the DataStoreService.CreateDataStore operation. This will be returned by the google.longrunning.Operation.metadata field.

### [CreateDataStoreRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.CreateDataStoreRequest)

Request for DataStoreService.CreateDataStore method.

### [CreateDocumentRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.CreateDocumentRequest)

Request message for DocumentService.CreateDocument method.

### [CreateEngineMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.CreateEngineMetadata)

Metadata related to the progress of the EngineService.CreateEngine operation. This will be returned by the google.longrunning.Operation.metadata field.

### [CreateEngineRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.CreateEngineRequest)

Request for EngineService.CreateEngine method.

### [CreateEvaluationMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.CreateEvaluationMetadata)

Metadata for EvaluationService.CreateEvaluation method.

### [CreateEvaluationRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.CreateEvaluationRequest)

Request message for EvaluationService.CreateEvaluation method.

### [CreateSampleQueryRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.CreateSampleQueryRequest)

Request message for SampleQueryService.CreateSampleQuery method.

### [CreateSampleQuerySetRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.CreateSampleQuerySetRequest)

Request message for SampleQuerySetService.CreateSampleQuerySet method.

### [CreateSchemaMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.CreateSchemaMetadata)

Metadata for Create Schema LRO.

### [CreateSchemaRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.CreateSchemaRequest)

Request message for SchemaService.CreateSchema method.

### [CreateSessionRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.CreateSessionRequest)

Request for CreateSession method.

### [CreateTargetSiteMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.CreateTargetSiteMetadata)

Metadata related to the progress of the SiteSearchEngineService.CreateTargetSite operation. This will be returned by the google.longrunning.Operation.metadata field.

### [CreateTargetSiteRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.CreateTargetSiteRequest)

Request message for SiteSearchEngineService.CreateTargetSite method.

### [CustomAttribute](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.CustomAttribute)

A custom attribute that is not explicitly modeled in a resource, e.g. UserEvent.

### [CustomFineTuningSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.CustomFineTuningSpec)

Defines custom fine tuning spec.

### [CustomTuningModel](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.CustomTuningModel)

Metadata that describes a custom tuned model.

### [MetricsEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.CustomTuningModel.MetricsEntry)

The abstract base class for a message.

### [ModelState](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.CustomTuningModel.ModelState)

The state of the model.

### [DataStore](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.DataStore)

DataStore captures global settings and configs at the DataStore level.

### [ContentConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.DataStore.ContentConfig)

Content config of the data store.

### [DeleteControlRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.DeleteControlRequest)

Request for DeleteControl method.

### [DeleteConversationRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.DeleteConversationRequest)

Request for DeleteConversation method.

### [DeleteDataStoreMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.DeleteDataStoreMetadata)

Metadata related to the progress of the DataStoreService.DeleteDataStore operation. This will be returned by the google.longrunning.Operation.metadata field.

### [DeleteDataStoreRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.DeleteDataStoreRequest)

Request message for DataStoreService.DeleteDataStore method.

### [DeleteDocumentRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.DeleteDocumentRequest)

Request message for DocumentService.DeleteDocument method.

### [DeleteEngineMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.DeleteEngineMetadata)

Metadata related to the progress of the EngineService.DeleteEngine operation. This will be returned by the google.longrunning.Operation.metadata field.

### [DeleteEngineRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.DeleteEngineRequest)

Request message for EngineService.DeleteEngine method.

### [DeleteSampleQueryRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.DeleteSampleQueryRequest)

Request message for SampleQueryService.DeleteSampleQuery method.

### [DeleteSampleQuerySetRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.DeleteSampleQuerySetRequest)

Request message for SampleQuerySetService.DeleteSampleQuerySet method.

### [DeleteSchemaMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.DeleteSchemaMetadata)

Metadata for DeleteSchema LRO.

### [DeleteSchemaRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.DeleteSchemaRequest)

Request message for SchemaService.DeleteSchema method.

### [DeleteSessionRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.DeleteSessionRequest)

Request for DeleteSession method.

### [DeleteTargetSiteMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.DeleteTargetSiteMetadata)

Metadata related to the progress of the SiteSearchEngineService.DeleteTargetSite operation. This will be returned by the google.longrunning.Operation.metadata field.

### [DeleteTargetSiteRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.DeleteTargetSiteRequest)

Request message for SiteSearchEngineService.DeleteTargetSite method.

### [DisableAdvancedSiteSearchMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.DisableAdvancedSiteSearchMetadata)

Metadata related to the progress of the SiteSearchEngineService.DisableAdvancedSiteSearch operation. This will be returned by the google.longrunning.Operation.metadata field.

### [DisableAdvancedSiteSearchRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.DisableAdvancedSiteSearchRequest)

Request message for SiteSearchEngineService.DisableAdvancedSiteSearch method.

### [DisableAdvancedSiteSearchResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.DisableAdvancedSiteSearchResponse)

Response message for SiteSearchEngineService.DisableAdvancedSiteSearch method.

### [Document](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Document)

Document captures all raw metadata information of items to be recommended or searched.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AclInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Document.AclInfo)

ACL Information of the Document.

### [AccessRestriction](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Document.AclInfo.AccessRestriction)

AclRestriction to model complex inheritance restrictions.

Example: Modeling a "Both Permit" inheritance, where to access a child document, user needs to have access to parent document.

Document Hierarchy - Space_S --> Page_P.

Readers: Space_S: group_1, user_1 Page_P: group_2, group_3, user_2

Space_S ACL Restriction - { "acl_info": { "readers": [ { "principals": [ { "group_id": "group_1" }, { "user_id": "user_1" } ] } ] } }

Page_P ACL Restriction. { "acl_info": { "readers": [ { "principals": [ { "group_id": "group_2" }, { "group_id": "group_3" }, { "user_id": "user_2" } ], }, { "principals": [ { "group_id": "group_1" }, { "user_id": "user_1" } ], } ] } }

### [Content](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Document.Content)

Unstructured data linked to this document.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [IndexStatus](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Document.IndexStatus)

Index status of the document.

### [DocumentInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.DocumentInfo)

Detailed document information associated with a user event.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [DocumentProcessingConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.DocumentProcessingConfig)

A singleton resource of DataStore. It's empty when DataStore is created, which defaults to digital parser. The first call to DataStoreService.UpdateDocumentProcessingConfig method will initialize the config.

### [ChunkingConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.DocumentProcessingConfig.ChunkingConfig)

Configuration for chunking config.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [LayoutBasedChunkingConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.DocumentProcessingConfig.ChunkingConfig.LayoutBasedChunkingConfig)

Configuration for the layout based chunking.

### [ParsingConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.DocumentProcessingConfig.ParsingConfig)

Related configurations applied to a specific type of document parser.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [DigitalParsingConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.DocumentProcessingConfig.ParsingConfig.DigitalParsingConfig)

The digital parsing configurations for documents.

### [LayoutParsingConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.DocumentProcessingConfig.ParsingConfig.LayoutParsingConfig)

The layout parsing configurations for documents.

### [OcrParsingConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.DocumentProcessingConfig.ParsingConfig.OcrParsingConfig)

The OCR parsing configurations for documents.

### [ParsingConfigOverridesEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.DocumentProcessingConfig.ParsingConfigOverridesEntry)

The abstract base class for a message.

### [DoubleList](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.DoubleList)

Double list.

### [EmbeddingConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.EmbeddingConfig)

Defines embedding config, used for bring your own embeddings feature.

### [EnableAdvancedSiteSearchMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.EnableAdvancedSiteSearchMetadata)

Metadata related to the progress of the SiteSearchEngineService.EnableAdvancedSiteSearch operation. This will be returned by the google.longrunning.Operation.metadata field.

### [EnableAdvancedSiteSearchRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.EnableAdvancedSiteSearchRequest)

Request message for SiteSearchEngineService.EnableAdvancedSiteSearch method.

### [EnableAdvancedSiteSearchResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.EnableAdvancedSiteSearchResponse)

Response message for SiteSearchEngineService.EnableAdvancedSiteSearch method.

### [Engine](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Engine)

Metadata that describes the training and serving parameters of an Engine.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ChatEngineConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Engine.ChatEngineConfig)

Configurations for a Chat Engine.

### [AgentCreationConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Engine.ChatEngineConfig.AgentCreationConfig)

Configurations for generating a Dialogflow agent.

Note that these configurations are one-time consumed by and passed to Dialogflow service. It means they cannot be retrieved using EngineService.GetEngine or EngineService.ListEngines API after engine creation.

### [ChatEngineMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Engine.ChatEngineMetadata)

Additional information of a Chat Engine. Fields in this message are output only.

### [CommonConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Engine.CommonConfig)

Common configurations for an Engine.

### [MediaRecommendationEngineConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Engine.MediaRecommendationEngineConfig)

Additional config specs for a Media Recommendation engine.

### [OptimizationObjectiveConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Engine.MediaRecommendationEngineConfig.OptimizationObjectiveConfig)

Custom threshold for `cvr` optimization_objective.

### [TrainingState](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Engine.MediaRecommendationEngineConfig.TrainingState)

The training state of the engine.

### [RecommendationMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Engine.RecommendationMetadata)

Additional information of a recommendation engine.

### [DataState](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Engine.RecommendationMetadata.DataState)

Describes whether this engine have sufficient training data to be continuously trained.

### [ServingState](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Engine.RecommendationMetadata.ServingState)

The serving state of the recommendation engine.

### [SearchEngineConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Engine.SearchEngineConfig)

Configurations for a Search Engine.

### [SimilarDocumentsEngineConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Engine.SimilarDocumentsEngineConfig)

Additional config specs for a `similar-items` engine.

### [EstimateDataSizeMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.EstimateDataSizeMetadata)

Metadata related to the progress of the EstimateDataSize operation. This is returned by the google.longrunning.Operation.metadata field.

### [EstimateDataSizeRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.EstimateDataSizeRequest)

Request message for EstimateBillingService.EstimateDataSize method

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [FileDataSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.EstimateDataSizeRequest.FileDataSource)

Data source contains files either in Cloud Storage or BigQuery.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [WebsiteDataSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.EstimateDataSizeRequest.WebsiteDataSource)

Data source is a set of website patterns that we crawl to get the total number of websites.

### [EstimatorUriPattern](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.EstimateDataSizeRequest.WebsiteDataSource.EstimatorUriPattern)

URI patterns that we use to crawl.

### [EstimateDataSizeResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.EstimateDataSizeResponse)

Response of the EstimateDataSize request. If the long running operation was successful, then this message is returned by the google.longrunning.Operations.response field if the operation was successful.

### [Evaluation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Evaluation)

An evaluation is a single execution (or run) of an evaluation process. It encapsulates the state of the evaluation and the resulting data.

### [EvaluationSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Evaluation.EvaluationSpec)

Describes the specification of the evaluation.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [QuerySetSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Evaluation.EvaluationSpec.QuerySetSpec)

Describes the specification of the query set.

### [State](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Evaluation.State)

Describes the state of an evaluation.

### [FactChunk](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.FactChunk)

Fact Chunk.

### [SourceMetadataEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.FactChunk.SourceMetadataEntry)

The abstract base class for a message.

### [FetchDomainVerificationStatusRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.FetchDomainVerificationStatusRequest)

Request message for SiteSearchEngineService.FetchDomainVerificationStatus method.

### [FetchDomainVerificationStatusResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.FetchDomainVerificationStatusResponse)

Response message for SiteSearchEngineService.FetchDomainVerificationStatus method.

### [FhirStoreSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.FhirStoreSource)

Cloud FhirStore source import data from.

### [FieldConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.FieldConfig)

Configurations for fields of a schema. For example, configuring a field is indexable, or searchable.

### [AdvancedSiteSearchDataSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.FieldConfig.AdvancedSiteSearchDataSource)

Optional source of the advanced site search field.

### [CompletableOption](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.FieldConfig.CompletableOption)

The setting of Completable options in schema.

### [DynamicFacetableOption](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.FieldConfig.DynamicFacetableOption)

The status of the dynamic facetable option of a schema field.

### [FieldType](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.FieldConfig.FieldType)

Field value type in the Schema.
    
    
        - `id`: a string representing the location id
        - `longitude`: a number representing the longitude
          coordinate of the location
        - `latitude`: a number repesenting the latitude coordinate
          of the location
        - `address`: a string representing the full address of the
          location
    
        `latitude` and `longitude` must always be provided
        together. At least one of a) `address` or b)
        `latitude`-`longitude` pair must be provided.
    DATETIME (7):
        Field value type is Datetime. Datetime can be expressed as
        either:
    
        - a number representing milliseconds-since-the-epoch
        - a string representing milliseconds-since-the-epoch. e.g.
          `"1420070400001"`
        - a string representing the `ISO
          8601 <https://en.wikipedia.org/wiki/ISO_8601>`__ date or
          date and time. e.g. `"2015-01-01"` or
          `"2015-01-01T12:10:30Z"`
    

### [FilterableOption](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.FieldConfig.FilterableOption)

Sets the filterable option for schema fields.

### [IndexableOption](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.FieldConfig.IndexableOption)

The setting of Indexable options in schema.

### [RetrievableOption](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.FieldConfig.RetrievableOption)

The setting of Retrievable options in schema.

### [SearchableOption](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.FieldConfig.SearchableOption)

The setting of Searchable options in schema.

### [FileCharacteristics](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.FileCharacteristics)

Caracteristics of other file types.

### [CharacteristicsEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.FileCharacteristics.CharacteristicsEntry)

The abstract base class for a message.

### [FileMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.FileMetadata)

Represents a file attached to a session (context file)

### [MetadataEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.FileMetadata.MetadataEntry)

The abstract base class for a message.

### [ViewsEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.FileMetadata.ViewsEntry)

The abstract base class for a message.

### [FileOriginType](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.FileOriginType)

The origin of the file.

### [FileSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.FileSource)

Original source of the file.

### [FileView](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.FileView)

Represents a specific alternate version or "view" of a file object, such as a summary, a thumbnail, a translated version, etc.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [FirestoreSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.FirestoreSource)

Firestore source import data from.

### [GcsSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.GcsSource)

Cloud Storage location for input content.

### [GetAclConfigRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.GetAclConfigRequest)

Request message for GetAclConfigRequest method.

### [GetAnswerRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.GetAnswerRequest)

Request for GetAnswer method.

### [GetChunkRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.GetChunkRequest)

Request message for ChunkService.GetChunk method.

### [GetControlRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.GetControlRequest)

Request for GetControl method.

### [GetConversationRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.GetConversationRequest)

Request for GetConversation method.

### [GetDataStoreRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.GetDataStoreRequest)

Request message for DataStoreService.GetDataStore method.

### [GetDocumentProcessingConfigRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.GetDocumentProcessingConfigRequest)

Request for DataStoreService.GetDocumentProcessingConfig method.

### [GetDocumentRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.GetDocumentRequest)

Request message for DocumentService.GetDocument method.

### [GetEngineRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.GetEngineRequest)

Request message for EngineService.GetEngine method.

### [GetEvaluationRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.GetEvaluationRequest)

Request message for EvaluationService.GetEvaluation method.

### [GetProcessedDocumentRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.GetProcessedDocumentRequest)

Request message for DocumentService.GetDocument method.

### [ProcessedDocumentFormat](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.GetProcessedDocumentRequest.ProcessedDocumentFormat)

The format of the returned processed document. If unspecified, defaults to JSON.

### [ProcessedDocumentType](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.GetProcessedDocumentRequest.ProcessedDocumentType)

The type of processing to return in the response.

### [GetProjectRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.GetProjectRequest)

Request message for ProjectService.GetProject method.

### [GetSampleQueryRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.GetSampleQueryRequest)

Request message for SampleQueryService.GetSampleQuery method.

### [GetSampleQuerySetRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.GetSampleQuerySetRequest)

Request message for SampleQuerySetService.GetSampleQuerySet method.

### [GetSchemaRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.GetSchemaRequest)

Request message for SchemaService.GetSchema method.

### [GetServingConfigRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.GetServingConfigRequest)

Request for GetServingConfig method.

### [GetSessionRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.GetSessionRequest)

Request for GetSession method.

### [GetSiteSearchEngineRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.GetSiteSearchEngineRequest)

Request message for SiteSearchEngineService.GetSiteSearchEngine method.

### [GetTargetSiteRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.GetTargetSiteRequest)

Request message for SiteSearchEngineService.GetTargetSite method.

### [GetUriPatternDocumentDataRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.GetUriPatternDocumentDataRequest)

Request message for SiteSearchEngineService.GetUriPatternDocumentData method.

### [GetUriPatternDocumentDataResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.GetUriPatternDocumentDataResponse)

Response message for SiteSearchEngineService.GetUriPatternDocumentData method.

### [DocumentDataMapEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.GetUriPatternDocumentDataResponse.DocumentDataMapEntry)

The abstract base class for a message.

### [GroundingFact](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.GroundingFact)

Grounding Fact.

### [AttributesEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.GroundingFact.AttributesEntry)

The abstract base class for a message.

### [GuidedSearchSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.GuidedSearchSpec)

Defines guided search spec.

### [IdpConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.IdpConfig)

Identity Provider Config.

### [ExternalIdpConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.IdpConfig.ExternalIdpConfig)

Third party IDP Config.

### [IdpType](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.IdpConfig.IdpType)

Identity Provider Type.

### [ImageCharacteristics](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ImageCharacteristics)

Standard characteristics of an image media view.

### [ColorSpace](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ImageCharacteristics.ColorSpace)

Possible color spaces of an image (e.g., "RGB", "CMYK", "Grayscale").

### [ImportCompletionSuggestionsMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ImportCompletionSuggestionsMetadata)

Metadata related to the progress of the ImportCompletionSuggestions operation. This will be returned by the google.longrunning.Operation.metadata field.

### [ImportCompletionSuggestionsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ImportCompletionSuggestionsRequest)

Request message for CompletionService.ImportCompletionSuggestions method.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [InlineSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ImportCompletionSuggestionsRequest.InlineSource)

The inline source for CompletionSuggestions.

### [ImportCompletionSuggestionsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ImportCompletionSuggestionsResponse)

Response of the CompletionService.ImportCompletionSuggestions method. If the long running operation is done, this message is returned by the google.longrunning.Operations.response field if the operation is successful.

### [ImportDocumentsMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ImportDocumentsMetadata)

Metadata related to the progress of the ImportDocuments operation. This is returned by the google.longrunning.Operation.metadata field.

### [ImportDocumentsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ImportDocumentsRequest)

Request message for Import methods.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [InlineSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ImportDocumentsRequest.InlineSource)

The inline source for the input config for ImportDocuments method.

### [ReconciliationMode](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ImportDocumentsRequest.ReconciliationMode)

Indicates how imported documents are reconciled with the existing documents created or imported before.

### [ImportDocumentsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ImportDocumentsResponse)

Response of the ImportDocumentsRequest. If the long running operation is done, then this message is returned by the google.longrunning.Operations.response field if the operation was successful.

### [ImportErrorConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ImportErrorConfig)

Configuration of destination for Import related errors.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ImportSampleQueriesMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ImportSampleQueriesMetadata)

Metadata related to the progress of the ImportSampleQueries operation. This will be returned by the google.longrunning.Operation.metadata field.

### [ImportSampleQueriesRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ImportSampleQueriesRequest)

Request message for SampleQueryService.ImportSampleQueries method.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [InlineSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ImportSampleQueriesRequest.InlineSource)

The inline source for SampleQuerys.

### [ImportSampleQueriesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ImportSampleQueriesResponse)

Response of the SampleQueryService.ImportSampleQueries method. If the long running operation is done, this message is returned by the google.longrunning.Operations.response field if the operation is successful.

### [ImportSuggestionDenyListEntriesMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ImportSuggestionDenyListEntriesMetadata)

Metadata related to the progress of the ImportSuggestionDenyListEntries operation. This is returned by the google.longrunning.Operation.metadata field.

### [ImportSuggestionDenyListEntriesRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ImportSuggestionDenyListEntriesRequest)

Request message for CompletionService.ImportSuggestionDenyListEntries method.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [InlineSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ImportSuggestionDenyListEntriesRequest.InlineSource)

The inline source for SuggestionDenyListEntry.

### [ImportSuggestionDenyListEntriesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ImportSuggestionDenyListEntriesResponse)

Response message for CompletionService.ImportSuggestionDenyListEntries method.

### [ImportUserEventsMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ImportUserEventsMetadata)

Metadata related to the progress of the Import operation. This is returned by the google.longrunning.Operation.metadata field.

### [ImportUserEventsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ImportUserEventsRequest)

Request message for the ImportUserEvents request.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [InlineSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ImportUserEventsRequest.InlineSource)

The inline source for the input config for ImportUserEvents method.

### [ImportUserEventsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ImportUserEventsResponse)

Response of the ImportUserEventsRequest. If the long running operation was successful, then this message is returned by the google.longrunning.Operations.response field if the operation was successful.

### [IndustryVertical](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.IndustryVertical)

The industry vertical associated with the DataStore.

### [Interval](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Interval)

A floating point interval.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [LanguageInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.LanguageInfo)

Language info for DataStore.

### [ListChunksRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListChunksRequest)

Request message for ChunkService.ListChunks method.

### [ListChunksResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListChunksResponse)

Response message for ChunkService.ListChunks method.

### [ListControlsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListControlsRequest)

Request for ListControls method.

### [ListControlsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListControlsResponse)

Response for ListControls method.

### [ListConversationsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListConversationsRequest)

Request for ListConversations method.

### [ListConversationsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListConversationsResponse)

Response for ListConversations method.

### [ListCustomModelsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListCustomModelsRequest)

Request message for SearchTuningService.ListCustomModels method.

### [ListCustomModelsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListCustomModelsResponse)

Response message for SearchTuningService.ListCustomModels method.

### [ListDataStoresRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListDataStoresRequest)

Request message for DataStoreService.ListDataStores method.

### [ListDataStoresResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListDataStoresResponse)

Response message for DataStoreService.ListDataStores method.

### [ListDocumentsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListDocumentsRequest)

Request message for DocumentService.ListDocuments method.

### [ListDocumentsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListDocumentsResponse)

Response message for DocumentService.ListDocuments method.

### [ListEnginesRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListEnginesRequest)

Request message for EngineService.ListEngines method.

### [ListEnginesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListEnginesResponse)

Response message for EngineService.ListEngines method.

### [ListEvaluationResultsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListEvaluationResultsRequest)

Request message for EvaluationService.ListEvaluationResults method.

### [ListEvaluationResultsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListEvaluationResultsResponse)

Response message for EvaluationService.ListEvaluationResults method.

### [EvaluationResult](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListEvaluationResultsResponse.EvaluationResult)

Represents the results of an evaluation for a single SampleQuery.

### [ListEvaluationsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListEvaluationsRequest)

Request message for EvaluationService.ListEvaluations method.

### [ListEvaluationsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListEvaluationsResponse)

Response message for EvaluationService.ListEvaluations method.

### [ListFilesRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListFilesRequest)

Request message for SessionService.ListFiles method.

### [ListFilesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListFilesResponse)

Response message for SessionService.ListFiles method.

### [ListSampleQueriesRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListSampleQueriesRequest)

Request message for SampleQueryService.ListSampleQueries method.

### [ListSampleQueriesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListSampleQueriesResponse)

Response message for SampleQueryService.ListSampleQueries method.

### [ListSampleQuerySetsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListSampleQuerySetsRequest)

Request message for SampleQuerySetService.ListSampleQuerySets method.

### [ListSampleQuerySetsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListSampleQuerySetsResponse)

Response message for SampleQuerySetService.ListSampleQuerySets method.

### [ListSchemasRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListSchemasRequest)

Request message for SchemaService.ListSchemas method.

### [ListSchemasResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListSchemasResponse)

Response message for SchemaService.ListSchemas method.

### [ListServingConfigsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListServingConfigsRequest)

Request for ListServingConfigs method.

### [ListServingConfigsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListServingConfigsResponse)

Response for ListServingConfigs method.

### [ListSessionsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListSessionsRequest)

Request for ListSessions method.

### [ListSessionsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListSessionsResponse)

Response for ListSessions method.

### [ListTargetSitesRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListTargetSitesRequest)

Request message for SiteSearchEngineService.ListTargetSites method.

### [ListTargetSitesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListTargetSitesResponse)

Response message for SiteSearchEngineService.ListTargetSites method.

### [MediaInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.MediaInfo)

Media-specific user event information.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [PageInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.PageInfo)

Detailed page information.

### [PanelInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.PanelInfo)

Detailed panel information associated with a user event.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [PauseEngineRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.PauseEngineRequest)

Request for pausing training of an engine.

### [Principal](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Principal)

Principal identifier of a user or a group.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ProcessedDocument](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ProcessedDocument)

Document captures all raw metadata information of items to be recommended or searched.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Project](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Project)

Metadata and configurations for a Google Cloud project in the service.

### [ServiceTerms](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Project.ServiceTerms)

Metadata about the terms of service.

### [State](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Project.ServiceTerms.State)

The agreement states this terms of service.

### [ServiceTermsMapEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Project.ServiceTermsMapEntry)

The abstract base class for a message.

### [ProvisionProjectMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ProvisionProjectMetadata)

Metadata associated with a project provision operation.

### [ProvisionProjectRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ProvisionProjectRequest)

Request for ProjectService.ProvisionProject method.

### [PurgeCompletionSuggestionsMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.PurgeCompletionSuggestionsMetadata)

Metadata related to the progress of the PurgeCompletionSuggestions operation. This is returned by the google.longrunning.Operation.metadata field.

### [PurgeCompletionSuggestionsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.PurgeCompletionSuggestionsRequest)

Request message for CompletionService.PurgeCompletionSuggestions method.

### [PurgeCompletionSuggestionsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.PurgeCompletionSuggestionsResponse)

Response message for CompletionService.PurgeCompletionSuggestions method.

### [PurgeDocumentsMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.PurgeDocumentsMetadata)

Metadata related to the progress of the PurgeDocuments operation. This will be returned by the google.longrunning.Operation.metadata field.

### [PurgeDocumentsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.PurgeDocumentsRequest)

Request message for DocumentService.PurgeDocuments method.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [InlineSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.PurgeDocumentsRequest.InlineSource)

The inline source for the input config for DocumentService.PurgeDocuments method.

### [PurgeDocumentsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.PurgeDocumentsResponse)

Response message for DocumentService.PurgeDocuments method. If the long running operation is successfully done, then this message is returned by the google.longrunning.Operations.response field.

### [PurgeErrorConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.PurgeErrorConfig)

Configuration of destination for Purge related errors.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [PurgeSuggestionDenyListEntriesMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.PurgeSuggestionDenyListEntriesMetadata)

Metadata related to the progress of the PurgeSuggestionDenyListEntries operation. This is returned by the google.longrunning.Operation.metadata field.

### [PurgeSuggestionDenyListEntriesRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.PurgeSuggestionDenyListEntriesRequest)

Request message for CompletionService.PurgeSuggestionDenyListEntries method.

### [PurgeSuggestionDenyListEntriesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.PurgeSuggestionDenyListEntriesResponse)

Response message for CompletionService.PurgeSuggestionDenyListEntries method.

### [PurgeUserEventsMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.PurgeUserEventsMetadata)

Metadata related to the progress of the PurgeUserEvents operation. This will be returned by the google.longrunning.Operation.metadata field.

### [PurgeUserEventsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.PurgeUserEventsRequest)

Request message for PurgeUserEvents method.

### [PurgeUserEventsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.PurgeUserEventsResponse)

Response of the PurgeUserEventsRequest. If the long running operation is successfully done, then this message is returned by the google.longrunning.Operations.response field.

### [QualityMetrics](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.QualityMetrics)

Describes the metrics produced by the evaluation.

### [TopkMetrics](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.QualityMetrics.TopkMetrics)

Stores the metric values at specific top-k levels.

### [Query](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Query)

Defines a user inputed query.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [RankRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.RankRequest)

Request message for RankService.Rank method.

### [UserLabelsEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.RankRequest.UserLabelsEntry)

The abstract base class for a message.

### [RankResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.RankResponse)

Response message for RankService.Rank method.

### [RankingRecord](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.RankingRecord)

Record message for RankService.Rank method.

### [RecommendRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.RecommendRequest)

Request message for Recommend method.

### [ParamsEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.RecommendRequest.ParamsEntry)

The abstract base class for a message.

### [UserLabelsEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.RecommendRequest.UserLabelsEntry)

The abstract base class for a message.

### [RecommendResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.RecommendResponse)

Response message for Recommend method.

### [RecommendationResult](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.RecommendResponse.RecommendationResult)

RecommendationResult represents a generic recommendation result with associated metadata.

### [MetadataEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.RecommendResponse.RecommendationResult.MetadataEntry)

The abstract base class for a message.

### [RecrawlUrisMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.RecrawlUrisMetadata)

Metadata related to the progress of the SiteSearchEngineService.RecrawlUris operation. This will be returned by the google.longrunning.Operation.metadata field.

### [RecrawlUrisRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.RecrawlUrisRequest)

Request message for SiteSearchEngineService.RecrawlUris method.

### [RecrawlUrisResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.RecrawlUrisResponse)

Response message for SiteSearchEngineService.RecrawlUris method.

### [FailureInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.RecrawlUrisResponse.FailureInfo)

Details about why a particular URI failed to be crawled. Each FailureInfo contains one FailureReason per CorpusType.

### [FailureReason](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.RecrawlUrisResponse.FailureInfo.FailureReason)

Details about why crawling failed for a particular CorpusType, e.g., DESKTOP and MOBILE crawling may fail for different reasons.

### [CorpusType](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.RecrawlUrisResponse.FailureInfo.FailureReason.CorpusType)

CorpusType for the failed crawling operation.

### [Reply](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Reply)

Defines a reply message to user.

### [Reference](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Reply.Reference)

Defines reference in reply.

### [ReportConsentChangeRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ReportConsentChangeRequest)

Request for ReportConsentChange method.

### [ConsentChangeAction](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ReportConsentChangeRequest.ConsentChangeAction)

Type of consent acknowledgement (accept / reject).

At this moment, only `ACCEPT` action is supported.

### [ResumeEngineRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ResumeEngineRequest)

Request for resuming training of an engine.

### [SampleQuery](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SampleQuery)

Sample Query captures metadata to be used for evaluation.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [QueryEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SampleQuery.QueryEntry)

Query Entry captures metadata to be used for search evaluation.

### [Target](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SampleQuery.QueryEntry.Target)

Defines the parameters of the query's expected outcome.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [SampleQuerySet](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SampleQuerySet)

A SampleQuerySet is the parent resource of SampleQuery, and contains the configurations shared by all SampleQuery under it.

### [Schema](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Schema)

Defines the structure and layout of a type of document data.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [SearchAddOn](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchAddOn)

Add-on that provides additional functionality for search.

### [SearchInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchInfo)

Detailed search information.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [SearchRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchRequest)

Request message for SearchService.Search method.

### [BoostSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchRequest.BoostSpec)

Boost specification to boost certain documents.

### [ConditionBoostSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchRequest.BoostSpec.ConditionBoostSpec)

Boost applies to documents which match a condition.

### [BoostControlSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchRequest.BoostSpec.ConditionBoostSpec.BoostControlSpec)

Specification for custom ranking based on customer specified attribute value. It provides more controls for customized ranking than the simple (condition, boost) combination above.

### [AttributeType](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchRequest.BoostSpec.ConditionBoostSpec.BoostControlSpec.AttributeType)

The attribute(or function) for which the custom ranking is to be applied.

### [ControlPoint](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchRequest.BoostSpec.ConditionBoostSpec.BoostControlSpec.ControlPoint)

The control points used to define the curve. The curve defined through these control points can only be monotonically increasing or decreasing(constant values are acceptable).

### [InterpolationType](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchRequest.BoostSpec.ConditionBoostSpec.BoostControlSpec.InterpolationType)

The interpolation type to be applied. Default will be linear (Piecewise Linear).

### [ContentSearchSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchRequest.ContentSearchSpec)

A specification for configuring the behavior of content search.

### [ChunkSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchRequest.ContentSearchSpec.ChunkSpec)

Specifies the chunk spec to be returned from the search response. Only available if the SearchRequest.ContentSearchSpec.search_result_mode is set to CHUNKS

### [ExtractiveContentSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchRequest.ContentSearchSpec.ExtractiveContentSpec)

A specification for configuring the extractive content in a search response.

### [SearchResultMode](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchRequest.ContentSearchSpec.SearchResultMode)

Specifies the search result mode. If unspecified, the search result mode defaults to `DOCUMENTS`.

### [SnippetSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchRequest.ContentSearchSpec.SnippetSpec)

A specification for configuring snippets in a search response.

### [SummarySpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchRequest.ContentSearchSpec.SummarySpec)

A specification for configuring a summary returned in a search response.

### [ModelPromptSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchRequest.ContentSearchSpec.SummarySpec.ModelPromptSpec)

Specification of the prompt to use with the model.

### [ModelSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchRequest.ContentSearchSpec.SummarySpec.ModelSpec)

Specification of the model.

### [DataStoreSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchRequest.DataStoreSpec)

A struct to define data stores to filter on in a search call and configurations for those data stores. Otherwise, an `INVALID_ARGUMENT` error is returned.

### [EmbeddingSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchRequest.EmbeddingSpec)

The specification that uses customized query embedding vector to do semantic document retrieval.

### [EmbeddingVector](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchRequest.EmbeddingSpec.EmbeddingVector)

Embedding vector.

### [FacetSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchRequest.FacetSpec)

A facet specification to perform faceted search.

### [FacetKey](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchRequest.FacetSpec.FacetKey)

Specifies how a facet is computed.

### [ImageQuery](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchRequest.ImageQuery)

Specifies the image query input.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [NaturalLanguageQueryUnderstandingSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchRequest.NaturalLanguageQueryUnderstandingSpec)

Specification to enable natural language understanding capabilities for search requests.

### [FilterExtractionCondition](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchRequest.NaturalLanguageQueryUnderstandingSpec.FilterExtractionCondition)

Enum describing under which condition filter extraction should occur.

### [ParamsEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchRequest.ParamsEntry)

The abstract base class for a message.

### [QueryExpansionSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchRequest.QueryExpansionSpec)

Specification to determine under which conditions query expansion should occur.

### [Condition](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchRequest.QueryExpansionSpec.Condition)

Enum describing under which condition query expansion should occur.

### [RankingExpressionBackend](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchRequest.RankingExpressionBackend)

The backend to use for the ranking expression evaluation.

### [RelevanceThreshold](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchRequest.RelevanceThreshold)

The relevance threshold of the search results. The higher relevance threshold is, the higher relevant results are shown and the less number of results are returned.

### [SearchAsYouTypeSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchRequest.SearchAsYouTypeSpec)

Specification for search as you type in search requests.

### [Condition](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchRequest.SearchAsYouTypeSpec.Condition)

Enum describing under which condition search as you type should occur.

### [SessionSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchRequest.SessionSpec)

Session specification.

Multi-turn Search feature is currently at private GA stage. Please use v1alpha or v1beta version instead before we launch this feature to public GA. Or ask for allowlisting through Google Support team.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [SpellCorrectionSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchRequest.SpellCorrectionSpec)

The specification for query spell correction.

### [Mode](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchRequest.SpellCorrectionSpec.Mode)

Enum describing under which mode spell correction should occur.

### [UserLabelsEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchRequest.UserLabelsEntry)

The abstract base class for a message.

### [SearchResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchResponse)

Response message for SearchService.Search method.

### [Facet](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchResponse.Facet)

A facet result.

### [FacetValue](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchResponse.Facet.FacetValue)

A facet value which contains value names and their count.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [GeoSearchDebugInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchResponse.GeoSearchDebugInfo)

Debug information specifically related to forward geocoding issues arising from Geolocation Search.

### [GuidedSearchResult](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchResponse.GuidedSearchResult)

Guided search result. The guided search helps user to refine the search results and narrow down to the real needs from a broaded search results.

### [RefinementAttribute](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchResponse.GuidedSearchResult.RefinementAttribute)

Useful attribute for search result refinements.

### [NaturalLanguageQueryUnderstandingInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchResponse.NaturalLanguageQueryUnderstandingInfo)

Information describing what natural language understanding was done on the input query.

### [StructuredExtractedFilter](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchResponse.NaturalLanguageQueryUnderstandingInfo.StructuredExtractedFilter)

The filters that were extracted from the input query represented in a structured form.

### [AndExpression](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchResponse.NaturalLanguageQueryUnderstandingInfo.StructuredExtractedFilter.AndExpression)

Logical `And` operator.

### [Expression](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchResponse.NaturalLanguageQueryUnderstandingInfo.StructuredExtractedFilter.Expression)

The expression denoting the filter that was extracted from the input query.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [GeolocationConstraint](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchResponse.NaturalLanguageQueryUnderstandingInfo.StructuredExtractedFilter.GeolocationConstraint)

Constraint of a geolocation field. Name of the geolocation field as defined in the schema.

### [NumberConstraint](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchResponse.NaturalLanguageQueryUnderstandingInfo.StructuredExtractedFilter.NumberConstraint)

Constraint expression of a number field. Example: price < 100.

### [Comparison](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchResponse.NaturalLanguageQueryUnderstandingInfo.StructuredExtractedFilter.NumberConstraint.Comparison)

The comparison operation that was performed.

### [OrExpression](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchResponse.NaturalLanguageQueryUnderstandingInfo.StructuredExtractedFilter.OrExpression)

Logical `Or` operator.

### [StringConstraint](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchResponse.NaturalLanguageQueryUnderstandingInfo.StructuredExtractedFilter.StringConstraint)

Constraint expression of a string field.

### [OneBoxResult](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchResponse.OneBoxResult)

OneBoxResult is a holder for all results of specific type that we want to display in UI differently.

### [OneBoxType](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchResponse.OneBoxResult.OneBoxType)

The type of One Box result.

### [QueryExpansionInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchResponse.QueryExpansionInfo)

Information describing query expansion including whether expansion has occurred.

### [SearchResult](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchResponse.SearchResult)

Represents the search results.

### [ModelScoresEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchResponse.SearchResult.ModelScoresEntry)

The abstract base class for a message.

### [RankSignals](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchResponse.SearchResult.RankSignals)

A set of ranking signals.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [CustomSignal](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchResponse.SearchResult.RankSignals.CustomSignal)

Custom clearbox signal represented by name and value pair.

### [SessionInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchResponse.SessionInfo)

Information about the session.

### [Summary](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchResponse.Summary)

Summary of the top N search results specified by the summary spec.

### [Citation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchResponse.Summary.Citation)

Citation info for a segment.

### [CitationMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchResponse.Summary.CitationMetadata)

Citation metadata.

### [CitationSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchResponse.Summary.CitationSource)

Citation source.

### [Reference](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchResponse.Summary.Reference)

Document reference.

### [ChunkContent](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchResponse.Summary.Reference.ChunkContent)

Chunk content.

### [SafetyAttributes](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchResponse.Summary.SafetyAttributes)

Safety Attribute categories and their associated confidence scores.

### [SummarySkippedReason](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchResponse.Summary.SummarySkippedReason)

An Enum for summary-skipped reasons.
    
    
        Only used when
        <xref uid="google.cloud.discoveryengine.v1alpha.SearchRequest.ContentSearchSpec.SummarySpec.ignore_adversarial_query">SummarySpec.ignore_adversarial_query</xref>
        is set to `true`.
    NON_SUMMARY_SEEKING_QUERY_IGNORED (2):
        The non-summary seeking query ignored case.
    
        Only used when
        <xref uid="google.cloud.discoveryengine.v1alpha.SearchRequest.ContentSearchSpec.SummarySpec.ignore_non_summary_seeking_query">SummarySpec.ignore_non_summary_seeking_query</xref>
        is set to `true`.
    OUT_OF_DOMAIN_QUERY_IGNORED (3):
        The out-of-domain query ignored case.
    
        Google skips the summary if there are no
        high-relevance search results. For example, the
        data store contains facts about company A but
        the user query is asking questions about company
        B.
    POTENTIAL_POLICY_VIOLATION (4):
        The potential policy violation case.
    
        Google skips the summary if there is a potential
        policy violation detected. This includes content
        that may be violent or toxic.
    LLM_ADDON_NOT_ENABLED (5):
        The LLM addon not enabled case.
    
        Google skips the summary if the LLM addon is not
        enabled.
    NO_RELEVANT_CONTENT (6):
        The no relevant content case.
    
        Google skips the summary if there is no relevant
        content in the retrieved search results.
    JAIL_BREAKING_QUERY_IGNORED (7):
        The jail-breaking query ignored case.
    
        For example, "Reply in the tone of a competing company's
        CEO". Only used when
        [SearchRequest.ContentSearchSpec.SummarySpec.ignore_jail_breaking_query]
        is set to `true`.
    CUSTOMER_POLICY_VIOLATION (8):
        The customer policy violation case.
    
        Google skips the summary if there is a customer
        policy violation detected. The policy is defined
        by the customer.
    NON_SUMMARY_SEEKING_QUERY_IGNORED_V2 (9):
        The non-answer seeking query ignored case.
    
        Only used when
        [SearchRequest.ContentSearchSpec.SummarySpec.ignore_non_answer_seeking_query]
        is set to `true`.
    

### [SummaryWithMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchResponse.Summary.SummaryWithMetadata)

Summary with metadata information.

### [SearchTier](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchTier)

Tiers of search features. Different tiers might have different pricing. To learn more, check the pricing documentation.

### [SearchUseCase](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SearchUseCase)

Defines a further subdivision of `SolutionType`. Specifically applies to SOLUTION_TYPE_SEARCH.

### [ServingConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ServingConfig)

Configures metadata that is used to generate serving time results (e.g. search results or recommendation predictions). The ServingConfig is passed in the search and predict request and generates results.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [GenericConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ServingConfig.GenericConfig)

Specifies the configurations needed for Generic Discovery.Currently we support:

  * `content_search_spec`: configuration for generic content search.



### [MediaConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ServingConfig.MediaConfig)

Specifies the configurations needed for Media Discovery. Currently we support:

  * `demote_content_watched`: Threshold for watched content demotion. Customers can specify if using watched content demotion or use viewed detail page. Using the content watched demotion, customers need to specify the watched minutes or percentage exceeds the threshold, the content will be demoted in the recommendation result.
  * `promote_fresh_content`: cutoff days for fresh content promotion. Customers can specify if using content freshness promotion. If the content was published within the cutoff days, the content will be promoted in the recommendation result. Can only be set if SolutionType is SOLUTION_TYPE_RECOMMENDATION.



This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Session](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Session)

External session proto definition.

### [State](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Session.State)

Enumeration of the state of the session.

### [Turn](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Session.Turn)

Represents a turn, including a query from the user and a answer from service.

### [QueryConfigEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.Session.Turn.QueryConfigEntry)

The abstract base class for a message.

### [SetUriPatternDocumentDataMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SetUriPatternDocumentDataMetadata)

Metadata related to the progress of the SiteSearchEngineService.SetUriPatternDocumentData operation. This will be returned by the google.longrunning.Operation.metadata field.

### [SetUriPatternDocumentDataRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SetUriPatternDocumentDataRequest)

Request message for SiteSearchEngineService.SetUriPatternDocumentData method.

### [DocumentDataMapEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SetUriPatternDocumentDataRequest.DocumentDataMapEntry)

The abstract base class for a message.

### [SetUriPatternDocumentDataResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SetUriPatternDocumentDataResponse)

Response message for SiteSearchEngineService.SetUriPatternDocumentData method.

### [SiteSearchEngine](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SiteSearchEngine)

SiteSearchEngine captures DataStore level site search persisting configurations. It is a singleton value per data store.

### [SiteVerificationInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SiteVerificationInfo)

Verification information for target sites in advanced site search.

### [SiteVerificationState](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SiteVerificationInfo.SiteVerificationState)

Site verification state.

### [SolutionType](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SolutionType)

The type of solution.

### [SpannerSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SpannerSource)

The Spanner source for importing data

### [SuggestionDenyListEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SuggestionDenyListEntry)

Suggestion deny list entry identifying the phrase to block from suggestions and the applied operation for the phrase.

### [MatchOperator](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.SuggestionDenyListEntry.MatchOperator)

Operator for matching with the generated suggestions.

### [TargetSite](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.TargetSite)

A target site for the SiteSearchEngine.

### [FailureReason](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.TargetSite.FailureReason)

Site search indexing failure reasons.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [QuotaFailure](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.TargetSite.FailureReason.QuotaFailure)

Failed due to insufficient quota.

### [IndexingStatus](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.TargetSite.IndexingStatus)

Target site indexing status enumeration.
    
    
        1. target site deleted if unindexing is
            successful;
        2. state reverts to SUCCEEDED if the unindexing
            fails.
    

### [Type](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.TargetSite.Type)

Possible target site types.

### [TextInput](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.TextInput)

Defines text input.

### [TrainCustomModelMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.TrainCustomModelMetadata)

Metadata related to the progress of the TrainCustomModel operation. This is returned by the google.longrunning.Operation.metadata field.

### [TrainCustomModelRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.TrainCustomModelRequest)

Request message for SearchTuningService.TrainCustomModel method.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [GcsTrainingInput](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.TrainCustomModelRequest.GcsTrainingInput)

Cloud Storage training data input.

### [TrainCustomModelResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.TrainCustomModelResponse)

Response of the TrainCustomModelRequest. This message is returned by the google.longrunning.Operations.response field.

### [MetricsEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.TrainCustomModelResponse.MetricsEntry)

The abstract base class for a message.

### [TransactionInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.TransactionInfo)

A transaction represents the entire purchase transaction.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [TuneEngineMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.TuneEngineMetadata)

Metadata associated with a tune operation.

### [TuneEngineRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.TuneEngineRequest)

Request to manually start a tuning process now (instead of waiting for the periodically scheduled tuning to happen).

### [TuneEngineResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.TuneEngineResponse)

Response associated with a tune operation.

### [UpdateAclConfigRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.UpdateAclConfigRequest)

Request message for UpdateAclConfig method.

### [UpdateControlRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.UpdateControlRequest)

Request for UpdateControl method.

### [UpdateConversationRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.UpdateConversationRequest)

Request for UpdateConversation method.

### [UpdateDataStoreRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.UpdateDataStoreRequest)

Request message for DataStoreService.UpdateDataStore method.

### [UpdateDocumentProcessingConfigRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.UpdateDocumentProcessingConfigRequest)

Request for DataStoreService.UpdateDocumentProcessingConfig method.

### [UpdateDocumentRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.UpdateDocumentRequest)

Request message for DocumentService.UpdateDocument method.

### [UpdateEngineRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.UpdateEngineRequest)

Request message for EngineService.UpdateEngine method.

### [UpdateSampleQueryRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.UpdateSampleQueryRequest)

Request message for SampleQueryService.UpdateSampleQuery method.

### [UpdateSampleQuerySetRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.UpdateSampleQuerySetRequest)

Request message for SampleQuerySetService.UpdateSampleQuerySet method.

### [UpdateSchemaMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.UpdateSchemaMetadata)

Metadata for UpdateSchema LRO.

### [UpdateSchemaRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.UpdateSchemaRequest)

Request message for SchemaService.UpdateSchema method.

### [UpdateServingConfigRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.UpdateServingConfigRequest)

Request for UpdateServingConfig method.

### [UpdateSessionRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.UpdateSessionRequest)

Request for UpdateSession method.

### [UpdateTargetSiteMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.UpdateTargetSiteMetadata)

Metadata related to the progress of the SiteSearchEngineService.UpdateTargetSite operation. This will be returned by the google.longrunning.Operation.metadata field.

### [UpdateTargetSiteRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.UpdateTargetSiteRequest)

Request message for SiteSearchEngineService.UpdateTargetSite method.

### [UserEvent](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.UserEvent)

UserEvent captures all metadata information Discovery Engine API needs to know about how end users interact with your website.

### [AttributesEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.UserEvent.AttributesEntry)

The abstract base class for a message.

### [UserInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.UserInfo)

Information of an end user.

### [VideoCharacteristics](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.VideoCharacteristics)

Standard characteristics of a video media view.

### [WorkspaceConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.WorkspaceConfig)

Config to store data store type configuration for workspace data

### [Type](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.WorkspaceConfig.Type)

Specifies the type of Workspace App supported by this DataStore

### [WriteUserEventRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.WriteUserEventRequest)

Request message for WriteUserEvent method.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AclConfigServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.acl_config_service.AclConfigServiceAsyncClient)

Service for managing Acl Configuration.

### [AclConfigServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.acl_config_service.AclConfigServiceClient)

Service for managing Acl Configuration.

### [AssistantServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.assistant_service.AssistantServiceAsyncClient)

Service for managing Assistant configuration and assisting users.

### [AssistantServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.assistant_service.AssistantServiceClient)

Service for managing Assistant configuration and assisting users.

### [ListAssistantsAsyncPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.assistant_service.pagers.ListAssistantsAsyncPager)

A pager for iterating through `list_assistants` requests.

This class thinly wraps an initial [ListAssistantsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListAssistantsResponse) object, and provides an `__aiter__` method to iterate through its `assistants` field.

If there are more pages, the `__aiter__` method will make additional `ListAssistants` requests and continue to iterate through the `assistants` field on the corresponding responses.

All the usual [ListAssistantsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListAssistantsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListAssistantsPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.assistant_service.pagers.ListAssistantsPager)

A pager for iterating through `list_assistants` requests.

This class thinly wraps an initial [ListAssistantsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListAssistantsResponse) object, and provides an `__iter__` method to iterate through its `assistants` field.

If there are more pages, the `__iter__` method will make additional `ListAssistants` requests and continue to iterate through the `assistants` field on the corresponding responses.

All the usual [ListAssistantsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListAssistantsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [CmekConfigServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.cmek_config_service.CmekConfigServiceAsyncClient)

Service for managing CMEK related tasks

### [CmekConfigServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.cmek_config_service.CmekConfigServiceClient)

Service for managing CMEK related tasks

### [CompletionServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.completion_service.CompletionServiceAsyncClient)

Service for Auto-Completion.

### [CompletionServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.completion_service.CompletionServiceClient)

Service for Auto-Completion.

### [ControlServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.control_service.ControlServiceAsyncClient)

Service for performing CRUD operations on Controls. Controls allow for custom logic to be implemented in the serving path. Controls need to be attached to a Serving Config to be considered during a request.

### [ControlServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.control_service.ControlServiceClient)

Service for performing CRUD operations on Controls. Controls allow for custom logic to be implemented in the serving path. Controls need to be attached to a Serving Config to be considered during a request.

### [ListControlsAsyncPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.control_service.pagers.ListControlsAsyncPager)

A pager for iterating through `list_controls` requests.

This class thinly wraps an initial [ListControlsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListControlsResponse) object, and provides an `__aiter__` method to iterate through its `controls` field.

If there are more pages, the `__aiter__` method will make additional `ListControls` requests and continue to iterate through the `controls` field on the corresponding responses.

All the usual [ListControlsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListControlsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListControlsPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.control_service.pagers.ListControlsPager)

A pager for iterating through `list_controls` requests.

This class thinly wraps an initial [ListControlsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListControlsResponse) object, and provides an `__iter__` method to iterate through its `controls` field.

If there are more pages, the `__iter__` method will make additional `ListControls` requests and continue to iterate through the `controls` field on the corresponding responses.

All the usual [ListControlsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListControlsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ConversationalSearchServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.conversational_search_service.ConversationalSearchServiceAsyncClient)

Service for conversational search.

### [ConversationalSearchServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.conversational_search_service.ConversationalSearchServiceClient)

Service for conversational search.

### [ListConversationsAsyncPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.conversational_search_service.pagers.ListConversationsAsyncPager)

A pager for iterating through `list_conversations` requests.

This class thinly wraps an initial [ListConversationsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListConversationsResponse) object, and provides an `__aiter__` method to iterate through its `conversations` field.

If there are more pages, the `__aiter__` method will make additional `ListConversations` requests and continue to iterate through the `conversations` field on the corresponding responses.

All the usual [ListConversationsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListConversationsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListConversationsPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.conversational_search_service.pagers.ListConversationsPager)

A pager for iterating through `list_conversations` requests.

This class thinly wraps an initial [ListConversationsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListConversationsResponse) object, and provides an `__iter__` method to iterate through its `conversations` field.

If there are more pages, the `__iter__` method will make additional `ListConversations` requests and continue to iterate through the `conversations` field on the corresponding responses.

All the usual [ListConversationsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListConversationsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListSessionsAsyncPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.conversational_search_service.pagers.ListSessionsAsyncPager)

A pager for iterating through `list_sessions` requests.

This class thinly wraps an initial [ListSessionsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListSessionsResponse) object, and provides an `__aiter__` method to iterate through its `sessions` field.

If there are more pages, the `__aiter__` method will make additional `ListSessions` requests and continue to iterate through the `sessions` field on the corresponding responses.

All the usual [ListSessionsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListSessionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListSessionsPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.conversational_search_service.pagers.ListSessionsPager)

A pager for iterating through `list_sessions` requests.

This class thinly wraps an initial [ListSessionsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListSessionsResponse) object, and provides an `__iter__` method to iterate through its `sessions` field.

If there are more pages, the `__iter__` method will make additional `ListSessions` requests and continue to iterate through the `sessions` field on the corresponding responses.

All the usual [ListSessionsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListSessionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [DataStoreServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.data_store_service.DataStoreServiceAsyncClient)

Service for managing DataStore configuration.

### [DataStoreServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.data_store_service.DataStoreServiceClient)

Service for managing DataStore configuration.

### [ListDataStoresAsyncPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.data_store_service.pagers.ListDataStoresAsyncPager)

A pager for iterating through `list_data_stores` requests.

This class thinly wraps an initial [ListDataStoresResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListDataStoresResponse) object, and provides an `__aiter__` method to iterate through its `data_stores` field.

If there are more pages, the `__aiter__` method will make additional `ListDataStores` requests and continue to iterate through the `data_stores` field on the corresponding responses.

All the usual [ListDataStoresResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListDataStoresResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListDataStoresPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.data_store_service.pagers.ListDataStoresPager)

A pager for iterating through `list_data_stores` requests.

This class thinly wraps an initial [ListDataStoresResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListDataStoresResponse) object, and provides an `__iter__` method to iterate through its `data_stores` field.

If there are more pages, the `__iter__` method will make additional `ListDataStores` requests and continue to iterate through the `data_stores` field on the corresponding responses.

All the usual [ListDataStoresResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListDataStoresResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [DocumentServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.document_service.DocumentServiceAsyncClient)

Service for ingesting Document information of the customer's website.

### [DocumentServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.document_service.DocumentServiceClient)

Service for ingesting Document information of the customer's website.

### [ListDocumentsAsyncPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.document_service.pagers.ListDocumentsAsyncPager)

A pager for iterating through `list_documents` requests.

This class thinly wraps an initial [ListDocumentsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListDocumentsResponse) object, and provides an `__aiter__` method to iterate through its `documents` field.

If there are more pages, the `__aiter__` method will make additional `ListDocuments` requests and continue to iterate through the `documents` field on the corresponding responses.

All the usual [ListDocumentsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListDocumentsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListDocumentsPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.document_service.pagers.ListDocumentsPager)

A pager for iterating through `list_documents` requests.

This class thinly wraps an initial [ListDocumentsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListDocumentsResponse) object, and provides an `__iter__` method to iterate through its `documents` field.

If there are more pages, the `__iter__` method will make additional `ListDocuments` requests and continue to iterate through the `documents` field on the corresponding responses.

All the usual [ListDocumentsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListDocumentsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [EngineServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.engine_service.EngineServiceAsyncClient)

Service for managing Engine configuration.

### [EngineServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.engine_service.EngineServiceClient)

Service for managing Engine configuration.

### [ListEnginesAsyncPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.engine_service.pagers.ListEnginesAsyncPager)

A pager for iterating through `list_engines` requests.

This class thinly wraps an initial [ListEnginesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListEnginesResponse) object, and provides an `__aiter__` method to iterate through its `engines` field.

If there are more pages, the `__aiter__` method will make additional `ListEngines` requests and continue to iterate through the `engines` field on the corresponding responses.

All the usual [ListEnginesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListEnginesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListEnginesPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.engine_service.pagers.ListEnginesPager)

A pager for iterating through `list_engines` requests.

This class thinly wraps an initial [ListEnginesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListEnginesResponse) object, and provides an `__iter__` method to iterate through its `engines` field.

If there are more pages, the `__iter__` method will make additional `ListEngines` requests and continue to iterate through the `engines` field on the corresponding responses.

All the usual [ListEnginesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListEnginesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [EvaluationServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.evaluation_service.EvaluationServiceAsyncClient)

Service for managing Evaluations,

### [EvaluationServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.evaluation_service.EvaluationServiceClient)

Service for managing Evaluations,

### [ListEvaluationResultsAsyncPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.evaluation_service.pagers.ListEvaluationResultsAsyncPager)

A pager for iterating through `list_evaluation_results` requests.

This class thinly wraps an initial [ListEvaluationResultsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListEvaluationResultsResponse) object, and provides an `__aiter__` method to iterate through its `evaluation_results` field.

If there are more pages, the `__aiter__` method will make additional `ListEvaluationResults` requests and continue to iterate through the `evaluation_results` field on the corresponding responses.

All the usual [ListEvaluationResultsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListEvaluationResultsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListEvaluationResultsPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.evaluation_service.pagers.ListEvaluationResultsPager)

A pager for iterating through `list_evaluation_results` requests.

This class thinly wraps an initial [ListEvaluationResultsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListEvaluationResultsResponse) object, and provides an `__iter__` method to iterate through its `evaluation_results` field.

If there are more pages, the `__iter__` method will make additional `ListEvaluationResults` requests and continue to iterate through the `evaluation_results` field on the corresponding responses.

All the usual [ListEvaluationResultsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListEvaluationResultsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListEvaluationsAsyncPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.evaluation_service.pagers.ListEvaluationsAsyncPager)

A pager for iterating through `list_evaluations` requests.

This class thinly wraps an initial [ListEvaluationsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListEvaluationsResponse) object, and provides an `__aiter__` method to iterate through its `evaluations` field.

If there are more pages, the `__aiter__` method will make additional `ListEvaluations` requests and continue to iterate through the `evaluations` field on the corresponding responses.

All the usual [ListEvaluationsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListEvaluationsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListEvaluationsPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.evaluation_service.pagers.ListEvaluationsPager)

A pager for iterating through `list_evaluations` requests.

This class thinly wraps an initial [ListEvaluationsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListEvaluationsResponse) object, and provides an `__iter__` method to iterate through its `evaluations` field.

If there are more pages, the `__iter__` method will make additional `ListEvaluations` requests and continue to iterate through the `evaluations` field on the corresponding responses.

All the usual [ListEvaluationsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListEvaluationsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [GroundedGenerationServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.grounded_generation_service.GroundedGenerationServiceAsyncClient)

Service for grounded generation.

### [GroundedGenerationServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.grounded_generation_service.GroundedGenerationServiceClient)

Service for grounded generation.

### [IdentityMappingStoreServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.identity_mapping_store_service.IdentityMappingStoreServiceAsyncClient)

Service for managing Identity Mapping Stores.

### [IdentityMappingStoreServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.identity_mapping_store_service.IdentityMappingStoreServiceClient)

Service for managing Identity Mapping Stores.

### [ListIdentityMappingStoresAsyncPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.identity_mapping_store_service.pagers.ListIdentityMappingStoresAsyncPager)

A pager for iterating through `list_identity_mapping_stores` requests.

This class thinly wraps an initial [ListIdentityMappingStoresResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListIdentityMappingStoresResponse) object, and provides an `__aiter__` method to iterate through its `identity_mapping_stores` field.

If there are more pages, the `__aiter__` method will make additional `ListIdentityMappingStores` requests and continue to iterate through the `identity_mapping_stores` field on the corresponding responses.

All the usual [ListIdentityMappingStoresResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListIdentityMappingStoresResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListIdentityMappingStoresPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.identity_mapping_store_service.pagers.ListIdentityMappingStoresPager)

A pager for iterating through `list_identity_mapping_stores` requests.

This class thinly wraps an initial [ListIdentityMappingStoresResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListIdentityMappingStoresResponse) object, and provides an `__iter__` method to iterate through its `identity_mapping_stores` field.

If there are more pages, the `__iter__` method will make additional `ListIdentityMappingStores` requests and continue to iterate through the `identity_mapping_stores` field on the corresponding responses.

All the usual [ListIdentityMappingStoresResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListIdentityMappingStoresResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListIdentityMappingsAsyncPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.identity_mapping_store_service.pagers.ListIdentityMappingsAsyncPager)

A pager for iterating through `list_identity_mappings` requests.

This class thinly wraps an initial [ListIdentityMappingsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListIdentityMappingsResponse) object, and provides an `__aiter__` method to iterate through its `identity_mapping_entries` field.

If there are more pages, the `__aiter__` method will make additional `ListIdentityMappings` requests and continue to iterate through the `identity_mapping_entries` field on the corresponding responses.

All the usual [ListIdentityMappingsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListIdentityMappingsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListIdentityMappingsPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.identity_mapping_store_service.pagers.ListIdentityMappingsPager)

A pager for iterating through `list_identity_mappings` requests.

This class thinly wraps an initial [ListIdentityMappingsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListIdentityMappingsResponse) object, and provides an `__iter__` method to iterate through its `identity_mapping_entries` field.

If there are more pages, the `__iter__` method will make additional `ListIdentityMappings` requests and continue to iterate through the `identity_mapping_entries` field on the corresponding responses.

All the usual [ListIdentityMappingsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListIdentityMappingsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [LicenseConfigServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.license_config_service.LicenseConfigServiceAsyncClient)

Service for managing license config related resources.

### [LicenseConfigServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.license_config_service.LicenseConfigServiceClient)

Service for managing license config related resources.

### [ListLicenseConfigsAsyncPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.license_config_service.pagers.ListLicenseConfigsAsyncPager)

A pager for iterating through `list_license_configs` requests.

This class thinly wraps an initial [ListLicenseConfigsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListLicenseConfigsResponse) object, and provides an `__aiter__` method to iterate through its `license_configs` field.

If there are more pages, the `__aiter__` method will make additional `ListLicenseConfigs` requests and continue to iterate through the `license_configs` field on the corresponding responses.

All the usual [ListLicenseConfigsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListLicenseConfigsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListLicenseConfigsPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.license_config_service.pagers.ListLicenseConfigsPager)

A pager for iterating through `list_license_configs` requests.

This class thinly wraps an initial [ListLicenseConfigsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListLicenseConfigsResponse) object, and provides an `__iter__` method to iterate through its `license_configs` field.

If there are more pages, the `__iter__` method will make additional `ListLicenseConfigs` requests and continue to iterate through the `license_configs` field on the corresponding responses.

All the usual [ListLicenseConfigsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListLicenseConfigsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ProjectServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.project_service.ProjectServiceAsyncClient)

Service for operations on the Project.

### [ProjectServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.project_service.ProjectServiceClient)

Service for operations on the Project.

### [RankServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.rank_service.RankServiceAsyncClient)

Service for ranking text records.

### [RankServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.rank_service.RankServiceClient)

Service for ranking text records.

### [RecommendationServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.recommendation_service.RecommendationServiceAsyncClient)

Service for making recommendations.

### [RecommendationServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.recommendation_service.RecommendationServiceClient)

Service for making recommendations.

### [SampleQueryServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.sample_query_service.SampleQueryServiceAsyncClient)

Service for managing SampleQuerys,

### [SampleQueryServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.sample_query_service.SampleQueryServiceClient)

Service for managing SampleQuerys,

### [ListSampleQueriesAsyncPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.sample_query_service.pagers.ListSampleQueriesAsyncPager)

A pager for iterating through `list_sample_queries` requests.

This class thinly wraps an initial [ListSampleQueriesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListSampleQueriesResponse) object, and provides an `__aiter__` method to iterate through its `sample_queries` field.

If there are more pages, the `__aiter__` method will make additional `ListSampleQueries` requests and continue to iterate through the `sample_queries` field on the corresponding responses.

All the usual [ListSampleQueriesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListSampleQueriesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListSampleQueriesPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.sample_query_service.pagers.ListSampleQueriesPager)

A pager for iterating through `list_sample_queries` requests.

This class thinly wraps an initial [ListSampleQueriesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListSampleQueriesResponse) object, and provides an `__iter__` method to iterate through its `sample_queries` field.

If there are more pages, the `__iter__` method will make additional `ListSampleQueries` requests and continue to iterate through the `sample_queries` field on the corresponding responses.

All the usual [ListSampleQueriesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListSampleQueriesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [SampleQuerySetServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.sample_query_set_service.SampleQuerySetServiceAsyncClient)

Service for managing SampleQuerySets,

### [SampleQuerySetServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.sample_query_set_service.SampleQuerySetServiceClient)

Service for managing SampleQuerySets,

### [ListSampleQuerySetsAsyncPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.sample_query_set_service.pagers.ListSampleQuerySetsAsyncPager)

A pager for iterating through `list_sample_query_sets` requests.

This class thinly wraps an initial [ListSampleQuerySetsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListSampleQuerySetsResponse) object, and provides an `__aiter__` method to iterate through its `sample_query_sets` field.

If there are more pages, the `__aiter__` method will make additional `ListSampleQuerySets` requests and continue to iterate through the `sample_query_sets` field on the corresponding responses.

All the usual [ListSampleQuerySetsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListSampleQuerySetsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListSampleQuerySetsPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.sample_query_set_service.pagers.ListSampleQuerySetsPager)

A pager for iterating through `list_sample_query_sets` requests.

This class thinly wraps an initial [ListSampleQuerySetsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListSampleQuerySetsResponse) object, and provides an `__iter__` method to iterate through its `sample_query_sets` field.

If there are more pages, the `__iter__` method will make additional `ListSampleQuerySets` requests and continue to iterate through the `sample_query_sets` field on the corresponding responses.

All the usual [ListSampleQuerySetsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListSampleQuerySetsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [SchemaServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.schema_service.SchemaServiceAsyncClient)

Service for managing Schemas.

### [SchemaServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.schema_service.SchemaServiceClient)

Service for managing Schemas.

### [ListSchemasAsyncPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.schema_service.pagers.ListSchemasAsyncPager)

A pager for iterating through `list_schemas` requests.

This class thinly wraps an initial [ListSchemasResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListSchemasResponse) object, and provides an `__aiter__` method to iterate through its `schemas` field.

If there are more pages, the `__aiter__` method will make additional `ListSchemas` requests and continue to iterate through the `schemas` field on the corresponding responses.

All the usual [ListSchemasResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListSchemasResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListSchemasPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.schema_service.pagers.ListSchemasPager)

A pager for iterating through `list_schemas` requests.

This class thinly wraps an initial [ListSchemasResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListSchemasResponse) object, and provides an `__iter__` method to iterate through its `schemas` field.

If there are more pages, the `__iter__` method will make additional `ListSchemas` requests and continue to iterate through the `schemas` field on the corresponding responses.

All the usual [ListSchemasResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListSchemasResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [SearchServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.search_service.SearchServiceAsyncClient)

Service for search.

### [SearchServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.search_service.SearchServiceClient)

Service for search.

### [SearchAsyncPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.search_service.pagers.SearchAsyncPager)

A pager for iterating through `search` requests.

This class thinly wraps an initial [SearchResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchResponse) object, and provides an `__aiter__` method to iterate through its `results` field.

If there are more pages, the `__aiter__` method will make additional `Search` requests and continue to iterate through the `results` field on the corresponding responses.

All the usual [SearchResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [SearchLiteAsyncPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.search_service.pagers.SearchLiteAsyncPager)

A pager for iterating through `search_lite` requests.

This class thinly wraps an initial [SearchResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchResponse) object, and provides an `__aiter__` method to iterate through its `results` field.

If there are more pages, the `__aiter__` method will make additional `SearchLite` requests and continue to iterate through the `results` field on the corresponding responses.

All the usual [SearchResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [SearchLitePager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.search_service.pagers.SearchLitePager)

A pager for iterating through `search_lite` requests.

This class thinly wraps an initial [SearchResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchResponse) object, and provides an `__iter__` method to iterate through its `results` field.

If there are more pages, the `__iter__` method will make additional `SearchLite` requests and continue to iterate through the `results` field on the corresponding responses.

All the usual [SearchResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [SearchPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.search_service.pagers.SearchPager)

A pager for iterating through `search` requests.

This class thinly wraps an initial [SearchResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchResponse) object, and provides an `__iter__` method to iterate through its `results` field.

If there are more pages, the `__iter__` method will make additional `Search` requests and continue to iterate through the `results` field on the corresponding responses.

All the usual [SearchResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [SearchTuningServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.search_tuning_service.SearchTuningServiceAsyncClient)

Service for search tuning.

### [SearchTuningServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.search_tuning_service.SearchTuningServiceClient)

Service for search tuning.

### [ServingConfigServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.serving_config_service.ServingConfigServiceAsyncClient)

Service for operations related to ServingConfig.

### [ServingConfigServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.serving_config_service.ServingConfigServiceClient)

Service for operations related to ServingConfig.

### [ListServingConfigsAsyncPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.serving_config_service.pagers.ListServingConfigsAsyncPager)

A pager for iterating through `list_serving_configs` requests.

This class thinly wraps an initial [ListServingConfigsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListServingConfigsResponse) object, and provides an `__aiter__` method to iterate through its `serving_configs` field.

If there are more pages, the `__aiter__` method will make additional `ListServingConfigs` requests and continue to iterate through the `serving_configs` field on the corresponding responses.

All the usual [ListServingConfigsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListServingConfigsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListServingConfigsPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.serving_config_service.pagers.ListServingConfigsPager)

A pager for iterating through `list_serving_configs` requests.

This class thinly wraps an initial [ListServingConfigsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListServingConfigsResponse) object, and provides an `__iter__` method to iterate through its `serving_configs` field.

If there are more pages, the `__iter__` method will make additional `ListServingConfigs` requests and continue to iterate through the `serving_configs` field on the corresponding responses.

All the usual [ListServingConfigsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListServingConfigsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [SessionServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.session_service.SessionServiceAsyncClient)

Service for managing Sessions and Session-related resources.

### [SessionServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.session_service.SessionServiceClient)

Service for managing Sessions and Session-related resources.

### [ListSessionsAsyncPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.session_service.pagers.ListSessionsAsyncPager)

A pager for iterating through `list_sessions` requests.

This class thinly wraps an initial [ListSessionsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListSessionsResponse) object, and provides an `__aiter__` method to iterate through its `sessions` field.

If there are more pages, the `__aiter__` method will make additional `ListSessions` requests and continue to iterate through the `sessions` field on the corresponding responses.

All the usual [ListSessionsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListSessionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListSessionsPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.session_service.pagers.ListSessionsPager)

A pager for iterating through `list_sessions` requests.

This class thinly wraps an initial [ListSessionsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListSessionsResponse) object, and provides an `__iter__` method to iterate through its `sessions` field.

If there are more pages, the `__iter__` method will make additional `ListSessions` requests and continue to iterate through the `sessions` field on the corresponding responses.

All the usual [ListSessionsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListSessionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [SiteSearchEngineServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.site_search_engine_service.SiteSearchEngineServiceAsyncClient)

Service for managing site search related resources.

### [SiteSearchEngineServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.site_search_engine_service.SiteSearchEngineServiceClient)

Service for managing site search related resources.

### [FetchDomainVerificationStatusAsyncPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.site_search_engine_service.pagers.FetchDomainVerificationStatusAsyncPager)

A pager for iterating through `fetch_domain_verification_status` requests.

This class thinly wraps an initial [FetchDomainVerificationStatusResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.FetchDomainVerificationStatusResponse) object, and provides an `__aiter__` method to iterate through its `target_sites` field.

If there are more pages, the `__aiter__` method will make additional `FetchDomainVerificationStatus` requests and continue to iterate through the `target_sites` field on the corresponding responses.

All the usual [FetchDomainVerificationStatusResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.FetchDomainVerificationStatusResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [FetchDomainVerificationStatusPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.site_search_engine_service.pagers.FetchDomainVerificationStatusPager)

A pager for iterating through `fetch_domain_verification_status` requests.

This class thinly wraps an initial [FetchDomainVerificationStatusResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.FetchDomainVerificationStatusResponse) object, and provides an `__iter__` method to iterate through its `target_sites` field.

If there are more pages, the `__iter__` method will make additional `FetchDomainVerificationStatus` requests and continue to iterate through the `target_sites` field on the corresponding responses.

All the usual [FetchDomainVerificationStatusResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.FetchDomainVerificationStatusResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListTargetSitesAsyncPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.site_search_engine_service.pagers.ListTargetSitesAsyncPager)

A pager for iterating through `list_target_sites` requests.

This class thinly wraps an initial [ListTargetSitesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListTargetSitesResponse) object, and provides an `__aiter__` method to iterate through its `target_sites` field.

If there are more pages, the `__aiter__` method will make additional `ListTargetSites` requests and continue to iterate through the `target_sites` field on the corresponding responses.

All the usual [ListTargetSitesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListTargetSitesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListTargetSitesPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.site_search_engine_service.pagers.ListTargetSitesPager)

A pager for iterating through `list_target_sites` requests.

This class thinly wraps an initial [ListTargetSitesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListTargetSitesResponse) object, and provides an `__iter__` method to iterate through its `target_sites` field.

If there are more pages, the `__iter__` method will make additional `ListTargetSites` requests and continue to iterate through the `target_sites` field on the corresponding responses.

All the usual [ListTargetSitesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListTargetSitesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [UserEventServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.user_event_service.UserEventServiceAsyncClient)

Service for ingesting end user actions on a website to Discovery Engine API.

### [UserEventServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.user_event_service.UserEventServiceClient)

Service for ingesting end user actions on a website to Discovery Engine API.

### [UserLicenseServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.user_license_service.UserLicenseServiceAsyncClient)

Service for managing User Licenses.

### [UserLicenseServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.user_license_service.UserLicenseServiceClient)

Service for managing User Licenses.

### [ListUserLicensesAsyncPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.user_license_service.pagers.ListUserLicensesAsyncPager)

A pager for iterating through `list_user_licenses` requests.

This class thinly wraps an initial [ListUserLicensesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListUserLicensesResponse) object, and provides an `__aiter__` method to iterate through its `user_licenses` field.

If there are more pages, the `__aiter__` method will make additional `ListUserLicenses` requests and continue to iterate through the `user_licenses` field on the corresponding responses.

All the usual [ListUserLicensesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListUserLicensesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListUserLicensesPager](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.user_license_service.pagers.ListUserLicensesPager)

A pager for iterating through `list_user_licenses` requests.

This class thinly wraps an initial [ListUserLicensesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListUserLicensesResponse) object, and provides an `__iter__` method to iterate through its `user_licenses` field.

If there are more pages, the `__iter__` method will make additional `ListUserLicenses` requests and continue to iterate through the `user_licenses` field on the corresponding responses.

All the usual [ListUserLicensesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListUserLicensesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [UserStoreServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.user_store_service.UserStoreServiceAsyncClient)

Service for managing User Stores.

### [UserStoreServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.user_store_service.UserStoreServiceClient)

Service for managing User Stores.

### [AclConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AclConfig)

Access Control Configuration.

### [AdvancedCompleteQueryRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AdvancedCompleteQueryRequest)

Request message for CompletionService.AdvancedCompleteQuery method. .

### [BoostSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AdvancedCompleteQueryRequest.BoostSpec)

Specification to boost suggestions based on the condition of the suggestion.

### [ConditionBoostSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AdvancedCompleteQueryRequest.BoostSpec.ConditionBoostSpec)

Boost applies to suggestions which match a condition.

### [SuggestionType](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AdvancedCompleteQueryRequest.SuggestionType)

Suggestion type to return.

### [SuggestionTypeSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AdvancedCompleteQueryRequest.SuggestionTypeSpec)

Specification of each suggestion type.

### [AdvancedCompleteQueryResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AdvancedCompleteQueryResponse)

Response message for CompletionService.AdvancedCompleteQuery method.

### [ContentSuggestion](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AdvancedCompleteQueryResponse.ContentSuggestion)

Suggestions as content.

### [ContentType](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AdvancedCompleteQueryResponse.ContentSuggestion.ContentType)

The type of the content returned for content suggestions.

### [PersonSuggestion](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AdvancedCompleteQueryResponse.PersonSuggestion)

Suggestions as people.

### [PersonType](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AdvancedCompleteQueryResponse.PersonSuggestion.PersonType)

The type of the person based on the source.

### [QuerySuggestion](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AdvancedCompleteQueryResponse.QuerySuggestion)

Suggestions as search queries.

### [RecentSearchSuggestion](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AdvancedCompleteQueryResponse.RecentSearchSuggestion)

Suggestions from recent search history.

### [AdvancedSiteSearchConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AdvancedSiteSearchConfig)

Configuration data for advance site search.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AgentGatewaySetting](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AgentGatewaySetting)

Agent Gateway setting, which may be attached to Gemini Enterprise resources for egress control of Gemini Enterprise agents to agents and tools outside of Gemini Enterprise.

### [AgentGatewayReference](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AgentGatewaySetting.AgentGatewayReference)

Reference to an Agent Gateway resource.

### [AlloyDbSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AlloyDbSource)

AlloyDB source import data from.

### [Answer](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Answer)

Defines an answer.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AnswerSkippedReason](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Answer.AnswerSkippedReason)

An enum for answer skipped reasons.
    
    
        Google skips the answer if the query is chit
        chat.
    OUT_OF_DOMAIN_QUERY_IGNORED (3):
        The out-of-domain query ignored case.
    
        Google skips the answer if there are no
        high-relevance search results.
    POTENTIAL_POLICY_VIOLATION (4):
        The potential policy violation case.
    
        Google skips the answer if there is a potential
        policy violation detected. This includes content
        that may be violent or toxic.
    NO_RELEVANT_CONTENT (5):
        The no relevant content case.
    
        Google skips the answer if there is no relevant
        content in the retrieved search results.
    JAIL_BREAKING_QUERY_IGNORED (6):
        The jail-breaking query ignored case.
    
        For example, "Reply in the tone of a competing
        company's CEO". Google skips the answer if the
        query is classified as a jail-breaking query.
    CUSTOMER_POLICY_VIOLATION (7):
        The customer policy violation case.
    
        Google skips the summary if there is a customer
        policy violation detected. The policy is defined
        by the customer.
    NON_ANSWER_SEEKING_QUERY_IGNORED_V2 (8):
        The non-answer seeking query ignored case.
    
        Google skips the answer if the query doesn't
        have clear intent.
    LOW_GROUNDED_ANSWER (9):
        The low-grounded answer case.
    
        Google skips the answer if a well grounded
        answer was unable to be generated.
    USER_DEFINED_CLASSIFICATION_QUERY_IGNORED (10):
        The user defined query classification ignored
        case.
        Google skips the answer if the query is
        classified as a user defined query
        classification.
    UNHELPFUL_ANSWER (11):
        The unhelpful answer case.
    
        Google skips the answer if the answer is not
        helpful. This can be due to a variety of
        factors, including but not limited to: the query
        is not answerable, the answer is not relevant to
        the query, or the answer is not well-formatted.
    

### [BlobAttachment](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Answer.BlobAttachment)

Stores binarydata attached to text answer, e.g. image, video, audio, etc.

### [AttributionType](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Answer.BlobAttachment.AttributionType)

The source of the blob.

### [Blob](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Answer.BlobAttachment.Blob)

The media type and data of the blob.

### [Citation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Answer.Citation)

Citation info for a segment.

### [CitationSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Answer.CitationSource)

Citation source.

### [GroundingSupport](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Answer.GroundingSupport)

Grounding support for a claim in `answer_text`.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [QueryUnderstandingInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Answer.QueryUnderstandingInfo)

Query understanding information.

### [QueryClassificationInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Answer.QueryUnderstandingInfo.QueryClassificationInfo)

Query classification information.

### [Type](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Answer.QueryUnderstandingInfo.QueryClassificationInfo.Type)

Query classification types.

### [Reference](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Answer.Reference)

Reference.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ChunkInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Answer.Reference.ChunkInfo)

Chunk information.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [DocumentMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Answer.Reference.ChunkInfo.DocumentMetadata)

Document metadata.

### [StructuredDocumentInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Answer.Reference.StructuredDocumentInfo)

Structured search information.

### [UnstructuredDocumentInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Answer.Reference.UnstructuredDocumentInfo)

Unstructured document information.

### [ChunkContent](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Answer.Reference.UnstructuredDocumentInfo.ChunkContent)

Chunk content.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [State](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Answer.State)

Enumeration of the state of the answer generation.

### [Step](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Answer.Step)

Step information.

### [Action](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Answer.Step.Action)

Action.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Observation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Answer.Step.Action.Observation)

Observation.

### [SearchResult](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Answer.Step.Action.Observation.SearchResult)

### [ChunkInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Answer.Step.Action.Observation.SearchResult.ChunkInfo)

Chunk information.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [SnippetInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Answer.Step.Action.Observation.SearchResult.SnippetInfo)

Snippet information.

### [SearchAction](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Answer.Step.Action.SearchAction)

Search action.

### [State](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Answer.Step.State)

Enumeration of the state of the step.

### [AnswerGenerationSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AnswerGenerationSpec)

The specification for answer generation.

### [UserDefinedClassifierSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AnswerGenerationSpec.UserDefinedClassifierSpec)

The specification for user defined classifier.

### [AnswerQueryRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AnswerQueryRequest)

Request message for ConversationalSearchService.AnswerQuery method.

### [AnswerGenerationSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AnswerQueryRequest.AnswerGenerationSpec)

Answer generation specification.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ModelSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AnswerQueryRequest.AnswerGenerationSpec.ModelSpec)

Answer Generation Model specification.

### [MultimodalSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AnswerQueryRequest.AnswerGenerationSpec.MultimodalSpec)

Multimodal specification: Will return an image from specified source. If multiple sources are specified, the pick is a quality based decision.

### [ImageSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AnswerQueryRequest.AnswerGenerationSpec.MultimodalSpec.ImageSource)

Specifies the image source.

### [PromptSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AnswerQueryRequest.AnswerGenerationSpec.PromptSpec)

Answer generation prompt specification.

### [EndUserSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AnswerQueryRequest.EndUserSpec)

End user specification.

### [EndUserMetaData](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AnswerQueryRequest.EndUserSpec.EndUserMetaData)

End user metadata.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ChunkInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AnswerQueryRequest.EndUserSpec.EndUserMetaData.ChunkInfo)

Chunk information.

### [DocumentMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AnswerQueryRequest.EndUserSpec.EndUserMetaData.ChunkInfo.DocumentMetadata)

Document metadata contains the information of the document of the current chunk.

### [GroundingSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AnswerQueryRequest.GroundingSpec)

Grounding specification.

### [FilteringLevel](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AnswerQueryRequest.GroundingSpec.FilteringLevel)

Level to filter based on answer grounding.

### [QueryUnderstandingSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AnswerQueryRequest.QueryUnderstandingSpec)

Query understanding specification.

### [QueryClassificationSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AnswerQueryRequest.QueryUnderstandingSpec.QueryClassificationSpec)

Query classification specification.

### [Type](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AnswerQueryRequest.QueryUnderstandingSpec.QueryClassificationSpec.Type)

Query classification types.

### [QueryRephraserSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AnswerQueryRequest.QueryUnderstandingSpec.QueryRephraserSpec)

Query rephraser specification.

### [ModelSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AnswerQueryRequest.QueryUnderstandingSpec.QueryRephraserSpec.ModelSpec)

Query Rephraser Model specification.

### [ModelType](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AnswerQueryRequest.QueryUnderstandingSpec.QueryRephraserSpec.ModelSpec.ModelType)

Query rephraser types. Currently only supports single-hop (max_rephrase_steps = 1) model selections. For multi-hop (max_rephrase_steps > 1), there is only one default model.

### [RelatedQuestionsSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AnswerQueryRequest.RelatedQuestionsSpec)

Related questions specification.

### [SafetySpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AnswerQueryRequest.SafetySpec)

Safety specification. There are two use cases:

  1. when only safety_spec.enable is set, the BLOCK_LOW_AND_ABOVE threshold will be applied for all categories.
  2. when safety_spec.enable is set and some safety_settings are set, only specified safety_settings are applied.



### [SafetySetting](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AnswerQueryRequest.SafetySpec.SafetySetting)

Safety settings.

### [HarmBlockThreshold](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AnswerQueryRequest.SafetySpec.SafetySetting.HarmBlockThreshold)

Probability based thresholds levels for blocking.

### [SearchSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AnswerQueryRequest.SearchSpec)

Search specification.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [SearchParams](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AnswerQueryRequest.SearchSpec.SearchParams)

Search parameters.

### [SearchResultList](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AnswerQueryRequest.SearchSpec.SearchResultList)

Search result list.

### [SearchResult](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AnswerQueryRequest.SearchSpec.SearchResultList.SearchResult)

Search result.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ChunkInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AnswerQueryRequest.SearchSpec.SearchResultList.SearchResult.ChunkInfo)

Chunk information.

### [DocumentMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AnswerQueryRequest.SearchSpec.SearchResultList.SearchResult.ChunkInfo.DocumentMetadata)

Document metadata contains the information of the document of the current chunk.

### [UnstructuredDocumentInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AnswerQueryRequest.SearchSpec.SearchResultList.SearchResult.UnstructuredDocumentInfo)

Unstructured document information.

### [DocumentContext](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AnswerQueryRequest.SearchSpec.SearchResultList.SearchResult.UnstructuredDocumentInfo.DocumentContext)

Document context.

### [ExtractiveAnswer](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AnswerQueryRequest.SearchSpec.SearchResultList.SearchResult.UnstructuredDocumentInfo.ExtractiveAnswer)

Extractive answer. `Guide <https://cloud.google.com/generative-ai-app-builder/docs/snippets#get-answers>`__

### [ExtractiveSegment](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AnswerQueryRequest.SearchSpec.SearchResultList.SearchResult.UnstructuredDocumentInfo.ExtractiveSegment)

Extractive segment. `Guide <https://cloud.google.com/generative-ai-app-builder/docs/snippets#extractive-segments>`__ Answer generation will only use it if document_contexts is empty. This is supposed to be shorter snippets.

### [UserLabelsEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AnswerQueryRequest.UserLabelsEntry)

The abstract base class for a message.

### [AnswerQueryResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AnswerQueryResponse)

Response message for ConversationalSearchService.AnswerQuery method.

### [AssistAnswer](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AssistAnswer)

AssistAnswer resource, main part of AssistResponse.

### [AssistSkippedReason](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AssistAnswer.AssistSkippedReason)

Possible reasons for not answering an assist call.

### [CustomerPolicyEnforcementResult](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AssistAnswer.CustomerPolicyEnforcementResult)

Customer policy enforcement results. Contains the results of the various policy checks, like the banned phrases or the Model Armor checks.

### [BannedPhraseEnforcementResult](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AssistAnswer.CustomerPolicyEnforcementResult.BannedPhraseEnforcementResult)

Customer policy enforcement result for the banned phrase policy.

### [ModelArmorEnforcementResult](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AssistAnswer.CustomerPolicyEnforcementResult.ModelArmorEnforcementResult)

Customer policy enforcement result for the Model Armor policy.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [PolicyEnforcementResult](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AssistAnswer.CustomerPolicyEnforcementResult.PolicyEnforcementResult)

Customer policy enforcement result for a single policy type.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Verdict](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AssistAnswer.CustomerPolicyEnforcementResult.Verdict)

The verdict of the customer policy enforcement.

### [Reply](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AssistAnswer.Reply)

One part of the multi-part response of the assist call.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [State](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AssistAnswer.State)

State of the answer generation.

### [AssistUserMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AssistUserMetadata)

User metadata of the request.

### [Assistant](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Assistant)

Discovery Engine Assistant resource.

### [CustomerPolicy](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Assistant.CustomerPolicy)

Customer-defined policy for the assistant.

### [BannedPhrase](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Assistant.CustomerPolicy.BannedPhrase)

Definition of a customer-defined banned phrase. A banned phrase is not allowed to appear in the user query or the LLM response, or else the answer will be refused.

### [BannedPhraseMatchType](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Assistant.CustomerPolicy.BannedPhrase.BannedPhraseMatchType)

The matching method for the banned phrase.

### [ModelArmorConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Assistant.CustomerPolicy.ModelArmorConfig)

Configuration for customer defined Model Armor templates to be used for sanitizing user prompts and assistant responses.

### [FailureMode](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Assistant.CustomerPolicy.ModelArmorConfig.FailureMode)

Determines the behavior when Model Armor fails to process a request.

### [EnabledToolsEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Assistant.EnabledToolsEntry)

The abstract base class for a message.

### [GenerationConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Assistant.GenerationConfig)

Configuration for the generation of the assistant response.

### [SystemInstruction](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Assistant.GenerationConfig.SystemInstruction)

System instruction, also known as the prompt preamble for LLM calls.

### [ToolInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Assistant.ToolInfo)

Information to identify a tool.

### [ToolList](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Assistant.ToolList)

The enabled tools on a connector

### [WebGroundingType](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Assistant.WebGroundingType)

The type of web grounding to use.

### [AssistantContent](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AssistantContent)

Multi-modal content.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Blob](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AssistantContent.Blob)

Inline blob.

### [CodeExecutionResult](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AssistantContent.CodeExecutionResult)

Result of executing ExecutableCode.

### [Outcome](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AssistantContent.CodeExecutionResult.Outcome)

Enumeration of possible outcomes of the code execution.

### [ExecutableCode](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AssistantContent.ExecutableCode)

Code generated by the model that is meant to be executed by the model.

### [File](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AssistantContent.File)

A file, e.g., an audio summary.

### [AssistantGroundedContent](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AssistantGroundedContent)

A piece of content and possibly its grounding information.

Not all content needs grounding. Phrases like "Of course, I will gladly search it for you." do not need grounding.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [TextGroundingMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AssistantGroundedContent.TextGroundingMetadata)

Grounding details for text sources.

### [Reference](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AssistantGroundedContent.TextGroundingMetadata.Reference)

Referenced content and related document metadata.

### [DocumentMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AssistantGroundedContent.TextGroundingMetadata.Reference.DocumentMetadata)

Document metadata.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Language](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AssistantGroundedContent.TextGroundingMetadata.Reference.DocumentMetadata.Language)

Language of the referenced content. For now, it is only used for code.

### [Segment](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AssistantGroundedContent.TextGroundingMetadata.Segment)

Grounding information for a segment of the text.

### [VisualSegment](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.AssistantGroundedContent.TextGroundingMetadata.VisualSegment)

Grounding information for a visual segment.

### [BatchCreateTargetSiteMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.BatchCreateTargetSiteMetadata)

Metadata related to the progress of the SiteSearchEngineService.BatchCreateTargetSites operation. This will be returned by the google.longrunning.Operation.metadata field.

### [BatchCreateTargetSitesRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.BatchCreateTargetSitesRequest)

Request message for SiteSearchEngineService.BatchCreateTargetSites method.

### [BatchCreateTargetSitesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.BatchCreateTargetSitesResponse)

Response message for SiteSearchEngineService.BatchCreateTargetSites method.

### [BatchGetDocumentsMetadataRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.BatchGetDocumentsMetadataRequest)

Request message for DocumentService.BatchGetDocumentsMetadata method.

### [FhirMatcher](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.BatchGetDocumentsMetadataRequest.FhirMatcher)

Matcher for the Documents by FHIR resource names.

### [Matcher](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.BatchGetDocumentsMetadataRequest.Matcher)

Matcher for the Documents. Currently supports matching by exact URIs.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [UrisMatcher](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.BatchGetDocumentsMetadataRequest.UrisMatcher)

Matcher for the Documents by exact uris.

### [BatchGetDocumentsMetadataResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.BatchGetDocumentsMetadataResponse)

Response message for DocumentService.BatchGetDocumentsMetadata method.

### [DocumentMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.BatchGetDocumentsMetadataResponse.DocumentMetadata)

The metadata of a Document.

### [MatcherValue](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.BatchGetDocumentsMetadataResponse.DocumentMetadata.MatcherValue)

The value of the matcher that was used to match the Document.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [State](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.BatchGetDocumentsMetadataResponse.State)

The state of the Document.

### [BatchUpdateUserLicensesMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.BatchUpdateUserLicensesMetadata)

Metadata related to the progress of the UserLicenseService.BatchUpdateUserLicenses operation. This will be returned by the google.longrunning.Operation.metadata field.

### [BatchUpdateUserLicensesRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.BatchUpdateUserLicensesRequest)

Request message for UserLicenseService.BatchUpdateUserLicenses method.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [InlineSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.BatchUpdateUserLicensesRequest.InlineSource)

The inline source for the input config for BatchUpdateUserLicenses method.

### [BatchUpdateUserLicensesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.BatchUpdateUserLicensesResponse)

Response message for UserLicenseService.BatchUpdateUserLicenses method.

### [BatchVerifyTargetSitesMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.BatchVerifyTargetSitesMetadata)

Metadata related to the progress of the SiteSearchEngineService.BatchVerifyTargetSites operation. This will be returned by the google.longrunning.Operation.metadata field.

### [BatchVerifyTargetSitesRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.BatchVerifyTargetSitesRequest)

Request message for SiteSearchEngineService.BatchVerifyTargetSites method.

### [BatchVerifyTargetSitesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.BatchVerifyTargetSitesResponse)

Response message for SiteSearchEngineService.BatchVerifyTargetSites method.

### [BigQuerySource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.BigQuerySource)

BigQuery source import data from.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [BigtableOptions](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.BigtableOptions)

The Bigtable Options object that contains information to support the import.

### [BigtableColumn](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.BigtableOptions.BigtableColumn)

The column of the Bigtable.

### [BigtableColumnFamily](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.BigtableOptions.BigtableColumnFamily)

The column family of the Bigtable.

### [Encoding](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.BigtableOptions.Encoding)

The encoding mode of a Bigtable column or column family.

### [FamiliesEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.BigtableOptions.FamiliesEntry)

The abstract base class for a message.

### [Type](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.BigtableOptions.Type)

The type of values in a Bigtable column or column family. The values are expected to be encoded using `HBase Bytes.toBytes <https://hbase.apache.org/1.4/apidocs/org/apache/hadoop/hbase/util/Bytes.html>`__ function when the encoding value is set to `BINARY`.

### [BigtableSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.BigtableSource)

The Cloud Bigtable source for importing data.

### [CheckGroundingRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.CheckGroundingRequest)

Request message for GroundedGenerationService.CheckGrounding method.

### [UserLabelsEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.CheckGroundingRequest.UserLabelsEntry)

The abstract base class for a message.

### [CheckGroundingResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.CheckGroundingResponse)

Response message for the GroundedGenerationService.CheckGrounding method.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [CheckGroundingFactChunk](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.CheckGroundingResponse.CheckGroundingFactChunk)

Fact chunk for grounding check.

### [Claim](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.CheckGroundingResponse.Claim)

Text and citation info for a claim in the answer candidate.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [CheckGroundingSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.CheckGroundingSpec)

Specification for the grounding check.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Chunk](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Chunk)

Chunk captures all raw metadata information of items to be recommended or searched in the chunk mode.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AnnotationMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Chunk.AnnotationMetadata)

The annotation metadata includes structured content in the current chunk.

### [ChunkMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Chunk.ChunkMetadata)

Metadata of the current chunk. This field is only populated on SearchService.Search API.

### [DocumentMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Chunk.DocumentMetadata)

Document metadata contains the information of the document of the current chunk.

### [PageSpan](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Chunk.PageSpan)

Page span of the chunk.

### [StructureType](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Chunk.StructureType)

Defines the types of the structured content that can be extracted.

### [StructuredContent](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Chunk.StructuredContent)

The structured content information.

### [Citation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Citation)

Source attributions for content.

### [PhishBlockThreshold](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Citation.PhishBlockThreshold)

These are available confidence level user can set to block malicious urls with chosen confidence and above. For understanding different confidence of webrisk, please refer to <https://cloud.google.com/web-risk/docs/reference/rpc/google.cloud.webrisk.v1eap1#confidencelevel>

### [CitationMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.CitationMetadata)

A collection of source attributions for a piece of content.

### [CloudSqlSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.CloudSqlSource)

Cloud SQL source import data from.

### [CmekConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.CmekConfig)

Configurations used to enable CMEK data encryption with Cloud KMS keys.

### [NotebookLMState](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.CmekConfig.NotebookLMState)

States of NotebookLM.

### [State](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.CmekConfig.State)

States of the CmekConfig.

### [CollectUserEventRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.CollectUserEventRequest)

Request message for CollectUserEvent method.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [CompleteQueryRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.CompleteQueryRequest)

Request message for CompletionService.CompleteQuery method.

### [CompleteQueryResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.CompleteQueryResponse)

Response message for CompletionService.CompleteQuery method.

### [QuerySuggestion](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.CompleteQueryResponse.QuerySuggestion)

Suggestions as search queries.

### [CompletionInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.CompletionInfo)

Detailed completion information including completion attribution token and clicked completion info.

### [CompletionSuggestion](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.CompletionSuggestion)

Autocomplete suggestions that are imported from Customer.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Condition](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Condition)

Defines circumstances to be checked before allowing a behavior

### [QueryTerm](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Condition.QueryTerm)

Matcher for search request query

### [TimeRange](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Condition.TimeRange)

Used for time-dependent conditions.

### [Control](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Control)

Defines a conditioned behavior to employ during serving. Must be attached to a ServingConfig to be considered at serving time. Permitted actions dependent on `SolutionType`.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [BoostAction](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Control.BoostAction)

Adjusts order of products in returned list.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [InterpolationBoostSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Control.BoostAction.InterpolationBoostSpec)

Specification for custom ranking based on customer specified attribute value. It provides more controls for customized ranking than the simple (condition, boost) combination above.

### [AttributeType](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Control.BoostAction.InterpolationBoostSpec.AttributeType)

The attribute(or function) for which the custom ranking is to be applied.

### [ControlPoint](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Control.BoostAction.InterpolationBoostSpec.ControlPoint)

The control points used to define the curve. The curve defined through these control points can only be monotonically increasing or decreasing(constant values are acceptable).

### [InterpolationType](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Control.BoostAction.InterpolationBoostSpec.InterpolationType)

The interpolation type to be applied. Default will be linear (Piecewise Linear).

### [FilterAction](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Control.FilterAction)

Specified which products may be included in results. Uses same filter as boost.

### [PromoteAction](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Control.PromoteAction)

Promote certain links based on some trigger queries.

Example: Promote shoe store link when searching for `shoe` keyword. The link can be outside of associated data store.

### [RedirectAction](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Control.RedirectAction)

Redirects a shopper to the provided URI.

### [SynonymsAction](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Control.SynonymsAction)

Creates a set of terms that will act as synonyms of one another. Example: "happy" will also be considered as "glad", "glad" will also be considered as "happy".

### [Conversation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Conversation)

External conversation proto definition.

### [State](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Conversation.State)

Enumeration of the state of the conversation.

### [ConversationContext](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ConversationContext)

Defines context of the conversation

### [ConversationMessage](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ConversationMessage)

Defines a conversation message.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ConverseConversationRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ConverseConversationRequest)

Request message for ConversationalSearchService.ConverseConversation method.

### [UserLabelsEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ConverseConversationRequest.UserLabelsEntry)

The abstract base class for a message.

### [ConverseConversationResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ConverseConversationResponse)

Response message for ConversationalSearchService.ConverseConversation method.

### [CreateAssistantRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.CreateAssistantRequest)

Request for the AssistantService.CreateAssistant method.

### [CreateControlRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.CreateControlRequest)

Request for CreateControl method.

### [CreateConversationRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.CreateConversationRequest)

Request for CreateConversation method.

### [CreateDataStoreMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.CreateDataStoreMetadata)

Metadata related to the progress of the DataStoreService.CreateDataStore operation. This will be returned by the google.longrunning.Operation.metadata field.

### [CreateDataStoreRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.CreateDataStoreRequest)

Request for DataStoreService.CreateDataStore method.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [CreateDocumentRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.CreateDocumentRequest)

Request message for DocumentService.CreateDocument method.

### [CreateEngineMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.CreateEngineMetadata)

Metadata related to the progress of the EngineService.CreateEngine operation. This will be returned by the google.longrunning.Operation.metadata field.

### [CreateEngineRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.CreateEngineRequest)

Request for EngineService.CreateEngine method.

### [CreateEvaluationMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.CreateEvaluationMetadata)

Metadata for EvaluationService.CreateEvaluation method.

### [CreateEvaluationRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.CreateEvaluationRequest)

Request message for EvaluationService.CreateEvaluation method.

### [CreateIdentityMappingStoreRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.CreateIdentityMappingStoreRequest)

Request message for IdentityMappingStoreService.CreateIdentityMappingStore

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [CreateLicenseConfigRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.CreateLicenseConfigRequest)

Request message for LicenseConfigService.CreateLicenseConfig method.

### [CreateSampleQueryRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.CreateSampleQueryRequest)

Request message for SampleQueryService.CreateSampleQuery method.

### [CreateSampleQuerySetRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.CreateSampleQuerySetRequest)

Request message for SampleQuerySetService.CreateSampleQuerySet method.

### [CreateSchemaMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.CreateSchemaMetadata)

Metadata for Create Schema LRO.

### [CreateSchemaRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.CreateSchemaRequest)

Request message for SchemaService.CreateSchema method.

### [CreateServingConfigRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.CreateServingConfigRequest)

Request for CreateServingConfig method.

### [CreateSessionRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.CreateSessionRequest)

Request for CreateSession method.

### [CreateSitemapMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.CreateSitemapMetadata)

Metadata related to the progress of the SiteSearchEngineService.CreateSitemap operation. This will be returned by the google.longrunning.Operation.metadata field.

### [CreateSitemapRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.CreateSitemapRequest)

Request message for SiteSearchEngineService.CreateSitemap method.

### [CreateTargetSiteMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.CreateTargetSiteMetadata)

Metadata related to the progress of the SiteSearchEngineService.CreateTargetSite operation. This will be returned by the google.longrunning.Operation.metadata field.

### [CreateTargetSiteRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.CreateTargetSiteRequest)

Request message for SiteSearchEngineService.CreateTargetSite method.

### [CustomAttribute](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.CustomAttribute)

A custom attribute that is not explicitly modeled in a resource, e.g. UserEvent.

### [CustomTuningModel](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.CustomTuningModel)

Metadata that describes a custom tuned model.

### [MetricsEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.CustomTuningModel.MetricsEntry)

The abstract base class for a message.

### [ModelState](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.CustomTuningModel.ModelState)

The state of the model.

### [DataStore](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.DataStore)

DataStore captures global settings and configs at the DataStore level.

### [BillingEstimation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.DataStore.BillingEstimation)

Estimation of data size per data store.

### [ConfigurableBillingApproach](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.DataStore.ConfigurableBillingApproach)

Configuration for configurable billing approach.

### [ContentConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.DataStore.ContentConfig)

Content config of the data store.

### [FederatedSearchConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.DataStore.FederatedSearchConfig)

Stores information for federated search.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AlloyDbConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.DataStore.FederatedSearchConfig.AlloyDbConfig)

Stores information for connecting to AlloyDB.

### [AlloyDbAiNaturalLanguageConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.DataStore.FederatedSearchConfig.AlloyDbConfig.AlloyDbAiNaturalLanguageConfig)

Configuration for AlloyDB AI Natural Language.

### [AlloyDbConnectionConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.DataStore.FederatedSearchConfig.AlloyDbConfig.AlloyDbConnectionConfig)

Configuration for connecting to AlloyDB.

### [AuthMode](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.DataStore.FederatedSearchConfig.AlloyDbConfig.AlloyDbConnectionConfig.AuthMode)

Auth mode.

### [NotebooklmConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.DataStore.FederatedSearchConfig.NotebooklmConfig)

Config for connecting to NotebookLM Enterprise.

### [ThirdPartyOauthConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.DataStore.FederatedSearchConfig.ThirdPartyOauthConfig)

Stores information for third party applicationOAuth.

### [ServingConfigDataStore](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.DataStore.ServingConfigDataStore)

Stores information regarding the serving configurations at DataStore level.

### [DeleteAssistantRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.DeleteAssistantRequest)

Request message for the AssistantService.DeleteAssistant method.

### [DeleteCmekConfigMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.DeleteCmekConfigMetadata)

Metadata related to the progress of the CmekConfigService.DeleteCmekConfig operation. This will be returned by the google.longrunning.Operation.metadata field.

### [DeleteCmekConfigRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.DeleteCmekConfigRequest)

Request message for CmekConfigService.DeleteCmekConfig method.

### [DeleteControlRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.DeleteControlRequest)

Request for DeleteControl method.

### [DeleteConversationRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.DeleteConversationRequest)

Request for DeleteConversation method.

### [DeleteDataStoreMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.DeleteDataStoreMetadata)

Metadata related to the progress of the DataStoreService.DeleteDataStore operation. This will be returned by the google.longrunning.Operation.metadata field.

### [DeleteDataStoreRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.DeleteDataStoreRequest)

Request message for DataStoreService.DeleteDataStore method.

### [DeleteDocumentRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.DeleteDocumentRequest)

Request message for DocumentService.DeleteDocument method.

### [DeleteEngineMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.DeleteEngineMetadata)

Metadata related to the progress of the EngineService.DeleteEngine operation. This will be returned by the google.longrunning.Operation.metadata field.

### [DeleteEngineRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.DeleteEngineRequest)

Request message for EngineService.DeleteEngine method.

### [DeleteIdentityMappingStoreMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.DeleteIdentityMappingStoreMetadata)

Metadata related to the progress of the IdentityMappingStoreService.DeleteIdentityMappingStore operation. This will be returned by the google.longrunning.Operation.metadata field.

### [DeleteIdentityMappingStoreRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.DeleteIdentityMappingStoreRequest)

Request message for IdentityMappingStoreService.DeleteIdentityMappingStore

### [DeleteSampleQueryRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.DeleteSampleQueryRequest)

Request message for SampleQueryService.DeleteSampleQuery method.

### [DeleteSampleQuerySetRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.DeleteSampleQuerySetRequest)

Request message for SampleQuerySetService.DeleteSampleQuerySet method.

### [DeleteSchemaMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.DeleteSchemaMetadata)

Metadata for DeleteSchema LRO.

### [DeleteSchemaRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.DeleteSchemaRequest)

Request message for SchemaService.DeleteSchema method.

### [DeleteServingConfigRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.DeleteServingConfigRequest)

Request for DeleteServingConfig method.

### [DeleteSessionRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.DeleteSessionRequest)

Request for DeleteSession method.

### [DeleteSitemapMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.DeleteSitemapMetadata)

Metadata related to the progress of the SiteSearchEngineService.DeleteSitemap operation. This will be returned by the google.longrunning.Operation.metadata field.

### [DeleteSitemapRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.DeleteSitemapRequest)

Request message for SiteSearchEngineService.DeleteSitemap method.

### [DeleteTargetSiteMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.DeleteTargetSiteMetadata)

Metadata related to the progress of the SiteSearchEngineService.DeleteTargetSite operation. This will be returned by the google.longrunning.Operation.metadata field.

### [DeleteTargetSiteRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.DeleteTargetSiteRequest)

Request message for SiteSearchEngineService.DeleteTargetSite method.

### [DisableAdvancedSiteSearchMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.DisableAdvancedSiteSearchMetadata)

Metadata related to the progress of the SiteSearchEngineService.DisableAdvancedSiteSearch operation. This will be returned by the google.longrunning.Operation.metadata field.

### [DisableAdvancedSiteSearchRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.DisableAdvancedSiteSearchRequest)

Request message for SiteSearchEngineService.DisableAdvancedSiteSearch method.

### [DisableAdvancedSiteSearchResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.DisableAdvancedSiteSearchResponse)

Response message for SiteSearchEngineService.DisableAdvancedSiteSearch method.

### [DistributeLicenseConfigRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.DistributeLicenseConfigRequest)

Request message for LicenseConfigService.DistributeLicenseConfig method.

### [DistributeLicenseConfigResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.DistributeLicenseConfigResponse)

Response message for LicenseConfigService.DistributeLicenseConfig method.

### [Document](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Document)

Document captures all raw metadata information of items to be recommended or searched.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AclInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Document.AclInfo)

ACL Information of the Document.

### [AccessRestriction](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Document.AclInfo.AccessRestriction)

AclRestriction to model complex inheritance restrictions.

Example: Modeling a "Both Permit" inheritance, where to access a child document, user needs to have access to parent document.

Document Hierarchy - Space_S --> Page_P.

Readers: Space_S: group_1, user_1 Page_P: group_2, group_3, user_2

Space_S ACL Restriction - { "acl_info": { "readers": [ { "principals": [ { "group_id": "group_1" }, { "user_id": "user_1" } ] } ] } }

Page_P ACL Restriction. { "acl_info": { "readers": [ { "principals": [ { "group_id": "group_2" }, { "group_id": "group_3" }, { "user_id": "user_2" } ], }, { "principals": [ { "group_id": "group_1" }, { "user_id": "user_1" } ], } ] } }

### [Content](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Document.Content)

Unstructured data linked to this document.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [IndexStatus](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Document.IndexStatus)

Index status of the document.

### [DocumentInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.DocumentInfo)

Detailed document information associated with a user event.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [DocumentProcessingConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.DocumentProcessingConfig)

A singleton resource of DataStore. If it's empty when DataStore is created and DataStore is set to DataStore.ContentConfig.CONTENT_REQUIRED, the default parser will default to digital parser.

### [ChunkingConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.DocumentProcessingConfig.ChunkingConfig)

Configuration for chunking config.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [LayoutBasedChunkingConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.DocumentProcessingConfig.ChunkingConfig.LayoutBasedChunkingConfig)

Configuration for the layout based chunking.

### [ParsingConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.DocumentProcessingConfig.ParsingConfig)

Related configurations applied to a specific type of document parser.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [DigitalParsingConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.DocumentProcessingConfig.ParsingConfig.DigitalParsingConfig)

The digital parsing configurations for documents.

### [LayoutParsingConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.DocumentProcessingConfig.ParsingConfig.LayoutParsingConfig)

The layout parsing configurations for documents.

### [OcrParsingConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.DocumentProcessingConfig.ParsingConfig.OcrParsingConfig)

The OCR parsing configurations for documents.

### [ParsingConfigOverridesEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.DocumentProcessingConfig.ParsingConfigOverridesEntry)

The abstract base class for a message.

### [DoubleList](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.DoubleList)

Double list.

### [EmbeddingConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.EmbeddingConfig)

Defines embedding config, used for bring your own embeddings feature.

### [EnableAdvancedSiteSearchMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.EnableAdvancedSiteSearchMetadata)

Metadata related to the progress of the SiteSearchEngineService.EnableAdvancedSiteSearch operation. This will be returned by the google.longrunning.Operation.metadata field.

### [EnableAdvancedSiteSearchRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.EnableAdvancedSiteSearchRequest)

Request message for SiteSearchEngineService.EnableAdvancedSiteSearch method.

### [EnableAdvancedSiteSearchResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.EnableAdvancedSiteSearchResponse)

Response message for SiteSearchEngineService.EnableAdvancedSiteSearch method.

### [Engine](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Engine)

Metadata that describes the training and serving parameters of an Engine.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AppType](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Engine.AppType)

The app of the engine.

### [ChatEngineConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Engine.ChatEngineConfig)

Configurations for a Chat Engine.

### [AgentCreationConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Engine.ChatEngineConfig.AgentCreationConfig)

Configurations for generating a Dialogflow agent.

Note that these configurations are one-time consumed by and passed to Dialogflow service. It means they cannot be retrieved using EngineService.GetEngine or EngineService.ListEngines API after engine creation.

### [ChatEngineMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Engine.ChatEngineMetadata)

Additional information of a Chat Engine. Fields in this message are output only.

### [CommonConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Engine.CommonConfig)

Common configurations for an Engine.

### [ConfigurableBillingApproach](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Engine.ConfigurableBillingApproach)

Configuration for configurable billing approach.

### [ConnectorTenantInfoEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Engine.ConnectorTenantInfoEntry)

The abstract base class for a message.

### [FeatureState](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Engine.FeatureState)

The state of the feature for the engine.

### [FeaturesEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Engine.FeaturesEntry)

The abstract base class for a message.

### [KnowledgeGraphConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Engine.KnowledgeGraphConfig)

Configuration message for the Knowledge Graph.

### [FeatureConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Engine.KnowledgeGraphConfig.FeatureConfig)

Feature config for the Knowledge Graph.

### [MarketplaceAgentVisibility](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Engine.MarketplaceAgentVisibility)

Represents which marketplace agents are visible to any users in agent gallery.

### [MediaRecommendationEngineConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Engine.MediaRecommendationEngineConfig)

Additional config specs for a Media Recommendation engine.

### [EngineFeaturesConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Engine.MediaRecommendationEngineConfig.EngineFeaturesConfig)

More feature configs of the selected engine type.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [MostPopularFeatureConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Engine.MediaRecommendationEngineConfig.MostPopularFeatureConfig)

Feature configurations that are required for creating a Most Popular engine.

### [OptimizationObjectiveConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Engine.MediaRecommendationEngineConfig.OptimizationObjectiveConfig)

Custom threshold for `cvr` optimization_objective.

### [RecommendedForYouFeatureConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Engine.MediaRecommendationEngineConfig.RecommendedForYouFeatureConfig)

Additional feature configurations for creating a `recommended-for-you` engine.

### [TrainingState](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Engine.MediaRecommendationEngineConfig.TrainingState)

The training state of the engine.

### [ModelConfigsEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Engine.ModelConfigsEntry)

The abstract base class for a message.

### [ModelState](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Engine.ModelState)

The status of the model for the engine.

### [SearchEngineConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Engine.SearchEngineConfig)

Configurations for a Search Engine.

### [Evaluation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Evaluation)

An evaluation is a single execution (or run) of an evaluation process. It encapsulates the state of the evaluation and the resulting data.

### [EvaluationSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Evaluation.EvaluationSpec)

Describes the specification of the evaluation.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [QuerySetSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Evaluation.EvaluationSpec.QuerySetSpec)

Describes the specification of the query set.

### [State](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Evaluation.State)

Describes the state of an evaluation.

### [FactChunk](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.FactChunk)

Fact Chunk.

### [SourceMetadataEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.FactChunk.SourceMetadataEntry)

The abstract base class for a message.

### [Feedback](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Feedback)

Information about the user feedback. This information will be used for logging and metrics purpose.

### [ConversationInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Feedback.ConversationInfo)

The conversation information such as the question index and session name.

### [FeedbackSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Feedback.FeedbackSource)

Source of the feedback as per integration.

### [FeedbackType](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Feedback.FeedbackType)

The type of the feedback user gives.

### [Reason](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Feedback.Reason)

The reason why user gives a negative feedback.

### [FetchDomainVerificationStatusRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.FetchDomainVerificationStatusRequest)

Request message for SiteSearchEngineService.FetchDomainVerificationStatus method.

### [FetchDomainVerificationStatusResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.FetchDomainVerificationStatusResponse)

Response message for SiteSearchEngineService.FetchDomainVerificationStatus method.

### [FetchSitemapsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.FetchSitemapsRequest)

Request message for SiteSearchEngineService.FetchSitemaps method.

### [Matcher](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.FetchSitemapsRequest.Matcher)

Matcher for the Sitemaps. Currently only supports uris matcher.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [UrisMatcher](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.FetchSitemapsRequest.UrisMatcher)

Matcher for the Sitemaps by their uris.

### [FetchSitemapsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.FetchSitemapsResponse)

Response message for SiteSearchEngineService.FetchSitemaps method.

### [SitemapMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.FetchSitemapsResponse.SitemapMetadata)

Contains a Sitemap and its metadata.

### [FhirStoreSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.FhirStoreSource)

Cloud FhirStore source import data from.

### [FirestoreSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.FirestoreSource)

Firestore source import data from.

### [GcsSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.GcsSource)

Cloud Storage location for input content.

### [GenerateGroundedContentRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.GenerateGroundedContentRequest)

Top-level message sent by the client for the `GenerateGroundedContent` method.

### [DynamicRetrievalConfiguration](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.GenerateGroundedContentRequest.DynamicRetrievalConfiguration)

Describes the options to customize dynamic retrieval.

### [DynamicRetrievalPredictor](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.GenerateGroundedContentRequest.DynamicRetrievalConfiguration.DynamicRetrievalPredictor)

Describes the predictor settings for dynamic retrieval.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Version](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.GenerateGroundedContentRequest.DynamicRetrievalConfiguration.DynamicRetrievalPredictor.Version)

The version of the predictor to be used in dynamic retrieval.

### [GenerationSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.GenerateGroundedContentRequest.GenerationSpec)

Content generation specification.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ProvisionedThroughputSetting](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.GenerateGroundedContentRequest.GenerationSpec.ProvisionedThroughputSetting)

Setting for provisioned throughput.

### [GroundingSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.GenerateGroundedContentRequest.GroundingSource)

Grounding source.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [EnterpriseWebRetrievalSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.GenerateGroundedContentRequest.GroundingSource.EnterpriseWebRetrievalSource)

Params for using enterprise web retrieval as grounding source.

### [GoogleSearchSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.GenerateGroundedContentRequest.GroundingSource.GoogleSearchSource)

Google Search config parameters.

### [InlineSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.GenerateGroundedContentRequest.GroundingSource.InlineSource)

Message to be used for grounding based on inline content.

### [AttributesEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.GenerateGroundedContentRequest.GroundingSource.InlineSource.AttributesEntry)

The abstract base class for a message.

### [SearchSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.GenerateGroundedContentRequest.GroundingSource.SearchSource)

Message to be used for grounding with Vertex AI Search.

### [GroundingSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.GenerateGroundedContentRequest.GroundingSpec)

Grounding specification.

### [UserLabelsEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.GenerateGroundedContentRequest.UserLabelsEntry)

The abstract base class for a message.

### [GenerateGroundedContentResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.GenerateGroundedContentResponse)

Response for the `GenerateGroundedContent` method.

### [Candidate](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.GenerateGroundedContentResponse.Candidate)

A response candidate generated from the model.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [GroundingMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.GenerateGroundedContentResponse.Candidate.GroundingMetadata)

Citation for the generated content.

### [DynamicRetrievalMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.GenerateGroundedContentResponse.Candidate.GroundingMetadata.DynamicRetrievalMetadata)

Describes the metadata about dynamic retrieval.

### [DynamicRetrievalPredictorMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.GenerateGroundedContentResponse.Candidate.GroundingMetadata.DynamicRetrievalPredictorMetadata)

Describes the metadata about the dynamic retrieval predictor.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Version](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.GenerateGroundedContentResponse.Candidate.GroundingMetadata.DynamicRetrievalPredictorMetadata.Version)

The version of the predictor which was used in dynamic retrieval.

### [GroundingSupport](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.GenerateGroundedContentResponse.Candidate.GroundingMetadata.GroundingSupport)

Grounding info for a claim in the candidate and its support.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ImageMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.GenerateGroundedContentResponse.Candidate.GroundingMetadata.ImageMetadata)

Metadata about an image from the web search.

### [Image](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.GenerateGroundedContentResponse.Candidate.GroundingMetadata.ImageMetadata.Image)

Metadata about the image.

### [WebsiteInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.GenerateGroundedContentResponse.Candidate.GroundingMetadata.ImageMetadata.WebsiteInfo)

Metadata about the website that the image is from.

### [RetrievalMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.GenerateGroundedContentResponse.Candidate.GroundingMetadata.RetrievalMetadata)

Describes the metadata associated with a retrieval step.

### [Source](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.GenerateGroundedContentResponse.Candidate.GroundingMetadata.RetrievalMetadata.Source)

Describes the source to which the metadata is associated to.

### [SearchEntryPoint](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.GenerateGroundedContentResponse.Candidate.GroundingMetadata.SearchEntryPoint)

Google search entry point.

### [VideoMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.GenerateGroundedContentResponse.Candidate.GroundingMetadata.VideoMetadata)

Metadata about a video from the web search.

### [GetAclConfigRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.GetAclConfigRequest)

Request message for GetAclConfigRequest method.

### [GetAnswerRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.GetAnswerRequest)

Request for GetAnswer method.

### [GetAssistantRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.GetAssistantRequest)

Request message for the AssistantService.GetAssistant method.

### [GetCmekConfigRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.GetCmekConfigRequest)

Request message for GetCmekConfigRequest method.

### [GetControlRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.GetControlRequest)

Request for GetControl method.

### [GetConversationRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.GetConversationRequest)

Request for GetConversation method.

### [GetDataStoreRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.GetDataStoreRequest)

Request message for DataStoreService.GetDataStore method.

### [GetDocumentRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.GetDocumentRequest)

Request message for DocumentService.GetDocument method.

### [GetEngineRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.GetEngineRequest)

Request message for EngineService.GetEngine method.

### [GetEvaluationRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.GetEvaluationRequest)

Request message for EvaluationService.GetEvaluation method.

### [GetIdentityMappingStoreRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.GetIdentityMappingStoreRequest)

Request message for IdentityMappingStoreService.GetIdentityMappingStore

### [GetLicenseConfigRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.GetLicenseConfigRequest)

Request message for LicenseConfigService.GetLicenseConfig method.

### [GetSampleQueryRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.GetSampleQueryRequest)

Request message for SampleQueryService.GetSampleQuery method.

### [GetSampleQuerySetRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.GetSampleQuerySetRequest)

Request message for SampleQuerySetService.GetSampleQuerySet method.

### [GetSchemaRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.GetSchemaRequest)

Request message for SchemaService.GetSchema method.

### [GetServingConfigRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.GetServingConfigRequest)

Request for GetServingConfig method.

### [GetSessionRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.GetSessionRequest)

Request for GetSession method.

### [GetSiteSearchEngineRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.GetSiteSearchEngineRequest)

Request message for SiteSearchEngineService.GetSiteSearchEngine method.

### [GetTargetSiteRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.GetTargetSiteRequest)

Request message for SiteSearchEngineService.GetTargetSite method.

### [GetUserStoreRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.GetUserStoreRequest)

Request message for UserStoreService.GetUserStore

### [GroundedGenerationContent](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.GroundedGenerationContent)

Base structured datatype containing multi-part content of a message.

### [Part](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.GroundedGenerationContent.Part)

Single part of content.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [GroundingConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.GroundingConfig)

Grounding configuration.

### [GroundingFact](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.GroundingFact)

Grounding Fact.

### [AttributesEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.GroundingFact.AttributesEntry)

The abstract base class for a message.

### [HarmCategory](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.HarmCategory)

Harm categories that will block the content.

### [HealthcareFhirConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.HealthcareFhirConfig)

Config to data store for `HEALTHCARE_FHIR` vertical.

### [IdentityMappingEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.IdentityMappingEntry)

Identity Mapping Entry that maps an external identity to an internal identity.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [IdentityMappingEntryOperationMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.IdentityMappingEntryOperationMetadata)

IdentityMappingEntry LongRunningOperation metadata for IdentityMappingStoreService.ImportIdentityMappings and IdentityMappingStoreService.PurgeIdentityMappings

### [IdentityMappingStore](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.IdentityMappingStore)

Identity Mapping Store which contains Identity Mapping Entries.

### [IdpConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.IdpConfig)

Identity Provider Config.

### [ExternalIdpConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.IdpConfig.ExternalIdpConfig)

Third party IDP Config.

### [IdpType](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.IdpConfig.IdpType)

Identity Provider Type.

### [ImportCompletionSuggestionsMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ImportCompletionSuggestionsMetadata)

Metadata related to the progress of the ImportCompletionSuggestions operation. This will be returned by the google.longrunning.Operation.metadata field.

### [ImportCompletionSuggestionsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ImportCompletionSuggestionsRequest)

Request message for CompletionService.ImportCompletionSuggestions method.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [InlineSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ImportCompletionSuggestionsRequest.InlineSource)

The inline source for CompletionSuggestions.

### [ImportCompletionSuggestionsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ImportCompletionSuggestionsResponse)

Response of the CompletionService.ImportCompletionSuggestions method. If the long running operation is done, this message is returned by the google.longrunning.Operations.response field if the operation is successful.

### [ImportDocumentsMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ImportDocumentsMetadata)

Metadata related to the progress of the ImportDocuments operation. This is returned by the google.longrunning.Operation.metadata field.

### [ImportDocumentsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ImportDocumentsRequest)

Request message for Import methods.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [InlineSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ImportDocumentsRequest.InlineSource)

The inline source for the input config for ImportDocuments method.

### [ReconciliationMode](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ImportDocumentsRequest.ReconciliationMode)

Indicates how imported documents are reconciled with the existing documents created or imported before.

### [ImportDocumentsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ImportDocumentsResponse)

Response of the ImportDocumentsRequest. If the long running operation is done, then this message is returned by the google.longrunning.Operations.response field if the operation was successful.

### [ImportErrorConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ImportErrorConfig)

Configuration of destination for Import related errors.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ImportIdentityMappingsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ImportIdentityMappingsRequest)

Request message for IdentityMappingStoreService.ImportIdentityMappings

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [InlineSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ImportIdentityMappingsRequest.InlineSource)

The inline source to import identity mapping entries from.

### [ImportIdentityMappingsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ImportIdentityMappingsResponse)

Response message for IdentityMappingStoreService.ImportIdentityMappings

### [ImportSampleQueriesMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ImportSampleQueriesMetadata)

Metadata related to the progress of the ImportSampleQueries operation. This will be returned by the google.longrunning.Operation.metadata field.

### [ImportSampleQueriesRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ImportSampleQueriesRequest)

Request message for SampleQueryService.ImportSampleQueries method.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [InlineSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ImportSampleQueriesRequest.InlineSource)

The inline source for SampleQuerys.

### [ImportSampleQueriesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ImportSampleQueriesResponse)

Response of the SampleQueryService.ImportSampleQueries method. If the long running operation is done, this message is returned by the google.longrunning.Operations.response field if the operation is successful.

### [ImportSuggestionDenyListEntriesMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ImportSuggestionDenyListEntriesMetadata)

Metadata related to the progress of the ImportSuggestionDenyListEntries operation. This is returned by the google.longrunning.Operation.metadata field.

### [ImportSuggestionDenyListEntriesRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ImportSuggestionDenyListEntriesRequest)

Request message for CompletionService.ImportSuggestionDenyListEntries method.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [InlineSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ImportSuggestionDenyListEntriesRequest.InlineSource)

The inline source for SuggestionDenyListEntry.

### [ImportSuggestionDenyListEntriesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ImportSuggestionDenyListEntriesResponse)

Response message for CompletionService.ImportSuggestionDenyListEntries method.

### [ImportUserEventsMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ImportUserEventsMetadata)

Metadata related to the progress of the Import operation. This is returned by the google.longrunning.Operation.metadata field.

### [ImportUserEventsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ImportUserEventsRequest)

Request message for the ImportUserEvents request.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [InlineSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ImportUserEventsRequest.InlineSource)

The inline source for the input config for ImportUserEvents method.

### [ImportUserEventsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ImportUserEventsResponse)

Response of the ImportUserEventsRequest. If the long running operation was successful, then this message is returned by the google.longrunning.Operations.response field if the operation was successful.

### [IndustryVertical](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.IndustryVertical)

The industry vertical associated with the DataStore.

### [Interval](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Interval)

A floating point interval.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [LanguageInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.LanguageInfo)

Language info for DataStore.

### [LicenseConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.LicenseConfig)

Information about users' licenses.

### [State](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.LicenseConfig.State)

License config state enumeration.

### [LicenseConfigUsageStats](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.LicenseConfigUsageStats)

Stats about users' licenses.

### [ListAssistantsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListAssistantsRequest)

Request message for the AssistantService.ListAssistants method.

### [ListAssistantsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListAssistantsResponse)

Response message for the AssistantService.ListAssistants method.

### [ListCmekConfigsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListCmekConfigsRequest)

Request message for CmekConfigService.ListCmekConfigs method.

### [ListCmekConfigsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListCmekConfigsResponse)

Response message for CmekConfigService.ListCmekConfigs method.

### [ListControlsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListControlsRequest)

Request for ListControls method.

### [ListControlsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListControlsResponse)

Response for ListControls method.

### [ListConversationsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListConversationsRequest)

Request for ListConversations method.

### [ListConversationsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListConversationsResponse)

Response for ListConversations method.

### [ListCustomModelsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListCustomModelsRequest)

Request message for SearchTuningService.ListCustomModels method.

### [ListCustomModelsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListCustomModelsResponse)

Response message for SearchTuningService.ListCustomModels method.

### [ListDataStoresRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListDataStoresRequest)

Request message for DataStoreService.ListDataStores method.

### [ListDataStoresResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListDataStoresResponse)

Response message for DataStoreService.ListDataStores method.

### [ListDocumentsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListDocumentsRequest)

Request message for DocumentService.ListDocuments method.

### [ListDocumentsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListDocumentsResponse)

Response message for DocumentService.ListDocuments method.

### [ListEnginesRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListEnginesRequest)

Request message for EngineService.ListEngines method.

### [ListEnginesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListEnginesResponse)

Response message for EngineService.ListEngines method.

### [ListEvaluationResultsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListEvaluationResultsRequest)

Request message for EvaluationService.ListEvaluationResults method.

### [ListEvaluationResultsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListEvaluationResultsResponse)

Response message for EvaluationService.ListEvaluationResults method.

### [EvaluationResult](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListEvaluationResultsResponse.EvaluationResult)

Represents the results of an evaluation for a single SampleQuery.

### [ListEvaluationsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListEvaluationsRequest)

Request message for EvaluationService.ListEvaluations method.

### [ListEvaluationsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListEvaluationsResponse)

Response message for EvaluationService.ListEvaluations method.

### [ListIdentityMappingStoresRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListIdentityMappingStoresRequest)

Request message for IdentityMappingStoreService.ListIdentityMappingStores

### [ListIdentityMappingStoresResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListIdentityMappingStoresResponse)

Response message for IdentityMappingStoreService.ListIdentityMappingStores

### [ListIdentityMappingsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListIdentityMappingsRequest)

Request message for IdentityMappingStoreService.ListIdentityMappings

### [ListIdentityMappingsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListIdentityMappingsResponse)

Response message for IdentityMappingStoreService.ListIdentityMappings

### [ListLicenseConfigsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListLicenseConfigsRequest)

Request message for LicenseConfigService.ListLicenseConfigs method.

### [ListLicenseConfigsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListLicenseConfigsResponse)

Response message for LicenseConfigService.ListLicenseConfigs method.

### [ListLicenseConfigsUsageStatsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListLicenseConfigsUsageStatsRequest)

Request message for UserLicenseService.ListLicenseConfigsUsageStats method.

### [ListLicenseConfigsUsageStatsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListLicenseConfigsUsageStatsResponse)

Response message for UserLicenseService.ListLicenseConfigsUsageStats method.

### [ListSampleQueriesRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListSampleQueriesRequest)

Request message for SampleQueryService.ListSampleQueries method.

### [ListSampleQueriesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListSampleQueriesResponse)

Response message for SampleQueryService.ListSampleQueries method.

### [ListSampleQuerySetsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListSampleQuerySetsRequest)

Request message for SampleQuerySetService.ListSampleQuerySets method.

### [ListSampleQuerySetsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListSampleQuerySetsResponse)

Response message for SampleQuerySetService.ListSampleQuerySets method.

### [ListSchemasRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListSchemasRequest)

Request message for SchemaService.ListSchemas method.

### [ListSchemasResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListSchemasResponse)

Response message for SchemaService.ListSchemas method.

### [ListServingConfigsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListServingConfigsRequest)

Request for ListServingConfigs method.

### [ListServingConfigsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListServingConfigsResponse)

Response for ListServingConfigs method.

### [ListSessionsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListSessionsRequest)

Request for ListSessions method.

### [ListSessionsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListSessionsResponse)

Response for ListSessions method.

### [ListTargetSitesRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListTargetSitesRequest)

Request message for SiteSearchEngineService.ListTargetSites method.

### [ListTargetSitesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListTargetSitesResponse)

Response message for SiteSearchEngineService.ListTargetSites method.

### [ListUserLicensesRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListUserLicensesRequest)

Request message for UserLicenseService.ListUserLicenses.

### [ListUserLicensesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListUserLicensesResponse)

Response message for UserLicenseService.ListUserLicenses.

### [MediaInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.MediaInfo)

Media-specific user event information.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [NaturalLanguageQueryUnderstandingConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.NaturalLanguageQueryUnderstandingConfig)

Configuration for Natural Language Query Understanding.

### [Mode](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.NaturalLanguageQueryUnderstandingConfig.Mode)

Mode of Natural Language Query Understanding. When the NaturalLanguageQueryUnderstandingConfig.Mode is ENABLED, the natural language understanding capabilities will be enabled for a search request if the NaturalLanguageQueryUnderstandingSpec.FilterExtractionCondition in the SearchRequest is ENABLED.

### [ObservabilityConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ObservabilityConfig)

Observability config for a resource.

### [PageInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.PageInfo)

Detailed page information.

### [PanelInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.PanelInfo)

Detailed panel information associated with a user event.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [PauseEngineRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.PauseEngineRequest)

Request for pausing training of an engine.

### [Principal](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Principal)

Principal identifier of a user or a group.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Project](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Project)

Metadata and configurations for a Google Cloud project in the service.

### [ConfigurableBillingStatus](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Project.ConfigurableBillingStatus)

Represents the currently effective configurable billing parameters. These values are derived from the customer's subscription history stored internally and reflect the thresholds actively being used for billing purposes at the time of the GetProject call. This includes the start_time of the subscription and may differ from the values in `customer_provided_config` due to billing rules (e.g., scale-downs taking effect only at the start of a new month). We also include the update type to indicate the type of update performed on the configurable billing configuration in the UpdateProject operation.

### [AgentSearchTokenSubscriptionStatus](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Project.ConfigurableBillingStatus.AgentSearchTokenSubscriptionStatus)

Per-model Agent Search TPM subscription status. One entry per active `core_subscription.agent_search_token_subscriptions[*]` entry in the customer-provided config; populated by UpdateProject and GetProject.

The lifecycle scalars on this message (`start_time`, `terminate_time`, `update_type`, `tpm_threshold_next_update_time`) are per (project, model_version) — siblings of the whole-relationship `start_time` / `terminate_time` / `update_type` on the enclosing ConfigurableBillingStatus, but scoped to this specific Agent Search TPM subscription instead of to the overall customer-configurable- pricing relationship. This per-instance granularity is intentional: the underlying SubV3 storage is per-(project, model_version), so each model has its own activation, termination, and deferred-update clock; surfacing that on the response gives customers the granularity they need to manage per-model commitments independently. QPM / IndexingCore differ — their storage is one row per (project, location), so their lifecycle is represented only by the whole- relationship scalars on ConfigurableBillingStatus.

### [UpdateType](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Project.ConfigurableBillingStatus.UpdateType)

The type of update performed on the configurable billing configuration.

### [CustomerProvidedConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Project.CustomerProvidedConfig)

Customer provided configurations.

### [NotebooklmConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Project.CustomerProvidedConfig.NotebooklmConfig)

Configuration for NotebookLM.

### [DataProtectionPolicy](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Project.CustomerProvidedConfig.NotebooklmConfig.DataProtectionPolicy)

Data protection policy config for NotebookLM.

### [SensitiveDataProtectionPolicy](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Project.CustomerProvidedConfig.NotebooklmConfig.DataProtectionPolicy.SensitiveDataProtectionPolicy)

Specifies a Sensitive Data Protection (<https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview>) policy.

### [ModelArmorConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Project.CustomerProvidedConfig.NotebooklmConfig.ModelArmorConfig)

Configuration for customer defined Model Armor templates to be used for sanitizing user prompts and LLM responses.

### [ServiceTerms](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Project.ServiceTerms)

Metadata about the terms of service.

### [State](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Project.ServiceTerms.State)

The agreement states this terms of service.

### [ServiceTermsMapEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Project.ServiceTermsMapEntry)

The abstract base class for a message.

### [ProvisionProjectMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ProvisionProjectMetadata)

Metadata associated with a project provision operation.

### [ProvisionProjectRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ProvisionProjectRequest)

Request for ProjectService.ProvisionProject method.

### [SaasParams](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ProvisionProjectRequest.SaasParams)

Parameters for Agentspace.

### [PurgeCompletionSuggestionsMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.PurgeCompletionSuggestionsMetadata)

Metadata related to the progress of the PurgeCompletionSuggestions operation. This is returned by the google.longrunning.Operation.metadata field.

### [PurgeCompletionSuggestionsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.PurgeCompletionSuggestionsRequest)

Request message for CompletionService.PurgeCompletionSuggestions method.

### [PurgeCompletionSuggestionsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.PurgeCompletionSuggestionsResponse)

Response message for CompletionService.PurgeCompletionSuggestions method.

### [PurgeDocumentsMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.PurgeDocumentsMetadata)

Metadata related to the progress of the PurgeDocuments operation. This will be returned by the google.longrunning.Operation.metadata field.

### [PurgeDocumentsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.PurgeDocumentsRequest)

Request message for DocumentService.PurgeDocuments method.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [InlineSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.PurgeDocumentsRequest.InlineSource)

The inline source for the input config for DocumentService.PurgeDocuments method.

### [PurgeDocumentsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.PurgeDocumentsResponse)

Response message for DocumentService.PurgeDocuments method. If the long running operation is successfully done, then this message is returned by the google.longrunning.Operations.response field.

### [PurgeErrorConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.PurgeErrorConfig)

Configuration of destination for Purge related errors.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [PurgeIdentityMappingsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.PurgeIdentityMappingsRequest)

Request message for IdentityMappingStoreService.PurgeIdentityMappings

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [InlineSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.PurgeIdentityMappingsRequest.InlineSource)

The inline source to purge identity mapping entries from.

### [PurgeSuggestionDenyListEntriesMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.PurgeSuggestionDenyListEntriesMetadata)

Metadata related to the progress of the PurgeSuggestionDenyListEntries operation. This is returned by the google.longrunning.Operation.metadata field.

### [PurgeSuggestionDenyListEntriesRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.PurgeSuggestionDenyListEntriesRequest)

Request message for CompletionService.PurgeSuggestionDenyListEntries method.

### [PurgeSuggestionDenyListEntriesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.PurgeSuggestionDenyListEntriesResponse)

Response message for CompletionService.PurgeSuggestionDenyListEntries method.

### [PurgeUserEventsMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.PurgeUserEventsMetadata)

Metadata related to the progress of the PurgeUserEvents operation. This will be returned by the google.longrunning.Operation.metadata field.

### [PurgeUserEventsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.PurgeUserEventsRequest)

Request message for PurgeUserEvents method.

### [PurgeUserEventsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.PurgeUserEventsResponse)

Response of the PurgeUserEventsRequest. If the long running operation is successfully done, then this message is returned by the google.longrunning.Operations.response field.

### [QualityMetrics](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.QualityMetrics)

Describes the metrics produced by the evaluation.

### [TopkMetrics](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.QualityMetrics.TopkMetrics)

Stores the metric values at specific top-k levels.

### [Query](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Query)

Defines a user inputed query.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [RankRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.RankRequest)

Request message for RankService.Rank method.

### [UserLabelsEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.RankRequest.UserLabelsEntry)

The abstract base class for a message.

### [RankResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.RankResponse)

Response message for RankService.Rank method.

### [RankingRecord](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.RankingRecord)

Record message for RankService.Rank method.

### [RecommendRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.RecommendRequest)

Request message for Recommend method.

### [ParamsEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.RecommendRequest.ParamsEntry)

The abstract base class for a message.

### [UserLabelsEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.RecommendRequest.UserLabelsEntry)

The abstract base class for a message.

### [RecommendResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.RecommendResponse)

Response message for Recommend method.

### [RecommendationResult](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.RecommendResponse.RecommendationResult)

RecommendationResult represents a generic recommendation result with associated metadata.

### [MetadataEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.RecommendResponse.RecommendationResult.MetadataEntry)

The abstract base class for a message.

### [RecrawlUrisMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.RecrawlUrisMetadata)

Metadata related to the progress of the SiteSearchEngineService.RecrawlUris operation. This will be returned by the google.longrunning.Operation.metadata field.

### [RecrawlUrisRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.RecrawlUrisRequest)

Request message for SiteSearchEngineService.RecrawlUris method.

### [RecrawlUrisResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.RecrawlUrisResponse)

Response message for SiteSearchEngineService.RecrawlUris method.

### [FailureInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.RecrawlUrisResponse.FailureInfo)

Details about why a particular URI failed to be crawled. Each FailureInfo contains one FailureReason per CorpusType.

### [FailureReason](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.RecrawlUrisResponse.FailureInfo.FailureReason)

Details about why crawling failed for a particular CorpusType, e.g., DESKTOP and MOBILE crawling may fail for different reasons.

### [CorpusType](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.RecrawlUrisResponse.FailureInfo.FailureReason.CorpusType)

CorpusType for the failed crawling operation.

### [RemoveSuggestionRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.RemoveSuggestionRequest)

Request message for CompletionService.RemoveSuggestion method.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [RemoveSuggestionResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.RemoveSuggestionResponse)

Response message for CompletionService.RemoveSuggestion method.

### [Reply](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Reply)

Defines a reply message to user.

### [Reference](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Reply.Reference)

Defines reference in reply.

### [ResumeEngineRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ResumeEngineRequest)

Request for resuming training of an engine.

### [RetractLicenseConfigRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.RetractLicenseConfigRequest)

Request message for LicenseConfigService.RetractLicenseConfig method.

### [RetractLicenseConfigResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.RetractLicenseConfigResponse)

Response message for LicenseConfigService.RetractLicenseConfig method.

### [SafetyRating](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SafetyRating)

Safety rating corresponding to the generated content.

### [HarmProbability](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SafetyRating.HarmProbability)

Harm probability levels in the content.

### [HarmSeverity](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SafetyRating.HarmSeverity)

Harm severity levels.

### [SampleQuery](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SampleQuery)

Sample Query captures metadata to be used for evaluation.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [QueryEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SampleQuery.QueryEntry)

Query Entry captures metadata to be used for search evaluation.

### [Target](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SampleQuery.QueryEntry.Target)

Defines the parameters of the query's expected outcome.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [SampleQuerySet](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SampleQuerySet)

A SampleQuerySet is the parent resource of SampleQuery, and contains the configurations shared by all SampleQuery under it.

### [Schema](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Schema)

Defines the structure and layout of a type of document data.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [SearchAddOn](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchAddOn)

Add-on that provides additional functionality for search.

### [SearchInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchInfo)

Detailed search information.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [SearchLinkPromotion](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchLinkPromotion)

Promotion proto includes uri and other helping information to display the promotion.

### [SearchRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchRequest)

Request message for SearchService.Search method.

### [BoostSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchRequest.BoostSpec)

Boost specification to boost certain documents.

### [ConditionBoostSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchRequest.BoostSpec.ConditionBoostSpec)

Boost applies to documents which match a condition.

### [BoostControlSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchRequest.BoostSpec.ConditionBoostSpec.BoostControlSpec)

Specification for custom ranking based on customer specified attribute value. It provides more controls for customized ranking than the simple (condition, boost) combination above.

### [AttributeType](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchRequest.BoostSpec.ConditionBoostSpec.BoostControlSpec.AttributeType)

The attribute(or function) for which the custom ranking is to be applied.

### [ControlPoint](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchRequest.BoostSpec.ConditionBoostSpec.BoostControlSpec.ControlPoint)

The control points used to define the curve. The curve defined through these control points can only be monotonically increasing or decreasing(constant values are acceptable).

### [InterpolationType](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchRequest.BoostSpec.ConditionBoostSpec.BoostControlSpec.InterpolationType)

The interpolation type to be applied. Default will be linear (Piecewise Linear).

### [ContentSearchSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchRequest.ContentSearchSpec)

A specification for configuring the behavior of content search.

### [ChunkSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchRequest.ContentSearchSpec.ChunkSpec)

Specifies the chunk spec to be returned from the search response. Only available if the SearchRequest.ContentSearchSpec.search_result_mode is set to CHUNKS

### [ExtractiveContentSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchRequest.ContentSearchSpec.ExtractiveContentSpec)

A specification for configuring the extractive content in a search response.

### [SearchResultMode](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchRequest.ContentSearchSpec.SearchResultMode)

Specifies the search result mode. If unspecified, the search result mode defaults to `DOCUMENTS`.

### [SnippetSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchRequest.ContentSearchSpec.SnippetSpec)

A specification for configuring snippets in a search response.

### [SummarySpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchRequest.ContentSearchSpec.SummarySpec)

A specification for configuring a summary returned in a search response.

### [ModelPromptSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchRequest.ContentSearchSpec.SummarySpec.ModelPromptSpec)

Specification of the prompt to use with the model.

### [ModelSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchRequest.ContentSearchSpec.SummarySpec.ModelSpec)

Specification of the model.

### [MultiModalSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchRequest.ContentSearchSpec.SummarySpec.MultiModalSpec)

Multimodal specification: Will return an image from specified source. If multiple sources are specified, the pick is a quality based decision.

### [ImageSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchRequest.ContentSearchSpec.SummarySpec.MultiModalSpec.ImageSource)

Specifies the image source.

### [CrowdingSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchRequest.CrowdingSpec)

Specification for crowding. Crowding improves the diversity of search results by limiting the number of results that share the same field value. For example, crowding on the color field with a max_count of 3 and mode DROP_CROWDED_RESULTS will return at most 3 results with the same color across all pages.

### [Mode](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchRequest.CrowdingSpec.Mode)

Enum describing the mode to use for documents that are crowded away. They can be dropped or demoted to the later pages.

### [CustomRankingParams](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchRequest.CustomRankingParams)

Configuration parameters for the Custom Ranking feature.

### [DataStoreSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchRequest.DataStoreSpec)

A struct to define data stores to filter on in a search call and configurations for those data stores. Otherwise, an `INVALID_ARGUMENT` error is returned.

### [DisplaySpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchRequest.DisplaySpec)

Specifies features for display, like match highlighting.

### [MatchHighlightingCondition](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchRequest.DisplaySpec.MatchHighlightingCondition)

Enum describing under which condition match highlighting should occur.

### [EmbeddingSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchRequest.EmbeddingSpec)

The specification that uses customized query embedding vector to do semantic document retrieval.

### [EmbeddingVector](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchRequest.EmbeddingSpec.EmbeddingVector)

Embedding vector.

### [FacetSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchRequest.FacetSpec)

A facet specification to perform faceted search.

### [FacetKey](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchRequest.FacetSpec.FacetKey)

Specifies how a facet is computed.

### [ImageQuery](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchRequest.ImageQuery)

Specifies the image query input.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [NaturalLanguageQueryUnderstandingSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchRequest.NaturalLanguageQueryUnderstandingSpec)

Specification to enable natural language understanding capabilities for search requests.

### [ExtractedFilterBehavior](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchRequest.NaturalLanguageQueryUnderstandingSpec.ExtractedFilterBehavior)

Enum describing how extracted filters are applied to the search.

### [FilterExtractionCondition](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchRequest.NaturalLanguageQueryUnderstandingSpec.FilterExtractionCondition)

Enum describing under which condition filter extraction should occur.

### [ParamsEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchRequest.ParamsEntry)

The abstract base class for a message.

### [PersonalizationSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchRequest.PersonalizationSpec)

The specification for personalization.

### [Mode](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchRequest.PersonalizationSpec.Mode)

The personalization mode of each search request.

### [QueryExpansionSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchRequest.QueryExpansionSpec)

Specification to determine under which conditions query expansion should occur.

### [Condition](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchRequest.QueryExpansionSpec.Condition)

Enum describing under which condition query expansion should occur.

### [RankingExpressionBackend](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchRequest.RankingExpressionBackend)

The backend to use for the ranking expression evaluation.

### [RelevanceFilterSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchRequest.RelevanceFilterSpec)

Relevance filtering specification.

### [RelevanceThresholdSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchRequest.RelevanceFilterSpec.RelevanceThresholdSpec)

Specification for relevance filtering on a specific sub-search.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [RelevanceScoreSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchRequest.RelevanceScoreSpec)

The specification for returning the document relevance score.

### [RelevanceThreshold](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchRequest.RelevanceThreshold)

The relevance threshold of the search results. The higher relevance threshold is, the higher relevant results are shown and the less number of results are returned.

### [SearchAddonSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchRequest.SearchAddonSpec)

SearchAddonSpec is used to disable add-ons for search as per new repricing model. By default if the SearchAddonSpec is not specified, we consider that the customer wants to enable them wherever applicable.

### [SearchAsYouTypeSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchRequest.SearchAsYouTypeSpec)

Specification for search as you type in search requests.

### [Condition](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchRequest.SearchAsYouTypeSpec.Condition)

Enum describing under which condition search as you type should occur.

### [SessionSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchRequest.SessionSpec)

Session specification.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [SpellCorrectionSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchRequest.SpellCorrectionSpec)

The specification for query spell correction.

### [Mode](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchRequest.SpellCorrectionSpec.Mode)

Enum describing under which mode spell correction should occur.

### [UserLabelsEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchRequest.UserLabelsEntry)

The abstract base class for a message.

### [SearchResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchResponse)

Response message for SearchService.Search method.

### [Facet](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchResponse.Facet)

A facet result.

### [FacetValue](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchResponse.Facet.FacetValue)

A facet value which contains value names and their count.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [GeoSearchDebugInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchResponse.GeoSearchDebugInfo)

Debug information specifically related to forward geocoding issues arising from Geolocation Search.

### [GuidedSearchResult](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchResponse.GuidedSearchResult)

Guided search result. The guided search helps user to refine the search results and narrow down to the real needs from a broaded search results.

### [RefinementAttribute](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchResponse.GuidedSearchResult.RefinementAttribute)

Useful attribute for search result refinements.

### [NaturalLanguageQueryUnderstandingInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchResponse.NaturalLanguageQueryUnderstandingInfo)

Information describing what natural language understanding was done on the input query.

### [StructuredExtractedFilter](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchResponse.NaturalLanguageQueryUnderstandingInfo.StructuredExtractedFilter)

The filters that were extracted from the input query represented in a structured form.

### [AndExpression](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchResponse.NaturalLanguageQueryUnderstandingInfo.StructuredExtractedFilter.AndExpression)

Logical `And` operator.

### [Expression](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchResponse.NaturalLanguageQueryUnderstandingInfo.StructuredExtractedFilter.Expression)

The expression denoting the filter that was extracted from the input query.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [GeolocationConstraint](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchResponse.NaturalLanguageQueryUnderstandingInfo.StructuredExtractedFilter.GeolocationConstraint)

Constraint of a geolocation field. Name of the geolocation field as defined in the schema.

### [NumberConstraint](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchResponse.NaturalLanguageQueryUnderstandingInfo.StructuredExtractedFilter.NumberConstraint)

Constraint expression of a number field. Example: price < 100.

### [Comparison](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchResponse.NaturalLanguageQueryUnderstandingInfo.StructuredExtractedFilter.NumberConstraint.Comparison)

The comparison operation that was performed.

### [OrExpression](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchResponse.NaturalLanguageQueryUnderstandingInfo.StructuredExtractedFilter.OrExpression)

Logical `Or` operator.

### [StringConstraint](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchResponse.NaturalLanguageQueryUnderstandingInfo.StructuredExtractedFilter.StringConstraint)

Constraint expression of a string field.

### [OneBoxResult](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchResponse.OneBoxResult)

OneBoxResult is a holder for all results of specific type that we want to display in UI differently.

### [OneBoxType](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchResponse.OneBoxResult.OneBoxType)

The type of One Box result.

### [QueryExpansionInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchResponse.QueryExpansionInfo)

Information describing query expansion including whether expansion has occurred.

### [SearchResult](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchResponse.SearchResult)

Represents the search results.

### [ModelScoresEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchResponse.SearchResult.ModelScoresEntry)

The abstract base class for a message.

### [RankSignals](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchResponse.SearchResult.RankSignals)

A set of ranking signals.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [CustomSignal](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchResponse.SearchResult.RankSignals.CustomSignal)

Custom clearbox signal represented by name and value pair.

### [SemanticState](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchResponse.SemanticState)

Semantic state of the search response.

### [SessionInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchResponse.SessionInfo)

Information about the session.

### [Summary](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchResponse.Summary)

Summary of the top N search results specified by the summary spec.

### [BlobAttachment](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchResponse.Summary.BlobAttachment)

Stores binarydata attached to text answer, e.g. image, video, audio, etc.

### [AttributionType](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchResponse.Summary.BlobAttachment.AttributionType)

Defines the attribution type of the blob.

### [Blob](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchResponse.Summary.BlobAttachment.Blob)

Stores type and data of the blob.

### [Citation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchResponse.Summary.Citation)

Citation info for a segment.

### [CitationMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchResponse.Summary.CitationMetadata)

Citation metadata.

### [CitationSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchResponse.Summary.CitationSource)

Citation source.

### [Reference](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchResponse.Summary.Reference)

Document reference.

### [ChunkContent](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchResponse.Summary.Reference.ChunkContent)

Chunk content.

### [SafetyAttributes](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchResponse.Summary.SafetyAttributes)

Safety Attribute categories and their associated confidence scores.

### [SummarySkippedReason](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchResponse.Summary.SummarySkippedReason)

An Enum for summary-skipped reasons.
    
    
        Only used when
        <xref uid="google.cloud.discoveryengine.v1beta.SearchRequest.ContentSearchSpec.SummarySpec.ignore_adversarial_query">SummarySpec.ignore_adversarial_query</xref>
        is set to `true`.
    NON_SUMMARY_SEEKING_QUERY_IGNORED (2):
        The non-summary seeking query ignored case.
    
        Google skips the summary if the query is chit chat. Only
        used when
        <xref uid="google.cloud.discoveryengine.v1beta.SearchRequest.ContentSearchSpec.SummarySpec.ignore_non_summary_seeking_query">SummarySpec.ignore_non_summary_seeking_query</xref>
        is set to `true`.
    OUT_OF_DOMAIN_QUERY_IGNORED (3):
        The out-of-domain query ignored case.
    
        Google skips the summary if there are no
        high-relevance search results. For example, the
        data store contains facts about company A but
        the user query is asking questions about company
        B.
    POTENTIAL_POLICY_VIOLATION (4):
        The potential policy violation case.
    
        Google skips the summary if there is a potential
        policy violation detected. This includes content
        that may be violent or toxic.
    LLM_ADDON_NOT_ENABLED (5):
        The LLM addon not enabled case.
    
        Google skips the summary if the LLM addon is not
        enabled.
    NO_RELEVANT_CONTENT (6):
        The no relevant content case.
    
        Google skips the summary if there is no relevant
        content in the retrieved search results.
    JAIL_BREAKING_QUERY_IGNORED (7):
        The jail-breaking query ignored case.
    
        For example, "Reply in the tone of a competing company's
        CEO". Only used when
        [SearchRequest.ContentSearchSpec.SummarySpec.ignore_jail_breaking_query]
        is set to `true`.
    CUSTOMER_POLICY_VIOLATION (8):
        The customer policy violation case.
    
        Google skips the summary if there is a customer
        policy violation detected. The policy is defined
        by the customer.
    NON_SUMMARY_SEEKING_QUERY_IGNORED_V2 (9):
        The non-answer seeking query ignored case.
    
        Google skips the summary if the query doesn't have clear
        intent. Only used when
        [SearchRequest.ContentSearchSpec.SummarySpec.ignore_non_answer_seeking_query]
        is set to `true`.
    TIME_OUT (10):
        The time out case.
    
        Google skips the summary if the time out.
    

### [SummaryWithMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchResponse.Summary.SummaryWithMetadata)

Summary with metadata information.

### [SearchTier](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchTier)

Tiers of search features. Different tiers might have different pricing. To learn more, check the pricing documentation.

### [SearchUseCase](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SearchUseCase)

Defines a further subdivision of `SolutionType`. Specifically applies to SOLUTION_TYPE_SEARCH.

### [ServingConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ServingConfig)

Configures metadata that is used to generate serving time results (e.g. search results or recommendation predictions). The ServingConfig is passed in the search and predict request and generates results.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [GenericConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ServingConfig.GenericConfig)

Specifies the configurations needed for Generic Discovery.Currently we support:

  * `content_search_spec`: configuration for generic content search.



### [MediaConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ServingConfig.MediaConfig)

Specifies the configurations needed for Media Discovery. Currently we support:

  * `demote_content_watched`: Threshold for watched content demotion. Customers can specify if using watched content demotion or use viewed detail page. Using the content watched demotion, customers need to specify the watched minutes or percentage exceeds the threshold, the content will be demoted in the recommendation result.
  * `promote_fresh_content`: cutoff days for fresh content promotion. Customers can specify if using content freshness promotion. If the content was published within the cutoff days, the content will be promoted in the recommendation result. Can only be set if SolutionType is SOLUTION_TYPE_RECOMMENDATION.



This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Session](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Session)

External session proto definition.

### [State](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Session.State)

Enumeration of the state of the session.

### [Turn](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Session.Turn)

Represents a turn, including a query from the user and a answer from service.

### [QueryConfigEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Session.Turn.QueryConfigEntry)

The abstract base class for a message.

### [SingleRegionKey](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SingleRegionKey)

Metadata for single-regional CMEKs.

### [SiteSearchEngine](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SiteSearchEngine)

SiteSearchEngine captures DataStore level site search persisting configurations. It is a singleton value per data store.

### [SiteVerificationInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SiteVerificationInfo)

Verification information for target sites in advanced site search.

### [SiteVerificationState](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SiteVerificationInfo.SiteVerificationState)

Site verification state.

### [Sitemap](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.Sitemap)

A sitemap for the SiteSearchEngine.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [SolutionType](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SolutionType)

The type of solution.

### [SpannerSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SpannerSource)

The Spanner source for importing data

### [StreamAssistRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.StreamAssistRequest)

Request for the AssistantService.StreamAssist method.

### [AgentsSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.StreamAssistRequest.AgentsSpec)

Specification of agents that are used to serve the request.

### [AgentSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.StreamAssistRequest.AgentsSpec.AgentSpec)

Specification of an agent.

### [GenerationSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.StreamAssistRequest.GenerationSpec)

Assistant generation specification for the request. This allows to override the default generation configuration at the engine level.

### [ToolsSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.StreamAssistRequest.ToolsSpec)

Specification of tools that are used to serve the request.

### [ImageGenerationSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.StreamAssistRequest.ToolsSpec.ImageGenerationSpec)

Specification of the image generation tool.

### [VertexAiSearchSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.StreamAssistRequest.ToolsSpec.VertexAiSearchSpec)

Specification of the Vertex AI Search tool.

### [VideoGenerationSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.StreamAssistRequest.ToolsSpec.VideoGenerationSpec)

Specification of the video generation tool.

### [WebGroundingSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.StreamAssistRequest.ToolsSpec.WebGroundingSpec)

Specification of the web grounding tool.

### [StreamAssistResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.StreamAssistResponse)

Response for the AssistantService.StreamAssist method.

### [InvokedSkill](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.StreamAssistResponse.InvokedSkill)

Represents a skill used during the assist call.

### [SessionInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.StreamAssistResponse.SessionInfo)

Information about the session.

### [SubscriptionTerm](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SubscriptionTerm)

Subscription term.

### [SubscriptionTier](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SubscriptionTier)

Subscription tier information.

### [SuggestionDenyListEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SuggestionDenyListEntry)

Suggestion deny list entry identifying the phrase to block from suggestions and the applied operation for the phrase.

### [MatchOperator](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.SuggestionDenyListEntry.MatchOperator)

Operator for matching with the generated suggestions.

### [TargetSite](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.TargetSite)

A target site for the SiteSearchEngine.

### [FailureReason](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.TargetSite.FailureReason)

Site search indexing failure reasons.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [QuotaFailure](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.TargetSite.FailureReason.QuotaFailure)

Failed due to insufficient quota.

### [IndexingStatus](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.TargetSite.IndexingStatus)

Target site indexing status enumeration.
    
    
        1. target site deleted if unindexing is
            successful;
        2. state reverts to SUCCEEDED if the unindexing
            fails.
    CANCELLABLE (5):
        The target site change is pending but
        cancellable.
    CANCELLED (6):
        The target site change is cancelled.
    

### [Type](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.TargetSite.Type)

Possible target site types.

### [TextInput](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.TextInput)

Defines text input.

### [TrainCustomModelMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.TrainCustomModelMetadata)

Metadata related to the progress of the TrainCustomModel operation. This is returned by the google.longrunning.Operation.metadata field.

### [TrainCustomModelRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.TrainCustomModelRequest)

Request message for SearchTuningService.TrainCustomModel method.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [GcsTrainingInput](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.TrainCustomModelRequest.GcsTrainingInput)

Cloud Storage training data input.

### [TrainCustomModelResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.TrainCustomModelResponse)

Response of the TrainCustomModelRequest. This message is returned by the google.longrunning.Operations.response field.

### [MetricsEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.TrainCustomModelResponse.MetricsEntry)

The abstract base class for a message.

### [TransactionInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.TransactionInfo)

A transaction represents the entire purchase transaction.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [TuneEngineMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.TuneEngineMetadata)

Metadata associated with a tune operation.

### [TuneEngineRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.TuneEngineRequest)

Request to manually start a tuning process now (instead of waiting for the periodically scheduled tuning to happen).

### [TuneEngineResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.TuneEngineResponse)

Response associated with a tune operation.

### [UpdateAclConfigRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.UpdateAclConfigRequest)

Request message for UpdateAclConfig method.

### [UpdateAssistantRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.UpdateAssistantRequest)

Request message for the AssistantService.UpdateAssistant method.

### [UpdateCmekConfigMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.UpdateCmekConfigMetadata)

Metadata related to the progress of the CmekConfigService.UpdateCmekConfig operation. This will be returned by the google.longrunning.Operation.metadata field.

### [UpdateCmekConfigRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.UpdateCmekConfigRequest)

Request message for UpdateCmekConfig method. rpc.

### [UpdateControlRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.UpdateControlRequest)

Request for UpdateControl method.

### [UpdateConversationRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.UpdateConversationRequest)

Request for UpdateConversation method.

### [UpdateDataStoreRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.UpdateDataStoreRequest)

Request message for DataStoreService.UpdateDataStore method.

### [UpdateDocumentRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.UpdateDocumentRequest)

Request message for DocumentService.UpdateDocument method.

### [UpdateEngineRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.UpdateEngineRequest)

Request message for EngineService.UpdateEngine method.

### [UpdateLicenseConfigRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.UpdateLicenseConfigRequest)

Request message for LicenseConfigService.UpdateLicenseConfig method.

### [UpdateSampleQueryRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.UpdateSampleQueryRequest)

Request message for SampleQueryService.UpdateSampleQuery method.

### [UpdateSampleQuerySetRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.UpdateSampleQuerySetRequest)

Request message for SampleQuerySetService.UpdateSampleQuerySet method.

### [UpdateSchemaMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.UpdateSchemaMetadata)

Metadata for UpdateSchema LRO.

### [UpdateSchemaRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.UpdateSchemaRequest)

Request message for SchemaService.UpdateSchema method.

### [UpdateServingConfigRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.UpdateServingConfigRequest)

Request for UpdateServingConfig method.

### [UpdateSessionRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.UpdateSessionRequest)

Request for UpdateSession method.

### [UpdateTargetSiteMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.UpdateTargetSiteMetadata)

Metadata related to the progress of the SiteSearchEngineService.UpdateTargetSite operation. This will be returned by the google.longrunning.Operation.metadata field.

### [UpdateTargetSiteRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.UpdateTargetSiteRequest)

Request message for SiteSearchEngineService.UpdateTargetSite method.

### [UpdateUserStoreRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.UpdateUserStoreRequest)

Request message for UserStoreService.UpdateUserStore method.

### [UserEvent](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.UserEvent)

UserEvent captures all metadata information Discovery Engine API needs to know about how end users interact with your website.

### [AttributesEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.UserEvent.AttributesEntry)

The abstract base class for a message.

### [UserInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.UserInfo)

Information of an end user.

### [PreciseLocation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.UserInfo.PreciseLocation)

Precise location info with multiple representation options. Currently only latitude and longitude point is supported.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [UserLicense](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.UserLicense)

User License information assigned by the admin.

### [LicenseAssignmentState](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.UserLicense.LicenseAssignmentState)

License assignment state enumeration.

### [UserStore](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.UserStore)

Configures metadata that is used for End User entities.

### [WorkspaceConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.WorkspaceConfig)

Config to store data store type configuration for workspace data

### [Type](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.WorkspaceConfig.Type)

Specifies the type of Workspace App supported by this DataStore

### [WriteUserEventRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.WriteUserEventRequest)

Request message for WriteUserEvent method.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Modules 

### [pagers](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.control_service.pagers)

API documentation for `discoveryengine_v1.services.control_service.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.conversational_search_service.pagers)

API documentation for `discoveryengine_v1.services.conversational_search_service.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.data_store_service.pagers)

API documentation for `discoveryengine_v1.services.data_store_service.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.document_service.pagers)

API documentation for `discoveryengine_v1.services.document_service.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.engine_service.pagers)

API documentation for `discoveryengine_v1.services.engine_service.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.identity_mapping_store_service.pagers)

API documentation for `discoveryengine_v1.services.identity_mapping_store_service.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.schema_service.pagers)

API documentation for `discoveryengine_v1.services.schema_service.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.search_service.pagers)

API documentation for `discoveryengine_v1.services.search_service.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.session_service.pagers)

API documentation for `discoveryengine_v1.services.session_service.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.site_search_engine_service.pagers)

API documentation for `discoveryengine_v1.services.site_search_engine_service.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.user_license_service.pagers)

API documentation for `discoveryengine_v1.services.user_license_service.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.chunk_service.pagers)

API documentation for `discoveryengine_v1alpha.services.chunk_service.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.control_service.pagers)

API documentation for `discoveryengine_v1alpha.services.control_service.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.conversational_search_service.pagers)

API documentation for `discoveryengine_v1alpha.services.conversational_search_service.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.data_store_service.pagers)

API documentation for `discoveryengine_v1alpha.services.data_store_service.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.document_service.pagers)

API documentation for `discoveryengine_v1alpha.services.document_service.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.engine_service.pagers)

API documentation for `discoveryengine_v1alpha.services.engine_service.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.evaluation_service.pagers)

API documentation for `discoveryengine_v1alpha.services.evaluation_service.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.sample_query_service.pagers)

API documentation for `discoveryengine_v1alpha.services.sample_query_service.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.sample_query_set_service.pagers)

API documentation for `discoveryengine_v1alpha.services.sample_query_set_service.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.schema_service.pagers)

API documentation for `discoveryengine_v1alpha.services.schema_service.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.search_service.pagers)

API documentation for `discoveryengine_v1alpha.services.search_service.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.serving_config_service.pagers)

API documentation for `discoveryengine_v1alpha.services.serving_config_service.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.session_service.pagers)

API documentation for `discoveryengine_v1alpha.services.session_service.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.services.site_search_engine_service.pagers)

API documentation for `discoveryengine_v1alpha.services.site_search_engine_service.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.assistant_service.pagers)

API documentation for `discoveryengine_v1beta.services.assistant_service.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.control_service.pagers)

API documentation for `discoveryengine_v1beta.services.control_service.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.conversational_search_service.pagers)

API documentation for `discoveryengine_v1beta.services.conversational_search_service.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.data_store_service.pagers)

API documentation for `discoveryengine_v1beta.services.data_store_service.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.document_service.pagers)

API documentation for `discoveryengine_v1beta.services.document_service.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.engine_service.pagers)

API documentation for `discoveryengine_v1beta.services.engine_service.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.evaluation_service.pagers)

API documentation for `discoveryengine_v1beta.services.evaluation_service.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.identity_mapping_store_service.pagers)

API documentation for `discoveryengine_v1beta.services.identity_mapping_store_service.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.license_config_service.pagers)

API documentation for `discoveryengine_v1beta.services.license_config_service.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.sample_query_service.pagers)

API documentation for `discoveryengine_v1beta.services.sample_query_service.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.sample_query_set_service.pagers)

API documentation for `discoveryengine_v1beta.services.sample_query_set_service.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.schema_service.pagers)

API documentation for `discoveryengine_v1beta.services.schema_service.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.search_service.pagers)

API documentation for `discoveryengine_v1beta.services.search_service.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.serving_config_service.pagers)

API documentation for `discoveryengine_v1beta.services.serving_config_service.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.session_service.pagers)

API documentation for `discoveryengine_v1beta.services.session_service.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.site_search_engine_service.pagers)

API documentation for `discoveryengine_v1beta.services.site_search_engine_service.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.services.user_license_service.pagers)

API documentation for `discoveryengine_v1beta.services.user_license_service.pagers` module.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
