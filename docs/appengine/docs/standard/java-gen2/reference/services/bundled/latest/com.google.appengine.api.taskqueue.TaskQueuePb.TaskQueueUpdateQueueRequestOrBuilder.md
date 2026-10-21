---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskQueuePb.TaskQueueUpdateQueueRequestOrBuilder
title: Interface TaskQueuePb.TaskQueueUpdateQueueRequestOrBuilder (3.0.2) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:52:05.563991+00:00
---

# Interface TaskQueuePb.TaskQueueUpdateQueueRequestOrBuilder (3.0.2)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskQueuePb.TaskQueueUpdateQueueRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)



Send feedback 

#  Interface TaskQueuePb.TaskQueueUpdateQueueRequestOrBuilder (3.0.2) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public static interface TaskQueuePb.TaskQueueUpdateQueueRequestOrBuilder extends MessageOrBuilder

## Implements

com.google.protobuf.MessageOrBuilder

## Methods 

### getAcl()
    
    
    public abstract TaskQueuePb.TaskQueueAcl getAcl()

**Returns**  
---  
**Type** | **Description**  
`[TaskQueueAcl](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskQueuePb.TaskQueueAcl)` |   
  
### getAclOrBuilder()
    
    
    public abstract TaskQueuePb.TaskQueueAclOrBuilder getAclOrBuilder()

**Returns**  
---  
**Type** | **Description**  
`[TaskQueueAclOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskQueuePb.TaskQueueAclOrBuilder)` |   
  
### getAppId()
    
    
    public abstract ByteString getAppId()

**Returns**  
---  
**Type** | **Description**  
`com.google.protobuf.ByteString` |   
  
### getBucketCapacity()
    
    
    public abstract int getBucketCapacity()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getBucketRefillPerSecond()
    
    
    public abstract double getBucketRefillPerSecond()

**Returns**  
---  
**Type** | **Description**  
`[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getHeaderOverride(int arg0)
    
    
    public abstract TaskQueuePb.TaskQueueHttpHeader getHeaderOverride(int arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TaskQueueHttpHeader](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskQueuePb.TaskQueueHttpHeader)` |   
  
### getHeaderOverrideCount()
    
    
    public abstract int getHeaderOverrideCount()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getHeaderOverrideList()
    
    
    public abstract List<TaskQueuePb.TaskQueueHttpHeader> getHeaderOverrideList()

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[TaskQueueHttpHeader](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskQueuePb.TaskQueueHttpHeader)>` |   
  
### getHeaderOverrideOrBuilder(int arg0)
    
    
    public abstract TaskQueuePb.TaskQueueHttpHeaderOrBuilder getHeaderOverrideOrBuilder(int arg0)

**Parameter**  
---  
**Name** | **Description**  
`arg0` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TaskQueueHttpHeaderOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskQueuePb.TaskQueueHttpHeaderOrBuilder)` |   
  
### getHeaderOverrideOrBuilderList()
    
    
    public abstract List<? extends TaskQueuePb.TaskQueueHttpHeaderOrBuilder> getHeaderOverrideOrBuilderList()

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.appengine.api.taskqueue.TaskQueuePb.TaskQueueHttpHeaderOrBuilder>` |   
  
### getMaxConcurrentRequests()
    
    
    public abstract int getMaxConcurrentRequests()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getMode()
    
    
    public abstract TaskQueuePb.TaskQueueMode.Mode getMode()

**Returns**  
---  
**Type** | **Description**  
`[Mode](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskQueuePb.TaskQueueMode.Mode)` |   
  
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
  
### getUserSpecifiedRate()
    
    
    public abstract String getUserSpecifiedRate()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getUserSpecifiedRateBytes()
    
    
    public abstract ByteString getUserSpecifiedRateBytes()

**Returns**  
---  
**Type** | **Description**  
`com.google.protobuf.ByteString` |   
  
### hasAcl()
    
    
    public abstract boolean hasAcl()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### hasAppId()
    
    
    public abstract boolean hasAppId()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### hasBucketCapacity()
    
    
    public abstract boolean hasBucketCapacity()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### hasBucketRefillPerSecond()
    
    
    public abstract boolean hasBucketRefillPerSecond()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### hasMaxConcurrentRequests()
    
    
    public abstract boolean hasMaxConcurrentRequests()

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
  
### hasUserSpecifiedRate()
    
    
    public abstract boolean hasUserSpecifiedRate()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-06 UTC."],[],[]] 
