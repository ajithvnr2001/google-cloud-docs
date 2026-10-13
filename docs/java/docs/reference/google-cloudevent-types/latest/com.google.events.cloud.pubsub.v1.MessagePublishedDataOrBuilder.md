---
url: https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.pubsub.v1.MessagePublishedDataOrBuilder
title: Interface MessagePublishedDataOrBuilder (0.16.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:23:41.110882+00:00
---

# Interface MessagePublishedDataOrBuilder (0.16.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.pubsub.v1.MessagePublishedDataOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface MessagePublishedDataOrBuilder (0.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 0.16.0 (latest) ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.pubsub.v1.MessagePublishedDataOrBuilder)
  * [ 0.15.0 ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/0.15.0/com.google.events.cloud.pubsub.v1.MessagePublishedDataOrBuilder)
  * [ 0.14.1 ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/0.14.1/com.google.events.cloud.pubsub.v1.MessagePublishedDataOrBuilder)


    
    
    public interface MessagePublishedDataOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getMessage()
    
    
    public abstract PubsubMessage getMessage()

The message that was published.

`.google.events.cloud.pubsub.v1.PubsubMessage message = 1;`

**Returns**  
---  
**Type** | **Description**  
`[PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.pubsub.v1.PubsubMessage)` | The message.  
  
### getMessageOrBuilder()
    
    
    public abstract PubsubMessageOrBuilder getMessageOrBuilder()

The message that was published.

`.google.events.cloud.pubsub.v1.PubsubMessage message = 1;`

**Returns**  
---  
**Type** | **Description**  
`[PubsubMessageOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.pubsub.v1.PubsubMessageOrBuilder)` |   
  
### getSubscription()
    
    
    public abstract String getSubscription()

The resource name of the subscription for which this event was generated. The format of the value is `projects/{project-id}/subscriptions/{subscription-id}`.

`string subscription = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The subscription.  
  
### getSubscriptionBytes()
    
    
    public abstract ByteString getSubscriptionBytes()

The resource name of the subscription for which this event was generated. The format of the value is `projects/{project-id}/subscriptions/{subscription-id}`.

`string subscription = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for subscription.  
  
### hasMessage()
    
    
    public abstract boolean hasMessage()

The message that was published.

`.google.events.cloud.pubsub.v1.PubsubMessage message = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the message field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
