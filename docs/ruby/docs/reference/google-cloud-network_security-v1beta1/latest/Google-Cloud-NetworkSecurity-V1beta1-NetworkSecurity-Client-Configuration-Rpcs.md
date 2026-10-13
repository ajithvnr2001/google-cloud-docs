---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1beta1/latest/Google-Cloud-NetworkSecurity-V1beta1-NetworkSecurity-Client-Configuration-Rpcs/
title: Network Security V1beta1 API - Class Google::Cloud::NetworkSecurity::V1beta1::NetworkSecurity::Client::Configuration::Rpcs (v0.17.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:16:33.653738+00:00
---

# Network Security V1beta1 API - Class Google::Cloud::NetworkSecurity::V1beta1::NetworkSecurity::Client::Configuration::Rpcs (v0.17.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1beta1/latest/Google-Cloud-NetworkSecurity-V1beta1-NetworkSecurity-Client-Configuration-Rpcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Network Security V1beta1 API - Class Google::Cloud::NetworkSecurity::V1beta1::NetworkSecurity::Client::Configuration::Rpcs (v0.17.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.17.0 (latest)  0.16.0  0.15.0  0.14.0  0.13.1  0.12.0  0.11.0  0.10.1  0.9.0  0.8.1  0.7.2  0.6.0  0.5.1  0.4.0  0.3.0  0.2.0  0.1.2 

Reference documentation and code samples for the Network Security V1beta1 API class Google::Cloud::NetworkSecurity::V1beta1::NetworkSecurity::Client::Configuration::Rpcs.

Configuration RPC class for the NetworkSecurity API.

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

### #create_authorization_policy
    
    
    def create_authorization_policy() -> ::Gapic::Config::Method

RPC-specific configuration for `create_authorization_policy`

**Returns**

  * (::Gapic::Config::Method) 



### #create_client_tls_policy
    
    
    def create_client_tls_policy() -> ::Gapic::Config::Method

RPC-specific configuration for `create_client_tls_policy`

**Returns**

  * (::Gapic::Config::Method) 



### #create_server_tls_policy
    
    
    def create_server_tls_policy() -> ::Gapic::Config::Method

RPC-specific configuration for `create_server_tls_policy`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_authorization_policy
    
    
    def delete_authorization_policy() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_authorization_policy`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_client_tls_policy
    
    
    def delete_client_tls_policy() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_client_tls_policy`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_server_tls_policy
    
    
    def delete_server_tls_policy() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_server_tls_policy`

**Returns**

  * (::Gapic::Config::Method) 



### #get_authorization_policy
    
    
    def get_authorization_policy() -> ::Gapic::Config::Method

RPC-specific configuration for `get_authorization_policy`

**Returns**

  * (::Gapic::Config::Method) 



### #get_client_tls_policy
    
    
    def get_client_tls_policy() -> ::Gapic::Config::Method

RPC-specific configuration for `get_client_tls_policy`

**Returns**

  * (::Gapic::Config::Method) 



### #get_server_tls_policy
    
    
    def get_server_tls_policy() -> ::Gapic::Config::Method

RPC-specific configuration for `get_server_tls_policy`

**Returns**

  * (::Gapic::Config::Method) 



### #list_authorization_policies
    
    
    def list_authorization_policies() -> ::Gapic::Config::Method

RPC-specific configuration for `list_authorization_policies`

**Returns**

  * (::Gapic::Config::Method) 



### #list_client_tls_policies
    
    
    def list_client_tls_policies() -> ::Gapic::Config::Method

RPC-specific configuration for `list_client_tls_policies`

**Returns**

  * (::Gapic::Config::Method) 



### #list_server_tls_policies
    
    
    def list_server_tls_policies() -> ::Gapic::Config::Method

RPC-specific configuration for `list_server_tls_policies`

**Returns**

  * (::Gapic::Config::Method) 



### #update_authorization_policy
    
    
    def update_authorization_policy() -> ::Gapic::Config::Method

RPC-specific configuration for `update_authorization_policy`

**Returns**

  * (::Gapic::Config::Method) 



### #update_client_tls_policy
    
    
    def update_client_tls_policy() -> ::Gapic::Config::Method

RPC-specific configuration for `update_client_tls_policy`

**Returns**

  * (::Gapic::Config::Method) 



### #update_server_tls_policy
    
    
    def update_server_tls_policy() -> ::Gapic::Config::Method

RPC-specific configuration for `update_server_tls_policy`

**Returns**

  * (::Gapic::Config::Method) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
