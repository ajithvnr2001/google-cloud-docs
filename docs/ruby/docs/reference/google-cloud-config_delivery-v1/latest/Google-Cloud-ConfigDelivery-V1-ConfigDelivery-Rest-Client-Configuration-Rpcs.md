---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_delivery-v1/latest/Google-Cloud-ConfigDelivery-V1-ConfigDelivery-Rest-Client-Configuration-Rpcs/
title: Config Delivery V1 API - Class Google::Cloud::ConfigDelivery::V1::ConfigDelivery::Rest::Client::Configuration::Rpcs (v1.0.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:47:02.450600+00:00
---

# Config Delivery V1 API - Class Google::Cloud::ConfigDelivery::V1::ConfigDelivery::Rest::Client::Configuration::Rpcs (v1.0.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-config_delivery-v1/latest/Google-Cloud-ConfigDelivery-V1-ConfigDelivery-Rest-Client-Configuration-Rpcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Config Delivery V1 API - Class Google::Cloud::ConfigDelivery::V1::ConfigDelivery::Rest::Client::Configuration::Rpcs (v1.0.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.1 (latest)  1.0.0  0.6.0  0.5.0  0.4.0  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Config Delivery V1 API class Google::Cloud::ConfigDelivery::V1::ConfigDelivery::Rest::Client::Configuration::Rpcs.

Configuration RPC class for the ConfigDelivery API.

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

### #abort_rollout
    
    
    def abort_rollout() -> ::Gapic::Config::Method

RPC-specific configuration for `abort_rollout`

**Returns**

  * (::Gapic::Config::Method) 



### #create_fleet_package
    
    
    def create_fleet_package() -> ::Gapic::Config::Method

RPC-specific configuration for `create_fleet_package`

**Returns**

  * (::Gapic::Config::Method) 



### #create_release
    
    
    def create_release() -> ::Gapic::Config::Method

RPC-specific configuration for `create_release`

**Returns**

  * (::Gapic::Config::Method) 



### #create_resource_bundle
    
    
    def create_resource_bundle() -> ::Gapic::Config::Method

RPC-specific configuration for `create_resource_bundle`

**Returns**

  * (::Gapic::Config::Method) 



### #create_variant
    
    
    def create_variant() -> ::Gapic::Config::Method

RPC-specific configuration for `create_variant`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_fleet_package
    
    
    def delete_fleet_package() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_fleet_package`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_release
    
    
    def delete_release() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_release`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_resource_bundle
    
    
    def delete_resource_bundle() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_resource_bundle`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_variant
    
    
    def delete_variant() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_variant`

**Returns**

  * (::Gapic::Config::Method) 



### #get_fleet_package
    
    
    def get_fleet_package() -> ::Gapic::Config::Method

RPC-specific configuration for `get_fleet_package`

**Returns**

  * (::Gapic::Config::Method) 



### #get_release
    
    
    def get_release() -> ::Gapic::Config::Method

RPC-specific configuration for `get_release`

**Returns**

  * (::Gapic::Config::Method) 



### #get_resource_bundle
    
    
    def get_resource_bundle() -> ::Gapic::Config::Method

RPC-specific configuration for `get_resource_bundle`

**Returns**

  * (::Gapic::Config::Method) 



### #get_rollout
    
    
    def get_rollout() -> ::Gapic::Config::Method

RPC-specific configuration for `get_rollout`

**Returns**

  * (::Gapic::Config::Method) 



### #get_variant
    
    
    def get_variant() -> ::Gapic::Config::Method

RPC-specific configuration for `get_variant`

**Returns**

  * (::Gapic::Config::Method) 



### #list_fleet_packages
    
    
    def list_fleet_packages() -> ::Gapic::Config::Method

RPC-specific configuration for `list_fleet_packages`

**Returns**

  * (::Gapic::Config::Method) 



### #list_releases
    
    
    def list_releases() -> ::Gapic::Config::Method

RPC-specific configuration for `list_releases`

**Returns**

  * (::Gapic::Config::Method) 



### #list_resource_bundles
    
    
    def list_resource_bundles() -> ::Gapic::Config::Method

RPC-specific configuration for `list_resource_bundles`

**Returns**

  * (::Gapic::Config::Method) 



### #list_rollouts
    
    
    def list_rollouts() -> ::Gapic::Config::Method

RPC-specific configuration for `list_rollouts`

**Returns**

  * (::Gapic::Config::Method) 



### #list_variants
    
    
    def list_variants() -> ::Gapic::Config::Method

RPC-specific configuration for `list_variants`

**Returns**

  * (::Gapic::Config::Method) 



### #resume_rollout
    
    
    def resume_rollout() -> ::Gapic::Config::Method

RPC-specific configuration for `resume_rollout`

**Returns**

  * (::Gapic::Config::Method) 



### #suspend_rollout
    
    
    def suspend_rollout() -> ::Gapic::Config::Method

RPC-specific configuration for `suspend_rollout`

**Returns**

  * (::Gapic::Config::Method) 



### #update_fleet_package
    
    
    def update_fleet_package() -> ::Gapic::Config::Method

RPC-specific configuration for `update_fleet_package`

**Returns**

  * (::Gapic::Config::Method) 



### #update_release
    
    
    def update_release() -> ::Gapic::Config::Method

RPC-specific configuration for `update_release`

**Returns**

  * (::Gapic::Config::Method) 



### #update_resource_bundle
    
    
    def update_resource_bundle() -> ::Gapic::Config::Method

RPC-specific configuration for `update_resource_bundle`

**Returns**

  * (::Gapic::Config::Method) 



### #update_variant
    
    
    def update_variant() -> ::Gapic::Config::Method

RPC-specific configuration for `update_variant`

**Returns**

  * (::Gapic::Config::Method) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
