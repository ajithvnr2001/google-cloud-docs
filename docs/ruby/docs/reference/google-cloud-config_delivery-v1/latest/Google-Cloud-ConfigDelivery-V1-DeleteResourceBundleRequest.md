---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_delivery-v1/latest/Google-Cloud-ConfigDelivery-V1-DeleteResourceBundleRequest/
title: Config Delivery V1 API - Class Google::Cloud::ConfigDelivery::V1::DeleteResourceBundleRequest (v1.0.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:06:03.771560+00:00
---

# Config Delivery V1 API - Class Google::Cloud::ConfigDelivery::V1::DeleteResourceBundleRequest (v1.0.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_delivery-v1/latest/Google-Cloud-ConfigDelivery-V1-DeleteResourceBundleRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Config Delivery V1 API - Class Google::Cloud::ConfigDelivery::V1::DeleteResourceBundleRequest (v1.0.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.1 (latest)  1.0.0  0.6.0  0.5.0  0.4.0  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Config Delivery V1 API class Google::Cloud::ConfigDelivery::V1::DeleteResourceBundleRequest.

Message for deleting a ResourceBundle

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

  * (::Boolean) — Optional. If set to true, any releases of this resource bundle will also be deleted. (Otherwise, the request will only work if the resource bundle has no releases.) 



### #force=
    
    
    def force=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. If set to true, any releases of this resource bundle will also be deleted. (Otherwise, the request will only work if the resource bundle has no releases.) 



**Returns**

  * (::Boolean) — Optional. If set to true, any releases of this resource bundle will also be deleted. (Otherwise, the request will only work if the resource bundle has no releases.) 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Required. Name of the resource 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Name of the resource 



**Returns**

  * (::String) — Required. Name of the resource 



### #request_id
    
    
    def request_id() -> ::String

**Returns**

  * (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




### #request_id=
    
    
    def request_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




**Returns**

  * (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
