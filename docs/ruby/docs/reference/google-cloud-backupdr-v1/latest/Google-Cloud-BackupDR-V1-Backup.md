---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-Backup/
title: Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::Backup (v1.11.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:47:27.462780+00:00
---

# Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::Backup (v1.11.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-Backup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::Backup (v1.11.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.11.2 (latest)  1.11.1  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.5.0  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Backup and DR Service V1 API class Google::Cloud::BackupDR::V1::Backup.

Message describing a Backup object.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #alloy_db_backup_properties
    
    
    def alloy_db_backup_properties() -> ::Google::Cloud::BackupDR::V1::AlloyDbClusterBackupProperties

**Returns**

  * ([::Google::Cloud::BackupDR::V1::AlloyDbClusterBackupProperties](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-AlloyDbClusterBackupProperties)) — Output only. AlloyDB specific backup properties.

Note: The following fields are mutually exclusive: `alloy_db_backup_properties`, `compute_instance_backup_properties`, `cloud_sql_instance_backup_properties`, `backup_appliance_backup_properties`, `disk_backup_properties`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #backup_appliance_backup_properties
    
    
    def backup_appliance_backup_properties() -> ::Google::Cloud::BackupDR::V1::BackupApplianceBackupProperties

**Returns**

  * ([::Google::Cloud::BackupDR::V1::BackupApplianceBackupProperties](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupApplianceBackupProperties)) — Output only. Backup Appliance specific backup properties.

Note: The following fields are mutually exclusive: `backup_appliance_backup_properties`, `compute_instance_backup_properties`, `cloud_sql_instance_backup_properties`, `alloy_db_backup_properties`, `disk_backup_properties`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #backup_appliance_locks
    
    
    def backup_appliance_locks() -> ::Array<::Google::Cloud::BackupDR::V1::BackupLock>

**Returns**

  * (::Array<[::Google::Cloud::BackupDR::V1::BackupLock](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupLock)>) — Optional. The list of BackupLocks taken by the accessor Backup Appliance. 



### #backup_appliance_locks=
    
    
    def backup_appliance_locks=(value) -> ::Array<::Google::Cloud::BackupDR::V1::BackupLock>

**Parameter**

  * **value** (::Array<[::Google::Cloud::BackupDR::V1::BackupLock](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupLock)>) — Optional. The list of BackupLocks taken by the accessor Backup Appliance. 



**Returns**

  * (::Array<[::Google::Cloud::BackupDR::V1::BackupLock](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupLock)>) — Optional. The list of BackupLocks taken by the accessor Backup Appliance. 



### #backup_retention_inheritance
    
    
    def backup_retention_inheritance() -> ::Google::Cloud::BackupDR::V1::BackupVault::BackupRetentionInheritance

**Returns**

  * ([::Google::Cloud::BackupDR::V1::BackupVault::BackupRetentionInheritance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupVault-BackupRetentionInheritance)) — Output only. Setting for how the enforced retention end time is inherited. This value is copied from this backup's BackupVault. 



### #backup_type
    
    
    def backup_type() -> ::Google::Cloud::BackupDR::V1::Backup::BackupType

**Returns**

  * ([::Google::Cloud::BackupDR::V1::Backup::BackupType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-Backup-BackupType)) — Output only. Type of the backup, unspecified, scheduled or ondemand. 



### #cloud_sql_instance_backup_properties
    
    
    def cloud_sql_instance_backup_properties() -> ::Google::Cloud::BackupDR::V1::CloudSqlInstanceBackupProperties

**Returns**

  * ([::Google::Cloud::BackupDR::V1::CloudSqlInstanceBackupProperties](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-CloudSqlInstanceBackupProperties)) — Output only. Cloud SQL specific backup properties.

Note: The following fields are mutually exclusive: `cloud_sql_instance_backup_properties`, `compute_instance_backup_properties`, `backup_appliance_backup_properties`, `alloy_db_backup_properties`, `disk_backup_properties`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #compute_instance_backup_properties
    
    
    def compute_instance_backup_properties() -> ::Google::Cloud::BackupDR::V1::ComputeInstanceBackupProperties

**Returns**

  * ([::Google::Cloud::BackupDR::V1::ComputeInstanceBackupProperties](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ComputeInstanceBackupProperties)) — Output only. Compute Engine specific backup properties.

Note: The following fields are mutually exclusive: `compute_instance_backup_properties`, `cloud_sql_instance_backup_properties`, `backup_appliance_backup_properties`, `alloy_db_backup_properties`, `disk_backup_properties`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #consistency_time
    
    
    def consistency_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Protobuf-Timestamp)) — Output only. The point in time when this backup was captured from the source. 



### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Protobuf-Timestamp)) — Output only. The time when the instance was created. 



### #description
    
    
    def description() -> ::String

**Returns**

  * (::String) — Output only. The description of the Backup instance (2048 characters or less). 



### #disk_backup_properties
    
    
    def disk_backup_properties() -> ::Google::Cloud::BackupDR::V1::DiskBackupProperties

**Returns**

  * ([::Google::Cloud::BackupDR::V1::DiskBackupProperties](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DiskBackupProperties)) — Output only. Disk specific backup properties.

Note: The following fields are mutually exclusive: `disk_backup_properties`, `compute_instance_backup_properties`, `cloud_sql_instance_backup_properties`, `backup_appliance_backup_properties`, `alloy_db_backup_properties`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #enforced_retention_end_time
    
    
    def enforced_retention_end_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Protobuf-Timestamp)) — Optional. The backup can not be deleted before this time. 



### #enforced_retention_end_time=
    
    
    def enforced_retention_end_time=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Protobuf-Timestamp)) — Optional. The backup can not be deleted before this time. 



**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Protobuf-Timestamp)) — Optional. The backup can not be deleted before this time. 



### #etag
    
    
    def etag() -> ::String

**Returns**

  * (::String) — Optional. Server specified ETag to prevent updates from overwriting each other. 



### #etag=
    
    
    def etag=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Server specified ETag to prevent updates from overwriting each other. 



**Returns**

  * (::String) — Optional. Server specified ETag to prevent updates from overwriting each other. 



### #expire_time
    
    
    def expire_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Protobuf-Timestamp)) — Optional. When this backup is automatically expired. 



### #expire_time=
    
    
    def expire_time=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Protobuf-Timestamp)) — Optional. When this backup is automatically expired. 



**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Protobuf-Timestamp)) — Optional. When this backup is automatically expired. 



### #gcp_backup_plan_info
    
    
    def gcp_backup_plan_info() -> ::Google::Cloud::BackupDR::V1::Backup::GCPBackupPlanInfo

**Returns**

  * ([::Google::Cloud::BackupDR::V1::Backup::GCPBackupPlanInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-Backup-GCPBackupPlanInfo)) — Output only. Configuration for a Google Cloud resource. 



### #gcp_resource
    
    
    def gcp_resource() -> ::Google::Cloud::BackupDR::V1::BackupGcpResource

**Returns**

  * ([::Google::Cloud::BackupDR::V1::BackupGcpResource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupGcpResource)) — Output only. Unique identifier of the GCP resource that is being backed up. 



### #kms_key_versions
    
    
    def kms_key_versions() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Optional. Output only. The list of KMS key versions used to encrypt the backup. 



### #labels
    
    
    def labels() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. Resource labels to represent user provided metadata. No labels currently defined. 



### #labels=
    
    
    def labels=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Optional. Resource labels to represent user provided metadata. No labels currently defined. 



**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. Resource labels to represent user provided metadata. No labels currently defined. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Output only. Identifier. Name of the backup to create. It must have the format`"projects/<project>/locations/<location>/backupVaults/<backupvault>/dataSources/{datasource}/backups/{backup}"`. `{backup}` cannot be changed after creation. It must be between 3-63 characters long and must be unique within the datasource. 



### #resource_size_bytes
    
    
    def resource_size_bytes() -> ::Integer

**Returns**

  * (::Integer) — Output only. source resource size in bytes at the time of the backup. 



### #satisfies_pzi
    
    
    def satisfies_pzi() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. Output only. Reserved for future use. 



### #satisfies_pzs
    
    
    def satisfies_pzs() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. Output only. Reserved for future use. 



### #service_locks
    
    
    def service_locks() -> ::Array<::Google::Cloud::BackupDR::V1::BackupLock>

**Returns**

  * (::Array<[::Google::Cloud::BackupDR::V1::BackupLock](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupLock)>) — Output only. The list of BackupLocks taken by the service to prevent the deletion of the backup. 



### #state
    
    
    def state() -> ::Google::Cloud::BackupDR::V1::Backup::State

**Returns**

  * ([::Google::Cloud::BackupDR::V1::Backup::State](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-Backup-State)) — Output only. The Backup resource instance state. 



### #update_time
    
    
    def update_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Protobuf-Timestamp)) — Output only. The time when the instance was updated. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
