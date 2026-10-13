---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ListArtifactsRequest/
title: Apigee Registry V1 API - Class Google::Cloud::ApigeeRegistry::V1::ListArtifactsRequest (v0.16.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:09:36.323332+00:00
---

# Apigee Registry V1 API - Class Google::Cloud::ApigeeRegistry::V1::ListArtifactsRequest (v0.16.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-ListArtifactsRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Apigee Registry V1 API - Class Google::Cloud::ApigeeRegistry::V1::ListArtifactsRequest (v0.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.17.0 (latest)  0.16.0  0.15.0  0.14.0  0.13.1  0.12.0  0.11.0  0.10.1  0.9.0  0.8.1  0.7.2  0.6.0  0.5.0  0.4.0  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Apigee Registry V1 API class Google::Cloud::ApigeeRegistry::V1::ListArtifactsRequest.

Request message for ListArtifacts.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #filter
    
    
    def filter() -> ::String

**Returns**

  * (::String) — An expression that can be used to filter the list. Filters use the Common Expression Language and can refer to all message fields except contents. 



### #filter=
    
    
    def filter=(value) -> ::String

**Parameter**

  * **value** (::String) — An expression that can be used to filter the list. Filters use the Common Expression Language and can refer to all message fields except contents. 



**Returns**

  * (::String) — An expression that can be used to filter the list. Filters use the Common Expression Language and can refer to all message fields except contents. 



### #page_size
    
    
    def page_size() -> ::Integer

**Returns**

  * (::Integer) — The maximum number of artifacts to return. The service may return fewer than this value. If unspecified, at most 50 values will be returned. The maximum is 1000; values above 1000 will be coerced to 1000. 



### #page_size=
    
    
    def page_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The maximum number of artifacts to return. The service may return fewer than this value. If unspecified, at most 50 values will be returned. The maximum is 1000; values above 1000 will be coerced to 1000. 



**Returns**

  * (::Integer) — The maximum number of artifacts to return. The service may return fewer than this value. If unspecified, at most 50 values will be returned. The maximum is 1000; values above 1000 will be coerced to 1000. 



### #page_token
    
    
    def page_token() -> ::String

**Returns**

  * (::String) — A page token, received from a previous `ListArtifacts` call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to `ListArtifacts` must match the call that provided the page token. 




### #page_token=
    
    
    def page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — A page token, received from a previous `ListArtifacts` call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to `ListArtifacts` must match the call that provided the page token. 




**Returns**

  * (::String) — A page token, received from a previous `ListArtifacts` call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to `ListArtifacts` must match the call that provided the page token. 




### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. The parent, which owns this collection of artifacts. Format: `{parent}`



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The parent, which owns this collection of artifacts. Format: `{parent}`



**Returns**

  * (::String) — Required. The parent, which owns this collection of artifacts. Format: `{parent}`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
