---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DataSource/
title: Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::DataSource (v1.11.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:47:42.895989+00:00
---

# Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::DataSource (v1.11.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DataSource/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::DataSource (v1.11.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.11.2 (latest)  1.11.1  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.5.0  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Backup and DR Service V1 API class Google::Cloud::BackupDR::V1::DataSource.

Message describing a DataSource object. Datasource object used to represent Datasource details for both admin and basic view.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #backup_blocked_by_vault_access_restriction
    
    
    def backup_blocked_by_vault_access_restriction() -> ::Boolean

**Returns**

  * (::Boolean) — Output only. This field is set to true if the backup is blocked by vault access restriction. 



### #backup_config_info
    
    
    def backup_config_info() -> ::Google::Cloud::BackupDR::V1::BackupConfigInfo

**Returns**

  * ([::Google::Cloud::BackupDR::V1::BackupConfigInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupConfigInfo)) — Output only. Details of how the resource is configured for backup. 



### #backup_count
    
    
    def backup_count() -> ::Integer

**Returns**

  * (::Integer) — Number of backups in the data source. 



### #backup_count=
    
    
    def backup_count=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Number of backups in the data source. 



**Returns**

  * (::Integer) — Number of backups in the data source. 



### #config_state
    
    
    def config_state() -> ::Google::Cloud::BackupDR::V1::BackupConfigState

**Returns**

  * ([::Google::Cloud::BackupDR::V1::BackupConfigState](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupConfigState)) — Output only. The backup configuration state. 



### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Protobuf-Timestamp)) — Output only. The time when the instance was created. 



### #data_source_backup_appliance_application
    
    
    def data_source_backup_appliance_application() -> ::Google::Cloud::BackupDR::V1::DataSourceBackupApplianceApplication

**Returns**

  * ([::Google::Cloud::BackupDR::V1::DataSourceBackupApplianceApplication](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DataSourceBackupApplianceApplication)) — The backed up resource is a backup appliance application.

Note: The following fields are mutually exclusive: `data_source_backup_appliance_application`, `data_source_gcp_resource`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #data_source_backup_appliance_application=
    
    
    def data_source_backup_appliance_application=(value) -> ::Google::Cloud::BackupDR::V1::DataSourceBackupApplianceApplication

**Parameter**

  * **value** ([::Google::Cloud::BackupDR::V1::DataSourceBackupApplianceApplication](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DataSourceBackupApplianceApplication)) — The backed up resource is a backup appliance application.

Note: The following fields are mutually exclusive: `data_source_backup_appliance_application`, `data_source_gcp_resource`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::BackupDR::V1::DataSourceBackupApplianceApplication](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DataSourceBackupApplianceApplication)) — The backed up resource is a backup appliance application.

Note: The following fields are mutually exclusive: `data_source_backup_appliance_application`, `data_source_gcp_resource`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #data_source_gcp_resource
    
    
    def data_source_gcp_resource() -> ::Google::Cloud::BackupDR::V1::DataSourceGcpResource

**Returns**

  * ([::Google::Cloud::BackupDR::V1::DataSourceGcpResource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DataSourceGcpResource)) — The backed up resource is a Google Cloud resource. The word 'DataSource' was included in the names to indicate that this is the representation of the Google Cloud resource used within the DataSource object.

Note: The following fields are mutually exclusive: `data_source_gcp_resource`, `data_source_backup_appliance_application`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #data_source_gcp_resource=
    
    
    def data_source_gcp_resource=(value) -> ::Google::Cloud::BackupDR::V1::DataSourceGcpResource

**Parameter**

  * **value** ([::Google::Cloud::BackupDR::V1::DataSourceGcpResource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DataSourceGcpResource)) — The backed up resource is a Google Cloud resource. The word 'DataSource' was included in the names to indicate that this is the representation of the Google Cloud resource used within the DataSource object.

Note: The following fields are mutually exclusive: `data_source_gcp_resource`, `data_source_backup_appliance_application`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::BackupDR::V1::DataSourceGcpResource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DataSourceGcpResource)) — The backed up resource is a Google Cloud resource. The word 'DataSource' was included in the names to indicate that this is the representation of the Google Cloud resource used within the DataSource object.

Note: The following fields are mutually exclusive: `data_source_gcp_resource`, `data_source_backup_appliance_application`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #etag
    
    
    def etag() -> ::String

**Returns**

  * (::String) — Server specified ETag for the ManagementServer resource to prevent simultaneous updates from overwiting each other. 



### #etag=
    
    
    def etag=(value) -> ::String

**Parameter**

  * **value** (::String) — Server specified ETag for the ManagementServer resource to prevent simultaneous updates from overwiting each other. 



**Returns**

  * (::String) — Server specified ETag for the ManagementServer resource to prevent simultaneous updates from overwiting each other. 



### #labels
    
    
    def labels() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. Resource labels to represent user provided metadata. No labels currently defined: 



### #labels=
    
    
    def labels=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Optional. Resource labels to represent user provided metadata. No labels currently defined: 



**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. Resource labels to represent user provided metadata. No labels currently defined: 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Output only. Identifier. Name of the datasource to create. It must have the format`"projects/{project}/locations/{location}/backupVaults/{backupvault}/dataSources/{datasource}"`. `{datasource}` cannot be changed after creation. It must be between 3-63 characters long and must be unique within the backup vault. 



### #state
    
    
    def state() -> ::Google::Cloud::BackupDR::V1::DataSource::State

**Returns**

  * ([::Google::Cloud::BackupDR::V1::DataSource::State](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DataSource-State)) — Output only. The DataSource resource instance state. 



### #total_stored_bytes
    
    
    def total_stored_bytes() -> ::Integer

**Returns**

  * (::Integer) — The number of bytes (metadata and data) stored in this datasource. 



### #total_stored_bytes=
    
    
    def total_stored_bytes=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The number of bytes (metadata and data) stored in this datasource. 



**Returns**

  * (::Integer) — The number of bytes (metadata and data) stored in this datasource. 



### #update_time
    
    
    def update_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Protobuf-Timestamp)) — Output only. The time when the instance was updated. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
