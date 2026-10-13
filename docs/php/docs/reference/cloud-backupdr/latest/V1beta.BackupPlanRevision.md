---
url: https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BackupPlanRevision
title: Google Cloud Backup Dr V1beta Client - Class BackupPlanRevision (0.15.1) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:19:07.601257+00:00
---

# Google Cloud Backup Dr V1beta Client - Class BackupPlanRevision (0.15.1)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BackupPlanRevision

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Backup Dr V1beta Client - Class BackupPlanRevision (0.15.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.15.1 (latest)  0.13.2  0.12.1  0.11.1  0.10.0  0.9.0  0.8.1  0.7.0  0.6.2  0.5.1  0.4.2  0.3.0  0.2.0  0.1.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Backup Dr V1beta Client class BackupPlanRevision.

`BackupPlanRevision` represents a snapshot of a `BackupPlan` at a point in time.

Generated from protobuf message `google.cloud.backupdr.v1beta.BackupPlanRevision`

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
Output only. Identifier. The resource name of the `BackupPlanRevision`. Format: `projects/{project}/locations/{location}/backupPlans/{backup_plan}/revisions/{revision}`  
`↳ revision_id` |  `string`   
Output only. The user friendly revision ID of the `BackupPlanRevision`. Example: v0, v1, v2, etc.  
`↳ state` |  `int`   
Output only. Resource State  
`↳ backup_plan_snapshot` |  `[BackupPlan](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BackupPlan)`   
The Backup Plan being encompassed by this revision.  
`↳ create_time` |  `Google\Protobuf\Timestamp`   
Output only. The timestamp that the revision was created.  
  
### getName

Output only. Identifier. The resource name of the `BackupPlanRevision`.

Format: `projects/{project}/locations/{location}/backupPlans/{backup_plan}/revisions/{revision}`

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setName

Output only. Identifier. The resource name of the `BackupPlanRevision`.

Format: `projects/{project}/locations/{location}/backupPlans/{backup_plan}/revisions/{revision}`

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getRevisionId

Output only. The user friendly revision ID of the `BackupPlanRevision`.

Example: v0, v1, v2, etc.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setRevisionId

Output only. The user friendly revision ID of the `BackupPlanRevision`.

Example: v0, v1, v2, etc.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getState

Output only. Resource State

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [State](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BackupPlanRevision.State).  
  
### setState

Output only. Resource State

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [State](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BackupPlanRevision.State).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getBackupPlanSnapshot

The Backup Plan being encompassed by this revision.

**Returns**  
---  
**Type** | **Description**  
`[BackupPlan](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BackupPlan)|null` |   
  
### hasBackupPlanSnapshot

### clearBackupPlanSnapshot

### setBackupPlanSnapshot

The Backup Plan being encompassed by this revision.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[BackupPlan](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BackupPlan)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCreateTime

Output only. The timestamp that the revision was created.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasCreateTime

### clearCreateTime

### setCreateTime

Output only. The timestamp that the revision was created.

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
