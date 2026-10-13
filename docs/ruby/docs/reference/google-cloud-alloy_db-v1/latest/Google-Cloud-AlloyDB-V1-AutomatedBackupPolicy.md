---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-AutomatedBackupPolicy/
title: AlloyDB V1 API - Class Google::Cloud::AlloyDB::V1::AutomatedBackupPolicy (v1.10.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:48:47.469914+00:00
---

# AlloyDB V1 API - Class Google::Cloud::AlloyDB::V1::AutomatedBackupPolicy (v1.10.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-AutomatedBackupPolicy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  AlloyDB V1 API - Class Google::Cloud::AlloyDB::V1::AutomatedBackupPolicy (v1.10.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.10.2 (latest)  1.10.1  1.9.0  1.7.0  1.6.2  1.5.0  1.4.0  1.3.1  1.2.0  1.1.0  1.0.1  0.12.0  0.11.0  0.10.0  0.9.2  0.8.2  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the AlloyDB V1 API class Google::Cloud::AlloyDB::V1::AutomatedBackupPolicy.

Message describing the user-specified automated backup policy.

All fields in the automated backup policy are optional. Defaults for each field are provided if they are not set.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #backup_window
    
    
    def backup_window() -> ::Google::Protobuf::Duration

**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Protobuf-Duration)) — The length of the time window during which a backup can be taken. If a backup does not succeed within this time window, it will be canceled and considered failed.

The backup window must be at least 5 minutes long. There is no upper bound on the window. If not set, it defaults to 1 hour. 




### #backup_window=
    
    
    def backup_window=(value) -> ::Google::Protobuf::Duration

**Parameter**

  * **value** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Protobuf-Duration)) — The length of the time window during which a backup can be taken. If a backup does not succeed within this time window, it will be canceled and considered failed.

The backup window must be at least 5 minutes long. There is no upper bound on the window. If not set, it defaults to 1 hour. 




**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Protobuf-Duration)) — The length of the time window during which a backup can be taken. If a backup does not succeed within this time window, it will be canceled and considered failed.

The backup window must be at least 5 minutes long. There is no upper bound on the window. If not set, it defaults to 1 hour. 




### #enabled
    
    
    def enabled() -> ::Boolean

**Returns**

  * (::Boolean) — Whether automated automated backups are enabled. If not set, defaults to true. 



### #enabled=
    
    
    def enabled=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Whether automated automated backups are enabled. If not set, defaults to true. 



**Returns**

  * (::Boolean) — Whether automated automated backups are enabled. If not set, defaults to true. 



### #encryption_config
    
    
    def encryption_config() -> ::Google::Cloud::AlloyDB::V1::EncryptionConfig

**Returns**

  * ([::Google::Cloud::AlloyDB::V1::EncryptionConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-EncryptionConfig)) — Optional. The encryption config can be specified to encrypt the backups with a customer-managed encryption key (CMEK). When this field is not specified, the backup will use the cluster's encryption config. 



### #encryption_config=
    
    
    def encryption_config=(value) -> ::Google::Cloud::AlloyDB::V1::EncryptionConfig

**Parameter**

  * **value** ([::Google::Cloud::AlloyDB::V1::EncryptionConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-EncryptionConfig)) — Optional. The encryption config can be specified to encrypt the backups with a customer-managed encryption key (CMEK). When this field is not specified, the backup will use the cluster's encryption config. 



**Returns**

  * ([::Google::Cloud::AlloyDB::V1::EncryptionConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-EncryptionConfig)) — Optional. The encryption config can be specified to encrypt the backups with a customer-managed encryption key (CMEK). When this field is not specified, the backup will use the cluster's encryption config. 



### #labels
    
    
    def labels() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Labels to apply to backups created using this configuration. 



### #labels=
    
    
    def labels=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Labels to apply to backups created using this configuration. 



**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Labels to apply to backups created using this configuration. 



### #location
    
    
    def location() -> ::String

**Returns**

  * (::String) — The location where the backup will be stored. Currently, the only supported option is to store the backup in the same region as the cluster.

If empty, defaults to the region of the cluster. 




### #location=
    
    
    def location=(value) -> ::String

**Parameter**

  * **value** (::String) — The location where the backup will be stored. Currently, the only supported option is to store the backup in the same region as the cluster.

If empty, defaults to the region of the cluster. 




**Returns**

  * (::String) — The location where the backup will be stored. Currently, the only supported option is to store the backup in the same region as the cluster.

If empty, defaults to the region of the cluster. 




### #quantity_based_retention
    
    
    def quantity_based_retention() -> ::Google::Cloud::AlloyDB::V1::AutomatedBackupPolicy::QuantityBasedRetention

**Returns**

  * ([::Google::Cloud::AlloyDB::V1::AutomatedBackupPolicy::QuantityBasedRetention](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-AutomatedBackupPolicy-QuantityBasedRetention)) — Quantity-based Backup retention policy to retain recent backups.

Note: The following fields are mutually exclusive: `quantity_based_retention`, `time_based_retention`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #quantity_based_retention=
    
    
    def quantity_based_retention=(value) -> ::Google::Cloud::AlloyDB::V1::AutomatedBackupPolicy::QuantityBasedRetention

**Parameter**

  * **value** ([::Google::Cloud::AlloyDB::V1::AutomatedBackupPolicy::QuantityBasedRetention](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-AutomatedBackupPolicy-QuantityBasedRetention)) — Quantity-based Backup retention policy to retain recent backups.

Note: The following fields are mutually exclusive: `quantity_based_retention`, `time_based_retention`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::AlloyDB::V1::AutomatedBackupPolicy::QuantityBasedRetention](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-AutomatedBackupPolicy-QuantityBasedRetention)) — Quantity-based Backup retention policy to retain recent backups.

Note: The following fields are mutually exclusive: `quantity_based_retention`, `time_based_retention`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #time_based_retention
    
    
    def time_based_retention() -> ::Google::Cloud::AlloyDB::V1::AutomatedBackupPolicy::TimeBasedRetention

**Returns**

  * ([::Google::Cloud::AlloyDB::V1::AutomatedBackupPolicy::TimeBasedRetention](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-AutomatedBackupPolicy-TimeBasedRetention)) — Time-based Backup retention policy.

Note: The following fields are mutually exclusive: `time_based_retention`, `quantity_based_retention`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #time_based_retention=
    
    
    def time_based_retention=(value) -> ::Google::Cloud::AlloyDB::V1::AutomatedBackupPolicy::TimeBasedRetention

**Parameter**

  * **value** ([::Google::Cloud::AlloyDB::V1::AutomatedBackupPolicy::TimeBasedRetention](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-AutomatedBackupPolicy-TimeBasedRetention)) — Time-based Backup retention policy.

Note: The following fields are mutually exclusive: `time_based_retention`, `quantity_based_retention`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::AlloyDB::V1::AutomatedBackupPolicy::TimeBasedRetention](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-AutomatedBackupPolicy-TimeBasedRetention)) — Time-based Backup retention policy.

Note: The following fields are mutually exclusive: `time_based_retention`, `quantity_based_retention`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #weekly_schedule
    
    
    def weekly_schedule() -> ::Google::Cloud::AlloyDB::V1::AutomatedBackupPolicy::WeeklySchedule

**Returns**

  * ([::Google::Cloud::AlloyDB::V1::AutomatedBackupPolicy::WeeklySchedule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-AutomatedBackupPolicy-WeeklySchedule)) — Weekly schedule for the Backup. 



### #weekly_schedule=
    
    
    def weekly_schedule=(value) -> ::Google::Cloud::AlloyDB::V1::AutomatedBackupPolicy::WeeklySchedule

**Parameter**

  * **value** ([::Google::Cloud::AlloyDB::V1::AutomatedBackupPolicy::WeeklySchedule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-AutomatedBackupPolicy-WeeklySchedule)) — Weekly schedule for the Backup. 



**Returns**

  * ([::Google::Cloud::AlloyDB::V1::AutomatedBackupPolicy::WeeklySchedule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1/latest/Google-Cloud-AlloyDB-V1-AutomatedBackupPolicy-WeeklySchedule)) — Weekly schedule for the Backup. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
