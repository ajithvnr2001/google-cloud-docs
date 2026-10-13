---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-CloudSqlSettings/
title: Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::CloudSqlSettings (v1.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:35:20.328676+00:00
---

# Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::CloudSqlSettings (v1.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-CloudSqlSettings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::CloudSqlSettings (v1.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.1 (latest)  1.8.0  1.7.0  1.6.0  1.5.1  1.4.0  1.3.1  1.2.2  1.1.0  1.0.1  0.8.0  0.7.2  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.5 

Reference documentation and code samples for the Cloud Database Migration Service V1 API class Google::Cloud::CloudDMS::V1::CloudSqlSettings.

Settings for creating a Cloud SQL database instance.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #activation_policy
    
    
    def activation_policy() -> ::Google::Cloud::CloudDMS::V1::CloudSqlSettings::SqlActivationPolicy

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::CloudSqlSettings::SqlActivationPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-CloudSqlSettings-SqlActivationPolicy)) — The activation policy specifies when the instance is activated; it is applicable only when the instance state is 'RUNNABLE'. Valid values:

'ALWAYS': The instance is on, and remains so even in the absence of connection requests.

`NEVER`: The instance is off; it is not activated, even if a connection request arrives. 




### #activation_policy=
    
    
    def activation_policy=(value) -> ::Google::Cloud::CloudDMS::V1::CloudSqlSettings::SqlActivationPolicy

**Parameter**

  * **value** ([::Google::Cloud::CloudDMS::V1::CloudSqlSettings::SqlActivationPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-CloudSqlSettings-SqlActivationPolicy)) — The activation policy specifies when the instance is activated; it is applicable only when the instance state is 'RUNNABLE'. Valid values:

'ALWAYS': The instance is on, and remains so even in the absence of connection requests.

`NEVER`: The instance is off; it is not activated, even if a connection request arrives. 




**Returns**

  * ([::Google::Cloud::CloudDMS::V1::CloudSqlSettings::SqlActivationPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-CloudSqlSettings-SqlActivationPolicy)) — The activation policy specifies when the instance is activated; it is applicable only when the instance state is 'RUNNABLE'. Valid values:

'ALWAYS': The instance is on, and remains so even in the absence of connection requests.

`NEVER`: The instance is off; it is not activated, even if a connection request arrives. 




### #auto_storage_increase
    
    
    def auto_storage_increase() -> ::Google::Protobuf::BoolValue

**Returns**

  * ([::Google::Protobuf::BoolValue](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Protobuf-BoolValue)) — [default: ON] If you enable this setting, Cloud SQL checks your available storage every 30 seconds. If the available storage falls below a threshold size, Cloud SQL automatically adds additional storage capacity. If the available storage repeatedly falls below the threshold size, Cloud SQL continues to add storage until it reaches the maximum of 30 TB. 



### #auto_storage_increase=
    
    
    def auto_storage_increase=(value) -> ::Google::Protobuf::BoolValue

**Parameter**

  * **value** ([::Google::Protobuf::BoolValue](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Protobuf-BoolValue)) — [default: ON] If you enable this setting, Cloud SQL checks your available storage every 30 seconds. If the available storage falls below a threshold size, Cloud SQL automatically adds additional storage capacity. If the available storage repeatedly falls below the threshold size, Cloud SQL continues to add storage until it reaches the maximum of 30 TB. 



**Returns**

  * ([::Google::Protobuf::BoolValue](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Protobuf-BoolValue)) — [default: ON] If you enable this setting, Cloud SQL checks your available storage every 30 seconds. If the available storage falls below a threshold size, Cloud SQL automatically adds additional storage capacity. If the available storage repeatedly falls below the threshold size, Cloud SQL continues to add storage until it reaches the maximum of 30 TB. 



### #availability_type
    
    
    def availability_type() -> ::Google::Cloud::CloudDMS::V1::CloudSqlSettings::SqlAvailabilityType

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::CloudSqlSettings::SqlAvailabilityType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-CloudSqlSettings-SqlAvailabilityType)) — 

Optional. Availability type. Potential values:

    * `ZONAL`: The instance serves data from only one zone. Outages in that zone affect data availability.
    * `REGIONAL`: The instance can serve data from more than one zone in a region (it is highly available).



### #availability_type=
    
    
    def availability_type=(value) -> ::Google::Cloud::CloudDMS::V1::CloudSqlSettings::SqlAvailabilityType

**Parameter**

  * **value** ([::Google::Cloud::CloudDMS::V1::CloudSqlSettings::SqlAvailabilityType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-CloudSqlSettings-SqlAvailabilityType)) — 

Optional. Availability type. Potential values:

    * `ZONAL`: The instance serves data from only one zone. Outages in that zone affect data availability.
    * `REGIONAL`: The instance can serve data from more than one zone in a region (it is highly available).



**Returns**

  * ([::Google::Cloud::CloudDMS::V1::CloudSqlSettings::SqlAvailabilityType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-CloudSqlSettings-SqlAvailabilityType)) — 

Optional. Availability type. Potential values:

    * `ZONAL`: The instance serves data from only one zone. Outages in that zone affect data availability.
    * `REGIONAL`: The instance can serve data from more than one zone in a region (it is highly available).



### #cmek_key_name
    
    
    def cmek_key_name() -> ::String

**Returns**

  * (::String) — The KMS key name used for the csql instance. 



### #cmek_key_name=
    
    
    def cmek_key_name=(value) -> ::String

**Parameter**

  * **value** (::String) — The KMS key name used for the csql instance. 



**Returns**

  * (::String) — The KMS key name used for the csql instance. 



### #collation
    
    
    def collation() -> ::String

**Returns**

  * (::String) — The Cloud SQL default instance level collation. 



### #collation=
    
    
    def collation=(value) -> ::String

**Parameter**

  * **value** (::String) — The Cloud SQL default instance level collation. 



**Returns**

  * (::String) — The Cloud SQL default instance level collation. 



### #data_disk_size_gb
    
    
    def data_disk_size_gb() -> ::Google::Protobuf::Int64Value

**Returns**

  * ([::Google::Protobuf::Int64Value](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Protobuf-Int64Value)) — The storage capacity available to the database, in GB. The minimum (and default) size is 10GB. 



### #data_disk_size_gb=
    
    
    def data_disk_size_gb=(value) -> ::Google::Protobuf::Int64Value

**Parameter**

  * **value** ([::Google::Protobuf::Int64Value](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Protobuf-Int64Value)) — The storage capacity available to the database, in GB. The minimum (and default) size is 10GB. 



**Returns**

  * ([::Google::Protobuf::Int64Value](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Protobuf-Int64Value)) — The storage capacity available to the database, in GB. The minimum (and default) size is 10GB. 



### #data_disk_type
    
    
    def data_disk_type() -> ::Google::Cloud::CloudDMS::V1::CloudSqlSettings::SqlDataDiskType

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::CloudSqlSettings::SqlDataDiskType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-CloudSqlSettings-SqlDataDiskType)) — The type of storage: `PD_SSD` (default) or `PD_HDD`. 



### #data_disk_type=
    
    
    def data_disk_type=(value) -> ::Google::Cloud::CloudDMS::V1::CloudSqlSettings::SqlDataDiskType

**Parameter**

  * **value** ([::Google::Cloud::CloudDMS::V1::CloudSqlSettings::SqlDataDiskType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-CloudSqlSettings-SqlDataDiskType)) — The type of storage: `PD_SSD` (default) or `PD_HDD`. 



**Returns**

  * ([::Google::Cloud::CloudDMS::V1::CloudSqlSettings::SqlDataDiskType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-CloudSqlSettings-SqlDataDiskType)) — The type of storage: `PD_SSD` (default) or `PD_HDD`. 



### #database_flags
    
    
    def database_flags() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — The database flags passed to the Cloud SQL instance at startup. An object containing a list of "key": value pairs. Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }. 



### #database_flags=
    
    
    def database_flags=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — The database flags passed to the Cloud SQL instance at startup. An object containing a list of "key": value pairs. Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }. 



**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — The database flags passed to the Cloud SQL instance at startup. An object containing a list of "key": value pairs. Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }. 



### #database_version
    
    
    def database_version() -> ::Google::Cloud::CloudDMS::V1::CloudSqlSettings::SqlDatabaseVersion

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::CloudSqlSettings::SqlDatabaseVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-CloudSqlSettings-SqlDatabaseVersion)) — The database engine type and version. 



### #database_version=
    
    
    def database_version=(value) -> ::Google::Cloud::CloudDMS::V1::CloudSqlSettings::SqlDatabaseVersion

**Parameter**

  * **value** ([::Google::Cloud::CloudDMS::V1::CloudSqlSettings::SqlDatabaseVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-CloudSqlSettings-SqlDatabaseVersion)) — The database engine type and version. 



**Returns**

  * ([::Google::Cloud::CloudDMS::V1::CloudSqlSettings::SqlDatabaseVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-CloudSqlSettings-SqlDatabaseVersion)) — The database engine type and version. 



### #edition
    
    
    def edition() -> ::Google::Cloud::CloudDMS::V1::CloudSqlSettings::Edition

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::CloudSqlSettings::Edition](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-CloudSqlSettings-Edition)) — Optional. The edition of the given Cloud SQL instance. 



### #edition=
    
    
    def edition=(value) -> ::Google::Cloud::CloudDMS::V1::CloudSqlSettings::Edition

**Parameter**

  * **value** ([::Google::Cloud::CloudDMS::V1::CloudSqlSettings::Edition](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-CloudSqlSettings-Edition)) — Optional. The edition of the given Cloud SQL instance. 



**Returns**

  * ([::Google::Cloud::CloudDMS::V1::CloudSqlSettings::Edition](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-CloudSqlSettings-Edition)) — Optional. The edition of the given Cloud SQL instance. 



### #ip_config
    
    
    def ip_config() -> ::Google::Cloud::CloudDMS::V1::SqlIpConfig

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::SqlIpConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-SqlIpConfig)) — The settings for IP Management. This allows to enable or disable the instance IP and manage which external networks can connect to the instance. The IPv4 address cannot be disabled. 



### #ip_config=
    
    
    def ip_config=(value) -> ::Google::Cloud::CloudDMS::V1::SqlIpConfig

**Parameter**

  * **value** ([::Google::Cloud::CloudDMS::V1::SqlIpConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-SqlIpConfig)) — The settings for IP Management. This allows to enable or disable the instance IP and manage which external networks can connect to the instance. The IPv4 address cannot be disabled. 



**Returns**

  * ([::Google::Cloud::CloudDMS::V1::SqlIpConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-SqlIpConfig)) — The settings for IP Management. This allows to enable or disable the instance IP and manage which external networks can connect to the instance. The IPv4 address cannot be disabled. 



### #root_password
    
    
    def root_password() -> ::String

**Returns**

  * (::String) — Input only. Initial root password. 



### #root_password=
    
    
    def root_password=(value) -> ::String

**Parameter**

  * **value** (::String) — Input only. Initial root password. 



**Returns**

  * (::String) — Input only. Initial root password. 



### #root_password_set
    
    
    def root_password_set() -> ::Boolean

**Returns**

  * (::Boolean) — Output only. Indicates If this connection profile root password is stored. 



### #secondary_zone
    
    
    def secondary_zone() -> ::String

**Returns**

  * (::String) — Optional. The Google Cloud Platform zone where the failover Cloud SQL database instance is located. Used when the Cloud SQL database availability type is REGIONAL (i.e. multiple zones / highly available). 



### #secondary_zone=
    
    
    def secondary_zone=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The Google Cloud Platform zone where the failover Cloud SQL database instance is located. Used when the Cloud SQL database availability type is REGIONAL (i.e. multiple zones / highly available). 



**Returns**

  * (::String) — Optional. The Google Cloud Platform zone where the failover Cloud SQL database instance is located. Used when the Cloud SQL database availability type is REGIONAL (i.e. multiple zones / highly available). 



### #source_id
    
    
    def source_id() -> ::String

**Returns**

  * (::String) — The Database Migration Service source connection profile ID, in the format: `projects/my_project_name/locations/us-central1/connectionProfiles/connection_profile_ID`



### #source_id=
    
    
    def source_id=(value) -> ::String

**Parameter**

  * **value** (::String) — The Database Migration Service source connection profile ID, in the format: `projects/my_project_name/locations/us-central1/connectionProfiles/connection_profile_ID`



**Returns**

  * (::String) — The Database Migration Service source connection profile ID, in the format: `projects/my_project_name/locations/us-central1/connectionProfiles/connection_profile_ID`



### #storage_auto_resize_limit
    
    
    def storage_auto_resize_limit() -> ::Google::Protobuf::Int64Value

**Returns**

  * ([::Google::Protobuf::Int64Value](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Protobuf-Int64Value)) — The maximum size to which storage capacity can be automatically increased. The default value is 0, which specifies that there is no limit. 



### #storage_auto_resize_limit=
    
    
    def storage_auto_resize_limit=(value) -> ::Google::Protobuf::Int64Value

**Parameter**

  * **value** ([::Google::Protobuf::Int64Value](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Protobuf-Int64Value)) — The maximum size to which storage capacity can be automatically increased. The default value is 0, which specifies that there is no limit. 



**Returns**

  * ([::Google::Protobuf::Int64Value](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Protobuf-Int64Value)) — The maximum size to which storage capacity can be automatically increased. The default value is 0, which specifies that there is no limit. 



### #tier
    
    
    def tier() -> ::String

**Returns**

  * (::String) — The tier (or machine type) for this instance, for example: `db-n1-standard-1` (MySQL instances) or `db-custom-1-3840` (PostgreSQL instances). For more information, see [Cloud SQL Instance Settings](https://cloud.google.com/sql/docs/mysql/instance-settings). 



### #tier=
    
    
    def tier=(value) -> ::String

**Parameter**

  * **value** (::String) — The tier (or machine type) for this instance, for example: `db-n1-standard-1` (MySQL instances) or `db-custom-1-3840` (PostgreSQL instances). For more information, see [Cloud SQL Instance Settings](https://cloud.google.com/sql/docs/mysql/instance-settings). 



**Returns**

  * (::String) — The tier (or machine type) for this instance, for example: `db-n1-standard-1` (MySQL instances) or `db-custom-1-3840` (PostgreSQL instances). For more information, see [Cloud SQL Instance Settings](https://cloud.google.com/sql/docs/mysql/instance-settings). 



### #user_labels
    
    
    def user_labels() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — The resource labels for a Cloud SQL instance to use to annotate any related underlying resources such as Compute Engine VMs. An object containing a list of "key": "value" pairs.

Example: `{ "name": "wrench", "mass": "18kg", "count": "3" }`. 




### #user_labels=
    
    
    def user_labels=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — The resource labels for a Cloud SQL instance to use to annotate any related underlying resources such as Compute Engine VMs. An object containing a list of "key": "value" pairs.

Example: `{ "name": "wrench", "mass": "18kg", "count": "3" }`. 




**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — The resource labels for a Cloud SQL instance to use to annotate any related underlying resources such as Compute Engine VMs. An object containing a list of "key": "value" pairs.

Example: `{ "name": "wrench", "mass": "18kg", "count": "3" }`. 




### #zone
    
    
    def zone() -> ::String

**Returns**

  * (::String) — The Google Cloud Platform zone where your Cloud SQL database instance is located. 



### #zone=
    
    
    def zone=(value) -> ::String

**Parameter**

  * **value** (::String) — The Google Cloud Platform zone where your Cloud SQL database instance is located. 



**Returns**

  * (::String) — The Google Cloud Platform zone where your Cloud SQL database instance is located. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
