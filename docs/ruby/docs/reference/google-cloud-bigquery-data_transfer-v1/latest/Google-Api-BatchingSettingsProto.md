---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-data_transfer-v1/latest/Google-Api-BatchingSettingsProto/
title: BigQuery Data Transfer Service V1 API - Class Google::Api::BatchingSettingsProto (v1.7.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:44:31.856389+00:00
---

# BigQuery Data Transfer Service V1 API - Class Google::Api::BatchingSettingsProto (v1.7.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-data_transfer-v1/latest/Google-Api-BatchingSettingsProto/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  BigQuery Data Transfer Service V1 API - Class Google::Api::BatchingSettingsProto (v1.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.7.1 (latest)  1.7.0  1.6.0  1.5.1  1.4.1  1.3.1  1.2.0  1.1.0  1.0.3  0.14.2  0.13.1  0.12.2  0.11.0  0.10.0  0.9.0  0.8.0  0.7.1  0.6.1  0.5.1  0.4.6 

Reference documentation and code samples for the BigQuery Data Transfer Service V1 API class Google::Api::BatchingSettingsProto.

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

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-data_transfer-v1/latest/Google-Protobuf-Duration)) — The duration after which a batch should be sent, starting from the addition of the first message to that batch. 



### #delay_threshold=
    
    
    def delay_threshold=(value) -> ::Google::Protobuf::Duration

**Parameter**

  * **value** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-data_transfer-v1/latest/Google-Protobuf-Duration)) — The duration after which a batch should be sent, starting from the addition of the first message to that batch. 



**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-data_transfer-v1/latest/Google-Protobuf-Duration)) — The duration after which a batch should be sent, starting from the addition of the first message to that batch. 



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

  * ([::Google::Api::FlowControlLimitExceededBehaviorProto](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-data_transfer-v1/latest/Google-Api-FlowControlLimitExceededBehaviorProto)) — The behavior to take when the flow control limit is exceeded. 



### #flow_control_limit_exceeded_behavior=
    
    
    def flow_control_limit_exceeded_behavior=(value) -> ::Google::Api::FlowControlLimitExceededBehaviorProto

**Parameter**

  * **value** ([::Google::Api::FlowControlLimitExceededBehaviorProto](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-data_transfer-v1/latest/Google-Api-FlowControlLimitExceededBehaviorProto)) — The behavior to take when the flow control limit is exceeded. 



**Returns**

  * ([::Google::Api::FlowControlLimitExceededBehaviorProto](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-data_transfer-v1/latest/Google-Api-FlowControlLimitExceededBehaviorProto)) — The behavior to take when the flow control limit is exceeded. 



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
