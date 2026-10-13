---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage-control-v2/latest/Google-Cloud-Storage-Control-V2-ListRapidCachesRequest/
title: Storage Control V2 API - Class Google::Cloud::Storage::Control::V2::ListRapidCachesRequest (v1.14.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:10:21.541945+00:00
---

# Storage Control V2 API - Class Google::Cloud::Storage::Control::V2::ListRapidCachesRequest (v1.14.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage-control-v2/latest/Google-Cloud-Storage-Control-V2-ListRapidCachesRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Storage Control V2 API - Class Google::Cloud::Storage::Control::V2::ListRapidCachesRequest (v1.14.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.14.1 (latest)  1.14.0  1.13.1  1.12.0  1.11.0  1.10.1  1.9.0  1.8.1  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.1.1 

Reference documentation and code samples for the Storage Control V2 API class Google::Cloud::Storage::Control::V2::ListRapidCachesRequest.

Request message for ListRapidCaches.

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

  * (::Integer) — Maximum number of caches to return in a single response. The service will use this parameter or 1,000 items, whichever is smaller. 



### #page_size=
    
    
    def page_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Maximum number of caches to return in a single response. The service will use this parameter or 1,000 items, whichever is smaller. 



**Returns**

  * (::Integer) — Maximum number of caches to return in a single response. The service will use this parameter or 1,000 items, whichever is smaller. 



### #page_token
    
    
    def page_token() -> ::String

**Returns**

  * (::String) — A previously-returned page token representing part of the larger set of results to view. 



### #page_token=
    
    
    def page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — A previously-returned page token representing part of the larger set of results to view. 



**Returns**

  * (::String) — A previously-returned page token representing part of the larger set of results to view. 



### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. The bucket to which this cache belongs. 



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The bucket to which this cache belongs. 



**Returns**

  * (::String) — Required. The bucket to which this cache belongs. 



### #request_id
    
    
    def request_id() -> ::String

**Returns**

  * (::String) — Optional. A unique identifier for this request. UUID is the recommended format, but other formats are still accepted. 



### #request_id=
    
    
    def request_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. A unique identifier for this request. UUID is the recommended format, but other formats are still accepted. 



**Returns**

  * (::String) — Optional. A unique identifier for this request. UUID is the recommended format, but other formats are still accepted. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
