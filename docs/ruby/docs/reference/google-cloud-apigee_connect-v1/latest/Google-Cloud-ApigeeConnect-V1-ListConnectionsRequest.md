---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_connect-v1/latest/Google-Cloud-ApigeeConnect-V1-ListConnectionsRequest/
title: Apigee Connect V1 API - Class Google::Cloud::ApigeeConnect::V1::ListConnectionsRequest (v1.7.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:34:26.833786+00:00
---

# Apigee Connect V1 API - Class Google::Cloud::ApigeeConnect::V1::ListConnectionsRequest (v1.7.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_connect-v1/latest/Google-Cloud-ApigeeConnect-V1-ListConnectionsRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Apigee Connect V1 API - Class Google::Cloud::ApigeeConnect::V1::ListConnectionsRequest (v1.7.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.7.2 (latest)  1.7.1  1.6.0  1.5.0  1.4.1  1.3.0  1.2.1  1.1.0  1.0.1  0.7.0  0.6.2  0.5.0  0.4.0  0.3.0  0.2.0  0.1.4 

Reference documentation and code samples for the Apigee Connect V1 API class Google::Cloud::ApigeeConnect::V1::ListConnectionsRequest.

The request for [ListConnections][Management.ListConnections].

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #page_size
    
    
    def page_size() -> ::Integer

**Returns**

  * (::Integer) — The maximum number of connections to return. The service may return fewer than this value. If unspecified, at most 100 connections will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000. 



### #page_size=
    
    
    def page_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The maximum number of connections to return. The service may return fewer than this value. If unspecified, at most 100 connections will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000. 



**Returns**

  * (::Integer) — The maximum number of connections to return. The service may return fewer than this value. If unspecified, at most 100 connections will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000. 



### #page_token
    
    
    def page_token() -> ::String

**Returns**

  * (::String) — A page token, received from a previous `ListConnections` call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to `ListConnections` must match the call that provided the page token. 




### #page_token=
    
    
    def page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — A page token, received from a previous `ListConnections` call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to `ListConnections` must match the call that provided the page token. 




**Returns**

  * (::String) — A page token, received from a previous `ListConnections` call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to `ListConnections` must match the call that provided the page token. 




### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. Parent name of the form: `projects/{project_number or project_id}/endpoints/{endpoint}`. 



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Parent name of the form: `projects/{project_number or project_id}/endpoints/{endpoint}`. 



**Returns**

  * (::String) — Required. Parent name of the form: `projects/{project_number or project_id}/endpoints/{endpoint}`. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
