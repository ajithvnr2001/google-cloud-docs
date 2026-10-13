---
url: https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.batch.v1.JobNotificationOrBuilder
title: Interface JobNotificationOrBuilder (0.16.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:53:59.943862+00:00
---

# Interface JobNotificationOrBuilder (0.16.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.batch.v1.JobNotificationOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface JobNotificationOrBuilder (0.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 0.16.0 (latest) ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.batch.v1.JobNotificationOrBuilder)
  * [ 0.15.0 ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/0.15.0/com.google.events.cloud.batch.v1.JobNotificationOrBuilder)
  * [ 0.14.1 ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/0.14.1/com.google.events.cloud.batch.v1.JobNotificationOrBuilder)


    
    
    public interface JobNotificationOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getMessage()
    
    
    public abstract JobNotification.Message getMessage()

The attribute requirements of messages to be sent to this Pub/Sub topic. Without this field, no message will be sent.

`.google.events.cloud.batch.v1.JobNotification.Message message = 2;`

**Returns**  
---  
**Type** | **Description**  
`[JobNotification.Message](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.batch.v1.JobNotification.Message)` | The message.  
  
### getMessageOrBuilder()
    
    
    public abstract JobNotification.MessageOrBuilder getMessageOrBuilder()

The attribute requirements of messages to be sent to this Pub/Sub topic. Without this field, no message will be sent.

`.google.events.cloud.batch.v1.JobNotification.Message message = 2;`

**Returns**  
---  
**Type** | **Description**  
`[JobNotification.MessageOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.batch.v1.JobNotification.MessageOrBuilder)` |   
  
### getPubsubTopic()
    
    
    public abstract String getPubsubTopic()

The Pub/Sub topic where notifications like the job state changes will be published. This topic exist in the same project as the job and billings will be charged to this project. If not specified, no Pub/Sub messages will be sent. Topic format: `projects/{project}/topics/{topic}`.

`string pubsub_topic = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The pubsubTopic.  
  
### getPubsubTopicBytes()
    
    
    public abstract ByteString getPubsubTopicBytes()

The Pub/Sub topic where notifications like the job state changes will be published. This topic exist in the same project as the job and billings will be charged to this project. If not specified, no Pub/Sub messages will be sent. Topic format: `projects/{project}/topics/{topic}`.

`string pubsub_topic = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for pubsubTopic.  
  
### hasMessage()
    
    
    public abstract boolean hasMessage()

The attribute requirements of messages to be sent to this Pub/Sub topic. Without this field, no message will be sent.

`.google.events.cloud.batch.v1.JobNotification.Message message = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the message field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
