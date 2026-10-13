---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Environments-Rest-Client-Configuration-Rpcs/
title: Dialogflow CX V3 API - Class Google::Cloud::Dialogflow::CX::V3::Environments::Rest::Client::Configuration::Rpcs (v1.12.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:49:48.415186+00:00
---

# Dialogflow CX V3 API - Class Google::Cloud::Dialogflow::CX::V3::Environments::Rest::Client::Configuration::Rpcs (v1.12.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Environments-Rest-Client-Configuration-Rpcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dialogflow CX V3 API - Class Google::Cloud::Dialogflow::CX::V3::Environments::Rest::Client::Configuration::Rpcs (v1.12.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.12.2 (latest)  1.12.1  1.11.0  1.10.1  1.9.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.0  1.3.0  1.2.0  1.1.1  1.0.0  0.26.0  0.25.0  0.24.2  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.1  0.14.0  0.13.0  0.12.0  0.11.0  0.10.2  0.9.0  0.8.1  0.7.1  0.6.0  0.5.0  0.4.0 

Reference documentation and code samples for the Dialogflow CX V3 API class Google::Cloud::Dialogflow::CX::V3::Environments::Rest::Client::Configuration::Rpcs.

Configuration RPC class for the Environments API.

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

### #create_environment
    
    
    def create_environment() -> ::Gapic::Config::Method

RPC-specific configuration for `create_environment`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_environment
    
    
    def delete_environment() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_environment`

**Returns**

  * (::Gapic::Config::Method) 



### #deploy_flow
    
    
    def deploy_flow() -> ::Gapic::Config::Method

RPC-specific configuration for `deploy_flow`

**Returns**

  * (::Gapic::Config::Method) 



### #get_environment
    
    
    def get_environment() -> ::Gapic::Config::Method

RPC-specific configuration for `get_environment`

**Returns**

  * (::Gapic::Config::Method) 



### #list_continuous_test_results
    
    
    def list_continuous_test_results() -> ::Gapic::Config::Method

RPC-specific configuration for `list_continuous_test_results`

**Returns**

  * (::Gapic::Config::Method) 



### #list_environments
    
    
    def list_environments() -> ::Gapic::Config::Method

RPC-specific configuration for `list_environments`

**Returns**

  * (::Gapic::Config::Method) 



### #lookup_environment_history
    
    
    def lookup_environment_history() -> ::Gapic::Config::Method

RPC-specific configuration for `lookup_environment_history`

**Returns**

  * (::Gapic::Config::Method) 



### #run_continuous_test
    
    
    def run_continuous_test() -> ::Gapic::Config::Method

RPC-specific configuration for `run_continuous_test`

**Returns**

  * (::Gapic::Config::Method) 



### #update_environment
    
    
    def update_environment() -> ::Gapic::Config::Method

RPC-specific configuration for `update_environment`

**Returns**

  * (::Gapic::Config::Method) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
