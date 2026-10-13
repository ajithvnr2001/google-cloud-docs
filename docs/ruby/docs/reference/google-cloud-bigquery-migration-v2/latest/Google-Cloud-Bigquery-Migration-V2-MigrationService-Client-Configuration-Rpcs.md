---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-MigrationService-Client-Configuration-Rpcs/
title: BigQuery Migration V2 API - Class Google::Cloud::Bigquery::Migration::V2::MigrationService::Client::Configuration::Rpcs (v0.23.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:09:59.584639+00:00
---

# BigQuery Migration V2 API - Class Google::Cloud::Bigquery::Migration::V2::MigrationService::Client::Configuration::Rpcs (v0.23.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-MigrationService-Client-Configuration-Rpcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  BigQuery Migration V2 API - Class Google::Cloud::Bigquery::Migration::V2::MigrationService::Client::Configuration::Rpcs (v0.23.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.23.0 (latest)  0.22.1  0.21.0  0.20.0  0.19.0  0.18.0  0.17.1  0.16.0  0.15.1  0.14.1  0.13.0  0.12.0  0.11.1  0.10.0  0.9.2  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the BigQuery Migration V2 API class Google::Cloud::Bigquery::Migration::V2::MigrationService::Client::Configuration::Rpcs.

Configuration RPC class for the MigrationService API.

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

### #create_migration_workflow
    
    
    def create_migration_workflow() -> ::Gapic::Config::Method

RPC-specific configuration for `create_migration_workflow`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_migration_workflow
    
    
    def delete_migration_workflow() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_migration_workflow`

**Returns**

  * (::Gapic::Config::Method) 



### #get_migration_subtask
    
    
    def get_migration_subtask() -> ::Gapic::Config::Method

RPC-specific configuration for `get_migration_subtask`

**Returns**

  * (::Gapic::Config::Method) 



### #get_migration_workflow
    
    
    def get_migration_workflow() -> ::Gapic::Config::Method

RPC-specific configuration for `get_migration_workflow`

**Returns**

  * (::Gapic::Config::Method) 



### #list_migration_subtasks
    
    
    def list_migration_subtasks() -> ::Gapic::Config::Method

RPC-specific configuration for `list_migration_subtasks`

**Returns**

  * (::Gapic::Config::Method) 



### #list_migration_workflows
    
    
    def list_migration_workflows() -> ::Gapic::Config::Method

RPC-specific configuration for `list_migration_workflows`

**Returns**

  * (::Gapic::Config::Method) 



### #start_migration_workflow
    
    
    def start_migration_workflow() -> ::Gapic::Config::Method

RPC-specific configuration for `start_migration_workflow`

**Returns**

  * (::Gapic::Config::Method) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
