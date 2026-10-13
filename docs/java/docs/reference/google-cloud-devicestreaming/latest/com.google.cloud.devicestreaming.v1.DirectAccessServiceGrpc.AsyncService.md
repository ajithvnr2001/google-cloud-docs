---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-devicestreaming/latest/com.google.cloud.devicestreaming.v1.DirectAccessServiceGrpc.AsyncService
title: Interface DirectAccessServiceGrpc.AsyncService (0.39.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:18:09.770468+00:00
---

# Interface DirectAccessServiceGrpc.AsyncService (0.39.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-devicestreaming/latest/com.google.cloud.devicestreaming.v1.DirectAccessServiceGrpc.AsyncService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface DirectAccessServiceGrpc.AsyncService (0.39.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.39.0 (latest)  0.35.0  0.34.0  0.33.0  0.31.0  0.28.0  0.27.0  0.25.0  0.23.0  0.22.0  0.21.0  0.20.0  0.18.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.10.0  0.8.0  0.7.0  0.4.0  0.3.0  0.2.0 
    
    
    public static interface DirectAccessServiceGrpc.AsyncService

A service for allocating Android devices and interacting with the live-allocated devices. Each Session will wait for available capacity, at a higher priority over Test Execution. When allocated, the session will be exposed through a stream for integration. DirectAccessService is currently available as a preview to select developers. You can register today on behalf of you and your team at <https://developer.android.com/studio/preview/android-device-streaming>

## Methods 

### adbConnect(StreamObserver<DeviceMessage> responseObserver)
    
    
    public default StreamObserver<AdbMessage> adbConnect(StreamObserver<DeviceMessage> responseObserver)

Exposes an ADB connection if the device supports ADB. gRPC headers are used to authenticate the Connect RPC, as well as associate to a particular DeviceSession. In particular, the user must specify the "X-Omnilab-Session-Name" header.

**Parameter**  
---  
**Name** | **Description**  
`responseObserver` | `io.grpc.stub.StreamObserver<[DeviceMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-devicestreaming/latest/com.google.cloud.devicestreaming.v1.DeviceMessage)>`  
  
**Returns**  
---  
**Type** | **Description**  
`io.grpc.stub.StreamObserver<[AdbMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-devicestreaming/latest/com.google.cloud.devicestreaming.v1.AdbMessage)>` |   
  
### cancelDeviceSession(CancelDeviceSessionRequest request, StreamObserver<Empty> responseObserver)
    
    
    public default void cancelDeviceSession(CancelDeviceSessionRequest request, StreamObserver<Empty> responseObserver)

Cancel a DeviceSession. This RPC changes the DeviceSession to state FINISHED and terminates all connections. Canceled sessions are not deleted and can be retrieved or listed by the user until they expire based on the 28 day deletion policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CancelDeviceSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-devicestreaming/latest/com.google.cloud.devicestreaming.v1.CancelDeviceSessionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### createDeviceSession(CreateDeviceSessionRequest request, StreamObserver<DeviceSession> responseObserver)
    
    
    public default void createDeviceSession(CreateDeviceSessionRequest request, StreamObserver<DeviceSession> responseObserver)

Creates a DeviceSession.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDeviceSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-devicestreaming/latest/com.google.cloud.devicestreaming.v1.CreateDeviceSessionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[DeviceSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-devicestreaming/latest/com.google.cloud.devicestreaming.v1.DeviceSession)>`  
  
  
### getDeviceSession(GetDeviceSessionRequest request, StreamObserver<DeviceSession> responseObserver)
    
    
    public default void getDeviceSession(GetDeviceSessionRequest request, StreamObserver<DeviceSession> responseObserver)

Gets a DeviceSession, which documents the allocation status and whether the device is allocated. Clients making requests from this API must poll GetDeviceSession.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDeviceSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-devicestreaming/latest/com.google.cloud.devicestreaming.v1.GetDeviceSessionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[DeviceSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-devicestreaming/latest/com.google.cloud.devicestreaming.v1.DeviceSession)>`  
  
  
### listDeviceSessions(ListDeviceSessionsRequest request, StreamObserver<ListDeviceSessionsResponse> responseObserver)
    
    
    public default void listDeviceSessions(ListDeviceSessionsRequest request, StreamObserver<ListDeviceSessionsResponse> responseObserver)

Lists DeviceSessions owned by the project user.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDeviceSessionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-devicestreaming/latest/com.google.cloud.devicestreaming.v1.ListDeviceSessionsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListDeviceSessionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-devicestreaming/latest/com.google.cloud.devicestreaming.v1.ListDeviceSessionsResponse)>`  
  
  
### updateDeviceSession(UpdateDeviceSessionRequest request, StreamObserver<DeviceSession> responseObserver)
    
    
    public default void updateDeviceSession(UpdateDeviceSessionRequest request, StreamObserver<DeviceSession> responseObserver)

Updates the current DeviceSession to the fields described by the update_mask.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDeviceSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-devicestreaming/latest/com.google.cloud.devicestreaming.v1.UpdateDeviceSessionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[DeviceSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-devicestreaming/latest/com.google.cloud.devicestreaming.v1.DeviceSession)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
