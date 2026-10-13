---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-v1/latest/Google-Cloud-Firestore-V1-GetDocumentRequest/
title: Cloud Firestore V1 API - Class Google::Cloud::Firestore::V1::GetDocumentRequest (v2.4.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:19:57.444660+00:00
---

# Cloud Firestore V1 API - Class Google::Cloud::Firestore::V1::GetDocumentRequest (v2.4.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-v1/latest/Google-Cloud-Firestore-V1-GetDocumentRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Firestore V1 API - Class Google::Cloud::Firestore::V1::GetDocumentRequest (v2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.1  2.1.1  2.0.1  1.3.0  1.2.0  1.1.1  1.0.0  0.14.0  0.13.0  0.12.0  0.11.1  0.10.0  0.9.0  0.8.0  0.7.1  0.6.0  0.5.0  0.4.8 

Reference documentation and code samples for the Cloud Firestore V1 API class Google::Cloud::Firestore::V1::GetDocumentRequest.

The request for [Firestore.GetDocument](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-v1/latest/Google-Cloud-Firestore-V1-Firestore-Client#Google__Cloud__Firestore__V1__Firestore__Client_get_document_instance_ "Google::Cloud::Firestore::V1::Firestore::Client#get_document \(method\)").

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #mask
    
    
    def mask() -> ::Google::Cloud::Firestore::V1::DocumentMask

**Returns**

  * ([::Google::Cloud::Firestore::V1::DocumentMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-v1/latest/Google-Cloud-Firestore-V1-DocumentMask)) — The fields to return. If not set, returns all fields.

If the document has a field that is not present in this mask, that field will not be returned in the response. 




### #mask=
    
    
    def mask=(value) -> ::Google::Cloud::Firestore::V1::DocumentMask

**Parameter**

  * **value** ([::Google::Cloud::Firestore::V1::DocumentMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-v1/latest/Google-Cloud-Firestore-V1-DocumentMask)) — The fields to return. If not set, returns all fields.

If the document has a field that is not present in this mask, that field will not be returned in the response. 




**Returns**

  * ([::Google::Cloud::Firestore::V1::DocumentMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-v1/latest/Google-Cloud-Firestore-V1-DocumentMask)) — The fields to return. If not set, returns all fields.

If the document has a field that is not present in this mask, that field will not be returned in the response. 




### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Required. The resource name of the Document to get. In the format: `projects/{project_id}/databases/{database_id}/documents/{document_path}`. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The resource name of the Document to get. In the format: `projects/{project_id}/databases/{database_id}/documents/{document_path}`. 



**Returns**

  * (::String) — Required. The resource name of the Document to get. In the format: `projects/{project_id}/databases/{database_id}/documents/{document_path}`. 



### #read_time
    
    
    def read_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-v1/latest/Google-Protobuf-Timestamp)) — Reads the version of the document at the given time.

This must be a microsecond precision timestamp within the past one hour, or if Point-in-Time Recovery is enabled, can additionally be a whole minute timestamp within the past 7 days.

Note: The following fields are mutually exclusive: `read_time`, `transaction`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #read_time=
    
    
    def read_time=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-v1/latest/Google-Protobuf-Timestamp)) — Reads the version of the document at the given time.

This must be a microsecond precision timestamp within the past one hour, or if Point-in-Time Recovery is enabled, can additionally be a whole minute timestamp within the past 7 days.

Note: The following fields are mutually exclusive: `read_time`, `transaction`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-firestore-v1/latest/Google-Protobuf-Timestamp)) — Reads the version of the document at the given time.

This must be a microsecond precision timestamp within the past one hour, or if Point-in-Time Recovery is enabled, can additionally be a whole minute timestamp within the past 7 days.

Note: The following fields are mutually exclusive: `read_time`, `transaction`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #transaction
    
    
    def transaction() -> ::String

**Returns**

  * (::String) — Reads the document in a transaction.

Note: The following fields are mutually exclusive: `transaction`, `read_time`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #transaction=
    
    
    def transaction=(value) -> ::String

**Parameter**

  * **value** (::String) — Reads the document in a transaction.

Note: The following fields are mutually exclusive: `transaction`, `read_time`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::String) — Reads the document in a transaction.

Note: The following fields are mutually exclusive: `transaction`, `read_time`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
