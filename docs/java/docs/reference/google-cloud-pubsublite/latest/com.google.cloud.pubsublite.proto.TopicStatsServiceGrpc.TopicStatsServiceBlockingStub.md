---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.TopicStatsServiceGrpc.TopicStatsServiceBlockingStub
title: Class TopicStatsServiceGrpc.TopicStatsServiceBlockingStub (1.16.5) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:34:53.232946+00:00
---

# Class TopicStatsServiceGrpc.TopicStatsServiceBlockingStub (1.16.5)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.TopicStatsServiceGrpc.TopicStatsServiceBlockingStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class TopicStatsServiceGrpc.TopicStatsServiceBlockingStub (1.16.5) Stay organized with collections  Save and categorize content based on your preferences. 

1.16.5 (latest)  1.16.2  1.15.21  1.14.8  1.13.8  1.12.22  1.11.2  1.10.0  1.9.4  1.8.0  1.7.1  1.6.3  1.5.5  1.4.12 
    
    
    public static final class TopicStatsServiceGrpc.TopicStatsServiceBlockingStub extends AbstractBlockingStub<TopicStatsServiceGrpc.TopicStatsServiceBlockingStub>

A stub to allow clients to do limited synchronous rpc calls to service TopicStatsService.

This service allows users to get stats about messages in their topic.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractBlockingStub > TopicStatsServiceGrpc.TopicStatsServiceBlockingStub

## Inherited Members

io.grpc.stub.AbstractBlockingStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel)

io.grpc.stub.AbstractBlockingStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel,io.grpc.CallOptions)

io.grpc.stub.AbstractStub.<T>withOption(io.grpc.CallOptions.Key<T>,T)

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

io.grpc.stub.AbstractStub.getCallOptions()

io.grpc.stub.AbstractStub.getChannel()

io.grpc.stub.AbstractStub.withCallCredentials(io.grpc.CallCredentials)

io.grpc.stub.AbstractStub.withChannel(io.grpc.Channel)

io.grpc.stub.AbstractStub.withCompression(java.lang.String)

io.grpc.stub.AbstractStub.withDeadline(io.grpc.Deadline)

io.grpc.stub.AbstractStub.withDeadlineAfter(java.time.Duration)

io.grpc.stub.AbstractStub.withDeadlineAfter(long,java.util.concurrent.TimeUnit)

io.grpc.stub.AbstractStub.withExecutor(java.util.concurrent.Executor)

io.grpc.stub.AbstractStub.withInterceptors(io.grpc.ClientInterceptor...)

io.grpc.stub.AbstractStub.withMaxInboundMessageSize(int)

io.grpc.stub.AbstractStub.withMaxOutboundMessageSize(int)

io.grpc.stub.AbstractStub.withOnReadyThreshold(int)

io.grpc.stub.AbstractStub.withWaitForReady()

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

## Methods 

### build(Channel channel, CallOptions callOptions)
    
    
    protected TopicStatsServiceGrpc.TopicStatsServiceBlockingStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[TopicStatsServiceGrpc.TopicStatsServiceBlockingStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.TopicStatsServiceGrpc.TopicStatsServiceBlockingStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### computeHeadCursor(ComputeHeadCursorRequest request)
    
    
    public ComputeHeadCursorResponse computeHeadCursor(ComputeHeadCursorRequest request)

Compute the head cursor for the partition. The head cursor's offset is guaranteed to be less than or equal to all messages which have not yet been acknowledged as published, and greater than the offset of any message whose publish has already been acknowledged. It is zero if there have never been messages in the partition.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ComputeHeadCursorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.ComputeHeadCursorRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ComputeHeadCursorResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.ComputeHeadCursorResponse)` |   
  
### computeMessageStats(ComputeMessageStatsRequest request)
    
    
    public ComputeMessageStatsResponse computeMessageStats(ComputeMessageStatsRequest request)

Compute statistics about a range of messages in a given topic and partition.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ComputeMessageStatsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.ComputeMessageStatsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ComputeMessageStatsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.ComputeMessageStatsResponse)` |   
  
### computeTimeCursor(ComputeTimeCursorRequest request)
    
    
    public ComputeTimeCursorResponse computeTimeCursor(ComputeTimeCursorRequest request)

Compute the corresponding cursor for a publish or event time in a topic partition.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ComputeTimeCursorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.ComputeTimeCursorRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ComputeTimeCursorResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.ComputeTimeCursorResponse)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-26 UTC."],[],[]] 
