---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Api-BatchingSettingsProto/
title: Vertex AI V1 API - Class Google::Api::BatchingSettingsProto (v1.49.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:07:19.834900+00:00
---

# Vertex AI V1 API - Class Google::Api::BatchingSettingsProto (v1.49.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Api-BatchingSettingsProto/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Vertex AI V1 API - Class Google::Api::BatchingSettingsProto (v1.49.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.49.0 (latest)  1.48.0  1.47.1  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.1  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.1  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.64.0  0.63.0  0.62.0  0.61.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.1  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Vertex AI V1 API class Google::Api::BatchingSettingsProto.

`BatchingSettingsProto` specifies a set of batching thresholds, each of which acts as a trigger to send a batch of messages as a request. At least one threshold must be positive nonzero.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #delay_threshold
    
    
    def delay_threshold() -> ::Google::Protobuf::Duration

**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Protobuf-Duration)) — The duration after which a batch should be sent, starting from the addition of the first message to that batch. 



### #delay_threshold=
    
    
    def delay_threshold=(value) -> ::Google::Protobuf::Duration

**Parameter**

  * **value** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Protobuf-Duration)) — The duration after which a batch should be sent, starting from the addition of the first message to that batch. 



**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Protobuf-Duration)) — The duration after which a batch should be sent, starting from the addition of the first message to that batch. 



### #element_count_limit
    
    
    def element_count_limit() -> ::Integer

**Returns**

  * (::Integer) — The maximum number of elements collected in a batch that could be accepted by server. 



### #element_count_limit=
    
    
    def element_count_limit=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The maximum number of elements collected in a batch that could be accepted by server. 



**Returns**

  * (::Integer) — The maximum number of elements collected in a batch that could be accepted by server. 



### #element_count_threshold
    
    
    def element_count_threshold() -> ::Integer

**Returns**

  * (::Integer) — The number of elements of a field collected into a batch which, if exceeded, causes the batch to be sent. 



### #element_count_threshold=
    
    
    def element_count_threshold=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The number of elements of a field collected into a batch which, if exceeded, causes the batch to be sent. 



**Returns**

  * (::Integer) — The number of elements of a field collected into a batch which, if exceeded, causes the batch to be sent. 



### #flow_control_byte_limit
    
    
    def flow_control_byte_limit() -> ::Integer

**Returns**

  * (::Integer) — The maximum size of data allowed by flow control. 



### #flow_control_byte_limit=
    
    
    def flow_control_byte_limit=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The maximum size of data allowed by flow control. 



**Returns**

  * (::Integer) — The maximum size of data allowed by flow control. 



### #flow_control_element_limit
    
    
    def flow_control_element_limit() -> ::Integer

**Returns**

  * (::Integer) — The maximum number of elements allowed by flow control. 



### #flow_control_element_limit=
    
    
    def flow_control_element_limit=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The maximum number of elements allowed by flow control. 



**Returns**

  * (::Integer) — The maximum number of elements allowed by flow control. 



### #flow_control_limit_exceeded_behavior
    
    
    def flow_control_limit_exceeded_behavior() -> ::Google::Api::FlowControlLimitExceededBehaviorProto

**Returns**

  * ([::Google::Api::FlowControlLimitExceededBehaviorProto](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Api-FlowControlLimitExceededBehaviorProto)) — The behavior to take when the flow control limit is exceeded. 



### #flow_control_limit_exceeded_behavior=
    
    
    def flow_control_limit_exceeded_behavior=(value) -> ::Google::Api::FlowControlLimitExceededBehaviorProto

**Parameter**

  * **value** ([::Google::Api::FlowControlLimitExceededBehaviorProto](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Api-FlowControlLimitExceededBehaviorProto)) — The behavior to take when the flow control limit is exceeded. 



**Returns**

  * ([::Google::Api::FlowControlLimitExceededBehaviorProto](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Api-FlowControlLimitExceededBehaviorProto)) — The behavior to take when the flow control limit is exceeded. 



### #request_byte_limit
    
    
    def request_byte_limit() -> ::Integer

**Returns**

  * (::Integer) — The maximum size of the request that could be accepted by server. 



### #request_byte_limit=
    
    
    def request_byte_limit=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The maximum size of the request that could be accepted by server. 



**Returns**

  * (::Integer) — The maximum size of the request that could be accepted by server. 



### #request_byte_threshold
    
    
    def request_byte_threshold() -> ::Integer

**Returns**

  * (::Integer) — The aggregated size of the batched field which, if exceeded, causes the batch to be sent. This size is computed by aggregating the sizes of the request field to be batched, not of the entire request message. 



### #request_byte_threshold=
    
    
    def request_byte_threshold=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The aggregated size of the batched field which, if exceeded, causes the batch to be sent. This size is computed by aggregating the sizes of the request field to be batched, not of the entire request message. 



**Returns**

  * (::Integer) — The aggregated size of the batched field which, if exceeded, causes the batch to be sent. This size is computed by aggregating the sizes of the request field to be batched, not of the entire request message. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
