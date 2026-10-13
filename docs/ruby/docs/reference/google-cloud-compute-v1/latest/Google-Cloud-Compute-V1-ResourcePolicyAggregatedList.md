---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ResourcePolicyAggregatedList/
title: Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::ResourcePolicyAggregatedList (v4.0.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:43:58.596581+00:00
---

# Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::ResourcePolicyAggregatedList (v4.0.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ResourcePolicyAggregatedList/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::ResourcePolicyAggregatedList (v4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.12.0  3.10.0  3.9.1  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.22.0  2.21.1  2.20.0  2.19.1  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.2  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.10.0  1.9.0  1.8.0  1.7.1  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.5.0 

Reference documentation and code samples for the Google Cloud Compute V1 API class Google::Cloud::Compute::V1::ResourcePolicyAggregatedList.

Contains a list of resourcePolicies.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #etag
    
    
    def etag() -> ::String

**Returns**

  * (::String) 



### #etag=
    
    
    def etag=(value) -> ::String

**Parameter**

  * **value** (::String) 



**Returns**

  * (::String) 



### #id
    
    
    def id() -> ::String

**Returns**

  * (::String) — [Output Only] Unique identifier for the resource; defined by the server. 



### #id=
    
    
    def id=(value) -> ::String

**Parameter**

  * **value** (::String) — [Output Only] Unique identifier for the resource; defined by the server. 



**Returns**

  * (::String) — [Output Only] Unique identifier for the resource; defined by the server. 



### #items
    
    
    def items() -> ::Google::Protobuf::Map{::String => ::Google::Cloud::Compute::V1::ResourcePoliciesScopedList}

**Returns**

  * (::Google::Protobuf::Map{::String => ::Google::Cloud::Compute::V1::ResourcePoliciesScopedList}) — A list of ResourcePolicy resources. 



### #items=
    
    
    def items=(value) -> ::Google::Protobuf::Map{::String => ::Google::Cloud::Compute::V1::ResourcePoliciesScopedList}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::Google::Cloud::Compute::V1::ResourcePoliciesScopedList}) — A list of ResourcePolicy resources. 



**Returns**

  * (::Google::Protobuf::Map{::String => ::Google::Cloud::Compute::V1::ResourcePoliciesScopedList}) — A list of ResourcePolicy resources. 



### #kind
    
    
    def kind() -> ::String

**Returns**

  * (::String) — Output only. Type of resource. 



### #kind=
    
    
    def kind=(value) -> ::String

**Parameter**

  * **value** (::String) — Output only. Type of resource. 



**Returns**

  * (::String) — Output only. Type of resource. 



### #next_page_token
    
    
    def next_page_token() -> ::String

**Returns**

  * (::String) — [Output Only] This token allows you to get the next page of results for list requests. If the number of results is larger thanmaxResults, use the nextPageToken as a value for the query parameter pageToken in the next list request. Subsequent list requests will have their own nextPageToken to continue paging through the results. 



### #next_page_token=
    
    
    def next_page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — [Output Only] This token allows you to get the next page of results for list requests. If the number of results is larger thanmaxResults, use the nextPageToken as a value for the query parameter pageToken in the next list request. Subsequent list requests will have their own nextPageToken to continue paging through the results. 



**Returns**

  * (::String) — [Output Only] This token allows you to get the next page of results for list requests. If the number of results is larger thanmaxResults, use the nextPageToken as a value for the query parameter pageToken in the next list request. Subsequent list requests will have their own nextPageToken to continue paging through the results. 



### #self_link
    
    
    def self_link() -> ::String

**Returns**

  * (::String) — Output only. [Output Only] Server-defined URL for this resource. 



### #self_link=
    
    
    def self_link=(value) -> ::String

**Parameter**

  * **value** (::String) — Output only. [Output Only] Server-defined URL for this resource. 



**Returns**

  * (::String) — Output only. [Output Only] Server-defined URL for this resource. 



### #unreachables
    
    
    def unreachables() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Output only. [Output Only] Unreachable resources. 



### #unreachables=
    
    
    def unreachables=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Output only. [Output Only] Unreachable resources. 



**Returns**

  * (::Array<::String>) — Output only. [Output Only] Unreachable resources. 



### #warning
    
    
    def warning() -> ::Google::Cloud::Compute::V1::Warning

**Returns**

  * ([::Google::Cloud::Compute::V1::Warning](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Warning)) — [Output Only] Informational warning message. 



### #warning=
    
    
    def warning=(value) -> ::Google::Cloud::Compute::V1::Warning

**Parameter**

  * **value** ([::Google::Cloud::Compute::V1::Warning](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Warning)) — [Output Only] Informational warning message. 



**Returns**

  * ([::Google::Cloud::Compute::V1::Warning](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Warning)) — [Output Only] Informational warning message. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
