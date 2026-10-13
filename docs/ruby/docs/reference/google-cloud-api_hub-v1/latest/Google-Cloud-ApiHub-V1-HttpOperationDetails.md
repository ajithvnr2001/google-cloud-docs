---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-HttpOperationDetails/
title: API hub V1 API - Class Google::Cloud::ApiHub::V1::HttpOperationDetails (v1.0.3) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:18:10.518123+00:00
---

# API hub V1 API - Class Google::Cloud::ApiHub::V1::HttpOperationDetails (v1.0.3)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-HttpOperationDetails/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  API hub V1 API - Class Google::Cloud::ApiHub::V1::HttpOperationDetails (v1.0.3) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.3 (latest)  1.0.2  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.1  0.3.0  0.2.0  0.1.1 

Reference documentation and code samples for the API hub V1 API class Google::Cloud::ApiHub::V1::HttpOperationDetails.

An HTTP-based API Operation, sometimes called a "REST" Operation.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #http_operation
    
    
    def http_operation() -> ::Google::Cloud::ApiHub::V1::HttpOperation

**Returns**

  * ([::Google::Cloud::ApiHub::V1::HttpOperation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-HttpOperation)) — Required. An HTTP Operation. 



### #http_operation=
    
    
    def http_operation=(value) -> ::Google::Cloud::ApiHub::V1::HttpOperation

**Parameter**

  * **value** ([::Google::Cloud::ApiHub::V1::HttpOperation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-HttpOperation)) — Required. An HTTP Operation. 



**Returns**

  * ([::Google::Cloud::ApiHub::V1::HttpOperation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-HttpOperation)) — Required. An HTTP Operation. 



### #path_params
    
    
    def path_params() -> ::Array<::Google::Cloud::ApiHub::V1::HttpOperationDetails::PathParam>

**Returns**

  * (::Array<[::Google::Cloud::ApiHub::V1::HttpOperationDetails::PathParam](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-HttpOperationDetails-PathParam)>) — Optional. Path params of HttpOperation 



### #path_params=
    
    
    def path_params=(value) -> ::Array<::Google::Cloud::ApiHub::V1::HttpOperationDetails::PathParam>

**Parameter**

  * **value** (::Array<[::Google::Cloud::ApiHub::V1::HttpOperationDetails::PathParam](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-HttpOperationDetails-PathParam)>) — Optional. Path params of HttpOperation 



**Returns**

  * (::Array<[::Google::Cloud::ApiHub::V1::HttpOperationDetails::PathParam](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-HttpOperationDetails-PathParam)>) — Optional. Path params of HttpOperation 



### #query_params
    
    
    def query_params() -> ::Google::Protobuf::Map{::String => ::Google::Cloud::ApiHub::V1::HttpOperationDetails::QueryParam}

**Returns**

  * (::Google::Protobuf::Map{::String => ::Google::Cloud::ApiHub::V1::HttpOperationDetails::QueryParam}) — Optional. Query params of HttpOperation 



### #query_params=
    
    
    def query_params=(value) -> ::Google::Protobuf::Map{::String => ::Google::Cloud::ApiHub::V1::HttpOperationDetails::QueryParam}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::Google::Cloud::ApiHub::V1::HttpOperationDetails::QueryParam}) — Optional. Query params of HttpOperation 



**Returns**

  * (::Google::Protobuf::Map{::String => ::Google::Cloud::ApiHub::V1::HttpOperationDetails::QueryParam}) — Optional. Query params of HttpOperation 



### #request
    
    
    def request() -> ::Google::Cloud::ApiHub::V1::HttpOperationDetails::HttpRequest

**Returns**

  * ([::Google::Cloud::ApiHub::V1::HttpOperationDetails::HttpRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-HttpOperationDetails-HttpRequest)) — Optional. Request metadata. 



### #request=
    
    
    def request=(value) -> ::Google::Cloud::ApiHub::V1::HttpOperationDetails::HttpRequest

**Parameter**

  * **value** ([::Google::Cloud::ApiHub::V1::HttpOperationDetails::HttpRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-HttpOperationDetails-HttpRequest)) — Optional. Request metadata. 



**Returns**

  * ([::Google::Cloud::ApiHub::V1::HttpOperationDetails::HttpRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-HttpOperationDetails-HttpRequest)) — Optional. Request metadata. 



### #response
    
    
    def response() -> ::Google::Cloud::ApiHub::V1::HttpOperationDetails::HttpResponse

**Returns**

  * ([::Google::Cloud::ApiHub::V1::HttpOperationDetails::HttpResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-HttpOperationDetails-HttpResponse)) — Optional. Response metadata. 



### #response=
    
    
    def response=(value) -> ::Google::Cloud::ApiHub::V1::HttpOperationDetails::HttpResponse

**Parameter**

  * **value** ([::Google::Cloud::ApiHub::V1::HttpOperationDetails::HttpResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-HttpOperationDetails-HttpResponse)) — Optional. Response metadata. 



**Returns**

  * ([::Google::Cloud::ApiHub::V1::HttpOperationDetails::HttpResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-HttpOperationDetails-HttpResponse)) — Optional. Response metadata. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
