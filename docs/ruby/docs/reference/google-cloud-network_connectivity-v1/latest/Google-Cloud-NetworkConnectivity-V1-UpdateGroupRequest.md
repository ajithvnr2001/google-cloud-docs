---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-UpdateGroupRequest/
title: Network Connectivity V1 API - Class Google::Cloud::NetworkConnectivity::V1::UpdateGroupRequest (v1.15.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:25:10.931595+00:00
---

# Network Connectivity V1 API - Class Google::Cloud::NetworkConnectivity::V1::UpdateGroupRequest (v1.15.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-UpdateGroupRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Network Connectivity V1 API - Class Google::Cloud::NetworkConnectivity::V1::UpdateGroupRequest (v1.15.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.15.0 (latest)  1.14.0  1.13.0  1.12.0  1.11.0  1.10.1  1.9.0  1.8.0  1.7.0  1.6.0  1.5.1  1.4.0  1.3.0  1.2.0  1.1.0  1.0.1  0.10.0  0.9.2  0.8.0  0.7.0  0.6.1  0.5.0  0.4.1  0.3.0  0.2.0  0.1.4 

Reference documentation and code samples for the Network Connectivity V1 API class Google::Cloud::NetworkConnectivity::V1::UpdateGroupRequest.

Request for [HubService.UpdateGroup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-HubService-Client#Google__Cloud__NetworkConnectivity__V1__HubService__Client_update_group_instance_ "Google::Cloud::NetworkConnectivity::V1::HubService::Client#update_group \(method\)") method.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #group
    
    
    def group() -> ::Google::Cloud::NetworkConnectivity::V1::Group

**Returns**

  * ([::Google::Cloud::NetworkConnectivity::V1::Group](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-Group)) — Required. The state that the group should be in after the update. 



### #group=
    
    
    def group=(value) -> ::Google::Cloud::NetworkConnectivity::V1::Group

**Parameter**

  * **value** ([::Google::Cloud::NetworkConnectivity::V1::Group](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-Group)) — Required. The state that the group should be in after the update. 



**Returns**

  * ([::Google::Cloud::NetworkConnectivity::V1::Group](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-Group)) — Required. The state that the group should be in after the update. 



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




### #update_mask
    
    
    def update_mask() -> ::Google::Protobuf::FieldMask

**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Protobuf-FieldMask)) — Optional. In the case of an update to an existing group, field mask is used to specify the fields to be overwritten. The fields specified in the update_mask are relative to the resource, not the full request. A field is overwritten if it is in the mask. If the user does not provide a mask, then all fields are overwritten. 



### #update_mask=
    
    
    def update_mask=(value) -> ::Google::Protobuf::FieldMask

**Parameter**

  * **value** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Protobuf-FieldMask)) — Optional. In the case of an update to an existing group, field mask is used to specify the fields to be overwritten. The fields specified in the update_mask are relative to the resource, not the full request. A field is overwritten if it is in the mask. If the user does not provide a mask, then all fields are overwritten. 



**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Protobuf-FieldMask)) — Optional. In the case of an update to an existing group, field mask is used to specify the fields to be overwritten. The fields specified in the update_mask are relative to the resource, not the full request. A field is overwritten if it is in the mask. If the user does not provide a mask, then all fields are overwritten. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-26 UTC."],[],[]] 
