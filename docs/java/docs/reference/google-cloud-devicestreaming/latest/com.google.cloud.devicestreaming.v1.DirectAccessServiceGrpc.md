---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-devicestreaming/latest/com.google.cloud.devicestreaming.v1.DirectAccessServiceGrpc
title: Class DirectAccessServiceGrpc (0.39.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:00:59.647737+00:00
---

# Class DirectAccessServiceGrpc (0.39.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-devicestreaming/latest/com.google.cloud.devicestreaming.v1.DirectAccessServiceGrpc

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class DirectAccessServiceGrpc (0.39.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.39.0 (latest)  0.35.0  0.34.0  0.33.0  0.31.0  0.28.0  0.27.0  0.25.0  0.23.0  0.22.0  0.21.0  0.20.0  0.18.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.10.0  0.8.0  0.7.0  0.4.0  0.3.0  0.2.0 
    
    
    public final class DirectAccessServiceGrpc

A service for allocating Android devices and interacting with the live-allocated devices. Each Session will wait for available capacity, at a higher priority over Test Execution. When allocated, the session will be exposed through a stream for integration. DirectAccessService is currently available as a preview to select developers. You can register today on behalf of you and your team at <https://developer.android.com/studio/preview/android-device-streaming>

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > DirectAccessServiceGrpc

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

### bindService(DirectAccessServiceGrpc.AsyncService service)
    
    
    public static final ServerServiceDefinition bindService(DirectAccessServiceGrpc.AsyncService service)

**Parameter**  
---  
**Name** | **Description**  
`service` | `[DirectAccessServiceGrpc.AsyncService](https://docs.cloud.google.com/java/docs/reference/google-cloud-devicestreaming/latest/com.google.cloud.devicestreaming.v1.DirectAccessServiceGrpc.AsyncService)`  
  
**Returns**  
---  
**Type** | **Description**  
`io.grpc.ServerServiceDefinition` |   
  
### getAdbConnectMethod()
    
    
    public static MethodDescriptor<AdbMessage,DeviceMessage> getAdbConnectMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[AdbMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-devicestreaming/latest/com.google.cloud.devicestreaming.v1.AdbMessage),[DeviceMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-devicestreaming/latest/com.google.cloud.devicestreaming.v1.DeviceMessage)>` |   
  
### getCancelDeviceSessionMethod()
    
    
    public static MethodDescriptor<CancelDeviceSessionRequest,Empty> getCancelDeviceSessionMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CancelDeviceSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-devicestreaming/latest/com.google.cloud.devicestreaming.v1.CancelDeviceSessionRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getCreateDeviceSessionMethod()
    
    
    public static MethodDescriptor<CreateDeviceSessionRequest,DeviceSession> getCreateDeviceSessionMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CreateDeviceSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-devicestreaming/latest/com.google.cloud.devicestreaming.v1.CreateDeviceSessionRequest),[DeviceSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-devicestreaming/latest/com.google.cloud.devicestreaming.v1.DeviceSession)>` |   
  
### getGetDeviceSessionMethod()
    
    
    public static MethodDescriptor<GetDeviceSessionRequest,DeviceSession> getGetDeviceSessionMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetDeviceSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-devicestreaming/latest/com.google.cloud.devicestreaming.v1.GetDeviceSessionRequest),[DeviceSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-devicestreaming/latest/com.google.cloud.devicestreaming.v1.DeviceSession)>` |   
  
### getListDeviceSessionsMethod()
    
    
    public static MethodDescriptor<ListDeviceSessionsRequest,ListDeviceSessionsResponse> getListDeviceSessionsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListDeviceSessionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-devicestreaming/latest/com.google.cloud.devicestreaming.v1.ListDeviceSessionsRequest),[ListDeviceSessionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-devicestreaming/latest/com.google.cloud.devicestreaming.v1.ListDeviceSessionsResponse)>` |   
  
### getServiceDescriptor()
    
    
    public static ServiceDescriptor getServiceDescriptor()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.ServiceDescriptor` |   
  
### getUpdateDeviceSessionMethod()
    
    
    public static MethodDescriptor<UpdateDeviceSessionRequest,DeviceSession> getUpdateDeviceSessionMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[UpdateDeviceSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-devicestreaming/latest/com.google.cloud.devicestreaming.v1.UpdateDeviceSessionRequest),[DeviceSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-devicestreaming/latest/com.google.cloud.devicestreaming.v1.DeviceSession)>` |   
  
### newBlockingStub(Channel channel)
    
    
    public static DirectAccessServiceGrpc.DirectAccessServiceBlockingStub newBlockingStub(Channel channel)

Creates a new blocking-style stub that supports unary and streaming output calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[DirectAccessServiceGrpc.DirectAccessServiceBlockingStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-devicestreaming/latest/com.google.cloud.devicestreaming.v1.DirectAccessServiceGrpc.DirectAccessServiceBlockingStub)` |   
  
### newBlockingV2Stub(Channel channel)
    
    
    public static DirectAccessServiceGrpc.DirectAccessServiceBlockingV2Stub newBlockingV2Stub(Channel channel)

Creates a new blocking-style stub that supports all types of calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[DirectAccessServiceGrpc.DirectAccessServiceBlockingV2Stub](https://docs.cloud.google.com/java/docs/reference/google-cloud-devicestreaming/latest/com.google.cloud.devicestreaming.v1.DirectAccessServiceGrpc.DirectAccessServiceBlockingV2Stub)` |   
  
### newFutureStub(Channel channel)
    
    
    public static DirectAccessServiceGrpc.DirectAccessServiceFutureStub newFutureStub(Channel channel)

Creates a new ListenableFuture-style stub that supports unary calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[DirectAccessServiceGrpc.DirectAccessServiceFutureStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-devicestreaming/latest/com.google.cloud.devicestreaming.v1.DirectAccessServiceGrpc.DirectAccessServiceFutureStub)` |   
  
### newStub(Channel channel)
    
    
    public static DirectAccessServiceGrpc.DirectAccessServiceStub newStub(Channel channel)

Creates a new async stub that supports all call types for the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[DirectAccessServiceGrpc.DirectAccessServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-devicestreaming/latest/com.google.cloud.devicestreaming.v1.DirectAccessServiceGrpc.DirectAccessServiceStub)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
