---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tpu-v1/latest/Google-Cloud-Tpu-V1-ListNodesResponse/
title: Cloud TPU V1 API - Class Google::Cloud::Tpu::V1::ListNodesResponse (v1.7.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:17:29.858130+00:00
---

# Cloud TPU V1 API - Class Google::Cloud::Tpu::V1::ListNodesResponse (v1.7.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tpu-v1/latest/Google-Cloud-Tpu-V1-ListNodesResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud TPU V1 API - Class Google::Cloud::Tpu::V1::ListNodesResponse (v1.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.7.1 (latest)  1.7.0  1.6.0  1.5.1  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.7.0  0.6.2  0.5.0  0.4.1  0.3.0  0.2.0  0.1.4 

Reference documentation and code samples for the Cloud TPU V1 API class Google::Cloud::Tpu::V1::ListNodesResponse.

Response for [ListNodes](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tpu-v1/latest/Google-Cloud-Tpu-V1-Tpu-Client#Google__Cloud__Tpu__V1__Tpu__Client_list_nodes_instance_ "Google::Cloud::Tpu::V1::Tpu::Client#list_nodes \(method\)").

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

  * (::String) — The next page token or empty if none. 



### #next_page_token=
    
    
    def next_page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — The next page token or empty if none. 



**Returns**

  * (::String) — The next page token or empty if none. 



### #nodes
    
    
    def nodes() -> ::Array<::Google::Cloud::Tpu::V1::Node>

**Returns**

  * (::Array<[::Google::Cloud::Tpu::V1::Node](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tpu-v1/latest/Google-Cloud-Tpu-V1-Node)>) — The listed nodes. 



### #nodes=
    
    
    def nodes=(value) -> ::Array<::Google::Cloud::Tpu::V1::Node>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Tpu::V1::Node](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tpu-v1/latest/Google-Cloud-Tpu-V1-Node)>) — The listed nodes. 



**Returns**

  * (::Array<[::Google::Cloud::Tpu::V1::Node](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tpu-v1/latest/Google-Cloud-Tpu-V1-Node)>) — The listed nodes. 



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

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
