---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-UpdateAuditScheduleRequest/
title: Audit Manager V1 API - Class Google::Cloud::AuditManager::V1::UpdateAuditScheduleRequest (v1.2.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:31:54.785006+00:00
---

# Audit Manager V1 API - Class Google::Cloud::AuditManager::V1::UpdateAuditScheduleRequest (v1.2.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-UpdateAuditScheduleRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Audit Manager V1 API - Class Google::Cloud::AuditManager::V1::UpdateAuditScheduleRequest (v1.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.2.0 (latest)  1.1.1  1.0.1  0.2.0  0.1.0 

Reference documentation and code samples for the Audit Manager V1 API class Google::Cloud::AuditManager::V1::UpdateAuditScheduleRequest.

Request message for [UpdateAuditSchedule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditManager-Client#Google__Cloud__AuditManager__V1__AuditManager__Client_update_audit_schedule_instance_ "Google::Cloud::AuditManager::V1::AuditManager::Client#update_audit_schedule \(method\)").

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #audit_schedule
    
    
    def audit_schedule() -> ::Google::Cloud::AuditManager::V1::AuditSchedule

**Returns**

  * ([::Google::Cloud::AuditManager::V1::AuditSchedule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditSchedule)) — Required. Audit schedule to update. 



### #audit_schedule=
    
    
    def audit_schedule=(value) -> ::Google::Cloud::AuditManager::V1::AuditSchedule

**Parameter**

  * **value** ([::Google::Cloud::AuditManager::V1::AuditSchedule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditSchedule)) — Required. Audit schedule to update. 



**Returns**

  * ([::Google::Cloud::AuditManager::V1::AuditSchedule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditSchedule)) — Required. Audit schedule to update. 



### #update_mask
    
    
    def update_mask() -> ::Google::Protobuf::FieldMask

**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Protobuf-FieldMask)) — Optional. List of fields to update. 



### #update_mask=
    
    
    def update_mask=(value) -> ::Google::Protobuf::FieldMask

**Parameter**

  * **value** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Protobuf-FieldMask)) — Optional. List of fields to update. 



**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Protobuf-FieldMask)) — Optional. List of fields to update. 



### #validate_only
    
    
    def validate_only() -> ::Boolean

**Returns**

  * (::Boolean) — 

Optional. If `true`, only validates the request and does not update the audit schedule. This executes standard request validation (such as schema, framework existence, scope, and IAM checks) and skips the apply phase.

Use this field for the following purposes:

    * **Infrastructure as Code (IaC)** : Allow tools like Terraform to run dry-run mutations (e.g., `terraform plan`) without creating real resources or incurring costs.
    * **User Interface Validation** : Enable real-time form and permission validation in custom UIs before submitting requests.
    * **CI/CD & Automation**: Test your scripts, permissions, and parameters safely without consuming resource quotas.



### #validate_only=
    
    
    def validate_only=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — 

Optional. If `true`, only validates the request and does not update the audit schedule. This executes standard request validation (such as schema, framework existence, scope, and IAM checks) and skips the apply phase.

Use this field for the following purposes:

    * **Infrastructure as Code (IaC)** : Allow tools like Terraform to run dry-run mutations (e.g., `terraform plan`) without creating real resources or incurring costs.
    * **User Interface Validation** : Enable real-time form and permission validation in custom UIs before submitting requests.
    * **CI/CD & Automation**: Test your scripts, permissions, and parameters safely without consuming resource quotas.



**Returns**

  * (::Boolean) — 

Optional. If `true`, only validates the request and does not update the audit schedule. This executes standard request validation (such as schema, framework existence, scope, and IAM checks) and skips the apply phase.

Use this field for the following purposes:

    * **Infrastructure as Code (IaC)** : Allow tools like Terraform to run dry-run mutations (e.g., `terraform plan`) without creating real resources or incurring costs.
    * **User Interface Validation** : Enable real-time form and permission validation in custom UIs before submitting requests.
    * **CI/CD & Automation**: Test your scripts, permissions, and parameters safely without consuming resource quotas.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
