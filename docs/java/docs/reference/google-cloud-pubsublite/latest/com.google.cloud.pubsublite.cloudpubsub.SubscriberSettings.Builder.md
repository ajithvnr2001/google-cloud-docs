---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.SubscriberSettings.Builder
title: Class SubscriberSettings.Builder (1.16.5) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:19:18.955558+00:00
---

# Class SubscriberSettings.Builder (1.16.5)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.SubscriberSettings.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class SubscriberSettings.Builder (1.16.5) Stay organized with collections  Save and categorize content based on your preferences. 

1.16.5 (latest)  1.16.2  1.15.21  1.14.8  1.13.8  1.12.22  1.11.2  1.10.0  1.9.4  1.8.0  1.7.1  1.6.3  1.5.5  1.4.12 
    
    
    public abstract static class SubscriberSettings.Builder

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > SubscriberSettings.Builder

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

## Constructors 

### Builder()
    
    
    public Builder()

## Methods 

### build()
    
    
    public abstract SubscriberSettings build()

**Returns**  
---  
**Type** | **Description**  
`[SubscriberSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.SubscriberSettings)` |   
  
### setAssignmentServiceClient(PartitionAssignmentServiceClient client)
    
    
    public abstract SubscriberSettings.Builder setAssignmentServiceClient(PartitionAssignmentServiceClient client)

A client to connect to the Pub/Sub lite assignment service. If present, ignores CredentialsProvider.

**Parameter**  
---  
**Name** | **Description**  
`client` | `[PartitionAssignmentServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.v1.PartitionAssignmentServiceClient)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SubscriberSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.SubscriberSettings.Builder)` |   
  
### setCredentialsProvider(CredentialsProvider provider)
    
    
    public abstract SubscriberSettings.Builder setCredentialsProvider(CredentialsProvider provider)

A provider for credentials.

**Parameter**  
---  
**Name** | **Description**  
`provider` | `[CredentialsProvider](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.core.CredentialsProvider.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SubscriberSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.SubscriberSettings.Builder)` |   
  
### setCursorServiceClient(CursorServiceClient client)
    
    
    public abstract SubscriberSettings.Builder setCursorServiceClient(CursorServiceClient client)

A CursorServiceClient to use, if present.

**Parameter**  
---  
**Name** | **Description**  
`client` | `[CursorServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.v1.CursorServiceClient)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SubscriberSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.SubscriberSettings.Builder)` |   
  
### setFramework(PubsubContext.Framework framework)
    
    
    public abstract SubscriberSettings.Builder setFramework(PubsubContext.Framework framework)

A Framework tag for internal metrics. Please set this if integrating with a public framework!

**Parameter**  
---  
**Name** | **Description**  
`framework` | `[PubsubContext.Framework](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.internal.wire.PubsubContext.Framework)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SubscriberSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.SubscriberSettings.Builder)` |   
  
### setNackHandler(NackHandler nackHandler)
    
    
    public abstract SubscriberSettings.Builder setNackHandler(NackHandler nackHandler)

A handler for the action to take when com.google.cloud.pubsub.v1.AckReplyConsumer#nack is called. In Pub/Sub Lite, only a single subscriber for a given subscription is connected to any partition at a time, and there is no other client that may be able to handle messages.

**Parameter**  
---  
**Name** | **Description**  
`nackHandler` | `[NackHandler](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.NackHandler)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SubscriberSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.SubscriberSettings.Builder)` |   
  
### setPartitions(List<Partition> partition)
    
    
    public abstract SubscriberSettings.Builder setPartitions(List<Partition> partition)

The partitions this subscriber should connect to to receive messages. If set, disables auto-assignment.

**Parameter**  
---  
**Name** | **Description**  
`partition` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Partition](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.Partition)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[SubscriberSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.SubscriberSettings.Builder)` |   
  
### setPerPartitionFlowControlSettings(FlowControlSettings settings)
    
    
    public abstract SubscriberSettings.Builder setPerPartitionFlowControlSettings(FlowControlSettings settings)

The per-partition flow control settings. Because these apply per-partition, if you are using them to bound memory usage, keep in mind the number of partitions in the associated topic.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[FlowControlSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.FlowControlSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SubscriberSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.SubscriberSettings.Builder)` |   
  
### setReassignmentHandler(ReassignmentHandler reassignmentHandler)
    
    
    public abstract SubscriberSettings.Builder setReassignmentHandler(ReassignmentHandler reassignmentHandler)

A handler that will be notified when partition assignments change from the backend.

**Parameter**  
---  
**Name** | **Description**  
`reassignmentHandler` | `[ReassignmentHandler](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.ReassignmentHandler)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SubscriberSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.SubscriberSettings.Builder)` |   
  
### setReceiver(MessageReceiver receiver)
    
    
    public abstract SubscriberSettings.Builder setReceiver(MessageReceiver receiver)

The receiver which handles new messages sent by the Pub/Sub Lite system. Only one downcall from any connected partition will be outstanding at a time, and blocking in this receiver callback will block forward progress.

**Parameter**  
---  
**Name** | **Description**  
`receiver` | `com.google.cloud.pubsub.v1.MessageReceiver`  
  
**Returns**  
---  
**Type** | **Description**  
`[SubscriberSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.SubscriberSettings.Builder)` |   
  
### setSubscriberServiceClient(SubscriberServiceClient client)
    
    
    public abstract SubscriberSettings.Builder setSubscriberServiceClient(SubscriberServiceClient client)

A SubscriberServiceClient to use, if present.

**Parameter**  
---  
**Name** | **Description**  
`client` | `[SubscriberServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.v1.SubscriberServiceClient)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SubscriberSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.SubscriberSettings.Builder)` |   
  
### setSubscriptionPath(SubscriptionPath path)
    
    
    public abstract SubscriberSettings.Builder setSubscriptionPath(SubscriptionPath path)

The subscription to use to receive messages.

**Parameter**  
---  
**Name** | **Description**  
`path` | `[SubscriptionPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SubscriptionPath)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SubscriberSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.SubscriberSettings.Builder)` |   
  
### setTransformer(MessageTransformer<SequencedMessage,PubsubMessage> transformer)
    
    
    public abstract SubscriberSettings.Builder setTransformer(MessageTransformer<SequencedMessage,PubsubMessage> transformer)

The MessageTransformer to get PubsubMessages from Pub/Sub Lite wire messages. The messageId field must not be set on the returned message.

**Parameter**  
---  
**Name** | **Description**  
`transformer` | `[MessageTransformer](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.MessageTransformer)<[SequencedMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SequencedMessage),com.google.pubsub.v1.PubsubMessage>`  
  
**Returns**  
---  
**Type** | **Description**  
`[SubscriberSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.SubscriberSettings.Builder)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-26 UTC."],[],[]] 
