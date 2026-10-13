---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Iam-V1-AuditLogConfig/
title: Policy Simulator V1 API - Class Google::Iam::V1::AuditLogConfig (v1.9.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:48:50.571042+00:00
---

# Policy Simulator V1 API - Class Google::Iam::V1::AuditLogConfig (v1.9.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Iam-V1-AuditLogConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Policy Simulator V1 API - Class Google::Iam::V1::AuditLogConfig (v1.9.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.9.0 (latest)  1.8.1  1.7.0  1.6.1  1.5.0  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.4.0  0.3.2  0.2.0  0.1.1 

Reference documentation and code samples for the Policy Simulator V1 API class Google::Iam::V1::AuditLogConfig.

Provides the configuration for logging a type of permissions. Example:
    
    
    {
      "audit_log_configs": [
        {
          "log_type": "DATA_READ",
          "exempted_members": [
            "user:jose@example.com"
          ]
        },
        {
          "log_type": "DATA_WRITE"
        }
      ]
    }
    

This enables 'DATA_READ' and 'DATA_WRITE' logging, while exempting jose@example.com from DATA_READ logging.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #exempted_members
    
    
    def exempted_members() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Specifies the identities that do not cause logging for this type of permission. Follows the same format of [Binding.members][google.iam.v1.Binding.members]. 



### #exempted_members=
    
    
    def exempted_members=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Specifies the identities that do not cause logging for this type of permission. Follows the same format of [Binding.members][google.iam.v1.Binding.members]. 



**Returns**

  * (::Array<::String>) — Specifies the identities that do not cause logging for this type of permission. Follows the same format of [Binding.members][google.iam.v1.Binding.members]. 



### #log_type
    
    
    def log_type() -> ::Google::Iam::V1::AuditLogConfig::LogType

**Returns**

  * ([::Google::Iam::V1::AuditLogConfig::LogType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Iam-V1-AuditLogConfig-LogType)) — The log type that this config enables. 



### #log_type=
    
    
    def log_type=(value) -> ::Google::Iam::V1::AuditLogConfig::LogType

**Parameter**

  * **value** ([::Google::Iam::V1::AuditLogConfig::LogType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Iam-V1-AuditLogConfig-LogType)) — The log type that this config enables. 



**Returns**

  * ([::Google::Iam::V1::AuditLogConfig::LogType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Iam-V1-AuditLogConfig-LogType)) — The log type that this config enables. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
