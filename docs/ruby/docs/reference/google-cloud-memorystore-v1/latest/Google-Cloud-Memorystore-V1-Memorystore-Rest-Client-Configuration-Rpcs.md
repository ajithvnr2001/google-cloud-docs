---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Cloud-Memorystore-V1-Memorystore-Rest-Client-Configuration-Rpcs/
title: Memorystore V1 API - Class Google::Cloud::Memorystore::V1::Memorystore::Rest::Client::Configuration::Rpcs (v1.11.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:20:17.442900+00:00
---

# Memorystore V1 API - Class Google::Cloud::Memorystore::V1::Memorystore::Rest::Client::Configuration::Rpcs (v1.11.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-memorystore-v1/latest/Google-Cloud-Memorystore-V1-Memorystore-Rest-Client-Configuration-Rpcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Memorystore V1 API - Class Google::Cloud::Memorystore::V1::Memorystore::Rest::Client::Configuration::Rpcs (v1.11.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.11.1 (latest)  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.1  1.0.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Memorystore V1 API class Google::Cloud::Memorystore::V1::Memorystore::Rest::Client::Configuration::Rpcs.

Configuration RPC class for the Memorystore API.

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

### #add_auth_token
    
    
    def add_auth_token() -> ::Gapic::Config::Method

RPC-specific configuration for `add_auth_token`

**Returns**

  * (::Gapic::Config::Method) 



### #add_token_auth_user
    
    
    def add_token_auth_user() -> ::Gapic::Config::Method

RPC-specific configuration for `add_token_auth_user`

**Returns**

  * (::Gapic::Config::Method) 



### #backup_instance
    
    
    def backup_instance() -> ::Gapic::Config::Method

RPC-specific configuration for `backup_instance`

**Returns**

  * (::Gapic::Config::Method) 



### #create_instance
    
    
    def create_instance() -> ::Gapic::Config::Method

RPC-specific configuration for `create_instance`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_auth_token
    
    
    def delete_auth_token() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_auth_token`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_backup
    
    
    def delete_backup() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_backup`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_instance
    
    
    def delete_instance() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_instance`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_token_auth_user
    
    
    def delete_token_auth_user() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_token_auth_user`

**Returns**

  * (::Gapic::Config::Method) 



### #export_backup
    
    
    def export_backup() -> ::Gapic::Config::Method

RPC-specific configuration for `export_backup`

**Returns**

  * (::Gapic::Config::Method) 



### #finish_migration
    
    
    def finish_migration() -> ::Gapic::Config::Method

RPC-specific configuration for `finish_migration`

**Returns**

  * (::Gapic::Config::Method) 



### #get_auth_token
    
    
    def get_auth_token() -> ::Gapic::Config::Method

RPC-specific configuration for `get_auth_token`

**Returns**

  * (::Gapic::Config::Method) 



### #get_backup
    
    
    def get_backup() -> ::Gapic::Config::Method

RPC-specific configuration for `get_backup`

**Returns**

  * (::Gapic::Config::Method) 



### #get_backup_collection
    
    
    def get_backup_collection() -> ::Gapic::Config::Method

RPC-specific configuration for `get_backup_collection`

**Returns**

  * (::Gapic::Config::Method) 



### #get_certificate_authority
    
    
    def get_certificate_authority() -> ::Gapic::Config::Method

RPC-specific configuration for `get_certificate_authority`

**Returns**

  * (::Gapic::Config::Method) 



### #get_instance
    
    
    def get_instance() -> ::Gapic::Config::Method

RPC-specific configuration for `get_instance`

**Returns**

  * (::Gapic::Config::Method) 



### #get_shared_regional_certificate_authority
    
    
    def get_shared_regional_certificate_authority() -> ::Gapic::Config::Method

RPC-specific configuration for `get_shared_regional_certificate_authority`

**Returns**

  * (::Gapic::Config::Method) 



### #get_token_auth_user
    
    
    def get_token_auth_user() -> ::Gapic::Config::Method

RPC-specific configuration for `get_token_auth_user`

**Returns**

  * (::Gapic::Config::Method) 



### #list_auth_tokens
    
    
    def list_auth_tokens() -> ::Gapic::Config::Method

RPC-specific configuration for `list_auth_tokens`

**Returns**

  * (::Gapic::Config::Method) 



### #list_backup_collections
    
    
    def list_backup_collections() -> ::Gapic::Config::Method

RPC-specific configuration for `list_backup_collections`

**Returns**

  * (::Gapic::Config::Method) 



### #list_backups
    
    
    def list_backups() -> ::Gapic::Config::Method

RPC-specific configuration for `list_backups`

**Returns**

  * (::Gapic::Config::Method) 



### #list_instances
    
    
    def list_instances() -> ::Gapic::Config::Method

RPC-specific configuration for `list_instances`

**Returns**

  * (::Gapic::Config::Method) 



### #list_token_auth_users
    
    
    def list_token_auth_users() -> ::Gapic::Config::Method

RPC-specific configuration for `list_token_auth_users`

**Returns**

  * (::Gapic::Config::Method) 



### #reschedule_maintenance
    
    
    def reschedule_maintenance() -> ::Gapic::Config::Method

RPC-specific configuration for `reschedule_maintenance`

**Returns**

  * (::Gapic::Config::Method) 



### #start_migration
    
    
    def start_migration() -> ::Gapic::Config::Method

RPC-specific configuration for `start_migration`

**Returns**

  * (::Gapic::Config::Method) 



### #update_instance
    
    
    def update_instance() -> ::Gapic::Config::Method

RPC-specific configuration for `update_instance`

**Returns**

  * (::Gapic::Config::Method) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
