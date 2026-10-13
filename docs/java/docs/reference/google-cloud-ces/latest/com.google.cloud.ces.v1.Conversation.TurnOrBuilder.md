---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.Conversation.TurnOrBuilder
title: Interface Conversation.TurnOrBuilder (0.15.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:55:07.982564+00:00
---

# Interface Conversation.TurnOrBuilder (0.15.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.Conversation.TurnOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface Conversation.TurnOrBuilder (0.15.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.15.0 (latest)  0.11.0  0.10.0  0.9.0  0.7.0  0.4.0  0.3.0  0.1.0 
    
    
    public static interface Conversation.TurnOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getMessages(int index)
    
    
    public abstract Message getMessages(int index)

Optional. List of messages in the conversation turn, including user input, agent responses and intermediate events during the processing.

` repeated .google.cloud.ces.v1.Message messages = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Message](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.Message)` |   
  
### getMessagesCount()
    
    
    public abstract int getMessagesCount()

Optional. List of messages in the conversation turn, including user input, agent responses and intermediate events during the processing.

` repeated .google.cloud.ces.v1.Message messages = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getMessagesList()
    
    
    public abstract List<Message> getMessagesList()

Optional. List of messages in the conversation turn, including user input, agent responses and intermediate events during the processing.

` repeated .google.cloud.ces.v1.Message messages = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Message](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.Message)>` |   
  
### getMessagesOrBuilder(int index)
    
    
    public abstract MessageOrBuilder getMessagesOrBuilder(int index)

Optional. List of messages in the conversation turn, including user input, agent responses and intermediate events during the processing.

` repeated .google.cloud.ces.v1.Message messages = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MessageOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.MessageOrBuilder)` |   
  
### getMessagesOrBuilderList()
    
    
    public abstract List<? extends MessageOrBuilder> getMessagesOrBuilderList()

Optional. List of messages in the conversation turn, including user input, agent responses and intermediate events during the processing.

` repeated .google.cloud.ces.v1.Message messages = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.ces.v1.MessageOrBuilder>` |   
  
### getRootSpan()
    
    
    public abstract Span getRootSpan()

Optional. The root span of the action processing.

`.google.cloud.ces.v1.Span root_span = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Span](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.Span)` | The rootSpan.  
  
### getRootSpanOrBuilder()
    
    
    public abstract SpanOrBuilder getRootSpanOrBuilder()

Optional. The root span of the action processing.

`.google.cloud.ces.v1.Span root_span = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[SpanOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.SpanOrBuilder)` |   
  
### hasRootSpan()
    
    
    public abstract boolean hasRootSpan()

Optional. The root span of the action processing.

`.google.cloud.ces.v1.Span root_span = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the rootSpan field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
