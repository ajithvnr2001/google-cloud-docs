---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupApplianceLockInfo/
title: Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::BackupApplianceLockInfo (v1.11.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:47:28.644338+00:00
---

# Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::BackupApplianceLockInfo (v1.11.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupApplianceLockInfo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::BackupApplianceLockInfo (v1.11.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.11.2 (latest)  1.11.1  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.5.0  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Backup and DR Service V1 API class Google::Cloud::BackupDR::V1::BackupApplianceLockInfo.

BackupApplianceLockInfo contains metadata about the backupappliance that created the lock.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #backup_appliance_id
    
    
    def backup_appliance_id() -> ::Integer

**Returns**

  * (::Integer) — Required. The ID of the backup/recovery appliance that created this lock. 



### #backup_appliance_id=
    
    
    def backup_appliance_id=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Required. The ID of the backup/recovery appliance that created this lock. 



**Returns**

  * (::Integer) — Required. The ID of the backup/recovery appliance that created this lock. 



### #backup_appliance_name
    
    
    def backup_appliance_name() -> ::String

**Returns**

  * (::String) — Required. The name of the backup/recovery appliance that created this lock. 



### #backup_appliance_name=
    
    
    def backup_appliance_name=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The name of the backup/recovery appliance that created this lock. 



**Returns**

  * (::String) — Required. The name of the backup/recovery appliance that created this lock. 



### #backup_image
    
    
    def backup_image() -> ::String

**Returns**

  * (::String) — The image name that depends on this Backup.

Note: The following fields are mutually exclusive: `backup_image`, `job_name`, `sla_id`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #backup_image=
    
    
    def backup_image=(value) -> ::String

**Parameter**

  * **value** (::String) — The image name that depends on this Backup.

Note: The following fields are mutually exclusive: `backup_image`, `job_name`, `sla_id`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::String) — The image name that depends on this Backup.

Note: The following fields are mutually exclusive: `backup_image`, `job_name`, `sla_id`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #job_name
    
    
    def job_name() -> ::String

**Returns**

  * (::String) — The job name on the backup/recovery appliance that created this lock.

Note: The following fields are mutually exclusive: `job_name`, `backup_image`, `sla_id`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #job_name=
    
    
    def job_name=(value) -> ::String

**Parameter**

  * **value** (::String) — The job name on the backup/recovery appliance that created this lock.

Note: The following fields are mutually exclusive: `job_name`, `backup_image`, `sla_id`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::String) — The job name on the backup/recovery appliance that created this lock.

Note: The following fields are mutually exclusive: `job_name`, `backup_image`, `sla_id`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #lock_reason
    
    
    def lock_reason() -> ::String

**Returns**

  * (::String) — Required. The reason for the lock: e.g. MOUNT/RESTORE/BACKUP/etc. The value of this string is only meaningful to the client and it is not interpreted by the BackupVault service. 



### #lock_reason=
    
    
    def lock_reason=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The reason for the lock: e.g. MOUNT/RESTORE/BACKUP/etc. The value of this string is only meaningful to the client and it is not interpreted by the BackupVault service. 



**Returns**

  * (::String) — Required. The reason for the lock: e.g. MOUNT/RESTORE/BACKUP/etc. The value of this string is only meaningful to the client and it is not interpreted by the BackupVault service. 



### #sla_id
    
    
    def sla_id() -> ::Integer

**Returns**

  * (::Integer) — The SLA on the backup/recovery appliance that owns the lock.

Note: The following fields are mutually exclusive: `sla_id`, `job_name`, `backup_image`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #sla_id=
    
    
    def sla_id=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The SLA on the backup/recovery appliance that owns the lock.

Note: The following fields are mutually exclusive: `sla_id`, `job_name`, `backup_image`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::Integer) — The SLA on the backup/recovery appliance that owns the lock.

Note: The following fields are mutually exclusive: `sla_id`, `job_name`, `backup_image`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
