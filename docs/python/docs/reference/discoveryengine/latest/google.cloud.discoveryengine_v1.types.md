---
url: https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types
title: Package types (0.20.5) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:00:35.642001+00:00
---

# Package types (0.20.5)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package types (0.20.5) Stay organized with collections  Save and categorize content based on your preferences. 

0.20.5 (latest)  0.20.4  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.12  0.12.3  0.11.14  0.10.0  0.9.1  0.8.1  0.7.0  0.6.0  0.5.0  0.4.1  0.3.1  0.2.1  0.1.1 

API documentation for `discoveryengine_v1.types` package.

## Classes 

### [AdvancedSiteSearchConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AdvancedSiteSearchConfig)

Configuration data for advance site search.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AlloyDbSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AlloyDbSource)

AlloyDB source import data from.

### [Answer](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Answer)

Defines an answer.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AnswerQueryRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AnswerQueryRequest)

Request message for ConversationalSearchService.AnswerQuery method.

### [AnswerQueryResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AnswerQueryResponse)

Response message for ConversationalSearchService.AnswerQuery method.

### [AssistAnswer](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AssistAnswer)

AssistAnswer resource, main part of AssistResponse.

### [AssistUserMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AssistUserMetadata)

User metadata of the request.

### [Assistant](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Assistant)

Discovery Engine Assistant resource.

### [AssistantContent](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AssistantContent)

Multi-modal content.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AssistantGroundedContent](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.AssistantGroundedContent)

A piece of content and possibly its grounding information.

Not all content needs grounding. Phrases like "Of course, I will gladly search it for you." do not need grounding.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [BatchCreateTargetSiteMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.BatchCreateTargetSiteMetadata)

Metadata related to the progress of the SiteSearchEngineService.BatchCreateTargetSites operation. This will be returned by the google.longrunning.Operation.metadata field.

### [BatchCreateTargetSitesRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.BatchCreateTargetSitesRequest)

Request message for SiteSearchEngineService.BatchCreateTargetSites method.

### [BatchCreateTargetSitesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.BatchCreateTargetSitesResponse)

Response message for SiteSearchEngineService.BatchCreateTargetSites method.

### [BatchGetDocumentsMetadataRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.BatchGetDocumentsMetadataRequest)

Request message for DocumentService.BatchGetDocumentsMetadata method.

### [BatchGetDocumentsMetadataResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.BatchGetDocumentsMetadataResponse)

Response message for DocumentService.BatchGetDocumentsMetadata method.

### [BatchUpdateUserLicensesMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.BatchUpdateUserLicensesMetadata)

Metadata related to the progress of the UserLicenseService.BatchUpdateUserLicenses operation. This will be returned by the google.longrunning.Operation.metadata field.

### [BatchUpdateUserLicensesRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.BatchUpdateUserLicensesRequest)

Request message for UserLicenseService.BatchUpdateUserLicenses method.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

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

### [BigtableSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.BigtableSource)

The Cloud Bigtable source for importing data.

### [CheckGroundingRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.CheckGroundingRequest)

Request message for GroundedGenerationService.CheckGrounding method.

### [CheckGroundingResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.CheckGroundingResponse)

Response message for the GroundedGenerationService.CheckGrounding method.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [CheckGroundingSpec](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.CheckGroundingSpec)

Specification for the grounding check.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Chunk](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Chunk)

Chunk captures all raw metadata information of items to be recommended or searched in the chunk mode.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [CloudSqlSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.CloudSqlSource)

Cloud SQL source import data from.

### [CmekConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.CmekConfig)

Configurations used to enable CMEK data encryption with Cloud KMS keys.

### [CollectUserEventRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.CollectUserEventRequest)

Request message for CollectUserEvent method.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [CompleteQueryRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.CompleteQueryRequest)

Request message for CompletionService.CompleteQuery method.

### [CompleteQueryResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.CompleteQueryResponse)

Response message for CompletionService.CompleteQuery method.

### [CompletionInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.CompletionInfo)

Detailed completion information including completion attribution token and clicked completion info.

### [CompletionSuggestion](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.CompletionSuggestion)

Autocomplete suggestions that are imported from Customer.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Condition](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Condition)

Defines circumstances to be checked before allowing a behavior

### [Control](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Control)

Defines a conditioned behavior to employ during serving. Must be attached to a ServingConfig to be considered at serving time. Permitted actions dependent on `SolutionType`.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Conversation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Conversation)

External conversation proto definition.

### [ConversationContext](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ConversationContext)

Defines context of the conversation

### [ConversationMessage](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ConversationMessage)

Defines a conversation message.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ConverseConversationRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ConverseConversationRequest)

Request message for ConversationalSearchService.ConverseConversation method.

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

### [DataStore](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.DataStore)

DataStore captures global settings and configs at the DataStore level.

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

### [DocumentInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.DocumentInfo)

Detailed document information associated with a user event.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [DocumentProcessingConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.DocumentProcessingConfig)

A singleton resource of DataStore. If it's empty when DataStore is created and DataStore is set to DataStore.ContentConfig.CONTENT_REQUIRED, the default parser will default to digital parser.

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

### [FactChunk](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.FactChunk)

Fact Chunk.

### [FetchDomainVerificationStatusRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.FetchDomainVerificationStatusRequest)

Request message for SiteSearchEngineService.FetchDomainVerificationStatus method.

### [FetchDomainVerificationStatusResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.FetchDomainVerificationStatusResponse)

Response message for SiteSearchEngineService.FetchDomainVerificationStatus method.

### [FetchSitemapsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.FetchSitemapsRequest)

Request message for SiteSearchEngineService.FetchSitemaps method.

### [FetchSitemapsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.FetchSitemapsResponse)

Response message for SiteSearchEngineService.FetchSitemaps method.

### [FhirStoreSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.FhirStoreSource)

Cloud FhirStore source import data from.

### [FirestoreSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.FirestoreSource)

Firestore source import data from.

### [GcsSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.GcsSource)

Cloud Storage location for input content.

### [GenerateGroundedContentRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.GenerateGroundedContentRequest)

Top-level message sent by the client for the `GenerateGroundedContent` method.

### [GenerateGroundedContentResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.GenerateGroundedContentResponse)

Response for the `GenerateGroundedContent` method.

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

### [GroundingFact](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.GroundingFact)

Grounding Fact.

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

### [ImportCompletionSuggestionsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ImportCompletionSuggestionsResponse)

Response of the CompletionService.ImportCompletionSuggestions method. If the long running operation is done, this message is returned by the google.longrunning.Operations.response field if the operation is successful.

### [ImportDocumentsMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ImportDocumentsMetadata)

Metadata related to the progress of the ImportDocuments operation. This is returned by the google.longrunning.Operation.metadata field.

### [ImportDocumentsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ImportDocumentsRequest)

Request message for Import methods.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ImportDocumentsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ImportDocumentsResponse)

Response of the ImportDocumentsRequest. If the long running operation is done, then this message is returned by the google.longrunning.Operations.response field if the operation was successful.

### [ImportErrorConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ImportErrorConfig)

Configuration of destination for Import related errors.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ImportIdentityMappingsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ImportIdentityMappingsRequest)

Request message for IdentityMappingStoreService.ImportIdentityMappings

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ImportIdentityMappingsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ImportIdentityMappingsResponse)

Response message for IdentityMappingStoreService.ImportIdentityMappings

### [ImportSuggestionDenyListEntriesMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ImportSuggestionDenyListEntriesMetadata)

Metadata related to the progress of the ImportSuggestionDenyListEntries operation. This is returned by the google.longrunning.Operation.metadata field.

### [ImportSuggestionDenyListEntriesRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ImportSuggestionDenyListEntriesRequest)

Request message for CompletionService.ImportSuggestionDenyListEntries method.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ImportSuggestionDenyListEntriesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ImportSuggestionDenyListEntriesResponse)

Response message for CompletionService.ImportSuggestionDenyListEntries method.

### [ImportUserEventsMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ImportUserEventsMetadata)

Metadata related to the progress of the Import operation. This is returned by the google.longrunning.Operation.metadata field.

### [ImportUserEventsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ImportUserEventsRequest)

Request message for the ImportUserEvents request.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

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

### [PurgeDocumentsResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.PurgeDocumentsResponse)

Response message for DocumentService.PurgeDocuments method. If the long running operation is successfully done, then this message is returned by the google.longrunning.Operations.response field.

### [PurgeErrorConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.PurgeErrorConfig)

Configuration of destination for Purge related errors.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [PurgeIdentityMappingsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.PurgeIdentityMappingsRequest)

Request message for IdentityMappingStoreService.PurgeIdentityMappings

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

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

### [RankResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.RankResponse)

Response message for RankService.Rank method.

### [RankingRecord](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.RankingRecord)

Record message for RankService.Rank method.

### [RecommendRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.RecommendRequest)

Request message for Recommend method.

### [RecommendResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.RecommendResponse)

Response message for Recommend method.

### [RecrawlUrisMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.RecrawlUrisMetadata)

Metadata related to the progress of the SiteSearchEngineService.RecrawlUris operation. This will be returned by the google.longrunning.Operation.metadata field.

### [RecrawlUrisRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.RecrawlUrisRequest)

Request message for SiteSearchEngineService.RecrawlUris method.

### [RecrawlUrisResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.RecrawlUrisResponse)

Response message for SiteSearchEngineService.RecrawlUris method.

### [Reply](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Reply)

Defines a reply message to user.

### [SafetyRating](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SafetyRating)

Safety rating corresponding to the generated content.

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

### [SearchResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchResponse)

Response message for SearchService.Search method.

### [SearchTier](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchTier)

Tiers of search features. Different tiers might have different pricing. To learn more, check the pricing documentation.

### [SearchUseCase](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchUseCase)

Defines a further subdivision of `SolutionType`. Specifically applies to SOLUTION_TYPE_SEARCH.

### [ServingConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ServingConfig)

Configures metadata that is used to generate serving time results (e.g. search results or recommendation predictions). The ServingConfig is passed in the search and predict request and generates results.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Session](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Session)

External session proto definition.

### [SingleRegionKey](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SingleRegionKey)

Metadata for single-regional CMEKs.

### [SiteSearchEngine](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SiteSearchEngine)

SiteSearchEngine captures DataStore level site search persisting configurations. It is a singleton value per data store.

### [SiteVerificationInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SiteVerificationInfo)

Verification information for target sites in advanced site search.

### [Sitemap](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Sitemap)

A sitemap for the SiteSearchEngine.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [SolutionType](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SolutionType)

The type of solution.

### [SpannerSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SpannerSource)

The Spanner source for importing data

### [StreamAssistRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.StreamAssistRequest)

Request for the AssistantService.StreamAssist method.

### [StreamAssistResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.StreamAssistResponse)

Response for the AssistantService.StreamAssist method.

### [SuggestionDenyListEntry](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SuggestionDenyListEntry)

Suggestion deny list entry identifying the phrase to block from suggestions and the applied operation for the phrase.

### [TargetSite](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.TargetSite)

A target site for the SiteSearchEngine.

### [TextInput](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.TextInput)

Defines text input.

### [TrainCustomModelMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.TrainCustomModelMetadata)

Metadata related to the progress of the TrainCustomModel operation. This is returned by the google.longrunning.Operation.metadata field.

### [TrainCustomModelRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.TrainCustomModelRequest)

Request message for SearchTuningService.TrainCustomModel method.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [TrainCustomModelResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.TrainCustomModelResponse)

Response of the TrainCustomModelRequest. This message is returned by the google.longrunning.Operations.response field.

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

### [UserInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.UserInfo)

Information of an end user.

### [UserLicense](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.UserLicense)

User License information assigned by the admin.

### [WorkspaceConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.WorkspaceConfig)

Config to store data store type configuration for workspace data

### [WriteUserEventRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.WriteUserEventRequest)

Request message for WriteUserEvent method.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
