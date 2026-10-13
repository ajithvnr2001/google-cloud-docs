---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-BeginTransactionRequest/
title: Cloud Spanner V1 API - Class Google::Cloud::Spanner::V1::BeginTransactionRequest (v1.19.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:48:28.004408+00:00
---

# Cloud Spanner V1 API - Class Google::Cloud::Spanner::V1::BeginTransactionRequest (v1.19.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-BeginTransactionRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Spanner V1 API - Class Google::Cloud::Spanner::V1::BeginTransactionRequest (v1.19.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.19.2 (latest)  1.19.1  1.18.0  1.17.1  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.1  1.10.1  1.9.1  1.8.0  1.7.1  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.2  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.2  0.21.0  0.20.1  0.19.0  0.18.0  0.17.0  0.16.0  0.15.1  0.14.1  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.1  0.7.4 

Reference documentation and code samples for the Cloud Spanner V1 API class Google::Cloud::Spanner::V1::BeginTransactionRequest.

The request for [BeginTransaction](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-Spanner-Client#Google__Cloud__Spanner__V1__Spanner__Client_begin_transaction_instance_ "Google::Cloud::Spanner::V1::Spanner::Client#begin_transaction \(method\)").

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #mutation_key
    
    
    def mutation_key() -> ::Google::Cloud::Spanner::V1::Mutation

**Returns**

  * ([::Google::Cloud::Spanner::V1::Mutation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-Mutation)) — Optional. Required for read-write transactions on a multiplexed session that commit mutations but don't perform any reads or queries. You must randomly select one of the mutations from the mutation set and send it as a part of this request. 



### #mutation_key=
    
    
    def mutation_key=(value) -> ::Google::Cloud::Spanner::V1::Mutation

**Parameter**

  * **value** ([::Google::Cloud::Spanner::V1::Mutation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-Mutation)) — Optional. Required for read-write transactions on a multiplexed session that commit mutations but don't perform any reads or queries. You must randomly select one of the mutations from the mutation set and send it as a part of this request. 



**Returns**

  * ([::Google::Cloud::Spanner::V1::Mutation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-Mutation)) — Optional. Required for read-write transactions on a multiplexed session that commit mutations but don't perform any reads or queries. You must randomly select one of the mutations from the mutation set and send it as a part of this request. 



### #options
    
    
    def options() -> ::Google::Cloud::Spanner::V1::TransactionOptions

**Returns**

  * ([::Google::Cloud::Spanner::V1::TransactionOptions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-TransactionOptions)) — Required. Options for the new transaction. 



### #options=
    
    
    def options=(value) -> ::Google::Cloud::Spanner::V1::TransactionOptions

**Parameter**

  * **value** ([::Google::Cloud::Spanner::V1::TransactionOptions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-TransactionOptions)) — Required. Options for the new transaction. 



**Returns**

  * ([::Google::Cloud::Spanner::V1::TransactionOptions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-TransactionOptions)) — Required. Options for the new transaction. 



### #request_options
    
    
    def request_options() -> ::Google::Cloud::Spanner::V1::RequestOptions

**Returns**

  * ([::Google::Cloud::Spanner::V1::RequestOptions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-RequestOptions)) — Common options for this request. Priority is ignored for this request. Setting the priority in this `request_options` struct doesn't do anything. To set the priority for a transaction, set it on the reads and writes that are part of this transaction instead. 



### #request_options=
    
    
    def request_options=(value) -> ::Google::Cloud::Spanner::V1::RequestOptions

**Parameter**

  * **value** ([::Google::Cloud::Spanner::V1::RequestOptions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-RequestOptions)) — Common options for this request. Priority is ignored for this request. Setting the priority in this `request_options` struct doesn't do anything. To set the priority for a transaction, set it on the reads and writes that are part of this transaction instead. 



**Returns**

  * ([::Google::Cloud::Spanner::V1::RequestOptions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-RequestOptions)) — Common options for this request. Priority is ignored for this request. Setting the priority in this `request_options` struct doesn't do anything. To set the priority for a transaction, set it on the reads and writes that are part of this transaction instead. 



### #routing_hint
    
    
    def routing_hint() -> ::Google::Cloud::Spanner::V1::RoutingHint

**Returns**

  * ([::Google::Cloud::Spanner::V1::RoutingHint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-RoutingHint)) — Optional. Makes the Spanner requests location-aware if present.

It gives the server hints that can be used to route the request to an appropriate server, potentially significantly decreasing latency and improving throughput. To achieve improved performance, most fields must be filled in with accurate values. 




### #routing_hint=
    
    
    def routing_hint=(value) -> ::Google::Cloud::Spanner::V1::RoutingHint

**Parameter**

  * **value** ([::Google::Cloud::Spanner::V1::RoutingHint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-RoutingHint)) — Optional. Makes the Spanner requests location-aware if present.

It gives the server hints that can be used to route the request to an appropriate server, potentially significantly decreasing latency and improving throughput. To achieve improved performance, most fields must be filled in with accurate values. 




**Returns**

  * ([::Google::Cloud::Spanner::V1::RoutingHint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-RoutingHint)) — Optional. Makes the Spanner requests location-aware if present.

It gives the server hints that can be used to route the request to an appropriate server, potentially significantly decreasing latency and improving throughput. To achieve improved performance, most fields must be filled in with accurate values. 




### #session
    
    
    def session() -> ::String

**Returns**

  * (::String) — Required. The session in which the transaction runs. 



### #session=
    
    
    def session=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The session in which the transaction runs. 



**Returns**

  * (::String) — Required. The session in which the transaction runs. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
