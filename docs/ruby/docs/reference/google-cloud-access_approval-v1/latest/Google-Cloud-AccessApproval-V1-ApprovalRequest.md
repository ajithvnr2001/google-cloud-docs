---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-access_approval-v1/latest/Google-Cloud-AccessApproval-V1-ApprovalRequest/
title: Access Approval V1 API - Class Google::Cloud::AccessApproval::V1::ApprovalRequest (v1.7.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:51:08.817131+00:00
---

# Access Approval V1 API - Class Google::Cloud::AccessApproval::V1::ApprovalRequest (v1.7.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-access_approval-v1/latest/Google-Cloud-AccessApproval-V1-ApprovalRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Access Approval V1 API - Class Google::Cloud::AccessApproval::V1::ApprovalRequest (v1.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.7.1 (latest)  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.1  1.1.0  1.0.2  0.12.0  0.11.2  0.10.0  0.9.0  0.8.0  0.7.1  0.6.0  0.5.0  0.4.5 

Reference documentation and code samples for the Access Approval V1 API class Google::Cloud::AccessApproval::V1::ApprovalRequest.

A request for the customer to approve access to a resource.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #approve
    
    
    def approve() -> ::Google::Cloud::AccessApproval::V1::ApproveDecision

**Returns**

  * ([::Google::Cloud::AccessApproval::V1::ApproveDecision](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-access_approval-v1/latest/Google-Cloud-AccessApproval-V1-ApproveDecision)) — Access was approved.

Note: The following fields are mutually exclusive: `approve`, `dismiss`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #approve=
    
    
    def approve=(value) -> ::Google::Cloud::AccessApproval::V1::ApproveDecision

**Parameter**

  * **value** ([::Google::Cloud::AccessApproval::V1::ApproveDecision](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-access_approval-v1/latest/Google-Cloud-AccessApproval-V1-ApproveDecision)) — Access was approved.

Note: The following fields are mutually exclusive: `approve`, `dismiss`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::AccessApproval::V1::ApproveDecision](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-access_approval-v1/latest/Google-Cloud-AccessApproval-V1-ApproveDecision)) — Access was approved.

Note: The following fields are mutually exclusive: `approve`, `dismiss`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #dismiss
    
    
    def dismiss() -> ::Google::Cloud::AccessApproval::V1::DismissDecision

**Returns**

  * ([::Google::Cloud::AccessApproval::V1::DismissDecision](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-access_approval-v1/latest/Google-Cloud-AccessApproval-V1-DismissDecision)) — The request was dismissed.

Note: The following fields are mutually exclusive: `dismiss`, `approve`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #dismiss=
    
    
    def dismiss=(value) -> ::Google::Cloud::AccessApproval::V1::DismissDecision

**Parameter**

  * **value** ([::Google::Cloud::AccessApproval::V1::DismissDecision](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-access_approval-v1/latest/Google-Cloud-AccessApproval-V1-DismissDecision)) — The request was dismissed.

Note: The following fields are mutually exclusive: `dismiss`, `approve`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::AccessApproval::V1::DismissDecision](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-access_approval-v1/latest/Google-Cloud-AccessApproval-V1-DismissDecision)) — The request was dismissed.

Note: The following fields are mutually exclusive: `dismiss`, `approve`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — The resource name of the request. Format is "{projects|folders|organizations}/{id}/approvalRequests/{approval_request}". 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — The resource name of the request. Format is "{projects|folders|organizations}/{id}/approvalRequests/{approval_request}". 



**Returns**

  * (::String) — The resource name of the request. Format is "{projects|folders|organizations}/{id}/approvalRequests/{approval_request}". 



### #request_time
    
    
    def request_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-access_approval-v1/latest/Google-Protobuf-Timestamp)) — The time at which approval was requested. 



### #request_time=
    
    
    def request_time=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-access_approval-v1/latest/Google-Protobuf-Timestamp)) — The time at which approval was requested. 



**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-access_approval-v1/latest/Google-Protobuf-Timestamp)) — The time at which approval was requested. 



### #requested_expiration
    
    
    def requested_expiration() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-access_approval-v1/latest/Google-Protobuf-Timestamp)) — The requested expiration for the approval. If the request is approved, access will be granted from the time of approval until the expiration time. 



### #requested_expiration=
    
    
    def requested_expiration=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-access_approval-v1/latest/Google-Protobuf-Timestamp)) — The requested expiration for the approval. If the request is approved, access will be granted from the time of approval until the expiration time. 



**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-access_approval-v1/latest/Google-Protobuf-Timestamp)) — The requested expiration for the approval. If the request is approved, access will be granted from the time of approval until the expiration time. 



### #requested_locations
    
    
    def requested_locations() -> ::Google::Cloud::AccessApproval::V1::AccessLocations

**Returns**

  * ([::Google::Cloud::AccessApproval::V1::AccessLocations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-access_approval-v1/latest/Google-Cloud-AccessApproval-V1-AccessLocations)) — The locations for which approval is being requested. 



### #requested_locations=
    
    
    def requested_locations=(value) -> ::Google::Cloud::AccessApproval::V1::AccessLocations

**Parameter**

  * **value** ([::Google::Cloud::AccessApproval::V1::AccessLocations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-access_approval-v1/latest/Google-Cloud-AccessApproval-V1-AccessLocations)) — The locations for which approval is being requested. 



**Returns**

  * ([::Google::Cloud::AccessApproval::V1::AccessLocations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-access_approval-v1/latest/Google-Cloud-AccessApproval-V1-AccessLocations)) — The locations for which approval is being requested. 



### #requested_reason
    
    
    def requested_reason() -> ::Google::Cloud::AccessApproval::V1::AccessReason

**Returns**

  * ([::Google::Cloud::AccessApproval::V1::AccessReason](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-access_approval-v1/latest/Google-Cloud-AccessApproval-V1-AccessReason)) — The justification for which approval is being requested. 



### #requested_reason=
    
    
    def requested_reason=(value) -> ::Google::Cloud::AccessApproval::V1::AccessReason

**Parameter**

  * **value** ([::Google::Cloud::AccessApproval::V1::AccessReason](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-access_approval-v1/latest/Google-Cloud-AccessApproval-V1-AccessReason)) — The justification for which approval is being requested. 



**Returns**

  * ([::Google::Cloud::AccessApproval::V1::AccessReason](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-access_approval-v1/latest/Google-Cloud-AccessApproval-V1-AccessReason)) — The justification for which approval is being requested. 



### #requested_resource_name
    
    
    def requested_resource_name() -> ::String

**Returns**

  * (::String) — The resource for which approval is being requested. The format of the resource name is defined at https://cloud.google.com/apis/design/resource_names. The resource name here may either be a "full" resource name (e.g. "//library.googleapis.com/shelves/shelf1/books/book2") or a "relative" resource name (e.g. "shelves/shelf1/books/book2") as described in the resource name specification. 



### #requested_resource_name=
    
    
    def requested_resource_name=(value) -> ::String

**Parameter**

  * **value** (::String) — The resource for which approval is being requested. The format of the resource name is defined at https://cloud.google.com/apis/design/resource_names. The resource name here may either be a "full" resource name (e.g. "//library.googleapis.com/shelves/shelf1/books/book2") or a "relative" resource name (e.g. "shelves/shelf1/books/book2") as described in the resource name specification. 



**Returns**

  * (::String) — The resource for which approval is being requested. The format of the resource name is defined at https://cloud.google.com/apis/design/resource_names. The resource name here may either be a "full" resource name (e.g. "//library.googleapis.com/shelves/shelf1/books/book2") or a "relative" resource name (e.g. "shelves/shelf1/books/book2") as described in the resource name specification. 



### #requested_resource_properties
    
    
    def requested_resource_properties() -> ::Google::Cloud::AccessApproval::V1::ResourceProperties

**Returns**

  * ([::Google::Cloud::AccessApproval::V1::ResourceProperties](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-access_approval-v1/latest/Google-Cloud-AccessApproval-V1-ResourceProperties)) — Properties related to the resource represented by requested_resource_name. 



### #requested_resource_properties=
    
    
    def requested_resource_properties=(value) -> ::Google::Cloud::AccessApproval::V1::ResourceProperties

**Parameter**

  * **value** ([::Google::Cloud::AccessApproval::V1::ResourceProperties](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-access_approval-v1/latest/Google-Cloud-AccessApproval-V1-ResourceProperties)) — Properties related to the resource represented by requested_resource_name. 



**Returns**

  * ([::Google::Cloud::AccessApproval::V1::ResourceProperties](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-access_approval-v1/latest/Google-Cloud-AccessApproval-V1-ResourceProperties)) — Properties related to the resource represented by requested_resource_name. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
