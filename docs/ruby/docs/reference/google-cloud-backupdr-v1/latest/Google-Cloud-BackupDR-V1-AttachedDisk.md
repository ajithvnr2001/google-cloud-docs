---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-AttachedDisk/
title: Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::AttachedDisk (v1.11.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:47:26.376729+00:00
---

# Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::AttachedDisk (v1.11.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-AttachedDisk/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::AttachedDisk (v1.11.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.11.2 (latest)  1.11.1  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.5.0  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Backup and DR Service V1 API class Google::Cloud::BackupDR::V1::AttachedDisk.

An instance-attached disk resource.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #auto_delete
    
    
    def auto_delete() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. Specifies whether the disk will be auto-deleted when the instance is deleted (but not when the disk is detached from the instance). 



### #auto_delete=
    
    
    def auto_delete=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. Specifies whether the disk will be auto-deleted when the instance is deleted (but not when the disk is detached from the instance). 



**Returns**

  * (::Boolean) — Optional. Specifies whether the disk will be auto-deleted when the instance is deleted (but not when the disk is detached from the instance). 



### #boot
    
    
    def boot() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. Indicates that this is a boot disk. The virtual machine will use the first partition of the disk for its root filesystem. 



### #boot=
    
    
    def boot=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. Indicates that this is a boot disk. The virtual machine will use the first partition of the disk for its root filesystem. 



**Returns**

  * (::Boolean) — Optional. Indicates that this is a boot disk. The virtual machine will use the first partition of the disk for its root filesystem. 



### #device_name
    
    
    def device_name() -> ::String

**Returns**

  * (::String) — Optional. This is used as an identifier for the disks. This is the unique name has to provided to modify disk parameters like disk_name and replica_zones (in case of RePDs) 



### #device_name=
    
    
    def device_name=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. This is used as an identifier for the disks. This is the unique name has to provided to modify disk parameters like disk_name and replica_zones (in case of RePDs) 



**Returns**

  * (::String) — Optional. This is used as an identifier for the disks. This is the unique name has to provided to modify disk parameters like disk_name and replica_zones (in case of RePDs) 



### #disk_encryption_key
    
    
    def disk_encryption_key() -> ::Google::Cloud::BackupDR::V1::CustomerEncryptionKey

**Returns**

  * ([::Google::Cloud::BackupDR::V1::CustomerEncryptionKey](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-CustomerEncryptionKey)) — Optional. Encrypts or decrypts a disk using a customer-supplied encryption key. 



### #disk_encryption_key=
    
    
    def disk_encryption_key=(value) -> ::Google::Cloud::BackupDR::V1::CustomerEncryptionKey

**Parameter**

  * **value** ([::Google::Cloud::BackupDR::V1::CustomerEncryptionKey](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-CustomerEncryptionKey)) — Optional. Encrypts or decrypts a disk using a customer-supplied encryption key. 



**Returns**

  * ([::Google::Cloud::BackupDR::V1::CustomerEncryptionKey](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-CustomerEncryptionKey)) — Optional. Encrypts or decrypts a disk using a customer-supplied encryption key. 



### #disk_interface
    
    
    def disk_interface() -> ::Google::Cloud::BackupDR::V1::AttachedDisk::DiskInterface

**Returns**

  * ([::Google::Cloud::BackupDR::V1::AttachedDisk::DiskInterface](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-AttachedDisk-DiskInterface)) — Optional. Specifies the disk interface to use for attaching this disk. 



### #disk_interface=
    
    
    def disk_interface=(value) -> ::Google::Cloud::BackupDR::V1::AttachedDisk::DiskInterface

**Parameter**

  * **value** ([::Google::Cloud::BackupDR::V1::AttachedDisk::DiskInterface](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-AttachedDisk-DiskInterface)) — Optional. Specifies the disk interface to use for attaching this disk. 



**Returns**

  * ([::Google::Cloud::BackupDR::V1::AttachedDisk::DiskInterface](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-AttachedDisk-DiskInterface)) — Optional. Specifies the disk interface to use for attaching this disk. 



### #disk_size_gb
    
    
    def disk_size_gb() -> ::Integer

**Returns**

  * (::Integer) — Optional. The size of the disk in GB. 



### #disk_size_gb=
    
    
    def disk_size_gb=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. The size of the disk in GB. 



**Returns**

  * (::Integer) — Optional. The size of the disk in GB. 



### #disk_type
    
    
    def disk_type() -> ::String

**Returns**

  * (::String) — Optional. Output only. The URI of the disk type resource. For example: projects/project/zones/zone/diskTypes/pd-standard or pd-ssd 



### #disk_type_deprecated
    
    
    def disk_type_deprecated() -> ::Google::Cloud::BackupDR::V1::AttachedDisk::DiskType

**Returns**

  * ([::Google::Cloud::BackupDR::V1::AttachedDisk::DiskType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-AttachedDisk-DiskType)) — Specifies the type of the disk. 



### #disk_type_deprecated=
    
    
    def disk_type_deprecated=(value) -> ::Google::Cloud::BackupDR::V1::AttachedDisk::DiskType

**Parameter**

  * **value** ([::Google::Cloud::BackupDR::V1::AttachedDisk::DiskType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-AttachedDisk-DiskType)) — Specifies the type of the disk. 



**Returns**

  * ([::Google::Cloud::BackupDR::V1::AttachedDisk::DiskType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-AttachedDisk-DiskType)) — Specifies the type of the disk. 



### #guest_os_feature
    
    
    def guest_os_feature() -> ::Array<::Google::Cloud::BackupDR::V1::GuestOsFeature>

**Returns**

  * (::Array<[::Google::Cloud::BackupDR::V1::GuestOsFeature](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-GuestOsFeature)>) — Optional. A list of features to enable on the guest operating system. Applicable only for bootable images. 



### #guest_os_feature=
    
    
    def guest_os_feature=(value) -> ::Array<::Google::Cloud::BackupDR::V1::GuestOsFeature>

**Parameter**

  * **value** (::Array<[::Google::Cloud::BackupDR::V1::GuestOsFeature](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-GuestOsFeature)>) — Optional. A list of features to enable on the guest operating system. Applicable only for bootable images. 



**Returns**

  * (::Array<[::Google::Cloud::BackupDR::V1::GuestOsFeature](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-GuestOsFeature)>) — Optional. A list of features to enable on the guest operating system. Applicable only for bootable images. 



### #index
    
    
    def index() -> ::Integer

**Returns**

  * (::Integer) — Optional. A zero-based index to this disk, where 0 is reserved for the boot disk. 



### #index=
    
    
    def index=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. A zero-based index to this disk, where 0 is reserved for the boot disk. 



**Returns**

  * (::Integer) — Optional. A zero-based index to this disk, where 0 is reserved for the boot disk. 



### #initialize_params
    
    
    def initialize_params() -> ::Google::Cloud::BackupDR::V1::AttachedDisk::InitializeParams

**Returns**

  * ([::Google::Cloud::BackupDR::V1::AttachedDisk::InitializeParams](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-AttachedDisk-InitializeParams)) — Optional. Specifies the parameters to initialize this disk. 



### #initialize_params=
    
    
    def initialize_params=(value) -> ::Google::Cloud::BackupDR::V1::AttachedDisk::InitializeParams

**Parameter**

  * **value** ([::Google::Cloud::BackupDR::V1::AttachedDisk::InitializeParams](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-AttachedDisk-InitializeParams)) — Optional. Specifies the parameters to initialize this disk. 



**Returns**

  * ([::Google::Cloud::BackupDR::V1::AttachedDisk::InitializeParams](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-AttachedDisk-InitializeParams)) — Optional. Specifies the parameters to initialize this disk. 



### #kind
    
    
    def kind() -> ::String

**Returns**

  * (::String) — Optional. Type of the resource. 



### #kind=
    
    
    def kind=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Type of the resource. 



**Returns**

  * (::String) — Optional. Type of the resource. 



### #license
    
    
    def license() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Optional. Any valid publicly visible licenses. 



### #license=
    
    
    def license=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Optional. Any valid publicly visible licenses. 



**Returns**

  * (::Array<::String>) — Optional. Any valid publicly visible licenses. 



### #mode
    
    
    def mode() -> ::Google::Cloud::BackupDR::V1::AttachedDisk::DiskMode

**Returns**

  * ([::Google::Cloud::BackupDR::V1::AttachedDisk::DiskMode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-AttachedDisk-DiskMode)) — Optional. The mode in which to attach this disk. 



### #mode=
    
    
    def mode=(value) -> ::Google::Cloud::BackupDR::V1::AttachedDisk::DiskMode

**Parameter**

  * **value** ([::Google::Cloud::BackupDR::V1::AttachedDisk::DiskMode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-AttachedDisk-DiskMode)) — Optional. The mode in which to attach this disk. 



**Returns**

  * ([::Google::Cloud::BackupDR::V1::AttachedDisk::DiskMode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-AttachedDisk-DiskMode)) — Optional. The mode in which to attach this disk. 



### #saved_state
    
    
    def saved_state() -> ::Google::Cloud::BackupDR::V1::AttachedDisk::DiskSavedState

**Returns**

  * ([::Google::Cloud::BackupDR::V1::AttachedDisk::DiskSavedState](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-AttachedDisk-DiskSavedState)) — Optional. Output only. The state of the disk. 



### #source
    
    
    def source() -> ::String

**Returns**

  * (::String) — Optional. Specifies a valid partial or full URL to an existing Persistent Disk resource. 



### #source=
    
    
    def source=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Specifies a valid partial or full URL to an existing Persistent Disk resource. 



**Returns**

  * (::String) — Optional. Specifies a valid partial or full URL to an existing Persistent Disk resource. 



### #type
    
    
    def type() -> ::Google::Cloud::BackupDR::V1::AttachedDisk::DiskType

**Returns**

  * ([::Google::Cloud::BackupDR::V1::AttachedDisk::DiskType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-AttachedDisk-DiskType)) — Optional. Specifies the type of the disk. 



### #type=
    
    
    def type=(value) -> ::Google::Cloud::BackupDR::V1::AttachedDisk::DiskType

**Parameter**

  * **value** ([::Google::Cloud::BackupDR::V1::AttachedDisk::DiskType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-AttachedDisk-DiskType)) — Optional. Specifies the type of the disk. 



**Returns**

  * ([::Google::Cloud::BackupDR::V1::AttachedDisk::DiskType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-AttachedDisk-DiskType)) — Optional. Specifies the type of the disk. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
