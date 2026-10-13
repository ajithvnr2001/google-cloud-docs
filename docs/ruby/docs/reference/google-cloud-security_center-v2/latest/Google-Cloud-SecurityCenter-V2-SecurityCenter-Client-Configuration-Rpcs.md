---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-SecurityCenter-Client-Configuration-Rpcs/
title: Security Command Center V2 API - Class Google::Cloud::SecurityCenter::V2::SecurityCenter::Client::Configuration::Rpcs (v1.9.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:54:02.573211+00:00
---

# Security Command Center V2 API - Class Google::Cloud::SecurityCenter::V2::SecurityCenter::Client::Configuration::Rpcs (v1.9.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-SecurityCenter-Client-Configuration-Rpcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Security Command Center V2 API - Class Google::Cloud::SecurityCenter::V2::SecurityCenter::Client::Configuration::Rpcs (v1.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.9.1 (latest)  1.9.0  1.8.0  1.7.1  1.6.0  1.5.1  1.4.0  1.3.0  1.2.0  1.1.1  1.0.0  0.6.0  0.5.0  0.4.1  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Security Command Center V2 API class Google::Cloud::SecurityCenter::V2::SecurityCenter::Client::Configuration::Rpcs.

Configuration RPC class for the SecurityCenter API.

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

  * [Object](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter-V2-Kubernetes-Object)



## Methods 

### #batch_create_resource_value_configs
    
    
    def batch_create_resource_value_configs() -> ::Gapic::Config::Method

RPC-specific configuration for `batch_create_resource_value_configs`

**Returns**

  * (::Gapic::Config::Method) 



### #bulk_mute_findings
    
    
    def bulk_mute_findings() -> ::Gapic::Config::Method

RPC-specific configuration for `bulk_mute_findings`

**Returns**

  * (::Gapic::Config::Method) 



### #create_big_query_export
    
    
    def create_big_query_export() -> ::Gapic::Config::Method

RPC-specific configuration for `create_big_query_export`

**Returns**

  * (::Gapic::Config::Method) 



### #create_finding
    
    
    def create_finding() -> ::Gapic::Config::Method

RPC-specific configuration for `create_finding`

**Returns**

  * (::Gapic::Config::Method) 



### #create_mute_config
    
    
    def create_mute_config() -> ::Gapic::Config::Method

RPC-specific configuration for `create_mute_config`

**Returns**

  * (::Gapic::Config::Method) 



### #create_notification_config
    
    
    def create_notification_config() -> ::Gapic::Config::Method

RPC-specific configuration for `create_notification_config`

**Returns**

  * (::Gapic::Config::Method) 



### #create_source
    
    
    def create_source() -> ::Gapic::Config::Method

RPC-specific configuration for `create_source`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_big_query_export
    
    
    def delete_big_query_export() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_big_query_export`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_mute_config
    
    
    def delete_mute_config() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_mute_config`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_notification_config
    
    
    def delete_notification_config() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_notification_config`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_resource_value_config
    
    
    def delete_resource_value_config() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_resource_value_config`

**Returns**

  * (::Gapic::Config::Method) 



### #get_big_query_export
    
    
    def get_big_query_export() -> ::Gapic::Config::Method

RPC-specific configuration for `get_big_query_export`

**Returns**

  * (::Gapic::Config::Method) 



### #get_iam_policy
    
    
    def get_iam_policy() -> ::Gapic::Config::Method

RPC-specific configuration for `get_iam_policy`

**Returns**

  * (::Gapic::Config::Method) 



### #get_mute_config
    
    
    def get_mute_config() -> ::Gapic::Config::Method

RPC-specific configuration for `get_mute_config`

**Returns**

  * (::Gapic::Config::Method) 



### #get_notification_config
    
    
    def get_notification_config() -> ::Gapic::Config::Method

RPC-specific configuration for `get_notification_config`

**Returns**

  * (::Gapic::Config::Method) 



### #get_resource_value_config
    
    
    def get_resource_value_config() -> ::Gapic::Config::Method

RPC-specific configuration for `get_resource_value_config`

**Returns**

  * (::Gapic::Config::Method) 



### #get_simulation
    
    
    def get_simulation() -> ::Gapic::Config::Method

RPC-specific configuration for `get_simulation`

**Returns**

  * (::Gapic::Config::Method) 



### #get_source
    
    
    def get_source() -> ::Gapic::Config::Method

RPC-specific configuration for `get_source`

**Returns**

  * (::Gapic::Config::Method) 



### #get_valued_resource
    
    
    def get_valued_resource() -> ::Gapic::Config::Method

RPC-specific configuration for `get_valued_resource`

**Returns**

  * (::Gapic::Config::Method) 



### #group_findings
    
    
    def group_findings() -> ::Gapic::Config::Method

RPC-specific configuration for `group_findings`

**Returns**

  * (::Gapic::Config::Method) 



### #list_attack_paths
    
    
    def list_attack_paths() -> ::Gapic::Config::Method

RPC-specific configuration for `list_attack_paths`

**Returns**

  * (::Gapic::Config::Method) 



### #list_big_query_exports
    
    
    def list_big_query_exports() -> ::Gapic::Config::Method

RPC-specific configuration for `list_big_query_exports`

**Returns**

  * (::Gapic::Config::Method) 



### #list_findings
    
    
    def list_findings() -> ::Gapic::Config::Method

RPC-specific configuration for `list_findings`

**Returns**

  * (::Gapic::Config::Method) 



### #list_mute_configs
    
    
    def list_mute_configs() -> ::Gapic::Config::Method

RPC-specific configuration for `list_mute_configs`

**Returns**

  * (::Gapic::Config::Method) 



### #list_notification_configs
    
    
    def list_notification_configs() -> ::Gapic::Config::Method

RPC-specific configuration for `list_notification_configs`

**Returns**

  * (::Gapic::Config::Method) 



### #list_resource_value_configs
    
    
    def list_resource_value_configs() -> ::Gapic::Config::Method

RPC-specific configuration for `list_resource_value_configs`

**Returns**

  * (::Gapic::Config::Method) 



### #list_sources
    
    
    def list_sources() -> ::Gapic::Config::Method

RPC-specific configuration for `list_sources`

**Returns**

  * (::Gapic::Config::Method) 



### #list_valued_resources
    
    
    def list_valued_resources() -> ::Gapic::Config::Method

RPC-specific configuration for `list_valued_resources`

**Returns**

  * (::Gapic::Config::Method) 



### #set_finding_state
    
    
    def set_finding_state() -> ::Gapic::Config::Method

RPC-specific configuration for `set_finding_state`

**Returns**

  * (::Gapic::Config::Method) 



### #set_iam_policy
    
    
    def set_iam_policy() -> ::Gapic::Config::Method

RPC-specific configuration for `set_iam_policy`

**Returns**

  * (::Gapic::Config::Method) 



### #set_mute
    
    
    def set_mute() -> ::Gapic::Config::Method

RPC-specific configuration for `set_mute`

**Returns**

  * (::Gapic::Config::Method) 



### #test_iam_permissions
    
    
    def test_iam_permissions() -> ::Gapic::Config::Method

RPC-specific configuration for `test_iam_permissions`

**Returns**

  * (::Gapic::Config::Method) 



### #update_big_query_export
    
    
    def update_big_query_export() -> ::Gapic::Config::Method

RPC-specific configuration for `update_big_query_export`

**Returns**

  * (::Gapic::Config::Method) 



### #update_external_system
    
    
    def update_external_system() -> ::Gapic::Config::Method

RPC-specific configuration for `update_external_system`

**Returns**

  * (::Gapic::Config::Method) 



### #update_finding
    
    
    def update_finding() -> ::Gapic::Config::Method

RPC-specific configuration for `update_finding`

**Returns**

  * (::Gapic::Config::Method) 



### #update_mute_config
    
    
    def update_mute_config() -> ::Gapic::Config::Method

RPC-specific configuration for `update_mute_config`

**Returns**

  * (::Gapic::Config::Method) 



### #update_notification_config
    
    
    def update_notification_config() -> ::Gapic::Config::Method

RPC-specific configuration for `update_notification_config`

**Returns**

  * (::Gapic::Config::Method) 



### #update_resource_value_config
    
    
    def update_resource_value_config() -> ::Gapic::Config::Method

RPC-specific configuration for `update_resource_value_config`

**Returns**

  * (::Gapic::Config::Method) 



### #update_security_marks
    
    
    def update_security_marks() -> ::Gapic::Config::Method

RPC-specific configuration for `update_security_marks`

**Returns**

  * (::Gapic::Config::Method) 



### #update_source
    
    
    def update_source() -> ::Gapic::Config::Method

RPC-specific configuration for `update_source`

**Returns**

  * (::Gapic::Config::Method) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
