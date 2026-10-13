---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-CustomAPIDependentRequestsConfig/
title: Chronicle V1 API - Class Google::Cloud::Chronicle::V1::CustomAPIDependentRequestsConfig (v1.1.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:32:13.665750+00:00
---

# Chronicle V1 API - Class Google::Cloud::Chronicle::V1::CustomAPIDependentRequestsConfig (v1.1.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-CustomAPIDependentRequestsConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Chronicle V1 API - Class Google::Cloud::Chronicle::V1::CustomAPIDependentRequestsConfig (v1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.1  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Chronicle V1 API class Google::Cloud::Chronicle::V1::CustomAPIDependentRequestsConfig.

Configuration for dependent requests (child chaining).

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #dependent_requests
    
    
    def dependent_requests() -> ::Array<::Google::Cloud::Chronicle::V1::CustomAPITransferNode>

**Returns**

  * (::Array<[::Google::Cloud::Chronicle::V1::CustomAPITransferNode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-CustomAPITransferNode)>) — Optional. Add follow-up API calls triggered for each item found in the primary request (e.g., fetching full event details for a list of basic alert IDs). Note: In MVP, the child depth fan-out limit is capped at 1. 



### #dependent_requests=
    
    
    def dependent_requests=(value) -> ::Array<::Google::Cloud::Chronicle::V1::CustomAPITransferNode>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Chronicle::V1::CustomAPITransferNode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-CustomAPITransferNode)>) — Optional. Add follow-up API calls triggered for each item found in the primary request (e.g., fetching full event details for a list of basic alert IDs). Note: In MVP, the child depth fan-out limit is capped at 1. 



**Returns**

  * (::Array<[::Google::Cloud::Chronicle::V1::CustomAPITransferNode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-CustomAPITransferNode)>) — Optional. Add follow-up API calls triggered for each item found in the primary request (e.g., fetching full event details for a list of basic alert IDs). Note: In MVP, the child depth fan-out limit is capped at 1. 



### #item_id_json_path
    
    
    def item_id_json_path() -> ::String

**Returns**

  * (::String) — Required. Enter the specific field in the response that uniquely identifies an individual record or alert. 



### #item_id_json_path=
    
    
    def item_id_json_path=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Enter the specific field in the response that uniquely identifies an individual record or alert. 



**Returns**

  * (::String) — Required. Enter the specific field in the response that uniquely identifies an individual record or alert. 



### #item_id_variable
    
    
    def item_id_variable() -> ::String

**Returns**

  * (::String) — Optional. Specify a custom variable name to hold the extracted ID, which can be linked as a placeholder in dependent requests. 



### #item_id_variable=
    
    
    def item_id_variable=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Specify a custom variable name to hold the extracted ID, which can be linked as a placeholder in dependent requests. 



**Returns**

  * (::String) — Optional. Specify a custom variable name to hold the extracted ID, which can be linked as a placeholder in dependent requests. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
