---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-ReportGenerationProgress/
title: Audit Manager V1 API - Class Google::Cloud::AuditManager::V1::ReportGenerationProgress (v1.2.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:31:53.221249+00:00
---

# Audit Manager V1 API - Class Google::Cloud::AuditManager::V1::ReportGenerationProgress (v1.2.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-ReportGenerationProgress/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Audit Manager V1 API - Class Google::Cloud::AuditManager::V1::ReportGenerationProgress (v1.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.2.0 (latest)  1.1.1  1.0.1  0.2.0  0.1.0 

Reference documentation and code samples for the Audit Manager V1 API class Google::Cloud::AuditManager::V1::ReportGenerationProgress.

Details about the current status of the report-generation process.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #audit_report
    
    
    def audit_report() -> ::String

**Returns**

  * (::String) — Output only. Name of the audit report. 



### #destination_gcs_bucket
    
    
    def destination_gcs_bucket() -> ::String

**Returns**

  * (::String) — Output only. Cloud Storage bucket where the audit report is uploaded to after the evaluation process is completed. 



### #evaluation_percent_complete
    
    
    def evaluation_percent_complete() -> ::Float

**Returns**

  * (::Float) — Progress of the evaluation process. The progress is defined in terms of percentage complete. 



### #evaluation_percent_complete=
    
    
    def evaluation_percent_complete=(value) -> ::Float

**Parameter**

  * **value** (::Float) — Progress of the evaluation process. The progress is defined in terms of percentage complete. 



**Returns**

  * (::Float) — Progress of the evaluation process. The progress is defined in terms of percentage complete. 



### #failure_reason
    
    
    def failure_reason() -> ::String

**Returns**

  * (::String) — Output only. Reason for failure during the audit report generation process. This field is set only if the `OperationState` attribute is `OPERATION_STATE_FAILED`. 



### #report_generation_percent_complete
    
    
    def report_generation_percent_complete() -> ::Float

**Returns**

  * (::Float) — Report generation progress, defined in terms of percentage complete. Until evaluation is complete, this value is always `0`. 



### #report_generation_percent_complete=
    
    
    def report_generation_percent_complete=(value) -> ::Float

**Parameter**

  * **value** (::Float) — Report generation progress, defined in terms of percentage complete. Until evaluation is complete, this value is always `0`. 



**Returns**

  * (::Float) — Report generation progress, defined in terms of percentage complete. Until evaluation is complete, this value is always `0`. 



### #report_uploading_percent_complete
    
    
    def report_uploading_percent_complete() -> ::Float

**Returns**

  * (::Float) — Report uploading progress, defined in terms of percentage complete. Until evaluation and report generation are complete, this value is always `0`. 



### #report_uploading_percent_complete=
    
    
    def report_uploading_percent_complete=(value) -> ::Float

**Parameter**

  * **value** (::Float) — Report uploading progress, defined in terms of percentage complete. Until evaluation and report generation are complete, this value is always `0`. 



**Returns**

  * (::Float) — Report uploading progress, defined in terms of percentage complete. Until evaluation and report generation are complete, this value is always `0`. 



### #state
    
    
    def state() -> ::Google::Cloud::AuditManager::V1::OperationState

**Returns**

  * ([::Google::Cloud::AuditManager::V1::OperationState](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-audit_manager-v1/latest/Google-Cloud-AuditManager-V1-OperationState)) — Output only. Current state of execution for report generation. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
