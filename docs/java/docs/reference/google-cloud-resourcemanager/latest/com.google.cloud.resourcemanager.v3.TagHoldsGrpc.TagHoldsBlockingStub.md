---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.TagHoldsGrpc.TagHoldsBlockingStub
title: Class TagHoldsGrpc.TagHoldsBlockingStub (1.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:56:35.573784+00:00
---

# Class TagHoldsGrpc.TagHoldsBlockingStub (1.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.TagHoldsGrpc.TagHoldsBlockingStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class TagHoldsGrpc.TagHoldsBlockingStub (1.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.101.0 (latest)  1.97.0  1.96.0  1.95.0  1.93.0  1.90.0  1.89.0  1.87.0  1.85.0  1.84.0  1.82.0  1.80.0  1.78.0  1.77.0  1.76.0  1.75.0  1.74.0  1.72.0  1.70.0  1.69.0  1.66.0  1.65.0  1.64.0  1.62.0  1.61.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.51.0  1.50.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.39.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.6  1.4.0  1.3.2  1.2.12 
    
    
    public static final class TagHoldsGrpc.TagHoldsBlockingStub extends AbstractBlockingStub<TagHoldsGrpc.TagHoldsBlockingStub>

A stub to allow clients to do limited synchronous rpc calls to service TagHolds.

Allow users to create and manage TagHolds for TagValues. TagHolds represent the use of a Tag Value that is not captured by TagBindings but should still block TagValue deletion (such as a reference in a policy condition). This service provides isolated failure domains by cloud location so that TagHolds can be managed in the same location as their usage.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractBlockingStub > TagHoldsGrpc.TagHoldsBlockingStub

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
    
    
    protected TagHoldsGrpc.TagHoldsBlockingStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[TagHoldsGrpc.TagHoldsBlockingStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.TagHoldsGrpc.TagHoldsBlockingStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createTagHold(CreateTagHoldRequest request)
    
    
    public Operation createTagHold(CreateTagHoldRequest request)

Creates a TagHold. Returns ALREADY_EXISTS if a TagHold with the same resource and origin exists under the same TagValue.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateTagHoldRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.CreateTagHoldRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### deleteTagHold(DeleteTagHoldRequest request)
    
    
    public Operation deleteTagHold(DeleteTagHoldRequest request)

Deletes a TagHold.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteTagHoldRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.DeleteTagHoldRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### listTagHolds(ListTagHoldsRequest request)
    
    
    public ListTagHoldsResponse listTagHolds(ListTagHoldsRequest request)

Lists TagHolds under a TagValue.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListTagHoldsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ListTagHoldsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListTagHoldsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ListTagHoldsResponse)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
