---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskQueuePb.TaskQueueAddRequestOrBuilder
title: Interface TaskQueuePb.TaskQueueAddRequestOrBuilder (3.0.2) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T06:10:30.051426+00:00
---

# Interface TaskQueuePb.TaskQueueAddRequestOrBuilder (3.0.2)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskQueuePb.TaskQueueAddRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)



Send feedback 

#  Interface TaskQueuePb.TaskQueueAddRequestOrBuilder (3.0.2) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public static interface TaskQueuePb.TaskQueueAddRequestOrBuilder extends MessageOrBuilder

## Implements

com.google.protobuf.MessageOrBuilder

## Methods 

### getAppId()
    
    
    public abstract ByteString getAppId()

**Returns**  
---  
**Type** | **Description**  
`com.google.protobuf.ByteString` |   
  
### getBody()
    
    
    public abstract ByteString getBody()

**Returns**  
---  
**Type** | **Description**  
`com.google.protobuf.ByteString` |   
  
### getCronRetryParameters()
    
    
    public abstract TaskQueuePb.TaskQueueRetryParameters getCronRetryParameters()

**Returns**  
---  
**Type** | **Description**  
`[TaskQueueRetryParameters](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskQueuePb.TaskQueueRetryParameters)` |   
  
### getCronRetryParametersOrBuilder()
    
    
    public abstract TaskQueuePb.TaskQueueRetryParametersOrBuilder getCronRetryParametersOrBuilder()

**Returns**  
---  
**Type** | **Description**  
`[TaskQueueRetryParametersOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskQueuePb.TaskQueueRetryParametersOrBuilder)` |   
  
### getCronTimetable()
    
    
    public abstract TaskQueuePb.TaskQueueAddRequest.CronTimetable getCronTimetable()

**Returns**  
---  
**Type** | **Description**  
`[CronTimetable](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskQueuePb.TaskQueueAddRequest.CronTimetable)` |   
  
### getCronTimetableOrBuilder()
    
    
    public abstract TaskQueuePb.TaskQueueAddRequest.CronTimetableOrBuilder getCronTimetableOrBuilder()

**Returns**  
---  
**Type** | **Description**  
`[CronTimetableOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskQueuePb.TaskQueueAddRequest.CronTimetableOrBuilder)` |   
  
### getDatastoreTransaction()
    
    
    public abstract ByteString getDatastoreTransaction()

**Returns**  
---  
**Type** | **Description**  
`com.google.protobuf.ByteString` |   
  
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
  
### getHeader(int arg0)
    
    
    public abstract TaskQueuePb.TaskQueueAddRequest.Header getHeader(int arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Header](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskQueuePb.TaskQueueAddRequest.Header)` |   
  
### getHeaderCount()
    
    
    public abstract int getHeaderCount()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getHeaderList()
    
    
    public abstract List<TaskQueuePb.TaskQueueAddRequest.Header> getHeaderList()

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Header](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskQueuePb.TaskQueueAddRequest.Header)>` |   
  
### getHeaderOrBuilder(int arg0)
    
    
    public abstract TaskQueuePb.TaskQueueAddRequest.HeaderOrBuilder getHeaderOrBuilder(int arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HeaderOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskQueuePb.TaskQueueAddRequest.HeaderOrBuilder)` |   
  
### getHeaderOrBuilderList()
    
    
    public abstract List<? extends TaskQueuePb.TaskQueueAddRequest.HeaderOrBuilder> getHeaderOrBuilderList()

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.appengine.api.taskqueue.TaskQueuePb.TaskQueueAddRequest.HeaderOrBuilder>` |   
  
### getMethod()
    
    
    public abstract TaskQueuePb.TaskQueueAddRequest.RequestMethod getMethod()

**Returns**  
---  
**Type** | **Description**  
`[RequestMethod](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskQueuePb.TaskQueueAddRequest.RequestMethod)` |   
  
### getMode()
    
    
    public abstract TaskQueuePb.TaskQueueMode.Mode getMode()

**Returns**  
---  
**Type** | **Description**  
`[Mode](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskQueuePb.TaskQueueMode.Mode)` |   
  
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
  
### getQueueName()
    
    
    public abstract ByteString getQueueName()

**Returns**  
---  
**Type** | **Description**  
`com.google.protobuf.ByteString` |   
  
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
  
### getTransaction()
    
    
    public abstract DatastoreV3Pb.Transaction getTransaction()

**Returns**  
---  
**Type** | **Description**  
`com.google.apphosting.datastore.proto2api.DatastoreV3Pb.Transaction` |   
  
### getTransactionOrBuilder()
    
    
    public abstract DatastoreV3Pb.TransactionOrBuilder getTransactionOrBuilder()

**Returns**  
---  
**Type** | **Description**  
`com.google.apphosting.datastore.proto2api.DatastoreV3Pb.TransactionOrBuilder` |   
  
### getUrl()
    
    
    public abstract ByteString getUrl()

**Returns**  
---  
**Type** | **Description**  
`com.google.protobuf.ByteString` |   
  
### hasAppId()
    
    
    public abstract boolean hasAppId()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### hasBody()
    
    
    public abstract boolean hasBody()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### hasCronRetryParameters()
    
    
    public abstract boolean hasCronRetryParameters()

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
  
### hasDatastoreTransaction()
    
    
    public abstract boolean hasDatastoreTransaction()

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
  
### hasMethod()
    
    
    public abstract boolean hasMethod()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### hasMode()
    
    
    public abstract boolean hasMode()

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
  
### hasQueueName()
    
    
    public abstract boolean hasQueueName()

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
  
### hasTransaction()
    
    
    public abstract boolean hasTransaction()

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
