---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-Stream/
title: Datastream V1alpha1 API - Class Google::Cloud::Datastream::V1alpha1::Stream (v0.15.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:45:38.722356+00:00
---

# Datastream V1alpha1 API - Class Google::Cloud::Datastream::V1alpha1::Stream (v0.15.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-Stream/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Datastream V1alpha1 API - Class Google::Cloud::Datastream::V1alpha1::Stream (v0.15.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.15.1 (latest)  0.15.0  0.14.0  0.13.1  0.12.0  0.11.1  0.10.1  0.9.0  0.8.0  0.7.1  0.6.2  0.5.0  0.4.0  0.3.0  0.2.0  0.1.2 

Reference documentation and code samples for the Datastream V1alpha1 API class Google::Cloud::Datastream::V1alpha1::Stream.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #backfill_all
    
    
    def backfill_all() -> ::Google::Cloud::Datastream::V1alpha1::Stream::BackfillAllStrategy

**Returns**

  * ([::Google::Cloud::Datastream::V1alpha1::Stream::BackfillAllStrategy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-Stream-BackfillAllStrategy)) — Automatically backfill objects included in the stream source configuration. Specific objects can be excluded.

Note: The following fields are mutually exclusive: `backfill_all`, `backfill_none`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #backfill_all=
    
    
    def backfill_all=(value) -> ::Google::Cloud::Datastream::V1alpha1::Stream::BackfillAllStrategy

**Parameter**

  * **value** ([::Google::Cloud::Datastream::V1alpha1::Stream::BackfillAllStrategy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-Stream-BackfillAllStrategy)) — Automatically backfill objects included in the stream source configuration. Specific objects can be excluded.

Note: The following fields are mutually exclusive: `backfill_all`, `backfill_none`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Datastream::V1alpha1::Stream::BackfillAllStrategy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-Stream-BackfillAllStrategy)) — Automatically backfill objects included in the stream source configuration. Specific objects can be excluded.

Note: The following fields are mutually exclusive: `backfill_all`, `backfill_none`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #backfill_none
    
    
    def backfill_none() -> ::Google::Cloud::Datastream::V1alpha1::Stream::BackfillNoneStrategy

**Returns**

  * ([::Google::Cloud::Datastream::V1alpha1::Stream::BackfillNoneStrategy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-Stream-BackfillNoneStrategy)) — Do not automatically backfill any objects.

Note: The following fields are mutually exclusive: `backfill_none`, `backfill_all`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #backfill_none=
    
    
    def backfill_none=(value) -> ::Google::Cloud::Datastream::V1alpha1::Stream::BackfillNoneStrategy

**Parameter**

  * **value** ([::Google::Cloud::Datastream::V1alpha1::Stream::BackfillNoneStrategy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-Stream-BackfillNoneStrategy)) — Do not automatically backfill any objects.

Note: The following fields are mutually exclusive: `backfill_none`, `backfill_all`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Datastream::V1alpha1::Stream::BackfillNoneStrategy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-Stream-BackfillNoneStrategy)) — Do not automatically backfill any objects.

Note: The following fields are mutually exclusive: `backfill_none`, `backfill_all`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Protobuf-Timestamp)) — Output only. The creation time of the stream. 



### #destination_config
    
    
    def destination_config() -> ::Google::Cloud::Datastream::V1alpha1::DestinationConfig

**Returns**

  * ([::Google::Cloud::Datastream::V1alpha1::DestinationConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-DestinationConfig)) — Required. Destination connection profile configuration. 



### #destination_config=
    
    
    def destination_config=(value) -> ::Google::Cloud::Datastream::V1alpha1::DestinationConfig

**Parameter**

  * **value** ([::Google::Cloud::Datastream::V1alpha1::DestinationConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-DestinationConfig)) — Required. Destination connection profile configuration. 



**Returns**

  * ([::Google::Cloud::Datastream::V1alpha1::DestinationConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-DestinationConfig)) — Required. Destination connection profile configuration. 



### #display_name
    
    
    def display_name() -> ::String

**Returns**

  * (::String) — Required. Display name. 



### #display_name=
    
    
    def display_name=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Display name. 



**Returns**

  * (::String) — Required. Display name. 



### #errors
    
    
    def errors() -> ::Array<::Google::Cloud::Datastream::V1alpha1::Error>

**Returns**

  * (::Array<[::Google::Cloud::Datastream::V1alpha1::Error](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-Error)>) — Output only. Errors on the Stream. 



### #labels
    
    
    def labels() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Labels. 



### #labels=
    
    
    def labels=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Labels. 



**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Labels. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Output only. The stream's name. 



### #source_config
    
    
    def source_config() -> ::Google::Cloud::Datastream::V1alpha1::SourceConfig

**Returns**

  * ([::Google::Cloud::Datastream::V1alpha1::SourceConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-SourceConfig)) — Required. Source connection profile configuration. 



### #source_config=
    
    
    def source_config=(value) -> ::Google::Cloud::Datastream::V1alpha1::SourceConfig

**Parameter**

  * **value** ([::Google::Cloud::Datastream::V1alpha1::SourceConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-SourceConfig)) — Required. Source connection profile configuration. 



**Returns**

  * ([::Google::Cloud::Datastream::V1alpha1::SourceConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-SourceConfig)) — Required. Source connection profile configuration. 



### #state
    
    
    def state() -> ::Google::Cloud::Datastream::V1alpha1::Stream::State

**Returns**

  * ([::Google::Cloud::Datastream::V1alpha1::Stream::State](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-Stream-State)) — The state of the stream. 



### #state=
    
    
    def state=(value) -> ::Google::Cloud::Datastream::V1alpha1::Stream::State

**Parameter**

  * **value** ([::Google::Cloud::Datastream::V1alpha1::Stream::State](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-Stream-State)) — The state of the stream. 



**Returns**

  * ([::Google::Cloud::Datastream::V1alpha1::Stream::State](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-Stream-State)) — The state of the stream. 



### #update_time
    
    
    def update_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Protobuf-Timestamp)) — Output only. The last update time of the stream. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
