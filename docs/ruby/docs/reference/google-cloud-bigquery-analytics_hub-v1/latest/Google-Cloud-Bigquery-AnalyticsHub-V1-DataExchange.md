---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-DataExchange/
title: Analytics Hub V1 API - Class Google::Cloud::Bigquery::AnalyticsHub::V1::DataExchange (v0.20.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:05:49.376025+00:00
---

# Analytics Hub V1 API - Class Google::Cloud::Bigquery::AnalyticsHub::V1::DataExchange (v0.20.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-DataExchange/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Analytics Hub V1 API - Class Google::Cloud::Bigquery::AnalyticsHub::V1::DataExchange (v0.20.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.20.1 (latest)  0.20.0  0.19.0  0.18.0  0.17.0  0.16.1  0.15.0  0.14.0  0.13.1  0.12.0  0.11.1  0.10.0  0.9.0  0.8.1  0.7.0  0.6.0  0.5.2  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Analytics Hub V1 API class Google::Cloud::Bigquery::AnalyticsHub::V1::DataExchange.

A data exchange is a container that lets you share data. Along with the descriptive information about the data exchange, it contains listings that reference shared datasets.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #description
    
    
    def description() -> ::String

**Returns**

  * (::String) — Optional. Description of the data exchange. The description must not contain Unicode non-characters as well as C0 and C1 control codes except tabs (HT), new lines (LF), carriage returns (CR), and page breaks (FF). Default value is an empty string. Max length: 2000 bytes. 



### #description=
    
    
    def description=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Description of the data exchange. The description must not contain Unicode non-characters as well as C0 and C1 control codes except tabs (HT), new lines (LF), carriage returns (CR), and page breaks (FF). Default value is an empty string. Max length: 2000 bytes. 



**Returns**

  * (::String) — Optional. Description of the data exchange. The description must not contain Unicode non-characters as well as C0 and C1 control codes except tabs (HT), new lines (LF), carriage returns (CR), and page breaks (FF). Default value is an empty string. Max length: 2000 bytes. 



### #discovery_type
    
    
    def discovery_type() -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::DiscoveryType

**Returns**

  * ([::Google::Cloud::Bigquery::AnalyticsHub::V1::DiscoveryType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-DiscoveryType)) — Optional. Type of discovery on the discovery page for all the listings under this exchange. Updating this field also updates (overwrites) the discovery_type field for all the listings under this exchange. 



### #discovery_type=
    
    
    def discovery_type=(value) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::DiscoveryType

**Parameter**

  * **value** ([::Google::Cloud::Bigquery::AnalyticsHub::V1::DiscoveryType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-DiscoveryType)) — Optional. Type of discovery on the discovery page for all the listings under this exchange. Updating this field also updates (overwrites) the discovery_type field for all the listings under this exchange. 



**Returns**

  * ([::Google::Cloud::Bigquery::AnalyticsHub::V1::DiscoveryType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-DiscoveryType)) — Optional. Type of discovery on the discovery page for all the listings under this exchange. Updating this field also updates (overwrites) the discovery_type field for all the listings under this exchange. 



### #display_name
    
    
    def display_name() -> ::String

**Returns**

  * (::String) — Required. Human-readable display name of the data exchange. The display name must contain only Unicode letters, numbers (0-9), underscores (_), dashes (-), spaces ( ), ampersands (&) and must not start or end with spaces. Default value is an empty string. Max length: 63 bytes. 



### #display_name=
    
    
    def display_name=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Human-readable display name of the data exchange. The display name must contain only Unicode letters, numbers (0-9), underscores (_), dashes (-), spaces ( ), ampersands (&) and must not start or end with spaces. Default value is an empty string. Max length: 63 bytes. 



**Returns**

  * (::String) — Required. Human-readable display name of the data exchange. The display name must contain only Unicode letters, numbers (0-9), underscores (_), dashes (-), spaces ( ), ampersands (&) and must not start or end with spaces. Default value is an empty string. Max length: 63 bytes. 



### #documentation
    
    
    def documentation() -> ::String

**Returns**

  * (::String) — Optional. Documentation describing the data exchange. 



### #documentation=
    
    
    def documentation=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Documentation describing the data exchange. 



**Returns**

  * (::String) — Optional. Documentation describing the data exchange. 



### #icon
    
    
    def icon() -> ::String

**Returns**

  * (::String) — Optional. Base64 encoded image representing the data exchange. Max Size: 3.0MiB Expected image dimensions are 512x512 pixels, however the API only performs validation on size of the encoded data. Note: For byte fields, the content of the fields are base64-encoded (which increases the size of the data by 33-36%) when using JSON on the wire. 



### #icon=
    
    
    def icon=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Base64 encoded image representing the data exchange. Max Size: 3.0MiB Expected image dimensions are 512x512 pixels, however the API only performs validation on size of the encoded data. Note: For byte fields, the content of the fields are base64-encoded (which increases the size of the data by 33-36%) when using JSON on the wire. 



**Returns**

  * (::String) — Optional. Base64 encoded image representing the data exchange. Max Size: 3.0MiB Expected image dimensions are 512x512 pixels, however the API only performs validation on size of the encoded data. Note: For byte fields, the content of the fields are base64-encoded (which increases the size of the data by 33-36%) when using JSON on the wire. 



### #listing_count
    
    
    def listing_count() -> ::Integer

**Returns**

  * (::Integer) — Output only. Number of listings contained in the data exchange. 



### #log_linked_dataset_query_user_email
    
    
    def log_linked_dataset_query_user_email() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. By default, false. If true, the DataExchange has an email sharing mandate enabled. 



### #log_linked_dataset_query_user_email=
    
    
    def log_linked_dataset_query_user_email=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. By default, false. If true, the DataExchange has an email sharing mandate enabled. 



**Returns**

  * (::Boolean) — Optional. By default, false. If true, the DataExchange has an email sharing mandate enabled. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Output only. The resource name of the data exchange. e.g. `projects/myproject/locations/us/dataExchanges/123`. 



### #primary_contact
    
    
    def primary_contact() -> ::String

**Returns**

  * (::String) — Optional. Email or URL of the primary point of contact of the data exchange. Max Length: 1000 bytes. 



### #primary_contact=
    
    
    def primary_contact=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Email or URL of the primary point of contact of the data exchange. Max Length: 1000 bytes. 



**Returns**

  * (::String) — Optional. Email or URL of the primary point of contact of the data exchange. Max Length: 1000 bytes. 



### #sharing_environment_config
    
    
    def sharing_environment_config() -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::SharingEnvironmentConfig

**Returns**

  * ([::Google::Cloud::Bigquery::AnalyticsHub::V1::SharingEnvironmentConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-SharingEnvironmentConfig)) — Optional. Configurable data sharing environment option for a data exchange. 



### #sharing_environment_config=
    
    
    def sharing_environment_config=(value) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::SharingEnvironmentConfig

**Parameter**

  * **value** ([::Google::Cloud::Bigquery::AnalyticsHub::V1::SharingEnvironmentConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-SharingEnvironmentConfig)) — Optional. Configurable data sharing environment option for a data exchange. 



**Returns**

  * ([::Google::Cloud::Bigquery::AnalyticsHub::V1::SharingEnvironmentConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-SharingEnvironmentConfig)) — Optional. Configurable data sharing environment option for a data exchange. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
