---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Services-Rest-Operations-Configuration-Rpcs/
title: Cloud Run V2 API - Class Google::Cloud::Run::V2::Services::Rest::Operations::Configuration::Rpcs (v0.29.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:40:36.367655+00:00
---

# Cloud Run V2 API - Class Google::Cloud::Run::V2::Services::Rest::Operations::Configuration::Rpcs (v0.29.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Services-Rest-Operations-Configuration-Rpcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Run V2 API - Class Google::Cloud::Run::V2::Services::Rest::Operations::Configuration::Rpcs (v0.29.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.29.1 (latest)  0.29.0  0.28.1  0.27.0  0.26.0  0.25.0  0.24.1  0.23.0  0.22.1  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.1  0.15.0  0.14.0  0.13.2  0.12.0  0.11.0  0.10.1  0.9.1  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Cloud Run V2 API class Google::Cloud::Run::V2::Services::Rest::Operations::Configuration::Rpcs.

Configuration RPC class for the Operations API.

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

### #cancel_operation
    
    
    def cancel_operation() -> ::Gapic::Config::Method

RPC-specific configuration for `cancel_operation`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_operation
    
    
    def delete_operation() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_operation`

**Returns**

  * (::Gapic::Config::Method) 



### #get_operation
    
    
    def get_operation() -> ::Gapic::Config::Method

RPC-specific configuration for `get_operation`

**Returns**

  * (::Gapic::Config::Method) 



### #list_operations
    
    
    def list_operations() -> ::Gapic::Config::Method

RPC-specific configuration for `list_operations`

**Returns**

  * (::Gapic::Config::Method) 



### #wait_operation
    
    
    def wait_operation() -> ::Gapic::Config::Method

RPC-specific configuration for `wait_operation`

**Returns**

  * (::Gapic::Config::Method) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
