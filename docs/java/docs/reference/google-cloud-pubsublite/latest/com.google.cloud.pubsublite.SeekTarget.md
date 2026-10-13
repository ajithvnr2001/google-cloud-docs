---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SeekTarget
title: Class SeekTarget (1.16.5) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:19:14.689390+00:00
---

# Class SeekTarget (1.16.5)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SeekTarget

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class SeekTarget (1.16.5) Stay organized with collections  Save and categorize content based on your preferences. 

1.16.5 (latest)  1.16.2  1.15.21  1.14.8  1.13.8  1.12.22  1.11.2  1.10.0  1.9.4  1.8.0  1.7.1  1.6.3  1.5.5  1.4.12 
    
    
    public abstract class SeekTarget implements Serializable

The target location to seek a subscription to.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > SeekTarget

## Implements

[Serializable](https://docs.oracle.com/javase/8/docs/api/java/io/Serializable.html)

## Inherited Members

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Static Methods 

### of(BacklogLocation location)
    
    
    public static SeekTarget of(BacklogLocation location)

Seek to a named backlog location.

**Parameter**  
---  
**Name** | **Description**  
`location` | `[BacklogLocation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.BacklogLocation)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SeekTarget](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SeekTarget)` |   
  
### ofEventTime(Timestamp time)
    
    
    public static SeekTarget ofEventTime(Timestamp time)

Seek to a message event timestamp.

**Parameter**  
---  
**Name** | **Description**  
`time` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SeekTarget](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SeekTarget)` |   
  
### ofPublishTime(Timestamp time)
    
    
    public static SeekTarget ofPublishTime(Timestamp time)

Seek to a message publish timestamp.

**Parameter**  
---  
**Name** | **Description**  
`time` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SeekTarget](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SeekTarget)` |   
  
## Constructors 

### SeekTarget()
    
    
    public SeekTarget()

## Methods 

### backlogLocation()
    
    
    public abstract BacklogLocation backlogLocation()

**Returns**  
---  
**Type** | **Description**  
`[BacklogLocation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.BacklogLocation)` |   
  
### eventTime()
    
    
    public abstract Timestamp eventTime()

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` |   
  
### getKind()
    
    
    public abstract SeekTarget.Kind getKind()

**Returns**  
---  
**Type** | **Description**  
`[SeekTarget.Kind](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SeekTarget.Kind)` |   
  
### publishTime()
    
    
    public abstract Timestamp publishTime()

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-26 UTC."],[],[]] 
