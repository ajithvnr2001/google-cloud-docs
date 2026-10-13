---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_gateway-v1/latest/Google-Cloud-ApiGateway-V1-UpdateGatewayRequest/
title: API Gateway V1 API - Class Google::Cloud::ApiGateway::V1::UpdateGatewayRequest (v2.8.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:04:46.616385+00:00
---

# API Gateway V1 API - Class Google::Cloud::ApiGateway::V1::UpdateGatewayRequest (v2.8.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_gateway-v1/latest/Google-Cloud-ApiGateway-V1-UpdateGatewayRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  API Gateway V1 API - Class Google::Cloud::ApiGateway::V1::UpdateGatewayRequest (v2.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.8.0 (latest)  2.7.0  2.6.2  2.5.0  2.4.0  2.3.1  2.2.0  2.1.0  2.0.1  1.2.0  1.1.0  1.0.1  0.7.0  0.6.2  0.5.0  0.4.0  0.3.0  0.2.0  0.1.5 

Reference documentation and code samples for the API Gateway V1 API class Google::Cloud::ApiGateway::V1::UpdateGatewayRequest.

Request message for ApiGatewayService.UpdateGateway

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #gateway
    
    
    def gateway() -> ::Google::Cloud::ApiGateway::V1::Gateway

**Returns**

  * ([::Google::Cloud::ApiGateway::V1::Gateway](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_gateway-v1/latest/Google-Cloud-ApiGateway-V1-Gateway)) — Required. Gateway resource. 



### #gateway=
    
    
    def gateway=(value) -> ::Google::Cloud::ApiGateway::V1::Gateway

**Parameter**

  * **value** ([::Google::Cloud::ApiGateway::V1::Gateway](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_gateway-v1/latest/Google-Cloud-ApiGateway-V1-Gateway)) — Required. Gateway resource. 



**Returns**

  * ([::Google::Cloud::ApiGateway::V1::Gateway](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_gateway-v1/latest/Google-Cloud-ApiGateway-V1-Gateway)) — Required. Gateway resource. 



### #update_mask
    
    
    def update_mask() -> ::Google::Protobuf::FieldMask

**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_gateway-v1/latest/Google-Protobuf-FieldMask)) — Field mask is used to specify the fields to be overwritten in the Gateway resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten. 



### #update_mask=
    
    
    def update_mask=(value) -> ::Google::Protobuf::FieldMask

**Parameter**

  * **value** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_gateway-v1/latest/Google-Protobuf-FieldMask)) — Field mask is used to specify the fields to be overwritten in the Gateway resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten. 



**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_gateway-v1/latest/Google-Protobuf-FieldMask)) — Field mask is used to specify the fields to be overwritten in the Gateway resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
