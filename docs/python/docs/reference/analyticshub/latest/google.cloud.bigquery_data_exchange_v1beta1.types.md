---
url: https://docs.cloud.google.com/python/docs/reference/analyticshub/latest/google.cloud.bigquery_data_exchange_v1beta1.types
title: Package types (0.9.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:30:04.810487+00:00
---

# Package types (0.9.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/analyticshub/latest/google.cloud.bigquery_data_exchange_v1beta1.types

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package types (0.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.9.1 (latest)  0.9.0  0.8.0  0.7.0  0.6.0  0.5.20  0.4.20  0.3.2  0.2.1  0.1.1 

API documentation for `bigquery_data_exchange_v1beta1.types` package.

## Classes 

### [CreateDataExchangeRequest](https://docs.cloud.google.com/python/docs/reference/analyticshub/latest/google.cloud.bigquery_data_exchange_v1beta1.types.CreateDataExchangeRequest)

Message for creating a data exchange.

### [CreateListingRequest](https://docs.cloud.google.com/python/docs/reference/analyticshub/latest/google.cloud.bigquery_data_exchange_v1beta1.types.CreateListingRequest)

Message for creating a listing.

### [DataExchange](https://docs.cloud.google.com/python/docs/reference/analyticshub/latest/google.cloud.bigquery_data_exchange_v1beta1.types.DataExchange)

A data exchange is a container that lets you share data. Along with the descriptive information about the data exchange, it contains listings that reference shared datasets.

### [DataProvider](https://docs.cloud.google.com/python/docs/reference/analyticshub/latest/google.cloud.bigquery_data_exchange_v1beta1.types.DataProvider)

Contains details of the data provider.

### [DeleteDataExchangeRequest](https://docs.cloud.google.com/python/docs/reference/analyticshub/latest/google.cloud.bigquery_data_exchange_v1beta1.types.DeleteDataExchangeRequest)

Message for deleting a data exchange.

### [DeleteListingRequest](https://docs.cloud.google.com/python/docs/reference/analyticshub/latest/google.cloud.bigquery_data_exchange_v1beta1.types.DeleteListingRequest)

Message for deleting a listing.

### [DestinationDataset](https://docs.cloud.google.com/python/docs/reference/analyticshub/latest/google.cloud.bigquery_data_exchange_v1beta1.types.DestinationDataset)

Defines the destination bigquery dataset.

### [DestinationDatasetReference](https://docs.cloud.google.com/python/docs/reference/analyticshub/latest/google.cloud.bigquery_data_exchange_v1beta1.types.DestinationDatasetReference)

Contains the reference that identifies a destination bigquery dataset.

### [GetDataExchangeRequest](https://docs.cloud.google.com/python/docs/reference/analyticshub/latest/google.cloud.bigquery_data_exchange_v1beta1.types.GetDataExchangeRequest)

Message for getting a data exchange.

### [GetListingRequest](https://docs.cloud.google.com/python/docs/reference/analyticshub/latest/google.cloud.bigquery_data_exchange_v1beta1.types.GetListingRequest)

Message for getting a listing.

### [ListDataExchangesRequest](https://docs.cloud.google.com/python/docs/reference/analyticshub/latest/google.cloud.bigquery_data_exchange_v1beta1.types.ListDataExchangesRequest)

Message for requesting the list of data exchanges.

### [ListDataExchangesResponse](https://docs.cloud.google.com/python/docs/reference/analyticshub/latest/google.cloud.bigquery_data_exchange_v1beta1.types.ListDataExchangesResponse)

Message for response to the list of data exchanges.

### [ListListingsRequest](https://docs.cloud.google.com/python/docs/reference/analyticshub/latest/google.cloud.bigquery_data_exchange_v1beta1.types.ListListingsRequest)

Message for requesting the list of listings.

### [ListListingsResponse](https://docs.cloud.google.com/python/docs/reference/analyticshub/latest/google.cloud.bigquery_data_exchange_v1beta1.types.ListListingsResponse)

Message for response to the list of Listings.

### [ListOrgDataExchangesRequest](https://docs.cloud.google.com/python/docs/reference/analyticshub/latest/google.cloud.bigquery_data_exchange_v1beta1.types.ListOrgDataExchangesRequest)

Message for requesting the list of data exchanges from projects in an organization and location.

### [ListOrgDataExchangesResponse](https://docs.cloud.google.com/python/docs/reference/analyticshub/latest/google.cloud.bigquery_data_exchange_v1beta1.types.ListOrgDataExchangesResponse)

Message for response to listing data exchanges in an organization and location.

### [Listing](https://docs.cloud.google.com/python/docs/reference/analyticshub/latest/google.cloud.bigquery_data_exchange_v1beta1.types.Listing)

A listing is what gets published into a data exchange that a subscriber can subscribe to. It contains a reference to the data source along with descriptive information that will help subscribers find and subscribe the data.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Publisher](https://docs.cloud.google.com/python/docs/reference/analyticshub/latest/google.cloud.bigquery_data_exchange_v1beta1.types.Publisher)

Contains details of the listing publisher.

### [SubscribeListingRequest](https://docs.cloud.google.com/python/docs/reference/analyticshub/latest/google.cloud.bigquery_data_exchange_v1beta1.types.SubscribeListingRequest)

Message for subscribing to a listing.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [SubscribeListingResponse](https://docs.cloud.google.com/python/docs/reference/analyticshub/latest/google.cloud.bigquery_data_exchange_v1beta1.types.SubscribeListingResponse)

Message for response when you subscribe to a listing.

### [UpdateDataExchangeRequest](https://docs.cloud.google.com/python/docs/reference/analyticshub/latest/google.cloud.bigquery_data_exchange_v1beta1.types.UpdateDataExchangeRequest)

Message for updating a data exchange.

### [UpdateListingRequest](https://docs.cloud.google.com/python/docs/reference/analyticshub/latest/google.cloud.bigquery_data_exchange_v1beta1.types.UpdateListingRequest)

Message for updating a Listing.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
