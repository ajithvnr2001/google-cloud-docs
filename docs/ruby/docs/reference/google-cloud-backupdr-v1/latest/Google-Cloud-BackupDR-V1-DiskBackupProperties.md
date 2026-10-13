---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DiskBackupProperties/
title: Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::DiskBackupProperties (v1.11.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:47:46.479979+00:00
---

# Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::DiskBackupProperties (v1.11.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DiskBackupProperties/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::DiskBackupProperties (v1.11.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.11.2 (latest)  1.11.1  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.5.0  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Backup and DR Service V1 API class Google::Cloud::BackupDR::V1::DiskBackupProperties.

DiskBackupProperties represents the properties of a Disk backup.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #architecture
    
    
    def architecture() -> ::Google::Cloud::BackupDR::V1::DiskBackupProperties::Architecture

**Returns**

  * ([::Google::Cloud::BackupDR::V1::DiskBackupProperties::Architecture](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DiskBackupProperties-Architecture)) — The architecture of the source disk. Valid values are ARM64 or X86_64. 



### #architecture=
    
    
    def architecture=(value) -> ::Google::Cloud::BackupDR::V1::DiskBackupProperties::Architecture

**Parameter**

  * **value** ([::Google::Cloud::BackupDR::V1::DiskBackupProperties::Architecture](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DiskBackupProperties-Architecture)) — The architecture of the source disk. Valid values are ARM64 or X86_64. 



**Returns**

  * ([::Google::Cloud::BackupDR::V1::DiskBackupProperties::Architecture](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DiskBackupProperties-Architecture)) — The architecture of the source disk. Valid values are ARM64 or X86_64. 



### #description
    
    
    def description() -> ::String

**Returns**

  * (::String) — A description of the source disk. 



### #description=
    
    
    def description=(value) -> ::String

**Parameter**

  * **value** (::String) — A description of the source disk. 



**Returns**

  * (::String) — A description of the source disk. 



### #guest_os_feature
    
    
    def guest_os_feature() -> ::Array<::Google::Cloud::BackupDR::V1::GuestOsFeature>

**Returns**

  * (::Array<[::Google::Cloud::BackupDR::V1::GuestOsFeature](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-GuestOsFeature)>) — A list of guest OS features that are applicable to this backup. 



### #guest_os_feature=
    
    
    def guest_os_feature=(value) -> ::Array<::Google::Cloud::BackupDR::V1::GuestOsFeature>

**Parameter**

  * **value** (::Array<[::Google::Cloud::BackupDR::V1::GuestOsFeature](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-GuestOsFeature)>) — A list of guest OS features that are applicable to this backup. 



**Returns**

  * (::Array<[::Google::Cloud::BackupDR::V1::GuestOsFeature](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-GuestOsFeature)>) — A list of guest OS features that are applicable to this backup. 



### #licenses
    
    
    def licenses() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — A list of publicly available licenses that are applicable to this backup. This is applicable if the original image had licenses attached, e.g. Windows image. 



### #licenses=
    
    
    def licenses=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — A list of publicly available licenses that are applicable to this backup. This is applicable if the original image had licenses attached, e.g. Windows image. 



**Returns**

  * (::Array<::String>) — A list of publicly available licenses that are applicable to this backup. This is applicable if the original image had licenses attached, e.g. Windows image. 



### #region
    
    
    def region() -> ::String

**Returns**

  * (::String) — Region and zone are mutually exclusive fields. The URL of the region of the source disk. 



### #region=
    
    
    def region=(value) -> ::String

**Parameter**

  * **value** (::String) — Region and zone are mutually exclusive fields. The URL of the region of the source disk. 



**Returns**

  * (::String) — Region and zone are mutually exclusive fields. The URL of the region of the source disk. 



### #replica_zones
    
    
    def replica_zones() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — The URL of the Zones where the source disk should be replicated. 



### #replica_zones=
    
    
    def replica_zones=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — The URL of the Zones where the source disk should be replicated. 



**Returns**

  * (::Array<::String>) — The URL of the Zones where the source disk should be replicated. 



### #size_gb
    
    
    def size_gb() -> ::Integer

**Returns**

  * (::Integer) — Size(in GB) of the source disk. 



### #size_gb=
    
    
    def size_gb=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Size(in GB) of the source disk. 



**Returns**

  * (::Integer) — Size(in GB) of the source disk. 



### #source_disk
    
    
    def source_disk() -> ::String

**Returns**

  * (::String) — The source disk used to create this backup. 



### #source_disk=
    
    
    def source_disk=(value) -> ::String

**Parameter**

  * **value** (::String) — The source disk used to create this backup. 



**Returns**

  * (::String) — The source disk used to create this backup. 



### #type
    
    
    def type() -> ::String

**Returns**

  * (::String) — The URL of the type of the disk. 



### #type=
    
    
    def type=(value) -> ::String

**Parameter**

  * **value** (::String) — The URL of the type of the disk. 



**Returns**

  * (::String) — The URL of the type of the disk. 



### #zone
    
    
    def zone() -> ::String

**Returns**

  * (::String) — The URL of the Zone where the source disk. 



### #zone=
    
    
    def zone=(value) -> ::String

**Parameter**

  * **value** (::String) — The URL of the Zone where the source disk. 



**Returns**

  * (::String) — The URL of the Zone where the source disk. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
