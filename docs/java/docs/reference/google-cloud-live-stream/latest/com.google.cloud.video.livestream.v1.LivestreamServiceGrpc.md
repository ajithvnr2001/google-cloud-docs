---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.LivestreamServiceGrpc
title: Class LivestreamServiceGrpc (0.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:28:26.494368+00:00
---

# Class LivestreamServiceGrpc (0.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.LivestreamServiceGrpc

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class LivestreamServiceGrpc (0.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.101.0 (latest)  0.97.0  0.96.0  0.95.0  0.93.0  0.90.0  0.89.0  0.87.0  0.85.0  0.84.0  0.82.0  0.80.0  0.78.0  0.77.0  0.76.0  0.75.0  0.74.0  0.72.0  0.70.0  0.69.0  0.66.0  0.65.0  0.64.0  0.62.0  0.61.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.8  0.3.0 
    
    
    public final class LivestreamServiceGrpc

Using Live Stream API, you can generate live streams in the various renditions and streaming formats. The streaming format include HTTP Live Streaming (HLS) and Dynamic Adaptive Streaming over HTTP (DASH). You can send a source stream in the various ways, including Real-Time Messaging Protocol (RTMP) and Secure Reliable Transport (SRT).

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > LivestreamServiceGrpc

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

### bindService(LivestreamServiceGrpc.AsyncService service)
    
    
    public static final ServerServiceDefinition bindService(LivestreamServiceGrpc.AsyncService service)

**Parameter**  
---  
**Name** | **Description**  
`service` | `[LivestreamServiceGrpc.AsyncService](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.LivestreamServiceGrpc.AsyncService)`  
  
**Returns**  
---  
**Type** | **Description**  
`io.grpc.ServerServiceDefinition` |   
  
### getCreateAssetMethod()
    
    
    public static MethodDescriptor<CreateAssetRequest,Operation> getCreateAssetMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CreateAssetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.CreateAssetRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getCreateChannelMethod()
    
    
    public static MethodDescriptor<CreateChannelRequest,Operation> getCreateChannelMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CreateChannelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.CreateChannelRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getCreateClipMethod()
    
    
    public static MethodDescriptor<CreateClipRequest,Operation> getCreateClipMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CreateClipRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.CreateClipRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getCreateDvrSessionMethod()
    
    
    public static MethodDescriptor<CreateDvrSessionRequest,Operation> getCreateDvrSessionMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CreateDvrSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.CreateDvrSessionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getCreateEventMethod()
    
    
    public static MethodDescriptor<CreateEventRequest,Event> getCreateEventMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CreateEventRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.CreateEventRequest),[Event](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Event)>` |   
  
### getCreateInputMethod()
    
    
    public static MethodDescriptor<CreateInputRequest,Operation> getCreateInputMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CreateInputRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.CreateInputRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getDeleteAssetMethod()
    
    
    public static MethodDescriptor<DeleteAssetRequest,Operation> getDeleteAssetMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[DeleteAssetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.DeleteAssetRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getDeleteChannelMethod()
    
    
    public static MethodDescriptor<DeleteChannelRequest,Operation> getDeleteChannelMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[DeleteChannelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.DeleteChannelRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getDeleteClipMethod()
    
    
    public static MethodDescriptor<DeleteClipRequest,Operation> getDeleteClipMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[DeleteClipRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.DeleteClipRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getDeleteDvrSessionMethod()
    
    
    public static MethodDescriptor<DeleteDvrSessionRequest,Operation> getDeleteDvrSessionMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[DeleteDvrSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.DeleteDvrSessionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getDeleteEventMethod()
    
    
    public static MethodDescriptor<DeleteEventRequest,Empty> getDeleteEventMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[DeleteEventRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.DeleteEventRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getDeleteInputMethod()
    
    
    public static MethodDescriptor<DeleteInputRequest,Operation> getDeleteInputMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[DeleteInputRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.DeleteInputRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getGetAssetMethod()
    
    
    public static MethodDescriptor<GetAssetRequest,Asset> getGetAssetMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetAssetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.GetAssetRequest),[Asset](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Asset)>` |   
  
### getGetChannelMethod()
    
    
    public static MethodDescriptor<GetChannelRequest,Channel> getGetChannelMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetChannelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.GetChannelRequest),[Channel](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Channel)>` |   
  
### getGetClipMethod()
    
    
    public static MethodDescriptor<GetClipRequest,Clip> getGetClipMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetClipRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.GetClipRequest),[Clip](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Clip)>` |   
  
### getGetDvrSessionMethod()
    
    
    public static MethodDescriptor<GetDvrSessionRequest,DvrSession> getGetDvrSessionMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetDvrSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.GetDvrSessionRequest),[DvrSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.DvrSession)>` |   
  
### getGetEventMethod()
    
    
    public static MethodDescriptor<GetEventRequest,Event> getGetEventMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetEventRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.GetEventRequest),[Event](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Event)>` |   
  
### getGetInputMethod()
    
    
    public static MethodDescriptor<GetInputRequest,Input> getGetInputMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetInputRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.GetInputRequest),[Input](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Input)>` |   
  
### getGetPoolMethod()
    
    
    public static MethodDescriptor<GetPoolRequest,Pool> getGetPoolMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.GetPoolRequest),[Pool](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Pool)>` |   
  
### getListAssetsMethod()
    
    
    public static MethodDescriptor<ListAssetsRequest,ListAssetsResponse> getListAssetsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListAssetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.ListAssetsRequest),[ListAssetsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.ListAssetsResponse)>` |   
  
### getListChannelsMethod()
    
    
    public static MethodDescriptor<ListChannelsRequest,ListChannelsResponse> getListChannelsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListChannelsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.ListChannelsRequest),[ListChannelsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.ListChannelsResponse)>` |   
  
### getListClipsMethod()
    
    
    public static MethodDescriptor<ListClipsRequest,ListClipsResponse> getListClipsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListClipsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.ListClipsRequest),[ListClipsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.ListClipsResponse)>` |   
  
### getListDvrSessionsMethod()
    
    
    public static MethodDescriptor<ListDvrSessionsRequest,ListDvrSessionsResponse> getListDvrSessionsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListDvrSessionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.ListDvrSessionsRequest),[ListDvrSessionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.ListDvrSessionsResponse)>` |   
  
### getListEventsMethod()
    
    
    public static MethodDescriptor<ListEventsRequest,ListEventsResponse> getListEventsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListEventsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.ListEventsRequest),[ListEventsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.ListEventsResponse)>` |   
  
### getListInputsMethod()
    
    
    public static MethodDescriptor<ListInputsRequest,ListInputsResponse> getListInputsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListInputsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.ListInputsRequest),[ListInputsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.ListInputsResponse)>` |   
  
### getPreviewInputMethod()
    
    
    public static MethodDescriptor<PreviewInputRequest,PreviewInputResponse> getPreviewInputMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[PreviewInputRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.PreviewInputRequest),[PreviewInputResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.PreviewInputResponse)>` |   
  
### getServiceDescriptor()
    
    
    public static ServiceDescriptor getServiceDescriptor()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.ServiceDescriptor` |   
  
### getStartChannelMethod()
    
    
    public static MethodDescriptor<StartChannelRequest,Operation> getStartChannelMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[StartChannelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.StartChannelRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getStartDistributionMethod()
    
    
    public static MethodDescriptor<StartDistributionRequest,Operation> getStartDistributionMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[StartDistributionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.StartDistributionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getStopChannelMethod()
    
    
    public static MethodDescriptor<StopChannelRequest,Operation> getStopChannelMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[StopChannelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.StopChannelRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getStopDistributionMethod()
    
    
    public static MethodDescriptor<StopDistributionRequest,Operation> getStopDistributionMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[StopDistributionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.StopDistributionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getUpdateChannelMethod()
    
    
    public static MethodDescriptor<UpdateChannelRequest,Operation> getUpdateChannelMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[UpdateChannelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.UpdateChannelRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getUpdateDvrSessionMethod()
    
    
    public static MethodDescriptor<UpdateDvrSessionRequest,Operation> getUpdateDvrSessionMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[UpdateDvrSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.UpdateDvrSessionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getUpdateInputMethod()
    
    
    public static MethodDescriptor<UpdateInputRequest,Operation> getUpdateInputMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[UpdateInputRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.UpdateInputRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getUpdatePoolMethod()
    
    
    public static MethodDescriptor<UpdatePoolRequest,Operation> getUpdatePoolMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[UpdatePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.UpdatePoolRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### newBlockingStub(Channel channel)
    
    
    public static LivestreamServiceGrpc.LivestreamServiceBlockingStub newBlockingStub(Channel channel)

Creates a new blocking-style stub that supports unary and streaming output calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[LivestreamServiceGrpc.LivestreamServiceBlockingStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.LivestreamServiceGrpc.LivestreamServiceBlockingStub)` |   
  
### newBlockingV2Stub(Channel channel)
    
    
    public static LivestreamServiceGrpc.LivestreamServiceBlockingV2Stub newBlockingV2Stub(Channel channel)

Creates a new blocking-style stub that supports all types of calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[LivestreamServiceGrpc.LivestreamServiceBlockingV2Stub](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.LivestreamServiceGrpc.LivestreamServiceBlockingV2Stub)` |   
  
### newFutureStub(Channel channel)
    
    
    public static LivestreamServiceGrpc.LivestreamServiceFutureStub newFutureStub(Channel channel)

Creates a new ListenableFuture-style stub that supports unary calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[LivestreamServiceGrpc.LivestreamServiceFutureStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.LivestreamServiceGrpc.LivestreamServiceFutureStub)` |   
  
### newStub(Channel channel)
    
    
    public static LivestreamServiceGrpc.LivestreamServiceStub newStub(Channel channel)

Creates a new async stub that supports all call types for the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[LivestreamServiceGrpc.LivestreamServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.LivestreamServiceGrpc.LivestreamServiceStub)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
