---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupDR-Rest-Client-Configuration-Rpcs/
title: Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::BackupDR::Rest::Client::Configuration::Rpcs (v1.11.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:58:23.062198+00:00
---

# Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::BackupDR::Rest::Client::Configuration::Rpcs (v1.11.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupDR-Rest-Client-Configuration-Rpcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::BackupDR::Rest::Client::Configuration::Rpcs (v1.11.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.11.2 (latest)  1.11.1  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.5.0  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Backup and DR Service V1 API class Google::Cloud::BackupDR::V1::BackupDR::Rest::Client::Configuration::Rpcs.

Configuration RPC class for the BackupDR API.

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

### #create_backup_plan
    
    
    def create_backup_plan() -> ::Gapic::Config::Method

RPC-specific configuration for `create_backup_plan`

**Returns**

  * (::Gapic::Config::Method) 



### #create_backup_plan_association
    
    
    def create_backup_plan_association() -> ::Gapic::Config::Method

RPC-specific configuration for `create_backup_plan_association`

**Returns**

  * (::Gapic::Config::Method) 



### #create_backup_vault
    
    
    def create_backup_vault() -> ::Gapic::Config::Method

RPC-specific configuration for `create_backup_vault`

**Returns**

  * (::Gapic::Config::Method) 



### #create_management_server
    
    
    def create_management_server() -> ::Gapic::Config::Method

RPC-specific configuration for `create_management_server`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_backup
    
    
    def delete_backup() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_backup`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_backup_plan
    
    
    def delete_backup_plan() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_backup_plan`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_backup_plan_association
    
    
    def delete_backup_plan_association() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_backup_plan_association`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_backup_vault
    
    
    def delete_backup_vault() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_backup_vault`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_management_server
    
    
    def delete_management_server() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_management_server`

**Returns**

  * (::Gapic::Config::Method) 



### #fetch_backup_plan_associations_for_resource_type
    
    
    def fetch_backup_plan_associations_for_resource_type() -> ::Gapic::Config::Method

RPC-specific configuration for `fetch_backup_plan_associations_for_resource_type`

**Returns**

  * (::Gapic::Config::Method) 



### #fetch_backups_for_resource_type
    
    
    def fetch_backups_for_resource_type() -> ::Gapic::Config::Method

RPC-specific configuration for `fetch_backups_for_resource_type`

**Returns**

  * (::Gapic::Config::Method) 



### #fetch_data_source_references_for_resource_type
    
    
    def fetch_data_source_references_for_resource_type() -> ::Gapic::Config::Method

RPC-specific configuration for `fetch_data_source_references_for_resource_type`

**Returns**

  * (::Gapic::Config::Method) 



### #fetch_usable_backup_vaults
    
    
    def fetch_usable_backup_vaults() -> ::Gapic::Config::Method

RPC-specific configuration for `fetch_usable_backup_vaults`

**Returns**

  * (::Gapic::Config::Method) 



### #get_backup
    
    
    def get_backup() -> ::Gapic::Config::Method

RPC-specific configuration for `get_backup`

**Returns**

  * (::Gapic::Config::Method) 



### #get_backup_plan
    
    
    def get_backup_plan() -> ::Gapic::Config::Method

RPC-specific configuration for `get_backup_plan`

**Returns**

  * (::Gapic::Config::Method) 



### #get_backup_plan_association
    
    
    def get_backup_plan_association() -> ::Gapic::Config::Method

RPC-specific configuration for `get_backup_plan_association`

**Returns**

  * (::Gapic::Config::Method) 



### #get_backup_plan_revision
    
    
    def get_backup_plan_revision() -> ::Gapic::Config::Method

RPC-specific configuration for `get_backup_plan_revision`

**Returns**

  * (::Gapic::Config::Method) 



### #get_backup_vault
    
    
    def get_backup_vault() -> ::Gapic::Config::Method

RPC-specific configuration for `get_backup_vault`

**Returns**

  * (::Gapic::Config::Method) 



### #get_data_source
    
    
    def get_data_source() -> ::Gapic::Config::Method

RPC-specific configuration for `get_data_source`

**Returns**

  * (::Gapic::Config::Method) 



### #get_data_source_reference
    
    
    def get_data_source_reference() -> ::Gapic::Config::Method

RPC-specific configuration for `get_data_source_reference`

**Returns**

  * (::Gapic::Config::Method) 



### #get_management_server
    
    
    def get_management_server() -> ::Gapic::Config::Method

RPC-specific configuration for `get_management_server`

**Returns**

  * (::Gapic::Config::Method) 



### #initialize_service
    
    
    def initialize_service() -> ::Gapic::Config::Method

RPC-specific configuration for `initialize_service`

**Returns**

  * (::Gapic::Config::Method) 



### #list_backup_plan_associations
    
    
    def list_backup_plan_associations() -> ::Gapic::Config::Method

RPC-specific configuration for `list_backup_plan_associations`

**Returns**

  * (::Gapic::Config::Method) 



### #list_backup_plan_revisions
    
    
    def list_backup_plan_revisions() -> ::Gapic::Config::Method

RPC-specific configuration for `list_backup_plan_revisions`

**Returns**

  * (::Gapic::Config::Method) 



### #list_backup_plans
    
    
    def list_backup_plans() -> ::Gapic::Config::Method

RPC-specific configuration for `list_backup_plans`

**Returns**

  * (::Gapic::Config::Method) 



### #list_backup_vaults
    
    
    def list_backup_vaults() -> ::Gapic::Config::Method

RPC-specific configuration for `list_backup_vaults`

**Returns**

  * (::Gapic::Config::Method) 



### #list_backups
    
    
    def list_backups() -> ::Gapic::Config::Method

RPC-specific configuration for `list_backups`

**Returns**

  * (::Gapic::Config::Method) 



### #list_data_source_references
    
    
    def list_data_source_references() -> ::Gapic::Config::Method

RPC-specific configuration for `list_data_source_references`

**Returns**

  * (::Gapic::Config::Method) 



### #list_data_sources
    
    
    def list_data_sources() -> ::Gapic::Config::Method

RPC-specific configuration for `list_data_sources`

**Returns**

  * (::Gapic::Config::Method) 



### #list_management_servers
    
    
    def list_management_servers() -> ::Gapic::Config::Method

RPC-specific configuration for `list_management_servers`

**Returns**

  * (::Gapic::Config::Method) 



### #restore_backup
    
    
    def restore_backup() -> ::Gapic::Config::Method

RPC-specific configuration for `restore_backup`

**Returns**

  * (::Gapic::Config::Method) 



### #trigger_backup
    
    
    def trigger_backup() -> ::Gapic::Config::Method

RPC-specific configuration for `trigger_backup`

**Returns**

  * (::Gapic::Config::Method) 



### #update_backup
    
    
    def update_backup() -> ::Gapic::Config::Method

RPC-specific configuration for `update_backup`

**Returns**

  * (::Gapic::Config::Method) 



### #update_backup_plan
    
    
    def update_backup_plan() -> ::Gapic::Config::Method

RPC-specific configuration for `update_backup_plan`

**Returns**

  * (::Gapic::Config::Method) 



### #update_backup_plan_association
    
    
    def update_backup_plan_association() -> ::Gapic::Config::Method

RPC-specific configuration for `update_backup_plan_association`

**Returns**

  * (::Gapic::Config::Method) 



### #update_backup_vault
    
    
    def update_backup_vault() -> ::Gapic::Config::Method

RPC-specific configuration for `update_backup_vault`

**Returns**

  * (::Gapic::Config::Method) 



### #update_data_source
    
    
    def update_data_source() -> ::Gapic::Config::Method

RPC-specific configuration for `update_data_source`

**Returns**

  * (::Gapic::Config::Method) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
