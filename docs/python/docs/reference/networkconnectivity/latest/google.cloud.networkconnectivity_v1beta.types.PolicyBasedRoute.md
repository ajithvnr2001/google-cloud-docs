---
url: https://docs.cloud.google.com/python/docs/reference/networkconnectivity/latest/google.cloud.networkconnectivity_v1beta.types.PolicyBasedRoute
title: Class PolicyBasedRoute (2.18.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:23:29.468812+00:00
---

# Class PolicyBasedRoute (2.18.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/networkconnectivity/latest/google.cloud.networkconnectivity_v1beta.types.PolicyBasedRoute

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class PolicyBasedRoute (2.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.18.0 (latest)  2.17.0  2.16.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.1  2.7.1  2.6.0  2.5.1  2.4.5  2.3.0  2.2.0  2.0.2  1.6.1  1.5.0  1.4.4  1.3.2  1.2.2  1.1.0  1.0.1  0.6.3  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    PolicyBasedRoute(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Policy-based routes route L4 network traffic based on not just destination IP address, but also source IP address, protocol, and more. If a policy-based route conflicts with other types of routes, the policy-based route always takes precedence.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`virtual_machine` |  `[google.cloud.networkconnectivity_v1beta.types.PolicyBasedRoute.VirtualMachine](https://docs.cloud.google.com/python/docs/reference/networkconnectivity/latest/google.cloud.networkconnectivity_v1beta.types.PolicyBasedRoute.VirtualMachine)`   
Optional. VM instances that this policy-based route applies to. This field is a member of `oneof`_ `target`.   
`interconnect_attachment` |  `[google.cloud.networkconnectivity_v1beta.types.PolicyBasedRoute.InterconnectAttachment](https://docs.cloud.google.com/python/docs/reference/networkconnectivity/latest/google.cloud.networkconnectivity_v1beta.types.PolicyBasedRoute.InterconnectAttachment)`   
Optional. The interconnect attachments that this policy-based route applies to. This field is a member of `oneof`_ `target`.   
`next_hop_ilb_ip` |  `str`   
Optional. The IP address of a global-access-enabled L4 ILB that is the next hop for matching packets. For this version, only nextHopIlbIp is supported. This field is a member of `oneof`_ `next_hop`.   
`next_hop_other_routes` |  `[google.cloud.networkconnectivity_v1beta.types.PolicyBasedRoute.OtherRoutes](https://docs.cloud.google.com/python/docs/reference/networkconnectivity/latest/google.cloud.networkconnectivity_v1beta.types.PolicyBasedRoute.OtherRoutes)`   
Optional. Other routes that will be referenced to determine the next hop of the packet. This field is a member of `oneof`_ `next_hop`.   
`name` |  `str`   
Immutable. Identifier. A unique name of the resource in the form of `projects/{project_number}/locations/global/PolicyBasedRoutes/{policy_based_route_id}`  
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Time when the policy-based route was created.   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Time when the policy-based route was updated.   
`labels` |  `MutableMapping[str, str]`   
User-defined labels.   
`description` |  `str`   
Optional. An optional description of this resource. Provide this field when you create the resource.   
`network` |  `str`   
Required. Fully-qualified URL of the network that this route applies to, for example: projects/my-project/global/networks/my-network.   
`filter` |  `[google.cloud.networkconnectivity_v1beta.types.PolicyBasedRoute.Filter](https://docs.cloud.google.com/python/docs/reference/networkconnectivity/latest/google.cloud.networkconnectivity_v1beta.types.PolicyBasedRoute.Filter)`   
Required. The filter to match L4 traffic.   
`priority` |  `int`   
Optional. The priority of this policy-based route. Priority is used to break ties in cases where there are more than one matching policy-based routes found. In cases where multiple policy-based routes are matched, the one with the lowest-numbered priority value wins. The default value is 1000\. The priority value must be from 1 to 65535, inclusive.   
`warnings` |  `MutableSequence[[google.cloud.networkconnectivity_v1beta.types.PolicyBasedRoute.Warnings](https://docs.cloud.google.com/python/docs/reference/networkconnectivity/latest/google.cloud.networkconnectivity_v1beta.types.PolicyBasedRoute.Warnings)]`   
Output only. If potential misconfigurations are detected for this route, this field will be populated with warning messages.   
`self_link` |  `str`   
Output only. Server-defined fully-qualified URL for this resource.   
`kind` |  `str`   
Output only. Type of this resource. Always networkconnectivity#policyBasedRoute for policy-based Route resources.   
  
## Classes 

### Filter
    
    
    Filter(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Filter matches L4 traffic.

### InterconnectAttachment
    
    
    InterconnectAttachment(mapping=None, *, ignore_unknown_fields=False, **kwargs)

InterconnectAttachment that this route applies to.

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
  
### OtherRoutes
    
    
    OtherRoutes(value)

The other routing cases.

### VirtualMachine
    
    
    VirtualMachine(mapping=None, *, ignore_unknown_fields=False, **kwargs)

VM instances that this policy-based route applies to.

### Warnings
    
    
    Warnings(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Informational warning message.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
