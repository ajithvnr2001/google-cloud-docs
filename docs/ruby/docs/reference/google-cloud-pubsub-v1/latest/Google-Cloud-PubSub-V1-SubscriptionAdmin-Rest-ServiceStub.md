---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-SubscriptionAdmin-Rest-ServiceStub/
title: Cloud Pub/Sub V1 API - Class Google::Cloud::PubSub::V1::SubscriptionAdmin::Rest::ServiceStub (v1.18.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:13:27.515821+00:00
---

# Cloud Pub/Sub V1 API - Class Google::Cloud::PubSub::V1::SubscriptionAdmin::Rest::ServiceStub (v1.18.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-SubscriptionAdmin-Rest-ServiceStub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Pub/Sub V1 API - Class Google::Cloud::PubSub::V1::SubscriptionAdmin::Rest::ServiceStub (v1.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.18.0 (latest)  1.17.0  1.16.0  1.15.0  1.14.2  1.13.0  1.12.0  1.11.1  1.10.0  1.9.0  1.8.2  1.7.1  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.2  1.0.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.2  0.20.2  0.19.0  0.18.1  0.17.4  0.16.0  0.15.1  0.14.0  0.13.1  0.12.1  0.11.0  0.10.0  0.9.0  0.8.0  0.7.1  0.6.2 

Reference documentation and code samples for the Cloud Pub/Sub V1 API class Google::Cloud::PubSub::V1::SubscriptionAdmin::Rest::ServiceStub.

REST service stub for the SubscriptionAdmin service. Service stub contains baseline method implementations including transcoding, making the REST call, and deserialing the response.

## Inherits

  * Object 



## Methods 

### #acknowledge
    
    
    def acknowledge(request_pb, options = nil) { |result, operation| ... } -> ::Google::Protobuf::Empty

Baseline implementation for the acknowledge REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::PubSub::V1::AcknowledgeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-AcknowledgeRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Protobuf-Empty)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Protobuf-Empty)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #create_snapshot
    
    
    def create_snapshot(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::PubSub::V1::Snapshot

Baseline implementation for the create_snapshot REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::PubSub::V1::CreateSnapshotRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-CreateSnapshotRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::PubSub::V1::Snapshot](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-Snapshot)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::PubSub::V1::Snapshot](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-Snapshot)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #create_subscription
    
    
    def create_subscription(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::PubSub::V1::Subscription

Baseline implementation for the create_subscription REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::PubSub::V1::Subscription](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-Subscription)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::PubSub::V1::Subscription](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-Subscription)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::PubSub::V1::Subscription](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-Subscription)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_snapshot
    
    
    def delete_snapshot(request_pb, options = nil) { |result, operation| ... } -> ::Google::Protobuf::Empty

Baseline implementation for the delete_snapshot REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::PubSub::V1::DeleteSnapshotRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-DeleteSnapshotRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Protobuf-Empty)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Protobuf-Empty)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_subscription
    
    
    def delete_subscription(request_pb, options = nil) { |result, operation| ... } -> ::Google::Protobuf::Empty

Baseline implementation for the delete_subscription REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::PubSub::V1::DeleteSubscriptionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-DeleteSubscriptionRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Protobuf-Empty)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Protobuf-Empty)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #endpoint
    
    
    def endpoint() -> String

The effective endpoint

**Returns**

  * (String) 



### #get_snapshot
    
    
    def get_snapshot(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::PubSub::V1::Snapshot

Baseline implementation for the get_snapshot REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::PubSub::V1::GetSnapshotRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-GetSnapshotRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::PubSub::V1::Snapshot](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-Snapshot)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::PubSub::V1::Snapshot](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-Snapshot)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_subscription
    
    
    def get_subscription(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::PubSub::V1::Subscription

Baseline implementation for the get_subscription REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::PubSub::V1::GetSubscriptionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-GetSubscriptionRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::PubSub::V1::Subscription](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-Subscription)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::PubSub::V1::Subscription](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-Subscription)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_snapshots
    
    
    def list_snapshots(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::PubSub::V1::ListSnapshotsResponse

Baseline implementation for the list_snapshots REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::PubSub::V1::ListSnapshotsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-ListSnapshotsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::PubSub::V1::ListSnapshotsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-ListSnapshotsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::PubSub::V1::ListSnapshotsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-ListSnapshotsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_subscriptions
    
    
    def list_subscriptions(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::PubSub::V1::ListSubscriptionsResponse

Baseline implementation for the list_subscriptions REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::PubSub::V1::ListSubscriptionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-ListSubscriptionsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::PubSub::V1::ListSubscriptionsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-ListSubscriptionsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::PubSub::V1::ListSubscriptionsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-ListSubscriptionsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #logger
    
    
    def logger(stub: false) -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #modify_ack_deadline
    
    
    def modify_ack_deadline(request_pb, options = nil) { |result, operation| ... } -> ::Google::Protobuf::Empty

Baseline implementation for the modify_ack_deadline REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::PubSub::V1::ModifyAckDeadlineRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-ModifyAckDeadlineRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Protobuf-Empty)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Protobuf-Empty)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #modify_push_config
    
    
    def modify_push_config(request_pb, options = nil) { |result, operation| ... } -> ::Google::Protobuf::Empty

Baseline implementation for the modify_push_config REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::PubSub::V1::ModifyPushConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-ModifyPushConfigRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Protobuf-Empty)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Protobuf-Empty)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #pull
    
    
    def pull(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::PubSub::V1::PullResponse

Baseline implementation for the pull REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::PubSub::V1::PullRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-PullRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::PubSub::V1::PullResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-PullResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::PubSub::V1::PullResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-PullResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #seek
    
    
    def seek(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::PubSub::V1::SeekResponse

Baseline implementation for the seek REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::PubSub::V1::SeekRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-SeekRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::PubSub::V1::SeekResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-SeekResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::PubSub::V1::SeekResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-SeekResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #update_snapshot
    
    
    def update_snapshot(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::PubSub::V1::Snapshot

Baseline implementation for the update_snapshot REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::PubSub::V1::UpdateSnapshotRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-UpdateSnapshotRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::PubSub::V1::Snapshot](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-Snapshot)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::PubSub::V1::Snapshot](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-Snapshot)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #update_subscription
    
    
    def update_subscription(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::PubSub::V1::Subscription

Baseline implementation for the update_subscription REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::PubSub::V1::UpdateSubscriptionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-UpdateSubscriptionRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::PubSub::V1::Subscription](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-Subscription)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::PubSub::V1::Subscription](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-Subscription)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
