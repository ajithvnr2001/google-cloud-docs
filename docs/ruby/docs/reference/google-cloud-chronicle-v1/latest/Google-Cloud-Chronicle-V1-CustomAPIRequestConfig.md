---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-CustomAPIRequestConfig/
title: Chronicle V1 API - Class Google::Cloud::Chronicle::V1::CustomAPIRequestConfig (v1.1.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:50:51.652728+00:00
---

# Chronicle V1 API - Class Google::Cloud::Chronicle::V1::CustomAPIRequestConfig (v1.1.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-CustomAPIRequestConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Chronicle V1 API - Class Google::Cloud::Chronicle::V1::CustomAPIRequestConfig (v1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.1  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Chronicle V1 API class Google::Cloud::Chronicle::V1::CustomAPIRequestConfig.

Configuration for the outgoing API request.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #custom_headers
    
    
    def custom_headers() -> ::Array<::Google::Cloud::Chronicle::V1::HeaderKeyValue>

**Returns**

  * (::Array<[::Google::Cloud::Chronicle::V1::HeaderKeyValue](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-HeaderKeyValue)>) — Optional. Define specialized key-value pairs sent with the request, often used for custom API versioning or specific vendor requirements. 



### #custom_headers=
    
    
    def custom_headers=(value) -> ::Array<::Google::Cloud::Chronicle::V1::HeaderKeyValue>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Chronicle::V1::HeaderKeyValue](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-HeaderKeyValue)>) — Optional. Define specialized key-value pairs sent with the request, often used for custom API versioning or specific vendor requirements. 



**Returns**

  * (::Array<[::Google::Cloud::Chronicle::V1::HeaderKeyValue](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-HeaderKeyValue)>) — Optional. Define specialized key-value pairs sent with the request, often used for custom API versioning or specific vendor requirements. 



### #endpoint_path
    
    
    def endpoint_path() -> ::String

**Returns**

  * (::String) — Required. Enter the specific API route appended to the Base URL to fetch the data (e.g., /v1/alerts). 



### #endpoint_path=
    
    
    def endpoint_path=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Enter the specific API route appended to the Base URL to fetch the data (e.g., /v1/alerts). 



**Returns**

  * (::String) — Required. Enter the specific API route appended to the Base URL to fetch the data (e.g., /v1/alerts). 



### #http_method
    
    
    def http_method() -> ::Google::Cloud::Chronicle::V1::CustomAPIRequestConfig::HttpMethod

**Returns**

  * ([::Google::Cloud::Chronicle::V1::CustomAPIRequestConfig::HttpMethod](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-CustomAPIRequestConfig-HttpMethod)) — Required. Select the type of action to perform on the API endpoint (usually GET to retrieve data or POST to submit a query). 



### #http_method=
    
    
    def http_method=(value) -> ::Google::Cloud::Chronicle::V1::CustomAPIRequestConfig::HttpMethod

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::CustomAPIRequestConfig::HttpMethod](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-CustomAPIRequestConfig-HttpMethod)) — Required. Select the type of action to perform on the API endpoint (usually GET to retrieve data or POST to submit a query). 



**Returns**

  * ([::Google::Cloud::Chronicle::V1::CustomAPIRequestConfig::HttpMethod](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-CustomAPIRequestConfig-HttpMethod)) — Required. Select the type of action to perform on the API endpoint (usually GET to retrieve data or POST to submit a query). 



### #max_requests_per_minute
    
    
    def max_requests_per_minute() -> ::Integer

**Returns**

  * (::Integer) — Optional. Set a safety limit to ensure the connector does not exceed the third-party vendor's API rate limits. 



### #max_requests_per_minute=
    
    
    def max_requests_per_minute=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. Set a safety limit to ensure the connector does not exceed the third-party vendor's API rate limits. 



**Returns**

  * (::Integer) — Optional. Set a safety limit to ensure the connector does not exceed the third-party vendor's API rate limits. 



### #query_parameters
    
    
    def query_parameters() -> ::Array<::Google::Cloud::Chronicle::V1::HeaderKeyValue>

**Returns**

  * (::Array<[::Google::Cloud::Chronicle::V1::HeaderKeyValue](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-HeaderKeyValue)>) — Optional. Add extra filters or settings appended to the end of the URL (e.g., ?status=critical). 



### #query_parameters=
    
    
    def query_parameters=(value) -> ::Array<::Google::Cloud::Chronicle::V1::HeaderKeyValue>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Chronicle::V1::HeaderKeyValue](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-HeaderKeyValue)>) — Optional. Add extra filters or settings appended to the end of the URL (e.g., ?status=critical). 



**Returns**

  * (::Array<[::Google::Cloud::Chronicle::V1::HeaderKeyValue](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-HeaderKeyValue)>) — Optional. Add extra filters or settings appended to the end of the URL (e.g., ?status=critical). 



### #request_body
    
    
    def request_body() -> ::String

**Returns**

  * (::String) — Optional. Provide the data payload sent to the API to specify what information you want, typically formatted in JSON. 



### #request_body=
    
    
    def request_body=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Provide the data payload sent to the API to specify what information you want, typically formatted in JSON. 



**Returns**

  * (::String) — Optional. Provide the data payload sent to the API to specify what information you want, typically formatted in JSON. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
