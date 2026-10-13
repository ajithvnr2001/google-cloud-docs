---
url: https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BackupPlanAssociation
title: Google Cloud Backup Dr V1beta Client - Class BackupPlanAssociation (0.15.1) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:19:06.970540+00:00
---

# Google Cloud Backup Dr V1beta Client - Class BackupPlanAssociation (0.15.1)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BackupPlanAssociation

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Backup Dr V1beta Client - Class BackupPlanAssociation (0.15.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.15.1 (latest)  0.13.2  0.12.1  0.11.1  0.10.0  0.9.0  0.8.1  0.7.0  0.6.2  0.5.1  0.4.2  0.3.0  0.2.0  0.1.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Backup Dr V1beta Client class BackupPlanAssociation.

A BackupPlanAssociation represents a single BackupPlanAssociation which contains details like workload, backup plan etc

Generated from protobuf message `google.cloud.backupdr.v1beta.BackupPlanAssociation`

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
`↳ cloud_sql_instance_backup_plan_association_properties` |  `[CloudSqlInstanceBackupPlanAssociationProperties](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.CloudSqlInstanceBackupPlanAssociationProperties)`   
Output only. Cloud SQL instance's backup plan association properties.  
`↳ alloydb_cluster_backup_plan_association_properties` |  `[AlloyDBClusterBackupPlanAssociationProperties](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.AlloyDBClusterBackupPlanAssociationProperties)`   
Output only. AlloyDB cluster's backup plan association properties.  
`↳ name` |  `string`   
Output only. Identifier. The resource name of BackupPlanAssociation in below format Format : projects/{project}/locations/{location}/backupPlanAssociations/{backupPlanAssociationId}  
`↳ resource_type` |  `string`   
Required. Immutable. Resource type of workload on which backupplan is applied  
`↳ resource` |  `string`   
Required. Immutable. Resource name of workload on which the backup plan is applied. The format can either be the resource name (e.g., "projects/my-project/zones/us-central1-a/instances/my-instance") or the full resource URI (e.g., "<https://www.googleapis.com/compute/v1/projects/my-project/zones/us-central1-a/instances/my-instance>").  
`↳ backup_plan` |  `string`   
Required. Resource name of backup plan which needs to be applied on workload. Format: projects/{project}/locations/{location}/backupPlans/{backupPlanId}  
`↳ create_time` |  `Google\Protobuf\Timestamp`   
Output only. The time when the instance was created.  
`↳ update_time` |  `Google\Protobuf\Timestamp`   
Output only. The time when the instance was updated.  
`↳ state` |  `int`   
Output only. The BackupPlanAssociation resource state.  
`↳ rules_config_info` |  `array<[RuleConfigInfo](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.RuleConfigInfo)>`   
Output only. The config info related to backup rules.  
`↳ data_source` |  `string`   
Output only. Resource name of data source which will be used as storage location for backups taken. Format : projects/{project}/locations/{location}/backupVaults/{backupvault}/dataSources/{datasource}  
`↳ backup_plan_revision_id` |  `string`   
Output only. The user friendly revision ID of the `BackupPlanRevision`. Example: v0, v1, v2, etc.  
`↳ backup_plan_revision_name` |  `string`   
Output only. The resource id of the `BackupPlanRevision`. Format: `projects/{project}/locations/{location}/backupPlans/{backup_plan}/revisions/{revision_id}`  
`↳ auto_protection_policy_binding` |  `string`   
Output only. The resource name of the `AutoProtectionPolicyBinding` that manages this association, if any. Format: `projects/{project}/locations/{location}/autoProtectionPolicies/{policy}/bindings/{binding}`.  
  
### getCloudSqlInstanceBackupPlanAssociationProperties

Output only. Cloud SQL instance's backup plan association properties.

**Returns**  
---  
**Type** | **Description**  
`[CloudSqlInstanceBackupPlanAssociationProperties](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.CloudSqlInstanceBackupPlanAssociationProperties)|null` |   
  
### hasCloudSqlInstanceBackupPlanAssociationProperties

### setCloudSqlInstanceBackupPlanAssociationProperties

Output only. Cloud SQL instance's backup plan association properties.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[CloudSqlInstanceBackupPlanAssociationProperties](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.CloudSqlInstanceBackupPlanAssociationProperties)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getAlloydbClusterBackupPlanAssociationProperties

Output only. AlloyDB cluster's backup plan association properties.

**Returns**  
---  
**Type** | **Description**  
`[AlloyDBClusterBackupPlanAssociationProperties](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.AlloyDBClusterBackupPlanAssociationProperties)|null` |   
  
### hasAlloydbClusterBackupPlanAssociationProperties

### setAlloydbClusterBackupPlanAssociationProperties

Output only. AlloyDB cluster's backup plan association properties.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[AlloyDBClusterBackupPlanAssociationProperties](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.AlloyDBClusterBackupPlanAssociationProperties)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getName

Output only. Identifier. The resource name of BackupPlanAssociation in below format Format : projects/{project}/locations/{location}/backupPlanAssociations/{backupPlanAssociationId}

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setName

Output only. Identifier. The resource name of BackupPlanAssociation in below format Format : projects/{project}/locations/{location}/backupPlanAssociations/{backupPlanAssociationId}

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getResourceType

Required. Immutable. Resource type of workload on which backupplan is applied

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setResourceType

Required. Immutable. Resource type of workload on which backupplan is applied

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getResource

Required. Immutable. Resource name of workload on which the backup plan is applied.

The format can either be the resource name (e.g., "projects/my-project/zones/us-central1-a/instances/my-instance") or the full resource URI (e.g., "<https://www.googleapis.com/compute/v1/projects/my-project/zones/us-central1-a/instances/my-instance>").

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setResource

Required. Immutable. Resource name of workload on which the backup plan is applied.

The format can either be the resource name (e.g., "projects/my-project/zones/us-central1-a/instances/my-instance") or the full resource URI (e.g., "<https://www.googleapis.com/compute/v1/projects/my-project/zones/us-central1-a/instances/my-instance>").

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getBackupPlan

Required. Resource name of backup plan which needs to be applied on workload. Format: projects/{project}/locations/{location}/backupPlans/{backupPlanId}

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setBackupPlan

Required. Resource name of backup plan which needs to be applied on workload. Format: projects/{project}/locations/{location}/backupPlans/{backupPlanId}

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCreateTime

Output only. The time when the instance was created.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasCreateTime

### clearCreateTime

### setCreateTime

Output only. The time when the instance was created.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getUpdateTime

Output only. The time when the instance was updated.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasUpdateTime

### clearUpdateTime

### setUpdateTime

Output only. The time when the instance was updated.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getState

Output only. The BackupPlanAssociation resource state.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [State](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BackupPlanAssociation.State).  
  
### setState

Output only. The BackupPlanAssociation resource state.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [State](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.BackupPlanAssociation.State).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getRulesConfigInfo

Output only. The config info related to backup rules.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\RepeatedField<[RuleConfigInfo](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.RuleConfigInfo)>` |   
  
### setRulesConfigInfo

Output only. The config info related to backup rules.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `array<[RuleConfigInfo](https://docs.cloud.google.com/php/docs/reference/cloud-backupdr/latest/V1beta.RuleConfigInfo)>`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDataSource

Output only. Resource name of data source which will be used as storage location for backups taken. Format : projects/{project}/locations/{location}/backupVaults/{backupvault}/dataSources/{datasource}

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setDataSource

Output only. Resource name of data source which will be used as storage location for backups taken. Format : projects/{project}/locations/{location}/backupVaults/{backupvault}/dataSources/{datasource}

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getBackupPlanRevisionId

Output only. The user friendly revision ID of the `BackupPlanRevision`.

Example: v0, v1, v2, etc.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setBackupPlanRevisionId

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
  
### getBackupPlanRevisionName

Output only. The resource id of the `BackupPlanRevision`.

Format: `projects/{project}/locations/{location}/backupPlans/{backup_plan}/revisions/{revision_id}`

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setBackupPlanRevisionName

Output only. The resource id of the `BackupPlanRevision`.

Format: `projects/{project}/locations/{location}/backupPlans/{backup_plan}/revisions/{revision_id}`

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getAutoProtectionPolicyBinding

Output only. The resource name of the `AutoProtectionPolicyBinding` that manages this association, if any.

Format: `projects/{project}/locations/{location}/autoProtectionPolicies/{policy}/bindings/{binding}`.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setAutoProtectionPolicyBinding

Output only. The resource name of the `AutoProtectionPolicyBinding` that manages this association, if any.

Format: `projects/{project}/locations/{location}/autoProtectionPolicies/{policy}/bindings/{binding}`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getResourceProperties

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
