---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-EdgeNetwork-Client-Configuration-Rpcs/
title: Distributed Cloud Edge Network V1 API - Class Google::Cloud::EdgeNetwork::V1::EdgeNetwork::Client::Configuration::Rpcs (v2.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:02:12.759907+00:00
---

# Distributed Cloud Edge Network V1 API - Class Google::Cloud::EdgeNetwork::V1::EdgeNetwork::Client::Configuration::Rpcs (v2.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-EdgeNetwork-Client-Configuration-Rpcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Distributed Cloud Edge Network V1 API - Class Google::Cloud::EdgeNetwork::V1::EdgeNetwork::Client::Configuration::Rpcs (v2.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.6.1 (latest)  2.6.0  2.5.0  2.4.0  2.3.1  2.2.0  2.1.0  2.0.2  1.2.0  1.1.0  1.0.3  0.5.0  0.4.1  0.3.1  0.2.1  0.1.0 

Reference documentation and code samples for the Distributed Cloud Edge Network V1 API class Google::Cloud::EdgeNetwork::V1::EdgeNetwork::Client::Configuration::Rpcs.

Configuration RPC class for the EdgeNetwork API.

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

### #create_interconnect_attachment
    
    
    def create_interconnect_attachment() -> ::Gapic::Config::Method

RPC-specific configuration for `create_interconnect_attachment`

**Returns**

  * (::Gapic::Config::Method) 



### #create_network
    
    
    def create_network() -> ::Gapic::Config::Method

RPC-specific configuration for `create_network`

**Returns**

  * (::Gapic::Config::Method) 



### #create_router
    
    
    def create_router() -> ::Gapic::Config::Method

RPC-specific configuration for `create_router`

**Returns**

  * (::Gapic::Config::Method) 



### #create_subnet
    
    
    def create_subnet() -> ::Gapic::Config::Method

RPC-specific configuration for `create_subnet`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_interconnect_attachment
    
    
    def delete_interconnect_attachment() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_interconnect_attachment`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_network
    
    
    def delete_network() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_network`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_router
    
    
    def delete_router() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_router`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_subnet
    
    
    def delete_subnet() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_subnet`

**Returns**

  * (::Gapic::Config::Method) 



### #diagnose_interconnect
    
    
    def diagnose_interconnect() -> ::Gapic::Config::Method

RPC-specific configuration for `diagnose_interconnect`

**Returns**

  * (::Gapic::Config::Method) 



### #diagnose_network
    
    
    def diagnose_network() -> ::Gapic::Config::Method

RPC-specific configuration for `diagnose_network`

**Returns**

  * (::Gapic::Config::Method) 



### #diagnose_router
    
    
    def diagnose_router() -> ::Gapic::Config::Method

RPC-specific configuration for `diagnose_router`

**Returns**

  * (::Gapic::Config::Method) 



### #get_interconnect
    
    
    def get_interconnect() -> ::Gapic::Config::Method

RPC-specific configuration for `get_interconnect`

**Returns**

  * (::Gapic::Config::Method) 



### #get_interconnect_attachment
    
    
    def get_interconnect_attachment() -> ::Gapic::Config::Method

RPC-specific configuration for `get_interconnect_attachment`

**Returns**

  * (::Gapic::Config::Method) 



### #get_network
    
    
    def get_network() -> ::Gapic::Config::Method

RPC-specific configuration for `get_network`

**Returns**

  * (::Gapic::Config::Method) 



### #get_router
    
    
    def get_router() -> ::Gapic::Config::Method

RPC-specific configuration for `get_router`

**Returns**

  * (::Gapic::Config::Method) 



### #get_subnet
    
    
    def get_subnet() -> ::Gapic::Config::Method

RPC-specific configuration for `get_subnet`

**Returns**

  * (::Gapic::Config::Method) 



### #get_zone
    
    
    def get_zone() -> ::Gapic::Config::Method

RPC-specific configuration for `get_zone`

**Returns**

  * (::Gapic::Config::Method) 



### #initialize_zone
    
    
    def initialize_zone() -> ::Gapic::Config::Method

RPC-specific configuration for `initialize_zone`

**Returns**

  * (::Gapic::Config::Method) 



### #list_interconnect_attachments
    
    
    def list_interconnect_attachments() -> ::Gapic::Config::Method

RPC-specific configuration for `list_interconnect_attachments`

**Returns**

  * (::Gapic::Config::Method) 



### #list_interconnects
    
    
    def list_interconnects() -> ::Gapic::Config::Method

RPC-specific configuration for `list_interconnects`

**Returns**

  * (::Gapic::Config::Method) 



### #list_networks
    
    
    def list_networks() -> ::Gapic::Config::Method

RPC-specific configuration for `list_networks`

**Returns**

  * (::Gapic::Config::Method) 



### #list_routers
    
    
    def list_routers() -> ::Gapic::Config::Method

RPC-specific configuration for `list_routers`

**Returns**

  * (::Gapic::Config::Method) 



### #list_subnets
    
    
    def list_subnets() -> ::Gapic::Config::Method

RPC-specific configuration for `list_subnets`

**Returns**

  * (::Gapic::Config::Method) 



### #list_zones
    
    
    def list_zones() -> ::Gapic::Config::Method

RPC-specific configuration for `list_zones`

**Returns**

  * (::Gapic::Config::Method) 



### #update_router
    
    
    def update_router() -> ::Gapic::Config::Method

RPC-specific configuration for `update_router`

**Returns**

  * (::Gapic::Config::Method) 



### #update_subnet
    
    
    def update_subnet() -> ::Gapic::Config::Method

RPC-specific configuration for `update_subnet`

**Returns**

  * (::Gapic::Config::Method) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
