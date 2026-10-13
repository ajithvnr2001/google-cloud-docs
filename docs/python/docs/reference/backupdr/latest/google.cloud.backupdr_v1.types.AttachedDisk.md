---
url: https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.AttachedDisk
title: Class AttachedDisk (0.10.3) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:17:46.174802+00:00
---

# Class AttachedDisk (0.10.3)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.AttachedDisk

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class AttachedDisk (0.10.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.3 (latest)  0.10.2  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.5  0.1.7 
    
    
    AttachedDisk(mapping=None, *, ignore_unknown_fields=False, **kwargs)

An instance-attached disk resource.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`initialize_params` |  `[google.cloud.backupdr_v1.types.AttachedDisk.InitializeParams](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.AttachedDisk.InitializeParams)`   
Optional. Specifies the parameters to initialize this disk. This field is a member of `oneof`_ `_initialize_params`.   
`device_name` |  `str`   
Optional. This is used as an identifier for the disks. This is the unique name has to provided to modify disk parameters like disk_name and replica_zones (in case of RePDs) This field is a member of `oneof`_ `_device_name`.   
`kind` |  `str`   
Optional. Type of the resource. This field is a member of `oneof`_ `_kind`.   
`disk_type_deprecated` |  `[google.cloud.backupdr_v1.types.AttachedDisk.DiskType](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.AttachedDisk.DiskType)`   
Specifies the type of the disk. This field is a member of `oneof`_ `_disk_type_deprecated`.   
`mode` |  `[google.cloud.backupdr_v1.types.AttachedDisk.DiskMode](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.AttachedDisk.DiskMode)`   
Optional. The mode in which to attach this disk. This field is a member of `oneof`_ `_mode`.   
`source` |  `str`   
Optional. Specifies a valid partial or full URL to an existing Persistent Disk resource. This field is a member of `oneof`_ `_source`.   
`index` |  `int`   
Optional. A zero-based index to this disk, where 0 is reserved for the boot disk. This field is a member of `oneof`_ `_index`.   
`boot` |  `bool`   
Optional. Indicates that this is a boot disk. The virtual machine will use the first partition of the disk for its root filesystem. This field is a member of `oneof`_ `_boot`.   
`auto_delete` |  `bool`   
Optional. Specifies whether the disk will be auto-deleted when the instance is deleted (but not when the disk is detached from the instance). This field is a member of `oneof`_ `_auto_delete`.   
`license_` |  `MutableSequence[str]`   
Optional. Any valid publicly visible licenses.   
`disk_interface` |  `[google.cloud.backupdr_v1.types.AttachedDisk.DiskInterface](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.AttachedDisk.DiskInterface)`   
Optional. Specifies the disk interface to use for attaching this disk. This field is a member of `oneof`_ `_disk_interface`.   
`guest_os_feature` |  `MutableSequence[[google.cloud.backupdr_v1.types.GuestOsFeature](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.GuestOsFeature)]`   
Optional. A list of features to enable on the guest operating system. Applicable only for bootable images.   
`disk_encryption_key` |  `[google.cloud.backupdr_v1.types.CustomerEncryptionKey](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.CustomerEncryptionKey)`   
Optional. Encrypts or decrypts a disk using a customer-supplied encryption key. This field is a member of `oneof`_ `_disk_encryption_key`.   
`disk_size_gb` |  `int`   
Optional. The size of the disk in GB. This field is a member of `oneof`_ `_disk_size_gb`.   
`saved_state` |  `[google.cloud.backupdr_v1.types.AttachedDisk.DiskSavedState](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.AttachedDisk.DiskSavedState)`   
Optional. Output only. The state of the disk. This field is a member of `oneof`_ `_saved_state`.   
`disk_type` |  `str`   
Optional. Output only. The URI of the disk type resource. For example: projects/project/zones/zone/diskTypes/pd-standard or pd-ssd This field is a member of `oneof`_ `_disk_type`.   
`type_` |  `[google.cloud.backupdr_v1.types.AttachedDisk.DiskType](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.AttachedDisk.DiskType)`   
Optional. Specifies the type of the disk. This field is a member of `oneof`_ `_type`.   
  
## Classes 

### DiskInterface
    
    
    DiskInterface(value)

List of the Disk Interfaces.

### DiskMode
    
    
    DiskMode(value)

List of the Disk Modes.

### DiskSavedState
    
    
    DiskSavedState(value)

List of the states of the Disk.

### DiskType
    
    
    DiskType(value)

List of the Disk Types.

### InitializeParams
    
    
    InitializeParams(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Specifies the parameters to initialize this disk.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
