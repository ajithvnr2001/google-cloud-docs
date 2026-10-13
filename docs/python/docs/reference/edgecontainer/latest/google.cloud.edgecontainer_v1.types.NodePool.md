---
url: https://docs.cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.types.NodePool
title: Class NodePool (0.8.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:46:38.445363+00:00
---

# Class NodePool (0.8.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.types.NodePool

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class NodePool (0.8.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.8.2 (latest)  0.8.1  0.7.0  0.6.0  0.5.18  0.4.1  0.3.0  0.2.1  0.1.0 
    
    
    NodePool(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A set of Kubernetes nodes in a cluster with common configuration and specification.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Required. The resource name of the node pool.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The time when the node pool was created.   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The time when the node pool was last updated.   
`labels` |  `MutableMapping[str, str]`   
Labels associated with this resource.   
`node_location` |  `str`   
Name of the Google Distributed Cloud Edge zone where this node pool will be created. For example: `us-central1-edge-customer-a`.   
`node_count` |  `int`   
Required. The number of nodes in the pool.   
`machine_filter` |  `str`   
Only machines matching this filter will be allowed to join the node pool. The filtering language accepts strings like "name=", and is documented in more detail in `AIP-160 `__.   
`local_disk_encryption` |  `[google.cloud.edgecontainer_v1.types.NodePool.LocalDiskEncryption](https://docs.cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.types.NodePool.LocalDiskEncryption)`   
Optional. Local disk encryption options. This field is only used when enabling CMEK support.   
`node_version` |  `str`   
Output only. The lowest release version among all worker nodes.   
`node_config` |  `[google.cloud.edgecontainer_v1.types.NodePool.NodeConfig](https://docs.cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.types.NodePool.NodeConfig)`   
Optional. Configuration for each node in the NodePool   
  
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
  
### LocalDiskEncryption
    
    
    LocalDiskEncryption(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Configuration for CMEK support for edge machine local disk encryption.

### NodeConfig
    
    
    NodeConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Configuration for each node in the NodePool

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
