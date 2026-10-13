---
url: https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DiskRestoreProperties
title: Class DiskRestoreProperties (0.10.3) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:17:57.149741+00:00
---

# Class DiskRestoreProperties (0.10.3)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DiskRestoreProperties

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class DiskRestoreProperties (0.10.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.3 (latest)  0.10.2  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.5  0.1.7 
    
    
    DiskRestoreProperties(mapping=None, *, ignore_unknown_fields=False, **kwargs)

DiskRestoreProperties represents the properties of a Disk restore.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Required. Name of the disk. This field is a member of `oneof`_ `_name`.   
`description` |  `str`   
Optional. An optional description of this resource. Provide this property when you create the resource. This field is a member of `oneof`_ `_description`.   
`size_gb` |  `int`   
Required. The size of the disk in GB. This field is a member of `oneof`_ `_size_gb`.   
`licenses` |  `MutableSequence[str]`   
Optional. A list of publicly available licenses that are applicable to this backup. This is applicable if the original image had licenses attached, e.g. Windows image   
`guest_os_feature` |  `MutableSequence[[google.cloud.backupdr_v1.types.GuestOsFeature](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.GuestOsFeature)]`   
Optional. A list of features to enable in the guest operating system. This is applicable only for bootable images.   
`disk_encryption_key` |  `[google.cloud.backupdr_v1.types.CustomerEncryptionKey](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.CustomerEncryptionKey)`   
Optional. Encrypts the disk using a customer-supplied encryption key or a customer-managed encryption key. This field is a member of `oneof`_ `_disk_encryption_key`.   
`physical_block_size_bytes` |  `int`   
Optional. Physical block size of the persistent disk, in bytes. If not present in a request, a default value is used. Currently, the supported size is 4096. This field is a member of `oneof`_ `_physical_block_size_bytes`.   
`provisioned_iops` |  `int`   
Optional. Indicates how many IOPS to provision for the disk. This sets the number of I/O operations per second that the disk can handle. This field is a member of `oneof`_ `_provisioned_iops`.   
`provisioned_throughput` |  `int`   
Optional. Indicates how much throughput to provision for the disk. This sets the number of throughput MB per second that the disk can handle. This field is a member of `oneof`_ `_provisioned_throughput`.   
`enable_confidential_compute` |  `bool`   
Optional. Indicates whether this disk is using confidential compute mode. Encryption with a Cloud KMS key is required to enable this option. This field is a member of `oneof`_ `_enable_confidential_compute`.   
`storage_pool` |  `str`   
Optional. The storage pool in which the new disk is created. You can provide this as a partial or full URL to the resource. This field is a member of `oneof`_ `_storage_pool`.   
`access_mode` |  `[google.cloud.backupdr_v1.types.DiskRestoreProperties.AccessMode](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DiskRestoreProperties.AccessMode)`   
Optional. The access mode of the disk. This field is a member of `oneof`_ `_access_mode`.   
`architecture` |  `[google.cloud.backupdr_v1.types.DiskRestoreProperties.Architecture](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DiskRestoreProperties.Architecture)`   
Optional. The architecture of the source disk. Valid values are ARM64 or X86_64. This field is a member of `oneof`_ `_architecture`.   
`resource_policy` |  `MutableSequence[str]`   
Optional. Resource policies applied to this disk.   
`type_` |  `str`   
Required. URL of the disk type resource describing which disk type to use to create the disk. This field is a member of `oneof`_ `_type`.   
`labels` |  `MutableMapping[str, str]`   
Optional. Labels to apply to this disk. These can be modified later using `setLabels` method. Label values can be empty.   
`resource_manager_tags` |  `MutableMapping[str, str]`   
Optional. Resource manager tags to be bound to the disk.   
  
## Classes 

### AccessMode
    
    
    AccessMode(value)

The supported access modes of the disk.

### Architecture
    
    
    Architecture(value)

Architecture of the source disk.

### LabelsEntry
    
    
    LabelsEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The abstract base class for a message.

**Parameters**  
---  
**Name** | **Description**  
`kwargs` |  `dict`   
Keys and values corresponding to the fields of the message.  
`mapping` |  `Union[dict, `.Message`]`   
A dictionary or message to be used to determine the values for this message.  
`ignore_unknown_fields` |  `Optional(bool)`   
If True, do not raise errors for unknown fields. Only applied if `mapping` is a mapping type or there are keyword parameters.  
  
### ResourceManagerTagsEntry
    
    
    ResourceManagerTagsEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The abstract base class for a message.

**Parameters**  
---  
**Name** | **Description**  
`kwargs` |  `dict`   
Keys and values corresponding to the fields of the message.  
`mapping` |  `Union[dict, `.Message`]`   
A dictionary or message to be used to determine the values for this message.  
`ignore_unknown_fields` |  `Optional(bool)`   
If True, do not raise errors for unknown fields. Only applied if `mapping` is a mapping type or there are keyword parameters.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
