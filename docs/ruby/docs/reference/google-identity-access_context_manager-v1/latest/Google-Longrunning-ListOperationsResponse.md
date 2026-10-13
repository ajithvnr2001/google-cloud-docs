---
url: https://docs.cloud.google.com/ruby/docs/reference/google-identity-access_context_manager-v1/latest/Google-Longrunning-ListOperationsResponse/
title: Access Context Manager V1 API - Class Google::Longrunning::ListOperationsResponse (v0.15.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:49:02.574630+00:00
---

# Access Context Manager V1 API - Class Google::Longrunning::ListOperationsResponse (v0.15.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-identity-access_context_manager-v1/latest/Google-Longrunning-ListOperationsResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Access Context Manager V1 API - Class Google::Longrunning::ListOperationsResponse (v0.15.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.15.1 (latest)  0.15.0  0.14.1  0.13.1  0.12.0  0.11.0  0.10.1  0.9.0  0.8.2  0.7.2  0.6.0  0.5.2  0.4.0  0.3.0  0.2.0  0.1.2 

Reference documentation and code samples for the Access Context Manager V1 API class Google::Longrunning::ListOperationsResponse.

The response message for Operations.ListOperations.

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

  * (::String) — The standard List next-page token. 



### #next_page_token=
    
    
    def next_page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — The standard List next-page token. 



**Returns**

  * (::String) — The standard List next-page token. 



### #operations
    
    
    def operations() -> ::Array<::Google::Longrunning::Operation>

**Returns**

  * (::Array<[::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-identity-access_context_manager-v1/latest/Google-Longrunning-Operation)>) — A list of operations that matches the specified filter in the request. 



### #operations=
    
    
    def operations=(value) -> ::Array<::Google::Longrunning::Operation>

**Parameter**

  * **value** (::Array<[::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-identity-access_context_manager-v1/latest/Google-Longrunning-Operation)>) — A list of operations that matches the specified filter in the request. 



**Returns**

  * (::Array<[::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-identity-access_context_manager-v1/latest/Google-Longrunning-Operation)>) — A list of operations that matches the specified filter in the request. 



### #unreachable
    
    
    def unreachable() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Unordered list. Unreachable resources. Populated when the request sets `ListOperationsRequest.return_partial_success` and reads across collections e.g. when attempting to list all resources across all supported locations. 



### #unreachable=
    
    
    def unreachable=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Unordered list. Unreachable resources. Populated when the request sets `ListOperationsRequest.return_partial_success` and reads across collections e.g. when attempting to list all resources across all supported locations. 



**Returns**

  * (::Array<::String>) — Unordered list. Unreachable resources. Populated when the request sets `ListOperationsRequest.return_partial_success` and reads across collections e.g. when attempting to list all resources across all supported locations. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
