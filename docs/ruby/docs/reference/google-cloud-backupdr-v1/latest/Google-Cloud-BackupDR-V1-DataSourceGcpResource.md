---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DataSourceGcpResource/
title: Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::DataSourceGcpResource (v1.11.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:47:44.852970+00:00
---

# Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::DataSourceGcpResource (v1.11.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DataSourceGcpResource/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::DataSourceGcpResource (v1.11.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.11.2 (latest)  1.11.1  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.5.0  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Backup and DR Service V1 API class Google::Cloud::BackupDR::V1::DataSourceGcpResource.

DataSourceGcpResource is used for protected resources that are Google Cloud Resources. This name is easeier to understand than GcpResourceDataSource or GcpDataSourceResource

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #alloy_db_cluster_datasource_properties
    
    
    def alloy_db_cluster_datasource_properties() -> ::Google::Cloud::BackupDR::V1::AlloyDBClusterDataSourceProperties

**Returns**

  * ([::Google::Cloud::BackupDR::V1::AlloyDBClusterDataSourceProperties](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-AlloyDBClusterDataSourceProperties)) — Output only. AlloyDBClusterDataSourceProperties has a subset of AlloyDB cluster properties that are useful at the Datasource level.

Note: The following fields are mutually exclusive: `alloy_db_cluster_datasource_properties`, `compute_instance_datasource_properties`, `cloud_sql_instance_datasource_properties`, `disk_datasource_properties`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #cloud_sql_instance_datasource_properties
    
    
    def cloud_sql_instance_datasource_properties() -> ::Google::Cloud::BackupDR::V1::CloudSqlInstanceDataSourceProperties

**Returns**

  * ([::Google::Cloud::BackupDR::V1::CloudSqlInstanceDataSourceProperties](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-CloudSqlInstanceDataSourceProperties)) — Output only. CloudSqlInstanceDataSourceProperties has a subset of Cloud SQL Instance properties that are useful at the Datasource level.

Note: The following fields are mutually exclusive: `cloud_sql_instance_datasource_properties`, `compute_instance_datasource_properties`, `alloy_db_cluster_datasource_properties`, `disk_datasource_properties`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #compute_instance_datasource_properties
    
    
    def compute_instance_datasource_properties() -> ::Google::Cloud::BackupDR::V1::ComputeInstanceDataSourceProperties

**Returns**

  * ([::Google::Cloud::BackupDR::V1::ComputeInstanceDataSourceProperties](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ComputeInstanceDataSourceProperties)) — ComputeInstanceDataSourceProperties has a subset of Compute Instance properties that are useful at the Datasource level.

Note: The following fields are mutually exclusive: `compute_instance_datasource_properties`, `cloud_sql_instance_datasource_properties`, `alloy_db_cluster_datasource_properties`, `disk_datasource_properties`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #compute_instance_datasource_properties=
    
    
    def compute_instance_datasource_properties=(value) -> ::Google::Cloud::BackupDR::V1::ComputeInstanceDataSourceProperties

**Parameter**

  * **value** ([::Google::Cloud::BackupDR::V1::ComputeInstanceDataSourceProperties](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ComputeInstanceDataSourceProperties)) — ComputeInstanceDataSourceProperties has a subset of Compute Instance properties that are useful at the Datasource level.

Note: The following fields are mutually exclusive: `compute_instance_datasource_properties`, `cloud_sql_instance_datasource_properties`, `alloy_db_cluster_datasource_properties`, `disk_datasource_properties`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::BackupDR::V1::ComputeInstanceDataSourceProperties](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ComputeInstanceDataSourceProperties)) — ComputeInstanceDataSourceProperties has a subset of Compute Instance properties that are useful at the Datasource level.

Note: The following fields are mutually exclusive: `compute_instance_datasource_properties`, `cloud_sql_instance_datasource_properties`, `alloy_db_cluster_datasource_properties`, `disk_datasource_properties`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #disk_datasource_properties
    
    
    def disk_datasource_properties() -> ::Google::Cloud::BackupDR::V1::DiskDataSourceProperties

**Returns**

  * ([::Google::Cloud::BackupDR::V1::DiskDataSourceProperties](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DiskDataSourceProperties)) — DiskDataSourceProperties has a subset of Disk properties that are useful at the Datasource level.

Note: The following fields are mutually exclusive: `disk_datasource_properties`, `compute_instance_datasource_properties`, `cloud_sql_instance_datasource_properties`, `alloy_db_cluster_datasource_properties`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #disk_datasource_properties=
    
    
    def disk_datasource_properties=(value) -> ::Google::Cloud::BackupDR::V1::DiskDataSourceProperties

**Parameter**

  * **value** ([::Google::Cloud::BackupDR::V1::DiskDataSourceProperties](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DiskDataSourceProperties)) — DiskDataSourceProperties has a subset of Disk properties that are useful at the Datasource level.

Note: The following fields are mutually exclusive: `disk_datasource_properties`, `compute_instance_datasource_properties`, `cloud_sql_instance_datasource_properties`, `alloy_db_cluster_datasource_properties`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::BackupDR::V1::DiskDataSourceProperties](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DiskDataSourceProperties)) — DiskDataSourceProperties has a subset of Disk properties that are useful at the Datasource level.

Note: The following fields are mutually exclusive: `disk_datasource_properties`, `compute_instance_datasource_properties`, `cloud_sql_instance_datasource_properties`, `alloy_db_cluster_datasource_properties`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #gcp_resourcename
    
    
    def gcp_resourcename() -> ::String

**Returns**

  * (::String) — Output only. Full resource pathname URL of the source Google Cloud resource. 



### #location
    
    
    def location() -> ::String

**Returns**

  * (::String) — Location of the resource: 



### #location=
    
    
    def location=(value) -> ::String

**Parameter**

  * **value** (::String) — Location of the resource: 



**Returns**

  * (::String) — Location of the resource: 



### #type
    
    
    def type() -> ::String

**Returns**

  * (::String) — The type of the Google Cloud resource. Use the Unified Resource Type, eg. compute.googleapis.com/Instance. 



### #type=
    
    
    def type=(value) -> ::String

**Parameter**

  * **value** (::String) — The type of the Google Cloud resource. Use the Unified Resource Type, eg. compute.googleapis.com/Instance. 



**Returns**

  * (::String) — The type of the Google Cloud resource. Use the Unified Resource Type, eg. compute.googleapis.com/Instance. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
