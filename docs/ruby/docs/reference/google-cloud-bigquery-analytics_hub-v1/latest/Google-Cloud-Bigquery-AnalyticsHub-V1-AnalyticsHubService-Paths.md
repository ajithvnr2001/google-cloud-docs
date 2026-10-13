---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-AnalyticsHubService-Paths/
title: Analytics Hub V1 API - Module Google::Cloud::Bigquery::AnalyticsHub::V1::AnalyticsHubService::Paths (v0.20.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:44:53.908258+00:00
---

# Analytics Hub V1 API - Module Google::Cloud::Bigquery::AnalyticsHub::V1::AnalyticsHubService::Paths (v0.20.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-AnalyticsHubService-Paths/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Analytics Hub V1 API - Module Google::Cloud::Bigquery::AnalyticsHub::V1::AnalyticsHubService::Paths (v0.20.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.20.1 (latest)  0.20.0  0.19.0  0.18.0  0.17.0  0.16.1  0.15.0  0.14.0  0.13.1  0.12.0  0.11.1  0.10.0  0.9.0  0.8.1  0.7.0  0.6.0  0.5.2  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Analytics Hub V1 API module Google::Cloud::Bigquery::AnalyticsHub::V1::AnalyticsHubService::Paths.

Path helper methods for the AnalyticsHubService API.

## Extended By

  * [Google::Cloud::Bigquery::AnalyticsHub::V1::AnalyticsHubService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-AnalyticsHubService-Paths)



## Included In

  * [Google::Cloud::Bigquery::AnalyticsHub::V1::AnalyticsHubService::Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-AnalyticsHubService-Client)
  * [Google::Cloud::Bigquery::AnalyticsHub::V1::AnalyticsHubService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-AnalyticsHubService-Paths)
  * [Google::Cloud::Bigquery::AnalyticsHub::V1::AnalyticsHubService::Rest::Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-AnalyticsHubService-Rest-Client)



## Methods 

### #data_exchange_path
    
    
    def data_exchange_path(project:, location:, data_exchange:) -> ::String

Create a fully-qualified DataExchange resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/dataExchanges/{data_exchange}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **data_exchange** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #dataset_path
    
    
    def dataset_path(project:, dataset:) -> ::String

Create a fully-qualified Dataset resource string.

The resource will be in the following format:

`projects/{project}/datasets/{dataset}`

**Parameters**

  * **project** (String) 
  * **dataset** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #listing_path
    
    
    def listing_path(project:, location:, data_exchange:, listing:) -> ::String

Create a fully-qualified Listing resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/dataExchanges/{data_exchange}/listings/{listing}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **data_exchange** (String) 
  * **listing** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #location_path
    
    
    def location_path(project:, location:) -> ::String

Create a fully-qualified Location resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}`

**Parameters**

  * **project** (String) 
  * **location** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #managed_service_path
    
    
    def managed_service_path(service:) -> ::String

Create a fully-qualified ManagedService resource string.

The resource will be in the following format:

`services/{service}`

**Parameter**

  * **service** (String) 



**Returns**

  * (::String) 



### #query_template_path
    
    
    def query_template_path(project:, location:, data_exchange:, query_template:) -> ::String

Create a fully-qualified QueryTemplate resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/dataExchanges/{data_exchange}/queryTemplates/{query_template}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **data_exchange** (String) 
  * **query_template** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #routine_path
    
    
    def routine_path(project:, dataset:, routine:) -> ::String

Create a fully-qualified Routine resource string.

The resource will be in the following format:

`projects/{project}/datasets/{dataset}/routines/{routine}`

**Parameters**

  * **project** (String) 
  * **dataset** (String) 
  * **routine** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #subscription_path
    
    
    def subscription_path(project:, location:, subscription:) -> ::String

Create a fully-qualified Subscription resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/subscriptions/{subscription}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **subscription** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #table_path
    
    
    def table_path(project:, dataset:, table:) -> ::String

Create a fully-qualified Table resource string.

The resource will be in the following format:

`projects/{project}/datasets/{dataset}/tables/{table}`

**Parameters**

  * **project** (String) 
  * **dataset** (String) 
  * **table** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #topic_path
    
    
    def topic_path(project:, topic:) -> ::String

Create a fully-qualified Topic resource string.

The resource will be in the following format:

`projects/{project}/topics/{topic}`

**Parameters**

  * **project** (String) 
  * **topic** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
