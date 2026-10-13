---
url: https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.Instance.Disk
title: Class Disk (1.18.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:40:41.762800+00:00
---

# Class Disk (1.18.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.Instance.Disk

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Disk (1.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.18.0 (latest)  1.17.0  1.16.0  1.15.0  1.14.0  1.13.3  1.12.0  1.11.1  1.10.5  1.9.0  1.8.0  1.7.1  1.6.1  1.5.1  1.4.4  1.3.2  1.2.1  1.1.1  1.0.0  0.4.3  0.3.2  0.2.0  0.1.2 
    
    
    Disk(mapping=None, *, ignore_unknown_fields=False, **kwargs)

An instance-attached disk resource.

## Attributes  
  
---  
**Name** | **Description**  
`auto_delete` |  `bool`   
Indicates whether the disk will be auto-deleted when the instance is deleted (but not when the disk is detached from the instance).   
`boot` |  `bool`   
Indicates that this is a boot disk. The virtual machine will use the first partition of the disk for its root filesystem.   
`device_name` |  `str`   
Indicates a unique device name of your choice that is reflected into the `/dev/disk/by-id/google-*` tree of a Linux operating system running within the instance. This name can be used to reference the device for mounting, resizing, and so on, from within the instance. If not specified, the server chooses a default device name to apply to this disk, in the form persistent-disk-x, where x is a number assigned by Google Compute Engine.This field is only applicable for persistent disks.   
`disk_size_gb` |  `int`   
Indicates the size of the disk in base-2 GB.   
`guest_os_features` |  `MutableSequence[[google.cloud.notebooks_v1.types.Instance.Disk.GuestOsFeature](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.Instance.Disk.GuestOsFeature)]`   
Indicates a list of features to enable on the guest operating system. Applicable only for bootable images. Read Enabling guest operating system features to see a list of available options.   
`index` |  `int`   
A zero-based index to this disk, where 0 is reserved for the boot disk. If you have many disks attached to an instance, each disk would have a unique index number.   
`interface` |  `str`   
Indicates the disk interface to use for attaching this disk, which is either SCSI or NVME. The default is SCSI. Persistent disks must always use SCSI and the request will fail if you attempt to attach a persistent disk in any other format than SCSI. Local SSDs can use either NVME or SCSI. For performance characteristics of SCSI over NVMe, see Local SSD performance. Valid values: \- `NVME` \- `SCSI`  
`kind` |  `str`   
Type of the resource. Always compute#attachedDisk for attached disks.   
`licenses` |  `MutableSequence[str]`   
A list of publicly visible licenses. Reserved for Google's use. A License represents billing and aggregate usage data for public and marketplace images.   
`mode` |  `str`   
The mode in which to attach this disk, either `READ_WRITE` or `READ_ONLY`. If not specified, the default is to attach the disk in `READ_WRITE` mode. Valid values: \- `READ_ONLY` \- `READ_WRITE`  
`source` |  `str`   
Indicates a valid partial or full URL to an existing Persistent Disk resource.   
`type_` |  `str`   
Indicates the type of the disk, either `SCRATCH` or `PERSISTENT`. Valid values: \- `PERSISTENT` \- `SCRATCH`  
  
## Classes 

### GuestOsFeature
    
    
    GuestOsFeature(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Guest OS features for boot disk.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
