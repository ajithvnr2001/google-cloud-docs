---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.Hardware
title: Class Hardware (0.5.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:16:44.870802+00:00
---

# Class Hardware (0.5.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.Hardware

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Hardware (0.5.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.2 (latest)  0.5.1  0.3.0  0.2.0  0.1.13 
    
    
    Hardware(mapping=None, *, ignore_unknown_fields=False, **kwargs)

An instance of hardware installed at a site.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Identifier. Name of this hardware. Format: `projects/{project}/locations/{location}/hardware/{hardware}`  
`display_name` |  `str`   
Optional. Display name for this hardware.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Time when this hardware was created.   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Time when this hardware was last updated.   
`labels` |  `MutableMapping[str, str]`   
Optional. Labels associated with this hardware as key value pairs. For more information about labels, see `Create and manage labels   
`order` |  `str`   
Required. Name of the order that this hardware belongs to. Format: `projects/{project}/locations/{location}/orders/{order}`  
`hardware_group` |  `str`   
Output only. Name for the hardware group that this hardware belongs to. Format: `projects/{project}/locations/{location}/orders/{order}/hardwareGroups/{hardware_group}`  
`site` |  `str`   
Required. Name for the site that this hardware belongs to. Format: `projects/{project}/locations/{location}/sites/{site}`  
`state` |  `[google.cloud.gdchardwaremanagement_v1alpha.types.Hardware.State](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.Hardware.State)`   
Output only. Current state for this hardware.   
`ciq_uri` |  `str`   
Output only. Link to the Customer Intake Questionnaire (CIQ) sheet for this Hardware.   
`config` |  `[google.cloud.gdchardwaremanagement_v1alpha.types.HardwareConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.HardwareConfig)`   
Required. Configuration for this hardware.   
`estimated_installation_date` |  `google.type.date_pb2.Date`   
Output only. Estimated installation date for this hardware.   
`physical_info` |  `[google.cloud.gdchardwaremanagement_v1alpha.types.HardwarePhysicalInfo](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.HardwarePhysicalInfo)`   
Optional. Physical properties of this hardware.   
`installation_info` |  `[google.cloud.gdchardwaremanagement_v1alpha.types.HardwareInstallationInfo](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.HardwareInstallationInfo)`   
Optional. Information for installation of this hardware.   
`zone` |  `str`   
Required. Name for the zone that this hardware belongs to. Format: `projects/{project}/locations/{location}/zones/{zone}`  
`requested_installation_date` |  `google.type.date_pb2.Date`   
Optional. Requested installation date for this hardware. If not specified, this is auto-populated from the order's fulfillment_time upon submission or from the HardwareGroup's requested_installation_date upon order acceptance.   
`actual_installation_date` |  `google.type.date_pb2.Date`   
Output only. Actual installation date for this hardware. Filled in by Google.   
`machine_infos` |  `MutableSequence[[google.cloud.gdchardwaremanagement_v1alpha.types.Hardware.MachineInfo](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.Hardware.MachineInfo)]`   
Output only. Per machine asset information needed for turnup.   
`estimated_delivery_date` |  `google.type.date_pb2.Date`   
Output only. The estimated delivery date of the hardware.   
  
## Classes 

### DiskInfo
    
    
    DiskInfo(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Information about individual disks on a machine.

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
  
### MacAddress
    
    
    MacAddress(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Message to describe the MAC address of a machine.

### MachineInfo
    
    
    MachineInfo(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Information about individual machines vendors will provide during turnup.

### State
    
    
    State(value)

Valid states for hardware.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
