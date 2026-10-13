---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-v1/latest/Google-Cloud-Firestore-V1-DocumentChange/
title: Cloud Firestore V1 API - Class Google::Cloud::Firestore::V1::DocumentChange (v2.4.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:14:14.634130+00:00
---

# Cloud Firestore V1 API - Class Google::Cloud::Firestore::V1::DocumentChange (v2.4.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-v1/latest/Google-Cloud-Firestore-V1-DocumentChange/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Firestore V1 API - Class Google::Cloud::Firestore::V1::DocumentChange (v2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.1  2.1.1  2.0.1  1.3.0  1.2.0  1.1.1  1.0.0  0.14.0  0.13.0  0.12.0  0.11.1  0.10.0  0.9.0  0.8.0  0.7.1  0.6.0  0.5.0  0.4.8 

Reference documentation and code samples for the Cloud Firestore V1 API class Google::Cloud::Firestore::V1::DocumentChange.

A [Document](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-v1/latest/Google-Cloud-Firestore-V1-Document "Google::Cloud::Firestore::V1::Document \(class\)") has changed.

May be the result of multiple [writes](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-v1/latest/Google-Cloud-Firestore-V1-Write "Google::Cloud::Firestore::V1::Write \(class\)"), including deletes, that ultimately resulted in a new value for the [Document](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-v1/latest/Google-Cloud-Firestore-V1-Document "Google::Cloud::Firestore::V1::Document \(class\)").

Multiple [DocumentChange](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-v1/latest/Google-Cloud-Firestore-V1-DocumentChange "Google::Cloud::Firestore::V1::DocumentChange \(class\)") messages may be returned for the same logical change, if multiple targets are affected.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #document
    
    
    def document() -> ::Google::Cloud::Firestore::V1::Document

**Returns**

  * ([::Google::Cloud::Firestore::V1::Document](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-v1/latest/Google-Cloud-Firestore-V1-Document)) — The new state of the [Document](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-v1/latest/Google-Cloud-Firestore-V1-Document "Google::Cloud::Firestore::V1::Document \(class\)").

If `mask` is set, contains only fields that were updated or added. 




### #document=
    
    
    def document=(value) -> ::Google::Cloud::Firestore::V1::Document

**Parameter**

  * **value** ([::Google::Cloud::Firestore::V1::Document](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-v1/latest/Google-Cloud-Firestore-V1-Document)) — The new state of the [Document](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-v1/latest/Google-Cloud-Firestore-V1-Document "Google::Cloud::Firestore::V1::Document \(class\)").

If `mask` is set, contains only fields that were updated or added. 




**Returns**

  * ([::Google::Cloud::Firestore::V1::Document](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-v1/latest/Google-Cloud-Firestore-V1-Document)) — The new state of the [Document](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-v1/latest/Google-Cloud-Firestore-V1-Document "Google::Cloud::Firestore::V1::Document \(class\)").

If `mask` is set, contains only fields that were updated or added. 




### #removed_target_ids
    
    
    def removed_target_ids() -> ::Array<::Integer>

**Returns**

  * (::Array<::Integer>) — A set of target IDs for targets that no longer match this document. 



### #removed_target_ids=
    
    
    def removed_target_ids=(value) -> ::Array<::Integer>

**Parameter**

  * **value** (::Array<::Integer>) — A set of target IDs for targets that no longer match this document. 



**Returns**

  * (::Array<::Integer>) — A set of target IDs for targets that no longer match this document. 



### #target_ids
    
    
    def target_ids() -> ::Array<::Integer>

**Returns**

  * (::Array<::Integer>) — A set of target IDs of targets that match this document. 



### #target_ids=
    
    
    def target_ids=(value) -> ::Array<::Integer>

**Parameter**

  * **value** (::Array<::Integer>) — A set of target IDs of targets that match this document. 



**Returns**

  * (::Array<::Integer>) — A set of target IDs of targets that match this document. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
