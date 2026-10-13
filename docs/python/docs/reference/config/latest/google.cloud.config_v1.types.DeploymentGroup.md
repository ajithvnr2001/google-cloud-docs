---
url: https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.DeploymentGroup
title: Class DeploymentGroup (0.7.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:12:39.061130+00:00
---

# Class DeploymentGroup (0.7.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.DeploymentGroup

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class DeploymentGroup (0.7.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.2 (latest)  0.7.1  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.21 
    
    
    DeploymentGroup(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A DeploymentGroup is a collection of DeploymentUnits that in a DAG-like structure.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Identifier. The name of the deployment group. Format: 'projects/{project_id}/locations/{location}/deploymentGroups/{deployment_group}'.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Time when the deployment group was created.   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Time when the deployment group was last updated.   
`labels` |  `MutableMapping[str, str]`   
Optional. User-defined metadata for the deployment group.   
`annotations` |  `MutableMapping[str, str]`   
Optional. Arbitrary key-value metadata storage e.g. to help client tools identify deployment group during automation. See https://google.aip.dev/148#annotations for details on format and size limitations.   
`state` |  `[google.cloud.config_v1.types.DeploymentGroup.State](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.DeploymentGroup.State)`   
Output only. Current state of the deployment group.   
`state_description` |  `str`   
Output only. Additional information regarding the current state.   
`deployment_units` |  `MutableSequence[[google.cloud.config_v1.types.DeploymentUnit](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.DeploymentUnit)]`   
The deployment units of the deployment group in a DAG like structure. When a deployment group is being provisioned, the deployment units are deployed in a DAG order. The provided units must be in a DAG order, otherwise an error will be returned.   
`provisioning_state` |  `[google.cloud.config_v1.types.DeploymentGroup.ProvisioningState](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.DeploymentGroup.ProvisioningState)`   
Output only. The provisioning state of the deployment group.   
`provisioning_state_description` |  `str`   
Output only. Additional information regarding the current provisioning state.   
`provisioning_error` |  `google.rpc.status_pb2.Status`   
Output only. The error status of the deployment group provisioning or deprovisioning.   
  
## Classes 

### AnnotationsEntry
    
    
    AnnotationsEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

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
  
### ProvisioningState
    
    
    ProvisioningState(value)

Possible provisioning states of a deployment group.

### State
    
    
    State(value)

Possible states of a deployment group.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
