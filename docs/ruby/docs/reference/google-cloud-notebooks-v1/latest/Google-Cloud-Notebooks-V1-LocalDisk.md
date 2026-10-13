---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-LocalDisk/
title: AI Platform Notebooks V1 API - Class Google::Cloud::Notebooks::V1::LocalDisk (v1.6.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:14:06.797311+00:00
---

# AI Platform Notebooks V1 API - Class Google::Cloud::Notebooks::V1::LocalDisk (v1.6.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-LocalDisk/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  AI Platform Notebooks V1 API - Class Google::Cloud::Notebooks::V1::LocalDisk (v1.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.6.0 (latest)  1.5.0  1.4.0  1.3.1  1.2.0  1.1.0  1.0.1  0.11.0  0.10.0  0.9.1  0.8.2  0.7.0  0.6.1  0.5.0  0.4.2  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the AI Platform Notebooks V1 API class Google::Cloud::Notebooks::V1::LocalDisk.

A Local attached disk resource.

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

  * (::Boolean) — Optional. Output only. Specifies whether the disk will be auto-deleted when the instance is deleted (but not when the disk is detached from the instance). 



### #boot
    
    
    def boot() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. Output only. Indicates that this is a boot disk. The virtual machine will use the first partition of the disk for its root filesystem. 



### #device_name
    
    
    def device_name() -> ::String

**Returns**

  * (::String) — Optional. Output only. Specifies a unique device name of your choice that is reflected into the `/dev/disk/by-id/google-*` tree of a Linux operating system running within the instance. This name can be used to reference the device for mounting, resizing, and so on, from within the instance.

If not specified, the server chooses a default device name to apply to this disk, in the form persistent-disk-x, where x is a number assigned by Google Compute Engine. This field is only applicable for persistent disks. 




### #guest_os_features
    
    
    def guest_os_features() -> ::Array<::Google::Cloud::Notebooks::V1::LocalDisk::RuntimeGuestOsFeature>

**Returns**

  * (::Array<[::Google::Cloud::Notebooks::V1::LocalDisk::RuntimeGuestOsFeature](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-LocalDisk-RuntimeGuestOsFeature)>) — Output only. Indicates a list of features to enable on the guest operating system. Applicable only for bootable images. Read Enabling guest operating system features to see a list of available options. 



### #index
    
    
    def index() -> ::Integer

**Returns**

  * (::Integer) — Output only. A zero-based index to this disk, where 0 is reserved for the boot disk. If you have many disks attached to an instance, each disk would have a unique index number. 



### #initialize_params
    
    
    def initialize_params() -> ::Google::Cloud::Notebooks::V1::LocalDiskInitializeParams

**Returns**

  * ([::Google::Cloud::Notebooks::V1::LocalDiskInitializeParams](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-LocalDiskInitializeParams)) — Input only. Specifies the parameters for a new disk that will be created alongside the new instance. Use initialization parameters to create boot disks or local SSDs attached to the new instance.

This property is mutually exclusive with the source property; you can only define one or the other, but not both. 




### #initialize_params=
    
    
    def initialize_params=(value) -> ::Google::Cloud::Notebooks::V1::LocalDiskInitializeParams

**Parameter**

  * **value** ([::Google::Cloud::Notebooks::V1::LocalDiskInitializeParams](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-LocalDiskInitializeParams)) — Input only. Specifies the parameters for a new disk that will be created alongside the new instance. Use initialization parameters to create boot disks or local SSDs attached to the new instance.

This property is mutually exclusive with the source property; you can only define one or the other, but not both. 




**Returns**

  * ([::Google::Cloud::Notebooks::V1::LocalDiskInitializeParams](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-LocalDiskInitializeParams)) — Input only. Specifies the parameters for a new disk that will be created alongside the new instance. Use initialization parameters to create boot disks or local SSDs attached to the new instance.

This property is mutually exclusive with the source property; you can only define one or the other, but not both. 




### #interface
    
    
    def interface() -> ::String

**Returns**

  * (::String) — 

Specifies the disk interface to use for attaching this disk, which is either SCSI or NVME. The default is SCSI. Persistent disks must always use SCSI and the request will fail if you attempt to attach a persistent disk in any other format than SCSI. Local SSDs can use either NVME or SCSI. For performance characteristics of SCSI over NVMe, see Local SSD performance. Valid values:

    * `NVME`
    * `SCSI`



### #interface=
    
    
    def interface=(value) -> ::String

**Parameter**

  * **value** (::String) — 

Specifies the disk interface to use for attaching this disk, which is either SCSI or NVME. The default is SCSI. Persistent disks must always use SCSI and the request will fail if you attempt to attach a persistent disk in any other format than SCSI. Local SSDs can use either NVME or SCSI. For performance characteristics of SCSI over NVMe, see Local SSD performance. Valid values:

    * `NVME`
    * `SCSI`



**Returns**

  * (::String) — 

Specifies the disk interface to use for attaching this disk, which is either SCSI or NVME. The default is SCSI. Persistent disks must always use SCSI and the request will fail if you attempt to attach a persistent disk in any other format than SCSI. Local SSDs can use either NVME or SCSI. For performance characteristics of SCSI over NVMe, see Local SSD performance. Valid values:

    * `NVME`
    * `SCSI`



### #kind
    
    
    def kind() -> ::String

**Returns**

  * (::String) — Output only. Type of the resource. Always compute#attachedDisk for attached disks. 



### #licenses
    
    
    def licenses() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Output only. Any valid publicly visible licenses. 



### #mode
    
    
    def mode() -> ::String

**Returns**

  * (::String) — 

The mode in which to attach this disk, either `READ_WRITE` or `READ_ONLY`. If not specified, the default is to attach the disk in `READ_WRITE` mode. Valid values:

    * `READ_ONLY`
    * `READ_WRITE`



### #mode=
    
    
    def mode=(value) -> ::String

**Parameter**

  * **value** (::String) — 

The mode in which to attach this disk, either `READ_WRITE` or `READ_ONLY`. If not specified, the default is to attach the disk in `READ_WRITE` mode. Valid values:

    * `READ_ONLY`
    * `READ_WRITE`



**Returns**

  * (::String) — 

The mode in which to attach this disk, either `READ_WRITE` or `READ_ONLY`. If not specified, the default is to attach the disk in `READ_WRITE` mode. Valid values:

    * `READ_ONLY`
    * `READ_WRITE`



### #source
    
    
    def source() -> ::String

**Returns**

  * (::String) — Specifies a valid partial or full URL to an existing Persistent Disk resource. 



### #source=
    
    
    def source=(value) -> ::String

**Parameter**

  * **value** (::String) — Specifies a valid partial or full URL to an existing Persistent Disk resource. 



**Returns**

  * (::String) — Specifies a valid partial or full URL to an existing Persistent Disk resource. 



### #type
    
    
    def type() -> ::String

**Returns**

  * (::String) — 

Specifies the type of the disk, either `SCRATCH` or `PERSISTENT`. If not specified, the default is `PERSISTENT`. Valid values:

    * `PERSISTENT`
    * `SCRATCH`



### #type=
    
    
    def type=(value) -> ::String

**Parameter**

  * **value** (::String) — 

Specifies the type of the disk, either `SCRATCH` or `PERSISTENT`. If not specified, the default is `PERSISTENT`. Valid values:

    * `PERSISTENT`
    * `SCRATCH`



**Returns**

  * (::String) — 

Specifies the type of the disk, either `SCRATCH` or `PERSISTENT`. If not specified, the default is `PERSISTENT`. Valid values:

    * `PERSISTENT`
    * `SCRATCH`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
