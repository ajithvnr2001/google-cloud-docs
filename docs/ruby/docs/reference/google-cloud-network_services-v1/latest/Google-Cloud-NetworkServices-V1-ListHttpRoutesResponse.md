---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_services-v1/latest/Google-Cloud-NetworkServices-V1-ListHttpRoutesResponse/
title: Network Services V1 API - Class Google::Cloud::NetworkServices::V1::ListHttpRoutesResponse (v2.12.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:04:16.439287+00:00
---

# Network Services V1 API - Class Google::Cloud::NetworkServices::V1::ListHttpRoutesResponse (v2.12.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_services-v1/latest/Google-Cloud-NetworkServices-V1-ListHttpRoutesResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Network Services V1 API - Class Google::Cloud::NetworkServices::V1::ListHttpRoutesResponse (v2.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.12.0 (latest)  2.11.0  2.10.1  2.9.0  2.8.0  2.7.0  2.6.1  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.1  1.2.0  1.1.0  1.0.1  0.2.0  0.1.0 

Reference documentation and code samples for the Network Services V1 API class Google::Cloud::NetworkServices::V1::ListHttpRoutesResponse.

Response returned by the ListHttpRoutes method.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #http_routes
    
    
    def http_routes() -> ::Array<::Google::Cloud::NetworkServices::V1::HttpRoute>

**Returns**

  * (::Array<[::Google::Cloud::NetworkServices::V1::HttpRoute](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_services-v1/latest/Google-Cloud-NetworkServices-V1-HttpRoute)>) — List of HttpRoute resources. 



### #http_routes=
    
    
    def http_routes=(value) -> ::Array<::Google::Cloud::NetworkServices::V1::HttpRoute>

**Parameter**

  * **value** (::Array<[::Google::Cloud::NetworkServices::V1::HttpRoute](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_services-v1/latest/Google-Cloud-NetworkServices-V1-HttpRoute)>) — List of HttpRoute resources. 



**Returns**

  * (::Array<[::Google::Cloud::NetworkServices::V1::HttpRoute](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_services-v1/latest/Google-Cloud-NetworkServices-V1-HttpRoute)>) — List of HttpRoute resources. 



### #next_page_token
    
    
    def next_page_token() -> ::String

**Returns**

  * (::String) — If there might be more results than those appearing in this response, then `next_page_token` is included. To get the next set of results, call this method again using the value of `next_page_token` as `page_token`. 



### #next_page_token=
    
    
    def next_page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — If there might be more results than those appearing in this response, then `next_page_token` is included. To get the next set of results, call this method again using the value of `next_page_token` as `page_token`. 



**Returns**

  * (::String) — If there might be more results than those appearing in this response, then `next_page_token` is included. To get the next set of results, call this method again using the value of `next_page_token` as `page_token`. 



### #unreachable
    
    
    def unreachable() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Unreachable resources. Populated when the request opts into [return_partial_success](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_services-v1/latest/Google-Cloud-NetworkServices-V1-ListHttpRoutesRequest#Google__Cloud__NetworkServices__V1__ListHttpRoutesRequest_return_partial_success_instance_ "Google::Cloud::NetworkServices::V1::ListHttpRoutesRequest#return_partial_success \(method\)") and reading across collections e.g. when attempting to list all resources across all supported locations. 



### #unreachable=
    
    
    def unreachable=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Unreachable resources. Populated when the request opts into [return_partial_success](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_services-v1/latest/Google-Cloud-NetworkServices-V1-ListHttpRoutesRequest#Google__Cloud__NetworkServices__V1__ListHttpRoutesRequest_return_partial_success_instance_ "Google::Cloud::NetworkServices::V1::ListHttpRoutesRequest#return_partial_success \(method\)") and reading across collections e.g. when attempting to list all resources across all supported locations. 



**Returns**

  * (::Array<::String>) — Unreachable resources. Populated when the request opts into [return_partial_success](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_services-v1/latest/Google-Cloud-NetworkServices-V1-ListHttpRoutesRequest#Google__Cloud__NetworkServices__V1__ListHttpRoutesRequest_return_partial_success_instance_ "Google::Cloud::NetworkServices::V1::ListHttpRoutesRequest#return_partial_success \(method\)") and reading across collections e.g. when attempting to list all resources across all supported locations. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-03 UTC."],[],[]] 
