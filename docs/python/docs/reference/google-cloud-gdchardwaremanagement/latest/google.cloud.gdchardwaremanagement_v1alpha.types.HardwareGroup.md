---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.HardwareGroup
title: Class HardwareGroup (0.5.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:16:45.312985+00:00
---

# Class HardwareGroup (0.5.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.HardwareGroup

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class HardwareGroup (0.5.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.2 (latest)  0.5.1  0.3.0  0.2.0  0.1.13 
    
    
    HardwareGroup(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A group of hardware that is part of the same order, has the same SKU, and is delivered to the same site.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Identifier. Name of this hardware group. Format: `projects/{project}/locations/{location}/orders/{order}/hardwareGroups/{hardware_group}`  
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Time when this hardware group was created.   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Time when this hardware group was last updated.   
`labels` |  `MutableMapping[str, str]`   
Optional. Labels associated with this hardware group as key value pairs. For more information about labels, see `Create and manage labels   
`hardware_count` |  `int`   
Required. Number of hardware in this HardwareGroup.   
`config` |  `[google.cloud.gdchardwaremanagement_v1alpha.types.HardwareConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.HardwareConfig)`   
Required. Configuration for hardware in this HardwareGroup.   
`site` |  `str`   
Required. Name of the site where the hardware in this HardwareGroup will be delivered. Format: `projects/{project}/locations/{location}/sites/{site}`  
`state` |  `[google.cloud.gdchardwaremanagement_v1alpha.types.HardwareGroup.State](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.HardwareGroup.State)`   
Output only. Current state of this HardwareGroup.   
`zone` |  `str`   
Optional. Name of the zone that the hardware in this HardwareGroup belongs to. Format: `projects/{project}/locations/{location}/zones/{zone}`  
`requested_installation_date` |  `google.type.date_pb2.Date`   
Deprecated: This value is not used. Use the requested_installation_date field in the Order resource instead.   
  
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
  
### State
    
    
    State(value)

Valid states of a HardwareGroup.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
