---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vmware_engine-v1/latest/Google-Cloud-VmwareEngine-V1-CreateExternalAddressRequest/
title: Google Cloud VMware Engine V1 API - Class Google::Cloud::VmwareEngine::V1::CreateExternalAddressRequest (v1.5.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:35:49.551417+00:00
---

# Google Cloud VMware Engine V1 API - Class Google::Cloud::VmwareEngine::V1::CreateExternalAddressRequest (v1.5.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vmware_engine-v1/latest/Google-Cloud-VmwareEngine-V1-CreateExternalAddressRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud VMware Engine V1 API - Class Google::Cloud::VmwareEngine::V1::CreateExternalAddressRequest (v1.5.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.5.2 (latest)  1.5.1  1.4.1  1.3.1  1.2.0  1.1.0  1.0.1  0.11.0  0.10.0  0.9.2  0.8.0  0.7.1  0.6.1  0.5.0  0.4.0  0.3.1  0.2.0  0.1.1 

Reference documentation and code samples for the Google Cloud VMware Engine V1 API class Google::Cloud::VmwareEngine::V1::CreateExternalAddressRequest.

Request message for [VmwareEngine.CreateExternalAddress](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vmware_engine-v1/latest/Google-Cloud-VmwareEngine-V1-VmwareEngine-Client#Google__Cloud__VmwareEngine__V1__VmwareEngine__Client_create_external_address_instance_ "Google::Cloud::VmwareEngine::V1::VmwareEngine::Client#create_external_address \(method\)")

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #external_address
    
    
    def external_address() -> ::Google::Cloud::VmwareEngine::V1::ExternalAddress

**Returns**

  * ([::Google::Cloud::VmwareEngine::V1::ExternalAddress](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vmware_engine-v1/latest/Google-Cloud-VmwareEngine-V1-ExternalAddress)) — Required. The initial description of a new external IP address. 



### #external_address=
    
    
    def external_address=(value) -> ::Google::Cloud::VmwareEngine::V1::ExternalAddress

**Parameter**

  * **value** ([::Google::Cloud::VmwareEngine::V1::ExternalAddress](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vmware_engine-v1/latest/Google-Cloud-VmwareEngine-V1-ExternalAddress)) — Required. The initial description of a new external IP address. 



**Returns**

  * ([::Google::Cloud::VmwareEngine::V1::ExternalAddress](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vmware_engine-v1/latest/Google-Cloud-VmwareEngine-V1-ExternalAddress)) — Required. The initial description of a new external IP address. 



### #external_address_id
    
    
    def external_address_id() -> ::String

**Returns**

  * (::String) — 

Required. The user-provided identifier of the `ExternalAddress` to be created. This identifier must be unique among `ExternalAddress` resources within the parent and becomes the final token in the name URI. The identifier must meet the following requirements:

    * Only contains 1-63 alphanumeric characters and hyphens
    * Begins with an alphabetical character
    * Ends with a non-hyphen character
    * Not formatted as a UUID
    * Complies with [RFC 1034](https://datatracker.ietf.org/doc/html/rfc1034) (section 3.5)



### #external_address_id=
    
    
    def external_address_id=(value) -> ::String

**Parameter**

  * **value** (::String) — 

Required. The user-provided identifier of the `ExternalAddress` to be created. This identifier must be unique among `ExternalAddress` resources within the parent and becomes the final token in the name URI. The identifier must meet the following requirements:

    * Only contains 1-63 alphanumeric characters and hyphens
    * Begins with an alphabetical character
    * Ends with a non-hyphen character
    * Not formatted as a UUID
    * Complies with [RFC 1034](https://datatracker.ietf.org/doc/html/rfc1034) (section 3.5)



**Returns**

  * (::String) — 

Required. The user-provided identifier of the `ExternalAddress` to be created. This identifier must be unique among `ExternalAddress` resources within the parent and becomes the final token in the name URI. The identifier must meet the following requirements:

    * Only contains 1-63 alphanumeric characters and hyphens
    * Begins with an alphabetical character
    * Ends with a non-hyphen character
    * Not formatted as a UUID
    * Complies with [RFC 1034](https://datatracker.ietf.org/doc/html/rfc1034) (section 3.5)



### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. The resource name of the private cloud to create a new external IP address in. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud`



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The resource name of the private cloud to create a new external IP address in. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud`



**Returns**

  * (::String) — Required. The resource name of the private cloud to create a new external IP address in. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud`



### #request_id
    
    
    def request_id() -> ::String

**Returns**

  * (::String) — Optional. A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server guarantees that a request doesn't result in creation of duplicate commitments for at least 60 minutes.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if the original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




### #request_id=
    
    
    def request_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server guarantees that a request doesn't result in creation of duplicate commitments for at least 60 minutes.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if the original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




**Returns**

  * (::String) — Optional. A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server guarantees that a request doesn't result in creation of duplicate commitments for at least 60 minutes.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if the original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
