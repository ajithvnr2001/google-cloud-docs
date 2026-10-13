---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-AML-Client-Configuration-Rpcs/
title: Financial Services V1 API - Class Google::Cloud::FinancialServices::V1::AML::Client::Configuration::Rpcs (v1.0.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:11:52.599530+00:00
---

# Financial Services V1 API - Class Google::Cloud::FinancialServices::V1::AML::Client::Configuration::Rpcs (v1.0.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-AML-Client-Configuration-Rpcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Financial Services V1 API - Class Google::Cloud::FinancialServices::V1::AML::Client::Configuration::Rpcs (v1.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0 (latest)  0.7.0  0.6.1  0.5.0  0.4.1  0.3.0  0.2.0  0.1.1 

Reference documentation and code samples for the Financial Services V1 API class Google::Cloud::FinancialServices::V1::AML::Client::Configuration::Rpcs.

Configuration RPC class for the AML API.

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

### #create_backtest_result
    
    
    def create_backtest_result() -> ::Gapic::Config::Method

RPC-specific configuration for `create_backtest_result`

**Returns**

  * (::Gapic::Config::Method) 



### #create_dataset
    
    
    def create_dataset() -> ::Gapic::Config::Method

RPC-specific configuration for `create_dataset`

**Returns**

  * (::Gapic::Config::Method) 



### #create_engine_config
    
    
    def create_engine_config() -> ::Gapic::Config::Method

RPC-specific configuration for `create_engine_config`

**Returns**

  * (::Gapic::Config::Method) 



### #create_instance
    
    
    def create_instance() -> ::Gapic::Config::Method

RPC-specific configuration for `create_instance`

**Returns**

  * (::Gapic::Config::Method) 



### #create_model
    
    
    def create_model() -> ::Gapic::Config::Method

RPC-specific configuration for `create_model`

**Returns**

  * (::Gapic::Config::Method) 



### #create_prediction_result
    
    
    def create_prediction_result() -> ::Gapic::Config::Method

RPC-specific configuration for `create_prediction_result`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_backtest_result
    
    
    def delete_backtest_result() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_backtest_result`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_dataset
    
    
    def delete_dataset() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_dataset`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_engine_config
    
    
    def delete_engine_config() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_engine_config`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_instance
    
    
    def delete_instance() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_instance`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_model
    
    
    def delete_model() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_model`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_prediction_result
    
    
    def delete_prediction_result() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_prediction_result`

**Returns**

  * (::Gapic::Config::Method) 



### #export_backtest_result_metadata
    
    
    def export_backtest_result_metadata() -> ::Gapic::Config::Method

RPC-specific configuration for `export_backtest_result_metadata`

**Returns**

  * (::Gapic::Config::Method) 



### #export_engine_config_metadata
    
    
    def export_engine_config_metadata() -> ::Gapic::Config::Method

RPC-specific configuration for `export_engine_config_metadata`

**Returns**

  * (::Gapic::Config::Method) 



### #export_model_metadata
    
    
    def export_model_metadata() -> ::Gapic::Config::Method

RPC-specific configuration for `export_model_metadata`

**Returns**

  * (::Gapic::Config::Method) 



### #export_prediction_result_metadata
    
    
    def export_prediction_result_metadata() -> ::Gapic::Config::Method

RPC-specific configuration for `export_prediction_result_metadata`

**Returns**

  * (::Gapic::Config::Method) 



### #export_registered_parties
    
    
    def export_registered_parties() -> ::Gapic::Config::Method

RPC-specific configuration for `export_registered_parties`

**Returns**

  * (::Gapic::Config::Method) 



### #get_backtest_result
    
    
    def get_backtest_result() -> ::Gapic::Config::Method

RPC-specific configuration for `get_backtest_result`

**Returns**

  * (::Gapic::Config::Method) 



### #get_dataset
    
    
    def get_dataset() -> ::Gapic::Config::Method

RPC-specific configuration for `get_dataset`

**Returns**

  * (::Gapic::Config::Method) 



### #get_engine_config
    
    
    def get_engine_config() -> ::Gapic::Config::Method

RPC-specific configuration for `get_engine_config`

**Returns**

  * (::Gapic::Config::Method) 



### #get_engine_version
    
    
    def get_engine_version() -> ::Gapic::Config::Method

RPC-specific configuration for `get_engine_version`

**Returns**

  * (::Gapic::Config::Method) 



### #get_instance
    
    
    def get_instance() -> ::Gapic::Config::Method

RPC-specific configuration for `get_instance`

**Returns**

  * (::Gapic::Config::Method) 



### #get_model
    
    
    def get_model() -> ::Gapic::Config::Method

RPC-specific configuration for `get_model`

**Returns**

  * (::Gapic::Config::Method) 



### #get_prediction_result
    
    
    def get_prediction_result() -> ::Gapic::Config::Method

RPC-specific configuration for `get_prediction_result`

**Returns**

  * (::Gapic::Config::Method) 



### #import_registered_parties
    
    
    def import_registered_parties() -> ::Gapic::Config::Method

RPC-specific configuration for `import_registered_parties`

**Returns**

  * (::Gapic::Config::Method) 



### #list_backtest_results
    
    
    def list_backtest_results() -> ::Gapic::Config::Method

RPC-specific configuration for `list_backtest_results`

**Returns**

  * (::Gapic::Config::Method) 



### #list_datasets
    
    
    def list_datasets() -> ::Gapic::Config::Method

RPC-specific configuration for `list_datasets`

**Returns**

  * (::Gapic::Config::Method) 



### #list_engine_configs
    
    
    def list_engine_configs() -> ::Gapic::Config::Method

RPC-specific configuration for `list_engine_configs`

**Returns**

  * (::Gapic::Config::Method) 



### #list_engine_versions
    
    
    def list_engine_versions() -> ::Gapic::Config::Method

RPC-specific configuration for `list_engine_versions`

**Returns**

  * (::Gapic::Config::Method) 



### #list_instances
    
    
    def list_instances() -> ::Gapic::Config::Method

RPC-specific configuration for `list_instances`

**Returns**

  * (::Gapic::Config::Method) 



### #list_models
    
    
    def list_models() -> ::Gapic::Config::Method

RPC-specific configuration for `list_models`

**Returns**

  * (::Gapic::Config::Method) 



### #list_prediction_results
    
    
    def list_prediction_results() -> ::Gapic::Config::Method

RPC-specific configuration for `list_prediction_results`

**Returns**

  * (::Gapic::Config::Method) 



### #update_backtest_result
    
    
    def update_backtest_result() -> ::Gapic::Config::Method

RPC-specific configuration for `update_backtest_result`

**Returns**

  * (::Gapic::Config::Method) 



### #update_dataset
    
    
    def update_dataset() -> ::Gapic::Config::Method

RPC-specific configuration for `update_dataset`

**Returns**

  * (::Gapic::Config::Method) 



### #update_engine_config
    
    
    def update_engine_config() -> ::Gapic::Config::Method

RPC-specific configuration for `update_engine_config`

**Returns**

  * (::Gapic::Config::Method) 



### #update_instance
    
    
    def update_instance() -> ::Gapic::Config::Method

RPC-specific configuration for `update_instance`

**Returns**

  * (::Gapic::Config::Method) 



### #update_model
    
    
    def update_model() -> ::Gapic::Config::Method

RPC-specific configuration for `update_model`

**Returns**

  * (::Gapic::Config::Method) 



### #update_prediction_result
    
    
    def update_prediction_result() -> ::Gapic::Config::Method

RPC-specific configuration for `update_prediction_result`

**Returns**

  * (::Gapic::Config::Method) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-04 UTC."],[],[]] 
