---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-lineage-v1/latest/Google-Cloud-DataCatalog-Lineage-V1-Lineage-Rest-Client-Configuration-Rpcs/
title: Data Lineage V1 API - Class Google::Cloud::DataCatalog::Lineage::V1::Lineage::Rest::Client::Configuration::Rpcs (v0.16.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:24:22.139570+00:00
---

# Data Lineage V1 API - Class Google::Cloud::DataCatalog::Lineage::V1::Lineage::Rest::Client::Configuration::Rpcs (v0.16.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-lineage-v1/latest/Google-Cloud-DataCatalog-Lineage-V1-Lineage-Rest-Client-Configuration-Rpcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Data Lineage V1 API - Class Google::Cloud::DataCatalog::Lineage::V1::Lineage::Rest::Client::Configuration::Rpcs (v0.16.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.16.1 (latest)  0.16.0  0.15.0  0.14.0  0.13.0  0.12.1  0.11.0  0.10.1  0.9.1  0.8.0  0.7.1  0.6.2  0.5.0  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Data Lineage V1 API class Google::Cloud::DataCatalog::Lineage::V1::Lineage::Rest::Client::Configuration::Rpcs.

Configuration RPC class for the Lineage API.

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

### #batch_search_link_processes
    
    
    def batch_search_link_processes() -> ::Gapic::Config::Method

RPC-specific configuration for `batch_search_link_processes`

**Returns**

  * (::Gapic::Config::Method) 



### #create_lineage_event
    
    
    def create_lineage_event() -> ::Gapic::Config::Method

RPC-specific configuration for `create_lineage_event`

**Returns**

  * (::Gapic::Config::Method) 



### #create_process
    
    
    def create_process() -> ::Gapic::Config::Method

RPC-specific configuration for `create_process`

**Returns**

  * (::Gapic::Config::Method) 



### #create_run
    
    
    def create_run() -> ::Gapic::Config::Method

RPC-specific configuration for `create_run`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_lineage_event
    
    
    def delete_lineage_event() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_lineage_event`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_process
    
    
    def delete_process() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_process`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_run
    
    
    def delete_run() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_run`

**Returns**

  * (::Gapic::Config::Method) 



### #get_lineage_event
    
    
    def get_lineage_event() -> ::Gapic::Config::Method

RPC-specific configuration for `get_lineage_event`

**Returns**

  * (::Gapic::Config::Method) 



### #get_process
    
    
    def get_process() -> ::Gapic::Config::Method

RPC-specific configuration for `get_process`

**Returns**

  * (::Gapic::Config::Method) 



### #get_run
    
    
    def get_run() -> ::Gapic::Config::Method

RPC-specific configuration for `get_run`

**Returns**

  * (::Gapic::Config::Method) 



### #list_lineage_events
    
    
    def list_lineage_events() -> ::Gapic::Config::Method

RPC-specific configuration for `list_lineage_events`

**Returns**

  * (::Gapic::Config::Method) 



### #list_processes
    
    
    def list_processes() -> ::Gapic::Config::Method

RPC-specific configuration for `list_processes`

**Returns**

  * (::Gapic::Config::Method) 



### #list_runs
    
    
    def list_runs() -> ::Gapic::Config::Method

RPC-specific configuration for `list_runs`

**Returns**

  * (::Gapic::Config::Method) 



### #process_open_lineage_run_event
    
    
    def process_open_lineage_run_event() -> ::Gapic::Config::Method

RPC-specific configuration for `process_open_lineage_run_event`

**Returns**

  * (::Gapic::Config::Method) 



### #search_lineage_streaming
    
    
    def search_lineage_streaming() -> ::Gapic::Config::Method

RPC-specific configuration for `search_lineage_streaming`

**Returns**

  * (::Gapic::Config::Method) 



### #search_links
    
    
    def search_links() -> ::Gapic::Config::Method

RPC-specific configuration for `search_links`

**Returns**

  * (::Gapic::Config::Method) 



### #update_process
    
    
    def update_process() -> ::Gapic::Config::Method

RPC-specific configuration for `update_process`

**Returns**

  * (::Gapic::Config::Method) 



### #update_run
    
    
    def update_run() -> ::Gapic::Config::Method

RPC-specific configuration for `update_run`

**Returns**

  * (::Gapic::Config::Method) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
