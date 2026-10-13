---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditManager-Client-Configuration-Rpcs/
title: Audit Manager V1 API - Class Google::Cloud::AuditManager::V1::AuditManager::Client::Configuration::Rpcs (v1.2.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:31:46.129226+00:00
---

# Audit Manager V1 API - Class Google::Cloud::AuditManager::V1::AuditManager::Client::Configuration::Rpcs (v1.2.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditManager-Client-Configuration-Rpcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Audit Manager V1 API - Class Google::Cloud::AuditManager::V1::AuditManager::Client::Configuration::Rpcs (v1.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.2.0 (latest)  1.1.1  1.0.1  0.2.0  0.1.0 

Reference documentation and code samples for the Audit Manager V1 API class Google::Cloud::AuditManager::V1::AuditManager::Client::Configuration::Rpcs.

Configuration RPC class for the AuditManager API.

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

### #create_audit_schedule
    
    
    def create_audit_schedule() -> ::Gapic::Config::Method

RPC-specific configuration for `create_audit_schedule`

**Returns**

  * (::Gapic::Config::Method) 



### #enroll_resource
    
    
    def enroll_resource() -> ::Gapic::Config::Method

RPC-specific configuration for `enroll_resource`

**Returns**

  * (::Gapic::Config::Method) 



### #generate_audit_report
    
    
    def generate_audit_report() -> ::Gapic::Config::Method

RPC-specific configuration for `generate_audit_report`

**Returns**

  * (::Gapic::Config::Method) 



### #generate_audit_scope_report
    
    
    def generate_audit_scope_report() -> ::Gapic::Config::Method

RPC-specific configuration for `generate_audit_scope_report`

**Returns**

  * (::Gapic::Config::Method) 



### #get_audit_report
    
    
    def get_audit_report() -> ::Gapic::Config::Method

RPC-specific configuration for `get_audit_report`

**Returns**

  * (::Gapic::Config::Method) 



### #get_audit_schedule
    
    
    def get_audit_schedule() -> ::Gapic::Config::Method

RPC-specific configuration for `get_audit_schedule`

**Returns**

  * (::Gapic::Config::Method) 



### #get_resource_enrollment_status
    
    
    def get_resource_enrollment_status() -> ::Gapic::Config::Method

RPC-specific configuration for `get_resource_enrollment_status`

**Returns**

  * (::Gapic::Config::Method) 



### #list_audit_reports
    
    
    def list_audit_reports() -> ::Gapic::Config::Method

RPC-specific configuration for `list_audit_reports`

**Returns**

  * (::Gapic::Config::Method) 



### #list_audit_schedules
    
    
    def list_audit_schedules() -> ::Gapic::Config::Method

RPC-specific configuration for `list_audit_schedules`

**Returns**

  * (::Gapic::Config::Method) 



### #list_controls
    
    
    def list_controls() -> ::Gapic::Config::Method

RPC-specific configuration for `list_controls`

**Returns**

  * (::Gapic::Config::Method) 



### #list_resource_enrollment_statuses
    
    
    def list_resource_enrollment_statuses() -> ::Gapic::Config::Method

RPC-specific configuration for `list_resource_enrollment_statuses`

**Returns**

  * (::Gapic::Config::Method) 



### #update_audit_schedule
    
    
    def update_audit_schedule() -> ::Gapic::Config::Method

RPC-specific configuration for `update_audit_schedule`

**Returns**

  * (::Gapic::Config::Method) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
