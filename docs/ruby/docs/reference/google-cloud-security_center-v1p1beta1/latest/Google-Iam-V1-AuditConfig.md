---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v1p1beta1/latest/Google-Iam-V1-AuditConfig/
title: Cloud Security Command Center V1p1beta1 API - Class Google::Iam::V1::AuditConfig (v0.22.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:42:45.245997+00:00
---

# Cloud Security Command Center V1p1beta1 API - Class Google::Iam::V1::AuditConfig (v0.22.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v1p1beta1/latest/Google-Iam-V1-AuditConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Security Command Center V1p1beta1 API - Class Google::Iam::V1::AuditConfig (v0.22.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.22.1 (latest)  0.22.0  0.21.1  0.20.0  0.19.1  0.18.0  0.17.0  0.16.1  0.15.0  0.14.2  0.13.2  0.12.0  0.11.2  0.10.0  0.9.0  0.8.0  0.7.5 

Reference documentation and code samples for the Cloud Security Command Center V1p1beta1 API class Google::Iam::V1::AuditConfig.

Specifies the audit configuration for a service. The configuration determines which permission types are logged, and what identities, if any, are exempted from logging. An AuditConfig must have one or more AuditLogConfigs.

If there are AuditConfigs for both `allServices` and a specific service, the union of the two AuditConfigs is used for that service: the log_types specified in each AuditConfig are enabled, and the exempted_members in each AuditLogConfig are exempted.

Example Policy with multiple AuditConfigs:
    
    
    {
      "audit_configs": [
        {
          "service": "allServices",
          "audit_log_configs": [
            {
              "log_type": "DATA_READ",
              "exempted_members": [
                "user:jose@example.com"
              ]
            },
            {
              "log_type": "DATA_WRITE"
            },
            {
              "log_type": "ADMIN_READ"
            }
          ]
        },
        {
          "service": "sampleservice.googleapis.com",
          "audit_log_configs": [
            {
              "log_type": "DATA_READ"
            },
            {
              "log_type": "DATA_WRITE",
              "exempted_members": [
                "user:aliya@example.com"
              ]
            }
          ]
        }
      ]
    }
    

For sampleservice, this policy enables DATA_READ, DATA_WRITE and ADMIN_READ logging. It also exempts `jose@example.com` from DATA_READ logging, and `aliya@example.com` from DATA_WRITE logging.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #audit_log_configs
    
    
    def audit_log_configs() -> ::Array<::Google::Iam::V1::AuditLogConfig>

**Returns**

  * (::Array<[::Google::Iam::V1::AuditLogConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v1p1beta1/latest/Google-Iam-V1-AuditLogConfig)>) — The configuration for logging of each type of permission. 



### #audit_log_configs=
    
    
    def audit_log_configs=(value) -> ::Array<::Google::Iam::V1::AuditLogConfig>

**Parameter**

  * **value** (::Array<[::Google::Iam::V1::AuditLogConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v1p1beta1/latest/Google-Iam-V1-AuditLogConfig)>) — The configuration for logging of each type of permission. 



**Returns**

  * (::Array<[::Google::Iam::V1::AuditLogConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v1p1beta1/latest/Google-Iam-V1-AuditLogConfig)>) — The configuration for logging of each type of permission. 



### #service
    
    
    def service() -> ::String

**Returns**

  * (::String) — Specifies a service that will be enabled for audit logging. For example, `storage.googleapis.com`, `cloudsql.googleapis.com`. `allServices` is a special value that covers all services. 



### #service=
    
    
    def service=(value) -> ::String

**Parameter**

  * **value** (::String) — Specifies a service that will be enabled for audit logging. For example, `storage.googleapis.com`, `cloudsql.googleapis.com`. `allServices` is a special value that covers all services. 



**Returns**

  * (::String) — Specifies a service that will be enabled for audit logging. For example, `storage.googleapis.com`, `cloudsql.googleapis.com`. `allServices` is a special value that covers all services. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
