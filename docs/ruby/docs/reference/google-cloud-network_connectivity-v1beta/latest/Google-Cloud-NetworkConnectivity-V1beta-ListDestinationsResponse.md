---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1beta/latest/Google-Cloud-NetworkConnectivity-V1beta-ListDestinationsResponse/
title: Network Connectivity V1BETA API - Class Google::Cloud::NetworkConnectivity::V1beta::ListDestinationsResponse (v0.3.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:34:57.353089+00:00
---

# Network Connectivity V1BETA API - Class Google::Cloud::NetworkConnectivity::V1beta::ListDestinationsResponse (v0.3.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1beta/latest/Google-Cloud-NetworkConnectivity-V1beta-ListDestinationsResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Network Connectivity V1BETA API - Class Google::Cloud::NetworkConnectivity::V1beta::ListDestinationsResponse (v0.3.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.3.2 (latest)  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Network Connectivity V1BETA API class Google::Cloud::NetworkConnectivity::V1beta::ListDestinationsResponse.

Response message to list `Destination` resources.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #destinations
    
    
    def destinations() -> ::Array<::Google::Cloud::NetworkConnectivity::V1beta::Destination>

**Returns**

  * (::Array<[::Google::Cloud::NetworkConnectivity::V1beta::Destination](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1beta/latest/Google-Cloud-NetworkConnectivity-V1beta-Destination)>) — The list of `Destination` resources to be listed. 



### #destinations=
    
    
    def destinations=(value) -> ::Array<::Google::Cloud::NetworkConnectivity::V1beta::Destination>

**Parameter**

  * **value** (::Array<[::Google::Cloud::NetworkConnectivity::V1beta::Destination](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1beta/latest/Google-Cloud-NetworkConnectivity-V1beta-Destination)>) — The list of `Destination` resources to be listed. 



**Returns**

  * (::Array<[::Google::Cloud::NetworkConnectivity::V1beta::Destination](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1beta/latest/Google-Cloud-NetworkConnectivity-V1beta-Destination)>) — The list of `Destination` resources to be listed. 



### #next_page_token
    
    
    def next_page_token() -> ::String

**Returns**

  * (::String) — The next page token. 



### #next_page_token=
    
    
    def next_page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — The next page token. 



**Returns**

  * (::String) — The next page token. 



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

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
