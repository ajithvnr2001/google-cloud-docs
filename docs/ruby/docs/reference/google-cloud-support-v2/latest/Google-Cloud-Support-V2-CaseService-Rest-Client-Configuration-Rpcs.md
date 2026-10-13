---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-support-v2/latest/Google-Cloud-Support-V2-CaseService-Rest-Client-Configuration-Rpcs/
title: Google Cloud Support V2 API - Class Google::Cloud::Support::V2::CaseService::Rest::Client::Configuration::Rpcs (v1.11.3) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:00:02.004421+00:00
---

# Google Cloud Support V2 API - Class Google::Cloud::Support::V2::CaseService::Rest::Client::Configuration::Rpcs (v1.11.3)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-support-v2/latest/Google-Cloud-Support-V2-CaseService-Rest-Client-Configuration-Rpcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud Support V2 API - Class Google::Cloud::Support::V2::CaseService::Rest::Client::Configuration::Rpcs (v1.11.3) Stay organized with collections  Save and categorize content based on your preferences. 

1.11.3 (latest)  1.11.2  1.10.0  1.9.0  1.8.0  1.7.1  1.6.0  1.5.1  1.4.1  1.3.0  1.2.1  1.1.0  1.0.1  0.4.0  0.3.2  0.2.0  0.1.0 

Reference documentation and code samples for the Google Cloud Support V2 API class Google::Cloud::Support::V2::CaseService::Rest::Client::Configuration::Rpcs.

Configuration RPC class for the CaseService API.

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

### #close_case
    
    
    def close_case() -> ::Gapic::Config::Method

RPC-specific configuration for `close_case`

**Returns**

  * (::Gapic::Config::Method) 



### #create_case
    
    
    def create_case() -> ::Gapic::Config::Method

RPC-specific configuration for `create_case`

**Returns**

  * (::Gapic::Config::Method) 



### #escalate_case
    
    
    def escalate_case() -> ::Gapic::Config::Method

RPC-specific configuration for `escalate_case`

**Returns**

  * (::Gapic::Config::Method) 



### #get_case
    
    
    def get_case() -> ::Gapic::Config::Method

RPC-specific configuration for `get_case`

**Returns**

  * (::Gapic::Config::Method) 



### #list_cases
    
    
    def list_cases() -> ::Gapic::Config::Method

RPC-specific configuration for `list_cases`

**Returns**

  * (::Gapic::Config::Method) 



### #search_case_classifications
    
    
    def search_case_classifications() -> ::Gapic::Config::Method

RPC-specific configuration for `search_case_classifications`

**Returns**

  * (::Gapic::Config::Method) 



### #search_cases
    
    
    def search_cases() -> ::Gapic::Config::Method

RPC-specific configuration for `search_cases`

**Returns**

  * (::Gapic::Config::Method) 



### #update_case
    
    
    def update_case() -> ::Gapic::Config::Method

RPC-specific configuration for `update_case`

**Returns**

  * (::Gapic::Config::Method) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
