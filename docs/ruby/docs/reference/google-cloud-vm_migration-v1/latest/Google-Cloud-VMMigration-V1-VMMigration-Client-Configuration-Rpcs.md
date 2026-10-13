---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vm_migration-v1/latest/Google-Cloud-VMMigration-V1-VMMigration-Client-Configuration-Rpcs/
title: Migrate for Compute Engine V1 API - Class Google::Cloud::VMMigration::V1::VMMigration::Client::Configuration::Rpcs (v2.9.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:06:43.607815+00:00
---

# Migrate for Compute Engine V1 API - Class Google::Cloud::VMMigration::V1::VMMigration::Client::Configuration::Rpcs (v2.9.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vm_migration-v1/latest/Google-Cloud-VMMigration-V1-VMMigration-Client-Configuration-Rpcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Migrate for Compute Engine V1 API - Class Google::Cloud::VMMigration::V1::VMMigration::Client::Configuration::Rpcs (v2.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.9.1 (latest)  2.9.0  2.8.0  2.7.0  2.6.0  2.5.1  2.4.0  2.3.0  2.2.0  2.1.1  2.0.0  1.3.0  1.2.0  1.1.0  1.0.2  0.9.0  0.8.2  0.7.0  0.6.1  0.5.0  0.4.0  0.3.0  0.2.0  0.1.1 

Reference documentation and code samples for the Migrate for Compute Engine V1 API class Google::Cloud::VMMigration::V1::VMMigration::Client::Configuration::Rpcs.

Configuration RPC class for the VmMigration API.

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

### #add_group_migration
    
    
    def add_group_migration() -> ::Gapic::Config::Method

RPC-specific configuration for `add_group_migration`

**Returns**

  * (::Gapic::Config::Method) 



### #cancel_clone_job
    
    
    def cancel_clone_job() -> ::Gapic::Config::Method

RPC-specific configuration for `cancel_clone_job`

**Returns**

  * (::Gapic::Config::Method) 



### #cancel_cutover_job
    
    
    def cancel_cutover_job() -> ::Gapic::Config::Method

RPC-specific configuration for `cancel_cutover_job`

**Returns**

  * (::Gapic::Config::Method) 



### #cancel_disk_migration_job
    
    
    def cancel_disk_migration_job() -> ::Gapic::Config::Method

RPC-specific configuration for `cancel_disk_migration_job`

**Returns**

  * (::Gapic::Config::Method) 



### #cancel_image_import_job
    
    
    def cancel_image_import_job() -> ::Gapic::Config::Method

RPC-specific configuration for `cancel_image_import_job`

**Returns**

  * (::Gapic::Config::Method) 



### #create_clone_job
    
    
    def create_clone_job() -> ::Gapic::Config::Method

RPC-specific configuration for `create_clone_job`

**Returns**

  * (::Gapic::Config::Method) 



### #create_cutover_job
    
    
    def create_cutover_job() -> ::Gapic::Config::Method

RPC-specific configuration for `create_cutover_job`

**Returns**

  * (::Gapic::Config::Method) 



### #create_datacenter_connector
    
    
    def create_datacenter_connector() -> ::Gapic::Config::Method

RPC-specific configuration for `create_datacenter_connector`

**Returns**

  * (::Gapic::Config::Method) 



### #create_disk_migration_job
    
    
    def create_disk_migration_job() -> ::Gapic::Config::Method

RPC-specific configuration for `create_disk_migration_job`

**Returns**

  * (::Gapic::Config::Method) 



### #create_group
    
    
    def create_group() -> ::Gapic::Config::Method

RPC-specific configuration for `create_group`

**Returns**

  * (::Gapic::Config::Method) 



### #create_image_import
    
    
    def create_image_import() -> ::Gapic::Config::Method

RPC-specific configuration for `create_image_import`

**Returns**

  * (::Gapic::Config::Method) 



### #create_migrating_vm
    
    
    def create_migrating_vm() -> ::Gapic::Config::Method

RPC-specific configuration for `create_migrating_vm`

**Returns**

  * (::Gapic::Config::Method) 



### #create_source
    
    
    def create_source() -> ::Gapic::Config::Method

RPC-specific configuration for `create_source`

**Returns**

  * (::Gapic::Config::Method) 



### #create_target_project
    
    
    def create_target_project() -> ::Gapic::Config::Method

RPC-specific configuration for `create_target_project`

**Returns**

  * (::Gapic::Config::Method) 



### #create_utilization_report
    
    
    def create_utilization_report() -> ::Gapic::Config::Method

RPC-specific configuration for `create_utilization_report`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_datacenter_connector
    
    
    def delete_datacenter_connector() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_datacenter_connector`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_disk_migration_job
    
    
    def delete_disk_migration_job() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_disk_migration_job`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_group
    
    
    def delete_group() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_group`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_image_import
    
    
    def delete_image_import() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_image_import`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_migrating_vm
    
    
    def delete_migrating_vm() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_migrating_vm`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_source
    
    
    def delete_source() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_source`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_target_project
    
    
    def delete_target_project() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_target_project`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_utilization_report
    
    
    def delete_utilization_report() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_utilization_report`

**Returns**

  * (::Gapic::Config::Method) 



### #extend_migration
    
    
    def extend_migration() -> ::Gapic::Config::Method

RPC-specific configuration for `extend_migration`

**Returns**

  * (::Gapic::Config::Method) 



### #fetch_inventory
    
    
    def fetch_inventory() -> ::Gapic::Config::Method

RPC-specific configuration for `fetch_inventory`

**Returns**

  * (::Gapic::Config::Method) 



### #fetch_storage_inventory
    
    
    def fetch_storage_inventory() -> ::Gapic::Config::Method

RPC-specific configuration for `fetch_storage_inventory`

**Returns**

  * (::Gapic::Config::Method) 



### #finalize_migration
    
    
    def finalize_migration() -> ::Gapic::Config::Method

RPC-specific configuration for `finalize_migration`

**Returns**

  * (::Gapic::Config::Method) 



### #get_clone_job
    
    
    def get_clone_job() -> ::Gapic::Config::Method

RPC-specific configuration for `get_clone_job`

**Returns**

  * (::Gapic::Config::Method) 



### #get_cutover_job
    
    
    def get_cutover_job() -> ::Gapic::Config::Method

RPC-specific configuration for `get_cutover_job`

**Returns**

  * (::Gapic::Config::Method) 



### #get_datacenter_connector
    
    
    def get_datacenter_connector() -> ::Gapic::Config::Method

RPC-specific configuration for `get_datacenter_connector`

**Returns**

  * (::Gapic::Config::Method) 



### #get_disk_migration_job
    
    
    def get_disk_migration_job() -> ::Gapic::Config::Method

RPC-specific configuration for `get_disk_migration_job`

**Returns**

  * (::Gapic::Config::Method) 



### #get_group
    
    
    def get_group() -> ::Gapic::Config::Method

RPC-specific configuration for `get_group`

**Returns**

  * (::Gapic::Config::Method) 



### #get_image_import
    
    
    def get_image_import() -> ::Gapic::Config::Method

RPC-specific configuration for `get_image_import`

**Returns**

  * (::Gapic::Config::Method) 



### #get_image_import_job
    
    
    def get_image_import_job() -> ::Gapic::Config::Method

RPC-specific configuration for `get_image_import_job`

**Returns**

  * (::Gapic::Config::Method) 



### #get_migrating_vm
    
    
    def get_migrating_vm() -> ::Gapic::Config::Method

RPC-specific configuration for `get_migrating_vm`

**Returns**

  * (::Gapic::Config::Method) 



### #get_replication_cycle
    
    
    def get_replication_cycle() -> ::Gapic::Config::Method

RPC-specific configuration for `get_replication_cycle`

**Returns**

  * (::Gapic::Config::Method) 



### #get_source
    
    
    def get_source() -> ::Gapic::Config::Method

RPC-specific configuration for `get_source`

**Returns**

  * (::Gapic::Config::Method) 



### #get_target_project
    
    
    def get_target_project() -> ::Gapic::Config::Method

RPC-specific configuration for `get_target_project`

**Returns**

  * (::Gapic::Config::Method) 



### #get_utilization_report
    
    
    def get_utilization_report() -> ::Gapic::Config::Method

RPC-specific configuration for `get_utilization_report`

**Returns**

  * (::Gapic::Config::Method) 



### #list_clone_jobs
    
    
    def list_clone_jobs() -> ::Gapic::Config::Method

RPC-specific configuration for `list_clone_jobs`

**Returns**

  * (::Gapic::Config::Method) 



### #list_cutover_jobs
    
    
    def list_cutover_jobs() -> ::Gapic::Config::Method

RPC-specific configuration for `list_cutover_jobs`

**Returns**

  * (::Gapic::Config::Method) 



### #list_datacenter_connectors
    
    
    def list_datacenter_connectors() -> ::Gapic::Config::Method

RPC-specific configuration for `list_datacenter_connectors`

**Returns**

  * (::Gapic::Config::Method) 



### #list_disk_migration_jobs
    
    
    def list_disk_migration_jobs() -> ::Gapic::Config::Method

RPC-specific configuration for `list_disk_migration_jobs`

**Returns**

  * (::Gapic::Config::Method) 



### #list_groups
    
    
    def list_groups() -> ::Gapic::Config::Method

RPC-specific configuration for `list_groups`

**Returns**

  * (::Gapic::Config::Method) 



### #list_image_import_jobs
    
    
    def list_image_import_jobs() -> ::Gapic::Config::Method

RPC-specific configuration for `list_image_import_jobs`

**Returns**

  * (::Gapic::Config::Method) 



### #list_image_imports
    
    
    def list_image_imports() -> ::Gapic::Config::Method

RPC-specific configuration for `list_image_imports`

**Returns**

  * (::Gapic::Config::Method) 



### #list_migrating_vms
    
    
    def list_migrating_vms() -> ::Gapic::Config::Method

RPC-specific configuration for `list_migrating_vms`

**Returns**

  * (::Gapic::Config::Method) 



### #list_replication_cycles
    
    
    def list_replication_cycles() -> ::Gapic::Config::Method

RPC-specific configuration for `list_replication_cycles`

**Returns**

  * (::Gapic::Config::Method) 



### #list_sources
    
    
    def list_sources() -> ::Gapic::Config::Method

RPC-specific configuration for `list_sources`

**Returns**

  * (::Gapic::Config::Method) 



### #list_target_projects
    
    
    def list_target_projects() -> ::Gapic::Config::Method

RPC-specific configuration for `list_target_projects`

**Returns**

  * (::Gapic::Config::Method) 



### #list_utilization_reports
    
    
    def list_utilization_reports() -> ::Gapic::Config::Method

RPC-specific configuration for `list_utilization_reports`

**Returns**

  * (::Gapic::Config::Method) 



### #pause_migration
    
    
    def pause_migration() -> ::Gapic::Config::Method

RPC-specific configuration for `pause_migration`

**Returns**

  * (::Gapic::Config::Method) 



### #remove_group_migration
    
    
    def remove_group_migration() -> ::Gapic::Config::Method

RPC-specific configuration for `remove_group_migration`

**Returns**

  * (::Gapic::Config::Method) 



### #resume_migration
    
    
    def resume_migration() -> ::Gapic::Config::Method

RPC-specific configuration for `resume_migration`

**Returns**

  * (::Gapic::Config::Method) 



### #run_disk_migration_job
    
    
    def run_disk_migration_job() -> ::Gapic::Config::Method

RPC-specific configuration for `run_disk_migration_job`

**Returns**

  * (::Gapic::Config::Method) 



### #start_migration
    
    
    def start_migration() -> ::Gapic::Config::Method

RPC-specific configuration for `start_migration`

**Returns**

  * (::Gapic::Config::Method) 



### #update_disk_migration_job
    
    
    def update_disk_migration_job() -> ::Gapic::Config::Method

RPC-specific configuration for `update_disk_migration_job`

**Returns**

  * (::Gapic::Config::Method) 



### #update_group
    
    
    def update_group() -> ::Gapic::Config::Method

RPC-specific configuration for `update_group`

**Returns**

  * (::Gapic::Config::Method) 



### #update_migrating_vm
    
    
    def update_migrating_vm() -> ::Gapic::Config::Method

RPC-specific configuration for `update_migrating_vm`

**Returns**

  * (::Gapic::Config::Method) 



### #update_source
    
    
    def update_source() -> ::Gapic::Config::Method

RPC-specific configuration for `update_source`

**Returns**

  * (::Gapic::Config::Method) 



### #update_target_project
    
    
    def update_target_project() -> ::Gapic::Config::Method

RPC-specific configuration for `update_target_project`

**Returns**

  * (::Gapic::Config::Method) 



### #upgrade_appliance
    
    
    def upgrade_appliance() -> ::Gapic::Config::Method

RPC-specific configuration for `upgrade_appliance`

**Returns**

  * (::Gapic::Config::Method) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
