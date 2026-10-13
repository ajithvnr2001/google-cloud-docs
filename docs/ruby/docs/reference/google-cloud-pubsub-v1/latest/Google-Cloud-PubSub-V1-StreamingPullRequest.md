---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-StreamingPullRequest/
title: Cloud Pub/Sub V1 API - Class Google::Cloud::PubSub::V1::StreamingPullRequest (v1.18.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:02:13.983312+00:00
---

# Cloud Pub/Sub V1 API - Class Google::Cloud::PubSub::V1::StreamingPullRequest (v1.18.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-StreamingPullRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Pub/Sub V1 API - Class Google::Cloud::PubSub::V1::StreamingPullRequest (v1.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.18.0 (latest)  1.17.0  1.16.0  1.15.0  1.14.2  1.13.0  1.12.0  1.11.1  1.10.0  1.9.0  1.8.2  1.7.1  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.2  1.0.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.2  0.20.2  0.19.0  0.18.1  0.17.4  0.16.0  0.15.1  0.14.0  0.13.1  0.12.1  0.11.0  0.10.0  0.9.0  0.8.0  0.7.1  0.6.2 

Reference documentation and code samples for the Cloud Pub/Sub V1 API class Google::Cloud::PubSub::V1::StreamingPullRequest.

Request for the `StreamingPull` streaming RPC method. This request is used to establish the initial stream as well as to stream acknowledgments and ack deadline modifications from the client to the server.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #ack_ids
    
    
    def ack_ids() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Optional. List of acknowledgment IDs for acknowledging previously received messages (received on this stream or a different stream). If an ack ID has expired, the corresponding message may be redelivered later. Acknowledging a message more than once will not result in an error. If the acknowledgment ID is malformed, the stream will be aborted with status `INVALID_ARGUMENT`. 



### #ack_ids=
    
    
    def ack_ids=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Optional. List of acknowledgment IDs for acknowledging previously received messages (received on this stream or a different stream). If an ack ID has expired, the corresponding message may be redelivered later. Acknowledging a message more than once will not result in an error. If the acknowledgment ID is malformed, the stream will be aborted with status `INVALID_ARGUMENT`. 



**Returns**

  * (::Array<::String>) — Optional. List of acknowledgment IDs for acknowledging previously received messages (received on this stream or a different stream). If an ack ID has expired, the corresponding message may be redelivered later. Acknowledging a message more than once will not result in an error. If the acknowledgment ID is malformed, the stream will be aborted with status `INVALID_ARGUMENT`. 



### #client_id
    
    
    def client_id() -> ::String

**Returns**

  * (::String) — Optional. A unique identifier that is used to distinguish client instances from each other. Only needs to be provided on the initial request. When a stream disconnects and reconnects for the same stream, the client_id should be set to the same value so that state associated with the old stream can be transferred to the new stream. The same client_id should not be used for different client instances. 



### #client_id=
    
    
    def client_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. A unique identifier that is used to distinguish client instances from each other. Only needs to be provided on the initial request. When a stream disconnects and reconnects for the same stream, the client_id should be set to the same value so that state associated with the old stream can be transferred to the new stream. The same client_id should not be used for different client instances. 



**Returns**

  * (::String) — Optional. A unique identifier that is used to distinguish client instances from each other. Only needs to be provided on the initial request. When a stream disconnects and reconnects for the same stream, the client_id should be set to the same value so that state associated with the old stream can be transferred to the new stream. The same client_id should not be used for different client instances. 



### #max_outstanding_bytes
    
    
    def max_outstanding_bytes() -> ::Integer

**Returns**

  * (::Integer) — Optional. Flow control settings for the maximum number of outstanding bytes. When there are `max_outstanding_bytes` or more worth of messages currently sent to the streaming pull client that have not yet been acked or nacked, the server will stop sending more messages. The sending of messages resumes once the number of outstanding bytes is less than this value. If the value is <= 0, there is no limit to the number of outstanding bytes. This property can only be set on the initial StreamingPullRequest. If it is set on a subsequent request, the stream will be aborted with status `INVALID_ARGUMENT`. 



### #max_outstanding_bytes=
    
    
    def max_outstanding_bytes=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. Flow control settings for the maximum number of outstanding bytes. When there are `max_outstanding_bytes` or more worth of messages currently sent to the streaming pull client that have not yet been acked or nacked, the server will stop sending more messages. The sending of messages resumes once the number of outstanding bytes is less than this value. If the value is <= 0, there is no limit to the number of outstanding bytes. This property can only be set on the initial StreamingPullRequest. If it is set on a subsequent request, the stream will be aborted with status `INVALID_ARGUMENT`. 



**Returns**

  * (::Integer) — Optional. Flow control settings for the maximum number of outstanding bytes. When there are `max_outstanding_bytes` or more worth of messages currently sent to the streaming pull client that have not yet been acked or nacked, the server will stop sending more messages. The sending of messages resumes once the number of outstanding bytes is less than this value. If the value is <= 0, there is no limit to the number of outstanding bytes. This property can only be set on the initial StreamingPullRequest. If it is set on a subsequent request, the stream will be aborted with status `INVALID_ARGUMENT`. 



### #max_outstanding_messages
    
    
    def max_outstanding_messages() -> ::Integer

**Returns**

  * (::Integer) — Optional. Flow control settings for the maximum number of outstanding messages. When there are `max_outstanding_messages` currently sent to the streaming pull client that have not yet been acked or nacked, the server stops sending more messages. The sending of messages resumes once the number of outstanding messages is less than this value. If the value is <= 0, there is no limit to the number of outstanding messages. This property can only be set on the initial StreamingPullRequest. If it is set on a subsequent request, the stream will be aborted with status `INVALID_ARGUMENT`. 



### #max_outstanding_messages=
    
    
    def max_outstanding_messages=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. Flow control settings for the maximum number of outstanding messages. When there are `max_outstanding_messages` currently sent to the streaming pull client that have not yet been acked or nacked, the server stops sending more messages. The sending of messages resumes once the number of outstanding messages is less than this value. If the value is <= 0, there is no limit to the number of outstanding messages. This property can only be set on the initial StreamingPullRequest. If it is set on a subsequent request, the stream will be aborted with status `INVALID_ARGUMENT`. 



**Returns**

  * (::Integer) — Optional. Flow control settings for the maximum number of outstanding messages. When there are `max_outstanding_messages` currently sent to the streaming pull client that have not yet been acked or nacked, the server stops sending more messages. The sending of messages resumes once the number of outstanding messages is less than this value. If the value is <= 0, there is no limit to the number of outstanding messages. This property can only be set on the initial StreamingPullRequest. If it is set on a subsequent request, the stream will be aborted with status `INVALID_ARGUMENT`. 



### #modify_deadline_ack_ids
    
    
    def modify_deadline_ack_ids() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Optional. List of acknowledgment IDs whose deadline will be modified based on the corresponding element in `modify_deadline_seconds`. This field can be used to indicate that more time is needed to process a message by the subscriber, or to make the message available for redelivery if the processing was interrupted. 



### #modify_deadline_ack_ids=
    
    
    def modify_deadline_ack_ids=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Optional. List of acknowledgment IDs whose deadline will be modified based on the corresponding element in `modify_deadline_seconds`. This field can be used to indicate that more time is needed to process a message by the subscriber, or to make the message available for redelivery if the processing was interrupted. 



**Returns**

  * (::Array<::String>) — Optional. List of acknowledgment IDs whose deadline will be modified based on the corresponding element in `modify_deadline_seconds`. This field can be used to indicate that more time is needed to process a message by the subscriber, or to make the message available for redelivery if the processing was interrupted. 



### #modify_deadline_seconds
    
    
    def modify_deadline_seconds() -> ::Array<::Integer>

**Returns**

  * (::Array<::Integer>) — Optional. The list of new ack deadlines for the IDs listed in `modify_deadline_ack_ids`. The size of this list must be the same as the size of `modify_deadline_ack_ids`. If it differs the stream will be aborted with `INVALID_ARGUMENT`. Each element in this list is applied to the element in the same position in `modify_deadline_ack_ids`. The new ack deadline is with respect to the time this request was sent to the Pub/Sub system. Must be >= 0. For example, if the value is 10, the new ack deadline will expire 10 seconds after this request is received. If the value is 0, the message is immediately made available for another streaming or non-streaming pull request. If the value is < 0 (an error), the stream will be aborted with status `INVALID_ARGUMENT`. 



### #modify_deadline_seconds=
    
    
    def modify_deadline_seconds=(value) -> ::Array<::Integer>

**Parameter**

  * **value** (::Array<::Integer>) — Optional. The list of new ack deadlines for the IDs listed in `modify_deadline_ack_ids`. The size of this list must be the same as the size of `modify_deadline_ack_ids`. If it differs the stream will be aborted with `INVALID_ARGUMENT`. Each element in this list is applied to the element in the same position in `modify_deadline_ack_ids`. The new ack deadline is with respect to the time this request was sent to the Pub/Sub system. Must be >= 0. For example, if the value is 10, the new ack deadline will expire 10 seconds after this request is received. If the value is 0, the message is immediately made available for another streaming or non-streaming pull request. If the value is < 0 (an error), the stream will be aborted with status `INVALID_ARGUMENT`. 



**Returns**

  * (::Array<::Integer>) — Optional. The list of new ack deadlines for the IDs listed in `modify_deadline_ack_ids`. The size of this list must be the same as the size of `modify_deadline_ack_ids`. If it differs the stream will be aborted with `INVALID_ARGUMENT`. Each element in this list is applied to the element in the same position in `modify_deadline_ack_ids`. The new ack deadline is with respect to the time this request was sent to the Pub/Sub system. Must be >= 0. For example, if the value is 10, the new ack deadline will expire 10 seconds after this request is received. If the value is 0, the message is immediately made available for another streaming or non-streaming pull request. If the value is < 0 (an error), the stream will be aborted with status `INVALID_ARGUMENT`. 



### #protocol_version
    
    
    def protocol_version() -> ::Integer

**Returns**

  * (::Integer) — Optional. The protocol version used by the client. This property can only be set on the initial StreamingPullRequest. If it is set on a subsequent request, the stream will be aborted with status `INVALID_ARGUMENT`. 



### #protocol_version=
    
    
    def protocol_version=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. The protocol version used by the client. This property can only be set on the initial StreamingPullRequest. If it is set on a subsequent request, the stream will be aborted with status `INVALID_ARGUMENT`. 



**Returns**

  * (::Integer) — Optional. The protocol version used by the client. This property can only be set on the initial StreamingPullRequest. If it is set on a subsequent request, the stream will be aborted with status `INVALID_ARGUMENT`. 



### #stream_ack_deadline_seconds
    
    
    def stream_ack_deadline_seconds() -> ::Integer

**Returns**

  * (::Integer) — Required. The ack deadline to use for the stream. This must be provided in the first request on the stream, but it can also be updated on subsequent requests from client to server. The minimum deadline you can specify is 10 seconds. The maximum deadline you can specify is 600 seconds (10 minutes). 



### #stream_ack_deadline_seconds=
    
    
    def stream_ack_deadline_seconds=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Required. The ack deadline to use for the stream. This must be provided in the first request on the stream, but it can also be updated on subsequent requests from client to server. The minimum deadline you can specify is 10 seconds. The maximum deadline you can specify is 600 seconds (10 minutes). 



**Returns**

  * (::Integer) — Required. The ack deadline to use for the stream. This must be provided in the first request on the stream, but it can also be updated on subsequent requests from client to server. The minimum deadline you can specify is 10 seconds. The maximum deadline you can specify is 600 seconds (10 minutes). 



### #subscription
    
    
    def subscription() -> ::String

**Returns**

  * (::String) — Required. The subscription for which to initialize the new stream. This must be provided in the first request on the stream, and must not be set in subsequent requests from client to server. Format is `projects/{project}/subscriptions/{sub}`. 



### #subscription=
    
    
    def subscription=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The subscription for which to initialize the new stream. This must be provided in the first request on the stream, and must not be set in subsequent requests from client to server. Format is `projects/{project}/subscriptions/{sub}`. 



**Returns**

  * (::String) — Required. The subscription for which to initialize the new stream. This must be provided in the first request on the stream, and must not be set in subsequent requests from client to server. Format is `projects/{project}/subscriptions/{sub}`. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
