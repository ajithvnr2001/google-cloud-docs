---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-saas_platform-saas_service_mgmt-v1beta1/latest/Google-Cloud-SaasPlatform-SaasServiceMgmt-V1beta1-CreateRolloutRequest/
title: App Lifecycle Manager V1BETA1 API - Class Google::Cloud::SaasPlatform::SaasServiceMgmt::V1beta1::CreateRolloutRequest (v0.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:11:02.208189+00:00
---

# App Lifecycle Manager V1BETA1 API - Class Google::Cloud::SaasPlatform::SaasServiceMgmt::V1beta1::CreateRolloutRequest (v0.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-saas_platform-saas_service_mgmt-v1beta1/latest/Google-Cloud-SaasPlatform-SaasServiceMgmt-V1beta1-CreateRolloutRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  App Lifecycle Manager V1BETA1 API - Class Google::Cloud::SaasPlatform::SaasServiceMgmt::V1beta1::CreateRolloutRequest (v0.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.8.1 (latest)  0.8.0  0.7.0  0.6.0  0.5.2  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the App Lifecycle Manager V1BETA1 API class Google::Cloud::SaasPlatform::SaasServiceMgmt::V1beta1::CreateRolloutRequest.

The request structure for the CreateRollout method.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. The parent of the rollout. 



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The parent of the rollout. 



**Returns**

  * (::String) — Required. The parent of the rollout. 



### #request_id
    
    
    def request_id() -> ::String

**Returns**

  * (::String) — An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




### #request_id=
    
    
    def request_id=(value) -> ::String

**Parameter**

  * **value** (::String) — An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




**Returns**

  * (::String) — An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




### #rollout
    
    
    def rollout() -> ::Google::Cloud::SaasPlatform::SaasServiceMgmt::V1beta1::Rollout

**Returns**

  * ([::Google::Cloud::SaasPlatform::SaasServiceMgmt::V1beta1::Rollout](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-saas_platform-saas_service_mgmt-v1beta1/latest/Google-Cloud-SaasPlatform-SaasServiceMgmt-V1beta1-Rollout)) — Required. The desired state for the rollout. 



### #rollout=
    
    
    def rollout=(value) -> ::Google::Cloud::SaasPlatform::SaasServiceMgmt::V1beta1::Rollout

**Parameter**

  * **value** ([::Google::Cloud::SaasPlatform::SaasServiceMgmt::V1beta1::Rollout](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-saas_platform-saas_service_mgmt-v1beta1/latest/Google-Cloud-SaasPlatform-SaasServiceMgmt-V1beta1-Rollout)) — Required. The desired state for the rollout. 



**Returns**

  * ([::Google::Cloud::SaasPlatform::SaasServiceMgmt::V1beta1::Rollout](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-saas_platform-saas_service_mgmt-v1beta1/latest/Google-Cloud-SaasPlatform-SaasServiceMgmt-V1beta1-Rollout)) — Required. The desired state for the rollout. 



### #rollout_id
    
    
    def rollout_id() -> ::String

**Returns**

  * (::String) — Required. The ID value for the new rollout. 



### #rollout_id=
    
    
    def rollout_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The ID value for the new rollout. 



**Returns**

  * (::String) — Required. The ID value for the new rollout. 



### #validate_only
    
    
    def validate_only() -> ::Boolean

**Returns**

  * (::Boolean) — If "validate_only" is set to true, the service will try to validate that this request would succeed, but will not actually make changes. 



### #validate_only=
    
    
    def validate_only=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — If "validate_only" is set to true, the service will try to validate that this request would succeed, but will not actually make changes. 



**Returns**

  * (::Boolean) — If "validate_only" is set to true, the service will try to validate that this request would succeed, but will not actually make changes. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
