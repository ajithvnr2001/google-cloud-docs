---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Cloud-AlloyDB-V1beta-UpdateInstanceRequest/
title: AlloyDB V1BETA API - Class Google::Cloud::AlloyDB::V1beta::UpdateInstanceRequest (v0.25.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:51:05.062774+00:00
---

# AlloyDB V1BETA API - Class Google::Cloud::AlloyDB::V1beta::UpdateInstanceRequest (v0.25.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Cloud-AlloyDB-V1beta-UpdateInstanceRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  AlloyDB V1BETA API - Class Google::Cloud::AlloyDB::V1beta::UpdateInstanceRequest (v0.25.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.25.0 (latest)  0.24.1  0.23.1  0.22.0  0.21.0  0.20.1  0.19.0  0.18.0  0.17.1  0.16.0  0.15.0  0.14.1  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.1  0.7.0  0.6.2  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the AlloyDB V1BETA API class Google::Cloud::AlloyDB::V1beta::UpdateInstanceRequest.

Message for updating a Instance

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #allow_missing
    
    
    def allow_missing() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. If set to true, update succeeds even if instance is not found. In that case, a new instance is created and `update_mask` is ignored. 



### #allow_missing=
    
    
    def allow_missing=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. If set to true, update succeeds even if instance is not found. In that case, a new instance is created and `update_mask` is ignored. 



**Returns**

  * (::Boolean) — Optional. If set to true, update succeeds even if instance is not found. In that case, a new instance is created and `update_mask` is ignored. 



### #instance
    
    
    def instance() -> ::Google::Cloud::AlloyDB::V1beta::Instance

**Returns**

  * ([::Google::Cloud::AlloyDB::V1beta::Instance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Cloud-AlloyDB-V1beta-Instance)) — Required. The resource being updated 



### #instance=
    
    
    def instance=(value) -> ::Google::Cloud::AlloyDB::V1beta::Instance

**Parameter**

  * **value** ([::Google::Cloud::AlloyDB::V1beta::Instance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Cloud-AlloyDB-V1beta-Instance)) — Required. The resource being updated 



**Returns**

  * ([::Google::Cloud::AlloyDB::V1beta::Instance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Cloud-AlloyDB-V1beta-Instance)) — Required. The resource being updated 



### #request_id
    
    
    def request_id() -> ::String

**Returns**

  * (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server ignores the request if it has already been completed. The server guarantees that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if the original operation with the same request ID was received, and if so, ignores the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




### #request_id=
    
    
    def request_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server ignores the request if it has already been completed. The server guarantees that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if the original operation with the same request ID was received, and if so, ignores the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




**Returns**

  * (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server ignores the request if it has already been completed. The server guarantees that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if the original operation with the same request ID was received, and if so, ignores the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




### #update_mask
    
    
    def update_mask() -> ::Google::Protobuf::FieldMask

**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Protobuf-FieldMask)) — Optional. Field mask is used to specify the fields to be overwritten in the Instance resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten. 



### #update_mask=
    
    
    def update_mask=(value) -> ::Google::Protobuf::FieldMask

**Parameter**

  * **value** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Protobuf-FieldMask)) — Optional. Field mask is used to specify the fields to be overwritten in the Instance resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten. 



**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Protobuf-FieldMask)) — Optional. Field mask is used to specify the fields to be overwritten in the Instance resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten. 



### #validate_only
    
    
    def validate_only() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. If set, performs request validation, for example, permission checks and any other type of validation, but does not actually execute the create request. 



### #validate_only=
    
    
    def validate_only=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. If set, performs request validation, for example, permission checks and any other type of validation, but does not actually execute the create request. 



**Returns**

  * (::Boolean) — Optional. If set, performs request validation, for example, permission checks and any other type of validation, but does not actually execute the create request. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
