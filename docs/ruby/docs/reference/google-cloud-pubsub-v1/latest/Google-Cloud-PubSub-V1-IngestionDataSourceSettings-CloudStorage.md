---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-IngestionDataSourceSettings-CloudStorage/
title: Cloud Pub/Sub V1 API - Class Google::Cloud::PubSub::V1::IngestionDataSourceSettings::CloudStorage (v1.18.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:39:03.350075+00:00
---

# Cloud Pub/Sub V1 API - Class Google::Cloud::PubSub::V1::IngestionDataSourceSettings::CloudStorage (v1.18.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-IngestionDataSourceSettings-CloudStorage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Pub/Sub V1 API - Class Google::Cloud::PubSub::V1::IngestionDataSourceSettings::CloudStorage (v1.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.18.0 (latest)  1.17.0  1.16.0  1.15.0  1.14.2  1.13.0  1.12.0  1.11.1  1.10.0  1.9.0  1.8.2  1.7.1  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.2  1.0.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.2  0.20.2  0.19.0  0.18.1  0.17.4  0.16.0  0.15.1  0.14.0  0.13.1  0.12.1  0.11.0  0.10.0  0.9.0  0.8.0  0.7.1  0.6.2 

Reference documentation and code samples for the Cloud Pub/Sub V1 API class Google::Cloud::PubSub::V1::IngestionDataSourceSettings::CloudStorage.

Ingestion settings for Cloud Storage.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #avro_format
    
    
    def avro_format() -> ::Google::Cloud::PubSub::V1::IngestionDataSourceSettings::CloudStorage::AvroFormat

**Returns**

  * ([::Google::Cloud::PubSub::V1::IngestionDataSourceSettings::CloudStorage::AvroFormat](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-IngestionDataSourceSettings-CloudStorage-AvroFormat)) — Optional. Data from Cloud Storage will be interpreted in Avro format.

Note: The following fields are mutually exclusive: `avro_format`, `text_format`, `pubsub_avro_format`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #avro_format=
    
    
    def avro_format=(value) -> ::Google::Cloud::PubSub::V1::IngestionDataSourceSettings::CloudStorage::AvroFormat

**Parameter**

  * **value** ([::Google::Cloud::PubSub::V1::IngestionDataSourceSettings::CloudStorage::AvroFormat](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-IngestionDataSourceSettings-CloudStorage-AvroFormat)) — Optional. Data from Cloud Storage will be interpreted in Avro format.

Note: The following fields are mutually exclusive: `avro_format`, `text_format`, `pubsub_avro_format`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::PubSub::V1::IngestionDataSourceSettings::CloudStorage::AvroFormat](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-IngestionDataSourceSettings-CloudStorage-AvroFormat)) — Optional. Data from Cloud Storage will be interpreted in Avro format.

Note: The following fields are mutually exclusive: `avro_format`, `text_format`, `pubsub_avro_format`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #bucket
    
    
    def bucket() -> ::String

**Returns**

  * (::String) — Optional. Cloud Storage bucket. The bucket name must be without any prefix like "gs://". See the [bucket naming requirements](https://cloud.google.com/storage/docs/buckets#naming). 



### #bucket=
    
    
    def bucket=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Cloud Storage bucket. The bucket name must be without any prefix like "gs://". See the [bucket naming requirements](https://cloud.google.com/storage/docs/buckets#naming). 



**Returns**

  * (::String) — Optional. Cloud Storage bucket. The bucket name must be without any prefix like "gs://". See the [bucket naming requirements](https://cloud.google.com/storage/docs/buckets#naming). 



### #match_glob
    
    
    def match_glob() -> ::String

**Returns**

  * (::String) — Optional. Glob pattern used to match objects that will be ingested. If unset, all objects will be ingested. See the [supported patterns](https://cloud.google.com/storage/docs/json_api/v1/objects/list#list-objects-and-prefixes-using-glob). 



### #match_glob=
    
    
    def match_glob=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Glob pattern used to match objects that will be ingested. If unset, all objects will be ingested. See the [supported patterns](https://cloud.google.com/storage/docs/json_api/v1/objects/list#list-objects-and-prefixes-using-glob). 



**Returns**

  * (::String) — Optional. Glob pattern used to match objects that will be ingested. If unset, all objects will be ingested. See the [supported patterns](https://cloud.google.com/storage/docs/json_api/v1/objects/list#list-objects-and-prefixes-using-glob). 



### #minimum_object_create_time
    
    
    def minimum_object_create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Protobuf-Timestamp)) — Optional. Only objects with a larger or equal creation timestamp will be ingested. 



### #minimum_object_create_time=
    
    
    def minimum_object_create_time=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Protobuf-Timestamp)) — Optional. Only objects with a larger or equal creation timestamp will be ingested. 



**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Protobuf-Timestamp)) — Optional. Only objects with a larger or equal creation timestamp will be ingested. 



### #pubsub_avro_format
    
    
    def pubsub_avro_format() -> ::Google::Cloud::PubSub::V1::IngestionDataSourceSettings::CloudStorage::PubSubAvroFormat

**Returns**

  * ([::Google::Cloud::PubSub::V1::IngestionDataSourceSettings::CloudStorage::PubSubAvroFormat](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-IngestionDataSourceSettings-CloudStorage-PubSubAvroFormat)) — Optional. It will be assumed data from Cloud Storage was written via [Cloud Storage subscriptions](https://cloud.google.com/pubsub/docs/cloudstorage).

Note: The following fields are mutually exclusive: `pubsub_avro_format`, `text_format`, `avro_format`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #pubsub_avro_format=
    
    
    def pubsub_avro_format=(value) -> ::Google::Cloud::PubSub::V1::IngestionDataSourceSettings::CloudStorage::PubSubAvroFormat

**Parameter**

  * **value** ([::Google::Cloud::PubSub::V1::IngestionDataSourceSettings::CloudStorage::PubSubAvroFormat](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-IngestionDataSourceSettings-CloudStorage-PubSubAvroFormat)) — Optional. It will be assumed data from Cloud Storage was written via [Cloud Storage subscriptions](https://cloud.google.com/pubsub/docs/cloudstorage).

Note: The following fields are mutually exclusive: `pubsub_avro_format`, `text_format`, `avro_format`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::PubSub::V1::IngestionDataSourceSettings::CloudStorage::PubSubAvroFormat](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-IngestionDataSourceSettings-CloudStorage-PubSubAvroFormat)) — Optional. It will be assumed data from Cloud Storage was written via [Cloud Storage subscriptions](https://cloud.google.com/pubsub/docs/cloudstorage).

Note: The following fields are mutually exclusive: `pubsub_avro_format`, `text_format`, `avro_format`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #state
    
    
    def state() -> ::Google::Cloud::PubSub::V1::IngestionDataSourceSettings::CloudStorage::State

**Returns**

  * ([::Google::Cloud::PubSub::V1::IngestionDataSourceSettings::CloudStorage::State](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-IngestionDataSourceSettings-CloudStorage-State)) — Output only. An output-only field that indicates the state of the Cloud Storage ingestion source. 



### #text_format
    
    
    def text_format() -> ::Google::Cloud::PubSub::V1::IngestionDataSourceSettings::CloudStorage::TextFormat

**Returns**

  * ([::Google::Cloud::PubSub::V1::IngestionDataSourceSettings::CloudStorage::TextFormat](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-IngestionDataSourceSettings-CloudStorage-TextFormat)) — Optional. Data from Cloud Storage will be interpreted as text.

Note: The following fields are mutually exclusive: `text_format`, `avro_format`, `pubsub_avro_format`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #text_format=
    
    
    def text_format=(value) -> ::Google::Cloud::PubSub::V1::IngestionDataSourceSettings::CloudStorage::TextFormat

**Parameter**

  * **value** ([::Google::Cloud::PubSub::V1::IngestionDataSourceSettings::CloudStorage::TextFormat](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-IngestionDataSourceSettings-CloudStorage-TextFormat)) — Optional. Data from Cloud Storage will be interpreted as text.

Note: The following fields are mutually exclusive: `text_format`, `avro_format`, `pubsub_avro_format`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::PubSub::V1::IngestionDataSourceSettings::CloudStorage::TextFormat](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-IngestionDataSourceSettings-CloudStorage-TextFormat)) — Optional. Data from Cloud Storage will be interpreted as text.

Note: The following fields are mutually exclusive: `text_format`, `avro_format`, `pubsub_avro_format`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
