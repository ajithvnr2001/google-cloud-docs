---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-StreamingPullResponse/
title: Cloud Pub/Sub V1 API - Class Google::Cloud::PubSub::V1::StreamingPullResponse (v1.18.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:57:19.486232+00:00
---

# Cloud Pub/Sub V1 API - Class Google::Cloud::PubSub::V1::StreamingPullResponse (v1.18.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-StreamingPullResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Pub/Sub V1 API - Class Google::Cloud::PubSub::V1::StreamingPullResponse (v1.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.18.0 (latest)  1.17.0  1.16.0  1.15.0  1.14.2  1.13.0  1.12.0  1.11.1  1.10.0  1.9.0  1.8.2  1.7.1  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.2  1.0.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.2  0.20.2  0.19.0  0.18.1  0.17.4  0.16.0  0.15.1  0.14.0  0.13.1  0.12.1  0.11.0  0.10.0  0.9.0  0.8.0  0.7.1  0.6.2 

Reference documentation and code samples for the Cloud Pub/Sub V1 API class Google::Cloud::PubSub::V1::StreamingPullResponse.

Response for the `StreamingPull` method. This response is used to stream messages from the server to the client.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #acknowledge_confirmation
    
    
    def acknowledge_confirmation() -> ::Google::Cloud::PubSub::V1::StreamingPullResponse::AcknowledgeConfirmation

**Returns**

  * ([::Google::Cloud::PubSub::V1::StreamingPullResponse::AcknowledgeConfirmation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-StreamingPullResponse-AcknowledgeConfirmation)) — Optional. This field will only be set if `enable_exactly_once_delivery` is set to `true` and is not guaranteed to be populated. 



### #acknowledge_confirmation=
    
    
    def acknowledge_confirmation=(value) -> ::Google::Cloud::PubSub::V1::StreamingPullResponse::AcknowledgeConfirmation

**Parameter**

  * **value** ([::Google::Cloud::PubSub::V1::StreamingPullResponse::AcknowledgeConfirmation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-StreamingPullResponse-AcknowledgeConfirmation)) — Optional. This field will only be set if `enable_exactly_once_delivery` is set to `true` and is not guaranteed to be populated. 



**Returns**

  * ([::Google::Cloud::PubSub::V1::StreamingPullResponse::AcknowledgeConfirmation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-StreamingPullResponse-AcknowledgeConfirmation)) — Optional. This field will only be set if `enable_exactly_once_delivery` is set to `true` and is not guaranteed to be populated. 



### #modify_ack_deadline_confirmation
    
    
    def modify_ack_deadline_confirmation() -> ::Google::Cloud::PubSub::V1::StreamingPullResponse::ModifyAckDeadlineConfirmation

**Returns**

  * ([::Google::Cloud::PubSub::V1::StreamingPullResponse::ModifyAckDeadlineConfirmation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-StreamingPullResponse-ModifyAckDeadlineConfirmation)) — Optional. This field will only be set if `enable_exactly_once_delivery` is set to `true` and is not guaranteed to be populated. 



### #modify_ack_deadline_confirmation=
    
    
    def modify_ack_deadline_confirmation=(value) -> ::Google::Cloud::PubSub::V1::StreamingPullResponse::ModifyAckDeadlineConfirmation

**Parameter**

  * **value** ([::Google::Cloud::PubSub::V1::StreamingPullResponse::ModifyAckDeadlineConfirmation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-StreamingPullResponse-ModifyAckDeadlineConfirmation)) — Optional. This field will only be set if `enable_exactly_once_delivery` is set to `true` and is not guaranteed to be populated. 



**Returns**

  * ([::Google::Cloud::PubSub::V1::StreamingPullResponse::ModifyAckDeadlineConfirmation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-StreamingPullResponse-ModifyAckDeadlineConfirmation)) — Optional. This field will only be set if `enable_exactly_once_delivery` is set to `true` and is not guaranteed to be populated. 



### #received_messages
    
    
    def received_messages() -> ::Array<::Google::Cloud::PubSub::V1::ReceivedMessage>

**Returns**

  * (::Array<[::Google::Cloud::PubSub::V1::ReceivedMessage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-ReceivedMessage)>) — Optional. Received Pub/Sub messages. 



### #received_messages=
    
    
    def received_messages=(value) -> ::Array<::Google::Cloud::PubSub::V1::ReceivedMessage>

**Parameter**

  * **value** (::Array<[::Google::Cloud::PubSub::V1::ReceivedMessage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-ReceivedMessage)>) — Optional. Received Pub/Sub messages. 



**Returns**

  * (::Array<[::Google::Cloud::PubSub::V1::ReceivedMessage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-ReceivedMessage)>) — Optional. Received Pub/Sub messages. 



### #subscription_properties
    
    
    def subscription_properties() -> ::Google::Cloud::PubSub::V1::StreamingPullResponse::SubscriptionProperties

**Returns**

  * ([::Google::Cloud::PubSub::V1::StreamingPullResponse::SubscriptionProperties](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-StreamingPullResponse-SubscriptionProperties)) — Optional. Properties associated with this subscription. 



### #subscription_properties=
    
    
    def subscription_properties=(value) -> ::Google::Cloud::PubSub::V1::StreamingPullResponse::SubscriptionProperties

**Parameter**

  * **value** ([::Google::Cloud::PubSub::V1::StreamingPullResponse::SubscriptionProperties](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-StreamingPullResponse-SubscriptionProperties)) — Optional. Properties associated with this subscription. 



**Returns**

  * ([::Google::Cloud::PubSub::V1::StreamingPullResponse::SubscriptionProperties](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-StreamingPullResponse-SubscriptionProperties)) — Optional. Properties associated with this subscription. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
