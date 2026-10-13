---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-artifact_registry-v1/latest/Google-Cloud-ArtifactRegistry-V1-ArtifactRegistry-Operations-Configuration-Rpcs/
title: Artifact Registry V1 API - Class Google::Cloud::ArtifactRegistry::V1::ArtifactRegistry::Operations::Configuration::Rpcs (v1.14.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:37:11.051527+00:00
---

# Artifact Registry V1 API - Class Google::Cloud::ArtifactRegistry::V1::ArtifactRegistry::Operations::Configuration::Rpcs (v1.14.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-artifact_registry-v1/latest/Google-Cloud-ArtifactRegistry-V1-ArtifactRegistry-Operations-Configuration-Rpcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Artifact Registry V1 API - Class Google::Cloud::ArtifactRegistry::V1::ArtifactRegistry::Operations::Configuration::Rpcs (v1.14.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.14.1 (latest)  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.1  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.13.0  0.12.2  0.11.0  0.10.0  0.9.1  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.2 

Reference documentation and code samples for the Artifact Registry V1 API class Google::Cloud::ArtifactRegistry::V1::ArtifactRegistry::Operations::Configuration::Rpcs.

Configuration RPC class for the Operations API.

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
