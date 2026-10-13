---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-CreateStreamRequest/
title: Datastream V1alpha1 API - Class Google::Cloud::Datastream::V1alpha1::CreateStreamRequest (v0.15.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:07:25.962363+00:00
---

# Datastream V1alpha1 API - Class Google::Cloud::Datastream::V1alpha1::CreateStreamRequest (v0.15.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-CreateStreamRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Datastream V1alpha1 API - Class Google::Cloud::Datastream::V1alpha1::CreateStreamRequest (v0.15.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.15.1 (latest)  0.15.0  0.14.0  0.13.1  0.12.0  0.11.1  0.10.1  0.9.0  0.8.0  0.7.1  0.6.2  0.5.0  0.4.0  0.3.0  0.2.0  0.1.2 

Reference documentation and code samples for the Datastream V1alpha1 API class Google::Cloud::Datastream::V1alpha1::CreateStreamRequest.

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

  * (::Boolean) — Optional. Create the stream without validating it. 



### #force=
    
    
    def force=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. Create the stream without validating it. 



**Returns**

  * (::Boolean) — Optional. Create the stream without validating it. 



### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. The parent that owns the collection of streams. 



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The parent that owns the collection of streams. 



**Returns**

  * (::String) — Required. The parent that owns the collection of streams. 



### #request_id
    
    
    def request_id() -> ::String

**Returns**

  * (::String) — Optional. A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




### #request_id=
    
    
    def request_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




**Returns**

  * (::String) — Optional. A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




### #stream
    
    
    def stream() -> ::Google::Cloud::Datastream::V1alpha1::Stream

**Returns**

  * ([::Google::Cloud::Datastream::V1alpha1::Stream](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-Stream)) — Required. The stream resource to create. 



### #stream=
    
    
    def stream=(value) -> ::Google::Cloud::Datastream::V1alpha1::Stream

**Parameter**

  * **value** ([::Google::Cloud::Datastream::V1alpha1::Stream](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-Stream)) — Required. The stream resource to create. 



**Returns**

  * ([::Google::Cloud::Datastream::V1alpha1::Stream](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-Stream)) — Required. The stream resource to create. 



### #stream_id
    
    
    def stream_id() -> ::String

**Returns**

  * (::String) — Required. The stream identifier. 



### #stream_id=
    
    
    def stream_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The stream identifier. 



**Returns**

  * (::String) — Required. The stream identifier. 



### #validate_only
    
    
    def validate_only() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. Only validate the stream, but do not create any resources. The default is false. 



### #validate_only=
    
    
    def validate_only=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. Only validate the stream, but do not create any resources. The default is false. 



**Returns**

  * (::Boolean) — Optional. Only validate the stream, but do not create any resources. The default is false. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
