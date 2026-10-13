---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-v1beta1/latest/Google-Cloud-Redis-V1beta1-CloudRedis-Rest-Client-Configuration-Rpcs/
title: Google Cloud Memorystore for Redis V1beta1 API - Class Google::Cloud::Redis::V1beta1::CloudRedis::Rest::Client::Configuration::Rpcs (v0.22.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:30:48.046646+00:00
---

# Google Cloud Memorystore for Redis V1beta1 API - Class Google::Cloud::Redis::V1beta1::CloudRedis::Rest::Client::Configuration::Rpcs (v0.22.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-redis-v1beta1/latest/Google-Cloud-Redis-V1beta1-CloudRedis-Rest-Client-Configuration-Rpcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud Memorystore for Redis V1beta1 API - Class Google::Cloud::Redis::V1beta1::CloudRedis::Rest::Client::Configuration::Rpcs (v0.22.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.22.0 (latest)  0.21.1  0.20.0  0.19.1  0.18.0  0.17.0  0.16.1  0.15.0  0.14.0  0.13.2  0.12.2  0.11.0  0.10.1  0.9.0  0.8.0  0.7.0  0.6.0  0.5.1 

Reference documentation and code samples for the Google Cloud Memorystore for Redis V1beta1 API class Google::Cloud::Redis::V1beta1::CloudRedis::Rest::Client::Configuration::Rpcs.

Configuration RPC class for the CloudRedis API.

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

### #create_instance
    
    
    def create_instance() -> ::Gapic::Config::Method

RPC-specific configuration for `create_instance`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_instance
    
    
    def delete_instance() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_instance`

**Returns**

  * (::Gapic::Config::Method) 



### #export_instance
    
    
    def export_instance() -> ::Gapic::Config::Method

RPC-specific configuration for `export_instance`

**Returns**

  * (::Gapic::Config::Method) 



### #failover_instance
    
    
    def failover_instance() -> ::Gapic::Config::Method

RPC-specific configuration for `failover_instance`

**Returns**

  * (::Gapic::Config::Method) 



### #get_instance
    
    
    def get_instance() -> ::Gapic::Config::Method

RPC-specific configuration for `get_instance`

**Returns**

  * (::Gapic::Config::Method) 



### #get_instance_auth_string
    
    
    def get_instance_auth_string() -> ::Gapic::Config::Method

RPC-specific configuration for `get_instance_auth_string`

**Returns**

  * (::Gapic::Config::Method) 



### #import_instance
    
    
    def import_instance() -> ::Gapic::Config::Method

RPC-specific configuration for `import_instance`

**Returns**

  * (::Gapic::Config::Method) 



### #list_instances
    
    
    def list_instances() -> ::Gapic::Config::Method

RPC-specific configuration for `list_instances`

**Returns**

  * (::Gapic::Config::Method) 



### #reschedule_maintenance
    
    
    def reschedule_maintenance() -> ::Gapic::Config::Method

RPC-specific configuration for `reschedule_maintenance`

**Returns**

  * (::Gapic::Config::Method) 



### #update_instance
    
    
    def update_instance() -> ::Gapic::Config::Method

RPC-specific configuration for `update_instance`

**Returns**

  * (::Gapic::Config::Method) 



### #upgrade_instance
    
    
    def upgrade_instance() -> ::Gapic::Config::Method

RPC-specific configuration for `upgrade_instance`

**Returns**

  * (::Gapic::Config::Method) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
