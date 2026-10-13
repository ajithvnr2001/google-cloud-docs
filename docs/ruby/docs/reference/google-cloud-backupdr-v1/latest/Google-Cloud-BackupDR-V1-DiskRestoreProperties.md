---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DiskRestoreProperties/
title: Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::DiskRestoreProperties (v1.11.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:47:46.889311+00:00
---

# Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::DiskRestoreProperties (v1.11.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DiskRestoreProperties/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::DiskRestoreProperties (v1.11.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.11.2 (latest)  1.11.1  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.5.0  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Backup and DR Service V1 API class Google::Cloud::BackupDR::V1::DiskRestoreProperties.

DiskRestoreProperties represents the properties of a Disk restore.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #access_mode
    
    
    def access_mode() -> ::Google::Cloud::BackupDR::V1::DiskRestoreProperties::AccessMode

**Returns**

  * ([::Google::Cloud::BackupDR::V1::DiskRestoreProperties::AccessMode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DiskRestoreProperties-AccessMode)) — Optional. The access mode of the disk. 



### #access_mode=
    
    
    def access_mode=(value) -> ::Google::Cloud::BackupDR::V1::DiskRestoreProperties::AccessMode

**Parameter**

  * **value** ([::Google::Cloud::BackupDR::V1::DiskRestoreProperties::AccessMode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DiskRestoreProperties-AccessMode)) — Optional. The access mode of the disk. 



**Returns**

  * ([::Google::Cloud::BackupDR::V1::DiskRestoreProperties::AccessMode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DiskRestoreProperties-AccessMode)) — Optional. The access mode of the disk. 



### #architecture
    
    
    def architecture() -> ::Google::Cloud::BackupDR::V1::DiskRestoreProperties::Architecture

**Returns**

  * ([::Google::Cloud::BackupDR::V1::DiskRestoreProperties::Architecture](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DiskRestoreProperties-Architecture)) — Optional. The architecture of the source disk. Valid values are ARM64 or X86_64. 



### #architecture=
    
    
    def architecture=(value) -> ::Google::Cloud::BackupDR::V1::DiskRestoreProperties::Architecture

**Parameter**

  * **value** ([::Google::Cloud::BackupDR::V1::DiskRestoreProperties::Architecture](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DiskRestoreProperties-Architecture)) — Optional. The architecture of the source disk. Valid values are ARM64 or X86_64. 



**Returns**

  * ([::Google::Cloud::BackupDR::V1::DiskRestoreProperties::Architecture](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DiskRestoreProperties-Architecture)) — Optional. The architecture of the source disk. Valid values are ARM64 or X86_64. 



### #description
    
    
    def description() -> ::String

**Returns**

  * (::String) — Optional. An optional description of this resource. Provide this property when you create the resource. 



### #description=
    
    
    def description=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. An optional description of this resource. Provide this property when you create the resource. 



**Returns**

  * (::String) — Optional. An optional description of this resource. Provide this property when you create the resource. 



### #disk_encryption_key
    
    
    def disk_encryption_key() -> ::Google::Cloud::BackupDR::V1::CustomerEncryptionKey

**Returns**

  * ([::Google::Cloud::BackupDR::V1::CustomerEncryptionKey](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-CustomerEncryptionKey)) — Optional. Encrypts the disk using a customer-supplied encryption key or a customer-managed encryption key. 



### #disk_encryption_key=
    
    
    def disk_encryption_key=(value) -> ::Google::Cloud::BackupDR::V1::CustomerEncryptionKey

**Parameter**

  * **value** ([::Google::Cloud::BackupDR::V1::CustomerEncryptionKey](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-CustomerEncryptionKey)) — Optional. Encrypts the disk using a customer-supplied encryption key or a customer-managed encryption key. 



**Returns**

  * ([::Google::Cloud::BackupDR::V1::CustomerEncryptionKey](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-CustomerEncryptionKey)) — Optional. Encrypts the disk using a customer-supplied encryption key or a customer-managed encryption key. 



### #enable_confidential_compute
    
    
    def enable_confidential_compute() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. Indicates whether this disk is using confidential compute mode. Encryption with a Cloud KMS key is required to enable this option. 



### #enable_confidential_compute=
    
    
    def enable_confidential_compute=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. Indicates whether this disk is using confidential compute mode. Encryption with a Cloud KMS key is required to enable this option. 



**Returns**

  * (::Boolean) — Optional. Indicates whether this disk is using confidential compute mode. Encryption with a Cloud KMS key is required to enable this option. 



### #guest_os_feature
    
    
    def guest_os_feature() -> ::Array<::Google::Cloud::BackupDR::V1::GuestOsFeature>

**Returns**

  * (::Array<[::Google::Cloud::BackupDR::V1::GuestOsFeature](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-GuestOsFeature)>) — Optional. A list of features to enable in the guest operating system. This is applicable only for bootable images. 



### #guest_os_feature=
    
    
    def guest_os_feature=(value) -> ::Array<::Google::Cloud::BackupDR::V1::GuestOsFeature>

**Parameter**

  * **value** (::Array<[::Google::Cloud::BackupDR::V1::GuestOsFeature](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-GuestOsFeature)>) — Optional. A list of features to enable in the guest operating system. This is applicable only for bootable images. 



**Returns**

  * (::Array<[::Google::Cloud::BackupDR::V1::GuestOsFeature](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-GuestOsFeature)>) — Optional. A list of features to enable in the guest operating system. This is applicable only for bootable images. 



### #labels
    
    
    def labels() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. Labels to apply to this disk. These can be modified later using `setLabels` method. Label values can be empty. 



### #labels=
    
    
    def labels=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Optional. Labels to apply to this disk. These can be modified later using `setLabels` method. Label values can be empty. 



**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. Labels to apply to this disk. These can be modified later using `setLabels` method. Label values can be empty. 



### #licenses
    
    
    def licenses() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Optional. A list of publicly available licenses that are applicable to this backup. This is applicable if the original image had licenses attached, e.g. Windows image 



### #licenses=
    
    
    def licenses=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Optional. A list of publicly available licenses that are applicable to this backup. This is applicable if the original image had licenses attached, e.g. Windows image 



**Returns**

  * (::Array<::String>) — Optional. A list of publicly available licenses that are applicable to this backup. This is applicable if the original image had licenses attached, e.g. Windows image 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Required. Name of the disk. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Name of the disk. 



**Returns**

  * (::String) — Required. Name of the disk. 



### #physical_block_size_bytes
    
    
    def physical_block_size_bytes() -> ::Integer

**Returns**

  * (::Integer) — Optional. Physical block size of the persistent disk, in bytes. If not present in a request, a default value is used. Currently, the supported size is 4096. 



### #physical_block_size_bytes=
    
    
    def physical_block_size_bytes=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. Physical block size of the persistent disk, in bytes. If not present in a request, a default value is used. Currently, the supported size is 4096. 



**Returns**

  * (::Integer) — Optional. Physical block size of the persistent disk, in bytes. If not present in a request, a default value is used. Currently, the supported size is 4096. 



### #provisioned_iops
    
    
    def provisioned_iops() -> ::Integer

**Returns**

  * (::Integer) — Optional. Indicates how many IOPS to provision for the disk. This sets the number of I/O operations per second that the disk can handle. 



### #provisioned_iops=
    
    
    def provisioned_iops=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. Indicates how many IOPS to provision for the disk. This sets the number of I/O operations per second that the disk can handle. 



**Returns**

  * (::Integer) — Optional. Indicates how many IOPS to provision for the disk. This sets the number of I/O operations per second that the disk can handle. 



### #provisioned_throughput
    
    
    def provisioned_throughput() -> ::Integer

**Returns**

  * (::Integer) — Optional. Indicates how much throughput to provision for the disk. This sets the number of throughput MB per second that the disk can handle. 



### #provisioned_throughput=
    
    
    def provisioned_throughput=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. Indicates how much throughput to provision for the disk. This sets the number of throughput MB per second that the disk can handle. 



**Returns**

  * (::Integer) — Optional. Indicates how much throughput to provision for the disk. This sets the number of throughput MB per second that the disk can handle. 



### #resource_manager_tags
    
    
    def resource_manager_tags() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. Resource manager tags to be bound to the disk. 



### #resource_manager_tags=
    
    
    def resource_manager_tags=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Optional. Resource manager tags to be bound to the disk. 



**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. Resource manager tags to be bound to the disk. 



### #resource_policy
    
    
    def resource_policy() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Optional. Resource policies applied to this disk. 



### #resource_policy=
    
    
    def resource_policy=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Optional. Resource policies applied to this disk. 



**Returns**

  * (::Array<::String>) — Optional. Resource policies applied to this disk. 



### #size_gb
    
    
    def size_gb() -> ::Integer

**Returns**

  * (::Integer) — Required. The size of the disk in GB. 



### #size_gb=
    
    
    def size_gb=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Required. The size of the disk in GB. 



**Returns**

  * (::Integer) — Required. The size of the disk in GB. 



### #storage_pool
    
    
    def storage_pool() -> ::String

**Returns**

  * (::String) — Optional. The storage pool in which the new disk is created. You can provide this as a partial or full URL to the resource. 



### #storage_pool=
    
    
    def storage_pool=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The storage pool in which the new disk is created. You can provide this as a partial or full URL to the resource. 



**Returns**

  * (::String) — Optional. The storage pool in which the new disk is created. You can provide this as a partial or full URL to the resource. 



### #type
    
    
    def type() -> ::String

**Returns**

  * (::String) — Required. URL of the disk type resource describing which disk type to use to create the disk. 



### #type=
    
    
    def type=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. URL of the disk type resource describing which disk type to use to create the disk. 



**Returns**

  * (::String) — Required. URL of the disk type resource describing which disk type to use to create the disk. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
