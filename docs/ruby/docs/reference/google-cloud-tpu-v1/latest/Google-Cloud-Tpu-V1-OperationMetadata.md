---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tpu-v1/latest/Google-Cloud-Tpu-V1-OperationMetadata/
title: Cloud TPU V1 API - Class Google::Cloud::Tpu::V1::OperationMetadata (v1.7.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:15:03.110568+00:00
---

# Cloud TPU V1 API - Class Google::Cloud::Tpu::V1::OperationMetadata (v1.7.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tpu-v1/latest/Google-Cloud-Tpu-V1-OperationMetadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud TPU V1 API - Class Google::Cloud::Tpu::V1::OperationMetadata (v1.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.7.1 (latest)  1.7.0  1.6.0  1.5.1  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.7.0  0.6.2  0.5.0  0.4.1  0.3.0  0.2.0  0.1.4 

Reference documentation and code samples for the Cloud TPU V1 API class Google::Cloud::Tpu::V1::OperationMetadata.

Metadata describing an [Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tpu-v1/latest/Google-Longrunning-Operation "Google::Longrunning::Operation \(class\)")

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #api_version
    
    
    def api_version() -> ::String

**Returns**

  * (::String) — API version. 



### #api_version=
    
    
    def api_version=(value) -> ::String

**Parameter**

  * **value** (::String) — API version. 



**Returns**

  * (::String) — API version. 



### #cancel_requested
    
    
    def cancel_requested() -> ::Boolean

**Returns**

  * (::Boolean) — Specifies if cancellation was requested for the operation. 



### #cancel_requested=
    
    
    def cancel_requested=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Specifies if cancellation was requested for the operation. 



**Returns**

  * (::Boolean) — Specifies if cancellation was requested for the operation. 



### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tpu-v1/latest/Google-Protobuf-Timestamp)) — The time the operation was created. 



### #create_time=
    
    
    def create_time=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tpu-v1/latest/Google-Protobuf-Timestamp)) — The time the operation was created. 



**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tpu-v1/latest/Google-Protobuf-Timestamp)) — The time the operation was created. 



### #end_time
    
    
    def end_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tpu-v1/latest/Google-Protobuf-Timestamp)) — The time the operation finished running. 



### #end_time=
    
    
    def end_time=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tpu-v1/latest/Google-Protobuf-Timestamp)) — The time the operation finished running. 



**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tpu-v1/latest/Google-Protobuf-Timestamp)) — The time the operation finished running. 



### #status_detail
    
    
    def status_detail() -> ::String

**Returns**

  * (::String) — Human-readable status of the operation, if any. 



### #status_detail=
    
    
    def status_detail=(value) -> ::String

**Parameter**

  * **value** (::String) — Human-readable status of the operation, if any. 



**Returns**

  * (::String) — Human-readable status of the operation, if any. 



### #target
    
    
    def target() -> ::String

**Returns**

  * (::String) — Target of the operation - for example projects/project-1/connectivityTests/test-1 



### #target=
    
    
    def target=(value) -> ::String

**Parameter**

  * **value** (::String) — Target of the operation - for example projects/project-1/connectivityTests/test-1 



**Returns**

  * (::String) — Target of the operation - for example projects/project-1/connectivityTests/test-1 



### #verb
    
    
    def verb() -> ::String

**Returns**

  * (::String) — Name of the verb executed by the operation. 



### #verb=
    
    
    def verb=(value) -> ::String

**Parameter**

  * **value** (::String) — Name of the verb executed by the operation. 



**Returns**

  * (::String) — Name of the verb executed by the operation. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
