---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-FindingsRefinementService-Client-Configuration-Rpcs/
title: Chronicle V1 API - Class Google::Cloud::Chronicle::V1::FindingsRefinementService::Client::Configuration::Rpcs (v1.1.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:22:29.359975+00:00
---

# Chronicle V1 API - Class Google::Cloud::Chronicle::V1::FindingsRefinementService::Client::Configuration::Rpcs (v1.1.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-FindingsRefinementService-Client-Configuration-Rpcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Chronicle V1 API - Class Google::Cloud::Chronicle::V1::FindingsRefinementService::Client::Configuration::Rpcs (v1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.1  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Chronicle V1 API class Google::Cloud::Chronicle::V1::FindingsRefinementService::Client::Configuration::Rpcs.

Configuration RPC class for the FindingsRefinementService API.

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

### #compute_all_findings_refinement_activities
    
    
    def compute_all_findings_refinement_activities() -> ::Gapic::Config::Method

RPC-specific configuration for `compute_all_findings_refinement_activities`

**Returns**

  * (::Gapic::Config::Method) 



### #compute_findings_refinement_activity
    
    
    def compute_findings_refinement_activity() -> ::Gapic::Config::Method

RPC-specific configuration for `compute_findings_refinement_activity`

**Returns**

  * (::Gapic::Config::Method) 



### #create_findings_refinement
    
    
    def create_findings_refinement() -> ::Gapic::Config::Method

RPC-specific configuration for `create_findings_refinement`

**Returns**

  * (::Gapic::Config::Method) 



### #get_findings_refinement
    
    
    def get_findings_refinement() -> ::Gapic::Config::Method

RPC-specific configuration for `get_findings_refinement`

**Returns**

  * (::Gapic::Config::Method) 



### #get_findings_refinement_deployment
    
    
    def get_findings_refinement_deployment() -> ::Gapic::Config::Method

RPC-specific configuration for `get_findings_refinement_deployment`

**Returns**

  * (::Gapic::Config::Method) 



### #list_all_findings_refinement_deployments
    
    
    def list_all_findings_refinement_deployments() -> ::Gapic::Config::Method

RPC-specific configuration for `list_all_findings_refinement_deployments`

**Returns**

  * (::Gapic::Config::Method) 



### #list_findings_refinements
    
    
    def list_findings_refinements() -> ::Gapic::Config::Method

RPC-specific configuration for `list_findings_refinements`

**Returns**

  * (::Gapic::Config::Method) 



### #update_findings_refinement
    
    
    def update_findings_refinement() -> ::Gapic::Config::Method

RPC-specific configuration for `update_findings_refinement`

**Returns**

  * (::Gapic::Config::Method) 



### #update_findings_refinement_deployment
    
    
    def update_findings_refinement_deployment() -> ::Gapic::Config::Method

RPC-specific configuration for `update_findings_refinement_deployment`

**Returns**

  * (::Gapic::Config::Method) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
