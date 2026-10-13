---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-assured_workloads-v1/latest/Google-Cloud-AssuredWorkloads-V1-ListWorkloadsResponse/
title: Assured Workloads for Government V1 API - Class Google::Cloud::AssuredWorkloads::V1::ListWorkloadsResponse (v1.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:18:11.845300+00:00
---

# Assured Workloads for Government V1 API - Class Google::Cloud::AssuredWorkloads::V1::ListWorkloadsResponse (v1.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-assured_workloads-v1/latest/Google-Cloud-AssuredWorkloads-V1-ListWorkloadsResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Assured Workloads for Government V1 API - Class Google::Cloud::AssuredWorkloads::V1::ListWorkloadsResponse (v1.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.1 (latest)  1.8.0  1.7.0  1.6.0  1.5.1  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.10.0  0.9.2  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.1 

Reference documentation and code samples for the Assured Workloads for Government V1 API class Google::Cloud::AssuredWorkloads::V1::ListWorkloadsResponse.

Response of ListWorkloads endpoint.

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

  * (::String) — The next page token. Return empty if reached the last page. 



### #next_page_token=
    
    
    def next_page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — The next page token. Return empty if reached the last page. 



**Returns**

  * (::String) — The next page token. Return empty if reached the last page. 



### #workloads
    
    
    def workloads() -> ::Array<::Google::Cloud::AssuredWorkloads::V1::Workload>

**Returns**

  * (::Array<[::Google::Cloud::AssuredWorkloads::V1::Workload](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-assured_workloads-v1/latest/Google-Cloud-AssuredWorkloads-V1-Workload)>) — List of Workloads under a given parent. 



### #workloads=
    
    
    def workloads=(value) -> ::Array<::Google::Cloud::AssuredWorkloads::V1::Workload>

**Parameter**

  * **value** (::Array<[::Google::Cloud::AssuredWorkloads::V1::Workload](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-assured_workloads-v1/latest/Google-Cloud-AssuredWorkloads-V1-Workload)>) — List of Workloads under a given parent. 



**Returns**

  * (::Array<[::Google::Cloud::AssuredWorkloads::V1::Workload](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-assured_workloads-v1/latest/Google-Cloud-AssuredWorkloads-V1-Workload)>) — List of Workloads under a given parent. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
