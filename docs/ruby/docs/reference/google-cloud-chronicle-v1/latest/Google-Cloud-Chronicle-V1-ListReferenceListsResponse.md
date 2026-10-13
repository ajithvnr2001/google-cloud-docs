---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-ListReferenceListsResponse/
title: Chronicle V1 API - Class Google::Cloud::Chronicle::V1::ListReferenceListsResponse (v1.1.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:40:52.930242+00:00
---

# Chronicle V1 API - Class Google::Cloud::Chronicle::V1::ListReferenceListsResponse (v1.1.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-ListReferenceListsResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Chronicle V1 API - Class Google::Cloud::Chronicle::V1::ListReferenceListsResponse (v1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.1  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Chronicle V1 API class Google::Cloud::Chronicle::V1::ListReferenceListsResponse.

A response to a request for a list of reference lists.

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

  * (::String) — A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. 



### #next_page_token=
    
    
    def next_page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. 



**Returns**

  * (::String) — A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. 



### #reference_lists
    
    
    def reference_lists() -> ::Array<::Google::Cloud::Chronicle::V1::ReferenceList>

**Returns**

  * (::Array<[::Google::Cloud::Chronicle::V1::ReferenceList](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-ReferenceList)>) — The reference lists. Ordered in ascending alphabetical order by name. 



### #reference_lists=
    
    
    def reference_lists=(value) -> ::Array<::Google::Cloud::Chronicle::V1::ReferenceList>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Chronicle::V1::ReferenceList](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-ReferenceList)>) — The reference lists. Ordered in ascending alphabetical order by name. 



**Returns**

  * (::Array<[::Google::Cloud::Chronicle::V1::ReferenceList](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-ReferenceList)>) — The reference lists. Ordered in ascending alphabetical order by name. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
