---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.NodeTemplate
title: Class NodeTemplate (0.12.7) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:14:55.000114+00:00
---

# Class NodeTemplate (0.12.7)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.NodeTemplate

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class NodeTemplate (0.12.7) Stay organized with collections  Save and categorize content based on your preferences. 

0.12.7 (latest)  0.12.6  0.11.0  0.4.0  0.3.0  0.2.0  0.1.8 
    
    
    NodeTemplate(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Represent a sole-tenant Node Template resource.

You can use a template to define properties for nodes in a node group. For more information, readCreating node groups and instances.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`cpu_overcommit_type` |  `str`   
CPU overcommit. Check the CpuOvercommitType enum for the list of possible values. This field is a member of `oneof`_ `_cpu_overcommit_type`.   
`creation_timestamp` |  `str`   
Output only. [Output Only] Creation timestamp inRFC3339 text format. This field is a member of `oneof`_ `_creation_timestamp`.   
`description` |  `str`   
An optional description of this resource. Provide this property when you create the resource. This field is a member of `oneof`_ `_description`.   
`id` |  `int`   
Output only. [Output Only] The unique identifier for the resource. This identifier is defined by the server. This field is a member of `oneof`_ `_id`.   
`kind` |  `str`   
Output only. [Output Only] The type of the resource. Alwayscompute#nodeTemplate for node templates. This field is a member of `oneof`_ `_kind`.   
`name` |  `str`   
The name of the resource, provided by the client when initially creating the resource. The resource name must be 1-63 characters long, and comply withRFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. This field is a member of `oneof`_ `_name`.   
`node_affinity_labels` |  `MutableMapping[str, str]`   
Labels to use for node affinity, which will be used in instance scheduling.   
`node_type` |  `str`   
The node type to use for nodes group that are created from this template. This field is a member of `oneof`_ `_node_type`.   
`node_type_flexibility` |  `[google.cloud.compute_v1beta.types.NodeTemplateNodeTypeFlexibility](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.NodeTemplateNodeTypeFlexibility)`   
Do not use. Instead, use the node_type property. This field is a member of `oneof`_ `_node_type_flexibility`.   
`region` |  `str`   
Output only. [Output Only] The name of the region where the node template resides, such as us-central1. This field is a member of `oneof`_ `_region`.   
`self_link` |  `str`   
Output only. [Output Only] Server-defined URL for the resource. This field is a member of `oneof`_ `_self_link`.   
`server_binding` |  `[google.cloud.compute_v1beta.types.ServerBinding](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.ServerBinding)`   
Sets the binding properties for the physical server. Valid values include: :: \- *[Default]* RESTART_NODE_ON_ANY_SERVER: Restarts VMs on any available physical server \- RESTART_NODE_ON_MINIMAL_SERVER: Restarts VMs on the same physical server whenever possible See Sole-tenant node options for more information. This field is a member of `oneof`_ `_server_binding`.   
`status` |  `str`   
Output only. [Output Only] The status of the node template. One of the following values:CREATING, READY, and DELETING. Check the Status enum for the list of possible values. This field is a member of `oneof`_ `_status`.   
`status_message` |  `str`   
Output only. [Output Only] An optional, human-readable explanation of the status. This field is a member of `oneof`_ `_status_message`.   
  
## Classes 

### CpuOvercommitType
    
    
    CpuOvercommitType(value)

CPU overcommit.

### NodeAffinityLabelsEntry
    
    
    NodeAffinityLabelsEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

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
  
### Status
    
    
    Status(value)

Output only. [Output Only] The status of the node template. One of the following values:CREATING, READY, and DELETING.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
