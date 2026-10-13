---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.StreamingServiceGrpc.StreamingServiceStub
title: Class StreamingServiceGrpc.StreamingServiceStub (0.56.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:52:30.691043+00:00
---

# Class StreamingServiceGrpc.StreamingServiceStub (0.56.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.StreamingServiceGrpc.StreamingServiceStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class StreamingServiceGrpc.StreamingServiceStub (0.56.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.56.0 (latest)  0.52.0  0.51.0  0.50.0  0.48.0  0.45.0  0.44.0  0.42.0  0.40.0  0.39.0  0.37.0  0.35.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.27.0  0.25.0  0.24.0  0.21.0  0.20.0  0.19.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static final class StreamingServiceGrpc.StreamingServiceStub extends AbstractAsyncStub<StreamingServiceGrpc.StreamingServiceStub>

A stub to allow clients to do asynchronous rpc calls to service StreamingService.

Streaming service for receiving and sending packets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractAsyncStub > StreamingServiceGrpc.StreamingServiceStub

## Inherited Members

io.grpc.stub.AbstractAsyncStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel)

io.grpc.stub.AbstractAsyncStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel,io.grpc.CallOptions)

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

### acquireLease(AcquireLeaseRequest request, StreamObserver<Lease> responseObserver)
    
    
    public void acquireLease(AcquireLeaseRequest request, StreamObserver<Lease> responseObserver)

AcquireLease acquires a lease.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AcquireLeaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.AcquireLeaseRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Lease](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Lease)>`  
  
  
### build(Channel channel, CallOptions callOptions)
    
    
    protected StreamingServiceGrpc.StreamingServiceStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[StreamingServiceGrpc.StreamingServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.StreamingServiceGrpc.StreamingServiceStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### receiveEvents(StreamObserver<ReceiveEventsResponse> responseObserver)
    
    
    public StreamObserver<ReceiveEventsRequest> receiveEvents(StreamObserver<ReceiveEventsResponse> responseObserver)

Receive events given the stream name.

**Parameter**  
---  
**Name** | **Description**  
`responseObserver` | `io.grpc.stub.StreamObserver<[ReceiveEventsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.ReceiveEventsResponse)>`  
  
**Returns**  
---  
**Type** | **Description**  
`io.grpc.stub.StreamObserver<[ReceiveEventsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.ReceiveEventsRequest)>` |   
  
### receivePackets(StreamObserver<ReceivePacketsResponse> responseObserver)
    
    
    public StreamObserver<ReceivePacketsRequest> receivePackets(StreamObserver<ReceivePacketsResponse> responseObserver)

Receive packets from the series.

**Parameter**  
---  
**Name** | **Description**  
`responseObserver` | `io.grpc.stub.StreamObserver<[ReceivePacketsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.ReceivePacketsResponse)>`  
  
**Returns**  
---  
**Type** | **Description**  
`io.grpc.stub.StreamObserver<[ReceivePacketsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.ReceivePacketsRequest)>` |   
  
### releaseLease(ReleaseLeaseRequest request, StreamObserver<ReleaseLeaseResponse> responseObserver)
    
    
    public void releaseLease(ReleaseLeaseRequest request, StreamObserver<ReleaseLeaseResponse> responseObserver)

RleaseLease releases a lease.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ReleaseLeaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.ReleaseLeaseRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ReleaseLeaseResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.ReleaseLeaseResponse)>`  
  
  
### renewLease(RenewLeaseRequest request, StreamObserver<Lease> responseObserver)
    
    
    public void renewLease(RenewLeaseRequest request, StreamObserver<Lease> responseObserver)

RenewLease renews a lease.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RenewLeaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.RenewLeaseRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Lease](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Lease)>`  
  
  
### sendPackets(StreamObserver<SendPacketsResponse> responseObserver)
    
    
    public StreamObserver<SendPacketsRequest> sendPackets(StreamObserver<SendPacketsResponse> responseObserver)

Send packets to the series.

**Parameter**  
---  
**Name** | **Description**  
`responseObserver` | `io.grpc.stub.StreamObserver<[SendPacketsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.SendPacketsResponse)>`  
  
**Returns**  
---  
**Type** | **Description**  
`io.grpc.stub.StreamObserver<[SendPacketsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.SendPacketsRequest)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
