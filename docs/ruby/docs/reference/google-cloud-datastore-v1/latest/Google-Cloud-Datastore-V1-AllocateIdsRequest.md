---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore-v1/latest/Google-Cloud-Datastore-V1-AllocateIdsRequest/
title: Firestore in Datastore mode V1 API - Class Google::Cloud::Datastore::V1::AllocateIdsRequest (v1.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:07:46.377889+00:00
---

# Firestore in Datastore mode V1 API - Class Google::Cloud::Datastore::V1::AllocateIdsRequest (v1.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore-v1/latest/Google-Cloud-Datastore-V1-AllocateIdsRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Firestore in Datastore mode V1 API - Class Google::Cloud::Datastore::V1::AllocateIdsRequest (v1.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.1 (latest)  1.8.0  1.7.0  1.6.0  1.5.1  1.4.1  1.3.1  1.2.0  1.1.0  1.0.1  0.19.0  0.18.0  0.17.0  0.16.3  0.15.0  0.14.0  0.13.1  0.12.0  0.11.1  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.5 

Reference documentation and code samples for the Firestore in Datastore mode V1 API class Google::Cloud::Datastore::V1::AllocateIdsRequest.

The request for [Datastore.AllocateIds](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore-v1/latest/Google-Cloud-Datastore-V1-Datastore-Client#Google__Cloud__Datastore__V1__Datastore__Client_allocate_ids_instance_ "Google::Cloud::Datastore::V1::Datastore::Client#allocate_ids \(method\)").

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #database_id
    
    
    def database_id() -> ::String

**Returns**

  * (::String) — The ID of the database against which to make the request.

'(default)' is not allowed; please use empty string '' to refer the default database. 




### #database_id=
    
    
    def database_id=(value) -> ::String

**Parameter**

  * **value** (::String) — The ID of the database against which to make the request.

'(default)' is not allowed; please use empty string '' to refer the default database. 




**Returns**

  * (::String) — The ID of the database against which to make the request.

'(default)' is not allowed; please use empty string '' to refer the default database. 




### #keys
    
    
    def keys() -> ::Array<::Google::Cloud::Datastore::V1::Key>

**Returns**

  * (::Array<[::Google::Cloud::Datastore::V1::Key](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore-v1/latest/Google-Cloud-Datastore-V1-Key)>) — Required. A list of keys with incomplete key paths for which to allocate IDs. No key may be reserved/read-only. 



### #keys=
    
    
    def keys=(value) -> ::Array<::Google::Cloud::Datastore::V1::Key>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Datastore::V1::Key](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore-v1/latest/Google-Cloud-Datastore-V1-Key)>) — Required. A list of keys with incomplete key paths for which to allocate IDs. No key may be reserved/read-only. 



**Returns**

  * (::Array<[::Google::Cloud::Datastore::V1::Key](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore-v1/latest/Google-Cloud-Datastore-V1-Key)>) — Required. A list of keys with incomplete key paths for which to allocate IDs. No key may be reserved/read-only. 



### #project_id
    
    
    def project_id() -> ::String

**Returns**

  * (::String) — Required. The ID of the project against which to make the request. 



### #project_id=
    
    
    def project_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The ID of the project against which to make the request. 



**Returns**

  * (::String) — Required. The ID of the project against which to make the request. 



### #request_options
    
    
    def request_options() -> ::Google::Cloud::Datastore::V1::RequestOptions

**Returns**

  * ([::Google::Cloud::Datastore::V1::RequestOptions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore-v1/latest/Google-Cloud-Datastore-V1-RequestOptions)) — Optional. The options for this request. 



### #request_options=
    
    
    def request_options=(value) -> ::Google::Cloud::Datastore::V1::RequestOptions

**Parameter**

  * **value** ([::Google::Cloud::Datastore::V1::RequestOptions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore-v1/latest/Google-Cloud-Datastore-V1-RequestOptions)) — Optional. The options for this request. 



**Returns**

  * ([::Google::Cloud::Datastore::V1::RequestOptions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore-v1/latest/Google-Cloud-Datastore-V1-RequestOptions)) — Optional. The options for this request. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
