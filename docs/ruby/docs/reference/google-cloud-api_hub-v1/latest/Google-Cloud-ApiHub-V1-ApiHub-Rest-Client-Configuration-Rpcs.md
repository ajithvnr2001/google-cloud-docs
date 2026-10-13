---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-ApiHub-Rest-Client-Configuration-Rpcs/
title: API hub V1 API - Class Google::Cloud::ApiHub::V1::ApiHub::Rest::Client::Configuration::Rpcs (v1.0.3) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:27:32.962311+00:00
---

# API hub V1 API - Class Google::Cloud::ApiHub::V1::ApiHub::Rest::Client::Configuration::Rpcs (v1.0.3)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-ApiHub-Rest-Client-Configuration-Rpcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  API hub V1 API - Class Google::Cloud::ApiHub::V1::ApiHub::Rest::Client::Configuration::Rpcs (v1.0.3) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.3 (latest)  1.0.2  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.1  0.3.0  0.2.0  0.1.1 

Reference documentation and code samples for the API hub V1 API class Google::Cloud::ApiHub::V1::ApiHub::Rest::Client::Configuration::Rpcs.

Configuration RPC class for the ApiHub API.

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



### #create_api_operation
    
    
    def create_api_operation() -> ::Gapic::Config::Method

RPC-specific configuration for `create_api_operation`

**Returns**

  * (::Gapic::Config::Method) 



### #create_attribute
    
    
    def create_attribute() -> ::Gapic::Config::Method

RPC-specific configuration for `create_attribute`

**Returns**

  * (::Gapic::Config::Method) 



### #create_deployment
    
    
    def create_deployment() -> ::Gapic::Config::Method

RPC-specific configuration for `create_deployment`

**Returns**

  * (::Gapic::Config::Method) 



### #create_external_api
    
    
    def create_external_api() -> ::Gapic::Config::Method

RPC-specific configuration for `create_external_api`

**Returns**

  * (::Gapic::Config::Method) 



### #create_spec
    
    
    def create_spec() -> ::Gapic::Config::Method

RPC-specific configuration for `create_spec`

**Returns**

  * (::Gapic::Config::Method) 



### #create_version
    
    
    def create_version() -> ::Gapic::Config::Method

RPC-specific configuration for `create_version`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_api
    
    
    def delete_api() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_api`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_api_operation
    
    
    def delete_api_operation() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_api_operation`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_attribute
    
    
    def delete_attribute() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_attribute`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_deployment
    
    
    def delete_deployment() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_deployment`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_external_api
    
    
    def delete_external_api() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_external_api`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_spec
    
    
    def delete_spec() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_spec`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_version
    
    
    def delete_version() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_version`

**Returns**

  * (::Gapic::Config::Method) 



### #get_api
    
    
    def get_api() -> ::Gapic::Config::Method

RPC-specific configuration for `get_api`

**Returns**

  * (::Gapic::Config::Method) 



### #get_api_operation
    
    
    def get_api_operation() -> ::Gapic::Config::Method

RPC-specific configuration for `get_api_operation`

**Returns**

  * (::Gapic::Config::Method) 



### #get_attribute
    
    
    def get_attribute() -> ::Gapic::Config::Method

RPC-specific configuration for `get_attribute`

**Returns**

  * (::Gapic::Config::Method) 



### #get_definition
    
    
    def get_definition() -> ::Gapic::Config::Method

RPC-specific configuration for `get_definition`

**Returns**

  * (::Gapic::Config::Method) 



### #get_deployment
    
    
    def get_deployment() -> ::Gapic::Config::Method

RPC-specific configuration for `get_deployment`

**Returns**

  * (::Gapic::Config::Method) 



### #get_external_api
    
    
    def get_external_api() -> ::Gapic::Config::Method

RPC-specific configuration for `get_external_api`

**Returns**

  * (::Gapic::Config::Method) 



### #get_spec
    
    
    def get_spec() -> ::Gapic::Config::Method

RPC-specific configuration for `get_spec`

**Returns**

  * (::Gapic::Config::Method) 



### #get_spec_contents
    
    
    def get_spec_contents() -> ::Gapic::Config::Method

RPC-specific configuration for `get_spec_contents`

**Returns**

  * (::Gapic::Config::Method) 



### #get_version
    
    
    def get_version() -> ::Gapic::Config::Method

RPC-specific configuration for `get_version`

**Returns**

  * (::Gapic::Config::Method) 



### #list_api_operations
    
    
    def list_api_operations() -> ::Gapic::Config::Method

RPC-specific configuration for `list_api_operations`

**Returns**

  * (::Gapic::Config::Method) 



### #list_apis
    
    
    def list_apis() -> ::Gapic::Config::Method

RPC-specific configuration for `list_apis`

**Returns**

  * (::Gapic::Config::Method) 



### #list_attributes
    
    
    def list_attributes() -> ::Gapic::Config::Method

RPC-specific configuration for `list_attributes`

**Returns**

  * (::Gapic::Config::Method) 



### #list_deployments
    
    
    def list_deployments() -> ::Gapic::Config::Method

RPC-specific configuration for `list_deployments`

**Returns**

  * (::Gapic::Config::Method) 



### #list_external_apis
    
    
    def list_external_apis() -> ::Gapic::Config::Method

RPC-specific configuration for `list_external_apis`

**Returns**

  * (::Gapic::Config::Method) 



### #list_specs
    
    
    def list_specs() -> ::Gapic::Config::Method

RPC-specific configuration for `list_specs`

**Returns**

  * (::Gapic::Config::Method) 



### #list_versions
    
    
    def list_versions() -> ::Gapic::Config::Method

RPC-specific configuration for `list_versions`

**Returns**

  * (::Gapic::Config::Method) 



### #search_resources
    
    
    def search_resources() -> ::Gapic::Config::Method

RPC-specific configuration for `search_resources`

**Returns**

  * (::Gapic::Config::Method) 



### #update_api
    
    
    def update_api() -> ::Gapic::Config::Method

RPC-specific configuration for `update_api`

**Returns**

  * (::Gapic::Config::Method) 



### #update_api_operation
    
    
    def update_api_operation() -> ::Gapic::Config::Method

RPC-specific configuration for `update_api_operation`

**Returns**

  * (::Gapic::Config::Method) 



### #update_attribute
    
    
    def update_attribute() -> ::Gapic::Config::Method

RPC-specific configuration for `update_attribute`

**Returns**

  * (::Gapic::Config::Method) 



### #update_deployment
    
    
    def update_deployment() -> ::Gapic::Config::Method

RPC-specific configuration for `update_deployment`

**Returns**

  * (::Gapic::Config::Method) 



### #update_external_api
    
    
    def update_external_api() -> ::Gapic::Config::Method

RPC-specific configuration for `update_external_api`

**Returns**

  * (::Gapic::Config::Method) 



### #update_spec
    
    
    def update_spec() -> ::Gapic::Config::Method

RPC-specific configuration for `update_spec`

**Returns**

  * (::Gapic::Config::Method) 



### #update_version
    
    
    def update_version() -> ::Gapic::Config::Method

RPC-specific configuration for `update_version`

**Returns**

  * (::Gapic::Config::Method) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
