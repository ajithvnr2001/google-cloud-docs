---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-FeedsService-Client-Configuration-Rpcs/
title: Chronicle V1 API - Class Google::Cloud::Chronicle::V1::FeedsService::Client::Configuration::Rpcs (v1.1.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:38:32.150890+00:00
---

# Chronicle V1 API - Class Google::Cloud::Chronicle::V1::FeedsService::Client::Configuration::Rpcs (v1.1.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-FeedsService-Client-Configuration-Rpcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Chronicle V1 API - Class Google::Cloud::Chronicle::V1::FeedsService::Client::Configuration::Rpcs (v1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.1  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Chronicle V1 API class Google::Cloud::Chronicle::V1::FeedsService::Client::Configuration::Rpcs.

Configuration RPC class for the FeedsService API.

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

### #create_feed
    
    
    def create_feed() -> ::Gapic::Config::Method

RPC-specific configuration for `create_feed`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_feed
    
    
    def delete_feed() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_feed`

**Returns**

  * (::Gapic::Config::Method) 



### #disable_feed
    
    
    def disable_feed() -> ::Gapic::Config::Method

RPC-specific configuration for `disable_feed`

**Returns**

  * (::Gapic::Config::Method) 



### #enable_feed
    
    
    def enable_feed() -> ::Gapic::Config::Method

RPC-specific configuration for `enable_feed`

**Returns**

  * (::Gapic::Config::Method) 



### #fetch_service_account_for_customer
    
    
    def fetch_service_account_for_customer() -> ::Gapic::Config::Method

RPC-specific configuration for `fetch_service_account_for_customer`

**Returns**

  * (::Gapic::Config::Method) 



### #generate_secret
    
    
    def generate_secret() -> ::Gapic::Config::Method

RPC-specific configuration for `generate_secret`

**Returns**

  * (::Gapic::Config::Method) 



### #get_feed
    
    
    def get_feed() -> ::Gapic::Config::Method

RPC-specific configuration for `get_feed`

**Returns**

  * (::Gapic::Config::Method) 



### #get_feed_pack
    
    
    def get_feed_pack() -> ::Gapic::Config::Method

RPC-specific configuration for `get_feed_pack`

**Returns**

  * (::Gapic::Config::Method) 



### #import_push_logs
    
    
    def import_push_logs() -> ::Gapic::Config::Method

RPC-specific configuration for `import_push_logs`

**Returns**

  * (::Gapic::Config::Method) 



### #list_feed_packs
    
    
    def list_feed_packs() -> ::Gapic::Config::Method

RPC-specific configuration for `list_feed_packs`

**Returns**

  * (::Gapic::Config::Method) 



### #list_feed_source_type_schemas
    
    
    def list_feed_source_type_schemas() -> ::Gapic::Config::Method

RPC-specific configuration for `list_feed_source_type_schemas`

**Returns**

  * (::Gapic::Config::Method) 



### #list_feeds
    
    
    def list_feeds() -> ::Gapic::Config::Method

RPC-specific configuration for `list_feeds`

**Returns**

  * (::Gapic::Config::Method) 



### #list_log_type_schemas
    
    
    def list_log_type_schemas() -> ::Gapic::Config::Method

RPC-specific configuration for `list_log_type_schemas`

**Returns**

  * (::Gapic::Config::Method) 



### #update_feed
    
    
    def update_feed() -> ::Gapic::Config::Method

RPC-specific configuration for `update_feed`

**Returns**

  * (::Gapic::Config::Method) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
