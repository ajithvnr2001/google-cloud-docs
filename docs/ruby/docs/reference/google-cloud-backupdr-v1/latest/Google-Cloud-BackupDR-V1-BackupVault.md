---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupVault/
title: Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::BackupVault (v1.11.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:47:38.142797+00:00
---

# Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::BackupVault (v1.11.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupVault/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::BackupVault (v1.11.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.11.2 (latest)  1.11.1  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.5.0  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Backup and DR Service V1 API class Google::Cloud::BackupDR::V1::BackupVault.

Message describing a BackupVault object.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #access_restriction
    
    
    def access_restriction() -> ::Google::Cloud::BackupDR::V1::BackupVault::AccessRestriction

**Returns**

  * ([::Google::Cloud::BackupDR::V1::BackupVault::AccessRestriction](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupVault-AccessRestriction)) — Optional. Restricts access to certain sources and destinations for data being sent into, or restored from, the backup vault. Defaults to WITHIN_ORGANIZATION if not provided during creation. 



### #access_restriction=
    
    
    def access_restriction=(value) -> ::Google::Cloud::BackupDR::V1::BackupVault::AccessRestriction

**Parameter**

  * **value** ([::Google::Cloud::BackupDR::V1::BackupVault::AccessRestriction](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupVault-AccessRestriction)) — Optional. Restricts access to certain sources and destinations for data being sent into, or restored from, the backup vault. Defaults to WITHIN_ORGANIZATION if not provided during creation. 



**Returns**

  * ([::Google::Cloud::BackupDR::V1::BackupVault::AccessRestriction](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupVault-AccessRestriction)) — Optional. Restricts access to certain sources and destinations for data being sent into, or restored from, the backup vault. Defaults to WITHIN_ORGANIZATION if not provided during creation. 



### #annotations
    
    
    def annotations() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. User annotations. See https://google.aip.dev/128#annotations Stores small amounts of arbitrary data. 



### #annotations=
    
    
    def annotations=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Optional. User annotations. See https://google.aip.dev/128#annotations Stores small amounts of arbitrary data. 



**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. User annotations. See https://google.aip.dev/128#annotations Stores small amounts of arbitrary data. 



### #backup_count
    
    
    def backup_count() -> ::Integer

**Returns**

  * (::Integer) — Output only. The number of backups in this backup vault. 



### #backup_minimum_enforced_retention_duration
    
    
    def backup_minimum_enforced_retention_duration() -> ::Google::Protobuf::Duration

**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Protobuf-Duration)) — Required. The default and minimum enforced retention for each backup within the backup vault. The enforced retention for each backup can be extended. 



### #backup_minimum_enforced_retention_duration=
    
    
    def backup_minimum_enforced_retention_duration=(value) -> ::Google::Protobuf::Duration

**Parameter**

  * **value** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Protobuf-Duration)) — Required. The default and minimum enforced retention for each backup within the backup vault. The enforced retention for each backup can be extended. 



**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Protobuf-Duration)) — Required. The default and minimum enforced retention for each backup within the backup vault. The enforced retention for each backup can be extended. 



### #backup_retention_inheritance
    
    
    def backup_retention_inheritance() -> ::Google::Cloud::BackupDR::V1::BackupVault::BackupRetentionInheritance

**Returns**

  * ([::Google::Cloud::BackupDR::V1::BackupVault::BackupRetentionInheritance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupVault-BackupRetentionInheritance)) — Optional. Setting for how a backup's enforced retention end time is inherited. 



### #backup_retention_inheritance=
    
    
    def backup_retention_inheritance=(value) -> ::Google::Cloud::BackupDR::V1::BackupVault::BackupRetentionInheritance

**Parameter**

  * **value** ([::Google::Cloud::BackupDR::V1::BackupVault::BackupRetentionInheritance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupVault-BackupRetentionInheritance)) — Optional. Setting for how a backup's enforced retention end time is inherited. 



**Returns**

  * ([::Google::Cloud::BackupDR::V1::BackupVault::BackupRetentionInheritance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupVault-BackupRetentionInheritance)) — Optional. Setting for how a backup's enforced retention end time is inherited. 



### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Protobuf-Timestamp)) — Output only. The time when the instance was created. 



### #deletable
    
    
    def deletable() -> ::Boolean

**Returns**

  * (::Boolean) — Output only. Set to true when there are no backups nested under this resource. 



### #description
    
    
    def description() -> ::String

**Returns**

  * (::String) — Optional. The description of the BackupVault instance (2048 characters or less). 



### #description=
    
    
    def description=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The description of the BackupVault instance (2048 characters or less). 



**Returns**

  * (::String) — Optional. The description of the BackupVault instance (2048 characters or less). 



### #effective_time
    
    
    def effective_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Protobuf-Timestamp)) — Optional. Time after which the BackupVault resource is locked. 



### #effective_time=
    
    
    def effective_time=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Protobuf-Timestamp)) — Optional. Time after which the BackupVault resource is locked. 



**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Protobuf-Timestamp)) — Optional. Time after which the BackupVault resource is locked. 



### #encryption_config
    
    
    def encryption_config() -> ::Google::Cloud::BackupDR::V1::BackupVault::EncryptionConfig

**Returns**

  * ([::Google::Cloud::BackupDR::V1::BackupVault::EncryptionConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupVault-EncryptionConfig)) — Optional. The encryption config of the backup vault. 



### #encryption_config=
    
    
    def encryption_config=(value) -> ::Google::Cloud::BackupDR::V1::BackupVault::EncryptionConfig

**Parameter**

  * **value** ([::Google::Cloud::BackupDR::V1::BackupVault::EncryptionConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupVault-EncryptionConfig)) — Optional. The encryption config of the backup vault. 



**Returns**

  * ([::Google::Cloud::BackupDR::V1::BackupVault::EncryptionConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupVault-EncryptionConfig)) — Optional. The encryption config of the backup vault. 



### #etag
    
    
    def etag() -> ::String

**Returns**

  * (::String) — Optional. Server specified ETag for the backup vault resource to prevent simultaneous updates from overwiting each other. 



### #etag=
    
    
    def etag=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Server specified ETag for the backup vault resource to prevent simultaneous updates from overwiting each other. 



**Returns**

  * (::String) — Optional. Server specified ETag for the backup vault resource to prevent simultaneous updates from overwiting each other. 



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

  * (::String) — Output only. Identifier. Name of the backup vault to create. It must have the format`"projects/{project}/locations/{location}/backupVaults/{backupvault}"`. `{backupvault}` cannot be changed after creation. It must be between 3-63 characters long and must be unique within the project and location. 



### #service_account
    
    
    def service_account() -> ::String

**Returns**

  * (::String) — Output only. Service account used by the BackupVault Service for this BackupVault. The user should grant this account permissions in their workload project to enable the service to run backups and restores there. 



### #state
    
    
    def state() -> ::Google::Cloud::BackupDR::V1::BackupVault::State

**Returns**

  * ([::Google::Cloud::BackupDR::V1::BackupVault::State](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupVault-State)) — Output only. The BackupVault resource instance state. 



### #total_stored_bytes
    
    
    def total_stored_bytes() -> ::Integer

**Returns**

  * (::Integer) — Output only. Total size of the storage used by all backup resources. 



### #uid
    
    
    def uid() -> ::String

**Returns**

  * (::String) — Output only. Immutable after resource creation until resource deletion. 



### #update_time
    
    
    def update_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Protobuf-Timestamp)) — Output only. The time when the instance was updated. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
