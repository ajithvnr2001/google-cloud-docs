---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskQueuePb.TaskQueueFetchQueuesResponseOrBuilder
title: Interface TaskQueuePb.TaskQueueFetchQueuesResponseOrBuilder (3.0.2) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:37:19.620876+00:00
---

# Interface TaskQueuePb.TaskQueueFetchQueuesResponseOrBuilder (3.0.2)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskQueuePb.TaskQueueFetchQueuesResponseOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)



Send feedback 

#  Interface TaskQueuePb.TaskQueueFetchQueuesResponseOrBuilder (3.0.2) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public static interface TaskQueuePb.TaskQueueFetchQueuesResponseOrBuilder extends MessageOrBuilder

## Implements

com.google.protobuf.MessageOrBuilder

## Methods 

### getQueue(int arg0)
    
    
    public abstract TaskQueuePb.TaskQueueFetchQueuesResponse.Queue getQueue(int arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Queue](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskQueuePb.TaskQueueFetchQueuesResponse.Queue)` |   
  
### getQueueCount()
    
    
    public abstract int getQueueCount()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getQueueList()
    
    
    public abstract List<TaskQueuePb.TaskQueueFetchQueuesResponse.Queue> getQueueList()

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Queue](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskQueuePb.TaskQueueFetchQueuesResponse.Queue)>` |   
  
### getQueueOrBuilder(int arg0)
    
    
    public abstract TaskQueuePb.TaskQueueFetchQueuesResponse.QueueOrBuilder getQueueOrBuilder(int arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[QueueOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskQueuePb.TaskQueueFetchQueuesResponse.QueueOrBuilder)` |   
  
### getQueueOrBuilderList()
    
    
    public abstract List<? extends TaskQueuePb.TaskQueueFetchQueuesResponse.QueueOrBuilder> getQueueOrBuilderList()

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.appengine.api.taskqueue.TaskQueuePb.TaskQueueFetchQueuesResponse.QueueOrBuilder>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-06 UTC."],[],[]] 
