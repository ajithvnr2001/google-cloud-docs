---
url: https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.AppliedAutoProtectionPolicy
title: Google Cloud Backup Dr V1beta Client - Class AppliedAutoProtectionPolicy (0.15.1) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:19:03.385737+00:00
---

# Google Cloud Backup Dr V1beta Client - Class AppliedAutoProtectionPolicy (0.15.1)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.AppliedAutoProtectionPolicy

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Backup Dr V1beta Client - Class AppliedAutoProtectionPolicy (0.15.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.15.1 (latest)  0.13.2  0.12.1  0.11.1  0.10.0  0.9.0  0.8.1  0.7.0  0.6.2  0.5.1  0.4.2  0.3.0  0.2.0  0.1.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Backup Dr V1beta Client class AppliedAutoProtectionPolicy.

AppliedAutoProtectionPolicy is a read-only view of AutoProtectionPolicy and AutoProtectionPolicyBinding resources that apply to a given workload project.

Generated from protobuf message `google.cloud.backupdr.v1beta.AppliedAutoProtectionPolicy`

## Namespace

Google \ Cloud \ BackupDR \ V1beta

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ name` |  `string`   
Identifier. Canonical resource name. Format: projects/{workload-project-number}/locations/{location}/appliedAutoProtectionPolicies/{id}.  
`↳ source_binding` |  `string`   
Output only. The full resource name of the AutoProtectionPolicyBinding that applies the source policy to a scope including this workload project. e.g., projects/{admin-project}/locations/{location}/autoProtectionPolicies/{policy_id}/autoProtectionPolicyBindings/{binding_id}.  
`↳ criteria` |  `[Criteria](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Criteria)`   
Output only. The criteria resources must meet for this rule to apply. From AutoProtectionPolicy.criteria.  
`↳ backup_plan_details` |  `array<[BackupPlanDetail](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BackupPlanDetail)>`   
Output only. The set of backup plan configurations, mirroring the backup_plan_details from the source AutoProtectionPolicy. Each element specifies a backup plan for a given resource type.  
`↳ update_time` |  `Google\Protobuf\Timestamp`   
Output only. Timestamp indicating when the binding was last modified.  
`↳ create_time` |  `Google\Protobuf\Timestamp`   
Output only. Timestamp indicating when the binding was last created.  
`↳ binding_evaluation_summary` |  `[BindingEvaluationSummary](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BindingEvaluationSummary)`   
Output only. The summary of the last policy application when the job has run.  
`↳ status` |  `int`   
Output only. The status of the applied auto protection policy.  
  
### getName

Identifier. Canonical resource name.

Format: projects/{workload-project-number}/locations/{location}/appliedAutoProtectionPolicies/{id}.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setName

Identifier. Canonical resource name.

Format: projects/{workload-project-number}/locations/{location}/appliedAutoProtectionPolicies/{id}.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getSourceBinding

Output only. The full resource name of the AutoProtectionPolicyBinding that applies the source policy to a scope including this workload project. e.g., projects/{admin-project}/locations/{location}/autoProtectionPolicies/{policy_id}/autoProtectionPolicyBindings/{binding_id}.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setSourceBinding

Output only. The full resource name of the AutoProtectionPolicyBinding that applies the source policy to a scope including this workload project. e.g., projects/{admin-project}/locations/{location}/autoProtectionPolicies/{policy_id}/autoProtectionPolicyBindings/{binding_id}.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCriteria

Output only. The criteria resources must meet for this rule to apply. From AutoProtectionPolicy.criteria.

**Returns**  
---  
**Type** | **Description**  
`[Criteria](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Criteria)|null` |   
  
### hasCriteria

### clearCriteria

### setCriteria

Output only. The criteria resources must meet for this rule to apply. From AutoProtectionPolicy.criteria.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Criteria](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Criteria)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getBackupPlanDetails

Output only. The set of backup plan configurations, mirroring the backup_plan_details from the source AutoProtectionPolicy. Each element specifies a backup plan for a given resource type.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\RepeatedField<[BackupPlanDetail](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BackupPlanDetail)>` |   
  
### setBackupPlanDetails

Output only. The set of backup plan configurations, mirroring the backup_plan_details from the source AutoProtectionPolicy. Each element specifies a backup plan for a given resource type.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `array<[BackupPlanDetail](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BackupPlanDetail)>`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getUpdateTime

Output only. Timestamp indicating when the binding was last modified.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasUpdateTime

### clearUpdateTime

### setUpdateTime

Output only. Timestamp indicating when the binding was last modified.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCreateTime

Output only. Timestamp indicating when the binding was last created.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasCreateTime

### clearCreateTime

### setCreateTime

Output only. Timestamp indicating when the binding was last created.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getBindingEvaluationSummary

Output only. The summary of the last policy application when the job has run.

**Returns**  
---  
**Type** | **Description**  
`[BindingEvaluationSummary](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BindingEvaluationSummary)|null` |   
  
### hasBindingEvaluationSummary

### clearBindingEvaluationSummary

### setBindingEvaluationSummary

Output only. The summary of the last policy application when the job has run.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[BindingEvaluationSummary](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BindingEvaluationSummary)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getStatus

Output only. The status of the applied auto protection policy.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [State](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.AppliedAutoProtectionPolicy.State).  
  
### setStatus

Output only. The status of the applied auto protection policy.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [State](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.AppliedAutoProtectionPolicy.State).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
