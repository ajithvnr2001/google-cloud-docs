---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-CreateSecondaryInstanceRequest/
title: AlloyDB V1ALPHA API - Class Google::Cloud::AlloyDB::V1alpha::CreateSecondaryInstanceRequest (v0.24.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:41:31.888471+00:00
---

# AlloyDB V1ALPHA API - Class Google::Cloud::AlloyDB::V1alpha::CreateSecondaryInstanceRequest (v0.24.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-CreateSecondaryInstanceRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  AlloyDB V1ALPHA API - Class Google::Cloud::AlloyDB::V1alpha::CreateSecondaryInstanceRequest (v0.24.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.24.0 (latest)  0.23.1  0.22.1  0.21.0  0.20.0  0.19.0  0.18.0  0.17.1  0.16.0  0.15.0  0.14.1  0.13.0  0.12.0  0.11.1  0.10.0  0.9.0  0.8.0  0.7.2  0.6.0  0.5.2  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the AlloyDB V1ALPHA API class Google::Cloud::AlloyDB::V1alpha::CreateSecondaryInstanceRequest.

Message for creating a Secondary Instance

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #instance
    
    
    def instance() -> ::Google::Cloud::AlloyDB::V1alpha::Instance

**Returns**

  * ([::Google::Cloud::AlloyDB::V1alpha::Instance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-Instance)) — Required. The resource being created 



### #instance=
    
    
    def instance=(value) -> ::Google::Cloud::AlloyDB::V1alpha::Instance

**Parameter**

  * **value** ([::Google::Cloud::AlloyDB::V1alpha::Instance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-Instance)) — Required. The resource being created 



**Returns**

  * ([::Google::Cloud::AlloyDB::V1alpha::Instance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1alpha/latest/Google-Cloud-AlloyDB-V1alpha-Instance)) — Required. The resource being created 



### #instance_id
    
    
    def instance_id() -> ::String

**Returns**

  * (::String) — Required. ID of the requesting object. 



### #instance_id=
    
    
    def instance_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. ID of the requesting object. 



**Returns**

  * (::String) — Required. ID of the requesting object. 



### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. The name of the parent resource. For the required format, see the comment on the Instance.name field. 



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The name of the parent resource. For the required format, see the comment on the Instance.name field. 



**Returns**

  * (::String) — Required. The name of the parent resource. For the required format, see the comment on the Instance.name field. 



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
