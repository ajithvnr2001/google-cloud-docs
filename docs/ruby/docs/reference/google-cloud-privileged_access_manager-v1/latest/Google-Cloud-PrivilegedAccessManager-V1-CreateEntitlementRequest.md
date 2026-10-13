---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-privileged_access_manager-v1/latest/Google-Cloud-PrivilegedAccessManager-V1-CreateEntitlementRequest/
title: Privileged Access Manager V1 API - Class Google::Cloud::PrivilegedAccessManager::V1::CreateEntitlementRequest (v1.7.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:47:08.810764+00:00
---

# Privileged Access Manager V1 API - Class Google::Cloud::PrivilegedAccessManager::V1::CreateEntitlementRequest (v1.7.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-privileged_access_manager-v1/latest/Google-Cloud-PrivilegedAccessManager-V1-CreateEntitlementRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Privileged Access Manager V1 API - Class Google::Cloud::PrivilegedAccessManager::V1::CreateEntitlementRequest (v1.7.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.7.2 (latest)  1.7.0  1.6.1  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.3.0  0.2.0  0.1.2 

Reference documentation and code samples for the Privileged Access Manager V1 API class Google::Cloud::PrivilegedAccessManager::V1::CreateEntitlementRequest.

Message for creating an entitlement.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #entitlement
    
    
    def entitlement() -> ::Google::Cloud::PrivilegedAccessManager::V1::Entitlement

**Returns**

  * ([::Google::Cloud::PrivilegedAccessManager::V1::Entitlement](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-privileged_access_manager-v1/latest/Google-Cloud-PrivilegedAccessManager-V1-Entitlement)) — Required. The resource being created 



### #entitlement=
    
    
    def entitlement=(value) -> ::Google::Cloud::PrivilegedAccessManager::V1::Entitlement

**Parameter**

  * **value** ([::Google::Cloud::PrivilegedAccessManager::V1::Entitlement](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-privileged_access_manager-v1/latest/Google-Cloud-PrivilegedAccessManager-V1-Entitlement)) — Required. The resource being created 



**Returns**

  * ([::Google::Cloud::PrivilegedAccessManager::V1::Entitlement](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-privileged_access_manager-v1/latest/Google-Cloud-PrivilegedAccessManager-V1-Entitlement)) — Required. The resource being created 



### #entitlement_id
    
    
    def entitlement_id() -> ::String

**Returns**

  * (::String) — Required. The ID to use for this entitlement. This becomes the last part of the resource name.

This value should be 4-63 characters in length, and valid characters are "[a-z]", "[0-9]", and "-". The first character should be from [a-z].

This value should be unique among all other entitlements under the specified `parent`. 




### #entitlement_id=
    
    
    def entitlement_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The ID to use for this entitlement. This becomes the last part of the resource name.

This value should be 4-63 characters in length, and valid characters are "[a-z]", "[0-9]", and "-". The first character should be from [a-z].

This value should be unique among all other entitlements under the specified `parent`. 




**Returns**

  * (::String) — Required. The ID to use for this entitlement. This becomes the last part of the resource name.

This value should be 4-63 characters in length, and valid characters are "[a-z]", "[0-9]", and "-". The first character should be from [a-z].

This value should be unique among all other entitlements under the specified `parent`. 




### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — 

Required. Name of the parent resource for the entitlement. Possible formats:

    * `organizations/{organization-number}/locations/{region}`
    * `folders/{folder-number}/locations/{region}`
    * `projects/{project-id|project-number}/locations/{region}`



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — 

Required. Name of the parent resource for the entitlement. Possible formats:

    * `organizations/{organization-number}/locations/{region}`
    * `folders/{folder-number}/locations/{region}`
    * `projects/{project-id|project-number}/locations/{region}`



**Returns**

  * (::String) — 

Required. Name of the parent resource for the entitlement. Possible formats:

    * `organizations/{organization-number}/locations/{region}`
    * `folders/{folder-number}/locations/{region}`
    * `projects/{project-id|project-number}/locations/{region}`



### #request_id
    
    
    def request_id() -> ::String

**Returns**

  * (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server knows to ignore the request if it has already been completed. The server guarantees this for at least 60 minutes after the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, ignores the second request and returns the previous operation's response. This prevents clients from accidentally creating duplicate entitlements.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




### #request_id=
    
    
    def request_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server knows to ignore the request if it has already been completed. The server guarantees this for at least 60 minutes after the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, ignores the second request and returns the previous operation's response. This prevents clients from accidentally creating duplicate entitlements.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




**Returns**

  * (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server knows to ignore the request if it has already been completed. The server guarantees this for at least 60 minutes after the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, ignores the second request and returns the previous operation's response. This prevents clients from accidentally creating duplicate entitlements.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
