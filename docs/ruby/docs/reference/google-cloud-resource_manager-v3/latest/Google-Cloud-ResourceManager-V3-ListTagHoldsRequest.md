---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-resource_manager-v3/latest/Google-Cloud-ResourceManager-V3-ListTagHoldsRequest/
title: Resource Manager V3 API - Class Google::Cloud::ResourceManager::V3::ListTagHoldsRequest (v1.8.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:24:20.003192+00:00
---

# Resource Manager V3 API - Class Google::Cloud::ResourceManager::V3::ListTagHoldsRequest (v1.8.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-resource_manager-v3/latest/Google-Cloud-ResourceManager-V3-ListTagHoldsRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Resource Manager V3 API - Class Google::Cloud::ResourceManager::V3::ListTagHoldsRequest (v1.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.0 (latest)  1.7.1  1.6.0  1.5.1  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.9.0  0.8.2  0.7.0  0.6.2  0.5.1  0.4.0  0.3.0  0.2.0  0.1.3 

Reference documentation and code samples for the Resource Manager V3 API class Google::Cloud::ResourceManager::V3::ListTagHoldsRequest.

The request message for listing the TagHolds under a TagValue.

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

  * (::String) — 

Optional. Criteria used to select a subset of TagHolds parented by the TagValue to return. This field follows the syntax defined by aip.dev/160; the `holder` and `origin` fields are supported for filtering. Currently only `AND` syntax is supported. Some example queries are:

    * `holder = //compute.googleapis.com/compute/projects/myproject/regions/us-east-1/instanceGroupManagers/instance-group`
    * `origin = 35678234`
    * `holder = //compute.googleapis.com/compute/projects/myproject/regions/us-east-1/instanceGroupManagers/instance-group AND origin = 35678234`



### #filter=
    
    
    def filter=(value) -> ::String

**Parameter**

  * **value** (::String) — 

Optional. Criteria used to select a subset of TagHolds parented by the TagValue to return. This field follows the syntax defined by aip.dev/160; the `holder` and `origin` fields are supported for filtering. Currently only `AND` syntax is supported. Some example queries are:

    * `holder = //compute.googleapis.com/compute/projects/myproject/regions/us-east-1/instanceGroupManagers/instance-group`
    * `origin = 35678234`
    * `holder = //compute.googleapis.com/compute/projects/myproject/regions/us-east-1/instanceGroupManagers/instance-group AND origin = 35678234`



**Returns**

  * (::String) — 

Optional. Criteria used to select a subset of TagHolds parented by the TagValue to return. This field follows the syntax defined by aip.dev/160; the `holder` and `origin` fields are supported for filtering. Currently only `AND` syntax is supported. Some example queries are:

    * `holder = //compute.googleapis.com/compute/projects/myproject/regions/us-east-1/instanceGroupManagers/instance-group`
    * `origin = 35678234`
    * `holder = //compute.googleapis.com/compute/projects/myproject/regions/us-east-1/instanceGroupManagers/instance-group AND origin = 35678234`



### #page_size
    
    
    def page_size() -> ::Integer

**Returns**

  * (::Integer) — Optional. The maximum number of TagHolds to return in the response. The server allows a maximum of 300 TagHolds to return. If unspecified, the server will use 100 as the default. 



### #page_size=
    
    
    def page_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. The maximum number of TagHolds to return in the response. The server allows a maximum of 300 TagHolds to return. If unspecified, the server will use 100 as the default. 



**Returns**

  * (::Integer) — Optional. The maximum number of TagHolds to return in the response. The server allows a maximum of 300 TagHolds to return. If unspecified, the server will use 100 as the default. 



### #page_token
    
    
    def page_token() -> ::String

**Returns**

  * (::String) — Optional. A pagination token returned from a previous call to `ListTagHolds` that indicates where this listing should continue from. 



### #page_token=
    
    
    def page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. A pagination token returned from a previous call to `ListTagHolds` that indicates where this listing should continue from. 



**Returns**

  * (::String) — Optional. A pagination token returned from a previous call to `ListTagHolds` that indicates where this listing should continue from. 



### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. The resource name of the parent TagValue. Must be of the form: `tagValues/{tag-value-id}`. 



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The resource name of the parent TagValue. Must be of the form: `tagValues/{tag-value-id}`. 



**Returns**

  * (::String) — Required. The resource name of the parent TagValue. Must be of the form: `tagValues/{tag-value-id}`. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
