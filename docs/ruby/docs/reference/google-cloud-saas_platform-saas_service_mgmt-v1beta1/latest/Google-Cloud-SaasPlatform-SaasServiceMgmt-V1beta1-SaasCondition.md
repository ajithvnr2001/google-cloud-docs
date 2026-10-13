---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-saas_platform-saas_service_mgmt-v1beta1/latest/Google-Cloud-SaasPlatform-SaasServiceMgmt-V1beta1-SaasCondition/
title: App Lifecycle Manager V1BETA1 API - Class Google::Cloud::SaasPlatform::SaasServiceMgmt::V1beta1::SaasCondition (v0.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:41:19.247945+00:00
---

# App Lifecycle Manager V1BETA1 API - Class Google::Cloud::SaasPlatform::SaasServiceMgmt::V1beta1::SaasCondition (v0.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-saas_platform-saas_service_mgmt-v1beta1/latest/Google-Cloud-SaasPlatform-SaasServiceMgmt-V1beta1-SaasCondition/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  App Lifecycle Manager V1BETA1 API - Class Google::Cloud::SaasPlatform::SaasServiceMgmt::V1beta1::SaasCondition (v0.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.8.1 (latest)  0.8.0  0.7.0  0.6.0  0.5.2  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the App Lifecycle Manager V1BETA1 API class Google::Cloud::SaasPlatform::SaasServiceMgmt::V1beta1::SaasCondition.

SaasCondition describes the status of a Saas.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #last_transition_time
    
    
    def last_transition_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-saas_platform-saas_service_mgmt-v1beta1/latest/Google-Protobuf-Timestamp)) — Required. Last time the condition transited from one status to another. 



### #last_transition_time=
    
    
    def last_transition_time=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-saas_platform-saas_service_mgmt-v1beta1/latest/Google-Protobuf-Timestamp)) — Required. Last time the condition transited from one status to another. 



**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-saas_platform-saas_service_mgmt-v1beta1/latest/Google-Protobuf-Timestamp)) — Required. Last time the condition transited from one status to another. 



### #message
    
    
    def message() -> ::String

**Returns**

  * (::String) — Required. Human readable message indicating details about the last transition. 



### #message=
    
    
    def message=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Human readable message indicating details about the last transition. 



**Returns**

  * (::String) — Required. Human readable message indicating details about the last transition. 



### #reason
    
    
    def reason() -> ::String

**Returns**

  * (::String) — Required. Brief reason for the condition's last transition. 



### #reason=
    
    
    def reason=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Brief reason for the condition's last transition. 



**Returns**

  * (::String) — Required. Brief reason for the condition's last transition. 



### #status
    
    
    def status() -> ::Google::Cloud::SaasPlatform::SaasServiceMgmt::V1beta1::SaasCondition::Status

**Returns**

  * ([::Google::Cloud::SaasPlatform::SaasServiceMgmt::V1beta1::SaasCondition::Status](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-saas_platform-saas_service_mgmt-v1beta1/latest/Google-Cloud-SaasPlatform-SaasServiceMgmt-V1beta1-SaasCondition-Status)) — Required. Status of the condition. 



### #status=
    
    
    def status=(value) -> ::Google::Cloud::SaasPlatform::SaasServiceMgmt::V1beta1::SaasCondition::Status

**Parameter**

  * **value** ([::Google::Cloud::SaasPlatform::SaasServiceMgmt::V1beta1::SaasCondition::Status](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-saas_platform-saas_service_mgmt-v1beta1/latest/Google-Cloud-SaasPlatform-SaasServiceMgmt-V1beta1-SaasCondition-Status)) — Required. Status of the condition. 



**Returns**

  * ([::Google::Cloud::SaasPlatform::SaasServiceMgmt::V1beta1::SaasCondition::Status](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-saas_platform-saas_service_mgmt-v1beta1/latest/Google-Cloud-SaasPlatform-SaasServiceMgmt-V1beta1-SaasCondition-Status)) — Required. Status of the condition. 



### #type
    
    
    def type() -> ::Google::Cloud::SaasPlatform::SaasServiceMgmt::V1beta1::SaasCondition::Type

**Returns**

  * ([::Google::Cloud::SaasPlatform::SaasServiceMgmt::V1beta1::SaasCondition::Type](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-saas_platform-saas_service_mgmt-v1beta1/latest/Google-Cloud-SaasPlatform-SaasServiceMgmt-V1beta1-SaasCondition-Type)) — Required. Type of the condition. 



### #type=
    
    
    def type=(value) -> ::Google::Cloud::SaasPlatform::SaasServiceMgmt::V1beta1::SaasCondition::Type

**Parameter**

  * **value** ([::Google::Cloud::SaasPlatform::SaasServiceMgmt::V1beta1::SaasCondition::Type](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-saas_platform-saas_service_mgmt-v1beta1/latest/Google-Cloud-SaasPlatform-SaasServiceMgmt-V1beta1-SaasCondition-Type)) — Required. Type of the condition. 



**Returns**

  * ([::Google::Cloud::SaasPlatform::SaasServiceMgmt::V1beta1::SaasCondition::Type](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-saas_platform-saas_service_mgmt-v1beta1/latest/Google-Cloud-SaasPlatform-SaasServiceMgmt-V1beta1-SaasCondition-Type)) — Required. Type of the condition. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
