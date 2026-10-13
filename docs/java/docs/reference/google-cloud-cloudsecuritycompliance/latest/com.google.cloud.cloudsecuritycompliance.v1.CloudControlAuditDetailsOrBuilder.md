---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.CloudControlAuditDetailsOrBuilder
title: Interface CloudControlAuditDetailsOrBuilder (0.26.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:01:47.258616+00:00
---

# Interface CloudControlAuditDetailsOrBuilder (0.26.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.CloudControlAuditDetailsOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface CloudControlAuditDetailsOrBuilder (0.26.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.26.0 (latest)  0.22.0  0.21.0  0.20.0  0.18.0  0.15.0  0.14.0  0.12.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface CloudControlAuditDetailsOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getCloudControl()
    
    
    public abstract String getCloudControl()

Output only. The name of the cloud control.

`string cloud_control = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The cloudControl.  
  
### getCloudControlBytes()
    
    
    public abstract ByteString getCloudControlBytes()

Output only. The name of the cloud control.

`string cloud_control = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for cloudControl.  
  
### getCloudControlDescription()
    
    
    public abstract String getCloudControlDescription()

Output only. The description of the cloud control.

`string cloud_control_description = 3 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The cloudControlDescription.  
  
### getCloudControlDescriptionBytes()
    
    
    public abstract ByteString getCloudControlDescriptionBytes()

Output only. The description of the cloud control.

`string cloud_control_description = 3 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for cloudControlDescription.  
  
### getCloudControlId()
    
    
    public abstract String getCloudControlId()

Output only. The ID of the cloud control.

`string cloud_control_id = 2 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The cloudControlId.  
  
### getCloudControlIdBytes()
    
    
    public abstract ByteString getCloudControlIdBytes()

Output only. The ID of the cloud control.

`string cloud_control_id = 2 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for cloudControlId.  
  
### getComplianceState()
    
    
    public abstract ComplianceState getComplianceState()

Output only. The overall status of the findings for the control.

` .google.cloud.cloudsecuritycompliance.v1.ComplianceState compliance_state = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ComplianceState](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ComplianceState)` | The complianceState.  
  
### getComplianceStateValue()
    
    
    public abstract int getComplianceStateValue()

Output only. The overall status of the findings for the control.

` .google.cloud.cloudsecuritycompliance.v1.ComplianceState compliance_state = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for complianceState.  
  
### getFindings(int index)
    
    
    public abstract FindingDetails getFindings(int index)

Output only. The findings for the control.

` repeated .google.cloud.cloudsecuritycompliance.v1.FindingDetails findings = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FindingDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.FindingDetails)` |   
  
### getFindingsCount()
    
    
    public abstract int getFindingsCount()

Output only. The findings for the control.

` repeated .google.cloud.cloudsecuritycompliance.v1.FindingDetails findings = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getFindingsList()
    
    
    public abstract List<FindingDetails> getFindingsList()

Output only. The findings for the control.

` repeated .google.cloud.cloudsecuritycompliance.v1.FindingDetails findings = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[FindingDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.FindingDetails)>` |   
  
### getFindingsOrBuilder(int index)
    
    
    public abstract FindingDetailsOrBuilder getFindingsOrBuilder(int index)

Output only. The findings for the control.

` repeated .google.cloud.cloudsecuritycompliance.v1.FindingDetails findings = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FindingDetailsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.FindingDetailsOrBuilder)` |   
  
### getFindingsOrBuilderList()
    
    
    public abstract List<? extends FindingDetailsOrBuilder> getFindingsOrBuilderList()

Output only. The findings for the control.

` repeated .google.cloud.cloudsecuritycompliance.v1.FindingDetails findings = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.cloudsecuritycompliance.v1.FindingDetailsOrBuilder>` |   
  
### getReportSummary()
    
    
    public abstract ReportSummary getReportSummary()

Output only. The summary of the report.

` .google.cloud.cloudsecuritycompliance.v1.ReportSummary report_summary = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ReportSummary](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ReportSummary)` | The reportSummary.  
  
### getReportSummaryOrBuilder()
    
    
    public abstract ReportSummaryOrBuilder getReportSummaryOrBuilder()

Output only. The summary of the report.

` .google.cloud.cloudsecuritycompliance.v1.ReportSummary report_summary = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ReportSummaryOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ReportSummaryOrBuilder)` |   
  
### hasReportSummary()
    
    
    public abstract boolean hasReportSummary()

Output only. The summary of the report.

` .google.cloud.cloudsecuritycompliance.v1.ReportSummary report_summary = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the reportSummary field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
