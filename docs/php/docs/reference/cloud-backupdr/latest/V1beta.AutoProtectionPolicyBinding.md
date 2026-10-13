---
url: https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.AutoProtectionPolicyBinding
title: Google Cloud Backup Dr V1beta Client - Class AutoProtectionPolicyBinding (0.15.1) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:19:04.342297+00:00
---

# Google Cloud Backup Dr V1beta Client - Class AutoProtectionPolicyBinding (0.15.1)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.AutoProtectionPolicyBinding

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Backup Dr V1beta Client - Class AutoProtectionPolicyBinding (0.15.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.15.1 (latest)  0.13.2  0.12.1  0.11.1  0.10.0  0.9.0  0.8.1  0.7.0  0.6.2  0.5.1  0.4.2  0.3.0  0.2.0  0.1.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Backup Dr V1beta Client class AutoProtectionPolicyBinding.

An AutoprotectionPolicyBinding (APPA) acts as the bridge between an AutoprotectionPolicy and the scope (Project, Folder, or Organization) where the policy should be applied.

Generated from protobuf message `google.cloud.backupdr.v1beta.AutoProtectionPolicyBinding`

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
Identifier. The resource name of the AutoProtectionPolicyBinding. Format: `projects/{project}/locations/{location}/autoProtectionPolicies/{auto_protection_policy}/bindings/{binding}`  
`↳ description` |  `string`   
Optional. A description of the binding.  
`↳ state` |  `int`   
Output only. The current state of the AutoProtectionPolicyBinding.  
`↳ scope` |  `string`   
Required. Immutable. Resource Id of target container on which policy will be applied. Format: projects/{project_id}  
`↳ binding_evaluation_summary` |  `[BindingEvaluationSummary](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BindingEvaluationSummary)`   
Output only. Summaries of the last policy application when the job has run, with one entry per resource type specified in the AutoProtectionPolicy.  
`↳ create_time` |  `Google\Protobuf\Timestamp`   
Output only. The timestamp when the binding was created.  
`↳ update_time` |  `Google\Protobuf\Timestamp`   
Output only. The timestamp when the binding was last updated.  
`↳ etag` |  `string`   
Optional. Output only. The etag for the binding. If this is provided on update, it must match the server's etag.  
  
### getName

Identifier. The resource name of the AutoProtectionPolicyBinding.

Format: `projects/{project}/locations/{location}/autoProtectionPolicies/{auto_protection_policy}/bindings/{binding}`

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setName

Identifier. The resource name of the AutoProtectionPolicyBinding.

Format: `projects/{project}/locations/{location}/autoProtectionPolicies/{auto_protection_policy}/bindings/{binding}`

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDescription

Optional. A description of the binding.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setDescription

Optional. A description of the binding.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getState

Output only. The current state of the AutoProtectionPolicyBinding.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [State](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.AutoProtectionPolicyBinding.State).  
  
### setState

Output only. The current state of the AutoProtectionPolicyBinding.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [State](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.AutoProtectionPolicyBinding.State).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getScope

Required. Immutable. Resource Id of target container on which policy will be applied. Format: projects/{project_id}

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setScope

Required. Immutable. Resource Id of target container on which policy will be applied. Format: projects/{project_id}

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getBindingEvaluationSummary

Output only. Summaries of the last policy application when the job has run, with one entry per resource type specified in the AutoProtectionPolicy.

**Returns**  
---  
**Type** | **Description**  
`[BindingEvaluationSummary](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BindingEvaluationSummary)|null` |   
  
### hasBindingEvaluationSummary

### clearBindingEvaluationSummary

### setBindingEvaluationSummary

Output only. Summaries of the last policy application when the job has run, with one entry per resource type specified in the AutoProtectionPolicy.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[BindingEvaluationSummary](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BindingEvaluationSummary)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCreateTime

Output only. The timestamp when the binding was created.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasCreateTime

### clearCreateTime

### setCreateTime

Output only. The timestamp when the binding was created.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getUpdateTime

Output only. The timestamp when the binding was last updated.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasUpdateTime

### clearUpdateTime

### setUpdateTime

Output only. The timestamp when the binding was last updated.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getEtag

Optional. Output only. The etag for the binding.

If this is provided on update, it must match the server's etag.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setEtag

Optional. Output only. The etag for the binding.

If this is provided on update, it must match the server's etag.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
