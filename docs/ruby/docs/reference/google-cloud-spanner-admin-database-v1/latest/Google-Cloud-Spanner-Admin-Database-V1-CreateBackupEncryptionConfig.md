---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-CreateBackupEncryptionConfig/
title: Cloud Spanner Database Admin V1 API - Class Google::Cloud::Spanner::Admin::Database::V1::CreateBackupEncryptionConfig (v1.14.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:04:57.121210+00:00
---

# Cloud Spanner Database Admin V1 API - Class Google::Cloud::Spanner::Admin::Database::V1::CreateBackupEncryptionConfig (v1.14.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-CreateBackupEncryptionConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Spanner Database Admin V1 API - Class Google::Cloud::Spanner::Admin::Database::V1::CreateBackupEncryptionConfig (v1.14.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.14.1 (latest)  1.14.0  1.13.1  1.12.0  1.11.1  1.10.0  1.9.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.0  1.3.0  1.2.1  1.1.1  1.0.0  0.20.0  0.19.0  0.18.0  0.17.1  0.16.1  0.15.0  0.14.2  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.6 

Reference documentation and code samples for the Cloud Spanner Database Admin V1 API class Google::Cloud::Spanner::Admin::Database::V1::CreateBackupEncryptionConfig.

Encryption configuration for the backup to create.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #encryption_type
    
    
    def encryption_type() -> ::Google::Cloud::Spanner::Admin::Database::V1::CreateBackupEncryptionConfig::EncryptionType

**Returns**

  * ([::Google::Cloud::Spanner::Admin::Database::V1::CreateBackupEncryptionConfig::EncryptionType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-CreateBackupEncryptionConfig-EncryptionType)) — Required. The encryption type of the backup. 



### #encryption_type=
    
    
    def encryption_type=(value) -> ::Google::Cloud::Spanner::Admin::Database::V1::CreateBackupEncryptionConfig::EncryptionType

**Parameter**

  * **value** ([::Google::Cloud::Spanner::Admin::Database::V1::CreateBackupEncryptionConfig::EncryptionType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-CreateBackupEncryptionConfig-EncryptionType)) — Required. The encryption type of the backup. 



**Returns**

  * ([::Google::Cloud::Spanner::Admin::Database::V1::CreateBackupEncryptionConfig::EncryptionType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-CreateBackupEncryptionConfig-EncryptionType)) — Required. The encryption type of the backup. 



### #kms_key_name
    
    
    def kms_key_name() -> ::String

**Returns**

  * (::String) — Optional. The Cloud KMS key that will be used to protect the backup. This field should be set only when [encryption_type](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-CreateBackupEncryptionConfig#Google__Cloud__Spanner__Admin__Database__V1__CreateBackupEncryptionConfig_encryption_type_instance_ "Google::Cloud::Spanner::Admin::Database::V1::CreateBackupEncryptionConfig#encryption_type \(method\)") is `CUSTOMER_MANAGED_ENCRYPTION`. Values are of the form `projects/<project>/locations/<location>/keyRings/<key_ring>/cryptoKeys/<kms_key_name>`. 



### #kms_key_name=
    
    
    def kms_key_name=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The Cloud KMS key that will be used to protect the backup. This field should be set only when [encryption_type](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-CreateBackupEncryptionConfig#Google__Cloud__Spanner__Admin__Database__V1__CreateBackupEncryptionConfig_encryption_type_instance_ "Google::Cloud::Spanner::Admin::Database::V1::CreateBackupEncryptionConfig#encryption_type \(method\)") is `CUSTOMER_MANAGED_ENCRYPTION`. Values are of the form `projects/<project>/locations/<location>/keyRings/<key_ring>/cryptoKeys/<kms_key_name>`. 



**Returns**

  * (::String) — Optional. The Cloud KMS key that will be used to protect the backup. This field should be set only when [encryption_type](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-CreateBackupEncryptionConfig#Google__Cloud__Spanner__Admin__Database__V1__CreateBackupEncryptionConfig_encryption_type_instance_ "Google::Cloud::Spanner::Admin::Database::V1::CreateBackupEncryptionConfig#encryption_type \(method\)") is `CUSTOMER_MANAGED_ENCRYPTION`. Values are of the form `projects/<project>/locations/<location>/keyRings/<key_ring>/cryptoKeys/<kms_key_name>`. 



### #kms_key_names
    
    
    def kms_key_names() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — 

Optional. Specifies the KMS configuration for the one or more keys used to protect the backup. Values are of the form `projects/<project>/locations/<location>/keyRings/<key_ring>/cryptoKeys/<kms_key_name>`.

The keys referenced by kms_key_names must fully cover all regions of the backup's instance configuration. Some examples:

    * For single region instance configs, specify a single regional location KMS key.
    * For multi-regional instance configs of type GOOGLE_MANAGED, either specify a multi-regional location KMS key or multiple regional location KMS keys that cover all regions in the instance config.
    * For an instance config of type USER_MANAGED, please specify only regional location KMS keys to cover each region in the instance config. Multi-regional location KMS keys are not supported for USER_MANAGED instance configs.



### #kms_key_names=
    
    
    def kms_key_names=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — 

Optional. Specifies the KMS configuration for the one or more keys used to protect the backup. Values are of the form `projects/<project>/locations/<location>/keyRings/<key_ring>/cryptoKeys/<kms_key_name>`.

The keys referenced by kms_key_names must fully cover all regions of the backup's instance configuration. Some examples:

    * For single region instance configs, specify a single regional location KMS key.
    * For multi-regional instance configs of type GOOGLE_MANAGED, either specify a multi-regional location KMS key or multiple regional location KMS keys that cover all regions in the instance config.
    * For an instance config of type USER_MANAGED, please specify only regional location KMS keys to cover each region in the instance config. Multi-regional location KMS keys are not supported for USER_MANAGED instance configs.



**Returns**

  * (::Array<::String>) — 

Optional. Specifies the KMS configuration for the one or more keys used to protect the backup. Values are of the form `projects/<project>/locations/<location>/keyRings/<key_ring>/cryptoKeys/<kms_key_name>`.

The keys referenced by kms_key_names must fully cover all regions of the backup's instance configuration. Some examples:

    * For single region instance configs, specify a single regional location KMS key.
    * For multi-regional instance configs of type GOOGLE_MANAGED, either specify a multi-regional location KMS key or multiple regional location KMS keys that cover all regions in the instance config.
    * For an instance config of type USER_MANAGED, please specify only regional location KMS keys to cover each region in the instance config. Multi-regional location KMS keys are not supported for USER_MANAGED instance configs.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
