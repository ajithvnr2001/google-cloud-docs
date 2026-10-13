---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-privileged_access_manager-v1/latest/Google-Cloud-PrivilegedAccessManager-V1-PrivilegedAccessManager-Rest-Client-Configuration-Rpcs/
title: Privileged Access Manager V1 API - Class Google::Cloud::PrivilegedAccessManager::V1::PrivilegedAccessManager::Rest::Client::Configuration::Rpcs (v1.7.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:22:19.399571+00:00
---

# Privileged Access Manager V1 API - Class Google::Cloud::PrivilegedAccessManager::V1::PrivilegedAccessManager::Rest::Client::Configuration::Rpcs (v1.7.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-privileged_access_manager-v1/latest/Google-Cloud-PrivilegedAccessManager-V1-PrivilegedAccessManager-Rest-Client-Configuration-Rpcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Privileged Access Manager V1 API - Class Google::Cloud::PrivilegedAccessManager::V1::PrivilegedAccessManager::Rest::Client::Configuration::Rpcs (v1.7.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.7.2 (latest)  1.7.0  1.6.1  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.3.0  0.2.0  0.1.2 

Reference documentation and code samples for the Privileged Access Manager V1 API class Google::Cloud::PrivilegedAccessManager::V1::PrivilegedAccessManager::Rest::Client::Configuration::Rpcs.

Configuration RPC class for the PrivilegedAccessManager API.

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

### #approve_grant
    
    
    def approve_grant() -> ::Gapic::Config::Method

RPC-specific configuration for `approve_grant`

**Returns**

  * (::Gapic::Config::Method) 



### #check_onboarding_status
    
    
    def check_onboarding_status() -> ::Gapic::Config::Method

RPC-specific configuration for `check_onboarding_status`

**Returns**

  * (::Gapic::Config::Method) 



### #create_entitlement
    
    
    def create_entitlement() -> ::Gapic::Config::Method

RPC-specific configuration for `create_entitlement`

**Returns**

  * (::Gapic::Config::Method) 



### #create_grant
    
    
    def create_grant() -> ::Gapic::Config::Method

RPC-specific configuration for `create_grant`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_entitlement
    
    
    def delete_entitlement() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_entitlement`

**Returns**

  * (::Gapic::Config::Method) 



### #deny_grant
    
    
    def deny_grant() -> ::Gapic::Config::Method

RPC-specific configuration for `deny_grant`

**Returns**

  * (::Gapic::Config::Method) 



### #get_entitlement
    
    
    def get_entitlement() -> ::Gapic::Config::Method

RPC-specific configuration for `get_entitlement`

**Returns**

  * (::Gapic::Config::Method) 



### #get_grant
    
    
    def get_grant() -> ::Gapic::Config::Method

RPC-specific configuration for `get_grant`

**Returns**

  * (::Gapic::Config::Method) 



### #list_entitlements
    
    
    def list_entitlements() -> ::Gapic::Config::Method

RPC-specific configuration for `list_entitlements`

**Returns**

  * (::Gapic::Config::Method) 



### #list_grants
    
    
    def list_grants() -> ::Gapic::Config::Method

RPC-specific configuration for `list_grants`

**Returns**

  * (::Gapic::Config::Method) 



### #revoke_grant
    
    
    def revoke_grant() -> ::Gapic::Config::Method

RPC-specific configuration for `revoke_grant`

**Returns**

  * (::Gapic::Config::Method) 



### #search_entitlements
    
    
    def search_entitlements() -> ::Gapic::Config::Method

RPC-specific configuration for `search_entitlements`

**Returns**

  * (::Gapic::Config::Method) 



### #search_grants
    
    
    def search_grants() -> ::Gapic::Config::Method

RPC-specific configuration for `search_grants`

**Returns**

  * (::Gapic::Config::Method) 



### #update_entitlement
    
    
    def update_entitlement() -> ::Gapic::Config::Method

RPC-specific configuration for `update_entitlement`

**Returns**

  * (::Gapic::Config::Method) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
