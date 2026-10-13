---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.AutoProtectionPolicyOrBuilder
title: Interface AutoProtectionPolicyOrBuilder (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:34:54.022956+00:00
---

# Interface AutoProtectionPolicyOrBuilder (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.AutoProtectionPolicyOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface AutoProtectionPolicyOrBuilder (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface AutoProtectionPolicyOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getBackupPlanDetails(int index)
    
    
    public abstract BackupPlanDetail getBackupPlanDetails(int index)

Required. The backup plan details for matching resources.

` repeated .google.cloud.backupdr.v1beta.BackupPlanDetail backup_plan_details = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BackupPlanDetail](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.BackupPlanDetail)` |   
  
### getBackupPlanDetailsCount()
    
    
    public abstract int getBackupPlanDetailsCount()

Required. The backup plan details for matching resources.

` repeated .google.cloud.backupdr.v1beta.BackupPlanDetail backup_plan_details = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getBackupPlanDetailsList()
    
    
    public abstract List<BackupPlanDetail> getBackupPlanDetailsList()

Required. The backup plan details for matching resources.

` repeated .google.cloud.backupdr.v1beta.BackupPlanDetail backup_plan_details = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[BackupPlanDetail](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.BackupPlanDetail)>` |   
  
### getBackupPlanDetailsOrBuilder(int index)
    
    
    public abstract BackupPlanDetailOrBuilder getBackupPlanDetailsOrBuilder(int index)

Required. The backup plan details for matching resources.

` repeated .google.cloud.backupdr.v1beta.BackupPlanDetail backup_plan_details = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BackupPlanDetailOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.BackupPlanDetailOrBuilder)` |   
  
### getBackupPlanDetailsOrBuilderList()
    
    
    public abstract List<? extends BackupPlanDetailOrBuilder> getBackupPlanDetailsOrBuilderList()

Required. The backup plan details for matching resources.

` repeated .google.cloud.backupdr.v1beta.BackupPlanDetail backup_plan_details = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.backupdr.v1beta.BackupPlanDetailOrBuilder>` |   
  
### getBindingSummary()
    
    
    public abstract BindingSummary getBindingSummary()

Output only. Summary of total count of different containers covered through this policy.

` .google.cloud.backupdr.v1beta.BindingSummary binding_summary = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[BindingSummary](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.BindingSummary)` | The bindingSummary.  
  
### getBindingSummaryOrBuilder()
    
    
    public abstract BindingSummaryOrBuilder getBindingSummaryOrBuilder()

Output only. Summary of total count of different containers covered through this policy.

` .google.cloud.backupdr.v1beta.BindingSummary binding_summary = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[BindingSummaryOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.BindingSummaryOrBuilder)` |   
  
### getCreateTime()
    
    
    public abstract Timestamp getCreateTime()

Output only. The timestamp when the policy was created.

`.google.protobuf.Timestamp create_time = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getCreateTimeOrBuilder()

Output only. The timestamp when the policy was created.

`.google.protobuf.Timestamp create_time = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getCriteria()
    
    
    public abstract Criteria getCriteria()

Required. The criteria for matching resources.

` .google.cloud.backupdr.v1beta.Criteria criteria = 4 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[Criteria](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.Criteria)` | The criteria.  
  
### getCriteriaOrBuilder()
    
    
    public abstract CriteriaOrBuilder getCriteriaOrBuilder()

Required. The criteria for matching resources.

` .google.cloud.backupdr.v1beta.Criteria criteria = 4 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[CriteriaOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.CriteriaOrBuilder)` |   
  
### getDescription()
    
    
    public abstract String getDescription()

Optional. A description of the policy.

`string description = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The description.  
  
### getDescriptionBytes()
    
    
    public abstract ByteString getDescriptionBytes()

Optional. A description of the policy.

`string description = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for description.  
  
### getEtag()
    
    
    public abstract String getEtag()

Output only. The etag for the policy. If this is provided on update, it must match the server's etag, otherwise the request will be rejected with an ABORTED error.

`string etag = 6;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The etag.  
  
### getEtagBytes()
    
    
    public abstract ByteString getEtagBytes()

Output only. The etag for the policy. If this is provided on update, it must match the server's etag, otherwise the request will be rejected with an ABORTED error.

`string etag = 6;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for etag.  
  
### getName()
    
    
    public abstract String getName()

Identifier. The resource name of the AutoprotectionPolicy. Format: `projects/{project}/locations/{location}/autoProtectionPolicies/{auto_protection_policy}`

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Identifier. The resource name of the AutoprotectionPolicy. Format: `projects/{project}/locations/{location}/autoProtectionPolicies/{auto_protection_policy}`

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getPolicyEvaluationSummary()
    
    
    public abstract PolicyEvaluationSummary getPolicyEvaluationSummary()

Output only. Summary of last policy application when job was run per workload type.

` .google.cloud.backupdr.v1beta.PolicyEvaluationSummary policy_evaluation_summary = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[PolicyEvaluationSummary](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.PolicyEvaluationSummary)` | The policyEvaluationSummary.  
  
### getPolicyEvaluationSummaryOrBuilder()
    
    
    public abstract PolicyEvaluationSummaryOrBuilder getPolicyEvaluationSummaryOrBuilder()

Output only. Summary of last policy application when job was run per workload type.

` .google.cloud.backupdr.v1beta.PolicyEvaluationSummary policy_evaluation_summary = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[PolicyEvaluationSummaryOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.PolicyEvaluationSummaryOrBuilder)` |   
  
### getState()
    
    
    public abstract AutoProtectionPolicy.State getState()

Output only. The current state of the AutoprotectionPolicy.

` .google.cloud.backupdr.v1beta.AutoProtectionPolicy.State state = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[AutoProtectionPolicy.State](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.AutoProtectionPolicy.State)` | The state.  
  
### getStateValue()
    
    
    public abstract int getStateValue()

Output only. The current state of the AutoprotectionPolicy.

` .google.cloud.backupdr.v1beta.AutoProtectionPolicy.State state = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for state.  
  
### getUpdateTime()
    
    
    public abstract Timestamp getUpdateTime()

Output only. The timestamp when the policy was last updated.

`.google.protobuf.Timestamp update_time = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The updateTime.  
  
### getUpdateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getUpdateTimeOrBuilder()

Output only. The timestamp when the policy was last updated.

`.google.protobuf.Timestamp update_time = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### hasBindingSummary()
    
    
    public abstract boolean hasBindingSummary()

Output only. Summary of total count of different containers covered through this policy.

` .google.cloud.backupdr.v1beta.BindingSummary binding_summary = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the bindingSummary field is set.  
  
### hasCreateTime()
    
    
    public abstract boolean hasCreateTime()

Output only. The timestamp when the policy was created.

`.google.protobuf.Timestamp create_time = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasCriteria()
    
    
    public abstract boolean hasCriteria()

Required. The criteria for matching resources.

` .google.cloud.backupdr.v1beta.Criteria criteria = 4 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the criteria field is set.  
  
### hasPolicyEvaluationSummary()
    
    
    public abstract boolean hasPolicyEvaluationSummary()

Output only. Summary of last policy application when job was run per workload type.

` .google.cloud.backupdr.v1beta.PolicyEvaluationSummary policy_evaluation_summary = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the policyEvaluationSummary field is set.  
  
### hasUpdateTime()
    
    
    public abstract boolean hasUpdateTime()

Output only. The timestamp when the policy was last updated.

`.google.protobuf.Timestamp update_time = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the updateTime field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
