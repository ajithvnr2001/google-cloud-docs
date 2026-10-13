---
url: https://docs.cloud.google.com/ruby/docs/reference/google-iam-v3/latest/Google-Iam-V3-PrincipalAccessBoundaryPolicies-Client-Configuration-Rpcs/
title: Identity and Access Management (IAM) V3 API - Class Google::Iam::V3::PrincipalAccessBoundaryPolicies::Client::Configuration::Rpcs (v0.6.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:24:33.617194+00:00
---

# Identity and Access Management (IAM) V3 API - Class Google::Iam::V3::PrincipalAccessBoundaryPolicies::Client::Configuration::Rpcs (v0.6.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-iam-v3/latest/Google-Iam-V3-PrincipalAccessBoundaryPolicies-Client-Configuration-Rpcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Identity and Access Management (IAM) V3 API - Class Google::Iam::V3::PrincipalAccessBoundaryPolicies::Client::Configuration::Rpcs (v0.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.6.0 (latest)  0.5.0  0.4.1  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Identity and Access Management (IAM) V3 API class Google::Iam::V3::PrincipalAccessBoundaryPolicies::Client::Configuration::Rpcs.

Configuration RPC class for the PrincipalAccessBoundaryPolicies API.

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

### #create_principal_access_boundary_policy
    
    
    def create_principal_access_boundary_policy() -> ::Gapic::Config::Method

RPC-specific configuration for `create_principal_access_boundary_policy`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_principal_access_boundary_policy
    
    
    def delete_principal_access_boundary_policy() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_principal_access_boundary_policy`

**Returns**

  * (::Gapic::Config::Method) 



### #get_principal_access_boundary_policy
    
    
    def get_principal_access_boundary_policy() -> ::Gapic::Config::Method

RPC-specific configuration for `get_principal_access_boundary_policy`

**Returns**

  * (::Gapic::Config::Method) 



### #list_principal_access_boundary_policies
    
    
    def list_principal_access_boundary_policies() -> ::Gapic::Config::Method

RPC-specific configuration for `list_principal_access_boundary_policies`

**Returns**

  * (::Gapic::Config::Method) 



### #search_principal_access_boundary_policy_bindings
    
    
    def search_principal_access_boundary_policy_bindings() -> ::Gapic::Config::Method

RPC-specific configuration for `search_principal_access_boundary_policy_bindings`

**Returns**

  * (::Gapic::Config::Method) 



### #update_principal_access_boundary_policy
    
    
    def update_principal_access_boundary_policy() -> ::Gapic::Config::Method

RPC-specific configuration for `update_principal_access_boundary_policy`

**Returns**

  * (::Gapic::Config::Method) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
