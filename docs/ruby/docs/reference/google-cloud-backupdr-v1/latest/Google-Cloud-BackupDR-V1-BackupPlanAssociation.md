---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupPlanAssociation/
title: Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::BackupPlanAssociation (v1.11.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:47:37.216262+00:00
---

# Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::BackupPlanAssociation (v1.11.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupPlanAssociation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::BackupPlanAssociation (v1.11.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.11.2 (latest)  1.11.1  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.5.0  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Backup and DR Service V1 API class Google::Cloud::BackupDR::V1::BackupPlanAssociation.

A BackupPlanAssociation represents a single BackupPlanAssociation which contains details like workload, backup plan etc

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #alloydb_cluster_backup_plan_association_properties
    
    
    def alloydb_cluster_backup_plan_association_properties() -> ::Google::Cloud::BackupDR::V1::AlloyDBClusterBackupPlanAssociationProperties

**Returns**

  * ([::Google::Cloud::BackupDR::V1::AlloyDBClusterBackupPlanAssociationProperties](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-AlloyDBClusterBackupPlanAssociationProperties)) — Output only. AlloyDB cluster's backup plan association properties.

Note: The following fields are mutually exclusive: `alloydb_cluster_backup_plan_association_properties`, `cloud_sql_instance_backup_plan_association_properties`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #backup_plan
    
    
    def backup_plan() -> ::String

**Returns**

  * (::String) — Required. Resource name of backup plan which needs to be applied on workload. Format: projects/{project}/locations/{location}/backupPlans/{backupPlanId} 



### #backup_plan=
    
    
    def backup_plan=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Resource name of backup plan which needs to be applied on workload. Format: projects/{project}/locations/{location}/backupPlans/{backupPlanId} 



**Returns**

  * (::String) — Required. Resource name of backup plan which needs to be applied on workload. Format: projects/{project}/locations/{location}/backupPlans/{backupPlanId} 



### #backup_plan_revision_id
    
    
    def backup_plan_revision_id() -> ::String

**Returns**

  * (::String) — Output only. The user friendly revision ID of the `BackupPlanRevision`.

Example: v0, v1, v2, etc. 




### #backup_plan_revision_name
    
    
    def backup_plan_revision_name() -> ::String

**Returns**

  * (::String) — Output only. The resource id of the `BackupPlanRevision`.

Format: `projects/{project}/locations/{location}/backupPlans/{backup_plan}/revisions/{revision_id}`




### #cloud_sql_instance_backup_plan_association_properties
    
    
    def cloud_sql_instance_backup_plan_association_properties() -> ::Google::Cloud::BackupDR::V1::CloudSqlInstanceBackupPlanAssociationProperties

**Returns**

  * ([::Google::Cloud::BackupDR::V1::CloudSqlInstanceBackupPlanAssociationProperties](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-CloudSqlInstanceBackupPlanAssociationProperties)) — Output only. Cloud SQL instance's backup plan association properties.

Note: The following fields are mutually exclusive: `cloud_sql_instance_backup_plan_association_properties`, `alloydb_cluster_backup_plan_association_properties`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Protobuf-Timestamp)) — Output only. The time when the instance was created. 



### #data_source
    
    
    def data_source() -> ::String

**Returns**

  * (::String) — Output only. Resource name of data source which will be used as storage location for backups taken. Format : projects/{project}/locations/{location}/backupVaults/{backupvault}/dataSources/{datasource} 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Output only. Identifier. The resource name of BackupPlanAssociation in below format Format : projects/{project}/locations/{location}/backupPlanAssociations/{backupPlanAssociationId} 



### #resource
    
    
    def resource() -> ::String

**Returns**

  * (::String) — Required. Immutable. Resource name of workload on which the backup plan is applied.

The format can either be the resource name (e.g., "projects/my-project/zones/us-central1-a/instances/my-instance") or the full resource URI (e.g., "https://www.googleapis.com/compute/v1/projects/my-project/zones/us-central1-a/instances/my-instance"). 




### #resource=
    
    
    def resource=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Immutable. Resource name of workload on which the backup plan is applied.

The format can either be the resource name (e.g., "projects/my-project/zones/us-central1-a/instances/my-instance") or the full resource URI (e.g., "https://www.googleapis.com/compute/v1/projects/my-project/zones/us-central1-a/instances/my-instance"). 




**Returns**

  * (::String) — Required. Immutable. Resource name of workload on which the backup plan is applied.

The format can either be the resource name (e.g., "projects/my-project/zones/us-central1-a/instances/my-instance") or the full resource URI (e.g., "https://www.googleapis.com/compute/v1/projects/my-project/zones/us-central1-a/instances/my-instance"). 




### #resource_type
    
    
    def resource_type() -> ::String

**Returns**

  * (::String) — Required. Immutable. Resource type of workload on which backupplan is applied 



### #resource_type=
    
    
    def resource_type=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Immutable. Resource type of workload on which backupplan is applied 



**Returns**

  * (::String) — Required. Immutable. Resource type of workload on which backupplan is applied 



### #rules_config_info
    
    
    def rules_config_info() -> ::Array<::Google::Cloud::BackupDR::V1::RuleConfigInfo>

**Returns**

  * (::Array<[::Google::Cloud::BackupDR::V1::RuleConfigInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-RuleConfigInfo)>) — Output only. The config info related to backup rules. 



### #state
    
    
    def state() -> ::Google::Cloud::BackupDR::V1::BackupPlanAssociation::State

**Returns**

  * ([::Google::Cloud::BackupDR::V1::BackupPlanAssociation::State](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupPlanAssociation-State)) — Output only. The BackupPlanAssociation resource state. 



### #update_time
    
    
    def update_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Protobuf-Timestamp)) — Output only. The time when the instance was updated. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
