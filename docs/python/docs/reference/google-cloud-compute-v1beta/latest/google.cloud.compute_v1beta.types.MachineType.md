---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.MachineType
title: Class MachineType (0.12.7) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:17:47.449843+00:00
---

# Class MachineType (0.12.7)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.MachineType

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class MachineType (0.12.7) Stay organized with collections  Save and categorize content based on your preferences. 

0.12.7 (latest)  0.12.6  0.11.0  0.4.0  0.3.0  0.2.0  0.1.8 
    
    
    MachineType(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Represents a Machine Type resource.

You can use specific machine types for your VM instances based on performance and pricing requirements. For more information, readMachine Types.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`accelerators` |  `MutableSequence[[google.cloud.compute_v1beta.types.Accelerators](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.Accelerators)]`   
[Output Only] A list of accelerator configurations assigned to this machine type.   
`architecture` |  `str`   
[Output Only] The architecture of the machine type. Check the Architecture enum for the list of possible values. This field is a member of `oneof`_ `_architecture`.   
`bundled_local_ssds` |  `[google.cloud.compute_v1beta.types.BundledLocalSsds](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.BundledLocalSsds)`   
[Output Only] The configuration of bundled local SSD for the machine type. This field is a member of `oneof`_ `_bundled_local_ssds`.   
`creation_timestamp` |  `str`   
[Output Only] Creation timestamp inRFC3339 text format. This field is a member of `oneof`_ `_creation_timestamp`.   
`deprecated` |  `[google.cloud.compute_v1beta.types.DeprecationStatus](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.DeprecationStatus)`   
[Output Only] The deprecation status associated with this machine type. Only applicable if the machine type is unavailable. This field is a member of `oneof`_ `_deprecated`.   
`description` |  `str`   
[Output Only] An optional textual description of the resource. This field is a member of `oneof`_ `_description`.   
`guest_cpus` |  `int`   
[Output Only] The number of virtual CPUs that are available to the instance. This field is a member of `oneof`_ `_guest_cpus`.   
`id` |  `int`   
[Output Only] The unique identifier for the resource. This identifier is defined by the server. This field is a member of `oneof`_ `_id`.   
`image_space_gb` |  `int`   
This field is a member of `oneof`_ `_image_space_gb`.   
`is_shared_cpu` |  `bool`   
[Output Only] Whether this machine type has a shared CPU. SeeShared-core machine types for more information. This field is a member of `oneof`_ `_is_shared_cpu`.   
`kind` |  `str`   
Output only. [Output Only] The type of the resource. Alwayscompute#machineType for machine types. This field is a member of `oneof`_ `_kind`.   
`maximum_persistent_disks` |  `int`   
[Output Only] Maximum persistent disks allowed. This field is a member of `oneof`_ `_maximum_persistent_disks`.   
`maximum_persistent_disks_size_gb` |  `int`   
[Output Only] Maximum total persistent disks size (GB) allowed. This field is a member of `oneof`_ `_maximum_persistent_disks_size_gb`.   
`memory_mb` |  `int`   
[Output Only] The amount of physical memory available to the instance, defined in MB. This field is a member of `oneof`_ `_memory_mb`.   
`name` |  `str`   
[Output Only] Name of the resource. This field is a member of `oneof`_ `_name`.   
`self_link` |  `str`   
[Output Only] Server-defined URL for the resource. This field is a member of `oneof`_ `_self_link`.   
`zone` |  `str`   
[Output Only] The name of the zone where the machine type resides, such as us-central1-a. This field is a member of `oneof`_ `_zone`.   
  
## Classes 

### Architecture
    
    
    Architecture(value)

[Output Only] The architecture of the machine type.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
