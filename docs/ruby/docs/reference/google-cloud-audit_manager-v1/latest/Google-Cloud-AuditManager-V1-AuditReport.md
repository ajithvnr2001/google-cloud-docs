---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditReport/
title: Audit Manager V1 API - Class Google::Cloud::AuditManager::V1::AuditReport (v1.2.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:31:48.237424+00:00
---

# Audit Manager V1 API - Class Google::Cloud::AuditManager::V1::AuditReport (v1.2.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditReport/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Audit Manager V1 API - Class Google::Cloud::AuditManager::V1::AuditReport (v1.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.2.0 (latest)  1.1.1  1.0.1  0.2.0  0.1.0 

Reference documentation and code samples for the Audit Manager V1 API class Google::Cloud::AuditManager::V1::AuditReport.

An audit report.

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

  * (::String) — Output only. Compliance framework to use for the audit report. For example, `CIS_GCP_FOUNDATIONS_V1_2_0`. 



### #compliance_standard
    
    
    def compliance_standard() -> ::String

**Returns**

  * (::String) — Output only. Deprecated. Compliance standard to be audited against.

Use the `compliance_framework` field instead. 




### #control_details
    
    
    def control_details() -> ::Array<::Google::Cloud::AuditManager::V1::ControlDetails>

**Returns**

  * (::Array<[::Google::Cloud::AuditManager::V1::ControlDetails](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-ControlDetails)>) — Output only. Overall status of the controls. 



### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Protobuf-Timestamp)) — Output only. Creation time of the audit report. 



### #destination_details
    
    
    def destination_details() -> ::Google::Cloud::AuditManager::V1::DestinationDetails

**Returns**

  * ([::Google::Cloud::AuditManager::V1::DestinationDetails](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-DestinationDetails)) — Output only. Cloud Storage bucket where the audit report is uploaded to. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — 

Identifier. Name of the audit report, in one of the following formats:

    * `projects/{project}/locations/{location}/auditReports/{audit_report}`
    * `folders/{folder}/locations/{location}/auditReports/{audit_report}`
    * `organizations/{organization}/locations/{location}/auditReports/{audit_report}`



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — 

Identifier. Name of the audit report, in one of the following formats:

    * `projects/{project}/locations/{location}/auditReports/{audit_report}`
    * `folders/{folder}/locations/{location}/auditReports/{audit_report}`
    * `organizations/{organization}/locations/{location}/auditReports/{audit_report}`



**Returns**

  * (::String) — 

Identifier. Name of the audit report, in one of the following formats:

    * `projects/{project}/locations/{location}/auditReports/{audit_report}`
    * `folders/{folder}/locations/{location}/auditReports/{audit_report}`
    * `organizations/{organization}/locations/{location}/auditReports/{audit_report}`



### #operation_id
    
    
    def operation_id() -> ::String

**Returns**

  * (::String) — Output only. Client operation ID for the audit report. 



### #report_generation_state
    
    
    def report_generation_state() -> ::Google::Cloud::AuditManager::V1::AuditReport::ReportGenerationState

**Returns**

  * ([::Google::Cloud::AuditManager::V1::AuditReport::ReportGenerationState](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditReport-ReportGenerationState)) — Output only. State of audit report generation. 



### #report_summary
    
    
    def report_summary() -> ::Google::Cloud::AuditManager::V1::ReportSummary

**Returns**

  * ([::Google::Cloud::AuditManager::V1::ReportSummary](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-ReportSummary)) — Output only. Report summary that includes information about compliance and violation counts. 



### #scope
    
    
    def scope() -> ::String

**Returns**

  * (::String) — 

Output only. Organization, folder, or project that the report is generated for, in one of the following formats:

    * `projects/{project}/locations/{location}`
    * `folders/{folder}/locations/{location}`
    * `organizations/{organization}/locations/{location}`



### #scope_id
    
    
    def scope_id() -> ::String

**Returns**

  * (::String) — Output only. Project number, folder ID, or organization ID that the audit report was generated for. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
