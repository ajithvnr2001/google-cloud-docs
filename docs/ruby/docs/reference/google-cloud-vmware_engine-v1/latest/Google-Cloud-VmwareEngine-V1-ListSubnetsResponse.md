---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vmware_engine-v1/latest/Google-Cloud-VmwareEngine-V1-ListSubnetsResponse/
title: Google Cloud VMware Engine V1 API - Class Google::Cloud::VmwareEngine::V1::ListSubnetsResponse (v1.5.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:34:16.907148+00:00
---

# Google Cloud VMware Engine V1 API - Class Google::Cloud::VmwareEngine::V1::ListSubnetsResponse (v1.5.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vmware_engine-v1/latest/Google-Cloud-VmwareEngine-V1-ListSubnetsResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud VMware Engine V1 API - Class Google::Cloud::VmwareEngine::V1::ListSubnetsResponse (v1.5.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.5.2 (latest)  1.5.1  1.4.1  1.3.1  1.2.0  1.1.0  1.0.1  0.11.0  0.10.0  0.9.2  0.8.0  0.7.1  0.6.1  0.5.0  0.4.0  0.3.1  0.2.0  0.1.1 

Reference documentation and code samples for the Google Cloud VMware Engine V1 API class Google::Cloud::VmwareEngine::V1::ListSubnetsResponse.

Response message for [VmwareEngine.ListSubnets](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vmware_engine-v1/latest/Google-Cloud-VmwareEngine-V1-VmwareEngine-Client#Google__Cloud__VmwareEngine__V1__VmwareEngine__Client_list_subnets_instance_ "Google::Cloud::VmwareEngine::V1::VmwareEngine::Client#list_subnets \(method\)")

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

  * (::String) — A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. 



### #next_page_token=
    
    
    def next_page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. 



**Returns**

  * (::String) — A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. 



### #subnets
    
    
    def subnets() -> ::Array<::Google::Cloud::VmwareEngine::V1::Subnet>

**Returns**

  * (::Array<[::Google::Cloud::VmwareEngine::V1::Subnet](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vmware_engine-v1/latest/Google-Cloud-VmwareEngine-V1-Subnet)>) — A list of subnets. 



### #subnets=
    
    
    def subnets=(value) -> ::Array<::Google::Cloud::VmwareEngine::V1::Subnet>

**Parameter**

  * **value** (::Array<[::Google::Cloud::VmwareEngine::V1::Subnet](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vmware_engine-v1/latest/Google-Cloud-VmwareEngine-V1-Subnet)>) — A list of subnets. 



**Returns**

  * (::Array<[::Google::Cloud::VmwareEngine::V1::Subnet](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vmware_engine-v1/latest/Google-Cloud-VmwareEngine-V1-Subnet)>) — A list of subnets. 



### #unreachable
    
    
    def unreachable() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Locations that could not be reached when making an aggregated query using wildcards. 



### #unreachable=
    
    
    def unreachable=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Locations that could not be reached when making an aggregated query using wildcards. 



**Returns**

  * (::Array<::String>) — Locations that could not be reached when making an aggregated query using wildcards. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
