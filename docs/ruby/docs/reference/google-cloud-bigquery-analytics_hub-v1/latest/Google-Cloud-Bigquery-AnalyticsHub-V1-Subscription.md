---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-Subscription/
title: Analytics Hub V1 API - Class Google::Cloud::Bigquery::AnalyticsHub::V1::Subscription (v0.20.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:27:07.824153+00:00
---

# Analytics Hub V1 API - Class Google::Cloud::Bigquery::AnalyticsHub::V1::Subscription (v0.20.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-Subscription/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Analytics Hub V1 API - Class Google::Cloud::Bigquery::AnalyticsHub::V1::Subscription (v0.20.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.20.1 (latest)  0.20.0  0.19.0  0.18.0  0.17.0  0.16.1  0.15.0  0.14.0  0.13.1  0.12.0  0.11.1  0.10.0  0.9.0  0.8.1  0.7.0  0.6.0  0.5.2  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Analytics Hub V1 API class Google::Cloud::Bigquery::AnalyticsHub::V1::Subscription.

A subscription represents a subscribers' access to a particular set of published data. It contains references to associated listings, data exchanges, and linked datasets.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #commercial_info
    
    
    def commercial_info() -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::Subscription::CommercialInfo

**Returns**

  * ([::Google::Cloud::Bigquery::AnalyticsHub::V1::Subscription::CommercialInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-Subscription-CommercialInfo)) — Output only. This is set if this is a commercial subscription i.e. if this subscription was created from subscribing to a commercial listing. 



### #creation_time
    
    
    def creation_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Protobuf-Timestamp)) — Output only. Timestamp when the subscription was created. 



### #data_exchange
    
    
    def data_exchange() -> ::String

**Returns**

  * (::String) — Output only. Resource name of the source Data Exchange. e.g. projects/123/locations/us/dataExchanges/456

Note: The following fields are mutually exclusive: `data_exchange`, `listing`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #destination_dataset
    
    
    def destination_dataset() -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::DestinationDataset

**Returns**

  * ([::Google::Cloud::Bigquery::AnalyticsHub::V1::DestinationDataset](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-DestinationDataset)) — Optional. BigQuery destination dataset to create for the subscriber. 



### #destination_dataset=
    
    
    def destination_dataset=(value) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::DestinationDataset

**Parameter**

  * **value** ([::Google::Cloud::Bigquery::AnalyticsHub::V1::DestinationDataset](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-DestinationDataset)) — Optional. BigQuery destination dataset to create for the subscriber. 



**Returns**

  * ([::Google::Cloud::Bigquery::AnalyticsHub::V1::DestinationDataset](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-DestinationDataset)) — Optional. BigQuery destination dataset to create for the subscriber. 



### #last_modify_time
    
    
    def last_modify_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Protobuf-Timestamp)) — Output only. Timestamp when the subscription was last modified. 



### #linked_dataset_map
    
    
    def linked_dataset_map() -> ::Google::Protobuf::Map{::String => ::Google::Cloud::Bigquery::AnalyticsHub::V1::Subscription::LinkedResource}

**Returns**

  * (::Google::Protobuf::Map{::String => ::Google::Cloud::Bigquery::AnalyticsHub::V1::Subscription::LinkedResource}) — Output only. Map of listing resource names to associated linked resource, e.g. projects/123/locations/us/dataExchanges/456/listings/789 -> projects/123/datasets/my_dataset

For listing-level subscriptions, this is a map of size 1. Only contains values if state == STATE_ACTIVE. 




### #linked_resources
    
    
    def linked_resources() -> ::Array<::Google::Cloud::Bigquery::AnalyticsHub::V1::Subscription::LinkedResource>

**Returns**

  * (::Array<[::Google::Cloud::Bigquery::AnalyticsHub::V1::Subscription::LinkedResource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-Subscription-LinkedResource)>) — Output only. Linked resources created in the subscription. Only contains values if state = STATE_ACTIVE. 



### #listing
    
    
    def listing() -> ::String

**Returns**

  * (::String) — Output only. Resource name of the source Listing. e.g. projects/123/locations/us/dataExchanges/456/listings/789

Note: The following fields are mutually exclusive: `listing`, `data_exchange`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #log_linked_dataset_query_user_email
    
    
    def log_linked_dataset_query_user_email() -> ::Boolean

**Returns**

  * (::Boolean) — Output only. By default, false. If true, the Subscriber agreed to the email sharing mandate that is enabled for DataExchange/Listing. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Output only. The resource name of the subscription. e.g. `projects/myproject/locations/us/subscriptions/123`. 



### #organization_display_name
    
    
    def organization_display_name() -> ::String

**Returns**

  * (::String) — Output only. Display name of the project of this subscription. 



### #organization_id
    
    
    def organization_id() -> ::String

**Returns**

  * (::String) — Output only. Organization of the project this subscription belongs to. 



### #resource_type
    
    
    def resource_type() -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::SharedResourceType

**Returns**

  * ([::Google::Cloud::Bigquery::AnalyticsHub::V1::SharedResourceType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-SharedResourceType)) — Output only. Listing shared asset type. 



### #state
    
    
    def state() -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::Subscription::State

**Returns**

  * ([::Google::Cloud::Bigquery::AnalyticsHub::V1::Subscription::State](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-Subscription-State)) — Output only. Current state of the subscription. 



### #subscriber_contact
    
    
    def subscriber_contact() -> ::String

**Returns**

  * (::String) — Output only. Email of the subscriber. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
