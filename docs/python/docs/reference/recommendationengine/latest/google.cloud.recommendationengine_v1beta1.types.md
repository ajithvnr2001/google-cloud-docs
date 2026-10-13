---
url: https://docs.cloud.google.com/python/docs/reference/recommendationengine/latest/google.cloud.recommendationengine_v1beta1.types
title: Package types (0.13.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:13:39.483787+00:00
---

# Package types (0.13.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/recommendationengine/latest/google.cloud.recommendationengine_v1beta1.types

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package types (0.13.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.13.2 (latest)  0.13.1  0.12.0  0.11.0  0.10.18  0.9.0  0.8.2  0.7.1  0.6.2  0.5.1  0.4.0  0.3.3  0.2.2  0.1.0 

API documentation for `recommendationengine_v1beta1.types` package.

## Classes 

### [CatalogInlineSource](https://docs.cloud.google.com/python/docs/reference/recommendationengine/latest/google.cloud.recommendationengine_v1beta1.types.CatalogInlineSource)

The inline source for the input config for ImportCatalogItems method.

### [CatalogItem](https://docs.cloud.google.com/python/docs/reference/recommendationengine/latest/google.cloud.recommendationengine_v1beta1.types.CatalogItem)

CatalogItem captures all metadata information of items to be recommended.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [CollectUserEventRequest](https://docs.cloud.google.com/python/docs/reference/recommendationengine/latest/google.cloud.recommendationengine_v1beta1.types.CollectUserEventRequest)

Request message for CollectUserEvent method.

### [CreateCatalogItemRequest](https://docs.cloud.google.com/python/docs/reference/recommendationengine/latest/google.cloud.recommendationengine_v1beta1.types.CreateCatalogItemRequest)

Request message for CreateCatalogItem method.

### [CreatePredictionApiKeyRegistrationRequest](https://docs.cloud.google.com/python/docs/reference/recommendationengine/latest/google.cloud.recommendationengine_v1beta1.types.CreatePredictionApiKeyRegistrationRequest)

Request message for the `CreatePredictionApiKeyRegistration` method.

### [DeleteCatalogItemRequest](https://docs.cloud.google.com/python/docs/reference/recommendationengine/latest/google.cloud.recommendationengine_v1beta1.types.DeleteCatalogItemRequest)

Request message for DeleteCatalogItem method.

### [DeletePredictionApiKeyRegistrationRequest](https://docs.cloud.google.com/python/docs/reference/recommendationengine/latest/google.cloud.recommendationengine_v1beta1.types.DeletePredictionApiKeyRegistrationRequest)

Request message for `DeletePredictionApiKeyRegistration` method.

### [EventDetail](https://docs.cloud.google.com/python/docs/reference/recommendationengine/latest/google.cloud.recommendationengine_v1beta1.types.EventDetail)

User event details shared by all recommendation types.

### [FeatureMap](https://docs.cloud.google.com/python/docs/reference/recommendationengine/latest/google.cloud.recommendationengine_v1beta1.types.FeatureMap)

FeatureMap represents extra features that customers want to include in the recommendation model for catalogs/user events as categorical/numerical features.

### [GcsSource](https://docs.cloud.google.com/python/docs/reference/recommendationengine/latest/google.cloud.recommendationengine_v1beta1.types.GcsSource)

Google Cloud Storage location for input content. format.

### [GetCatalogItemRequest](https://docs.cloud.google.com/python/docs/reference/recommendationengine/latest/google.cloud.recommendationengine_v1beta1.types.GetCatalogItemRequest)

Request message for GetCatalogItem method.

### [Image](https://docs.cloud.google.com/python/docs/reference/recommendationengine/latest/google.cloud.recommendationengine_v1beta1.types.Image)

Catalog item thumbnail/detail image.

### [ImportCatalogItemsRequest](https://docs.cloud.google.com/python/docs/reference/recommendationengine/latest/google.cloud.recommendationengine_v1beta1.types.ImportCatalogItemsRequest)

Request message for Import methods.

### [ImportCatalogItemsResponse](https://docs.cloud.google.com/python/docs/reference/recommendationengine/latest/google.cloud.recommendationengine_v1beta1.types.ImportCatalogItemsResponse)

Response of the ImportCatalogItemsRequest. If the long running operation is done, then this message is returned by the google.longrunning.Operations.response field if the operation was successful.

### [ImportErrorsConfig](https://docs.cloud.google.com/python/docs/reference/recommendationengine/latest/google.cloud.recommendationengine_v1beta1.types.ImportErrorsConfig)

Configuration of destination for Import related errors.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ImportMetadata](https://docs.cloud.google.com/python/docs/reference/recommendationengine/latest/google.cloud.recommendationengine_v1beta1.types.ImportMetadata)

Metadata related to the progress of the Import operation. This will be returned by the google.longrunning.Operation.metadata field.

### [ImportUserEventsRequest](https://docs.cloud.google.com/python/docs/reference/recommendationengine/latest/google.cloud.recommendationengine_v1beta1.types.ImportUserEventsRequest)

Request message for the ImportUserEvents request.

### [ImportUserEventsResponse](https://docs.cloud.google.com/python/docs/reference/recommendationengine/latest/google.cloud.recommendationengine_v1beta1.types.ImportUserEventsResponse)

Response of the ImportUserEventsRequest. If the long running operation was successful, then this message is returned by the google.longrunning.Operations.response field if the operation was successful.

### [InputConfig](https://docs.cloud.google.com/python/docs/reference/recommendationengine/latest/google.cloud.recommendationengine_v1beta1.types.InputConfig)

The input config source.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ListCatalogItemsRequest](https://docs.cloud.google.com/python/docs/reference/recommendationengine/latest/google.cloud.recommendationengine_v1beta1.types.ListCatalogItemsRequest)

Request message for ListCatalogItems method.

### [ListCatalogItemsResponse](https://docs.cloud.google.com/python/docs/reference/recommendationengine/latest/google.cloud.recommendationengine_v1beta1.types.ListCatalogItemsResponse)

Response message for ListCatalogItems method.

### [ListPredictionApiKeyRegistrationsRequest](https://docs.cloud.google.com/python/docs/reference/recommendationengine/latest/google.cloud.recommendationengine_v1beta1.types.ListPredictionApiKeyRegistrationsRequest)

Request message for the `ListPredictionApiKeyRegistrations`.

### [ListPredictionApiKeyRegistrationsResponse](https://docs.cloud.google.com/python/docs/reference/recommendationengine/latest/google.cloud.recommendationengine_v1beta1.types.ListPredictionApiKeyRegistrationsResponse)

Response message for the `ListPredictionApiKeyRegistrations`.

### [ListUserEventsRequest](https://docs.cloud.google.com/python/docs/reference/recommendationengine/latest/google.cloud.recommendationengine_v1beta1.types.ListUserEventsRequest)

Request message for ListUserEvents method.

### [ListUserEventsResponse](https://docs.cloud.google.com/python/docs/reference/recommendationengine/latest/google.cloud.recommendationengine_v1beta1.types.ListUserEventsResponse)

Response message for ListUserEvents method.

### [PredictRequest](https://docs.cloud.google.com/python/docs/reference/recommendationengine/latest/google.cloud.recommendationengine_v1beta1.types.PredictRequest)

Request message for Predict method.

### [PredictResponse](https://docs.cloud.google.com/python/docs/reference/recommendationengine/latest/google.cloud.recommendationengine_v1beta1.types.PredictResponse)

Response message for predict method.

### [PredictionApiKeyRegistration](https://docs.cloud.google.com/python/docs/reference/recommendationengine/latest/google.cloud.recommendationengine_v1beta1.types.PredictionApiKeyRegistration)

Registered Api Key.

### [ProductCatalogItem](https://docs.cloud.google.com/python/docs/reference/recommendationengine/latest/google.cloud.recommendationengine_v1beta1.types.ProductCatalogItem)

ProductCatalogItem captures item metadata specific to retail products.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ProductDetail](https://docs.cloud.google.com/python/docs/reference/recommendationengine/latest/google.cloud.recommendationengine_v1beta1.types.ProductDetail)

Detailed product information associated with a user event.

### [ProductEventDetail](https://docs.cloud.google.com/python/docs/reference/recommendationengine/latest/google.cloud.recommendationengine_v1beta1.types.ProductEventDetail)

ProductEventDetail captures user event information specific to retail products.

### [PurchaseTransaction](https://docs.cloud.google.com/python/docs/reference/recommendationengine/latest/google.cloud.recommendationengine_v1beta1.types.PurchaseTransaction)

A transaction represents the entire purchase transaction.

### [PurgeUserEventsMetadata](https://docs.cloud.google.com/python/docs/reference/recommendationengine/latest/google.cloud.recommendationengine_v1beta1.types.PurgeUserEventsMetadata)

Metadata related to the progress of the PurgeUserEvents operation. This will be returned by the google.longrunning.Operation.metadata field.

### [PurgeUserEventsRequest](https://docs.cloud.google.com/python/docs/reference/recommendationengine/latest/google.cloud.recommendationengine_v1beta1.types.PurgeUserEventsRequest)

Request message for PurgeUserEvents method.

### [PurgeUserEventsResponse](https://docs.cloud.google.com/python/docs/reference/recommendationengine/latest/google.cloud.recommendationengine_v1beta1.types.PurgeUserEventsResponse)

Response of the PurgeUserEventsRequest. If the long running operation is successfully done, then this message is returned by the google.longrunning.Operations.response field.

### [UpdateCatalogItemRequest](https://docs.cloud.google.com/python/docs/reference/recommendationengine/latest/google.cloud.recommendationengine_v1beta1.types.UpdateCatalogItemRequest)

Request message for UpdateCatalogItem method.

### [UserEvent](https://docs.cloud.google.com/python/docs/reference/recommendationengine/latest/google.cloud.recommendationengine_v1beta1.types.UserEvent)

UserEvent captures all metadata information recommendation engine needs to know about how end users interact with customers' website.

### [UserEventImportSummary](https://docs.cloud.google.com/python/docs/reference/recommendationengine/latest/google.cloud.recommendationengine_v1beta1.types.UserEventImportSummary)

A summary of import result. The UserEventImportSummary summarizes the import status for user events.

### [UserEventInlineSource](https://docs.cloud.google.com/python/docs/reference/recommendationengine/latest/google.cloud.recommendationengine_v1beta1.types.UserEventInlineSource)

The inline source for the input config for ImportUserEvents method.

### [UserInfo](https://docs.cloud.google.com/python/docs/reference/recommendationengine/latest/google.cloud.recommendationengine_v1beta1.types.UserInfo)

Information of end users.

### [WriteUserEventRequest](https://docs.cloud.google.com/python/docs/reference/recommendationengine/latest/google.cloud.recommendationengine_v1beta1.types.WriteUserEventRequest)

Request message for WriteUserEvent method.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
