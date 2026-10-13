---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupConfigInfo/
title: Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::BackupConfigInfo (v1.11.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:14:40.575173+00:00
---

# Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::BackupConfigInfo (v1.11.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupConfigInfo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::BackupConfigInfo (v1.11.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.11.2 (latest)  1.11.1  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.5.0  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Backup and DR Service V1 API class Google::Cloud::BackupDR::V1::BackupConfigInfo.

BackupConfigInfo has information about how the resource is configured for Backup and about the most recent backup to this vault.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #backup_appliance_backup_config
    
    
    def backup_appliance_backup_config() -> ::Google::Cloud::BackupDR::V1::BackupApplianceBackupConfig

**Returns**

  * ([::Google::Cloud::BackupDR::V1::BackupApplianceBackupConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupApplianceBackupConfig)) — Configuration for an application backed up by a Backup Appliance.

Note: The following fields are mutually exclusive: `backup_appliance_backup_config`, `gcp_backup_config`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #backup_appliance_backup_config=
    
    
    def backup_appliance_backup_config=(value) -> ::Google::Cloud::BackupDR::V1::BackupApplianceBackupConfig

**Parameter**

  * **value** ([::Google::Cloud::BackupDR::V1::BackupApplianceBackupConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupApplianceBackupConfig)) — Configuration for an application backed up by a Backup Appliance.

Note: The following fields are mutually exclusive: `backup_appliance_backup_config`, `gcp_backup_config`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::BackupDR::V1::BackupApplianceBackupConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupApplianceBackupConfig)) — Configuration for an application backed up by a Backup Appliance.

Note: The following fields are mutually exclusive: `backup_appliance_backup_config`, `gcp_backup_config`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #gcp_backup_config
    
    
    def gcp_backup_config() -> ::Google::Cloud::BackupDR::V1::GcpBackupConfig

**Returns**

  * ([::Google::Cloud::BackupDR::V1::GcpBackupConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-GcpBackupConfig)) — Configuration for a Google Cloud resource.

Note: The following fields are mutually exclusive: `gcp_backup_config`, `backup_appliance_backup_config`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #gcp_backup_config=
    
    
    def gcp_backup_config=(value) -> ::Google::Cloud::BackupDR::V1::GcpBackupConfig

**Parameter**

  * **value** ([::Google::Cloud::BackupDR::V1::GcpBackupConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-GcpBackupConfig)) — Configuration for a Google Cloud resource.

Note: The following fields are mutually exclusive: `gcp_backup_config`, `backup_appliance_backup_config`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::BackupDR::V1::GcpBackupConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-GcpBackupConfig)) — Configuration for a Google Cloud resource.

Note: The following fields are mutually exclusive: `gcp_backup_config`, `backup_appliance_backup_config`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #last_backup_error
    
    
    def last_backup_error() -> ::Google::Rpc::Status

**Returns**

  * ([::Google::Rpc::Status](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Rpc-Status)) — Output only. If the last backup failed, this field has the error message. 



### #last_backup_state
    
    
    def last_backup_state() -> ::Google::Cloud::BackupDR::V1::BackupConfigInfo::LastBackupState

**Returns**

  * ([::Google::Cloud::BackupDR::V1::BackupConfigInfo::LastBackupState](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupConfigInfo-LastBackupState)) — Output only. The status of the last backup to this BackupVault 



### #last_successful_backup_consistency_time
    
    
    def last_successful_backup_consistency_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Protobuf-Timestamp)) — Output only. If the last backup were successful, this field has the consistency date. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
