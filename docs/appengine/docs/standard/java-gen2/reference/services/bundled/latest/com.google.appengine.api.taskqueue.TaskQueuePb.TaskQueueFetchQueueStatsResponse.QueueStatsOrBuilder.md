---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskQueuePb.TaskQueueFetchQueueStatsResponse.QueueStatsOrBuilder
title: Interface TaskQueuePb.TaskQueueFetchQueueStatsResponse.QueueStatsOrBuilder (3.0.2) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:16:01.490110+00:00
---

# Interface TaskQueuePb.TaskQueueFetchQueueStatsResponse.QueueStatsOrBuilder (3.0.2)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskQueuePb.TaskQueueFetchQueueStatsResponse.QueueStatsOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)



Send feedback 

#  Interface TaskQueuePb.TaskQueueFetchQueueStatsResponse.QueueStatsOrBuilder (3.0.2) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public static interface TaskQueuePb.TaskQueueFetchQueueStatsResponse.QueueStatsOrBuilder extends MessageOrBuilder

## Implements

com.google.protobuf.MessageOrBuilder

## Methods 

### getNumTasks()
    
    
    public abstract int getNumTasks()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getOldestEtaUsec()
    
    
    public abstract long getOldestEtaUsec()

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getScannerInfo()
    
    
    public abstract TaskQueuePb.TaskQueueScannerQueueInfo getScannerInfo()

**Returns**  
---  
**Type** | **Description**  
`[TaskQueueScannerQueueInfo](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskQueuePb.TaskQueueScannerQueueInfo)` |   
  
### getScannerInfoOrBuilder()
    
    
    public abstract TaskQueuePb.TaskQueueScannerQueueInfoOrBuilder getScannerInfoOrBuilder()

**Returns**  
---  
**Type** | **Description**  
`[TaskQueueScannerQueueInfoOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskQueuePb.TaskQueueScannerQueueInfoOrBuilder)` |   
  
### hasNumTasks()
    
    
    public abstract boolean hasNumTasks()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### hasOldestEtaUsec()
    
    
    public abstract boolean hasOldestEtaUsec()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### hasScannerInfo()
    
    
    public abstract boolean hasScannerInfo()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-06 UTC."],[],[]] 
