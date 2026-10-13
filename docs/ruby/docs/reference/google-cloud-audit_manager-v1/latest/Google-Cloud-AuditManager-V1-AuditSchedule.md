---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditSchedule/
title: Audit Manager V1 API - Class Google::Cloud::AuditManager::V1::AuditSchedule (v1.2.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:31:48.708655+00:00
---

# Audit Manager V1 API - Class Google::Cloud::AuditManager::V1::AuditSchedule (v1.2.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditSchedule/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Audit Manager V1 API - Class Google::Cloud::AuditManager::V1::AuditSchedule (v1.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.2.0 (latest)  1.1.1  1.0.1  0.2.0  0.1.0 

Reference documentation and code samples for the Audit Manager V1 API class Google::Cloud::AuditManager::V1::AuditSchedule.

An audit schedule, in one of the following formats:

  * `projects/{project}/locations/{location}/auditSchedules/{audit_schedule}`
  * `folders/{folder}/locations/{location}/auditSchedules/{audit_schedule}`



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

  * (::String) — Required. Framework (set of controls) that the audit scope report is generated against. For example, `NIST_800_53`. 



### #compliance_framework=
    
    
    def compliance_framework=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Framework (set of controls) that the audit scope report is generated against. For example, `NIST_800_53`. 



**Returns**

  * (::String) — Required. Framework (set of controls) that the audit scope report is generated against. For example, `NIST_800_53`. 



### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Protobuf-Timestamp)) — Output only. Timestamp when the schedule was created. 



### #display_name
    
    
    def display_name() -> ::String

**Returns**

  * (::String) — Optional. Display name for the audit schedule. 



### #display_name=
    
    
    def display_name=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Display name for the audit schedule. 



**Returns**

  * (::String) — Optional. Display name for the audit schedule. 



### #error_message
    
    
    def error_message() -> ::String

**Returns**

  * (::String) — Output only. Describes the error if the schedule is in an error state. 



### #gcs_uri
    
    
    def gcs_uri() -> ::String

**Returns**

  * (::String) — Required. Cloud Storage bucket where Audit Manager can upload the audit report and evidence. The format is `gs://{bucket_name}`. 



### #gcs_uri=
    
    
    def gcs_uri=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Cloud Storage bucket where Audit Manager can upload the audit report and evidence. The format is `gs://{bucket_name}`. 



**Returns**

  * (::String) — Required. Cloud Storage bucket where Audit Manager can upload the audit report and evidence. The format is `gs://{bucket_name}`. 



### #last_trigger_time
    
    
    def last_trigger_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Protobuf-Timestamp)) — Output only. Timestamp when the audit run was last triggered. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Identifier. Unique identifier for the audit schedule. Format: projects/{project}/locations/{location}/auditSchedules/{audit_schedule} folders/{folder}/locations/{location}/auditSchedules/{audit_schedule} organizations/{organization}/locations/{location}/auditSchedules/{audit_schedule} 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Identifier. Unique identifier for the audit schedule. Format: projects/{project}/locations/{location}/auditSchedules/{audit_schedule} folders/{folder}/locations/{location}/auditSchedules/{audit_schedule} organizations/{organization}/locations/{location}/auditSchedules/{audit_schedule} 



**Returns**

  * (::String) — Identifier. Unique identifier for the audit schedule. Format: projects/{project}/locations/{location}/auditSchedules/{audit_schedule} folders/{folder}/locations/{location}/auditSchedules/{audit_schedule} organizations/{organization}/locations/{location}/auditSchedules/{audit_schedule} 



### #next_run_time
    
    
    def next_run_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Protobuf-Timestamp)) — Output only. Calculated timestamp for the next scheduled run. 



### #report_format
    
    
    def report_format() -> ::Google::Cloud::AuditManager::V1::AuditSchedule::AuditReportFormat

**Returns**

  * ([::Google::Cloud::AuditManager::V1::AuditSchedule::AuditReportFormat](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditSchedule-AuditReportFormat)) — Required. Format for the audit report. 



### #report_format=
    
    
    def report_format=(value) -> ::Google::Cloud::AuditManager::V1::AuditSchedule::AuditReportFormat

**Parameter**

  * **value** ([::Google::Cloud::AuditManager::V1::AuditSchedule::AuditReportFormat](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditSchedule-AuditReportFormat)) — Required. Format for the audit report. 



**Returns**

  * ([::Google::Cloud::AuditManager::V1::AuditSchedule::AuditReportFormat](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditSchedule-AuditReportFormat)) — Required. Format for the audit report. 



### #schedule_config
    
    
    def schedule_config() -> ::Google::Cloud::AuditManager::V1::ScheduleConfig

**Returns**

  * ([::Google::Cloud::AuditManager::V1::ScheduleConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-ScheduleConfig)) — Required. Configuration that defines when and how often audit runs are automatically triggered for this schedule. 



### #schedule_config=
    
    
    def schedule_config=(value) -> ::Google::Cloud::AuditManager::V1::ScheduleConfig

**Parameter**

  * **value** ([::Google::Cloud::AuditManager::V1::ScheduleConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-ScheduleConfig)) — Required. Configuration that defines when and how often audit runs are automatically triggered for this schedule. 



**Returns**

  * ([::Google::Cloud::AuditManager::V1::ScheduleConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-ScheduleConfig)) — Required. Configuration that defines when and how often audit runs are automatically triggered for this schedule. 



### #state
    
    
    def state() -> ::Google::Cloud::AuditManager::V1::ScheduleState

**Returns**

  * ([::Google::Cloud::AuditManager::V1::ScheduleState](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-ScheduleState)) — Optional. State of the audit schedule. While most states are managed by the system, you can use [UpdateAuditSchedule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditManager-Client#Google__Cloud__AuditManager__V1__AuditManager__Client_update_audit_schedule_instance_ "Google::Cloud::AuditManager::V1::AuditManager::Client#update_audit_schedule \(method\)") to start, pause, or delete the schedule. 



### #state=
    
    
    def state=(value) -> ::Google::Cloud::AuditManager::V1::ScheduleState

**Parameter**

  * **value** ([::Google::Cloud::AuditManager::V1::ScheduleState](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-ScheduleState)) — Optional. State of the audit schedule. While most states are managed by the system, you can use [UpdateAuditSchedule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditManager-Client#Google__Cloud__AuditManager__V1__AuditManager__Client_update_audit_schedule_instance_ "Google::Cloud::AuditManager::V1::AuditManager::Client#update_audit_schedule \(method\)") to start, pause, or delete the schedule. 



**Returns**

  * ([::Google::Cloud::AuditManager::V1::ScheduleState](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-ScheduleState)) — Optional. State of the audit schedule. While most states are managed by the system, you can use [UpdateAuditSchedule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-AuditManager-Client#Google__Cloud__AuditManager__V1__AuditManager__Client_update_audit_schedule_instance_ "Google::Cloud::AuditManager::V1::AuditManager::Client#update_audit_schedule \(method\)") to start, pause, or delete the schedule. 



### #update_time
    
    
    def update_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Protobuf-Timestamp)) — Output only. Timestamp when the schedule was last updated. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
