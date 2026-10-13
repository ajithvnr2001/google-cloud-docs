---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-SqlInstancesStartExternalSyncRequest/
title: Cloud SQL Admin V1 API - Class Google::Cloud::Sql::V1::SqlInstancesStartExternalSyncRequest (v0.4.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:04:26.606891+00:00
---

# Cloud SQL Admin V1 API - Class Google::Cloud::Sql::V1::SqlInstancesStartExternalSyncRequest (v0.4.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-SqlInstancesStartExternalSyncRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud SQL Admin V1 API - Class Google::Cloud::Sql::V1::SqlInstancesStartExternalSyncRequest (v0.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.4.0 (latest)  0.2.0  0.1.0 

Reference documentation and code samples for the Cloud SQL Admin V1 API class Google::Cloud::Sql::V1::SqlInstancesStartExternalSyncRequest.

Instance start external sync request.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #instance
    
    
    def instance() -> ::String

**Returns**

  * (::String) — Cloud SQL instance ID. This does not include the project ID. 



### #instance=
    
    
    def instance=(value) -> ::String

**Parameter**

  * **value** (::String) — Cloud SQL instance ID. This does not include the project ID. 



**Returns**

  * (::String) — Cloud SQL instance ID. This does not include the project ID. 



### #location
    
    
    def location() -> ::String

**Returns**

  * (::String) — Optional. Region of the Cloud SQL instance. 



### #location=
    
    
    def location=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Region of the Cloud SQL instance. 



**Returns**

  * (::String) — Optional. Region of the Cloud SQL instance. 



### #migration_type
    
    
    def migration_type() -> ::Google::Cloud::Sql::V1::SqlInstancesVerifyExternalSyncSettingsRequest::MigrationType

**Returns**

  * ([::Google::Cloud::Sql::V1::SqlInstancesVerifyExternalSyncSettingsRequest::MigrationType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-SqlInstancesVerifyExternalSyncSettingsRequest-MigrationType)) — Optional. MigrationType configures the migration to use physical files or logical dump files. If not set, then the logical dump file configuration is used. Valid values are `LOGICAL` or `PHYSICAL`. Only applicable to MySQL. 



### #migration_type=
    
    
    def migration_type=(value) -> ::Google::Cloud::Sql::V1::SqlInstancesVerifyExternalSyncSettingsRequest::MigrationType

**Parameter**

  * **value** ([::Google::Cloud::Sql::V1::SqlInstancesVerifyExternalSyncSettingsRequest::MigrationType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-SqlInstancesVerifyExternalSyncSettingsRequest-MigrationType)) — Optional. MigrationType configures the migration to use physical files or logical dump files. If not set, then the logical dump file configuration is used. Valid values are `LOGICAL` or `PHYSICAL`. Only applicable to MySQL. 



**Returns**

  * ([::Google::Cloud::Sql::V1::SqlInstancesVerifyExternalSyncSettingsRequest::MigrationType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-SqlInstancesVerifyExternalSyncSettingsRequest-MigrationType)) — Optional. MigrationType configures the migration to use physical files or logical dump files. If not set, then the logical dump file configuration is used. Valid values are `LOGICAL` or `PHYSICAL`. Only applicable to MySQL. 



### #mysql_sync_config
    
    
    def mysql_sync_config() -> ::Google::Cloud::Sql::V1::MySqlSyncConfig

**Returns**

  * ([::Google::Cloud::Sql::V1::MySqlSyncConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-MySqlSyncConfig)) — MySQL-specific settings for start external sync. 



### #mysql_sync_config=
    
    
    def mysql_sync_config=(value) -> ::Google::Cloud::Sql::V1::MySqlSyncConfig

**Parameter**

  * **value** ([::Google::Cloud::Sql::V1::MySqlSyncConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-MySqlSyncConfig)) — MySQL-specific settings for start external sync. 



**Returns**

  * ([::Google::Cloud::Sql::V1::MySqlSyncConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-MySqlSyncConfig)) — MySQL-specific settings for start external sync. 



### #project
    
    
    def project() -> ::String

**Returns**

  * (::String) — ID of the project that contains the instance. 



### #project=
    
    
    def project=(value) -> ::String

**Parameter**

  * **value** (::String) — ID of the project that contains the instance. 



**Returns**

  * (::String) — ID of the project that contains the instance. 



### #replica_overwrite_enabled
    
    
    def replica_overwrite_enabled() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. MySQL only. True if end-user has confirmed that this SES call will wipe replica databases overlapping with the proposed selected_objects. If this field is not set and there are both overlapping and additional databases proposed, an error will be returned. 



### #replica_overwrite_enabled=
    
    
    def replica_overwrite_enabled=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. MySQL only. True if end-user has confirmed that this SES call will wipe replica databases overlapping with the proposed selected_objects. If this field is not set and there are both overlapping and additional databases proposed, an error will be returned. 



**Returns**

  * (::Boolean) — Optional. MySQL only. True if end-user has confirmed that this SES call will wipe replica databases overlapping with the proposed selected_objects. If this field is not set and there are both overlapping and additional databases proposed, an error will be returned. 



### #skip_verification
    
    
    def skip_verification() -> ::Boolean

**Returns**

  * (::Boolean) — Whether to skip the verification step (VESS). 



### #skip_verification=
    
    
    def skip_verification=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Whether to skip the verification step (VESS). 



**Returns**

  * (::Boolean) — Whether to skip the verification step (VESS). 



### #sync_mode
    
    
    def sync_mode() -> ::Google::Cloud::Sql::V1::SqlInstancesVerifyExternalSyncSettingsRequest::ExternalSyncMode

**Returns**

  * ([::Google::Cloud::Sql::V1::SqlInstancesVerifyExternalSyncSettingsRequest::ExternalSyncMode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-SqlInstancesVerifyExternalSyncSettingsRequest-ExternalSyncMode)) — External sync mode. 



### #sync_mode=
    
    
    def sync_mode=(value) -> ::Google::Cloud::Sql::V1::SqlInstancesVerifyExternalSyncSettingsRequest::ExternalSyncMode

**Parameter**

  * **value** ([::Google::Cloud::Sql::V1::SqlInstancesVerifyExternalSyncSettingsRequest::ExternalSyncMode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-SqlInstancesVerifyExternalSyncSettingsRequest-ExternalSyncMode)) — External sync mode. 



**Returns**

  * ([::Google::Cloud::Sql::V1::SqlInstancesVerifyExternalSyncSettingsRequest::ExternalSyncMode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-SqlInstancesVerifyExternalSyncSettingsRequest-ExternalSyncMode)) — External sync mode. 



### #sync_parallel_level
    
    
    def sync_parallel_level() -> ::Google::Cloud::Sql::V1::ExternalSyncParallelLevel

**Returns**

  * ([::Google::Cloud::Sql::V1::ExternalSyncParallelLevel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-ExternalSyncParallelLevel)) — Optional. Parallel level for initial data sync. Currently only applicable for MySQL. 



### #sync_parallel_level=
    
    
    def sync_parallel_level=(value) -> ::Google::Cloud::Sql::V1::ExternalSyncParallelLevel

**Parameter**

  * **value** ([::Google::Cloud::Sql::V1::ExternalSyncParallelLevel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-ExternalSyncParallelLevel)) — Optional. Parallel level for initial data sync. Currently only applicable for MySQL. 



**Returns**

  * ([::Google::Cloud::Sql::V1::ExternalSyncParallelLevel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-ExternalSyncParallelLevel)) — Optional. Parallel level for initial data sync. Currently only applicable for MySQL. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
