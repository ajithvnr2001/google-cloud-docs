---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DataSourceReference/
title: Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::DataSourceReference (v1.11.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:47:43.936085+00:00
---

# Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::DataSourceReference (v1.11.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DataSourceReference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::DataSourceReference (v1.11.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.11.2 (latest)  1.11.1  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.5.0  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Backup and DR Service V1 API class Google::Cloud::BackupDR::V1::DataSourceReference.

DataSourceReference is a reference to a DataSource resource.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Protobuf-Timestamp)) — Output only. The time when the DataSourceReference was created. 



### #data_source
    
    
    def data_source() -> ::String

**Returns**

  * (::String) — Output only. The resource name of the DataSource. Format: projects/{project}/locations/{location}/backupVaults/{backupVault}/dataSources/{dataSource} 



### #data_source_backup_config_info
    
    
    def data_source_backup_config_info() -> ::Google::Cloud::BackupDR::V1::DataSourceBackupConfigInfo

**Returns**

  * ([::Google::Cloud::BackupDR::V1::DataSourceBackupConfigInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DataSourceBackupConfigInfo)) — Output only. Information of backup configuration on the DataSource. 



### #data_source_backup_config_state
    
    
    def data_source_backup_config_state() -> ::Google::Cloud::BackupDR::V1::BackupConfigState

**Returns**

  * ([::Google::Cloud::BackupDR::V1::BackupConfigState](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupConfigState)) — Output only. The backup configuration state of the DataSource. 



### #data_source_backup_count
    
    
    def data_source_backup_count() -> ::Integer

**Returns**

  * (::Integer) — Output only. Number of backups in the DataSource. 



### #data_source_gcp_resource_info
    
    
    def data_source_gcp_resource_info() -> ::Google::Cloud::BackupDR::V1::DataSourceGcpResourceInfo

**Returns**

  * ([::Google::Cloud::BackupDR::V1::DataSourceGcpResourceInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DataSourceGcpResourceInfo)) — Output only. The GCP resource that the DataSource is associated with. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Identifier. The resource name of the DataSourceReference. Format: projects/{project}/locations/{location}/dataSourceReferences/{data_source_reference} 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Identifier. The resource name of the DataSourceReference. Format: projects/{project}/locations/{location}/dataSourceReferences/{data_source_reference} 



**Returns**

  * (::String) — Identifier. The resource name of the DataSourceReference. Format: projects/{project}/locations/{location}/dataSourceReferences/{data_source_reference} 



### #total_stored_bytes
    
    
    def total_stored_bytes() -> ::Integer

**Returns**

  * (::Integer) — Output only. Total size of the storage used by all backup resources for the referenced datasource. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
