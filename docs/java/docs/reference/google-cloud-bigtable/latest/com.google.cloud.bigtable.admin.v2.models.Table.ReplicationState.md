---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.models.Table.ReplicationState
title: Enum Table.ReplicationState (2.85.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:01:45.505310+00:00
---

# Enum Table.ReplicationState (2.85.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.models.Table.ReplicationState

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Enum Table.ReplicationState (2.85.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.85.0 (latest)  2.81.0  2.80.0  2.79.0  2.78.1  2.77.0  2.74.0  2.73.0  2.72.0  2.71.0  2.70.0  2.68.0  2.67.1  2.66.0  2.65.1  2.63.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.2  2.56.0  2.54.0  2.52.0  2.51.2  2.49.0  2.46.0  2.45.1  2.44.1  2.43.0  2.42.0  2.40.0  2.39.5  2.37.0  2.35.1  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.1  2.28.0 
    
    
    public enum Table.ReplicationState extends Enum<Table.ReplicationState>

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
`INITIALIZING` | The cluster was recently created, and the table must finish copying over pre-existing data from other clusters before it can begin receiving live replication updates and serving Data API requests.  
`NOT_KNOWN` | The replication state of the table is unknown in this cluster.  
`PLANNED_MAINTENANCE` | The table is temporarily unable to serve Data API requests from this cluster due to planned internal maintenance.  
`READY` | The table can serve Data API requests from this cluster. Depending on replication delay, reads may not immediately reflect the state of the table in other clusters.  
`READY_OPTIMIZING` | The table is fully created and ready for use after a restore, and is being optimized for performance. When optimizations are complete, the table will transition to`READY` state.  
`UNPLANNED_MAINTENANCE` | The table is temporarily unable to serve Data API requests from this cluster due to unplanned or emergency maintenance.  
`UNRECOGNIZED` | The replication state of table is not known by this client. Please upgrade your client.  
  
## Static Methods   
  
---  
**Name** | **Description**  
`fromProto(Table.ClusterState.ReplicationState proto)` | **Internal Only** : This feature is not stable for application use. Wraps the protobuf. This method is considered an internal implementation detail and not meant to be used by applications.  
`valueOf(String name)` |   
`values()` |   
  
## Methods   
  
---  
**Name** | **Description**  
`toProto()` | **Internal Only** : This feature is not stable for application use. Creates the request protobuf. This method is considered an internal implementation detail and not meant to be used by applications.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
