---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-ListHubSpokesRequest/
title: Network Connectivity V1 API - Class Google::Cloud::NetworkConnectivity::V1::ListHubSpokesRequest (v1.15.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:28:37.570898+00:00
---

# Network Connectivity V1 API - Class Google::Cloud::NetworkConnectivity::V1::ListHubSpokesRequest (v1.15.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-ListHubSpokesRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Network Connectivity V1 API - Class Google::Cloud::NetworkConnectivity::V1::ListHubSpokesRequest (v1.15.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.15.0 (latest)  1.14.0  1.13.0  1.12.0  1.11.0  1.10.1  1.9.0  1.8.0  1.7.0  1.6.0  1.5.1  1.4.0  1.3.0  1.2.0  1.1.0  1.0.1  0.10.0  0.9.2  0.8.0  0.7.0  0.6.1  0.5.0  0.4.1  0.3.0  0.2.0  0.1.4 

Reference documentation and code samples for the Network Connectivity V1 API class Google::Cloud::NetworkConnectivity::V1::ListHubSpokesRequest.

The request for [HubService.ListHubSpokes](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-HubService-Client#Google__Cloud__NetworkConnectivity__V1__HubService__Client_list_hub_spokes_instance_ "Google::Cloud::NetworkConnectivity::V1::HubService::Client#list_hub_spokes \(method\)").

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

  * (::String) — An expression that filters the list of results. 



### #filter=
    
    
    def filter=(value) -> ::String

**Parameter**

  * **value** (::String) — An expression that filters the list of results. 



**Returns**

  * (::String) — An expression that filters the list of results. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Required. The name of the hub. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The name of the hub. 



**Returns**

  * (::String) — Required. The name of the hub. 



### #order_by
    
    
    def order_by() -> ::String

**Returns**

  * (::String) — Sort the results by name or create_time. 



### #order_by=
    
    
    def order_by=(value) -> ::String

**Parameter**

  * **value** (::String) — Sort the results by name or create_time. 



**Returns**

  * (::String) — Sort the results by name or create_time. 



### #page_size
    
    
    def page_size() -> ::Integer

**Returns**

  * (::Integer) — The maximum number of results to return per page. 



### #page_size=
    
    
    def page_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The maximum number of results to return per page. 



**Returns**

  * (::Integer) — The maximum number of results to return per page. 



### #page_token
    
    
    def page_token() -> ::String

**Returns**

  * (::String) — The page token. 



### #page_token=
    
    
    def page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — The page token. 



**Returns**

  * (::String) — The page token. 



### #spoke_locations
    
    
    def spoke_locations() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — A list of locations. Specify one of the following: `[global]`, a single region (for example, `[us-central1]`), or a combination of values (for example, `[global, us-central1, us-west1]`). If the spoke_locations field is populated, the list of results includes only spokes in the specified location. If the spoke_locations field is not populated, the list of results includes spokes in all locations. 



### #spoke_locations=
    
    
    def spoke_locations=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — A list of locations. Specify one of the following: `[global]`, a single region (for example, `[us-central1]`), or a combination of values (for example, `[global, us-central1, us-west1]`). If the spoke_locations field is populated, the list of results includes only spokes in the specified location. If the spoke_locations field is not populated, the list of results includes spokes in all locations. 



**Returns**

  * (::Array<::String>) — A list of locations. Specify one of the following: `[global]`, a single region (for example, `[us-central1]`), or a combination of values (for example, `[global, us-central1, us-west1]`). If the spoke_locations field is populated, the list of results includes only spokes in the specified location. If the spoke_locations field is not populated, the list of results includes spokes in all locations. 



### #view
    
    
    def view() -> ::Google::Cloud::NetworkConnectivity::V1::ListHubSpokesRequest::SpokeView

**Returns**

  * ([::Google::Cloud::NetworkConnectivity::V1::ListHubSpokesRequest::SpokeView](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-ListHubSpokesRequest-SpokeView)) — The view of the spoke to return. The view that you use determines which spoke fields are included in the response. 



### #view=
    
    
    def view=(value) -> ::Google::Cloud::NetworkConnectivity::V1::ListHubSpokesRequest::SpokeView

**Parameter**

  * **value** ([::Google::Cloud::NetworkConnectivity::V1::ListHubSpokesRequest::SpokeView](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-ListHubSpokesRequest-SpokeView)) — The view of the spoke to return. The view that you use determines which spoke fields are included in the response. 



**Returns**

  * ([::Google::Cloud::NetworkConnectivity::V1::ListHubSpokesRequest::SpokeView](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-ListHubSpokesRequest-SpokeView)) — The view of the spoke to return. The view that you use determines which spoke fields are included in the response. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-26 UTC."],[],[]] 
