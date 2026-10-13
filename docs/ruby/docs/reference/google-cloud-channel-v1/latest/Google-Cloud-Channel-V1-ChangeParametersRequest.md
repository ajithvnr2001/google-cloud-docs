---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChangeParametersRequest/
title: Cloud Channel V1 API - Class Google::Cloud::Channel::V1::ChangeParametersRequest (v2.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:49:07.645588+00:00
---

# Cloud Channel V1 API - Class Google::Cloud::Channel::V1::ChangeParametersRequest (v2.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-ChangeParametersRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Channel V1 API - Class Google::Cloud::Channel::V1::ChangeParametersRequest (v2.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.6.1 (latest)  2.6.0  2.5.0  2.4.1  2.3.0  2.2.1  2.1.0  2.0.1  1.3.0  1.2.0  1.1.0  1.0.1  0.24.0  0.23.2  0.22.1  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.5 

Reference documentation and code samples for the Cloud Channel V1 API class Google::Cloud::Channel::V1::ChangeParametersRequest.

Request message for [CloudChannelService.ChangeParameters](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-CloudChannelService-Client#Google__Cloud__Channel__V1__CloudChannelService__Client_change_parameters_instance_ "Google::Cloud::Channel::V1::CloudChannelService::Client#change_parameters \(method\)").

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Required. The name of the entitlement to update. Name uses the format: accounts/{account_id}/customers/{customer_id}/entitlements/{entitlement_id} 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The name of the entitlement to update. Name uses the format: accounts/{account_id}/customers/{customer_id}/entitlements/{entitlement_id} 



**Returns**

  * (::String) — Required. The name of the entitlement to update. Name uses the format: accounts/{account_id}/customers/{customer_id}/entitlements/{entitlement_id} 



### #parameters
    
    
    def parameters() -> ::Array<::Google::Cloud::Channel::V1::Parameter>

**Returns**

  * (::Array<[::Google::Cloud::Channel::V1::Parameter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Parameter)>) — Required. Entitlement parameters to update. You can only change editable parameters.

To view the available Parameters for a request, refer to the [Offer.parameter_definitions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Offer#Google__Cloud__Channel__V1__Offer_parameter_definitions_instance_ "Google::Cloud::Channel::V1::Offer#parameter_definitions \(method\)") from the desired offer. 




### #parameters=
    
    
    def parameters=(value) -> ::Array<::Google::Cloud::Channel::V1::Parameter>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Channel::V1::Parameter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Parameter)>) — Required. Entitlement parameters to update. You can only change editable parameters.

To view the available Parameters for a request, refer to the [Offer.parameter_definitions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Offer#Google__Cloud__Channel__V1__Offer_parameter_definitions_instance_ "Google::Cloud::Channel::V1::Offer#parameter_definitions \(method\)") from the desired offer. 




**Returns**

  * (::Array<[::Google::Cloud::Channel::V1::Parameter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Parameter)>) — Required. Entitlement parameters to update. You can only change editable parameters.

To view the available Parameters for a request, refer to the [Offer.parameter_definitions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-Offer#Google__Cloud__Channel__V1__Offer_parameter_definitions_instance_ "Google::Cloud::Channel::V1::Offer#parameter_definitions \(method\)") from the desired offer. 




### #purchase_order_id
    
    
    def purchase_order_id() -> ::String

**Returns**

  * (::String) — Optional. Purchase order ID provided by the reseller. 



### #purchase_order_id=
    
    
    def purchase_order_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Purchase order ID provided by the reseller. 



**Returns**

  * (::String) — Optional. Purchase order ID provided by the reseller. 



### #request_id
    
    
    def request_id() -> ::String

**Returns**

  * (::String) — Optional. You can specify an optional unique request ID, and if you need to retry your request, the server will know to ignore the request if it's complete.

For example, you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if it received the original operation with the same request ID. If it did, it will ignore the second request.

The request ID must be a valid [UUID](https://tools.ietf.org/html/rfc4122) with the exception that zero UUID is not supported (`00000000-0000-0000-0000-000000000000`). 




### #request_id=
    
    
    def request_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. You can specify an optional unique request ID, and if you need to retry your request, the server will know to ignore the request if it's complete.

For example, you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if it received the original operation with the same request ID. If it did, it will ignore the second request.

The request ID must be a valid [UUID](https://tools.ietf.org/html/rfc4122) with the exception that zero UUID is not supported (`00000000-0000-0000-0000-000000000000`). 




**Returns**

  * (::String) — Optional. You can specify an optional unique request ID, and if you need to retry your request, the server will know to ignore the request if it's complete.

For example, you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if it received the original operation with the same request ID. If it did, it will ignore the second request.

The request ID must be a valid [UUID](https://tools.ietf.org/html/rfc4122) with the exception that zero UUID is not supported (`00000000-0000-0000-0000-000000000000`). 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
