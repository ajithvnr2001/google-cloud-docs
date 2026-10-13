---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_security_compliance-v1/latest/Google-Cloud-CloudSecurityCompliance-V1-Config-Rest-Client-Configuration-Rpcs/
title: Cloud Security Compliance V1 API - Class Google::Cloud::CloudSecurityCompliance::V1::Config::Rest::Client::Configuration::Rpcs (v1.0.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:52:43.690256+00:00
---

# Cloud Security Compliance V1 API - Class Google::Cloud::CloudSecurityCompliance::V1::Config::Rest::Client::Configuration::Rpcs (v1.0.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_security_compliance-v1/latest/Google-Cloud-CloudSecurityCompliance-V1-Config-Rest-Client-Configuration-Rpcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Security Compliance V1 API - Class Google::Cloud::CloudSecurityCompliance::V1::Config::Rest::Client::Configuration::Rpcs (v1.0.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.1 (latest)  1.0.0  0.5.0  0.4.1  0.3.0  0.2.0  0.1.1 

Reference documentation and code samples for the Cloud Security Compliance V1 API class Google::Cloud::CloudSecurityCompliance::V1::Config::Rest::Client::Configuration::Rpcs.

Configuration RPC class for the Config API.

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

### #create_cloud_control
    
    
    def create_cloud_control() -> ::Gapic::Config::Method

RPC-specific configuration for `create_cloud_control`

**Returns**

  * (::Gapic::Config::Method) 



### #create_framework
    
    
    def create_framework() -> ::Gapic::Config::Method

RPC-specific configuration for `create_framework`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_cloud_control
    
    
    def delete_cloud_control() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_cloud_control`

**Returns**

  * (::Gapic::Config::Method) 



### #delete_framework
    
    
    def delete_framework() -> ::Gapic::Config::Method

RPC-specific configuration for `delete_framework`

**Returns**

  * (::Gapic::Config::Method) 



### #get_cloud_control
    
    
    def get_cloud_control() -> ::Gapic::Config::Method

RPC-specific configuration for `get_cloud_control`

**Returns**

  * (::Gapic::Config::Method) 



### #get_framework
    
    
    def get_framework() -> ::Gapic::Config::Method

RPC-specific configuration for `get_framework`

**Returns**

  * (::Gapic::Config::Method) 



### #list_cloud_controls
    
    
    def list_cloud_controls() -> ::Gapic::Config::Method

RPC-specific configuration for `list_cloud_controls`

**Returns**

  * (::Gapic::Config::Method) 



### #list_frameworks
    
    
    def list_frameworks() -> ::Gapic::Config::Method

RPC-specific configuration for `list_frameworks`

**Returns**

  * (::Gapic::Config::Method) 



### #update_cloud_control
    
    
    def update_cloud_control() -> ::Gapic::Config::Method

RPC-specific configuration for `update_cloud_control`

**Returns**

  * (::Gapic::Config::Method) 



### #update_framework
    
    
    def update_framework() -> ::Gapic::Config::Method

RPC-specific configuration for `update_framework`

**Returns**

  * (::Gapic::Config::Method) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
