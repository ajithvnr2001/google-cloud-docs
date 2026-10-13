---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-v1/latest/Google-Cloud-Firestore-V1-DocumentMask/
title: Cloud Firestore V1 API - Class Google::Cloud::Firestore::V1::DocumentMask (v2.4.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:12:36.982431+00:00
---

# Cloud Firestore V1 API - Class Google::Cloud::Firestore::V1::DocumentMask (v2.4.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-v1/latest/Google-Cloud-Firestore-V1-DocumentMask/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Firestore V1 API - Class Google::Cloud::Firestore::V1::DocumentMask (v2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.1  2.1.1  2.0.1  1.3.0  1.2.0  1.1.1  1.0.0  0.14.0  0.13.0  0.12.0  0.11.1  0.10.0  0.9.0  0.8.0  0.7.1  0.6.0  0.5.0  0.4.8 

Reference documentation and code samples for the Cloud Firestore V1 API class Google::Cloud::Firestore::V1::DocumentMask.

A set of field paths on a document. Used to restrict a get or update operation on a document to a subset of its fields. This is different from standard field masks, as this is always scoped to a [Document](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-v1/latest/Google-Cloud-Firestore-V1-Document "Google::Cloud::Firestore::V1::Document \(class\)"), and takes in account the dynamic nature of [Value](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-v1/latest/Google-Cloud-Firestore-V1-Value "Google::Cloud::Firestore::V1::Value \(class\)").

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #field_paths
    
    
    def field_paths() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — The list of field paths in the mask. See [Document.fields](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-v1/latest/Google-Cloud-Firestore-V1-Document#Google__Cloud__Firestore__V1__Document_fields_instance_ "Google::Cloud::Firestore::V1::Document#fields \(method\)") for a field path syntax reference. 



### #field_paths=
    
    
    def field_paths=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — The list of field paths in the mask. See [Document.fields](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-v1/latest/Google-Cloud-Firestore-V1-Document#Google__Cloud__Firestore__V1__Document_fields_instance_ "Google::Cloud::Firestore::V1::Document#fields \(method\)") for a field path syntax reference. 



**Returns**

  * (::Array<::String>) — The list of field paths in the mask. See [Document.fields](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-v1/latest/Google-Cloud-Firestore-V1-Document#Google__Cloud__Firestore__V1__Document_fields_instance_ "Google::Cloud::Firestore::V1::Document#fields \(method\)") for a field path syntax reference. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
