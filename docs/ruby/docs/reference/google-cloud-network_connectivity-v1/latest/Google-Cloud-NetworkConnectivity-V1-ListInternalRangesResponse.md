---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-ListInternalRangesResponse/
title: Network Connectivity V1 API - Class Google::Cloud::NetworkConnectivity::V1::ListInternalRangesResponse (v1.15.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:09:24.440015+00:00
---

# Network Connectivity V1 API - Class Google::Cloud::NetworkConnectivity::V1::ListInternalRangesResponse (v1.15.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-ListInternalRangesResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Network Connectivity V1 API - Class Google::Cloud::NetworkConnectivity::V1::ListInternalRangesResponse (v1.15.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.15.0 (latest)  1.14.0  1.13.0  1.12.0  1.11.0  1.10.1  1.9.0  1.8.0  1.7.0  1.6.0  1.5.1  1.4.0  1.3.0  1.2.0  1.1.0  1.0.1  0.10.0  0.9.2  0.8.0  0.7.0  0.6.1  0.5.0  0.4.1  0.3.0  0.2.0  0.1.4 

Reference documentation and code samples for the Network Connectivity V1 API class Google::Cloud::NetworkConnectivity::V1::ListInternalRangesResponse.

Response for InternalRange.ListInternalRanges

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #internal_ranges
    
    
    def internal_ranges() -> ::Array<::Google::Cloud::NetworkConnectivity::V1::InternalRange>

**Returns**

  * (::Array<[::Google::Cloud::NetworkConnectivity::V1::InternalRange](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-InternalRange)>) — Internal ranges to be returned. 



### #internal_ranges=
    
    
    def internal_ranges=(value) -> ::Array<::Google::Cloud::NetworkConnectivity::V1::InternalRange>

**Parameter**

  * **value** (::Array<[::Google::Cloud::NetworkConnectivity::V1::InternalRange](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-InternalRange)>) — Internal ranges to be returned. 



**Returns**

  * (::Array<[::Google::Cloud::NetworkConnectivity::V1::InternalRange](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-InternalRange)>) — Internal ranges to be returned. 



### #next_page_token
    
    
    def next_page_token() -> ::String

**Returns**

  * (::String) — The next pagination token in the List response. It should be used as page_token for the following request. An empty value means no more result. 



### #next_page_token=
    
    
    def next_page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — The next pagination token in the List response. It should be used as page_token for the following request. An empty value means no more result. 



**Returns**

  * (::String) — The next pagination token in the List response. It should be used as page_token for the following request. An empty value means no more result. 



### #unreachable
    
    
    def unreachable() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Locations that could not be reached. 



### #unreachable=
    
    
    def unreachable=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Locations that could not be reached. 



**Returns**

  * (::Array<::String>) — Locations that could not be reached. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-26 UTC."],[],[]] 
