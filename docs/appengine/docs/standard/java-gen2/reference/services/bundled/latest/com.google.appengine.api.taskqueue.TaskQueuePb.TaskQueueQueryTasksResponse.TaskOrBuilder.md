---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskQueuePb.TaskQueueQueryTasksResponse.TaskOrBuilder
title: Interface TaskQueuePb.TaskQueueQueryTasksResponse.TaskOrBuilder (3.0.2) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:07:25.329395+00:00
---

# Interface TaskQueuePb.TaskQueueQueryTasksResponse.TaskOrBuilder (3.0.2)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskQueuePb.TaskQueueQueryTasksResponse.TaskOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)



Send feedback 

#  Interface TaskQueuePb.TaskQueueQueryTasksResponse.TaskOrBuilder (3.0.2) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public static interface TaskQueuePb.TaskQueueQueryTasksResponse.TaskOrBuilder extends MessageOrBuilder

## Implements

com.google.protobuf.MessageOrBuilder

## Methods 

### getBody()
    
    
    public abstract ByteString getBody()

**Returns**  
---  
**Type** | **Description**  
`com.google.protobuf.ByteString` |   
  
### getBodySize()
    
    
    public abstract int getBodySize()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getCreationTimeUsec()
    
    
    public abstract long getCreationTimeUsec()

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getCronTimetable()
    
    
    public abstract TaskQueuePb.TaskQueueQueryTasksResponse.Task.CronTimetable getCronTimetable()

**Returns**  
---  
**Type** | **Description**  
`[CronTimetable](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskQueuePb.TaskQueueQueryTasksResponse.Task.CronTimetable)` |   
  
### getCronTimetableOrBuilder()
    
    
    public abstract TaskQueuePb.TaskQueueQueryTasksResponse.Task.CronTimetableOrBuilder getCronTimetableOrBuilder()

**Returns**  
---  
**Type** | **Description**  
`[CronTimetableOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskQueuePb.TaskQueueQueryTasksResponse.Task.CronTimetableOrBuilder)` |   
  
### getDescription()
    
    
    public abstract ByteString getDescription()

**Returns**  
---  
**Type** | **Description**  
`com.google.protobuf.ByteString` |   
  
### getDispatchDeadlineUsec()
    
    
    public abstract long getDispatchDeadlineUsec()

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getEtaUsec()
    
    
    public abstract long getEtaUsec()

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getExecutionCount()
    
    
    public abstract int getExecutionCount()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getFirstTryUsec()
    
    
    public abstract long getFirstTryUsec()

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getHeader(int arg0)
    
    
    public abstract TaskQueuePb.TaskQueueQueryTasksResponse.Task.Header getHeader(int arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Header](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskQueuePb.TaskQueueQueryTasksResponse.Task.Header)` |   
  
### getHeaderCount()
    
    
    public abstract int getHeaderCount()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getHeaderList()
    
    
    public abstract List<TaskQueuePb.TaskQueueQueryTasksResponse.Task.Header> getHeaderList()

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Header](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskQueuePb.TaskQueueQueryTasksResponse.Task.Header)>` |   
  
### getHeaderOrBuilder(int arg0)
    
    
    public abstract TaskQueuePb.TaskQueueQueryTasksResponse.Task.HeaderOrBuilder getHeaderOrBuilder(int arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HeaderOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskQueuePb.TaskQueueQueryTasksResponse.Task.HeaderOrBuilder)` |   
  
### getHeaderOrBuilderList()
    
    
    public abstract List<? extends TaskQueuePb.TaskQueueQueryTasksResponse.Task.HeaderOrBuilder> getHeaderOrBuilderList()

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.appengine.api.taskqueue.TaskQueuePb.TaskQueueQueryTasksResponse.Task.HeaderOrBuilder>` |   
  
### getMethod()
    
    
    public abstract TaskQueuePb.TaskQueueQueryTasksResponse.Task.RequestMethod getMethod()

**Returns**  
---  
**Type** | **Description**  
`[RequestMethod](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskQueuePb.TaskQueueQueryTasksResponse.Task.RequestMethod)` |   
  
### getPayload()
    
    
    public abstract TaskQueuePb.TaskPayload getPayload()

**Returns**  
---  
**Type** | **Description**  
`[TaskPayload](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskQueuePb.TaskPayload)` |   
  
### getPayloadOrBuilder()
    
    
    public abstract TaskQueuePb.TaskPayloadOrBuilder getPayloadOrBuilder()

**Returns**  
---  
**Type** | **Description**  
`[TaskPayloadOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskQueuePb.TaskPayloadOrBuilder)` |   
  
### getRetryCount()
    
    
    public abstract int getRetryCount()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getRetryParameters()
    
    
    public abstract TaskQueuePb.TaskQueueRetryParameters getRetryParameters()

**Returns**  
---  
**Type** | **Description**  
`[TaskQueueRetryParameters](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskQueuePb.TaskQueueRetryParameters)` |   
  
### getRetryParametersOrBuilder()
    
    
    public abstract TaskQueuePb.TaskQueueRetryParametersOrBuilder getRetryParametersOrBuilder()

**Returns**  
---  
**Type** | **Description**  
`[TaskQueueRetryParametersOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskQueuePb.TaskQueueRetryParametersOrBuilder)` |   
  
### getRunLog()
    
    
    public abstract TaskQueuePb.TaskQueueQueryTasksResponse.Task.RunLog getRunLog()

**Returns**  
---  
**Type** | **Description**  
`[RunLog](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskQueuePb.TaskQueueQueryTasksResponse.Task.RunLog)` |   
  
### getRunLogOrBuilder()
    
    
    public abstract TaskQueuePb.TaskQueueQueryTasksResponse.Task.RunLogOrBuilder getRunLogOrBuilder()

**Returns**  
---  
**Type** | **Description**  
`[RunLogOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskQueuePb.TaskQueueQueryTasksResponse.Task.RunLogOrBuilder)` |   
  
### getTag()
    
    
    public abstract ByteString getTag()

**Returns**  
---  
**Type** | **Description**  
`com.google.protobuf.ByteString` |   
  
### getTaskName()
    
    
    public abstract ByteString getTaskName()

**Returns**  
---  
**Type** | **Description**  
`com.google.protobuf.ByteString` |   
  
### getUrl()
    
    
    public abstract ByteString getUrl()

**Returns**  
---  
**Type** | **Description**  
`com.google.protobuf.ByteString` |   
  
### hasBody()
    
    
    public abstract boolean hasBody()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### hasBodySize()
    
    
    public abstract boolean hasBodySize()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### hasCreationTimeUsec()
    
    
    public abstract boolean hasCreationTimeUsec()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### hasCronTimetable()
    
    
    public abstract boolean hasCronTimetable()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### hasDescription()
    
    
    public abstract boolean hasDescription()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### hasDispatchDeadlineUsec()
    
    
    public abstract boolean hasDispatchDeadlineUsec()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### hasEtaUsec()
    
    
    public abstract boolean hasEtaUsec()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### hasExecutionCount()
    
    
    public abstract boolean hasExecutionCount()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### hasFirstTryUsec()
    
    
    public abstract boolean hasFirstTryUsec()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### hasMethod()
    
    
    public abstract boolean hasMethod()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### hasPayload()
    
    
    public abstract boolean hasPayload()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### hasRetryCount()
    
    
    public abstract boolean hasRetryCount()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### hasRetryParameters()
    
    
    public abstract boolean hasRetryParameters()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### hasRunLog()
    
    
    public abstract boolean hasRunLog()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### hasTag()
    
    
    public abstract boolean hasTag()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### hasTaskName()
    
    
    public abstract boolean hasTaskName()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### hasUrl()
    
    
    public abstract boolean hasUrl()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-06 UTC."],[],[]] 
