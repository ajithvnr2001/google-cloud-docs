---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-license_manager-v1/latest/Google-Cloud-LicenseManager-V1-ListConfigurationsResponse/
title: License Manager V1 API - Class Google::Cloud::LicenseManager::V1::ListConfigurationsResponse (v1.0.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:20:00.482665+00:00
---

# License Manager V1 API - Class Google::Cloud::LicenseManager::V1::ListConfigurationsResponse (v1.0.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-license_manager-v1/latest/Google-Cloud-LicenseManager-V1-ListConfigurationsResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  License Manager V1 API - Class Google::Cloud::LicenseManager::V1::ListConfigurationsResponse (v1.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0 (latest)  0.6.0  0.5.0  0.4.0  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the License Manager V1 API class Google::Cloud::LicenseManager::V1::ListConfigurationsResponse.

Message for response to listing Configurations

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #configurations
    
    
    def configurations() -> ::Array<::Google::Cloud::LicenseManager::V1::Configuration>

**Returns**

  * (::Array<[::Google::Cloud::LicenseManager::V1::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-license_manager-v1/latest/Google-Cloud-LicenseManager-V1-Configuration)>) — The list of Configuration 



### #configurations=
    
    
    def configurations=(value) -> ::Array<::Google::Cloud::LicenseManager::V1::Configuration>

**Parameter**

  * **value** (::Array<[::Google::Cloud::LicenseManager::V1::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-license_manager-v1/latest/Google-Cloud-LicenseManager-V1-Configuration)>) — The list of Configuration 



**Returns**

  * (::Array<[::Google::Cloud::LicenseManager::V1::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-license_manager-v1/latest/Google-Cloud-LicenseManager-V1-Configuration)>) — The list of Configuration 



### #next_page_token
    
    
    def next_page_token() -> ::String

**Returns**

  * (::String) — A token identifying a page of results the server should return. 



### #next_page_token=
    
    
    def next_page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — A token identifying a page of results the server should return. 



**Returns**

  * (::String) — A token identifying a page of results the server should return. 



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

Last updated 2026-08-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-04 UTC."],[],[]] 
