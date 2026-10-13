---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-commerce-consumer-procurement-v1/latest/Google-Cloud-Commerce-Consumer-Procurement-V1-EnumerateLicensedUsersRequest/
title: Cloud Commerce Consumer Procurement V1 API - Class Google::Cloud::Commerce::Consumer::Procurement::V1::EnumerateLicensedUsersRequest (v1.10.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:35:16.615060+00:00
---

# Cloud Commerce Consumer Procurement V1 API - Class Google::Cloud::Commerce::Consumer::Procurement::V1::EnumerateLicensedUsersRequest (v1.10.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-commerce-consumer-procurement-v1/latest/Google-Cloud-Commerce-Consumer-Procurement-V1-EnumerateLicensedUsersRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Commerce Consumer Procurement V1 API - Class Google::Cloud::Commerce::Consumer::Procurement::V1::EnumerateLicensedUsersRequest (v1.10.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.10.0 (latest)  1.9.1  1.8.0  1.7.0  1.6.1  1.5.0  1.4.1  1.3.1  1.2.0  1.1.0  1.0.2  0.4.0  0.3.2  0.2.0  0.1.0 

Reference documentation and code samples for the Cloud Commerce Consumer Procurement V1 API class Google::Cloud::Commerce::Consumer::Procurement::V1::EnumerateLicensedUsersRequest.

Request message for [LicenseManagementService.EnumerateLicensedUsers](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-commerce-consumer-procurement-v1/latest/Google-Cloud-Commerce-Consumer-Procurement-V1-LicenseManagementService-Client#Google__Cloud__Commerce__Consumer__Procurement__V1__LicenseManagementService__Client_enumerate_licensed_users_instance_ "Google::Cloud::Commerce::Consumer::Procurement::V1::LicenseManagementService::Client#enumerate_licensed_users \(method\)").

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #page_size
    
    
    def page_size() -> ::Integer

**Returns**

  * (::Integer) — Optional. The maximum number of users to return. The service may return fewer than this value. 



### #page_size=
    
    
    def page_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. The maximum number of users to return. The service may return fewer than this value. 



**Returns**

  * (::Integer) — Optional. The maximum number of users to return. The service may return fewer than this value. 



### #page_token
    
    
    def page_token() -> ::String

**Returns**

  * (::String) — Optional. A page token, received from a previous `EnumerateLicensedUsers` call. Provide this to retrieve the subsequent page. 



### #page_token=
    
    
    def page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. A page token, received from a previous `EnumerateLicensedUsers` call. Provide this to retrieve the subsequent page. 



**Returns**

  * (::String) — Optional. A page token, received from a previous `EnumerateLicensedUsers` call. Provide this to retrieve the subsequent page. 



### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. License pool name. 



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. License pool name. 



**Returns**

  * (::String) — Required. License pool name. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
