---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-oracle_database-v1/latest/Google-Cloud-OracleDatabase-V1-ExadbVmClusterProperties/
title: Oracle Database@Google Cloud V1 API - Class Google::Cloud::OracleDatabase::V1::ExadbVmClusterProperties (v1.1.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:02:26.987875+00:00
---

# Oracle Database@Google Cloud V1 API - Class Google::Cloud::OracleDatabase::V1::ExadbVmClusterProperties (v1.1.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-oracle_database-v1/latest/Google-Cloud-OracleDatabase-V1-ExadbVmClusterProperties/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Oracle Database@Google Cloud V1 API - Class Google::Cloud::OracleDatabase::V1::ExadbVmClusterProperties (v1.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.1 (latest)  1.1.0  1.0.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.1  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.1  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Oracle Database@Google Cloud V1 API class Google::Cloud::OracleDatabase::V1::ExadbVmClusterProperties.

The properties of an ExadbVmCluster.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #additional_ecpu_count_per_node
    
    
    def additional_ecpu_count_per_node() -> ::Integer

**Returns**

  * (::Integer) — Optional. Immutable. The number of additional ECPUs per node for an Exadata VM cluster on exascale infrastructure. 



### #additional_ecpu_count_per_node=
    
    
    def additional_ecpu_count_per_node=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. Immutable. The number of additional ECPUs per node for an Exadata VM cluster on exascale infrastructure. 



**Returns**

  * (::Integer) — Optional. Immutable. The number of additional ECPUs per node for an Exadata VM cluster on exascale infrastructure. 



### #cluster_name
    
    
    def cluster_name() -> ::String

**Returns**

  * (::String) — Optional. Immutable. The cluster name for Exascale vm cluster. The cluster name must begin with an alphabetic character and may contain hyphens(-) but can not contain underscores(_). It should be not more than 11 characters and is not case sensitive. OCI Cluster name. 



### #cluster_name=
    
    
    def cluster_name=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Immutable. The cluster name for Exascale vm cluster. The cluster name must begin with an alphabetic character and may contain hyphens(-) but can not contain underscores(_). It should be not more than 11 characters and is not case sensitive. OCI Cluster name. 



**Returns**

  * (::String) — Optional. Immutable. The cluster name for Exascale vm cluster. The cluster name must begin with an alphabetic character and may contain hyphens(-) but can not contain underscores(_). It should be not more than 11 characters and is not case sensitive. OCI Cluster name. 



### #data_collection_options
    
    
    def data_collection_options() -> ::Google::Cloud::OracleDatabase::V1::DataCollectionOptionsCommon

**Returns**

  * ([::Google::Cloud::OracleDatabase::V1::DataCollectionOptionsCommon](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-oracle_database-v1/latest/Google-Cloud-OracleDatabase-V1-DataCollectionOptionsCommon)) — Optional. Immutable. Indicates user preference for data collection options. 



### #data_collection_options=
    
    
    def data_collection_options=(value) -> ::Google::Cloud::OracleDatabase::V1::DataCollectionOptionsCommon

**Parameter**

  * **value** ([::Google::Cloud::OracleDatabase::V1::DataCollectionOptionsCommon](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-oracle_database-v1/latest/Google-Cloud-OracleDatabase-V1-DataCollectionOptionsCommon)) — Optional. Immutable. Indicates user preference for data collection options. 



**Returns**

  * ([::Google::Cloud::OracleDatabase::V1::DataCollectionOptionsCommon](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-oracle_database-v1/latest/Google-Cloud-OracleDatabase-V1-DataCollectionOptionsCommon)) — Optional. Immutable. Indicates user preference for data collection options. 



### #enabled_ecpu_count_per_node
    
    
    def enabled_ecpu_count_per_node() -> ::Integer

**Returns**

  * (::Integer) — Required. Immutable. The number of ECPUs enabled per node for an exadata vm cluster on exascale infrastructure. 



### #enabled_ecpu_count_per_node=
    
    
    def enabled_ecpu_count_per_node=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Required. Immutable. The number of ECPUs enabled per node for an exadata vm cluster on exascale infrastructure. 



**Returns**

  * (::Integer) — Required. Immutable. The number of ECPUs enabled per node for an exadata vm cluster on exascale infrastructure. 



### #exascale_db_storage_vault
    
    
    def exascale_db_storage_vault() -> ::String

**Returns**

  * (::String) — Required. Immutable. The name of ExascaleDbStorageVault associated with the ExadbVmCluster. It can refer to an existing ExascaleDbStorageVault. Or a new one can be created during the ExadbVmCluster creation (requires storage_vault_properties to be set). Format: projects/{project}/locations/{location}/exascaleDbStorageVaults/{exascale_db_storage_vault} 



### #exascale_db_storage_vault=
    
    
    def exascale_db_storage_vault=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Immutable. The name of ExascaleDbStorageVault associated with the ExadbVmCluster. It can refer to an existing ExascaleDbStorageVault. Or a new one can be created during the ExadbVmCluster creation (requires storage_vault_properties to be set). Format: projects/{project}/locations/{location}/exascaleDbStorageVaults/{exascale_db_storage_vault} 



**Returns**

  * (::String) — Required. Immutable. The name of ExascaleDbStorageVault associated with the ExadbVmCluster. It can refer to an existing ExascaleDbStorageVault. Or a new one can be created during the ExadbVmCluster creation (requires storage_vault_properties to be set). Format: projects/{project}/locations/{location}/exascaleDbStorageVaults/{exascale_db_storage_vault} 



### #gi_version
    
    
    def gi_version() -> ::String

**Returns**

  * (::String) — Output only. The Oracle Grid Infrastructure (GI) software version. 



### #grid_image_id
    
    
    def grid_image_id() -> ::String

**Returns**

  * (::String) — Required. Immutable. Grid Infrastructure Version. 



### #grid_image_id=
    
    
    def grid_image_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Immutable. Grid Infrastructure Version. 



**Returns**

  * (::String) — Required. Immutable. Grid Infrastructure Version. 



### #hostname
    
    
    def hostname() -> ::String

**Returns**

  * (::String) — Output only. The hostname of the ExadbVmCluster. 



### #hostname_prefix
    
    
    def hostname_prefix() -> ::String

**Returns**

  * (::String) — Required. Immutable. Prefix for VM cluster host names. 



### #hostname_prefix=
    
    
    def hostname_prefix=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Immutable. Prefix for VM cluster host names. 



**Returns**

  * (::String) — Required. Immutable. Prefix for VM cluster host names. 



### #license_model
    
    
    def license_model() -> ::Google::Cloud::OracleDatabase::V1::ExadbVmClusterProperties::LicenseModel

**Returns**

  * ([::Google::Cloud::OracleDatabase::V1::ExadbVmClusterProperties::LicenseModel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-oracle_database-v1/latest/Google-Cloud-OracleDatabase-V1-ExadbVmClusterProperties-LicenseModel)) — Optional. Immutable. The license type of the ExadbVmCluster. 



### #license_model=
    
    
    def license_model=(value) -> ::Google::Cloud::OracleDatabase::V1::ExadbVmClusterProperties::LicenseModel

**Parameter**

  * **value** ([::Google::Cloud::OracleDatabase::V1::ExadbVmClusterProperties::LicenseModel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-oracle_database-v1/latest/Google-Cloud-OracleDatabase-V1-ExadbVmClusterProperties-LicenseModel)) — Optional. Immutable. The license type of the ExadbVmCluster. 



**Returns**

  * ([::Google::Cloud::OracleDatabase::V1::ExadbVmClusterProperties::LicenseModel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-oracle_database-v1/latest/Google-Cloud-OracleDatabase-V1-ExadbVmClusterProperties-LicenseModel)) — Optional. Immutable. The license type of the ExadbVmCluster. 



### #lifecycle_state
    
    
    def lifecycle_state() -> ::Google::Cloud::OracleDatabase::V1::ExadbVmClusterProperties::ExadbVmClusterLifecycleState

**Returns**

  * ([::Google::Cloud::OracleDatabase::V1::ExadbVmClusterProperties::ExadbVmClusterLifecycleState](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-oracle_database-v1/latest/Google-Cloud-OracleDatabase-V1-ExadbVmClusterProperties-ExadbVmClusterLifecycleState)) — Output only. State of the cluster. 



### #memory_size_gb
    
    
    def memory_size_gb() -> ::Integer

**Returns**

  * (::Integer) — Output only. Memory per VM (GB) (Read-only): Shows the amount of memory allocated to each VM. Memory is calculated based on 2.75 GB per Total ECPUs. 



### #node_count
    
    
    def node_count() -> ::Integer

**Returns**

  * (::Integer) — Required. The number of nodes/VMs in the ExadbVmCluster. 



### #node_count=
    
    
    def node_count=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Required. The number of nodes/VMs in the ExadbVmCluster. 



**Returns**

  * (::Integer) — Required. The number of nodes/VMs in the ExadbVmCluster. 



### #oci_uri
    
    
    def oci_uri() -> ::String

**Returns**

  * (::String) — Output only. Deep link to the OCI console to view this resource. 



### #scan_listener_port_tcp
    
    
    def scan_listener_port_tcp() -> ::Integer

**Returns**

  * (::Integer) — Optional. Immutable. SCAN listener port - TCP 



### #scan_listener_port_tcp=
    
    
    def scan_listener_port_tcp=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. Immutable. SCAN listener port - TCP 



**Returns**

  * (::Integer) — Optional. Immutable. SCAN listener port - TCP 



### #shape_attribute
    
    
    def shape_attribute() -> ::Google::Cloud::OracleDatabase::V1::ExadbVmClusterProperties::ShapeAttribute

**Returns**

  * ([::Google::Cloud::OracleDatabase::V1::ExadbVmClusterProperties::ShapeAttribute](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-oracle_database-v1/latest/Google-Cloud-OracleDatabase-V1-ExadbVmClusterProperties-ShapeAttribute)) — Required. Immutable. The shape attribute of the VM cluster. The type of Exascale storage used for Exadata VM cluster. The default is SMART_STORAGE which supports Oracle Database 23ai and later 



### #shape_attribute=
    
    
    def shape_attribute=(value) -> ::Google::Cloud::OracleDatabase::V1::ExadbVmClusterProperties::ShapeAttribute

**Parameter**

  * **value** ([::Google::Cloud::OracleDatabase::V1::ExadbVmClusterProperties::ShapeAttribute](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-oracle_database-v1/latest/Google-Cloud-OracleDatabase-V1-ExadbVmClusterProperties-ShapeAttribute)) — Required. Immutable. The shape attribute of the VM cluster. The type of Exascale storage used for Exadata VM cluster. The default is SMART_STORAGE which supports Oracle Database 23ai and later 



**Returns**

  * ([::Google::Cloud::OracleDatabase::V1::ExadbVmClusterProperties::ShapeAttribute](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-oracle_database-v1/latest/Google-Cloud-OracleDatabase-V1-ExadbVmClusterProperties-ShapeAttribute)) — Required. Immutable. The shape attribute of the VM cluster. The type of Exascale storage used for Exadata VM cluster. The default is SMART_STORAGE which supports Oracle Database 23ai and later 



### #ssh_public_keys
    
    
    def ssh_public_keys() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Required. Immutable. The SSH public keys for the ExadbVmCluster. 



### #ssh_public_keys=
    
    
    def ssh_public_keys=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Required. Immutable. The SSH public keys for the ExadbVmCluster. 



**Returns**

  * (::Array<::String>) — Required. Immutable. The SSH public keys for the ExadbVmCluster. 



### #time_zone
    
    
    def time_zone() -> ::Google::Type::TimeZone

**Returns**

  * ([::Google::Type::TimeZone](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-oracle_database-v1/latest/Google-Type-TimeZone)) — Optional. Immutable. The time zone of the ExadbVmCluster. 



### #time_zone=
    
    
    def time_zone=(value) -> ::Google::Type::TimeZone

**Parameter**

  * **value** ([::Google::Type::TimeZone](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-oracle_database-v1/latest/Google-Type-TimeZone)) — Optional. Immutable. The time zone of the ExadbVmCluster. 



**Returns**

  * ([::Google::Type::TimeZone](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-oracle_database-v1/latest/Google-Type-TimeZone)) — Optional. Immutable. The time zone of the ExadbVmCluster. 



### #vm_file_system_storage
    
    
    def vm_file_system_storage() -> ::Google::Cloud::OracleDatabase::V1::ExadbVmClusterStorageDetails

**Returns**

  * ([::Google::Cloud::OracleDatabase::V1::ExadbVmClusterStorageDetails](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-oracle_database-v1/latest/Google-Cloud-OracleDatabase-V1-ExadbVmClusterStorageDetails)) — Required. Immutable. Total storage details for the ExadbVmCluster. 



### #vm_file_system_storage=
    
    
    def vm_file_system_storage=(value) -> ::Google::Cloud::OracleDatabase::V1::ExadbVmClusterStorageDetails

**Parameter**

  * **value** ([::Google::Cloud::OracleDatabase::V1::ExadbVmClusterStorageDetails](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-oracle_database-v1/latest/Google-Cloud-OracleDatabase-V1-ExadbVmClusterStorageDetails)) — Required. Immutable. Total storage details for the ExadbVmCluster. 



**Returns**

  * ([::Google::Cloud::OracleDatabase::V1::ExadbVmClusterStorageDetails](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-oracle_database-v1/latest/Google-Cloud-OracleDatabase-V1-ExadbVmClusterStorageDetails)) — Required. Immutable. Total storage details for the ExadbVmCluster. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
