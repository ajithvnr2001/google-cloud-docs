---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.CrossInstanceReplicationConfig.MembershipOrBuilder
title: Interface CrossInstanceReplicationConfig.MembershipOrBuilder (0.45.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:27:02.453522+00:00
---

# Interface CrossInstanceReplicationConfig.MembershipOrBuilder (0.45.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.CrossInstanceReplicationConfig.MembershipOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface CrossInstanceReplicationConfig.MembershipOrBuilder (0.45.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.45.0 (latest)  0.41.0  0.40.0  0.39.0  0.37.0  0.34.0  0.33.0  0.31.0  0.29.0  0.28.0  0.26.0  0.24.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.16.0  0.14.0  0.13.0  0.10.0  0.9.0  0.8.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static interface CrossInstanceReplicationConfig.MembershipOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getPrimaryInstance()
    
    
    public abstract CrossInstanceReplicationConfig.RemoteInstance getPrimaryInstance()

Output only. The primary instance that acts as the source of replication for the secondary instances.

` .google.cloud.memorystore.v1.CrossInstanceReplicationConfig.RemoteInstance primary_instance = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[CrossInstanceReplicationConfig.RemoteInstance](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.CrossInstanceReplicationConfig.RemoteInstance)` | The primaryInstance.  
  
### getPrimaryInstanceOrBuilder()
    
    
    public abstract CrossInstanceReplicationConfig.RemoteInstanceOrBuilder getPrimaryInstanceOrBuilder()

Output only. The primary instance that acts as the source of replication for the secondary instances.

` .google.cloud.memorystore.v1.CrossInstanceReplicationConfig.RemoteInstance primary_instance = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[CrossInstanceReplicationConfig.RemoteInstanceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.CrossInstanceReplicationConfig.RemoteInstanceOrBuilder)` |   
  
### getSecondaryInstances(int index)
    
    
    public abstract CrossInstanceReplicationConfig.RemoteInstance getSecondaryInstances(int index)

Output only. The list of secondary instances replicating from the primary instance.

` repeated .google.cloud.memorystore.v1.CrossInstanceReplicationConfig.RemoteInstance secondary_instances = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CrossInstanceReplicationConfig.RemoteInstance](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.CrossInstanceReplicationConfig.RemoteInstance)` |   
  
### getSecondaryInstancesCount()
    
    
    public abstract int getSecondaryInstancesCount()

Output only. The list of secondary instances replicating from the primary instance.

` repeated .google.cloud.memorystore.v1.CrossInstanceReplicationConfig.RemoteInstance secondary_instances = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getSecondaryInstancesList()
    
    
    public abstract List<CrossInstanceReplicationConfig.RemoteInstance> getSecondaryInstancesList()

Output only. The list of secondary instances replicating from the primary instance.

` repeated .google.cloud.memorystore.v1.CrossInstanceReplicationConfig.RemoteInstance secondary_instances = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[RemoteInstance](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.CrossInstanceReplicationConfig.RemoteInstance)>` |   
  
### getSecondaryInstancesOrBuilder(int index)
    
    
    public abstract CrossInstanceReplicationConfig.RemoteInstanceOrBuilder getSecondaryInstancesOrBuilder(int index)

Output only. The list of secondary instances replicating from the primary instance.

` repeated .google.cloud.memorystore.v1.CrossInstanceReplicationConfig.RemoteInstance secondary_instances = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CrossInstanceReplicationConfig.RemoteInstanceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.CrossInstanceReplicationConfig.RemoteInstanceOrBuilder)` |   
  
### getSecondaryInstancesOrBuilderList()
    
    
    public abstract List<? extends CrossInstanceReplicationConfig.RemoteInstanceOrBuilder> getSecondaryInstancesOrBuilderList()

Output only. The list of secondary instances replicating from the primary instance.

` repeated .google.cloud.memorystore.v1.CrossInstanceReplicationConfig.RemoteInstance secondary_instances = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.memorystore.v1.CrossInstanceReplicationConfig.RemoteInstanceOrBuilder>` |   
  
### hasPrimaryInstance()
    
    
    public abstract boolean hasPrimaryInstance()

Output only. The primary instance that acts as the source of replication for the secondary instances.

` .google.cloud.memorystore.v1.CrossInstanceReplicationConfig.RemoteInstance primary_instance = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the primaryInstance field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
