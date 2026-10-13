---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1beta/latest/Google-Cloud-NetworkConnectivity-V1beta-RejectSpokeUpdateRequest/
title: Network Connectivity V1BETA API - Class Google::Cloud::NetworkConnectivity::V1beta::RejectSpokeUpdateRequest (v0.3.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:14:32.825258+00:00
---

# Network Connectivity V1BETA API - Class Google::Cloud::NetworkConnectivity::V1beta::RejectSpokeUpdateRequest (v0.3.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1beta/latest/Google-Cloud-NetworkConnectivity-V1beta-RejectSpokeUpdateRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Network Connectivity V1BETA API - Class Google::Cloud::NetworkConnectivity::V1beta::RejectSpokeUpdateRequest (v0.3.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.3.2 (latest)  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Network Connectivity V1BETA API class Google::Cloud::NetworkConnectivity::V1beta::RejectSpokeUpdateRequest.

The request for [HubService.RejectSpokeUpdate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1beta/latest/Google-Cloud-NetworkConnectivity-V1beta-HubService-Client#Google__Cloud__NetworkConnectivity__V1beta__HubService__Client_reject_spoke_update_instance_ "Google::Cloud::NetworkConnectivity::V1beta::HubService::Client#reject_spoke_update \(method\)").

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #details
    
    
    def details() -> ::String

**Returns**

  * (::String) — Optional. Additional information provided by the hub administrator. 



### #details=
    
    
    def details=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Additional information provided by the hub administrator. 



**Returns**

  * (::String) — Optional. Additional information provided by the hub administrator. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Required. The name of the hub to reject spoke update. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The name of the hub to reject spoke update. 



**Returns**

  * (::String) — Required. The name of the hub to reject spoke update. 



### #request_id
    
    
    def request_id() -> ::String

**Returns**

  * (::String) — Optional. A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server knows to ignore the request if it has already been completed. The server guarantees that a request doesn't result in creation of duplicate commitments for at least 60 minutes.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check to see whether the original operation was received. If it was, the server ignores the second request. This behavior prevents clients from mistakenly creating duplicate commitments.

The request ID must be a valid UUID, with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




### #request_id=
    
    
    def request_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server knows to ignore the request if it has already been completed. The server guarantees that a request doesn't result in creation of duplicate commitments for at least 60 minutes.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check to see whether the original operation was received. If it was, the server ignores the second request. This behavior prevents clients from mistakenly creating duplicate commitments.

The request ID must be a valid UUID, with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




**Returns**

  * (::String) — Optional. A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server knows to ignore the request if it has already been completed. The server guarantees that a request doesn't result in creation of duplicate commitments for at least 60 minutes.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check to see whether the original operation was received. If it was, the server ignores the second request. This behavior prevents clients from mistakenly creating duplicate commitments.

The request ID must be a valid UUID, with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




### #spoke_etag
    
    
    def spoke_etag() -> ::String

**Returns**

  * (::String) — Required. The etag of the spoke to reject update. 



### #spoke_etag=
    
    
    def spoke_etag=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The etag of the spoke to reject update. 



**Returns**

  * (::String) — Required. The etag of the spoke to reject update. 



### #spoke_uri
    
    
    def spoke_uri() -> ::String

**Returns**

  * (::String) — Required. The URI of the spoke to reject update. 



### #spoke_uri=
    
    
    def spoke_uri=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The URI of the spoke to reject update. 



**Returns**

  * (::String) — Required. The URI of the spoke to reject update. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
