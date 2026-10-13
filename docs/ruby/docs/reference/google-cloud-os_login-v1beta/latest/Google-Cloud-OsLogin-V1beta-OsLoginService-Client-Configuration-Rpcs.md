---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_login-v1beta/latest/Google-Cloud-OsLogin-V1beta-OsLoginService-Client-Configuration-Rpcs/
title: Cloud OS Login V1beta API - Class Google::Cloud::OsLogin::V1beta::OsLoginService::Client::Configuration::Rpcs (v0.22.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:21:19.471888+00:00
---

# Cloud OS Login V1beta API - Class Google::Cloud::OsLogin::V1beta::OsLoginService::Client::Configuration::Rpcs (v0.22.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_login-v1beta/latest/Google-Cloud-OsLogin-V1beta-OsLoginService-Client-Configuration-Rpcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud OS Login V1beta API - Class Google::Cloud::OsLogin::V1beta::OsLoginService::Client::Configuration::Rpcs (v0.22.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.22.0 (latest)  0.21.1  0.20.0  0.19.1  0.18.0  0.17.2  0.16.0  0.15.2  0.14.2  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.5 

Reference documentation and code samples for the Cloud OS Login V1beta API class Google::Cloud::OsLogin::V1beta::OsLoginService::Client::Configuration::Rpcs.

Configuration RPC class for the OsLoginService API.

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

### #create_ssh_public_key
    
    
    def create_ssh_public_key() -> ::Gapic::Config::Method

RPC-specific configuration for `create_ssh_public_key`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_posix_account
    
    
    def delete_posix_account() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_posix_account`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_ssh_public_key
    
    
    def delete_ssh_public_key() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_ssh_public_key`

**Returns**

  * (::Gapic::Config::Method) 



### #get_login_profile
    
    
    def get_login_profile() -> ::Gapic::Config::Method

RPC-specific configuration for `get_login_profile`

**Returns**

  * (::Gapic::Config::Method) 



### #get_ssh_public_key
    
    
    def get_ssh_public_key() -> ::Gapic::Config::Method

RPC-specific configuration for `get_ssh_public_key`

**Returns**

  * (::Gapic::Config::Method) 



### #import_ssh_public_key
    
    
    def import_ssh_public_key() -> ::Gapic::Config::Method

RPC-specific configuration for `import_ssh_public_key`

**Returns**

  * (::Gapic::Config::Method) 



### #sign_ssh_public_key
    
    
    def sign_ssh_public_key() -> ::Gapic::Config::Method

RPC-specific configuration for `sign_ssh_public_key`

**Returns**

  * (::Gapic::Config::Method) 



### #update_ssh_public_key
    
    
    def update_ssh_public_key() -> ::Gapic::Config::Method

RPC-specific configuration for `update_ssh_public_key`

**Returns**

  * (::Gapic::Config::Method) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
