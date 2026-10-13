---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-ReadChangeStreamResponse-DataChange/
title: Cloud Bigtable V2 API - Class Google::Cloud::Bigtable::V2::ReadChangeStreamResponse::DataChange (v1.18.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:16:13.439816+00:00
---

# Cloud Bigtable V2 API - Class Google::Cloud::Bigtable::V2::ReadChangeStreamResponse::DataChange (v1.18.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-ReadChangeStreamResponse-DataChange/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Bigtable V2 API - Class Google::Cloud::Bigtable::V2::ReadChangeStreamResponse::DataChange (v1.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.18.0 (latest)  1.17.0  1.16.0  1.15.1  1.14.0  1.13.0  1.12.0  1.11.0  1.10.1  1.9.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.0  1.3.0  1.2.1  1.1.0  1.0.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.2  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.1  0.6.0  0.5.0  0.4.0  0.3.5 

Reference documentation and code samples for the Cloud Bigtable V2 API class Google::Cloud::Bigtable::V2::ReadChangeStreamResponse::DataChange.

A message corresponding to one or more mutations to the partition being streamed. A single logical `DataChange` message may also be split across a sequence of multiple individual messages. Messages other than the first in a sequence will only have the `type` and `chunks` fields populated, with the final message in the sequence also containing `done` set to true.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #chunks
    
    
    def chunks() -> ::Array<::Google::Cloud::Bigtable::V2::ReadChangeStreamResponse::MutationChunk>

**Returns**

  * ([::Array](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-Type-Array)<[::Google::Cloud::Bigtable::V2::ReadChangeStreamResponse::MutationChunk](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-ReadChangeStreamResponse-MutationChunk)>) — The mutations associated with this change to the partition. May contain complete mutations or chunks of a multi-message chunked `DataChange` record. 



### #chunks=
    
    
    def chunks=(value) -> ::Array<::Google::Cloud::Bigtable::V2::ReadChangeStreamResponse::MutationChunk>

**Parameter**

  * **value** ([::Array](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-Type-Array)<[::Google::Cloud::Bigtable::V2::ReadChangeStreamResponse::MutationChunk](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-ReadChangeStreamResponse-MutationChunk)>) — The mutations associated with this change to the partition. May contain complete mutations or chunks of a multi-message chunked `DataChange` record. 



**Returns**

  * ([::Array](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-Type-Array)<[::Google::Cloud::Bigtable::V2::ReadChangeStreamResponse::MutationChunk](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-ReadChangeStreamResponse-MutationChunk)>) — The mutations associated with this change to the partition. May contain complete mutations or chunks of a multi-message chunked `DataChange` record. 



### #commit_timestamp
    
    
    def commit_timestamp() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Protobuf-Timestamp)) — The timestamp at which the mutation was applied on the Bigtable server. 



### #commit_timestamp=
    
    
    def commit_timestamp=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Protobuf-Timestamp)) — The timestamp at which the mutation was applied on the Bigtable server. 



**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Protobuf-Timestamp)) — The timestamp at which the mutation was applied on the Bigtable server. 



### #done
    
    
    def done() -> ::Boolean

**Returns**

  * (::Boolean) — When true, indicates that the entire `DataChange` has been read and the client can safely process the message. 



### #done=
    
    
    def done=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — When true, indicates that the entire `DataChange` has been read and the client can safely process the message. 



**Returns**

  * (::Boolean) — When true, indicates that the entire `DataChange` has been read and the client can safely process the message. 



### #estimated_low_watermark
    
    
    def estimated_low_watermark() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Protobuf-Timestamp)) — An estimate of the commit timestamp that is usually lower than or equal to any timestamp for a record that will be delivered in the future on the stream. It is possible that, under particular circumstances that a future record has a timestamp that is lower than a previously seen timestamp. For an example usage see https://beam.apache.org/documentation/basics/#watermarks 



### #estimated_low_watermark=
    
    
    def estimated_low_watermark=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Protobuf-Timestamp)) — An estimate of the commit timestamp that is usually lower than or equal to any timestamp for a record that will be delivered in the future on the stream. It is possible that, under particular circumstances that a future record has a timestamp that is lower than a previously seen timestamp. For an example usage see https://beam.apache.org/documentation/basics/#watermarks 



**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Protobuf-Timestamp)) — An estimate of the commit timestamp that is usually lower than or equal to any timestamp for a record that will be delivered in the future on the stream. It is possible that, under particular circumstances that a future record has a timestamp that is lower than a previously seen timestamp. For an example usage see https://beam.apache.org/documentation/basics/#watermarks 



### #row_key
    
    
    def row_key() -> ::String

**Returns**

  * ([::String](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-Type-String)) — The row key for all mutations that are part of this `DataChange`. If the `DataChange` is chunked across multiple messages, then this field will only be set for the first message. 



### #row_key=
    
    
    def row_key=(value) -> ::String

**Parameter**

  * **value** ([::String](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-Type-String)) — The row key for all mutations that are part of this `DataChange`. If the `DataChange` is chunked across multiple messages, then this field will only be set for the first message. 



**Returns**

  * ([::String](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-Type-String)) — The row key for all mutations that are part of this `DataChange`. If the `DataChange` is chunked across multiple messages, then this field will only be set for the first message. 



### #source_cluster_id
    
    
    def source_cluster_id() -> ::String

**Returns**

  * ([::String](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-Type-String)) — The cluster where the mutation was applied. Not set when `type` is `GARBAGE_COLLECTION`. 



### #source_cluster_id=
    
    
    def source_cluster_id=(value) -> ::String

**Parameter**

  * **value** ([::String](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-Type-String)) — The cluster where the mutation was applied. Not set when `type` is `GARBAGE_COLLECTION`. 



**Returns**

  * ([::String](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-Type-String)) — The cluster where the mutation was applied. Not set when `type` is `GARBAGE_COLLECTION`. 



### #tiebreaker
    
    
    def tiebreaker() -> ::Integer

**Returns**

  * (::Integer) — A value that lets stream consumers reconstruct Bigtable's conflict resolution semantics. https://cloud.google.com/bigtable/docs/writes#conflict-resolution In the event that the same row key, column family, column qualifier, timestamp are modified on different clusters at the same `commit_timestamp`, the mutation with the larger `tiebreaker` will be the one chosen for the eventually consistent state of the system. 



### #tiebreaker=
    
    
    def tiebreaker=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — A value that lets stream consumers reconstruct Bigtable's conflict resolution semantics. https://cloud.google.com/bigtable/docs/writes#conflict-resolution In the event that the same row key, column family, column qualifier, timestamp are modified on different clusters at the same `commit_timestamp`, the mutation with the larger `tiebreaker` will be the one chosen for the eventually consistent state of the system. 



**Returns**

  * (::Integer) — A value that lets stream consumers reconstruct Bigtable's conflict resolution semantics. https://cloud.google.com/bigtable/docs/writes#conflict-resolution In the event that the same row key, column family, column qualifier, timestamp are modified on different clusters at the same `commit_timestamp`, the mutation with the larger `tiebreaker` will be the one chosen for the eventually consistent state of the system. 



### #token
    
    
    def token() -> ::String

**Returns**

  * ([::String](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-Type-String)) — An encoded position for this stream's partition to restart reading from. This token is for the StreamPartition from the request. 



### #token=
    
    
    def token=(value) -> ::String

**Parameter**

  * **value** ([::String](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-Type-String)) — An encoded position for this stream's partition to restart reading from. This token is for the StreamPartition from the request. 



**Returns**

  * ([::String](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-Type-String)) — An encoded position for this stream's partition to restart reading from. This token is for the StreamPartition from the request. 



### #type
    
    
    def type() -> ::Google::Cloud::Bigtable::V2::ReadChangeStreamResponse::DataChange::Type

**Returns**

  * ([::Google::Cloud::Bigtable::V2::ReadChangeStreamResponse::DataChange::Type](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-ReadChangeStreamResponse-DataChange-Type)) — The type of the mutation. 



### #type=
    
    
    def type=(value) -> ::Google::Cloud::Bigtable::V2::ReadChangeStreamResponse::DataChange::Type

**Parameter**

  * **value** ([::Google::Cloud::Bigtable::V2::ReadChangeStreamResponse::DataChange::Type](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-ReadChangeStreamResponse-DataChange-Type)) — The type of the mutation. 



**Returns**

  * ([::Google::Cloud::Bigtable::V2::ReadChangeStreamResponse::DataChange::Type](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable-v2/latest/Google-Cloud-Bigtable-V2-ReadChangeStreamResponse-DataChange-Type)) — The type of the mutation. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
