---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-saas_platform-saas_service_mgmt-v1beta1/latest/Google-Cloud-SaasPlatform-SaasServiceMgmt-V1beta1-ListUnitKindsResponse/
title: App Lifecycle Manager V1BETA1 API - Class Google::Cloud::SaasPlatform::SaasServiceMgmt::V1beta1::ListUnitKindsResponse (v0.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:52:31.106368+00:00
---

# App Lifecycle Manager V1BETA1 API - Class Google::Cloud::SaasPlatform::SaasServiceMgmt::V1beta1::ListUnitKindsResponse (v0.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-saas_platform-saas_service_mgmt-v1beta1/latest/Google-Cloud-SaasPlatform-SaasServiceMgmt-V1beta1-ListUnitKindsResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  App Lifecycle Manager V1BETA1 API - Class Google::Cloud::SaasPlatform::SaasServiceMgmt::V1beta1::ListUnitKindsResponse (v0.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.8.1 (latest)  0.8.0  0.7.0  0.6.0  0.5.2  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the App Lifecycle Manager V1BETA1 API class Google::Cloud::SaasPlatform::SaasServiceMgmt::V1beta1::ListUnitKindsResponse.

The response structure for the ListUnitKinds method.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #next_page_token
    
    
    def next_page_token() -> ::String

**Returns**

  * (::String) — If present, the next page token can be provided to a subsequent ListUnitKinds call to list the next page. If empty, there are no more pages. 



### #next_page_token=
    
    
    def next_page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — If present, the next page token can be provided to a subsequent ListUnitKinds call to list the next page. If empty, there are no more pages. 



**Returns**

  * (::String) — If present, the next page token can be provided to a subsequent ListUnitKinds call to list the next page. If empty, there are no more pages. 



### #unit_kinds
    
    
    def unit_kinds() -> ::Array<::Google::Cloud::SaasPlatform::SaasServiceMgmt::V1beta1::UnitKind>

**Returns**

  * (::Array<[::Google::Cloud::SaasPlatform::SaasServiceMgmt::V1beta1::UnitKind](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-saas_platform-saas_service_mgmt-v1beta1/latest/Google-Cloud-SaasPlatform-SaasServiceMgmt-V1beta1-UnitKind)>) — The resulting unit kinds. 



### #unit_kinds=
    
    
    def unit_kinds=(value) -> ::Array<::Google::Cloud::SaasPlatform::SaasServiceMgmt::V1beta1::UnitKind>

**Parameter**

  * **value** (::Array<[::Google::Cloud::SaasPlatform::SaasServiceMgmt::V1beta1::UnitKind](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-saas_platform-saas_service_mgmt-v1beta1/latest/Google-Cloud-SaasPlatform-SaasServiceMgmt-V1beta1-UnitKind)>) — The resulting unit kinds. 



**Returns**

  * (::Array<[::Google::Cloud::SaasPlatform::SaasServiceMgmt::V1beta1::UnitKind](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-saas_platform-saas_service_mgmt-v1beta1/latest/Google-Cloud-SaasPlatform-SaasServiceMgmt-V1beta1-UnitKind)>) — The resulting unit kinds. 



### #unreachable
    
    
    def unreachable() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Locations that could not be reached. 



### #unreachable=
    
    
    def unreachable=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Locations that could not be reached. 



**Returns**

  * (::Array<::String>) — Locations that could not be reached. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
