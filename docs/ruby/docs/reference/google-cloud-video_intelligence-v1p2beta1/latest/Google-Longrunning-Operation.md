---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video_intelligence-v1p2beta1/latest/Google-Longrunning-Operation/
title: Cloud Video Intelligence V1p2beta1 API - Class Google::Longrunning::Operation (v0.18.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:09:53.864848+00:00
---

# Cloud Video Intelligence V1p2beta1 API - Class Google::Longrunning::Operation (v0.18.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video_intelligence-v1p2beta1/latest/Google-Longrunning-Operation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Video Intelligence V1p2beta1 API - Class Google::Longrunning::Operation (v0.18.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.18.1 (latest)  0.18.0  0.17.0  0.16.1  0.15.0  0.14.0  0.13.1  0.12.0  0.11.2  0.10.2  0.9.0  0.8.1  0.7.0  0.6.0  0.5.0  0.4.5 

Reference documentation and code samples for the Cloud Video Intelligence V1p2beta1 API class Google::Longrunning::Operation.

This resource represents a long-running operation that is the result of a network API call.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #done
    
    
    def done() -> ::Boolean

**Returns**

  * (::Boolean) — If the value is `false`, it means the operation is still in progress. If `true`, the operation is completed, and either `error` or `response` is available. 



### #done=
    
    
    def done=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — If the value is `false`, it means the operation is still in progress. If `true`, the operation is completed, and either `error` or `response` is available. 



**Returns**

  * (::Boolean) — If the value is `false`, it means the operation is still in progress. If `true`, the operation is completed, and either `error` or `response` is available. 



### #error
    
    
    def error() -> ::Google::Rpc::Status

**Returns**

  * ([::Google::Rpc::Status](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video_intelligence-v1p2beta1/latest/Google-Rpc-Status)) — The error result of the operation in case of failure or cancellation.

Note: The following fields are mutually exclusive: `error`, `response`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #error=
    
    
    def error=(value) -> ::Google::Rpc::Status

**Parameter**

  * **value** ([::Google::Rpc::Status](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video_intelligence-v1p2beta1/latest/Google-Rpc-Status)) — The error result of the operation in case of failure or cancellation.

Note: The following fields are mutually exclusive: `error`, `response`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Rpc::Status](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video_intelligence-v1p2beta1/latest/Google-Rpc-Status)) — The error result of the operation in case of failure or cancellation.

Note: The following fields are mutually exclusive: `error`, `response`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #metadata
    
    
    def metadata() -> ::Google::Protobuf::Any

**Returns**

  * ([::Google::Protobuf::Any](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video_intelligence-v1p2beta1/latest/Google-Protobuf-Any)) — Service-specific metadata associated with the operation. It typically contains progress information and common metadata such as create time. Some services might not provide such metadata. Any method that returns a long-running operation should document the metadata type, if any. 



### #metadata=
    
    
    def metadata=(value) -> ::Google::Protobuf::Any

**Parameter**

  * **value** ([::Google::Protobuf::Any](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video_intelligence-v1p2beta1/latest/Google-Protobuf-Any)) — Service-specific metadata associated with the operation. It typically contains progress information and common metadata such as create time. Some services might not provide such metadata. Any method that returns a long-running operation should document the metadata type, if any. 



**Returns**

  * ([::Google::Protobuf::Any](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video_intelligence-v1p2beta1/latest/Google-Protobuf-Any)) — Service-specific metadata associated with the operation. It typically contains progress information and common metadata such as create time. Some services might not provide such metadata. Any method that returns a long-running operation should document the metadata type, if any. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — The server-assigned name, which is only unique within the same service that originally returns it. If you use the default HTTP mapping, the `name` should be a resource name ending with `operations/{unique_id}`. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — The server-assigned name, which is only unique within the same service that originally returns it. If you use the default HTTP mapping, the `name` should be a resource name ending with `operations/{unique_id}`. 



**Returns**

  * (::String) — The server-assigned name, which is only unique within the same service that originally returns it. If you use the default HTTP mapping, the `name` should be a resource name ending with `operations/{unique_id}`. 



### #response
    
    
    def response() -> ::Google::Protobuf::Any

**Returns**

  * ([::Google::Protobuf::Any](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video_intelligence-v1p2beta1/latest/Google-Protobuf-Any)) — The normal, successful response of the operation. If the original method returns no data on success, such as `Delete`, the response is `google.protobuf.Empty`. If the original method is standard `Get`/`Create`/`Update`, the response should be the resource. For other methods, the response should have the type `XxxResponse`, where `Xxx` is the original method name. For example, if the original method name is `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.

Note: The following fields are mutually exclusive: `response`, `error`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #response=
    
    
    def response=(value) -> ::Google::Protobuf::Any

**Parameter**

  * **value** ([::Google::Protobuf::Any](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video_intelligence-v1p2beta1/latest/Google-Protobuf-Any)) — The normal, successful response of the operation. If the original method returns no data on success, such as `Delete`, the response is `google.protobuf.Empty`. If the original method is standard `Get`/`Create`/`Update`, the response should be the resource. For other methods, the response should have the type `XxxResponse`, where `Xxx` is the original method name. For example, if the original method name is `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.

Note: The following fields are mutually exclusive: `response`, `error`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Protobuf::Any](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video_intelligence-v1p2beta1/latest/Google-Protobuf-Any)) — The normal, successful response of the operation. If the original method returns no data on success, such as `Delete`, the response is `google.protobuf.Empty`. If the original method is standard `Get`/`Create`/`Update`, the response should be the resource. For other methods, the response should have the type `XxxResponse`, where `Xxx` is the original method name. For example, if the original method name is `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.

Note: The following fields are mutually exclusive: `response`, `error`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
