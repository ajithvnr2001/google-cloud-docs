---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.types.EdgeSlm
title: Class EdgeSlm (0.5.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:13:26.229923+00:00
---

# Class EdgeSlm (0.5.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.types.EdgeSlm

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class EdgeSlm (0.5.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.2 (latest)  0.5.1  0.4.0  0.3.0  0.2.11  0.1.2 
    
    
    EdgeSlm(mapping=None, *, ignore_unknown_fields=False, **kwargs)

EdgeSlm represents an SLM instance which manages the lifecycle of edge components installed on Workload clusters managed by an Orchestration Cluster.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Name of the EdgeSlm resource.   
`orchestration_cluster` |  `str`   
Immutable. Reference to the orchestration cluster on which templates for this resources will be applied. This should be of format projects/{project}/locations/{location}/orchestrationClusters/{orchestration_cluster}.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. [Output only] Create time stamp.   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. [Output only] Update time stamp.   
`labels` |  `MutableMapping[str, str]`   
Optional. Labels as key value pairs. The key and value should contain characters which are UTF-8 compliant and less than 50 characters.   
`tna_version` |  `str`   
Output only. Provides the active TNA version for this resource.   
`state` |  `[google.cloud.telcoautomation_v1alpha1.types.EdgeSlm.State](https://docs.cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.types.EdgeSlm.State)`   
Output only. State of the EdgeSlm resource.   
`workload_cluster_type` |  `[google.cloud.telcoautomation_v1alpha1.types.EdgeSlm.WorkloadClusterType](https://docs.cloud.google.com/python/docs/reference/google-cloud-telcoautomation/latest/google.cloud.telcoautomation_v1alpha1.types.EdgeSlm.WorkloadClusterType)`   
Optional. Type of workload cluster for which an EdgeSLM resource is created.   
  
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

Possible states of the resource.

### WorkloadClusterType
    
    
    WorkloadClusterType(value)

Workload clusters supported by TNA. New values will be added to the enum list as TNA adds supports for new workload clusters in future.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
