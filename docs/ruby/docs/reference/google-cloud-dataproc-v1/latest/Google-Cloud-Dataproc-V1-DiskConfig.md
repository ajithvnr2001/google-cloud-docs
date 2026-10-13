---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-DiskConfig/
title: Cloud Dataproc V1 API - Class Google::Cloud::Dataproc::V1::DiskConfig (v1.17.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:20:58.120035+00:00
---

# Cloud Dataproc V1 API - Class Google::Cloud::Dataproc::V1::DiskConfig (v1.17.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-DiskConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Dataproc V1 API - Class Google::Cloud::Dataproc::V1::DiskConfig (v1.17.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.17.1 (latest)  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.1  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.1  1.2.0  1.1.0  1.0.2  0.26.0  0.25.0  0.24.1  0.23.1  0.22.0  0.21.0  0.20.0  0.19.0  0.18.1  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.1 

Reference documentation and code samples for the Cloud Dataproc V1 API class Google::Cloud::Dataproc::V1::DiskConfig.

Specifies the config of boot disk and attached disk options for a group of VM instances.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #attached_disk_configs
    
    
    def attached_disk_configs() -> ::Array<::Google::Cloud::Dataproc::V1::AttachedDiskConfig>

**Returns**

  * (::Array<[::Google::Cloud::Dataproc::V1::AttachedDiskConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-AttachedDiskConfig)>) — Optional. A list of attached disk configs for a group of VM instances. 



### #attached_disk_configs=
    
    
    def attached_disk_configs=(value) -> ::Array<::Google::Cloud::Dataproc::V1::AttachedDiskConfig>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Dataproc::V1::AttachedDiskConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-AttachedDiskConfig)>) — Optional. A list of attached disk configs for a group of VM instances. 



**Returns**

  * (::Array<[::Google::Cloud::Dataproc::V1::AttachedDiskConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-AttachedDiskConfig)>) — Optional. A list of attached disk configs for a group of VM instances. 



### #boot_disk_provisioned_iops
    
    
    def boot_disk_provisioned_iops() -> ::Integer

**Returns**

  * (::Integer) — Optional. Indicates how many IOPS to provision for the disk. This sets the number of I/O operations per second that the disk can handle. **This field is supported only if[boot_disk_type](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-DiskConfig#Google__Cloud__Dataproc__V1__DiskConfig_boot_disk_type_instance_ "Google::Cloud::Dataproc::V1::DiskConfig#boot_disk_type \(method\)") is `hyperdisk-balanced`.**



### #boot_disk_provisioned_iops=
    
    
    def boot_disk_provisioned_iops=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. Indicates how many IOPS to provision for the disk. This sets the number of I/O operations per second that the disk can handle. **This field is supported only if[boot_disk_type](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-DiskConfig#Google__Cloud__Dataproc__V1__DiskConfig_boot_disk_type_instance_ "Google::Cloud::Dataproc::V1::DiskConfig#boot_disk_type \(method\)") is `hyperdisk-balanced`.**



**Returns**

  * (::Integer) — Optional. Indicates how many IOPS to provision for the disk. This sets the number of I/O operations per second that the disk can handle. **This field is supported only if[boot_disk_type](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-DiskConfig#Google__Cloud__Dataproc__V1__DiskConfig_boot_disk_type_instance_ "Google::Cloud::Dataproc::V1::DiskConfig#boot_disk_type \(method\)") is `hyperdisk-balanced`.**



### #boot_disk_provisioned_throughput
    
    
    def boot_disk_provisioned_throughput() -> ::Integer

**Returns**

  * (::Integer) — Optional. Indicates how much throughput to provision for the disk. This sets the number of throughput mb per second that the disk can handle. Values must be greater than or equal to 1. **This field is supported only if[boot_disk_type](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-DiskConfig#Google__Cloud__Dataproc__V1__DiskConfig_boot_disk_type_instance_ "Google::Cloud::Dataproc::V1::DiskConfig#boot_disk_type \(method\)") is `hyperdisk-balanced`.**



### #boot_disk_provisioned_throughput=
    
    
    def boot_disk_provisioned_throughput=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. Indicates how much throughput to provision for the disk. This sets the number of throughput mb per second that the disk can handle. Values must be greater than or equal to 1. **This field is supported only if[boot_disk_type](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-DiskConfig#Google__Cloud__Dataproc__V1__DiskConfig_boot_disk_type_instance_ "Google::Cloud::Dataproc::V1::DiskConfig#boot_disk_type \(method\)") is `hyperdisk-balanced`.**



**Returns**

  * (::Integer) — Optional. Indicates how much throughput to provision for the disk. This sets the number of throughput mb per second that the disk can handle. Values must be greater than or equal to 1. **This field is supported only if[boot_disk_type](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-DiskConfig#Google__Cloud__Dataproc__V1__DiskConfig_boot_disk_type_instance_ "Google::Cloud::Dataproc::V1::DiskConfig#boot_disk_type \(method\)") is `hyperdisk-balanced`.**



### #boot_disk_size_gb
    
    
    def boot_disk_size_gb() -> ::Integer

**Returns**

  * (::Integer) — Optional. Size in GB of the boot disk (default is 500GB). 



### #boot_disk_size_gb=
    
    
    def boot_disk_size_gb=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. Size in GB of the boot disk (default is 500GB). 



**Returns**

  * (::Integer) — Optional. Size in GB of the boot disk (default is 500GB). 



### #boot_disk_type
    
    
    def boot_disk_type() -> ::String

**Returns**

  * (::String) — Optional. Type of the boot disk (default is `pd-standard`). Valid values: `pd-balanced` (Persistent Disk Balanced Solid State Drive), `pd-ssd` (Persistent Disk Solid State Drive), or `pd-standard` (Persistent Disk Hard Disk Drive). See [Disk types](https://cloud.google.com/compute/docs/disks#disk-types). 



### #boot_disk_type=
    
    
    def boot_disk_type=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Type of the boot disk (default is `pd-standard`). Valid values: `pd-balanced` (Persistent Disk Balanced Solid State Drive), `pd-ssd` (Persistent Disk Solid State Drive), or `pd-standard` (Persistent Disk Hard Disk Drive). See [Disk types](https://cloud.google.com/compute/docs/disks#disk-types). 



**Returns**

  * (::String) — Optional. Type of the boot disk (default is `pd-standard`). Valid values: `pd-balanced` (Persistent Disk Balanced Solid State Drive), `pd-ssd` (Persistent Disk Solid State Drive), or `pd-standard` (Persistent Disk Hard Disk Drive). See [Disk types](https://cloud.google.com/compute/docs/disks#disk-types). 



### #local_ssd_interface
    
    
    def local_ssd_interface() -> ::String

**Returns**

  * (::String) — Optional. Interface type of local SSDs (default is `scsi`). Valid values: `scsi` (Small Computer System Interface), `nvme` (Non-Volatile Memory Express). See [local SSD performance](https://cloud.google.com/compute/docs/disks/local-ssd#performance). 



### #local_ssd_interface=
    
    
    def local_ssd_interface=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Interface type of local SSDs (default is `scsi`). Valid values: `scsi` (Small Computer System Interface), `nvme` (Non-Volatile Memory Express). See [local SSD performance](https://cloud.google.com/compute/docs/disks/local-ssd#performance). 



**Returns**

  * (::String) — Optional. Interface type of local SSDs (default is `scsi`). Valid values: `scsi` (Small Computer System Interface), `nvme` (Non-Volatile Memory Express). See [local SSD performance](https://cloud.google.com/compute/docs/disks/local-ssd#performance). 



### #num_local_ssds
    
    
    def num_local_ssds() -> ::Integer

**Returns**

  * (::Integer) — Optional. Number of attached SSDs, from 0 to 8 (default is 0). If SSDs are not attached, the boot disk is used to store runtime logs and [HDFS](https://hadoop.apache.org/docs/r1.2.1/hdfs_user_guide.html) data. If one or more SSDs are attached, this runtime bulk data is spread across them, and the boot disk contains only basic config and installed binaries.

Note: Local SSD options may vary by machine type and number of vCPUs selected. 




### #num_local_ssds=
    
    
    def num_local_ssds=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. Number of attached SSDs, from 0 to 8 (default is 0). If SSDs are not attached, the boot disk is used to store runtime logs and [HDFS](https://hadoop.apache.org/docs/r1.2.1/hdfs_user_guide.html) data. If one or more SSDs are attached, this runtime bulk data is spread across them, and the boot disk contains only basic config and installed binaries.

Note: Local SSD options may vary by machine type and number of vCPUs selected. 




**Returns**

  * (::Integer) — Optional. Number of attached SSDs, from 0 to 8 (default is 0). If SSDs are not attached, the boot disk is used to store runtime logs and [HDFS](https://hadoop.apache.org/docs/r1.2.1/hdfs_user_guide.html) data. If one or more SSDs are attached, this runtime bulk data is spread across them, and the boot disk contains only basic config and installed binaries.

Note: Local SSD options may vary by machine type and number of vCPUs selected. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
