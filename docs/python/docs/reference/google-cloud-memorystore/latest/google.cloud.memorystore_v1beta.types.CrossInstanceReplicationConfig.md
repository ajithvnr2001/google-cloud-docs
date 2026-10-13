---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-memorystore/latest/google.cloud.memorystore_v1beta.types.CrossInstanceReplicationConfig
title: Class CrossInstanceReplicationConfig (0.5.5) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:35:41.283837+00:00
---

# Class CrossInstanceReplicationConfig (0.5.5)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-memorystore/latest/google.cloud.memorystore_v1beta.types.CrossInstanceReplicationConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class CrossInstanceReplicationConfig (0.5.5) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.5 (latest)  0.5.4  0.4.0  0.3.0  0.2.0  0.1.3 
    
    
    CrossInstanceReplicationConfig(
        mapping=None, *, ignore_unknown_fields=False, **kwargs
    )

Cross instance replication config.

## Attributes  
  
---  
**Name** | **Description**  
`instance_role` |  `[google.cloud.memorystore_v1beta.types.CrossInstanceReplicationConfig.InstanceRole](https://docs.cloud.google.com/python/docs/reference/google-cloud-memorystore/latest/google.cloud.memorystore_v1beta.types.CrossInstanceReplicationConfig.InstanceRole)`   
Required. The role of the instance in cross instance replication.   
`primary_instance` |  `[google.cloud.memorystore_v1beta.types.CrossInstanceReplicationConfig.RemoteInstance](https://docs.cloud.google.com/python/docs/reference/google-cloud-memorystore/latest/google.cloud.memorystore_v1beta.types.CrossInstanceReplicationConfig.RemoteInstance)`   
Optional. Details of the primary instance that is used as the replication source for this secondary instance. This field is only set for a secondary instance.   
`secondary_instances` |  `MutableSequence[[google.cloud.memorystore_v1beta.types.CrossInstanceReplicationConfig.RemoteInstance](https://docs.cloud.google.com/python/docs/reference/google-cloud-memorystore/latest/google.cloud.memorystore_v1beta.types.CrossInstanceReplicationConfig.RemoteInstance)]`   
Optional. List of secondary instances that are replicating from this primary instance. This field is only set for a primary instance.   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The last time cross instance replication config was updated.   
`membership` |  `[google.cloud.memorystore_v1beta.types.CrossInstanceReplicationConfig.Membership](https://docs.cloud.google.com/python/docs/reference/google-cloud-memorystore/latest/google.cloud.memorystore_v1beta.types.CrossInstanceReplicationConfig.Membership)`   
Output only. An output only view of all the member instances participating in the cross instance replication. This view will be provided by every member instance irrespective of its instance role(primary or secondary). A primary instance can provide information about all the secondary instances replicating from it. However, a secondary instance only knows about the primary instance from which it is replicating. However, for scenarios, where the primary instance is unavailable(e.g. regional outage), a Getinstance request can be sent to any other member instance and this field will list all the member instances participating in cross instance replication.   
  
## Classes 

### InstanceRole
    
    
    InstanceRole(value)

The role of the instance in cross instance replication.

### Membership
    
    
    Membership(mapping=None, *, ignore_unknown_fields=False, **kwargs)

An output only view of all the member instances participating in the cross instance replication.

### RemoteInstance
    
    
    RemoteInstance(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Details of the remote instance associated with this instance in a cross instance replication setup.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
