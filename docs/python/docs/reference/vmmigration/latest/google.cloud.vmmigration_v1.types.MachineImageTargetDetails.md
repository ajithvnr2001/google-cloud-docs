---
url: https://docs.cloud.google.com/python/docs/reference/vmmigration/latest/google.cloud.vmmigration_v1.types.MachineImageTargetDetails
title: Class MachineImageTargetDetails (1.18.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:57:20.876717+00:00
---

# Class MachineImageTargetDetails (1.18.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/vmmigration/latest/google.cloud.vmmigration_v1.types.MachineImageTargetDetails

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class MachineImageTargetDetails (1.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.18.0 (latest)  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.3  1.10.0  1.9.1  1.8.5  1.7.0  1.6.2  1.5.1  1.4.0  1.3.3  1.2.0  1.1.2  1.0.0  0.1.0 
    
    
    MachineImageTargetDetails(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The target details of the machine image resource that will be created by the image import job.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`os_adaptation_parameters` |  `[google.cloud.vmmigration_v1.types.ImageImportOsAdaptationParameters](https://docs.cloud.google.com/python/docs/reference/vmmigration/latest/google.cloud.vmmigration_v1.types.ImageImportOsAdaptationParameters)`   
Optional. Use to set the parameters relevant for the OS adaptation process. This field is a member of `oneof`_ `os_adaptation_config`.   
`skip_os_adaptation` |  `[google.cloud.vmmigration_v1.types.SkipOsAdaptation](https://docs.cloud.google.com/python/docs/reference/vmmigration/latest/google.cloud.vmmigration_v1.types.SkipOsAdaptation)`   
Optional. Use to skip OS adaptation process. This field is a member of `oneof`_ `os_adaptation_config`.   
`machine_image_name` |  `str`   
Required. The name of the machine image to be created.   
`target_project` |  `str`   
Required. Reference to the TargetProject resource that represents the target project in which the imported machine image will be created.   
`description` |  `str`   
Optional. An optional description of the machine image.   
`single_region_storage` |  `bool`   
Optional. Set to true to set the machine image storageLocations to the single region of the import job. When false, the closest multi-region is selected.   
`encryption` |  `[google.cloud.vmmigration_v1.types.Encryption](https://docs.cloud.google.com/python/docs/reference/vmmigration/latest/google.cloud.vmmigration_v1.types.Encryption)`   
Immutable. The encryption to apply to the machine image. If the Image Import resource has an encryption, this field must be set to the same encryption key.   
`machine_image_parameters_overrides` |  `[google.cloud.vmmigration_v1.types.MachineImageParametersOverrides](https://docs.cloud.google.com/python/docs/reference/vmmigration/latest/google.cloud.vmmigration_v1.types.MachineImageParametersOverrides)`   
Optional. Parameters overriding decisions based on the source machine image configurations.   
`service_account` |  `[google.cloud.vmmigration_v1.types.ServiceAccount](https://docs.cloud.google.com/python/docs/reference/vmmigration/latest/google.cloud.vmmigration_v1.types.ServiceAccount)`   
Optional. The service account to assign to the instance created by the machine image.   
`additional_licenses` |  `MutableSequence[str]`   
Optional. Additional licenses to assign to the instance created by the machine image. Format: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/licenses/LICENSE_NAME Or https://www.googleapis.com/compute/beta/projects/PROJECT_ID/global/licenses/LICENSE_NAME   
`labels` |  `MutableMapping[str, str]`   
Optional. The labels to apply to the instance created by the machine image.   
`tags` |  `MutableSequence[str]`   
Optional. The tags to apply to the instance created by the machine image.   
`shielded_instance_config` |  `[google.cloud.vmmigration_v1.types.ShieldedInstanceConfig](https://docs.cloud.google.com/python/docs/reference/vmmigration/latest/google.cloud.vmmigration_v1.types.ShieldedInstanceConfig)`   
Optional. Shielded instance configuration.   
`network_interfaces` |  `MutableSequence[[google.cloud.vmmigration_v1.types.NetworkInterface](https://docs.cloud.google.com/python/docs/reference/vmmigration/latest/google.cloud.vmmigration_v1.types.NetworkInterface)]`   
Optional. The network interfaces to create with the instance created by the machine image. Internal and external IP addresses, and network tiers are ignored for machine image import.   
  
## Classes 

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
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
