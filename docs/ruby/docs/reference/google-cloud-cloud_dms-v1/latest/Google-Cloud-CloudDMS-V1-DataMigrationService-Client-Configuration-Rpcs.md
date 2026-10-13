---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DataMigrationService-Client-Configuration-Rpcs/
title: Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::DataMigrationService::Client::Configuration::Rpcs (v1.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:35:25.076045+00:00
---

# Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::DataMigrationService::Client::Configuration::Rpcs (v1.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DataMigrationService-Client-Configuration-Rpcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::DataMigrationService::Client::Configuration::Rpcs (v1.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.1 (latest)  1.8.0  1.7.0  1.6.0  1.5.1  1.4.0  1.3.1  1.2.2  1.1.0  1.0.1  0.8.0  0.7.2  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.5 

Reference documentation and code samples for the Cloud Database Migration Service V1 API class Google::Cloud::CloudDMS::V1::DataMigrationService::Client::Configuration::Rpcs.

Configuration RPC class for the DataMigrationService API.

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

### #apply_conversion_workspace
    
    
    def apply_conversion_workspace() -> ::Gapic::Config::Method

RPC-specific configuration for `apply_conversion_workspace`

**Returns**

  * (::Gapic::Config::Method) 



### #commit_conversion_workspace
    
    
    def commit_conversion_workspace() -> ::Gapic::Config::Method

RPC-specific configuration for `commit_conversion_workspace`

**Returns**

  * (::Gapic::Config::Method) 



### #convert_conversion_workspace
    
    
    def convert_conversion_workspace() -> ::Gapic::Config::Method

RPC-specific configuration for `convert_conversion_workspace`

**Returns**

  * (::Gapic::Config::Method) 



### #create_connection_profile
    
    
    def create_connection_profile() -> ::Gapic::Config::Method

RPC-specific configuration for `create_connection_profile`

**Returns**

  * (::Gapic::Config::Method) 



### #create_conversion_workspace
    
    
    def create_conversion_workspace() -> ::Gapic::Config::Method

RPC-specific configuration for `create_conversion_workspace`

**Returns**

  * (::Gapic::Config::Method) 



### #create_mapping_rule
    
    
    def create_mapping_rule() -> ::Gapic::Config::Method

RPC-specific configuration for `create_mapping_rule`

**Returns**

  * (::Gapic::Config::Method) 



### #create_migration_job
    
    
    def create_migration_job() -> ::Gapic::Config::Method

RPC-specific configuration for `create_migration_job`

**Returns**

  * (::Gapic::Config::Method) 



### #create_private_connection
    
    
    def create_private_connection() -> ::Gapic::Config::Method

RPC-specific configuration for `create_private_connection`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_connection_profile
    
    
    def delete_connection_profile() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_connection_profile`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_conversion_workspace
    
    
    def delete_conversion_workspace() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_conversion_workspace`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_mapping_rule
    
    
    def delete_mapping_rule() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_mapping_rule`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_migration_job
    
    
    def delete_migration_job() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_migration_job`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_private_connection
    
    
    def delete_private_connection() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_private_connection`

**Returns**

  * (::Gapic::Config::Method) 



### #describe_conversion_workspace_revisions
    
    
    def describe_conversion_workspace_revisions() -> ::Gapic::Config::Method

RPC-specific configuration for `describe_conversion_workspace_revisions`

**Returns**

  * (::Gapic::Config::Method) 



### #describe_database_entities
    
    
    def describe_database_entities() -> ::Gapic::Config::Method

RPC-specific configuration for `describe_database_entities`

**Returns**

  * (::Gapic::Config::Method) 



### #fetch_static_ips
    
    
    def fetch_static_ips() -> ::Gapic::Config::Method

RPC-specific configuration for `fetch_static_ips`

**Returns**

  * (::Gapic::Config::Method) 



### #generate_ssh_script
    
    
    def generate_ssh_script() -> ::Gapic::Config::Method

RPC-specific configuration for `generate_ssh_script`

**Returns**

  * (::Gapic::Config::Method) 



### #generate_tcp_proxy_script
    
    
    def generate_tcp_proxy_script() -> ::Gapic::Config::Method

RPC-specific configuration for `generate_tcp_proxy_script`

**Returns**

  * (::Gapic::Config::Method) 



### #get_connection_profile
    
    
    def get_connection_profile() -> ::Gapic::Config::Method

RPC-specific configuration for `get_connection_profile`

**Returns**

  * (::Gapic::Config::Method) 



### #get_conversion_workspace
    
    
    def get_conversion_workspace() -> ::Gapic::Config::Method

RPC-specific configuration for `get_conversion_workspace`

**Returns**

  * (::Gapic::Config::Method) 



### #get_mapping_rule
    
    
    def get_mapping_rule() -> ::Gapic::Config::Method

RPC-specific configuration for `get_mapping_rule`

**Returns**

  * (::Gapic::Config::Method) 



### #get_migration_job
    
    
    def get_migration_job() -> ::Gapic::Config::Method

RPC-specific configuration for `get_migration_job`

**Returns**

  * (::Gapic::Config::Method) 



### #get_private_connection
    
    
    def get_private_connection() -> ::Gapic::Config::Method

RPC-specific configuration for `get_private_connection`

**Returns**

  * (::Gapic::Config::Method) 



### #import_mapping_rules
    
    
    def import_mapping_rules() -> ::Gapic::Config::Method

RPC-specific configuration for `import_mapping_rules`

**Returns**

  * (::Gapic::Config::Method) 



### #list_connection_profiles
    
    
    def list_connection_profiles() -> ::Gapic::Config::Method

RPC-specific configuration for `list_connection_profiles`

**Returns**

  * (::Gapic::Config::Method) 



### #list_conversion_workspaces
    
    
    def list_conversion_workspaces() -> ::Gapic::Config::Method

RPC-specific configuration for `list_conversion_workspaces`

**Returns**

  * (::Gapic::Config::Method) 



### #list_mapping_rules
    
    
    def list_mapping_rules() -> ::Gapic::Config::Method

RPC-specific configuration for `list_mapping_rules`

**Returns**

  * (::Gapic::Config::Method) 



### #list_migration_jobs
    
    
    def list_migration_jobs() -> ::Gapic::Config::Method

RPC-specific configuration for `list_migration_jobs`

**Returns**

  * (::Gapic::Config::Method) 



### #list_private_connections
    
    
    def list_private_connections() -> ::Gapic::Config::Method

RPC-specific configuration for `list_private_connections`

**Returns**

  * (::Gapic::Config::Method) 



### #promote_migration_job
    
    
    def promote_migration_job() -> ::Gapic::Config::Method

RPC-specific configuration for `promote_migration_job`

**Returns**

  * (::Gapic::Config::Method) 



### #restart_migration_job
    
    
    def restart_migration_job() -> ::Gapic::Config::Method

RPC-specific configuration for `restart_migration_job`

**Returns**

  * (::Gapic::Config::Method) 



### #resume_migration_job
    
    
    def resume_migration_job() -> ::Gapic::Config::Method

RPC-specific configuration for `resume_migration_job`

**Returns**

  * (::Gapic::Config::Method) 



### #rollback_conversion_workspace
    
    
    def rollback_conversion_workspace() -> ::Gapic::Config::Method

RPC-specific configuration for `rollback_conversion_workspace`

**Returns**

  * (::Gapic::Config::Method) 



### #search_background_jobs
    
    
    def search_background_jobs() -> ::Gapic::Config::Method

RPC-specific configuration for `search_background_jobs`

**Returns**

  * (::Gapic::Config::Method) 



### #seed_conversion_workspace
    
    
    def seed_conversion_workspace() -> ::Gapic::Config::Method

RPC-specific configuration for `seed_conversion_workspace`

**Returns**

  * (::Gapic::Config::Method) 



### #start_migration_job
    
    
    def start_migration_job() -> ::Gapic::Config::Method

RPC-specific configuration for `start_migration_job`

**Returns**

  * (::Gapic::Config::Method) 



### #stop_migration_job
    
    
    def stop_migration_job() -> ::Gapic::Config::Method

RPC-specific configuration for `stop_migration_job`

**Returns**

  * (::Gapic::Config::Method) 



### #update_connection_profile
    
    
    def update_connection_profile() -> ::Gapic::Config::Method

RPC-specific configuration for `update_connection_profile`

**Returns**

  * (::Gapic::Config::Method) 



### #update_conversion_workspace
    
    
    def update_conversion_workspace() -> ::Gapic::Config::Method

RPC-specific configuration for `update_conversion_workspace`

**Returns**

  * (::Gapic::Config::Method) 



### #update_migration_job
    
    
    def update_migration_job() -> ::Gapic::Config::Method

RPC-specific configuration for `update_migration_job`

**Returns**

  * (::Gapic::Config::Method) 



### #verify_migration_job
    
    
    def verify_migration_job() -> ::Gapic::Config::Method

RPC-specific configuration for `verify_migration_job`

**Returns**

  * (::Gapic::Config::Method) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
