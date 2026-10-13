---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vmware_engine-v1/latest/Google-Cloud-VmwareEngine-V1-RevokeDnsBindPermissionRequest/
title: Google Cloud VMware Engine V1 API - Class Google::Cloud::VmwareEngine::V1::RevokeDnsBindPermissionRequest (v1.5.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:37:13.142759+00:00
---

# Google Cloud VMware Engine V1 API - Class Google::Cloud::VmwareEngine::V1::RevokeDnsBindPermissionRequest (v1.5.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vmware_engine-v1/latest/Google-Cloud-VmwareEngine-V1-RevokeDnsBindPermissionRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud VMware Engine V1 API - Class Google::Cloud::VmwareEngine::V1::RevokeDnsBindPermissionRequest (v1.5.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.5.2 (latest)  1.5.1  1.4.1  1.3.1  1.2.0  1.1.0  1.0.1  0.11.0  0.10.0  0.9.2  0.8.0  0.7.1  0.6.1  0.5.0  0.4.0  0.3.1  0.2.0  0.1.1 

Reference documentation and code samples for the Google Cloud VMware Engine V1 API class Google::Cloud::VmwareEngine::V1::RevokeDnsBindPermissionRequest.

Request message for [VmwareEngine.RevokeDnsBindPermission](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vmware_engine-v1/latest/Google-Cloud-VmwareEngine-V1-VmwareEngine-Client#Google__Cloud__VmwareEngine__V1__VmwareEngine__Client_revoke_dns_bind_permission_instance_ "Google::Cloud::VmwareEngine::V1::VmwareEngine::Client#revoke_dns_bind_permission \(method\)")

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Required. The name of the resource which stores the users/service accounts having the permission to bind to the corresponding intranet VPC of the consumer project. DnsBindPermission is a global resource. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: `projects/my-project/locations/global/dnsBindPermission`



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The name of the resource which stores the users/service accounts having the permission to bind to the corresponding intranet VPC of the consumer project. DnsBindPermission is a global resource. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: `projects/my-project/locations/global/dnsBindPermission`



**Returns**

  * (::String) — Required. The name of the resource which stores the users/service accounts having the permission to bind to the corresponding intranet VPC of the consumer project. DnsBindPermission is a global resource. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: `projects/my-project/locations/global/dnsBindPermission`



### #principal
    
    
    def principal() -> ::Google::Cloud::VmwareEngine::V1::Principal

**Returns**

  * ([::Google::Cloud::VmwareEngine::V1::Principal](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vmware_engine-v1/latest/Google-Cloud-VmwareEngine-V1-Principal)) — Required. The consumer provided user/service account which needs to be granted permission to bind with the intranet VPC corresponding to the consumer project. 



### #principal=
    
    
    def principal=(value) -> ::Google::Cloud::VmwareEngine::V1::Principal

**Parameter**

  * **value** ([::Google::Cloud::VmwareEngine::V1::Principal](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vmware_engine-v1/latest/Google-Cloud-VmwareEngine-V1-Principal)) — Required. The consumer provided user/service account which needs to be granted permission to bind with the intranet VPC corresponding to the consumer project. 



**Returns**

  * ([::Google::Cloud::VmwareEngine::V1::Principal](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vmware_engine-v1/latest/Google-Cloud-VmwareEngine-V1-Principal)) — Required. The consumer provided user/service account which needs to be granted permission to bind with the intranet VPC corresponding to the consumer project. 



### #request_id
    
    
    def request_id() -> ::String

**Returns**

  * (::String) — Optional. A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server guarantees that a request doesn't result in creation of duplicate commitments for at least 60 minutes.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




### #request_id=
    
    
    def request_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server guarantees that a request doesn't result in creation of duplicate commitments for at least 60 minutes.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




**Returns**

  * (::String) — Optional. A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server guarantees that a request doesn't result in creation of duplicate commitments for at least 60 minutes.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
