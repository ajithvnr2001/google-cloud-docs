---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.StreamingServiceGrpc
title: Class StreamingServiceGrpc (0.56.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:26:33.238357+00:00
---

# Class StreamingServiceGrpc (0.56.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.StreamingServiceGrpc

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class StreamingServiceGrpc (0.56.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.56.0 (latest)  0.52.0  0.51.0  0.50.0  0.48.0  0.45.0  0.44.0  0.42.0  0.40.0  0.39.0  0.37.0  0.35.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.27.0  0.25.0  0.24.0  0.21.0  0.20.0  0.19.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public final class StreamingServiceGrpc

Streaming service for receiving and sending packets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > StreamingServiceGrpc

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

## Static Fields 

### SERVICE_NAME
    
    
    public static final String SERVICE_NAME

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
## Static Methods 

### bindService(StreamingServiceGrpc.AsyncService service)
    
    
    public static final ServerServiceDefinition bindService(StreamingServiceGrpc.AsyncService service)

**Parameter**  
---  
**Name** | **Description**  
`service` | `[StreamingServiceGrpc.AsyncService](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.StreamingServiceGrpc.AsyncService)`  
  
**Returns**  
---  
**Type** | **Description**  
`io.grpc.ServerServiceDefinition` |   
  
### getAcquireLeaseMethod()
    
    
    public static MethodDescriptor<AcquireLeaseRequest,Lease> getAcquireLeaseMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[AcquireLeaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.AcquireLeaseRequest),[Lease](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Lease)>` |   
  
### getReceiveEventsMethod()
    
    
    public static MethodDescriptor<ReceiveEventsRequest,ReceiveEventsResponse> getReceiveEventsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ReceiveEventsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.ReceiveEventsRequest),[ReceiveEventsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.ReceiveEventsResponse)>` |   
  
### getReceivePacketsMethod()
    
    
    public static MethodDescriptor<ReceivePacketsRequest,ReceivePacketsResponse> getReceivePacketsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ReceivePacketsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.ReceivePacketsRequest),[ReceivePacketsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.ReceivePacketsResponse)>` |   
  
### getReleaseLeaseMethod()
    
    
    public static MethodDescriptor<ReleaseLeaseRequest,ReleaseLeaseResponse> getReleaseLeaseMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ReleaseLeaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.ReleaseLeaseRequest),[ReleaseLeaseResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.ReleaseLeaseResponse)>` |   
  
### getRenewLeaseMethod()
    
    
    public static MethodDescriptor<RenewLeaseRequest,Lease> getRenewLeaseMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[RenewLeaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.RenewLeaseRequest),[Lease](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.Lease)>` |   
  
### getSendPacketsMethod()
    
    
    public static MethodDescriptor<SendPacketsRequest,SendPacketsResponse> getSendPacketsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[SendPacketsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.SendPacketsRequest),[SendPacketsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.SendPacketsResponse)>` |   
  
### getServiceDescriptor()
    
    
    public static ServiceDescriptor getServiceDescriptor()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.ServiceDescriptor` |   
  
### newBlockingStub(Channel channel)
    
    
    public static StreamingServiceGrpc.StreamingServiceBlockingStub newBlockingStub(Channel channel)

Creates a new blocking-style stub that supports unary and streaming output calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[StreamingServiceGrpc.StreamingServiceBlockingStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.StreamingServiceGrpc.StreamingServiceBlockingStub)` |   
  
### newBlockingV2Stub(Channel channel)
    
    
    public static StreamingServiceGrpc.StreamingServiceBlockingV2Stub newBlockingV2Stub(Channel channel)

Creates a new blocking-style stub that supports all types of calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[StreamingServiceGrpc.StreamingServiceBlockingV2Stub](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.StreamingServiceGrpc.StreamingServiceBlockingV2Stub)` |   
  
### newFutureStub(Channel channel)
    
    
    public static StreamingServiceGrpc.StreamingServiceFutureStub newFutureStub(Channel channel)

Creates a new ListenableFuture-style stub that supports unary calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[StreamingServiceGrpc.StreamingServiceFutureStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.StreamingServiceGrpc.StreamingServiceFutureStub)` |   
  
### newStub(Channel channel)
    
    
    public static StreamingServiceGrpc.StreamingServiceStub newStub(Channel channel)

Creates a new async stub that supports all call types for the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[StreamingServiceGrpc.StreamingServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.StreamingServiceGrpc.StreamingServiceStub)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
