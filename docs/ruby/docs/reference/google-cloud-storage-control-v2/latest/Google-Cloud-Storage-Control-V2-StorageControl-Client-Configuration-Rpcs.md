---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage-control-v2/latest/Google-Cloud-Storage-Control-V2-StorageControl-Client-Configuration-Rpcs/
title: Storage Control V2 API - Class Google::Cloud::Storage::Control::V2::StorageControl::Client::Configuration::Rpcs (v1.14.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:14:29.183944+00:00
---

# Storage Control V2 API - Class Google::Cloud::Storage::Control::V2::StorageControl::Client::Configuration::Rpcs (v1.14.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage-control-v2/latest/Google-Cloud-Storage-Control-V2-StorageControl-Client-Configuration-Rpcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Storage Control V2 API - Class Google::Cloud::Storage::Control::V2::StorageControl::Client::Configuration::Rpcs (v1.14.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.14.1 (latest)  1.14.0  1.13.1  1.12.0  1.11.0  1.10.1  1.9.0  1.8.1  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.1.1 

Reference documentation and code samples for the Storage Control V2 API class Google::Cloud::Storage::Control::V2::StorageControl::Client::Configuration::Rpcs.

Configuration RPC class for the StorageControl API.

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

### #create_anywhere_cache
    
    
    def create_anywhere_cache() -> ::Gapic::Config::Method

RPC-specific configuration for `create_anywhere_cache`

**Returns**

  * (::Gapic::Config::Method) 



### #create_folder
    
    
    def create_folder() -> ::Gapic::Config::Method

RPC-specific configuration for `create_folder`

**Returns**

  * (::Gapic::Config::Method) 



### #create_managed_folder
    
    
    def create_managed_folder() -> ::Gapic::Config::Method

RPC-specific configuration for `create_managed_folder`

**Returns**

  * (::Gapic::Config::Method) 



### #create_rapid_cache
    
    
    def create_rapid_cache() -> ::Gapic::Config::Method

RPC-specific configuration for `create_rapid_cache`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_folder
    
    
    def delete_folder() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_folder`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_folder_recursive
    
    
    def delete_folder_recursive() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_folder_recursive`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_managed_folder
    
    
    def delete_managed_folder() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_managed_folder`

**Returns**

  * (::Gapic::Config::Method) 



### #disable_anywhere_cache
    
    
    def disable_anywhere_cache() -> ::Gapic::Config::Method

RPC-specific configuration for `disable_anywhere_cache`

**Returns**

  * (::Gapic::Config::Method) 



### #disable_rapid_cache
    
    
    def disable_rapid_cache() -> ::Gapic::Config::Method

RPC-specific configuration for `disable_rapid_cache`

**Returns**

  * (::Gapic::Config::Method) 



### #get_anywhere_cache
    
    
    def get_anywhere_cache() -> ::Gapic::Config::Method

RPC-specific configuration for `get_anywhere_cache`

**Returns**

  * (::Gapic::Config::Method) 



### #get_folder
    
    
    def get_folder() -> ::Gapic::Config::Method

RPC-specific configuration for `get_folder`

**Returns**

  * (::Gapic::Config::Method) 



### #get_folder_intelligence_config
    
    
    def get_folder_intelligence_config() -> ::Gapic::Config::Method

RPC-specific configuration for `get_folder_intelligence_config`

**Returns**

  * (::Gapic::Config::Method) 



### #get_iam_policy
    
    
    def get_iam_policy() -> ::Gapic::Config::Method

RPC-specific configuration for `get_iam_policy`

**Returns**

  * (::Gapic::Config::Method) 



### #get_intelligence_finding
    
    
    def get_intelligence_finding() -> ::Gapic::Config::Method

RPC-specific configuration for `get_intelligence_finding`

**Returns**

  * (::Gapic::Config::Method) 



### #get_intelligence_finding_revision
    
    
    def get_intelligence_finding_revision() -> ::Gapic::Config::Method

RPC-specific configuration for `get_intelligence_finding_revision`

**Returns**

  * (::Gapic::Config::Method) 



### #get_managed_folder
    
    
    def get_managed_folder() -> ::Gapic::Config::Method

RPC-specific configuration for `get_managed_folder`

**Returns**

  * (::Gapic::Config::Method) 



### #get_organization_intelligence_config
    
    
    def get_organization_intelligence_config() -> ::Gapic::Config::Method

RPC-specific configuration for `get_organization_intelligence_config`

**Returns**

  * (::Gapic::Config::Method) 



### #get_project_intelligence_config
    
    
    def get_project_intelligence_config() -> ::Gapic::Config::Method

RPC-specific configuration for `get_project_intelligence_config`

**Returns**

  * (::Gapic::Config::Method) 



### #get_rapid_cache
    
    
    def get_rapid_cache() -> ::Gapic::Config::Method

RPC-specific configuration for `get_rapid_cache`

**Returns**

  * (::Gapic::Config::Method) 



### #get_storage_layout
    
    
    def get_storage_layout() -> ::Gapic::Config::Method

RPC-specific configuration for `get_storage_layout`

**Returns**

  * (::Gapic::Config::Method) 



### #list_anywhere_caches
    
    
    def list_anywhere_caches() -> ::Gapic::Config::Method

RPC-specific configuration for `list_anywhere_caches`

**Returns**

  * (::Gapic::Config::Method) 



### #list_folders
    
    
    def list_folders() -> ::Gapic::Config::Method

RPC-specific configuration for `list_folders`

**Returns**

  * (::Gapic::Config::Method) 



### #list_intelligence_finding_revisions
    
    
    def list_intelligence_finding_revisions() -> ::Gapic::Config::Method

RPC-specific configuration for `list_intelligence_finding_revisions`

**Returns**

  * (::Gapic::Config::Method) 



### #list_intelligence_findings
    
    
    def list_intelligence_findings() -> ::Gapic::Config::Method

RPC-specific configuration for `list_intelligence_findings`

**Returns**

  * (::Gapic::Config::Method) 



### #list_managed_folders
    
    
    def list_managed_folders() -> ::Gapic::Config::Method

RPC-specific configuration for `list_managed_folders`

**Returns**

  * (::Gapic::Config::Method) 



### #list_rapid_caches
    
    
    def list_rapid_caches() -> ::Gapic::Config::Method

RPC-specific configuration for `list_rapid_caches`

**Returns**

  * (::Gapic::Config::Method) 



### #pause_anywhere_cache
    
    
    def pause_anywhere_cache() -> ::Gapic::Config::Method

RPC-specific configuration for `pause_anywhere_cache`

**Returns**

  * (::Gapic::Config::Method) 



### #rename_folder
    
    
    def rename_folder() -> ::Gapic::Config::Method

RPC-specific configuration for `rename_folder`

**Returns**

  * (::Gapic::Config::Method) 



### #resume_anywhere_cache
    
    
    def resume_anywhere_cache() -> ::Gapic::Config::Method

RPC-specific configuration for `resume_anywhere_cache`

**Returns**

  * (::Gapic::Config::Method) 



### #set_iam_policy
    
    
    def set_iam_policy() -> ::Gapic::Config::Method

RPC-specific configuration for `set_iam_policy`

**Returns**

  * (::Gapic::Config::Method) 



### #summarize_intelligence_findings
    
    
    def summarize_intelligence_findings() -> ::Gapic::Config::Method

RPC-specific configuration for `summarize_intelligence_findings`

**Returns**

  * (::Gapic::Config::Method) 



### #test_iam_permissions
    
    
    def test_iam_permissions() -> ::Gapic::Config::Method

RPC-specific configuration for `test_iam_permissions`

**Returns**

  * (::Gapic::Config::Method) 



### #update_anywhere_cache
    
    
    def update_anywhere_cache() -> ::Gapic::Config::Method

RPC-specific configuration for `update_anywhere_cache`

**Returns**

  * (::Gapic::Config::Method) 



### #update_folder_intelligence_config
    
    
    def update_folder_intelligence_config() -> ::Gapic::Config::Method

RPC-specific configuration for `update_folder_intelligence_config`

**Returns**

  * (::Gapic::Config::Method) 



### #update_managed_folder
    
    
    def update_managed_folder() -> ::Gapic::Config::Method

RPC-specific configuration for `update_managed_folder`

**Returns**

  * (::Gapic::Config::Method) 



### #update_organization_intelligence_config
    
    
    def update_organization_intelligence_config() -> ::Gapic::Config::Method

RPC-specific configuration for `update_organization_intelligence_config`

**Returns**

  * (::Gapic::Config::Method) 



### #update_project_intelligence_config
    
    
    def update_project_intelligence_config() -> ::Gapic::Config::Method

RPC-specific configuration for `update_project_intelligence_config`

**Returns**

  * (::Gapic::Config::Method) 



### #update_rapid_cache
    
    
    def update_rapid_cache() -> ::Gapic::Config::Method

RPC-specific configuration for `update_rapid_cache`

**Returns**

  * (::Gapic::Config::Method) 



### #view_object_full_context
    
    
    def view_object_full_context() -> ::Gapic::Config::Method

RPC-specific configuration for `view_object_full_context`

**Returns**

  * (::Gapic::Config::Method) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
