---
url: https://docs.cloud.google.com/python/docs/reference/networkconnectivity/latest/google.cloud.networkconnectivity_v1alpha1.types.Spoke
title: Class Spoke (2.18.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:18:24.021596+00:00
---

# Class Spoke (2.18.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/networkconnectivity/latest/google.cloud.networkconnectivity_v1alpha1.types.Spoke

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Spoke (2.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.18.0 (latest)  2.17.0  2.16.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.1  2.7.1  2.6.0  2.5.1  2.4.5  2.3.0  2.2.0  2.0.2  1.6.1  1.5.0  1.4.4  1.3.2  1.2.2  1.1.0  1.0.1  0.6.3  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    Spoke(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A Spoke is an abstraction of a network attachment being attached to a Hub. A Spoke can be underlying a VPN tunnel, a VLAN (interconnect) attachment, a Router appliance, etc.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Immutable. The name of a Spoke resource.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
The time when the Spoke was created.   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
The time when the Spoke was updated.   
`labels` |  `MutableMapping[str, str]`   
User-defined labels.   
`description` |  `str`   
Short description of the spoke resource   
`hub` |  `str`   
The resource URL of the hub resource that the spoke is attached to   
`linked_vpn_tunnels` |  `MutableSequence[str]`   
The URIs of linked VPN tunnel resources   
`linked_interconnect_attachments` |  `MutableSequence[str]`   
The URIs of linked interconnect attachment resources   
`linked_router_appliance_instances` |  `MutableSequence[[google.cloud.networkconnectivity_v1alpha1.types.RouterApplianceInstance](https://docs.cloud.google.com/python/docs/reference/networkconnectivity/latest/google.cloud.networkconnectivity_v1alpha1.types.RouterApplianceInstance)]`   
The URIs of linked Router appliance resources   
`unique_id` |  `str`   
Output only. Google-generated UUID for this resource. This is unique across all Spoke resources. If a Spoke resource is deleted and another with the same name is created, it gets a different unique_id.   
`state` |  `[google.cloud.networkconnectivity_v1alpha1.types.State](https://docs.cloud.google.com/python/docs/reference/networkconnectivity/latest/google.cloud.networkconnectivity_v1alpha1.types.State)`   
Output only. The current lifecycle state of this Hub.   
  
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
