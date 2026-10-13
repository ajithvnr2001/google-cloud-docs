---
url: https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.AutoProtectionPolicy
title: Google Cloud Backup Dr V1beta Client - Class AutoProtectionPolicy (0.15.1) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:19:04.074982+00:00
---

# Google Cloud Backup Dr V1beta Client - Class AutoProtectionPolicy (0.15.1)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.AutoProtectionPolicy

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Backup Dr V1beta Client - Class AutoProtectionPolicy (0.15.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.15.1 (latest)  0.13.2  0.12.1  0.11.1  0.10.0  0.9.0  0.8.1  0.7.0  0.6.2  0.5.1  0.4.2  0.3.0  0.2.0  0.1.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Backup Dr V1beta Client class AutoProtectionPolicy.

An AutoprotectionPolicy is a policy resource designed to automate backup management, moving from manual per-resource protection to a bulk approach.

The policy dynamically discovers and applies a specified backup plan to all eligible resources that match its defined scope and criteria.

Generated from protobuf message `google.cloud.backupdr.v1beta.AutoProtectionPolicy`

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
Identifier. The resource name of the AutoprotectionPolicy. Format: `projects/{project}/locations/{location}/autoProtectionPolicies/{auto_protection_policy}`  
`↳ description` |  `string`   
Optional. A description of the policy.  
`↳ backup_plan_details` |  `array<[BackupPlanDetail](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BackupPlanDetail)>`   
Required. The backup plan details for matching resources.  
`↳ criteria` |  `[Criteria](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Criteria)`   
Required. The criteria for matching resources.  
`↳ state` |  `int`   
Output only. The current state of the AutoprotectionPolicy.  
`↳ etag` |  `string`   
Output only. The etag for the policy. If this is provided on update, it must match the server's etag, otherwise the request will be rejected with an ABORTED error.  
`↳ binding_summary` |  `[BindingSummary](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BindingSummary)`   
Output only. Summary of total count of different containers covered through this policy.  
`↳ policy_evaluation_summary` |  `[PolicyEvaluationSummary](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.PolicyEvaluationSummary)`   
Output only. Summary of last policy application when job was run per workload type.  
`↳ create_time` |  `Google\Protobuf\Timestamp`   
Output only. The timestamp when the policy was created.  
`↳ update_time` |  `Google\Protobuf\Timestamp`   
Output only. The timestamp when the policy was last updated.  
  
### getName

Identifier. The resource name of the AutoprotectionPolicy.

Format: `projects/{project}/locations/{location}/autoProtectionPolicies/{auto_protection_policy}`

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setName

Identifier. The resource name of the AutoprotectionPolicy.

Format: `projects/{project}/locations/{location}/autoProtectionPolicies/{auto_protection_policy}`

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDescription

Optional. A description of the policy.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setDescription

Optional. A description of the policy.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getBackupPlanDetails

Required. The backup plan details for matching resources.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\RepeatedField<[BackupPlanDetail](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BackupPlanDetail)>` |   
  
### setBackupPlanDetails

Required. The backup plan details for matching resources.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `array<[BackupPlanDetail](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BackupPlanDetail)>`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCriteria

Required. The criteria for matching resources.

**Returns**  
---  
**Type** | **Description**  
`[Criteria](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Criteria)|null` |   
  
### hasCriteria

### clearCriteria

### setCriteria

Required. The criteria for matching resources.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Criteria](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.Criteria)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getState

Output only. The current state of the AutoprotectionPolicy.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [State](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.AutoProtectionPolicy.State).  
  
### setState

Output only. The current state of the AutoprotectionPolicy.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [State](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.AutoProtectionPolicy.State).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getEtag

Output only. The etag for the policy.

If this is provided on update, it must match the server's etag, otherwise the request will be rejected with an ABORTED error.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setEtag

Output only. The etag for the policy.

If this is provided on update, it must match the server's etag, otherwise the request will be rejected with an ABORTED error.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getBindingSummary

Output only. Summary of total count of different containers covered through this policy.

**Returns**  
---  
**Type** | **Description**  
`[BindingSummary](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BindingSummary)|null` |   
  
### hasBindingSummary

### clearBindingSummary

### setBindingSummary

Output only. Summary of total count of different containers covered through this policy.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[BindingSummary](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BindingSummary)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPolicyEvaluationSummary

Output only. Summary of last policy application when job was run per workload type.

**Returns**  
---  
**Type** | **Description**  
`[PolicyEvaluationSummary](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.PolicyEvaluationSummary)|null` |   
  
### hasPolicyEvaluationSummary

### clearPolicyEvaluationSummary

### setPolicyEvaluationSummary

Output only. Summary of last policy application when job was run per workload type.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[PolicyEvaluationSummary](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.PolicyEvaluationSummary)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCreateTime

Output only. The timestamp when the policy was created.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasCreateTime

### clearCreateTime

### setCreateTime

Output only. The timestamp when the policy was created.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getUpdateTime

Output only. The timestamp when the policy was last updated.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasUpdateTime

### clearUpdateTime

### setUpdateTime

Output only. The timestamp when the policy was last updated.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
