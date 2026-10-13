---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-Listing/
title: Analytics Hub V1 API - Class Google::Cloud::Bigquery::AnalyticsHub::V1::Listing (v0.20.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:17:21.826428+00:00
---

# Analytics Hub V1 API - Class Google::Cloud::Bigquery::AnalyticsHub::V1::Listing (v0.20.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-Listing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Analytics Hub V1 API - Class Google::Cloud::Bigquery::AnalyticsHub::V1::Listing (v0.20.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.20.1 (latest)  0.20.0  0.19.0  0.18.0  0.17.0  0.16.1  0.15.0  0.14.0  0.13.1  0.12.0  0.11.1  0.10.0  0.9.0  0.8.1  0.7.0  0.6.0  0.5.2  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Analytics Hub V1 API class Google::Cloud::Bigquery::AnalyticsHub::V1::Listing.

A listing is what gets published into a data exchange that a subscriber can subscribe to. It contains a reference to the data source along with descriptive information that will help subscribers find and subscribe the data.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #allow_only_metadata_sharing
    
    
    def allow_only_metadata_sharing() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. If true, the listing is only available to get the resource metadata. Listing is non subscribable. 



### #allow_only_metadata_sharing=
    
    
    def allow_only_metadata_sharing=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. If true, the listing is only available to get the resource metadata. Listing is non subscribable. 



**Returns**

  * (::Boolean) — Optional. If true, the listing is only available to get the resource metadata. Listing is non subscribable. 



### #bigquery_dataset
    
    
    def bigquery_dataset() -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::Listing::BigQueryDatasetSource

**Returns**

  * ([::Google::Cloud::Bigquery::AnalyticsHub::V1::Listing::BigQueryDatasetSource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-Listing-BigQueryDatasetSource)) — Shared dataset i.e. BigQuery dataset source.

Note: The following fields are mutually exclusive: `bigquery_dataset`, `pubsub_topic`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #bigquery_dataset=
    
    
    def bigquery_dataset=(value) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::Listing::BigQueryDatasetSource

**Parameter**

  * **value** ([::Google::Cloud::Bigquery::AnalyticsHub::V1::Listing::BigQueryDatasetSource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-Listing-BigQueryDatasetSource)) — Shared dataset i.e. BigQuery dataset source.

Note: The following fields are mutually exclusive: `bigquery_dataset`, `pubsub_topic`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Bigquery::AnalyticsHub::V1::Listing::BigQueryDatasetSource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-Listing-BigQueryDatasetSource)) — Shared dataset i.e. BigQuery dataset source.

Note: The following fields are mutually exclusive: `bigquery_dataset`, `pubsub_topic`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #categories
    
    
    def categories() -> ::Array<::Google::Cloud::Bigquery::AnalyticsHub::V1::Listing::Category>

**Returns**

  * (::Array<[::Google::Cloud::Bigquery::AnalyticsHub::V1::Listing::Category](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-Listing-Category)>) — Optional. Categories of the listing. Up to five categories are allowed. 



### #categories=
    
    
    def categories=(value) -> ::Array<::Google::Cloud::Bigquery::AnalyticsHub::V1::Listing::Category>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Bigquery::AnalyticsHub::V1::Listing::Category](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-Listing-Category)>) — Optional. Categories of the listing. Up to five categories are allowed. 



**Returns**

  * (::Array<[::Google::Cloud::Bigquery::AnalyticsHub::V1::Listing::Category](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-Listing-Category)>) — Optional. Categories of the listing. Up to five categories are allowed. 



### #commercial_info
    
    
    def commercial_info() -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::Listing::CommercialInfo

**Returns**

  * ([::Google::Cloud::Bigquery::AnalyticsHub::V1::Listing::CommercialInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-Listing-CommercialInfo)) — Output only. Commercial info contains the information about the commercial data products associated with the listing. 



### #data_provider
    
    
    def data_provider() -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::DataProvider

**Returns**

  * ([::Google::Cloud::Bigquery::AnalyticsHub::V1::DataProvider](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-DataProvider)) — Optional. Details of the data provider who owns the source data. 



### #data_provider=
    
    
    def data_provider=(value) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::DataProvider

**Parameter**

  * **value** ([::Google::Cloud::Bigquery::AnalyticsHub::V1::DataProvider](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-DataProvider)) — Optional. Details of the data provider who owns the source data. 



**Returns**

  * ([::Google::Cloud::Bigquery::AnalyticsHub::V1::DataProvider](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-DataProvider)) — Optional. Details of the data provider who owns the source data. 



### #description
    
    
    def description() -> ::String

**Returns**

  * (::String) — Optional. Short description of the listing. The description must not contain Unicode non-characters and C0 and C1 control codes except tabs (HT), new lines (LF), carriage returns (CR), and page breaks (FF). Default value is an empty string. Max length: 2000 bytes. 



### #description=
    
    
    def description=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Short description of the listing. The description must not contain Unicode non-characters and C0 and C1 control codes except tabs (HT), new lines (LF), carriage returns (CR), and page breaks (FF). Default value is an empty string. Max length: 2000 bytes. 



**Returns**

  * (::String) — Optional. Short description of the listing. The description must not contain Unicode non-characters and C0 and C1 control codes except tabs (HT), new lines (LF), carriage returns (CR), and page breaks (FF). Default value is an empty string. Max length: 2000 bytes. 



### #discovery_type
    
    
    def discovery_type() -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::DiscoveryType

**Returns**

  * ([::Google::Cloud::Bigquery::AnalyticsHub::V1::DiscoveryType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-DiscoveryType)) — Optional. Type of discovery of the listing on the discovery page. 



### #discovery_type=
    
    
    def discovery_type=(value) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::DiscoveryType

**Parameter**

  * **value** ([::Google::Cloud::Bigquery::AnalyticsHub::V1::DiscoveryType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-DiscoveryType)) — Optional. Type of discovery of the listing on the discovery page. 



**Returns**

  * ([::Google::Cloud::Bigquery::AnalyticsHub::V1::DiscoveryType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-DiscoveryType)) — Optional. Type of discovery of the listing on the discovery page. 



### #display_name
    
    
    def display_name() -> ::String

**Returns**

  * (::String) — Required. Human-readable display name of the listing. The display name must contain only Unicode letters, numbers (0-9), underscores (_), dashes (-), spaces ( ), ampersands (&) and can't start or end with spaces. Default value is an empty string. Max length: 63 bytes. 



### #display_name=
    
    
    def display_name=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Human-readable display name of the listing. The display name must contain only Unicode letters, numbers (0-9), underscores (_), dashes (-), spaces ( ), ampersands (&) and can't start or end with spaces. Default value is an empty string. Max length: 63 bytes. 



**Returns**

  * (::String) — Required. Human-readable display name of the listing. The display name must contain only Unicode letters, numbers (0-9), underscores (_), dashes (-), spaces ( ), ampersands (&) and can't start or end with spaces. Default value is an empty string. Max length: 63 bytes. 



### #documentation
    
    
    def documentation() -> ::String

**Returns**

  * (::String) — Optional. Documentation describing the listing. 



### #documentation=
    
    
    def documentation=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Documentation describing the listing. 



**Returns**

  * (::String) — Optional. Documentation describing the listing. 



### #icon
    
    
    def icon() -> ::String

**Returns**

  * (::String) — Optional. Base64 encoded image representing the listing. Max Size: 3.0MiB Expected image dimensions are 512x512 pixels, however the API only performs validation on size of the encoded data. Note: For byte fields, the contents of the field are base64-encoded (which increases the size of the data by 33-36%) when using JSON on the wire. 



### #icon=
    
    
    def icon=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Base64 encoded image representing the listing. Max Size: 3.0MiB Expected image dimensions are 512x512 pixels, however the API only performs validation on size of the encoded data. Note: For byte fields, the contents of the field are base64-encoded (which increases the size of the data by 33-36%) when using JSON on the wire. 



**Returns**

  * (::String) — Optional. Base64 encoded image representing the listing. Max Size: 3.0MiB Expected image dimensions are 512x512 pixels, however the API only performs validation on size of the encoded data. Note: For byte fields, the contents of the field are base64-encoded (which increases the size of the data by 33-36%) when using JSON on the wire. 



### #log_linked_dataset_query_user_email
    
    
    def log_linked_dataset_query_user_email() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. By default, false. If true, the Listing has an email sharing mandate enabled. 



### #log_linked_dataset_query_user_email=
    
    
    def log_linked_dataset_query_user_email=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. By default, false. If true, the Listing has an email sharing mandate enabled. 



**Returns**

  * (::Boolean) — Optional. By default, false. If true, the Listing has an email sharing mandate enabled. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Output only. The resource name of the listing. e.g. `projects/myproject/locations/us/dataExchanges/123/listings/456`



### #primary_contact
    
    
    def primary_contact() -> ::String

**Returns**

  * (::String) — Optional. Email or URL of the primary point of contact of the listing. Max Length: 1000 bytes. 



### #primary_contact=
    
    
    def primary_contact=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Email or URL of the primary point of contact of the listing. Max Length: 1000 bytes. 



**Returns**

  * (::String) — Optional. Email or URL of the primary point of contact of the listing. Max Length: 1000 bytes. 



### #publisher
    
    
    def publisher() -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::Publisher

**Returns**

  * ([::Google::Cloud::Bigquery::AnalyticsHub::V1::Publisher](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-Publisher)) — Optional. Details of the publisher who owns the listing and who can share the source data. 



### #publisher=
    
    
    def publisher=(value) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::Publisher

**Parameter**

  * **value** ([::Google::Cloud::Bigquery::AnalyticsHub::V1::Publisher](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-Publisher)) — Optional. Details of the publisher who owns the listing and who can share the source data. 



**Returns**

  * ([::Google::Cloud::Bigquery::AnalyticsHub::V1::Publisher](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-Publisher)) — Optional. Details of the publisher who owns the listing and who can share the source data. 



### #pubsub_topic
    
    
    def pubsub_topic() -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::Listing::PubSubTopicSource

**Returns**

  * ([::Google::Cloud::Bigquery::AnalyticsHub::V1::Listing::PubSubTopicSource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-Listing-PubSubTopicSource)) — Pub/Sub topic source.

Note: The following fields are mutually exclusive: `pubsub_topic`, `bigquery_dataset`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #pubsub_topic=
    
    
    def pubsub_topic=(value) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::Listing::PubSubTopicSource

**Parameter**

  * **value** ([::Google::Cloud::Bigquery::AnalyticsHub::V1::Listing::PubSubTopicSource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-Listing-PubSubTopicSource)) — Pub/Sub topic source.

Note: The following fields are mutually exclusive: `pubsub_topic`, `bigquery_dataset`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Bigquery::AnalyticsHub::V1::Listing::PubSubTopicSource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-Listing-PubSubTopicSource)) — Pub/Sub topic source.

Note: The following fields are mutually exclusive: `pubsub_topic`, `bigquery_dataset`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #request_access
    
    
    def request_access() -> ::String

**Returns**

  * (::String) — Optional. Email or URL of the request access of the listing. Subscribers can use this reference to request access. Max Length: 1000 bytes. 



### #request_access=
    
    
    def request_access=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Email or URL of the request access of the listing. Subscribers can use this reference to request access. Max Length: 1000 bytes. 



**Returns**

  * (::String) — Optional. Email or URL of the request access of the listing. Subscribers can use this reference to request access. Max Length: 1000 bytes. 



### #resource_type
    
    
    def resource_type() -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::SharedResourceType

**Returns**

  * ([::Google::Cloud::Bigquery::AnalyticsHub::V1::SharedResourceType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-SharedResourceType)) — Output only. Listing shared asset type. 



### #restricted_export_config
    
    
    def restricted_export_config() -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::Listing::RestrictedExportConfig

**Returns**

  * ([::Google::Cloud::Bigquery::AnalyticsHub::V1::Listing::RestrictedExportConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-Listing-RestrictedExportConfig)) — Optional. If set, restricted export configuration will be propagated and enforced on the linked dataset. 



### #restricted_export_config=
    
    
    def restricted_export_config=(value) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::Listing::RestrictedExportConfig

**Parameter**

  * **value** ([::Google::Cloud::Bigquery::AnalyticsHub::V1::Listing::RestrictedExportConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-Listing-RestrictedExportConfig)) — Optional. If set, restricted export configuration will be propagated and enforced on the linked dataset. 



**Returns**

  * ([::Google::Cloud::Bigquery::AnalyticsHub::V1::Listing::RestrictedExportConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-Listing-RestrictedExportConfig)) — Optional. If set, restricted export configuration will be propagated and enforced on the linked dataset. 



### #state
    
    
    def state() -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::Listing::State

**Returns**

  * ([::Google::Cloud::Bigquery::AnalyticsHub::V1::Listing::State](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-Listing-State)) — Output only. Current state of the listing. 



### #stored_procedure_config
    
    
    def stored_procedure_config() -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::StoredProcedureConfig

**Returns**

  * ([::Google::Cloud::Bigquery::AnalyticsHub::V1::StoredProcedureConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-StoredProcedureConfig)) — Optional. If set, stored procedure configuration will be propagated and enforced on the linked dataset. 



### #stored_procedure_config=
    
    
    def stored_procedure_config=(value) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::StoredProcedureConfig

**Parameter**

  * **value** ([::Google::Cloud::Bigquery::AnalyticsHub::V1::StoredProcedureConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-StoredProcedureConfig)) — Optional. If set, stored procedure configuration will be propagated and enforced on the linked dataset. 



**Returns**

  * ([::Google::Cloud::Bigquery::AnalyticsHub::V1::StoredProcedureConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-StoredProcedureConfig)) — Optional. If set, stored procedure configuration will be propagated and enforced on the linked dataset. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
