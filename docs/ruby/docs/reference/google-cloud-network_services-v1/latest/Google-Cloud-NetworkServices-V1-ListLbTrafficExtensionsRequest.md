---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_services-v1/latest/Google-Cloud-NetworkServices-V1-ListLbTrafficExtensionsRequest/
title: Network Services V1 API - Class Google::Cloud::NetworkServices::V1::ListLbTrafficExtensionsRequest (v2.12.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:52:32.110495+00:00
---

# Network Services V1 API - Class Google::Cloud::NetworkServices::V1::ListLbTrafficExtensionsRequest (v2.12.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_services-v1/latest/Google-Cloud-NetworkServices-V1-ListLbTrafficExtensionsRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Network Services V1 API - Class Google::Cloud::NetworkServices::V1::ListLbTrafficExtensionsRequest (v2.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.12.0 (latest)  2.11.0  2.10.1  2.9.0  2.8.0  2.7.0  2.6.1  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.1  1.2.0  1.1.0  1.0.1  0.2.0  0.1.0 

Reference documentation and code samples for the Network Services V1 API class Google::Cloud::NetworkServices::V1::ListLbTrafficExtensionsRequest.

Message for requesting list of `LbTrafficExtension` resources.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #filter
    
    
    def filter() -> ::String

**Returns**

  * (::String) — Optional. Filtering results. 



### #filter=
    
    
    def filter=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Filtering results. 



**Returns**

  * (::String) — Optional. Filtering results. 



### #order_by
    
    
    def order_by() -> ::String

**Returns**

  * (::String) — Optional. Hint about how to order the results. 



### #order_by=
    
    
    def order_by=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Hint about how to order the results. 



**Returns**

  * (::String) — Optional. Hint about how to order the results. 



### #page_size
    
    
    def page_size() -> ::Integer

**Returns**

  * (::Integer) — Optional. Requested page size. The server might return fewer items than requested. If unspecified, the server picks an appropriate default. 



### #page_size=
    
    
    def page_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. Requested page size. The server might return fewer items than requested. If unspecified, the server picks an appropriate default. 



**Returns**

  * (::Integer) — Optional. Requested page size. The server might return fewer items than requested. If unspecified, the server picks an appropriate default. 



### #page_token
    
    
    def page_token() -> ::String

**Returns**

  * (::String) — Optional. A token identifying a page of results that the server returns. 



### #page_token=
    
    
    def page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. A token identifying a page of results that the server returns. 



**Returns**

  * (::String) — Optional. A token identifying a page of results that the server returns. 



### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. The project and location from which the `LbTrafficExtension` resources are listed. These values are specified in the following format: `projects/{project}/locations/{location}`. 



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The project and location from which the `LbTrafficExtension` resources are listed. These values are specified in the following format: `projects/{project}/locations/{location}`. 



**Returns**

  * (::String) — Required. The project and location from which the `LbTrafficExtension` resources are listed. These values are specified in the following format: `projects/{project}/locations/{location}`. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-03 UTC."],[],[]] 
