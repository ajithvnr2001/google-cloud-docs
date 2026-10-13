---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v2/latest/Google-Cloud-Notebooks-V2-ListInstancesRequest/
title: Notebooks V2 API - Class Google::Cloud::Notebooks::V2::ListInstancesRequest (v1.6.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:24:04.133608+00:00
---

# Notebooks V2 API - Class Google::Cloud::Notebooks::V2::ListInstancesRequest (v1.6.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v2/latest/Google-Cloud-Notebooks-V2-ListInstancesRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Notebooks V2 API - Class Google::Cloud::Notebooks::V2::ListInstancesRequest (v1.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.6.0 (latest)  1.5.0  1.4.0  1.3.1  1.2.0  1.1.0  1.0.1  0.6.0  0.5.0  0.4.2  0.3.2  0.2.0  0.1.0 

Reference documentation and code samples for the Notebooks V2 API class Google::Cloud::Notebooks::V2::ListInstancesRequest.

Request for listing notebook instances.

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

  * (::String) — Optional. List filter. 



### #filter=
    
    
    def filter=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. List filter. 



**Returns**

  * (::String) — Optional. List filter. 



### #order_by
    
    
    def order_by() -> ::String

**Returns**

  * (::String) — Optional. Sort results. Supported values are "name", "name desc" or "" (unsorted). 



### #order_by=
    
    
    def order_by=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Sort results. Supported values are "name", "name desc" or "" (unsorted). 



**Returns**

  * (::String) — Optional. Sort results. Supported values are "name", "name desc" or "" (unsorted). 



### #page_size
    
    
    def page_size() -> ::Integer

**Returns**

  * (::Integer) — Optional. Maximum return size of the list call. 



### #page_size=
    
    
    def page_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. Maximum return size of the list call. 



**Returns**

  * (::Integer) — Optional. Maximum return size of the list call. 



### #page_token
    
    
    def page_token() -> ::String

**Returns**

  * (::String) — Optional. A previous returned page token that can be used to continue listing from the last result. 



### #page_token=
    
    
    def page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. A previous returned page token that can be used to continue listing from the last result. 



**Returns**

  * (::String) — Optional. A previous returned page token that can be used to continue listing from the last result. 



### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. Format: `parent=projects/{project_id}/locations/{location}`



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Format: `parent=projects/{project_id}/locations/{location}`



**Returns**

  * (::String) — Required. Format: `parent=projects/{project_id}/locations/{location}`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-26 UTC."],[],[]] 
