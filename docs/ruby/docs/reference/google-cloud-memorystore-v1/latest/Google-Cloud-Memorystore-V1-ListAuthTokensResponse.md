---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Cloud-Memorystore-V1-ListAuthTokensResponse/
title: Memorystore V1 API - Class Google::Cloud::Memorystore::V1::ListAuthTokensResponse (v1.11.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:35:06.269922+00:00
---

# Memorystore V1 API - Class Google::Cloud::Memorystore::V1::ListAuthTokensResponse (v1.11.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Cloud-Memorystore-V1-ListAuthTokensResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Memorystore V1 API - Class Google::Cloud::Memorystore::V1::ListAuthTokensResponse (v1.11.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.11.1 (latest)  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.1  1.0.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Memorystore V1 API class Google::Cloud::Memorystore::V1::ListAuthTokensResponse.

Response message for `ListAuthTokens`.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #auth_tokens
    
    
    def auth_tokens() -> ::Array<::Google::Cloud::Memorystore::V1::AuthToken>

**Returns**

  * (::Array<[::Google::Cloud::Memorystore::V1::AuthToken](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Cloud-Memorystore-V1-AuthToken)>) — A list of auth tokens in the project. 



### #auth_tokens=
    
    
    def auth_tokens=(value) -> ::Array<::Google::Cloud::Memorystore::V1::AuthToken>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Memorystore::V1::AuthToken](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Cloud-Memorystore-V1-AuthToken)>) — A list of auth tokens in the project. 



**Returns**

  * (::Array<[::Google::Cloud::Memorystore::V1::AuthToken](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Cloud-Memorystore-V1-AuthToken)>) — A list of auth tokens in the project. 



### #next_page_token
    
    
    def next_page_token() -> ::String

**Returns**

  * (::String) — Token to retrieve the next page of results, or empty if there are no more results in the list. 



### #next_page_token=
    
    
    def next_page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — Token to retrieve the next page of results, or empty if there are no more results in the list. 



**Returns**

  * (::String) — Token to retrieve the next page of results, or empty if there are no more results in the list. 



### #unreachable
    
    
    def unreachable() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Unordered list. Auth tokens that could not be reached. 



### #unreachable=
    
    
    def unreachable=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Unordered list. Auth tokens that could not be reached. 



**Returns**

  * (::Array<::String>) — Unordered list. Auth tokens that could not be reached. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
