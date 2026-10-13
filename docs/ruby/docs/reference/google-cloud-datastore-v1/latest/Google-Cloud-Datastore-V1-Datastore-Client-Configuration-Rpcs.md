---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore-v1/latest/Google-Cloud-Datastore-V1-Datastore-Client-Configuration-Rpcs/
title: Firestore in Datastore mode V1 API - Class Google::Cloud::Datastore::V1::Datastore::Client::Configuration::Rpcs (v1.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:47:17.883012+00:00
---

# Firestore in Datastore mode V1 API - Class Google::Cloud::Datastore::V1::Datastore::Client::Configuration::Rpcs (v1.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastore-v1/latest/Google-Cloud-Datastore-V1-Datastore-Client-Configuration-Rpcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Firestore in Datastore mode V1 API - Class Google::Cloud::Datastore::V1::Datastore::Client::Configuration::Rpcs (v1.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.1 (latest)  1.8.0  1.7.0  1.6.0  1.5.1  1.4.1  1.3.1  1.2.0  1.1.0  1.0.1  0.19.0  0.18.0  0.17.0  0.16.3  0.15.0  0.14.0  0.13.1  0.12.0  0.11.1  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.5 

Reference documentation and code samples for the Firestore in Datastore mode V1 API class Google::Cloud::Datastore::V1::Datastore::Client::Configuration::Rpcs.

Configuration RPC class for the Datastore API.

Includes fields providing the configuration for each RPC in this service. Each configuration object is of type `Gapic::Config::Method` and includes the following configuration fields:

  * `timeout` (_type:_ `Numeric`) - The call timeout in seconds
  * `metadata` (_type:_ `Hash{Symbol=>String}`) - Additional gRPC headers
  * `retry_policy (_type:_`Hash`) - The retry policy. The policy fields include the following keys: 
    * `:initial_delay` (_type:_ `Numeric`) - The initial delay in seconds.
    * `:max_delay` (_type:_ `Numeric`) - The max delay in seconds.
    * `:multiplier` (_type:_ `Numeric`) - The incremental backoff multiplier.
    * `:jitter` (_type:_ `Numeric`) - The jitter in seconds. Default: 1.0.
    * `:retry_codes` (_type:_ `Array<String>`) - The error codes that should trigger a retry.



## Inherits

  * Object 



## Methods 

### #allocate_ids
    
    
    def allocate_ids() -> ::Gapic::Config::Method

RPC-specific configuration for `allocate_ids`

**Returns**

  * (::Gapic::Config::Method) 



### #begin_transaction
    
    
    def begin_transaction() -> ::Gapic::Config::Method

RPC-specific configuration for `begin_transaction`

**Returns**

  * (::Gapic::Config::Method) 



### #commit
    
    
    def commit() -> ::Gapic::Config::Method

RPC-specific configuration for `commit`

**Returns**

  * (::Gapic::Config::Method) 



### #lookup
    
    
    def lookup() -> ::Gapic::Config::Method

RPC-specific configuration for `lookup`

**Returns**

  * (::Gapic::Config::Method) 



### #reserve_ids
    
    
    def reserve_ids() -> ::Gapic::Config::Method

RPC-specific configuration for `reserve_ids`

**Returns**

  * (::Gapic::Config::Method) 



### #rollback
    
    
    def rollback() -> ::Gapic::Config::Method

RPC-specific configuration for `rollback`

**Returns**

  * (::Gapic::Config::Method) 



### #run_aggregation_query
    
    
    def run_aggregation_query() -> ::Gapic::Config::Method

RPC-specific configuration for `run_aggregation_query`

**Returns**

  * (::Gapic::Config::Method) 



### #run_query
    
    
    def run_query() -> ::Gapic::Config::Method

RPC-specific configuration for `run_query`

**Returns**

  * (::Gapic::Config::Method) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
