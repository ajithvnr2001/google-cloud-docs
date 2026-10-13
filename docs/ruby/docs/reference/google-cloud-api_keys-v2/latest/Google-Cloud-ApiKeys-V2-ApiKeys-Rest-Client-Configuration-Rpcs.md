---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_keys-v2/latest/Google-Cloud-ApiKeys-V2-ApiKeys-Rest-Client-Configuration-Rpcs/
title: API Keys V2 API - Class Google::Cloud::ApiKeys::V2::ApiKeys::Rest::Client::Configuration::Rpcs (v0.14.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:19:56.954967+00:00
---

# API Keys V2 API - Class Google::Cloud::ApiKeys::V2::ApiKeys::Rest::Client::Configuration::Rpcs (v0.14.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_keys-v2/latest/Google-Cloud-ApiKeys-V2-ApiKeys-Rest-Client-Configuration-Rpcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  API Keys V2 API - Class Google::Cloud::ApiKeys::V2::ApiKeys::Rest::Client::Configuration::Rpcs (v0.14.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.14.2 (latest)  0.14.1  0.13.0  0.12.0  0.11.1  0.10.0  0.9.0  0.8.1  0.7.0  0.6.1  0.5.2  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the API Keys V2 API class Google::Cloud::ApiKeys::V2::ApiKeys::Rest::Client::Configuration::Rpcs.

Configuration RPC class for the ApiKeys API.

Includes fields providing the configuration for each RPC in this service. Each configuration object is of type `Gapic::Config::Method` and includes the following configuration fields:

  * `timeout` (_type:_ `Numeric`) - The call timeout in seconds
  * `metadata` (_type:_ `Hash{Symbol=>String}`) - Additional headers
  * `retry_policy (_type:_`Hash`) - The retry policy. The policy fields include the following keys: 
    * `:initial_delay` (_type:_ `Numeric`) - The initial delay in seconds.
    * `:max_delay` (_type:_ `Numeric`) - The max delay in seconds.
    * `:multiplier` (_type:_ `Numeric`) - The incremental backoff multiplier.
    * `:jitter` (_type:_ `Numeric`) - The jitter in seconds. Default: 1.0.
    * `:retry_codes` (_type:_ `Array<String>`) - The error codes that should trigger a retry.



## Inherits

  * Object 



## Methods 

### #create_key
    
    
    def create_key() -> ::Gapic::Config::Method

RPC-specific configuration for `create_key`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_key
    
    
    def delete_key() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_key`

**Returns**

  * (::Gapic::Config::Method) 



### #get_key
    
    
    def get_key() -> ::Gapic::Config::Method

RPC-specific configuration for `get_key`

**Returns**

  * (::Gapic::Config::Method) 



### #get_key_string
    
    
    def get_key_string() -> ::Gapic::Config::Method

RPC-specific configuration for `get_key_string`

**Returns**

  * (::Gapic::Config::Method) 



### #list_keys
    
    
    def list_keys() -> ::Gapic::Config::Method

RPC-specific configuration for `list_keys`

**Returns**

  * (::Gapic::Config::Method) 



### #lookup_key
    
    
    def lookup_key() -> ::Gapic::Config::Method

RPC-specific configuration for `lookup_key`

**Returns**

  * (::Gapic::Config::Method) 



### #undelete_key
    
    
    def undelete_key() -> ::Gapic::Config::Method

RPC-specific configuration for `undelete_key`

**Returns**

  * (::Gapic::Config::Method) 



### #update_key
    
    
    def update_key() -> ::Gapic::Config::Method

RPC-specific configuration for `update_key`

**Returns**

  * (::Gapic::Config::Method) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
