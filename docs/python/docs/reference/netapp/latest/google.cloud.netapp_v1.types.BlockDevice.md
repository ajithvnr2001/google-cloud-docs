---
url: https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.BlockDevice
title: Class BlockDevice (0.10.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:28:14.803600+00:00
---

# Class BlockDevice (0.10.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.BlockDevice

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class BlockDevice (0.10.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.2 (latest)  0.10.1  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.24  0.2.0  0.1.0 
    
    
    BlockDevice(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Block device represents the device(s) which are stored in the block volume.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Optional. User-defined name for the block device, unique within the volume. In case no user input is provided, name will be auto-generated in the backend. The name must meet the following requirements: \- Be between 1 and 255 characters long. \- Contain only uppercase or lowercase letters (A-Z, a-z), numbers (0-9), and the following special characters: "-", "\\_", "}", "{", ".". \- Spaces are not allowed. This field is a member of `oneof`_ `_name`.   
`host_groups` |  `MutableSequence[str]`   
Optional. A list of host groups that identify hosts that can mount the block volume. Format: `projects/{project_id}/locations/{location}/hostGroups/{host_group_id}` This field can be updated after the block device is created.   
`identifier` |  `str`   
Output only. Device identifier of the block volume. This represents `lun_serial_number` for iSCSI volumes.   
`size_gib` |  `int`   
Optional. The size of the block device in GiB. Any value provided for the `size_gib` field during volume creation is ignored. The block device's size is system-managed and will be set to match the parent Volume's `capacity_gib`. This field is a member of `oneof`_ `_size_gib`.   
`os_type` |  `[google.cloud.netapp_v1.types.OsType](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.OsType)`   
Required. Immutable. The OS type of the volume. This field can't be changed after the block device is created.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
