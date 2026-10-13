---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-auditmanager/latest/com.google.cloud.auditmanager.v1.ReportGenerationProgressOrBuilder
title: Interface ReportGenerationProgressOrBuilder (0.17.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:38:32.062918+00:00
---

# Interface ReportGenerationProgressOrBuilder (0.17.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-auditmanager/latest/com.google.cloud.auditmanager.v1.ReportGenerationProgressOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ReportGenerationProgressOrBuilder (0.17.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.17.0 (latest)  0.13.0  0.12.0  0.11.0  0.9.0  0.6.0  0.5.0  0.3.0  0.1.0 
    
    
    public interface ReportGenerationProgressOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAuditReport()
    
    
    public abstract String getAuditReport()

Output only. Name of the audit report.

` string audit_report = 51 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The auditReport.  
  
### getAuditReportBytes()
    
    
    public abstract ByteString getAuditReportBytes()

Output only. Name of the audit report.

` string audit_report = 51 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for auditReport.  
  
### getDestinationGcsBucket()
    
    
    public abstract String getDestinationGcsBucket()

Output only. Cloud Storage bucket where the audit report is uploaded to after the evaluation process is completed.

`string destination_gcs_bucket = 50 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The destinationGcsBucket.  
  
### getDestinationGcsBucketBytes()
    
    
    public abstract ByteString getDestinationGcsBucketBytes()

Output only. Cloud Storage bucket where the audit report is uploaded to after the evaluation process is completed.

`string destination_gcs_bucket = 50 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for destinationGcsBucket.  
  
### getEvaluationPercentComplete()
    
    
    public abstract double getEvaluationPercentComplete()

Progress of the evaluation process. The progress is defined in terms of percentage complete.

`double evaluation_percent_complete = 20;`

**Returns**  
---  
**Type** | **Description**  
`[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The evaluationPercentComplete.  
  
### getFailureReason()
    
    
    public abstract String getFailureReason()

Output only. Reason for failure during the audit report generation process. This field is set only if the `OperationState` attribute is `OPERATION_STATE_FAILED`.

`string failure_reason = 2 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The failureReason.  
  
### getFailureReasonBytes()
    
    
    public abstract ByteString getFailureReasonBytes()

Output only. Reason for failure during the audit report generation process. This field is set only if the `OperationState` attribute is `OPERATION_STATE_FAILED`.

`string failure_reason = 2 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for failureReason.  
  
### getReportGenerationPercentComplete()
    
    
    public abstract double getReportGenerationPercentComplete()

Report generation progress, defined in terms of percentage complete. Until evaluation is complete, this value is always `0`.

`double report_generation_percent_complete = 30;`

**Returns**  
---  
**Type** | **Description**  
`[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The reportGenerationPercentComplete.  
  
### getReportUploadingPercentComplete()
    
    
    public abstract double getReportUploadingPercentComplete()

Report uploading progress, defined in terms of percentage complete. Until evaluation and report generation are complete, this value is always `0`.

`double report_uploading_percent_complete = 40;`

**Returns**  
---  
**Type** | **Description**  
`[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The reportUploadingPercentComplete.  
  
### getState()
    
    
    public abstract OperationState getState()

Output only. Current state of execution for report generation.

` .google.cloud.auditmanager.v1.OperationState state = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[OperationState](https://docs.cloud.google.com/java/docs/reference/google-cloud-auditmanager/latest/com.google.cloud.auditmanager.v1.OperationState)` | The state.  
  
### getStateValue()
    
    
    public abstract int getStateValue()

Output only. Current state of execution for report generation.

` .google.cloud.auditmanager.v1.OperationState state = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for state.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
