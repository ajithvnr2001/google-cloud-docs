---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-OperationMetadataV1/
title: App Engine Admin V1 API - Class Google::Cloud::AppEngine::V1::OperationMetadataV1 (v1.8.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:48:33.500608+00:00
---

# App Engine Admin V1 API - Class Google::Cloud::AppEngine::V1::OperationMetadataV1 (v1.8.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-OperationMetadataV1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  App Engine Admin V1 API - Class Google::Cloud::AppEngine::V1::OperationMetadataV1 (v1.8.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.2 (latest)  1.8.1  1.7.0  1.6.0  1.5.1  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.10.0  0.9.2  0.8.0  0.7.0  0.6.1  0.5.0  0.4.0  0.3.6 

Reference documentation and code samples for the App Engine Admin V1 API class Google::Cloud::AppEngine::V1::OperationMetadataV1.

Metadata for the given [google.longrunning.Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Longrunning-Operation "Google::Longrunning::Operation \(class\)").

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #create_version_metadata
    
    
    def create_version_metadata() -> ::Google::Cloud::AppEngine::V1::CreateVersionMetadataV1

**Returns**

  * ([::Google::Cloud::AppEngine::V1::CreateVersionMetadataV1](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-CreateVersionMetadataV1)) 



### #create_version_metadata=
    
    
    def create_version_metadata=(value) -> ::Google::Cloud::AppEngine::V1::CreateVersionMetadataV1

**Parameter**

  * **value** ([::Google::Cloud::AppEngine::V1::CreateVersionMetadataV1](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-CreateVersionMetadataV1)) 



**Returns**

  * ([::Google::Cloud::AppEngine::V1::CreateVersionMetadataV1](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-CreateVersionMetadataV1)) 



### #end_time
    
    
    def end_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Protobuf-Timestamp)) — Time that this operation completed. 



### #end_time=
    
    
    def end_time=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Protobuf-Timestamp)) — Time that this operation completed. 



**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Protobuf-Timestamp)) — Time that this operation completed. 



### #ephemeral_message
    
    
    def ephemeral_message() -> ::String

**Returns**

  * (::String) — Ephemeral message that may change every time the operation is polled. 



### #ephemeral_message=
    
    
    def ephemeral_message=(value) -> ::String

**Parameter**

  * **value** (::String) — Ephemeral message that may change every time the operation is polled. 



**Returns**

  * (::String) — Ephemeral message that may change every time the operation is polled. 



### #insert_time
    
    
    def insert_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Protobuf-Timestamp)) — Time that this operation was created. 



### #insert_time=
    
    
    def insert_time=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Protobuf-Timestamp)) — Time that this operation was created. 



**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Protobuf-Timestamp)) — Time that this operation was created. 



### #method
    
    
    def method() -> ::String

**Returns**

  * (::String) — API method that initiated this operation. Example: `google.appengine.v1.Versions.CreateVersion`. 



### #method=
    
    
    def method=(value) -> ::String

**Parameter**

  * **value** (::String) — API method that initiated this operation. Example: `google.appengine.v1.Versions.CreateVersion`. 



**Returns**

  * (::String) — API method that initiated this operation. Example: `google.appengine.v1.Versions.CreateVersion`. 



### #target
    
    
    def target() -> ::String

**Returns**

  * (::String) — Name of the resource that this operation is acting on. Example: `apps/myapp/services/default`. 



### #target=
    
    
    def target=(value) -> ::String

**Parameter**

  * **value** (::String) — Name of the resource that this operation is acting on. Example: `apps/myapp/services/default`. 



**Returns**

  * (::String) — Name of the resource that this operation is acting on. Example: `apps/myapp/services/default`. 



### #user
    
    
    def user() -> ::String

**Returns**

  * (::String) — User who requested this operation. 



### #user=
    
    
    def user=(value) -> ::String

**Parameter**

  * **value** (::String) — User who requested this operation. 



**Returns**

  * (::String) — User who requested this operation. 



### #warning
    
    
    def warning() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Durable messages that persist on every operation poll. 



### #warning=
    
    
    def warning=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Durable messages that persist on every operation poll. 



**Returns**

  * (::Array<::String>) — Durable messages that persist on every operation poll. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
