---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_gateway-v1/latest/Google-Cloud-ApiGateway-V1-ApiGatewayService-Rest-Client-Configuration-Rpcs/
title: API Gateway V1 API - Class Google::Cloud::ApiGateway::V1::ApiGatewayService::Rest::Client::Configuration::Rpcs (v2.8.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:34:30.293546+00:00
---

# API Gateway V1 API - Class Google::Cloud::ApiGateway::V1::ApiGatewayService::Rest::Client::Configuration::Rpcs (v2.8.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_gateway-v1/latest/Google-Cloud-ApiGateway-V1-ApiGatewayService-Rest-Client-Configuration-Rpcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  API Gateway V1 API - Class Google::Cloud::ApiGateway::V1::ApiGatewayService::Rest::Client::Configuration::Rpcs (v2.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.8.0 (latest)  2.7.0  2.6.2  2.5.0  2.4.0  2.3.1  2.2.0  2.1.0  2.0.1  1.2.0  1.1.0  1.0.1  0.7.0  0.6.2  0.5.0  0.4.0  0.3.0  0.2.0  0.1.5 

Reference documentation and code samples for the API Gateway V1 API class Google::Cloud::ApiGateway::V1::ApiGatewayService::Rest::Client::Configuration::Rpcs.

Configuration RPC class for the ApiGatewayService API.

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

### #create_api
    
    
    def create_api() -> ::Gapic::Config::Method

RPC-specific configuration for `create_api`

**Returns**

  * (::Gapic::Config::Method) 



### #create_api_config
    
    
    def create_api_config() -> ::Gapic::Config::Method

RPC-specific configuration for `create_api_config`

**Returns**

  * (::Gapic::Config::Method) 



### #create_gateway
    
    
    def create_gateway() -> ::Gapic::Config::Method

RPC-specific configuration for `create_gateway`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_api
    
    
    def delete_api() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_api`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_api_config
    
    
    def delete_api_config() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_api_config`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_gateway
    
    
    def delete_gateway() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_gateway`

**Returns**

  * (::Gapic::Config::Method) 



### #get_api
    
    
    def get_api() -> ::Gapic::Config::Method

RPC-specific configuration for `get_api`

**Returns**

  * (::Gapic::Config::Method) 



### #get_api_config
    
    
    def get_api_config() -> ::Gapic::Config::Method

RPC-specific configuration for `get_api_config`

**Returns**

  * (::Gapic::Config::Method) 



### #get_gateway
    
    
    def get_gateway() -> ::Gapic::Config::Method

RPC-specific configuration for `get_gateway`

**Returns**

  * (::Gapic::Config::Method) 



### #list_api_configs
    
    
    def list_api_configs() -> ::Gapic::Config::Method

RPC-specific configuration for `list_api_configs`

**Returns**

  * (::Gapic::Config::Method) 



### #list_apis
    
    
    def list_apis() -> ::Gapic::Config::Method

RPC-specific configuration for `list_apis`

**Returns**

  * (::Gapic::Config::Method) 



### #list_gateways
    
    
    def list_gateways() -> ::Gapic::Config::Method

RPC-specific configuration for `list_gateways`

**Returns**

  * (::Gapic::Config::Method) 



### #update_api
    
    
    def update_api() -> ::Gapic::Config::Method

RPC-specific configuration for `update_api`

**Returns**

  * (::Gapic::Config::Method) 



### #update_api_config
    
    
    def update_api_config() -> ::Gapic::Config::Method

RPC-specific configuration for `update_api_config`

**Returns**

  * (::Gapic::Config::Method) 



### #update_gateway
    
    
    def update_gateway() -> ::Gapic::Config::Method

RPC-specific configuration for `update_gateway`

**Returns**

  * (::Gapic::Config::Method) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
