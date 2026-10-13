---
url: https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.alloydb.v1.Cluster.State
title: Enum Cluster.State (0.16.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:12:49.519472+00:00
---

# Enum Cluster.State (0.16.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.alloydb.v1.Cluster.State

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Enum Cluster.State (0.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 0.16.0 (latest) ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.alloydb.v1.Cluster.State)
  * [ 0.15.0 ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/0.15.0/com.google.events.cloud.alloydb.v1.Cluster.State)
  * [ 0.14.1 ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/0.14.1/com.google.events.cloud.alloydb.v1.Cluster.State)


    
    
    public enum Cluster.State extends Enum<Cluster.State> implements ProtocolMessageEnum

Cluster State

Protobuf enum `google.events.cloud.alloydb.v1.Cluster.State`

## Implements

[ProtocolMessageEnum](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ProtocolMessageEnum.html)

## Inherited Members

[Enum.<T>valueOf(Class<T>,String)](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#valueOf-java.lang.Class-java.lang.String-)

[Enum.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#clone--)

[Enum.compareTo(E)](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#compareTo-E-)

[Enum.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#equals-java.lang.Object-)

[Enum.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#finalize--)

[Enum.getDeclaringClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#getDeclaringClass--)

[Enum.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#hashCode--)

[Enum.name()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#name--)

[Enum.ordinal()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#ordinal--)

[Enum.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#toString--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Static Fields   
  
---  
**Name** | **Description**  
`BOOTSTRAPPING` |  The cluster is bootstrapping with data from some other source. Direct mutations to the cluster (e.g. adding read pool) are not allowed. `BOOTSTRAPPING = 7;`  
`BOOTSTRAPPING_VALUE` |  The cluster is bootstrapping with data from some other source. Direct mutations to the cluster (e.g. adding read pool) are not allowed. `BOOTSTRAPPING = 7;`  
`CREATING` |  The cluster is being created. `CREATING = 4;`  
`CREATING_VALUE` |  The cluster is being created. `CREATING = 4;`  
`DELETING` |  The cluster is being deleted. `DELETING = 5;`  
`DELETING_VALUE` |  The cluster is being deleted. `DELETING = 5;`  
`EMPTY` |  The cluster is empty and has no associated resources. All instances, associated storage and backups have been deleted. `EMPTY = 3;`  
`EMPTY_VALUE` |  The cluster is empty and has no associated resources. All instances, associated storage and backups have been deleted. `EMPTY = 3;`  
`FAILED` |  The creation of the cluster failed. `FAILED = 6;`  
`FAILED_VALUE` |  The creation of the cluster failed. `FAILED = 6;`  
`MAINTENANCE` |  The cluster is under maintenance. AlloyDB regularly performs maintenance and upgrades on customer clusters. Updates on the cluster are not allowed while the cluster is in this state. `MAINTENANCE = 8;`  
`MAINTENANCE_VALUE` |  The cluster is under maintenance. AlloyDB regularly performs maintenance and upgrades on customer clusters. Updates on the cluster are not allowed while the cluster is in this state. `MAINTENANCE = 8;`  
`PROMOTING` |  The cluster is being promoted. `PROMOTING = 9;`  
`PROMOTING_VALUE` |  The cluster is being promoted. `PROMOTING = 9;`  
`READY` |  The cluster is active and running. `READY = 1;`  
`READY_VALUE` |  The cluster is active and running. `READY = 1;`  
`STATE_UNSPECIFIED` |  The state of the cluster is unknown. `STATE_UNSPECIFIED = 0;`  
`STATE_UNSPECIFIED_VALUE` |  The state of the cluster is unknown. `STATE_UNSPECIFIED = 0;`  
`STOPPED` |  The cluster is stopped. All instances in the cluster are stopped. Customers can start a stopped cluster at any point and all their instances will come back to life with same names and IP resources. In this state, customer pays for storage. Associated backups could also be present in a stopped cluster. `STOPPED = 2;`  
`STOPPED_VALUE` |  The cluster is stopped. All instances in the cluster are stopped. Customers can start a stopped cluster at any point and all their instances will come back to life with same names and IP resources. In this state, customer pays for storage. Associated backups could also be present in a stopped cluster. `STOPPED = 2;`  
`UNRECOGNIZED` |   
  
## Static Methods   
  
---  
**Name** | **Description**  
`forNumber(int value)` |   
`getDescriptor()` |   
`internalGetValueMap()` |   
`valueOf(Descriptors.EnumValueDescriptor desc)` |   
`valueOf(int value)` | **Deprecated.** _Use[#forNumber(int)](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.alloydb.v1.Cluster.State#com_google_events_cloud_alloydb_v1_Cluster_State_forNumber_int_) instead._  
`valueOf(String name)` |   
`values()` |   
  
## Methods   
  
---  
**Name** | **Description**  
`getDescriptorForType()` |   
`getNumber()` |   
`getValueDescriptor()` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
