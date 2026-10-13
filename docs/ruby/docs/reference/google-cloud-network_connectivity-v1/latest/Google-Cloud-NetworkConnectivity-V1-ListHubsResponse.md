---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-ListHubsResponse/
title: Network Connectivity V1 API - Class Google::Cloud::NetworkConnectivity::V1::ListHubsResponse (v1.15.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:42:33.776529+00:00
---

# Network Connectivity V1 API - Class Google::Cloud::NetworkConnectivity::V1::ListHubsResponse (v1.15.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-ListHubsResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Network Connectivity V1 API - Class Google::Cloud::NetworkConnectivity::V1::ListHubsResponse (v1.15.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.15.0 (latest)  1.14.0  1.13.0  1.12.0  1.11.0  1.10.1  1.9.0  1.8.0  1.7.0  1.6.0  1.5.1  1.4.0  1.3.0  1.2.0  1.1.0  1.0.1  0.10.0  0.9.2  0.8.0  0.7.0  0.6.1  0.5.0  0.4.1  0.3.0  0.2.0  0.1.4 

Reference documentation and code samples for the Network Connectivity V1 API class Google::Cloud::NetworkConnectivity::V1::ListHubsResponse.

Response for [HubService.ListHubs](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-HubService-Client#Google__Cloud__NetworkConnectivity__V1__HubService__Client_list_hubs_instance_ "Google::Cloud::NetworkConnectivity::V1::HubService::Client#list_hubs \(method\)") method.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #hubs
    
    
    def hubs() -> ::Array<::Google::Cloud::NetworkConnectivity::V1::Hub>

**Returns**

  * (::Array<[::Google::Cloud::NetworkConnectivity::V1::Hub](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-Hub)>) — The requested hubs. 



### #hubs=
    
    
    def hubs=(value) -> ::Array<::Google::Cloud::NetworkConnectivity::V1::Hub>

**Parameter**

  * **value** (::Array<[::Google::Cloud::NetworkConnectivity::V1::Hub](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-Hub)>) — The requested hubs. 



**Returns**

  * (::Array<[::Google::Cloud::NetworkConnectivity::V1::Hub](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-Hub)>) — The requested hubs. 



### #next_page_token
    
    
    def next_page_token() -> ::String

**Returns**

  * (::String) — The token for the next page of the response. To see more results, use this value as the page_token for your next request. If this value is empty, there are no more results. 



### #next_page_token=
    
    
    def next_page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — The token for the next page of the response. To see more results, use this value as the page_token for your next request. If this value is empty, there are no more results. 



**Returns**

  * (::String) — The token for the next page of the response. To see more results, use this value as the page_token for your next request. If this value is empty, there are no more results. 



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
