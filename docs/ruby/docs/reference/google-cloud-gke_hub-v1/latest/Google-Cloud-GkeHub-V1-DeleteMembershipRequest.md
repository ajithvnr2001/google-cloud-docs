---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_hub-v1/latest/Google-Cloud-GkeHub-V1-DeleteMembershipRequest/
title: GKE Hub V1 API - Class Google::Cloud::GkeHub::V1::DeleteMembershipRequest (v2.6.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:11:40.848161+00:00
---

# GKE Hub V1 API - Class Google::Cloud::GkeHub::V1::DeleteMembershipRequest (v2.6.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_hub-v1/latest/Google-Cloud-GkeHub-V1-DeleteMembershipRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  GKE Hub V1 API - Class Google::Cloud::GkeHub::V1::DeleteMembershipRequest (v2.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.6.0 (latest)  2.5.0  2.4.1  2.3.0  2.2.0  2.1.0  2.0.1  1.2.0  1.1.0  1.0.1  0.10.0  0.9.0  0.8.2  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.2 

Reference documentation and code samples for the GKE Hub V1 API class Google::Cloud::GkeHub::V1::DeleteMembershipRequest.

Request message for `GkeHub.DeleteMembership` method.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #force
    
    
    def force() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. If set to true, any subresource from this Membership will also be deleted. Otherwise, the request will only work if the Membership has no subresource. 



### #force=
    
    
    def force=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. If set to true, any subresource from this Membership will also be deleted. Otherwise, the request will only work if the Membership has no subresource. 



**Returns**

  * (::Boolean) — Optional. If set to true, any subresource from this Membership will also be deleted. Otherwise, the request will only work if the Membership has no subresource. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Required. The Membership resource name in the format `projects/*/locations/*/memberships/*`. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The Membership resource name in the format `projects/*/locations/*/memberships/*`. 



**Returns**

  * (::String) — Required. The Membership resource name in the format `projects/*/locations/*/memberships/*`. 



### #request_id
    
    
    def request_id() -> ::String

**Returns**

  * (::String) — Optional. A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




### #request_id=
    
    
    def request_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




**Returns**

  * (::String) — Optional. A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
