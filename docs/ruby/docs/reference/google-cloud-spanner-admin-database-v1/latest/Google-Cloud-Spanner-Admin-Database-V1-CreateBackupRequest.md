---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-CreateBackupRequest/
title: Cloud Spanner Database Admin V1 API - Class Google::Cloud::Spanner::Admin::Database::V1::CreateBackupRequest (v1.14.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:14:47.846898+00:00
---

# Cloud Spanner Database Admin V1 API - Class Google::Cloud::Spanner::Admin::Database::V1::CreateBackupRequest (v1.14.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-CreateBackupRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Spanner Database Admin V1 API - Class Google::Cloud::Spanner::Admin::Database::V1::CreateBackupRequest (v1.14.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.14.1 (latest)  1.14.0  1.13.1  1.12.0  1.11.1  1.10.0  1.9.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.0  1.3.0  1.2.1  1.1.1  1.0.0  0.20.0  0.19.0  0.18.0  0.17.1  0.16.1  0.15.0  0.14.2  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.6 

Reference documentation and code samples for the Cloud Spanner Database Admin V1 API class Google::Cloud::Spanner::Admin::Database::V1::CreateBackupRequest.

The request for [CreateBackup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-DatabaseAdmin-Client#Google__Cloud__Spanner__Admin__Database__V1__DatabaseAdmin__Client_create_backup_instance_ "Google::Cloud::Spanner::Admin::Database::V1::DatabaseAdmin::Client#create_backup \(method\)").

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #backup
    
    
    def backup() -> ::Google::Cloud::Spanner::Admin::Database::V1::Backup

**Returns**

  * ([::Google::Cloud::Spanner::Admin::Database::V1::Backup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-Backup)) — Required. The backup to create. 



### #backup=
    
    
    def backup=(value) -> ::Google::Cloud::Spanner::Admin::Database::V1::Backup

**Parameter**

  * **value** ([::Google::Cloud::Spanner::Admin::Database::V1::Backup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-Backup)) — Required. The backup to create. 



**Returns**

  * ([::Google::Cloud::Spanner::Admin::Database::V1::Backup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-Backup)) — Required. The backup to create. 



### #backup_id
    
    
    def backup_id() -> ::String

**Returns**

  * (::String) — Required. The id of the backup to be created. The `backup_id` appended to `parent` forms the full backup name of the form `projects/<project>/instances/<instance>/backups/<backup_id>`. 



### #backup_id=
    
    
    def backup_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The id of the backup to be created. The `backup_id` appended to `parent` forms the full backup name of the form `projects/<project>/instances/<instance>/backups/<backup_id>`. 



**Returns**

  * (::String) — Required. The id of the backup to be created. The `backup_id` appended to `parent` forms the full backup name of the form `projects/<project>/instances/<instance>/backups/<backup_id>`. 



### #encryption_config
    
    
    def encryption_config() -> ::Google::Cloud::Spanner::Admin::Database::V1::CreateBackupEncryptionConfig

**Returns**

  * ([::Google::Cloud::Spanner::Admin::Database::V1::CreateBackupEncryptionConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-CreateBackupEncryptionConfig)) — Optional. The encryption configuration used to encrypt the backup. If this field is not specified, the backup will use the same encryption configuration as the database by default, namely [encryption_type](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-CreateBackupEncryptionConfig#Google__Cloud__Spanner__Admin__Database__V1__CreateBackupEncryptionConfig_encryption_type_instance_ "Google::Cloud::Spanner::Admin::Database::V1::CreateBackupEncryptionConfig#encryption_type \(method\)") = `USE_DATABASE_ENCRYPTION`. 



### #encryption_config=
    
    
    def encryption_config=(value) -> ::Google::Cloud::Spanner::Admin::Database::V1::CreateBackupEncryptionConfig

**Parameter**

  * **value** ([::Google::Cloud::Spanner::Admin::Database::V1::CreateBackupEncryptionConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-CreateBackupEncryptionConfig)) — Optional. The encryption configuration used to encrypt the backup. If this field is not specified, the backup will use the same encryption configuration as the database by default, namely [encryption_type](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-CreateBackupEncryptionConfig#Google__Cloud__Spanner__Admin__Database__V1__CreateBackupEncryptionConfig_encryption_type_instance_ "Google::Cloud::Spanner::Admin::Database::V1::CreateBackupEncryptionConfig#encryption_type \(method\)") = `USE_DATABASE_ENCRYPTION`. 



**Returns**

  * ([::Google::Cloud::Spanner::Admin::Database::V1::CreateBackupEncryptionConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-CreateBackupEncryptionConfig)) — Optional. The encryption configuration used to encrypt the backup. If this field is not specified, the backup will use the same encryption configuration as the database by default, namely [encryption_type](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-CreateBackupEncryptionConfig#Google__Cloud__Spanner__Admin__Database__V1__CreateBackupEncryptionConfig_encryption_type_instance_ "Google::Cloud::Spanner::Admin::Database::V1::CreateBackupEncryptionConfig#encryption_type \(method\)") = `USE_DATABASE_ENCRYPTION`. 



### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. The name of the instance in which the backup will be created. This must be the same instance that contains the database the backup will be created from. The backup will be stored in the location(s) specified in the instance configuration of this instance. Values are of the form `projects/<project>/instances/<instance>`. 



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The name of the instance in which the backup will be created. This must be the same instance that contains the database the backup will be created from. The backup will be stored in the location(s) specified in the instance configuration of this instance. Values are of the form `projects/<project>/instances/<instance>`. 



**Returns**

  * (::String) — Required. The name of the instance in which the backup will be created. This must be the same instance that contains the database the backup will be created from. The backup will be stored in the location(s) specified in the instance configuration of this instance. Values are of the form `projects/<project>/instances/<instance>`. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
