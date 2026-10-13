---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-license_manager-v1/latest/Google-Cloud-LicenseManager-V1-AggregateUsageRequest/
title: License Manager V1 API - Class Google::Cloud::LicenseManager::V1::AggregateUsageRequest (v1.0.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:45:24.765185+00:00
---

# License Manager V1 API - Class Google::Cloud::LicenseManager::V1::AggregateUsageRequest (v1.0.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-license_manager-v1/latest/Google-Cloud-LicenseManager-V1-AggregateUsageRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  License Manager V1 API - Class Google::Cloud::LicenseManager::V1::AggregateUsageRequest (v1.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0 (latest)  0.6.0  0.5.0  0.4.0  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the License Manager V1 API class Google::Cloud::LicenseManager::V1::AggregateUsageRequest.

Message for requesting aggregate of Usage per configuration.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #end_time
    
    
    def end_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-license_manager-v1/latest/Google-Protobuf-Timestamp)) — Required. Usage track is always for a month. This parameter is for the end time of the month. 



### #end_time=
    
    
    def end_time=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-license_manager-v1/latest/Google-Protobuf-Timestamp)) — Required. Usage track is always for a month. This parameter is for the end time of the month. 



**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-license_manager-v1/latest/Google-Protobuf-Timestamp)) — Required. Usage track is always for a month. This parameter is for the end time of the month. 



### #filter
    
    
    def filter() -> ::String

**Returns**

  * (::String) — Optional. Filtering results 



### #filter=
    
    
    def filter=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Filtering results 



**Returns**

  * (::String) — Optional. Filtering results 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Required. Parent value for AggregateUsageRequest 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Parent value for AggregateUsageRequest 



**Returns**

  * (::String) — Required. Parent value for AggregateUsageRequest 



### #order_by
    
    
    def order_by() -> ::String

**Returns**

  * (::String) — Optional. Hint for how to order the results 



### #order_by=
    
    
    def order_by=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Hint for how to order the results 



**Returns**

  * (::String) — Optional. Hint for how to order the results 



### #page_size
    
    
    def page_size() -> ::Integer

**Returns**

  * (::Integer) — Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default. 



### #page_size=
    
    
    def page_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default. 



**Returns**

  * (::Integer) — Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default. 



### #page_token
    
    
    def page_token() -> ::String

**Returns**

  * (::String) — Optional. A token identifying a page of results the server should return. 



### #page_token=
    
    
    def page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. A token identifying a page of results the server should return. 



**Returns**

  * (::String) — Optional. A token identifying a page of results the server should return. 



### #start_time
    
    
    def start_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-license_manager-v1/latest/Google-Protobuf-Timestamp)) — Required. Licenses are purchased per month - so usage track needs start time of a month. 



### #start_time=
    
    
    def start_time=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-license_manager-v1/latest/Google-Protobuf-Timestamp)) — Required. Licenses are purchased per month - so usage track needs start time of a month. 



**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-license_manager-v1/latest/Google-Protobuf-Timestamp)) — Required. Licenses are purchased per month - so usage track needs start time of a month. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-04 UTC."],[],[]] 
