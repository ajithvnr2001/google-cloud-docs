---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Iam-V1-AuditConfigDelta/
title: BigQuery Reservation V1 API - Class Google::Iam::V1::AuditConfigDelta (v1.14.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:42:29.174829+00:00
---

# BigQuery Reservation V1 API - Class Google::Iam::V1::AuditConfigDelta (v1.14.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Iam-V1-AuditConfigDelta/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  BigQuery Reservation V1 API - Class Google::Iam::V1::AuditConfigDelta (v1.14.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.14.0 (latest)  1.13.1  1.12.1  1.11.0  1.10.0  1.9.2  1.8.0  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.12.0  0.11.2  0.10.0  0.9.0  0.8.1  0.7.0  0.6.0  0.5.0  0.4.2 

Reference documentation and code samples for the BigQuery Reservation V1 API class Google::Iam::V1::AuditConfigDelta.

One delta entry for AuditConfig. Each individual change (only one exempted_member in each entry) to a AuditConfig will be a separate entry.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #action
    
    
    def action() -> ::Google::Iam::V1::AuditConfigDelta::Action

**Returns**

  * ([::Google::Iam::V1::AuditConfigDelta::Action](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Iam-V1-AuditConfigDelta-Action)) — The action that was performed on an audit configuration in a policy. Required 



### #action=
    
    
    def action=(value) -> ::Google::Iam::V1::AuditConfigDelta::Action

**Parameter**

  * **value** ([::Google::Iam::V1::AuditConfigDelta::Action](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Iam-V1-AuditConfigDelta-Action)) — The action that was performed on an audit configuration in a policy. Required 



**Returns**

  * ([::Google::Iam::V1::AuditConfigDelta::Action](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Iam-V1-AuditConfigDelta-Action)) — The action that was performed on an audit configuration in a policy. Required 



### #exempted_member
    
    
    def exempted_member() -> ::String

**Returns**

  * (::String) — A single identity that is exempted from "data access" audit logging for the `service` specified above. Follows the same format of Binding.members. 



### #exempted_member=
    
    
    def exempted_member=(value) -> ::String

**Parameter**

  * **value** (::String) — A single identity that is exempted from "data access" audit logging for the `service` specified above. Follows the same format of Binding.members. 



**Returns**

  * (::String) — A single identity that is exempted from "data access" audit logging for the `service` specified above. Follows the same format of Binding.members. 



### #log_type
    
    
    def log_type() -> ::String

**Returns**

  * (::String) — Specifies the log_type that was be enabled. ADMIN_ACTIVITY is always enabled, and cannot be configured. Required 



### #log_type=
    
    
    def log_type=(value) -> ::String

**Parameter**

  * **value** (::String) — Specifies the log_type that was be enabled. ADMIN_ACTIVITY is always enabled, and cannot be configured. Required 



**Returns**

  * (::String) — Specifies the log_type that was be enabled. ADMIN_ACTIVITY is always enabled, and cannot be configured. Required 



### #service
    
    
    def service() -> ::String

**Returns**

  * (::String) — Specifies a service that was configured for Cloud Audit Logging. For example, `storage.googleapis.com`, `cloudsql.googleapis.com`. `allServices` is a special value that covers all services. Required 



### #service=
    
    
    def service=(value) -> ::String

**Parameter**

  * **value** (::String) — Specifies a service that was configured for Cloud Audit Logging. For example, `storage.googleapis.com`, `cloudsql.googleapis.com`. `allServices` is a special value that covers all services. Required 



**Returns**

  * (::String) — Specifies a service that was configured for Cloud Audit Logging. For example, `storage.googleapis.com`, `cloudsql.googleapis.com`. `allServices` is a special value that covers all services. Required 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
