---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-GenerateAuditReportRequest/
title: Audit Manager V1 API - Class Google::Cloud::AuditManager::V1::GenerateAuditReportRequest (v1.2.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:31:50.379082+00:00
---

# Audit Manager V1 API - Class Google::Cloud::AuditManager::V1::GenerateAuditReportRequest (v1.2.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-GenerateAuditReportRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Audit Manager V1 API - Class Google::Cloud::AuditManager::V1::GenerateAuditReportRequest (v1.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.2.0 (latest)  1.1.1  1.0.1  0.2.0  0.1.0 

Reference documentation and code samples for the Audit Manager V1 API class Google::Cloud::AuditManager::V1::GenerateAuditReportRequest.

Request message for [GenerateAuditReport](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditManager-Client#Google__Cloud__AuditManager__V1__AuditManager__Client_generate_audit_report_instance_ "Google::Cloud::AuditManager::V1::AuditManager::Client#generate_audit_report \(method\)").

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #compliance_framework
    
    
    def compliance_framework() -> ::String

**Returns**

  * (::String) — Required. The framework that's used for the audit report. For example, `NIST_800_53`. 



### #compliance_framework=
    
    
    def compliance_framework=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The framework that's used for the audit report. For example, `NIST_800_53`. 



**Returns**

  * (::String) — Required. The framework that's used for the audit report. For example, `NIST_800_53`. 



### #compliance_standard
    
    
    def compliance_standard() -> ::String

**Returns**

  * (::String) — Optional. Deprecated. Compliance standard for the audit report.

Use the `compliance_framework` field instead. 




### #compliance_standard=
    
    
    def compliance_standard=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Deprecated. Compliance standard for the audit report.

Use the `compliance_framework` field instead. 




**Returns**

  * (::String) — Optional. Deprecated. Compliance standard for the audit report.

Use the `compliance_framework` field instead. 




### #gcs_uri
    
    
    def gcs_uri() -> ::String

**Returns**

  * (::String) — URL for the Cloud Storage bucket where the report and evidence is uploaded. You must select a bucket that was provided during the enrollment process. 



### #gcs_uri=
    
    
    def gcs_uri=(value) -> ::String

**Parameter**

  * **value** (::String) — URL for the Cloud Storage bucket where the report and evidence is uploaded. You must select a bucket that was provided during the enrollment process. 



**Returns**

  * (::String) — URL for the Cloud Storage bucket where the report and evidence is uploaded. You must select a bucket that was provided during the enrollment process. 



### #report_format
    
    
    def report_format() -> ::Google::Cloud::AuditManager::V1::GenerateAuditReportRequest::AuditReportFormat

**Returns**

  * ([::Google::Cloud::AuditManager::V1::GenerateAuditReportRequest::AuditReportFormat](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-GenerateAuditReportRequest-AuditReportFormat)) — Required. Format for the audit report. 



### #report_format=
    
    
    def report_format=(value) -> ::Google::Cloud::AuditManager::V1::GenerateAuditReportRequest::AuditReportFormat

**Parameter**

  * **value** ([::Google::Cloud::AuditManager::V1::GenerateAuditReportRequest::AuditReportFormat](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-GenerateAuditReportRequest-AuditReportFormat)) — Required. Format for the audit report. 



**Returns**

  * ([::Google::Cloud::AuditManager::V1::GenerateAuditReportRequest::AuditReportFormat](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-GenerateAuditReportRequest-AuditReportFormat)) — Required. Format for the audit report. 



### #scope
    
    
    def scope() -> ::String

**Returns**

  * (::String) — 

Required. Organization, folder, or project that the audit applies to, in one of the following formats:

    * `projects/{project}/locations/{location}`
    * `folders/{folder}/locations/{location}`
    * `organizations/{organization}/locations/{location}`



### #scope=
    
    
    def scope=(value) -> ::String

**Parameter**

  * **value** (::String) — 

Required. Organization, folder, or project that the audit applies to, in one of the following formats:

    * `projects/{project}/locations/{location}`
    * `folders/{folder}/locations/{location}`
    * `organizations/{organization}/locations/{location}`



**Returns**

  * (::String) — 

Required. Organization, folder, or project that the audit applies to, in one of the following formats:

    * `projects/{project}/locations/{location}`
    * `folders/{folder}/locations/{location}`
    * `organizations/{organization}/locations/{location}`



### #validate_only
    
    
    def validate_only() -> ::Boolean

**Returns**

  * (::Boolean) — 

Optional. If `true`, only validates the request and does not generate the audit report. This executes standard request validation (such as schema, framework existence, scope, and IAM checks) and skips the apply phase.

Use this field for the following purposes:

    * **Infrastructure as Code (IaC)** : Allow tools like Terraform to run dry-run mutations (e.g., `terraform plan`) without creating real resources or incurring costs.
    * **User Interface Validation** : Enable real-time form and permission validation in custom UIs before submitting requests.
    * **CI/CD & Automation**: Test your scripts, permissions, and parameters safely without triggering expensive Long-Running Operations (LROs) or consuming resource quotas.



### #validate_only=
    
    
    def validate_only=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — 

Optional. If `true`, only validates the request and does not generate the audit report. This executes standard request validation (such as schema, framework existence, scope, and IAM checks) and skips the apply phase.

Use this field for the following purposes:

    * **Infrastructure as Code (IaC)** : Allow tools like Terraform to run dry-run mutations (e.g., `terraform plan`) without creating real resources or incurring costs.
    * **User Interface Validation** : Enable real-time form and permission validation in custom UIs before submitting requests.
    * **CI/CD & Automation**: Test your scripts, permissions, and parameters safely without triggering expensive Long-Running Operations (LROs) or consuming resource quotas.



**Returns**

  * (::Boolean) — 

Optional. If `true`, only validates the request and does not generate the audit report. This executes standard request validation (such as schema, framework existence, scope, and IAM checks) and skips the apply phase.

Use this field for the following purposes:

    * **Infrastructure as Code (IaC)** : Allow tools like Terraform to run dry-run mutations (e.g., `terraform plan`) without creating real resources or incurring costs.
    * **User Interface Validation** : Enable real-time form and permission validation in custom UIs before submitting requests.
    * **CI/CD & Automation**: Test your scripts, permissions, and parameters safely without triggering expensive Long-Running Operations (LROs) or consuming resource quotas.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
