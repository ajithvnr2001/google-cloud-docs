---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.ViolationOrBuilder
title: Interface ViolationOrBuilder (2.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:48:25.672762+00:00
---

# Interface ViolationOrBuilder (2.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.ViolationOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ViolationOrBuilder (2.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.99.0 (latest)  2.95.0  2.94.0  2.93.0  2.91.0  2.88.0  2.87.0  2.85.0  2.83.0  2.82.0  2.81.0  2.80.0  2.78.0  2.76.0  2.75.0  2.74.0  2.73.0  2.72.0  2.70.0  2.68.0  2.67.0  2.64.0  2.63.0  2.62.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.51.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.1.0  2.0.0  1.1.0  1.0.4  0.9.0  0.8.2 
    
    
    public interface ViolationOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAcknowledged()
    
    
    public abstract boolean getAcknowledged()

Output only. A boolean that indicates if the violation is acknowledged

`bool acknowledged = 14 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The acknowledged.  
  
### getAcknowledgementTime()
    
    
    public abstract Timestamp getAcknowledgementTime()

Optional. Timestamp when this violation was acknowledged last. This will be absent when acknowledged field is marked as false.

` optional .google.protobuf.Timestamp acknowledgement_time = 15 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The acknowledgementTime.  
  
### getAcknowledgementTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getAcknowledgementTimeOrBuilder()

Optional. Timestamp when this violation was acknowledged last. This will be absent when acknowledged field is marked as false.

` optional .google.protobuf.Timestamp acknowledgement_time = 15 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getAuditLogLink()
    
    
    public abstract String getAuditLogLink()

Output only. Immutable. Audit Log Link for violated resource Format: https://console.cloud.google.com/logs/query;query={logName}{protoPayload.resourceName}{timeRange}{folder}

` string audit_log_link = 11 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The auditLogLink.  
  
### getAuditLogLinkBytes()
    
    
    public abstract ByteString getAuditLogLinkBytes()

Output only. Immutable. Audit Log Link for violated resource Format: https://console.cloud.google.com/logs/query;query={logName}{protoPayload.resourceName}{timeRange}{folder}

` string audit_log_link = 11 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for auditLogLink.  
  
### getBeginTime()
    
    
    public abstract Timestamp getBeginTime()

Output only. Time of the event which triggered the Violation.

`.google.protobuf.Timestamp begin_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The beginTime.  
  
### getBeginTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getBeginTimeOrBuilder()

Output only. Time of the event which triggered the Violation.

`.google.protobuf.Timestamp begin_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getCategory()
    
    
    public abstract String getCategory()

Output only. Category under which this violation is mapped. e.g. Location, Service Usage, Access, Encryption, etc.

`string category = 6 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The category.  
  
### getCategoryBytes()
    
    
    public abstract ByteString getCategoryBytes()

Output only. Category under which this violation is mapped. e.g. Location, Service Usage, Access, Encryption, etc.

`string category = 6 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for category.  
  
### getDescription()
    
    
    public abstract String getDescription()

Output only. Description for the Violation. e.g. OrgPolicy gcp.resourceLocations has non compliant value.

`string description = 2 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The description.  
  
### getDescriptionBytes()
    
    
    public abstract ByteString getDescriptionBytes()

Output only. Description for the Violation. e.g. OrgPolicy gcp.resourceLocations has non compliant value.

`string description = 2 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for description.  
  
### getExceptionAuditLogLink()
    
    
    public abstract String getExceptionAuditLogLink()

Output only. Immutable. Audit Log link to find business justification provided for violation exception. Format: https://console.cloud.google.com/logs/query;query={logName}{protoPayload.resourceName}{protoPayload.methodName}{timeRange}{organization}

` string exception_audit_log_link = 16 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The exceptionAuditLogLink.  
  
### getExceptionAuditLogLinkBytes()
    
    
    public abstract ByteString getExceptionAuditLogLinkBytes()

Output only. Immutable. Audit Log link to find business justification provided for violation exception. Format: https://console.cloud.google.com/logs/query;query={logName}{protoPayload.resourceName}{protoPayload.methodName}{timeRange}{organization}

` string exception_audit_log_link = 16 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for exceptionAuditLogLink.  
  
### getName()
    
    
    public abstract String getName()

Output only. Immutable. Name of the Violation. Format: organizations/{organization}/locations/{location}/workloads/{workload_id}/violations/{violations_id}

` string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Output only. Immutable. Name of the Violation. Format: organizations/{organization}/locations/{location}/workloads/{workload_id}/violations/{violations_id}

` string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getNonCompliantOrgPolicy()
    
    
    public abstract String getNonCompliantOrgPolicy()

Output only. Immutable. Name of the OrgPolicy which was modified with non-compliant change and resulted this violation. Format: projects/{project_number}/policies/{constraint_name} folders/{folder_id}/policies/{constraint_name} organizations/{organization_id}/policies/{constraint_name}

` string non_compliant_org_policy = 12 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The nonCompliantOrgPolicy.  
  
### getNonCompliantOrgPolicyBytes()
    
    
    public abstract ByteString getNonCompliantOrgPolicyBytes()

Output only. Immutable. Name of the OrgPolicy which was modified with non-compliant change and resulted this violation. Format: projects/{project_number}/policies/{constraint_name} folders/{folder_id}/policies/{constraint_name} organizations/{organization_id}/policies/{constraint_name}

` string non_compliant_org_policy = 12 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for nonCompliantOrgPolicy.  
  
### getOrgPolicyConstraint()
    
    
    public abstract String getOrgPolicyConstraint()

Output only. Immutable. The org-policy-constraint that was incorrectly changed, which resulted in this violation.

` string org_policy_constraint = 8 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The orgPolicyConstraint.  
  
### getOrgPolicyConstraintBytes()
    
    
    public abstract ByteString getOrgPolicyConstraintBytes()

Output only. Immutable. The org-policy-constraint that was incorrectly changed, which resulted in this violation.

` string org_policy_constraint = 8 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for orgPolicyConstraint.  
  
### getRemediation()
    
    
    public abstract Violation.Remediation getRemediation()

Output only. Compliance violation remediation

` .google.cloud.assuredworkloads.v1.Violation.Remediation remediation = 13 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Violation.Remediation](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.Violation.Remediation)` | The remediation.  
  
### getRemediationOrBuilder()
    
    
    public abstract Violation.RemediationOrBuilder getRemediationOrBuilder()

Output only. Compliance violation remediation

` .google.cloud.assuredworkloads.v1.Violation.Remediation remediation = 13 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Violation.RemediationOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.Violation.RemediationOrBuilder)` |   
  
### getResolveTime()
    
    
    public abstract Timestamp getResolveTime()

Output only. Time of the event which fixed the Violation. If the violation is ACTIVE this will be empty.

`.google.protobuf.Timestamp resolve_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The resolveTime.  
  
### getResolveTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getResolveTimeOrBuilder()

Output only. Time of the event which fixed the Violation. If the violation is ACTIVE this will be empty.

`.google.protobuf.Timestamp resolve_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getState()
    
    
    public abstract Violation.State getState()

Output only. State of the violation

` .google.cloud.assuredworkloads.v1.Violation.State state = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Violation.State](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1.Violation.State)` | The state.  
  
### getStateValue()
    
    
    public abstract int getStateValue()

Output only. State of the violation

` .google.cloud.assuredworkloads.v1.Violation.State state = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for state.  
  
### getUpdateTime()
    
    
    public abstract Timestamp getUpdateTime()

Output only. The last time when the Violation record was updated.

`.google.protobuf.Timestamp update_time = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The updateTime.  
  
### getUpdateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getUpdateTimeOrBuilder()

Output only. The last time when the Violation record was updated.

`.google.protobuf.Timestamp update_time = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### hasAcknowledgementTime()
    
    
    public abstract boolean hasAcknowledgementTime()

Optional. Timestamp when this violation was acknowledged last. This will be absent when acknowledged field is marked as false.

` optional .google.protobuf.Timestamp acknowledgement_time = 15 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the acknowledgementTime field is set.  
  
### hasBeginTime()
    
    
    public abstract boolean hasBeginTime()

Output only. Time of the event which triggered the Violation.

`.google.protobuf.Timestamp begin_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the beginTime field is set.  
  
### hasRemediation()
    
    
    public abstract boolean hasRemediation()

Output only. Compliance violation remediation

` .google.cloud.assuredworkloads.v1.Violation.Remediation remediation = 13 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the remediation field is set.  
  
### hasResolveTime()
    
    
    public abstract boolean hasResolveTime()

Output only. Time of the event which fixed the Violation. If the violation is ACTIVE this will be empty.

`.google.protobuf.Timestamp resolve_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the resolveTime field is set.  
  
### hasUpdateTime()
    
    
    public abstract boolean hasUpdateTime()

Output only. The last time when the Violation record was updated.

`.google.protobuf.Timestamp update_time = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the updateTime field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
