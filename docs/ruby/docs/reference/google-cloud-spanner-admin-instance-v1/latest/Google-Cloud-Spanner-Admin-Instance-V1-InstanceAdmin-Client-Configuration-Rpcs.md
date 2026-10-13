---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-instance-v1/latest/Google-Cloud-Spanner-Admin-Instance-V1-InstanceAdmin-Client-Configuration-Rpcs/
title: Cloud Spanner Instance Admin V1 API - Class Google::Cloud::Spanner::Admin::Instance::V1::InstanceAdmin::Client::Configuration::Rpcs (v2.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:33:58.194035+00:00
---

# Cloud Spanner Instance Admin V1 API - Class Google::Cloud::Spanner::Admin::Instance::V1::InstanceAdmin::Client::Configuration::Rpcs (v2.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-instance-v1/latest/Google-Cloud-Spanner-Admin-Instance-V1-InstanceAdmin-Client-Configuration-Rpcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Spanner Instance Admin V1 API - Class Google::Cloud::Spanner::Admin::Instance::V1::InstanceAdmin::Client::Configuration::Rpcs (v2.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.8.1 (latest)  2.8.0  2.7.1  2.6.0  2.5.0  2.4.0  2.3.1  2.2.0  2.1.0  2.0.1  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.1  1.0.0  0.16.0  0.15.0  0.14.0  0.13.2  0.12.0  0.11.0  0.10.2  0.9.0  0.8.0  0.7.0  0.6.0  0.5.5 

Reference documentation and code samples for the Cloud Spanner Instance Admin V1 API class Google::Cloud::Spanner::Admin::Instance::V1::InstanceAdmin::Client::Configuration::Rpcs.

Configuration RPC class for the InstanceAdmin API.

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

### #create_instance
    
    
    def create_instance() -> ::Gapic::Config::Method

RPC-specific configuration for `create_instance`

**Returns**

  * (::Gapic::Config::Method) 



### #create_instance_config
    
    
    def create_instance_config() -> ::Gapic::Config::Method

RPC-specific configuration for `create_instance_config`

**Returns**

  * (::Gapic::Config::Method) 



### #create_instance_partition
    
    
    def create_instance_partition() -> ::Gapic::Config::Method

RPC-specific configuration for `create_instance_partition`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_instance
    
    
    def delete_instance() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_instance`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_instance_config
    
    
    def delete_instance_config() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_instance_config`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_instance_partition
    
    
    def delete_instance_partition() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_instance_partition`

**Returns**

  * (::Gapic::Config::Method) 



### #get_iam_policy
    
    
    def get_iam_policy() -> ::Gapic::Config::Method

RPC-specific configuration for `get_iam_policy`

**Returns**

  * (::Gapic::Config::Method) 



### #get_instance
    
    
    def get_instance() -> ::Gapic::Config::Method

RPC-specific configuration for `get_instance`

**Returns**

  * (::Gapic::Config::Method) 



### #get_instance_config
    
    
    def get_instance_config() -> ::Gapic::Config::Method

RPC-specific configuration for `get_instance_config`

**Returns**

  * (::Gapic::Config::Method) 



### #get_instance_partition
    
    
    def get_instance_partition() -> ::Gapic::Config::Method

RPC-specific configuration for `get_instance_partition`

**Returns**

  * (::Gapic::Config::Method) 



### #list_instance_config_operations
    
    
    def list_instance_config_operations() -> ::Gapic::Config::Method

RPC-specific configuration for `list_instance_config_operations`

**Returns**

  * (::Gapic::Config::Method) 



### #list_instance_configs
    
    
    def list_instance_configs() -> ::Gapic::Config::Method

RPC-specific configuration for `list_instance_configs`

**Returns**

  * (::Gapic::Config::Method) 



### #list_instance_partition_operations
    
    
    def list_instance_partition_operations() -> ::Gapic::Config::Method

RPC-specific configuration for `list_instance_partition_operations`

**Returns**

  * (::Gapic::Config::Method) 



### #list_instance_partitions
    
    
    def list_instance_partitions() -> ::Gapic::Config::Method

RPC-specific configuration for `list_instance_partitions`

**Returns**

  * (::Gapic::Config::Method) 



### #list_instances
    
    
    def list_instances() -> ::Gapic::Config::Method

RPC-specific configuration for `list_instances`

**Returns**

  * (::Gapic::Config::Method) 



### #move_instance
    
    
    def move_instance() -> ::Gapic::Config::Method

RPC-specific configuration for `move_instance`

**Returns**

  * (::Gapic::Config::Method) 



### #set_iam_policy
    
    
    def set_iam_policy() -> ::Gapic::Config::Method

RPC-specific configuration for `set_iam_policy`

**Returns**

  * (::Gapic::Config::Method) 



### #test_iam_permissions
    
    
    def test_iam_permissions() -> ::Gapic::Config::Method

RPC-specific configuration for `test_iam_permissions`

**Returns**

  * (::Gapic::Config::Method) 



### #update_instance
    
    
    def update_instance() -> ::Gapic::Config::Method

RPC-specific configuration for `update_instance`

**Returns**

  * (::Gapic::Config::Method) 



### #update_instance_config
    
    
    def update_instance_config() -> ::Gapic::Config::Method

RPC-specific configuration for `update_instance_config`

**Returns**

  * (::Gapic::Config::Method) 



### #update_instance_partition
    
    
    def update_instance_partition() -> ::Gapic::Config::Method

RPC-specific configuration for `update_instance_partition`

**Returns**

  * (::Gapic::Config::Method) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
