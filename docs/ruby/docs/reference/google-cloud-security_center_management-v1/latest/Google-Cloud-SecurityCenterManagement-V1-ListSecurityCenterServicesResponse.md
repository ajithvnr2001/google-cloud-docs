---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-ListSecurityCenterServicesResponse/
title: Security Command Center Management V1 API - Class Google::Cloud::SecurityCenterManagement::V1::ListSecurityCenterServicesResponse (v1.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:51:24.367149+00:00
---

# Security Command Center Management V1 API - Class Google::Cloud::SecurityCenterManagement::V1::ListSecurityCenterServicesResponse (v1.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-ListSecurityCenterServicesResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Security Command Center Management V1 API - Class Google::Cloud::SecurityCenterManagement::V1::ListSecurityCenterServicesResponse (v1.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.1 (latest)  1.8.0  1.7.1  1.6.0  1.5.1  1.4.0  1.3.1  1.2.0  1.1.0  1.0.1  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Security Command Center Management V1 API class Google::Cloud::SecurityCenterManagement::V1::ListSecurityCenterServicesResponse.

Response message for [SecurityCenterManagement.ListSecurityCenterServices](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-SecurityCenterManagement-Client#Google__Cloud__SecurityCenterManagement__V1__SecurityCenterManagement__Client_list_security_center_services_instance_ "Google::Cloud::SecurityCenterManagement::V1::SecurityCenterManagement::Client#list_security_center_services \(method\)").

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

  * (::String) — A pagination token. To retrieve the next page of results, call the method again with this token. 



### #next_page_token=
    
    
    def next_page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — A pagination token. To retrieve the next page of results, call the method again with this token. 



**Returns**

  * (::String) — A pagination token. To retrieve the next page of results, call the method again with this token. 



### #security_center_services
    
    
    def security_center_services() -> ::Array<::Google::Cloud::SecurityCenterManagement::V1::SecurityCenterService>

**Returns**

  * (::Array<[::Google::Cloud::SecurityCenterManagement::V1::SecurityCenterService](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-SecurityCenterService)>) — The list of services. 



### #security_center_services=
    
    
    def security_center_services=(value) -> ::Array<::Google::Cloud::SecurityCenterManagement::V1::SecurityCenterService>

**Parameter**

  * **value** (::Array<[::Google::Cloud::SecurityCenterManagement::V1::SecurityCenterService](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-SecurityCenterService)>) — The list of services. 



**Returns**

  * (::Array<[::Google::Cloud::SecurityCenterManagement::V1::SecurityCenterService](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center_management-v1/latest/Google-Cloud-SecurityCenterManagement-V1-SecurityCenterService)>) — The list of services. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
