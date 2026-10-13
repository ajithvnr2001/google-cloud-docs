---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-batch-v1/latest/Google-Cloud-Batch-V1-AllocationPolicy-Disk/
title: Batch V1 API - Class Google::Cloud::Batch::V1::AllocationPolicy::Disk (v1.9.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:51:28.402709+00:00
---

# Batch V1 API - Class Google::Cloud::Batch::V1::AllocationPolicy::Disk (v1.9.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-batch-v1/latest/Google-Cloud-Batch-V1-AllocationPolicy-Disk/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Batch V1 API - Class Google::Cloud::Batch::V1::AllocationPolicy::Disk (v1.9.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.9.0 (latest)  1.8.2  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.1  1.0.0  0.21.0  0.20.1  0.19.2  0.18.3  0.17.4  0.16.2  0.15.1  0.14.0  0.13.1  0.12.0  0.11.1  0.10.5  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.3  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Batch V1 API class Google::Cloud::Batch::V1::AllocationPolicy::Disk.

A new persistent disk or a local ssd. A VM can only have one local SSD setting but multiple local SSD partitions. See <https://cloud.google.com/compute/docs/disks#pdspecs> and <https://cloud.google.com/compute/docs/disks#localssds>.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #disk_interface
    
    
    def disk_interface() -> ::String

**Returns**

  * (::String) — Local SSDs are available through both "SCSI" and "NVMe" interfaces. If not indicated, "NVMe" will be the default one for local ssds. This field is ignored for persistent disks as the interface is chosen automatically. See https://cloud.google.com/compute/docs/disks/persistent-disks#choose_an_interface. 



### #disk_interface=
    
    
    def disk_interface=(value) -> ::String

**Parameter**

  * **value** (::String) — Local SSDs are available through both "SCSI" and "NVMe" interfaces. If not indicated, "NVMe" will be the default one for local ssds. This field is ignored for persistent disks as the interface is chosen automatically. See https://cloud.google.com/compute/docs/disks/persistent-disks#choose_an_interface. 



**Returns**

  * (::String) — Local SSDs are available through both "SCSI" and "NVMe" interfaces. If not indicated, "NVMe" will be the default one for local ssds. This field is ignored for persistent disks as the interface is chosen automatically. See https://cloud.google.com/compute/docs/disks/persistent-disks#choose_an_interface. 



### #image
    
    
    def image() -> ::String

**Returns**

  * (::String) — URL for a VM image to use as the data source for this disk. For example, the following are all valid URLs:

    * Specify the image by its family name: projects/{project}/global/images/family/{image_family}
    * Specify the image version: projects/{project}/global/images/{image_version}

You can also use Batch customized image in short names. The following image values are supported for a boot disk:

    * `batch-debian`: use Batch Debian images.
    * `batch-cos`: use Batch Container-Optimized images.
    * `batch-hpc-rocky`: use Batch HPC Rocky Linux images.

Note: The following fields are mutually exclusive: `image`, `snapshot`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #image=
    
    
    def image=(value) -> ::String

**Parameter**

  * **value** (::String) — URL for a VM image to use as the data source for this disk. For example, the following are all valid URLs:

    * Specify the image by its family name: projects/{project}/global/images/family/{image_family}
    * Specify the image version: projects/{project}/global/images/{image_version}

You can also use Batch customized image in short names. The following image values are supported for a boot disk:

    * `batch-debian`: use Batch Debian images.
    * `batch-cos`: use Batch Container-Optimized images.
    * `batch-hpc-rocky`: use Batch HPC Rocky Linux images.

Note: The following fields are mutually exclusive: `image`, `snapshot`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::String) — URL for a VM image to use as the data source for this disk. For example, the following are all valid URLs:

    * Specify the image by its family name: projects/{project}/global/images/family/{image_family}
    * Specify the image version: projects/{project}/global/images/{image_version}

You can also use Batch customized image in short names. The following image values are supported for a boot disk:

    * `batch-debian`: use Batch Debian images.
    * `batch-cos`: use Batch Container-Optimized images.
    * `batch-hpc-rocky`: use Batch HPC Rocky Linux images.

Note: The following fields are mutually exclusive: `image`, `snapshot`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #size_gb
    
    
    def size_gb() -> ::Integer

**Returns**

  * (::Integer) — Disk size in GB.

**Non-Boot Disk** : If the `type` specifies a persistent disk, this field is ignored if `data_source` is set as `image` or `snapshot`. If the `type` specifies a local SSD, this field should be a multiple of 375 GB, otherwise, the final size will be the next greater multiple of 375 GB.

**Boot Disk** : Batch will calculate the boot disk size based on source image and task requirements if you do not speicify the size. If both this field and the `boot_disk_mib` field in task spec's `compute_resource` are defined, Batch will only honor this field. Also, this field should be no smaller than the source disk's size when the `data_source` is set as `snapshot` or `image`. For example, if you set an image as the `data_source` field and the image's default disk size 30 GB, you can only use this field to make the disk larger or equal to 30 GB. 




### #size_gb=
    
    
    def size_gb=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Disk size in GB.

**Non-Boot Disk** : If the `type` specifies a persistent disk, this field is ignored if `data_source` is set as `image` or `snapshot`. If the `type` specifies a local SSD, this field should be a multiple of 375 GB, otherwise, the final size will be the next greater multiple of 375 GB.

**Boot Disk** : Batch will calculate the boot disk size based on source image and task requirements if you do not speicify the size. If both this field and the `boot_disk_mib` field in task spec's `compute_resource` are defined, Batch will only honor this field. Also, this field should be no smaller than the source disk's size when the `data_source` is set as `snapshot` or `image`. For example, if you set an image as the `data_source` field and the image's default disk size 30 GB, you can only use this field to make the disk larger or equal to 30 GB. 




**Returns**

  * (::Integer) — Disk size in GB.

**Non-Boot Disk** : If the `type` specifies a persistent disk, this field is ignored if `data_source` is set as `image` or `snapshot`. If the `type` specifies a local SSD, this field should be a multiple of 375 GB, otherwise, the final size will be the next greater multiple of 375 GB.

**Boot Disk** : Batch will calculate the boot disk size based on source image and task requirements if you do not speicify the size. If both this field and the `boot_disk_mib` field in task spec's `compute_resource` are defined, Batch will only honor this field. Also, this field should be no smaller than the source disk's size when the `data_source` is set as `snapshot` or `image`. For example, if you set an image as the `data_source` field and the image's default disk size 30 GB, you can only use this field to make the disk larger or equal to 30 GB. 




### #snapshot
    
    
    def snapshot() -> ::String

**Returns**

  * (::String) — Name of a snapshot used as the data source. Snapshot is not supported as boot disk now.

Note: The following fields are mutually exclusive: `snapshot`, `image`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #snapshot=
    
    
    def snapshot=(value) -> ::String

**Parameter**

  * **value** (::String) — Name of a snapshot used as the data source. Snapshot is not supported as boot disk now.

Note: The following fields are mutually exclusive: `snapshot`, `image`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::String) — Name of a snapshot used as the data source. Snapshot is not supported as boot disk now.

Note: The following fields are mutually exclusive: `snapshot`, `image`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #type
    
    
    def type() -> ::String

**Returns**

  * (::String) — Disk type as shown in `gcloud compute disk-types list`. For example, local SSD uses type "local-ssd". Persistent disks and boot disks use "pd-balanced", "pd-extreme", "pd-ssd" or "pd-standard". If not specified, "pd-standard" will be used as the default type for non-boot disks, "pd-balanced" will be used as the default type for boot disks. 



### #type=
    
    
    def type=(value) -> ::String

**Parameter**

  * **value** (::String) — Disk type as shown in `gcloud compute disk-types list`. For example, local SSD uses type "local-ssd". Persistent disks and boot disks use "pd-balanced", "pd-extreme", "pd-ssd" or "pd-standard". If not specified, "pd-standard" will be used as the default type for non-boot disks, "pd-balanced" will be used as the default type for boot disks. 



**Returns**

  * (::String) — Disk type as shown in `gcloud compute disk-types list`. For example, local SSD uses type "local-ssd". Persistent disks and boot disks use "pd-balanced", "pd-extreme", "pd-ssd" or "pd-standard". If not specified, "pd-standard" will be used as the default type for non-boot disks, "pd-balanced" will be used as the default type for boot disks. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
