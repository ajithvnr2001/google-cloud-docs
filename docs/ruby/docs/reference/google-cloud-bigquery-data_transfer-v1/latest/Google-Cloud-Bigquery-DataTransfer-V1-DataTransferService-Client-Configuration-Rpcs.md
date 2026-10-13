---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-data_transfer-v1/latest/Google-Cloud-Bigquery-DataTransfer-V1-DataTransferService-Client-Configuration-Rpcs/
title: BigQuery Data Transfer Service V1 API - Class Google::Cloud::Bigquery::DataTransfer::V1::DataTransferService::Client::Configuration::Rpcs (v1.7.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:36:59.968325+00:00
---

# BigQuery Data Transfer Service V1 API - Class Google::Cloud::Bigquery::DataTransfer::V1::DataTransferService::Client::Configuration::Rpcs (v1.7.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-data_transfer-v1/latest/Google-Cloud-Bigquery-DataTransfer-V1-DataTransferService-Client-Configuration-Rpcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  BigQuery Data Transfer Service V1 API - Class Google::Cloud::Bigquery::DataTransfer::V1::DataTransferService::Client::Configuration::Rpcs (v1.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.7.1 (latest)  1.7.0  1.6.0  1.5.1  1.4.1  1.3.1  1.2.0  1.1.0  1.0.3  0.14.2  0.13.1  0.12.2  0.11.0  0.10.0  0.9.0  0.8.0  0.7.1  0.6.1  0.5.1  0.4.6 

Reference documentation and code samples for the BigQuery Data Transfer Service V1 API class Google::Cloud::Bigquery::DataTransfer::V1::DataTransferService::Client::Configuration::Rpcs.

Configuration RPC class for the DataTransferService API.

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

### #check_valid_creds
    
    
    def check_valid_creds() -> ::Gapic::Config::Method

RPC-specific configuration for `check_valid_creds`

**Returns**

  * (::Gapic::Config::Method) 



### #create_transfer_config
    
    
    def create_transfer_config() -> ::Gapic::Config::Method

RPC-specific configuration for `create_transfer_config`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_transfer_config
    
    
    def delete_transfer_config() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_transfer_config`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_transfer_run
    
    
    def delete_transfer_run() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_transfer_run`

**Returns**

  * (::Gapic::Config::Method) 



### #enroll_data_sources
    
    
    def enroll_data_sources() -> ::Gapic::Config::Method

RPC-specific configuration for `enroll_data_sources`

**Returns**

  * (::Gapic::Config::Method) 



### #get_data_source
    
    
    def get_data_source() -> ::Gapic::Config::Method

RPC-specific configuration for `get_data_source`

**Returns**

  * (::Gapic::Config::Method) 



### #get_transfer_config
    
    
    def get_transfer_config() -> ::Gapic::Config::Method

RPC-specific configuration for `get_transfer_config`

**Returns**

  * (::Gapic::Config::Method) 



### #get_transfer_run
    
    
    def get_transfer_run() -> ::Gapic::Config::Method

RPC-specific configuration for `get_transfer_run`

**Returns**

  * (::Gapic::Config::Method) 



### #list_data_sources
    
    
    def list_data_sources() -> ::Gapic::Config::Method

RPC-specific configuration for `list_data_sources`

**Returns**

  * (::Gapic::Config::Method) 



### #list_transfer_configs
    
    
    def list_transfer_configs() -> ::Gapic::Config::Method

RPC-specific configuration for `list_transfer_configs`

**Returns**

  * (::Gapic::Config::Method) 



### #list_transfer_logs
    
    
    def list_transfer_logs() -> ::Gapic::Config::Method

RPC-specific configuration for `list_transfer_logs`

**Returns**

  * (::Gapic::Config::Method) 



### #list_transfer_runs
    
    
    def list_transfer_runs() -> ::Gapic::Config::Method

RPC-specific configuration for `list_transfer_runs`

**Returns**

  * (::Gapic::Config::Method) 



### #schedule_transfer_runs
    
    
    def schedule_transfer_runs() -> ::Gapic::Config::Method

RPC-specific configuration for `schedule_transfer_runs`

**Returns**

  * (::Gapic::Config::Method) 



### #start_manual_transfer_runs
    
    
    def start_manual_transfer_runs() -> ::Gapic::Config::Method

RPC-specific configuration for `start_manual_transfer_runs`

**Returns**

  * (::Gapic::Config::Method) 



### #unenroll_data_sources
    
    
    def unenroll_data_sources() -> ::Gapic::Config::Method

RPC-specific configuration for `unenroll_data_sources`

**Returns**

  * (::Gapic::Config::Method) 



### #update_transfer_config
    
    
    def update_transfer_config() -> ::Gapic::Config::Method

RPC-specific configuration for `update_transfer_config`

**Returns**

  * (::Gapic::Config::Method) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
