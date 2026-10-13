---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage-control-v2/latest/Google-Cloud-Storage-Control-V2-GetFolderRequest/
title: Storage Control V2 API - Class Google::Cloud::Storage::Control::V2::GetFolderRequest (v1.14.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:48:56.405084+00:00
---

# Storage Control V2 API - Class Google::Cloud::Storage::Control::V2::GetFolderRequest (v1.14.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage-control-v2/latest/Google-Cloud-Storage-Control-V2-GetFolderRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Storage Control V2 API - Class Google::Cloud::Storage::Control::V2::GetFolderRequest (v1.14.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.14.1 (latest)  1.14.0  1.13.1  1.12.0  1.11.0  1.10.1  1.9.0  1.8.1  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.1.1 

Reference documentation and code samples for the Storage Control V2 API class Google::Cloud::Storage::Control::V2::GetFolderRequest.

Request message for GetFolder. This operation is only applicable to a hierarchical namespace enabled bucket.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #if_metageneration_match
    
    
    def if_metageneration_match() -> ::Integer

**Returns**

  * (::Integer) — Makes the operation only succeed conditional on whether the folder's current metageneration matches the given value. 



### #if_metageneration_match=
    
    
    def if_metageneration_match=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Makes the operation only succeed conditional on whether the folder's current metageneration matches the given value. 



**Returns**

  * (::Integer) — Makes the operation only succeed conditional on whether the folder's current metageneration matches the given value. 



### #if_metageneration_not_match
    
    
    def if_metageneration_not_match() -> ::Integer

**Returns**

  * (::Integer) — Makes the operation only succeed conditional on whether the folder's current metageneration does not match the given value. 



### #if_metageneration_not_match=
    
    
    def if_metageneration_not_match=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Makes the operation only succeed conditional on whether the folder's current metageneration does not match the given value. 



**Returns**

  * (::Integer) — Makes the operation only succeed conditional on whether the folder's current metageneration does not match the given value. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Required. Name of the folder. Format: `projects/{project}/buckets/{bucket}/folders/{folder}`



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Name of the folder. Format: `projects/{project}/buckets/{bucket}/folders/{folder}`



**Returns**

  * (::String) — Required. Name of the folder. Format: `projects/{project}/buckets/{bucket}/folders/{folder}`



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
