---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_services-v1/latest/Google-Cloud-NetworkServices-V1-UpdateEndpointPolicyRequest/
title: Network Services V1 API - Class Google::Cloud::NetworkServices::V1::UpdateEndpointPolicyRequest (v2.12.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:48:10.009511+00:00
---

# Network Services V1 API - Class Google::Cloud::NetworkServices::V1::UpdateEndpointPolicyRequest (v2.12.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_services-v1/latest/Google-Cloud-NetworkServices-V1-UpdateEndpointPolicyRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Network Services V1 API - Class Google::Cloud::NetworkServices::V1::UpdateEndpointPolicyRequest (v2.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.12.0 (latest)  2.11.0  2.10.1  2.9.0  2.8.0  2.7.0  2.6.1  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.1  1.2.0  1.1.0  1.0.1  0.2.0  0.1.0 

Reference documentation and code samples for the Network Services V1 API class Google::Cloud::NetworkServices::V1::UpdateEndpointPolicyRequest.

Request used with the UpdateEndpointPolicy method.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #endpoint_policy
    
    
    def endpoint_policy() -> ::Google::Cloud::NetworkServices::V1::EndpointPolicy

**Returns**

  * ([::Google::Cloud::NetworkServices::V1::EndpointPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_services-v1/latest/Google-Cloud-NetworkServices-V1-EndpointPolicy)) — Required. Updated EndpointPolicy resource. 



### #endpoint_policy=
    
    
    def endpoint_policy=(value) -> ::Google::Cloud::NetworkServices::V1::EndpointPolicy

**Parameter**

  * **value** ([::Google::Cloud::NetworkServices::V1::EndpointPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_services-v1/latest/Google-Cloud-NetworkServices-V1-EndpointPolicy)) — Required. Updated EndpointPolicy resource. 



**Returns**

  * ([::Google::Cloud::NetworkServices::V1::EndpointPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_services-v1/latest/Google-Cloud-NetworkServices-V1-EndpointPolicy)) — Required. Updated EndpointPolicy resource. 



### #update_mask
    
    
    def update_mask() -> ::Google::Protobuf::FieldMask

**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_services-v1/latest/Google-Protobuf-FieldMask)) — Optional. Field mask is used to specify the fields to be overwritten in the EndpointPolicy resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten. 



### #update_mask=
    
    
    def update_mask=(value) -> ::Google::Protobuf::FieldMask

**Parameter**

  * **value** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_services-v1/latest/Google-Protobuf-FieldMask)) — Optional. Field mask is used to specify the fields to be overwritten in the EndpointPolicy resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten. 



**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_services-v1/latest/Google-Protobuf-FieldMask)) — Optional. Field mask is used to specify the fields to be overwritten in the EndpointPolicy resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-03 UTC."],[],[]] 
