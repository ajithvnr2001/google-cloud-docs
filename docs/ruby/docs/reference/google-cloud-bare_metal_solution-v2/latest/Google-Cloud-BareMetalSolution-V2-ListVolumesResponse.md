---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bare_metal_solution-v2/latest/Google-Cloud-BareMetalSolution-V2-ListVolumesResponse/
title: Bare Metal Solution V2 API - Class Google::Cloud::BareMetalSolution::V2::ListVolumesResponse (v1.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:33:39.680032+00:00
---

# Bare Metal Solution V2 API - Class Google::Cloud::BareMetalSolution::V2::ListVolumesResponse (v1.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bare_metal_solution-v2/latest/Google-Cloud-BareMetalSolution-V2-ListVolumesResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Bare Metal Solution V2 API - Class Google::Cloud::BareMetalSolution::V2::ListVolumesResponse (v1.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.6.1 (latest)  1.6.0  1.5.0  1.4.0  1.3.1  1.2.0  1.1.0  1.0.1  0.10.0  0.9.0  0.8.1  0.7.2  0.6.0  0.5.1  0.4.1  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Bare Metal Solution V2 API class Google::Cloud::BareMetalSolution::V2::ListVolumesResponse.

Response message containing the list of storage volumes.

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

  * (::String) — A token identifying a page of results from the server. 



### #next_page_token=
    
    
    def next_page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — A token identifying a page of results from the server. 



**Returns**

  * (::String) — A token identifying a page of results from the server. 



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



### #volumes
    
    
    def volumes() -> ::Array<::Google::Cloud::BareMetalSolution::V2::Volume>

**Returns**

  * (::Array<[::Google::Cloud::BareMetalSolution::V2::Volume](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bare_metal_solution-v2/latest/Google-Cloud-BareMetalSolution-V2-Volume)>) — The list of storage volumes. 



### #volumes=
    
    
    def volumes=(value) -> ::Array<::Google::Cloud::BareMetalSolution::V2::Volume>

**Parameter**

  * **value** (::Array<[::Google::Cloud::BareMetalSolution::V2::Volume](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bare_metal_solution-v2/latest/Google-Cloud-BareMetalSolution-V2-Volume)>) — The list of storage volumes. 



**Returns**

  * (::Array<[::Google::Cloud::BareMetalSolution::V2::Volume](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bare_metal_solution-v2/latest/Google-Cloud-BareMetalSolution-V2-Volume)>) — The list of storage volumes. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
